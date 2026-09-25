// i18n F2: el núcleo del sistema de idiomas (DISENO §3.1 y §3.2). Casos a mano.
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES, elegir, htmlDir, htmlLang, LANG_DICTADO, LOCALE_BASE, LOCALES, normalizarIdioma } from "./config";
import { interpolar, plural } from "./interpolar";
import { idiomasDeAcceptLanguage, negociarIdioma } from "./negociar";
import { etiquetasDe, rico } from "./rico";
import { idiomaDeRequest } from "./servidor";

describe("config", () => {
  it("once idiomas de la marca; en F2 solo el español está activo", () => {
    expect(LOCALES).toEqual(["es", "en", "pt", "fr", "de", "it", "ja", "zh", "ko", "ar", "hi"]);
    // F3: el inglés primero (decisión del fundador, 24 sep 2026).
    expect(ACTIVE_LOCALES).toEqual(["es", "en"]);
    expect(LOCALE_BASE).toBe("es");
  });
  it("un idioma no activo cae al español", () => {
    expect(normalizarIdioma("fr")).toBe("es");
    expect(normalizarIdioma("en")).toBe("en");
    expect(normalizarIdioma("xx")).toBe("es");
    expect(normalizarIdioma(undefined)).toBe("es");
    expect(elegir({ es: { hola: "Hola" }, en: { hola: "Hello" } }, "fr")).toEqual({ hola: "Hola" });
    expect(elegir({ es: { hola: "Hola" }, en: { hola: "Hello" } }, "en")).toEqual({ hola: "Hello" });
  });
  it("el dictado por voz sigue el idioma de la interfaz; en español, es-MX como siempre", () => {
    // Casos a mano: la variante de cada idioma, fijada por el diseño.
    expect(LANG_DICTADO).toEqual({
      es: "es-MX",
      en: "en-US",
      pt: "pt-BR",
      fr: "fr-CA",
      de: "de-DE",
      it: "it-IT",
      ja: "ja-JP",
      zh: "zh-CN",
      ko: "ko-KR",
      ar: "ar-SA",
      hi: "hi-IN",
    });
    // Cada variante empieza por su idioma (no se cruzan).
    for (const l of LOCALES) expect(LANG_DICTADO[l].split("-")[0]).toBe(l);
    // useSpeech ya no fija el español: toma la variante del idioma que recibe.
    const hook = readFileSync(path.join(__dirname, "..", "useSpeech.ts"), "utf8");
    expect(hook).toMatch(/rec\.lang = LANG_DICTADO\[idiomaRef\.current\];/);
    expect(hook).not.toMatch(/"es-MX"/);
  });
  it("lang y dir de <html>: zh-Hans y el árabe de derecha a izquierda", () => {
    expect(htmlLang("es")).toBe("es");
    expect(htmlLang("zh")).toBe("zh-Hans");
    expect(htmlDir("ar")).toBe("rtl");
    expect(htmlDir("es")).toBe("ltr");
  });
});

describe("negociación del idioma", () => {
  it("el Accept-Language por su q, con la subetiqueta primaria", () => {
    // fr-CA (q 1) > en (0.8) > es-MX (0.5); el * se ignora
    expect(idiomasDeAcceptLanguage("es-MX;q=0.5, fr-CA, en;q=0.8, *;q=0.1")).toEqual(["fr", "en", "es"]);
    expect(idiomasDeAcceptLanguage(null)).toEqual([]);
  });
  it("primera visita: del navegador si está activo, si no el español; y se escribe la cookie", () => {
    expect(negociarIdioma({ acceptLanguage: "es-MX,es;q=0.9" })).toEqual({ idioma: "es", escribirCookie: true });
    // F3: el inglés ya está activo; el francés todavía no, cae al español
    expect(negociarIdioma({ acceptLanguage: "en-US" })).toEqual({ idioma: "en", escribirCookie: true });
    expect(negociarIdioma({ acceptLanguage: "fr-CA,fr;q=0.9" })).toEqual({ idioma: "es", escribirCookie: true });
    expect(negociarIdioma({ acceptLanguage: "fr-CA,en;q=0.8" })).toEqual({ idioma: "en", escribirCookie: true });
  });
  it("con cookie: manda la cookie y no se reescribe", () => {
    expect(negociarIdioma({ cookie: "es", acceptLanguage: "en" })).toEqual({ idioma: "es", escribirCookie: false });
  });
  it("?lang= manda sobre la cookie (D9) y la actualiza solo si cambia", () => {
    expect(negociarIdioma({ parametroUrl: "es", cookie: "es" })).toEqual({ idioma: "es", escribirCookie: false });
    expect(negociarIdioma({ parametroUrl: "es", cookie: null })).toEqual({ idioma: "es", escribirCookie: true });
    // un ?lang= que no está activo se ignora
    expect(negociarIdioma({ parametroUrl: "zz", cookie: "es" })).toEqual({ idioma: "es", escribirCookie: false });
    expect(negociarIdioma({ parametroUrl: "en", cookie: "es" })).toEqual({ idioma: "en", escribirCookie: true });
  });
  it("proxy.ts negocia y escribe la cookie, también en la portada pública", () => {
    const proxy = readFileSync(path.join(__dirname, "..", "..", "proxy.ts"), "utf8");
    expect(proxy).toMatch(/negociarIdioma\(/);
    expect(proxy).toMatch(/response\.cookies\.set\(COOKIE_IDIOMA/);
    // la negociación va antes de la regla de rutas públicas (la portada también la recibe)
    expect(proxy.indexOf("negociarIdioma(")).toBeLessThan(proxy.indexOf("esRutaPublica(pathname)"));
  });
  it("las rutas de /api leen el idioma de la cookie de la petición", () => {
    const con = (cookie: string) => new Request("http://x", { headers: { cookie } });
    expect(idiomaDeRequest(con("otra=1; myidea_idioma=es"))).toBe("es");
    expect(idiomaDeRequest(con("myidea_idioma=zz"))).toBe("es");
    expect(idiomaDeRequest(new Request("http://x"))).toBe("es");
  });
});

describe("interpolar y plural", () => {
  it("reemplaza los marcadores", () => {
    expect(interpolar("hace {{n}} min", { n: 21 })).toBe("hace 21 min");
  });
  it("un marcador sin valor lanza (nunca un {{n}} en pantalla)", () => {
    expect(() => interpolar("hace {{n}} min", {})).toThrow(/falta el valor de \{\{n\}\}/);
  });
  it("plural por las reglas del idioma: 1 crédito, 0 y 2 créditos", () => {
    const formas = { one: "{{n}} crédito", other: "{{n}} créditos" };
    expect(plural("es", 1, formas)).toBe("1 crédito");
    expect(plural("es", 0, formas)).toBe("0 créditos");
    expect(plural("es", 2, formas)).toBe("2 créditos");
  });
});

describe("rico: frases con partes marcadas", () => {
  it("convierte las etiquetas en sus elementos", () => {
    const html = renderToStaticMarkup(<p>{rico("Tu plan <b>ya está</b> listo<br/>seguimos", { b: (c) => <strong>{c}</strong> })}</p>);
    expect(html).toBe("<p>Tu plan <strong>ya está</strong> listo<br/>seguimos</p>");
  });
  it("sin etiquetas devuelve el texto tal cual", () => {
    expect(rico("Guardar")).toBe("Guardar");
  });
  it("una etiqueta sin componente lanza", () => {
    expect(() => rico("hola <x>mundo</x>")).toThrow(/<x> no tiene componente/);
  });
  it("etiquetasDe lista las etiquetas (para el auditor)", () => {
    expect(etiquetasDe("a <b>b</b> c<br/>")).toEqual(["b", "br"]);
  });
});
