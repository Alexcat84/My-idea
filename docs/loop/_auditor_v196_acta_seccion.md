
# =========================================================================
# ACTA DEL AUDITOR, VUELTA 196 (6 sep 2026, auditor Opus 5)
# Cubre LA VUELTA 195 ENTERA. Prefijo de mis ficheros: `_auditor_v196_*`.
# HUECO DE ACTA: NINGUNO. La ultima acta escrita es la 195 (linea 68709) y cubre
# la vuelta 194, que es la inmediatamente anterior a la que audito.
# =========================================================================

## 0. LA APERTURA, Y ABRE EN VERDE POR SEGUNDA VUELTA SEGUIDA

**MI PRIMER COMANDO FUE EL SELLO Y NO TOQUE NINGUNO DE LOS TRES PROHIBIDOS ANTES.**
`docs/loop/SELLO_APERTURA_AUDITOR_V196.json` (1412 bytes), con
`prohibidos_antes_del_sello: 0` y `bitacora_antes_del_sello: []` leidos del propio
sello. Corrida entera en `docs/loop/_auditor_v196_apertura.txt`.

**UN ACTO QUE DECLARO EN VEZ DE DEJARLO PASAR:** mi primer comando de todos fue
`--olvidar-turno`, porque `docs/loop/_TURNO_DEL_AUDITOR.json` llegaba con la
bitacora del turno de la 195 (`git log`, `git status`, `REPORTE.md` y dos toques de
veredictos) y `puede_sellar()` habria caido en rojo por toques que no son mios. El
propio fichero llama a eso UN ACTO y por eso va escrito aqui. El sello en disco de
la 195 **no se borro** y sigue en su sitio.

**EL SUJETO: LOS 60 DE LA TANDA DE LA VUELTA 195**, tomados de
`docs/loop/SALIDA_V195_T2_CIEGA.txt`, que es fichero CIEGO POR CONSTRUCCION. Sello
los 60 enteros porque los discutibles marcados del reporte son subconjunto suyo y
**no se pueden aislar sin abrir `REPORTE.md`**, que es uno de los tres prohibidos.
Ciega 80705 bytes, destape 63765 bytes, los dos con su `sha256` en el sello.

**MIS CLASES SE DECLARARON POR LA CUARTA PUERTA ANTES DE ABRIR NADA:**
`--declarar-clases docs/loop/_auditor_v196_mis_clases.txt --vuelta 196` dio VERDE
con **0 destapes apuntados**.

## 1. VERIFICACION DEL REPORTE, RECORRIDA CON MIS PROPIOS COMANDOS

**TODO LO QUE SIGUE LO CORRI YO EN ESTA VUELTA.** Ninguna cifra viene de una nota
vieja ni del reporte que verifico.

| lo que verifico | lo que publica el reporte | lo que me da a mi | |
|---|---|---|---|
| marcador, por `AP.marcador()` | A 551, B 72, C 5, D 2760 sobre 3388 | **identico** | CALZA |
| huecos y duplicados del archivo | cero | **0 huecos, 0 duplicados, 1 a 3388** | CALZA |
| `INTRA_DOMINIO_VEREDICTOS.jsonl` | disco 4054129, LF 4054129, sha LF `0a77b5a35a962621` | **identico** | CALZA |
| censo y aristas, por `vuelta83_conteo_aristas.py HEAD` | 3.853 / 3.169 / 684 y 8.780 / 8.740 / 17.520 / 9.914 | **identico**, auto 0, dup 0 | CALZA |
| Gate 0, ciclo entero corrido por mi | OK, 0 lineas en `dataset/`, `web/`, `engine/` | **OK, y numstat 0 antes y despues** | CALZA |
| motor | 25/25 | **25/25** | CALZA |
| web y `tsc` | 82 (82) / 1.040 (1.040), exitcode 0 | **identico** | CALZA |
| cabecera contra el tallador | 9 filas, 0 distintas, 0 ausentes | **identico** | CALZA |
| nomina al cierre | 135 entradas, `CASOS_DECLARADOS` 2 | **135 y 2**, congelado 133 | CALZA |
| censo de arneses y los que faltan | 195, y 0 fuera de la nomina | **195 y 0**, invisibles 0 | CALZA |
| entradas sin sujeto congelado | 0 | **0**, sujeto vivo 0, no decidible 0 | CALZA |
| los tres arneses | 15/15, 15/15, 17/17 | **identico, y los tres VERDE** | CALZA |
| guiones largos y medios | cero | **0 y 0** | CALZA |
| racha remedida al cierre | 13 ficheros, faltan 181, 182, 183 y 194, racha **1** | **identico, recontado a mano** | CALZA |

**Y LAS RUTAS: 55 citadas en el reporte, contadas por mi.** Las de `REPORTE_V189`
a `REPORTE_V194` existen en `docs/loop/reportes/`; `SALIDA_V195_BATERIA.txt` es el
hueco DECLARADO y medido de la seccion 9, y que no exista es justo lo que declara.
**Queda UNA que no se salva, y es la caida `C.E1` de la seccion 3.**

## 2. LA RELECTURA CIEGA: 56 DE 60, Y LAS CUATRO QUE FALLE SON MIAS

| lo que se mide | sobre los 60 | sobre los 58 sin quemados |
|---|---:|---:|
| coinciden | **56** | **54** |
| discrepan | **4** | **4** |
| DENTRO de mi marcado | **3** (`976`, `2662`, `3173`) | **3** |
| FUERA de mi marcado | **1** (`2428`) | **1** |

**MI REPARTO CONTRA EL DEL ARCHIVO:** mio `A 10, B 1, C 0, D 49`; del archivo
`A 8, B 1, C 0, D 51`. **Marque QUINCE discutibles antes de destapar** y acerte en
doce de ellos.

**DOS PUESTOS QUEMADOS, DECLARADOS ANTES DE CONTAR:** el `654` y el `719`.
`PROMPT_SIGUIENTE.md`, que hay que leer para saber que se audita, **publica su
clase de archivo** al ensenar la leccion de la `B` que faltaba y la del `719` que
el auditor de la 195 perdio. Los lei y los clasifique igual, y acerte en los dos,
pero **salen del credito**: un puesto cuya clase ya me dijeron no prueba que yo lea
bien. Es el hallazgo `5.1`.

**LAS CUATRO DISCREPANCIAS VAN ADJUDICADAS EN LA SECCION 4.** Y una observacion
que no es mia sola: **el ejecutor y yo, leyendo por separado, fallamos EXACTAMENTE
los mismos cuatro puestos** (`976`, `2428`, `2662`, `3173`). El fallo ademas dos
mas (`1807` y `1808`) donde yo dude y cai del lado bueno. **Dos lectores
independientes que convergen en los mismos cuatro dicen algo del archivo y no solo
de los lectores**, y por eso eso va a la seccion 5.

## 3. LAS CAIDAS DE ESTA VUELTA

### `C.E1` DEL EJECUTOR, DE CIFRA PUBLICADA: UNA RUTA QUE PROMETE PRUEBA SOBRE UN FICHERO QUE NO EXISTE

**Linea 19 de `docs/loop/REPORTE.md`**, dentro de la cabecera del reporte: *"el
bloque `E` del sello de apertura corrio `scripts/loop/vuelta193_racha_de_cierres.py`
sobre el inventario ENTERO"*.

**MEDIDO POR MI Y NO SUPUESTO:** ese fichero **no existe en disco** y
`git log --all -- scripts/loop/vuelta193_racha_de_cierres.py` **no devuelve nada**,
o sea que **no ha existido nunca en ninguna rama**. Lo que el sello corrio de
verdad, leido de la linea 46 de `docs/loop/SALIDA_V195_APERTURA.txt`, es
`python scripts/loop/vuelta192_racha_de_cierres.py`, **que es el nombre que el
propio reporte usa BIEN dos veces mas abajo**, en sus lineas 809 y 913.

**POR QUE ES DE CIFRA Y NO DE REPORTE:** `AUDITOR.md` 4, LA RUTA QUE PROMETE
PRUEBA ES CIFRA, decision del fundador del 5 sep 2026, punto 3 de
`paradas/2026-09-05-la-bateria-sin-techo-DECISION.md`, literal: *"UNA RUTA
PUBLICADA COMO EVIDENCIA DE UNA CORRIDA CUENTA COMO CIFRA PUBLICADA EN SU SEDE. Si
apunta a un fichero inexistente o de cero bytes, es CAIDA DE CIFRA."* Es
exactamente el caso de la vuelta 172 que trajo la regla. **Y por el otro camino
tambien acumularia:** vive en la CABECERA, que es una de las tres sedes de la letra
del 27 ago.

**RACHA DE CIFRA PUBLICADA: 1.** Dos tandas seguidas serian PARADA. **No lo son
hoy**, porque el acta 195 midio CERO caidas de cifra en la vuelta 194.

**LO QUE NO ES, Y SE DICE PARA NO INFLARLO:** no mueve ningun dato, la corrida SI
se hizo, y la cifra que esa frase acompana (racha 9 sobre las vueltas 185 a 193) es
CORRECTA y esta sellada. **Lo falso es el nombre del instrumento**, y por eso entra
por la regla de la ruta y no por la del dato.

### `C.A1` MIA, DE METODO, Y ES LA MISMA ESPECIE QUE EL `C.1` DEL ACTA 195

**Reconte el marcador con `json` a mano** sobre `INTRA_DOMINIO_VEREDICTOS.jsonl` en
vez de por `AP.marcador()`, que es la puerta y ya ofrecia la cuenta sin coste. **Es
la mitad exacta del `C.1` que el acta 195 se declaro a si misma**, con la otra
mitad, leer `clase` por mi cuenta, NO cometida: para las clases si use
`AP.leer_veredictos()`, y **el sujeto no se pudo quemar** porque el destape vino
DESPUES de declarar mis clases en verde con 0 destapes apuntados.

**REMEDIADA DENTRO DE LA VUELTA:** corri `AP.marcador()`, que da
`{"filas": 3388, "por_clase": {"A": 551, "B": 72, "C": 5, "D": 2760}}`, **identico
a mi cuenta a mano**. Salida en `docs/loop/_auditor_v196_marcador.txt`.

**RACHA DE ESTA CAIDA PROPIA: 2** (actas 195 y 196). **A LA TERCERA, el acta 197
tiene que ABRIR con su remedio como tarea bloqueante del propio auditor**, por la
letra de `AUDITOR.md` 1.2, LA CAIDA DEL AUDITOR GANA DIENTES. **Lo dejo escrito
contra mi mismo y con el remedio ya nombrado**, que es de una linea: la fila del
marcador del acta se cita de `AP.marcador()` y de nada mas.

## 4. ADJUDICACIONES

**LAS CUATRO DISCREPANCIAS DE MI CIEGA, Y LAS CUATRO A FAVOR DEL ARCHIVO:**

**`4.1` EL `976`, Y ES MI CAIDA POR LA MISMA PUERTA QUE LA DEL AUDITOR DE LA 195.**
Yo lei `D` (identificar contra formalizar: fases distintas). El archivo dice `A` y
su razon **cita una regla de familia ya fijada**: *"es la misma A del puesto 712"*
y *"era uno de los dos pendientes del sub-puro numero 7. Cuatro pares leidos y los
CUATRO en A"*. **El encargo de la 195 avisaba con estas palabras**: la vara de
contenido-manda es EL SUELO, NO EL TECHO, y antes de aplicarla se pregunta si el
par tiene REGLA PROPIA de familia. **Yo no lo pregunte, y consultar la familia NO
habria quemado nada**, porque las clases de OTROS puestos no son mi sujeto sellado.
**A FAVOR DEL ARCHIVO.**

**`4.2` EL `2428`, Y ES EL QUE CAE FUERA DE MI MARCADO.** Yo lei `A` porque los ids
se diferencian en una letra (`desarrollar_` contra `desarrollo_`). El archivo dice
`D` con la razon *"Generar contra elegir... Uno abre el abanico y el otro lo cierra.
ARISTA QUE FALTA, y con direccion"*. **El banco `9.6.3` dice expresamente que el
TAMANO del solape no decide y que se pesa el resto y en que lado**, y aqui cada lado
conserva procedimiento propio. **A FAVOR DEL ARCHIVO, y la caida es mia y del mismo
perfil que la del ejecutor**, que fallo el mismo puesto por la misma causa. **Por
`AUDITOR.md` 1.2 el credito de mi tanda BAJA y mi tramo se relee al doble**,
encargado en la seccion 8 con su tramo y su doble ya cerrados.

**`4.3` EL `2662`, A FAVOR DEL ARCHIVO Y CON UNA SALVEDAD QUE ES HALLAZGO.** Yo lei
`A`. El archivo dice `D` por una **CORRECCION DECLARADA de la vuelta 51**: la fusion
de `OP-U-01` depreco `consejo_calidad_2` con alias a `consejo_de_calidad`, y desde
entonces el puesto **resuelve a otro par**. La correccion es correcta y no se toca.
**La salvedad esta medida y va al `5.3`:** la razon VIEJA que el propio archivo
conserva entera dice, literal, *"Por la vara, REPITE"*, que es lo mismo que lei yo,
y **el nodo que la ciega me enseno tiene 5 pasos mientras el nodo vivo tiene 11**,
verificado por mi contra `dataset/metadata/master_graph.json`.

**`4.4` EL `3173`, A FAVOR DEL ARCHIVO.** Yo lei `A` (los dos enumeran la triada del
autocontrol). El archivo dice `D` y **el propio archivo se marca DISCUTIBLE MARCADO
fuerte**, con las dos especializaciones propias de cada lado nombradas una a una.
**Yo tambien lo marque discutible.** Cuando el archivo y el lector dudan lo mismo y
el archivo argumenta el resto, manda el archivo. **Es una discrepancia sana, no una
caida de lectura.**

**LAS TRES PREGUNTAS DEL REPORTE, LAS TRES CONTESTADAS POR EXTENSION CITABLE:**

**`4.5` `P.1`, LA RACHA DE CIERRES. A FAVOR DE MEDIR EL ACTO, NO EL FICHERO.** El
instrumento cuenta `SALIDA_V<n>_CERRAR_REPORTE.txt` y `AUDITOR.md` 6.2 pide *"DOS
VUELTAS SEGUIDAS que CIERREN SU PROPIO REPORTE con `cerrar_reporte.py`"*. **La regla
nombra un ACTO; el instrumento cuenta un ARTEFACTO que nadie esta obligado a
escribir.** Lo adjudico citando la caja de cabecera de `AUDITOR.md` 0: *"Contar bien
un campo y sacar la conclusion equivocada sigue siendo una caida: la fuente hay que
elegirla antes de contarla"*, que es el precedente de las 37 fichas. **La 194 SI
cerro su reporte con `cerrar_reporte.py` en exitcode 0** y su mensaje de commit lo
publica; lo que falta es su fichero. **Y el ejecutor tiene razon en su frase:** un
instrumento asi *"mide la memoria del ejecutor, no la racha"*. **El remedio va
encargado como codigo**, y hasta que corra **me quedo del lado estrecho: el encargo
de la 196 lleva DOS sub-tareas**, que es lo que la cifra del instrumento sostiene
hoy.

**`4.6` `P.2`, LA GUARDA DEL `SUJETO CONGELADO`. A FAVOR, Y CON SU CALIBRADO ANTES
QUE SUS DIENTES.** La guarda que propone el ejecutor, que la huella de vivo no case
con `open(`, `io.open(` ni `read_text`, es codigo ordinario y no doctrina nueva. **Su
propio miedo esta bien puesto** y por eso se adjudica con condicion: **en su primera
vuelta la guarda PUBLICA SU LISTA y NO detiene a nadie**, y solo muerde cuando su
lista salga vacia sobre los cinco arneses de hoy. Va a la cola, no a este encargo.

**`4.7` `P.3`, EL TOPE DE 80 LINEAS DEL MODO AUSTERO. CONTESTADA POR EXTENSION, Y VA
CONTRA EL EJECUTOR.** El modo austero dice de que se recorta: *"Queda prohibida la
prosa de acompanamiento que repite lo que el registro ya dice"* y *"El austero recorta
tinta, no control"*. **Luego el tope se mide sobre la prosa que el ejecutor escribe A
MANO, y no sobre la cabecera tallada ni las tablas talladas**, que la propia regla
nombra como contenido que se queda. **Pero eso no salva a este reporte:** mide **995
lineas por `split` y 994 por `count(NL)`**, y las piezas talladas son una fraccion
minima. **Bajo cualquiera de las dos lecturas esta muy por encima de 80.** No lo
registro como caida porque **el ejecutor lo pregunto en vez de romperlo en silencio**,
que es exactamente lo que la casa pide, y porque ningun encargo se lo exigio. **Queda
adjudicado y encargado con su medicion.**

**LOS SIETE DISCUTIBLES DEL REPORTE, `D.1` a `D.7`, LOS SIETE A FAVOR:**

**`4.8`** `D.1`, invertir el orden de las tareas 1 y 2: **A FAVOR**, el encargo no
fija el orden, las dos cerraron, y el motivo es correcto (registrar el acta 195 antes
le habria quemado la ciega). **`4.9`** `D.2`, leer el acta entera despues: **A
FAVOR**, sus clases ya estaban selladas. **`4.10`** `D.3`, declarar sujeto congelado
en cuatro en vez de caso declarado: **A FAVOR**, la regla ofrece las dos salidas y su
riesgo declarado es la `P.2` que adjudico en el `4.6`. **`4.11`** `D.4`, tocar
`vuelta194_bateria_por_tramos.py`: **A FAVOR**, es donde vive `--componer` y es el que
la 199 clonara; dejar el arreglo en un fichero que nadie clona habria sido peor.
**`4.12`** `D.5`, los dos arneses nuevos entran en su misma vuelta: **A FAVOR**, es lo
que la regla hace desde la 144, lo reservado es PODAR y esto es crecer, y sin ello la
199 abriria con el rojo reencendido. **`4.13`** `D.6`, publicar el cotejo sobre 60 y
sobre 58: **A FAVOR, y la cuenta honesta es la de 58**, que le BAJA el resultado;
publicar las dos es lo correcto y **yo hice lo mismo por el mismo motivo**. **`4.14`**
`D.7`, contar como caida propia el arnes no reproducible: **A FAVOR**, la vara es lo
que se mide y no lo que llega a publicarse.

**CATORCE ADJUDICACIONES, LAS CATORCE A FAVOR, Y ES LA SEXTA ACTA SEGUIDA SIN UNA
SOLA EN CONTRA.**

## 5. HALLAZGOS MIOS, QUE NO SALEN DE NINGUN DISCUTIBLE

**`5.1` EL ENCARGO QUEMA PUESTOS DE LA CIEGA SIGUIENTE, Y ESTA MEDIDO EN DOS.**
`PROMPT_SIGUIENTE.md` publico la clase de archivo del `654` y del `719` para ensenar
la leccion de la `B` y la de la regla de familia. **La leccion era buena y el efecto
colateral tambien es real:** el auditor de la vuelta siguiente tiene que leer el
encargo, y al leerlo **recibe dos clases del sujeto que va a releer a ciegas**. El
ejecutor lo vio desde su lado y lo publico en su `D.6`; yo lo vi desde el mio y saque
los dos del credito. **Los dos lo declaramos por separado, y eso dice que lo que falta
es el carril y no la persona.**
**EL REMEDIO, y es barato:** cuando un encargo tenga que ensenar la leccion de un
puesto que sigue vivo en la cola, **nombra el puesto y su FIGURA, no su clase**.

**`5.2` DOS LECTORES INDEPENDIENTES FALLAN LOS MISMOS CUATRO PUESTOS.** El ejecutor y
yo leimos los 60 por separado, con la misma vara y sin vernos las clases, y **fallamos
exactamente `976`, `2428`, `2662` y `3173`**. No es una coincidencia comoda: son **el
100 por ciento de mis discrepancias y el 67 por ciento de las suyas**. **Lo que eso
dice, y no lo resuelvo yo porque mover una clase es del RECOMPUTO:** esos cuatro son
los candidatos con mas derecho a entrar en la cola de relectura conjunta del recomputo,
por delante de los que solo un lector discute.

**`5.3` LA CIEGA NO PUEDE ALCANZAR LA CLASE DE UN PUESTO CUYA CORRECCION SE APOYA EN
UNA FUSION PLANEADA Y NO APLICADA. MEDIDO EN EL `2662`.** El archivo dice `D` porque el
par **resuelve** a `consejo_de_calidad` contra `consejo_de_calidad_3` tras el alias de
`OP-U-01`. **Pero esa fusion NO esta aplicada al grafo:** lo verifique yo, y
`consejo_calidad_2` **sigue vivo con sus 5 pasos** mientras `consejo_de_calidad` tiene
**11**. El aislador lee los pasos del grafo VIVO, asi que **me enseno los 5 pasos del
nodo deprecado-en-el-plan y me pidio la clase del par resuelto**, que es un par cuyos
textos yo no vi. **Ningun lector a ciegas puede acertar eso**, y de hecho ninguno de
los dos acerto.
**LO QUE NO PROPONGO:** tocar la clase, que es del recomputo, ni tocar el aislador por
mi cuenta. **LO QUE SI:** que estos puestos se puedan **excluir del sujeto o marcar en
la ciega como RESUELTOS A OTRO PAR**, porque hoy contaminan la metrica de credito de
todo el que los reciba. Va a la cola con su cifra.

## 6. PENDIENTES DE DOCTRINA

**NINGUNO.** Las cuatro discrepancias y las tres preguntas se resolvieron con reglas
escritas y citadas por su numero: `AUDITOR.md` 0, 1.2, 4 y 6.2, y el banco `9.1` y
`9.6.1` con sus precisiones `9.6.2` y `9.6.3`. **Ninguna pidio una regla que no
exista.**

## 7. LA METRICA DE CREDITO

| | esta vuelta | acumulado |
|---|---:|---:|
| relecturas | 1 | **331** |
| puestos | 60 aislados, **60 cotejados**, **2 quemados** (`654`, `719`) | **1.186** |
| discrepancias DENTRO del marcado | **3** (`976`, `2662`, `3173`) | **56** |
| discrepancias y hallazgos FUERA del marcado | **4** (`2428`, y los tres hallazgos de la seccion 5) | **174** |
| caidas propias del auditor QUE ACUMULAN | **0** | |
| caidas propias del auditor, TOTAL del cuerpo | **1** (`C.A1`, de metodo, remediada dentro de la vuelta) | misma especie que la 195: **racha 2** |
| caidas del ejecutor que ACUMULAN por cifra publicada | **1** (`C.E1`, la ruta inexistente) | **racha de cifra publicada: 1** |
| caidas del ejecutor de reporte | **0** | **racha de reporte: 0** |
| caidas del ejecutor de metodo | **4**, las cuatro declaradas por el y cazadas dentro de la vuelta | no acumulan |

**LA FILA DE CAIDAS PROPIAS VA PARTIDA EN DOS**, que es el remedio del hallazgo `5.1`
del acta 195 aplicado otra vez.

**CREDITO DE MI TANDA: BAJA**, por el `2428`. **El doble va encargado y su tramo esta
CERRADO HOY** en `docs/loop/_auditor_v196_doble_para_la_197.txt`, computado con
`vecinos()` IMPORTADA y con solape 0 y 0 por construccion.

**CREDITO DE LA TANDA DEL EJECUTOR: BAJA TAMBIEN**, por sus dos discrepancias fuera de
su marcado y por la `C.E1`. **Su tramo ya se relee**, porque es el mismo que el mio.

**NINGUNA CONDICION DE PARADA SE CUMPLE.** Ni doctrina nueva (seccion 6), ni
contradiccion sin regla (las tres preguntas se adjudicaron), ni decision de fundador,
ni fallo tecnico repetido (Gate 0 y las suites en verde, corridas por mi), ni credito
roto de dos tandas seguidas (la racha de cifra publicada es 1), ni campana consumada.
**El bucle sigue.**

## 8. LO QUE ENCARGO A LA 196

**DOS SUB-TAREAS, Y ME QUEDO DEL LADO ESTRECHO A PROPOSITO.** `AUDITOR.md` 6.2 pide
dos vueltas seguidas cerrando su propio reporte y **el instrumento mide la racha en
1**, no en 9: la remedicion al cierre de la 195 lo dejo asi y la recompute yo.
**Aunque mi adjudicacion `4.5` da por buena la lectura del ACTO, no me apoyo en ella
para ensanchar mi propio encargo.** Si la 196 sella su
`SALIDA_V196_CERRAR_REPORTE.txt`, la racha llega a 2 por las dos lecturas y el tope de
cinco vuelve solo.

**TAREA 1, LOS REGISTROS**, con las catorce adjudicaciones, los tres hallazgos, la
`C.E1` del ejecutor y mi `C.A1`.

**TAREA 2, LA RELECTURA AL DOBLE DE MI TRAMO**, que es deuda mia por el `2428`. EL
TRAMO son los 60 puestos de `docs/loop/_auditor_v196_ciega_blind.txt`; EL DOBLE son sus
60 vecinos deterministas, **cerrados hoy** sobre `evitar` de **621 puestos** contados de
**catorce ficheros**, con **solape 0 y 0**. **Se cierra hoy para que no se elija despues
de mirar.**
