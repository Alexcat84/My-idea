// Fase 3.8 §5 — POST /api/project/[id]/realizar: marcar realizada / reabrir.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

import { POST } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1" }) };

function req(body: unknown) {
  return new Request("http://x/api/project/p1/realizar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sembrar(realizada: string | null = null) {
  estadoFalso.projects["p1"] = {
    id: "p1",
    user_id: "user-fake",
    entrada_original: "idea",
    session_count: 1,
    realizada_at: realizada,
  };
}

describe("POST /api/project/[id]/realizar (Fase 3.8)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("400 si la accion es inválida", async () => {
    sembrar();
    expect((await POST(req({ accion: "borrar" }), PARAMS)).status).toBe(400);
  });

  it("401 si no hay usuario", async () => {
    sembrar();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    expect((await POST(req({ accion: "realizar" }), PARAMS)).status).toBe(401);
  });

  it("realizar sella realizada_at (no null)", async () => {
    sembrar(null);
    const res = await POST(req({ accion: "realizar" }), PARAMS);
    expect(res.status).toBe(200);
    expect((await res.json()).realizada_at).toBeTruthy();
    expect(estadoFalso.projects["p1"].realizada_at).toBeTruthy();
  });

  it("reabrir pone realizada_at a null", async () => {
    sembrar("2026-05-01T12:00:00.000Z");
    const res = await POST(req({ accion: "reabrir" }), PARAMS);
    expect(res.status).toBe(200);
    expect((await res.json()).realizada_at).toBeNull();
    expect(estadoFalso.projects["p1"].realizada_at).toBeNull();
  });
});
