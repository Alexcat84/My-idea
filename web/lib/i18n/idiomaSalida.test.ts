/**
 * i18n F5 (DISENO §5): la regla de IDIOMA DE SALIDA. Los prompts son fijos y
 * en español (el caché de Anthropic depende de que su prefijo no cambie); el
 * idioma de la idea viaja en un SEGUNDO bloque de sistema, después del
 * cacheado. En español no se agrega nada: el prompt queda como siempre.
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { bloquesDeSistema, reglaIdiomaSalida } from "./idiomaSalida";
import { llamarClaude, llamarClaudeConversacion, usoVacio } from "../costmeter";

describe("reglaIdiomaSalida", () => {
  it("en español no hay regla", () => {
    expect(reglaIdiomaSalida("es")).toBeNull();
    expect(reglaIdiomaSalida(undefined)).toBeNull();
  });

  it("nombra el idioma en español y en su escritura, y dice que el material viene en español", () => {
    const r = reglaIdiomaSalida("ko")!;
    expect(r).toMatch(/^IDIOMA DE SALIDA: coreano \(한국어\)\./);
    expect(r).toContain("los nodos que recibes están en español: úsalos como fuente y exprésalos en coreano (한국어)");
  });

  it("los rótulos fijos se listan para escribirse tal cual, en español", () => {
    const r = reglaIdiomaSalida("ru", ["## Etapa N:", "**Esta semana:**"])!;
    expect(r).toContain("«## Etapa N:», «**Esta semana:**»");
    expect(r).toMatch(/tal cual, en español/);
  });
});

describe("bloquesDeSistema", () => {
  it("español: un solo bloque, cacheado (idéntico a antes de F5)", () => {
    expect(bloquesDeSistema("PROMPT", "es")).toEqual([{ type: "text", text: "PROMPT", cache_control: { type: "ephemeral" } }]);
  });
  it("otro idioma: el cacheado primero y la regla después, sin marca de caché", () => {
    const b = bloquesDeSistema("PROMPT", "ar");
    expect(b).toHaveLength(2);
    expect(b[0]).toEqual({ type: "text", text: "PROMPT", cache_control: { type: "ephemeral" } });
    expect(b[1].text).toMatch(/^IDIOMA DE SALIDA: árabe/);
    expect(b[1]).not.toHaveProperty("cache_control");
  });
});

function clienteFalso() {
  const create = vi.fn(async () => ({
    content: [{ type: "text", text: "hola" }],
    usage: { input_tokens: 1, output_tokens: 1 },
  }));
  return { create, client: { messages: { create } } as unknown as Anthropic };
}

describe("llamarClaude y llamarClaudeConversacion llevan el idioma de salida", () => {
  it("llamarClaude con idiomaSalida ko manda los dos bloques", async () => {
    const { create, client } = clienteFalso();
    await llamarClaude(client, "PROMPT", "u", "m", usoVacio(), { idiomaSalida: "ko" });
    const sistema = (create.mock.calls[0] as unknown as [{ system: Array<{ text: string }> }])[0].system;
    expect(sistema).toHaveLength(2);
    expect(sistema[1].text).toMatch(/coreano/);
  });
  it("llamarClaude sin idiomaSalida: como siempre", async () => {
    const { create, client } = clienteFalso();
    await llamarClaude(client, "PROMPT", "u", "m", usoVacio());
    const sistema = (create.mock.calls[0] as unknown as [{ system: unknown[] }])[0].system;
    expect(sistema).toHaveLength(1);
  });
  it("llamarClaudeConversacion con idiomaSalida hi manda los dos bloques", async () => {
    const { create, client } = clienteFalso();
    await llamarClaudeConversacion(client, "PROMPT", [], "u", "m", usoVacio(), { idiomaSalida: "hi" });
    const sistema = (create.mock.calls[0] as unknown as [{ system: Array<{ text: string }> }])[0].system;
    expect(sistema[1].text).toMatch(/hindi/);
  });
});

// DISENO §5: cada prompt que escribe texto para la persona termina con la regla
// de IDIOMA DE SALIDA (los que producen JSON interno no cambian).
import * as P from "../prompts";

describe("los prompts que escriben para la persona terminan con la regla de idioma", () => {
  const conRegla = [
    "SYSTEM_INTERPRETE_MULTI",
    "SYSTEM_PREGUNTA_DIRIGIDA",
    "SYSTEM_PLAN",
    "SYSTEM_ESTADO_VIVO",
    "SYSTEM_ORGANIZADOR",
    "SYSTEM_REPORTE",
    "SYSTEM_DIAGNOSTICO_MUNDO",
    "SYSTEM_CLASIFICAR_OFERTA",
    "SYSTEM_REFORMULADOR_PROTECCION",
  ] as const;
  const sinRegla = ["SYSTEM_CLASIFICACION", "SYSTEM_PUERTA_AVANZADA", "SYSTEM_PROFUNDIZAR", "SYSTEM_JUEZ_SESION", "SYSTEM_ENLACE_PROTECCION", "SYSTEM_ESTIMACION_BANDA"] as const;

  it.each(conRegla)("%s", (nombre) => {
    const texto = (P as Record<string, unknown>)[nombre] as string;
    expect(texto.trimEnd()).toMatch(/IDIOMA DE SALIDA: espanol, salvo que un bloque posterior[\s\S]*manda sobre estas reglas\.$/);
  });
  it.each(sinRegla)("%s (JSON interno) no la lleva", (nombre) => {
    const texto = (P as Record<string, unknown>)[nombre] as string;
    expect(texto).not.toContain("IDIOMA DE SALIDA");
  });
});
