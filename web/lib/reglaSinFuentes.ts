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
 * Y el 7 oct 2026, por decision del fundador (hallazgo C7 de docs/auditoria_final/informes/auditoria_prompts.md): sin
 * ejemplos de metodos con nombre, porque viajaban en toda llamada y le ofrecian a la IA metodos que el material de esa
 * llamada no traia. Un metodo se nombra solo si viene en el material.
 * Y el 9 oct 2026 (REDACTOR_CON_RESPALDO punto 1): el payload ya no se llama "material" sino "temas", y esta regla
 * prohibe citarlos como fuente; la ultima medicion sostuvo "El material enseña que..." como procedencia.
 */
export const REGLA_SIN_FUENTES =
  "SIN FUENTES: la persona jamás debe saber ni poder intuir de dónde sale lo que dices. No nombres el título de un " +
  "libro ni cites a un autor como fuente (nada de 'según el autor', 'como explica el libro', 'en su libro', " +
  "'propuesto por tal experto', 'como decía tal persona'). Tampoco atribuyas lo que dices a estudios, investigaciones, " +
  "expertos, la literatura o los datos ('los estudios muestran', 'la investigación sugiere', 'los expertos " +
  "recomiendan', 'según estudios'), ni uses etiquetas de procedencia como 'Sugerencia de My Idea', ni insinúes un " +
  "origen de ningún otro modo, aunque los temas que recibes lo hagan: lo que dices lo dices tú, directamente y con " +
  "tus palabras: todo lo que dices es consejo tuyo. Tampoco nombres como fuente los temas que recibes ('el material', " +
  "'los temas', 'el contenido de este plan', 'el método base'): la persona no sabe que existen. Un método se nombra " +
  "solo si viene en los temas que recibes, y " +
  "se explica sin atribuirlo a nadie, ni a una persona ni a un libro (nada de 'según tal autor', 'de acuerdo con', " +
  "'como propone'); si tiene un nombre neutro, usa ese y no el que lleva el apellido de una persona.";
