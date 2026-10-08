/**
 * Decisión del fundador (corrida final, 8 oct 2026): se generan las VERSIONES NEUTRALES de TODAS las preguntas, base y
 * de entrada. La pregunta de entrada de una puerta guarda la suya en un campo aparte de la caché
 * (`pregunta_entrada_neutral`, la entrada sigue intacta) y es su SALIDA SEGURA: si la adaptación falla, tarda o no
 * pasa las comprobaciones, sale la neutral de la entrada. Sin ella, la entrada tal cual (como hasta hoy).
 *
 * Todo con clientes falsos: ninguna llamada a la API real.
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { adaptarPregunta, adaptarResultadoTurno } from "./adaptadorPregunta";
import { usoVacio } from "../costmeter";
import type { Grafo, PreguntasCache } from "./graph";
import type { EventoInterprete } from "./interprete";

const BASE = "¿Qué le dirías a tu propio jefe si te pide un informe de avance?";
const NEUTRAL = "¿Qué le contarías a quien sigue tu avance si te pide un informe?";
const ENTRADA = "¿Tu equipo ya sabe a quién acudir cuando algo se atasca?";
const ENTRADA_NEUTRAL = "¿Quién sabe hoy a quién acudir cuando algo se atasca en tu proyecto?";
const PLANTILLA = "¿En qué punto está hoy tu idea con este paso?";

function clienteFalso(respuesta: string | Error) {
  const create = vi.fn(async (_req: unknown) => {
    if (respuesta instanceof Error) throw respuesta;
    return { usage: { input_tokens: 500, output_tokens: 80 }, stop_reason: "end_turn", content: [{ type: "text", text: respuesta }] };
  });
  return { client: { messages: { create } } as unknown as Anthropic, create };
}
const json = (pregunta: string) => JSON.stringify({ pregunta, busca: "a quien acude cuando algo se atasca" });

describe("adaptarPregunta con una pregunta de entrada", () => {
  const entrada = { nodo: "p1", base: ENTRADA, neutral: ENTRADA_NEUTRAL, plantilla: PLANTILLA, siguientes: [], esEntrada: true };

  it("si la llamada falla, sale la NEUTRAL de la entrada, no la entrada cruda", async () => {
    const { client } = clienteFalso(new Error("529 overloaded"));
    const r = await adaptarPregunta(client, entrada, usoVacio(), { idiomaSalida: "es", contexto: null });
    expect(r).toMatchObject({ pregunta: ENTRADA_NEUTRAL, salida: "neutral", fallo: "529 overloaded" });
  });

  it("si la adaptada no pasa las comprobaciones, también sale la neutral de la entrada", async () => {
    const { client } = clienteFalso("sin json");
    const r = await adaptarPregunta(client, entrada, usoVacio(), { idiomaSalida: "es", contexto: null });
    expect(r).toMatchObject({ pregunta: ENTRADA_NEUTRAL, salida: "neutral", fallo: "no_json" });
  });

  it("una entrada sin neutral todavía: sale la entrada tal cual (nunca la plantilla genérica)", async () => {
    const { client } = clienteFalso(new Error("timeout"));
    const r = await adaptarPregunta(client, { ...entrada, neutral: null }, usoVacio(), { idiomaSalida: "es", contexto: null });
    expect(r).toMatchObject({ pregunta: ENTRADA, salida: "entrada", fallo: "timeout" });
  });
});

describe("adaptarResultadoTurno con la pregunta de entrada de una puerta", () => {
  const graph = {
    n0: { titulo_concepto: "Inicio", etiqueta_arbol: "Empieza por aquí", dominio: "core" },
    p1: { titulo_concepto: "Puerta", etiqueta_arbol: "Ordena a quién acudir", dominio: "primer_equipo" },
  } as unknown as Grafo;
  const cache: PreguntasCache = {
    p1: { pregunta: BASE, pregunta_neutral: NEUTRAL, pregunta_entrada: ENTRADA, pregunta_entrada_neutral: ENTRADA_NEUTRAL, candidatos: [] },
  };
  const turno = (pregunta: string) => ({
    tipo: "pregunta" as const,
    pregunta,
    acumulado: usoVacio(),
    estado: { ruta: ["n0", "p1"], idioma: "es", preguntaPendiente: pregunta, ultimasPreguntas: [pregunta], fallbackEvents: [] as EventoInterprete[] },
  });

  it("si el adaptador falla, la entrada sale por su neutral de entrada, no por la neutral de la base", async () => {
    const { client } = clienteFalso(new Error("timeout"));
    const r = await adaptarResultadoTurno(client, turno(ENTRADA), { graph, preguntasCache: cache, idiomaPlantilla: "es" });
    expect(r.pregunta).toBe(ENTRADA_NEUTRAL);
    expect(r.estado.fallbackEvents[0]).toMatchObject({ de: ENTRADA, a: ENTRADA_NEUTRAL, salida: "neutral" });
  });

  it("la neutral de entrada que ya se mostró también se adapta, con la entrada como base", async () => {
    const { client, create } = clienteFalso(json("¿A quién acudes cuando algo se atasca?"));
    const r = await adaptarResultadoTurno(client, turno(ENTRADA_NEUTRAL), { graph, preguntasCache: cache, idiomaPlantilla: "es" });
    expect(create).toHaveBeenCalledTimes(1);
    const content = (create.mock.calls[0][0] as { messages: Array<{ content: string | Array<{ text: string }> }> }).messages[0].content;
    const enviado = JSON.parse(typeof content === "string" ? content : content[content.length - 1].text);
    expect(enviado.pregunta_base).toBe(ENTRADA);
    expect(r.pregunta).toBe("¿A quién acudes cuando algo se atasca?");
  });
});

// SEGURIDAD MÁXIMA DE SENTIDO (decisión del fundador, 8 oct 2026): las neutrales salen por niveles. Si la edición
// mínima no supera todas las comprobaciones, la neutral queda vacía con nivel 3 y se usa la PLANTILLA SEGURA. Para una
// entrada en nivel 3 eso cambia lo de antes: nunca la entrada tal cual, la plantilla.
describe("entrada en nivel 3 (la edición mínima no pasó): plantilla segura", () => {
  const graph = {
    n0: { titulo_concepto: "Inicio", etiqueta_arbol: "Empieza por aquí", dominio: "core" },
    p1: { titulo_concepto: "Puerta", etiqueta_arbol: "Ordena a quién acudir", dominio: "primer_equipo" },
  } as unknown as Grafo;
  const cache: PreguntasCache = {
    p1: { pregunta: BASE, pregunta_neutral: NEUTRAL, pregunta_neutral_nivel: 2, pregunta_entrada: ENTRADA, pregunta_entrada_neutral_nivel: 3, candidatos: [] },
  };
  const turno = (pregunta: string) => ({
    tipo: "pregunta" as const,
    pregunta,
    acumulado: usoVacio(),
    estado: { ruta: ["n0", "p1"], idioma: "es", preguntaPendiente: pregunta, ultimasPreguntas: [pregunta], fallbackEvents: [] as EventoInterprete[] },
  });

  it("si el adaptador falla, sale la plantilla, no la entrada cruda", async () => {
    const { client } = clienteFalso(new Error("timeout"));
    const r = await adaptarResultadoTurno(client, turno(ENTRADA), { graph, preguntasCache: cache, idiomaPlantilla: "es" });
    expect(r.estado.fallbackEvents[0]).toMatchObject({ de: ENTRADA, salida: "plantilla_neutral" });
    expect(r.pregunta).not.toBe(ENTRADA);
  });

  it("adaptarPregunta con plantillaSegura: la plantilla", async () => {
    const { client } = clienteFalso(new Error("timeout"));
    const r = await adaptarPregunta(
      client,
      { nodo: "p1", base: ENTRADA, neutral: null, plantilla: PLANTILLA, siguientes: [], esEntrada: true, plantillaSegura: true },
      usoVacio(),
      { idiomaSalida: "es", contexto: null }
    );
    expect(r).toMatchObject({ pregunta: PLANTILLA, salida: "plantilla_neutral" });
  });
});
