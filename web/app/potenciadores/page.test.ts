// UNA SOLA FUENTE DE VERDAD para las tarjetas de potenciadores (decisión del
// fundador, ago 2026, no discutible). Esta página tuvo su propia copia de la
// parrilla y se quedó DOS campañas atrás sin que nadie lo notara, mintiendo el
// catálogo en vivo. La regla ahora: la parrilla vive SOLO en PotenciaTuIdea
// (dentro de la idea) y /potenciadores REDIRIGE hacia ella. Este contrato lee
// el fuente y falla si a la página le vuelve a crecer una parrilla propia.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const pagina = readFileSync(path.join(__dirname, "page.tsx"), "utf-8");
const fila = readFileSync(path.join(__dirname, "..", "ui", "PotenciaTuIdea.tsx"), "utf-8");

describe("contrato: /potenciadores redirige, no duplica", () => {
  it("con idea elegida, la página REDIRIGE a la fuente de verdad (vista=manos)", () => {
    expect(pagina).toContain("redirect(`/idea/${ideaId}?vista=manos`)");
  });

  it("la página NO tiene parrilla propia: ni catálogo, ni precios, ni promesas de mundos", () => {
    expect(pagina).not.toContain("packs_catalog");
    expect(pagina).not.toContain("PRECIOS");
    expect(pagina).not.toContain("MUNDOS");
    expect(pagina).not.toContain("promesa");
    expect(pagina).not.toContain("créditos");
    expect(pagina).not.toContain("diagnóstico");
    expect(pagina).not.toContain("Tus Números");
  });

  it("el lenguaje muerto no vuelve a NINGUNA de las dos superficies", () => {
    for (const fuente of [pagina, fila]) {
      expect(fuente).not.toContain("Explóralo gratis");
      expect(fuente).not.toContain("Exploralo gratis");
      expect(fuente).not.toContain("Se paga por uso");
    }
  });

  it("la fuente única (PotenciaTuIdea) conserva el catálogo vigente", () => {
    expect(fila).toContain("PRECIOS.mundo_activar");
    expect(fila).toContain("diagnóstico gratis");
    expect(fila).toContain("Incluido con tu plan");
  });
});
