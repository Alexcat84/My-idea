/**
 * AUD-09 B10: la ÚNICA regla de la etapa de una idea, para /ideas y para el
 * encabezado de la idea. Antes cada una tenía la suya y, en un seguimiento
 * abierto, el encabezado volvía a "La Exploración" (3). Pura.
 *
 * - La exploración del NÚCLEO antes de tener plan: 3.
 * - Un seguimiento abierto trabaja sobre el plan: cuenta como obra (5).
 * - Una sesión de mundo no hace retroceder el viaje principal.
 */
export function etapaDeIdea(d: {
  conPlan: boolean;
  enObra: boolean;
  explorandoNucleo: boolean;
  seguimientoAbierto: boolean;
  ordenada: boolean;
}): number {
  if (d.enObra || (d.conPlan && d.seguimientoAbierto)) return 5;
  if (d.conPlan) return 4;
  if (d.explorandoNucleo) return 3;
  return d.ordenada ? 2 : 1;
}
