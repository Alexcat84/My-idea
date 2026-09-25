/**
 * POST /api/auth/reset — "olvidé mi contraseña" (modelo I Ching):
 * resetPasswordForEmail manda un enlace de recuperación a /auth/callback,
 * que reconoce type=recovery y lleva a /auth/update-password. Respuesta
 * SIEMPRE genérica: no revela si el correo tiene cuenta (anti-enumeración).
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { SERVIDOR_CUENTA } from "@/lib/i18n/mensajes/servidorCuenta";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  const t = elegir(SERVIDOR_CUENTA, idiomaDeRequest(request));
  let body: { email?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: t.comun.cuerpoInvalido }, { status: 400 });
  }
  const email = String(body.email ?? "").trim().toLowerCase();
  if (!email || !email.includes("@")) {
    return NextResponse.json({ error: t.comun.correoInvalido }, { status: 400 });
  }

  const origen = new URL(request.url).origin;
  const supabase = await createClient();
  const { error } = await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: `${origen}/auth/callback?type=recovery`,
  });
  if (error) console.error("[reset] resetPasswordForEmail fallo:", error.message);
  // Genérico pase lo que pase: si el correo existe, le llega el enlace.
  return NextResponse.json({ enviado: true });
}
