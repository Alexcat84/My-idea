// Ciclo de replanteamiento, Fase 2 (decisiones del fundador, 27 sep 2026):
// POST /api/project/[id]/replantear, el paso 3 de "Replantear mi camino". Aquí
// nace la sesión: se aparta el precio de precios.ts (replanteamiento), cuentan
// el fusible y el límite diario, y una sola llamada a la IA propone dos o tres
// caminos anclados a conceptos del grafo aún no cubiertos. La IA se sustituye
// por un cliente falso que responde con los candidatos que la ruta le ofreció
// (así ningún veredicto depende de una clave real, regla de AGENTS.md).
import { beforeEach, describe, expect, it, vi } from "vitest";
import { SERVIDOR_PROYECTO } from "@/lib/i18n/mensajes/servidorProyecto";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/creditos", async (importOriginal) => {
  const real = await importOriginal<typeof import("@/lib/creditos")>();
  return {
    ...real,
    verificarSaldo: vi.fn(async () => ({ alcanza: true, creditos: 20 })),
    reservarCreditos: vi.fn(async () => ({ reservado: true, disponible: 10 })),
    resolverReserva: vi.fn(async () => undefined),
  };
});
vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  faltaSegundoFactor: async () => false,
}));
vi.mock("@/lib/supabase/server", () => ({ createClient: vi.fn(async () => supabaseFalso) }));
vi.mock("@/lib/rateLimit", () => ({
  identidadLimite: () => "id",
  mensajeFusible: () => "fusible",
  mensajeLimite: () => "limite",
  mensajeServicioNoDisponible: () => "caido",
  verificarFusibleGlobal: vi.fn(async () => ({ permitido: true })),
  verificarLimiteDiario: vi.fn(async () => ({ permitido: true })),
}));
// El bloque de realidad lee el Análisis entero; tiene sus propias pruebas.
vi.mock("@/lib/cicloApertura", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/cicloApertura")>()),
  realidadDelCiclo: vi.fn(async () => "Mi realidad medida: ciclo 2."),
}));

// La IA falsa: toma los ids de candidatos que la ruta le mandó y arma dos caminos.
let respuestaIA: (candidatos: string[]) => string = (c) =>
  JSON.stringify({
    caminos: [
      { titulo: "Vender por encargo", descripcion: "Sin local.", nodos: [c[0], c[1], "inventado"] },
      { titulo: "Feria del barrio", descripcion: "Un puesto.", nodos: [c[2], c[3]] },
    ],
  });
const create = vi.fn(async (req: { messages: Array<{ content: string }> }) => {
  const ctx = JSON.parse(req.messages[0].content) as { candidatos: Array<{ id: string }> };
  return {
    content: [{ type: "text", text: respuestaIA(ctx.candidatos.map((x) => x.id)) }],
    usage: { input_tokens: 1000, output_tokens: 200 },
  };
});
vi.mock("@/lib/anthropicClient", () => ({ createAnthropicClient: () => ({ messages: { create } }) }));

import { GET, POST } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1" }) };
const req = (body: unknown) =>
  new Request("http://x/api/project/p1/replantear", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

function sembrar() {
  estadoFalso.projects["p1"] = {
    id: "p1",
    user_id: "user-fake",
    titulo: "Pan",
    entrada_original: "vendo pan",
    estado_vivo: "vende pan en su barrio",
    fase_actual: "validacion",
  };
  estadoFalso.sessions["s0"] = { id: "s0", project_id: "p1", tipo: "inicial", dominio: "core", created_at: "2026-09-01T00:00:00Z" };
  estadoFalso.plans.push({
    id: "pl0",
    session_id: "s0",
    dominio: "core",
    etiqueta: "completo",
    contenido_md: "# Pan\n\n## Etapa 1: Valida\n\n## Etapa 2: Local\n",
    created_at: "2026-09-01T00:00:00Z",
  });
  const item = (id: string, etapa: number, orden: number, texto: string, estado: string, completed_at: string | null) => ({
    id,
    project_id: "p1",
    plan_id: "pl0",
    dominio: "core",
    etapa,
    orden,
    texto,
    destacado: false,
    estado,
    nota: null,
    completed_at,
    created_at: "2026-09-01T00:00:00Z",
  });
  estadoFalso.checklistItems.push(
    item("t1", 1, 1, "Hablar con 5 panaderías", "hecho", "2026-09-10T15:00:00Z"),
    item("t2", 2, 1, "Rentar un local", "hecho", "2026-09-12T15:00:00Z"),
    item("t3", 2, 2, "Pintar el local", "pendiente", null)
  );
}

describe("POST replantear: el paso 3 de Replantear mi camino", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    create.mockClear();
    respuestaIA = (c) =>
      JSON.stringify({
        caminos: [
          { titulo: "Vender por encargo", descripcion: "Sin local.", nodos: [c[0], c[1], "inventado"] },
          { titulo: "Feria del barrio", descripcion: "Un puesto.", nodos: [c[2], c[3]] },
        ],
      });
  });

  it("sin historia: 400 con el mensaje del catálogo, sin apartar nada ni llamar a la IA", async () => {
    sembrar();
    const { reservarCreditos } = await import("@/lib/creditos");
    vi.mocked(reservarCreditos).mockClear();
    const res = await POST(req({ historia: "   ", suelta: [] }), PARAMS);
    expect(res.status).toBe(400);
    expect((await res.json()).error).toBe(SERVIDOR_PROYECTO.es.follow.historiaObligatoria);
    expect(reservarCreditos).not.toHaveBeenCalled();
    expect(create).not.toHaveBeenCalled();
  });

  it("aparta el precio del replanteamiento (5, precios.ts) con la clave plan:{sesión}", async () => {
    sembrar();
    const { reservarCreditos } = await import("@/lib/creditos");
    vi.mocked(reservarCreditos).mockClear();
    await POST(req({ historia: "Se cayó el local.", suelta: [] }), PARAMS);
    expect(reservarCreditos).toHaveBeenCalledWith(expect.any(String), expect.stringMatching(/^plan:/), "replanteamiento", 5);
  });

  it("200: dos caminos sin conceptos inventados, y la sesión guarda la historia, lo que se conserva y lo que se suelta", async () => {
    sembrar();
    const res = await POST(req({ historia: "  Se cayó el local.  ", suelta: ["t2"], dominio: "core" }), PARAMS);
    expect(res.status).toBe(200);
    const data = (await res.json()) as { session_id: string; caminos: Array<{ id: string; titulo: string; descripcion: string }> };
    // Solo id, título y descripción viajan a la pantalla (los conceptos se quedan en el servidor).
    expect(data.caminos).toEqual([
      { id: "a", titulo: "Vender por encargo", descripcion: "Sin local." },
      { id: "b", titulo: "Feria del barrio", descripcion: "Un puesto." },
    ]);
    const sesion = estadoFalso.sessions[data.session_id] as {
      tipo: string;
      estado_recorrido: { recorrido: { esSeguimiento: boolean; ciclo: Record<string, unknown>; fase: string }; acumulado: { uso_por_componente?: Record<string, number> } };
    };
    expect(sesion.tipo).toBe("seguimiento");
    const { recorrido } = sesion.estado_recorrido;
    expect(recorrido.esSeguimiento).toBe(true);
    expect(recorrido.fase).toBe("listo_para_plan");
    // t1 hecha y no soltada: se conserva. t2 soltada. t3 no es hecha: no entra en ninguna.
    expect(recorrido.ciclo).toMatchObject({
      tipo: "replantear",
      historia: "Se cayó el local.",
      conserva: [{ id: "t1", texto: "Hablar con 5 panaderías", completed_at: "2026-09-10T15:00:00Z" }],
      suelta: [{ id: "t2", texto: "Rentar un local" }],
      caminoElegido: null,
    });
    // El primer camino perdió "inventado": le quedan dos conceptos.
    const caminos = recorrido.ciclo.caminos as Array<{ nodos: string[] }>;
    expect(caminos[0].nodos).toHaveLength(2);
    expect(caminos[0].nodos).not.toContain("inventado");
    // Una sola llamada a la IA, que ve la historia y el plan anterior.
    expect(create).toHaveBeenCalledTimes(1);
    const ctx = JSON.parse(create.mock.calls[0][0].messages[0].content);
    expect(ctx.historia).toBe("Se cayó el local.");
    expect(ctx.se_conserva).toEqual(["Hablar con 5 panaderías"]);
    expect(ctx.se_suelta).toEqual(["Rentar un local"]);
    expect(ctx.plan_anterior.etapas.map((e: { titulo: string }) => e.titulo)).toEqual(["Valida", "Local"]);
  });

  it("si la IA no da dos caminos válidos: 503 con el mensaje del catálogo y se suelta lo apartado", async () => {
    sembrar();
    respuestaIA = () => JSON.stringify({ caminos: [{ titulo: "Solo uno", descripcion: "x", nodos: ["inventado"] }] });
    const { resolverReserva } = await import("@/lib/creditos");
    vi.mocked(resolverReserva).mockClear();
    const res = await POST(req({ historia: "Se cayó el local.", suelta: [] }), PARAMS);
    expect(res.status).toBe(503);
    expect((await res.json()).error).toBe(SERVIDOR_PROYECTO.es.follow.caminosFallidos);
    expect(resolverReserva).toHaveBeenCalledWith(expect.stringMatching(/^plan:/), "liberada");
  });
});

describe("POST replantear: volver a pedir caminos no deja precio apartado", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    // La prueba anterior deja a la IA falsa respondiendo basura: se restablece.
    respuestaIA = (c) =>
      JSON.stringify({
        caminos: [
          { titulo: "Vender por encargo", descripcion: "Sin local.", nodos: [c[0], c[1]] },
          { titulo: "Feria del barrio", descripcion: "Un puesto.", nodos: [c[2], c[3]] },
        ],
      });
  });

  it("con session_previa (un replanteamiento sin plan), suelta su reserva y la cierra antes de apartar otra vez", async () => {
    sembrar();
    estadoFalso.sessions["s-prev"] = {
      id: "s-prev",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: { ciclo: { tipo: "replantear" } }, acumulado: {} },
    };
    const { resolverReserva, reservarCreditos } = await import("@/lib/creditos");
    vi.mocked(resolverReserva).mockClear();
    vi.mocked(reservarCreditos).mockClear();
    const res = await POST(req({ historia: "Se cayó el local.", suelta: [], session_previa: "s-prev" }), PARAMS);
    expect(res.status).toBe(200);
    expect(resolverReserva).toHaveBeenCalledWith("plan:s-prev", "liberada");
    expect(estadoFalso.sessions["s-prev"].closed_at).toBeTruthy();
    // La liberación va ANTES de la reserva nueva.
    const orden = (fn: unknown) => (fn as { mock: { invocationCallOrder: number[] } }).mock.invocationCallOrder[0];
    expect(orden(resolverReserva)).toBeLessThan(orden(reservarCreditos));
  });

  it("una sesión previa que ya dio su plan, o que no es de replantear, no se toca", async () => {
    sembrar();
    estadoFalso.sessions["s-prof"] = {
      id: "s-prof",
      project_id: "p1",
      closed_at: null,
      estado_recorrido: { recorrido: { ciclo: { tipo: "profundizar" } }, acumulado: {} },
    };
    const { resolverReserva } = await import("@/lib/creditos");
    vi.mocked(resolverReserva).mockClear();
    await POST(req({ historia: "Se cayó el local.", suelta: [], session_previa: "s-prof" }), PARAMS);
    expect(resolverReserva).not.toHaveBeenCalledWith("plan:s-prof", "liberada");
    expect(estadoFalso.sessions["s-prof"].closed_at).toBeNull();
  });
});

describe("GET replantear: ¿alcanza para abrir el ritual?", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("con saldo: 200 con el precio del replanteamiento de ese espacio (5 y 5)", async () => {
    sembrar();
    const core = await GET(new Request("http://x/api/project/p1/replantear"), PARAMS);
    expect(await core.json()).toEqual({ alcanza: true, costo: 5 });
    const mundo = await GET(new Request("http://x/api/project/p1/replantear?dominio=quality"), PARAMS);
    expect(await mundo.json()).toEqual({ alcanza: true, costo: 5 });
  });
});
