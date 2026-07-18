/**
 * identidad.ts — ETAPA 2 (la frontera): distinguir la identidad INVISIBLE
 * (el invitado que acuña proxy.ts para el organizador gratuito) de una
 * CUENTA REAL (magic link + allowlist). La web y el organizador siguen
 * libres; el motor de pago exige cuenta real desde "Iniciar La Exploración".
 */
import type { User } from "@supabase/supabase-js";

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
export const AVISO_LOGIN = {
  login_requerido: true,
  error: "Para explorar tu idea necesitas tu cuenta. Entra con tu correo y seguimos justo donde quedaste.",
} as const;
