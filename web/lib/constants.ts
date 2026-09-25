/**
 * Fase 3.0: limites duros compartidos por las rutas de API (defensa de
 * seguridad pedida explicitamente en el prompt de la Fase 3.0: cap de
 * 4000 caracteres por mensaje de usuario).
 */
export const MAX_LARGO_TEXTO_USUARIO = 4000;

/** AUD-09 H03: el rechazo por texto largo, en palabras de persona y con su
 * límite. Viaja con `limite` para que la pantalla lo muestre tal cual. */
export const MENSAJE_TEXTO_LARGO = `Tu texto pasa de ${MAX_LARGO_TEXTO_USUARIO} caracteres. Recórtalo un poco y seguimos.`;

/** El tope de la IDEA (decisión del fundador, 27 sep 2026): 12.000 caracteres,
 * para dictar ideas ricas. Solo la idea (ordenarla y empezar su exploración):
 * entra una vez y luego se lee de caché. Las respuestas siguen en
 * MAX_LARGO_TEXTO_USUARIO porque cada una se arrastra en toda la sesión. */
export const MAX_LARGO_IDEA = 12_000;
export const MENSAJE_IDEA_LARGA = "Tu idea pasa de 12.000 caracteres. Recórtala un poco y seguimos.";

/** AUD-09 H07: el aviso de que las ideas escritas como invitado todavía no
 * llegaron a la cuenta (la adopción se reintentó y siguió fallando; queda
 * anotada y se reintenta en cada ingreso). */
export const MENSAJE_ADOPCION_PENDIENTE =
  "Algunas ideas que escribiste antes de entrar todavía no llegan a tu cuenta. Lo reintento cada vez que entras; no se perdió nada.";
