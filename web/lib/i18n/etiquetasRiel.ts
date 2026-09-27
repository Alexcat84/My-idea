/**
 * D3 (i18n F5): las etiquetas del riel en cada idioma. Son una traducción
 * DERIVADA de `etiqueta_arbol` (la del grafo, en español), en archivos aparte:
 * el grafo no se toca. Las mantiene `scripts/i18n/etiquetasRiel.ts` (exporta
 * las que faltan, valida y aplica) y el auditor (`etiquetasRiel.test.ts`) exige
 * una por idioma para cada nodo vivo; al cambiar el grafo, solo se traducen las
 * que falten.
 *
 * Solo del lado del servidor (las lee `etiquetaArbol` en lib/engine/graph.ts).
 */
import type { ActiveLocale } from "./config";
import en from "./etiquetas/en.json";
import pt from "./etiquetas/pt.json";
import fr from "./etiquetas/fr.json";
import de from "./etiquetas/de.json";
import it from "./etiquetas/it.json";
import ja from "./etiquetas/ja.json";
import zh from "./etiquetas/zh.json";
import ko from "./etiquetas/ko.json";
import ar from "./etiquetas/ar.json";
import hi from "./etiquetas/hi.json";

export type IdiomaDerivado = Exclude<ActiveLocale, "es">;

export const ETIQUETAS_RIEL: Record<IdiomaDerivado, Record<string, string>> = {
  en: en as Record<string, string>,
  pt: pt as Record<string, string>,
  fr: fr as Record<string, string>,
  de: de as Record<string, string>,
  it: it as Record<string, string>,
  ja: ja as Record<string, string>,
  zh: zh as Record<string, string>,
  ko: ko as Record<string, string>,
  ar: ar as Record<string, string>,
  hi: hi as Record<string, string>,
};
