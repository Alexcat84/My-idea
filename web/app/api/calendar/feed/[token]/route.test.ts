// El feed .ics de cada usuario es un dato PERSONAL y siempre fresco (decision del fundador, corrida final, 8 oct 2026).
// Antes salia con "Cache-Control: public, max-age=3600" y el borde de Vercel guardaba una copia por hora: en produccion
// el feed respondio x-vercel-cache: HIT con age 1285 (una copia de 21 minutos), sin las tareas nuevas del usuario.
// Ahora es privado y sin copias: ni Vercel ni nadie en el camino lo guarda, y nunca muestra fechas viejas.
import { describe, expect, it, vi } from "vitest";

vi.mock("@/lib/supabase/admin", () => ({
  createAdminClient: () => ({
    from: () => ({ select: () => ({ eq: async () => ({ data: [] }) }) }),
  }),
}));
vi.mock("@/lib/feedCalendario", async (original) => ({
  ...(await original<typeof import("@/lib/feedCalendario")>()),
  usuarioDeToken: (token: string) => (token === "valido" ? "u1" : null),
}));

import { GET } from "./route";

const llamar = (token: string) =>
  GET(new Request(`https://www.myideaproject.com/api/calendar/feed/${token}.ics`), { params: Promise.resolve({ token: `${token}.ics` }) });

describe("el feed de calendario no se guarda en ninguna cache compartida", () => {
  it("sale privado y sin copias (nada de public ni max-age para el borde)", async () => {
    const res = await llamar("valido");
    expect(res.status).toBe(200);
    const cc = res.headers.get("Cache-Control") ?? "";
    expect(cc).toContain("private");
    expect(cc).toContain("no-store");
    expect(cc).not.toContain("public");
    expect(cc).not.toMatch(/s-maxage|max-age=[1-9]/);
  });

  it("sigue siendo un .ics valido", async () => {
    const res = await llamar("valido");
    expect(res.headers.get("Content-Type")).toContain("text/calendar");
    expect(await res.text()).toContain("BEGIN:VCALENDAR");
  });

  it("un token invalido sigue dando 404", async () => {
    expect((await llamar("otro")).status).toBe(404);
  });
});
