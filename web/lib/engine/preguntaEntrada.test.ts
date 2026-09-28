/**
 * Decisión del fundador (28 sep 2026, punto 3): cada puerta de los mundos recibe una PREGUNTA DE ENTRADA propia, en un
 * campo aparte de la caché (`pregunta_entrada`), que parte del concepto de la puerta y de la situación que la persona
 * cuenta. La pregunta base NO se toca (Principio 2): se escribió para elegir entre los siguientes y por eso mira al
 * concepto que viene. El adaptador trata la pregunta de entrada igual que las demás; su salida segura es la propia
 * pregunta de entrada, que se verificó a ciegas sin papeles supuestos.
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { usoVacio } from "../costmeter";
import { cargarGrafo, obtenerPregunta, preguntaDeEntrada, type PreguntasCache } from "./graph";
import { adaptarResultadoTurno } from "./adaptadorPregunta";

const graph = cargarGrafo();
const NODO = "mapeo_capas_diseno";
const BASE = "Más allá de las capas, ¿qué parte de tu diseño quieres revisar primero?";
const ENTRADA = "¿Cómo tienes hoy separadas las partes de lo que diseñas, y cuál te cuesta más cambiar sin tocar las demás?";
const cacheConEntrada: PreguntasCache = { [NODO]: { pregunta: BASE, candidatos: [], pregunta_entrada: ENTRADA } };
const cacheSinEntrada: PreguntasCache = { [NODO]: { pregunta: BASE, candidatos: [] } };

function cliente(texto: string | Error) {
  const create = vi.fn(async (_req: unknown) => {
    if (texto instanceof Error) throw texto;
    return { content: [{ type: "text", text: texto }], usage: { input_tokens: 10, output_tokens: 5 }, stop_reason: "end_turn" };
  });
  return { create, client: { messages: { create } } as unknown as Anthropic };
}

function turno(pregunta: string) {
  return {
    tipo: "pregunta" as const,
    pregunta,
    acumulado: usoVacio(),
    estado: { ruta: [NODO], preguntaPendiente: pregunta, ultimasPreguntas: [pregunta], fallbackEvents: [] },
  };
}

describe("la pregunta de entrada de una puerta", () => {
  it("sale la de entrada cuando la puerta la tiene; la base no cambia", () => {
    expect(preguntaDeEntrada(NODO, graph[NODO], cacheConEntrada)).toBe(ENTRADA);
    expect(obtenerPregunta(NODO, graph[NODO], cacheConEntrada)).toBe(BASE);
  });

  it("sin pregunta de entrada, sale la base como hasta ahora", () => {
    expect(preguntaDeEntrada(NODO, graph[NODO], cacheSinEntrada)).toBe(BASE);
  });

  it("el adaptador la trata igual que las demás: le llega como la pregunta a decir", async () => {
    const { client, create } = cliente(JSON.stringify({ pregunta: "¿Qué parte de tu diseño separaste primero?", busca: "como separa las partes" }));
    const r = await adaptarResultadoTurno(client, turno(ENTRADA), { graph, preguntasCache: cacheConEntrada, idiomaPlantilla: "es" });
    expect(create).toHaveBeenCalledTimes(1);
    expect(JSON.stringify(create.mock.calls[0][0])).toContain(ENTRADA);
    expect(r.pregunta).toBe("¿Qué parte de tu diseño separaste primero?");
  });

  it("si la IA falla, sale la propia pregunta de entrada, nunca la base", async () => {
    const { client } = cliente(new Error("caida"));
    const r = await adaptarResultadoTurno(client, turno(ENTRADA), { graph, preguntasCache: cacheConEntrada, idiomaPlantilla: "es" });
    expect(r.pregunta).toBe(ENTRADA);
    const ev = r.estado.fallbackEvents.at(-1) as unknown as { tipo: string; salida: string; de: string };
    expect(ev.tipo).toBe("adaptacion_pregunta");
    expect(ev.salida).toBe("entrada");
    expect(ev.de).toBe(ENTRADA);
  });
});
