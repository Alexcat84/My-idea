### TAREA 2. EL CIERRE INTEGRAL, MEDIDO DE SUS FICHEROS Y NO TECLEADO

**EL INSTRUMENTO ES `scripts/loop/_v217_t2_cierre.py` Y SU SALIDA SELLADA ES
`docs/loop/SALIDA_V217_T2_CIERRE.txt`, 10425 bytes en disco y 10425 normalizado a LF.** Todas las
tablas de abajo se cuentan de ese fichero.

#### 2.a.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, CON SU CONSOLA SELLADA DESDE DENTRO

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0**
**CIFRA salidas SIN exitcode dentro: 0**
**CIFRA peor exitcode de las dieciocho: 0**

**EL REMEDIO DE LA 215 SE MANTIENE Y NO SE AFLOJA:** el ciclo sella su propia
consola desde dentro, en el nombre exacto que el compositor busca, y cae en rojo
por sus dos puertas, la del fichero **ausente** y la del fichero de **cero
bytes**.

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V217_T2_CIERRE.txt`: 2. FILAS QUE DEBERIA HABER: 2.**

| lado | fichero de la consola | bytes, por las dos convenciones | peor exitcode que declara |
|---|---|---|---:|
| **APERTURA** | `docs/loop/SALIDA_V217_CICLO_GATE0_APERTURA_CONSOLA.txt` | **965** bytes en disco y **965** bytes normalizado a LF | 0 |
| **CIERRE** | `docs/loop/SALIDA_V217_CICLO_GATE0_CIERRE_CONSOLA.txt` | **961** bytes en disco y **961** bytes normalizado a LF | 0 |

#### 2.a.2. LAS TRES SUITES SOLAS, CADA UNA CON SU EXITCODE Y SUS BYTES

**FILAS ARMADAS: 3. FILAS QUE DEBERIA HABER: 3.**

| suite | fichero | exitcode | bytes, por las dos convenciones |
|---|---|---:|---|
| **motor** | `docs/loop/SALIDA_V217_T2_SUITE_MOTOR.txt` | **0** | **1160** bytes en disco y **1131** bytes normalizado a LF |
| **tsc** | `docs/loop/SALIDA_V217_T2_SUITE_TSC.txt` | **0** | **11** bytes en disco y **11** bytes normalizado a LF |
| **web** | `docs/loop/SALIDA_V217_T2_SUITE_WEB.txt` | **0** | **334** bytes en disco y **334** bytes normalizado a LF |

#### 2.a.3. EL MARCADOR Y EL CENSO, RECOMPUTADOS CON SU COMANDO Y COTEJADOS SIN COPIAR

**LOS DOS COMANDOS, ESCRITOS ANTES DE SU RESULTADO:**
`python scripts/recomputar_marcador.py 3388` y
`python scripts/loop/vuelta83_conteo_aristas.py WORK`.

**FILAS ARMADAS: 16. FILAS QUE DEBERIA HABER: 16. LA COLUMNA DE LA
IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas porque
son de autores distintos.

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

**CIFRA cifras cotejadas: 16 | CIFRA que NO calzan: 0**

#### 2.a.4. LAS SEDES, Y LA PRUEBA MEDIDA DE QUE ESTA VUELTA NO ESCRIBIO NI UNA FICHA

**CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 0**
**CIFRA sedes cuya quietud se midio por sha256 de apertura: 9 | por git diff, porque la apertura no las nombraba: 4**

```
SEDE docs/plan/INVENTARIO.jsonl                 | al abrir 43cea06634e6fc1a | al cerrar 43cea06634e6fc1a | QUIETA | 629533 / 629533 bytes | cotejo de los dos sha256
SEDE docs/plan/OPERACIONES.jsonl                | al abrir 650578474361eb2b | al cerrar 650578474361eb2b | QUIETA | 517181 / 517181 bytes | cotejo de los dos sha256
SEDE docs/plan/08_VERIFICACION.md               | al abrir 578eeefab6db2fd4 | al cerrar 578eeefab6db2fd4 | QUIETA | 73652 / 73652 bytes | cotejo de los dos sha256
SEDE docs/plan/10_INVENTARIO.md                 | al abrir NO_MEDIDA_AL_ABRIR | al cerrar 67f464d3d0b9e067 | QUIETA | 34258 / 33845 bytes | NO MEDIDA AL ABRIR (no estaba en la lista del sello de apertura): su quietud se mide con git diff --numstat HEAD, 0 filas
SEDE docs/plan/LECTURAS_DIRIGIDAS.md            | al abrir NO_MEDIDA_AL_ABRIR | al cerrar a8ba1749b9a3fa13 | QUIETA | 219178 / 219178 bytes | NO MEDIDA AL ABRIR (no estaba en la lista del sello de apertura): su quietud se mide con git diff --numstat HEAD, 0 filas
SEDE docs/INTRA_DOMINIO_VEREDICTOS.jsonl        | al abrir 758edf1f5c313c18 | al cerrar 758edf1f5c313c18 | QUIETA | 4057130 / 4057130 bytes | cotejo de los dos sha256
SEDE docs/INTRA_DOMINIO_INFORME.md              | al abrir NO_MEDIDA_AL_ABRIR | al cerrar c05b6bcd20188a9c | QUIETA | 943970 / 943970 bytes | NO MEDIDA AL ABRIR (no estaba en la lista del sello de apertura): su quietud se mide con git diff --numstat HEAD, 0 filas
SEDE docs/plan/00_INDICE.md                     | al abrir NO_MEDIDA_AL_ABRIR | al cerrar 2e71336cc2fdc387 | QUIETA | 45278 / 45278 bytes | NO MEDIDA AL ABRIR (no estaba en la lista del sello de apertura): su quietud se mide con git diff --numstat HEAD, 0 filas
SEDE docs/BANCO_DE_TEXTOS.md                    | al abrir 8adbd60239509bb4 | al cerrar 8adbd60239509bb4 | QUIETA | 186490 / 186490 bytes | cotejo de los dos sha256
SEDE docs/plan/BANCO_DEL_PLAN.md                | al abrir 7836c8976c585143 | al cerrar 7836c8976c585143 | QUIETA | 61554 / 61554 bytes | cotejo de los dos sha256
SEDE dataset/metadata/master_graph.json         | al abrir 627cc662296f7f00 | al cerrar 627cc662296f7f00 | QUIETA | 8375817 / 8375817 bytes | cotejo de los dos sha256
SEDE docs/loop/ACTA_AUDITOR.md                  | al abrir d1e494504a480ac5 | al cerrar d1e494504a480ac5 | QUIETA | 5092743 / 5092743 bytes | cotejo de los dos sha256
SEDE docs/loop/PROMPT_SIGUIENTE.md              | al abrir 88e737f47a3be5b9 | al cerrar 88e737f47a3be5b9 | QUIETA | 9216 / 9216 bytes | cotejo de los dos sha256
```

#### 2.a.5. LA MORATORIA, Y LA CIFRA CON SU HUECO AL LADO

**LA OBLIGACION DE DICTADO NUEVA DEL ENCARGO DE LA 217 SE CUMPLE AQUI, Y NACE DE
MI CAIDA DE LA 216:** aquella publico **16** ficheros escritos donde el auditor
conto **18**, porque el instrumento corre **antes** de que el cierre escriba los
suyos. La regla que el encargo fija es publicar **las dos cifras juntas**, la
medida y la que el propio cierre anade, y el hueco no se estima: **se nombra
fichero a fichero**.

**CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 7 | CIFRA de esos con el prefijo que le toca: 7**

**CIFRA MEDIDA AHORA: 7 | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: 4 | CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: 11**
**Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL: 4 de 4, contado de sus propios nombres.**

```
TOCADO scripts/loop/_v217_apertura.py                       | prefijo _v217_: SI
TOCADO scripts/loop/_v217_ciclo_gate0.py                    | prefijo _v217_: SI
TOCADO scripts/loop/_v217_esqueleto.py                      | prefijo _v217_: SI
TOCADO scripts/loop/_v217_t1_diecisiete.py                  | prefijo _v217_: SI
TOCADO scripts/loop/_v217_t1_seccion.md                     | prefijo _v217_: SI
TOCADO scripts/loop/_v217_t1_seccion.py                     | prefijo _v217_: SI
TOCADO scripts/loop/_v217_t2_cierre.py                      | prefijo _v217_: SI
DEL HUECO scripts/loop/_v217_t2_seccion.py                 | ya contado arriba: NO
DEL HUECO scripts/loop/_v217_t2_seccion.md                 | ya contado arriba: NO
DEL HUECO scripts/loop/_v217_cierre_texto.py               | ya contado arriba: NO
DEL HUECO scripts/loop/_v217_cierre_texto.md               | ya contado arriba: NO
```

#### 2.a.6. LA FECHA, MEDIDA Y NO SUPUESTA

**fecha del commit de apertura, leida de git log: 2026-09-09**
**fecha del commit de ahora mismo, leida de git log: 2026-09-09**

**CIFRA comprobaciones que fallan: 0**
