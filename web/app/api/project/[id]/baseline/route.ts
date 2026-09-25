/**
 * POST /api/project/[id]/baseline — Fase 3.8 §4: confirmar la línea base.
 * body { plan_id, fechas: [{item_id, fecha (ISO), origen}] }.
 *
 * Al confirmar: se sella plans.baseline_confirmada_at del ciclo y cada ítem
 * guarda su fecha_base + fecha_base_origen. Si un ítem YA tenía fecha_base
 * (re-confirmación tras reactivar), la primera se preserva en
 * fecha_base_original — la historia no se reescribe. La base VIGENTE de
 * lectura es la del último plan con baseline confirmada.
 *
 * El cliente manda fechas ISO ya en hora local (mediodía) para que el día
 * de calendario no dependa de la zona horaria del servidor.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_PROYECTO } from "@/lib/i18n/mensajes/servidorProyecto";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { FECHA_BASE_ORIGEN, type FechaBaseOrigen } from "@/lib/dbContract";
import { obtenerProyecto } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

interface EntradaFecha {
  item_id: string;
  fecha: string; // ISO
  origen: FechaBaseOrigen;
}

function parsear(body: unknown): { plan_id: string; fechas: EntradaFecha[] } | null {
  if (typeof body !== "object" || body === null) return null;
  const b = body as { plan_id?: unknown; fechas?: unknown };
  if (typeof b.plan_id !== "string" || !Array.isArray(b.fechas)) return null;
  const fechas: EntradaFecha[] = [];
  for (const f of b.fechas) {
    if (typeof f !== "object" || f === null) return null;
    const e = f as { item_id?: unknown; fecha?: unknown; origen?: unknown };
    if (typeof e.item_id !== "string") return null;
    if (typeof e.fecha !== "string" || Number.isNaN(Date.parse(e.fecha))) return null;
    const origen =
      typeof e.origen === "string" && (FECHA_BASE_ORIGEN as readonly string[]).includes(e.origen)
        ? (e.origen as FechaBaseOrigen)
        : "sugerida";
    fechas.push({ item_id: e.item_id, fecha: new Date(Date.parse(e.fecha)).toISOString(), origen });
  }
  return { plan_id: b.plan_id, fechas };
}

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_PROYECTO, idioma).baseline;

  let cuerpo: unknown;
  try {
    cuerpo = await request.json();
  } catch {
    return NextResponse.json({ error: r.cuerpoJsonInvalido }, { status: 400 });
  }
  const datos = parsear(cuerpo);
  if (!datos) {
    return NextResponse.json({ error: t.faltaPlanOFechas }, { status: 400 });
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });
  }

  // Estado previo de los ítems de este plan: para preservar la PRIMERA
  // fecha_base en fecha_base_original al re-confirmar (no reescribir historia).
  const { data: previos } = await supabase
    .from("checklist_items")
    .select("id, fecha_base, fecha_base_original")
    .eq("project_id", projectId)
    .eq("plan_id", datos.plan_id);
  const prevPorId = new Map(
    ((previos ?? []) as Array<{ id: string; fecha_base: string | null; fecha_base_original: string | null }>).map(
      (p) => [p.id, p]
    )
  );

  const ahora = new Date().toISOString();
  // AUD-09 (tanda 5): toda escritura que falla deja rastro. Antes estos updates
  // no miraban su error y la ruta respondía "confirmadas: N" aunque no se
  // hubiera guardado nada.
  let fallos = 0;
  for (const f of datos.fechas) {
    const prev = prevPorId.get(f.item_id);
    const cambios: Record<string, unknown> = {
      fecha_base: f.fecha,
      fecha_base_origen: f.origen,
      updated_at: ahora,
    };
    if (prev?.fecha_base && !prev.fecha_base_original) {
      cambios.fecha_base_original = prev.fecha_base;
    }
    const { error: errEscritura1 } = await supabase.from("checklist_items").update(cambios).eq("id", f.item_id).eq("project_id", projectId);
    if (errEscritura1) {
      console.error("[app/api/project/[id]/baseline/route.ts] update checklist_items fallo:", errEscritura1);
      fallos += 1;
    }
  }

  if (fallos > 0) {
    return NextResponse.json({ error: r.noPudeGuardarFechas, fallidas: fallos }, { status: 500 });
  }

  // Sella la baseline del ciclo. RLS de plans (user_id) garantiza propiedad.
  // AUD-09 M34: el sello es el del PRIMER cierre de fechas. Re-confirmar (un
  // recálculo) ya no lo pisa: la bitácora conserva cuándo quedó sellada.
  const { data: planPrevio } = await supabase.from("plans").select("baseline_confirmada_at").eq("id", datos.plan_id);
  const selloPrevio =
    ((planPrevio ?? []) as Array<{ baseline_confirmada_at?: string | null }>)[0]?.baseline_confirmada_at ?? null;
  if (selloPrevio) {
    return NextResponse.json({ ok: true, baseline_confirmada_at: selloPrevio, confirmadas: datos.fechas.length });
  }
  const { error: errorPlan } = await supabase
    .from("plans")
    .update({ baseline_confirmada_at: ahora })
    .eq("id", datos.plan_id)
    .is("baseline_confirmada_at", null);
  if (errorPlan) {
    return NextResponse.json({ error: t.noPudimosSellar }, { status: 500 });
  }

  return NextResponse.json({ ok: true, baseline_confirmada_at: ahora, confirmadas: datos.fechas.length });
}
