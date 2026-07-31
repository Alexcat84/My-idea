/**
 * GET /api/calendar/google/conectar — arranca el OAuth PROPIO del calendario
 * (aparte del login de Supabase). Pide el scope `calendar.app.created` con
 * acceso offline. Guarda un `state` anti-CSRF y el `next` (a dónde volver) en
 * cookies cortas que /callback lee al regresar. Exige cuenta real (no invitado).
 */
import { NextResponse } from "next/server";
import { randomBytes } from "node:crypto";
import { createClient } from "@/lib/supabase/server";
import { esInvitadoInvisible } from "@/lib/identidad";
import { urlConsentimiento } from "@/lib/googleCalendar";

export const runtime = "nodejs";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const origin = url.origin;
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user || esInvitadoInvisible(user)) {
    return NextResponse.redirect(new URL("/login", origin));
  }
  const clientId = process.env.GOOGLE_OAUTH_CLIENT_ID;
  if (!clientId) {
    console.error("[gcal/conectar] falta GOOGLE_OAUTH_CLIENT_ID");
    return NextResponse.redirect(new URL("/ideas?gcal=config", origin));
  }
  const state = randomBytes(16).toString("hex");
  const redirectUri = `${origin}/api/calendar/google/callback`;
  const res = NextResponse.redirect(urlConsentimiento({ clientId, redirectUri, state }));
  const opts = { httpOnly: true as const, sameSite: "lax" as const, secure: process.env.NODE_ENV === "production", path: "/", maxAge: 600 };
  res.cookies.set("gcal_state", state, opts);
  const next = url.searchParams.get("next");
  if (next && next.startsWith("/")) res.cookies.set("gcal_next", next, opts);
  return res;
}
