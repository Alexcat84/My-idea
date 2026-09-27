/**
 * AUD-09 M32: el aviso de precio bajo "Explorar estas suposiciones" (canon 03).
 * Una sola fuente para /nueva y la idea; la cifra sale de precios.ts y la frase
 * dice cuándo se cobra (a la entrega del plan, y solo si se entrega:
 * ANALISIS_PRECIOS §4). i18n F2: la frase vive en el catálogo de la Claridad.
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolar } from "./i18n/interpolar";
import { CLARIDAD } from "./i18n/mensajes/claridad";
import { PRECIOS } from "./precios";

/** El aviso en el idioma pedido (las pantallas pasan el suyo). */
export function avisoPrecioExploracion(idioma: Locale = LOCALE_BASE): string {
  return interpolar(elegir(CLARIDAD, idioma).avisoPrecioExploracion, { n: PRECIOS.plan_completo });
}

/** El valor base (español), para quien lo importa como constante. */
export const AVISO_PRECIO_EXPLORACION = avisoPrecioExploracion(LOCALE_BASE);
