// AUD-09 M47 (tanda 7B, confianza): /creditos prometía ANTES de pagar que "cada
// mundo se refleja también en la vista completa de tu proyecto", una vista que
// BANCO §7.1 eliminó (cero mezcla de medidas; la única lectura de la idea
// entera es el Expediente). Regla del fundador: el texto no promete lo que
// falta; dice lo que hay.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

import { CREDITOS } from "@/lib/i18n/mensajes/creditos";

const creditos = readFileSync(path.join(__dirname, "..", "creditos", "page.tsx"), "utf8");
// i18n F2: el copy de /creditos vive en su catálogo; la página lo pinta desde ahí.
const catalogo = readFileSync(path.join(__dirname, "..", "..", "lib", "i18n", "mensajes", "creditos.ts"), "utf8");

describe("/creditos no promete una vista que no existe (AUD-09 M47)", () => {
  it("sin 'la vista completa de tu proyecto'", () => {
    for (const fuente of [creditos, catalogo]) {
      expect(fuente).not.toMatch(/vista completa de tu proyecto/);
      expect(fuente).not.toMatch(/el panorama entero/);
    }
  });
  it("dice lo que hay: el Expediente reúne la idea y cada mundo", () => {
    expect(CREDITOS.es.incluyeMundo).toContain(
      "<b>Y queda en tu Expediente:</b> el único documento que reúne tu idea, tu plan y cada mundo, cada uno en su propia sección."
    );
    // y la página pinta esa lista del plan de un mundo
    expect(creditos).toContain("<Incluye items={t.incluyeMundo} />");
  });
});
