/**
 * POST /api/cuenta/2fa/email/enviar — envía el código de verificación por
 * correo (réplica del I Ching api/auth/2fa/email/send): límite 5 por
 * usuario / 20 por IP cada 10 min, un solo código vigente a la vez (hash
 * con pimienta, TTL 10 min), envío por Resend API. Si Resend falla, el
 * código se anula y se avisa: jamás un código fantasma en la base.
 * Sirve tanto para ENROLAR el método email como para el desafío del login.
 */
import { NextResponse } from "next/server";
import { elegir, htmlDir, htmlLang, type ActiveLocale } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { SERVIDOR_CUENTA } from "@/lib/i18n/mensajes/servidorCuenta";
import { SERVIDOR_DOS_FACTORES } from "@/lib/i18n/mensajes/servidorDosFactores";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { createSixDigitCode, EMAIL_CODE_TTL_MINUTES, hashEmailCode } from "@/lib/dosFactores";
import { limitarPorClave } from "@/lib/rateLimit";
import {
  aviso2FA,
  desafioSuperadoEnSesion,
  estadoSeguridad,
  ipDelRequest,
  sesionRealDeCookies,
} from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

async function enviarPorResend(params: {
  apiKey: string;
  from: string;
  to: string;
  codigo: string;
  idioma: ActiveLocale;
}): Promise<{ ok: boolean; status: number; message?: string }> {
  const t = elegir(SERVIDOR_DOS_FACTORES, params.idioma).correo;
  const valores = { codigo: params.codigo, minutos: EMAIL_CODE_TTL_MINUTES };
  const asunto = interpolar(t.asunto, valores);
  const texto = interpolar(t.texto, valores);
  // i18n F6: lang y dir del idioma (el árabe se lee de derecha a izquierda);
  // el texto es el mismo del catálogo.
  const html =
    `<div lang="${htmlLang(params.idioma)}" dir="${htmlDir(params.idioma)}">` +
    `<p>${t.htmlTuCodigo}</p>` +
    `<p style="font-size:28px;font-weight:700;letter-spacing:6px">${params.codigo}</p>` +
    `<p>${interpolar(t.htmlVence, valores)}</p>` +
    `</div>`;
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
  const idioma = idiomaDeRequest(request);
  const c = elegir(SERVIDOR_CUENTA, idioma).comun;
  const t = elegir(SERVIDOR_DOS_FACTORES, idioma);
  const sesion = await sesionRealDeCookies();
  if (!sesion || !sesion.user.email) {
    return NextResponse.json({ error: c.necesitasCuenta }, { status: 401 });
  }
  const userId = sesion.user.id;
  const ip = ipDelRequest(request);

  // Cuando el método vigente ES correo, enviar el código es el CAMINO del
  // desafío (el login lo necesita): se permite siempre. Lo que se cierra es
  // que la sesión sin desafío de un usuario TOTP inicie un cambio de método
  // (review de seguridad del commit: re-enrolar = reemplazar el candado).
  const previo = await estadoSeguridad(userId);
  if (
    previo.habilitado &&
    previo.metodo !== "email" &&
    !(await desafioSuperadoEnSesion(userId, sesion.sessionId))
  ) {
    return NextResponse.json(aviso2FA(idioma), { status: 403 });
  }

  const porUsuario = await limitarPorClave(`2fa_email:user:${userId}`, 600, 5);
  if (!porUsuario.permitido) {
    return NextResponse.json(
      { error: t.demasiadosEnvios },
      { status: 429 }
    );
  }
  const porIp = await limitarPorClave(`2fa_email:ip:${ip}`, 600, 20);
  if (!porIp.permitido) {
    return NextResponse.json(
      { error: t.demasiadosEnvios },
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
    return NextResponse.json({ error: t.correoNoDisponible }, { status: 503 });
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
    return NextResponse.json({ error: c.algoSeAtoro }, { status: 500 });
  }
  const { error: insertError } = await admin.from("two_factor_email_codes").insert({
    user_id: userId,
    code_hash: hashEmailCode(codigo, codeSecret),
    expires_at: new Date(Date.now() + EMAIL_CODE_TTL_MINUTES * 60_000).toISOString(),
  });
  if (insertError) {
    console.error("[2fa/email/enviar] fallo el insert:", insertError.message);
    return NextResponse.json({ error: c.algoSeAtoro }, { status: 500 });
  }

  const envio = await enviarPorResend({ apiKey, from, to: sesion.user.email, codigo, idioma });
  if (!envio.ok) {
    console.error("[2fa/email/enviar] Resend fallo:", envio.status, envio.message);
    const { error: errEscritura1 } = await admin.from("two_factor_email_codes").delete().eq("user_id", userId).is("consumed_at", null);
    if (errEscritura1) {
      console.error("[app/api/cuenta/2fa/email/enviar/route.ts] delete two_factor_email_codes fallo:", errEscritura1);
    }
    return NextResponse.json(
      { error: t.noPudimosEnviar },
      { status: 502 }
    );
  }

  return NextResponse.json({ ok: true, venceEnMinutos: EMAIL_CODE_TTL_MINUTES });
}
