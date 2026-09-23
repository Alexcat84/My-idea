/**
 * nextSeguro.ts — el destino post-login "seguimos justo donde quedaste".
 * Cuando la frontera manda al login, lleva un `?next=` con la ruta a
 * reanudar; al entrar, el login vuelve ahí. Para que ese parámetro no sea
 * un agujero de open-redirect, SOLO se acepta una ruta INTERNA: empieza con
 * un único "/" (nunca "//" ni "/\", que saltarían a otro dominio). Cualquier
 * cosa sospechosa cae al home de ideas.
 *
 * AUD-09 H14: mirar caracteres sueltos no basta. El parser de URL descarta
 * tabuladores y saltos de línea, así que "/<TAB>/evil.com" pasaba el filtro y
 * resolvía a //evil.com. Por eso: (1) todo carácter de control se rechaza, y
 * (2) la vara final es el ORIGEN después de resolver la URL; lo que se
 * devuelve es la ruta ya resuelta, no el texto crudo.
 */
const ORIGEN_INTERNO = "http://interno.invalid";

export function destinoPostLogin(raw: string | null | undefined): string {
  if (!raw || raw[0] !== "/") return "/ideas";
  if (raw[1] === "/" || raw[1] === "\\") return "/ideas";
  if (/[\u0000-\u001f\u007f]/.test(raw)) return "/ideas";
  let resuelta: URL;
  try {
    resuelta = new URL(raw, ORIGEN_INTERNO);
  } catch {
    return "/ideas";
  }
  if (resuelta.origin !== ORIGEN_INTERNO) return "/ideas";
  return `${resuelta.pathname}${resuelta.search}${resuelta.hash}`;
}

/** Construye la URL del login que reanudará en `destino` (una ruta interna
 * ya conocida por el llamador). */
export function loginConNext(destino: string): string {
  return `/login?next=${encodeURIComponent(destino)}`;
}

/** La cookie corta donde /api/auth/google guarda el destino antes de salir a
 * Google; /auth/callback la lee al volver (el next no puede viajar en el
 * redirect_to de Supabase sin arriesgar el fallback a Site URL). */
export const COOKIE_NEXT = "post_login_next";
