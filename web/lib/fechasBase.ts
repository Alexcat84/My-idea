/**
 * fechasBase.ts — Fase 3.8 §4: el sugeridor determinístico de la línea
 * base. CERO LLM, corre al abrir el ritual (canon 10, vista B). Reglas:
 *
 *  - Ítems de la etapa N  → plan.created_at + N semanas, "fin de semana
 *    laboral" (viernes) de esa semana ISO. Sin hora.
 *  - Ítems "Esta semana" (destacado) de la etapa N → "inicio de su semana"
 *    (lunes) de esa misma semana.
 *  - Si hay completed_at previos con un patrón de día (el usuario suele
 *    cerrar los sábados), las sugerencias del ciclo siguiente respetan ese
 *    día para los ítems regulares.
 *
 * Devuelve fechas de CALENDARIO ("YYYY-MM-DD" local): sin hora y sin
 * corrimiento de zona horaria. La persistencia (ISO mediodía local) la hace
 * isoDesdeInputLocal(); la lectura humana, fechaHumana().
 */
import { esEstaSemana, fechaInputLocal } from "./fechas";

const VIERNES = 5; // fin de la semana laboral
const LUNES = 1; // inicio de la semana

/** La fecha del `weekday` (0=Dom..6=Sáb) dentro de la semana ISO (lun..dom)
 * que cae `semanas` después de `base`. Todo en componentes locales. */
function objetivoEnSemana(base: Date, semanas: number, weekday: number): Date {
  const anchor = new Date(base.getFullYear(), base.getMonth(), base.getDate() + semanas * 7, 12);
  const desdeLunes = (anchor.getDay() + 6) % 7; // días transcurridos desde el lunes
  const lunes = new Date(anchor.getFullYear(), anchor.getMonth(), anchor.getDate() - desdeLunes, 12);
  const offset = (weekday + 6) % 7; // días desde el lunes hasta `weekday`
  return new Date(lunes.getFullYear(), lunes.getMonth(), lunes.getDate() + offset, 12);
}

/** El día de la semana (0=Dom..6=Sáb) en que el usuario suele cerrar,
 * según sus completed_at previos. null si no hay ninguno. Empates: gana el
 * más temprano de la semana (índice menor). */
export function diaDominante(completedAts: Array<string | null | undefined>): number | null {
  const cuenta = new Array(7).fill(0);
  let hay = false;
  for (const c of completedAts) {
    if (!c) continue;
    const d = new Date(c);
    if (Number.isNaN(d.getTime())) continue;
    cuenta[d.getDay()] += 1;
    hay = true;
  }
  if (!hay) return null;
  let mejor = 0;
  for (let i = 1; i < 7; i += 1) if (cuenta[i] > cuenta[mejor]) mejor = i;
  return mejor;
}

export interface ItemSugerible {
  id: string;
  etapa: number;
  destacado: boolean;
}

export interface FechaSugerida {
  id: string;
  /** "YYYY-MM-DD" local, lista para un <input type="date"> */
  fecha: string;
}

/**
 * Fase 4.0 §1[8]: la cadencia REAL del ciclo previo, en semanas por etapa.
 * Entra la `duracionPorEtapa` que ya calculó analytics.ts (aquí NO se recalcula
 * nada: §6). Si el usuario tardó de verdad tres semanas por etapa, el ciclo
 * nuevo deja de prometerle una: promete tres. Sin datos → 1 (el default de
 * siempre). Se acota a [1, 6] para que una etapa rara (o un dato sucio) no
 * dispare fechas absurdas a un año vista.
 */
export function cadenciaRealSemanas(duracionPorEtapa: Array<{ etapa: number; dias: number }>): number {
  const dias = duracionPorEtapa.map((e) => e.dias).filter((d) => d > 0);
  if (dias.length === 0) return 1;
  const media = dias.reduce((a, b) => a + b, 0) / dias.length;
  return Math.min(6, Math.max(1, Math.round(media / 7)));
}

/**
 * La chapa "esta semana", HONESTA (adjudicación fundador+auditor, ago 2026).
 *   - En modo FECHAS: aparece SOLO si la fecha vigente del ítem cae en la
 *     semana ISO actual (no en el bit `destacado`). Así, la destacada de una
 *     etapa FUTURA (fecha la semana que viene) NO la lleva: el rótulo deja de
 *     mentir sobre el calendario.
 *   - En modo A-MI-RITMO (o sin modo): se conserva atada a `destacado` — sin
 *     fechas, es la señal de arranque de la etapa, no un claim de calendario.
 * El gate !hecho/!retirada lo pone el llamador (la fila).
 */
export function chapaEstaSemana(
  modo: "ritmo" | "fechas" | null | undefined,
  item: { destacado: boolean; fecha_base?: string | null },
  ahora?: Date
): boolean {
  return modo === "fechas" ? esEstaSemana(item.fecha_base, ahora) : item.destacado;
}

/**
 * El ORDEN de lectura de los ítems de UNA etapa en modo FECHAS (adjudicación
 * ago 2026): por FECHA VIGENTE ascendente, con desempate ESTABLE por el orden
 * del plan (el sort estable de ES2019 conserva el orden de entrada ante fechas
 * iguales). Así la destacada del lunes sube al frente ("empieza por esta") y los
 * movimientos manuales de fecha del usuario también reordenan. Los sin-fecha van
 * al final. NO cambia la fecha (el viernes compartido de la etapa se respeta):
 * solo el orden en que se leen. En a-mi-ritmo el llamador NO ordena (deja el
 * orden del plan intacto).
 */
export function ordenarEnFechas<T extends { fecha_base?: string | null }>(items: T[]): T[] {
  return [...items].sort((a, b) => {
    const fa = a.fecha_base ?? null;
    const fb = b.fecha_base ?? null;
    if (fa && fb) return fa < fb ? -1 : fa > fb ? 1 : 0;
    if (fa) return -1;
    if (fb) return 1;
    return 0;
  });
}

/** Sugiere una fecha de calendario para cada ítem (determinístico). */
export function sugerirFechasBase(opts: {
  planCreatedAt: string;
  items: ItemSugerible[];
  /** día preferido (0-6) derivado de completed_at previos; null = por defecto */
  diaPreferido?: number | null;
  /** Fase 4.0: semanas por etapa aprendidas del ciclo previo (default 1). */
  cadenciaSemanas?: number;
}): FechaSugerida[] {
  const base = new Date(opts.planCreatedAt);
  const preferido = opts.diaPreferido ?? null;
  const cadencia = Math.max(1, Math.round(opts.cadenciaSemanas ?? 1));
  return opts.items.map((it) => {
    // "Esta semana" → inicio (lunes); regular → viernes, o el día preferido.
    const weekday = it.destacado ? LUNES : preferido ?? VIERNES;
    // La etapa N cae a N x cadencia semanas: el espaciado aprende del ritmo real.
    const objetivo = objetivoEnSemana(base, it.etapa * cadencia, weekday);
    return { id: it.id, fecha: fechaInputLocal(objetivo) };
  });
}
