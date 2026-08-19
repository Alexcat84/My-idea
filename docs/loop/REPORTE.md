# REPORTE DE LA VUELTA 46 DEL EJECUTOR (19 ago 2026)

**Encargo:** registros (TAREA 1) y `OP-D-07` con el cierre medido de la fase 02, mas la primera
operacion de la fase 03 si quedaba cuerda (TAREA 2).

> **LAS DOS TAREAS ESTAN COMPLETAS, PERO LA SEGUNDA NO SALIO COMO EL ENCARGO LA IMAGINABA, Y ESA
> ES LA NOTICIA DE LA VUELTA: LA CIRUGIA DE `OP-D-07` YA ESTABA HECHA DESDE EL 14 DE AGOSTO, Y LA
> HIZO LA FASE 01.** No se toco **ni un solo nodo**. Lo que quedaba por hacer era **medir sus tres
> verificaciones y publicarlas**, y eso destapo **una PARADA** que no se arregla aqui.

---

## 0. LO PRIMERO: EL ARBOL AL ABRIR, Y LA APERTURA MEDIDA ANTES DE NADA

**El acta de la vuelta 45 dejo verificado el arbol limpio y todo pusheado, y asi estaba:** `git
status` **vacio**, `HEAD` en **`2f0c47ef`** sobre `origin/pasada-unica`, sin adelanto ni retraso.
**No hubo parada que traer por este concepto.**

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION Y SE COMMITEO SOLA** (`a00a95c7`), regla 1
tercer renglon. **Se midio incluso antes de los registros de la TAREA 1**, que es mas estricto que
lo que el encargo pedia, con el mismo precedente de la vuelta 45.

```
python scripts/loop/vuelta31_estado.py APERTURA  -> SALIDA_V46_APERTURA.txt (exit 0)
python scripts/costuras_internas.py              -> SALIDA_V46_APERTURA_COLA.txt (exit 0)
```

| lo que el encargo exigia como apertura | lo que MI corrida dio | calza |
|---|---|---|
| marcador A 575, B 79, C 8, D 2.726 en n 3.388 | **A 575, B 79, C 8, D 2.726 en n 3.388** | **AL DIGITO** |
| grafo 3.853 ficheros, 3.524 vivos, 329 deprecados, 16.898 enlaces | **3.853 / 3.524 / 329 / 16.898** | **AL DIGITO** |
| cola 1.494 sobre 3.524 | **1.494 sobre 3.524 (42,4 por ciento)** | **AL DIGITO** |

**CERO discrepancias, asi que no hubo parada.** Ademas: rango de puestos 1 a 3.388, **huecos 0**,
**duplicados 0**, **clases fuera de ABCD 0**, operaciones **71** con **dependencias rotas 0**. Y el
arbol quedo **limpio** tras la corrida de costuras, o sea que el instrumento **reprodujo byte igual**
los ficheros commiteados.

---

## 1. HASH FINAL, COMMITS Y RUTAS TOCADAS

**`HEAD` de `pasada-unica`: el commit de este reporte.** El ultimo de trabajo es **`48efbcf0`**.
Arbol limpio y todo pusheado a `origin/pasada-unica`.

| # | hash | que es |
|---:|---|---|
| 1 | `a00a95c7` | **la apertura**, medida antes de la primera operacion y **commiteada sola** |
| 2 | `67dd8d3e` | **TAREA 1 completa**: la auditoria de la vuelta 45 registrada, con la tabla **impresa desde el acta** |
| 3 | `a380c20b` | `OP-D-07` **primer commit**: la lectura de cero **y el hallazgo**. Ni un nodo tocado |
| 4 | `42d500e2` | `OP-D-07` **segundo commit**: el ciclo Gate 0 verde, las tres suites y el **cierre de la fase 02 medido** |
| 5 | `48efbcf0` | `OP-D-07` **tercer commit**: el registro escrito, el cierre declarado midiendo y **la PARADA** |

**LAS RUTAS**, con `git diff --shortstat 2f0c47ef..48efbcf0`: **19 ficheros, 2.368 lineas anadidas
y CERO borradas**. Por carpeta, contado con mi comando: **`docs/loop` 14, `scripts/loop` 4,
`docs/plan` 1**. Total **19**.

> **Y LA CIFRA QUE MANDA EN ESTA VUELTA: NODOS TOCADOS, CERO.** `git diff --name-only` sobre
> `dataset/nodos` da **0 ficheros**. **No se toco el grafo, no se toco el censo, no se movio un
> solo veredicto.**

---

## 2. TAREA 1: LOS REGISTROS

**Escrita en `docs/plan/02_DESTEJIDOS.md`, bajo el registro de cierre de `OP-D-09`, con la tabla
IMPRESA y no tecleada** (regla 1, cuarto renglon):

```
python scripts/loop/vuelta46_registro_auditoria.py --escribir
  -> docs/loop/SALIDA_V46_REGISTRO_AUDITORIA.txt (exit 0)
```

**El instrumento imprime VERBATIM cada linea del acta que cada celda cita, mas la seccion 5 entera
(lineas 10.046 a 10.092), para que ninguna celda sea un recuerdo.** El acta de la vuelta 45 se leyo
**hoy**: abre en la linea **9.794** y cierra en la **10.157**.

| lo que el encargo mandaba registrar | la linea del acta que lo dice |
|---|---|
| la vuelta 45 auditada **ENTERA**, con Gate 0 y las tres suites re-corridos por corrida propia | **9.801**, y **9.797** para el *sin hueco de acta* |
| **CERO caidas del ejecutor** | **10.127** |
| **ciega 5 de 5**, con las cuatro piezas nombradas | **9.941**; la clase del **784** en **9.909**, la del **2695** en **9.917**, la lectura textual de `principio_calidad_mvp` en **9.923**, y los dos repartos origen por origen en **9.929** y **9.933** |
| **los ONCE discutibles A FAVOR** | **9.946** a **10.027** |
| **las SEIS correcciones correctas** | **10.028** |
| racha de reporte en **CERO** con **TRES reportes limpios seguidos** | **10.136** |
| la adjudicacion de la seccion 5: el `depende_de` de `OP-D-07` **se satisface con la mesa `OP-M-03` ADJUDICADA**, cuatro apoyos escritos, **cero doctrina nueva** | **10.051** y **10.077** |
| el aviso medido de que **las reescrituras de la mesa siguen pendientes** de su fase 06 | **10.074** |

**EL AVISO NO SE COPIO: SE RE-MIDIO** (regla 2, *una cifra de un acta es contraste, no fuente*).
Los siete puestos, leidos por mi de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:

| puesto | clase medida HOY por mi |
|---:|---|
| **668**, **737**, **771**, **843**, **957**, **1298**, **753** | **los SIETE en `B`** |

**COINCIDE AL DIGITO con lo que el acta declara.** Son trabajo de `OP-M-03` en su fase 06, no
precondicion del corte.

**Y LA CASILLA DE LA CAIDA DE REPORTE NO SE RELLENA, porque no hay nada que poner en ella.** El
acta declara cero caidas y adjudica las seis correcciones como correctas, con la frase que cierra
el punto: *NINGUNA afirmacion del reporte resulto falsa contra mi corrida*. **Se dice asi.**

---

## 3. TAREA 2: `OP-D-07`, Y EL HALLAZGO

### 3.1 LA LECTURA DE CERO, ANTES DE TOCAR NADA

`python scripts/loop/vuelta46_lectura_opd07.py` (**exit 0**, `SALIDA_V46_OPD07_LECTURA.txt`),
**instrumento de solo lectura**. La operacion se leyo **entera** de `OPERACIONES.jsonl` (los
diecisiete campos, impresos uno a uno) y el nodo **de cero**, hoy y desde `git`.

**Lo que la operacion dice, en lo material:** nodo unico `decision_pivote_perseverar`,
`superviviente` **nulo**, `eliminar` **vacio**, `aristas_nuevas` **vacio**, `preservar` con el
bloque de Traction (pasos 5 a 9), y **tres** puntos de `verificacion`.

### 3.2 EL HALLAZGO

> **EL DESTEJIDO QUE `OP-D-07` LEGISLA YA ESTABA EJECUTADO DESDE EL 14 DE AGOSTO DE 2026, Y LO
> EJECUTO LA FASE 01.**

- **Quien:** `OP-F-04-WEI`, **segunda tanda**, commit **`1eef1c6b`**.
- **Como lo halle:** `git log --follow` sobre `dataset/nodos/decision_pivote_perseverar.json`,
  **corrido hoy**. No sale de ningun acta ni de ningun reporte.
- **Y esta escrito:** `docs/plan/01_FUENTES.md` **linea 982** lo registra con su frontera
  (`decision_pivote_perseverar`, **5 a 9**, destino **nodo propio**
  `puntos_brillantes_antes_del_pivote`, por `P.18` punto 3), y el nodo nuevo figura en
  `INDICE_ROJO_DECLARADO.jsonl` con **esa misma fecha**.
- **`OP-D-07` tiene `fecha_corte` 2026-08-12**: se escribio **dos dias antes** de que otra fase se
  le adelantara.

**NO SE TOCO NI UN NODO.** Volver a cortar un nodo ya cortado no es ejecutar la operacion: **es
fabricar**. La guarda de simulacion previa, el caso positivo y las guardas de duplicadas **no
tienen sobre que correr**, y decirlo es mas honesto que inventarles un sujeto.

### 3.3 LAS TRES VERIFICACIONES, MEDIDAS

| # | lo que exige | como sale medido HOY |
|---:|---|---|
| **1** | el corte cae **entre el paso 4 y el 5** | **CUMPLE.** De **9** pasos a **4**, con prefijo **VERBATIM** comun de **4**. Los cuatro que quedan son los de Ries |
| **3** | el campo `fuente` queda con **UNA sola obra** | **CUMPLE.** De **2** obras a **1** (`The Lean Startup - Eric Ries`) |
| **2** | el bloque del punto brillante **no se pierde**, y **viaja entero al superviviente del acto I** | **MITAD Y MITAD.** El bloque **NO se perdio**: sus **5** pasos viven **byte a byte** en `puntos_brillantes_antes_del_pivote`, con arista desde el sujeto **y su espejo**. **Pero de viajar al superviviente, nada**: en `pivotar_o_perseverar` viven **0 de 5**, y en `decision_pivote_perseverar` **0 de 5** |

**El bloque va publicado paso por paso en el registro**, con su numero viejo (5 a 9) y su numero
nuevo (1 a 5). **CERO contenido perdido.**

### 3.4 LOS PARES DEL CASO, LEIDOS Y NO MOVIDOS

`OP-D-07` **no manda ninguna relectura ni ningun caso positivo sobre pares** (sus tres puntos de
`verificacion` estan copiados arriba y ninguno lo pide). Los tres del expediente se leyeron igual,
**y ninguno se movio**:

- **843** (`B`): su propia razon **ya nombraba el corte** entre el paso 4 y el 5.
- **860** (`A`): la razon dice que **el solape cae en los pasos 1 y 3, dentro del bloque de Ries**.
  **Medido hoy: esos cuatro pasos siguen verbatim.** O sea que **el adelanto de la fase 01 no toco
  el solape**, que era exactamente el riesgo que la `nota` de `OP-D-07` nombraba. **El par se
  sostiene en `A` y no hace falta recomputo.**
- **1298** (`B`): la frontera del punto brillante. Ver la PARADA.

---

## 4. LA PARADA, Y NO LA ARREGLO YO (regla 5)

**La segunda mitad de la verificacion 2 ya no se puede cumplir por la ruta que el plan escribio.**
No por un descuido de hoy: porque **el adelanto de la fase 01 saco el bloque del nodo que muere en
el acto I**. Los cuatro textos que la medicion contradice, **citados enteros y ninguno reescrito**:

| donde | que da por hecho | que mide el archivo HOY |
|---|---|---|
| `OP-D-07`, `verificacion` 2 | el bloque *viaja entero al superviviente del acto I* | el bloque **no esta** en el nodo que muere |
| `OP-M-03-I`, `preservar` | *del que muere, ya destejido: EL BLOQUE DEL PUNTO BRILLANTE entero, pasos 5 a 9* | **el que muere ya no lo trae**: **0 de 5** |
| `OP-M-03-I`, `verificacion` 3 | *el bloque del punto brillante esta entero y es identificable como bloque: la frontera del 1298 lo necesita nombrado* | esta entero **y es identificable**, pero **en un tercer nodo** que no es ninguno de los dos de `OP-M-03-I` |
| `FRONTERAS_DECLARADAS.md` **linea 82**, del **12 ago 2026** | *llega por el destejido `OP-D-07` y se conserva entero en el superviviente del acto I* | **hoy no llega por ahi, porque ya no sale de ahi** |

> **LA FRONTERA DEL 1298 NO ESTA PERDIDA: ESTA EN OTRO SITIO DEL QUE EL PLAN DICE.** Su lado del
> punto brillante vive **entero**, con `fuente` `Traction` **sola**, en un nodo propio y enlazado.
> **Lo que ya no se sostiene es la RUTA escrita, no el contenido.**

**Decidir si el lado se queda donde esta, si viaja al superviviente en el acto I, o si la frontera
se re-declara entre otros dos nodos, es una decision de la fase 03 y de la mesa.** Se trae como
**PARADA** y **no se arregla aqui**.

---

## 5. EL PRECEDENTE, HALLADO DESPUES DE ESCRIBIR EL REGISTRO Y EN LA MISMA VUELTA

**Se declara la secuencia en vez de disimularla**: el registro de `OP-D-07` se escribio primero, y
**despues** encontre que **esta pagina ya habia nombrado esta especie TRES veces**, con **el mismo
metodo** (medir el nodo de hoy, hallar la operacion que se llevo el bloque con `git log --follow`,
**y decirlo con la medicion delante**). El precedente **se anadio debajo del registro y no dentro**,
porque *una correccion que tapa lo que corrige no se puede auditar*.

| donde, en `02_DESTEJIDOS.md` | que dice, leido hoy |
|---|---|
| linea **251** y linea **292**, `OP-D-01`, vuelta 32 | *el destejido del pariente, **CONSUMIDO, y se dice con su medicion*** / *el destejido que esta operacion pedia **ya esta consumido*** |
| lineas **798** a **805**, `OP-D-03`, vuelta 34 | *DOS YA ESTABAN **CONSUMIDAS POR LA FASE 01***, con su tabla y las operaciones que se llevaron los bloques |
| linea **1773**, `OP-D-05`, vuelta 40 | *Ya se lo llevo `OP-F-04-HOR`, commit `2bd8dd76`, **medido con `git log --follow` y no supuesto**. Es el mismo caso que `OP-D-03`*. **Y esa operacion quedo `SELLADA`** (linea **1765**) |

> **LO QUE ESTO SIGNIFICA, SIN ESTIRARLO: NO HACE FALTA DOCTRINA NUEVA PARA LA MITAD DE LA
> CIRUGIA.** Un destejido consumido por la fase 01, medido y con su commit nombrado, **es una forma
> ya escrita de cerrar**, y `OP-D-05` la uso para quedar **`SELLADA`**. Aqui el bloque ademas **no
> se disolvio: fue a un nodo propio**, que es **mas** trazable, no menos.

> **Y LO QUE EL PRECEDENTE NO CUBRE, que es donde la PARADA se queda entera:** en `OP-D-03` y en
> `OP-D-05` **nada aguas abajo dependia de DONDE aterrizara el bloque**. **Aqui si**, y son dos
> textos los que lo escriben. **El precedente cierra la cirugia; NO cierra la ruta.**

---

## 6. EL CIERRE DE LA FASE 02, DECLARADO MIDIENDO

`python scripts/loop/vuelta46_cierre_fase02.py` (**exit 0**, `SALIDA_V46_CIERRE_FASE02.txt`).

**LAS NUEVE OPERACIONES DE LA FASE, con su registro:** `OP-D-01` a `OP-D-09`, **las nueve en estado
`LISTA`**. **OCHO tenian ya registro de cierre escrito** en una de las dos formas de la campana (la
frase `REGISTRO DE OPERACION HECHA` acunada en la vuelta 30, en `OP-D-01`, `OP-D-02`, `OP-D-06`,
`OP-D-08` y `OP-D-09`; el encabezado `CERRADA` o `SELLADA` de la forma anterior, en `OP-D-03`,
`OP-D-04` y `OP-D-05`). **La unica sin registro era `OP-D-07`, y lo recibio hoy.**

**EL CRITERIO DE HECHO**, copiado de `08_VERIFICACION.md`: linea **25**, *02 DESTEJIDOS: los quince
congelados releidos; cada perdida en el bloque del que proviene*; y linea **9**, *UNA FASE ESTA
HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA*.

**LOS CONGELADOS, CONTADOS HOY SOBRE EL ARCHIVO ENTERO** (detector: la razon abre con *NO SE JUZGA*,
*NO PUEDO JUZGAR* o *CONGELAD*, el mismo del verificador de la vuelta 45): **UNO sobre 3.388**, el
**1190** (`formalize_advisory_board` contra `identificar_consejo_asesores`), **que es de la junta
asesora y NO de esta fase**. **Los quince que el criterio nombra estan releidos.**

**GATE 0 Y SUITES, CORRIDOS EN ESTA VUELTA:**

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | los tres **exit 0**: `GATE 0: OK`, **71** etiquetas reaplicadas, **6** assets sincronizados |
| el comando **4** | **NO corre**: el censo **no se movio**, porque no se toco ningun nodo |
| **arbol tras el ciclo** | **byte igual a `HEAD`**. `phase1_run_log.json` respaldado antes y **comprobado byte igual despues**: no hizo falta restaurarlo |
| **suite del motor** | **25 de 25**, exit 0 |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas, exit 0 |
| **`tsc --noEmit`** | **CERO** lineas, exit 0 |

### LO QUE NO CIERRA, DECLARADO CON LA MEDICION DELANTE Y NO DECLARADO CERRADO

1. **LA MITAD DIFERIDA DE LA VERIFICACION 2 DE `OP-D-07`**: la **PARADA** de la seccion 4.
2. **EL MARCADOR DEL `00_INDICE` ESTA RANCIO.** Es una tabla de prosa que **ningun instrumento
   valida**, la especie exacta contra la que se escribio el cuarto renglon de la regla 1.
   Contrastada hoy fila por fila contra `OPERACIONES.jsonl`, **CUATRO filas no calzan**:

| fila | el indice publica | **mido hoy** |
|---|---:|---:|
| operaciones (total) | 69 | **71** |
| **02 DESTEJIDOS** | **7** | **9** |
| 0 CODIGO | 5 | **7** |
| 05 SANEO | 12 | **10** |

   **La de esta fase es la que mas importa: el indice dice SIETE operaciones y el fichero tiene
   NUEVE**, porque `OP-D-08` y `OP-D-09` nacieron despues. **Y la tabla de orden de fases del mismo
   indice repite el error en su celda de HECHO**, donde dice *las siete cirugias hechas*. **Se
   declara y NO se reescribe**: rehacer ese marcador es un encargo propio con su instrumento, no un
   apano al margen.

---

## 7. LA FASE 03 NO SE ABRE, Y VA CON LA CITA DELANTE

**El punto 6 del encargo dice que se ejecuta la primera operacion de la fase 03 por su orden
escrito, y que si el orden no esta escrito o exige decidir, NO se abre.** Medido
(`SALIDA_V46_ORDEN_FASE03.txt`):

> **EL PRIMER PUESTO ESTA EMPATADO A TRES**: `OP-M-02-PROG`, `OP-M-03-I` y `OP-U-01`, **las tres con
> `orden` = 1**.

Y **la pagina de la fase no escribe ninguna lista de orden**: `03_FUSIONES.md` tiene **cero** lineas
que fijen uno, y sus encabezados son de contenido (*las dos reglas de ejecucion*, *lo que no entra
aqui*), no de secuencia. El `00_INDICE` ordena **fases**, no operaciones dentro de la fase 03.

**Asi que la fase 03 NO SE ABRE.** Y aunque el empate se deshiciera a favor de `OP-M-03-I`, **esa
tampoco seria ejecutable hoy**: su `preservar` y su `verificacion` 3 son **dos de los cuatro textos
que la PARADA contradice**.

---

## 8. EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE (regla 1, segundo renglon)

**Recomputado al cierre y no copiado de la apertura.** Da **identico**, y **ese es el resultado
correcto**: esta vuelta no movio un nodo ni un veredicto.

| | apertura de la vuelta 46 | **al cierre, recomputado** | lo que lo movio |
|---|---|---|---|
| marcador | A 575, B 79, C 8, D 2.726, n 3.388 | **A 575, B 79, C 8, D 2.726, n 3.388** | **nada** |
| grafo | 3.853 / 3.524 / 329 / 16.898 | **3.853 / 3.524 / 329 / 16.898** | **nada** |
| cola de costuras | 1.494 sobre 3.524 | **1.494 sobre 3.524** | **nada** |
| operaciones | 71, dependencias rotas 0 | **71, dependencias rotas 0** | **nada** |
| congelados | 1 (el 1190) | **1 (el 1190)** | **nada** |

**Tasa por dominio, vara por tramo y figuras: NO se publican en esta vuelta, y se dice por que.**
Son cifras del **cribado**, y la campana esta en **ejecucion por fases** (regla 7: *por fase en la
ejecucion*). **El marcador no se movio**, asi que ninguna de esas cifras pudo moverse tampoco.

---

## 9. CORRECCIONES Y MANEJOS DECLARADOS, todos vistos ANTES de publicar

**Ninguno movio una cifra. Los cinco van con nombre y el texto viejo queda a la vista.**

1. **El emparejador contra el campo `preservar` daba 0 de 5, y eso NO era una ausencia: era el
   emparejador.** `preservar` es una **parafrasis en prosa**, en infinitivo y sin acentos; los pasos
   son imperativos con acentos. Corregido a **raices de 5 letras**: **3 de 5 mecanicos**, y **los
   dos que la parafrasis REORDENA van declarados como LECTURA MIA**, con los dos textos impresos uno
   al lado del otro. **5 de 5 cubiertos, 3 por mecanica y 2 por lectura declarada.**
2. **Buscar solo la frase `REGISTRO DE OPERACION HECHA` daba 5 de 9**, y eso tampoco era ausencia de
   registro: **esa frase se acuno en la vuelta 30**, y `OP-D-03`, `OP-D-04` y `OP-D-05` cerraron
   **antes**, con encabezado `CERRADA` o `SELLADA`. **Se miden LAS DOS FORMAS y se publican por
   separado, sin fundir una en otra.**
3. **Mi prueba de deprecacion usaba un campo `estado` que el nodo no tiene.** El campo real es
   `deprecado`, medido hoy: **presente en 329 ficheros y siempre `True`**. Corregido antes de contar.
4. **El campo `fuente` lleva un `|`, y un `|` crudo parte una tabla markdown en columnas falsas.**
   Visto en la corrida seca **antes de escribir nada**; escapado **en un solo sitio** del generador.
5. **La primera version del generador de la TAREA 1 pegaba la marca de linea al final de la celda** y
   **duplicaba la cita en tres filas**. Visto **antes de commitear**; la linea pasa a **columna
   propia** y el motivo queda escrito en el comentario del script.

**Y UN LIMITE DECLARADO, que no es correccion:** `OP-D-01` y `OP-D-02` **comparten una sola seccion**
en `02_DESTEJIDOS.md` (la de la vuelta 45, que las verifica juntas), asi que mi localizador las
apunta **a la misma linea**. **No son dos secciones contadas una vez.**

---

## 10. PENDIENTES DE DOCTRINA

**UNO, y es estrecho a proposito** (la mitad ancha la cubre el precedente de la seccion 5):

> **QUE PASA CON UN `depende_de` Y UN `preservar` QUE APUNTAN A UNA RUTA QUE OTRA FASE YA DESHIZO.**
> El plan tiene escrito como cerrar **un destejido consumido** (`OP-D-01`, `OP-D-03`, `OP-D-05`).
> **Lo que no tiene escrito es que hacer cuando lo consumido era ademas el CAMINO por el que una
> operacion posterior esperaba recibir un bloque**, y esa operacion posterior lo tiene escrito en
> dos campos y en una pagina de fronteras. **No invento la regla: registro lo mejor sostenido (el
> bloque esta entero, medido y enlazado), lo marco PENDIENTE DE DOCTRINA, y sigo**, que es lo que la
> regla 5 manda.

---

## 11. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Doce.** Cada uno con la rama que elegi y la cita con la que la elegi.

- **D1. NO EJECUTAR NINGUNA CIRUGIA.** El encargo mandaba simulacion, cirugia y caso positivo.
  **Yo no toque un nodo**, porque el corte ya estaba hecho. **Lo discutible es si eso es obediencia
  o incumplimiento.** Mi rama: **obediencia**, con el precedente de `OP-D-05` (seccion 5) y con la
  regla 4 del `EJECUTOR.md` delante.
- **D2. NO ESTRENAR LA PALABRA `OPERACION HECHA` PARA `OP-D-07`.** Las verificaciones 1 y 3
  **cumplen**; la 2 cumple **en su mitad material** y no en la diferida. **Podria defenderse que
  basta.** Mi rama: **no se estrena**, y si el auditor lee que basta, **se escribe en la vuelta
  siguiente con su acta detras**.
- **D3. DECLARAR LA PARADA EN VEZ DE TRATARLA COMO SIMPLE TRABAJO DIFERIDO DE LA FASE 03.** El acta
  de la 45 (linea 10.086) ya la llamaba **DEFERIDA**. **Lo discutible es si mi medicion la asciende
  a PARADA o si sigue siendo el mismo diferido de siempre.** Mi rama: **PARADA**, porque lo que mido
  no es que falte hacerlo, **es que la ruta escrita ya no existe**.
- **D4. AÑADIR EL PRECEDENTE DEBAJO DEL REGISTRO EN VEZ DE REESCRIBIR EL REGISTRO.** Mi rama: debajo
  y declarado, por *una correccion que tapa lo que corrige no se puede auditar*. **Se puede sostener
  que un registro que nace incompleto debio rehacerse entero.**
- **D5. NO ABRIR LA FASE 03 POR EL EMPATE A TRES EN EL CAMPO `orden`.** **Contra-argumento real:
  en la fase 02 el criterio NO era el campo `orden` sino CONGELADOS LIBERADOS** (adjudicado en el
  acta de la vuelta 44), asi que **puede que la fase 03 tenga tambien un criterio propio que yo no
  encontre y que deshaga el empate**. Mi rama: **no abrir**, porque el punto 6 del encargo manda no
  abrir cuando el orden **exige decidir**, y buscar un criterio no escrito es decidir.
- **D6. DECLARAR EL MARCADOR RANCIO DEL `00_INDICE` Y NO ARREGLARLO.** Mi rama: **declarar**. **Se
  puede sostener que con el instrumento ya escrito arreglarlo costaba una linea** y que dejarlo mal
  otra vuelta es peor. **Lo dejo porque reescribir una pagina que el encargo no me mando es
  ejecutar mas alla de lo escrito.**
- **D7. LA FORMA DE LOS TRES COMMITS, ADAPTADA.** El patron asentado es *lectura, cirugia, costuras*.
  **Sin cirugia lo cambie a** *lectura y hallazgo, ciclo verde y cierre medido, registro y parada*.
  **Se puede leer como que estrene una forma.**
- **D8. MEDIR LA APERTURA ANTES INCLUSO DE LA TAREA 1.** Mas estricto que lo pedido, con el
  precedente de la vuelta 45. **Nadie lo mando.**
- **D9. LEER LOS TRES PARES (843, 860, 1298) CUANDO LA OPERACION NO MANDA NINGUNA RELECTURA.** Los
  lei y **no movi ninguno**. **Se puede sostener que leer sin mandato es alcance que me tome.**
- **D10. CONTAR "8 DE 9 CON REGISTRO" FUNDIENDO DOS FORMAS DISTINTAS DE REGISTRO.** Las publico por
  separado en la tabla, **pero el total las suma**. **Se puede sostener que son varas distintas y
  que el total no deberia existir.**
- **D11. LOS DOS PASOS QUE NINGUNA MECANICA ADJUDICA, RESUELTOS POR LECTURA MIA DECLARADA.** Imprimo
  los dos textos y digo que estan reordenados y en infinitivo. **Es una lectura, no una medicion.**
- **D12. ATRIBUIR LA CIRUGIA A `OP-F-04-WEI` / `1eef1c6b`.** La evidencia son **tres**: `git log
  --follow`, `01_FUENTES.md` linea 982 y `INDICE_ROJO_DECLARADO.jsonl`. **Se puede pedir una cuarta.**

---

## 12. LAS PREGUNTAS QUE NO ADIVINO Y TRAIGO

1. **¿Se marca `OP-D-07` como HECHA?** Las verificaciones 1 y 3 cumplen medidas y la 2 cumple en su
   mitad material. **No lo decido yo.**
2. **¿Donde queda el lado del punto brillante de la frontera del 1298?** Tres ramas escritas y
   ninguna elegida: **(a)** se queda en `puntos_brillantes_antes_del_pivote` y la frontera se
   re-declara entre ese nodo y la puerta; **(b)** el bloque viaja al superviviente en el acto I y el
   nodo propio muere; **(c)** la frontera se re-declara entre otros dos nodos. **Es decision de la
   mesa `OP-M-03` y de la fase 03, con el expediente delante.**
3. **¿Cual es la primera operacion de la fase 03?** Tres empatadas en `orden` = 1 y ninguna pagina
   que las desempate. **¿Tiene la fase 03 un criterio propio, como la 02 tenia CONGELADOS
   LIBERADOS?**
4. **¿Quien rehace el marcador del `00_INDICE`, y con que instrumento?** Cuatro filas rancias
   medidas hoy, y la tabla de orden de fases repite el error en su celda de HECHO.

---

## 13. CONDICIONES DE PARADA, RECORRIDAS

| condicion | se cumple |
|---|---|
| **doctrina nueva** | **NO** para la cirugia (precedente escrito, seccion 5). **SI hay un PENDIENTE DE DOCTRINA estrecho**, seccion 10, registrado sin parar como manda la regla 5 |
| **contradiccion sin regla de correccion** | **SI, UNA**: la de la seccion 4. **Va como PARADA, escrita y sin arreglar** |
| **decision de fundador** | **NO**. `MIN_BLOQUE` intacto, cero contenido borrado, cero ramas fundidas, cero nodos tocados |
| **fallo tecnico repetido** | **NO**. Gate 0 en verde, tres suites en verde, cero rojos |
| **credito roto** | **NO** por mi parte: cero cifras publicadas sin medir en esta vuelta |
| **campana consumada** | **NO**. La fase 03 entera por delante |
| **credenciales** | no hicieron falta |

**EL BUCLE SIGUE**, con la PARADA de la seccion 4 y las cuatro preguntas de la seccion 12 sobre la
mesa del auditor.
