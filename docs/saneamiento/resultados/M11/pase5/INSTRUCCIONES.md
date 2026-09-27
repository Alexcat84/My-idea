# QUINTO PASE DE LA LIMPIEZA M11 (28 sep 2026): invenciones y contrarios

Lee ENTERAS `C:\Users\AlexDesk\Documents\m11-trabajo\auditoria\INSTRUCCIONES.md` (la vara, los tipos, el formato de
salida y lo que NO es defecto) y las dos varas que cita. Ademas: el leismo de persona masculina esta admitido;
"superestrella" y "estrella de rock" son los dos perfiles del metodo; "salida" en par con "entrada" en un modelo de
proceso no es defecto; "a tu cargo" / "a su cargo" es la forma fijada.

Este pase existe porque la muestra ciega final 4, en 50 nodos ya auditados cuatro veces, encontro 1 INVENCION
confirmada: "Prueba la ambiguedad con un ejemplo concreto, que es como lo comprobaron" (el libro usa la pelicula como
ilustracion de su razonamiento, no cuenta que lo comprobaran asi). El umbral del fundador es CERO invenciones y cero
contrarios. Este pase busca SOLO eso: invencion (una causa, un efecto, una finalidad, una procedencia, una cifra o un
contenido que el libro no dice) y contrario (el texto dice lo contrario que el libro o cambia quien hace que). Un
absoluto ("siempre", "nunca", "todos", "nadie") donde el libro matiza es `matiz`; marcalo tambien.

## Clausulas (obligatorio, una por una)

Cada nodo trae `clausulas`: los puntos donde el texto afirma una causa ("porque", "por eso", "asi que"), un efecto o
una finalidad ("para que", "evita que", "con eso"), una procedencia ("que es como"), un absoluto o una cifra. Para CADA
una: busca en el pasaje del libro (la evidencia) y en su capitulo lo que la sostiene. Si el libro lo dice (aunque con
otras palabras, o unas lineas antes o despues), no es defecto. Si no lo dice, o dice otra cosa, es defecto: marca el
tipo, la linea del libro que mas se acerca y la frase exacta en ingles, y propone el texto con la clausula quitada o
ajustada a lo que el libro dice (cambio minimo). Devuelve en cada nodo `clausulas_revisadas`: [{"campo": "...",
"marca": "...", "sostenida": true|false, "linea": "..."}] con TODAS las clausulas del nodo.

Lee ademas el nodo entero buscando otras invenciones o contrarios que no lleven marca (un efecto dicho sin "porque",
una atribucion a quien no hizo algo). No marques en este pase calcos, regionalismos, voz ni coherencia salvo que sean
evidentes y graves.

No inventes defectos: cita el texto exacto y la linea del libro. Tu entrada y tu salida son las que te indiquen; el
formato de salida es el de `auditoria/INSTRUCCIONES.md` mas `clausulas_revisadas` en cada nodo.
