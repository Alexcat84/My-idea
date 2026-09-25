/**
 * seguridad.ts — Centro de cuenta: la capa de servidor del 2FA (migración
 * 029). Réplica del modelo del I Ching con UNA adaptación: allá la sesión es
 * bearer y el gate por sesión vive en el cliente; aquí la sesión va en
 * cookies, así que el desafío superado se REGISTRA con el session_id del JWT
 * (two_factor_attempts.session_id) y las rutas sensibles lo exigen en el
 * servidor. Prueba verificable, no un flag del navegador.
 */
import { timingSafeEqual } from "node:crypto";
import type { User } from "@supabase/supabase-js";
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { SERVIDOR_COMUN } from "./i18n/mensajes/servidorComun";
import { esInvitadoInvisible } from "./identidad";
import { shouldLockTwoFactor } from "./dosFactores";
import { createAdminClient } from "./supabase/admin";
import { createClient } from "./supabase/server";

export interface SesionReal {
  user: User;
  /** session_id del JWT vigente (claim del access token que getUser ya
   * validó contra Supabase); null solo si el token no lo trae. */
  sessionId: string | null;
}

/** El usuario REAL de las cookies de este request (la identidad invisible no
 * tiene centro de cuenta). null = sin sesión o invitado invisible. */
export async function sesionRealDeCookies(): Promise<SesionReal | null> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user || esInvitadoInvisible(user)) return null;
  const {
    data: { session },
  } = await supabase.auth.getSession();
  return { user, sessionId: sessionIdDelJwt(session?.access_token) };
}

/** Extrae el claim session_id del access token (payload base64url). El token
 * ya fue validado por getUser; aquí solo se lee el claim. */
export function sessionIdDelJwt(accessToken: string | null | undefined): string | null {
  if (!accessToken) return null;
  try {
    const payload = JSON.parse(Buffer.from(accessToken.split(".")[1] ?? "", "base64url").toString());
    return typeof payload.session_id === "string" ? payload.session_id : null;
  } catch {
    return null;
  }
}

export interface EstadoSeguridad {
  habilitado: boolean;
  metodo: "totp" | "email" | null;
  totpSecret: string | null;
  /** AUD-09 M50: el secreto de un alta en curso, aún sin verificar. */
  totpSecretPendiente: string | null;
  totpLastUsedStep: number | null;
}

/** Fila de user_seguridad del usuario (o el estado virgen si no existe). */
export async function estadoSeguridad(userId: string): Promise<EstadoSeguridad> {
  const admin = createAdminClient();
  const COLS = "two_factor_enabled, two_factor_method, totp_secret, totp_last_used_step, totp_secret_pendiente";
  const leer = (cols: string) => admin.from("user_seguridad").select(cols).eq("user_id", userId).maybeSingle();
  let { data, error } = await leer(COLS);
  // Sin la migración 043 se lee sin el pendiente (el candado sigue igual).
  if (error && /totp_secret_pendiente/.test(error.message ?? "")) {
    console.error("[seguridad] falta la migracion 043 (totp_secret_pendiente):", error.message);
    ({ data, error } = await leer(COLS.replace(", totp_secret_pendiente", "")));
  }
  if (error) throw error;
  const fila = data as Record<string, unknown> | null;
  return {
    habilitado: Boolean(fila?.two_factor_enabled),
    metodo: (fila?.two_factor_method as "totp" | "email" | null) ?? null,
    totpSecret: (fila?.totp_secret as string | null) ?? null,
    totpSecretPendiente: (fila?.totp_secret_pendiente as string | null) ?? null,
    totpLastUsedStep: (fila?.totp_last_used_step as number | null) ?? null,
  };
}

export function ipDelRequest(request: Request): string {
  return (request.headers.get("x-forwarded-for") ?? "unknown").split(",")[0]?.trim() ?? "unknown";
}

export async function registrarIntento2FA(
  userId: string,
  ip: string,
  success: boolean,
  sessionId?: string | null
): Promise<void> {
  const admin = createAdminClient();
  const { error } = await admin.from("two_factor_attempts").insert({
    user_id: userId,
    ip_address: ip,
    success,
    session_id: success ? (sessionId ?? null) : null,
  });
  if (error) throw error;
}

/** Candado del I Ching: 5 fallos en 15 minutos (últimos 20 intentos). */
export async function candado2FAActivo(userId: string): Promise<boolean> {
  const admin = createAdminClient();
  const { data, error } = await admin
    .from("two_factor_attempts")
    .select("created_at, success")
    .eq("user_id", userId)
    .order("created_at", { ascending: false })
    .limit(20);
  if (error) throw error;
  return shouldLockTwoFactor(
    (data ?? []).map((a) => ({ timestampMs: new Date(a.created_at as string).getTime(), success: Boolean(a.success) }))
  );
}

/** ¿Esta sesión ya superó el desafío? (un success registrado con SU
 * session_id). */
export async function desafioSuperadoEnSesion(userId: string, sessionId: string | null): Promise<boolean> {
  if (!sessionId) return false;
  const admin = createAdminClient();
  const { data, error } = await admin
    .from("two_factor_attempts")
    .select("id")
    .eq("user_id", userId)
    .eq("session_id", sessionId)
    .eq("success", true)
    .limit(1)
    .maybeSingle();
  if (error) throw error;
  return data !== null;
}

/** El 403 de frontera del segundo factor, en palabras de persona. La UI lo
 * detecta por `segundo_factor_requerido` y abre el desafío. */
export function aviso2FA(idioma: Locale = LOCALE_BASE) {
  return { segundo_factor_requerido: true, error: elegir(SERVIDOR_COMUN, idioma).aviso2FA } as const;
}

/** El aviso en el idioma base (para quien aún no elige por idioma). */
export const AVISO_2FA = aviso2FA(LOCALE_BASE);

/**
 * El gate de las rutas sensibles (puntos de cobro y borrados): si el usuario
 * REAL tiene 2FA y esta sesión no ha superado el desafío, 403 AVISO_2FA.
 * Devuelve null cuando se puede seguir. La identidad invisible pasa siempre
 * (no tiene 2FA ni centro de cuenta).
 */
export async function faltaSegundoFactor(): Promise<boolean> {
  const sesion = await sesionRealDeCookies();
  if (!sesion) return false; // invisible o sin sesión: no aplica
  const estado = await estadoSeguridad(sesion.user.id);
  if (!estado.habilitado) return false;
  return !(await desafioSuperadoEnSesion(sesion.user.id, sesion.sessionId));
}

/** Comparación en tiempo constante de dos hex (I Ching). */
export function secureEqualHex(a: string, b: string): boolean {
  const aBuf = Buffer.from(a, "hex");
  const bBuf = Buffer.from(b, "hex");
  if (aBuf.length !== bBuf.length) return false;
  return timingSafeEqual(aBuf, bBuf);
}

export function normalizarCodigo(raw: string): string {
  return raw.replace(/\D/g, "").slice(0, 6);
}
