// La cara "Tu avance": los hitos de cada espacio, en orden cronológico (es un
// camino, no un registro). Decisión del fundador (26 sep 2026): en la IDEA se
// ven las SEIS etapas del recorrido (La Chispa, Claridad, La Exploración, Tu
// Plan, Manos a la Obra y Realizado): las alcanzadas con color, la actual con su
// punto animado y las que faltan en gris desde el principio. La etapa actual es
// la de la regla única (lib/etapaIdea.ts), la misma del paso a paso. En los
// MUNDOS se quedan sus hitos propios (diagnóstico, plan y cierre).
import { describe, expect, it } from "vitest";
import { hitosDeEspacio } from "./hitosEspacio";

const SEIS = ["La Chispa", "Claridad", "La Exploración", "Tu Plan", "Manos a la Obra", "Realizado"];
const D = {
  chispa: "2026-01-01T00:00:00Z",
  claridad: "2026-01-01T00:05:00Z",
  exploracion: "2026-01-02T00:00:00Z",
  plan: "2026-01-03T00:00:00Z",
  manos: "2026-01-10T00:00:00Z",
  realizada: "2026-02-01T00:00:00Z",
};

describe("la idea muestra las seis etapas del recorrido", () => {
  it("en obra, sin tareas hechas: cinco alcanzadas (Manos sin fecha, no se inventa) y Realizado en gris", () => {
    const h = hitosDeEspacio({ espacio: "core", etapa: 5, chispaAt: D.chispa, claridadAt: D.claridad, exploracionAt: D.exploracion, planAt: D.plan, manosAt: null, realizadaAt: null });
    expect(h.map((x) => x.etiqueta)).toEqual(SEIS);
    expect(h.map((x) => x.alcanzado)).toEqual([true, true, true, true, true, false]);
    expect(h.map((x) => x.fecha)).toEqual([D.chispa, D.claridad, D.exploracion, D.plan, null, null]);
  });

  it("con plan pero sin empezar la obra (etapa 4): Manos y Realizado en gris", () => {
    const h = hitosDeEspacio({ espacio: "core", etapa: 4, chispaAt: D.chispa, claridadAt: D.claridad, exploracionAt: D.exploracion, planAt: D.plan, manosAt: null, realizadaAt: null });
    expect(h.map((x) => x.alcanzado)).toEqual([true, true, true, true, false, false]);
  });

  it("recién nacida (etapa 1): solo La Chispa con color, las otras cinco en gris y sin fecha", () => {
    const h = hitosDeEspacio({ espacio: "core", etapa: 1, chispaAt: D.chispa, claridadAt: null, exploracionAt: null, planAt: null, manosAt: null, realizadaAt: null });
    expect(h.map((x) => x.alcanzado)).toEqual([true, false, false, false, false, false]);
    expect(h.filter((x) => !x.alcanzado).every((x) => x.fecha === null)).toBe(true);
  });

  it("una etapa pendiente no muestra fecha aunque el dato exista (lo que falta es lo que falta)", () => {
    const h = hitosDeEspacio({ espacio: "core", etapa: 4, chispaAt: D.chispa, claridadAt: D.claridad, exploracionAt: D.exploracion, planAt: D.plan, manosAt: D.manos, realizadaAt: null });
    expect(h[4]).toMatchObject({ etiqueta: "Manos a la Obra", alcanzado: false, fecha: null });
  });

  it("realizada: las seis alcanzadas; Realizado es el cierre, con su fecha", () => {
    const h = hitosDeEspacio({ espacio: "core", etapa: 5, chispaAt: D.chispa, claridadAt: D.claridad, exploracionAt: D.exploracion, planAt: D.plan, manosAt: D.manos, realizadaAt: D.realizada });
    expect(h.map((x) => x.alcanzado)).toEqual([true, true, true, true, true, true]);
    expect(h.at(-1)).toMatchObject({ tipo: "cierre", etiqueta: "Realizado", fecha: D.realizada, subtitulo: "Aquí nace tu proyecto" });
  });

  it("las etapas llevan su subtítulo; el cierre pendiente dice 'Cuando lo sientas real'", () => {
    const h = hitosDeEspacio({ espacio: "core", etapa: 3, chispaAt: D.chispa, claridadAt: D.claridad, exploracionAt: D.exploracion, planAt: null, manosAt: null, realizadaAt: null });
    expect(h.map((x) => x.subtitulo)).toEqual([
      "La idea nace",
      "Tu idea, organizada",
      "Tu idea, puesta a prueba",
      "Tu plan de acción, listo",
      "Tu plan, en marcha",
      "Cuando lo sientas real",
    ]);
  });

  it("en inglés, los nombres del glosario (los mismos del paso a paso)", () => {
    const h = hitosDeEspacio({ espacio: "core", etapa: 2, chispaAt: D.chispa, claridadAt: D.claridad, exploracionAt: null, planAt: null, manosAt: null, realizadaAt: null }, "en");
    expect(h.map((x) => x.etiqueta)).toEqual(["The Spark", "Clarity", "Exploration", "Your Plan", "Get to Work", "Achieved"]);
  });
});

describe("un mundo cuenta desde su diagnóstico (sus hitos propios)", () => {
  it("diagnóstico · su plan · cerrado (alcanzado)", () => {
    const mundo = hitosDeEspacio({ espacio: "mundo", nombre: "Calidad y Confianza", diagnosticoAt: "2026-03-01T00:00:00Z", planAt: "2026-03-02T00:00:00Z", cerradoAt: "2026-03-20T00:00:00Z" });
    expect(mundo.map((h) => h.etiqueta)).toEqual(["Tu diagnóstico", "El plan de Calidad y Confianza", "Cerrado"]);
    expect(mundo.at(-1)!.alcanzado).toBe(true);
  });
  it("recién activado (solo el diagnóstico): su plan y el cierre van pendientes", () => {
    const h = hitosDeEspacio({ espacio: "mundo", nombre: "Calidad y Confianza", diagnosticoAt: "2026-03-01T00:00:00Z", planAt: null, cerradoAt: null });
    expect(h.map((x) => x.alcanzado)).toEqual([true, false, false]);
    expect(h[1].etiqueta).toBe("El plan de Calidad y Confianza");
  });
  it("el core NO trae hitos de mundo (cada espacio, lo suyo)", () => {
    const core = hitosDeEspacio({ espacio: "core", etapa: 4, chispaAt: D.chispa, claridadAt: null, exploracionAt: null, planAt: D.plan, manosAt: null, realizadaAt: null });
    expect(core.some((h) => h.tipo === "diagnostico")).toBe(false);
  });
});
