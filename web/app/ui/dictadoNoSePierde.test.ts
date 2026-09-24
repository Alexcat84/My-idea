// AUD-09 B14b: contrato de CampoConVoz. El campo muestra el valor (con lo
// provisional ya adentro) y detener el micrófono no descarta lo que se oyó.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const src = readFileSync(path.join(__dirname, "CampoConVoz.tsx"), "utf8");

describe("el dictado provisional no se pierde (AUD-09 B14b)", () => {
  it("usa fusionarDictado y el campo muestra el valor tal cual", () => {
    expect(src).toMatch(/fusionarDictado\(/);
    expect(src).toMatch(/value=\{valor\}/);
  });
  it("detener el micrófono no borra lo provisional", () => {
    const fn = src.match(/function alternarMicrofono\(\)[\s\S]*?\r?\n  \}\r?\n/)?.[0] ?? "";
    expect(fn).not.toMatch(/setProvisional\(""\)/);
  });
});
