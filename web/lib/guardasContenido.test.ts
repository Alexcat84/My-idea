/**
 * Las guardas de contenido como datos con versión (auditoría final, punto 4, 28 sep 2026): el fichero que copia la
 * forja no puede divergir del código que aplica las guardas. Una sola fuente: el código; el fichero se regenera.
 */
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { guardasContenido, leerGlosario, VERSION_GUARDAS } from "./guardasContenido";
import { REGLAS_VOZ } from "./i18n/frasesProhibidas";

const RAIZ = path.resolve(__dirname, "..", "..");
const FICHERO = path.join(RAIZ, "dataset", "metadata", "guardas_contenido.json");

describe("las guardas de contenido en datos, para la forja", () => {
  it("el fichero existe y coincide con el código (si no, npx tsx scripts/exportar_guardas.ts)", () => {
    expect(existsSync(FICHERO)).toBe(true);
    expect(JSON.parse(readFileSync(FICHERO, "utf8"))).toEqual(JSON.parse(JSON.stringify(guardasContenido(RAIZ))));
  });

  it("lleva versión y todas las reglas de voz, con sus patrones compilables", () => {
    const g = guardasContenido(RAIZ);
    expect(g.version).toBe(VERSION_GUARDAS);
    expect(g.voz.map((r) => r.id)).toEqual(REGLAS_VOZ.map((r) => r.id));
    for (const r of g.voz) {
      for (const lista of Object.values(r.porIdioma)) {
        for (const { patron, flags } of lista) expect(() => new RegExp(patron, flags)).not.toThrow();
      }
    }
  });

  it("el glosario sale entero de su tabla: la fila de 'coger' y la de 'banderas rojas' están", () => {
    const g = leerGlosario(RAIZ);
    expect(g.length).toBeGreaterThanOrEqual(20);
    expect(g.some((f) => f.aparece.includes('"coger"'))).toBe(true);
    expect(g.some((f) => f.aparece.includes('"banderas rojas"'))).toBe(true);
  });
});
