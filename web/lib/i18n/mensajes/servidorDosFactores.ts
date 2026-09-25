/** Mensajes de las rutas del doble factor (app/api/cuenta/2fa/**) y el correo
 * del código de verificación (asunto y cuerpo; los correos son la fase F6). */
import type { PorIdioma } from "../config";

const es = {
  necesitasCuentaSeguridad: "necesitas tu cuenta para configurar la seguridad",
  demasiadosIntentos: "Demasiados intentos. Espera 15 minutos y vuelve a intentar.",
  verificacionNoDisponible: "la verificación no está disponible ahora",
  dosPasosNoDisponible: "la seguridad en dos pasos no está disponible ahora",
  correoNoDisponible: "el código por correo no está disponible ahora",
  algoSeAtoroMasTarde: "algo se atoró de nuestro lado; intenta más tarde",
  codigoYaUsado: "Ese código ya se usó. Espera el siguiente y escríbelo.",
  noPudeConfirmar: "No pude confirmar tu código; intenta de nuevo en un momento.",
  sinCodigoVigente: "Pide un código nuevo: no hay ninguno vigente.",
  codigoVencido: "Ese código ya venció. Pide uno nuevo.",
  noCoincide: "Ese código no coincide. Vuelve a intentarlo.",
  noCoincideApp: "Ese código no coincide. Revisa tu app de autenticación y vuelve a escribirlo.",
  primeroQr: "primero genera tu código QR (paso anterior)",
  seisDigitos: "el código son 6 dígitos",
  demasiadosEnvios: "Demasiados envíos de código. Espera unos minutos y vuelve a pedirlo.",
  noPudimosEnviar: "No pudimos enviar el correo. Intenta de nuevo en un momento.",
  correo: {
    asunto: "{{codigo}} es tu código de verificación de My Idea",
    texto:
      "Tu código de verificación es {{codigo}}. Vence en {{minutos}} minutos. Si no fuiste tú, ignora este correo: nadie entra sin este código.",
    htmlTuCodigo: "Tu código de verificación es:",
    htmlVence: "Vence en {{minutos}} minutos. Si no fuiste tú, ignora este correo: nadie entra sin este código.",
  },
};

const en: typeof es = {
  necesitasCuentaSeguridad: "you need your account to set up security",
  demasiadosIntentos: "Too many attempts. Wait 15 minutes and try again.",
  verificacionNoDisponible: "verification isn't available right now",
  dosPasosNoDisponible: "two-step verification isn't available right now",
  correoNoDisponible: "email codes aren't available right now",
  algoSeAtoroMasTarde: "something got stuck on our end; try again later",
  codigoYaUsado: "That code was already used. Wait for the next one and type it in.",
  noPudeConfirmar: "I couldn't confirm your code; try again in a moment.",
  sinCodigoVigente: "Request a new code: there isn't an active one.",
  codigoVencido: "That code has expired. Request a new one.",
  noCoincide: "That code doesn't match. Try again.",
  noCoincideApp: "That code doesn't match. Check your authenticator app and type it again.",
  primeroQr: "generate your QR code first (previous step)",
  seisDigitos: "the code is 6 digits",
  demasiadosEnvios: "Too many codes sent. Wait a few minutes and request it again.",
  noPudimosEnviar: "We couldn't send the email. Try again in a moment.",
  correo: {
    asunto: "{{codigo}} is your My Idea verification code",
    texto:
      "Your verification code is {{codigo}}. It expires in {{minutos}} minutes. If this wasn't you, ignore this email: no one can get in without this code.",
    htmlTuCodigo: "Your verification code is:",
    htmlVence: "It expires in {{minutos}} minutes. If this wasn't you, ignore this email: no one can get in without this code.",
  },
};

export const SERVIDOR_DOS_FACTORES: PorIdioma<typeof es> = { es, en };
