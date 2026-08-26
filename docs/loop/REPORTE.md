# REPORTE DE LA VUELTA 74: EL PESO DEL CIERRE DE LA FASE 03, ARMADO CON INSTRUMENTO Y NO DECIDIDO, Y LA REGLA NUEVA DE LAS PROMESAS DE MARCADO

**Fase III, ejecucion continua. Rama `pasada-unica`. 26 ago 2026.**

**FECHA POR DOS RELOJES, CORRIDOS POR MI:** el reloj del sistema da **2026-08-26** y `git log -1
--date=format` sobre el commit de apertura da **2026-08-26 08:40**. **Toda cifra de este reporte tiene
ese corte.** La vuelta abrio con el arbol limpio en `fee44694` y **no cruzo medianoche**.

**EL CONTADOR DE PARADA ENTRO A ESTA VUELTA EN CERO TANDAS** (acta 73, seccion 6, con las dos rachas
en cero y las dos por TERCERA tanda limpia seguida). **ESTA ES UNA VUELTA DE MEDICION Y ESO CAMBIA LO
QUE HAY QUE MIRAR:** cero fusiones, cero actos declarados, cero nodos tocados, cero planes sellados, y
por eso **las dos columnas de la cabecera salen IDENTICAS**. Esa identidad es la forma exacta que
tenia la caida de la vuelta 56, asi que **va declarada de frente y con el aviso del propio tallador
copiado** (seccion 1), en vez de presentada como si nada.

**Y HAY UNA COSA QUE ESTE REPORTE TRAE Y QUE EL ENCARGO NO PEDIA, QUE ES LA MAS CARA DE LA VUELTA Y VA
LA PRIMERA: LA FASE 03 TIENE SEIS FUSIONES SIN HACER.** No son actos del tramo: son **SEIS de sus
DIECISEIS fichas** cuyos miembros siguen todos vivos, medidas una a una en el bloque 1 del instrumento
nuevo. El acta 73 enumero cuatro cosas que faltaba pesar y **esta no estaba entre ellas**. Va con su
medicion en la seccion 4 y **NO se decide aqui**: el peso se arma, no se falla.

---

## 1. LA CABECERA, TALLADA Y NO TECLEADA

**Generada entera con** `python scripts/loop/tallar_cabecera_reporte.py --vuelta 74` y **pegada sin
tocar una celda** ([`SALIDA_V74_CABECERA.txt`](SALIDA_V74_CABECERA.txt)). **La celda que no salga de
un instrumento no se escribe.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.188 / 665 / 17.671 | **3.853 / 3.188 / 665 / 17.671** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 376 / 175 | **551 / 376 / 175** |
| actos (componentes) | 49 | **49** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 23 | **26 / 23** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 127 | **61 / 127** |
| cola de costuras | 1.438 | **1.438** |
| colisiones de clase vigentes | 7 | **7** |
| auto-pares (los dos lados al mismo vivo) | 286 | **286** |
| duplicadas historicas: grupos / nodos | 898 / 711 | **898 / 711** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (188 igual a 188; 175 igual a 175) | **TODAS OK (188 igual a 188; 175 igual a 175)** |

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION** (regla 1, tercer renglon): los seis
instrumentos de apertura corrieron con el arbol limpio en `fee44694`, **antes de escribir nada**, y
`git status --porcelain` tras correrlos dio **CERO ficheros rastreados movidos** (solo las siete
salidas nuevas, sin trackear). **EL CIERRE SE RECOMPUTO AL CIERRE**, despues de la `TAREA 1`, de la
`TAREA 2` y de `run_phase1`.

> **LAS DOS COLUMNAS SON IDENTICAS Y EL PROPIO TALLADOR LO AVISA. NO SE TAPA: SE COPIA SU AVISO.**
> `SALIDA_V74_CABECERA.txt` termina con esta frase suya, verbatim: *AVISO: los dos lados dan la MISMA
> cifra. Puede ser cierto (vuelta que no movio el retrato), pero es la forma que la caida de la vuelta
> 56 tenia.*
>
> **AQUI ES CIERTO, Y LA PRUEBA NO ES QUE YO LO DIGA SINO QUE LOS DOS LADOS SE LEEN DE FICHEROS
> DISTINTOS.** Las catorce filas de la izquierda salen de las seis salidas `_APERTURA` y las catorce
> de la derecha de las seis `_CIERRE`, **corridas en momentos distintos y guardadas aparte**. Ademas:
> el `diff` entre `SALIDA_V74_MARCADOR_APERTURA.txt` y `SALIDA_V74_MARCADOR_CIERRE.txt` da **CERO
> lineas**, y `git diff` sobre `dataset/` en toda la vuelta da **VACIO**. **Una vuelta que no toca un
> nodo tiene que dar exactamente esto**, y lo contrario habria sido la noticia.

**LA APERTURA DE HOY CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 73 PUBLICO** (marcador 551 / 72 / 5 /
2.760, grafo 3.853 / 3.188 / 665 con 17.671 enlaces, retrato 551 / 376 / 175, 49 componentes, 26 y 23
sobre 61 y 127, cola 1.438, colisiones 7, auto-pares 286, duplicadas 898/711, 71 `LISTA`, 672 entradas
y las cuatro comprobaciones en 188 y 175), **que es el contraste que la regla 2 permite**: entre las
dos vueltas nadie movio dato.

---

## 2. `TAREA 1`: EL REGISTRO DEL ACTA 73 Y LA REGLA NUEVA DE REDACCION

`python scripts/loop/vuelta74_registrar_acta73.py`
([`SALIDA_V74_REGISTRO_ACTA73.txt`](SALIDA_V74_REGISTRO_ACTA73.txt))

**`+235` lineas y CERO borradas** (`git show --numstat` sobre `85a83352`: **`235 0`** en
`docs/plan/03_FUSIONES.md`), **60 agujas derivadas y NINGUNA tecleada**, **tres agujas NEGATIVAS de
sustancia en verde**, **idempotencia MORDIENDO** (segunda corrida:
[`SALIDA_V74_REGISTRO_ACTA73_IDEM.txt`](SALIDA_V74_REGISTRO_ACTA73_IDEM.txt), *YA ADOSADA*, arbol
limpio despues), y **el re-cotejo tras adosar mide que las 60 sedes de arriba siguen en su linea**
(`OK 60 de 60`).

**LA MAQUINA SE COPIO POR EXTRACCION Y NO SE RETECLEO**
(`scripts/loop/_v74_construir_registrador_acta.py`): las dos piezas copiadas (los imports, 11 lineas,
y la maquina entera de la guarda de citas, 163 lineas con 9 sub-piezas comprobadas por `assert`)
**aparecen LITERALES en el destino**, comprobado por el propio constructor. **LA MAQUINA NO CRECE NI
ENCOGE**: cero mecanismos nuevos, cero filas, cero columnas, y ninguno de los cuatro mecanismos se
cae por el camino (adjudicacion 3 del acta 69, mas el `D12` del acta 73 que recordo que encoger esta
igual de prohibido).

> **LO QUE SE ANADE ES UNA SOLA CONSTANTE DE RUTA, Y ESTA VEZ TIENE UN MOTIVO QUE NO ES UNA
> CORRECCION:** la vuelta 72 estreno TRES ficheros de aguja porque traia TRES correcciones y su `D11`
> quedo `A FAVOR`; la 73 estreno UNA por la misma via. **Esta estrena UNA
> (`comprobar_promesas_de_marcado.py`) porque la REGLA NUEVA nombra TRES FORMAS y las tres se CITAN
> POR AGUJA en vez de teclearse.** Y el motivo de citarlas es **la propia regla que se registra**: una
> regla que teclea tres cadenas puede divergir del instrumento sin que nadie lo note, **que es
> exactamente la especie de averia que el `D13` declara**. Citadas por aguja, si el instrumento
> cambiara una forma, el registro caeria en `ROJO` y no escribiria nada. **Va marcado `D2`.**

### 2.1 **LA REGLA NUEVA, ESCRITA DONDE SE PUEDE CITAR** (encargo `TAREA 1.2`, adjudicada en el `D13` del acta 73)

**Vive en el apartado `d)` del registro que esta vuelta adoso**, y la adjudicacion va **VERBATIM y no
parafraseada**, copiada por el instrumento con `[[VERBATIM:A73_D13:11]]` desde la cabecera del `D13`
del acta. **La cita no la teclee yo: la extrajo la maquina de la linea que la aguja localizo.**

| lo que la regla manda | como queda escrito, y medido |
|---|---|
| **quien la obedece** | **toda promesa de marcado escrita en un motivo sellado**, de la **vuelta 74 en adelante** |
| **las tres formas** | **NO TECLEADAS**: citadas por aguja sobre las lineas **63**, **67** y **89** de `scripts/loop/comprobar_promesas_de_marcado.py`, mas la tupla de la **90** y la corrida que las imprime de la **113** |
| **lo que NO se toca** | **el instrumento NO se ensancha**: cero formas nuevas, cero condiciones, cero tablas |
| **hacia atras** | **los planes ya ejecutados NO se re-sellan** (acta 68, `D15`), y las dos promesas invisibles de la vuelta 73 **se quedan declaradas donde estan** |
| **lo que la regla no promete** | **la forma no es la cosa**: la promesa que vale es la que **se cumple** en la seccion 6; la forma solo garantiza que el instrumento pueda **verla para exigirla** |

**EL CASO POSITIVO DEL INSTRUMENTO DE PROMESAS SE RE-CORRIO IGUAL**
([`SALIDA_V74_CASO_POSITIVO_PROMESAS.txt`](SALIDA_V74_CASO_POSITIVO_PROMESAS.txt)): **LAS DOS MITADES
MUERDEN**, sin regresion (2 de 2 y 2 de 2 al digito contra las salidas selladas) y **la forma plural
sigue viendose**. **La regla se apoya en un instrumento que hoy esta probado, no en uno recordado.**

### 2.2 **LAS OTRAS DOS ADJUDICACIONES, REGISTRADAS PARA CUANDO VUELVAN A SALIR** (encargo `TAREA 1.3`)

**Van en el apartado `e)` del registro, con la linea de cada una**, y el motivo de sacarlas de los
trece discutibles y ponerlas juntas esta escrito ahi: **una regla que solo vive en el acta que la
escribio se pierde en la vuelta siguiente**.

| | lo adjudicado, con la letra ya escrita que lo sostiene |
|---:|---|
| **1** | **LA FORMA `UNA SOLA VARA` CON LAS RAZONES EN CONTRA ES UN `CHOCAN` QUE EL INSTRUMENTO NO SABE VER, Y MANDA LA PIEZA DECLARADA**: por `P.8` (una contencion declarada por el archivo es contenido **con el mismo peso**) y por el acta 53, pregunta 3 (a `CHOCAN` decide **la pieza declarada**) |
| **2** | **LA FRASE SELLADA DENTRO DE UNA NEGACION ES REGLA DE REDACCION, NO MAQUINA NUEVA**: **basta con dejarla escrita**, y el instrumento **no se ensancha a distinguir negaciones** |

> **LAS TRES COMPARTEN FIGURA Y REGISTRARLA JUNTA VALE MAS QUE REGISTRARLAS SUELTAS: NINGUNA ENSANCHA
> UN INSTRUMENTO.** La primera manda leer la letra de `P.8` en vez de ensenarle razones al medidor; la
> segunda deja una regla de redaccion en vez de ensenarle negaciones; la tercera deja otra regla de
> redaccion en vez de ensenarle formas. **Tres problemas distintos, la misma salida barata.** Y las
> tres **con letra ya escrita**, que es lo que la condicion de parada de doctrina obliga a comprobar.

---

## 3. `TAREA 2`: EL PESO DEL CIERRE, ARMADO CON INSTRUMENTO

`python scripts/loop/vuelta74_peso_del_cierre.py`
([`SALIDA_V74_PESO_DEL_CIERRE.txt`](SALIDA_V74_PESO_DEL_CIERRE.txt))

**EL INSTRUMENTO ES DE SOLO LECTURA Y ESO ES LA MITAD DE SU CONTRATO:** no escribe un nodo, no funde,
no declara, no sienta ninguna mesa, no abre la fase 04. **MEDIR NO ES DECIDIR**, y el reparto esta
escrito en el acta 73: **la vuelta 74 arma el peso, el auditor de la 74 lo pesa y la parada la escribe
el.**

**LA REGLA DEL DESTINO SE IMPRIME ANTES DE APLICARSE**, que es lo que la hace discutible en vez de
opaca. Es una sola y vale para las dieciseis:

| | la regla, tal como el instrumento la imprime |
|---:|---|
| **a** | ficha **sin nomina de nodos** a `ABRIDOR DE UNIVERSO`: su destino son sus **REGISTROS** |
| **b** | nomina que resuelve por `P.1` a **UN vivo o a ninguno** a **sin fusion pendiente**, y entonces: **b.1** con declaracion de `CONSUMIDA` en su `nota` a `CONSUMIDA`; **b.2** sin ella a `EJECUTADA` |
| **c** | nomina con **DOS o mas vivos** a `FUSION PENDIENTE`, **y se dice por que espera** |

---

## 4. LAS DIECISEIS FICHAS DE LA FASE 03, UNA A UNA, CON SU DESTINO MEDIDO

**Medidas contra el grafo de HOY, no contra el recuerdo.** Los ids se resuelven por `P.1` antes de
contar (regla 9).

| ficha | nodos | resueltos | **VIVOS** | **DESTINO MEDIDO** | la evidencia, citada |
|---|---:|---:|---:|---|---|
| `OP-U-01` | 0 | 0 | 0 | **ABRIDOR DE UNIVERSO** | **14** cabeceras de nivel 2 en la pagina, de la linea **185** a la **2782**: sus SEIS tramos con su cierre |
| `OP-U-02` | 0 | 0 | 0 | **ABRIDOR DE UNIVERSO** | **11** cabeceras de nivel 2, de la **221** a la **8532**: la apertura y **los NUEVE lotes `A` a `I`**, vueltas 65 a 73 |
| `OP-M-02-PROG` | 2 | 1 | **1** | **EJECUTADA** | sede en la linea **3161**, *EL REGISTRO DE LA FUSION (2026-08-20, vuelta 63)* |
| `OP-M-03-I` | 2 | 1 | **1** | **EJECUTADA** | sede en la linea **3057**, *EL REGISTRO DE LA FUSION (2026-08-20, vuelta 63)* |
| `OP-M-03-II` | 2 | 1 | **1** | **EJECUTADA** | sede en la linea **3486**, *EL REGISTRO DE LA FUSION (2026-08-20, vuelta 64)* |
| `OP-M-02-MEDIOS` | 2 | 1 | **1** | **CONSUMIDA** | fila **3395** y glosa en la **3401**: `OP-U-01`, tramo 3, vuelta 56, lote `B`, acto 32 |
| `OP-M-02-ASSESS` | 2 | 1 | **1** | **CONSUMIDA** | fila **3396**: `OP-U-01`, tramo 2, vuelta 55, acto 30, lote `A` |
| `OP-M-02-ADMIT` | 2 | 1 | **1** | **CONSUMIDA** | fila **3397**: `OP-U-01`, tramo 2, vuelta 55, acto 38, lote `B` |
| `OP-M-02-ACTIVATE` | 2 | 1 | **1** | **CONSUMIDA** | fila **3398**: `OP-U-01`, tramo 1, vuelta 48, acto 44 |
| `OP-M-02-ACCOMPLISH` | 2 | 1 | **1** | **CONSUMIDA** | fila **3399**: `OP-U-01`, tramo 3, vuelta 56, acto 9, lote `A` |
| **`OP-M-01-FUSION`** | 5 | 5 | **5** | **FUSION PENDIENTE** | **NINGUNA cabecera de nivel 2 la nombra**; espera por `OP-M-01`, fase `06_MESAS` |
| **`OP-M-02-ACCLIMATE`** | 2 | 2 | **2** | **FUSION PENDIENTE** | **NINGUNA cabecera de nivel 2**; espera por `OP-M-02` (`06_MESAS`) y por `OP-M-02-MEDIOS` (ya `CONSUMIDA`) |
| **`OP-M-03-III`** | 3 | 3 | **3** | **FUSION PENDIENTE** | **NINGUNA cabecera de nivel 2**; espera por `OP-M-03`, fase `06_MESAS` |
| **`OP-M-05-INDICE`** | 3 | 3 | **3** | **FUSION PENDIENTE** | **NINGUNA cabecera de nivel 2**; espera por `OP-M-05`, `OP-M-04` (`06_MESAS`) y `OP-M-03-II` (ya `EJECUTADA`) |
| **`OP-M-05-EDIFICIO`** | 3 | 3 | **3** | **FUSION PENDIENTE** | **NINGUNA cabecera de nivel 2**; mismos tres que la anterior |
| **`OP-M-05-APERTURA`** | 3 | 3 | **3** | **FUSION PENDIENTE** | **NINGUNA cabecera de nivel 2**; mismos tres que la anterior |

**EL REPARTO, CONTADO POR EL PROPIO INSTRUMENTO:** **2** abridores, **3** `EJECUTADAS`, **5**
`CONSUMIDAS` y **6** con `FUSION PENDIENTE`. **Dos mas tres mas cinco mas seis son dieciseis, y las
dieciseis estan.**

### 4.1 **LA PIEZA QUE EL ENCARGO NO NOMBRABA: LA FASE 03 TIENE SEIS FUSIONES SIN HACER**

**Y no es una lectura: es la nomina viva de cada una, impresa.** `OP-M-01-FUSION` conserva sus CINCO
(la camarilla de los gates), `OP-M-03-III` sus TRES (el acto de pivotar), las tres de `OP-M-05` sus
TRES cada una (customer discovery, salir del edificio y customer validation) y `OP-M-02-ACCLIMATE`
sus DOS. **Ninguna tiene registro de fusion en la pagina, y eso se midio buscandolo, no suponiendolo.**

**QUIEN LAS BLOQUEA, MEDIDO POR SU `depende_de` y con la fase de cada bloqueador leida de SU ficha**
(bloque 4.b del instrumento):

| quien bloquea | su fase | su estado | a cuantas | cuales |
|---|---|---|---:|---|
| `OP-M-01` | **`06_MESAS`** | `LISTA` | 1 | `OP-M-01-FUSION` |
| `OP-M-02` | **`06_MESAS`** | `LISTA` | 1 | `OP-M-02-ACCLIMATE` |
| `OP-M-02-MEDIOS` | `03_FUSIONES` | `LISTA` | 1 | `OP-M-02-ACCLIMATE` |
| `OP-M-03` | **`06_MESAS`** | `LISTA` | 1 | `OP-M-03-III` |
| `OP-M-03-II` | `03_FUSIONES` | `LISTA` | 3 | `OP-M-05-APERTURA`, `OP-M-05-EDIFICIO`, `OP-M-05-INDICE` |
| `OP-M-04` | **`06_MESAS`** | `LISTA` | 3 | las tres de `OP-M-05` |
| `OP-M-05` | **`06_MESAS`** | `LISTA` | 3 | las tres de `OP-M-05` |

> **LOS DOS BLOQUEADORES DE DENTRO DE LA FASE 03 YA ESTAN RESUELTOS, Y ESO SE MIDE EN LA MISMA
> SALIDA:** `OP-M-02-MEDIOS` esta `CONSUMIDA` y `OP-M-03-II` esta `EJECUTADA`. **Los que quedan de
> verdad son los CINCO de la fase `06_MESAS`**, y **las cinco mesas de la campana son exactamente esas
> cinco**: `OP-M-01`, `OP-M-02`, `OP-M-03`, `OP-M-04` y `OP-M-05`, **todas `LISTA` y todas con su
> campo `adjudicacion` escrito** (956, 1.559, 1.918, 1.935 y 758 caracteres), **CERO sin adjudicar**
> (bloque 4.c). **Adjudicadas no es ejecutadas, y la diferencia es justo lo que falta.**

---

## 5. LOS QUINCE DECLARADOS, MEDIDOS POR DOS VIAS QUE CALZAN

**LA LISTA NO ENTRA POR ARGUMENTO EN ESTE INSTRUMENTO, Y ESA ES SU NOVEDAD.** `tramo_al_cierre.py`
recibe los `DECLARADOS` como HISTORIA y lo dice en su docstring, porque **un declarado tiene todos sus
miembros vivos igual que uno sin tocar**: sobre el grafo solo, no se distinguen. **Aqui se miden POR
DOS VIAS y se cruzan.**

| | la via | lo que da |
|---|---|---|
| **A** | **sobre el grafo de hoy**: un acto esta `ABIERTO` si conserva **DOS o mas** miembros vivos | **30** fundidos y **17** abiertos |
| **B** | **sobre la pagina**: sedes en la region del tramo unico con la frase `DECLARADO Y NO FUNDIDO` (singular o plural) que ademas **nombren al acto por un token canonico con borde de palabra** | **15** actos con al menos una sede |

**CRUZADAS:** los `ABIERTOS` que la pagina **DECLARA** son **15** y son
**1, 5, 10, 11, 12, 13, 14, 15, 17, 20, 21, 23, 24, 27 y 44**. Los `ABIERTOS` que la pagina **NO
declara** son **2**: el **31** y el **37**. **CERO actos abiertos sin declaracion y sin dueno.** **Y
cero declarados en la pagina que ya no esten abiertos**, que es la otra mitad del cruce y tambien se
mide.

> **LA LISTA MEDIDA HOY POR LA PAGINA COINCIDE AL DIGITO CON LA QUE EL ACTA 73 PUBLICO** (su seccion
> 1, tramo al cierre: *los 15 DECLARADOS del argumento*, con esos mismos quince numeros). **Es
> contraste, no fuente**: la de este reporte sale de la corrida de hoy.

### 5.1 **LOS QUINCE, UNO A UNO, CON SUS PUERTAS Y EL MOTIVO QUE SU SEDE CITA**

| acto | miembros | vivos | **PUERTAS** | motivo que la sede cita | sede |
|---:|---:|---:|---:|---|---:|
| **1** | 15 | 15 | **2** | `P.10` | **3744** |
| **5** | 8 | 8 | 0 | `P.5` (y la sede nombra tambien `P.10` para decir que **no** se dispara) | **4365** |
| **10** | 6 | 6 | 0 | `P.10` | **4419** |
| **11** | 5 | 5 | 0 | `P.10` | **4419** y **5330** |
| **12** | 5 | 5 | 0 | `PENDIENTE DE DOCTRINA` primero, y **`D` directo interno** despues | **4631**, **4797**, **5144** |
| **13** | 5 | 5 | **2** | guarda `1B` | **4632** |
| **14** | 5 | 5 | 0 | `P.5` | **4633** y **4920** |
| **15** | 5 | 5 | **2** | guarda `1B` | **4634** |
| **17** | 5 | 5 | **1** | `P.10` | **4636** y **4962** |
| **20** | 4 | 4 | 0 | `P.10` | **5239** |
| **21** | 4 | 4 | 0 | `P.10` | **5240** |
| **23** | 4 | 4 | 0 | `P.10` | **5242** |
| **24** | 4 | 4 | 0 | `P.10` | **5243** |
| **27** | 4 | 4 | 0 | `P.10` | **5773** y **6043** |
| **44** | 3 | 3 | **2** | guarda `1B` | **7790**, **7797** y **7897** |

**Suman 82 nodos vivos**, contados por el instrumento. **Las PUERTAS se midieron contra el universo
protegido de 256 ids** (semillas de entrada mas extremos de puente aprobado), **importado de
`scripts/loop/varas_n_arias_del_tramo.py` y no re-inventado aqui** (`D1`).

### 5.2 **EL `ACTO 44`, NOMBRADO APARTE** (adjudicacion 3 del acta 72, y el encargo lo repite)

**No es uno mas de los quince, y la medicion lo confirma sin necesidad de creerle a nadie:** sus TRES
miembros siguen vivos, **DOS de ellos son PUERTAS**
(`explotacion_tecnologias_disruptivas` y `tecnologias_disruptivas_oportunidad`), y su motivo sellado
es **la guarda `1B`**, no `P.10` ni `P.5`. **De los quince, solo TRES traen dos puertas** (el 13, el 15
y el 44) **y solo el 44 cerro por ellas con la vara apuntando a una**, que es lo que lo hace especie
propia: **la guarda `1B` NO ORDENA LAS PUERTAS ENTRE SI**, y ninguna regla escrita ordena hoy esa
eleccion. **Sus tres nodos y sus dos puertas no se tocan.**

### 5.3 **EL SUBCONJUNTO, DESCRITO COMO PREGUNTA Y NO RESUELTO** (el encargo lo pide con esas palabras)

**La pregunta, dicha entera y sin contestarla:** `P.10` ofrece el **subconjunto cerrado** como salida
de un acto con triangulo, **pero la condiciona a que TODAS las lecturas del acto esten hechas**. La
pagina lo tiene registrado como **pendiente 2** en la linea **4061**, con estas palabras suyas: *en
los actos con puente no lo estan ni pueden estarlo sin lecturas nuevas que ninguna operacion
escribio*, y su destino escrito es **el cierre de la fase 03**, *con el fundador delante si pide
lecturas nuevas*.

**LO QUE ESTA VUELTA ANADE A ESA PREGUNTA, Y ES MEDICION Y NO OPINION:** el instrumento cuenta
**DIEZ** actos cuya sede **nombra `P.10`**, pero **UNO de esos diez lo nombra para decir que NO se
dispara**: el `acto 5`, cuya sede cita **`P.10` y `P.5` a la vez** y cierra por el segundo. **Los que
cierran POR `P.10` son por tanto NUEVE**: el 1, el 10, el 11, el 17, el 20, el 21, el 23, el 24 y el
27. **Los SEIS restantes cierran por otra cosa**: `P.5` (el 5 y el 14), la guarda `1B` (el 13, el 15 y
el 44) y el cuarto motivo (el 12), **y a esos el subconjunto de `P.10` no les aplica siquiera**.
**Nueve mas seis son quince.** **La pregunta abierta tiene por tanto un tamano medido: NUEVE actos, no
quince.** **No la contesto: resolverla es del paquete del fundador, y el encargo lo dice.**

> **LA DIFERENCIA ENTRE DIEZ Y NUEVE SE ESCRIBE EN VEZ DE ELEGIRSE EN SILENCIO**, porque el
> instrumento **no lee razones, solo cuenta agujas**: para el, una sede que nombra `P.10` cita `P.10`,
> diga lo que diga de el. **La lectura la puse yo, abriendo la sede del `acto 5`** (linea **4365**),
> **y por eso las dos cifras van publicadas.** **Va marcado `D13`.**

---

## 6. LOS DOS ACTOS CON DUENO, RE-MEDIDOS CAMPO A CAMPO

**La vara es la adjudicacion 2 del acta 68:** el dueno de un acto es **toda ficha que nombre a alguno
de sus miembros en `nodos`, `preservar` o `eliminar`**, cruzado contra **LAS 71 FICHAS** y no contra
las de una fase.

| acto | miembros | vivos | duenos escritos en el fichero del tramo | duenos **RE-MEDIDOS** campo a campo | calzan |
|---:|---:|---:|---|---|:---:|
| **31** | 3 | 3 | `OP-F-04-WEI`, `OP-S-04` | `OP-F-04-WEI`, `OP-S-04` | **SI** |
| **37** | 3 | 3 | `OP-S-07` | `OP-S-07` | **SI** |

| dueno | **SU FASE, leida de SU ficha** | estado | tipo | por que campo lo agarra |
|---|---|---|---|---|
| `OP-F-04-WEI` | **`01_FUENTES`** | `LISTA` | `DECISION_DE_FUENTE` | `nodos`: `analisis_trafico_competitivo` |
| `OP-S-04` | **`05_SANEO`** | `LISTA` | `HERRAMIENTA` | `nodos`: `analisis_trafico_competitivo`, `capturar_conocimiento_de_mercado` |
| `OP-S-07` | **`00_CODIGO`** | `LISTA` | `CAMPO_SUCIO` | `nodos`: `cumplimiento_inversionistas_acreditados` |

> **LA RESPUESTA, CON LA FICHA DELANTE Y NO DE MEMORIA:** **SI, el destino de los tres duenos vive
> FUERA de la fase 03.** `01_FUENTES`, `05_SANEO` y `00_CODIGO`, leidos del campo `fase` de cada
> ficha en esta corrida. **Ninguno es de `03_FUSIONES`.**
>
> **Y UN MATIZ QUE LA MEDICION DESTAPA Y QUE NADIE HABIA ESCRITO:** el **`acto 24` esta DECLARADO Y
> ADEMAS TIENE DUENO** (su sede, la linea **5243**, lo dice con todas sus letras: *`P.10`, dos
> triangulos, la figura `ESTRELLA` y el dueno `OP-S-07`*). **Las dos columnas del cierre no son
> disjuntas**, y contarlas como si lo fueran es lo que hace que **15 mas 2 den 17 abiertos y no 16**.
> **Va marcado `D4`.**

---

## 7. LA MESA `OP-M-03`, CON SU FICHA LEIDA ENTERA

| campo | lo que la ficha dice, leido hoy |
|---|---|
| **`fase`** | **`06_MESAS`** |
| `tipo` | `MESA ADJUDICADA: DOS PUERTAS MAS UN ACTO` |
| `estado` | `LISTA` |
| `orden` / `fecha_corte` | 3 / **2026-08-12** |
| `nodos` | **vacio** |
| `depende_de` | **vacio** |
| `bloquea_a` | `OP-D-07`, `OP-M-03-I`, `OP-M-03-II`, `OP-M-03-III`, `OP-M-03-ENLACES`, `OP-S-12` |
| `pregunta_pendiente` | **ninguna** |
| `adjudicacion` | **ADJUDICADA**, 1.918 caracteres, del **12 ago 2026** |

**LA RESPUESTA, CON LA LETRA DELANTE:** **el campo `fase` de `OP-M-03` dice `06_MESAS`, asi que NO
pertenece a la fase 03.** **Ni la sente ni la ejecute ni la toque.**

**PERO NO BASTA CON ESO, Y AQUI ESTA LA HONESTIDAD DE LA MEDICION:** de las seis fichas que bloquea,
**TRES son de la fase 03** (`OP-M-03-I`, `OP-M-03-II` y `OP-M-03-III`), y **dos de esas tres ya estan
`EJECUTADAS`**; **la que queda es `OP-M-03-III`**. Asi que **la mesa no pertenece a la fase 03 y aun
asi la fase 03 depende de ella**. **Las dos cosas son ciertas a la vez y las dos van escritas**, que
es lo que el encargo pedia cuando dijo *di con la letra delante*: **la letra dice que no es de la
fase; la medicion dice que la estorba.** **Cual de las dos manda para el cierre no lo decide este
reporte.**

---

## 8. EL VEREDICTO MEDIDO: QUE LE FALTA A LA FASE 03 PARA ESTAR CERRADA

**La tabla sale del bloque 5 del instrumento y se pega entera.** **Ninguna celda esta tecleada.**
**El instrumento marca `LISTA` o `PENDIENTE` por lo que mide, y NO dice si la fase esta cerrada.**

| pieza | lo medido | estado | nota |
|---|---|---|---|
| fichas de la fase `03_FUSIONES` con **`FUSION PENDIENTE`** | **6 de 16** | **PENDIENTE** | `OP-M-01-FUSION`, `OP-M-02-ACCLIMATE`, `OP-M-03-III`, `OP-M-05-APERTURA`, `OP-M-05-EDIFICIO`, `OP-M-05-INDICE` |
| actos del tramo **SIN declaracion y SIN dueno** | **0** | **LISTA** | medido por las dos vias: todo acto abierto o esta `DECLARADO` o tiene dueno |
| actos **`DECLARADOS Y NO FUNDIDOS`** | **15 actos, 82 nodos** | **PENDIENTE** | su subconjunto es pregunta abierta, no se resuelve aqui |
| actos con **DUENO fuera de la fase `03_FUSIONES`** | **2 actos, 6 nodos** | **PENDIENTE** | sus duenos y sus fases van medidos en la seccion 6 |
| la mesa `OP-M-03` | fase **`06_MESAS`** | **FUERA DE LA FASE** | bloquea a 6 fichas, tres de ellas de la fase 03 |
| mesas y fichas que **BLOQUEAN** a las pendientes de la fase 03 | **7 bloqueadores distintos** | **PENDIENTE** | `OP-M-01`, `OP-M-02`, `OP-M-02-MEDIOS`, `OP-M-03`, `OP-M-03-II`, `OP-M-04`, `OP-M-05` |

**LO QUE ESTE REPORTE DICE Y LO QUE NO:**

**DICE** que hay **cuatro piezas en `PENDIENTE` y una en `LISTA`**, cada una con su cifra y su cita.
**DICE** que **la unica que la vuelta 73 dejo cerrada** (ningun acto sin dueno y sin destino) **sigue
cerrada hoy, re-medida**. **DICE** que **la pieza mas grande no estaba en la lista del acta 73**: las
seis fusiones sin hacer.

**NO DICE** si la fase 03 esta `CERRADA Y VERIFICADA`. **NO abre la fase 04. NO funde. NO declara. NO
sienta la mesa. NO toca un nodo.** **La parada la escribe el auditor de la 74, y este reporte no la
adelanta ni la insinua.**

**Y NO PARO, PORQUE NO HAY CONTRADICCION QUE TRAER:** ninguna cifra medida hoy contradice una cifra
publicada con su corte, y ninguna operacion pidio una regla que no existe. **Lo que hay es una pieza
NUEVA en el peso**, y una pieza nueva medida no es una parada: es lo que el encargo pedia armar.

---

## 9. LO QUE NO SE MOVIO, MEDIDO EN VEZ DE PROMETIDO

| lo que no se movio | como se midio |
|---|---|
| **el grafo entero** | `git diff` sobre `dataset/` en toda la vuelta: **VACIO**. Las catorce filas de la cabecera, identicas de lado a lado |
| **las 71 fichas** | `git diff` sobre `docs/plan/OPERACIONES.jsonl`, `INVENTARIO.jsonl` y `RACIMOS_MIEMBROS.jsonl`: **VACIO**. 71 `LISTA`, **0** dependencias rotas, **672** entradas |
| **las siete colisiones vigentes** | censo re-corrido al cierre: **7** vigentes, **286** auto-pares, **3.082** pares resueltos distintos, identico a la apertura |
| **la mesa y los actos con dueno** | ni un nodo tocado; los seis nodos del 31 y del 37 siguen los seis vivos |
| **los quince declarados** | **82** nodos vivos, los mismos que al abrir |
| **el `acto 44`** | tres miembros vivos, dos puertas, cero cambios |
| **los planes** | `PLAN_V74_*.json`: **CERO ficheros**, contados sobre el directorio. **Esta vuelta no sella ningun plan** |
| **los instrumentos de nombre estable** | `git diff --diff-filter=M` sobre `scripts/`: **NINGUNO**. Los cuatro ficheros nuevos entran por `--diff-filter=A` |

---

## 10. `Gate 0`, LAS TRES SUITES Y LOS CENSOS

| corrida | lo que dio |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, todos los chequeos en `[OK]`; universo **3.188 activos / 665 deprecados**; alcanzabilidad **100,0 por ciento** (3.188/3.188, 85 semillas validas) |
| `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas** re-aplicadas |
| `python scripts/sync_assets_web.py` | **6 assets** mas `manifest.json` |
| **el ciclo de tres, comprobado** | `master_graph.json` queda **IDENTICO al committeado** (`git diff` vacio). El unico fichero movido fue `phase1_run_log.json`, **el log de MI corrida**, restaurado con `git checkout` |
| `python engine/run_all_tests.py` | **25 de 25** |
| `npx vitest run` (en `web/`) | **80 ficheros**, **1.030 pasadas** y **3 saltadas** |
| `npx tsc --noEmit` (en `web/`) | **CERO lineas** |
| `python scripts/loop/barrido_titulos_tallados.py` | **491** ficheros, `ROJO` **32**, `AMBAR` **0**, `ROTULADO` **57**, `CENSO` **225**, `ILEGIBLE` **1** |
| `python scripts/loop/censo_de_plantillas_talladas.py` | corrido, sin tallados nuevos |
| `python scripts/loop/vuelta65_caso_positivo_promesas.py` | **LAS DOS MITADES MUERDEN**, sin regresion |

> **EL `ROJO` NO SUBE, Y ESO SE MIDE FICHERO A FICHERO EN VEZ DE COMPARAR EL TOTAL:** compare la lista
> de `ROJO` de hoy contra la de [`SALIDA_V73_BARRIDO.txt`](SALIDA_V73_BARRIDO.txt) y salen
> **IDENTICAS**: **cero nuevos y cero desaparecidos**. **Los CUATRO instrumentos nuevos de esta vuelta
> no anaden ni un `ROJO`.** El barrido pasa de **487** ficheros a **491** (los cuatro nuevos) y el
> `ROTULADO` de **56** a **57** (el registrador clonado, que lleva su rotulo extraido del ancestro).

**CODIFICACION:** **29** ficheros `V74` en `docs/loop`, **29 de 29 en `UTF-8`** al cierre. **Uno de
ellos no lo estaba en su primera escritura y la averia va declarada en la seccion 11.**

---

## 11. AVERIAS PROPIAS DE ESTA VUELTA, CON NOMBRE Y NINGUNA CON CIFRA PUBLICADA DE POR MEDIO

**11.1 LA SALIDA DE ETIQUETAS SE ESCRIBIO FUERA DE `UTF-8`.** La primera corrida de
`etiquetas_de_cara.py --aplicar` volco su salida en la pagina de codigos de la consola de Windows, y
el fichero traia un byte `0xf3` que no es `UTF-8` valido. **La cazo MI PROPIO censo de codificacion
sobre los ficheros `V74`, antes de escribir una sola linea de este reporte.** Se re-corrio con
`PYTHONIOENCODING=utf-8` y al cierre son **29 de 29**. **Ninguna cifra publicada salio de la salida mala.**
**Efecto colateral que tambien se declara:** el paso de etiquetas del ciclo de tres se corrio **dos
veces**; `master_graph.json` quedo identico al committeado despues (`git diff` vacio), comprobado
otra vez. **Va marcado `D12`.**

**11.2 CORRI LA SUITE WEB CON UN REPORTER QUE NO EXISTE.** El primer intento fue
`npx vitest run --reporter=basic` y `vitest 4.1.10` **no lo tiene**: la corrida murio cargando el
reporter, con `exit 1`. **No es un fallo de la suite y no se leyo como tal:** se re-corrio con el
reporter por defecto, que es el que la casa usa, y dio **80 ficheros, 1.030 pasadas y 3 saltadas**.
**La leccion es la del acta 73 sobre el comando equivocado de la suite: el comando de la casa se
comprueba, no se recuerda.**

**11.3 EL PRIMER `recomputo_3388.py` MURIO CON `exit 2` POR FALTARLE `--salida`.** El instrumento lo
hizo **a proposito**: su docstring dice que la forma sin `--salida` **ya no existe** y que falla
visible en vez de pisar un fichero. **Cayo en rojo, no escribio nada, y se re-corrio con la ruta
nombrada.** **Es el instrumento haciendo su trabajo, y por eso se declara sin disfrazarlo de
descuido.**

**11.4 MI PRIMERA REGLA DE DETECCION DE DECLARADOS SE COMIA DOS ACTOS Y SE ROBABA SEDES AJENAS.**
El primer intento buscaba la frase `DECLARADO Y NO FUNDIDO` **solo en singular** y nombraba el acto
**sin borde de palabra**: perdia el **10** (su cabecera dice `DECLARADOS Y NO FUNDIDOS`, en plural) y
le adjudicaba al **acto 1** las sedes del **12**, del **14** y del **17**. **Lo cazo el propio cruce
de las dos vias del instrumento**, que dijo `coinciden: NO` y **nombro los dos actos que sobraban y
faltaban**, antes de que ninguna cifra saliera de ahi. **Corregido con la forma plural y con borde de
palabra, las dos vias calzan.** **Es el argumento a favor de medir por dos vias en vez de una.**

**11.5 MI PRIMERA PARTICION DE LOS ABIERTOS ERA FALSA.** Clasifique los actos abiertos como
`declarado` **o** `con dueno`, en ramas excluyentes, y dio **14 y 3**. **La particion no es
excluyente**: el `acto 24` es las dos cosas. **Lo cazo el contraste contra los quince del acta 73**, y
la correccion (declarar por la pagina y llamar `con dueno` solo a los NO declarados) da **15 y 2**,
que calza. **Ninguna cifra publicada salio de la version mala**, y la nota del `acto 24` de la seccion
6 es lo que quedo de esa averia.

**NINGUNA DE LAS CINCO CUENTA COMO CAIDA DE CLASE, DE CIFRA PUBLICADA NI DE REPORTE.** Las cinco las
cazo un instrumento o un cruce **antes** de que una cifra llegara a este fichero. **Se registran con
nombre, como esta mandado.**

---

## 12. PENDIENTES DE DOCTRINA Y PREGUNTAS PARA EL AUDITOR

**PENDIENTE DE DOCTRINA 1 (NUEVO, y es el que mas pesa): NINGUNA REGLA ESCRITA DICE SI UNA FASE PUEDE
CERRAR CON FUSIONES SIN HACER QUE DEPENDEN DE OTRA FASE.** La parada del 21 ago 2026 dispara cuando la
fase 03 quede `CERRADA Y VERIFICADA`, y **la letra que la campana tiene escrita habla de operaciones
con destino**. **Seis fichas de la fase 03 no tienen fusion hecha y las cinco mesas que las bloquean
son de la fase 06.** No paro por esto (regla 5: lo registro y sigo), **pero es la pieza que puede
cambiar la respuesta entera del cierre** y por eso va la primera.

**PENDIENTE DE DOCTRINA 2 (heredado): el subconjunto cerrado de un acto con puente**, pendiente 2 de
la linea **4061** de la pagina, **hoy con su tamano medido: DIEZ de los quince declarados citan
`P.10`**, que es el motivo al que el subconjunto aplica.

**PENDIENTE DE DOCTRINA 3 (heredado): el `INCISO` de condiciones sigue sin existir** (acta 55,
pregunta 5), y **4: la marca para *ya lo dice el `APPEND` de un hermano*** sigue sin marca propia
aunque su definicion ya este escrita. **Esta vuelta no toca ninguno de los dos.**

**PENDIENTE DE DOCTRINA 5 (heredado): el esquema de `OPERACIONES.jsonl`** (acta 55 en su cierre, acta
64 en su `D7`). **Esta vuelta lo LEE entero y no escribe ni un campo.**

### **PREGUNTAS, TRAIDAS EN VEZ DE ADIVINADAS** (regla 11)

**PREGUNTA 1. ?CUENTAN LAS SEIS FUSIONES PENDIENTES PARA EL CIERRE DE LA FASE 03?** Si cuentan, el
cierre **no esta cerca**: exige sentar cinco mesas. Si no cuentan (porque lo que las bloquea vive en
la fase 06 y la fase 03 no manda sobre ella), **entonces la fase 03 puede cerrar con seis fusiones
suyas sin hacer**, y eso hay que poder decirlo con una letra. **No tengo regla escrita para ninguna de
las dos lecturas y no invento una.**

**PREGUNTA 2. ?EL `ACTO 24` PESA EN LAS DOS COLUMNAS O EN UNA?** Esta `DECLARADO` **y** tiene dueno
(`OP-S-07`, el mismo del 37). Este reporte lo cuenta **entre los quince declarados** y **no** entre los
dos con dueno, que es como la vuelta 73 y el acta 73 lo contaron. **Es coherente, pero la coherencia
no es una regla**: si el cierre exige que todo acto con dueno se resuelva por su dueno, el 24 tambien
lo tiene.

**PREGUNTA 3. ?LA MESA `OP-M-03` ENTRA EN EL PAQUETE DEL CIERRE DE LA FASE 03 O NO?** Su ficha dice
`06_MESAS` (letra), y bloquea a `OP-M-03-III`, que es de la fase 03 (medicion). **Las dos son ciertas
y apuntan a lados distintos.** La misma pregunta vale para las otras cuatro mesas, que estorban
exactamente igual. **La traigo entera en vez de resolverla, porque resolverla es decidir el cierre.**

---

## 13. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Marcados ANTES de la relectura ciega del auditor**, que es la unica forma en que este marcado vale
algo. **TRECE.**

| | el discutible, dicho en contra de mi propia decision |
|---|---|
| **`D1`** | **IMPORTE `protegidos` en vez de copiarlo.** El `D14` del acta 68 fijo que el carril de COPIAR es el que protege a los instrumentos de vueltas distintas, y **yo importe** de `varas_n_arias_del_tramo.py`. Mi motivo esta escrito en el docstring: aqui el riesgo es el contrario, **dos listas de puertas divergiendo en silencio**. Pero es una excepcion a una regla vigente y **la marco yo mismo** |
| **`D2`** | **ESTRENE UNA RUTA DE AGUJA NUEVA** (`comprobar_promesas_de_marcado.py`) en el registrador. Mismo carril que el `D11` del acta 72 adjudico `A FAVOR`, **pero la costumbre de estrenar una por vuelta empieza a parecerse a una capacidad que se usa por inercia** |
| **`D3`** | **MEDI LOS DECLARADOS SOBRE LA PAGINA** cuando el instrumento de la casa (`tramo_al_cierre.py`) dice en su docstring que **no se pueden medir** y los recibe por argumento. **Mi via B es una regla de tokens que yo escribi**, y una regla de deteccion escrita en la misma vuelta que la usa es exactamente la especie que la campana desconfia |
| **`D4`** | **DEJE AL `ACTO 24` CONTADO EN UNA SOLA COLUMNA** aunque este `DECLARADO` y ademas tenga dueno. Elegi la lectura que calza con lo publicado, **y la lectura contraria (que su dueno lo saca de los quince) es sostenible** |
| **`D5`** | **LA REGLA `b.1` DEL DESTINO ES UNA LECTURA DE TEXTO, NO UNA MEDICION DE GRAFO**: distingue `CONSUMIDA` de `EJECUTADA` **buscando una palabra en el campo `nota`**. Si una ficha ejecutada trajera esa palabra por otro motivo, la clasificaria mal |
| **`D6`** | **PUBLICO LAS DOS COLUMNAS DE LA CABECERA IDENTICAS**, que es la forma exacta de la caida de la vuelta 56. Lo declaro y doy dos pruebas, **pero una cabecera identica sigue siendo una cabecera que nadie puede distinguir de la mala sin abrir los ficheros** |
| **`D7`** | **TRAIGO UNA PIEZA QUE EL ENCARGO NO PEDIA** (las seis fusiones pendientes). **Ensanchar el peso por mi cuenta es una decision**, y la lectura contraria es que el encargo enumero cuatro cosas y yo debia pesar cuatro |
| **`D8`** | **MEDI LAS CINCO MESAS** cuando el encargo preguntaba por una. Mismo motivo y misma objecion que el `D7` |
| **`D9`** | **LA COLUMNA `commits que la nombran` DEL BLOQUE 1 SE AUTO-REFERENCIA**: el commit de la `TAREA 2` nombra las dieciseis fichas, asi que re-correr el instrumento despues de committear sube esa columna **en exactamente uno por ficha**. Lo comprobe por `diff` de dos corridas. **La salida guardada es la PRE commit y eso queda dicho, pero es una cifra que se mueve sola** |
| **`D10`** | **EL REGISTRO DEL ACTA 73 NO LLEVA SECCION DE ADJUDICACIONES NUEVAS** porque el acta no la tiene: adjudica dentro de los discutibles. **Las saque de ahi y las agrupe en dos apartados**, lo cual es una re-organizacion editorial de un acta ajena |
| **`D11`** | **MI INSTRUMENTO ESCRIBE `LISTA` Y `PENDIENTE` EN SU TABLA DE VEREDICTO.** Es una etiqueta de forma y no de fondo, **pero un instrumento que etiqueta ya esta a un paso de decidir**, y el contrato de esta vuelta era medir |
| **`D12`** | **CORRI EL PASO DE ETIQUETAS DEL CICLO DE TRES DOS VECES** para arreglar la codificacion de una salida. Comprobe que `master_graph.json` quedo identico las dos veces, **pero re-correr un paso del ciclo por un motivo de forma es tocar el ciclo por algo que no es el ciclo** |
| **`D13`** | **BAJE DE DIEZ A NUEVE LOS ACTOS QUE CIERRAN POR `P.10` LEYENDO UNA SEDE A MANO.** El instrumento cuenta diez agujas; yo abri la del `acto 5` y vi que nombra `P.10` para negarlo. **Publico las dos cifras, pero la de nueve la sostiene MI lectura y no una maquina**, que es exactamente lo que la campana no deja pasar sin marcar |

---

## 14. RUTAS TOCADAS

| ruta | que le paso |
|---|---|
| `docs/plan/03_FUSIONES.md` | **`+235`, `0` borradas**: el registro del acta 73 adosado al final. **Unico fichero rastreado MODIFICADO en toda la vuelta** |
| `scripts/loop/_v74_texto_acta73.py` | **nuevo**, 265 lineas: el texto editorial del registro |
| `scripts/loop/_v74_construir_registrador_acta.py` | **nuevo**, 326 lineas: el constructor por extraccion |
| `scripts/loop/vuelta74_registrar_acta73.py` | **nuevo**, 432 lineas: el registrador, con la maquina copiada literal |
| `scripts/loop/vuelta74_peso_del_cierre.py` | **nuevo**, 550 lineas: el instrumento del peso, de solo lectura |
| `docs/loop/*V74*` | **29** salidas nuevas, **29 de 29 en `UTF-8`** |
| `docs/loop/REPORTE.md` | este fichero, sobrescrito |
| `dataset/` | **NADA**. `git diff` vacio en toda la vuelta |
| `docs/plan/OPERACIONES.jsonl`, `INVENTARIO.jsonl`, `RACIMOS_MIEMBROS.jsonl` | **NADA** |

---

## 15. LA TASA POR DOMINIO AL CIERRE, IDENTICA A LA DE APERTURA

**Las diez lineas salen de `SALIDA_V74_MARCADOR_CIERRE.txt` y el `diff` contra la de apertura da CERO
lineas.**

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

**VARA POR TRAMO, FIGURAS Y FAMILIAS: NO HAY NADA QUE PUBLICAR Y SE DICE POR QUE.** Esta vuelta **no
abrio ningun lote, no midio ninguna vara y no adjudico ninguna familia**, porque **no fundio**. **El
tramo al cierre** ([`SALIDA_V74_TRAMO_CIERRE.txt`](SALIDA_V74_TRAMO_CIERRE.txt)) da **47 filas, 30
`FUNDIDOS`, 17 con dos o mas vivos, 15 declarados y 2 con dueno**, **identico al de la vuelta 73**.
**Un cero que se publica con su motivo no es un hueco.**

---

## 16. HASH FINAL Y COMMITS

**LA CADENA ENTERA DE LA VUELTA 74, ESCRITA AQUI POR EL SEXTO COMMIT:** `46aee890` (la apertura),
`85a83352` (`TAREA 1`), `5a44b1cf` (`TAREA 2`), `36949269` (el cierre y las suites), `97bbddab` (el
reporte) **y este, que es el que puede escribir el hash del anterior.**
**`origin/pasada-unica` queda igual a `HEAD` y el arbol limpio de rastreados.**

**Los commits de esta vuelta en `pasada-unica`, en orden:**

| commit | que trae |
|---|---|
| **`46aee890`** | **la APERTURA medida antes de la primera operacion**: los seis instrumentos con el arbol limpio en `fee44694`, `CERO` rastreados movidos |
| **`85a83352`** | **`TAREA 1` entera**: el registro del acta 73 (`+235`, `0` borradas, 60 agujas, tres negativas de sustancia, idempotencia mordiendo) **mas la REGLA NUEVA de redaccion de las promesas de marcado, con sus tres formas citadas por aguja y no tecleadas** |
| **`5a44b1cf`** | **`TAREA 2` entera**: el instrumento del peso y su salida, con las dieciseis fichas, los quince declarados por dos vias, los duenos campo a campo, la mesa leida entera y **las seis fusiones pendientes destapadas** |
| **`36949269`** | **el CIERRE medido al cierre** y las tres suites: cabecera tallada, `Gate 0` con su ciclo de tres, motor, web, `tsc`, barrido, censo y el caso positivo de promesas |
| **`97bbddab`** | **el reporte**, este fichero, con la cabecera tallada y cotejada, los trece discutibles, las cinco averias y las tres preguntas |
| **este** | **la cabecera de esta seccion 16**, con el hash del commit del reporte y la cadena entera |

**El hash final de la vuelta y la cadena entera van escritos en la cabecera de esta seccion por un
commit posterior**, que es lo que la regla 7 pide y lo que el commit del reporte no puede contener: un
commit no puede llevar su propio hash. **Misma via que las vueltas 69 a 73 usaron en sus commits
`a943673c`, `66ef6d38`, `fd46adc3`, `fdb45f33` y `7afccb39`.**

**`origin/pasada-unica` queda igual a `HEAD` y el arbol limpio de rastreados.**

**EL BUCLE SIGUE. EL PESO ESTA ARMADO Y NO PESADO.**
