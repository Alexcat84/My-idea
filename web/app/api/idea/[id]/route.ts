/**
 * GET /api/idea/[id] — Fase 3.2: todo lo que la vista de idea necesita
 * para renderizarse desde lo persistido (refresh-proof): el proyecto, su
 * organizador, el último plan, el último reporte, y la entrevista
 * abierta (pregunta pendiente + ruta con títulos reales del grafo para
 * el árbol). RLS garantiza que solo se ve lo propio.
 */
import { NextResponse } from "next/server";
import { PREGUNTA_TIPO_OFERTA } from "@/lib/engine/constants";
import { obtenerProyecto, type EstadoSesionPersistido } from "@/lib/db";
import { cargarGrafo, etiquetaArbol } from "@/lib/engine/graph";
import { preguntasPorTipo } from "@/lib/engine/reporte";
import { nombreDeIdea } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";

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

  const { data: sesiones } = await supabase
    .from("sessions")
    .select("id, closed_at, estado_recorrido, created_at, dominio")
    .eq("project_id", projectId)
    .order("created_at", { ascending: true });

  const idsSesiones = ((sesiones ?? []) as Array<{ id: string }>).map((s) => s.id);
  const { data: planes } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("session_id, etiqueta, contenido_md, created_at, dominio")
        .in("session_id", idsSesiones)
        .order("created_at", { ascending: true })
    : { data: [] };

  type FilaPlan = {
    session_id: string;
    etiqueta: string;
    contenido_md: string;
    created_at: string;
    dominio: string | null;
  };
  const filas = (planes ?? []) as FilaPlan[];
  const esCore = (p: FilaPlan) => !p.dominio || p.dominio === "core";
  const ultimo = (pred: (p: FilaPlan) => boolean) => filas.filter(pred).at(-1) ?? null;
  const organizador = ultimo((p) => p.etiqueta === "organizador");
  // El plan de la vista es el ÚLTIMO plan CORE: los planes de mundos viven
  // en su propia sección (canon 08), no tapan el viaje principal.
  const plan = ultimo((p) => esCore(p) && ["inicial", "completo", "seguimiento"].includes(p.etiqueta));
  const reporte = ultimo((p) => p.etiqueta === "reporte_numeros");

  // Mundos (Fase 3.5/3.6): unlocks del proyecto + último plan por dominio.
  // project_unlocks puede no existir pre-016: se tolera con lista vacía.
  // Fase 4.2: el ciclo de vida del mundo (completado_at + cierre_motivo) llega
  // con la 026; si aún no está aplicada el select entero falla, y se reintenta
  // sin esas columnas — los mundos se leen abiertos, que es lo que son.
  type FilaUnlock = {
    dominio: string;
    completado_at?: string | null;
    cierre_motivo?: string | null;
    /** Fase 4.5 (migración 028): el escaparate del preview. */
    preview_at?: string | null;
    preview_session_id?: string | null;
    resumen_md?: string | null;
    resumen_at?: string | null;
    plan_pagado_at?: string | null;
  };
  let unlocksRaw: FilaUnlock[] = [];
  try {
    const { data, error } = await supabase
      .from("project_unlocks")
      .select("dominio, completado_at, cierre_motivo, preview_at, preview_session_id, resumen_md, resumen_at, plan_pagado_at")
      .eq("project_id", projectId);
    if (!error) unlocksRaw = (data ?? []) as FilaUnlock[];
    else {
      // Pre-028: reintento sin las columnas del preview; pre-026, solo dominio.
      const { data: sin45, error: err45 } = await supabase
        .from("project_unlocks")
        .select("dominio, completado_at, cierre_motivo")
        .eq("project_id", projectId);
      if (!err45) unlocksRaw = (sin45 ?? []) as FilaUnlock[];
      else {
        const { data: previo } = await supabase
          .from("project_unlocks")
          .select("dominio")
          .eq("project_id", projectId);
        unlocksRaw = (previo ?? []) as FilaUnlock[];
      }
    }
  } catch {
    unlocksRaw = [];
  }
  const unlocks = unlocksRaw.map((u) => u.dominio);
  const mundos = unlocksRaw.map((u) => {
    const planMundo = ultimo(
      (p) => p.dominio === u.dominio && ["inicial", "completo", "seguimiento"].includes(p.etiqueta)
    );
    return {
      dominio: u.dominio,
      completado_at: u.completado_at ?? null,
      cierre_motivo: u.cierre_motivo ?? null,
      // Fase 4.5: lo que la UI necesita para pintar los cuatro estados.
      preview_at: u.preview_at ?? null,
      preview_session_id: u.preview_session_id ?? null,
      resumen_md: u.resumen_md ?? null,
      resumen_at: u.resumen_at ?? null,
      plan_pagado_at: u.plan_pagado_at ?? null,
      plan: planMundo && {
        etiqueta: planMundo.etiqueta,
        contenido_md: planMundo.contenido_md,
        created_at: planMundo.created_at,
      },
    };
  });

  // Historia (canon 06): etiqueta y fecha de cada plan core anterior al
  // vigente — lo releíble, sin duplicar el contenido pesado.
  const historialCore = filas.filter(
    (p) => esCore(p) && ["inicial", "completo", "seguimiento"].includes(p.etiqueta)
  );
  const historial = historialCore.slice(0, -1).map((p) => ({
    etiqueta: p.etiqueta,
    created_at: p.created_at,
    contenido_md: p.contenido_md,
  }));

  // Entrevista abierta: sesión sin cerrar con estado resumible. El dominio
  // etiqueta la exploración de mundo (canon 08) sin cambiar el flujo.
  const graph = cargarGrafo();
  let entrevista: {
    session_id: string;
    pregunta: string | null;
    listo_para_plan: boolean;
    dominio: string;
    ruta: Array<{ id: string; titulo: string; etiqueta: string; modo: string }>;
  } | null = null;
  for (const s of ((sesiones ?? []) as Array<{
    id: string;
    closed_at: string | null;
    estado_recorrido: EstadoSesionPersistido | null;
    dominio?: string | null;
  }>).reverse()) {
    if (s.closed_at || !s.estado_recorrido) continue;
    // Fase 4.5: una sesión con recorrido en fase 'cerrada' pero sin closed_at
    // es un preview con diagnóstico listo (esperando compra). NO es una
    // entrevista abierta: su cara es el escaparate del mundo, no una pregunta.
    if (s.estado_recorrido.recorrido.fase === "cerrada") continue;
    const rec = s.estado_recorrido.recorrido;
    entrevista = {
      session_id: s.id,
      pregunta: rec.preguntaPendiente,
      // Phase 3.7.2: la oferta abierta (esperando_profundizar) tambien es
      // "listo" para la UI; sin esto, recargar en plena oferta dejaba la
      // vista vacia (ni pregunta ni tarjeta).
      listo_para_plan: rec.fase === "listo_para_plan" || rec.fase === "esperando_profundizar",
      dominio: s.dominio ?? "core",
      ruta: rec.ruta.map((nid, i) => ({
        id: nid,
        titulo: graph[nid]?.titulo_concepto ?? nid,
        etiqueta: etiquetaArbol(nid, graph),
        modo: rec.modos[i],
      })),
    };
    break;
  }

  // El recorrido que construyó el plan vigente (canon 05, sidebar "Construido
  // con tu recorrido"): disponible incluso con la sesión ya cerrada, leyendo
  // el estado_recorrido de la sesión del plan.
  let recorrido: Array<{ id: string; titulo: string; etiqueta: string; modo: string }> = [];
  if (plan) {
    const s = ((sesiones ?? []) as Array<{ id: string; estado_recorrido: EstadoSesionPersistido | null }>).find(
      (x) => x.id === plan.session_id
    );
    const rec = s?.estado_recorrido?.recorrido;
    if (rec) {
      recorrido = rec.ruta.map((nid, i) => ({
        id: nid,
        titulo: graph[nid]?.titulo_concepto ?? nid,
        etiqueta: etiquetaArbol(nid, graph),
        modo: rec.modos[i],
      }));
    }
  }

  // Mini-entrevista de reporte a medias (refresh-proof): reconstruye la
  // pregunta pendiente desde projects.estado_reporte, igual que lo haría
  // el siguiente paso del flujo.
  let reporteEnCurso: { pregunta: string } | null = null;
  if (proyecto.estado_reporte) {
    const e = proyecto.estado_reporte.estado;
    if (e.fase === "clasificando_oferta" || e.fase === "reclasificando_molde") {
      reporteEnCurso = { pregunta: PREGUNTA_TIPO_OFERTA };
    } else {
      const campo = e.faltantesEsenciales[e.idx];
      if (campo) {
        reporteEnCurso = { pregunta: preguntasPorTipo(e.tipoOferta, e.unidadVenta)[campo] };
      }
    }
  }

  return NextResponse.json({
    idea: {
      id: proyecto.id,
      nombre: nombreDeIdea(proyecto.titulo, proyecto.entrada_original),
      entrada_original: proyecto.entrada_original,
      fase_actual: proyecto.fase_actual,
      tipo_oferta: proyecto.tipo_oferta ?? null,
      // Fase 3.8: el modo del camino y si la idea ya es un proyecto realizado.
      modo_camino: proyecto.modo_camino ?? null,
      realizada_at: proyecto.realizada_at ?? null,
    },
    organizador: organizador && { contenido_md: organizador.contenido_md },
    plan: plan && { etiqueta: plan.etiqueta, contenido_md: plan.contenido_md, created_at: plan.created_at },
    reporte: reporte && { contenido_md: reporte.contenido_md, created_at: reporte.created_at },
    reporte_en_curso: reporteEnCurso,
    entrevista,
    recorrido,
    unlocks,
    mundos,
    historial,
  });
}
