// AUD-09 M40 (tanda 7B, confianza): la pregunta de capacidad arranca en el
// chip por defecto (5 a 10 horas) y la pantalla lo muestra como elegido, pero
// si el usuario no lo tocaba, nada se guardaba: el espacio seguía "sin
// declarar" y el panel después no lo recordaba. Al aceptar las fechas se guarda
// la capacidad que estaba en pantalla.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const manos = readFileSync(path.join(__dirname, "ManosALaObra.tsx"), "utf8");

describe("la capacidad que se ve elegida se guarda (AUD-09 M40)", () => {
  it("aceptar guarda la capacidad por defecto si el espacio no tenía una", () => {
    const fn = manos.match(/function aceptar\(\) \{[\s\S]*?\r?\n  \}\r?\n/)?.[0] ?? "";
    expect(fn).toMatch(/if \(preguntarCapacidad && capacidad == null\) onCapacidad\?\.\(capacidadLocal\);/);
  });
});
