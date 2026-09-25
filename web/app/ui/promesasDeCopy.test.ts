// AUD-09 B03a (tanda 7B, confianza; decisión del fundador 25 sep 2026): tres
// promesas del copy sin respaldo. "Tu teléfono te recuerda cada tarea el día
// antes" (el aviso del calendario salta el MISMO día: TRIGGER:-PT0M) pasa a lo
// que de verdad hace; "Yo te recuerdo" (no hay sistema de recordatorios propio)
// y "El más elegido" (sin dato que lo respalde) se quitan.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const leer = (rel: string) => readFileSync(path.join(__dirname, rel), "utf8");

describe("el copy no promete lo que no pasa (AUD-09 B03a)", () => {
  it("el aviso del calendario es el mismo día, y así se dice", () => {
    // i18n F2: el copy vive en el catálogo del calendario; el componente lo pinta con t.info.
    const s = leer("SuscripcionCalendario.tsx");
    const cat = readFileSync(path.join(__dirname, "..", "..", "lib", "i18n", "mensajes", "calendario.ts"), "utf8");
    expect(s).not.toMatch(/el día\s+antes/);
    expect(cat).not.toMatch(/el día\s+antes/);
    expect(cat).toMatch(/Tu calendario te avisa de cada tarea el mismo día\./);
    expect(s).toMatch(/\{t\.info\}/);
    expect(readFileSync(path.join(__dirname, "..", "..", "lib", "ics.ts"), "utf8")).toMatch(/TRIGGER:-PT0M/);
  });
  it("sin 'Yo te recuerdo'", () => {
    expect(leer("ManosALaObra.tsx")).not.toMatch(/Yo te recuerdo/);
    // i18n F2: los textos de Manos a la Obra viven en su catálogo.
    expect(readFileSync(path.join(__dirname, "..", "..", "lib", "i18n", "mensajes", "manosALaObra.ts"), "utf8")).not.toMatch(
      /Yo te recuerdo/
    );
  });
  it("sin 'El más elegido'", () => {
    expect(readFileSync(path.join(__dirname, "..", "creditos", "page.tsx"), "utf8")).not.toMatch(/El más elegido/);
    // i18n F2: los textos de /creditos (y los nombres de las recargas) viven en sus catálogos.
    for (const cat of ["creditos.ts", "packsRecarga.ts"]) {
      expect(readFileSync(path.join(__dirname, "..", "..", "lib", "i18n", "mensajes", cat), "utf8")).not.toMatch(/El más elegido/);
    }
  });
});
