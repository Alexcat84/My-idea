/**
 * La elisión del italiano ante una cifra (i18n F6, decisión del fundador del
 * 25 sep 2026): "l'8 marzo", "dall'11 aprile", no "il 8 marzo".
 *
 * La regla: "il" y las preposiciones articuladas que lo llevan (dal, al, del,
 * nel, sul) se eliden ante una palabra que empieza por vocal. Ante una cifra
 * manda cómo se LEE: 8 "otto", 11 "undici", 80-89, 800-899, 8.000-8.999,
 * 11.000-11.999… empiezan por vocal. Es decir, la parte entera (sin los puntos
 * de miles) empieza por 8, o empieza por 11 con 2, 5, 8… cifras (undici,
 * undicimila, undici milioni). El 1 de una fecha se lee "primo" ("il 1º
 * marzo"): no se elide. Casos contados a mano en elision.test.ts.
 *
 * Las frases del catálogo ("Chiusa il {{fecha}}", "Dal {{desde}} al
 * {{hasta}}") no pueden saber qué cifra les tocará: por eso se elide DESPUÉS
 * de interpolar, y solo en italiano (el español "del 8 al 11" no se toca).
 */
import type { Locale } from "./config";
import { interpolar } from "./interpolar";

const ELIDIDO: Record<string, string> = {
  il: "l'",
  dal: "dall'",
  al: "all'",
  del: "dell'",
  nel: "nell'",
  sul: "sull'",
};

/** ¿La cifra se lee empezando por vocal? `entera`: solo dígitos. */
function suenaAVocal(entera: string): boolean {
  if (entera.startsWith("8")) return true;
  return entera.startsWith("11") && entera.length % 3 === 2;
}

// El artículo como palabra suelta (sin letra ni apóstrofo pegados delante),
// un espacio, y la cifra con sus puntos de miles.
const RE = /(^|[^\p{L}\p{M}'’])(il|dal|al|del|nel|sul|Il|Dal|Al|Del|Nel|Sul)\s+(\d[\d.]*)/gu;

export function elidir(idioma: Locale, texto: string): string {
  if (idioma !== "it") return texto;
  return texto.replace(RE, (todo, antes: string, articulo: string, cifra: string) => {
    const entera = cifra.replace(/\./g, "");
    if (!suenaAVocal(entera)) return todo;
    const elidido = ELIDIDO[articulo.toLowerCase()];
    const conMayuscula = articulo[0] === articulo[0].toUpperCase();
    return `${antes}${conMayuscula ? elidido[0].toUpperCase() + elidido.slice(1) : elidido}${cifra}`;
  });
}

/** `interpolar` y después la elisión del idioma. Para las frases con una
 * fecha o una cifra detrás de un artículo. */
export function interpolarEn(idioma: Locale, texto: string, valores: Record<string, string | number>): string {
  return elidir(idioma, interpolar(texto, valores));
}
