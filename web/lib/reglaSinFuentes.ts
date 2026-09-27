/**
 * REGLA ESTRICTA del fundador (26 sep 2026): el cliente NUNCA ve el titulo de un libro ni un autor citado como
 * fuente, tampoco en una respuesta de la IA. Viaja en TODA llamada a la IA como un bloque fijo de sistema, despues
 * del prompt cacheado (lib/i18n/idiomaSalida.ts, bloquesDeSistema), asi que vale para los prompts del motor y para
 * los que nacieron en TS, y para los que vengan. Guarda: lib/reglaSinFuentes.test.ts.
 */
export const REGLA_SIN_FUENTES =
  "SIN FUENTES: jamás nombres el título de un libro ni cites a un autor como fuente de lo que dices " +
  "(nada de 'según Blank', 'como explica el libro', 'en su libro', 'propuesto por Osterwalder', 'Deming dice'), " +
  "aunque el material que recibes los mencione: lo que dices lo dices tú, con tus palabras. Un concepto que lleva " +
  "un nombre propio es vocabulario del oficio y sí puedes usarlo (el ciclo de Deming, las cinco fuerzas de Porter, " +
  "el diagrama de Ishikawa).";
