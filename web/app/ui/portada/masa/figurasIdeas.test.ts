/**
 * Decisión del fundador (8 oct 2026): la masa deja de alternar las cinco etapas
 * y forma MUCHAS figuras (al menos 40) de ideas hechas realidad, en orden
 * aleatorio y distinto en cada visita; ninguna es un logotipo, una marca ni un
 * personaje conocido; siluetas precalculadas para que sea ligera en móviles.
 *
 * Cada valor esperado sale del cálculo a mano del comentario (AGENTS.md).
 */
import { existsSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { FIGURAS } from "./catalogo";
import { DURACION_CICLO, figuraEn, ordenDeVisita } from "./ciclo";
import { codificarCampo, decodificarCampo, LADO_CAMPO, puntosDeCampo, RANGO_CAMPO } from "./figuras";

const PUBLICO = path.join(__dirname, "..", "..", "..", "..", "public", "portada", "figuras");

describe("el catálogo: ideas hechas realidad", () => {
  it("son al menos 40, sin nombres repetidos", () => {
    expect(FIGURAS.length).toBeGreaterThanOrEqual(40);
    expect(new Set(FIGURAS).size).toBe(FIGURAS.length);
  });

  it("ya no están las cinco etapas de antes", () => {
    for (const vieja of ["foco", "lente", "brujula", "escalera", "casa"]) expect(FIGURAS as readonly string[]).not.toContain(vieja);
  });

  it("están las que pidió el fundador", () => {
    for (const pedida of ["cafeteria", "bicicleta", "maceta", "panaderia", "laptop", "foodtruck", "tienda", "cohete", "guitarra", "velero", "camara", "casahuerto"]) {
      expect(FIGURAS as readonly string[]).toContain(pedida);
    }
  });

  it("cada una tiene su campo precalculado: 128 x 128 valores de 16 bits = 32 768 bytes", () => {
    // 128 * 128 = 16 384 valores * 2 bytes = 32 768
    expect(LADO_CAMPO).toBe(128);
    for (const nombre of FIGURAS) {
      const archivo = path.join(PUBLICO, `${nombre}.bin`);
      expect(existsSync(archivo), nombre).toBe(true);
      expect(statSync(archivo).size, nombre).toBe(32768);
    }
  });

  it("cada campo tiene trazo (valores negativos) y aire (positivos)", () => {
    for (const nombre of FIGURAS) {
      const b = readFileSync(path.join(PUBLICO, `${nombre}.bin`));
      const campo = decodificarCampo(new Uint16Array(b.buffer, b.byteOffset, b.byteLength / 2));
      let dentro = 0;
      let fuera = 0;
      for (const d of campo) {
        if (d < 0) dentro++;
        else fuera++;
      }
      expect(dentro, nombre).toBeGreaterThan(200);
      expect(fuera, nombre).toBeGreaterThan(dentro);
    }
  });

  it("el navegador no carga los dibujos: ni el motor ni el respaldo importan el horno", () => {
    for (const f of ["motor.ts", "respaldo.ts", "figuras.ts", "ciclo.ts", "trabajador.ts", "anfitrion.ts"]) {
      expect(readFileSync(path.join(__dirname, f), "utf8"), f).not.toMatch(/from ["'][^"']*(scripts\/portada|dibujos)/);
    }
  });
});

describe("el orden de la visita", () => {
  // azar fijo 0: Fisher-Yates de i = n-1 a 1 con j = floor(0 * (i + 1)) = 0.
  // n = 4, [0,1,2,3]: i=3 cambia 3<->0 -> [3,1,2,0]; i=2 cambia 2<->0 -> [2,1,3,0];
  // i=1 cambia 1<->0 -> [1,2,3,0].
  it("es una permutación de Fisher-Yates (azar 0 -> [1, 2, 3, 0])", () => {
    expect(ordenDeVisita(4, () => 0)).toEqual([1, 2, 3, 0]);
  });

  it("recorre todas las figuras, cada una una vez", () => {
    const orden = ordenDeVisita(FIGURAS.length, Math.random);
    expect([...orden].sort((a, b) => a - b)).toEqual(FIGURAS.map((_, i) => i));
  });

  it("dos visitas no salen en el mismo orden", () => {
    // Con 53 figuras hay 53! órdenes: que dos azares independientes coincidan
    // es imposible en la práctica.
    expect(ordenDeVisita(FIGURAS.length, Math.random)).not.toEqual(ordenDeVisita(FIGURAS.length, Math.random));
  });
});

describe("qué figura forma cada ciclo", () => {
  // ciclo k = floor(t / 9.8); figura = orden[k mod largo]
  const orden = [7, 2, 5];
  it("sigue el orden de la visita y vuelve a empezar", () => {
    expect(figuraEn(0, orden)).toBe(7);
    expect(figuraEn(DURACION_CICLO * 1.5, orden)).toBe(2);
    expect(figuraEn(DURACION_CICLO * 2.5, orden)).toBe(5);
    expect(figuraEn(DURACION_CICLO * 3.5, orden)).toBe(7);
  });
});

describe("el campo en 16 bits", () => {
  it("codifica lineal sobre [-2.6, 2.6] y recorta fuera", () => {
    // d = 0    -> (0 + 0.5) * 65535 = 32767.5 -> 32768
    // d = 1.3  -> (0.25 + 0.5) * 65535 = 49151.25 -> 49151
    // d = -2.6 -> 0;  d = 2.6 -> 65535;  d = 5 -> recorta a 2.6 -> 65535
    expect(RANGO_CAMPO).toBe(2.6);
    expect(Array.from(codificarCampo(Float32Array.from([0, 1.3, -2.6, 2.6, 5])))).toEqual([32768, 49151, 0, 65535, 65535]);
  });

  it("decodifica de vuelta con error menor a un paso (5.2 / 65535 = 0.0000793)", () => {
    // 49151 -> 49151 / 65535 * 2 - 1 = 0.4999924 -> * 2.6 = 1.2999802
    const d = decodificarCampo(Uint16Array.from([0, 32768, 49151, 65535]));
    expect(d[0]).toBeCloseTo(-2.6, 6);
    expect(Math.abs(d[1])).toBeLessThan(0.0000793);
    expect(d[2]).toBeCloseTo(1.2999802, 6);
    expect(d[3]).toBeCloseTo(2.6, 6);
  });
});

describe("puntos para el respaldo de partículas", () => {
  // Grilla de 4 x 4 sobre [-1.8, 1.8]: paso 0.9. Solo el texel (i = 2, j = 1)
  // está dentro del trazo -> x en [-1.8 + 2 * 0.9, -1.8 + 3 * 0.9] = [0, 0.9],
  // y en [-1.8 + 0.9, -1.8 + 2 * 0.9] = [-0.9, 0].
  it("caen todos dentro del texel del trazo", () => {
    const campo = new Float32Array(16).fill(1);
    campo[1 * 4 + 2] = -0.2;
    const p = puntosDeCampo(campo, 4, 50, Math.random, 0);
    for (let k = 0; k < 50; k++) {
      expect(p[k * 3]).toBeGreaterThanOrEqual(0);
      expect(p[k * 3]).toBeLessThanOrEqual(0.9);
      expect(p[k * 3 + 1]).toBeGreaterThanOrEqual(-0.9);
      expect(p[k * 3 + 1]).toBeLessThanOrEqual(0);
      expect(Math.abs(p[k * 3 + 2])).toBe(0);
    }
  });

  it("sin trazo, no inventa puntos (todo en cero)", () => {
    expect(Array.from(puntosDeCampo(new Float32Array(16).fill(1), 4, 3, Math.random))).toEqual(new Array(9).fill(0));
  });
});
