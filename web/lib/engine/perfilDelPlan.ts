/**
 * AUD-09 H05 (PREVIEW_MUNDOS_PLAN §4): el estado vivo ACTUAL del proyecto, leído en el momento del plan. En la compra
 * de un mundo el perfil de la sesión se congeló en el preview; si el proyecto cambió de ciclo desde entonces, el
 * redactor debe ver la realidad de hoy. Una sola función para la ruta del plan y para el guion de medición (decisión
 * del fundador, 9 oct 2026: la medición usa el camino de producción).
 */
export function perfilConEstadoVivoActual(
  perfil: string,
  o: { dominio: string; esSeguimiento: boolean; estadoVivoActual: string | null }
): string {
  if (o.dominio === "core" || o.esSeguimiento || !o.estadoVivoActual || perfil.includes(o.estadoVivoActual)) return perfil;
  return `${perfil}
Estado actual del proyecto, más reciente que la exploración: ${o.estadoVivoActual}`.trim();
}
