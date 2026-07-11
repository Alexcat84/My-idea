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

/** Chip de estado de la cinta (canon 3.6): el verde ejecuta, el azul piensa. */
export interface ChipCinta {
  texto: string;
  tono: "verde" | "azul" | "neutro";
}

export interface Cinta {
  id: string;
  nombre: string;
  estado: EstadoIdea;
  actualizado: string; // ISO
  /** 1-5 según la verdad persistida (nunca teatro) */
  etapa: number;
  /** entrevista abierta: el punto actual gira */
  pensando: boolean;
  /** chip principal + chips de progreso por dominio si hay mundos */
  chips: ChipCinta[];
  /** línea secundaria ("una pregunta te espera" / "última acción hace 2 días") */
  pista: string;
}

export function nombreDeIdea(titulo: string | null, entradaOriginal: string): string {
  if (titulo && titulo.trim()) return titulo.trim();
  const palabras = entradaOriginal.trim().split(/\s+/).slice(0, 8).join(" ");
  return palabras.length < entradaOriginal.trim().length ? `${palabras}…` : palabras;
}

/** Nombre canon de cada mundo para los chips (espejo de packs_catalog). */
const NOMBRE_MUNDO: Record<string, string> = {
  quality: "Calidad y Confianza",
  health_safety: "Seguridad y Personas",
  environmental: "Ambiente y Futuro",
};

export async function listarIdeasConEstado(supabase: SupabaseClient): Promise<Cinta[]> {
  const proyectos = await listarProyectos(supabase);
  if (proyectos.length === 0) return [];

  // RLS limita las consultas al usuario autenticado. El checklist puede no
  // existir aún (pre-migración 015): se tolera con lista vacía.
  const [{ data: sesiones }, { data: planes }, checklistRes] = await Promise.all([
    supabase.from("sessions").select("id, project_id, closed_at, estado_recorrido"),
    supabase.from("plans").select("session_id, etiqueta"),
    supabase.from("checklist_items").select("project_id, plan_id, dominio, estado, created_at"),
  ]);
  const checklist = (checklistRes.error ? [] : (checklistRes.data ?? [])) as Array<{
    project_id: string;
    plan_id: string;
    dominio: string;
    estado: string;
    created_at: string;
  }>;

  // Progreso del plan VIGENTE por proyecto y dominio (el último por fecha):
  // los checklists de planes anteriores son Historia, no el estado actual.
  const planVigente = new Map<string, { plan_id: string; created_at: string }>();
  for (const item of checklist) {
    const clave = `${item.project_id}|${item.dominio}`;
    const actual = planVigente.get(clave);
    if (!actual || item.created_at > actual.created_at) {
      planVigente.set(clave, { plan_id: item.plan_id, created_at: item.created_at });
    }
  }
  const progreso = new Map<string, Map<string, { total: number; hechos: number; empezoAlguno: boolean }>>();
  for (const item of checklist) {
    if (planVigente.get(`${item.project_id}|${item.dominio}`)?.plan_id !== item.plan_id) continue;
    if (!progreso.has(item.project_id)) progreso.set(item.project_id, new Map());
    const porDominio = progreso.get(item.project_id)!;
    const r = porDominio.get(item.dominio) ?? { total: 0, hechos: 0, empezoAlguno: false };
    r.total += 1;
    if (item.estado === "hecho") r.hechos += 1;
    if (item.estado !== "pendiente") r.empezoAlguno = true;
    porDominio.set(item.dominio, r);
  }

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

    // Etapa canónica y chips (canon 3.6): solo lecturas de lo persistido.
    const conPlan = etiquetas.has("inicial") || etiquetas.has("completo") || etiquetas.has("seguimiento");
    const porDominio = progreso.get(p.id) ?? new Map<string, { total: number; hechos: number; empezoAlguno: boolean }>();
    const core = porDominio.get("core");
    const enObra = Boolean(core?.empezoAlguno) || etiquetas.has("seguimiento");

    let etapa: number;
    const pensando = entrevistaAbierta.has(p.id);
    if (enObra) etapa = 5;
    else if (conPlan) etapa = 4;
    else if (pensando) etapa = 3;
    else etapa = 2; // hay proyecto ⇒ hubo Chispa; con organizador es Claridad

    const chips: ChipCinta[] = [];
    if (etapa === 5 && core) {
      chips.push({ texto: `Manos a la Obra · ${core.hechos}/${core.total}`, tono: "verde" });
      for (const [dominio, r] of porDominio) {
        if (dominio === "core") continue;
        chips.push({ texto: `${NOMBRE_MUNDO[dominio] ?? dominio} · ${r.hechos}/${r.total}`, tono: "verde" });
      }
    } else if (pensando) {
      chips.push({ texto: "En exploración", tono: "azul" });
    } else if (conPlan) {
      chips.push({ texto: "Con plan", tono: "azul" });
    } else {
      chips.push({ texto: "Con claridad", tono: "neutro" });
    }

    const pista = pensando ? "una pregunta te espera" : `última acción ${haceCuanto(p.updated_at)}`;

    return {
      id: p.id,
      nombre: nombreDeIdea(p.titulo, p.entrada_original),
      estado,
      actualizado: p.updated_at,
      etapa,
      pensando,
      chips,
      pista,
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
