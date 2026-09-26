/**
 * robots.txt (i18n F6, DISENO §3.6): la portada se deja rastrear en sus once
 * idiomas (`/?lang=xx`); las rutas de sesión se cierran, sobre todo /nueva, que
 * acuña una identidad invisible al entrar (proxy.ts). La lista vive en
 * lib/i18n/seo.ts.
 */
import type { MetadataRoute } from "next";
import { RUTAS_PRIVADAS, SITIO_URL } from "@/lib/i18n/seo";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: "*", allow: "/", disallow: RUTAS_PRIVADAS },
    sitemap: `${SITIO_URL}/sitemap.xml`,
  };
}
