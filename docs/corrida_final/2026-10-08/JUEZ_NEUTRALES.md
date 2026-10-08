# Instrucciones del juez: ¿la neutral busca lo mismo que su base?

My Idea entrevista a personas que quieren llevar una idea a la práctica. Cada pregunta tiene una **base** (escrita
para cualquiera; a veces supone un jefe, un equipo o socios) y una **versión neutral**: la misma pregunta dicha sin
suponer papeles ni estructuras que la persona puede no tener, en tuteo neutro. La neutral es la que ve la persona
cuando la adaptación a su caso falla, así que tiene que buscar exactamente lo mismo que la base.

Vas a juzgar pares base/neutral. Juzga SOLO con lo que trae el paquete: no abras otros archivos.

## Para cada par, un veredicto

- `fiel`: la neutral busca la misma información y sirve para lo mismo que la base. Cambiar la forma, quitar un papel
  supuesto o plantearlo en condicional está bien.
- `no_fiel`: la neutral busca otra cosa, pierde el foco de la base o le añade uno que la base no tiene.
- `papel_supuesto`: la neutral da por hecho un papel o una estructura (jefe, equipo, socios, empleados, recursos
  humanos) que la persona puede no tener.
- `otro`: la neutral habla con voz de libro ("el libro", "el autor", "como se explica"), cita una fuente, inventa una
  cifra, un plazo o una norma, o marca el género de la persona ("tú misma", "si trabajas sola", "te sientes preparada"):
  a la persona se le habla en masculino genérico.

Si dudas entre `fiel` y otro veredicto, elige el otro y explícalo: un falso hallazgo se descarta después, uno que se
calla no se recupera.

## Salida

Escribe un archivo JSON con esta forma exacta, un objeto por par del paquete y en el mismo orden:

```json
{"paquete": "n01", "veredictos": [{"id": "n01-01", "veredicto": "fiel", "motivo": "una frase"}]}
```

El motivo es obligatorio cuando el veredicto no es `fiel`.
