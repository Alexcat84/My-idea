# TERCER PASE DE LA LIMPIEZA M11 (28 sep 2026): matiz dirigido y lo blando que queda

Lee ENTERAS `C:\Users\AlexDesk\Documents\m11-trabajo\auditoria\INSTRUCCIONES.md` (la vara, los tipos, el formato de
salida y lo que NO es defecto). Ademas: el leismo de persona masculina esta admitido; "superestrella" y "estrella de rock"
son los dos perfiles del metodo de crecimiento; "salida" en par con "entrada" en un modelo de proceso no es defecto.

Este pase existe porque la muestra ciega final 2, en 50 nodos ya auditados dos veces, encontro 11 defectos confirmados
(ninguna invencion ni contrario): 6 de MATIZ, 1 calco, 1 voz, 1 coherencia, 1 ortografia, 1 resumen demasiado largo.
El matiz es lo que mas se escapa: por eso este pase lo revisa con una lista.

## 1. Matiz dirigido (obligatorio, frase por frase)

Cada nodo de tu entrada trae `frases_con_matiz`: las frases de su pasaje del libro (las lineas de su evidencia) que
llevan una marca de matiz o de experiencia personal (can, may, might, often, usually, most, some, sometimes, probably,
likely, tend to, almost, virtually, "I've found", "I see", "in my experience"...). Para CADA frase de la lista:
1. Busca si algun texto del nodo (titulo, resumen, pasos, entregable, condiciones) cuenta ese contenido.
2. Si lo cuenta, comprueba que conserva el matiz: "can help" es "puede ayudar", no "ayuda"; "often" es "a menudo", no
   "siempre" ni nada; "most managers" es "casi todos" o "la mayoria", no "los jefes"; "I see virtually every new manager
   make" es lo que alguien ha visto ("hay quien ve", "es frecuente ver"), no un hecho general; "Sometimes, when..." es
   "a veces, cuando...".
3. Si lo pierde, es un defecto `matiz` en ese campo, con la linea y la frase del libro.
Lee la frase EN SU CONTEXTO (lineas de alrededor): "most important" no es un matiz; "can't" no se pierde si el texto dice
"no puedes"; "some" en "some of your reports" es una cantidad, no un matiz, si el texto no dice "todos".

Ejemplos reales de la muestra 2: "el error que comete practicamente todo directivo que empieza" (el libro: "that I see
virtually every apprentice manager make"); "cuando un aporte llegaba sin detalle escribia..." (el libro: "Sometimes,
when..."); "porque distrae" (el libro: "as it can be distracting"); "semanal y a seis meses" dado como regla cuando es
la costumbre de una persona dentro de "busca lo que mejor te funcione"; "si no tienes un historial" cuando el libro habla
de no tener un historial de grandes transformaciones.

Devuelve en cada nodo `matiz_revisado`: [{"linea": N, "usa": true|false, "conserva": true|false|null}] con TODAS las
frases de su lista (usa=false y conserva=null si el nodo no cuenta esa frase).

## 2. Lo blando que queda

Lee ademas cada texto buscando `calco`, `coherencia`, `voz`, `regionalismo` y `ortografia`, como en las instrucciones.
Ejemplos reales de la muestra 2: "conseguir una gran opinion" (calco de "great feedback"); "lo que se espera de su
puesto" (voz: "se espera"); "en vez de tratar todo el manuscrito, partelo" (coherencia: el imperativo te habla a ti y el
objeto era del caso); "Se humilde e habla" (ortografia).

## 3. Avisos mecanicos

Si un nodo trae `avisos` (resumen fuera de 400 a 600 caracteres, "y" ante sonido i), cada aviso es un defecto: marcalo
con tipo `longitud` u `ortografia` y da la propuesta (un resumen recortado o alargado con el cambio minimo, medido con
un script).

No inventes defectos: cita el texto exacto y, en matiz, la linea y la frase del libro. Tu entrada y tu salida son las que
te indiquen; el formato de salida es el de `auditoria/INSTRUCCIONES.md` mas `matiz_revisado` en cada nodo.
