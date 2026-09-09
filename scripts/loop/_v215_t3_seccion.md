### TAREA 3. EL CIERRE INTEGRAL, TODO LO QUE NO NECESITA CREDENCIAL

**LA GUARDA DE ESTA SECCION ES LA QUE ME FALTO EN LA 214, Y VA DELANTE.** El
compositor mira **las seis fuentes** antes de componer y **CIFRA fuentes
ausentes: 0**; si faltara una, **REVIENTA y no escribe**, en vez de dejar una
celda en blanco y seguir. Lo mismo con las cifras: **necesita 25 y le
faltan 0**.

#### 3.a. EL CICLO ENTERO DE GATE 0, Y POR QUE SUS DOS LADOS NO VAN LOS DOS AQUI

**EL LADO APERTURA CORRIO ANTES DE LA PRIMERA TAREA Y ESTA SELLADO**, con su
consola en `docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt` y sus nueve salidas en disco. **PEOR EXITCODE DE LOS
OCHO, LEIDO DE ESA CONSOLA: 0.**

**EL LADO CIERRE NO SE CORRE AQUI Y DIGO POR QUE, QUE NO ES PEREZA:**
`EJECUTOR.md` 1 dice que **EL ESTADO AL CIERRE SE MIDE AL CIERRE**, y medirlo en
mitad de la vuelta y publicarlo como cierre es la caida de la vuelta 28. **El
lado CIERRE corre al cerrar y sus cifras van en la seccion 3.1**, con las
DIECIOCHO salidas cotejadas y los dos lados juntos.

#### 3.b. LAS TRES SUITES, CADA UNA CORRIDA SOLA Y SELLADA APARTE

**Son las mismas tres que el ciclo corre en sus puestos 7, 8a y 8b, y aqui van
CORRIDAS OTRA VEZ Y SOLAS**, para que su cifra no dependa de leer dentro de la
salida de otro instrumento.

**FILAS ARMADAS: 3. FILAS QUE DEBERIA HABER: 3.**

| suite | comando | exitcode | bytes | salida sellada |
|---|---|---:|---:|---|
| **motor** | `engine/run_all_tests.py` | **0** | 1164 | `docs/loop/SALIDA_V215_T3_SUITE_MOTOR.txt` |
| **tsc** | `npx tsc --noEmit -p tsconfig.json` | **0** | 15 | `docs/loop/SALIDA_V215_T3_SUITE_TSC.txt` |
| **web** | `pnpm test` | **0** | 338 | `docs/loop/SALIDA_V215_T3_SUITE_WEB.txt` |

#### 3.c. EL INVENTARIO DE LAS 71 FICHAS CONTRA SUS PRUEBAS

**Corrido con `scripts/loop/vuelta150_3_relectura_expediente.py --corte` y el
hash de MI apertura, `416c7a43`**, que es el que el encargo pide. Salida sellada
en `docs/loop/SALIDA_V215_T3_EXPEDIENTE.txt`.

**PUBLICO LA CIFRA QUE SALE, NO LA QUE ME GUSTE:**

- **CIFRA fichas del expediente: 71.**
- **CIFRA fichas que NO CALZAN: 40.**
- **CIFRA congeladas DECLARADAS: 24 | congeladas EN SILENCIO:
  12.**
- **CIFRA fichas en HECHA SIN NINGUNA PRUEBA: 4.**
- **CIFRA fichas en LISTA sin ninguna prueba: 3.**

**MI CIFRA DE 40 ES LA SUYA, Y NO LA AJUSTO PORQUE NO HACE FALTA.** Lo comprobe
ademas **con SU corte** (`docs/loop/SALIDA_V215_T3_EXPEDIENTE_CORTE_AUDITOR.txt`, corrido con `--corte 89c7bf23`): da
**40** que no calzan y **4** en HECHA sin prueba.
**Los dos cortes dan lo mismo**, o sea que la cifra no depende de cual de los dos
hashes se use.

**Y AQUI VA UNA DISCREPANCIA QUE DECLARO EN VEZ DE RESOLVER COPIANDO.** El
encargo dice *"dos de ellas, `OP-V-01` y `OP-L-01`, siguen en HECHA SIN NINGUNA
PRUEBA"*. **Yo mido 4, no dos**, y las cuatro van con su nombre:

| id_op | fase | veredicto de la vara |
|---|---|---|
| `OP-V-01` | 08_VERIFICACION | **HECHA SIN NINGUNA PRUEBA** |
| `OP-L-01` | 09_LECTURAS_DIRIGIDAS | **HECHA SIN NINGUNA PRUEBA** |
| `OP-L-02` | 09_LECTURAS_DIRIGIDAS | **HECHA SIN NINGUNA PRUEBA** |
| `OP-L-03` | 09_LECTURAS_DIRIGIDAS | **HECHA SIN NINGUNA PRUEBA** |

**NO DIGO QUE EL AUDITOR SE EQUIVOQUE Y NO TENGO COMO SABERLO:** las dos que
nombra estan entre las cuatro, y nombrar dos de cuatro no es afirmar que sean
dos. **Lo que hago es publicar las cuatro con su nombre**, porque una vuelta que
copia "dos" de un encargo teniendo cuatro delante es la caida que
`EJECUTOR.md` 2 prohibe.

#### 3.d. EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO

**MARCADOR**, con `python scripts/recomputar_marcador.py 3388`, sellado en
`docs/loop/SALIDA_V215_T3_MARCADOR.txt`: **n 3388, corte 3388, A 550, B 72, C 5,
D 2761, huecos 0, duplicados de puesto 0, pares duplicados
0.**

**CENSO Y ARISTAS**, con `python scripts/loop/vuelta83_conteo_aristas.py WORK`,
sellado en `docs/loop/SALIDA_V215_T3_ARISTAS.txt`: **nodos 3853, vivos 3169, deprecados
684; siguientes 8780, previos 8740, suma 17520.** La union sale
**9914** y **la publico sin cotejarla**, porque el encargo no da su pareja y
una cifra sin pareja no se coteja, se dice.

**EL COTEJO CONTRA LAS CIFRAS QUE EL ENCARGO ME DA, PARA COTEJAR Y NO PARA
COPIAR.** Las suyas viven en `docs/loop/PROMPT_SIGUIENTE.md`, TAREA 3, apartados
(c) y (d).

**FILAS ARMADAS: 13. FILAS QUE DEBERIA HABER: 13.**
**CIFRA celdas que NO CALZAN: 0.**

| cifra | la MIA, medida hoy | la del encargo | veredicto |
|---|---:|---:|---|
| `A` | **550** | 550 | calza |
| `B` | **72** | 72 | calza |
| `C` | **5** | 5 | calza |
| `D` | **2761** | 2761 | calza |
| `depre` | **684** | 684 | calza |
| `huecos` | **0** | 0 | calza |
| `marcador_n` | **3388** | 3388 | calza |
| `no_calzan` | **40** | 40 | calza |
| `nodos` | **3853** | 3853 | calza |
| `prev` | **8740** | 8740 | calza |
| `sig` | **8780** | 8780 | calza |
| `suma` | **17520** | 17520 | calza |
| `vivos` | **3169** | 3169 | calza |

**LAS 13 CALZAN UNA A UNA, Y NO ME LAS CREI: LAS MEDI.** Es la unica
manera de que un cotejo signifique algo.
