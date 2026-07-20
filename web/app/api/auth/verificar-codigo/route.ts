/**
 * POST /api/auth/verificar-codigo — el login por CÓDIGO (decisión del
 * fundador, jul 2026): el correo trae un código de 6 dígitos (Resend vía el
 * SMTP de Supabase, template con {{ .Token }}) y el usuario lo escribe aquí.
 * El magic link por enlace queda obsoleto: sin redirects, sin Site URL
 * frágil, sin enlaces que caducan en otro dispositivo.
 *
 * La sesión nace en las cookies de ESTE request (verifyOtp con el cliente de
 * server.ts) y de inmediato corren los dos actos de la bienvenida
 * (lib/cuentas.bienvenidaTrasLogin): cortesía una-sola-vez + adopción del
 * organizador anónimo. La prueba de posesión de la adopción es la sesión
 * invisible que el propio request traía ANTES de verificar.
 */
import { NextResponse } from "next/server";
import { bienvenidaTrasLogin } from "@/lib/cuentas";
import { esInvitadoInvisible } from "@/lib/identidad";
import { estadoSeguridad } from "@/lib/seguridad";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  let body: { email?: unknown; codigo?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }
  const email = String(body.email ?? "").trim().toLowerCase();
  const codigo = String(body.codigo ?? "").trim();
  if (!email || !email.includes("@")) {
    return NextResponse.json({ error: "escribe un correo valido" }, { status: 400 });
  }
  if (!/^\d{6}$/.test(codigo)) {
    return NextResponse.json({ error: "el código son 6 dígitos" }, { status: 400 });
  }

  const supabase = await createClient();

  // La identidad que este navegador traía ANTES del login (si la traía):
  // la prueba de posesión de la adopción.
  const {
    data: { user: previo },
  } = await supabase.auth.getUser();
  const anonId = previo && esInvitadoInvisible(previo) ? previo.id : null;

  const { error } = await supabase.auth.verifyOtp({ email, token: codigo, type: "email" });
  if (error) {
    return NextResponse.json(
      { error: "Ese código no es válido o ya venció. Pide uno nuevo y vuelve a intentar." },
      { status: 400 }
    );
  }

  const {
    data: { user: real },
  } = await supabase.auth.getUser();
  if (real) await bienvenidaTrasLogin(real, anonId);

  // Centro de cuenta: si la cuenta tiene 2FA, el login sigue con el desafío
  // (la bienvenida ya corrió: cortesía y adopción son de SU propia cuenta;
  // lo que el desafío protege es el motor pagado y los borrados).
  if (real) {
    try {
      const seguridad = await estadoSeguridad(real.id);
      if (seguridad.habilitado) {
        return NextResponse.json({ ok: true, requiere2FA: true, metodo: seguridad.metodo ?? "totp" });
      }
    } catch (e) {
      // Sin la 029 aplicada aún, el login no se rompe: solo no hay 2FA.
      console.error("[verificar-codigo] no se pudo leer user_seguridad:", e);
    }
  }

  return NextResponse.json({ ok: true });
}
