Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 196. Rama `pasada-unica`. FASE III, EJECUCION.

NO ES VUELTA DE BATERIA. La 194 la corrio entera por sus diez tramos y la proxima
cae en la 199, por la cadencia de `AUDITOR.md` 6.1. Tu seccion 9 cierra con el
HUECO DECLARADO Y MEDIDO por el carril de la TAREA 1.b de la vuelta 173, con su
medicion, su atribucion y su corrida. Un hueco declarado no es un hueco escondido.

VAN DOS SUB-TAREAS Y LAS DOS SON BLOQUEANTES, Y TE DIGO POR QUE SON DOS Y NO
CINCO, PORQUE ES LO CONTRARIO DE LO QUE TE ENCONTRASTE LA VUELTA PASADA. Tu propia
remedicion al cierre de la 195 dejo la racha de cierres en 1, no en 9: el
inventario tiene 13 ficheros, la vuelta mas alta es la 195 y dentro del rango
faltan 181, 182, 183 y 194, asi que la racha contada hacia atras desde la mas alta
vale 1. LO RECONTE YO A MANO en esta auditoria y me da lo mismo que a ti.
`AUDITOR.md` 6.2 pide DOS vueltas seguidas cerrando su propio reporte, y con 1 el
tope es de DOS sub-tareas. CUENTALA TU DEL INSTRUMENTO al abrir, con
`scripts/loop/vuelta192_racha_de_cierres.py`, y publica lo que salga. Ese
instrumento PISA su propia sellada: si la corres, restaurala con `git checkout --`
y REMIDELA antes de darla por restaurada.

Y AQUI VA LA PARTE QUE SI ESTA EN TU MANO, EN UNA LINEA: SELLA TU
`docs/loop/SALIDA_V196_CERRAR_REPORTE.txt`. Con eso la racha llega a 2 y el tope de
CINCO vuelve solo en la 197, sin que nadie tenga que adjudicar nada. Tu `P.1`
quedo contestada en la adjudicacion `4.5` de mi acta, a favor de medir el ACTO y no
el fichero, pero NO me apoyo en mi propia adjudicacion para ensanchar tu encargo:
me quedo del lado estrecho hasta que el instrumento lo diga.

ABRE EL REPORTE AL EMPEZAR, con su esqueleto tallado y en su propio commit, y mide
tu desfase de calibrado DENTRO del bloque de apertura y ANTES de la primera
operacion. Tu bloque de apertura corrio el ciclo completo la vuelta pasada y
escribio el mismo los dos literales de la guarda `D.1`: eso funciono y no se
deshace.

Y LO QUE TE AHORRO DE MI AUDITORIA, QUE ES LO MAS UTIL QUE SACO DE ELLA: TU Y YO
LEIMOS LOS MISMOS 60 POR SEPARADO Y FALLAMOS EXACTAMENTE LOS MISMOS CUATRO
PUESTOS. `976`, `2428`, `2662` y `3173`. Yo saque 56 de 60 y tu 54, pero mis cuatro
son un subconjunto de tus seis. Dos lectores independientes que convergen dicen
algo del archivo y no solo de los lectores, y por eso los tres hallazgos de mi
seccion 5 salen de ahi.

=============================================================================
TAREA 1. LOS REGISTROS. BLOQUEANTE.
=============================================================================

El acta 196 entra en la serie con el numero que devuelva
`scripts/loop/serie_de_registros.py`, computado y no tecleado. El acta vive en
`docs/loop/ACTA_AUDITOR.md` a partir de la linea 69019, contada por mi hoy con
`grep -n`; RECUENTALA TU, porque el fichero puede haber crecido.

La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta y no de
aqui:

  - LAS CATORCE ADJUDICACIONES `4.1` a `4.14`, Y LAS CATORCE VAN A FAVOR. Cuatro
    son las discrepancias de mi propia ciega, resueltas a favor del archivo; tres
    son tus preguntas `P.1`, `P.2` y `P.3`, las tres contestadas por extension
    citable; y siete son tus discutibles `D.1` a `D.7`. CERO EN CONTRA, y es la
    SEXTA acta seguida.
  - LOS TRES HALLAZGOS DE LA SECCION 5, que no salen de ningun discutible: el
    encargo que quema puestos de la ciega siguiente (`5.1`), los mismos cuatro
    puestos fallados por dos lectores independientes (`5.2`), y la ciega que no
    puede alcanzar la clase de un puesto cuya correccion se apoya en una fusion
    planeada y no aplicada (`5.3`, medido en el `2662`).
  - UNA CAIDA TUYA, Y ES DE CIFRA PUBLICADA, NO DE REPORTE: `C.E1`. La linea 19
    de tu reporte dice que el bloque `E` del sello de apertura corrio
    `scripts/loop/vuelta193_racha_de_cierres.py`, y ese fichero NO EXISTE en disco
    NI EN NINGUNA RAMA (`git log --all` sobre esa ruta no devuelve nada). Lo que
    corrio de verdad, en la linea 46 de `SALIDA_V195_APERTURA.txt`, es
    `vuelta192_racha_de_cierres.py`, que es el nombre que tu propio reporte usa
    BIEN en sus lineas 809 y 913. Entra por `AUDITOR.md` 4, LA RUTA QUE PROMETE
    PRUEBA ES CIFRA. LA RACHA DE CIFRA PUBLICADA QUEDA EN 1: dos tandas seguidas
    serian PARADA, y por eso se registra con su nombre y no se suaviza. Lo que NO
    es: la corrida se hizo y su cifra es correcta y esta sellada. Lo falso es el
    nombre del instrumento.
  - TUS CUATRO CAIDAS DE METODO (`C.1` a `C.4` de tu seccion 8.1), LAS CUATRO
    CAZADAS DENTRO DE LA VUELTA POR GUARDAS QUE TU MISMO ESCRIBISTE, y NINGUNA
    ACUMULA. Se registran porque la vara es lo que se mide, no lo que llega a
    publicarse, que es tu propio `D.7` y lo adjudique a favor.
  - UNA CAIDA PROPIA MIA, `C.A1`, DE METODO, Y CON SU RACHA EN 2: reconte el
    marcador con `json` a mano en vez de por `AP.marcador()`, que es la misma
    especie que el `C.1` del acta 195. La remedie dentro de la vuelta y
    `AP.marcador()` da lo mismo que mi cuenta. A LA TERCERA, el acta 197 tiene
    que ABRIR con su remedio como tarea bloqueante del propio auditor.
  - LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de
    puestos: 60 aislados, 60 cotejados y DOS QUEMADOS, el `654` y el `719`, que
    salen del credito porque el encargo publico su clase de archivo. La fila de
    caidas propias va PARTIDA EN DOS, las que acumulan y el total del cuerpo.

EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada. Pruebalo re
corriendolo, con la sede medida en bytes antes y despues.

=============================================================================
TAREA 2. LA RELECTURA AL DOBLE DE MI TRAMO. BLOQUEANTE, Y ES DEUDA MIA QUE
PAGAS TU CON EL INSTRUMENTO.
=============================================================================

`AUDITOR.md` 1.2: UNA discrepancia mia cayo FUERA de mi marcado, el `2428`, asi
que EL CREDITO DE MI TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE.

EL TRAMO Y EL DOBLE ESTAN CERRADOS DESDE HOY, computados y no tecleados, en
`docs/loop/_auditor_v196_doble_para_la_197.txt`, para que no se elijan despues de
mirar:

  EL TRAMO son los 60 puestos de `docs/loop/_auditor_v196_ciega_blind.txt`, que
  son los mismos 60 de tu tanda de la 195.
  EL DOBLE son sus 60 vecinos deterministas: 12, 13, 26, 27, 73, 74, 135, 139,
  161, 162, 206, 207, 399, 400, 615, 616, 656, 657, 721, 722, 882, 883, 911, 912,
  979, 980, 981, 982, 1072, 1073, 1212, 1213, 1374, 1379, 1809, 1810, 1820, 1821,
  2033, 2034, 2160, 2161, 2429, 2430, 2663, 2664, 2839, 2840, 2916, 2917, 3073,
  3074, 3092, 3093, 3174, 3180, 3188, 3189, 3332, 3333.

SON CIENTO VEINTE PARES, Y LA CIFRA NO ES UN DESCUIDO: el doble compone. La serie
medida va 30, 60 y ahora 120, porque cada tanda doblada que vuelva a dar una
discrepancia fuera del marcado dobla otra vez. NO CAMBIO LA REGLA, que es del
fundador y esta escrita: la ejecuto y la nombro con su serie para que se vea venir.
Si al medirla te sale que no cabe en una vuelta con sus guardas completas, PARAS Y
LO TRAES con tu cifra delante, en vez de leer 120 mal o leer 60 y llamarlo 120.

QUE HACER:

  a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`
     y NO se copia, con `evitar` cargado de TODO lo consumido y contado de sus
     ficheros, que hoy son CATORCE y dan 621 puestos (561 sin el tramo).
     Recomputalo tu y publica lo que salga: si tu cifra no es 621, publica la tuya
     y di de que ficheros sale. El solape con el tramo y con el universo tiene que
     salir CERO POR CONSTRUCCION, no por suerte.
  b) LEE LOS 120 A CIEGAS, tramo y doble, con `aislador_de_ciega.py`, y escribe tus
     clases ANTES de abrir el destape.
  c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no
     parafraseada, con sus precisiones `9.6.2` y `9.6.3`. Y LLEVATE PUESTOS LOS
     DOS ERRORES QUE TU Y YO COMPARTIMOS, porque son los que mas rinden:
       PRIMERO, LA VARA ES EL SUELO Y NO EL TECHO. Antes de aplicarla pregunta si
       el par pertenece a una familia con REGLA PROPIA ya fijada, porque entonces
       manda la especifica. Yo perdi el `976` por no preguntarlo: su razon cita
       que es la misma A del puesto `712` y que el sub-puro numero 7 lleva cuatro
       pares leidos y los cuatro en A. Y consultar la familia NO quema nada,
       porque las clases de OTROS puestos no son tu sujeto sellado.
       SEGUNDO, LA SEMEJANZA DE LOS IDS NO DECIDE. El banco `9.6.3` dice que el
       tamano del solape no decide y que se pesa el resto y en que lado. Los dos
       perdimos el `2428` (`desarrollar_` contra `desarrollo_`) por dejar que el
       nombre pesara, cuando uno genera y el otro elige y hay ARISTA QUE FALTA
       con direccion.
  d) NO TE SALTES LA `B` NI LA SOBRE EMITAS. Tu emitiste 4 donde el archivo tiene
     1 y el auditor de la 195 emitio 0 donde tenia 1. Yo emiti 1 y acerte. El
     sesgo esta medido en las dos direcciones y las dos son perdida.
  e) PUBLICA EL COTEJO con sus cifras: cuantos coinciden, cuantos discrepan, y
     cuales caen dentro y fuera de tu marcado. Marca tus discutibles ANTES de
     saber si aciertas.
  f) Y SI ALGUN PUESTO DE LOS 120 RESULTA INALCANZABLE A CIEGAS por lo que mi
     hallazgo `5.3` describe, o sea que su clase se apoya en una fusion planeada
     y NO aplicada al grafo y la ciega te ensena los pasos del nodo viejo,
     DECLARALO CON SU NUMERO Y SU MEDICION y sacalo de tu credito, como yo saque
     los dos quemados. NO lo arregles por tu cuenta: tocar el aislador o mover una
     clase no es de esta vuelta.

=============================================================================
LO QUE NO ENTRA, DICHO PARA QUE NO SE COLE NI SE REDESCUBRA
=============================================================================

Ni cribado, ni recomputo, ni operaciones del plan, ni las mesas anotadas, ni podar
la nomina, ni la bateria entera, que no es su vuelta y cae en la 199.

Y ESTAS SIGUEN FUERA, EN ESTE ORDEN, PARA QUE LA 197 NO LAS REDESCUBRA. Las tres
primeras son las que yo pondria delante si el tope subiera a cinco:

  - QUE `cerrar_reporte.py` ESCRIBA SU PROPIA SALIDA SELLADA. Es el remedio de tu
    `P.1` y de mi adjudicacion `4.5`, y es codigo, no doctrina. Mientras el
    fichero lo tenga que redirigir alguien a mano, el instrumento mide la memoria
    del ejecutor y no la racha, que es tu propia frase y tienes razon.
  - EL TOPE DE 80 LINEAS DEL MODO AUSTERO, ADJUDICADO EN MI `4.7` Y EN CONTRA
    TUYA. El tope se mide sobre la prosa que escribes A MANO y no sobre la
    cabecera ni las tablas talladas, que la propia regla nombra como contenido
    que se queda. Pero tu reporte de la 195 mide 995 lineas por `split` y 994 por
    `count(NL)`, y las piezas talladas son una fraccion minima: bajo las dos
    lecturas esta muy por encima. NO lo registro como caida porque preguntaste en
    vez de romperlo en silencio. Lo que queda encargado es MEDIR tu reporte por
    las dos varas y publicar las dos cifras, y bajar la prosa de acompanamiento
    que el registro ya dice.
  - LA GUARDA DE LA `P.2`, ADJUDICADA A FAVOR EN MI `4.6` Y CON SU CALIBRADO
    ANTES QUE SUS DIENTES: que la huella de vivo no case con `open(`, `io.open(`
    ni `read_text`. En su PRIMERA vuelta la guarda PUBLICA SU LISTA y NO detiene a
    nadie, y solo muerde cuando su lista salga vacia sobre los cinco arneses de
    hoy. Tu propio miedo esta bien puesto y por eso va asi.
  - EL DESFASE DE `PATRONES_ACTA`, que apunta al acta de `VUELTA - 1`. Lleva
    cuatro encargos en primer lugar de la cola y sigue sin hacerse; lo digo con su
    numero en vez de dejarlo caer otra vez. Es cosmetica de cabecera y por eso
    pierde contra las tres de arriba, pero cuatro aplazamientos ya son un patron.
  - LA FILA DE CREDITO DEL ACTA CON SU ROTULO IMPUESTO POR EL INSTRUMENTO que la
    talla. A mano ya la aplicamos el acta 195 y yo.
  - LA GUARDA DE CODIGO DEL HALLAZGO `5.3` DEL ACTA 194, los mensajes de commit
    sin clases por puesto ni reparto de ciega. A mano funciona y esta medido: mis
    60 llegaron con CERO QUEMADOS por esa via.
  - EL REMEDIO DE MI HALLAZGO `5.1`: que un encargo que ensene la leccion de un
    puesto vivo en la cola nombre su FIGURA y no su CLASE. Es de una linea de
    disciplina y no de codigo, y lo aplico yo mismo en esta TAREA 2 (por eso el
    `976` y el `2428` van con su figura y su razon, que ya estan destapados, y no
    hay ningun puesto de tus 120 cuya clase te haya dicho).
  - `acumulan()` que lea la tabla, o que declare en su salida que no es la sede.
  - El cotejo de clon declarado que separa sentencia de codigo de cambio de texto.
  - La excepcion que publica siempre su lista.
  - La medicion del censo de arneses con carril de mutacion sin fichero propio.
  - Las ocho actas sin entrada propia en la serie (173 a 180), medidas y no
    arregladas.
  - Que el campo `evidencia` de `OP-L-02` nombre los ficheros que ya existen. Su
    ESTADO NO SE MUEVE: sigue en `LISTA`, y declararla HECHA es del fundador.
  - QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO, y ahora tambien LOS CUATRO PUESTOS
    QUE DOS LECTORES INDEPENDIENTES FALLARON (`976`, `2428`, `2662`, `3173`), que
    son mi hallazgo `5.2`. Los dejo NOMBRADOS y medidos y NO resueltos, porque
    mover una clase esta reservado y eso es del RECOMPUTO. El marcador de hoy,
    recomputado por mi con `AP.marcador()`: `A 551, B 72, C 5, D 2760` sobre 3388
    filas, cero huecos y cero duplicados.

Y NO SE MUEVE NINGUN VEREDICTO: el `sha256` LF de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` tiene que abrir y cerrar en
`0a77b5a35a962621`, que es lo que medi hoy por las dos convenciones sobre 4054129
bytes. Y `dataset/` no se toca a mano: el `numstat` se mide al entrar y al salir y
las dos cifras se publican. El ciclo de Gate 0 se corre ENTERO, con
`run_phase1.py --reaplico-curaduria` y despues `etiquetas_de_cara.py --aplicar`:
corrido por mi hoy, asi da CERO lineas en `dataset/`, `web/` y `engine/`. La nomina
NO se poda: sigue en 135 entradas con `CASOS_DECLARADOS` en 2, medido por mi.

Y SI RE CORRES UN INSTRUMENTO QUE PISA UNA SALIDA SELLADA AJENA, RESTAURALA CON
`git checkout --` Y REMIDELA ANTES DE DARLA POR RESTAURADA, Y NO LE TOQUES LOS
FINALES DE LINEA A MANO.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
