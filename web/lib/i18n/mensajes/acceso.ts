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

export const LOGIN: PorIdioma<typeof esLogin> = { es: esLogin };

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

export const CLAVE_NUEVA: PorIdioma<typeof esClaveNueva> = { es: esClaveNueva };

/** lib/password.ts: el problema de la contraseña en palabras de persona. */
const esReglasClave = {
  corta: "Tu contraseña necesita al menos {{n}} caracteres.",
  sinMayuscula: "Tu contraseña necesita al menos una letra mayúscula.",
  sinNumero: "Tu contraseña necesita al menos un número.",
};

export const REGLAS_CLAVE: PorIdioma<typeof esReglasClave> = { es: esReglasClave };
