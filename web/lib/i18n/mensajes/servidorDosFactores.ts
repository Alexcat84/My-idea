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

export const SERVIDOR_DOS_FACTORES: PorIdioma<typeof es> = { es };
