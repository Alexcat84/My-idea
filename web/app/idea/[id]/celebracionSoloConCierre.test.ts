// AUD-09 M09 (tanda 7A, datos): ?vista=celebracion abría la Celebración aunque
// la idea no estuviera cerrada, y su "Reabrir" escribía una reapertura falsa. Al
// revés, una idea realizada con un mundo abierto abría la Celebración al recargar
// el hub del mundo. Contrato de fuente de IdeaView.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const fuente = readFileSync(path.join(__dirname, "IdeaView.tsx"), "utf8");

describe("la Celebración solo existe con el cierre (AUD-09 M09)", () => {
  it("se pinta solo si la idea está realizada", () => {
    expect(fuente).toMatch(/\) : vistaCelebracion && realizadaAt \? \(/);
    expect(fuente).not.toMatch(/\) : vistaCelebracion \? \(/);
  });

  it("al cargar, abre sola solo cuando la URL no pide ninguna vista", () => {
    expect(fuente).toMatch(/if \(d\.idea\.realizada_at && !searchParams\.get\("vista"\)\) setVistaCelebracion\(true\);/);
    expect(fuente).not.toMatch(/if \(d\.idea\.realizada_at && !quiereManos && !quiereAnalisis\)/);
  });
});
