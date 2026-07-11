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

export function cargarEntrySeeds(): string[] {
  if (!_entrySeeds) {
    _entrySeeds = (entrySeedsJson as { seeds: string[] }).seeds;
  }
  return _entrySeeds;
}

/** Hotfix v2.1.1: groundwork de dominios. Hoy todo el dataset es "core" y
 * todo proyecto tiene ["core"] desbloqueado por defecto. */
export function dominioPermitido(nid: string, graph: Grafo, dominiosDesbloqueados?: string[] | null): boolean {
  return (dominiosDesbloqueados ?? DOMINIOS_DESBLOQUEADOS_DEFECTO).includes(graph[nid]?.dominio ?? "core");
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
    .filter((c) => c in graph && !visitados.has(c) && dominioPermitido(c, graph, dominiosDesbloqueados))
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
