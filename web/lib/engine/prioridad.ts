/**
 * CONSTRUCCION 4 (decision del fundador, 28 sep 2026, docs/REGLAS_DE_LA_CASA.md): la PRIORIDAD declarada es una regla
 * en CODIGO, no un consejo en el prompt. Si la persona declaro una prioridad y entre los candidatos (siguientes, saltos,
 * puertas) hay alguno que la atiende, no se puede elegir uno que no la atienda, salvo que haga falta un paso previo: eso
 * se permite y el motivo queda escrito.
 *
 * "Atiende" = su coseno contra la prioridad en el indice semantico llega al umbral de la brujula (MIN_SCORE_SALTO,
 * 0,30, calibrado para consulta contra nodo; ver compass.ts). Si ningun candidato llega, manda el camino local.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { MIN_SCORE_SALTO, puntuadorContra, type NodoConDominio } from "../compass";
import type { UsoAcumulado } from "../costmeter";
import { consultaAlEspanol } from "./consultaAlEspanol";

export const UMBRAL_PRIORIDAD = MIN_SCORE_SALTO;

export type Puntuador = (id: string) => number | null;

/** Los candidatos que atienden la prioridad, del que mas al que menos (empate: id), sin repetir. */
export function queAtienden(ids: string[], puntuar: Puntuador | null, umbral = UMBRAL_PRIORIDAD): string[] {
  if (!puntuar) return [];
  return [...new Set(ids)]
    .map((id) => ({ id, s: puntuar(id) }))
    .filter((x): x is { id: string; s: number } => x.s !== null && x.s >= umbral)
    .sort((a, b) => b.s - a.s || a.id.localeCompare(b.id))
    .map((x) => x.id);
}

/** true si elegir `destino` desatiende la prioridad: hay quien la atiende, el destino no, y no hay paso previo escrito. */
export function violaPrioridad(destino: string, atienden: string[], pasoPrevio: string | null | undefined): boolean {
  return atienden.length > 0 && !atienden.includes(destino) && !(pasoPrevio && pasoPrevio.trim());
}

/** El puntuador de la prioridad declarada. El indice esta en español: en una idea en otro idioma, la prioridad se
 * traduce antes (la misma consulta que la brujula). null si no hay prioridad o la brujula no esta disponible.
 * `contexto`: el contexto completo de la sesion (Principio 1, 28 sep 2026), obligatorio como en toda llamada a la IA
 * (guarda lib/contextoEnTodaLlamada.test.ts); null solo si la sesion es anterior a la memoria. */
export async function puntuadorDePrioridad(
  client: Anthropic,
  prioridadTexto: string | null | undefined,
  idiomaSalida: string | null,
  acumulado: UsoAcumulado,
  graph: Record<string, NodoConDominio>,
  contexto: string | null
): Promise<{ puntuar: Puntuador | null; acumulado: UsoAcumulado }> {
  const texto = (prioridadTexto ?? "").trim();
  if (!texto) return { puntuar: null, acumulado };
  const t = await consultaAlEspanol(client, texto, idiomaSalida, acumulado, contexto);
  return { puntuar: await puntuadorContra(t.consulta, graph), acumulado: t.acumulado };
}
