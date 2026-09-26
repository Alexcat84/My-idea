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
 * Si las credenciales no están en el entorno de DESARROLLO (dev local sin
 * .env completo), los límites se desactivan con un aviso en consola. En
 * producción, sin credenciales o con la base caída, la IA FALLA CERRADA
 * (decisión del fundador, 25 sep 2026; ver contarEnUpstash).
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolar, plural } from "./i18n/interpolar";
import { SERVIDOR_COMUN } from "./i18n/mensajes/servidorComun";

const LIMITE_DIARIO_DEFAULT = 5;
const FUSIBLE_DEFAULT = 30;

interface ResultadoLimite {
  permitido: boolean;
  usados: number;
  limite: number;
  /** La base del contador no respondió: no es un tope alcanzado, es una
   * caída. Las rutas de la IA lo dicen con su propio mensaje (503). */
  caido?: boolean;
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

/** INCR + EXPIRE(primera del periodo) contra Upstash.
 *
 * UPSTASH CAÍDO (decisión del fundador, 25 sep 2026): si la base no responde
 * (la red falla o responde con error), el resultado es FALLA CERRADA:
 * `permitido: false, caido: true`, con un error explícito en los registros. El
 * 24 sep la base desapareció, `fetch` lanzó sin que nadie lo atrapara y toda la
 * IA dio un 500 genérico; el comentario de entonces prometía "se permite y se
 * registra" y solo lo cumplía si Upstash respondía. Sin el contador no hay tope
 * de gasto (el fusible también vive aquí), así que la IA se detiene. */
async function contarEnUpstash(clave: string, ttlSegundos: number, limite: number): Promise<ResultadoLimite> {
  const cred = credencialesUpstash();
  if (!cred) {
    // En producción, sin credenciales no hay contador: es una caída, no un
    // permiso. En desarrollo y en las pruebas, los límites se apagan.
    if (process.env.NODE_ENV === "production") {
      console.error("[rateLimit] UPSTASH NO RESPONDE: faltan UPSTASH_REDIS_REST_URL/TOKEN en producción; se detiene la IA (falla cerrada)", { clave });
      return { permitido: false, usados: 0, limite, caido: true };
    }
    console.warn("rateLimit: UPSTASH_REDIS_REST_URL/TOKEN ausentes; limite desactivado");
    return { permitido: true, usados: 0, limite, caido: false };
  }
  const headers = { Authorization: `Bearer ${cred.token}` };
  let usados: number;
  try {
    const resIncr = await fetch(`${cred.url}/incr/${encodeURIComponent(clave)}`, { headers });
    if (!resIncr.ok) throw new Error(`INCR respondió ${resIncr.status}`);
    usados = Number(((await resIncr.json()) as { result: number }).result);
    if (!Number.isFinite(usados)) throw new Error("INCR sin número");
  } catch (e) {
    console.error("[rateLimit] UPSTASH NO RESPONDE: se detiene la IA (falla cerrada)", { clave, error: e instanceof Error ? e.message : String(e) });
    return { permitido: false, usados: 0, limite, caido: true };
  }
  if (usados === 1) {
    await fetch(`${cred.url}/expire/${encodeURIComponent(clave)}/${ttlSegundos}`, { headers }).catch((e) => {
      console.error("[rateLimit] EXPIRE falló; la clave queda sin vencimiento", { clave, error: e instanceof Error ? e.message : String(e) });
    });
  }
  return { permitido: usados <= limite, usados, limite, caido: false };
}

/** El latido diario a la base del contador (decisión del fundador, 25 sep
 * 2026): lo da la tarea programada para que una base gratuita sin uso no se
 * archive (como la que desapareció el 24 sep) y para enterarse si no responde. */
export async function latidoUpstash(): Promise<"vivo" | "caido" | "sin_credenciales"> {
  const cred = credencialesUpstash();
  if (!cred) return "sin_credenciales";
  try {
    const res = await fetch(`${cred.url}/incr/myidea:latido`, { headers: { Authorization: `Bearer ${cred.token}` } });
    return res.ok ? "vivo" : "caido";
  } catch {
    return "caido";
  }
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
 * (5 por usuario / 10 min). Upstash caído: aquí se deja pasar (no es la IA), ver el cuerpo. */
export async function limitarPorClave(clave: string, ttlSegundos: number, limite: number): Promise<ResultadoLimite> {
  const r = await contarEnUpstash(`myidea:k:${clave}`, ttlSegundos, limite);
  // Este límite no es de la IA (los envíos del código de doble factor): con la
  // base caída no se le cierra a nadie la entrada a su cuenta. Se deja pasar y
  // el error ya quedó registrado en contarEnUpstash.
  return r.caido ? { ...r, permitido: true } : r;
}

/** Mensajes en palabras de persona (el usuario web nunca ve maquinaria). */
// AUD-09 B05: el límite dice su número REAL (sale de LIMITE_ARRANQUES_DIA);
// antes el texto decía "5" fijo aunque el entorno dijera otra cosa.
export function mensajeLimite(limite: number, idioma: Locale = LOCALE_BASE): string {
  const t = elegir(SERVIDOR_COMUN, idioma);
  return interpolar(t.limiteDiario, { arranques: plural(idioma, limite, t.arranques) });
}

export function mensajeFusible(idioma: Locale = LOCALE_BASE): string {
  return elegir(SERVIDOR_COMUN, idioma).fusible;
}
export const MENSAJE_FUSIBLE = mensajeFusible(LOCALE_BASE);

/** La base del contador cayó (decisión del fundador, 25 sep 2026): qué pasa y
 * que no se cobró nada. Nunca el genérico. */
export function mensajeServicioNoDisponible(idioma: Locale = LOCALE_BASE): string {
  return elegir(SERVIDOR_COMUN, idioma).servicioNoDisponible;
}

export const MENSAJE_SERVICIO_NO_DISPONIBLE = mensajeServicioNoDisponible(LOCALE_BASE);
