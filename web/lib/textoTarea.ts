/**
 * El recorte de una tarea del checklist vive SOLO al mostrarla (contexto de la entrevista, 28 sep 2026). En la base y
 * en todo lo que viaja al motor la tarea va entera; una lista la muestra cortada en la ultima frontera de palabra
 * antes del tope, con "…", y el detalle de la actividad la muestra completa.
 */
export const TOPE_TAREA_EN_LISTA = 180;

export function textoParaMostrar(texto: string, tope = TOPE_TAREA_EN_LISTA): string {
  const t = (texto ?? "").replace(/\s+/g, " ").trim();
  if (t.length <= tope) return t;
  const corte = t.lastIndexOf(" ", tope - 1);
  return `${t.slice(0, corte > 0 ? corte : tope - 1).trimEnd()}…`;
}
