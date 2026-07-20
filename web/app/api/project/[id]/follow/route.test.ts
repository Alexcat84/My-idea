// Fase 4.2 §1 — POST /api/project/[id]/follow con `dominio`: los MUROS del
// follow de mundo. Todos devuelven antes de tocar el modelo, así que se prueban
// sin mockearlo: si alguno cayera, la ruta gastaría un arranque (y, cuando la
// ETAPA 2 despierte, 2 créditos) en algo que no debía pasar.
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

  it("401 si no hay usuario, sea cual sea el dominio", async () => {
    sembrarProyecto();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    expect((await POST(req({ dominio: "quality" }), PARAMS)).status).toBe(401);
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
