/**
 * reeleccionPuerta.ts — Fase 4.3: EL MUNDO NUNCA ABANDONA.
 *
 * El hallazgo (barrido de 380, jul 2026): el intérprete salió de un mundo en el
 * turno 1 con este razonamiento, textual de la caja de vidrio:
 *
 *   "El nodo_actual 'Medición de la Calidad' y todos sus sucesores están
 *    diseñados para organizaciones con estructura, equipos, múltiples procesos
 *    y sistemas formales de calidad. La usuaria es…"
 *
 * El juicio era CORRECTO: ese nodo no es para quien arma tres kits en su casa.
 * Lo que estaba mal era la consecuencia — la sesión se cerraba y el usuario, que
 * había pagado 3 créditos por explorar ESE mundo, se quedaba mirando una
 * pantalla muda. La semilla la eligió `evaluacionBrecha`, que es ciega al perfil
 * (V2 de la auditoría de paridad); el intérprete la corrige un turno tarde.
 *
 * La regla nueva: en una sesión de mundo, 'salir' NO cierra — RE-ELIGE PUERTA.
 * La brújula evalúa las demás semillas del dominio (y sus vecinos) contra el
 * estado vivo y entra por la mejor. Solo si TODAS son incompatibles con el
 * perfil hay cierre, y entonces es un cierre honesto y con reembolso.
 *
 * Determinístico, CERO LLM: mismo esquema de puntaje que `evaluacionBrecha` y
 * `candidatosSeguimiento` (afinidad de tokens con el estado vivo). Quien juzga
 * el perfil sigue siendo el intérprete: si rechaza también la puerta nueva, se
 * vuelve a re-elegir con la rama nueva descartada, y así hasta que no quede
 * ninguna. La brújula propone; el intérprete dispone.
 */
import { semillasDelPack } from "./evaluacionBrecha";
import { dominioPermitido, type Grafo } from "./graph";
import { tokensCosecha } from "./tokens";

/**
 * El nodo y TODOS sus sucesores transitivos. El intérprete no rechaza un nodo:
 * rechaza una RAMA ("el nodo_actual y todos sus sucesores están diseñados
 * para…"). Descartar solo el nodo lo devolvería por la puerta de al lado, con
 * el mismo desajuste y un turno más de por medio.
 */
export function ramaDe(nid: string, graph: Grafo, tope = 500): Set<string> {
  const rama = new Set<string>([nid]);
  const cola = [nid];
  while (cola.length > 0 && rama.size < tope) {
    const actual = cola.shift()!;
    for (const siguiente of graph[actual]?.nodos_siguientes ?? []) {
      if (!rama.has(siguiente) && siguiente in graph) {
        rama.add(siguiente);
        cola.push(siguiente);
      }
    }
  }
  return rama;
}

export interface ResultadoReeleccion {
  puertaId: string;
  puntaje: number;
  /** true si la puerta nueva es una semilla del pack; false si es un vecino. */
  esSemilla: boolean;
  /** cuántas puertas del dominio quedaban disponibles al elegir esta */
  candidatas: number;
}

/** Afinidad: cuántos tokens del nodo aparecen en el estado vivo + el perfil de
 * la sesión. El mismo +1 por token de evaluacionBrecha y candidatosSeguimiento. */
function afinidad(nid: string, graph: Grafo, contexto: Set<string>): number {
  const n = graph[nid];
  if (!n) return 0;
  const texto = `${n.titulo_concepto ?? ""} ${(n.condiciones_activacion ?? []).join(" ")} ${
    (n.resumen_teorico ?? "").slice(0, 300)
  }`;
  let p = 0;
  for (const t of tokensCosecha(texto)) if (contexto.has(t)) p += 1;
  return p;
}

/**
 * La mejor puerta que le queda a este mundo, o null si no queda ninguna.
 *
 * Orden de preferencia, fiel a "las demás semillas del dominio (y sus vecinos)":
 * primero las SEMILLAS del pack que sobrevivan al descarte; si ninguna, sus
 * vecinos (cualquier nodo del dominio que siga en pie). Dentro de cada grupo,
 * la de mayor afinidad con el estado vivo. Empate → id, para que sea estable y
 * testeable.
 */
export function reelegirPuertaDeMundo(params: {
  dominio: string;
  graph: Grafo;
  /** el estado vivo del proyecto + el perfil de la sesión: el "contra qué" */
  estadoVivo: string | null;
  perfilSesion: string | null;
  /** nodos ya cubiertos por el proyecto (no se repite una puerta ya recorrida) */
  cubiertos: Set<string>;
  /** ramas que el intérprete ya rechazó en esta sesión */
  descartados: Set<string>;
}): ResultadoReeleccion | null {
  const { dominio, graph, cubiertos, descartados } = params;
  const contexto = tokensCosecha(`${params.estadoVivo ?? ""} ${params.perfilSesion ?? ""}`);

  const disponible = (nid: string) =>
    nid in graph &&
    !cubiertos.has(nid) &&
    !descartados.has(nid) &&
    dominioPermitido(nid, graph, [dominio]);

  const ordenar = (ids: string[]) =>
    ids
      .map((id) => ({ id, p: afinidad(id, graph, contexto) }))
      .sort((a, b) => b.p - a.p || a.id.localeCompare(b.id));

  const semillas = ordenar(semillasDelPack(dominio).map((s) => s.id).filter(disponible));
  if (semillas.length > 0) {
    return { puertaId: semillas[0].id, puntaje: semillas[0].p, esSemilla: true, candidatas: semillas.length };
  }

  // Sin semillas en pie: los vecinos del dominio. Un mundo es mucho más que sus
  // puertas de entrada, y el usuario pagó por el mundo entero.
  const vecinos = ordenar(Object.keys(graph).filter(disponible));
  if (vecinos.length > 0) {
    return { puertaId: vecinos[0].id, puntaje: vecinos[0].p, esSemilla: false, candidatas: vecinos.length };
  }
  return null;
}
