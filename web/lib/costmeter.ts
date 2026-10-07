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
import { bloquesDeSistema } from "./i18n/idiomaSalida";
import Anthropic from "@anthropic-ai/sdk";
import { limpiarGuiones } from "./voz";

export const MODEL = "claude-sonnet-4-6";
export const MODEL_HAIKU = "claude-haiku-4-5";

export const PRECIOS: Record<string, [number, number]> = {
  [MODEL]: [3.0, 15.0],
  [MODEL_HAIKU]: [1.0, 5.0],
};

// Multiplicadores de cache sobre el precio de entrada: lectura ~10%;
// escritura de 5 minutos ~125% (Fase 2.7); escritura de 1 hora ~200%
// (contexto de la entrevista, principio 3, 28 sep 2026).
export const CACHE_READ_MULT = 0.1;
export const CACHE_WRITE_MULT = 1.25;
export const CACHE_WRITE_1H_MULT = 2.0;

/** Marca de cache de 1 hora: la parte fija (system y reglas) y el contexto del
 * proyecto. La parte del turno usa la de 5 minutos, la marca sin ttl. */
export const CACHE_1H = { type: "ephemeral", ttl: "1h" } as const;

// Hotfix v2.2.1: configurable por variable de entorno, espejo exacto de
// PRESUPUESTO_SESION_USD en prototipo_motor.py (mismo nombre de env var,
// mismo default subido de 0.30 a 0.35). PRESUPUESTO_REPORTE_USD se
// mantiene fijo -- --reporte es una corrida corta y aislada, no necesita
// ser configurable por separado.
function leerPresupuestoSesionUsd(): number {
  const raw = process.env.PRESUPUESTO_SESION_USD;
  if (!raw) return 0.35;
  const valor = Number(raw);
  return Number.isFinite(valor) ? valor : 0.35;
}

export const PRESUPUESTO_SESION_USD_DEFAULT = leerPresupuestoSesionUsd();
export const PRESUPUESTO_REPORTE_USD = 0.1;

export interface UsoModelo {
  in: number;
  out: number;
  llamadas: number;
  cache_read: number;
  /** escrituras de cache de 5 minutos (1.25x) */
  cache_write: number;
  /** escrituras de cache de 1 hora (2x); ausente en registros anteriores */
  cache_write_1h?: number;
}

/** El registro de UNA llamada, para medir el ahorro real del cache. */
export interface RegistroLlamada {
  componente: string | null;
  modelo: string;
  in: number;
  out: number;
  cache_read: number;
  cache_write_5m: number;
  cache_write_1h: number;
  usd: number;
  stop_reason: string | null;
  /** si la llamada llevo el contexto del proyecto (memoria y ficha); la prueba de coherencia lo exige salvo en su
   * lista blanca (los organizadores). Ausente en registros anteriores, que cuentan como sin contexto. */
  con_contexto?: boolean;
}

export interface UsoAcumulado {
  uso: Record<string, UsoModelo>;
  uso_por_componente: Record<string, number>;
  presupuesto_excedido: boolean;
  /** una entrada por llamada; ausente en registros anteriores */
  llamadas?: RegistroLlamada[];
}

/** Una respuesta cortada por tope de tokens que siguio cortada tras el
 * reintento: no se guarda nunca, se falla con aviso. */
export class RespuestaCortadaError extends Error {
  constructor(componente: string | null | undefined, maxTokens: number) {
    super(`respuesta cortada por tope de tokens (${componente ?? "sin componente"}, max_tokens ${maxTokens})`);
    this.name = "RespuestaCortadaError";
  }
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
  cacheWriteTokens = 0,
  cacheWrite1hTokens = 0
): number {
  const [pin, pout] = PRECIOS[model] ?? [0.0, 0.0];
  return (
    (inTokens / 1_000_000) * pin +
    (cacheReadTokens / 1_000_000) * pin * CACHE_READ_MULT +
    (cacheWriteTokens / 1_000_000) * pin * CACHE_WRITE_MULT +
    (cacheWrite1hTokens / 1_000_000) * pin * CACHE_WRITE_1H_MULT +
    (outTokens / 1_000_000) * pout
  );
}

/** Misma formula que costo_acumulado_usd en Python. */
export function costoAcumuladoUsd(acumulado: UsoAcumulado): number {
  let total = 0;
  for (const [model, s] of Object.entries(acumulado.uso)) {
    total += costoLlamadaUsd(model, s.in, s.out, s.cache_read, s.cache_write, s.cache_write_1h ?? 0);
  }
  return total;
}

/** Registra el uso de una llamada real (equivalente a _registrar_uso).
 * Devuelve un NUEVO UsoAcumulado (no muta el original), porque este
 * modulo no tiene estado propio -- el llamador decide cuando persistirlo. */
export function registrarUso(
  acumulado: UsoAcumulado,
  model: string,
  usage: {
    input_tokens: number;
    output_tokens: number;
    cache_read_input_tokens?: number | null;
    cache_creation_input_tokens?: number | null;
    cache_creation?: { ephemeral_5m_input_tokens?: number | null; ephemeral_1h_input_tokens?: number | null } | null;
  },
  componente?: string | null,
  stopReason: string | null = null,
  /** si la llamada llevo el contexto del proyecto; sin decirlo, cuenta como sin contexto */
  conContexto = false
): UsoAcumulado {
  const previo = acumulado.uso[model] ?? { in: 0, out: 0, llamadas: 0, cache_read: 0, cache_write: 0 };
  const cacheRead = usage.cache_read_input_tokens ?? 0;
  // Con desglose por TTL, cada escritura con su tarifa; sin el (respuestas
  // anteriores o dobles de prueba), toda escritura cuenta como de 5 minutos.
  const cacheWrite1h = usage.cache_creation ? usage.cache_creation.ephemeral_1h_input_tokens ?? 0 : 0;
  const cacheWrite = usage.cache_creation
    ? usage.cache_creation.ephemeral_5m_input_tokens ?? 0
    : usage.cache_creation_input_tokens ?? 0;
  const nuevoUso: UsoModelo = {
    in: previo.in + usage.input_tokens,
    out: previo.out + usage.output_tokens,
    cache_read: previo.cache_read + cacheRead,
    cache_write: previo.cache_write + cacheWrite,
    cache_write_1h: (previo.cache_write_1h ?? 0) + cacheWrite1h,
    llamadas: previo.llamadas + 1,
  };
  const costo = costoLlamadaUsd(model, usage.input_tokens, usage.output_tokens, cacheRead, cacheWrite, cacheWrite1h);
  const usoPorComponente = { ...acumulado.uso_por_componente };
  if (componente) {
    usoPorComponente[componente] = (usoPorComponente[componente] ?? 0) + costo;
  }
  const registro: RegistroLlamada = {
    componente: componente ?? null,
    modelo: model,
    in: usage.input_tokens,
    out: usage.output_tokens,
    cache_read: cacheRead,
    cache_write_5m: cacheWrite,
    cache_write_1h: cacheWrite1h,
    usd: costo,
    stop_reason: stopReason,
    con_contexto: conContexto,
  };
  return {
    uso: { ...acumulado.uso, [model]: nuevoUso },
    uso_por_componente: usoPorComponente,
    presupuesto_excedido: acumulado.presupuesto_excedido,
    llamadas: [...(acumulado.llamadas ?? []), registro],
  };
}

/** Suma dos acumulados (AUD-09 H06): una llamada con presupuesto PROPIO se
 * mide desde cero y su gasto se suma después al de la sesión, para que el
 * registro de costos siga completo. No muta ninguno de los dos. */
export function sumarUso(base: UsoAcumulado, extra: UsoAcumulado): UsoAcumulado {
  const uso: Record<string, UsoModelo> = { ...base.uso };
  for (const [model, e] of Object.entries(extra.uso)) {
    const b = uso[model] ?? { in: 0, out: 0, llamadas: 0, cache_read: 0, cache_write: 0 };
    uso[model] = {
      in: b.in + e.in,
      out: b.out + e.out,
      llamadas: b.llamadas + e.llamadas,
      cache_read: b.cache_read + e.cache_read,
      cache_write: b.cache_write + e.cache_write,
      cache_write_1h: (b.cache_write_1h ?? 0) + (e.cache_write_1h ?? 0),
    };
  }
  const uso_por_componente = { ...base.uso_por_componente };
  for (const [c, costo] of Object.entries(extra.uso_por_componente)) {
    uso_por_componente[c] = (uso_por_componente[c] ?? 0) + costo;
  }
  return {
    uso,
    uso_por_componente,
    presupuesto_excedido: base.presupuesto_excedido || extra.presupuesto_excedido,
    llamadas: [...(base.llamadas ?? []), ...(extra.llamadas ?? [])],
  };
}

export class PresupuestoExcedidoError extends Error {
  constructor(presupuestoUsd: number) {
    super(`presupuesto de sesion excedido ($${presupuestoUsd.toFixed(2)})`);
    this.name = "PresupuestoExcedidoError";
  }
}

/** i18n F5: `idiomaSalida` es el idioma de la IDEA (lib/i18n/idiomaSalida);
 * `rotulosFijos`, los marcadores de estructura que el código lee de la salida. */
export interface LlamadaOpts {
  maxTokens?: number;
  /** El contexto del proyecto (memoria y ficha de la persona): viaja en su
   * propio bloque, con cache de 1 hora, antes de la parte del turno. */
  contexto?: string | null;
  componente?: string;
  presupuestoUsd?: number;
  idiomaSalida?: string | null;
  rotulosFijos?: readonly string[];
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
  opts: LlamadaOpts = {}
): Promise<ResultadoLlamada> {
  const presupuestoUsd = opts.presupuestoUsd ?? PRESUPUESTO_SESION_USD_DEFAULT;
  if (costoAcumuladoUsd(acumulado) >= presupuestoUsd) {
    throw new PresupuestoExcedidoError(presupuestoUsd);
  }
  const content: string | BloqueTexto[] = opts.contexto
    ? [
        { type: "text", text: opts.contexto, cache_control: CACHE_1H },
        { type: "text", text: userText },
      ]
    : userText;
  let maxTokens = opts.maxTokens ?? 1500;
  let nuevoAcumulado = acumulado;
  for (let intento = 0; ; intento++) {
    const msg = await client.messages.create({
      model,
      max_tokens: maxTokens,
      system: bloquesDeSistema(system, opts.idiomaSalida, opts.rotulosFijos),
      messages: [{ role: "user", content }] as Anthropic.MessageParam[],
    });
    nuevoAcumulado = registrarUso(nuevoAcumulado, model, msg.usage, opts.componente, msg.stop_reason ?? null, Boolean(opts.contexto));
    // Una respuesta cortada por tope de tokens no se guarda nunca: un
    // reintento con el doble de tope, y si sigue cortada, error con aviso.
    if (msg.stop_reason === "max_tokens") {
      if (intento === 0) {
        maxTokens *= 2;
        continue;
      }
      throw new RespuestaCortadaError(opts.componente, maxTokens);
    }
    // Phase 3.7 (voz): punto único de salida — ningún texto del modelo viaja
    // con guiones largos/medios, ni siquiera si el prompt fue desobedecido.
    const texto = limpiarGuiones(
      msg.content
        .filter((b): b is Anthropic.TextBlock => b.type === "text")
        .map((b) => b.text)
        .join("")
    );
    return { texto, acumulado: nuevoAcumulado };
  }
}

export type BloqueTexto = { type: "text"; text: string; cache_control?: { type: "ephemeral"; ttl?: "5m" | "1h" } };
export type MensajeConversacion =
  | { role: "user"; content: string | BloqueTexto[] }
  | { role: "assistant"; content: string };

export interface ResultadoLlamadaConversacion {
  texto: string;
  acumulado: UsoAcumulado;
  historialMensajes: MensajeConversacion[];
}

/**
 * Equivalente a llamar_claude_conversacion(): mantiene una conversacion
 * (historialMensajes) que crece turno a turno, con el marcador de cache
 * SIEMPRE en el ultimo bloque enviado (se quita del turno previamente
 * marcado, se coloca en el nuevo) -- asi todo el prefijo previo (entrada
 * original, perfil acumulado, turnos anteriores) se lee de cache en vez
 * de repagarse completo cada vez. Devuelve un historialMensajes NUEVO (no
 * muta el array de entrada); el llamador (la ruta de /turn) es quien
 * decide persistirlo en Supabase para el proximo turno de la misma
 * sesion -- a diferencia del CLI, donde este historial vive solo en
 * memoria del proceso y --continuar lo pierde (Fase 2.7 docstring: "vive
 * solo en memoria de esta corrida, no se persiste"), la web SI puede
 * persistirlo, logrando el mismo beneficio de cache incluso despues de
 * que el usuario cierre la pestaña entre turnos.
 */
export async function llamarClaudeConversacion(
  client: Anthropic,
  system: string,
  historialMensajes: MensajeConversacion[],
  nuevoTurnoTexto: string,
  model: string,
  acumulado: UsoAcumulado,
  opts: LlamadaOpts = {}
): Promise<ResultadoLlamadaConversacion> {
  const presupuestoUsd = opts.presupuestoUsd ?? PRESUPUESTO_SESION_USD_DEFAULT;
  if (costoAcumuladoUsd(acumulado) >= presupuestoUsd) {
    throw new PresupuestoExcedidoError(presupuestoUsd);
  }

  // Quita cache_control del ultimo bloque previamente marcado (busca hacia
  // atras el primer mensaje con content en forma de lista -- el mas
  // reciente puede ser un turno "assistant" con content string plano).
  const historialSinMarca: MensajeConversacion[] = historialMensajes.map((m) => m);
  for (let i = historialSinMarca.length - 1; i >= 0; i--) {
    const msg = historialSinMarca[i];
    if (msg.role === "user" && Array.isArray(msg.content) && msg.content.length > 0) {
      const bloques = [...msg.content];
      const ultimo = { ...bloques[bloques.length - 1] };
      delete ultimo.cache_control;
      bloques[bloques.length - 1] = ultimo;
      historialSinMarca[i] = { role: "user", content: bloques };
      break;
    }
  }

  // Principio 1 (28 sep 2026): en el PRIMER turno de la conversacion, el
  // contexto del proyecto entra en su propio bloque con cache de 1 hora; desde
  // ahi vive al principio del historial, que solo crece por el final.
  const bloqueTurno: BloqueTexto = { type: "text", text: nuevoTurnoTexto, cache_control: { type: "ephemeral" } };
  const nuevoTurno: MensajeConversacion = {
    role: "user",
    content:
      historialMensajes.length === 0 && opts.contexto
        ? [{ type: "text", text: opts.contexto, cache_control: CACHE_1H }, bloqueTurno]
        : [bloqueTurno],
  };

  // La llamada lleva el contexto si su bloque de 1 hora viaja en lo que se envia: en este turno (el primero) o al
  // principio del historial (los siguientes). Se registra por llamada para la prueba de coherencia.
  const conContexto = [...historialSinMarca, nuevoTurno].some(
    (m) => m.role === "user" && Array.isArray(m.content) && m.content.some((b) => b.cache_control?.ttl === "1h")
  );

  let maxTokens = opts.maxTokens ?? 600;
  let nuevoAcumulado = acumulado;
  let msg: Anthropic.Message;
  for (let intento = 0; ; intento++) {
    msg = await client.messages.create({
      model,
      max_tokens: maxTokens,
      system: bloquesDeSistema(system, opts.idiomaSalida, opts.rotulosFijos),
      messages: [...historialSinMarca, nuevoTurno] as Anthropic.MessageParam[],
    });
    nuevoAcumulado = registrarUso(nuevoAcumulado, model, msg.usage, opts.componente, msg.stop_reason ?? null, conContexto);
    // Misma regla que llamarClaude: nunca se guarda una respuesta cortada.
    if (msg.stop_reason === "max_tokens") {
      if (intento === 0) {
        maxTokens *= 2;
        continue;
      }
      throw new RespuestaCortadaError(opts.componente, maxTokens);
    }
    break;
  }
  // Phase 3.7 (voz): mismo filtro que llamarClaude — ver nota allá.
  const texto = limpiarGuiones(
    msg.content
      .filter((b): b is Anthropic.TextBlock => b.type === "text")
      .map((b) => b.text)
      .join("")
  );

  // Solo se compromete al historial real si la llamada tuvo exito (si
  // client.messages.create() lanza, no llegamos aqui).
  const historialActualizado: MensajeConversacion[] = [
    ...historialSinMarca,
    nuevoTurno,
    { role: "assistant", content: texto },
  ];

  return { texto, acumulado: nuevoAcumulado, historialMensajes: historialActualizado };
}

export interface DesgloseCosto {
  por_modelo: Record<
    string,
    { llamadas: number; in: number; out: number; cache_read: number; cache_write: number; cache_write_1h: number; costo_usd: number }
  >;
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
    const costo = costoLlamadaUsd(model, s.in, s.out, s.cache_read, s.cache_write, s.cache_write_1h ?? 0);
    total += costo;
    porModelo[model] = {
      llamadas: s.llamadas,
      in: s.in,
      out: s.out,
      cache_read: s.cache_read,
      cache_write: s.cache_write,
      cache_write_1h: s.cache_write_1h ?? 0,
      costo_usd: costo,
    };
  }
  return {
    por_modelo: porModelo,
    por_componente: acumulado.uso_por_componente,
    total_usd: total,
    presupuesto_excedido: acumulado.presupuesto_excedido,
  };
}
