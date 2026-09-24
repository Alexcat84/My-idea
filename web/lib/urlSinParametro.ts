/**
 * AUD-09 M30: la misma ruta sin un parámetro de la query, conservando los
 * demás. Sirve para CONSUMIR un parámetro de un solo uso (?entrevista=1) en el
 * momento en que dispara su acción: recargar no debe repetirla.
 */
export function urlSinParametro(pathname: string, query: string, clave: string): string {
  const params = new URLSearchParams(query);
  params.delete(clave);
  const resto = params.toString();
  return resto ? `${pathname}?${resto}` : pathname;
}
