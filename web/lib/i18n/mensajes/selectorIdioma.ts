/** El selector de idioma (app/ui/SelectorIdioma.tsx). Los nombres de cada
 * idioma NO están aquí: van en su propia escritura (NOMBRE_IDIOMA, config.ts). */
import type { PorIdioma } from "../config";

const es = {
  etiqueta: "Idioma",
};

const en: typeof es = {
  etiqueta: "Language",
};

const fr: typeof es = {
  etiqueta: "Langue",
};

const pt: typeof es = {
  etiqueta: "Idioma",
};

const de: typeof es = {
  etiqueta: "Sprache",
};

const it: typeof es = {
  etiqueta: "Lingua",
};

const ja: typeof es = {
  etiqueta: "言語",
};

const zh: typeof es = {
  etiqueta: "语言",
};

const ko: typeof es = {
  etiqueta: "언어",
};

const ar: typeof es = {
  etiqueta: "اللغة",
};

const hi: typeof es = {
  etiqueta: "भाषा",
};

export const SELECTOR_IDIOMA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
