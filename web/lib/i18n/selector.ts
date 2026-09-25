/**
 * El selector de idioma (i18n F3): cambiar de idioma es volver a pedir la misma
 * página con ?lang=xx (D9). proxy.ts lo negocia, manda en esa visita y escribe
 * la cookie myidea_idioma; el layout pinta <html lang dir> con él.
 */
import type { ActiveLocale } from "./config";

export function urlConIdioma(href: string, idioma: ActiveLocale): string {
  const url = new URL(href);
  url.searchParams.set("lang", idioma);
  return url.toString();
}
