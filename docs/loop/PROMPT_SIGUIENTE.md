Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ESTA ES LA VUELTA 115, NO LA 114 OTRA VEZ. El numero 114 quedo gastado
por mi acta (precedente del acta 81 seccion 5.3). Tus ficheros se llaman
SALIDA_V115_*, y los diez SALIDA_V114_*_APERTURA.txt que ya estan en el
arbol son pieza historica: NO se tocan, NO se reusan, NO se borran.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V115_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 115 con EXIT 0. Y
ESTA VEZ SU SALIDA SE COMMITEA, en docs/loop/SALIDA_V115_APERTURA_SELLADA.txt,
no solo se corre: la 114 no dejo la suya y yo no pude saber si la habia
corrido (acta 114, 4.3). Corrida sin fichero es corrida que no existe.

LO PRIMERO QUE TIENES QUE SABER, Y NO ES UN REPROCHE: LA VUELTA 114 NO SE
ENTREGO ENTERA. Corrio seis minutos y cuarenta y seis segundos, commiteo
TRES tramos y murio. No escribio REPORTE.md, ni ciclo de cierre, ni
guardas. LO QUE SI ENTREGO ESTA BIEN HECHO Y LO VERIFIQUE ENTERO. El acta
de la vuelta 114 esta en docs/loop/ACTA_AUDITOR.md a partir de la linea
39830. En resumen, y sin adornarlo:

TUS TRES PIEZAS CALZAN TODAS Y LAS CORRI YO. La apertura esta sellada de
verdad: verificar_apertura_sellada.py --vuelta 114 me da VERDE EXIT 0 con
los diez ficheros nacidos en a33dab20, hijo directo del acta c1fb9681. El
techo de la TAREA 3.0 nace en 27dec876 con solo su fichero y su script, o
sea sellado antes de medir, y sus cuatro cifras me salen identicas (10
fase 04, 10 fase 05, 220 decididas, 71 total). El barrido de la TAREA 2.1
lo rehice CON CODIGO MIO sobre los 620 ficheros .py de scripts/loop:
crudo 16 / 5 / 59 / union 73, neto 15 / 4 / 58 / union 72, identico a tu
salida, y tu script corrido por mi da salida IDENTICA BYTE A BYTE, igual
que la MUTACION Y. La TAREA 2.5 corrige la ruta de forma aditiva y los
dos ficheros que cita existen en disco (2.098 y 2.889 bytes) mientras que
el que nombraba mal sigue sin existir. Las caidas 4.1 y 4.3 del acta 113
quedan CERRADAS.

Y VERIFIQUE TODO LO DEMAS AUNQUE TU NO LLEGARAS A ESCRIBIRLO. Censo
3.853 / 3.188 / 665, aristas 9.190 / 9.169 / 18.359 / 9.813 con cero
auto-aristas y cero duplicadas, Gate 0 OK con alcanzabilidad 100,0%
(3188/3188) y 85 semillas y salida IDENTICA a la tuya, grafo en 8.391.653
bytes y sha256 f0e399396745 tras el ciclo de tres entero, motor 25/25,
web 80 (80) / 1.030 y 3 skipped, tsc EXIT 0 y cero lineas, marcador A 551
/ B 72 / C 5 / D 2.760 sin huecos y con las diez tasas por dominio
identicas, desfase en 1 fila de 468, cierre efectivo 74 / 109 (59,6%) e
invertidas 2, bolsa 74/74/0. Diff sobre dataset/, web/ y engine/ commit a
commit sobre los TRES: CERO lineas. docs/plan/ NO se toco en todo el
tramo. Guiones largos y medios: CERO. Y corri tus guardas heredadas
(vuelta113_guardas_cierre.py) sobre el arbol de hoy: EXIT 0 y salida
IDENTICA BYTE A BYTE, sus veintiseis casos y sus nueve instrumentos, o
sea que tu retoque del docstring no rompio ninguna.

LO QUE COBRO ES UNA SOLA COSA Y ES MIA. La letra de mi 2.1 decia "si tu
recuento crudo no es el mio, PARAS Y LO TRAES", y ordenaba su propio
imposible: la cura encargada era un fichero NUEVO dentro de scripts/loop,
o sea dentro del conjunto que el barrido mide, y ese fichero cita por
fuerza las tres cadenas que busca. El crudo de hoy NO PODIA ser el mio.
Tu resolviste bien y no te lo cobro: no paraste, publicaste los dos
recuentos, y dejaste escrito en la salida, en el docstring y en el asunto
del commit por que el comparable es el neto. QUEDA ADJUDICADO POR
EXTENSION NATURAL del acta 113 seccion 4.4: CUANDO LA PROPIA CURA ENTRA
EN EL CONJUNTO QUE LA VARA MIDE, EL CONTRASTE DEL AUDITOR SE COMPARA
CONTRA EL NETO, LA DIFERENCIA SE DECLARA EN LA SALIDA, Y ESO NO ES
PARADA. La constancia sigue yendo a los tres sitios: instrumento, commit
y reporte.

Y LO QUE NO COBRO. La vuelta parcial queda REGISTRADA CON NOMBRE en mi
acta y NO ACUMULA EN NINGUNA RACHA, por la aritmetica que el acta 81 dejo
escrita: las rachas se miden sobre caidas de clase, de cifra publicada y
de reporte, y una vuelta sin reporte no es ninguna de las tres porque no
hay afirmacion equivocada, no hay afirmacion. Y es MAS LEVE que la 81:
aquella murio sin un solo commit y perdio su trabajo; la tuya commiteo
por tramo como manda EJECUTOR.md regla 6 y las tres piezas estan
salvadas. LA REGLA FUNCIONO, Y POR ESO ESTA VUELTA LA APRIETO: cada tarea
va en SU PROPIO COMMIT, para que si la sesion vuelve a morir se pierda
como mucho una.

ESTA VUELTA TERMINA LA 114. No se abre ninguna fase, no se escribe ni se
retira una sola arista, no se toca el campo estado de ninguna operacion,
no se mueve ninguna operacion de fase. El diff sobre dataset/, web/ y
engine/ tiene que dar CERO lineas al cierre, medido commit a commit.

- TAREA 1, LOS REGISTROS, Y SON DOS BLOQUES PORQUE LA 114 NO ESCRIBIO EL
  SUYO. Van los dos en docs/PENDIENTES.md, cada uno en su seccion propia
  y claramente nombrada, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su fichero de salida
  commiteado, y con la extraccion del bloque hecha DESPUES de la ultima
  edicion, con su diff de fidelidad como las tres vueltas pasadas.
  Numera los subapartados COMO ESTAN AQUI.

  BLOQUE A, HEREDADO: LOS REGISTROS DEL ACTA 113, que el encargo de la
  114 pidio y la 114 no llego a escribir. Van tal cual estaban pedidos:
  (A.1) LA CAIDA DEL EJECUTOR DEL BARRIDO QUE SE EXCLUYE A SI MISMO SIN
  DECIRLO EN LA SALIDA, con las dos ternas de cifras (15 / 4 / 58 / 72
  crudas contra 14 / 3 / 57 / 71 publicadas), el nombre del unico fichero
  de diferencia, la constancia de que la exclusion es legitima y esta en
  el docstring de buscar(), la constancia de que la conclusion aguanta y
  la verifico el auditor, y la de que fue la SEGUNDA vuelta seguida de la
  especie. Y ANADE, porque ya es medible: QUEDA CERRADA en la vuelta 114
  (barrido nuevo con crudo/neto y seccion EXCLUSIONES, verificado por el
  auditor con codigo propio, acta 114 seccion 2a).
  (A.2) LA CAIDA DE LA CITA QUE PROMETE DETALLE Y NO LO TIENE, con la
  linea literal que el fichero si trae sobre T, los dos sitios donde el
  detalle si esta, y el limite del instrumento que destapa (comprueba
  existencia, no contenido). Y ANADE que SIGUE ABIERTA: su remedio es la
  TAREA 2.3 de esta vuelta.
  (A.3) LA CAIDA DE RUTA EN EL DOCSTRING, con el nombre citado y los dos
  nombres reales. Y ANADE que QUEDA CERRADA en la vuelta 114 (acta 114
  seccion 2c).
  (A.4) LA CAIDA DEL AUDITOR DE ENCARGO POR EL IMPOSIBLE DE T, con la
  doctrina adjudicada escrita entera (el esperado se actualiza y la
  constancia va en los tres sitios) y con la constancia de que el
  ejecutor lo resolvio bien.
  (A.5) LA CAIDA DEL AUDITOR DE ENCARGO POR LA REGLA 3.6 CORTA, con los
  ocho puestos nombrados (20, 31, 93, 147, 161, 172, 174, 175) y con la
  extension adjudicada escrita entera: la 3.6 alcanza al campo razon de
  la fila Y a la razon de cualquier correccion_vNN declarada sobre ella.
  (A.6) LO QUE NO ES CAIDA EN LA 113: la frase del tsc de la 112, el
  cambio de cuatro a tres exclusiones en la mutacion X, y la escoria del
  dry run del auditor.

  BLOQUE B, LOS REGISTROS DEL ACTA 114:
  (B.1) LA VUELTA 114 COMO VUELTA PARCIAL, con la lista literal de lo que
  quedo sin hacer, con la constancia de que NO ACUMULA EN NINGUNA RACHA y
  el motivo escrito (acta 81 seccion 7: sin afirmacion no hay afirmacion
  equivocada), y con la diferencia medida contra la 81 (aquella sin un
  solo commit; esta con tres tramos salvados por EJECUTOR.md regla 6).
  (B.2) LO QUE LA 114 SI ENTREGO Y CALZA: apertura sellada VERDE, techo
  sellado en su propio commit, TAREAS 2.1, 2.2 y 2.5, con la constancia
  de que el auditor rehizo el barrido con codigo propio y de que las dos
  salidas salen identicas byte a byte. CERO caidas del ejecutor.
  (B.3) MI CAIDA DE ENCARGO POR LA LETRA DEL CRUDO IMPOSIBLE, con la
  doctrina adjudicada escrita entera (cuando la propia cura entra en el
  conjunto que la vara mide, el contraste se compara contra el NETO y la
  diferencia se declara en la salida).
  (B.4) LA OBSERVACION QUE NO ES CAIDA: la salida de
  verificar_apertura_sellada.py --vuelta 114 no quedo commiteada, el
  auditor no supone en ninguna direccion, la corrio el y salio VERDE EXIT
  0, y la letra queda apretada para esta vuelta.

- TAREA 2, BLOQUEANTE: LAS DOS CURAS QUE FALTAN, CADA UNA CON SU
  MUTACION. La 2.1, la 2.2 y la 2.5 YA ESTAN HECHAS Y VERIFICADAS: NO SE
  REHACEN Y NO SE TOCAN SUS FICHEROS.
  (2.3) LA SALIDA DE GUARDAS ESCRIBE EL MOTIVO DE TODO ESPERADO QUE
  CAMBIA. En el guardas de esta vuelta (fichero nuevo, vuelta115_*; el de
  la 113 es historia y no se toca), cada caso lleva su esperado Y, cuando
  ese esperado sea DISTINTO del que la vuelta anterior daba por bueno,
  una linea de MOTIVO en la propia salida, no solo en el codigo. Empieza
  por T, que arrastra el motivo desde la 113. Asi la frase "el detalle
  esta en el fichero" se vuelve cierta por construccion, y la caida A.2
  se cierra.
  (2.4) MUTACION Z, del lado rojo: cambia el esperado de UN caso en una
  copia del script SIN escribirle motivo, y la salida tiene que
  DELATARLO, no decir CALZA en silencio. Pega la salida de antes y la de
  despues, cada una en su fichero nombrado.

- TAREA 3, EL CENSO MEDIDO DE DONDE ESTAMOS, Y NO SE ABRE NINGUNA FASE.
  El territorio de lectura de OP-E-03 SE ACABO: las 109 NO RESUELTA estan
  releidas enteras (80 en la 112, 8 mas 21 en la 113) con cosecha cero en
  las tres tandas. Esta vuelta se mide y se registra el estado.
  (3.0) EL TECHO, OTRA VEZ Y EN SU PROPIO COMMIT ANTES DE MEDIR. NO
  reescribas scripts/loop/vuelta114_tarea3_0_techo.py, que es historia:
  CORRELO tal cual, guarda su salida en
  docs/loop/SALIDA_V115_TAREA3_0_TECHO.txt, commiteala SOLA, y DI en el
  reporte si calza o no con la de la 114. Mi medicion de hoy, para
  contrastar y no para copiar: 10 fase 04, 10 fase 05, 220 decididas, 71
  total.
  (3.1) CENSO DE LA FASE 04 CON UN TALLADOR, no tecleado: las diez
  operaciones con su id_op, su tipo, su estado, su orden y, para cada
  una, sus dependencias declaradas CON LA FASE Y EL ESTADO DE CADA UNA,
  leido de docs/plan/OPERACIONES.jsonl. Publica la tabla. MI MEDICION,
  PARA CONTRASTAR Y NO PARA COPIAR: OP-E-01 ENLACE LISTA orden 1 sin
  dependencias; OP-E-02 ENLACE HECHA orden 2 sin dependencias; OP-E-03
  LECTURA DIRIGIDA LISTA orden 3 (OP-E-01 de 04, OP-U-02 de 03);
  OP-M-03-ENLACES ENLACE LISTA orden 4 (OP-M-03-I, -II, -III, las tres de
  03); OP-E-04 ENLACE LISTA orden 5 (OP-M-01 de 06, OP-M-01-FUSION de
  03); OP-E-05 ENLACE MUTUO LISTA orden 6 (las mismas dos);
  OP-M-01-ESLABONES ENLACE LISTA orden 7 (las mismas dos); OP-M-01-SEXTO
  ENLACE MAS PODA DEL SOLAPE LISTA orden 8 (las mismas dos); OP-E-06
  ENLACE CON EVIDENCIA DE LECTURA LISTA orden 9 (OP-D-01 a OP-D-07, las
  siete de 02); OP-E-07 LECTURA DIRIGIDA CORTA LISTA orden 10 (OP-E-06).
  Si tu tabla no es la mia, PARAS Y LO TRAES.
  (3.2) OP-E-01 CONTRA EL GRAFO, HOY. Cuenta sus 220 decididas por su
  campo decision y comprueba, contra dataset/metadata/master_graph.json,
  cuantas de las ESCRITA estan presentes como arista y cuantas ausentes.
  MI MEDICION, CORRIDA HOY CON CODIGO PROPIO, PARA CONTRASTAR Y NO PARA
  COPIAR: 220 filas, 98 ESCRITA y 122 NO SE ENLAZA, y las 98 PRESENTES en
  el grafo con CERO ausentes. Una arista cuenta como presente si el hijo
  esta en nodos_siguientes de la madre O la madre esta en nodos_previos
  del hijo: di cual de los dos criterios usas. Si tu cuenta no es la mia,
  PARAS Y LO TRAES.
  (3.3) EL REGISTRO DE CIERRE DE LECTURA DE OP-E-03 en
  docs/plan/04_ENLACES.md, apartado nuevo y ADITIVO (no se borra una
  palabra de los apartados viejos), con las cifras medidas por ti hoy:
  109 igual a 80 mas 8 mas 21, cosecha cero en las tres tandas, cifra de
  cierre 74 / 109 (59,6%) sin cambio, y la constancia expresa de que
  estado NO SE TOCA y sigue en LISTA (acta 100 4.2, doctrina vigente).
  Mide la aditividad con difflib y commitea su salida.
  (3.4) CENSO DE LA FASE 05, SOLO MEDIR: sus diez operaciones con su
  estado, su orden, sus dependencias declaradas y su bloquea_a. NO
  ADJUDICAS NADA, NO ABRES NADA: la decision de orden es del auditor de
  la 116 y la quiero tomar con tu censo delante. MI MEDICION, PARA
  CONTRASTAR Y NO PARA COPIAR: diez operaciones, LAS DIEZ EN LISTA;
  NUEVE sin ninguna dependencia declarada (OP-S-01, OP-S-02, OP-S-03,
  OP-S-04, OP-S-05, OP-S-08, OP-S-09, OP-S-10, OP-S-11) y UNA con
  dependencias, OP-S-12, que depende de OP-S-01 y OP-S-09 de su propia
  fase mas OP-D-01 a OP-D-06 de 02 y OP-U-01 de 03; OP-S-11 declara
  bloquea_a OP-A-01 y OP-A-02, y OP-S-12 declara bloquea_a OP-C-05.
  Y AQUI VA UNA TRAMPA MEDIDA QUE TE AHORRO: NO PUEDES RESPONDER "CUALES
  DEPENDEN DE ALGO QUE NO ESTE CERRADO" LEYENDO EL CAMPO estado, porque
  la doctrina vigente (acta 100 4.2) es que estado NO SE TOCA, y por eso
  las operaciones de las fases 02 y 03 siguen diciendo LISTA aunque la
  fase 03 quedo CERRADA CON REMISION en la vuelta 74. PUBLICA EL CAMPO
  TAL COMO ESTA Y DECLARA ESA LIMITACION EN LA PROPIA SALIDA; no la
  resuelvas tu, que eso es adjudicacion y es mia.
  (3.5) LO QUE NO SE TOCA: cero aristas escritas o retiradas, cero
  cambios en el campo estado, cero operaciones movidas de fase, no se
  abre la fase 05 ni la 06. El diff sobre dataset/, web/ y engine/ tiene
  que dar CERO lineas al cierre, medido commit a commit como siempre.

- LAS GUARDAS DEL CIERRE, y siguen siendo NUEVE instrumentos y VEINTIOCHO
  casos. Contados uno por uno.
  INSTRUMENTOS (9): los mismos nueve, con su --vuelta actualizado a 115
  (tallar_veredictos_reporte.py sobre tu propio reporte;
  tallar_nombre_de_operacion.py OP-E-03;
  verificar_apertura_sellada.py --vuelta 115;
  verificar_cabecera_pegada_o_condensada.py --vuelta 115;
  verificar_cobertura_bolsa_tres_vias.py; contar_cierre_efectivo.py;
  verificar_vuelco_de_veredicto.py; tallar_cabecera_reporte.py --fase04
  --vuelta 115; tallar_cifras_de_antes.py sobre tu propio reporte).
  CASOS DE MUTACION (28): los VEINTISEIS de la vuelta 113 (A, B, C, D, E,
  F, G, H, el reporte 102 por git show f253842b, mI.md, mJ.md, mK.md,
  mL.md, mM.md, la de la TAREA 2.4 de la vuelta 109, N, O, P, Q, R, S, T,
  U, V, W y X) MAS Y (el barrido de la 114 corrido con --sin-exclusion) y
  Z (un esperado cambiado sin motivo, la salida lo DELATA).
  LOS RESULTADOS QUE NO PUEDEN CAMBIAR: A, B, C, E, F, G en ROJO EXIT 1;
  D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; I ROJO por la
  promesa falsa; J ROJO senalando fila 7 apertura; K ROJO por numero de
  filas; L ROJO EXIT 1 con 0 DISTINTA y 3 AUSENTE; M ROJO EXIT 1 con
  CUATRO celdas; la de la TAREA 2.4 con el 123 pasando de DECLARADO a
  MUDO; N ROJO nombrando el 87 en_sitio; O ROJO nombrando el 91 cruce; P
  ROJO nombrando el 154 en_sitio; Q y R en ROJO con la linea que les
  toca; S y U en VERDE EXIT 0; V y W en VERDE EXIT 0 con celdas
  DISTINTAS entre si; T en ROJO EXIT 1 CON SU MOTIVO ESCRITO EN LA SALIDA
  (esperado actualizado en la vuelta 113, adjudicado en el acta 113
  seccion 4.4); X en ROJO EXIT 1. La H sigue siendo la frontera declarada
  por diseno: si algun dia da ROJO, eso no es una mejora, es que se movio
  el perimetro sin decidirlo, y paras.
  Y LA Y SE VERIFICA POR SU PROPIEDAD, NO POR SUS NUMEROS, y esto es
  medicion mia de hoy y no un permiso suelto: el barrido cuenta ficheros
  .py de scripts/loop, y esta vuelta va a crear al menos dos (tu guardas
  y tu tallador de censo), asi que los absolutos 16 / 5 / 59 / 73 y
  15 / 4 / 58 / 72 PUEDEN SUBIR legitimamente. Lo que la guarda Y exige
  es la PROPIEDAD: con exclusion, crudo distinto de neto en al menos una
  busqueda y el fichero excluido NOMBRADO con su motivo; sin exclusion,
  crudo igual a neto y el fichero nombrado como no excluido. Publica los
  absolutos que te salgan y di contra que cifra de las mias los comparas.
  Si algun absoluto BAJA, eso si es rojo y PARAS.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Va fijo el
  sellado de la apertura con su salida commiteada, que es antes de todo;
  el sellado del techo de la 3.0 en su propio commit ANTES de la primera
  medicion de la TAREA 3; y que la TAREA 2 quede cerrada con su mutacion
  Z ANTES de que escribas una sola cifra de "antes" en el reporte:
  primero la guarda reparada, despues el dictado que ella vigila. Y UNA
  MAS, QUE NACE DE LA 114: CADA TAREA VA EN SU PROPIO COMMIT, con su
  asunto diciendo que tarea cierra, y el push detras. Si la sesion muere,
  que cueste una tarea y no una vuelta.

- LO QUE NO SE ABRE Y LO QUE SIGUE ANOTADO. La deriva de contenido (26
  nodos de 140, 32 pares de 87, acta 92 seccion 4.4), los siete nodos con
  guion, el bloque repetido de formalizar_un_proceso_ad_hoc y los titulos
  gemelos por mayuscula (sistema_responsabilidad_gerencial y su _2) siguen
  ANOTADOS PARA ALEXIS Y SIN ENCARGAR, porque rozan el ALCANCE de la
  campana. Y sigue constando que Gate 0 tiene razon al dar 0 en
  duplicadas: su guarda dice "titulo_concepto EXACTO duplicado" y esos dos
  titulos no son exactos.

- LA NOTA DE HIGIENE DE SIEMPRE, remedida hoy por mi: git status trae M en
  dataset/metadata/master_graph.json desde antes de que nadie toque nada,
  y NO es un cambio (git diff sobre ese fichero da CERO lineas; es final de
  linea). Corri el ciclo de tres entero y despues medi: 8.391.653 bytes,
  sha256 f0e399396745. No lo commitees y no lo "arregles". El ciclo de
  tres es run_phase1.py, DESPUES etiquetas_de_cara.py CON --aplicar (sin
  --aplicar es dry run y el recompilado te deja las 71 etiquetas
  revertidas), y DESPUES sync_assets_web.py. El validador vive en
  scripts/run_phase1.py, y etiquetas_de_cara.py y sync_assets_web.py viven
  en scripts/, NO en scripts/loop/; el recomputador del marcador, en
  scripts/recomputar_marcador.py. Y aviso medido: run_phase1.py termina
  con EXITCODE 2 por la alarma de las etiquetas aunque imprima GATE 0: OK;
  el verde que se publica es el de la linea "GATE 0: OK" y el ciclo se
  cierra con los otros dos pasos, no el exitcode del primero.

- Y LAS CINCO DEL DICTADO, INTACTAS. La primera: toda cifra que publiques
  sobre un estado ANTERIOR se mide corriendo el instrumento sobre ese
  estado y se cita el fichero de salida; si la frase habla del antes Y del
  despues, son DOS ficheros, uno por lado. La segunda: toda vara que
  corras declara SU TECHO medido antes de correrse y SELLADO en su propio
  commit; una cosecha 0 sin techo declarado no cuenta como prueba de
  salud. La tercera: EL DOCSTRING DE UN INSTRUMENTO ES EXPEDIENTE Y SE
  MIDE COMO EL REPORTE, y el mensaje de commit igual. La cuarta: NO SE LE
  CAMBIA LA CONVENCION DE ENTRADA A UNA GUARDA SIN CORRER LA GUARDA
  DESPUES Y MIRAR SU SALIDA. La quinta: UNA CITA QUE PROMETE DETALLE
  ("declarado con el detalle completo en X", "explicado en X", "con su
  motivo en X") SOLO SE ESCRIBE SI X CONTIENE ESE DETALLE; si el detalle
  vive en el codigo o en el mensaje de commit, la cita nombra ESE sitio, o
  se mete el detalle en el fichero.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
