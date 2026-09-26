// Campaña "Espacios" — la cara "Tu avance": los hitos ESTRUCTURALES por espacio
// (calco del timeline de La Celebración). Lo más importante, no cada acción.
import { describe, expect, it } from "vitest";
import { hitosDeEspacio } from "./hitosEspacio";

describe("hitosDeEspacio: el core cuenta su historia (La Chispa → Claridad → Tu Plan → cierre)", () => {
  const base = hitosDeEspacio({
    espacio: "core",
    chispaAt: "2026-01-01T00:00:00Z",
    claridadAt: "2026-01-01T00:05:00Z",
    planAt: "2026-01-02T00:00:00Z",
    realizadaAt: null,
  });

  it("muestra los hitos estructurales, no acciones sueltas", () => {
    expect(base.map((h) => h.etiqueta)).toEqual(["La Chispa", "Claridad", "Tu Plan", "El cierre"]);
  });
  it("sin realizada, el cierre es pendiente (gris)", () => {
    const cierre = base.at(-1)!;
    expect(cierre.tipo).toBe("cierre");
    expect(cierre.alcanzado).toBe(false);
    expect(cierre.fecha).toBeNull();
  });
  it("con realizada, el cierre es 'Realizada' y alcanzado", () => {
    const cerrado = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", planAt: "2026-01-02T00:00:00Z", realizadaAt: "2026-02-01T00:00:00Z" });
    const cierre = cerrado.at(-1)!;
    expect(cierre.etiqueta).toBe("Realizada");
    expect(cierre.alcanzado).toBe(true);
    expect(cierre.subtitulo).toBe("Aquí nace tu proyecto");
  });
  it("un arranque sin fecha (Claridad null) no se dibuja", () => {
    const sinClaridad = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", claridadAt: null, planAt: "2026-01-02T00:00:00Z", realizadaAt: null });
    expect(sinClaridad.map((h) => h.etiqueta)).toEqual(["La Chispa", "Tu Plan", "El cierre"]);
  });
  it("los arranques traen subtítulo (para el timeline)", () => {
    expect(base[0].subtitulo).toBe("La idea nace");
    expect(base[1].subtitulo).toBe("Tu idea, organizada");
  });
});

describe("hitosDeEspacio: un mundo cuenta desde su diagnóstico", () => {
  const mundo = hitosDeEspacio({
    espacio: "mundo",
    nombre: "Calidad y Confianza",
    diagnosticoAt: "2026-03-01T00:00:00Z",
    planAt: "2026-03-02T00:00:00Z",
    cerradoAt: "2026-03-20T00:00:00Z",
  });
  it("diagnóstico · su plan · cerrado (alcanzado)", () => {
    expect(mundo.map((h) => h.etiqueta)).toEqual(["Tu diagnóstico", "El plan de Calidad y Confianza", "Cerrado"]);
    expect(mundo.at(-1)!.alcanzado).toBe(true);
  });
  it("el core NO trae hitos de mundo (cada espacio, lo suyo)", () => {
    const core = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", planAt: "2026-01-02T00:00:00Z", realizadaAt: null });
    expect(core.some((h) => h.tipo === "diagnostico")).toBe(false);
  });
});

// "TU AVANCE" CONSERVA EL ORDEN CRONOLÓGICO Y MUESTRA LO QUE FALTA (decisión del
// fundador, 26 sep 2026): es un camino, no un registro. Desde el principio se
// ven en gris, después del hito actual, todas las etapas que faltan. Una etapa
// ANTERIOR al hito actual que nunca ocurrió sigue sin dibujarse (no se inventa).
describe("hitosDeEspacio: las etapas que faltan, en gris, después del hito actual", () => {
  it("core recién nacido (solo La Chispa): Claridad, Tu Plan y el cierre van pendientes", () => {
    const h = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", claridadAt: null, planAt: null, realizadaAt: null });
    expect(h.map((x) => x.etiqueta)).toEqual(["La Chispa", "Claridad", "Tu Plan", "El cierre"]);
    expect(h.map((x) => x.alcanzado)).toEqual([true, false, false, false]);
    expect(h.map((x) => x.fecha)).toEqual(["2026-01-01T00:00:00Z", null, null, null]);
  });
  it("core con Claridad: falta Tu Plan y el cierre", () => {
    const h = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", claridadAt: "2026-01-01T00:05:00Z", planAt: null, realizadaAt: null });
    expect(h.map((x) => [x.etiqueta, x.alcanzado])).toEqual([["La Chispa", true], ["Claridad", true], ["Tu Plan", false], ["El cierre", false]]);
  });
  it("mundo recién activado (solo el diagnóstico): su plan y el cierre van pendientes", () => {
    const h = hitosDeEspacio({ espacio: "mundo", nombre: "Calidad y Confianza", diagnosticoAt: "2026-03-01T00:00:00Z", planAt: null, cerradoAt: null });
    expect(h.map((x) => x.alcanzado)).toEqual([true, false, false]);
    expect(h[1].etiqueta).toBe("El plan de Calidad y Confianza");
  });
});
