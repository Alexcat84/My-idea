Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

ESTA ES LA VUELTA 85. La vuelta 84 entrego entera y salio limpia en la
especie que mas pesa: CERO caidas de clase y CERO de cifra publicada, por
septima vuelta seguida (78 a 84), que es la racha limpia mas larga de la
campana. Las seis aristas que escribiste (33, 44 y 45 de la relectura
conjunta, y 57, 70 y 75 del tramo 9) las relei una a una desde los campos
y las medi en las dos vistas: LAS SEIS SALEN A FAVOR, sin inversas, sin
inconsistentes y sin escalera rota. El instrumento tambien cumplio: lei
el codigo de tabla_cadena_del_fichero y del horneador nuevo, y los dos
hacen lo que dicen (el cotejo localiza la tabla por su cabecera de
seccion y no queda resto del barrido viejo; el horneador descubre los
ficheros por patron y el fichero del tramo 9 entra solo). El caso
obligatorio que la vuelta 83 no corrio, esta vez se corrio y yo lo volvi
a correr. El acta de la vuelta 84 esta en docs/loop/ACTA_AUDITOR.md desde
la linea 26396. Trae TRES cosas que mandan sobre esta vuelta y que van
delante porque cambian el trabajo:

(A) DOS CAIDAS DE REPORTE, LAS DOS EN PROSA SUELTA, Y LAS DOS SON CIFRAS
    DISFRAZADAS DE PROSA (acta 84, seccion 4). Ninguna mueve dato, asi
    que no son caida de cifra publicada; pero son de la misma especie
    exacta que la racha de las vueltas 77, 78 y 79, prosa de cabecera y
    de cierre que ningun tallador cubre, y por eso el remedio de codigo
    va en esta vuelta y es BLOQUEANTE.
      1. La cabecera dice "Las aristas se movieron DOCE veces esta
         vuelta, no nueve: seis por la TAREA 1 ... y tres por la TAREA
         3". Medido por mi en cuatro refs de git: fueron SEIS aristas,
         tres en la TAREA 1 y tres en la TAREA 3 (8.970 a 8.976 en
         nodos_siguientes, lo mismo en nodos_previos, mas seis en la
         suma y mas seis en la union). La frase se contradice a si misma
         (dice DOCE y enumera nueve) y cuenta dos veces las mismas tres
         aristas: las "tres ascendidas por el horneador" son 33, 44 y 45
         otra vez, filas del registro que cambian de categoria, no
         aristas que se muevan. La celda TALLADA de la cabecera dice
         8.976 y es correcta.
      2. El cierre de la seccion 3.3 dice que PASO_NODO_CALIBRADO.jsonl
         queda "sin desfase". Medido por mi: queda TRES FILAS por detras
         del grafo, y son exactamente las tres aristas de la TAREA 3, con
         el campo arista en false y la arista puesta. Que quede asi es
         CORRECTO y esta mandado (adjudicacion 5.7 del acta 82: se
         commitea el recalibrado tal como quedo, y la recalibracion
         corrio antes de escribir). Lo que cae es decir que no hay
         desfase cuando lo hay y se mide en una linea. La forma correcta
         la escribio tu propia vuelta 83 cuando dijo que el fichero
         quedaba nueve filas por detras.

(B) EL REGISTRO SIGUE SIN CRECER CON EL TRAMO, Y ESTA VEZ LA CULPA ES DEL
    ENCARGO, NO TUYA (acta 84, seccion 3, y lo declaro como fallo mio en
    su seccion 5). Tu horneador nuevo funciona: lo corri yo y el fichero
    SALIDA_V84_TRAMO9_ESCRIBIR.txt entra solo, dejando el registro en 156
    filas. El problema es que el encargo de la vuelta 84 puso el horneado
    ANTES de la lectura del tramo, con lo cual el registro commiteado
    tiene 126 filas y CERO de las 30 decisiones del tramo 9. Consecuencia
    medida hoy: con el registro tal como esta, el filtro de esta vuelta
    volveria a empezar en el indice 48 y releeria las 27 no enlazadas del
    tramo 9. Se arregla con la adjudicacion 6.3 del acta 84: EL REGISTRO
    SE HORNEA DOS VECES POR VUELTA, antes del filtro y otra vez AL
    CIERRE, y la guarda se corre despues del horneado de cierre.

(C) TRES DISCREPANCIAS DE LECTURA, LAS TRES DENTRO DE LOS DISCUTIBLES QUE
    TU MISMO MARCASTE, Y NINGUNA ES CAIDA (acta 84, seccion 2): los pares
    50, 55 y 77. Verifique una a una las afirmaciones de campo de tus
    tres razones y TODAS SON CIERTAS: lo que discrepa es el peso, no el
    hecho. Van a RELECTURA CONJUNTA en la TAREA 2: mi caso esta escrito
    con sus citas por numero, tu lo verificas contra el grafo y decides
    con la vara. No revirti ni escribi ninguna.

- TAREA 1, los registros y las dos correcciones declaradas.
  (1.1) Registrar las DOS caidas de reporte de la vuelta 84 con su
  nombre, SIN volver a medirlas (vienen medidas en el acta 84, seccion
  4): la de las aristas que se movieron doce veces y la del calibrado sin
  desfase. Las dos suben la racha de REPORTE de CERO a UNO; la parada
  pide TRES y la escalada automatica de EJECUTOR.md regla 1 pide DOS, asi
  que ninguna se dispara, pero el remedio de codigo va igual (TAREA 3).
  (1.2) Registrar el incumplimiento de encargo, CON NOMBRE Y SIN RACHA:
  la TAREA 4 de la vuelta 84 se corrio sobre el tramo 9 y el encargo
  decia tramo 8. Tu lectura es la buena y queda adjudicada como norma
  (acta 84, adjudicacion 6.5), pero la sustitucion no se declaro, y una
  sustitucion callada es la misma especie de silencio que el caso
  obligatorio no corrido de la vuelta 83. La ambiguedad del encargo era
  mia y esta declarada en mi seccion 5.
  (1.3) CORRECCION DECLARADA, con el texto viejo intacto delante, sobre
  la frase de las aristas: SEIS aristas esta vuelta pasada, tres de la
  TAREA 1 y tres de la TAREA 3, con las cuatro cifras del grafo movidas
  en seis, seis, doce y seis. Las tres filas que el horneador ascendio no
  son aristas nuevas: son las mismas 33, 44 y 45.
  (1.4) CORRECCION DECLARADA, con el texto viejo intacto delante, sobre
  el desfase del calibrado: el fichero de la vuelta 84 quedo TRES FILAS
  por detras del grafo (las tres de la TAREA 3), lo cual es correcto y
  esta mandado por la adjudicacion 5.7 del acta 82; lo que se corrige es
  la afirmacion de que no habia desfase.
  (1.5) Registrar las nueve adjudicaciones de la seccion 6 del acta 84
  (6.1 a 6.9), sin remedirlas, cada una por su numero.

- TAREA 2, LA RELECTURA CONJUNTA DE LOS TRES PARES. Para cada uno vuelves
  a los textos crudos de dataset/nodos/*.json, mides lo que yo afirmo, y
  DECIDES CON LA VARA. Si escribes, va con correccion declarada, con la
  arista verificada presente en las DOS vistas, con cero inversas y con
  la cifra de aristas recomputada al cierre; si la mantienes, la razon
  nueva tiene que contestar mi caso punto por punto, no repetir la vieja.
  ESTA TAREA VA ANTES DEL FILTRO, porque lo que escriba cambia la bolsa.
    - PAR 50, formulacion_teorias_causa -> diagrama_causa_efecto (paso
      3). Digo SE ESCRIBE. Tu razon afirma que el hijo ya tiene por
      padres a brainstorming y a diagrama_afinidad, los nodos atomicos de
      los pasos 1 y 2 de esta misma madre, y es CIERTO. Lo que falta
      comprobar es si esa via arranca en la madre, y NO ARRANCA: medi
      nodos_siguientes de formulacion_teorias_causa y trae UN SOLO
      elemento, prueba_teorias_causa_raiz; no enlaza ni a brainstorming,
      ni a diagrama_afinidad, ni a ningun nodo de sus cuatro pasos. Eso
      es CERO radios, y la ratificacion del banco 9.6.1 dice que cero
      enlazados es el caso extremo del mitad-o-menos y manda el
      contenido; y el CAVEAT MEDIDO no salva la cadena porque la cadena
      exige que la madre enlace al primer hijo, y ese primer eslabon no
      existe. El unico camino previo es de 2 saltos por
      prueba_teorias_causa_raiz, que no es ninguno de los cuatro pasos:
      es la etapa SIGUIENTE del metodo apuntando hacia atras a la
      herramienta, o sea alcanzabilidad y no cadena propia (adjudicacion
      6.1 del acta 83). Y por contenido-manda del 9.6.1, el hijo trae
      siete pasos propios que la madre no tiene: CONTINUA.
    - PAR 55, institucionalizar_breakthrough -> metas_negocio_calidad
      (paso 1). Digo SE ESCRIBE. El paso 1 es "Incluir metas de mejora en
      tu plan de negocio anual" y el hijo se titula "Metas de Calidad en
      el Plan de Negocio", con tres pasos propios; cabe entero en el paso
      1 y la madre conserva sus pasos 2 a 5, que es el perfil madre e
      hijo del 9.6.2. Y la senal que el 9.6.2 declara mas fiable, los
      entregables, apunta al mismo lado: la madre entrega el plan anual
      con metas integradas MAS la forma de reconocimiento, dos productos,
      y el hijo entrega solo el primero, que es exactamente el ejemplar
      del puesto 2.215 citado en la regla. Tu razon dice que el camino de
      4 saltos por revision_progreso mata la arista, y el camino existe y
      arranca donde dices; lo que discuto es su direccion: arranca en el
      nodo del PASO 3 y desemboca en el contenido del PASO 1, o sea va
      hacia atras en el orden de la madre, y por dos nodos de gobernanza
      que la madre no enumera. La adjudicacion 6.1 del acta 83 pide dos
      cosas y no una: que arranque de lo que el paso nombra o de un hijo
      de un paso, Y que avance en el orden que la madre o los nodos
      declaran. El contraste esta en tu propia tanda: el par 66 se
      sostiene NO SE ENLAZA porque alli el camino arranca en el nodo del
      paso 5 y desemboca en el del paso 6. Ese si avanza.
    - PAR 77, eliminacion_inspeccion_masiva_por_control_estadistico ->
      carta_de_control_shewhart (paso 3). Digo SE ESCRIBE. La madre tiene
      nodos_siguientes VACIO (lo medi hoy, y tu propia razon lo dice), y
      mi BFS dice que el hijo NO es alcanzable ni a 30 saltos: es el caso
      puro del banco 9.6, un nodo entero que el lector no va a encontrar
      nunca porque nada lo lleva alli. El paso 1 nombra la carta
      ("Establecer cartas de control para verificar la estabilidad") y el
      paso 3, que es el que la unidad trae, la vuelve a nombrar
      ("mantenimiento de la carta de control"). El hijo trae seis pasos
      propios y la madre conserva su tesis entera. Tu razon dice
      direccion invertida porque la carta es fundacional, y eso es cierto
      como observacion, pero el 9.6.2 dice que la vara pregunta que anade
      el HIJO a la MADRE, nunca al reves, y su formulacion citable es que
      una linea que tarda siete pasos en ejecutarse no es una linea, es
      un procedimiento nombrado en una linea, y que la prueba de que el
      paso es un procedimiento es que existe el hijo que lo ejecuta. Si
      "el hijo es mas fundacional" bastara, moririan todos los pasos que
      invocan una herramienta, que es la reduccion al absurdo que la
      propia regla escribe.

- TAREA 3, EL INSTRUMENTO, Y ES BLOQUEANTE. Tres piezas, las tres
  adjudicadas en el acta 84 (6.3 y 6.4), sin doctrina nueva. Commit
  propio.
  (3.a) EL REGISTRO SE HORNEA DOS VECES. Primero AHORA, despues de la
  TAREA 2 y ANTES del filtro, para que el tramo 9 (y lo que la relectura
  conjunta haya escrito) este dentro; y otra vez AL CIERRE de la vuelta,
  despues de escribir todo lo que esta vuelta escriba, para que el tramo
  10 entre. El horneador no cambia de mecanismo: ya descubre por patron y
  eso lo verifique leyendo su codigo. Lo que cambia es CUANDO corre, y
  eso se deja escrito en su docstring para que no dependa de que el
  encargo se acuerde. VARA DE CONTRASTE MEDIDA POR MI HOY, corriendo tu
  propio horneador y restaurando el fichero despues: con el tramo 9
  dentro y sin nada mas, el registro pasa de 126 a 156 filas (79 ESCRITA,
  77 NO SE ENLAZA), con 5 ascendidas y 4 degradadas. Si la TAREA 2
  escribe alguno de los tres pares, esas filas suben a ESCRITA y el
  reparto cambia: la DISCREPANCIA CONTRA MI VARA SE DECLARA, no se
  resuelve copiando (EJECUTOR.md regla 2).
  (3.b) LAS DOS FRASES QUE CAYERON SE TALLAN.
  scripts/loop/tallar_cabecera_reporte.py gana DOS FILAS mas en el modo
  --fase04, y las dos salen de ficheros de salida, no de prosa:
    - ARISTAS MOVIDAS EN LA VUELTA: cierre menos apertura en las CUATRO
      cifras (nodos_siguientes, nodos_previos, suma, union), contadas de
      los ficheros de conteo de la propia vuelta, con el desglose por
      tanda de escritura si hay mas de una.
    - DESFASE DEL CALIBRADO RASTREADO: cuantas filas de
      docs/plan/PASO_NODO_CALIBRADO.jsonl tienen el campo arista
      distinto de lo que dice el grafo de hoy, con la lista de esas filas
      cuando sean pocas. Hoy son TRES y las nombro en el acta.
    CASOS OBLIGATORIOS, los dos con su salida citada en el reporte: (i)
    VERDE, las dos filas talladas sobre los ficheros de ESTA vuelta y
    --comparar docs/loop/REPORTE.md dando CABECERA IDENTICA AL TALLADOR
    con las dos filas nuevas dentro; (ii) ROJO INVENTADO POR TI, una
    copia del reporte con una de las dos celdas nuevas adulterada, que
    tiene que morder con exit 1 y nombrar cual.
  (3.c) EL --comparar DEL TRAMO SE VUELVE A CORRER, esta vez sobre el
  tramo 10 y contra TU PROPIO REPORTE, con CABECERA Y TABLA DE LA CADENA
  IDENTICAS y EXIT 0, y su salida citada. Es el caso que la vuelta 83 no
  corrio y la 84 si: no se afloja.

- TAREA 4, EL TRAMO 10 DE OP-E-01, leido POR LO NO DECIDIDO con el
  registro ya crecido. Bolsa recalibrada FRESCA antes de leer (el grafo
  se movio: seis aristas en la vuelta 84 y las que escriba la TAREA 2 de
  esta), con el filtro P.9.1 ensanchado, la guarda del par no dirigido y
  la vara de la cadena corridas ANTES de leer nada, y la tabla de
  alcanzabilidad TALLADA con el registro cruzado, con el horizonte
  publicado debajo tal como quedo adjudicado (acta 84, 6.6). La unidad de
  lectura son LAS PRIMERAS 30 UNIDADES SIN DECISION REGISTRADA, en orden
  de fichero y sin sorteo (acta 82, adjudicacion 5.1). Las decididas que
  sigan en la bolsa se listan por su nombre con su cuenta y NO se vuelven
  a leer ni se re-derivan sus razones. LA VARA DE LA CADENA SE APLICA CON
  EL CRITERIO DE LA ADJUDICACION 6.1 DEL ACTA 83, no por longitud: para
  cada unidad marcada ALCANZABLE, la razon dice si el camino es o no LA
  CADENA PROPIA de la madre, NOMBRANDO los nodos intermedios, el paso del
  que arrancan y SI AVANZA O RETROCEDE en el orden de la madre, que es lo
  que distinguio al par 66 del par 55. Marca los discutibles ANTES de
  saber si aciertas. Si entregas menos de 30, di cuantas leiste y por
  que, con la cuenta de lo que queda. COMMITEA POR MITADES si hace falta
  (EJECUTOR.md regla 6).
  VARAS DE CONTRASTE MEDIDAS POR MI HOY, para que sepas que tiene que
  salir: sobre la bolsa de hoy menos las tres escritas del tramo 9 quedan
  139 unidades, y con el registro re-horneado LA PRIMERA SIN DECIDIR ES
  search_for_business_model -> herramientas_computacionales_business_model
  (paso 8, dominio core), en el indice 75, con 64 sin decidir por detras.
  Si la TAREA 2 escribe los tres pares, la bolsa queda en 136 y ese mismo
  par baja al indice 72, con las mismas 64 sin decidir. Si tu corrida
  discrepa en un digito, LA DISCREPANCIA SE DECLARA.

- TAREA 5, la vara del tramo 10, corrida con instrumento propio y con los
  pares LEIDOS del fichero del filtro, no tecleados. Y el alcance queda
  fijado por la adjudicacion 6.5 del acta 84, para que no vuelva a haber
  ambiguedad: (5.a) LAS UNIDADES FRESCAS DEL TRAMO QUE ACABAS DE LEER, el
  10, contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl SIN direccion; (5.b) las
  mismas contra docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V84.jsonl, la
  bolsa de la vuelta ANTERIOR, buscando la reciproca. Cifras que yo ya
  medi hoy y que tienen que salir igual: 3.388 veredictos y 3.388 pares
  no dirigidos unicos, 142 unidades en la bolsa filtrada V84. Lo demas lo
  mides tu; si discrepa en un digito, LA DISCREPANCIA SE DECLARA.

- LA CABECERA DEL REPORTE SE TALLA con --fase04 --vuelta 85 y se pega
  entera, ahora con las dos filas nuevas de la TAREA 3.b dentro, y antes
  del commit de cierre --comparar docs/loop/REPORTE.md tiene que dar
  CABECERA IDENTICA AL TALLADOR, con su salida citada. La fila de
  identidad lleva el commit del acta y el HEAD real de la apertura: sella
  el HEAD con git rev-parse HEAD > docs/loop/SALIDA_V85_HEAD_APERTURA.txt
  ANTES de commitear nada, y tiene que salir el commit del acta de la
  vuelta 84. Mide la apertura antes de la primera operacion (Gate 0 el
  ciclo de tres, censo, aristas, motor, web y tsc), cada uno con su
  fichero, y recomputa el cierre AL CIERRE. Y commitea
  PASO_NODO_CALIBRADO.jsonl recalibrado tal como quede, con su desfase
  DICHO y medido en vez de negado, que es lo unico que la vuelta 84 hizo
  mal con ese fichero.

- Con el freno delante, y las cifras son del acta 84 seccion 7: la racha
  de CLASE O CIFRA PUBLICADA esta en CERO y la parada pide DOS seguidas;
  van siete vueltas limpias de esas dos especies, la racha mas larga de
  la campana. La de REPORTE sube de CERO a UNO y la parada pide TRES: no
  se dispara, pero las dos caidas son de la especie que ya produjo una
  racha entera (vueltas 77, 78 y 79), asi que el remedio va en codigo y
  no en promesa. El credito de tanda queda REBAJADO, esta vez por caida:
  releere el tramo 10 ENTERO, no una muestra, mas lo que resuelvas de 50,
  55 y 77. Y lo que mas te conviene tener presente: las dos faltas de
  esta vuelta fueron frases de prosa que contradicen a la tabla tallada
  que ellas mismas acompanan. Antes de cerrar, repasa el encargo punto
  por punto y di de cada uno si se corrio o no; y si cambias el alcance
  de una tarea porque el encargo se contradice, DILO en ese repaso en vez
  de renombrar la tarea, que es lo que paso con la TAREA 4.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
