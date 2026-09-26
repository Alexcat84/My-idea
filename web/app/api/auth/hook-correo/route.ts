/**
 * POST /api/auth/hook-correo — el Send Email Hook de Supabase Auth (i18n F6,
 * decisión D4). Con el hook activo, Supabase NO manda sus plantillas: llama
 * aquí con el usuario y los datos del correo (confirmar registro, recuperar
 * contraseña, cambio de correo…), y este handler lo arma en el idioma guardado
 * de la persona (lib/correosAuth.ts + catálogo correosAuth) y lo manda por
 * Resend, igual que el código del 2FA.
 *
 * Falla cerrada y ruidosa: sin SEND_EMAIL_HOOK_SECRET o con la firma mala no
 * se manda nada (500 / 401) y queda en el log. Todo error vuelve a Supabase
 * con la forma que documenta ({ error: { http_code, message } }); Supabase
 * entonces falla la acción (el registro o el "olvidé mi contraseña" dan error)
 * en vez de dar por enviado un correo que no salió. Éxito: 200 con {}.
 * Supabase da 5 s en total al hook; el envío a Resend se corta a los 4 s.
 * Configuración en el tablero: docs/i18n/F6_CORREOS.md.
 */
import { NextResponse } from "next/server";
import { armarCorreos, verificarFirmaHook, type CorreoArmado, type PayloadHook } from "@/lib/correosAuth";

const LIMITE_RESEND_MS = 4000;

function errorHook(status: number, message: string) {
  return NextResponse.json({ error: { http_code: status, message } }, { status });
}

async function enviar(c: CorreoArmado, apiKey: string, from: string): Promise<{ ok: boolean; status: number; message?: string }> {
  try {
    const response = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${apiKey}`, "Content-Type": "application/json" },
      body: JSON.stringify({ from, to: [c.para], subject: c.asunto, text: c.texto, html: c.html }),
      signal: AbortSignal.timeout(LIMITE_RESEND_MS),
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
  } catch (e) {
    return { ok: false, status: 0, message: e instanceof Error ? e.message : String(e) };
  }
}

export async function POST(request: Request) {
  const cuerpo = await request.text();

  const secreto = process.env.SEND_EMAIL_HOOK_SECRET?.trim();
  if (!secreto) {
    console.error("[hook-correo] falta SEND_EMAIL_HOOK_SECRET: no se verifica ni se manda nada");
    return errorHook(500, "send email hook not configured");
  }
  if (!verificarFirmaHook(cuerpo, request.headers, secreto)) {
    console.error("[hook-correo] firma ausente o inválida: petición rechazada", {
      conId: request.headers.has("webhook-id"),
      conFirma: request.headers.has("webhook-signature"),
    });
    return errorHook(401, "invalid signature");
  }

  const apiKey = process.env.RESEND_API_KEY?.trim();
  const from = process.env.TWO_FACTOR_EMAIL_FROM?.trim();
  const supabaseUrl = (process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL)?.trim();
  if (!apiKey || !from || !supabaseUrl) {
    console.error("[hook-correo] falta config:", { sinResendKey: !apiKey, sinFrom: !from, sinSupabaseUrl: !supabaseUrl });
    return errorHook(500, "email sending not configured");
  }

  let payload: PayloadHook;
  try {
    payload = JSON.parse(cuerpo) as PayloadHook;
    if (!payload?.user || !payload?.email_data) throw new Error("sin user o email_data");
  } catch (e) {
    console.error("[hook-correo] payload ilegible:", e);
    return errorHook(400, "invalid payload");
  }

  let correos: CorreoArmado[];
  try {
    correos = armarCorreos(payload, supabaseUrl);
  } catch (e) {
    console.error("[hook-correo] no se pudo armar el correo:", e);
    return errorHook(500, "could not build email");
  }

  for (const correo of correos) {
    const envio = await enviar(correo, apiKey, from);
    if (!envio.ok) {
      console.error("[hook-correo] Resend fallo:", payload.email_data.email_action_type, envio.status, envio.message);
      // 429: Supabase reintenta (hasta 3 veces dentro de sus 5 s).
      return errorHook(envio.status === 429 ? 429 : 500, "email provider failed");
    }
  }
  return NextResponse.json({}, { status: 200 });
}
