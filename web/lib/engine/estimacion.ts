/**
 * estimacion.ts — Scheduler Inteligente, Fase 1: la estimación NACE con el plan.
 *
 * Al nacer todo plan nuevo (core o mundo), el modelo estima la BANDA de esfuerzo
 * (S/M/L/XL) + espera_externa de cada ítem del checklist. Para bajar la varianza
 * inter-corrida a la que el spike de F0 midió (97.2% exacta-o-adyacente a nivel
 * ítem), producción usa MAYORÍA-DE-3: tres corridas batch, banda = voto
 * mayoritario; empate → la banda MAYOR de las empatadas (conservador). Mismo
 * criterio para espera_externa.
 *
 * Doctrina de fallo (BANCO §9, "fallar ruidoso"): si la estimación falla —red,
 * JSON no parseable, presupuesto— el ítem queda SIN banda (null) y el plan JAMÁS
 * se bloquea. El sugeridor viejo de fechas sigue siendo el fallback que nunca
 * muere. El fallo deja síntoma: la ruta del plan registra un evento de sesión.
 *
 * Este módulo es PURO salvo estimarLoteMayoria (una llamada aislada corta). El
 * voto y el parser se prueban sin tocar el LLM.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { BANDA, type Banda } from "../dbContract";
import { llamarClaude, MODEL, type UsoAcumulado } from "../costmeter";
import { SYSTEM_ESTIMACION_BANDA } from "../prompts";

export interface EstimacionItem {
  banda: Banda;
  espera_externa: boolean;
}

/** Lo mínimo que necesita estimar un ítem: su texto y (contexto) su etapa. */
export interface ItemAEstimar {
  texto: string;
  etapa?: number;
}

const ORDEN_BANDA: readonly Banda[] = BANDA;
const idxBanda = (b: Banda) => ORDEN_BANDA.indexOf(b);

const CORRIDAS = 3;
/** Mayoría-de-3: sin al menos 2 corridas válidas que voten un ítem, no se le
 * inventa banda (una sola corrida no es "mayoría de 3"). En la degradación
 * total (2 de 3 corridas caídas) esto deja el plan sin bandas = el fallback. */
const MIN_VOTOS = 2;

/** Voto por mayoría sobre las bandas de las corridas. Empate → la banda MAYOR de
 * las empatadas (conservador, criterio del fundador). null si no hay votos. */
export function votoMayoriaBanda(bandas: Banda[]): Banda | null {
  if (bandas.length === 0) return null;
  const cuenta = new Map<Banda, number>();
  for (const b of bandas) cuenta.set(b, (cuenta.get(b) ?? 0) + 1);
  const max = Math.max(...cuenta.values());
  const empatadas = [...cuenta.entries()].filter(([, c]) => c === max).map(([b]) => b);
  // empate → la mayor de las empatadas
  return empatadas.reduce((a, b) => (idxBanda(b) > idxBanda(a) ? b : a));
}

/** Voto por mayoría sobre espera_externa. Empate (recuento par partido) → true
 * (conservador: asumir que sí hay espera reserva más colchón en el calendario). */
export function votoMayoriaEspera(esperas: boolean[]): boolean {
  if (esperas.length === 0) return false;
  const si = esperas.filter((e) => e).length;
  const no = esperas.length - si;
  if (si === no) return true; // empate → conservador
  return si > no;
}

interface Voto {
  id: number;
  banda: Banda;
  espera: boolean;
}

/** Parsea la respuesta batch: un array JSON [{id,banda,espera_externa}]. Robusto
 * a fences ```json y a texto alrededor. Ignora entradas mal formadas (no
 * inventa): un objeto sin id entero o sin banda válida no vota. */
export function parsearLote(texto: string): Voto[] {
  const m = texto.match(/\[[\s\S]*\]/);
  if (!m) return [];
  let arr: unknown;
  try {
    arr = JSON.parse(m[0]);
  } catch {
    return [];
  }
  if (!Array.isArray(arr)) return [];
  const votos: Voto[] = [];
  for (const el of arr) {
    if (!el || typeof el !== "object") continue;
    const o = el as { id?: unknown; banda?: unknown; espera_externa?: unknown };
    const id = typeof o.id === "number" && Number.isInteger(o.id) ? o.id : null;
    const banda = (ORDEN_BANDA as readonly string[]).includes(o.banda as string) ? (o.banda as Banda) : null;
    if (id === null || banda === null) continue;
    const espera = typeof o.espera_externa === "boolean" ? o.espera_externa : false;
    votos.push({ id, banda, espera });
  }
  return votos;
}

/** El mensaje de usuario: la lista de tareas como array JSON con id por índice. */
export function construirUserText(items: ItemAEstimar[]): string {
  const tareas = items.map((it, i) => ({ id: i, tarea: it.texto, etapa: it.etapa ?? null }));
  return [
    "Estima el esfuerzo de CADA una de estas tareas de un plan de negocio.",
    "Devuelve SOLO el array JSON de salida, con un objeto por tarea y su mismo id.",
    "",
    JSON.stringify(tareas),
  ].join("\n");
}

export interface ResultadoEstimacion {
  /** Por índice de items: la estimación con mayoría, o null (sin banda). */
  estimaciones: (EstimacionItem | null)[];
  acumulado: UsoAcumulado;
}

/**
 * Estima el lote entero por MAYORÍA-DE-3. Cada corrida que falla (red, JSON no
 * parseable, presupuesto) simplemente no aporta votos: la mayoría degrada con
 * gracia; si TODAS fallan, todo queda null (fallback declarado, sin lanzar).
 */
export async function estimarLoteMayoria(
  client: Anthropic,
  items: ItemAEstimar[],
  acumulado: UsoAcumulado,
  opts: { componente?: string; presupuestoUsd?: number } = {}
): Promise<ResultadoEstimacion> {
  if (items.length === 0) return { estimaciones: [], acumulado };
  const userText = construirUserText(items);
  const maxTokens = Math.min(4000, 200 + items.length * 40);

  const votosPorItem: { bandas: Banda[]; esperas: boolean[] }[] = items.map(() => ({ bandas: [], esperas: [] }));
  let acc = acumulado;
  for (let c = 0; c < CORRIDAS; c += 1) {
    let texto: string;
    try {
      const r = await llamarClaude(client, SYSTEM_ESTIMACION_BANDA, userText, MODEL, acc, {
        maxTokens,
        componente: opts.componente ?? "estimacion_banda",
        presupuestoUsd: opts.presupuestoUsd ?? 5,
      });
      acc = r.acumulado;
      texto = r.texto;
    } catch {
      continue; // corrida perdida: sin votos, sin romper el plan
    }
    for (const v of parsearLote(texto)) {
      if (v.id >= 0 && v.id < items.length) {
        votosPorItem[v.id].bandas.push(v.banda);
        votosPorItem[v.id].esperas.push(v.espera);
      }
    }
  }

  const estimaciones = votosPorItem.map(({ bandas, esperas }): EstimacionItem | null => {
    if (bandas.length < MIN_VOTOS) return null; // sin mayoría real: no se inventa
    return { banda: votoMayoriaBanda(bandas)!, espera_externa: votoMayoriaEspera(esperas) };
  });
  return { estimaciones, acumulado: acc };
}

/** Rango honesto en palabras para una banda (para el detalle de la tarea). Son
 * las MISMAS fronteras del prompt validado; JAMÁS un número de horas inventado. */
export function rangoDeBanda(banda: Banda | null | undefined): string | null {
  switch (banda) {
    case "S":
      return "~1 h";
    case "M":
      return "~2-4 h";
    case "L":
      return "una jornada";
    case "XL":
      return "varios días";
    default:
      return null; // plan viejo o estimación fallida: sin rango, cero invención
  }
}
