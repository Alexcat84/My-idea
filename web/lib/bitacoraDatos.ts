/**
 * bitacoraDatos.ts — el CARGADOR de la bitácora del cliente (Fase 4.8): junta
 * de Supabase las fuentes que el lector puro (bitacoraCliente) necesita y
 * devuelve las entradas ya ordenadas. Lo comparten la ruta del documento
 * (.md/PDF) y la ruta JSON de la página en vivo, para que ambas cuenten la
 * MISMA historia. Cero motor, cero créditos.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import catalogo from "./assets/packs_catalog.json";
import {
  construirBitacora,
  type EntradaBitacora,
  type EventoBita,
  type PlanBita,
  type SesionBita,
} from "./bitacoraCliente";

interface ProyectoMin {
  created_at: string;
  realizada_at?: string | null;
}

export async function cargarEntradasBitacora(
  supabase: SupabaseClient,
  projectId: string,
  proyecto: ProyectoMin,
  nombre: string
): Promise<EntradaBitacora[]> {
  const packs = (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs;
  const nombreMundo = (dominio: string) => packs.find((p) => p.clave === dominio)?.nombre ?? dominio;

  const { data: sesionesRaw } = await supabase
    .from("sessions")
    .select("id, created_at, tipo, dominio")
    .eq("project_id", projectId);
  const sesiones = (sesionesRaw ?? []) as Array<SesionBita & { id: string }>;
  const idsSesiones = sesiones.map((s) => s.id);

  const { data: planesRaw } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("etiqueta, created_at, dominio, baseline_confirmada_at")
        .in("session_id", idsSesiones)
    : { data: [] };
  const planes = (planesRaw ?? []) as PlanBita[];

  const { data: itemsRaw } = await supabase
    .from("checklist_items")
    .select("id, texto, completed_at, dominio")
    .eq("project_id", projectId);

  let eventos: EventoBita[] = [];
  try {
    const { data, error } = await supabase
      .from("project_bitacora")
      .select("tipo, payload, created_at")
      .eq("project_id", projectId);
    if (!error) eventos = (data ?? []) as EventoBita[];
  } catch {
    eventos = [];
  }

  return construirBitacora({
    nombreIdea: nombre,
    creadaAt: proyecto.created_at,
    realizadaAt: proyecto.realizada_at ?? null,
    sesiones,
    planes,
    items: ((itemsRaw ?? []) as Array<{ id: string; texto: string; completed_at: string | null; dominio: string | null }>).map((i) => ({
      id: i.id,
      texto: i.texto,
      completed_at: i.completed_at,
      dominio: i.dominio ?? null,
    })),
    eventos,
    nombreMundo,
    generadoAt: new Date().toISOString(),
  });
}
