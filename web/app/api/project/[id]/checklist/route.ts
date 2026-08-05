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
import { BANDA, CHECKLIST_ESTADO, esActivo, type Banda, type ChecklistEstado, type FechaBaseOrigen } from "@/lib/dbContract";
import { obtenerProyecto, registrarBitacora } from "@/lib/db";
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
  no_aplica_motivo: string | null;
  fecha_base: string | null;
  fecha_base_origen: FechaBaseOrigen | null;
  fecha_base_original: string | null;
  // Scheduler F1: la banda de esfuerzo estimada + si arrastra espera de terceros.
  banda: Banda | null;
  espera_externa: boolean | null;
  created_at: string;
  updated_at: string;
}

const COLUMNAS =
  "id, plan_id, dominio, etapa, orden, texto, destacado, estado, nota, completed_at, no_aplica_motivo, fecha_base, fecha_base_origen, fecha_base_original, banda, espera_externa, created_at, updated_at";

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
  //
  // no_aplica_motivo llega con la migración 030, y banda/espera_externa con la
  // 033. Si el código se despliega un instante antes de aplicar alguna, el
  // select entero fallaría y la LECTURA del checklist se caería para todos: por
  // eso se reintenta degradando las columnas nuevas (se leen null) en vez de
  // romper. Patrón de project_unlocks (pre-026).
  const leer = (columnas: string) =>
    supabase
      .from("checklist_items")
      .select(columnas)
      .eq("project_id", projectId)
      .order("created_at", { ascending: true })
      .order("etapa", { ascending: true })
      .order("orden", { ascending: true });
  let { data, error } = await leer(COLUMNAS);
  if (error) ({ data, error } = await leer(COLUMNAS.replace(", banda, espera_externa", "")));
  if (error)
    ({ data, error } = await leer(COLUMNAS.replace(", banda, espera_externa", "").replace(", no_aplica_motivo", "")));
  if (error) {
    return NextResponse.json({ error: "no pudimos leer tu checklist" }, { status: 500 });
  }
  const items = ((data ?? []) as Array<Partial<ItemChecklist>>).map((i) => ({
    ...i,
    no_aplica_motivo: i.no_aplica_motivo ?? null,
    banda: i.banda ?? null,
    espera_externa: i.espera_externa ?? null,
  })) as ItemChecklist[];

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

  // Cuentas honestas (gestor de estados): 'total' es el denominador de ACTIVAS
  // (todo menos las retiradas 'no_aplica'); 'retiradas' se cuenta aparte. El
  // avance es "hechos de total activas", nunca sobre tareas que el usuario
  // retiró a propósito.
  const resumen: Record<string, { total: number; hechos: number; retiradas: number }> = {};
  for (const item of items) {
    const r = (resumen[item.dominio] ??= { total: 0, hechos: 0, retiradas: 0 });
    if (esActivo(item.estado)) {
      r.total += 1;
      if (item.estado === "hecho") r.hechos += 1;
    } else {
      r.retiradas += 1;
    }
  }

  return NextResponse.json({ planes, resumen });
}

interface CambiosItem {
  updated_at: string;
  estado?: ChecklistEstado;
  nota?: string | null;
  completed_at?: string | null;
  no_aplica_motivo?: string | null;
  fecha_base?: string | null;
  fecha_base_origen?: FechaBaseOrigen;
  fecha_base_original?: string | null;
  banda?: Banda;
}

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: {
    item_id?: unknown;
    estado?: unknown;
    nota?: unknown;
    completed_at?: unknown;
    no_aplica_motivo?: unknown;
    fecha_base?: unknown;
    banda?: unknown;
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

  // Motivo de "no aplica" (gestor de estados): opcional, para la memoria del
  // usuario. Regla, en orden:
  //  - al PASAR a 'no_aplica' sin motivo explícito, se conserva null.
  //  - al SALIR de 'no_aplica' (cualquier otro estado), se limpia el motivo:
  //    el registro del porqué queda en la bitácora, no en la fila.
  //  - se puede editar el motivo de una tarea que ya está en 'no_aplica'.
  if (body.no_aplica_motivo !== undefined) {
    if (body.no_aplica_motivo !== null && typeof body.no_aplica_motivo !== "string") {
      return NextResponse.json({ error: "no_aplica_motivo debe ser texto o null" }, { status: 400 });
    }
    cambios.no_aplica_motivo =
      body.no_aplica_motivo === null ? null : (body.no_aplica_motivo as string).slice(0, 500).trim() || null;
  } else if (cambios.estado !== undefined && cambios.estado !== "no_aplica") {
    cambios.no_aplica_motivo = null;
  }

  // Scheduler F1 — corrección de banda: el usuario ajusta la estimación del
  // modelo. Se valida contra BANDA; solo corrige (no admite null: para "quitar"
  // no hay caso de uso, y null es "sin estimar", no una elección del usuario).
  if (body.banda !== undefined) {
    if (typeof body.banda !== "string" || !(BANDA as readonly string[]).includes(body.banda)) {
      return NextResponse.json({ error: `banda inválida; usa una de: ${BANDA.join(", ")}` }, { status: 400 });
    }
    cambios.banda = body.banda as Banda;
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
    cambios.no_aplica_motivo === undefined &&
    nuevaFechaBase === undefined &&
    cambios.banda === undefined
  ) {
    return NextResponse.json(
      { error: "nada que actualizar: manda estado, nota, completed_at, no_aplica_motivo, fecha_base y/o banda" },
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

  // Se lee el estado previo cuando lo necesita la replanificación (preservar
  // la primera fecha_base) o el cruce de 'no_aplica' (registrar en bitácora
  // estado_anterior). Una sola lectura para las dos cosas.
  type PrevItem = {
    estado: ChecklistEstado;
    fecha_base: string | null;
    fecha_base_origen: FechaBaseOrigen | null;
    fecha_base_original: string | null;
    no_aplica_motivo: string | null;
    completed_at: string | null;
    nota: string | null;
    banda?: Banda | null;
  };
  let prev: PrevItem | null = null;
  // Se lee el previo para cualquier decisión que la BITÁCORA deba comparar: el
  // cambio de estado, mover la fecha (base o de realización), la nota y la banda
  // corregida. Así la historia del usuario queda completa (Fase 4.8).
  // 'banda' solo se pide cuando se corrige banda: ese camino está UI-gated a que
  // 033 exista, así que un PATCH de estado normal jamás depende de esa columna.
  if (
    nuevaFechaBase !== undefined ||
    cambios.estado !== undefined ||
    cambios.completed_at !== undefined ||
    cambios.nota !== undefined ||
    cambios.banda !== undefined
  ) {
    const colsPrev =
      "estado, fecha_base, fecha_base_origen, fecha_base_original, no_aplica_motivo, completed_at, nota" +
      (cambios.banda !== undefined ? ", banda" : "");
    const { data: previo } = await supabase
      .from("checklist_items")
      .select(colsPrev)
      .eq("id", itemId)
      .eq("project_id", projectId)
      .single();
    prev = (previo ?? null) as PrevItem | null;
  }

  // Replanificación: el ítem que YA tenía fecha_base pasó por una confirmación
  // de baseline; moverla es replanificar y la primera fecha no se reescribe.
  if (nuevaFechaBase !== undefined) {
    cambios.fecha_base = nuevaFechaBase;
    if (nuevaFechaBase !== null && prev?.fecha_base) {
      if (!prev.fecha_base_original) cambios.fecha_base_original = prev.fecha_base;
      cambios.fecha_base_origen =
        prev.fecha_base_origen === "sugerida" || prev.fecha_base_origen === "ajustada" ? "ajustada" : "manual";
    } else if (nuevaFechaBase !== null) {
      cambios.fecha_base_origen = "manual";
    }
  }

  // 'banda' solo se pide de vuelta cuando se corrigió: así un PATCH normal no
  // depende de la 033. Con la lista de columnas armada en runtime, Supabase no
  // puede inferir la fila: se castea al tipo real (mismo patrón que el GET).
  const colsRet =
    "id, estado, nota, completed_at, no_aplica_motivo, fecha_base, fecha_base_origen, fecha_base_original, dominio, updated_at" +
    (cambios.banda !== undefined ? ", banda" : "");
  const { data: filaCruda, error } = await supabase
    .from("checklist_items")
    .update(cambios)
    .eq("id", itemId)
    .eq("project_id", projectId)
    .select(colsRet)
    .single();
  if (error || !filaCruda) {
    return NextResponse.json({ error: "ítem no encontrado" }, { status: 404 });
  }
  const data = filaCruda as unknown as {
    id: string;
    estado: ChecklistEstado;
    nota: string | null;
    completed_at: string | null;
    no_aplica_motivo: string | null;
    fecha_base: string | null;
    fecha_base_origen: FechaBaseOrigen | null;
    fecha_base_original: string | null;
    dominio: string | null;
    updated_at: string;
    banda?: Banda | null;
  };

  // Fase 3 (Espacios): cada evento de bitácora de un ítem viaja con el dominio
  // del ítem, para que la entrada sea auto-descriptiva y su espacio no dependa
  // de que el ítem siga existiendo (deja el borde no-derivable solo arqueológico).
  const dom = (data.dominio as string | null) ?? null;

  // Bitácora del gestor de estados: cada cruce de la frontera 'no_aplica' deja
  // rastro reversible. Retirar registra {item, estado_anterior, motivo};
  // revertir registra el motivo nuevo JUNTO al anterior (nada se reescribe: la
  // fila pierde el motivo, la historia lo conserva). No bloquea la respuesta.
  if (cambios.estado !== undefined && prev) {
    const nuevo = data.estado as ChecklistEstado;
    if (nuevo === "no_aplica" && prev.estado !== "no_aplica") {
      await registrarBitacora(supabase, projectId, "item_no_aplica", {
        item: itemId,
        dominio: dom,
        estado_anterior: prev.estado,
        motivo: (cambios.no_aplica_motivo ?? null) as string | null,
      });
    } else if (prev.estado === "no_aplica" && nuevo !== "no_aplica") {
      await registrarBitacora(supabase, projectId, "item_reactivada", {
        item: itemId,
        dominio: dom,
        estado_nuevo: nuevo,
        motivo_anterior: prev.no_aplica_motivo ?? null,
      });
    }
  }

  // Fase 4.8 (bitácora completa): cada decisión del usuario deja rastro.
  if (prev) {
    const nuevoEstado = data.estado as ChecklistEstado;
    // Cambio de estado que NO es el cruce de 'no_aplica' (ya registrado arriba)
    // ni 'hecho' (su entrada nace de completed_at, no se duplica): empezar,
    // poner en proceso o volver a pendiente son decisiones que cuentan.
    if (
      cambios.estado !== undefined &&
      nuevoEstado !== prev.estado &&
      nuevoEstado !== "no_aplica" &&
      prev.estado !== "no_aplica" &&
      nuevoEstado !== "hecho"
    ) {
      await registrarBitacora(supabase, projectId, "item_estado", {
        item: itemId,
        dominio: dom,
        de: prev.estado,
        a: nuevoEstado,
      });
    }
    // Ajustar la fecha de realización de algo YA hecho ("cambiar fecha"): es
    // un cambio, no la primera marca (esa la cuenta completed_at por sí sola).
    if (
      body.completed_at !== undefined &&
      cambios.estado === undefined &&
      prev.estado === "hecho" &&
      prev.completed_at &&
      (data.completed_at ?? null) !== prev.completed_at
    ) {
      await registrarBitacora(supabase, projectId, "fecha_hecho_movida", {
        item: itemId,
        dominio: dom,
        de: prev.completed_at,
        a: data.completed_at ?? null,
      });
    }
    // Nota escrita o cambiada (el contenido NO se guarda en la bitácora: es
    // privado; solo queda que decidiste anotar algo).
    const notaNueva = (data.nota ?? "").trim();
    if (cambios.nota !== undefined && notaNueva && notaNueva !== (prev.nota ?? "").trim()) {
      await registrarBitacora(supabase, projectId, "nota_escrita", { item: itemId, dominio: dom });
    }
    // Scheduler F1 — banda corregida por el usuario {de, a}: telemetría de oro
    // para el multiplicador por banda de F4 (dónde el modelo se equivoca y hacia
    // dónde). Solo cuando de verdad cambió (no re-elegir la misma).
    const bandaNueva = (data.banda ?? null) as Banda | null;
    if (cambios.banda !== undefined && bandaNueva && bandaNueva !== (prev.banda ?? null)) {
      await registrarBitacora(supabase, projectId, "banda_corregida", {
        item: itemId,
        dominio: dom,
        de: prev.banda ?? null,
        a: bandaNueva,
      });
    }
  }

  return NextResponse.json({ item: data });
}
