// Decisión del fundador (8 oct 2026): los enlaces legales (Privacidad, Términos,
// Cookies, Eliminar cuenta) claramente visibles y con buen contraste; Preguntas
// frecuentes más vistosa (una tarjeta destacada).
//
// Contraste (WCAG 2.x, cálculo a mano): luminancia relativa L = 0.2126 R +
// 0.7152 G + 0.0722 B con cada canal linealizado; contraste = (L1 + 0.05) /
// (L2 + 0.05). El fondo es negro (#000, L = 0), así que contraste = 20 L + 1.
//   #A6A7AD (el gris de antes): canales 166/167/173 → lineales 0.3813, 0.3864,
//   0.4179 → L = 0.0811 + 0.2764 + 0.0302 = 0.3877 → contraste 8.75.
//   #E4E5EA (el de ahora): 228/229/234 → 0.7758, 0.7835, 0.8228 → L = 0.1649 +
//   0.5604 + 0.0594 = 0.7847 → contraste 16.69.
// La vara: AAA (7) y además MÁS claro que los enlaces de navegación del pie,
// para que lo legal no se pierda entre ellos.
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { PORTADA } from "@/lib/i18n/mensajes/portada";
import { navPublica } from "@/lib/legal/paginas";
import { PaginaPublica } from "./PaginaPublica";

function lineal(c: number) {
  const s = c / 255;
  return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4;
}
function contrasteSobreNegro(hex: string) {
  const [r, g, b] = [1, 3, 5].map((i) => lineal(parseInt(hex.slice(i, i + 2), 16)));
  return 20 * (0.2126 * r + 0.7152 * g + 0.0722 * b) + 1;
}

describe("el cálculo de contraste coincide con el hecho a mano", () => {
  it("#A6A7AD ≈ 8.75 y #E4E5EA ≈ 16.69", () => {
    expect(contrasteSobreNegro("#A6A7AD")).toBeCloseTo(8.75, 1);
    expect(contrasteSobreNegro("#E4E5EA")).toBeCloseTo(16.69, 1);
  });
});

describe("la portada: lo legal en su propia fila, la ayuda en una tarjeta", () => {
  const landing = readFileSync(path.join(__dirname, "Landing.tsx"), "utf8");
  const colorLegal = landing.match(/const COLOR_LEGAL = "(#[0-9A-Fa-f]{6})"/)?.[1] ?? "";

  it("los cuatro legales van en un <nav> propio con su etiqueta", () => {
    const nav = landing.match(/<nav aria-label=\{t\.pie\.legal\}[\s\S]*?<\/nav>/)?.[0] ?? "";
    for (const href of ["/privacidad", "/terminos", "/cookies", "/eliminar-cuenta"]) expect(nav).toContain(`href="${href}"`);
    expect(nav).not.toContain('href="/preguntas-frecuentes"');
  });

  it("con contraste AAA y más claros que la navegación (#A6A7AD)", () => {
    expect(contrasteSobreNegro(colorLegal)).toBeGreaterThanOrEqual(7);
    expect(contrasteSobreNegro(colorLegal)).toBeGreaterThan(contrasteSobreNegro("#A6A7AD"));
  });

  it("Preguntas frecuentes es una tarjeta con su descripción, en los once idiomas", () => {
    expect(landing).toMatch(/href="\/preguntas-frecuentes"[\s\S]{0,1200}\{t\.pie\.preguntasDesc\}/);
    for (const idioma of ACTIVE_LOCALES) {
      expect(PORTADA[idioma].pie.preguntasDesc.length, idioma).toBeGreaterThan(10);
      expect(PORTADA[idioma].pie.legal.length, idioma).toBeGreaterThan(1);
    }
  });
});

describe("las páginas públicas (legales y de ayuda)", () => {
  const html = renderToStaticMarkup(
    <PaginaPublica idioma="es">
      <h1>Privacidad</h1>
    </PaginaPublica>,
  );
  const t = navPublica("es");

  /** Las clases de la etiqueta <a> con ese href (el orden de atributos no importa). */
  const clasesDe = (re: RegExp) => (html.match(re)?.[0].match(/class="([^"]*)"/)?.[1] ?? "").split(/\s+/);
  const enlace = (href: string) => clasesDe(new RegExp(`<a[^>]*href="${href}"[^>]*>`));

  it("el texto usa la tinta del tema, no un --ink inexistente que caía en negro sobre negro", () => {
    expect(html).not.toContain("--ink");
    expect(clasesDe(/<main[^>]*>/)).toEqual(expect.arrayContaining(["text-ink", "bg-bg"]));
  });

  it("los legales se leen en la tinta clara y subrayados", () => {
    for (const href of ["/privacidad", "/terminos", "/cookies", "/eliminar-cuenta"]) {
      expect(enlace(href), href).toEqual(expect.arrayContaining(["text-ink", "underline"]));
    }
  });

  it("Preguntas frecuentes es una tarjeta destacada", () => {
    expect(enlace("/preguntas-frecuentes")).toEqual(expect.arrayContaining(["border-accent/45", "bg-accent/10"]));
    expect(html).toContain(t.preguntas);
  });
});
