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
 * Recargas de créditos (fase "Catálogo congruente", jul 2026). Congruencia
 * EXACTA: cada pack ES un paquete real de trabajo. Los créditos son FUNGIBLES
 * (una sola billetera): los packs se narran por lo que "alcanza para", JAMÁS
 * como derechos cerrados —no hay contador de bundle ni "incluye 3 seguimientos"
 * (ANÁLISIS §7). El chip de saldo + el precio en cada compuerta son el contador
 * honesto. La compra con dinero sigue DORMIDA hasta que despierten las pasarelas
 * (ETAPA 3); este catálogo alimenta la pantalla y, cuando despierten, RevenueCat.
 */
export const PACKS = [
  { nombre: "Recarga", creditos: 5, usd: 4.99, alcanza: "un seguimiento o un mundo suelto", destacado: false },
  { nombre: "Básico", creditos: 10, usd: 9.99, alcanza: "tu plan completo, con tus números incluidos", destacado: false },
  { nombre: "Premium", creditos: 15, usd: 14.99, alcanza: "tu plan y tu primer seguimiento", destacado: true },
  { nombre: "Profesional", creditos: 30, usd: 29.99, alcanza: "el viaje entero de una idea", destacado: false },
] as const;
