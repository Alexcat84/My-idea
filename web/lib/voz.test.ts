// Phase 3.7 (regla A): el filtro mecánico anti-guiones es la garantía de
// que ningún texto del modelo llega al usuario con — o – aunque el prompt
// sea desobedecido (el caso real: preguntas del caché v1.3 y planes con
// incisos entre guiones largos).
import { describe, expect, it } from "vitest";
import { limpiarGuiones } from "./voz";

describe("limpiarGuiones (la casa no escribe con guiones largos ni medios)", () => {
  it("inciso entre pares de guiones -> entre comas", () => {
    expect(limpiarGuiones("un gasto importante —como contratar a alguien— antes de pagarlo")).toBe(
      "un gasto importante, como contratar a alguien, antes de pagarlo"
    );
  });

  it("guion suelto -> coma", () => {
    expect(limpiarGuiones("eso cambia todo — calcula tu margen")).toBe("eso cambia todo, calcula tu margen");
    expect(limpiarGuiones("eso cambia todo – calcula tu margen")).toBe("eso cambia todo, calcula tu margen");
  });

  it("rango numérico -> guion corto", () => {
    expect(limpiarGuiones("entre 3–5 clientes")).toBe("entre 3-5 clientes");
  });

  it("viñeta con guion largo al inicio de línea -> viñeta normal", () => {
    expect(limpiarGuiones("— primer paso\n— segundo paso")).toBe("- primer paso\n- segundo paso");
  });

  it("no deja coma huérfana antes de puntuación", () => {
    expect(limpiarGuiones("tu margen —el real—. Y sigue.")).toBe("tu margen, el real. Y sigue.");
  });

  it("texto limpio pasa intacto (misma referencia)", () => {
    const limpio = "Sin guiones raros: comas, dos puntos (y paréntesis).";
    expect(limpiarGuiones(limpio)).toBe(limpio);
  });

  it("no toca guiones cortos legítimos", () => {
    expect(limpiarGuiones("problem-solution fit y e-commerce")).toBe("problem-solution fit y e-commerce");
  });
});
