/**
 * LOS NUMEROS DEL MOMENTO DE CADA PLAN (decision del fundador, 10 oct 2026). La medicion final armo el bloque de numeros
 * con los numeros_proyecto de HOY, y esos proyectos traian las cifras que la fase 3 del vuelo siembra despues para el
 * guardian GIGO: 18 de los 30 sostenidos. Cada cifra guardada lleva su fecha (updated_at); en el momento del plan solo
 * existian las anteriores a el. Casos reales (fechas de la base, 8 oct 2026, UTC):
 *  - plan 9909f451 a las 23:37:25; precio 13, 20 unidades, 200 fijos y costo 0 guardados a las 23:37:42-43 -> ninguna;
 *  - plan aad2749d a las 23:00:20; las cifras de las macetas, a las 22:59:45-51 -> todas.
 */
import { describe, expect, it } from "vitest";
import { numerosDelMomento } from "./numerosDelMomento";

const APP = {
  precio_tentativo: { valor: 13, updated_at: "2026-10-08T23:37:43.100Z" },
  unidades_vendidas: { valor: 20, updated_at: "2026-10-08T23:37:43.050Z" },
  costos_fijos_mensuales: { valor: 200, updated_at: "2026-10-08T23:37:42.900Z" },
  costo_materiales_unidad: { valor: 0, updated_at: "2026-10-08T23:37:42.800Z" },
};
const MACETAS = {
  costo_materiales_unidad: { valor: 130, updated_at: "2026-10-08T22:59:48Z", texto_original: "130 incluyendo mi hora a 50" },
  horas_por_unidad: { valor: 2, updated_at: "2026-10-08T22:59:45Z" },
  precio_tentativo: { valor: 250, updated_at: "2026-10-08T22:59:48Z" },
};

describe("numerosDelMomento: solo las cifras que existían cuando nació el plan", () => {
  it("caso real 9909f451: las cifras GIGO, guardadas 18 segundos después del plan, no entran", () => {
    const r = numerosDelMomento(APP, {}, "2026-10-08T23:37:25.000+00:00");
    expect(r.numeros).toEqual({});
    expect(r.fuera.sort()).toEqual(["costo_materiales_unidad", "costos_fijos_mensuales", "precio_tentativo", "unidades_vendidas"]);
  });

  it("caso real aad2749d: las cifras de las macetas, guardadas antes del plan, entran todas", () => {
    const r = numerosDelMomento(MACETAS, {}, "2026-10-08T23:00:20.000+00:00");
    expect(Object.keys(r.numeros).sort()).toEqual(["costo_materiales_unidad", "horas_por_unidad", "precio_tentativo"]);
    expect(r.fuera).toEqual([]);
  });

  it("las cifras de la propia sesión entran siempre (son de ese momento) y mandan sobre las del proyecto", () => {
    const r = numerosDelMomento(APP, { precio_tentativo: { valor: 15 } }, "2026-10-08T23:37:25Z");
    expect(r.numeros).toEqual({ precio_tentativo: { valor: 15 } });
  });

  it("una cifra del proyecto sin fecha no se puede situar: no entra y se avisa", () => {
    const r = numerosDelMomento({ precio_tentativo: { valor: 250 } }, {}, "2026-10-08T23:00:00Z");
    expect(r.numeros).toEqual({});
    expect(r.sinFecha).toEqual(["precio_tentativo"]);
  });
});
