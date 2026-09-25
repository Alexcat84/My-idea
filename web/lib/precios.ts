// Canon comercial — fase "Catálogo congruente" (ANÁLISIS_PRECIOS §4, jul 2026).
// El catálogo del §4 es LEY. Decisión del fundador: subir los unitarios a
// múltiplos de 5 para que packs y paquetes reales sean EL MISMO número
// (congruencia exacta: 10+5+5+5+5 = 30), y una regla narrable en una línea:
//   "Tu plan: 10 créditos. Todo lo demás: 5. La Claridad y los diagnósticos:
//    gratis."
// Los precios viven AQUÍ y SOLO aquí; ninguna ruta
// hardcodea números. 1 crédito = 1 USD sigue siendo el ancla del ledger, pero
// NO se le vende al usuario como eslogan. Pagos reales (pasarelas) llegan en la
// ETAPA 3: por ahora los endpoints validan contra estas constantes.
//
// Cuándo se cobra (decisión del fundador, 25 sep 2026): se verifica el saldo
// al empezar y se cobra al final, SOLO si se entregó lo prometido. Un plan
// armado sin IA no se cobra: se entrega gratis con un aviso honesto
// (docs/ANALISIS_PRECIOS.md §4, "Cuándo se cobra: solo lo entregado").
import { elegir, LOCALE_BASE } from "./i18n/config";
import { PACKS_RECARGA } from "./i18n/mensajes/packsRecarga";

export const PRECIOS = {
  organizador: 0, // Claridad: el gancho freemium, siempre gratis y sin cuenta
  plan_completo: 10, // Tu Plan (La Exploración) e INCLUYE Tus Números (ver tus_numeros: 0 y §7.1)
  seguimiento: 5, // ciclo de seguimiento del viaje principal
  tus_numeros: 0, // INCLUIDO en el plan (decisión jul 2026, ANÁLISIS §4/§7.1): la activación sigue anclada por activado_at, sin cobro
  mundo_activar: 5, // brecha + plan del dominio; el preview (entrevista + diagnóstico) sigue gratis
  mundo_seguimiento: 5, // ciclo de seguimiento dentro de un mundo
} as const;

export type ConceptoPrecio = keyof typeof PRECIOS;

/**
 * La regla de concepto del plan (CUENTAS_DISENO §5, actualizada por la 4.5):
 *   core + inicial/completo  → plan_completo
 *   core + seguimiento       → seguimiento
 *   mundo + inicial/completo → mundo_activar  ← el preview fue GRATIS;
 *                              lo que se compra es el PLAN, a la entrega.
 *   mundo + seguimiento      → mundo_seguimiento
 * Vive aquí, junto a los precios, porque es PURA y la usan los dos lados: el
 * cobro del servidor y el precio que pinta la pantalla (AUD-09 H01: la
 * pantalla tecleaba plan_completo y anunciaba 10 donde se cobraban 5).
 */
export function conceptoDelPlan(dominio: string, esSeguimiento: boolean): ConceptoPrecio {
  if (dominio === "core") return esSeguimiento ? "seguimiento" : "plan_completo";
  return esSeguimiento ? "mundo_seguimiento" : "mundo_activar";
}

export function montoDelPlan(dominio: string, esSeguimiento: boolean): number {
  return PRECIOS[conceptoDelPlan(dominio, esSeguimiento)];
}

/**
 * Recargas de créditos (fase "Catálogo congruente", jul 2026). Congruencia
 * EXACTA: cada pack ES un paquete real de trabajo. Los créditos son FUNGIBLES
 * (una sola billetera): los packs se narran por lo que "alcanza para", JAMÁS
 * como derechos cerrados —no hay contador de bundle ni "incluye 3 seguimientos"
 * (ANÁLISIS §7). El chip de saldo + el precio en cada compuerta son el contador
 * honesto. La compra con dinero sigue DORMIDA hasta que despierten las pasarelas
 * (ETAPA 3); este catálogo alimenta la pantalla y, cuando despierten, RevenueCat.
 *
 * i18n F2: el nombre y el "alcanza para" son texto visible y nacen en el
 * catálogo (lib/i18n/mensajes/packsRecarga.ts, por `clave`); aquí quedan en
 * el idioma base para quien los lea directo. Las cifras NO salen de aquí.
 */
const TEXTO_PACKS = elegir(PACKS_RECARGA, LOCALE_BASE);
export const PACKS = [
  { clave: "recarga", nombre: TEXTO_PACKS.recarga.nombre, creditos: 5, usd: 4.99, alcanza: TEXTO_PACKS.recarga.alcanza, destacado: false },
  { clave: "basico", nombre: TEXTO_PACKS.basico.nombre, creditos: 10, usd: 9.99, alcanza: TEXTO_PACKS.basico.alcanza, destacado: false },
  { clave: "premium", nombre: TEXTO_PACKS.premium.nombre, creditos: 15, usd: 14.99, alcanza: TEXTO_PACKS.premium.alcanza, destacado: true },
  { clave: "profesional", nombre: TEXTO_PACKS.profesional.nombre, creditos: 30, usd: 29.99, alcanza: TEXTO_PACKS.profesional.alcanza, destacado: false },
] as const;
