/**
 * POST /api/auth/entrar — iniciar sesión con correo + CONTRASEÑA (modelo del
 * I Ching). A diferencia del código-cada-vez, esto NO manda ningún correo:
 * por eso no choca con el límite de Resend ni obliga a nadie a "esperar dos
 * horas". La allowlist se revisa también aquí (vaciarla cierra la puerta a
 * los ya registrados, no solo a los nuevos). Al entrar: adopción del
 * organizador anónimo + cortesía idempotente (bienvenidaTrasLogin), y si la
 * cuenta tiene 2FA, el login sigue con el desafío.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { SERVIDOR_CUENTA } from "@/lib/i18n/mensajes/servidorCuenta";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { bienvenidaTrasLogin, estaEnAllowlist } from "@/lib/cuentas";
import { esInvitadoInvisible } from "@/lib/identidad";
import { estadoSeguridad } from "@/lib/seguridad";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  const idioma = idiomaDeRequest(request);
  const t = elegir(SERVIDOR_CUENTA, idioma);
  let body: { email?: unknown; password?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: t.comun.cuerpoInvalido }, { status: 400 });
  }
  const email = String(body.email ?? "").trim().toLowerCase();
  const password = String(body.password ?? "");
  if (!email || !email.includes("@") || !password) {
    return NextResponse.json({ error: t.entrar.faltanDatos }, { status: 400 });
  }

  // La allowlist gatea también el ingreso: cerrar la beta (vaciarla) cierra
  // la puerta a todos, no solo a los nuevos.
  let invitado: boolean;
  try {
    invitado = await estaEnAllowlist(email);
  } catch {
    return NextResponse.json(
      { error: t.comun.algoSeAtoroMomento },
      { status: 500 }
    );
  }
  if (!invitado) {
    return NextResponse.json({ ok: false, invitado: false });
  }

  const supabase = await createClient();

  // La identidad invisible que este navegador traía ANTES del login: la
  // prueba de posesión de la adopción (jamás un parámetro).
  const {
    data: { user: previo },
  } = await supabase.auth.getUser();
  const anonId = previo && esInvitadoInvisible(previo) ? previo.id : null;

  const { error } = await supabase.auth.signInWithPassword({ email, password });
  if (error) {
    const msg = error.message.toLowerCase();
    if (msg.includes("email not confirmed") || msg.includes("not confirmed")) {
      return NextResponse.json(
        { error: t.entrar.sinConfirmar, sinConfirmar: true },
        { status: 403 }
      );
    }
    // Credenciales malas: mismo mensaje para correo inexistente o contraseña
    // errada (no revelar cuáles correos tienen cuenta).
    return NextResponse.json({ error: t.entrar.credencialesMalas }, { status: 401 });
  }

  const {
    data: { user: real },
  } = await supabase.auth.getUser();

  // i18n F6 (D4): el idioma de la interfaz queda en user_metadata.idioma para
  // los correos que manda Supabase (recuperar la contraseña, cambio de correo)
  // por el Send Email Hook. Solo si cambió; si falla, la entrada sigue y se dice.
  if (real && real.user_metadata?.idioma !== idioma) {
    const { error: errIdioma } = await supabase.auth.updateUser({ data: { idioma } });
    if (errIdioma) console.error("[entrar] no se pudo guardar el idioma en user_metadata:", errIdioma.message);
  }
  // AUD-09 H07: si la adopción queda pendiente, la respuesta lo dice para que la
  // pantalla lo muestre (y el próximo ingreso lo reintenta).
  const { pendientes } = real ? await bienvenidaTrasLogin(real, anonId) : { pendientes: 0 };
  const adopcion_pendiente = pendientes > 0;

  // Centro de cuenta: con 2FA, el login sigue con el desafío.
  if (real) {
    try {
      const seguridad = await estadoSeguridad(real.id);
      if (seguridad.habilitado) {
        return NextResponse.json({ ok: true, requiere2FA: true, metodo: seguridad.metodo ?? "totp", adopcion_pendiente });
      }
    } catch (e) {
      console.error("[entrar] no se pudo leer user_seguridad:", e);
    }
  }

  return NextResponse.json({ ok: true, adopcion_pendiente });
}
