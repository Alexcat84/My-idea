# REPORTE DE LA VUELTA 138

**Rama `pasada-unica`. Fase III, EJECUCION, fase 06 MESAS. Regimen completo: el
modo austero sigue suspendido por su propio punto 5.** Corte de todas las cifras
de esta pagina: **2 sep 2026**, salvo donde se diga otra cosa.

## 0. LA CABECERA, Y LA CELDA QUE NO SALE

**LA IDENTIDAD SE LEE DE GIT, no se teclea.** `git rev-parse HEAD` escrito en el
primer commit de la vuelta y en el cierre:

| | valor | de donde sale |
|---|---|---|
| commit de APERTURA | `732cb930aa3dff3785a3f71a4a79073d3fe2a597` | `SALIDA_V138_HEAD_APERTURA.txt` |
| commit de CIERRE (al correr la bateria) | `fbcb950ce358e715476f5ccded9488cd5f6b0914` | `SALIDA_V138_HEAD_CIERRE.txt` |
| rama | `pasada-unica` | `git rev-parse --abbrev-ref HEAD` |

**LA CABECERA TALLADA NO SALE, Y NO SE TECLEA EN SU LUGAR.**
`tallar_cabecera_reporte.py --vuelta 138 --fase04` da **ROJO EXIT 1**, y su
salida entera esta en `SALIDA_V138_TALLADOR_CABECERA.txt`:

```
  ROJO, 2 celdas no se pudieron leer y NO se talla nada:
     no existe la salida SALIDA_V138_DESFASE_CALIBRADO_APERTURA.txt
     sin texto para desfase APERTURA
```

**POR QUE, y esto no se afirma, se mide.** El camino `--fase04` del tallador lee
**DIEZ** familias de salida y el encargo de esta vuelta nombro **NUEVE**: la que
falta es `DESFASE_CALIBRADO`. El lado de CIERRE se midio y esta
(`SALIDA_V138_DESFASE_CALIBRADO_CIERRE.txt`, **468 filas en el calibrado, 3 filas
de desfase**). El de APERTURA **no puede existir**, y lo probe corriendo la
guarda tres veces sobre el mismo arbol
(`SALIDA_V138_CIERRE_CELDA_QUE_NO_SALE.txt`):

1. `verificar_apertura_sellada.py --vuelta 138` sin el fichero: **VERDE EXIT 0**.
2. Fabrico el fichero midiendo contra el ref de apertura y vuelvo a correrla:
   **ROJO EXIT 1**, `SALIDA_V138_DESFASE_CALIBRADO_APERTURA.txt: ningun commit lo
   anade (no versionado)`.
3. Lo retiro (P.16, quien fabrica limpia) y vuelvo a correrla: **VERDE EXIT 0**.

O sea que la celda que el tallador pide **haria caer en ROJO la guarda que la
TAREA 1.d exige en VERDE**, porque ese fichero no nacio en el primer commit de la
vuelta y no puede nacer alli a posteriori. **La celda no sale de un instrumento,
y por tanto no se escribe.** Es la misma figura de la caida 4.4 del acta 137, y
la dejo apuntada en la seccion 7 como pregunta.

## 1. TAREA 1, EL BLOQUE DE APERTURA. ENTERA.

Los **NUEVE** ficheros `SALIDA_V138_*_APERTURA.txt` en **UN SOLO COMMIT**,
`7e285147`, hijo directo de `732cb930`, el acta de la vuelta 137, y ANTES de la
primera operacion. La bateria se corrio con el arbol limpio
(`git status --porcelain` vacio) y una sola vez, en el orden del encargo.

**LA COMPROBACION, que es la que caza el fallo de la 137 al primer intento.**
Los ficheros de apertura sellados en el primer commit son **9 ficheros**,
contados con `ls | wc -l` en `SALIDA_V138_9_APOYO_CIFRAS.txt`.
Y `verificar_apertura_sellada.py --vuelta 138` da **VERDE EXIT 0** sobre esos
mismos, diciendo que *"nacieron todos en el primer commit de la vuelta (hijo
directo del acta)"*: salida entera en
`SALIDA_V138_TAREA1D_APERTURA_SELLADA.txt`.

## 2. LAS DOS COLUMNAS, CADA CELDA DE SU FICHERO

Cada fila cita el fichero del que sale y se reconstruyo contandolo. El cierre se
midio AL CIERRE, despues de la fusion.

| medida | APERTURA (`732cb930`) | CIERRE (`fbcb950c`) | ficheros |
|---|---|---|---|
| Gate 0, comando 1 | `GATE 0: OK`, EXITCODE 0 | `GATE 0: OK`, EXITCODE 0 | `SALIDA_V138_GATE0_CMD1_APERTURA.txt` / `_CIERRE.txt` |
| etiquetas de cara | 71 etiquetas, EXITCODE 0 | 71 etiquetas, EXITCODE 0 | `SALIDA_V138_CICLO_ETIQUETAS_APERTURA.txt` / `_CIERRE.txt` |
| sync de assets | 6 assets, EXITCODE 0 | 6 assets, EXITCODE 0 | `SALIDA_V138_CICLO_SYNC_APERTURA.txt` / `_CIERRE.txt` |
| numstat del ciclo | VACIO | **1 fichero, y es el log** | `SALIDA_V138_CICLO_NUMSTAT_APERTURA.txt` / `_CIERRE.txt` |
| nodos / vivos / deprecados | 3853 / 3184 / 669 | 3853 / **3183** / **670** | `SALIDA_V138_CONTEO_APERTURA.txt` / `_CIERRE.txt` |
| sig / prev / suma / union | 9198 / 9180 / 18378 / 9833 | **9197** / **9181** / 18378 / **9835** | idem |
| auto aristas / dups en lista | 0 / 0 | 0 / 0 | idem |
| motor | 25 de 25, EXITCODE 0 | 25 de 25, EXITCODE 0 | `SALIDA_V138_MOTOR_APERTURA.txt` / `_CIERRE.txt` |
| vitest | 80 de 80 ficheros, 1030 passed 3 skipped | 80 de 80 ficheros, 1030 passed 3 skipped | `SALIDA_V138_WEB_APERTURA.txt` / `_CIERRE.txt` |
| tsc | EXIT 0, cero lineas | EXIT 0, cero lineas | `SALIDA_V138_TSC_APERTURA.txt` / `_CIERRE.txt` |
| desfase del calibrado | **no existe** (ver seccion 0) | 468 filas, 3 de desfase | `SALIDA_V138_DESFASE_CALIBRADO_CIERRE.txt` |

**EL NUMSTAT DEL CIERRE NO ES VACIO Y NO SE PUBLICA COMO VACIO.** Trae UNA linea,
`1 12 dataset/metadata/phase1_run_log.json`, y leido el diff entero es el LOG de
la corrida: la corrida anterior simetrizo dos aristas de
`fase_acclimate_experiencia_cliente` (que ya se escribieron y se commitearon) y
esta ya no tiene nada que simetrizar, asi que `symmetrize_added` pasa de dos
entradas a la lista vacia. **Ni un nodo ni el `master_graph.json` aparecen en el
numstat.** Es el ciclo llegando a su punto fijo, no un cambio de dato.

**EL VIVO QUE FALTA Y EL DEPRECADO QUE SOBRA SON EL MISMO NODO:**
`fase_acclimate_mapa_de_proceso`, que murio en la fusion de la seccion 5.

## 3. TAREA 2.a, EL REPARTO POR ABSORBIDO. ENTERA, CON SUS CINCO GUARDAS.

Commit `7078f902`. El defecto que se repara:
`marcar(spec["pasos"], ...)` corria dentro de `for ab in absorbidos` con el MISMO
`spec`, y `spec["pasos"]` se indexaba por NUMERO DE PASO y nunca por el par, asi
que el paso 1 de dos absorbidos distintos leia LA MISMA marca.

**(i) EL CASO POSITIVO, `SALIDA_V138_2A_CASO_POSITIVO.txt`.** Los TRES planes de
las vueltas 63 y 64, regenerados con el generador de HOY:

| plan | veredicto |
|---|---|
| `PLAN_V63_OPM02PROG.json` | IDENTICOS salvo la fecha, declarada |
| `PLAN_V63_OPM03I.json` | IDENTICOS salvo la fecha, declarada |
| `PLAN_V64_OPM03II.json` | IDENTICOS salvo la fecha, declarada |

**DOS COSAS QUE NO SABIA Y QUE MEDI, y las dos cambian el metodo, no el
resultado.** PRIMERA: **no se puede regenerar contra el arbol de hoy**, porque los
tres absorbidos estan DEPRECADOS desde las vueltas 63 y 64 y el generador cae en
ROJO con toda la razon. Se regenera en un `git worktree` sobre el **PADRE** del
commit del sellado, y el worktree se retira siempre (P.16). SEGUNDA, y es la que
importa: **la vara no puede ser el fichero de hoy, porque DOS de los tres se
editaron DESPUES de sellarse**, y `git log` lo dice:
`PLAN_V63_OPM02PROG.json` en `be69bc56` deriva **14 lineas** y
`PLAN_V64_OPM03II.json` en `ca74f202` deriva **1 lineas**, las dos contadas en
`SALIDA_V138_9_APOYO_CIFRAS.txt`; `PLAN_V63_OPM03I.json` intacto. La comparacion va contra el
blob del commit del sellado, y **la deriva del fichero de hoy se mide y se imprime
con su commit** en vez de callarse.

**LA UNICA DIFERENCIA TOLERADA, declarada:** la linea `"fecha"`, que el generador
computa con `datetime.date.today()` y que NO se parchea ni se fija por bandera.

**LAS MUTACIONES, `SALIDA_V138_2A_MUTACION_CASO_POSITIVO.txt`,** sobre la variable
COMPUTADA `distintas` y nunca sobre un literal:

| mutacion | esperado | medido |
|---|---|---|
| `--mutar-rotulo` | CAE | CAE, 3 de 3 en ROJO, EXIT 0 |
| `--mutar-marca` | CAE | CAE, 3 de 3 en ROJO, EXIT 0 |
| `--mutar-fecha` | **NO cae** (borde de la tolerancia) | NO cae, VERDE, EXIT 0 |

Las tres juntas acotan la tolerancia por los dos lados: una linea dentro y dos
fuera. Si `--mutar-fecha` cayera, la tolerancia estaria mal escrita; si las otras
dos no cayeran, se habria comido lineas que no le tocan.

**(ii) A (v), `SALIDA_V138_2A_GUARDAS_II_III_IV_V.txt`, SIETE guardas en verde:**

| guarda | medido |
|---|---|
| (ii) dos absorbidos, marcas DISTINTAS para el paso 1 | `APPEND` contra `CUBIERTO:2`, distintas |
| (ii) su mutacion, el mismo sujeto por el reparto VIEJO | CAE, 3 colisiones |
| (iii) falta la marca de un par: ROJO NOMBRANDO EL PAR | `FALTA EL PAR (v138_ab_dos_fixture, 1)` |
| (iii) su mutacion, se devuelve la marca | CAE, EXIT 0 y ningun `FALTA EL PAR` |
| (iv) el fallo viejo EXHIBIDO con `--reparto-viejo` | 3 colisiones, con su tabla |
| (iv) su mutacion, el mismo spec plano SIN la bandera | CAE, ROJO nombrando los DOS absorbidos, sin escribir plan |
| (v) cero escritura si hay fallos | NINGUN fichero tras el ROJO |

**SOBRE QUE SUJETO, y por que no sobre `OP-M-03-III`:** sobre un banco propio y
CONGELADO (tres nodos y una ficha sinteticos en un directorio temporal; ningun id
pisa el catalogo, y se comprueba antes de empezar). Usar `OP-M-03-III`, que es la
ficha real con dos absorbidos, habria dejado la guarda envejecida en cuanto esa
mesa se funda: es la leccion de banco 9.10 aplicada del lado del sujeto.

**UN FLAKE CAZADO Y ARREGLADO, NO REINTENTADO.** La segunda corrida de
`vuelta138_2a_mutaciones.py` cayo con `ModuleNotFoundError` sobre su PROPIO
sujeto: el buscador de modulos de Python cachea el listado del directorio por su
mtime, y un modulo escrito despues del primer `__import__` quedaba invisible. Se
anadio `importlib.invalidate_caches()`. **Cinco corridas seguidas en verde.** Una
guarda que a veces no encuentra su sujeto no es una guarda, y el fallo
intermitente es la peor especie.

**EL CICLO DE GATE 0 CON LAS SUITES DETRAS, `SALIDA_V138_2A_CICLO_GATE0.txt`:**
Gate 0 OK exit 0, etiquetas 71, sync 6 assets, numstat VACIO, motor 25 de 25,
vitest 80 de 80 y 1030 passed 3 skipped, tsc EXIT 0.

## 4. TAREA 2.b, EL RE-ANCLAJE. ENTERA.

Commit `b61d8abd`. **EL SUJETO NUEVO:**
`docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md`, el `REPORTE.md` de la vuelta 134
copiado del blob del acta 134 (`e12e4c36`), byte a byte. **NO es
`docs/loop/REPORTE.md`, que es lo que se sobreescribe cada vuelta y era el ancla
que se perdio.** Las tres mutaciones cotejan en CADA corrida el sha256 normalizado
del sujeto contra el del blob leido de git, y caen en ROJO nombrandolo si alguien
lo toca. sha256 comprobado hoy:
`d1f97a510f17e35046eeec4975e1e0a1adabcfdda5a4646a250aa6db97d61fdd`.

**LA GUARDA PARA QUE NO VUELVA A PASAR:**
`scripts/loop/verificar_mutaciones_viejas.py`, nombre estable, entra en el ciclo
de cierre de cada vuelta. **ANCLA PERDIDA cuenta como ROJO**, que es justo lo que
la mutacion D de la vuelta 137 hacia bien en NO contar cuando todavia estaban
desancladas. `SALIDA_V138_2B_MUTACIONES_VIEJAS.txt`:

| corrida | medido |
|---|---|
| sin mutar | las 4 en OK, ANCLA PERDIDA 0, NO MORDIO 0, VERDE |
| `--mutar-ancla` | las 3 re-ancladas caen como ANCLA PERDIDA, VERDE de la mutacion |

**CORRIDA OTRA VEZ EN EL CIERRE DE ESTA MISMA VUELTA**
(`SALIDA_V138_CIERRE_MUTACIONES_VIEJAS.txt`): **VERDE, las 4 corren y muerden**,
ANCLA PERDIDA 0.

## 5. TAREA 3, LA FASE 06. UNA FUSION DE SEIS, Y EL MOTIVO DE LAS CINCO CONTADO

### 5.1 LA LECTURA DE ACTO POR P.5, LAS SEIS, PAR A PAR

Instrumento nuevo, `scripts/loop/vuelta138_p5_lectura_de_acto.py`. Enumera los
pares internos del acto y busca cada uno en `INTRA_DOMINIO_VEREDICTOS.jsonl` y en
las lecturas dirigidas de `docs/plan/`. **No decide una clase, no redacta un
veredicto y no inventa un par.** `SALIDA_V138_3_P5_LAS_SEIS.txt`:

| operacion | pares | leidos | sin leer | clases |
|---|---|---|---|---|
| OP-M-01-FUSION | 10 | 10 | 0 | A 10 |
| OP-M-02-ACCLIMATE | 1 | 1 | 0 | A 1 |
| OP-M-03-III | 3 | 2 | **1** | A 2 |
| OP-M-05-INDICE | 3 | 3 | 0 | A 3 |
| OP-M-05-EDIFICIO | 3 | 3 | 0 | A 3 |
| OP-M-05-APERTURA | 3 | 3 | 0 | A 3 |

**LA DECLARACION DE `OP-M-01-FUSION` QUEDA VERIFICADA Y NO SE REPITE LA LECTURA,
que es lo que el encargo pide.** La ficha dice "P.5 SATISFECHA POR CONSTRUCCION:
los diez pares del acto estan leidos y los diez en A". Medido: **10 pares
posibles, 10 leidos, 10 en A**, las tres cifras contadas en
`SALIDA_V138_3_P5_LAS_SEIS.txt`. Las fuentes son exactamente las que la ficha
cita: puestos **1038, 801, 356, 745, 765 y 1524** del cribado, mas **LD-58,
LD-60, LD-61 y LD-64**. Seis mas cuatro son diez. **La declaracion es cierta.**

**Y EL UNICO SIN LEER ES EL QUE LA FICHA Y EL ENCARGO AVISABAN:**
`pivote_estrategico` contra `pivotes_e_iteraciones`.

### 5.2 LA LECTURA QUE FALTABA, HECHA. `docs/plan/LD_ACTO_III_DEL_PIVOTE.md`

Trabajo propio y obligatorio ANTES de fundir, por la letra de P.5. **Veredicto:
`LD-138-01`, A. REPITE.** El eje se repite entero (decidir sobre evidencia que
cambia el rumbo del modelo) y los pasos se emparejan: el 1 de
`pivote_estrategico` con el 6 y el 4 del otro, el 4 con el 2, el 2 con el 3. Lo
propio son **DOS y DOS** piezas (desechar lo construido y comunicar el pivote, de
uno; distinguir ajuste de cambio y documentar la version nueva del lienzo, del
otro), y ninguna de las cuatro es un ejercicio que alguien haria otro dia con otro
proposito. **Son PIEZAS, no una segunda familia: el acto es UNA familia y no dos
pegadas por un puente**, que es la pregunta que P.5 existe para responder. La
frontera del 1298 no se toca: esa pieza es del tercero.

**LECTURA DIRIGIDA: no entra en la cola y NO MUEVE EL MARCADOR** (banco 9.6.1).

**EL ROJO Y EL VERDE DEL MISMO INSTRUMENTO SOBRE EL MISMO SUJETO REAL, y por eso
no hace falta fabricar ningun caso:** antes de escribir la lectura,
`vuelta138_p5_lectura_de_acto.py --id-op OP-M-03-III` daba **3 pares, 2 leidos, 1
SIN LEER, EXIT 1**, y ese estado rojo esta congelado en
`SALIDA_V138_3_P5_LAS_SEIS.txt`, que se genero antes de escribir la lectura;
despues, **3 de 3, EXIT 0**.

### 5.3 `OP-M-02-ACCLIMATE`, FUNDIDA. Commit `4b981c04`

`fase_acclimate_experiencia_cliente` absorbe `fase_acclimate_mapa_de_proceso`,
tal como la ficha lo escribe. **Es la unica de las seis con un solo absorbido, y
la primera de la campana sellada con el reparto POR PAR** de la 2.a.

**SIMULACION PREVIA SOBRE COPIA EN MEMORIA (P.7),
`SALIDA_V138_3_SIM_OPM02ACCLIMATE.txt`:** 4 entradas se redirigen, **0 auto
aristas**, el acto queda sin aristas internas.

**GUARDAS DEL FUNDIDOR, `SALIDA_V138_3_FUNDIR_EJEC_OPM02ACCLIMATE.txt`:**

| guarda | medido |
|---|---|
| A, cero auto aristas nuevas | OK (0) |
| B, cero duplicadas nuevas tras resolver | OK (0), y P.16 BAJA el pasivo historico de 875 a 874 |
| C, los cinco campos que no se redactan, intactos | 5 de 5 |
| D, el absorbido conserva su texto INTACTO | OK |
| tabla de perdidas, pieza por pieza | 9 filas: 4 viajan enteras, 5 ya estaban dichas |
| perdidas selladas en campo propio | 3, las tres de matiz y ninguna de gesto |

**LA PIEZA QUE LA FICHA MANDA PRESERVAR SE COMPRUEBA POR SU NOMBRE:** el mapa
visual del proceso es hoy el **paso 6** del superviviente. `ids_alias` del
superviviente: `['fase_acclimate_mapa_de_proceso']`, como la ficha pide.

**EL CICLO DE GATE 0 CON LAS SUITES DETRAS,
`SALIDA_V138_3_CICLO_TRAS_OPM02ACCLIMATE.txt`:** Gate 0 OK, etiquetas 71, sync 6
assets, motor 25 de 25, vitest 80 de 80 y 1030 passed 3 skipped, tsc EXIT 0, y el
censo recomputado que ya esta en la tabla de la seccion 2.

### 5.4 LAS CINCO QUE NO SE FUNDEN, Y EL MOTIVO CONTADO, NO OPINADO

**EL HUECO DEL CONTRATO DE MARCAS.** El contrato tiene cuatro destinos para una
pieza del que muere (`APPEND`, `CUBIERTO:n`, `CUBIERTO_COND:n`,
`INCISO:n|trozo|nexo`) y **los cuatro miran AL SUPERVIVIENTE**, validados contra
los pasos que el superviviente tiene ANTES de la fusion. **No hay ningun destino
que diga "esta pieza ya viaja en este mismo acto, por otro absorbido".** Con un
solo absorbido no hace falta, y las tres fusiones de mesa ya ejecutadas tienen uno
cada una: por eso nadie lo echo de menos.

**DONDE MUERDE, medido en dos sitios distintos:**

- **`OP-M-01-FUSION`**, por instrumento
  (`SALIDA_V138_3_PIEZA_DE_VARIOS_DUENOS.txt`). Su ficha trae una linea de
  `preservar` que dice literalmente *"VIAJA, de `requisitos_gates_con_dientes` y
  `estructura_gates` y `estructura_de_gates`: LOS ENTREGABLES CLAROS Y
  ESTANDARIZADOS con sus plantillas. El superviviente NO los tiene y los tres que
  mueren si"*. **La propia ficha declara las dos mitades del hueco: TRES duenos, y
  el superviviente no la tiene.**
- **`OP-M-03-III`**, a mano y con los dos textos delante
  (`SALIDA_V138_3_OPM03III_EL_HUECO_MUERDE.txt`). El **paso 2 de
  `pivote_startup`** ("Identifica que parte de tu modelo de negocio necesita
  cambiar") y el **paso 3 de `pivotes_e_iteraciones`** ("Usa tu lienzo de modelo
  de negocio para ubicar que parte necesita el cambio") son **el mismo gesto**, y
  el superviviente no lo tiene: `pivote_estrategico` FORMULA la hipotesis nueva,
  que es el nombre que se le pone al resultado, no el barrido previo entre las
  nueve casillas.

**LAS CUATRO SALIDAS FALLAN LAS CUATRO:** `APPEND` en los dos deja al
superviviente con el mismo gesto dos veces; `CUBIERTO` afirma del superviviente
algo que el superviviente no dice, que es exactamente la mentira callada que la
casa persigue; `CUBIERTO_COND` lo mismo contra una condicion; y el `INCISO` al
paso que ya viaja **lo prohibe la guarda del generador**, porque ese paso todavia
no existe cuando el plan se sella.

**LO QUE HAGO, por EJECUTOR regla 5 y no por gusto:** no paro la vuelta, registro
lo mejor sostenido y lo marco **PENDIENTE DE DOCTRINA**. Y **no fundo**: la fusion
es irreversible por definicion ("una vez fundido, el acto es un nodo y la pregunta
de si eran una familia o dos se vuelve irrespondible"), y no se hace una cosa
irreversible sobre una regla que no existe.

**UNA CORRECCION DECLARADA DENTRO DE LA MISMA VUELTA, sin borrar el texto viejo.**
La primera version de
`scripts/loop/vuelta138_3_pieza_de_varios_duenos.py` solo miraba la cabeza de las
lineas que empiezan por `VIAJA, de ` y **SUB-CONTABA**: publicaba UNA sola pieza en
el hueco. Corregida a la linea entera, son **DOS** las operaciones con una linea
que nombra dos o mas absorbidos. Mutacion sobre la cifra computada,
`--mutar-umbral` de 2 duenos a 1: la cuenta pasa de **2 lineas a 20** y de **2
operaciones a 4**, o sea que sale del texto de las fichas y no de una tabla a mano.
Las dos cifras estan en `SALIDA_V138_3_PIEZA_DE_VARIOS_DUENOS.txt`.

**Y EL LIMITE QUE QUEDA, DICHO EN VEZ DE CALLADO.** Segun
`SALIDA_V138_3_PIEZA_DE_VARIOS_DUENOS.txt` hay **7 lineas** de
`preservar` que no nombran ningun id (dicen "los dos indices", por ejemplo) y que
**ningun contador de ids puede ver**. El cero que ese instrumento sostiene es
"cero lineas que NOMBREN dos absorbidos", **nunca "cero piezas de varios
duenos"**. Por eso:

**LAS TRES DE `OP-M-05` NO SE DECLARAN LIMPIAS.** `OP-M-05-INDICE`,
`OP-M-05-EDIFICIO` y `OP-M-05-APERTURA` **no se leyeron a mano** buscando el
hueco, y una busqueda negativa no se puede citar (EJECUTOR regla 9). Quedan por
mirar, y lo digo aqui en vez de dejar que la tabla parezca un verde.

**CIFRAS DE LA FASE 06, todas de `SALIDA_V138_3_PIEZA_DE_VARIOS_DUENOS.txt` y
`SALIDA_V138_3_OPM03III_EL_HUECO_MUERDE.txt`:**

| medida | cifra |
|---|---|
| fusiones de la fase 06 | 6 grupos |
| fundidas en esta vuelta | 1 grupo |
| con dos o mas absorbidos, donde el hueco PUEDE morder | 5 grupos |
| leidas a mano en esta vuelta buscando el hueco | 2 grupos |
| donde el hueco MUERDE, comprobado | 2 grupos |
| lineas de `preservar` que nombran dos o mas absorbidos | 2 lineas |
| lineas de `preservar` sin ningun id, que la maquina NO clasifica | 7 lineas |

**`OP-S-12` sigue al final de la pasada entera**, despues de la ultima fusion, por
la atadura 2 del indice. No se toco.

## 6. TAREA 4, LOS REGISTROS Y LAS DECLARACIONES

**(4.a) R.19 EN `docs/PENDIENTES.md`, POR ADICION.** Commit `199401ce`.
Anade **97 lineas** y borra **0 lineas**, contado en
`SALIDA_V138_9_APOYO_CIFRAS.txt` con `git diff --numstat 199401ce^ 199401ce`. Registra los cuatro
discutibles adjudicados (3.1, 3.2, 3.3 y 3.6), las dos adjudicaciones de
procedimiento (3.4 y 3.5), las **dos caidas del ejecutor** de fuera de lo marcado
(4.1 y 4.2) y las **tres del auditor** (4.4, 4.5 y 4.6), **escritas igual que las
del ejecutor**, que es lo que el encargo pide con esas palabras.

**(4.c) FICHEROS SELLADOS DE OTRA VUELTA QUE ESTA VUELTA REESCRIBE.**
`SALIDA_V138_4C_SELLADOS_REESCRITOS.txt` trae el `git status` y el diff entero.
**UNO solo cambia: `docs/loop/SALIDA_V135_2E_MUTACION_3.txt`**, y su recuento,
contado en `SALIDA_V138_9_APOYO_CIFRAS.txt`, es de **3 lineas**. El
cambio no viene de la reparacion 2.b: viene de que
`verificar_cifras_del_reporte.py`, reparado en la vuelta 137, ahora nombra la
etiqueta `CIFRA` y el camino (`POR ETIQUETA`) al citar el fichero, mas el nombre
aleatorio del temporal. Los `_1` y `_2` salen identicos y git no los marca.

**(4.b) LA CONDICION DEL DISCUTIBLE 1.** Va en la seccion 9, al pie, porque la
cobertura se mide sobre este mismo fichero ya escrito.

## 7. LO QUE NO HICE, Y POR QUE

1. **`OP-M-01-FUSION`, `OP-M-03-III`, `OP-M-05-INDICE`, `OP-M-05-EDIFICIO` y
   `OP-M-05-APERTURA` NO SE FUNDIERON.** Cinco de seis. El motivo de las dos
   primeras esta medido arriba (el hueco muerde); el de las tres ultimas es que la
   vuelta se acabo antes de llegar a leerlas a mano, y **no las declaro limpias**.
   El encargo manda partir por la TAREA 3 y no por las guardas si no cabe todo:
   eso hice, y ninguna guarda se recorto.
2. **No toque el campo `estado` de ninguna ficha.** Por precedente medido: el
   commit `f5e9a72b` de la vuelta 63, que ejecuto `OP-M-03-I`, tampoco toco
   `docs/plan/OPERACIONES.jsonl`. Por eso las dieciseis fichas de fase 03 siguen
   leyendo LISTA. El estado se mide contra el grafo.
3. **No talle la cabecera.** Ver seccion 0: la celda no sale, y esta probado que
   no puede salir sin romper el sello de la apertura.

## 8. DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**DISCUTIBLE 1. NO FUNDIR `OP-M-01-FUSION` NI `OP-M-03-III` POR UN HUECO DE
DOCTRINA, EN VEZ DE FUNDIR CON LA MARCA MENOS MALA.** EJECUTOR regla 5 dice "NO
pares, registra lo mejor sostenido, marcalo PENDIENTE DE DOCTRINA en su razon, y
sigue". Leo "sigue" como "pasa a lo siguiente", no como "funde igual", porque la
fusion es irreversible y P.5 escribe con todas sus letras que despues la pregunta
se vuelve irrespondible. **Si el auditor lee que "lo mejor sostenido" incluia
sellar el plan con la marca menos mala y anotarlo, entonces esto es una caida
mia** y las dos mesas se pierden por mi lectura de la regla.

**DISCUTIBLE 2. LOS TRES `APPEND` DE MAS EN `OP-M-02-ACCLIMATE`.** La ficha
recomputo perdidas por P.13 el 12 ago 2026 y dejo **UNA** sola pieza en
`preservar`, el mapa visual. Leido el nodo entero hoy, **TRES** gestos mas no
estan en el superviviente en ningun grado: detectar las senales silenciosas antes
de la queja, simplificar los procesos complejos, y asignar un responsable por
punto de contacto. Los marque `APPEND` porque marcarlos `CUBIERTO` afirmaria del
superviviente algo que no dice, y porque leo `preservar` como el **suelo** de lo
que no se puede perder y no como el **techo** de lo que puede viajar. **El
superviviente pasa de 5 a 9 pasos, que es mucho crecimiento**, y la divergencia
con una pasada P.13 sellada la declaro en vez de resolverla copiando. Si la vara
es que `preservar` es tambien el techo, esto es una caida mia.

**DISCUTIBLE 3. LA SIMULACION DE HOY CONTRADICE LA VERIFICACION SELLADA DE LA
FICHA DE `OP-M-02-ACCLIMATE`.** La ficha dice "la simulacion fabrica 0
duplicadas" y su nota anade "es ademas la unica de las cinco que NO fabrica
ninguna duplicada". **La simulacion de hoy fabrica DOS**
(`gamificacion_onboarding_visual` en `nodos_previos` y
`ocho_fases_experiencia_cliente` en `nodos_siguientes`). No corregi la ficha ni
copie su cifra: declare la discrepancia y **fundi igual**, porque la propia ficha
manda que las duplicadas queden para `OP-S-12`. **Y hay una segunda lectura que
dejo abierta:** `simular_fusion.py` cuenta DOS duplicadas nuevas y la guarda B del
fundidor cuenta CERO, y no son la misma medida (la segunda cuenta tras resolver
alias y tras la limpieza de P.16, y ademas BAJA el pasivo de 875 a 874). **Publico
las dos cifras y no las promedio ni elijo una.** Si la vara dice que una
discrepancia con la verificacion sellada de una ficha detiene la fusion, esto es
una caida mia.

**DISCUTIBLE 4. EL CABLEADO DE HOY NO ES EL DE LA FICHA, EN LAS DOS QUE MEDI.**
`OP-M-02-ACCLIMATE`: la ficha dice 10 contra 3 y hoy es **11 contra 4**.
`OP-M-03-I` en su dia tuvo el mismo tipo de deriva. **Ninguna cambia el
superviviente** y por eso no pare. Lo marco porque una deriva de cableado
sostenida entre todas las fichas del 12 ago 2026 podria merecer un recomputo de
mesa entero, y eso no lo decido yo.

**DISCUTIBLE 5. ESCRIBI UNA LECTURA DIRIGIDA NUEVA
(`docs/plan/LD_ACTO_III_DEL_PIVOTE.md`) SIN QUE EL ENCARGO NOMBRARA EL FICHERO.**
El encargo dice que la lectura de acto por P.5 es trabajo propio y obligatorio,
pero no dice donde se escribe. Segui la forma de la casa (`LD_*.md` en
`docs/plan/`, con su veredicto, su clase y su aviso de que no mueve el marcador) y
la hice legible por el instrumento de P.5. **Si el sitio correcto era otro, se
mueve, pero la lectura esta hecha y esta entera.**

**DISCUTIBLE 6. EL VEREDICTO `LD-138-01` ES MIO Y NO DE UN INSTRUMENTO.** La clase
A de ese par la decidi yo leyendo los dos nodos: **no hay caso rojo automatico que
la respalde, y lo digo en vez de fabricar uno.** Lo que si es automatico es que el
par **estaba sin leer** (medido, EXIT 1) y que **ahora tiene lectura** (medido,
EXIT 0); la CLASE es juicio.

## 9. PENDIENTES DE DOCTRINA, Y LA COBERTURA

**PENDIENTE DE DOCTRINA 1, EL UNICO, Y ES EL QUE PARA LA FASE 06.** Falta un
destino en el contrato de marcas para la pieza que **DOS O MAS absorbidos del
mismo acto tienen y el superviviente NO**. La pregunta, formulada para que se
pueda contestar con si o con no: **cuando dos absorbidos traen el mismo gesto y el
superviviente no lo tiene, la pieza viaja UNA vez y la segunda se marca como
CUBIERTA POR EL ACTO (marca nueva), o viaja UNA vez y la segunda se declara
PERDIDA en campo propio aunque no se pierda nada, o el generador debe permitir el
`INCISO` a un paso APPENDido dentro de la misma corrida?** Las tres son
sostenibles y no me toca elegir. **Afecta a `OP-M-01-FUSION` y a `OP-M-03-III` con
certeza medida, y a las tres de `OP-M-05` no lo se.**

**PREGUNTA 1 (no es doctrina, es encargo).** El bloque de apertura de la TAREA 1
nombra **NUEVE** ficheros canonicos y el tallador `--fase04` lee **DIEZ**
familias. Falta `DESFASE_CALIBRADO`. **Mientras la lista de nombres no lo incluya,
ninguna vuelta podra tallar su cabecera sin romper el sello de la apertura**, y
esta probado arriba. Es la misma especie que la caida 4.4 del acta 137.

**(4.b) LA COBERTURA, CON SU REPARTO, que es la condicion del DISCUTIBLE 1
adjudicado en el acta 137, 3.1.** Corrida sobre este mismo fichero:

**La corrida completa, con su reparto contado, esta en
`SALIDA_V138_9_COBERTURA.txt`.** El veredicto es **VERDE EXIT 0**, y el reparto
que el acta 137 exige publicar es: **4 cifras** por el camino `POR ETIQUETA` y
**6 cifras** por el camino `POR CONJUNTO`, las dos contadas en ese mismo fichero.

**LAS QUE VAN POR CONJUNTO, NOMBRADAS, que es la condicion entera:**

| cifra | fichero y etiqueta |
|---|---|
| `10 pares` | `SALIDA_V138_3_P5_LAS_SEIS.txt`, etiqueta *pares internos del acto* |
| `3 pares` | `SALIDA_V138_3_P5_LAS_SEIS.txt`, etiqueta *pares internos del acto* |
| `2 lineas` | `SALIDA_V138_3_PIEZA_DE_VARIOS_DUENOS.txt`, etiqueta *lineas de preservar que nombran dos o mas absorbidos* |
| `7 lineas` | `SALIDA_V138_3_PIEZA_DE_VARIOS_DUENOS.txt`, etiqueta *lineas de preservar sin ningun id* |
| `97 lineas` | `SALIDA_V138_9_APOYO_CIFRAS.txt`, etiqueta *lineas anadidas a docs/PENDIENTES.md por R.19* |
| `0 lineas` | `SALIDA_V138_9_APOYO_CIFRAS.txt`, etiqueta *lineas borradas de docs/PENDIENTES.md por R.19* |

**Las dos primeras son el caso exacto que el acta 137 acoto:** el fichero de P.5
trae SEIS lineas `CIFRA pares internos del acto`, una por operacion, y el camino
debil no puede saber cual es cual. **No admite un numero inventado** (las seis
lineas son reales y del mismo fichero), pero si podria emparejar la de una
operacion con la cifra de otra. Aqui las dos cifras publicadas, 10 y 3, son
ademas correctas leyendo el fichero con el ojo: 10 es la de `OP-M-01-FUSION` y 3
la de `OP-M-03-III`.

---

**COMMITS DE ESTA VUELTA (`git log 732cb930..HEAD`, leidos de git):**

- `fbcb950c` VUELTA 138, TAREA 3: LA LECTURA DE ACTO QUE FALTABA, HECHA Y ESCRITA, Y EL HUECO DEL CONTRATO QUE PARA A OP-M-03-III.
- `4b981c04` VUELTA 138, OP-M-02-ACCLIMATE EJECUTADA: LA PRIMERA FUSION DE LA FASE 06, Y LA PRIMERA DE LA CAMPANA SELLADA CON EL REPARTO POR PAR.
- `c3a5b4e1` VUELTA 138, TAREA 3, PASO PREVIO: LA LECTURA DE ACTO POR P.5 DE LAS SEIS, MEDIDA PAR A PAR, Y UN HUECO DEL CONTRATO DE MARCAS QUE APARECE AL SENTAR LA PRIMERA MESA.
- `199401ce` VUELTA 138, TAREA 4.a: R.19, el registro de las adjudicaciones y las caidas del acta 137, POR ADICION.
- `b61d8abd` VUELTA 138, OPERACION 2.b: LAS TRES MUTACIONES SELLADAS, RE-ANCLADAS A UN SUJETO PROPIO Y CONGELADO, Y LA GUARDA QUE IMPIDE QUE VUELVA A PASAR.
- `7078f902` VUELTA 138, OPERACION 2.a: EL REPARTO SE INDEXA POR EL PAR (absorbido, paso), CON SUS CINCO GUARDAS EN VERDE.
- `1afcc05c` VUELTA 138, TAREA 1.d: la guarda de la apertura da VERDE EXIT 0 antes de tocar nada.
- `7e285147` VUELTA 138, TAREA 1: EL BLOQUE DE APERTURA, SELLADO ANTES DE LA PRIMERA OPERACION.
