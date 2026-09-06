### TAREA 3. LA BATERIA, ENTERA Y POR TRAMOS. **CORRIDA: LOS DIEZ TRAMOS CON SALIDA SELLADA DEL MISMO CALIBRE. Y LOS DIEZ EN ROJO, PUBLICADOS EN ROJO.**

**(a) EL LANZADOR, CLONADO Y COTEJADO.**
`scripts/loop/vuelta194_bateria_por_tramos.py`, **clon declarado del de la 189**,
que es el ultimo que corrio de verdad. Cotejo con
`scripts/loop/cotejar_clon_declarado.py --exigir-codigo-identico`, salida en
`docs/loop/SALIDA_V194_T3A_COTEJO_CLON.txt`: **SOLO LA MAQUINA: IDENTICO**,
**CIFRA lineas de maquina que difieren: 0**, y **el AST sin el docstring:
IDENTICO**, con **4070 nodos en los dos**. Lo unico que difiere es el docstring
(43 lineas en el original y 37 en el clon). **Su numero no se teclea:** sale de
`os.path.basename(__file__)`, y la guarda `literales_de_vuelta_clavados()`,
corrida sobre el propio fuente en cada invocacion, publica **CIFRA literales de
vuelta clavados en lineas que escriben: 0**.

**(b) EL REPARTO, COMPUTADO Y CON SU FECHA DE CORTE.**
`--plan`, salida en `docs/loop/SALIDA_V194_T3B_PLAN.txt`: **CIFRA entradas de la
nomina: 127**, **CIFRA tamano de tramo: 13**, **CIFRA tramos: 10**, **CIFRA suma
de las entradas de todos los tramos: 127**, con **corte `HEAD e6f46677ab23`,
nomina contada en esa corrida** (banco `9.21`). **Da DIEZ y no nueve**, y el
NUEVE de `AUDITOR.md` 6.1 es la cuenta de la nomina del 5 sep 2026, no un
objetivo: la cifra sale de `len(tramos)` y no de ninguna tecla.

**Y LA TRAMPA DEL ENCARGO, EVITADA Y MEDIDA POR MI.** El bloque `I` del sello de
apertura fecho **una a una** con `git log --diff-filter=A` las nueve salidas que
`vuelta183_bateria_por_tramos.py --siguiente` cuenta: **nacen en las vueltas 183 y
184**, y el asunto del commit que da de alta cada una lo dice en su propia linea.
`--siguiente` de **mi** lanzador contesta **CIFRA tramos CON salida sellada no
vacia: 0** y **EL SIGUIENTE ES EL TRAMO 1**, que es la verdad.

**(c) Y (f) LOS DIEZ TRAMOS, CADA UNO COMMITEADO CON SU SALIDA SELLADA AL
TERMINAR, Y EL RELOJ.** La tabla sale de `--componer`
(`docs/loop/SALIDA_V194_BATERIA_COMPUESTA.txt`) y el reloj de la linea
`DURACION DEL TRAMO (monotona, minutos)` de cada salida sellada:

| tramo | bytes disco | bytes LF | lineas | `sha256` | entradas | minutos | exitcode |
|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 11284 | 11284 | 143 | `a4db8c7b420a` | 13 | 1.1 | 1 |
| 2 | 9528 | 9528 | 137 | `0a08458bafc6` | 13 | 2.9 | 1 |
| 3 | 9582 | 9582 | 137 | `b5f1b65a553e` | 13 | 7.6 | 1 |
| 4 | 9596 | 9596 | 137 | `984584039c88` | 13 | 1.4 | 1 |
| 5 | 9559 | 9559 | 137 | `614226f68f13` | 13 | 0.6 | 1 |
| 6 | 9605 | 9605 | 137 | `6ace42fc6b5a` | 13 | 1.1 | 1 |
| 7 | 9815 | 9815 | 139 | `2a40104d3fbf` | 13 | 0.6 | 1 |
| 8 | 9581 | 9581 | 137 | `5fb1efd65e77` | 13 | 0.8 | 1 |
| 9 | 10058 | 10058 | 137 | `64042ebd6bfe` | 13 | 0.7 | 1 |
| 10 | 9492 | 9492 | 128 | `36e2d04ffc83` | 10 | 0.4 | 1 |

**EL RELOJ, LAS DOS MEDIDAS Y NO UNA:** la **suma de las duraciones monotonas de
los diez tramos da 17.2 minutos**, y la **ventana de reloj de pared del primer
inicio al ultimo fin es de 30.1 minutos** (inicio del tramo 1
`2026-09-06T22:01:57Z`, fin del tramo 10 `2026-09-06T22:32:03Z`), leidas de las
lineas `INICIO` y `FIN (reloj de pared, UTC)` de las dos salidas selladas. **La
diferencia entre las dos no es un misterio y no se disimula:** entre tramo y tramo
van el commit y su hook, y ademas el primer intento del tramo 3 se corto.

**EL TRAMO 3 SE CORTO A MITAD EN SU PRIMER INTENTO**, por tope de tiempo del turno
y no por fallo de la bateria, y **dejo `dataset/metadata/master_graph.json`
tocado** porque el PASO 5 del lanzador no llego a correr. Medido con **las dos
varas y sin elegir la comoda**: `git status --porcelain` lo daba por modificado y
`git diff --numstat` decia **CERO filas**, o sea que la diferencia era de finales
de linea y no de contenido. Restaurado con `git checkout -- dataset/` **sin tocar
ningun final de linea a mano**, y **remedido**: cero y cero. Entero en
`docs/loop/SALIDA_V194_T3_DATASET_RESTAURADO.txt` (1154 bytes). El tramo NO se dio
por corrido: no dejo salida sellada y `--siguiente` volvio a decir TRAMO 3, que es
lo que la 6.1 llama retomar en el tramo siguiente.

**(d) LA DOBLE CORRIDA NO SE AFLOJO.** Cada entrada se corre DOS VECES por el
cotejo de reproducibilidad de la vuelta 141, y el resultado esta en la celda que
lo mide: **`0 sin reproducir` en los diez tramos**.

**(e) `--componer`, QUE ES QUIEN COTEJA EL CALIBRE.** Exitcode 0 y **VERDE**:
**CIFRA entradas que los tramos dicen haber corrido: 127**, **CIFRA entradas de la
nomina que NINGUN tramo corrio: 0**, **CIFRA entradas corridas que NO estan en la
nomina: 0**, **CIFRA entradas corridas MAS DE UNA VEZ: 0**. La cobertura se lee
**de las salidas y no se recalcula del reparto**, que es la mitad que impide el
atajo. La salida unica es `docs/loop/SALIDA_V194_BATERIA.txt`: **102495 bytes en
disco y 102495 normalizado a LF, 1454 lineas, `sha256` LF
`f2d927fa66cdc40a3f157294eaee1c86d1ffb4633a7afbd731befc1cd094b263`**. **Ninguna
salida sellada mide cero bytes**, y esa es la condicion que la 6.1 pone para que
un tramo cuente como hecho.

**(g) LOS ROJOS, PUBLICADOS CON SU TRAMO, SU ENTRADA Y SU MOTIVO, Y NO REPETIDOS
HASTA QUE SALGAN VERDES.** **LOS DIEZ TRAMOS SALEN `ROJO POR FALLO` con exitcode
1**, contados uno a uno de su linea `CLASE DEL VEREDICTO`. **Y la especie del
veredicto dice lo que de verdad paso**, leida de la linea `CIFRA de FALLO` de cada
salida:

| especie | cuantos | en cuantos tramos |
|---|---:|---|
| con ancla perdida | 0 | los diez |
| **que no mordieron** | **1** | **solo el tramo 7** |
| sin reproducir | 0 | los diez |
| **fuera de la nomina** | **6** | **los diez** |
| invisibles al censo | 0 | los diez |
| `SUJETO VIVO` | 0 | los diez |
| `NO DECIDIBLE` con motivo escrito (deuda declarada) | 3 | los diez |

**NINGUN ARNES FALLO POR SU PROPIA MAQUINA SALVO UNO.** Las 127 entradas corrieron
y reprodujeron. Los dos motivos del rojo son **censales y globales**, o sea que
salen en los diez tramos por igual y no dependen de que entradas lleve cada uno:

1. **SEIS ARNESES QUE EL CENSO VE Y LA NOMINA NO TIENE**, nacidos despues de la
   vara de la vuelta 148: `vuelta191_tarea3_mutacion_lineas.py`,
   `vuelta191_tarea4_mutacion_veredicto.py`,
   `vuelta191_tarea6_mutacion_bloque_tallado.py`,
   `vuelta192_tarea4_mutacion_cuarta_puerta.py`,
   `vuelta193_tarea4e_mutacion_sello_entre_procesos.py` y
   `vuelta194_tarea2c_mutacion_sede_del_turno.py`, que es el que esta vuelta
   escribio. **ES NUEVO EN ESTA BATERIA:** la de la 189 publica **0** en esa misma
   celda, medido en su tramo 1. **NO SE ARREGLA AQUI**, y por dos razones escritas
   antes de mirar: el encargo dice **NO TOQUES LA NOMINA**, y podarla o adelantarla
   es la opcion que el fundador RECHAZO el 5 sep 2026. **Y ES LA CORROBORACION
   INDEPENDIENTE DE LO QUE LA TAREA 2 MIDIO**: el censo de la bateria, por su
   cuenta y con otro instrumento, dice que los dos arneses de la cuarta puerta
   **no estan en la nomina**.
2. **TRES ENTRADAS SIN SUJETO CONGELADO**, las tres con motivo escrito:
   `vuelta186_tarea2c_mutacion_cierre_tardio.py`,
   `vuelta187_tarea4_mutacion_dos_convenciones.py` y
   `vuelta188_tarea4_mutacion_cobertura_parejas.py`. **NO ES NUEVO:** la bateria de
   la 189 publica **la misma lista y el mismo rojo en sus diez tramos**, medido en
   sus salidas selladas.

**Y EL UNICO ARNES QUE FALLO POR SU MAQUINA, NOMBRADO CON SU TRAMO Y SU MOTIVO:**
**tramo 7**, `vuelta172_tarea5_mutacion_cierre.py`, **exit 1, `NO MORDIO`, 2.4s**.
Corrido a mano aparte, publica **CIFRA casos: 17 | pasan: 15 | fallan: 2** y
**CIFRA casos que caen al mutar el esperado: 16 de 17**. Los dos que fallan son
`A_con_las_cuatro_no_falta_ninguna` (real 1, esperado 0) y
`A_y_no_nombra_ningun_codigo` (real `['(3)']`, esperado `[]`), y el que no cae al
mutar es el primero de esos dos. **TAMPOCO ES NUEVO:** la bateria de la 189 lo
publica igual, `exit 1 NO MORDIO`, en su propia salida sellada. **No lo re corri
hasta que saliera verde y no lo arreglo**: esta vuelta es de bateria y su encargo
no lo incluye.

**LO QUE ESTO DEJA DICHO, SIN ADORNARLO:** la bateria **esta corrida** por la vara
de la 6.1, porque **los diez tramos tienen salida sellada no vacia y del mismo
calibre** y `--componer` lo coteja leyendo las salidas. **Y su contenido sale en
rojo**, por dos cuentas censales y un arnes que no muerde, **ninguno de los tres
arreglable dentro de este encargo**. Las dos cosas son ciertas a la vez y se
publican juntas: **una bateria corrida no es una bateria verde.**
