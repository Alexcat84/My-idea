// PATCH /api/project/[id]/modo: elegir/alternar el modo del camino POR ESPACIO
// ("todo separado", migration 032). Valida contra MODO_CAMINO y persiste en
// project_modos (project_id, dominio). El core dual-lee su modo previo.
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

function modoDe(dominio: string): string | undefined {
  const fila = estadoFalso.projectModos.find(
    (r) => (r as Record<string, unknown>).project_id === "p1" && (r as Record<string, unknown>).dominio === dominio
  );
  return fila ? ((fila as Record<string, unknown>).modo_camino as string) : undefined;
}

describe("PATCH /api/project/[id]/modo (todo separado: modo por espacio)", () => {
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

  it("persiste 'fechas' del core en project_modos y lo devuelve", async () => {
    sembrarProyecto(null);
    const res = await PATCH(req({ modo_camino: "fechas" }), PARAMS);
    expect(res.status).toBe(200);
    expect((await res.json()).modo_camino).toBe("fechas");
    expect(modoDe("core")).toBe("fechas");
  });

  it("pausar (fechas→ritmo) del core: dual-read del previo y upsert del nuevo", async () => {
    sembrarProyecto("fechas"); // sin fila en project_modos: el previo cae a projects.modo_camino
    const res = await PATCH(req({ modo_camino: "ritmo" }), PARAMS);
    expect(res.status).toBe(200);
    expect(modoDe("core")).toBe("ritmo");
  });

  it("un MUNDO tiene su propio modo, SEPARADO del core", async () => {
    sembrarProyecto("ritmo");
    const res = await PATCH(req({ modo_camino: "fechas", dominio: "quality" }), PARAMS);
    expect(res.status).toBe(200);
    expect((await res.json()).dominio).toBe("quality");
    expect(modoDe("quality")).toBe("fechas");
    // escribir el modo del mundo NO crea ni toca la fila del core
    expect(modoDe("core")).toBeUndefined();
  });
});
