# -*- coding: utf-8 -*-
"""_v69_texto_acta68.py . EL TEXTO EDITORIAL DEL REGISTRO DEL ACTA 68.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo coteja y lo adosa es
scripts/loop/vuelta69_registrar_acta68.py, que lo importa. Vive aparte por la
misma razon por la que el contenido de un lote vive aparte del generador: para
que el fichero que MIDE y el fichero que DICE no se confundan. Es el mismo
reparto que las vueltas 66, 67 y 68 usaron con _v66_texto_acta65.py,
_v67_texto_acta66.py y _v68_texto_acta67.py.

AQUI NO HAY NI UN NUMERO DE LINEA TECLEADO, que es la correccion que la vuelta
68 estreno y que el encargo de esta vuelta repite con todas sus letras. Cada
cita va como marca [[CLAVE]] y el registrador la sustituye por el numero que le
devuelve BUSCAR la aguja de esa clave en su fichero.
"""

TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 68, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 69, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **NUEVE** veces, la ultima de ellas la del acta 67 en la linea
**[[PAG_ACTA67]]** y la anterior la del acta 66 en la **[[PAG_ACTA66]]**, **las dos cotejadas HOY
abriendo el fichero**. **Ninguna cifra publicada de arriba se toca.**

**NINGUNA CITA DE LINEA DE ESTA SECCION ESTA TECLEADA**, que es el procedimiento que la vuelta 68
estreno y que esta vuelta hereda entero: cada una es una marca que el registrador sustituye por el
numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de escribir una sola
letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero de linea que
aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe nada**.

**El acta de la vuelta 68 abre en la linea **[[A68_ABRE]]** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por corrida propia en la
**[[A68_VERIF]]**, su relectura ciega en la **[[A68_CIEGA]]**, sus caidas en la **[[A68_CAIDAS]]**,
sus dieciseis adjudicaciones en la **[[A68_DIECISEIS]]**, sus adjudicaciones nuevas y sus pendientes
en la **[[A68_ADJUD]]**, su metrica de credito en la **[[A68_METRICA]]** y sus condiciones de parada
en la **[[A68_PARADAS]]**.

### a) **LA CAIDA DE REPORTE DEL EJECUTOR, CON SU NOMBRE Y SU MEDICION: EL `D9` DIJO CUATRO Y LO MEDIDO ES SEIS**

**Se registra aqui, y no solo en el acta, porque una caida que solo vive en un acta se olvida.** **Y
se dice primero lo que NO cayo**: la cuenta equivocada vivia **solo en `REPORTE.md`**, **esta pagina
publica la tabla entera de perdidas con sus atenuantes verbatim y NO publica esa cuenta agregada**, y
**ninguna cifra de `docs/plan/` ni del banco se movio**.

| | lo que el acta 68 mide, copiado de su linea | linea |
|---|---|---:|
| **lo que el reporte dijo** | **el `D9` del reporte de la vuelta 68 dice CUATRO perdidas con atenuante declarado** | **[[A68_CAIDA_MEDICION]]** |
| **lo que el auditor midio** | contadas por el auditor sobre el plan sellado y sobre el registro, **fila a fila: SEIS filas llevan `ATENUANTE DECLARADO` en su campo `que`** | **[[A68_CAIDA_SEIS]]** |
| **las seis filas, nombradas** | **las filas 3, 4, 7, 8, 9 y 10** | **[[A68_CAIDA_FILAS]]** |
| **la mitad que si era exacta** | **DOS de las seis son de la especie del pendiente 4**, las filas 8 y 10 | **[[A68_CAIDA_DOS]]** |
| **la lectura con la que el cuatro se entiende, y por que no basta** | excluir la fila 9, que el `D10` cuenta aparte, y la fila 7, que el `D8` cuenta aparte; **pero la frase publicada no dice eso: dice cuatro y son seis** | **[[A68_CAIDA_LECTURA]]** |
| **la especie** | **CAIDA DE REPORTE**: se registra con nombre, dispara la relectura al doble del tramo y **NO acumula para la parada** | **[[A68_ESPECIE]]** |
| **la relectura al doble, ejecutada** | el tramo es la tabla de perdidas, **releida ENTERA y DOS VECES** (las 11 filas en el plan sellado y las 11 en el registro), **con la cuenta de atenuantes hecha por dos vias** | **[[A68_RELECTURA_DOBLE]]** |
| **la cuenta buena, contada fila a fila por el auditor** | **11 filas**, especies **7 `DE PARAMETRO DE PASO`** y **4 `DE CONDICIONES`**; **DOS filas con dos sedes** en el campo `donde`; **SEIS con atenuante declarado**; y las **CUATRO `DE CONDICIONES`** del pendiente son las filas 5, 6, 10 y 11 | **[[A68_PERDIDAS_FILA]]** |

> **LA REGLA QUE SALE DE ESTA CAIDA, y vale desde hoy para todo lote:** **toda cuenta agregada que se
> publique sobre una tabla** (cuantas filas cumplen `X`) **se deriva CONTANDO POR MAQUINA en la
> corrida de esa vuelta, no de memoria del reparto**; y **si se excluyen filas de una cuenta porque
> otro discutible las cubre, la frase lo DICE**. **Una cuenta que el autor recuerda no es una cuenta
> medida**, que es la misma familia de la regla 2 del ejecutor (*el instrumento manda*) aplicada al
> agregado y no solo a la celda.

### b) **EL CONTADOR DE PARADA VUELVE A CERO, Y LA RACHA DE REPORTE SE ROMPE EN LA CUARTA**

**Se escribe con estas letras porque manda sobre esta vuelta y sobre la siguiente.**

| | lo medido al cierre de la tanda 68 | linea |
|---|---|---:|
| **caidas de CLASE y de CIFRA PUBLICADA** | **CERO y CERO** | **[[A68_CAIDAS]]** |
| **caidas de REPORTE** | **UNA**, la cuenta del `D9` | **[[A68_CAIDAS]]** |
| **el contador de parada** | **VUELVE A CERO**: la 67 lo dejo en UNO, la parada pide **DOS TANDAS SEGUIDAS** con caida de clase o de cifra publicada, y **la segunda no llego** | **[[A68_EFECTO_CREDITO]]** |
| **la racha de reporte** | **ROTA en la cuarta tanda**, con **UNA** caida; **TRES seguidas de esta especie si serian `PARADA`** | **[[A68_EFECTO_CREDITO]]** |
| **las rachas escritas juntas** | **CLASE O CIFRA EN CERO otra vez**; **REPORTE roto en la cuarta** | **[[A68_RACHAS]]** |
| **el acumulado** | **464 relecturas, 794 puestos, 7 caidas de clase, 28 de reporte del ejecutor, 14 de cifra publicada del ejecutor, 3 de cifra del auditor, 7 de acta del auditor y 4 de procedimiento del auditor** | **[[A68_ACUMULADO]]** |

### c) **LOS DIECISEIS DISCUTIBLES, ADJUDICADOS: LOS DIECISEIS `A FAVOR`, CON LA CUENTA DEL `D9` CAIDA APARTE**

**La cifra de cabecera y el detalle coinciden**: **dieciseis marcados, dieciseis adjudicados, cero
sin contestar**, y **la unica discrepancia del dia no esta en la lista sino en una cuenta**, que es
lo que el apartado a) registra.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | el ensanche de la guarda de citas con cuatro mecanismos donde el encargo pedia dos | **`A FAVOR`**: las dos condiciones del acta 61 cumplidas, y **los dos mecanismos de mas son guardas que aprietan**, justificadas por la especie exacta de la caida de la 67 | **[[A68_D1]]** |
| **`D2`** | fundir el `acto 22`, bloque de cuatro de un racimo cuyo inventario dice *en mesa* | **`A FAVOR`**, y **la pregunta 5 queda adjudicada** (apartado e): el dueno es **EL MEDIDO**, la particion **calza al digito** y el precedente es doble | **[[A68_D2]]** |
| **`D3`** | el superviviente del `acto 22` contra el cableado 7 a 3 | **`A FAVOR`**: **`P.8` es regla de PRELACION** y la vara de pasos hablo; **el cableado solo decide a contenido empatado** | **[[A68_D3]]** |
| **`D4`** | el nodo de nueve pasos | **`A FAVOR`** por el carril del `D8` del acta 67; **la redaccion fina es de la fase 04** | **[[A68_D4]]** |
| **`D5`** | tres `APPEND` de condicion en el `acto 19` | **`A FAVOR`**: la vara del acta 55 pregunta 5 es **disparador DISTINTO**, y **los tres lo son**; tres de golpe es **volumen, no una regla rota** | **[[A68_D5]]** |
| **`D6`** | el `acto 18` en transito sin superviviente elegido | **`A FAVOR`**: es **el carril que el acta 67 adjudico, ejecutado a la letra**; el costo de seis cerrados en vez de siete **es el diseno del carril, no una perdida** | **[[A68_D6]]** |
| **`D7`** | declarar el lote en seis | **`A FAVOR`**: el encargo manda **declarar al abrir y entregar lo declarado**, y **ninguna letra fija el tamano** | **[[A68_D7]]** |
| **`D8`** | dos perdidas con dos sedes en una fila | **`A FAVOR`**: es la aplicacion consciente del `D10` del acta 67, **la fila es POR PIEZA** | **[[A68_D8]]** |
| **`D9`** | sobre-sellar perdidas con atenuante declarado | **LA PRACTICA `A FAVOR`** (declarar es mas auditable que callar), **con LA CUENTA CAIDA aparte**: la buena es **SEIS**, dos del pendiente 4 | **[[A68_D9]]** |
| **`D10`** | sellar la perdida que el `INCISO` del mismo acto repara | **`A FAVOR`**: **el sello es del reparto y no del resultado**, y el atenuante medido evita el doble conteo | **[[A68_D10]]** |
| **`D11`** | un `CUBIERTO` que apunta al superviviente cuando el contenido llega por el `APPEND` del hermano | **`A FAVOR`** como **la mejor marca DISPONIBLE** mientras el pendiente 4 no tenga marca propia, con la perdida declarandolo | **[[A68_D11]]** |
| **`D12`** | los dos `INCISO` con nexo de coma sobre pasos que no terminan en punto | **`A FAVOR`**: la guarda de la **JUNTURA ROTA** cubre la especie del `D5` del acta 66 y **aqui no aplica** | **[[A68_D12]]** |
| **`D13`** | la fila de duenos en `tabla_declarado` sin encargo | **`A FAVOR`** con las dos condiciones del acta 61 cumplidas: **una razon de cierre que solo vive en la prosa se pierde** | **[[A68_D13]]** |
| **`D14`** | importar la guarda en vez de copiarla | **`A FAVOR` CON LA REGLA DICHA**: el carril de copiar protege a los registradores de **VUELTAS DISTINTAS**; **dentro de LA MISMA vuelta el import garantiza identidad mejor que la copia** | **[[A68_D14]]** |
| **`D15`** | el plan sellado dos veces | **`A FAVOR`**: el diff de sellos esta **medido en UNA linea** y **el plan no se habia ejecutado**; **un plan EJECUTADO no se re-sella** | **[[A68_D15]]** |
| **`D16`** | leer entero y declarar el acto con dueno en vez de saltarlo | **`A FAVOR`**: **la letra prohibe FUNDIR un acto con dueno, no leerlo**, y la lectura produjo dos razones mas | **[[A68_D16]]** |

### d) **EL SUPERVIVIENTE DEL `ACTO 18`, ADJUDICADO POR EL AUDITOR: `alianzas_cross_industry`, CON LAS CINCO PIEZAS QUE EL PLAN TIENE QUE CONSERVAR O SELLAR**

**Es la mitad que le faltaba al carril del `EMPATE SIN VARA`** (registrado en la linea
**[[PAG_TRANSITO]]** de esta pagina, y estrenado sobre este acto en la **[[PAG_ACTO18_TRANSITO]]**):
**el ejecutor escribe el caso y NO elige; el auditor adjudica en su acta con el caso delante; y el
lote siguiente ejecuta esa fusion como su primera operacion.** **El acta lo cerro**, y la
adjudicacion abre en la linea **[[A68_SUP18]]**.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **el superviviente** | **`alianzas_cross_industry`** | **[[A68_SUP18_ES]]** |
| **PRIMERA, el alcance** | **es el unico de los cuatro que apunta al MERCADO ENTERO** (el poder de compra colectivo para mover el mercado hacia otro tipo de producto); **los otros tres caben dentro de ese marco y el marco no cabe en ninguno de los tres** | **[[A68_SUP18_PRIMERA]]** |
| **SEGUNDA, el reparto con menos perdida** | **sus piezas ya alojan lo propio de los otros con la costura mas corta**: su condicion 1 **ES** el test del poder de mercado dicho como condicion, su paso 2 aloja la convocatoria por asociaciones, y su paso 3 son los estandares comunes | **[[A68_SUP18_SEGUNDA]]** |
| **TERCERA, lo buscable** | **trae los nombres propios** (`EICC`, `AIM-PROGRESS`) **que la razon del puesto 1903 senala como lo que vuelve buscable el paso** | **[[A68_SUP18_TERCERA]]** |
| **CUARTA, el cableado no lo desmiente** | **empata en cabeza** (3 con `co_opetition_industria`), **y entre esos dos deciden el alcance y el reparto** | **[[A68_SUP18_CUARTA]]** |

> **LAS CINCO PIEZAS QUE EL PLAN DEL LOTE E TIENE QUE CONSERVAR O SELLAR, nombradas para que no se
> pierdan en el reparto** (linea **[[A68_SUP18_CONSERVAR]]**): **1)** publicar y monitorear el
> cumplimiento colectivo (`co_opetition_industria`, paso 4); **2)** aplicar el estandar conjunto a
> los proveedores compartidos (`trabajo_colectivo_estandares_industria`, paso 4); **3)** el test del
> poder de mercado como **arranque explicito** (`colaboracion_sectorial`, paso 1); **4)** el encuadre
> por **riesgo reputacional compartido** (`trabajo_colectivo_estandares_industria`, condicion 1); y
> **5)** el marco nombrado **Responsible Care** (`trabajo_colectivo_estandares_industria`, paso 3).
> **El reparto pieza a pieza es del ejecutor bajo el contrato `CAMPO PROPIO`**, con simulacion previa
> y todas las guardas.

**LAS TRES RAZONES QUE SOSTIENEN LA FAMILIA, y son las que el ejecutor leyo enteras antes de que el
auditor adjudicara:** el puesto **1797** (la misma alianza entre competidores dos veces), el
**1871** (la familia pasa de DOS a TRES por cierre transitivo) y el **1903** (de TRES a CUATRO).
**La ciega del auditor sobre este acto dio 1 de 1 en el fondo**, con los cuatro textos leidos
enteros antes de destapar las razones (linea **[[A68_CIEGA]]**).

### e) **LA PREGUNTA 5, ADJUDICADA: UN ESTADO DE INVENTARIO *EN MESA* CON `operaciones` VACIO NO ES DUENO, Y LA FRONTERA QUEDA ESCRITA**

**Adjudicado POR EXTENSION CITABLE** (linea **[[A68_P5]]**), **y no es doctrina nueva**: es **el
criterio con el que `OP-U-02` abrio su universo**, mas el precedente del `acto 11` (misma nomina,
mismo estado) y el carril del `acto 17` con el puesto 460.

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **el criterio** | **el dueno a efectos del universo de `OP-U-02` es EL MEDIDO: los dos campos `duenos_*` del tramo fijado y el campo `operaciones` de la entrada del inventario** | **[[A68_P5_CRITERIO]]** |
| **LA FRONTERA, y se escribe para que no oscile** | **si la entrada del inventario nombra una operacion en su campo `operaciones`, o el tramo trae dueno en cualquiera de los dos campos, ESO es dueno y el acto NO se funde** | **[[A68_P5_FRONTERA]]** |

> **LA FUSION DEL `ACTO 22` NO SE DESHACE** (linea **[[A68_D2]]**), y su registro sigue donde estaba,
> en la linea **[[PAG_ACTO22]]** de esta pagina.

### f) **LA PREGUNTA 6, ADJUDICADA: LA FUSION DEL TRANSITO ABRE EL LOTE `E` CON PLAN PROPIO Y CUENTA EN SU DECLARACION**

**Adjudicado POR EXTENSION** (linea **[[A68_P6]]**), **extension del carril del transito y del patron
de un plan por lote**, que es como esta pagina viene sellando los lotes desde el `A` (linea
**[[PAG_LOTE_D]]** para el ultimo de ellos).

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **con que plan** | **dentro del PLAN PROPIO del lote `E`, sellado por `generar_plan_del_lote.py` como cualquier otro**; **el plan del lote `D` NO se reabre** | **[[A68_P6_PLAN]]** |
| **en que puesto del lote, y si cuenta** | **como PRIMERA operacion del lote `E`**, y **el `acto 18` CUENTA en la declaracion del lote como uno de los que cierran ENTEROS** | **[[A68_P6_PLAN]]** |

### g) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy.**

| | lo que el acta 68 deja escrito | destino | linea |
|---|---|---|---:|
| **el subconjunto cerrado de un acto con puente** | sigue **NOMBRADO**, ahora con **TRECE actos declarados esperandolo** (1, 5, 10, 11, 12, 13, 14, 15, 17, 20, 21, 23 y 24), **contados por el auditor** | **el cierre de la fase 03**, donde la parada de `AUDITOR.md` espera al fundador | **[[A68_PEND4]]** |
| **la marca para *ya lo dice el `APPEND` de un hermano*** | sigue **NOMBRADO**; **el carril vigente alcanza** y la vuelta 68 lo pago **DOS veces** con atenuante declarado | **la cuenta crece y se publica en cada lote** | **[[A68_PEND5]]** |
| **el `INCISO` de condiciones** | sigue en su carril, con **CUATRO piezas `DE CONDICIONES` mas** (filas 5, 6, 10 y 11) | **la fase 04** (acta 55, pregunta 5) | **[[A68_PEND6]]** |
| **el esquema de `OPERACIONES.jsonl`** | sigue **pendiente**; la vuelta 68 **no toco ninguna ficha y no estreno ninguna clave** | **sin fecha, y se dice** | **[[A68_PEND7]]** |
| **el cierre de la fase 03** | **NO SE CUMPLE TODAVIA**: quedan **27 actos y 85 nodos**, la mesa `OP-M-03`, y los trece declarados | **la parada escrita de `AUDITOR.md`, tal como esta** | **[[A68_CIERRE03]]** |

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO` SIGUEN SIENDO CUATRO Y LA LISTA SIGUE SIN
SER CERRADA:** el triangulo de `P.10` (linea **[[PAG_ACTO1_P10]]**), la guarda `1B` (linea
**[[PAG_GUARDA_1B]]**), la respuesta *DOS FAMILIAS* de `P.5` (linea **[[PAG_P5_MOTIVO]]**) y el
veredicto `D` directo interno (linea **[[PAG_CUARTO_MOTIVO]]**). **La linea base del censo de
colisiones sigue en `4`** (linea **[[PAG_LINEA_BASE]]**) y **el carril de las dos de la mesa sigue
donde estaba** (linea **[[PAG_CARRIL_COLISIONES]]**).

### h) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba**, **NO funde ni deshace nada**, **NO elige ningun
superviviente** (el del `acto 18` lo eligio el auditor y aqui solo se transcribe), **NO re-lee ni un
veredicto de las cuatro colisiones vigentes**, **NO toca la mesa `OP-M-03`**, **NO toca ninguna ficha
de `OP-U-02` ni de `OPERACIONES.jsonl`** y **NO abre el lote `E`**: **registra adjudicaciones**. El
lote `E` es la TAREA 2 de esta misma vuelta y se registra en su propia seccion, debajo de esta.
"""
