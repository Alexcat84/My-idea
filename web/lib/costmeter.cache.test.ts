// Contexto de la entrevista, principio 3 (decision del fundador, 28 sep 2026):
// AHORRO CON EL CACHE DE LA API, y la falla nueva de las respuestas cortadas.
//
//  - La escritura de cache de 1 hora cuesta 2x la entrada; la de 5 minutos,
//    1.25x; la lectura, 0.1x. costo_usd las cobra con su tarifa.
//  - Cada llamada deja su registro (componente, modelo, tokens, lecturas y
//    escrituras de cache, USD, stop_reason) para medir el ahorro real.
//  - Orden para el cache: lo fijo (system con sus reglas, marca de 1 hora),
//    despues el contexto del proyecto (marca de 1 hora), al final el turno.
//  - Una respuesta cortada por tope de tokens no se guarda nunca: se reintenta
//    una vez con el doble de tope y, si vuelve a cortarse, falla con aviso.
//
// A mano, Haiku (1 USD entrada / 5 USD salida por millon):
//   in 1000 -> 1000 * 1          = 1000
//   out 100 -> 100 * 5           =  500
//   lectura 10000 -> 10000*1*0.1 = 1000
//   escritura 5m 2000 -> *1.25   = 2500
//   escritura 1h 4000 -> *2      = 8000
//   total 13000 / 1e6            = 0.013 USD
import type Anthropic from "@anthropic-ai/sdk";
import { describe, expect, it, vi } from "vitest";
import {
  RespuestaCortadaError,
  costoAcumuladoUsd,
  costoLlamadaUsd,
  llamarClaude,
  registrarUso,
  usoVacio,
} from "./costmeter";

const USAGE_A_MANO = {
  input_tokens: 1000,
  output_tokens: 100,
  cache_read_input_tokens: 10000,
  cache_creation_input_tokens: 6000,
  cache_creation: { ephemeral_5m_input_tokens: 2000, ephemeral_1h_input_tokens: 4000 },
};

describe("tarifas de cache y registro por llamada", () => {
  it("costoLlamadaUsd cobra la escritura de 1 hora a 2x", () => {
    expect(costoLlamadaUsd("claude-haiku-4-5", 1000, 100, 10000, 2000, 4000)).toBeCloseTo(0.013, 10);
  });

  it("registrarUso separa las escrituras de 5 minutos y de 1 hora y deja el registro de la llamada", () => {
    const a = registrarUso(usoVacio(), "claude-haiku-4-5", USAGE_A_MANO, "turnos", "end_turn");
    expect(a.uso["claude-haiku-4-5"]).toMatchObject({ cache_read: 10000, cache_write: 2000, cache_write_1h: 4000, llamadas: 1 });
    expect(costoAcumuladoUsd(a)).toBeCloseTo(0.013, 10);
    expect(a.llamadas).toHaveLength(1);
    expect(a.llamadas![0]).toMatchObject({
      componente: "turnos",
      modelo: "claude-haiku-4-5",
      in: 1000,
      out: 100,
      cache_read: 10000,
      cache_write_5m: 2000,
      cache_write_1h: 4000,
      stop_reason: "end_turn",
    });
    expect(a.llamadas![0].usd).toBeCloseTo(0.013, 10);
  });

  it("sin desglose por TTL, toda escritura cuenta como de 5 minutos (compatibilidad)", () => {
    const a = registrarUso(usoVacio(), "claude-haiku-4-5", { input_tokens: 0, output_tokens: 0, cache_creation_input_tokens: 800 });
    expect(a.uso["claude-haiku-4-5"]).toMatchObject({ cache_write: 800, cache_write_1h: 0 });
  });
});

function clienteSecuencia(respuestas: Array<{ stop: string; texto: string }>) {
  const create = vi.fn(async (_kw: Record<string, unknown>) => {
    const r = respuestas.shift()!;
    return { content: [{ type: "text", text: r.texto }], stop_reason: r.stop, usage: { input_tokens: 10, output_tokens: 10 } };
  });
  return { create, client: { messages: { create } } as unknown as Anthropic };
}

describe("respuestas cortadas por tope de tokens", () => {
  it("reintenta una vez con el doble de tope y devuelve la respuesta completa", async () => {
    const { create, client } = clienteSecuencia([
      { stop: "max_tokens", texto: "cort" },
      { stop: "end_turn", texto: "completa" },
    ]);
    const r = await llamarClaude(client, "P", "u", "claude-haiku-4-5", usoVacio(), { maxTokens: 300, componente: "x" });
    expect(r.texto).toBe("completa");
    expect(create).toHaveBeenCalledTimes(2);
    expect(create.mock.calls[1][0].max_tokens).toBe(600);
    // las dos llamadas se pagan y se registran
    expect(r.acumulado.uso["claude-haiku-4-5"].llamadas).toBe(2);
    expect(r.acumulado.llamadas!.map((l) => l.stop_reason)).toEqual(["max_tokens", "end_turn"]);
  });

  it("si vuelve a cortarse, falla con aviso y no devuelve la salida cortada", async () => {
    const { client } = clienteSecuencia([
      { stop: "max_tokens", texto: "cort" },
      { stop: "max_tokens", texto: "cortada otra vez" },
    ]);
    await expect(llamarClaude(client, "P", "u", "claude-haiku-4-5", usoVacio(), { maxTokens: 300, componente: "x" })).rejects.toBeInstanceOf(
      RespuestaCortadaError
    );
  });
});

describe("orden para el cache: fijo, contexto del proyecto, turno", () => {
  it("el contexto del proyecto va en su propio bloque con cache de 1 hora, antes del turno", async () => {
    const { create, client } = clienteSecuencia([{ stop: "end_turn", texto: "ok" }]);
    await llamarClaude(client, "P", "TURNO", "claude-haiku-4-5", usoVacio(), { contexto: "CONTEXTO DEL PROYECTO" });
    const kw = create.mock.calls[0][0] as { messages: Array<{ content: unknown }>; system: Array<{ cache_control?: unknown }> };
    expect(kw.messages[0].content).toEqual([
      { type: "text", text: "CONTEXTO DEL PROYECTO", cache_control: { type: "ephemeral", ttl: "1h" } },
      { type: "text", text: "TURNO" },
    ]);
    // el system cacheado a 1 hora (su ultimo bloque fijo lleva la marca)
    expect(kw.system.some((b) => JSON.stringify(b.cache_control) === JSON.stringify({ type: "ephemeral", ttl: "1h" }))).toBe(true);
  });

  it("sin contexto, el turno va como siempre (texto plano)", async () => {
    const { create, client } = clienteSecuencia([{ stop: "end_turn", texto: "ok" }]);
    await llamarClaude(client, "P", "TURNO", "claude-haiku-4-5", usoVacio());
    expect((create.mock.calls[0][0] as { messages: Array<{ content: unknown }> }).messages[0].content).toBe("TURNO");
  });
});
