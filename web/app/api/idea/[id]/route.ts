/**
 * GET /api/idea/[id] — Fase 3.2: todo lo que la vista de idea necesita
 * para renderizarse desde lo persistido (refresh-proof): el proyecto, su
 * organizador, el último plan, el último reporte, y la entrevista
 * abierta (pregunta pendiente + ruta con títulos reales del grafo para
 * el árbol). RLS garantiza que solo se ve lo propio.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { preguntaTipoOferta } from "@/lib/engine/constants";
import { obtenerCapacidadesPorEspacio, obtenerModosPorEspacio, obtenerProyecto, type EstadoSesionPersistido } from "@/lib/db";
import { ESPACIO_CORE } from "@/lib/espacios";
import { cargarGrafo, etiquetaArbol } from "@/lib/engine/graph";
import { avisosNodo } from "@/lib/engine/avisos";
import { avisoDelPlan } from "@/lib/engine/planRedactor";
import { preguntasPorTipo } from "@/lib/engine/reporte";
import { nombreDeIdea } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";
import { estadoEntrevista } from "@/lib/entrevistaAbierta";
import { ETIQUETAS_CICLO } from "@/lib/dbContract";
import { puedeVerOcultos } from "@/lib/fundador";

export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);

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

  const { data: sesiones } = await supabase
    .from("sessions")
    .select("id, closed_at, estado_recorrido, created_at, dominio, decisiones")
    .eq("project_id", projectId)
    .order("created_at", { ascending: true });

  const idsSesiones = ((sesiones ?? []) as Array<{ id: string }>).map((s) => s.id);
  const { data: planes } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("id, session_id, etiqueta, contenido_md, created_at, dominio")
        .in("session_id", idsSesiones)
        .order("created_at", { ascending: true })
    : { data: [] };

  type FilaPlan = {
    id?: string;
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
  const plan = ultimo((p) => esCore(p) && ETIQUETAS_CICLO.includes(p.etiqueta));
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
    /** AUD-09 (migración 039): la marca del plan básico (no es sello de pago). */
    plan_basico_at?: string | null;
  };
  let unlocksRaw: FilaUnlock[] = [];
  try {
    const COLS_028 = "dominio, completado_at, cierre_motivo, preview_at, preview_session_id, resumen_md, resumen_at, plan_pagado_at";
    // Con la 039, la marca del plan básico; sin ella, el mismo select de la 028
    // (la app tolera la migración pendiente, pero el mundo no puede ofrecer el
    // plan completo hasta aplicarla).
    const con039 = await supabase
      .from("project_unlocks")
      .select(`${COLS_028}, plan_basico_at`)
      .eq("project_id", projectId);
    let data: unknown[] | null = con039.data;
    let error = con039.error;
    if (error) {
      console.error("[idea] sin plan_basico_at en project_unlocks (¿falta la migracion 039?):", error.message);
      const sin039 = await supabase.from("project_unlocks").select(COLS_028).eq("project_id", projectId);
      data = sin039.data;
      error = sin039.error;
    }
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

  // Historia (canon 06): cada plan ANTERIOR al vigente de su espacio, releíble.
  // Ciclo de replanteamiento, Fase 2 ("lo hecho no se pierde"): con sus tareas
  // hechas y con lo que la persona contó al pedir ese plan (el evento ciclo_*
  // con su plan_id). Las copias heredadas no se repiten: salen bajo su original.
  const anterioresDe = (enEspacio: (p: FilaPlan) => boolean) =>
    filas.filter((p) => enEspacio(p) && ETIQUETAS_CICLO.includes(p.etiqueta)).slice(0, -1);
  const anterioresCore = anterioresDe(esCore);
  const anterioresMundo = new Map(unlocks.map((d) => [d, anterioresDe((p) => p.dominio === d)]));
  const idsAnteriores = [...anterioresCore, ...[...anterioresMundo.values()].flat()]
    .map((p) => p.id)
    .filter((id): id is string => Boolean(id));
  const hechasDe = new Map<string, Array<{ texto: string; completed_at: string | null }>>();
  const relatoDe = new Map<string, string>();
  if (idsAnteriores.length > 0) {
    // heredado_de llega con la 047: sin ella se lee sin la columna.
    const leerHechas = (cols: string) =>
      supabase.from("checklist_items").select(cols).eq("project_id", projectId).in("plan_id", idsAnteriores).eq("estado", "hecho");
    const conHeredado = await leerHechas("plan_id, texto, completed_at, etapa, orden, heredado_de");
    const hechas = conHeredado.error ? (await leerHechas("plan_id, texto, completed_at, etapa, orden")).data : conHeredado.data;
    const ordenadas = ((hechas ?? []) as unknown as Array<{
      plan_id: string;
      texto: string;
      completed_at: string | null;
      etapa: number;
      orden: number;
      heredado_de?: string | null;
    }>)
      .filter((h) => !h.heredado_de)
      .sort((a, c) => a.etapa - c.etapa || a.orden - c.orden);
    for (const h of ordenadas) {
      const lista = hechasDe.get(h.plan_id) ?? [];
      lista.push({ texto: h.texto, completed_at: h.completed_at ?? null });
      hechasDe.set(h.plan_id, lista);
    }
    const { data: ciclos } = await supabase
      .from("project_bitacora")
      .select("payload")
      .eq("project_id", projectId)
      .in("tipo", ["ciclo_profundizado", "ciclo_replanteado"]);
    for (const c of (ciclos ?? []) as Array<{ payload?: { plan_id?: unknown; relato?: unknown } }>) {
      const planId = c.payload?.plan_id;
      const relato = typeof c.payload?.relato === "string" ? c.payload.relato.trim() : "";
      if (typeof planId === "string" && relato) relatoDe.set(planId, relato);
    }
  }
  const aHistoria = (p: FilaPlan) => ({
    etiqueta: p.etiqueta,
    created_at: p.created_at,
    contenido_md: p.contenido_md,
    hechas: (p.id && hechasDe.get(p.id)) || [],
    relato: (p.id && relatoDe.get(p.id)) || null,
  });

  const mundos = unlocksRaw.map((u) => {
    const planMundo = ultimo(
      (p) => p.dominio === u.dominio && ETIQUETAS_CICLO.includes(p.etiqueta)
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
      plan_basico_at: u.plan_basico_at ?? null,
      // Fase 2 del ciclo de replanteamiento: la Historia del mundo.
      historial: (anterioresMundo.get(u.dominio) ?? []).map(aHistoria),
      plan: planMundo && {
        // AUD-09: la sesión del plan, para regenerarlo si es básico.
        session_id: planMundo.session_id,
        etiqueta: planMundo.etiqueta,
        contenido_md: planMundo.contenido_md,
        created_at: planMundo.created_at,
      },
    };
  });

  const historial = anterioresCore.map(aHistoria);

  // Entrevista abierta: sesión sin cerrar con estado resumible. El dominio
  // etiqueta la exploración de mundo (canon 08) sin cambiar el flujo.
  const graph = cargarGrafo();
  let entrevista: {
    session_id: string;
    pregunta: string | null;
    listo_para_plan: boolean;
    dominio: string;
    /** AUD-09 H01: al recargar, la pantalla sabe si es un seguimiento (plan del
     * ciclo, a su precio) o un preview de mundo (diagnóstico gratis). */
    es_seguimiento: boolean;
    ruta: Array<{ id: string; etiqueta: string; modo: string }>;
    /** El recorrido conversado ya persistido: al reentrar a la idea, la UI lo
     * vuelve a pintar en vez de arrancar en blanco. */
    turnos: Array<{ pregunta: string; respuesta: string }>;
  } | null = null;
  for (const s of ((sesiones ?? []) as Array<{
    id: string;
    closed_at: string | null;
    estado_recorrido: EstadoSesionPersistido | null;
    dominio?: string | null;
  }>).reverse()) {
    // AUD-09 M29: la regla única de "entrevista abierta" (la misma de /ideas).
    // Fase 4.5: una sesión con recorrido en fase 'cerrada' pero sin closed_at
    // es un preview con diagnóstico listo (esperando compra): no cuenta.
    if (!estadoEntrevista(s) || !s.estado_recorrido) continue;
    const rec = s.estado_recorrido.recorrido;
    entrevista = {
      session_id: s.id,
      pregunta: rec.preguntaPendiente,
      // Phase 3.7.2: la oferta abierta (esperando_profundizar) tambien es
      // "listo" para la UI; sin esto, recargar en plena oferta dejaba la
      // vista vacia (ni pregunta ni tarjeta).
      listo_para_plan: rec.fase === "listo_para_plan" || rec.fase === "esperando_profundizar",
      dominio: s.dominio ?? "core",
      es_seguimiento: rec.esSeguimiento === true,
      ruta: rec.ruta.map((nid, i) => ({
        id: nid,
        // Solo la etiqueta de cara: el nombre técnico del concepto no sale
        // de casa (decisión del fundador, jul 2026).
        etiqueta: etiquetaArbol(nid, graph, idioma),
        avisos: avisosNodo(nid, graph, idioma),
        modo: rec.modos[i],
      })),
      turnos: (s.estado_recorrido.turnos ?? []).map((t) => ({ pregunta: t.pregunta, respuesta: t.respuesta })),
    };
    break;
  }

  // El recorrido que construyó el plan vigente (canon 05, sidebar "Construido
  // con tu recorrido"): disponible incluso con la sesión ya cerrada, leyendo
  // el estado_recorrido de la sesión del plan.
  let recorrido: Array<{ id: string; etiqueta: string; modo: string }> = [];
  if (plan) {
    const s = ((sesiones ?? []) as Array<{ id: string; estado_recorrido: EstadoSesionPersistido | null }>).find(
      (x) => x.id === plan.session_id
    );
    const rec = s?.estado_recorrido?.recorrido;
    if (rec) {
      recorrido = rec.ruta.map((nid, i) => ({
        id: nid,
        etiqueta: etiquetaArbol(nid, graph, idioma),
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
      reporteEnCurso = { pregunta: preguntaTipoOferta(idioma) };
    } else {
      const campo = e.faltantesEsenciales[e.idx];
      if (campo) {
        reporteEnCurso = { pregunta: preguntasPorTipo(e.tipoOferta, e.unidadVenta, idioma)[campo] };
      }
    }
  }

  // "Todo separado" (T3): el modo del camino POR ESPACIO (project_modos). El core
  // dual-lee (project_modos.core ó projects.modo_camino). `modos` es el mapa que
  // usará el selector/ritual de cada espacio; `modo_camino` es el del core (compat).
  const modos = await obtenerModosPorEspacio(supabase, projectId);
  const modoCore = modos[ESPACIO_CORE] ?? proyecto.modo_camino ?? null;
  // Scheduler F2: las horas por semana declaradas por espacio. El ritual las usa
  // para empaquetar; un espacio sin declarar no aparece (arranca en el default).
  const capacidades = await obtenerCapacidadesPorEspacio(supabase, projectId);

  return NextResponse.json({
    // Punto 7c del encargo del 6 oct: ?ver=ocultos solo se enciende si el servidor dice que puedes (lib/fundador.ts).
    puedeVerOcultos: puedeVerOcultos(user),
    idea: {
      id: proyecto.id,
      nombre: nombreDeIdea(proyecto.titulo, proyecto.entrada_original),
      entrada_original: proyecto.entrada_original,
      // i18n F6 (D2): el idioma del proyecto, para que el plan en pantalla lo
      // siga como los documentos. null = idea de antes de F5 (español).
      idioma: proyecto.idioma ?? null,
      fase_actual: proyecto.fase_actual,
      tipo_oferta: proyecto.tipo_oferta ?? null,
      // El modo del camino del CORE (dual-read) y si la idea ya es un proyecto.
      modo_camino: modoCore,
      // El modo por espacio (dominio → 'ritmo'|'fechas'); el core no está si nunca eligió.
      modos,
      // La capacidad por espacio (dominio → '2-5'|'5-10'|'10-20'|'20+').
      capacidades,
      realizada_at: proyecto.realizada_at ?? null,
      // Campaña "Espacios" (cara "Tu avance"): La Chispa = nacimiento del proyecto.
      created_at: proyecto.created_at,
      // "Tu avance" (26 sep 2026): cuándo empezó La Exploración del núcleo, la
      // primera sesión que no es de un mundo.
      // (la MÁS ANTIGUA por fecha, sin fiarse del orden de la lista).
      exploracion_at:
        ((sesiones ?? []) as Array<{ created_at: string; dominio: string | null }>)
          .filter((s) => !s.dominio || s.dominio === "core")
          .map((s) => s.created_at)
          .sort()[0] ?? null,
    },
    organizador: organizador && { contenido_md: organizador.contenido_md, created_at: organizador.created_at },
    plan: plan && {
      session_id: plan.session_id,
      etiqueta: plan.etiqueta,
      contenido_md: plan.contenido_md,
      created_at: plan.created_at,
      // AUD-09 H02: un plan armado sin IA conserva su aviso tras recargar.
      aviso: avisoDelPlan(
        ((sesiones ?? []) as Array<{ id: string; decisiones?: unknown }>).find((x) => x.id === plan.session_id)
          ?.decisiones,
        idioma
      ),
    },
    reporte: reporte && { contenido_md: reporte.contenido_md, created_at: reporte.created_at },
    reporte_en_curso: reporteEnCurso,
    entrevista,
    recorrido,
    unlocks,
    mundos,
    historial,
  });
}
