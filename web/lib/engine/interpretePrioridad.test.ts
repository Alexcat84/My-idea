/**
 * CONSTRUCCION 4 (decision del fundador, 28 sep 2026): la prioridad declarada es una REGLA EN CODIGO. Si hay un
 * candidato que la atiende, el interprete no puede elegir uno que no la atienda, salvo un paso previo con su motivo
 * escrito. Todo con la brujula y el modelo simulados: ninguna llamada a la API real hasta la corrida final.
 *
 * Puntuaciones fijadas a mano contra la prioridad (umbral 0,30, el de la brujula):
 *   mapeo_capas_diseno       0,52  -> atiende
 *   encuadre_desafio_diseno  0,34  -> atiende
 *   cualquier otro           0,10  -> no atiende
 * Luego los que atienden, del que mas al que menos: [mapeo_capas_diseno, encuadre_desafio_diseno].
 */
import { beforeEach, describe, expect, it, vi } from "vitest";

const buscarAfinesFalso = vi.fn<(...args: unknown[]) => Promise<{ id: string; score: number }[]>>(async () => []);
const puntuadorContraFalso = vi.fn<(...args: unknown[]) => Promise<((id: string) => number | null) | null>>();

vi.mock("../compass", () => ({
  MAX_SALTOS_POSIBLES_OFRECIDOS: 8,
  MIN_SCORE_SALTO: 0.3,
  buscarAfines: (...args: unknown[]) => buscarAfinesFalso(...args),
  puntuadorContra: (...args: unknown[]) => puntuadorContraFalso(...args),
}));

import { usoVacio } from "../costmeter";
import { cargarGrafo, cargarPreguntasCache } from "./graph";
import { consultaParaBrujula, elegirPorAfinidad, interpretarMultiSalto } from "./interprete";
import { queAtienden, violaPrioridad } from "./prioridad";

const graph = cargarGrafo();
const preguntasCache = cargarPreguntasCache();
const actualId = "design_thinking_fundamentos";
const ATIENDE_1 = "mapeo_capas_diseno";
const ATIENDE_2 = "encuadre_desafio_diseno";
const NO_ATIENDE = "convertir_necesidad_en_demanda";
const PUNTAJES: Record<string, number> = { [ATIENDE_1]: 0.52, [ATIENDE_2]: 0.34 };
const puntuarFijo = (id: string) => PUNTAJES[id] ?? 0.1;
const PRIORIDAD = { texto: "dirigir a mis dos empleados", conteo: 2 };

function respuesta(json: unknown) {
  return { content: [{ type: "text", text: JSON.stringify(json) }], usage: { input_tokens: 300, output_tokens: 60 }, stop_reason: "end_turn" };
}
const avanzarA = (destino: string, extra: Record<string, unknown> = {}) =>
  respuesta({ accion: "avanzar", camino: [destino], pregunta_necesaria: true, pregunta_adaptada: "¿Y cómo lo ves?", ...extra });

function clienteFalso(respuestas: unknown[]) {
  const llamadas: Array<{ messages: Array<{ content: string }> }> = [];
  let i = 0;
  const cliente = {
    messages: {
      create: vi.fn(async (kw: { messages: Array<{ content: string }> }) => {
        llamadas.push(kw);
        return respuestas[i++];
      }),
    },
  };
  return { cliente, llamadas };
}

function llamar(cliente: unknown, prioridad: typeof PRIORIDAD | null, eventos: unknown[]) {
  return interpretarMultiSalto({
    client: cliente as never,
    actualId,
    graph,
    visitados: new Set([actualId]),
    perfilSesion: "Tiene un taller y dos empleados.",
    textoOriginal: "taller de macetas",
    preguntaHecha: "¿Qué te preocupa?",
    respuestaUsuario: "me cuesta que mis empleados hagan las cosas sin mí",
    repreguntasDisponibles: true,
    preguntasCache,
    historialMensajes: null,
    acumulado: usoVacio(),
    prioridadDeclaradaActual: prioridad,
    registrarEvento: (e) => eventos.push(e),
  });
}

const tipo = (eventos: unknown[], t: string) => eventos.filter((e) => (e as { tipo: string }).tipo === t);

beforeEach(() => {
  buscarAfinesFalso.mockReset();
  buscarAfinesFalso.mockResolvedValue([]);
  puntuadorContraFalso.mockReset();
  puntuadorContraFalso.mockResolvedValue(puntuarFijo);
});

describe("prioridad: las piezas puras", () => {
  it("queAtienden: solo los que llegan al umbral, del que mas al que menos, sin repetir", () => {
    // a 0,45 y b 0,30 llegan (0,30 >= 0,30); c 0,29 no; d sin vector no.
    const p = (id: string) => ({ a: 0.45, b: 0.3, c: 0.29 } as Record<string, number>)[id] ?? null;
    expect(queAtienden(["c", "b", "a", "d", "a"], p)).toEqual(["a", "b"]);
    expect(queAtienden(["a"], null)).toEqual([]);
  });

  it("violaPrioridad: solo si hay quien la atiende, el destino no, y no hay paso previo escrito", () => {
    expect(violaPrioridad("x", ["a"], null)).toBe(true);
    expect(violaPrioridad("a", ["a"], null)).toBe(false);
    expect(violaPrioridad("x", [], null)).toBe(false);
    expect(violaPrioridad("x", ["a"], "antes necesita saber a quien le vende")).toBe(false);
    expect(violaPrioridad("x", ["a"], "   ")).toBe(true);
  });

  it("la brujula busca con la respuesta y la prioridad", () => {
    expect(consultaParaBrujula("me cuesta delegar", PRIORIDAD)).toBe("me cuesta delegar dirigir a mis dos empleados");
    expect(consultaParaBrujula("me cuesta delegar", null)).toBe("me cuesta delegar");
  });

  it("el respaldo sin modelo puntua tambien contra la prioridad", () => {
    // sin respuesta ni perfil, solo la prioridad decide entre dos candidatos
    const a = elegirPorAfinidad([NO_ATIENDE, ATIENDE_1], graph, null, null, { texto: graph[ATIENDE_1].titulo_concepto, conteo: 1 });
    expect(a).toBe(ATIENDE_1);
  });
});

describe("interpretarMultiSalto: la prioridad manda", () => {
  it("elegir un destino que no la atiende se rechaza y el reintento lleva el motivo y los que la atienden", async () => {
    const { cliente, llamadas } = clienteFalso([avanzarA(NO_ATIENDE), avanzarA(ATIENDE_1)]);
    const eventos: unknown[] = [];
    const r = await llamar(cliente, PRIORIDAD, eventos);
    expect(llamadas).toHaveLength(2);
    const primero = JSON.parse(llamadas[0].messages[0].content);
    expect(primero.candidatos_que_atienden_prioridad).toEqual([ATIENDE_1, ATIENDE_2]);
    const segundo = JSON.parse(llamadas[1].messages[0].content);
    expect(segundo.error_previo).toMatch(/prioridad/);
    expect(r.resultado?.camino).toEqual([ATIENDE_1]);
    expect(tipo(eventos, "prioridad_rechazo")).toEqual([
      { tipo: "prioridad_rechazo", nodo_actual: actualId, destino: NO_ATIENDE, atienden: [ATIENDE_1, ATIENDE_2] },
    ]);
  });

  it("un paso previo con su motivo se permite y el motivo queda escrito", async () => {
    const motivo = "antes de dirigir, necesita saber qué demanda atiende su taller";
    const { cliente, llamadas } = clienteFalso([avanzarA(NO_ATIENDE, { paso_previo: motivo })]);
    const eventos: unknown[] = [];
    const r = await llamar(cliente, PRIORIDAD, eventos);
    expect(llamadas).toHaveLength(1);
    expect(r.resultado?.camino).toEqual([NO_ATIENDE]);
    expect(r.resultado?.pasoPrevio).toBe(motivo);
    expect(tipo(eventos, "prioridad_paso_previo")).toEqual([
      { tipo: "prioridad_paso_previo", nodo_actual: actualId, destino: NO_ATIENDE, motivo, atienden: [ATIENDE_1, ATIENDE_2] },
    ]);
  });

  it("si el modelo insiste dos veces, el respaldo elige el que mejor la atiende", async () => {
    const { cliente } = clienteFalso([avanzarA(NO_ATIENDE), avanzarA(NO_ATIENDE)]);
    const eventos: unknown[] = [];
    const r = await llamar(cliente, PRIORIDAD, eventos);
    expect(r.resultado?.camino).toEqual([ATIENDE_1]);
    expect((tipo(eventos, "fallback_auto")[0] as { candidato_elegido: string }).candidato_elegido).toBe(ATIENDE_1);
  });

  it("si ningun candidato la atiende, manda el camino local y no hay rechazo", async () => {
    puntuadorContraFalso.mockResolvedValue(() => 0.1);
    const { cliente, llamadas } = clienteFalso([avanzarA(NO_ATIENDE)]);
    const eventos: unknown[] = [];
    const r = await llamar(cliente, PRIORIDAD, eventos);
    expect(llamadas).toHaveLength(1);
    expect(r.resultado?.camino).toEqual([NO_ATIENDE]);
    expect(JSON.parse(llamadas[0].messages[0].content).candidatos_que_atienden_prioridad).toBeUndefined();
  });

  it("sin prioridad declarada no se mide nada", async () => {
    const { cliente } = clienteFalso([avanzarA(NO_ATIENDE)]);
    await llamar(cliente, null, []);
    expect(puntuadorContraFalso).not.toHaveBeenCalled();
  });

  it("sin brujula la regla no se puede medir: se dice en un evento y el turno sigue", async () => {
    puntuadorContraFalso.mockResolvedValue(null);
    const { cliente } = clienteFalso([avanzarA(NO_ATIENDE)]);
    const eventos: unknown[] = [];
    const r = await llamar(cliente, PRIORIDAD, eventos);
    expect(r.resultado?.camino).toEqual([NO_ATIENDE]);
    expect(tipo(eventos, "prioridad_sin_medir")).toEqual([{ tipo: "prioridad_sin_medir", nodo_actual: actualId }]);
  });
});
