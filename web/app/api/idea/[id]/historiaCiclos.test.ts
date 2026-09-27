// Ciclo de replanteamiento, Fase 2 (decisiones del fundador, 27 sep 2026): "lo
// hecho no se pierde". El detalle de la idea trae, de cada plan ANTERIOR al
// vigente (núcleo y cada mundo), sus tareas hechas y lo que la persona contó al
// pedir ESE plan (el evento ciclo_* con su plan_id). Las copias heredadas no se
// repiten: ya salen bajo su plan original.
//
// A mano: núcleo = [pA completo 01-sep, pB replanteamiento 10-sep, pC seguimiento
// 20-sep (vigente)]. Historia = [pA, pB]. pA: hechas = [t1]. pB: hechas = [t5]
// (t9 es la copia heredada de t1: fuera), relato "Se cayó el local.".
// Mundo quality = [m1 completo 05-sep, m2 seguimiento 15-sep (vigente)].
// Historia del mundo = [m1] con hechas = [q1].
import { describe, expect, it, vi } from "vitest";

type Fila = Record<string, unknown>;
let tablas: Record<string, Fila[]> = {};
function consulta(nombre: string) {
  const filtros: Array<(f: Fila) => boolean> = [];
  const q = {
    select: () => q,
    eq: (c: string, v: unknown) => (filtros.push((f) => f[c] === v), q),
    in: (c: string, vs: unknown[]) => (filtros.push((f) => vs.includes(f[c])), q),
    order: () => q,
    limit: () => q,
    then: (res: (v: unknown) => unknown, rej: (e: unknown) => unknown) =>
      Promise.resolve({ data: (tablas[nombre] ?? []).filter((f) => filtros.every((p) => p(f))), error: null }).then(res, rej),
  };
  return q;
}
vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => ({ auth: { getUser: vi.fn(async () => ({ data: { user: { id: "u1" } } })) }, from: (n: string) => consulta(n) })),
}));

import { GET } from "./route";

const item = (id: string, plan_id: string, texto: string, estado: string, completed_at: string | null, extra: Fila = {}) => ({
  id,
  project_id: "p1",
  plan_id,
  texto,
  estado,
  completed_at,
  etapa: 1,
  orden: 1,
  ...extra,
});

describe("la Historia trae lo hecho y lo contado de cada plan anterior", () => {
  it("núcleo y mundo, sin repetir las heredadas", async () => {
    tablas = {
      projects: [{ id: "p1", titulo: "Pan", entrada_original: "idea", created_at: "2026-08-30T12:00:00Z" }],
      sessions: [
        { id: "sA", project_id: "p1", created_at: "2026-09-01T00:00:00Z", closed_at: "2026-09-01T01:00:00Z", estado_recorrido: null },
        { id: "sB", project_id: "p1", created_at: "2026-09-10T00:00:00Z", closed_at: "2026-09-10T01:00:00Z", estado_recorrido: null },
        { id: "sC", project_id: "p1", created_at: "2026-09-20T00:00:00Z", closed_at: "2026-09-20T01:00:00Z", estado_recorrido: null },
        { id: "sM1", project_id: "p1", created_at: "2026-09-05T00:00:00Z", closed_at: "2026-09-05T01:00:00Z", dominio: "quality", estado_recorrido: null },
        { id: "sM2", project_id: "p1", created_at: "2026-09-15T00:00:00Z", closed_at: "2026-09-15T01:00:00Z", dominio: "quality", estado_recorrido: null },
      ],
      plans: [
        { id: "pA", session_id: "sA", etiqueta: "completo", contenido_md: "# A", created_at: "2026-09-01T00:00:00Z", dominio: "core" },
        { id: "m1", session_id: "sM1", etiqueta: "completo", contenido_md: "# M1", created_at: "2026-09-05T00:00:00Z", dominio: "quality" },
        { id: "pB", session_id: "sB", etiqueta: "replanteamiento", contenido_md: "# B", created_at: "2026-09-10T00:00:00Z", dominio: "core" },
        { id: "m2", session_id: "sM2", etiqueta: "seguimiento", contenido_md: "# M2", created_at: "2026-09-15T00:00:00Z", dominio: "quality" },
        { id: "pC", session_id: "sC", etiqueta: "seguimiento", contenido_md: "# C", created_at: "2026-09-20T00:00:00Z", dominio: "core" },
      ],
      checklist_items: [
        item("t1", "pA", "Hablar con 5", "hecho", "2026-09-05T15:00:00Z"),
        item("t2", "pA", "Rentar local", "pendiente", null),
        item("t9", "pB", "Hablar con 5", "hecho", "2026-09-05T15:00:00Z", { heredado_de: "t1" }),
        item("t5", "pB", "Vender por encargo", "hecho", "2026-09-12T15:00:00Z"),
        item("q1", "m1", "Definir estándar", "hecho", "2026-09-06T15:00:00Z", { dominio: "quality" }),
      ],
      project_unlocks: [{ project_id: "p1", dominio: "quality" }],
      project_bitacora: [
        { project_id: "p1", tipo: "ciclo_replanteado", payload: { plan_id: "pB", relato: "Se cayó el local." }, created_at: "2026-09-10T00:00:01Z" },
      ],
    };
    const d = await (await GET(new Request("http://x/api/idea/p1"), { params: Promise.resolve({ id: "p1" }) })).json();
    expect(d.historial.map((h: { etiqueta: string }) => h.etiqueta)).toEqual(["completo", "replanteamiento"]);
    expect(d.historial[0]).toMatchObject({ hechas: [{ texto: "Hablar con 5", completed_at: "2026-09-05T15:00:00Z" }], relato: null });
    expect(d.historial[1]).toMatchObject({
      hechas: [{ texto: "Vender por encargo", completed_at: "2026-09-12T15:00:00Z" }],
      relato: "Se cayó el local.",
    });
    const mundo = d.mundos.find((m: { dominio: string }) => m.dominio === "quality");
    expect(mundo.historial).toEqual([
      { etiqueta: "completo", created_at: "2026-09-05T00:00:00Z", contenido_md: "# M1", hechas: [{ texto: "Definir estándar", completed_at: "2026-09-06T15:00:00Z" }], relato: null },
    ]);
  });
});
