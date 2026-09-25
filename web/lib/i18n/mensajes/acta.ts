/** El acta de cierre en el informe markdown (lib/acta.ts: actaMarkdown). Los
 * "## ", "- " y "**" son estructura markdown y se conservan en cada idioma;
 * {{pct}} es " (NN%)" o vacío. */
import type { PorIdioma } from "../config";

const es = {
  titulo: "## Acta de cierre",
  cerradaEl: "- Cerrada el {{fecha}}",
  accionesAlCerrar: "- Acciones al cerrar: **{{hechas}} de {{total}}**{{pct}}",
  mundo: "- {{mundo}}: **{{hechas}} de {{total}}**{{pct}}, {{estado}}",
  completadoEl: "completado el {{fecha}}",
  abierto: "abierto",
  tituloPorQue: "### Por qué la cerraste aquí",
};

const en: typeof es = {
  titulo: "## Closing record",
  cerradaEl: "- Closed on {{fecha}}",
  accionesAlCerrar: "- Actions at close: **{{hechas}} of {{total}}**{{pct}}",
  mundo: "- {{mundo}}: **{{hechas}} of {{total}}**{{pct}}, {{estado}}",
  completadoEl: "completed on {{fecha}}",
  abierto: "open",
  tituloPorQue: "### Why you closed it here",
};

export const ACTA: PorIdioma<typeof es> = { es, en };
