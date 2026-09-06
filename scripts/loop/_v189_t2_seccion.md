### TAREA 2. LA BATERIA DE MUTACIONES, ENTERA, POR TRAMOS Y SOLA. CORRIDA, Y CON UN ROJO DE VERDAD CAZADO

#### 2.a. PRIMERO EL CLON, QUE ERA BLOQUEANTE, Y SU COTEJO PEGADO SALGA LO QUE SALGA

`scripts/loop/vuelta189_bateria_por_tramos.py`, **clon declarado** de
`vuelta183_bateria_por_tramos.py`. El cotejo lo corrio
`scripts/loop/cotejar_clon_declarado.py --a ... --b ... --num-a 183 --num-b 189`
y su salida entera vive en `docs/loop/SALIDA_V189_T2_COTEJO_CLON.txt` (**3022
bytes en disco**). **Contado de ese fichero**:

| lo que el cotejo dice | cifra |
|---|---|
| FICHERO ENTERO / SOLO DOCSTRING / SOLO LA MAQUINA | **DIFIERE / DIFIERE / DIFIERE** |
| AST del fichero entero / AST sin el docstring | **DIFIERE / DIFIERE** |
| nodos del arbol sin docstring, A contra B | **4074 contra 4070** |
| lineas de maquina que difieren | **13** |
| **SENTENCIAS DE CODIGO** | **3** |
| **LITERALES DE TEXTO** | **10** |

**AQUI NO SE AFIRMA QUE EL DIFF SALGA VACIO, Y ES EL CASO QUE LA `4.8` DEL ACTA
DESCRIBE.** De las 3 SENTENCIAS DE CODIGO, **una sola es del original**:
`A:108 TRAMOS_QUE_MANDA_LA_DECISION = 9`, **retirada en el clon**; las otras dos
que el instrumento lista (`B:98` y `B:99`) son lineas de comentario que su
atribucion por linea arrastra. **Por que se retira, medido y no supuesto:** la
constante **no la usa nadie** (`grep -rn TRAMOS_QUE_MANDA_LA_DECISION scripts/
docs/` da su propia definicion y dos salidas selladas que la citan, y ninguna
lectura), y su valor **9 ya no dice la verdad**: con la nomina de hoy el reparto
da **10**. Dejar en el fuente un numero muerto que miente es la especie de cosa
que esta campana persigue. **Se declara, se publica y no se esconde detras de
"solo cambia texto".**

#### 2.b. LAS DOS COMPROBACIONES ANTES DE LANZAR NADA, QUE ERAN LA MITAD DEL ENCARGO

**`--plan`** (`docs/loop/SALIDA_V189_T2_PLAN.txt`), **computado y no tecleado**:

- **CIFRA entradas de la nomina: 125.** **CIFRA tamano de tramo: 13.**
  **CIFRA tramos: 10.** **CIFRA suma de las entradas de todos los tramos: 125.**
- **Nueve tramos de 13 y uno de 8**, publicados tramo a tramo por el propio
  instrumento.
- **LA ESTIMACION, DICHA COMO ESTIMACION Y CON SU CORTE PEGADO EN LA MISMA
  LINEA:** `entre 4.3 y 5.6` minutos por tramo y `entre 41.2 y 53.8` de la nomina
  entera, `(corte: HEAD d1c2f6d6c51c, nomina de 125 entradas contada en esta
  corrida)`.

**`--siguiente` ANTES DE EMPEZAR** (`docs/loop/SALIDA_V189_T2_SIGUIENTE_ANTES.txt`):
**`CIFRA tramos CON salida sellada no vacia: 0`**, **`CIFRA tramos que FALTAN:
10`**, **`EL SIGUIENTE ES EL TRAMO 1`**. **El clon cuenta desde cero**, que era
exactamente lo que la adjudicacion de la seccion 5 del acta pedia. Y su guarda de
atribucion, corrida sobre el propio fuente: **`CIFRA literales de vuelta clavados
en lineas que escriben: 0`**.

**EL CONTRASTE, QUE ES LO QUE PRUEBA QUE EL CLON HACIA FALTA.** El bloque **H.4**
del sello de apertura de esta vuelta corrio el lanzador **de la 183** y sello su
respuesta: **`CIFRA tramos CON salida sellada no vacia: 9`**, **`CIFRA tramos que
FALTAN: 1`**, **`EL SIGUIENTE ES EL TRAMO 10`**. Correrlo tal cual habria corrido
**8 arneses de 125** y se habria declarado corrido. **Y no se borro nada:** el
bloque **H.5** midio las **nueve** salidas `SALIDA_V183_BATERIA_TRAMO_n.txt` una
a una, y ahi siguen.

#### 2.c. LOS DIEZ TRAMOS, CADA UNO SELLADO Y COMMITEADO ANTES DEL SIGUIENTE

**LA TABLA SALE DE `--componer`, QUE LEE LOS FICHEROS, Y NO DE MI MEMORIA**
(`docs/loop/SALIDA_V189_T2_COMPONER_CONSOLA.txt`). La columna de minutos la
publica cada tramo al cerrarse:

| tramo | fichero | bytes | lineas | sha256 LF | entradas | minutos medidos |
|---:|---|---:|---:|---|---:|---:|
| 1 | `SALIDA_V189_BATERIA_TRAMO_1.txt` | 9296 | 122 | `0e27295e3ea0` | 13 | 2,6 |
| 2 | `SALIDA_V189_BATERIA_TRAMO_2.txt` | 7529 | 116 | `0854947a9b4e` | 13 | 5,8 |
| 3 | `SALIDA_V189_BATERIA_TRAMO_3.txt` | 7594 | 116 | `a85d7c71461b` | 13 | 8,3 |
| 4 | `SALIDA_V189_BATERIA_TRAMO_4.txt` | 7606 | 116 | `9f3a18ee5eae` | 13 | 2,4 |
| 5 | `SALIDA_V189_BATERIA_TRAMO_5.txt` | 7566 | 116 | `87c71accfa34` | 13 | 1,9 |
| 6 | `SALIDA_V189_BATERIA_TRAMO_6.txt` | 7626 | 116 | `0ff009ab23dc` | 13 | 2,3 |
| 7 | `SALIDA_V189_BATERIA_TRAMO_7.txt` | 7843 | 118 | `7f166322f04e` | 13 | 2,0 |
| 8 | `SALIDA_V189_BATERIA_TRAMO_8.txt` | 7595 | 116 | `5156306187dc` | 13 | 2,3 |
| 9 | `SALIDA_V189_BATERIA_TRAMO_9.txt` | 8062 | 116 | `5ce6ccd89c3e` | 13 | 2,1 |
| 10 | `SALIDA_V189_BATERIA_TRAMO_10.txt` | 6861 | 99 | `f7ae02f06cce` | 8 | 1,2 |

**NINGUNA MIDE CERO BYTES**, y esa es la condicion que el encargo pone para que
una salida sellada cuente como hecha.

**EL RELOJ: LA ESTIMACION ERA ESTIMACION Y LA MEDICION MANDA.** Suma de los diez
tramos: **30,9 minutos** contra **41,2 a 53,8** estimados. Pero la estimacion
**por tramo** se quedo corta en dos de los diez: el tramo 3 tardo **8,3** minutos
contra un techo estimado de **5,6**. **Las dos cifras se publican y la de verdad
es la medida.**

#### 2.d. LA COMPOSICION, Y LA COBERTURA LEIDA DE LAS SALIDAS Y NO DEL REPARTO

`--componer` cerro en **VERDE**:

- **CIFRA entradas que los tramos dicen haber corrido: 125.**
- **CIFRA entradas de la nomina que NINGUN tramo corrio: 0.**
- **CIFRA entradas corridas que NO estan en la nomina: 0.**
- **CIFRA entradas corridas MAS DE UNA VEZ: 0.**
- La salida unica `docs/loop/SALIDA_V189_BATERIA.txt`: **81968 bytes, 1236
  lineas, sha256 LF `f6b49dab8d357cb3bf4156d582c7fa88d1d3b3d86ea129cfcc128488d4212743`**.

**`--siguiente` CORRIDO DESPUES** (`docs/loop/SALIDA_V189_T2_SIGUIENTE_DESPUES.txt`):
**`CIFRA tramos CON salida sellada no vacia: 10`**, **`CIFRA tramos que FALTAN:
0`**. **LA BATERIA DE LA 189 QUEDA CORRIDA ENTERA SOBRE LA NOMINA DE HOY.**

#### 2.e. EL ROJO DE VERDAD QUE LA BATERIA CAZO, TRAIDO SIN RE CORRERLO Y SIN ARREGLARLO

**`vuelta172_tarea5_mutacion_cierre.py` sale `exit 1 NO MORDIO` en 10,9s**, en el
**tramo 7**, linea **52** de `docs/loop/SALIDA_V189_BATERIA_TRAMO_7.txt`. Es un
**arnes ya sellado**, o sea el caso que el punto 5 del encargo describe: **se
detiene AL ARNES, no a la vuelta**, y **no se re corre ni se arregla**.

**EL CONTRASTE, LEIDO DE UNA SALIDA SELLADA Y NO RECORDADO:** en
`docs/loop/SALIDA_V183_BATERIA_TRAMO_7.txt`, **linea 52**, el **mismo** arnes
daba **`exit 0 OK` en 2,2s**.

**LO QUE SE PUEDE AFIRMAR Y LO QUE NO, SEPARADO:**

- **MEDIDO:** su sujeto son **cadenas literales en memoria** (su propio docstring
  lo declara y su fuente lo confirma: *"todos los reportes de mentira son CADENAS
  literales de este proceso. NO se lee el disco"*), asi que **no puede haber
  cambiado por el dia**. Lo que prueba es
  `cerrar_reporte.piezas_que_faltan()`, que importa.
- **MEDIDO:** entre las dos corridas, `scripts/loop/cerrar_reporte.py` **si se
  movio**: es el sujeto que la **TAREA 4.b de la vuelta 188** cambio para exigir
  que las secciones sean **unicas y esten en orden**.
- **NO MEDIDO, Y POR ESO NO SE PUBLICA COMO CAUSA:** cual de sus casos concretos
  es el que deja de morder. **La salida sellada de la bateria no conserva el
  stdout del arnes**, solo su veredicto, y **averiguarlo exigiria re correrlo**,
  que es exactamente lo que el encargo prohibe. **Se trae asi, con la causa
  acotada y no afirmada.**

**LA EXCLUSION NO ES MUDA, Y HOY NO ESTA VACIA POR PRIMERA VEZ.**
`docs/loop/ROJOS_DE_LA_VUELTA_189.txt` (**964 bytes, sha256 LF
`aefae0656fe1612f`**) lleva su linea con **nombre, ruta de su salida en rojo y
motivo**, y `scripts/loop/vuelta189_tarea2_nomina.py` la lee con
`rojos_registrados()` y `particion_por_rojo()`, **importadas** del instrumento de
la 188 y no clonadas. Su salida
(`docs/loop/SALIDA_V189_T2_NOMINA.txt`, **4822 bytes**) publica
**`CIFRA arneses EXCLUIDOS de la doble corrida: 1`** con el excluido nombrado y
**`CIFRA arneses que SI se corren dos veces: 1 de 2`**.

#### 2.f. EL exitcode 1 DE LOS DIEZ TRAMOS, QUE NO ES DE NINGUN ARNES

**DISCUTIBLE MARCADO.** Los diez tramos salen con **exitcode 1**, y **en nueve de
los diez no cayo ni un arnes**. La fuente es siempre la misma linea, identica en
los diez:

> `ROJO: 3 entrada(s) de la nomina NO tienen su sujeto congelado ... La lista
> entera: vuelta186_tarea2c_mutacion_cierre_tardio.py,
> vuelta187_tarea4_mutacion_dos_convenciones.py,
> vuelta188_tarea4_mutacion_cobertura_parejas.py`

**ES LA DEUDA QUE EL ACTA 189 YA MIDIO** en su seccion 2, con estas palabras:
*"el `ROJO` es solo `guarda_del_sujeto_congelado(): 3 entradas`"*, **y que su
`4.7` deja abierta a proposito**: `NO DECIDIBLE` se queda como esta porque deja
la deuda visible, y el remedio (separar en la salida las que traen motivo escrito
de las que no) **va encargado a la vuelta 190**.

**POR QUE SEGUI EN VEZ DE PARAR, Y ES LO DISCUTIBLE:** el punto 5 del encargo
manda detener **AL ARNES**, y aqui **no cayo ningun arnes**: cayo una guarda de
nomina que **cae igual en los diez tramos**. Parar en el tramo 1 habria dejado la
bateria sin correr, y `AUDITOR.md` 6.1 la manda **entera**. **No lo traigo como
PARADA** porque no contradice ninguna regla vigente ni ninguna cifra publicada:
es una deuda declarada, visible y con remedio ya encargado. **Lo marco como
discutible para que se adjudique.**

#### 2.g. LA DOBLE CORRIDA, LA NOMINA AL CERRAR Y EL ARBOL

**LA DOBLE CORRIDA DE LOS 125 LA HACE LA PROPIA BATERIA** (TAREA 2.f de la vuelta
141) y su veredicto esta en los diez tramos: **`NO REPRODUCIBLE: 0 (ninguna)` en
los diez**. Ningun arnes cambia solo entre dos corridas del mismo dia sobre el
mismo sujeto, asi que **no hay PARADA de esa especie**.

**LA NOMINA AL CERRAR** (`docs/loop/SALIDA_V189_T2_NOMINA.txt`, contado de ese
fichero): **censo 185, nomina 125, `VARA_DEL_CENSO` 148**,
**`arneses_que_faltan()` ultima vuelta 188 y FALTAN 0**,
**`nomina_invisible_al_censo()` 0**, **`guarda_del_sujeto_congelado()` 3**.
**LA NOMINA NO SE PODO**: sigue en 125, y la opcion `c` que el fundador rechazo
el 5 sep no se toco.

**LA DOBLE CORRIDA DEL ARNES QUE NACE HOY**, que es el carril `--mutacion` del
registrador: **corrida 1 y corrida 2, exitcode 0 las dos, y el mismo sha256 LF
`ac68abfc3a17628f`** sobre 5068 bytes. Y el registrador **sin argumentos**,
corrido dos veces mas: **exitcode 0 las dos y el mismo sha256 LF
`49cbe8bf0840e5d8`**, que es su idempotencia otra vez.

**Y UNA MEDICION QUE NO ESTABA ENCARGADA Y SALIO AL MEDIR, ANOTADA Y NO
ARREGLADA:** el arnes que nace hoy **el censo NO LO VE**. `PATRON_ARNES` es
`^vuelta(\d+).*(?:mutacion|caso_positivo|simular).*\.py$` y **mira el nombre del
fichero**, y este arnes vive en el carril `--mutacion` de
`vuelta189_tarea1a_registrar_acta189.py`, que no dice `mutacion` en su nombre.
**No lo introduce esta vuelta** (el registrador de la 188 tiene la misma forma, y
tampoco esta en la nomina) y **esta vuelta no lo arregla**, porque su encargo dice
*NADA MAS ENTRA EN ESTA VUELTA*. **Queda anotado con su cifra.**

**EL ARBOL:** `git diff --numstat -- dataset/` da **0 filas** al terminar, medido
por el propio instrumento, y **se midio antes de cada commit de tramo** desde el
tramo 4 en adelante.
