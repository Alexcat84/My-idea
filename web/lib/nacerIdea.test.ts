// i18n F5: toda idea nueva nace con el idioma de su texto, y ese idioma suma
// uno al conteo anónimo (046). Las tres puertas de entrada (session/start,
// organizer y organizer/stream) crean la idea por aquí.
import { describe, expect, it, vi } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { crearSupabaseFalso, estadoFalsoVacio } from "./testUtils/fakeSupabase";

const contados: Array<[string, string]> = [];
vi.mock("@/lib/i18n/conteoIdiomas", () => ({
  contarIdiomaDeIdea: async (idea: string, interfaz: string) => {
    contados.push([idea, interfaz]);
  },
}));

import { nacerIdea } from "./nacerIdea";

describe("nacerIdea", () => {
  it("una idea en coreano con la interfaz en español nace en coreano y se cuenta así", async () => {
    const estado = estadoFalsoVacio();
    const client = crearSupabaseFalso(estado) as unknown as SupabaseClient;
    const { projectId, idioma } = await nacerIdea(client, "u1", "우리 동네에서 빵을 팔고 싶어요", "es");
    expect(idioma).toBe("ko");
    expect(estado.projects[projectId]).toMatchObject({ idioma: "ko" });
    expect(contados).toEqual([["ko", "es"]]);
  });

  it("una idea en ruso (fuera de los once) guarda ruso; la interfaz queda aparte", async () => {
    contados.length = 0;
    const estado = estadoFalsoVacio();
    const client = crearSupabaseFalso(estado) as unknown as SupabaseClient;
    const { projectId } = await nacerIdea(client, "u1", "Я хочу продавать хлеб в своём районе", "en");
    expect(estado.projects[projectId]).toMatchObject({ idioma: "ru" });
    expect(contados).toEqual([["ru", "en"]]);
  });
});
