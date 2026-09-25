/**
 * Fase 3.0: limites duros compartidos por las rutas de API (defensa de
 * seguridad pedida explicitamente en el prompt de la Fase 3.0: cap de
 * 4000 caracteres por mensaje de usuario).
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolar } from "./i18n/interpolar";
import { SERVIDOR_COMUN } from "./i18n/mensajes/servidorComun";

export const MAX_LARGO_TEXTO_USUARIO = 4000;

/** AUD-09 H03: el rechazo por texto largo, en palabras de persona y con su
 * límite. Viaja con `limite` para que la pantalla lo muestre tal cual. */
export function mensajeTextoLargo(idioma: Locale = LOCALE_BASE): string {
  return interpolar(elegir(SERVIDOR_COMUN, idioma).textoLargo, { limite: MAX_LARGO_TEXTO_USUARIO });
}
export const MENSAJE_TEXTO_LARGO = mensajeTextoLargo(LOCALE_BASE);

/** El tope de la IDEA (decisión del fundador, 27 sep 2026): 12.000 caracteres,
 * para dictar ideas ricas. Solo la idea (ordenarla y empezar su exploración):
 * entra una vez y luego se lee de caché. Las respuestas siguen en
 * MAX_LARGO_TEXTO_USUARIO porque cada una se arrastra en toda la sesión. */
export const MAX_LARGO_IDEA = 12_000;
export function mensajeIdeaLarga(idioma: Locale = LOCALE_BASE): string {
  return elegir(SERVIDOR_COMUN, idioma).ideaLarga;
}
export const MENSAJE_IDEA_LARGA = mensajeIdeaLarga(LOCALE_BASE);

/** AUD-09 H07: el aviso de que las ideas escritas como invitado todavía no
 * llegaron a la cuenta (la adopción se reintentó y siguió fallando; queda
 * anotada y se reintenta en cada ingreso). */
export function mensajeAdopcionPendiente(idioma: Locale = LOCALE_BASE): string {
  return elegir(SERVIDOR_COMUN, idioma).adopcionPendiente;
}
export const MENSAJE_ADOPCION_PENDIENTE = mensajeAdopcionPendiente(LOCALE_BASE);
