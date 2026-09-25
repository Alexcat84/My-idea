/**
 * Los textos del catálogo con variables: `{{clave}}` (DISENO §3.1). Una clave
 * que falta es un error de programación, así que lanza (fallar ruidoso): nunca
 * un "{{n}}" visible en pantalla.
 */
import type { Locale } from "./config";

export function interpolar(texto: string, valores: Record<string, string | number>): string {
  return texto.replace(/\{\{(\w+)\}\}/g, (_, clave: string) => {
    if (!(clave in valores)) throw new Error(`i18n: falta el valor de {{${clave}}} en "${texto}"`);
    return String(valores[clave]);
  });
}

/** Las formas de una palabra según la cantidad, por las reglas del idioma
 * (Intl.PluralRules): en español "one" y "other"; otros idiomas usan más. */
export type FormasPlural = { one: string; other: string } & Partial<Record<"zero" | "two" | "few" | "many", string>>;

/** Elige la forma plural y le pone la cantidad en `{{n}}`. */
export function plural(idioma: Locale, n: number, formas: FormasPlural): string {
  const categoria = new Intl.PluralRules(idioma).select(n) as keyof FormasPlural;
  return interpolar(formas[categoria] ?? formas.other, { n });
}
