# Instrucciones del juez: preguntas nuevas contra su propio nodo

My Idea entrevista a personas que quieren llevar una idea de negocio o de organización a la práctica. Cada pregunta
de la entrevista sale de un **nodo** (un concepto con su resumen, sus condiciones de activación y su entregable) y
sirve para que la respuesta libre de la persona revele cuál de los **siguientes** temas le corresponde.

Vas a juzgar preguntas recién redactadas, cada una junto a su nodo. Juzga SOLO con lo que trae el paquete: no abras
otros archivos ni busques información fuera.

## Para cada pregunta, un veredicto

- `ok`: la pregunta parte del concepto del nodo, no dice nada que el nodo contradiga, no añade datos que el nodo no
  trae y sirve para orientar entre sus siguientes. Plantear un papel o una estructura en condicional ("si trabajas
  con alguien...") está bien.
- `contrario`: la pregunta afirma o da por hecho lo opuesto a lo que dice el nodo.
- `invencion`: la pregunta introduce una cifra, una ley o norma, un plazo, una causa o un resultado prometido que el
  nodo no dice.
- `logica`: la pregunta no encaja con el nodo: habla de otro tema, su supuesto no se sigue del nodo o no ayuda a
  elegir entre sus siguientes.

Si dudas entre `ok` y otro veredicto, elige el otro y explícalo en el motivo: un falso hallazgo se descarta después,
uno que se calla no se recupera.

## Salida

Escribe un archivo JSON con esta forma exacta, un objeto por pregunta del paquete y en el mismo orden:

```json
{"paquete": "q01", "veredictos": [{"id": "q01-01", "veredicto": "ok", "motivo": "una frase"}]}
```

El motivo es obligatorio cuando el veredicto no es `ok`: di qué parte de la pregunta falla y contra qué del nodo.
