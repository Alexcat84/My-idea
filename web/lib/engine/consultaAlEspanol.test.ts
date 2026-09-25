/**
 * El remedio de F1 (i18n F5; docs/i18n/F1_BUSCADOR.md): el índice semántico
 * está hecho con el español de los nodos. Una consulta en otro idioma recupera
 * peor (en inglés, 2,80 candidatos sobre el umbral contra 7,35 en español);
 * traducida al español con Haiku, vuelve a 7,40. Si la traducción falla, se
 * busca con el original y queda registrado.
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { consultaAlEspanol } from "./consultaAlEspanol";
import { usoVacio } from "../costmeter";
import { SYSTEM_CONSULTA_AL_ESPANOL } from "../prompts";

function cliente(texto: string | Error) {
  const create = vi.fn(async () => {
    if (texto instanceof Error) throw texto;
    return { content: [{ type: "text", text: texto }], usage: { input_tokens: 10, output_tokens: 5 } };
  });
  return { create, client: { messages: { create } } as unknown as Anthropic };
}

describe("consultaAlEspanol", () => {
  it("en español (o sin idioma) no llama a la IA", async () => {
    const { create, client } = cliente("x");
    expect(await consultaAlEspanol(client, "vendo pan", "es", usoVacio())).toMatchObject({ consulta: "vendo pan", fallo: false });
    expect(await consultaAlEspanol(client, "vendo pan", null, usoVacio())).toMatchObject({ consulta: "vendo pan", fallo: false });
    expect(create).not.toHaveBeenCalled();
  });

  it("en coreano, traduce con el prompt medido en F1 (sin regla de idioma: la salida es español)", async () => {
    const { create, client } = cliente("quiero vender pan en mi barrio");
    const r = await consultaAlEspanol(client, "우리 동네에서 빵을 팔고 싶어요", "ko", usoVacio());
    expect(r).toMatchObject({ consulta: "quiero vender pan en mi barrio", fallo: false });
    const sistema = (create.mock.calls[0] as unknown as [{ system: Array<{ text: string }> }])[0].system;
    expect(sistema).toHaveLength(1);
    expect(sistema[0].text).toBe(SYSTEM_CONSULTA_AL_ESPANOL);
  });

  it("si falla, busca con el original y lo marca", async () => {
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    const r = await consultaAlEspanol(cliente(new Error("sin red")).client, "빵", "ko", usoVacio());
    expect(r).toMatchObject({ consulta: "빵", fallo: true });
    expect(log).toHaveBeenCalled();
    log.mockRestore();
  });
});
