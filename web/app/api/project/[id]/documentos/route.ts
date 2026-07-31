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
import type { AnalisisPapelData } from "@/app/ui/AnalisisPapel";
import { calcularAnalytics, informeMarkdown } from "@/lib/analytics";
import { fechaHumanaCorta } from "@/lib/fechas";
import catalogo from "@/lib/assets/packs_catalog.json";
import { cargarEntradaAnalytics } from "@/lib/analyticsEntrada";
import { bitacoraCuerpo, bitacoraMarkdown } from "@/lib/bitacoraCliente";
import { cargarEntradasBitacora } from "@/lib/bitacoraDatos";
import { obtenerProyecto } from "@/lib/db";
import {
  CLAVE_ANALISIS,
  CLAVE_BITACORA,
  CLAVE_EXPEDIENTE,
  cicloMarkdown,
  expedienteMarkdown,
  indiceDeDocumentos,
  nombreArchivo,
  titulosDeCiclos,
  type AccionExpediente,
  type CicloExpediente,
  type MundoExpediente,
} from "@/lib/expediente";
import { nombreDeIdea } from "@/lib/ideas";
import { sinProcedencia } from "@/lib/planParser";
import { createClient } from "@/lib/supabase/server";

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

export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
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

  const { data: sesionesRaw } = await supabase
    .from("sessions")
    .select("id, created_at, tipo, dominio")
    .eq("project_id", projectId);
  const sesiones = (sesionesRaw ?? []) as FilaSesion[];
  const idsSesiones = sesiones.map((s) => s.id);
  const { data: planesRaw } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("id, etiqueta, contenido_md, created_at, dominio, baseline_confirmada_at")
        .in("session_id", idsSesiones)
        .order("created_at", { ascending: true })
    : { data: [] };
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

  const doc = new URL(request.url).searchParams.get("doc");
  if (!doc) {
    return NextResponse.json({ nombre, documentos: indiceDeDocumentos(ciclos, realizadaAt) });
  }

  if (doc === CLAVE_BITACORA) {
    const generado = new Date().toISOString();
    const entradas = await cargarEntradasBitacora(supabase, projectId, proyecto, nombre);
    return NextResponse.json({
      titulo: "Tu bitácora",
      nombre,
      archivo: nombreArchivo(nombre, "Tu bitacora"),
      markdown: bitacoraMarkdown(nombre, entradas, generado),
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
    const nombreDom = (dom: string) => (dom === "core" ? "Tu viaje principal" : nombreMundo(dom));
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
            porDominio: c.porDominio.map((d) => ({
              nombre: nombreDom(d.dominio),
              adelantadas: d.adelantadas,
              aTiempo: d.aTiempo,
              tardias: d.tardias,
              completado: analytics.mundos.some((m) => m.dominio === d.dominio && m.completadoAt),
            })),
          }
        : null,
    };
    return NextResponse.json({
      titulo: "Análisis del proyecto",
      nombre,
      archivo: nombreArchivo(nombre, "Analisis del proyecto"),
      markdown: informeMarkdown(nombre, analytics, realizadaAt, nombreMundo),
      papel: { analisis },
    });
  }

  if (doc !== CLAVE_EXPEDIENTE) {
    const titulado = titulosDeCiclos(ciclos).find(({ ciclo }) => `ciclo:${ciclo.planId}` === doc);
    if (!titulado) {
      return NextResponse.json({ error: "documento no encontrado" }, { status: 404 });
    }
    return NextResponse.json({
      titulo: titulado.titulo,
      nombre,
      archivo: nombreArchivo(nombre, titulado.titulo),
      markdown: cicloMarkdown(nombre, titulado.titulo, titulado.ciclo),
    });
  }

  // ── Expediente completo ────────────────────────────────────────────────
  // no_aplica_motivo llega con la 030: se reintenta sin ella si aún no está.
  const COLS_ACC = "dominio, etapa, texto, estado, completed_at, fecha_base, orden";
  const accConMotivo = await supabase
    .from("checklist_items")
    .select(`${COLS_ACC}, no_aplica_motivo`)
    .eq("project_id", projectId)
    .order("etapa", { ascending: true })
    .order("orden", { ascending: true });
  const itemsRaw = accConMotivo.error
    ? (
        await supabase
          .from("checklist_items")
          .select(COLS_ACC)
          .eq("project_id", projectId)
          .order("etapa", { ascending: true })
          .order("orden", { ascending: true })
      ).data
    : accConMotivo.data;
  // Solo el viaje principal: las acciones de un mundo se cuentan dentro de su
  // propia sección, no mezcladas con las del core (regla de no mezclar
  // procesos: cada cosa en su carril).
  const acciones: AccionExpediente[] = (
    (itemsRaw ?? []) as Array<{
      dominio: string | null;
      etapa: number;
      texto: string;
      estado: string;
      completed_at: string | null;
      fecha_base: string | null;
      no_aplica_motivo?: string | null;
    }>
  )
    .filter((i) => esCore(i.dominio))
    .map((i) => ({
      etapa: i.etapa,
      texto: i.texto,
      estado: i.estado,
      completedAt: i.completed_at,
      fechaBase: i.fecha_base,
      noAplicaMotivo: i.no_aplica_motivo ?? null,
    }));

  let unlocks: Array<{ dominio: string; completado_at?: string | null }> = [];
  try {
    const { data, error } = await supabase
      .from("project_unlocks")
      .select("dominio, completado_at")
      .eq("project_id", projectId);
    if (!error) unlocks = (data ?? []) as typeof unlocks;
    else {
      const { data: previo } = await supabase.from("project_unlocks").select("dominio").eq("project_id", projectId);
      unlocks = (previo ?? []) as typeof unlocks;
    }
  } catch {
    unlocks = [];
  }
  const mundos: MundoExpediente[] = unlocks.map((u) => {
    const planMundo = planes.filter((p) => p.dominio === u.dominio && ETIQUETAS_CICLO.includes(p.etiqueta)).at(-1);
    return {
      nombre: nombreMundo(u.dominio),
      contenidoMd: planMundo ? sinProcedencia(planMundo.contenido_md) : null,
      completadoAt: u.completado_at ?? null,
    };
  });

  const ahora = new Date().toISOString();
  const entrada = await cargarEntradaAnalytics(supabase, projectId, proyecto, ahora);
  const analytics = calcularAnalytics(entrada);
  const entradasBita = await cargarEntradasBitacora(supabase, projectId, proyecto, nombre);

  const organizadorMd = (() => {
    const org = planes.find((p) => esCore(p.dominio) && p.etiqueta === "organizador");
    return org ? sinProcedencia(org.contenido_md) : null;
  })();
  const numerosMd = (() => {
    const num = planes.filter((p) => p.etiqueta === "reporte_numeros").at(-1);
    return num ? sinProcedencia(num.contenido_md) : null;
  })();
  const informeMd = acciones.length ? informeMarkdown(nombre, analytics, realizadaAt, nombreMundo) : null;

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
    bitacoraMd: bitacoraCuerpo(entradasBita, 3).join("\n"),
  });

  // PDF: el CUERPO va como markdown (sin informe ni secuencia), y el resumen
  // "Cómo te fue" + la secuencia se dibujan ESTRUCTURADOS (páginas de papel de
  // Design), en su propia página. Los datos del resumen salen de analytics.
  const bodyMarkdown = expedienteMarkdown({ ...baseDoc, informeMd: null, bitacoraMd: null });
  const u = analytics.universal;
  const c = analytics.cumplimiento;
  const resumen = acciones.length
    ? {
        cerrada: Boolean(realizadaAt),
        cierreMotivo: proyecto.cierre_motivo ?? null,
        intro: realizadaAt
          ? "Empezaste con una idea y llegaste hasta el cierre. Esto es lo que dejó el camino."
          : "Vas por buen camino. Esto es lo que llevas hasta aquí.",
        dias: u.duracionTotalDias,
        accionesCumplidas: u.accionesHechas,
        hitos: analytics.hitos
          .filter((h) => h.tipo !== "accion")
          .map((h) => ({ fecha: h.fecha, nombre: h.tipo === "realizada" ? "Realizado" : h.etiqueta })),
        loQueMovio:
          c && c.replanificaciones > 0
            ? `Frente a tu plan inicial te moviste ${c.desviacionVsInicialDias >= 0 ? "+" : ""}${c.desviacionVsInicialDias.toFixed(1)} días de media a lo largo de ${c.replanificaciones} replanificación${c.replanificaciones === 1 ? "" : "es"}. Ajustar el mapa fue parte del método.`
            : "Mantuviste tu ritmo cerca de tu plan a lo largo del camino.",
        loQuePendiente: `Quedan ${Math.max(0, u.accionesVigente.total - u.accionesVigente.hechas)} acciones por delante${u.retiradas.length ? ` y ${u.retiradas.length} que retiraste con su motivo` : ""}. Nada se borró: siguen en tu expediente.`,
      }
    : null;

  return NextResponse.json({
    titulo: "Expediente completo",
    nombre,
    archivo: nombreArchivo(nombre, "Expediente completo"),
    markdown,
    papel: { bodyMarkdown, resumen, entradas: entradasBita },
  });
}
