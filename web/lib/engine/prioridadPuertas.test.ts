/**
 * CONSTRUCCION 4 (decision del fundador, 28 sep 2026): la prioridad manda tambien en las PUERTAS (la re-eleccion de
 * puerta de un mundo y la puerta avanzada del seguimiento), y viaja entre sesiones: un mundo o un seguimiento arranca
 * con la prioridad que la ficha del proyecto ya guardo. Brujula y modelo simulados.
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { usoVacio } from "../costmeter";
import { cargarFamilies } from "../readiness";
import { semillasDelPack } from "./evaluacionBrecha";
import { cargarGrafo } from "./graph";
import { fichaVacia, fusionarFicha } from "./memoria";
import { seleccionarPuertaAvanzada } from "./puertaAvanzada";
import { estadoInicial } from "./recorrido";
import { reelegirPuertaDeMundo } from "./reeleccionPuerta";

const graph = cargarGrafo();
const families = cargarFamilies();
const PRIORIDAD = { texto: "dirigir a mis dos empleados", conteo: 2 };

describe("la prioridad viaja entre sesiones", () => {
  it("estadoInicial arranca con la prioridad de la ficha guardada", () => {
    const ficha = fusionarFicha(fichaVacia(), { prioridad_declarada: PRIORIDAD });
    expect(estadoInicial({ actualId: "x", perfilSesion: "", textoOriginal: "", ficha }).prioridadDeclarada).toEqual(PRIORIDAD);
    expect(estadoInicial({ actualId: "x", perfilSesion: "", textoOriginal: "" }).prioridadDeclarada).toBeNull();
  });
});

describe("reelegirPuertaDeMundo: la puerta que atiende la prioridad va primero", () => {
  const base = { dominio: "quality", graph, estadoVivo: null, perfilSesion: null, cubiertos: new Set<string>(), descartados: new Set<string>() };

  it("sin prioridad elige por afinidad; con ella, la semilla que la atiende aunque tenga menos afinidad", () => {
    const sin = reelegirPuertaDeMundo(base)!;
    const otra = semillasDelPack("quality").map((s) => s.id).find((id) => id !== sin.puertaId)!;
    expect(otra).toBeTruthy();
    // A mano: 'otra' puntua 0,50 contra la prioridad (>= 0,30, la atiende); las demas 0,10 (no la atienden).
    const con = reelegirPuertaDeMundo({ ...base, puntuarPrioridad: (id) => (id === otra ? 0.5 : 0.1) })!;
    expect(con.puertaId).toBe(otra);
  });

  it("si ninguna la atiende, el orden de siempre", () => {
    const sin = reelegirPuertaDeMundo(base)!;
    expect(reelegirPuertaDeMundo({ ...base, puntuarPrioridad: () => 0.1 })!.puertaId).toBe(sin.puertaId);
  });
});

describe("seleccionarPuertaAvanzada: la prioridad manda en la puerta del seguimiento", () => {
  function cliente(respuesta: Record<string, unknown>) {
    const create = vi.fn(async (_req: unknown) => ({
      content: [{ type: "text", text: JSON.stringify(respuesta) }],
      usage: { input_tokens: 400, output_tokens: 60 },
      stop_reason: "end_turn",
    }));
    return { client: { messages: { create } } as unknown as Anthropic, create };
  }
  const cubiertos = new Set<string>();
  const llamar = (client: Anthropic, puntuar: ((id: string) => number | null) | null) =>
    seleccionarPuertaAvanzada(client, "contraté a dos personas y no sé dirigirlas", null, "ejecucion", families, graph, cubiertos, ["design_thinking_fundamentos"], usoVacio(), ["core"], null, puntuar);

  // A mano: ATIENDE puntua 0,60 contra la prioridad; todo lo demas 0,10. Solo ATIENDE la atiende.
  const ATIENDE = "mapeo_capas_diseno";
  const puntuar = (id: string) => (id === ATIENDE ? 0.6 : 0.1);

  it("el que la atiende entra a los candidatos y viaja marcado", async () => {
    const { client, create } = cliente({ puerta_id: ATIENDE, perfil_sesion: "p" });
    const r = await llamar(client, puntuar);
    const ctx = JSON.parse((create.mock.calls[0][0] as { messages: Array<{ content: string }> }).messages[0].content);
    expect(ctx.candidatos.map((c: { id: string }) => c.id)).toContain(ATIENDE);
    expect(ctx.candidatos_que_atienden_prioridad).toEqual([ATIENDE]);
    expect(r.puertaId).toBe(ATIENDE);
    expect(r.eventos).toEqual([]);
  });

  it("si el modelo elige otra sin paso previo, el codigo la corrige y lo deja escrito", async () => {
    // el modelo elige un candidato real que no la atiende: el primero de la lista que no sea ATIENDE
    const { client, create } = cliente({ puerta_id: ATIENDE, perfil_sesion: "p" });
    await llamar(client, puntuar);
    const ctx = JSON.parse((create.mock.calls[0][0] as { messages: Array<{ content: string }> }).messages[0].content);
    const otro = (ctx.candidatos as Array<{ id: string }>).map((c) => c.id).find((id) => id !== ATIENDE)!;
    const r = await llamar(cliente({ puerta_id: otro, perfil_sesion: "p" }).client, puntuar);
    expect(r.puertaId).toBe(ATIENDE);
    expect(r.eventos).toEqual([{ tipo: "prioridad_rechazo", nodo_actual: "(puerta de seguimiento)", destino: otro, atienden: [ATIENDE] }]);
  });

  it("con paso previo escrito se respeta la eleccion y el motivo queda", async () => {
    const { client, create } = cliente({ puerta_id: ATIENDE, perfil_sesion: "p" });
    await llamar(client, puntuar);
    const ctx = JSON.parse((create.mock.calls[0][0] as { messages: Array<{ content: string }> }).messages[0].content);
    const otro = (ctx.candidatos as Array<{ id: string }>).map((c) => c.id).find((id) => id !== ATIENDE)!;
    const motivo = "primero necesita ordenar qué vende antes de repartir tareas";
    const r = await llamar(cliente({ puerta_id: otro, perfil_sesion: "p", paso_previo: motivo }).client, puntuar);
    expect(r.puertaId).toBe(otro);
    expect(r.eventos).toEqual([
      { tipo: "prioridad_paso_previo", nodo_actual: "(puerta de seguimiento)", destino: otro, motivo, atienden: [ATIENDE] },
    ]);
  });

  it("sin prioridad, como siempre y sin eventos", async () => {
    const { client, create } = cliente({ puerta_id: ATIENDE, perfil_sesion: "p" });
    const r = await llamar(client, null);
    const ctx = JSON.parse((create.mock.calls[0][0] as { messages: Array<{ content: string }> }).messages[0].content);
    expect(ctx.candidatos_que_atienden_prioridad).toBeUndefined();
    expect(r.eventos).toEqual([]);
  });
});
