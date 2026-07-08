/**
 * costmeter.ts - Fase 3.0: port de la contabilidad de costo real de
 * engine/prototipo_motor.py (PRECIOS, USO, USO_POR_COMPONENTE,
 * _costo_llamada_usd, costo_acumulado_usd, costo_por_componente_usd,
 * reportar_costo).
 *
 * DIFERENCIA DE ARQUITECTURA DELIBERADA (no es un descuido de puerteo):
 * en Python, USO/USO_POR_COMPONENTE/PRESUPUESTO_EXCEDIDO son variables
 * globales de modulo que viven mientras dura UN proceso de CLI = UNA
 * sesion. En la web, cada ruta de API es una invocacion de funcion
 * serverless separada, sin memoria compartida entre llamadas (ni
 * siquiera entre dos turnos consecutivos de la MISMA sesion). Por eso
 * este modulo expone funciones PURAS sobre un acumulador explicito
 * (UsoAcumulado), y el llamador (la ruta de API) es responsable de leer
 * el acumulador desde sessions.costo_usd/costo_desglose en Supabase antes
 * de cada llamada, y persistir el acumulador actualizado despues -- el
 * presupuesto duro por sesion sigue siendo real, solo que vive en la
 * base de datos en vez de en memoria del proceso.
 */
import Anthropic from "@anthropic-ai/sdk";

export const MODEL = "claude-sonnet-4-6";
export const MODEL_HAIKU = "claude-haiku-4-5";

export const PRECIOS: Record<string, [number, number]> = {
  [MODEL]: [3.0, 15.0],
  [MODEL_HAIKU]: [1.0, 5.0],
};

// Multiplicadores de cache ephemeral (5 min) sobre el precio de entrada:
// lectura de cache cuesta ~10%, escritura de cache cuesta ~125% (Fase 2.7).
export const CACHE_READ_MULT = 0.1;
export const CACHE_WRITE_MULT = 1.25;

export const PRESUPUESTO_SESION_USD_DEFAULT = 0.3;
export const PRESUPUESTO_REPORTE_USD = 0.1;

export interface UsoModelo {
  in: number;
  out: number;
  llamadas: number;
  cache_read: number;
  cache_write: number;
}

export interface UsoAcumulado {
  uso: Record<string, UsoModelo>;
  uso_por_componente: Record<string, number>;
  presupuesto_excedido: boolean;
}

export function usoVacio(): UsoAcumulado {
  return { uso: {}, uso_por_componente: {}, presupuesto_excedido: false };
}

/** Misma formula que _costo_llamada_usd en Python. */
export function costoLlamadaUsd(
  model: string,
  inTokens: number,
  outTokens: number,
  cacheReadTokens = 0,
  cacheWriteTokens = 0
): number {
  const [pin, pout] = PRECIOS[model] ?? [0.0, 0.0];
  return (
    (inTokens / 1_000_000) * pin +
    (cacheReadTokens / 1_000_000) * pin * CACHE_READ_MULT +
    (cacheWriteTokens / 1_000_000) * pin * CACHE_WRITE_MULT +
    (outTokens / 1_000_000) * pout
  );
}

/** Misma formula que costo_acumulado_usd en Python. */
export function costoAcumuladoUsd(acumulado: UsoAcumulado): number {
  let total = 0;
  for (const [model, s] of Object.entries(acumulado.uso)) {
    total += costoLlamadaUsd(model, s.in, s.out, s.cache_read, s.cache_write);
  }
  return total;
}

/** Registra el uso de una llamada real (equivalente a _registrar_uso).
 * Devuelve un NUEVO UsoAcumulado (no muta el original), porque este
 * modulo no tiene estado propio -- el llamador decide cuando persistirlo. */
export function registrarUso(
  acumulado: UsoAcumulado,
  model: string,
  usage: { input_tokens: number; output_tokens: number; cache_read_input_tokens?: number | null; cache_creation_input_tokens?: number | null },
  componente?: string | null
): UsoAcumulado {
  const previo = acumulado.uso[model] ?? { in: 0, out: 0, llamadas: 0, cache_read: 0, cache_write: 0 };
  const cacheRead = usage.cache_read_input_tokens ?? 0;
  const cacheWrite = usage.cache_creation_input_tokens ?? 0;
  const nuevoUso: UsoModelo = {
    in: previo.in + usage.input_tokens,
    out: previo.out + usage.output_tokens,
    cache_read: previo.cache_read + cacheRead,
    cache_write: previo.cache_write + cacheWrite,
    llamadas: previo.llamadas + 1,
  };
  const usoPorComponente = { ...acumulado.uso_por_componente };
  if (componente) {
    const costo = costoLlamadaUsd(model, usage.input_tokens, usage.output_tokens, cacheRead, cacheWrite);
    usoPorComponente[componente] = (usoPorComponente[componente] ?? 0) + costo;
  }
  return {
    uso: { ...acumulado.uso, [model]: nuevoUso },
    uso_por_componente: usoPorComponente,
    presupuesto_excedido: acumulado.presupuesto_excedido,
  };
}

export class PresupuestoExcedidoError extends Error {
  constructor(presupuestoUsd: number) {
    super(`presupuesto de sesion excedido ($${presupuestoUsd.toFixed(2)})`);
    this.name = "PresupuestoExcedidoError";
  }
}

export interface ResultadoLlamada {
  texto: string;
  acumulado: UsoAcumulado;
}

/**
 * Equivalente a llamar_claude(): chequea presupuesto ANTES de llamar
 * (mismo criterio: costoAcumuladoUsd(acumulado) >= presupuestoUsd), y si
 * ya esta excedido, marca presupuesto_excedido=true en el acumulador
 * devuelto y lanza PresupuestoExcedidoError -- el llamador debe persistir
 * ese acumulado (con presupuesto_excedido=true) incluso en el catch, para
 * que el proximo turno de la misma sesion no vuelva a intentar la
 * llamada real.
 */
export async function llamarClaude(
  client: Anthropic,
  system: string,
  userText: string,
  model: string,
  acumulado: UsoAcumulado,
  opts: { maxTokens?: number; componente?: string; presupuestoUsd?: number } = {}
): Promise<ResultadoLlamada> {
  const presupuestoUsd = opts.presupuestoUsd ?? PRESUPUESTO_SESION_USD_DEFAULT;
  if (costoAcumuladoUsd(acumulado) >= presupuestoUsd) {
    throw new PresupuestoExcedidoError(presupuestoUsd);
  }
  const msg = await client.messages.create({
    model,
    max_tokens: opts.maxTokens ?? 1500,
    system: [{ type: "text", text: system, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content: userText }],
  });
  const nuevoAcumulado = registrarUso(acumulado, model, msg.usage, opts.componente);
  const texto = msg.content
    .filter((b): b is Anthropic.TextBlock => b.type === "text")
    .map((b) => b.text)
    .join("");
  return { texto, acumulado: nuevoAcumulado };
}

export interface DesgloseCosto {
  por_modelo: Record<string, { llamadas: number; in: number; out: number; cache_read: number; cache_write: number; costo_usd: number }>;
  por_componente: Record<string, number>;
  total_usd: number;
  presupuesto_excedido: boolean;
}

/** Equivalente a reportar_costo(), pero devuelve el desglose estructurado
 * en vez de imprimirlo (la UI/route decide como mostrarlo). */
export function desgloseCosto(acumulado: UsoAcumulado): DesgloseCosto {
  const porModelo: DesgloseCosto["por_modelo"] = {};
  let total = 0;
  for (const [model, s] of Object.entries(acumulado.uso)) {
    const costo = costoLlamadaUsd(model, s.in, s.out, s.cache_read, s.cache_write);
    total += costo;
    porModelo[model] = { llamadas: s.llamadas, in: s.in, out: s.out, cache_read: s.cache_read, cache_write: s.cache_write, costo_usd: costo };
  }
  return {
    por_modelo: porModelo,
    por_componente: acumulado.uso_por_componente,
    total_usd: total,
    presupuesto_excedido: acumulado.presupuesto_excedido,
  };
}
