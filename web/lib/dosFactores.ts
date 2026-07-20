/**
 * dosFactores.ts — Centro de cuenta: el motor 2FA replicado del I Ching
 * (backend/auth/src/index.ts, en producción allá). Los nombres se conservan
 * en inglés A PROPÓSITO: permiten cotejar contra la referencia línea a
 * línea. Piezas: TOTP (otplib preset v12, el mismo de allá) con QR, guardia
 * anti-replay por step, secreto cifrado AES-256-GCM (TOTP_ENCRYPTION_KEY),
 * 8 códigos de recuperación bcrypt, candado tras 5 fallos en 15 minutos y
 * el hash de los códigos por correo. Puro y testeable: aquí no entra
 * Supabase ni Resend.
 */
import bcrypt from "bcryptjs";
import { authenticator } from "@otplib/preset-default";
import QRCode from "qrcode";
import { createCipheriv, createDecipheriv, createHash, randomBytes, randomInt } from "node:crypto";

export interface TotpEnrollment {
  secret: string;
  otpauthUrl: string;
  qrDataUrl: string;
}

const TOTP_STEP_MS = 30_000;
/** ±1 step (~30s por lado) por deriva de reloj del teléfono (I Ching). */
const TOTP_VERIFY_WINDOW = 1;

export async function createTotpEnrollment(email: string, issuer = "My Idea"): Promise<TotpEnrollment> {
  const secret = authenticator.generateSecret();
  const otpauthUrl = authenticator.keyuri(email, issuer, secret);
  const qrDataUrl = await QRCode.toDataURL(otpauthUrl, { margin: 1, width: 280 });
  return { secret, otpauthUrl, qrDataUrl };
}

export type TotpVerificationResult = {
  verified: boolean;
  replayed: boolean;
  usedStep: number | null;
};

/** Verifica el token TOTP y además impide REUSAR un código ya aceptado
 * (replay): cada verificación exitosa registra su step y ningún step menor
 * o igual vuelve a pasar (I Ching, migración 016). */
export function verifyTotpTokenWithReplayGuard(
  secret: string,
  token: string,
  opts?: { lastUsedStep?: number | null; nowMs?: number }
): TotpVerificationResult {
  const nowMs = opts?.nowMs ?? Date.now();
  authenticator.options = { window: TOTP_VERIFY_WINDOW };
  const delta = authenticator.checkDelta(token, secret);
  if (typeof delta !== "number") {
    return { verified: false, replayed: false, usedStep: null };
  }
  const usedStep = Math.floor(nowMs / TOTP_STEP_MS) + delta;
  const lastUsedStep = opts?.lastUsedStep;
  if (typeof lastUsedStep === "number" && usedStep <= lastUsedStep) {
    return { verified: false, replayed: true, usedStep };
  }
  return { verified: true, replayed: false, usedStep };
}

/** 12 hex = 48 bits de entropía por código (I Ching). */
export function generateRecoveryCodes(count = 8): string[] {
  return Array.from({ length: count }, () => randomBytes(6).toString("hex").toUpperCase());
}

export async function hashRecoveryCodes(codes: string[]): Promise<string[]> {
  return Promise.all(codes.map((code) => bcrypt.hash(code, 10)));
}

export async function consumeRecoveryCode(
  code: string,
  hashes: string[]
): Promise<{ consumed: boolean; remainingHashes: string[] }> {
  for (let i = 0; i < hashes.length; i += 1) {
    const ok = await bcrypt.compare(code, hashes[i]!);
    if (ok) {
      const remaining = hashes.filter((_, idx) => idx !== i);
      return { consumed: true, remainingHashes: remaining };
    }
  }
  return { consumed: false, remainingHashes: hashes };
}

export interface TwoFactorAttempt {
  timestampMs: number;
  success: boolean;
}

/** Candado: 5 fallos dentro de los últimos 15 minutos (I Ching). */
export function shouldLockTwoFactor(attempts: TwoFactorAttempt[], nowMs = Date.now()): boolean {
  const withinWindow = attempts.filter((a) => nowMs - a.timestampMs <= 15 * 60 * 1000);
  const failed = withinWindow.filter((a) => !a.success).length;
  return failed >= 5;
}

export function encryptTotpSecret(secret: string, encryptionKey: string): string {
  const iv = randomBytes(12);
  const key = createHash("sha256").update(encryptionKey).digest();
  const cipher = createCipheriv("aes-256-gcm", key, iv);
  const encrypted = Buffer.concat([cipher.update(secret, "utf8"), cipher.final()]);
  const tag = cipher.getAuthTag();
  return `${iv.toString("base64")}.${tag.toString("base64")}.${encrypted.toString("base64")}`;
}

export function decryptTotpSecret(encryptedValue: string, encryptionKey: string): string {
  const [ivB64, tagB64, payloadB64] = encryptedValue.split(".");
  if (!ivB64 || !tagB64 || !payloadB64) {
    throw new Error("Invalid encrypted secret format");
  }
  const key = createHash("sha256").update(encryptionKey).digest();
  const decipher = createDecipheriv("aes-256-gcm", key, Buffer.from(ivB64, "base64"));
  decipher.setAuthTag(Buffer.from(tagB64, "base64"));
  const decrypted = Buffer.concat([decipher.update(Buffer.from(payloadB64, "base64")), decipher.final()]);
  return decrypted.toString("utf8");
}

// ── Códigos por correo (I Ching: api/auth/2fa/email/send) ────────────────

export const EMAIL_CODE_TTL_MINUTES = 10;

/** Hash del código con pimienta de servidor (TWO_FACTOR_EMAIL_CODE_SECRET):
 * la base jamás guarda el código en claro. */
export function hashEmailCode(code: string, secret: string): string {
  return createHash("sha256").update(`${code}:${secret}`).digest("hex");
}

export function createSixDigitCode(): string {
  return String(randomInt(0, 1_000_000)).padStart(6, "0");
}
