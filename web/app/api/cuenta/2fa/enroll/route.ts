/**
 * POST /api/cuenta/2fa/enroll — inicia el alta del autenticador (réplica del
 * I Ching api/auth/2fa/enroll): genera secreto TOTP + QR, guarda el secreto
 * CIFRADO (AES-256-GCM, TOTP_ENCRYPTION_KEY) en user_seguridad y limpia el
 * contador anti-replay. El 2FA NO queda activo aquí: se activa al verificar
 * el primer código (POST 2fa/verificar).
 */
import { NextResponse } from "next/server";
import { createTotpEnrollment, encryptTotpSecret } from "@/lib/dosFactores";
import {
  AVISO_2FA,
  desafioSuperadoEnSesion,
  estadoSeguridad,
  sesionRealDeCookies,
} from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

export async function POST() {
  const sesion = await sesionRealDeCookies();
  if (!sesion || !sesion.user.email) {
    return NextResponse.json({ error: "necesitas tu cuenta para configurar la seguridad" }, { status: 401 });
  }
  // Con 2FA ya activo, RE-enrolar (cambiar el secreto o el método) es tan
  // sensible como desactivar: una sesión con solo el primer factor podría
  // reemplazar el candado en vez de abrirlo. Exige el desafío superado
  // (hallazgo del review de seguridad del commit).
  const previo = await estadoSeguridad(sesion.user.id);
  if (previo.habilitado && !(await desafioSuperadoEnSesion(sesion.user.id, sesion.sessionId))) {
    return NextResponse.json(AVISO_2FA, { status: 403 });
  }
  const encryptionKey = process.env.TOTP_ENCRYPTION_KEY;
  if (!encryptionKey || encryptionKey.length < 32) {
    console.error("[2fa/enroll] TOTP_ENCRYPTION_KEY ausente o corta");
    return NextResponse.json({ error: "la seguridad en dos pasos no está disponible ahora" }, { status: 503 });
  }

  const enrollment = await createTotpEnrollment(sesion.user.email);
  const admin = createAdminClient();
  const { error } = await admin.from("user_seguridad").upsert({
    user_id: sesion.user.id,
    two_factor_method: "totp",
    totp_secret: encryptTotpSecret(enrollment.secret, encryptionKey),
    totp_last_used_step: null,
    updated_at: new Date().toISOString(),
  });
  if (error) {
    console.error("[2fa/enroll] fallo el upsert:", error.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }
  return NextResponse.json({ ok: true, otpauthUrl: enrollment.otpauthUrl, qrDataUrl: enrollment.qrDataUrl });
}
