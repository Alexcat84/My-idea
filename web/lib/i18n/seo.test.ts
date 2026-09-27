// i18n F6 (DISENO §3.6 y D9): el SEO por idioma. Los hreflang apuntan a las
// variantes `?lang=xx` de la URL canónica, con el chino como zh-Hans, más un
// x-default a la URL sin parámetro (la que negocia el idioma del navegador). El
// auditor de §3.1: "la lista hreflang es igual a LOCALES". Los valores
// esperados están escritos a mano, no copiados de la función.
import { describe, expect, it } from "vitest";
import robots from "@/app/robots";
import sitemap from "@/app/sitemap";
import { LOCALES } from "./config";
import { alternatesDe, canonicaDe, hreflangDe, PAGINAS_PUBLICAS, RUTAS_PRIVADAS, SITIO_URL, urlDeIdioma } from "./seo";

describe("SEO por idioma", () => {
  it("la URL canónica del sitio es la de producción", () => {
    expect(SITIO_URL).toBe("https://www.myideaproject.com");
  });

  it("la variante de un idioma es ?lang=xx sobre la URL canónica", () => {
    expect(urlDeIdioma("/", "fr")).toBe("https://www.myideaproject.com/?lang=fr");
    expect(urlDeIdioma("/", "zh")).toBe("https://www.myideaproject.com/?lang=zh");
  });

  it("hreflang: los once con su etiqueta (zh → zh-Hans) más x-default a la URL sin parámetro", () => {
    expect(hreflangDe("/")).toEqual({
      es: "https://www.myideaproject.com/?lang=es",
      en: "https://www.myideaproject.com/?lang=en",
      pt: "https://www.myideaproject.com/?lang=pt",
      fr: "https://www.myideaproject.com/?lang=fr",
      de: "https://www.myideaproject.com/?lang=de",
      it: "https://www.myideaproject.com/?lang=it",
      ja: "https://www.myideaproject.com/?lang=ja",
      "zh-Hans": "https://www.myideaproject.com/?lang=zh",
      ko: "https://www.myideaproject.com/?lang=ko",
      ar: "https://www.myideaproject.com/?lang=ar",
      hi: "https://www.myideaproject.com/?lang=hi",
      "x-default": "https://www.myideaproject.com/",
    });
  });

  it("auditor (DISENO §3.1): la lista hreflang es igual a LOCALES, ni más ni menos", () => {
    const deVuelta = Object.entries(hreflangDe("/"))
      .filter(([codigo]) => codigo !== "x-default")
      .map(([, url]) => new URL(url).searchParams.get("lang"));
    expect([...deVuelta].sort()).toEqual([...LOCALES].sort());
    expect(Object.keys(hreflangDe("/"))).toHaveLength(LOCALES.length + 1);
  });

  it("la canónica de una visita: su variante si pidió ?lang= servible; si no, la URL sin parámetro", () => {
    expect(canonicaDe("/", "ko")).toBe("https://www.myideaproject.com/?lang=ko");
    expect(canonicaDe("/", undefined)).toBe("https://www.myideaproject.com/");
    expect(canonicaDe("/", "zz")).toBe("https://www.myideaproject.com/");
    expect(canonicaDe("/", ["en", "fr"])).toBe("https://www.myideaproject.com/?lang=en");
  });

  it("alternates junta canónica y hreflang", () => {
    const a = alternatesDe("/", "fr");
    expect(a.canonical).toBe("https://www.myideaproject.com/?lang=fr");
    expect(a.languages).toEqual(hreflangDe("/"));
  });

  it("solo la portada es pública para el buscador; las rutas de sesión quedan fuera", () => {
    expect(PAGINAS_PUBLICAS).toEqual(["/"]);
    for (const r of ["/login", "/auth/", "/nueva", "/ideas", "/idea/", "/cuenta", "/creditos", "/potenciadores", "/dev/", "/api/"])
      expect(RUTAS_PRIVADAS).toContain(r);
  });

  it("robots: deja la portada, cierra las rutas de sesión y anuncia el sitemap", () => {
    const r = robots();
    const reglas = Array.isArray(r.rules) ? r.rules[0] : r.rules;
    expect(reglas.userAgent).toBe("*");
    expect(reglas.allow).toBe("/");
    expect(reglas.disallow).toEqual(RUTAS_PRIVADAS);
    expect(r.sitemap).toBe("https://www.myideaproject.com/sitemap.xml");
  });

  it("sitemap: la portada en cada idioma y la sin parámetro, cada una con los doce alternos", () => {
    const s = sitemap();
    // 11 variantes ?lang= + 1 x-default = 12 entradas para la única página pública.
    expect(s).toHaveLength(12);
    expect(s.map((e) => e.url)).toContain("https://www.myideaproject.com/");
    expect(s.map((e) => e.url)).toContain("https://www.myideaproject.com/?lang=zh");
    for (const e of s) expect(e.alternates?.languages).toEqual(hreflangDe("/"));
  });
});
