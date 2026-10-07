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
const guardarAceptacion = vi.fn<(userId: string, idioma: string) => Promise<void>>(async () => undefined);
vi.mock("@/lib/legal/aceptacionServidor", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/legal/aceptacionServidor")>()),
  guardarAceptacion: (userId: string, idioma: string) => guardarAceptacion(userId, idioma),
}));
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
import { VERSION_LEGAL } from "@/lib/legal/consentimiento";

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

// AL ENTRAR CON LA CUENTA (corrección del fundador, 7 oct 2026, punto 3): una línea junto al botón ("Al continuar,
// aceptas los Términos y la Política de Privacidad"), no un modal. Si la pantalla manda la aceptación de la versión
// vigente, el servidor la guarda en la cuenta tras entrar (después de la adopción, que traslada la del invitado).
// Una versión vieja no se guarda (la siguiente vez que envíe datos se le pedirá). Si guardar falla, la entrada
// sigue: el envío de datos la volverá a pedir, porque la guarda está en el servidor. Prueba en rojo primero.
describe("POST /api/auth/entrar guarda la aceptación de la línea del login", () => {
  function entrarCon(acepta: unknown) {
    return POST(
      new Request("http://test/api/auth/entrar", {
        method: "POST",
        body: JSON.stringify({ email: "ana@example.com", password: "Una-clave-larga-1", acepta_legal: acepta }),
      })
    );
  }
  beforeEach(() => guardarAceptacion.mockClear());

  it("con la versión vigente, la guarda en la cuenta con el idioma del texto", async () => {
    const res = await entrarCon({ version: VERSION_LEGAL, idioma_texto: "fr" });
    expect(res.status).toBe(200);
    expect(guardarAceptacion).toHaveBeenCalledWith("real-1", "fr");
  });

  it("con una versión vieja o sin aceptación, no guarda nada", async () => {
    await entrarCon({ version: "2000-01-01", idioma_texto: "es" });
    await entrarCon(undefined);
    expect(guardarAceptacion).not.toHaveBeenCalled();
  });

  it("si guardarla falla, la entrada sigue y queda en el registro", async () => {
    const spy = vi.spyOn(console, "error").mockImplementation(() => undefined);
    guardarAceptacion.mockRejectedValueOnce(new Error("la base no responde"));
    const res = await entrarCon({ version: VERSION_LEGAL, idioma_texto: "es" });
    expect(res.status).toBe(200);
    expect((await res.json()).ok).toBe(true);
    expect(spy).toHaveBeenCalled();
    spy.mockRestore();
  });
});
