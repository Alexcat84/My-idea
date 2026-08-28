Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ESTA ES LA VUELTA 117. El numero 116 quedo gastado por mi acta
(precedente del acta 81 seccion 5.3). Tus ficheros se llaman
SALIDA_V117_*, y los SALIDA_V116_* que ya estan en el arbol son pieza
historica: NO se tocan, NO se reusan, NO se borran.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V117_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 117 con EXIT 0 y SU
SALIDA COMMITEADA en docs/loop/SALIDA_V117_APERTURA_SELLADA.txt. La 116
lo hizo bien y lo verifique: sigue igual.

LA VUELTA 116 ENTREGO SUS TRES TAREAS Y SUS MEDICIONES SON CIERTAS AL
DIGITO. Las recompute todas con codigo mio: censo 3.853 / 3.188 / 665,
aristas 9.190 / 9.169 / 18.359 / 9.813 con cero auto-aristas y cero
duplicadas, Gate 0 OK con alcanzabilidad 100,0% (3188/3188) y 85
semillas, grafo en 8.391.653 bytes y sha256 f0e399396745 tras el ciclo de
tres entero, motor 25/25, web 80 (80) / 1.030 y 3 skipped, tsc EXIT 0 y
cero lineas, marcador A 551 / B 72 / C 5 / D 2.760 sin huecos y con las
diez tasas, desfase 1 de 468, cierre efectivo 74 / 109 (59,6%) e
invertidas 2, bolsa 74/74/0. Diff sobre dataset/, web/ y engine/ commit a
commit sobre los TRECE: CERO lineas. docs/plan/ NO SE TOCA en toda la
vuelta. Guiones: CERO. wc -l del reporte: 32, y su fichero dice 32. Tu
BFS del cierre transitivo me sale identico operacion por operacion, tu
nomina 2/9/2/2/1/0/0 = 16 tambien, tus 98 de 98 con extremos vivos y 0
bidireccionales tambien, y el techo es un diff de cero lineas contra el
de la 115. LA TAREA 2 ESTA BIEN HECHA Y CIERRA SU CAIDA: lei la capa de
motivo entera, ESPERADO_BASE_EXTRA es un literal fijo declarado aparte de
las constantes ACTUAL y de CASOS_OVERRIDE, la cobertura se cuenta del
codigo (28 de 28) y tiene rama SIN ANCLA por si faltara alguno, y la
MUTACION AA muerde: en el ANTES X y AA sin una sola ALERTA, en el DESPUES
X sigue en CALZA pero la ALERTA lo nombra, AA cae a NO CALZA y el ROJO
pasa de 2 a 4. CERO caidas de clase y CERO de cifra publicada.

LO QUE COBRO SON CUATRO COSAS Y NINGUNA MUEVE UN DATO. Y ANTES DE
ELLAS, LO QUE ME COBRO YO, QUE ES MAS GRANDE.

MI PRIMERA CAIDA: TE MANDE MEDIR EL DESBLOQUEO DE DOS OPERACIONES QUE YA
ESTABAN EJECUTADAS. OP-E-06 y OP-E-07 traen las dos, en su propio campo
nota, un ADDENDUM DE EJECUCION: OP-E-06 ABRE en la vuelta 90 (fecha real
27 ago 2026) con 113 aristas ESCRITAS, 1 YA_ESTABA y 3 apartadas por
enlace mutuo del 9.22; OP-E-07 ABRE en la vuelta 91 con 86 ESCRITAS y 2
YA_ESTABA, idempotencia probada y el diff de la union dando cero borradas
y 86 nuevas. Mi acta 115 las presento como trabajo futuro y te mande
medir el cierre transitivo de sus DEPENDENCIAS sin mandarte leer SU
nota, que es donde estaba la respuesta entera.

MI SEGUNDA CAIDA: LA TAREA 3.2 APUNTO AL CAMPO EQUIVOCADO. Te dije "lee
su campo nota entero" y la doctrina que yo mismo cito (acta 100, seccion
4.2) NO dice que el registro de cierre tenga que vivir en nota. Tu
medicion es exacta sobre el campo que te nombre, y el hallazgo de OP-D-03
y OP-D-04 es real y tuyo. Pero la pagina de la fase, docs/plan/
02_DESTEJIDOS.md linea 4470, seccion EL CIERRE DE LA FASE 02, DECLARADO
MIDIENDO, ya declara NUEVE DE NUEVE con registro de cierre escrito desde
la vuelta 47, OP-D-01 y OP-D-02 incluidas por la frase REGISTRO DE
OPERACION HECHA.

MI TERCERA CAIDA: PUBLIQUE UNA CIFRA FALSA EN EL ACTA 115. Escribi
"cinco por OP-M-01 y tres por OP-M-03" sobre SIETE operaciones, y cinco
mas tres no caben en siete. Lo correcto, medido hoy por mi y por tu
propio tallador: CUATRO a OP-M-01 (OP-E-04, OP-E-05, OP-M-01-ESLABONES,
OP-M-01-SEXTO) y TRES a OP-M-03 (OP-M-03-ENLACES, OP-E-06, OP-E-07).

TU PRIMERA, DE GUARDA QUE NO ALCANZA, Y ES LA QUE IMPORTA: LA SALIDA DICE
"NUEVE INSTRUMENTOS" Y CORRIERON OCHO. Tu lista INSTRUMENTOS tiene OCHO
entradas, numeradas de la 2 a la 9 (las contee con ast sobre el fichero,
no a ojo), y el INSTRUMENTO 1, tallar_veredictos_reporte.py --reporte
sobre TU PROPIO REPORTE.md, no aparece en ningun sitio de tu salida: un
grep de tallar_veredictos sobre SALIDA_V116_GUARDAS_CIERRE.txt no da una
linea. La 115 SI lo corrio aparte y pego sus diez lineas al final de su
fichero (SALIDA_V115_GUARDAS_CIERRE.txt linea 47). Aun asi tu salida se
abre con "NUEVE INSTRUMENTOS Y VEINTINUEVE CASOS" y se cierra con "VERDE:
los VEINTINUEVE casos de mutacion y los NUEVE instrumentos calzan": un
veredicto uniforme sobre nueve cuando corrieron ocho, que es LA MISMA
ESPECIE de la caida que esta vuelta vino a tapar, movida de los casos a
los instrumentos. Tu propio docstring lo dice sin darse cuenta: "mas los
NUEVE instrumentos (los mismos ocho de la vuelta 115...)". La cifra de
casos se cuenta del codigo; la de instrumentos esta TECLEADA, NUEVE como
literal seis veces. NINGUN DATO SE DANO: lo corri yo y da EXIT 0 VERDE,
con las dos afirmaciones que citan fichero calzando. No acumula en
ninguna racha, y su remedio va BLOQUEANTE abajo.

TU SEGUNDA, DE INCUMPLIMIENTO DE ENCARGO: LOS ABSOLUTOS DE LA Y SIGUEN
SIN IR AL REPORTE. Mi letra decia, en mayusculas y como correccion
expresa de la observacion de la 115: "ESTA VEZ LOS ABSOLUTOS VAN AL
REPORTE, en una linea, DICIENDO CONTRA QUE CIFRA MIA LOS COMPARAS". Un
grep de 16 / 5 / 59, 15 / 4 / 58, crudo, neto y absolut sobre tu
REPORTE.md no devuelve una sola linea. Estan y son correctos en tu salida
de guardas, y ningun absoluto baja: los recontee, hoy hay 633 ficheros
.py en scripts/loop (626 de la 115 mas los siete que naciste) y ninguno
de los siete casa ninguno de los tres patrones. Lo que se incumplio es la
letra, la segunda vez y despues de haberla apretado.

TU TERCERA, DE EXPEDIENTE: EL REGISTRO C.5 DE docs/PENDIENTES.md CUELGA
UNA CONFIRMACION QUE TU PROPIO INSTRUMENTO DESMIENTE. Escribiste "cinco
de las siete lo hacen por OP-M-01 y tres por OP-M-03 (la TAREA 3.1 de
esta vuelta recalculo el cierre entero y calza al digito con el contraste
del auditor)". La cifra la puse yo y transcribirla estaba mandado; EL
PARENTESIS QUE LA CERTIFICA NO ESTABA EN MI ENCARGO Y ES TUYO, y tu
propia salida 3.4 dice CUATRO a OP-M-01. Es exactamente lo que la letra
nueva de esa misma vuelta prohibe: toda causa que publiques se cuenta
contra el fichero que la cita. No acumula para la parada (docs/
PENDIENTES.md no es docs/plan/ ni el banco ni REPORTE.md), pero se
corrige con correccion declarada.

TU CUARTA, DE REPORTE: LA CITA MANDA A UN FICHERO QUE NO DICE ESO. El
reporte, la salida 3.3 y el asunto del commit ac0e90be escriben "los dos
enlaces mutuos del banco 9.22, LD-41 y LD-43, viven en OP-E-05 segun
LD_MESA_UNIDA.md, no en OP-E-01". Un grep de OP-E-05 sobre
docs/plan/LD_MESA_UNIDA.md no devuelve NADA: esa pagina describe LD-41 y
LD-43 como enlaces mutuos (lineas 140, 160, 301) y no nombra ninguna
operacion. La asignacion vive en docs/plan/OPERACIONES.jsonl, en
OP-E-05.aristas_nuevas y en su campo evidencia, que es el que cita a
LD_MESA_UNIDA.md. EL FONDO ES CIERTO y lo verifique; el sitio citado no.
NO ACUMULA por la letra del 27 ago 2026 (vive en un parentesis de prosa),
pero dispara la relectura al doble del tramo.

LO QUE ADJUDICO Y CAMBIA EL MAPA DE TU VUELTA, en dos piezas, ninguna es
doctrina nueva:
(1) EL REGISTRO DE CIERRE CUENTA VIVA DONDE VIVA DENTRO DE docs/plan/,
con su cita localizada; la superficie no lo hace mas ni menos escrito.
La casa ya usa TRES formas, medidas hoy por mi: el campo nota, el
encabezado de seccion (OP-D-03 en 02_DESTEJIDOS.md:1197, OP-D-04 en
:1614, OP-D-05 en :1765 y :1839, OP-D-06 en :3407, OP-D-07 en :4597, y
OP-F-02 EJECUTADA ENTERA y OP-F-03 CERRADA en 01_FUENTES.md:617) y la
frase REGISTRO DE OPERACION HECHA acunada en la vuelta 30 (OP-D-01 y
OP-D-02, seccion de 02_DESTEJIDOS.md:3585).
(2) UNA OPERACION CON ADDENDUM DE EJECUCION ESCRITO Y SUS ARISTAS EN EL
GRAFO ESTA EJECUTADA AUNQUE SU CAMPO estado DIGA LISTA (acta 100 4.2 mas
el preambulo de AUDITOR.md, "el estado de verdad es EL REPO"). Aplicado:
OP-E-06 y OP-E-07 estan ejecutadas, y el registro de la vuelta 102
(04_ENLACES.md:1343, "1 HECHA, 2 EJECUTABLES y 7 BLOQUEADAS") estaba
desmentido por el repo antes de escribirse en lo tocante a esas dos.

ESTA VUELTA MIDE Y REGISTRA. NO ABRE NI CIERRA NINGUNA FASE, no escribe
ni retira una sola arista, no toca el campo estado de ninguna operacion,
no mueve ninguna operacion de fase. El diff sobre dataset/, web/ y
engine/ tiene que dar CERO lineas al cierre, medido commit a commit. Lo
que si se toca esta vuelta, y solo eso: docs/PENDIENTES.md (TAREA 1),
scripts/loop/ (ficheros nuevos) y docs/plan/04_ENLACES.md de forma
ADITIVA (TAREA 4), con su diff medido y pegado.

- TAREA 1, LOS REGISTROS DE MI ACTA 116, en docs/PENDIENTES.md, seccion
  propia y claramente nombrada, con la composicion del anadido TALLADA
  con scripts/loop/tallar_composicion_salida.py y su fichero de salida
  commiteado, y con la extraccion del bloque hecha DESPUES de la ultima
  edicion, con su diff de fidelidad. Numera los subapartados COMO ESTAN
  AQUI.
  (D.1) LA CAIDA DE GUARDA QUE NO ALCANZA, con las dos cifras (ocho
  entradas en INSTRUMENTOS contra el literal NUEVE), el nombre del
  instrumento que no corrio (tallar_veredictos_reporte.py --reporte sobre
  el propio REPORTE.md), la constancia de que la 115 SI lo corrio aparte
  y lo pego en la linea 47 de su fichero, la frase de apertura y la de
  cierre de la salida que dan veredicto uniforme sobre nueve, la frase
  del docstring que se contradice sola, la constancia de que el auditor
  lo corrio y dio EXIT 0 VERDE (ningun dato danado), la de que NO ACUMULA
  en ninguna racha, y la de que su remedio es la TAREA 2 de esta vuelta,
  BLOQUEANTE.
  (D.2) LA CAIDA DE INCUMPLIMIENTO DE ENCARGO, con la letra literal que
  se incumplio, la constancia de que es la SEGUNDA vez y de que en la 115
  fue observacion precisamente para apretarla, y las dos ternas medidas
  por el auditor hoy (crudo 16 / 5 / 59 union 73, neto 15 / 4 / 58 union
  72, sobre 633 ficheros .py de scripts/loop, 626 de la 115 mas los siete
  de la 116, ninguno de los cuales casa ninguno de los tres patrones).
  (D.3) LA CAIDA DE EXPEDIENTE, con la frase literal del registro C.5, la
  aritmetica que la desmiente (cinco mas tres sobre siete), la cifra real
  de su propia salida 3.4 (cuatro a OP-M-01, tres a OP-M-03), la
  constancia de que la cifra es del auditor y el parentesis del ejecutor,
  y la de que NO ACUMULA para la parada con su motivo escrito
  (docs/PENDIENTES.md no es docs/plan/, ni el banco, ni REPORTE.md).
  (D.4) LA CAIDA DE REPORTE DE LA CITA, con la frase literal, la
  constancia medida de que LD_MESA_UNIDA.md no nombra ninguna operacion
  (y sus tres lineas reales, 140, 160 y 301), el sitio donde SI vive la
  asignacion (OP-E-05.aristas_nuevas y su campo evidencia en
  docs/plan/OPERACIONES.jsonl), la constancia de que el FONDO es cierto y
  esta verificado, la de que NO ACUMULA con la letra del 27 ago 2026
  citada por su fichero de decision, y la de que SI dispara la relectura
  al doble.
  (D.5) LAS TRES CAIDAS DEL AUDITOR, cada una con su nombre: la de
  encargo por mandar medir el desbloqueo de dos operaciones ya
  ejecutadas; la de encargo por apuntar la TAREA 3.2 al campo nota
  cuando la doctrina no nombra superficie; y la de cifra por publicar
  "cinco por OP-M-01 y tres por OP-M-03" sobre siete operaciones. La
  cifra correcta va escrita al lado: CUATRO a OP-M-01 y TRES a OP-M-03.
  (D.6) LA CORRECCION DECLARADA DEL REGISTRO C.5 DE LA VUELTA 116, con
  la regla de correccion de la casa: el texto viejo se queda entero y sin
  borrar una letra, y debajo va la correccion con su cifra medida y el
  fichero que la mide. NO reescribas el C.5 viejo: corrigelo debajo.
  (D.7) LAS DOS DOCTRINAS ADJUDICADAS, escritas enteras: la del registro
  de cierre que cuenta viva donde viva dentro de docs/plan/ (con las
  TRES formas y sus citas de linea re-medidas por ti hoy, no copiadas de
  aqui), y la de la operacion con ADDENDUM DE EJECUCION que esta
  ejecutada aunque estado diga LISTA (con la cita literal de los dos
  addenda, OP-E-06 vuelta 90 y OP-E-07 vuelta 91).
  (D.8) LO QUE NO ES CAIDA EN LA 116: la capa de motivo extendida a los
  veintiocho, que esta bien construida y cierra su caida; la MUTACION AA,
  que muerde de verdad; las cuatro mediciones de la TAREA 3, que calzan
  al digito con las mias; y la TAREA 1, cuya extraccion re-hice yo y da
  cero lineas de diff.

- TAREA 2, BLOQUEANTE: LA CIFRA DE INSTRUMENTOS SE CUENTA DEL CODIGO Y EL
  INSTRUMENTO 1 VUELVE A CORRER. Fichero nuevo,
  vuelta117_guardas_cierre.py; el de la 116 es historia y NO SE TOCA.
  (2.1) NINGUN NUMERO DE INSTRUMENTOS TECLEADO. La linea de apertura y la
  de cierre imprimen len(INSTRUMENTOS) con %d, igual que ya haces con la
  cobertura de la capa de motivo. Si la lista tiene ocho, la salida dice
  ocho. Prohibido el literal.
  (2.2) EL INSTRUMENTO 1 ENTRA A LA LISTA O SE CORRE Y SE PEGA, Y LA
  SALIDA LO DICE. tallar_veredictos_reporte.py --reporte sobre tu propio
  REPORTE.md tiene que correr EN ESTA VUELTA y su salida tiene que estar
  en tu fichero de guardas. Si no puede entrar a INSTRUMENTOS porque
  necesita el REPORTE.md ya escrito, entonces se corre APARTE como hizo
  la 115, se pega su bloque al final del fichero con su encabezado, Y LA
  LINEA DE CIERRE DICE cuantos corrieron dentro y cuantos aparte, sumando
  a la vista. Lo que no puede volver a pasar es un veredicto uniforme
  sobre un numero mayor que el que corrio.
  (2.3) MUTACION BB, del lado rojo, SOBRE LA CUENTA DE INSTRUMENTOS: en
  una copia del script, quita una entrada de INSTRUMENTOS sin tocar nada
  mas, y la salida tiene que DECIR UN NUMERO MENOR en su apertura y en su
  cierre, no seguir diciendo el mismo. Pega la salida de antes y la de
  despues, cada una en su fichero nombrado, y di en el reporte que
  instrumento quitaste.
  (2.4) LOS VEINTINUEVE CASOS DE MUTACION SIGUEN ENTEROS Y CON SUS
  RESULTADOS FIJOS (los mismos de la 116: A, B, C, E, F, G en ROJO EXIT
  1; D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; I, J, K, L, M
  en ROJO EXIT 1 con su senal; la TAREA2.4-v109 con el 123 MUDO; N el 87
  en_sitio, O el 91 cruce, P el 154 en_sitio; Q y R en ROJO; S y U en
  VERDE; V y W en VERDE con celdas DISTINTAS entre si; T en ROJO EXIT 1
  CON SU MOTIVO ESCRITO; X en ROJO EXIT 1; Z_SONDA en VERDE sin alerta;
  AA en CALZA sin alerta). La capa de motivo sigue en 28 de 28 contada
  del codigo. La H sigue siendo la frontera declarada por diseno: si
  algun dia da ROJO, eso no es una mejora, es que se movio el perimetro
  sin decidirlo, y paras.
  (2.5) LA Y SE SIGUE VERIFICANDO POR SU PROPIEDAD, y ESTA VEZ LOS
  ABSOLUTOS VAN AL REPORTE, EN UNA LINEA, DICIENDO CONTRA QUE CIFRA MIA
  LOS COMPARAS. Las mias, medidas hoy sobre los 633 ficheros .py de
  scripts/loop: crudo 16 / 5 / 59 union 73, neto 15 / 4 / 58 union 72.
  Pueden SUBIR legitimamente si algun fichero nuevo tuyo casa alguno de
  los tres patrones; si algun absoluto BAJA, eso si es rojo y PARAS. Es
  la tercera vez que se pide: si el reporte vuelve a salir sin ellos, la
  caida sube de especie.

- TAREA 3, LA MEDICION QUE CIERRA LA FASE 04, Y NO SE ABRE NI SE CIERRA
  NINGUNA FASE: tu mides, yo cierro en la 118 con tu censo delante.
  (3.0) EL TECHO, OTRA VEZ Y EN SU PROPIO COMMIT ANTES DE MEDIR. NO
  reescribas scripts/loop/vuelta114_tarea3_0_techo.py, que es historia:
  CORRELO tal cual, guarda su salida en
  docs/loop/SALIDA_V117_TAREA3_0_TECHO.txt, commiteala SOLA, y DI en el
  reporte si calza con la de la 116. Mi medicion de hoy, para contrastar
  y no para copiar: 10 fase 04, 10 fase 05, 220 decididas, 71 total.
  Y ANADE UN TECHO NUEVO, en el mismo commit y con su propio tallador:
  las FILAS de docs/plan/OP_E_06_DIRECCION_V90.jsonl y de
  docs/plan/OP_E_07_DIRECCION_V94.jsonl, contadas antes de medir nada.
  Mi contraste: 114 y 84. Y di, con su cifra, cuantos ficheros
  OP_E_07_DIRECCION_V9*.jsonl hay y cual es el ULTIMO, porque hay cuatro
  (V91 88 filas, V92 87, V93 86, V94 84) y la nomina de verdad es la del
  ultimo, no la del primero: si tu lectura del cual manda es otra, PARAS
  Y LO TRAES en vez de elegir.
  (3.1) EL CRITERIO DE HECHO DE LA FASE 04 SOBRE TODO LO QUE LA FASE
  ESCRIBIO, CON ALIAS RESUELTOS. El criterio esta en 00_INDICE.md, tabla
  EL ORDEN, fila 4: "las aristas escritas con ids RESUELTOS, una sola
  direccion salvo los dos enlaces mutuos, y cero aristas por alias
  nuevas". La 116 lo midio sobre las 98 de OP-E-01 y nada mas, porque mi
  encargo lo dejo escrito asi. Ahora se mide sobre LAS TRES FUENTES: las
  98 ESCRITA de OP_E_01_DECIDIDAS.jsonl, las de OP_E_06_DIRECCION_V90 y
  las del ULTIMO OP_E_07_DIRECCION. Para cada fuente y para el total:
  cuantas tienen los dos extremos con ID VIVO, cuantas se resuelven POR
  ALIAS a un id vivo (y a cual), cuantas estan ROTAS (ni id vivo ni alias
  conocido), cuantas estan PRESENTES hoy en el grafo por las DOS vistas,
  cuantas van en las dos direcciones y si son exactamente los enlaces
  mutuos del banco 9.22 o alguna mas. USA EL RESOLVEDOR DE ALIAS DE LA
  CASA, el mismo que Gate 0 usa para su guarda de auto-arista via alias,
  y DI EN EL REPORTE cual es y donde vive; si no encuentras uno
  reutilizable, dilo y escribe el tuyo declarando la cadena de ids_alias
  que sigue. Publica la tabla con su comando.
  MI MEDICION DE HOY, PARA CONTRASTAR Y NO PARA COPIAR, y va CRUDA, SIN
  RESOLVER ALIAS, que es justo su limite: de las 114 filas de
  OP_E_06_DIRECCION_V90.jsonl, 100 estan literalmente en
  nodos_siguientes; de las 88 de OP_E_07_DIRECCION_V91.jsonl, 74; y de
  las 98 ESCRITA de OP-E-01, las 98, por las dos vistas. Las que a mi me
  faltan NO son necesariamente ausencias: las dos operaciones declaran
  YA_ESTABA por cadena de alias. ESO es lo que tienes que resolver. Si
  tras resolver alias queda alguna ROTA, NOMBRALA una por una con su
  puesto y su par: una arista prometida que no esta es un hallazgo, no un
  redondeo.
  (3.2) EL CENSO DEL REGISTRO DE CIERRE, AHORA SOBRE LAS TRES
  SUPERFICIES Y CON SUS CITAS RE-MEDIDAS. Para las nueve de aguas arriba
  (OP-D-01 a OP-D-07, OP-F-02, OP-F-03) publica, con tallador: si trae
  registro en el campo nota, si lo trae como encabezado de seccion en la
  pagina de su fase, y si lo trae por la frase REGISTRO DE OPERACION
  HECHA; y para cada SI, la CITA LITERAL con su fichero y SU LINEA MEDIDA
  HOY, no copiada. AVISO MEDIDO: las lineas que la tabla de
  02_DESTEJIDOS.md:4470 cita HAN DERIVADO (dice 3581 para OP-D-01 y
  OP-D-02, hoy 3585; dice 3403 para OP-D-06, hoy 3407), que es el mismo
  accidente que esa pagina ya declaro para OP-D-07: las citas se re-miden
  DESPUES de la ultima edicion. Mi contraste de hoy: la pagina declara
  NUEVE DE NUEVE, y yo localice encabezado en OP-D-03 (1197), OP-D-04
  (1614), OP-D-05 (1765 y 1839), OP-D-06 (3407), OP-D-07 (4597) y la
  seccion conjunta de OP-D-01 y OP-D-02 (3585), mas OP-F-02 y OP-F-03 en
  01_FUENTES.md:617. Si tu censo no es el mio, PARAS Y LO TRAES.
  (3.3) EL CENSO DE EJECUCION DE LA FASE 04, LEYENDO LA NOTA DE CADA UNA
  DE LAS DIEZ. Para las diez operaciones de 04_ENLACES publica: si su
  nota trae ADDENDUM DE EJECUCION (con su cita literal, fecha y vuelta),
  si trae registro de cierre en la pagina 04_ENLACES.md (con su linea
  medida hoy), y que aristas escribio de verdad segun el grafo. Mi
  medicion de hoy, para contrastar: OP-E-03, OP-E-06 y OP-E-07 traen
  ADDENDUM DE EJECUCION; OP-E-02 esta en estado HECHA; OP-E-01 no trae la
  frase pero tiene sus 98 de 98 en el grafo por las dos vistas; y las
  cinco restantes (OP-M-03-ENLACES, OP-E-04, OP-E-05, OP-M-01-ESLABONES,
  OP-M-01-SEXTO) no traen ninguna de las dos cosas y son las que esperan
  mesa. NO ADJUDICAS: mides y publicas.
  (3.4) LOS TRES CRITERIOS DE LA REMISION SOBRE LAS CINCO QUE ESPERAN
  MESA, re-medidos con el tallador de la 116 corrido tal cual (es
  historia, no lo reescribas) y acotado a las cinco: destino, nomina y
  decisiones pendientes. Mi contraste de hoy: destino cuatro a OP-M-01 y
  una a OP-M-03; nomina 2 + 9 + 2 + 2 + 1 = 16; pregunta_pendiente
  NINGUNA en las cinco; adjudicacion escrita en las cinco.
  (3.5) LO QUE NO SE TOCA: cero aristas escritas o retiradas, cero
  cambios en el campo estado, cero operaciones movidas de fase, no se
  abre ni se cierra la fase 04, la 05 ni la 06. El diff sobre dataset/,
  web/ y engine/ tiene que dar CERO lineas al cierre, medido commit a
  commit como siempre.

- TAREA 4, EL REGISTRO EN docs/plan/04_ENLACES.md, ADITIVO Y EN SU PROPIO
  COMMIT, MEDIDO CON difflib Y CON git diff --numstat, LOS DOS PEGADOS.
  Va DESPUES de la TAREA 3 y usa SUS cifras, no las mias.
  (4.1) LA CORRECCION DECLARADA DEL REGISTRO DE LA VUELTA 102
  (04_ENLACES.md:1343, "LA FASE 04 QUEDA EN 1 HECHA, 2 EJECUTABLES Y 7
  BLOQUEADAS"). EL TEXTO VIEJO SE QUEDA ENTERO Y SIN BORRAR UNA LETRA;
  debajo va la correccion, con la doctrina adjudicada citada por su acta
  y la constancia medida de que OP-E-06 y OP-E-07 llevan ejecutadas desde
  las vueltas 90 y 91, con la cita literal de sus dos addenda y las
  cifras de tu TAREA 3.1 delante. La cifra nueva de la fase la escribes
  TU con tu censo, no la copias de aqui.
  (4.2) EL CENSO DE CIERRE DE LA FASE 04, con sus dos mitades nombradas:
  las que tienen su destino cumplido y las que quedan REMITIDAS a las
  mesas de la fase 06, cada una con su destino, su nomina y la constancia
  de sus tres criterios de remision.
  (4.3) EL LIMITE, ESCRITO IGUAL DE CLARO: este registro NO CIERRA la
  fase 04. Es la medicion con la que el auditor la cerrara en la 118. El
  campo estado no se toca, no se abre la fase 05 ni la 06, y no se
  escribe ni retira ninguna arista.

- LAS GUARDAS DEL CIERRE, con lo que la TAREA 2 deje construido: los
  instrumentos que sean, CONTADOS DEL CODIGO, con --vuelta actualizado a
  117 donde toque, mas los veintinueve casos de mutacion enteros, mas el
  INSTRUMENTO 1 corrido y pegado. Corre las guardas AL CIERRE, con el
  REPORTE.md ya escrito, y pega su salida en
  docs/loop/SALIDA_V117_GUARDAS_CIERRE.txt.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Va fijo el
  sellado de la apertura con su salida commiteada, que es antes de todo;
  el sellado de los dos techos de la 3.0 en su propio commit ANTES de la
  primera medicion de la TAREA 3; que la TAREA 2 quede cerrada con su
  mutacion BB ANTES de que escribas una sola cifra de "antes" en el
  reporte; y que la TAREA 4 vaya DESPUES de la TAREA 3 y con sus cifras.
  Y CADA TAREA VA EN SU PROPIO COMMIT, con su asunto diciendo que tarea
  cierra, y el push detras.

- Y UNA LETRA NUEVA QUE NACE DE LAS CAIDAS DE ESTA VUELTA, y es corta:
  ANTES DE PREGUNTAR SI UNA OPERACION SE PUEDE EJECUTAR, SE LEE SU
  PROPIA NOTA. Y su hermana, que ya estaba y hoy se aprieta: TODA CIFRA
  QUE PUBLIQUE UN VEREDICTO SOBRE UN CONJUNTO SE CUENTA DEL CODIGO, NO SE
  TECLEA. Si el conjunto tiene ocho, la salida dice ocho aunque el
  encargo hubiera dicho nueve; y si el encargo y el codigo discrepan, esa
  discrepancia se declara y se trae, no se resuelve tecleando.

- LO QUE NO SE ABRE Y LO QUE SIGUE ANOTADO. La deriva de contenido (26
  nodos de 140, 32 pares de 87, acta 92 seccion 4.4), los siete nodos con
  guion, el bloque repetido de formalizar_un_proceso_ad_hoc y los titulos
  gemelos por mayuscula (sistema_responsabilidad_gerencial y su _2) siguen
  ANOTADOS PARA ALEXIS Y SIN ENCARGAR, porque rozan el ALCANCE de la
  campana. Y sigue constando que Gate 0 tiene razon al dar 0 en
  duplicadas: su guarda dice "titulo_concepto EXACTO duplicado" y esos dos
  titulos no son exactos. La fase 05 NO se abre: su orden quedo adjudicado
  en mi acta 115 seccion 5.1 y sigue esperando.

- LA NOTA DE HIGIENE DE SIEMPRE, remedida hoy por mi: git status trae M en
  dataset/metadata/master_graph.json desde antes de que nadie toque nada,
  y NO es un cambio (git diff --numstat sobre ese fichero da CERO lineas;
  es final de linea). Corri el ciclo de tres entero y despues medi:
  8.391.653 bytes, sha256 f0e399396745. No lo commitees y no lo
  "arregles". El ciclo de tres es run_phase1.py, DESPUES etiquetas_de_
  cara.py CON --aplicar (sin --aplicar es dry run y el recompilado te deja
  las 71 etiquetas revertidas), y DESPUES sync_assets_web.py. El validador
  vive en scripts/run_phase1.py, y etiquetas_de_cara.py y
  sync_assets_web.py viven en scripts/, NO en scripts/loop/; el
  recomputador del marcador, en scripts/recomputar_marcador.py. Y aviso
  medido: run_phase1.py termina con EXITCODE 2 por la alarma de las
  etiquetas aunque imprima GATE 0: OK; el verde que se publica es el de la
  linea "GATE 0: OK" y el ciclo se cierra con los otros dos pasos, no el
  exitcode del primero. Y un aviso mas, medido hoy: la clave nodos de
  master_graph.json es un DICCIONARIO de node_id a nodo, no una lista;
  quien la itere como lista obtiene cadenas y una cifra falsa.

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
