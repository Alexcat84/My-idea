// i18n F6 (D2 + F4): la tipografía del PAPEL sigue el idioma del documento.
//
// F4 carga la Noto de una escritura (JP, SC, KR, Devanagari, Arabic) solo en
// su idioma de interfaz: la clase de next/font va en <html> según la cookie, y
// las cinco van sin precarga (el navegador baja una fuente solo si algo la
// usa). Un proyecto en coreano impreso desde una interfaz en español quedaba
// sin su Noto. Ahora el layout le pasa al papel la clase de cada escritura
// (solo nombres de clase, sin cargar nada) y PapelEnIdioma pone en su
// envoltorio la del idioma del documento, con `papel-escritura`, que vuelve a
// declarar la familia del cuerpo (la de <body> ya viene resuelta con la
// variable de <html>, así que sin redeclararla la clase no cambiaría nada).
//
// Casos, contados a mano:
//   - interfaz es, documento ko, clases { ko: "noto-kr" } → envoltorio con "noto-kr papel-escritura"
//   - interfaz es, documento en (latino, sin Noto)        → envoltorio sin clase de escritura
//   - interfaz ja, documento ko                           → la de ko ("noto-kr"), no la de ja
//   - sin clases (fuera del layout, p. ej. en una prueba)  → sin clase de escritura
//   - mismo idioma                                         → sin envoltorio, marcado idéntico
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import type { ActiveLocale } from "@/lib/i18n/config";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { PapelEnIdioma, TipografiasDeEscritura } from "./PapelEnIdioma";

const CLASES = { ja: "noto-jp", zh: "noto-sc", ko: "noto-kr", ar: "noto-ar", hi: "noto-hi" };

function pintar(interfaz: ActiveLocale, documento: ActiveLocale, clases: Record<string, string> | null = CLASES) {
  const papel = (
    <IdiomaProvider idioma={interfaz}>
      <PapelEnIdioma idioma={documento}>
        <p>텍스트</p>
      </PapelEnIdioma>
    </IdiomaProvider>
  );
  return renderToStaticMarkup(clases ? <TipografiasDeEscritura clases={clases}>{papel}</TipografiasDeEscritura> : papel);
}

describe("la Noto del idioma del documento en el papel", () => {
  it("interfaz español, documento coreano: la clase de la Noto KR y papel-escritura", () => {
    const html = pintar("es", "ko");
    expect(html).toContain('class="contents noto-kr papel-escritura"');
  });
  it("interfaz español, documento inglés: ninguna Noto", () => {
    const html = pintar("es", "en");
    expect(html).toContain('class="contents"');
    expect(html).not.toContain("papel-escritura");
  });
  it("interfaz japonés, documento coreano: la de coreano", () => {
    const html = pintar("ja", "ko");
    expect(html).toContain("noto-kr papel-escritura");
    expect(html).not.toContain("noto-jp");
  });
  it("interfaz japonés, documento español: el papel no cambia de familia", () => {
    expect(pintar("ja", "es")).not.toContain("papel-escritura");
  });
  it("sin las clases del layout: ninguna Noto", () => {
    expect(pintar("es", "ko", null)).not.toContain("papel-escritura");
  });
  it("mismo idioma: sin envoltorio", () => {
    expect(pintar("ko", "ko")).toBe("<p>텍스트</p>");
  });
});

describe("el layout y la hoja de estilo", () => {
  const raiz = path.join(__dirname, "..", "..");
  const layout = readFileSync(path.join(raiz, "app", "layout.tsx"), "utf8");
  const css = readFileSync(path.join(raiz, "app", "globals.css"), "utf8");
  it("el layout le pasa al papel las clases de cada escritura", () => {
    expect(layout).toMatch(/<TipografiasDeEscritura clases=\{CLASES_ESCRITURA\}>/);
    expect(layout).toMatch(/const CLASES_ESCRITURA/);
  });
  it("papel-escritura vuelve a declarar la familia del cuerpo con la escritura detrás de Inter", () => {
    expect(css).toMatch(/\.papel-escritura\s*\{[^}]*font-family: var\(--font-inter\), var\(--font-escritura, system-ui\), system-ui, sans-serif;/);
  });
  it("los títulos del papel impreso, en serif, caen en la Noto de la escritura antes que en la del sistema", () => {
    expect(css).toMatch(/font-family: Georgia, "Source Serif 4", "Times New Roman", var\(--font-escritura, serif\), serif !important;/);
  });
});
