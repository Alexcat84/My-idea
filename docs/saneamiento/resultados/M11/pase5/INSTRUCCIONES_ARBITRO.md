# ARBITRO DE LA AUDITORIA COMPLETA (limpieza M11, 28 sep 2026)

Lee antes `auditoria/INSTRUCCIONES.md` (la vara del auditor, sus tipos y lo que NO es defecto). Tu entrada
(`auditoria/arbitro_entrada_NN.json`) trae, por CAMPO de cada nodo, el texto actual, los defectos que marco el auditor
(tipo, cita, motivo, fichero, lineas, frase, propuesta) y los demas textos del nodo como contexto. Los libros estan en
`C:\Users\AlexDesk\Documents\forja-lectura\` + `fuentes/...`: LEE EL PASAJE antes de decidir.

CORRECCION DEL ORQUESTADOR (28 sep): la primera version de las instrucciones del auditor decia que el nombre fijado del
cuadrante es "agresividad molesta"; es un error: el pack usa "agresion odiosa" (8 nodos) y se queda. Un defecto que pida
cambiar "agresion odiosa" no se sostiene. Tampoco "palanca" (concepto de productividad del mando) ni "estrella de rock".

DECISIONES DEL ORQUESTADOR (segundo a quinto pase, 28 sep):
- Los dos perfiles del metodo de crecimiento son "superestrella" y "estrella de rock" (el libro: "Superstar", "Rock Star").
  "Estrella en ascenso" pasa a "superestrella". "Superestrella" no es defecto.
- "La salida" como traduccion de "output" (Grove) es calco: pasa a "la produccion" cuando habla de una fabrica u
  operacion que entrega algo, y a "el resultado" cuando habla de un mando, un equipo o una organizacion.
- El leismo de persona masculina esta admitido.

Por campo decide UN texto final:
- "actual": ningun defecto se sostiene; el texto se queda.
- "corregido": escribes el texto final con TODOS los defectos que se sostienen corregidos a la vez, con el cambio minimo
  (puedes tomar la propuesta del auditor si es correcta; mirala con la misma vara: a veces arregla uno y mete otro).
Voz de la casa: espanol con tildes, tu (nunca usted, ustedes ni vosotros), sin guiones largos o medios, sin voz de libro,
sin autores ni personajes con nombre, sin "se espera", "se recomienda", "se debe", "se traduce", "su equipo", "el equipo
de". Un resumen_teorico mide de 400 a 600 caracteres (cuentalos con un script).

Declara en cada "corregido":
- `veredicto`: el primero que aplique en este orden: CONTRARIO (contrario), ANADIDO (invencion o matiz), VOZ (calco,
  regionalismo, voz), COHERENCIA (coherencia), ORTOGRAFIA.
- en CONTRARIO y ANADIDO: `fichero` (ruta desde fuentes/), `lineas` y `frase` (la frase del libro, en ingles, exacta).
- en VOZ: `fragmentos`: los trozos EXACTOS del texto actual que salen y no quedan en el final.
- `tipos` (todos los que corriges) y `motivo`.

Salida `auditoria/arbitro_salida_NN.json` en UTF-8:
{"lote": "NN", "campos": [{"node_id": "...", "campo": "pasos_accionables[3]", "decision": "actual"|"corregido",
 "texto_final": "...", "veredicto": "...", "tipos": [...], "fichero": "...", "lineas": "...", "frase": "...",
 "fragmentos": [...], "motivo": "..."}]}
con TODOS los campos de tu entrada (compruebalo con un script).

TERCER PASE: los defectos de tipo `longitud` (resumen fuera de 400 a 600 caracteres) se declaran con veredicto
COHERENCIA y tipo "longitud", con el recorte minimo medido con un script. En `matiz`, lee la frase del libro EN SU
CONTEXTO: solo se sostiene si el texto cuenta ese mismo contenido y pierde el matiz ("some" como cantidad, "most
important" o un "can't" traducido por "no puedes" no son matices perdidos).

CUARTO PASE: "salida" en par con "entrada" en un modelo de proceso se queda. "a tu cargo" y "a su cargo" son la forma
fijada; "la persona a cargo" sin posesivo se lee como quien manda. Un regionalismo es una forma que un lector de otra
region no entenderia o leeria como ajena; si el mismo termino aparece en otros campos del nodo que estan en tu entrada,
decidelos igual. Un "nosotros" dentro de lo que dice una persona del caso, entre comillas, no es defecto.
DECISIONES DEL ORQUESTADOR PARA TODO EL PACK (cuarto pase, para que todos los lotes decidan igual): "tu persona a cargo",
"tus personas a cargo", "cada persona a cargo" y "la persona a cargo" pasan a la forma fijada ("la persona a tu cargo",
"las personas a tu cargo", "cada persona a tu cargo"; "a su cargo" cuando se habla de otro jefe). Las formas propias de
una sola region, aunque no sean coloquiales ("pegatina", "repostar", "cien por cien", "movil", "coche", "ordenador",
"auto", "carro", "celular", "computadora"), pasan a la forma neutra ("adhesivo", "cargar combustible", "cien por ciento",
"telefono", "vehiculo" o la palabra que calce, "computador" no: "equipo" o "portatil" segun el caso).
El "nosotros" GENERICO de quien escribe ("tendemos", "todos tenemos sesgos", "nos creemos", "nuestro problema") es voz de
libro: pasa a tu ("tiendes", "tienes sesgos, como todo el mundo") o a la tercera persona ("la gente tiende"). El
"nosotros" dentro de una frase que dice una persona (tu a tu equipo, una persona del caso, un ejemplo de lo que puedes
decir) se queda.

QUINTO PASE (invenciones y contrarios): una invencion es una causa, un efecto, una finalidad, una procedencia, una
cifra o un contenido que el libro no dice. Antes de confirmarla, busca en el pasaje Y en todo su capitulo: si el libro
lo dice con otras palabras, o unas lineas antes o despues, no es invencion. Un enfasis que no cambia lo que el libro
afirma no es invencion. Un absoluto donde el libro matiza es `matiz` (veredicto ANADIDO). La correccion es el cambio
minimo: quitar la clausula o ajustarla a lo que el libro dice. CONTRARIO y ANADIDO llevan fichero, lineas y la frase
exacta del libro.
