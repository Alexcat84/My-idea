// FASE B (canon 14): logica pura del tablero vivo. Veredicto determinista
// (numeros por codigo), comparacion de cifras, y el mensaje del tope diario.
import { describe, expect, it } from "vitest";
import { cifrasCambiaron, fraseCicloCaja, MENSAJE_TOPE_RENARRACION, veredictoNumeros } from "./numerosVivo";
import { armarTablero } from "./tableroNumeros";
import type { NumerosProyecto } from "./calculadora";

function numeros(campos: Record<string, number | { min: number; max: number }>): NumerosProyecto {
  const out: NumerosProyecto = {};
  for (const [campo, valor] of Object.entries(campos)) {
    out[campo] = { valor, unidad: null, texto_original: "" };
  }
  return out;
}

const velas = numeros({ costo_materiales_unidad: 30, horas_por_unidad: 2, valor_hora: 6, precio_tentativo: 38, costos_fijos_mensuales: 200 });
const kits = numeros({ costo_materiales_unidad: 100, horas_por_unidad: 4, valor_hora: 20, precio_tentativo: 350, costos_fijos_mensuales: 1200, capacidad_semanal: 7.5 });

describe("veredictoNumeros: la frase con su color, por codigo", () => {
  it("PERDIDA: ambar, dice cuanto pierde por unidad, espejo sin regano", () => {
    const v = veredictoNumeros(armarTablero(velas), "vela");
    expect(v.tono).toBe("perdida");
    expect(v.acento).toBe("$4 mas de lo que cobras");
    expect(v.frase).toContain("cada vela que vendes te cuesta $4 mas de lo que cobras");
    expect(v.frase).not.toContain("—"); // sin guiones largos (voz)
  });

  it("SANO: verde, margen limpio y punto de equilibrio", () => {
    const v = veredictoNumeros(armarTablero(kits), "kit");
    expect(v.tono).toBe("sano");
    expect(v.acento).toBe("$170 limpios");
    expect(v.frase).toContain("con vender 8 al mes ya cubres tus $1.200 de gasto fijo");
  });

  it("DATOS: azul, no inventa cifras cuando faltan", () => {
    const v = veredictoNumeros(armarTablero(numeros({ costos_fijos_mensuales: 200 })), "kit");
    expect(v.tono).toBe("datos");
    expect(v.acento).toBeNull();
  });
});

describe("cifrasCambiaron: solo los valores, no los metadatos", () => {
  it("sin version previa, es cambio (primera corrida)", () => {
    expect(cifrasCambiaron(velas, null)).toBe(true);
  });
  it("mismos valores, distinto metadato: NO es cambio", () => {
    const otro: NumerosProyecto = { precio_tentativo: { valor: 38, unidad: "$", texto_original: "otro", updated_at: "2026-01-01" } };
    const base: NumerosProyecto = { precio_tentativo: { valor: 38, unidad: null, texto_original: "" } };
    expect(cifrasCambiaron(otro, base)).toBe(false);
  });
  it("un valor distinto: es cambio", () => {
    const subido = numeros({ costo_materiales_unidad: 30, horas_por_unidad: 2, valor_hora: 6, precio_tentativo: 45, costos_fijos_mensuales: 200 });
    expect(cifrasCambiaron(subido, velas)).toBe(true);
  });
});

describe("fraseCicloCaja: el ciclo de caja en palabras de persona", () => {
  it("null cuando faltan los datos", () => {
    expect(fraseCicloCaja(null)).toBeNull();
  });
  it("positivo: la plata tarda N días en volver", () => {
    expect(fraseCicloCaja(50)).toContain("tarda unos 50 días en volver");
  });
  it("cero: vuelve el mismo día", () => {
    expect(fraseCicloCaja(0)).toContain("el mismo día");
  });
  it("negativo: cobras antes de pagar, a favor (nunca 'malo')", () => {
    const f = fraseCicloCaja(-10)!;
    expect(f).toContain("Cobras antes de pagar");
    expect(f).toContain("10 días de holgura");
  });
});

describe("mensaje del tope diario", () => {
  it("habla en palabras de persona y promete que nada se pierde", () => {
    expect(MENSAJE_TOPE_RENARRACION).toContain("limite de relecturas");
    expect(MENSAJE_TOPE_RENARRACION).toContain("quedan guardados");
  });
});
