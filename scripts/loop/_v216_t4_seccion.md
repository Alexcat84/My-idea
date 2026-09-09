### TAREA 4. EL CIERRE INTEGRAL, MEDIDO DE SUS FICHEROS Y NO TECLEADO

**EL INSTRUMENTO ES `scripts/loop/_v216_t4_cierre.py` Y SU SALIDA SELLADA ES
`docs/loop/SALIDA_V216_T4_CIERRE.txt`.** Todas las tablas de abajo se cuentan de ese fichero.

#### 4.a.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, CON SU CONSOLA SELLADA DESDE DENTRO

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18.**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0 | CIFRA sin
exitcode dentro: 0 | CIFRA peor exitcode de las dieciocho:
0.**

**EL REMEDIO DE LA 215 SE MANTIENE Y NO SE AFLOJA, Y ADEMAS SE LE ANADE LA
PUERTA QUE LE FALTABA:** el ciclo sella su propia consola desde dentro, en el
nombre exacto que el compositor busca, y cae en rojo **por sus dos puertas**, la
del fichero **ausente** y la del fichero de **cero bytes**.

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T4_CIERRE.txt`: 2. FILAS QUE DEBERIA HABER: 2.**

| lado | fichero de la consola | bytes, por las dos convenciones | peor exitcode que declara |
|---|---|---|---:|
| **APERTURA** | `docs/loop/SALIDA_V216_CICLO_GATE0_APERTURA_CONSOLA.txt` | **965** bytes en disco y **965** bytes normalizado a LF | 0 |
| **CIERRE** | `docs/loop/SALIDA_V216_CICLO_GATE0_CIERRE_CONSOLA.txt` | **961** bytes en disco y **961** bytes normalizado a LF | 0 |

#### 4.a.2. LAS TRES SUITES SOLAS, CADA UNA CON SU EXITCODE Y SUS BYTES

**FILAS ARMADAS: 3. FILAS QUE DEBERIA HABER: 3.**

| suite | fichero | exitcode | bytes, por las dos convenciones |
|---|---|---:|---|
| **motor** | `docs/loop/SALIDA_V216_T4_SUITE_MOTOR.txt` | **0** | **1160** bytes en disco y **1131** bytes normalizado a LF |
| **tsc** | `docs/loop/SALIDA_V216_T4_SUITE_TSC.txt` | **0** | **11** bytes en disco y **11** bytes normalizado a LF |
| **web** | `docs/loop/SALIDA_V216_T4_SUITE_WEB.txt` | **0** | **334** bytes en disco y **334** bytes normalizado a LF |

#### 4.a.3. EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO, Y COTEJADOS SIN COPIAR

**LOS DOS COMANDOS, ESCRITOS ANTES DE SU RESULTADO:**
`python scripts/recomputar_marcador.py 3388` y
`python scripts/loop/vuelta83_conteo_aristas.py WORK`.

**FILAS ARMADAS: 16. FILAS QUE DEBERIA HABER: 16.** **LA COLUMNA DE
LA IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas
porque son de autores distintos.

| cifra | LA MIA, recomputada hoy | la del encargo, del auditor | calzan |
|---|---:|---:|---|
| marcador n | **3388** | 3388 | SI |
| marcador A | **550** | 550 | SI |
| marcador B | **72** | 72 | SI |
| marcador C | **5** | 5 | SI |
| marcador D | **2761** | 2761 | SI |
| marcador huecos | **0** | 0 | SI |
| censo nodos | **3853** | 3853 | SI |
| censo vivos | **3169** | 3169 | SI |
| censo deprecados | **684** | 684 | SI |
| aristas siguientes | **8780** | 8780 | SI |
| aristas previos | **8740** | 8740 | SI |
| aristas suma | **17520** | 17520 | SI |
| aristas union | **9914** | 9914 | SI |
| Gate 0 peor exitcode | **0** | 0 | SI |
| salidas selladas del ciclo | **18** | 18 | SI |
| salidas ausentes del ciclo | **0** | 0 | SI |

**CIFRA cifras cotejadas: 16 | CIFRA que NO calzan: 0.**

#### 4.a.4. LAS SEDES QUE LA VUELTA PUDO MOVER, Y LA PRUEBA MEDIDA DE QUE NO LAS MOVIO

**FILAS ARMADAS: 13. FILAS QUE DEBERIA HABER: 13.** **CIFRA sedes que
se movieron: 0.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes |
|---|---|---|---|---|
| `docs/plan/INVENTARIO.jsonl` | 43cea06634e6fc1a | 43cea06634e6fc1a | **QUIETA** | 629533 bytes en disco y 629533 bytes normalizado a LF |
| `docs/plan/OPERACIONES.jsonl` | 650578474361eb2b | 650578474361eb2b | **QUIETA** | 517181 bytes en disco y 517181 bytes normalizado a LF |
| `docs/plan/08_VERIFICACION.md` | 578eeefab6db2fd4 | 578eeefab6db2fd4 | **QUIETA** | 73652 bytes en disco y 73652 bytes normalizado a LF |
| `docs/plan/10_INVENTARIO.md` | 67f464d3d0b9e067 | 67f464d3d0b9e067 | **QUIETA** | 34258 bytes en disco y 33845 bytes normalizado a LF |
| `docs/plan/LECTURAS_DIRIGIDAS.md` | NO_MEDIDA_AL_ABRIR | a8ba1749b9a3fa13 | **QUIETA** | 219178 bytes en disco y 219178 bytes normalizado a LF |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 758edf1f5c313c18 | 758edf1f5c313c18 | **QUIETA** | 4057130 bytes en disco y 4057130 bytes normalizado a LF |
| `docs/INTRA_DOMINIO_INFORME.md` | c05b6bcd20188a9c | c05b6bcd20188a9c | **QUIETA** | 943970 bytes en disco y 943970 bytes normalizado a LF |
| `docs/plan/00_INDICE.md` | 2e71336cc2fdc387 | 2e71336cc2fdc387 | **QUIETA** | 45278 bytes en disco y 45278 bytes normalizado a LF |
| `docs/BANCO_DE_TEXTOS.md` | 8adbd60239509bb4 | 8adbd60239509bb4 | **QUIETA** | 186490 bytes en disco y 186490 bytes normalizado a LF |
| `docs/plan/BANCO_DEL_PLAN.md` | 7836c8976c585143 | 7836c8976c585143 | **QUIETA** | 61554 bytes en disco y 61554 bytes normalizado a LF |
| `dataset/metadata/master_graph.json` | 627cc662296f7f00 | 627cc662296f7f00 | **QUIETA** | 8375817 bytes en disco y 8375817 bytes normalizado a LF |
| `docs/loop/ACTA_AUDITOR.md` | c0e023c04c02d6b7 | c0e023c04c02d6b7 | **QUIETA** | 5067810 bytes en disco y 5067810 bytes normalizado a LF |
| `docs/loop/PROMPT_SIGUIENTE.md` | 1fff5c15dd6fc5e7 | 1fff5c15dd6fc5e7 | **QUIETA** | 9866 bytes en disco y 9866 bytes normalizado a LF |

**UNA DE LAS TRECE NO ESTABA EN LA LISTA DEL SELLO DE APERTURA Y LO DIGO EN VEZ
DE PUBLICAR UN FALSO ROJO:** `docs/plan/LECTURAS_DIRIGIDAS.md` es sede que esta
vuelta LEYO y su apertura no la nombraba, asi que **su quietud se mide con
`git diff --numstat`, que es una medicion y no una suposicion**. La primera
corrida de este instrumento la publicaba como SE MOVIO comparando un sha contra
una ausencia, **y eso era un falso rojo mio**: queda corregido y el texto viejo
sigue en el codigo.

#### 4.a.5. LA MORATORIA, MEDIDA Y NO PROMETIDA

**CIFRA ficheros del arbol de scripts que esta vuelta escribio: 16 |
CIFRA de esos con el prefijo `_v216_` que le toca: 16.** Ninguno
entra en el censo ni en la nomina, y **la nomina sigue CONGELADA EN 135**.

#### 4.a.6. EL VEREDICTO DE ESTA TAREA

**CIFRA comprobaciones que fallan en el cierre integral: 0.**
