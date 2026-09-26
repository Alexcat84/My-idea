// i18n F6 (D4): al entrar, el idioma de la interfaz se guarda en
// user_metadata.idioma (lo lee el Send Email Hook para el correo de recuperar
// la contraseña y los demás). Solo se escribe si cambió.
import { beforeEach, describe, expect, it, vi } from "vitest";

const updateUser = vi.fn<(args: unknown) => Promise<{ data: object; error: { message: string } | null }>>(async () => ({ data: {}, error: null }));
let metadata: Record<string, unknown> = {};
vi.mock("@/lib/cuentas", () => ({
  estaEnAllowlist: async () => true,
  bienvenidaTrasLogin: async () => ({ pendientes: 0 }),
}));
vi.mock("@/lib/identidad", () => ({ esInvitadoInvisible: () => false }));
vi.mock("@/lib/seguridad", () => ({ estadoSeguridad: async () => ({ habilitado: false }) }));
vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({
    auth: {
      getUser: async () => ({ data: { user: { id: "real-1", user_metadata: metadata } } }),
      signInWithPassword: async () => ({ error: null }),
      updateUser: (args: unknown) => updateUser(args),
    },
  }),
}));

import { POST } from "./route";

function entrar(cookie?: string) {
  return POST(
    new Request("http://test/api/auth/entrar", {
      method: "POST",
      headers: cookie ? { cookie } : {},
      body: JSON.stringify({ email: "ana@example.com", password: "Una-clave-larga-1" }),
    })
  );
}

describe("POST /api/auth/entrar guarda el idioma de la interfaz", () => {
  beforeEach(() => {
    updateUser.mockClear();
    metadata = {};
  });

  it("si la cuenta no tenía idioma, guarda el de la cookie", async () => {
    const res = await entrar("myidea_idioma=fr");
    expect(res.status).toBe(200);
    expect(updateUser).toHaveBeenCalledWith({ data: { idioma: "fr" } });
  });

  it("si ya tenía el mismo, no escribe nada", async () => {
    metadata = { idioma: "fr" };
    await entrar("myidea_idioma=fr");
    expect(updateUser).not.toHaveBeenCalled();
  });

  it("si cambió, guarda el nuevo", async () => {
    metadata = { idioma: "es" };
    await entrar("myidea_idioma=ja");
    expect(updateUser).toHaveBeenCalledWith({ data: { idioma: "ja" } });
  });

  it("si guardarlo falla, la entrada sigue (y queda en el log)", async () => {
    const spy = vi.spyOn(console, "error").mockImplementation(() => undefined);
    updateUser.mockResolvedValueOnce({ data: {}, error: { message: "caído" } });
    const res = await entrar("myidea_idioma=de");
    expect(res.status).toBe(200);
    expect((await res.json()).ok).toBe(true);
    expect(spy).toHaveBeenCalled();
    spy.mockRestore();
  });
});
