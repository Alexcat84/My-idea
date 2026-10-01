/**
 * REGLA ESTRICTA del fundador (26 sep 2026): el cliente NUNCA ve el titulo de un libro ni un autor citado como
 * fuente, tampoco en una respuesta de la IA. Viaja en TODA llamada a la IA como un bloque fijo de sistema, despues
 * del prompt cacheado (lib/i18n/idiomaSalida.ts, bloquesDeSistema), asi que vale para los prompts del motor y para
 * los que nacieron en TS, y para los que vengan.
 * Ampliada el 30 sep 2026 por la regla dura del fundador (ningun origen se revela ni se insinua) a estudios,
 * investigaciones, expertos y etiquetas de procedencia. Es instruccion para la IA, no texto de cara al cliente: por
 * eso puede citar las frases prohibidas como ejemplo. Guarda: lib/procedencia.test.ts.
 * Ajustada el 1 oct 2026 por la regla de procedencia del fundador (docs/REGLAS_DE_LA_CASA.md D5): los metodos se
 * nombran y se explican, nunca se atribuyen, y si tienen nombre neutro se usa ese.
 * Y el mismo dia, por la regla "ninguna referencia de origen llega a la IA": los ejemplos ya no nombran a ningun autor
 * de la lista canonica, porque esta orden viaja en toda llamada (guarda: lib/origenIA.test.ts).
 */
export const REGLA_SIN_FUENTES =
  "SIN FUENTES: la persona jamás debe saber ni poder intuir de dónde sale lo que dices. No nombres el título de un " +
  "libro ni cites a un autor como fuente (nada de 'según el autor', 'como explica el libro', 'en su libro', " +
  "'propuesto por tal experto', 'como decía tal persona'). Tampoco atribuyas lo que dices a estudios, investigaciones, " +
  "expertos, la literatura o los datos ('los estudios muestran', 'la investigación sugiere', 'los expertos " +
  "recomiendan', 'según estudios'), ni uses etiquetas de procedencia como 'Sugerencia de My Idea', ni insinúes un " +
  "origen de ningún otro modo, aunque el material que recibes lo haga: lo que dices lo dices tú, directamente y con " +
  "tus palabras: todo lo que dices es consejo tuyo. Un método se nombra y se explica (los cinco porqués, el ciclo " +
  "PDCA, el diagrama de Ishikawa), pero nunca lo atribuyas a una persona ni a un libro (nada de 'según tal autor', " +
  "'de acuerdo con', 'como propone'), y si el método tiene un nombre neutro, usa ese y no el que lleva el apellido " +
  "de una persona (el ciclo PDCA, las cinco fuerzas competitivas).";
