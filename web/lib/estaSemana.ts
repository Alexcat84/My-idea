/**
 * estaSemana.ts: "Esta semana", CALCULADO POR LA APP (decisión del fundador,
 * 26 sep 2026).
 *
 * El plan repetía "Esta semana" en cada etapa, y eso prometía tiempos
 * imposibles: las etapas son secuenciales, la 3 no puede ser "esta semana" a la
 * vez que la 1. Ahora cada etapa trae su "Primera acción" (sin fecha) y
 * "Esta semana" aparece UNA sola vez, en Manos a la Obra, calculado aquí:
 *
 *  - La ETAPA ACTIVA es la primera con algo sin terminar (hecho y no aplica
 *    terminan; en proceso, apenas empezada y sin empezar no).
 *  - Su PRIMERA ACCIÓN: la del plan para esa etapa (el marcador nuevo o, en los
 *    planes viejos, su "Esta semana"), que es la tarea destacada; si esa ya está
 *    terminada, la primera pendiente de la etapa.
 *  - Con fechas: lo que CABE en las horas por semana del espacio, con las mismas
 *    horas del empaquetado (HORAS_MEDIA por banda, el piso de la capacidad). Se
 *    llena en el orden del plan y se corta en la primera que no cabe, igual que
 *    el empaquetado reparte semanas. Jamás entra una tarea de una etapa
 *    posterior mientras la activa tenga pendientes.
 *  - A mi ritmo (o sin modo elegido): "Tu siguiente paso", sin plazo: la etapa
 *    activa, su primera acción y la tarea que sigue. A quien eligió su ritmo no
 *    se le habla de calendario (BANCO §3).
 *
 * PURO: sin React, sin red, sin reloj.
 */
import type { Banda, CapacidadSemanal, ChecklistEstado, ModoCamino } from "./dbContract";
import { CAPACIDAD_DEFAULT, HORAS_MEDIA, HORAS_POR_SEMANA } from "./empaquetado";
import { RE_PRIMERA_ACCION } from "./engine/checklist";

/** Lo mínimo de una tarea del checklist que este cálculo necesita. */
export interface ItemSemana {
  id: string;
  etapa: number;
  orden: number;
  texto: string;
  destacado: boolean;
  estado: ChecklistEstado;
  banda: Banda | null;
}

export interface BloqueEstaSemana<T extends ItemSemana = ItemSemana> {
  /** "semana" con fechas; "ritmo" a mi ritmo o sin modo elegido. */
  modo: "semana" | "ritmo";
  etapa: number;
  /** itemId null solo si el texto vino del plan sin una tarea que lo respalde. */
  primeraAccion: { texto: string; itemId: string | null };
  /** Con fechas: las pendientes de la etapa activa que caben después de la primera acción. */
  tambienCaben: T[];
  /** A mi ritmo: la tarea que sigue a la primera acción (o null). */
  siguiente: T | null;
  /** Con fechas: las horas con las que se planifica la semana. A mi ritmo, null. */
  horasSemana: number | null;
}

const terminada = (estado: ChecklistEstado) => estado === "hecho" || estado === "no_aplica";

/** Etapa → texto de su primera acción, tal como lo escribió el plan. Lee el
 * marcador nuevo ("**Primera acción:**") y el viejo ("**Esta semana:**") como el
 * mismo campo. Fuera de una "## Etapa N:" no cuenta (la sección de números). */
export function primerasAccionesDelPlan(md: string): Record<number, string> {
  const out: Record<number, string> = {};
  let etapa = 0;
  for (const cruda of md.split(/\r?\n/)) {
    const linea = cruda.trim();
    const me = /^##\s+Etapa\s+(\d+)\s*:/.exec(linea);
    if (me) {
      etapa = parseInt(me[1], 10);
      continue;
    }
    if (linea.startsWith("## ")) {
      etapa = 0;
      continue;
    }
    if (etapa === 0 || out[etapa] !== undefined) continue;
    const m = RE_PRIMERA_ACCION.exec(linea);
    if (m && m[1].trim()) out[etapa] = m[1].trim();
  }
  return out;
}

export function calcularEstaSemana<T extends ItemSemana>(opts: {
  items: T[];
  modo: ModoCamino | null;
  capacidad: CapacidadSemanal | null;
  /** primerasAccionesDelPlan(planMd): el texto completo del plan por etapa. */
  primerasAcciones?: Record<number, string>;
}): BloqueEstaSemana<T> | null {
  const abiertas = opts.items.filter((i) => !terminada(i.estado));
  if (abiertas.length === 0) return null;
  const etapa = Math.min(...abiertas.map((i) => i.etapa));
  const deLaEtapa = opts.items.filter((i) => i.etapa === etapa);
  // Orden del arranque, el mismo del empaquetado: la destacada primero, luego el plan.
  const pendientes = abiertas
    .filter((i) => i.etapa === etapa)
    .sort((a, b) => Number(b.destacado) - Number(a.destacado) || a.orden - b.orden);

  const destacada = deLaEtapa.find((i) => i.destacado) ?? null;
  const destacadaHecha = destacada !== null && terminada(destacada.estado);
  const primera = destacadaHecha ? pendientes[0] : (destacada ?? pendientes[0]);
  const textoPlan = destacadaHecha ? undefined : opts.primerasAcciones?.[etapa];
  const primeraAccion = { texto: textoPlan ?? primera.texto, itemId: primera.id };
  const resto = pendientes.filter((i) => i.id !== primera.id);

  if (opts.modo !== "fechas") {
    return { modo: "ritmo", etapa, primeraAccion, tambienCaben: [], siguiente: resto[0] ?? null, horasSemana: null };
  }

  const horasSemana = HORAS_POR_SEMANA[opts.capacidad ?? CAPACIDAD_DEFAULT];
  const tambienCaben: T[] = [];
  // Sin banda no hay horas que sumar: la lista se corta ahí (cero invención).
  if (primera.banda) {
    let acumulado = HORAS_MEDIA[primera.banda];
    for (const it of resto) {
      if (!it.banda) break;
      acumulado += HORAS_MEDIA[it.banda];
      if (acumulado > horasSemana) break;
      tambienCaben.push(it);
    }
  }
  return { modo: "semana", etapa, primeraAccion, tambienCaben, siguiente: null, horasSemana };
}
