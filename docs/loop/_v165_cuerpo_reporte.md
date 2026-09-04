# REPORTE DE LA VUELTA 165 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**EL VEREDICTO DE UNA LINEA: LAS SEIS TAREAS ENTREGADAS, Y LA SEXTA ENTREGA UNA
PARADA QUE NO ES UNA EXCUSA SINO UN HALLAZGO.** `OP-L-01` se abre, se mide contra
el archivo de hoy y **NO se cierra**: su clausula 2 no se puede leer sin
estrechar ni ensanchar, y **su clausula 1, cierta comparando ids literalmente, es
FALSA en cuanto se pasa el resolutor que `P.1` obliga**. Traigo **una caida
propia de esta vuelta, cazada por una medicion mia y no por una relectura**,
**una familia inventada que mi propio arnes me tumbo antes de publicarla**,
**CINCO DISCUTIBLES MARCADOS** y **TRES PREGUNTAS**. **Cero nodos tocados, cero
aristas movidas y el grafo intacto.** Marco los discutibles antes de saber si
acierto.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

Todo lo de esta seccion sale de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 165`, salida
`docs/loop/SALIDA_V165_T7_CABECERA.txt`, pegada entera por
`scripts/loop/vuelta165_tarea7_escribir_reporte.py`, que la LEE del fichero y
PARA si no esta.

<!-- CABECERA TALLADA -->
<<<CABECERA>>>
<!-- FIN CABECERA TALLADA -->

**LA UNICA FILA QUE SE MUEVE CONTRA LA CABECERA DE LA 164 ES LA DE LA WEB, Y EL
MOTIVO ESTA FUERA DEL BUCLE.** De **80 y 1.030**, que era la cifra vieja de la
cabecera de la 164, a **82 y 1.040**, medidas hoy en
`docs/loop/SALIDA_V165_WEB_APERTURA.txt`, `docs/loop/SALIDA_V165_WEB_CIERRE.txt`
y `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`. No lo movio esta vuelta ni
ninguna del bucle: lo movio la sesion con credencial del fundador al cerrar la
fase 08. **Medido con mi comando** en la TAREA 5, no copiado de su commit.

**EL CORREDOR DE ESTA VUELTA NO ADMITE NINGUN HASH Y NO HIZO FALTA ADMITIR
NINGUNO.** El acta 164 (`2c00a1c0`) escribe su encargo en el mismo commit. El
bloque de apertura nace como HIJO DIRECTO del acta en `d6fa3df1`, y la guarda lo
confirma: `verificar_apertura_sellada.py --vuelta 165` sale **VERDE exit 0**
(`docs/loop/SALIDA_V165_APERTURA_GUARDA.txt`), con los **diez** ficheros de
apertura nacidos todos ahi. **El bloque no se fragmento.**

**EL CORREDOR TIENE SIETE COMMITS**, contados con
`git rev-list --count 2c00a1c0..HEAD` en esta vuelta; el octavo es el que lleva
este reporte, y **un reporte no puede nombrar el commit que lo lleva**, porque
ese commit se crea despues de escribirlo (la menor 5.4 del acta 164, acatada).

**LA APERTURA Y EL CIERRE NO HEREDAN UNO DEL OTRO.** El ciclo de Gate 0 se corrio
ENTERO y en su orden las dos veces, **nunca `run_phase1` suelto**, que es la
trampa que el auditor piso en su CAIDA 1 de la 164: `--reaplico-curaduria`,
`etiquetas_de_cara --aplicar`, `sync_assets_web` y DESPUES
`git diff HEAD --numstat -- dataset/ web/ engine/`, que da **CERO FILAS** en los
dos lados (`SALIDA_V165_CICLO_NUMSTAT_APERTURA.txt` y
`SALIDA_V165_CICLO_NUMSTAT_CIERRE.txt`).

**LA `M` DE `dataset/metadata/master_graph.json` NO SE ARREGLA Y NO SE COMMITEA
SOLA**, como el encargo manda: es fin de linea y no contenido, y el `numstat` en
cero filas lo prueba en los dos lados.

## 1. TAREA 1, LOS REGISTROS: `R.34`, Y SU CIFRA DE CAIDAS SE CUENTA PORQUE EL ENCARGO TRAE DOS

**Salidas:** `docs/loop/SALIDA_V165_T1_REGISTRO_ACTA_164.txt` (la escritura),
`SALIDA_V165_T1_REGISTRO_IDEM.txt` (la segunda corrida),
`SALIDA_V165_T1_MUTACION_REGISTRO.txt` (el caso positivo). **Instrumento:**
`scripts/loop/vuelta165_tarea1_registrar_acta164.py`.

**EL NUMERO NO SE TECLEA.** `serie_de_registros.py` recomputado ANTES de escribir
da **25 entradas, 0 colisiones, 0 huecos, siguiente libre `R.34`**; recomputado
DESPUES da **26 entradas, 0 colisiones, 0 huecos**, y la serie ve la entrada
nueva en `docs/PENDIENTES.md:11623`. **La cifra que el encargo adelanta coincide
con la mia, y la que se publica es la mia.**

**LA ESCRITURA ES POR ADICION PURA:** `git diff --numstat -- docs/PENDIENTES.md`
da **85 anadidas y 0 borradas**.

**IDEMPOTENTE Y COMPROBADO:** la segunda corrida imprime *"YA ESTABA: la entrada
vive como R.34"* y **CIFRA entradas escritas: 0**.

**EL REPARTO POR VIA, CONTADO DEL DICCIONARIO Y NO TECLEADO**
(`SALIDA_V165_T1_REGISTRO_ACTA_164.txt`, seccion E):

| via | cifra | cuales |
|---|---:|---|
| SIN TOCAR NADA | 4 | 6.1, 6.2, 6.7, 6.8 |
| EN MEDICION | 3 | 6.5, 6.6, 6.9 |
| EN CODIGO | 1 | 6.3 |
| EN EL REPORTE | 1 | 6.4 |
| EN EJECUCION | 1 | 6.10 |

**Y LA DISCREPANCIA DEL PROPIO ENCARGO SE DECLARA EN VEZ DE RESOLVERSE
COPIANDO** (`EJECUTOR.md` 2). Su TAREA 1 pide *"MIS DOS CAIDAS de la seccion 4
del acta"*; su prosa de apertura, en el mismo encargo, dice *"Y VAN MIS TRES
CAIDAS DE HOY, que se registran igual que las tuyas"* **y las enumera**. **La
seccion 4 del acta 164, contada hoy por el instrumento dentro del cuerpo acotado
del acta, trae TRES** negritas `CAIDA n`, en `docs/loop/ACTA_AUDITOR.md:54578`,
`:54589` y `:54605`. **Se registran las TRES: tres cubre dos, y dos dejaria una
caida del auditor sin registro.** La cifra **no esta tecleada en el
instrumento**: se cuenta, y el caso positivo lo prueba con actas fabricadas de
1, 2, 3 y 5 caidas.

**CASO POSITIVO POR MUTACION: 18 casos pasan tal cual y los 18 CAEN al mutar su
esperado** (`SALIDA_V165_T1_MUTACION_REGISTRO.txt`, secciones F y G).

## 2. TAREA 2, EL PUNTO CIEGO DEL CENSO: ARREGLADO EN LA FUENTE, Y CON EL INVARIANTE QUE EL ENSANCHE SOLO NO DA

**Salidas:** `docs/loop/SALIDA_V165_T2_CENSO_ANTES_DESPUES.txt` y
`SALIDA_V165_T2_MUTACION_CENSO.txt`. **Fuente tocada:**
`scripts/loop/verificar_mutaciones_viejas.py`.

**EL AGUJERO, RECOMPUTADO POR MI ANTES DE TOCAR NADA.** El patron era
`^vuelta(\d+).*mutacion.*\.py$` y **exigia la palabra `mutacion` en el nombre**.
Dos entradas de su propia nomina no la llevan:
`vuelta144_3c_caso_positivo_1190.py` y `vuelta147_3e_simular_a26.py`, **y las dos
existen en disco**. `arneses_que_faltan()` produce el VERDE *"NINGUN arnes
posterior se queda fuera de la nomina"*, y **ese verde solo cubria a los que se
llamaran `mutacion`**.

**LAS DOS SALIDAS QUE LA 6.3 ADMITE SE TOMAN LAS DOS, PORQUE NINGUNA SOLA
BASTA:**

  - **(a) EL PATRON CUBRE LO QUE LA NOMINA YA CONTIENE.** `FAMILIAS_DE_ARNES` no
    se invento: **se leyo de los nombres que la nomina real trae**, y son
    **`mutacion`, `caso_positivo`, `simular`**. Los invisibles de la nomina pasan
    de **2 a 0**.
  - **(b) LA FRASE DEL VERDE SE ESTRECHA Y NOMBRA SU UNIVERSO.** Ensanchar el
    patron **mueve la frontera, no la borra**: un arnes de una familia QUINTA
    seguiria siendo invisible, y el verde ahora lo dice con esas palabras.
  - **Y ENCIMA VA EL INVARIANTE QUE FALTABA Y QUE NO CADUCA CUANDO APAREZCA ESA
    FAMILIA QUINTA: `nomina_invisible_al_censo()`.** Un censo que no ve su propia
    nomina esta ciego, y **eso ahora tumba la corrida entera, con su lista
    delante**, al abrir y **recomputado al cierre**.

**Y VA UNA COSA MIA QUE NO LLEGA A CAIDA PUBLICADA PORQUE EL ARNES LA CAZO ANTES,
Y SE DICE IGUAL: DECLARE UNA CUARTA FAMILIA QUE ERA INVENTO MIO.** Puse
`caso_rojo` en `FAMILIAS_DE_ARNES` y el caso `D_ninguna_familia_declarada_sobra`
salio en **FALLA** en la primera corrida del arnes: existe un
`vuelta88_tarea3_caso_rojo.py` en el directorio, **pero NO en la nomina**, o sea
que declararla era lectura de mi cabeza y no del fichero. **Retirada.** Queda
escrito en el fuente y aqui.

**LA CADENA, ANCLADA A GIT Y NO A LA MEMORIA**
(`SALIDA_V165_T2_CENSO_ANTES_DESPUES.txt`, secciones A0, A y B; el A0 lee
`git ls-tree` sobre `scripts/loop/` y saca la nomina del fuente de ESE arbol):

| arbol | vistos por el censo | nomina | visibles | fuera | la resta que cierra |
|---|---:|---:|---:|---:|---|
| acta 164 `2c00a1c0` | 92 | 53 | 51 | 41 | 92 menos 51 es 41 |
| apertura de la 165 `d6fa3df1` | 92 | 53 | 51 | 41 | 92 menos 51 es 41 |
| hoy, con el patron VIEJO | 95 | 61 | 59 | 36 | 95 menos 59 es 36 |
| hoy, con el patron NUEVO | 123 | 61 | **61** | 62 | 123 menos 61 es 62 |

> Las cifras de hoy se mueven respecto de las de la apertura **porque esta misma
> vuelta anade arneses a la nomina**, y por eso la apertura se lee del arbol de
> git y no de la memoria. La ultima fila es de ANTES de que la TAREA 6 anadiera
> su arnes; la cifra al cierre esta en la seccion 8.

**LA POBLACION QUE EL ENSANCHE HACE VISIBLE Y QUE NADIE HA ADJUDICADO SE DECLARA
Y NO SE TOCA:** **26 arneses pre 148** que el patron viejo no veia y que ahora si
(`caso_positivo` y `simular`), **cero de ellos posteriores a la ultima vuelta de
la nomina**, o sea que **ninguno enciende el rojo del verde**. Van con su nombre
en la seccion D de esa salida. **No entran en la TAREA 4 y no se miden por cuenta
propia.**

**CASO POSITIVO POR MUTACION: 13 casos pasan tal cual y los 13 CAEN**
(`SALIDA_V165_T2_MUTACION_CENSO.txt`). **Corre el patron VIEJO y el NUEVO sobre
el MISMO sujeto fabricado**, asi que **CAE si alguien devuelve el patron a su
forma vieja**, que es la letra del encargo: sobre un directorio fabricado el
patron viejo reclama **1** y el nuevo **3**, y **los 2 que el viejo dejaba pasar
sin mirar van nombrados**.

## 3. TAREA 3, LA CAIDA DE REPORTE DE LA 164: CORREGIDA POR DECLARACION Y SIN BORRAR NADA

**LO QUE EL REPORTE DE LA 164 ESCRIBIO, Y NO SE TOCA:** *"La nomina se COMPUTA
importando el censo de la propia bateria: 92 arneses en `scripts/loop/`, 53 en la
nomina, 41 fuera y anteriores a la vuelta 148."*

**LO QUE FALLA:** las tres cifras son ciertas por separado y **la resta no
cierra**, porque **92 menos 53 son 39, no 41**. El instrumento que produjo el 41
imprime otra cosa y esta sellada: `SALIDA_V164_T5_PRE148.txt` dice **`CIFRA
entradas en la nomina de la bateria: 51`**. **El reporte cambio el 51 del
instrumento por el 53 de la bateria.**

**LA CADENA ENTERA Y CERRADA, RECOMPUTADA HOY DEL ARBOL DEL ACTA**
(`SALIDA_V165_T2_CENSO_ANTES_DESPUES.txt`, seccion A0, sobre `2c00a1c0`): **92
vistos por el censo, 53 en la nomina, 51 de ellas VISIBLES al censo, 41 fuera**,
y la resta que cierra es **92 menos 51**, no 92 menos 53. **El 41 nunca se resto
de 53: se resta de 51**, y **el motivo de fondo es el punto ciego de la TAREA 2**,
que ya esta arreglado en la fuente.

**SE REGISTRA Y NO ACUMULA**, por la letra afinada del 27 ago 2026 que el acta
164 cita: vive en prosa de acompanamiento y no en tabla, cabecera ni conclusion.
**PERO DISPARA LA RELECTURA AL DOBLE DEL TRAMO Y ESO SI SE HACE, Y ESTA HECHO:**
el tramo de esta caida es la propia cadena, y se releyo corriendo el mismo
computo sobre **DOS arboles distintos** (`2c00a1c0` y `d6fa3df1`), **con el mismo
resultado en los dos**, mas una tercera pasada con el patron nuevo. **Tres
pasadas sobre el mismo tramo, no dos.**

## 4. TAREA 4, LOS 41 PRE 148: MEDIDOS UNO POR UNO, Y UNA MEDICION MIA ME TUMBA MI PROPIA CLASIFICACION A MITAD DE CAMINO

**Salidas:** `docs/loop/SALIDA_V165_T4_SUJETO_41.txt` (primera pasada, corrida
sola y sin nada al lado), `SALIDA_V165_T4_SUJETO_41_TRANSITIVO.txt` (**la que
manda**) y `SALIDA_V165_T4_MUTACION_SUJETO.txt`. **Instrumentos:**
`scripts/loop/vuelta165_tarea4_sujeto_de_los_41.py` y su arnes.

**LA PENDIENTE DE DOCTRINA DE LA 164 QUEDA RETIRADA POR MI, Y NO HAY PARADA.** La
adjudicacion 6.5 tiene razon y la cito: *"LO QUE ESTA REGLA EXIGE ES SUJETO
CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN."* **Una regla cuya
condicion es el estado del sujeto no habla del calendario**, asi que no puede ser
retroactiva ni dejar de serlo. **No hace falta doctrina nueva.**

**EL UNIVERSO NO SE INVENTA:** los 41 se computan con el **patron VIEJO**, que es
el universo en el que el acta 164 los nombro y los adjudico. Los 26 que el
ensanche de la TAREA 2 hace visibles **no entran aqui**.

**LA MITAD EMPIRICA, CORRIDA HOY Y SOLA** (`SALIDA_V165_T4_SUJETO_41.txt`,
secciones D, F y H):

| medida | cifra | contra el fichero sellado de la 164 |
|---|---:|---|
| medidos | 41 | 41 |
| exit 0 (`OK`) | 30 | 30 |
| `ANCLA PERDIDA` | 3 | 3 |
| `NO MORDIO` | 8 | 8 |
| tiempo total, segundos | 1.106,2 | 1.091,4 |
| tiempo total, minutos | 18,4 | 18,2 |
| el mas lento | `vuelta142_2d_mutacion_bateria.py`, 507,6s | el mismo, 465,4s |

**Reproduce entero contra la medicion sellada del auditor**, y **el reloj es
mio, no heredado**.

**Y AQUI VA MI CAIDA DE ESTA VUELTA, Y LA CAZO EL ARBOL, NO UNA RELECTURA.** La
primera pasada del clasificador dio **17 SUJETOS CONGELADOS**. Su propia seccion
E publica el `git status` antes y despues, y ahi salen
`SALIDA_V118_TAREA2_6_MUTACION_DD_ANTES.txt` y `_DESPUES.txt` **reescritos con
contenido distinto**: `OP-E-04` y `OP-E-05` pasan de `LISTA` a `HECHA` y sus
aristas de AUSENTES a PRESENTES. **Eso lo movio la sesion con credencial del
fundador, no el arnes.** `vuelta118_tarea2_6_mutacion_dd.py` estaba clasificado
**CONGELADO** y su sujeto es **VIVO**: su fuente no nombra ningun artefacto vivo,
**corre a otro que si**. **Un clasificador de un solo nivel no ve el sujeto de
nadie que delegue.**

**LOS DOS ARREGLOS, LOS DOS MEDIBLES, Y NINGUNO BORRA NADA:**

  1. **TRANSITIVIDAD** hasta punto fijo, con la cadena impresa entera.
  2. **LA REESCRITURA CON CAMBIO REAL ES SENAL VIVA, Y ES EMPIRICA.** La
     atribucion se **computa** del nombre del fichero sellado (`SALIDA_V118_...`
     cruzado contra el censo de scripts), **no se teclea**.

**EL EJEMPLAR QUE JUSTIFICA EL ARREGLO, Y ES EL MEJOR QUE SALIO:**
`vuelta115_tarea2_4_mutacion_z.py` corre `vuelta115_guardas_cierre.py`, que corre
`tallar_veredictos_reporte.py` sobre `docs/loop/REPORTE.md`. **Su sujeto es el
REPORTE VIVO**, que es exactamente la enfermedad de
`vuelta144_2d_mutacion_cobertura.py` que la propia regla del sujeto congelado
cita. Con un solo nivel salia congelado; con la cadena, vivo.

**LAS DOS PASADAS SE QUEDAN LAS DOS Y LA SEGUNDA ES LA QUE MANDA. La mitad
empirica NO se re corrio**: `--reusar` la lee de la salida sellada de esta misma
vuelta, porque lo que se arreglo es la mitad ESTATICA y volver a correr los 41
costaba otros 18 minutos sin anadir una sola cifra.

| pasada | SUJETO CONGELADO | SUJETO VIVO | NO DECIDIBLE |
|---|---:|---:|---:|
| primera, un solo nivel (`SALIDA_V165_T4_SUJETO_41.txt`) | 17 | 24 | 0 |
| **la que manda, con transitividad** (`..._TRANSITIVO.txt`) | **5** | **36** | **0** |

**ENTRAN CINCO, Y CADA UNO CON SU TIEMPO AL LADO** (adjudicacion 6.6; seccion G
de `SALIDA_V165_T4_SUJETO_41_TRANSITIVO.txt`):

| arnes | tiempo, una corrida |
|---|---:|
| `vuelta98_tarea4_prueba_mutacion.py` | 0,1s |
| `vuelta99_tarea3_prueba_mutacion.py` | 0,1s |
| `vuelta109_tarea2_4_prueba_mutacion.py` | 12,3s |
| `vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py` | 0,1s |
| `vuelta113_tarea2_mutacion_tsc.py` | 0,1s |
| **coste total, una corrida** | **12,7s** |
| **coste total, DOS corridas, que es lo que la bateria hace** | **25,4s** |

**NINGUNO ENTRA EN BLOQUE Y NINGUNO SE DESCARTA EN BLOQUE.** Los **36** que se
quedan fuera **costarian 1.094,1 segundos mas**, y por eso importa que el
criterio sea el sujeto y no la antiguedad: **el criterio del sujeto deja fuera
casi todo el coste sin recortar nada por cuenta propia**.

**EL LIMITE DE LOS VEINTE MINUTOS, CON SU CIFRA DELANTE** (adjudicacion 6.6). La
bateria con **62 entradas** tarda **1.156,2 segundos, 19,3 minutos EN MI
MAQUINA** (`docs/loop/SALIDA_V165_BATERIA.txt`). **No pasa de veinte aqui, y muy
probablemente si pasa en la del auditor**, que midio **19,9 minutos con 53
entradas** en la 164, o sea **3,6 minutos mas que yo sobre la misma nomina**.
**Lo digo con la cifra y no recorto la nomina por cuenta propia.**

**CASO POSITIVO POR MUTACION: 28 casos pasan y los 28 CAEN**
(`SALIDA_V165_T4_MUTACION_SUJETO.txt`), con un bloque **C2 nuevo que cubre justo
la transitividad que fallo**: un arnes que delega hereda el sujeto del delegado,
uno que no delega no hereda nada, y el que delega **tampoco entra**.

## 5. TAREA 5, EL ESTADO NUEVO SE MIDE Y NO SE HEREDA

**Salida:** `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`. **Instrumento:**
`scripts/loop/vuelta165_tarea5_estado_nuevo.py`.

| medida | mi comando | **medido hoy por mi** | contraste, y solo contraste |
|---|---|---|---|
| suites de la web (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`) | `pnpm test` en `web/` | **`Test Files 82 passed (82)`** y **`Tests 1040 passed (1040)`**, exitcode 0 | el commit `e966d896` dice 82 y 1.040; la cabecera de la 164 decia 80 y 1.030 |
| `tsc` | `npx tsc --noEmit -p tsconfig.json` en `web/` | **exitcode 0, CERO lineas** | el commit del fundador dice exitcode 0 |
| `sha256` del indice semantico | `hashlib` byte a byte | **`42223fccc725103e861b40e7681afff135267c5c6c4761c8e13dac4fc076d8fd`**, 21.854.994 bytes | el sello publica `42223fcc`; el auditor dice haberlo recomputado |

**LA SEDE DEL INDICE NO SE SUPONE: SE LEE DEL PROPIO `sync_assets_web.py`**
(`DEST = BASE / "web" / "lib" / "assets"`), que es la medicina con la que el
auditor saldo la deuda de los assets. **Comprobadas las tres rutas posibles, hay
UNA sola en disco:** `dataset/metadata/` y `engine/` **NO EXISTEN** (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`).
**Y esa frase no es una busqueda negativa suelta: va con su BARRIDO EXHAUSTIVO
sellado en `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`**, con su `PREGUNTA`, su
`UNIVERSO` (`os.walk` del repo entero salvo `node_modules`, `.git`, `.next` y
`__pycache__`), su `CARDINAL` y **sus dos piernas**:
por nombre da **1 ficheros** (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`),
y por contenido da **395 ficheros** (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`) que solo lo nombran sin serlo,
mas **440** mirados y no decodificables, que se cuentan y no se cuelan como sin
coincidencia.

**EL SELLO SE CIERRA POR ADICION Y NO SE LE BORRA UNA LINEA.**
`docs/loop/SELLO_SESION_CREDENCIAL_2026-09-03.md`, **51 anadidas y 0 borradas**.
Su ultima linea sigue diciendo *"la fase 08 NO se declara cerrada hoy"* y **era
cierta el 3 sep**; el commit `e966d896` la cierra el **4 sep**. **Las dos van en
una tabla con su fecha al lado**, porque el fichero no las distinguia, que es la
enfermedad de la `CORRECCION 22` en otro sitio. Queda anotada tambien la cifra de
la deuda de los assets: **son SEIS y no cinco**, con el cotejo del auditor
(**6 cotejados, 6 cuadran, 0 no cuadran**) citado **como suyo y con su
atribucion**.

## 6. TAREA 6, `OP-L-01`: SE ABRE, SE MIDE Y SALE POR PARADA

**Salidas:** `docs/loop/SALIDA_V165_T6_OP_L_01.txt` y
`SALIDA_V165_T6_MUTACION_OP_L_01.txt`. **Instrumentos:**
`scripts/loop/vuelta165_tarea6_op_l_01.py` y su arnes.

**LA FICHA ENTERA, LEIDA HOY DE `docs/plan/OPERACIONES.jsonl:41`.** Tipo `MESA`,
`orden` 1, `estado` `LISTA`, `fecha_corte` **2026-08-11**, **cero dependencias
declaradas** (por eso la 6.10 la pone primera), y `nodos`, `preservar`,
`eliminar` y `aristas_nuevas` **todos VACIOS**
(`docs/loop/SALIDA_V165_T6_OP_L_01.txt`, seccion A).

**LA SIMULACION PREVIA:** **CERO elementos declarados para escribir**. Es una
operacion de **VERIFICACION PURA**: no mueve un nodo, no mueve una arista y no
toca el grafo. Lo unico que podria cambiar es su propio `estado`.

**EL RESOLUTOR VA DELANTE DE TODO CONTEO** (`P.1`, `EJECUTOR.md` 9): **3.853
ficheros de nodo leidos, 761 alias en el mapa**. La clausula 1 se mide **DOS
veces, literal y resuelta**, para que la diferencia **se vea** en vez de
afirmarse.

**CLAUSULA 1, Y ES EL HALLAZGO DE LA TAREA: NO SE CUMPLE.** Dice *"ninguna de las
once aparece en `INTRA_DOMINIO_VEREDICTOS.jsonl`: viven solo aqui"*. Con
**3.388** filas leidas de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:

| comparacion | pares distintos | de las once, cuantas aparecen |
|---|---:|---:|
| **LITERAL** | 3.388 | **0** |
| **RESUELTA (la que `P.1` obliga)** | 3.009 | **3** |

**LAS TRES, CON SU PUESTO Y SU CLASE, LEIDAS HOY DEL FICHERO:**

| lectura dirigida | donde aparece ya en el cribado | por que la literal no lo veia |
|---|---|---|
| `LD-01` `formalizar_junta_asesora` contra `identificar_consejo_asesores` | **puestos 712 (`A`), 976 (`A`) y 1190 (`D`)** | via el alias `identificar_junta_asesores` y via `formalize_advisory_board` |
| `LD-05` `estrategia_innovacion_producto` contra `estrategia_de_innovacion_producto` | **puesto 1325 (`D`)** | via `estrategia_de_innovacion_de_producto` |
| `LD-11` `pensamiento_visual` contra `pensamiento_visual_modelos_negocio` | **puesto 1281 (`D`)** | `pensamiento_visual` resuelve a `get_visual`, cosa que el propio `LECTURAS_DIRIGIDAS.md` ya decia en su nota |

> **Es exactamente la especie que `P.1` tiene escrita con nombre: una comparacion
> literal INVENTA SALUD, hace desaparecer un problema real.** La clausula es
> verde si nadie resuelve, y `P.1` dice que hay que resolver **sin excepcion**.

**CLAUSULA 2: PARADA, Y VA CON LA LETRA DELANTE.** Dice *"el marcador del cribado
no se mueve: sigue en 2.117"*, con `fecha_corte` **2026-08-11**. **El marcador de
hoy, contado del fichero, es 3.388**, y la diferencia es **1.271**.

  - **(a) LECTURA LITERAL**, *"el marcador vale 2.117 hoy"*: **no se cumple, y no
    puede cumplirse**, porque el cribado cerro en 3.388 con su corte publicado.
  - **(b) LECTURA DE EFECTO**, *"esta operacion no mueve el marcador"*: **si se
    cumpliria**, porque la simulacion da cero escrituras. **Pero para leerla asi
    hay que DESCARTAR el numeral `2.117` de la propia clausula, y eso es
    ESTRECHARLA.**

**NO SE ELIGE NINGUNA DE LAS DOS.** El encargo lo dijo antes de que yo lo
midiera: *"si la clausula no se puede leer como 'el marcador no se mueve por esta
operacion' sin estrechar ni ensanchar nada, PARAS Y LO TRAES con la letra
delante"*. **Esta es la letra, y esta es la parada.**

**CLAUSULA 3: SE CUMPLE SOLO EN PARTE, Y SE DICE POR QUE.** La tabla *"QUE
NOMINAS Y QUE FORMAS CAMBIAN"* de `LECTURAS_DIRIGIDAS.md` nombra **OCHO** nominas
afectadas. `docs/plan/INVENTARIO.jsonl`, cuyas **672** entradas se cuentan en
`docs/loop/SALIDA_V165_T6_OP_L_01.txt`, seccion F, tiene entrada **con
miembros** para **TRES**, y esas tres se re miden hoy con su cobertura al lado
(banco 9.26):

| nomina | entrada del inventario | miembros resueltos | posibles | **cobertura RE MEDIDA HOY** | lo que el inventario declara |
|---|---|---:|---:|---:|---|
| junta asesora | racimo `la junta asesora` | **2** | 1 | **1 de 1** | 6 de 6 (sobre 4 miembros) |
| seleccion de canal | racimo `la seleccion de canal` | 5 | 10 | **10 de 10** | 10 de 10 |
| sales roadmap | racimo `el sales roadmap` | 6 | 15 | **10 de 15** | 15 de 15, citando `LD-66` a `LD-70` |

> **DOS COSAS QUE ESTA RE MEDICION SACA Y QUE NO SON DE LA OPERACION.** La
> **junta asesora** declara 4 miembros y **resueltos colapsan a 2**: su "6 de 6"
> era sobre ids que hoy son el mismo nodo escrito de dos maneras. Y el **sales
> roadmap** declara **15 de 15** citando `LD-66` a `LD-70`, **lecturas dirigidas
> que no viven en el fichero de veredictos**, asi que contra ese fichero la
> cobertura re medida es **10 de 15**. **Las dos van como DISCUTIBLES, no como
> veredicto.**

**LAS OTRAS CINCO** (tecnologias disruptivas, pass/fail, pensamiento visual,
estrategia de innovacion de producto, `project_close_out`) **solo existen como
prosa**: el barrido de las ocho contra el inventario entero esta impreso
entero en `docs/loop/SALIDA_V165_T6_OP_L_01.txt`, seccion F, y para esas cinco
imprime `SIN ENTRADA CON MIEMBROS en el inventario`. **Elegirles una seria
DECIDIR, no medir.**

**`OP-L-01` NO SE CIERRA Y SU ESTADO NO SE TOCA: sigue en `LISTA`.** **Cero nodos
tocados, cero aristas movidas.**

**CASO POSITIVO POR MUTACION: 14 casos pasan y los 14 CAEN**
(`SALIDA_V165_T6_MUTACION_OP_L_01.txt`). Prueba sobre sujeto fabricado que **la
comparacion literal NO ve lo que la resuelta SI** (que es lo que sostiene el
hallazgo) y que **las dos lecturas de la clausula 2 no pueden ser ciertas a la
vez**, con las dos cifras computadas.

## 7. LAS CONSTANCIAS DEL CIERRE, CADA UNA CON SU FICHERO

**LA BATERIA SE CORRIO SOLA, Y SU PROPIA GUARDA LO CONFIRMA**
(`docs/loop/SALIDA_V165_BATERIA.txt`), que es lo que la CAIDA 3 del auditor
ensena:

| medida | cifra |
|---|---|
| veredicto | **VERDE, exit 0** |
| entradas en la nomina | **62** |
| arneses que el censo reconoce | **124** |
| entradas de la nomina que el censo NO VE | **0** (al abrir y recomputado al cierre) |
| arneses posteriores que se quedan FUERA | **0** (al abrir y recomputado al cierre) |
| `ANCLA PERDIDA` / `NO MORDIO` / `NO REPRODUCIBLE` | **0 / 0 / 0** |
| `CASO DECLARADO` | **2** (`vuelta135_2e_mutacion_3.py`, `vuelta140_2a_mutaciones.py`) |
| **`RUIDO DE CONCURRENCIA`** (`docs/loop/SALIDA_V165_BATERIA.txt`) | **0**, ninguno |
| tiempo total | **1.156,2s, 19,3 minutos** |
| el mas lento | `vuelta159_tarea6c_mutacion_exencion.py`, 426,2s |
| arneses que pasan de 30 segundos | **6** |

**EL ESTADO DE LAS ONCE FASES, TALLADO UNA POR UNA CON
`scripts/loop/tallar_estado_de_fase.py --fase` Y SUMADO DEL FICHERO**
(`docs/loop/SALIDA_V165_T7_FASES.txt`):

**LA TABLA VA UNA FILA POR FASE Y CADA FILA CITA SU PROPIO FICHERO**, que es la
unica forma en que la vara de cifras puede cotejarla:

| fase | catalogo / cumplidas / sin cumplir | fichero |
|---|---:|---|
| `00_CODIGO` | 7 / 0 / 7 | `docs/loop/SALIDA_V165_T7_FASE_00.txt` |
| `01_FUENTES` | 7 / 0 / 7 | `docs/loop/SALIDA_V165_T7_FASE_01.txt` |
| `02_DESTEJIDOS` | 9 / 2 / 7 | `docs/loop/SALIDA_V165_T7_FASE_02.txt` |
| `03_FUSIONES` | 16 / 12 / 4 | `docs/loop/SALIDA_V165_T7_FASE_03.txt` |
| `04_ENLACES` | 10 / 5 / 5 | `docs/loop/SALIDA_V165_T7_FASE_04.txt` |
| `05_SANEO` | 10 / 1 / 9 | `docs/loop/SALIDA_V165_T7_FASE_05.txt` |
| `06_MESAS` | 16 / 16 / 0 | `docs/loop/SALIDA_V165_T7_FASE_06.txt` |
| `07_ADUANA` | 2 / 0 / 2 | `docs/loop/SALIDA_V165_T7_FASE_07.txt` |
| `08_VERIFICACION` | 1 / 0 / 1 | `docs/loop/SALIDA_V165_T7_FASE_08.txt` |
| `09_LECTURAS_DIRIGIDAS` | 3 / 0 / 3 | `docs/loop/SALIDA_V165_T7_FASE_09.txt` |
| `10_INVENTARIO` | 1 / 0 / 1 | `docs/loop/SALIDA_V165_T7_FASE_10.txt` |

**LA SUMA NO SE TECLEA: LA CUENTA
`scripts/loop/vuelta165_tarea7_sumar_fases.py` LEYENDO
`docs/loop/SALIDA_V165_T7_FASES.txt`** y apendandole sus lineas `CIFRA`, porque
las once corridas imprimen su fase y ninguna imprime el total:

  - `CIFRA fases sumadas: 11`
  - `CIFRA operaciones del catalogo: 82`
  - `CIFRA con destino cumplido: 36`
  - `CIFRA sin cumplir: 46`
  - `CIFRA sin vara escrita: 44`
  - `CIFRA consumidas con superviviente divergente: 2`
  - `COMPROBACION: cumplidas mas sin cumplir es 82, y el catalogo es 82: CUADRA`

> **Reproduce al digito contra la suma que el auditor publico en la 164**, y **se
> vuelve a decir lo que esa suma ya decia:** `08_VERIFICACION` sale **1 del
> catalogo, 0 con destino cumplido, 1 sin cumplir y esa 1 SIN VARA ESCRITA**,
> aunque el `estado` de `OP-V-01` sea `HECHA`. **No es una contradiccion y no la
> arreglo:** esta vara mide el destino contra el grafo, y el barrido entero de
> `08_VERIFICACION` en `docs/loop/SALIDA_V165_T7_FASES.txt` imprime
> `sin vara escrita: 1`, o sea que `OP-V-01` **carece de destino medible contra
> el grafo**, que es lo que el propio auditor dejo escrito en su seccion 8. **Su
> cierre es una declaracion del fundador, y ningun instrumento de esta casa lo
> confirma ni lo desmiente.**

**Y UNA VARA MAS SALE EN EXITCODE 1 Y NO LA ESCONDO, AUNQUE NO SEA DE ESTA
VUELTA.** `tallar_cifras_de_antes.py --fichero docs/loop/REPORTE.md` da
**exitcode 1** sobre el reporte de la 165. **Antes de decir nada la corri sobre
el reporte de la 164**, sacado de su propio commit `c59d111a`, y da **exitcode 1
tambien**:

| sujeto | exitcode | hallazgos | fichero |
|---|---:|---:|---|
| reporte de la 164 (`c59d111a`) | 1 | 36 | `docs/loop/SALIDA_V165_T7_CIFRAS_DE_ANTES_164.txt` |
| reporte de la 165 (este) | 1 | 23 | `docs/loop/SALIDA_V165_T7_CIFRAS_DE_ANTES_165.txt` |

> **Asi que NO es una regresion de esta vuelta y no la arreglo por cuenta
> propia.** Su vara pide una cita de fichero detras de cada oracion que hable en
> pasado, y su vocabulario dispara con palabras corrientes (`antes`, `era`,
> `sigue`, `hoy`), asi que sobre un reporte de fase 04 marca prosa que no es
> ninguna cifra de antes. **Lo que me importa decir es lo otro: llevaba al menos
> dos vueltas en rojo y ningun reporte lo nombraba.** Va como PREGUNTA 3.

**RE SELLADO DECLARADO, PORQUE NO SE PROHIBE RE SELLAR SINO RE SELLAR EN
SILENCIO.** La corrida de los 41 de la TAREA 4 reescribio **cinco** salidas
selladas. **Sus lineas van talladas por `verificar_re_sellado.py` y no
tecleadas:**

<!-- RE SELLADO DECLARADO -->
  - `RE SELLADO DECLARADO: SALIDA_V118_TAREA2_6_MUTACION_DD_ANTES.txt numstat +15/-32, lineas CIFRA con valor cambiado: 0 (ninguna)`
  - `RE SELLADO DECLARADO: SALIDA_V118_TAREA2_6_MUTACION_DD_DESPUES.txt numstat +15/-32, lineas CIFRA con valor cambiado: 0 (ninguna)`
  - `RE SELLADO DECLARADO: SALIDA_V135_4C_MUTACION.txt numstat +2/-1, lineas CIFRA con valor cambiado: 0 (ninguna)`
  - `RE SELLADO DECLARADO: SALIDA_V137_1A_MUTACION.txt numstat +3/-3, lineas CIFRA con valor cambiado: 0 (ninguna)`
  - `RE SELLADO DECLARADO: SALIDA_V137_1C_MUTACION.txt numstat +23/-26, lineas CIFRA con valor cambiado: 0 (ninguna)`
  - `RE SELLADO DECLARADO: SALIDA_V165_T2_CENSO_ANTES_DESPUES.txt numstat +48/-53, lineas CIFRA con valor cambiado: 8 (CIFRA de esas entradas VISIBLES al censo nuevo, CIFRA de esas entradas VISIBLES al censo viejo, CIFRA entradas en la nomina, CIFRA entradas en la nomina antes y despues del arreglo, CIFRA fuera de la nomina, CIFRA pre 148 fuera de la nomina (patron viejo), CIFRA vistos por el censo NUEVO, CIFRA vistos por el censo VIEJO)`
  - `RE SELLADO DECLARADO: SALIDA_V165_T4_MUTACION_SUJETO.txt numstat +19/-3, lineas CIFRA con valor cambiado: 2 (CIFRA casos, CIFRA casos que caen al mutar el esperado)`
  - `RE SELLADO DECLARADO: SALIDA_V165_T5_ESTADO_NUEVO.txt numstat +31/-1, lineas CIFRA con valor cambiado: 3 (CIFRA ficheros del universo, CIFRA ficheros que solo lo nombran, sin serlo, CIFRA sedes del indice halladas por nombre)`

**Y TRES DE LAS OCHO SON SALIDAS DE ESTA MISMA VUELTA, RE CORRIDAS
DESPUES DEL COMMIT DE SU TAREA, Y SE DECLARAN IGUAL.**
`SALIDA_V165_T2_CENSO_ANTES_DESPUES.txt` se re corrio cada vez que la
nomina crecio, y por eso mueve OCHO lineas `CIFRA`;
`SALIDA_V165_T4_MUTACION_SUJETO.txt` se re corrio al anadirle el bloque
`C2` de la transitividad, y mueve DOS; y `SALIDA_V165_T5_ESTADO_NUEVO.txt`
se re corrio cuando su instrumento gano el `BARRIDO EXHAUSTIVO` que la vara
de ausencias pedia, y mueve TRES. **Nacer no es re sellar, pero re correr si
lo es, y la guarda no distingue de quien es la mano.**
<!-- FIN RE SELLADO DECLARADO -->

> **Y LO QUE ESAS CINCO ENSENAN, QUE ES MAS QUE SU NUMSTAT.** Las de la 118 y la
> `137_1C` cambian **porque el archivo cambio**: `OP-E-04` y `OP-E-05` pasaron a
> `HECHA`. Las de `V135_4C` y `V137_1A` cambian **SOLO en el nombre aleatorio de
> un directorio temporal**, o sea que **esas dos salidas selladas no son
> reproducibles por construccion**. Ninguna de las dos entra en la nomina, asi
> que la bateria no las ve, **pero queda dicho**.

**LAS CONSTANCIAS DEL CICLO, CADA CELDA CON EL FICHERO DEL QUE SALE:**

| constancia | apertura | cierre | fichero |
|---|---|---|---|
| Gate 0 | **GATE 0 OK, exit 0** | **GATE 0 OK, exit 0** | `SALIDA_V165_GATE0_CMD1_APERTURA.txt` y `SALIDA_V165_GATE0_CMD1_CIERRE.txt` |
| motor | **25/25** | **25/25** | `SALIDA_V165_MOTOR_APERTURA.txt` y `SALIDA_V165_MOTOR_CIERRE.txt` |
| `tsc` | exitcode 0, cero lineas | exitcode 0, cero lineas | `SALIDA_V165_TSC_APERTURA.txt` y `SALIDA_V165_TSC_CIERRE.txt` |
| web | 82 y 1.040 | 82 y 1.040 | `SALIDA_V165_WEB_APERTURA.txt` y `SALIDA_V165_WEB_CIERRE.txt` |
| censo y aristas | 3.853 / 3.169 / 684 y 8.780 / 8.740 / 17.520 / 9.914 | **identicos**, cero aristas movidas | `SALIDA_V165_CONTEO_APERTURA.txt` y `SALIDA_V165_CONTEO_CIERRE.txt` |
| desfase del calibrado | cuatro | **las mismas cuatro** | `SALIDA_V165_DESFASE_CALIBRADO_APERTURA.txt` y su gemela |
| `numstat` de `dataset/ web/ engine/` | cero filas | cero filas | `SALIDA_V165_CICLO_NUMSTAT_APERTURA.txt` y `SALIDA_V165_CICLO_NUMSTAT_CIERRE.txt` |

**LA CABECERA SE COTEJA CON `--comparar` DESPUES DE ESCRIBIR EL REPORTE**, y da
**CABECERA IDENTICA AL TALLADOR**, con nueve filas cotejadas, **0 DISTINTAS,
0 ausentes** y **exitcode 0**
(`docs/loop/SALIDA_V165_T7_CABECERA_COMPARADA.txt`).

## 8. LO QUE SE MOVIO EN ESTA VUELTA Y LO QUE NO

| cosa | apertura | **cierre** | quien lo movio |
|---|---|---|---|
| nodos del grafo | 3.853 / 3.169 / 684 | **igual** | nadie |
| aristas | 8.780 / 8.740 / 17.520 / 9.914 | **igual** | nadie |
| marcador del cribado (filas de `INTRA_DOMINIO_VEREDICTOS.jsonl`) | 3.388 | **3.388** | nadie |
| serie de registros | 25 entradas | **26** | la TAREA 1, `R.34` |
| nomina de la bateria | 53 | **62** | las TAREAS 2, 4 y 6 |
| suites de la web | 82 / 1.040 | **82 / 1.040** | se movio ANTES de esta vuelta, y fuera del bucle |
| `OP-L-01` | `LISTA` | **`LISTA`** | nadie, y a proposito |

**Rutas tocadas:** `docs/PENDIENTES.md` (adicion pura),
`docs/loop/SELLO_SESION_CREDENCIAL_2026-09-03.md` (adicion pura),
`scripts/loop/verificar_mutaciones_viejas.py` (la fuente de la TAREA 2), los
instrumentos y arneses nuevos de la vuelta, las salidas `SALIDA_V165_*` y las
cinco re selladas. **`dataset/` NO se toco: el `numstat` da cero filas.**

## 9. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

  - **DISCUTIBLE 1. ENSANCHAR EL PATRON A TRES FAMILIAS Y NO ESTRECHAR SOLO LA
    FRASE.** La 6.3 admitia las dos salidas y **tome las dos**, pero el ensanche
    **cambia una cifra publicada**: el censo pasa de ver 92 a ver 122 sobre el
    mismo arbol. **Si el auditor cree que la 6.3 pedia elegir UNA**, la que
    sobra es el ensanche, porque el invariante de
    `nomina_invisible_al_censo()` es el que de verdad cierra el agujero y el
    ensanche solo mueve la frontera. **Lo marco yo.**
  - **DISCUTIBLE 2. LA TRANSITIVIDAD PUEDE SER DEMASIADO ANCHA.** Sigue literales
    de ruta y `import`, y no distingue una linea que se ejecuta de una que no.
    **Su error es conservador** (deja fuera, no mete dentro), pero **dejar fuera
    en bloque es lo que la 6.5 prohibe**. De 17 congelados a 5 hay 12 arneses
    cuya exclusion depende de una cadena que **no comprobe uno por uno**.
    **Marcado.**
  - **DISCUTIBLE 3. REGISTRAR TRES CAIDAS CUANDO LA TAREA 1 PEDIA DOS.** Conte la
    seccion en vez de elegir cifra, y registrar de mas es **inventar registro**
    tanto como registrar de menos es perderlo. **Si el auditor queria dos, sobra
    una.** **Marcado.**
  - **DISCUTIBLE 4. LA COBERTURA RE MEDIDA DE LA JUNTA ASESORA, `1 de 1`.** Sale
    de resolver los cuatro miembros del racimo a dos nodos
    (`docs/loop/SALIDA_V165_T6_OP_L_01.txt`, seccion F). **Puede ser que el racimo
    este declarado sobre ids que a proposito NO se resuelven**, y entonces mi
    `1 de 1` estaria midiendo otra cosa que el `6 de 6` del inventario. **No lo
    se y no lo decido.** **Marcado.**
  - **DISCUTIBLE 5. HABER MEDIDO LA CLAUSULA 1 CON EL RESOLUTOR PUESTO.** `P.1`
    dice **sin excepcion**, y por eso lo hice; pero la clausula se escribio el
    11 ago 2026 y **puede que quien la escribio quisiera decir "no aparece este
    par de ids"** y no "no aparece esta pareja de nodos". **Si es asi, la
    clausula 1 se cumple y mi hallazgo es de otra cosa.** **Marcado, y es el que
    mas me interesa que releas.**

## 10. PREGUNTAS, Y NO SON DOCTRINA NUEVA

  1. **LOS 26 QUE EL ENSANCHE HACE VISIBLES.** Son pre 148, estan fuera de la
     nomina y **nadie los ha adjudicado**. No los mido y no los meto: **la 6.5
     adjudico los 41, no estos**. **Pregunto si su sujeto se mide en la vuelta
     siguiente o si se quedan declarados y quietos.**
  2. **LAS DOS SALIDAS SELLADAS QUE NO SON REPRODUCIBLES POR CONSTRUCCION**
     (`SALIDA_V135_4C_MUTACION.txt` y `SALIDA_V137_1A_MUTACION.txt`, que embeben
     el nombre aleatorio de un temporal). **Hoy no molestan porque sus arneses no
     estan en la nomina.** **Pregunto si eso se arregla o se declara**, sabiendo
     que arreglarlo toca ficheros de vueltas pasadas.

  3. **`tallar_cifras_de_antes.py` LLEVA AL MENOS DOS VUELTAS EN EXITCODE 1 Y
     NINGUN REPORTE LO NOMBRA.** Medido hoy sobre los dos reportes, el de la 164 y el de la 165, con
     su salida sellada cada uno. **No lo arreglo**: o su vocabulario se estrecha,
     o esa vara se declara ajena al reporte de fase 04, y las dos cosas son
     decision de quien tenga la vara, no mia. **Pregunto cual de las dos.**

**PENDIENTES DE DOCTRINA: NINGUNA.** La unica que traia el reporte de la 164
queda **retirada por mi** citando la letra de la propia regla (seccion 4). **Las
dos preguntas del reporte de la 164 (el campo `cita` y `node_modules/`) quedan
CERRADAS por las adjudicaciones 6.7 y 6.8 y este reporte deja de arrastrarlas.**

## 11. LO QUE NO HAGO Y LO DIGO

  - **No toco un solo nodo ni una sola arista.** La vuelta es de codigo, medicion
    y registro.
  - **No cierro `OP-L-01` ni le cambio el estado**, y no toco `OP-L-02`,
    `OP-L-03` ni `OP-I-01`.
  - **No arreglo la clausula 2 de `OP-L-01`**, ni la 1, ni la 3: **eso es del
    fundador o del auditor, no mio**.
  - **No recorto la nomina de la bateria para que corra antes**, aunque roce los
    veinte minutos.
  - **No arreglo la `M` de `master_graph.json` y no la commiteo sola.**
  - **El merge de `pasada-unica` no se pide y no se hace: es del fundador y solo
    suyo.**
