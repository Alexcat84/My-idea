Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 191. Rama `pasada-unica`. FASE III, EJECUCION.

NO ES VUELTA DE BATERIA. La 189 la corrio entera y por `AUDITOR.md` 6.1 la
siguiente cae en la 194. La seccion 9 de tu reporte cierra con el HUECO
DECLARADO Y MEDIDO por su carril, con su nombre, sus bytes medidos y su
atribucion, LAS TRES JUNTAS. Un hueco declarado no es un hueco escondido.

VAN CINCO SUB-TAREAS. El tope de CINCO ya esta vigente desde la 4.10 del acta
190 y no hace falta volver a ganarlo. Lo remedi para que la cifra no envejezca:
son CUATRO las vueltas seguidas que cerraron su propio reporte con
`cerrar_reporte.py`, la 187, la 188, la 189 y la 190, no tres.

ABRE EL REPORTE AL EMPEZAR, con su esqueleto tallado y en su propio commit, y
mide tu desfase de calibrado DENTRO del bloque de apertura y ANTES de la primera
operacion. Una columna de apertura medida al cierre es caida que ACUMULA.

=============================================================================
TAREA 1. LOS REGISTROS. BLOQUEANTE.
=============================================================================

El acta 191 entra en la serie con el numero que devuelva
`scripts/loop/serie_de_registros.py`, computado y no tecleado (hoy el siguiente
libre es `R.53`, pero lo dice el instrumento, no este encargo).

La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta, no de
aqui:

  - LAS NUEVE ADJUDICACIONES `4.1` a `4.9`, y esta vez SI son nueve a favor:
    seis son los discutibles del ejecutor (`D.1` a `D.6`) y los seis van A FAVOR,
    y las tres restantes (`4.7`, `4.8`, `4.9`) son las tres preguntas
    contestadas. Tu registrador de la 190 aprendio a contar la marca EN CONTRA;
    esta vuelta tiene que salir CERO EN CONTRA sin que la maquina se rompa por
    no encontrar ninguna. Pruebalo por mutacion con un acta fabricada que si
    lleve una.
  - LOS TRES HALLAZGOS DE LA SECCION 5, que no salen de ningun discutible: la
    marca `DISCUTIBLE MARCADO` contra la dificultad medida (`5.1`), la etiqueta
    del veredicto duplicada (`5.2`), y `git checkout --` que no restaura byte a
    byte (`5.3`).
  - UNA CAIDA PROPIA DEL AUDITOR, de metodo, la `5.3`, ESCRITA COMO UNA Y NO
    OMITIDA; y CERO caidas del ejecutor que acumulen, con las TRES de metodo que
    el reporte de la 190 declara registradas como tales.
  - LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de
    puestos con su nota: los 30 de esta acta son SOLAPE TOTAL a proposito, o sea
    control y no cobertura nueva.

EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada. Pruebalo
re corriendolo, con la sede medida en bytes antes y despues, como en la 190.

=============================================================================
TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DEL 3182. BLOQUEANTE.
=============================================================================

ES LA DEUDA DE CREDITO QUE TU PROPIA TAREA 4 DE LA 190 DEJO MEDIDA Y QUE NO SE
AUTO ENCARGO, y la adjudique A FAVOR en la 4.5 de mi acta: quien encarga el
doble es el auditor, y lo encargo aqui.

QUE TRAMO. La tanda de 30 puestos de la vuelta 190, la de
`docs/loop/SALIDA_V190_T4_CIEGA.txt`, donde la discrepancia del `3182` cayo
FUERA de tus dudosos marcados.

QUE ES AL DOBLE. Sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada. 30 del
tramo mas 30 vecinos son 60: el doble exacto.

EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO. A `vecinos()` se le pasa
`evitar` con TODO lo consumido, que hoy son 471 puestos: los 441 de antes de la
190 (las dos exclusiones, 411 y 381, y las dos ciegas de las actas 189b y 190,
30 y 30) MAS los 30 de la tanda de la 190, que ademas son los mismos 30 que yo
relei en el acta 191 (`docs/loop/_auditor_v191_ciega_blind.txt`, y son el mismo
conjunto: lo medi). Cuentalo tu de sus ficheros, no de esta cifra. Solape con el
propio tramo y con el universo consumido: 0 y 0, POR CONSTRUCCION.

COMO SIEMPRE: `scripts/loop/aislador_de_ciega.py`, criterio escrito literal,
ciega y destape en ficheros SEPARADOS, tus clases escritas y COMMITEADAS en su
propio commit ANTES de abrir el destape, y tus dudosos NOMBRADOS DELANTE.
Publica cuantos coinciden, cuantos discrepan, cuantos dentro y cuantos fuera de
tus dudosos.

NO SE TOCA NINGUNA CLASE. `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en
lectura y su `sha256` LF abre y cierra en `0a77b5a35a962621` por las dos
convenciones. Si de la relectura sale una correccion, se declara y se trae; no
se escribe ni una fila.

=============================================================================
TAREA 3. LAS DOS CONVENCIONES DE `lineas`, QUE LLEVAN DOS VUELTAS ESPERANDO.
=============================================================================

ES LA `5.1` DEL ACTA 190 Y NO SE HA TOCADO. Hay instrumentos de la cadena que
cuentan lineas con `len(texto.split(NL))`, que suma un elemento vacio final que
no es una linea, y otros que cuentan con `texto.count(NL)`, que si calza con
`wc -l`. El de la 190 publico "2231 lineas" de `docs/plan/LECTURAS_DIRIGIDAS.md`
donde `wc -l` dice 2230. La cifra no era inventada, la imprimia su instrumento:
por eso el defecto es del instrumento y no del que lo leyo.

QUE HACER, Y ES UNA MEDICION ANTES QUE UN ARREGLO:

  a) MIDE PRIMERO. Cuenta cuantos ficheros de `scripts/loop/` cuentan lineas por
     cada una de las dos convenciones, nombralos, y publica la cifra. Sin esa
     cifra el arreglo no se sabe de que tamano es. Es la misma disciplina que le
     aplique a la `P.2` del acta 190: primero se cuenta, despues se cambia.
  b) DESPUES ARREGLA, y la vara es la de las dos convenciones de BYTES que esta
     casa ya construyo: una cifra que no se puede cotejar con la herramienta
     obvia no sirve de cifra. O se publica la pareja, o se publica la que calza
     con `wc -l` diciendo cual es.
  c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un instrumento vuelve a
     publicar una sola cifra de lineas por la convencion que no calza.

NO TOQUES LOS NUMEROS YA PUBLICADOS EN REPORTES CERRADOS. Un reporte cerrado no
se reescribe: si una cifra vieja queda explicada por esto, se dice al lado.

=============================================================================
TAREA 4. LA GUARDA DEL VEREDICTO DUPLICADO EN `cerrar_reporte.py`.
=============================================================================

ES MI HALLAZGO `5.2` DEL ACTA 191, Y ES NUEVO DE LA VUELTA 190. La linea 50 del
reporte de la 190 dice `**EL VEREDICTO DE UNA LINEA: **EL VEREDICTO DE UNA
LINEA: LAS CINCO TAREAS...`. La causa esta medida: `cerrar_reporte.py` en su
linea 1817 compone `"**EL VEREDICTO DE UNA LINEA: %s**"`, y su propia salida
(`SALIDA_V190_CERRAR_REPORTE.txt`, linea 45) prueba que el veredicto que se le
paso YA traia la etiqueta y sus asteriscos. Los reportes 186 a 189 la traen una
sola vez, o sea que no es herencia.

QUE HACER:

  a) QUE `cerrar_reporte.py` CAIGA EN ROJO si el `--veredicto` que recibe ya
     trae la etiqueta o los asteriscos, en vez de pegarla dos veces. Fallar
     ruidoso: no la limpies en silencio, porque limpiar en silencio es la otra
     mitad de la misma enfermedad. Que diga que recibio y que esperaba.
  b) CASO POSITIVO POR MUTACION que CAIGA si la guarda se quita.
  c) EL REPORTE DE LA 190 NO SE REESCRIBE. Esta cerrado y archivado byte a byte,
     y su etiqueta doble se queda donde esta con esta explicacion al lado. Lo que
     se arregla es que no vuelva a pasar.

=============================================================================
TAREA 5. LA MARCA `DISCUTIBLE MARCADO` CONTRA LA DIFICULTAD MEDIDA. SOLO MEDIR.
=============================================================================

ES MI HALLAZGO `5.1`, Y ESTA TAREA NO TOCA NI UNA RAZON DEL ARCHIVO.

LO QUE MEDI SOBRE MI TANDA DE TREINTA: dos lectores independientes, tu y yo,
discrepamos del archivo en los MISMOS OCHO puestos (872, 904, 963, 1201, 1366,
2423, 3067 y 3086); `DISCUTIBLE MARCADO` aparece en 427 de las 3.388 filas del
archivo, el 12,6 por ciento, y en CERO de esos ocho; el unico de los treinta que
la lleva es el 3182, que tumbo a un lector y no al otro.

TREINTA CASOS NO SON UNA LEY, Y POR ESO ESTO ES UNA MEDICION Y NO UN ARREGLO.
Lo que encargo es llevar esa cuenta a TODA la historia de ciegas de la campana
que se pueda medir de ficheros del repo:

  a) DI PRIMERO CUAL ES TU UNIVERSO Y COMO LO CONSTRUYES, antes de contar nada:
     que ficheros de cotejo de ciega existen, de que vueltas, y cuales quedan
     fuera por no ser legibles con una regla unica. Publica la cifra de los que
     entran y de los que no, con sus nombres. Un universo elegido despues de ver
     el resultado no sirve.
  b) CUENTA, sobre ese universo: cuantos puestos han tumbado alguna vez a un
     lector, cuantos de esos llevan `DISCUTIBLE MARCADO` en su razon, y cual es
     la tasa de la marca en el archivo entero para poder compararla. Las tres
     cifras juntas o ninguna.
  c) NO SAQUES LA CONCLUSION SI LA CUENTA NO LA SOSTIENE. Si el universo sale
     pequeno, dilo y publica el tamano: "no alcanza para concluir" es un
     resultado y se escribe como tal. Inventar una tendencia sobre veinte casos
     es exactamente lo que esta casa persigue.
  d) NO SE ESCRIBE NI UNA FILA DEL ARCHIVO. Ponerle la marca a ocho razones
     seria editar datos publicados sobre una muestra de treinta, y eso ni lo
     adjudico yo ni lo hace esta vuelta.

=============================================================================
LO QUE NO ENTRA, DICHO PARA QUE NO SE COLE NI SE REDESCUBRA
=============================================================================

Ni cribado, ni recomputo, ni operaciones del plan, ni las mesas anotadas, ni
podar la nomina (la opcion `c` que el fundador RECHAZO el 5 sep 2026: la nomina
sigue creciendo y nadie la poda sin el fundador), ni la bateria, que cae en la
194.

Y SIGUEN FUERA, NOMBRADAS PARA QUE LA 192 NO LAS REDESCUBRA:

  - `acumulan()` que lea la tabla, o que declare en su salida que no es la sede.
  - El cotejo de clon declarado que separa sentencia de codigo de cambio de
    texto.
  - La excepcion que publica siempre su lista.
  - La medicion del censo de arneses con carril de mutacion sin fichero propio.
  - Las ocho actas sin entrada propia en la serie (173 a 180), medidas y no
    arregladas.
  - El exitcode 2 propagado a `--componer`, que adjudique A FAVOR en la 4.9 del
    acta 191 por extension citable del banco 9, y que no entra en esta vuelta.
  - Que el campo `evidencia` de `OP-L-02` nombre los ficheros que ya existen,
    adjudicado en la 4.7 como la mitad barata de esa pregunta. Su ESTADO NO SE
    MUEVE: sigue en `LISTA`, y declararla HECHA es del fundador.

Y NO SE MUEVE NINGUN VEREDICTO: el `sha256` LF de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en el mismo valor, y
`dataset/` no se toca a mano: el `numstat` se mide al entrar y al salir y las
dos cifras se publican.

Y SI RE CORRES UN INSTRUMENTO QUE PISA UNA SALIDA SELLADA AJENA, RESTAURALA EN
LF Y REMIDELA ANTES DE DARLA POR RESTAURADA. `git checkout --` te la devuelve en
CRLF y te cambia los bytes publicados: me paso a mi en esta acta y lo declare
como caida propia en su `5.3`. El corte nuevo, si interesa, va al lado con su
nombre y su vuelta, nunca encima.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
