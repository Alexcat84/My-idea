/**
 * GET /api/project/[id]/analisis — Fase 3.8 §5/§6: todo el análisis del
 * proyecto calculado de lo persistido (CERO LLM, cero costo por render).
 * Alimenta la pantalla Análisis (capa universal + cumplimiento) y la
 * Celebración (mismos números + el timeline con acciones).
 *
 * Devuelve: nombre, modo_camino, realizada_at, tiene_baseline, analytics
 * (hitos sin acciones), hitosCelebracion (con acciones), informe_md.
 */
import { NextResponse } from "next/server";
import {
  calcularAnalytics,
  construirHitos,
  informeMarkdown,
  type EntradaAnalytics,
  type ItemAnalytics,
  type PlanCoreAnalytics,
} from "@/lib/analytics";
import { obtenerProyecto } from "@/lib/db";
import { nombreDeIdea } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

const ETIQUETAS_CICLO = ["inicial", "completo", "seguimiento"];
const esCore = (dominio: string | null | undefined) => !dominio || dominio === "core";

export async function GET(_request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
  }

  const { data: sesiones } = await supabase
    .from("sessions")
    .select("id")
    .eq("project_id", projectId);
  const idsSesiones = ((sesiones ?? []) as Array<{ id: string }>).map((s) => s.id);

  const { data: planesRaw } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("id, etiqueta, created_at, baseline_confirmada_at, dominio")
        .in("session_id", idsSesiones)
        .order("created_at", { ascending: true })
    : { data: [] };
  type FilaPlan = {
    id: string;
    etiqueta: string;
    created_at: string;
    baseline_confirmada_at: string | null;
    dominio: string | null;
  };
  const planes = (planesRaw ?? []) as FilaPlan[];
  const planesCore: PlanCoreAnalytics[] = planes
    .filter((p) => esCore(p.dominio) && ETIQUETAS_CICLO.includes(p.etiqueta))
    .map((p) => ({
      id: p.id,
      etiqueta: p.etiqueta,
      created_at: p.created_at,
      baseline_confirmada_at: p.baseline_confirmada_at,
    }));
  const organizador = planes.find((p) => esCore(p.dominio) && p.etiqueta === "organizador");

  const { data: itemsRaw } = await supabase
    .from("checklist_items")
    .select("plan_id, dominio, etapa, estado, destacado, texto, completed_at, fecha_base, fecha_base_original")
    .eq("project_id", projectId);
  const items: ItemAnalytics[] = ((itemsRaw ?? []) as Array<ItemAnalytics & { dominio: string | null }>)
    .filter((i) => esCore(i.dominio))
    .map((i) => ({
      plan_id: i.plan_id,
      etapa: i.etapa,
      estado: i.estado,
      destacado: i.destacado,
      texto: i.texto,
      completed_at: i.completed_at,
      fecha_base: i.fecha_base,
      fecha_base_original: i.fecha_base_original,
    }));

  let mundos: Array<{ dominio: string; unlocked_at: string }> = [];
  try {
    const { data, error } = await supabase.from("project_unlocks").select("dominio, unlocked_at").eq("project_id", projectId);
    if (!error) mundos = (data ?? []) as Array<{ dominio: string; unlocked_at: string }>;
  } catch {
    mundos = [];
  }

  const ahora = new Date().toISOString();
  const entrada: EntradaAnalytics = {
    proyectoCreatedAt: proyecto.created_at,
    realizadaAt: proyecto.realizada_at ?? null,
    organizadorAt: organizador?.created_at ?? null,
    planesCore,
    items,
    mundos,
    ahora,
  };

  const analytics = calcularAnalytics(entrada);
  const nombre = nombreDeIdea(proyecto.titulo, proyecto.entrada_original);

  return NextResponse.json({
    nombre,
    modo_camino: proyecto.modo_camino ?? null,
    realizada_at: proyecto.realizada_at ?? null,
    tiene_baseline: analytics.cumplimiento !== null,
    analytics,
    hitosCelebracion: construirHitos(entrada, ahora, true),
    informe_md: informeMarkdown(nombre, analytics),
  });
}
