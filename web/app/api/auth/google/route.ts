/**
 * GET /api/auth/google — el inicio del login con Google (réplica de la
 * lógica del I Ching, adaptada a la casa). El botón del login navega AQUÍ
 * (link normal, no fetch): este handler pide a Supabase la URL de OAuth
 * (PKCE; el code_verifier queda en cookies de este mismo response) y
 * redirige al consentimiento de Google. Google devuelve a /auth/callback.
 *
 * La allowlist NO puede aplicarse aquí (el email se conoce al volver):
 * se aplica en el callback, después de autenticar.
 */
import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";

export async function GET(request: Request) {
  const origen = new URL(request.url).origin;
  const supabase = await createClient();
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: "google",
    options: { redirectTo: `${origen}/auth/callback` },
  });
  if (error || !data?.url) {
    console.error("[google] no se pudo iniciar OAuth:", error?.message);
    return NextResponse.redirect(new URL("/login?google=fallo", origen));
  }
  return NextResponse.redirect(data.url);
}
