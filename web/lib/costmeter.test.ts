// Fase 3.0: paridad numerica contra la contabilidad de costo real de
// prototipo_motor.py. El primer caso usa numeros REALES ya impresos en
// una sesion en vivo de este mismo proyecto (hotfix v2.1.2:
// "claude-haiku-4-5: 1 llamadas | 3 in / 575 out (cache_read 8081,
// cache_write 1275) | $0.0053"), calculado a mano antes del assert.
import { describe, expect, it } from "vitest";
import {
  CACHE_READ_MULT,
  CACHE_WRITE_MULT,
  MODEL_HAIKU,
  costoAcumuladoUsd,
  costoLlamadaUsd,
  desgloseCosto,
  registrarUso,
  usoVacio,
} from "./costmeter";

describe("costoLlamadaUsd -- caso real documentado (hotfix v2.1.2)", () => {
  it("3 in / 575 out / cache_read 8081 / cache_write 1275 (Haiku) = $0.0053", () => {
    // Calculo manual: pin=1.00, pout=5.00 (Haiku, por millon de tokens)
    //   in:          3 / 1e6 * 1.00        = 0.000003
    //   cache_read:  8081 / 1e6 * 1.00 * 0.1  = 0.0008081
    //   cache_write: 1275 / 1e6 * 1.00 * 1.25 = 0.00159375
    //   out:         575 / 1e6 * 5.00        = 0.002875
    //   total = 0.000003 + 0.0008081 + 0.00159375 + 0.002875 = 0.00527985
    const costo = costoLlamadaUsd(MODEL_HAIKU, 3, 575, 8081, 1275);
    expect(Number(costo.toFixed(4))).toBe(0.0053);
    expect(costo).toBeCloseTo(0.00527985, 8);
  });
});

describe("multiplicadores de cache", () => {
  it("CACHE_READ_MULT=0.1, CACHE_WRITE_MULT=1.25 (mismos valores que Python)", () => {
    expect(CACHE_READ_MULT).toBe(0.1);
    expect(CACHE_WRITE_MULT).toBe(1.25);
  });
});

describe("registrarUso + costoAcumuladoUsd: acumula sin mutar el original", () => {
  it("dos llamadas al mismo modelo se suman; el acumulador original queda intacto", () => {
    const inicial = usoVacio();
    const despuesDeUnaLlamada = registrarUso(
      inicial,
      MODEL_HAIKU,
      { input_tokens: 100, output_tokens: 20, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
      "turnos"
    );
    // El acumulador original nunca se muta -- principio de funciones puras.
    expect(inicial.uso).toEqual({});

    const despuesDeDosLlamadas = registrarUso(
      despuesDeUnaLlamada,
      MODEL_HAIKU,
      { input_tokens: 50, output_tokens: 10, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
      "turnos"
    );
    expect(despuesDeDosLlamadas.uso[MODEL_HAIKU].llamadas).toBe(2);
    expect(despuesDeDosLlamadas.uso[MODEL_HAIKU].in).toBe(150);
    expect(despuesDeDosLlamadas.uso[MODEL_HAIKU].out).toBe(30);

    // costoAcumuladoUsd sobre 150 in / 30 out, sin cache:
    //   150/1e6*1.00 + 30/1e6*5.00 = 0.00015 + 0.00015 = 0.0003
    expect(costoAcumuladoUsd(despuesDeDosLlamadas)).toBeCloseTo(0.0003, 8);
  });

  it("desgloseCosto agrega por componente y por modelo", () => {
    const acumulado = registrarUso(
      usoVacio(),
      MODEL_HAIKU,
      { input_tokens: 3, output_tokens: 575, cache_read_input_tokens: 8081, cache_creation_input_tokens: 1275 },
      "turnos"
    );
    const desglose = desgloseCosto(acumulado);
    expect(desglose.por_componente.turnos).toBeCloseTo(0.00527985, 8);
    expect(Number(desglose.total_usd.toFixed(4))).toBe(0.0053);
  });
});
