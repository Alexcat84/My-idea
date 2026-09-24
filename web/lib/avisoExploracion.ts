/**
 * AUD-09 M32: el aviso de precio bajo "Explorar estas suposiciones" (canon 03).
 * Una sola fuente para /nueva y la idea; la cifra sale de precios.ts y la frase
 * dice cuándo se cobra (a la entrega del plan, y solo si se entrega:
 * ANALISIS_PRECIOS §4).
 */
import { PRECIOS } from "./precios";

export const AVISO_PRECIO_EXPLORACION = `La Exploración usa ${PRECIOS.plan_completo} créditos, que se cobran solo cuando recibes tu plan. Tu Claridad es gratis y queda guardada para siempre.`;
