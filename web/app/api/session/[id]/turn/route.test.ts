// Fase 3.0: prueba de integracion de POST /api/session/[id]/turn.
// avanzarTurno ya esta cubierto en detalle por recorrido.test.ts -- esta
// prueba mockea avanzarTurno y se enfoca en la orquestacion de la ruta:
// validacion, autenticacion, carga del estado persistido, los 409 de
// sesion cerrada/sin turno pendiente/en fase que no espera respuesta, y
// que la respuesta dependa correctamente de resultado.tipo.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));
vi.mock("@/lib/anthropicClient", () => ({
  createAnthropicClient: vi.fn(() => ({ messages: { create: vi.fn() } })),
}));

const avanzarTurnoFalso = vi.fn();
vi.mock("@/lib/engine/recorrido", () => ({
  avanzarTurno: (...args: unknown[]) => avanzarTurnoFalso(...args),
}));

import { POST } from "./route";

const acumuladoFalso = { uso: {}, uso_por_componente: {}, presupuesto_excedido: false };

function requestFalso(payload: unknown) {
  return new Request("http://test/api/session/s1/turn", { method: "POST", body: JSON.stringify(payload) });
}

function ctxFalso(id: string) {
  return { params: Promise.resolve({ id }) };
}

function estadoRecorridoBase(overrides: Record<string, unknown> = {}) {
  return {
    ruta: ["design_thinking_fundamentos"],
    modos: ["conversado"],
    perfilSesion: "perfil",
    textoOriginal: "mi idea",
    profundizarOfrecido: false,
    esSeguimiento: false,
    estadoVivoPrevio: null,
    fallbackEvents: [],
    prioridadDeclarada: null,
    preguntaPendiente: "¿que capas has mapeado?",
    ultimasPreguntas: [],
    repreguntasUsadas: 0,
    historialMensajes: [],
    numerosDetectadosSesion: {},
    tipoOfertaSesion: null,
    unidadVentaSesion: null,
    fase: "esperando_respuesta",
    sigamosDirigido: null,
    ...overrides,
  };
}

describe("POST /api/session/[id]/turn", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    avanzarTurnoFalso.mockReset();
  });

  it("rechaza sin 'respuesta'", async () => {
    const res = await POST(requestFalso({}), ctxFalso("s1"));
    expect(res.status).toBe(400);
  });

  it("rechaza respuesta que supera el maximo de 4000 caracteres", async () => {
    const res = await POST(requestFalso({ respuesta: "a".repeat(4001) }), ctxFalso("s1"));
    expect(res.status).toBe(400);
  });

  it("401 si no hay usuario autenticado", async () => {
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await POST(requestFalso({ respuesta: "algo" }), ctxFalso("s1"));
    expect(res.status).toBe(401);
  });

  it("404 si la sesion no existe", async () => {
    const res = await POST(requestFalso({ respuesta: "algo" }), ctxFalso("no-existe"));
    expect(res.status).toBe(404);
  });

  it("409 si la sesion ya esta cerrada", async () => {
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: new Date().toISOString(),
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoFalso },
    };
    const res = await POST(requestFalso({ respuesta: "algo" }), ctxFalso("s1"));
    expect(res.status).toBe(409);
  });

  it("409 si la sesion no tiene estado_recorrido (no se llamo a /start)", async () => {
    estadoFalso.sessions["s1"] = { id: "s1", project_id: "p1", closed_at: null, estado_recorrido: null };
    const res = await POST(requestFalso({ respuesta: "algo" }), ctxFalso("s1"));
    expect(res.status).toBe(409);
  });

  it("409 si la fase ya es listo_para_plan (no espera respuesta nueva)", async () => {
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase({ fase: "listo_para_plan" }), acumulado: acumuladoFalso },
    };
    const res = await POST(requestFalso({ respuesta: "algo" }), ctxFalso("s1"));
    expect(res.status).toBe(409);
  });

  it("avanza el turno y persiste el nuevo estado_recorrido", async () => {
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoFalso },
    };
    avanzarTurnoFalso.mockResolvedValueOnce({
      tipo: "pregunta",
      estado: estadoRecorridoBase({ ruta: ["design_thinking_fundamentos", "mapeo_capas_diseno"], preguntaPendiente: "siguiente pregunta" }),
      pregunta: "siguiente pregunta",
      acumulado: acumuladoFalso,
      nodosNuevos: [{ id: "mapeo_capas_diseno", titulo: "Mapeo de capas", modo: "conversado" }],
    });

    const res = await POST(requestFalso({ respuesta: "hago macetas de cemento" }), ctxFalso("s1"));
    expect(res.status).toBe(200);
    const body = await res.json();
    expect(body.tipo).toBe("pregunta");
    expect(body.pregunta).toBe("siguiente pregunta");

    expect(avanzarTurnoFalso).toHaveBeenCalledTimes(1);
    const argsLlamada = avanzarTurnoFalso.mock.calls[0][0] as { respuestaUsuario: string; dbSessionId: string };
    expect(argsLlamada.respuestaUsuario).toBe("hago macetas de cemento");
    expect(argsLlamada.dbSessionId).toBe("s1");

    const sesionActualizada = estadoFalso.sessions["s1"] as Record<string, unknown>;
    expect((sesionActualizada.estado_recorrido as { recorrido: { ruta: string[] } }).recorrido.ruta).toEqual([
      "design_thinking_fundamentos",
      "mapeo_capas_diseno",
    ]);
  });

  it("tipo=salio cierra la sesion", async () => {
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoFalso },
    };
    avanzarTurnoFalso.mockResolvedValueOnce({
      tipo: "salio",
      estado: estadoRecorridoBase({ fase: "cerrada" }),
      acumulado: acumuladoFalso,
    });

    const res = await POST(requestFalso({ respuesta: "ya no quiero seguir" }), ctxFalso("s1"));
    expect(res.status).toBe(200);
    const sesionActualizada = estadoFalso.sessions["s1"] as Record<string, unknown>;
    expect(sesionActualizada.closed_at).toBeTruthy();
  });
});
