// AUD-09 M28 (tanda 7B, confianza): el organizador crea la idea ANTES de llamar
// a la IA; si la IA falla, la idea queda sin su Claridad. /ideas la presentaba
// "Con claridad" (mentira) y la página abría vacía, sin salida. Ahora se dice lo
// que es ("Sin ordenar") y la idea ofrece ordenarla, reusando la misma idea.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { crearSupabaseFalso, estadoFalsoVacio } from "./testUtils/fakeSupabase";
import { listarIdeasConEstado } from "./ideas";

const leer = (rel: string) => readFileSync(path.join(__dirname, "..", rel), "utf8");

describe("una idea sin Claridad no se presenta con Claridad (AUD-09 M28)", () => {
  it("/ideas: 'Sin ordenar' sin organizador; 'Con claridad' con él", async () => {
    const e = estadoFalsoVacio();
    e.projects["p1"] = { id: "p1", entrada_original: "vendo macetas", titulo: null, created_at: "2026-09-01T00:00:00Z", updated_at: "2026-09-01T00:00:00Z" };
    e.projects["p2"] = { id: "p2", entrada_original: "vendo tamales", titulo: null, created_at: "2026-09-02T00:00:00Z", updated_at: "2026-09-02T00:00:00Z" };
    e.sessions["s1"] = { id: "s1", project_id: "p1", closed_at: "2026-09-01T00:00:01Z", estado_recorrido: null };
    e.sessions["s2"] = { id: "s2", project_id: "p2", closed_at: "2026-09-02T00:00:01Z", estado_recorrido: null };
    e.plans.push({ id: "pl2", session_id: "s2", etiqueta: "organizador" });
    const cintas = await listarIdeasConEstado(crearSupabaseFalso(e) as unknown as SupabaseClient);
    const chip = (id: string) => cintas.find((c) => c.id === id)?.chips.map((x) => x.texto);
    expect(chip("p1")).toEqual(["Sin ordenar"]);
    expect(chip("p2")).toEqual(["Con claridad"]);
  });

  it("la idea sin Claridad ofrece ordenarla, con su propio texto", () => {
    const idea = leer("app/idea/[id]/IdeaView.tsx");
    expect(idea).toMatch(/\/nueva\?idea=\$\{projectId\}/);
  });

  it("/nueva y el organizador reusan la idea en vez de crear otra", () => {
    expect(leer("app/nueva/page.tsx")).toMatch(/project_id: ideaAReordenar/);
    const org = leer("app/api/organizer/stream/route.ts");
    expect(org).toMatch(/project_id/);
    // i18n F2: la frase vive en el catálogo; la ruta la usa por su clave.
    expect(org).toMatch(/error: t\.yaOrdenada/);
    expect(leer("lib/i18n/mensajes/servidorSesion.ts")).toMatch(/yaOrdenada: "Esta idea ya está ordenada\."/);
  });
});
