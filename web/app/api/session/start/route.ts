/**
 * POST /api/session/start - Fase 3.0: port de modo_nuevo_proyecto (rama
 * "proyecto nuevo") en engine/prototipo_motor.py. Clasifica la entrada
 * (Capa 1), crea el proyecto+sesion, y corre el primer turno del bucle de
 * entrevista (avanzarTurno) -- exactamente lo que el CLI hace entre
 * clasificar_entrada() y la primera pregunta real que el usuario ve.
 *
 * Fase 3.2: acepta `project_id` opcional -- el flujo del brief manda toda
 * idea nueva primero por el organizador (que ya creo el proyecto), y
 * "Continuar el desarrollo de mi idea" arranca la entrevista sobre ESE
 * mismo proyecto en vez de crear uno nuevo. Sin project_id, el
 * comportamiento original (crear proyecto) se mantiene intacto (vuelo.ts
 * fase 2 y el flujo del CLI dependen de el).
 */
import { NextResponse } from "next/server";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { responderResultadoTurno } from "@/lib/apiSesion";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { usoVacio } from "@/lib/costmeter";
import { crearProyecto, crearSesion, obtenerProyecto } from "@/lib/db";
import { clasificarEntrada } from "@/lib/engine/clasificar";
import { cargarEntrySeeds, cargarGrafo, cargarPreguntasCache } from "@/lib/engine/graph";
import { avanzarTurno, estadoInicial } from "@/lib/engine/recorrido";
import { MENSAJE_LIMITE, verificarLimiteDiario } from "@/lib/rateLimit";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido, se esperaba JSON" }, { status: 400 });
  }
  const texto = (body as { texto?: unknown } | null)?.texto;
  const projectIdSolicitado = (body as { project_id?: unknown } | null)?.project_id;
  if (typeof texto !== "string" || texto.trim().length === 0) {
    return NextResponse.json({ error: "falta 'texto'" }, { status: 400 });
  }
  if (texto.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json(
      { error: `'texto' supera el maximo de ${MAX_LARGO_TEXTO_USUARIO} caracteres` },
      { status: 400 }
    );
  }
  if (projectIdSolicitado !== undefined && typeof projectIdSolicitado !== "string") {
    return NextResponse.json({ error: "'project_id' debe ser un string" }, { status: 400 });
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }

  const limite = await verificarLimiteDiario(user.id, user.email);
  if (!limite.permitido) {
    return NextResponse.json({ error: MENSAJE_LIMITE }, { status: 429 });
  }

  const graph = cargarGrafo();
  const entrySeeds = cargarEntrySeeds();
  const preguntasCache = cargarPreguntasCache();
  const families = cargarFamilies();

  let projectId: string;
  if (projectIdSolicitado) {
    // RLS garantiza que solo se ve el proyecto propio; si no aparece, o
    // no existe o no es de este usuario -- misma respuesta en ambos casos.
    const proyecto = await obtenerProyecto(supabase, projectIdSolicitado);
    if (!proyecto) {
      return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
    }
    projectId = projectIdSolicitado;
  } else {
    projectId = await crearProyecto(supabase, user.id, texto);
  }
  const sessionId = await crearSesion(supabase, user.id, projectId, "inicial", texto);

  const client = createAnthropicClient();
  let acumulado = usoVacio();

  const clasificacion = await clasificarEntrada(client, texto, entrySeeds, graph, acumulado);
  acumulado = clasificacion.acumulado;

  const estado = estadoInicial({
    actualId: clasificacion.puertaId,
    perfilSesion: clasificacion.perfilSesion,
    textoOriginal: texto,
  });

  const resultado = await avanzarTurno({
    client,
    graph,
    families,
    preguntasCache,
    estado,
    respuestaUsuario: null,
    acumulado,
    dbSessionId: sessionId,
  });

  // La puerta de entrada vive en la ruta DESDE estadoInicial, asi que el
  // diff de nodos nuevos del turno nunca la incluye -- se antepone aqui
  // para que el arbol del cliente arranque por donde de verdad entro.
  const puerta = {
    id: clasificacion.puertaId,
    titulo: graph[clasificacion.puertaId]?.titulo_concepto ?? clasificacion.puertaId,
    modo: "conversado" as const,
  };

  return responderResultadoTurno(supabase, projectId, sessionId, resultado, resultado.acumulado, [puerta]);
}
