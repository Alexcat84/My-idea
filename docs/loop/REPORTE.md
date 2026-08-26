# REPORTE DE LA VUELTA 73: EL LOTE I DEL TRAMO UNICO DE `OP-U-02`, EL ULTIMO SIN DUENO, Y EL TRAMO SE QUEDA SIN NINGUN ACTO SIN DESTINO

**Fase III, ejecucion continua. Rama `pasada-unica`. 26 ago 2026.**

**FECHA POR DOS RELOJES, CORRIDOS POR MI:** el reloj del sistema da **2026-08-26** y `git log -1
--date=format` sobre el commit de apertura da **2026-08-26 07:12**. **Toda cifra de este reporte tiene
ese corte.** La vuelta abrio con el arbol limpio en `3e3f6683` y **no cruzo medianoche**.

**EL CONTADOR DE PARADA ENTRO A ESTA VUELTA EN CERO TANDAS** (acta 72, seccion 7, con las dos rachas
en cero y la de reporte por SEGUNDA tanda seguida). **Lo que este reporte trae para ese contador va
dicho de frente y no al final:** cero veredictos movidos, cero colisiones fabricadas, y **el marcador
identico al digito entre apertura y cierre, las catorce filas y las diez tasas**, comprobado por
`diff` entre las dos salidas del tallador de marcador. **Las averias propias de la vuelta son CUATRO y
ninguna llego a una cifra publicada** (seccion 7). **Y hay UNA COSA que este reporte declara en vez de
esconder, que es la mas cara de la vuelta y va la primera: EL `ACTO 50` SE FUNDIO CONTRA SU UNICA
VARA, porque esa vara apunta al nodo que LAS DOS RAZONES ESCRITAS DEL ACTO MATAN** (`D1`, con su
pendiente de doctrina nombrado en la seccion 8).

---

## 1. LA CABECERA, TALLADA Y NO TECLEADA

**Generada entera con** `python scripts/loop/tallar_cabecera_reporte.py --vuelta 73` y **pegada sin
tocar una celda** ([`SALIDA_V73_CABECERA.txt`](SALIDA_V73_CABECERA.txt)). **La celda que no salga de
un instrumento no se escribe.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.196 / 657 / 17.663 | **3.853 / 3.188 / 665 / 17.671** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 368 / 183 | **551 / 376 / 175** |
| actos (componentes) | 53 | **49** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 27 | **26 / 23** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 139 | **61 / 127** |
| cola de costuras | 1.440 | **1.438** |
| colisiones de clase vigentes | 7 | **7** |
| auto-pares (los dos lados al mismo vivo) | 282 | **286** |
| duplicadas historicas: grupos / nodos | 899 / 712 | **898 / 711** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (200 igual a 200; 183 igual a 183) | **TODAS OK (188 igual a 188; 175 igual a 175)** |

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION** (regla 1): los seis instrumentos de apertura
corrieron con el arbol limpio en `3e3f6683`, **antes de escribir nada**, y `git status --porcelain`
tras correrlos dio **CERO ficheros rastreados movidos** (solo las salidas nuevas, sin trackear).
**EL CIERRE SE RECOMPUTO AL CIERRE**, despues de que las cuatro fusiones y `run_phase1` movieran el
arbol.

**LA APERTURA DE HOY CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 72 PUBLICO** (marcador 551 / 72 / 5 /
2.760, grafo 3.853 / 3.196 / 657 con 17.663 enlaces, retrato 551 / 368 / 183, 53 componentes, 26 y 27
sobre 61 y 139, cola 1.440, colisiones 7, auto-pares 282, duplicadas 899/712, 71 `LISTA`, 672 entradas
y las cuatro comprobaciones en 200 y 183), **que es el contraste que la regla 2 permite**: entre las
dos vueltas nadie movio dato.

**LA ARITMETICA DEL SALTO ES COHERENTE ENTERA:** cuatro actos fundidos son **menos 4 componentes** (53
a 49), **menos 12 nodos abiertos** (139 a 127), **menos 8 vivos** (3.196 a 3.188) y **mas 8
deprecados** (657 a 665). El retrato sube 8 colapsos y baja 8 pares distintos (183 a 175), que es **un
par interno por acto colapsando a auto-arista**, y los auto-pares suben exactamente esos **4** (282 a
286). Las duplicadas bajan **1** por el resolutor. Los enlaces suben **8**.

> **LA COLA DE COSTURAS BAJA DOS, Y EL DELTA NO SE DEJA COMO UN MENOS DOS MUDO**, porque el
> instrumento la mide nodo a nodo ([`SALIDA_V73_COLA_DELTA.txt`](SALIDA_V73_COLA_DELTA.txt)): **ENTRAN
> DOS y SALEN CUATRO**. Los cuatro que salen son **absorbidos** que dejan de ser vivos
> (`new_view_vs_old_view_de_error_humano`, `perspectiva_dentro_del_tunel`,
> `valor_del_dinero_en_el_tiempo` y `valor_presente`); **los DOS que entran son supervivientes de este
> lote** (`investigacion_new_view` y `shadow_ia_organizacional`), **los dos que crecieron dos pasos**.
> **Es un costo y va nombrado**, que es la especie que el `D6` del acta 71 marco cuando el lote `G`
> metio tres. **El corte de esta medicion es `c584f060`, el commit del plan, que es PRE fusion.**

---

## 2. TAREA 1: EL REGISTRO DEL ACTA 72 Y LA UNICA CORRECCION DECLARADA

`python scripts/loop/vuelta73_registrar_acta72.py`
([`SALIDA_V73_REGISTRO_ACTA72.txt`](SALIDA_V73_REGISTRO_ACTA72.txt))

**`+260` lineas y CERO borradas** (`git show --numstat` sobre `1562faa9`: **`260 0`**), **73 agujas
derivadas y NINGUNA tecleada**, **tres agujas NEGATIVAS de sustancia en verde**, **idempotencia
MORDIENDO** (segunda corrida: *YA ADOSADA*, arbol limpio despues), y **el re-cotejo tras adosar mide
que las 73 sedes de arriba siguen en su linea**.

**LA MAQUINA SE COPIO POR EXTRACCION Y NO SE RETECLEO** (`_v73_construir_registrador_acta.py`): las
dos piezas copiadas (los imports y la maquina entera de la guarda de citas, 9 sub-piezas comprobadas
con `assert`) **aparecen LITERALES en el destino**, comprobado por el propio constructor. **La maquina
NO CRECE**: cero mecanismos nuevos, cero filas, cero columnas (adjudicacion 3 del acta 69).

> **LO QUE SE ANADE ES UNA SOLA CONSTANTE DE RUTA, Y BAJA DE TRES A UNA**: la vuelta 72 estreno TRES
> ficheros de aguja porque traia TRES correcciones, y su `D11` quedo `A FAVOR`. Esta vuelta trae UNA y
> anade UNA (`cuenta_agregada_de_perdidas.py`). **La ruta se anade cuando hay una sede que citar, no
> por costumbre**, y eso se dice porque una capacidad que se usa por inercia deja de ser una decision.
>
> **Y EL CORTE DE EXTRACCION DEL BLOQUE DE IMPORTS TUVO QUE CAMBIAR, Y VA DECLARADO EN VEZ DE
> CALLADO:** el constructor de la vuelta 72 cortaba en el comentario de `AGUJAS`, que en SU ancestro
> era la primera linea del bloque propio. En el MIO ya no lo es, porque el ancestro estreno rutas
> propias delante. Cortar ahi se habria llevado dos lineas de prosa ajena al bloque de imports. **El
> corte nuevo esta en el comienzo del bloque propio y se MIDE con un `assert` que ninguna de las tres
> rutas del ancestro se cuele.**

### 2.1 **CORRECCION DECLARADA, UNICA: LA GLOSA DE LA ESPECIE DEL PENDIENTE 4** (adjudicacion 1 del acta 72)

([`SALIDA_V73_CORRECCION_GLOSA_P4.txt`](SALIDA_V73_CORRECCION_GLOSA_P4.txt))

**El instrumento es de nombre estable** (`cuenta_agregada_de_perdidas.py`) **y por eso la correccion
va por el carril declarado**, el mismo que `generar_plan_del_lote.py` uso en las vueltas 63, 65 y 72:
**el texto viejo se queda entero, citado VERBATIM en el docstring, y no se tacha.** **`git diff
--numstat`: `33 0`, treinta y tres lineas anadidas y CERO borradas.**

| | medido por el propio instrumento antes de escribir |
|---|---|
| **el texto viejo, VERBATIM y sin tachar** | `la frase sellada ATENUANTE DECLARADO, las que ademas son de la ESPECIE DEL PENDIENTE 4, las que llevan ATENUANTE DECLARADO Y MEDIDO` |
| **la pista del vehiculo en `PISTAS_SIN_SELLO`** | sigue presente, **sin estrechar ni ensanchar** |
| **la definicion POR EL HECHO, escrita** | *una fila es de esta especie cuando LA SUSTANCIA QUE SE PIERDE LLEGA ENTERA DESDE OTRO ABSORBIDO DEL MISMO ACTO, sea el vehiculo un `APPEND` o un `INCISO`* |
| **el cuerpo (busqueda y aritmetica), IDENTICO byte a byte** | **SI**, comprobado comparando todo lo que va del final del docstring en adelante **antes de escribir**; si hubiera diferido, no habria escrito nada |
| **el caso positivo re-corrido despues** | **LAS CINCO MITADES EN VERDE** |

> **LA CORRECCION ES DE GLOSA Y NO DE MAQUINA, Y ESO SE MIDE EN VEZ DE PROMETERSE.** La constante de
> la frase sellada no se toca, la nomina sigue buscandola en el mismo campo, y la lectura contraria
> sigue sumando igual. **Lo unico que cambia es lo que el lector entiende**, y eso era exactamente el
> hueco: la vuelta 72 publico su celda en `0` **con una glosa que decia que en sustancia si habia
> una**, porque el nombre historico de la marca nombra un vehiculo.
>
> **Y SE ESCRIBE DENTRO DE LA PROPIA CORRECCION POR QUE LA TUPLA DE PISTAS NO SE TOCA**, que era la
> tentacion: esa tupla **no define la especie**, solo delata prosa de atenuante sin sello, y
> estrecharla o ensancharla **seria mover la busqueda**, que es justo lo que el encargo prohibe.

---

## 3. TAREA 2: EL LOTE I, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO

**SE DECLARARON CUATRO ACTOS Y 12 NODOS AL ABRIR, Y SE ENTREGO EL DESTINO DE LOS CUATRO.** **LOS
CUATRO CIERRAN FUNDIDOS Y NINGUNO CIERRA `DECLARADO`.**

| acto | cierra | **FORMA medida** | superviviente | quien decide |
|---:|---|---|---|---|
| **49** | **FUNDIDO** | `UNA SOLA VARA` | `shadow_ia_organizacional` | la vara de **pasos**, sola |
| **50** | **FUNDIDO** | `UNA SOLA VARA` | `investigacion_new_view` | **el ARCHIVO, contra la unica vara que habla** |
| **51** | **FUNDIDO** | `UNA SOLA VARA` | `metodo_valor_presente_neto` **(LA PUERTA)** | la vara de **pasos**, y la puerta y el cableado con ella |
| **53** | **FUNDIDO** | `TODAS DE ACUERDO` | `reconocimiento_al_desempeno` | **las dos varas de contenido**, al mismo lado |

**LOS DOS SALTOS VAN DECLARADOS CON SU CITA** (adjudicacion 2 del acta 69): el `acto 31` tiene dueno
medido (`OP-F-04-WEI` y `OP-S-04`) y el `acto 37` tambien (`OP-S-07`), **leidos hoy del fichero fijado
por maquina**; ninguno de los dos es una fusion de `OP-U-02`, asi que **saltarlos no rompe el prefijo
sin saltos**. **EL TOPE DE ESTE LOTE NO ES DE CUERDA NI DE ENCARGO: ES EL FINAL DE LA COLA SIN
DUENO.** Despues del `53` no queda ningun acto del tramo sin dueno y sin destino.

### 3.1 **`P.5`: EL ACTO LEIDO ENTERO, Y LA PREGUNTA CONTESTADA CON EL TEXTO ESTABLE**

**El acto se leyo ENTERO** con `python scripts/loop/dossier_del_tramo.py --tramo
docs/loop/TRAMO_UNICO_OPU02_V64.jsonl --actos 49,50,51,53`
([`SALIDA_V73_DOSSIER_LOTE_I.txt`](SALIDA_V73_DOSSIER_LOTE_I.txt), **248 lineas**): los **12** nodos
con sus pasos, condiciones, previos, siguientes y entregable, y **los 8 pares con su razon ENTERA sin
recortar**. **`P.5` contesta UNA FAMILIA en los cuatro**, y en el `51` **la propia razon escribe la
palabra FAMILIA con su nomina de tres dentro**, que es la contestacion mas fuerte posible: no es
lectura mia.

**MEDIDO** con `python scripts/loop/vuelta65_puentes_del_tramo.py --tramo ... --actos 49,50,51,53
--detalle` ([`SALIDA_V73_PUENTES_TRAMO.txt`](SALIDA_V73_PUENTES_TRAMO.txt)): **los cuatro son de 3
miembros con 2 pares `A`, 0 `D` y 1 sin veredicto, y los cuatro traen CERO nodos puente y CERO
triangulos**. **`P.10` no tiene sujeto en ninguno.**

### 3.2 **`P.8` EN ORDEN, Y TODA CIFRA DE CABLEADO DE LA COLUMNA `cab`**

`python scripts/loop/varas_n_arias_del_tramo.py --tramo ... --actos 49,50,51,53`
([`SALIDA_V73_VARAS_N_ARIAS.txt`](SALIDA_V73_VARAS_N_ARIAS.txt)). **Ninguna cifra de esta tabla esta
tecleada: las tres columnas salen del instrumento**, que es la unica fuente de cifra de cableado desde
la adjudicacion 3 del acta 70.

| acto | pasos | condiciones | **cableado (`cab`)** | forma | quien decide, por la letra |
|---:|---|---|---|---|---|
| **49** | apunta al superviviente, **4** contra 3 y 3 | **EMPATA** en 2 a tres bandas | **3 contra 2 y 2**, al OTRO lado | `UNA SOLA VARA` | la de pasos. **El cableado NO habla**, y su margen es de UNA arista |
| **50** | **EMPATA** en 5 entre los dos grandes | apunta a `new_view_vs_old_view_...`, **3** contra 2 y 2 | **EMPATA** en 5 entre los dos grandes | `UNA SOLA VARA` | **el ARCHIVO: las dos razones matan al nodo que la vara elige** |
| **51** | apunta al superviviente, **6** contra 5 y 4 | **EMPATA** en 3 | **10 contra 5 y 4**, al MISMO lado | `UNA SOLA VARA` | la de pasos, **con la puerta y el cableado de acuerdo** |
| **53** | apunta al superviviente, **5** contra 4 y 3 | apunta al superviviente, **3** contra 2 y 1 | **EMPATA** en 5 | `TODAS DE ACUERDO` | **las dos varas de contenido** |

> **LAS FORMAS MEDIDAS HOY CALZAN AL DIGITO CON LAS QUE EL ACTA 72 PUBLICO** para estos cuatro (49, 50
> y 51 `UNA SOLA VARA`; 53 `TODAS DE ACUERDO`) **y con la puerta que nombro** (el `51` con UNA, y
> ninguno con dos). **Es contraste, no fuente**: las cifras de arriba salen de mi corrida de hoy.

### 3.3 **EL `ACTO 50`: LA UNICA VARA APUNTA AL NODO QUE LAS DOS RAZONES MATAN, Y MANDA EL ARCHIVO**

**Es lo mas caro de esta vuelta y va con su choque entero, no en una nota al pie.**

| lo que dice cada fuente | a quien apunta |
|---|---|
| la vara de **pasos** | **EMPATA** en 5 entre `investigacion_new_view` y `new_view_vs_old_view_de_error_humano` |
| la vara de **condiciones**, la UNICA que habla | **`new_view_vs_old_view_de_error_humano`**, 3 contra 2 y 2 |
| el **cableado** | **EMPATA** en 5 entre los dos grandes; por la letra tampoco habla |
| la razon del puesto **2290** | cierra con *SOBREVIVE `investigacion_new_view`* |
| la razon del puesto **2292** | cierra con *SOBREVIVE `perspectiva_dentro_del_tunel`* |

**LAS DOS RAZONES MATAN AL MISMO NODO: el que la vara elige.** **Fundir a favor de la vara habria
desmentido DOS razones publicadas a la vez.**

**POR QUE MANDA EL ARCHIVO, CITADO Y NO IMPROVISADO.** **`P.8` dice que donde el contenido dice algo,
el contenido manda**, y define expresamente que **contenido no es solo el texto de los pasos**: un
**padre declarado por el archivo** es contenido, *con el mismo peso*. **Aqui el archivo declara
CONTENCION dos veces:** el **2290** escribe que el paso 1 del absorbido **ES** el paso 1 del otro y que
sus pasos 2, 3 y 5 son *formas de decir lo que el otro pide con instrumentos*, y remata con *le queda
una linea propia*; el **2292** escribe la misma contencion contra el tercero y remata con *le quedan
dos lineas*. **Un conteo de condiciones de 3 contra 2 no vence a una contencion declarada dos veces**,
y la letra del tramo lo dice por su lado: **`CHOCAN` decide LA PIEZA DECLARADA** (acta 53, pregunta 3).

**LA ELECCION ENTRE LOS DOS CORONADOS NO LA HACE MI LECTURA, LA HACEN LAS VARAS.** Las coronas son
**cruzadas y sobre SU propio par**, que es la figura que las actas 70, 71 y 72 adjudicaron `A FAVOR`
en su `D6`, su `D5` y su `D6`. **El par que falta, el unico sin veredicto del acto, es exactamente el
que enfrentaria a los dos coronados**, asi que el archivo no los compara y hay que medirlos:

| entre los DOS coronados | `investigacion_new_view` | `perspectiva_dentro_del_tunel` |
|---|---:|---:|
| pasos | **5** | 4 |
| condiciones | 2 | 2 (**EMPATA**) |
| cableado (`cab`) | **5** | 3 |

**Las dos varas que hablan apuntan al mismo, y ninguna apunta a `perspectiva_dentro_del_tunel`.** Y el
fondo lo confirma sin decidirlo: el entregable de `investigacion_new_view` es **el informe entero** y
el del otro es **una narrativa dentro de ese informe**.

> **PENDIENTE DE DOCTRINA, NOMBRADO Y NO INVENTADO:** ninguna regla escrita dice hoy que hacer cuando
> la FORMA que el instrumento imprime es `UNA SOLA VARA` **y esa vara apunta al nodo que las razones
> matan**. **El instrumento no lee razones y por eso no puede imprimir `CHOCAN`.** Registro lo mejor
> sostenido, **lo marco (`D1`)** y sigo, que es la regla 5 del `EJECUTOR`. **No estreno ninguna regla.**

### 3.4 **EL `ACTO 51`: LA PUERTA SOBREVIVE Y NO HAY NINGUN CHOQUE QUE PUBLICAR**

`metodo_valor_presente_neto` **es PUERTA** (universo protegido de **256** ids) **y SOBREVIVE**, que es
lo que el acta 54, pregunta 1, manda **gane o pierda en contenido**. **AQUI GANA, y se dice en vez de
darse por hecho:** la vara de pasos apunta a la puerta (6 contra 5 y 4) y el cableado tambien (10
contra 5 y 4). **NO HAY CHOQUE QUE ESCRIBIR EN EL MOTIVO SELLADO**, a diferencia del `acto 46` del
lote `H`, **y callarlo dejaria al lector sin saber si se miro**. **Es el unico acto del lote donde la
vara, el cableado y la puerta apuntan al mismo sitio.**

**Y ES EL REPARTO MAS BARATO DE TODO EL TRAMO:** el nodo **NO crece ni un paso** (6 pasos y 3
condiciones antes y despues), **cero `APPEND`** y **un solo `INCISO`**. El **1332** lo habia escrito
antes: *PERDIDA CERO Y DIRECCION FORZADA: el nodo que muere no tiene ni una linea propia*.

> **SE DICE ALGO QUE LA RAZON NO DIJO, PORQUE ESCUDARSE EN ELLA SERIA CALLAR:** el **1332** mide
> *perdida cero* sobre los **PASOS** de `valor_presente`, y es cierto al digito, **pero las condiciones
> de los dos absorbidos SI pierden**, y esas tres perdidas van selladas con su motivo. **Va marcado
> (`D5`).**

### 3.5 **EL `ACTO 53`: LA PROMESA DE MARCADO DE SU RAZON, CUMPLIDA Y ADEMAS DESACTIVADA**

El **2942** lleva escrito *DISCUTIBLE MARCADO fuerte* sobre la linea de `reconocimiento_crosby` de
**adaptar el reconocimiento a tu forma de trabajar con tu gente**, con esta frase: *quien la lea como
un paso entero propio dira D*. **Va marcada (`D6`).**

> **Y ESTE REPARTO LE QUITA EL FILO A LA PREGUNTA EN VEZ DE ESQUIVARLA:** esa linea **NO SE PIERDE**.
> Entra de `INCISO` al paso 3 del superviviente, **asi que se lea como paso o como linea, el contenido
> se conserva**. La pregunta sigue abierta como pregunta de doctrina; **el dato ya no depende de como
> se conteste.** **Es el segundo reparto del lote con CERO `APPEND`**, y tampoco es casualidad: las dos
> razones dicen que *ninguno trae un paso entero ajeno al otro*.

### 3.6 **EL BORDE DEL DUENO, MEDIDO ANTES DE SELLAR** (`_v73_borde_del_dueno.py`)

([`SALIDA_V73_BORDE_DEL_DUENO.txt`](SALIDA_V73_BORDE_DEL_DUENO.txt))

| | medido hoy por maquina |
|---|---:|
| entradas del inventario barridas, el fichero **ENTERO** | **672** |
| entradas que tocan a alguno de los **12** miembros | **6** |
| de ellas, de tipo `acto` | **6**, o sea **TODAS** |
| de ellas, de tipo **`familia_de_ids`** | **0** |
| **`familia_de_ids` que cubren la NOMINA ENTERA de un acto del lote** | **0** |
| miembros del lote en alguna nomina de `RACIMOS_MIEMBROS.jsonl` (32 lineas) | **0** |
| menciones en `OPERACIONES.jsonl`, barrido **CAMPO A CAMPO** sobre las 71 fichas | **0** |

**EL BORDE DE LA ADJUDICACION 2 DEL ACTA 71 NO SE PISA, Y ESTA VEZ NI SIQUIERA SE ACERCA.** **Las seis
entradas de tipo acto nombran en `operaciones` a `OP-L-03` y a `OP-U-02`**, que es la propia operacion
que funde, **y eso no hace dueno a nadie** por la adjudicacion 2 del acta 68: las tres fuentes que
hacen dueno son los campos `nodos`, `preservar` y `eliminar`, **y el barrido campo a campo no devuelve
ninguna**. **Es la figura del lote `G` y no la del `H`**, que trajo siete menciones en cuatro fichas.

### 3.7 **EL PLAN, SELLADO DOS VECES, CON EL DIFF MEDIDO CAMPO A CAMPO**

`python scripts/loop/generar_plan_del_lote.py --lote I --vuelta 73 --operacion OP-U-02 ...`
([`SALIDA_V73_SELLO_PLAN_1.txt`](SALIDA_V73_SELLO_PLAN_1.txt),
[`SALIDA_V73_SELLO_PLAN_2.txt`](SALIDA_V73_SELLO_PLAN_2.txt)). **El diff de los dos sellos es de UN
SOLO CAMPO** (`colisiones_esperadas`), **comprobado campo a campo y no solo por lineas**
([`SALIDA_V73_DIFF_SELLOS.txt`](SALIDA_V73_DIFF_SELLOS.txt): **2 lineas de diff, 1 campo distinto, y
el campo `actos` IDENTICO entre los dos**).

**EL NOMBRE DEL PLAN SALIO `PLAN_V73_OPU02_LOTE_I.json` SIN PASAR `--prefijo`**, que es la correccion
de la vuelta 72 mordiendo por segunda vez, **comprobado leyendo la linea `plan escrito` de la salida
antes de sellar**.

**LAS GUARDAS DEL GENERADOR, TODAS EN VERDE:** las cuatro fichas del lote; **guarda `1B`: ningun
absorbido es puerta**; **cobertura exacta** con marca UNICA por indice; **los SIETE `INCISO`
EXTRAIDOS del nodo y comprobados VERBATIM**, con su paso resultante impreso y **la tilde comprobada
leyendo los resultantes** (`información`, `señales`, `ecuación`, `cómo`, `tú solo`); **la guarda de la
JUNTURA ROTA** no salto en ninguno, porque **ninguno de los siete pasos receptores termina en punto**.

### 3.8 **LA FUSION, Y SUS GUARDAS**

`python scripts/loop/fundir_por_plan.py --plan docs/loop/PLAN_V73_OPU02_LOTE_I.json --ejecutar`
([`SALIDA_V73_FUSION_LOTE_I.txt`](SALIDA_V73_FUSION_LOTE_I.txt), simulada antes en
[`SALIDA_V73_FUSION_SIMULADA.txt`](SALIDA_V73_FUSION_SIMULADA.txt))

| | |
|---|---:|
| actos fundidos / declarados | **4** / **0** |
| nodos que **MUEREN** | **8** |
| vivos, antes y despues | **3.196** a **3.188** (delta deprecados **+8**, esperado **+8**: `OK`) |
| ficheros tocados | **30** |
| piezas repartidas | **47** (**4** enteras, **36** ya dichas, **7** de `INCISO`) |
| redirecciones sobre nodos vivos | **26** |
| **`P.16`**, duplicadas que la propia fusion fabrica | **7**, **limpiadas en la misma corrida** |
| auto-aristas que la fusion habria creado y se retiran | **2** |
| guarda `C`, campos que esta operacion NO redacta | **20 de 20 intactos** |
| guarda `D`, los absorbidos conservan su texto INTACTO | **`OK`**, los **8** |
| pasivo propio de la guarda `B` | **877** a **876** (la operacion lo BAJA en 1) |

**`P.16` RE-COMPROBADO POR SEPARADO:** `retirar_duplicada_por_resolutor.py --plan ...` corrido **tras**
la fusion dice **NINGUNA**, que es la idempotencia de la limpieza que el fundidor ya hizo.

**EL CRECIMIENTO, ACTO A ACTO, LEIDO DEL INSTRUMENTO:** el `49` de **4 pasos a 6**; el `50` de **5 a
7**; el `51` **de 6 a 6**; el `53` **de 5 a 5**. **Las condiciones no se mueven en ninguno de los
cuatro.** **DOS de los cuatro no crecen ni un paso**, que es la cifra mas baja de crecimiento del
tramo, y **es la contrapartida medida del `D3` del acta 72**, que anoto la tendencia de los nodos
grandes: **esta vuelta la tendencia no sube.**

### 3.9 **EL REANCLAJE, Y EL ANCLA DUPLICADA QUE NO SE FABRICO**

`python scripts/reanclar_por_resolutor.py`, **corrido ENTRE la fusion y `run_phase1`**
([`SALIDA_V73_REANCLAJE.txt`](SALIDA_V73_REANCLAJE.txt)): **NADA QUE RE-ANCLAR**, y **es un cero
medido y no un cero supuesto**: el fundidor ya habia redirigido **26** referencias vivas y **no quedo
ninguna fuera del grafo**.

> **LA LECCION DEL ACTA 71 SE APLICO AUNQUE EL REANCLAJE NO TOCARA NADA**, que es la unica forma de
> saber que no toco nada: el censo de anclas se re-corrio **despues** de la fusion
> ([`SALIDA_V73_ANCLA_TRAS_FUSION.txt`](SALIDA_V73_ANCLA_TRAS_FUSION.txt)) y midio **CERO anclas
> repetidas sobre los 49 rumbos**. **Ninguna se fabrico y por eso ninguna se limpio.**

### 3.10 **EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y CON LA APERTURA SACADA DE `git`**

`python scripts/loop/diff_duplicadas_por_resolutor.py --antes <git show c584f060:...> --despues
docs/plan/ARISTAS_DUPLICADAS.jsonl`
([`SALIDA_V73_DIFF_DUPLICADAS.txt`](SALIDA_V73_DIFF_DUPLICADAS.txt)).

> **GRUPOS FABRICADOS DE VERDAD: `0`.** **RENOMBRADOS: `0`.** **GRUPOS QUE DESAPARECEN: `0`.** Los
> grupos **por rotulo crudo** bajan de **899** a **898**, y **los grupos ya RESUELTOS son 898 en los
> dos cortes**: lo que cambia es el rotulo, no el conjunto. **Las 7 duplicadas que la propia fusion
> fabrico se limpiaron en la misma corrida por `P.16`**, y por eso el diff no las ve.

**EL CORTE DE *ANTES* SALE DE `git show` SOBRE EL COMMIT DEL PLAN** (`c584f060`), **anterior a la
fusion**, y el de *despues* es el fichero **tras recompilar el grafo con `run_phase1`**.

### 3.11 **EL CENSO DE COLISIONES: ESTE LOTE NO FABRICA NINGUNA, Y SE PUBLICA IGUAL**

`python scripts/loop/vuelta65_colisiones_esperadas.py --plan docs/loop/PLAN_V73_OPU02_LOTE_I.json`
([`SALIDA_V73_COLISIONES_ESPERADAS.txt`](SALIDA_V73_COLISIONES_ESPERADAS.txt)), **corrido sobre el
arbol de antes y simulando en memoria, sin tocar un nodo**.

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **7** |
| **colisiones NUEVAS que la fusion fabricaria** | **0** |
| colisiones que desaparecerian | **0** |
| **ESPERADAS TRAS FUNDIR** | **7** |
| **MEDIDAS al cierre por el censo** | **7** |
| **`CALZA`** | **`SI`** |
| auto-pares: **NUEVOS predichos** y **medidos al cierre** | **4** nuevos predichos (282 a 286) y **286** medidos |

> **LA BASE ENTRO POR EL DEFECTO DEL INSTRUMENTO, QUE ES LO QUE LA VUELTA 71 DEJO EN `7`**: no hizo
> falta pasarla a mano, **y la guarda la MIDIO sobre el arbol antes de usarla**. **TERCER LOTE SEGUIDO
> DEL TRAMO QUE NO FABRICA NINGUNA COLISION.** **Las dos de la mesa `OP-M-03` y las CINCO de `OP-U-02`
> ya publicadas siguen vigentes con su duena y no se tocan.**

### 3.12 **GATE 0 CON SU CICLO DE TRES, Y NO DE CUATRO**

| paso | resultado |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, todos los chequeos en `[OK]`; universo **3.188 activos / 665 deprecados**; alcanzabilidad **100,0 por ciento** (3.188/3.188, 85 semillas validas) |
| `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas** re-aplicadas |
| `python scripts/sync_assets_web.py` | **6 assets** mas `manifest.json` |
| **una cuarta corrida** | **NO SE HIZO** |

**LAS TRES SUITES, CORRIDAS POR MI:** motor **25/25**
([`SALIDA_V73_SUITE_MOTOR.txt`](SALIDA_V73_SUITE_MOTOR.txt)); web **80 ficheros, 1.030 pasadas, 3
saltadas** ([`SALIDA_V73_SUITE_WEB.txt`](SALIDA_V73_SUITE_WEB.txt)); `tsc --noEmit` **CERO lineas**
([`SALIDA_V73_TSC.txt`](SALIDA_V73_TSC.txt)). **Y el guardian de commit las volvio a correr en verde
en los cuatro commits de trabajo de esta vuelta.**

### 3.13 **EL REGISTRO EN `03_FUSIONES.md`** (`+463` lineas, `0` borradas)

`python scripts/loop/vuelta73_registro_lote_i.py`
([`SALIDA_V73_REGISTRO_LOTE_I.txt`](SALIDA_V73_REGISTRO_LOTE_I.txt)), **bajo la cabecera de tramo que
la vuelta 65 adoso** (derivada hoy por aguja) y **sin reescribir ni una linea de arriba** (`git show
--numstat` sobre `7f07d02f`: **`463 0`**). **14 agujas derivadas, ninguna tecleada**, **idempotencia
MORDIENDO**, y **las 14 sedes de arriba siguen en su linea** tras adosar.

**LA MAQUINA DE TABLAS SE COPIO POR EXTRACCION** (`_v73_construir_registro_lote.py`): `tabla_reparto`,
`tabla_por_absorbido` **y `tabla_declarado` aparecen LITERALES** en el destino. **Esta vuelta puede
comprobar `tabla_declarado` ENTERA, a diferencia de la 72, porque no la corrige**, y ademas comprueba
**por AUSENCIA** que la coletilla que aquella vuelta corrigio **no reaparece**. **DOS cambios
declarados y solo dos:** el fichero del tallador de perdidas, y **`MOTIVO_SELLADO` que vuelve a estar
VACIO** porque este lote no declara ningun acto.

> **`tabla_declarado` NO SE BORRA AUNQUE NO SE LLAME, Y SE DICE POR QUE:** borrarla seria **ENCOGER**
> la tabla, y la adjudicacion 3 del acta 69 lo prohibe tanto como hacerla crecer. **El proximo
> declarado la necesitara.**

---

## 4. LA CUENTA AGREGADA DE LAS PERDIDAS, POR MAQUINA Y CON LA DEFINICION CORREGIDA

`python scripts/loop/cuenta_agregada_de_perdidas.py --plan docs/loop/PLAN_V73_OPU02_LOTE_I.json`
([`SALIDA_V73_CUENTA_ATENUANTES.txt`](SALIDA_V73_CUENTA_ATENUANTES.txt))

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **18** |
| de ellas `DE PARAMETRO DE PASO` | **6** |
| de ellas `DE CONDICIONES` | **12** |
| **filas con `ATENUANTE DECLARADO`** | **1** |
| de ellas, de la **especie del pendiente 4**, medida con la **definicion CORREGIDA de esta vuelta** | **0** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **1** |
| **filas con DOS SEDES en el campo `donde`** | **5** |
| **filas que describen un atenuante SIN la frase sellada** | **NINGUNA**, medido: **CERO exclusiones que declarar** |
| la aritmetica de **la lectura contraria** (una fila por SITIO y no por PIEZA) | **23** y no **18** |

> **LA CELDA DEL PENDIENTE 4 SALE EN `0` Y AHORA ESA CIFRA SIGNIFICA ALGO DISTINTO QUE HACE UNA
> VUELTA.** La 72 la publico en cero **con una glosa que decia que en sustancia si habia una**, porque
> el instrumento buscaba el VEHICULO. **Con la definicion corregida de esta misma vuelta la cuenta se
> hizo contra el HECHO, fila a fila, y sigue dando `0`**: en ninguna de las 18 la sustancia perdida
> llega entera desde otro absorbido, ni por `APPEND` ni por `INCISO`.
>
> **LA UNICA QUE SE ACERCO LLEVA SU `ATENUANTE DECLARADO Y MEDIDO` Y LLEVA ESCRITO DENTRO POR QUE NO
> ENTRA:** es la prohibicion explicita de vocabulario del `acto 50`. **Lo que llega por el `INCISO` al
> paso 4 es LA POSTURA** (*honrar la experiencia humana en lugar de reducirla a una lista de errores*);
> **lo que se pierde es LA LISTA DE PALABRAS**. **Una pieza vecina no es la misma pieza**, y la
> definicion nueva sirve justamente para poder decir que no con una vara y no con una impresion. **Va
> marcado (`D8`).**

**LAS CINCO FILAS CON DOS SEDES SON LA CIFRA MAS ALTA DEL TRAMO**, y va con su motivo: la fila del
contrato es **por PIEZA que se pierde y no por sitio donde vivia** (acta 67, `D10`), y en este lote
**los dos absorbidos de un mismo acto traen la misma pieza mas veces que en ningun lote anterior**,
porque los tres miembros de cada acto son del mismo libro y describen el mismo gesto. **Va marcado
(`D9`).**

---

## 5. LO QUE ESTA VUELTA APRENDIO DE UNA FRASE SELLADA ESCRITA DENTRO DE UNA NEGACION

**La primera redaccion de la fila del atenuante del `acto 50` escribia, dentro del campo `que`, la
frase `ESPECIE DEL PENDIENTE 4` PARA NEGARLA:** *y se dice por que NO ES DE LA ESPECIE DEL PENDIENTE
4...*. **El instrumento busca esa frase DENTRO de ese campo, y la conto como POSITIVA: publico `1`
donde la verdad es `0`.**

**La cazo el propio instrumento, corrido sobre el plan ANTES de commitear el plan y antes de tocar un
nodo.** **Corregido reescribiendo la fila sin la frase**, y **diciendo dentro de la propia fila por
que no se escribe**, para que el proximo que la lea no la vuelva a meter. **El plan se re-sello
entero** (no estaba ejecutado ni committeado: **re-sellar aqui es legitimo y no choca con el `D15` del
acta 68**, que habla de planes YA EJECUTADOS).

> **LA LECCION ES DE LA MISMA FAMILIA QUE LA DEL ACTA 64, PREGUNTA 6, PERO AL REVES:** alli una
> promesa **invisible** era peor que una incumplida; **aqui una negacion resulto VISIBLE para una
> maquina que solo sabe buscar la cadena.** **Una frase sellada no se puede escribir dentro de una
> negacion en el campo donde el instrumento la busca**, y eso queda dicho en el propio contenido del
> lote. **Va marcado (`D7`).**

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D1` . EL `ACTO 49` Y EL `ACTO 50` DEL LOTE `I` VAN LOS DOS AQUI, Y EL `50` ES EL CARO: SE FUNDIO
CONTRA LA UNICA VARA QUE HABLA.** La de **condiciones** apunta a `new_view_vs_old_view_de_error_humano`
(3 contra 2 y 2), **y las DOS razones escritas del acto matan a ese nodo**. Fundi a favor de
`investigacion_new_view` **por `P.8`** (el contenido manda, y una contencion declarada por el archivo
ES contenido, *con el mismo peso*, segun su propia tabla) **y por la letra `CHOCAN` decide la pieza
declarada** (acta 53, pregunta 3), **eligiendo entre los dos coronados con las varas restringidas a
ellos** (pasos 5 contra 4 y cableado 5 contra 3, las dos al mismo). **La lectura contraria:** que la
FORMA que el instrumento imprime es `UNA SOLA VARA`, que la letra dice `UNA SOLA VARA BASTA`, y que
tratarla como si fuera `CHOCAN` es estrenar doctrina sobre un acto en vez de traerlo como pregunta.
**No pare porque las dos lecturas se apoyan en reglas escritas y ninguna es doctrina nueva, y porque
fundir al reves habria desmentido dos razones publicadas.** **La pregunta concreta va en la seccion
8.**

**`D2` . EL `ACTO 49` FUNDE CONTRA UN CABLEADO DE 3 A 2 Y 2.** La unica vara que habla es la de
**pasos** (4 contra 3 y 3) y el cableado apunta a `shadow_ai_use_organizacional`. **Es la misma forma
que el `D2` del acta 72 (el `acto 43`) y el `D4` del acta 71 (el `acto 42`), las dos `A FAVOR` con las
palabras UNA SOLA VARA BASTA.** **Lo que lo hace distinto y por eso va marcado igual: el margen es de
UNA SOLA ARISTA**, el mas estrecho del tramo. **La lectura contraria:** que un margen de uno es ruido
en las dos direcciones y que un acto asi merece mirarse dos veces antes de fundir.

**`D3` . SALVE UN `APPEND` QUE NINGUNA RAZON DECLARA PROPIO.** El paso 2 de
`shadow_ai_use_organizacional` (*realizar encuestas anonimas para detectar el nivel real de adopcion*)
entra de `APPEND` **y ninguna de las dos razones del `acto 49` lo nombra**. **Mi vara, escrita entera:
es el UNICO instrumento de MEDIDA de los tres nodos**, ninguno de los otros seis pasos mide nada, y
**el entregable de ese absorbido es literalmente un *diagnostico del uso real (visible y oculto) de
IA***, que sin ese paso no lo produce nadie. **La lectura contraria:** que un `APPEND` que ninguna
razon declara propio es el ejecutor decidiendo contenido, y que el carril conservador era sellarlo
como perdida.

**`D4` . UNA PIEZA DECLARADA PROPIA COMPITIO POR EL UNICO `INCISO` DEL PASO 1 DEL `ACTO 50` Y LA OTRA
SE SELLO.** Al paso 1 solo cabe un `INCISO` (acta 64) y competian **reconstruir la informacion y las
senales disponibles** (que el **2292** declara propia) y **la enumeracion del contexto** (que las
razones declaran **mutuamente cubierta**). **Salve la declarada propia y selle la otra.** **La lectura
contraria:** que la enumeracion del contexto es lo unico que dice QUE hay que documentar, y que
perderla vacia el gesto que queda.

**`D5` . SELLE TRES PERDIDAS DE CONDICIONES EN UN ACTO CUYA RAZON DICE *PERDIDA CERO*.** El **1332**
escribe *PERDIDA CERO Y DIRECCION FORZADA* sobre el `acto 51`. **Lo mide sobre los PASOS y es cierto
al digito**; las condiciones de los dos absorbidos si pierden, **y las selle con su motivo en vez de
escudarme en la frase de la razon**. **La lectura contraria:** que sellar perdidas donde el archivo
escribio *perdida cero* contradice una razon publicada. **La lectura por la que fui:** que callarlas
seria la degradacion muda, y que la razon acota su propio alcance.

**`D6` . EL `ACTO 53` TRAIA UNA PROMESA DE MARCADO EN SU RAZON Y LA CUMPLO AQUI.** El **2942** dejo
escrito *DISCUTIBLE MARCADO fuerte* sobre la linea de `reconocimiento_crosby` de **adaptar el
reconocimiento a tu forma de trabajar con tu gente**: *quien la lea como un paso entero propio dira
D*. **Queda marcada.** **Y el reparto la salva de `INCISO`**, asi que **el dato no depende de como se
conteste la pregunta**. **La lectura contraria:** que si esa linea es un paso propio, el acto no era
`TODAS DE ACUERDO` sino un acto con propio de un solo lado, y eso cambia la vara.

**`D7` . ESCRIBI LA FRASE SELLADA DEL PENDIENTE 4 DENTRO DE UNA NEGACION Y EL INSTRUMENTO LA CONTO
COMO POSITIVA.** Seccion 5. **La cazo el propio instrumento antes de commitear el plan y antes de
tocar un nodo**, y la fila se reescribio. **La lectura contraria:** que reescribir el contenido de un
lote despues de haberlo generado es editar un modulo de contenido, que la adjudicacion 4 del acta 71
prohibe. **La lectura por la que fui:** que aquella adjudicacion habla del modulo de una vuelta
**PASADA**, y este es de la mia y no estaba ni sellado en firme ni ejecutado.

**`D8` . LA UNICA FILA CON ATENUANTE DE ESTE LOTE NO ENTRA EN LA CUENTA DEL PENDIENTE 4, Y LO DECIDI
YO CON LA DEFINICION NUEVA DELANTE.** Lo que llega por el `INCISO` es **la postura**; lo que se pierde
es **la lista de palabras prohibidas**. **La lectura contraria:** que las dos son la misma pieza
partida (no escribir *fallaron en* y honrar la experiencia humana son el mismo mandato dicho de dos
maneras), y que la fila si era de la especie. **Fui por la lectura estrecha porque la definicion nueva
pide que la sustancia llegue ENTERA.**

**`D9` . CINCO FILAS CON DOS SEDES ES LA CIFRA MAS ALTA DEL TRAMO, Y LA VUELTA ANTERIOR TUVO CERO.**
**La lectura contraria:** que agrupar dos sitios en una fila esconde la mitad del costo y que la
lectura por SITIO (23) es la honesta. **La vara: el `D10` del acta 67 descarto esa lectura y el
instrumento publica las dos cifras**, asi que nadie tiene que recontar.

**`D10` . EL LOTE CIERRA CON CERO `DECLARADOS` Y ESO NO SE PARECE A NINGUN LOTE RECIENTE.** El `H`
cerro uno y el `E` otro. **Aqui los cuatro motivos sellados posibles se recorrieron uno a uno y
NINGUNO tuvo sujeto.** **Lo digo porque un lote sin declarados puede leerse como un lote que no miro,
y la unica defensa es la tabla del recorrido**, que esta en el registro. **La lectura contraria:** que
cuatro actos seguidos sin ningun freno es estadisticamente el momento de sospechar del propio criterio.

**`D11` . LOS DOS SUPERVIVIENTES QUE CRECEN ENTRAN A LA COLA DE COSTURAS.** `investigacion_new_view` y
`shadow_ia_organizacional`, los dos que pasan de 4 a 6 y de 5 a 7 pasos. **Es el costo que el `D6` del
acta 71 marco cuando el lote `G` metio tres.** **La lectura contraria:** que meter en la cola de
costuras a los nodos que la propia fusion engorda es fabricar trabajo para la fase 04. **La vara: la
cola CITA, no juzga, y el delta esta medido nodo a nodo.**

**`D12` . EL REGISTRO DEL LOTE NO LLAMA A `tabla_declarado` Y AUN ASI LA COPIA ENTERA.** Sostengo que
borrar una funcion de tabla que este lote no usa seria **ENCOGER** la tabla, y la adjudicacion 3 del
acta 69 lo prohibe igual que hacerla crecer. **La lectura contraria:** que codigo que no se ejecuta en
esta vuelta es codigo sin probar, y que arrastrarlo es arrastrar deuda. **Lo comprobe por dos vias:
que aparece LITERAL y que la coletilla corregida en la vuelta 72 no reaparece.**

**`D13` . LOS DOS MOTIVOS SELLADOS DEL `50` Y DEL `53` PROMETEN MARCADO SIN LA FRASE QUE EL INSTRUMENTO
BUSCA.** El del `50` dice *lo marco DISCUTIBLE* y el del `53` dice *va marcada en la seccion 6*, y
**ninguna de las dos formas es una de las TRES que `comprobar_promesas_de_marcado.py` reconoce**. **El
instrumento midio DOS promesas y las dos son del `acto 49`.** **Las marcas estan igual (`D1` y `D6`),
asi que ninguna promesa se incumple en sustancia**, pero **la guarda no las vio**, que es exactamente
*la promesa invisible* del acta 64, pregunta 6. **El plan esta EJECUTADO y NO se re-sella** (acta 68,
`D15`). **Lo declaro aqui y va en la seccion 8 como pendiente.**

---

## 7. LAS AVERIAS PROPIAS, CAZADAS ANTES DE UNA CIFRA PUBLICADA

**CERO de ellas llego a una cifra publicada ni a un dato movido**, y **las CUATRO las cazo un
instrumento.**

### 7.1 **ESCRIBI LA FRASE SELLADA DEL PENDIENTE 4 DENTRO DE UNA NEGACION**

Seccion 5 entera. **El instrumento de la cuenta agregada publico `1` donde la verdad es `0`**, y lo
publico **sobre el plan y antes de commitearlo**. Corregido reescribiendo la fila; **el plan se
re-sello, el diff de sellos se rehizo y la cuenta bajo a `0`**. **Cero nodos tocados en medio.**

### 7.2 **TECLEE SIETE CIFRAS EN NEGRITA EN EL TEXTO DEL REGISTRO DEL LOTE**

`672`, `12`, `6`, `32`, `71`, `49` y `47`. **La red ancha de la guarda de citas cayo en `ROJO` sobre
`672`** (*el texto escribe `672` en negrita y ni sale de una aguja ni esta en `NUMEROS_DECLARADOS`*)
**y NO escribio nada**, que es para lo que esta. Corregido **anadiendo ONCE celdas que se leen POR
AGUJA** de `SALIDA_V73_BORDE_DEL_DUENO.txt`, `SALIDA_V73_ANCLA_TRAS_FUSION.txt` y
`SALIDA_V73_TRAMO_CIERRE.txt`. **Las otras seis eran de menos de tres digitos y la red no las alcanza:
las derive igual, y eso se dice porque la guarda no me obligaba.**

### 7.3 **CORRI LA SUITE DEL MOTOR CON EL COMANDO EQUIVOCADO**

`python -m pytest engine/tests` cayo en **`No module named pytest`**. **El comando de la casa es
`python engine/run_all_tests.py`**, que es el que el propio guardian de commit usa, **y lo comprobe
leyendo `.githooks/pre-commit` en vez de adivinando otro**. **La salida vacia se sobreescribio con la
buena antes de commitear nada.**

### 7.4 **EL CORTE DE EXTRACCION HEREDADO HABRIA METIDO PROSA AJENA EN EL BLOQUE DE IMPORTS**

El constructor de la vuelta 72 cortaba el bloque de imports en el comentario de `AGUJAS`. **En mi
ancestro ese comentario ya no es la primera linea del bloque propio**, porque la vuelta 72 estreno
tres rutas delante. **Lo vi leyendo el ancestro antes de correr nada**, no despues. Corregido cortando
en el comienzo del bloque propio **y anadiendo un `assert` que MIDE que ninguna de las tres rutas del
ancestro se cuela**.

> **LAS CUATRO MURIERON ANTES DE UNA CIFRA PUBLICADA**, y **dos de las cuatro las cazo un instrumento
> cayendo en `ROJO` sin escribir**, que es la diferencia entre una averia y una caida. **La 7.3 la
> cazo `argparse` del interprete y la 7.4 una lectura hecha a tiempo.**

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **NUEVA, Y ES LA DE ESTA VUELTA: QUE MANDA CUANDO LA FORMA ES `UNA SOLA VARA` Y ESA VARA APUNTA AL
   NODO QUE LAS RAZONES MATAN?** El `acto 50`. **El instrumento no lee razones y por eso no puede
   imprimir `CHOCAN`**, asi que la FORMA sale `UNA SOLA VARA` y su letra dice que BASTA; pero `P.8`
   dice que **una contencion declarada por el archivo es contenido con el mismo peso** y la letra del
   tramo dice que **`CHOCAN` decide la pieza declarada**. **La pregunta concreta: cuando la vara y la
   razon escrita apuntan a lados distintos, es un `CHOCAN` que el instrumento no sabe ver, o es una
   `UNA SOLA VARA` que hay que obedecer?** **Fui por la primera lectura, va marcado (`D1`) y no
   invente regla.**
2. **NUEVA: UNA FRASE SELLADA NO SE PUEDE ESCRIBIR DENTRO DE UNA NEGACION EN EL CAMPO DONDE EL
   INSTRUMENTO LA BUSCA.** Seccion 5 y `D7`. **La pregunta concreta: esto es una regla practica de
   redaccion que basta con dejar escrita, o el instrumento deberia distinguir una negacion de una
   afirmacion?** **Lo segundo seria maquina nueva y no la estreno.**
3. **NUEVA: LAS TRES FORMAS QUE `comprobar_promesas_de_marcado.py` RECONOCE NO CUBREN *LO MARCO
   DISCUTIBLE* NI *VA MARCADA EN LA SECCION 6*.** `D13`. **La pregunta concreta: se ensancha el
   instrumento una cuarta vez, o se escribe la regla de que el motivo sellado use SIEMPRE una de las
   tres formas?** **No lo decido: el instrumento es de nombre estable y ensancharlo sin encargo es lo
   que la adjudicacion 3 del acta 69 mira de cerca.**
4. **EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE** (heredado): los **QUINCE** declarados siguen
   esperando el cierre de la fase 03. **Ya no puede crecer por `P.10` en este tramo**, medido: **cero
   puentes en los 2 que quedan**.
5. **EL `ACTO 44` COMO ESPECIE PROPIA** (heredado, adjudicacion 3 del acta 72): entra **NOMBRADO
   APARTE** en el paquete del cierre de la fase 03. **Esta vuelta no lo toca, no decide su salida y
   deja el dato medido**: sus tres nodos siguen vivos.
6. **LA MARCA PARA *YA LO DICE EL `APPEND` DE UN HERMANO*** (heredado): **esta vuelta NO la paga ni
   una vez**, medido con la definicion corregida. **Lo que sigue sin existir es la marca propia**, no
   su definicion, que esta vuelta escribio.
7. **EL `INCISO` DE CONDICIONES SIGUE SIN EXISTIR** (heredado): **doce perdidas `DE CONDICIONES`** en
   esta vuelta, **dos tercios del total y la cifra mas alta del tramo**, enrutadas a la fase 04 por el
   carril del acta 55, pregunta 5.
8. **EL ESQUEMA DE `OPERACIONES.jsonl`** (heredado): sigue pendiente, y **esta vuelta NO toca ninguna
   ficha** (`git diff --numstat` sobre `OPERACIONES.jsonl`: vacio).

---

## 9. RUTAS TOCADAS Y CENSOS AL CIERRE

**Del grafo (30 ficheros):** los **cuatro supervivientes** (`shadow_ia_organizacional`,
`investigacion_new_view`, `metodo_valor_presente_neto`, `reconocimiento_al_desempeno`), sus **ocho
absorbidos** (`incentivos_transparencia_ia`, `shadow_ai_use_organizacional`,
`new_view_vs_old_view_de_error_humano`, `perspectiva_dentro_del_tunel`, `valor_del_dinero_en_el_tiempo`,
`valor_presente`, `reconocimiento`, `reconocimiento_crosby`), los **redirigidos** (26 referencias sobre
nodos vivos), mas `dataset/metadata/master_graph.json` y `dataset/metadata/phase1_run_log.json`
(**32 ficheros de `dataset/` en total**, contados por maquina sobre el commit de la fusion). **NI UN
NODO DEL `ACTO 44` NI DE LOS OTROS CATORCE DECLARADOS SE TOCO.**

**Del registro:** `docs/plan/03_FUSIONES.md` (**`+260`** del acta 72 y **`+463`** del lote `I`, **cero
borradas en los dos**), `docs/plan/ARISTAS_DUPLICADAS.jsonl`, `docs/COSTURAS_INTERNAS.jsonl` y su
resumen, y `web/lib/assets/` por el `sync`. **`docs/plan/INVENTARIO.jsonl`,
`docs/RACIMOS_MIEMBROS.jsonl` y `docs/plan/OPERACIONES.jsonl` NO se tocaron** (`git diff --numstat`
sobre los tres: vacio).

**Instrumentos nuevos (OCHO, contados por maquina con `git diff --name-status --diff-filter=A
3e3f6683..HEAD -- scripts/`): NINGUNO de nombre estable**, los ocho son de vuelta:
`_v73_construir_registrador_acta.py`, `_v73_texto_acta72.py`, `vuelta73_registrar_acta72.py`,
`_v73_borde_del_dueno.py`, `_v73_lote_i.py`, `_v73_construir_registro_lote.py`,
`_v73_texto_lote_i.py` y `vuelta73_registro_lote_i.py`. **Y UN SOLO instrumento de nombre estable se
MODIFICO**, contado por la misma via (`--diff-filter=M`): **`cuenta_agregada_de_perdidas.py`**, por la
**CORRECCION DECLARADA** de la `TAREA 1`. **Esta vuelta NO crea ningun instrumento de medida de nombre
estable.**

| censo al cierre | valor |
|---|---|
| **barrido de titulos** ([`SALIDA_V73_BARRIDO.txt`](SALIDA_V73_BARRIDO.txt)), **re-corrido AL CIERRE** | **487 ficheros**, `ROJO` **32** (**linea base heredada, EN SU SITIO**), **`AMBAR` 0**, `ROTULADO` **56**, `CENSO` **225**, `ILEGIBLE` **1** |
| **censo de plantillas talladas** ([`SALIDA_V73_CENSO_PLANTILLAS.txt`](SALIDA_V73_CENSO_PLANTILLAS.txt)) | **CERO TALLADOS** sobre **26** instrumentos de nombre estable |
| **estado de las operaciones** ([`SALIDA_V73_CIERRE.txt`](SALIDA_V73_CIERRE.txt)) | **71**, todas `LISTA`, **0** dependencias rotas, **672** entradas, enlaces **17.671** |
| **casos positivos** ([`SALIDA_V73_CASOS_POSITIVOS.txt`](SALIDA_V73_CASOS_POSITIVOS.txt)) | **SEIS, y los seis sobre sujetos que esta vuelta NO toca**: mesa **LAS NUEVE** sobre `OP-M-02-ACCLIMATE`; contrato de perdidas **LAS CUATRO**; varas **LAS TRES mitades**; promesas **LAS DOS mitades**; **cuenta agregada LAS CINCO mitades, que esta vuelta mira con mas cuidado porque su `TAREA 1` corrigio ese instrumento**; y el del generador |
| **promesas de marcado** ([`SALIDA_V73_PROMESAS.txt`](SALIDA_V73_PROMESAS.txt)), **cotejadas por maquina ANTES de sellar este reporte** | **2 de 2 CUMPLIDAS**, cero incumplidas: las dos son del `acto 49` y **la seccion 6 lo nombra** |
| **cabecera del reporte** ([`SALIDA_V73_CABECERA_COMPARADA.txt`](SALIDA_V73_CABECERA_COMPARADA.txt)) | **`CABECERA: IDENTICA AL TALLADOR`**, **14** filas cotejadas, **DISTINTAS 0**, ausentes **0** |
| **codificacion de las salidas** ([`SALIDA_V73_CENSO_CODIFICACION.txt`](SALIDA_V73_CENSO_CODIFICACION.txt)) | **52** ficheros `V73` de `docs/loop` barridos por maquina (47 `txt`, 4 `jsonl`, 1 plan), **CERO fuera de `UTF-8` estricto**, con **la nomina entera impresa para que la cifra se pueda recontar**, y **ninguno se toco despues de generarse** (adjudicacion 5 del acta 71 aplicada desde el primer minuto con `PYTHONIOENCODING=utf-8`) |

> **EL `ROTULADO` SUBE DE 54 A 56 Y NO SE DEJA COMO UN NUMERO QUE CAMBIA SOLO:** son **los dos rotulos
> de los dos ficheros nuevos que los llevan** (`vuelta73_registrar_acta72.py` y
> `vuelta73_registro_lote_i.py`), **los dos EXTRAIDOS del ancestro y no tecleados**, comprobado con
> `grep` sobre los ocho ficheros nuevos: **solo esos dos traen `# ROTULO`**. **El `CENSO` no se mueve
> de 225 y el `ROJO` no se mueve de su linea base de 32.**

> **Y EL CENSO DE CODIFICACION SE CUENTA A SI MISMO, QUE ES LA OBSERVACION (a) DEL ACTA 72 APLICADA
> ANTES DE QUE VUELVA A PASAR:** la vuelta 72 publico **54** cuando existian **55**, porque su censo
> corrio antes de la ultima salida. **El de esta vuelta corrio DESPUES de las promesas y de la cabecera
> comparada, y su propio fichero esta dentro de la nomina que imprime** (es el vigesimo sexto de la
> lista). **`ls docs/loop | grep -c V73` da la misma cifra, 52, corrido aparte.**

### 9.1 **LA TASA POR DOMINIO AL CIERRE, IDENTICA A LA DE APERTURA**

**Fundir no volteo ni un veredicto**, y por eso el marcador de cierre sale **identico** al de apertura,
**las diez lineas**, comprobado por `diff` entre las dos salidas del tallador de marcador, **que salio
sin una sola diferencia**.

| dominio | pares | `A` | tasa |
|---|---:|---:|---:|
| compras | 155 | 1 | 0,6 |
| core | 1.445 | 325 | 22,5 |
| entrega | 171 | 2 | 1,2 |
| environmental | 170 | 28 | 16,5 |
| exportacion | 130 | 15 | 11,5 |
| franquicias | 148 | 15 | 10,1 |
| health_safety | 192 | 43 | 22,4 |
| quality | 844 | 119 | 14,1 |
| risk_management | 106 | 0 | 0,0 |
| seguridad_digital | 27 | 3 | 11,1 |

**Corte de todas estas cifras: 26 ago 2026, puesto 3.388.**

---

## 10. LO QUE QUEDA DEL TRAMO, MEDIDO AL CIERRE

([`SALIDA_V73_TRAMO_CIERRE.txt`](SALIDA_V73_TRAMO_CIERRE.txt),
[`SALIDA_V73_PUERTAS_DE_LOS_QUE_QUEDAN.txt`](SALIDA_V73_PUERTAS_DE_LOS_QUE_QUEDAN.txt) y
[`SALIDA_V73_PUENTES_DE_LOS_QUE_QUEDAN.txt`](SALIDA_V73_PUENTES_DE_LOS_QUE_QUEDAN.txt))

| | |
|---|---:|
| actos del tramo unico | **47** |
| actos **FUNDIDOS**, medido sobre el grafo | **30** |
| actos **`DECLARADOS Y NO FUNDIDOS`** | **15** |
| **quedan sin destino** | **2 actos y 6 nodos** |
| **el siguiente del prefijo** | el acto **31**, **con dueno** (`OP-F-04-WEI`, `OP-S-04`) |
| **el primero SIN dueno** | **NINGUNO: ya no queda ninguno** |
| de los que quedan, **con dueno medido** | **2** (los actos **31** y **37**), **o sea TODOS** |
| de los que quedan, **con nodo puente** | **0** |
| de los que quedan, **con par `D` interno** | **0** |
| de los que quedan, **con puerta dentro** | **1** (el **31**, `captura_conocimiento_mercado`) |
| **actos declarados que esperan el cierre de la fase 03** | **15** |

> **ESTE ES EL ESTADO CON EL QUE LA VUELTA SIGUIENTE PESA EL CIERRE DE LA FASE 03, Y POR ESO SE DEJA
> ESCRITO ENTERO: NO QUEDA NINGUN ACTO DEL TRAMO SIN DUENO Y SIN DESTINO.** Los **2** que quedan
> **traen dueno los dos** y su destino esta **en sus fases, no aqui**. **Las FORMAS de los dos, medidas
> hoy: el `31` `CHOCAN` y el `37` `UNA SOLA VARA`.** **Ninguno de los dos puede cerrar `DECLARADO` por
> la guarda `1B`, porque esa guarda pide DOS puertas y el `31` trae una y el `37` ninguna.**
>
> **Y LOS QUINCE DECLARADOS SIGUEN ESPERANDO, CON EL `44` NOMBRADO APARTE** (adjudicacion 3 del acta
> 72): **espera por sus DOS puertas y no por `P.10` ni por su familia**, que es una pregunta distinta
> de la de los otros catorce.

**NO SE FUNDIO NINGUN ACTO CON DUENO** (el `31` y el `37` quedan con los suyos), **no se toco la mesa
`OP-M-03` ni sus dos colisiones**, **las cinco colisiones de `OP-U-02` ya publicadas siguen vigentes
con su duena**, **no se toco ni un nodo del `acto 44` ni de los otros catorce declarados**, **NO SE
ABRIO LA FASE 04**, **NO SE DECIDIO EL CIERRE DE LA FASE 03** (que es parada de fundador), y **las
cinco fichas `OP-M-02` consumidas no se ejecutaron**: lo consumado no se ejecuta ni se rehace.

---

## 11. CONDICIONES DE PARADA, RECORRIDAS

| condicion | hoy |
|---|---|
| **doctrina nueva** | **NO**. Todo va por extension citable: `P.8` con su tabla de que cuenta como contenido, la letra `CHOCAN` decide la pieza declarada (acta 53, pregunta 3), `UNA SOLA VARA BASTA` (acta 53, pregunta 4), la puerta unica (acta 54, pregunta 1), la frontera del dueno (acta 68 adj. 2, acta 70 adj. 2, acta 71 adj. 2 con su borde), el carril de correccion declarada sobre instrumento estable, y `P.16` |
| **contradiccion sin regla** | **NO**. Las tres preguntas nuevas de la seccion 8 van marcadas y **ninguna bloqueo la operacion**. El `acto 50` tiene DOS reglas escritas apuntando a lados distintos, no una regla sin cubrir: **se eligio la de mas peso, se dijo cual y se marco** |
| **decision de fundador** | **NINGUNA SE TOMA**. El merge sigue siendo suyo y el cierre de la fase 03 tambien |
| **fallo tecnico repetido** | **NO**. Gate 0 y las tres suites en verde |
| **credito de tanda roto** | **NO**. El contador entro en **CERO** y esta vuelta no publica ninguna cifra movida |
| **campana consumada** | **NO** |
| **CIERRE DE LA FASE 03** (la parada del fundador) | **NO SE CUMPLE TODAVIA**, y **queda mas cerca que nunca**: ya **no queda ningun acto sin dueno y sin destino**, pero **quedan los 2 actos con dueno (`31` y `37`), la mesa `OP-M-03` y los QUINCE declarados**. **La vuelta siguiente lo pesa; esta no lo decide** |
| **credenciales** | no hicieron falta |

---

## 12. HASH FINAL Y COMMITS

**LA CADENA ENTERA DE LA VUELTA 73, ESCRITA AQUI POR EL SEXTO COMMIT:** `1562faa9` (TAREA 1),
`c584f060` (el plan sellado del lote `I`), `d6341ebe` (la fusion), `7f07d02f` (el registro del lote),
`c9457681` (el reporte) **y este, que es el que puede escribir el hash del anterior.**
**`origin/pasada-unica` queda igual a `HEAD` y el arbol limpio de rastreados.**

**Los commits de esta vuelta en `pasada-unica`, en orden:**

| commit | que trae |
|---|---|
| **`1562faa9`** | **TAREA 1 entera**: el registro del acta 72 (`+260`, `0` borradas, 73 agujas, tres negativas de sustancia) **mas la UNICA CORRECCION DECLARADA** (la glosa de la especie del pendiente 4 por el HECHO, `33 0`, con el cuerpo comprobado identico byte a byte) **y la APERTURA medida antes de la primera operacion**, con toda salida escrita en `UTF-8` desde el origen |
| **`c584f060`** | **TAREA 2, paso 1**: el lote `I` **declarado al abrirlo** y su **plan sellado dos veces**, con el `P.5`, las varas, el borde del dueno medido por maquina y **las colisiones esperadas sobre base 7**, todo **ANTES DE TOCAR UN NODO** |
| **`d6341ebe`** | **TAREA 2 ejecutada**: las cuatro fusiones, `P.16` con su limpieza en la misma corrida, el reanclaje, el diff de duplicadas, `Gate 0` con su ciclo de tres y las tres suites |
| **`7f07d02f`** | **TAREA 2, paso 3**: el registro del lote `I` en `03_FUSIONES.md` (`+463`, `0` borradas) y los censos del cierre |
| **`c9457681`** | **el reporte**, este fichero, con la cabecera tallada, los trece discutibles, las cuatro averias y las promesas cotejadas por maquina antes de sellarlo |
| **este** | **la cabecera de esta seccion 12**, con el hash del commit del reporte y la cadena entera |

**El hash final de la vuelta y la cadena entera van escritos en la cabecera de esta seccion por un
commit posterior**, que es lo que la regla 7 pide y lo que el commit del reporte no puede contener: un
commit no puede llevar su propio hash. **Misma via que las vueltas 69 a 72 usaron en sus commits
`a943673c`, `66ef6d38`, `fd46adc3` y `fdb45f33`.**
