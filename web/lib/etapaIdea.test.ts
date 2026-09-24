// AUD-09 B10 (tanda 7B, confianza): /ideas y el encabezado de la idea calculaban
// la etapa con reglas distintas; en un seguimiento abierto, el encabezado volvía
// a "La Exploración" (3) mientras /ideas decía otra cosa. Una sola regla.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { crearSupabaseFalso, estadoFalsoVacio } from "./testUtils/fakeSupabase";
import { etapaDeIdea } from "./etapaIdea";
import { listarIdeasConEstado } from "./ideas";

describe("etapaDeIdea: una sola regla (AUD-09 B10)", () => {
  const base = { conPlan: false, enObra: false, explorandoNucleo: false, seguimientoAbierto: false, ordenada: true };
  it("la exploración del núcleo antes del plan es la 3", () => {
    expect(etapaDeIdea({ ...base, explorandoNucleo: true })).toBe(3);
  });
  it("un seguimiento abierto es Manos a la Obra (5), no vuelve a la Exploración", () => {
    expect(etapaDeIdea({ ...base, conPlan: true, seguimientoAbierto: true })).toBe(5);
  });
  it("con plan sin empezar, la 4; con obra, la 5; sin nada, Claridad o Chispa", () => {
    expect(etapaDeIdea({ ...base, conPlan: true })).toBe(4);
    expect(etapaDeIdea({ ...base, conPlan: true, enObra: true })).toBe(5);
    expect(etapaDeIdea(base)).toBe(2);
    expect(etapaDeIdea({ ...base, ordenada: false })).toBe(1);
  });
});

describe("/ideas y el encabezado usan la regla (AUD-09 B10)", () => {
  it("/ideas: con plan y un seguimiento abierto, etapa 5", async () => {
    const e = estadoFalsoVacio();
    e.projects["p1"] = { id: "p1", entrada_original: "vendo macetas", titulo: null, created_at: "2026-09-01T00:00:00Z", updated_at: "2026-09-01T00:00:00Z" };
    e.sessions["s0"] = { id: "s0", project_id: "p1", closed_at: "2026-09-01T00:00:01Z", estado_recorrido: null };
    e.plans.push({ id: "pl0", session_id: "s0", etiqueta: "organizador" }, { id: "pl1", session_id: "s0", etiqueta: "completo" });
    e.sessions["s1"] = { id: "s1", project_id: "p1", closed_at: null, dominio: "core", estado_recorrido: { recorrido: { fase: "esperando_respuesta", esSeguimiento: true } } };
    const [c] = await listarIdeasConEstado(crearSupabaseFalso(e) as unknown as SupabaseClient);
    expect(c.etapa).toBe(5);
  });
  it("el encabezado de la idea la usa", () => {
    const idea = readFileSync(path.join(__dirname, "..", "app", "idea", "[id]", "IdeaView.tsx"), "utf8");
    expect(idea).toMatch(/etapaDeIdea\(/);
  });
});
