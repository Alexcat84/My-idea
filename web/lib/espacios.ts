/**
 * Campaña "Espacios": un proyecto = el viaje CORE + sus MUNDOS; cada uno es un
 * ESPACIO con operación propia (su plan, sus tareas, su línea de tiempo), bajo
 * un mismo techo de historia. La regla de la casa (BANCO §7.1):
 *   "lo que cuenta historia es global; lo que mide operación es del espacio."
 *
 * Estas funciones PURAS deciden qué pertenece a qué espacio: las usan la vista
 * scopeada (ManosALaObra), la navegación al hub (IdeaView) y —Fase 3— las
 * etiquetas de espacio de la bitácora/expediente. Fuente única de la regla,
 * para que la UI y los tests nunca discrepen.
 */

export const ESPACIO_CORE = "core";

/** El dominio pertenece al core si es nulo o "core"; cualquier otro es un mundo. */
export function esEspacioCore(dominio: string | null | undefined): boolean {
  return !dominio || dominio === ESPACIO_CORE;
}

/**
 * LAS DOS FAMILIAS DE MUNDOS (BANCO §7.1, campaña "Mundos de protección"). Los
 * de PROTECCIÓN se aplican SOBRE las actividades reales del núcleo: su
 * entrevista y su diagnóstico reciben el snapshot del plan vigente, y su plan
 * enlaza cada respuesta con lo que protege. Los de mejora y expansión (Calidad,
 * Internacionalización, Multiplica, Sostenibilidad) construyen su plan desde el
 * contexto del negocio, como siempre, y NO se tocan.
 *
 * Esta lista es la frontera: si un dominio no está aquí, ninguna pieza de la
 * campaña de protección lo mira.
 */
export const MUNDOS_PROTECCION = ["risk_management", "health_safety", "seguridad_digital"] as const;

export function esMundoProteccion(dominio: string | null | undefined): boolean {
  return !!dominio && (MUNDOS_PROTECCION as readonly string[]).includes(dominio);
}

/**
 * LA MURALLA DEL SIN PLAN (BANCO §7.1). Un mundo se construye sobre la idea ya
 * trabajada, y uno de protección literalmente no tiene nada sobre lo cual
 * evaluar sin el plan del núcleo. Se dice en persona y se ofrece el camino, en
 * vez de generar una plantilla: fallar honesto, jamás plantilla.
 *
 * UNA sola frase para toda la casa: la escribe la ruta cuando responde 409 y la
 * pinta la pantalla del escaparate. Si vivieran en dos sitios, algún día dirían
 * cosas distintas.
 */
export function murallaSinPlan(nombreDelMundo: string): string {
  return `Primero genera el plan de tu idea: tu mundo de ${nombreDelMundo} se construirá sobre él.`;
}

/**
 * Qué mundos se muestran en una vista scopeada a `soloDominio`:
 * - sin `soloDominio` (undefined/null) → TODOS (comportamiento histórico:
 *   los mundos apilados bajo el core en la misma vista).
 * - `"core"` → NINGUNO (los mundos viven en su propio hub, no bajo el core).
 * - un dominio de mundo → solo ESE (su hub muestra únicamente su operación).
 */
export function mundosDelEspacio<T extends { dominio: string }>(
  mundos: T[],
  soloDominio?: string | null
): T[] {
  if (!soloDominio) return mundos;
  if (soloDominio === ESPACIO_CORE) return [];
  return mundos.filter((m) => m.dominio === soloDominio);
}

/** El deep-link del espacio: el hub de un mundo, o el Manos a la Obra del core. */
export function urlDelEspacio(projectId: string, dominio: string): string {
  return esEspacioCore(dominio)
    ? `/idea/${projectId}?vista=manos`
    : `/idea/${projectId}?vista=mundo&dominio=${dominio}`;
}

/**
 * "Todo separado" (T3c, B5): qué ESPACIOS entran en el ritual de fechas/línea
 * base de un espacio dado. La respuesta es **SOLO ese espacio** — el ritual del
 * core JAMÁS arrastra los tramos de los mundos, y el de un mundo es solo suyo.
 * (Antes, el ritual del core cubría el proyecto entero: core + todos los mundos;
 * eso mezclaba medidas entre espacios. Cada espacio sella SU baseline en SU
 * ritual.) Fuente única para que la UI y el test del no-arrastre no discrepen.
 */
export function dominiosDelRitual(espacioActual: string): string[] {
  return [espacioActual];
}
