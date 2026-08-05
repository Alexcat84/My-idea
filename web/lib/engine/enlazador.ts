/**
 * enlazador.ts — Mundos de protección (P2): EL ENLACE.
 *
 * Cuando nace el plan de un mundo de protección, esta SEGUNDA llamada lee el
 * plan ya escrito y el snapshot del núcleo, y dice qué respuesta protege a qué
 * actividad, con la detección que la originó y su severidad en palabras.
 *
 * Por qué una segunda llamada y no estructura dentro del plan (adjudicado por el
 * fundador y el auditor): el plan se escribe en STREAMING y el usuario lo está
 * mirando; meterle una gramática nueva ensuciaría lo que lee y obligaría a tocar
 * el parser que sostiene TODOS los planes de la casa. Y el tercer camino, enlazar
 * por coincidencia de texto, quedó rechazado con nombre: adivinar no es enlazar.
 * Es exactamente el patrón de la estimación de F1, que ya lleva semanas vivo.
 *
 * CERO INVENCIÓN, y aquí se paga en el validador:
 *  - un índice de actividad que no existe NO se convierte en "sistémico": se
 *    descarta el enlace entero, porque decir "protege al negocio" cuando el
 *    modelo quiso apuntar a algo concreto es inventarle una intención;
 *  - `null` sí es un valor declarado: la respuesta protege al negocio entero;
 *  - la severidad fuera del vocabulario cerrado queda en null, campo por campo;
 *  - si la llamada falla entera, todos los enlaces quedan null y **el plan
 *    JAMÁS se bloquea** (fallback declarado, con síntoma persistido).
 */
import type Anthropic from "@anthropic-ai/sdk";
import { DOLOR, PROBABILIDAD, type Dolor, type Probabilidad } from "../dbContract";
import { costoAcumuladoUsd, llamarClaude, MODEL, type UsoAcumulado } from "../costmeter";
import { SYSTEM_ENLACE_PROTECCION } from "../prompts";
import type { SnapshotNucleo } from "./snapshotProyecto";

/** Lo que se persiste por cada respuesta del plan de protección. */
export interface EnlaceProteccion {
  /** uuid del ítem del núcleo protegido; null = sistémico (el negocio entero). */
  protege_item: string | null;
  deteccion: string | null;
  probabilidad: Probabilidad | null;
  dolor: Dolor | null;
}

/** Tope de la detección: es una frase, no un párrafo. */
const MAX_DETECCION = 200;

interface EnlaceCrudo {
  item_orden: number;
  deteccion: string;
  protege_indice: number | null;
  probabilidad: string | null;
  dolor: string | null;
}

/** Parsea el array JSON del enlazador. Robusto a fences y a prosa alrededor;
 * ignora lo que no tenga la forma mínima (no lo arregla, lo deja fuera). */
export function parsearEnlaces(texto: string): EnlaceCrudo[] {
  const m = texto.match(/\[[\s\S]*\]/);
  if (!m) return [];
  let arr: unknown;
  try {
    arr = JSON.parse(m[0]);
  } catch {
    return [];
  }
  if (!Array.isArray(arr)) return [];
  const out: EnlaceCrudo[] = [];
  for (const el of arr) {
    if (!el || typeof el !== "object") continue;
    const o = el as Record<string, unknown>;
    if (typeof o.item_orden !== "number" || !Number.isInteger(o.item_orden)) continue;
    const protege =
      typeof o.protege_indice === "number" && Number.isInteger(o.protege_indice) ? o.protege_indice : null;
    out.push({
      item_orden: o.item_orden,
      deteccion: typeof o.deteccion === "string" ? o.deteccion : "",
      // Se distingue "vino null" de "vino basura": el segundo caso lo caza
      // `validarEnlaces`, que descarta el enlace en vez de fingir un sistémico.
      protege_indice: o.protege_indice === null ? null : protege === null ? Number.NaN : protege,
      probabilidad: typeof o.probabilidad === "string" ? o.probabilidad : null,
      dolor: typeof o.dolor === "string" ? o.dolor : null,
    });
  }
  return out;
}

export interface ResultadoValidacion {
  /** Por posición del ítem del plan del mundo (0..N-1). */
  enlaces: (EnlaceProteccion | null)[];
  /** Cuántos enlaces se descartaron por apuntar a una actividad inexistente. */
  descartados: number;
}

/**
 * Valida los enlaces crudos contra el snapshot y el vocabulario cerrado, y
 * traduce el índice de actividad a su uuid. El mapa índice→id vive AQUÍ, en el
 * servidor: al modelo nunca se le mandan uuid.
 */
export function validarEnlaces(
  crudos: EnlaceCrudo[],
  snapshot: SnapshotNucleo,
  totalItems: number
): ResultadoValidacion {
  const porIndice = new Map(snapshot.actividades.map((a) => [a.indice, a.id]));
  const enlaces: (EnlaceProteccion | null)[] = new Array(totalItems).fill(null);
  let descartados = 0;

  for (const c of crudos) {
    const pos = c.item_orden - 1; // el prompt numera desde 1
    if (pos < 0 || pos >= totalItems) {
      descartados += 1;
      continue;
    }
    let protege: string | null = null;
    if (c.protege_indice !== null) {
      const id = Number.isNaN(c.protege_indice) ? undefined : porIndice.get(c.protege_indice);
      if (!id) {
        // Índice inventado: se descarta el enlace ENTERO. Convertirlo en
        // sistémico sería ponerle al modelo una intención que no tuvo.
        descartados += 1;
        continue;
      }
      protege = id;
    }
    const deteccion = c.deteccion.trim().slice(0, MAX_DETECCION);
    enlaces[pos] = {
      protege_item: protege,
      deteccion: deteccion || null,
      probabilidad: (PROBABILIDAD as readonly string[]).includes(c.probabilidad ?? "")
        ? (c.probabilidad as Probabilidad)
        : null,
      dolor: (DOLOR as readonly string[]).includes(c.dolor ?? "") ? (c.dolor as Dolor) : null,
    };
  }
  return { enlaces, descartados };
}

/** El mensaje de usuario: las dos listas numeradas que el prompt espera. */
export function construirUserTextEnlace(
  respuestas: Array<{ texto: string; etapa: number }>,
  snapshot: SnapshotNucleo
): string {
  const actividades = snapshot.actividades.map((a) => `#${a.indice} · ${a.titulo}`);
  const items = respuestas.map((r, i) => `#${i + 1} · E${r.etapa} · ${r.texto}`);
  return [
    "ACTIVIDADES DEL NÚCLEO (a esto puede proteger):",
    ...actividades,
    "",
    "RESPUESTAS DEL PLAN DE PROTECCIÓN (una salida por cada una):",
    ...items,
  ].join("\n");
}

export interface ResultadoEnlace {
  enlaces: (EnlaceProteccion | null)[];
  acumulado: UsoAcumulado;
  /** Costo REAL de esta llamada, en dólares. El fundador lo quiere medido. */
  costoUsd: number;
  descartados: number;
  /** Motivo del fallo si no se pudo enlazar (el plan sigue igual). */
  fallo: string | null;
}

/**
 * Enlaza el plan de protección recién nacido. Nunca lanza: si algo falla, los
 * enlaces salen todos null y el llamador guarda el plan igual, con su síntoma.
 */
export async function enlazarPlanProteccion(
  client: Anthropic,
  respuestas: Array<{ texto: string; etapa: number }>,
  snapshot: SnapshotNucleo,
  acumulado: UsoAcumulado,
  opts: { presupuestoUsd?: number } = {}
): Promise<ResultadoEnlace> {
  const vacio = (fallo: string | null): ResultadoEnlace => ({
    enlaces: new Array(respuestas.length).fill(null),
    acumulado,
    costoUsd: 0,
    descartados: 0,
    fallo,
  });
  if (respuestas.length === 0) return vacio(null);
  if (snapshot.actividades.length === 0) {
    // Sin actividades no hay nada a lo que enlazar. No es un error: es que este
    // plan no tiene núcleo vigente que proteger, y se dice en vez de llamar.
    return vacio("sin actividades del núcleo que enlazar");
  }

  const antes = costoAcumuladoUsd(acumulado);
  try {
    const r = await llamarClaude(
      client,
      SYSTEM_ENLACE_PROTECCION,
      construirUserTextEnlace(respuestas, snapshot),
      MODEL,
      acumulado,
      {
        maxTokens: Math.min(4000, 300 + respuestas.length * 60),
        componente: "enlace_proteccion",
        presupuestoUsd: opts.presupuestoUsd ?? 5,
      }
    );
    const { enlaces, descartados } = validarEnlaces(parsearEnlaces(r.texto), snapshot, respuestas.length);
    return {
      enlaces,
      acumulado: r.acumulado,
      costoUsd: costoAcumuladoUsd(r.acumulado) - antes,
      descartados,
      fallo: null,
    };
  } catch (e) {
    return vacio(e instanceof Error ? e.message : String(e));
  }
}
