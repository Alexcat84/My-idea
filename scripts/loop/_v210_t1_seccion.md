### TAREA 1. LA BATERIA DE MUTACIONES, ENTERA, POR SUS ONCE TRAMOS

**CERRADA. LOS ONCE TRAMOS TIENEN SALIDA SELLADA DE ESTA VUELTA Y `--componer`
SALIO VERDE**, que es la condicion que `AUDITOR.md` 6.1 pone para declarar la
bateria corrida y no antes.

#### 1.a. EL REPARTO, RECOMPUTADO POR MI, Y LA DISCREPANCIA CON `AUDITOR.md` 6.1 DECLARADA

Salida: `docs/loop/SALIDA_V210_T1A_PLAN.txt`, de
`python scripts/loop/vuelta183_bateria_por_tramos.py --plan`.

- **CIFRA entradas de la nomina: 135**, leidas del modulo
  `verificar_mutaciones_viejas` y no tecleadas.
- **CIFRA tamano de tramo: 13.**
- **CIFRA tramos del reparto: 11.**
- **CIFRA suma de las entradas de todos los tramos: 135**, que calza con la
  nomina.
- **CIFRA literales de vuelta clavados en lineas que escriben: 0**, que
  es la guarda que el propio lanzador se corre encima antes de arrancar.

**MI CIFRA CALZA CON EL CONTRASTE DEL ENCARGO** (nomina 135, tramos
11): **cero discrepancias**.

**Y LA DISCREPANCIA CON `AUDITOR.md` 6.1 SE DECLARA EN VEZ DE RESOLVERSE
COPIANDO.** Ese fichero dice **NUEVE tramos**, con estas palabras: *"Su reparto,
computado y no tecleado, da NUEVE tramos sobre la nomina de hoy"*. **La glosa
lleva su corte dentro**, "sobre la nomina de hoy", y esa nomina era la del 5 sep
2026, cuando tenia 82 entradas. Hoy la nomina esta **congelada en 135** por
`AUDITOR.md` 6.3 y el mismo `TAMANO` de 13 reparte en 11. **La letra de 6.1
envejecio honestamente y no hay contradiccion que parar**: el propio 6.1 dice que
lo que manda es el reparto computado, no el numero.

#### 1.b. EL `--siguiente` SE USO PARA LEER EL REPARTO Y NUNCA PARA SABER QUE FALTABA

**La trampa, medida en las DOS puntas y no narrada.** El lanzador **computa su
vuelta de su propio nombre de fichero** y lo dice de si mismo en cada corrida
(`vuelta (computada del nombre, no tecleada): 183`), asi que **sus salidas se
llaman `SALIDA_V183_*` corra la vuelta que corra** y `--siguiente` cuenta ESOS
ficheros por su nombre.

| cuando | fichero de salida | tramos CON salida sellada no vacia | tramos que FALTAN |
|---|---|---|---|
| ANTES de correr nada | `SALIDA_V210_T1B_SIGUIENTE_ANTES.txt` | 11 | 0 |
| DESPUES de los once | `SALIDA_V210_T1B_SIGUIENTE_DESPUES.txt` | 11 | 0 |

**LAS DOS PUNTAS DAN LA MISMA CIFRA, Y ESA ES LA PRUEBA.** Antes de que esta
vuelta corriera un solo tramo, `--siguiente` ya publicaba `CIFRA tramos que
FALTAN: 0` y `LOS 11 TRAMOS TIENEN SALIDA SELLADA` **sobre las
salidas que dejo la VUELTA 200**. Si le hubiera hecho caso habria declarado
corrida una bateria que esta vuelta no habia corrido. **No se le hizo caso y no se
arreglo el lanzador**, que es moratoria.

**QUE SI PROBO LA APERTURA, ANTES DE LA PRIMERA OPERACION:**
`docs/loop/SALIDA_V210_APERTURA.txt` mide los **12 ficheros de la
bateria** (los once tramos mas la compuesta) tal como estaban al entrar y lee de
`git log` la vuelta que los sello: **200**, la misma para los doce.
`HEAD` de apertura `e3d33e42f41167b24e35eacbb68eea0e14d1c7b4`.

#### 1.c. LOS ONCE TRAMOS, COMMITEADOS UNO A UNO, Y LA VARA DE FRESCURA

Los once se corrieron **empezando por el 1** y **cada uno se committeo con su
salida sellada al terminar**, no todos al final, que es lo que permite que una
vuelta cortada retome en el tramo siguiente.

**LA TABLA DEL CALIBRE, PEGADA ENTERA DE `docs/loop/SALIDA_V210_T1E_TABLAS.txt`**
y no tecleada. La imprime `scripts/loop/_v210_tabla_tramos.py`, que **importa**
`medir`, `nombre_tramo`, `nombre_de_la_compuesta` y `entradas_de_la_salida` del
lanzador y `vuelta_que_sello` de `cerrar_reporte.py`, sin copiarles una linea.

| tramo | fichero sellado | bytes disco | bytes LF | lineas | sha256 LF | entradas | OK | CASO DECLARADO | NO MORDIO | ANCLA PERDIDA | NO REPRODUCIBLE | RUIDO | exitcode | minutos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `SALIDA_V183_BATERIA_TRAMO_1.txt` | 9544 | 9544 | 129 | `42aa5cfefc6430c9` | 13 | 11 | 2 | 0 | 0 | 0 | 0 | 1 | 0.9 |
| 2 | `SALIDA_V183_BATERIA_TRAMO_2.txt` | 7795 | 7795 | 123 | `81a3c7a531cf6a0e` | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 1 | 3.8 |
| 3 | `SALIDA_V183_BATERIA_TRAMO_3.txt` | 8050 | 8050 | 125 | `59a76bcd2a130c26` | 13 | 12 | 0 | 1 | 0 | 0 | 0 | 1 | 10.6 |
| 4 | `SALIDA_V183_BATERIA_TRAMO_4.txt` | 7862 | 7862 | 123 | `057302c48260d68e` | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 1 | 1.4 |
| 5 | `SALIDA_V183_BATERIA_TRAMO_5.txt` | 8274 | 8274 | 127 | `3af8acc15e739cce` | 13 | 10 | 0 | 3 | 0 | 0 | 0 | 1 | 0.7 |
| 6 | `SALIDA_V183_BATERIA_TRAMO_6.txt` | 8205 | 8205 | 126 | `59159791450eb06a` | 13 | 11 | 0 | 2 | 0 | 0 | 0 | 1 | 1.4 |
| 7 | `SALIDA_V183_BATERIA_TRAMO_7.txt` | 7893 | 7893 | 123 | `eb7f1f76a3ffb256` | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 1 | 0.7 |
| 8 | `SALIDA_V183_BATERIA_TRAMO_8.txt` | 7848 | 7848 | 123 | `f1f6f5e46d6b9ea5` | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 1 | 0.8 |
| 9 | `SALIDA_V183_BATERIA_TRAMO_9.txt` | 8525 | 8525 | 125 | `acec86b22c4647ce` | 13 | 12 | 0 | 1 | 0 | 0 | 0 | 1 | 0.8 |
| 10 | `SALIDA_V183_BATERIA_TRAMO_10.txt` | 8472 | 8472 | 123 | `f399ff43b678a39d` | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 1 | 2.0 |
| 11 | `SALIDA_V183_BATERIA_TRAMO_11.txt` | 6273 | 6273 | 94 | `e9ecd2bf6606e3be` | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0.3 |

- **CIFRA suma de entradas de los once tramos: 135**, que es la nomina
  entera.
- **CIFRA suma de OK: 126 | CASO DECLARADO: 2 | NO MORDIO: 7**, y
  **las tres clases suman 135**, o sea que ninguna entrada se quedo sin
  clasificar.
- **CIFRA suma de bytes en disco de los once: 88741 | CIFRA suma de minutos:
  23.4.**
- **CIFRA tramos con exitcode distinto de 1: 0** y **CIFRA tramos con RUIDO
  DE CONCURRENCIA distinto de cero: 0**.

**LA TABLA DE LA FRESCURA, PEGADA ENTERA DEL MISMO FICHERO.** Es la vara que el
nombre del fichero **no** da:

| tramo | commit que lo sello | vuelta que nombra su asunto |
|---|---|---|
| 1 | `ca702058` | 210 |
| 2 | `4895fb06` | 210 |
| 3 | `3fa5b035` | 210 |
| 4 | `a9a8fff9` | 210 |
| 5 | `274a0aed` | 210 |
| 6 | `fc68e550` | 210 |
| 7 | `3d79c288` | 210 |
| 8 | `97185bc4` | 210 |
| 9 | `ed74786d` | 210 |
| 10 | `08e9acdd` | 210 |
| 11 | `7dfbfdf7` | 210 |
| compuesta | `cb80b4e7` | 210 |

- **CIFRA tramos cuyo commit nombra la VUELTA 210: 11 de 11**, y
  **CIFRA tramos cuyo commit nombra OTRA vuelta: 0**.
- **No se renombro ni se copio ninguna salida a un nombre `V210`**: un fichero
  copiado no es un fichero corrido, y eso seria fabricar la prueba en vez de
  tenerla.

#### 1.d. LAS TRES GUARDAS DEL REGIMEN, LAS TRES SIN ABLANDAR

**LA DOBLE CORRIDA.** Cada entrada se corre **dos veces** por el cotejo de
reproducibilidad de la TAREA 2.f de la vuelta 141. La columna **NO REPRODUCIBLE
da 0 en los ONCE tramos**, o sea que **las dos corridas de las 135
entradas dieron lo mismo en las 135**. La cifra no se afirma de
memoria: esta en la tabla de arriba, columna por columna.

**CERO BYTES NO CUENTA COMO HECHO.** Ninguno de los once mide cero: el mas
pequeno es el tramo 11 con 6273 bytes y el mas grande el tramo 1 con 9544, los
dos en la tabla. `--componer` lo vuelve a comprobar por su cuenta y publica
**0 salidas de cero bytes**.

**DEL MISMO CALIBRE.** Los once traen **13 entradas cada uno salvo el 11, que
lleva las 5 de la cola** (135 menos diez por 13); los once salen con
**exitcode 1**; los once recomputan al cierre las mismas cifras de fallo; y
ninguno sale de otra hondura que los demas. La tabla entera esta arriba para que
se vea y no para que se crea.

#### 1.e. `--componer` Y LA SALIDA UNICA

Salida: `docs/loop/SALIDA_V210_T1D_COMPONER.txt`.

- **CIFRA entradas que los tramos dicen haber corrido: 135**, leidas de
  las salidas y **no recalculadas del reparto**, que es como el propio instrumento
  dice que hay que leerlas.
- **CIFRA entradas de la nomina que NINGUN tramo corrio: 0 | ajenas:
  0 | repetidas: 0.**
- **La salida unica: `docs/loop/SALIDA_V183_BATERIA.txt`, 93499 bytes en
  disco y 93499 normalizado a LF**, 1433 lineas, `sha256` LF
  `68e7505d560634c36af0e606cd35f51ad5564353286faf80972c5574ea8194ba`.

**VERDE:** los once tramos cubren la nomina entera, cada entrada **exactamente una
vez**, y la salida unica existe y no mide cero.

#### 1.f. EL ROJO DE LA BATERIA, Y LOS SIETE `NO MORDIO`

**LOS ONCE TRAMOS SALEN CON `exitcode 1` Y CLASE `ROJO POR FALLO`. Eso estaba
nombrado de antemano y no es una sorpresa**: el acta 205 ya lo dijo con estas
palabras, *"la bateria NO PUEDE SALIR VERDE mientras la moratoria viva, asi que
la 210 y la 215 saldran rojas igual"*. La causa estructural es la misma en los
once: **2 arneses que el censo VE, no anteriores a la vara 148, que se quedan
FUERA de la nomina** porque `AUDITOR.md` 6.3 la congela en 135. Son
`vuelta197_tarea2_mutacion_orden_del_turno.py` y
`vuelta199_tarea1_mutacion_guardas_revividas.py`.

**PERO HAY UN SEGUNDO ROJO Y NO ES ESTRUCTURAL: SIETE ENTRADAS DE LA NOMINA NO
MUERDEN.** Pegados enteros de `docs/loop/SALIDA_V210_T1E_TABLAS.txt`:

  LOS NO MORDIO, UNO A UNO, CON EL TRAMO QUE LOS CAZO:
      tramo 3   vuelta160_tarea6b_mutacion_puerta.py                 exit 1
      tramo 5   vuelta165_tarea6_mutacion_op_l_01.py                 exit 1
      tramo 5   vuelta166_tarea2_mutacion_correccion.py              exit 1
      tramo 5   vuelta168_tarea1_mutacion_nota.py                    exit 1
      tramo 6   vuelta168_tarea2_mutacion_reconstructor.py           exit 1
      tramo 6   vuelta171_mutacion_busqueda_acta.py                  exit 1
      tramo 9   vuelta185_tarea1c_mutacion_bateria_continuada.py     exit 1

- **CIFRA entradas NO MORDIO, contadas de las filas: 7**, y calza con
  la suma de la columna, que da **7**. **Las dos cuentas se hacen por
  caminos distintos a proposito.**
- **NO SE DIAGNOSTICAN Y NO SE ARREGLAN.** Diagnosticar por que una guarda dejo de
  morder pide abrir su sujeto y su arnes, y eso es fabricar: **la moratoria de
  `AUDITOR.md` 6.3 lo prohibe y esta vuelta no lo hace**. Se cuentan, se nombran
  con su tramo y suben marcados.
- **UNO DE LOS SIETE MERECE SU LINEA APARTE, Y LO DECLARO ANTES DE USARLO:**
  `vuelta185_tarea1c_mutacion_bateria_continuada.py` es el arnes que vigila el
  carril de **la bateria continuada** de `rama_de_la_seccion9()` en
  `scripts/loop/cerrar_reporte.py`, que es **exactamente el carril por el que va a
  pasar el cierre de esta misma vuelta**, porque mi salida compuesta se llama
  `SALIDA_V183_BATERIA.txt` y la vuelta que cierra es la 210. **Declararlo antes
  de pasar por el es la unica forma honesta de pasar por el.**

**CONTRASTE CON EL ACTA 205, DECLARADO Y NO RESUELTO COPIANDO.** Aquel acta
nombra **5** entradas que no mordieron; yo mido **7**. **Coinciden dos**
(`vuelta165_tarea6_mutacion_op_l_01.py` y
`vuelta185_tarea1c_mutacion_bateria_continuada.py`), **y una tercera coincide en
el nombre pero no en la cifra**: el acta le atribuye a
`vuelta160_tarea6b_mutacion_puerta.py` el exit `3221225794`, que es una caida del
proceso, y hoy sale con `exit 1`, que es otra cosa. **La diferencia queda escrita
y no la resuelvo copiando ninguna de las dos.**
