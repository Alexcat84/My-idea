// LA MONEDA SALE DE LOS DATOS QUE DIO LA PERSONA, NUNCA DE LA IA (decision del fundador, corrida final, 8 oct 2026).
// El juez de fidelidad sostuvo una invencion en el plan de Riesgos ff010188: «para ver en pesos cuánto te cuesta un mes
// sin ese canal». La persona solo dio cifras (68, 17, 85, 250, 130, 50), nunca una moneda; y el interprete ya las habia
// guardado como USD (su prompt enseñaba "$8" -> "USD"). Las dos monedas las puso la IA.
import { describe, expect, it } from "vitest";
import { limpiarMonedaNoDicha, monedaDicha } from "./moneda";

describe("monedaDicha: la moneda tal como la dijo la persona", () => {
  it("sin moneda en sus palabras, no hay moneda", () => {
    expect(monedaDicha(["Cada maceta me cuesta como 68 en materiales", "Las vendo en 85 cada una"])).toBeNull();
  });
  it("la nombra con su palabra", () => {
    expect(monedaDicha(["me pagan 300 pesos por pieza"])).toBe("pesos");
    expect(monedaDicha(["cobro 20 dólares la hora"])).toBe("dólares");
    expect(monedaDicha(["son 15 euros"])).toBe("euros");
  });
  it("el signo $ solo es $ (no se traduce a USD ni a pesos)", () => {
    expect(monedaDicha(["me cuesta como $8 en materiales"])).toBe("$");
  });
});

describe("limpiarMonedaNoDicha: ninguna moneda que la persona no dijo", () => {
  it("el caso real: «en pesos» sin que la persona dijera pesos", () => {
    expect(limpiarMonedaNoDicha("para ver en pesos cuánto te cuesta un mes sin ese canal", null).texto).toBe(
      "para ver cuánto te cuesta un mes sin ese canal"
    );
  });
  it("una cifra con moneda inventada queda como cifra", () => {
    expect(limpiarMonedaNoDicha("te quedan 120 dólares por maceta", null).texto).toBe("te quedan 120 por maceta");
    expect(limpiarMonedaNoDicha("unos 200 USD al mes", null).texto).toBe("unos 200 al mes");
  });
  it("si la persona dijo pesos y la IA escribio dolares, sale pesos", () => {
    expect(limpiarMonedaNoDicha("te quedan 120 dólares por maceta", "pesos").texto).toBe("te quedan 120 pesos por maceta");
  });
  it("lo que la persona dijo se respeta", () => {
    const t = "te quedan 120 pesos por maceta";
    expect(limpiarMonedaNoDicha(t, "pesos")).toEqual({ texto: t, cambios: 0 });
  });
  it("no toca palabras que no son moneda", () => {
    const t = "pesas el cemento y lo anotas; el peso de cada maceta importa";
    expect(limpiarMonedaNoDicha(t, null)).toEqual({ texto: t, cambios: 0 });
  });
});

describe("el plan que se entrega no lleva una moneda que la persona no dijo (extremo a extremo)", () => {
  it("finalizarPlan quita «en pesos» si la persona solo dio cifras, y deja la que si dijo", async () => {
    const { cargarFamilies } = await import("../readiness");
    const { cargarGrafo } = await import("./graph");
    const { finalizarPlan, prepararPlan } = await import("./planRedactor");
    const graph = cargarGrafo();
    const families = cargarFamilies();
    const ruta = ["punto_equilibrio_unidades"];
    const prep = prepararPlan(ruta, graph, families, "Hago macetas de cemento", "perfil", null, false, null);
    const raw = "# Tu plan\n\n## Etapa 1: Mide\n\nEscribe cuántas llegan por Instagram, para ver en pesos cuánto te cuesta un mes sin ese canal.\n";
    const sin = finalizarPlan(raw, prep, ruta, families, "Hago macetas de cemento", undefined, {}, "es", ["Las vendo en 85 cada una"]);
    expect(sin.markdown).toContain("para ver cuánto te cuesta un mes sin ese canal");
    expect(sin.markdown).not.toMatch(/pesos/);
    const con = finalizarPlan(raw, prep, ruta, families, "Hago macetas de cemento", undefined, {}, "es", ["Las vendo en 85 pesos cada una"]);
    expect(con.markdown).toContain("para ver en pesos cuánto");
  });
});
