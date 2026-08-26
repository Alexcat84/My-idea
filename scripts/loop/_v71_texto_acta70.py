# -*- coding: utf-8 -*-
"""_v71_texto_acta70.py . EL TEXTO EDITORIAL DEL REGISTRO DEL ACTA 70.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo coteja y lo adosa es
scripts/loop/vuelta71_registrar_acta70.py, que lo importa. Vive aparte por la
misma razon por la que el contenido de un lote vive aparte del generador: para
que el fichero que MIDE y el fichero que DICE no se confundan. Es el mismo
reparto que las vueltas 66 a 70 usaron con _v66_texto_acta65.py,
_v67_texto_acta66.py, _v68_texto_acta67.py, _v69_texto_acta68.py y
_v70_texto_acta69.py.

AQUI NO HAY NI UN NUMERO DE LINEA TECLEADO. Cada cita va como marca [[CLAVE]] y
el registrador la sustituye por el numero que le devuelve BUSCAR la aguja de esa
clave en su fichero.

LO QUE ESTE TEXTO REGISTRA, y es lo que el encargo de la vuelta 71 pide: LA
CAIDA DE CIFRA PUBLICADA con su causa y el contador de parada en UNO DE DOS; las
DOS caidas de reporte con nombre; la ciega 6 de 6 con sus puestos y los tres
supervivientes ciegos; los catorce discutibles A FAVOR con su vara citada; las
cuatro adjudicaciones nuevas con sus letras; los pendientes heredados con su
destino; y LAS DOS CORRECCIONES DECLARADAS que esta vuelta aplica, la de las
celdas de cableado y la del defecto de --base de 6 a 7.
"""

TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 70, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 71, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **ONCE** veces, **y la cifra va con su medicion del dia al lado en vez
de heredada**: **NUEVE** llevan esta misma cabecera de nivel dos (de la del acta 61 a la del acta
69, contadas hoy por maquina sobre el fichero) y **DOS** son las mas viejas, que la pagina adoso con
cabecera de nivel tres. **La ultima de las once es la del acta 69 en la linea **[[PAG_ACTA69]]** y
la anterior la del acta 68 en la **[[PAG_ACTA68]]**, las dos cotejadas HOY abriendo el fichero.**
**Ninguna cifra publicada de arriba se toca.**

**NINGUNA CITA DE LINEA DE ESTA SECCION ESTA TECLEADA:** cada una es una marca que el registrador
sustituye por el numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de
escribir una sola letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero
de linea que aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe
nada**.

**El acta de la vuelta 70 abre en la linea **[[A70_ABRE]]** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por corrida propia en la
**[[A70_VERIF]]**, su relectura ciega en la **[[A70_CIEGA]]**, LA CAIDA DE CIFRA PUBLICADA en la
**[[A70_CAIDA]]**, las dos caidas de reporte en la **[[A70_REPORTE]]**, sus catorce adjudicaciones de
discutibles en la **[[A70_CATORCE]]**, sus cuatro adjudicaciones nuevas en la **[[A70_ADJUD]]**, su
metrica de credito en la **[[A70_METRICA]]** y sus condiciones de parada en la **[[A70_PARADAS]]**.

### a) **LA NOTICIA DE LA TANDA ES UNA CAIDA DE CIFRA PUBLICADA, Y VA PRIMERA PORQUE ES LA QUE MUEVE EL CONTADOR DE PARADA**

**La tanda 70 NO salio limpia**, y eso se registra **antes** que nada de lo que salio bien. **La
caida es UNA, de UNA sola causa, y no movio ningun dato.**

| | lo que el acta 70 mide, copiado de su linea | linea |
|---|---|---:|
| **el hecho** | el cableado de los `actos 34` y `36` se publico con el **conteo CRUDO de las listas de enlaces**, y el instrumento de la propia vuelta mide otra cosa | **[[A70_CAIDA_HECHO]]** |
| **las cifras crudas publicadas** | **6 contra 5 y 2** para el `34` y **5 contra 4 y 3** para el `36` | **[[A70_CAIDA_CRUDAS]]** |
| **las cifras del instrumento** | **6 contra 4 y 2** para el `34` y **4 contra 3 y 2** para el `36` | **[[A70_CAIDA_BUENAS]]** |
| **la causa, medida con el resolutor del propio instrumento** | los ids **no se pasaron por el resolutor**: un vecino que resuelve al mismo vivo que otro se conto dos veces, una arista repetida se conto dos veces, y un alias se conto aparte de su vivo | **[[A70_CAIDA_CAUSA]]** |
| **la letra que se incumplio** | el docstring del propio instrumento cita `P.1` con estas palabras: **TODO ID PASA POR EL RESOLUTOR ANTES DE CONTAR** | **[[A70_CAIDA_P1]]** |
| **lo que NO se movio, y se dice entero** | **ningun ganador cambia**, **el cableado no decidio en ninguno de los dos actos** (el `34` fue `TODAS DE ACUERDO` por contenido y el `36` fue `CHOCAN` resuelto por la pieza declarada) y **ni un veredicto ni el marcador se tocan** | **[[A70_CAIDA_NO_MUEVE]]** |
| **EL CONTADOR DE PARADA** | **PASA DE CERO A UNA TANDA**, y **dos tandas seguidas serian PARADA** | **[[A70_CAIDA_CONTADOR]]** |
| **la regla que sale de aqui, y vale desde el acta 70** | **TODA cifra de cableado que se publique sale de la columna `cab` del instrumento de varas, no de contar listas a mano** | **[[A70_ADJ3_REGLA]]** |

> **LO QUE ESTA VUELTA MIDE POR SU CUENTA Y DISCREPA DEL ACTA, DECLARADO EN VEZ DE COPIADO** (regla 2
> del ejecutor: un acta previa se cita como contraste, y **si discrepa de la medicion de hoy la
> discrepancia se declara**). **Las dos cifras del instrumento las re-corri yo en un worktree sobre el
> arbol de antes de fundir y salen identicas a las del acta**: `6 contra 4 y 2` y `4 contra 3 y 2`.
> **Lo que NO calza es la SEDE.** El acta nombra a esta pagina como sede de las dos celdas malas;
> **contado hoy por maquina sobre el fichero, esta pagina trae CERO ocurrencias de las dos cifras
> crudas**. **Donde SI viven es en el plan sellado del lote `F` y en el modulo de contenido que lo
> genero, y en forma abreviada en la tabla de varas del reporte de la vuelta 70**, que esta vuelta
> sobrescribe. **La correccion se adosa aqui igual, que es lo que el encargo manda y donde el registro
> queda**, y **el plan ejecutado NO se re-sella** por el carril del `D15` del acta 68.

### b) **CORRECCION DECLARADA, PRIMERA: LAS DOS CELDAS DE CABLEADO DE LOS `ACTOS 34` Y `36`**

**Se ADOSA y no se tacha, que es la unica forma en que una correccion se puede auditar.** **El texto
de arriba se queda entero donde esta**: el registro del `acto 34` sigue en la linea
**[[PAG_ACTO34]]**, con su celda de cableado en la **[[PAG_ACTO34_CABLE]]**, y el del `acto 36` en la
**[[PAG_ACTO36]]**, con su forma medida en la **[[PAG_ACTO36_FORMA]]**.

| acto | lo que el cableado mide, **leido HOY de la columna `cab` del instrumento** | quien apunta | decidio? |
|---:|---|---|---|
| **34** | **6 contra 4 y 2** | `ciclo_de_culpa` | **NO**: la forma es `TODAS DE ACUERDO` y el contenido no empata, asi que `P.8` no le da la palabra |
| **36** | **4 contra 3 y 2** | `matriz_de_control_de_proceso` | **NO**: la forma es `CHOCAN` y decide la pieza declarada |

> **LA CORRECCION NO MUEVE NI UN SUPERVIVIENTE NI UN VEREDICTO NI UNA CIFRA DEL MARCADOR, Y SE DICE
> ASI EN VEZ DE DEJARLO IMPLICITO:** **los dos ganadores del cableado son los mismos con las cifras
> crudas y con las buenas**, y **en los dos actos el cableado no fue lo que decidio**. **Lo que se
> corrige es la CIFRA, no la DECISION**, y por eso la correccion es una correccion y no una
> reapertura. **La medicion de hoy salio de correr `varas_n_arias_del_tramo.py` sobre un worktree del
> arbol previo a la fusion, no de copiar el acta.**

### c) **LAS DOS CAIDAS DE REPORTE, CON NOMBRE, PORQUE UNA CAIDA SIN NOMBRE NO SE CORRIGE**

**Las dos vivian solo en el reporte, no movieron dato y NO acumulan para la parada**, pero **las dos
dispararon la relectura al doble** y **una de ellas cambia lo que los lotes que vienen pueden
esperar**.

| | lo que el acta 70 mide, copiado de su linea | linea |
|---|---|---:|
| **1. las puertas de los que quedan NO son cero** | el reporte publico **cero puertas** en los que quedan **sin instrumento que lo midiera**; medido por el auditor con `varas_n_arias` sobre los **16**, **CUATRO tienen puertas** | **[[A70_REP_PUERTAS]]** |
| **cuales, nombradas una a una** | el `31` **UNA** (y ademas tiene dueno), el **`44` DOS**, el `46` **UNA** y el `51` **UNA** | **[[A70_PUERTAS_CUATRO]]** |
| **la especie de la caida** | **una busqueda no corrida afirmada como corrida**, que es exactamente lo que la disciplina del dictado prohibe | **[[A70_PUERTAS_ESPECIE]]** |
| **2. el desglose del `D3`** | el reporte dijo **tres siguientes y un previo** donde lo medido es **DOS siguientes y UN previo**; **la cifra total de cableado es la buena, el desglose no** | **[[A70_REP_D3]]** |
| **la racha de reporte** | queda en **UNA tanda** (la 69 vino limpia; **se necesitan tres seguidas**) | **[[A70_RACHA_REPORTE]]** |

### d) **LA RELECTURA CIEGA: 6 DE 6 COINCIDEN, CON SUS PUESTOS, MAS LOS TRES SUPERVIVIENTES ADJUDICADOS CIEGOS**

**El auditor leyo PRIMERO los textos enteros de los nodos en su version PRE fusion** (por `git show`
sobre el commit de la `TAREA 1` de la vuelta 70), **adjudico su clase y su superviviente, y SOLO
DESPUES destapo la razon escrita.** **Los seis puestos van nombrados uno a uno.**

| puesto | lo que el auditor adjudico ciego | linea |
|---:|---|---:|
| **880** | `A` **por contencion**, con residuo *el ethos y la transformacion de identidad*. Escrita `A`, y **su razon nombra ESE MISMO residuo** | **[[A70_CIEGA_880]]** |
| **2233** | `A`, **el mismo gesto**: sustituir el ritual de culpar y entrenar por analisis genuino de causas. Escrita `A` | **[[A70_CIEGA_2233]]** |
| **2272** | `A`, **el mismo ciclo de culpa contado dos veces por el mismo libro**. Escrita `A` | **[[A70_CIEGA_2272]]** |
| **2562** | `A`, **el mismo artefacto**. Escrita `A` | **[[A70_CIEGA_2562]]** |
| **2639** | `A` **con residuo capacitar y auditar**, y la razon **nombra exactamente esas dos lineas**. Escrita `A` | **[[A70_CIEGA_2639]]** |
| **279** | `B`, **la etapa entera contra la senal que vive dentro de ella**. Escrita `B`, **DUDOSO de su propio autor** | **[[A70_CIEGA_279]]** |
| **los TRES supervivientes, ademas** | `ciclo_de_culpa_2` en el `acto 34`, `construccion_tribu_de_marca` en el `35` y `plan_de_control` en el `36`, **elegidos ciegos y COINCIDENTES con lo ejecutado** | **[[A70_CIEGA_SUP]]** |
| **el saldo** | **CERO discrepancias en la ciega**, **pero DOS discrepancias FUERA de los discutibles marcados**: el credito de la tanda **BAJA** y **los dos tramos se releyeron AL DOBLE** | **[[A70_CIEGA_SALDO]]** |

### e) **LOS CATORCE DISCUTIBLES, ADJUDICADOS: LOS CATORCE `A FAVOR`, CON SU VARA**

**La cifra de cabecera y el detalle coinciden**: **catorce marcados, catorce adjudicados, cero sin
contestar**. **Y la lectura que hay que retener es la incomoda**: **los catorce marcados salieron a
favor y las dos discrepancias reales cayeron FUERA del marcado**, o sea que **marcar bien no es lo
mismo que medir bien**.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | el `acto 34` se funde pese a una entrada `familia_de_ids` que nombra a `OP-S-09` | **`A FAVOR`**, y la frontera queda adjudicada en el apartado g) de esta seccion | **[[A70_D1]]** |
| **`D2`** | la colision fabricada y la linea base | **`A FAVOR`**: predicha **antes de tocar un nodo**, sellada, publicada en rojo con su duena, y **CALZA al digito** en la re-simulacion del auditor; **ninguna letra manda parar por una colision predicha** | **[[A70_D2]]** |
| **`D3`** | el `acto 33` se funde contra un cableado ancho | **`A FAVOR` por la letra**: **el cableado solo habla a contenido empatado** y **la vara de pasos hablo**; el costo de redirigir esta **pagado y medido** | **[[A70_D3]]** |
| **`D4`** | el nodo de diez pasos | **`A FAVOR`** por el carril del catalogo mas rico (actas 67, 68 y 69), **y la ciega confirma que los dos `APPEND` son las dos lineas que la razon repone** | **[[A70_D4]]** |
| **`D5`** | dos nodos mas a ocho pasos | **`A FAVOR`**, mismo carril; **tres nodos de ocho o mas en un lote queda anotado como TENDENCIA para la fase 04**, no como regla nueva | **[[A70_D5]]** |
| **`D6`** | las dos razones del `34` coronan supervivientes distintos | **`A FAVOR`**: **cada corona es sobre SU par**, **las dos razones matan al mismo nodo** y `P.8` salio `TODAS DE ACUERDO`. **No hay DOS FAMILIAS que declarar** | **[[A70_D6]]** |
| **`D7`** | el `32` elige por cableado con margen de uno | **`A FAVOR`**: contenido empatado a tres bandas **es EL supuesto** en que `P.8` le da la palabra al cableado. **Margen de uno es margen** | **[[A70_D7]]** |
| **`D8`** | el `35` se funde contra la vara de pasos | **`A FAVOR`**: `CHOCAN` **lo decide la pieza declarada**, y **la ciega independiente eligio el mismo superviviente por el mismo fondo** | **[[A70_D8]]** |
| **`D9`** | seis `APPEND` de paso en un lote | **`A FAVOR`**; los seis son gestos que **las razones nombran como propios**; **el volumen queda anotado para la fase 04** | **[[A70_D9]]** |
| **`D10`** | el `33` triplica sus condiciones | **`A FAVOR`** por la puerta del acta 55 pregunta 5: **los tres disparadores son distintos** (reactivo, deliberado y de contexto) | **[[A70_D10]]** |
| **`D11`** | los nexos de los `INCISO` son cosecha propia | **`A FAVOR`**: **los cinco trozos son verbatim** (comprobados contra su fuente exacta) y **los cinco resultantes estan en el grafo** | **[[A70_D11]]** |
| **`D12`** | el fichero del marcador de apertura se genero al cierre | **`A FAVOR`**: la cifra **es la de la apertura y esta demostrado por `sha`**, y **la leccion va al encargo**: la apertura se talla con `recomputar_marcador.py` desde el principio | **[[A70_D12]]** |
| **`D13`** | dos instrumentos nuevos sin encargo | **`A FAVOR` con la distincion confirmada**: la adjudicacion 3 del acta 69 congelo **LAS TABLAS DE LOS REGISTRADORES**, no la creacion de instrumentos **DE MEDIDA** | **[[A70_D13]]** |
| **`D14`** | arreglar las regresiones propias en vez de declarar la base movida | **`A FAVOR`**: las causas eran de ficheros nuevos del ejecutor y **ninguna toca lo que los instrumentos miden**; **un verde falso seria CALLAR el barrido** | **[[A70_D14]]** |

### f) **ADJUDICACION 1: LA LINEA BASE OPERATIVA DEL CENSO DE COLISIONES PASA DE `6` A `7`, Y LA CORRECCION DECLARADA YA ESTA APLICADA SOBRE EL INSTRUMENTO**

**Es la adjudicacion que MUEVE una cifra, y por eso va con la correccion pegada al lado.** El carril
esta escrito en esta misma pagina, en la linea **[[PAG_LINEA_BASE]]**: **la duena de una colision que
fabrica una fusion es quien la fabrica**.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo adjudicado** | **la linea base pasa de `6` a `7`** | **[[A70_ADJ1]]** |
| **el carril, y es el CUARTO escalon del mismo** | **2 por el acta 64, 4 por el acta 66, 6 por el acta 69 y 7 por esta** | **[[A70_ADJ1_CARRIL]]** |
| **las tres condiciones que una colision cumple para entrar a la base** | **PREDICHA**, **PUBLICADA con duena sellada** y **REGISTRADA con sus puestos**; la del `acto 33` cumple las tres y esta registrada en esta pagina en la linea **[[PAG_COLISION_F]]** | **[[A70_ADJ1_TRES]]** |
| **el encargo al ejecutor** | aplicar la **CORRECCION DECLARADA** del defecto de `--base`, **con la aritmetica intacta** | **[[A70_ADJ1_ENCARGO]]** |

> **CORRECCION DECLARADA, SEGUNDA, APLICADA HOY:** el valor por defecto de `--base` de
> `scripts/loop/vuelta65_colisiones_esperadas.py` pasa de `6` a `7`, **con el texto viejo entero
> conservado en el docstring y en el sitio donde muerde, sin tachar nada**, y **con las DOS llamadas
> viejas citadas verbatim en un comentario encima de la nueva**. **Es el cuarto escalon del mismo
> carril.** **La guarda no cambia**: si el censo de ANTES no mide exactamente la base declarada, el
> instrumento cae en `ROJO` y dice *la base se mide, no se supone*.

### g) **ADJUDICACION 2: LA FRONTERA DEL DUENO SE LEE SOBRE SU SUJETO, Y EL `ACTO 34` ESTA BIEN FUNDIDO**

**Es la adjudicacion de mas peso del acta, y se registra entera porque manda sobre todo lo que
queda del tramo.**

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo adjudicado** | **el `acto 34` esta BIEN FUNDIDO y los `actos 3` y `7` quedan FIRMES** | **[[A70_ADJ2]]** |
| **el dueno MEDIDO, con sus TRES fuentes** | los **dos campos `duenos_*` del fichero fijado** y **el campo `operaciones` DE LA ENTRADA DEL ACTO** en el inventario | **[[A70_ADJ2_TRES]]** |
| **lo que NO es dueno** | una entrada de **OTRO tipo** (`familia_de_ids`) que nombra una operacion sobre **PARTE de la nomina**: es **jurisdiccion sobre SU sujeto**, no sobre el acto | **[[A70_ADJ2_FAMILIA]]** |
| **lo que la fusion SI le debe** | **dejarle su sujeto servible y publicarlo**, cosa que quedo medida y publicada | **[[A70_ADJ2_DEBE]]** |
| **lo que lo confirma** | **el precedente medido** (los `actos 3` y `7`, con entradas de la misma especie) **y la aritmetica**: todas las entradas de tipo `acto` del tramo nombran `OP-U-02`, **con lo que la lectura contraria vacia el universo entero de la operacion** | **[[A70_ADJ2_ARIT]]** |
| **su naturaleza** | **extension citable, no doctrina nueva** | **[[A70_ADJ2_EXT]]** |

> **COMO SE APLICA EN LOS LOTES QUE VIENEN, y por eso se registra aqui:** si un acto trae una entrada
> de esa especie, **se cita, se publica la consecuencia para la operacion nombrada, y se sigue**. El
> registro del `acto 34` queda donde esta, en la linea **[[PAG_ACTO34]]**, y **esta seccion es la
> adjudicacion encima**.

### h) **ADJUDICACION 4: EN LO QUE RESTA DEL TRAMO SI QUEDAN PUERTAS, ASI QUE LOS MOTIVOS DE `DECLARADO` POSIBLES SON DOS**

**Esta adjudicacion CORRIGE una premisa del reporte de la vuelta 70 con una medicion, y por eso se
registra: cambia lo que los lotes que vienen pueden esperar.**

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo medido** | **SI quedan puertas**: el `44` con **DOS**, el `46` y el `51` con **UNA**, y el `31` con una y con dueno | **[[A70_ADJ4_PUERTAS]]** |
| **los motivos de `DECLARADO` que quedan, y son DOS** | **la guarda `1B` con dos o mas puertas** (linea **[[PAG_GUARDA_1B]]**) y **la respuesta *DOS FAMILIAS* de `P.5`** (linea **[[PAG_P5_MOTIVO]]**) | **[[A70_ADJ4_DOS]]** |
| **el sujeto concreto de la guarda `1B`** | **el `acto 44`, cuando el prefijo lo alcance** | **[[A70_ADJ4_DOS]]** |
| **los actos `46` y `51`** | **funden con su puerta SOBREVIVIENDO** (acta 54, pregunta 1) | **[[A70_ADJ4_54]]** |
| **lo que queda SIN sujeto, y sigue igual** | **`P.10`** (linea **[[PAG_ACTO1_P10]]**), **el cuarto motivo** (linea **[[PAG_CUARTO_MOTIVO]]**) y **el transito del `EMPATE SIN VARA`** (linea **[[PAG_TRANSITO]]**) mientras ninguna forma salga asi | **[[A70_ADJ4_PUERTAS]]** |
| **su naturaleza** | **cero doctrina nueva: era una medicion que faltaba** | **[[A70_ADJ4_54]]** |

### i) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy.** **Y se dice como
se midieron**: el acta 70 **no los re-enumera en una lista propia** (comprobado abriendo el acta
hoy), asi que **su destino se lee de donde SI esta escrito**: la seccion de pendientes del registro
del acta 69 en esta misma pagina, linea **[[PAG_PENDIENTES]]**, y las lineas del acta 70 que los
tocan una a una.

| | lo que queda escrito, con su medicion | destino | linea |
|---|---|---|---:|
| **el subconjunto cerrado de un acto con puente** | siguen siendo **CATORCE** los actos declarados que esperan, **y el acta 70 los cuenta al cerrar** | **el cierre de la fase 03**, donde la parada de `AUDITOR.md` espera al fundador | **[[A70_CIERRE03_16]]** |
| **la marca para *ya lo dice el `APPEND` de un hermano*** | sigue **NOMBRADA** y su cuenta **se publica por maquina en cada lote**: el auditor reconto las **21** filas del plan sellado **una a una**, con **cero exclusiones que declarar** | **la cuenta crece y se publica en cada lote**, con la exclusion DICHA | **[[A70_PERDIDAS]]** |
| **el `INCISO` de condiciones** | **sigue sin existir**; el acta 70 lo toca en su `D10`, con los tres disparadores del `acto 33` medidos como distintos | **la fase 04** (acta 55, pregunta 5) | **[[A70_D10]]** |
| **el esquema de `OPERACIONES.jsonl`** | **sigue pendiente**; el acta 70 mide que **`OPERACIONES.jsonl` no se toco** en toda la vuelta, asi que **no se estreno ninguna clave** | **sin fecha, y se dice** | **[[A70_ESTADO_OPS]]** |
| **el cierre de la fase 03** | **NO SE CUMPLE TODAVIA**: quedan **16** actos sin destino y **48** nodos, **dos de ellos con dueno**, la mesa `OP-M-03` y los catorce declarados | **la parada escrita de `AUDITOR.md`, tal como esta** | **[[A70_CIERRE03]]** |

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO` SIGUEN SIENDO CUATRO Y LA LISTA SIGUE SIN
SER CERRADA**, pero **SOLO DOS TIENEN SUJETO EN LO QUE RESTA DEL TRAMO** por la adjudicacion 4 del
apartado h). **La linea base del censo de colisiones YA NO ES `6`: es `7`**, por la adjudicacion 1
del apartado f), y **el sitio donde la pagina la habia dejado en `4` no se reescribe**: queda donde
estaba, en la linea **[[PAG_LINEA_BASE]]**, y **esta seccion es la correccion declarada encima**.

### j) **LA METRICA DE CREDITO, REGISTRADA CON SU CIFRA Y NO CON SU ADJETIVO**

| | lo que el acta 70 mide | linea |
|---|---|---:|
| **el acumulado de relecturas y puestos** | **475** relecturas y **805** puestos | **[[A70_ACUMULADO]]** |
| **la racha de CLASE O CIFRA PUBLICADA** | **pasa de cero a UNA tanda**: **EL CONTADOR DE PARADA ESTA EN UNO DE DOS** | **[[A70_RACHAS]]** |
| **lo que decide la vuelta siguiente** | **si la tanda de la vuelta 71 trae otra caida de clase o de cifra publicada, ES PARADA** | **[[A70_RACHAS_71]]** |

### k) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba**, **NO funde ni deshace nada**, **NO elige ningun
superviviente**, **NO re-lee ni un veredicto de las siete colisiones vigentes**, **NO toca la mesa
`OP-M-03`**, **NO toca ninguna ficha de `OP-U-02` ni de `OPERACIONES.jsonl`**, **NO re-sella el plan
ejecutado del lote `F`** (carril del `D15` del acta 68), **NO anade ni una fila ni una columna a
ninguna tabla de registrador** (adjudicacion 3 del acta 69) y **NO abre el lote `G`**: **registra
adjudicaciones y declara DOS correcciones**. El lote `G` es la `TAREA 2` de esta misma vuelta y se
registra en su propia seccion, debajo de esta. **El registro del lote `F` de la vuelta 70 queda
intacto donde esta**, en la linea **[[PAG_LOTE_F]]**, y su cierre de tramo medido en la linea
**[[PAG_TRAMO_CIERRE_F]]**.
"""
