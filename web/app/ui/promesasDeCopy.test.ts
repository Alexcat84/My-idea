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
    const s = leer("SuscripcionCalendario.tsx");
    expect(s).not.toMatch(/el día\s+antes/);
    expect(s).toMatch(/Tu calendario te avisa de cada tarea el mismo día\./);
    expect(readFileSync(path.join(__dirname, "..", "..", "lib", "ics.ts"), "utf8")).toMatch(/TRIGGER:-PT0M/);
  });
  it("sin 'Yo te recuerdo'", () => {
    expect(leer("ManosALaObra.tsx")).not.toMatch(/Yo te recuerdo/);
  });
  it("sin 'El más elegido'", () => {
    expect(readFileSync(path.join(__dirname, "..", "creditos", "page.tsx"), "utf8")).not.toMatch(/El más elegido/);
  });
});
