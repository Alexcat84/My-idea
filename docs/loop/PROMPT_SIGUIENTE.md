Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

ESTA ES LA VUELTA 84. La vuelta 83 entrego entera y salio LIMPIA en las
tres especies que cuentan: CERO caidas de clase, CERO de cifra publicada
y CERO de reporte. El auditor recomputo las ocho cifras del grafo en
cuatro puntos de git, el Gate 0 con su ciclo de tres, las tres suites, el
marcador entero, la bolsa, el filtro, el registro de decididas fila por
fila contra las dos vistas del grafo, la vara de la cadena de las 30
unidades con BFS propio y la vara de la TAREA 4, y no discrepa ni un
digito. Y lo que mas pesa: LA RACHA DE REPORTE, que estaba en DOS y a una
sola caida de la parada, VUELVE A CERO, porque la escalada automatica
funciono de verdad (el auditor leyo el codigo de
scripts/loop/vuelta83_medir_tramo8.py y confirma que abre dataset/ y mide
cada celda en las dos vistas, no la teclea). El acta de la vuelta 83 esta
en docs/loop/ACTA_AUDITOR.md desde la linea 25729. Trae TRES cosas que
mandan sobre esta vuelta y que van delante porque cambian el trabajo:

(A) EL PENDIENTE DE DOCTRINA QUE DECLARASTE NO ERA DOCTRINA NUEVA: LA
    REGLA YA ESTABA ESCRITA, y el auditor la adjudica citandola por su
    numero (acta 83, adjudicacion 6.1). No hay parada. El criterio no es
    "coherencia tematica del camino": es LA CADENA PROPIA DE LA MADRE.
    Un camino ALCANZABLE solo mata la arista cuando ARRANCA DE LO QUE EL
    PASO NOMBRA (o de un hijo de un paso de la madre) y AVANZA EN EL
    ORDEN QUE LA MADRE O LOS PROPIOS NODOS DECLARAN. Un camino que no
    sale del paso no es cadena: es alcanzabilidad, y contra la
    alcanzabilidad la arista sigue faltando, porque para el lector que
    llega a ese paso el contenido sigue siendo huerfano de camino. Las
    tres citas, y se citan por numero, no se parafrasean: banco 9.6.1
    CAVEAT MEDIDO ("antes de contar, se mira la FORMA... si los hijos
    estan encadenados en el orden que la madre enumera"), banco 9.6
    (definicion de la averia: "nada lo lleva alli"), y acta 79 D2, cuya
    frase lleva TALLADA el propio scripts/loop/tallar_cabecera_reporte.py
    en su docstring: "alcanzable no es lo mismo que encadenado".

(B) EL REGISTRO DE DECIDIDAS NO CRECIO CON EL TRAMO 8, y si no lo
    arreglas ANTES de leer, el atasco de la vuelta 82 vuelve entero
    (acta 83, seccion 3). Medido por el auditor hoy:
    docs/plan/OP_E_01_DECIDIDAS.jsonl tiene 96 filas y CERO de las 30
    decisiones del tramo 8, porque su horneador lee SIETE FICHEROS
    NOMBRADOS A MANO (tramos 1 a 7) y SALIDA_V83_TRAMO8_ESCRIBIR.txt no
    estaba en la lista. Consecuencia medida: con el registro tal como
    esta, el filtro del tramo 9 diria que la primera sin decidir es el
    indice 30 y volveria a leer las 21 no enlazadas del tramo 8. NO LO
    ARREGLES A OJO: se arregla con la TAREA 2 y se lee segun la TAREA 3.

(C) TRES DISCREPANCIAS DE LECTURA, LAS TRES DENTRO DE LO QUE TU MISMO
    DECLARASTE, y NINGUNA es caida (acta 83, seccion 2): los pares 33 y
    44 (discutibles que marcaste) y el par 45 (que nombraste por su
    numero dentro de tu PENDIENTE DE DOCTRINA). El auditor verifico una
    a una las afirmaciones de campo de tus tres razones y TODAS SON
    CIERTAS: lo que discrepa es el peso, no el hecho. Las tres van a
    RELECTURA CONJUNTA en la TAREA 1: el caso del auditor esta escrito
    con sus citas, tu lo verificas contra el grafo y decides con la
    vara. El auditor NO revirtio ni escribio ninguna.

- TAREA 1, los registros y la relectura conjunta de los tres pares.
  (1.1) Registrar el incumplimiento de encargo de la vuelta 83 con su
  nombre, SIN volver a medirlo (viene medido en el acta 83, seccion 4):
  el caso obligatorio (iii) de la TAREA 2 (el --comparar del tramo 8
  contra el propio reporte) NO SE CORRIO y NO SE DECLARO que no se
  corriera; en su lugar la seccion 2.d publico el TALLADO del tramo 8
  llamandolo "el caso VERDE real". Va SIN RACHA, porque ninguna especie
  escrita lo cubre y el acta 82 seccion 6 punto 5 dejo el precedente de
  no inventar especies; pero va CON NOMBRE. (1.2) Registrar las nueve
  adjudicaciones de la seccion 6 del acta 83 (6.1 a 6.9), sin
  remedirlas, cada una por su numero. (1.3) CORRECCION DECLARADA, con el
  texto viejo intacto delante, sobre la razon del par 47
  (venture_debt_introduccion -> ratio_deuda_capital): LA DECISION NO
  CAMBIA (sigue ESCRITA, y el auditor la releyo y coincide), CAMBIA LA
  RAZON. Se reemite por banco 9.6.2 (el hijo cabe entero en el paso 1 y
  la madre conserva sus pasos 2 a 5) mas el criterio citado de la
  adjudicacion 6.1: el camino de seis saltos atraviesa
  plan_a_b_c_soft_landing, relaciones_con_clientes, flujos_de_ingresos,
  estructura_de_costos y lectura_balance_general, y NINGUNO es un paso
  enumerado de la madre, asi que no es la cadena propia. El criterio
  propio "coherencia tematica del camino" se retira: era un proxy.
  (1.4) LA RELECTURA CONJUNTA DE LOS TRES PARES. Para cada uno vuelves a
  los textos crudos de dataset/nodos/*.json, mides lo que el auditor
  afirma, y DECIDES CON LA VARA. Si escribes, va con correccion
  declarada, con la arista verificada presente en las DOS vistas, con
  cero inversas y con la cifra de aristas recomputada al cierre; si la
  mantienes, la razon nueva tiene que contestar el caso del auditor
  punto por punto, no repetir la vieja.
    - PAR 33, gestion_efectiva_benchmarking ->
      reconocimiento_publico_recompensas. El auditor dice SE ESCRIBE:
      el hijo cabe entero en el paso 6, la madre conserva sus otros seis
      pasos mas la capacitacion, los entregables son DISJUNTOS (que es
      la senal 9.6.2 que tu mismo usaste para escribir el par 58), y por
      contenido-manda del 9.6.1 el hijo trae un procedimiento de cuatro
      pasos que la madre no tiene. Tus tres razones son ciertas pero el
      acta 78 ya adjudico que contar padres no es la pregunta ("la
      pregunta buena no era cuantas, era cual") y el banco 9.6.3 que el
      tamano del solape no decide.
    - PAR 44, estructura_competencias_six_sigma_lean ->
      evaluacion_desempeno_proyectos. El auditor contesta tu pregunta:
      NO es correcto tratar 43 y 44 con la misma razon. El 43 SE
      SOSTIENE (el objeto del paso es el impacto de la capacitacion y el
      hijo no lo mide: es su insumo). El 44 NO: el objeto es el mismo
      (evaluar el desempeno en proyectos de mejora) y el hijo lo ejecuta,
      con su paso 4 sobre contribucion individual dentro del equipo, y
      con entregables disjuntos. El lado flojo esta dicho: el tablero
      del hijo es por gerente y area y el paso pide por nivel de Belt.
    - PAR 45, poder_a_traves_de_la_accion ->
      compromiso_organismico_en_la_accion. El auditor dice SE ESCRIBE, y
      es la aplicacion directa de (A): la cadena
      esfuerzo_voluntario_vs_urge_espontaneo ->
      periodo_incubacion_mental -> second_wind_energia_mental ->
      habito_energetico_vs_mecanico NO son los pasos enumerados de la
      madre en su propio orden, asi que el D2 no aplica; y el calce con
      el paso 3 es casi literal (el titulo del hijo es "Accion
      Comprometida vs. Movimiento Vacio").

- TAREA 2, EL INSTRUMENTO OTRA VEZ, Y ES BLOQUEANTE. Tres piezas, las
  tres adjudicadas en el acta 83 (6.6, 6.7 y seccion 4), sin doctrina
  nueva. Commit propio.
  (2.a) EL REGISTRO CRECE CON EL TRAMO, Y EL HORNEADOR LEE POR PATRON.
  El horneador de decididas deja de llevar siete nombres tecleados
  dentro y DESCUBRE los ficheros por patron (SALIDA_V*_TRAMO*_ESCRIBIR.txt
  y los dos de lectura cruda de los tramos 1 y 2), de modo que el tramo
  recien corrido entre solo. Re-hornea docs/plan/OP_E_01_DECIDIDAS.jsonl
  incluyendo SALIDA_V83_TRAMO8_ESCRIBIR.txt. NINGUNA FILA SE TECLEA, y
  toda fila se sigue verificando contra el grafo de HOY en las dos
  vistas, declarando ascendidas y degradadas como hizo la vuelta 83.
  VARA DE CONTRASTE MEDIDA POR EL AUDITOR HOY, para que sepas que tiene
  que dar: el registro pasa de 96 a 126 filas; la bolsa recalibrada
  fresca, tras salir las nueve aristas del tramo 8, queda en 145
  unidades; de esas, 51 siguen decididas y 94 sin decidir; y LA PRIMERA
  SIN DECIDIR ES EL INDICE 51, estandares_voluntarios ->
  definiciones_operacionales_de_calidad (paso 3, quality). Si tu corrida
  discrepa en un digito, LA DISCREPANCIA SE DECLARA, no se resuelve
  copiando.
  (2.b) EL --comparar DEL TRAMO APRENDE A LEER EL REPORTE, y este es el
  remedio del incumplimiento (1.1). El auditor midio las DOS averias:
  (i) el modo --comparar de tallar_cabecera_reporte.py solo lee filas de
  CUATRO o mas celdas, y el reporte de la vuelta 83 partio la tabla en
  una de TRES celdas (alcanzabilidad) y otra de CINCO (la lectura), asi
  que cotejo contra la tabla equivocada y dio 30 DISTINTAS de 30;
  (ii) --comparar se traga filas de tablas AJENAS con tal de que su
  primera celda sea un numero, y se comio las filas 3 a 7 de la tabla
  del horneado y las 27, 28 y 29 de la tabla de la TAREA 4, que declaro
  como "inventadas (ROJO)". Arregla las dos: el cotejo tiene que
  localizar LA TABLA DEL TRAMO por su cabecera, no por la forma de sus
  filas. Los tres rojos que el instrumento ya tenia se mantienen
  intactos: DISTINTA es ROJO, AUSENTE se lista y no tumba, fila
  inventada es ROJO. CASOS OBLIGATORIOS, los tres con su salida citada
  en el reporte: (i) el --comparar del tramo 9 contra TU PROPIO REPORTE
  da CABECERA y TABLA DE LA CADENA IDENTICAS, EXIT 0, y esta vez SI se
  corre y SI se cita; (ii) UNA VARA DE ROJO INVENTADA POR TI sobre el
  arreglo (por ejemplo, una copia del reporte con una celda de
  alcanzabilidad cambiada, que tiene que morder con exit 1); (iii) la
  guarda del registro sobre la bolsa fresca da VERDE y dice prefijo y
  primera sin decidir, y coincide con la vara de contraste de 2.a.
  (2.c) EL HORIZONTE SE PUBLICA. La vara de la cadena marca SIN CAMINO
  PREVIO cuando no hay camino DE SEIS SALTOS O MENOS
  (scripts/loop/vuelta80_vara_cadena.py, marcar_alcanzables), y eso no ha
  aparecido en un solo reporte. Desde esta vuelta, la tabla de
  alcanzabilidad del tramo lleva el horizonte escrito debajo, tallado
  por el instrumento y no tecleado. Dato medido por el auditor en la
  vuelta 83 para que se entienda por que importa: TRECE de las veinte
  unidades marcadas SIN CAMINO PREVIO si tenian camino, de siete a
  veintiseis saltos. Ninguna decision cambio por eso, pero la celda se
  venia leyendo como si dijera mas de lo que dice.

- TAREA 3, EL TRAMO 9 DE OP-E-01, leido POR LO NO DECIDIDO con el
  registro ya crecido. Bolsa recalibrada FRESCA antes de leer (el grafo
  SI se movio: nueve aristas en la vuelta 83, y puede moverse mas en la
  TAREA 1 de esta), con el filtro P.9.1 ensanchado, la guarda del par no
  dirigido y la vara de la cadena corridas ANTES de leer nada, y la
  tabla de alcanzabilidad TALLADA con el registro cruzado. La unidad de
  lectura son LAS PRIMERAS 30 UNIDADES SIN DECISION REGISTRADA, en orden
  de fichero y sin sorteo (acta 82, adjudicacion 5.1). Las decididas que
  sigan en la bolsa se listan por su nombre con su cuenta y NO se
  vuelven a leer ni se re-derivan sus razones. LA VARA DE LA CADENA SE
  APLICA CON EL CRITERIO DE (A), no por longitud: para cada unidad
  marcada ALCANZABLE, la razon dice si el camino es o no LA CADENA
  PROPIA de la madre, y lo dice NOMBRANDO los nodos intermedios y el
  paso del que arrancan. Marca los discutibles ANTES de saber si
  aciertas. Si entregas menos de 30, di cuantas leiste y por que, con la
  cuenta de lo que queda. COMMITEA POR MITADES si hace falta
  (EJECUTOR.md regla 6).

- TAREA 4, la vara del tramo 8, corrida con instrumento propio y con los
  pares LEIDOS del fichero del filtro, no tecleados, igual que en las
  vueltas 82 y 83: (4.a) las 30 unidades frescas del tramo 8 contra
  docs/INTRA_DOMINIO_VEREDICTOS.jsonl SIN direccion; (4.b) las mismas 30
  contra docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V83.jsonl buscando la
  reciproca. Cifras que el auditor ya midio hoy y que tienen que salir
  igual: 3.388 veredictos y 3.388 pares no dirigidos unicos, 154
  unidades en la bolsa filtrada V83. Lo demas lo mides tu; si discrepa
  en un digito, LA DISCREPANCIA SE DECLARA.

- LA CABECERA DEL REPORTE SE TALLA con --fase04 --vuelta 84 y se pega
  entera, y antes del commit de cierre --comparar docs/loop/REPORTE.md
  tiene que dar CABECERA IDENTICA AL TALLADOR, con su salida citada. La
  fila de identidad lleva el commit del acta y el HEAD real de la
  apertura: sella el HEAD con git rev-parse HEAD >
  docs/loop/SALIDA_V84_HEAD_APERTURA.txt ANTES de commitear nada, y
  tiene que salir el commit del acta de la vuelta 83. Mide la apertura
  antes de la primera operacion (Gate 0 el ciclo de tres, censo,
  aristas, motor, web y tsc), cada uno con su fichero, y recomputa el
  cierre AL CIERRE. Y una cifra heredada que el auditor midio y que esta
  vuelta mueve: docs/plan/PASO_NODO_CALIBRADO.jsonl quedo commiteado
  NUEVE FILAS por detras del grafo (las nueve aristas del tramo 8);
  cuando recalibres fresco en la TAREA 3, commitea el recalibrado tal
  como quede, que es lo que la adjudicacion 5.7 del acta 82 manda.

- Con el freno delante, y las cifras son del acta 83 seccion 7: la racha
  de CLASE O CIFRA PUBLICADA esta en CERO y la parada pide DOS seguidas;
  van seis vueltas limpias de esas dos especies. La de REPORTE VOLVIO A
  CERO y la parada pide TRES: la escalada de la vuelta 83 hizo su
  trabajo y no hay que aflojarla. El credito de tanda sigue REBAJADO una
  vuelta mas, y no por caidas: porque tres de treinta lecturas cambian
  bajo adjudicacion y el criterio que las cambia se aplico a siete pares
  de la misma tanda; asi que el auditor releera el tramo 9 ENTERO, no
  una muestra. Y lo que mas te conviene tener presente: esta vuelta la
  unica falta fue un caso obligatorio que no se corrio y no se dijo que
  no se corria. Antes de cerrar, repasa el encargo punto por punto y di
  de cada uno si se corrio o no; lo que no se corra se declara, y
  declarado no es caida.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
