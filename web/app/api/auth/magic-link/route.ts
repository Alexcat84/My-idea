/**
 * POST /api/auth/magic-link — Fase 3.2 (item 9 original), remodelada en la
 * ETAPA 2: la allowlist de beta se aplica AQUÍ, antes de que exista sesión
 * alguna: solo los emails presentes en beta_allowlist (migration 008, solo
 * legible con service role) reciben el correo. Quien no está invitado recibe
 * una respuesta amable — jamás un error técnico.
 *
 * Desde jul 2026 el correo trae un CÓDIGO de 6 dígitos (template de Supabase
 * con {{ .Token }}, enviado por Resend) que se canjea en
 * /api/auth/verificar-codigo. El enlace mágico quedó obsoleto (el
 * emailRedirectTo se conserva solo para el camino legacy de /auth/confirm).
 */
import { NextResponse } from "next/server";
import { estaEnAllowlist } from "@/lib/cuentas";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }
  const email = String((body as { email?: unknown } | null)?.email ?? "")
    .trim()
    .toLowerCase();
  if (!email || !email.includes("@") || email.length > 254) {
    return NextResponse.json({ error: "escribe un correo valido" }, { status: 400 });
  }

  let invitado: boolean;
  try {
    invitado = await estaEnAllowlist(email);
  } catch {
    return NextResponse.json(
      { error: "algo se atoro de nuestro lado; intenta de nuevo en un momento" },
      { status: 500 }
    );
  }
  if (!invitado) {
    // Mensaje amable al no invitado (brief 2.1) -- 200, no es un error.
    return NextResponse.json({ enviado: false, invitado: false });
  }

  const origen = new URL(request.url).origin;
  const supabase = await createClient();
  const { error } = await supabase.auth.signInWithOtp({
    email,
    options: { emailRedirectTo: `${origen}/auth/confirm` },
  });
  if (error) {
    return NextResponse.json(
      { error: "no pudimos enviar el enlace; intenta de nuevo en un momento" },
      { status: 500 }
    );
  }
  return NextResponse.json({ enviado: true, invitado: true });
}
