/**
 * puertaAvanzada.ts — Fase 3.3: port de candidatos_seguimiento (línea 2366)
 * y seleccionar_puerta_avanzada (línea 2398) de engine/prototipo_motor.py,
 * función por función. La Capa 1 avanzada de --seguir: elige CUALQUIER nodo
 * del grafo aún no cubierto como puerta de la sesión de seguimiento,
 * priorizando fase del proyecto, familias sin cubrir y afinidad de palabras
 * clave con el mensaje nuevo + estado_vivo.
 *
 * Divergencia deliberada (misma que clasificar.ts): si la llamada al modelo
 * falla, el respaldo no interactivo es el candidato de mayor puntaje, y en
 * última instancia la primera semilla — jamás bloquear una ruta serverless.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_HAIKU, type UsoAcumulado } from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_PUERTA_AVANZADA } from "../prompts";
import type { Grafo } from "./graph";
import { tokensCosecha } from "./tokens";

const ORDEN_FASES: Record<string, number> = { ideacion: 0, validacion: 1, planificacion: 2, ejecucion: 3 };

/** Port de candidatos_seguimiento: nodos de cualquier parte del grafo que el
 * proyecto aún no cubrió, puntuados y ordenados, tope 30. */
export function candidatosSeguimiento(
  mensajeNuevo: string,
  estadoVivo: string | null,
  faseActual: string,
  families: Record<string, string>,
  graph: Grafo,
  cubiertos: Set<string>,
  tope = 30
): string[] {
  const faseIdx = ORDEN_FASES[faseActual] ?? 0;
  const conteoFam: Record<string, number> = {};
  for (const nid of cubiertos) {
    const f = families[nid] ?? "general";
    conteoFam[f] = (conteoFam[f] ?? 0) + 1;
  }
  const contextoTokens = tokensCosecha(`${mensajeNuevo ?? ""} ${estadoVivo ?? ""}`);

  const puntaje = (nid: string): number => {
    const n = graph[nid];
    let p = 0;
    const fNodo = ORDEN_FASES[n.fase_proyecto ?? ""] ?? 0;
    if (fNodo === faseIdx) p += 5;
    else if (fNodo === faseIdx + 1) p += 3;
    const fam = families[nid] ?? "general";
    if (fam !== "general" && (conteoFam[fam] ?? 0) === 0) p += 6;
    if (contextoTokens.size > 0) {
      const textoNodo = `${n.titulo_concepto ?? ""} ${(n.condiciones_activacion ?? []).join(" ")}`;
      for (const t of tokensCosecha(textoNodo)) if (contextoTokens.has(t)) p += 1;
    }
    return p;
  };

  return Object.keys(graph)
    .filter((nid) => !cubiertos.has(nid))
    .sort((a, b) => puntaje(b) - puntaje(a))
    .slice(0, tope);
}

export interface ResultadoPuertaAvanzada {
  puertaId: string;
  perfilSesion: string;
  acumulado: UsoAcumulado;
}

/** Port de seleccionar_puerta_avanzada: candidatos → Haiku elige la puerta
 * (validada contra la lista); respaldos en cascada sin bloquear. */
export async function seleccionarPuertaAvanzada(
  client: Anthropic,
  mensajeNuevo: string,
  estadoVivo: string | null,
  faseActual: string,
  families: Record<string, string>,
  graph: Grafo,
  cubiertos: Set<string>,
  entrySeeds: string[],
  acumulado: UsoAcumulado
): Promise<ResultadoPuertaAvanzada> {
  const candidatosIds = candidatosSeguimiento(mensajeNuevo, estadoVivo, faseActual, families, graph, cubiertos);
  if (candidatosIds.length > 0) {
    const opciones = candidatosIds.map((nid) => {
      const n = graph[nid];
      return {
        id: nid,
        titulo: n.titulo_concepto,
        fase: n.fase_proyecto,
        resumen: (n.resumen_teorico ?? "").slice(0, 150),
        condiciones_activacion: (n.condiciones_activacion ?? []).slice(0, 2),
      };
    });
    const ctx = { estado_vivo: estadoVivo, mensaje_nuevo: mensajeNuevo, candidatos: opciones };
    try {
      const r = await llamarClaude(client, SYSTEM_PUERTA_AVANZADA, JSON.stringify(ctx), MODEL_HAIKU, acumulado, {
        maxTokens: 400,
        componente: "clasificacion",
      });
      const data = parsearJson<{ puerta_id?: string; perfil_sesion?: string }>(r.texto);
      if (data.puerta_id && candidatosIds.includes(data.puerta_id)) {
        return { puertaId: data.puerta_id, perfilSesion: (data.perfil_sesion ?? "").trim(), acumulado: r.acumulado };
      }
      // puerta_id fuera de los candidatos: mismo respaldo que el except de Python.
      return { puertaId: candidatosIds[0], perfilSesion: estadoVivo ?? "", acumulado: r.acumulado };
    } catch {
      return { puertaId: candidatosIds[0], perfilSesion: estadoVivo ?? "", acumulado };
    }
  }
  return { puertaId: entrySeeds[0], perfilSesion: estadoVivo ?? "", acumulado };
}
