/**
 * Fase 3.3 — el checklist como superficie de trabajo. Ampliado en 3.8 con
 * el sentido del tiempo:
 *
 * GET  /api/project/[id]/checklist — ítems agrupados por plan y etapa,
 *      más resumen {total, hechos} por dominio. RLS filtra por dueño.
 * PATCH /api/project/[id]/checklist — body {item_id, estado?, nota?,
 *      completed_at?, fecha_base?}: actualiza un ítem de un toque. estado se
 *      valida contra CHECKLIST_ESTADO (dbContract); RLS hace el resto.
 *      - completed_at (Fase 3.8 §2, timeline real para TODOS): cuándo se
 *        hizo. Al pasar a 'hecho' sin fecha explícita → now(); al salir de
 *        'hecho' → null; editable después. No admite futuro.
 *      - fecha_base (Fase 3.8 §4, replanificación): mover la fecha objetivo
 *        de un ítem. Si el ítem YA tenía fecha_base (baseline confirmada),
 *        la primera se preserva en fecha_base_original y el origen pasa a
 *        'ajustada' (o 'manual' si nunca fue 'sugerida') — la historia no
 *        se reescribe.
 */
import { NextResponse } from "next/server";
import { CHECKLIST_ESTADO, type ChecklistEstado, type FechaBaseOrigen } from "@/lib/dbContract";
import { obtenerProyecto } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

interface ItemChecklist {
  id: string;
  plan_id: string;
  dominio: string;
  etapa: number;
  orden: number;
  texto: string;
  destacado: boolean;
  estado: ChecklistEstado;
  nota: string | null;
  completed_at: string | null;
  fecha_base: string | null;
  fecha_base_origen: FechaBaseOrigen | null;
  fecha_base_original: string | null;
  created_at: string;
  updated_at: string;
}

const COLUMNAS =
  "id, plan_id, dominio, etapa, orden, texto, destacado, estado, nota, completed_at, fecha_base, fecha_base_origen, fecha_base_original, created_at, updated_at";

/** Un timestamp ISO válido y no futuro (tolera 1 min de desfase de reloj). */
function fechaIsoValida(valor: unknown): string | null {
  if (typeof valor !== "string") return null;
  const t = Date.parse(valor);
  if (Number.isNaN(t)) return null;
  if (t > Date.now() + 60_000) return null;
  return new Date(t).toISOString();
}

export async function GET(_request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
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

  // Orden cronológico de planes (created_at) para que el grupo VIGENTE de
  // cada dominio sea el último (Fase 3.6: la pantalla Manos a la Obra lo
  // necesita; plan_id es uuid y su orden era arbitrario).
  const { data, error } = await supabase
    .from("checklist_items")
    .select(COLUMNAS)
    .eq("project_id", projectId)
    .order("created_at", { ascending: true })
    .order("etapa", { ascending: true })
    .order("orden", { ascending: true });
  if (error) {
    return NextResponse.json({ error: "no pudimos leer tu checklist" }, { status: 500 });
  }
  const items = (data ?? []) as ItemChecklist[];

  // Agrupado plan -> etapas (el orden de inserción ya viene garantizado).
  const planes: Array<{ plan_id: string; dominio: string; etapas: Array<{ etapa: number; items: ItemChecklist[] }> }> = [];
  for (const item of items) {
    let plan = planes.find((p) => p.plan_id === item.plan_id);
    if (!plan) {
      plan = { plan_id: item.plan_id, dominio: item.dominio, etapas: [] };
      planes.push(plan);
    }
    let etapa = plan.etapas.find((e) => e.etapa === item.etapa);
    if (!etapa) {
      etapa = { etapa: item.etapa, items: [] };
      plan.etapas.push(etapa);
    }
    etapa.items.push(item);
  }

  const resumen: Record<string, { total: number; hechos: number }> = {};
  for (const item of items) {
    const r = (resumen[item.dominio] ??= { total: 0, hechos: 0 });
    r.total += 1;
    if (item.estado === "hecho") r.hechos += 1;
  }

  return NextResponse.json({ planes, resumen });
}

interface CambiosItem {
  updated_at: string;
  estado?: ChecklistEstado;
  nota?: string | null;
  completed_at?: string | null;
  fecha_base?: string | null;
  fecha_base_origen?: FechaBaseOrigen;
  fecha_base_original?: string | null;
}

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: {
    item_id?: unknown;
    estado?: unknown;
    nota?: unknown;
    completed_at?: unknown;
    fecha_base?: unknown;
  };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  const itemId = typeof body.item_id === "string" ? body.item_id : null;
  if (!itemId) {
    return NextResponse.json({ error: "falta item_id" }, { status: 400 });
  }
  const cambios: CambiosItem = { updated_at: new Date().toISOString() };

  if (body.estado !== undefined) {
    if (typeof body.estado !== "string" || !(CHECKLIST_ESTADO as readonly string[]).includes(body.estado)) {
      return NextResponse.json(
        { error: `estado inválido; usa uno de: ${CHECKLIST_ESTADO.join(", ")}` },
        { status: 400 }
      );
    }
    cambios.estado = body.estado as ChecklistEstado;
  }
  if (body.nota !== undefined) {
    if (body.nota !== null && typeof body.nota !== "string") {
      return NextResponse.json({ error: "nota debe ser texto o null" }, { status: 400 });
    }
    cambios.nota = body.nota === null ? null : (body.nota as string).slice(0, 500);
  }

  // Fase 3.8 §2 — completed_at: cuándo se hizo. Regla, en orden:
  //  - completed_at explícito (incl. null para limpiar/editar): manda tal cual.
  //  - si no viene explícito pero el estado pasa a 'hecho': default now().
  //  - si no viene explícito y el estado sale de 'hecho': se limpia (null).
  if (body.completed_at !== undefined) {
    if (body.completed_at === null) {
      cambios.completed_at = null;
    } else {
      const iso = fechaIsoValida(body.completed_at);
      if (!iso) {
        return NextResponse.json({ error: "completed_at debe ser una fecha ISO no futura o null" }, { status: 400 });
      }
      cambios.completed_at = iso;
    }
  } else if (cambios.estado === "hecho") {
    cambios.completed_at = cambios.updated_at;
  } else if (cambios.estado !== undefined) {
    cambios.completed_at = null;
  }

  // Fase 3.8 §4 — fecha_base (replanificación). Se resuelve más abajo con el
  // estado previo del ítem (para preservar la primera fecha). Aquí solo se
  // valida la forma.
  let nuevaFechaBase: string | null | undefined;
  if (body.fecha_base !== undefined) {
    if (body.fecha_base === null) {
      nuevaFechaBase = null;
    } else if (typeof body.fecha_base === "string" && !Number.isNaN(Date.parse(body.fecha_base))) {
      nuevaFechaBase = new Date(Date.parse(body.fecha_base)).toISOString();
    } else {
      return NextResponse.json({ error: "fecha_base debe ser una fecha ISO o null" }, { status: 400 });
    }
  }

  if (
    cambios.estado === undefined &&
    cambios.nota === undefined &&
    cambios.completed_at === undefined &&
    nuevaFechaBase === undefined
  ) {
    return NextResponse.json(
      { error: "nada que actualizar: manda estado, nota, completed_at y/o fecha_base" },
      { status: 400 }
    );
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

  // Replanificación: leer el estado previo del ítem para preservar la
  // primera fecha_base y calcular el nuevo origen. El ítem que YA tiene
  // fecha_base pasó por una confirmación de baseline; moverla es replanificar.
  if (nuevaFechaBase !== undefined) {
    const { data: previo } = await supabase
      .from("checklist_items")
      .select("fecha_base, fecha_base_origen, fecha_base_original")
      .eq("id", itemId)
      .eq("project_id", projectId)
      .single();
    const prev = (previo ?? null) as
      | { fecha_base: string | null; fecha_base_origen: FechaBaseOrigen | null; fecha_base_original: string | null }
      | null;
    cambios.fecha_base = nuevaFechaBase;
    if (nuevaFechaBase !== null && prev?.fecha_base) {
      // Tenía una fecha previa = replanificación: no reescribir la historia.
      if (!prev.fecha_base_original) cambios.fecha_base_original = prev.fecha_base;
      cambios.fecha_base_origen =
        prev.fecha_base_origen === "sugerida" || prev.fecha_base_origen === "ajustada" ? "ajustada" : "manual";
    } else if (nuevaFechaBase !== null) {
      // Primera vez que se le pone fecha fuera del ritual: entrada manual.
      cambios.fecha_base_origen = "manual";
    }
  }

  const { data, error } = await supabase
    .from("checklist_items")
    .update(cambios)
    .eq("id", itemId)
    .eq("project_id", projectId)
    .select("id, estado, nota, completed_at, fecha_base, fecha_base_origen, fecha_base_original, updated_at")
    .single();
  if (error || !data) {
    return NextResponse.json({ error: "ítem no encontrado" }, { status: 404 });
  }
  return NextResponse.json({ item: data });
}
