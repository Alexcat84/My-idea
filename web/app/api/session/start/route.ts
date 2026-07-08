/**
 * POST /api/session/start - Fase 3.0: port de modo_nuevo_proyecto (rama
 * "proyecto nuevo") en engine/prototipo_motor.py. Clasifica la entrada
 * (Capa 1), crea el proyecto+sesion, y corre el primer turno del bucle de
 * entrevista (avanzarTurno) -- exactamente lo que el CLI hace entre
 * clasificar_entrada() y la primera pregunta real que el usuario ve.
 */
import { NextResponse } from "next/server";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { responderResultadoTurno } from "@/lib/apiSesion";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { usoVacio } from "@/lib/costmeter";
import { crearProyecto, crearSesion } from "@/lib/db";
import { clasificarEntrada } from "@/lib/engine/clasificar";
import { cargarEntrySeeds, cargarGrafo, cargarPreguntasCache } from "@/lib/engine/graph";
import { avanzarTurno, estadoInicial } from "@/lib/engine/recorrido";
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
  if (typeof texto !== "string" || texto.trim().length === 0) {
    return NextResponse.json({ error: "falta 'texto'" }, { status: 400 });
  }
  if (texto.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json(
      { error: `'texto' supera el maximo de ${MAX_LARGO_TEXTO_USUARIO} caracteres` },
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

  const graph = cargarGrafo();
  const entrySeeds = cargarEntrySeeds();
  const preguntasCache = cargarPreguntasCache();
  const families = cargarFamilies();

  const projectId = await crearProyecto(supabase, user.id, texto);
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

  return responderResultadoTurno(supabase, projectId, sessionId, resultado, resultado.acumulado);
}
