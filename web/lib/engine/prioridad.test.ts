/**
 * Contexto completo en cada llamada (docs/auditoria_final/informes/estado_memoria_contexto.md, fila 2, propuesta a):
 * la traduccion de la prioridad declarada al español (solo si la idea no esta en español) es una llamada a la IA y,
 * como todas, lleva el contexto de la sesion en su bloque con cache de 1 hora. Antes iba con contexto null.
 * Modelo y brujula simulados: ninguna llamada real, ni a Anthropic ni al indice semantico.
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { usoVacio } from "../costmeter";

vi.mock("../compass", async (importOriginal) => ({
  ...(await importOriginal<typeof import("../compass")>()),
  puntuadorContra: vi.fn(async () => () => 0.5),
}));

import { puntuadorDePrioridad } from "./prioridad";

function cliente(texto: string) {
  const create = vi.fn(async (_req: unknown) => ({
    content: [{ type: "text", text: texto }],
    usage: { input_tokens: 10, output_tokens: 5 },
    stop_reason: "end_turn",
  }));
  return { create, client: { messages: { create } } as unknown as Anthropic };
}

const CONTEXTO = "CONTEXTO DEL PROYECTO (prueba)\nIdea original: vender pan en mi barrio";

describe("puntuadorDePrioridad lleva el contexto de la sesion", () => {
  it("en una idea en coreano, la traduccion de la prioridad viaja con el contexto en su bloque de 1 hora", async () => {
    const { create, client } = cliente("dirigir a mis dos empleados");
    const r = await puntuadorDePrioridad(client, "두 직원을 이끌고 싶어요", "ko", usoVacio(), {}, CONTEXTO);
    expect(r.puntuar).not.toBeNull();
    expect(create).toHaveBeenCalledTimes(1);
    const req = create.mock.calls[0][0] as { messages: Array<{ content: unknown }> };
    expect(req.messages[0].content).toEqual([
      { type: "text", text: CONTEXTO, cache_control: { type: "ephemeral", ttl: "1h" } },
      { type: "text", text: "두 직원을 이끌고 싶어요" },
    ]);
  });

  it("en español no llama a la IA (no hay nada que traducir)", async () => {
    const { create, client } = cliente("x");
    await puntuadorDePrioridad(client, "dirigir a mis dos empleados", "es", usoVacio(), {}, CONTEXTO);
    expect(create).not.toHaveBeenCalled();
  });
});
