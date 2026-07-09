/**
 * apiSesion.ts - Fase 3.0: lo comun entre POST /api/session/start y
 * POST /api/session/[id]/turn despues de llamar a avanzarTurno(): persistir
 * el estado resumible, y si el resultado es "salio", cerrar la sesion y
 * mergear numeros_proyecto/tipo_oferta en el proyecto (igual que
 * _persistir_resultado en Python para el caso "salio" -- el caso "plan"
 * vive en la ruta /api/session/[id]/plan, no aqui).
 */
import { NextResponse } from "next/server";
import type { SupabaseClient } from "@supabase/supabase-js";
import { costoAcumuladoUsd, PRESUPUESTO_SESION_USD_DEFAULT, type UsoAcumulado } from "./costmeter";
import { cerrarSesion, guardarEstadoSesion, mergeNumerosProyecto, mergeTipoOferta } from "./db";
import type { NodoTranscrito, ResultadoTurno } from "./engine/recorrido";

export async function responderResultadoTurno(
  supabase: SupabaseClient,
  projectId: string,
  sessionId: string,
  resultado: ResultadoTurno,
  acumuladoFinal: UsoAcumulado,
  /** Fase 3.2: nodos que el cliente aun no conoce pero que preceden al
   * diff de este turno -- hoy, SOLO la puerta de entrada en /start:
   * estadoInicial la siembra en la ruta ANTES del primer avanzarTurno,
   * asi que nodosNuevosDesdeInicio() jamas la reporta y el arbol de la
   * UI arrancaria sin su primer nodo (gap real cazado por la fase 2e de
   * vuelo.ts: arbol 11 vs ruta 12). */
  nodosPrefijo: NodoTranscrito[] = []
): Promise<NextResponse> {
  await guardarEstadoSesion(supabase, sessionId, { recorrido: resultado.estado, acumulado: acumuladoFinal });
  const costoUsd = costoAcumuladoUsd(acumuladoFinal);

  if (resultado.tipo === "salio") {
    // Fiel a _persistir_resultado en Python: el caso "salio" cierra con
    // ruta=[] (no se persiste la ruta recorrida sin un plan que la use).
    await cerrarSesion(
      supabase,
      projectId,
      sessionId,
      [],
      costoUsd,
      acumuladoFinal.presupuesto_excedido,
      acumuladoFinal.uso_por_componente,
      PRESUPUESTO_SESION_USD_DEFAULT,
      resultado.estado.fallbackEvents
    );
    await mergeNumerosProyecto(supabase, projectId, resultado.estado.numerosDetectadosSesion);
    await mergeTipoOferta(supabase, projectId, resultado.estado.tipoOfertaSesion, resultado.estado.unidadVentaSesion);
    return NextResponse.json({
      project_id: projectId,
      session_id: sessionId,
      tipo: "salio",
      costo_usd: costoUsd,
    });
  }

  if (resultado.tipo === "error_temporal") {
    return NextResponse.json(
      {
        project_id: projectId,
        session_id: sessionId,
        tipo: "error_temporal",
        opciones: resultado.opciones,
        costo_usd: costoUsd,
      },
      { status: 502 }
    );
  }

  if (resultado.tipo === "listo_para_plan") {
    return NextResponse.json({
      project_id: projectId,
      session_id: sessionId,
      tipo: "listo_para_plan",
      evaluacion: resultado.evaluacion,
      nodos_nuevos: [...nodosPrefijo, ...resultado.nodosNuevos],
      costo_usd: costoUsd,
    });
  }

  return NextResponse.json({
    project_id: projectId,
    session_id: sessionId,
    tipo: "pregunta",
    pregunta: resultado.pregunta,
    nodos_nuevos: [...nodosPrefijo, ...resultado.nodosNuevos],
    costo_usd: costoUsd,
  });
}
