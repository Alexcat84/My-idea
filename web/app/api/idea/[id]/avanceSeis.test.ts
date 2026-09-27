// "Tu avance" en la idea, las seis etapas (decisión del fundador, 26 sep 2026):
// el detalle trae cuándo empezó La Exploración del núcleo (la primera sesión que
// no es de un mundo) y la vista le pasa a Manos a la Obra la etapa actual de la
// regla única, la misma del paso a paso.
//
// A mano: sesiones p1 = [mundo "calidad" 01-mar, núcleo 03-mar, núcleo 09-mar]
// → exploracion_at = la del 03-mar (la primera del núcleo; la del mundo no cuenta).
import { readFileSync } from "node:fs";
import { join } from "node:path";
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

const pedir = () => GET(new Request("http://x/api/idea/p1"), { params: Promise.resolve({ id: "p1" }) });

describe("el detalle trae el inicio de La Exploración del núcleo", () => {
  it("la primera sesión que no es de un mundo", async () => {
    tablas = {
      projects: [{ id: "p1", titulo: "Pan", entrada_original: "idea", created_at: "2026-02-28T12:00:00Z" }],
      sessions: [
        { id: "s0", project_id: "p1", created_at: "2026-03-01T10:00:00Z", dominio: "calidad", estado_recorrido: null },
        { id: "s1", project_id: "p1", created_at: "2026-03-03T10:00:00Z", dominio: null, estado_recorrido: null },
        { id: "s2", project_id: "p1", created_at: "2026-03-09T10:00:00Z", dominio: null, estado_recorrido: null },
      ],
      plans: [],
    };
    const d = await (await pedir()).json();
    expect(d.idea.exploracion_at).toBe("2026-03-03T10:00:00Z");
  });

  it("sin sesiones del núcleo: null (no se inventa)", async () => {
    tablas = { projects: [{ id: "p1", titulo: "Pan", entrada_original: "idea", created_at: "2026-02-28T12:00:00Z" }], sessions: [], plans: [] };
    const d = await (await pedir()).json();
    expect(d.idea.exploracion_at).toBeNull();
  });
});

describe("la vista le pasa a Manos a la Obra la etapa y las fechas", () => {
  const raiz = join(__dirname, "..", "..", "..", "..");
  it("IdeaView pasa etapaIdea={etapaBase} y exploracionAt; Manos arma las seis etapas con ellos", () => {
    const vista = readFileSync(join(raiz, "app", "idea", "[id]", "IdeaView.tsx"), "utf8");
    const manos = readFileSync(join(raiz, "app", "ui", "ManosALaObra.tsx"), "utf8");
    expect(vista).toMatch(/etapaIdea=\{etapaBase\}/);
    expect(vista).toMatch(/exploracionAt=\{detalle\.idea\.exploracion_at \?\? null\}/);
    expect(manos).toMatch(/etapa: etapaIdea \?\?/);
    expect(manos).toMatch(/manosAt:/);
  });
});
