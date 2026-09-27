/**
 * El remedio de F1 (i18n F5; docs/i18n/F1_BUSCADOR.md): el índice semántico
 * (Voyage) está hecho con el español de los nodos. Antes de buscar, la
 * consulta de una idea escrita en otro idioma se traduce al español con Haiku.
 * Si la traducción falla, se busca con el original y queda registrado.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_HAIKU, type UsoAcumulado } from "../costmeter";
import { SYSTEM_CONSULTA_AL_ESPANOL } from "../prompts";

export async function consultaAlEspanol(
  client: Anthropic,
  texto: string,
  idiomaIdea: string | null | undefined,
  acumulado: UsoAcumulado
): Promise<{ consulta: string; acumulado: UsoAcumulado; fallo: boolean }> {
  if (!idiomaIdea || idiomaIdea === "es" || !texto.trim()) return { consulta: texto, acumulado, fallo: false };
  try {
    const r = await llamarClaude(client, SYSTEM_CONSULTA_AL_ESPANOL, texto, MODEL_HAIKU, acumulado, {
      maxTokens: 400,
      componente: "turnos",
    });
    const consulta = r.texto.trim();
    if (!consulta) throw new Error("traducción vacía");
    return { consulta, acumulado: r.acumulado, fallo: false };
  } catch (e) {
    console.error("[consultaAlEspanol] se busca con el original:", e instanceof Error ? e.message : e);
    return { consulta: texto, acumulado, fallo: true };
  }
}
