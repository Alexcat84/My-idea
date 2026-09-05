Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

ESTA ES UNA VUELTA DE BATERIA, Y ESO MANDA SOBRE TODO LO DEMAS.
AUDITOR.md 6.1, decision del fundador del 5 sep 2026: la bateria corre
CADA CINCO, en una VUELTA DE BATERIA propia QUE NO LLEVA NADA MAS. La
vuelta 174 fue la ultima intermedia y su encargo ya dejo escrito que la
proxima VUELTA DE BATERIA es la 175. NO HAY TRABAJO DE PLAN AL LADO:
OP-L-03 no se toca aqui, ni ninguna otra ficha.

LO QUE MI ACTA DE LA VUELTA 174 ADJUDICO Y NO HAY QUE VOLVER A DECIDIR:

- LOS SIETE DISCUTIBLES (D.1 a D.7) SE ADJUDICAN TODOS A TU FAVOR, y las
  dos preguntas tambien. La P.1: el tope de 80 lineas del modo austero
  NO RIGE, porque el austero se suspendio solo por su punto 5 al abrirse
  la fase 06 y las actas lo declaran sin interrupcion desde la 137. La
  P.2: las dos caidas de ruta del acta 172 NO acumulan hacia atras, por
  la letra SIN RETROACTIVIDAD del 2 sep y el precedente del 27 ago. El
  PD.1: no se estrena etiqueta de VIA, la glosa con su medicion al lado
  ya basta (EJECUTOR.md 1).
- LAS DOS RACHAS ESTAN EN CERO: cifra publicada cero y reporte cero. No
  publicaste ni una cifra falsa en toda la vuelta, y lo medi pieza a
  pieza.
- LA 174 ES LA PRIMERA DE LAS DOS SEGUIDAS que AUDITOR.md 6.2 pide para
  levantar el regimen temporal. ESTA VUELTA ES LA SEGUNDA, y por eso su
  reporte importa tanto como su bateria.
- REGIMEN TEMPORAL DE DOS SUB-TAREAS (AUDITOR.md 6.2), todavia vigente.
  POR ESO ESTE ENCARGO TRAE EXACTAMENTE DOS, y no una mas.

- TAREA 1, LA BATERIA ENTERA, SOLA Y CON SU DOBLE CORRIDA. Es la primera
  desde que el regimen cambio y lleva cuatro vueltas saliendo en cero
  bytes (171, 172, 173 y 174, esta ultima por regimen y no por caida).
  Va entera y sin aflojar ninguna guarda: la nomina completa, CADA
  ENTRADA CORRIDA DOS VECES (cotejo de reproducibilidad de la vuelta
  141), su reloj, y su salida SELLADA en docs/loop/SALIDA_V175_BATERIA.txt.
  Antes de nombrar esa ruta en ningun sitio, MIDELA: la regla LA RUTA QUE
  PROMETE PRUEBA ES CIFRA sigue viva y un fichero de cero bytes es caida
  de cifra.
  Y LA NOMINA AL DIA VA DENTRO DE ESTA MISMA TAREA, NO ES UNA TERCERA
  SUB-TAREA, y lo adjudico yo para que no lo tengas que decidir: es
  contrato del propio fichero, que cada arnes entre en la nomina a la
  vuelta siguiente. HOY FALTAN CINCO, no uno, medido por mi con la
  funcion pura arneses_que_faltan() de verificar_mutaciones_viejas.py:
  vuelta173_tarea1b_mutacion_hueco.py, vuelta174_tarea1a_mutacion_44.py,
  vuelta174_tarea1b_mutacion_esqueleto.py,
  vuelta174_tarea1b_mutacion_sellar.py y
  vuelta174_tarea2b_mutacion_confirmar.py. La lista VIEJAS esta en 82 y
  el directorio tiene 149. LA NOMINA NO SE PODA: crece, y podarla es lo
  que la casa reserva al fundador (AUDITOR.md 6.1, opcion c RECHAZADA).
- TAREA 2, ABRIR Y CERRAR TU PROPIO REPORTE, QUE ES LA SEGUNDA DE LAS DOS
  SEGUIDAS. Esqueleto al empezar, fila anexada al cerrarse la TAREA 1, y
  cierre con scripts/loop/cerrar_reporte.py en la misma vuelta. Ya lo
  hiciste una vez y salio: se hace igual. Y ARCHIVA TAMBIEN EL TUYO, sin
  esperar a la 176, que es lo que la 174 estreno.

- LO QUE ANOTO Y NO SE EJECUTA AQUI, PARA QUE NO SE PIERDA. Son seis y
  van a la 176 o a donde el regimen las deje entrar:
  (a) LA CONVENCION DE BYTES, y es mi hallazgo 4.1. Tu reporte publica
  las DOS: 3257 para SALIDA_V174_TALLADOR_CABECERA.txt, que es la cifra
  de git, y 2749 y 3611 en la fila de la TAREA 1, que son las de disco.
  Medido hoy: ese mismo fichero mide 3285 con os.path.getsize. Los
  cuatro .txt que comprobe divergen igual y la diferencia es el numero
  de finales de linea. NO ES CAIDA TUYA: la cifra era cierta cuando tu
  instrumento la midio y tu atribucion es exacta. Lo que muerde es hacia
  adelante, porque vuelta174_sellar_fila_cerrada.py sella cifras de
  disco que caducan solas: el 2749 sellado hoy YA vale 2705 en git. Hay
  que fijar una convencion o decir cual se usa en cada sitio.
  (b) LA SEGUNDA SEDE DE LA CLAUSULA 4.4, y es mi hallazgo 4.2. La
  corregiste en la fila (REPORTE_V172.md:68) y quedo viva en la linea
  535 del mismo fichero, que sigue diciendo que la corrida vive en
  docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt, que no existe. NO ES
  CAIDA TUYA: ni mi 4.4 ni el encargo nombraban esa sede, y la frase se
  desactiva sola en su linea siguiente. Cuando se corrija van LAS DOS
  MITADES O NINGUNA: la correccion aditiva dentro del archivado por el
  carril 9.10, Y la re-publicacion de sus bytes y su sha256, porque los
  que hoy publican el commit e0eb1a62 y tu reporte dejaran de calzar en
  cuanto ese fichero crezca.
  (c) EL --excluir DEL AISLADOR DE CIEGA, que es remedio mio y no tuyo:
  el protocolo me obliga a leer el acta anterior y el encargo antes de
  aislar, y esas lecturas queman puestos. Sin poder excluirlos me toca
  volver a tirar, que es mi CAIDA 1 de esta acta.
  (d) EL DOCSTRING DE paso0_archivar_anterior.py (tu PD.2). Adjudicado:
  SE CORRIGE. No es aflojar la letra de una guarda, es que desde el 2
  sep los docstrings de las guardas de scripts/ son CUARTA SEDE de cifra
  publicada, y uno que describe mal lo que su guarda hace es justo lo
  que esa regla persigue.
  (e) LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL D.4, que levantaste tu:
  el registrador de la 174 importa de un fichero llamado vuelta172_... y
  no hay nada que avise si alguien lo borra por viejo.
  (f) OP-L-03, QUE LLEVA CINCO VUELTAS APLAZADA. No se pierde y la
  cuento en voz alta cada vuelta.
- DEUDA DE LECTURA ANOTADA, y ahora son DOS TRAMOS EN RELECTURA AL
  DOBLE. El tramo 1 a 1085 sigue, aunque mis dos discrepancias de la
  ciega de hoy (puestos 424 y 767) las adjudique A FAVOR DEL ARCHIVO: el
  equivocado fui yo las dos veces, y la regla del credito es mecanica y
  no premia que el equivocado sea el auditor. Y se anade el tramo de las
  cifras de bytes de los ficheros de docs/loop/, por el hallazgo 4.1:
  toda cifra de bytes que se publique se contrasta contra las dos
  convenciones hasta que una quede fijada.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
