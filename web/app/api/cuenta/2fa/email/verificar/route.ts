/**
 * POST /api/cuenta/2fa/email/verificar — completa el ALTA del método por
 * correo (réplica del I Ching api/auth/2fa/email/verify): valida el código
 * vigente (hash + tiempo constante, un solo uso), enciende el 2FA con
 * método 'email' (y borra cualquier secreto TOTP a medias: la lección
 * documentada allá — método a medias rompía el login) y entrega los 8
 * códigos de rescate. El intento exitoso se registra con el session_id.
 */
import { NextResponse } from "next/server";
import { generateRecoveryCodes, hashEmailCode, hashRecoveryCodes } from "@/lib/dosFactores";
import {
  candado2FAActivo,
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
  let body: { code?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }
  const codigo = typeof body.code === "string" ? normalizarCodigo(body.code) : "";
  if (codigo.length !== 6) {
    return NextResponse.json({ error: "el código son 6 dígitos" }, { status: 400 });
  }

  const userId = sesion.user.id;
  const ip = ipDelRequest(request);

  if (await candado2FAActivo(userId)) {
    return NextResponse.json(
      { error: "Demasiados intentos. Espera 15 minutos y vuelve a intentar." },
      { status: 423 }
    );
  }

  const codeSecret = process.env.TWO_FACTOR_EMAIL_CODE_SECRET?.trim();
  if (!codeSecret) {
    console.error("[2fa/email/verificar] TWO_FACTOR_EMAIL_CODE_SECRET ausente");
    return NextResponse.json({ error: "el código por correo no está disponible ahora" }, { status: 503 });
  }

  const admin = createAdminClient();
  const ahora = new Date().toISOString();
  const { data: fila, error: filaError } = await admin
    .from("two_factor_email_codes")
    .select("id, code_hash, expires_at")
    .eq("user_id", userId)
    .is("consumed_at", null)
    .order("created_at", { ascending: false })
    .limit(1)
    .maybeSingle();
  if (filaError) {
    console.error("[2fa/email/verificar] fallo la lectura:", filaError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }
  if (!fila) {
    return NextResponse.json({ error: "Pide un código nuevo: no hay ninguno vigente." }, { status: 400 });
  }
  if (new Date(fila.expires_at as string).getTime() < Date.now()) {
    return NextResponse.json({ error: "Ese código ya venció. Pide uno nuevo." }, { status: 400 });
  }

  const esperado = hashEmailCode(codigo, codeSecret).toLowerCase();
  if (!secureEqualHex(esperado, String(fila.code_hash).trim().toLowerCase())) {
    await registrarIntento2FA(userId, ip, false);
    return NextResponse.json({ error: "Ese código no coincide. Vuelve a intentarlo." }, { status: 401 });
  }

  const { error: consumeError } = await admin
    .from("two_factor_email_codes")
    .update({ consumed_at: ahora })
    .eq("id", fila.id as string)
    .eq("user_id", userId);
  if (consumeError) {
    console.error("[2fa/email/verificar] fallo el consumo:", consumeError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  // Alta del método email: siempre 'email' y sin secreto TOTP a medias
  // (lección del I Ching: preferir totp por un QR nunca verificado rompía
  // el login).
  const { error: altaError } = await admin.from("user_seguridad").upsert({
    user_id: userId,
    two_factor_enabled: true,
    two_factor_method: "email",
    totp_secret: null,
    totp_verified_at: ahora,
    totp_last_used_step: null,
    updated_at: ahora,
  });
  if (altaError) {
    console.error("[2fa/email/verificar] fallo el alta:", altaError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  await registrarIntento2FA(userId, ip, true, sesion.sessionId);

  const recoveryCodes = generateRecoveryCodes(8);
  const hashed = await hashRecoveryCodes(recoveryCodes);
  const { error: rpcError } = await admin.rpc("reset_2fa_recovery_codes", {
    p_user_id: userId,
    p_hashed_codes: hashed,
  });
  if (rpcError) {
    console.error("[2fa/email/verificar] fallo la rotacion de codigos:", rpcError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  return NextResponse.json({ ok: true, recoveryCodes });
}
