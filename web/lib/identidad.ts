/**
 * identidad.ts — ETAPA 2 (la frontera): distinguir la identidad INVISIBLE
 * (el invitado que acuña proxy.ts para el organizador gratuito) de una
 * CUENTA REAL (magic link + allowlist). La web y el organizador siguen
 * libres; el motor de pago exige cuenta real desde "Iniciar La Exploración".
 */
import type { User } from "@supabase/supabase-js";
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { SERVIDOR_COMUN } from "./i18n/mensajes/servidorComun";

export const DOMINIO_INVITADO = "@invitado.my-idea.local";

/** true si el usuario es la identidad invisible (anónimo de Supabase o el
 * invitado de respaldo acuñado por proxy.ts). */
export function esInvitadoInvisible(user: Pick<User, "is_anonymous" | "email"> | null | undefined): boolean {
  if (!user) return true;
  if (user.is_anonymous) return true;
  return (user.email ?? "").toLowerCase().endsWith(DOMINIO_INVITADO);
}

/** El aviso del 401 de frontera, en palabras de persona. La UI lo detecta por
 * `login_requerido` y lleva al login conservando adónde volver. */
export function avisoLogin(idioma: Locale = LOCALE_BASE) {
  return { login_requerido: true, error: elegir(SERVIDOR_COMUN, idioma).avisoLogin } as const;
}

/** El aviso en el idioma base (para quien aún no elige por idioma). */
export const AVISO_LOGIN = avisoLogin(LOCALE_BASE);
