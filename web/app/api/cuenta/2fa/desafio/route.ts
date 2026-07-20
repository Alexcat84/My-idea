/**
 * POST /api/cuenta/2fa/desafio — el desafío del segundo factor tras el login
 * (réplica del I Ching api/auth/2fa/challenge/verify). Acepta según el
 * método configurado: token TOTP (con anti-replay), código por correo
 * (hash con pimienta + tiempo constante + un solo uso) o un código de
 * rescate. El éxito se registra con el session_id del JWT: ESA es la prueba
 * que las rutas sensibles exigen (adaptación nuestra a sesión por cookies).
 */
import { NextResponse } from "next/server";
import {
  consumeRecoveryCode,
  decryptTotpSecret,
  hashEmailCode,
  verifyTotpTokenWithReplayGuard,
} from "@/lib/dosFactores";
import {
  candado2FAActivo,
  estadoSeguridad,
  ipDelRequest,
  normalizarCodigo,
  registrarIntento2FA,
  secureEqualHex,
  sesionRealDeCookies,
} from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

export async function POST(request: Request) {
  const sesion = await sesionRealDeCookies();
  if (!sesion) {
    return NextResponse.json({ error: "necesitas tu cuenta para esto" }, { status: 401 });
  }
  let body: { token?: unknown; emailCode?: unknown; recoveryCode?: unknown };
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
  if (!estado.habilitado) {
    // Sin 2FA no hay desafío que superar: la UI no debería llegar aquí.
    return NextResponse.json({ ok: true, omitido: true });
  }

  const admin = createAdminClient();
  const metodo = estado.metodo === "email" ? "email" : "totp";
  const token = typeof body.token === "string" ? normalizarCodigo(body.token) : "";
  const emailCode = typeof body.emailCode === "string" ? normalizarCodigo(body.emailCode) : "";
  let verified = false;
  let verifiedTotpStep: number | null = null;

  if (metodo === "totp" && token.length === 6 && estado.totpSecret) {
    const encryptionKey = process.env.TOTP_ENCRYPTION_KEY;
    if (!encryptionKey || encryptionKey.length < 32) {
      console.error("[2fa/desafio] TOTP_ENCRYPTION_KEY ausente o corta");
      return NextResponse.json({ error: "la verificación no está disponible ahora" }, { status: 503 });
    }
    let secreto: string;
    try {
      secreto = decryptTotpSecret(estado.totpSecret, encryptionKey);
    } catch {
      console.error("[2fa/desafio] no se pudo descifrar el secreto (¿cambió TOTP_ENCRYPTION_KEY?)");
      return NextResponse.json({ error: "algo se atoró de nuestro lado; intenta más tarde" }, { status: 500 });
    }
    const r = verifyTotpTokenWithReplayGuard(secreto, token, { lastUsedStep: estado.totpLastUsedStep });
    if (r.replayed) {
      return NextResponse.json({ error: "Ese código ya se usó. Espera el siguiente y escríbelo." }, { status: 401 });
    }
    verified = r.verified;
    verifiedTotpStep = r.usedStep;
  }

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

  if (!verified && metodo === "email" && emailCode.length === 6) {
    const codeSecret = process.env.TWO_FACTOR_EMAIL_CODE_SECRET?.trim();
    if (!codeSecret) {
      console.error("[2fa/desafio] TWO_FACTOR_EMAIL_CODE_SECRET ausente");
      return NextResponse.json({ error: "la verificación no está disponible ahora" }, { status: 503 });
    }
    const { data: fila } = await admin
      .from("two_factor_email_codes")
      .select("id, code_hash, expires_at")
      .eq("user_id", userId)
      .is("consumed_at", null)
      .order("created_at", { ascending: false })
      .limit(1)
      .maybeSingle();
    if (!fila) {
      return NextResponse.json({ error: "Pide un código nuevo: no hay ninguno vigente." }, { status: 400 });
    }
    if (new Date(fila.expires_at as string).getTime() < Date.now()) {
      return NextResponse.json({ error: "Ese código ya venció. Pide uno nuevo." }, { status: 400 });
    }
    const esperado = hashEmailCode(emailCode, codeSecret).toLowerCase();
    if (secureEqualHex(esperado, String(fila.code_hash).trim().toLowerCase())) {
      verified = true;
      await admin
        .from("two_factor_email_codes")
        .update({ consumed_at: new Date().toISOString() })
        .eq("id", fila.id as string)
        .eq("user_id", userId);
    }
  }

  if (!verified) {
    await registrarIntento2FA(userId, ip, false);
    return NextResponse.json({ error: "Ese código no coincide. Vuelve a intentarlo." }, { status: 401 });
  }
  await registrarIntento2FA(userId, ip, true, sesion.sessionId);

  if (verifiedTotpStep !== null) {
    await admin
      .from("user_seguridad")
      .update({
        totp_last_used_step: verifiedTotpStep,
        totp_verified_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      })
      .eq("user_id", userId);
  }

  return NextResponse.json({ ok: true });
}
