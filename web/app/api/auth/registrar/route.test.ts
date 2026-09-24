// AUD-09 H07: al registrarse, la identidad invisible del navegador (la prueba
// de posesión es la cookie de ESTE request) queda anotada en la cuenta nueva,
// para adoptar sus ideas al confirmar desde cualquier navegador.
import { beforeEach, describe, expect, it, vi } from "vitest";

const registrarAdopcionPendiente = vi.fn(async () => undefined);
vi.mock("@/lib/cuentas", () => ({
  estaEnAllowlist: async () => true,
  registrarAdopcionPendiente: (...a: unknown[]) => registrarAdopcionPendiente(...(a as [])),
}));
vi.mock("@/lib/identidad", () => ({ esInvitadoInvisible: (u: { is_anonymous?: boolean }) => u.is_anonymous === true }));
vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({
    auth: {
      getUser: async () => ({ data: { user: { id: "anon-1", is_anonymous: true } } }),
      signUp: async () => ({ data: { user: { id: "real-1", identities: [{ id: "i" }] } }, error: null }),
    },
  }),
}));

import { POST } from "./route";

describe("POST /api/auth/registrar", () => {
  beforeEach(() => registrarAdopcionPendiente.mockClear());

  it("una cuenta nueva anota la identidad invisible del navegador como adopción pendiente", async () => {
    const res = await POST(
      new Request("http://test/api/auth/registrar", {
        method: "POST",
        body: JSON.stringify({ email: "ana@example.com", password: "Una-clave-larga-1" }),
      })
    );
    expect(res.status).toBe(200);
    expect(registrarAdopcionPendiente).toHaveBeenCalledWith("real-1", "anon-1");
  });
});
