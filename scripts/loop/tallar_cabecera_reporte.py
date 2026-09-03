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

--- TAREA 2.c: LA FILA DEL DESFASE DEJA DE SER OPCIONAL (vuelta 86) ---

POR QUE NACE (acta de la vuelta 85, seccion 1.14 y adjudicacion 5.4). La fila
del desfase (TAREA 3.b, vuelta 85) se leia con `leer_opcional()`, la misma
funcion que la fila del marcador, cuyo docstring decia que el marcador era
"la unica opcional". Ya no lo era: una vuelta que no generara
`SALIDA_V<N>_DESFASE_CALIBRADO_<LADO>.txt` perdia la fila SIN NINGUN AVISO,
que es exactamente la degradacion silenciosa que el canon de fallar ruidoso
del banco, seccion 9, prohibe ("la degradacion silenciosa es la peor clase
de fallo: no deja sintoma"), y `EJECUTOR.md` regla 1 en una linea ("la celda
que no salga de un instrumento no se escribe").

EL ARREGLO: en `lado_fase04`, el desfase se lee ahora con `leer()` (la misma
funcion que censo, Gate 0, aristas, motor, web y tsc), que SI registra el
fallo en `fallos` cuando el fichero no existe. Ausencia del fichero del
desfase en modo `--fase04` es ahora un FALLO DECLARADO: el tallador cae en
ROJO y no talla nada, igual que si faltara cualquier otra celda obligatoria.
El marcador SIGUE siendo la fila opcional que queda (la fase 04 no toca el
cribado) y sigue leyendose con `leer_opcional()`, cuyo docstring ya no dice
que sea "la unica".

CASO OBLIGATORIO (vuelta 86): correr `--fase04 --vuelta 86` con
`SALIDA_V86_DESFASE_CALIBRADO_APERTURA.txt` (o el de cierre) renombrado a un
lado tiene que dar ROJO nombrando esa salida como no encontrada, y no talla
la tabla; con el fichero de vuelta a su sitio, el mismo comando talla igual
que antes.

--- TAREA 2.b: LA FILA DE IDENTIDAD DEJA DE SER UN LITERAL (vuelta 95) ---

POR QUE NACE (acta de la vuelta 94, sobre la linea 1187 de este fichero, tal
como estaba antes de este remedio). La celda de identidad imprimia, SIEMPRE,
"(sellado por el ejecutor antes de la 1.a operacion)", sin mirar nunca CUANDO
se habia escrito de verdad `SALIDA_V<N>_HEAD_APERTURA.txt`: `leer_head_apertura`
solo comprueba que el fichero exista y traiga 40 caracteres hexadecimales. En
la vuelta 94 esa frase era FALSA (el sello se commiteo a mitad de la vuelta,
no antes de la primera operacion) y el ejecutor tuvo que desmentir a su propio
instrumento en prosa: la misma especie que "LOS SEIS CASOS".

EL ARREGLO, `procedencia_sello_apertura()`: se busca, con `git log
--diff-filter=A`, el commit que ANADE `docs/loop/SALIDA_V<N>_HEAD_APERTURA.txt`
en la rama actual. Si el PADRE de ese commit es el hash que el propio fichero
sella, la celda dice "sellado antes de la 1.a operacion" (el commit que anadio
el sello es hijo directo del commit que el sello nombra: se escribio antes de
tocar nada); si no, la celda dice "sello RECONSTRUIDO DESPUES (commit X)",
nombrando sin adornos el commit que lo anadio. Nunca inventa: sin commit que
anada el fichero, o con mas de uno (ambiguo), ROJO.

CASOS OBLIGATORIOS (vuelta 95, medidos por el auditor): `--fase04 --vuelta 93`
tiene que dar "sellado antes de la 1.a operacion" (sello 85a250be..., anadido
en f73adb67, cuyo padre es 85a250be...); `--fase04 --vuelta 94` tiene que dar
"sello RECONSTRUIDO DESPUES (commit a4c89ab6)" (sello 267365c8..., anadido en
a4c89ab6, cuyo padre es 4c22a083, NO 267365c8). OJO: la cabecera YA PUBLICADA
de la vuelta 94 es una medicion historica cerrada y NO se retoca con este
arreglo; el instrumento reparado se estrena con la cabecera de la vuelta 95.

--- TAREA 2.1: EL TSC DESCUENTA SU PROPIO MARCADOR DE EXIT (vuelta 113) ---

POR QUE NACE (acta de la vuelta 112, seccion "TU CAIDA GRANDE ES DE GUARDA
CEGADA"). Desde la vuelta 112 el ejecutor apenda una linea final "EXIT=<n>" a
TODOS sus ficheros de salida, tsc incluido. La regla vieja de esta celda
("tsc sin salida == exitcode 0", literal desde la creacion de este fichero)
solo sabia leer un fichero VACIO como el caso bueno: un fichero con nada mas
que "EXIT=0" (7 bytes) ya no cuenta como vacio, y la celda publicaba "1
linea(s) de salida (revisar)", la MISMA forma que produciria un tsc con una
linea de error real. Asi nacieron `SALIDA_V112_TSC_APERTURA.txt` y
`_CIERRE.txt` (7 bytes cada uno, solo el marcador) y la cabecera de la vuelta
112 publico "revisar" en sus dos columnas con el tsc realmente en exit 0 y
cero lineas: guarda muerta, nadie lo declaro.

LA DECISION (con su unica condicion, resuelta por el ejecutor: distinguir un
tsc limpio de uno con una linea de error real), decidida en la opcion b del
encargo en vez de volver al fichero vacio de las vueltas 110 y 111: el
tallador APRENDE a leer el marcador en vez de que el ejecutor deje de
escribirlo. Si la ULTIMA linea no vacia del fichero hace match con
`^EXIT=(numero)$`, se separa del CONTENIDO (nunca cuenta como linea de salida
del tsc) y su numero se publica en la celda con el prefijo "EXITCODE <n>, ".
Sobre el CONTENIDO que queda (sin esa linea): vacio es tsc LIMPIO ("EXITCODE
<n>, cero lineas", o "EXITCODE 0, cero lineas" si no habia marcador: un
fichero totalmente vacio, como en las vueltas 110 y 111, sigue siendo el caso
bueno); no vacio es tsc SUCIO, y la celda NOMBRA las lineas (hasta 5) para
que nunca salga igual a la de un tsc limpio.

MUTACION V (verde) y MUTACION W (rojo), vuelta 113, corridas juntas por
`scripts/loop/vuelta113_tarea2_mutacion_tsc.py`: un fichero con SOLO "EXIT=0"
tiene que tallar "EXITCODE 0, cero lineas" (tsc LIMPIO); un fichero con una
linea de error real mas "EXIT=1" tiene que tallar una celda DISTINTA, con la
linea nombrada. Salida commiteada en
`docs/loop/SALIDA_V113_TAREA2_2_3_MUTACION_V_W.txt`.

--- ADJUDICACION 6.1 DEL ACTA 158 (3 sep 2026): LA VUELTA QUE ABRE UN ACTA N SE
NUMERA N MAS 1, Y ESA ARITMETICA ES LA DE ESTA GUARDA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

EL INVARIANTE, QUE ESTA GUARDA YA LLEVABA ESCRITO Y QUE AHORA QUEDA DICHO CON SU
NOMBRE: la apertura de la vuelta N es el commit del acta de la vuelta N MENOS 1.
Dicho al reves, que es como se lee desde fuera: EL ACTA N ABRE LA VUELTA N MAS 1.

QUE PASO Y POR QUE NO FUE CAIDA DE NADIE (acta 158, seccion 4, medido con
`git log` sobre la rama): el invariante se cumplio sin excepcion en todo el
tramo (acta 149 abre la 150, acta 151 la 152, acta 153 la 154, acta 155 la 156).
El acta 157 abria la vuelta 158, pero el encargo de aquella vuelta NUNCA dijo
que numero de vuelta tocaba, solo de que acta venia; el ejecutor numero la suya
157 igualando su vuelta al numero del acta, y esta guarda y
`tallar_cabecera_reporte.py` se quedaron las dos ciegas buscando un
"ACTA DE LA VUELTA 156" que no existe.

EL REMEDIO NO ES DE CODIGO Y ESTA GUARDA NO SE TOCA: desde el acta 158 EL
ENCARGO LLEVA EL NUMERO DE VUELTA EN SU CABECERA FIJA, junto al rotulo de hashes
admitidos. La aritmetica de esta guarda era la correcta y sigue igual.

--- ADJUDICACION 6.2 DEL ACTA 158 (3 sep 2026): EL SELLO DE APERTURA TARDIO ES
CAIDA DE PROCEDIMIENTO, NO DE CIFRA, Y SU REMEDIO YA ESTABA CONSTRUIDO: ES ESTA
GUARDA, DESBLOQUEADA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

EL HECHO. En la vuelta 157 el valor de la apertura no fue falso (es re derivable
de git, y el auditor lo re derivo: `git rev-parse 23004b4d^` da `abb2fe4e`),
pero `SALIDA_V157_HEAD_APERTURA.txt` no se sello hasta el cierre. La regla que
se incumplio ya existe, y su guarda es esta.

LO QUE ESTE CASO DEJA ESCRITO, Y VALE PARA CUALQUIER GUARDA DE LA CASA: EN LA
MISMA VUELTA EN QUE ESTA GUARDA QUEDO CIEGA PASO EXACTAMENTE EL FALLO QUE
VIGILA. Una guarda bloqueada no es un evento neutro. No hay que construir nada:
desbloqueada, muerde.
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
    marcador en fase04, que es la fila que QUEDA opcional (la fase 04 no toca
    el cribado). YA NO ES LA UNICA (vuelta 86, adjudicacion 5.4 del acta 85):
    el desfase del calibrado dejo de leerse con esta funcion porque su
    ausencia silenciosa era la degradacion que el canon de fallar ruidoso del
    banco, seccion 9, prohibe. Devuelve None si el fichero no existe."""
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        return None
    return io.open(ruta, encoding="utf-8").read()


def interpretar_tsc(contenido_tsc):
    """TAREA 2.1 (vuelta 113): descuenta el marcador final "EXIT=<n>" antes de
    contar lineas del tsc, y publica el exitcode que lea. Extraida a funcion
    propia (antes vivia inline en lado_fase04) para que la prueba de mutacion
    V/W la llame directo, sin tener que fabricar una vuelta entera. Ver el
    docstring del modulo, seccion 'TAREA 2.1', para el porque y la decision."""
    lineas_tsc = contenido_tsc.split("\n")
    if lineas_tsc and lineas_tsc[-1] == "":
        lineas_tsc.pop()
    exit_leido = None
    if lineas_tsc:
        m_exit = re.match(r"^EXIT=(\d+)\s*$", lineas_tsc[-1].strip())
        if m_exit:
            exit_leido = m_exit.group(1)
            lineas_tsc = lineas_tsc[:-1]
    while lineas_tsc and lineas_tsc[-1].strip() == "":
        lineas_tsc.pop()
    if not lineas_tsc:
        return "EXITCODE %s, cero lineas" % (exit_leido if exit_leido is not None else "0")
    prefijo = ("EXITCODE %s, " % exit_leido) if exit_leido is not None else ""
    if len(lineas_tsc) <= 5:
        return "%s%d linea(s) de salida (revisar): %s" % (prefijo, len(lineas_tsc), "; ".join(lineas_tsc))
    return "%s%d linea(s) de salida (revisar)" % (prefijo, len(lineas_tsc))


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

    # EL TSC DESCUENTA SU PROPIO MARCADOR DE EXIT ANTES DE CONTAR (TAREA 2.1,
    # vuelta 113, encargo del auditor sobre el acta de la vuelta 112, "TU
    # CAIDA GRANDE ES DE GUARDA CEGADA"). Desde la vuelta 112 el ejecutor
    # empezo a apendar una linea final "EXIT=<n>" a TODOS los ficheros de
    # salida, tsc incluido. Para el tsc eso mato la guarda: un fichero con
    # SOLO "EXIT=0" (7 bytes) ya no esta vacio, y la vieja regla ("tsc vacio
    # == exito") lo contaba como "1 linea(s) de salida (revisar)", la MISMA
    # celda que produciria un tsc con una linea de error de verdad. Las dos
    # vueltas 112 nacieron asi (docs/loop/SALIDA_V112_TSC_APERTURA.txt y
    # _CIERRE.txt, 7 bytes cada uno) y la cabecera publico "revisar" con el
    # tsc realmente en exit 0 y cero lineas, sin que nadie lo declarara.
    #
    # LA DECISION (opcion b del encargo): en vez de volver al fichero vacio,
    # el tallador APRENDE a leer el marcador. Si la ULTIMA linea no vacia del
    # fichero hace match con `^EXIT=(\d+)$`, esa linea se separa del CONTENIDO
    # (nunca se cuenta como "linea de salida del tsc": es el marcador, no un
    # error) y su numero se publica en la celda. El resto del fichero, sin esa
    # linea, es el CONTENIDO REAL: si queda vacio, el tsc esta LIMPIO (se
    # publica el exitcode leido, o 0 si no habia marcador: fichero totalmente
    # vacio sigue siendo el caso bueno, como en las vueltas 110 y 111); si NO
    # queda vacio, el tsc tiene errores de verdad, y la celda NOMBRA las
    # lineas (hasta 5; mas de 5 se cuentan sin listarlas) para que la celda de
    # un tsc sucio nunca sea igual, ni por accidente, a la de uno limpio.
    ruta_tsc = os.path.join(LOOP, p + "TSC_" + sufijo + ".txt")
    if not os.path.exists(ruta_tsc):
        fallos.append("no existe la salida %s" % (p + "TSC_" + sufijo + ".txt"))
        d["tsc"] = "?"
    else:
        d["tsc"] = interpretar_tsc(io.open(ruta_tsc, encoding="utf-8").read())

    # TAREA 2.1 (vuelta 106, adjudicacion del auditor sobre la vuelta 105,
    # "PENDIENTE DE DOCTRINA" resuelta como GUARDA ENVEJECIDA y no como
    # doctrina nueva). Los cinco regex de aqui abajo esperaban el formato
    # VIEJO de un marcador tipo diccionario ("'A': 551 ... } 3388"), que NINGUN
    # script vigente imprime desde la vuelta 53. `scripts/recomputar_marcador.py`
    # (el que produce SALIDA_V<N>_MARCADOR_<LADO>.txt desde entonces) imprime:
    #   n = 3388 corte = 3388 huecos: [] dups(puesto): 0
    #   ...
    #   MARCADOR GLOBAL
    #     A 551 16.3
    #     B 72 2.1
    #     C 5 0.1
    #     D 2760 81.5
    # que es EXACTAMENTE lo que lado() (la funcion hermana del modo cribado,
    # mas arriba en este fichero) ya lee bien con r"\n  A\s+(\d+)" y compania:
    # ese es el ejemplar que el encargo pide seguir. A/B/C/D se leen ahora con
    # el mismo patron que lado().
    #
    # LA CELDA n: lado() la lee de un fichero de ESTADO aparte
    # (SALIDA_V<N>_APERTURA.txt/_CIERRE.txt, sin segmento intermedio) que la
    # fase 04 NUNCA produce (esa fase no corre el ciclo del cribado, solo Gate
    # 0 + tres suites + censo + aristas + marcador si toca). No hay ESTADO que
    # leer aqui. Pero el propio MARCADOR_<LADO>.txt trae n en su primera
    # linea ("n = 3388 corte = 3388 huecos: [] dups(puesto): 0"): ahi SI es
    # una cifra suelta (a diferencia de "huecos", que en esa misma linea es
    # una LISTA (huecos: []) y por eso no se talla esa celda con el mismo
    # mecanismo). Se lee de ahi, del mismo fichero que A/B/C/D, sin inventar
    # una fuente nueva.
    mar = leer_opcional(p + "MARCADOR_" + sufijo + ".txt")
    if mar is not None:
        d["marcador_A"] = busca(mar, r"\n  A\s+(\d+)", "marcador A %s" % sufijo, fallos)
        d["marcador_B"] = busca(mar, r"\n  B\s+(\d+)", "marcador B %s" % sufijo, fallos)
        d["marcador_C"] = busca(mar, r"\n  C\s+(\d+)", "marcador C %s" % sufijo, fallos)
        d["marcador_D"] = busca(mar, r"\n  D\s+(\d+)", "marcador D %s" % sufijo, fallos)
        d["marcador_n"] = busca(mar, r"^n = (\d+)", "marcador n %s" % sufijo, fallos)
    else:
        d["marcador_A"] = None

    # TAREA 2.c (vuelta 86, adjudicacion 5.4 del acta 85): el desfase del
    # calibrado rastreado DEJA DE SER OPCIONAL. Hasta la vuelta 85 se leia con
    # leer_opcional() y una vuelta sin el fichero simplemente perdia la fila
    # sin ruido; el docstring de leer_opcional() decia que el marcador era "la
    # unica opcional" y ya no lo era. Desde ahora se lee con leer(), que SI
    # registra fallo (fallos.append) cuando el fichero falta: la ausencia es
    # un FALLO DECLARADO, no una fila que desaparece en silencio. El marcador
    # sigue leyendose con leer_opcional() arriba: esa diferencia queda escrita
    # aqui, en el codigo, y no solo en la prosa del reporte.
    des = leer(p + "DESFASE_CALIBRADO_" + sufijo + ".txt", fallos)
    d["desfase_n"] = busca(des, r"DESFASE DEL CALIBRADO RASTREADO: (\d+) fila", "desfase %s" % sufijo, fallos)
    d["desfase_lista"] = re.findall(r"^\s{2}(\S+ -> \S+) \|", des, re.MULTILINE)
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

    # TAREA 2.c (vuelta 86): fila OBLIGATORIA, no opcional. Si su fichero
    # faltara, lado_fase04 ya registro el fallo en `fallos` y main() ROJO
    # antes de llegar aqui: para cuando esta funcion corre, las dos celdas
    # existen siempre.
    def celda_desfase(d):
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
    NINGUNO o hay MAS DE UNO, ROJO: jamas inventa un hash.

    Devuelve (hash_corto, asunto_real) y no solo el hash (vuelta 106): el
    asunto real se publica en la celda de identidad en vez de repetir SIEMPRE
    la frase 'ACTA DE LA VUELTA N DEL AUDITOR', que dejo de ser literalmente
    cierta el dia (vuelta 106) que un acta empezo a titularse distinto (ver
    abajo) y una celda que repite una frase fija sin mirar cual de los dos
    patrones caso en realidad es, en si misma, el tipo de afirmacion no
    tallada que este fichero existe para evitar."""
    if rama is None:
        fallos.append("sin rama, no se busca el commit de apertura")
        return None, None
    try:
        r = subprocess.run(["git", "log", rama, "--pretty=format:%H\x01%s"], cwd=RAIZ,
                           capture_output=True, text=True, check=True)
    except Exception as e:
        fallos.append("no se pudo leer git log de la rama %s: %s" % (rama, e))
        return None, None
    # LAS DOS FORMAS DEL TITULO DEL ACTA (vuelta 106): 'ACTA DE LA VUELTA N DEL
    # AUDITOR' (vigente 92 a 104) y 'ACTA DEL AUDITOR, VUELTA N' (nacida en el
    # acta de la vuelta 105, commit fc504151, que rompio el patron literal sin
    # avisar). Mismo remedio y mismo motivo que en
    # verificar_apertura_sellada.py:commit_acta.
    patrones = [
        re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR\b" % (vuelta - 1)),
        re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d\b" % (vuelta - 1)),
    ]
    hallados = []
    for linea in r.stdout.splitlines():
        if "\x01" not in linea:
            continue
        h, s = linea.split("\x01", 1)
        if any(p.match(s) for p in patrones):
            hallados.append((h, s))
    if not hallados:
        fallos.append("git log de la rama %s no trae ningun commit 'ACTA DE LA VUELTA %d "
                      "DEL AUDITOR' ni 'ACTA DEL AUDITOR, VUELTA %d': no se talla el commit "
                      "de apertura" % (rama, vuelta - 1, vuelta - 1))
        return None, None
    if len(hallados) > 1:
        fallos.append("git log de la rama %s trae %d commits 'ACTA DE LA VUELTA %d DEL "
                      "AUDITOR' (%s): ambiguo, no se talla el commit de apertura"
                      % (rama, len(hallados), vuelta - 1, ", ".join(h[:8] for h, _ in hallados)))
        return None, None
    h, s = hallados[0]
    return h[:8], s


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


def leer_head_cierre(vuelta, fallos):
    """TAREA 2.4 (vuelta 106, adjudicacion del auditor sobre el acta de la
    vuelta 105: "el hash de HEAD de tu cabecera contradice tu propio
    fichero"). El reporte de la vuelta 105 publico como HEAD de cierre
    `ba261321` (el HEAD de su TAREA 4.4, dos commits antes del cierre real),
    mientras que `SALIDA_V105_HEAD_CIERRE.txt` -- que ya existia, escrito por
    el ejecutor, pero que NINGUN tallador leia -- decia `275cb46c` (el commit
    donde de verdad corrio el ciclo de cierre). Es la misma especie que
    `leer_head_apertura`, aplicada al otro lado: el HEAD de cierre SE LEE del
    sello que el ejecutor escribe, nunca se teclea. Fallo declarado
    (fallos.append) si el fichero no existe: la celda de identidad de la
    columna de cierre no se talla sin el."""
    nombre = "SALIDA_V%d_HEAD_CIERRE.txt" % vuelta
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("no existe el sello %s (el ejecutor debe correr `git rev-parse HEAD` "
                      "tras la ultima operacion, antes de escribir el reporte, y guardarlo ahi)" % nombre)
        return None
    texto = io.open(ruta, encoding="utf-8").read().strip()
    m = re.match(r"^([0-9a-f]{40})", texto)
    if not m:
        fallos.append("%s no trae un hash de 40 caracteres reconocible" % nombre)
        return None
    return m.group(1)


def procedencia_sello_apertura(vuelta, rama, head_real, fallos):
    """LA FILA DE IDENTIDAD SE LEE DE GIT, NUNCA TECLEADA (TAREA 2.b, vuelta
    95, encargo del auditor, acta de la vuelta 94: el tallador imprimia, como
    literal incondicional, "(sellado por el ejecutor antes de la 1.a
    operacion)", y `leer_head_apertura` solo comprueba que el fichero exista
    y traiga 40 caracteres hexadecimales, nada mira CUANDO se escribio). Este
    remedio busca en `git log --diff-filter=A` de RAMA el commit que ANADE
    `docs/loop/SALIDA_V<vuelta>_HEAD_APERTURA.txt`. Si el PADRE de ese commit
    es HEAD_REAL (el hash que el propio fichero sella), el sello se escribio
    de verdad ANTES de la primera operacion, como manda la regla; si el padre
    es cualquier otro commit, el fichero se anadio DESPUES, a mitad o al
    final de la vuelta, y el sello esta RECONSTRUIDO. Nunca inventa: si no
    hay NINGUN commit que anada el fichero, o hay MAS DE UNO (ambiguo), ROJO.

    CASOS OBLIGATORIOS (vuelta 95, medidos por el auditor): la vuelta 93
    (sello 85a250be..., anadido en f73adb67, cuyo padre es 85a250be...) tiene
    que dar "sellado antes de la 1.a operacion"; la vuelta 94 (sello
    267365c8..., anadido en a4c89ab6, cuyo padre es 4c22a083) tiene que dar
    "sello RECONSTRUIDO DESPUES (commit a4c89ab6)"."""
    if rama is None or head_real is None:
        fallos.append("sin rama o sin sello de apertura, no se puede leer la procedencia del sello")
        return None
    nombre_rel = "docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % vuelta
    try:
        r = subprocess.run(["git", "log", rama, "--diff-filter=A", "--pretty=format:%H", "--", nombre_rel],
                           cwd=RAIZ, capture_output=True, text=True, check=True)
    except Exception as e:
        fallos.append("no se pudo leer git log --diff-filter=A de %s: %s" % (nombre_rel, e))
        return None
    hallados = [h for h in r.stdout.splitlines() if h.strip()]
    if not hallados:
        fallos.append("git log --diff-filter=A no trae ningun commit que anada %s: no se talla la "
                      "procedencia del sello" % nombre_rel)
        return None
    if len(hallados) > 1:
        fallos.append("git log --diff-filter=A trae %d commits que anaden %s (%s): ambiguo, no se "
                      "talla la procedencia del sello" % (len(hallados), nombre_rel,
                                                            ", ".join(h[:8] for h in hallados)))
        return None
    commit_anade = hallados[0]
    try:
        r2 = subprocess.run(["git", "rev-parse", "%s^" % commit_anade], cwd=RAIZ,
                            capture_output=True, text=True, check=True)
        padre = r2.stdout.strip()
    except Exception as e:
        fallos.append("no se pudo leer el padre de %s: %s" % (commit_anade, e))
        return None
    if padre == head_real:
        return "sellado antes de la 1.a operacion"
    return "sello RECONSTRUIDO DESPUES (commit %s)" % commit_anade[:8]


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


# --------------------------- EL BLOQUE DE COMMITS SE COTEJA (TAREA 2.d, v141)
#
# POR QUE NACE (acta de la vuelta 140, caida 4.3, "de guarda que no alcanza, de
# la casa"). La cabecera tallada tiene delimitador Y --comparar, que exige
# CABECERA IDENTICA AL TALLADOR antes del commit. El bloque de commits estrenado
# en la vuelta 140 tiene delimitador y NINGUN COTEJO: verificar_cifras_del_reporte.py
# solo lo usa para SALTARSE esa ventana, asi que cualquier prosa metida entre las
# dos marcas queda invisible para la guarda de cifras. Es una exencion sin nada
# detras.
#
# QUE COMPRUEBA --comparar-commits: lee lo que hay entre <!-- COMMITS TALLADOS -->
# y <!-- FIN COMMITS TALLADOS --> del fichero, saca de ahi las lineas de commit
# (hash corto mas asunto) y las coteja contra `git log <apertura>..HEAD`:
#   - MISMO NUMERO de commits;
#   - MISMOS HASHES, cada uno prefijo del hash completo que git da;
#   - EN EL MISMO ORDEN, posicion por posicion;
#   - el ASUNTO tiene que ser PREFIJO del asunto real. Si es mas corto, se
#     DECLARA como truncado y se cuenta; si no es prefijo, es ROJO.
# El commit de apertura es el mismo que la fila de identidad ya usa
# (commit_apertura_desde_git), o sea leido de git y nunca tecleado.
#
# --- EL BLOQUE DE COMMITS SE ANCLA AL HEAD SELLADO (TAREA 2.b, VUELTA 142) ---
#
# POR QUE CAMBIA (acta de la vuelta 141: caida 4.2 de la casa, y 4.6 de encargo
# del auditor, que se declara autor del anclaje malo porque su TAREA 2.d de la
# 140 decia literal "lo coteja contra `git log <apertura>..HEAD`").
#
# EL DEFECTO, MEDIDO: anclado a HEAD VIVO, este cotejo SOLO PUEDE ESTAR VERDE EN
# EL INSTANTE EN QUE SE CORRE. En cuanto el reporte se commitea, git da un
# commit mas que el bloque, y la guarda pasa a ROJO con "el bloque trae 11 y git
# da 12" mas las once posiciones corridas un lugar. Corrida por el auditor sobre
# la vuelta 141 ya cerrada: ROJO con 13 cosas que no cuadran, sin que ninguna
# cifra estuviera mal (el auditor coteje el bloque a mano contra
# `git log 4b0fcb20..5a82ce38` y sale identico). UNA GUARDA QUE EL AUDITOR NO
# PUEDE RE-CORRER NO ES UNA GUARDA.
#
# EL REMEDIO, QUE ES EL QUE LA CABECERA YA USABA: el extremo de arriba se lee
# del SELLO, `SALIDA_V<N>_HEAD_CIERRE.txt`, con `leer_head_cierre()`, la misma
# funcion que la fila de identidad de la columna de cierre usa desde la vuelta
# 106. Asi el rango es FIJO y el cotejo es REPRODUCIBLE cualquier dia.
#
# SI EL SELLO NO EXISTE TODAVIA, ES ROJO Y SE DICE: no se cae de vuelta a HEAD
# vivo (eso seria reintroducir el defecto en silencio) y no se salta el chequeo.
# La consecuencia practica, dicha para que no sorprenda: `--comparar-commits` se
# corre DESPUES de sellar el HEAD de cierre, igual que `--comparar` de la
# cabecera.
#
# UNA CORRECCION AL ENCARGO, MEDIDA Y DECLARADA (vuelta 142, 2.b). El encargo
# decia "pasa a cotejar contra `git log <apertura>..<HEAD sellado de cierre>`,
# leido de SALIDA_V<N>_HEAD_CIERRE.txt". SE IMPLEMENTO ASI PRIMERO Y SE MIDIO:
# sobre el reporte de la vuelta 141 sale ROJO CON 12, no VERDE. La causa es
# estructural y no del reporte: EL HASH SELLADO ES, POR CONSTRUCCION, EL COMMIT
# ANTERIOR AL COMMIT QUE LLEVA EL SELLO. El ejecutor corre `git rev-parse HEAD`,
# escribe el fichero y LUEGO commitea; en la vuelta 141 el sello dice `84e4d861`
# y el commit que lo anade es `5a82ce38`, el commit de CIERRE, que el bloque
# lista y que `..84e4d861` deja fuera. Medido: `git log --diff-filter=A --
# docs/loop/SALIDA_V141_HEAD_CIERRE.txt` da `5a82ce38`, y `git rev-parse
# 5a82ce38^` da exactamente `84e4d861`.
#
# EL ANCLA QUE SI FUNCIONA, Y SIGUE SIN TECLEARSE: el COMMIT QUE ANADE el sello,
# leido con `git log --diff-filter=A`, igual que ya hace
# verificar_apertura_sellada.py con los ficheros de apertura. Es fijo,
# reproducible y no depende de HEAD. Y el hash escrito DENTRO del sello no se
# tira: se usa como GUARDA, exigiendo que sea el PADRE del commit que lo lleva.
# Si no lo es, es ROJO nombrando los dos, porque significa que el sello se
# escribio en un momento distinto del que dice.
#
# MUTACION (vuelta 142, 2.b): sobre el reporte de la vuelta 141 esta version
# tiene que salir VERDE donde la vieja salia ROJO con 13; y metiendo un commit
# inventado dentro del bloque, ROJO nombrandolo. Ver
# scripts/loop/vuelta142_2b_mutacion_commits.py.
MARCA_COMMITS_ABRE = "<!-- COMMITS TALLADOS -->"
MARCA_COMMITS_CIERRA = "<!-- FIN COMMITS TALLADOS -->"
RE_LINEA_COMMIT = re.compile(r"^\s*([0-9a-f]{7,40})\s+(\S.*?)\s*$")


def bloque_de_commits_del_fichero(ruta, fallos):
    """Las lineas de commit que el fichero trae ENTRE LAS DOS MARCAS. Devuelve
    la lista [(hash_corto, asunto)] en el orden en que aparecen."""
    texto = io.open(ruta, encoding="utf-8").read().splitlines()
    abre = [i for i, l in enumerate(texto) if MARCA_COMMITS_ABRE in l]
    cierra = [i for i, l in enumerate(texto) if MARCA_COMMITS_CIERRA in l]
    if len(abre) != 1 or len(cierra) != 1:
        fallos.append("el fichero trae %d marca(s) de apertura y %d de cierre del bloque "
                      "de commits: se esperaba una de cada" % (len(abre), len(cierra)))
        return []
    if cierra[0] < abre[0]:
        fallos.append("la marca de cierre del bloque de commits va ANTES que la de apertura")
        return []
    filas = []
    for linea in texto[abre[0] + 1:cierra[0]]:
        m = RE_LINEA_COMMIT.match(linea)
        if m:
            filas.append((m.group(1), m.group(2)))
    return filas


def commit_que_lleva_el_sello_de_cierre(vuelta, fallos):
    """EL EXTREMO DE ARRIBA DEL RANGO (TAREA 2.b, vuelta 142). Devuelve
    (commit_que_anade_el_sello, hash_escrito_dentro_del_sello), los dos leidos
    de git y del fichero, nunca tecleados. Ver el bloque
    "EL BLOQUE DE COMMITS SE ANCLA AL HEAD SELLADO" de arriba, y en particular
    "UNA CORRECCION AL ENCARGO, MEDIDA Y DECLARADA", que explica por que el
    ancla es el commit QUE LLEVA el sello y no el hash escrito dentro.

    ROJO, nombrando, si: el sello no existe (`leer_head_cierre` ya lo dice);
    ningun commit lo anade, o mas de uno; o el hash escrito dentro NO es el
    PADRE del commit que lo lleva."""
    sellado = leer_head_cierre(vuelta, fallos)
    if sellado is None:
        return None, None
    nombre = "SALIDA_V%d_HEAD_CIERRE.txt" % vuelta
    rel = "docs/loop/%s" % nombre
    try:
        r = subprocess.run(["git", "log", "--diff-filter=A", "--pretty=format:%H", "--", rel],
                           cwd=RAIZ, capture_output=True, text=True, check=True)
    except Exception as e:
        fallos.append("no se pudo leer el commit de nacimiento de %s: %s" % (nombre, e))
        return None, sellado
    nacidos = [h for h in r.stdout.splitlines() if h.strip()]
    if len(nacidos) != 1:
        fallos.append("%s tiene %d commit(s) que lo anaden (%s): el ancla del bloque de "
                      "commits queda ambigua y no se adivina"
                      % (nombre, len(nacidos), ", ".join(h[:8] for h in nacidos) or "ninguno"))
        return None, sellado
    portador = nacidos[0]
    try:
        padre = subprocess.run(["git", "rev-parse", "%s^" % portador], cwd=RAIZ,
                               capture_output=True, text=True, check=True).stdout.strip()
    except Exception as e:
        fallos.append("no se pudo leer el padre de %s: %s" % (portador[:8], e))
        return None, sellado
    if padre != sellado:
        fallos.append("%s dice %s, pero el PADRE del commit que lo anade (%s) es %s: el sello "
                      "no se escribio donde dice" % (nombre, sellado[:8], portador[:8], padre[:8]))
        return None, sellado
    return portador, sellado


def commits_de_git(apertura, cierre, fallos):
    """`git log <apertura>..<cierre>`, hash completo y asunto entero, en el
    orden que git da (el mas reciente primero), que es el orden en que el
    bloque se escribe.

    EL EXTREMO DE ARRIBA ES EL HEAD SELLADO, NO `HEAD` (TAREA 2.b, vuelta 142;
    acta 141, caida 4.2 de la casa y 4.6 de encargo del auditor). Ver el bloque
    "EL BLOQUE DE COMMITS SE ANCLA AL HEAD SELLADO" mas arriba."""
    try:
        r = subprocess.run(["git", "log", "%s..%s" % (apertura, cierre),
                            "--pretty=format:%H\x01%s"],
                           cwd=RAIZ, capture_output=True, text=True, check=True)
    except Exception as e:
        fallos.append("no se pudo correr git log %s..%s: %s" % (apertura, cierre, e))
        return []
    salida = []
    for linea in r.stdout.splitlines():
        if "\x01" in linea:
            h, s = linea.split("\x01", 1)
            salida.append((h, s))
    return salida


def comparar_commits(vuelta, ruta_arg):
    """El cotejo de la TAREA 2.d. Devuelve el exit code (0 calza, 1 rojo)."""
    print("--- COTEJO DEL BLOQUE DE COMMITS DE %s ---" % ruta_arg)
    print()
    fallos = []
    ruta = ruta_arg if os.path.isabs(ruta_arg) else os.path.join(RAIZ, ruta_arg)
    if not os.path.exists(ruta):
        print("  ROJO: no existe %s" % ruta)
        return 1
    rama = rama_actual(fallos)
    apertura, asunto_acta = commit_apertura_desde_git(vuelta, rama, fallos)
    if fallos:
        for x in fallos:
            print("  ROJO: %s" % x)
        return 1
    # EL EXTREMO DE ARRIBA: EL HEAD SELLADO DE CIERRE, LEIDO DE SU FICHERO
    # (TAREA 2.b, vuelta 142). Si el sello no existe todavia, la guarda LO DICE
    # Y SALE ROJO: no se salta y no cae de vuelta a HEAD vivo, que es
    # exactamente lo que la hacia irrepetible.
    cierre, sellado = commit_que_lleva_el_sello_de_cierre(vuelta, fallos)
    if fallos:
        for x in fallos:
            print("  ROJO: %s" % x)
        print("  BLOQUE DE COMMITS: NO SE PUEDE COTEJAR SIN EL HEAD SELLADO DE CIERRE")
        return 1
    print("  commit de apertura, leido de git (no tecleado): %s" % apertura)
    print("  asunto real del acta: %r" % asunto_acta)
    print("  HEAD sellado en SALIDA_V%d_HEAD_CIERRE.txt: %s" % (vuelta, sellado))
    print("  commit que LLEVA ese sello (git log --diff-filter=A), y padre del cual es el "
          "sellado: %s" % cierre)
    print("  rango cotejado, FIJO y sin HEAD vivo: git log %s..%s" % (apertura, cierre))
    print()

    del_fichero = bloque_de_commits_del_fichero(ruta, fallos)
    de_git = commits_de_git(apertura, cierre, fallos)
    if fallos:
        for x in fallos:
            print("  ROJO: %s" % x)
        return 1

    print("  commits en el bloque del fichero: %d | commits en git: %d"
          % (len(del_fichero), len(de_git)))
    problemas = []
    if len(del_fichero) != len(de_git):
        problemas.append("EL NUMERO NO CALZA: el bloque trae %d y git da %d"
                         % (len(del_fichero), len(de_git)))

    truncados = 0
    for i in range(max(len(del_fichero), len(de_git))):
        if i >= len(del_fichero):
            problemas.append("posicion %d: git trae %s %r y el bloque no trae nada"
                             % (i + 1, de_git[i][0][:8], de_git[i][1][:60]))
            continue
        if i >= len(de_git):
            problemas.append("posicion %d: el bloque trae %s %r y git no trae nada "
                             "(commit INVENTADO o fuera del rango)"
                             % (i + 1, del_fichero[i][0], del_fichero[i][1][:60]))
            continue
        h_f, s_f = del_fichero[i]
        h_g, s_g = de_git[i]
        if not h_g.startswith(h_f):
            problemas.append("posicion %d: el bloque dice %s y git dice %s (hash distinto "
                             "o fuera de orden)" % (i + 1, h_f, h_g[:len(h_f)]))
            continue
        if s_f == s_g:
            continue
        if s_g.startswith(s_f):
            truncados += 1
            continue
        problemas.append("posicion %d (%s): el asunto del bloque NO es prefijo del real.\n"
                         "             bloque: %s\n             git   : %s"
                         % (i + 1, h_f, s_f, s_g))

    print("  asuntos TRUNCADOS y declarados como tales: %d" % truncados)
    print()
    if problemas:
        print("  ROJO, %d cosa(s) no cuadran en el bloque de commits:" % len(problemas))
        for x in problemas:
            print("     %s" % x)
        print()
        print("  BLOQUE DE COMMITS: NO CALZA CON GIT")
        return 1
    print("  BLOQUE DE COMMITS: IDENTICO A GIT (%d commit(s), mismo orden, %d asunto(s) "
          "truncado(s) declarado(s))" % (len(de_git), truncados))
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
    ap_arg.add_argument("--comparar-commits", default=None, metavar="RUTA",
                        help="TAREA 2.d (vuelta 141): coteja el bloque entre "
                             "<!-- COMMITS TALLADOS --> y su cierre contra "
                             "git log <apertura>..HEAD (mismo numero, mismos hashes, "
                             "mismo orden), declarando el truncado de asunto")
    ap_arg.add_argument("--registro", default=None, metavar="RUTA",
                        help="TAREA 2.d: con --tramo-cadena, niega que alguna unidad tallada "
                             "ya tenga decision NO SE ENLAZA en este registro jsonl "
                             "(docs/plan/OP_E_01_DECIDIDAS.jsonl)")
    a = ap_arg.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    con_miles = not a.sin_miles

    if a.comparar_commits is not None:
        return comparar_commits(a.vuelta, a.comparar_commits)

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
        commit_ap, asunto_acta = commit_apertura_desde_git(a.vuelta, rama, fallos)
        # TAREA 2.b (vuelta 81): el HEAD real de la apertura, sellado por el
        # ejecutor, mas el chequeo de que su arbol de dataset/ coincide con el
        # del commit del acta. Si no coinciden, ROJO: las cifras de apertura
        # no son fiables para el commit que la fila nombra.
        head_real = leer_head_apertura(a.vuelta, fallos)
        procedencia_sello = procedencia_sello_apertura(a.vuelta, rama, head_real, fallos)
        # TAREA 2.4 (vuelta 106): el HEAD de cierre, leido de SALIDA_V<N>_HEAD_CIERRE.txt,
        # nunca tecleado. Ver leer_head_cierre() para el motivo.
        head_cierre = leer_head_cierre(a.vuelta, fallos)
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
        celda_identidad_ap = (
            "rama `%s`, commit del acta `%s` (asunto real leido de git log: %r), "
            "HEAD real de apertura `%s` (%s, leido de git log --diff-filter=A), arboles "
            "de `dataset/` %s"
            % (rama, commit_ap, asunto_acta, head_real[:8], procedencia_sello,
               "IGUALES: VERDE" if arbol_verde else "?")
        )
        # TAREA 2.4 (vuelta 106): la columna de CIERRE ya no repite la celda de
        # apertura. Publica su propio HEAD, leido de SALIDA_V<N>_HEAD_CIERRE.txt
        # (leer_head_cierre), que es el remedio de la caida 1.1 del acta de la
        # vuelta 105 ("el hash de HEAD de tu cabecera contradice tu propio
        # fichero").
        celda_identidad_ci = (
            "rama `%s`, HEAD de cierre `%s` (leido de `SALIDA_V%d_HEAD_CIERRE.txt`, "
            "sellado tras la ultima operacion)"
            % (rama, head_cierre[:8] if head_cierre else "?", a.vuelta)
        )
        f.append(("identidad: rama y commit de apertura (leidos de git, no tecleados)",
                  celda_identidad_ap, celda_identidad_ci))

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
