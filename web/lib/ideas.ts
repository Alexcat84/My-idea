/**
 * ideas.ts — Fase 3.2: la vista "Mis ideas" (cintas) del brief 2.2.
 * Deriva el mini-estado de cada idea a partir de lo ya persistido
 * (sessions + plans), sin columnas nuevas: el estado es una LECTURA de
 * la verdad existente, no un campo que pueda desincronizarse.
 *
 * Precedencia: una entrevista abierta gana (es el estado accionable:
 * "continúa donde quedaste"); luego seguimiento > con plan > organizada.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import { listarProyectos } from "./db";

export type EstadoIdea = "Organizada" | "En entrevista" | "Con plan" | "En seguimiento";

export interface Cinta {
  id: string;
  nombre: string;
  estado: EstadoIdea;
  actualizado: string; // ISO
}

export function nombreDeIdea(titulo: string | null, entradaOriginal: string): string {
  if (titulo && titulo.trim()) return titulo.trim();
  const palabras = entradaOriginal.trim().split(/\s+/).slice(0, 8).join(" ");
  return palabras.length < entradaOriginal.trim().length ? `${palabras}…` : palabras;
}

export async function listarIdeasConEstado(supabase: SupabaseClient): Promise<Cinta[]> {
  const proyectos = await listarProyectos(supabase);
  if (proyectos.length === 0) return [];

  // RLS limita ambas consultas al usuario autenticado.
  const [{ data: sesiones }, { data: planes }] = await Promise.all([
    supabase.from("sessions").select("id, project_id, closed_at, estado_recorrido"),
    supabase.from("plans").select("session_id, etiqueta"),
  ]);

  const proyectoDeSesion = new Map<string, string>();
  const entrevistaAbierta = new Set<string>();
  for (const s of (sesiones ?? []) as Array<{
    id: string;
    project_id: string;
    closed_at: string | null;
    estado_recorrido: unknown;
  }>) {
    proyectoDeSesion.set(s.id, s.project_id);
    if (!s.closed_at && s.estado_recorrido) entrevistaAbierta.add(s.project_id);
  }

  const etiquetasPorProyecto = new Map<string, Set<string>>();
  for (const p of (planes ?? []) as Array<{ session_id: string; etiqueta: string }>) {
    const projectId = proyectoDeSesion.get(p.session_id);
    if (!projectId) continue;
    if (!etiquetasPorProyecto.has(projectId)) etiquetasPorProyecto.set(projectId, new Set());
    etiquetasPorProyecto.get(projectId)!.add(p.etiqueta);
  }

  return proyectos.map((p) => {
    const etiquetas = etiquetasPorProyecto.get(p.id) ?? new Set<string>();
    let estado: EstadoIdea;
    if (entrevistaAbierta.has(p.id)) estado = "En entrevista";
    else if (etiquetas.has("seguimiento")) estado = "En seguimiento";
    else if (etiquetas.has("inicial") || etiquetas.has("completo")) estado = "Con plan";
    else estado = "Organizada";
    return {
      id: p.id,
      nombre: nombreDeIdea(p.titulo, p.entrada_original),
      estado,
      actualizado: p.updated_at,
    };
  });
}

/** "hace 2 días", "hace 3 h", "ahora mismo" — español, sin librerías. */
export function haceCuanto(iso: string): string {
  const ms = Date.now() - new Date(iso).getTime();
  const min = Math.floor(ms / 60_000);
  if (min < 2) return "ahora mismo";
  if (min < 60) return `hace ${min} min`;
  const h = Math.floor(min / 60);
  if (h < 24) return `hace ${h} h`;
  const d = Math.floor(h / 24);
  if (d < 30) return d === 1 ? "ayer" : `hace ${d} días`;
  const meses = Math.floor(d / 30);
  return meses === 1 ? "hace un mes" : `hace ${meses} meses`;
}
