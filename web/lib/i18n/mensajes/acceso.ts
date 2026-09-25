/** El acceso: app/login/page.tsx, app/auth/update-password/page.tsx y las reglas de lib/password.ts. */
import type { PorIdioma } from "../config";

const esLogin = {
  lema: "El espacio donde tus ideas se trabajan.",
  errores: {
    enviarCodigo: "no pudimos enviar el código; intenta de nuevo",
    conectar: "no pudimos conectar; intenta de nuevo",
    conectarInternet: "no pudimos conectar; revisa tu internet e intenta de nuevo",
    atoro: "algo se atoró; intenta de nuevo",
    yaTieneCuenta: "Ese correo ya tiene cuenta. Inicia sesión.",
    escribeCorreo: "Escribe tu correo arriba y toca de nuevo.",
  },
  avisos: {
    codigoEnviado: "Te enviamos un código a tu correo.",
    codigoNuevo: "Código nuevo enviado a tu correo.",
    confirmacionReenviada: "Te reenviamos el correo de confirmación. Revisa tu bandeja.",
  },
  revisaCorreo: {
    titulo: "Revisa tu correo",
    texto: "Te enviamos un enlace a <correo/> para confirmar tu cuenta. Ábrelo y quedas dentro. (Si no lo ves, revisa el spam.)",
  },
  resetEnviado: {
    titulo: "Enlace enviado",
    texto: "Si <correo/> tiene cuenta, le llegó un enlace para elegir una contraseña nueva. Revisa tu bandeja (y el spam).",
  },
  volver: "Volver",
  desafio: {
    titulo: "Un paso más: tu verificación en dos pasos",
    escribeRescate: "Escribe uno de tus códigos de rescate.",
    etiquetaRescate: "Código de rescate",
    escribeCodigoApp: "Escribe el código de tu app de autenticación.",
    etiquetaCodigo: "Código de 6 dígitos",
    verificando: "Verificando…",
    verificar: "Verificar",
    reenviarCodigo: "Reenviarme el código",
    volverNormal: "Volver al código normal",
    usarRescate: "No tengo mi código: usar uno de rescate",
  },
  noInvitado: {
    titulo: "My Idea está en beta privada.",
    texto:
      "Ese correo aún no está en la lista de invitados (es la misma lista para entrar con contraseña o con Google). Si alguien te invitó, pídele que confirme el correo que registró.",
    otroCorreo: "Probar con otro correo",
  },
  entrar: "Entrar",
  crearCuenta: "Crear cuenta",
  enlaceVencido: "Ese enlace ya venció o ya se usó. Pide uno nuevo aquí abajo.",
  googleFallo: "No pudimos completar el acceso con Google. Intenta de nuevo, o entra con tu contraseña.",
  etiquetaCorreo: "Correo electrónico",
  placeholderCorreo: "tu@correo.com",
  etiquetaContrasena: "Contraseña",
  placeholderContrasena: "Tu contraseña",
  reglasContrasena: "Al menos {{n}} caracteres, una mayúscula y un número.",
  reenviarConfirmacion: "Reenviarme el correo de confirmación",
  unMomento: "Un momento…",
  crearMiCuenta: "Crear mi cuenta",
  olvide: "Olvidé mi contraseña",
  separador: "o",
  continuarGoogle: "Continuar con Google",
};

const enLogin: typeof esLogin = {
  lema: "The space where your ideas get worked out.",
  errores: {
    enviarCodigo: "we couldn't send the code; try again",
    conectar: "we couldn't connect; try again",
    conectarInternet: "we couldn't connect; check your internet and try again",
    atoro: "something got stuck; try again",
    yaTieneCuenta: "That email already has an account. Log in.",
    escribeCorreo: "Type your email above and tap again.",
  },
  avisos: {
    codigoEnviado: "We sent a code to your email.",
    codigoNuevo: "New code sent to your email.",
    confirmacionReenviada: "We sent the confirmation email again. Check your inbox.",
  },
  revisaCorreo: {
    titulo: "Check your email",
    texto: "We sent a link to <correo/> to confirm your account. Open it and you're in. (If you don't see it, check your spam.)",
  },
  resetEnviado: {
    titulo: "Link sent",
    texto: "If <correo/> has an account, a link to choose a new password is on its way. Check your inbox (and your spam).",
  },
  volver: "Back",
  desafio: {
    titulo: "One more step: your two-step verification",
    escribeRescate: "Type one of your recovery codes.",
    etiquetaRescate: "Recovery code",
    escribeCodigoApp: "Type the code from your authenticator app.",
    etiquetaCodigo: "6-digit code",
    verificando: "Verifying…",
    verificar: "Verify",
    reenviarCodigo: "Send me the code again",
    volverNormal: "Back to the regular code",
    usarRescate: "I don't have my code: use a recovery code",
  },
  noInvitado: {
    titulo: "My Idea is in private beta.",
    texto:
      "That email isn't on the guest list yet (it's the same list for signing in with a password or with Google). If someone invited you, ask them to double-check the email they registered.",
    otroCorreo: "Try another email",
  },
  entrar: "Log in",
  crearCuenta: "Create account",
  enlaceVencido: "That link has expired or was already used. Request a new one below.",
  googleFallo: "We couldn't finish signing you in with Google. Try again, or log in with your password.",
  etiquetaCorreo: "Email",
  placeholderCorreo: "you@email.com",
  etiquetaContrasena: "Password",
  placeholderContrasena: "Your password",
  reglasContrasena: "At least {{n}} characters, one uppercase letter, and one number.",
  reenviarConfirmacion: "Send me the confirmation email again",
  unMomento: "One moment…",
  crearMiCuenta: "Create my account",
  olvide: "I forgot my password",
  separador: "or",
  continuarGoogle: "Continue with Google",
};

export const LOGIN: PorIdioma<typeof esLogin> = { es: esLogin, en: enLogin };

const esClaveNueva = {
  noCoinciden: "Las dos contraseñas no coinciden.",
  enlaceVencido: "Ese enlace ya venció o ya se usó. Pide uno nuevo desde 'Olvidé mi contraseña'.",
  noActualizo: "No pudimos actualizar tu contraseña; intenta de nuevo.",
  conectarInternet: "no pudimos conectar; revisa tu internet e intenta de nuevo",
  lema: "Elige tu nueva contraseña.",
  actualizada: "Contraseña actualizada. Entrando…",
  etiquetaNueva: "Nueva contraseña",
  placeholderNueva: "Nueva contraseña",
  etiquetaRepetir: "Repetir contraseña",
  placeholderRepetir: "Repite tu contraseña",
  reglas: "Al menos {{n}} caracteres, una mayúscula y un número.",
  guardando: "Guardando…",
  guardar: "Guardar contraseña",
};

const enClaveNueva: typeof esClaveNueva = {
  noCoinciden: "The two passwords don't match.",
  enlaceVencido: "That link has expired or was already used. Request a new one from 'I forgot my password'.",
  noActualizo: "We couldn't update your password; try again.",
  conectarInternet: "we couldn't connect; check your internet and try again",
  lema: "Choose your new password.",
  actualizada: "Password updated. Logging you in…",
  etiquetaNueva: "New password",
  placeholderNueva: "New password",
  etiquetaRepetir: "Repeat password",
  placeholderRepetir: "Repeat your password",
  reglas: "At least {{n}} characters, one uppercase letter, and one number.",
  guardando: "Saving…",
  guardar: "Save password",
};

export const CLAVE_NUEVA: PorIdioma<typeof esClaveNueva> = { es: esClaveNueva, en: enClaveNueva };

/** lib/password.ts: el problema de la contraseña en palabras de persona. */
const esReglasClave = {
  corta: "Tu contraseña necesita al menos {{n}} caracteres.",
  sinMayuscula: "Tu contraseña necesita al menos una letra mayúscula.",
  sinNumero: "Tu contraseña necesita al menos un número.",
};

const enReglasClave: typeof esReglasClave = {
  corta: "Your password needs at least {{n}} characters.",
  sinMayuscula: "Your password needs at least one uppercase letter.",
  sinNumero: "Your password needs at least one number.",
};

export const REGLAS_CLAVE: PorIdioma<typeof esReglasClave> = { es: esReglasClave, en: enReglasClave };
