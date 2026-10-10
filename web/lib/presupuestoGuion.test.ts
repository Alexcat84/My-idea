/**
 * TOPES DE LOS GUIONES (decision del fundador, 10 oct 2026). Los guiones de la API miraban el tope antes de cada
 * llamada, pero con llamadas en paralelo las que ya estaban en curso terminaban despues del tope: la parte 1 de la copia
 * fiel paso de 8 a 8,76 USD y la reescritura r3 de 3,6 a 4,77. Ahora cada llamada RESERVA su coste maximo antes de
 * lanzarse (entrada estimada + el tope de salida al precio del modelo) y, al terminar, la reserva se cambia por el coste
 * real. Una llamada que no cabe con lo gastado mas lo reservado no se lanza. Asi el tope se cumple aunque haya
 * llamadas en paralelo.
 *
 * Calculo a mano del caso de la prueba: tope 1,00; cada llamada reserva 0,30 y cuesta de verdad 0,25.
 *   con 6 en paralelo caben 3 reservas (0,90); la cuarta (1,20) no se lanza hasta que alguna termina;
 *   tras terminar las tres: gastado 0,75; cabe una mas (0,75 + 0,30 = 1,05 > 1,00): NO cabe -> se para.
 *   gasto final: 0,75, nunca por encima de 1,00; llamadas hechas: 3.
 */
import { describe, expect, it } from "vitest";
import { Presupuesto, TopeAlcanzado, reservaDeLlamada } from "./presupuestoGuion";

const espera = (ms: number) => new Promise((r) => setTimeout(r, ms));

describe("Presupuesto: el tope se cumple aunque haya llamadas en paralelo", () => {
  it("con 6 llamadas en paralelo, el gasto nunca pasa del tope (caso a mano: 3 llamadas, 0,75)", async () => {
    const p = new Presupuesto(1.0);
    let hechas = 0;
    let topes = 0;
    const llamada = async () => {
      const r = p.reservar(0.3);
      await espera(5 + Math.random() * 10);
      p.cerrar(r, 0.25);
      hechas++;
    };
    const trabajadores = Array.from({ length: 6 }, async () => {
      for (let i = 0; i < 4; i++) {
        try {
          await llamada();
        } catch (e) {
          if (e instanceof TopeAlcanzado) {
            topes++;
            return;
          }
          throw e;
        }
      }
    });
    await Promise.all(trabajadores);
    expect(p.gastado).toBeCloseTo(0.75, 10);
    expect(p.gastado).toBeLessThanOrEqual(1.0);
    expect(hechas).toBe(3);
    expect(topes).toBe(6);
  });

  it("una reserva que no cabe no se lanza y no deja nada reservado", () => {
    const p = new Presupuesto(0.5);
    p.reservar(0.4);
    expect(() => p.reservar(0.2)).toThrow(TopeAlcanzado);
    expect(p.reservado).toBeCloseTo(0.4, 10);
  });

  it("si la llamada falla, la reserva se libera sin gasto", () => {
    const p = new Presupuesto(1);
    const r = p.reservar(0.3);
    p.liberar(r);
    expect(p.reservado).toBe(0);
    expect(p.gastado).toBe(0);
  });

  it("la reserva es el peor caso: entrada estimada por lo alto y todo el tope de salida", () => {
    // 3.000 caracteres / 2,5 = 1.200 tokens de entrada x 5 USD/M = 0,006; 16.000 de salida x 25 USD/M = 0,4. Total 0,406.
    expect(reservaDeLlamada(3000, 16000, [5, 25])).toBeCloseTo(0.406, 10);
  });
});
