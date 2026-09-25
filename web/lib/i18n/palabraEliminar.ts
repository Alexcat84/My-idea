/**
 * La palabra que se escribe para borrar la cuenta (i18n F3). Es un DATO que
 * /api/cuenta/eliminar compara, no un texto del catálogo; pero cada idioma
 * tiene la suya, y el compilador la exige en cada idioma activo (PorIdioma).
 * El servidor acepta la del idioma de quien pide y siempre la del español.
 */
import { elegir, LOCALE_BASE, type PorIdioma } from "./config";

const PALABRA: PorIdioma<string> = {
  es: "ELIMINAR",
  en: "DELETE",
};

/** La palabra a escribir en el idioma de la interfaz (ya en mayúsculas). */
export function palabraEliminar(idioma: unknown): string {
  return elegir(PALABRA, idioma);
}

const normalizar = (s: string) => s.normalize("NFC").trim().toUpperCase();

/** ¿Lo escrito confirma el borrado? Recorta y no distingue mayúsculas. */
export function esPalabraEliminar(texto: unknown, idioma: unknown): boolean {
  if (typeof texto !== "string") return false;
  const escrito = normalizar(texto);
  return escrito === normalizar(palabraEliminar(idioma)) || escrito === normalizar(PALABRA[LOCALE_BASE]);
}
