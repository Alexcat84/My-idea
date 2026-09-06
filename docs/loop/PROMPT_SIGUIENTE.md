Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 194. Rama `pasada-unica`. FASE III, EJECUCION.

ESTA ES VUELTA DE BATERIA. Por `AUDITOR.md` 6.1, decision del fundador del 5 sep
2026, la bateria corre CADA CINCO VUELTAS en una vuelta propia QUE NO LLEVA NADA
MAS. La 189 la corrio entera, y por esa cadencia te toca a ti. La seccion 9 de tu
reporte NO cierra con hueco declarado: cierra con la bateria corrida.

VAN TRES SUB-TAREAS Y DOS SON BLOQUEANTES. El tope de CINCO sigue vigente y esta
ganado: la racha de cierres mide 9 hoy (185 a 193), contada por mi del inventario
entero con `scripts/loop/vuelta192_racha_de_cierres.py`. CUENTALA TU DEL
INSTRUMENTO y publica lo que salga. Ese instrumento PISA su propia sellada: si la
corres, restaurala con `git checkout --` y REMIDELA antes de darla por
restaurada.

Y LA TAREA 2 NO ES TRABAJO DE AL LADO: ES LA PRECONDICION DE LA BATERIA. Dos
entradas de la nomina estan rotas de una forma que la bateria misma va a pisar, y
por `AUDITOR.md` 6.1 nueve salidas selladas no valen si una es de otra hondura que
las demas. Es el mismo criterio con el que el acta 193 me puso a mi dos
bloqueantes antes de esta bateria, y no lo invento hoy.

ABRE EL REPORTE AL EMPEZAR, con su esqueleto tallado y en su propio commit, y mide
tu desfase de calibrado DENTRO del bloque de apertura y ANTES de la primera
operacion. Una columna de apertura medida al cierre es caida que ACUMULA, y esa
fue mi `C.1` en tu vuelta anterior.

Y UNA COSA QUE ME PASO A MI EN ESTA AUDITORIA Y TE AHORRO: el ciclo de Gate 0 hay
que correrlo ENTERO. Con solo `run_phase1.py --reaplico-curaduria` quedan 72
lineas cambiadas en `dataset/metadata/master_graph.json`, y es
`scripts/etiquetas_de_cara.py --aplicar` quien las repone. Medido por mi hoy: tras
el ciclo completo el `numstat` de `dataset/`, `web/` y `engine/` da CERO lineas.

=============================================================================
TAREA 1. LOS REGISTROS. BLOQUEANTE.
=============================================================================

El acta 194 entra en la serie con el numero que devuelva
`scripts/loop/serie_de_registros.py`, computado y no tecleado (hoy el siguiente
libre es `R.56`, pero lo dice el instrumento, no este encargo).

La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta y no de
aqui:

  - LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, y las diez van A FAVOR: siete son tus
    discutibles (`D.1` a `D.7`) y las tres restantes son tus preguntas `P.1`, `P.2`
    y `P.3` contestadas por extension citable. CERO EN CONTRA, y es la cuarta acta
    seguida.
  - LOS TRES HALLAZGOS DE LA SECCION 5, que no salen de ningun discutible: los dos
    arneses de la cuarta puerta que se contradicen en la sede de verdad (`5.1`), la
    seccion 8 que dice cuatro donde el instrumento dice cinco (`5.2`), y los
    mensajes de commit del bucle que queman la ciega del auditor antes de su primer
    comando (`5.3`).
  - UNA CAIDA DEL EJECUTOR, DE REPORTE, QUE **SI ACUMULA**: es el hallazgo `5.2`.
    Vive solo en `REPORTE.md` y no mueve ningun dato, luego es de reporte; y vive
    en una CONCLUSION (la seccion 8 se titula LO QUE LA 194 RECIBE y la frase es su
    titular en negrita), luego cuenta para la racha por la letra del 27 ago 2026.
    **RACHA DE REPORTE: 1.** No hay escalada que encargar todavia, porque la
    escalada se dispara a DOS, y lo digo expresamente para que no se lea como
    olvido.
  - TRES CAIDAS DEL EJECUTOR DE METODO, `C.1` a `C.3`, todas declaradas por ti
    mismo en tu propia seccion 8.1. Se registran y no abren racha.
  - DOS CAIDAS PROPIAS DEL AUDITOR, y la primera es grave: `C.1`, ROMPER UN REMEDIO
    ESCRITO, que CUENTA PARA LA PARADA por la letra del 5 sep 2026 (abri
    `REPORTE.md` con un `wc -l` antes de sellar, lo apunte a mano, y el sello de la
    vuelta 194 SALIO ROJO y no existe); y `C.2`, de metodo, haber commiteado
    `docs/loop/_TURNO_DEL_AUDITOR.json`, que es estado de turno y no contenido de
    campana.
  - LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de
    puestos con su nota: 30 aislados, 30 cotejados, **ONCE QUEMADOS** por el
    contexto de sesion y no por comando del auditor, y el cotejo publicado dos
    veces, sobre los 30 y sobre los 19 limpios.

EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada. Pruebalo re
corriendolo, con la sede medida en bytes antes y despues.

=============================================================================
TAREA 2. LOS DOS ARNESES DE LA CUARTA PUERTA QUE SE CONTRADICEN. BLOQUEANTE, Y
ES LA PRECONDICION DE LA BATERIA.
=============================================================================

ES MI HALLAZGO `5.1`, Y ESTA CORRIDO Y NO DEDUCIDO:
`docs/loop/_auditor_v194_cuarta_puerta_rota.txt`, con sus tres casos.

  `vuelta192_tarea4_mutacion_cuarta_puerta.py`
      llama a `AP.olvidar_todo()` OCHO veces contra el modulo REAL (lineas 103,
      123, 137, 158, 184, 210, 226 y 239) y NUNCA redirige `AP.RUTA_DEL_TURNO` a
      un temporal. Tu TAREA 4.a le anadio a `olvidar_todo()` el
      `os.remove(RUTA_DEL_TURNO)`, y con eso este arnes BORRA EL TURNO VIVO DEL
      AUDITOR en su sede de verdad. Corrido solo, con el fichero puesto: sale
      exitcode 0 y el fichero queda BORRADO. No avisa y no cae.

  `vuelta193_tarea4e_mutacion_sello_entre_procesos.py`
      su caso `H` exige `os.path.exists(turno_real) == False` (lineas 262 a 264).
      Corrido solo, con el fichero puesto: exitcode 1, VEREDICTO ROJO.

  LOS DOS EN EL ORDEN ALFABETICO EN QUE LA BATERIA LOS CORRE: el de la 192 borra
  el fichero y el de la 193 sale VERDE. **SU VERDE NO ES SUYO: se lo debe al
  otro.** Lo unico que hoy los pone de acuerdo es el orden, y un verde que depende
  del orden en que corren dos arneses no prueba nada.

NADIE LO HABIA VISTO PORQUE EL FICHERO DEL TURNO LO ESTRENA MI VUELTA: la
persistencia nacio en tu TAREA 4.a y yo soy el primer turno que la usa.

QUE HACER:

  a) QUE EL ARNES DE LA 192 NO TOQUE LA SEDE DE VERDAD. Redirige
     `AP.RUTA_DEL_TURNO` a un temporal antes de su primer `olvidar_todo()`, que es
     exactamente para lo que tu propio comentario dice que esa variable es de
     modulo: *"PARA QUE LOS ARNESES LO PUEDAN REDIRIGIR A UN TEMPORAL: un arnes
     que escribiera en la sede de verdad ensuciaria el turno del auditor"*. El
     mecanismo ya lo tienes escrito en el arnes de la 193, linea 45.
  b) QUE EL ARNES DE LA 193 DEJE DE EXIGIR QUE EL FICHERO NO EXISTA. Lo que tiene
     que comprobar es que EL NO LO TOCO, no que no exista: mide el fichero ANTES
     y DESPUES (existencia, bytes y `sha256`) y cae si CAMBIA. Un turno de auditor
     vivo tiene ese fichero puesto, y un arnes que exige su ausencia esta pidiendo
     que no haya auditor.
  c) CON SU CASO POSITIVO POR MUTACION, y que pruebe LA COSA QUE FALLA HOY: que
     CAIGA si un arnes de la nomina modifica o borra `_TURNO_DEL_AUDITOR.json` en
     su sede de verdad. Que lance PROCESOS DE VERDAD, como hiciste en la 193.4.e,
     porque corriendo todo en uno esto no se ve.
  d) QUE EL FICHERO DEL TURNO NO SE PUEDA VOLVER A COMMITEAR. Es mi caida `C.2`
     y la reparo a medias: lo saco del arbol al cerrar mi turno, pero la guarda
     durable es tuya. Lo natural es `.gitignore`; si eliges otra via, dilo con su
     motivo.
  e) NO SE CLONA NINGUNO DE LOS DOS FICHEROS: se les anade.
  f) NO TOQUES LA NOMINA. No se poda, no se adelanta y no se le meten entradas
     nuevas: la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada,
     y sigue en 127 entradas leidas del instrumento.
  g) AL CERRAR, CORRE LOS DOS ARNESES EN LOS TRES ESCENARIOS DE MI FICHERO (cada
     uno solo con el fichero del turno puesto, y los dos seguidos) Y PUBLICA LAS
     TRES SALIDAS. Si el verde de alguno sigue dependiendo del orden, PARAS Y LO
     TRAES: la bateria no se corre con esto abierto.

=============================================================================
TAREA 3. LA BATERIA, ENTERA Y POR TRAMOS.
=============================================================================

`AUDITOR.md` 6.1, literal: *"LA BATERIA CORRE POR TRAMOS OBLIGATORIOS. CADA TRAMO
SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR. UNA VUELTA CORTADA RETOMA EN EL
TRAMO SIGUIENTE, no desde el principio. Y LA BATERIA SE DECLARA CORRIDA CUANDO LOS
NUEVE TRAMOS TIENEN SALIDA SELLADA DEL MISMO CALIBRE."*

UNA TRAMPA MEDIDA POR MI, Y TE LA PONGO DELANTE PORQUE ES LA QUE MAS BARATO SALE
DE PISAR. Corri `python scripts/loop/vuelta183_bateria_por_tramos.py --siguiente` y
me contesto *"CIFRA tramos CON salida sellada no vacia: 9. LOS QUE FALTAN: 10. EL
SIGUIENTE ES EL TRAMO 10."* **ESAS NUEVE SALIDAS SON DE LAS VUELTAS 183 Y 184, NO
TUYAS**, y lo verifique con `git log` fichero a fichero: el tramo 1 es de
`aac1c84e` (vuelta 183), el 5 de `d0058b86` (vuelta 184) y el 9 de `3500db9d`
(vuelta 184, y su asunto dice EN ROJO). Si corres ese fichero y solo el tramo 10,
declararias la bateria corrida sobre la corrida de otra vuelta, y la 6.1 lo prohibe
con estas palabras: *"una corrida de otra vuelta pegada aqui tampoco vale"*.

LA SALIDA ES LA QUE LA 189 YA USO Y NADIE OBJETO: el lanzador SE CLONA por vuelta,
y su numero NO se teclea, se computa de `os.path.basename(__file__)` (lineas 87 a
96 del de la 183). Existe `scripts/loop/vuelta189_bateria_por_tramos.py` y es el
precedente vivo.

QUE HACER:

  a) CLONA EL LANZADOR COMO `scripts/loop/vuelta194_bateria_por_tramos.py`, CLON
     DECLARADO del de la 189, que es el ultimo que corrio de verdad. Cotejalo con
     `scripts/loop/cotejar_clon_declarado.py` y pega su salida en el reporte. Con
     el nombre puesto, sus salidas se llaman solas `SALIDA_V194_BATERIA_TRAMO_N.txt`
     y `--siguiente` te dira TRAMO 1, que es la verdad.
  b) EL NUMERO DE TRAMOS SE COMPUTA, NO SE TECLEA NI SE HEREDA. Correlo con
     `--plan` y publica lo que salga con su FECHA DE CORTE (banco `9.21`). Hoy la
     nomina esta en 127 y el reparto da DIEZ. El NUEVE de `AUDITOR.md` 6.1 es la
     cuenta de la nomina del 5 sep 2026, no un objetivo: el propio fichero lo dice
     en su comentario (*"el numero de tramos NO se teclea tampoco: sale de
     len(tramos)"*) y la 189 corrio DIEZ y el acta 190 lo dio por bueno. SI TU
     `--plan` da otra cifra, publica esa y di de que nomina sale.
  c) CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR, antes de seguir al
     siguiente. Si la vuelta se corta, la que venga retoma con `--siguiente`.
  d) LA DOBLE CORRIDA NO SE AFLOJA: cada entrada se corre DOS VECES por el cotejo
     de reproducibilidad de la vuelta 141. Sigue entera.
  e) AL FINAL, `--componer`, que es quien coteja EL CALIBRE. La bateria se declara
     corrida cuando TODOS los tramos tienen salida sellada del mismo calibre, y
     UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA.
  f) PUBLICA EL RELOJ de la corrida, que la 6.1 lo pide junto a la doble corrida y
     la salida sellada.
  g) SI UN TRAMO CAE EN ROJO, NO LO ESCONDAS Y NO LO REPITAS HASTA QUE SALGA
     VERDE: publicalo con su tramo, su entrada y su motivo. La 189 tumbo una
     entrada y eso fue lo util de aquella bateria.

=============================================================================
LO QUE NO ENTRA, DICHO PARA QUE NO SE COLE NI SE REDESCUBRA
=============================================================================

Ni cribado, ni recomputo, ni operaciones del plan, ni las mesas anotadas, ni
podar la nomina (la opcion `c` que el fundador RECHAZO el 5 sep 2026), ni ciegas
nuevas: ES VUELTA DE BATERIA y no lleva trabajo de plan al lado.

Y SIGUEN FUERA, NOMBRADAS PARA QUE LA 195 NO LAS REDESCUBRA:

  - LA RELECTURA AL DOBLE DEL TRAMO DE MI TANDA, que es MI deuda de credito y la
    encargo yo, que es donde `AUDITOR.md` 1.2 la pone. VA A LA 195 porque la 194
    es de bateria, y la dejo CERRADA HOY para que no se elija despues de mirar:
    EL TRAMO son los 30 puestos de `docs/loop/_auditor_v194_ciega_blind.txt`, que
    son los mismos 30 de `docs/loop/SALIDA_V193_T3_CIEGA.txt`; EL DOBLE son sus 30
    vecinos deterministas con `vecinos()` IMPORTADA de
    `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada, con
    `evitar` cargado de TODO lo consumido y contado de sus ficheros. El motivo:
    dos discrepancias fuera de mi marcado, `612` y `2426`.
  - EL REMEDIO DE MI HALLAZGO `5.3`, que es el que de verdad importa y que NO es
    tuyo del todo: los mensajes de commit del bucle NO deben publicar la clase de
    ningun puesto ni el reparto de una tanda a ciegas. Tu commit `b57aa7d6`
    publico ocho puestos con su clase y el reparto entero, y el contexto de
    apertura de mi sesion me los puso delante ANTES de mi primer comando: once de
    mis treinta llegaron quemados y ninguna de las cuatro puertas de
    `apertura_del_auditor.py` puede impedirlo, porque las cuatro vigilan comandos
    del auditor. DESDE HOY Y SIN ESPERAR A NADIE: escribe tus mensajes de commit
    SIN clases por puesto y SIN reparto de ciega; di que las clases estan escritas
    y commiteadas y nombra el fichero, que es lo que hace falta para poder
    citarlo. La guarda de codigo que lo imponga se encarga en la 195, y va
    nombrada aqui para que no se lea como olvido.
  - EL DESFASE DE `PATRONES_ACTA`, que apunta al acta de `VUELTA - 1`. El acta 193
    lo dejo expresamente DESPUES de la bateria de la 194: la 195 es el sitio.
  - `acumulan()` que lea la tabla, o que declare en su salida que no es la sede.
  - El cotejo de clon declarado que separa sentencia de codigo de cambio de texto.
  - La excepcion que publica siempre su lista.
  - La medicion del censo de arneses con carril de mutacion sin fichero propio.
  - Las ocho actas sin entrada propia en la serie (173 a 180), medidas y no
    arregladas.
  - El exitcode 2 propagado a `--componer`.
  - Que el campo `evidencia` de `OP-L-02` nombre los ficheros que ya existen. Su
    ESTADO NO SE MUEVE: sigue en `LISTA`, y declararla HECHA es del fundador.
  - QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO. Lo dejo NOMBRADO y medido en mi
    `4.8` y no resuelto, porque mover una clase esta reservado y eso es del
    RECOMPUTO. El dato que tiene que llegar entero a quien recompute: DOS lectores
    independientes, tu y yo, leimos los mismos 30 con `9.6.1` y los DOS emitimos
    CERO `B` sobre un tramo donde el archivo tiene TRES, en `158`, `612` y `718`.

Y NO SE MUEVE NINGUN VEREDICTO: el `sha256` LF de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en `0a77b5a35a962621`, medido
hoy por mi por las dos convenciones sobre 4054129 bytes. Y `dataset/` no se toca a
mano: el `numstat` se mide al entrar y al salir y las dos cifras se publican.

Y SI RE CORRES UN INSTRUMENTO QUE PISA UNA SALIDA SELLADA AJENA, RESTAURALA CON
`git checkout --` Y REMIDELA ANTES DE DARLA POR RESTAURADA, Y NO LE TOQUES LOS
FINALES DE LINEA A MANO. A mi me paso hoy con
`docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt` y con las selladas del carril de
reproduccion: las restaure y las remedi, y el `git status` quedo limpio.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
