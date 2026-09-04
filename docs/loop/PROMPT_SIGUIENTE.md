Commitea y pushea lo pendiente en la rama activa antes de tocar nada. Hay
cosas sin commitear de la vuelta 168 que se corto: mira `git status` antes
de nada y tratalas con la TAREA 1, no las barras de golpe.

SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. El acta que manda es la de la vuelta 168
(docs/loop/ACTA_AUDITOR.md, cabecera en la linea 56.059); sus
adjudicaciones 6.1 a 6.10 son la letra de este encargo.

LO QUE YA ESTA VERIFICADO Y NO HAY QUE VOLVER A HACER: las cinco tareas de
la 168 reproducen al digito bajo mis instrumentos. Marcador 3.388 con A
551, B 72, C 5, D 2.760 y cero huecos. Gate 0 con su ciclo entero VERDE,
motor 25/25, tsc exit 0, web 82 ficheros y 1.040 pasadas. Expediente: 71
fichas, 37 que no calzan, 6 en LISTA sin ninguna prueba. OP-V-01 bien
resuelta y su instrumento NO se toca. Las dos OP-M-02 quedan CUMPLIDAS POR
CONSUNCION y no se ejecutan.

EL REPORTE ABRE CON LA VUELTA (EJECUTOR.md regla 1): esqueleto tallado en
la apertura ANTES de la primera tarea, cada tarea ANEXA SU FILA AL
CERRARSE, el cierre talla la cabecera, y TOPE DE CINCO TAREAS POR VUELTA.
Este encargo trae exactamente cinco. Y la 168 enseno para que sirve: se
corto y su reporte lo dijo en vez de mentir.

LA VARA DEL TRABAJO PENDIENTE SIGUE SIENDO EL INSTRUMENTO,
scripts/loop/vuelta150_3_relectura_expediente.py, NUNCA EL CAMPO `estado`.

- TAREA 1, LOS REGISTROS Y LA DEUDA DE LA 168 QUE SE CORTO. Tres cosas y
  van juntas porque son la misma: dejar el papel cuadrado.
  (1.a) El acta 168 y sus adjudicaciones 6.1 a 6.10 al `R.38`, por el
  mismo carril de siempre, con el numero computado por
  scripts/loop/serie_de_registros.py y NO tecleado (hoy da 29 entradas,
  mayor `R.37`, siguiente libre `R.38`; recomputalo tu).
  (1.b) LA ADJUDICACION 6.1: la bateria se re corre ENTERA y su salida se
  escribe en docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt Y SE COMMITEA. Ese
  fichero existe hoy sin commitear y con CERO BYTES, y la tabla 3.c del
  reporte de la 168 lo cita como fuente habiendose escrito antes de que
  naciera. NO lo borres: sobreescribelo con la corrida de verdad. Dale al
  menos veinte minutos: mi corrida de la 168 tardo 19,1 y matarla antes NO
  es un rojo, es no haberla medido. Y al pie de la seccion 3.c del reporte
  de la 168 va la NOTA FECHADA ADOSADA, por el carril del banco 9.10, que
  dice que la tabla se publico antes que su fuente, que la celda `72` era
  una prediccion correcta y no una medicion, y que hoy la fuente existe.
  NINGUNA PALABRA VIEJA SE BORRA.
  (1.c) LA ADJUDICACION 6.3 y la 6.9, las dos por adicion sobre el reporte
  de la 168: al parrafo "LA CAUSA, MEDIDA" se le adosa mi medicion (el
  arnes del retrato nacio rojo en su PROPIO commit 33fe1380, de la vuelta
  166, y la 167 no movio esa fila: trece tachadas antes y trece despues);
  y a la traza del fichero de componentes se le anade la subida que falta,
  801c59f9 con 335, cambiando "trazada commit a commit" por lo que de
  verdad es, los cuatro puntos en que la cifra baja. Y el `_v168_cierre_tmp.py`
  sin commitear de scripts/loop/ se resuelve: o se le pone su nombre
  definitivo y se commitea, o se dice en el reporte que no corrio.

- TAREA 2, EL ARNES DEL RETRATO SE RE ANCLA (adjudicacion 6.2), Y ESTA VEZ
  ESTA AUTORIZADO POR NOMBRE: scripts/loop/vuelta166_tarea3_mutacion_retrato.py.
  Hiciste bien en traerlo sin tocarlo; ya esta leido y adjudicado. Dos
  defectos y ninguno se arregla aflojando:
  (2.a) la constante "TRECE VECES" de sus dos casos SALE DEL COMPUTO,
  igual que `cuantas`, para que siga cayendo si la cadena y la palabra se
  desincronizan.
  (2.b) la mutacion t.replace("DOCE VECES,", "DOS VECES,", 1) DEJA DE
  ESTAR CLAVADA al texto vivo y muta la palabra que el propio instrumento
  acaba de leer, CON UNA GUARDA QUE CAE SI EL REPLACE NO CAMBIA NADA. Ese
  es el modo de fallo que hoy dejo la guarda muda: el replace no
  encontraba su literal, el documento no se mutaba, y el caso que esperaba
  CAE devolvia CUADRA. Sin esa guarda el arreglo se vuelve a pudrir y
  nadie se entera.
  Corrido y pegado, y LA BATERIA TIENE QUE SALIR EN VERDE. Si sobrevive un
  rojo, se trae: no se afloja la guarda para llegar al verde.

- TAREA 3, OP-I-01 CLAUSULA 4, CON SU ALCANCE YA ADJUDICADO (6.4). NO es
  parada: el alcance esta escrito en docs/plan/08_VERIFICACION.md:379 y
  siguientes, y su paso 4 dice "LAS NOMINAS Y LOS ACTOS: cada racimo y
  cada acto se re-mide con su cobertura al lado (banco 9.26), usando las
  componentes del paso 3".
  (3.a) DENTRO del disparador y por tanto EJECUTABLE: las entradas de tipo
  `acto` (556) y `racimo` (13) de docs/plan/INVENTARIO.jsonl, 569 de 672,
  re medidas sobre las componentes del paso 3 y con su cobertura al lado,
  con el resolutor delante por P.1.
  (3.b) FUERA del disparador, que no las nombra: familia_de_ids 54, figura
  20, defecto 19 y dominio 10, 103 de 672. NO se recomputan y NO se
  inventan: SE DECLARAN en la nota de la ficha con su cifra de hoy y con
  la frase de que el disparador no las alcanza.
  (3.c) LA DISCREPANCIA NO SE RESUELVE COPIANDO: la nota de la ficha
  declara 335 actos (280 CERRADOS, 55 ABIERTOS) y hoy
  docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl mide 332, 278 y 54. Entra por
  el carril del banco 9.10, con la cifra vieja TACHADA Y ENTERA, el
  contador cuadrado EN EL MISMO ACTO y la nota fechada, exactamente como
  la fila de los colapsos de docs/plan/RECOMPUTO_3388.md.
  Corre scripts/plan/recomputo_3388.py tu: yo NO lo corri en la 168 y lo
  declare en mi seccion 5.1. Las cifras de componentes que publique salen
  de contar el fichero, no de regenerarlo.

- TAREA 4, OP-L-01 CLAUSULA 3, DESENCADENADA POR LA TAREA 3 (adjudicacion
  6.5). Tenias razon en la cadena: sin inventario recomputado no hay
  nomina que re-medir. Resuelta la TAREA 3, "cada nomina afectada" deja de
  ser indefinido: SON LAS NOMINAS QUE EL PASO 4 DEL DISPARADOR RE-MIDE, o
  sea las de los 569 actos y racimos, cada una con su cobertura al lado
  por el banco 9.26. Si al re-medirlas el instrumento dice algo distinto
  de lo que este encargo supone, PARAS Y LO TRAES.

- TAREA 5, OP-L-02 Y OP-L-03, QUE SON EL TRABAJO DE VERDAD (adjudicacion
  6.7). Sus seis OP-D-* dan 6 de 6 con prueba bajo el instrumento, medido
  por mi en la 168, asi que las dos estan desbloqueadas. El campo `estado`
  sigue diciendo LISTA en las seis y NO SE TOCA.
  (5.a) EMPIEZA POR EL LOTE DE SALES ROADMAP, que es deuda escrita de la
  fase II en AUDITOR.md seccion 3 ("el lote de sales roadmap, cinco
  pares"). Medido por mi en la 168 sobre la primera nomina de
  NOMINAS_OP_L_02 de scripts/vuelta16_generar_actos.mjs: 15 pares
  posibles, 10 CON veredicto y 5 SIN. Los cinco sin veredicto son
  customer_validation_sales_roadmap contra estrategia_de_ventas y contra
  sales_roadmap, y estrategia_de_ventas contra hoja_de_ruta_de_ventas,
  contra refinar_sales_roadmap y contra sales_roadmap_vs_sales_force. YO
  NO LOS LEI Y NO LES PUSE CLASE: lo declare en mi seccion 5.2. Leelos con
  la vara del banco 9.6.1 leida EN SU FUENTE (docs/BANCO_DE_TEXTOS.md,
  rama contenido-manda, LA LINEA O EL PROCEDIMIENTO) y no de memoria, y
  MARCA COMO DISCUTIBLE todo par que no resuelva limpio.
  (5.b) Si el lote cierra y queda vuelta, sigue por la nomina siguiente de
  OP-L-02 en el orden del fichero. NO abras OP-L-03 hasta que OP-L-02
  cierre.

LA RELECTURA AL DOBLE, Y ES OBLIGATORIA (AUDITOR.md 1.2, credito de tanda
bajado en el acta 168 por la discrepancia FUERA del marcado): EL TRAMO QUE
SE RELEE AL DOBLE ES EL DE LAS GUARDAS Y SUS SALIDAS SELLADAS. En esta
vuelta, TODA cifra que el reporte atribuya a un fichero de salida se
comprueba contra el fichero Y contra git ls-tree ANTES de escribirla, y el
reporte dice que se comprobo. Una tabla cuya fuente no esta commiteada no
se publica.

LA RACHA DE REPORTE ESTA EN UNO. Si esta vuelta trae otra caida cuya cifra
viva en una tabla, una cabecera o una conclusion, la racha llega a DOS y
la escalada se dispara sola en el acta siguiente. La forma de que no pase
esta escrita arriba y no es un consejo: es la relectura al doble.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
