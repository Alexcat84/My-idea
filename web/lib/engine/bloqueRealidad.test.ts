// Fase 4.0 §3 — el BLOQUE DE REALIDAD. Se arma un Analytics a mano (no se
// recalcula nada aquí: el bloque solo REDACTA lo que analytics.ts ya midió) y
// se verifica que diga la verdad, y que en modo "a mi ritmo" NO juzgue contra
// fechas que el usuario eligió no tener.
import { describe, expect, it } from "vitest";
import { construirBloqueRealidad, construirBloqueRealidadMundo } from "./bloqueRealidad";
import type { Analytics, AnalyticsMundo } from "../analytics";

const UNIVERSAL: Analytics["universal"] = {
  duracionTotalDias: 61,
  accionesHechas: 4,
  accionesVigente: { hechas: 3, total: 8 },
  retiradas: [],
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
  porDominio: [
    {
      dominio: "core",
      aTiempo: 12,
      adelantadas: 5,
      tardias: 2,
      total: 19,
      desviacionMediaDias: 3.4,
      tardiasTop: [],
      replanificados: [],
    },
  ],
};

const base = (over: Partial<Analytics> = {}): Analytics => ({
  universal: UNIVERSAL,
  cumplimiento: CUMPLIMIENTO,
  hitos: [],
  modoCamino: "fechas",
  cierreMotivo: null,
  mundos: [],
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

// ---------------------------------------------------------------------------
// Fase 4.2 — EL BLOQUE DE UN MUNDO. La regla que este bloque existe para
// cumplir: jamás presentarle al motor las tardanzas del core como si fueran del
// mundo. Los números del mundo y los del proyecto son DISTINTOS a propósito en
// estos fixtures: si el bloque se equivoca de dominio, el test lo caza.
// ---------------------------------------------------------------------------
const MUNDO: AnalyticsMundo = {
  dominio: "quality",
  universal: {
    duracionTotalDias: 30,
    accionesHechas: 4,
    accionesVigente: { hechas: 4, total: 9 },
    retiradas: [],
    ritmoAccionesPorSemana: 0.9,
    rachaMasLargaDias: 3,
    ciclosDePlan: 1,
    mundos: 0,
    duracionPorEtapa: [{ etapa: 1, dias: 12 }],
    diasSinAvance: 6,
    planVigenteAt: "2026-04-15T12:00:00Z",
    diasDeVidaPlanVigente: 16,
  },
  cumplimiento: {
    dominio: "quality",
    aTiempo: 2,
    adelantadas: 0,
    tardias: 2,
    total: 4,
    desviacionMediaDias: 5.5,
    tardiasTop: [{ texto: "Escribe tu protocolo de curado", etapa: 1, diasRetraso: 9 }],
    replanificados: [{ texto: "Compra el termómetro", etapa: 2 }],
  },
  completadoAt: null,
  cierreMotivo: null,
};

describe("construirBloqueRealidadMundo — habla del MUNDO, no del proyecto", () => {
  const b = construirBloqueRealidadMundo(MUNDO, base(), "Calidad y Confianza")!;

  it("se presenta con el nombre humano del mundo", () => {
    expect(b).toContain("Mi realidad medida en «Calidad y Confianza»");
  });

  it("lleva el ritmo y el ciclo DEL MUNDO, no los del core", () => {
    expect(b).toContain("Ciclo 1 de este mundo");
    expect(b).toContain("4 de 9 acciones de este mundo hechas en su ciclo");
    expect(b).toContain("0.9 acciones por semana");
    expect(b).toContain("6 días desde mi último avance aquí");
    // Los numeros del core (ciclo 2, 3 de 8, 2.1/semana, 37 dias) solo pueden
    // vivir en la linea de contexto: en la del ritmo del mundo, jamas. Por eso
    // el assert mira ESA linea y no el bloque entero.
    const suRitmo = b.split("\n").find((l) => l.startsWith("- Ritmo en este mundo"))!;
    expect(suRitmo).not.toContain("3 de 8");
    expect(suRitmo).not.toContain("2.1 acciones");
    expect(suRitmo).not.toContain("37 días");
    expect(b.split("\n").find((l) => l.startsWith("- Ciclo"))).not.toContain("Ciclo 2");
  });

  it("lleva el cumplimiento DEL MUNDO contra SUS fechas", () => {
    expect(b).toContain("2 a tiempo, 0 adelantadas, 2 tardías (de 4 con fecha)");
    expect(b).toContain("desviación media de +5.5 días");
    // el del core es 12/5/2 de 19 con +3.4: si aparece, el bloque miente
    expect(b).not.toContain("12 a tiempo");
    expect(b).not.toContain("+3.4");
  });

  it("dice dónde se atora EN EL MUNDO, nunca las tardías del core", () => {
    expect(b).toContain('"Escribe tu protocolo de curado" (etapa 1, 9 días tarde)');
    expect(b).not.toContain("Prueba 10 entregas");
    expect(b).not.toContain("Fija tu precio");
  });

  it("dice cuáles movieron su fecha EN EL MUNDO", () => {
    expect(b).toContain('Moví la fecha de 1 acción de este mundo: "Compra el termómetro"');
    expect(b).not.toContain("Habla con 5 cafeterías");
  });

  it("lleva UNA sola línea del proyecto, y va rotulada como contexto", () => {
    const lineas = b.split("\n").filter((l) => l.includes("Contexto de mi proyecto"));
    expect(lineas).toHaveLength(1);
    expect(lineas[0]).toContain("NO de este mundo");
    expect(lineas[0]).toContain("mi viaje principal va 3 de 8 acciones en su ciclo 2");
  });
});

describe("construirBloqueRealidadMundo — bordes", () => {
  it("en modo a mi ritmo NO juzga el mundo contra fechas", () => {
    const b = construirBloqueRealidadMundo(MUNDO, base({ modoCamino: "ritmo" }), "Calidad y Confianza")!;
    expect(b).toContain("0.9 acciones por semana");
    expect(b).toContain("Elegí llevar esto a mi ritmo");
    expect(b).not.toContain("a tiempo");
    expect(b).not.toContain("tarde");
    expect(b).not.toContain("desviación");
  });

  it("mundo sin fechas propias: ritmo sí, cumplimiento no", () => {
    const sinFechas = { ...MUNDO, cumplimiento: null };
    const b = construirBloqueRealidadMundo(sinFechas, base(), "Calidad y Confianza")!;
    expect(b).toContain("4 de 9 acciones de este mundo");
    expect(b).not.toContain("a tiempo");
  });

  it("mundo recién activado sin plan ni avances: null (nada que contar)", () => {
    const vacio: AnalyticsMundo = {
      ...MUNDO,
      universal: { ...MUNDO.universal, accionesHechas: 0, planVigenteAt: null, diasSinAvance: null },
      cumplimiento: null,
    };
    expect(construirBloqueRealidadMundo(vacio, base(), "Calidad y Confianza")).toBeNull();
  });
});
