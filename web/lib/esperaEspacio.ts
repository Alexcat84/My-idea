/**
 * esperaEspacio.ts: qué muestra la página de la idea cuando se pidió un
 * espacio (Manos a la Obra o el de un mundo) y sus datos aún no están
 * (AUD-09 H09). Pura. Toda espera tiene salida: sin plan no hay nada que
 * esperar, y si el checklist falló se dice y se ofrece reintentar.
 */
export type EstadoEspacio = "listo" | "cargando" | "sin_plan" | "error";

export function estadoEspacio(e: { hayPlan: boolean; hayChecklist: boolean; errorChecklist: string | null }): EstadoEspacio {
  if (!e.hayPlan) return "sin_plan";
  if (e.hayChecklist) return "listo";
  if (e.errorChecklist) return "error";
  return "cargando";
}
