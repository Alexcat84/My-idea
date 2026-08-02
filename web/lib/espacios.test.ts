// Campaña "Espacios" — la regla de pertenencia por espacio (fuente única que
// comparten ManosALaObra e IdeaView). Casos a mano: un proyecto core + 2 mundos.
import { describe, expect, it } from "vitest";
import { ESPACIO_CORE, esEspacioCore, mundosDelEspacio, urlDelEspacio } from "./espacios";

const MUNDOS = [{ dominio: "quality" }, { dominio: "risk_management" }];

describe("esEspacioCore: la frontera core / mundo", () => {
  it("null, undefined y 'core' son el core", () => {
    expect(esEspacioCore(null)).toBe(true);
    expect(esEspacioCore(undefined)).toBe(true);
    expect(esEspacioCore(ESPACIO_CORE)).toBe(true);
  });
  it("cualquier otro dominio es un mundo", () => {
    expect(esEspacioCore("quality")).toBe(false);
    expect(esEspacioCore("risk_management")).toBe(false);
  });
});

describe("mundosDelEspacio: qué mundos muestra cada espacio", () => {
  it("sin soloDominio → TODOS (histórico: apilados bajo el core)", () => {
    expect(mundosDelEspacio(MUNDOS)).toEqual(MUNDOS);
    expect(mundosDelEspacio(MUNDOS, null)).toEqual(MUNDOS);
  });
  it("'core' → NINGUNO (los mundos viven en su hub)", () => {
    expect(mundosDelEspacio(MUNDOS, ESPACIO_CORE)).toEqual([]);
  });
  it("un dominio de mundo → SOLO ese (su hub)", () => {
    expect(mundosDelEspacio(MUNDOS, "quality")).toEqual([{ dominio: "quality" }]);
    expect(mundosDelEspacio(MUNDOS, "risk_management")).toEqual([{ dominio: "risk_management" }]);
  });
  it("un dominio que no está activado → vacío (nunca inventa)", () => {
    expect(mundosDelEspacio(MUNDOS, "hseq")).toEqual([]);
  });
  it("partición exacta: core + cada hub = cada mundo una sola vez, sin apilar", () => {
    // La suma de las vistas por espacio (core + los dos hubs) cubre los dos
    // mundos exactamente una vez, y el core no muestra ninguno.
    const desdeCore = mundosDelEspacio(MUNDOS, ESPACIO_CORE);
    const porHub = MUNDOS.flatMap((m) => mundosDelEspacio(MUNDOS, m.dominio));
    expect(desdeCore.length + porHub.length).toBe(MUNDOS.length);
    expect(porHub).toEqual(MUNDOS);
  });
});

describe("urlDelEspacio: el deep-link con dominio", () => {
  it("el core lleva a ?vista=manos", () => {
    expect(urlDelEspacio("p1", ESPACIO_CORE)).toBe("/idea/p1?vista=manos");
  });
  it("un mundo lleva a su hub con el dominio, JAMÁS a ?vista=manos", () => {
    expect(urlDelEspacio("p1", "quality")).toBe("/idea/p1?vista=mundo&dominio=quality");
    expect(urlDelEspacio("p1", "risk_management")).toBe("/idea/p1?vista=mundo&dominio=risk_management");
  });
});
