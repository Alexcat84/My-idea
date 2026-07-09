/**
 * juezSesion.ts - Fase 3.1 (caja de vidrio): port exacto de
 * evaluar_calidad_sesion en prototipo_motor.py. Juez de sesion muestreado
 * (Haiku, ~$0.003/sesion): revisa la bitacora decision_turno de la
 * sesion (candidatos locales, saltos_posibles con sus scores, la
 * decision tomada, la respuesta del usuario y el razonamiento del
 * interprete en cada paso) y devuelve una señal de triage para revision
 * humana despues -- NUNCA bloquea ni decide nada.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_HAIKU, type UsoAcumulado } from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_JUEZ_SESION } from "../prompts";
import type { EventoInterprete } from "./interprete";
import type { Grafo } from "./graph";

/** Fraccion de sesiones que pasan por el juez. Default 1.0 (100%) durante
 * la beta -- se baja via env var cuando ya no haga falta revisar cada
 * sesion. Mismo nombre de env var que el espejo Python. */
function leerMuestreo(): number {
  const raw = process.env.JUEZ_SESION_MUESTREO;
  if (!raw) return 1.0;
  const valor = Number(raw);
  return Number.isFinite(valor) ? valor : 1.0;
}

export interface VeredictoJuez {
  pertinencia_transiciones: 1 | 2 | 3 | 4 | 5;
  repeticion_detectada: boolean;
  señales_fuera_de_material: string[];
  comentario: string;
}

/** Devuelve {calidad: null, acumulado sin cambios} si no se muestreo esta
 * sesion, si no hay eventos decision_turno que evaluar, o si la llamada
 * falla -- la ausencia de veredicto no es un problema: es simplemente
 * una sesion sin revisar. */
export async function evaluarCalidadSesion(
  client: Anthropic,
  decisiones: Array<EventoInterprete | Record<string, unknown>>,
  graph: Grafo,
  acumulado: UsoAcumulado,
  muestreo?: number
): Promise<{ calidad: VeredictoJuez | null; acumulado: UsoAcumulado }> {
  const tasaMuestreo = muestreo ?? leerMuestreo();
  if (Math.random() >= tasaMuestreo) {
    return { calidad: null, acumulado };
  }
  const turnosDecision = decisiones.filter(
    (d): d is Extract<EventoInterprete, { tipo: "decision_turno" }> => d.tipo === "decision_turno"
  );
  if (turnosDecision.length === 0) {
    return { calidad: null, acumulado };
  }

  const titulo = (nid: string) => graph[nid]?.titulo_concepto ?? nid;
  const turnos = turnosDecision.map((d) => ({
    nodo: d.nodo_actual ? titulo(d.nodo_actual) : null,
    destino: d.decision.camino.map(titulo),
    es_salto: d.decision.es_salto,
    candidatos_locales: d.candidatos_locales.map(titulo),
    saltos_posibles: d.saltos_posibles.map((s) => ({ titulo: s.titulo, afinidad: s.afinidad })),
    respuesta_usuario: d.respuesta_usuario ?? null,
    razonamiento: d.razonamiento,
  }));

  try {
    const r = await llamarClaude(client, SYSTEM_JUEZ_SESION, JSON.stringify({ turnos }), MODEL_HAIKU, acumulado, {
      maxTokens: 400,
      componente: "juez_sesion",
    });
    const calidad = parsearJson<VeredictoJuez>(r.texto);
    return { calidad, acumulado: r.acumulado };
  } catch {
    return { calidad: null, acumulado };
  }
}
