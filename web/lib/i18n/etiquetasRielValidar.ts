/**
 * La vara de una etiqueta del riel derivada (D3, i18n F5). La usan la
 * herramienta que las aplica (scripts/i18n/etiquetasRiel.ts) y el auditor
 * (etiquetasRiel.test.ts). Devuelve el problema, o null si está bien.
 *
 * Una etiqueta enamora (AGENTS.md): corta, en segunda persona, sin jerga. Aquí
 * solo se mide lo que se puede medir sin leerla: que exista, que sea corta y
 * que respete la voz (sin rayas, sin los signos de apertura del español).
 */

/** Largo máximo en caracteres. Las del español llegan a ~50; las escrituras
 * de CJK son mucho más cortas; el alemán y el hindi, algo más largas. */
export const LARGO_MAXIMO_ETIQUETA = 70;

export function validarEtiquetaRiel(valor: unknown): string | null {
  if (typeof valor !== "string" || !valor.trim()) return "vacía";
  const v = valor.trim();
  if ([...v].length > LARGO_MAXIMO_ETIQUETA) return `más de ${LARGO_MAXIMO_ETIQUETA} caracteres`;
  if (/[—–]/.test(v)) return "lleva rayas (la voz las prohíbe)";
  if (/[¿¡]/.test(v)) return "lleva ¿ o ¡ (son del español)";
  if (/\{\{|\}\}|[<>]/.test(v)) return "lleva marcas de plantilla";
  if (/\n/.test(v)) return "tiene saltos de línea";
  return null;
}
