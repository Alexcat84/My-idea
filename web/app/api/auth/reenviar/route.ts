/**
 * POST /api/auth/reenviar — reenviar el correo de confirmación del registro
 * (modelo I Ching: sb.auth.resend type=signup) para quien no lo recibió o lo
 * dejó vencer. Respuesta genérica (no revela si el correo tiene cuenta).
 */
import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  let body: { email?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }
  const email = String(body.email ?? "").trim().toLowerCase();
  if (!email || !email.includes("@")) {
    return NextResponse.json({ error: "escribe un correo valido" }, { status: 400 });
  }

  const origen = new URL(request.url).origin;
  const supabase = await createClient();
  const { error } = await supabase.auth.resend({
    type: "signup",
    email,
    options: { emailRedirectTo: `${origen}/auth/callback` },
  });
  if (error) console.error("[reenviar] resend fallo:", error.message);
  return NextResponse.json({ enviado: true });
}
