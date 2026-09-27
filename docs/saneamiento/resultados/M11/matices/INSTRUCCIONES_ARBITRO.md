# ARBITRO DEL PASE DE MATICES (limpieza M11, 28 sep 2026)

Lee antes `matices/INSTRUCCIONES.md` (lo que buscaba el lector). Cada caso de tu entrada trae el texto ACTUAL (un
`resumen` con sus lineas del libro y los pasos, o un paso/entregable/condicion con `viejo` y `nuevo`), el `tipo` y la
`objecion` del lector de matices, y su `propuesta_lector`. Los libros estan en `C:\Users\AlexDesk\Documents\forja-lectura\`
+ `fuentes/...`: lee el pasaje real cuando haga falta.

Decide por caso:
- "actual": la objecion no se sostiene; el texto actual se queda.
- "lector": la propuesta del lector es correcta tal cual.
- "propio": ni una ni otra; escribes tu el texto.

La vara: el texto dice lo que dicen las lineas y los pasos, con sus matices (a menudo, algunos, suele, puede,
probablemente); una experiencia de una persona se cuenta como caso ("una directiva", "hay quien", "en un equipo"); no
se inventan causas ni efectos. OJO: el resumen tiene que decir que sostiene el procedimiento y por que funciona, PERO
solo con la razon que dan las lineas o los pasos; si el libro no da la razon, el resumen describe lo que sostiene el
procedimiento sin inventarla. Mira la propuesta del lector con la misma vara: a veces quita un matiz y mete otro, o
se queda corta de largo. Voz de la casa: espanol con tildes, tu (nunca usted, ustedes ni vosotros, ni plural implicito
dirigido al lector), sin guiones largos o medios ni tres puntos, sin voz de libro, sin autores ni personajes con
nombre, sin ingles. Un resumen final mide de 400 a 600 caracteres: cuentalos con un script. No uses "se espera", "se
recomienda", "se debe", "se traduce", "su equipo" ni "el equipo de" (barandas de la casa).

Salida `matices/arbitro_salida_NN.json` en UTF-8:
{"lote": "NN", "casos": [{"item": "...", "tipo": "...", "decision": "actual"|"lector"|"propio", "texto_final": "...", "motivo": "..."}]}
con TODOS los casos de tu entrada (en "actual", texto_final = el texto actual).
