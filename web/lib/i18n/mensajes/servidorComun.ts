/** Mensajes compartidos del servidor: los que arman lib/mensajeServidor.ts,
 * lib/constants.ts, lib/rateLimit.ts, lib/creditos.ts, lib/seguridad.ts y
 * lib/identidad.ts, y que muchas rutas devuelven en `error`. */
import type { PorIdioma } from "../config";

const es = {
  /** lib/mensajeServidor.ts: el genérico, solo cuando el servidor no dio razón. */
  errorGenerico: "algo se atoró de nuestro lado; intenta de nuevo en un momento",
  /** lib/constants.ts */
  textoLargo: "Tu texto pasa de {{limite}} caracteres. Recórtalo un poco y seguimos.",
  ideaLarga: "Tu idea pasa de 12.000 caracteres. Recórtala un poco y seguimos.",
  adopcionPendiente:
    "Algunas ideas que escribiste antes de entrar todavía no llegan a tu cuenta. Lo reintento cada vez que entras; no se perdió nada.",
  /** lib/rateLimit.ts */
  limiteDiario:
    "Por hoy alcanzaste el límite de la beta ({{arranques}} al día). Tus ideas quedan guardadas. Vuelve mañana y seguimos donde quedamos.",
  arranques: { one: "{{n}} arranque", other: "{{n}} arranques" },
  fusible: "Estamos a capacidad por hoy; tus ideas te esperan mañana.",
  /** lib/creditos.ts: el 402 en palabras de persona. */
  saldoInsuficiente: "Te quedan {{creditos}}; esto cuesta {{costo}}. Tu trabajo queda guardado tal como está.",
  saldoInsuficienteConApartados:
    "Tienes {{creditos}} y {{apartados}} para un plan que tienes en curso; esto cuesta {{costo}}. Tu trabajo queda guardado tal como está.",
  creditos: { one: "{{n}} crédito", other: "{{n}} créditos" },
  apartados: { one: "{{n}} ya está apartado", other: "{{n}} ya están apartados" },
  /** lib/seguridad.ts: el 403 de frontera del segundo factor. */
  aviso2FA: "Tu cuenta tiene verificación en dos pasos. Confirma tu segundo factor y seguimos justo donde quedaste.",
  /** lib/identidad.ts: el 401 de frontera. */
  avisoLogin: "Para explorar tu idea necesitas tu cuenta. Entra con tu correo y seguimos justo donde quedaste.",
};

const en: typeof es = {
  errorGenerico: "something got stuck on our end; try again in a moment",
  textoLargo: "Your text is over {{limite}} characters. Trim it a little and we'll keep going.",
  ideaLarga: "Your idea is over 12,000 characters. Trim it a little and we'll keep going.",
  adopcionPendiente:
    "Some ideas you wrote before logging in haven't reached your account yet. I retry every time you log in; nothing was lost.",
  limiteDiario:
    "You've reached today's beta limit ({{arranques}} a day). Your ideas are saved. Come back tomorrow and we'll pick up where we left off.",
  arranques: { one: "{{n}} start", other: "{{n}} starts" },
  fusible: "We're at capacity for today; your ideas will be waiting for you tomorrow.",
  saldoInsuficiente: "You have {{creditos}} left; this costs {{costo}}. Your work is saved just as it is.",
  saldoInsuficienteConApartados:
    "You have {{creditos}}, and {{apartados}} for a plan you have in progress; this costs {{costo}}. Your work is saved just as it is.",
  creditos: { one: "{{n}} credit", other: "{{n}} credits" },
  apartados: { one: "{{n}} is already set aside", other: "{{n}} are already set aside" },
  aviso2FA: "Your account has two-step verification. Confirm your second factor and we'll pick up right where you left off.",
  avisoLogin: "To explore your idea, you need your account. Log in with your email and we'll pick up right where you left off.",
};

export const SERVIDOR_COMUN: PorIdioma<typeof es> = { es, en };
