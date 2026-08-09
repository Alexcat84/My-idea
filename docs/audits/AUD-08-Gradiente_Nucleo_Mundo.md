# AUD-08 · La campaña del gradiente núcleo-mundo

**Estado: ABIERTO. 40 de 346 pares leídos (11,6%).** Esta auditoría documenta el
proceso completo desde la primera pasada: la doctrina, el instrumento, seis lotes
de lectura, dos cirugías ejecutadas y la deuda de validador que la ejecución
destapó. **Se escribe desde los documentos versionados y los hashes, no de
memoria**: cada afirmación lleva su commit o su documento fuente.

Documentos vivos de la campaña:

| documento | qué es |
|---|---|
| `docs/GRADIENTE_NUCLEO_MUNDO.md` | la vara y su doctrina |
| `docs/GRADIENTE_PARES.jsonl` | la cola de 346 pares, salida del instrumento |
| `docs/GRADIENTE_PARES_RESUMEN.md` | los umbrales, la distribución medida y la calibración |
| `docs/GRADIENTE_VEREDICTOS.md` | los veredictos, lote a lote, y el marcador |
| `docs/CIFRAS_EN_PALABRAS_CASOS_GRISES.md` | el acta del paro de la baranda |

---

## 1. EL ORIGEN

### El requisito del fundador

Escrito textual en la cabecera de `docs/GRADIENTE_NUCLEO_MUNDO.md`:

> Leída textual en los nodos, la información del núcleo debe ser verdaderamente
> superficial frente a la del mundo específico, **contrastada uno a uno**. El
> núcleo **jamás** más profundo y concreto que el mundo aplicable, y la
> diferencia debe **crecer**, no empatarse.

No es una métrica de conteo ni un muestreo de calidad: es un contraste **par por
par**, leído.

### El compromiso de rigor

Dispuesto por el fundador al abrir la campaña y respetado en los seis lotes:

1. **Los 346 pares de la cola se leen TODOS. Sin muestreo.** Ningún veredicto se
   extrapola de un vecino.
2. **Cuando la cola de señal alta se agote, se baja el umbral y se barre la
   franja siguiente.** El instrumento acepta `--umbral-semantico` justamente para
   eso, y su resumen ya deja escrito que bajar a 0,70 o 0,65 la ensancha.

**Lo segundo importa tanto como lo primero**: la cola actual está calibrada muy
por encima del percentil 99,9 de la distribución real (ver sección 3), así que
**cerrar los 346 no cierra el barrido, cierra la primera franja.**

---

## 2. LA DOCTRINA

### `6e315d2` (8 ago 2026), las cinco cláusulas

`docs/GRADIENTE_NUCLEO_MUNDO.md`. Cero código, cero catálogo.

| | cláusula |
|---|---|
| **(a)** | **El núcleo es SUFICIENTE.** Entrega la base completa de cada tema que toca. *"Ya está la base"* tiene que ser verdad: quien se quede solo con el núcleo tiene algo entero, no un teaser. |
| **(b)** | **El mundo es EXPONENCIAL respecto de esa base.** Pasos más específicos, entregable más avanzado, supuestos que **ya asumen la base hecha**. |
| **(c)** | **PROHIBIDO el arreglo por empobrecimiento.** Una violación jamás se corrige recortando el núcleo hasta dejarlo mudo. Se profundiza el nodo del mundo, o se reencuadra el del núcleo hacia su versión de base. **El núcleo es la puerta de entrada gratuita y no se degrada.** |
| **(d)** | **La profundidad se adjudica por LECTURA TEXTUAL** de `pasos_accionables` y `entregable_esperado`. **Jamás por conteos ni por largos**: los conteos solo ordenan la cola. |
| **(e)** | **Vigencia**: deuda a medir sobre los nueve mundos existentes, y **REGLA DE NACIMIENTO** para todo mundo futuro, empezando por el 11. |

### La regla 9 del SOP, en el mismo commit

La vara no se quedó solo en su doctrina: entró **donde se mina**, en las reglas de
extracción de `docs/SOP_EXTRACCION_PACKS.md`. Todo concepto se coteja **ANTES**
contra el núcleo; si hay base, el nodo del mundo **(i)** la declara en
`nodos_previos` cuando el puente aplique según la ley del ancla, **(ii)** la asume
hecha en vez de repetirla y **(iii)** profundiza.

> Un nodo de mundo que repite la base del núcleo al mismo nivel es un **RECHAZO DE
> EXTRACCIÓN**, no un caso de fusión posterior.

### `4081842` (9 ago 2026), lo que faltaba para sostener los veredictos

**Las tres vías de profundizar, por orden de costo:**

1. **REENCUADRE.** La profundidad **ya existe** en la escalera del propio mundo y
   el peldaño de entrada repitió la base. Se reescribe para que sus pasos
   **empiecen donde los del núcleo terminan**. Cero fuentes nuevas, cero nodos
   nuevos.
2. **RE-MINADO.** La extracción se quedó en la superficie del capítulo. Se vuelve
   al texto real de la sección fuente (regla 8 del SOP). **Cuesta lectura, no
   bibliografía.**
3. **LITERATURA NUEVA.** Solo con la fuente genuinamente exprimida, y pasa por
   adjudicación de bibliografía con visto del fundador. **Es la excepción.**

**El techo de la profundidad, tres paredes:** **la fuente** (jamás se inventa lo
que el libro no da), **la válvula** (los pasos siguen siendo hacibles esta semana
por el lector del taller) y **la voz** (profundo no es técnico ni corporativo: se
pide más precisión, no más empresa).

> **EXPONENCIAL significa relativo a la base del núcleo, no enciclopédico.**

**La prohibición complementaria: tampoco se DESPLAZA.** Mover nodos base del
núcleo hacia los mundos queda prohibido igual que empobrecerlos: deja el plan
gratuito cojo y **serrucha puntos de anclaje de la ley del ancla**, cuyos puentes
anclan siempre en el núcleo.

> **El defecto de una violación no es que existan dos nodos: es que el de pago
> quedó a la altura del gratis.**

**Una precisión verificada contra el grafo antes de escribirla**, registrada en el
propio documento: la evidencia de que la vía 1 alcanza decía *"dos peldaños
después"*. `la_matriz_de_colores_te_engana` es **sucesor DIRECTO** de
`cuan_probable_y_cuanto_doleria`, que lo declara en sus `nodos_previos`. **Es un
peldaño, no dos.** El argumento se refuerza: la profundidad estaba a un solo paso.

---

## 3. EL INSTRUMENTO

`scripts/gradiente_pares.py`, commit **`f4ee778`** (8 ago 2026). **Estrictamente
de solo lectura**: no toca ni un nodo, ni el motor, ni la web. Lo único que
escribe son sus dos salidas en `docs/`.

### Las dos señales, independientes, y basta con que dispare cualquiera

| señal | método | umbral |
|---|---|---:|
| **título** | `token_sort_ratio` de rapidfuzz | **80** |
| **semántica** | coseno sobre `web/lib/assets/semantic_index.json` | **0,75** |

**Se reportan LAS DOS por par, siempre**, aunque solo una haya disparado: el
auditor necesita ver por cuál entró cada uno. Los veinte primeros del resumen se
ordenan por la señal **más fuerte** de las dos, normalizando el título a 0-1, y
por eso hay filas con semántica baja y título alto.

### La distribución medida, que es lo que permite calibrar

Sobre **3.079.054** comparaciones mundo contra núcleo:

| percentil | coseno |
|---|---:|
| p50 | 0,3965 |
| p90 | 0,5083 |
| p99 | 0,6070 |
| p99.9 | 0,6859 |
| máximo | 0,8936 |

Media 0,3991. **Por encima del umbral 0,75: 342 comparaciones.**

> **El umbral 0,75 está muy por encima del p99.9.** La señal semántica caza solo
> la cola extrema, **deliberadamente**: la cola es para LEER, y una cola de miles
> de pares no se lee.

### La cola resultante

**346 pares**, sobre **1.618** nodos de núcleo y **1.903** de mundo.

| mundo | pares | | mundo | pares |
|---|---:|---|---|---:|
| quality | 174 | | exportacion | 17 |
| risk_management | 44 | | entrega | 9 |
| franquicias | 37 | | health_safety | 6 |
| compras | 36 | | seguridad_digital | 3 |
| environmental | 20 | | | |

### La calibración conocida, con salida 1

`PAR_DE_CALIBRACION = ("plan_gestion_calidad", "sistema_gestion_calidad")`. Si el
instrumento **no** caza ese par, escribe *"NO CAZADO. EL INSTRUMENTO ESTÁ MAL
CALIBRADO"* en su propio resumen y **devuelve código 1**
(`gradiente_pares.py:210`). No es un aviso decorativo: **el instrumento se declara
inservible antes de que alguien use su salida.**

Cazado en la corrida vigente: título **83,6**, semántica **0,7797**, disparo por
las dos.

### La declaración que gobierna todo lo demás

> **ESTE INSTRUMENTO EMPAREJA, NO JUZGA.** Un par en la cola es **una cita para
> leer**, no una violación.

Y coherente con la cláusula (d): **los conteos de pasos están en la salida y NO en
el criterio.** Solo ordenan la cola.

---

## 4. LA LECTURA

`docs/GRADIENTE_VEREDICTOS.md`. Adjudica el auditor, da el visto el fundador.
**Ningún veredicto ejecuta corrección.**

| lote | pares | commit |
|---|---|---|
| 1 | 1 a 3 | `79acb9e` (8 ago) |
| 2 | 4 a 8 | `2eb355e` |
| 3 | 9 a 13 | `56b6f5b` |
| 4 | 14 a 20, con cierre del top-20 | `c066dc4` |
| 5 | 21 a 27 | `eddee4b` |
| 6 | 28 a 40 | este commit |

Los veredictos de los pares 1, 4, 5, 8, 17 y 19 llevan además la marca de
ejecución que les pusieron las dos cirugías (`08988ad` y `1260581`).

### Marcador tras 40 de 346

| ficha | estado |
|---|---|
| VIOLACIONES clásicas | **6** (5 de `risk_management`, 1 de `quality`); **las 5 de risk curadas en la cirugía 1** |
| VIOLACIONES INVERTIDAS | **2 cargos sobre UN solo nodo del núcleo**: `gestion_inventario`, contra `compras` (par 23) y contra `quality` (par 37) |
| FRONTERAS con choque de fuentes | **2**: objeciones (par 6) y plazos de negociación (par 38) |
| SUB-FUSIÓN | **4 temas del núcleo** más **1 de `quality`** |
| DUDOSOS de ensanche | 2, uno de ellos resuelto por la cirugía 1b |

### Las clases, y dónde nació cada una

**Cuatro se declararon antes de leer** (cabecera del documento de veredictos):
`VIOLACION`, `DUDOSO`, `FALSO PAR` y `GRADIENTE OK`. **Las demás nacieron
leyendo**, que es el hallazgo de proceso más importante de la campaña:

| clase | nació en | qué nombra |
|---|---|---|
| **FRONTERA CON CHOQUE DE FUENTES** | lote 2, par 6 | dos nodos con **doctrina opuesta** integrada, ninguno sabe que el otro existe. No es defecto de gradiente |
| **FUGA DE SECCIÓN** | lote 3, par 12 | el par cumple, pero la profundidad del tema **está en el peldaño de al lado**, no en el nodo titular |
| **SUB-FUSIÓN DEL NÚCLEO** | lote 3, pares 9 y 10 | el núcleo tiene **dos o tres nodos del mismo tema**, iluminado de rebote por el gradiente |
| **GRADIENTE OK POR ESPECIALIZACIÓN** | lote 5, par 21 | el mundo **no es más profundo en la mecánica**: añade lo que su dominio exige y el núcleo no puede dar |
| **VIOLACIÓN INVERTIDA: EL NÚCLEO SE PASÓ** | lote 5, par 23 | el nodo del mundo es correcto; **el del núcleo tiene profundidad de curso**, en voz de manual, dentro del plan gratuito |
| **FALSO PAR FUNCIONAL** | lote 5, par 26 | no son homónimos: son **momentos distintos de la misma secuencia** (cuándo contra cómo) |
| **SUB-FUSIÓN DEL LADO MUNDO** | lote 6, par 31 | el mismo método escrito **dos veces dentro del mismo mundo** |

> **La cola de gradiente resultó ser también un detector de deuda del núcleo.**
> Ninguna de esas siete clases estaba prevista al diseñar el instrumento.

### La tendencia, confirmada en el lote 6

> **Bajando la señal, la cola encuentra cada vez menos gradiente roto y cada vez
> más deuda estructural del núcleo y costuras de fusión.**

Los lotes 5 y 6 **no trajeron ninguna violación clásica**: trajeron dos cargos
invertidos, una frontera nueva, una sub-fusión de mundo y confirmaciones de las
sub-fusiones del núcleo.

---

## 5. LAS CIRUGÍAS

### Cirugía 1, `08988ad` (9 ago 2026): los cinco peldaños de `risk_management`

**Primera ejecución del arreglo por vía 1.** Cero contenido inventado, cero nodos
nuevos, cero deprecados, **cero aristas tocadas**. Solo texto.

| nodo | con qué se queda ahora |
|---|---|
| `cuan_probable_y_cuanto_doleria` | la calibración honesta: el daño en dinero o tiempo y el rango declarado, en vez de una etiqueta |
| `haz_tu_lista_de_lo_que_puede_fallar` | la sesión de censo: nombrar sin filtro, y el criterio de qué entra al registro |
| `manten_viva_tu_lista_de_riesgos` | el ritual de vida: un riesgo se cierra cuando ya no puede afectarte, no cuando te cansas de mirarlo |
| `evalua_la_gravedad_sin_autoengano` | el autoengaño de inflar lo ya decidido evitar y minimizar lo que no se quiere enfrentar |
| `revisa_tus_riesgos_con_un_ritmo` | la cadencia proporcional a la gravedad, subiendo en etapas intensas |

**Los cinco subieron por encima de su base sin inventar nada. Ninguno activó la
condición de paro.**

**Cierre verificado**: Gate 0 completo OK antes y después del reindex (0 activos
sin vector), reindex completo de Voyage y sync, **rumbos 42/1/0 sin deriva y
trinquete íntegro**. Las cinco anclas de la vara congelada: tres inmóviles y dos
que suben un puesto. **Ruido**, como se esperaba de seis nodos reescritos en un
mundo que no compite por esas consultas.

### Cirugía 1b, `1260581` (9 ago 2026): el par 8, con la arista adjudicada

La cirugía 1 **paró** en su parte 2 al descubrir que **no existía arista** entre
los dos nodos, y lo reportó sin crearla. La adjudicación desbloqueó el paro con un
razonamiento de ley: **los dos nodos son del MISMO mundo**, y la ley del ancla
prohíbe el acoplamiento **mundo a mundo**, no las aristas internas.

Arista bidireccional creada espejando el formato del resto del archivo (ids, no
títulos, comprobado antes de escribir); **Gate 0 la validó con la alcanzabilidad
dirigida al 100%**. `cradle_to_cradle_concepto` pasa a ser **la puerta del tema**;
`desperdicio_es_alimento` no se tocó. Rumbos 42/1/0 sin deriva.

**Una decisión tomada y reportada**: el resumen orienta hacia la profundización
**sin nombrar el nodo destino**. La arista recién creada ya es el mecanismo de
navegación, y un título cableado en prosa sería **una segunda fuente de verdad que
envejece** si el nodo se renombra.

### La palanca reservada, con dos casos legítimos y **cero ejecuciones**

La cláusula (c) permite **reencuadrar el nodo del NÚCLEO hacia su versión de
base** como arreglo alternativo. En la cirugía 1 quedó **reservada**: no se usó.

Los pares **23** y **37** son su **primer y segundo caso legítimo**, y ambos caen
sobre el mismo nodo, `nucleo/gestion_inventario`, con nueve pasos que incluyen
inventario cíclico óptimo, costos de ordenar contra mantener, estacionalidad y
puntos de reorden.

> **No es base: es un curso de operaciones en el plan gratuito.**

**PENDIENTE DEL VISTO DEL FUNDADOR. No se ejecuta desde ningún documento.**

---

## 6. LO QUE LA EJECUCIÓN ENSEÑÓ

La cirugía 1 no solo arregló cinco nodos: **destapó dos defectos que ninguna
lectura habría encontrado**, porque solo aparecen cuando se escribe.

### a) `RE_CIFRA` era ciega a las cifras en palabras

Un peldaño reencuadrado volvió con *"no es lo mismo un veinte por ciento que un
cuarenta y cinco"*: **un ejemplo inventado**. `RE_CIFRA` era `\d+(?:[.,]\d+)?`,
**solo dígitos**, y no lo vio. Se quitó a mano y quedó como deuda del validador.

**El paro, `a42fcfd`.** Al construir la extensión, el encargo obligaba a parar si
la frontera resultaba más fina de lo que los ejemplos sugerían. **Lo era, y no por
poco.** No se partió de ejemplos de laboratorio: se buscó cada palabra candidata
en los 3.521 nodos activos, y **casi todas viven en el catálogo con dos sentidos y
uno de ellos no es una cifra** (*"cajas de doble pared"*, *"número par de
miembros"*, *"resolver de una vez"*, *"la primera mitad de la llamada"*).

**El radio de explosión, medido antes de decidir:**

| patrón ingenuo | nodos que caza | del catálogo |
|---|---:|---:|
| numerales sueltos (uno, dos, tres...) | **2.488** | **70,7%** |
| ordinales | 440 | 12,5% |
| **porcentaje escrito (X por ciento)** | **8** | **0,2%** |

> **Un detector de numerales sueltos marcaría siete de cada diez nodos. Eso no es
> una baranda: es ruido que se acaba desactivando.**

**La adjudicación de las cuatro preguntas** quedó en
`docs/CIFRAS_EN_PALABRAS_CASOS_GRISES.md`: alcance **estrecho** (el compuesto
exacto `<numeral> por ciento` más decenas, centenas y mil como palabra); **sí** a
la regla de contexto, porque **falla hacia el falso negativo**, que la lectura ve,
mientras un falso positivo bloquea nodos buenos en silencio; **rechaza**, con la
semántica de diff intacta; y **sin lista de exenciones**, porque `MIL-STD` cae
solo por la regla de tokenización.

**La construcción, `7db1810`.** La baranda salió a **un solo sitio**,
`scripts/cifras.py`: estaba **duplicada** en `revoz_pack.py` y `consolidar_pack.py`
y ampliarla habría dejado la misma regla escrita dos veces. Los dos scripts la
importan y **ninguno guarda copia**, con un test que lo custodia.

**La pasada en seco**: los 3.521 nodos activos comparados **consigo mismos**,
**cero disparos**. `engine/test_cifras.py` custodia las seis cosas, con 13 casos de
NO-DEBE-CAZAR **sacados del catálogo real y no de laboratorio**.

**Válvula de degradación, fijada por adelantado y no discutible en caliente**: si
en operación se adjudican **dos falsos positivos** de esta extensión, **se degrada
a aviso** y vuelve a adjudicación.

### b) La precedencia del SYSTEM de la re-voz

El peldaño 4 de la cirugía 1 **volvió idéntico a como entró**. El prompt del
sistema dice *"los HECHOS: ni uno nuevo, ni uno menos"* y la orden del editor
pedía **quitar** dos pasos. **El SYSTEM ganó**, que es lo correcto: es una defensa
que no se debilita.

Hubo que autorizar el borrado expresamente con la fórmula **"quitar no es
inventar"** para que aplicara. **Todo reencuadre que quita necesitará esa
autorización.**

La cláusula quedó **junto a la herramienta** (`scripts/revoz_pack.py`) y no en el
SOP, con este motivo escrito: **quien la va a necesitar no está minando un pack,
está escribiendo un `--instruccion`**, y ahí es donde tiene que tropezarse con
ella. Va en dos sitios del mismo archivo: la nota larga con el porqué encima del
argumento, y un recordatorio en el propio `--help`.

### c) La rectificación del deprecado (`06df920`): el sistema de paro funcionó

**El ejecutor reportó un hallazgo falso**: que
`quality/auditoria_sistema_control_calidad_2` no registraba a su hermano
deprecado como sucesor. Sobre ese reporte se adjudicó una cirugía de historia. **Al
ir a ejecutarla, la verificación previa la desmintió y nada se tocó.**

**La sucesión estaba completa desde el día de la fusión**: `ids_alias` con el id
muerto y `merged_originals` con su id, su título y su fuente.

**Tres clases de error quedaron con nombre:**

**(a) Una consulta fallida contada como dato.** Se buscó el mapa de alias como
**clave de nivel superior** de `master_graph.json`. No vive ahí: vive en el campo
`ids_alias` **de cada nodo**, que es exactamente como lo lee `mapaDeAlias` en
`web/lib/engine/graph.ts`. La consulta **no encontró el mapa**, y esa nada se
reportó **como una ausencia medida**.

> **Una consulta que no encuentra nada no es lo mismo que un catálogo que no tiene
> nada, y la diferencia no se ve en la salida.**

**(b) El `null` de un campo inexistente leído como valor vacío.**
`deprecado_por` y `motivo_deprecacion` **no existen en el esquema**, en ninguno de
los 3.835 nodos: la sucesión vive **en el superviviente, nunca en el deprecado**.
Un `.get()` sobre un campo que no está devuelve lo mismo que sobre un campo vacío.

**(c) DEL AUDITOR: adjudicar sobre un hallazgo sin verificarlo por cuenta
propia.**

> **Los reportes convincentes son los que MÁS verificación merecen, no los que
> menos.** Un hallazgo bien redactado, con tabla y cifras, es exactamente el que
> pasa sin que nadie lo mire dos veces.

**La cadena funcionó porque tiene dos eslabones y el segundo re-verificó antes de
tocar.** El paro no lo produjo la duda: lo produjo **el hábito de medir otra vez
justo antes de escribir**.

### La relectura que quedó: las aristas hacia deprecados son DISEÑO

De rebote, la verificación midió lo que nadie había medido:

| | |
|---|---:|
| aristas de nodos **activos** hacia ids **deprecados** | **1.149** |
| nodos activos que las declaran | **824** (23% de los 3.521) |
| ids deprecados apuntados | **308** de 314 |

**No son residuo: son la historia viva**, y **la simetría las exige en ambos
extremos**. Quitarlas de un solo lado pone el Gate en rojo, y el paso 5 de
simetrización **las vuelve a poner**. El propio Gate lo tiene escrito: *"un
deprecado sigue EN el grafo, con sus aristas intactas"*.

---

## 7. EL TABLERO ABIERTO

### Lectura

- **306 pares por leer** (41 a 346), sin muestreo.
- **La franja bajo el umbral**, entera. El barrido a 0,70 o 0,65 no se ha corrido
  y no se ha dimensionado.

### Fichas abiertas, ninguna ejecutada

| ficha | contenido |
|---|---|
| **SUB-FUSIÓN** | **ABIERTA en `docs/FICHA_SUBFUSION_GRADIENTE.md`**, con los cinco casos por nombre: Goldratt, el trío de brainstorming, `criterios_seleccion_proveedores`, `gestion_inventario` (los cuatro del núcleo) y el método COC duplicado de `quality` (el del lado mundo). La cuenta sin nombre del marcador del lote 5 **queda fijada ahí**: el cuarto era `gestion_inventario` |
| **FRONTERAS CON CHOQUE** | objeciones (par 6) y plazos de negociación (par 38). Decidir **quién se queda con qué**, y **si el contexto se escribe en los nodos** |
| **INVENTARIO DE ESCALA** | `docs/INVENTARIO_ESCALA.md` es parcial a propósito (1.573 de 3.521 clasificados). **Sus dos usos declarados siguen sin construir**: material para que el intérprete converse sabiendo qué nodos son de operación corporativa, e insumo del **mapa tema-a-mundo** de la invitación al final del plan |

### Límite conocido del instrumento, anotado sin construir nada

**El instrumento solo empareja mundo contra núcleo.** Los solapes **MUNDO CONTRA
MUNDO son invisibles para él, por diseño.**

El **lote 7, puesto 51**, lo dejó a la vista: `quality` contiene **una
minisección de riesgos** (`identificacion_de_riesgos`,
`evaluacion_gestion_riesgos`, `plan_de_gestion_de_riesgos`) **paralela al mundo
`risk_management` entero**.

> **Cuando la cola de 346 se agote, la franja siguiente no es solo bajar el
> umbral semántico: es también la pregunta mundo contra mundo.**

### DECISIÓN DEL FUNDADOR: el barrido intra-dominio se hace

**El barrido INTRA-DOMINIO** (el núcleo contra sí mismo, y cada mundo contra sí
mismo) **SE HACE, y cierra el 100%.**

**Converge con las otras dos preguntas abiertas**, y esa es la razón de la
decisión: no son tres trabajos, son **tres caras del mismo instrumento**.

| pregunta | dónde nació |
|---|---|
| **mundo contra mundo** | lote 7, puesto 51: la minisección de riesgos de `quality` |
| **la clase de huérfanos por NOMBRE LIBRE** | ficha de sub-fusión: declarada **NO MEDIDA** |
| **el intra-dominio** | esta decisión |

**Las tres se responden con lo mismo**: **pares por semántica dentro y entre
dominios, sin pasar por el núcleo.** Es `scripts/gradiente_pares.py` **con otro
emparejamiento**: las **mismas dos señales**, los mismos umbrales calibrables, y
**la misma doctrina de que empareja pero no juzga.**

### ORDEN FIJADO, para no duplicar lecturas

| | qué |
|---|---|
| **1.º** | **agotar la cola de 346** |
| **2.º** | **la franja bajo el umbral** |
| **3.º** | **el intra-dominio, AL FINAL**, con su cola propia |

> **El intra-dominio va último por una razón económica, no por prioridad:
> muchos de sus pares caerán solos cuando las fusiones de
> `docs/FICHA_SUBFUSION_GRADIENTE.md` se ejecuten.** Leerlos antes sería leer dos
> veces lo mismo, y la segunda vez con el catálogo ya cambiado debajo.

**El instrumento no se extiende hasta llegar al tercer punto.**

### Decisiones que esperan al fundador

1. **La palanca reservada sobre `nucleo/gestion_inventario`** (pares 23 y 37):
   reencuadrarlo a versión de base. **Dos cargos, ninguna ejecución.**
2. **El par 2**, dudoso de ensanche, que sigue sin adjudicar.
3. **Cuándo se baja el umbral** y con qué valor.

---

## 8. LA REGLA DE TRÁNSITO para el trabajo en paralelo

**Nueva, fijada por el auditor con el fundador en el cierre de este lote.** Vale
para toda sesión de CC, no solo para esta campaña.

> **CC puede tener sesiones en paralelo SOLO para trabajo que no toca el
> catálogo**: documentación, instrumentos, lectura.
>
> **Lo que toca nodos o índice va SIEMPRE en secuencia. Un solo escritor.**

**Por qué la regla es esta y no un candado técnico**: en esta campaña, una sola
cirugía de cinco nodos arrastró reindex completo de Voyage, `sync_assets_web.py`,
`master_graph.json`, `semantic_index.json`, el manifest y la corrida del trinquete
de rumbos. **Dos escritores concurrentes sobre esa cadena no producen un conflicto
de merge legible: producen un índice que no corresponde al grafo**, que es
exactamente la avería silenciosa que esta casa persigue.

La lectura y la documentación no tienen esa cadena: escriben en `docs/` y no
mueven el catálogo.
