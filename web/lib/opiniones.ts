/**
 * LAS OPINIONES DE LOS USUARIOS (decisión del fundador, 8 oct 2026, antes de la beta). Lo puro: cuándo se pregunta,
 * qué se acepta del navegador y cómo sale el CSV del panel del fundador. Lo que toca la base vive en
 * lib/opinionesServidor.ts; la tabla es la de la migración 051 (opiniones). Prueba: lib/opiniones.test.ts.
 *
 * Solo opinan las cuentas reales. La pregunta de un clic sale en los momentos clave (al recibir un plan, un plan de
 * mundo, una profundización o un replanteamiento) y, de vez en cuando, en el seguimiento ("¿Qué tal va tu idea?").
 * Nunca es un modal: es una tarjeta dentro de la pantalla, una sola vez por plan, con su botón de cerrar y con tope.
 */
import { OPINIONES_MOTIVO, OPINIONES_TIPO, OPINIONES_VALORACION, type OpinionMotivo, type OpinionTipo, type OpinionValoracion } from "./dbContract";

export const TEXTO_MAX = 2000;
/** Comentarios y sugerencias por cuenta en 24 horas. */
export const TOPE_GENERALES_DIA = 5;
/** Escrituras de opiniones por cuenta en 24 horas (todas: tarjetas, cierres, motivos y comentarios). */
export const TOPE_ESCRITURAS_DIA = 30;

/** Las reglas de frecuencia. Cambiarlas cambia cuánto se le pregunta a la gente: van con su prueba. */
export const REGLAS_FRECUENCIA = {
  /** Un plan se pregunta solo si llegó hace esta cantidad de días o menos ("al recibirlo"). */
  ventanaPlanDias: 14,
  /** Como máximo estas tarjetas respondidas o cerradas en las últimas 24 horas. */
  topeTarjetasDia: 2,
  /** "¿Qué tal va tu idea?" solo si el último plan de la idea tiene al menos estos días. */
  seguimientoTrasPlanDias: 7,
  /** …y como mucho una vez cada tantos días por idea. */
  seguimientoCadaDias: 30,
  /** …y nunca dentro de estas horas después de cualquier otra tarjeta. */
  pausaSeguimientoHoras: 72,
} as const;

const HORA = 3_600_000;
const DIA = 24 * HORA;

export type TipoDePlan = Exclude<OpinionTipo, "seguimiento" | "general">;

/** El tipo de la opinión sale del plan (etiqueta y espacio), nunca del navegador. La Claridad y el informe de
 * números no se preguntan. */
export function tipoDePlan(etiqueta: string, dominio: string | null | undefined): TipoDePlan | null {
  if (etiqueta === "seguimiento") return "profundizacion";
  if (etiqueta === "replanteamiento") return "replanteamiento";
  if (etiqueta === "inicial" || etiqueta === "completo") return !dominio || dominio === "core" ? "plan" : "plan_mundo";
  return null;
}

/** Lo que el historial de la persona necesita para decidir: sus opiniones anteriores. */
export interface FilaHistorial {
  tipo: OpinionTipo;
  objeto_id: string | null;
  created_at: string;
}

export type EventoOpinion =
  | { tipo: TipoDePlan; objetoId: string; creadoAt: string }
  | { tipo: "seguimiento"; objetoId: string; ultimoPlanAt: string | null };

export type Decision =
  | { preguntar: true }
  | { preguntar: false; razon: "ya_respondida" | "fuera_de_ventana" | "tope_diario" | "muy_pronto" | "reciente" | "pausa" };

/** ¿Se le muestra la tarjeta? Las tarjetas de evento cuentan para el tope; los Comentarios y sugerencias, no. */
export function decidirPregunta(evento: EventoOpinion, historial: readonly FilaHistorial[], ahora: Date): Decision {
  const t = ahora.getTime();
  const hace = (iso: string) => t - new Date(iso).getTime();
  const deEvento = historial.filter((h) => h.tipo !== "general");

  if (evento.tipo === "seguimiento") {
    if (!evento.ultimoPlanAt || hace(evento.ultimoPlanAt) < REGLAS_FRECUENCIA.seguimientoTrasPlanDias * DIA) {
      return { preguntar: false, razon: "muy_pronto" };
    }
    if (deEvento.some((h) => h.tipo === "seguimiento" && h.objeto_id === evento.objetoId && hace(h.created_at) < REGLAS_FRECUENCIA.seguimientoCadaDias * DIA)) {
      return { preguntar: false, razon: "reciente" };
    }
    if (deEvento.some((h) => hace(h.created_at) < REGLAS_FRECUENCIA.pausaSeguimientoHoras * HORA)) {
      return { preguntar: false, razon: "pausa" };
    }
  } else {
    if (deEvento.some((h) => h.tipo !== "seguimiento" && h.objeto_id === evento.objetoId)) return { preguntar: false, razon: "ya_respondida" };
    if (hace(evento.creadoAt) > REGLAS_FRECUENCIA.ventanaPlanDias * DIA) return { preguntar: false, razon: "fuera_de_ventana" };
  }
  if (deEvento.filter((h) => hace(h.created_at) < DIA).length >= REGLAS_FRECUENCIA.topeTarjetasDia) {
    return { preguntar: false, razon: "tope_diario" };
  }
  return { preguntar: true };
}

export type OpinionValida = { ok: true; valoracion: OpinionValoracion | null; motivo: OpinionMotivo | null; texto: string | null };

/** Lo que se acepta del navegador. Todo vacío vale: es "cerrar sin responder". El motivo solo va con "malo". */
export function validarOpinion(body: unknown): OpinionValida | { ok: false } {
  const b = (body && typeof body === "object" ? body : {}) as Record<string, unknown>;
  const valoracion = b.valoracion ?? null;
  const motivo = b.motivo ?? null;
  const texto = typeof b.texto === "string" ? b.texto.trim() : b.texto ?? null;
  if (valoracion !== null && !(OPINIONES_VALORACION as readonly unknown[]).includes(valoracion)) return { ok: false };
  if (motivo !== null && !(OPINIONES_MOTIVO as readonly unknown[]).includes(motivo)) return { ok: false };
  if (motivo !== null && valoracion !== "malo") return { ok: false };
  if (texto !== null && (typeof texto !== "string" || texto.length > TEXTO_MAX)) return { ok: false };
  return {
    ok: true,
    valoracion: valoracion as OpinionValoracion | null,
    motivo: motivo as OpinionMotivo | null,
    texto: texto ? (texto as string) : null,
  };
}

/** Una opinión tal como la lee el panel del fundador (contexto incluido). */
export interface FilaOpinion {
  id: string;
  created_at: string;
  tipo: OpinionTipo;
  valoracion: OpinionValoracion | null;
  motivo: OpinionMotivo | null;
  texto: string | null;
  idioma: string;
  proyecto_id: string | null;
  objeto_id: string | null;
  contexto: { etiqueta?: string; ciclo?: number; mundo?: string; nodos?: string[] } | Record<string, never>;
}

const CORREO = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g;

/** Una celda de CSV: sin correos (alguien pudo escribir el suyo en el texto), sin fórmulas y con comillas cuando
 * hacen falta. */
function celda(v: unknown): string {
  let s = v === null || v === undefined ? "" : String(v);
  s = s.replace(CORREO, "[correo]");
  if (/^[=+\-@\t\r]/.test(s)) s = `'${s}`;
  return /[",\r\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

export const CABECERA_CSV = ["fecha", "tipo", "valoracion", "motivo", "texto", "idioma", "proyecto", "objeto", "etiqueta", "ciclo", "mundo", "nodos", "id"] as const;

/** El CSV que descarga el fundador: una fila por opinión, con su contexto interno aplanado. */
export function aCsv(filas: readonly FilaOpinion[]): string {
  const lineas = filas.map((f) => {
    const c = f.contexto as { etiqueta?: string; ciclo?: number; mundo?: string; nodos?: string[] };
    return [f.created_at, f.tipo, f.valoracion, f.motivo, f.texto, f.idioma, f.proyecto_id, f.objeto_id, c.etiqueta, c.ciclo, c.mundo, (c.nodos ?? []).join(" "), f.id]
      .map(celda)
      .join(",");
  });
  return [CABECERA_CSV.join(","), ...lineas].join("\r\n");
}

/** La "versión" del plan: su número de ciclo dentro de su espacio (el primer plan del núcleo es el 1, la primera
 * profundización del núcleo el 2; los mundos cuentan aparte). */
export function numeroDeCiclo(
  ciclos: ReadonlyArray<{ id: string; dominio: string | null; created_at: string }>,
  plan: { id: string; dominio: string | null; created_at: string },
): number {
  const espacio = (d: string | null) => d || "core";
  const previos = ciclos.filter((c) => espacio(c.dominio) === espacio(plan.dominio) && c.id !== plan.id && c.created_at <= plan.created_at);
  return previos.length + 1;
}

/** Los filtros del panel del fundador. Un valor que no existe se ignora (lista todo). */
export interface FiltrosPanel {
  tipo?: OpinionTipo | null;
  /** 'sin' = sin valoración (cerró sin responder o comentario sin valorar). */
  valoracion?: OpinionValoracion | "sin" | null;
  limite?: number;
}

export function filtrosDe(params: URLSearchParams): FiltrosPanel {
  const tipo = params.get("tipo") ?? "";
  const valoracion = params.get("valoracion") ?? "";
  return {
    tipo: (OPINIONES_TIPO as readonly string[]).includes(tipo) ? (tipo as OpinionTipo) : null,
    valoracion: valoracion === "sin" ? "sin" : (OPINIONES_VALORACION as readonly string[]).includes(valoracion) ? (valoracion as OpinionValoracion) : null,
  };
}
