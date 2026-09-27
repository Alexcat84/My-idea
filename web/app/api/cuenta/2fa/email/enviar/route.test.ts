// i18n F6 (D4): el correo del código de 2FA sale en el idioma de la interfaz
// (cookie), con lang y dir en el html (el árabe de derecha a izquierda). Sin
// secretos reales: entorno falso explícito y Resend (fetch) como doble.
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { interpolar } from "@/lib/i18n/interpolar";
import { SERVIDOR_DOS_FACTORES } from "@/lib/i18n/mensajes/servidorDosFactores";

vi.mock("@/lib/seguridad", () => ({
  sesionRealDeCookies: async () => ({ user: { id: "u1", email: "ana@example.com" }, sessionId: "s1" }),
  estadoSeguridad: async () => ({ habilitado: false }),
  desafioSuperadoEnSesion: async () => true,
  aviso2FA: () => ({ error: "2fa" }),
  ipDelRequest: () => "127.0.0.1",
}));
vi.mock("@/lib/rateLimit", () => ({ limitarPorClave: async () => ({ permitido: true }) }));
vi.mock("@/lib/supabase/admin", () => {
  const cadena = { delete: () => cadena, eq: () => cadena, is: async () => ({ error: null }), insert: async () => ({ error: null }) };
  return { createAdminClient: () => ({ from: () => cadena }) };
});

import { POST } from "./route";

const fetchFalso = vi.fn();

beforeEach(() => {
  vi.stubEnv("RESEND_API_KEY", "test-fake-resend-key");
  vi.stubEnv("TWO_FACTOR_EMAIL_FROM", "My Idea <no-reply@example.com>");
  vi.stubEnv("TWO_FACTOR_EMAIL_CODE_SECRET", "test-fake-code-secret");
  fetchFalso.mockReset();
  fetchFalso.mockResolvedValue(new Response("{}", { status: 200 }));
  vi.stubGlobal("fetch", fetchFalso);
});

afterEach(() => {
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
});

async function enviarCon(cookie: string) {
  const res = await POST(new Request("http://test/api/cuenta/2fa/email/enviar", { method: "POST", headers: { cookie } }));
  expect(res.status).toBe(200);
  return JSON.parse(String((fetchFalso.mock.calls[0][1] as RequestInit).body)) as { subject: string; text: string; html: string };
}

describe("POST /api/cuenta/2fa/email/enviar: el idioma del correo", () => {
  it("en árabe: asunto del catálogo y html con lang=ar dir=rtl", async () => {
    const correo = await enviarCon("myidea_idioma=ar");
    const t = SERVIDOR_DOS_FACTORES.ar.correo;
    const codigo = correo.subject.slice(0, 6);
    expect(codigo).toMatch(/^\d{6}$/);
    expect(correo.subject).toBe(interpolar(t.asunto, { codigo }));
    expect(correo.html).toContain('lang="ar"');
    expect(correo.html).toContain('dir="rtl"');
    expect(correo.html).toContain(t.htmlTuCodigo);
  });

  it("en español sigue el mismo texto de siempre, con lang=es dir=ltr", async () => {
    const correo = await enviarCon("myidea_idioma=es");
    expect(correo.subject).toMatch(/^\d{6} es tu código de verificación de My Idea$/);
    expect(correo.html).toContain('lang="es"');
    expect(correo.html).toContain('dir="ltr"');
    expect(correo.html).toContain("<p>Tu código de verificación es:</p>");
  });

  it("el chino va como zh-Hans", async () => {
    const correo = await enviarCon("myidea_idioma=zh");
    expect(correo.html).toContain('lang="zh-Hans"');
  });
});
