/**
 * rateLimit.ts — Fase 3.2 (item del plan original de Fase 3.0): límite
 * de beta de 5 arranques al día (ideas nuevas + entrevistas), patrón
 * Upstash del proyecto I Ching. Ventana fija por día UTC via INCR +
 * EXPIRE sobre el REST API de Upstash (sin SDK: dos fetch).
 *
 * Solo se cobra el ARRANQUE de trabajo caro (organizador, inicio de
 * entrevista); los turnos siguientes de una entrevista ya arrancada no
 * cuentan — cortar a alguien a mitad de entrevista sería castigarlo por
 * habernos respondido.
 *
 * Pre-beta (fusible, post-auditoría v1.3.2):
 * 1. FUSIBLE GLOBAL: tope diario de arranques de TODA la app
 *    (FUSIBLE_SESIONES_DIA, default 30; 0 o negativo lo desactiva).
 *    Contador único por día UTC con TTL de 48h. Se verifica ANTES de
 *    cobrar créditos y de tocar la API. Al superarse, toda la app
 *    responde 503 en palabras de persona (MENSAJE_FUSIBLE).
 * 2. El límite de 5/día pasa de user-id a IP mientras la identidad de
 *    invitado sea invisible (proxy.ts) y no haya auth real: con user-id
 *    compartido o rotable el límite era decorativo. RATE_LIMIT_POR=usuario
 *    lo revierte cuando llegue el clon de cuentas. El fusible global es
 *    el respaldo si la IP rota.
 *
 * Si las credenciales no están en el entorno (dev local sin .env
 * completo), los límites se desactivan con un aviso en consola: nunca
 * deben romper el flujo por configuración faltante.
 */

const LIMITE_DIARIO_DEFAULT = 5;
const FUSIBLE_DEFAULT = 30;

interface ResultadoLimite {
  permitido: boolean;
  usados: number;
  limite: number;
}

function credencialesUpstash(): { url: string; token: string } | null {
  const url = process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!url || !token) return null;
  return { url, token };
}

/** El dev user de los arneses (vuelo.ts/probar.ts) queda exento SOLO
 * fuera de produccion: una corrida del vuelo hace varios arranques y dos
 * corridas el mismo dia reventarian ambos limites. En produccion la
 * exencion se apaga (hallazgo del review de seguridad: la credencial del
 * dev user vive en el repo y la anon key es publica por diseno). */
function esDevUserExento(email?: string | null): boolean {
  return process.env.NODE_ENV !== "production" && email === "dev@my-idea.local";
}

/** INCR + EXPIRE(primera del periodo) contra Upstash. Upstash caído no
 * debe tumbar el producto: se permite y se registra. */
async function contarEnUpstash(clave: string, ttlSegundos: number, limite: number): Promise<ResultadoLimite> {
  const cred = credencialesUpstash();
  if (!cred) {
    console.warn("rateLimit: UPSTASH_REDIS_REST_URL/TOKEN ausentes; limite desactivado");
    return { permitido: true, usados: 0, limite };
  }
  const headers = { Authorization: `Bearer ${cred.token}` };
  const resIncr = await fetch(`${cred.url}/incr/${encodeURIComponent(clave)}`, { headers });
  if (!resIncr.ok) {
    console.warn(`rateLimit: INCR fallo (${resIncr.status}); se permite la solicitud`);
    return { permitido: true, usados: 0, limite };
  }
  const usados = Number(((await resIncr.json()) as { result: number }).result);
  if (usados === 1) {
    await fetch(`${cred.url}/expire/${encodeURIComponent(clave)}/${ttlSegundos}`, { headers }).catch(() => {});
  }
  return { permitido: usados <= limite, usados, limite };
}

function diaUtc(): string {
  return new Date().toISOString().slice(0, 10); // YYYY-MM-DD (UTC)
}

/** Fusible global pre-beta: tope diario de arranques de TODA la app.
 * Verificar ANTES de cobrar créditos y de tocar la API. */
export async function verificarFusibleGlobal(email?: string | null): Promise<ResultadoLimite> {
  const limite = Number(process.env.FUSIBLE_SESIONES_DIA ?? FUSIBLE_DEFAULT);
  if (!Number.isFinite(limite) || limite <= 0) {
    // Desactivado explícitamente (la palanca de reversión es el env).
    return { permitido: true, usados: 0, limite: 0 };
  }
  if (esDevUserExento(email)) {
    return { permitido: true, usados: 0, limite };
  }
  // TTL 48h: la clave sobrevive el cambio de día para inspección, pero
  // cada día UTC tiene su propio contador.
  return contarEnUpstash(`myidea:fusible:${diaUtc()}`, 172800, limite);
}

/** Identidad del límite por-quién: IP mientras no haya auth real
 * (RATE_LIMIT_POR=usuario revierte a user-id con el clon de cuentas). */
export function identidadLimite(userId: string, request?: Request): string {
  if (process.env.RATE_LIMIT_POR === "usuario") return userId;
  const xff = request?.headers.get("x-forwarded-for");
  if (xff) return `ip:${xff.split(",")[0].trim()}`;
  const real = request?.headers.get("x-real-ip");
  if (real) return `ip:${real.trim()}`;
  // Sin headers de proxy (dev local): cae al user-id, mejor que una
  // clave global compartida.
  return userId;
}

export async function verificarLimiteDiario(identidad: string, email?: string | null): Promise<ResultadoLimite> {
  const limite = Number(process.env.LIMITE_ARRANQUES_DIA ?? LIMITE_DIARIO_DEFAULT);
  if (esDevUserExento(email)) {
    return { permitido: true, usados: 0, limite };
  }
  const clave = `myidea:rl:${identidad}:${diaUtc()}`;
  return contarEnUpstash(clave, 86400, limite);
}

/** Limitador genérico por clave (patrón rateLimitByKey del I Ching): para
 * ventanas cortas ajenas al día UTC, como los envíos de código 2FA
 * (5 por usuario / 10 min). Upstash caído no tumba el producto. */
export async function limitarPorClave(clave: string, ttlSegundos: number, limite: number): Promise<ResultadoLimite> {
  return contarEnUpstash(`myidea:k:${clave}`, ttlSegundos, limite);
}

/** Mensajes en palabras de persona (el usuario web nunca ve maquinaria). */
export const MENSAJE_LIMITE =
  "Por hoy alcanzaste el límite de la beta (5 arranques al día). " +
  "Tus ideas quedan guardadas — vuelve mañana y seguimos donde quedamos.";

export const MENSAJE_FUSIBLE = "Estamos a capacidad por hoy; tus ideas te esperan mañana.";
