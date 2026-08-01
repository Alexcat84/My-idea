/**
 * GET /api/calendar/feed-url — le da a la UI la URL del feed suscribible del
 * usuario (https para copiar, webcal:// para el botón que abre el diálogo de
 * suscripción del sistema). Requiere cuenta real (no invitado).
 */
import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";
import { esInvitadoInvisible } from "@/lib/identidad";
import { tokenDeUsuario } from "@/lib/feedCalendario";

export const runtime = "nodejs";

export async function GET(request: Request) {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user || esInvitadoInvisible(user)) {
    return NextResponse.json({ disponible: false, url: null, webcal: null });
  }
  const token = tokenDeUsuario(user.id);
  const origin = new URL(request.url).origin;
  const url = `${origin}/api/calendar/feed/${token}.ics`;
  const webcal = url.replace(/^https?:\/\//, "webcal://");
  return NextResponse.json({ disponible: true, url, webcal });
}
