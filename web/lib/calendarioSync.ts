/**
 * calendarioSync — la orquestación de la sincronía de UNA VÍA (app → Google).
 * Reglas del evento: una tarea del viaje principal con fecha y aún abierta
 * (no hecha, no retirada) TIENE evento en el calendario dedicado "My Idea";
 * si se marca hecha/retirada o pierde la fecha, el evento se BORRA. El mapa
 * tarea→evento (google_calendar_evento) permite actualizar/borrar el correcto.
 *
 * Todo con el cliente ADMIN (service_role): las tablas son internas y el token
 * jamás sale del servidor. Best-effort: los errores se registran (fallar
 * ruidoso) pero jamás rompen la acción del usuario (se llama desde `after()`).
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import { descifrar } from "./cifrado";
import {
  actualizarEvento,
  borrarCalendario,
  borrarEvento,
  crearCalendario,
  crearEvento,
  refrescarAccessToken,
  type EventoGoogle,
} from "./googleCalendar";
import { nombreDeIdea } from "./ideas";

const esCore = (dominio: string | null | undefined) => !dominio || dominio === "core";
/** aviso la víspera a las 20:00 = 240 min antes del inicio (medianoche del día). */
const AVISO_MIN = 240;

interface FilaItem {
  id: string;
  texto: string;
  etapa: number;
  fecha_base: string | null;
  estado: string;
  project_id: string;
}

function debeTenerEvento(it: FilaItem): boolean {
  return Boolean(it.fecha_base) && it.estado !== "hecho" && it.estado !== "no_aplica";
}

function eventoDe(it: FilaItem, nombreIdea: string): EventoGoogle {
  const dia = it.fecha_base!.slice(0, 10); // YYYY-MM-DD
  const fin = new Date(`${dia}T00:00:00Z`);
  fin.setUTCDate(fin.getUTCDate() + 1); // end.date es EXCLUSIVO en eventos de día completo
  return {
    summary: it.texto,
    description: `${nombreIdea} · Etapa ${it.etapa}\n\nDe tu plan en My Idea.`,
    start: { date: dia },
    end: { date: fin.toISOString().slice(0, 10) },
    reminders: { useDefault: false, overrides: [{ method: "popup", minutes: AVISO_MIN }] },
    extendedProperties: { private: { myIdeaItemId: it.id } },
  };
}

/** Estado de la conexión, para la UI. */
export async function estadoConexion(admin: SupabaseClient, userId: string): Promise<{ conectado: boolean; email: string | null }> {
  const { data } = await admin.from("google_calendar_cuenta").select("email").eq("user_id", userId).maybeSingle();
  return { conectado: Boolean(data), email: (data?.email as string | null) ?? null };
}

/** Carga la conexión, refresca el access_token y asegura el calendario dedicado.
 * null si el usuario no está conectado. */
async function contexto(admin: SupabaseClient, userId: string): Promise<{ accessToken: string; calendarId: string } | null> {
  const clientId = process.env.GOOGLE_OAUTH_CLIENT_ID;
  const clientSecret = process.env.GOOGLE_OAUTH_CLIENT_SECRET;
  const clave = process.env.GOOGLE_TOKEN_ENCRYPTION_KEY;
  if (!clientId || !clientSecret || !clave) {
    console.error("[calendarioSync] faltan GOOGLE_OAUTH_CLIENT_ID/SECRET o GOOGLE_TOKEN_ENCRYPTION_KEY");
    return null;
  }
  const { data } = await admin.from("google_calendar_cuenta").select("refresh_token_cifrado, calendar_id").eq("user_id", userId).maybeSingle();
  if (!data) return null;
  const refreshToken = descifrar(data.refresh_token_cifrado as string, clave);
  const accessToken = await refrescarAccessToken({ refreshToken, clientId, clientSecret });
  let calendarId = (data.calendar_id as string | null) ?? null;
  if (!calendarId) {
    calendarId = await crearCalendario(accessToken, "My Idea");
    await admin.from("google_calendar_cuenta").update({ calendar_id: calendarId, updated_at: new Date().toISOString() }).eq("user_id", userId);
  }
  return { accessToken, calendarId };
}

/** Sincroniza una LISTA de eventos (ya con su contexto), actualizando el mapa. */
async function aplicar(admin: SupabaseClient, userId: string, ctx: { accessToken: string; calendarId: string }, items: FilaItem[], nombreIdea: string): Promise<void> {
  for (const it of items) {
    const { data: mapa } = await admin.from("google_calendar_evento").select("event_id").eq("item_id", it.id).maybeSingle();
    const eventId = (mapa?.event_id as string | null) ?? null;
    if (debeTenerEvento(it)) {
      if (eventId) {
        await actualizarEvento(ctx.accessToken, ctx.calendarId, eventId, eventoDe(it, nombreIdea));
      } else {
        const nuevo = await crearEvento(ctx.accessToken, ctx.calendarId, eventoDe(it, nombreIdea));
        await admin.from("google_calendar_evento").upsert({ item_id: it.id, user_id: userId, event_id: nuevo, sincronizado_at: new Date().toISOString() });
      }
    } else if (eventId) {
      await borrarEvento(ctx.accessToken, ctx.calendarId, eventId);
      await admin.from("google_calendar_evento").delete().eq("item_id", it.id);
    }
  }
}

/** Nombre de la idea de un proyecto (para el título del evento). */
async function nombreProyecto(admin: SupabaseClient, projectId: string): Promise<string> {
  const { data } = await admin.from("projects").select("titulo, entrada_original").eq("id", projectId).maybeSingle();
  return nombreDeIdea((data?.titulo as string | null) ?? null, (data?.entrada_original as string | null) ?? "");
}

/** Sincroniza ítems concretos (por id) de un proyecto — el hook por cambio. */
export async function sincronizarIds(admin: SupabaseClient, userId: string, projectId: string, itemIds: string[]): Promise<void> {
  if (itemIds.length === 0) return;
  const ctx = await contexto(admin, userId);
  if (!ctx) return; // no conectado: no-op
  const { data } = await admin.from("checklist_items").select("id, texto, etapa, fecha_base, estado, project_id, dominio").in("id", itemIds);
  const items = ((data ?? []) as Array<FilaItem & { dominio: string | null }>).filter((i) => esCore(i.dominio));
  if (items.length === 0) return;
  const nombre = await nombreProyecto(admin, projectId);
  await aplicar(admin, userId, ctx, items, nombre);
}

/** Sincronía COMPLETA de todo lo del usuario (al conectar): todas sus ideas. */
export async function sincronizarUsuario(admin: SupabaseClient, userId: string): Promise<void> {
  const ctx = await contexto(admin, userId);
  if (!ctx) return;
  const { data: proyectos } = await admin.from("projects").select("id, titulo, entrada_original").eq("user_id", userId);
  for (const p of (proyectos ?? []) as Array<{ id: string; titulo: string | null; entrada_original: string | null }>) {
    const { data } = await admin
      .from("checklist_items")
      .select("id, texto, etapa, fecha_base, estado, project_id, dominio")
      .eq("project_id", p.id)
      .not("fecha_base", "is", null);
    const items = ((data ?? []) as Array<FilaItem & { dominio: string | null }>).filter((i) => esCore(i.dominio));
    if (items.length === 0) continue;
    await aplicar(admin, userId, ctx, items, nombreDeIdea(p.titulo, p.entrada_original ?? ""));
  }
}

/** Desconectar: borra el calendario dedicado (con todos sus eventos), el mapa y
 * la conexión. Si el calendario ya no existe, no pasa nada (idempotente). */
export async function desconectar(admin: SupabaseClient, userId: string): Promise<void> {
  try {
    const ctx = await contexto(admin, userId);
    if (ctx) await borrarCalendario(ctx.accessToken, ctx.calendarId);
  } catch (e) {
    console.error("[calendarioSync] borrarCalendario al desconectar:", (e as Error).message);
  }
  await admin.from("google_calendar_evento").delete().eq("user_id", userId);
  await admin.from("google_calendar_cuenta").delete().eq("user_id", userId);
}
