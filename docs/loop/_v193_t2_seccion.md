### TAREA 2. LOS ARNESES QUE NO REPRODUCEN. **CERRADA EN VERDE, Y CON UN CUARTO CASO QUE EL ACTA NO TRAIA.**

**LO QUE ENCONTRE AL ENTRAR, ANTES DE TOCAR NADA** (bloque `F` del sello de
apertura): las tres selladas del acta 193 estaban INTACTAS y ninguna de cero
bytes, con los mismos bytes que el acta publica, **5836**, **4173** y **2433**
por LF, y los mismos `sha256` `bc8d7273baf30644`, `6de586c0e5c7a104` y
`d2c99c7e27f40183`.

**a) LOS DOS PRIMEROS: SUJETO CONGELADO, POR `git show` SOBRE UN COMMIT CLAVADO.**
Ninguno se declara como `CASO DECLARADO`: **los dos se congelan**, que es la
salida que el encargo pone primero.

| arnes | lo que leia VIVO | lo que lee ahora |
|---|---|---|
| `vuelta191_tarea3_mutacion_lineas.py` | el censo de `scripts/loop` del arbol, la lista de `vuelta191_*` del arbol, y `docs/plan/LECTURAS_DIRIGIDAS.md` | los tres, del arbol del commit `21ffca0c`, que es **el commit que ANADIO su salida sellada**, localizado con `git log --diff-filter=A` |
| `vuelta191_tarea6_mutacion_bloque_tallado.py` | `docs/loop/REPORTE.md`, que es un fichero distinto en cada vuelta por construccion | `docs/loop/reportes/REPORTE_V191.md` del commit `92a09bfa`, o sea **un reporte archivado, que no se reescribe, sacado de un commit, que no se mueve** |

**Y EL COMMIT CLAVADO DEL SEGUNDO NO ES EL DE SU PROPIA SELLADA, Y SE DICE POR
QUE:** se probo primero con `576fa467`, el commit que anadio su salida, y **en su
arbol el reporte de la 191 todavia NO estaba archivado**, porque el archivado
ocurre al cerrar la vuelta siguiente. **El arnes salio ROJO por sujeto vacio**,
que es la conducta correcta de una guarda que no puede pasar en verde sobre un
vacio, y de ahi salio el commit bueno.

**LO QUE ESTE CONGELADO CUESTA, DICHO Y NO CALLADO.** En el primero, **el censo
del arbol VIVO deja de correr dentro del arnes**; no se pierde, y se dice con su
nombre: vive en `scripts/loop/vuelta191_tarea3_censo.py`, que corre con
`--commit HEAD` y **no esta en la nomina**, que es donde tiene que vivir un
sujeto que se mueve. En el segundo, **el bloque `D` deja de lanzar
`tallar_cabecera_reporte.py --comparar`**, porque ese comando **RE TALLA leyendo
git en cada corrida** y su fila de identidad busca el asunto de un commit en una
ventana de `git log`: es sujeto vivo por dentro aunque el fichero comparado sea
fijo. **Tampoco se pierde:** el `--comparar` sobre el reporte VIVO sigue
corriendo cada vuelta en `cerrar_reporte.py`, que es su sede. **En su lugar el
bloque prueba algo mas estrecho y mas duro: que la comparacion es BYTE A BYTE,
mutando UN SOLO BYTE dentro de una linea sin cambiar ni el largo ni el numero de
lineas**, que es justo lo que una comparacion por lineas o por conteo no veria.

**b) EL TERCERO YA NO IMPRIME SU `mkdtemp`.** El directorio se sigue fabricando y
se sigue retirando (`P.16`), y se sigue comprobando que quedo retirado. Lo unico
que se calla es su nombre, **que es aleatorio por construccion y no prueba nada**.

**c) LA GUARDA QUE NO LO VIO, ARREGLADA, Y SIN AFLOJAR NADA.**
`guarda_de_entrada_a_la_nomina.py` gana el carril `--reproduccion`, que **corre
cada arnes reclamado DOS VECES y compara su salida sellada byte a byte**, mide
las selladas antes, y **restaura con `git checkout --` REMIDIENDO** antes de dar
nada por restaurado. **Y la corrida SIN esa bandera declara en su propia salida
que su columna de huella es UN INDICIO Y NO UN VEREDICTO DE REPRODUCCION**, con
la causa medida al lado. El carril es caro y por eso no corre por defecto: eso se
dice, no se esconde.

**LA VARA PARA LOCALIZAR LA SALIDA SELLADA VA EN DOS PASADAS, Y LA SEGUNDA NACIO
DE UNA MEDICION FALLIDA MIA.** Con la pasada del literal suelto, **los CUATRO
arneses reclamados salian `NO MEDIBLE`**, porque sus docstrings NOMBRAN otras
salidas de las que hablan. La pasada que manda mira **la asignacion de modulo
`SALIDA = os.path.join(LOOP, "...")`**, o sea la maquina y no la prosa. **Y la
sede por defecto del arnes iba mal**: buscaba en `docs/loop`, donde viven las
salidas, y los arneses viven donde `verificar_mutaciones_viejas.py` los busca.
Las dos correcciones van declaradas dentro del propio fichero.

**d) EL CASO POSITIVO POR MUTACION, Y CAE.** Se fabrican DOS arneses que **la
huella de texto ve EXACTAMENTE IGUAL** (los dos nombran `mkdtemp`) y que se
comportan al reves: uno escribe siempre lo mismo y el otro escribe una linea
distinta en cada corrida. **La huella dice `CONGELADO` de LOS DOS**, y la corrida
doble dice `reproduce=True` y `reproduce=False`. Mas la mutacion de que un arnes
que no nombre una sola salida sale `NO MEDIBLE` y **no se cuela como
reproducido**. Salida:
`docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt`, **VEREDICTO: VERDE**.

**e) LA NOMINA NO SE TOCO.** Sigue en **127 entradas**, leidas de `VMV.VIEJAS` en
el bloque `H` del sello de apertura. No se poda, no se adelanta y no se le meten
entradas nuevas.

**UN CUARTO ARNES QUE NO REPRODUCIA, Y NO ESTABA EN EL ACTA. LO CAZO EL CARRIL
NUEVO EN SU PRIMERA CORRIDA DE VERDAD.** `vuelta191_tarea4_mutacion_veredicto.py`
imprimia **los bytes ABSOLUTOS de `cerrar_reporte.py`**, que crece cada vuelta.
Daba **6072 bytes las dos corridas y `sha256` DISTINTO**, porque las dos cifras
tienen el mismo numero de digitos: **una vara que solo mirase bytes lo habria
dado por bueno**. Su sujeto sigue vivo A PROPOSITO, porque lo que prueba es que
**la guarda de HOY** se puede quitar de una copia y que la copia compila. **La
reproduccion no se le exige al sujeto: se le exige a la SALIDA**, y lo que se
imprime ahora es la DIFERENCIA, que solo depende del trozo sustituido. Iba a
entrar en la bateria de la 194 exactamente igual que los otros tres.

**f) AL CERRAR, LOS CUATRO CORRIDOS DOS VECES, CON SUS BYTES Y SUS `sha256`.**
Tabla pegada de `docs/loop/SALIDA_V193_T2C_GUARDA_REPRODUCCION.txt` (4367 bytes),
que es el fichero del que sale y que existe y no esta vacio:

| arnes | sellada (LF, `sha256`) | corrida 1 | corrida 2 | reproduce | contra su sellada |
|---|---|---|---|---|---|
| `vuelta191_tarea3_mutacion_lineas.py` | 7246, `c053d5ebeee3afd2` | 7246, `c053d5ebeee3afd2` | 7246, `c053d5ebeee3afd2` | **True** | **True** |
| `vuelta191_tarea4_mutacion_veredicto.py` | 6426, `c7893936f11c7023` | 6426, `c7893936f11c7023` | 6426, `c7893936f11c7023` | **True** | **True** |
| `vuelta191_tarea6_mutacion_bloque_tallado.py` | 3976, `a5b846ea7deb3868` | 3976, `a5b846ea7deb3868` | 3976, `a5b846ea7deb3868` | **True** | **True** |
| `vuelta192_tarea4_mutacion_cuarta_puerta.py` | 4282, `4779fcd04bc5b2da` | 4282, `4779fcd04bc5b2da` | 4282, `4779fcd04bc5b2da` | **True** | **True** |

**CIFRA arneses medidos: 4. CIFRA NO MEDIBLES: 0. CIFRA QUE NO REPRODUCEN: 0.
CIFRA SIN RESTAURAR: 0. VEREDICTO DE REPRODUCCION: VERDE.** **NO HAY PARADA: la
194 no se abre con esto abierto.**

**LAS SELLADAS VIEJAS NO SE BORRAN, QUE UNA CORRECCION QUE TAPA LO QUE CORRIGE NO
SE PUEDE AUDITAR.** Los cuatro cortes anteriores quedan al lado con su nombre y
su vuelta: `SALIDA_V191_T3_MUTACION_LINEAS_CORTE_191.txt`,
`SALIDA_V191_T4_MUTACION_VEREDICTO_CORTE_191.txt`,
`SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO_CORTE_191.txt` y
`SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA_CORTE_192.txt`.
