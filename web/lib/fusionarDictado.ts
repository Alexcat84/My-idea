/**
 * AUD-09 B14b: funde un evento del dictado en el valor del campo. Lo
 * provisional (lo que aún se está oyendo) vive DENTRO del valor como un sufijo,
 * así que enviar o detener el micrófono a mitad de frase no lo pierde. El
 * siguiente evento recorta ese sufijo (si sigue al final: el usuario pudo
 * editar a mano) y pone encima lo final y lo nuevo provisional. Pura.
 */
export function fusionarDictado(
  valor: string,
  sufijoPrevio: string,
  nuevoFinal: string,
  provisional: string
): { valor: string; sufijo: string } {
  let base = valor;
  if (sufijoPrevio && base.endsWith(sufijoPrevio)) base = base.slice(0, base.length - sufijoPrevio.length);
  const trozo = nuevoFinal.trim();
  if (trozo) base = base ? `${base} ${trozo}` : trozo;
  const p = provisional.trim();
  const sufijo = p ? (base ? ` ${p}` : p) : "";
  return { valor: base + sufijo, sufijo };
}
