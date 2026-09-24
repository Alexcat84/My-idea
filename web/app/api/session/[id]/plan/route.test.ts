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

vi.mock("@/lib/creditos", async (importOriginal) => {
  // ETAPA 2: las funciones PURAS (conceptoDelPlan, montos, mensajes) son las
  // reales; las que tocan el ledger (RPC service-role) se stubean con saldo
  // holgado -- la ley de AGENTS.md: ningun test depende de secretos del
  // ambiente, y el ledger REAL se verifica en vivo en el vuelo de dinero.
  const real = await importOriginal<typeof import("@/lib/creditos")>();
  return {
    ...real,
    saldoDe: vi.fn(async () => 20),
    verificarSaldo: vi.fn(async () => ({ alcanza: true, creditos: 20 })),
    cobrar: vi.fn(async () => 15),
    reembolsar: vi.fn(async () => 20),
    otorgarCortesia: vi.fn(async () => 20),
    // AUD-09 M25: la reserva de créditos (migración 042).
    reservarCreditos: vi.fn(async () => ({ reservado: true, disponible: 10 })),
    resolverReserva: vi.fn(async () => undefined),
  };
});
// El gate 2FA tiene su propia cobertura (dosFactores.test + el vuelo de
// cuenta); aqui se abre para probar la logica de la ruta.
vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  faltaSegundoFactor: async () => false,
}));

// AUD-09 M26: para reproducir una falla ENTRE guardar el plan y cerrar la
// sesión, insertarChecklist puede fallar una vez a pedido (por defecto, real).
let fallarChecklistUnaVez = false;
vi.mock("@/lib/db", async (importOriginal) => {
  const real = await importOriginal<typeof import("@/lib/db")>();
  return {
    ...real,
    insertarChecklist: async (...a: Parameters<typeof real.insertarChecklist>) => {
      if (fallarChecklistUnaVez) {
        fallarChecklistUnaVez = false;
        throw new Error("falla simulada al escribir el checklist");
      }
      return real.insertarChecklist(...a);
    },
  };
});
vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

const messagesStreamFalso = vi.fn();
vi.mock("@/lib/anthropicClient", () => ({
  createAnthropicClient: vi.fn(() => ({ messages: { stream: messagesStreamFalso } })),
}));

import { POST } from "./route";
import { cobrar } from "@/lib/creditos";

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
    // AUD-09 B07a: el evento de error no lleva el mensaje interno al cliente.
    expect(texto).not.toContain("overload persistente");
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
    const done = await leerEventoDone(res);
    // AUD-09 H02: el aviso ya no es un evento interno que la pantalla ignoraba;
    // viaja en el done, marcado como version basica.
    expect(done.version_basica).toBe(true);
    expect(String(done.markdown)).toContain("# Tu plan de accion");
    expect(estadoFalso.sessions["s1"].closed_at).toBeTruthy();
    // Ni un solo intento al modelo: el presupuesto se corta ANTES.
    expect(messagesStreamFalso).not.toHaveBeenCalled();
  });

  // AUD-09 H02, politica del fundador (25 sep 2026): se verifica al empezar y
  // se cobra al final SOLO si se entrego lo prometido. Un plan armado sin IA
  // no es lo prometido: se entrega gratis, con un aviso honesto en pantalla.
  // Antes se cobraba completo y el aviso (un evento que la pantalla ignoraba)
  // hablaba en jerga interna.
  it("un plan armado sin IA NO se cobra y lleva su aviso honesto en el done", async () => {
    vi.mocked(cobrar).mockClear();
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: {
        recorrido: estadoRecorridoBase(),
        acumulado: {
          ...acumuladoVacio,
          uso: { "claude-sonnet-4-6": { in: 0, out: 10_000_000, cache_read: 0, cache_write: 0 } },
        },
      },
    };

    const res = await POST(requestFalso(), ctxFalso("s1"));
    const done = await leerEventoDone(res);
    expect(cobrar).not.toHaveBeenCalled();
    expect(done.version_basica).toBe(true);
    expect(done.creditos_restantes).toBeNull();
    expect(String(done.aviso)).toMatch(/no se te cobró/i);
    // El techo SI se cruzo: la sesion lo registra (antes quedaba en false).
    expect(estadoFalso.sessions["s1"].presupuesto_excedido).toBe(true);
  });

  // AUD-09, decision del fundador (25 sep 2026): UN SELLO DE PAGO SOLO EXISTE
  // SI HUBO PAGO. Un plan basico de mundo no escribe plan_pagado_at; se marca
  // con su propio campo (plan_basico_at) y el mundo ofrece el plan completo.
  function sembrarMundo(acumulado: Record<string, unknown>) {
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
    estadoFalso.projectUnlocks.push({ project_id: "p1", dominio: "quality", resumen_md: "diag", plan_pagado_at: null });
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      dominio: "quality",
      closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado },
    };
  }
  const acumuladoAgotado = {
    ...acumuladoVacio,
    uso: { "claude-sonnet-4-6": { in: 0, out: 10_000_000, cache_read: 0, cache_write: 0 } },
  };

  it("un plan BASICO de mundo no sella la compra: se marca con plan_basico_at", async () => {
    sembrarMundo(acumuladoAgotado);
    const res = await POST(requestFalso(), ctxFalso("s1"));
    await leerEventoDone(res);
    const fila = estadoFalso.projectUnlocks[0];
    expect(fila.plan_pagado_at ?? null).toBeNull();
    expect(fila.plan_basico_at).toBeTruthy();
    expect(estadoFalso.bitacora.some((e) => e.tipo === "preview_a_compra")).toBe(false);
  });

  it("un plan de mundo redactado con IA y cobrado SI sella la compra", async () => {
    sembrarMundo(acumuladoVacio);
    messagesStreamFalso.mockReturnValue(streamFalsoExitoso(["# Tu plan", "", "## Etapa 1: Arranca", "", "- [ ] Haz algo concreto", ""].join("\n")));
    const res = await POST(requestFalso(), ctxFalso("s1"));
    await leerEventoDone(res);
    expect(estadoFalso.projectUnlocks[0].plan_pagado_at).toBeTruthy();
  });

  // AUD-09 H05: PREVIEW_MUNDOS_PLAN §4, "si el proyecto cambio de ciclo entre
  // preview y compra, el plan se genera con el estado vivo ACTUAL". La compra
  // usaba el perfil congelado del preview y, al comprimir sin estado anterior,
  // pisaba projects.estado_vivo (lo aprendido en el ciclo del nucleo se perdia)
  // y ponia la fase del proyecto en la del ultimo nodo del mundo.
  it("comprar un mundo tras un ciclo del nucleo usa el estado vivo ACTUAL y no lo pisa", async () => {
    estadoFalso.projects["p1"] = {
      id: "p1",
      session_count: 3,
      titulo: null,
      numeros_proyecto: {},
      estado_vivo: "E2: ya vende 30 macetas al mes tras el seguimiento",
      fase_actual: "ejecucion",
    };
    estadoFalso.projectUnlocks.push({ project_id: "p1", dominio: "quality", resumen_md: "diag", plan_pagado_at: null });
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      dominio: "quality",
      closed_at: null,
      estado_recorrido: {
        recorrido: estadoRecorridoBase({ perfilSesion: "E1: vende 12 macetas al mes." }),
        acumulado: acumuladoVacio,
      },
    };
    messagesStreamFalso.mockReturnValue(streamFalsoExitoso(["# Tu plan", "", "## Etapa 1: Arranca", "", "- [ ] Haz algo concreto", ""].join("\n")));
    const res = await POST(requestFalso(), ctxFalso("s1"));
    await leerEventoDone(res);
    // el redactor recibio el estado actual
    const payload = JSON.stringify(messagesStreamFalso.mock.calls[0][0]);
    expect(payload).toContain("E2: ya vende 30 macetas");
    // el estado vivo del proyecto conserva lo del ciclo del nucleo
    const proyecto = estadoFalso.projects["p1"] as Record<string, unknown>;
    expect(String(proyecto.estado_vivo)).toContain("E2: ya vende 30 macetas");
    // y la fase del proyecto es la del nucleo, no la del mundo
    expect(proyecto.fase_actual).toBe("ejecucion");
  });

  it("un plan redactado con IA SI se cobra, sin aviso de version basica", async () => {
    vi.mocked(cobrar).mockClear();
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
    estadoFalso.sessions["s1"] = {
      id: "s1",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoVacio },
    };
    messagesStreamFalso.mockReturnValue(streamFalsoExitoso(["# Tu plan", "", "## Etapa 1: Arranca", "", "- [ ] Haz algo concreto", ""].join("\n")));
    const res = await POST(requestFalso(), ctxFalso("s1"));
    const done = await leerEventoDone(res);
    // Calculo a mano: nucleo, primera entrevista -> plan_completo = 10.
    expect(cobrar).toHaveBeenCalledWith("user-fake", "plan_completo", 10, "plan:s1");
    expect(done.version_basica).toBe(false);
  });
});

// AUD-09 M25 (tanda 7A, dinero): la entrega renueva la reserva de SU sesión
// (clave plan:{sessionId}) antes de gastar un token, la marca COBRADA al cobrar
// y la LIBERA cuando no cobra (plan sin IA).
describe("POST /api/session/[id]/plan: reserva de créditos (AUD-09 M25)", () => {
  beforeEach(async () => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    messagesStreamFalso.mockReset();
    const c = await import("@/lib/creditos");
    vi.mocked(c.reservarCreditos).mockClear();
    vi.mocked(c.resolverReserva).mockClear();
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
  });

  it("con IA: renueva la reserva de su clave, cobra y la marca cobrada", async () => {
    const { reservarCreditos, resolverReserva } = await import("@/lib/creditos");
    estadoFalso.sessions["s1"] = {
      id: "s1", project_id: "p1", closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoVacio },
    };
    messagesStreamFalso.mockReturnValue(streamFalsoExitoso(["# Tu plan", "", "## Etapa 1: Arranca", "", "- [ ] Haz algo concreto", ""].join(String.fromCharCode(10))));
    await leerEventoDone(await POST(requestFalso(), ctxFalso("s1")));
    // A MANO: núcleo, primera entrevista -> plan_completo = 10.
    expect(reservarCreditos).toHaveBeenCalledWith("user-fake", "plan:s1", "plan_completo", 10);
    expect(resolverReserva).toHaveBeenCalledWith("plan:s1", "cobrada");
  });

  it("sin IA (plan básico): no cobra y LIBERA la reserva", async () => {
    const { resolverReserva } = await import("@/lib/creditos");
    estadoFalso.sessions["s1"] = {
      id: "s1", project_id: "p1", closed_at: null,
      estado_recorrido: {
        recorrido: estadoRecorridoBase(),
        acumulado: { ...acumuladoVacio, uso: { "claude-sonnet-4-6": { in: 0, out: 10_000_000, cache_read: 0, cache_write: 0 } } },
      },
    };
    await leerEventoDone(await POST(requestFalso(), ctxFalso("s1")));
    expect(resolverReserva).toHaveBeenCalledWith("plan:s1", "liberada");
  });

  it("si el saldo ya está apartado por otra sesión: 402 antes de gastar un token", async () => {
    const { reservarCreditos } = await import("@/lib/creditos");
    vi.mocked(reservarCreditos).mockResolvedValueOnce({ reservado: false, disponible: 0 });
    estadoFalso.sessions["s1"] = {
      id: "s1", project_id: "p1", closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoVacio },
    };
    const res = await POST(requestFalso(), ctxFalso("s1"));
    expect(res.status).toBe(402);
    expect(messagesStreamFalso).not.toHaveBeenCalled();
  });
});

// AUD-09 M26 (tanda 7A, datos): la sospecha era que, si algo falla ENTRE
// guardarPlan y cerrarSesion, el reintento crea un segundo plan y su checklist.
// Decisión del fundador: primero reproducirlo; si no se reproduce, se documenta
// y no se toca el código. Esta prueba es la reproducción.
describe("reintento tras una falla entre guardar el plan y cerrar la sesión (AUD-09 M26)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    messagesStreamFalso.mockReset();
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1, titulo: null, numeros_proyecto: {} };
    estadoFalso.sessions["s1"] = {
      id: "s1", project_id: "p1", closed_at: null,
      estado_recorrido: { recorrido: estadoRecorridoBase(), acumulado: acumuladoVacio },
    };
    messagesStreamFalso.mockReturnValue(streamFalsoExitoso(["# Tu plan", "", "## Etapa 1: Arranca", "", "- [ ] Haz algo concreto", ""].join(String.fromCharCode(10))));
  });

  it("el reintento no deja dos planes de la misma sesión", async () => {
    fallarChecklistUnaVez = true;
    const primero = await (await POST(requestFalso(), ctxFalso("s1"))).text();
    expect(primero).toMatch(/event: error/);
    // la sesión sigue abierta: el usuario puede reintentar
    expect(estadoFalso.sessions["s1"].closed_at).toBeNull();
    await leerEventoDone(await POST(requestFalso(), ctxFalso("s1")));
    const planesDeLaSesion = estadoFalso.plans.filter((p) => (p as { session_id?: string }).session_id === "s1");
    expect(planesDeLaSesion).toHaveLength(1);
  });
});

