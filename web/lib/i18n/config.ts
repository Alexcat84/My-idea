/**
 * Idiomas de My Idea (i18n F2; diseño en docs/i18n/DISENO.md §3). Calco del
 * I Ching (iching-experiments/web/lib/i18n/config.ts), con el español de base.
 *
 * LOCALES son los once de la marca. ACTIVE_LOCALES son los que se sirven HOY:
 * los catálogos se exigen completos sobre los activos, no sobre los once. En F2
 * solo el español está activo (la app se ve idéntica); F3 agrega los otros diez
 * a ACTIVE_LOCALES y el compilador reclama cada clave que falte en cada idioma.
 *
 * Sin librería (como el I Ching, que prohíbe next-intl): catálogos TypeScript
 * por área en `mensajes/`, cada uno un `PorIdioma<T>`.
 */

/** Los once idiomas de la marca. */
export const LOCALES = ["es", "en", "pt", "fr", "de", "it", "ja", "zh", "ko", "ar", "hi"] as const;
export type Locale = (typeof LOCALES)[number];

/** Los idiomas servidos hoy (F2: solo el español). */
export const ACTIVE_LOCALES = ["es"] as const satisfies readonly Locale[];
export type ActiveLocale = (typeof ACTIVE_LOCALES)[number];

/** El idioma en que se escribe todo (y el que recibe quien no pide otro). */
export const LOCALE_BASE: ActiveLocale = "es";

/** Un catálogo que el compilador obliga a completar en cada idioma activo. */
export type PorIdioma<T> = Record<ActiveLocale, T>;

/** La cookie de la preferencia de idioma (legible por el cliente). */
export const COOKIE_IDIOMA = "myidea_idioma";
export const COOKIE_IDIOMA_MAX_AGE = 60 * 60 * 24 * 365;

export function esLocale(x: unknown): x is Locale {
  return typeof x === "string" && (LOCALES as readonly string[]).includes(x);
}

export function esActivo(x: unknown): x is ActiveLocale {
  return typeof x === "string" && (ACTIVE_LOCALES as readonly string[]).includes(x);
}

/** Un idioma servible a partir de cualquier cosa: si no está activo, el base. */
export function normalizarIdioma(x: unknown): ActiveLocale {
  return esActivo(x) ? x : LOCALE_BASE;
}

/** Los textos de un catálogo en un idioma (cae al base si no está activo). */
export function elegir<T>(catalogo: PorIdioma<T>, idioma: unknown): T {
  return catalogo[normalizarIdioma(idioma)];
}

/** El atributo lang de <html>: el chino va como zh-Hans (D7). */
export function htmlLang(idioma: Locale): string {
  return idioma === "zh" ? "zh-Hans" : idioma;
}

/** Dirección del documento: el árabe es de derecha a izquierda. */
export function htmlDir(idioma: Locale): "ltr" | "rtl" {
  return idioma === "ar" ? "rtl" : "ltr";
}

/** Cada idioma en su propia escritura (para el selector). */
export const NOMBRE_IDIOMA: Record<Locale, string> = {
  es: "Español",
  en: "English",
  pt: "Português",
  fr: "Français",
  de: "Deutsch",
  it: "Italiano",
  ja: "日本語",
  zh: "中文",
  ko: "한국어",
  ar: "العربية",
  hi: "हिन्दी",
};
