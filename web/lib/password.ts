/**
 * password.ts — reglas de contraseña del login por correo+contraseña
 * (réplica del registerStep1Schema del I Ching: mín. 8, una mayúscula, un
 * dígito). Puras y testeables; las usan la ruta de registro y la UI.
 */
export const LARGO_MINIMO = 8;

/** Devuelve el problema de la contraseña en palabras de persona, o null si
 * es válida. */
export function validarPassword(password: string): string | null {
  if (password.length < LARGO_MINIMO) return `Tu contraseña necesita al menos ${LARGO_MINIMO} caracteres.`;
  if (!/[A-Z]/.test(password)) return "Tu contraseña necesita al menos una letra mayúscula.";
  if (!/[0-9]/.test(password)) return "Tu contraseña necesita al menos un número.";
  return null;
}

export function passwordValida(password: string): boolean {
  return validarPassword(password) === null;
}
