/**
 * reformuladorProteccion.ts — Mundos de protección (P2b): EL ANCLAJE DE LA
 * PREGUNTA.
 *
 * En un mundo de protección, la entrevista no debería preguntar en abstracto
 * ("¿qué riesgos ves en tu operación?") teniendo delante las actividades reales
 * de la persona. Esta pieza toma la pregunta que produjo el motor y la apunta a
 * una actividad concreta del snapshot.
 *
 * POR QUÉ VIVE AQUÍ Y NO EN UN PROMPT DEL MOTOR (verificado antes de escribirlo):
 * no existe un SYSTEM por mundo. Los doce SYSTEM_* de engine/prototipo_motor.py
 * son globales y los comparte toda entrevista del producto, el núcleo incluido;
 * y las preguntas de los turnos no las escribe un modelo, salen del caché del
 * grafo. Así que esto corre DESPUÉS del motor, solo en los tres mundos de
 * protección, y no cambia una coma de lo que ve el resto del producto.
 *
 * LAS TRES BARANDAS (del fundador, no negociables):
 *  (a) ANCLA, jamás cambia qué se pregunta. La intención metodológica de la
 *      pregunta del grafo sobrevive; si ninguna actividad aplica, vuelve tal
 *      cual. La baraja está en el prompt y la vigila un test de contrato.
 *  (b) FALLBACK declarado: llamada fallida o respuesta inválida → la pregunta
 *      cacheada tal cual. La entrevista JAMÁS se bloquea; el fallo deja síntoma.
 *  (c) Calidad plena (Sonnet siempre) dentro del presupuesto, con el costo
 *      MEDIDO y reportado.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { costoAcumuladoUsd, llamarClaude, MODEL, type UsoAcumulado } from "../costmeter";
import { SYSTEM_REFORMULADOR_PROTECCION } from "../prompts";

/** Una pregunta es una línea corta. Más allá de esto, lo que volvió no es una
 * pregunta anclada: es el modelo explicando teoría, y se descarta. */
const MAX_LARGO_PREGUNTA = 400;

export interface ResultadoAnclaje {
  /** La pregunta que se le muestra al usuario: la anclada, o la original. */
  pregunta: string;
  acumulado: UsoAcumulado;
  /** Costo REAL de esta llamada en dólares (baranda c: medido, no supuesto). */
  costoUsd: number;
  /** true si de verdad se ancló (para telemetría honesta: no toda pregunta se ancla). */
  anclada: boolean;
  /** Motivo si no se pudo anclar. null cuando no hubo fallo. */
  fallo: string | null;
}

/**
 * ¿Lo que volvió sirve como pregunta? Baraja (b): esto NO juzga si el anclaje
 * fue bueno (eso no se puede medir aquí), solo si tiene forma de pregunta. Una
 * respuesta idéntica a la original es VÁLIDA: es el camino declarado de "ninguna
 * actividad aplica".
 */
export function esPreguntaUsable(texto: string): boolean {
  const t = texto.trim();
  if (t.length === 0 || t.length > MAX_LARGO_PREGUNTA) return false;
  if (t.includes("```") || t.startsWith("{") || t.startsWith("[")) return false;
  // Un párrafo de varias líneas no es "UNA sola pregunta".
  if (t.split("\n").filter((l) => l.trim()).length > 2) return false;
  return true;
}

/**
 * Ancla una pregunta al snapshot. Nunca lanza: ante cualquier problema devuelve
 * la pregunta original, que es exactamente lo que el usuario habría visto sin
 * esta pieza.
 */
export async function anclarPregunta(
  client: Anthropic,
  pregunta: string,
  snapshotTexto: string | null,
  acumulado: UsoAcumulado,
  opts: { presupuestoUsd?: number } = {}
): Promise<ResultadoAnclaje> {
  const sinAnclar = (fallo: string | null): ResultadoAnclaje => ({
    pregunta,
    acumulado,
    costoUsd: 0,
    anclada: false,
    fallo,
  });
  if (!pregunta.trim()) return sinAnclar(null);
  if (!snapshotTexto || !snapshotTexto.trim()) return sinAnclar(null); // nada a lo que anclar

  const antes = costoAcumuladoUsd(acumulado);
  try {
    const r = await llamarClaude(
      client,
      SYSTEM_REFORMULADOR_PROTECCION,
      [snapshotTexto, "", "PREGUNTA A ANCLAR:", pregunta].join("\n"),
      // Baraja (c): calidad plena. Es la pregunta que la persona lee; degradarla
      // a un modelo menor abarata justo lo que se ve.
      MODEL,
      acumulado,
      { maxTokens: 300, componente: "anclaje_proteccion", presupuestoUsd: opts.presupuestoUsd ?? 5 }
    );
    const texto = r.texto.trim();
    if (!esPreguntaUsable(texto)) {
      return { ...sinAnclar("la reformulación no tenía forma de pregunta"), acumulado: r.acumulado };
    }
    return {
      pregunta: texto,
      acumulado: r.acumulado,
      costoUsd: costoAcumuladoUsd(r.acumulado) - antes,
      anclada: texto !== pregunta.trim(),
      fallo: null,
    };
  } catch (e) {
    return sinAnclar(e instanceof Error ? e.message : String(e));
  }
}

/**
 * El enganche de los dos sitios donde nace una pregunta de mundo (el arranque
 * del preview y cada turno). Parchea el resultado ENTERO, no solo el texto que
 * se responde: la pregunta pendiente y el historial anti-repetición se persisten
 * con la versión anclada, para que al reentrar el usuario vea lo mismo y el
 * motor no se repita contra un texto que nadie leyó.
 *
 * Solo actúa si el turno trae pregunta y la sesión lleva snapshot (es decir,
 * solo en los mundos de protección: nadie más lo lleva).
 */
export async function anclarResultadoTurno<
  R extends { tipo: string; pregunta?: string; estado: { snapshotNucleo: string | null; preguntaPendiente: string | null; ultimasPreguntas: string[] } }
>(
  client: Anthropic,
  resultado: R,
  acumulado: UsoAcumulado,
  opts: { presupuestoUsd?: number } = {}
): Promise<{ resultado: R; acumulado: UsoAcumulado; anclaje: ResultadoAnclaje | null }> {
  if (resultado.tipo !== "pregunta" || !resultado.pregunta || !resultado.estado.snapshotNucleo) {
    return { resultado, acumulado, anclaje: null };
  }
  const original = resultado.pregunta;
  const anclaje = await anclarPregunta(client, original, resultado.estado.snapshotNucleo, acumulado, opts);
  if (!anclaje.anclada) return { resultado, acumulado: anclaje.acumulado, anclaje };

  const ultimas = resultado.estado.ultimasPreguntas.map((q) => (q === original ? anclaje.pregunta : q));
  return {
    resultado: {
      ...resultado,
      pregunta: anclaje.pregunta,
      estado: { ...resultado.estado, preguntaPendiente: anclaje.pregunta, ultimasPreguntas: ultimas },
    },
    acumulado: anclaje.acumulado,
    anclaje,
  };
}
