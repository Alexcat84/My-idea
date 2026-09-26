/**
 * GET /auth/callback — el regreso del OAuth de Google (réplica del patrón
 * del I Ching, adaptada a las dos leyes de la casa):
 *
 * 1. ALLOWLIST DESPUÉS DE AUTENTICAR, en los TRES caminos (Google,
 *    confirmación de registro y recuperación de contraseña). Con el
 *    código por email la allowlist
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
import { idiomaDeRequest } from "@/lib/i18n/servidor";
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
  // El destino vive en una cookie corta: la deja /api/auth/google (antes de
  // salir a Google) o /api/auth/registrar (antes de mandar el correo de
  // confirmación). Así el redirect_to de Supabase queda limpio. Toda salida
  // limpia la cookie.
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
    // Sirve a tres enlaces: Google, confirmación de registro y recuperación.
    // Un enlace vencido o ya usado cae aquí.
    console.error("[auth/callback] fallo el intercambio del code:", error.message);
    return responder("/login?enlace=vencido");
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

  // AUD-09 H07: la adopción corre en TODO camino de sesión, también en la
  // recuperación. Si queda pendiente (se reintentó y siguió fallando), el
  // destino lo dice para que la pantalla lo muestre: nada se pierde en silencio.
  const { pendientes } = await bienvenidaTrasLogin(real, anonId);

  // i18n F6 (D4): como en /api/auth/entrar, el idioma de la interfaz queda en
  // user_metadata.idioma: el hook de correos (api/auth/hook-correo) lo lee para
  // escribir en su idioma. Si falla, el acceso sigue y queda en el registro.
  const idioma = idiomaDeRequest(request);
  if (real.user_metadata?.idioma !== idioma) {
    const { error: errIdioma } = await supabase.auth.updateUser({ data: { idioma } });
    if (errIdioma) console.error("[auth/callback] no se pudo guardar el idioma en user_metadata:", errIdioma.message);
  }
  const conAviso = (ruta: string) =>
    pendientes > 0 ? `${ruta}${ruta.includes("?") ? "&" : "?"}adopcion=pendiente` : ruta;
  const destinoFinal = conAviso(destino);

  // Recuperación de contraseña (resetPasswordForEmail): el enlace trae
  // type=recovery. La sesión de recuperación ya está puesta; se fija la
  // contraseña nueva en /auth/update-password (sin cortesía ni 2FA aquí).
  // AUD-09 H15: este ramal va DESPUÉS de la allowlist. `type` es un parámetro
  // de la query que controla el cliente; antes retornaba primero y cualquier
  // code válido abría sesión aunque el correo no estuviera invitado.
  if (url.searchParams.get("type") === "recovery") {
    return responder(conAviso("/auth/update-password"));
  }

  // Centro de cuenta: con 2FA activo, el login sigue con el desafío en la
  // pantalla de login (la sesión ya existe; el motor pagado queda gateado
  // hasta superar el desafío). El destino se arrastra en ?next= para que, al
  // superar el desafío, la pantalla reanude donde el usuario iba.
  try {
    const seguridad = await estadoSeguridad(real.id);
    if (seguridad.habilitado) {
      const nextParam = destinoFinal !== "/ideas" ? `&next=${encodeURIComponent(destinoFinal)}` : "";
      return responder(`/login?desafio=1&metodo=${seguridad.metodo ?? "totp"}${nextParam}`);
    }
  } catch (e) {
    console.error("[google] no se pudo leer user_seguridad:", e);
  }

  return responder(destinoFinal);
}
