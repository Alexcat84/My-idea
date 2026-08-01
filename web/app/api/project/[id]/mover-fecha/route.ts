/**
 * POST /api/project/[id]/mover-fecha — Fase 4.7: mover la fecha objetivo de una
 * actividad pendiente, con CASCADA opcional a las que siguen.
 * body { item_id, fecha (ISO nueva), cascada: boolean }.
 *
 * - Mueve la fecha del ítem objetivo a `fecha`.
 * - Si `cascada`: corre el MISMO delta a las pendientes POSTERIORES del mismo
 *   dominio (misma etapa o posteriores, por fecha vigente; excluye hechas y
 *   no_aplica). Nada se mueve sin este flag: la oferta la confirma el usuario.
 * - Cada ítem movido CONGELA su fecha original si es su primera movida
 *   (fecha_base_original), y su origen pasa a 'ajustada' (o 'manual').
 * - Registra UNA entrada de bitácora `fecha_movida { item, delta, cascada }`.
 *
 * El cumplimiento se mide contra la fecha VIGENTE (re-baseline = control de
 * cambios); la honestidad histórica vive en analytics (línea "frente a tu plan
 * inicial", desde fecha_base_original).
 */
import { NextResponse } from "next/server";
import { obtenerProyecto, registrarBitacora } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

interface ItemFecha {
  id: string;
  dominio: string;
  etapa: number;
  estado: string;
  fecha_base: string | null;
  fecha_base_origen: string | null;
  fecha_base_original: string | null;
}

function parsear(body: unknown): { item_id: string; fecha: string; cascada: boolean } | null {
  if (typeof body !== "object" || body === null) return null;
  const b = body as { item_id?: unknown; fecha?: unknown; cascada?: unknown };
  if (typeof b.item_id !== "string") return null;
  if (typeof b.fecha !== "string" || Number.isNaN(Date.parse(b.fecha))) return null;
  return { item_id: b.item_id, fecha: new Date(Date.parse(b.fecha)).toISOString(), cascada: b.cascada === true };
}

/** El cambio de fecha_base de un ítem, respetando la regla de la historia: la
 * PRIMERA fecha se preserva en fecha_base_original y el origen pasa a 'ajustada'
 * (o 'manual' si nunca fue sugerida). */
function cambioFecha(prev: ItemFecha, nueva: string): Record<string, unknown> {
  const c: Record<string, unknown> = { fecha_base: nueva, updated_at: new Date().toISOString() };
  if (prev.fecha_base) {
    if (!prev.fecha_base_original) c.fecha_base_original = prev.fecha_base;
    c.fecha_base_origen =
      prev.fecha_base_origen === "sugerida" || prev.fecha_base_origen === "ajustada" ? "ajustada" : "manual";
  } else {
    c.fecha_base_origen = "manual";
  }
  return c;
}

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let cuerpo: unknown;
  try {
    cuerpo = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  const datos = parsear(cuerpo);
  if (!datos) {
    return NextResponse.json({ error: "falta item_id o fecha mal formada" }, { status: 400 });
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });

  // Todo el checklist del proyecto: el objetivo y sus posibles posteriores.
  const { data: filas } = await supabase
    .from("checklist_items")
    .select("id, dominio, etapa, estado, fecha_base, fecha_base_origen, fecha_base_original")
    .eq("project_id", projectId);
  const items = (filas ?? []) as ItemFecha[];
  const objetivo = items.find((i) => i.id === datos.item_id);
  if (!objetivo) return NextResponse.json({ error: "actividad no encontrada" }, { status: 404 });
  if (!objetivo.fecha_base) {
    return NextResponse.json({ error: "esta actividad no tiene una fecha que mover" }, { status: 400 });
  }

  const deltaMs = Date.parse(datos.fecha) - Date.parse(objetivo.fecha_base);

  // Mover a la MISMA fecha no es un cambio: no se escribe nada ni se registra en
  // la bitácora (regla del fundador: cambios reales, no clics).
  if (deltaMs === 0) {
    return NextResponse.json({ ok: true, movidos: 0, cascada: 0 });
  }

  // Posteriores del MISMO dominio: activas (no hechas ni retiradas), misma etapa
  // o posteriores, y programadas DESPUÉS del objetivo por su fecha vigente.
  const posteriores = datos.cascada
    ? items.filter(
        (i) =>
          i.id !== objetivo.id &&
          i.dominio === objetivo.dominio &&
          i.estado !== "hecho" &&
          i.estado !== "no_aplica" &&
          i.etapa >= objetivo.etapa &&
          i.fecha_base !== null &&
          Date.parse(i.fecha_base) > Date.parse(objetivo.fecha_base!)
      )
    : [];

  // Aplica: el objetivo a su nueva fecha; cada posterior corre el MISMO delta.
  await supabase.from("checklist_items").update(cambioFecha(objetivo, datos.fecha)).eq("id", objetivo.id).eq("project_id", projectId);
  for (const p of posteriores) {
    const nueva = new Date(Date.parse(p.fecha_base!) + deltaMs).toISOString();
    await supabase.from("checklist_items").update(cambioFecha(p, nueva)).eq("id", p.id).eq("project_id", projectId);
  }

  await registrarBitacora(supabase, projectId, "fecha_movida", {
    item: objetivo.id,
    delta_dias: Math.round(deltaMs / 86_400_000),
    cascada: datos.cascada ? posteriores.length : "solo",
  });

  return NextResponse.json({ ok: true, movidos: 1 + posteriores.length, cascada: posteriores.length });
}
