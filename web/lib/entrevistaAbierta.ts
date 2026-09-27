/**
 * AUD-09 M29: la ÚNICA regla de "entrevista abierta", para /ideas y para la
 * idea. Una sesión sin cerrar con recorrido persistido está abierta, salvo la
 * de fase 'cerrada' (un diagnóstico de mundo esperando compra: su cara es el
 * escaparate, no una pregunta). Dice también QUÉ espera: una pregunta, o el
 * plan listo para armarse.
 */
export function estadoEntrevista(s: {
  closed_at: string | null;
  estado_recorrido: unknown;
}): "pregunta" | "listo_para_plan" | null {
  if (s.closed_at || !s.estado_recorrido) return null;
  const recorrido = (s.estado_recorrido as { recorrido?: { fase?: string; ciclo?: { tipo?: string } } }).recorrido;
  const fase = recorrido?.fase;
  if (fase === "cerrada") return null;
  // Ciclo de replanteamiento, Fase 2: "Replantear mi camino" no tiene
  // entrevista. Su sesión espera el camino elegido en el ritual, no una pregunta.
  if (recorrido?.ciclo?.tipo === "replantear") return null;
  return fase === "listo_para_plan" ? "listo_para_plan" : "pregunta";
}
