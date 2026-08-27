# -*- coding: utf-8 -*-
"""tallar_cabecera_reporte.py . TALLA LA TABLA DE COMPROBACIONES DE LA CABECERA
DEL REPORTE (apertura y cierre), CON CADA CELDA LEIDA DE LA SALIDA QUE LA CITA.

NOMBRE ESTABLE A PROPOSITO: no lleva numero de vuelta. La vuelta se pasa con
--vuelta y el prefijo de las salidas se arma solo (SALIDA_V<N>_...), asi que
este fichero NO se clona cada vuelta. Sucesor declarado de
scripts/loop/vuelta56_registro_tramo.py, cuya maquina se copia entera: LAS
CIFRAS SE EXTRAEN POR EXPRESION REGULAR de las salidas del dia y el tallador
CAE EN ROJO, sin escribir nada, si alguna celda no se puede leer.

POR QUE NACE (decision del fundador, 20 ago 2026, opcion b): las TRES caidas de
la racha de reporte de las vueltas 54, 55 y 56 fueron frases TECLEADAS en la
cabecera, ninguna salio de un tallador. La de la vuelta 56 es el ejemplar
exacto: la celda de las cuatro comprobaciones al CIERRE publicaba "623 igual a
623", que es la cifra de la APERTURA heredada; el instrumento del cierre dice
529. El registro del tramo ya se tallaba desde la vuelta 55; la cabecera del
reporte no, y ahi es donde caian.

LA DIFERENCIA CON EL TALLADOR DEL REGISTRO, y es la que motiva este fichero:
aquel talla UNA tabla de cierre para docs/plan/03_FUSIONES.md; este talla LAS
DOS COLUMNAS de la cabecera del reporte, apertura y cierre POR SEPARADO, cada
una con SUS CUATRO COMPROBACIONES medidas de SU PROPIA salida de recomputo. Un
lado no puede heredar del otro porque cada lado se lee de su fichero.

USO:
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 56
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 56 --comparar docs/loop/REPORTE.md
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 56 --sin-miles

--comparar RUTA extrae la tabla de cabecera que ese fichero YA tiene y la coteja
fila a fila contra la tallada, nombrando cada celda que difiera. Es el modo con
el que se prueba que la celda mala de una vuelta vieja sale distinta del
tallador, y que una cabecera ya tallada sale identica a si misma.

FORMATO: los millares se escriben con punto (3.388), que es el estilo que la
cabecera del reporte ya usa. Con --sin-miles salen crudos como el instrumento
los imprime. Es lo unico que este tallador decide sobre la forma; el resto es
copia literal de lo medido.

SALIDA: exit 0 si talla (y si, con --comparar, no hay diferencias); exit 1 si
alguna celda no se pudo leer o si la comparacion encuentra diferencias.

--- LA IDENTIDAD SE LEE DE GIT (ESCALADA AUTOMATICA, vuelta 80) ---

POR QUE NACE (decision del fundador, 26 ago 2026, opcion b, disparada por la
racha de reporte llegando a TRES tandas seguidas, vueltas 77, 78 y 79): la
vuelta 79 tallaba ya las seis filas de la cabecera (censo, Gate 0, aristas,
motor, web, tsc) pero la LINEA DEL COMMIT DE APERTURA seguia siendo prosa
suelta tecleada encima de la tabla, y ahi cayo la tercera caida: el reporte
de la vuelta 79 publico `43b02413` (el commit de su propia TAREA 4) como
"commit de apertura", cuando el commit de apertura real era `aea7cc81` (el
acta de la vuelta 78).

En modo `--fase04`, el tallador ahora lee TAMBIEN el commit de apertura,
como UNA FILA MAS de la tabla, con la misma mecanica de ROJO que las seis
filas de arriba: se busca en `git log` de la rama actual el commit cuyo
mensaje EMPIEZA por "ACTA DE LA VUELTA <vuelta-1> DEL AUDITOR" (el patron
exacto que todo acta de auditor usa); si no hay NINGUNO, o si hay MAS DE
UNO (ambiguo), el tallador cae en ROJO y no talla nada. Nunca inventa un
hash. La rama se lee de `git rev-parse --abbrev-ref HEAD` (no se pide por
argumento, para que no se pueda teclear una rama distinta de la real).

USO:
  python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 79
  python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 78 --comparar docs/loop/REPORTE.md

CASO POSITIVO OBLIGATORIO (vuelta 80), contra la vuelta 79: tallar la vuelta
79 tiene que dar como commit de apertura `aea7cc81` y NO `43b02413`.

LO QUE ESTA REGLA TODAVIA NO CUBRE, Y SE DICE EN VEZ DE CALLARLO: la regla
del fundador (EJECUTOR.md, "LA IDENTIDAD SE LEE DE GIT") alcanza a TODO hash,
nombre de commit, rama o fecha de apertura o de cierre. Esta vuelta talla el
COMMIT DE APERTURA porque fue el que causo la caida y el unico que el
encargo pedia. La RAMA se talla como dato de apoyo (se lee de git, no se
teclea) pero NO como fila propia comparable con su propio ROJO: no hay una
segunda rama contra la que fallar. EL COMMIT DE CIERRE y la FECHA DE
APERTURA/CIERRE quedan FUERA de este tallador: el commit de cierre de una
vuelta no existe todavia en el momento en que el tallador corre (el reporte
que lo cita es, el mismo, parte de ese commit), asi que no hay como leerlo
de git sin inventarlo. Mientras el reporte necesite nombrar un commit de
cierre, lo hace citando los commits de tarea ya creados (que si existen), no
un hash unico de cierre.

--- MODO --fase04 (ESCALADA AUTOMATICA, vuelta 79) ---

POR QUE NACE (decision del fundador, 26 ago 2026, opcion b, disparada por la
racha de reporte volviendo a DOS tandas seguidas, vueltas 77 y 78): el modo de
arriba lee salidas DEL CRIBADO (`SALIDA_V<N>_MARCADOR_*`,
`SALIDA_V<N>_RECOMPUTO_*`), y la fase 04 (ENLACES) no produce ninguna de las
dos. Desde que el bucle entro al tramo mecanico, las cifras de la cabecera del
reporte volvieron a teclearse a mano. `--fase04` talla la cabecera propia de
esa fase, apertura y cierre por separado, cada celda leida de SU PROPIA salida
del dia:

  - censo del grafo y las tres comprobaciones de Gate 0: `SALIDA_V<N>_GATE0_CMD1_<LADO>.txt`
  - las cuatro cifras de aristas: `SALIDA_V<N>_CONTEO_<LADO>.txt`
  - el motor: `SALIDA_V<N>_MOTOR_<LADO>.txt`
  - la web: `SALIDA_V<N>_WEB_<LADO>.txt`
  - el tsc: `SALIDA_V<N>_TSC_<LADO>.txt`
  - el marcador del cribado: `SALIDA_V<N>_MARCADOR_<LADO>.txt`, SOLO si la
    vuelta lo produce (no es obligatorio: la fase 04 no toca el cribado)

USO:
  python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 79
  python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 78 --comparar docs/loop/REPORTE.md

Misma mecanica que el modo de cribado: ROJO sin escribir nada si una celda
obligatoria no se puede leer; `--comparar` coteja fila a fila la tabla que el
fichero YA tiene contra la tallada. El marcador es la unica fila opcional: si
no hay `SALIDA_V<N>_MARCADOR_*` para esa vuelta, la fila simplemente no se
imprime (no es una celda rota, es una fase que no toco el cribado).

--- TAREA 2.a: LA TABLA DE LA CADENA SE TALLA, NO SE TECLEA (vuelta 81) ---

POR QUE NACE (acta de la vuelta 80, seccion 4: caida de reporte FUERA del
marcado). El reporte de la vuelta 80 publico a mano, en su tabla de las 10
lecturas frescas del tramo 6, una columna "alcanzable previo (vara de la
cadena)" que CONTRADIJO la salida del instrumento que la propia columna
nombra (`SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt`): la fila 27 publico
"no" donde el instrumento imprimio YA ALCANZABLE (6 saltos); la fila 28
publico "si, en direccion inversa" donde el instrumento imprimio sin camino
previo. Es la misma especie que motivo la cabecera: una tabla que un
instrumento YA produce y que alguien volvio a teclear.

`--tramo-cadena K` (combinado con `--vuelta N`) lee
`SALIDA_V<N>_TRAMO<K>_FILTRO_P91_GUARDA_CADENA.txt`, localiza la seccion
"CABEZA DE LA BOLSA FILTRADA" y talla, por cada UNIDAD que ese fichero trae
(sueltas y parejas), UNA SOLA columna: si hay o no camino previo, y con
cuantos saltos. "YA ALCANZABLE (N saltos)" se talla como "ALCANZABLE (N
saltos)"; "sin camino previo" se talla como "SIN CAMINO PREVIO". SI EL
FICHERO NO EXISTE O UNA UNIDAD NO SE PUEDE LEER, NO TALLA NADA Y SALE CON
EXIT 1 (misma mecanica de ROJO que las demas filas).

LA COLUMNA CONTESTA UNA SOLA PREGUNTA, la que su titulo dice (alcanzabilidad
previa). NO dice si ese camino es o no LA CADENA PROPIA de la madre (sus
pasos enumerados, en su propio orden): esa es una decision de LECTURA, ajena
a este instrumento, y por eso no se mezcla en esta columna (distincion que el
acta 79 dejo escrita: "alcanzable no es lo mismo que encadenado").

USO:
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 80 --tramo-cadena 6
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 80 --tramo-cadena 6 --comparar docs/loop/REPORTE.md

`--comparar` busca, en el fichero dado, filas de tabla con AL MENOS 4 celdas
(`# | par (paso) | alcanzable | decision`) cuya primera celda sea un numero:
es la forma exacta de la tabla de las lecturas frescas del reporte. Las filas
de 3 celdas (la tabla de las unidades "ya decididas en vueltas anteriores",
que no lleva columna de alcanzabilidad) se ignoran a proposito: no son la
misma tabla y comparar contra ellas seria comparar dos preguntas distintas.

CASO POSITIVO OBLIGATORIO (vuelta 81), contra la vuelta 80: tallar el tramo 6
de la vuelta 80 tiene que dar, en la fila 27, "ALCANZABLE (6 saltos)", y en la
fila 28, "SIN CAMINO PREVIO"; el reporte de la vuelta 80 publico exactamente
lo contrario en esas dos celdas.

--- TAREA 2.b y 2.c: EL REMEDIO DEL REMEDIO (vuelta 82) ---

POR QUE NACE (acta de la vuelta 81, seccion 4.5). `--comparar` solo sabe leer
la tabla de CUATRO celdas (# | par | alcanzable | decision), que en el tramo
6 eran solo las 10 lecturas frescas: las otras 20 unidades de la cabeza de la
bolsa viven en una tabla HERMANA de tres celdas (las "ya decididas en vueltas
anteriores"), que el codigo ignora a proposito porque no es la misma
pregunta. Contarlas como AUSENTE y sumarlas al ROJO fabricaba un chequeo
obligatorio que no podia aprobarse NUNCA (20 AUSENTES y exit 1 pase lo que
pase), que es un chequeo que se acaba saltando.

EL ARREGLO: (2.b) AUSENTE deja de ser ROJO por si sola. El tallador imprime
debajo de la comparacion la lista NOMINAL de las unidades no publicadas en
esa tabla, con su cuenta, para que nada se esconda callado, pero no tumba el
exit code. (2.c) ROJO NUEVO, la fila inventada: si la tabla del reporte
publica un numero de fila que el fichero del filtro no tiene, es ROJO y exit
1 (una fila que no viene de ninguna unidad real del instrumento es peor que
una AUSENTE: es una tabla inventando una unidad, no callando una que si
existe). DISTINTA (2.a) sigue igual, sin cambio: sigue siendo la unica razon
"de contenido" para el ROJO.

CASO POSITIVO OBLIGATORIO (vuelta 82), contra la vuelta 80: `--vuelta 80
--tramo-cadena 6 --comparar docs/loop/REPORTE.md` tiene que dar exit 1 (las
filas 27 y 28 siguen DISTINTA, con el texto del instrumento al lado) y tiene
que listar las 20 unidades de las "ya decididas" por su nombre bajo "UNIDADES
NO PUBLICADAS EN ESA TABLA", no contarlas como rojo.

--- TAREA 2.b: LA IDENTIDAD GANA EL HEAD REAL DE LA APERTURA (vuelta 81) ---

POR QUE NACE (acta de la vuelta 80, seccion 1.8 y seccion 3.1). El modo
`--fase04` ya tallaba el "commit de apertura" como el commit del ACTA de la
vuelta anterior, pero el HEAD real cuando el ejecutor abrio la vuelta 80 NO
era ese commit (`bc9cde6f`, el acta 79): era `3cdf90d1`, el commit de una
decision del fundador que entro ENTRE el acta y la primera tarea. Esa vez fue
inocuo (los tres ficheros del commit intermedio eran de `docs/`, y los
arboles de `dataset/` de los dos commits coinciden), pero el hueco es real:
el dia que un commit se cuele ahi y SI toque `dataset/`, la fila de identidad
nombraria un arbol que no es el medido.

EL REMEDIO: el ejecutor sella `git rev-parse HEAD` ANTES de la primera
operacion de la vuelta, en un fichero propio,
`SALIDA_V<N>_HEAD_APERTURA.txt` (una linea, el hash completo de 40
caracteres). En modo `--fase04`, el tallador ahora LEE ese sello (nunca corre
`git rev-parse HEAD` el mismo: para cuando el tallador corre, HEAD ya se
movio con las operaciones de la vuelta) y lo compara contra el commit del
acta: si el ARBOL DE `dataset/` de los dos commits (`git rev-parse
<commit>:dataset`) NO COINCIDE, el tallador cae en ROJO (no talla nada, exit
1), porque entonces las cifras de apertura publicadas no son fiables para el
commit que la fila nombra. Si los dos arboles SI coinciden, la fila lo dice
explicito: "arboles de `dataset/` IGUALES: VERDE".

Si `SALIDA_V<N>_HEAD_APERTURA.txt` no existe, es ROJO igual (no se inventa el
HEAD real, ni se calla el chequeo).

CASO POSITIVO OBLIGATORIO (vuelta 81), contra la vuelta 80: los dos hashes
salen DISTINTOS (`bc9cde6f` el commit del acta, `3cdf90d1` el HEAD real de
apertura, reconstruido y verificado por `git log` en esta vuelta porque el
sello en vivo no existia antes de esta TAREA) y el chequeo da VERDE, porque
sus arboles de `dataset/` son iguales (`git rev-parse bc9cde6f:dataset` y
`git rev-parse 3cdf90d1:dataset` dan el mismo hash de arbol).

--- TAREA 2.d: EL TALLADOR APRENDE EL REGISTRO (vuelta 83) ---

POR QUE NACE (acta de la vuelta 82, seccion 3 y seccion 5 punto 1: la cola de
`OP-E-01` estaba atascada porque un par leido y NO enlazado se queda en la
bolsa, y como cada tramo leia LA CABEZA, los no enlazados se apilaban ahi).
Desde el tramo 8, la unidad de lectura son las primeras 30 unidades de la
bolsa filtrada que NO tengan decision registrada en
`docs/plan/OP_E_01_DECIDIDAS.jsonl` (adjudicacion 5.1 del acta 82), no las 30
primeras a secas. `--tramo-cadena` ya tallaba, sin cambios de codigo, lo que
sea que el fichero del filtro ponga bajo "CABEZA DE LA BOLSA FILTRADA" (el
indice de cada unidad es texto libre, no se recalcula), asi que la
responsabilidad de saltar las decididas recae en el script que genera ESE
fichero. `--registro RUTA` (opcional, combinado con `--tramo-cadena`) es la
RED DE SEGURIDAD que no depende de que ese script generador este bien
escrito: cruza cada unidad tallada contra el registro, y si CUALQUIERA tiene
decision `NO SE ENLAZA` ya registrada, es ROJO (una unidad decidida se colo
en la cabeza que se talla como si fuera fresca: exactamente el defecto que
produjo el atasco). Sin `--registro`, el comportamiento es identico al de
antes (no se cruza nada).

USO:
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 83 --tramo-cadena 8 --registro docs/plan/OP_E_01_DECIDIDAS.jsonl
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 83 --tramo-cadena 8 --registro docs/plan/OP_E_01_DECIDIDAS.jsonl --comparar docs/loop/REPORTE.md

CASO POSITIVO OBLIGATORIO (vuelta 83): tallar el tramo 8 con
`--registro docs/plan/OP_E_01_DECIDIDAS.jsonl` sobre un fichero de filtro que
(por error) SI trajera una de las unidades ya decididas en el registro bajo
su CABEZA tiene que dar ROJO, nombrando el par; sobre el fichero real (que
solo trae las 30 frescas) da VERDE.

--- TAREA 3.b: DOS FILAS MAS EN --fase04, LAS DOS CIFRAS DISFRAZADAS DE PROSA (vuelta 85) ---

POR QUE NACE (acta de la vuelta 84, seccion 4, adjudicacion 6.4). Dos frases
de la cabecera del reporte de la vuelta 84 vivian FUERA de la tabla tallada,
en prosa suelta que ningun tallador cubria, y las dos eran cifras: "las
aristas se movieron DOCE veces" (eran seis) y "el calibrado queda sin
desfase" (quedaba con tres filas de desfase). Las dos se tallan ahora como
filas mas de `--fase04`, con la misma mecanica de ROJO que las demas: si la
celda no se puede leer, no se talla nada.

FILA "aristas movidas en la vuelta": cierre menos apertura en las CUATRO
cifras (`nodos_siguientes`, `nodos_previos`, suma, union), calculada de las
MISMAS `SALIDA_V<N>_CONTEO_<LADO>.txt` que ya leen las seis filas de arriba
(sig/prev/suma/union): ningun fichero nuevo, solo la resta de dos cifras ya
citadas.

FILA "desfase del calibrado rastreado": lee
`SALIDA_V<N>_DESFASE_CALIBRADO_<LADO>.txt` (instrumento
`scripts/loop/vuelta85_medir_desfase_calibrado.py <ref>`, que replica la
MISMA definicion de "arista" que `scripts/plan/paso_contra_nodo_calibrado.py`:
hijo en vecinos(madre) O madre en vecinos(hijo), resuelto por alias, no el
chequeo estricto de las dos vistas), cuenta cuantas filas de
`docs/plan/PASO_NODO_CALIBRADO.jsonl` tienen el campo `arista` distinto de lo
que el grafo de ESE lado dice, y lista los pares cuando son pocos (10 o
menos). Que haya desfase NO es, por si solo, una caida: es correcto y esta
mandado (adjudicacion 5.7 del acta 82) cuando el fichero se commitea "tal
como quedo" tras una escritura posterior a su propia recalibracion. Lo que
esta fila remedia es que la prosa pueda NEGARLO cuando existe: la cifra
tallada no permite esa negacion.

CASO OBLIGATORIO (vuelta 85): tallar la vuelta 84 con `--fase04` tiene que
dar, en la fila del desfase, apertura "?" (la vuelta 84 no genero ese
fichero: no existia esta fila) salvo que se reconstruya con el instrumento
nuevo corrido sobre el commit de esa vuelta; sobre la vuelta 85 (que si
genera los dos lados) tiene que dar 3 en la apertura (las tres aristas de
la TAREA 3 de la vuelta 84, heredadas) y lo que la TAREA 4 de esta vuelta
deje en el cierre.

--- TAREA 2.b: EL COTEJO LOCALIZA LA TABLA POR SU CABECERA DE SECCION (vuelta 84) ---

POR QUE NACE (acta de la vuelta 83, seccion 4). `--comparar` aceptaba
CUALQUIER fila de 4 o mas celdas con la primera celda numerica, EN TODO EL
FICHERO, como si fuera la tabla del tramo. Dos averias, medidas por el
auditor: (i) el reporte de la vuelta 83 partio la tabla en una de TRES
celdas (alcanzabilidad sola) y otra de CINCO (alcanzabilidad + decision +
razon), y el cotejo viejo solo sabia leer la de cuatro o mas, asi que
cotejaba contra la de CINCO, cuya celda de alcanzable trae PROSA
("ALCANZABLE 3 saltos via ...") en vez del texto exacto tallado ("ALCANZABLE
(3 saltos)"), dando 30 DISTINTAS de 30; (ii) por buscar en TODO el fichero,
se tragaba filas de tablas AJENAS (la del horneado de la TAREA 2.a, la de la
TAREA 4) con tal de que su primera celda fuera un numero, contandolas como
"inventadas".

EL ARREGLO: `tabla_cadena_del_fichero(ruta, tramo)` ya NO barre el fichero
entero. Primero localiza la SECCION del tramo por su encabezado markdown (una
linea que empieza por `#` y menciona "tramo N" y "alcanzabilidad", sin
importar el orden ni las mayusculas); despues, DENTRO de esa seccion (hasta
el siguiente encabezado), busca la tabla por su FILA DE TITULOS EXACTA
(`# | par (paso) | alcanzable previo (vara de la cadena)`, la misma que este
tallador imprime), y toma solo las filas que la siguen. Si la seccion no
aparece, o si aparece pero no trae esa fila de titulos exacta, es ROJO (no
calza) con el mensaje explicito de cual de las dos cosas falto: NUNCA cae de
vuelta al barrido viejo.

CONVENCION QUE EL REPORTE TIENE QUE SEGUIR para que el cotejo la encuentre:
la tabla tallada por `--tramo-cadena` se pega ENTERA (titulos incluidos)
bajo un encabezado markdown propio que mencione el numero de tramo y la
palabra "alcanzabilidad" (por ejemplo, "### La tabla de alcanzabilidad
(vara de la cadena) del tramo 9"). Una tabla de "lectura" con mas columnas
(decision, razon) puede convivir en la misma seccion o en otra: el cotejo
solo mira la fila de titulos exacta, no la posicion ni la cantidad de tablas
alrededor.

CASO POSITIVO OBLIGATORIO (vuelta 84): `--vuelta 83 --tramo-cadena 8
--comparar docs/loop/REPORTE.md` (el REPORTE.md de la vuelta 83, antes de
que este arreglo tuviera donde encontrar su tabla) tiene que seguir dando
ROJO, y ahora con el mensaje nuevo (seccion o fila de titulos no encontrada
con esa forma), no con "30 DISTINTAS" ni con "filas inventadas" fantasma.

--- TAREA 2.c: EL HORIZONTE DE LA VARA SE PUBLICA (vuelta 84) ---

POR QUE NACE (acta de la vuelta 83, seccion 1.10 y adjudicacion 6.7). La vara
de la cadena (`scripts/loop/vuelta80_vara_cadena.py`, `marcar_alcanzables`)
tiene un HORIZONTE de seis saltos: "SIN CAMINO PREVIO" no quiere decir
inalcanzable, quiere decir "inalcanzable en seis saltos o menos". Ese dato
vive en el codigo desde la vuelta 80 y no habia aparecido en un reporte. Este
tallador no calcula el horizonte (no vuelve a correr la vara): el ejecutor lo
publica como una linea de prosa debajo de la tabla pegada, citando el
instrumento que la corrio sin horizonte para la vuelta de que se trate. No es
una fila mas del tallador porque el fichero del filtro no trae esa cifra por
defecto.
"""
import argparse
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")


def leer(nombre, fallos):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("no existe la salida %s" % nombre)
        return ""
    return io.open(ruta, encoding="utf-8").read()


def busca(texto, patron, etiqueta, fallos):
    if not texto:
        fallos.append("sin texto para %s" % etiqueta)
        return "?"
    m = re.search(patron, texto)
    if not m:
        fallos.append("no se pudo leer %s" % etiqueta)
        return "?"
    return m.group(1)


def miles(valor, con_miles):
    if not con_miles or not valor.isdigit():
        return valor
    return "{:,}".format(int(valor)).replace(",", ".")


def lado(vuelta, sufijo, fallos):
    """Lee TODAS las cifras de un lado (APERTURA o CIERRE) de sus propias salidas."""
    p = "SALIDA_V%d_" % vuelta
    d = {}

    est = leer(p + ("APERTURA.txt" if sufijo == "APERTURA" else "CIERRE.txt"), fallos)
    d["ficheros"] = busca(est, r"ficheros\s+: (\d+)", "ficheros %s" % sufijo, fallos)
    d["vivos"] = busca(est, r"vivos\s+: (\d+)", "vivos %s" % sufijo, fallos)
    d["deprecados"] = busca(est, r"deprecados\s+: (\d+)", "deprecados %s" % sufijo, fallos)
    d["enlaces"] = busca(est, r"enlaces\s+: (\d+)", "enlaces %s" % sufijo, fallos)
    d["operaciones"] = busca(est, r"operaciones: (\d+), ids unicos", "operaciones %s" % sufijo, fallos)
    d["estados"] = busca(est, r"estados: \{'([A-Z]+)': \d+\}", "estados %s" % sufijo, fallos)
    d["rotas"] = busca(est, r"dependencias rotas: (\d+)", "dependencias rotas %s" % sufijo, fallos)
    d["inventario"] = busca(est, r"entradas: (\d+)", "inventario %s" % sufijo, fallos)

    mar = leer(p + "MARCADOR_" + sufijo + ".txt", fallos)
    d["A"] = busca(mar, r"\n  A\s+(\d+)", "A %s" % sufijo, fallos)
    d["B"] = busca(mar, r"\n  B\s+(\d+)", "B %s" % sufijo, fallos)
    d["C"] = busca(mar, r"\n  C\s+(\d+)", "C %s" % sufijo, fallos)
    d["D"] = busca(mar, r"\n  D\s+(\d+)", "D %s" % sufijo, fallos)
    # n, huecos y duplicados salen del fichero de ESTADO y no del de marcador:
    # aquel los da ya contados (huecos: 0), y el de marcador imprime la LISTA
    # de huecos (huecos: []), que no es la cifra que la cabecera publica.
    d["n"] = busca(est, r"n = (\d+)", "n %s" % sufijo, fallos)
    d["huecos"] = busca(est, r"\nhuecos: (\d+)", "huecos %s" % sufijo, fallos)
    d["duplicados"] = busca(est, r"\nduplicados: (\d+)", "duplicados %s" % sufijo, fallos)

    rec = leer(p + "RECOMPUTO_" + sufijo + ".txt", fallos)
    d["crudas"] = busca(rec, r"clase == 'A'\): (\d+)", "A crudas %s" % sufijo, fallos)
    d["colapsos"] = busca(rec, r"los dos lados\): (\d+)", "colapsos %s" % sufijo, fallos)
    d["pares"] = busca(rec, r"deduplicar\): (\d+)", "pares distintos %s" % sufijo, fallos)
    d["componentes"] = busca(rec, r"componentes totales: (\d+)", "componentes %s" % sufijo, fallos)
    d["cerrados"] = busca(rec, r"CERRADOS: (\d+) sobre", "CERRADOS %s" % sufijo, fallos)
    d["cerrados_n"] = busca(rec, r"CERRADOS: \d+ sobre (\d+) nodos", "nodos CERRADOS %s" % sufijo, fallos)
    d["abiertos"] = busca(rec, r"ABIERTOS: (\d+) sobre", "ABIERTOS %s" % sufijo, fallos)
    d["abiertos_n"] = busca(rec, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos ABIERTOS %s" % sufijo, fallos)

    # LAS CUATRO COMPROBACIONES, cada lado de SU PROPIA salida. Es la celda que
    # la vuelta 56 heredo del otro lado, y por eso se lee aqui pieza por pieza.
    d["c1_izq"] = busca(rec, r"i\. nodos en actos \((\d+)\)", "comprobacion i izquierda %s" % sufijo, fallos)
    d["c1_der"] = busca(rec, r"i\. nodos en actos \(\d+\) == suma de tamanos de las componentes \((\d+)\)",
                        "comprobacion i derecha %s" % sufijo, fallos)
    d["c2_izq"] = busca(rec, r"ii\. A vigentes resueltas del retrato \((\d+)\)",
                        "comprobacion ii izquierda %s" % sufijo, fallos)
    d["c2_der"] = busca(rec, r"ii\. A vigentes resueltas del retrato \(\d+\) == suma de aristas A internas de las componentes \((\d+)\)",
                        "comprobacion ii derecha %s" % sufijo, fallos)
    d["cuatro"] = "TODAS OK" if "LAS CUATRO: TODAS OK" in rec else "NO TODAS OK"

    d["cola"] = busca(leer(p + "COLA_" + sufijo + ".txt", fallos),
                      r"nodos en la cola: (\d+)", "cola %s" % sufijo, fallos)

    col = leer(p + "COLISIONES_" + sufijo + ".txt", fallos)
    d["colisiones"] = busca(col, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones %s" % sufijo, fallos)
    d["autopares"] = busca(col, r"AUTO-PARES \(los dos lados al mismo vivo\): (\d+)",
                           "auto-pares %s" % sufijo, fallos)

    dup = leer(p + "DUPLICADAS_" + sufijo + ".txt", fallos)
    d["dup_grupos"] = busca(dup, r"grupos afectados \(nodo mas campo mas destino\) \| (\d+)",
                            "grupos de duplicadas %s" % sufijo, fallos)
    d["dup_nodos"] = busca(dup, r"nodos con al menos una duplicada\*\* \| \*\*(\d+)",
                           "nodos con duplicadas %s" % sufijo, fallos)
    return d


def filas(ap, ci, con_miles):
    """Las filas de la tabla, cada una con su etiqueta, su celda de apertura y
    su celda de cierre. La etiqueta es la clave de comparacion."""
    m = lambda v: miles(v, con_miles)
    f = []
    f.append(("marcador `A` / `B` / `C` / `D`",
              "%s / %s / %s / %s" % (m(ap["A"]), m(ap["B"]), m(ap["C"]), m(ap["D"])),
              "%s / %s / %s / %s" % (m(ci["A"]), m(ci["B"]), m(ci["C"]), m(ci["D"]))))
    f.append(("`n`, huecos, duplicados",
              "%s / %s / %s" % (m(ap["n"]), ap["huecos"], ap["duplicados"]),
              "%s / %s / %s" % (m(ci["n"]), ci["huecos"], ci["duplicados"])))
    f.append(("grafo: ficheros / vivos / deprecados / enlaces",
              "%s / %s / %s / %s" % (m(ap["ficheros"]), m(ap["vivos"]), m(ap["deprecados"]), m(ap["enlaces"])),
              "%s / %s / %s / %s" % (m(ci["ficheros"]), m(ci["vivos"]), m(ci["deprecados"]), m(ci["enlaces"]))))
    f.append(("retrato: `A` crudas / colapsos / pares distintos",
              "%s / %s / %s" % (m(ap["crudas"]), m(ap["colapsos"]), m(ap["pares"])),
              "%s / %s / %s" % (m(ci["crudas"]), m(ci["colapsos"]), m(ci["pares"]))))
    f.append(("actos (componentes)", m(ap["componentes"]), m(ci["componentes"])))
    f.append(("actos `CERRADOS` / `ABIERTOS`",
              "%s / %s" % (m(ap["cerrados"]), m(ap["abiertos"])),
              "%s / %s" % (m(ci["cerrados"]), m(ci["abiertos"]))))
    f.append(("nodos en `CERRADOS` / `ABIERTOS`",
              "%s / %s" % (m(ap["cerrados_n"]), m(ap["abiertos_n"])),
              "%s / %s" % (m(ci["cerrados_n"]), m(ci["abiertos_n"]))))
    f.append(("cola de costuras", m(ap["cola"]), m(ci["cola"])))
    f.append(("colisiones de clase vigentes", m(ap["colisiones"]), m(ci["colisiones"])))
    f.append(("auto-pares (los dos lados al mismo vivo)", m(ap["autopares"]), m(ci["autopares"])))
    f.append(("duplicadas historicas: grupos / nodos",
              "%s / %s" % (m(ap["dup_grupos"]), m(ap["dup_nodos"])),
              "%s / %s" % (m(ci["dup_grupos"]), m(ci["dup_nodos"]))))
    f.append(("operaciones, estados, dependencias rotas",
              "%s, todas `%s`, %s" % (m(ap["operaciones"]), ap["estados"], ap["rotas"]),
              "%s, todas `%s`, %s" % (m(ci["operaciones"]), ci["estados"], ci["rotas"])))
    f.append(("entradas del inventario", m(ap["inventario"]), m(ci["inventario"])))
    # LA CELDA QUE LA RACHA PAGO: cada lado con SUS PROPIAS cifras.
    f.append(("las cuatro comprobaciones de `08_VERIFICACION`",
              "%s (%s igual a %s; %s igual a %s)" % (ap["cuatro"], m(ap["c1_izq"]), m(ap["c1_der"]),
                                                    m(ap["c2_izq"]), m(ap["c2_der"])),
              "%s (%s igual a %s; %s igual a %s)" % (ci["cuatro"], m(ci["c1_izq"]), m(ci["c1_der"]),
                                                    m(ci["c2_izq"]), m(ci["c2_der"]))))
    return f


def leer_opcional(nombre):
    """Como leer(), pero SIN registrar fallo si no existe: para la fila del
    marcador en fase04, que es la unica opcional (la fase 04 no toca el
    cribado). Devuelve None si el fichero no existe."""
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        return None
    return io.open(ruta, encoding="utf-8").read()


def lado_fase04(vuelta, sufijo, fallos, con_miles=True):
    """Lee TODAS las cifras de un lado (APERTURA o CIERRE) de fase 04, cada
    una de SU PROPIA salida del dia. Ninguna celda hereda del otro lado."""
    p = "SALIDA_V%d_" % vuelta
    m = lambda v: miles(v, con_miles)
    d = {}

    gate = leer(p + "GATE0_CMD1_" + sufijo + ".txt", fallos)
    d["nodos"] = busca(gate, r"master_graph\.json == archivos en disco \(valor: (\d+) vs \d+\)",
                       "censo (nodos) %s" % sufijo, fallos)
    d["vivos"] = busca(gate, r"Universo: activos / deprecados \(valor: (\d+) activos",
                       "censo (vivos) %s" % sufijo, fallos)
    d["deprecados"] = busca(gate, r"Universo: activos / deprecados \(valor: \d+ activos, (\d+) deprecados",
                            "censo (deprecados) %s" % sufijo, fallos)
    d["auto_aristas"] = busca(gate, r"auto-arista via alias\) \(valor: (\d+) auto-aristas\)",
                              "Gate 0 auto-aristas %s" % sufijo, fallos)
    d["dup_titulo"] = busca(gate, r"titulo_concepto exacto duplicado \(valor: (\d+)\)",
                            "Gate 0 duplicadas de titulo %s" % sufijo, fallos)
    d["divergentes"] = busca(gate, r"dicen lo mismo \(valor: (\d+) nodos divergentes\)",
                             "Gate 0 nodos divergentes %s" % sufijo, fallos)
    d["gate_veredicto"] = busca(gate, r"GATE 0: (\w+)", "veredicto Gate 0 %s" % sufijo, fallos)

    con = leer(p + "CONTEO_" + sufijo + ".txt", fallos)
    ocurrencias = re.findall(r"sig (\d+) prev (\d+) suma (\d+) union (\d+)", con) if con else []
    if not ocurrencias:
        fallos.append("no se pudo leer las cifras de aristas %s" % sufijo)
        d["sig"] = d["prev"] = d["suma"] = d["union"] = "?"
    else:
        d["sig"], d["prev"], d["suma"], d["union"] = ocurrencias[-1]

    motor = leer(p + "MOTOR_" + sufijo + ".txt", fallos)
    d["motor"] = busca(motor, r"TODOS LOS TESTS PASARON \((\d+/\d+)\)", "motor %s" % sufijo, fallos)

    web = leer(p + "WEB_" + sufijo + ".txt", fallos)
    m_ficheros = re.search(r"Test Files\s+(\d+) passed \((\d+)\)", web) if web else None
    if not m_ficheros:
        fallos.append("no se pudo leer web ficheros %s" % sufijo)
        d["web_ficheros"] = "?"
    else:
        d["web_ficheros"] = "%s passed (%s)" % (m(m_ficheros.group(1)), m(m_ficheros.group(2)))
    m_tests = re.search(r"Tests\s+(\d+) passed(?:\s*\|\s*(\d+) skipped)? \((\d+)\)", web) if web else None
    if not m_tests:
        fallos.append("no se pudo leer web tests %s" % sufijo)
        d["web_tests"] = "?"
    else:
        pasadas, saltadas, total = m_tests.groups()
        d["web_tests"] = ("%s passed, %s skipped (%s)" % (m(pasadas), m(saltadas), m(total))) if saltadas \
            else ("%s passed (%s)" % (m(pasadas), m(total)))

    # El tsc vacio ES la senal de exito (tsc sin salida == exitcode 0), asi que
    # se lee aparte, sin pasar por busca() (que exigiria un patron y fallaria
    # sobre un fichero vacio que en realidad es el caso bueno).
    ruta_tsc = os.path.join(LOOP, p + "TSC_" + sufijo + ".txt")
    if not os.path.exists(ruta_tsc):
        fallos.append("no existe la salida %s" % (p + "TSC_" + sufijo + ".txt"))
        d["tsc"] = "?"
    else:
        contenido_tsc = io.open(ruta_tsc, encoding="utf-8").read()
        if contenido_tsc.strip() == "":
            d["tsc"] = "EXITCODE 0, cero lineas"
        else:
            n = len(contenido_tsc.strip("\n").splitlines())
            d["tsc"] = "%d linea(s) de salida (revisar)" % n

    mar = leer_opcional(p + "MARCADOR_" + sufijo + ".txt")
    if mar is not None:
        d["marcador_A"] = busca(mar, r"'A': (\d+)", "marcador A %s" % sufijo, fallos)
        d["marcador_B"] = busca(mar, r"'B': (\d+)", "marcador B %s" % sufijo, fallos)
        d["marcador_C"] = busca(mar, r"'C': (\d+)", "marcador C %s" % sufijo, fallos)
        d["marcador_D"] = busca(mar, r"'D': (\d+)", "marcador D %s" % sufijo, fallos)
        d["marcador_n"] = busca(mar, r"\}\s*(\d+)\s*$", "marcador n %s" % sufijo, fallos)
    else:
        d["marcador_A"] = None

    # TAREA 3.b (vuelta 85): el desfase del calibrado rastreado, opcional
    # (una vuelta que no genero el fichero no talla la fila, igual que el
    # marcador). Cuando SI existe, ninguna de sus cifras se deja sin leer.
    des = leer_opcional(p + "DESFASE_CALIBRADO_" + sufijo + ".txt")
    if des is not None:
        d["desfase_n"] = busca(des, r"DESFASE DEL CALIBRADO RASTREADO: (\d+) fila", "desfase %s" % sufijo, fallos)
        d["desfase_lista"] = re.findall(r"^\s{2}(\S+ -> \S+) \|", des, re.MULTILINE)
    else:
        d["desfase_n"] = None
    return d


def filas_fase04(ap, ci, con_miles):
    """Las filas de la cabecera de fase 04, etiqueta + celda apertura + celda
    cierre, cada celda leida de SU PROPIO lado."""
    m = lambda v: miles(v, con_miles)
    f = []
    f.append(("censo: nodos / vivos / deprecados",
              "%s / %s / %s" % (m(ap["nodos"]), m(ap["vivos"]), m(ap["deprecados"])),
              "%s / %s / %s" % (m(ci["nodos"]), m(ci["vivos"]), m(ci["deprecados"]))))
    f.append(("Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes",
              "%s (auto-aristas %s, duplicadas %s, divergentes %s)"
              % (ap["gate_veredicto"], ap["auto_aristas"], ap["dup_titulo"], ap["divergentes"]),
              "%s (auto-aristas %s, duplicadas %s, divergentes %s)"
              % (ci["gate_veredicto"], ci["auto_aristas"], ci["dup_titulo"], ci["divergentes"])))
    f.append(("aristas: `nodos_siguientes` / `nodos_previos` / suma / union",
              "%s / %s / %s / %s" % (m(ap["sig"]), m(ap["prev"]), m(ap["suma"]), m(ap["union"])),
              "%s / %s / %s / %s" % (m(ci["sig"]), m(ci["prev"]), m(ci["suma"]), m(ci["union"]))))
    f.append(("motor", ap["motor"], ci["motor"]))
    f.append(("web: ficheros / tests",
              "%s / %s" % (ap["web_ficheros"], ap["web_tests"]),
              "%s / %s" % (ci["web_ficheros"], ci["web_tests"])))
    f.append(("tsc", ap["tsc"], ci["tsc"]))
    if ap.get("marcador_A") is not None or ci.get("marcador_A") is not None:
        def celda_marcador(d):
            if d.get("marcador_A") is None:
                return "(sin cambio esta vuelta: no se remidio)"
            return "%s / %s / %s / %s, n %s" % (m(d["marcador_A"]), m(d["marcador_B"]),
                                                m(d["marcador_C"]), m(d["marcador_D"]), m(d["marcador_n"]))
        f.append(("marcador del cribado `A` / `B` / `C` / `D`, `n`",
                  celda_marcador(ap), celda_marcador(ci)))

    # TAREA 3.b (vuelta 85): las dos filas que remedian las dos caidas de
    # reporte de la vuelta 84 (acta 84, seccion 4, adjudicacion 6.4).
    dif = lambda campo: int(ci[campo]) - int(ap[campo])
    f.append(("aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union",
              "(no aplica: la celda de cierre es la resta contra esta apertura)",
              "%+d / %+d / %+d / %+d" % (dif("sig"), dif("prev"), dif("suma"), dif("union"))))

    if ap.get("desfase_n") is not None or ci.get("desfase_n") is not None:
        def celda_desfase(d):
            if d.get("desfase_n") is None:
                return "?"
            n = d["desfase_n"]
            lista = d.get("desfase_lista") or []
            if lista and len(lista) <= 10:
                return "%s fila(s): %s" % (m(n), ", ".join("`%s`" % p for p in lista))
            return "%s fila(s)" % m(n)
        f.append(("desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo)",
                  celda_desfase(ap), celda_desfase(ci)))
    return f


def rama_actual(fallos):
    """La rama de HEAD, leida de git y no tecleada. No es una fila del tallador
    (no hay una segunda rama contra la que comparar), pero toda cifra que se
    imprima sale de aqui, nunca de un argumento."""
    try:
        r = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=RAIZ,
                           capture_output=True, text=True, check=True)
        return r.stdout.strip()
    except Exception as e:
        fallos.append("no se pudo leer la rama actual con git rev-parse: %s" % e)
        return None


def commit_apertura_desde_git(vuelta, rama, fallos):
    """EL COMMIT DE APERTURA, LEIDO DE GIT (escalada del 26 ago 2026, vuelta
    80): busca en `git log` de RAMA el commit cuyo mensaje EMPIEZA por 'ACTA
    DE LA VUELTA <vuelta-1> DEL AUDITOR', que es el patron exacto y estable
    que todo acta de auditor usa para nombrar la vuelta que cierra. Si no hay
    NINGUNO o hay MAS DE UNO, ROJO: jamas inventa un hash."""
    if rama is None:
        fallos.append("sin rama, no se busca el commit de apertura")
        return None
    try:
        r = subprocess.run(["git", "log", rama, "--pretty=format:%H\x01%s"], cwd=RAIZ,
                           capture_output=True, text=True, check=True)
    except Exception as e:
        fallos.append("no se pudo leer git log de la rama %s: %s" % (rama, e))
        return None
    patron = re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR\b" % (vuelta - 1))
    hallados = []
    for linea in r.stdout.splitlines():
        if "\x01" not in linea:
            continue
        h, s = linea.split("\x01", 1)
        if patron.match(s):
            hallados.append(h)
    if not hallados:
        fallos.append("git log de la rama %s no trae ningun commit 'ACTA DE LA VUELTA %d "
                      "DEL AUDITOR': no se talla el commit de apertura" % (rama, vuelta - 1))
        return None
    if len(hallados) > 1:
        fallos.append("git log de la rama %s trae %d commits 'ACTA DE LA VUELTA %d DEL "
                      "AUDITOR' (%s): ambiguo, no se talla el commit de apertura"
                      % (rama, len(hallados), vuelta - 1, ", ".join(h[:8] for h in hallados)))
        return None
    return hallados[0][:8]


def leer_head_apertura(vuelta, fallos):
    """EL HEAD REAL DE LA APERTURA, SELLADO POR EL EJECUTOR (TAREA 2.b, vuelta
    81): lee SALIDA_V<vuelta>_HEAD_APERTURA.txt, una linea con el hash
    completo de 40 caracteres de `git rev-parse HEAD` corrido ANTES de la
    primera operacion. El tallador NUNCA corre `git rev-parse HEAD` el mismo:
    para cuando el tallador corre, HEAD ya se movio con las operaciones de la
    vuelta, asi que solo puede LEER lo que el ejecutor sello a tiempo."""
    nombre = "SALIDA_V%d_HEAD_APERTURA.txt" % vuelta
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("no existe el sello %s (el ejecutor debe correr `git rev-parse HEAD` "
                      "antes de la 1.a operacion y guardarlo ahi)" % nombre)
        return None
    texto = io.open(ruta, encoding="utf-8").read().strip()
    m = re.match(r"^([0-9a-f]{40})", texto)
    if not m:
        fallos.append("%s no trae un hash de 40 caracteres reconocible" % nombre)
        return None
    return m.group(1)


def arbol_dataset(commit, etiqueta, fallos):
    """El arbol de dataset/ de COMMIT, leido con `git rev-parse <commit>:dataset`
    (nunca tecleado). None y fallo registrado si el commit o la ruta no existen."""
    try:
        r = subprocess.run(["git", "rev-parse", "%s:dataset" % commit], cwd=RAIZ,
                           capture_output=True, text=True, check=True)
        return r.stdout.strip()
    except Exception as e:
        fallos.append("no se pudo leer el arbol de dataset/ de %s (%s): %s" % (etiqueta, commit, e))
        return None


RE_FILA = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")


def limpiar(celda):
    """Quita el resaltado de la celda para comparar contenido y no maquillaje."""
    return re.sub(r"\s+", " ", celda.replace("**", "")).strip()


def tabla_del_fichero(ruta):
    """Extrae las filas de la primera tabla de cabecera que el fichero tenga."""
    texto = io.open(ruta, encoding="utf-8").read()
    filas_halladas = {}
    for linea in texto.splitlines():
        if not linea.strip().startswith("|"):
            continue
        m = RE_FILA.match(linea.strip())
        if not m:
            continue
        etiqueta = limpiar(m.group(1))
        if not etiqueta or set(etiqueta) <= set("-: "):
            continue
        if etiqueta not in filas_halladas:
            filas_halladas[etiqueta] = (limpiar(m.group(2)), limpiar(m.group(3)))
    return filas_halladas


def comparar_contra(f, ruta_arg):
    """Cotejo compartido por los dos modos: extrae la tabla que RUTA_ARG YA
    tiene y la coteja fila a fila contra F (las filas talladas). Devuelve el
    exit code (0 identica, 1 rojo o con diferencias)."""
    print("--- COMPARACION CONTRA %s ---" % ruta_arg)
    print()
    ruta = ruta_arg if os.path.isabs(ruta_arg) else os.path.join(RAIZ, ruta_arg)
    if not os.path.exists(ruta):
        print("  ROJO: no existe %s" % ruta)
        return 1
    existentes = tabla_del_fichero(ruta)
    diferencias = 0
    ausentes = 0
    for etiqueta, celda_ap, celda_ci in f:
        clave = limpiar(etiqueta)
        if clave not in existentes:
            print("  AUSENTE  | %s | la fila no esta en el fichero" % etiqueta)
            ausentes += 1
            continue
        vieja_ap, vieja_ci = existentes[clave]
        for nombre, vieja, tallada in (("apertura", vieja_ap, limpiar(celda_ap)),
                                       ("cierre", vieja_ci, limpiar(celda_ci))):
            if vieja != tallada:
                diferencias += 1
                print("  DISTINTA | %s | %s" % (etiqueta, nombre))
                print("             fichero : %s" % vieja)
                print("             tallador: %s" % tallada)
    print()
    print("  filas cotejadas: %d | DISTINTAS: %d | ausentes: %d"
          % (len(f), diferencias, ausentes))
    if diferencias or ausentes:
        print("  CABECERA: NO CALZA CON EL TALLADOR")
        return 1
    print("  CABECERA: IDENTICA AL TALLADOR")
    print()
    return 0


RE_UNIDAD_CADENA = re.compile(
    r"^\s*(\d+):\s*(.+?)\s*->\s*(.+?)\s*\(paso\s*(.+?),\s*dominio\s*(.+?)\)\s*\|\s*(.+?)\s*$"
)
RE_PAREJA_CADENA = re.compile(r"^\s*(\d+):\s*PAREJA:\s*(.+?)\s*$")
RE_SALTOS = re.compile(r"^YA ALCANZABLE \((\d+)\s*saltos?\)")


def leer_tramo_cadena(vuelta, tramo, fallos):
    """TAREA 2.a: lee SALIDA_V<vuelta>_TRAMO<tramo>_FILTRO_P91_GUARDA_CADENA.txt
    y devuelve la lista de unidades de la seccion "CABEZA DE LA BOLSA
    FILTRADA", cada una con su celda de alcanzabilidad TALLADA (nunca
    tecleada). ROJO (fallos.append) y unidad con alcanzable=None si una linea
    no se puede leer; ninguna cifra se inventa."""
    nombre = "SALIDA_V%d_TRAMO%d_FILTRO_P91_GUARDA_CADENA.txt" % (vuelta, tramo)
    texto = leer(nombre, fallos)
    if not texto:
        return []
    lineas = texto.splitlines()
    inicio = None
    for i, l in enumerate(lineas):
        if l.startswith("CABEZA DE LA BOLSA FILTRADA"):
            inicio = i
            break
    if inicio is None:
        fallos.append("%s no trae la seccion 'CABEZA DE LA BOLSA FILTRADA': no se talla nada" % nombre)
        return []
    i = inicio + 1
    while i < len(lineas) and not re.match(r"^\s*\d+:", lineas[i]):
        i += 1
    unidades = []
    while i < len(lineas) and lineas[i].strip():
        l = lineas[i]
        m = RE_UNIDAD_CADENA.match(l)
        mp = RE_PAREJA_CADENA.match(l)
        if m:
            idx, madre, hijo, paso, dominio, alc = m.groups()
            if alc.startswith("YA ALCANZABLE"):
                ms = RE_SALTOS.match(alc)
                if not ms:
                    fallos.append("unidad %s de %s: no se pudo leer el numero de saltos en %r"
                                  % (idx, nombre, alc))
                    texto_alc = None
                else:
                    texto_alc = "ALCANZABLE (%s saltos)" % ms.group(1)
            elif alc.strip() == "sin camino previo":
                texto_alc = "SIN CAMINO PREVIO"
            else:
                fallos.append("unidad %s de %s: alcanzabilidad no reconocida: %r" % (idx, nombre, alc))
                texto_alc = None
            unidades.append({"idx": idx, "par": "%s -> %s (paso %s)" % (madre, hijo, paso),
                             "alcanzable": texto_alc})
        elif mp:
            idx, desc = mp.groups()
            unidades.append({"idx": idx, "par": "PAREJA: %s" % desc,
                             "alcanzable": "(pareja, sin alcanzabilidad individual)"})
        else:
            break
        i += 1
    if not unidades:
        fallos.append("no se pudo leer ninguna unidad de %s" % nombre)
    return unidades


def parse_filas_pipe(ruta):
    """Toda fila de tabla markdown del fichero, como lista de celdas limpias
    (sin las celdas vacias de los extremos, sin filas separadoras)."""
    texto = io.open(ruta, encoding="utf-8").read()
    filas_out = []
    for linea in texto.splitlines():
        s = linea.strip()
        if not (s.startswith("|") and s.endswith("|")):
            continue
        celdas = [limpiar(c) for c in s.split("|")[1:-1]]
        if not celdas or set("".join(celdas)) <= set("-: "):
            continue
        filas_out.append(celdas)
    return filas_out


RE_HEADING = re.compile(r"^#{1,6}\s")

HEADER_TALLADA = ["#", "par (paso)", "alcanzable previo (vara de la cadena)"]


def _es_heading_de_tramo(linea, tramo):
    """TAREA 2.b (vuelta 84): LOCALIZA LA TABLA DEL TRAMO POR SU CABECERA DE
    SECCION, no por la forma de sus filas (acta de la vuelta 83, seccion 4: el
    cotejo viejo aceptaba cualquier fila de 4+ celdas con primera celda
    numerica en TODO el fichero, y asi se tragaba filas de tablas ajenas, la
    del horneado de la TAREA 2.a y la de la TAREA 4). Una linea de encabezado
    markdown (empieza por 1 a 6 '#') que mencione 'tramo N' y 'alcanzabilidad'
    (en cualquier orden, sin importar mayusculas) marca el INICIO de la
    seccion de ese tramo."""
    if not RE_HEADING.match(linea):
        return False
    if not re.search(r"(?i)\btramo\s*%d\b" % tramo, linea):
        return False
    return "alcanzabilidad" in linea.lower()


def tabla_cadena_del_fichero(ruta, tramo):
    """TAREA 2.b (vuelta 84): localiza la seccion del TRAMO por su cabecera
    (una linea markdown que menciona 'tramo N' y 'alcanzabilidad'), y DENTRO
    de esa seccion (hasta el siguiente encabezado) busca la tabla TALLADA por
    su propia fila de titulos exacta (HEADER_TALLADA: '# | par (paso) |
    alcanzable previo (vara de la cadena)'), que es la unica tabla que este
    tallador imprime con esa forma. Toma TODAS las filas que sigan a esa fila
    de titulos (saltando la de separadores) hasta la siguiente linea que no
    sea de tabla. Devuelve (dict numero -> celda alcanzable, None) si se
    encuentra, o (None, mensaje de fallo) si la seccion o la tabla no
    aparecen: NUNCA cae de vuelta al barrido viejo de "cualquier fila con 4+
    celdas", que es exactamente el defecto que este remedio corrige."""
    texto = io.open(ruta, encoding="utf-8").read()
    lineas = texto.splitlines()

    inicio_seccion = None
    for i, linea in enumerate(lineas):
        if _es_heading_de_tramo(linea, tramo):
            inicio_seccion = i
            break
    if inicio_seccion is None:
        return None, ("no se encontro, en %s, un encabezado markdown que mencione "
                      "'tramo %d' y 'alcanzabilidad': la tabla del tramo se localiza "
                      "por su cabecera de seccion, no por la forma de sus filas" % (ruta, tramo))

    fin_seccion = len(lineas)
    for i in range(inicio_seccion + 1, len(lineas)):
        if RE_HEADING.match(lineas[i]):
            fin_seccion = i
            break

    seccion = lineas[inicio_seccion:fin_seccion]
    idx_header_tabla = None
    for i, linea in enumerate(seccion):
        s = linea.strip()
        if not (s.startswith("|") and s.endswith("|")):
            continue
        celdas = [limpiar(c) for c in s.split("|")[1:-1]]
        if celdas == HEADER_TALLADA:
            idx_header_tabla = i
            break
    if idx_header_tabla is None:
        return None, ("la seccion del tramo %d (encabezado en la linea %d de %s) no trae "
                      "la fila de titulos exacta de la tabla tallada (%s): la tabla no se "
                      "puede localizar dentro de esa seccion"
                      % (tramo, inicio_seccion + 1, ruta, " | ".join(HEADER_TALLADA)))

    resultado = {}
    j = idx_header_tabla + 1
    while j < len(seccion):
        s = seccion[j].strip()
        if not (s.startswith("|") and s.endswith("|")):
            break
        celdas = [limpiar(c) for c in s.split("|")[1:-1]]
        if celdas and set("".join(celdas)) <= set("-: "):
            j += 1
            continue  # fila separadora
        if len(celdas) >= 3 and celdas[0].isdigit():
            resultado[celdas[0]] = celdas[2]
        j += 1
    return resultado, None


def cargar_registro_decididas(ruta_registro, fallos):
    """TAREA 2.d: carga el set de pares (madre, hijo) con decision 'NO SE
    ENLAZA' en el registro, para que --tramo-cadena pueda negar que
    cualquiera de ellos aparezca bajo la CABEZA que talla (red de seguridad,
    independiente de que el generador del fichero del filtro este bien
    escrito)."""
    ruta = ruta_registro if os.path.isabs(ruta_registro) else os.path.join(RAIZ, ruta_registro)
    if not os.path.exists(ruta):
        fallos.append("no existe el registro %s" % ruta_registro)
        return None
    decididas = set()
    with io.open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            import json as _json
            try:
                fila = _json.loads(linea)
            except ValueError as e:
                fallos.append("linea no JSON en %s: %s" % (ruta_registro, e))
                continue
            if fila.get("decision") == "NO SE ENLAZA":
                decididas.add((fila.get("madre"), fila.get("hijo")))
    return decididas


RE_PAR_UNIDAD_TALLADA = re.compile(r"^(.+?)\s*->\s*(.+?)\s*\(paso")


def modo_tramo_cadena(vuelta, tramo, comparar_ruta, registro_ruta=None):
    """TAREA 2.a: talla la tabla de alcanzabilidad del tramo, la imprime para
    pegar, y si se pide --comparar, coteja celda por celda contra el fichero
    dado. Mecanica de ROJO identica a los demas modos. TAREA 2.d (vuelta 83):
    con --registro, ademas niega que alguna unidad tallada ya tenga decision
    NO SE ENLAZA registrada (ROJO si la tiene: una decidida se colo como
    fresca)."""
    fallos = []
    unidades = leer_tramo_cadena(vuelta, tramo, fallos)
    if fallos:
        print("  ROJO, %d cosa(s) no se pudieron leer y NO se talla nada:" % len(fallos))
        for fallo in fallos:
            print("     %s" % fallo)
        return 1

    if registro_ruta:
        fallos_reg = []
        decididas = cargar_registro_decididas(registro_ruta, fallos_reg)
        if fallos_reg:
            print("  ROJO, %d cosa(s) no se pudieron leer y NO se talla nada:" % len(fallos_reg))
            for fallo in fallos_reg:
                print("     %s" % fallo)
            return 1
        coladas = []
        for u in unidades:
            m = RE_PAR_UNIDAD_TALLADA.match(u["par"])
            if not m:
                continue
            clave = (m.group(1), m.group(2))
            if clave in decididas:
                coladas.append((u["idx"], u["par"]))
        if coladas:
            print("  ROJO: %d unidad(es) YA DECIDIDA(S) (NO SE ENLAZA en el registro) se colaron "
                  "bajo la CABEZA que se talla como si fueran frescas:" % len(coladas))
            for idx, par in coladas:
                print("     fila %s | %s" % (idx, par))
            print("  TAREA 2.d: EL TALLADOR APRENDE EL REGISTRO, y esto es lo que niega. NO SE TALLA NADA.")
            return 1

    print("=" * 78)
    print("LA TABLA DE ALCANZABILIDAD (VARA DE LA CADENA) DEL TRAMO %d, TALLADA. Vuelta %d." % (tramo, vuelta))
    print("Cada celda sale de SALIDA_V%d_TRAMO%d_FILTRO_P91_GUARDA_CADENA.txt; ninguna tecleada." % (vuelta, tramo))
    print("LA COLUMNA CONTESTA UNA SOLA PREGUNTA: si hay o no camino previo, y con cuantos saltos.")
    print("Si ese camino es o no LA CADENA PROPIA de la madre es una decision de lectura aparte.")
    print("=" * 78)
    print()
    print("| # | par (paso) | alcanzable previo (vara de la cadena) |")
    print("|---:|---|---|")
    for u in unidades:
        celda = u["alcanzable"] if u["alcanzable"] is not None else "?"
        print("| %s | `%s` | %s |" % (u["idx"], u["par"], celda))
    print()

    if not comparar_ruta:
        print("FIN")
        return 0

    print("--- COMPARACION CONTRA %s ---" % comparar_ruta)
    print()
    ruta = comparar_ruta if os.path.isabs(comparar_ruta) else os.path.join(RAIZ, comparar_ruta)
    if not os.path.exists(ruta):
        print("  ROJO: no existe %s" % ruta)
        return 1
    existentes, fallo_seccion = tabla_cadena_del_fichero(ruta, tramo)
    if fallo_seccion:
        print("  ROJO: %s" % fallo_seccion)
        print("  TABLA DE LA CADENA: NO CALZA CON EL TALLADOR")
        print("FIN")
        return 1
    diferencias = 0
    ausentes = []
    for u in unidades:
        if u["alcanzable"] is None:
            continue
        clave = u["idx"]
        if clave not in existentes:
            ausentes.append(u)
            continue
        vieja = existentes[clave]
        if limpiar(vieja) != limpiar(u["alcanzable"]):
            diferencias += 1
            print("  DISTINTA | fila %s | %s" % (clave, u["par"]))
            print("             fichero : %s" % vieja)
            print("             tallador: %s" % u["alcanzable"])

    # TAREA 2.c (vuelta 82): ROJO NUEVO, la fila inventada. Si la tabla del
    # reporte publica un numero de fila que el fichero del filtro no tiene,
    # es ROJO y exit 1: no es una unidad AUSENTE (que es la tabla callando
    # algo real), es la tabla publicando algo que el instrumento nunca trajo.
    claves_unidades = set(u["idx"] for u in unidades)
    inventadas = sorted((k for k in existentes if k not in claves_unidades), key=int)

    # TAREA 2.b (vuelta 82): AUSENTE deja de ser ROJO por si sola. Se imprime
    # la lista NOMINAL de las unidades no publicadas en esa tabla, con su
    # cuenta, para que nada se esconda callado, pero no tumba la comparacion.
    print()
    if ausentes:
        print("  UNIDADES NO PUBLICADAS EN ESA TABLA (AUSENTE, NO es rojo por si sola): %d" % len(ausentes))
        for u in ausentes:
            print("     fila %s | %s" % (u["idx"], u["par"]))
    else:
        print("  UNIDADES NO PUBLICADAS EN ESA TABLA: 0")
    if inventadas:
        print("  ROJO: fila(s) inventada(s) (numero que el fichero del filtro no tiene): %s"
              % ", ".join(inventadas))

    print()
    print("  filas cotejadas: %d | DISTINTAS: %d | ausentes (no rojo): %d | inventadas (ROJO): %d"
          % (len(unidades), diferencias, len(ausentes), len(inventadas)))
    if diferencias or inventadas:
        print("  TABLA DE LA CADENA: NO CALZA CON EL TALLADOR")
        print("FIN")
        return 1
    print("  TABLA DE LA CADENA: IDENTICA AL TALLADOR (las ausentes listadas no son rojo)")
    print("FIN")
    return 0


def main():
    ap_arg = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    ap_arg.add_argument("--vuelta", type=int, required=True)
    ap_arg.add_argument("--sin-miles", action="store_true")
    ap_arg.add_argument("--fase04", action="store_true",
                        help="talla la cabecera de la fase 04 (ENLACES) en vez de la del cribado")
    ap_arg.add_argument("--tramo-cadena", type=int, default=None, metavar="TRAMO",
                        help="talla la tabla de alcanzabilidad (vara de la cadena) del TRAMO K de "
                             "OP-E-01 (TAREA 2.a), leyendo "
                             "SALIDA_V<vuelta>_TRAMO<K>_FILTRO_P91_GUARDA_CADENA.txt")
    ap_arg.add_argument("--comparar", default=None,
                        help="fichero cuya tabla se coteja contra la tallada")
    ap_arg.add_argument("--registro", default=None, metavar="RUTA",
                        help="TAREA 2.d: con --tramo-cadena, niega que alguna unidad tallada "
                             "ya tenga decision NO SE ENLAZA en este registro jsonl "
                             "(docs/plan/OP_E_01_DECIDIDAS.jsonl)")
    a = ap_arg.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    con_miles = not a.sin_miles

    if a.tramo_cadena is not None:
        return modo_tramo_cadena(a.vuelta, a.tramo_cadena, a.comparar, a.registro)

    print("=" * 78)
    print("LA CABECERA DEL REPORTE, TALLADA. Vuelta %d.%s" % (a.vuelta, " Modo fase04." if a.fase04 else ""))
    print("Cada celda sale de la salida que la cita; ninguna esta tecleada.")
    print("=" * 78)
    print()

    fallos = []
    if a.fase04:
        apertura = lado_fase04(a.vuelta, "APERTURA", fallos, con_miles)
        cierre = lado_fase04(a.vuelta, "CIERRE", fallos, con_miles)
        rama = rama_actual(fallos)
        commit_ap = commit_apertura_desde_git(a.vuelta, rama, fallos)
        # TAREA 2.b (vuelta 81): el HEAD real de la apertura, sellado por el
        # ejecutor, mas el chequeo de que su arbol de dataset/ coincide con el
        # del commit del acta. Si no coinciden, ROJO: las cifras de apertura
        # no son fiables para el commit que la fila nombra.
        head_real = leer_head_apertura(a.vuelta, fallos)
        arbol_verde = None
        if commit_ap and head_real:
            arbol_acta = arbol_dataset(commit_ap, "commit del acta %s" % commit_ap, fallos)
            arbol_head = arbol_dataset(head_real, "HEAD real de apertura %s" % head_real[:8], fallos)
            if arbol_acta is not None and arbol_head is not None:
                if arbol_acta != arbol_head:
                    fallos.append(
                        "el arbol de dataset/ del commit del acta (%s, arbol %s) y el HEAD real de "
                        "apertura (%s, arbol %s) NO COINCIDEN: las cifras de apertura no son las del "
                        "commit que la fila nombra" % (commit_ap, arbol_acta[:8], head_real[:8], arbol_head[:8]))
                else:
                    arbol_verde = True
    else:
        apertura = lado(a.vuelta, "APERTURA", fallos)
        cierre = lado(a.vuelta, "CIERRE", fallos)

    if fallos:
        print("  ROJO, %d celdas no se pudieron leer y NO se talla nada:" % len(fallos))
        for fallo in fallos:
            print("     %s" % fallo)
        return 1

    f = filas_fase04(apertura, cierre, con_miles) if a.fase04 else filas(apertura, cierre, con_miles)
    if a.fase04:
        celda_identidad = (
            "rama `%s`, commit del acta `%s` (ACTA DE LA VUELTA %d DEL AUDITOR, leido de git log), "
            "HEAD real de apertura `%s` (sellado por el ejecutor antes de la 1.a operacion), arboles "
            "de `dataset/` %s"
            % (rama, commit_ap, a.vuelta - 1, head_real[:8], "IGUALES: VERDE" if arbol_verde else "?")
        )
        f.append(("identidad: rama y commit de apertura (leidos de git, no tecleados)",
                  celda_identidad, celda_identidad))

    print("--- LA TABLA, PARA PEGAR ENTERA EN LA CABECERA DEL REPORTE ---")
    print()
    print("| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |")
    print("|---|---:|---:|")
    for etiqueta, celda_ap, celda_ci in f:
        print("| %s | %s | **%s** |" % (etiqueta, celda_ap, celda_ci))
    print()

    if not a.fase04:
        print("--- LAS CUATRO COMPROBACIONES, CADA LADO DE SU PROPIA SALIDA ---")
        print()
        print("  APERTURA (SALIDA_V%d_RECOMPUTO_APERTURA.txt):" % a.vuelta)
        print("    i.  nodos en actos %s == componentes %s" % (apertura["c1_izq"], apertura["c1_der"]))
        print("    ii. A vigentes %s == aristas A internas %s" % (apertura["c2_izq"], apertura["c2_der"]))
        print("    veredicto: %s" % apertura["cuatro"])
        print("  CIERRE   (SALIDA_V%d_RECOMPUTO_CIERRE.txt):" % a.vuelta)
        print("    i.  nodos en actos %s == componentes %s" % (cierre["c1_izq"], cierre["c1_der"]))
        print("    ii. A vigentes %s == aristas A internas %s" % (cierre["c2_izq"], cierre["c2_der"]))
        print("    veredicto: %s" % cierre["cuatro"])
        if apertura["c1_izq"] == cierre["c1_izq"] and apertura["c2_izq"] == cierre["c2_izq"]:
            print("  AVISO: los dos lados dan la MISMA cifra. Puede ser cierto (vuelta que no")
            print("  movio el retrato), pero es la forma que la caida de la vuelta 56 tenia.")
        print()

    if not a.comparar:
        print("FIN")
        return 0

    resultado = comparar_contra(f, a.comparar)
    print("FIN")
    return resultado


if __name__ == "__main__":
    raise SystemExit(main())
