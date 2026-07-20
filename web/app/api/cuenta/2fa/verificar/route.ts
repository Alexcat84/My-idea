/**
 * POST /api/cuenta/2fa/verificar — activa el autenticador (réplica del
 * I Ching api/auth/2fa/verify): candado de intentos, verificación TOTP con
 * guardia anti-replay (o un código de rescate), enciende two_factor_enabled
 * y entrega los 8 códigos de rescate NUEVOS (rotación atómica vía RPC
 * reset_2fa_recovery_codes). El intento exitoso se registra con el
 * session_id: la sesión que activa el 2FA ya queda desafiada.
 */
import { NextResponse } from "next/server";
import {
  consumeRecoveryCode,
  decryptTotpSecret,
  generateRecoveryCodes,
  hashRecoveryCodes,
  verifyTotpTokenWithReplayGuard,
} from "@/lib/dosFactores";
import {
  AVISO_2FA,
  candado2FAActivo,
  desafioSuperadoEnSesion,
  estadoSeguridad,
  ipDelRequest,
  normalizarCodigo,
  registrarIntento2FA,
  sesionRealDeCookies,
} from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

export async function POST(request: Request) {
  const sesion = await sesionRealDeCookies();
  if (!sesion) {
    return NextResponse.json({ error: "necesitas tu cuenta para configurar la seguridad" }, { status: 401 });
  }
  let body: { token?: unknown; recoveryCode?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }

  const userId = sesion.user.id;
  const ip = ipDelRequest(request);

  if (await candado2FAActivo(userId)) {
    return NextResponse.json(
      { error: "Demasiados intentos. Espera 15 minutos y vuelve a intentar." },
      { status: 423 }
    );
  }

  const estado = await estadoSeguridad(userId);
  // Con 2FA ya activo, activar un secreto NUEVO = reemplazar el candado:
  // exige el desafío superado en esta sesión (review de seguridad).
  if (estado.habilitado && !(await desafioSuperadoEnSesion(userId, sesion.sessionId))) {
    return NextResponse.json(AVISO_2FA, { status: 403 });
  }
  if (!estado.totpSecret) {
    return NextResponse.json({ error: "primero genera tu código QR (paso anterior)" }, { status: 400 });
  }
  const encryptionKey = process.env.TOTP_ENCRYPTION_KEY;
  if (!encryptionKey || encryptionKey.length < 32) {
    console.error("[2fa/verificar] TOTP_ENCRYPTION_KEY ausente o corta");
    return NextResponse.json({ error: "la seguridad en dos pasos no está disponible ahora" }, { status: 503 });
  }

  let verified = false;
  let verifiedTotpStep: number | null = null;
  const token = typeof body.token === "string" ? normalizarCodigo(body.token) : "";
  if (token.length === 6) {
    let secreto: string;
    try {
      secreto = decryptTotpSecret(estado.totpSecret, encryptionKey);
    } catch {
      console.error("[2fa/verificar] no se pudo descifrar el secreto (¿cambió TOTP_ENCRYPTION_KEY?)");
      return NextResponse.json({ error: "algo se atoró de nuestro lado; intenta más tarde" }, { status: 500 });
    }
    const r = verifyTotpTokenWithReplayGuard(secreto, token, { lastUsedStep: estado.totpLastUsedStep });
    if (r.replayed) {
      return NextResponse.json({ error: "Ese código ya se usó. Espera el siguiente y escríbelo." }, { status: 401 });
    }
    verified = r.verified;
    verifiedTotpStep = r.usedStep;
  }

  const admin = createAdminClient();

  if (!verified && typeof body.recoveryCode === "string" && body.recoveryCode.trim()) {
    const { data: codes } = await admin
      .from("two_factor_recovery_codes")
      .select("code_hash")
      .eq("user_id", userId)
      .is("used_at", null);
    const hashes = ((codes ?? []) as Array<{ code_hash: string }>).map((c) => c.code_hash);
    const consumo = await consumeRecoveryCode(body.recoveryCode.trim(), hashes);
    if (consumo.consumed) {
      verified = true;
      const usado = hashes.find((h) => !consumo.remainingHashes.includes(h));
      if (usado) {
        await admin
          .from("two_factor_recovery_codes")
          .update({ used_at: new Date().toISOString() })
          .eq("user_id", userId)
          .eq("code_hash", usado);
      }
    }
  }

  if (!verified) {
    await registrarIntento2FA(userId, ip, false);
    return NextResponse.json(
      { error: "Ese código no coincide. Revisa tu app de autenticación y vuelve a escribirlo." },
      { status: 401 }
    );
  }
  await registrarIntento2FA(userId, ip, true, sesion.sessionId);

  const { error: updError } = await admin
    .from("user_seguridad")
    .update({
      two_factor_enabled: true,
      two_factor_method: "totp",
      totp_verified_at: new Date().toISOString(),
      updated_at: new Date().toISOString(),
      ...(verifiedTotpStep !== null ? { totp_last_used_step: verifiedTotpStep } : {}),
    })
    .eq("user_id", userId);
  if (updError) {
    console.error("[2fa/verificar] fallo la activacion:", updError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  const recoveryCodes = generateRecoveryCodes(8);
  const hashed = await hashRecoveryCodes(recoveryCodes);
  const { error: rpcError } = await admin.rpc("reset_2fa_recovery_codes", {
    p_user_id: userId,
    p_hashed_codes: hashed,
  });
  if (rpcError) {
    console.error("[2fa/verificar] fallo la rotacion de codigos de rescate:", rpcError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  return NextResponse.json({ ok: true, recoveryCodes });
}
