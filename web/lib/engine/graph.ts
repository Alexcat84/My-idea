/**
 * graph.ts - Fase 3.0: port de las funciones de acceso al grafo de
 * prototipo_motor.py (cargar_grafo, cargar_entry_seeds, sucesores_nivel,
 * resumen_nodo, obtener_pregunta, _dominio_permitido). Los assets ya
 * estan sincronizados como JSON estatico (scripts/sync_assets_web.py) --
 * esto solo expone las mismas funciones de acceso que el CLI, sin
 * recompilar nada.
 */
import masterGraphJson from "../assets/master_graph.json";
import preguntasCacheJson from "../assets/preguntas_cache.json";
import entrySeedsJson from "../assets/entry_seeds.json";

export const MAX_OPCIONES = 6;
export const MAX_SUCESORES_NIVEL2 = 4;
export const DOMINIOS_DESBLOQUEADOS_DEFECTO = ["core"];

export interface NodoGrafo {
  /** Hygiene v1.3.1: etiqueta corta del arbol (4-5 palabras, segunda persona). */
  etiqueta_arbol?: string;
  node_id: string;
  fase_proyecto: string;
  dominio?: string;
  titulo_concepto: string;
  fuente?: string;
  resumen_teorico: string;
  pasos_accionables?: string[];
  entregable_esperado?: string;
  nodos_previos?: string[];
  nodos_siguientes?: string[];
  condiciones_activacion?: string[];
  /** Fusión de duplicados: el nodo sigue EXISTIENDO (su historia resuelve) pero
   * ya no se ofrece. Ver esOfrecible: es la única puerta que lo mira. */
  deprecado?: boolean;
  /** Los ids que este nodo absorbió al fusionarse. */
  ids_alias?: string[];
}

export type Grafo = Record<string, NodoGrafo>;

export interface PreguntaCacheEntry {
  pregunta?: string;
  [key: string]: unknown;
}

export type PreguntasCache = Record<string, PreguntaCacheEntry>;

let _grafo: Grafo | null = null;
let _preguntasCache: PreguntasCache | null = null;
let _entrySeeds: string[] | null = null;

export function cargarGrafo(): Grafo {
  if (!_grafo) {
    _grafo = (masterGraphJson as { nodos: Grafo }).nodos;
  }
  return _grafo;
}

export function cargarPreguntasCache(): PreguntasCache {
  if (!_preguntasCache) {
    _preguntasCache = preguntasCacheJson as PreguntasCache;
  }
  return _preguntasCache;
}

/** Las semillas de entrada. Con el grafo, pasan por la PUERTA ÚNICA: una
 * semilla deprecada abriría el recorrido por un nodo que ya no se ofrece. */
export function cargarEntrySeeds(graph?: Grafo): string[] {
  if (!_entrySeeds) {
    _entrySeeds = (entrySeedsJson as { seeds: string[] }).seeds;
  }
  return graph ? _entrySeeds.filter((nid) => esOfrecible(nid, graph)) : _entrySeeds;
}

/** Fase 3.9: lo que se muestra en las SUPERFICIES DE NAVEGACIÓN (riel del
 * árbol, cintillo de la tarjeta) es la etiqueta_arbol -- 4-5 palabras en
 * segunda persona, generada para enamorar. El titulo_concepto (el nombre del
 * libro) solo respalda en el DETALLE del nodo. Fallback al título si falta la
 * etiqueta, y al id como último recurso. "La etiqueta enamora, el título
 * respalda". */
export function etiquetaArbol(nid: string, graph: Grafo): string {
  return graph[nid]?.etiqueta_arbol ?? graph[nid]?.titulo_concepto ?? nid;
}

/**
 * LA PUERTA ÚNICA DE OFERTA. Todo camino que le proponga un nodo al usuario
 * pasa por aquí: los sucesores del recorrido, las semillas de entrada y los
 * resultados del índice semántico.
 *
 * Es única a propósito, y es ley de la casa (adjudicada ago 2026). Antes había
 * dos filtros de dominio: éste y una copia a mano dentro de compass.ts. Un
 * criterio de elegibilidad repartido en varios sitios no falla de golpe: falla
 * en el camino que alguien olvidó actualizar, y el síntoma aparece semanas
 * después en el recorrido de una persona. Si mañana hace falta una condición
 * nueva para ofrecer un nodo, se escribe AQUÍ o no se escribe.
 *
 * Tres cosas mira, en este orden:
 *   1. que el nodo exista en el grafo,
 *   2. que NO esté deprecado (fusionado dentro de otro: sigue existiendo para
 *      que la historia resuelva, pero ya no se ofrece),
 *   3. que su dominio esté desbloqueado para este proyecto.
 */
export type NodoOfrecible = { dominio?: string; deprecado?: boolean };

export function esOfrecible(
  nid: string,
  // Lo MÍNIMO que la puerta necesita mirar. Así la usan igual el motor (que
  // tiene el grafo entero) y el índice semántico (que solo carga dominio), sin
  // que ninguno tenga excusa para escribirse su propio filtro.
  graph: Record<string, NodoOfrecible>,
  dominiosDesbloqueados?: string[] | null,
): boolean {
  const n = graph[nid];
  if (!n) return false;
  if (n.deprecado) return false;
  return (dominiosDesbloqueados ?? DOMINIOS_DESBLOQUEADOS_DEFECTO).includes(n.dominio ?? "core");
}

export function sucesoresNivel(
  nid: string,
  graph: Grafo,
  visitados: Set<string>,
  limite = MAX_OPCIONES,
  dominiosDesbloqueados?: string[] | null
): string[] {
  const siguientes = graph[nid]?.nodos_siguientes ?? [];
  return siguientes
    .filter((c) => !visitados.has(c) && esOfrecible(c, graph, dominiosDesbloqueados))
    .slice(0, limite);
}

/** Pregunta abierta pregenerada para este nodo, o una generica si no esta
 * en el cache. */
export function obtenerPregunta(nodeId: string, node: NodoGrafo, cache: PreguntasCache): string {
  const entry = cache[nodeId];
  if (entry?.pregunta) return entry.pregunta;
  return (
    `Pensando en "${node.titulo_concepto}", cuentame en tus palabras ` +
    "donde estas parado ahora mismo con tu idea y que es lo que mas " +
    "te preocupa o te entusiasma."
  );
}

export interface ResumenNodo {
  id: string;
  titulo: string;
  condiciones_activacion: string[];
  pregunta_cache?: string;
  sucesores?: ResumenNodo[];
}

export function resumenNodo(nid: string, graph: Grafo, preguntasCache?: PreguntasCache | null): ResumenNodo {
  const n = graph[nid];
  const out: ResumenNodo = {
    id: nid,
    titulo: n.titulo_concepto,
    condiciones_activacion: (n.condiciones_activacion ?? []).slice(0, 2),
  };
  if (preguntasCache) {
    out.pregunta_cache = obtenerPregunta(nid, n, preguntasCache);
  }
  return out;
}
