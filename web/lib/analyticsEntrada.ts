/**
 * analyticsEntrada.ts — Fase 4.0 §6: cargar de Supabase lo que analytics.ts
 * necesita, UNA sola vez y en un solo sitio. La leen los DOS espejos de la
 * misma agua: el Análisis (para el humano) y el follow (para el motor). Sin
 * esto, cada uno arma su propia entrada y la regla "prohibido duplicar la
 * lógica del tiempo" se rompe por la puerta de atrás.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import type { EntradaAnalytics, ItemAnalytics, MundoAnalytics, PlanCoreAnalytics } from "./analytics";
import { obtenerModosPorEspacio, type Proyecto } from "./db";

const ETIQUETAS_CICLO = ["inicial", "completo", "seguimiento"];

/** AUD-09 M18: una lectura que falla NO es "no hay nada". Antes el Análisis, la
 * Celebración y el bloque de realidad del seguimiento salían en cero ante un
 * error transitorio, presentados como verdad. Quien llama lo traduce a un
 * mensaje honesto; nadie recibe ceros inventados. */
export class LecturaFallidaError extends Error {
  constructor(que: string, causa: unknown) {
    super(`no se pudo leer ${que}`);
    this.name = "LecturaFallidaError";
    console.error(`[analytics] no se pudo leer ${que}:`, causa);
  }
}

/** El mensaje honesto de una lectura fallida, el mismo en toda ruta que la usa. */
export const MENSAJE_LECTURA_FALLIDA = "No pude leer tu avance en este momento; intenta de nuevo en un rato.";
const esCore = (dominio: string | null | undefined) => !dominio || dominio === "core";

export async function cargarEntradaAnalytics(
  supabase: SupabaseClient,
  projectId: string,
  proyecto: Proyecto,
  ahora = new Date().toISOString()
): Promise<EntradaAnalytics> {
  const { data: sesiones, error: errSesiones } = await supabase.from("sessions").select("id").eq("project_id", projectId);
  if (errSesiones) throw new LecturaFallidaError("las sesiones", errSesiones);
  const idsSesiones = ((sesiones ?? []) as Array<{ id: string }>).map((s) => s.id);

  const { data: planesRaw, error: errPlanes } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("id, etiqueta, created_at, baseline_confirmada_at, dominio")
        .in("session_id", idsSesiones)
        .order("created_at", { ascending: true })
    : { data: [], error: null };
  if (errPlanes) throw new LecturaFallidaError("los planes", errPlanes);
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
  // P4: id + protege_item alimentan el carril de protección. Degradación en
  // cadena (patrón del GET del checklist): si una columna nueva aún no existe,
  // se recorta y el Análisis sigue; el carril simplemente sale vacío.
  const COLS_ITEMS = "id, plan_id, dominio, etapa, estado, destacado, texto, completed_at, fecha_base, fecha_base_original, protege_item";
  const COLS_VIEJAS = COLS_ITEMS.replace("id, ", "").replace(", protege_item", "");
  // AUD-09 M15: nodos_origen (037) y protege_nodos (041) resuelven la
  // protección por nodo contra el plan vigente. Si la 041 aún no se aplicó, se
  // lee sin protege_nodos y el carril resuelve por id, como antes.
  const candidatas = [
    `${COLS_ITEMS}, nodos_origen, protege_nodos, no_aplica_motivo`,
    `${COLS_ITEMS}, nodos_origen, no_aplica_motivo`,
    `${COLS_ITEMS}, no_aplica_motivo`,
    COLS_ITEMS,
    `${COLS_VIEJAS}, no_aplica_motivo`,
    COLS_VIEJAS,
  ];
  let itemsRaw: unknown[] | null = null;
  let ultimoErrorItems: unknown = null;
  for (const cols of candidatas) {
    const r = await supabase.from("checklist_items").select(cols).eq("project_id", projectId);
    if (!r.error) {
      itemsRaw = (r.data ?? []) as unknown[];
      break;
    }
    ultimoErrorItems = r.error;
  }
  // Si NINGUNA variante de columnas se pudo leer, no es "sin tareas": es una falla.
  if (itemsRaw === null) throw new LecturaFallidaError("las tareas", ultimoErrorItems);
  // Fase 4.1 (V3b): ya NO se excluyen los mundos. La entrada los lleva CON su
  // dominio; analytics decide que capa los usa (la universal los ignora para no
  // mover el ritmo del viaje principal; el desglose de cumplimiento los cuenta).
  const items: ItemAnalytics[] = ((itemsRaw ?? []) as Array<ItemAnalytics & { dominio: string | null }>)
    .map((i) => ({
      plan_id: i.plan_id,
      // P4, ARREGLADO el 4 sep 2026 (decisión del fundador, sesión con
      // credencial). `id` y `protege_item` SE PEDÍAN en COLS_ITEMS y el comentario
      // de arriba ya decía que "alimentan el carril de protección", pero este
      // mapeo NO los llevaba: como los dos son OPCIONALES en ItemAnalytics,
      // TypeScript callaba. Efecto medido: `porIdCore` (analytics.ts:618) quedaba
      // SIEMPRE vacío y el filtro del carril no casaba nunca, así que
      // `carrilProteccion` era SIEMPRE [] en la app real, para cualquier
      // proyecto. Lo cazó el vuelo (corridas E y F) y NINGUNA suite lo veía,
      // porque los tests de analytics fabricaban los ItemAnalytics a mano con
      // los dos campos puestos. La prueba de CRUCE que lo impide de ahora en
      // adelante vive en analyticsEntrada.test.ts.
      id: i.id,
      protege_item: i.protege_item ?? null,
      // AUD-09 M15: los nodos de la tarea y los de lo protegido (misma lección
      // de arriba: opcionales en ItemAnalytics, así que el cruce los vigila).
      nodos_origen: i.nodos_origen ?? null,
      protege_nodos: i.protege_nodos ?? null,
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
  const { data: conCierre, error: errCierre } = await supabase
    .from("project_unlocks")
    .select("dominio, unlocked_at, completado_at, cierre_motivo")
    .eq("project_id", projectId);
  if (!errCierre) mundos = (conCierre ?? []) as MundoAnalytics[];
  else {
    const { data: previo, error: errPrevio } = await supabase
      .from("project_unlocks")
      .select("dominio, unlocked_at")
      .eq("project_id", projectId);
    // Si tampoco la lectura mínima responde, es una falla, no "sin mundos".
    if (errPrevio) throw new LecturaFallidaError("los mundos", errPrevio);
    mundos = (previo ?? []) as MundoAnalytics[];
  }

  // "Todo separado" (T3): el modo del CORE viene de project_modos (dual-read del
  // core en la transición: si no hay fila 'core', cae a projects.modo_camino).
  // El analytics del core es core-centrico, así que su modo es el del core.
  const modos = await obtenerModosPorEspacio(supabase, projectId);
  const modoCore = modos.core ?? (proyecto.modo_camino as "ritmo" | "fechas" | null) ?? null;

  return {
    proyectoCreatedAt: proyecto.created_at,
    realizadaAt: proyecto.realizada_at ?? null,
    organizadorAt: organizador?.created_at ?? null,
    planesCore,
    planesMundo,
    items,
    mundos,
    modoCamino: modoCore,
    cierreMotivo: proyecto.cierre_motivo ?? null,
    ahora,
  };
}
