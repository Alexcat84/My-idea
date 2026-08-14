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

// ── EL RESOLUTOR DE LA HISTORIA ──────────────────────────────────────────────
//
// LA PROMESA: "la historia resuelve". Cada fusión escribe `ids_alias` en el
// superviviente, y la deprecación conserva el nodo absorbido entero (título,
// resumen, aristas) justamente para que un recorrido viejo siga contando algo.
//
// LA PROMESA ESTABA A MEDIO CUMPLIR (auditoría del motor, ago 2026): el alias
// se escribía, se declaraba en el tipo, y NADIE lo leía. 77 de los 285 alias
// apuntan a ids que ya NO son nodos -- herencia de la era en que fusionar
// BORRABA en vez de deprecar. Una referencia histórica a uno de ellos caía en
// `?? nid` y el usuario veía el id crudo en su plan.
//
// Tres cosas aprendidas MIRANDO los datos, no suponiéndolas:
//   1. el superviviente de un alias es SIEMPRE el nodo que lo lista, y ninguno
//      está listado por dos nodos: la resolución es única, sin ambigüedad;
//   2. hay CADENAS: 9 alias apuntan a un superviviente que a su vez fue
//      absorbido después (`costo_de_calidad_5` -> `_6` -> el superviviente de
//      la ronda 2). Por eso se camina la cadena en vez de dar un salto;
//   3. hay 10 deprecados SIN sucesor: los que el auditor retiró de la selección
//      porque no existe equivalente universal (los programas de OSHA, NIOSH,
//      SBREFA, los programas estatales). Esos NO resuelven a otro nodo, y no
//      deben: se representan a sí mismos, que conservan título y contenido.

let _alias: Record<string, string> | null = null;

/** alias -> el nodo que lo absorbió. Se construye una vez por proceso. */
/**
 * Lo MINIMO que el resolutor necesita mirar, por la misma razon que `esOfrecible`
 * declara `NodoOfrecible`: asi lo usan igual el motor (que tiene el grafo entero)
 * y el indice semantico (que solo carga unos campos), sin que ninguno tenga
 * excusa para escribirse su propia resolucion. `Grafo` lo satisface entero.
 */
export type NodoResoluble = { deprecado?: boolean; ids_alias?: string[] };
export type GrafoResoluble = Record<string, NodoResoluble>;

function mapaDeAlias(graph: GrafoResoluble): Record<string, string> {
  // El cache es por PROCESO y por el grafo de produccion, que es el unico que
  // el motor carga. Un grafo distinto (un test con fixture sintetico) no puede
  // leer el mapa del real: se le construye el suyo y no se cachea.
  if (graph !== _grafo) {
    const m: Record<string, string> = {};
    for (const [nid, n] of Object.entries(graph)) {
      for (const a of n.ids_alias ?? []) if (a !== nid) m[a] = nid;
    }
    return m;
  }
  if (_alias) return _alias;
  const m: Record<string, string> = {};
  for (const [nid, n] of Object.entries(graph)) {
    for (const a of n.ids_alias ?? []) {
      if (a !== nid) m[a] = nid; // el auto-alias (7 nodos) no dice nada
    }
  }
  _alias = m;
  return m;
}

/**
 * Un id CUALQUIERA -- de hoy, de una fusión, o de la era en que se borraba --
 * al nodo que hoy lo representa. `null` solo si el id no significa nada en
 * ninguna era, que es el único caso que merece salir a la superficie como tal.
 *
 * Orden: el nodo activo si existe; si no, se camina la cadena de alias hasta
 * uno activo; si la cadena entera fue retirada de la selección, el eslabón más
 * RECIENTE que exista (tiene título, y es la versión más nueva de esa historia).
 */
export function resolverId(nid: string, graph: GrafoResoluble): string | null {
  const n = graph[nid];
  if (n && !n.deprecado) return nid;
  const alias = mapaDeAlias(graph);
  const visto = new Set<string>([nid]);
  let cur = nid;
  // El último nodo REAL que se pisó al caminar. Si la cadena entera fue
  // retirada de la selección, ése es el representante honesto. Pasa en
  // `involucramiento_sindical`, cuyo sucesor es el que el auditor retiró:
  // devolver el punto de partida sería contar una versión más vieja.
  let ultimoReal: string | null = n ? nid : null;
  while (alias[cur] !== undefined) {
    cur = alias[cur];
    if (visto.has(cur)) break; // un ciclo no existe hoy; si aparece, se corta
    visto.add(cur);
    const c = graph[cur];
    if (!c) continue; // eslabón de la era en que se borraba: se sigue caminando
    ultimoReal = cur;
    if (!c.deprecado) return cur;
  }
  return ultimoReal;
}

/** Fase 3.9: lo que se muestra en las SUPERFICIES DE NAVEGACIÓN (riel del
 * árbol, cintillo de la tarjeta) es la etiqueta_arbol -- 4-5 palabras en
 * segunda persona, generada para enamorar. El titulo_concepto (el nombre del
 * libro) solo respalda en el DETALLE del nodo. "La etiqueta enamora, el título
 * respalda".
 *
 * Pasa por el resolutor: una referencia histórica muestra el título de quien la
 * representa hoy. El id crudo ya no lo alcanza ninguna referencia real -- solo
 * un id que jamás existió. */
export function etiquetaArbol(nid: string, graph: Grafo): string {
  const real = resolverId(nid, graph) ?? nid;
  return graph[real]?.etiqueta_arbol ?? graph[real]?.titulo_concepto ?? real;
}

/** El TÍTULO de un nodo por su id, de cualquier era. Mismo resolutor que
 * etiquetaArbol, pero sin la etiqueta: para los sitios donde lo que se cita es
 * el nombre del concepto (el material del juez, el perfil de sesión). */
export function tituloDeNodo(nid: string, graph: Grafo): string {
  const real = resolverId(nid, graph) ?? nid;
  return graph[real]?.titulo_concepto ?? real;
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
