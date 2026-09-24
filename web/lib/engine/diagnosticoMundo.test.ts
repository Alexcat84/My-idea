// AUD-09 H06: el diagnóstico prometía un presupuesto propio "independiente del
// de sesión", pero pasaba su tope de 0,10 USD junto con el acumulado de TODA la
// entrevista. Una entrevista de 0,10 o más dejaba el diagnóstico bloqueado para
// siempre (el mismo 502 en cada reintento). La regla: el tope del diagnóstico se
// mide contra SU PROPIO gasto, y ese gasto se suma después al de la sesión.
import { describe, expect, it } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { costoAcumuladoUsd, MODEL, type UsoAcumulado } from "../costmeter";
import { redactarDiagnostico, type MaterialDiagnostico } from "./diagnosticoMundo";

function clienteFalso(usage: { input_tokens: number; output_tokens: number }) {
  return {
    messages: {
      create: async () => ({ content: [{ type: "text", text: "Tu diagnóstico." }], usage }),
    },
  } as unknown as Anthropic;
}

const material = {} as MaterialDiagnostico;

describe("redactarDiagnostico: su tope se mide contra su propio gasto", () => {
  it("una entrevista que ya gastó más de 0,10 USD no bloquea el diagnóstico", async () => {
    // Cálculo a mano (Sonnet: 3 USD por millón de entrada, 15 por millón de salida):
    //   entrevista: 20.000 entrada + 5.000 salida = 0,02 × 3 + 0,005 × 15 = 0,06 + 0,075 = 0,135
    //   diagnóstico: 2.000 entrada + 400 salida  = 0,002 × 3 + 0,0004 × 15 = 0,006 + 0,006 = 0,012
    //   total de la sesión después: 0,135 + 0,012 = 0,147
    const entrevista: UsoAcumulado = {
      uso: { [MODEL]: { in: 20_000, out: 5_000, llamadas: 6, cache_read: 0, cache_write: 0 } },
      uso_por_componente: { interprete: 0.135 },
      presupuesto_excedido: false,
    };
    const r = await redactarDiagnostico(clienteFalso({ input_tokens: 2_000, output_tokens: 400 }), material, entrevista);
    expect(r.resumen).toBe("Tu diagnóstico.");
    expect(costoAcumuladoUsd(r.acumulado)).toBeCloseTo(0.147, 6);
    expect(r.acumulado.uso[MODEL].llamadas).toBe(7);
    expect(r.acumulado.uso_por_componente.diagnostico).toBeCloseTo(0.012, 6);
    expect(r.acumulado.uso_por_componente.interprete).toBeCloseTo(0.135, 6);
  });
});
