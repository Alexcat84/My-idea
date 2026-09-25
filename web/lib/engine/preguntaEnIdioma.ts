/**
 * D3 (i18n F5): fuera del español, las preguntas del grafo las adapta la IA.
 * Las cacheadas (preguntas_cache.json) están en español; si una llega cruda a
 * una idea escrita en otro idioma, Haiku la expresa en ese idioma. Si la IA
 * falla, queda la cacheada: mejor una pregunta en español que ninguna.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_HAIKU, type UsoAcumulado } from "../costmeter";
import { SYSTEM_TRADUCIR_PREGUNTA } from "../prompts";

export async function preguntaEnIdioma(
  client: Anthropic,
  pregunta: string,
  idiomaSalida: string | null | undefined,
  acumulado: UsoAcumulado
): Promise<{ pregunta: string; acumulado: UsoAcumulado; traducida: boolean }> {
  if (!idiomaSalida || idiomaSalida === "es" || !pregunta.trim()) return { pregunta, acumulado, traducida: false };
  try {
    const r = await llamarClaude(client, SYSTEM_TRADUCIR_PREGUNTA, pregunta, MODEL_HAIKU, acumulado, {
      maxTokens: 200,
      componente: "turnos",
      idiomaSalida,
    });
    const texto = r.texto.trim();
    if (!texto) return { pregunta, acumulado: r.acumulado, traducida: false };
    return { pregunta: texto, acumulado: r.acumulado, traducida: true };
  } catch (e) {
    console.error("[preguntaEnIdioma] no se pudo adaptar; queda la cacheada:", e instanceof Error ? e.message : e);
    return { pregunta, acumulado, traducida: false };
  }
}
