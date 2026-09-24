/**
 * Fase 3.0: limites duros compartidos por las rutas de API (defensa de
 * seguridad pedida explicitamente en el prompt de la Fase 3.0: cap de
 * 4000 caracteres por mensaje de usuario).
 */
export const MAX_LARGO_TEXTO_USUARIO = 4000;

/** AUD-09 H03: el rechazo por texto largo, en palabras de persona y con su
 * límite. Viaja con `limite` para que la pantalla lo muestre tal cual. */
export const MENSAJE_TEXTO_LARGO = `Tu texto pasa de ${MAX_LARGO_TEXTO_USUARIO} caracteres. Recórtalo un poco y seguimos.`;
