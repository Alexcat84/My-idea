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
import { cookies } from "next/headers";
import { bienvenidaTrasLogin, adoptarProyectosDeUsuario, estaEnAllowlist } from "@/lib/cuentas";
import { esInvitadoInvisible } from "@/lib/identidad";
import { COOKIE_NEXT, destinoPostLogin } from "@/lib/nextSeguro";
import { estadoSeguridad } from "@/lib/seguridad";
import { createClient } from "@/lib/supabase/server";

export async function GET(request: Request) {
  const url = new URL(request.url);

  // "Seguimos justo donde quedaste": el destino que /api/auth/google dejó en
  // una cookie antes de salir a Google (o /ideas si no había). Toda salida de
  // esta ruta limpia la cookie para que no quede colgada.
  const cookieStore = await cookies();
  const destino = destinoPostLogin(cookieStore.get(COOKIE_NEXT)?.value);
  const responder = (ruta: string) => {
    const res = NextResponse.redirect(new URL(ruta, url.origin));
    res.cookies.delete(COOKIE_NEXT);
    return res;
  };

  const code = url.searchParams.get("code");
  if (!code) return responder("/login?google=fallo");

  const supabase = await createClient();

  // La identidad que este navegador traía ANTES del login (si la traía).
  const {
    data: { user: previo },
  } = await supabase.auth.getUser();
  const anonId = previo && esInvitadoInvisible(previo) ? previo.id : null;

  const { error } = await supabase.auth.exchangeCodeForSession(code);
  if (error) {
    console.error("[google] fallo el intercambio del code:", error.message);
    return responder("/login?google=fallo");
  }

  const {
    data: { user: real },
  } = await supabase.auth.getUser();
  const email = (real?.email ?? "").trim().toLowerCase();
  if (!real || !email) {
    await supabase.auth.signOut();
    return responder("/login?google=fallo");
  }

  let invitado: boolean;
  try {
    invitado = await estaEnAllowlist(email);
  } catch (e) {
    // Error de infraestructura, NO "no invitado": fuera la sesión y a
    // reintentar. Jamás dejar pasar sin veredicto de la allowlist.
    console.error("[google] fallo la consulta de allowlist:", e);
    await supabase.auth.signOut();
    return responder("/login?google=fallo");
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
    // El correo viaja de vuelta: la pantalla amable muestra QUÉ correo no
    // está en la lista (canon 15 v2: el dato accionable).
    return responder(`/login?google=no-invitado&correo=${encodeURIComponent(email)}`);
  }

  await bienvenidaTrasLogin(real, anonId);

  // Centro de cuenta: con 2FA activo, el login sigue con el desafío en la
  // pantalla de login (la sesión ya existe; el motor pagado queda gateado
  // hasta superar el desafío). El destino se arrastra en ?next= para que, al
  // superar el desafío, la pantalla reanude donde el usuario iba.
  try {
    const seguridad = await estadoSeguridad(real.id);
    if (seguridad.habilitado) {
      const nextParam = destino !== "/ideas" ? `&next=${encodeURIComponent(destino)}` : "";
      return responder(`/login?desafio=1&metodo=${seguridad.metodo ?? "totp"}${nextParam}`);
    }
  } catch (e) {
    console.error("[google] no se pudo leer user_seguridad:", e);
  }

  return responder(destino);
}
