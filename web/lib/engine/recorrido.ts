/**
 * recorrido.ts - Fase 3.0: version RESUMIBLE de ejecutar_recorrido en
 * prototipo_motor.py. El CLI corre un while(true) que bloquea en
 * leer_entrada() cada vez que necesita una respuesta; una funcion
 * serverless no puede bloquear entre requests, asi que avanzarTurno()
 * hace exactamente el mismo trabajo por PASOS: avanza en silencio todo lo
 * que el interprete decida (multi-hop, Fase 2.3) y se detiene en el
 * primer punto donde de verdad hace falta una respuesta nueva del
 * usuario, devolviendo el estado completo para que la ruta lo persista
 * en Supabase (sessions.estado_recorrido) y lo pase de vuelta en el
 * siguiente turno.
 *
 * Cubre las mismas 4 salidas que el bucle de Python: "avanzar" (silencioso
 * o conversado), "repreguntar", "generar_plan" (con la oferta de
 * profundizar de Fase 2.8/2.9 y su extension dirigida por la brujula), y
 * "salir". El ensamblado del plan en si (ensamblar_plan) vive en la ruta
 * /api/session/[id]/plan, no aqui -- el boton "Generar mi plan" de la UI
 * es permanente y no depende de que el interprete decida "generar_plan"
 * (ver decision de arquitectura de la Fase 3.0).
 */
import type Anthropic from "@anthropic-ai/sdk";
import { buscarAfines } from "../compass";
import { llamarClaude, MODEL_HAIKU, type MensajeConversacion, type UsoAcumulado } from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_PREGUNTA_DIRIGIDA, SYSTEM_PROFUNDIZAR } from "../prompts";
import { evaluarRuta, type EvaluacionCobertura, type Familia } from "../readiness";
import { FAMILIA_QUERY_BRUJULA, MAX_DEPTH, MAX_REPREGUNTAS_POR_PUNTO, MAX_TURNOS_EXTRA_SIGAMOS_DIRIGIDO } from "./constants";
import { dominioPermitido, obtenerPregunta, sucesoresNivel, type Grafo, type PreguntasCache } from "./graph";
import {
  interpretarMultiSalto,
  type EventoFallback,
  type NumeroDetectadoEntry,
  type PrioridadDeclarada,
} from "./interprete";

export type ModoNodo = "conversado" | "silencioso" | "salto";

export interface NumeroDetectadoSesion extends NumeroDetectadoEntry {
  session_id: string;
  updated_at: string;
}

export type FaseRecorrido =
  | "esperando_respuesta"
  | "esperando_profundizar"
  | "extendiendo_dirigido"
  | "listo_para_plan"
  | "cerrada";

export interface SigamosDirigidoState {
  elegidos: string[];
  indice: number;
}

export interface EstadoRecorrido {
  ruta: string[];
  modos: ModoNodo[];
  perfilSesion: string;
  textoOriginal: string;
  profundizarOfrecido: boolean;
  esSeguimiento: boolean;
  estadoVivoPrevio: string | null;
  fallbackEvents: EventoFallback[];
  prioridadDeclarada: PrioridadDeclarada | null;
  preguntaPendiente: string | null;
  ultimasPreguntas: string[];
  repreguntasUsadas: number;
  historialMensajes: MensajeConversacion[];
  numerosDetectadosSesion: Record<string, NumeroDetectadoSesion>;
  tipoOfertaSesion: string | null;
  unidadVentaSesion: string | null;
  fase: FaseRecorrido;
  sigamosDirigido: SigamosDirigidoState | null;
}

export function estadoInicial(params: {
  actualId: string;
  perfilSesion: string;
  textoOriginal: string;
  esSeguimiento?: boolean;
  estadoVivoPrevio?: string | null;
}): EstadoRecorrido {
  return {
    ruta: [params.actualId],
    modos: ["conversado"],
    perfilSesion: params.perfilSesion,
    textoOriginal: params.textoOriginal,
    profundizarOfrecido: false,
    esSeguimiento: params.esSeguimiento ?? false,
    estadoVivoPrevio: params.estadoVivoPrevio ?? null,
    fallbackEvents: [],
    prioridadDeclarada: null,
    preguntaPendiente: null,
    ultimasPreguntas: [],
    repreguntasUsadas: 0,
    historialMensajes: [],
    numerosDetectadosSesion: {},
    tipoOfertaSesion: null,
    unidadVentaSesion: null,
    fase: "esperando_respuesta",
    sigamosDirigido: null,
  };
}

interface NodoTranscrito {
  id: string;
  titulo: string;
  modo: ModoNodo;
}

export type ResultadoTurno =
  | { tipo: "pregunta"; estado: EstadoRecorrido; pregunta: string; acumulado: UsoAcumulado; nodosNuevos: NodoTranscrito[] }
  | {
      tipo: "listo_para_plan";
      estado: EstadoRecorrido;
      acumulado: UsoAcumulado;
      evaluacion: EvaluacionCobertura;
      nodosNuevos: NodoTranscrito[];
    }
  | { tipo: "salio"; estado: EstadoRecorrido; acumulado: UsoAcumulado }
  | {
      tipo: "error_temporal";
      estado: EstadoRecorrido;
      acumulado: UsoAcumulado;
      opciones: Array<{ id: string; titulo: string }>;
    };

/** Port de _detectar_decision_plan: clasifica una respuesta libre como
 * 'generar_ya' o 'continuar'. Reutilizado por la oferta de profundizar y
 * por la extension dirigida (Fase 2.9: la salida del usuario se respeta
 * turno a turno tambien DENTRO de la extension). */
export async function detectarDecisionPlan(
  client: Anthropic,
  respuesta: string,
  acumulado: UsoAcumulado
): Promise<{ decision: "generar_ya" | "continuar"; acumulado: UsoAcumulado }> {
  let acumuladoActualizado = acumulado;
  try {
    const r = await llamarClaude(client, SYSTEM_PROFUNDIZAR, respuesta, MODEL_HAIKU, acumulado, {
      maxTokens: 100,
      componente: "turnos",
    });
    acumuladoActualizado = r.acumulado;
    const data = parsearJson<{ decision?: string }>(r.texto);
    if (data.decision === "generar_ya" || data.decision === "continuar") {
      return { decision: data.decision, acumulado: acumuladoActualizado };
    }
  } catch {
    // fallo la interpretacion: cae al detector simple de palabras clave
  }
  const low = respuesta.trim().toLowerCase();
  const positivas = ["ya", "ahora", "dame", "listo", "asi esta bien", "así está bien"];
  const decision = positivas.some((p) => low.includes(p)) ? "generar_ya" : "continuar";
  return { decision, acumulado: acumuladoActualizado };
}

/** Port de pregunta_dirigida: pregunta adaptada para un nodo elegido por
 * la brujula en la extension dirigida, sin pasar por el contrato completo
 * del interprete (el nodo ya se eligio por afinidad a la familia
 * faltante, no hay camino/salto que decidir). */
export async function preguntaDirigida(
  client: Anthropic,
  nid: string,
  graph: Grafo,
  preguntasCache: PreguntasCache,
  perfilSesion: string | null,
  ultimasPreguntas: string[],
  acumulado: UsoAcumulado
): Promise<{ pregunta: string; acumulado: UsoAcumulado }> {
  const plano = obtenerPregunta(nid, graph[nid], preguntasCache);
  try {
    const ctx = {
      perfil_sesion: perfilSesion,
      pregunta_cache: plano,
      ultimas_preguntas_hechas: ultimasPreguntas.slice(-3),
    };
    const r = await llamarClaude(client, SYSTEM_PREGUNTA_DIRIGIDA, JSON.stringify(ctx), MODEL_HAIKU, acumulado, {
      maxTokens: 150,
      componente: "turnos",
    });
    const texto = r.texto.trim();
    return { pregunta: texto || plano, acumulado: r.acumulado };
  } catch {
    return { pregunta: plano, acumulado };
  }
}

export interface AvanzarTurnoParams {
  client: Anthropic;
  graph: Grafo;
  families: Record<string, Familia>;
  preguntasCache: PreguntasCache;
  estado: EstadoRecorrido;
  /** La respuesta del usuario a estado.preguntaPendiente, o null en el
   * primerisimo turno (recien clasificada la puerta de entrada, aun no se
   * hizo ninguna pregunta de nodo). */
  respuestaUsuario: string | null;
  acumulado: UsoAcumulado;
  /** Metadata de codigo (no algo que el modelo deba inventar) para
   * timestampear numeros_detectados_sesion, igual que Python. */
  dbSessionId: string;
}

export async function avanzarTurno(params: AvanzarTurnoParams): Promise<ResultadoTurno> {
  const { client, graph, families, preguntasCache, dbSessionId } = params;
  let estado = params.estado;
  let acumulado = params.acumulado;
  let respuestaUsuario = params.respuestaUsuario;
  const rutaLongitudInicial = estado.ruta.length;

  function nodosNuevosDesdeInicio(): NodoTranscrito[] {
    return estado.ruta.slice(rutaLongitudInicial).map((nid, i) => ({
      id: nid,
      titulo: graph[nid]?.titulo_concepto ?? nid,
      modo: estado.modos[rutaLongitudInicial + i],
    }));
  }

  // --- Sub-fase: esperando "¿seguimos un poco o lo quieres ya?" ---
  if (estado.fase === "esperando_profundizar") {
    const { decision, acumulado: a1 } = await detectarDecisionPlan(client, respuestaUsuario ?? "", acumulado);
    acumulado = a1;
    if (decision === "generar_ya") {
      estado = { ...estado, fase: "listo_para_plan", preguntaPendiente: null };
      return { tipo: "listo_para_plan", estado, acumulado, evaluacion: evaluarRuta(estado.ruta, families), nodosNuevos: [] };
    }
    const evaluacion = evaluarRuta(estado.ruta, families);
    const familiasFaltantesKeys: string[] = [];
    if (!evaluacion.tiene_accion_clientes) familiasFaltantesKeys.push("accion_clientes");
    if (!evaluacion.tiene_viabilidad_economica) familiasFaltantesKeys.push("viabilidad_economica");

    const visitados = new Set(estado.ruta);
    const query = familiasFaltantesKeys.map((f) => FAMILIA_QUERY_BRUJULA[f] ?? f).join(" ");
    const afines = await buscarAfines(query, visitados, { k: 20, graph });
    let candidatosFamilia = afines.map((c) => c.id).filter((nid) => familiasFaltantesKeys.includes(families[nid] ?? "general"));
    if (candidatosFamilia.length === 0) {
      candidatosFamilia = Object.keys(graph).filter(
        (nid) => !visitados.has(nid) && familiasFaltantesKeys.includes(families[nid] ?? "general") && dominioPermitido(nid, graph)
      );
    }
    const elegidos = candidatosFamilia.slice(0, MAX_TURNOS_EXTRA_SIGAMOS_DIRIGIDO);
    if (elegidos.length === 0) {
      estado = { ...estado, fase: "listo_para_plan", preguntaPendiente: null };
      return { tipo: "listo_para_plan", estado, acumulado, evaluacion: evaluarRuta(estado.ruta, families), nodosNuevos: [] };
    }

    const primerNid = elegidos[0];
    const { pregunta, acumulado: a2 } = await preguntaDirigida(
      client,
      primerNid,
      graph,
      preguntasCache,
      estado.perfilSesion,
      estado.ultimasPreguntas,
      acumulado
    );
    acumulado = a2;
    estado = {
      ...estado,
      ruta: [...estado.ruta, primerNid],
      modos: [...estado.modos, "conversado"],
      fase: "extendiendo_dirigido",
      sigamosDirigido: { elegidos, indice: 0 },
      preguntaPendiente: pregunta,
      ultimasPreguntas: [...estado.ultimasPreguntas, pregunta].slice(-3),
    };
    return { tipo: "pregunta", estado, pregunta, acumulado, nodosNuevos: nodosNuevosDesdeInicio() };
  }

  // --- Sub-fase: dentro de la extension dirigida (Fase 2.8/2.9) ---
  if (estado.fase === "extendiendo_dirigido" && estado.sigamosDirigido) {
    const { decision, acumulado: a1 } = await detectarDecisionPlan(client, respuestaUsuario ?? "", acumulado);
    acumulado = a1;
    if (decision === "generar_ya") {
      estado = { ...estado, fase: "listo_para_plan", preguntaPendiente: null, sigamosDirigido: null };
      return { tipo: "listo_para_plan", estado, acumulado, evaluacion: evaluarRuta(estado.ruta, families), nodosNuevos: [] };
    }
    const { elegidos, indice } = estado.sigamosDirigido;
    const nidActual = elegidos[indice];
    const titulo = graph[nidActual]?.titulo_concepto ?? nidActual;
    const perfilNuevo = `${estado.perfilSesion}\nSobre ${titulo}: ${respuestaUsuario ?? ""}`.trim();
    const siguienteIndice = indice + 1;

    if (siguienteIndice >= elegidos.length) {
      estado = {
        ...estado,
        perfilSesion: perfilNuevo,
        fase: "listo_para_plan",
        preguntaPendiente: null,
        sigamosDirigido: null,
      };
      return { tipo: "listo_para_plan", estado, acumulado, evaluacion: evaluarRuta(estado.ruta, families), nodosNuevos: [] };
    }

    const siguienteNid = elegidos[siguienteIndice];
    const { pregunta, acumulado: a2 } = await preguntaDirigida(
      client,
      siguienteNid,
      graph,
      preguntasCache,
      perfilNuevo,
      estado.ultimasPreguntas,
      acumulado
    );
    acumulado = a2;
    estado = {
      ...estado,
      perfilSesion: perfilNuevo,
      ruta: [...estado.ruta, siguienteNid],
      modos: [...estado.modos, "conversado"],
      sigamosDirigido: { elegidos, indice: siguienteIndice },
      preguntaPendiente: pregunta,
      ultimasPreguntas: [...estado.ultimasPreguntas, pregunta].slice(-3),
    };
    return { tipo: "pregunta", estado, pregunta, acumulado, nodosNuevos: nodosNuevosDesdeInicio() };
  }

  // --- Fase normal: bucle de interpretar_multi_salto (silencioso + repreguntas) ---
  let preguntaHecha = estado.preguntaPendiente;
  const eventosNuevos: EventoFallback[] = [];

  while (true) {
    const actualId = estado.ruta[estado.ruta.length - 1];
    const visitados = new Set(estado.ruta);
    const nivel1Ids = sucesoresNivel(actualId, graph, visitados);
    if (nivel1Ids.length === 0 || estado.ruta.length >= MAX_DEPTH) {
      estado = { ...estado, fase: "listo_para_plan", preguntaPendiente: null };
      return {
        tipo: "listo_para_plan",
        estado,
        acumulado,
        evaluacion: evaluarRuta(estado.ruta, families),
        nodosNuevos: nodosNuevosDesdeInicio(),
      };
    }

    const resultadoInterprete = await interpretarMultiSalto({
      client,
      actualId,
      graph,
      visitados,
      perfilSesion: estado.perfilSesion,
      textoOriginal: estado.textoOriginal,
      preguntaHecha,
      respuestaUsuario,
      repreguntasDisponibles: estado.repreguntasUsadas < MAX_REPREGUNTAS_POR_PUNTO,
      preguntasCache,
      ultimasPreguntas: estado.ultimasPreguntas,
      prioridadDeclaradaActual: estado.prioridadDeclarada,
      historialMensajes: estado.historialMensajes,
      acumulado,
      registrarEvento: (e) => eventosNuevos.push(e),
    });
    acumulado = resultadoInterprete.acumulado;
    if (resultadoInterprete.historialMensajes) {
      estado = { ...estado, historialMensajes: resultadoInterprete.historialMensajes };
    }
    if (eventosNuevos.length > 0) {
      estado = { ...estado, fallbackEvents: [...estado.fallbackEvents, ...eventosNuevos] };
      eventosNuevos.length = 0;
    }

    const resultado = resultadoInterprete.resultado;
    if (!resultado) {
      return {
        tipo: "error_temporal",
        estado,
        acumulado,
        opciones: nivel1Ids.map((nid) => ({ id: nid, titulo: graph[nid].titulo_concepto })),
      };
    }

    if (resultado.perfilUpdate) {
      estado = {
        ...estado,
        perfilSesion: estado.perfilSesion ? `${estado.perfilSesion}\n${resultado.perfilUpdate}`.trim() : resultado.perfilUpdate,
      };
    }
    if (resultado.prioridadDeclarada) {
      estado = { ...estado, prioridadDeclarada: resultado.prioridadDeclarada };
    }
    if (resultado.numerosDetectados) {
      const nuevos = { ...estado.numerosDetectadosSesion };
      const ahora = new Date().toISOString();
      for (const [campo, entry] of Object.entries(resultado.numerosDetectados)) {
        if (!entry) continue;
        nuevos[campo] = { ...entry, session_id: dbSessionId, updated_at: ahora };
      }
      estado = { ...estado, numerosDetectadosSesion: nuevos };
    }
    if (resultado.tipoOfertaDetectado) estado = { ...estado, tipoOfertaSesion: resultado.tipoOfertaDetectado };
    if (resultado.unidadVentaDetectada) estado = { ...estado, unidadVentaSesion: resultado.unidadVentaDetectada };

    if (resultado.accion === "salir") {
      estado = { ...estado, fase: "cerrada", preguntaPendiente: null };
      return { tipo: "salio", estado, acumulado };
    }

    if (resultado.accion === "repreguntar") {
      const repregunta = resultado.repregunta ?? "";
      estado = {
        ...estado,
        repreguntasUsadas: estado.repreguntasUsadas + 1,
        preguntaPendiente: repregunta,
        ultimasPreguntas: [...estado.ultimasPreguntas, repregunta].slice(-3),
      };
      return { tipo: "pregunta", estado, pregunta: repregunta, acumulado, nodosNuevos: nodosNuevosDesdeInicio() };
    }

    if (resultado.accion === "generar_plan") {
      const evaluacion = evaluarRuta(estado.ruta, families);
      if (!evaluacion.es_completa && !estado.profundizarOfrecido) {
        const faltanTxt = evaluacion.familias_faltantes.join("; ");
        const mensaje =
          `Puedo darte tu plan ahora mismo. Eso si: con algunas preguntas mas ` +
          `incluiria ${faltanTxt}. ¿Seguimos un poco o lo quieres ya?`;
        estado = { ...estado, profundizarOfrecido: true, fase: "esperando_profundizar", preguntaPendiente: mensaje };
        return { tipo: "pregunta", estado, pregunta: mensaje, acumulado, nodosNuevos: nodosNuevosDesdeInicio() };
      }
      estado = { ...estado, fase: "listo_para_plan", preguntaPendiente: null };
      return { tipo: "listo_para_plan", estado, acumulado, evaluacion, nodosNuevos: nodosNuevosDesdeInicio() };
    }

    // accion === "avanzar": 1-3 nodos, algunos silenciosos + a lo sumo uno
    // conversado al final (o un unico salto semantico).
    const camino = resultado.camino;
    const preguntaNecesaria = resultado.preguntaNecesaria;
    const esSalto = resultado.esSalto;
    const nuevaRuta = [...estado.ruta];
    const nuevosModos = [...estado.modos];
    camino.forEach((nid, idx) => {
      const esUltimo = idx === camino.length - 1;
      const modo: ModoNodo = esSalto ? "salto" : esUltimo && preguntaNecesaria ? "conversado" : "silencioso";
      nuevaRuta.push(nid);
      nuevosModos.push(modo);
    });
    estado = { ...estado, ruta: nuevaRuta, modos: nuevosModos, repreguntasUsadas: 0 };
    const nuevoActualId = camino[camino.length - 1];

    if (preguntaNecesaria) {
      const pregunta = resultado.preguntaAdaptada || obtenerPregunta(nuevoActualId, graph[nuevoActualId], preguntasCache);
      estado = {
        ...estado,
        preguntaPendiente: pregunta,
        ultimasPreguntas: [...estado.ultimasPreguntas, pregunta].slice(-3),
      };
      return { tipo: "pregunta", estado, pregunta, acumulado, nodosNuevos: nodosNuevosDesdeInicio() };
    }

    // Silencioso: el turno sigue avanzando sin pedir nada nuevo todavia.
    preguntaHecha = null;
    respuestaUsuario = null;
  }
}
