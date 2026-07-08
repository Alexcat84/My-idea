// Fase 3.0: prueba de integracion de POST /api/session/[id]/plan. Usa el
// grafo/families REALES (mismo patron que planRedactor.test.ts) para que
// cosecharVecindario/evaluarRuta produzcan resultados genuinos, y mockea
// solo la parte de red: el cliente Anthropic (stream falso) y Supabase.
// La respuesta es SSE -- se lee el body completo como texto y se parsea
// el evento "done" para verificar el resultado final.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

const messagesStreamFalso = vi.fn();
vi.mock("@/lib/anthropicClient", () => ({
  createAnthropicClient: vi.fn(() => ({ messages: { stream: messagesStreamFalso } })),
}));

import { POST } from "./route";

function ctxFalso(id: string) {
  return { params: Promise.resolve({ id }) };
}

function requestFalso() {
  return new Request("http://test/api/session/s1/plan", { method: "POST" });
}

function streamFalsoExitoso(textoFinal: string) {
  return {
    on(evento: string, cb: (t: string) => void) {
      if (evento === "text") cb(textoFinal);
      return this;
    },
    async finalMessage() {
      return {
        content: [{ type: "text", text: textoFinal }],
        usage: { input_tokens: 500, output_tokens: 200, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
      };
    },
  };
}

function streamFalsoFallido(mensaje: string) {
  return {
    on() {
      return this;
    },
    async finalMessage(): Promise<never> {
      throw new Error(mensaje);
    },
  };
}

function estadoRecorridoBase(overrides: Record<string, unknown> = {}) {
  return {
    ruta: ["design_thinking_fundamentos"],
    modos: ["conversado"],
    perfilSesion: "Hace macetas de cemento, trabaja solo.",
    textoOriginal: "quiero vender macetas de cemento",
    profundizarOfrecido: false,
    esSeguimiento: false,
    estadoVivoPrevio: null,
    fallbackEvents: [],
    prioridadDeclarada: null,
    preguntaPendiente: null,
    ultimasPreguntas: [],
    repreguntasUsadas: 0,
    historialMensajes: [],
    numerosDetectadosSesion: {},
    tipoOfertaSesion: null,
    unidadVentaSesion: null,
    fase: "listo_para_plan",
    sigamosDirigido: null,
    ...overrides,
  };
}

const acumuladoVacio = { uso: {}, uso_por_componente: {}, presupuesto_excedido: false };

async function leerEventoDone(res: Response): Promise<Record<string, unknown>> {
  const texto = await res.text();
  const match = texto.match(/event: done\ndata: (.+)\n\n/);
  expect(match).toBeTruthy();
  return JSON.parse(match![1]);
}

describe("POST /api/session/[id]/plan", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    messagesStreamFalso.mockReset();
  });

  it("401 si no hay usuario autenticado", async () => {
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await POST(requestFalso(), ctxFalso("s1"));
    expect(res.status).toBe(401);
  });

  it("404 si la sesion no existe", async () => {
    const res = await POST(requestFalso(), ctxFalso("no-existe"));
    expect(res.status).toBe(404);
  });

  it("409 si la sesion ya esta cerrada", async () => {
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: new Date().toISOString(),
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoVacio },
    };
    const res = await POST(requestFalso(), ctxFalso("s1"));
    expect(res.status).toBe(409);
  });

  it("409 si no hay estado_recorrido", async () => {
    estadoFalso.sessions["s1"] = { id: "s1", project_id: "p1", closed_at: null, estado_recorrido: null };
    const res = await POST(requestFalso(), ctxFalso("s1"));
    expect(res.status).toBe(409);
  });

  it("streamea deltas, ensambla el plan, y persiste plan/sesion/proyecto", async () => {
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoVacio },
    };
    const rawModelo =
      '# Plan para vender macetas\n\nContenido real del plan.\n\n===JSON===\n{"familias_tratadas": ["accion_clientes"]}';
    messagesStreamFalso.mockReturnValueOnce(streamFalsoExitoso(rawModelo));

    const res = await POST(requestFalso(), ctxFalso("s1"));
    expect(res.headers.get("Content-Type")).toContain("text/event-stream");

    const done = await leerEventoDone(res);
    expect(done.project_id).toBe("p1");
    expect(done.session_id).toBe("s1");
    expect(done.markdown).toContain("# Plan para vender macetas");
    expect((done.costo_usd as number)).toBeGreaterThan(0);

    const sesion = estadoFalso.sessions["s1"] as Record<string, unknown>;
    expect(sesion.closed_at).toBeTruthy();
    expect(estadoFalso.plans).toHaveLength(1);
    expect(estadoFalso.plans[0].contenido_md).toBe(done.markdown);

    const proyecto = estadoFalso.projects["p1"] as Record<string, unknown>;
    expect(proyecto.titulo).toBe("Plan para vender macetas");
    expect(proyecto.estado_vivo).toBeTruthy();

    expect(estadoFalso.projectNodes.length).toBeGreaterThan(0);
  });

  it("si la llamada a Claude falla, cae al ensamblado offline y aun asi cierra la sesion", async () => {
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoVacio },
    };
    messagesStreamFalso.mockReturnValueOnce(streamFalsoFallido("fallo de red simulado"));

    const res = await POST(requestFalso(), ctxFalso("s1"));
    const texto = await res.text();
    expect(texto).toContain("event: aviso");
    const match = texto.match(/event: done\ndata: (.+)\n\n/);
    expect(match).toBeTruthy();
    const done = JSON.parse(match![1]);
    expect(done.markdown).toContain("# Tu plan de accion");

    const sesion = estadoFalso.sessions["s1"] as Record<string, unknown>;
    expect(sesion.closed_at).toBeTruthy();
  });
});
