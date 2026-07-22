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
import { COOKIE_NEXT, destinoPostLogin } from "@/lib/nextSeguro";
import { createClient } from "@/lib/supabase/server";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const origen = url.origin;
  const supabase = await createClient();
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: "google",
    options: { redirectTo: `${origen}/auth/callback` },
  });
  if (error || !data?.url) {
    console.error("[google] no se pudo iniciar OAuth:", error?.message);
    return NextResponse.redirect(new URL("/login?google=fallo", origen));
  }
  const res = NextResponse.redirect(data.url);
  // "Seguimos justo donde quedaste": el next NO puede viajar en el redirect_to
  // (lo acabamos de estabilizar contra el fallback a Site URL), así que va en
  // una cookie corta que /auth/callback lee al volver. SameSite=Lax para que
  // sobreviva la navegación de vuelta desde Google.
  const destino = destinoPostLogin(url.searchParams.get("next"));
  if (destino !== "/ideas") {
    res.cookies.set(COOKIE_NEXT, destino, {
      httpOnly: true,
      sameSite: "lax",
      secure: process.env.NODE_ENV === "production",
      path: "/",
      maxAge: 600,
    });
  }
  return res;
}
