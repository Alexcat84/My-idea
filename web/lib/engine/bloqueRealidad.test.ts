// Fase 4.0 §3 — el BLOQUE DE REALIDAD. Se arma un Analytics a mano (no se
// recalcula nada aquí: el bloque solo REDACTA lo que analytics.ts ya midió) y
// se verifica que diga la verdad, y que en modo "a mi ritmo" NO juzgue contra
// fechas que el usuario eligió no tener.
import { describe, expect, it } from "vitest";
import { construirBloqueRealidad } from "./bloqueRealidad";
import type { Analytics } from "../analytics";

const UNIVERSAL: Analytics["universal"] = {
  duracionTotalDias: 61,
  accionesHechas: 4,
  accionesVigente: { hechas: 3, total: 8 },
  ritmoAccionesPorSemana: 2.1,
  rachaMasLargaDias: 11,
  ciclosDePlan: 2,
  mundos: 1,
  duracionPorEtapa: [
    { etapa: 1, dias: 18 },
    { etapa: 2, dias: 24 },
  ],
  diasSinAvance: 37,
  planVigenteAt: "2026-04-01T12:00:00Z",
  diasDeVidaPlanVigente: 30,
};

const CUMPLIMIENTO: Analytics["cumplimiento"] = {
  aTiempo: 12,
  adelantadas: 5,
  tardias: 2,
  totalConFecha: 19,
  pctATiempo: 63,
  pctAdelantadas: 26,
  pctTardias: 11,
  desviacionMediaDias: 3.4,
  replanificaciones: 1,
  porEtapa: [],
  tardiasTop: [
    { texto: "Prueba 10 entregas con dos empaques", etapa: 2, diasRetraso: 12 },
    { texto: "Fija tu precio con costo real", etapa: 3, diasRetraso: 5 },
  ],
  replanificados: [{ texto: "Habla con 5 cafeterías", etapa: 1 }],
  // Fase 4.1 (V3b): el desglose por dominio existe, pero el bloque del follow
  // core NO lo usa — el follow es core (V4) y su bloque también.
  porDominio: [{ dominio: "core", aTiempo: 12, adelantadas: 5, tardias: 2, total: 19 }],
};

const base = (over: Partial<Analytics> = {}): Analytics => ({
  universal: UNIVERSAL,
  cumplimiento: CUMPLIMIENTO,
  hitos: [],
  modoCamino: "fechas",
  cierreMotivo: null,
  ...over,
});

describe("construirBloqueRealidad — modo fechas", () => {
  const b = construirBloqueRealidad(base())!;

  it("dice el ciclo y la vida del plan vigente", () => {
    expect(b).toContain("Ciclo 2");
    expect(b).toContain("el plan vigente lleva 30 días");
  });

  it("dice el ritmo real, incluidos los dias sin avance", () => {
    expect(b).toContain("3 de 8 acciones hechas en este ciclo");
    expect(b).toContain("2.1 acciones por semana");
    expect(b).toContain("racha más larga de 11 días");
    expect(b).toContain("37 días desde mi último avance");
  });

  it("dice el cumplimiento con su desviación media", () => {
    expect(b).toContain("12 a tiempo, 5 adelantadas, 2 tardías");
    expect(b).toContain("desviación media de +3.4 días");
  });

  it("dice DONDE se atora, con la etapa y los dias", () => {
    expect(b).toContain('"Prueba 10 entregas con dos empaques" (etapa 2, 12 días tarde)');
    expect(b).toContain('"Fija tu precio con costo real" (etapa 3, 5 días tarde)');
  });

  it("dice CUALES movieron su fecha", () => {
    expect(b).toContain("Moví la fecha de 1 acción");
    expect(b).toContain('"Habla con 5 cafeterías" (etapa 1)');
  });
});

describe("construirBloqueRealidad — modo a mi ritmo (§3: jamás juzgar sin fechas)", () => {
  // Caso real: el usuario tuvo baseline y luego PAUSÓ las fechas. El
  // cumplimiento sigue existiendo en analytics, pero el bloque NO debe usarlo.
  const b = construirBloqueRealidad(base({ modoCamino: "ritmo" }))!;

  it("conserva duraciones y ritmo", () => {
    expect(b).toContain("2.1 acciones por semana");
    expect(b).toContain("etapa 1: 18 días");
  });

  it("NO menciona cumplimiento, tardías ni replanificaciones", () => {
    expect(b).not.toContain("a tiempo");
    expect(b).not.toContain("tarde");
    expect(b).not.toContain("desviación");
    expect(b).not.toContain("Moví la fecha");
    expect(b).toContain("Elegí llevar esto a mi ritmo");
  });
});

describe("construirBloqueRealidad — bordes", () => {
  it("sin cumplimiento (nunca hubo baseline) no inventa nada", () => {
    const b = construirBloqueRealidad(base({ cumplimiento: null, modoCamino: "fechas" }))!;
    expect(b).toContain("2.1 acciones por semana");
    expect(b).not.toContain("a tiempo");
  });

  it("sin avances lo dice, en vez de callar", () => {
    const b = construirBloqueRealidad(
      base({ universal: { ...UNIVERSAL, diasSinAvance: null, accionesHechas: 0 } })
    )!;
    expect(b).toContain("aún sin ningún avance registrado");
  });

  it("proyecto recién nacido sin plan ni avances: null (nada que contar)", () => {
    const vacio = base({
      universal: { ...UNIVERSAL, accionesHechas: 0, planVigenteAt: null, diasSinAvance: null },
      cumplimiento: null,
    });
    expect(construirBloqueRealidad(vacio)).toBeNull();
  });
});
