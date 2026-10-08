/**
 * Decisión del fundador (corrida final, 8 oct 2026), CAMBIO DE MODELOS:
 *  - lo que usaba Haiku 4.5 pasa a Haiku 5.5 (claude-haiku-5-5);
 *  - lo que usaba Sonnet 4.6 pasa a Sonnet 5.5 (claude-sonnet-5-5);
 *  - el ESTIMADOR (SYSTEM_ESTIMACION_BANDA) es método validado: se re-validó con los casos de su validación original
 *    (constancia del 100 % en los dos modelos) y pasó a Sonnet 5.5 con el VISTO DEL FUNDADOR (8 oct 2026). Llama con
 *    MODEL_ESTIMACION, a la vista en estimacion.ts, para que un cambio de modelo toque el archivo sellado.
 *
 * Los dos modelos 5.5 RAZONAN POR DEFECTO (sondeado contra la API real el 8 oct 2026): Haiku 5.5 gastó 60 de 123
 * tokens de salida en razonar; Sonnet 5.5, 293 de 300, y la respuesta salió CORTADA. El razonamiento sale del tope de
 * salida, así que se apaga: en Haiku 5.5 con `thinking: { type: "disabled" }`; en Sonnet 5.5 la API rechaza
 * "disabled" y pide `thinking: { type: "between_tools" }` (sondeado: responde solo texto, 0 tokens de razonamiento).
 *
 * Precios oficiales (platform.claude.com/docs/en/about-claude/pricing, 8 oct 2026), por millón de tokens:
 *   Haiku 5.5 (prompts hasta 100.000 tokens): 0,10 / 0,50; lectura de caché 0,1x.
 *   Sonnet 5.5: 2 / 10; lectura de caché 0,05x (el 5 % de la entrada, no el 10 %).
 *   Sonnet 4.6: 3 / 15 y Haiku 4.5: 1 / 5, que se conservan (estimador y sesiones viejas).
 *   Escrituras de caché: 1,25x (5 min) y 2x (1 h) en todos.
 */
import { describe, expect, it, vi } from "vitest";
import { readFileSync } from "node:fs";
import path from "node:path";
import type Anthropic from "@anthropic-ai/sdk";
import {
  costoLlamadaUsd,
  llamarClaude,
  llamarClaudeConversacion,
  MODEL,
  MODEL_ESTIMACION,
  MODEL_SONNET,
  MODEL_HAIKU,
  MODEL_HAIKU_4_5,
  MODEL_SONNET_4_6,
  PRECIOS,
  usoVacio,
} from "./costmeter";

function clienteFalso() {
  const create = vi.fn(async (_req: unknown) => ({
    usage: { input_tokens: 10, output_tokens: 5 },
    stop_reason: "end_turn",
    content: [{ type: "text", text: "{}" }],
  }));
  return { client: { messages: { create } } as unknown as Anthropic, create };
}
const leer = (rel: string) => readFileSync(path.join(__dirname, "..", rel), "utf8");

describe("los modelos de la corrida final", () => {
  it("Haiku 5.5 y Sonnet 5.5; el estimador también en Sonnet 5.5 (visto del fundador)", () => {
    expect(MODEL_HAIKU).toBe("claude-haiku-5-5");
    expect(MODEL_SONNET).toBe("claude-sonnet-5-5");
    expect(MODEL).toBe(MODEL_SONNET);
    expect(MODEL_SONNET_4_6).toBe("claude-sonnet-4-6");
    expect(MODEL_HAIKU_4_5).toBe("claude-haiku-4-5");
    expect(MODEL_ESTIMACION).toBe("claude-sonnet-5-5");
  });

  it("precios por millón [entrada, salida]", () => {
    expect(PRECIOS[MODEL_HAIKU]).toEqual([0.1, 0.5]);
    expect(PRECIOS[MODEL_SONNET]).toEqual([2.0, 10.0]);
    expect(PRECIOS[MODEL_SONNET_4_6]).toEqual([3.0, 15.0]);
    expect(PRECIOS[MODEL_HAIKU_4_5]).toEqual([1.0, 5.0]);
  });

  it("coste de una llamada a Haiku 5.5, calculado a mano", () => {
    // 1.000 de entrada, 100 de salida, 10.000 leídos de caché, 2.000 escritos 5 min y 4.000 escritos 1 h:
    //   entrada 1.000 x 0,10 = 100; salida 100 x 0,50 = 50; lectura 10.000 x 0,10 x 0,1 = 100;
    //   escr. 5 min 2.000 x 0,10 x 1,25 = 250; escr. 1 h 4.000 x 0,10 x 2 = 800
    //   total = 1.300 / 1.000.000 = 0,0013 USD
    expect(costoLlamadaUsd(MODEL_HAIKU, 1000, 100, 10000, 2000, 4000)).toBeCloseTo(0.0013, 10);
  });

  it("coste de una llamada a Sonnet 5.5, con su lectura de caché al 5 %, calculado a mano", () => {
    // Mismas cifras con Sonnet 5.5 (2 / 10, lectura 0,05x):
    //   entrada 1.000 x 2 = 2.000; salida 100 x 10 = 1.000; lectura 10.000 x 2 x 0,05 = 1.000;
    //   escr. 5 min 2.000 x 2 x 1,25 = 5.000; escr. 1 h 4.000 x 2 x 2 = 16.000
    //   total = 25.000 / 1.000.000 = 0,025 USD
    expect(costoLlamadaUsd(MODEL_SONNET, 1000, 100, 10000, 2000, 4000)).toBeCloseTo(0.025, 10);
  });

  it("Sonnet 4.6 sigue leyendo caché al 10 %, calculado a mano", () => {
    // entrada 1.000 x 3 = 3.000; salida 100 x 15 = 1.500; lectura 10.000 x 3 x 0,1 = 3.000 -> 7.500 / 1e6
    expect(costoLlamadaUsd(MODEL_SONNET_4_6, 1000, 100, 10000)).toBeCloseTo(0.0075, 10);
  });
});

describe("el razonamiento por defecto se apaga en los modelos 5.5", () => {
  const thinking = (create: ReturnType<typeof vi.fn>) => (create.mock.calls[0][0] as { thinking?: unknown }).thinking;

  it("Haiku 5.5: thinking disabled, en las dos funciones de llamada", async () => {
    const a = clienteFalso();
    await llamarClaude(a.client, "P", "u", MODEL_HAIKU, usoVacio(), { maxTokens: 300 });
    expect(thinking(a.create)).toEqual({ type: "disabled" });
    const b = clienteFalso();
    await llamarClaudeConversacion(b.client, "P", [], "T", MODEL_HAIKU, usoVacio());
    expect(thinking(b.create)).toEqual({ type: "disabled" });
  });

  it("Sonnet 5.5: thinking between_tools (la API rechaza disabled en este modelo)", async () => {
    const { client, create } = clienteFalso();
    await llamarClaude(client, "P", "u", MODEL_SONNET, usoVacio(), { maxTokens: 300 });
    expect(thinking(create)).toEqual({ type: "between_tools" });
  });

  it("Sonnet 4.6 (el estimador) no recibe el parámetro", async () => {
    const { client, create } = clienteFalso();
    await llamarClaude(client, "P", "u", MODEL_SONNET_4_6, usoVacio(), { maxTokens: 300 });
    expect(create.mock.calls[0][0]).not.toHaveProperty("thinking");
  });

  it("las llamadas directas (stream de la Claridad y redactor del plan) lo apagan también", () => {
    expect(leer("app/api/organizer/stream/route.ts")).toMatch(/model: MODEL_HAIKU,\s*\.\.\.parametrosDeModelo\(MODEL_HAIKU\)/);
    expect(leer("lib/engine/redactorPlan.ts")).toMatch(/model: MODEL_SONNET,\s*\.\.\.parametrosDeModelo\(MODEL_SONNET\)/);
  });
});

describe("el estimador queda protegido", () => {
  it("estimacion.ts (método validado) llama con MODEL_ESTIMACION, que es Sonnet 5.5", () => {
    const fuente = leer("lib/engine/estimacion.ts");
    expect(fuente).toMatch(/llamarClaude\(client, SYSTEM_ESTIMACION_BANDA, userText, MODEL_ESTIMACION,/);
    expect(MODEL_ESTIMACION).toBe(MODEL_SONNET);
  });

  it("ningún otro componente de la app usa MODEL: todos usan MODEL_SONNET o MODEL_HAIKU", () => {
    for (const rel of [
      "lib/engine/diagnosticoMundo.ts",
      "lib/engine/enlazador.ts",
      "lib/engine/redactorPlan.ts",
      "lib/engine/reformuladorProteccion.ts",
      "lib/engine/reporte.ts",
      "app/api/project/[id]/replantear/route.ts",
    ]) {
      expect(leer(rel), rel).not.toMatch(/\bMODEL\b/);
    }
  });
});
