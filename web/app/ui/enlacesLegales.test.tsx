// Corrección del fundador (8 oct 2026): el pie de la portada se queda con su
// diseño ORIGINAL (posición, tamaño, colores: una sola fila). Lo que estaba
// "opaco" eran las PÁGINAS legales y de ayuda: su marco pedía un --ink que no
// existe y caía en #1a1a1a, texto casi negro sobre el fondo negro. Eso es lo que
// se arregla: las páginas se leen en la tinta del tema, con su barra de enlaces
// original. Y en Preguntas frecuentes, la pregunta en azul y la respuesta en
// blanco.
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { navPublica } from "@/lib/legal/paginas";
import { PaginaPublica } from "./PaginaPublica";

const LEGALES = ["/privacidad", "/terminos", "/cookies", "/preguntas-frecuentes", "/eliminar-cuenta"];

describe("la portada: el pie original, intacto", () => {
  const landing = readFileSync(path.join(__dirname, "Landing.tsx"), "utf8");
  const pie = landing.match(/<footer[\s\S]*?<\/footer>/)?.[0] ?? "";

  it("una sola fila con su relleno, su caja y su orden de siempre", () => {
    expect(pie).toContain('padding: "32px 24px", display: "flex", alignItems: "center", gap: "24px", flexWrap: "wrap"');
    expect(pie).not.toContain("flexDirection");
    expect(pie.match(/<nav\b/g)).toBeNull();
  });

  it("los cinco enlaces legales en la misma fila, con el gris y el tamaño de la navegación", () => {
    for (const href of LEGALES) {
      expect(pie, href).toMatch(new RegExp(`<a href="${href}" style=\\{\\{ color: "#A6A7AD" \\}\\} className="lh5">`));
    }
  });

  it("sin la tarjeta ni los colores añadidos", () => {
    expect(landing).not.toContain("COLOR_LEGAL");
    expect(landing).not.toContain("preguntasDesc");
  });
});

describe("las páginas públicas (legales y de ayuda) se leen", () => {
  const html = renderToStaticMarkup(
    <IdiomaProvider idioma="es">
      <PaginaPublica idioma="es">
        <h1>Privacidad</h1>
      </PaginaPublica>
    </IdiomaProvider>,
  );
  const clasesDe = (re: RegExp) => (html.match(re)?.[0].match(/class="([^"]*)"/)?.[1] ?? "").split(/\s+/);

  it("el texto usa la tinta del tema, no un --ink inexistente que caía en negro sobre negro", () => {
    expect(html).not.toContain("--ink");
    expect(clasesDe(/<main[^>]*>/)).toEqual(expect.arrayContaining(["text-ink", "bg-bg"]));
  });

  it("la barra de enlaces es la original: una fila con los cinco, en el mismo orden", () => {
    const nav = html.match(/<nav[\s\S]*?<\/nav>/)?.[0] ?? "";
    expect(nav).toContain("gap:16px");
    const orden = ["/privacidad", "/terminos", "/cookies", "/eliminar-cuenta", "/preguntas-frecuentes"].map((h) => nav.indexOf(`href="${h}"`));
    expect(orden.every((i, k) => i >= 0 && (k === 0 || orden[k - 1] < i))).toBe(true);
    expect(nav).toContain(navPublica("es").preguntas);
  });
});

describe("Preguntas frecuentes: la pregunta en azul, la respuesta en blanco", () => {
  const pagina = readFileSync(path.join(__dirname, "..", "preguntas-frecuentes", "page.tsx"), "utf8");
  it("summary en text-accent y la respuesta en text-ink", () => {
    expect(pagina).toMatch(/<summary[^>]*className="[^"]*\btext-accent\b/);
    expect(pagina).toMatch(/<p className="[^"]*\btext-ink\b[^"]*">\{it\.r\}<\/p>/);
  });
});
