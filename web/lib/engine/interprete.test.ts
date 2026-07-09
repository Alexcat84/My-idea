// Fase 3.0: paridad de comportamiento contra engine/test_autocorreccion.py
// y engine/test_salto_semantico.py, sobre el grafo real (mismo nodo de
// prueba, design_thinking_fundamentos, ya usado en graph.test.ts) y con
// la brujula (compass.ts) mockeada para no depender de la red.
import { beforeEach, describe, expect, it, vi } from "vitest";

const buscarAfinesFalso = vi.fn<(...args: unknown[]) => Promise<{ id: string; score: number }[]>>(
  async () => []
);

vi.mock("../compass", () => ({
  MAX_SALTOS_POSIBLES_OFRECIDOS: 8,
  MIN_SCORE_SALTO: 0.3,
  buscarAfines: (...args: unknown[]) => buscarAfinesFalso(...args),
}));

import { usoVacio } from "../costmeter";
import { cargarGrafo, cargarPreguntasCache } from "./graph";
import { interpretarMultiSalto } from "./interprete";

const graph = cargarGrafo();
const preguntasCache = cargarPreguntasCache();
const actualId = "design_thinking_fundamentos";

function respuestaClaudeFalsa(json: unknown) {
  return {
    content: [{ type: "text", text: JSON.stringify(json) }],
    usage: { input_tokens: 300, output_tokens: 60, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
  };
}

function clienteFalso(respuestas: unknown[]) {
  const llamadas: Array<{ messages: Array<{ content: string }> }> = [];
  let idx = 0;
  return {
    cliente: {
      messages: {
        create: vi.fn(async (kwargs: { messages: Array<{ content: string }> }) => {
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

describe("interpretarMultiSalto: auto-correccion silenciosa tras 2 fallos de validacion", () => {
  beforeEach(() => {
    buscarAfinesFalso.mockReset();
    buscarAfinesFalso.mockResolvedValue([]);
  });

  it("reintenta una vez con error_previo+ids_validos, y si vuelve a fallar auto-selecciona por afinidad", async () => {
    const respuestaInvalida = respuestaClaudeFalsa({
      accion: "avanzar",
      camino: ["id_totalmente_inventado_no_existe"],
      pregunta_necesaria: true,
      repregunta: null,
      perfil_update: null,
    });
    const { cliente, llamadas } = clienteFalso([respuestaInvalida, respuestaInvalida]);

    const eventos: unknown[] = [];
    const r = await interpretarMultiSalto({
      client: cliente as never,
      actualId,
      graph,
      visitados: new Set([actualId]),
      perfilSesion: "Quiero validar con clientes reales antes de construir nada.",
      textoOriginal: "tengo miedo de construir algo que nadie use",
      preguntaHecha: "¿Qué te preocupa más?",
      respuestaUsuario: "me preocupa hablar con clientes reales antes de construir",
      repreguntasDisponibles: true,
      preguntasCache,
      ultimasPreguntas: [],
      historialMensajes: null,
      acumulado: usoVacio(),
      registrarEvento: (e) => eventos.push(e),
    });

    expect(llamadas).toHaveLength(2);
    const segundaLlamada = JSON.parse(llamadas[1].messages[0].content);
    expect(segundaLlamada.error_previo).toBeTruthy();
    expect(segundaLlamada.ids_validos.length).toBeGreaterThan(0);

    expect(r.resultado).not.toBeNull();
    expect(r.resultado?.accion).toBe("avanzar");
    expect(r.resultado?.camino).toHaveLength(1);
    const candidatoElegido = r.resultado?.camino[0] as string;
    expect(graph[actualId].nodos_siguientes).toContain(candidatoElegido);
    expect(eventos).toHaveLength(2);
    const fallbackEventos = eventos.filter((e) => (e as { tipo: string }).tipo === "fallback_auto");
    const decisionEventos = eventos.filter((e) => (e as { tipo: string }).tipo === "decision_turno");
    expect(fallbackEventos).toHaveLength(1);
    expect(decisionEventos).toHaveLength(1);
    expect((fallbackEventos[0] as { candidato_elegido: string }).candidato_elegido).toBe(candidatoElegido);
    expect(r.resultado?.preguntaAdaptada).toBeTruthy();

    // Fase 3.1 (caja de vidrio): decision_turno tambien se emite en el
    // camino de fallback, con un razonamiento sintetico documentando que
    // fue automatico, no una eleccion real del modelo.
    const decisionEvento = decisionEventos[0] as {
      decision: { camino: string[] };
      razonamiento: string | null;
      candidatos_locales: string[];
      saltos_posibles: unknown[];
    };
    expect(decisionEvento.decision.camino).toEqual([candidatoElegido]);
    expect(decisionEvento.razonamiento).toBe("fallback automatico tras 2 respuestas invalidas del modelo");
    expect(decisionEvento.candidatos_locales.length).toBeGreaterThan(0);
    expect(Array.isArray(decisionEvento.saltos_posibles)).toBe(true);
  });
});

describe("interpretarMultiSalto: validacion de salto_semantico", () => {
  const candidatoSalto = "decision_fundador_solo_vs_equipo";

  beforeEach(() => {
    buscarAfinesFalso.mockReset();
    buscarAfinesFalso.mockResolvedValue([{ id: candidatoSalto, score: 0.9 }]);
  });

  it("el grafo real contiene el nodo de prueba", () => {
    expect(graph[candidatoSalto]).toBeDefined();
  });

  it("acepta un salto valido en el primer intento (esSalto=true, sin retry)", async () => {
    const { cliente, llamadas } = clienteFalso([
      respuestaClaudeFalsa({
        accion: "avanzar",
        camino: [],
        salto_semantico: candidatoSalto,
        pregunta_necesaria: true,
        pregunta_adaptada: "ya que haces todo tu solo, ¿has pensado en tu limite de produccion mensual?",
        repregunta: null,
        perfil_update: null,
        prioridad_declarada: null,
      }),
    ]);

    const r = await interpretarMultiSalto({
      client: cliente as never,
      actualId,
      graph,
      visitados: new Set([actualId]),
      perfilSesion: "Hace macetas, trabaja solo.",
      textoOriginal: "quiero saber si mi idea tiene futuro",
      preguntaHecha: null,
      respuestaUsuario: "hago todo yo solo, sin equipo ni empleados",
      repreguntasDisponibles: true,
      preguntasCache,
      historialMensajes: null,
      acumulado: usoVacio(),
    });

    expect(llamadas).toHaveLength(1);
    expect(r.resultado?.esSalto).toBe(true);
    expect(r.resultado?.camino).toEqual([candidatoSalto]);
  });

  it("rechaza un salto no ofrecido, reintenta exactamente una vez, y cae al respaldo tier-2 (esSalto=false)", async () => {
    const respuestaInvalida = respuestaClaudeFalsa({
      accion: "avanzar",
      camino: [],
      salto_semantico: "id_que_no_fue_ofrecido",
      pregunta_necesaria: true,
      pregunta_adaptada: "algo",
      repregunta: null,
      perfil_update: null,
      prioridad_declarada: null,
    });
    const { cliente, llamadas } = clienteFalso([respuestaInvalida, respuestaInvalida]);

    const r = await interpretarMultiSalto({
      client: cliente as never,
      actualId,
      graph,
      visitados: new Set([actualId]),
      perfilSesion: "Hace macetas, trabaja solo.",
      textoOriginal: "quiero saber si mi idea tiene futuro",
      preguntaHecha: null,
      respuestaUsuario: "hago todo yo solo, sin equipo ni empleados",
      repreguntasDisponibles: true,
      preguntasCache,
      historialMensajes: null,
      acumulado: usoVacio(),
    });

    expect(llamadas).toHaveLength(2);
    const segundaLlamada = JSON.parse(llamadas[1].messages[0].content);
    expect(segundaLlamada.ids_validos).toBeDefined();
    expect(r.resultado).not.toBeNull();
    expect(r.resultado?.esSalto).toBe(false);
  });
});

describe("interpretarMultiSalto: presupuesto excedido se propaga como resultado=null (menu de emergencia)", () => {
  it("no llama a la API si el acumulado ya supera el presupuesto", async () => {
    buscarAfinesFalso.mockReset();
    buscarAfinesFalso.mockResolvedValue([]);
    const { cliente } = clienteFalso([respuestaClaudeFalsa({ accion: "salir" })]);
    const acumuladoExcedido = {
      uso: { "claude-haiku-4-5": { in: 400_000, out: 0, llamadas: 1, cache_read: 0, cache_write: 0 } },
      uso_por_componente: {},
      presupuesto_excedido: false,
    };

    const r = await interpretarMultiSalto({
      client: cliente as never,
      actualId,
      graph,
      visitados: new Set([actualId]),
      perfilSesion: null,
      textoOriginal: "algo",
      preguntaHecha: null,
      respuestaUsuario: null,
      repreguntasDisponibles: true,
      preguntasCache,
      historialMensajes: null,
      acumulado: acumuladoExcedido,
    });

    expect(r.resultado).toBeNull();
    expect(cliente.messages.create).not.toHaveBeenCalled();
  });
});
