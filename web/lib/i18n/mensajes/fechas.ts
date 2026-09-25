/** Fechas en palabras de persona (lib/fechas.ts): meses, días y los sellos de tiempo de la UI. */
import type { PorIdioma } from "../config";

const es = {
  meses: ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
  dias: ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"],
  haceUnMomento: "hace un momento",
  haceMin: "hace {{n}} min",
  hoyHora: "hoy {{hora}}",
  ayerHora: "ayer {{hora}}",
  haceDias: "hace {{n}} días",
  hoy: "hoy",
  ayer: "ayer",
  /** "20 de marzo" */
  diaDeMes: "{{d}} de {{mes}}",
  /** "20 de marzo de 2026" */
  diaDeMesAno: "{{d}} de {{mes}} de {{ano}}",
  /** "viernes 20 de marzo" */
  diaSemanaDeMes: "{{dia}} {{d}} de {{mes}}",
  /** "18 de julio, 14:32" */
  momento: "{{fecha}}, {{hora}}",
};

export const FECHAS: PorIdioma<typeof es> = { es };
