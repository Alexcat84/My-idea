// AUD-09 M42 (tanda 7B, confianza): "última acción" en /ideas salía de
// projects.updated_at, que marcar tareas o mover fechas no actualiza: alguien
// que trabajó ayer en su checklist veía "última acción" de hace semanas. Ahora
// es lo más reciente entre la idea y sus tareas.
import { describe, expect, it } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { crearSupabaseFalso, estadoFalsoVacio } from "./testUtils/fakeSupabase";
import { fechaSello } from "./fechas";
import { listarIdeasConEstado } from "./ideas";

describe("la última acción cuenta el trabajo en las tareas (AUD-09 M42)", () => {
  it("una tarea movida el 10-sep manda sobre la idea tocada el 01-sep", async () => {
    const e = estadoFalsoVacio();
    e.projects["p1"] = { id: "p1", entrada_original: "vendo macetas", titulo: null, created_at: "2026-08-20T00:00:00Z", updated_at: "2026-09-01T12:00:00Z" };
    e.sessions["s0"] = { id: "s0", project_id: "p1", closed_at: "2026-08-20T00:00:01Z", estado_recorrido: null };
    e.plans.push({ id: "pl0", session_id: "s0", etiqueta: "organizador" });
    e.checklistItems.push({ project_id: "p1", plan_id: "plc", dominio: "core", estado: "empezado", created_at: "2026-08-25T00:00:00Z", updated_at: "2026-09-10T15:00:00Z" });
    const [c] = await listarIdeasConEstado(crearSupabaseFalso(e) as unknown as SupabaseClient);
    expect(c.pista).toContain(fechaSello("2026-09-10T15:00:00Z"));
    expect(c.pista).not.toContain(fechaSello("2026-09-01T12:00:00Z"));
  });
});
