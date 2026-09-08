# REPORTE DE LA VUELTA 210 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v210_esqueleto.py` **antes de la primera tarea**; la tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO EN LA 208 Y EN LA
> 209.** No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **UNA SOLA TAREA, Y ESO NO ES UN RECORTE SINO LA LETRA.** `AUDITOR.md` 6.1 dice
> que la bateria corre **en una VUELTA DE BATERIA propia que NO LLEVA NADA MAS**,
> y la cadencia de cinco pone la 210 detras de la 205. El trabajo de plan que el
> acta 209 deja adjudicado (los dos campos `estado` de `OP-L-02` y `OP-L-03`, y la
> ficha `OP-I-01`) **espera a la 211** y no se toca aqui.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo. Todo lo que esta vuelta escribe son ficheros `_v210_*` **con
> prefijo de guion bajo, fuera del censo y fuera de la nomina**. La nomina sigue
> **CONGELADA EN 135** y no se poda. **El lanzador de la bateria NO SE CLONA NI SE
> TOCA.**
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR, Y ESO ES LA `C.5` DE LA 209
> REMEDIADA.** `docs/loop/SALIDA_V210_APERTURA.txt`,
> `docs/loop/SALIDA_V210_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes del primer tramo**, no al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 210`, y su salida
cruda vive en `docs/loop/SALIDA_V210_TALLADOR_CABECERA.txt` (2476 bytes en disco y 2456 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `e3d33e42` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 209: LA VUELTA ENTREGO SUS TRES TAREAS Y TODA CIFRA REPRODUCE AL DIGITO SALVO UN CORTE MAL NOMBRADO. CIERRO OP-L-02 CON SUS DOS A MEDIAS SUBIDOS A CUBRE. MI CIEGA SALIO 31 DE 40 Y LA DEUDA ES MIA.'), HEAD real de apertura `e3d33e42` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `36997247` (leido de `SALIDA_V210_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LA TAREA DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LA BATERIA DE MUTACIONES, ENTERA, POR SUS ONCE TRAMOS, con el lanzador `scripts/loop/vuelta183_bateria_por_tramos.py` corrido SIN CLONARLO Y SIN TOCARLO (moratoria). El reparto recomputado de la nomina; los once tramos corridos empezando por el 1, cada uno committeado con su salida sellada al terminar y esa lista de commits publicada como VARA DE FRESCURA; las tres guardas del regimen sin ablandar (doble corrida, cero bytes no cuenta, mismo calibre); y `--componer` al final. **El `--siguiente` se usa SOLO para leer el reparto y NUNCA para saber que falta** | **CERRADA. LOS ONCE TRAMOS SELLADOS Y COMMITEADOS EN ESTA VUELTA, Y `--componer` VERDE** | `SALIDA_V210_T1A_PLAN.txt`, `SALIDA_V210_T1B_SIGUIENTE_ANTES.txt`, `SALIDA_V210_T1B_SIGUIENTE_DESPUES.txt`, los once ficheros de tramo desde `SALIDA_V183_BATERIA_TRAMO_1.txt` hasta `SALIDA_V183_BATERIA_TRAMO_11.txt`, `SALIDA_V183_BATERIA.txt`, `SALIDA_V210_T1D_COMPONER.txt`, `SALIDA_V210_T1E_TABLAS.txt`, `SALIDA_V210_T1F_SECCION.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LA TAREA, AL DETALLE (la seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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

**CERO BYTES NO CUENTA COMO HECHO.** Ninguno de los once mide cero, y la cifra
de cada uno esta en la columna `bytes disco` de la tabla de arriba, que sale de
su propio fichero. `--componer` lo vuelve a comprobar por su cuenta y publica
**0 salidas de cero bytes**. Aqui no se repite ninguna de esas cifras en prosa
a proposito: repetirla seria teclearla dos veces y una de las dos acabaria
envejeciendo sola.

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
- La salida unica, **con sus dos convenciones EN LA MISMA LINEA**, que es como
  esta casa publica una pareja y como la guarda de `cerrar_reporte.py` sabe
  leerla:
- `docs/loop/SALIDA_V183_BATERIA.txt`: **93499 bytes en disco y 93499 bytes normalizado a LF**, **1433 lineas**, `sha256` LF `68e7505d560634c36af0e606cd35f51ad5564353286faf80972c5574ea8194ba`.

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

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: LA UNICA TAREA DE LA VUELTA DE BATERIA QUEDA ENTREGADA: LOS ONCE TRAMOS CORRIDOS, SELLADOS Y COMMITEADOS EN ESTA VUELTA, 11 DE 11 CON COMMIT QUE NOMBRA LA 210 Y 0 QUE NOMBRE OTRA, LAS 135 ENTRADAS DE LA NOMINA CORRIDAS EXACTAMENTE UNA VEZ Y DOS VECES CADA UNA CON NO REPRODUCIBLE EN CERO, --componer VERDE, Y DOS ROJOS DICHOS: EL ESTRUCTURAL DE LA MORATORIA Y 7 GUARDAS QUE NO MUERDEN. 3 DISCUTIBLES MARCADOS, 2 PREGUNTAS, 1 PENDIENTE DE DOCTRINA Y 3 CAIDAS PROPIAS.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Las compone
`scripts/loop/_v210_cierre.py` leyendolas de los ficheros de salida de la
vuelta, y **cae en rojo si no puede leer una** o si encuentra mas de una
coincidencia. Es la letra de `EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO.

### 3.1. LA UNICA TAREA, CADA CIFRA CON EL FICHERO DEL QUE SALE

| que se midio | cifra | fichero de salida |
|---|---:|---|
| entradas de la nomina, congelada por `AUDITOR.md` 6.3 | **135** | `SALIDA_V210_T1A_PLAN.txt` |
| tamano de tramo, y tramos del reparto | **13** y **11** | `SALIDA_V210_T1A_PLAN.txt` |
| tramos que `--siguiente` decia que FALTABAN antes de correr nada | **0** | `SALIDA_V210_T1B_SIGUIENTE_ANTES.txt` |
| entradas corridas sumadas de los once tramos | **135** | `SALIDA_V210_T1E_TABLAS.txt` |
| reparto de veredictos: OK, CASO DECLARADO y NO MORDIO | **126**, **2** y **7** | `SALIDA_V210_T1E_TABLAS.txt` |
| suma de las tres clases | **135** | `SALIDA_V210_T1E_TABLAS.txt` |
| tramos con exitcode distinto de 1 | **0** | `SALIDA_V210_T1E_TABLAS.txt` |
| tramos con RUIDO DE CONCURRENCIA distinto de cero | **0** | `SALIDA_V210_T1E_TABLAS.txt` |
| tramos cuyo commit nombra la VUELTA 210, y los que nombran otra | **11 de 11** y **0** | `SALIDA_V210_T1E_TABLAS.txt` |
| minutos sumados de los once tramos | **23.4** | `SALIDA_V210_T1E_TABLAS.txt` |
| entradas sin correr, ajenas y repetidas segun `--componer` | **0**, **0** y **0** | `SALIDA_V210_T1D_COMPONER.txt` |

**LA SALIDA UNICA DE LA BATERIA**, remedida al cierre por
`scripts/loop/_v210_tabla_tramos.py` y no copiada de `--componer`. **Las dos
convenciones van en la misma linea, y los dos `sha256` tambien**, que es como
esta casa publica una pareja:

- `docs/loop/SALIDA_V183_BATERIA.txt`: **93499 bytes en disco y 93499 bytes normalizado a LF**, **1433 lineas**.
- `docs/loop/SALIDA_V183_BATERIA.txt`: **sha256 disco `68e7505d560634c3` y sha256 LF `68e7505d560634c3`**.

**EL MARCADOR DEL CRIBADO NO SE MOVIO Y ESA GLOSA LLEVA SU CORTE:** esta vuelta
**no adjudica ninguna clase** y **no toca `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**,
medido con `git diff --numstat` al cierre en la tabla de la seccion 4. La vuelta
de bateria no lleva trabajo de plan al lado, que es la letra de `AUDITOR.md` 6.1.

### 3.2. EL CICLO ENTERO DE GATE 0, CORRIDO POR MI Y NUNCA `run_phase1.py` A SECAS

Los ocho comandos en su orden, con `scripts/loop/_v210_ciclo_gate0.py`, que
**IMPORTA** `_v205_ciclo_gate0.py` y solo le cambia el numero de vuelta, que
computa de su propio nombre. **IMPORTAR NO ES CLONAR** (acta 206 `6.5`).
**El lado APERTURA se corrio ANTES del primer tramo y el lado CIERRE despues del
ultimo**, que es la `C.5` de la 209 remediada.

| que | cifra | fichero de salida |
|---|---:|---|
| peor `EXITCODE` de los ocho, en los dos lados | **0** | las ocho salidas `SALIDA_V210_*_CIERRE.txt` |
| censo del grafo: nodos, activos y deprecados | **3853**, **3169** y **684** | `SALIDA_V210_GATE0_CMD1_CIERRE.txt` |
| Gate 0: auto-aristas, duplicadas de titulo y divergentes | **0**, **0** y **0** | `SALIDA_V210_GATE0_CMD1_CIERRE.txt` |
| aristas: siguientes, previas, suma y union | **8780**, **8740**, **17520** y **9914** | `SALIDA_V210_CONTEO_CIERRE.txt` |
| desfase del calibrado | **4** filas | `SALIDA_V210_DESFASE_CALIBRADO_CIERRE.txt` |
| tests del motor | **25** de **25** | `SALIDA_V210_MOTOR_CIERRE.txt` |
| web: ficheros de test y tests | **82 (82)** y **1040 (1040)** | `SALIDA_V210_WEB_CIERRE.txt` |
| `npx tsc --noEmit` | **EXIT 0** | `SALIDA_V210_TSC_CIERRE.txt` |
| filas de `git diff HEAD --numstat` tras correr el ciclo | **0** | `SALIDA_V210_CICLO_NUMSTAT_CIERRE.txt` |

**LAS 4 FILAS DEL DESFASE SON LAS MISMAS DE SIEMPRE**, y esa glosa
lleva su corte: son las cuatro que el ciclo de la vuelta 209 ya listaba en su
propia salida, **remedidas hoy en el lado CIERRE de esta vuelta** y no heredadas.

## 4. LO QUE SE TOCO, Y LO QUE NO

**ESTA TABLA SE RECOMPUTA AL CIERRE Y NO SE HEREDA DE LA APERTURA**
(`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE).

**Mi apertura sellada, `docs/loop/SALIDA_V210_APERTURA.txt`, publica con
`git status --porcelain` 1 lineas al entrar, y con
`git diff --numstat -- dataset/` AL ENTRAR: 0 filas.** Las dos se
LEEN de la apertura sellada y no se teclean.

**Y RECOMPUTADAS AL CIERRE POR MI, CON LOS MISMOS DOS COMANDOS: 3
y 0.**

| sede | filas de `numstat` al cierre | por que |
|---|---:|---|
| `dataset/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `web/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `engine/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `docs/plan/` | **0** | la vuelta de bateria no lleva trabajo de plan al lado |

**LO QUE SI SE MOVIO SON LAS SALIDAS DE LA BATERIA Y LOS FICHEROS DE COMPUTO DE
LA VUELTA**, y todo va committeado tramo a tramo. **`docs/plan/` no se toca en
ninguna de sus filas**, que es lo que `AUDITOR.md` 6.1 pide de una vuelta de
bateria: los dos campos `estado` de `OP-L-02` y `OP-L-03` y la ficha `OP-I-01`
que el acta 209 adjudica **esperan a la 211**.

### 4.1. LA MORATORIA, MEDIDA CON SU CORTE LEIDO Y NO TECLEADO

**AQUI VA APLICADA LA UNICA CAIDA QUE EL ACTA 209 ME CUENTA, Y NO SOLO CITADA.**
Su `4.1` midio que mi glosa nombraba *el commit de la TAREA 3* mientras la cifra
salia de un commit de cierre. **La causa estaba en el codigo**: el computo iba
contra el `HEAD` vivo y la frase que lo nombraba estaba TECLEADA. En
`scripts/loop/_v210_cierre.py` la funcion `moratoria()` devuelve **la cifra y
el `HEAD` contra el que la midio en la misma tupla**, y la frase de abajo se
compone con ese `HEAD`: **no hay forma de nombrar un corte distinto del medido.**

**CIFRA ficheros anadidos a `scripts/loop/` entre `e3d33e42` y `cb5a201a`,
que es el `HEAD` que este mismo computo leyo y no uno tecleado: 10, de
los que 10 llevan el prefijo `_v210_` y 0 no lo llevan.**

**ESTA CIFRA NACE CORTA POR CONSTRUCCION Y LO DIGO DENTRO DE LA MISMA FRASE:**
`scripts/loop/_v210_cierre.py` es el fichero que cuenta, va en el commit del
cierre, y **ese commit todavia no existe cuando el conteo corre**. Falta por
tanto **este mismo fichero** y cualquiera que nazca despues de `cb5a201a`.
**No se arregla el instrumento, que es moratoria**: se escribe la glosa con su
corte, y el corte es el que la frase nombra.

**LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135**, recomputada
importando su fuente y no tecleada, y **el lanzador
`scripts/loop/vuelta183_bateria_por_tramos.py` no se clono ni se toco**: su
`sha256` de disco y de LF al entrar estan en mi apertura sellada.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. RE CORRI EL TRAMO 4 EN VEZ DE PUBLICARLO CON SU `RUIDO DE
CONCURRENCIA` EN 2 Y DEJARLO.** El propio instrumento dice de esa cifra que
*"NO son de nadie y NO son rojo de nadie"*, o sea que la letra escrita **no me
obligaba a re correr**: podia haber publicado el tramo 4 tal cual, con su ruido
declarado, y seguir. Elegi re correrlo solo, y su ruido bajo de 2 a
**0** en los once.
**Por donde me puedo estar equivocando:** re correr un tramo que la letra admite
es gastar reloj y, peor, **es una decision mia que ninguna regla me manda**, y
esta casa castiga al que se inventa severidad tanto como al que afloja. La
objecion contraria es que el ruido de ese tramo no venia de un fichero cualquiera
sino de **otra corrida de la misma bateria cerrandose encima**, que es la cosa
exacta que `AUDITOR.md` 6.1 quiere evitar cuando dice que la bateria **se corre
sola**. **Si el auditor lee que bastaba con declararlo, el tramo 4 viejo esta
entero en el commit `3fa5b035` y su cifra sigue siendo leible.**

**`D.2`. PUBLICO LOS SIETE `NO MORDIO` SIN DIAGNOSTICAR NINGUNO.** Son siete
guardas de la nomina que ya no tumban lo que decian tumbar, y las dejo nombradas
con su tramo y nada mas.
**Por donde me puedo estar equivocando:** puede que **una guarda que no muerde
sea una CAIDA DE DATO** y que la moratoria, que exceptua justamente *"lo que una
CAIDA DE DATO exija, con su cita"*, me estuviera pidiendo abrir al menos una y
medir por que. Lo que me sostiene es que el acta 205 ya nombro cinco de estas
mismas y **no las adjudico como caida de dato sino como hallazgo que sube**, y
que abrir siete arneses y sus siete sujetos es maquinaria de la que la moratoria
me saca. **Marco el punto y no lo defiendo mas.**

**`D.3`. USO EL CARRIL DE LA BATERIA CONTINUADA DE `cerrar_reporte.py` SABIENDO
QUE SU ARNES NO MUERDE.** Mi salida compuesta se llama `SALIDA_V183_BATERIA.txt`
porque el lanzador computa su vuelta de su propio nombre, asi que
`rama_de_la_seccion9()` la juzga por el carril de la **bateria continuada**, y
`vuelta185_tarea1c_mutacion_bateria_continuada.py`, que es el arnes de ese
carril, sale **NO MORDIO** en el tramo 9 de esta misma corrida.
**Por donde me puedo estar equivocando:** cerrar por un carril cuya guarda esta
apagada es cerrar sin red, y se podria defender que hay que parar hasta que esa
guarda vuelva a morder. Lo que me sostiene es que **el carril lo abre la
evidencia de `git log`, no el arnes**: `tramos_por_vuelta()` lee de los commits
que los once tramos los sello la VUELTA 210, y esa evidencia **no se puede
teclear**. Aun asi **lo declaro antes de pasar por el**, que es lo unico que
puedo hacer sin tocar maquinaria.

## 6. LAS PREGUNTAS

**`P.1`. SIETE GUARDAS QUE NO MUERDEN, SON UNA CAIDA DE DATO O NO?** Es el `D.2`
puesto como pregunta general y va a volver a pasar cada cinco vueltas. La
moratoria de `AUDITOR.md` 6.3 exceptua *"lo que una CAIDA DE DATO exija, con su
cita"*. **Una entrada de la nomina que sale `NO MORDIO` entra en esa excepcion, o
se acumula hasta la auditoria integral?** Yo no lo decido.

**`P.2`. UN TRAMO CON `RUIDO DE CONCURRENCIA` DISTINTO DE CERO, SE RE CORRE O SE
DECLARA?** Es el `D.1` puesto como pregunta general. El instrumento dice que el
ruido **no es rojo de nadie**, pero no dice que hacer cuando el ruido lo produce
**otra corrida de la misma bateria**. Una letra general me ahorra decidirlo cada
cinco vueltas.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`. UN PROCESO LANZADO EN SEGUNDO PLANO CUYO LOG QUEDA EN CERO BYTES NO
ESTA MUERTO, Y ESTA CASA NO TIENE ESCRITO COMO COMPROBARLO.** Me paso en esta
misma vuelta y es mi `C.1`: di por muerto un tramo porque su log medía cero
bytes, lo relance, y los dos corrieron a la vez. **La letra vigente dice que una
SALIDA SELLADA de cero bytes no cuenta como hecha, y esa letra es buena; lo que
no existe es la hermana: un LOG de cero bytes NO prueba que el proceso murio.**
El remedio que use no cuesta codigo nuevo: **preguntar por el proceso, no por su
log**, antes de relanzar nada. Lo dejo como PENDIENTE DE DOCTRINA y **no lo
convierto en regla yo**.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. DI POR MUERTO UN TRAMO VIVO Y CORRI DOS BATERIAS A LA VEZ.** Lance el
tramo 3 con un `nohup ... &` dentro de un shell que se cierra al devolver, vi su
log en cero bytes y lo di por muerto. **No lo estaba.** Relance, y hubo dos
corridas del tramo 3 solapadas: la primera de `04:10:51Z` a `04:21:39Z` y la
segunda empezada a `04:20:42Z`, **cincuenta y siete segundos antes de que la
primera terminara**. Committee la primera, y la segunda me la piso despues.
**Quien me cazo fue la guarda de concurrencia del propio instrumento**, que
publico `RUIDO DE CONCURRENCIA: 2 fichero(s)` en la salida del tramo 4. **El
remedio fue correr, no narrar:** comprobe con `ps` que no quedaba proceso vivo y
re corri los tramos 3 y 4 solos, los dos con ruido en cero. **El commit
`e72a22b9` y el `3fa5b035` quedan enteros en la historia y no se reescriben:
decian la verdad de lo que habian medido.** Cuenta como UNA caida, no como tres.

**`C.2`. EL PRIMER INTENTO DE ESCRIBIR EL ESQUELETO MURIO EN EL SHELL Y NO EN EL
JUICIO.** El fichero `_v210_esqueleto.py` se escribio a la segunda porque el
primer intento se fue por una comilla del propio `heredoc`, no por nada del
esqueleto. **No toco ninguna cifra ni ningun fichero del repo** y lo digo porque
la casa cuenta las caidas, no solo las que dejan rastro.

**`C.3`. RE CORRI EL ESQUELETO SOBRE MI PROPIO REPORTE YA ANEXADO, Y SU PASO 0
ARCHIVO MI PARCIAL COMO SI FUERA EL DE UNA VUELTA CERRADA.** Al remediar el rojo
de las cifras sin pareja re corri la cadena entera, y `_v210_esqueleto.py`
empieza por archivar *el reporte que va a pisar*: como el del arbol ya era el de
la 210 anexado, escribio `docs/loop/reportes/REPORTE_V210.md`. **El archivo de
una vuelta lo escribe la vuelta SIGUIENTE, nunca ella misma**, asi que ese
fichero se retiro con `git rm` y queda declarado en el commit que lo retira.
**Y el esqueleto me cazo:** cayo en ROJO con dos motivos y **no escribio nada**,
diciendo con sus palabras *"EL TEXTO QUE SE VA A PISAR NO ESTA GUARDADO"* y
nombrando los dos `sha256`. Su salida esta entera en
`docs/loop/SALIDA_V210_ESQUELETO.txt`. **La consecuencia si la cause yo:** como
el esqueleto no escribio, el anexado siguiente metio un SEGUNDO cuerpo de la
TAREA 1 en el mismo reporte. **El remedio no fue re correr el esqueleto sino
recuperar el original** del commit `e411137f`, que es el que se tallo antes de la
primera tarea, y anexar UNA sola vez encima, contando con `grep` que la cabecera
de la TAREA 1 aparece exactamente una vez. Cuenta como UNA caida.

**Y LAS TRES SE PARECEN, QUE ES LO QUE ME LLEVO DE LA VUELTA:** en la `C.1` di
por muerto un proceso vivo y en la `C.3` di por fresco un arbol que ya estaba
escrito. **Las dos veces supuse el estado en vez de mirarlo, y las dos veces me
cazo una guarda de la casa y no yo.**

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**La 211 no es de bateria** (la cadencia de cinco pone la siguiente en la 215) y
el trabajo de plan que el acta 209 deja adjudicado esta esperando: el campo
`estado` de **`OP-L-02`** a `HECHA` con las tres guardas del `2.c` de la 209, el
de **`OP-L-03`** puesto al dia por el mismo carril y en el mismo computo, y
**`OP-I-01`**, que es la ultima de las cuatro fichas reales de la moratoria y no
se ha empezado. **Y los siete `NO MORDIO` de esta bateria necesitan una
adjudicacion**, que es mi `P.1`.

## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE

**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**
Fichero: `docs/loop/SALIDA_V183_BATERIA.txt` (**93499 bytes en disco y 93499 normalizado a LF**, **1321 lineas
no vacias**, contadas
por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta
seccion se queda sin ella**, que es la cuarta de sus cuatro piezas.

```
LA BATERIA DE MUTACIONES DE LA VUELTA 183, CORRIDA ENTERA Y EN TRAMOS
compuesta por scripts/loop/vuelta183_bateria_por_tramos.py --componer

LO QUE SE PARTIO ES EL BOCADO, NO LA BATERIA. Las cuatro cosas que la
letra del fundador del 5 sep 2026 fija siguen enteras: la cadencia (cada
cinco vueltas), la soledad (vuelta propia sin nada al lado), la
integridad (cada entrada corrida, y corrida DOS VECES) y la prohibicion
de podar la nomina.

CIFRA entradas de la nomina: 135
CIFRA tramos: 11
CIFRA entradas que los tramos dicen haber corrido: 135
CIFRA entradas sin correr: 0 | repetidas: 0 | ajenas: 0
LA COBERTURA SE LEYO DE LAS SALIDAS, no se recalculo del reparto.

  tramo 1 -> SALIDA_V183_BATERIA_TRAMO_1.txt: 9544 bytes disco, 9544 bytes LF, 129 lineas, sha256 42aa5cfefc6430c9
  tramo 2 -> SALIDA_V183_BATERIA_TRAMO_2.txt: 7795 bytes disco, 7795 bytes LF, 123 lineas, sha256 81a3c7a531cf6a0e
  tramo 3 -> SALIDA_V183_BATERIA_TRAMO_3.txt: 8050 bytes disco, 8050 bytes LF, 125 lineas, sha256 59a76bcd2a130c26
  tramo 4 -> SALIDA_V183_BATERIA_TRAMO_4.txt: 7862 bytes disco, 7862 bytes LF, 123 lineas, sha256 057302c48260d68e
  tramo 5 -> SALIDA_V183_BATERIA_TRAMO_5.txt: 8274 bytes disco, 8274 bytes LF, 127 lineas, sha256 3af8acc15e739cce
  tramo 6 -> SALIDA_V183_BATERIA_TRAMO_6.txt: 8205 bytes disco, 8205 bytes LF, 126 lineas, sha256 59159791450eb06a
  tramo 7 -> SALIDA_V183_BATERIA_TRAMO_7.txt: 7893 bytes disco, 7893 bytes LF, 123 lineas, sha256 eb7f1f76a3ffb256
  tramo 8 -> SALIDA_V183_BATERIA_TRAMO_8.txt: 7848 bytes disco, 7848 bytes LF, 123 lineas, sha256 f1f6f5e46d6b9ea5
  tramo 9 -> SALIDA_V183_BATERIA_TRAMO_9.txt: 8525 bytes disco, 8525 bytes LF, 125 lineas, sha256 acec86b22c4647ce
  tramo 10 -> SALIDA_V183_BATERIA_TRAMO_10.txt: 8472 bytes disco, 8472 bytes LF, 123 lineas, sha256 f399ff43b678a39d
  tramo 11 -> SALIDA_V183_BATERIA_TRAMO_11.txt: 6273 bytes disco, 6273 bytes LF, 94 lineas, sha256 e9ecd2bf6606e3be
==============================================================================

==============================================================================
TRAMO 1 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_1.txt
==============================================================================

CORRIDA DEL TRAMO 1 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:03:42Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD e411137f9d81, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD e411137f9d81, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD e411137f9d81, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 1 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta133_tarea2e_mutacion_cifras.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_1.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_2.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_3.py
      ENTRADA DEL TRAMO: vuelta139_2b_mutaciones.py
      ENTRADA DEL TRAMO: vuelta140_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta141_2_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2b_mutacion_bateria.py
      ENTRADA DEL TRAMO: vuelta143_2c_mutacion_positivo.py
      ENTRADA DEL TRAMO: vuelta144_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_2b_mutacion_giro.py
      ENTRADA DEL TRAMO: vuelta144_2d_mutacion_cobertura.py


  vuelta133_tarea2e_mutacion_cifras.py   exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta135_2e_mutacion_1.py             exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_1.txt
  vuelta135_2e_mutacion_2.py             exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_2.txt
  vuelta135_2e_mutacion_3.py             exit 1  CASO DECLARADO       3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_3.txt
      SUJETO FIJO VERIFICADO: SUJETO_FIJO_V135_2E_REPORTE_134.md calza con el blob e12e4c36 (sha256 d1f97a510f17e35046eeec4975e1e0a1adabcfdda5a4646a250aa6db
  vuelta139_2b_mutaciones.py             exit 0  OK                   4.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta140_2a_mutaciones.py             exit 2  CASO DECLARADO       3.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta141_2_mutaciones.py              exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2a_mutaciones.py             exit 0  OK                   5.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2b_mutacion_bateria.py       exit 0  OK                   4.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2c_mutacion_positivo.py      exit 0  OK                   4.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2a_mutaciones.py             exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2b_mutacion_giro.py          exit 0  OK                   7.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2d_mutacion_cobertura.py     exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 50.2
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.8
  CIFRA arnes MAS LENTO: vuelta144_2b_mutacion_giro.py con 7.1s
  CIFRA arnes MAS RAPIDO: vuelta144_2a_mutaciones.py con 2.7s
  CIFRA mediana por arnes, en segundos: 3.3
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta144_2b_mutacion_giro.py                  7.1s
      vuelta143_2a_mutaciones.py                     5.1s
      vuelta143_2c_mutacion_positivo.py              4.7s
      vuelta143_2b_mutacion_bateria.py               4.1s
      vuelta139_2b_mutaciones.py                     4.0s
      vuelta140_2a_mutaciones.py                     3.8s
      vuelta133_tarea2e_mutacion_cifras.py           3.3s
      vuelta141_2_mutaciones.py                      3.3s
      vuelta135_2e_mutacion_2.py                     3.2s
      vuelta135_2e_mutacion_1.py                     3.1s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
      vuelta135_2e_mutacion_3.py, exit declarado 1, marca obligatoria 'NO TIENE CONVENCION MECANICA DE CONTEO':
         su SUJETO FIJO es el REPORTE.md de la vuelta 134, congelado por banco 9.10, y ES ANTERIOR A LOS DELIMITADORES DE CABECERA TALLADA. Medido en esta vuelta: grep -c 'CABECERA TALLADA' docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md da 0, y sobre docs/loop/REPORTE.md da 3. La ampliacion del vocabulario de la TAREA 2.a (vuelta 142) hace que la guarda vea ahora la celda '3 fila(s)' del desfase del calibrado, que EN UN REPORTE MODERNO vive DENTRO de la cabecera delimitada y queda recortada antes de parsear, y en este sujeto no, porque las marcas no existian aun. LAS DOS CIFRAS QUE ESTA MUTACION PRUEBA SI COTEJAN (la salida publica '2 POR ETIQUETA'): lo que cae es una tercera, ajena al caso. El sujeto NO se retoca, porque su valor es estar congelado.
      vuelta140_2a_mutaciones.py, exit declarado 2, marca obligatoria 'VEREDICTO (iii): NO CALZA':
         su bloque (iii), el caso positivo sobre la fase 05, sale NO CALZA y esta DECLARADO desde la vuelta 140: el auditor lo reconocio como caida SUYA de encargo (acta 140, 4.5, 'EL AUDITOR ELIGIO MAL EL SUJETO CONGELADO'). OP-S-05, OP-S-08, OP-S-11 y OP-S-12 tienen HUELLA DE GRAFO IDENTICA (los cuatro campos vacios) y lo unico que las separa es `estado`, que el encargo prohibe mirar: NINGUNA VARA DE GRAFO PUEDE SEPARARLAS. Los bloques (i) y (ii) SI muerden y son los que esta bateria vigila.
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD e411137f9d81, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD e411137f9d81, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 1: 1
FIN (reloj de pared, UTC): 2026-09-08T04:04:34Z
DURACION DEL TRAMO (monotona, segundos): 52.2
DURACION DEL TRAMO (monotona, minutos): 0.9


==============================================================================
TRAMO 2 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_2.txt
==============================================================================

CORRIDA DEL TRAMO 2 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:06:22Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD ca70205861b4, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD ca70205861b4, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD ca70205861b4, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 2 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta144_3a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_3b_mutacion_negativa.py
      ENTRADA DEL TRAMO: vuelta144_3c_caso_positivo_1190.py
      ENTRADA DEL TRAMO: vuelta145_2a_mutacion_ancla_unica.py
      ENTRADA DEL TRAMO: vuelta145_2b_mutacion_arneses.py
      ENTRADA DEL TRAMO: vuelta145_2c_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta146_2b_mutacion_ausencias.py
      ENTRADA DEL TRAMO: vuelta147_2c_mutacion_vitalidad.py
      ENTRADA DEL TRAMO: vuelta147_3d_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta147_3e_simular_a26.py
      ENTRADA DEL TRAMO: vuelta148_0d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta148_1a_mutacion_embebido.py
      ENTRADA DEL TRAMO: vuelta148_2a_mutacion_nomina_commiteada.py


  vuelta144_3a_mutaciones.py             exit 0  OK                   4.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3b_mutacion_negativa.py      exit 0  OK                  12.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3c_caso_positivo_1190.py     exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2a_mutacion_ancla_unica.py   exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2b_mutacion_arneses.py       exit 0  OK                  20.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2c_mutacion_censo.py         exit 0  OK                  13.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta146_2b_mutacion_ausencias.py     exit 0  OK                   3.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_2c_mutacion_vitalidad.py     exit 0  OK                 135.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3d_mutacion_nomina.py        exit 0  OK                   5.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3e_simular_a26.py            exit 0  OK                   5.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_0d_mutacion_corredor.py      exit 0  OK                   8.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_1a_mutacion_embebido.py      exit 0  OK                   6.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2a_mutacion_nomina_commiteada.py exit 0  OK                   4.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 225.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 3.8
  CIFRA arnes MAS LENTO: vuelta147_2c_mutacion_vitalidad.py con 135.2s
  CIFRA arnes MAS RAPIDO: vuelta144_3c_caso_positivo_1190.py con 2.9s
  CIFRA mediana por arnes, en segundos: 5.6
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta147_2c_mutacion_vitalidad.py           135.2s
      vuelta145_2b_mutacion_arneses.py              20.1s
      vuelta145_2c_mutacion_censo.py                13.8s
      vuelta144_3b_mutacion_negativa.py             12.7s
      vuelta148_0d_mutacion_corredor.py              8.2s
      vuelta148_1a_mutacion_embebido.py              6.4s
      vuelta147_3d_mutacion_nomina.py                5.6s
      vuelta147_3e_simular_a26.py                    5.1s
      vuelta144_3a_mutaciones.py                     4.7s
      vuelta148_2a_mutacion_nomina_commiteada.py     4.3s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD ca70205861b4, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD ca70205861b4, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 2: 1
FIN (reloj de pared, UTC): 2026-09-08T04:10:10Z
DURACION DEL TRAMO (monotona, segundos): 227.7
DURACION DEL TRAMO (monotona, minutos): 3.8


==============================================================================
TRAMO 3 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_3.txt
==============================================================================

CORRIDA DEL TRAMO 3 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:33:52Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD e72a22b97168, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD e72a22b97168, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD e72a22b97168, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 3 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta148_2b_mutacion_cifras_conjunto.py
      ENTRADA DEL TRAMO: vuelta148_2c_mutacion_vara_parada.py
      ENTRADA DEL TRAMO: vuelta148_2d_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta150_5c_mutacion_ciclo.py
      ENTRADA DEL TRAMO: vuelta154_tarea2d_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta154_tarea6_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta156_tarea4b_mutacion_tallador.py
      ENTRADA DEL TRAMO: vuelta156_tarea5d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta157_tarea4b_mutacion_tachado.py
      ENTRADA DEL TRAMO: vuelta157_tarea5c_mutacion_ruido.py
      ENTRADA DEL TRAMO: vuelta157_tarea6b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta159_tarea6c_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta160_tarea6b_mutacion_puerta.py


  vuelta148_2b_mutacion_cifras_conjunto.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2c_mutacion_vara_parada.py   exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2d_mutacion_exencion.py      exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_5c_mutacion_ciclo.py         exit 0  OK                   3.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea2d_mutacion_guarda.py   exit 0  OK                  95.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea6_mutacion_corredor.py  exit 0  OK                   5.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea4b_mutacion_tallador.py exit 0  OK                   3.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea5d_mutacion_corredor.py exit 0  OK                  51.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea4b_mutacion_tachado.py  exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea5c_mutacion_ruido.py    exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea6b_mutacion_re_sellado.py exit 0  OK                   7.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta159_tarea6c_mutacion_exencion.py exit 0  OK                 451.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea6b_mutacion_puerta.py   exit 1  NO MORDIO            2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 635.2
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 10.6
  CIFRA arnes MAS LENTO: vuelta159_tarea6c_mutacion_exencion.py con 451.0s
  CIFRA arnes MAS RAPIDO: vuelta148_2d_mutacion_exencion.py con 2.6s
  CIFRA mediana por arnes, en segundos: 3.6
  CIFRA arneses que pasan de 30 segundos: 3
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta159_tarea6c_mutacion_exencion.py       451.0s
      vuelta154_tarea2d_mutacion_guarda.py          95.5s
      vuelta156_tarea5d_mutacion_corredor.py        51.1s
      vuelta157_tarea6b_mutacion_re_sellado.py       7.6s
      vuelta154_tarea6_mutacion_corredor.py          5.5s
      vuelta156_tarea4b_mutacion_tallador.py         3.8s
      vuelta150_5c_mutacion_ciclo.py                 3.6s
      vuelta157_tarea5c_mutacion_ruido.py            3.4s
      vuelta160_tarea6b_mutacion_puerta.py           2.9s
      vuelta157_tarea4b_mutacion_tachado.py          2.8s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta160_tarea6b_mutacion_puerta.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD e72a22b97168, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD e72a22b97168, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 3: 1
FIN (reloj de pared, UTC): 2026-09-08T04:44:28Z
DURACION DEL TRAMO (monotona, segundos): 636.5
DURACION DEL TRAMO (monotona, minutos): 10.6


==============================================================================
TRAMO 4 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_4.txt
==============================================================================

CORRIDA DEL TRAMO 4 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:45:31Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 3fa5b035c853, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 3fa5b035c853, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 3fa5b035c853, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 4 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta160_tarea7c_mutacion_guarda_cita.py
      ENTRADA DEL TRAMO: vuelta161_tarea1a_mutacion_alcance.py
      ENTRADA DEL TRAMO: vuelta162_tarea1a_mutacion_serie.py
      ENTRADA DEL TRAMO: vuelta162_tarea2a_mutacion_puerta.py
      ENTRADA DEL TRAMO: vuelta162_tarea2b_mutacion_excepcion.py
      ENTRADA DEL TRAMO: vuelta162_tarea3_mutacion_fila.py
      ENTRADA DEL TRAMO: vuelta163_tarea1b_mutacion_relectura.py
      ENTRADA DEL TRAMO: vuelta163_tarea1c_mutacion_tramo.py
      ENTRADA DEL TRAMO: vuelta163_tarea2_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta163_tarea4a_mutacion_cobertura.py
      ENTRADA DEL TRAMO: vuelta163_tarea4b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta163_tarea5a_mutacion_contador.py
      ENTRADA DEL TRAMO: vuelta164_tarea1_mutacion_registro.py


  vuelta160_tarea7c_mutacion_guarda_cita.py exit 0  OK                   8.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta161_tarea1a_mutacion_alcance.py  exit 0  OK                  13.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea1a_mutacion_serie.py    exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2a_mutacion_puerta.py   exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2b_mutacion_excepcion.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea3_mutacion_fila.py      exit 0  OK                   3.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1b_mutacion_relectura.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1c_mutacion_tramo.py    exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea2_mutacion_nomina.py    exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4a_mutacion_cobertura.py exit 0  OK                   5.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4b_mutacion_re_sellado.py exit 0  OK                  25.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea5a_mutacion_contador.py exit 0  OK                   6.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta164_tarea1_mutacion_registro.py  exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 81.1
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.4
  CIFRA arnes MAS LENTO: vuelta163_tarea4b_mutacion_re_sellado.py con 25.7s
  CIFRA arnes MAS RAPIDO: vuelta163_tarea1c_mutacion_tramo.py con 2.7s
  CIFRA mediana por arnes, en segundos: 2.8
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta163_tarea4b_mutacion_re_sellado.py      25.7s
      vuelta161_tarea1a_mutacion_alcance.py         13.0s
      vuelta160_tarea7c_mutacion_guarda_cita.py      8.5s
      vuelta163_tarea5a_mutacion_contador.py         6.1s
      vuelta163_tarea4a_mutacion_cobertura.py        5.2s
      vuelta162_tarea3_mutacion_fila.py              3.3s
      vuelta162_tarea2b_mutacion_excepcion.py        2.8s
      vuelta162_tarea2a_mutacion_puerta.py           2.8s
      vuelta162_tarea1a_mutacion_serie.py            2.8s
      vuelta164_tarea1_mutacion_registro.py          2.8s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 3fa5b035c853, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 3fa5b035c853, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 4: 1
FIN (reloj de pared, UTC): 2026-09-08T04:46:53Z
DURACION DEL TRAMO (monotona, segundos): 82.8
DURACION DEL TRAMO (monotona, minutos): 1.4


==============================================================================
TRAMO 5 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_5.txt
==============================================================================

CORRIDA DEL TRAMO 5 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:47:36Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD a9a8fff983c3, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD a9a8fff983c3, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD a9a8fff983c3, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 5 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta164_tarea4_mutacion_005.py
      ENTRADA DEL TRAMO: vuelta165_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta165_tarea2_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta165_tarea4_mutacion_sujeto.py
      ENTRADA DEL TRAMO: vuelta165_tarea6_mutacion_op_l_01.py
      ENTRADA DEL TRAMO: vuelta166_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta166_tarea2_mutacion_correccion.py
      ENTRADA DEL TRAMO: vuelta166_tarea3_mutacion_retrato.py
      ENTRADA DEL TRAMO: vuelta166_tarea6_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta167_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta167_tarea3_mutacion_ii.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_nota.py


  vuelta164_tarea4_mutacion_005.py       exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea1_mutacion_registro.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea2_mutacion_censo.py     exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea4_mutacion_sujeto.py    exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea6_mutacion_op_l_01.py   exit 1  NO MORDIO            3.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta166_tarea1_mutacion_registro.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea2_mutacion_correccion.py exit 1  NO MORDIO            3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta166_tarea3_mutacion_retrato.py   exit 0  OK                   7.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea6_mutacion_guarda.py    exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea1_mutacion_registro.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea3_mutacion_ii.py        exit 0  OK                   3.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_registro.py  exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_nota.py      exit 1  NO MORDIO            2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 42.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.7
  CIFRA arnes MAS LENTO: vuelta166_tarea3_mutacion_retrato.py con 7.6s
  CIFRA arnes MAS RAPIDO: vuelta166_tarea1_mutacion_registro.py con 2.7s
  CIFRA mediana por arnes, en segundos: 2.9
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta166_tarea3_mutacion_retrato.py           7.6s
      vuelta167_tarea3_mutacion_ii.py                3.4s
      vuelta166_tarea2_mutacion_correccion.py        3.4s
      vuelta165_tarea6_mutacion_op_l_01.py           3.1s
      vuelta165_tarea4_mutacion_sujeto.py            3.1s
      vuelta165_tarea2_mutacion_censo.py             2.9s
      vuelta168_tarea1_mutacion_nota.py              2.9s
      vuelta166_tarea6_mutacion_guarda.py            2.8s
      vuelta164_tarea4_mutacion_005.py               2.8s
      vuelta165_tarea1_mutacion_registro.py          2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 3 (vuelta165_tarea6_mutacion_op_l_01.py, vuelta166_tarea2_mutacion_correccion.py, vuelta168_tarea1_mutacion_nota.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD a9a8fff983c3, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD a9a8fff983c3, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 3 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 3 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 5: 1
FIN (reloj de pared, UTC): 2026-09-08T04:48:21Z
DURACION DEL TRAMO (monotona, segundos): 44.7
DURACION DEL TRAMO (monotona, minutos): 0.7


==============================================================================
TRAMO 6 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_6.txt
==============================================================================

CORRIDA DEL TRAMO 6 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:49:13Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 274a0aed8b83, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 274a0aed8b83, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 274a0aed8b83, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 6 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta168_tarea2_mutacion_reconstructor.py
      ENTRADA DEL TRAMO: vuelta168_tarea4_mutacion_op_v_01.py
      ENTRADA DEL TRAMO: vuelta169_tarea2_mutacion_reanclaje.py
      ENTRADA DEL TRAMO: vuelta170_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta170_tarea2a_mutacion_aislador.py
      ENTRADA DEL TRAMO: vuelta98_tarea4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta99_tarea3_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta109_tarea2_4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py
      ENTRADA DEL TRAMO: vuelta113_tarea2_mutacion_tsc.py
      ENTRADA DEL TRAMO: vuelta171_mutacion_busqueda_acta.py
      ENTRADA DEL TRAMO: vuelta171_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta171_tarea5a_mutacion_enchufe.py


  vuelta168_tarea2_mutacion_reconstructor.py exit 1  NO MORDIO            2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta168_tarea4_mutacion_op_v_01.py   exit 0  OK                  21.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta169_tarea2_mutacion_reanclaje.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea1a_mutacion_registro.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea2a_mutacion_aislador.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta98_tarea4_prueba_mutacion.py     exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta99_tarea3_prueba_mutacion.py     exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta109_tarea2_4_prueba_mutacion.py  exit 0  OK                  29.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta113_tarea2_mutacion_tsc.py       exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_mutacion_busqueda_acta.py    exit 1  NO MORDIO            2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta171_tarea1a_mutacion_registro.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea5a_mutacion_enchufe.py  exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 80.0
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.3
  CIFRA arnes MAS LENTO: vuelta109_tarea2_4_prueba_mutacion.py con 29.0s
  CIFRA arnes MAS RAPIDO: vuelta98_tarea4_prueba_mutacion.py con 2.6s
  CIFRA mediana por arnes, en segundos: 2.7
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta109_tarea2_4_prueba_mutacion.py         29.0s
      vuelta168_tarea4_mutacion_op_v_01.py          21.2s
      vuelta171_tarea5a_mutacion_enchufe.py          2.8s
      vuelta168_tarea2_mutacion_reconstructor.py     2.8s
      vuelta99_tarea3_prueba_mutacion.py             2.8s
      vuelta170_tarea2a_mutacion_aislador.py         2.8s
      vuelta170_tarea1a_mutacion_registro.py         2.7s
      vuelta169_tarea2_mutacion_reanclaje.py         2.7s
      vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py     2.7s
      vuelta171_tarea1a_mutacion_registro.py         2.6s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 2 (vuelta168_tarea2_mutacion_reconstructor.py, vuelta171_mutacion_busqueda_acta.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 274a0aed8b83, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 274a0aed8b83, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 2 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 2 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 6: 1
FIN (reloj de pared, UTC): 2026-09-08T04:50:35Z
DURACION DEL TRAMO (monotona, segundos): 81.7
DURACION DEL TRAMO (monotona, minutos): 1.4


==============================================================================
TRAMO 7 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_7.txt
==============================================================================

CORRIDA DEL TRAMO 7 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:51:16Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD fc68e550e46a, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD fc68e550e46a, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD fc68e550e46a, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 7 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta172_tarea1b_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta172_tarea2a_mutacion_exclusion.py
      ENTRADA DEL TRAMO: vuelta172_tarea3_mutacion_numeracion.py
      ENTRADA DEL TRAMO: vuelta172_tarea5_mutacion_cierre.py
      ENTRADA DEL TRAMO: vuelta173_tarea1b_mutacion_hueco.py
      ENTRADA DEL TRAMO: vuelta174_tarea1a_mutacion_44.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_esqueleto.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_sellar.py
      ENTRADA DEL TRAMO: vuelta174_tarea2b_mutacion_confirmar.py
      ENTRADA DEL TRAMO: vuelta176_tarea1c_mutacion_tramos.py
      ENTRADA DEL TRAMO: vuelta177_tarea1b_mutacion_esperado_vivo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1d_mutacion_cotejo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1e_mutacion_correcciones_chicas.py


  vuelta172_tarea1b_mutacion_registro.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea2a_mutacion_exclusion.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea3_mutacion_numeracion.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea5_mutacion_cierre.py    exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta173_tarea1b_mutacion_hueco.py    exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1a_mutacion_44.py       exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_esqueleto.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_sellar.py   exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea2b_mutacion_confirmar.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta176_tarea1c_mutacion_tramos.py   exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1b_mutacion_esperado_vivo.py exit 0  OK                   3.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1d_mutacion_cotejo.py   exit 0  OK                   3.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1e_mutacion_correcciones_chicas.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 37.3
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.6
  CIFRA arnes MAS LENTO: vuelta177_tarea1d_mutacion_cotejo.py con 3.6s
  CIFRA arnes MAS RAPIDO: vuelta174_tarea2b_mutacion_confirmar.py con 2.6s
  CIFRA mediana por arnes, en segundos: 2.8
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta177_tarea1d_mutacion_cotejo.py           3.6s
      vuelta177_tarea1b_mutacion_esperado_vivo.py     3.5s
      vuelta173_tarea1b_mutacion_hueco.py            2.8s
      vuelta177_tarea1e_mutacion_correcciones_chicas.py     2.8s
      vuelta172_tarea1b_mutacion_registro.py         2.8s
      vuelta172_tarea2a_mutacion_exclusion.py        2.8s
      vuelta174_tarea1b_mutacion_esqueleto.py        2.8s
      vuelta176_tarea1c_mutacion_tramos.py           2.8s
      vuelta172_tarea5_mutacion_cierre.py            2.7s
      vuelta174_tarea1a_mutacion_44.py               2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD fc68e550e46a, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD fc68e550e46a, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 7: 1
FIN (reloj de pared, UTC): 2026-09-08T04:51:55Z
DURACION DEL TRAMO (monotona, segundos): 39.1
DURACION DEL TRAMO (monotona, minutos): 0.7


==============================================================================
TRAMO 8 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_8.txt
==============================================================================

CORRIDA DEL TRAMO 8 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:52:34Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 3d79c288f84a, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 3d79c288f84a, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 3d79c288f84a, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 8 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta177_tarea1f_mutacion_tope_minutos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1b_mutacion_hermano.py
      ENTRADA DEL TRAMO: vuelta178_tarea1c_mutacion_ast.py
      ENTRADA DEL TRAMO: vuelta178_tarea1d_mutacion_puestos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1e_mutacion_higiene.py
      ENTRADA DEL TRAMO: vuelta178_tarea2_mutacion_resolutor.py
      ENTRADA DEL TRAMO: vuelta178_tarea4_mutacion_consumidas.py
      ENTRADA DEL TRAMO: vuelta150_2d_simular_op_c_05.py
      ENTRADA DEL TRAMO: vuelta160_tarea3b_caso_positivo.py
      ENTRADA DEL TRAMO: vuelta179_tarea1b_mutacion_citas.py
      ENTRADA DEL TRAMO: vuelta179_tarea3_mutacion_triangulos.py
      ENTRADA DEL TRAMO: vuelta179_tarea1d_mutacion_corte.py
      ENTRADA DEL TRAMO: vuelta180_tarea1b_mutacion_etiqueta.py


  vuelta177_tarea1f_mutacion_tope_minutos.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1b_mutacion_hermano.py  exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1c_mutacion_ast.py      exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1d_mutacion_puestos.py  exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1e_mutacion_higiene.py  exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea2_mutacion_resolutor.py exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea4_mutacion_consumidas.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_2d_simular_op_c_05.py        exit 0  OK                   4.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea3b_caso_positivo.py     exit 0  OK                  12.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1b_mutacion_citas.py    exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea3_mutacion_triangulos.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1d_mutacion_corte.py    exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea1b_mutacion_etiqueta.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 48.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.8
  CIFRA arnes MAS LENTO: vuelta160_tarea3b_caso_positivo.py con 12.7s
  CIFRA arnes MAS RAPIDO: vuelta180_tarea1b_mutacion_etiqueta.py con 2.7s
  CIFRA mediana por arnes, en segundos: 2.8
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta160_tarea3b_caso_positivo.py            12.7s
      vuelta150_2d_simular_op_c_05.py                4.3s
      vuelta178_tarea1c_mutacion_ast.py              3.2s
      vuelta178_tarea1d_mutacion_puestos.py          3.2s
      vuelta178_tarea2_mutacion_resolutor.py         3.0s
      vuelta178_tarea1e_mutacion_higiene.py          2.9s
      vuelta179_tarea1d_mutacion_corte.py            2.8s
      vuelta179_tarea3_mutacion_triangulos.py        2.8s
      vuelta178_tarea1b_mutacion_hermano.py          2.8s
      vuelta179_tarea1b_mutacion_citas.py            2.8s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 3d79c288f84a, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 3d79c288f84a, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 8: 1
FIN (reloj de pared, UTC): 2026-09-08T04:53:25Z
DURACION DEL TRAMO (monotona, segundos): 50.4
DURACION DEL TRAMO (monotona, minutos): 0.8


==============================================================================
TRAMO 9 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_9.txt
==============================================================================

CORRIDA DEL TRAMO 9 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:54:05Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 97185bc4b223, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 97185bc4b223, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 97185bc4b223, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 9 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta180_tarea2c_mutacion_cableado.py
      ENTRADA DEL TRAMO: vuelta180_tarea3_mutacion_corte_de_tramos.py
      ENTRADA DEL TRAMO: vuelta180_tarea4_mutacion_texto_y_clon.py
      ENTRADA DEL TRAMO: vuelta180_tarea5_mutacion_backlog_l02.py
      ENTRADA DEL TRAMO: vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py
      ENTRADA DEL TRAMO: vuelta182_tarea2_mutacion_apertura_auditor.py
      ENTRADA DEL TRAMO: vuelta183_tarea1c_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta183_tarea1b_mutacion_atribucion.py
      ENTRADA DEL TRAMO: vuelta184_tarea1c_mutacion_estimacion.py
      ENTRADA DEL TRAMO: vuelta185_tarea1b_mutacion_sin_temporal.py
      ENTRADA DEL TRAMO: vuelta185_tarea1c_mutacion_bateria_continuada.py
      ENTRADA DEL TRAMO: vuelta186_tarea2a_mutacion_pieza4.py
      ENTRADA DEL TRAMO: vuelta186_tarea2b_mutacion_pieza2_cercas.py


  vuelta180_tarea2c_mutacion_cableado.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea3_mutacion_corte_de_tramos.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea4_mutacion_texto_y_clon.py exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea5_mutacion_backlog_l02.py exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py exit 0  OK                   3.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta182_tarea2_mutacion_apertura_auditor.py exit 0  OK                   3.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt
  vuelta183_tarea1c_mutacion_veredicto.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1C_MUTACION_VEREDICTO.txt
  vuelta183_tarea1b_mutacion_atribucion.py exit 0  OK                   3.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt
  vuelta184_tarea1c_mutacion_estimacion.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V184_T1C_MUTACION_ESTIMACION.txt
  vuelta185_tarea1b_mutacion_sin_temporal.py exit 0  OK                   4.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt, SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt
  vuelta185_tarea1c_mutacion_bateria_continuada.py exit 1  NO MORDIO            5.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt
      ARNES DE LA RAMA DE LA BATERIA CONTINUADA (vuelta 185, TAREA 1.c)
  vuelta186_tarea2a_mutacion_pieza4.py   exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2A_MUTACION_PIEZA4.txt
  vuelta186_tarea2b_mutacion_pieza2_cercas.py exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 44.3
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.7
  CIFRA arnes MAS LENTO: vuelta185_tarea1c_mutacion_bateria_continuada.py con 5.9s
  CIFRA arnes MAS RAPIDO: vuelta180_tarea3_mutacion_corte_de_tramos.py con 2.7s
  CIFRA mediana por arnes, en segundos: 3.0
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta185_tarea1c_mutacion_bateria_continuada.py     5.9s
      vuelta185_tarea1b_mutacion_sin_temporal.py     4.5s
      vuelta182_tarea2_mutacion_apertura_auditor.py     3.8s
      vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py     3.6s
      vuelta183_tarea1b_mutacion_atribucion.py       3.5s
      vuelta184_tarea1c_mutacion_estimacion.py       3.1s
      vuelta180_tarea4_mutacion_texto_y_clon.py      3.0s
      vuelta180_tarea5_mutacion_backlog_l02.py       2.9s
      vuelta186_tarea2a_mutacion_pieza4.py           2.9s
      vuelta186_tarea2b_mutacion_pieza2_cercas.py     2.9s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta185_tarea1c_mutacion_bateria_continuada.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 97185bc4b223, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 97185bc4b223, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 9: 1
FIN (reloj de pared, UTC): 2026-09-08T04:54:51Z
DURACION DEL TRAMO (monotona, segundos): 45.9
DURACION DEL TRAMO (monotona, minutos): 0.8


==============================================================================
TRAMO 10 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_10.txt
==============================================================================

CORRIDA DEL TRAMO 10 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:55:39Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD ed74786dbe7a, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD ed74786dbe7a, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD ed74786dbe7a, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 10 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta186_tarea2c_mutacion_cierre_tardio.py
      ENTRADA DEL TRAMO: vuelta186_tarea2d_mutacion_seccion4.py
      ENTRADA DEL TRAMO: vuelta187_tarea4_mutacion_dos_convenciones.py
      ENTRADA DEL TRAMO: vuelta187_tarea5b_mutacion_seccion4_tardio.py
      ENTRADA DEL TRAMO: vuelta188_tarea2_mutacion_pata_documental.py
      ENTRADA DEL TRAMO: vuelta188_tarea3c_mutacion_exclusion_por_rojo.py
      ENTRADA DEL TRAMO: vuelta188_tarea4_mutacion_cobertura_parejas.py
      ENTRADA DEL TRAMO: vuelta188_tarea5a_mutacion_vecinos_evitar.py
      ENTRADA DEL TRAMO: vuelta190_tarea2b_mutacion_deuda_y_fallo.py
      ENTRADA DEL TRAMO: vuelta190_tarea3b_mutacion_selladas_ajenas.py
      ENTRADA DEL TRAMO: vuelta191_tarea3_mutacion_lineas.py
      ENTRADA DEL TRAMO: vuelta191_tarea4_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta191_tarea6_mutacion_bloque_tallado.py


  vuelta186_tarea2c_mutacion_cierre_tardio.py exit 0  OK                   2.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
  vuelta186_tarea2d_mutacion_seccion4.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2D_MUTACION_SECCION4.txt
  vuelta187_tarea4_mutacion_dos_convenciones.py exit 0  OK                   3.2s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt
  vuelta187_tarea5b_mutacion_seccion4_tardio.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO.txt
  vuelta188_tarea2_mutacion_pata_documental.py exit 0  OK                   2.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt
  vuelta188_tarea3c_mutacion_exclusion_por_rojo.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt
  vuelta188_tarea4_mutacion_cobertura_parejas.py exit 0  OK                   3.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt
  vuelta188_tarea5a_mutacion_vecinos_evitar.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T5A_MUTACION_VECINOS_EVITAR.txt
  vuelta190_tarea2b_mutacion_deuda_y_fallo.py exit 0  OK                   3.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt
  vuelta190_tarea3b_mutacion_selladas_ajenas.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt
  vuelta191_tarea3_mutacion_lineas.py    exit 0  OK                  80.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T3_MUTACION_LINEAS.txt
  vuelta191_tarea4_mutacion_veredicto.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T4_MUTACION_VEREDICTO.txt
  vuelta191_tarea6_mutacion_bloque_tallado.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 115.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.9
  CIFRA arnes MAS LENTO: vuelta191_tarea3_mutacion_lineas.py con 80.5s
  CIFRA arnes MAS RAPIDO: vuelta191_tarea4_mutacion_veredicto.py con 2.7s
  CIFRA mediana por arnes, en segundos: 2.9
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta191_tarea3_mutacion_lineas.py           80.5s
      vuelta188_tarea4_mutacion_cobertura_parejas.py     3.9s
      vuelta187_tarea4_mutacion_dos_convenciones.py     3.2s
      vuelta191_tarea6_mutacion_bloque_tallado.py     3.1s
      vuelta190_tarea3b_mutacion_selladas_ajenas.py     3.1s
      vuelta190_tarea2b_mutacion_deuda_y_fallo.py     3.0s
      vuelta186_tarea2c_mutacion_cierre_tardio.py     2.9s
      vuelta188_tarea2_mutacion_pata_documental.py     2.8s
      vuelta188_tarea5a_mutacion_vecinos_evitar.py     2.7s
      vuelta188_tarea3c_mutacion_exclusion_por_rojo.py     2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD ed74786dbe7a, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD ed74786dbe7a, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 10: 1
FIN (reloj de pared, UTC): 2026-09-08T04:57:36Z
DURACION DEL TRAMO (monotona, segundos): 117.6
DURACION DEL TRAMO (monotona, minutos): 2.0


==============================================================================
TRAMO 11 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V183_BATERIA_TRAMO_11.txt
==============================================================================

CORRIDA DEL TRAMO 11 DE 11, BATERIA DE LA VUELTA 183
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-08T04:58:16Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 08e9acddabec, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 08e9acddabec, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 08e9acddabec, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 11 de 11
  CIFRA entradas de ESTE tramo: 5
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta192_tarea4_mutacion_cuarta_puerta.py
      ENTRADA DEL TRAMO: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      ENTRADA DEL TRAMO: vuelta194_tarea2c_mutacion_sede_del_turno.py
      ENTRADA DEL TRAMO: vuelta195_tarea3g_mutacion_nomina_enchufada.py
      ENTRADA DEL TRAMO: vuelta195_tarea4c_mutacion_componer_rojo.py


  vuelta192_tarea4_mutacion_cuarta_puerta.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt
  vuelta193_tarea4e_mutacion_sello_entre_procesos.py exit 0  OK                   3.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt
  vuelta194_tarea2c_mutacion_sede_del_turno.py exit 0  OK                   5.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt, SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt, SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt
  vuelta195_tarea3g_mutacion_nomina_enchufada.py exit 0  OK                   2.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt
  vuelta195_tarea4c_mutacion_componer_rojo.py exit 0  OK                   3.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 5
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 17.2
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.3
  CIFRA arnes MAS LENTO: vuelta194_tarea2c_mutacion_sede_del_turno.py con 5.3s
  CIFRA arnes MAS RAPIDO: vuelta195_tarea3g_mutacion_nomina_enchufada.py con 2.5s
  CIFRA mediana por arnes, en segundos: 3.1
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta194_tarea2c_mutacion_sede_del_turno.py     5.3s
      vuelta193_tarea4e_mutacion_sello_entre_procesos.py     3.7s
      vuelta195_tarea4c_mutacion_componer_rojo.py     3.1s
      vuelta192_tarea4_mutacion_cuarta_puerta.py     2.6s
      vuelta195_tarea3g_mutacion_nomina_enchufada.py     2.5s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 08e9acddabec, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 08e9acddabec, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 11: 1
FIN (reloj de pared, UTC): 2026-09-08T04:58:34Z
DURACION DEL TRAMO (monotona, segundos): 18.5
DURACION DEL TRAMO (monotona, minutos): 0.3
```
