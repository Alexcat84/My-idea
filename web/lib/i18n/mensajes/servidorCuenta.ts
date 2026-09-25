/** Mensajes de las rutas de cuenta y acceso: app/api/auth/** (registrar,
 * entrar, reset, reenviar), app/api/cuenta/eliminar y los comunes que
 * comparten con las rutas del doble factor (app/api/cuenta/2fa/**). */
import type { PorIdioma } from "../config";

const es = {
  comun: {
    cuerpoInvalido: "cuerpo inválido",
    necesitasCuenta: "necesitas tu cuenta para esto",
    algoSeAtoro: "algo se atoró; intenta de nuevo",
    algoSeAtoroMomento: "algo se atoró de nuestro lado; intenta de nuevo en un momento",
    correoInvalido: "escribe un correo válido",
  },
  entrar: {
    faltanDatos: "escribe tu correo y tu contraseña",
    sinConfirmar: "Aún no confirmaste tu correo. Revisa tu bandeja (y el spam) o pide un enlace nuevo.",
    credencialesMalas: "Correo o contraseña incorrectos.",
  },
  registrar: {
    demasiadosIntentos: "Demasiados intentos por ahora. Espera unos minutos y vuelve a intentar.",
    noPudimosCrear: "no pudimos crear tu cuenta; intenta de nuevo en un momento",
  },
  eliminar: {
    escribeEliminar: 'Para borrar tu cuenta escribe la palabra "{{palabra}}" tal cual.',
    seguridadSinConfirmar:
      "No pude confirmar la seguridad de tu cuenta, así que no borré nada. Intenta de nuevo en un momento.",
    noPudeBorrarTodo: "No pude borrar todos tus datos, así que tu cuenta sigue igual. Intenta de nuevo en un momento.",
  },
};

const en: typeof es = {
  comun: {
    cuerpoInvalido: "invalid body",
    necesitasCuenta: "you need your account for this",
    algoSeAtoro: "something got stuck; try again",
    algoSeAtoroMomento: "something got stuck on our end; try again in a moment",
    correoInvalido: "enter a valid email",
  },
  entrar: {
    faltanDatos: "enter your email and password",
    sinConfirmar: "You haven't confirmed your email yet. Check your inbox (and your spam) or request a new link.",
    credencialesMalas: "Incorrect email or password.",
  },
  registrar: {
    demasiadosIntentos: "Too many attempts for now. Wait a few minutes and try again.",
    noPudimosCrear: "we couldn't create your account; try again in a moment",
  },
  eliminar: {
    escribeEliminar: 'To delete your account, type the word "{{palabra}}" exactly as shown.',
    seguridadSinConfirmar:
      "I couldn't verify your account's security, so I didn't delete anything. Try again in a moment.",
    noPudeBorrarTodo: "I couldn't delete all your data, so your account is unchanged. Try again in a moment.",
  },
};

export const SERVIDOR_CUENTA: PorIdioma<typeof es> = { es, en };
