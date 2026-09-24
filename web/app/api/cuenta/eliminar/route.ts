/**
 * POST /api/cuenta/eliminar — borra la cuenta COMPLETA (réplica del I Ching
 * api/account/delete): exige la palabra escrita "ELIMINAR", y con 2FA activo
 * exige además el desafío superado en esta sesión. Antes de borrar, si la
 * cuenta recibió cortesía, se escribe la huella del correo
 * (cortesia_email_log): borrar-y-volver no re-otorga los 20.
 *
 * BORRADO REAL (decisiones del fundador, 26 sep 2026): "nada se borra jamás"
 * es del catálogo de conocimiento, NO de los datos de los usuarios. Casi todas
 * las tablas cuelgan de auth.users con ON DELETE CASCADE, pero cuatro cosas
 * sobrevivían al deleteUser y aquí se atienden ANTES de borrar la cuenta (si
 * un paso falla, no se borra nada más y se dice):
 *   B4. las identidades invisibles pendientes de adopción se borran, y con
 *       ellas las ideas escritas antes de entrar (solo si de verdad son
 *       invisibles: nunca una cuenta real);
 *   B1. credit_refund_log se ANONIMIZA (queda el importe y la fecha: podría
 *       ser registro fiscal; migración 044 permite el user_id nulo);
 *   B2. revenuecat_webhook_events se ANONIMIZA;
 *   B3. el correo sale de beta_allowlist.
 */
import { NextResponse } from "next/server";
import { huellaDeEmail } from "@/lib/cuentas";
import {
  AVISO_2FA,
  desafioSuperadoEnSesion,
  estadoSeguridad,
  sesionRealDeCookies,
} from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

export async function POST(request: Request) {
  const sesion = await sesionRealDeCookies();
  if (!sesion) {
    return NextResponse.json({ error: "necesitas tu cuenta para esto" }, { status: 401 });
  }
  let body: { confirmacion?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }
  if (String(body.confirmacion ?? "").trim().toUpperCase() !== "ELIMINAR") {
    return NextResponse.json(
      { error: 'Para borrar tu cuenta escribe la palabra "ELIMINAR" tal cual.' },
      { status: 400 }
    );
  }

  const userId = sesion.user.id;
  try {
    const seguridad = await estadoSeguridad(userId);
    if (seguridad.habilitado && !(await desafioSuperadoEnSesion(userId, sesion.sessionId))) {
      return NextResponse.json(AVISO_2FA, { status: 403 });
    }
  } catch (e) {
    // AUD-09 H16: el borrado es irreversible, así que el candado falla
    // CERRADO. Sin veredicto de seguridad no se borra nada.
    console.error("[cuenta/eliminar] no se pudo leer user_seguridad; no se borra:", e);
    return NextResponse.json(
      { error: "No pude confirmar la seguridad de tu cuenta, así que no borré nada. Intenta de nuevo en un momento." },
      { status: 503 }
    );
  }

  const admin = createAdminClient();

  // La huella de la cortesía ANTES del borrado (después ya no hay fila que
  // consultar). Solo si de verdad la recibió.
  const email = sesion.user.email ?? "";
  if (email) {
    const { data: cortesia } = await admin
      .from("beta_courtesy_log")
      .select("user_id")
      .eq("user_id", userId)
      .maybeSingle();
    if (cortesia) {
      const { error: huellaError } = await admin
        .from("cortesia_email_log")
        .upsert({ email_hash: huellaDeEmail(email) });
      if (huellaError) {
        // Sin huella no se borra: borrar dejaría la puerta del re-otorgo
        // abierta (dinero). Ruidoso y reintentable.
        console.error("[cuenta/eliminar] fallo la huella de cortesia:", huellaError.message);
        return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
      }
    }
  }

  const fallo = (paso: string, detalle: unknown) => {
    console.error(`[cuenta/eliminar] fallo ${paso}; no se borra la cuenta:`, detalle);
    return NextResponse.json({ error: "No pude borrar todos tus datos, así que tu cuenta sigue igual. Intenta de nuevo en un momento." }, { status: 500 });
  };

  // B4: las identidades invisibles pendientes de adopción (y sus ideas).
  const { data: yo, error: errYo } = await admin.auth.admin.getUserById(userId);
  if (errYo) return fallo("la lectura de la cuenta", errYo);
  const pendientes = (yo?.user?.app_metadata as { adopcion_pendiente?: unknown } | undefined)?.adopcion_pendiente;
  for (const anonId of Array.isArray(pendientes) ? pendientes.filter((x): x is string => typeof x === "string") : []) {
    const { data: otra, error: errOtra } = await admin.auth.admin.getUserById(anonId);
    if (errOtra) return fallo("la lectura de una identidad invisible", errOtra);
    const u = otra?.user as { is_anonymous?: boolean; user_metadata?: { invitado?: boolean } } | null | undefined;
    if (!u) continue; // ya no existe
    const esInvisible = u.is_anonymous === true || u.user_metadata?.invitado === true;
    if (!esInvisible) continue; // una cuenta real jamás se borra por esta vía
    const { error: errAnon } = await admin.auth.admin.deleteUser(anonId);
    if (errAnon) return fallo("el borrado de una identidad invisible", errAnon);
  }

  // B1 y B2: sin vínculo con la persona (solo importe y fecha).
  const { error: errReembolsos } = await admin
    .from("credit_refund_log")
    .update({ user_id: null, motivo: null })
    .eq("user_id", userId);
  if (errReembolsos) return fallo("la anonimización de los reembolsos (¿falta la migración 044?)", errReembolsos);
  const { error: errPagos } = await admin
    .from("revenuecat_webhook_events")
    .update({ app_user_id: null })
    .eq("app_user_id", userId);
  if (errPagos) return fallo("la anonimización de los eventos de pago", errPagos);

  // B3: el correo sale de la lista de invitados (normalizado como la guarda).
  if (email) {
    const { error: errLista } = await admin.from("beta_allowlist").delete().eq("email", email.trim().toLowerCase());
    if (errLista) return fallo("el borrado de la lista de invitados", errLista);
  }

  const { error: deleteError } = await admin.auth.admin.deleteUser(userId);
  if (deleteError) {
    console.error("[cuenta/eliminar] fallo el borrado:", deleteError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  console.log(`[cuenta/eliminar] cuenta ${userId.slice(0, 8)}… borrada por su dueño`);
  return NextResponse.json({ ok: true });
}
