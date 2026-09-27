/**
 * replanteamiento.ts — Ciclo de replanteamiento, Fase 2 (decisiones del
 * fundador, 27 sep 2026; docs/producto/CICLO_REPLANTEAMIENTO.md).
 *
 * Las piezas PURAS de las dos entradas de Manos a la Obra:
 *  - "Replantear mi camino": su mensaje a la IA (la historia primero), la
 *    validación de los caminos que propone la IA, y las filas que traen al plan
 *    nuevo, COMO HECHAS, las tareas que "me siguen sirviendo".
 *  - Lo común a los dos ciclos: el plan anterior como lo recibe el redactor
 *    (etapas con sus tareas y su estado) y el relato de la persona que queda en
 *    la bitácora, el Expediente y la Historia.
 *
 * Determinístico, sin IA ni base de datos: las rutas lo usan y las pruebas lo
 * ejercitan de verdad.
 */
import type { ChecklistEstado } from "../dbContract";
import type { ItemParaComponer } from "./seguimientoComposer";

/** Una tarea hecha del plan vigente, como la eligió la persona en el paso 2. */
export interface TareaCiclo {
  id: string;
  texto: string;
  nota?: string | null;
  completed_at?: string | null;
  etapa?: number;
}

/** Un camino posible del paso 3, anclado a conceptos del grafo que el código
 * ofreció (los `nodos` son la ruta del plan si la persona lo elige). */
export interface Camino {
  id: string;
  titulo: string;
  descripcion: string;
  nodos: string[];
}

/** Lo que la persona pidió al abrir el ciclo, guardado con la sesión
 * (estado_recorrido.recorrido.ciclo). Viaja hasta la entrega del plan, donde se
 * registra en la bitácora. */
export type CicloSesion =
  | { tipo: "profundizar"; detalles: string | null; enfoque: string | null }
  | {
      tipo: "replantear";
      historia: string;
      conserva: TareaCiclo[];
      suelta: TareaCiclo[];
      caminos: Camino[];
      caminoElegido: string | null;
      /** Qué vuelta de caminos es esta (1, 2 o 3): cuenta desde la sesión
       * previa del mismo ritual. Ausente en sesiones de antes del tope = 1. */
      generacion?: number;
    };

const linea = (t: TareaCiclo) => `- ${t.texto}${t.nota?.trim() ? ` (nota: ${t.nota.trim()})` : ""}`;

/**
 * El mensaje de entrada de un replanteamiento. Va a la IA (los caminos y el
 * plan) y queda como mensaje_entrada de la sesión. Como el del seguimiento, en
 * español: la IA responde en el idioma de la idea (lib/i18n/idiomaSalida).
 * Orden: la historia de la persona manda, luego lo que se conserva (construir
 * encima), lo que se suelta (no volver a proponerlo), lo pendiente del plan
 * anterior, la realidad medida y la orden de no empezar de cero.
 */
export function componerMensajeReplanteamiento(e: {
  historia: string;
  conserva: TareaCiclo[];
  suelta: TareaCiclo[];
  pendientes: ItemParaComponer[];
  bloqueRealidad: string | null;
}): string {
  const partes = ["Quiero replantear mi camino. Esto es lo que pasó:", e.historia.trim(), ""];
  if (e.conserva.length) {
    partes.push(`Lo que ya construí y ME SIGUE SIRVIENDO (${e.conserva.length}). No lo repitas, construye encima:`, ...e.conserva.map(linea));
  }
  if (e.suelta.length) {
    partes.push(`Lo que ya construí y YA NO APLICA (${e.suelta.length}). No lo vuelvas a proponer:`, ...e.suelta.map(linea));
  }
  if (e.pendientes.length) {
    partes.push(`Lo que quedaba pendiente del plan anterior (${e.pendientes.length}):`, ...e.pendientes.map((p) => `- ${p.texto}`));
  }
  const bloque = e.bloqueRealidad?.trim();
  if (e.conserva.length || e.suelta.length || e.pendientes.length) partes.push("");
  if (bloque) partes.push(bloque, "");
  partes.push("No empieces de cero: parte de lo que ya tengo.");
  return partes.join("\n");
}

/** Decisión del fundador (28 sep 2026): un replanteamiento pide caminos 3
 * veces como mucho (la primera y dos vueltas atrás). Cada vuelta es una llamada
 * a la IA dentro del mismo cobro. */
export const TOPE_GENERACIONES_CAMINOS = 3;

const MAX_CAMINOS = 3;
const MAX_NODOS_POR_CAMINO = 5;

/**
 * Lo que devolvió la IA para el paso 3, validado por código: cada camino con
 * título y solo con conceptos de la lista que se le ofreció (sin inventados ni
 * repetidos, hasta 5); los que se quedan sin conceptos o sin título se caen.
 * Hasta tres, numerados a, b, c. Quien llama decide qué hacer con menos de dos.
 */
export function validarCaminos(data: unknown, candidatos: string[]): Camino[] {
  const lista = (data as { caminos?: unknown } | null)?.caminos;
  if (!Array.isArray(lista)) return [];
  const validos = new Set(candidatos);
  const caminos: Camino[] = [];
  for (const crudo of lista) {
    if (caminos.length >= MAX_CAMINOS) break;
    const c = crudo as { titulo?: unknown; descripcion?: unknown; nodos?: unknown };
    const titulo = typeof c.titulo === "string" ? c.titulo.trim() : "";
    const descripcion = typeof c.descripcion === "string" ? c.descripcion.trim() : "";
    const nodos: string[] = [];
    for (const n of Array.isArray(c.nodos) ? c.nodos : []) {
      if (typeof n === "string" && validos.has(n) && !nodos.includes(n)) nodos.push(n);
      if (nodos.length >= MAX_NODOS_POR_CAMINO) break;
    }
    if (!titulo || nodos.length === 0) continue;
    caminos.push({ id: "abc"[caminos.length], titulo, descripcion, nodos });
  }
  return caminos;
}

export interface TareaPlanAnterior {
  texto: string;
  estado: ChecklistEstado;
  nota?: string;
}

export interface PlanAnteriorIA {
  etapas: Array<{ numero: number; titulo: string; tareas: TareaPlanAnterior[] }>;
}

const RE_ETAPA = /^##\s+Etapa\s+(\d+)\s*:\s*(.+)$/gm;

/**
 * El plan anterior como lo recibe el redactor (payload.plan_anterior, regla
 * 8-ter de SYSTEM_PLAN): sus etapas, con el título del markdown, y las tareas
 * de cada una con su estado (y la nota si la hay). null si no hay plan anterior.
 */
export function planAnteriorParaIA(
  md: string | null,
  items: Array<{ etapa: number; texto: string; estado: ChecklistEstado; nota?: string | null }>
): PlanAnteriorIA | null {
  if (!md || !md.trim()) return null;
  const titulos = new Map<number, string>();
  for (const m of md.matchAll(RE_ETAPA)) titulos.set(parseInt(m[1], 10), m[2].trim());
  const numeros = [...new Set([...titulos.keys(), ...items.map((i) => i.etapa)])].sort((a, b) => a - b);
  return {
    etapas: numeros.map((numero) => ({
      numero,
      titulo: titulos.get(numero) ?? "",
      tareas: items
        .filter((i) => i.etapa === numero)
        .map((i) => ({ texto: i.texto, estado: i.estado, ...(i.nota?.trim() ? { nota: i.nota.trim() } : {}) })),
    })),
  };
}

/** Una fila de checklist heredada, lista para insertarse bajo el plan nuevo. */
export interface FilaHeredada {
  etapa: number;
  orden: number;
  texto: string;
  destacado: boolean;
  estado: "hecho";
  completed_at: string | null;
  nota: string | null;
  heredado_de: string;
}

/**
 * Al replantear, lo marcado "me sigue sirviendo" pasa al plan nuevo COMO HECHO:
 * en la etapa 1, antes de las tareas nuevas (órdenes negativos: las derivadas
 * empiezan en 1), con su fecha de realización y su nota, y con `heredado_de`
 * apuntando a la original (migración 047) para no contarla dos veces.
 */
export function filasHeredadas(conserva: TareaCiclo[]): FilaHeredada[] {
  return conserva.map((t, i) => ({
    etapa: 1,
    orden: i - conserva.length,
    texto: t.texto,
    destacado: false,
    estado: "hecho",
    completed_at: t.completed_at ?? null,
    nota: t.nota ?? null,
    heredado_de: t.id,
  }));
}

/** Lo que la persona escribió o dictó al pedir el ciclo, tal cual (recortado
 * en los bordes): su historia al replantear; lo que contó y hacia dónde quiere
 * ir al profundizar. null si no escribió nada. */
export function relatoDeCiclo(ciclo: CicloSesion | null | undefined): string | null {
  if (!ciclo) return null;
  if (ciclo.tipo === "replantear") return ciclo.historia.trim() || null;
  const partes = [ciclo.detalles, ciclo.enfoque].map((p) => p?.trim()).filter((p): p is string => Boolean(p));
  return partes.length ? partes.join("\n") : null;
}
