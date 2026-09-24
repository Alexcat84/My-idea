// AUD-09 B12 (tanda 7A, seguridad): abrir un mundo (unlock) no revisaba si la
// cuenta era real ni si la idea tenía plan del núcleo, cuando world/start (el
// preview) exige las dos cosas: un invitado o una idea sin plan dejaban filas de
// mundos abiertos que el resto de la casa no puede usar. Mismas puertas que el
// arranque del mundo.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);
vi.mock("@/lib/supabase/server", () => ({ createClient: vi.fn(async () => supabaseFalso) }));
let invitado = false;
vi.mock("@/lib/identidad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/identidad")>()),
  esInvitadoInvisible: () => invitado,
}));
let planCore: string | null = "plan-core-1";
vi.mock("@/lib/db", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/db")>()),
  obtenerPlanCoreVigente: async () => planCore,
}));

import { POST } from "./route";

const pedir = () =>
  POST(new Request("http://x/api/project/p1/world/quality/unlock", { method: "POST" }), {
    params: Promise.resolve({ id: "p1", pack: "quality" }),
  });

describe("abrir un mundo pide cuenta real y plan del núcleo (AUD-09 B12)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    estadoFalso.projects["p1"] = { id: "p1", session_count: 1 };
    invitado = false;
    planCore = "plan-core-1";
  });

  it("un invitado: 401 y no se abre nada", async () => {
    invitado = true;
    const res = await pedir();
    expect(res.status).toBe(401);
    expect(estadoFalso.projectUnlocks).toHaveLength(0);
  });

  it("sin plan del núcleo: 409 con la muralla de siempre y no se abre nada", async () => {
    planCore = null;
    const res = await pedir();
    expect(res.status).toBe(409);
    expect((await res.json()).error).toMatch(/^Primero genera el plan de tu idea/);
    expect(estadoFalso.projectUnlocks).toHaveLength(0);
  });

  it("con cuenta y plan, abre el mundo", async () => {
    const res = await pedir();
    expect(res.status).toBe(200);
    expect(estadoFalso.projectUnlocks).toHaveLength(1);
  });
});
