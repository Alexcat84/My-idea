/**
 * analyticsEntrada.ts — Fase 4.0 §6: cargar de Supabase lo que analytics.ts
 * necesita, UNA sola vez y en un solo sitio. La leen los DOS espejos de la
 * misma agua: el Análisis (para el humano) y el follow (para el motor). Sin
 * esto, cada uno arma su propia entrada y la regla "prohibido duplicar la
 * lógica del tiempo" se rompe por la puerta de atrás.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import type { EntradaAnalytics, ItemAnalytics, MundoAnalytics, PlanCoreAnalytics } from "./analytics";
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
  // Fase 4.2: los planes de los MUNDOS, con su dominio — un mundo es un
  // subproyecto y tiene sus propios ciclos (su plan original + cada follow).
  const planesMundo = planes
    .filter((p) => !esCore(p.dominio))
    .map((p) => ({
      id: p.id,
      etiqueta: p.etiqueta,
      created_at: p.created_at,
      baseline_confirmada_at: p.baseline_confirmada_at,
      dominio: p.dominio as string,
    }));
  const organizador = planes.find((p) => esCore(p.dominio) && p.etiqueta === "organizador");

  // no_aplica_motivo llega con la 030: se reintenta sin ella si aún no se
  // aplicó, para no romper el Análisis ni el follow. Patrón de project_unlocks.
  const COLS_ITEMS = "plan_id, dominio, etapa, estado, destacado, texto, completed_at, fecha_base, fecha_base_original";
  const conMotivo = await supabase
    .from("checklist_items")
    .select(`${COLS_ITEMS}, no_aplica_motivo`)
    .eq("project_id", projectId);
  const itemsRaw = conMotivo.error
    ? (await supabase.from("checklist_items").select(COLS_ITEMS).eq("project_id", projectId)).data
    : conMotivo.data;
  // Fase 4.1 (V3b): ya NO se excluyen los mundos. La entrada los lleva CON su
  // dominio; analytics decide que capa los usa (la universal los ignora para no
  // mover el ritmo del viaje principal; el desglose de cumplimiento los cuenta).
  const items: ItemAnalytics[] = ((itemsRaw ?? []) as Array<ItemAnalytics & { dominio: string | null }>)
    .map((i) => ({
      plan_id: i.plan_id,
      dominio: i.dominio,
      etapa: i.etapa,
      estado: i.estado,
      destacado: i.destacado,
      texto: i.texto,
      completed_at: i.completed_at,
      fecha_base: i.fecha_base,
      fecha_base_original: i.fecha_base_original,
      no_aplica_motivo: (i as { no_aplica_motivo?: string | null }).no_aplica_motivo ?? null,
    }));

  // project_unlocks puede no existir pre-016: se tolera con lista vacía.
  // Fase 4.2: completado_at/cierre_motivo llegan con la 026; si la migración
  // aún no está aplicada, el select entero falla — se reintenta sin esas dos
  // columnas y los mundos se leen como abiertos (que es lo que son).
  let mundos: MundoAnalytics[] = [];
  try {
    const { data, error } = await supabase
      .from("project_unlocks")
      .select("dominio, unlocked_at, completado_at, cierre_motivo")
      .eq("project_id", projectId);
    if (!error) mundos = (data ?? []) as MundoAnalytics[];
    else {
      const { data: previo } = await supabase
        .from("project_unlocks")
        .select("dominio, unlocked_at")
        .eq("project_id", projectId);
      mundos = (previo ?? []) as MundoAnalytics[];
    }
  } catch {
    mundos = [];
  }

  return {
    proyectoCreatedAt: proyecto.created_at,
    realizadaAt: proyecto.realizada_at ?? null,
    organizadorAt: organizador?.created_at ?? null,
    planesCore,
    planesMundo,
    items,
    mundos,
    modoCamino: (proyecto.modo_camino as "ritmo" | "fechas" | null) ?? null,
    cierreMotivo: proyecto.cierre_motivo ?? null,
    ahora,
  };
}
