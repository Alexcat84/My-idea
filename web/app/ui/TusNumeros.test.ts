// AUD-09 H12: la frase de la palanca de volumen podía decir "A null …",
// "unidads" y "— de ganancia". Una cifra que no existe no se escribe.
import { describe, expect, it } from "vitest";
import { textoPalanca } from "./TusNumeros";
import type { Palanca } from "@/lib/palancas";

const volumen = (meta: number | null, ganancia: number | null) =>
  ({ clave: "volumen", modo: "sano", bloqueada: false, meta, actual: null, gananciaResultante: ganancia, recomendada: true }) as unknown as Palanca;

describe("textoPalanca (volumen)", () => {
  it("el plural de la unidad es español: unidad -> unidades, pieza -> piezas", () => {
    expect(textoPalanca(volumen(44, 6300), "unidad")).toContain("44 unidades al mes");
    expect(textoPalanca(volumen(44, 6300), "pieza")).toContain("44 piezas al mes");
  });
  it("sin capacidad declarada no escribe 'null'", () => {
    const t = textoPalanca(volumen(null, null), "unidad");
    expect(t).not.toMatch(/null/);
    expect(t).toMatch(/por semana/);
  });
  it("sin gastos fijos no escribe '— de ganancia'", () => {
    const t = textoPalanca(volumen(44, null), "unidad");
    expect(t).not.toContain("—");
    expect(t).toContain("44 unidades al mes");
  });
});
