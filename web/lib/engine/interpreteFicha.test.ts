// PRINCIPIO 1 en el interprete (28 sep 2026): el contexto completo viaja SIEMPRE.
//  - En el primer turno de la sesion, el contexto del proyecto va en su propio
//    bloque con cache de 1 hora; queda al principio del historial, que solo crece
//    por el final.
//  - En CADA turno viajan la ficha de contexto actual y el perfil actual (antes,
//    desde el turno 2 el interprete ya no veia ni la idea ni el perfil).
//  - El interprete actualiza la ficha en la misma llamada: `ficha_update`.
import { beforeEach, describe, expect, it, vi } from "vitest";

vi.mock("../compass", () => ({
  MAX_SALTOS_POSIBLES_OFRECIDOS: 8,
  MIN_SCORE_SALTO: 0.3,
  buscarAfines: async () => [],
}));

import { usoVacio } from "../costmeter";
import { cargarGrafo, cargarPreguntasCache } from "./graph";
import { interpretarMultiSalto } from "./interprete";
import { fichaVacia, fusionarFicha } from "./memoria";

const graph = cargarGrafo();
const preguntasCache = cargarPreguntasCache();
const actualId = "design_thinking_fundamentos";
const siguiente = graph[actualId].nodos_siguientes![0];

function respuesta(json: unknown) {
  return { content: [{ type: "text", text: JSON.stringify(json) }], stop_reason: "end_turn", usage: { input_tokens: 10, output_tokens: 10 } };
}
const SALIDA = {
  accion: "avanzar",
  camino: [siguiente],
  salto_semantico: null,
  pregunta_necesaria: true,
  pregunta_adaptada: "¿Cómo repartes hoy el trabajo con tus dos empleados?",
  repregunta: null,
  perfil_update: "Tiene un taller con dos empleados.",
  ficha_update: { papel: "dueno", tiene_jefe: false, equipo: { personas: 2, descripcion: "dos empleados" } },
};

type Llamada = { messages: Array<{ role: string; content: string | Array<{ text: string; cache_control?: unknown }> }> };

function cliente() {
  const llamadas: Llamada[] = [];
  const create = vi.fn(async (kw: Llamada) => {
    llamadas.push(JSON.parse(JSON.stringify(kw)));
    return respuesta(SALIDA);
  });
  return { client: { messages: { create } } as never, llamadas };
}

const FICHA = fusionarFicha(fichaVacia(), { papel: "dueno", tiene_jefe: false });

const base = {
  actualId,
  graph,
  visitados: new Set([actualId]),
  perfilSesion: "Taller de macetas.",
  textoOriginal: "Quiero ordenar mi taller",
  preguntaHecha: null,
  respuestaUsuario: null,
  repreguntasDisponibles: true,
  preguntasCache,
  acumulado: usoVacio(),
  contextoProyecto: "CONTEXTO DEL PROYECTO: taller con dos empleados",
  fichaActual: FICHA,
};

describe("la ficha y el contexto del proyecto en el interprete", () => {
  beforeEach(() => vi.clearAllMocks());

  it("turno 1: el contexto del proyecto va en su bloque cacheado 1 hora, y la ficha en el turno", async () => {
    const { client, llamadas } = cliente();
    await interpretarMultiSalto({ ...base, client, historialMensajes: [] });
    const contenido = llamadas[0].messages[0].content as Array<{ text: string; cache_control?: unknown }>;
    expect(contenido[0]).toEqual({ type: "text", text: "CONTEXTO DEL PROYECTO: taller con dos empleados", cache_control: { type: "ephemeral", ttl: "1h" } });
    const turno = JSON.parse(contenido[1].text);
    expect(turno.ficha_contexto.papel).toBe("dueno");
    expect(turno.perfil_sesion).toBe("Taller de macetas.");
  });

  it("turno 2: la ficha y el perfil ACTUALES viajan otra vez; el contexto sigue al principio del historial", async () => {
    const { client, llamadas } = cliente();
    const r1 = await interpretarMultiSalto({ ...base, client, historialMensajes: [] });
    const fichaNueva = fusionarFicha(FICHA, { equipo: { personas: 2, descripcion: null } });
    await interpretarMultiSalto({
      ...base,
      client,
      historialMensajes: r1.historialMensajes,
      preguntaHecha: "¿Cómo repartes hoy el trabajo?",
      respuestaUsuario: "Lo hago todo yo",
      perfilSesion: "Taller de macetas.\nHace todo el trabajo el mismo.",
      fichaActual: fichaNueva,
    });
    const mensajes = llamadas[1].messages;
    // el primer mensaje del historial conserva el bloque del contexto del proyecto
    expect((mensajes[0].content as Array<{ text: string }>)[0].text).toBe("CONTEXTO DEL PROYECTO: taller con dos empleados");
    const ultimo = mensajes.at(-1)!.content as Array<{ text: string }>;
    const turno = JSON.parse(ultimo.at(-1)!.text);
    expect(turno.ficha_contexto.equipo.personas).toBe(2);
    expect(turno.perfil_sesion).toBe("Taller de macetas.\nHace todo el trabajo el mismo.");
  });

  it("la ficha_update del interprete sale en el resultado", async () => {
    const { client } = cliente();
    const r = await interpretarMultiSalto({ ...base, client, historialMensajes: [] });
    expect(r.resultado?.fichaUpdate).toEqual({ papel: "dueno", tiene_jefe: false, equipo: { personas: 2, descripcion: "dos empleados" } });
  });
});
