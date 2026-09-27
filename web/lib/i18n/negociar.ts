/**
 * Qué idioma recibe una visita (DISENO §3.2). Puro: lo usa proxy.ts.
 *
 * Orden: `?lang=xx` en la URL manda en esa visita (D9) y actualiza la cookie;
 * si no, la cookie `myidea_idioma`; si no hay cookie (primera visita), el
 * `Accept-Language` del navegador (por su `q`, con la subetiqueta primaria:
 * pt-BR → pt, zh-TW → zh, fr-CA → fr); y si nada coincide, el español.
 * Solo se devuelven idiomas ACTIVOS.
 */
import { esActivo, LOCALE_BASE, type ActiveLocale } from "./config";

/** Los idiomas del Accept-Language, del más preferido al menos (subetiqueta primaria). */
export function idiomasDeAcceptLanguage(cabecera: string | null | undefined): string[] {
  if (!cabecera) return [];
  return cabecera
    .split(",")
    .map((parte, orden) => {
      const [etiqueta, ...params] = parte.trim().split(";");
      const q = params.map((p) => p.trim()).find((p) => p.startsWith("q="));
      const peso = q ? Number(q.slice(2)) : 1;
      return { idioma: etiqueta.trim().toLowerCase().split("-")[0], peso: Number.isFinite(peso) ? peso : 0, orden };
    })
    .filter((x) => x.idioma && x.idioma !== "*" && x.peso > 0)
    .sort((a, b) => b.peso - a.peso || a.orden - b.orden)
    .map((x) => x.idioma);
}

export function negociarIdioma(d: {
  parametroUrl?: string | null;
  cookie?: string | null;
  acceptLanguage?: string | null;
}): { idioma: ActiveLocale; escribirCookie: boolean } {
  if (esActivo(d.parametroUrl)) return { idioma: d.parametroUrl, escribirCookie: d.parametroUrl !== d.cookie };
  if (esActivo(d.cookie)) return { idioma: d.cookie, escribirCookie: false };
  const delNavegador = idiomasDeAcceptLanguage(d.acceptLanguage).find(esActivo);
  return { idioma: delNavegador ?? LOCALE_BASE, escribirCookie: true };
}
