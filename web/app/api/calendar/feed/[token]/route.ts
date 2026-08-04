/**
 * GET /api/calendar/feed/[token].ics — el feed de calendario SUSCRIBIBLE
 * (universal, una vía). El teléfono se suscribe a esta URL y la re-lee cada
 * cierto tiempo; devolvemos SIEMPRE fresco un .ics con las fechas PENDIENTES de
 * todas las ideas del usuario (las hechas/retiradas no llevan recordatorio).
 *
 * Sin cookie de sesión: el `token` firmado ES la autorización (lo verifica
 * feedCalendario). Solo lectura, cliente admin. Funciona en Google/Apple/
 * Outlook y cualquier app que soporte "suscribir calendario por URL".
 */
import catalogo from "@/lib/assets/packs_catalog.json";
import { createAdminClient } from "@/lib/supabase/admin";
import { generarIcs, type TareaIcs } from "@/lib/ics";
import { nombreDeIdea } from "@/lib/ideas";
import { usuarioDeToken } from "@/lib/feedCalendario";

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
  const { data: proyectos } = await admin.from("projects").select("id, titulo, entrada_original").eq("user_id", userId);

  const tareas: TareaIcs[] = [];
  for (const p of (proyectos ?? []) as Array<{ id: string; titulo: string | null; entrada_original: string | null }>) {
    const nombre = nombreDeIdea(p.titulo, p.entrada_original ?? "");
    const { data: items } = await admin
      .from("checklist_items")
      .select("id, texto, etapa, fecha_base, estado, dominio")
      .eq("project_id", p.id)
      .not("fecha_base", "is", null);
    const filas = (items ?? []) as Array<{ id: string; texto: string | null; etapa: number; fecha_base: string | null; estado: string; dominio: string | null }>;
    // "Todo separado" (T6, D3): el feed CRECE con los mundos — ya no es core-only.
    // Cada actividad lleva el nombre de cara de SU espacio; ruido cero si el
    // proyecto no tiene mundos (nada que distinguir). Misma vara que etiquetaEspacio.
    const hayMundos = filas.some((i) => !esCore(i.dominio));
    const espacioDe = (dominio: string | null): string | undefined =>
      !hayMundos ? undefined : esCore(dominio) ? "Tu viaje" : nombreMundo(dominio as string);
    for (const i of filas) {
      if (i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica") {
        tareas.push({
          id: i.id,
          texto: i.texto ?? "",
          etapa: i.etapa,
          fechaBase: i.fecha_base,
          nombreIdea: nombre,
          espacio: espacioDe(i.dominio),
        });
      }
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
