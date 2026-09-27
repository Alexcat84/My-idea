# CUARTO PASE DE LA LIMPIEZA M11 (28 sep 2026): coherencia, regionalismo, calco, voz y ortografia

Lee ENTERAS `C:\Users\AlexDesk\Documents\m11-trabajo\auditoria\INSTRUCCIONES.md` (la vara, los tipos, el formato de
salida y lo que NO es defecto) y las dos varas que cita. Ademas: el leismo de persona masculina esta admitido;
"superestrella" y "estrella de rock" son los dos perfiles del metodo de crecimiento; "salida" en par con "entrada" en un
modelo de proceso no es defecto; "a tu cargo" y "a su cargo" son la forma fijada.

Este pase existe porque la muestra ciega final 3, en 50 nodos ya auditados tres veces, encontro 11 defectos confirmados
(ninguna invencion, contrario ni matiz): 4 de COHERENCIA, 3 de REGIONALISMO, 2 de CALCO, 1 de VOZ y 1 de ORTOGRAFIA.
Este pase NO busca matices (el pase anterior los reviso frase por frase y la muestra dio 0); busca solo esos cinco tipos.
Ejemplos reales de la muestra 3:
- coherencia: "la persona a cargo" (se lee como quien manda; es "la persona a tu cargo"); "usa este mismo metodo" sin
  antecedente en el nodo; "Siempre, y no cuando se abre una vacante" (se contradice: es "no solo cuando").
- regionalismo: "pegas" (coloquial de Espana; "inconvenientes").
- calco: "como estas entregando el mensaje" (delivering: "transmitiendo"); "la guia entregada" ("dada").
- voz: "que pasen nuestra criba telefonica", "que deberiamos contratar" (el nosotros del libro; en la casa es tu).
- ortografia: "con duenos que por lo general no seas tu" (concordancia).

## 1. Avisos (obligatorio, uno por uno)

Cada nodo trae `avisos`: candidatos que un script encontro por lexico (regionalismos de ambos lados del Atlantico,
primera persona del plural, "a cargo" sin posesivo, calcos conocidos, demostrativos que pueden no tener antecedente,
longitud del resumen). NO son veredictos: muchos son correctos (un "nosotros" dentro de una frase que dice una persona
del caso, "vale la pena", "a cargo de un proyecto", "tiene sentido" bien usado). Juzga cada uno EN SU CONTEXTO; si es
defecto, marcalo con su tipo real y tu propuesta. Devuelve en cada nodo `avisos_revisados`: [{"campo": "...",
"texto": "...", "defecto": true|false}] con TODOS los avisos del nodo.

## 2. Lectura de coherencia interna (obligatoria)

Lee cada nodo como lo leeria el cliente, de arriba abajo: cada referente ("ese", "esa lista", "el caso", "la
directiva", "el metodo") tiene antecedente DENTRO del nodo; el sujeto no cambia de persona sin motivo (tu frente a el
caso de otra persona); el imperativo te habla a ti y no manda sobre objetos del caso de otro; ninguna condicion o paso
se contradice ni contradice a otro campo; la concordancia (genero, numero, tiempos) es correcta. Busca ademas calcos,
regionalismos y voz en todo el texto, no solo en los avisos.

Lee el pasaje del libro (forja-lectura + la evidencia) cuando lo necesites para decidir un calco o un referente; no hace
falta leerlo entero para cada nodo.

No inventes defectos: cita el texto exacto. Tu entrada y tu salida son las que te indiquen; el formato de salida es el
de `auditoria/INSTRUCCIONES.md` mas `avisos_revisados` en cada nodo.
