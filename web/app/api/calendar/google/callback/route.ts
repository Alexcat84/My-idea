/**
 * GET /api/calendar/google/callback — la vuelta de Google. Verifica el `state`,
 * canjea el código por tokens (con acceso offline llega el refresh_token), crea
 * el calendario dedicado "My Idea" (o reusa el que ya hubiera), guarda el
 * refresh_token CIFRADO, y lanza la sincronía inicial DESPUÉS de responder
 * (`after`, sin bloquear la vuelta). Regresa a donde el usuario venía.
 */
import { NextResponse, after } from "next/server";
import { cookies } from "next/headers";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { cifrar } from "@/lib/cifrado";
import { canjearCodigo, crearCalendario, SCOPE_CALENDARIO } from "@/lib/googleCalendar";
import { sincronizarUsuario } from "@/lib/calendarioSync";

export const runtime = "nodejs";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const origin = url.origin;
  const jar = await cookies();
  const cookieState = jar.get("gcal_state")?.value;
  const nextRaw = jar.get("gcal_next")?.value;
  const destino = (extra = "") => new URL((nextRaw && nextRaw.startsWith("/") ? nextRaw : "/ideas") + extra, origin);

  const code = url.searchParams.get("code");
  const state = url.searchParams.get("state");
  const errParam = url.searchParams.get("error");
  if (errParam || !code || !state || !cookieState || state !== cookieState) {
    return NextResponse.redirect(destino("?gcal=error"));
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return NextResponse.redirect(new URL("/login", origin));

  const clientId = process.env.GOOGLE_OAUTH_CLIENT_ID;
  const clientSecret = process.env.GOOGLE_OAUTH_CLIENT_SECRET;
  const clave = process.env.GOOGLE_TOKEN_ENCRYPTION_KEY;
  if (!clientId || !clientSecret || !clave) {
    console.error("[gcal/callback] faltan credenciales/clave de Google");
    return NextResponse.redirect(destino("?gcal=config"));
  }

  try {
    const redirectUri = `${origin}/api/calendar/google/callback`;
    const { accessToken, refreshToken, email } = await canjearCodigo({ code, clientId, clientSecret, redirectUri });
    const admin = createAdminClient();

    // La conexión previa (si reconecta): conserva su refresh_token y su
    // calendario para no dejar calendarios "My Idea" huérfanos.
    const { data: prev } = await admin
      .from("google_calendar_cuenta")
      .select("refresh_token_cifrado, calendar_id")
      .eq("user_id", user.id)
      .maybeSingle();

    const rtCifrado = refreshToken ? cifrar(refreshToken, clave) : ((prev?.refresh_token_cifrado as string | null) ?? null);
    if (!rtCifrado) return NextResponse.redirect(destino("?gcal=sinrefresh"));

    let calendarId = (prev?.calendar_id as string | null) ?? null;
    if (!calendarId) calendarId = await crearCalendario(accessToken, "My Idea");

    await admin.from("google_calendar_cuenta").upsert({
      user_id: user.id,
      refresh_token_cifrado: rtCifrado,
      calendar_id: calendarId,
      scope: SCOPE_CALENDARIO,
      email,
      updated_at: new Date().toISOString(),
    });

    after(async () => {
      try {
        await sincronizarUsuario(admin, user.id);
      } catch (e) {
        console.error("[gcal/callback] sync inicial:", (e as Error).message);
      }
    });

    const res = NextResponse.redirect(destino("?gcal=ok"));
    res.cookies.delete("gcal_state");
    res.cookies.delete("gcal_next");
    return res;
  } catch (e) {
    console.error("[gcal/callback]", (e as Error).message);
    return NextResponse.redirect(destino("?gcal=error"));
  }
}
