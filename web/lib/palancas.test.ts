// FASE B (canon 14): la capa de politica de las tres palancas. Los numeros
// salen de los primitivos inversos (con paridad Python); aqui se verifica la
// POLITICA del fundador: piso de margen sano 30% (arreglo en perdida), test
// suave ~10% ya sano, redondeo humano de toda cifra recomendada con el margen
// recalculado sobre el numero redondo. Calculo A MANO antes del assert.
import { describe, expect, it } from "vitest";
import { construirPalancas, redondearHumano, type Palancas } from "./palancas";
import type { NumerosProyecto } from "./calculadora";

function numeros(campos: Record<string, number | { min: number; max: number }>): NumerosProyecto {
  const out: NumerosProyecto = {};
  for (const [campo, valor] of Object.entries(campos)) {
    out[campo] = { valor, unidad: null, texto_original: "" };
  }
  return out;
}

describe("redondearHumano: paso segun magnitud", () => {
  it("centavos no, numeros de tienda si", () => {
    expect(redondearHumano(26.6)).toBe(27); // <30 -> paso 1
    expect(redondearHumano(434.78)).toBe(435); // <1000 -> paso 5
    expect(redondearHumano(385)).toBe(385);
    expect(redondearHumano(3900)).toBe(3900); // >=1000 -> paso 50
    expect(redondearHumano(60)).toBe(60);
  });
});

describe("construirPalancas: estado PERDIDA (velas del canon 14)", () => {
  // costo 30 + 2h x $6 = 42 ; precio 38 ; fijos 200 ; margen -4 (-10.5%)
  //   estado = perdida -> ARREGLO al piso 30%
  //   precio  = 42 / 0.70 = 60 (ya redondo)
  //     margen a $60 = 18 ; 18/60 = 30.0% ; ventas ceil(200/18) = 12
  //   costo   = 38 x 0.70 = 26.6 -> redondeo humano -> $27
  //     margen a $27 = 38 - 27 = 11 ; 11/38 = 28.9%  (verdad sobre el redondo)
  //   volumen = BLOQUEADA
  //   recomendada = precio
  const p: Palancas = construirPalancas(
    numeros({ costo_materiales_unidad: 30, horas_por_unidad: 2, valor_hora: 6, precio_tentativo: 38, costos_fijos_mensuales: 200 })
  );

  it("estado perdida, piso 30%, modo arreglo", () => {
    expect(p.estado).toBe("perdida");
    expect(p.pisoMargenSanoPct).toBe(30);
    expect(p.precio.modo).toBe("arreglo");
  });

  it("palanca precio: sube a $60 -> +$18 (30%), 12 ventas cubren fijos", () => {
    expect(p.precio.meta).toBe(60);
    expect(p.precio.margenResultante?.valor).toBe(18);
    expect(p.precio.margenResultante?.porcentaje).toBe(30);
    expect(p.precio.ventasParaCubrirFijos).toBe(12);
    expect(p.precio.recomendada).toBe(true);
  });

  it("palanca costo: baja a $27 redondo -> +$11 (28.9%), margen sobre el redondo", () => {
    expect(p.costo.meta).toBe(27);
    expect(p.costo.margenResultante?.valor).toBe(11);
    expect(p.costo.margenResultante?.porcentaje).toBe(28.9);
  });

  it("palanca volumen: bloqueada honesta", () => {
    expect(p.volumen.bloqueada).toBe(true);
    expect(p.volumen.razonBloqueo).toContain("agranda la pérdida");
    expect(p.volumen.recomendada).toBe(false);
  });
});

describe("construirPalancas: estado SANO (kits del canon 14)", () => {
  // costo 100 + 4h x $20 = 180 ; precio 350 ; fijos 1200 ; capacidad 7.5/sem
  //   margen 170 (48.6%) -> estado sano -> TEST ~10% (experimento, no decreto)
  //   precio  = 350 x 1.10 = 385 (redondo)
  //     margen a $385 = 205 ; 205/385 = 53.2%
  //   costo   = 180 x 0.90 = 162 -> redondeo humano -> $160
  //     margen a $160 = 190 ; 190/350 = 54.3%
  //   volumen = techo capacidad 30 kits/mes ; ganancia 30 x 170 - 1200 = 3900
  //   recomendada = volumen
  const p: Palancas = construirPalancas(
    numeros({ costo_materiales_unidad: 100, horas_por_unidad: 4, valor_hora: 20, precio_tentativo: 350, costos_fijos_mensuales: 1200, capacidad_semanal: 7.5 })
  );

  it("estado sano, modo test", () => {
    expect(p.estado).toBe("sano");
    expect(p.precio.modo).toBe("test");
  });

  it("palanca precio (test): sube a $385 -> 53.2%, no recomendada", () => {
    expect(p.precio.meta).toBe(385);
    expect(p.precio.margenResultante?.porcentaje).toBe(53.2);
    expect(p.precio.recomendada).toBe(false);
  });

  it("palanca costo (test): baja a $160 redondo -> 54.3%", () => {
    expect(p.costo.meta).toBe(160);
    expect(p.costo.margenResultante?.porcentaje).toBe(54.3);
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
