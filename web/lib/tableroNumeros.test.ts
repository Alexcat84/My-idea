// FASE B (canon 14): el tablero determinista que pinta la pantalla. Verifica
// las derivaciones propias (barra de la verdad, faltantes) y el ensamblado.
// Calculo a mano antes del assert.
import { describe, expect, it } from "vitest";
import { armarTablero, barraVerdad, faltantesDeReporte } from "./tableroNumeros";
import { calcularReporte, type NumerosProyecto } from "./calculadora";

function numeros(campos: Record<string, number | { min: number; max: number }>): NumerosProyecto {
  const out: NumerosProyecto = {};
  for (const [campo, valor] of Object.entries(campos)) {
    out[campo] = { valor, unidad: null, texto_original: "" };
  }
  return out;
}

describe("barraVerdad: costo vs precio escalados a la mayor", () => {
  it("perdida (velas 42/38): costo 100%, precio 90.5%, en perdida", () => {
    // mayor = 42 ; costo 42/42 = 100 ; precio 38/42 = 90.476 -> 90.5
    expect(barraVerdad(42, 38)).toEqual({ costoPct: 100, precioPct: 90.5, enPerdida: true });
  });
  it("sano (kits 180/350): costo 51.4%, precio 100%, sin perdida", () => {
    // mayor = 350 ; costo 180/350 = 51.428 -> 51.4 ; precio 100
    expect(barraVerdad(180, 350)).toEqual({ costoPct: 51.4, precioPct: 100, enPerdida: false });
  });
  it("sin datos: nulls, sin perdida", () => {
    expect(barraVerdad(null, 38)).toEqual({ costoPct: null, precioPct: null, enPerdida: false });
  });
});

describe("faltantesDeReporte: agrega insumos faltantes sin repetir", () => {
  it("velas sin capacidad ni datos de ciclo: los lista ordenados", () => {
    const rep = calcularReporte(numeros({ costo_materiales_unidad: 30, horas_por_unidad: 2, valor_hora: 6, precio_tentativo: 38, costos_fijos_mensuales: 200 }));
    const f = faltantesDeReporte(rep);
    expect(f).toContain("capacidad_semanal");
    expect(f).toContain("dias_inventario");
    // ordenado y sin repetir
    expect(f).toEqual([...f].sort());
    expect(new Set(f).size).toBe(f.length);
  });
});

describe("armarTablero: ensamblado sobre los dos casos del canon", () => {
  it("PERDIDA (velas): tiles, estado y equilibrio coherentes", () => {
    const t = armarTablero(numeros({ costo_materiales_unidad: 30, horas_por_unidad: 2, valor_hora: 6, precio_tentativo: 38, costos_fijos_mensuales: 200 }));
    expect(t.estado).toBe("perdida");
    expect(t.costoUnitario).toBe(42);
    expect(t.precio).toBe(38);
    expect(t.margen).toBe(-4);
    expect(t.margenPct).toBe(-10.5);
    expect(t.puntoEquilibrio).toBeNull(); // margen negativo: no hay
    expect(t.puntoEquilibrioNota).toBeTruthy();
    expect(t.barra).toEqual({ costoPct: 100, precioPct: 90.5, enPerdida: true });
    expect(t.gigo.inconsistente).toBe(false); // -10.5% no dispara el guardian
    expect(t.palancas.precio.recomendada).toBe(true);
  });

  it("SANO (kits): tiles y equilibrio positivos", () => {
    const t = armarTablero(numeros({ costo_materiales_unidad: 100, horas_por_unidad: 4, valor_hora: 20, precio_tentativo: 350, costos_fijos_mensuales: 1200, capacidad_semanal: 7.5 }));
    expect(t.estado).toBe("sano");
    expect(t.margen).toBe(170);
    expect(t.puntoEquilibrio).toBe(8); // ceil(1200/170)
    expect(t.barra).toEqual({ costoPct: 51.4, precioPct: 100, enPerdida: false });
    expect(t.palancas.volumen.recomendada).toBe(true);
  });
});
