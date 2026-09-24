// AUD-09 M50 (tanda 7A, seguridad): re-enrolar el autenticador con el doble
// factor ya activo (por correo o por otra app) cambiaba el método y pisaba el
// secreto ANTES de verificar el código nuevo. Si el usuario abandonaba el QR, el
// candado quedaba pidiendo un autenticador que nunca configuró: solo entraba con
// un código de rescate. Ahora el secreto nuevo espera en totp_secret_pendiente
// (migración 043) y solo pasa a vigente al verificar un código de ÉL.
import { beforeEach, describe, expect, it, vi } from "vitest";

const escrituras: Array<{ op: string; payload: Record<string, unknown> }> = [];
let estado = { habilitado: true, metodo: "email" as "totp" | "email" | null, totpSecret: null as string | null, totpSecretPendiente: null as string | null, totpLastUsedStep: null as number | null };

vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  sesionRealDeCookies: async () => ({ user: { id: "u1", email: "a@b.c" }, sessionId: "s1" }),
  estadoSeguridad: async () => estado,
  desafioSuperadoEnSesion: async () => true,
  candado2FAActivo: async () => false,
  registrarIntento2FA: async () => undefined,
}));
vi.mock("@/lib/dosFactores", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/dosFactores")>()),
  createTotpEnrollment: async () => ({ secret: "NUEVO", otpauthUrl: "otpauth://x", qrDataUrl: "data:x" }),
  encryptTotpSecret: (s: string) => `enc(${s})`,
  decryptTotpSecret: (s: string) => s.replace(/^enc\((.*)\)$/, "$1"),
  verifyTotpTokenWithReplayGuard: (secreto: string, token: string) =>
    secreto === "NUEVO" && token === "123456" ? { verified: true, replayed: false, usedStep: 42 } : { verified: false, replayed: false, usedStep: null },
  generateRecoveryCodes: () => ["r1"],
  hashRecoveryCodes: async () => ["h1"],
}));
vi.mock("@/lib/supabase/admin", () => ({
  createAdminClient: () => ({
    from: () => ({
      upsert: async (payload: Record<string, unknown>) => (escrituras.push({ op: "upsert", payload }), { error: null }),
      update: (payload: Record<string, unknown>) => ({
        eq: async () => (escrituras.push({ op: "update", payload }), { error: null }),
      }),
    }),
    rpc: async () => ({ error: null }),
  }),
}));

import { POST as enrolar } from "./enroll/route";
import { POST as verificar } from "./verificar/route";

beforeEach(() => {
  escrituras.length = 0;
  process.env.TOTP_ENCRYPTION_KEY = "k".repeat(32);
  estado = { habilitado: true, metodo: "email", totpSecret: null, totpSecretPendiente: null, totpLastUsedStep: null };
});

describe("re-enrolar no desarma el candado vigente (AUD-09 M50)", () => {
  it("enrolar guarda el secreto nuevo como PENDIENTE y no toca el método ni el secreto vigente", async () => {
    const res = await enrolar();
    expect(res.status).toBe(200);
    const w = escrituras.at(-1)!.payload;
    expect(w.totp_secret_pendiente).toBe("enc(NUEVO)");
    expect(w).not.toHaveProperty("two_factor_method");
    expect(w).not.toHaveProperty("totp_secret");
  });

  it("verificar con un código del autenticador nuevo lo vuelve vigente y cambia el método", async () => {
    estado = { ...estado, totpSecretPendiente: "enc(NUEVO)" };
    const res = await verificar(new Request("http://x", { method: "POST", body: JSON.stringify({ token: "123456" }) }));
    expect(res.status).toBe(200);
    const w = escrituras.find((e) => e.op === "update")!.payload;
    expect(w).toMatchObject({ two_factor_enabled: true, two_factor_method: "totp", totp_secret: "enc(NUEVO)", totp_secret_pendiente: null, totp_last_used_step: 42 });
  });

  it("en un alta en curso, un código de rescate no activa el autenticador nuevo", async () => {
    estado = { ...estado, totpSecretPendiente: "enc(NUEVO)" };
    const res = await verificar(new Request("http://x", { method: "POST", body: JSON.stringify({ recoveryCode: "r1" }) }));
    expect(res.status).toBe(401);
    expect(escrituras.find((e) => e.op === "update")).toBeUndefined();
  });
});
