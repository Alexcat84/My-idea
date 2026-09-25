/** El riel del recorrido (app/ui/ArbolPensante.tsx). */
import type { PorIdioma } from "../config";

const es = {
  fueUnSalto: "fue un salto",
  generandoCon: "generando: {{etiqueta}}",
  generando: "generando…",
};

const en: typeof es = {
  fueUnSalto: "a jump in topic",
  generandoCon: "generating: {{etiqueta}}",
  generando: "generating…",
};

export const ARBOL_PENSANTE: PorIdioma<typeof es> = { es, en };
