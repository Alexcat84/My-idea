### TAREA 3. LA MESA `OP-L-02`, MEDIDA POR EL MISMO METODO QUE LAS DOS ANTERIORES

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de
`docs/loop/SALIDA_V209_T3A_VARA.txt` y `docs/loop/SALIDA_V209_T3_COTEJO.txt`
con `scripts/loop/_v209_t3_seccion.py`, que **cae en rojo si no puede leer
una**; y **la tabla del cotejo se reconstruye barriendo el fichero**, no se
copia a mano.

#### 3.a. LA VARA, SELLADA EN SU PROPIO COMMIT ANTES DE COTEJAR NADA

La vara vive en `scripts/loop/_v209_t3_vara.py` y quedo **committeada antes
de abrir ningun documento del cotejo**. El cotejo la **IMPORTA** y no puede
cambiarla: si pudiera, el sello no valdria para nada. Es el metodo que la 207
uso con `OP-L-01` y la 208 con `OP-L-03`, las dos veces bien.

**LA SEDE FINA ES `campo[indice]` Y NO UN NUMERO DE LINEA**, porque la ficha
entera vive en UNA sola linea de `docs/plan/OPERACIONES.jsonl`, la **42**, que
mide **7989** bytes en disco y **7989** bytes normalizado a LF. Decir *linea 42*
dieciocho veces no localiza nada.

| que se sella | cifra |
|---|---:|
| puntos de la vara | **18** |
| de ellos DOCUMENTALES | **13** |
| de ellos NO DOCUMENTALES | **5** |
| citas que NO aparecen VERBATIM en su campo | **0** |
| controles positivos que FALLAN | **0** |
| candidatos a NO DOCUMENTAL cuyo literal SI aparece en el corpus | **0** |
| discrepancias con el contraste del encargo | **0** |

**EL ESCARMIENTO, APLICADO Y NO SOLO CITADO.** Antes de sellar un punto como
NO DOCUMENTAL se busca su literal en el corpus y **la vara CAE EN ROJO si
aparece**: da **0**. Los tres primeros (`V.1`, `V.2` y `V.3`) **no se buscan
a proposito y se dice por que**: son campos de la propia ficha (`tipo`,
`orden`, `fecha_corte`) y su unica sede posible es ella. Y **la sede de la
propia ficha queda FUERA de esa busqueda**, porque encontrar ahi el literal de
su propio campo probaria que la ficha existe, no que tenga sede documental.

**LA BUSQUEDA VA TAMBIEN POSITIVA** (`EJECUTOR.md` 9, una busqueda negativa no
se puede citar sola), con un literal de control por cada uno de los **11**
documentos del corpus: **0 fallan**.

**Y LA PRIMERA CORRIDA DE LA VARA CAYO EN ROJO, POR MI CONTROL Y NO POR EL
FICHERO.** El control de `SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` era la palabra
`marcador` y aparecia **0** veces: ese fichero habla del marcador **por su
sede y su cifra** (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl: 3388 filas`, en su
linea **48**) y **nunca escribe la palabra**. **Un control positivo que no
aparece no invalida el documento: invalida el control**, y para eso esta la
guarda. Quedo por `OP-L-02`, que aparece en su linea **9**. La correccion va
**declarada dentro del propio sello y con el texto viejo sin borrar**, y **no
toco ni un punto de la vara ni el reparto documental**.

#### 3.b. LOS DOS AVISOS DE ESTA FICHA, LOS DOS MEDIDOS

**LA `evidencia` TIENE UN SOLO ELEMENTO Y ES PROSA QUE NO NOMBRA NINGUN
FICHERO**, y por eso `vuelta150_3_relectura_expediente.py` la lista como la
unica de las tres mesas sin documento que medir. **Eso no la deja sin
cotejar:** se coteja contra lo que su prosa AFIRMA, que es una cifra con su
fecha de corte, y esa aritmetica se remide aqui. **CIFRA aritmeticas de la
ficha comprobadas: 11, de las que cuadran 11 y no cuadran 0.**
Las tres cifras de la `evidencia` cuadran entre si (11 mas 194 dan 205) y con
la particion de la `nota` (126 mas 79 dan 205), y **205 menos las 16 de la
segunda tanda dan los 189 del backlog**.

**Y `adjudicacion` Y `nota` SI TRAEN TEXTO, que es lo que las otras dos mesas
no tenian igual:** **260** y **5578** caracteres. **Ahi es donde vive lo que la
mesa decidio**, y de ahi salen la mayoria de los puntos de la vara.

**LAS DOS CIFRAS DEL MARCADOR, PUBLICADAS JUNTAS Y CADA UNA CON SU CORTE**, que
es lo que el encargo manda y lo que el banco `9.21` pide:

| cifra | corte | de donde sale |
|---:|---|---|
| **2.117** | **2026-08-11**, el `fecha_corte` de la ficha | `verificacion[1]`. **TESTIGO Y NO CONDICION** |
| **3388** | **7 sep 2026** | recomputado por mi de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` linea a linea |

**NO SE ARREGLA TOCANDO LA FICHA.** El instrumento no fallo, **la cifra se
quedo vieja** (banco `9.21`), y la clausula exige que la OPERACION no mueva el
marcador, **no que el marcador valga 2.117 hoy**. La `verificacion[3]` de la
propia ficha ya le puso el corte al lado el 4 sep 2026 por CORRECCION
DECLARADA, sin borrar el numeral viejo.

**MI RECOMPUTO DEL MARCADOR: 3388 filas, repartidas en A 551, B 72, C 5 y D 2760**,
con **3388** puestos distintos y **0** huecos. **Calza con el sello del auditor**
`docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json`: **SI,**.

**UNA CAIDA MIA CAZADA ANTES DE PUBLICAR, Y VA MARCADA COMO `C.2`.** La primera
version del cotejo leia el puesto como `puesto`, y **ese campo no existe en ese
archivo**: se llama `puesto_intra`. `.get()` devolvia vacio en las **3388** filas,
el conjunto se quedaba con un solo valor y la salida publicaba **CIFRA puestos
distintos: 1** sobre un archivo de **3388** puestos. **Ese 1 no era una medicion:
era el uno de un patron roto**, que es justo lo que `EJECUTOR.md` 9 prohibe
publicar como hecho del mundo. Arreglado el campo, **queda ademas una guarda**
que comprueba que el campo se lee en todas las filas **antes** de publicar la
cifra, y que la declara NO COMPUTABLE si no. Va entera en la seccion 8.

#### 3.c. EL COTEJO PUNTO POR PUNTO, CON SU CITA EN CADA FILA

| punto | veredicto | sede citada | por que entra asi |
|---|---|---|---|
| `V.1` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `tipo`, y su criterio de HECHO en `docs/plan/08_VERIFICACION.md:29` | el campo dice 'MESA', y la fila 06 MESAS existe en su linea medida |
| `V.2` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `orden` | vale 2, la segunda de las tres mesas |
| `V.3` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `fecha_corte` | vale '2026-08-11', y es contra ese corte contra el que se juzgan sus cifras |
| `V.4` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `depende_de`, y las tres halladas en ese mismo fichero | las 3 dependencias existen; 0 no se encuentran |
| `V.5` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `evidencia[0]` | sus tres cifras cuadran entre si (11 mas 194 da 205) y con la particion de la nota (126 mas 79 da 205); 11 de 11 aritmeticas de la ficha cuadran |
| `V.6` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campos `verificacion[0]` y `nota` | las tres nominas SI se pueden nombrar desde la propia ficha (3 de 3), asi que NO hay parada por texto insuficiente |
| `V.7` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `verificacion[1]`, con su correccion en `verificacion[3]` | la clausula exige que la OPERACION no mueva el marcador, no que valga 2.117 hoy; las dos cifras van publicadas juntas con su corte (2.117 al 2026-08-11 y 3388 al 7 sep 2026) |
| `V.8` | **A MEDIAS** | `docs/plan/OPERACIONES.jsonl:42` campos `verificacion[2]`, `nota` y `adjudicacion` | 3 de 4 grupos del backlog llevan su motivo escrito y no solo su cuenta |
| `V.9` | **CUBRE** | `docs/INTRA_DOMINIO_VEREDICTOS.jsonl:recomputado entero, 3388 filas` y `docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json:1` | mi recomputo da 3388 filas con A 551, B 72, C 5 y D 2760, identico a lo que la correccion declarada publica y al sello del auditor |
| `V.10` | **CUBRE** | `docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt:9` | la ruta existe y no mide cero bytes; de las 11 rutas del corpus fallan 0 |
| `V.11` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `adjudicacion` | la decision de la mesa esta escrita, y la `nota` le pone al lado su motivo y su cobertura, que es lo que la fila 06 MESAS exige |
| `V.12` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `adjudicacion`, cotejado contra el reparto por nomina de la `nota` | 2 A mas 14 D dan 16, y las tres nominas leidas (8 mas 5 mas 3) tambien dan 16 |
| `V.13` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `nota`, y las tres nominas en `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt:45` | las tres estan NOMBRADAS y sus tres cuentas suman 16 |
| `V.14` | **CUBRE** | `docs/plan/LD_SALES_ROADMAP.md:48` a `docs/plan/LD_SALES_ROADMAP.md:195` | las 5 cabeceras estan, y su reparto contado de ellas da 1 A y 4 D, que es el `SALDO: 1 A y 4 D` de la ficha |
| `V.15` | **A MEDIAS** | `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt:35` | la salida sellada trae las 6 nominas y suma 0 pares SIN veredicto de ninguna sede, o sea que la parte de `cero pares sin veredicto` CUBRE; pero `cobertura COMPLETA` solo se sostiene en la convencion LITERAL, porque la NOMINA 2 publica `0 de 0` con 5 de sus 6 miembros colapsados por alias. Las dos convenciones van publicadas y manda la LITERAL |
| `V.16` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:42` campo `nota` | los cuatro grupos suman 189, y 205 menos las 16 de la segunda tanda tambien dan 189 |
| `V.17` | **CUBRE** | `scripts/vuelta16_generar_actos.mjs:8` y el resolutor de la casa | 6 miembros escritos, 6 vivos tras resolver y 15 pares posibles, recomputado por mi con `mapa_de_alias()` y `resolver()` |
| `V.18` | **CUBRE** | `docs/plan/OPERACIONES.jsonl:las 71 fichas barridas` | el barrido da 0 apariciones, y su CONTROL POSITIVO da 47 fichas con `nodos` no vacio, asi que el cero no es el cero de un patron roto |

**CIFRA filas del cotejo SIN cita de fichero y linea: 0.** Ninguna sin cita,
que es lo que el encargo exige.

**LAS MEDICIONES QUE SOSTIENEN ESAS FILAS, CADA UNA CON SU CIFRA:**

| que se midio | cifra |
|---|---:|
| las tres nominas de `verificacion[0]` que la ficha NOMBRA | **3** de 3 |
| cabeceras `LD-66` a `LD-70` halladas en su documento | **5** de 5 |
| reparto de esas cinco, contado de sus cabeceras | **1** A y **4** D |
| nominas de la ficha en su salida sellada de la 169 | **6** |
| pares SIN veredicto de ninguna sede, sumando las seis | **0** |
| fichas barridas para la busqueda negativa | **71** |
| apariciones de los nodos del acto en `nodos`, `preservar`, `eliminar` y `superviviente` | **0** |
| control positivo del mismo barrido: fichas con `nodos` no vacio | **47** |
| rutas del corpus comprobadas, y de ellas las que fallan | **11** y **0** |
| dependencias de la ficha que NO existen | **0** |
| grupos del backlog, y de ellos los que llevan su motivo escrito | **4** y **3** |

**LA BUSQUEDA NEGATIVA SE RE-VERIFICO EN VEZ DE CITARSE** (`EJECUTOR.md` 9): la
`nota` declara un barrido de las fichas buscando los nodos del acto, y aqui se
repite entero sobre las **71** de hoy. Da **0** apariciones, **y su CONTROL
POSITIVO da 47 fichas con `nodos` no vacio**, asi que ese cero **no es el cero
de un patron roto**.

**LA DISCREPANCIA QUE ENCUENTRO Y QUE NO RESUELVO COPIANDO** (`EJECUTOR.md` 2).
La `nota` dice *cuadrantes 15 de 15 con 8 A y 7 D*, y la **NOMINA 2** de su
propia salida sellada, que es la de los cuadrantes, publica **0 de 0** con 6
miembros escritos, 1 vivo tras resolver y 5 colapsados por alias. **Son las dos
convenciones y la ficha habla en LITERAL:** el **15** son los pares de SEIS
miembros escritos, que es el universo que habia en el `fecha_corte`
**2026-08-11**; el **0 de 0** es la foto RESUELTA de hoy, **7 sep 2026**,
despues de que cinco de esos seis se fundieran. **Manda la LITERAL** por la
adjudicacion `6.6` del acta 208, **y la resuelta va al lado**. Por eso la `V.15`
entra **A MEDIAS** y no CUBRE ni NO CUBRE.

**LAS DOS CUENTAS, SEPARADAS Y JUNTAS, COMO EN LA 208:**

| cuenta | cifra |
|---|---|
| **la del SELLO**, escrita ANTES de mirar | **18** puntos, **13** DOCUMENTALES y **5** NO DOCUMENTALES |
| **la de los VEREDICTOS**, sacada DESPUES de mirar | **18** emitidos: **16** CUBRE, **2** A MEDIAS y **0** NO CUBRE |

**LA COBERTURA, MEDIDA Y NO NARRADA: 16 de 18 CUBREN**, y su lista NOMINAL de
los que no cubren entero es **`V.8`** (**3** de **4** grupos del backlog
llevan su motivo escrito: el de los **126 que esperan destejido** trae la
cuenta pero no un motivo propio) y **`V.15`** (la cobertura COMPLETA solo se
sostiene en la convencion LITERAL). **Ningun `NO CUBRE`.**

#### 3.d. NO SE CIERRA `OP-L-02` Y NO SE TOCA SU CAMPO `estado`

**AQUI SE MIDE, SE PROPONE Y SE PARA.** La autorizacion del 2.c era **SOLO**
para `OP-L-01`, y la adjudicacion de esta mesa es del auditor. **Lo que
propongo, y no lo adjudico yo:** con **16 de 18** puntos cubriendo, **0 NO
CUBRE** y los dos A MEDIAS declarados con su motivo, la ficha esta **a un
juicio de cerrarse**, y el juicio no es mio.

**Y PARA PROBAR QUE NO LA TOQUE, LA SEDE VA PUBLICADA POR LAS DOS CONVENCIONES
AL ENTRAR Y AL SALIR DE ESTA TAREA:**

| `docs/plan/OPERACIONES.jsonl` | bytes en disco y bytes normalizado a LF | `sha256` disco |
|---|---:|---|
| **AL ENTRAR** | **513043** y **513043** | **`e96dbe74485814e9`** |
| **AL SALIR** | **513043** y **513043** | **`e96dbe74485814e9`** |

**Los cuatro valores son identicos y el `estado` sigue en `LISTA`.** Los `sha256`
de esta tabla **no** son los de mi sello de apertura, y eso tambien se dice: la
TAREA 2 movio ese fichero **antes** de esta tarea, con su propia guarda de una
linea. Lo que esta tabla prueba es que **la TAREA 3 no lo movio**, que es lo
que el `3.d` pide.

#### 3.e. LA TAREA CABE ENTERA CON SUS GUARDAS, Y NO HAY PARADA

**NO QUEDA ABIERTA.** Los **18** puntos estan cotejados, las **18** filas llevan
su cita, el reparto documental se sello antes de mirar y las dos cuentas van
publicadas.

**Y EL CASO DE PARADA QUE EL ENCARGO AVISA NO SE CUMPLE, Y LO MIDO EN VEZ DE
SUPONERLO.** `verificacion[0]` habla de *las tres nominas afectadas* y no las
nombra; **la `nota` SI las nombra las tres**, con su literal y su cuenta:
*cuadrantes de mercado (8)*, *ecuacion de valor (5)* y *el bloque humano de la
supervision de la IA (3)*, y las tres cuentas suman 16. **CIFRA de las tres que
la ficha nombra: 3 de 3.** No hay que adivinar ninguna, asi que **la ficha SI
alcanza para cotejarse sin decidir y NO hay PARADA por este motivo**
(`AUDITOR.md` 3).

