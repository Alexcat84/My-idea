/**
 * interprete.ts - Fase 3.0: port de interpretar_multi_salto (Capa 2) y sus
 * funciones de reparacion de camino / respaldo tier-2 en
 * prototipo_motor.py. Decide un camino de 1-3 nodos (silenciosos + a lo
 * sumo uno conversado al final, o un unico salto semantico) y, si se
 * detiene a preguntar, la pregunta_adaptada para ese nodo.
 *
 * Contrato de fallos, identico al Python: 1) primer intento invalido ->
 * reintento aislado (nunca toca historialMensajes) con el error y los ids
 * validos literales; 2) si el reintento tambien falla -> auto-seleccion
 * SILENCIOSA por afinidad de palabras clave (registra el evento via
 * registrarEvento, si se provee), sin ninguna llamada mas a la API; 3)
 * solo un fallo de RED/presupuesto en la llamada principal devuelve
 * resultado=null (el llamador debe tratarlo como "sin IA disponible ahora
 * mismo", equivalente al menu de emergencia del CLI).
 */
import type Anthropic from "@anthropic-ai/sdk";
import { MAX_SALTOS_POSIBLES_OFRECIDOS, MIN_SCORE_SALTO, buscarAfines } from "../compass";
import {
  llamarClaude,
  llamarClaudeConversacion,
  MODEL_HAIKU,
  type MensajeConversacion,
  type UsoAcumulado,
} from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_INTERPRETE_MULTI } from "../prompts";
import { CAMPOS_NUMERICOS_PROYECTO, MAX_SALTOS_SILENCIOSOS_POR_LLAMADA, TIPOS_OFERTA_VALIDOS, type CampoNumericoProyecto } from "./constants";
import {
  MAX_SUCESORES_NIVEL2,
  obtenerPregunta,
  resumenNodo,
  sucesoresNivel,
  type Grafo,
  type PreguntasCache,
  type ResumenNodo,
} from "./graph";
import { tokensCosecha } from "./tokens";

export interface PrioridadDeclarada {
  texto: string;
  conteo: number;
}

export interface NumeroDetectadoEntry {
  valor: number | string;
  unidad: string | null;
  texto_original: string | null;
}

export type NumerosDetectados = Partial<Record<CampoNumericoProyecto, NumeroDetectadoEntry>>;

export type AccionInterprete = "avanzar" | "repreguntar" | "generar_plan" | "salir";

export interface ResultadoInterprete {
  accion: AccionInterprete;
  camino: string[];
  esSalto: boolean;
  preguntaNecesaria: boolean;
  preguntaAdaptada: string | null;
  repregunta: string | null;
  perfilUpdate: string | null;
  prioridadDeclarada: PrioridadDeclarada | null;
  numerosDetectados: NumerosDetectados | null;
  tipoOfertaDetectado: string | null;
  unidadVentaDetectada: string | null;
  razonamiento: string | null;
}

export interface EventoFallback {
  tipo: "fallback_auto";
  nodo_actual: string;
  candidato_elegido: string;
  motivo: string;
}

/** Fase 3.1 (caja de vidrio): lo que el interprete ya calculo para
 * decidir (candidatos locales, saltos_posibles con sus scores) mas la
 * decision final y su razonamiento corto -- mismo canal lateral que
 * EventoFallback, sin tocar el contrato de retorno de
 * interpretarMultiSalto. */
export interface EventoDecisionTurno {
  tipo: "decision_turno";
  nodo_actual: string;
  respuesta_usuario: string | null | undefined;
  candidatos_locales: string[];
  saltos_posibles: Array<{
    id: string;
    titulo: string;
    fase_proyecto: string | null | undefined;
    condiciones_activacion: string[];
    afinidad: number;
  }>;
  decision: { accion: AccionInterprete; camino: string[]; es_salto: boolean };
  razonamiento: string | null;
  /** Fase 3.9 (E16): la prioridad que el usuario declaro EN ESTE turno (null si
   * no declaro ninguna). Antes solo se aplicaba al estado, nunca se registraba;
   * ahora la bitacora dice en que turnos disparo la regla de prioridad. */
  prioridad_declarada: PrioridadDeclarada | null;
}

/**
 * Fase 4.3 (el mundo nunca abandona): el intérprete dijo 'salir' en una sesión
 * de mundo y la brújula re-eligió puerta en vez de cerrar. Queda en la bitácora
 * de la sesión con el motivo LITERAL del intérprete: es la señal de que
 * evaluacionBrecha eligió una semilla que el perfil no admitía (V2), y el
 * digest de `pnpm salud` la cuenta para que el hueco tenga cara.
 */
export interface EventoPuertaReelegida {
  tipo: "puerta_reelegida";
  dominio: string;
  puerta_descartada: string;
  puerta_nueva: string;
  /** el razonamiento del intérprete al querer salir: por qué no encajaba */
  motivo: string | null;
  es_semilla: boolean;
  candidatas_restantes: number;
}

/** Fase 4.3: no quedaba NINGUNA puerta del dominio compatible con el perfil.
 * El cierre honesto, con su reembolso: el único final legítimo de un mundo que
 * no era para este usuario. */
export interface EventoMundoIncompatible {
  tipo: "mundo_incompatible";
  dominio: string;
  puertas_descartadas: string[];
  motivo: string | null;
}

export type EventoInterprete =
  | EventoFallback
  | EventoDecisionTurno
  | EventoPuertaReelegida
  | EventoMundoIncompatible;

/** Reparo 1 (cadena estricta): ver docstring de _reparar_camino_cadena. */
function repararCaminoCadena(actualId: string, camino: string[], graph: Grafo, visitados: Set<string>): string[] {
  const reparado: string[] = [];
  let prev = actualId;
  const vistos = new Set<string>();
  for (const nid of camino) {
    const siguientesPrev = graph[prev]?.nodos_siguientes ?? [];
    if (siguientesPrev.includes(nid)) {
      reparado.push(nid);
      vistos.add(nid);
      prev = nid;
      continue;
    }
    const padre = siguientesPrev.find(
      (c) => !visitados.has(c) && !vistos.has(c) && (graph[c]?.nodos_siguientes ?? []).includes(nid)
    );
    if (!padre) {
      throw new Error(`${nid} no es sucesor de ${prev} ni de ninguno de sus sucesores directos`);
    }
    reparado.push(padre);
    vistos.add(padre);
    reparado.push(nid);
    vistos.add(nid);
    prev = nid;
  }
  return reparado;
}

/** Reparo 2 (reconstruccion desde el objetivo): ver docstring de
 * _reparar_camino_desde_objetivo. */
function repararCaminoDesdeObjetivo(camino: string[], nivel1Pool: ResumenNodo[], visitados: Set<string>): string[] {
  if (camino.length === 0) throw new Error("camino vacio");
  const objetivo = camino[camino.length - 1];
  if (visitados.has(objetivo)) throw new Error(`objetivo ${objetivo} ya fue visitado`);
  const nivel1Ids = new Set(nivel1Pool.map((n) => n.id));
  if (nivel1Ids.has(objetivo)) return [objetivo];
  for (const n of nivel1Pool) {
    const hijos = new Set((n.sucesores ?? []).map((h) => h.id));
    if (hijos.has(objetivo) && !visitados.has(n.id)) return [n.id, objetivo];
  }
  throw new Error(`${objetivo} no es sucesor de nivel 1 ni de nivel 2 conocido`);
}

function validarCamino(
  actualId: string,
  camino: string[],
  graph: Grafo,
  visitados: Set<string>,
  nivel1Pool?: ResumenNodo[]
): string[] {
  if (camino.length === 0) throw new Error("camino vacio");
  let caminoReparado: string[];
  try {
    caminoReparado = repararCaminoCadena(actualId, camino, graph, visitados);
    if (caminoReparado.length > MAX_SALTOS_SILENCIOSOS_POR_LLAMADA) {
      throw new Error(`camino excede ${MAX_SALTOS_SILENCIOSOS_POR_LLAMADA} nodos tras reparacion en cadena`);
    }
  } catch (e) {
    if (!nivel1Pool) throw e;
    caminoReparado = repararCaminoDesdeObjetivo(camino, nivel1Pool, visitados);
  }

  let prev = actualId;
  const vistosEnCamino = new Set<string>();
  for (const nid of caminoReparado) {
    if (!(nid in graph) || visitados.has(nid) || vistosEnCamino.has(nid)) {
      throw new Error(`nodo invalido o repetido en camino: ${nid}`);
    }
    if (!(graph[prev]?.nodos_siguientes ?? []).includes(nid)) {
      throw new Error(`${nid} no es sucesor de ${prev}`);
    }
    vistosEnCamino.add(nid);
    prev = nid;
  }
  return caminoReparado;
}

/** Ultimo recurso silencioso: elige el candidato de mayor afinidad de
 * palabras clave con la ultima respuesta del usuario (y el perfil de
 * sesion), en vez de un menu numerado. */
function elegirPorAfinidad(
  candidatosIds: string[],
  graph: Grafo,
  respuestaUsuario: string | null,
  perfilSesion: string | null
): string | null {
  if (candidatosIds.length === 0) return null;
  const contexto = tokensCosecha(`${respuestaUsuario ?? ""} ${perfilSesion ?? ""}`);
  if (contexto.size === 0) return candidatosIds[0];
  const puntaje = (nid: string): number => {
    const n = graph[nid];
    const textoNodo = `${n.titulo_concepto ?? ""} ${(n.condiciones_activacion ?? []).join(" ")}`;
    let interseccion = 0;
    for (const t of tokensCosecha(textoNodo)) if (contexto.has(t)) interseccion++;
    return interseccion;
  };
  let mejor = candidatosIds[0];
  let mejorPuntaje = puntaje(mejor);
  for (const nid of candidatosIds.slice(1)) {
    const p = puntaje(nid);
    if (p > mejorPuntaje) {
      mejor = nid;
      mejorPuntaje = p;
    }
  }
  return mejor;
}

export interface InterpretarMultiSaltoParams {
  client: Anthropic;
  actualId: string;
  graph: Grafo;
  visitados: Set<string>;
  perfilSesion: string | null;
  textoOriginal: string;
  preguntaHecha: string | null;
  respuestaUsuario: string | null;
  repreguntasDisponibles: boolean;
  preguntasCache: PreguntasCache;
  ultimasPreguntas?: string[];
  prioridadDeclaradaActual?: PrioridadDeclarada | null;
  /** null = llamada aislada (llamarClaude clasico), como las pruebas
   * unitarias de Python; un array (incluso vacio) = conversacion cacheada
   * turno a turno (llamarClaudeConversacion), como el CLI en produccion. */
  historialMensajes: MensajeConversacion[] | null;
  acumulado: UsoAcumulado;
  registrarEvento?: (evento: EventoInterprete) => void;
  /** Fase 3.5: dominios recorribles del proyecto (core + unlocks);
   * undefined = solo core, el comportamiento de siempre. */
  dominiosDesbloqueados?: string[];
}

export interface ResultadoInterpretarMultiSalto {
  /** null = fallo de red/presupuesto en la llamada principal. */
  resultado: ResultadoInterprete | null;
  acumulado: UsoAcumulado;
  historialMensajes: MensajeConversacion[] | null;
}

export async function interpretarMultiSalto(
  params: InterpretarMultiSaltoParams
): Promise<ResultadoInterpretarMultiSalto> {
  const {
    client,
    actualId,
    graph,
    visitados,
    perfilSesion,
    textoOriginal,
    preguntaHecha,
    respuestaUsuario,
    repreguntasDisponibles,
    preguntasCache,
    ultimasPreguntas = [],
    prioridadDeclaradaActual = null,
    historialMensajes,
    registrarEvento,
    dominiosDesbloqueados,
  } = params;
  let acumulado = params.acumulado;

  const nivel1Ids = sucesoresNivel(actualId, graph, visitados, undefined, dominiosDesbloqueados);
  const visitadosONivel1 = new Set([...visitados, ...nivel1Ids]);
  const nivel1: ResumenNodo[] = nivel1Ids.map((nid) => {
    const nivel2Ids = sucesoresNivel(nid, graph, visitadosONivel1, MAX_SUCESORES_NIVEL2, dominiosDesbloqueados);
    const entradaNivel1 = resumenNodo(nid, graph, preguntasCache);
    entradaNivel1.sucesores = nivel2Ids.map((n2) => resumenNodo(n2, graph, preguntasCache));
    return entradaNivel1;
  });

  const textoParaBrujula = respuestaUsuario || textoOriginal;
  const excluidosBrujula = new Set([...visitados, ...nivel1Ids]);
  const saltoCandidatos = await buscarAfines(textoParaBrujula, excluidosBrujula, {
    k: MAX_SALTOS_POSIBLES_OFRECIDOS,
    minScore: MIN_SCORE_SALTO,
    graph,
    dominiosDesbloqueados,
  });
  const idsSaltoOfrecidos = new Set(saltoCandidatos.map((c) => c.id));
  const saltosPosibles = saltoCandidatos.map(({ id, score }) => ({
    id,
    titulo: graph[id].titulo_concepto,
    fase_proyecto: graph[id].fase_proyecto,
    condiciones_activacion: (graph[id].condiciones_activacion ?? []).slice(0, 2),
    afinidad: Math.round(score * 1000) / 1000,
  }));

  const ctxCompleto: Record<string, unknown> = {
    entrada_original: textoOriginal,
    perfil_sesion: perfilSesion,
    nodo_actual: resumenNodo(actualId, graph, preguntasCache),
    sucesores_nivel1_y_nivel2: nivel1,
    saltos_posibles: saltosPosibles,
    pregunta_hecha: preguntaHecha,
    respuesta_usuario: respuestaUsuario,
    repreguntas_disponibles: repreguntasDisponibles,
    ultimas_preguntas_hechas: ultimasPreguntas.slice(-3),
    prioridad_declarada_actual: prioridadDeclaradaActual,
  };
  const usaHistorial = historialMensajes !== null && historialMensajes.length > 0;
  const ctxTurno = usaHistorial
    ? Object.fromEntries(Object.entries(ctxCompleto).filter(([k]) => k !== "entrada_original" && k !== "perfil_sesion"))
    : ctxCompleto;

  function validarRespuesta(raw: string): ResultadoInterprete {
    const data = parsearJson<Record<string, unknown>>(raw);
    const accion = data.accion as string;
    if (!["avanzar", "repreguntar", "generar_plan", "salir"].includes(accion)) {
      throw new Error(`accion invalida: ${accion}`);
    }
    if (accion === "repreguntar" && !repreguntasDisponibles) {
      throw new Error("el modelo repregunto sin repreguntas disponibles");
    }

    let esSalto = false;
    let camino: string[] = [];
    let preguntaNecesaria = false;
    let preguntaAdaptada: string | null = null;
    if (accion === "avanzar") {
      const salto = data.salto_semantico as string | undefined;
      if (salto) {
        if (!idsSaltoOfrecidos.has(salto)) {
          throw new Error(`salto_semantico '${salto}' no esta entre los saltos_posibles ofrecidos`);
        }
        if (visitados.has(salto)) {
          throw new Error(`salto_semantico '${salto}' ya fue visitado`);
        }
        camino = [salto];
        esSalto = true;
      } else {
        const caminoBruto = (data.camino as string[] | undefined) ?? [];
        camino = validarCamino(actualId, caminoBruto, graph, visitados, nivel1);
      }
      preguntaNecesaria = data.pregunta_necesaria === undefined ? true : Boolean(data.pregunta_necesaria);
      if (preguntaNecesaria) {
        const adaptada = String(data.pregunta_adaptada ?? "").trim();
        if (!adaptada) throw new Error("pregunta_necesaria=true pero falta pregunta_adaptada");
        preguntaAdaptada = adaptada;
      } else {
        preguntaAdaptada = null;
      }
    }

    let prioridadDeclarada: PrioridadDeclarada | null = null;
    const pd = data.prioridad_declarada;
    if (pd && typeof pd === "object" && "texto" in pd && "conteo" in pd) {
      const pdObj = pd as Record<string, unknown>;
      prioridadDeclarada = { texto: String(pdObj.texto), conteo: Number(pdObj.conteo) };
    }

    let numerosDetectados: NumerosDetectados | null = null;
    const nd = data.numeros_detectados;
    if (nd && typeof nd === "object") {
      const limpio: NumerosDetectados = {};
      for (const [campo, entry] of Object.entries(nd as Record<string, unknown>)) {
        if (!CAMPOS_NUMERICOS_PROYECTO.has(campo) || !entry || typeof entry !== "object") continue;
        const e = entry as Record<string, unknown>;
        if (e.valor === undefined || e.valor === null) continue;
        limpio[campo as CampoNumericoProyecto] = {
          valor: e.valor as number | string,
          unidad: (e.unidad as string | null | undefined) ?? null,
          texto_original: (e.texto_original as string | null | undefined) ?? null,
        };
      }
      numerosDetectados = Object.keys(limpio).length > 0 ? limpio : null;
    }

    const tipoOfertaRaw = data.tipo_oferta_detectado;
    const tipoOfertaDetectado =
      typeof tipoOfertaRaw === "string" && TIPOS_OFERTA_VALIDOS.has(tipoOfertaRaw) ? tipoOfertaRaw : null;
    const unidadVentaRaw = data.unidad_venta_detectada;
    const unidadVentaDetectada = unidadVentaRaw ? String(unidadVentaRaw).trim() : null;
    const razonamientoRaw = data.razonamiento;
    const razonamiento = razonamientoRaw ? String(razonamientoRaw).trim() : null;

    return {
      accion: accion as AccionInterprete,
      camino,
      esSalto,
      preguntaNecesaria,
      preguntaAdaptada,
      repregunta: (data.repregunta as string | null | undefined) ?? null,
      perfilUpdate: (data.perfil_update as string | null | undefined) ?? null,
      prioridadDeclarada,
      numerosDetectados,
      tipoOfertaDetectado,
      unidadVentaDetectada,
      razonamiento,
    };
  }

  function emitirDecisionTurno(resultado: ResultadoInterprete | null, razonamientoFallback?: string) {
    if (!registrarEvento || !resultado) return;
    registrarEvento({
      tipo: "decision_turno",
      nodo_actual: actualId,
      respuesta_usuario: respuestaUsuario,
      candidatos_locales: nivel1.map((n) => n.id),
      saltos_posibles: saltosPosibles,
      decision: { accion: resultado.accion, camino: resultado.camino, es_salto: resultado.esSalto },
      razonamiento: resultado.razonamiento ?? razonamientoFallback ?? null,
      prioridad_declarada: resultado.prioridadDeclarada ?? null,
    });
  }

  let nuevoHistorial: MensajeConversacion[] | null = historialMensajes;
  let raw: string;
  try {
    if (historialMensajes !== null) {
      const r = await llamarClaudeConversacion(
        client,
        SYSTEM_INTERPRETE_MULTI,
        historialMensajes,
        JSON.stringify(ctxTurno),
        MODEL_HAIKU,
        acumulado,
        { maxTokens: 700, componente: "turnos" }
      );
      raw = r.texto;
      acumulado = r.acumulado;
      nuevoHistorial = r.historialMensajes;
    } else {
      const r = await llamarClaude(client, SYSTEM_INTERPRETE_MULTI, JSON.stringify(ctxTurno), MODEL_HAIKU, acumulado, {
        maxTokens: 700,
        componente: "turnos",
      });
      raw = r.texto;
      acumulado = r.acumulado;
    }
  } catch {
    // Fallo de red/presupuesto: unico caso que debe llegar al modo de
    // emergencia (resultado=null), no al reintento ni al respaldo tier-2.
    return { resultado: null, acumulado, historialMensajes: nuevoHistorial };
  }

  let mensajeErrorPrevio: string;
  try {
    const resultado = validarRespuesta(raw);
    emitirDecisionTurno(resultado);
    return { resultado, acumulado, historialMensajes: nuevoHistorial };
  } catch (errorValidacion) {
    mensajeErrorPrevio = errorValidacion instanceof Error ? errorValidacion.message : String(errorValidacion);
  }

  // El reintento y el respaldo tier-2 SIEMPRE usan el contexto completo y
  // aislado (llamarClaude clasico): no tocan historialMensajes, para no
  // comprometer la conversacion cacheada con un intento invalido.
  const idsValidos = [...nivel1.map((n) => n.id), ...nivel1.flatMap((n) => (n.sucesores ?? []).map((h) => h.id))];
  const ctxRetry = { ...ctxCompleto, error_previo: mensajeErrorPrevio, ids_validos: idsValidos };

  try {
    const r2 = await llamarClaude(client, SYSTEM_INTERPRETE_MULTI, JSON.stringify(ctxRetry), MODEL_HAIKU, acumulado, {
      maxTokens: 700,
      componente: "turnos",
    });
    acumulado = r2.acumulado;
    const resultado = validarRespuesta(r2.texto);
    emitirDecisionTurno(resultado);
    return { resultado, acumulado, historialMensajes: nuevoHistorial };
  } catch (segundoError) {
    const candidato = elegirPorAfinidad(nivel1Ids, graph, respuestaUsuario, perfilSesion);
    if (!candidato) {
      return { resultado: null, acumulado, historialMensajes: nuevoHistorial };
    }
    if (registrarEvento) {
      registrarEvento({
        tipo: "fallback_auto",
        nodo_actual: actualId,
        candidato_elegido: candidato,
        motivo: segundoError instanceof Error ? segundoError.message : String(segundoError),
      });
    }
    const preguntaFallback = obtenerPregunta(candidato, graph[candidato], preguntasCache);
    const resultado: ResultadoInterprete = {
      accion: "avanzar",
      camino: [candidato],
      esSalto: false,
      preguntaNecesaria: true,
      preguntaAdaptada: preguntaFallback,
      repregunta: null,
      perfilUpdate: null,
      prioridadDeclarada: prioridadDeclaradaActual,
      numerosDetectados: null,
      tipoOfertaDetectado: null,
      unidadVentaDetectada: null,
      razonamiento: null,
    };
    emitirDecisionTurno(resultado, "fallback automatico tras 2 respuestas invalidas del modelo");
    return { resultado, acumulado, historialMensajes: nuevoHistorial };
  }
}
