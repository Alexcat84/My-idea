/**
 * SEO por idioma (i18n F6; DISENO §3.6 y D9). El idioma de la interfaz vive en
 * una cookie, que un buscador no trae: por eso cada idioma tiene su variante
 * `?lang=xx` de la misma URL (proxy.ts la honra en esa visita y escribe la
 * cookie), y los `hreflang` apuntan a esas variantes. El `x-default` es la URL
 * sin parámetro: la que negocia el idioma del navegador (y cae al español).
 *
 * Lo usan los metadatos de app/page.tsx, app/robots.ts y app/sitemap.ts. El
 * auditor de §3.1 ("la lista hreflang es igual a LOCALES") vive en seo.test.ts.
 */
import { ACTIVE_LOCALES, esActivo, htmlLang, LANG_DICTADO, type ActiveLocale } from "./config";

/** La URL canónica de producción (la que se indexa). */
export const SITIO_URL = "https://www.myideaproject.com";

/** Las páginas que se ofrecen al buscador. Solo la portada: es la única pública
 * de verdad. /login existe pero está fuera de todo flujo (proxy.ts) y no tiene
 * contenido que indexar; lo demás pide sesión o la acuña. */
export const PAGINAS_PUBLICAS = ["/"] as const;

/** Lo que robots.txt cierra: las rutas de sesión. /nueva va aquí sobre todo
 * porque ENTRAR ahí acuña una identidad invisible (proxy.ts): un rastreador no
 * debe fabricar usuarios invitados. */
export const RUTAS_PRIVADAS = [
  "/api/",
  "/auth/",
  "/login",
  "/nueva",
  "/ideas",
  "/idea/",
  "/cuenta",
  "/creditos",
  "/potenciadores",
  "/dev/",
];

/** La variante de una ruta en un idioma: `?lang=xx` sobre la URL canónica. */
export function urlDeIdioma(ruta: string, idioma: ActiveLocale): string {
  return `${SITIO_URL}${ruta}?lang=${idioma}`;
}

/** El mapa hreflang de una ruta: cada idioma servido con su etiqueta de <html>
 * (zh → zh-Hans) y el x-default a la URL sin parámetro. */
export function hreflangDe(ruta: string): Record<string, string> {
  const mapa: Record<string, string> = {};
  for (const idioma of ACTIVE_LOCALES) mapa[htmlLang(idioma)] = urlDeIdioma(ruta, idioma);
  mapa["x-default"] = `${SITIO_URL}${ruta}`;
  return mapa;
}

/** La canónica de una visita: su propia variante si pidió un `?lang=` servible
 * (cada variante se declara canónica de sí misma); si no, la URL sin parámetro. */
export function canonicaDe(ruta: string, lang: string | string[] | undefined): string {
  const pedido = Array.isArray(lang) ? lang[0] : lang;
  return esActivo(pedido) ? urlDeIdioma(ruta, pedido) : `${SITIO_URL}${ruta}`;
}

/** El bloque `alternates` de los metadatos de Next para una ruta. */
export function alternatesDe(ruta: string, lang: string | string[] | undefined) {
  return { canonical: canonicaDe(ruta, lang), languages: hreflangDe(ruta) };
}

/** La etiqueta de OpenGraph de un idioma (formato ll_RR): la misma variante
 * regional del dictado (LANG_DICTADO), una sola fuente. */
export function localeOg(idioma: ActiveLocale): string {
  return LANG_DICTADO[idioma].replace("-", "_");
}
