// Fase 3.0: paridad numerica exacta contra engine/test_calculadora.py.
// Los mismos valores calculados A MANO (regla de AGENTS.md), no derivados
// de correr esta implementacion -- si algo diverge de la version Python,
// el bug esta aqui, no en el calculo manual.
import { describe, expect, it } from "vitest";
import {
  calcularReporte,
  costoMaximoParaMargenObjetivo,
  costoUnitarioTotal,
  detectarInconsistenciaGigo,
  escenariosAdopcion,
  escenariosCapacidad,
  margenConCosto,
  margenConPrecio,
  margenUnitario,
  precioParaMargenObjetivo,
  puntoEquilibrioUnidadesMes,
  techoIngresoCapacidad,
  unidadesParaGananciaObjetivo,
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

describe("palancas inversas (canon 14) -- paridad con test_palancas_inversas de Python", () => {
  // Caso PERDIDA (velas de soya del canon 14): costo total $42, precio $38.
  //   costo_unitario = 30 (materiales) + 2h x $6/h = 30 + 12               = 42
  //   margen         = 38 - 42                                             = -4  (-10.5%)
  //   precioParaMargenObjetivo(0.25) = 42 / (1 - 0.25) = 42 / 0.75         = 56.0
  //   margenConPrecio(56)            = 56 - 42 = 14 ; 14/56 x 100          = 25.0%
  //   costoMaximoParaMargenObjetivo(0.25) = 38 x (1 - 0.25) = 38 x 0.75    = 28.5
  //   margenConCosto(28.5)           = 38 - 28.5 = 9.5 ; 9.5/38 x 100      = 25.0%
  //   unidadesParaGananciaObjetivo(0): margen -4 <= 0 -> null + nota (no hay equilibrio)
  const velas = numeros({ costo_materiales_unidad: 30, horas_por_unidad: 2, valor_hora: 6, precio_tentativo: 38, costos_fijos_mensuales: 200 });

  it("PERDIDA: margen base es -$4 (-10.5%)", () => {
    const m = margenUnitario(velas);
    expect(m.valor).toBe(-4);
    expect(m.porcentaje).toBe(-10.5);
  });

  it("PERDIDA: subir el precio a $56 lleva el margen a +$14 (25%)", () => {
    expect(precioParaMargenObjetivo(velas, 0.25).valor).toBe(56);
    const m = margenConPrecio(velas, 56);
    expect(m.valor).toBe(14);
    expect(m.porcentaje).toBe(25);
  });

  it("PERDIDA: bajar el costo a $28.5 lleva el margen a +$9.5 (25%)", () => {
    expect(costoMaximoParaMargenObjetivo(velas, 0.25).valor).toBe(28.5);
    const m = margenConCosto(velas, 28.5);
    expect(m.valor).toBe(9.5);
    expect(m.porcentaje).toBe(25);
  });

  it("PERDIDA: el volumen no salva una perdida (null + nota)", () => {
    const u = unidadesParaGananciaObjetivo(velas, 0);
    expect(u.valor).toBeNull();
    expect(u.nota).toContain("no es positivo");
  });

  // Caso SANO (kits de huerto del canon 14): costo total $180, precio $350, fijos $1.200.
  //   costo_unitario = 100 (materiales) + 4h x $20/h = 100 + 80           = 180
  //   margen         = 350 - 180                                          = 170  (48.6%)
  //   unidadesParaGananciaObjetivo(0)    = ceil(1200 / 170) = ceil(7.06)  = 8
  //   unidadesParaGananciaObjetivo(2880) = ceil((1200+2880)/170) = ceil(24) = 24
  //   precioParaMargenObjetivo(0.55)  = 180 / 0.45                        = 400.0
  //   costoMaximoParaMargenObjetivo(0.55) = 350 x 0.45                    = 157.5
  const kits = numeros({ costo_materiales_unidad: 100, horas_por_unidad: 4, valor_hora: 20, precio_tentativo: 350, costos_fijos_mensuales: 1200 });

  it("SANO: 8 unidades cubren los fijos; 24 dejan $2.880 de ganancia", () => {
    expect(margenUnitario(kits).valor).toBe(170);
    expect(unidadesParaGananciaObjetivo(kits, 0).valor).toBe(8);
    expect(unidadesParaGananciaObjetivo(kits, 2880).valor).toBe(24);
  });

  it("SANO: exprimir el precio a $400 (55%) y el costo maximo a $157.5", () => {
    expect(precioParaMargenObjetivo(kits, 0.55).valor).toBe(400);
    expect(costoMaximoParaMargenObjetivo(kits, 0.55).valor).toBe(157.5);
  });

  // RANGOS: costo {min 42, max 52} con margen objetivo 25% -> factor 0.75
  //   precio = {min 42/0.75 = 56, max 52/0.75 = 69.33}
  it("RANGO: precioParaMargenObjetivo respeta el intervalo del costo", () => {
    const conRango = numeros({ costo_materiales_unidad: { min: 30, max: 40 }, horas_por_unidad: 2, valor_hora: 6, precio_tentativo: 38 });
    expect(precioParaMargenObjetivo(conRango, 0.25).valor).toEqual({ min: 56, max: 69.33 });
  });

  it("un margen objetivo de 100% o mas no da precio valido (null + nota)", () => {
    const r = precioParaMargenObjetivo(kits, 1);
    expect(r.valor).toBeNull();
    expect(r.nota).toContain("infinito");
  });

  it("sin costo declarado, margenConPrecio devuelve el faltante, no una cifra", () => {
    const sinCosto = numeros({ precio_tentativo: 38 });
    const m = margenConPrecio(sinCosto, 56);
    expect(m.valor).toBeNull();
    expect(m.insumos_faltantes).toContain("costo_materiales_unidad");
  });
});
