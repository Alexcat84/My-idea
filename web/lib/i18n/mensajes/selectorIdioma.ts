/** El selector de idioma (app/ui/SelectorIdioma.tsx). Los nombres de cada
 * idioma NO están aquí: van en su propia escritura (NOMBRE_IDIOMA, config.ts). */
import type { PorIdioma } from "../config";

const es = {
  etiqueta: "Idioma",
};

const en: typeof es = {
  etiqueta: "Language",
};

export const SELECTOR_IDIOMA: PorIdioma<typeof es> = { es, en };
