Commitea y pushea lo pendiente en la rama activa antes de tocar nada. Mira
`git status` antes de nada. Lo que vas a encontrar y como se trata, uno por uno:
`dataset/metadata/master_graph.json` modificado con diff de cero bytes es
suciedad de indice y NO se commitea, como la 169, la 170 y la 171 midieron;
`node_modules/` NO se toca y NO entra en `.gitignore` (sigue siendo decision del
fundador, adjudicacion 6.5 de mi acta 170); **y los TRECE ficheros que tu vuelta
anterior dejo sueltos YA LOS COMMITEE YO CON MI ACTA Y NO SE BORRA NINGUNO**:
los doce `docs/loop/SALIDA_V171_*` del bloque de cierre (incluido el
`SALIDA_V171_BATERIA.txt` de cero bytes, que es la prueba medida de que la
bateria no corrio, y el `SALIDA_V171_TALLADOR_CABECERA.txt`, que esta VERDE y lo
vas a necesitar) y `scripts/loop/vuelta171_cierre.py`. Dejarlos sueltos era
arriesgarse a perder los objetos que este encargo te manda usar, que es
exactamente lo que la vuelta 171 recibio de mi por el mismo motivo.

SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE EJECUCION
CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias por operacion.
REGIMEN COMPLETO: el modo austero sigue suspendido por su punto 5. El acta que
manda es la de la vuelta 171 (docs/loop/ACTA_AUDITOR.md, cabecera en la linea
57.847); sus adjudicaciones 6.1 a 6.12 son la letra de este encargo.

LO QUE YA ESTA VERIFICADO Y NO HAY QUE VOLVER A HACER: las cuatro tareas que
corriste reproducen bajo mis instrumentos, digito a digito. Marcador 3.388 con
A 551, B 72, C 5, D 2.760 y cero huecos. Gate 0 con su ciclo entero VERDE por mi
mano, numstat de cero filas, motor 25/25, tsc exit 0, web 82 ficheros y 1.040
pasadas. Censo 3.853 / 3.169 / 684 y aristas 8.780 / 8.740 / 17.520 / 9.914 con
cero auto-aristas. Inventario 672 entradas y 71 fichas. Las cuatro lecturas del
contador `LD` las reproduje exactas, dos de ellas en worktrees limpios que cree
yo, y tu atribucion de los dos ficheros envenenadores es correcta. El censo del
campo `forma` lo recompute con codigo mio y sale igual entero, `REPITE` incluido
en cero. Los 8 pares y su cero de aciertos los recompute con mi propio resolutor
y salen igual, con los 251 ids del universo. Y la cifra de la CUARTA SEDE que
escribiste en el docstring del tallador (400 asuntos, 0 empiezan, 1 contiene) la
recompute sobre `git log -400` y da eso mismo. TU PARADA ESTABA BIEN TRAIDA Y LA
ADJUDICO EN LA 6.1 Y LA 6.2: la guarda que te pusieron era insatisfacible y no
podias saberlo sin medirlo. Mediste bien y no inventaste nada.

LA VARA DEL TRABAJO PENDIENTE SIGUE SIENDO EL INSTRUMENTO,
scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD, NUNCA EL CAMPO
`estado`. Corrida por mi hoy: 71 fichas, 37 que no calzan, 6 en LISTA sin
ninguna prueba, y de esas seis las dos OP-M-02 siguen CUMPLIDAS POR CONSUNCION
por la 6.6 del acta 168. El trabajo real son cuatro fichas.

Y LO PRIMERO QUE TIENES QUE SABER, PORQUE ES LA RAZON DE QUE ESTE ENCARGO SEA EL
QUE ES: LA VUELTA 171 TAMPOCO CERRO SU REPORTE, Y ES LA SEGUNDA SEGUIDA. Tu
bloque de cierre corrio entero a las 00:09 y su tallador salio VERDE, pero
`docs/loop/REPORTE.md` sigue en 454 lineas, sigue diciendo "SIN ESCRIBIR
TODAVIA" y "PENDIENTE DE TALLAR AL CIERRE", y sus secciones 3 a 9 no existen.
NO ES UNA CAIDA DE CIFRA PUBLICADA NI DE REPORTE, porque el reporte dice la
verdad y dice que le falta el cierre. PERO LA CAUSA LA MEDI Y NO ES PRISA:
`scripts/loop/vuelta171_cierre.py` SOLO MIDE, escribe once ficheros `SALIDA_*` y
no toca `REPORTE.md` en ninguna linea. Cerrar el reporte no es un paso del
instrumento: es un paso a mano que viene despues, y las dos vueltas que han
caido han caido justo ahi. Por eso la TAREA 5 de este encargo es codigo.

Y HAY UNA LECCION QUE VA CON TU NOMBRE Y CON EL MIO: EL REMEDIO SE APLICO HACIA
ATRAS. El encargo anterior te mando releer al doble las cuatro piezas del cierre
y lo hiciste, y lo hiciste bien, sobre el cierre de la 170, con once
comprobaciones desde `git show` y cero fallos. Lo que falto fue aplicartelo a ti
mismo. LA RELECTURA AL DOBLE DE ESTA VUELTA SE APLICA AL CIERRE PROPIO: cada una
de las cuatro piezas (reporte cerrado, cabecera pegada, bateria corrida, arbol
limpio) se comprueba dos veces, una al hacerla y otra DESPUES DE COMMITEAR,
leyendo del arbol y de `git show` lo que acabas de escribir, Y ESTA VEZ SOBRE LO
TUYO.

TOPE DE CINCO TAREAS POR VUELTA, y este encargo trae exactamente cinco.

- TAREA 1, BLOQUEANTE Y VA PRIMERA: EL CIERRE QUE FALTA Y LOS REGISTROS.
  (1.a) CIERRAS EL REPORTE DE LA VUELTA 171. El cuerpo lo escribes tu, que eres
  quien corrio la vuelta, y va con sus secciones 3 a 9. NO SE SUAVIZA NADA: los
  cuatro discutibles `D.1` a `D.4` que declaraste en la prosa de tus tareas van
  a la seccion 5 con su pregunta, y tu `CAIDA 1` (los "345 nodos") va a la
  seccion 8 con su nombre. Encima va la cabecera tallada, que YA ESTA VERDE en
  `docs/loop/SALIDA_V171_TALLADOR_CABECERA.txt`: SE PEGA ENTERA, no se teclea, y
  la corri yo hoy y sale identica. Y la seccion 9, LA BATERIA, DICE LA VERDAD:
  la de la vuelta 171 NO CORRIO, su fichero mide cero bytes, y ademas HOY ESTA
  ROJA por letra de su propio codigo (tres arneses tuyos fuera de la nomina).
  Remite a la seccion 5 de mi acta 171 con mi atribucion delante. ESCRIBIR AHI
  UNA CORRIDA DE LA 172 COMO SI FUERA DE LA 171 ES LA ESPECIE QUE ESTA CAMPANA
  PERSIGUE.
  (1.b) EL ACTA 171 Y SUS ADJUDICACIONES 6.1 A 6.12 AL `R.41`, por el mismo
  carril de siempre, con el numero computado por
  `scripts/loop/serie_de_registros.py` y NO tecleado (hoy da 32 entradas, mayor
  `R.40`, siguiente libre `R.41`; recomputalo tu). Con su arnes de mutacion del
  registro, como las vueltas 164 a 168, 170 y 171. Mi acta trae TRES caidas
  propias y las tres van registradas, como el `R.40` hizo con las cuatro de la
  170.
  (1.c) Y SOLO ENTONCES, el archivador para la 171 y el esqueleto de la 172. NO
  te vas a poder saltar el orden aunque quieras: corri el paso 0 en modo solo
  comprobacion contra el repo real y dice ROJO por su clausula (d). TU PROPIA
  GUARDA DE LA 5.a ESTA MORDIENDO EN LA VUELTA SIGUIENTE A LA QUE NACIO, y eso
  hay que decirlo en el reporte.

- TAREA 2, BLOQUEANTE PARA LA 3: SE DESENVENENA EL CONTADOR Y SE CORRIGE EL
  `R.40` (adjudicaciones 6.1 y 6.3).
  (2.a) `docs/loop/reportes/REPORTE_V<N>.md` ENTRA EN LA LISTA DE NARRATIVOS DEL
  BUCLE de `scripts/loop/vuelta48_contar_ld.py`. No es doctrina nueva y no es la
  guarda general que el acta 170 reservo al fundador: es la exclusion que el
  instrumento YA TIENE para `REPORTE.md`, aplicada a un fichero que no se le
  parece sino que ES EL MISMO, y lo prueba el sha256 que tu mismo publicaste,
  `0b85f30e9c78e2b4...` identico al blob de `ca55afd8`. La exclusion va POR
  PATRON de la carpeta de archivo, no por el nombre de una vuelta, o dentro de
  tres vueltas hay que volver a tocarla. Con su caso positivo por mutacion, que
  tiene que CAER si alguien la estrecha o si el archivo vuelve a contar.
  (2.b) EL `R.40` TRAE UNA AFIRMACION FALSA Y SE CORRIGE, que es tu propia
  doctrina de la TAREA 4.a aplicada a ti: `docs/PENDIENTES.md:12323` dice de la
  adjudicacion 6.1 "VIA: EJECUTADA" y "EJECUTADA, TAREA 3 de esta vuelta ... las
  16 filas ganan LD-139 a LD-154", Y LA TAREA 3 NO SE CORRIO, cosa que tu propio
  reporte dice tres veces. Carril del banco `9.10`: la frase vieja ENTERA Y
  TACHADA, la correccion fechada debajo con la medicion pegada, y EL REPARTO POR
  VIA RECOMPUTADO POR INSTRUMENTO, no tecleado, porque el "EJECUTADA: 8" de esa
  entrada cuenta esa entre las ocho. NO se toca la glosa de la 6.2, que describe
  bien lo que paso, parada incluida.
  (2.c) Vuelves a correr el contador y publicas la lectura nueva al lado de la
  vieja, Y CON LA ATRIBUCION DELANTE: cada numero por encima de `LD-138` que
  siga en el universo, con SU FICHERO Y SU LINEA. Esa lista es la guarda de la
  TAREA 3 y sin ella la 3 no se corre.

- TAREA 3, LA NUMERACION `LD`, QUE AHORA SI SE ESCRIBE (adjudicacion 6.2, que
  refina la 6.2 de mi acta 170 con el codigo delante). La convergencia en
  `LD-138` que aquella adjudicacion pedia es INALCANZABLE, y la culpa no es
  tuya: el residuo es la glosa del `R.40` citando la orden del acta, y
  `docs/PENDIENTES.md` no se puede excluir porque SI es sitio donde cabe un
  encargo, como tu razonaste bien. LA SALIDA ESTABA EN EL MISMO SITIO DONDE
  ESTABA LA REGLA DE LA 6.1: `serie_de_registros.py` computa el siguiente libre
  sobre `^##\s+R\.(\d+)\.`, o sea sobre ENTRADAS ESCRITAS CON SU CABECERA, y su
  docstring se cuida expresamente de no confundir una serie con menciones de
  otra forma. UNA MENCION EN PROSA NO ASIGNA UN NUMERO; UNA ENTRADA ESCRITA SI.
  Asi que la vara que asigna es la de las HECHAS, las que tienen seccion propia,
  que hoy dan `LD-138`, y el siguiente libre es `LD-139`. Las 16 filas de la
  segunda tanda de `docs/plan/LECTURAS_DIRIGIDAS.md` (lineas 327 a 518) GANAN
  `LD-139` a `LD-154` POR ADICION PURA, con los numeros COMPUTADOS POR
  INSTRUMENTO y SIN TOCAR UNA PALABRA de su texto. CON DOS GUARDAS, y las dos
  tienen que caer por mutacion: (i) que el numero se compute y no se teclee, y
  (ii) que NINGUN numero por encima de `LD-138` tenga seccion propia en la
  lectura de la 2.c; si alguno la tuviera, entonces si hay una asignacion ajena
  y PARAS Y LO TRAES. Al terminar, el contador tiene que dar 98 hechas y
  `LD-154` de mayor en las dos varas. Y DESPUES, la fila "lecturas dirigidas
  encargadas y sin hacer" de `docs/plan/00_INDICE.md` recibe su cifra de hoy por
  `9.21`, por adicion y sin tocar la letra vieja (adjudicacion 6.10): tu `D.4`
  era correcto, y con la 2.a esa cifra deja de estar contaminada.

- TAREA 4, LOS TRES ARNESES Y LA BATERIA (adjudicaciones 6.4 y 6.5). EL ORDEN
  ES OBLIGATORIO Y NO ES CAPRICHO: si metes el arnes roto en la nomina, metes un
  rojo dentro de la bateria.
  (4.a) PRIMERO SE REFUNDA EL CASO `F` DE `vuelta171_tarea5a_mutacion_enchufe.py`
  SOBRE SUJETO CONGELADO. Lo corri hoy y da EXIT 1: nueve casos pasan y
  `F_el_reporte_170_del_repo_esta_archivado_y_calza` FALLA, real=False
  esperado=True. La causa es de diseno, no de azar: ese caso mira EL ARBOL VIVO,
  y solo fue cierto durante los minutos entre archivar la 170 y pisar
  `REPORTE.md` con el esqueleto. Hoy es falso y lo sera para siempre. Contra la
  condicion de la vuelta 148, SUJETO CONGELADO, que la 6.10 del acta 170
  confirmo con esas palabras. Se fabrica el escenario en un temporal, como hacen
  sus otros nueve casos, y el arnes tiene que salir verde HOY y seguir verde
  dentro de diez vueltas. La cifra que publicaste, "10 casos, 10 pasan, 10
  caen", era cierta cuando la corriste y NO la cuento como caida; lo que no se
  sostiene es el arnes.
  (4.b) LOS TRES ARNESES DE LA 171 ENTRAN EN LA NOMINA de
  `scripts/loop/verificar_mutaciones_viejas.py`:
  `vuelta171_mutacion_busqueda_acta.py`, `vuelta171_tarea1a_mutacion_registro.py`
  y `vuelta171_tarea5a_mutacion_enchufe.py`. Medido por mi con la funcion pura
  del propio instrumento: `arneses_que_faltan()` da 3, la nomina tiene 75
  entradas y su ultima vuelta representada es la 170. El propio codigo dice que
  eso es ROJO. Los otros dos los corri y salen verdes, 43 de 43 y 16 de 16.
  (4.c) LA BATERIA SE CORRE ENTERA Y SOLA AL CIERRE, sin nada al lado, y su
  salida entera va en la seccion 9 del reporte de esta vuelta. Con las tres
  entradas nuevas la nomina tiene que dar 78 y su ultima vuelta representada
  tiene que ser la 171.

- TAREA 5, EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO (adjudicacion 6.6).
  Nace `scripts/loop/cerrar_reporte.py`, DE NOMBRE ESTABLE Y SIN NUMERO DE
  VUELTA, como sus hermanos `paso0_archivar_anterior.py`,
  `tallar_cabecera_reporte.py`, `archivar_reporte.py`, `serie_de_registros.py` y
  `aislador_de_ciega.py`, para que el proximo clon no lo pierda. Hace en UN SOLO
  ACTO lo que `vuelta171_tarea1b_cerrar_reporte_170.py` ya sabe hacer, y que ese
  fichero te sirva de plano: pega la cabecera tallada leyendola del fichero del
  tallador, anexa el cuerpo del cierre, escribe el veredicto de una linea, y
  RELEE DEL DISCO lo que acaba de escribir. Y CAE EN ROJO si al terminar falta
  cualquiera de las cuatro piezas: veredicto escrito, cabecera pegada, secciones
  3 a 9 presentes, y la salida de la bateria dentro de la seccion 9. Con su caso
  positivo por mutacion, que tiene que CAER si el instrumento da verde con
  cualquiera de las cuatro ausente. ESTA VUELTA SE CIERRA CON EL, que es la
  unica forma de saber si sirve. NO es la escalada de la racha de reporte, que
  sigue en UNO y no se dispara; es la operacion de codigo que pide una especie
  que ya mordio dos vueltas seguidas.

LO QUE ESTE ENCARGO NO TRAE, DICHO PARA QUE NO LO BUSQUES: `OP-L-03` sigue
abierta y leida y NO se ejecuta esta vuelta tampoco, y el motivo lo digo entero
en vez de esconderlo en el tope de cinco tareas: dos vueltas seguidas se han
cortado antes de cerrar su reporte, y una vuelta entera dedicada a pagar esa
deuda y a ponerle codigo vale mas que media ficha ejecutada sobre un mecanismo
de cierre que no aguanta. La 173 abre con `OP-L-03`.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
