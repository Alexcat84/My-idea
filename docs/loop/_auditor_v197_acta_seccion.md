
# ACTA DEL AUDITOR, VUELTA 197 (6 sep 2026, auditor Opus 5)
# Cubre LA VUELTA 196 ENTERA. Prefijo de mis ficheros: `_auditor_v197_*`.

**CERO HUECO DE ACTA** (`AUDITOR.md` 1.0): la ultima acta escrita es la **196**, cubre
la **195**, y esta cubre la **196**, que es la inmediatamente anterior. Los commits de
la vuelta auditada van de `0bbe5f86` a `f7d41c38`, leidos por `AP.git_log()`.

## 0. MI APERTURA, Y LO QUE NO PUEDE TAPAR

**SELLO VERDE, CON CERO PROHIBIDOS ANTES DE SELLAR:**
`docs/loop/SELLO_APERTURA_AUDITOR_V197.json`, 1657 bytes. Ciega
`_auditor_v197_ciega_blind.txt` 162966 bytes, `sha256` `bd701135c5eb5c58`; destape
`_auditor_v197_ciega_reveal.txt` 123065 bytes, `sha256` `f3d2620178997f0b`.
**Sello los 120 ENTEROS y no una muestra**, a diferencia de la 196 que sello 60: asi
el mandato de empezar por los discutibles marcados queda cubierto POR CONSTRUCCION.

**EL FICHERO DEL TURNO LLEGO SUCIO Y LO BORRE, Y ESO ES UN ACTO.**
`_TURNO_DEL_AUDITOR.json` traia la bitacora del turno ANTERIOR (`git log`, `git
status`, `REPORTE.md` y dos destapes) y con ella `sellar()` caia en rojo. Corri
`--olvidar-turno`, con el estado heredado copiado antes a
`_auditor_v197_turno_heredado.json` y `.txt`. **Y ES UN AGUJERO, no una anecdota:
el fichero del turno NO SE LIMPIA AL CERRAR UN TURNO**, asi que todo auditor nuevo
hereda una bitacora que le impide sellar y tiene que borrarla. Va encargado.

**LO QUE MI SELLO NO PUEDE PROBAR, Y LO DIGO YO:** el arnes que me lanza inyecta en
mi contexto, ANTES de mi primer comando, un bloque `gitStatus` con la rama y los
cinco commits mas recientes. **El sello publica `prohibidos antes del sello: 0` y eso
es cierto PARA EL MODULO, no para mi.** Lo que vi ahi son asuntos de commit, no
clases ni razones, asi que **el sujeto de la ciega no se quemo por esa via**; pero la
frase del fichero (*"no puede impedir que corras `git status` por tu cuenta"*) cubre
este caso por extension y **la declaracion es mia, no del sello**.

## 1. LA VERIFICACION, TODA CORRIDA POR MI EN ESTA VUELTA

| que | mi medicion | calza con el reporte |
|---|---|---|
| Gate 0 | **OK**, auto-aristas 0, duplicadas 0, divergentes 0 | SI |
| censo: nodos / vivos / deprecados | **3853 / 3169 / 684** | SI |
| aristas: siguientes / previos / suma / union | **8780 / 8740 / 17520 / 9914** | SI |
| motor | **25/25** | SI |
| tsc | **exitcode 0, cero lineas** | SI |
| web | **82 passed (82) / 1040 passed (1040)** | SI |
| marcador, por `AP.marcador()` | **3388 filas; A 551, B 72, C 5, D 2760**; 0 huecos, 0 duplicados | SI |
| `INTRA_DOMINIO_VEREDICTOS.jsonl` | disco **4054129** bytes y LF **4054129**; `sha256` `0a77b5a35a962621` por las dos | SI |
| `docs/PENDIENTES.md` | **1063803** bytes por las dos convenciones | SI |
| serie de registros | **R.58** escrita, siguiente libre **R.59**, 0 colisiones, 0 huecos | SI |
| racha de cierres, por `vuelta192_racha_de_cierres.py` | **2**, vueltas **195 y 196**, cortada por la 194 | SI |
| selladas de cierre en disco | **14**, **13 en VERDE** (la 184 sin la linea), faltan 181, 182, 183, 194 | SI |
| selladas de bateria TRAMO en 176/183/189/194 | **38** | SI |
| razones de los 120 que citan RACIMO / CORRECCION DECLARADA | **6** y **3** | SI |
| `dataset/`, `web/`, `engine/` al cerrar | **0 filas** de `git diff --numstat` cada uno | SI |

**LA RUTA QUE PROMETE PRUEBA, BARRIDA ENTERA:** de **40** rutas citadas en
`REPORTE.md`, **38 existen y ninguna mide cero bytes**. Las dos restantes son
`docs/loop/SALIDA_V196_BATERIA.txt`, que el propio reporte declara INEXISTENTE en su
seccion 9 con su atribucion, y `SALIDA_V196_BATERIA_TRAMO_N.txt`, que es un **nombre
de patron dentro de una medicion** y no una promesa de prueba. **Cero caidas de esta
especie.**

**LA SELLADA AJENA QUE TOQUE, RESTAURADA Y REMEDIDA:** correr el instrumento de la
racha reescribe `SALIDA_V192_RACHA_DE_CIERRES.txt`. La restaure con `git checkout --`
y la remedi: **disco 2443 bytes y LF 2399 bytes**, `sha256` `ceb100c9fb83df88` por
disco y `4469a54a3417f36b` por LF, **identicos a los que el reporte publica**.

**LA VUELTA 196 REPRODUCE ENTERA. No encontre ni una sola cifra falsa suya.**

## 2. LA CIEGA: 120 SELLADOS, 8 QUEMADOS POR EL PROPIO REPORTE, 103 DE 112

**LA CONTAMINACION SE DECLARO ANTES DE ESCRIBIR UNA CLASE**, en
`_auditor_v197_contaminacion.txt`, y **el orden esta probado**: clases declaradas en
VERDE por `--declarar-clases` con **0 destapes apuntados** antes.

| sobre que se mide | coinciden | discrepan |
|---|---:|---:|
| los **120** enteros | 107 de 120 | 13 |
| **los 112 LIMPIOS, y es la cifra que manda** | **103 de 112** | **9** |
| solo los 8 quemados, fuera del credito | 4 de 8 | 4 |

| | mio | del archivo |
|---|---|---|
| sobre los 120 | A 22, B 1, C 0, D 97 | A 17, B 1, C 0, D 102 |
| sobre los 112 limpios | A 16, D 96 | A 13, D 99 |

**SOBRE EMITI `A` POR TRES EN LA MITAD LIMPIA**, y esa es mi desviacion: 16 contra 13.
**La `B` no la puedo reclamar**: el reporte publica que la unica `B` del archivo es el
`654`, asi que en esta tanda no la lei, la supe.

**LOS 8 QUEMADOS Y POR QUE**: `207`, `616`, `880`, `2429`, `2430`, `2662` y `2917`
porque la tabla de las siete discrepancias de la seccion 2 del reporte publica su
clase de archivo; y el `654` porque su prosa dice *"la que si acerte es el 654"* sobre
la clase `B`. **Y la contaminacion agregada tambien va dicha:** el reporte publica el
reparto del archivo sobre MIS MISMOS 120 (`A 17, B 1, C 0, D 102`), asi que supe
cuantas `A` quedaban por encontrar antes de buscarlas.

## 3. LAS CAIDAS

### `C.E1` DEL EJECUTOR, Y LA RE CLASIFICO A SU FAVOR: ES DE REPORTE, NO DE CIFRA

El `12038` de `SALIDA_V196_T2_SUJETO.txt`, publicado en la seccion de la TAREA 2
cuando el fichero medi 12683. **El ejecutor la registro contra si mismo como cifra
publicada** y pregunta en su `P.1` si mueve la racha. **La adjudico en la `4.3` y la
letra dice que no.**

### `C.E2` Y `C.E3` DEL EJECUTOR, DE METODO, NO ACUMULAN
Correr el sujeto antes de comprobar su bloque `C` (causa directa de la `C.E1`), y el
tope de 80 lineas del modo austero. **Las dos declaradas por el.**

### `C.A1` MIA, DE METODO, Y ES LA TERCERA ACTA SEGUIDA DE LA MISMA ESPECIE

**Reconte el marcador con `json` a mano** en vez de por `AP.marcador()`. **Es
EXACTAMENTE la `C.A1` del acta 196 y la mitad del `C.1` del acta 195.** Con esta van
**TRES ACTAS SEGUIDAS**, y eso dispara la letra de `AUDITOR.md` 1.2, LA CAIDA DEL
AUDITOR GANA DIENTES: **el acta 198 ABRE con su remedio, como TAREA BLOQUEANTE del
propio auditor, antes de verificar nada.** Y **no me quedo en declararla**: va
encargada como codigo en la TAREA 2, porque el remedio de la 196 fue correr el
instrumento y a la vuelta siguiente volvi a caer, que es la prueba de que un remedio
de memoria no es un remedio.
**REMEDIADA DENTRO DE LA VUELTA:** `AP.marcador()` da
`{"filas": 3388, "por_clase": {"A": 551, "B": 72, "C": 5, "D": 2760}}`, **identico a
mi cuenta a mano**.

### `C.A2` MIA, DE METODO, Y ES LA QUE MAS PUDO COSTAR

**Corri `scripts/run_phase1.py` SIN `--reaplico-curaduria` y mute `dataset/`:**
`git diff --numstat` dio **72 y 72 sobre `dataset/metadata/master_graph.json`**, 71
etiquetas revertidas al titulo del libro. **Reparada con el mismo carril que usa el
ciclo** (`etiquetas_de_cara.py --aplicar`) y verificada: `dataset/`, `web/` y
`engine/` cierran en **0 filas** cada uno. **Cazada dentro de la vuelta, y ni un
veredicto ni una clase se movio.**

### `C.A3` Y `C.A4` MIAS, DE METODO, CAZADAS ANTES DE PUBLICAR
Mi barrido de rutas ponia `json` antes que `jsonl` en la alternancia y dio un
`INEXISTENTE` falso. Y conte **45** selladas de bateria con el glob ancho donde el
reporte cuenta **38** con el estrecho, que es el correcto porque es el que compara
contra `SALIDA_V196_BATERIA_TRAMO_N.txt`. **Ademas lei como "2 arneses fuera de la
nomina" lo que era LA LONGITUD DE UNA TUPLA**; la cifra real es **0** con la vara y
**60** sin ella. **Ninguna de las tres llego a publicarse: las tres se corrigieron en
su propio fichero.**

### `C.A5` MIA, DE METODO, Y HABRIA FALSEADO UN "POR CONSTRUCCION"
Compute el universo consumido con UNA sola expresion para todos los ficheros y me dio
**300**, cuando los dos `_exclusion.txt` guardan enteros sueltos y se leen con
`numeros_de()`. **Con esa cuenta el "solape 0 por construccion" del doble habria sido
falso.** Recomputado importando `puestos_de()`, `numeros_de()` y
`UNIVERSO_CONSUMIDO` del fichero de la 196: **681 de 16 ficheros, y 561 por diferencia
de conjuntos con mi tramo, que es la misma cifra que la 196 publica.**

## 4. LAS ADJUDICACIONES

**`4.1` LAS NUEVE DISCREPANCIAS LIMPIAS, LAS NUEVE A FAVOR DEL ARCHIVO.** `655`,
`719`, `976`, `1809`, `1810`, `2838`, `2916`, `3072` y `3173`. **CERO caidas de clase
del ejecutor.** Y mis errores tienen dos especies medidas, las dos mias:
**la de familia** (`719` y `976`: el archivo cita una REGLA PROPIA ya fijada, la del
puesto 595 y la del sub-puro 7, y yo aplique la vara de contenido-manda como si fuera
el techo, con la advertencia escrita en mi propio criterio sellado); y **la de
contencion invertida** (`2838`: el nodo corto cabe entero en el largo y NO trae ni un
paso propio, y aun asi lei "el hijo trae procedimiento, luego CONTINUA" mirando el
residuo del contenedor en vez del del contenido).

**`4.2` LAS CUATRO DISCREPANCIAS QUEMADAS SE PUBLICAN Y NO ENTRAN AL CREDITO**
(`616`, `2429`, `2430`, `2662`), por la via del `2662` que el acta 196 ya acepto.

**`4.3` LA `P.1` DEL REPORTE: NO MUEVE LA RACHA, Y NO HACE FALTA DOCTRINA NUEVA.**
La letra define la CAIDA DE CIFRA PUBLICADA por sus SEDES: *"un veredicto, el
marcador, o una cifra que vive en `docs/plan/` o en el banco"*, mas la cuarta sede del
2 sep (comentarios y docstrings de guardas en `scripts/`) y la ruta que promete
prueba en la suya. **`REPORTE.md` NO ES SEDE DE ESA ESPECIE.** Y la letra define la
CAIDA DE REPORTE como *"una afirmacion equivocada que vive solo en `REPORTE.md` y no
mueve ningun dato"*, que es exactamente el `12038`. **Luego es CAIDA DE REPORTE.**
Y por la letra afinada del **27 ago 2026**, cuenta para la racha *"solo cuando la
cifra vive en una tabla, una cabecera o una conclusion"*: el `12038` vive **dentro de
un parentesis, en prosa de acompanamiento**, que es la misma forma del parentesis de
la vuelta 95 que el fundador declaro expresamente *"se registra y no acumula"*.
**SE REGISTRA CON SU NOMBRE, DISPARA LA RELECTURA AL DOBLE DE SU TRAMO, Y NO
ACUMULA. LA RACHA DE CIFRA PUBLICADA SIGUE EN 1 Y LA DE REPORTE PASA A 1.**
**Y lo digo con su consecuencia delante, para que se vea que no es comodidad:** si
acumulara, serian dos tandas seguidas y **esto seria una PARADA**. No adjudico a
favor del bucle: adjudico por la sede, que estaba escrita antes de que yo llegara.

**`4.4` LA `P.2` DEL REPORTE: NO SE ENSANCHA LA LISTA BLANCA; ESOS PUESTOS SALEN DEL
CREDITO.** Meter la pertenencia a un racimo censado en la ciega **entregaria la
respuesta**, porque un par de racimo declarado *"no pelea la clase"*. La via ya
existe y el acta 196 la acepto para el `2662`: **se declaran INALCANZABLES A CIEGAS y
salen de la metrica**. **Y lo confirmo en primera persona y con cifra: mis dos
errores de la especie de familia (`719` y `976`) son exactamente eso.**

**`4.5` LA `P.3` DEL REPORTE, ADJUDICADA POR EXTENSION Y CONTRA MI PROPIO TURNO.**
`AUDITOR.md` 1.2 manda *"imprime PRIMERO los pasos, adjudica tu clase, y SOLO DESPUES
destapa la razon escrita"*. **La tabla de discrepancias de un reporte ES un destape**,
y por extension natural de esa misma linea **el orden obligatorio del turno del
auditor pasa a ser: `sellar()` -> clasificar -> `--declarar-clases` -> `leer_reporte()`**,
y no el que hoy figura en la seccion 1. **Por el mismo argumento, el acta no publica
el reparto de una tanda que se va a releer.** Va encargado como codigo en la TAREA 2.

**`4.6` EL TOPE DE 80 LINEAS DEL MODO AUSTERO: SE MANTIENE Y NO SE AFLOJA, PERO SE
MIDE POR TRES VARAS.** El propio texto del austero dice *"el austero recorta tinta, no
control"*, y el crecimiento del reporte viene de piezas de control obligatorias
(cabecera tallada de 11 filas, tabla de tareas, seccion 9). **No invento una
excepcion:** el reporte mide **588 lineas por `count(NL)` y 589 por `split`**, y aun
por la vara estrecha del acta 196 son 318, cuatro veces el tope. **Encargo que se
publiquen las TRES medidas** (total, escrita a mano, y escrita a mano menos lo que
otra regla obliga) **para que el fundador decida sobre cifras y no sobre una queja.**

**`4.7` EL "0 ARNESES DEL CENSO FUERA DE LA NOMINA" DE LA SECCION 9 NO ES CAIDA, Y SE
ARREGLA IGUAL.** Medido por mi: censo **195**, nomina **135**, entradas invisibles al
censo **0**, fuera de la nomina **SIN vara 60** y **CON la vara 148: 0**. La frase del
reporte omite la vara, pero **nombra su fuente** (el bloque `F` del sello), y esa
fuente si la lleva. **No acumula nada.** Encargo que la cifra viaje con su vara.

## 5. HALLAZGOS QUE NO SALEN DE NINGUN DISCUTIBLE

**`5.1` EL REPORTE QUEMA LA CIEGA DEL AUDITOR POR CONSTRUCCION, Y ES LA `P.3` PERO
DEL OTRO LADO.** La `P.3` del ejecutor pregunta si el acta quema su tanda. **Lo mismo
me paso a mi con el reporte, y peor**: `AUDITOR.md` manda abrir `REPORTE.md` justo
despues de sellar, y ese reporte publica **la clase de archivo de 8 de mis 120
puestos** y **el reparto entero del archivo sobre esos mismos 120**. **No es un
descuido de nadie: es el orden escrito.** Su remedio es la `4.5`.

**`5.2` EL MARCADO DE DISCUTIBLES NO EXISTE POR DEBAJO DEL PUESTO 2662, Y LA METRICA
DE CREDITO SE APOYA EN EL.** Medido sobre mi sujeto: de los **120**, llevan el literal
`DISCUTIBLE MARCADO` **14**, y **los 14 son del 2662 para arriba**; de los **89**
puestos por debajo del 2662, **ninguno lleva marca**. **Mis cinco discrepancias de
fuera del marcado (`655`, `719`, `976`, `1809`, `1810`) caen las cinco en el tramo
donde el archivo no marca nada.** La regla del credito ("dentro o fuera del marcado")
**no es comparable entre tramos del archivo**, y **eso hace casi automatico que el
credito baje y el tramo se duplique**. **No lo resuelvo yo: la cifra queda publicada.**

**`5.3` TRES PUESTOS TIENEN YA TRES LECTORES INDEPENDIENTES CONTRA EL ARCHIVO.** El
reporte nombra cuatro que *"dos lectores independientes fallaron"*: `976`, `2428`,
`2662` y `3173`. **Yo soy el tercer lector y discrepo del archivo en `976`, `2662` y
`3173`, y COINCIDO con el en el `2428`.** O sea: **tres lectores contra el archivo en
tres puestos**, y el `2428`, que fue el que disparo toda esta relectura, **se estabiliza
a favor del archivo**. Las razones de los tres son solidas y verificadas contra el
grafo, y **por eso no muevo ninguna clase**: mover una clase es del RECOMPUTO. Va a la
cola con su cifra.

**`5.4` EL FICHERO DEL TURNO DEL AUDITOR NO SE LIMPIA AL CERRAR.** Llegue con la
bitacora del turno anterior y tuve que borrarla para poder sellar. **Una guarda que
obliga a un `--olvidar-turno` en cada vuelta ensena a borrar la bitacora**, que es lo
contrario de lo que la guarda quiere. Va encargado.

## 6. PENDIENTES DE DOCTRINA

**NINGUNO.** Las tres preguntas del reporte (`P.1`, `P.2`, `P.3`) se adjudican en la
`4.3`, la `4.4` y la `4.5` **citando letra escrita**, y la `P.1` en contra de lo que
me habria convenido si la letra hubiera dicho otra cosa.

## 7. LA METRICA DE CREDITO

| | esta vuelta | acumulado |
|---|---:|---:|
| relecturas | 1 | **332** |
| puestos | **120 aislados, 120 cotejados, 8 quemados** | **1.306** |
| discrepancias DENTRO del marcado | **4** (`2838`, `2916`, `3072`, `3173`) | **60** |
| discrepancias y hallazgos FUERA del marcado | **5** (`655`, `719`, `976`, `1809`, `1810`) | **179** |
| caidas propias del auditor QUE ACUMULAN | **0** | |
| caidas propias del auditor, TOTAL del cuerpo | **5** (`C.A1` a `C.A5`, todas de metodo, todas remediadas dentro de la vuelta) | `C.A1`: **TERCERA seguida de su especie** |
| caidas del ejecutor que ACUMULAN por cifra publicada | **0** | **racha de cifra publicada: 1** |
| caidas del ejecutor de reporte | **1** (`C.E1`, re clasificada en la `4.3`), en prosa: **no acumula** | **racha de reporte: 1** |
| caidas del ejecutor de metodo | **2** (`C.E2`, `C.E3`), declaradas por el | no acumulan |

**CREDITO DE MI TANDA: BAJA**, por las cinco de fuera del marcado. **EL DOBLE ESTA
CERRADO HOY**, antes de que nadie mire, en `docs/loop/_auditor_v197_doble_para_la_198.txt`:
**tramo 120, doble 120, solape con el tramo 0 y con el universo 0 POR CONSTRUCCION**,
con `vecinos()` importada y el universo de **681** contado de **16** ficheros.
**Y DIGO LO QUE ESA SERIE SIGNIFICA: va 30, 60, 120 y ahora 240, y el `5.2` explica
por que no se detiene sola.**

**CREDITO DE LA TANDA DEL EJECUTOR: SE SOSTIENE.** Cero caidas de clase, cero cifras
falsas halladas por mi, y las tres caidas de la vuelta las declaro el.

**NINGUNA CONDICION DE PARADA SE CUMPLE.** Ni doctrina nueva (seccion 6), ni
contradiccion sin regla (las tres preguntas se adjudicaron con letra escrita), ni
decision de fundador, ni fallo tecnico repetido (Gate 0 y las suites en verde,
corridas por mi), ni credito roto de dos tandas seguidas (la racha de cifra publicada
sigue en 1 por la `4.3`), ni campana consumada. **El bucle sigue.**

## 8. LO QUE ENCARGO A LA 197

**CUATRO SUB-TAREAS, Y EL TOPE DE CINCO VOLVIO SOLO.** `AUDITOR.md` 6.2 pide dos
vueltas seguidas cerrando su propio reporte con `cerrar_reporte.py`, y **el
instrumento corrido por mi hoy da la racha en 2, con las vueltas 195 y 196**. El
regimen temporal de dos sub-tareas **se apaga por su propio disparador de salida**,
sin que nadie tenga que adjudicarlo. Uso cuatro de las cinco.

**TAREA 1, LOS REGISTROS.** El acta 197 entra como `R.59`.

**TAREA 2, BLOQUEANTE Y DE CODIGO: EL ORDEN DEL TURNO DEL AUDITOR**, que es la `4.5`
y el remedio del `5.1`, mas el remedio de mi `C.A1` y el del `5.4`.

**TAREA 3, LA RELECTURA AL DOBLE**, que es deuda mia por las cinco de fuera del
marcado. Son **240**: los 120 del tramo mas los 120 del doble ya cerrado.

**TAREA 4, LAS DOS CIFRAS QUE VIAJAN SIN SU VARA**, que son la `4.6` y la `4.7`.
