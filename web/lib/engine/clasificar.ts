/**
 * clasificar.ts - Fase 3.0: port de clasificar_entrada (Capa 1) en
 * prototipo_motor.py: texto libre -> (puerta_id, perfil_sesion).
 *
 * Divergencia deliberada: el CLI cae a un cuestionario cerrado
 * interactivo (preguntar_opcion, bloqueante) si la clasificacion con IA
 * falla. La web no tiene ese lujo -- no hay input() posible en una ruta
 * serverless -- asi que el respaldo no interactivo es la primera puerta
 * de la lista curada de 20 (misma logica de "mejor una eleccion
 * razonable que bloquear la sesion" que ya usa seleccionar_puerta_avanzada
 * en Python para su propio respaldo sin IA).
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_HAIKU, type UsoAcumulado } from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_CLASIFICACION } from "../prompts";
import type { Grafo } from "./graph";

export interface ResultadoClasificacion {
  puertaId: string;
  perfilSesion: string;
  acumulado: UsoAcumulado;
}

export async function clasificarEntrada(
  client: Anthropic,
  texto: string,
  entrySeeds: string[],
  graph: Grafo,
  acumulado: UsoAcumulado
): Promise<ResultadoClasificacion> {
  const puertas = entrySeeds.map((s) => ({
    id: s,
    fase: graph[s].fase_proyecto,
    titulo: graph[s].titulo_concepto,
    resumen: graph[s].resumen_teorico.slice(0, 200),
  }));

  try {
    const r = await llamarClaude(
      client,
      SYSTEM_CLASIFICACION,
      JSON.stringify({ texto_usuario: texto, puertas }),
      MODEL_HAIKU,
      acumulado,
      { maxTokens: 400, componente: "clasificacion" }
    );
    const data = parsearJson<{ puerta_id?: string; perfil_sesion?: string }>(r.texto);
    if (data.puerta_id && entrySeeds.includes(data.puerta_id)) {
      return { puertaId: data.puerta_id, perfilSesion: (data.perfil_sesion ?? "").trim(), acumulado: r.acumulado };
    }
    return { puertaId: entrySeeds[0], perfilSesion: "", acumulado: r.acumulado };
  } catch {
    return { puertaId: entrySeeds[0], perfilSesion: "", acumulado };
  }
}
