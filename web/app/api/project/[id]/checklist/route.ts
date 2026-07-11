/**
 * Fase 3.3 — el checklist como superficie de trabajo:
 *
 * GET  /api/project/[id]/checklist — ítems agrupados por plan y etapa,
 *      más resumen {total, hechos} por dominio. RLS filtra por dueño.
 * PATCH /api/project/[id]/checklist — body {item_id, estado?, nota?}:
 *      actualiza un ítem de un toque. estado se valida contra
 *      CHECKLIST_ESTADO (dbContract); RLS hace el resto.
 */
import { NextResponse } from "next/server";
import { CHECKLIST_ESTADO, type ChecklistEstado } from "@/lib/dbContract";
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
  created_at: string;
  updated_at: string;
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
    .select("id, plan_id, dominio, etapa, orden, texto, destacado, estado, nota, created_at, updated_at")
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

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: { item_id?: unknown; estado?: unknown; nota?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  const itemId = typeof body.item_id === "string" ? body.item_id : null;
  if (!itemId) {
    return NextResponse.json({ error: "falta item_id" }, { status: 400 });
  }
  const cambios: { estado?: ChecklistEstado; nota?: string | null; updated_at: string } = {
    updated_at: new Date().toISOString(),
  };
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
  if (cambios.estado === undefined && cambios.nota === undefined) {
    return NextResponse.json({ error: "nada que actualizar: manda estado y/o nota" }, { status: 400 });
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

  const { data, error } = await supabase
    .from("checklist_items")
    .update(cambios)
    .eq("id", itemId)
    .eq("project_id", projectId)
    .select("id, estado, nota, updated_at")
    .single();
  if (error || !data) {
    return NextResponse.json({ error: "ítem no encontrado" }, { status: 404 });
  }
  return NextResponse.json({ item: data });
}
