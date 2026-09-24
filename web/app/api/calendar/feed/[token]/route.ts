/**
 * GET /api/calendar/feed/[token].ics — el feed de calendario SUSCRIBIBLE
 * (universal, una vía). El teléfono se suscribe a esta URL y la re-lee cada
 * cierto tiempo; devolvemos SIEMPRE fresco un .ics con las fechas PENDIENTES de
 * todas las ideas del usuario (las hechas/retiradas no llevan recordatorio).
 * AUD-09 H11: y solo del plan VIGENTE de cada espacio, nunca de un espacio "a
 * mi ritmo", de un mundo completado ni de una idea realizada.
 *
 * Sin cookie de sesión: el `token` firmado ES la autorización (lo verifica
 * feedCalendario). Solo lectura, cliente admin. Funciona en Google/Apple/
 * Outlook y cualquier app que soporte "suscribir calendario por URL".
 */
import catalogo from "@/lib/assets/packs_catalog.json";
import { createAdminClient } from "@/lib/supabase/admin";
import { generarIcs, type TareaIcs } from "@/lib/ics";
import { nombreDeIdea } from "@/lib/ideas";
import { itemsQueAvisan, usuarioDeToken, type ItemFeed, type PlanFeed } from "@/lib/feedCalendario";

export const runtime = "nodejs";
// Cada visita regenera el feed (el teléfono controla su cadencia de refresco).
export const dynamic = "force-dynamic";

const esCore = (dominio: string | null | undefined) => !dominio || dominio === "core";
const PACKS = (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs;
const nombreMundo = (dominio: string) => PACKS.find((p) => p.clave === dominio)?.nombre ?? dominio;

export async function GET(_request: Request, { params }: { params: Promise<{ token: string }> }) {
  const { token: crudo } = await params;
  const token = crudo.endsWith(".ics") ? crudo.slice(0, -4) : crudo;
  const userId = usuarioDeToken(token);
  if (!userId) return new Response("Calendario no encontrado.", { status: 404 });

  const admin = createAdminClient();
  // AUD-09 H11: solo avisa lo vigente, con fechas y abierto (itemsQueAvisan).
  const { data: proyectos } = await admin
    .from("projects")
    .select("id, titulo, entrada_original, realizada_at, modo_camino")
    .eq("user_id", userId);

  const tareas: TareaIcs[] = [];
  for (const p of (proyectos ?? []) as Array<{
    id: string;
    titulo: string | null;
    entrada_original: string | null;
    realizada_at: string | null;
    modo_camino: "ritmo" | "fechas" | null;
  }>) {
    if (p.realizada_at) continue; // silencio para ideas cerradas
    const nombre = nombreDeIdea(p.titulo, p.entrada_original ?? "");
    const { data: items } = await admin
      .from("checklist_items")
      .select("id, texto, etapa, fecha_base, estado, dominio, plan_id")
      .eq("project_id", p.id)
      .not("fecha_base", "is", null);
    const filas = (items ?? []) as ItemFeed[];
    if (filas.length === 0) continue;
    const { data: sesiones } = await admin.from("sessions").select("id").eq("project_id", p.id);
    const idsSesion = ((sesiones ?? []) as Array<{ id: string }>).map((x) => x.id);
    const { data: planes } = idsSesion.length
      ? await admin.from("plans").select("id, dominio, created_at, etiqueta").in("session_id", idsSesion)
      : { data: [] };
    const { data: modosRaw } = await admin.from("project_modos").select("dominio, modo_camino").eq("project_id", p.id);
    const modos: Record<string, "ritmo" | "fechas"> = {};
    // Lectura doble del núcleo: la columna vieja del proyecto, y encima la de project_modos.
    if (p.modo_camino) modos.core = p.modo_camino;
    for (const m of (modosRaw ?? []) as Array<{ dominio: string; modo_camino: "ritmo" | "fechas" }>) modos[m.dominio] = m.modo_camino;
    const { data: unlocks } = await admin.from("project_unlocks").select("dominio, completado_at").eq("project_id", p.id);
    const mundosCompletados = ((unlocks ?? []) as Array<{ dominio: string; completado_at: string | null }>)
      .filter((u) => u.completado_at)
      .map((u) => u.dominio);

    const vigentes = itemsQueAvisan({
      realizada: false,
      items: filas,
      planes: (planes ?? []) as PlanFeed[],
      modos,
      mundosCompletados,
    });
    // "Todo separado" (T6, D3): el feed CRECE con los mundos — ya no es core-only.
    // Cada actividad lleva el nombre de cara de SU espacio; ruido cero si el
    // proyecto no tiene mundos (nada que distinguir). Misma vara que etiquetaEspacio.
    const hayMundos = vigentes.some((i) => !esCore(i.dominio));
    const espacioDe = (dominio: string | null): string | undefined =>
      !hayMundos ? undefined : esCore(dominio) ? "Tu viaje" : nombreMundo(dominio as string);
    for (const i of vigentes) {
      tareas.push({
        id: i.id,
        texto: i.texto ?? "",
        etapa: i.etapa,
        fechaBase: i.fecha_base as string,
        nombreIdea: nombre,
        espacio: espacioDe(i.dominio),
      });
    }
  }

  const ics = generarIcs({ nombreIdea: "My Idea", tareas });
  return new Response(ics, {
    status: 200,
    headers: {
      "Content-Type": "text/calendar; charset=utf-8",
      "Content-Disposition": 'inline; filename="my-idea.ics"',
      // el cliente de calendario decide cuándo re-leer; una hora de gracia.
      "Cache-Control": "public, max-age=3600",
    },
  });
}
