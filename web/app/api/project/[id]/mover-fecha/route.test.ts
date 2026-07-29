// Fase 4.7 — POST /api/project/[id]/mover-fecha: mover la fecha de una
// pendiente con cascada opcional. Fechas a mano: mover it2 +7 días.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

import { POST } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1" }) };
const D = (s: string) => `${s}T12:00:00.000Z`;

function req(body: unknown) {
  return new Request("http://x/api/project/p1/mover-fecha", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sembrar() {
  estadoFalso.projects["p1"] = { id: "p1", user_id: "user-fake", entrada_original: "idea", session_count: 1 };
  estadoFalso.checklistItems.push(
    // hecha: nunca se mueve en cascada
    { id: "it1", project_id: "p1", plan_id: "pl", dominio: "core", etapa: 1, estado: "hecho", fecha_base: D("2026-03-10"), fecha_base_origen: "sugerida", fecha_base_original: null },
    // anterior por etapa/fecha: no es "posterior", no se mueve
    { id: "it6", project_id: "p1", plan_id: "pl", dominio: "core", etapa: 1, estado: "pendiente", fecha_base: D("2026-03-05"), fecha_base_origen: "sugerida", fecha_base_original: null },
    // OBJETIVO
    { id: "it2", project_id: "p1", plan_id: "pl", dominio: "core", etapa: 2, estado: "pendiente", fecha_base: D("2026-03-20"), fecha_base_origen: "sugerida", fecha_base_original: null },
    // posterior misma etapa
    { id: "it3", project_id: "p1", plan_id: "pl", dominio: "core", etapa: 2, estado: "en_proceso", fecha_base: D("2026-03-25"), fecha_base_origen: "sugerida", fecha_base_original: null },
    // posterior etapa mayor
    { id: "it4", project_id: "p1", plan_id: "pl", dominio: "core", etapa: 3, estado: "pendiente", fecha_base: D("2026-04-01"), fecha_base_origen: "sugerida", fecha_base_original: null },
    // retirada: nunca se mueve
    { id: "it5", project_id: "p1", plan_id: "pl", dominio: "core", etapa: 3, estado: "no_aplica", fecha_base: D("2026-04-05"), fecha_base_origen: "sugerida", fecha_base_original: null }
  );
}

const fb = (id: string) => estadoFalso.checklistItems.find((i) => i.id === id)!.fecha_base;

describe("POST /api/project/[id]/mover-fecha (Fase 4.7)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    sembrar();
  });

  it("400 sin item_id o fecha; 401 sin usuario", async () => {
    expect((await POST(req({ fecha: D("2026-03-27") }), PARAMS)).status).toBe(400);
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    expect((await POST(req({ item_id: "it2", fecha: D("2026-03-27") }), PARAMS)).status).toBe(401);
  });

  it("SIN cascada: solo el objetivo se mueve; las demás intactas", async () => {
    const res = await POST(req({ item_id: "it2", fecha: D("2026-03-27"), cascada: false }), PARAMS);
    expect(res.status).toBe(200);
    expect(fb("it2")).toBe(D("2026-03-27")); // objetivo movido
    expect(fb("it3")).toBe(D("2026-03-25")); // posterior intacta
    expect(fb("it4")).toBe(D("2026-04-01"));
    expect(fb("it1")).toBe(D("2026-03-10")); // hecha intacta
    expect(fb("it5")).toBe(D("2026-04-05")); // retirada intacta
    expect(estadoFalso.bitacora.at(-1)).toMatchObject({ tipo: "fecha_movida", payload: { cascada: "solo" } });
  });

  it("CON cascada: las posteriores corren el mismo delta (+7 días); hechas, retiradas y anteriores intactas", async () => {
    const res = await POST(req({ item_id: "it2", fecha: D("2026-03-27"), cascada: true }), PARAMS);
    expect(res.status).toBe(200);
    // delta = +7 días: it2 03-20→03-27; it3 03-25→04-01; it4 04-01→04-08.
    expect(fb("it2")).toBe(D("2026-03-27"));
    expect(fb("it3")).toBe(D("2026-04-01"));
    expect(fb("it4")).toBe(D("2026-04-08"));
    // NO se tocan: hecha, retirada, ni la anterior (etapa/fecha previa).
    expect(fb("it1")).toBe(D("2026-03-10"));
    expect(fb("it5")).toBe(D("2026-04-05"));
    expect(fb("it6")).toBe(D("2026-03-05"));
    // UNA entrada de bitácora, con el número de la cascada (it3 + it4 = 2).
    expect(estadoFalso.bitacora.at(-1)).toMatchObject({ tipo: "fecha_movida", payload: { cascada: 2, delta_dias: 7 } });
  });

  it("congela la fecha ORIGINAL en la primera movida y pasa el origen a 'ajustada'", async () => {
    await POST(req({ item_id: "it2", fecha: D("2026-03-27"), cascada: true }), PARAMS);
    const it2 = estadoFalso.checklistItems.find((i) => i.id === "it2")!;
    const it3 = estadoFalso.checklistItems.find((i) => i.id === "it3")!;
    expect(it2.fecha_base_original).toBe(D("2026-03-20"));
    expect(it2.fecha_base_origen).toBe("ajustada");
    expect(it3.fecha_base_original).toBe(D("2026-03-25")); // también congela la suya
  });
});
