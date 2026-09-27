/**
 * La cita del motivo al final de una entrada de la bitácora (i18n F3). En
 * español el builder escribe "Retiraste X: «motivo»" y la pantalla colorea la
 * cita; en otros idiomas cambian las comillas (“…”, „…“, 「…」) y los dos puntos
 * (" : " en francés, "：" en japonés y chino). Aquí se reconocen todas.
 */

/** Pares de comillas (apertura, cierre) que puede traer un motivo citado. */
const PARES: ReadonlyArray<readonly [string, string]> = [
  ["«", "»"],
  ["“", "”"],
  ["„", "“"],
  ["「", "」"],
  ["『", "』"],
  ["‘", "’"],
  ['"', '"'],
];

const escapar = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const ALTERNATIVAS = PARES.map(([a, c]) => `${escapar(a)}[\\s\\S]*${escapar(c)}`).join("|");
const PATRON = new RegExp(`^([\\s\\S]*?)(\\s?[:：]\\s?)(${ALTERNATIVAS})$`);

/** [lo de antes, el separador, la cita con sus comillas], o null si el texto no
 * termina en un motivo citado. */
export function partirMotivo(texto: string): [string, string, string] | null {
  const m = texto.match(PATRON);
  return m ? [m[1], m[2], m[3]] : null;
}
