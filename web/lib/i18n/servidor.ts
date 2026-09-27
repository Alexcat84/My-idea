/**
 * El idioma de la interfaz del lado del servidor, leído de la cookie
 * `myidea_idioma` que escribe proxy.ts (DISENO §3.2). Las rutas de /api lo
 * leen de su Request (proxy.ts no corre en /api, pero la cookie viaja igual);
 * los componentes del servidor, de next/headers.
 */
import { COOKIE_IDIOMA, normalizarIdioma, type ActiveLocale } from "./config";

/** El valor de una cookie en una cabecera Cookie. */
function cookieDe(cabecera: string | null, nombre: string): string | null {
  if (!cabecera) return null;
  for (const par of cabecera.split(";")) {
    const i = par.indexOf("=");
    if (i > 0 && par.slice(0, i).trim() === nombre) return decodeURIComponent(par.slice(i + 1).trim());
  }
  return null;
}

/** Para las rutas de /api: el idioma de la petición. */
export function idiomaDeRequest(request: Request): ActiveLocale {
  return normalizarIdioma(cookieDe(request.headers.get("cookie"), COOKIE_IDIOMA));
}

/** Para los componentes del servidor y el layout. */
export async function idiomaDeCookies(): Promise<ActiveLocale> {
  const { cookies } = await import("next/headers");
  return normalizarIdioma((await cookies()).get(COOKIE_IDIOMA)?.value);
}
