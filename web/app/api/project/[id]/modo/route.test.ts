// Fase 3.8 §3 — PATCH /api/project/[id]/modo: elegir/alternar el modo del
// camino. Valida contra MODO_CAMINO y persiste projects.modo_camino.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

import { PATCH } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1" }) };

function req(body: unknown) {
  return new Request("http://x/api/project/p1/modo", {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sembrarProyecto(modo: string | null = null) {
  estadoFalso.projects["p1"] = {
    id: "p1",
    user_id: "user-fake",
    titulo: "Idea",
    entrada_original: "una idea",
    session_count: 1,
    modo_camino: modo,
  };
}

describe("PATCH /api/project/[id]/modo (Fase 3.8)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("400 si modo_camino es inválido", async () => {
    sembrarProyecto();
    const res = await PATCH(req({ modo_camino: "turbo" }), PARAMS);
    expect(res.status).toBe(400);
  });

  it("401 si no hay usuario", async () => {
    sembrarProyecto();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await PATCH(req({ modo_camino: "fechas" }), PARAMS);
    expect(res.status).toBe(401);
  });

  it("persiste 'fechas' y lo devuelve", async () => {
    sembrarProyecto(null);
    const res = await PATCH(req({ modo_camino: "fechas" }), PARAMS);
    expect(res.status).toBe(200);
    expect((await res.json()).modo_camino).toBe("fechas");
    expect(estadoFalso.projects["p1"].modo_camino).toBe("fechas");
  });

  it("pausar (fechas→ritmo) cambia el modo sin tocar nada más", async () => {
    sembrarProyecto("fechas");
    const res = await PATCH(req({ modo_camino: "ritmo" }), PARAMS);
    expect(res.status).toBe(200);
    expect(estadoFalso.projects["p1"].modo_camino).toBe("ritmo");
  });
});
