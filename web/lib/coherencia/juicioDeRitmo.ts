/**
 * CONTROL DEL MODO "A MI RITMO" (FLUJO_TRACKING §3; decision del fundador, corrida final, 8 oct 2026).
 *
 * En "a mi ritmo" la persona no tiene fechas, asi que ningun texto puede juzgar SU puntualidad frente a SU plan
 * ("vas atrasado", "no llegaste a tiempo", "vas por delante"). "A tiempo", "atrasos" o "retrasos" como consejo de
 * negocio (entregar a tiempo a los clientes, pagar a tiempo, el riesgo de atrasos del proveedor) estan permitidos.
 *
 * Antes el vuelo buscaba las expresiones sueltas ("a tiempo", "tardia"...) y paro el 8 oct por "detectar el defecto a
 * tiempo". Este control caza el JUICIO: la persona (segunda persona) puesta contra su propio avance, sus tareas o sus
 * fechas. Devuelve los fragmentos que lo hacen; vacio si no hay ninguno.
 */
const sinAcentos = (s: string) => s.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();

const JUICIOS: RegExp[] = [
  // la persona va atrasada o adelantada: "vas atrasado", "estas adelantada", "vas por delante", "sigues al dia"
  /\b(?:vas|ibas|estas|estabas|andas|sigues|quedaste|quedas|vienes|llevas|te quedaste)\s+(?:muy\s+|un poco\s+|algo\s+|bastante\s+)?(?:atrasad[oa]s?|retrasad[oa]s?|adelantad[oa]s?|por delante|por detras|con retraso|con atraso|al dia)\b/gu,
  // la persona hizo o va tarde / a tiempo: "no llegaste a tiempo", "terminaste tarde", "cumpliste a tiempo", "vas tarde"
  /\b(?:vas|ibas|andas|vienes|llegaste|terminaste|acabaste|completaste|cumpliste|hiciste)\b[^.;:\n]{0,25}?\b(?:tarde|a tiempo|fuera de plazo|antes de tiempo|antes de lo previsto|despues de la fecha)\b/gu,
  // sus tareas puestas contra el plan: "tus tareas atrasadas", "acciones vencidas"
  /\b(?:tareas|acciones|actividades|pasos|etapas?)\s+(?:atrasad|retrasad|tardi|adelantad|vencid)\w*/gu,
  // una tarea calificada como tardia o adelantada: "quedo tardia", "salieron adelantadas"
  /\b(?:quedo|quedaron|salio|salieron|fue|fueron|resulto|resultaron|marcadas? como)\s+(?:tardi|adelantad)\w*/gu,
  // la cuenta del atraso de la persona: "llevas cinco dias de retraso"
  /\b(?:llevas|acumulas|acumulaste|tienes|tuviste|vas con)\s+(?:\w+\s+)?(?:dias|semanas)\s+(?:de\s+)?(?:retraso|atraso|adelanto)\b/gu,
  // su puntualidad como tema: "tu puntualidad", "tu cumplimiento", "tus atrasos"
  /\btus?\s+(?:puntualidad|cumplimiento|retraso|retrasos|atraso|atrasos|adelanto)\b/gu,
  // la desviacion contra sus fechas o su plan
  /\bdesviacion\b[^.;:\n]{0,30}\b(?:fechas?|plan|calendario|plazos?)\b/gu,
];

export function juiciosDeRitmo(texto: string): string[] {
  const t = sinAcentos(texto);
  const hallados: string[] = [];
  for (const re of JUICIOS) for (const m of t.matchAll(re)) hallados.push(m[0]);
  return hallados;
}
