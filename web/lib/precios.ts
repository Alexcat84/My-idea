// Canon comercial (beta). 1 crédito = $1 USD; pack $10 = 10 créditos.
// Los precios viven AQUÍ y en packs_catalog.json (mundos); ninguna ruta
// hardcodea números. Pagos reales (Stripe) llegan en fase posterior: por
// ahora los endpoints validan contra estas constantes con créditos stub.
// Valores actualizados por el fundador (2026-07-10) sobre el patch
// original: seguimiento 3->2, mundo_activar 4->3.
export const PRECIOS = {
  organizador: 0, // el gancho freemium: siempre gratis
  plan_completo: 5, // La Exploración + Tu Plan
  seguimiento: 2, // más barato que el plan: el bucle es la retención
  tus_numeros: 2, // reporte de sostenibilidad (regeneraciones incluidas)
  mundo_activar: 3, // brecha + exploración del dominio + plan del mundo
  mundo_seguimiento: 2, // ciclo de seguimiento dentro de un mundo
} as const;

export type ConceptoPrecio = keyof typeof PRECIOS;
