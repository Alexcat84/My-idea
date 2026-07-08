// Fase 3.0: paridad numerica exacta contra engine/test_calculadora.py.
// Los mismos valores calculados A MANO (regla de AGENTS.md), no derivados
// de correr esta implementacion -- si algo diverge de la version Python,
// el bug esta aqui, no en el calculo manual.
import { describe, expect, it } from "vitest";
import {
  calcularReporte,
  costoUnitarioTotal,
  detectarInconsistenciaGigo,
  escenariosAdopcion,
  escenariosCapacidad,
  margenUnitario,
  puntoEquilibrioUnidadesMes,
  techoIngresoCapacidad,
  type NumerosProyecto,
} from "./calculadora";

function numeros(campos: Record<string, number | { min: number; max: number }>): NumerosProyecto {
  const out: NumerosProyecto = {};
  for (const [campo, valor] of Object.entries(campos)) {
    out[campo] = { valor, unidad: null, texto_original: "" };
  }
  return out;
}

describe("escenario macetas (calcita/resina) -- mismo caso que test_escenario_macetas", () => {
  // Calculo manual (identico al de engine/test_calculadora.py):
  //   costo_unitario = 8 (materiales) + 4h x $15/h = 8 + 60           = 68
  //   margen         = precio 85 - costo 68                          = 17
  //   margen_pct     = 17 / 85 x 100                                  = 20.0
  //   unidades_mes   = capacidad 5/semana x 4 semanas/mes             = 20
  //   ingreso_mes    = 20 unidades x $85                              = 1700
  //   margen_mes     = 20 unidades x $17                              = 340
  //   pesimista (50%) = 10 unidades -> ingreso 850, margen 170
  //   base (100%)     = 20 unidades -> ingreso 1700, margen 340
  //   sobredemanda: demanda 30, no_atendidas 10, ingreso_perdido 850, margen_perdido 170
  const n = numeros({
    costo_materiales_unidad: 8,
    horas_por_unidad: 4,
    valor_hora: 15,
    precio_tentativo: 85,
    capacidad_semanal: 5,
  });

  it("costo unitario = 68", () => {
    expect(costoUnitarioTotal(n).valor).toBe(68);
  });

  it("margen = 17 (20%)", () => {
    const margen = margenUnitario(n);
    expect(margen.valor).toBe(17);
    expect(margen.porcentaje).toBe(20.0);
  });

  it("techo de capacidad: 20 unidades/mes, $1700 ingreso, $340 margen", () => {
    const capacidad = techoIngresoCapacidad(n);
    expect(capacidad.unidades_mes).toBe(20);
    expect(capacidad.ingreso).toBe(1700);
    expect(capacidad.margen_mensual).toBe(340);
  });

  it("escenarios: pesimista/base/sobredemanda con ingreso_perdido != margen_perdido (850 vs 170)", () => {
    const escenarios = escenariosCapacidad(n);
    expect(escenarios.pesimista).toEqual({ unidades_mes: 10, ingreso: 850, margen_mensual: 170 });
    expect(escenarios.base).toEqual({ unidades_mes: 20, ingreso: 1700, margen_mensual: 340 });
    const sd = escenarios.sobredemanda!;
    expect(sd.demanda_estimada).toBe(30);
    expect(sd.unidades_no_atendidas).toBe(10);
    expect(sd.ingreso_perdido_estimado).toBe(850);
    expect(sd.margen_perdido_estimado).toBe(170);
    // Guardrail del hotfix v2.1.1: nunca deben coincidir por error de formula.
    expect(sd.ingreso_perdido_estimado).not.toBe(sd.margen_perdido_estimado);
  });
});

describe("caso real del fundador (app de I Ching, digital) -- mismo caso que test_digital_founder_caso_real", () => {
  // Calculo manual (numeros YA corregidos a su unidad real):
  //   costo_unitario (rama digital) = 0 (variable declarado)          = 0
  //   margen          = precio 13 - costo 0                           = 13
  //   margen_pct      = 13 / 13 x 100                                  = 100.0
  //   punto_equilibrio = ceil(200 / 13) = ceil(15.3846...)            = 16 (packs/mes)
  //   escenarios (meta 20): 50%->10 (ingreso 130, margen 130),
  //                         100%->20 (ingreso 260, margen 260),
  //                         200%->40 (ingreso 520, margen 520)
  const n = numeros({
    costos_fijos_mensuales: 200,
    costo_materiales_unidad: 0,
    precio_tentativo: 13,
    unidades_vendidas: 20,
  });

  it("costo unitario digital = 0, sin pedir horas/valor_hora", () => {
    const costo = costoUnitarioTotal(n, "digital");
    expect(costo.valor).toBe(0);
    expect(costo.insumos_faltantes).toEqual([]);
  });

  it("margen = 13 (100%)", () => {
    const margen = margenUnitario(n, "digital");
    expect(margen.valor).toBe(13);
    expect(margen.porcentaje).toBe(100.0);
  });

  it("punto de equilibrio = 16 packs/mes (redondeado hacia arriba, no 15.4)", () => {
    const equilibrio = puntoEquilibrioUnidadesMes(n, "digital");
    expect(equilibrio.valor).toBe(16);
  });

  it("escenarios de adopcion 50/100/200% correctos", () => {
    const escenarios = escenariosAdopcion(n, "digital");
    expect(escenarios["50%"]).toEqual({ unidades: 10, ingreso: 130, margen_total: 130 });
    expect(escenarios["100%"]).toEqual({ unidades: 20, ingreso: 260, margen_total: 260 });
    expect(escenarios["200%"]).toEqual({ unidades: 40, ingreso: 520, margen_total: 520 });
  });

  it("guardian GIGO no marca inconsistente (numeros sanos)", () => {
    expect(detectarInconsistenciaGigo(n, "digital").inconsistente).toBe(false);
  });
});

describe("caso SaaS sintetico -- mismo caso que test_digital_saas_sintetico", () => {
  // Calculo manual:
  //   costo_unitario = 0.50 (variable, rama digital)                  = 0.50
  //   margen         = precio 5 - costo 0.50                          = 4.50
  //   margen_pct     = 4.50 / 5 x 100                                  = 90.0
  //   punto_equilibrio = ceil(200 / 4.50) = ceil(44.444...)           = 45 (usuarios/mes)
  //   escenarios (meta 100): 50%->50 (ingreso 250, margen 225),
  //                          100%->100 (ingreso 500, margen 450),
  //                          200%->200 (ingreso 1000, margen 900)
  const n = numeros({
    costos_fijos_mensuales: 200,
    costo_materiales_unidad: 0.5,
    precio_tentativo: 5,
    unidades_vendidas: 100,
  });

  it("margen = 4.5 (90%)", () => {
    const margen = margenUnitario(n, "digital");
    expect(margen.valor).toBe(4.5);
    expect(margen.porcentaje).toBe(90.0);
  });

  it("punto de equilibrio = 45 usuarios/mes", () => {
    expect(puntoEquilibrioUnidadesMes(n, "digital").valor).toBe(45);
  });

  it("escenarios de adopcion 50/100/200% correctos", () => {
    const escenarios = escenariosAdopcion(n, "digital");
    expect(escenarios["50%"]).toEqual({ unidades: 50, ingreso: 250, margen_total: 225 });
    expect(escenarios["100%"]).toEqual({ unidades: 100, ingreso: 500, margen_total: 450 });
    expect(escenarios["200%"]).toEqual({ unidades: 200, ingreso: 1000, margen_total: 900 });
  });
});

describe("guardian GIGO -- mismo caso que test_gigo_detecta_unidad_equivocada", () => {
  // Calculo manual (numeros CONTAMINADOS, el bug real del hotfix v2.2):
  //   costo_unitario = materiales 200 + horas 4 x valor_hora 50 = 400
  //   margen         = precio 13 - costo 400                    = -387
  //   margen_pct     = -387 / 13 x 100                           = -2976.923... ~ -2976.9
  const contaminados = numeros({
    costo_materiales_unidad: 200,
    horas_por_unidad: 4,
    valor_hora: 50,
    precio_tentativo: 13,
  });

  it("margen -2976.9% detectado como inconsistente", () => {
    const margen = margenUnitario(contaminados);
    expect(margen.porcentaje).toBe(-2976.9);
    expect(detectarInconsistenciaGigo(contaminados).inconsistente).toBe(true);
  });

  it("escenario sano (macetas) NO dispara falso positivo", () => {
    const sanos = numeros({ costo_materiales_unidad: 8, horas_por_unidad: 4, valor_hora: 15, precio_tentativo: 85 });
    expect(detectarInconsistenciaGigo(sanos).inconsistente).toBe(false);
  });
});

describe("calcularReporte: dispatch por tipoOferta", () => {
  it("digital omite 'capacidad' y usa escenariosAdopcion", () => {
    const n = numeros({ costos_fijos_mensuales: 200, costo_materiales_unidad: 0, precio_tentativo: 13, unidades_vendidas: 20 });
    const reporte = calcularReporte(n, "digital");
    expect(reporte.capacidad.unidades_mes).toBeNull();
    expect("50%" in reporte.escenarios).toBe(true);
  });

  it("producto_fisico/undefined usa capacidad + escenariosCapacidad (retrocompatible)", () => {
    const n = numeros({
      costo_materiales_unidad: 8,
      horas_por_unidad: 4,
      valor_hora: 15,
      precio_tentativo: 85,
      capacidad_semanal: 5,
    });
    const reporte = calcularReporte(n);
    expect(reporte.capacidad.unidades_mes).toBe(20);
    expect("pesimista" in reporte.escenarios).toBe(true);
  });
});
