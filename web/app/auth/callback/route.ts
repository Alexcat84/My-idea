/**
 * GET /auth/callback — el regreso del OAuth de Google (réplica del patrón
 * del I Ching, adaptada a las dos leyes de la casa):
 *
 * 1. ALLOWLIST DESPUÉS DE AUTENTICAR. Con el código por email la allowlist
 *    filtra antes de enviar el correo; con OAuth el email solo se conoce al
 *    volver de Google. Si el correo no está invitado: sesión fuera y de
 *    vuelta al login con el mensaje amable — jamás un usuario colado.
 *
 * 2. EL TRABAJO NUNCA SE PIERDE. El intercambio del code REEMPLAZA la
 *    cookie de la identidad invisible. Por eso el id anónimo se captura
 *    ANTES (prueba de posesión: la propia cookie del request, jamás un
 *    parámetro). Si el login prospera, la bienvenida adopta esos proyectos.
 *    Si el correo NO estaba invitado, se acuña una identidad invisible
 *    nueva y los proyectos del anónimo viejo se adoptan a ella: el
 *    visitante vuelve al login con su mundo intacto.
 */
import { NextResponse } from "next/server";
import { bienvenidaTrasLogin, adoptarProyectosDeUsuario, estaEnAllowlist } from "@/lib/cuentas";
import { esInvitadoInvisible } from "@/lib/identidad";
import { createClient } from "@/lib/supabase/server";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const code = url.searchParams.get("code");
  if (!code) return NextResponse.redirect(new URL("/login?google=fallo", url.origin));

  const supabase = await createClient();

  // La identidad que este navegador traía ANTES del login (si la traía).
  const {
    data: { user: previo },
  } = await supabase.auth.getUser();
  const anonId = previo && esInvitadoInvisible(previo) ? previo.id : null;

  const { error } = await supabase.auth.exchangeCodeForSession(code);
  if (error) {
    console.error("[google] fallo el intercambio del code:", error.message);
    return NextResponse.redirect(new URL("/login?google=fallo", url.origin));
  }

  const {
    data: { user: real },
  } = await supabase.auth.getUser();
  const email = (real?.email ?? "").trim().toLowerCase();
  if (!real || !email) {
    await supabase.auth.signOut();
    return NextResponse.redirect(new URL("/login?google=fallo", url.origin));
  }

  let invitado: boolean;
  try {
    invitado = await estaEnAllowlist(email);
  } catch (e) {
    // Error de infraestructura, NO "no invitado": fuera la sesión y a
    // reintentar. Jamás dejar pasar sin veredicto de la allowlist.
    console.error("[google] fallo la consulta de allowlist:", e);
    await supabase.auth.signOut();
    return NextResponse.redirect(new URL("/login?google=fallo", url.origin));
  }

  if (!invitado) {
    await supabase.auth.signOut();
    // Restaurar el mundo del visitante: identidad invisible nueva y sus
    // proyectos anónimos adoptados a ella (la vieja sesión ya no existe).
    if (anonId) {
      try {
        const { data: nueva, error: errAnon } = await supabase.auth.signInAnonymously();
        const nuevoId = nueva?.user?.id ?? null;
        if (errAnon || !nuevoId) throw errAnon ?? new Error("sin usuario anonimo nuevo");
        await adoptarProyectosDeUsuario(anonId, nuevoId);
      } catch (e) {
        // Ruidoso: los proyectos quedan bajo el anónimo viejo (recuperables
        // por el script del fundador), pero nadie debe perder trabajo mudo.
        console.error(`[google] no se pudo restaurar la identidad invisible; proyectos bajo ${anonId}:`, e);
      }
    }
    return NextResponse.redirect(new URL("/login?google=no-invitado", url.origin));
  }

  await bienvenidaTrasLogin(real, anonId);
  return NextResponse.redirect(new URL("/ideas", url.origin));
}
