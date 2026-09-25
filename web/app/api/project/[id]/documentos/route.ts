/**
 * GET /api/project/[id]/documentos — Fase 4.6: lo que el usuario se lleva.
 *
 * Sin `?doc=` devuelve el ÍNDICE: un documento por fase del viaje (Tu Plan,
 * cada Seguimiento) más el expediente completo. Con `?doc=<clave>` devuelve el
 * markdown de ese documento, que es la misma fuente para la descarga .md y
 * para la vista de impresión que produce el PDF (una sola verdad; si el .md y
 * el PDF se armaran por separado, acabarían diciendo cosas distintas).
 *
 * CERO LLM y cero créditos: todo sale de lo ya persistido. Descargar lo que ya
 * es tuyo no se cobra.
 */
import { NextResponse } from "next/server";
import { elegir, LOCALE_BASE } from "@/lib/i18n/config";
import { formaPlural, interpolar } from "@/lib/i18n/interpolar";
import { DOCUMENTOS_RUTA } from "@/lib/i18n/mensajes/documentosRuta";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { actasVigentes } from "@/lib/acta";
import type { AnalisisPapelData } from "@/app/ui/AnalisisPapel";
import { analyticsDeMundo, calcularAnalytics, informeMarkdown, resumenEspacioMd } from "@/lib/analytics";
import { fechaHumanaCorta } from "@/lib/fechas";
import catalogo from "@/lib/assets/packs_catalog.json";
import { cargarEntradaAnalytics, LecturaFallidaError, mensajeLecturaFallida } from "@/lib/analyticsEntrada";
import { bitacoraCuerpo, bitacoraDeEspacio, bitacoraMarkdown, etiquetaEspacio, proyectoTieneMundos } from "@/lib/bitacoraCliente";
import { cargarEntradasBitacora } from "@/lib/bitacoraDatos";
import { obtenerItemsDePlan, obtenerPlanCoreVigente, obtenerProyecto } from "@/lib/db";
import { esMundoProteccion } from "@/lib/espacios";
import { armarSnapshot, type FilaChecklistSnapshot } from "@/lib/engine/snapshotProyecto";
import { armarRegistro, registroMarkdown, type FilaRespuesta } from "@/lib/registroProteccion";
import {
  CLAVE_ANALISIS,
  CLAVE_BITACORA,
  CLAVE_EXPEDIENTE,
  cicloMarkdown,
  expedienteMarkdown,
  indiceDeDocumentos,
  nombreArchivo,
  reporteMundoMarkdown,
  titulosDeCiclos,
  type AccionExpediente,
  type CicloExpediente,
  type MundoExpediente,
  accionesDelCicloVigente,
} from "@/lib/expediente";
import { nombreDeIdea } from "@/lib/ideas";
import { sinProcedencia } from "@/lib/planParser";
import { createClient } from "@/lib/supabase/server";
import { resumenCaminoExpediente } from "@/lib/resumenExpediente";

export const runtime = "nodejs";

const ETIQUETAS_CICLO = ["inicial", "completo", "seguimiento"];
const esCore = (dominio: string | null | undefined) => !dominio || dominio === "core";

type FilaPlan = {
  id: string;
  etiqueta: string;
  contenido_md: string;
  created_at: string;
  dominio: string | null;
  baseline_confirmada_at: string | null;
};
type FilaSesion = { id: string; created_at: string; tipo: string; dominio: string | null };
type FilaAccion = {
  /** AUD-09 M02: el plan de la tarea, para quedarse con el ciclo vigente. */
  plan_id?: string | null;
  dominio: string | null;
  etapa: number;
  texto: string;
  estado: string;
  completed_at: string | null;
  fecha_base: string | null;
  no_aplica_motivo?: string | null;
};

/** Carga TODAS las acciones (checklist) con el fallback de no_aplica_motivo (030:
 * se reintenta sin esa columna si aún no está). Compartido por el expediente y el
 * Reporte de un mundo, que luego filtran por dominio. */
async function cargarAcciones(supabase: Awaited<ReturnType<typeof createClient>>, projectId: string): Promise<FilaAccion[]> {
  const COLS = "plan_id, dominio, etapa, texto, estado, completed_at, fecha_base, orden";
  const con = await supabase
    .from("checklist_items")
    .select(`${COLS}, no_aplica_motivo`)
    .eq("project_id", projectId)
    .order("etapa", { ascending: true })
    .order("orden", { ascending: true });
  let raw: unknown[] | null = con.data;
  if (con.error) {
    const sin030 = await supabase
      .from("checklist_items")
      .select(COLS)
      .eq("project_id", projectId)
      .order("etapa", { ascending: true })
      .order("orden", { ascending: true });
    // AUD-09 M18: si tampoco la lectura mínima responde, no es "sin tareas".
    if (sin030.error) throw new LecturaFallidaError("las tareas", sin030.error);
    raw = sin030.data;
  }
  return ((raw ?? []) as FilaAccion[]).map((i) => ({ ...i, no_aplica_motivo: i.no_aplica_motivo ?? null }));
}

const aAccion = (i: FilaAccion): AccionExpediente => ({
  etapa: i.etapa,
  texto: i.texto,
  estado: i.estado,
  completedAt: i.completed_at,
  fechaBase: i.fecha_base,
  noAplicaMotivo: i.no_aplica_motivo ?? null,
});

async function generarDocumentos(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(DOCUMENTOS_RUTA, idioma);
  // Lo que forma el documento (títulos, archivo, encabezados) sigue el idioma
  // del proyecto (D2, llega en F5): hoy el base. Los rechazos, el de la interfaz.
  const tDoc = elegir(DOCUMENTOS_RUTA, LOCALE_BASE);

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

  const { data: sesionesRaw, error: errSesiones } = await supabase
    .from("sessions")
    .select("id, created_at, tipo, dominio")
    .eq("project_id", projectId);
  if (errSesiones) throw new LecturaFallidaError("las sesiones", errSesiones);
  const sesiones = (sesionesRaw ?? []) as FilaSesion[];
  const idsSesiones = sesiones.map((s) => s.id);
  const { data: planesRaw, error: errPlanes } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("id, etiqueta, contenido_md, created_at, dominio, baseline_confirmada_at")
        .in("session_id", idsSesiones)
        .order("created_at", { ascending: true })
    : { data: [], error: null };
  if (errPlanes) throw new LecturaFallidaError("los planes", errPlanes);
  const planes = (planesRaw ?? []) as FilaPlan[];

  const ciclos: CicloExpediente[] = planes
    .filter((p) => esCore(p.dominio) && ETIQUETAS_CICLO.includes(p.etiqueta))
    // sinProcedencia: los planes viejos llevan grabada la línea de mecánica
    // interna; se limpia al leer para que ninguna descarga la filtre.
    .map((p) => ({
      planId: p.id,
      etiqueta: p.etiqueta,
      createdAt: p.created_at,
      contenidoMd: sinProcedencia(p.contenido_md),
    }));

  const nombre = nombreDeIdea(proyecto.titulo, proyecto.entrada_original);
  const realizadaAt = proyecto.realizada_at ?? null;

  const packs = (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs;
  const nombreMundo = (dominio: string) => packs.find((p) => p.clave === dominio)?.nombre ?? dominio;

  // Fase 3 (tanda 5): los mundos con plan (dominios distintos entre los planes de
  // mundo), para el Reporte por espacio del índice. Los ciclos de un dominio se
  // arman igual que los del core (plan + seguimientos), filtrados por dominio.
  const ciclosDeDominio = (dominio: string): CicloExpediente[] =>
    planes
      .filter((p) => p.dominio === dominio && ETIQUETAS_CICLO.includes(p.etiqueta))
      .map((p) => ({ planId: p.id, etiqueta: p.etiqueta, createdAt: p.created_at, contenidoMd: sinProcedencia(p.contenido_md) }));
  const dominiosMundo = [
    ...new Set(planes.filter((p) => !esCore(p.dominio) && ETIQUETAS_CICLO.includes(p.etiqueta)).map((p) => p.dominio!)),
  ];
  const mundosIndice = dominiosMundo.map((dom) => ({ dominio: dom, nombre: nombreMundo(dom) }));

  const doc = new URL(request.url).searchParams.get("doc");
  if (!doc) {
    return NextResponse.json({ nombre, documentos: indiceDeDocumentos(ciclos, realizadaAt, mundosIndice) });
  }

  // ── Reporte de un mundo (documento por espacio) ────────────────────────────
  if (doc.startsWith("reporte:")) {
    const dominio = doc.slice("reporte:".length);
    const ciclosMundo = ciclosDeDominio(dominio);
    if (ciclosMundo.length === 0) {
      return NextResponse.json({ error: t.noEncontrado }, { status: 404 });
    }
    const ahora = new Date().toISOString();
    const entrada = await cargarEntradaAnalytics(supabase, projectId, proyecto, ahora);
    const am = analyticsDeMundo(entrada, dominio);
    const comoTeFueMd = am ? resumenEspacioMd(am.universal, am.cumplimiento).join("\n") : null;

    const entradasBita = await cargarEntradasBitacora(supabase, projectId, proyecto, nombre);
    // Scopeado: la secuencia del mundo NO se auto-etiqueta (ya estás en su espacio).
    const bitacoraMd = bitacoraCuerpo(bitacoraDeEspacio(entradasBita, dominio), 3).join("\n");

    // AUD-09 M02: solo el ciclo vigente del mundo (los anteriores son sus ciclos).
    const accionesMundo = accionesDelCicloVigente(await cargarAcciones(supabase, projectId), planes)
      .filter((i) => i.dominio === dominio)
      .map(aAccion);

    const nombreDom = nombreMundo(dominio);
    return NextResponse.json({
      titulo: interpolar(tDoc.tituloReporte, { mundo: nombreDom }),
      nombre,
      archivo: nombreArchivo(nombre, interpolar(tDoc.tituloReporte, { mundo: nombreDom })),
      markdown: reporteMundoMarkdown({
        nombreIdea: nombre,
        nombreMundo: nombreDom,
        ciclos: ciclosMundo,
        acciones: accionesMundo,
        comoTeFueMd,
        bitacoraMd,
        completadoAt: am?.completadoAt ?? null,
        generadoAt: ahora,
      }),
    });
  }

  // ── Registro de protección (documento del espacio, P3) ────────────────────
  if (doc.startsWith("registro:")) {
    const dominio = doc.slice("registro:".length);
    // Solo los tres mundos de protección y solo con plan: el índice no lo ofrece
    // en ningún otro caso, así que llegar aquí sin eso es una clave inventada.
    if (!esMundoProteccion(dominio) || ciclosDeDominio(dominio).length === 0) {
      return NextResponse.json({ error: t.noEncontrado }, { status: 404 });
    }
    const COLS_REGISTRO = "id, plan_id, texto, etapa, orden, estado, protege_item, protege_nodos, deteccion, probabilidad, dolor, camino";
    const leerRegistro = (cols: string) =>
      supabase.from("checklist_items").select(cols).eq("project_id", projectId).eq("dominio", dominio);
    let { data: filasMundo, error: errRegistro } = await leerRegistro(COLS_REGISTRO);
    // Si la 041 aún no se aplicó, se lee sin protege_nodos (resuelve por id).
    if (errRegistro) ({ data: filasMundo, error: errRegistro } = await leerRegistro(COLS_REGISTRO.replace(", protege_nodos", "")));
    if (errRegistro) {
      // Fallar ruidoso (BANCO §9): sin registro a medias ni plantilla.
      return NextResponse.json({ error: t.noPudimosLeerRegistro }, { status: 500 });
    }
    // Las actividades del núcleo con su #N, del MISMO armador que usó el
    // enlazador: pantalla, papel y enlace comparten numeración.
    const planCore = await obtenerPlanCoreVigente(supabase, projectId);
    const filasNucleo = planCore ? await obtenerItemsDePlan(supabase, projectId, planCore) : [];
    // AUD-09 M15: con sus nodos (la protección se resuelve por nodo contra
    // este plan) y con los ids de TODO el plan, retiradas incluidas.
    const nodosPorId = new Map(filasNucleo.map((f) => [f.id, f.nodos_origen ?? null]));
    const actividades = armarSnapshot(filasNucleo as unknown as FilaChecklistSnapshot[]).actividades.map((a) => ({
      id: a.id,
      indice: a.indice,
      titulo: a.titulo,
      nodos_origen: nodosPorId.get(a.id) ?? null,
    }));
    const idsDelPlan = new Set(filasNucleo.map((f) => f.id));
    // AUD-09 M03: el Registro del ciclo vigente, igual que la pantalla.
    const filasVigentes = accionesDelCicloVigente(
      ((filasMundo ?? []) as unknown as Array<Record<string, unknown>>).map((f) => ({ ...f, dominio })) as Array<{ plan_id: string | null; dominio: string }>,
      planes
    );
    const entradas = armarRegistro(filasVigentes as unknown as FilaRespuesta[], actividades, idsDelPlan);
    const nombreDom = nombreMundo(dominio);
    const generado = new Date().toISOString();
    return NextResponse.json({
      titulo: interpolar(tDoc.tituloRegistro, { mundo: nombreDom }),
      nombre,
      archivo: nombreArchivo(nombre, interpolar(tDoc.tituloRegistro, { mundo: nombreDom })),
      markdown: [
        interpolar(tDoc.encabezadoRegistro, { nombre, mundo: nombreDom, fecha: fechaHumanaCorta(generado) }),
        "",
        registroMarkdown(nombreDom, entradas),
      ].join("\n"),
    });
  }

  if (doc === CLAVE_BITACORA) {
    const generado = new Date().toISOString();
    const entradas = await cargarEntradasBitacora(supabase, projectId, proyecto, nombre);
    // Fase 3 (tanda 4): la bitácora GLOBAL etiqueta cada entrada con su espacio
    // (nombre de cara), con RUIDO CERO — un proyecto solo-core no etiqueta nada.
    const hayMundos = proyectoTieneMundos(entradas);
    return NextResponse.json({
      titulo: tDoc.tituloBitacora,
      nombre,
      archivo: nombreArchivo(nombre, tDoc.archivoBitacora),
      markdown: bitacoraMarkdown(nombre, entradas, generado, undefined, (e) =>
        etiquetaEspacio(e.dominio, hayMundos, nombreMundo),
      ),
      // El PDF de la bitácora se dibuja estructurado (espina continua), no como
      // markdown; el .md sigue saliendo del mismo texto de arriba.
      papel: { entradas },
    });
  }

  if (doc === CLAVE_ANALISIS) {
    // El análisis del proyecto como documento: .md = el informe de analytics;
    // PDF = la página VISUAL con toda la estadística (AnalisisPapel), no ya el
    // resumen "Cómo te fue". Centralizado aquí; la pantalla de Análisis no tiene
    // su propio botón de descarga.
    const ahora = new Date().toISOString();
    const entrada = await cargarEntradaAnalytics(supabase, projectId, proyecto, ahora);
    const analytics = calcularAnalytics(entrada);
    const u = analytics.universal;
    const c = analytics.cumplimiento;
    const restantes = Math.max(0, u.accionesVigente.total - u.accionesVigente.hechas);
    const semanas = u.ritmoAccionesPorSemana > 0 ? Math.ceil(restantes / u.ritmoAccionesPorSemana) : 0;
    const proyeccion =
      !realizadaAt && restantes > 0 && u.ritmoAccionesPorSemana > 0
        ? {
            restantes,
            semanas,
            ritmo: u.ritmoAccionesPorSemana,
            fechaHumana: fechaHumanaCorta(new Date(Date.parse(ahora) + semanas * 7 * 86_400_000).toISOString()),
          }
        : null;
    const analisis: AnalisisPapelData = {
      cerrada: Boolean(realizadaAt),
      avance: { hechas: u.accionesVigente.hechas, total: u.accionesVigente.total },
      cifras: { dias: u.duracionTotalDias, ritmo: u.ritmoAccionesPorSemana, racha: u.rachaMasLargaDias, ciclos: u.ciclosDePlan, mundos: u.mundos },
      retiradas: u.retiradas.length,
      avancePorSemana: u.avancePorSemana,
      distribucionEstados: u.distribucionEstados,
      accionesPorEtapa: u.accionesPorEtapa,
      proyeccion,
      cumplimiento: c
        ? {
            adelantadas: c.adelantadas,
            aTiempo: c.aTiempo,
            tardias: c.tardias,
            pctAdelantadas: c.pctAdelantadas,
            pctATiempo: c.pctATiempo,
            pctTardias: c.pctTardias,
            desviacionMediaDias: c.desviacionMediaDias,
            porEtapa: c.porEtapa,
          }
        : null,
    };
    return NextResponse.json({
      titulo: tDoc.tituloAnalisis,
      nombre,
      archivo: nombreArchivo(nombre, tDoc.archivoAnalisis),
      markdown: informeMarkdown(nombre, analytics, realizadaAt, nombreMundo, (await actasVigentes(supabase, projectId)).core ?? null),
      papel: { analisis },
    });
  }

  if (doc !== CLAVE_EXPEDIENTE) {
    const titulado = titulosDeCiclos(ciclos).find(({ ciclo }) => `ciclo:${ciclo.planId}` === doc);
    if (!titulado) {
      return NextResponse.json({ error: t.noEncontrado }, { status: 404 });
    }
    return NextResponse.json({
      titulo: titulado.titulo,
      nombre,
      archivo: nombreArchivo(nombre, titulado.titulo),
      markdown: cicloMarkdown(nombre, titulado.titulo, titulado.ciclo),
    });
  }

  // ── Expediente completo ────────────────────────────────────────────────
  // AUD-09 M02: el Expediente cuenta el ciclo vigente de cada espacio, como el
  // tablero; los ciclos anteriores viven en sus propias secciones.
  const todasAcciones = accionesDelCicloVigente(await cargarAcciones(supabase, projectId), planes);
  // Solo el viaje principal en la sección de acciones del core: las de un mundo
  // van dentro de SU sección (cada cosa en su carril).
  const acciones: AccionExpediente[] = todasAcciones.filter((i) => esCore(i.dominio)).map(aAccion);

  let unlocks: Array<{ dominio: string; completado_at?: string | null }> = [];
  const conCierre = await supabase.from("project_unlocks").select("dominio, completado_at").eq("project_id", projectId);
  if (!conCierre.error) unlocks = (conCierre.data ?? []) as typeof unlocks;
  else {
    const previo = await supabase.from("project_unlocks").select("dominio").eq("project_id", projectId);
    // AUD-09 M18: si tampoco la lectura mínima responde, no es "sin mundos".
    if (previo.error) throw new LecturaFallidaError("los mundos", previo.error);
    unlocks = (previo.data ?? []) as typeof unlocks;
  }

  const ahora = new Date().toISOString();
  const entrada = await cargarEntradaAnalytics(supabase, projectId, proyecto, ahora);
  const analytics = calcularAnalytics(entrada);
  const entradasBita = await cargarEntradasBitacora(supabase, projectId, proyecto, nombre);

  // Fase 3 (tanda 5): cada mundo se COMPLETA con su plan, SUS acciones y su cómo
  // te fue (su capa universal ya calculada en analytics.mundos, sin recalcular).
  const mundos: MundoExpediente[] = unlocks.map((u) => {
    const planMundo = planes.filter((p) => p.dominio === u.dominio && ETIQUETAS_CICLO.includes(p.etiqueta)).at(-1);
    const am = analytics.mundos.find((m) => m.dominio === u.dominio);
    return {
      nombre: nombreMundo(u.dominio),
      contenidoMd: planMundo ? sinProcedencia(planMundo.contenido_md) : null,
      completadoAt: u.completado_at ?? null,
      acciones: todasAcciones.filter((i) => i.dominio === u.dominio).map(aAccion),
      comoTeFueMd: am ? resumenEspacioMd(am.universal, am.cumplimiento).join("\n") : null,
    };
  });

  const organizadorMd = (() => {
    const org = planes.find((p) => esCore(p.dominio) && p.etiqueta === "organizador");
    return org ? sinProcedencia(org.contenido_md) : null;
  })();
  const numerosMd = (() => {
    const num = planes.filter((p) => p.etiqueta === "reporte_numeros").at(-1);
    return num ? sinProcedencia(num.contenido_md) : null;
  })();
  const informeMd = acciones.length ? informeMarkdown(nombre, analytics, realizadaAt, nombreMundo, (await actasVigentes(supabase, projectId)).core ?? null) : null;

  const baseDoc = {
    nombre,
    entradaOriginal: proyecto.entrada_original ?? "",
    creadaAt: proyecto.created_at,
    realizadaAt,
    cierreMotivo: proyecto.cierre_motivo ?? null,
    organizadorMd,
    ciclos,
    acciones,
    numerosMd,
    mundos,
    generadoAt: ahora,
  };

  // .md descargable: el texto COMPLETO (una sola verdad), con el informe y la
  // secuencia como markdown.
  const markdown = expedienteMarkdown({
    ...baseDoc,
    informeMd,
    // Fase 3 (tanda 4): la secuencia del expediente etiqueta cada entrada con su
    // espacio (nombre de cara), con RUIDO CERO (solo-core no etiqueta nada).
    bitacoraMd: bitacoraCuerpo(entradasBita, 3, (e) =>
      etiquetaEspacio(e.dominio, proyectoTieneMundos(entradasBita), nombreMundo),
    ).join("\n"),
  });

  // PDF: el CUERPO va como markdown (sin informe ni secuencia), y el resumen
  // "Cómo te fue" + la secuencia se dibujan ESTRUCTURADOS (páginas de papel de
  // Design), en su propia página. Los datos del resumen salen de analytics.
  const bodyMarkdown = expedienteMarkdown({ ...baseDoc, informeMd: null, bitacoraMd: null });
  const u = analytics.universal;
  // AUD-09 M39: el "Cómo te fue" habla con los datos (modo y cumplimiento), no
  // con un veredicto fijo.
  const camino = resumenCaminoExpediente({
    cerrada: Boolean(realizadaAt),
    modo: analytics.modoCamino,
    cumplimiento: analytics.cumplimiento,
  });
  const pendientes = Math.max(0, u.accionesVigente.total - u.accionesVigente.hechas);
  const resumen = acciones.length
    ? {
        cerrada: Boolean(realizadaAt),
        cierreMotivo: proyecto.cierre_motivo ?? null,
        intro: camino.intro,
        dias: u.duracionTotalDias,
        accionesCumplidas: u.accionesVigente.hechas,
        hitos: analytics.hitos
          .filter((h) => h.tipo !== "accion")
          .map((h) => ({ fecha: h.fecha, nombre: h.tipo === "realizada" ? tDoc.hitoRealizado : h.etiqueta })),
        loQueMovio: camino.loQueMovio,
        loQuePendiente: u.retiradas.length
          ? interpolar(formaPlural(idioma, pendientes, tDoc.loQuePendienteConRetiradas), {
              n: pendientes,
              retiradas: u.retiradas.length,
            })
          : interpolar(formaPlural(idioma, pendientes, tDoc.loQuePendiente), { n: pendientes }),
      }
    : null;

  return NextResponse.json({
    titulo: tDoc.tituloExpediente,
    nombre,
    archivo: nombreArchivo(nombre, tDoc.tituloExpediente),
    markdown,
    papel: { bodyMarkdown, resumen, entradas: entradasBita },
  });
}

/** AUD-09 M18: una lectura fallida en cualquier punto de los documentos se dice
 * (503 con el mismo mensaje honesto), nunca se descarga un papel con ceros. */
export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
  try {
    return await generarDocumentos(request, { params });
  } catch (e) {
    if (e instanceof LecturaFallidaError) return NextResponse.json({ error: mensajeLecturaFallida(idiomaDeRequest(request)) }, { status: 503 });
    throw e;
  }
}
