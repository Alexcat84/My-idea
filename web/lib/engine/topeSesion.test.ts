// TOPE POR SESION (visto del fundador, corrida final, 8 oct 2026): USD 1,00 por defecto en el codigo, con dos
// condiciones: al alcanzarlo la sesion termina de forma ORDENADA, guardando lo hecho y sin cortar un plan a mitad.
//
// Antes (el 502 de la prueba de coherencia del 8 oct): el presupuesto agotado dentro del interprete se leia como un
// fallo de red; el turno devolvia error_temporal y cada reintento volvia a fallar (el gasto no baja), la sesion
// quedaba atascada. Ahora:
//  - la ENTREVISTA se cierra en el borde de un turno: listo_para_plan, con el turno y la memoria guardados;
//  - el PLAN que arranca se termina entero con IA: tiene su propio margen (MARGEN_PLAN_USD) sobre el tope de la
//    entrevista, para el redactor y todo lo que le sigue (estado vivo, estimacion, enlace, juez). El ensamblado
//    offline queda solo para un gasto desbocado, por encima de tope + margen.
//
// Calculo a mano de los acumulados (Sonnet 5.5: USD 10 por millon de tokens de salida):
//   tope por defecto 1,00; margen del plan 0,50 -> techo del plan 1,00 + 0,50 = 1,50
//   100.000 de salida -> 100.000 × 10 / 1.000.000 = 1,00 (justo en el tope de la entrevista)
//   120.000 de salida -> 1,20 (pasado el tope de la entrevista, dentro del margen del plan)
//   160.000 de salida -> 1,60 (por encima del techo del plan: desbocado)
import type Anthropic from "@anthropic-ai/sdk";
import { beforeEach, describe, expect, it, vi } from "vitest";

const interpretarMultiSaltoFalso = vi.fn();
vi.mock("./interprete", () => ({
  interpretarMultiSalto: (...args: unknown[]) => interpretarMultiSaltoFalso(...args),
}));

import { MODEL_SONNET, MARGEN_PLAN_USD, presupuestoDelPlanUsd, presupuestoSesionUsdDe, usoVacio, type UsoAcumulado } from "../costmeter";
import { cargarFamilies } from "../readiness";
import { cargarGrafo, cargarPreguntasCache } from "./graph";
import { avanzarTurno, estadoInicial } from "./recorrido";
import { generarTextoPlan } from "./redactorPlan";
import { comprimirEstadoVivo } from "./planRedactor";
import { evaluarCalidadSesion } from "./juezSesion";

const graph = cargarGrafo();
const families = cargarFamilies();
const preguntasCache = cargarPreguntasCache();

function gastado(salidaTokens: number): UsoAcumulado {
  return { ...usoVacio(), uso: { [MODEL_SONNET]: { in: 0, out: salidaTokens, llamadas: 1, cache_read: 0, cache_write: 0 } } };
}

describe("el valor del tope", () => {
  it("por defecto es USD 1,00; la variable de entorno lo cambia; un valor roto vuelve al defecto", () => {
    expect(presupuestoSesionUsdDe(undefined)).toBe(1);
    expect(presupuestoSesionUsdDe("")).toBe(1);
    expect(presupuestoSesionUsdDe("2.5")).toBe(2.5);
    expect(presupuestoSesionUsdDe("abc")).toBe(1);
  });

  it("el plan tiene su margen de USD 0,50 sobre el tope de la entrevista", () => {
    expect(MARGEN_PLAN_USD).toBe(0.5);
    expect(presupuestoDelPlanUsd(1)).toBe(1.5);
  });
});

describe("la entrevista termina de forma ordenada al alcanzar el tope", () => {
  beforeEach(() => interpretarMultiSaltoFalso.mockReset());
  const estadoCon = () => ({
    ...estadoInicial({ actualId: "design_thinking_fundamentos", perfilSesion: "p", textoOriginal: "t" }),
    preguntaPendiente: "¿Cómo separas hoy las capas de tu taller?",
  });

  it("con el tope ya alcanzado no llama a la IA: pasa al plan, sin error", async () => {
    const r = await avanzarTurno({
      client: {} as Anthropic, graph, families, preguntasCache, estado: estadoCon(),
      respuestaUsuario: "Las separo a mano", acumulado: gastado(100_000), dbSessionId: "s",
    });
    expect(interpretarMultiSaltoFalso).not.toHaveBeenCalled();
    expect(r.tipo).toBe("listo_para_plan");
    expect(r.estado.fase).toBe("listo_para_plan");
    expect(r.estado.preguntaPendiente).toBeNull();
    expect(r.estado.fallbackEvents.at(-1)).toMatchObject({ tipo: "cierre_por_presupuesto" });
  });

  it("si el tope se cruza DENTRO del turno, tambien cierra ordenado (no error_temporal)", async () => {
    interpretarMultiSaltoFalso.mockResolvedValueOnce({ resultado: null, acumulado: gastado(120_000), historialMensajes: [] });
    const r = await avanzarTurno({
      client: {} as Anthropic, graph, families, preguntasCache, estado: estadoCon(),
      respuestaUsuario: "Las separo a mano", acumulado: gastado(90_000), dbSessionId: "s",
    });
    expect(r.tipo).toBe("listo_para_plan");
    expect(r.estado.fallbackEvents.at(-1)).toMatchObject({ tipo: "cierre_por_presupuesto" });
  });

  it("un fallo de red de verdad (sin tope) sigue siendo error_temporal", async () => {
    interpretarMultiSaltoFalso.mockResolvedValueOnce({ resultado: null, acumulado: gastado(10_000), historialMensajes: [] });
    const r = await avanzarTurno({
      client: {} as Anthropic, graph, families, preguntasCache, estado: estadoCon(),
      respuestaUsuario: "Las separo a mano", acumulado: gastado(10_000), dbSessionId: "s",
    });
    expect(r.tipo).toBe("error_temporal");
  });
});

describe("el plan no se corta a mitad", () => {
  function streamFalso() {
    return {
      on: () => undefined,
      finalMessage: async () => ({ content: [{ type: "text", text: "plan completo" }], stop_reason: "end_turn", usage: { input_tokens: 10, output_tokens: 10 } }),
    };
  }

  it("con la entrevista cerrada por el tope (1,20), el plan se escribe entero con IA", async () => {
    const stream = vi.fn(streamFalso);
    const r = await generarTextoPlan({ messages: { stream } } as unknown as Anthropic, { payload: {} } as never, gastado(120_000), () => undefined, () => undefined, null, { backoffsMs: [0] });
    expect(stream).toHaveBeenCalledTimes(1);
    expect(r.rawTexto).toBe("plan completo");
  });

  it("solo un gasto desbocado (1,60, por encima de tope + margen) cae al ensamblado offline", async () => {
    const stream = vi.fn(streamFalso);
    const r = await generarTextoPlan({ messages: { stream } } as unknown as Anthropic, { payload: {} } as never, gastado(160_000), () => undefined, () => undefined, null, { backoffsMs: [0] });
    expect(stream).not.toHaveBeenCalled();
    expect(r.rawTexto).toBeNull();
  });
});

describe("lo que sigue al redactor tambien se termina (estado vivo y juez)", () => {
  function clienteTexto(texto: string) {
    const create = vi.fn(async () => ({ content: [{ type: "text", text: texto }], stop_reason: "end_turn", usage: { input_tokens: 10, output_tokens: 10 } }));
    return { create, client: { messages: { create } } as unknown as Anthropic };
  }

  it("el estado vivo se actualiza con la entrevista cerrada por el tope (1,20)", async () => {
    const { client, create } = clienteTexto("Estado vivo nuevo.");
    const r = await comprimirEstadoVivo(client, "Estado viejo.", "perfil", [], gastado(120_000), null, null, presupuestoDelPlanUsd());
    expect(create).toHaveBeenCalledTimes(1);
    expect(r.estadoVivo).toBe("Estado vivo nuevo.");
  });

  it("el juez de la sesion tambien corre (1,20)", async () => {
    const { client, create } = clienteTexto(JSON.stringify({ veredicto: "ok" }));
    const decision = {
      tipo: "decision_turno", nodo_actual: "design_thinking_fundamentos", decision: { camino: [], es_salto: false },
      candidatos_locales: [], saltos_posibles: [], respuesta_usuario: "r", razonamiento: "z", pregunta: "p",
    };
    const r = await evaluarCalidadSesion(client, [decision], graph, gastado(120_000), 1, null, presupuestoDelPlanUsd());
    expect(create).toHaveBeenCalledTimes(1);
    expect(r.calidad).not.toBeNull();
  });
});
