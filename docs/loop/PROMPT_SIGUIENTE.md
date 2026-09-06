Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Corre tu bloque de apertura ANTES de la primera operacion, como siempre, y mide
en el su desfase de calibrado en su sitio.

ESTA VUELTA ES LA CONTINUACION DE LA 183, Y ESO MANDA SOBRE LA COSTUMBRE. La 183
se corto en el TRAMO 2 DE 9 de su bateria. NO ABRAS UN REPORTE NUEVO, NO ARCHIVES
`docs/loop/REPORTE.md` Y NO TALLES NINGUN ESQUELETO: sigue escribiendo EN EL
MISMO `docs/loop/REPORTE.md` de la 183, que crece por anexion y ya tiene su TAREA
1 cerrada y su TAREA 2 abierta. El motivo esta medido en la adjudicacion 5.7 del
acta 183 y son dos reglas escritas sumadas: `cerrar_reporte.py` exige
`--bateria docs/loop/SALIDA_V183_BATERIA.txt`, que solo existe cuando `--componer`
junta los NUEVE tramos, y `AUDITOR.md` 6.1 manda que una vuelta cortada retome en
el tramo siguiente. Si abres reporte propio y archivas el de la 183 sin cerrar,
el disparador del regimen 6.2 no se puede cumplir nunca.

TAREA 1. LOS REGISTROS Y LA CORRECCION DE LA ATRIBUCION, BLOQUEANTE Y ANTES DE
TOCAR LA BATERIA.

(a) El acta 183 entra en la serie con el numero que devuelve
`scripts/loop/serie_de_registros.py` y NO tecleado (al cerrar la 183 el siguiente
libre era `R.45`, pero se vuelve a preguntar y se usa lo que conteste hoy), con
sus siete adjudicaciones `5.1` a `5.7`, la caida del ejecutor `E.1`, las CERO
caidas propias del auditor y su caso por mutacion.

(b) LA CORRECCION DEL `E.1`, QUE ES LA OPERACION DE CODIGO DE ESTA VUELTA Y VA
ANTES DE SELLAR UN SOLO TRAMO MAS. `scripts/loop/vuelta183_bateria_por_tramos.py`
imprime en sus salidas selladas que la bateria es la de la VUELTA 176 y que la
lanzo el fichero de la 176. Las dos cosas son falsas y ya salieron impresas en
cuatro ficheros sellados. Vive en sus lineas 181, 217 y 218, y volveria a salir
en la cabecera de la composicion por sus lineas 359 y 360. Las cifras y la
atribucion SE COMPUTAN DEL PROPIO FICHERO, no se teclea un 183 encima de un 176:
el numero de vuelta y el nombre del lanzador salen de `os.path.basename` y de la
constante que ya reparte los tramos, de modo que un clon futuro no vuelva a
heredar el numero de su padre. LO QUE PASABA ANTES NO SE BORRA, SE CUENTA:
publica la cuenta de menciones de `176` en las cuatro salidas selladas de hoy
(`grep -c` da 3 en cada una) antes de arreglarlo. CON CASO POSITIVO POR MUTACION
SOBRE VARIABLE COMPUTADA: el arnes tiene que CAER si alguien vuelve a clavar el
numero de vuelta como literal.

(c) LOS TRAMOS 1 Y 2 SE VUELVEN A CORRER DESPUES DE (b), Y SE DICE POR QUE. El
regimen 6.1 pide que los nueve tengan salida sellada DEL MISMO CALIBRE, y dos
salidas que se atribuyen a otra vuelta no son del mismo calibre que siete que se
atribuyen bien. NO CONTRADICE "lo corrido queda corrido": esa regla protege el
trabajo cuando la vuelta se corta, y aqui el coste medido de rehacer los dos es
2,1 mas 5,6 igual a 7,7 minutos sobre una bateria estimada en 36,6 a 47,7. Se
publica ese coste medido al lado de la decision.

(d) LAS TRES RUTAS DE LA CELDA "donde vive la prueba" DE LA TAREA 1 SE ESCRIBEN
ENTERAS: `_T1A_MUTACION_REGISTRO.txt`, `_T1C_MUTACION_VEREDICTO.txt` y
`_T1E_RELECTURA_AL_DOBLE.txt` van con su prefijo `SALIDA_V183` y su carpeta. No
es una caida y el acta 183 lo adjudica a tu favor en su 5.2; se corrige porque
una ruta abreviada no se puede pegar en un comando para cotejarla.

(e) `scripts/loop/_v183_tallar_cierre.py` (18.855 bytes) esta sin seguir por git.
NO SE BORRA: se commitea, porque es el tallador del cuerpo del cierre que esta
vuelta va a necesitar.

(f) LA RELECTURA AL DOBLE DEL TRAMO DE MI CIEGA, por `AUDITOR.md` 1.2, porque mi
discrepancia salio fuera del marcado. Los 30 puestos son los de
`docs/loop/_auditor_v184_ciega_blind.txt`, y se leen de ahi cotejando antes su
`sha256` contra `docs/loop/SELLO_APERTURA_AUDITOR_V184.json` (43.593 bytes,
`sha256` `217077af6ea96a18`); si no calzan, no se relee nada y se dice. Mas sus 30
vecinos deterministas, mecanica y con la vara, SIN volver a decidir la clase de
ningun par.

TAREA 2. LA BATERIA, HASTA LOS NUEVE, Y EL CIERRE DEL REPORTE DE LA 183.

Con (b) ya puesto: corre los tramos 1 y 2 otra vez y luego del 3 al 9, con
`scripts/loop/vuelta183_bateria_por_tramos.py --tramo N`. Cual toca lo dice
`--siguiente` y no la memoria. CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL
TERMINAR, antes de seguir con el siguiente. Una salida sellada que mide CERO
BYTES no cuenta como hecha. La doble corrida y todas las demas guardas siguen
enteras: no se afloja ninguna, solo cambia la cadencia, y LA NOMINA NO SE PODA.
El reloj de cada tramo se mide al cerrarlo y se publica medido; la estimacion del
`--plan` es estimacion y se dice como tal. Si un arnes cae en rojo, te detienes
ahi y lo traes con su salida entera.

Cuando los nueve tengan salida sellada no vacia: `--componer` para producir
`docs/loop/SALIDA_V183_BATERIA.txt`, y con esa pieza CIERRA EL REPORTE DE LA 183
con `scripts/loop/cerrar_reporte.py` y ARCHIVALO. El veredicto de una linea lo
talla el cierre y sus numerales tienen que calzar con lo que el cuerpo permite
contar: la guarda que la TAREA 1.c de la 183 puso cae en rojo y no escribe nada
si no calzan, y esa guarda esta corrida y verificada por el auditor.

Mide `git diff --numstat -- dataset/` al entrar y al salir de cada tramo, y
publica las dos cifras: la bateria muta `dataset/` de verdad y si se corta te
deja el catalogo sucio.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
