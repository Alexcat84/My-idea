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
import { nombreDeMundo } from "./catalogoMundos";
import { listarProyectos } from "./db";
import { estadoEntrevista } from "./entrevistaAbierta";
import { etapaDeIdea } from "./etapaIdea";
import { fechaSello } from "./fechas";
import { esActivo, type ChecklistEstado } from "./dbContract";

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
  /** Fase 3.8: la idea ya es un proyecto realizado (se agrupa al final) */
  realizada: boolean;
  /** "87 días · de la chispa al proyecto" (solo realizadas) */
  resumenRealizada?: string;
}

export function nombreDeIdea(titulo: string | null, entradaOriginal: string): string {
  if (titulo && titulo.trim()) return titulo.trim();
  const palabras = entradaOriginal.trim().split(/\s+/).slice(0, 8).join(" ");
  return palabras.length < entradaOriginal.trim().length ? `${palabras}…` : palabras;
}

// El "espejo de packs_catalog" que vivia aqui era una COPIA de los nombres, y
// una copia se separa: bastaba un mundo nuevo para que esta pantalla lo llamara
// por su clave mientras las demas lo nombraban. Ahora se lee de la fuente.

export async function listarIdeasConEstado(supabase: SupabaseClient): Promise<Cinta[]> {
  const proyectos = await listarProyectos(supabase);
  if (proyectos.length === 0) return [];

  // RLS limita las consultas al usuario autenticado. El checklist puede no
  // existir aún (pre-migración 015): se tolera con lista vacía.
  const [{ data: sesiones }, { data: planes }, checklistRes] = await Promise.all([
    supabase.from("sessions").select("id, project_id, closed_at, estado_recorrido, dominio"),
    supabase.from("plans").select("session_id, etiqueta"),
    supabase.from("checklist_items").select("project_id, plan_id, dominio, estado, created_at, updated_at"),
  ]);
  const checklist = (checklistRes.error ? [] : (checklistRes.data ?? [])) as Array<{
    project_id: string;
    plan_id: string;
    dominio: string;
    estado: string;
    created_at: string;
    updated_at?: string | null;
  }>;
  // AUD-09 M42: la última acción de cada idea cuenta el trabajo en sus tareas
  // (marcar, mover fechas, anotar), que no toca projects.updated_at.
  const ultimaEnTareas = new Map<string, string>();
  for (const item of checklist) {
    const t = item.updated_at ?? item.created_at;
    const actual = ultimaEnTareas.get(item.project_id);
    if (!actual || t > actual) ultimaEnTareas.set(item.project_id, t);
  }

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
    // AUD-09 M01: las retiradas no cuentan en el total (la cuenta honesta de
    // dbContract.cuentaHonesta, "X de N activas").
    if (esActivo(item.estado as ChecklistEstado)) {
      r.total += 1;
      if (item.estado === "hecho") r.hechos += 1;
    }
    if (item.estado !== "pendiente") r.empezoAlguno = true;
    porDominio.set(item.dominio, r);
  }

  const proyectoDeSesion = new Map<string, string>();
  const entrevistaAbierta = new Set<string>();
  // AUD-09 M29: qué espera cada idea con entrevista abierta (la regla única).
  const esperaPlan = new Set<string>();
  // AUD-09 B10: qué clase de sesión está abierta (la regla única de la etapa).
  const explorandoNucleo = new Set<string>();
  const seguimientoAbierto = new Set<string>();
  for (const s of (sesiones ?? []) as Array<{
    id: string;
    project_id: string;
    closed_at: string | null;
    estado_recorrido: unknown;
  }>) {
    proyectoDeSesion.set(s.id, s.project_id);
    const abierta = estadoEntrevista(s);
    if (abierta) entrevistaAbierta.add(s.project_id);
    const deNucleo = !(s as { dominio?: string | null }).dominio || (s as { dominio?: string | null }).dominio === "core";
    if (abierta && deNucleo) {
      const esSeg = (s.estado_recorrido as { recorrido?: { esSeguimiento?: boolean } }).recorrido?.esSeguimiento === true;
      (esSeg ? seguimientoAbierto : explorandoNucleo).add(s.project_id);
    }
    if (abierta === "listo_para_plan") esperaPlan.add(s.project_id);
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

    const pensando = entrevistaAbierta.has(p.id);
    // AUD-09 M28: sin organizador no hay Claridad (su IA falló): se queda en la
    // Chispa y se dice "Sin ordenar", no "Con claridad".
    const ordenada = etiquetas.has("organizador");
    // AUD-09 B10: la regla única de la etapa (la misma del encabezado de la idea).
    const etapa = etapaDeIdea({
      conPlan,
      enObra,
      explorandoNucleo: explorandoNucleo.has(p.id),
      seguimientoAbierto: seguimientoAbierto.has(p.id),
      ordenada,
    });

    const chips: ChipCinta[] = [];
    if (etapa === 5 && core) {
      chips.push({ texto: `Manos a la Obra · ${core.hechos}/${core.total}`, tono: "verde" });
      for (const [dominio, r] of porDominio) {
        if (dominio === "core") continue;
        chips.push({ texto: `${nombreDeMundo(dominio)} · ${r.hechos}/${r.total}`, tono: "verde" });
      }
    } else if (pensando) {
      chips.push({ texto: "En exploración", tono: "azul" });
    } else if (conPlan) {
      chips.push({ texto: "Con plan", tono: "azul" });
    } else {
      chips.push({ texto: ordenada ? "Con claridad" : "Sin ordenar", tono: "neutro" });
    }

    // Fase 4.3.1: la pista ANCLA la idea en el calendario (fechaSello) en vez
    // de solo "hace X" — el fundador lo pidió para poder ordenar y ubicar el
    // historial. "una pregunta te espera" cuando el motor tiene el turno.
    // Canon 01: la meta line COMBINA la invitación con el sello, no una u otra
    // ("Una pregunta te espera · última acción ayer 21:26").
    const tareas = ultimaEnTareas.get(p.id);
    const ultimaAccion = tareas && tareas > p.updated_at ? tareas : p.updated_at;
    const pista = pensando
      ? esperaPlan.has(p.id)
        ? `Tu plan está listo para armarse · última acción ${fechaSello(ultimaAccion)}`
        : `Una pregunta te espera · última acción ${fechaSello(ultimaAccion)}`
      : `última acción · ${fechaSello(ultimaAccion)}`;

    // Fase 3.8: una idea realizada es un Proyecto — se agrupa al final.
    const realizadaAt = (p as { realizada_at?: string | null }).realizada_at ?? null;
    const realizada = Boolean(realizadaAt);
    const resumenRealizada = realizadaAt
      ? `realizada ${fechaSello(realizadaAt)} · ${Math.max(0, Math.round((new Date(realizadaAt).getTime() - new Date(p.created_at).getTime()) / 86_400_000))} días de la chispa al proyecto`
      : undefined;

    return {
      id: p.id,
      nombre: nombreDeIdea(p.titulo, p.entrada_original),
      estado,
      actualizado: ultimaAccion,
      etapa,
      pensando,
      chips,
      pista,
      realizada,
      resumenRealizada,
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
