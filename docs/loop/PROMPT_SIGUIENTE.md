Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 192. Rama `pasada-unica`. FASE III, EJECUCION.

NO ES VUELTA DE BATERIA. La 189 la corrio entera y por `AUDITOR.md` 6.1 la
siguiente cae en la 194. La seccion 9 de tu reporte cierra con el HUECO
DECLARADO Y MEDIDO por su carril, con su nombre, sus bytes medidos y su
atribucion, LAS TRES JUNTAS. Un hueco declarado no es un hueco escondido.

VAN CINCO SUB-TAREAS y DOS SON BLOQUEANTES. El tope de CINCO sigue vigente y no
hace falta volver a ganarlo. Y la cifra que lo sostiene la remedi en vez de
heredarla: los ficheros `SALIDA_V<n>_CERRAR_REPORTE.txt` existen para la 186, la
187, la 188, la 189, la 190 y la 191, o sea SEIS vueltas seguidas, una mas que
las cinco que salen de contar desde la 187 como venia haciendo el acta 191.
CUENTALO TU DEL INSTRUMENTO y publica lo que salga, que para eso lo dejo medido
y no cerrado.

ABRE EL REPORTE AL EMPEZAR, con su esqueleto tallado y en su propio commit, y
mide tu desfase de calibrado DENTRO del bloque de apertura y ANTES de la primera
operacion. Una columna de apertura medida al cierre es caida que ACUMULA.

=============================================================================
TAREA 1. LOS REGISTROS. BLOQUEANTE.
=============================================================================

El acta 192 entra en la serie con el numero que devuelva
`scripts/loop/serie_de_registros.py`, computado y no tecleado (hoy el siguiente
libre es `R.54`, pero lo dice el instrumento, no este encargo).

La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta, no de
aqui:

  - LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, y las diez van A FAVOR: siete son
    los discutibles del ejecutor (`D.1` a `D.7`, y ojo con la numeracion, que en
    el reporte de la 191 el `D.7` va escrito ANTES del `D.6`) y las tres
    restantes son las preguntas y los pendientes de doctrina contestados. Otra
    vez CERO EN CONTRA, y tu registrador ya sabe contarlo sin romperse: no
    vuelvas a probarlo por mutacion si el arnes de la 191 ya lo cubre, y si lo
    cubre, DILO CON SU FICHERO en vez de re fabricarlo.
  - LOS TRES HALLAZGOS DE LA SECCION 5, que no salen de ningun discutible: los
    dos arneses de la 191 que salen `SUJETO VIVO` antes de entrar en la nomina
    (`5.1`), la cuarta puerta del sello de la apertura (`5.2`), y el segundo
    dato independiente sobre la marca contra la dificultad (`5.3`).
  - DOS CAIDAS PROPIAS DEL AUDITOR, y UNA DE ELLAS ES DE CIFRA PUBLICADA: la
    `C.1` es la cifra falsa de mi propia acta 191 (la etiqueta duplicada NO era
    nueva de la 190: el `REPORTE_V188.md` la trae en su linea 56), corregida por
    DECLARACION; la `C.2` es de metodo, que queme dos de mis treinta sujetos de
    ciega. Las dos van escritas como dos y ninguna se omite.
  - CERO caidas del ejecutor que acumulen, con las SEIS de metodo que el reporte
    de la 191 declara registradas como tales.
  - LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de
    puestos con su nota: 30 aislados y 28 cotejados, y los 28 son SOLAPE TOTAL a
    proposito, o sea control y no cobertura nueva.

EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada. Pruebalo re
corriendolo, con la sede medida en bytes antes y despues.

=============================================================================
TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DE LA 191. BLOQUEANTE.
=============================================================================

ES LA DEUDA DE CREDITO DE MI PROPIA TANDA Y LA ENCARGO YO, que es donde
`AUDITOR.md` 1.2 la pone. Y esta vez el motivo es DOBLE: el puesto `2832` cayo
FUERA de los dudosos marcados de DOS lectores independientes en DOS tandas
seguidas, la tuya de la 191 y la mia de la 192.

QUE TRAMO. Los 30 puestos de `docs/loop/SALIDA_V191_T2_CIEGA.txt`, que son los
mismos 30 de mi ciega `docs/loop/_auditor_v192_ciega_blind.txt`. Lo mido y lo
digo para que no lo busques: son el mismo conjunto.

QUE ES AL DOBLE. Sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada. 30 del
tramo mas 30 vecinos son 60: el doble exacto.

EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO. A `vecinos()` se le pasa
`evitar` con TODO lo consumido, que hoy son 501 puestos: los 471 que la 191 ya
conto de sus ficheros MAS los 30 de su propia tanda. CUENTALO TU DE SUS
FICHEROS, NO DE ESTA CIFRA, y publica el conteo con los nombres de los ficheros
de los que sale. Solape con el propio tramo y con el universo consumido: 0 y 0,
POR CONSTRUCCION.

COMO SIEMPRE: `scripts/loop/aislador_de_ciega.py`, criterio escrito literal,
ciega y destape en ficheros SEPARADOS, tus clases escritas y COMMITEADAS en su
propio commit ANTES de abrir el destape, y tus dudosos NOMBRADOS DELANTE.
Publica cuantos coinciden, cuantos discrepan, cuantos dentro y cuantos fuera de
tus dudosos.

Y UNA COSA MAS, QUE SALE MEDIDA DE MI ACTA Y NO DE UNA CORAZONADA: mis tres
discrepancias fueron SUBCONJUNTO EXACTO de tus siete. Si en este doble vuelve a
pasar que un tramo tumba a los dos lectores en los mismos puestos, DILO CON SUS
NUMEROS, porque es la unica via barata que tenemos de separar el par dificil del
lector distraido.

NO SE TOCA NINGUNA CLASE. `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en
lectura y su `sha256` LF abre y cierra en `0a77b5a35a962621` por las dos
convenciones. Si de la relectura sale una correccion, se declara y se trae; no
se escribe ni una fila.

=============================================================================
TAREA 3. LOS DOS ARNESES `SUJETO VIVO` DE LA 191, ANTES DE QUE ENTREN EN LA
NOMINA. BLOQUEANTE, Y LO ES POR LA BATERIA DE LA 194.
=============================================================================

ES MI HALLAZGO `5.1`, Y NO ES UNA SOSPECHA: esta corrido con la guarda de la
casa y medido en `docs/loop/_auditor_v192_sujeto_vivo.txt`.

LO QUE MEDI. Sobre la nomina de hoy, 127 entradas,
`guarda_del_sujeto_congelado_separada()` da `sujeto_vivo 0` y `sin_motivo 0`,
que es lo que el acta 191 dejo dicho y sigue siendo cierto. Sobre los DOCE
arneses de la vuelta 191, que hoy NO estan en la nomina y que entran por la
regla de entrada del propio fichero, da `sujeto_vivo 2` y `sin_motivo 6`. Los
dos vivos son `vuelta191_tarea1a_registrar_acta191.py` y
`vuelta191_tarea3_arreglar_lineas.py`.

Y LA CONFIRMACION EMPIRICA, QUE ME SALIO SIN BUSCARLA: re corri tus tres arneses
de mutacion y DOS de sus salidas selladas NO reprodujeron byte a byte. La de la
TAREA 3 pasa de 5836 a 6559 bytes porque censa el repo de hoy y desde entonces
nacieron seis ficheros; la de la TAREA 4 cambia porque `cerrar_reporte.py` paso
de 112413 a 114466 bytes durante tu propio cierre. LAS RESTAURE EN LF Y LAS
REMEDI (5836 y 6072, identicas a su commit) y mis dos cortes nuevos quedan al
lado con su nombre.

QUE HACER:

  a) CORRE TU LA GUARDA y publica sus tres listas sobre los doce arneses de la
     191, con sus nombres. Si tu medicion no da 2 y 6, la tuya manda y la mia se
     declara equivocada: para eso se publica el comando.
  b) ARREGLA LOS DOS `SUJETO VIVO` para que su sujeto quede CONGELADO, o
     DECLARA EL CASO en el propio arnes por el carril que la casa ya tiene para
     los `CASO DECLARADO`. La `4.4` del acta 191 ya adjudico que `SUJETO VIVO`
     es FALLO y no deuda, asi que dejarlos como estan no es una opcion que yo
     pueda adjudicar.
  c) LOS SEIS `sin_motivo` NO SON FALLO PERO SI SON DEUDA: nombra los seis y di,
     por cada uno, si su sujeto esta vivo de verdad o si solo le falta escribir
     el motivo. No los arregles a ciegas.
  d) NO TOQUES LA NOMINA. No se poda, no se adelanta y no se le meten entradas
     nuevas en esta vuelta: la opcion `c` que el fundador RECHAZO el 5 sep 2026
     sigue rechazada, y quien mete a los doce en la nomina es la regla del
     fichero, no tu.
  e) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes con sujeto vivo
     vuelve a colarse hacia la nomina sin declararse.

POR QUE ES BLOQUEANTE Y NO PUEDE ESPERAR A LA 194: la bateria compara salidas
selladas del mismo calibre, y una salida que no reproduce por sujeto vivo
convierte una corrida legitima en un rojo que nadie sabra leer. Se arregla
ANTES, no dentro.

=============================================================================
TAREA 4. LA CUARTA PUERTA DEL SELLO DE LA APERTURA DEL AUDITOR.
=============================================================================

ES MI HALLAZGO `5.2`, Y LO LEVANTO CONTRA MI MISMO, porque soy el que se colo
por esa puerta esta misma vuelta.

EL CASO, MEDIDO. `scripts/loop/apertura_del_auditor.py` impide tocar `git log`,
`git status` y `REPORTE.md` antes del sello, y eso FUNCIONO: mi bitacora salio
vacia y mi sello es verde. Pero EL SUJETO DE LA CIEGA NO VIVE EN NINGUNO DE LOS
TRES: vive en las razones y las clases de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.
Buscando la leyenda de las clases corri una consulta sobre ese archivo que me
imprimio las razones de dos puestos de mi propia tanda, el 156 y el 201, CON EL
SELLO YA ESCRITO Y SIN ROMPER NINGUNA GUARDA. Los saque del cotejo y lo declare
antes de contar, pero el remedio no puede ser que el auditor se acuerde: esa es
justo la enfermedad que el fichero vino a curar.

QUE HACER:

  a) AL SELLO SE LE ANADE LA CUARTA PUERTA: una funcion del propio fichero para
     leer `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` que APUNTE SU TOQUE, y una
     comprobacion que CAIGA EN ROJO si el turno leyo `clase` o `razon` DE LOS
     PUESTOS SELLADOS antes de que las clases del auditor esten escritas. No se
     prohibe leer el archivo entero, que hace falta para el marcador: se
     prohibe destapar el sujeto.
  b) DI EN EL PROPIO FICHERO LO QUE ESTA GUARDA NO PUEDE HACER, como su
     docstring ya hace con las otras tres: no puede impedir que alguien abra el
     jsonl por su cuenta en su terminal. Lo que si puede es que el sello no se
     pueda escribir despues, y que quien se la salte lo haga a sabiendas.
  c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si la cuarta puerta se quita.
  d) NO SE CLONA EL FICHERO. `apertura_del_auditor.py` tiene nombre estable y
     sin numero de vuelta, como sus hermanos: se le anade, no se le hace una
     version 2.

=============================================================================
TAREA 5. EL FORMATO UNICO DEL COTEJO DE CIEGA. ES TU `P.2`, ADJUDICADA A FAVOR.
=============================================================================

TU TAREA 5 MIDIO QUE EL UNIVERSO SE QUEDA EN 6 FICHEROS DE 43, y tus palabras
son las que adjudico: mientras eso siga asi, ninguna medicion sobre la historia
de ciegas va a alcanzar para concluir nada. Tres cotejos de ciega DE VERDAD (los
del 183, 184 y 190) quedan fuera por formato y no por fondo.

QUE HACER, Y ES UN FORMATO ANTES QUE UNA RE MEDICION:

  a) ESCRIBE EL FORMATO UNICO del cotejo de ciega, con nombre estable y sin
     numero de vuelta, y que sea el que produzcan las ciegas de aqui en
     adelante. Que lleve, como minimo y explicitos: el puesto, la clase del
     lector, la clase del archivo, si el puesto estaba en los dudosos del
     lector, y el COINCIDE o DISCREPA. El denominador tiene que quedar
     recuperable: dos de los seis ficheros de hoy solo listan discrepancias y
     por eso no se sabe sobre cuantos se midieron.
  b) UN LECTOR QUE LEA LOS FORMATOS VIEJOS y publique CUANTOS de los 43 pasa a
     recuperar, con sus nombres, y cuantos siguen fuera y por que. Publica la
     cifra de antes (6) y la de despues, las dos juntas.
  c) NO RE MIDAS LA MARCA CONTRA LA DIFICULTAD EN ESTA VUELTA. El universo
     nuevo se usa cuando este medido y declarado, no en la misma vuelta en que
     se construye: elegir el universo y sacar la conclusion en el mismo acto es
     exactamente lo que tu TAREA 5 evito bien.
  d) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un cotejo del formato nuevo
     no permite recuperar el denominador.

=============================================================================
LO QUE NO ENTRA, DICHO PARA QUE NO SE COLE NI SE REDESCUBRA
=============================================================================

Ni cribado, ni recomputo, ni operaciones del plan, ni las mesas anotadas, ni
podar la nomina (la opcion `c` que el fundador RECHAZO el 5 sep 2026), ni la
bateria, que cae en la 194.

Y SIGUEN FUERA, NOMBRADAS PARA QUE LA 193 NO LAS REDESCUBRA:

  - EL DESFASE DE `PATRONES_ACTA`, que apunta al acta de `VUELTA - 1` y por eso
    la cabecera cita el acta 190 en vez de la 191. Tu reporte lo declara como
    SEPTIMA vuelta, contado de su propia linea, y NO se arregla todavia: toca
    `tallar_cabecera_reporte.py`, que
    CUATRO entradas de la nomina nombran, y moverlo antes de la bateria de la
    194 pone en riesgo una corrida por algo que no es un fallo. SE ENCARGA
    DESPUES DE LA 194, y lo digo aqui para que no se lea como olvido. Tu `D.7`
    acerto en no tomarlo y lo adjudique a favor por eso.
  - `acumulan()` que lea la tabla, o que declare en su salida que no es la sede.
  - El cotejo de clon declarado que separa sentencia de codigo de cambio de
    texto.
  - La excepcion que publica siempre su lista.
  - La medicion del censo de arneses con carril de mutacion sin fichero propio.
  - Las ocho actas sin entrada propia en la serie (173 a 180), medidas y no
    arregladas.
  - El exitcode 2 propagado a `--componer`, adjudicado A FAVOR en la 4.9 del
    acta 191 y que sigue sin entrar.
  - Que el campo `evidencia` de `OP-L-02` nombre los ficheros que ya existen,
    adjudicado en la 4.7 del acta 191. Su ESTADO NO SE MUEVE: sigue en `LISTA`,
    y declararla HECHA es del fundador.

Y NO SE MUEVE NINGUN VEREDICTO: el `sha256` LF de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en el mismo valor, y
`dataset/` no se toca a mano: el `numstat` se mide al entrar y al salir y las
dos cifras se publican.

Y SI RE CORRES UN INSTRUMENTO QUE PISA UNA SALIDA SELLADA AJENA, RESTAURALA EN
LF Y REMIDELA ANTES DE DARLA POR RESTAURADA. Me volvio a pasar a mi en esta acta
con DOS de tus salidas, y las dos veces la orden obvia habria dejado la cifra
cambiada. El corte nuevo, si interesa, va al lado con su nombre y su vuelta,
nunca encima.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
