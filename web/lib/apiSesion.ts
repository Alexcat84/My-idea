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

/** FASE B (canon 12): el cierre honesto es una CONFESIÓN CON DIGNIDAD, no una
 * disculpa. Título y cuerpo son marco fijo (tono cuidado, con acentos, sin
 * guiones); el "porqué" NO se escribe aquí: es la caja de vidrio, el motivo
 * REAL que el intérprete registró (razonamiento / cierreMundo.motivo). La UI
 * pinta ambos; jamás inventa copy ni se queda muda (ley de la Fase 4.3 §2).
 *
 * Compat (amarre 1): además del `cierre` estructurado, la respuesta sigue
 * llevando `mensaje` plano (= el cuerpo), para que cualquier consumidor que
 * solo lea `mensaje` no se rompa. */
const CIERRE_CAMINO = {
  titulo: "Por aquí no encuentro un plan que valga tu tiempo.",
  cuerpo:
    "Exploré lo que me contaste y, siendo honesto, este ángulo no me da material suficiente para " +
    "armarte un plan que de verdad te mueva. Prefiero decírtelo a entregarte relleno. No es un no a " +
    "tu idea: es un no a este camino.",
};

/** El cierre honesto de un mundo que no era para este proyecto (§1).
 *
 * Fase 4.3.2 (regla de claims del BANCO): el texto NO afirma nada sobre dinero.
 * Dice el hecho real (el mundo queda reabierto y pueden volver a entrar) sin
 * "te devolvimos N créditos": esa es una afirmación de dinero, y solo la UI
 * puede mostrarla, y solo cuando `creditos_devueltos` trae un número respaldado
 * por el ledger. En beta la activación es gratis: no hubo consumo, no hay
 * reembolso que anunciar en el cuerpo. */
function cierreMundoTexto(dominio: string): { titulo: string; cuerpo: string } {
  const nombre =
    (catalogo.packs as Array<{ clave: string; nombre: string }>).find((p) => p.clave === dominio)?.nombre ??
    "Este mundo";
  return {
    titulo: `${nombre} no es para esta idea, todavía.`,
    cuerpo:
      "Activé y exploré este mundo con lo que hay hoy, y no encontré un subproyecto que te sume sin " +
      "inventarte trabajo. Antes que darte un checklist de relleno, prefiero parar aquí. Este mundo te " +
      "sigue esperando: puedes volver a entrar cuando tu proyecto crezca.",
  };
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
    // Fase 4.3.2: DOS cosas distintas, que la regla de claims obliga a separar.
    //  (1) `unlock_revertido` — HECHO real: se borra la fila y el usuario puede
    //      volver a entrar al mundo. No es una afirmación de dinero.
    //  (2) `creditos_devueltos` — AFIRMACIÓN DE DINERO: cuántos créditos se le
    //      devolvieron. Solo puede tener valor si un evento del ledger lo
    //      respalda. En beta la activación es gratis (no hubo consumo): null.
    // ── ANCLA para la ETAPA 2 (rama cuentas-y-creditos) ──────────────────
    // Hoy: null (no hay ledger, la activación de beta es gratis). El día de la
    // ETAPA 2, esta línea pasa a
    //   `const creditosDevueltos = cierre ? await reembolsarCreditos(projectId,
    //      cierre.dominio, "mundo_incompatible") : null;`
    // Esa función consulta el ledger, ve si HUBO un cargo real por la
    // activación, lo revierte con su propio evento y devuelve el monto (o null
    // si no hubo cargo — p.ej. cortesía de beta). El claim de dinero de la UI
    // cuelga de ESE valor, jamás de un flag de entorno: si el ledger no lo
    // respalda, no se afirma.
    const creditosDevueltos: number | null = null;
    if (cierre) {
      // Revertir el unlock: real hoy, sin ledger. El mundo vuelve a estar
      // disponible para reintentarlo cuando el proyecto crezca.
      await supabase.from("project_unlocks").delete().eq("project_id", projectId).eq("dominio", cierre.dominio);
      await registrarBitacora(supabase, projectId, "mundo_incompatible", {
        mundo: cierre.dominio,
        motivo: cierre.motivo,
        unlock_revertido: true,
        creditos_devueltos: creditosDevueltos,
      });
    }

    // Canon 12: el cierre estructurado. El "porque" es el motivo REAL del
    // interprete (glass box), no prosa generica; null si no lo hubo.
    const cierreTexto = cierre ? cierreMundoTexto(cierre.dominio) : CIERRE_CAMINO;
    const porque = cierre ? cierre.motivo : resultado.cierreCamino?.motivo ?? null;

    return NextResponse.json({
      project_id: projectId,
      session_id: sessionId,
      tipo: "salio",
      costo_usd: costoUsd,
      // §2 + canon 12: el cierre SIEMPRE viaja, ahora estructurado. La UI no
      // inventa copy y no se queda muda.
      cierre: {
        tipo: cierre ? "mundo" : "camino",
        titulo: cierreTexto.titulo,
        cuerpo: cierreTexto.cuerpo,
        porque,
        dominio: cierre?.dominio ?? null,
      },
      // Compat (amarre 1): el `mensaje` plano sigue viajando (= el cuerpo), para
      // que un consumidor viejo que solo lea `mensaje` no se rompa ni se quede mudo.
      mensaje: cierreTexto.cuerpo,
      dominio: cierre?.dominio ?? null,
      unlock_revertido: Boolean(cierre),
      // El claim de dinero: null en beta. La UI solo muestra la línea de
      // reembolso si esto trae un número.
      creditos_devueltos: creditosDevueltos,
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
