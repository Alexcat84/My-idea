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
import { tituloDeNodo, type Grafo } from "./graph";

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
  /** Bloque 7 (28 sep 2026): preguntas que suponen un papel o una estructura que la ficha contradice o que la
   * persona no menciono (un jefe, recursos humanos, un equipo). Ausente en veredictos de antes. */
  desajustes_de_papel?: string[];
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
  muestreo?: number,
  /** Principio 1 (28 sep 2026): el contexto completo del proyecto y de la persona. */
  contexto: string | null = null,
  /** Tope por sesion (8 oct 2026): dentro de un plan, el techo del plan (presupuestoDelPlanUsd), no el de la entrevista. */
  presupuestoUsd?: number
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

  // Por el resolutor: el juez lee títulos, y un id crudo en su material lo
  // haría juzgar una sesión que no entiende.
  const titulo = (nid: string) => tituloDeNodo(nid, graph);
  const turnos = turnosDecision.map((d) => ({
    nodo: d.nodo_actual ? titulo(d.nodo_actual) : null,
    destino: d.decision.camino.map(titulo),
    es_salto: d.decision.es_salto,
    candidatos_locales: d.candidatos_locales.map(titulo),
    saltos_posibles: d.saltos_posibles.map((s) => ({ titulo: s.titulo, afinidad: s.afinidad })),
    respuesta_usuario: d.respuesta_usuario ?? null,
    razonamiento: d.razonamiento,
    pregunta: d.pregunta ?? null,
  }));
  // Bloque 7: las preguntas de la cache tal como se mostraron, junto a su base, para mirar papeles y fondo.
  const preguntasAdaptadas = decisiones
    .filter((d): d is Extract<EventoInterprete, { tipo: "adaptacion_pregunta" }> => d.tipo === "adaptacion_pregunta")
    .map((d) => ({ base: d.de, mostrada: d.a }));

  try {
    const r = await llamarClaude(client, SYSTEM_JUEZ_SESION, JSON.stringify({ turnos, preguntas_adaptadas: preguntasAdaptadas }), MODEL_HAIKU, acumulado, {
      maxTokens: 400,
      contexto,
      componente: "juez_sesion",
      presupuestoUsd,
    });
    const calidad = parsearJson<VeredictoJuez>(r.texto);
    return { calidad, acumulado: r.acumulado };
  } catch (e) {
    // AUD-09 M17: el juez es muestreado y su ausencia es honesta (null), pero
    // su caída deja rastro.
    console.error("[juez] no se pudo evaluar la sesión:", e);
    return { calidad: null, acumulado };
  }
}
