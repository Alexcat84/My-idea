/**
 * db.ts - Fase 3.0: port de la porcion de engine/db.py que las rutas de
 * API necesitan (proyectos, sesiones, planes). A diferencia del CLI, no
 * hay modo --offline aqui: la web SIEMPRE tiene Supabase. El cliente se
 * recibe por parametro (nunca un singleton propio) porque cada ruta debe
 * usar el cliente RLS-scoped de la request (lib/supabase/server.ts), que
 * ya sabe quien es el usuario autenticado via cookies -- las politicas
 * RLS de projects/sessions/plans (auth.uid() = user_id) hacen el resto.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import type { NumerosProyecto } from "./calculadora";
import type { UsoAcumulado } from "./costmeter";
import type { ModoRuta, PlanEtiqueta, ProjectNodeTipo, SessionTipo } from "./dbContract";
import type { EstadoRecorrido } from "./engine/recorrido";
import type { EstadoReporte } from "./engine/reporteFlow";

export const FASES = ["ideacion", "validacion", "planificacion", "ejecucion"] as const;
export type Fase = (typeof FASES)[number];

export interface Proyecto {
  id: string;
  user_id: string;
  titulo: string | null;
  entrada_original: string;
  estado_vivo: string | null;
  fase_actual: Fase;
  session_count: number;
  status: "active" | "archived";
  tipo_oferta?: string | null;
  unidad_venta?: string | null;
  numeros_proyecto?: NumerosProyecto;
  numeros_descartados?: unknown;
  estado_reporte?: EstadoReportePersistido | null;
  created_at: string;
  updated_at: string;
}

/** Estado resumible de la mini-entrevista de POST /api/project/[id]/report
 * (projects.estado_reporte, migration 010) entre una pregunta y la
 * siguiente. numeros_proyecto ya vive en su propia columna (fuente de
 * verdad, se re-lee y se re-escribe en cada paso, igual que Python), asi
 * que aqui solo hace falta el progreso de la mini-entrevista en si mas el
 * acumulado de costo (tope propio PRESUPUESTO_REPORTE_USD). */
export interface EstadoReportePersistido {
  estado: EstadoReporte;
  acumulado: UsoAcumulado;
}

export interface RutaNodo {
  node_id: string;
  tipo: ModoRuta;
}

export interface Sesion {
  id: string;
  project_id: string;
  user_id: string;
  session_position: number;
  tipo: SessionTipo;
  mensaje_entrada: string;
  puerta_entrada: string | null;
  ruta: RutaNodo[];
  costo_usd: number;
  presupuesto_excedido: boolean;
  presupuesto_usd?: number | null;
  decisiones?: unknown[] | null;
  calidad?: Record<string, unknown> | null;
  estado_recorrido: EstadoSesionPersistido | null;
  created_at: string;
  closed_at: string | null;
}

/** Todo lo que hace falta para resumir un turno: el estado del bucle de
 * entrevista (recorrido) MAS el acumulado de costo real (uso, no solo el
 * total en dolares) -- llamarClaude necesita el desglose de tokens por
 * modelo para decidir si el presupuesto de la sesion ya se supero, asi
 * que no alcanza con persistir costo_usd. */
export interface EstadoSesionPersistido {
  recorrido: EstadoRecorrido;
  acumulado: UsoAcumulado;
}

function ahora(): string {
  return new Date().toISOString();
}

export async function crearProyecto(supabase: SupabaseClient, userId: string, entradaOriginal: string): Promise<string> {
  const { data, error } = await supabase
    .from("projects")
    .insert({ user_id: userId, entrada_original: entradaOriginal, fase_actual: "ideacion" })
    .select("id")
    .single();
  if (error) throw error;
  return (data as { id: string }).id;
}

export async function obtenerProyecto(supabase: SupabaseClient, projectId: string): Promise<Proyecto | null> {
  const { data, error } = await supabase.from("projects").select("*").eq("id", projectId).limit(1);
  if (error) throw error;
  const filas = data as Proyecto[];
  return filas.length > 0 ? filas[0] : null;
}

/** Lista los proyectos del usuario autenticado (RLS ya filtra por
 * user_id), mas recientes primero -- reemplaza a --seguir/necesitar saber
 * el project_id de memoria: la UI muestra esta lista para retomar. */
export async function listarProyectos(supabase: SupabaseClient): Promise<Proyecto[]> {
  const { data, error } = await supabase.from("projects").select("*").order("updated_at", { ascending: false });
  if (error) throw error;
  return data as Proyecto[];
}

export async function actualizarProyecto(
  supabase: SupabaseClient,
  projectId: string,
  campos: Record<string, unknown>
): Promise<void> {
  const { error } = await supabase
    .from("projects")
    .update({ ...campos, updated_at: ahora() })
    .eq("id", projectId);
  if (error) throw error;
}

export async function crearSesion(
  supabase: SupabaseClient,
  userId: string,
  projectId: string,
  tipo: SessionTipo,
  mensajeEntrada: string,
  puertaEntrada: string | null = null
): Promise<string> {
  const proyecto = await obtenerProyecto(supabase, projectId);
  const posicion = (proyecto?.session_count ?? 0) + 1;
  const { data, error } = await supabase
    .from("sessions")
    .insert({
      project_id: projectId,
      user_id: userId,
      session_position: posicion,
      tipo,
      mensaje_entrada: mensajeEntrada,
      puerta_entrada: puertaEntrada,
    })
    .select("id")
    .single();
  if (error) throw error;
  return (data as { id: string }).id;
}

export async function cerrarSesion(
  supabase: SupabaseClient,
  projectId: string,
  sessionId: string,
  rutaConModos: RutaNodo[],
  costoUsd: number,
  presupuestoExcedido: boolean,
  costoDesglose?: Record<string, number>,
  presupuestoUsd?: number,
  decisiones?: unknown[],
  calidad?: unknown
): Promise<void> {
  const campos: Record<string, unknown> = {
    ruta: rutaConModos,
    costo_usd: costoUsd,
    presupuesto_excedido: presupuestoExcedido,
    closed_at: ahora(),
  };
  if (costoDesglose && Object.keys(costoDesglose).length > 0) {
    campos.costo_desglose = costoDesglose;
  }
  // Hotfix v2.2.1: presupuesto vigente con el que esta sesion realmente
  // corrio (--reporte usa PRESUPUESTO_REPORTE_USD en vez del default de
  // sesion, asi que puede diferir entre sesiones).
  if (presupuestoUsd !== undefined) {
    campos.presupuesto_usd = presupuestoUsd;
  }
  // Fase 3.1 (caja de vidrio): bitacora completa de eventos de la sesion
  // (decision_turno por turno, fallback_auto, etc.), acumulada en
  // estado_recorrido turno a turno y persistida de una sola vez aqui.
  if (decisiones && decisiones.length > 0) {
    campos.decisiones = decisiones;
  }
  // Fase 3.1: veredicto del juez de sesion muestreado, o ausente si esta
  // sesion no se muestreo.
  if (calidad) {
    campos.calidad = calidad;
  }
  const { error } = await supabase.from("sessions").update(campos).eq("id", sessionId);
  if (error) throw error;
  const proyecto = await obtenerProyecto(supabase, projectId);
  const nuevoConteo = (proyecto?.session_count ?? 0) + 1;
  await actualizarProyecto(supabase, projectId, { session_count: nuevoConteo });
}

export async function obtenerSesion(supabase: SupabaseClient, sessionId: string): Promise<Sesion | null> {
  const { data, error } = await supabase.from("sessions").select("*").eq("id", sessionId).limit(1);
  if (error) throw error;
  const filas = data as Sesion[];
  return filas.length > 0 ? filas[0] : null;
}

/** Persiste el estado resumible del bucle de entrevista entre turnos
 * (sessions.estado_recorrido, migration 009). No cierra la sesion. */
export async function guardarEstadoSesion(
  supabase: SupabaseClient,
  sessionId: string,
  estado: EstadoSesionPersistido
): Promise<void> {
  const { error } = await supabase.from("sessions").update({ estado_recorrido: estado }).eq("id", sessionId);
  if (error) throw error;
}

/** Motor v2.1: mergea lo detectado ESTA sesion dentro de
 * projects.numeros_proyecto (solo pisa los campos que esta sesion SI
 * detecto; el resto del historial numerico del proyecto queda intacto). */
export async function mergeNumerosProyecto(
  supabase: SupabaseClient,
  projectId: string,
  numerosDetectadosSesion: Record<string, unknown> | null | undefined
): Promise<void> {
  if (!numerosDetectadosSesion || Object.keys(numerosDetectadosSesion).length === 0) return;
  const proyecto = await obtenerProyecto(supabase, projectId);
  const numeros = { ...((proyecto?.numeros_proyecto as Record<string, unknown>) ?? {}), ...numerosDetectadosSesion };
  await actualizarProyecto(supabase, projectId, { numeros_proyecto: numeros });
}

/** Motor v2.2: persiste tipo_oferta/unidad_venta si esta sesion detecto
 * algo nuevo (nunca pisa con null lo que ya estaba guardado de una
 * sesion anterior). */
export async function mergeTipoOferta(
  supabase: SupabaseClient,
  projectId: string,
  tipoOfertaSesion: string | null | undefined,
  unidadVentaSesion: string | null | undefined
): Promise<void> {
  if (!tipoOfertaSesion && !unidadVentaSesion) return;
  const campos: Record<string, unknown> = {};
  if (tipoOfertaSesion) campos.tipo_oferta = tipoOfertaSesion;
  if (unidadVentaSesion) campos.unidad_venta = unidadVentaSesion;
  await actualizarProyecto(supabase, projectId, campos);
}

export async function nodosCubiertos(supabase: SupabaseClient, projectId: string): Promise<Set<string>> {
  const { data, error } = await supabase.from("project_nodes").select("node_id").eq("project_id", projectId);
  if (error) throw error;
  return new Set((data as Array<{ node_id: string }>).map((row) => row.node_id));
}

export interface NodoConTipo {
  node_id: string;
  tipo: ProjectNodeTipo;
}

/** Port de registrar_nodos: ignora duplicados (un nodo cuenta una sola
 * vez por proyecto, sin importar en que sesion se cubrio primero). */
export async function registrarNodos(
  supabase: SupabaseClient,
  projectId: string,
  sessionId: string,
  nodosConTipo: NodoConTipo[]
): Promise<void> {
  const yaCubiertos = await nodosCubiertos(supabase, projectId);
  const nuevos = nodosConTipo.filter((n) => !yaCubiertos.has(n.node_id));
  if (nuevos.length === 0) return;
  const { error } = await supabase.from("project_nodes").insert(
    nuevos.map((n) => ({ project_id: projectId, session_id: sessionId, node_id: n.node_id, tipo: n.tipo }))
  );
  if (error) throw error;
}

export async function guardarPlan(
  supabase: SupabaseClient,
  userId: string,
  sessionId: string,
  etiqueta: PlanEtiqueta,
  contenidoMd: string,
  conceptosUsados: number,
  familiasCubiertas: string[]
): Promise<void> {
  const { error } = await supabase.from("plans").insert({
    session_id: sessionId,
    user_id: userId,
    etiqueta,
    contenido_md: contenidoMd,
    conceptos_usados: conceptosUsados,
    familias_cubiertas: familiasCubiertas,
  });
  if (error) throw error;
}
