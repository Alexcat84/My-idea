// Fase 4.2 §1 — POST /api/project/[id]/follow con `dominio`: los MUROS del
// follow de mundo. Todos devuelven antes de tocar el modelo, así que se prueban
// sin mockearlo: si alguno cayera, la ruta gastaría un arranque en algo que no
// debía pasar.
//
// La composición en sí (qué ítems entran, qué dice el bloque) se prueba en las
// funciones puras — itemsDelUltimoPlanDe y construirBloqueRealidadMundo — y de
// punta a punta en el vuelo, con el motor real.
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

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));
// El fusible y el límite diario tocan la red: aquí siempre permiten, para que
// lo que falle sea lo que se está probando y no la infraestructura.
vi.mock("@/lib/rateLimit", () => ({
  identidadLimite: () => "id",
  MENSAJE_FUSIBLE: "fusible",
  MENSAJE_LIMITE: "limite",
  verificarFusibleGlobal: vi.fn(async () => ({ permitido: true })),
  verificarLimiteDiario: vi.fn(async () => ({ permitido: true })),
}));

import * as ruta from "./route";
import { POST } from "./route";

function req(body: unknown) {
  return new Request("http://x/api/project/p1/follow", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}
const PARAMS = { params: Promise.resolve({ id: "p1" }) };

function sembrarProyecto() {
  estadoFalso.projects["p1"] = {
    id: "p1",
    user_id: "user-fake",
    titulo: "Macetas",
    entrada_original: "vendo macetas",
    estado_vivo: "vende macetas de cemento",
    fase_actual: "ejecucion",
    session_count: 3,
  };
}

describe("POST follow con dominio — los muros del mundo (Fase 4.2)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("404 si el mundo no existe en el catálogo", async () => {
    sembrarProyecto();
    const res = await POST(req({ dominio: "mundo_inventado" }), PARAMS);
    expect(res.status).toBe(404);
  });

  it("403 si el mundo no está activado para esta idea (el muro de siempre)", async () => {
    sembrarProyecto();
    const res = await POST(req({ dominio: "quality" }), PARAMS);
    expect(res.status).toBe(403);
    expect(String((await res.json()).error)).toContain("Calidad y Confianza");
  });

  it("409 si el mundo está COMPLETADO: primero se reabre", async () => {
    sembrarProyecto();
    estadoFalso.projectUnlocks.push({
      project_id: "p1",
      dominio: "quality",
      completado_at: "2026-05-01T10:00:00Z",
    });
    const res = await POST(req({ dominio: "quality" }), PARAMS);
    expect(res.status).toBe(409);
    expect(String((await res.json()).error)).toContain("Reábrelo");
  });

  it("409 si el mundo aún no tiene checklist propio: su seguimiento nace de su plan", async () => {
    sembrarProyecto();
    estadoFalso.projectUnlocks.push({ project_id: "p1", dominio: "quality", completado_at: null });
    // Hay ítems CORE, pero ninguno del mundo: el follow del mundo no puede
    // caer al core como si nada (ese es el hallazgo V4 en su otra dirección).
    estadoFalso.checklistItems.push({
      plan_id: "core1",
      project_id: "p1",
      dominio: "core",
      etapa: 1,
      texto: "Cierra tu costo",
      destacado: false,
      estado: "hecho",
      created_at: "2026-04-01T10:00:00Z",
    });
    const res = await POST(req({ dominio: "quality" }), PARAMS);
    expect(res.status).toBe(409);
    expect(String((await res.json()).error)).toContain("Primero explora");
  });

  it("sin saldo responde 402 SIN gastar el límite diario ni el fusible (AUD-09)", async () => {
    sembrarProyecto();
    const { verificarSaldo } = await import("@/lib/creditos");
    const rl = await import("@/lib/rateLimit");
    vi.mocked(rl.verificarLimiteDiario).mockClear();
    vi.mocked(rl.verificarFusibleGlobal).mockClear();
    vi.mocked(verificarSaldo).mockResolvedValueOnce({ alcanza: false, creditos: 0 });
    const res = await POST(req({ detalles: "avancé", enfoque: null }), PARAMS);
    expect(res.status).toBe(402);
    expect(rl.verificarLimiteDiario).not.toHaveBeenCalled();
    expect(rl.verificarFusibleGlobal).not.toHaveBeenCalled();
  });

  it("401 si no hay usuario, sea cual sea el dominio", async () => {
    sembrarProyecto();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    expect((await POST(req({ dominio: "quality" }), PARAMS)).status).toBe(401);
  });

  // AUD-09 (tanda 5, dinero): con la idea realizada no se puede pagar un
  // seguimiento del nucleo. Antes follow no miraba realizada_at (si lo hacia
  // con un mundo completado): se cobraba un ciclo despues del cierre y nacia un
  // "ciclo N" posterior a REALIZADA en el timeline.
  it("409 si la idea esta REALIZADA: el nucleo no se replanifica cerrado, y no se verifica saldo", async () => {
    sembrarProyecto();
    estadoFalso.projects["p1"].realizada_at = "2026-09-01T10:00:00Z";
    const { verificarSaldo } = await import("@/lib/creditos");
    vi.mocked(verificarSaldo).mockClear();
    const res = await POST(req({ detalles: "algo" }), PARAMS);
    expect(res.status).toBe(409);
    expect(verificarSaldo).not.toHaveBeenCalled();
  });

  it("un mundo COMPLETADO no bloquea el follow CORE (son subproyectos distintos)", async () => {
    sembrarProyecto();
    estadoFalso.projectUnlocks.push({
      project_id: "p1",
      dominio: "quality",
      completado_at: "2026-05-01T10:00:00Z",
    });
    // Sin dominio en el body: el follow de siempre. No debe morir en los muros
    // del mundo — pasa de largo (y sigue su camino, que aquí no ejercitamos).
    const res = await POST(req({ detalles: "algo" }), PARAMS).catch(() => null);
    expect(res?.status).not.toBe(403);
    expect(res?.status).not.toBe(409);
  });
});

// AUD-09 M25 (tanda 7A, dinero): el seguimiento reserva su precio al empezar,
// con la clave del cobro de la sesión nueva; si otra sesión ya apartó el saldo,
// 402 sin crear sesión ni gastar el límite del día.
describe("POST follow: reserva de créditos (AUD-09 M25)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("reserva el precio del seguimiento del núcleo con la clave plan:{sesión}", async () => {
    sembrarProyecto();
    const { reservarCreditos } = await import("@/lib/creditos");
    vi.mocked(reservarCreditos).mockClear();
    await POST(req({ detalles: "avancé" }), PARAMS).catch(() => null);
    // A MANO: núcleo, seguimiento -> PRECIOS.seguimiento = 5.
    expect(reservarCreditos).toHaveBeenCalledWith(expect.any(String), expect.stringMatching(/^plan:/), "seguimiento", 5);
  });

  it("si la reserva no alcanza: 402 sin crear sesión ni gastar el límite", async () => {
    sembrarProyecto();
    const { reservarCreditos } = await import("@/lib/creditos");
    const rl = await import("@/lib/rateLimit");
    vi.mocked(rl.verificarLimiteDiario).mockClear();
    vi.mocked(reservarCreditos).mockResolvedValueOnce({ reservado: false, disponible: 0 });
    const res = await POST(req({ detalles: "avancé" }), PARAMS);
    expect(res.status).toBe(402);
    expect(Object.values(estadoFalso.sessions)).toHaveLength(0);
    expect(rl.verificarLimiteDiario).not.toHaveBeenCalled();
  });
});

// AUD-09 M22 (tanda 7A, dinero): el canon §5 pide rechazar ANTES de que el
// usuario escriba su "qué pasó". El ritual se abría sin consultar el saldo y el
// 402 llegaba después de escribir. GET follow responde si alcanza, sin gastar el
// límite del día ni apartar nada.
describe("GET follow: ¿alcanza para el ritual? (AUD-09 M22)", () => {
  const pedirGet = (q = "") =>
    (ruta as unknown as { GET: (r: Request, p: typeof PARAMS) => Promise<Response> }).GET(
      new Request(`http://x/api/project/p1/follow${q}`),
      PARAMS
    );
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("existe", () => {
    expect(typeof (ruta as Record<string, unknown>).GET).toBe("function");
  });

  it("sin saldo: 402 con el mensaje de siempre, sin gastar el límite ni reservar", async () => {
    sembrarProyecto();
    const { verificarSaldo, reservarCreditos } = await import("@/lib/creditos");
    const rl = await import("@/lib/rateLimit");
    vi.mocked(rl.verificarLimiteDiario).mockClear();
    vi.mocked(reservarCreditos).mockClear();
    vi.mocked(verificarSaldo).mockResolvedValueOnce({ alcanza: false, creditos: 2, apartados: 0 });
    const res = await pedirGet();
    expect(res.status).toBe(402);
    // A MANO: núcleo, seguimiento -> PRECIOS.seguimiento = 5.
    expect((await res.json()).error).toBe("Te quedan 2 créditos; esto cuesta 5. Tu trabajo queda guardado tal como está.");
    expect(rl.verificarLimiteDiario).not.toHaveBeenCalled();
    expect(reservarCreditos).not.toHaveBeenCalled();
  });

  it("con saldo: 200 con el costo del seguimiento de ese espacio", async () => {
    sembrarProyecto();
    const res = await pedirGet("?dominio=quality");
    expect(res.status).toBe(200);
    // A MANO: mundo, seguimiento -> PRECIOS.mundo_seguimiento = 5.
    expect(await res.json()).toEqual({ alcanza: true, costo: 5 });
  });
});
