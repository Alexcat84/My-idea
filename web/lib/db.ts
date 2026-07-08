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
  numeros_proyecto?: unknown;
  numeros_descartados?: unknown;
  created_at: string;
  updated_at: string;
}

export interface RutaNodo {
  node_id: string;
  tipo: "conversado" | "silencioso";
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
  tipo: "gratuito" | "inicial" | "seguimiento",
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
  costoDesglose?: Record<string, number>
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
  const { error } = await supabase.from("sessions").update(campos).eq("id", sessionId);
  if (error) throw error;
  const proyecto = await obtenerProyecto(supabase, projectId);
  const nuevoConteo = (proyecto?.session_count ?? 0) + 1;
  await actualizarProyecto(supabase, projectId, { session_count: nuevoConteo });
}

export async function guardarPlan(
  supabase: SupabaseClient,
  userId: string,
  sessionId: string,
  etiqueta: "organizador" | "inicial" | "completo" | "seguimiento",
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
