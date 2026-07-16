/**
 * POST /api/project/[id]/world/[pack]/start — Fase 3.5: arranca la
 * exploración de un mundo activado.
 *
 * Requisitos en orden: unlock (403 amable si no existe la fila — el
 * muro), plan core previo (el mundo se construye SOBRE la idea ya
 * trabajada), y evaluacionBrecha determinística (estado_vivo + tipo de
 * oferta + fase → semilla del pack, cero LLM). La sesión nace tipo
 * 'inicial' con dominio=pack; sus planes heredan ese dominio y derivan
 * checklist con él (la ruta del plan ya lo hace sola).
 *
 * Pre-integración (línea de ensamblaje pendiente): si la semilla aún no
 * está en el grafo compilado de la web, 503 con palabras de persona —
 * el mundo existe comercialmente pero su contenido llega con
 * integrar_packs.py.
 */
import { NextResponse } from "next/server";
import { responderResultadoTurno } from "@/lib/apiSesion";
import catalogo from "@/lib/assets/packs_catalog.json";
import { usoVacio } from "@/lib/costmeter";
import { crearSesion, dominiosDesbloqueados, nodosCubiertos, obtenerProyecto } from "@/lib/db";
import { PACK_CLICKS_PACK } from "@/lib/dbContract";
import { evaluacionBrecha } from "@/lib/engine/evaluacionBrecha";
import { cargarGrafo, cargarPreguntasCache, etiquetaArbol, obtenerPregunta } from "@/lib/engine/graph";
import { estadoInicial } from "@/lib/engine/recorrido";
import { identidadLimite, MENSAJE_FUSIBLE, MENSAJE_LIMITE, verificarFusibleGlobal, verificarLimiteDiario } from "@/lib/rateLimit";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string; pack: string }> }) {
  const { id: projectId, pack } = await params;

  const entrada = (catalogo.packs as Array<{ clave: string; nombre: string; promesa: string }>).find(
    (p) => p.clave === pack
  );
  if (!entrada || !(PACK_CLICKS_PACK as readonly string[]).includes(pack)) {
    return NextResponse.json({ error: "ese mundo no existe" }, { status: 404 });
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

  // El muro: sin fila en project_unlocks, el mundo no existe para esta idea.
  const { data: unlock } = await supabase
    .from("project_unlocks")
    .select("id")
    .eq("project_id", projectId)
    .eq("dominio", pack)
    .limit(1);
  if (!unlock || unlock.length === 0) {
    return NextResponse.json(
      { error: `El mundo "${entrada.nombre}" aún no está activado para esta idea.` },
      { status: 403 }
    );
  }

  // El mundo se construye sobre la idea ya trabajada: exige plan core.
  const { data: sesionesProyecto } = await supabase.from("sessions").select("id").eq("project_id", projectId);
  const sessionIds = (sesionesProyecto ?? []).map((s: { id: string }) => s.id);
  const { data: planesCore } = sessionIds.length
    ? await supabase.from("plans").select("id").in("session_id", sessionIds).in("etiqueta", ["inicial", "completo"]).limit(1)
    : { data: [] };
  if (!planesCore || planesCore.length === 0) {
    return NextResponse.json(
      { error: "Primero genera el plan de tu idea — el mundo se construye sobre él." },
      { status: 409 }
    );
  }

  const graph = cargarGrafo();
  const preguntasCache = cargarPreguntasCache();
  const families = cargarFamilies();
  const cubiertos = await nodosCubiertos(supabase, projectId);
  const estadoVivo = (proyecto.estado_vivo as string | null) ?? null;

  const brecha = evaluacionBrecha(
    pack,
    estadoVivo,
    (proyecto.tipo_oferta as string | null) ?? null,
    (proyecto.fase_actual as string | null) ?? "ideacion",
    cubiertos
  );
  if (!brecha) {
    return NextResponse.json({ error: "Ya recorriste todas las puertas de este mundo." }, { status: 409 });
  }
  if (!(brecha.semillaId in graph)) {
    console.warn(`world/start: semilla '${brecha.semillaId}' de '${pack}' no está en el grafo (línea de ensamblaje pendiente)`);
    return NextResponse.json(
      { error: "Este mundo se está preparando — muy pronto podrás explorarlo." },
      { status: 503 }
    );
  }

  // El límite se cobra al FINAL de las validaciones (hallado por el vuelo:
  // cobrarlo antes quemaba un arranque en el 503 de pre-integración).
  // Pre-beta: fusible global ANTES de cobrar creditos y de tocar la API.
  const fusible = await verificarFusibleGlobal(user.email);
  if (!fusible.permitido) {
    return NextResponse.json({ error: MENSAJE_FUSIBLE }, { status: 503 });
  }
  const limite = await verificarLimiteDiario(identidadLimite(user.id, request), user.email);
  if (!limite.permitido) {
    return NextResponse.json({ error: MENSAJE_LIMITE }, { status: 429 });
  }

  const mensaje = `Exploración del mundo "${entrada.nombre}" (${entrada.promesa}) para mi idea. Contexto actual: ${
    estadoVivo ?? (proyecto.entrada_original as string | null) ?? ""
  }`;
  const sessionId = await crearSesion(supabase, user.id, projectId, "inicial", mensaje, brecha.semillaId, pack);

  const dominios = await dominiosDesbloqueados(supabase, projectId);
  const estado = estadoInicial({
    actualId: brecha.semillaId,
    perfilSesion: estadoVivo ?? "",
    textoOriginal: mensaje,
    nodosCubiertosPrevios: [...cubiertos],
    dominiosDesbloqueados: dominios,
    // Fase 4.3: el motor debe saber que esta es una sesion DE MUNDO. Sin esto,
    // 'salir' cerraria en vez de re-elegir puerta y el usuario que pago por
    // este mundo se quedaria mirando una pantalla muda.
    dominioSesion: pack,
  });

  // Fase v1.3.2 (cazado por el vuelo, dos veces): la PRIMERA pregunta del
  // mundo es la CACHEADA de la semilla que eligió evaluacionBrecha —
  // determinística, cero LLM, igual que la elección de la semilla. Ni
  // intérprete (con un estado_vivo cargado de urgencias core juzgaba la
  // semilla "desalineada" y salía en el turno 0: el usuario pagó por
  // explorar ESTE mundo) ni preguntaDirigida (el mismo estado_vivo hacía
  // que la reescritura se comiera al nodo). Desde el turno 2, el
  // intérprete manda como siempre.
  const pregunta = obtenerPregunta(brecha.semillaId, graph[brecha.semillaId], preguntasCache);
  const estadoConPregunta = {
    ...estado,
    preguntaPendiente: pregunta,
    ultimasPreguntas: [pregunta],
  };
  const resultado = {
    tipo: "pregunta" as const,
    estado: estadoConPregunta,
    pregunta,
    acumulado: usoVacio(),
    nodosNuevos: [],
  };

  const puerta = {
    id: brecha.semillaId,
    titulo: graph[brecha.semillaId]?.titulo_concepto ?? brecha.semillaId,
    etiqueta: etiquetaArbol(brecha.semillaId, graph),
    modo: "conversado" as const,
  };
  return responderResultadoTurno(supabase, projectId, sessionId, resultado, resultado.acumulado, [puerta]);
}
