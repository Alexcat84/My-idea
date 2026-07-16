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
import catalogo from "./assets/packs_catalog.json";
import { costoAcumuladoUsd, PRESUPUESTO_SESION_USD_DEFAULT, type UsoAcumulado } from "./costmeter";
import { cerrarSesion, guardarEstadoSesion, mergeNumerosProyecto, mergeTipoOferta, registrarBitacora } from "./db";
import type { NodoTranscrito, ResultadoTurno } from "./engine/recorrido";

/** Fase 4.3 §2: un cierre JAMAS deja pantalla muda. Todo 'salio' viaja con su
 * mensaje en palabras de persona; la UI lo pinta tal cual, sin inventar copy. */
const MENSAJE_CIERRE_CORE =
  "Con lo que me contaste no puedo seguir preguntando sin hacerte perder el tiempo. " +
  "Tu idea queda guardada tal como está: vuelve cuando quieras y seguimos desde aquí.";

/** El cierre honesto de un mundo que no era para este proyecto (§1). Las
 * palabras son del fundador, literales. */
function mensajeMundoIncompatible(dominio: string): string {
  const nombre =
    (catalogo.packs as Array<{ clave: string; nombre: string }>).find((p) => p.clave === dominio)?.nombre ??
    "Este mundo";
  return (
    `${nombre} está pensado para negocios con más estructura de la que tu proyecto necesita hoy; ` +
    "te lo digo antes de hacerte perder tiempo. Te devolvimos la activación: puedes volver a " +
    "entrar sin pagar de nuevo cuando tu proyecto crezca."
  );
}

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

    // Fase 4.3 §1: un mundo solo cierra cuando NINGUNA de sus puertas era
    // compatible con el perfil (el motor ya re-eligio todo lo que pudo).
    const cierre = resultado.cierreMundo;
    if (cierre) {
      // Se revierte el unlock: el usuario pago por explorar un mundo que no era
      // para su proyecto de hoy, y podra volver a entrar gratis cuando crezca.
      //
      // ── ANCLA para la ETAPA 2 del frente de cuentas (rama cuentas-y-creditos)
      // Aqui va reembolsar_creditos(projectId, 3, 'mundo_incompatible'): el
      // reembolso AUTOMATICO de los 3 creditos de la activacion. Hoy no hay
      // ledger, asi que revertir el unlock ES el reembolso -- devuelve la unica
      // cosa que el usuario compro. Cuando el ledger exista, las dos cosas van
      // juntas y en esta misma transaccion logica.
      await supabase.from("project_unlocks").delete().eq("project_id", projectId).eq("dominio", cierre.dominio);
      await registrarBitacora(supabase, projectId, "mundo_incompatible", {
        mundo: cierre.dominio,
        motivo: cierre.motivo,
        unlock_revertido: true,
      });
    }

    return NextResponse.json({
      project_id: projectId,
      session_id: sessionId,
      tipo: "salio",
      costo_usd: costoUsd,
      // §2: el cierre SIEMPRE viaja con su mensaje. La UI no inventa copy y,
      // sobre todo, no se queda muda.
      mensaje: cierre ? mensajeMundoIncompatible(cierre.dominio) : MENSAJE_CIERRE_CORE,
      dominio: cierre?.dominio ?? null,
      unlock_revertido: Boolean(cierre),
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
      // Phase 3.7.2 (la oferta honesta): presente cuando el motor OFRECE
      // (doble CTA); ausente en los cierres sin vuelta (CTA unico).
      temas_pendientes: resultado.temasPendientes,
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
