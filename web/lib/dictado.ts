/**
 * El dictado por voz, en funciones puras (las usa CampoConVoz).
 *
 * Chrome en Android no entrega los resultados como el estándar: manda cada
 * frase como una versión final NUEVA que crece, a veces la reinicia desde la
 * mitad de la anterior y a veces le cambia un acento o una mayúscula (reporte
 * del fundador con un S23, 26 sep 2026: el texto se duplicaba solo hasta el
 * tope). Por eso el campo no pega trozos: (1) textoDeSesion lee el evento
 * ENTERO y funde las versiones de una misma frase en la más reciente, y
 * (2) componerDictado REEMPLAZA el aporte de la sesión en el campo cada vez.
 * Así, lo mande como lo mande el navegador, cada frase ocupa su lugar una vez.
 */

/** Un resultado del reconocedor tal como llega. */
export interface ResultadoVoz {
  isFinal: boolean;
  transcript: string;
}

const palabras = (t: string) => t.trim().split(/\s+/).filter(Boolean);

/** Para comparar: sin mayúsculas, acentos ni puntuación. */
const normal = (p: string) =>
  p
    .toLocaleLowerCase()
    .normalize("NFD")
    .replace(/[^\p{L}\p{N}]/gu, "");

/** La misma palabra, o una palabra a medio oír y su forma completa
 * ("verificar" / "verificarlas"). */
function mismaPalabra(a: string, b: string): boolean {
  const x = normal(a);
  const y = normal(b);
  if (x === y) return true;
  return Math.min(x.length, y.length) >= 3 && (x.startsWith(y) || y.startsWith(x));
}

/** Qué fracción de palabras deben coincidir para tomar un resultado como otra
 * versión de lo ya dicho (y no como frase nueva). */
const PARECIDO_MINIMO = 0.7;

/**
 * Suma `nuevo` a lo ya dicho. Si `nuevo` es otra versión del final de lo dicho
 * (la misma frase crecida, reiniciada desde la mitad o con un acento cambiado),
 * la reemplaza; si es una versión más corta (un reenvío viejo), no cambia nada;
 * si es frase nueva, se suma al final.
 */
function fundir(dicho: string[], nuevo: string[]): string[] {
  if (!dicho.length) return nuevo;
  // Una versión de lo dicho empieza cerca del final: no más atrás que su
  // propio largo (más un margen por las palabras que cambian).
  const desde = Math.max(0, dicho.length - nuevo.length - 2);
  for (let j = desde; j < dicho.length; j++) {
    const cola = dicho.slice(j);
    const n = Math.min(cola.length, nuevo.length);
    let iguales = 0;
    for (let k = 0; k < n; k++) if (mismaPalabra(cola[k], nuevo[k])) iguales++;
    const esVersion =
      n === 1
        ? cola.length === 1 && nuevo.length > 1 && iguales === 1 // una palabra que empieza a crecer
        : iguales >= 2 && iguales / n >= PARECIDO_MINIMO;
    if (!esVersion) continue;
    return nuevo.length >= cola.length ? [...dicho.slice(0, j), ...nuevo] : dicho;
  }
  return [...dicho, ...nuevo];
}

/** El texto de la sesión del micrófono a partir de TODOS los resultados del
 * evento (no solo los nuevos: el navegador no siempre avisa bien cuáles son). */
export function textoDeSesion(results: ArrayLike<ResultadoVoz>): string {
  let dicho: string[] = [];
  for (let k = 0; k < results.length; k++) {
    const nuevo = palabras(results[k].transcript);
    if (nuevo.length) dicho = fundir(dicho, nuevo);
  }
  return dicho.join(" ");
}

/**
 * Lo que el campo recuerda de la sesión en curso: `sufijo` es su aporte, al
 * final del valor (lo que el próximo evento reemplaza); `yaColocadas` son las
 * palabras de la sesión que ya quedaron en el campo por una edición a mano (no
 * se vuelven a pegar).
 */
export interface EstadoDictado {
  sufijo: string;
  yaColocadas: number;
}

export function estadoDictadoInicial(): EstadoDictado {
  return { sufijo: "", yaColocadas: 0 };
}

/** Pone el texto de la sesión en el campo, en lugar de su aporte anterior. */
export function componerDictado(
  valor: string,
  estado: EstadoDictado,
  textoSesion: string
): { valor: string; estado: EstadoDictado } {
  let base = valor;
  if (estado.sufijo && base.endsWith(estado.sufijo)) base = base.slice(0, base.length - estado.sufijo.length);
  const trozo = palabras(textoSesion).slice(estado.yaColocadas).join(" ");
  const sufijo = trozo ? (base ? ` ${trozo}` : trozo) : "";
  return { valor: base + sufijo, estado: { sufijo, yaColocadas: estado.yaColocadas } };
}

/**
 * El usuario editó a mano mientras dictaba. Si lo dictado sigue al final, nada
 * cambia; si no (escribió al final, o lo borró), lo dicho hasta ahora queda
 * como está y la sesión solo agrega lo que se diga de aquí en adelante.
 */
export function alEditarAMano(valorNuevo: string, estado: EstadoDictado, ultimoTextoSesion: string): EstadoDictado {
  if (estado.sufijo && valorNuevo.endsWith(estado.sufijo)) return estado;
  return { sufijo: "", yaColocadas: Math.max(estado.yaColocadas, palabras(ultimoTextoSesion).length) };
}
