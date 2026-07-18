/**
 * previewMundos.ts - Fase 4.5 (docs/PREVIEW_MUNDOS_PLAN.md): la logica PURA
 * del preview de los mundos. Tres piezas, cero LLM, cero DB:
 *
 * 1. La MAQUINA DE ESTADOS (§4): bloqueado / abierto / diagnostico_listo /
 *    plan_comprado, derivada de la fila del unlock + si hay plan core.
 * 2. El derecho a RE-PREVIEW: un preview por mundo por proyecto; re-correrlo
 *    requiere compra o ciclo nuevo (un plan core mas nuevo que el resumen:
 *    realidad nueva amerita mirada nueva).
 * 3. La FRONTERA (§3) como guardia determinista: el preview es diagnostico,
 *    jamas plan encubierto. Esta guardia no redacta (eso es del prompt); caza
 *    violaciones gruesas para el vuelo y los tests.
 */

export type EstadoMundo = "bloqueado" | "abierto" | "diagnostico_listo" | "plan_comprado";

/** Lo que la maquina necesita de la fila de project_unlocks (null = sin fila). */
export interface UnlockPreview {
  preview_at?: string | null;
  resumen_md?: string | null;
  resumen_at?: string | null;
  plan_pagado_at?: string | null;
}

/**
 * La maquina de estados del §4. La fila del unlock es la presencia del mundo
 * en la idea; sin plan core todo esta bloqueado (candado de secuencia, §2.4).
 * Un unlock del modelo viejo (fila sin preview ni plan pagado, pre-028 sin
 * backfill aplicable) cuenta como "abierto": puede entrar a explorar gratis.
 */
export function estadoMundo(unlock: UnlockPreview | null | undefined, hayPlanCore: boolean): EstadoMundo {
  if (!hayPlanCore) return "bloqueado";
  if (!unlock) return "abierto";
  if (unlock.plan_pagado_at) return "plan_comprado";
  if (unlock.resumen_md && unlock.resumen_at) return "diagnostico_listo";
  return "abierto";
}

/**
 * ¿Puede re-correr el preview? Un preview por mundo por proyecto. Se re-abre
 * solo si el proyecto cambio de ciclo DESPUES del resumen: hay un plan core
 * mas nuevo que resumen_at (la compra es el otro camino y no pasa por aqui).
 * Sin resumen todavia, el preview esta disponible (o en curso).
 */
export function puedeRePreview(unlock: UnlockPreview | null | undefined, planCoreMasNuevoAt: string | null): boolean {
  if (!unlock?.resumen_at) return true;
  if (!planCoreMasNuevoAt) return false;
  return new Date(planCoreMasNuevoAt).getTime() > new Date(unlock.resumen_at).getTime();
}

/**
 * La frontera del §3, como detector determinista de violaciones GRUESAS.
 * Prohibido en el resumen del preview: pasos accionables, "Esta semana",
 * secuencias de ejecucion, entregables por etapa. Devuelve la lista de
 * violaciones encontradas ([] = limpio). Conservador a proposito: la voz y el
 * matiz los gobierna el prompt; esto es la red del vuelo, no el redactor.
 */
export function violacionesFronteraPreview(md: string): string[] {
  const violaciones: string[] = [];
  const texto = md.toLowerCase();

  if (/esta semana/.test(texto)) violaciones.push('"esta semana" (accion calendarizada)');
  if (/entregable/.test(texto)) violaciones.push('"entregable" (estructura de plan)');
  if (/^#+\s*etapa\b/im.test(md) || /\betapa\s+\d/.test(texto)) violaciones.push("etapas numeradas (secuencia de ejecucion)");
  if (/^\s*(paso|dia|semana)\s+\d+\s*[:.]/im.test(md)) violaciones.push("pasos/dias numerados (secuencia de ejecucion)");
  // Tres o mas items de lista NUMERADA consecutivos = una secuencia de
  // ejecucion disfrazada (los bullets tematicos "- tema" son legitimos).
  const numerados = md.match(/^\s*\d+[.)]\s+/gm);
  if (numerados && numerados.length >= 3) violaciones.push(`${numerados.length} items numerados (lista de ejecucion)`);

  return violaciones;
}
