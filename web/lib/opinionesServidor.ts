/**
 * Las opiniones contra la base (tabla opiniones, migración 051). SOLO servidor: usa la service role, así que cada
 * función recibe el id de una cuenta que la ruta YA verificó y filtra por él. El contexto interno (etiqueta, ciclo,
 * mundo, nodos) se arma aquí, nunca en el navegador, y nunca vuelve al navegador.
 * Lo puro (cuándo preguntar, qué se acepta) vive en lib/opiniones.ts.
 */
import { createAdminClient } from "@/lib/supabase/admin";
import { ETIQUETAS_CICLO, type OpinionMotivo, type OpinionTipo, type OpinionValoracion } from "./dbContract";
import { numeroDeCiclo, tipoDePlan, type EventoOpinion, type FilaHistorial, type FilaOpinion, type FiltrosPanel } from "./opiniones";

export interface ContextoInterno {
  etiqueta?: string;
  ciclo?: number;
  mundo?: string;
  nodos?: string[];
}

export interface EventoResuelto {
  evento: EventoOpinion;
  proyectoId: string;
  contexto: ContextoInterno;
}

/** Las opiniones anteriores de la cuenta (lo que decide si se vuelve a preguntar). */
export async function historialDe(userId: string): Promise<FilaHistorial[]> {
  const { data, error } = await createAdminClient()
    .from("opiniones")
    .select("tipo, objeto_id, created_at")
    .eq("user_id", userId)
    .order("created_at", { ascending: false })
    .limit(500);
  if (error) throw new Error(error.message);
  return (data ?? []) as FilaHistorial[];
}

/** Los planes de ciclo de una idea (para el número de ciclo y el último plan). */
async function planesDeCiclo(proyectoId: string): Promise<Array<{ id: string; etiqueta: string; dominio: string; created_at: string; session_id: string }>> {
  const admin = createAdminClient();
  const { data: sesiones, error: e1 } = await admin.from("sessions").select("id").eq("project_id", proyectoId);
  if (e1) throw new Error(e1.message);
  const ids = (sesiones ?? []).map((s) => s.id as string);
  if (ids.length === 0) return [];
  const { data, error } = await admin
    .from("plans")
    .select("id, etiqueta, dominio, created_at, session_id")
    .in("session_id", ids)
    .in("etiqueta", [...ETIQUETAS_CICLO]);
  if (error) throw new Error(error.message);
  return (data ?? []) as Array<{ id: string; etiqueta: string; dominio: string; created_at: string; session_id: string }>;
}

/** El plan de una entrevista de ESTA cuenta, como evento de opinión. null si la sesión no es suya, no tiene plan o su
 * plan no se pregunta (la Claridad). */
export async function eventoDePlan(userId: string, sesionId: string): Promise<EventoResuelto | null> {
  const admin = createAdminClient();
  const { data: sesion, error: e1 } = await admin
    .from("sessions")
    .select("id, project_id, ruta:estado_recorrido->recorrido->ruta")
    .eq("id", sesionId)
    .eq("user_id", userId)
    .maybeSingle();
  if (e1) throw new Error(e1.message);
  if (!sesion) return null;
  const { data: plan, error: e2 } = await admin
    .from("plans")
    .select("id, etiqueta, dominio, created_at")
    .eq("session_id", sesionId)
    .order("created_at", { ascending: false })
    .limit(1)
    .maybeSingle();
  if (e2) throw new Error(e2.message);
  if (!plan) return null;
  const tipo = tipoDePlan(plan.etiqueta as string, plan.dominio as string);
  if (!tipo) return null;
  const proyectoId = sesion.project_id as string;
  const ciclos = await planesDeCiclo(proyectoId);
  const ruta = Array.isArray(sesion.ruta) ? (sesion.ruta as unknown[]).filter((n): n is string => typeof n === "string") : [];
  return {
    evento: { tipo, objetoId: plan.id as string, creadoAt: plan.created_at as string },
    proyectoId,
    contexto: {
      etiqueta: plan.etiqueta as string,
      ciclo: numeroDeCiclo(ciclos, { id: plan.id as string, dominio: plan.dominio as string, created_at: plan.created_at as string }),
      mundo: (plan.dominio as string) || "core",
      nodos: ruta,
    },
  };
}

/** "¿Qué tal va tu idea?" para una idea de ESTA cuenta. null si la idea no es suya. */
export async function eventoDeSeguimiento(userId: string, proyectoId: string): Promise<EventoResuelto | null> {
  const { data: proyecto, error } = await createAdminClient()
    .from("projects")
    .select("id")
    .eq("id", proyectoId)
    .eq("user_id", userId)
    .maybeSingle();
  if (error) throw new Error(error.message);
  if (!proyecto) return null;
  const ciclos = (await planesDeCiclo(proyectoId)).filter((p) => (p.dominio || "core") === "core");
  const ultimo = ciclos.sort((a, b) => b.created_at.localeCompare(a.created_at))[0] ?? null;
  return {
    evento: { tipo: "seguimiento", objetoId: proyectoId, ultimoPlanAt: ultimo?.created_at ?? null },
    proyectoId,
    contexto: ultimo ? { etiqueta: ultimo.etiqueta, ciclo: ciclos.length, mundo: "core" } : { mundo: "core" },
  };
}

export interface NuevaOpinion {
  userId: string;
  tipo: OpinionTipo;
  objetoId: string | null;
  proyectoId: string | null;
  valoracion: OpinionValoracion | null;
  motivo: OpinionMotivo | null;
  texto: string | null;
  idioma: string;
  contexto: ContextoInterno;
}

/** Guarda una opinión. "repetida" si ese plan ya tenía la suya (índice único de la 051): la ruta la da por hecha. */
export async function guardarOpinion(o: NuevaOpinion): Promise<{ id: string } | "repetida"> {
  const { data, error } = await createAdminClient()
    .from("opiniones")
    .insert({
      user_id: o.userId,
      tipo: o.tipo,
      objeto_id: o.objetoId,
      proyecto_id: o.proyectoId,
      valoracion: o.valoracion,
      motivo: o.motivo,
      texto: o.texto,
      idioma: o.idioma,
      contexto: o.contexto,
    })
    .select("id")
    .single();
  if (error) {
    if (error.code === "23505") return "repetida";
    throw new Error(error.message);
  }
  return { id: (data as { id: string }).id };
}

/** Después de "Malo", la persona añade el motivo o el texto: se completa SU opinión "malo" de la última hora. */
export async function completarOpinion(userId: string, id: string, motivo: OpinionMotivo | null, texto: string | null, ahora = new Date()): Promise<boolean> {
  const { data, error } = await createAdminClient()
    .from("opiniones")
    .update({ motivo, texto, updated_at: ahora.toISOString() })
    .eq("id", id)
    .eq("user_id", userId)
    .eq("valoracion", "malo")
    .gte("created_at", new Date(ahora.getTime() - 3_600_000).toISOString())
    .select("id");
  if (error) throw new Error(error.message);
  return (data ?? []).length > 0;
}

/** Las opiniones de TODAS las cuentas, para el panel del fundador (la ruta ya comprobó que es el fundador). */
export async function listarOpiniones(f: FiltrosPanel): Promise<FilaOpinion[]> {
  let q = createAdminClient()
    .from("opiniones")
    .select("id, created_at, tipo, valoracion, motivo, texto, idioma, proyecto_id, objeto_id, contexto")
    .order("created_at", { ascending: false })
    .limit(f.limite ?? 2000);
  if (f.tipo) q = q.eq("tipo", f.tipo);
  if (f.valoracion === "sin") q = q.is("valoracion", null);
  else if (f.valoracion) q = q.eq("valoracion", f.valoracion);
  const { data, error } = await q;
  if (error) throw new Error(error.message);
  return (data ?? []) as FilaOpinion[];
}
