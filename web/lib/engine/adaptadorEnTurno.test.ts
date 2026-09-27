/**
 * CONSTRUCCION 2 (decision del fundador, 28 sep 2026): el adaptador dentro del turno. Antes (D3, i18n F5) la cacheada
 * solo se traducia fuera del español y en español salia cruda. Ahora toda pregunta que sale de la cache pasa por el
 * adaptador, en cualquier idioma: la dice a esta persona y en el idioma de su idea (sustituye a la traduccion). Si la
 * IA falla, sale la neutral del nodo; si aun no la tiene, su base, y el evento lo dice.
 * Y la pregunta genérica (nodo sin cacheada) nombra el tema por su ETIQUETA, nunca por el titulo_concepto (AGENTS.md:
 * la etiqueta enamora).
 */
import { beforeEach, describe, expect, it, vi } from "vitest";

const interpretarMultiSaltoFalso = vi.fn();
vi.mock("./interprete", () => ({
  interpretarMultiSalto: (...args: unknown[]) => interpretarMultiSaltoFalso(...args),
}));

import type Anthropic from "@anthropic-ai/sdk";
import { usoVacio } from "../costmeter";
import { cargarFamilies } from "../readiness";
import { cargarGrafo, cargarPreguntasCache, obtenerPregunta } from "./graph";
import { avanzarTurno, estadoInicial } from "./recorrido";
import { MOTOR } from "../i18n/mensajes/motor";
import { interpolar } from "../i18n/interpolar";
import { ETIQUETAS_RIEL } from "../i18n/etiquetasRiel";

const graph = cargarGrafo();
const families = cargarFamilies();
const preguntasCache = cargarPreguntasCache();

function cliente(texto: string | Error) {
  const create = vi.fn(async (_req: unknown) => {
    if (texto instanceof Error) throw texto;
    return { content: [{ type: "text", text: texto }], usage: { input_tokens: 10, output_tokens: 5 }, stop_reason: "end_turn" };
  });
  return { create, client: { messages: { create } } as unknown as Anthropic };
}

const salidaAdaptador = (pregunta: string) => JSON.stringify({ pregunta, busca: "como separa las capas de su diseño" });

describe("avanzarTurno pasa la pregunta cacheada por el adaptador", () => {
  beforeEach(() => interpretarMultiSaltoFalso.mockReset());
  const nid = "mapeo_capas_diseno";

  function avance() {
    interpretarMultiSaltoFalso.mockResolvedValueOnce({
      resultado: {
        accion: "avanzar", camino: [nid], esSalto: false, preguntaNecesaria: true, preguntaAdaptada: null,
        repregunta: null, perfilUpdate: null, prioridadDeclarada: null, numerosDetectados: null,
        tipoOfertaDetectado: null, unidadVentaDetectada: null,
      },
      acumulado: usoVacio(),
      historialMensajes: [],
    });
  }

  it("idea en coreano: la cacheada (en español) llega adaptada y en coreano, y queda como pendiente", async () => {
    avance();
    const { client, create } = cliente(salidaAdaptador("디자인 층을 어떻게 나눴나요?"));
    const estado = estadoInicial({ actualId: "design_thinking_fundamentos", perfilSesion: "p", textoOriginal: "t", idioma: "ko" });
    const r = await avanzarTurno({ client, graph, families, preguntasCache, estado, respuestaUsuario: null, acumulado: usoVacio(), dbSessionId: "s" });
    if (r.tipo !== "pregunta") throw new Error("esperaba pregunta");
    expect(preguntasCache[nid]?.pregunta).toBeTruthy();
    expect(r.pregunta).toBe("디자인 층을 어떻게 나눴나요?");
    expect(r.estado.preguntaPendiente).toBe("디자인 층을 어떻게 나눴나요?");
    expect(r.estado.ultimasPreguntas.at(-1)).toBe("디자인 층을 어떻게 나눴나요?");
    const sistema = (create.mock.calls[0][0] as { system: Array<{ text: string }> }).system;
    expect(sistema.at(-1)!.text).toMatch(/^IDIOMA DE SALIDA: coreano/);
  });

  it("idea en español: la cacheada ya no sale cruda, tambien se adapta", async () => {
    avance();
    const { create, client } = cliente(salidaAdaptador("¿Cómo separas hoy las capas de tu taller?"));
    const estado = estadoInicial({ actualId: "design_thinking_fundamentos", perfilSesion: "p", textoOriginal: "t" });
    const r = await avanzarTurno({ client, graph, families, preguntasCache, estado, respuestaUsuario: null, acumulado: usoVacio(), dbSessionId: "s" });
    if (r.tipo !== "pregunta") throw new Error("esperaba pregunta");
    expect(create).toHaveBeenCalledTimes(1);
    expect(r.pregunta).toBe("¿Cómo separas hoy las capas de tu taller?");
    expect(r.estado.fallbackEvents.at(-1)).toMatchObject({ tipo: "adaptacion_pregunta", nodo: nid, de: preguntasCache[nid]!.pregunta, salida: "adaptada" });
  });

  it("si la IA falla, el turno sigue: sale la salida segura y el evento dice cual", async () => {
    avance();
    const { client } = cliente(new Error("sin red"));
    const estado = estadoInicial({ actualId: "design_thinking_fundamentos", perfilSesion: "p", textoOriginal: "t" });
    const r = await avanzarTurno({ client, graph, families, preguntasCache, estado, respuestaUsuario: null, acumulado: usoVacio(), dbSessionId: "s" });
    if (r.tipo !== "pregunta") throw new Error("esperaba pregunta");
    const entrada = preguntasCache[nid]!;
    const neutral = typeof entrada.pregunta_neutral === "string" ? entrada.pregunta_neutral : null;
    expect(r.pregunta).toBe(neutral ?? entrada.pregunta);
    expect(r.estado.fallbackEvents.at(-1)).toMatchObject({
      tipo: "adaptacion_pregunta",
      salida: neutral ? "neutral" : "base_sin_neutral",
      motivo: "sin red",
    });
  });
});

describe("la pregunta genérica nombra el tema por su etiqueta", () => {
  const sinCache = Object.keys(graph).find((k) => !graph[k].deprecado && !preguntasCache[k]?.pregunta && graph[k].etiqueta_arbol)!;

  it("en español, con la etiqueta del grafo (no el título técnico)", () => {
    expect(obtenerPregunta(sinCache, graph[sinCache], preguntasCache)).toBe(
      interpolar(MOTOR.es.preguntaGenerica, { titulo: graph[sinCache].etiqueta_arbol! })
    );
  });

  it("en inglés, con la etiqueta derivada", () => {
    const antes = ETIQUETAS_RIEL.en[sinCache];
    ETIQUETAS_RIEL.en[sinCache] = "Your Topic In English";
    try {
      expect(obtenerPregunta(sinCache, graph[sinCache], preguntasCache, "en")).toBe(
        interpolar(MOTOR.en.preguntaGenerica, { titulo: "Your Topic In English" })
      );
    } finally {
      if (antes === undefined) delete ETIQUETAS_RIEL.en[sinCache];
      else ETIQUETAS_RIEL.en[sinCache] = antes;
    }
  });
});
