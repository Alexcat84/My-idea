// i18n F6 (D2): el plan EN PANTALLA sigue el idioma del proyecto, como los
// documentos que se descargan. Para eso el detalle de la idea tiene que traer
// `projects.idioma` (null en una idea de antes de F5: la pantalla la lee como
// español con idiomaDelProyecto), y la vista tiene que pasárselo al papel.
//
// Lo esperado, contado a mano:
//   - proyecto con idioma "ko"      → detalle.idea.idioma === "ko"
//   - proyecto sin idioma (pre-F5)  → detalle.idea.idioma === null
//   - idiomaDeDocumentos({ idioma: "ko" }, "es") = "ko" (de los once)
//   - idiomaDeDocumentos({ idioma: null }, "fr") = "es" (pre-F5 es español)
//   - idiomaDeDocumentos({ idioma: "ru" }, "en") = "en" (fuera de los once: la interfaz)
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it, vi } from "vitest";
import { idiomaDeDocumentos } from "@/lib/i18n/idiomaDocumento";

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
const supabaseFalso = {
  auth: { getUser: vi.fn(async () => ({ data: { user: { id: "u1" } } })) },
  from: (nombre: string) => consulta(nombre),
};
vi.mock("@/lib/supabase/server", () => ({ createClient: vi.fn(async () => supabaseFalso) }));

import { GET } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1" }) };

function sembrar(proyecto: Fila) {
  tablas = {
    projects: [{ id: "p1", titulo: "Pan de barrio", entrada_original: "idea", created_at: "2026-03-08T12:00:00Z", ...proyecto }],
    sessions: [],
    plans: [],
  };
}

const pedir = () => GET(new Request("http://x/api/idea/p1", { headers: { cookie: "myidea_idioma=es" } }), PARAMS);

describe("el detalle de la idea trae el idioma del proyecto (D2)", () => {
  it("idea en coreano: idea.idioma = 'ko'", async () => {
    sembrar({ idioma: "ko" });
    const d = await (await pedir()).json();
    expect(d.idea.idioma).toBe("ko");
  });

  it("idea de antes de F5 (sin la columna): idea.idioma = null", async () => {
    sembrar({});
    const d = await (await pedir()).json();
    expect(d.idea.idioma).toBeNull();
  });
});

describe("la regla que aplica la pantalla", () => {
  it("de los once, pre-F5 y fuera de los once", () => {
    expect(idiomaDeDocumentos({ idioma: "ko" }, "es")).toBe("ko");
    expect(idiomaDeDocumentos({ idioma: null }, "fr")).toBe("es");
    expect(idiomaDeDocumentos({ idioma: "ru" }, "en")).toBe("en");
  });
});

describe("la vista le pasa al plan el idioma de los documentos", () => {
  const raiz = join(__dirname, "..", "..", "..", "..");
  const vista = readFileSync(join(raiz, "app", "idea", "[id]", "IdeaView.tsx"), "utf8");
  const manos = readFileSync(join(raiz, "app", "ui", "ManosALaObra.tsx"), "utf8");

  it("IdeaView calcula el idioma del documento con el idioma del proyecto y la interfaz", () => {
    expect(vista).toMatch(/idiomaDeDocumentos\(\{\s*idioma:\s*detalle\.idea\.idioma\s*\},\s*idioma\)/);
  });

  it("cada PlanDocumento en pantalla recibe idiomaDocumento", () => {
    for (const fuente of [vista, manos]) {
      const usos = fuente.match(/<PlanDocumento\b[\s\S]*?\/>/g) ?? [];
      expect(usos.length).toBeGreaterThan(0);
      for (const uso of usos) expect(uso).toMatch(/idiomaDocumento=\{/);
    }
  });
});
