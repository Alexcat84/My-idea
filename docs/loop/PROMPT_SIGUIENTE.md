Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. El acta de la vuelta 64 esta al final de
docs/loop/ACTA_AUDITOR.md: verificacion completa al digito (cabecera 14
filas identicas, marcador, recomputo, cola, colisiones, duplicadas,
estado, barrido, Gate 0 con ciclo de tres, motor 25/25, web 1030, tsc
cero, promesas 2 de 2, censo de plantillas cero tallados sobre 22,
cuenta independiente con 35 comprobaciones y cero fallos, cableado por
las dos varas, tramo de OP-U-02 47 de 47 contra mi recomputo con 6/39
fuera, casos positivos con las nueve, la guarda de consumido y las seis
mordiendo), ciega 1 de 1 en el fondo con el reparto pieza a pieza, los
NUEVE discutibles A FAVOR (el D5 registrado como caida de procedimiento
autodeclarada), UNA caida de reporte del ejecutor (la 7.1, verificada
exacta; racha de reporte EN UNO), y las siete preguntas contestadas sin
doctrina nueva.

TRES ADJUDICACIONES DEL ACTA 64 QUE MANDAN EN ESTA VUELTA:

1. LAS DOS COLISIONES DE CLASE SON DE LA MESA OP-M-03 Y LAS RESUELVE LA
   MESA EN SU TURNO (acta 64, pregunta 3, por el carril del acta 52
   pregunta 4 registrado en 03_FUSIONES desde la linea 1377): quedan
   VIGENTES, publicadas en rojo y NO SE TOCAN. LA LINEA BASE DEL CENSO
   DE COLISIONES ES AHORA 2, DECLARADA: toda operacion corre el censo
   con esperadas MEDIDAS sobre esa base (simulacion sobre el arbol de
   antes, ANTES de fundir, que es la leccion del D5), y un delta no
   predicho por la operacion es PARADA de guarda.
2. NO SE APILA MAS DE UN INCISO SOBRE EL MISMO PASO por defecto (acta
   64, pregunta 5); si un caso leyera limpio con dos, se ejecuta
   marcado discutible.
3. LA AGUJA DEL COMPROBADOR DE PROMESAS SE ENSANCHA (acta 64, pregunta
   6), por el carril de correccion de instrumento estable, y es la
   TAREA 1.b de abajo.

- TAREA 1: registros y el ensanche del comprobador.
  a) El registro de las adjudicaciones del acta 64 donde el patron de
  la campana las pone (final de docs/plan/03_FUSIONES.md, adosado, sin
  reescribir lo de arriba, con la guarda de citas cotejadas antes de
  escribir y la guarda de idempotencia): los nueve A FAVOR con su vara
  citada, el carril de las colisiones con la mesa OP-M-03 como duena y
  la linea base del censo en 2, la regla de no apilar incisos, la
  caida de reporte con su nombre y la racha en uno, y las respuestas de
  las preguntas 4 y 7 (registradas, no encargadas).
  b) EL ENSANCHE DE LA AGUJA de
  scripts/loop/comprobar_promesas_de_marcado.py por correccion
  declarada (docstring con nota fechada y el texto viejo citado): se
  anade la forma plural (VAN MARCADAS COMO DISCUTIBLES) a la aguja
  singular existente, sin quitar nada. Con caso positivo en DOS
  mitades, corrido y committeado: NO REGRESION (las corridas de los
  planes de las vueltas 63 y 64 se re-corren con el instrumento
  ensanchado y siguen dando sus promesas CUMPLIDAS, 2 de 2 y 2 de 2) y
  VISIBILIDAD (una nota en plural que la aguja vieja no ve pasa a
  verse, probado con un plan de mentira que se borra tras la prueba).
  Si al ensanchar aflora en un plan sellado una promesa INCUMPLIDA que
  hoy es invisible, PARAS y lo traes con la medicion: eso es hallazgo,
  no regresion.
- TAREA 2: EL LOTE A DEL TRAMO UNICO DE OP-U-02. El tramo esta FIJADO
  en docs/loop/TRAMO_UNICO_OPU02_V64.jsonl (47 actos, 201 nodos, en su
  orden_universo; tramo unico y final por agotamiento). El lote es
  PREFIJO de ese orden, sin saltos: declaras al abrirlo cuantos actos
  entran (los que cierren ENTEROS en la vuelta) y entregas lo
  declarado. Cada acto con las reglas ya escritas: P.5 con el acto
  leido entero y su pregunta de UNA familia o DOS contestada con el
  texto estable, el carril del DECLARADO Y NO FUNDIDO con motivo
  sellado, P.8 en orden, las varas por forma con su letra (una sola
  vara BASTA, acta 53 pregunta 4; todas de acuerdo funde a su lado;
  contenido empatado decide el cableado solo; CHOCAN decide la pieza
  declarada; EMPATE SIN VARA por su carril; el rotulo solo y la
  cantidad NUNCA deciden), el contrato CAMPO PROPIO v1 (perdidas en
  campo aunque vayan vacias), generar_plan_del_lote.py con --operacion
  OP-U-02, P.16 con limpieza en el mismo commit y diff de duplicadas
  por instrumento (CERO fabricadas fuera de las declaradas, o parada),
  censo de colisiones con esperadas MEDIDAS sobre la linea base 2 y
  CALZA, reanclar entre la fusion y run_phase1, Gate 0 con su ciclo de
  tres y las tres suites, caso positivo sobre un sujeto que la vuelta
  NO toque (caso_positivo_de_fusion_de_mesa.py exige --id-op y su
  guarda de consumido muerde; el de tramos por su via), promesas de
  marcado cotejadas por maquina antes de sellar el reporte, y el
  registro en 03_FUSIONES.md por el patron de la campana bajo cabecera
  de tramo de OP-U-02. NO fundas ningun acto con dueno (los 6 de fuera
  siguen fuera), no tocas la mesa OP-M-03 ni sus colisiones, y las
  cinco fichas OP-M-02 consumidas no se ejecutan (acta 63, pregunta 1:
  lo consumado no se ejecuta ni se rehace).

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
