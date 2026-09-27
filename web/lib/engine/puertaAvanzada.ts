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
import { esOfrecible, type Grafo } from "./graph";
import { tokensCosecha } from "./tokens";
import type { EventoInterprete } from "./interprete";
import { queAtienden, violaPrioridad, type Puntuador } from "./prioridad";

/** Cuantos nodos que atienden la prioridad entran a los candidatos aunque el puntaje de siempre no los traiga. */
const MAX_ATIENDEN_EXTRA = 8;

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
  tope = 30,
  dominiosDesbloqueados: string[] | null = null
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
    .filter((nid) => !cubiertos.has(nid) && esOfrecible(nid, graph, dominiosDesbloqueados))
    .sort((a, b) => puntaje(b) - puntaje(a))
    .slice(0, tope);
}

export interface ResultadoPuertaAvanzada {
  puertaId: string;
  perfilSesion: string;
  acumulado: UsoAcumulado;
  /** Construccion 4: lo que la prioridad decidio en la puerta (rechazo corregido o paso previo). */
  eventos: EventoInterprete[];
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
  acumulado: UsoAcumulado,
  dominiosDesbloqueados: string[] | null = null,
  /** Principio 1 (28 sep 2026): el contexto completo del proyecto y de la persona. */
  contexto: string | null = null,
  /** Construccion 4 (28 sep 2026): la prioridad declarada manda (null = sin prioridad o sin brujula). */
  puntuarPrioridad: Puntuador | null = null
): Promise<ResultadoPuertaAvanzada> {
  const PUERTA = "(puerta de seguimiento)";
  const deSiempre = candidatosSeguimiento(
    mensajeNuevo,
    estadoVivo,
    faseActual,
    families,
    graph,
    cubiertos,
    undefined,
    dominiosDesbloqueados
  );
  // Los que atienden la prioridad entran aunque el puntaje de siempre no los traiga, y van primero.
  const atiendenTodos = puntuarPrioridad
    ? queAtienden(
        Object.keys(graph).filter((nid) => !cubiertos.has(nid) && esOfrecible(nid, graph, dominiosDesbloqueados)),
        puntuarPrioridad
      ).slice(0, MAX_ATIENDEN_EXTRA)
    : [];
  const candidatosIds = [...new Set([...atiendenTodos, ...deSiempre])];
  const atienden = queAtienden(candidatosIds, puntuarPrioridad);
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
    const ctx = {
      estado_vivo: estadoVivo,
      mensaje_nuevo: mensajeNuevo,
      candidatos: opciones,
      ...(atienden.length > 0 ? { candidatos_que_atienden_prioridad: atienden } : {}),
    };
    const respaldo = atienden[0] ?? candidatosIds[0];
    try {
      const r = await llamarClaude(client, SYSTEM_PUERTA_AVANZADA, JSON.stringify(ctx), MODEL_HAIKU, acumulado, {
        maxTokens: 400,
        contexto,
        componente: "clasificacion",
      });
      const data = parsearJson<{ puerta_id?: string; perfil_sesion?: string; paso_previo?: string | null }>(r.texto);
      if (data.puerta_id && candidatosIds.includes(data.puerta_id)) {
        const perfilSesion = (data.perfil_sesion ?? "").trim();
        const pasoPrevio = data.paso_previo ? String(data.paso_previo).trim() || null : null;
        if (violaPrioridad(data.puerta_id, atienden, pasoPrevio)) {
          // Una sola llamada aqui: la puerta se corrige en codigo al candidato que mejor atiende la prioridad.
          return {
            puertaId: atienden[0],
            perfilSesion,
            acumulado: r.acumulado,
            eventos: [{ tipo: "prioridad_rechazo", nodo_actual: PUERTA, destino: data.puerta_id, atienden }],
          };
        }
        const eventos: EventoInterprete[] =
          pasoPrevio && atienden.length > 0 && !atienden.includes(data.puerta_id)
            ? [{ tipo: "prioridad_paso_previo", nodo_actual: PUERTA, destino: data.puerta_id, motivo: pasoPrevio, atienden }]
            : [];
        return { puertaId: data.puerta_id, perfilSesion, acumulado: r.acumulado, eventos };
      }
      // puerta_id fuera de los candidatos: el respaldo (el que mejor atiende la prioridad, o el primero).
      return { puertaId: respaldo, perfilSesion: estadoVivo ?? "", acumulado: r.acumulado, eventos: [] };
    } catch {
      return { puertaId: respaldo, perfilSesion: estadoVivo ?? "", acumulado, eventos: [] };
    }
  }
  return { puertaId: entrySeeds[0], perfilSesion: estadoVivo ?? "", acumulado, eventos: [] };
}
