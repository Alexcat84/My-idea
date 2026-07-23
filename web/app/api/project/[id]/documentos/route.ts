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
import { calcularAnalytics, informeMarkdown } from "@/lib/analytics";
import catalogo from "@/lib/assets/packs_catalog.json";
import { cargarEntradaAnalytics } from "@/lib/analyticsEntrada";
import { obtenerProyecto } from "@/lib/db";
import {
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
};

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

  const { data: sesiones } = await supabase.from("sessions").select("id").eq("project_id", projectId);
  const idsSesiones = ((sesiones ?? []) as Array<{ id: string }>).map((s) => s.id);
  const { data: planesRaw } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("id, etiqueta, contenido_md, created_at, dominio")
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

  const doc = new URL(request.url).searchParams.get("doc");
  if (!doc) {
    return NextResponse.json({ nombre, documentos: indiceDeDocumentos(ciclos, realizadaAt) });
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
  const { data: itemsRaw } = await supabase
    .from("checklist_items")
    .select("dominio, etapa, texto, estado, completed_at, fecha_base, orden")
    .eq("project_id", projectId)
    .order("etapa", { ascending: true })
    .order("orden", { ascending: true });
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
    }>
  )
    .filter((i) => esCore(i.dominio))
    .map((i) => ({
      etapa: i.etapa,
      texto: i.texto,
      estado: i.estado,
      completedAt: i.completed_at,
      fechaBase: i.fecha_base,
    }));

  const packs = (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs;
  const nombreMundo = (dominio: string) => packs.find((p) => p.clave === dominio)?.nombre ?? dominio;

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

  const markdown = expedienteMarkdown({
    nombre,
    entradaOriginal: proyecto.entrada_original ?? "",
    creadaAt: proyecto.created_at,
    realizadaAt,
    cierreMotivo: proyecto.cierre_motivo ?? null,
    organizadorMd: (() => {
      const org = planes.find((p) => esCore(p.dominio) && p.etiqueta === "organizador");
      return org ? sinProcedencia(org.contenido_md) : null;
    })(),
    ciclos,
    acciones,
    numerosMd: (() => {
      const num = planes.filter((p) => p.etiqueta === "reporte_numeros").at(-1);
      return num ? sinProcedencia(num.contenido_md) : null;
    })(),
    mundos,
    // El informe entero solo tiene sentido cuando hay camino andado; si no,
    // el expediente ya cuenta lo mismo con menos ruido.
    informeMd: acciones.length ? informeMarkdown(nombre, analytics, realizadaAt, nombreMundo) : null,
    generadoAt: ahora,
  });

  return NextResponse.json({
    titulo: "Expediente completo",
    nombre,
    archivo: nombreArchivo(nombre, "Expediente completo"),
    markdown,
  });
}
