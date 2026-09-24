/**
 * registroProteccion.ts — Mundos de protección (P3): EL REGISTRO VISIBLE.
 *
 * La herramienta canónica de cada mundo de protección (el registro de riesgos,
 * el de peligros, el inventario de activos) instanciada sobre las actividades
 * REALES de la persona. Es la vista que convierte los enlaces de P2 en algo que
 * se lee: "esto detecté, así de probable y así de doloroso, y esta es la
 * respuesta, que protege a esta actividad tuya".
 *
 * PURO: recibe filas y devuelve filas. Sin red, sin Supabase, sin reloj.
 *
 * LA REGLA QUE MANDA AQUÍ (BANCO §7.1, y no la inventamos nosotros: la trae el
 * nodo "la matriz de colores te engaña"): la severidad se dice EN PALABRAS.
 * Nada de puntajes, porcentajes ni colores que finjan precisión. Este módulo no
 * calcula ningún número de riesgo y un test vigila que no empiece a hacerlo.
 */
import type { Camino, Dolor, Probabilidad } from "./dbContract";

/** Una respuesta del plan del mundo, tal como sale del checklist. */
export interface FilaRespuesta {
  id: string;
  texto: string;
  etapa: number;
  orden: number;
  estado: string;
  protege_item?: string | null;
  /** AUD-09 M15 (migración 041): los NODOS de la tarea protegida. La
   * protección apunta al nodo, no al id de la tarea de un ciclo. */
  protege_nodos?: string[] | null;
  deteccion?: string | null;
  probabilidad?: Probabilidad | null;
  dolor?: Dolor | null;
  camino?: Camino | null;
}

/** Una actividad del núcleo, para resolver a qué apunta cada respuesta. */
export interface ActividadProtegida {
  id: string;
  indice: number;
  titulo: string;
  /** Los nodos de la tarea (checklist_items.nodos_origen), para resolver la
   * protección por nodo en el plan vigente (AUD-09 M15). */
  nodos_origen?: string[] | null;
}

/**
 * AUD-09 M15 (decisión del fundador, 25 sep 2026): a qué tarea del plan VIGENTE
 * del núcleo apunta una respuesta de protección. Apunta al NODO de la tarea: un
 * ciclo nuevo inserta tareas con ids nuevos, y por id la protección quedaba
 * huérfana sin aviso. Orden: (1) si el id sigue en el plan vigente, ese (el
 * mismo ciclo no se mueve); (2) si no, la tarea vigente que comparte más nodos
 * (a igualdad, la primera del plan). Límite declarado: nodos_origen se guarda
 * por ETAPA (migración 037), así que en un ciclo nuevo la resolución es exacta
 * a nivel de etapa, no de tarea. Filas sin nodos (antes de la 037/041): solo por
 * id. `idsDelPlan` (opcional): TODOS los ids del plan vigente, retiradas
 * incluidas; si el id está ahí pero no en `vigente`, la tarea se retiró en este
 * ciclo y el nodo NO la muda a una hermana de etapa. Devuelve el id de la tarea
 * vigente, o null si ya no está. Pura.
 */
export function resolverProtegido(
  r: { protege_item?: string | null; protege_nodos?: string[] | null },
  vigente: ReadonlyArray<{ id: string; nodos_origen?: string[] | null }>,
  idsDelPlan?: ReadonlySet<string>
): string | null {
  if (r.protege_item && vigente.some((a) => a.id === r.protege_item)) return r.protege_item;
  if (r.protege_item && idsDelPlan?.has(r.protege_item)) return null;
  const nodos = r.protege_nodos ?? [];
  if (nodos.length > 0) {
    let mejor: { id: string; comunes: number } | null = null;
    for (const a of vigente) {
      const comunes = (a.nodos_origen ?? []).filter((n) => nodos.includes(n)).length;
      if (comunes > 0 && (!mejor || comunes > mejor.comunes)) mejor = { id: a.id, comunes };
    }
    return mejor?.id ?? null;
  }
  return null;
}

export interface EntradaRegistro {
  id: string;
  /** Lo que se detectó, en una frase. null si el enlazador no la produjo. */
  deteccion: string | null;
  /** La severidad EN PALABRAS. null cuando no vino o cayó fuera del enum. */
  probabilidad: Probabilidad | null;
  dolor: Dolor | null;
  /** El camino elegido (035). null = el enlazador no lo clasificó: se calla. */
  camino: Camino | null;
  /** La respuesta: la actividad del plan del mundo. */
  respuesta: string;
  estado: string;
  /** A qué actividad del núcleo protege. null = sistémica (el negocio entero). */
  protege: ActividadProtegida | null;
  /** true cuando la respuesta apuntaba a una actividad que ya no existe. La
   * migración 034 pone protege_item en null al borrarse, así que esto solo lo
   * sabe quien compara: se deja preparado para el chip de P4 y hoy es false. */
  protegidaDesaparecida: boolean;
}

/** La severidad en palabras de persona. Fuente única para pantalla y documento:
 * si vivieran en dos sitios, algún día dirían cosas distintas. */
export const PALABRA_PROBABILIDAD: Record<Probabilidad, string> = {
  poco_probable: "poco probable",
  probable: "probable",
  muy_probable: "muy probable",
};

export const PALABRA_DOLOR: Record<Dolor, string> = {
  poco: "dolería poco",
  bastante: "dolería bastante",
  mucho: "dolería mucho",
};

/** El camino en palabras de persona. Fuente única para pantalla y papel. */
export const PALABRA_CAMINO: Record<Camino, string> = {
  evitar: "evitarlo",
  mitigar: "reducirlo",
  transferir: "pasárselo a otro",
  aceptar: "aceptarlo con los ojos abiertos",
};

/**
 * La severidad de una entrada, en una frase. null cuando no hay nada que decir:
 * se calla en vez de rellenar con un "sin definir" que no aporta.
 */
export function severidadEnPalabras(e: {
  probabilidad: Probabilidad | null;
  dolor: Dolor | null;
}): string | null {
  const p = e.probabilidad ? PALABRA_PROBABILIDAD[e.probabilidad] : null;
  const d = e.dolor ? PALABRA_DOLOR[e.dolor] : null;
  if (p && d) return `${p} y ${d}`;
  return p ?? d ?? null;
}

/**
 * Arma el registro de un mundo de protección.
 *
 * Solo entran las respuestas que de verdad tienen algo que registrar: una
 * detección, un enlace o una severidad. Una tarea del plan del mundo que no es
 * una respuesta a nada (por ejemplo, si la estimación o el enlazador fallaron)
 * NO se inventa como fila del registro: se queda fuera, y la pantalla dirá que
 * el registro está por llenarse.
 */
export function armarRegistro(
  respuestas: FilaRespuesta[],
  actividadesNucleo: ActividadProtegida[],
  /** AUD-09 M15: todos los ids del plan vigente del núcleo, retiradas incluidas
   * (ver resolverProtegido). Sin él, una retirada podría mudarse por nodo. */
  idsDelPlan?: ReadonlySet<string>
): EntradaRegistro[] {
  const porId = new Map(actividadesNucleo.map((a) => [a.id, a]));
  return respuestas
    .filter((r) => r.deteccion || r.protege_item || r.protege_nodos?.length || r.probabilidad || r.dolor)
    .slice()
    .sort((a, b) => a.etapa - b.etapa || a.orden - b.orden)
    .map((r) => {
      const apuntaA = Boolean(r.protege_item || r.protege_nodos?.length);
      const idVigente = resolverProtegido(r, actividadesNucleo, idsDelPlan);
      const protege = idVigente ? porId.get(idVigente) ?? null : null;
      return {
        id: r.id,
        deteccion: r.deteccion ?? null,
        probabilidad: r.probabilidad ?? null,
        dolor: r.dolor ?? null,
        camino: r.camino ?? null,
        respuesta: r.texto,
        estado: r.estado,
        protege,
        protegidaDesaparecida: apuntaA && protege === null,
      };
    });
}

/** Cómo se nombra lo protegido en pantalla y en el documento. */
export function textoProtege(e: EntradaRegistro): string {
  if (e.protege) return `#${e.protege.indice} · ${e.protege.titulo}`;
  if (e.protegidaDesaparecida) return "la actividad que protegía ya no está en tu plan";
  return "tu negocio entero";
}

/**
 * El registro como markdown, para el documento descargable del espacio.
 * Mismo contenido que la pantalla, del mismo armador: el papel y la pantalla no
 * pueden contar cosas distintas.
 */
export function registroMarkdown(nombreMundo: string, entradas: EntradaRegistro[]): string {
  const l: string[] = [];
  l.push(`## Registro de ${nombreMundo}`);
  l.push("");
  if (entradas.length === 0) {
    l.push("Este registro se llenará con el plan de este mundo: cada cosa que detecte");
    l.push("quedará aquí junto a la respuesta que la atiende.");
    l.push("");
    return l.join("\n");
  }
  for (const e of entradas) {
    l.push(`### ${e.deteccion ?? e.respuesta}`);
    l.push("");
    const sev = severidadEnPalabras(e);
    if (sev) l.push(`Qué tan serio: ${sev}.`);
    if (e.camino) l.push(`El camino: ${PALABRA_CAMINO[e.camino]}.`);
    l.push(`Qué protege: ${textoProtege(e)}.`);
    l.push(`Tu respuesta: ${e.respuesta}`);
    l.push("");
  }
  return l.join("\n");
}
