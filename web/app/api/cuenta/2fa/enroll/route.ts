/**
 * POST /api/cuenta/2fa/enroll — inicia el alta del autenticador (réplica del
 * I Ching api/auth/2fa/enroll): genera secreto TOTP + QR, guarda el secreto
 * CIFRADO (AES-256-GCM, TOTP_ENCRYPTION_KEY) en user_seguridad y limpia el
 * contador anti-replay. El 2FA NO queda activo aquí: se activa al verificar
 * el primer código (POST 2fa/verificar).
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { SERVIDOR_CUENTA } from "@/lib/i18n/mensajes/servidorCuenta";
import { SERVIDOR_DOS_FACTORES } from "@/lib/i18n/mensajes/servidorDosFactores";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { createTotpEnrollment, encryptTotpSecret } from "@/lib/dosFactores";
import {
  aviso2FA,
  desafioSuperadoEnSesion,
  estadoSeguridad,
  sesionRealDeCookies,
} from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

export async function POST(request: Request) {
  const idioma = idiomaDeRequest(request);
  const c = elegir(SERVIDOR_CUENTA, idioma).comun;
  const t = elegir(SERVIDOR_DOS_FACTORES, idioma);
  const sesion = await sesionRealDeCookies();
  if (!sesion || !sesion.user.email) {
    return NextResponse.json({ error: t.necesitasCuentaSeguridad }, { status: 401 });
  }
  // Con 2FA ya activo, RE-enrolar (cambiar el secreto o el método) es tan
  // sensible como desactivar: una sesión con solo el primer factor podría
  // reemplazar el candado en vez de abrirlo. Exige el desafío superado
  // (hallazgo del review de seguridad del commit).
  const previo = await estadoSeguridad(sesion.user.id);
  if (previo.habilitado && !(await desafioSuperadoEnSesion(sesion.user.id, sesion.sessionId))) {
    return NextResponse.json(aviso2FA(idioma), { status: 403 });
  }
  const encryptionKey = process.env.TOTP_ENCRYPTION_KEY;
  if (!encryptionKey || encryptionKey.length < 32) {
    console.error("[2fa/enroll] TOTP_ENCRYPTION_KEY ausente o corta");
    return NextResponse.json({ error: t.dosPasosNoDisponible }, { status: 503 });
  }

  const enrollment = await createTotpEnrollment(sesion.user.email);
  const admin = createAdminClient();
  // AUD-09 M50: el secreto nuevo ESPERA su primer código. El método y el
  // secreto vigentes no se tocan hasta verificar: abandonar el QR ya no deja el
  // candado pidiendo un autenticador que nunca se configuró.
  const { error } = await admin.from("user_seguridad").upsert({
    user_id: sesion.user.id,
    totp_secret_pendiente: encryptTotpSecret(enrollment.secret, encryptionKey),
    updated_at: new Date().toISOString(),
  });
  if (error) {
    console.error("[2fa/enroll] fallo el upsert:", error.message);
    return NextResponse.json({ error: c.algoSeAtoro }, { status: 500 });
  }
  return NextResponse.json({ ok: true, otpauthUrl: enrollment.otpauthUrl, qrDataUrl: enrollment.qrDataUrl });
}
