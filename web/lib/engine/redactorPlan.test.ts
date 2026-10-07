// La falla nueva de las respuestas cortadas, en el redactor del plan (contexto de
// la entrevista, 28 sep 2026): un plan cortado por el tope de tokens no se trata
// como completo. Ese intento se registra (se pago), el siguiente dobla el tope, y
// si se agotan los intentos se falla con aviso. Nunca se entrega un plan cortado.
import type Anthropic from "@anthropic-ai/sdk";
import { describe, expect, it, vi } from "vitest";
import { usoVacio } from "../costmeter";
import { generarTextoPlan } from "./redactorPlan";

function streamFalso(texto: string, stop: string) {
  return {
    on: () => undefined,
    finalMessage: async () => ({
      content: [{ type: "text", text: texto }],
      stop_reason: stop,
      usage: { input_tokens: 10, output_tokens: 10 },
    }),
  };
}

const PAYLOAD = { material: [] };
const PREP = { payload: PAYLOAD } as never;

describe("generarTextoPlan: nunca entrega un plan cortado", () => {
  it("un intento cortado se registra y el siguiente dobla el tope", async () => {
    const stream = vi
      .fn()
      .mockReturnValueOnce(streamFalso("plan cort", "max_tokens"))
      .mockReturnValueOnce(streamFalso("plan completo", "end_turn"));
    const client = { messages: { stream } } as unknown as Anthropic;
    const reinicios = vi.fn();
    const r = await generarTextoPlan(client, PREP, usoVacio(), () => undefined, reinicios, null, { backoffsMs: [0, 0, 0] });
    expect(r.rawTexto).toBe("plan completo");
    expect(stream.mock.calls[0][0].max_tokens).toBe(5000);
    expect(stream.mock.calls[1][0].max_tokens).toBe(10000);
    expect(reinicios).toHaveBeenCalledTimes(1);
    expect(r.acumulado.llamadas!.map((l) => l.stop_reason)).toEqual(["max_tokens", "end_turn"]);
  });

  it("si todos los intentos salen cortados, falla con aviso", async () => {
    const stream = vi.fn(() => streamFalso("cortado", "max_tokens"));
    const client = { messages: { stream } } as unknown as Anthropic;
    await expect(
      generarTextoPlan(client, PREP, usoVacio(), () => undefined, () => undefined, null, { backoffsMs: [0, 0, 0] })
    ).rejects.toThrow(/cortad/);
  });

  it("el contexto del proyecto viaja en su bloque con cache de 1 hora, antes del material", async () => {
    const stream = vi.fn(() => streamFalso("ok", "end_turn"));
    const client = { messages: { stream } } as unknown as Anthropic;
    await generarTextoPlan(client, PREP, usoVacio(), () => undefined, () => undefined, null, {
      backoffsMs: [0],
      contexto: "MEMORIA",
    });
    expect((stream.mock.calls[0] as unknown as [{ messages: Array<{ content: unknown }> }])[0].messages[0].content).toEqual([
      { type: "text", text: "MEMORIA", cache_control: { type: "ephemeral", ttl: "1h" } },
      { type: "text", text: JSON.stringify(PAYLOAD) },
    ]);
  });

  it("cada intento registra si llevo el contexto (condicion de contexto de la prueba de coherencia)", async () => {
    const stream = vi.fn(() => streamFalso("ok", "end_turn"));
    const client = { messages: { stream } } as unknown as Anthropic;
    const con = await generarTextoPlan(client, PREP, usoVacio(), () => undefined, () => undefined, null, { backoffsMs: [0], contexto: "MEMORIA" });
    expect(con.acumulado.llamadas![0].con_contexto).toBe(true);
    const sin = await generarTextoPlan(client, PREP, usoVacio(), () => undefined, () => undefined, null, { backoffsMs: [0] });
    expect(sin.acumulado.llamadas![0].con_contexto).toBe(false);
  });
});
