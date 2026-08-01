/**
 * feedCalendario — el token del feed de calendario suscribible (Nivel 1
 * UNIVERSAL, opción B). La suscripción a un calendario no puede mandar cabeceras
 * de auth, así que la URL lleva un token FIRMADO: `base64url(userId).firma`,
 * donde firma = HMAC-SHA256(userId) con una clave del servidor. El feed es de
 * SOLO LECTURA (las fechas del propio usuario), así que el token es de bajo
 * riesgo; verificarlo evita que alguien forje el de otro usuario.
 *
 * La clave HMAC reusa `SUPABASE_SERVICE_ROLE_KEY` (alta entropía, ya presente en
 * el entorno, nunca expuesta): sin variable nueva. Rotarla invalida todos los
 * feeds (revocación global); la per-usuario no hace falta para un feed público.
 * SOLO server-side (node:crypto).
 */
import { createHmac, timingSafeEqual } from "node:crypto";

function claveHmac(): string {
  const s = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!s) throw new Error("falta SUPABASE_SERVICE_ROLE_KEY para el feed de calendario");
  return s;
}

function firmar(userId: string): string {
  return createHmac("sha256", claveHmac()).update(userId).digest("base64url");
}

/** token = base64url(userId).firma */
export function tokenDeUsuario(userId: string): string {
  return `${Buffer.from(userId).toString("base64url")}.${firmar(userId)}`;
}

/** Verifica el token y devuelve el userId; null si no cuadra (comparación en
 * tiempo constante para no filtrar por temporización). */
export function usuarioDeToken(token: string): string | null {
  const punto = token.indexOf(".");
  if (punto <= 0) return null;
  const uidB64 = token.slice(0, punto);
  const firma = token.slice(punto + 1);
  let userId: string;
  try {
    userId = Buffer.from(uidB64, "base64url").toString("utf8");
  } catch {
    return null;
  }
  if (!userId) return null;
  const esperada = Buffer.from(firmar(userId));
  const recibida = Buffer.from(firma);
  if (esperada.length !== recibida.length) return null;
  return timingSafeEqual(esperada, recibida) ? userId : null;
}
