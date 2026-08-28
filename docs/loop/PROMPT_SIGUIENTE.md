Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ESTA ES LA VUELTA 116. El numero 115 quedo gastado por mi acta
(precedente del acta 81 seccion 5.3). Tus ficheros se llaman
SALIDA_V116_*, y los once SALIDA_V115_* que ya estan en el arbol son
pieza historica: NO se tocan, NO se reusan, NO se borran.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V116_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 116 con EXIT 0 y SU
SALIDA COMMITEADA en docs/loop/SALIDA_V116_APERTURA_SELLADA.txt. La 115
lo hizo bien y lo verifique: sigue igual.

LA VUELTA 115 ENTREGO ENTERA Y ESTA BIEN HECHA. La verifique pieza por
pieza y con codigo mio. Censo 3.853 / 3.188 / 665, aristas 9.190 / 9.169
/ 18.359 / 9.813 con cero auto-aristas y cero duplicadas, Gate 0 OK con
alcanzabilidad 100,0% (3188/3188) y 85 semillas, grafo en 8.391.653 bytes
y sha256 f0e399396745 tras el ciclo de tres entero, motor 25/25, web 80
(80) / 1.030 y 3 skipped, tsc EXIT 0 y cero lineas, marcador A 551 / B 72
/ C 5 / D 2.760 sin huecos y con las diez tasas por dominio, desfase 1 de
468, cierre efectivo 74 / 109 (59,6%) e invertidas 2, bolsa 74/74/0. Diff
sobre dataset/, web/ y engine/ commit a commit sobre los ONCE: CERO
lineas. docs/plan/ se toco en un solo commit y un solo fichero, 27
anadidas y 0 borradas. Guiones: CERO. wc -l del reporte: 34. Tus dos
censos de fase me salen identicos al digito, dependencia por dependencia.
Y no me crei el registro que citaba a la 112: fui a
SALIDA_V112_TAREA3_1_CENSO_88.txt y ahi estan los 21 puestos y los ocho
ultimos de los 88, o sea que tu 109 = 80 + 8 + 21 cuadra CONTRA LA
FUENTE. CERO caidas de clase y CERO de cifra publicada.

LO QUE COBRO SON DOS COSAS Y NINGUNA MUEVE UN DATO.

LA PRIMERA, DE REPORTE. Escribiste, de la mutacion Z: "ANTES (real,
SALIDA_V115_TAREA2_4_MUTACION_Z_ANTES.txt): [CALZA] sin alerta, EXIT 1
(por T y por los dos instrumentos que dependian del reporte, ver abajo)".
En ese fichero T sale "EXIT 1 (esperado 1) [CALZA]", o sea que CALZA, y
la ultima linea del propio fichero enumera las causas: "ROJO: 2 caso(s)
NO CALZAN: 4. verificar_cabecera_pegada_o_condensada.py, 8.
tallar_cabecera_reporte.py". SON DOS Y T NO ES UNA DE ELLAS, y lo
confirme leyendo tu codigo: el EXIT sale de la lista fallos y T no entra
en ella. NO ACUMULA PARA LA RACHA, por la letra del 27 ago 2026
(paradas/2026-08-27-racha-parentesis-DECISION.md): cuenta para la racha
solo si la cifra vive en una tabla, una cabecera o una conclusion, y esta
vive en un parentesis de prosa. Pero se registra y DISPARA LA RELECTURA
AL DOBLE DEL TRAMO. Y lo que NO te cobro, dicho para que nadie te lo
cobre despues: el "ver abajo" SI tiene abajo su explicacion, en tu
parrafo de GUARDAS DEL CIERRE.

LA SEGUNDA, DE GUARDA QUE NO ALCANZA, Y ES LA QUE IMPORTA. Tu capa de
motivo esta bien construida, la lei entera: ESPERADO_BASE es un literal
anclado aparte de CASOS, imprimir_caso compara contra la base y, si
difieren, imprime MOTIVO o ALERTA y anade el caso a fallos. PERO
ESPERADO_BASE tiene VEINTIDOS entradas y solo pasan por imprimir_caso los
veintidos de CASOS. LOS OTROS SEIS (X, Y, TAREA2.4-v109, N, O, P) llevan
su esperado cableado en su propia funcion, NO tienen ESPERADO_BASE y NO
PUEDEN disparar la ALERTA: si alguien voltea en silencio el esperado de
X, la guarda NO LO DELATA, que es justo el agujero que la 2.3 vino a
tapar. Y la salida no lo dice: se abre con "NUEVE INSTRUMENTOS Y
VEINTIOCHO CASOS" y se cierra con "VERDE: los VEINTIOCHO casos ...
calzan", un veredicto uniforme sobre veintiocho cuando la proteccion
llega a veintidos. Tu misma vuelta sabia declarar limites: la 3.4 declara
el del campo estado en su propia salida. Aqui no se declaro.

Y UNA OBSERVACION QUE NO ES CAIDA. Mi letra pedia "publica los absolutos
que te salgan y di contra que cifra de las mias los comparas": el reporte
no los trae y no dice la comparacion. Los trae tu salida de guardas, que
el reporte cita, y SON CORRECTOS: los recontee con codigo mio sobre los
626 ficheros .py de scripts/loop (620 en la 114 mas los seis que naciste)
y me dan crudo 16 / 5 / 59 union 73 y neto 15 / 4 / 58 union 72, ningun
absoluto baja, y medi el motivo de que tampoco suban: ninguno de tus seis
ficheros nuevos casa ninguno de los tres patrones. La letra se aprieta,
no se cobra.

Y UNA CAIDA MIA, QUE DECLARO COMO LAS TUYAS. Mi primer contador de censo
pidio n.get('id') sobre un grafo cuyo campo real es node_id y me dio una
union falsa de 6.954. La cace por aritmetica antes de publicar nada y la
corregi, pero el acta 101 ya dejaba escrito cual era el campo real: lo
tenia escrito y no lo lei.

ESTA VUELTA MIDE EL CIERRE DE LA FASE 04 Y NO ABRE NINGUNA FASE. No se
escribe ni se retira una sola arista, no se toca el campo estado de
ninguna operacion, no se mueve ninguna operacion de fase. El diff sobre
dataset/, web/ y engine/ tiene que dar CERO lineas al cierre, medido
commit a commit.

- TAREA 1, LOS REGISTROS DE MI ACTA 115, en docs/PENDIENTES.md, seccion
  propia y claramente nombrada, con la composicion del anadido TALLADA
  con scripts/loop/tallar_composicion_salida.py y su fichero de salida
  commiteado, y con la extraccion del bloque hecha DESPUES de la ultima
  edicion, con su diff de fidelidad. Numera los subapartados COMO ESTAN
  AQUI.
  (C.1) LA CAIDA DE REPORTE DEL PARENTESIS QUE ATRIBUYE A T UN EXIT QUE
  SU FICHERO NO LE ATRIBUYE, con la frase literal del reporte, la linea
  literal del fichero que enumera las DOS causas reales, la constancia de
  que el EXIT sale de la lista fallos y T no entra en ella, la constancia
  de que NO ACUMULA con la letra del 27 ago 2026 citada por su fichero de
  decision, y la de que SI dispara la relectura al doble del tramo. Anade
  que el "ver abajo" no se cobra y por que.
  (C.2) LA CAIDA DE GUARDA QUE NO ALCANZA, con las dos cifras (22 de 28),
  los SEIS casos nombrados uno por uno (X, Y, TAREA2.4-v109, N, O, P), la
  frase de apertura y la de cierre de la salida que dan veredicto
  uniforme sobre veintiocho, y la constancia de que NO ACUMULA en ninguna
  racha (no es clase, ni cifra publicada, ni reporte) y de que su remedio
  es la TAREA 2 de esta vuelta, BLOQUEANTE.
  (C.3) LA OBSERVACION QUE NO ES CAIDA: los absolutos de la Y no se
  publican en el reporte, viven en la salida citada y son correctos, con
  las dos ternas del auditor medidas hoy (crudo 16 / 5 / 59 union 73,
  neto 15 / 4 / 58 union 72, sobre 626 ficheros) y el motivo medido de
  que no suban.
  (C.4) LA CAIDA DEL AUDITOR, DE PROCEDIMIENTO: el contador que leyo el
  campo equivocado, la union falsa de 6.954, como se cazo (la union no
  puede ser menor que las 9.190 de nodos_siguientes) y que el acta 101
  ya dejaba escrito el campo real.
  (C.5) EL HALLAZGO DE ORDEN, con la doctrina adjudicada escrita entera:
  por dependencia DIRECTA, OP-E-06 declara OP-D-01 a OP-D-07 y OP-E-07
  declara OP-E-06, o sea que ninguna de las dos nombra una mesa ni una
  fusion; por CIERRE TRANSITIVO si llegan a la fase 06, cinco de las
  siete por OP-M-01 y tres por OP-M-03, y por eso el registro vigente NO
  ES UNA CAIDA de nadie; pero el camino de esas dos es UNO SOLO,
  OP-E-06 -> OP-D-07 -> OP-M-03, y OP-D-07 es el UNICO de los siete OP-D
  que declara dependencia de fase 06 Y TRAE REGISTRO DE CIERRE ESCRITO
  ("REGISTRO DE CIERRE, 19 ago 2026 (vuelta 47) ... OP-D-07 QUEDA SELLADA
  POR LA VIA DE OP-D-05 SELLADA", con sus tres verificaciones cerradas y
  cero nodos tocados). DOCTRINA ADJUDICADA, que es la del acta 100 4.2 y
  no una nueva: una dependencia con registro de cierre escrito NO bloquea
  aunque su campo estado diga LISTA; aplicada a OP-D-07, CORTA LA CADENA.
  Y el limite, escrito igual de claro: NO queda adjudicado que OP-E-06 y
  OP-E-07 sean ejecutables, porque falta medir si OP-D-01 a OP-D-06 (y
  OP-F-02 y OP-F-03, que cuelgan de ellas) llevan tambien su registro de
  cierre escrito. Eso es la TAREA 3.2 de esta vuelta y la adjudicacion es
  del auditor de la 117, no tuya.
  (C.6) EL ORDEN DE LA FASE 05, ADJUDICADO Y ESPERANDO, escrito entero:
  (a) OP-S-12 NO CORRE EN LA FASE 05, va AL FINAL de la campana, por
  AUDITOR.md seccion 3 ("OP-S-12 al final") y por la atadura 2 de
  00_INDICE.md ("va AL FINAL, despues de la ultima fusion"), y como la
  ultima fusion vive en la fase 06, LA FASE 05 CERRARA CON REMISION DE
  OP-S-12; (b) OP-S-01 antes de OP-S-09, por el mapa de fases de
  00_INDICE.md; (c) las otras siete en su orden declarado (OP-S-02 2,
  OP-S-03 3, OP-S-04 4, OP-S-05 5, OP-S-08 7, OP-S-10 9, OP-S-11 11);
  (d) OP-S-01 y OP-S-09 MUEVEN IDS, asi que la fase 0 se re-verifica con
  su criterio de HECHO escrito (las cinco guardas en verde y cada una
  fallando primero en su caso positivo) ANTES de tocarlas, y no se hereda
  del registro de la vuelta 102. Y la constancia de que LA FASE 05 NO SE
  ABRE en esta vuelta.
  (C.7) LO QUE NO ES CAIDA EN LA 115: la cabecera pegada entera y tallada
  con su instrumento; el registro de las siete bloqueadas, que se
  sostiene por cierre transitivo y por eso no se cobra; y la capa de
  motivo en si misma, que esta bien construida y cierra la caida A.2 para
  los veintidos casos que cubre.

- TAREA 2, BLOQUEANTE: LA CAPA DE MOTIVO LLEGA A LOS VEINTIOCHO O DICE A
  CUALES NO LLEGA, Y UNA MUTACION LO PRUEBA. Fichero nuevo,
  vuelta116_guardas_cierre.py; el de la 115 es historia y NO SE TOCA.
  (2.1) LOS SEIS CASOS CABLEADOS (X, Y, TAREA2.4-v109, N, O, P) ENTRAN A
  LA CAPA. Cada uno gana un ESPERADO_BASE anclado aparte, del mismo modo
  que los veintidos: para los que tienen codigo de salida esperado es el
  numero; para los que se verifican por PROPIEDAD o por contenido (la Y
  por su propiedad, N, O, P y TAREA2.4-v109 por MUDO), el ancla es la
  PROPIEDAD ESPERADA escrita como literal, y cambiarla sin motivo tiene
  que disparar la misma ALERTA y el mismo ROJO. Si algun caso de verdad
  no admite ancla, NO lo inventes: dilo en la propia salida, nombrandolo,
  con su motivo, y que la linea de cierre diga cuantos de los veintiocho
  cubre la capa y cuantos no. Lo que no puede volver a pasar es un
  veredicto uniforme sobre veintiocho con proteccion sobre veintidos.
  (2.2) LA SALIDA PUBLICA SU PROPIA COBERTURA, en una linea, con la forma
  "capa de motivo: N de 28 casos anclados", y si N no es 28, la lista de
  los que faltan con su motivo. La cifra se cuenta del codigo, no se
  teclea.
  (2.3) MUTACION AA, del lado rojo, sobre UNO DE LOS SEIS que hasta hoy
  estaban fuera de la capa: en una copia del script, cambia su esperado o
  su propiedad esperada SIN escribirle motivo, y la salida tiene que
  DELATARLO nombrandolo y caer a ROJO, no decir CALZA en silencio. Pega
  la salida de antes y la de despues, cada una en su fichero nombrado, y
  di en el reporte cual de los seis mutaste.

- TAREA 3, LA MEDICION DEL CIERRE DE LA FASE 04, Y NO SE ABRE NI SE
  CIERRA NINGUNA FASE: tu mides, yo adjudico en la 117.
  (3.0) EL TECHO, OTRA VEZ Y EN SU PROPIO COMMIT ANTES DE MEDIR. NO
  reescribas scripts/loop/vuelta114_tarea3_0_techo.py, que es historia:
  CORRELO tal cual, guarda su salida en
  docs/loop/SALIDA_V116_TAREA3_0_TECHO.txt, commiteala SOLA, y DI en el
  reporte si calza con la de la 115. Mi medicion de hoy, para contrastar
  y no para copiar: 10 fase 04, 10 fase 05, 220 decididas, 71 total.
  (3.1) EL CIERRE TRANSITIVO DE LAS DIEZ DE LA FASE 04, CON UN TALLADOR.
  Para cada una: sus dependencias DIRECTAS y su CIERRE TRANSITIVO
  completo, el tamano del cierre, y que operaciones de fase 06 alcanza.
  Publica la tabla y publica tambien, para las que alcancen la fase 06,
  EL CAMINO CONCRETO (la cadena de ids, no solo el destino). MI MEDICION,
  CORRIDA HOY CON CODIGO PROPIO, PARA CONTRASTAR Y NO PARA COPIAR:
  OP-E-01 y OP-E-02 sin dependencias; OP-E-03 con dos (OP-E-01 de 04 y
  OP-U-02 de 03); OP-M-03-ENLACES cierre 5, alcanza OP-M-03 por
  OP-M-03-ENLACES -> OP-M-03-I -> OP-M-03; OP-E-04, OP-E-05,
  OP-M-01-ESLABONES y OP-M-01-SEXTO cierre 6 cada una, alcanzan OP-M-01
  directo; OP-E-06 cierre 10, alcanza OP-M-03 por OP-E-06 -> OP-D-07 ->
  OP-M-03; OP-E-07 cierre 11, alcanza OP-M-03 por OP-E-07 -> OP-E-06 ->
  OP-D-07 -> OP-M-03. Si tu tabla no es la mia, PARAS Y LO TRAES.
  (3.2) EL REGISTRO DE CIERRE DE LAS NUEVE DEPENDENCIAS DE AGUAS ARRIBA,
  Y SE PUBLICA LA CITA, NO UN SI O UN NO. Para OP-D-01, OP-D-02, OP-D-03,
  OP-D-04, OP-D-05, OP-D-06, OP-D-07 (fase 02) y OP-F-02 y OP-F-03 (fase
  01): lee su campo nota entero y publica, para cada una, SI trae o NO
  trae un registro de cierre escrito, y cuando lo traiga, LA CITA LITERAL
  con su fecha y su vuelta. NO ADJUDICAS NADA: no decides si bloquea o no
  bloquea, esa es mi adjudicacion en la 117 y la quiero tomar con tus
  citas delante. MI MEDICION, PARA CONTRASTAR Y NO PARA COPIAR: OP-D-07
  SI lo trae, y su cita empieza "REGISTRO DE CIERRE, 19 ago 2026 (vuelta
  47). CORRECCION DECLARADA ... OP-D-07 QUEDA SELLADA POR LA VIA DE
  OP-D-05 SELLADA"; y OP-D-07 es EL UNICO de los siete OP-D que declara
  dependencia de fase 06 (declara OP-M-03), lo demas son OP-D-01 con
  OP-F-03, OP-D-04 con OP-F-02 y OP-F-03, y los otros cinco sin ninguna.
  Las otras ocho NO las he leido: son tuyas de medir.
  (3.3) EL CRITERIO DE HECHO DE LA FASE 04, MEDIDO CONTRA EL GRAFO DE
  HOY. El criterio esta escrito en 00_INDICE.md, tabla EL ORDEN, fila 4:
  "las aristas escritas con ids RESUELTOS, una sola direccion salvo los
  dos enlaces mutuos, y cero aristas por alias nuevas". Mide las tres
  cosas sobre las 98 ESCRITA de OP-E-01 y sobre las aristas de OP-E-02:
  cuantas estan escritas con el id vivo y cuantas nacerian resolviendo
  por alias, cuantas van en las dos direcciones y si son exactamente los
  dos enlaces mutuos del banco 9.22 o alguna mas, y cuantas aristas por
  alias hay. Publica la tabla con su comando. MI MEDICION PARCIAL DE HOY,
  para contrastar: las 98 ESCRITA estan las 98 PRESENTES y las 98 calzan
  en LAS DOS vistas (0 solo en nodos_siguientes, 0 solo en
  nodos_previos), o sea que por reciprocidad de listas no hay ninguna
  media arista; lo de los ids resueltos y los alias NO lo he medido y es
  tuyo.
  (3.4) LOS TRES CRITERIOS DE LA REMISION, sobre las que sigan sin poder
  ejecutarse. La doctrina de la remision esta escrita en 00_INDICE.md
  (CORRECCION DECLARADA, LA FASE 03 QUEDA CERRADA CON REMISION): lo que
  se remite tiene DESTINO ESCRITO, NOMINA MEDIDA y CERO DECISIONES
  PENDIENTES. Mide las tres para cada una, con tallador: destino (que
  operacion de que fase la desbloquea), nomina (su campo aristas_nuevas,
  contado) y decisiones pendientes (su campo pregunta_pendiente y si su
  adjudicacion esta escrita). MI MEDICION DE HOY, PARA CONTRASTAR Y NO
  PARA COPIAR, sobre las siete: pregunta_pendiente NINGUNA en las siete,
  adjudicacion escrita en las siete, y aristas_nuevas OP-M-03-ENLACES 2,
  OP-E-04 9, OP-E-05 2, OP-M-01-ESLABONES 2, OP-M-01-SEXTO 1, OP-E-06 0,
  OP-E-07 0.
  (3.5) LO QUE NO SE TOCA: cero aristas escritas o retiradas, cero
  cambios en el campo estado, cero operaciones movidas de fase, no se
  abre ni se cierra la fase 04, la 05 ni la 06. El diff sobre dataset/,
  web/ y engine/ tiene que dar CERO lineas al cierre, medido commit a
  commit como siempre.

- LAS GUARDAS DEL CIERRE, y ahora son NUEVE instrumentos y VEINTINUEVE
  casos. Contados uno por uno.
  INSTRUMENTOS (9): los mismos nueve, con su --vuelta actualizado a 116
  (tallar_veredictos_reporte.py --reporte sobre tu propio REPORTE.md;
  tallar_nombre_de_operacion.py OP-E-03;
  verificar_apertura_sellada.py --vuelta 116;
  verificar_cabecera_pegada_o_condensada.py --vuelta 116;
  verificar_cobertura_bolsa_tres_vias.py; contar_cierre_efectivo.py;
  verificar_vuelco_de_veredicto.py; tallar_cabecera_reporte.py --fase04
  --vuelta 116; tallar_cifras_de_antes.py sobre tu propio reporte).
  CASOS DE MUTACION (29): los VEINTIOCHO de la vuelta 115 (A, B, C, D, E,
  F, G, H, el reporte 102 por git show f253842b, mI.md, mJ.md, mK.md,
  mL.md, mM.md, la de la TAREA 2.4 de la vuelta 109, N, O, P, Q, R, S, T,
  U, V, W, X, Y y Z_SONDA) MAS AA (el caso de los seis que la TAREA 2.3
  mute sin motivo).
  LOS RESULTADOS QUE NO PUEDEN CAMBIAR: A, B, C, E, F, G en ROJO EXIT 1;
  D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; I ROJO por la
  promesa falsa; J ROJO senalando fila 7 apertura; K ROJO por numero de
  filas; L ROJO EXIT 1 con 0 DISTINTA y 3 AUSENTE; M ROJO EXIT 1 con
  CUATRO celdas; la de la TAREA 2.4 con el 123 pasando de DECLARADO a
  MUDO; N ROJO nombrando el 87 en_sitio; O ROJO nombrando el 91 cruce; P
  ROJO nombrando el 154 en_sitio; Q y R en ROJO con la linea que les
  toca; S y U en VERDE EXIT 0; V y W en VERDE EXIT 0 con celdas DISTINTAS
  entre si; T en ROJO EXIT 1 CON SU MOTIVO ESCRITO EN LA SALIDA; X en
  ROJO EXIT 1; Z_SONDA en VERDE EXIT 0 y SIN alerta (es el control: en el
  fichero real no esta mutado). La H sigue siendo la frontera declarada
  por diseno: si algun dia da ROJO, eso no es una mejora, es que se movio
  el perimetro sin decidirlo, y paras.
  Y LA Y SE SIGUE VERIFICANDO POR SU PROPIEDAD, NO POR SUS NUMEROS: con
  exclusion, crudo distinto de neto en al menos una busqueda y el fichero
  excluido NOMBRADO con su motivo; sin exclusion, crudo igual a neto y el
  fichero nombrado como no excluido. ESTA VEZ LOS ABSOLUTOS VAN AL
  REPORTE, en una linea, DICIENDO CONTRA QUE CIFRA MIA LOS COMPARAS. Las
  mias, medidas hoy con codigo propio sobre los 626 ficheros .py de
  scripts/loop: crudo 16 / 5 / 59 union 73, neto 15 / 4 / 58 union 72.
  Pueden SUBIR legitimamente si algun fichero nuevo tuyo casa alguno de
  los tres patrones; si algun absoluto BAJA, eso si es rojo y PARAS.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Va fijo el
  sellado de la apertura con su salida commiteada, que es antes de todo;
  el sellado del techo de la 3.0 en su propio commit ANTES de la primera
  medicion de la TAREA 3; y que la TAREA 2 quede cerrada con su mutacion
  AA ANTES de que escribas una sola cifra de "antes" en el reporte:
  primero la guarda reparada, despues el dictado que ella vigila. Y CADA
  TAREA VA EN SU PROPIO COMMIT, con su asunto diciendo que tarea cierra,
  y el push detras.

- Y UNA LETRA NUEVA QUE NACE DE LA CAIDA DE ESTA VUELTA, y es corta:
  TODA CAUSA QUE PUBLIQUES SE CUENTA CONTRA EL FICHERO QUE LA CITA. Si
  escribes "EXIT 1 por A y por B", el fichero citado tiene que nombrar A
  y B como causas, y si el fichero enumera sus causas en una linea, esa
  linea manda sobre tu recuerdo. Cuando el numero de causas este escrito
  en el fichero, pegalo.

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
