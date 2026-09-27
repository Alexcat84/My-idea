/**
 * sitemap.xml (i18n F6, DISENO §3.6 y D9): cada página pública en cada idioma
 * (`?lang=xx`) y en su URL sin parámetro (x-default), cada entrada con el mapa
 * hreflang completo, como pide el buscador. Hoy la única pública es la portada
 * (lib/i18n/seo.ts explica por qué /login no entra).
 */
import type { MetadataRoute } from "next";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { hreflangDe, PAGINAS_PUBLICAS, SITIO_URL, urlDeIdioma } from "@/lib/i18n/seo";

export default function sitemap(): MetadataRoute.Sitemap {
  return PAGINAS_PUBLICAS.flatMap((ruta) => {
    const languages = hreflangDe(ruta);
    const urls = [`${SITIO_URL}${ruta}`, ...ACTIVE_LOCALES.map((idioma) => urlDeIdioma(ruta, idioma))];
    return urls.map((url) => ({ url, changeFrequency: "monthly" as const, priority: 1, alternates: { languages } }));
  });
}
