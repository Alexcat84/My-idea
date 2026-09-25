/**
 * /cuenta, el centro de cuenta: app/cuenta/page.tsx y ui/CuentaCliente.tsx.
 * La palabra de confirmación del borrado (ELIMINAR) NO está aquí: es un dato
 * que el servidor compara (/api/cuenta/eliminar), vive en lib/i18n/palabraEliminar
 * (una por idioma), y entra a las frases por la etiqueta <palabra/>.
 */
import type { PorIdioma } from "../config";

const es = {
  misIdeas: "Mis ideas",
  tuCuenta: "Tu cuenta",
  errores: {
    atoro: "algo se atoró; intenta de nuevo",
    enviarCodigo: "no pudimos enviar el código; intenta de nuevo",
    desactivarSinDesafio: "Para desactivarla, vuelve a entrar y supera el desafío primero.",
  },
  codigoEnviadoA: "Te enviamos un código a {{email}}.",
  desactivada: "Verificación en dos pasos desactivada.",
  tuIdentidad: "Tu identidad",
  seguridad: {
    titulo: "Seguridad · verificación en dos pasos",
    leyendo: "Leyendo el estado de tu seguridad…",
    activadaCompleta: "Verificación en dos pasos activada.",
    guardaRescate:
      "Guarda estos códigos de rescate en un lugar seguro. Cada uno abre tu cuenta UNA vez si pierdes tu método habitual, y no volverán a mostrarse.",
    yaGuarde: "Ya los guardé",
    activada: "Activada",
    codigoPorCorreo: "código por correo",
    appAutenticacion: "app de autenticación",
    alEntrar: "Al entrar, además de tu acceso normal te pediremos {{que}}.",
    unCodigoCorreo: "un código que llega a tu correo",
    elCodigoApp: "el código de tu app",
    desactivar: "Desactivar la verificación en dos pasos",
    pasoEscanear: "1. Escanea este código con tu app de autenticación (Google Authenticator, 1Password, Authy…).",
    altQr: "Código QR para tu app de autenticación",
    pasoEscribir: "2. Escribe el código de 6 dígitos que te muestra la app.",
    verificando: "Verificando…",
    activar: "Activar",
    cancelar: "Cancelar",
    queHace:
      "Te pide un segundo paso antes de usar tus créditos y antes de borrar una idea o tu cuenta. Es opcional y puedes apagarlo cuando quieras.",
    activarApp: "Activar con app de autenticación",
    activarCorreo: "Activar con código por correo",
  },
  peligro: {
    titulo: "Zona de peligro",
    borrarTuCuenta: "Borrar tu cuenta",
    borrarTexto:
      "Se borra todo: tus ideas, tus planes, tu historial y tus créditos. No hay vuelta atrás. Para confirmar, escribe <palabra/>.",
    etiquetaPalabra: "Escribe la palabra para confirmar",
    borrarParaSiempre: "Borrar mi cuenta para siempre",
  },
};

const en: typeof es = {
  misIdeas: "My ideas",
  tuCuenta: "Your account",
  errores: {
    atoro: "something got stuck; try again",
    enviarCodigo: "we couldn't send the code; try again",
    desactivarSinDesafio: "To turn it off, log in again and pass the challenge first.",
  },
  codigoEnviadoA: "We sent a code to {{email}}.",
  desactivada: "Two-step verification turned off.",
  tuIdentidad: "Your identity",
  seguridad: {
    titulo: "Security · two-step verification",
    leyendo: "Checking your security settings…",
    activadaCompleta: "Two-step verification turned on.",
    guardaRescate:
      "Keep these recovery codes somewhere safe. Each one unlocks your account ONCE if you lose your usual method, and they won't be shown again.",
    yaGuarde: "I've saved them",
    activada: "On",
    codigoPorCorreo: "code by email",
    appAutenticacion: "authenticator app",
    alEntrar: "When you log in, on top of your usual sign-in we'll ask you for {{que}}.",
    unCodigoCorreo: "a code sent to your email",
    elCodigoApp: "the code from your app",
    desactivar: "Turn off two-step verification",
    pasoEscanear: "1. Scan this code with your authenticator app (Google Authenticator, 1Password, Authy…).",
    altQr: "QR code for your authenticator app",
    pasoEscribir: "2. Type the 6-digit code the app shows you.",
    verificando: "Verifying…",
    activar: "Turn on",
    cancelar: "Cancel",
    queHace:
      "It asks you for a second step before you use your credits and before you delete an idea or your account. It's optional, and you can turn it off whenever you want.",
    activarApp: "Turn on with an authenticator app",
    activarCorreo: "Turn on with a code by email",
  },
  peligro: {
    titulo: "Danger zone",
    borrarTuCuenta: "Delete your account",
    borrarTexto:
      "Everything gets deleted: your ideas, your plans, your history, and your credits. There's no going back. To confirm, type <palabra/>.",
    etiquetaPalabra: "Type the word to confirm",
    borrarParaSiempre: "Delete my account forever",
  },
};

export const CUENTA: PorIdioma<typeof es> = { es, en };
