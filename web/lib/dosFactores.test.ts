// Centro de cuenta: el motor 2FA replicado del I Ching. Los tests cubren lo
// PURO (TOTP+replay, cifrado, recovery, candado, hash email); las rutas se
// prueban en el vuelo de cuenta contra la base real.
import { describe, expect, it } from "vitest";
import { authenticator } from "@otplib/preset-default";
import {
  consumeRecoveryCode,
  createSixDigitCode,
  createTotpEnrollment,
  decryptTotpSecret,
  encryptTotpSecret,
  generateRecoveryCodes,
  hashEmailCode,
  hashRecoveryCodes,
  shouldLockTwoFactor,
  verifyTotpTokenWithReplayGuard,
} from "./dosFactores";

const LLAVE = "una-llave-de-cifrado-larga-para-tests-0123456789";

describe("TOTP: enrolamiento y verificación con guardia anti-replay", () => {
  it("el token generado con el secreto verifica; uno inventado no", async () => {
    const e = await createTotpEnrollment("fundador@myideaproject.com");
    expect(e.otpauthUrl).toContain("My%20Idea");
    expect(e.qrDataUrl.startsWith("data:image/png;base64,")).toBe(true);
    const token = authenticator.generate(e.secret);
    const r = verifyTotpTokenWithReplayGuard(e.secret, token);
    expect(r.verified).toBe(true);
    expect(r.replayed).toBe(false);
    expect(typeof r.usedStep).toBe("number");
    expect(verifyTotpTokenWithReplayGuard(e.secret, "000000").verified).toBe(false);
  });

  it("replay: el MISMO token no pasa dos veces (step <= lastUsedStep)", async () => {
    const e = await createTotpEnrollment("fundador@myideaproject.com");
    const token = authenticator.generate(e.secret);
    const primera = verifyTotpTokenWithReplayGuard(e.secret, token);
    expect(primera.verified).toBe(true);
    const repetida = verifyTotpTokenWithReplayGuard(e.secret, token, { lastUsedStep: primera.usedStep });
    expect(repetida.verified).toBe(false);
    expect(repetida.replayed).toBe(true);
  });
});

describe("cifrado AES-256-GCM del secreto TOTP", () => {
  it("roundtrip: cifrar y descifrar devuelve el secreto", () => {
    const cifrado = encryptTotpSecret("JBSWY3DPEHPK3PXP", LLAVE);
    expect(cifrado.split(".").length).toBe(3); // iv.tag.payload
    expect(decryptTotpSecret(cifrado, LLAVE)).toBe("JBSWY3DPEHPK3PXP");
  });

  it("con otra llave o formato roto, lanza (jamás devuelve basura muda)", () => {
    const cifrado = encryptTotpSecret("JBSWY3DPEHPK3PXP", LLAVE);
    expect(() => decryptTotpSecret(cifrado, "otra-llave-distinta-igual-de-larga-987654321")).toThrow();
    expect(() => decryptTotpSecret("sin-puntos", LLAVE)).toThrow();
  });
});

describe("códigos de recuperación", () => {
  it("8 códigos de 12 hex; consumir uno lo gasta y deja 7; repetirlo no pasa", async () => {
    const codigos = generateRecoveryCodes();
    expect(codigos.length).toBe(8);
    for (const c of codigos) expect(c).toMatch(/^[0-9A-F]{12}$/);
    const hashes = await hashRecoveryCodes(codigos);
    const consumo = await consumeRecoveryCode(codigos[3]!, hashes);
    expect(consumo.consumed).toBe(true);
    expect(consumo.remainingHashes.length).toBe(7);
    const repetido = await consumeRecoveryCode(codigos[3]!, consumo.remainingHashes);
    expect(repetido.consumed).toBe(false);
  });
});

describe("candado de intentos (5 fallos en 15 minutos)", () => {
  // A mano: now=1_000_000_000; ventana = 15*60*1000 = 900_000 ms.
  const now = 1_000_000_000;
  const dentro = (msAtras: number, success: boolean) => ({ timestampMs: now - msAtras, success });

  it("4 fallos recientes: abierto; el 5.º lo cierra", () => {
    const cuatro = [dentro(1000, false), dentro(2000, false), dentro(3000, false), dentro(4000, false)];
    expect(shouldLockTwoFactor(cuatro, now)).toBe(false);
    expect(shouldLockTwoFactor([...cuatro, dentro(5000, false)], now)).toBe(true);
  });

  it("fallos viejos (fuera de los 900_000 ms) no cuentan; los éxitos tampoco", () => {
    const viejos = Array.from({ length: 5 }, (_, i) => dentro(900_001 + i, false));
    expect(shouldLockTwoFactor(viejos, now)).toBe(false);
    const exitos = Array.from({ length: 5 }, (_, i) => dentro(1000 + i, true));
    expect(shouldLockTwoFactor(exitos, now)).toBe(false);
  });
});

describe("código por correo", () => {
  it("hash determinista con pimienta: mismo código+secreto = mismo hash; otra pimienta, otro hash", () => {
    expect(hashEmailCode("123456", "pimienta")).toBe(hashEmailCode("123456", "pimienta"));
    expect(hashEmailCode("123456", "pimienta")).not.toBe(hashEmailCode("123456", "otra"));
  });

  it("createSixDigitCode: siempre 6 dígitos con ceros a la izquierda", () => {
    for (let i = 0; i < 50; i += 1) {
      expect(createSixDigitCode()).toMatch(/^\d{6}$/);
    }
  });
});
