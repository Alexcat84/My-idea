/**
 * El rango en palabras de una banda de esfuerzo, para el detalle de la tarea. Modulo PURO a proposito: lo importa
 * un componente de cliente (DetalleActividad), y estimacion.ts, donde nacio, arrastra las instrucciones de la IA
 * (prompts.json), que jamas llegan al navegador (NADA INTERNO LLEGA AL NAVEGADOR, fundador, 27 sep 2026;
 * guarda: lib/procedencia.test.ts).
 */
import type { Banda } from "../dbContract";
import { elegir, LOCALE_BASE, type Locale } from "../i18n/config";
import { MOTOR } from "../i18n/mensajes/motor";

/** Rango honesto en palabras para una banda (para el detalle de la tarea). Son
 * las MISMAS fronteras del prompt validado; JAMÁS un número de horas inventado. */
export function rangoDeBanda(banda: Banda | null | undefined, idioma: Locale = LOCALE_BASE): string | null {
  const t = elegir(MOTOR, idioma).rangoBanda;
  switch (banda) {
    case "S":
      return t.S;
    case "M":
      return t.M;
    case "L":
      return t.L;
    case "XL":
      return t.XL;
    default:
      return null; // plan viejo o estimación fallida: sin rango, cero invención
  }
}
