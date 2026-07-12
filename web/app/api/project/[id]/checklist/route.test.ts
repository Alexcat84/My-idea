// Fase 3.8 §2/§4 — pruebas del PATCH del checklist ampliado con el sentido
// del tiempo: completed_at (timeline real, para TODOS) y fecha_base
// (replanificación que NO reescribe la historia).
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
  return new Request("http://x/api/project/p1/checklist", {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sembrarItem(extra: Record<string, unknown> = {}) {
  estadoFalso.projects["p1"] = {
    id: "p1",
    user_id: "user-fake",
    titulo: "Idea",
    entrada_original: "una idea",
    session_count: 1,
  };
  estadoFalso.checklistItems.push({
    id: "it1",
    project_id: "p1",
    plan_id: "plan-1",
    dominio: "core",
    etapa: 1,
    orden: 0,
    texto: "Compra dos termos",
    destacado: false,
    estado: "pendiente",
    nota: null,
    completed_at: null,
    fecha_base: null,
    fecha_base_origen: null,
    fecha_base_original: null,
    ...extra,
  });
}

describe("PATCH /api/project/[id]/checklist — sentido del tiempo (Fase 3.8)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("401 si no hay usuario", async () => {
    sembrarItem();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await PATCH(req({ item_id: "it1", estado: "hecho" }), PARAMS);
    expect(res.status).toBe(401);
  });

  it("400 si falta item_id", async () => {
    sembrarItem();
    const res = await PATCH(req({ estado: "hecho" }), PARAMS);
    expect(res.status).toBe(400);
  });

  it("400 si no hay nada que actualizar", async () => {
    sembrarItem();
    const res = await PATCH(req({ item_id: "it1" }), PARAMS);
    expect(res.status).toBe(400);
  });

  it("marcar hecho SIN completed_at → default a ahora (no null)", async () => {
    sembrarItem();
    const antes = Date.now();
    const res = await PATCH(req({ item_id: "it1", estado: "hecho" }), PARAMS);
    expect(res.status).toBe(200);
    const { item } = await res.json();
    expect(item.estado).toBe("hecho");
    expect(item.completed_at).toBeTruthy();
    const t = Date.parse(item.completed_at);
    // el default cae dentro de una ventana razonable alrededor de ahora
    expect(t).toBeGreaterThanOrEqual(antes - 1000);
    expect(t).toBeLessThanOrEqual(Date.now() + 1000);
  });

  it("salir de hecho (a pendiente) limpia completed_at", async () => {
    sembrarItem({ estado: "hecho", completed_at: "2026-03-20T12:00:00.000Z" });
    const res = await PATCH(req({ item_id: "it1", estado: "pendiente" }), PARAMS);
    const { item } = await res.json();
    expect(item.estado).toBe("pendiente");
    expect(item.completed_at).toBeNull();
  });

  it("acepta completed_at pasado explícito", async () => {
    sembrarItem();
    // 2026-03-15 mediodía local → una fecha claramente pasada respecto a hoy (2026-07)
    const res = await PATCH(
      req({ item_id: "it1", estado: "hecho", completed_at: "2026-03-15T12:00:00.000Z" }),
      PARAMS
    );
    const { item } = await res.json();
    expect(item.completed_at).toBe("2026-03-15T12:00:00.000Z");
  });

  it("400 si completed_at es futuro", async () => {
    sembrarItem();
    const futuro = new Date(Date.now() + 5 * 24 * 3600 * 1000).toISOString();
    const res = await PATCH(req({ item_id: "it1", estado: "hecho", completed_at: futuro }), PARAMS);
    expect(res.status).toBe(400);
  });

  // Replanificación (§4): mover una fecha_base que existía (origen 'sugerida')
  // preserva la PRIMERA en fecha_base_original y el origen pasa a 'ajustada'.
  it("replan: preserva fecha_base_original y pone origen 'ajustada'", async () => {
    sembrarItem({ fecha_base: "2026-03-20T12:00:00.000Z", fecha_base_origen: "sugerida", fecha_base_original: null });
    const res = await PATCH(req({ item_id: "it1", fecha_base: "2026-03-27" }), PARAMS);
    const { item } = await res.json();
    expect(item.fecha_base).toBe("2026-03-27T00:00:00.000Z");
    expect(item.fecha_base_original).toBe("2026-03-20T12:00:00.000Z");
    expect(item.fecha_base_origen).toBe("ajustada");
  });

  it("replan repetido NO reescribe fecha_base_original (guarda solo la primera)", async () => {
    sembrarItem({
      fecha_base: "2026-03-27T12:00:00.000Z",
      fecha_base_origen: "ajustada",
      fecha_base_original: "2026-03-20T12:00:00.000Z",
    });
    const res = await PATCH(req({ item_id: "it1", fecha_base: "2026-04-03" }), PARAMS);
    const { item } = await res.json();
    expect(item.fecha_base_original).toBe("2026-03-20T12:00:00.000Z");
    expect(item.fecha_base_origen).toBe("ajustada");
  });

  it("primera fecha_base fuera del ritual → origen 'manual', original null", async () => {
    sembrarItem();
    const res = await PATCH(req({ item_id: "it1", fecha_base: "2026-05-01" }), PARAMS);
    const { item } = await res.json();
    expect(item.fecha_base).toBe("2026-05-01T00:00:00.000Z");
    expect(item.fecha_base_origen).toBe("manual");
    expect(item.fecha_base_original).toBeNull();
  });
});
