// Fase 3.0: prueba de integracion de GET /api/projects.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

import { GET } from "./route";

describe("GET /api/projects", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("401 si no hay usuario autenticado", async () => {
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await GET();
    expect(res.status).toBe(401);
  });

  it("lista los proyectos, mas recientes primero", async () => {
    estadoFalso.projects["p-viejo"] = {
      id: "p-viejo",
      titulo: "Idea vieja",
      entrada_original: "una idea vieja",
      fase_actual: "ideacion",
      session_count: 1,
      status: "active",
      updated_at: "2026-01-01T00:00:00.000Z",
    };
    estadoFalso.projects["p-nuevo"] = {
      id: "p-nuevo",
      titulo: "Idea nueva",
      entrada_original: "una idea nueva",
      fase_actual: "validacion",
      session_count: 2,
      status: "active",
      tipo_oferta: "digital",
      updated_at: "2026-06-01T00:00:00.000Z",
    };

    const res = await GET();
    expect(res.status).toBe(200);
    const body = await res.json();
    expect(body.proyectos).toHaveLength(2);
    expect(body.proyectos[0].id).toBe("p-nuevo");
    expect(body.proyectos[0].tipo_oferta).toBe("digital");
    expect(body.proyectos[1].id).toBe("p-viejo");
  });

  it("lista vacia si el usuario no tiene proyectos", async () => {
    const res = await GET();
    const body = await res.json();
    expect(body.proyectos).toEqual([]);
  });
});
