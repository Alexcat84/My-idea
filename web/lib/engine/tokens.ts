/**
 * tokens.ts - Fase 3.0: port de _tokens_cosecha en prototipo_motor.py.
 * Usado por _elegir_por_afinidad (respaldo tier-2 del interprete) y por
 * la cosecha de vecindario del redactor de planes.
 */
const STOPWORDS_COSECHA = new Set(
  (
    "de la el en y a los las que para con su sus un una como al del por se es " +
    "son o u e no ya mas tu tus este esta estos estas"
  ).split(" ")
);

export function tokensCosecha(texto: string): Set<string> {
  // NFKD + strip de marcas diacriticas combinantes, igual que
  // unicodedata.normalize("NFKD", ...) + filtrar unicodedata.combining(c).
  const ascii = texto
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "");
  const palabras = ascii.match(/[a-z0-9]+/g) ?? [];
  return new Set(palabras.filter((w) => !STOPWORDS_COSECHA.has(w) && w.length > 2));
}
