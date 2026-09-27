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
