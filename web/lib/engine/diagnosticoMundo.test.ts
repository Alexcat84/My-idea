// AUD-09 H06: el diagnóstico prometía un presupuesto propio "independiente del
// de sesión", pero pasaba su tope de 0,10 USD junto con el acumulado de TODA la
// entrevista. Una entrevista de 0,10 o más dejaba el diagnóstico bloqueado para
// siempre (el mismo 502 en cada reintento). La regla: el tope del diagnóstico se
// mide contra SU PROPIO gasto, y ese gasto se suma después al de la sesión.
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { costoAcumuladoUsd, MODEL_SONNET, type UsoAcumulado } from "../costmeter";
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
    // Cálculo a mano (Sonnet 5.5 desde el 8 oct 2026: 2 USD por millón de entrada, 10 por millón de salida):
    //   entrevista: 30.000 entrada + 6.000 salida = 0,03 × 2 + 0,006 × 10 = 0,06 + 0,06 = 0,12 (más de 0,10)
    //   diagnóstico: 2.000 entrada + 400 salida  = 0,002 × 2 + 0,0004 × 10 = 0,004 + 0,004 = 0,008
    //   total de la sesión después: 0,12 + 0,008 = 0,128
    const entrevista: UsoAcumulado = {
      uso: { [MODEL_SONNET]: { in: 30_000, out: 6_000, llamadas: 6, cache_read: 0, cache_write: 0 } },
      uso_por_componente: { interprete: 0.135 },
      presupuesto_excedido: false,
    };
    const r = await redactarDiagnostico(clienteFalso({ input_tokens: 2_000, output_tokens: 400 }), material, entrevista);
    expect(r.resumen).toBe("Tu diagnóstico.");
    expect(costoAcumuladoUsd(r.acumulado)).toBeCloseTo(0.128, 6);
    expect(r.acumulado.uso[MODEL_SONNET].llamadas).toBe(7);
    expect(r.acumulado.uso_por_componente.diagnostico).toBeCloseTo(0.008, 6);
    expect(r.acumulado.uso_por_componente.interprete).toBeCloseTo(0.135, 6);
  });
});

// i18n F5: el diagnóstico de un mundo lo escribe la IA en el idioma de la idea.
import { redactarDiagnostico as redactarI18n } from "./diagnosticoMundo";
import { usoVacio as usoVacioI18n } from "../costmeter";

describe("redactarDiagnostico: el idioma de la idea (i18n F5)", () => {
  it("con idiomaSalida ar, la llamada lleva la regla de idioma", async () => {
    const create = vi.fn(async () => ({ content: [{ type: "text", text: "تشخيص" }], usage: { input_tokens: 1, output_tokens: 1 } }));
    await redactarI18n({ messages: { create } } as never, {} as never, usoVacioI18n(), "ar");
    const sistema = (create.mock.calls[0] as unknown as [{ system: Array<{ text: string }> }])[0].system;
    expect(sistema).toHaveLength(4); // prompt, sin fuentes, regla de contexto (28 sep 2026), idioma;
    expect(sistema[3].text).toMatch(/^IDIOMA DE SALIDA: árabe/);
  });
});
