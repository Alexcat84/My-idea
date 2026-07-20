/**
 * POST /api/cuenta/2fa/email/enviar — envía el código de verificación por
 * correo (réplica del I Ching api/auth/2fa/email/send): límite 5 por
 * usuario / 20 por IP cada 10 min, un solo código vigente a la vez (hash
 * con pimienta, TTL 10 min), envío por Resend API. Si Resend falla, el
 * código se anula y se avisa: jamás un código fantasma en la base.
 * Sirve tanto para ENROLAR el método email como para el desafío del login.
 */
import { NextResponse } from "next/server";
import { createSixDigitCode, EMAIL_CODE_TTL_MINUTES, hashEmailCode } from "@/lib/dosFactores";
import { limitarPorClave } from "@/lib/rateLimit";
import { ipDelRequest, sesionRealDeCookies } from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

async function enviarPorResend(params: {
  apiKey: string;
  from: string;
  to: string;
  codigo: string;
}): Promise<{ ok: boolean; status: number; message?: string }> {
  const asunto = `${params.codigo} es tu código de verificación de My Idea`;
  const texto =
    `Tu código de verificación es ${params.codigo}. ` +
    `Vence en ${EMAIL_CODE_TTL_MINUTES} minutos. ` +
    `Si no fuiste tú, ignora este correo: nadie entra sin este código.`;
  const html =
    `<p>Tu código de verificación es:</p>` +
    `<p style="font-size:28px;font-weight:700;letter-spacing:6px">${params.codigo}</p>` +
    `<p>Vence en ${EMAIL_CODE_TTL_MINUTES} minutos. Si no fuiste tú, ignora este correo: nadie entra sin este código.</p>`;
  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${params.apiKey}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from: params.from, to: [params.to], subject: asunto, text: texto, html }),
  });
  if (response.ok) return { ok: true, status: response.status };
  let message: string | undefined;
  try {
    const body = (await response.json()) as { message?: string; error?: { message?: string } };
    message = body.error?.message ?? body.message;
  } catch {
    message = undefined;
  }
  return { ok: false, status: response.status, message };
}

export async function POST(request: Request) {
  const sesion = await sesionRealDeCookies();
  if (!sesion || !sesion.user.email) {
    return NextResponse.json({ error: "necesitas tu cuenta para esto" }, { status: 401 });
  }
  const userId = sesion.user.id;
  const ip = ipDelRequest(request);

  const porUsuario = await limitarPorClave(`2fa_email:user:${userId}`, 600, 5);
  if (!porUsuario.permitido) {
    return NextResponse.json(
      { error: "Demasiados envíos de código. Espera unos minutos y vuelve a pedirlo." },
      { status: 429 }
    );
  }
  const porIp = await limitarPorClave(`2fa_email:ip:${ip}`, 600, 20);
  if (!porIp.permitido) {
    return NextResponse.json(
      { error: "Demasiados envíos de código. Espera unos minutos y vuelve a pedirlo." },
      { status: 429 }
    );
  }

  const apiKey = process.env.RESEND_API_KEY?.trim();
  const from = process.env.TWO_FACTOR_EMAIL_FROM?.trim();
  const codeSecret = process.env.TWO_FACTOR_EMAIL_CODE_SECRET?.trim();
  if (!apiKey || !from || !codeSecret) {
    console.error("[2fa/email/enviar] falta config:", {
      sinResendKey: !apiKey,
      sinFrom: !from,
      sinCodeSecret: !codeSecret,
    });
    return NextResponse.json({ error: "el código por correo no está disponible ahora" }, { status: 503 });
  }

  const codigo = createSixDigitCode();
  const admin = createAdminClient();

  const { error: limpiarError } = await admin
    .from("two_factor_email_codes")
    .delete()
    .eq("user_id", userId)
    .is("consumed_at", null);
  if (limpiarError) {
    console.error("[2fa/email/enviar] fallo la limpieza:", limpiarError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }
  const { error: insertError } = await admin.from("two_factor_email_codes").insert({
    user_id: userId,
    code_hash: hashEmailCode(codigo, codeSecret),
    expires_at: new Date(Date.now() + EMAIL_CODE_TTL_MINUTES * 60_000).toISOString(),
  });
  if (insertError) {
    console.error("[2fa/email/enviar] fallo el insert:", insertError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  const envio = await enviarPorResend({ apiKey, from, to: sesion.user.email, codigo });
  if (!envio.ok) {
    console.error("[2fa/email/enviar] Resend fallo:", envio.status, envio.message);
    await admin.from("two_factor_email_codes").delete().eq("user_id", userId).is("consumed_at", null);
    return NextResponse.json(
      { error: "No pudimos enviar el correo. Intenta de nuevo en un momento." },
      { status: 502 }
    );
  }

  return NextResponse.json({ ok: true, venceEnMinutos: EMAIL_CODE_TTL_MINUTES });
}
