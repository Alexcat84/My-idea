Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

El acta de la vuelta 97 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 34539. En resumen, y sin adornarlo:

EL DATO ESTA SANO Y TU TRABAJO ES BUENO. Verifique el grafo en SEIS refs
con sha256 en las seis, cero aristas movidas, Gate 0 identico byte a byte
tras transcodificar, las tres suites, el marcador, la cabecera con
--comparar en 9 filas y 0 distintas, los cinco puntos de OP-E-03 con
cruce propio (incluido el 2.796), las dos tablas de la senial con MI
mediana y DOS normalizaciones de fuente, la mutacion 12 de 12, la
idempotencia disparada en vivo, y DOCE cuentas de piezas talladas una
por una: las doce calzan. Segunda tanda seguida con la especie cortada.
Mi lectura ciega dio 12 de 13.

PERO LA VUELTA TRAE UNA CAIDA DE CIFRA PUBLICADA Y DOS DE REPORTE, y la
racha de clase o cifra publicada pasa de CERO (tres tandas: 94, 95, 96)
a UNO. No es parada, porque la parada pide DOS tandas seguidas. Te lo
digo entero y al frente: SI LA VUELTA 98 TRAE OTRA DE ESA FAMILIA, ES
PARADA. La racha de REPORTE que acumula sigue en CERO (las dos de esta
vuelta viven en prosa y no acumulan por la letra del 27 ago), asi que NO
hay escalada que encargar, y lo digo expresamente para que mi silencio
no se lea como la omision de la vuelta 89.

- TAREA 1, BLOQUEANTE Y PRIMERA: LA CORRECCION DECLARADA DE LA FECHA.
  Nada de la TAREA 2 se toca hasta que esto este commiteado.
  docs/plan/OPERACIONES.jsonl, nota de OP-E-03, dice "ADDENDUM DE
  EJECUCION (30 ago 2026, vuelta 97, TAREA 2)". NINGUN commit de este
  repo, en toda su historia, es posterior al 27 ago 2026: lo medi con
  git log --all --format=%ad --date=short | sort -u | tail -1, y los
  CUATRO commits de tu vuelta son 2026-08-27. El "30 ago" nace tecleado
  como constante literal en scripts/loop/vuelta97_tarea2_addendum_opE03.py
  linea 43 (MARCA = "..."). Es CAIDA DE CIFRA PUBLICADA por EJECUTOR.md
  regla 1 ("TODO HASH, NOMBRE DE COMMIT, RAMA O FECHA... SE LEE DE git
  rev-parse O DE git log EN ESA VUELTA Y SE TALLA; UNA LINEA DE IDENTIDAD
  TECLEADA NO SE PUBLICA") y regla 8 ("toda cifra con su fecha de corte"),
  y por la definicion de cifra publicada de AUDITOR.md seccion 4 ("una
  cifra que vive en docs/plan/ o en el banco"). Acta 97 seccion 4.1,
  linea 34956.
  (1.1) CORRIGE SIN BORRAR LO VIEJO, que es la regla de correccion
  existente y por eso esto NO es parada: el texto "(30 ago 2026, vuelta
  97, TAREA 2)" se queda donde esta y DEBAJO va la correccion declarada,
  con la fecha real LEIDA DE GIT en esta vuelta y su comando pegado.
  (1.2) ARREGLA LA FUENTE, no solo el sintoma: la constante MARCA del
  script deja de tener la fecha tecleada y la LEE de git en tiempo de
  ejecucion. Si eso no es posible sin reescribir el addendum ya aplicado,
  lo dices con la cifra y dejas el script con un assert que CAIGA si la
  fecha de la marca no es la que git devuelve hoy. Prueba de mutacion
  obligatoria para ese assert (EJECUTOR.md regla 1, EL CASO ROJO SE
  PRUEBA POR MUTACION): cambias la fecha esperada y compruebas que CAE.
  (1.3) LA MISMA ESPECIE ESTA EN LA VUELTA 94, y no es tuya de hoy: su
  addendum dice "29 ago 2026" contra el mismo reloj de 27 ago. La
  verifique yo y ninguna acta la cazo, incluida la 94, cosa que declaro
  como falla de mi oficina en el acta 97 seccion 6 punto 3. Corrigela
  con el mismo gesto y en el mismo commit. NO la cuento para la racha
  retroactivamente: AUDITOR.md no tiene letra para eso y fabricarla seria
  doctrina nueva.
  (1.4) MIDE Y DECLARA la serie entera: recorre TODOS los addenda de
  docs/plan/OPERACIONES.jsonl que lleven fecha, coteja cada uno contra
  git log, y publica la tabla con su instrumento. Si hay mas de dos, las
  quiero todas en esa tabla, no solo las dos que yo encontre.

- TAREA 2, LOS REGISTROS DEL ACTA 97. En docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y no contada a ojo. Y esta
  vuelta el caso positivo del tallador SE COMMITEA con su fichero de
  salida: el de la vuelta 97 era cierto (lo corri yo y da 1 y 4) pero no
  dejo fichero, y una garantia sin salida guardada no se puede auditar
  la vuelta siguiente.
  (2.1) LAS OCHO ADJUDICACIONES del acta 97 (3.1 a 3.8), cada una por su
  numero y con su linea leida en esa vuelta, y con su efecto sobre el
  trabajo. Las que cierran cosas:
  La 3.1 (linea 34759) CONFIRMA que la subida al 45% ES LA BOLSA Y NO TU
  VARA. Lei a ciegas las CINCO no resueltas de mayor titulo_ratio (43,
  63, 67, 85, 96), o sea la muestra elegida en tu contra, y llegue a NO
  RESUELTA en las cinco por mi cuenta. EL UMBRAL NO SE TOCA, misma letra
  que la 4.4 del acta 96. Y tu caveat se queda entero: esto no PRUEBA que
  el umbral sea correcto, falla en refutarlo donde era mas facil, que es
  todo lo que este control puede dar.
  La 3.3 (34834) CONFIRMA el 66 y el 77 en LEIDA. La 3.4 (34847)
  CONFIRMA el 47 en B. La 3.5 (34859) CONFIRMA que NO afirmar las
  inversiones del 82, 89 y 65 fue PRUDENCIA y no incoherencia con el par
  16: en el 16 habia linea de un lado y nueve pasos del otro, o sea algo
  que invertir; en esos tres no hay linea y procedimiento en ninguno de
  los dos sentidos. La 3.6 (34876) CONFIRMA las NUEVE figuras sin
  colapsar ninguna: la proporcion es identica a la del tramo 1 (0,150 por
  par en los dos), las que llamas propiedades del barrido son TRES
  mecanismos distintos, y la 8 no pertenece a ese grupo porque su propio
  texto dice que no es defecto del barrido. NADA DE ESO SE REHACE.
  La 3.7 (34896) adjudica que el ADDENDUM NO FUE EXTRALIMITACION.
  Verifique que el encargo de la vuelta 96 tampoco lo pedia y que el acta
  96 lo acepto, y la regla que lo cubre por extension es AUDITOR.md 0 y
  1.1 (el estado de verdad es el repo; una nota vieja nunca es fuente de
  una cifra nueva). PERO REGISTRA EL BORDE, que es lo que impide que sea
  un cheque en blanco: puedes mantener al dia una cifra publicada en
  ficheros del plan SIN encargo solo si (a) la cifra nueva sale de un
  instrumento corrido en esa vuelta, (b) la escritura es puramente
  aditiva y no borra el texto viejo, y (c) no mueve ninguna decision,
  ningun alcance y ningun estado. Fuera de esas tres, necesitas el
  encargo.
  (2.2) LAS DOS CAIDAS DE REPORTE, nombradas como tales, sin borrar el
  texto viejo. La primera (acta 4.2, linea 34998): tu explicacion de la
  codificacion decia que la salida equivalente de la vuelta 96 SI es
  UTF-8 "y no una propiedad del instrumento". Las dos mitades caen y las
  medi: SALIDA_V96_GATE0_CMD1_APERTURA.txt son 81 lineas de run_phase1
  solo con CERO bytes no-ASCII (UTF-8 valida por vacio, no podia revelar
  nada) contra tus 312 lineas del ciclo entero con 88 bytes no-ASCII; y
  MI PROPIA REDIRECCION de los mismos tres comandos hoy salio TAMBIEN en
  cp1252. Lo que hiciste bien queda escrito: lo encontro un instrumento,
  lo declaraste tu, dejaste los sha256, y NO volviste a correr el ciclo
  de tres para no convertir la apertura sellada en estado intermedio.
  Lo que fallo es el diagnostico, no el gesto.
  La segunda (acta 4.3, linea 35031): "estos son titulos que la web
  muestra" es falso para CINCO de los doce nodos con guion, porque estan
  DEPRECADOS y web/lib/engine/graph.ts lineas 142 y 158 los resuelve
  fuera del camino. La cifra 12 es correcta; VIVOS son SIETE.
  (2.3) LA RELECTURA AL DOBLE que esas dos disparan: los tramos son la
  prosa de declaracion de desviaciones y la prosa de la pregunta al
  fundador. En la vuelta 98, toda afirmacion de esos dos tramos lleva su
  medicion al lado o no se escribe. En particular: NINGUNA comparacion
  contra una vuelta anterior se publica sin haber medido primero que las
  dos cosas comparadas son equivalentes. Esa es la especie exacta de la
  4.2 y es la unica letra nueva que te pido.
  (2.4) LA PREGUNTA DE LOS NODOS CON GUION, CORREGIDA, sigue ANOTADA
  PARA ALEXIS Y SIN ENCARGAR, porque tocar nodos por una regla de estilo
  que ninguna operacion ordena roza el ALCANCE de la campana. Registra la
  cifra buena: SIETE vivos, no doce, y son costo_de_mala_calidad_copq,
  muestreo_dodge_romig, organizaciones_alta_confiabilidad_hro,
  realizar_analisis_ciclo_de_vida_lca, realizar_analisis_ciclo_vida,
  sistemas_alta_confiabilidad_hro y smed_setup_reduction. NO LOS TOQUES.
  Hiciste bien en no tocarlos y en traerla medida.

- TAREA 3, LA RELECTURA CONJUNTA DEL PAR 42. Es la unica discrepancia de
  mis trece lecturas ciegas, y cae DENTRO de tus discutibles marcados,
  asi que no baja el credito de la tanda. Acta 97 seccion 3.2, linea
  34789. MI CASO, para que lo verifiques contra el grafo: tu propia razon
  dice, casi con las palabras del banco 9.6.2, que "el hijo cabe entero
  dentro del paso 2 de la madre" y que "la madre conserva materia propia
  que el hijo no toca", que es EL TEST DE RECONOCIMIENTO de madre e hijo
  del 9.6.2; y la formulacion que el 9.6.2 manda citar dice que "una
  linea que tarda siete pasos en ejecutarse no es una linea: es un
  procedimiento nombrado en una linea, y la prueba de que el paso de la
  madre es un procedimiento es que existe el hijo que lo ejecuta". El
  paso 2 de cultura_justa_2 es una instruccion pelada sin una palabra
  sobre COMO, y preguntar_que_no_quien tarda cuatro pasos en ejecutarla,
  con un residuo que es secuencia con logica propia (mirar el sistema,
  anotar las condiciones, usar el hallazgo para cambiar el sistema). Por
  la tercera fila del 9.22 eso es procedimiento en un solo sentido: D.
  TU DECIDES CON LA VARA, no yo (AUDITOR.md 1.3 y la adjudicacion 4.5 del
  acta 96: la lectura ciega es control de la clase y detector de
  discrepancia, NUNCA fuente de direccion). Si te sostienes en A, escribe
  por que el residuo son dos lineas sueltas y no una secuencia, y queda
  cerrado. Si se mueve, va con correccion declarada y recomputo del
  addendum, porque la clase del 42 vive en docs/plan/.
  Y LO QUE YA ESTA ADJUDICADO Y NO SE REABRE: la premisa de tu discutible
  3 ("si el 42 es D, el 12 tambien lo era") ES FALSA, y la falsea tu
  propia razon del tramo 1, que dice que el hijo del 12 esta repartido
  entre los pasos 1, 2 y 4 de la madre, o sea que NO cabe dentro de UN
  paso. EL PAR 12 SE QUEDA EN A decidas lo que decidas sobre el 42.
  NINGUNA CLASE PUBLICADA DEL TRAMO 1 SE MUEVE.

- TAREA 4, EL TERCER Y ULTIMO TRAMO DE OP-E-03. Las 83 que quedan, filas
  101 a 183 de docs/plan/DIFERENCIA_CONTRA_COLA.jsonl, con
  scripts/loop/vuelta96_tarea3_tramo1_opE03.py --desde 100 --cuantos 83,
  el mismo instrumento sin tocarle una linea. CIERRA LA OPERACION.
  Si el tramo entero no cabe en una vuelta, PARAS DONDE VAYAS Y LO DICES
  CON LA CIFRA, igual que en la vuelta 94, y la 99 lo termina: prefiero
  cincuenta bien leidas que ochenta y tres a la carrera. Nadie te lo
  reprocha.
  Los CINCO PUNTOS de OP-E-03.verificacion se REMIDEN en la vuelta, no se
  heredan: cribado cerrado en 3.388 filas cada fichero contadas; ids por
  el RESOLUTOR antes de cruzar nada (P.1), y si no mueve ninguno lo
  declaras igual porque P.1 obliga; cuenta sin fugas contra los pares
  distintos de la cola tras resolver (el 2.796 ya tiene TRES varas: la
  tuya, la del acta 96 y la mia de esta vuelta); marca LECTURA DIRIGIDA
  en cada fila del material y del JSONL; y veredictos APARTE de la tasa
  por dominio del banco 9.27, en fichero propio y rotulado.
  EL UMBRAL DE DIRECCION NO SE MUEVE, ni para arriba ni para abajo. Esta
  adjudicado dos veces ya (acta 96 seccion 4.4 y acta 97 seccion 3.1), y
  la segunda con la muestra elegida en tu contra. Este tramo es el mas
  debil de la bolsa medido por tu propio instrumento (mediana 76,2 contra
  84,3 del tramo 1), asi que ESPERA UNA PROPORCION DE NO RESUELTAS AUN
  MAS ALTA QUE EL 45%. Si sale asi, no la maquilles ni la expliques: la
  publicas con la cifra y con la mediana del tramo al lado, que es
  exactamente lo que hiciste bien esta vuelta. Y SI SALE MAS BAJA, eso SI
  es la senial que hay que mirar de cerca, porque contradiria la
  tendencia medida: en ese caso lo dices y lo marcas como discutible.
  LAS FIGURAS del tramo, si las hay, REGISTRADAS Y SIN ADJUDICAR, mismo
  trato que las seis del tramo 1 y las nueve del tramo 2. Y aprovecha lo
  que tu mismo dejaste escrito: la figura 4 (nodos iman) y la 7 (falso
  amigo por nombre propio) son un aviso operativo para leer estas 83, no
  solo un adorno del acta anterior.
  AL CERRAR: el addendum del cierre de OP-E-03, con las tres condiciones
  del borde de la 3.7 cumplidas y verificadas, con --simular antes de
  --aplicar, con las cifras leidas del JSONL y no tecleadas, LA FECHA
  LEIDA DE GIT, y la idempotencia probada en vivo.

- LA DERIVA DE CONTENIDO (26 nodos de 140, 32 pares de 87, medida por el
  auditor en el acta 92 seccion 4.4) SIGUE ANOTADA PARA ALEXIS Y SIN
  ENCARGAR, porque roza el ALCANCE de la campana. No la toques. Citarla
  como contraste, con su fuente nombrada, es correcto.

- Con el freno delante: la racha de clase o cifra publicada esta en UNO y
  la de reporte en CERO. La cuenta de piezas de artefacto se talla
  SIEMPRE y se pega con su comando, NI SIQUIERA LAS FACILES, que es lo
  que lleva dos tandas cortando esa especie. Y ahora se le suma la
  hermana que cayo esta vuelta: TODA FECHA QUE ESCRIBAS EN UN FICHERO DEL
  PLAN SE LEE DE git log EN ESA VUELTA Y SE PEGA CON SU COMANDO. Una
  fecha tecleada es una linea de identidad tecleada.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
