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
import { createAdminClient } from "@/lib/supabase/admin";
import { generarIcs, type TareaIcs } from "@/lib/ics";
import { nombreDeIdea } from "@/lib/ideas";
import { usuarioDeToken } from "@/lib/feedCalendario";

export const runtime = "nodejs";
// Cada visita regenera el feed (el teléfono controla su cadencia de refresco).
export const dynamic = "force-dynamic";

const esCore = (dominio: string | null | undefined) => !dominio || dominio === "core";

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
    for (const i of (items ?? []) as Array<{ id: string; texto: string | null; etapa: number; fecha_base: string | null; estado: string; dominio: string | null }>) {
      if (esCore(i.dominio) && i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica") {
        tareas.push({ id: i.id, texto: i.texto ?? "", etapa: i.etapa, fechaBase: i.fecha_base, nombreIdea: nombre });
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
