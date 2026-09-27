// AUD-09 M41 (tanda 7A, datos): mover-fecha ahora rechaza lo hecho y lo
// retirado con un 409 que dice qué hacer. Las dos pantallas que lo llaman lo
// cambiaban por un genérico: el rechazo se muestra tal cual (regla de H03).
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

describe("el rechazo de mover-fecha se muestra tal cual (AUD-09 M41)", () => {
  for (const archivo of ["Calendario.tsx", "ManosALaObra.tsx"]) {
    it(archivo, () => {
      const src = readFileSync(path.join(__dirname, archivo), "utf8");
      const tras = src.slice(src.indexOf("/mover-fecha`"));
      const bloque = tras.slice(0, 400);
      expect(bloque).toMatch(/if \(!res\.ok\)[\s\S]*leerRechazo\(res, idioma\)/);
    });
  }
});
