// Fase 3.8 §4 — POST /api/project/[id]/baseline: sella la línea base del
// ciclo y escribe fecha_base + origen por ítem, preservando la primera
// fecha al re-confirmar.
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
  return new Request("http://x/api/project/p1/baseline", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sembrar() {
  estadoFalso.projects["p1"] = { id: "p1", user_id: "user-fake", entrada_original: "idea", session_count: 1 };
  estadoFalso.plans.push({ id: "plan-1", baseline_confirmada_at: null });
  estadoFalso.checklistItems.push(
    { id: "it1", project_id: "p1", plan_id: "plan-1", etapa: 1, fecha_base: null, fecha_base_original: null },
    { id: "it2", project_id: "p1", plan_id: "plan-1", etapa: 2, fecha_base: null, fecha_base_original: null }
  );
}

describe("POST /api/project/[id]/baseline (Fase 3.8)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("400 si falta plan_id o fechas", async () => {
    sembrar();
    expect((await POST(req({ fechas: [] }), PARAMS)).status).toBe(400);
    expect((await POST(req({ plan_id: "plan-1", fechas: "x" }), PARAMS)).status).toBe(400);
  });

  it("401 si no hay usuario", async () => {
    sembrar();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await POST(req({ plan_id: "plan-1", fechas: [] }), PARAMS);
    expect(res.status).toBe(401);
  });

  it("confirma: escribe fecha_base+origen y sella baseline_confirmada_at", async () => {
    sembrar();
    const res = await POST(
      req({
        plan_id: "plan-1",
        fechas: [
          { item_id: "it1", fecha: "2026-03-09T12:00:00.000Z", origen: "sugerida" },
          { item_id: "it2", fecha: "2026-03-20T12:00:00.000Z", origen: "ajustada" },
        ],
      }),
      PARAMS
    );
    expect(res.status).toBe(200);
    const it1 = estadoFalso.checklistItems.find((i) => i.id === "it1")!;
    expect(it1.fecha_base).toBe("2026-03-09T12:00:00.000Z");
    expect(it1.fecha_base_origen).toBe("sugerida");
    const it2 = estadoFalso.checklistItems.find((i) => i.id === "it2")!;
    expect(it2.fecha_base_origen).toBe("ajustada");
    const plan = estadoFalso.plans.find((p) => (p as { id: string }).id === "plan-1")! as Record<string, unknown>;
    expect(plan.baseline_confirmada_at).toBeTruthy();
  });

  it("re-confirmar preserva la PRIMERA fecha_base en fecha_base_original", async () => {
    sembrar();
    // primera confirmación
    await POST(
      req({ plan_id: "plan-1", fechas: [{ item_id: "it1", fecha: "2026-03-09T12:00:00.000Z", origen: "sugerida" }] }),
      PARAMS
    );
    // segunda confirmación (recalculo): mueve it1 a otra fecha
    await POST(
      req({ plan_id: "plan-1", fechas: [{ item_id: "it1", fecha: "2026-03-16T12:00:00.000Z", origen: "sugerida" }] }),
      PARAMS
    );
    const it1 = estadoFalso.checklistItems.find((i) => i.id === "it1")!;
    expect(it1.fecha_base).toBe("2026-03-16T12:00:00.000Z");
    expect(it1.fecha_base_original).toBe("2026-03-09T12:00:00.000Z");
  });
});
