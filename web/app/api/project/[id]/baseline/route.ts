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

  let cuerpo: unknown;
  try {
    cuerpo = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  const datos = parsear(cuerpo);
  if (!datos) {
    return NextResponse.json({ error: "falta plan_id o fechas mal formadas" }, { status: 400 });
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
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
    await supabase.from("checklist_items").update(cambios).eq("id", f.item_id).eq("project_id", projectId);
  }

  // Sella la baseline del ciclo. RLS de plans (user_id) garantiza propiedad.
  const { error: errorPlan } = await supabase
    .from("plans")
    .update({ baseline_confirmada_at: ahora })
    .eq("id", datos.plan_id);
  if (errorPlan) {
    return NextResponse.json({ error: "no pudimos sellar la línea base" }, { status: 500 });
  }

  return NextResponse.json({ ok: true, baseline_confirmada_at: ahora, confirmadas: datos.fechas.length });
}
