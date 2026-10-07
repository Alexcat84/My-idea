// AUD-09 H07: al registrarse, la identidad invisible del navegador (la prueba
// de posesión es la cookie de ESTE request) queda anotada en la cuenta nueva,
// para adoptar sus ideas al confirmar desde cualquier navegador.
import { beforeEach, describe, expect, it, vi } from "vitest";

const registrarAdopcionPendiente = vi.fn(async () => undefined);
const signUp = vi.fn<(args: unknown) => Promise<{ data: { user: { id: string; identities: { id: string }[] } }; error: null }>>(
  async () => ({ data: { user: { id: "real-1", identities: [{ id: "i" }] } }, error: null })
);
vi.mock("@/lib/cuentas", () => ({
  estaEnAllowlist: async () => true,
  registrarAdopcionPendiente: (...a: unknown[]) => registrarAdopcionPendiente(...(a as [])),
}));
const guardarAceptacion = vi.fn<(userId: string, idioma: string) => Promise<void>>(async () => undefined);
vi.mock("@/lib/legal/aceptacionServidor", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/legal/aceptacionServidor")>()),
  guardarAceptacion: (userId: string, idioma: string) => guardarAceptacion(userId, idioma),
}));
vi.mock("@/lib/identidad", () => ({ esInvitadoInvisible: (u: { is_anonymous?: boolean }) => u.is_anonymous === true }));
vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({
    auth: {
      getUser: async () => ({ data: { user: { id: "anon-1", is_anonymous: true } } }),
      signUp: (args: unknown) => signUp(args),
    },
  }),
}));

import { POST } from "./route";
import { VERSION_LEGAL } from "@/lib/legal/consentimiento";

describe("POST /api/auth/registrar", () => {
  beforeEach(() => {
    registrarAdopcionPendiente.mockClear();
    signUp.mockClear();
  });

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

  // i18n F6 (D4): el idioma de la interfaz queda en user_metadata.idioma, que es
  // lo que lee el Send Email Hook para mandar el correo de confirmación.
  it("guarda el idioma de la interfaz en user_metadata al crear la cuenta", async () => {
    await POST(
      new Request("http://test/api/auth/registrar", {
        method: "POST",
        headers: { cookie: "myidea_idioma=ko" },
        body: JSON.stringify({ email: "ana@example.com", password: "Una-clave-larga-1" }),
      })
    );
    const args = signUp.mock.calls[0][0] as { options: { data?: { idioma?: string } } };
    expect(args.options.data).toEqual({ idioma: "ko" });
  });

  it("sin cookie, el idioma guardado es el español", async () => {
    await POST(
      new Request("http://test/api/auth/registrar", {
        method: "POST",
        body: JSON.stringify({ email: "ana@example.com", password: "Una-clave-larga-1" }),
      })
    );
    const args = signUp.mock.calls[0][0] as { options: { data?: { idioma?: string } } };
    expect(args.options.data).toEqual({ idioma: "es" });
  });
});

// AL CREAR LA CUENTA (corrección del fundador, 7 oct 2026, punto 3): la línea "Al continuar, aceptas los Términos y
// la Política de Privacidad" está junto al botón de crear la cuenta; si la pantalla manda la aceptación de la versión
// vigente, se guarda en la cuenta nueva. Si el correo ya tenía cuenta, no se escribe nada (no se revela ni se toca una
// cuenta ajena). Prueba en rojo primero.
describe("POST /api/auth/registrar guarda la aceptación de la línea del login", () => {
  function crearCon(acepta: unknown) {
    return POST(
      new Request("http://test/api/auth/registrar", {
        method: "POST",
        body: JSON.stringify({ email: "ana@example.com", password: "Una-clave-larga-1", acepta_legal: acepta }),
      })
    );
  }
  beforeEach(() => {
    guardarAceptacion.mockClear();
    signUp.mockClear();
  });

  it("una cuenta nueva con la versión vigente: la guarda", async () => {
    const res = await crearCon({ version: VERSION_LEGAL, idioma_texto: "es" });
    expect(res.status).toBe(200);
    expect(guardarAceptacion).toHaveBeenCalledWith("real-1", "es");
  });

  it("un correo que ya tenía cuenta: no escribe nada", async () => {
    signUp.mockResolvedValueOnce({ data: { user: { id: "otro", identities: [] } }, error: null });
    await crearCon({ version: VERSION_LEGAL, idioma_texto: "es" });
    expect(guardarAceptacion).not.toHaveBeenCalled();
  });

  it("una versión vieja: no la guarda", async () => {
    await crearCon({ version: "2000-01-01", idioma_texto: "es" });
    expect(guardarAceptacion).not.toHaveBeenCalled();
  });
});
