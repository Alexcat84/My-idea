Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), en REGIMEN COMPLETO, con las
guardas obligatorias por operacion.

El acta que te encarga esto es ACTA_AUDITOR.md, VUELTA 153. Su veredicto:
la 152 entrega las seis tareas y casi todo reproduce al digito con mi
instrumento (censo, aristas, ciclo entero con numstat en cero filas, Gate
0 en 26 de 26, motor 25/25, vitest 80 y 1.030 con 3 saltadas, tsc exit 0,
cabecera identica al tallador con 9 filas y 0 distintas, registro en 153
entradas y 153 pares distintos, 3.388 veredictos, 83 del mergebase, 307
destinos sobre 255 nodos, 71 fichas con 18 claves, tabla por fase 4/4/0 y
expediente 48/26/22/0/0). La ciega dio OCHO A FAVOR Y CERO DISCREPAN, y
en el 042 viste algo que yo no vi. Los seis discutibles y las cuatro
preguntas quedan TODOS adjudicados en la seccion 6 del acta. Pero hay un
hallazgo fuera de lo marcado y es de los que importan, y por el EL
CREDITO DE LA TANDA BAJA y el tramo del registro de citas SE RELEE AL
DOBLE. LA RACHA DE CIFRA PUBLICADA QUEDA EN UNO: dos seguidas son PARADA.

- TAREA 1, LOS REGISTROS, Y ES LO PRIMERO: deja escritas en el repo las
  nueve adjudicaciones de la seccion 6 del acta 153 donde cada una vive
  (6.1 y 6.2 en el instrumento de la relectura, 6.3 en la ficha de las
  mesas, 6.6 en el arnes de la tabla por fase, 6.7 en la guarda del
  corredor, 6.8 y 6.9 donde corresponda), TODAS POR ADICION Y CON
  CORRECCION DECLARADA, sin borrar una linea del texto viejo.

- TAREA 2, Y ES BLOQUEANTE, LA GUARDA DE OP-C-05 ESTA VERDE SOBRE UN
  UNIVERSO INCOMPLETO. Esto no es una opinion mia: esta medido y la
  aritmetica lo cierra sola.
  LO QUE LA GUARDA HACE HOY: recorre los nodos ACTIVOS y de cada uno lee
  SOLO su lista nodos_siguientes. Resuelve el DESTINO, pero LA FUENTE NO
  LA RESUELVE NUNCA (el nodo de partida ya es vivo por construccion), y
  NO LEE nodos_previos.
  LO QUE ESO CUESTA, MEDIDO CON RESOLUTOR PROPIO SOBRE EL MISMO ARBOL:
  con la vara de la guarda salen 153 pares y 0 sin cita; con fuentes
  vivas y LOS DOS CAMPOS salen 154 y 1 SIN CITA; con todas las fuentes y
  solo nodos_siguientes salen 155 y 2 SIN CITA; con todas las fuentes y
  los dos campos salen 157 y 4 SIN CITA.
  EL PAR QUE NO NECESITA NINGUNA DISCUSION ES error_proofing_servicio
  contra metodologia_6s: los dos VIVOS, y las dos direcciones las declara
  EL PROPIO metodologia_6s dentro de sus dos listas (nodos_siguientes
  trae mistake_proofing_poka_yoke y nodos_previos trae
  errores_a_prueba_poka_yoke, y los dos resuelven a
  error_proofing_servicio). NO HACE FALTA ADMITIR FUENTES DEPRECADAS NI
  NINGUNA VARA ANCHA. No esta en el registro y Gate 0 esta en verde.
  Y LA ARITMETICA LO CIERRA CON LA CIFRA QUE TU MISMO ACABAS DE
  CORREGIR EN LA TAREA 4: las relaciones de ida y vuelta declaradas
  dentro de un nodo vivo son 307 sobre 255 nodos; 306 son mutuas y 306
  entre dos son exactamente los 153 pares que la guarda cuenta; QUEDA UNA
  DECLARADA POR UN SOLO LADO, y es esa. 307 es impar y ese uno es el
  agujero.
  LO QUE HAY QUE HACER, EN ESTE ORDEN:
  (2.a) UN INSTRUMENTO TUYO, escrito hoy, mide el universo con las cuatro
  varas de la tabla de arriba y PUBLICA LAS CUATRO CIFRAS, no solo la que
  te convenga. Si tus cuatro no dan 153/154/155/157, PARAS Y LO TRAES: o
  mi medicion o la tuya esta mal y eso se resuelve antes de tocar la
  guarda.
  (2.b) SE DECLARA LA VARA. La vara de arista de esta campaña son LOS DOS
  CAMPOS y esta escrita en tres sitios: la cabecera cuenta 8.740
  nodos_previos y la union de 9.914 sale de los dos, Gate 0 tiene una
  comprobacion de simetria que los trata como dos vistas de la misma
  arista, y web/lib/engine/planRedactor.ts linea 96 recorre los dos
  juntos como vecinos. Mas P.1, que manda resolver antes de contar. SI
  DECIDES UNA VARA MAS ESTRECHA QUE ESA, NO LA APLICAS: LA TRAES.
  (2.c) LOS PARES QUE LA VARA NUEVA DESTAPE VAN A LECTURA DIRIGIDA POR
  P.5, con su entrada en el registro y SIN MOVER n. Si alguno no lo
  cubren las dos vias de la decision del fundador y la lectura dirigida
  no puede resolverlo, PARAS Y LO TRAES: no lo metes en el registro para
  que la guarda encienda.
  (2.d) LA GUARDA SE ENSANCHA AL UNIVERSO DECLARADO, con CASO POSITIVO
  POR MUTACION QUE MUERDA POR EL LADO QUE HOY ES CIEGO: una arista
  bidireccional metida SOLO por nodos_previos de un nodo vivo tiene que
  TUMBAR Gate 0 nombrando el par. Sobre copia, con dataset/ identico
  antes y despues comprobado por sha256. Y CONTRAPRUEBA OBLIGATORIA: la
  guarda VIEJA sobre esa misma mutacion tiene que salir VERDE. Si sale
  roja, tu mutacion no ataca el punto ciego y no prueba nada.
  (2.e) CORRECCION DECLARADA de la cifra en SUS DOS SEDES, por adicion y
  sin borrar el texto viejo: la nota de OP-C-05 en
  docs/plan/OPERACIONES.jsonl y los comentarios de la guarda en
  scripts/run_phase1.py. La segunda es la CUARTA SEDE DE CIFRA PUBLICADA
  que el fundador creo el 2 sep 2026 y esta escrita HOY, asi que la falta
  de retroactividad no la salva.
  (2.f) Y EL estado DE OP-C-05 SE REVISA AL FINAL, no al principio: su
  verificacion 8 ("cero pares bidireccionales entre vivos SIN CITA
  REGISTRADA") NO ESTA CONTESTADA hoy. Cuando lo este, se dice; si al
  cerrar sigue sin estarlo, la ficha vuelve a LISTA con su correccion
  declarada y se dice tambien.

- TAREA 3, LA RELECTURA AL DOBLE DEL TRAMO, que es lo que la regla del
  credito manda cuando aparece un hallazgo fuera de lo marcado. El tramo
  es EL REGISTRO DE CITAS DE OP-C-05. Al doble quiere decir: una segunda
  lectura independiente de una MUESTRA DOBLE de las 121 lecturas
  dirigidas (no menos de 32, elegidas POR COMPUTO y no a dedo, con la
  zancada escrita en la salida), imprimiendo primero los pasos y
  adjudicando antes de destapar la razon escrita. Publicas cuantas
  coinciden y cuantas discrepan. LAS QUE DISCREPEN NO SE ARREGLAN
  CALLANDO: se traen con su caso escrito.

- TAREA 4, LAS DOS VARAS DE LA RELECTURA DEL EXPEDIENTE, POR LA
  ADJUDICACION 6.1 Y 6.2.
  (4.a) LA P3 DEJA DE CONTAR MENCIONES. La vara ya existe y es EL
  CRITERIO DE HECHO de docs/plan/08_VERIFICACION.md: "UNA FASE ESTA HECHA
  CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA. No cuando pasa
  verde: cuando se CAERIA." Un commit que NOMBRA una operacion no hace
  que ninguna verificacion se caiga. La P3 pasa a contar commits que
  tocan dataset/, web/ o engine/ en la nomina de la ficha, o el caso
  positivo de la ficha corriendo en rojo antes y en verde despues. CON SU
  CASO POR MUTACION: el commit c9c6ea40 (el que dice que OP-V-01 y
  OP-L-01 NO tienen prueba) tiene que DEJAR DE CONTAR COMO PRUEBA de esas
  dos, y eso se demuestra corriendo la vara vieja y la nueva sobre el
  mismo corte y enseñando las dos salidas.
  (4.b) LA ASIMETRIA P2 CONTRA P3 SE QUEDA, y te doy la razon: la P2 mide
  EXISTENCIA de un control en el codigo vivo, que es un estado, y el
  arbol de trabajo es su fuente correcta. LA CONDICION es que la
  asimetria quede escrita DENTRO DEL INSTRUMENTO, no solo en el reporte.
  (4.c) RECUENTO CON LA VARA NUEVA, con su corte al lado, y la tabla
  contada de su fichero. Si el 48/26/22/0/0 se mueve, se dice cuanto y
  por que.

- TAREA 5, EL PASE DE estado DE LAS CINCO MESAS, POR LA ADJUDICACION 6.3.
  Hiciste bien en no moverlas: la reserva del acta 139, 3.6 nombra "las
  once (las seis fusiones y las cinco remitidas)" y las mesas no estan
  ahi. Pero el disparador que esa misma 3.6 les puso es "cuando la fase
  06 cierre", y hoy la fase 06 mide VERDE, 5 de 5 mesas completas, medido
  con el arnes al corte 6f695db6. Van EN UN SOLO ACTO, con el conteo
  ANTES y DESPUES, el esquema intacto (71 fichas, 18 claves) y la guarda
  de cifras del plan re corrida. Si al medir el disparador con TU
  instrumento alguna de las cinco NO sale CUMPLIDO, NO LA MUEVES y lo
  dices: la adjudicacion cubre a las que el disparador alcance, no a las
  cinco por decreto.

- TAREA 6, EL CORREDOR DE LA APERTURA, POR LA ADJUDICACION 6.7. El
  corredor admite el commit de la decision del fundador que
  PROMPT_SIGUIENTE.md cita por su hash, y la guarda LO NOMBRA APARTE en
  vez de fallar por el. EL ROJO POR TU PROPIO COMMIT SE QUEDA INTACTO: esa
  mitad del rojo de la 152 era legitima y la declaraste tu solo, cosa que
  te cuento a favor. Con caso por mutacion por los dos lados: con solo el
  commit del fundador en el corredor, VERDE; con un commit del ejecutor
  dentro, ROJO nombrandolo.

- TAREA 7, LAS DOS DEUDAS DEL REPORTE.
  (7.a) LA MARCA LITERAL EN PROSA. Sobre el reporte tal como quedo
  commiteado, verificar_cifras_del_reporte.py ni llega a contar: muere en
  ROJO POR AMBIGUA porque la seccion 7.b escribe la marca literal de
  apertura de la cabecera tallada dentro de la prosa (linea 311) y la
  marca queda dos veces. El mensaje de la propia guarda lo dice: "para
  citar el mecanismo en prosa se usa OTRO literal, no la marca de
  verdad". Arreglalo en el reporte de esta vuelta y NO LO REPITAS.
  (7.b) LAS LINEAS CIFRA, QUE ERA TU PREGUNTA 3 Y ESTABA ESCRITA EN EL
  FICHERO QUE CITABAS: scripts/loop/verificar_cifras_del_reporte.py,
  docstring lineas 131 a 144 y patron en la linea 394. El formato es
  "CIFRA <etiqueta>: <n> <unidad>", con la unidad del vocabulario cerrado
  de la linea 350 (fichero/ficheros, par/pares, grupo/grupos,
  grafia/grafias, colapso/colapsos, nodo/nodos, linea/lineas,
  arista/aristas, direccion/direcciones, fila/filas,
  comprobacion/comprobaciones, operacion/operaciones), Y VA EN EL FICHERO
  DE SALIDA QUE LA CIFRA CITA, no en el reporte. Se aplica igual a un
  reporte de fase III: la guarda no distingue fase. Tus instrumentos de
  esta vuelta imprimen esa linea, y la cobertura de la guarda deja de ser
  CERO. Publicas la linea COBERTURA entera, salga como salga.
  (7.c) Y LA CIFRA DEL "BAJA DE 12 A 7" QUEDA REGISTRADA COMO CAIDA DE
  REPORTE en el acta 153, seccion 5: la salida sellada que el reporte
  cita dice 12 y no dice 7 en ningun sitio. Vive en prosa de
  acompanamiento, asi que por la letra del 27 ago 2026 NO ACUMULA. No hay
  que arreglar el reporte viejo; hay que no repetirlo.

- TAREA 8, LA FILA 03 FUSIONES, POR LA ADJUDICACION 6.6. Tenias razon:
  lo que le falta a esa celda no es una medicion sino una decision, y la
  decision es mia. LA DOY: los dos divergentes que la CORRECCION 16 ya
  clasifica NO son un pendiente de la fase 03. La celda pide un
  superviviente por acto con el resto deprecado y con alias, y eso esta
  medido en 0 incumplimientos sobre 14 fichas. El arnes de la tabla por
  fase deja de contar los dos divergentes como falta, con la adjudicacion
  citada dentro del arnes, y la fila 03 pasa a VERDE. ES UN CAMBIO DE LA
  CELDA, NO DEL GRAFO: si al correrlo se mueve una sola cifra del grafo,
  paras.

- TAREA 9, EL CIERRE RECOMPUTADO AL CIERRE, con el ciclo entero en su
  orden (run_phase1 --reaplico-curaduria, etiquetas_de_cara --aplicar,
  sync_assets_web, y despues el numstat de dataset/ web/ engine/),
  NUNCA run_phase1 suelto, las tres suites, la cabecera tallada y
  comparada, y las guardas del cierre con su estado real aunque no te
  favorezcan.

- Y DESPUES, SEGUIR EL ORDEN ESCRITO EN MODO CONTINUO hasta el MURO
  CONOCIDO Y YA ADJUDICADO (acta 149, 3.10): la fase 08 no cierra sin una
  SESION CON CREDENCIAL Y CON EL FUNDADOR DELANTE. Al llegar ahi se para y
  se dice, que es donde termina lo que un bucle puede hacer solo. EL
  MERGE NO SE PIDE NI SE HACE: es del fundador y solo suyo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
