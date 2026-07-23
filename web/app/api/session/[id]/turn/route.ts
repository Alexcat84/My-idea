/**
 * POST /api/session/[id]/turn - Fase 3.0: un turno del bucle de
 * entrevista para una sesion ya arrancada por /api/session/start. Carga
 * el estado resumible (sessions.estado_recorrido), avanza exactamente un
 * paso logico (silencioso multi-hop incluido) via avanzarTurno, y
 * persiste el resultado. Cada invocacion es una funcion serverless
 * independiente -- nunca hay memoria compartida con el turno anterior,
 * por eso todo el estado viaja por Supabase, nunca en memoria del
 * proceso (a diferencia de historial_mensajes en el CLI).
 */
import { NextResponse } from "next/server";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { responderResultadoTurno } from "@/lib/apiSesion";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { obtenerSesion, type EstadoSesionPersistido } from "@/lib/db";
import { cargarGrafo, cargarPreguntasCache } from "@/lib/engine/graph";
import { avanzarTurno } from "@/lib/engine/recorrido";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: sessionId } = await params;

  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido, se esperaba JSON" }, { status: 400 });
  }
  const respuesta = (body as { respuesta?: unknown } | null)?.respuesta;
  if (typeof respuesta !== "string" || respuesta.trim().length === 0) {
    return NextResponse.json({ error: "falta 'respuesta'" }, { status: 400 });
  }
  if (respuesta.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json(
      { error: `'respuesta' supera el maximo de ${MAX_LARGO_TEXTO_USUARIO} caracteres` },
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

  const sesion = await obtenerSesion(supabase, sessionId);
  if (!sesion) {
    return NextResponse.json({ error: "sesion no encontrada" }, { status: 404 });
  }
  if (sesion.closed_at) {
    return NextResponse.json({ error: "la sesion ya esta cerrada" }, { status: 409 });
  }
  const estadoPersistido = sesion.estado_recorrido as EstadoSesionPersistido | null;
  if (!estadoPersistido) {
    return NextResponse.json(
      { error: "la sesion no tiene un turno pendiente; llama a /api/session/start primero" },
      { status: 409 }
    );
  }
  if (estadoPersistido.recorrido.fase === "cerrada" || estadoPersistido.recorrido.fase === "listo_para_plan") {
    return NextResponse.json(
      { error: `la sesion esta en fase '${estadoPersistido.recorrido.fase}', no espera una respuesta nueva` },
      { status: 409 }
    );
  }

  const graph = cargarGrafo();
  const preguntasCache = cargarPreguntasCache();
  const families = cargarFamilies();
  const client = createAnthropicClient();

  const resultado = await avanzarTurno({
    client,
    graph,
    families,
    preguntasCache,
    estado: estadoPersistido.recorrido,
    respuestaUsuario: respuesta,
    acumulado: estadoPersistido.acumulado,
    dbSessionId: sessionId,
  });

  // El recorrido conversado: se cierra la pareja (la pregunta que estaba en
  // pantalla + esta respuesta) y viaja al estado persistido, para que el
  // usuario lo vuelva a ver al reentrar y para el análisis de la beta.
  const turnos = [...(estadoPersistido.turnos ?? [])];
  if (estadoPersistido.ultimaPregunta) {
    turnos.push({
      pregunta: estadoPersistido.ultimaPregunta,
      respuesta,
      en: new Date().toISOString(),
    });
  }

  return responderResultadoTurno(
    supabase,
    sesion.project_id,
    sessionId,
    resultado,
    resultado.acumulado,
    [],
    turnos
  );
}
