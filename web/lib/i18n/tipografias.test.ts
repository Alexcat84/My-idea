// i18n F4 (DISENO §3.5): Inter no trae kana, han, hangul, devanagari ni árabe.
// Cada una de esas escrituras tiene su Noto con next/font, y se carga SOLO
// cuando la página va en ese idioma: preload: false (nadie descarga lo que no
// usa) y la clase de la fuente se pone en <html> según el idioma. La fuente
// de la escritura entra DETRÁS de Inter: las letras latinas y las cifras
// siguen siendo Inter en todos los idiomas.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const raiz = path.join(__dirname, "..", "..");
const layout = readFileSync(path.join(raiz, "app", "layout.tsx"), "utf8");
const css = readFileSync(path.join(raiz, "app", "globals.css"), "utf8");

describe("tipografías por escritura (F4)", () => {
  it("una Noto por escritura, sin precarga, con la misma variable", () => {
    for (const f of ["Noto_Sans_JP", "Noto_Sans_SC", "Noto_Sans_KR", "Noto_Sans_Devanagari", "Noto_Sans_Arabic"]) {
      expect(layout, f).toMatch(new RegExp(`${f}\\(\\{[^}]*variable: "--font-escritura"[^}]*preload: false`));
    }
  });
  it("cada idioma elige la suya; los latinos, ninguna", () => {
    expect(layout).toMatch(/ja: notoJP/);
    expect(layout).toMatch(/zh: notoSC/);
    expect(layout).toMatch(/ko: notoKR/);
    expect(layout).toMatch(/hi: notoDevanagari/);
    expect(layout).toMatch(/ar: notoArabic/);
    for (const l of ["es", "en", "pt", "fr", "de", "it"]) expect(layout).toMatch(new RegExp(`${l}: null`));
  });
  it("la escritura va detrás de Inter en la familia del cuerpo", () => {
    expect(css).toMatch(/font-family: var\(--font-inter\), var\(--font-escritura, system-ui\), system-ui/);
    expect(css).toMatch(/--font-sans: var\(--font-inter\), var\(--font-escritura, system-ui\)/);
  });
});
