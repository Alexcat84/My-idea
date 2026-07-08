// Fase 3.0: paridad de comportamiento contra engine/test_conversacion_incremental.py
// -- mismo contrato (el marcador cache_control vive SOLO en el ultimo
// bloque enviado, se mueve turno a turno; una llamada fallida no debe
// producir ningun historial nuevo), pero expresado de forma inmutable:
// llamarClaudeConversacion devuelve un historialMensajes NUEVO en vez de
// mutar el array de entrada (estilo del resto de costmeter.ts).
import { describe, expect, it, vi } from "vitest";
import { costoAcumuladoUsd, llamarClaudeConversacion, usoVacio } from "./costmeter";

function clienteFalso(respuestas: unknown[]) {
  const llamadas: unknown[] = [];
  let idx = 0;
  return {
    cliente: {
      messages: {
        create: vi.fn(async (kwargs: unknown) => {
          llamadas.push(kwargs);
          const item = respuestas[idx++];
          if (item instanceof Error) throw item;
          return item;
        }),
      },
    },
    llamadas,
  };
}

function msgFalso(texto: string, usage: Partial<{ cache_read: number; cache_write: number }> = {}) {
  return {
    content: [{ type: "text", text: texto }],
    usage: {
      input_tokens: 100,
      output_tokens: 20,
      cache_read_input_tokens: usage.cache_read ?? 0,
      cache_creation_input_tokens: usage.cache_write ?? 0,
    },
  };
}

describe("llamarClaudeConversacion: dos llamadas exitosas seguidas", () => {
  it("el historial crece de a 2, cache_control se mueve correctamente turno a turno", async () => {
    const { cliente, llamadas } = clienteFalso([
      msgFalso('{"ok": 1}', { cache_write: 500 }),
      msgFalso('{"ok": 2}', { cache_read: 500 }),
    ]);

    let acumulado = usoVacio();
    const r1 = await llamarClaudeConversacion(
      cliente as never, "system-x", [], "turno 1", "modelo-fake", acumulado, { componente: "turnos" }
    );
    expect(r1.texto).toBe('{"ok": 1}');
    expect(r1.historialMensajes).toHaveLength(2);
    expect(r1.historialMensajes[0].role).toBe("user");
    expect(r1.historialMensajes[1].role).toBe("assistant");
    const turno1 = r1.historialMensajes[0] as { content: Array<{ cache_control?: unknown }> };
    expect(turno1.content.at(-1)?.cache_control).toEqual({ type: "ephemeral" });
    acumulado = r1.acumulado;

    const r2 = await llamarClaudeConversacion(
      cliente as never, "system-x", r1.historialMensajes, "turno 2", "modelo-fake", acumulado, { componente: "turnos" }
    );
    expect(r2.texto).toBe('{"ok": 2}');
    expect(r2.historialMensajes).toHaveLength(4);
    const turno1Despues = r2.historialMensajes[0] as { content: Array<{ cache_control?: unknown }> };
    const turno2 = r2.historialMensajes[2] as { content: Array<{ cache_control?: unknown }> };
    expect(turno1Despues.content.at(-1)?.cache_control).toBeUndefined();
    expect(turno2.content.at(-1)?.cache_control).toEqual({ type: "ephemeral" });

    // La 2a llamada a la API debio incluir los 2 mensajes previos + el nuevo turno = 3.
    const segundoRequest = llamadas[1] as { messages: unknown[] };
    expect(segundoRequest.messages).toHaveLength(3);

    // r1.historialMensajes (el array devuelto en la 1a llamada) nunca se muta por la 2a.
    expect(r1.historialMensajes).toHaveLength(2);
  });
});

describe("llamarClaudeConversacion: una llamada fallida no produce historial nuevo", () => {
  it("propaga el error y no hay historial actualizado que comprometer", async () => {
    const { cliente } = clienteFalso([new Error("fallo de red simulado")]);
    const historialPrevio = [
      { role: "user" as const, content: [{ type: "text" as const, text: "turno 1" }] },
      { role: "assistant" as const, content: '{"ok": 1}' },
    ];
    await expect(
      llamarClaudeConversacion(cliente as never, "system-x", historialPrevio, "turno 3", "modelo-fake", usoVacio())
    ).rejects.toThrow("fallo de red simulado");
    // El array previo, al ser inmutable, sigue exactamente igual (nunca se le pidio mutarse).
    expect(historialPrevio).toHaveLength(2);
  });
});

describe("llamarClaudeConversacion: presupuesto excedido corta ANTES de llamar a la API", () => {
  it("no llama a create() si el acumulado ya supera el presupuesto", async () => {
    const { cliente } = clienteFalso([msgFalso("no deberia usarse")]);
    let acumulado = usoVacio();
    // Registra un costo que ya supera el presupuesto por defecto ($0.30) a mano:
    // MODEL_HAIKU pin=1.00 -> 400,000 in tokens = $0.40
    acumulado = {
      uso: { "claude-haiku-4-5": { in: 400_000, out: 0, llamadas: 1, cache_read: 0, cache_write: 0 } },
      uso_por_componente: {},
      presupuesto_excedido: false,
    };
    expect(costoAcumuladoUsd(acumulado)).toBeGreaterThan(0.3);
    await expect(
      llamarClaudeConversacion(cliente as never, "system-x", [], "turno", "claude-haiku-4-5", acumulado)
    ).rejects.toThrow(/presupuesto/);
    expect(cliente.messages.create).not.toHaveBeenCalled();
  });
});
