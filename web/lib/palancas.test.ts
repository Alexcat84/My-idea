// FASE B (canon 14): la capa de politica de las tres palancas. Los numeros
// salen de los primitivos inversos (con paridad Python); aqui se verifica la
// POLITICA por defecto (piso de margen sano 30%, estiron +10pp si ya sano,
// volumen honesto). Calculo A MANO antes del assert (regla AGENTS.md).
import { describe, expect, it } from "vitest";
import { construirPalancas, type Palancas } from "./palancas";
import type { NumerosProyecto } from "./calculadora";

function numeros(campos: Record<string, number | { min: number; max: number }>): NumerosProyecto {
  const out: NumerosProyecto = {};
  for (const [campo, valor] of Object.entries(campos)) {
    out[campo] = { valor, unidad: null, texto_original: "" };
  }
  return out;
}

describe("construirPalancas: estado PERDIDA (velas del canon 14)", () => {
  // costo 30 + 2h x $6 = 42 ; precio 38 ; fijos 200 ; margen -4 (-10.5%)
  //   estado = perdida (margen <= 0)
  //   objetivo = piso 30%  (no estas sano)
  //   precio  = 42 / (1 - 0.30) = 42 / 0.70                    = $60
  //     margen a $60 = 60 - 42 = 18 ; 18/60 = 30.0%
  //     ventas para cubrir $200 al nuevo margen = ceil(200/18) = 12
  //   costo   = 38 x (1 - 0.30) = 38 x 0.70                    = $26.6
  //     margen a $26.6 = 38 - 26.6 = 11.4 ; 11.4/38 = 30.0%
  //   volumen = BLOQUEADA (vender mas agranda la perdida)
  //   recomendada = precio
  const p: Palancas = construirPalancas(
    numeros({ costo_materiales_unidad: 30, horas_por_unidad: 2, valor_hora: 6, precio_tentativo: 38, costos_fijos_mensuales: 200 })
  );

  it("estado perdida y objetivo al piso 30%", () => {
    expect(p.estado).toBe("perdida");
    expect(p.margenObjetivoPct).toBe(30);
  });

  it("palanca precio: sube a $60 -> margen +$18 (30%), 12 ventas cubren fijos", () => {
    expect(p.precio.meta).toBe(60);
    expect(p.precio.margenResultante?.valor).toBe(18);
    expect(p.precio.margenResultante?.porcentaje).toBe(30);
    expect(p.precio.ventasParaCubrirFijos).toBe(12);
    expect(p.precio.recomendada).toBe(true);
  });

  it("palanca costo: baja a $26.6 -> margen +$11.4 (30%)", () => {
    expect(p.costo.meta).toBe(26.6);
    expect(p.costo.margenResultante?.valor).toBe(11.4);
    expect(p.costo.margenResultante?.porcentaje).toBe(30);
  });

  it("palanca volumen: bloqueada honesta", () => {
    expect(p.volumen.bloqueada).toBe(true);
    expect(p.volumen.razonBloqueo).toContain("agranda la perdida");
    expect(p.volumen.recomendada).toBe(false);
  });
});

describe("construirPalancas: estado SANO (kits del canon 14)", () => {
  // costo 100 + 4h x $20 = 180 ; precio 350 ; fijos 1200 ; capacidad 7.5/sem
  //   margen 170 (48.6%) -> estado sano
  //   objetivo = estiron: 48.6% + 10pp = 58.6%
  //   precio  = 180 / (1 - 0.586) = 180 / 0.414                = $434.78
  //   costo   = 350 x 0.414                                    = $144.9
  //   volumen = techo capacidad = 7.5 x 4 = 30 kits/mes
  //     ganancia = 30 x 170 - 1200 = 5100 - 1200               = $3.900
  //   recomendada = volumen
  const p: Palancas = construirPalancas(
    numeros({ costo_materiales_unidad: 100, horas_por_unidad: 4, valor_hora: 20, precio_tentativo: 350, costos_fijos_mensuales: 1200, capacidad_semanal: 7.5 })
  );

  it("estado sano y objetivo con estiron a 58.6%", () => {
    expect(p.estado).toBe("sano");
    expect(p.margenObjetivoPct).toBe(58.6);
  });

  it("palanca precio: sube a $434.78 (58.6%)", () => {
    expect(p.precio.meta).toBe(434.78);
    expect(p.precio.margenResultante?.porcentaje).toBe(58.6);
    expect(p.precio.recomendada).toBe(false);
  });

  it("palanca costo: baja a $144.9 (58.6%)", () => {
    expect(p.costo.meta).toBe(144.9);
    expect(p.costo.margenResultante?.porcentaje).toBe(58.6);
  });

  it("palanca volumen: vende 30/mes -> $3.900, y es la recomendada", () => {
    expect(p.volumen.bloqueada).toBe(false);
    expect(p.volumen.meta).toBe(30);
    expect(p.volumen.gananciaResultante).toBe(3900);
    expect(p.volumen.recomendada).toBe(true);
  });
});

describe("construirPalancas: sin datos suficientes no inventa palancas", () => {
  it("sin precio ni costo: estado datos, metas null, recomendada recae en precio", () => {
    const p = construirPalancas(numeros({ costos_fijos_mensuales: 200 }));
    expect(p.estado).toBe("datos");
    expect(p.precio.meta).toBeNull();
    expect(p.costo.meta).toBeNull();
    expect(p.precio.recomendada).toBe(true);
  });
});
