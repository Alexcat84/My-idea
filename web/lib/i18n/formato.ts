/**
 * Números y dinero por idioma, con Intl (DISENO §3.4 y D6: formato por idioma,
 * símbolo "$" por ahora; la moneda por proyecto es función futura).
 *
 * REGLA DE F2: en español el resultado es IDÉNTICO al de hoy. Hoy la app agrupa
 * los miles con punto siempre ("$1.200", también con cuatro cifras, que el
 * español de Intl no agrupa por omisión: de ahí `useGrouping: "always"`) y
 * escribe los decimales con punto y sin agrupar ("12.5", como `toFixed(1)`).
 *
 * F3: los demás idiomas siguen su regla de Intl (CLDR): separadores, posición
 * del "$" y agrupación (la india en hindi). Todos con cifras latinas
 * (`numberingSystem: "latn"`): el servidor y el navegador deben escribir lo
 * mismo, y las cifras por omisión del árabe cambian según la versión de ICU.
 */
import type { Locale } from "./config";

// `useGrouping: "always"` es ES2023; el tipo de TS de esta versión aún no lo lista.
// Igual `signDisplay: "negative"` (sin "-0").
type OpcionesNumero = Omit<Intl.NumberFormatOptions, "useGrouping" | "signDisplay"> & {
  useGrouping?: boolean | "always" | "auto" | "min2";
  signDisplay?: Intl.NumberFormatOptions["signDisplay"] | "negative";
};
const formateador = (etiqueta: string, opciones: OpcionesNumero) =>
  new Intl.NumberFormat(etiqueta, opciones as Intl.NumberFormatOptions);

const ENTERO: Record<string, Intl.NumberFormat> = {};
function formatoEntero(idioma: Locale): Intl.NumberFormat {
  return (ENTERO[idioma] ??= formateador(idioma, { maximumFractionDigits: 0, useGrouping: "always", numberingSystem: "latn" }));
}

// El dinero fuera del español: la plantilla de moneda de cada idioma, con el
// símbolo "$" en lugar del de la moneda (D6) y sin "-0".
const DINERO: Record<string, Intl.NumberFormat> = {};
function formatoDinero(idioma: Locale): Intl.NumberFormat {
  return (DINERO[idioma] ??= formateador(idioma, {
    style: "currency",
    currency: "USD",
    currencyDisplay: "narrowSymbol",
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
    useGrouping: "always",
    numberingSystem: "latn",
    signDisplay: "negative",
  }));
}

/** Un entero con los miles agrupados: "1.200" en español. Redondea. */
export function entero(idioma: Locale, n: number): string {
  const cifra = formatoEntero(idioma).format(Math.round(Math.abs(n)));
  return (n < 0 && cifra !== "0" ? "-" : "") + cifra;
}

/** Dinero entero con el símbolo delante: "$1.200", "-$1.200" (el signo antes del símbolo, como hoy). */
export function dinero(idioma: Locale, n: number): string {
  if (idioma === "es") return (n < 0 ? "-$" : "$") + formatoEntero(idioma).format(Math.round(Math.abs(n)));
  // Se redondea como en español (el valor absoluto), y el signo lo pone Intl.
  const redondo = Math.sign(n) * Math.round(Math.abs(n));
  return formatoDinero(idioma)
    .formatToParts(redondo)
    .map((p) => (p.type === "currency" ? "$" : p.value))
    .join("");
}

/** Un decimal con `digitos` cifras tras el separador, sin agrupar: "12.5" en español.
 * En español es EXACTAMENTE toFixed (Intl redondea distinto algunos casos borde:
 * 1.45 da "1.5" con Intl y "1.4" con toFixed); los demás idiomas usan Intl. */
export function decimal(idioma: Locale, n: number, digitos = 1): string {
  if (idioma === "es") return n.toFixed(digitos);
  return formateador(idioma, { minimumFractionDigits: digitos, maximumFractionDigits: digitos, useGrouping: false, numberingSystem: "latn" }).format(n);
}
