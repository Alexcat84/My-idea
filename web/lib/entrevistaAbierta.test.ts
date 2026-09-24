// AUD-09 M29 (tanda 7B, confianza): había dos definiciones de "entrevista
// abierta". /ideas contaba toda sesión sin cerrar con estado; la idea excluía
// el diagnóstico de mundo esperando compra (fase 'cerrada'). Resultado: "Una
// pregunta te espera" para siempre tras un diagnóstico no comprado, o en
// 'listo para plan', donde lo que espera es el plan. Una sola regla.
import { describe, expect, it } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { crearSupabaseFalso, estadoFalsoVacio } from "./testUtils/fakeSupabase";
import { estadoEntrevista } from "./entrevistaAbierta";
import { listarIdeasConEstado } from "./ideas";

const ses = (fase: string, closed_at: string | null = null) => ({ closed_at, estado_recorrido: { recorrido: { fase } } });

describe("estadoEntrevista: una sola regla (AUD-09 M29)", () => {
  it("pregunta pendiente, plan listo, o nada", () => {
    expect(estadoEntrevista(ses("esperando_respuesta"))).toBe("pregunta");
    expect(estadoEntrevista(ses("listo_para_plan"))).toBe("listo_para_plan");
    expect(estadoEntrevista(ses("cerrada"))).toBeNull(); // diagnóstico esperando compra
    expect(estadoEntrevista(ses("esperando_respuesta", "2026-09-01T00:00:00Z"))).toBeNull();
    expect(estadoEntrevista({ closed_at: null, estado_recorrido: null })).toBeNull();
  });
});

describe("/ideas usa la misma regla (AUD-09 M29)", () => {
  async function cintaCon(fase: string) {
    const e = estadoFalsoVacio();
    e.projects["p1"] = { id: "p1", entrada_original: "vendo macetas", titulo: null, created_at: "2026-09-01T00:00:00Z", updated_at: "2026-09-01T00:00:00Z" };
    e.sessions["s0"] = { id: "s0", project_id: "p1", closed_at: "2026-09-01T00:00:01Z", estado_recorrido: null };
    e.plans.push({ id: "pl0", session_id: "s0", etiqueta: "organizador" });
    e.sessions["s1"] = { id: "s1", project_id: "p1", ...ses(fase) };
    return (await listarIdeasConEstado(crearSupabaseFalso(e) as unknown as SupabaseClient))[0];
  }

  it("un diagnóstico de mundo esperando compra no es una pregunta esperando", async () => {
    const c = await cintaCon("cerrada");
    expect(c.pista).not.toMatch(/Una pregunta te espera/);
    expect(c.chips.map((x) => x.texto)).not.toContain("En exploración");
  });

  it("con el plan listo para armarse, lo que espera es el plan", async () => {
    const c = await cintaCon("listo_para_plan");
    expect(c.pista).toMatch(/^Tu plan está listo para armarse/);
  });

  it("con una pregunta pendiente, la pista de siempre", async () => {
    const c = await cintaCon("esperando_respuesta");
    expect(c.pista).toMatch(/^Una pregunta te espera/);
  });
});
