# -*- coding: utf-8 -*-
"""_v70_texto_acta69.py . EL TEXTO EDITORIAL DEL REGISTRO DEL ACTA 69.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo coteja y lo adosa es
scripts/loop/vuelta70_registrar_acta69.py, que lo importa. Vive aparte por la
misma razon por la que el contenido de un lote vive aparte del generador: para
que el fichero que MIDE y el fichero que DICE no se confundan. Es el mismo
reparto que las vueltas 66, 67, 68 y 69 usaron con _v66_texto_acta65.py,
_v67_texto_acta66.py, _v68_texto_acta67.py y _v69_texto_acta68.py.

AQUI NO HAY NI UN NUMERO DE LINEA TECLEADO. Cada cita va como marca [[CLAVE]] y
el registrador la sustituye por el numero que le devuelve BUSCAR la aguja de esa
clave en su fichero.

LO QUE ESTE TEXTO REGISTRA, y es lo que el encargo de la vuelta 70 pide: la
tanda limpia entera con el contador en cero y la racha de reporte rota; la ciega
5 de 5 con sus puestos; los catorce discutibles A FAVOR con su vara citada; las
cuatro adjudicaciones nuevas con sus letras; los pendientes heredados con su
destino; y la CORRECCION DECLARADA de la linea base, que esta vuelta aplica
sobre el instrumento.
"""

TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 69, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 70, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **DIEZ** veces, **y la cifra va con su medicion del dia al lado en vez
de heredada**: **OCHO** llevan esta misma cabecera de nivel dos (de la del acta 61 a la del acta 68,
contadas hoy por maquina sobre el fichero) y **DOS** son las mas viejas, que la pagina adoso con
cabecera de nivel tres (la del acta 52 en la linea **[[PAG_ACTA52]]** y la del acta 57 sobre el
`acto 25` en la **[[PAG_ACTA57]]**). **La ultima de las diez es la del acta 68 en la linea
**[[PAG_ACTA68]]** y la anterior la del acta 67 en la **[[PAG_ACTA67]]**, las cuatro cotejadas HOY
abriendo el fichero.** **Ninguna cifra publicada de arriba se toca.**

**NINGUNA CITA DE LINEA DE ESTA SECCION ESTA TECLEADA:** cada una es una marca que el registrador
sustituye por el numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de
escribir una sola letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero
de linea que aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe
nada**.

**El acta de la vuelta 69 abre en la linea **[[A69_ABRE]]** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por corrida propia en la
**[[A69_VERIF]]**, su relectura ciega en la **[[A69_CIEGA]]**, sus caidas en la **[[A69_CAIDAS]]**,
sus catorce adjudicaciones de discutibles en la **[[A69_CATORCE]]**, sus cuatro adjudicaciones nuevas
en la **[[A69_ADJUD]]**, su metrica de credito en la **[[A69_METRICA]]** y sus condiciones de parada
en la **[[A69_PARADAS]]**.

### a) **LA TANDA 69 QUEDO LIMPIA ENTERA, Y ESO SE REGISTRA CON EL MISMO CUIDADO CON EL QUE SE REGISTRA UNA CAIDA**

**Una tanda limpia que solo vive en un acta se olvida igual que una caida que solo vive en un acta**,
y por eso entra aqui con su medicion al lado y no como un elogio.

| | lo que el acta 69 mide, copiado de su linea | linea |
|---|---|---:|
| **caidas del ejecutor: de CLASE, de CIFRA PUBLICADA y de REPORTE** | **CERO, CERO y CERO**; **toda cifra del reporte que el auditor toco calzo al digito con su corrida** | **[[A69_CAIDAS_CERO]]** |
| **el contador de parada** | **SIGUE EN CERO**, con **dos tandas limpias seguidas** (la 68 y la 69) | **[[A69_RACHAS]]** |
| **la racha de reporte** | **VUELVE A CERO**: la caida del `D9` de la vuelta 68 **quedo en UNA** | **[[A69_RACHAS]]** |
| **la regla que salio de aquella caida, estrenada y funcionando** | la cuenta agregada **por maquina** con **la exclusion DICHA**: el auditor reconto las 21 filas del plan sellado **fila a fila** y **leyo entera la fila 5**, que describe el mecanismo del pendiente 4 en su prosa y **NO lleva la frase sellada**; la cuenta buena es **14** | **[[A69_PERDIDAS_FILA5]]** |
| **el acumulado del credito** | **469 relecturas**, **799 puestos**, 7 caidas de clase, 28 de reporte del ejecutor, 14 de cifra publicada del ejecutor, 3 de cifra del auditor, 7 de acta del auditor y 4 de procedimiento del auditor | **[[A69_ACUMULADO]]** |
| **las caidas del auditor** | **CERO**, con **TRES manejos propios declarados** y sin cifra publicada de por medio | **[[A69_MANEJOS]]** |

> **LO QUE LA REGLA NUEVA VALE PARA TODO LOTE, y por eso se copia aqui en vez de dejarla en el
> acta:** **la cuenta agregada se cuenta por maquina en la corrida de la vuelta**, y **si una fila
> queda fuera de la cuenta, la frase lo DICE**. **El lote `F` de esta misma vuelta la aplica igual.**

### b) **LA RELECTURA CIEGA: 5 DE 5 COINCIDEN, CON SUS PUESTOS, MAS LOS DOS SUPERVIVIENTES ADJUDICADOS CIEGOS**

**El auditor leyo PRIMERO los pasos de los nodos en su texto PRE fusion** (por `git show` sobre el
commit de la `TAREA 1` de la vuelta 69), **adjudico su clase, y SOLO DESPUES destapo la razon
escrita.** **Es la mitad del procedimiento que hace creible el resultado**, y por eso los cinco
puestos van nombrados uno a uno.

| puesto | lo que el auditor adjudico ciego | linea |
|---:|---|---:|
| **2838** | `A` **por contencion** con superviviente `viaje_diagnostico_remedial`, **y hasta el mismo residuo**: la lectura contraria del Pareto y la validacion estadistica es defendible. **La razon escrita dice eso mismo** | **[[A69_CIEGA_2838]]** |
| **839** | `A`, **el mismo instrumento entero con parametros propios a cada lado**. Escrita `A` | **[[A69_CIEGA_839]]** |
| **775** | `B`, **el marco entero contra una regla de enfasis sobre una de sus etapas**. Escrita `B` | **[[A69_CIEGA_775]]** |
| **220** y **482** | `A` y `A`, **repeticion del gesto de Rackham**; en el segundo el marco anade la taxonomia completa. Escritas `A` y `A` | **[[A69_CIEGA_220]]** |
| **los dos supervivientes, ademas** | `marco_avances_continuaciones` en el `acto 29` y `viaje_diagnostico_remedial` en el `acto 30`, **elegidos ciegos y COINCIDENTES con lo ejecutado** | **[[A69_CIEGA_SUP]]** |
| **el saldo** | **CERO discrepancias y CERO fuera del marcado**: el credito de la tanda **queda entero** y **no hay tramo al doble** | **[[A69_CIEGA_CERO]]** |

### c) **LOS CATORCE DISCUTIBLES, ADJUDICADOS: LOS CATORCE `A FAVOR`, CON SU VARA**

**La cifra de cabecera y el detalle coinciden**: **catorce marcados, catorce adjudicados, cero sin
contestar**, y **ninguna discrepancia fuera de la lista**.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | la fusion del `acto 25` fabrica **dos colisiones de clase** | **`A FAVOR`**: predichas **antes de tocar un nodo**, selladas, publicadas en rojo con su duena y **CALZAN al digito** en la re-simulacion del auditor; **ninguna letra manda deshacer una fusion por una colision predicha** | **[[A69_D1]]** |
| **`D2`** | la puerta del `acto 26` a nueve pasos | **`A FAVOR`** por el carril del `D8` del acta 67 y del `D4` del acta 68; **la redaccion de un nodo de nueve pasos es asunto de la fase 04** | **[[A69_D2]]** |
| **`D3`** | cuatro `INCISO` en el `acto 30` | **`A FAVOR`**: **ninguno apilado**, pasos receptores **sin punto final**, resultantes **impresos y leidos** por el auditor | **[[A69_D3]]** |
| **`D4`** | el racimo del `acto 29` tocado a medias | **`A FAVOR`**: **la particion 3 mas 2 esta MEDIDA** y la fusion opera **sobre los dos sueltos** | **[[A69_D4]]** |
| **`D5`** | el **2838** con discutible fuerte de su propio autor | **`A FAVOR`**: la ciega independiente dio **la misma clase y el mismo superviviente**, y el reparto conserva por `INCISO` lo que haria valer la lectura contraria | **[[A69_D5]]** |
| **`D6`** | una sola vara con margen 2 contra 1 | **`A FAVOR`**: **donde el contenido dice algo el contenido manda**, y la eleccion ciega cayo en el mismo superviviente **por la misma vara** | **[[A69_D6]]** |
| **`D7`** | el tope del lote lo eligio un acto con dueno | **`A FAVOR`**: el contrato es **entregar lo declarado**, y **saltarse el 31 romperia el prefijo** | **[[A69_D7]]** |
| **`D8`** | la fila de figura en `tabla_declarado` sin encargo | **`A FAVOR`** con las condiciones del acta 61 cumplidas, **y la advertencia del propio ejecutor atendida**: la tabla **queda CONGELADA** | **[[A69_D8]]** |
| **`D9`** | cuatro perdidas con `ATENUANTE DECLARADO Y MEDIDO` | **`A FAVOR`** por el carril del `D10` del acta 68 (**el sello es del reparto y no del resultado**), **con la cuenta por maquina al lado para restarlas** | **[[A69_D9]]** |
| **`D10`** | la fila 5 sin la frase sellada, **14** y no **15** | **`A FAVOR`**: la cuenta por maquina **mide la frase sellada** y **la exclusion va DICHA**; **un plan ejecutado no se re-sella** | **[[A69_D10]]** |
| **`D11`** | el plan sellado dos veces | **`A FAVOR`**, el mismo carril del `D15` de la vuelta 68; **el diff es UNA linea y el auditor lo corrio** | **[[A69_D11]]** |
| **`D12`** | los nexos de los `INCISO` son cosecha propia | **`A FAVOR`**: **el trozo es verbatim** (comprobado por el auditor) y **el nexo minimo evita pasos ilegibles** | **[[A69_D12]]** |
| **`D13`** | ocho perdidas en el `acto 26` | **`A FAVOR`**: el **839** sostiene la fusion (**la ciega tambien lo dio `A`**) y **las ocho estan selladas con destino** | **[[A69_D13]]** |
| **`D14`** | dos puertas crecen el mismo dia | **`A FAVOR`**: **con UNA puerta el acto funde y la puerta sobrevive** (acta 54, pregunta 1), aplicado dos veces con su letra | **[[A69_D14]]** |

### d) **ADJUDICACION 1: LA LINEA BASE OPERATIVA DEL CENSO DE COLISIONES PASA DE `4` A `6`, Y LA CORRECCION DECLARADA YA ESTA APLICADA SOBRE EL INSTRUMENTO**

**Es la adjudicacion que MUEVE una cifra, y por eso va primero y con la correccion pegada al lado.**
El carril esta escrito en esta misma pagina, en la linea **[[PAG_LINEA_BASE]]**: **la duena de una
colision que fabrica una fusion es quien la fabrica**.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo adjudicado** | **la linea base pasa de `4` a `6`** | **[[A69_ADJ1]]** |
| **el carril, y no es nuevo** | **el mismo con el que la base paso de 2 a 4** (acta 66, pregunta 2, con la correccion declarada de la vuelta 67) | **[[A69_ADJ1_CARRIL]]** |
| **las tres condiciones que una colision cumple para entrar a la base** | **PREDICHA**, **PUBLICADA** y **con DUENA sellada**; **las dos nuevas cumplen las tres** y estan registradas en esta pagina con sus puestos, en la linea **[[PAG_COLISIONES_E]]** | **[[A69_ADJ1]]** |
| **el encargo al ejecutor** | aplicar en `TAREA 1` la **CORRECCION DECLARADA** sobre el defecto de `--base` de `vuelta65_colisiones_esperadas.py` | **[[A69_ADJ1_ENCARGO]]** |
| **lo que NO se toca, y se dice** | **LA ARITMETICA**: la guarda **sigue midiendo la base sobre el arbol** y **comparando esperadas contra medidas** | **[[A69_ADJ1_ARIT]]** |

> **LA CORRECCION, APLICADA HOY Y DECLARADA COMO LA DE LA VUELTA 67:** el valor por defecto de
> `--base` de `scripts/loop/vuelta65_colisiones_esperadas.py` pasa de `4` a `6`, **con el texto viejo
> entero conservado en el docstring y en el sitio donde muerde, sin tachar nada**, y **con la llamada
> vieja citada verbatim en un comentario encima de la nueva**. **Es el segundo escalon del mismo
> carril**: 2 por el acta 64, 4 por el acta 66 y 6 por el acta 69. **La guarda no cambia**: si el
> censo de ANTES no mide exactamente la base declarada, el instrumento cae en `ROJO` y dice *la base
> se mide, no se supone*.

### e) **ADJUDICACION 2: EL `ACTO 31` NO ES UNA FUSION DE `OP-U-02`, Y EL PREFIJO DEL LOTE `F` ABRE EN EL `32`**

**Adjudicado por el criterio del propio plan escrito en la ficha de `OP-U-02`**, no por doctrina
nueva.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo adjudicado** | **el `acto 31` NO es una fusion de `OP-U-02` y el prefijo del lote `F` ABRE EN EL `32`** | **[[A69_ADJ2]]** |
| **la letra que lo sostiene** | **la ficha de `OP-U-02`** (criterio del propio plan, con correccion declarada de la vuelta 48): **los actos que ya tienen dueno en otra operacion NO se cuentan como fusiones que el recomputo abra** | **[[A69_ADJ2_LETRA]]** |
| **el dueno, MEDIDO** | `OP-F-04-WEI` y `OP-S-04`, **y ademas el acto no trae ningun motivo sellado de `DECLARADO`** | **[[A69_ADJ2_DUENO]]** |
| **por que el salto NO rompe el prefijo sin saltos** | **porque el `31` no esta en la cola de fusiones de `OP-U-02`**: su destino queda con sus duenos en sus fases, y **el salto va DECLARADO con esta cita** | **[[A69_ADJ2_SALTO]]** |
| **y lo mismo para el `37`** | **`OP-S-07`**, cuando el prefijo lo alcance | **[[A69_ADJ2_37]]** |

### f) **ADJUDICACION 3: `tabla_declarado` QUEDA CONGELADA, Y NINGUNA TABLA DE REGISTRADOR CRECE SIN ENCARGO**

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo que se queda** | **la fila de duenos** (vuelta 68) **y la de figura** (vuelta 69): **las dos entraron con docstring y marcado**, que son las condiciones del acta 61 | **[[A69_ADJ3]]** |
| **la regla, desde el acta 69** | **ninguna fila ni columna nueva entra a las tablas de los registradores sin encargo previo del auditor** | **[[A69_ADJ3_REGLA]]** |

> **ESTA SECCION SE ESCRIBE BAJO ESA REGLA Y SE DICE:** el registrador del lote `F` de esta misma
> vuelta **copia la maquina del de la vuelta 69 SIN ANADIRLE NI UNA FILA NI UNA COLUMNA**, y lo unico
> propio son sus agujas, sus anclas y su texto. **Una tabla que crece sola es lo que esta
> adjudicacion viene a parar.**

### g) **ADJUDICACION 4: EL RESTO DEL TRAMO NO TRAE PUENTES NI PARES `D` INTERNOS, ASI QUE `P.10` Y EL CUARTO MOTIVO QUEDAN SIN SUJETO**

**Esta es la adjudicacion que MANDA sobre lo que el lote `F` puede esperar**, y por eso se registra
aunque no encargue trabajo por si sola.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **lo medido** | **en lo que resta del tramo no hay actos con nodo puente ni con par `D` interno** | **[[A69_ADJ4]]** |
| **la medicion del auditor, aparte** | **47 filas, cerrados 26, quedan 21 actos y 63 nodos**, recontados por el | **[[A69_TRAMO]]** |
| **cero y cero, recontados sobre el instrumento** | **cero con par `D` interno** (sobre `clases_internas`) y **cero con nodo puente** (instrumento re-corrido sobre los 21) | **[[A69_TRAMO_PUENTES]]** |
| **que queda sin sujeto** | **`P.10`** (el triangulo, linea **[[PAG_ACTO1_P10]]**) y **el cuarto motivo** (el `D` directo interno, linea **[[PAG_CUARTO_MOTIVO]]**) | **[[A69_ADJ4]]** |
| **de donde saldran los cierres `DECLARADO` que vengan** | **de la guarda `1B` con DOS o mas puertas** (linea **[[PAG_GUARDA_1B]]**), **de la respuesta *DOS FAMILIAS* de `P.5`** (linea **[[PAG_P5_MOTIVO]]**) **o del transito de un `EMPATE SIN VARA`** (linea **[[PAG_TRANSITO]]**) | **[[A69_ADJ4_SALEN]]** |
| **el aviso sobre el ritmo** | **los lotes que vienen seran casi todos fusiones y el ritmo de colisiones puede subir**: **cada una sigue exigiendo prediccion, sello y duena, SIN EXCEPCION POR VOLUMEN** | **[[A69_ADJ4_VOLUMEN]]** |

### h) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy.** **Y se dice como
se midieron**: el acta 69 **no los re-enumera en una lista propia** (medido abriendo el acta hoy: su
seccion 5 trae las cuatro adjudicaciones nuevas, y el pendiente 6 va entre ellas), asi que **su
destino se lee de donde SI esta escrito**: la seccion de los pendientes del acta 68 en esta misma
pagina, linea **[[PAG_PENDIENTES68]]**, y las lineas del acta 69 que los tocan una a una.

| | lo que queda escrito, con su medicion | destino | linea |
|---|---|---|---:|
| **el subconjunto cerrado de un acto con puente** | ahora son **CATORCE** los actos declarados que esperan, con el `acto 27` de la vuelta 69 sumado (linea **[[PAG_ACTO27]]**) | **el cierre de la fase 03**, donde la parada de `AUDITOR.md` espera al fundador | **[[A69_CIERRE03_CATORCE]]** |
| **la marca para *ya lo dice el `APPEND` de un hermano*** | sigue **NOMBRADA** y **su cuenta ya no es anecdotica**: la vuelta 69 la pago **SEIS** veces, y el auditor reconto las filas **una a una** leyendo entera la que no lleva la frase sellada | **la cuenta crece y se publica en cada lote**, con la exclusion DICHA | **[[A69_PERDIDAS_FILA5]]** |
| **el `INCISO` de condiciones** | sigue sin existir; el acta 69 lo toca en su `D3` y en su `D12`, **con los cuatro `INCISO` del `acto 30` leidos y los nexos comprobados** | **la fase 04** (acta 55, pregunta 5) | **[[A69_D12]]** |
| **el esquema de `OPERACIONES.jsonl`** | sigue **pendiente**; el barrido del auditor sobre los 18 miembros del lote `E` devolvio **UNA sola mencion** y **una mencion en el campo `evidencia` NO es dueno** | **sin fecha, y se dice** | **[[A69_OPS_MENCION]]** |
| **el cierre de la fase 03** | **NO SE CUMPLE TODAVIA**: quedan **21 actos y 63 nodos**, **dos actos con dueno**, la mesa `OP-M-03` y los catorce declarados | **la parada escrita de `AUDITOR.md`, tal como esta** | **[[A69_CIERRE03]]** |

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO` SIGUEN SIENDO CUATRO Y LA LISTA SIGUE SIN
SER CERRADA**, pero **DOS DE ELLOS SE QUEDAN SIN SUJETO EN LO QUE RESTA DEL TRAMO** por la
adjudicacion 4 del apartado g). **La linea base del censo de colisiones YA NO ES `4`: es `6`**, por
la adjudicacion 1 del apartado d), y **el sitio donde la pagina la habia dejado en `4` no se
reescribe**: queda donde estaba, en la linea **[[PAG_LINEA_BASE]]**, y **esta seccion es la
correccion declarada encima**.

### i) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba**, **NO funde ni deshace nada**, **NO elige ningun
superviviente**, **NO re-lee ni un veredicto de las seis colisiones vigentes**, **NO toca la mesa
`OP-M-03`**, **NO toca ninguna ficha de `OP-U-02` ni de `OPERACIONES.jsonl`**, **NO anade ni una fila
ni una columna a ninguna tabla de registrador** (adjudicacion 3) y **NO abre el lote `F`**:
**registra adjudicaciones y declara una correccion**. El lote `F` es la `TAREA 2` de esta misma
vuelta y se registra en su propia seccion, debajo de esta. **El registro del lote `E` de la vuelta 69
queda intacto donde esta**, en la linea **[[PAG_LOTE_E]]**, **con su cierre de tramo medido en la
[[PAG_TRAMO_CIERRE_E]]**.
"""
