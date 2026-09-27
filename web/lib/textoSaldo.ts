/**
 * AUD-09 M31 (decisión del fundador, 25 sep 2026): el texto del saldo que se
 * puede gastar. Una sola fuente para el chip del encabezado (cliente) y la
 * barra de /creditos (servidor). Pura.
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { plural } from "./i18n/interpolar";
import { SALDO } from "./i18n/mensajes/saldo";

export function textoChipSaldo(
  disponible: number,
  reservados: number,
  idioma: Locale = LOCALE_BASE
): { principal: string; reservados: string | null } {
  const t = elegir(SALDO, idioma);
  return {
    principal: plural(idioma, disponible, t.creditos),
    reservados: reservados > 0 ? plural(idioma, reservados, t.reservados) : null,
  };
}
