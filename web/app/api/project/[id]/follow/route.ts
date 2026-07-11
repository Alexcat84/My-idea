/**
 * POST /api/project/[id]/follow — Fase 3.3: port de modo_seguir
 * (engine/prototipo_motor.py línea 2801), el hueco que jamás se había
 * portado. El ritual de 3 tarjetas del frontend (checklist actualizado +
 * detalles + enfoque) entra aquí; el handler:
 *
 *   a. lee estados+notas del checklist del ÚLTIMO plan y compone el
 *      mensaje "qué ha pasado" con componerMensajeSeguimiento — ese texto
 *      queda auditable como mensaje_entrada de la sesión (bitácora);
 *   b. transcribe la entrada de modo_seguir: sesión tipo 'seguimiento',
 *      puerta por seleccionar_puerta_avanzada (cualquier nodo no cubierto,
 *      estado_vivo como contexto del intérprete), visitados = cubiertos ∪
 *      ruta (nodosCubiertosPrevios), y devuelve el primer turno igual que
 *      session/start. La conversación sigue por /turn y /plan sin cambios;
 *      el plan resultante sale con etiqueta 'seguimiento' (ya cableado) y
 *      deriva SU checklist — el bucle queda encadenado.
 *
 * Cobra 1 arranque del límite diario: es una sesión de entrevista nueva,
 * mismo perfil de costo que session/start.
 */
import { NextResponse } from "next/server";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { responderResultadoTurno } from "@/lib/apiSesion";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { usoVacio } from "@/lib/costmeter";
import { crearSesion, dominiosDesbloqueados, nodosCubiertos, obtenerProyecto } from "@/lib/db";
import type { ChecklistEstado } from "@/lib/dbContract";
import { cargarEntrySeeds, cargarGrafo, cargarPreguntasCache } from "@/lib/engine/graph";
import { seleccionarPuertaAvanzada } from "@/lib/engine/puertaAvanzada";
import { avanzarTurno, estadoInicial } from "@/lib/engine/recorrido";
import { componerMensajeSeguimiento, type ItemParaComponer } from "@/lib/engine/seguimientoComposer";
import { identidadLimite, MENSAJE_FUSIBLE, MENSAJE_LIMITE, verificarFusibleGlobal, verificarLimiteDiario } from "@/lib/rateLimit";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: { detalles?: unknown; enfoque?: unknown };
  try {
    body = await request.json();
  } catch {
    body = {};
  }
  const detalles = typeof body.detalles === "string" ? body.detalles : null;
  const enfoque = typeof body.enfoque === "string" ? body.enfoque : null;
  for (const [campo, valor] of [
    ["detalles", detalles],
    ["enfoque", enfoque],
  ] as const) {
    if (valor && valor.length > MAX_LARGO_TEXTO_USUARIO) {
      return NextResponse.json(
        { error: `'${campo}' supera el maximo de ${MAX_LARGO_TEXTO_USUARIO} caracteres` },
        { status: 400 }
      );
    }
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

  // Pre-beta: fusible global ANTES de cobrar creditos y de tocar la API.
  const fusible = await verificarFusibleGlobal(user.email);
  if (!fusible.permitido) {
    return NextResponse.json({ error: MENSAJE_FUSIBLE }, { status: 503 });
  }
  const limite = await verificarLimiteDiario(identidadLimite(user.id, request), user.email);
  if (!limite.permitido) {
    return NextResponse.json({ error: MENSAJE_LIMITE }, { status: 429 });
  }

  // (a) El checklist del último plan (por fecha de inserción) con estados y
  // notas — la historia real del avance, sin que el usuario la redacte.
  const { data: filas, error: errorItems } = await supabase
    .from("checklist_items")
    .select("plan_id, etapa, texto, destacado, estado, nota, created_at")
    .eq("project_id", projectId)
    .order("created_at", { ascending: false })
    .order("etapa", { ascending: true })
    .order("orden", { ascending: true });
  if (errorItems) {
    return NextResponse.json({ error: "no pudimos leer tu checklist" }, { status: 500 });
  }
  const ultimoPlanId = filas?.[0]?.plan_id ?? null;
  const items: ItemParaComponer[] = (filas ?? [])
    .filter((f) => f.plan_id === ultimoPlanId)
    .map((f) => ({
      etapa: f.etapa as number,
      texto: f.texto as string,
      destacado: f.destacado as boolean,
      estado: f.estado as ChecklistEstado,
      nota: (f.nota as string | null) ?? null,
    }));

  const mensaje = componerMensajeSeguimiento({ items, detalles, enfoque });

  // (b) Entrada de modo_seguir, línea por línea.
  const graph = cargarGrafo();
  const entrySeeds = cargarEntrySeeds();
  const preguntasCache = cargarPreguntasCache();
  const families = cargarFamilies();

  const cubiertos = await nodosCubiertos(supabase, projectId);
  const estadoVivoPrevio = (proyecto.estado_vivo as string | null) ?? null;
  // Fase 3.5: core + unlocks; solo-core si la 016 aún no está aplicada.
  let dominios = ["core"];
  try {
    dominios = await dominiosDesbloqueados(supabase, projectId);
  } catch {
    dominios = ["core"];
  }

  // El mensaje compuesto es el mensaje_entrada de la sesión: bitácora.
  const sessionId = await crearSesion(supabase, user.id, projectId, "seguimiento", mensaje);

  const client = createAnthropicClient();
  const acumulado = usoVacio();

  const puerta = await seleccionarPuertaAvanzada(
    client,
    mensaje,
    estadoVivoPrevio,
    (proyecto.fase_actual as string | null) ?? "ideacion",
    families,
    graph,
    cubiertos,
    entrySeeds,
    acumulado,
    dominios
  );

  const estado = estadoInicial({
    actualId: puerta.puertaId,
    perfilSesion: puerta.perfilSesion,
    textoOriginal: mensaje,
    esSeguimiento: true,
    estadoVivoPrevio,
    nodosCubiertosPrevios: [...cubiertos],
    dominiosDesbloqueados: dominios,
  });

  const resultado = await avanzarTurno({
    client,
    graph,
    families,
    preguntasCache,
    estado,
    respuestaUsuario: null,
    acumulado: puerta.acumulado,
    dbSessionId: sessionId,
  });

  // Igual que session/start: la puerta vive en la ruta desde estadoInicial
  // y el diff de nodos nuevos no la incluye — se antepone para el árbol.
  const nodoPuerta = {
    id: puerta.puertaId,
    titulo: graph[puerta.puertaId]?.titulo_concepto ?? puerta.puertaId,
    modo: "conversado" as const,
  };

  return responderResultadoTurno(supabase, projectId, sessionId, resultado, resultado.acumulado, [nodoPuerta]);
}
