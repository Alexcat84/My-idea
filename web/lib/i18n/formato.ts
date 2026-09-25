/**
 * Números y dinero por idioma, con Intl (DISENO §3.4 y D6: formato por idioma,
 * símbolo "$" por ahora; la moneda por proyecto es función futura).
 *
 * REGLA DE F2: en español el resultado es IDÉNTICO al de hoy. Hoy la app agrupa
 * los miles con punto siempre ("$1.200", también con cuatro cifras, que el
 * español de Intl no agrupa por omisión: de ahí `useGrouping: "always"`) y
 * escribe los decimales con punto y sin agrupar ("12.5", como `toFixed(1)`).
 * F3 revisa estos formatos idioma por idioma.
 */
import type { Locale } from "./config";

// `useGrouping: "always"` es ES2023; el tipo de TS de esta versión aún no lo lista.
type OpcionesNumero = Omit<Intl.NumberFormatOptions, "useGrouping"> & { useGrouping?: boolean | "always" | "auto" | "min2" };
const formateador = (etiqueta: string, opciones: OpcionesNumero) =>
  new Intl.NumberFormat(etiqueta, opciones as Intl.NumberFormatOptions);

const ENTERO: Record<string, Intl.NumberFormat> = {};
function formatoEntero(idioma: Locale): Intl.NumberFormat {
  return (ENTERO[idioma] ??= formateador(idioma, { maximumFractionDigits: 0, useGrouping: "always" }));
}

/** Un entero con los miles agrupados: "1.200" en español. Redondea. */
export function entero(idioma: Locale, n: number): string {
  const cifra = formatoEntero(idioma).format(Math.round(Math.abs(n)));
  return (n < 0 && cifra !== "0" ? "-" : "") + cifra;
}

/** Dinero entero con el símbolo delante: "$1.200", "-$1.200" (el signo antes del símbolo, como hoy). */
export function dinero(idioma: Locale, n: number): string {
  const cifra = formatoEntero(idioma).format(Math.round(Math.abs(n)));
  return (n < 0 ? "-$" : "$") + cifra;
}

/** Un decimal con `digitos` cifras tras el separador, sin agrupar: "12.5" en español.
 * En español es EXACTAMENTE toFixed (Intl redondea distinto algunos casos borde:
 * 1.45 da "1.5" con Intl y "1.4" con toFixed); los demás idiomas usan Intl. */
export function decimal(idioma: Locale, n: number, digitos = 1): string {
  if (idioma === "es") return n.toFixed(digitos);
  return formateador(idioma, { minimumFractionDigits: digitos, maximumFractionDigits: digitos, useGrouping: false }).format(n);
}
