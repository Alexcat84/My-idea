// AUD-09 H15: /auth/callback sirve a tres enlaces (Google, confirmación de
// registro y recuperación de contraseña). El ramal de recuperación retornaba
// ANTES de la allowlist, y `type=recovery` es un parámetro de la query que
// controla el cliente: cualquier code válido abría sesión aunque el correo no
// estuviera invitado. La allowlist vale para los tres caminos.
import { beforeEach, describe, expect, it, vi } from "vitest";

let invitado = true;
const estaEnAllowlist = vi.fn(async () => invitado);
const bienvenidaTrasLogin = vi.fn(async () => undefined);
vi.mock("@/lib/cuentas", () => ({
  estaEnAllowlist: (...a: unknown[]) => estaEnAllowlist(...(a as [])),
  bienvenidaTrasLogin: (...a: unknown[]) => bienvenidaTrasLogin(...(a as [])),
  adoptarProyectosDeUsuario: vi.fn(async () => undefined),
}));
vi.mock("@/lib/identidad", () => ({ esInvitadoInvisible: () => false }));
vi.mock("@/lib/seguridad", () => ({ estadoSeguridad: async () => ({ habilitado: false }) }));
vi.mock("next/headers", () => ({
  cookies: async () => ({ get: () => undefined }),
}));

const signOut = vi.fn(async () => ({ error: null }));
vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({
    auth: {
      getUser: async () => ({ data: { user: { id: "u1", email: "colado@example.com" } } }),
      exchangeCodeForSession: async () => ({ error: null }),
      signOut,
      signInAnonymously: async () => ({ data: { user: { id: "anon-2" } }, error: null }),
    },
  }),
}));

import { GET } from "./route";

function destino(res: Response): string {
  const loc = new URL(res.headers.get("location") ?? "", "http://test");
  return `${loc.pathname}${loc.search}`;
}

describe("GET /auth/callback: la allowlist vale para todo camino de sesión", () => {
  beforeEach(() => {
    invitado = true;
    estaEnAllowlist.mockClear();
    bienvenidaTrasLogin.mockClear();
    signOut.mockClear();
  });

  it("recuperación con un correo NO invitado: sesión fuera y de vuelta al login", async () => {
    invitado = false;
    const res = await GET(new Request("http://test/auth/callback?code=abc&type=recovery"));
    expect(estaEnAllowlist).toHaveBeenCalledWith("colado@example.com");
    expect(signOut).toHaveBeenCalled();
    expect(destino(res)).toMatch(/^\/login\?google=no-invitado/);
  });

  it("recuperación con un correo invitado: va a fijar la contraseña nueva", async () => {
    const res = await GET(new Request("http://test/auth/callback?code=abc&type=recovery"));
    expect(signOut).not.toHaveBeenCalled();
    expect(destino(res)).toBe("/auth/update-password");
  });

  it("login normal con un correo NO invitado sigue rechazado", async () => {
    invitado = false;
    const res = await GET(new Request("http://test/auth/callback?code=abc"));
    expect(signOut).toHaveBeenCalled();
    expect(destino(res)).toMatch(/^\/login\?google=no-invitado/);
  });
});
