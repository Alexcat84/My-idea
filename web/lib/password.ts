/**
 * password.ts — reglas de contraseña del login por correo+contraseña
 * (réplica del registerStep1Schema del I Ching: mín. 8, una mayúscula, un
 * dígito). Puras y testeables; las usan la ruta de registro y la UI.
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolar } from "./i18n/interpolar";
import { REGLAS_CLAVE } from "./i18n/mensajes/acceso";

export const LARGO_MINIMO = 8;

/** Devuelve el problema de la contraseña en palabras de persona, o null si
 * es válida. */
export function validarPassword(password: string, idioma: Locale = LOCALE_BASE): string | null {
  const t = elegir(REGLAS_CLAVE, idioma);
  if (password.length < LARGO_MINIMO) return interpolar(t.corta, { n: LARGO_MINIMO });
  if (!/[A-Z]/.test(password)) return t.sinMayuscula;
  if (!/[0-9]/.test(password)) return t.sinNumero;
  return null;
}

export function passwordValida(password: string): boolean {
  return validarPassword(password) === null;
}
