// AUD-09 M47 (tanda 7B, confianza): /creditos prometía ANTES de pagar que "cada
// mundo se refleja también en la vista completa de tu proyecto", una vista que
// BANCO §7.1 eliminó (cero mezcla de medidas; la única lectura de la idea
// entera es el Expediente). Regla del fundador: el texto no promete lo que
// falta; dice lo que hay.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const creditos = readFileSync(path.join(__dirname, "..", "creditos", "page.tsx"), "utf8");

describe("/creditos no promete una vista que no existe (AUD-09 M47)", () => {
  it("sin 'la vista completa de tu proyecto'", () => {
    expect(creditos).not.toMatch(/vista completa de tu proyecto/);
    expect(creditos).not.toMatch(/el panorama entero/);
  });
  it("dice lo que hay: el Expediente reúne la idea y cada mundo", () => {
    expect(creditos).toMatch(/\["Y queda en tu Expediente:", "el único documento que reúne tu idea, tu plan y cada mundo, cada uno en su propia sección\."\]/);
  });
});
