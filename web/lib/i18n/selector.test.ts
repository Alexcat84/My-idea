// i18n F3: el selector de idioma cambia de idioma navegando a la misma página
// con ?lang=xx (D9): proxy.ts lo lee, manda en esa visita y escribe la cookie.
// Casos a mano: se agrega o se reemplaza `lang`, lo demás de la URL queda igual.
import { describe, expect, it } from "vitest";
import { urlConIdioma } from "./selector";

describe("urlConIdioma", () => {
  it("agrega lang a una URL sin parámetros", () => {
    expect(urlConIdioma("https://myidea.app/cuenta", "en")).toBe("https://myidea.app/cuenta?lang=en");
  });
  it("reemplaza un lang anterior y conserva los demás parámetros y el ancla", () => {
    expect(urlConIdioma("https://myidea.app/idea/1?vista=mundo&lang=es#plan", "en")).toBe(
      "https://myidea.app/idea/1?vista=mundo&lang=en#plan"
    );
  });
});

// Decisión del fundador (25 sep 2026): el selector manual, opcional, a la
// derecha de TODA pantalla (el automático por cookie y navegador sigue
// mandando). En cada cabecera; donde no hay cabecera, fijo arriba a la derecha
// desde el layout de esa sección.
import { readFileSync } from "node:fs";
import path from "node:path";

describe("el selector de idioma está en toda pantalla", () => {
  const raiz = path.join(__dirname, "..", "..");
  const conSelector = [
    "app/ui/Landing.tsx",
    "app/ideas/page.tsx",
    "app/creditos/page.tsx",
    "app/cuenta/page.tsx",
    "app/potenciadores/page.tsx",
    "app/idea/[id]/IdeaView.tsx",
    "app/login/layout.tsx",
    "app/nueva/layout.tsx",
    "app/auth/layout.tsx",
  ];
  for (const archivo of conSelector) {
    it(archivo, () => {
      expect(readFileSync(path.join(raiz, archivo), "utf8")).toMatch(/<SelectorIdioma\b[^>]*\bcompacto\b/);
    });
  }
});

// Pedido del fundador (25 sep 2026): el menú nativo del sistema se abría como
// un rectángulo blanco que ignoraba el tema oscuro. El selector pasa a una
// lista propia (botón + listbox), pintada con la paleta de la casa.
import { renderToStaticMarkup } from "react-dom/server";
import { createElement } from "react";
import { moverIndice } from "./selector";
import { SelectorIdioma } from "../../app/ui/SelectorIdioma";

describe("el selector usa una lista propia, no el menú del sistema", () => {
  it("moverIndice recorre la lista en círculo (flechas del teclado)", () => {
    // 11 idiomas: de 0 hacia arriba va al 10; del 10 hacia abajo vuelve al 0.
    expect(moverIndice(0, 1, 11)).toBe(1);
    expect(moverIndice(10, 1, 11)).toBe(0);
    expect(moverIndice(0, -1, 11)).toBe(10);
    expect(moverIndice(5, -1, 11)).toBe(4);
  });
  it("sin <select>: un botón que abre una lista (compacto y de pie)", () => {
    for (const compacto of [true, false]) {
      const html = renderToStaticMarkup(createElement(SelectorIdioma, { compacto }));
      expect(html).not.toContain("<select");
      expect(html).toContain('aria-haspopup="listbox"');
      expect(html).toContain('aria-expanded="false"');
    }
  });
});
