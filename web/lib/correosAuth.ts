/**
 * Los correos de Supabase Auth en el idioma de la persona (i18n F6, D4): el
 * Send Email Hook de Supabase llama a app/api/auth/hook-correo con el usuario
 * y los datos del correo; aquí se verifica la firma, se elige el idioma y se
 * arman asunto, texto y html desde el catálogo `correosAuth`. Puro (sin red):
 * el envío por Resend vive en la ruta.
 *
 * Contrato de Supabase (docs "Send Email Hook", leídas el 25 sep 2026):
 * - Firma Standard Webhooks: cabeceras webhook-id, webhook-timestamp y
 *   webhook-signature ("v1,<base64>" separadas por espacio); se firma
 *   `${id}.${timestamp}.${cuerpo}` con HMAC-SHA256 y la clave es el base64 que
 *   sigue a "whsec_" en el secreto "v1,whsec_…".
 * - Enlace: {SUPABASE_URL}/auth/v1/verify?token={token_hash}&type={email_action_type}&redirect_to={redirect_to}
 *   (lo mismo que arma {{ .ConfirmationURL }} en las plantillas del tablero:
 *   con PKCE el token trae "pkce_" y /verify devuelve a /auth/callback con ?code=).
 * - Cambio de correo seguro: los nombres están cruzados por compatibilidad:
 *   token_hash_new va al correo ACTUAL (user.email) y token_hash al NUEVO
 *   (user.new_email).
 */
import { createHmac, timingSafeEqual } from "node:crypto";
import { elegir, htmlDir, htmlLang, normalizarIdioma, type ActiveLocale } from "./i18n/config";
import { interpolar } from "./i18n/interpolar";
import { CORREOS_AUTH } from "./i18n/mensajes/correosAuth";

/** Lo que Supabase manda al hook (solo los campos que se usan). */
export type PayloadHook = {
  user: {
    id: string;
    email?: string;
    new_email?: string;
    user_metadata?: Record<string, unknown>;
  };
  email_data: {
    token: string;
    token_hash: string;
    redirect_to: string;
    email_action_type: string;
    site_url: string;
    token_new?: string;
    token_hash_new?: string;
    old_email?: string;
  };
};

export type CorreoArmado = { para: string; asunto: string; texto: string; html: string };

/** Tolerancia de la marca de tiempo (Standard Webhooks: 5 minutos). */
export const TOLERANCIA_FIRMA_S = 300;

/** ¿La petición viene firmada por Supabase con este secreto? Falla cerrada:
 * cualquier dato ausente o raro da false. */
export function verificarFirmaHook(cuerpo: string, cabeceras: Headers, secreto: string, ahoraMs: number = Date.now()): boolean {
  const id = cabeceras.get("webhook-id");
  const timestamp = cabeceras.get("webhook-timestamp");
  const firmas = cabeceras.get("webhook-signature");
  if (!id || !timestamp || !firmas || !secreto) return false;
  if (!/^\d+$/.test(timestamp)) return false;
  if (Math.abs(Math.floor(ahoraMs / 1000) - Number(timestamp)) > TOLERANCIA_FIRMA_S) return false;

  const base64 = secreto.trim().replace(/^v1,/, "").replace(/^whsec_/, "");
  const clave = Buffer.from(base64, "base64");
  if (clave.length === 0) return false;
  const esperada = createHmac("sha256", clave).update(`${id}.${timestamp}.${cuerpo}`).digest();

  for (const parte of firmas.split(" ")) {
    const [version, firma] = parte.split(",", 2);
    if (version !== "v1" || !firma) continue;
    const recibida = Buffer.from(firma, "base64");
    if (recibida.length === esperada.length && timingSafeEqual(recibida, esperada)) return true;
  }
  return false;
}

/** El idioma guardado de la persona (user_metadata.idioma, que escriben el
 * registro y la entrada); sin él, el español. */
export function idiomaDelUsuario(user: { user_metadata?: Record<string, unknown> }): ActiveLocale {
  return normalizarIdioma(user.user_metadata?.idioma);
}

/** El enlace de verificación, como lo documenta Supabase. */
export function enlaceDeAccion(p: { supabaseUrl: string; tokenHash: string; tipo: string; redirectTo: string; siteUrl: string }): string {
  const params = new URLSearchParams({
    token: p.tokenHash,
    type: p.tipo,
    redirect_to: p.redirectTo || p.siteUrl,
  });
  return `${p.supabaseUrl.replace(/\/+$/, "")}/auth/v1/verify?${params.toString()}`;
}

function escaparHtml(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

type Piezas = {
  para: string;
  asunto: string;
  titulo: string;
  cuerpo: string;
  nota: string;
  enlace?: { url: string; boton: string };
  codigo?: { intro: string | null; valor: string };
};

function componer(p: Piezas, idioma: ActiveLocale): CorreoArmado {
  const c = elegir(CORREOS_AUTH, idioma).comun;
  const lineas = [p.titulo, "", p.cuerpo, ""];
  let medio = "";
  if (p.enlace) {
    lineas.push(p.enlace.url, "");
    const url = escaparHtml(p.enlace.url);
    medio +=
      `<p style="margin:24px 0"><a href="${url}" style="background:#1f2937;color:#ffffff;padding:12px 20px;border-radius:8px;text-decoration:none;display:inline-block">${escaparHtml(p.enlace.boton)}</a></p>` +
      `<p style="font-size:13px;color:#6b7280">${escaparHtml(c.siBotonNoAbre)}<br><a href="${url}" style="color:#6b7280;word-break:break-all">${url}</a></p>`;
  }
  if (p.codigo) {
    if (p.codigo.intro) {
      lineas.push(p.codigo.intro, "");
      medio += `<p>${escaparHtml(p.codigo.intro)}</p>`;
    } else {
      lineas.push(p.codigo.valor, "");
      medio += `<p style="font-size:28px;font-weight:700;letter-spacing:6px">${escaparHtml(p.codigo.valor)}</p>`;
    }
  }
  lineas.push(p.nota, "", c.firma);
  const html =
    `<div lang="${htmlLang(idioma)}" dir="${htmlDir(idioma)}" style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.5;color:#111827;max-width:520px">` +
    `<h1 style="font-size:20px;margin:0 0 16px">${escaparHtml(p.titulo)}</h1>` +
    `<p>${escaparHtml(p.cuerpo)}</p>` +
    medio +
    `<p style="font-size:13px;color:#6b7280">${escaparHtml(p.nota)}</p>` +
    `<p style="font-size:13px;color:#6b7280">${escaparHtml(c.firma)}</p>` +
    `</div>`;
  return { para: p.para, asunto: p.asunto, texto: lineas.join("\n"), html };
}

const AVISOS = {
  password_changed_notification: "contrasenaCambiada",
  email_changed_notification: "correoCambiado",
  phone_changed_notification: "telefonoCambiado",
  identity_linked_notification: "accesoVinculado",
  identity_unlinked_notification: "accesoDesvinculado",
  mfa_factor_enrolled_notification: "verificacionAgregada",
  mfa_factor_unenrolled_notification: "verificacionQuitada",
} as const;

/** Los correos que toca mandar por este llamado del hook (uno, o dos en el
 * cambio de correo seguro). Lanza ante un tipo desconocido o sin destinatario:
 * la ruta responde error a Supabase y queda en el log (fallar ruidoso). */
export function armarCorreos(payload: PayloadHook, supabaseUrl: string): CorreoArmado[] {
  const { user, email_data: d } = payload;
  const idioma = idiomaDelUsuario(user);
  const t = elegir(CORREOS_AUTH, idioma);
  const tipo = d.email_action_type;
  const email = (user.email ?? "").trim();
  const enlace = (tokenHash: string) =>
    enlaceDeAccion({ supabaseUrl, tokenHash, tipo, redirectTo: d.redirect_to, siteUrl: d.site_url });
  const exigir = (para: string) => {
    if (!para) throw new Error(`hook-correo: sin destinatario para ${tipo}`);
    return para;
  };
  const conEnlace = (para: string, tokenHash: string, textos: { asunto: string; titulo: string; cuerpo: string; boton: string; nota: string }, codigo?: string): CorreoArmado =>
    componer(
      {
        para: exigir(para),
        asunto: textos.asunto,
        titulo: textos.titulo,
        cuerpo: textos.cuerpo,
        nota: textos.nota,
        enlace: { url: enlace(tokenHash), boton: textos.boton },
        codigo: codigo ? { intro: interpolar(t.comun.oEscribeCodigo, { codigo }), valor: codigo } : undefined,
      },
      idioma
    );

  switch (tipo) {
    case "signup":
      return [conEnlace(email, d.token_hash, t.registro)];
    case "invite":
      return [conEnlace(email, d.token_hash, t.invitacion)];
    case "magiclink":
    case "email":
      return [conEnlace(email, d.token_hash, t.enlaceEntrar, d.token || undefined)];
    case "recovery":
      return [conEnlace(email, d.token_hash, t.recuperar)];
    case "email_change": {
      const nuevo = (user.new_email ?? "").trim();
      const correos: CorreoArmado[] = [];
      if (d.token_hash_new) {
        const textos = t.cambioCorreoActual;
        correos.push(
          conEnlace(email, d.token_hash_new, {
            ...textos,
            cuerpo: interpolar(textos.cuerpo, { actual: email, nuevo: nuevo || email }),
          })
        );
      }
      if (d.token_hash && nuevo) {
        const textos = t.cambioCorreoNuevo;
        correos.push(conEnlace(nuevo, d.token_hash, { ...textos, cuerpo: interpolar(textos.cuerpo, { nuevo }) }));
      }
      if (correos.length === 0) throw new Error("hook-correo: email_change sin token_hash utilizable");
      return correos;
    }
    case "reauthentication": {
      const r = t.reautenticacion;
      if (!d.token) throw new Error("hook-correo: reauthentication sin código");
      return [componer({ para: exigir(email), asunto: r.asunto, titulo: r.titulo, cuerpo: r.cuerpo, nota: r.nota, codigo: { intro: null, valor: d.token } }, idioma)];
    }
    default: {
      if (tipo in AVISOS) {
        const a = t.avisos[AVISOS[tipo as keyof typeof AVISOS]];
        const para = tipo === "email_changed_notification" ? (d.old_email ?? "").trim() || email : email;
        return [componer({ para: exigir(para), asunto: a.asunto, titulo: a.asunto, cuerpo: a.cuerpo, nota: t.avisos.notaSeguridad }, idioma)];
      }
      throw new Error(`hook-correo: tipo de correo desconocido: ${tipo}`);
    }
  }
}
