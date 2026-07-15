/**
 * analyticsEntrada.ts — Fase 4.0 §6: cargar de Supabase lo que analytics.ts
 * necesita, UNA sola vez y en un solo sitio. La leen los DOS espejos de la
 * misma agua: el Análisis (para el humano) y el follow (para el motor). Sin
 * esto, cada uno arma su propia entrada y la regla "prohibido duplicar la
 * lógica del tiempo" se rompe por la puerta de atrás.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import type { EntradaAnalytics, ItemAnalytics, PlanCoreAnalytics } from "./analytics";
import type { Proyecto } from "./db";

const ETIQUETAS_CICLO = ["inicial", "completo", "seguimiento"];
const esCore = (dominio: string | null | undefined) => !dominio || dominio === "core";

export async function cargarEntradaAnalytics(
  supabase: SupabaseClient,
  projectId: string,
  proyecto: Proyecto,
  ahora = new Date().toISOString()
): Promise<EntradaAnalytics> {
  const { data: sesiones } = await supabase.from("sessions").select("id").eq("project_id", projectId);
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

  // project_unlocks puede no existir pre-016: se tolera con lista vacía.
  let mundos: Array<{ dominio: string; unlocked_at: string }> = [];
  try {
    const { data, error } = await supabase
      .from("project_unlocks")
      .select("dominio, unlocked_at")
      .eq("project_id", projectId);
    if (!error) mundos = (data ?? []) as Array<{ dominio: string; unlocked_at: string }>;
  } catch {
    mundos = [];
  }

  return {
    proyectoCreatedAt: proyecto.created_at,
    realizadaAt: proyecto.realizada_at ?? null,
    organizadorAt: organizador?.created_at ?? null,
    planesCore,
    items,
    mundos,
    modoCamino: (proyecto.modo_camino as "ritmo" | "fechas" | null) ?? null,
    ahora,
  };
}
