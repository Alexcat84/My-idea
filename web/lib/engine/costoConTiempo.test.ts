// UN COSTO TOTAL QUE INCLUYE EL TIEMPO DE LA PERSONA NUNCA ES COSTO DE MATERIALES (decision del fundador, 8 oct 2026).
// El juez de fidelidad sostuvo un contrario en el plan del nucleo aad2749d: «divide lo que gastaste en materiales [...]
// y anótalo al lado de tu costo de 130 para ver si coincide». La persona habia dicho "ya sé mi costo real por pieza: 130
// incluyendo mi hora a 50"; el interprete lo guardo como costo_materiales_unidad = 130 y el plan le creyo a la etiqueta.
import { beforeEach, describe, expect, it, vi } from "vitest";

vi.mock("../compass", () => ({ MAX_SALTOS_POSIBLES_OFRECIDOS: 8, MIN_SCORE_SALTO: 0.3, buscarAfines: async () => [] }));

import PROMPTS from "../assets/prompts.json";
import { usoVacio } from "../costmeter";
import { cargarGrafo, cargarPreguntasCache } from "./graph";
import { esCostoQueIncluyeTiempo, interpretarMultiSalto } from "./interprete";
import { fichaVacia } from "./memoria";

const graph = cargarGrafo();
const preguntasCache = cargarPreguntasCache();
const actualId = "design_thinking_fundamentos";
const CASO_REAL = "ya sé mi costo real por pieza: 130 incluyendo mi hora a 50";

describe("esCostoQueIncluyeTiempo", () => {
  it.each([CASO_REAL, "me sale en 200 contando mis horas", "unos 90 con la mano de obra", "son 75 sumando mi tiempo"])("«%s» incluye tiempo", (t) => {
    expect(esCostoQueIncluyeTiempo(t)).toBe(true);
  });
  it.each(["me cuesta como 68 en materiales", "gasto 40 en cemento y pintura por maceta", "le dedico un par de horas"])("«%s» no es un costo con tiempo", (t) => {
    expect(esCostoQueIncluyeTiempo(t)).toBe(false);
  });
});

describe("el interprete no guarda un costo con tiempo como costo de materiales", () => {
  beforeEach(() => vi.clearAllMocks());

  it("el caso real se descarta del campo costo_materiales_unidad y queda registrado", async () => {
    const salida = {
      accion: "avanzar", camino: [graph[actualId].nodos_siguientes![0]], salto_semantico: null, pregunta_necesaria: true,
      pregunta_adaptada: "¿A cuánto vendes cada maceta?", repregunta: null, perfil_update: null,
      numeros_detectados: {
        costo_materiales_unidad: { valor: 130, unidad: null, texto_original: CASO_REAL },
        valor_hora: { valor: 50, unidad: null, texto_original: "mi hora a 50" },
      },
    };
    const create = vi.fn(async () => ({ content: [{ type: "text", text: JSON.stringify(salida) }], stop_reason: "end_turn", usage: { input_tokens: 10, output_tokens: 10 } }));
    const eventos: Array<Record<string, unknown>> = [];
    const r = await interpretarMultiSalto({
      client: { messages: { create } } as never, actualId, graph, visitados: new Set([actualId]), perfilSesion: "p",
      textoOriginal: "macetas", preguntaHecha: "¿Cuánto te cuesta cada pieza?", respuestaUsuario: CASO_REAL,
      repreguntasDisponibles: true, preguntasCache, acumulado: usoVacio(), historialMensajes: [], fichaActual: fichaVacia(),
      registrarEvento: (e) => eventos.push(e as unknown as Record<string, unknown>),
    });
    expect(r.resultado?.numerosDetectados?.costo_materiales_unidad).toBeUndefined();
    expect(r.resultado?.numerosDetectados?.valor_hora?.valor).toBe(50);
    expect(eventos.some((e) => e.tipo === "costo_con_tiempo_descartado")).toBe(true);
  });

  it("el prompt del interprete lleva la regla", () => {
    expect((PROMPTS as Record<string, string>).SYSTEM_INTERPRETE_MULTI).toMatch(/un costo total que incluye el tiempo de la persona[^.]*nunca es costo_materiales_unidad/i);
  });
});
