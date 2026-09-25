/**
 * /cuenta, el centro de cuenta: app/cuenta/page.tsx y ui/CuentaCliente.tsx.
 * La palabra de confirmación del borrado (ELIMINAR) NO está aquí: es un dato
 * que el servidor compara (/api/cuenta/eliminar), y entra a las frases por la
 * etiqueta <palabra/>.
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

export const CUENTA: PorIdioma<typeof es> = { es };
