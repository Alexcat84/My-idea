// AUD-09 M05 (tanda 5, mezcla núcleo y mundos): la decisión D1 de
// PLAN_TODO_SEPARADO mató las barras cruzadas de "Cumplimiento por mundo" en la
// pantalla (BANCO §7.1: "cero mezcla de medidas"), pero el PDF "Análisis del
// proyecto" del núcleo las seguía imprimiendo.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

describe("el papel del Análisis del núcleo no mezcla medidas de los mundos", () => {
  it("AnalisisPapel no pinta el cumplimiento por mundo", () => {
    const f = readFileSync(path.join(__dirname, "AnalisisPapel.tsx"), "utf8");
    expect(f).not.toMatch(/porDominio/);
  });
  it("la ruta de documentos no se lo manda", () => {
    const f = readFileSync(path.join(__dirname, "..", "api", "project", "[id]", "documentos", "route.ts"), "utf8");
    expect(f).not.toMatch(/porDominio/);
  });
});
