/**
 * POST /api/auth/registrar — crear cuenta con correo + CONTRASEÑA (modelo del
 * I Ching; el login por código-cada-vez quedó obsoleto: chocaba con el límite
 * de correos de producción y con el 2FA). La allowlist de beta gatea AQUÍ,
 * antes de crear nada. `signUp` manda UN correo de confirmación (una sola vez
 * en la vida de la cuenta) con el enlace a /auth/callback; la cortesía y la
 * adopción corren al confirmar (bienvenidaTrasLogin), no aquí.
 */
import { NextResponse } from "next/server";
import { estaEnAllowlist } from "@/lib/cuentas";
import { COOKIE_NEXT, destinoPostLogin } from "@/lib/nextSeguro";
import { validarPassword } from "@/lib/password";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  let body: { email?: unknown; password?: unknown; next?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }
  const email = String(body.email ?? "").trim().toLowerCase();
  const password = String(body.password ?? "");
  // "Seguimos justo donde quedaste": si el registro nació en la frontera de
  // una idea, el destino se guarda en una cookie (NO en el redirect_to de
  // Supabase, que debe quedar limpio para no arriesgar el fallback a Site
  // URL). /auth/callback la lee al confirmar. Validado como ruta interna.
  const next = destinoPostLogin(typeof body.next === "string" ? body.next : null);
  if (!email || !email.includes("@") || email.length > 254) {
    return NextResponse.json({ error: "escribe un correo valido" }, { status: 400 });
  }
  const problema = validarPassword(password);
  if (problema) return NextResponse.json({ error: problema }, { status: 400 });

  // La allowlist de beta gatea el registro (quién puede tener cuenta).
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
    // Mensaje amable al no invitado (200, no es un error técnico).
    return NextResponse.json({ creado: false, invitado: false });
  }

  const origen = new URL(request.url).origin;
  const supabase = await createClient();
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: { emailRedirectTo: `${origen}/auth/callback` },
  });
  if (error) {
    const msg = error.message.toLowerCase();
    if (msg.includes("rate") && msg.includes("limit")) {
      return NextResponse.json(
        { error: "Demasiados intentos por ahora. Espera unos minutos y vuelve a intentar." },
        { status: 429 }
      );
    }
    console.error("[registrar] signUp fallo:", error.message);
    return NextResponse.json({ error: "no pudimos crear tu cuenta; intenta de nuevo en un momento" }, { status: 500 });
  }

  // signUp con un correo YA registrado no da error: devuelve un usuario con
  // identities vacío. Se trata como "ya existe" (entra, no registra) sin
  // filtrar si el correo existe a un desconocido (mismo mensaje ambiguo).
  const identities = data.user?.identities ?? [];
  if (identities.length === 0) {
    return NextResponse.json({ creado: true, yaExistia: true, invitado: true });
  }

  // Cuenta NUEVA (se envió el correo de confirmación): si el registro vino de
  // la frontera de una idea, deja el destino en la cookie para reanudar al
  // confirmar (mismo navegador; SameSite=Lax sobrevive el clic del enlace).
  const res = NextResponse.json({ creado: true, yaExistia: false, invitado: true });
  if (next !== "/ideas") {
    res.cookies.set(COOKIE_NEXT, next, {
      httpOnly: true,
      sameSite: "lax",
      secure: process.env.NODE_ENV === "production",
      path: "/",
      maxAge: 1800,
    });
  }
  return res;
}
