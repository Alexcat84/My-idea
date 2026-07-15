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

  // ── Fix (retry en el stream del plan): el redactor corre en el momento de
  // mayor inversion del usuario (y pronto, pagado). Antes, CUALQUIER fallo del
  // modelo degradaba en silencio a un ensamblado offline; ahora se reintenta, y
  // si se agota se dice de frente para que el usuario reintente SOLO la redaccion.
  function sembrarSesionViva() {
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoVacio },
    };
  }

  it("un hipo transitorio a mitad de stream se REINTENTA y el plan sale igual", async () => {
    sembrarSesionViva();
    const rawBueno =
      '# Plan para vender macetas\n\n## Etapa 1: Cierra tu costo real\n\nContenido real.\n\n' +
      '===JSON===\n{"familias_tratadas": ["accion_clientes"]}';
    // El primer intento muere; el segundo (tras el backoff) va bien.
    messagesStreamFalso.mockReturnValueOnce(streamFalsoFallido("overload simulado"));
    messagesStreamFalso.mockReturnValueOnce(streamFalsoExitoso(rawBueno));

    const res = await POST(requestFalso(), ctxFalso("s1"));
    const texto = await res.text();

    // El usuario recibe SU plan, no un ensamblado offline de consolacion.
    expect(texto).not.toContain("event: aviso");
    const match = texto.match(/event: done\ndata: (.+)\n\n/);
    expect(match).toBeTruthy();
    expect(JSON.parse(match![1]).markdown).toContain("Etapa 1");
    // Y se le avisa al cliente que descarte lo que el intento muerto pinto:
    // anunciar una sola vez (la leccion del organizador).
    expect(texto).toContain("event: reinicio");
    expect(estadoFalso.sessions["s1"].closed_at).toBeTruthy();
  });

  it("agotados los reintentos: error honesto y la sesion NO se cierra (se puede reintentar)", async () => {
    sembrarSesionViva();
    messagesStreamFalso.mockReturnValue(streamFalsoFallido("overload persistente"));

    const res = await POST(requestFalso(), ctxFalso("s1"));
    const texto = await res.text();

    expect(texto).toContain("event: error");
    expect(texto).not.toContain("event: done");
    // La sesion sigue viva: el recorrido esta persistido y reintentar re-lanza
    // SOLO la redaccion, sin repetirle la entrevista al usuario.
    expect(estadoFalso.sessions["s1"].closed_at).toBeFalsy();
    // 3 intentos: el hipo se reintenta, no se abandona al primer tropiezo.
    expect(messagesStreamFalso).toHaveBeenCalledTimes(3);
  });

  it("presupuesto excedido: NO se reintenta, se ensambla offline y se cierra", async () => {
    // El presupuesto no es un hipo: reintentar solo quemaria mas. Es el unico
    // caso que sigue cayendo al ensamblado offline, que para eso existe.
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: {
        recorrido: estadoRecorridoBase(),
        // El costo sale de los tokens ya gastados: 10M de salida en el modelo
        // del redactor rebasan cualquier presupuesto de sesion.
        acumulado: {
          ...acumuladoVacio,
          uso: { "claude-sonnet-4-6": { in: 0, out: 10_000_000, cache_read: 0, cache_write: 0 } },
        },
      },
    };

    const res = await POST(requestFalso(), ctxFalso("s1"));
    const texto = await res.text();
    expect(texto).toContain("event: aviso");
    const match = texto.match(/event: done\ndata: (.+)\n\n/);
    expect(match).toBeTruthy();
    expect(JSON.parse(match![1]).markdown).toContain("# Tu plan de accion");
    expect(estadoFalso.sessions["s1"].closed_at).toBeTruthy();
    // Ni un solo intento al modelo: el presupuesto se corta ANTES.
    expect(messagesStreamFalso).not.toHaveBeenCalled();
  });
});
