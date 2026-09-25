// i18n F2: el auditor corre sobre TODOS los catálogos de lib/i18n/mensajes y
// falla la suite (y el guardián de commit) ante cualquier catálogo roto. Más
// sus propias pruebas con catálogos de juguete, para que no apruebe en falso.
import { readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { describe, expect, it } from "vitest";
import { auditarCatalogo, pareceCatalogo } from "./auditor";

const DIR = path.join(__dirname, "mensajes");

function archivos(dir: string): string[] {
  return readdirSync(dir).flatMap((n) => {
    const p = path.join(dir, n);
    return statSync(p).isDirectory() ? archivos(p) : p.endsWith(".ts") && !p.endsWith(".test.ts") ? [p] : [];
  });
}

describe("el auditor de idiomas", () => {
  it("todos los catálogos pasan", async () => {
    const fallas: string[] = [];
    let catalogos = 0;
    for (const archivo of archivos(DIR)) {
      const mod = (await import(pathToFileURL(archivo).href)) as Record<string, unknown>;
      for (const [nombre, valor] of Object.entries(mod)) {
        if (!pareceCatalogo(valor)) continue;
        catalogos++;
        fallas.push(...auditarCatalogo(`${path.relative(DIR, archivo)}:${nombre}`, valor));
      }
    }
    expect(catalogos).toBeGreaterThan(0);
    expect(fallas).toEqual([]);
  });

  it("ningún archivo usa Partial<Record<Locale (el catálogo incompleto se prohíbe)", () => {
    const raiz = path.join(__dirname, "..", "..");
    const fuentes = [...archivos(path.join(raiz, "lib")), ...archivos(path.join(raiz, "app"))];
    const culpables = fuentes.filter((f) => !f.endsWith("auditor.test.ts") && /Partial<\s*Record<\s*(Active)?Locale/.test(readFileSync(f, "utf8")));
    expect(culpables).toEqual([]);
  });

  it("detecta las fallas (no aprueba en falso)", () => {
    expect(auditarCatalogo("ok", { es: { a: "Hola {{n}}", b: ["x"], c: { d: "<b>sí</b>" } } })).toEqual([]);
    expect(auditarCatalogo("vacio", { es: { a: " " } })).toEqual(["vacio.a [es]: cadena vacía"]);
    expect(auditarCatalogo("sinBase", { en: { a: "x" } })).toContain("sinBase: falta el idioma base (es)");
    expect(auditarCatalogo("numero", { es: { a: 3 } })).toEqual(["numero.a [es]: tipo no admitido en un catálogo (number)"]);
  });
});
