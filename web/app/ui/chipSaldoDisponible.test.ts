// AUD-09 M31 + decisión del fundador (25 sep 2026): el chip muestra lo
// DISPONIBLE y, con reserva activa, "N reservados para tu sesión en curso"; y
// se vuelve a pedir cuando la idea cambia el saldo (antes se quedaba con el
// número de la carga: tras cobrar un plan seguía mostrando el saldo previo).
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { textoChipSaldo } from "./ChipSaldo";

const idea = readFileSync(path.join(__dirname, "..", "idea", "[id]", "IdeaView.tsx"), "utf8");

describe("el chip del saldo dice lo que se puede gastar (AUD-09 M31)", () => {
  it("lo disponible, en singular y plural", () => {
    expect(textoChipSaldo(15, 0)).toEqual({ principal: "15 créditos", reservados: null });
    expect(textoChipSaldo(1, 0)).toEqual({ principal: "1 crédito", reservados: null });
  });

  it("con reserva activa, lo dice", () => {
    // A MANO: saldo 25 con 10 reservados -> disponible 15.
    expect(textoChipSaldo(15, 10)).toEqual({ principal: "15 créditos", reservados: "10 reservados para tu sesión en curso" });
    expect(textoChipSaldo(4, 1)).toEqual({ principal: "4 créditos", reservados: "1 reservado para tu sesión en curso" });
  });

  it("la idea le avisa al chip cuando el saldo cambia", () => {
    expect(idea).toMatch(/<ChipSaldo version=\{versionSaldo\} \/>/);
    expect(idea).toMatch(/setVersionSaldo\(/);
  });

  // Una sola fuente: /ideas pintaba su propio chip con el saldo entero.
  it("/ideas usa el chip de siempre, no una copia", () => {
    const ideas = readFileSync(path.join(__dirname, "..", "ideas", "page.tsx"), "utf8");
    expect(ideas).toMatch(/<ChipSaldo \/>/);
    expect(ideas).not.toMatch(/\{saldo\} \{saldo === 1 \? "crédito" : "créditos"\}/);
  });

  it("/creditos dice lo disponible en su barra y lo reservado en su héroe", () => {
    const creditos = readFileSync(path.join(__dirname, "..", "creditos", "page.tsx"), "utf8");
    expect(creditos).toMatch(/apartadoDe\(/);
    expect(creditos).toMatch(/textoChipSaldo\(/);
  });
});
