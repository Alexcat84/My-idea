/**
 * D3 (i18n F5): fuera del español, las preguntas del grafo las adapta la IA.
 * Las cacheadas están en español; si una llega cruda a una idea en otro idioma,
 * Haiku la expresa en ese idioma (misma intención, una sola pregunta). Si la IA
 * falla, queda la cacheada: mejor una pregunta en español que ninguna.
 * Y la pregunta genérica (nodo sin cacheada) nombra el tema por su ETIQUETA,
 * nunca por el titulo_concepto (AGENTS.md: la etiqueta enamora).
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
import { preguntaEnIdioma } from "./preguntaEnIdioma";
import { avanzarTurno, estadoInicial } from "./recorrido";
import { MOTOR } from "../i18n/mensajes/motor";
import { interpolar } from "../i18n/interpolar";
import { ETIQUETAS_RIEL } from "../i18n/etiquetasRiel";

const graph = cargarGrafo();
const families = cargarFamilies();
const preguntasCache = cargarPreguntasCache();

function cliente(texto: string | Error) {
  const create = vi.fn(async () => {
    if (texto instanceof Error) throw texto;
    return { content: [{ type: "text", text: texto }], usage: { input_tokens: 10, output_tokens: 5 } };
  });
  return { create, client: { messages: { create } } as unknown as Anthropic };
}

describe("preguntaEnIdioma", () => {
  it("en español (o sin idioma) no llama a la IA", async () => {
    const { create, client } = cliente("x");
    expect((await preguntaEnIdioma(client, "¿Cómo vas?", "es", usoVacio())).pregunta).toBe("¿Cómo vas?");
    expect((await preguntaEnIdioma(client, "¿Cómo vas?", null, usoVacio())).pregunta).toBe("¿Cómo vas?");
    expect(create).not.toHaveBeenCalled();
  });

  it("en coreano, la IA la expresa con la regla de idioma", async () => {
    const { create, client } = cliente("요즘 어떻게 지내요?");
    const r = await preguntaEnIdioma(client, "¿Cómo vas?", "ko", usoVacio());
    expect(r).toMatchObject({ pregunta: "요즘 어떻게 지내요?", traducida: true });
    const sistema = (create.mock.calls[0] as unknown as [{ system: Array<{ text: string }> }])[0].system;
    expect(sistema[1].text).toMatch(/^IDIOMA DE SALIDA: coreano/);
  });

  it("si la IA falla o devuelve vacío, queda la cacheada", async () => {
    expect(await preguntaEnIdioma(cliente(new Error("sin red")).client, "¿Cómo vas?", "ko", usoVacio())).toMatchObject({
      pregunta: "¿Cómo vas?",
      traducida: false,
    });
    expect((await preguntaEnIdioma(cliente("   ").client, "¿Cómo vas?", "ko", usoVacio())).traducida).toBe(false);
  });
});

describe("avanzarTurno adapta la pregunta cacheada fuera del español", () => {
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

  it("idea en coreano: la cacheada (en español) llega traducida y queda como pendiente", async () => {
    avance();
    const { client } = cliente("디자인 층을 어떻게 나눴나요?");
    const estado = estadoInicial({ actualId: "design_thinking_fundamentos", perfilSesion: "p", textoOriginal: "t", idioma: "ko" });
    const r = await avanzarTurno({ client, graph, families, preguntasCache, estado, respuestaUsuario: null, acumulado: usoVacio(), dbSessionId: "s" });
    if (r.tipo !== "pregunta") throw new Error("esperaba pregunta");
    expect(preguntasCache[nid]?.pregunta).toBeTruthy();
    expect(r.pregunta).toBe("디자인 층을 어떻게 나눴나요?");
    expect(r.estado.preguntaPendiente).toBe("디자인 층을 어떻게 나눴나요?");
    expect(r.estado.ultimasPreguntas.at(-1)).toBe("디자인 층을 어떻게 나눴나요?");
  });

  it("idea en español: la cacheada tal cual, sin llamar a la IA", async () => {
    avance();
    const { create, client } = cliente("no");
    const estado = estadoInicial({ actualId: "design_thinking_fundamentos", perfilSesion: "p", textoOriginal: "t" });
    const r = await avanzarTurno({ client, graph, families, preguntasCache, estado, respuestaUsuario: null, acumulado: usoVacio(), dbSessionId: "s" });
    if (r.tipo !== "pregunta") throw new Error("esperaba pregunta");
    expect(r.pregunta).toBe(preguntasCache[nid]!.pregunta);
    expect(create).not.toHaveBeenCalled();
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
