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
import { elegir } from "@/lib/i18n/config";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_SESION } from "@/lib/i18n/mensajes/servidorSesion";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { responderResultadoTurno } from "@/lib/apiSesion";
import { MAX_LARGO_TEXTO_USUARIO, MENSAJE_TEXTO_LARGO } from "@/lib/constants";
import { obtenerSesion, type EstadoSesionPersistido } from "@/lib/db";
import { cargarGrafo, cargarPreguntasCache } from "@/lib/engine/graph";
import { avanzarTurno } from "@/lib/engine/recorrido";
import { anclarResultadoTurno } from "@/lib/engine/reformuladorProteccion";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: sessionId } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_SESION, idioma).turno;

  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: r.cuerpoInvalidoJson }, { status: 400 });
  }
  const respuesta = (body as { respuesta?: unknown } | null)?.respuesta;
  if (typeof respuesta !== "string" || respuesta.trim().length === 0) {
    return NextResponse.json({ error: t.faltaRespuesta }, { status: 400 });
  }
  if (respuesta.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json(
      { error: MENSAJE_TEXTO_LARGO, limite: MAX_LARGO_TEXTO_USUARIO },
      { status: 400 }
    );
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  }

  const sesion = await obtenerSesion(supabase, sessionId);
  if (!sesion) {
    return NextResponse.json({ error: r.sesionNoEncontrada }, { status: 404 });
  }
  if (sesion.closed_at) {
    return NextResponse.json({ error: r.conversacionTerminada }, { status: 409 });
  }
  const estadoPersistido = sesion.estado_recorrido as EstadoSesionPersistido | null;
  if (!estadoPersistido) {
    return NextResponse.json(
      { error: r.conversacionSinPendiente },
      { status: 409 }
    );
  }
  if (estadoPersistido.recorrido.fase === "cerrada" || estadoPersistido.recorrido.fase === "listo_para_plan") {
    return NextResponse.json(
      { error: r.conversacionSinPendiente, fase: estadoPersistido.recorrido.fase },
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

  // P2b: en los mundos de protección la pregunta del turno se ancla a una
  // actividad real antes de responder (y de persistirse). En todo lo demás el
  // resultado pasa intacto: el estado no lleva snapshot y el anclaje no corre.
  const anclado = await anclarResultadoTurno(client, resultado, resultado.acumulado);

  return responderResultadoTurno(
    supabase,
    sesion.project_id,
    sessionId,
    anclado.resultado,
    anclado.acumulado,
    [],
    turnos,
    idioma
  );
}
