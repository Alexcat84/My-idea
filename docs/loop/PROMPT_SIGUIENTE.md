Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

PERO HOY ESA PRIMERA LINEA LLEVA UNA COMPROBACION DELANTE, Y ES EL
HALLAZGO PRINCIPAL DE MI ACTA. ANTES DE COMMITEAR, CORRE:

    git diff --numstat -- dataset/

SI ESO DEVUELVE UNA SOLA FILA, PARA Y NO COMMITEES dataset/. Significa
que hay una mutacion de bateria sin restaurar en el arbol, y commitearla
mete una arista falsa en el catalogo. Restaura con git checkout -- sobre
los ficheros que salgan, vuelve a medir hasta que de cero filas, y DILO
EN TU REPORTE con su medicion. Lo demas (docs/, scripts/) se commitea
normal.

SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

LA 176 VUELVE A SER VUELTA DE BATERIA, Y NO ES UN CAMBIO DE CADENCIA: ES
LA DEUDA DE LA 175, QUE NO SE PAGO. AUDITOR.md 6.1 sigue igual, la
bateria corre CADA CINCO en vuelta propia que no lleva nada mas, y la
vuelta propia que le tocaba se murio antes de producir una linea. NO HAY
TRABAJO DE PLAN AL LADO: OP-L-03 no se toca aqui, ni ninguna otra ficha.
EL TOPE SIGUE EN DOS SUB-TAREAS (AUDITOR.md 6.2): la 174 fue la primera
de las dos seguidas, la 175 no cerro su reporte, y la racha vuelve a
empezar.

LO QUE PASO EN LA 175, MEDIDO POR MI, PARA QUE NO LO TENGAS QUE
RECONSTRUIR:

- LA VUELTA MURIO DENTRO DE LA BATERIA. Tu reporte quedo abierto con sus
  dos filas diciendo ABIERTA, SIN CERRAR, y eso es lo que tenia que
  pasar: el esqueleto hizo exactamente lo que promete. NO ES UNA CAIDA
  TUYA. No publicaste ni una cifra falsa: las siete que alcanzaste a
  escribir las medi una a una y calzan todas.
- EL ARBOL ME LLEGO CONTAMINADO Y LO RESTAURE YO. El arnes
  vuelta154_tarea2d_mutacion_guarda.py habia metido un alias deprecado en
  las dos listas de ab_testing_optimizacion, run_phase1 lo simetrizo, y
  su restauracion no corrio porque vive en un finally y al proceso lo
  mataron. Hice git checkout -- sobre los cuatro ficheros de dataset/ y
  NADA MAS. La evidencia entera esta en
  docs/loop/SALIDA_V175_AUD_ARBOL_CONTAMINADO.txt. Gate 0 despues, ciclo
  entero por mi mano: numstat 0 filas, motor 25/25, tsc 0, web 82 y 1040.
- NO TOQUE scripts/loop/verificar_mutaciones_viejas.py. Tu trabajo de la
  nomina ESTA HECHO Y ESTA BIEN, y sigue sin commitear: 82 a 87, ultima
  vuelta representada 174, arneses_que_faltan() en 0, cero duplicados,
  las 87 entradas con fichero, y los cinco que mi acta 174 nombraba estan
  los cinco y cada uno una vez. NO LO VUELVAS A HACER: COMMITEALO.
  LOS TRES SALIDA_V175_T1A_*.txt YA LOS COMMITEE YO con mi acta, porque
  viven en docs/loop/ y ese es mi mandato (AUDITOR.md 1.5); no los
  busques como pendientes. LO QUE SI SIGUE PENDIENTE ES scripts/:
  verificar_mutaciones_viejas.py modificado, y sin seguir todavia
  vuelta175_correr_bateria.py, vuelta175_cierre.py y
  _prueba_v142_2d_bateria.py. Todo eso es trabajo bueno: entra tal cual.
- LA GUARDA DEL CATALOGO SI MUERDE, Y LO MEDI EN VEZ DE SUPONERLO. Corri
  el arnes culpable entero, 3 casos de 3, y su CASO A pone Gate 0 en rojo
  nombrando el par: 155 pares tras resolver, 154 con cita, 1 SIN CITA,
  ab_testing_optimizacion <-> abandonar_arreglos_rapidos. La arista falsa
  no podia entrar callada. El agujero esta un paso antes, en el commit, y
  por eso esta encargo abre como abre.

LO QUE ADJUDICO Y NO HAY QUE VOLVER A DECIDIR:

- LA BATERIA SE PUEDE PARTIR EN TRAMOS, Y NO ES DOCTRINA NUEVA. La letra
  del fundador del 5 sep fija cuatro cosas: la cadencia (cada cinco), la
  soledad (vuelta propia sin nada al lado), la integridad (entera, doble
  corrida, ninguna guarda aflojada) y la prohibicion de podar la nomina.
  Partir la corrida en tramos DENTRO de esta misma vuelta no toca ninguna
  de las cuatro. Cada entrada sigue corriendo, y sigue corriendo DOS
  VECES. Lo que cambia es el tamano del bocado.
- LA NOMINA NO SE PODA. Sigue en 87 y sigue creciendo. La opcion (c) de
  la parada del 5 sep quedo RECHAZADA y no se reabre.
- LA RUTA SALIDA_V175_BATERIA.txt NO EXISTE Y NO TE CUENTA COMO CAIDA DE
  RUTA. Estaba nombrada en futuro, en la columna que encarga de una fila
  marcada ABIERTA SIN CERRAR, con su columna de prueba vacia. Eso no es
  un letrero sobre un vacio: es un encargo que no se cumplio y que ademas
  se declara. Cero caidas de ruta en la 175.
- LAS DOS RACHAS SIGUEN EN CERO: cifra publicada cero y reporte cero.

TAREA 1, LA BATERIA ENTERA, EN TRAMOS, CON RESTAURACION AL ENTRAR Y CON
SU GUARDA DE COMMIT. Es la unica tarea de trabajo de la vuelta y va sola.

  Lo que hay que construir es un corredor por tramos. La causa esta
  medida y no supuesta, con las cifras del propio archivo: la bateria
  corre a 0,33 minutos por entrada de media y a 0,43 en su ultima corrida
  con cuerpo (75 entradas en 32,5 minutos). Con la nomina en 87, LA DOBLE
  CORRIDA SON ENTRE 57 Y 75 MINUTOS DE BLOQUE INDIVISIBLE, y por eso se
  la comio la vuelta entera. vuelta175_correr_bateria.py ya arreglo el
  sintoma del cero de bytes con la escritura sin buffer y linea a linea,
  y eso se conserva: lo que le falta es no ser un solo bocado.

  (a) LA GUARDA DEL COMMIT, PRIMERO Y BLOQUEANTE. Antes de cualquier otra
      cosa, un instrumento que mida git diff --numstat -- dataset/ y que
      CAIGA EN ROJO si devuelve una sola fila, nombrando los ficheros. Va
      con su caso positivo por mutacion, como todo. Es el remedio del
      agujero que la 175 destapo y es la condicion para que la bateria se
      pueda correr sin peligro; por eso va DENTRO de esta tarea y no es
      una tercera sub-tarea.
  (b) RESTAURACION AL ENTRAR. Cada tramo empieza comprobando que
      dataset/ esta limpio contra HEAD y, si no lo esta, restaurando y
      declarando la restauracion con su medicion. Un finally no sobrevive
      a que maten el proceso; una comprobacion al entrar si.
  (c) LOS TRAMOS. Reparte las 87 entradas en tramos que quepan holgados
      en una sesion, con la cifra del reparto computada de la nomina y no
      tecleada. Cada tramo SELLA SU PROPIA SALIDA, medida antes de
      nombrarla en ningun sitio, y SE COMMITEA AL CERRARSE. Si la sesion
      se muere, lo que se pierde es un tramo y no la vuelta.
  (d) LA DOBLE CORRIDA NO SE TOCA. Cada entrada dos veces, cotejo de
      reproducibilidad de la vuelta 141, y el reloj por los dos extremos.
  (e) AL FINAL, LA SALIDA UNICA. Se compone de los tramos, se MIDE
      (bytes, lineas, sha256) y solo entonces se nombra. Si midiera cero
      bytes, sale en rojo y no se publica la ruta: la regla LA RUTA QUE
      PROMETE PRUEBA ES CIFRA sigue viva.
  (f) SI UN TRAMO SALE EN ROJO, PARA AHI Y TRAELO. No lo re-corras hasta
      que salga verde: la guarda que muerde es informacion, no un
      estorbo.

TAREA 2, ABRIR Y CERRAR TU PROPIO REPORTE. Esqueleto al empezar, la fila
de la TAREA 1 anexada al cerrarse cada tramo (no al final), cierre con
scripts/loop/cerrar_reporte.py en la misma vuelta, y ARCHIVADO EN LA
MISMA VUELTA sin esperar a la 177. Ahi van tambien los registros de esta
vuelta: la restauracion del arbol que hice yo, con su medicion, y el
reparto de tramos con su cifra. La 174 lo hizo entero y salio; la 175 no
llego. Esta es otra vez la primera de las dos seguidas que AUDITOR.md 6.2
pide para levantar el regimen temporal, y por eso su reporte importa
tanto como su bateria. scripts/loop/vuelta175_cierre.py ya esta escrito y
sin commitear: clonalo declarando el clon, como se ha hecho desde la 172.

LO QUE ANOTO Y NO SE EJECUTA AQUI, PARA QUE NO SE PIERDA. Son seis y van
a la 177 o a donde el regimen las deje entrar:
  (a) LA CONVENCION DE BYTES, hallazgo 4.1 del acta 174: que el sello
      publique la cifra que reproduce, o que diga cual de las dos usa. La
      apertura de la 175 ya estreno medir por las dos y eso se conserva.
  (b) LA SEGUNDA SEDE DE LA CLAUSULA 4.4, en REPORTE_V172.md:535, con sus
      DOS MITADES O NINGUNA: la correccion aditiva por el carril 9.10 y
      la re-publicacion de sus bytes y su sha256.
  (c) EL --excluir DEL AISLADOR DE CIEGA. Baja de urgencia y lo digo yo,
      que soy el interesado: esta vuelta tire una sola vez y no me hizo
      falta.
  (d) EL DOCSTRING DE paso0_archivar_anterior.py. Adjudicado desde la
      174: SE CORRIGE, por la cuarta sede del 2 sep.
  (e) LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL D.4: el registrador de la
      174 importa de un fichero llamado vuelta172_... y nada avisa si
      alguien lo borra por viejo.
  (f) OP-L-03, QUE LLEVA SEIS VUELTAS APLAZADA. No se pierde y la cuento
      en voz alta cada vuelta.

DEUDA DE LECTURA ANOTADA, Y SIGUEN SIENDO DOS TRAMOS EN RELECTURA AL
DOBLE. El tramo 1 a 1085 sigue, aunque mi ciega de hoy saliera 8 de 8 sin
una sola discrepancia: la regla es mecanica y no premia una buena tanda,
igual que no premio que el equivocado fuera yo en la 174. Y sigue el
tramo de las cifras de bytes de los ficheros de docs/loop/, por el
hallazgo 4.1: toda cifra de bytes que se publique se contrasta contra las
dos convenciones hasta que una quede fijada.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
