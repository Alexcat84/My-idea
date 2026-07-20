/**
 * POST /api/cuenta/2fa/desactivar — apaga la verificación en dos pasos
 * (réplica del I Ching api/auth/2fa/disable) con un endurecimiento nuestro:
 * exige que ESTA sesión haya superado el desafío (allá el orden lo garantiza
 * el cliente; aquí lo garantiza el servidor). Limpia secreto, códigos de
 * rescate y códigos de correo pendientes; deja el intento en la bitácora.
 */
import { NextResponse } from "next/server";
import {
  AVISO_2FA,
  desafioSuperadoEnSesion,
  estadoSeguridad,
  ipDelRequest,
  registrarIntento2FA,
  sesionRealDeCookies,
} from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

export async function POST(request: Request) {
  const sesion = await sesionRealDeCookies();
  if (!sesion) {
    return NextResponse.json({ error: "necesitas tu cuenta para esto" }, { status: 401 });
  }
  const userId = sesion.user.id;
  const estado = await estadoSeguridad(userId);
  if (!estado.habilitado) return NextResponse.json({ ok: true, omitido: true });

  if (!(await desafioSuperadoEnSesion(userId, sesion.sessionId))) {
    return NextResponse.json(AVISO_2FA, { status: 403 });
  }

  const admin = createAdminClient();
  const { error } = await admin
    .from("user_seguridad")
    .update({
      two_factor_enabled: false,
      two_factor_method: null,
      totp_secret: null,
      totp_verified_at: null,
      totp_last_used_step: null,
      updated_at: new Date().toISOString(),
    })
    .eq("user_id", userId);
  if (error) {
    console.error("[2fa/desactivar] fallo:", error.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  await admin.from("two_factor_recovery_codes").delete().eq("user_id", userId);
  await admin.from("two_factor_email_codes").delete().eq("user_id", userId).is("consumed_at", null);
  await registrarIntento2FA(userId, ipDelRequest(request), true, sesion.sessionId);

  return NextResponse.json({ ok: true });
}
