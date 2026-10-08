# Instrucciones del juez: ¿la neutral pregunta lo mismo que su base, en el mismo sentido?

My Idea entrevista a personas que quieren llevar una idea a la práctica. Cada pregunta tiene una **base** (escrita
para cualquiera; a veces supone un jefe, un equipo o socios) y una **versión neutral**: la misma pregunta sin suponer
papeles ni estructuras que la persona puede no tener, en tuteo neutro y en masculino genérico. La neutral se muestra
cuando la adaptación al caso de la persona falla, así que tiene que preguntar **exactamente lo mismo que la base, en el
mismo sentido**. Muchas neutrales son la base palabra por palabra; otras solo cambian unas pocas palabras.

Vas a juzgar pares base/neutral. Juzga SOLO con lo que trae el paquete: no abras otros archivos.

## Para cada par, un veredicto

- `fiel`: la neutral pregunta lo mismo, en el mismo sentido. Quitar un papel supuesto o volverlo condicional ("tu
  equipo, si lo tienes") está bien.
- `cambio_de_sentido`: la neutral pregunta otra cosa o lo contrario: cambia una negación o un límite ("no", "sin",
  "solo", "más", "menos"), un término del tema (franquicias, proveedores, clientes, exportar...), una opción, una
  cifra, un plazo o el orden de los hechos ("antes", "después"), o pierde o añade un foco.
- `papel_supuesto`: la neutral sigue dando por hecho un papel o una estructura (jefe, equipo, socios, empleados, un
  grupo) que la persona puede no tener.
- `otro`: cualquier otro defecto que no cambia el sentido: marca el género de la persona ("tú misma", "si trabajas
  sola"), voz de libro ("el libro", "el autor"), voseo, una forma rota.

Si dudas entre `fiel` y otro veredicto, elige el otro y explícalo: un falso hallazgo se descarta después, uno que se
calla no se recupera.

## Salida

Escribe un archivo JSON con esta forma exacta, un objeto por par del paquete y en el mismo orden:

```json
{"paquete": "n01", "veredictos": [{"id": "n01-01", "veredicto": "fiel", "motivo": "una frase"}]}
```

El motivo es obligatorio cuando el veredicto no es `fiel`.
