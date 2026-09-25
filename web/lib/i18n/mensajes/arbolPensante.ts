/** El riel del recorrido (app/ui/ArbolPensante.tsx). */
import type { PorIdioma } from "../config";

const es = {
  fueUnSalto: "fue un salto",
  generandoCon: "generando: {{etiqueta}}",
  generando: "generando…",
};

export const ARBOL_PENSANTE: PorIdioma<typeof es> = { es };
