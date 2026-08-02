/**
 * Campaña "Espacios": un proyecto = el viaje CORE + sus MUNDOS; cada uno es un
 * ESPACIO con operación propia (su plan, sus tareas, su línea de tiempo), bajo
 * un mismo techo de historia. La regla de la casa (BANCO §7.1):
 *   "lo que cuenta historia es global; lo que mide operación es del espacio."
 *
 * Estas funciones PURAS deciden qué pertenece a qué espacio: las usan la vista
 * scopeada (ManosALaObra), la navegación al hub (IdeaView) y —Fase 3— las
 * etiquetas de espacio de la bitácora/expediente. Fuente única de la regla,
 * para que la UI y los tests nunca discrepen.
 */

export const ESPACIO_CORE = "core";

/** El dominio pertenece al core si es nulo o "core"; cualquier otro es un mundo. */
export function esEspacioCore(dominio: string | null | undefined): boolean {
  return !dominio || dominio === ESPACIO_CORE;
}

/**
 * Qué mundos se muestran en una vista scopeada a `soloDominio`:
 * - sin `soloDominio` (undefined/null) → TODOS (comportamiento histórico:
 *   los mundos apilados bajo el core en la misma vista).
 * - `"core"` → NINGUNO (los mundos viven en su propio hub, no bajo el core).
 * - un dominio de mundo → solo ESE (su hub muestra únicamente su operación).
 */
export function mundosDelEspacio<T extends { dominio: string }>(
  mundos: T[],
  soloDominio?: string | null
): T[] {
  if (!soloDominio) return mundos;
  if (soloDominio === ESPACIO_CORE) return [];
  return mundos.filter((m) => m.dominio === soloDominio);
}

/** El deep-link del espacio: el hub de un mundo, o el Manos a la Obra del core. */
export function urlDelEspacio(projectId: string, dominio: string): string {
  return esEspacioCore(dominio)
    ? `/idea/${projectId}?vista=manos`
    : `/idea/${projectId}?vista=mundo&dominio=${dominio}`;
}
