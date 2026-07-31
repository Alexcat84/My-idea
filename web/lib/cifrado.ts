/**
 * cifrado — AES-256-GCM genérico (mismo formato que el secreto TOTP de
 * dosFactores.ts: `iv.tag.payload`, los tres en base64). Se usa para guardar el
 * refresh_token de Google cifrado en la base (la clave nunca toca al cliente).
 * SOLO server-side (usa node:crypto). La passphrase se pasa por sha256 a 32 B.
 */
import { createCipheriv, createDecipheriv, createHash, randomBytes } from "node:crypto";

export function cifrar(texto: string, clave: string): string {
  const iv = randomBytes(12);
  const key = createHash("sha256").update(clave).digest();
  const cipher = createCipheriv("aes-256-gcm", key, iv);
  const enc = Buffer.concat([cipher.update(texto, "utf8"), cipher.final()]);
  const tag = cipher.getAuthTag();
  return `${iv.toString("base64")}.${tag.toString("base64")}.${enc.toString("base64")}`;
}

export function descifrar(valor: string, clave: string): string {
  const [ivB64, tagB64, payloadB64] = valor.split(".");
  if (!ivB64 || !tagB64 || !payloadB64) throw new Error("valor cifrado inválido");
  const key = createHash("sha256").update(clave).digest();
  const decipher = createDecipheriv("aes-256-gcm", key, Buffer.from(ivB64, "base64"));
  decipher.setAuthTag(Buffer.from(tagB64, "base64"));
  const dec = Buffer.concat([decipher.update(Buffer.from(payloadB64, "base64")), decipher.final()]);
  return dec.toString("utf8");
}
