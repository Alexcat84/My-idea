/**
 * inicioProyecto.ts — ¿una fecha de realización es anterior al nacimiento del
 * proyecto? Desde el 8 oct 2026 (decisión del fundador, que revierte la
 * restricción de esa mañana) SÍ se puede marcar hecha una tarea con fecha
 * anterior (nunca futura): la bitácora la cuenta como "Ya lo habías hecho" y no
 * entra al ritmo personal ni a la puntualidad.
 *
 * El servidor no conoce la zona horaria de la persona; la pantalla ancla el día
 * elegido al mediodía local (isoDesdeInputLocal). El mediodía del día de
 * creación queda a menos de 12 h del instante de creación; el de cualquier día
 * anterior, a 12 h o más. Por eso: anterior ⇔ completado < creado − 12 h.
 */
const DOCE_HORAS = 12 * 3600 * 1000;

/** ¿La fecha de realización `valor` es anterior al inicio del proyecto
 * (`creadoIso`)? Una fecha sin hora ("2026-03-10") se lee como su mediodía UTC.
 * Sin fecha de creación no hay contra qué comparar: no es anterior. */
export function anteriorAlInicio(valor: string, creadoIso: string | null | undefined): boolean {
  if (!creadoIso) return false;
  const creado = Date.parse(creadoIso);
  const t = Date.parse(/^\d{4}-\d{2}-\d{2}$/.test(valor) ? `${valor}T12:00:00Z` : valor);
  if (Number.isNaN(creado) || Number.isNaN(t)) return false;
  return t < creado - DOCE_HORAS;
}
