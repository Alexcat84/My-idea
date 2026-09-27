// i18n F6 (D2): la bitácora de un espacio. La línea de la pantalla sigue la
// interfaz; el documento (.md, papel del PDF, nombre del archivo), el idioma
// del proyecto. Lo esperado sale de los catálogos: el título del documento en
// coreano es SERVIDOR_PROYECTO.ko.bitacora.tituloEspacio ("# {{espacio}} 기록장")
// con el mundo "quality" en coreano ("품질과 신뢰", glosario §6); en español
// ("Calidad y Confianza") para la pantalla.
import { describe, expect, it, vi } from "vitest";

type Fila = Record<string, unknown>;
const tablas: Record<string, Fila[]> = {
  projects: [{ id: "p1", titulo: "Pan de barrio", entrada_original: "idea", created_at: "2026-03-08T12:00:00Z", idioma: "ko" }],
};
function consulta(nombre: string) {
  const filtros: Array<(f: Fila) => boolean> = [];
  const q = {
    select: () => q,
    eq: (c: string, v: unknown) => (filtros.push((f) => f[c] === v), q),
    limit: () => q,
    then: (res: (v: unknown) => unknown, rej: (e: unknown) => unknown) =>
      Promise.resolve({ data: (tablas[nombre] ?? []).filter((f) => filtros.every((p) => p(f))), error: null }).then(res, rej),
  };
  return q;
}
vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => ({
    auth: { getUser: vi.fn(async () => ({ data: { user: { id: "u1" } } })) },
    from: (nombre: string) => consulta(nombre),
  })),
}));

const cargar = vi.fn(async (_s: unknown, _p: unknown, _pr: unknown, _n: unknown, idioma: unknown) => [
  { fecha: "2026-03-08T12:00:00Z", texto: `entrada-${String(idioma)}`, peso: "accion", dominio: "quality" },
]);
vi.mock("@/lib/bitacoraDatos", () => ({
  cargarEntradasBitacora: (...a: unknown[]) => cargar(...(a as [unknown, unknown, unknown, unknown, unknown])),
}));

import { GET } from "./route";

describe("bitácora de un espacio: pantalla en la interfaz, documento en el proyecto", () => {
  it("idea en coreano, interfaz en español", async () => {
    const res = await GET(
      new Request("http://x/api/project/p1/bitacora?dominio=quality", { headers: { cookie: "myidea_idioma=es" } }),
      { params: Promise.resolve({ id: "p1" }) }
    );
    const d = await res.json();
    expect(d.nombre).toBe("Calidad y Confianza");
    expect(d.entradas[0].texto).toBe("entrada-es");
    expect(d.idioma).toBe("ko");
    expect(d.papel.entradas[0].texto).toBe("entrada-ko");
    expect(d.papel.nombre).toBe("품질과 신뢰");
    expect(d.markdown.split("\n")[0]).toBe("# 품질과 신뢰 기록장");
  });
});
