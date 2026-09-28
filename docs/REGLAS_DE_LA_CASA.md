# Reglas de la casa

Principios de producto que mandan sobre el código, los prompts y los datos. Cada regla lleva su fecha, quién la decidió
y por qué existe. Las reglas de proceso del repositorio viven en `AGENTS.md`; la voz y el copy, en
`docs/BANCO_DE_TEXTOS.md`. Este fichero nació el 28 sep 2026 con su primera regla.

## 1. Las preguntas de la caché son PREGUNTAS BASE, no ley

**Decisión del fundador con el auditor, 28 sep 2026.**

Las preguntas guardadas en `preguntas_cache.json` son preguntas base: dicen QUÉ hay que averiguar en ese punto del
camino para elegir el siguiente paso. No son el texto que la persona tiene que leer.

- **La adaptación cambia la FORMA, nunca el FONDO.** Se ajustan el papel (dueña, empleado, directivo), el contexto
  (tamaño del equipo, sector, etapa) y las palabras de la persona. La pregunta adaptada tiene que buscar lo mismo que
  la base: si una respuesta a la adaptada no serviría para elegir entre los mismos siguientes pasos, la adaptación está
  mal.
- **Nunca se suponen roles ni estructuras que la persona no mencionó.** Si la base supone un jefe, un departamento de
  recursos humanos o varios niveles de mando y la persona es dueña de su negocio, se adapta a quien cumple ese papel en
  su caso o se pregunta en condicional.
- **La salida segura, si la adaptación falla, es una versión NEUTRAL sin roles supuestos, nunca la base cruda.** Una
  pregunta que le habla de "tu propio jefe" a una persona que no lo tiene rompe la conversación más que una pregunta
  sencilla.

**Por qué:** en el vuelo del 27 sep 2026 la entrevista del mundo 11 le preguntó a un dueño de taller por su propio
jefe y por recursos humanos. El fallo no era del dataset ni del mundo: era de los prompts y de la secuencia, y afecta
a todos los mundos. El diagnóstico está en `docs/producto/CONTEXTO_ENTREVISTA.md`.

**Dónde vive:** el adaptador (`web/lib/engine/adaptadorPregunta.ts`), la versión neutral en el campo aparte
`pregunta_neutral` de la caché (`engine/build_question_cache.py --neutrales`) y la regla única que viaja en toda
llamada a la IA (`web/lib/reglaContextoUsuario.ts`).

## 2. Memoria de contexto de principio a fin

**Principio 1 del fundador, 28 sep 2026.**

El contexto completo de la persona viaja siempre: en cada turno, en cada llamada a la IA, al pasar de una sesión a otra
y al abrir cada mundo, que recibe todo lo del núcleo y de los mundos anteriores. Se guarda en la base del proyecto y se
actualiza en cada turno.

- **La ficha de contexto** (papel, si tiene jefe, equipo, sector, etapa, prioridad declarada y frases textuales) la
  actualiza el intérprete en la misma llamada de cada turno. Un dato desconocido nunca pisa uno conocido; las frases
  solo se añaden.
- **El hilo** guarda cada pregunta y cada respuesta de todas las sesiones, en orden, solo añadiendo.
- **Al abrir una sesión** se fija la foto del proyecto (idea, estado vivo, ficha e hilo), y la ficha de ese momento
  viaja aparte en cada turno. La prioridad declarada también pasa de una sesión a la siguiente.
- **Ninguna salida de la IA se guarda cortada:** toda llamada mira si se quedó sin tokens, reintenta con más o falla
  con aviso. Las tareas del checklist se guardan completas y solo se acortan al mostrarlas.

**Por qué:** en el vuelo del 27 sep 2026 el intérprete perdía la idea y el perfil desde el segundo turno, y un mundo
nuevo no sabía nada de lo que la persona había contado en el núcleo.

**Dónde vive:** `projects.memoria` (migración 049), `web/lib/engine/memoria.ts`, `anotarEnMemoria` en `web/lib/db.ts`.

## 3. Nada se elimina ni se cambia

**Principio 2 del fundador, 28 sep 2026.**

- **Ningún nodo se quita ni se salta por el papel de la persona:** todos se adaptan.
- **Las preguntas base de la caché se quedan EXACTAMENTE como están.** Las versiones neutrales van en un campo aparte.
  Nada regenera una base: el generador solo añade (`--faltantes`, `--neutrales`) y `--patch` ya no pisa una base.
- **Los nodos con siguientes y sin pregunta** reciben una nueva, que se AÑADE.
- **Queda cancelada la regeneración de las preguntas en voseo:** el adaptador las dice en tuteo neutro al momento, y
  su versión neutral también.

**Por qué:** una pregunta base guarda una intención que costó construir. Si se regenera, se pierde; si se adapta al
decirla, se conserva y además le habla a la persona real.

## 4. El caché de la IA tiene un orden fijo

**Principio 3 del fundador, 28 sep 2026.**

Toda llamada va en el mismo orden: primero lo fijo (el prompt, la regla sin fuentes y la regla única), después el
contexto del proyecto (la foto y la ficha), después el turno. El historial crece solo por el final.

- **Lo fijo y el contexto del proyecto, con caché de 1 hora. El resto, con caché de 5 minutos.**
- **Por qué 1 hora ahí:** escribir en el caché de 1 hora cuesta 2 veces la entrada normal; en el de 5 minutos, 1,25
  veces; leer cuesta 0,1. Una sesión tiene entre 4 y 13 turnos (vuelo del 27 sep 2026), y entre turno y turno la
  persona piensa y escribe. Con 5 minutos, cada pausa más larga obliga a reescribir el prefijo (1,25 veces cada vez).
  Con 1 hora se paga 0,75 de más una sola vez. Basta una pausa larga en la sesión para que la hora salga más barata, y
  el prefijo se reutiliza en todos los turnos.
- **Por qué 5 minutos en el historial:** su final cambia en cada turno, así que se vuelve a escribir en cada turno de
  todas formas. Pagar el doble por una escritura que el turno siguiente ya deja atrás no compra nada.
- **Cada llamada deja registro** de sus tokens leídos del caché y escritos en él (1 hora y 5 minutos), y `costo_usd`
  los cobra con su tarifa.

**Dónde vive:** `web/lib/costmeter.ts` (`CACHE_1H`, `registrarUso`, `costoLlamadaUsd`) y
`web/lib/i18n/idiomaSalida.ts` (`bloquesDeSistema`).

## 5. Toda rúbrica que juzga preguntas mira papeles y contexto

**Decisión del fundador, 28 sep 2026.**

Toda verificación de preguntas, sea un juez automático o una lectura ciega, mira además si la pregunta supone un papel
o una estructura que la persona no tiene: un jefe a quien es dueña de su negocio, recursos humanos, directivos, varios
departamentos, un equipo a quien trabaja sola. Una pregunta así es un fallo aunque parta bien del nodo y sirva para
elegir el siguiente paso.

**Por qué:** la verificación ciega de las preguntas de puerta del mundo 11 dio por buena la pregunta de "tu propio
jefe": miraba si partía de la situación del nodo y si servía para elegir, pero no los papeles.

**Dónde vive:** el juez de sesión (`desajustes_de_papel` en `SYSTEM_JUEZ_SESION`) y el juez de la prueba de coherencia.
Toda rúbrica nueva que juzgue preguntas lo lleva desde el primer día.
