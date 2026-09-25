/** Mensajes de las rutas de cuenta y acceso: app/api/auth/** (registrar,
 * entrar, reset, reenviar), app/api/cuenta/eliminar y los comunes que
 * comparten con las rutas del doble factor (app/api/cuenta/2fa/**). */
import type { PorIdioma } from "../config";

const es = {
  comun: {
    cuerpoInvalido: "cuerpo invalido",
    necesitasCuenta: "necesitas tu cuenta para esto",
    algoSeAtoro: "algo se atoró; intenta de nuevo",
    algoSeAtoroMomento: "algo se atoro de nuestro lado; intenta de nuevo en un momento",
    correoInvalido: "escribe un correo valido",
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

export const SERVIDOR_CUENTA: PorIdioma<typeof es> = { es };
