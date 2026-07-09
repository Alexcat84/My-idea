// Fase 3.1 (caja de vidrio): paridad de comportamiento contra
// engine/test_juez_sesion.py. Verifica muestreo (0 = nunca llama, 1 =
// siempre llama), que resuelve node_ids a titulos reales antes de
// mandarlos al juez, y que una sesion sin decision_turno no llama a nada.
import { describe, expect, it, vi } from "vitest";
import { usoVacio } from "../costmeter";
import { cargarGrafo } from "./graph";
import { evaluarCalidadSesion } from "./juezSesion";

const graph = cargarGrafo();
const nodoId = Object.keys(graph)[0];
const tituloReal = graph[nodoId].titulo_concepto;

function respuestaClaudeFalsa(json: unknown) {
  return {
    content: [{ type: "text", text: JSON.stringify(json) }],
    usage: { input_tokens: 100, output_tokens: 30, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
  };
}

const decisiones = [
  { tipo: "fallback_auto", nodo_actual: nodoId, candidato_elegido: nodoId, motivo: "x" },
  {
    tipo: "decision_turno",
    nodo_actual: nodoId,
    respuesta_usuario: "no he calculado costos todavia",
    candidatos_locales: [nodoId],
    saltos_posibles: [{ id: nodoId, titulo: tituloReal, fase_proyecto: null, condiciones_activacion: [], afinidad: 0.5 }],
    decision: { accion: "avanzar" as const, camino: [nodoId], es_salto: false },
    razonamiento: "el usuario menciono costos",
  },
];

describe("evaluarCalidadSesion (Fase 3.1)", () => {
  it("muestreo=0 nunca invoca al juez", async () => {
    const create = vi.fn();
    const { calidad, acumulado } = await evaluarCalidadSesion(
      { messages: { create } } as never,
      decisiones,
      graph,
      usoVacio(),
      0
    );
    expect(calidad).toBeNull();
    expect(create).not.toHaveBeenCalled();
    expect(acumulado).toEqual(usoVacio());
  });

  it("sin eventos decision_turno, no invoca al juez", async () => {
    const create = vi.fn();
    const soloFallback = decisiones.filter((d) => d.tipo !== "decision_turno");
    const { calidad } = await evaluarCalidadSesion({ messages: { create } } as never, soloFallback, graph, usoVacio(), 1);
    expect(calidad).toBeNull();
    expect(create).not.toHaveBeenCalled();
  });

  it("muestreo=1 con eventos reales SI llama, filtra solo decision_turno, y resuelve ids a titulos reales", async () => {
    const create = vi.fn<(kwargs: { messages: Array<{ content: string }> }) => Promise<unknown>>(async () =>
      respuestaClaudeFalsa({
        pertinencia_transiciones: 5,
        repeticion_detectada: false,
        señales_fuera_de_material: [],
        comentario: "todo coherente",
      })
    );
    const { calidad, acumulado } = await evaluarCalidadSesion(
      { messages: { create } } as never,
      decisiones,
      graph,
      usoVacio(),
      1
    );
    expect(create).toHaveBeenCalledTimes(1);
    expect(calidad).toEqual({
      pertinencia_transiciones: 5,
      repeticion_detectada: false,
      señales_fuera_de_material: [],
      comentario: "todo coherente",
    });
    expect(acumulado).not.toEqual(usoVacio());

    const enviado = create.mock.calls[0][0];
    const turnos = JSON.parse(enviado.messages[0].content).turnos;
    expect(turnos).toHaveLength(1);
    expect(turnos[0].nodo).toBe(tituloReal);
    expect(turnos[0].destino).toEqual([tituloReal]);
    expect(turnos[0].respuesta_usuario).toBe("no he calculado costos todavia");
  });
});
