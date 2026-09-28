# AUDITORIA COMPLETA DEL PACK DEL MUNDO 11 (limpieza M11, 28 sep 2026)

Eres un AUDITOR. Tus nodos ya pasaron una limpieza; tu trabajo es encontrar lo que se le haya escapado. Lee
`C:\Users\AlexDesk\Documents\my-idea-integracion\docs\saneamiento\instrumentos\M11_LIMPIEZA.md` (la vara) y
`C:\Users\AlexDesk\Documents\m11-trabajo\matices\INSTRUCCIONES.md` (la vara de matices). Tu entrada trae, por nodo, todos
los textos que ve el cliente y la evidencia (fichero y lineas) del resumen; los libros estan en
`C:\Users\AlexDesk\Documents\forja-lectura\` + la ruta `fuentes/...`. LEE EL PASAJE: los pasos salen del mismo pasaje o de
su entorno; busca en el capitulo lo que no este en las lineas citadas antes de llamarlo invencion.

Revisa CADA texto de CADA nodo y anota todo defecto, con su `tipo`:
- `invencion`: una causa, un efecto, una cifra o un contenido que el libro no dice.
- `contrario`: el texto dice lo contrario que el libro, o cambia quien hace que.
- `matiz`: un matiz del libro perdido (often, can, may, might, tend to, most, some, probably...) o la experiencia de una
  persona vuelta regla general (cuentala como caso: "una directiva", "hay quien", "en un equipo").
- `calco`: calco del ingles ("se cuelan por las grietas", "cables cruzados", "escalar" por crecer, "salida no lamentada",
  "capturar", "honra el proceso") o ingles que quedo.
- `regionalismo`: forma de una sola region ("va a por ti", "tira de", "vale" de muletilla, "coger", "movil", "coche").
- `coherencia`: referente que no existe en el nodo ("la octava de las diez cosas", "la fabrica de desayunos", "esos
  casos" sin antecedente), condicion que no corresponde, sujeto ambiguo.
- `voz`: voz de libro, autores o personajes con nombre, usted/ustedes/vosotros, plural dirigido al lector, guiones largos
  o medios, "se espera", "se recomienda", "se debe", "se traduce", "su equipo", "el equipo de".
- `ortografia`.
NO son defecto (decisiones ya tomadas): "franqueza radical", "empatia ruinosa", "agresion odiosa" (el nombre que usa el pack, en 8 nodos), "insinceridad
manipuladora" como nombres del metodo; "jugador A", "metodo A", "tarjeta de puntuacion", "reunion de salto de nivel",
"el Pozo (el bache de desanimo)", "las cinco areas de la venta", "a tu cargo"; el femenino de una anecdota en tercera
persona; las cifras que estan en el libro; "palanca" y "palanca gerencial" (nombre del concepto de productividad del mando); "estrella de rock" y "estrella en ascenso" (los dos perfiles del metodo de crecimiento).

Se estricto pero no inventes defectos: cita el texto exacto y, en invencion, contrario y matiz, la linea del libro.
Por cada defecto da `propuesta`: el texto COMPLETO corregido con el cambio minimo, en espanol con tildes, en tu. Un
resumen_teorico mide de 400 a 600 caracteres (cuentalos con un script).

Salida `auditoria/salida_NN.json` en UTF-8:
{"lote": "NN", "nodos": [{"node_id": "...", "limpio": true|false, "defectos": [{"campo": "pasos_accionables[3]",
 "tipo": "...", "cita": "...", "motivo": "...", "fichero": "fuentes/... (en invencion, contrario, matiz)",
 "lineas": "...", "frase": "frase del libro en ingles (en invencion, contrario, matiz)", "propuesta": "..."}]}]}
con TODOS los nodos de tu entrada (compruebalo con un script).
