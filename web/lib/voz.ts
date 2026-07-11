/**
 * voz.ts — Phase 3.7 (regla A): la casa no escribe con guiones largos ni
 * medios. Los prompts ya lo prohíben; este filtro mecánico es la garantía
 * post-salida (los modelos reinciden). Se aplica en el punto único por el
 * que pasa todo texto del modelo (costmeter.llamarClaude*), así que
 * preguntas, planes, reportes y organizador quedan cubiertos sin que cada
 * llamador tenga que acordarse.
 *
 * Reglas de reemplazo (deterministas, sin LLM):
 * 1. Guion de viñeta al inicio de línea → viñeta con guion corto.
 * 2. Rango numérico 3–5 → 3-5.
 * 3. Inciso entre pares de guiones → entre comas.
 * 4. Guion suelto → coma.
 * 5. Limpieza de dobles comas/espacios que dejen los reemplazos.
 */
export function limpiarGuiones(texto: string): string {
  if (!/[—–]/.test(texto)) return texto;
  return (
    texto
      // viñeta markdown con guion largo al inicio de línea
      .replace(/^[ \t]*[—–][ \t]*/gm, "- ")
      // rangos numéricos: 3–5 → 3-5
      .replace(/(\d)\s*[—–]\s*(\d)/g, "$1-$2")
      // inciso entre guiones dentro de una línea: a —b— c → a, b, c
      .replace(/[ \t]*[—–][ \t]*([^—–\n]*?)[ \t]*[—–][ \t]*/g, ", $1, ")
      // guion suelto restante → coma
      .replace(/[ \t]*[—–][ \t]*/g, ", ")
      // artefactos: coma huérfana antes de puntuación, dobles comas/espacios
      .replace(/,\s*([,.;:!?)])/g, "$1")
      .replace(/\(\s*,\s*/g, "(")
      .replace(/([ \t]){2,}/g, "$1")
  );
}
