# REPORTE DE LA VUELTA 40, 19 ago 2026. Ejecutor: Opus 5. Rama `pasada-unica`

**LO QUE ESTA VUELTA HIZO EN UNA LINEA: LA PUERTA DE CALIBRACION DEL INSTRUMENTO DE COSTURAS
REPARADA SIN TOCAR UN UMBRAL NI UN NODO, y `OP-D-05` EJECUTADA ENTERA Y CERRADA CON ESE
INSTRUMENTO YA VIVO.** Dos nodos absorbidos, cero borrados, todo verde, `OP-D-06` abierta y medida,
**y un hallazgo incomodo que va antes que los buenos: la fusion de `OP-D-05` ENCENDIO la senal del
instrumento sobre su propio resultante, y quien declara que ahi no hay costura soy yo, que hice la
fusion.**

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1), Y CON SU LIMITE DICHO

**Corrida:** `python scripts/loop/vuelta31_estado.py`, salida entera en
`docs/loop/SALIDA_V40_APERTURA.txt`, **commiteada sola en `002edf43`.**

| | apertura (antes de la primera operacion de `OP-D-05`) |
|---|---:|
| marcador | `n 3.388`, A **575**, B **83**, C **8**, D **2.722**, tasa **17,0** |
| grafo | **3.853** ficheros, ~~3.538~~ **3.534** vivos, **319** deprecados, **16.869** enlaces (la cifra tachada es una caida mia, corregida en la seccion 6 y no borrada) |
| operaciones | **71**, todas `LISTA`, **0** dependencias rotas |
| inventario | **672** entradas |

**EL LIMITE, y se dice en vez de taparlo:** esta medicion se corrio **DESPUES** de la tarea 1 y de
la reparacion de la puerta, o sea que **no es la primera medicion de la vuelta**. Se declara asi y
**se prueba que sirve igual de apertura**: es **`BYTE IGUAL`** al cierre de la vuelta 39,
`md5 9331c557163d522c98ebd8ba03dbdccf` **en los dos ficheros**, corrido hoy. Ni la tarea 1 (prosa en
`docs/plan/`) ni la reparacion (codigo en `scripts/`) tocaron nada de lo que esta medicion mide.
**La regla 1 pide medir antes de la primera operacion; lo que se hace aqui es medir despues y
PROBAR que nada se movio, que es mas trabajo y no menos.**

---

## 1. TAREA 1: EL ACTA DE LA VUELTA 39, ANOTADA BAJO EL CIERRE DE `OP-D-04`

Escrita en `docs/plan/02_DESTEJIDOS.md` como seccion nueva **debajo** del registro de cierre, **sin
tocar ni una linea de lo que corrige**. Cada adjudicacion va con **su linea del acta leida hoy**:

| discutible | adjudicacion | linea del acta |
|---|---|---:|
| `d1`, el re-anclaje del puente | **PROCEDE**, por `P.1`, la regla escrita del propio `Gate 0` y el precedente triple `a2902995`, `06dd2922`, `33265c05` | **8.252** |
| `d2`, los dos de siete pasos | **PROCEDEN LOS DOS** por la excepcion de clase de `OP-F-01`, con la senal de `reglas_brainstorming` **registrada como cita** y encargada a la cola de lectura | **8.267** y **8.275** |
| `d3`, la arista de `P.10` y su ciclo | **PROCEDE Y SE QUEDA**: **134 ciclos dirigidos de tres** medidos por el auditor entre nodos vivos | **8.278** y **8.283** |
| `d4`, restaurar y rehacer | **PROCEDE** | **8.290** |

**Y la verificacion entera del acta se cita con su linea: `CERO DISCREPANCIAS: todo lo cotejado
calza al digito`, linea 8.217.** Las dos lineas que el acta usa para `d2` se comprobaron por mi:
`01_FUENTES.md` linea **90** dice *tienen narracion repetida dentro*, y `02_DESTEJIDOS.md` linea
**294** es el precedente del nodo de siete. **Leidas hoy, no recordadas.**

---

## 2. PARTE A: LA PUERTA DE CALIBRACION, REPARADA

### 2.1 LA AVERIA, MEDIDA Y NO HEREDADA

`scripts/costuras_internas.py` se negaba entero desde la vuelta 34: **`exit 1`, cero entregas**,
porque su fixture `plan_mejora_procesos` daba **43,1 contra un umbral de 44**. Corrido por mi hoy
antes de tocar nada, reproduce tal cual.

**EL ROTO NO ERA EL INSTRUMENTO: ERA EL FIXTURE.** Medido por mi con `git log --follow`, el ultimo
commit que toco `dataset/nodos/plan_mejora_procesos.json` es **`2bd8dd76`** (*OP-F-04-HOR ejecutada
en casi todo: doce nodos en trece cortes*), y medido contra `OPERACIONES.jsonl`, **ese nodo esta en
la NOMINA de `OP-F-04-HOR`**. **La propia campana recorto su fixture por una operacion legitima, y
la puerta confundio *mi fixture quedo rancio* con *el instrumento esta roto*.**

### 2.2 LAS CINCO GUARDAS DEL ENCARGO, UNA A UNA

| guarda | como quedo |
|---|---|
| **1**, los umbrales no se tocan | **`UMBRAL_PAREJA = 80` y `UMBRAL_BLOQUE = 44` intactos**, comprobado con `git diff HEAD` filtrando esas lineas: **salida vacia** |
| **2**, ningun nodo se toca | **`git status` sobre `dataset/`, `packs/`, `web/` y `engine/`: vacio.** La reparacion vive entera en `scripts/` |
| **3**, fixture nuevo por criterio escrito y con su medicion al lado | **criterio de CINCO puntos escrito arriba de la lista**, y los tres fixtures con su medicion de hoy impresa. **El candidato del acta se VERIFICO con el instrumento y no se cito de aquella pagina** |
| **4**, la calibracion vieja conservada declarada | **`CALIBRACION_RETIRADA`**, con motivo, commit de origen y medicion. **El instrumento LA SIGUE MIDIENDO E IMPRIMIENDO en cada corrida** |
| **5**, la salida sellada con `exit 0` | **`docs/loop/SALIDA_V40_COSTURAS_REPARADO.txt`, exit 0** |

### 2.3 EL CRITERIO, Y LOS TRES FIXTURES CON SU MEDICION

**El criterio, escrito dentro del instrumento y medido antes de escribirse**
(`scripts/loop/vuelta40_calibrar_costuras.py`, salida en `docs/loop/SALIDA_V40_CALIBRACION.txt`):

1. **dispara HOY** con los umbrales vigentes;
2. **entra por la senal de BLOQUE**, que es la senal de la que nacio la clase;
3. **mas de uno, y al menos uno con margen amplio** (la averia de hoy es justo lo contrario);
4. **se prefiere el que NO este en la nomina de ninguna operacion** del plan, medido contra
   `OPERACIONES.jsonl`, porque es el que la campana no tiene previsto recortar;
5. **cuando un fixture queda rancio se RETIRA DECLARADO**, nunca se afloja el umbral.

| fixture | bloque | corte | margen | por que entra |
|---|---:|---:|---:|---|
| `fases_traccion_producto` | **72,6** | 4 | **mas 28,6** | **EL ANCLA**: el bloque mas alto del catalogo activo medido hoy, y **el unico de los tres que NO esta en la nomina de ninguna operacion** |
| `reglas_brainstorming` | **50,6** | 2 | **mas 6,6** | el candidato del acta, **verificado aqui**. Su operacion `OP-D-04` ya esta cerrada |
| `economia_circular_como_modelo_de_negocio` | **44,2** | 3 | **mas 0,2** | **el fundador superviviente** de los dos que dieron origen a la clase. **VA DECLARADO FRAGIL** |
| ~~`plan_mejora_procesos`~~ | ~~43,1~~ | 2 | menos 0,9 | **RETIRADO DECLARADO**, y el instrumento lo sigue midiendo e imprimiendo |

### 2.4 LO QUE SE ANADIO Y LO QUE NO SE ARREGLO

**SE ANADIO UN AVISO DE BORDE.** En su corrida normal el instrumento imprime el margen de cada
fixture y **avisa si alguno esta a menos de un punto del umbral**. Hoy avisa de
`economia_circular`. **La averia de la vuelta 34 se descubrio por un `exit 1` a destiempo; con el
aviso, la siguiente se ve venir.** Y el diagnostico de la puerta rota **ahora dice QUE HACER**:
retirar declarado, nunca aflojar el umbral.

**LO QUE NO SE ARREGLA, y no se disfraza:** **la cola sale en 1.496 nodos sobre 3.534 activos, el
42,3 por ciento**, con **1.494 entrando por la senal de bloque**. **Es exactamente el costo que la
vuelta 34 midio y publico** (1.497 sobre el grafo de aquel dia). El propio encabezado del
instrumento llama a eso **una baranda rota**. **Reparar la puerta no era arreglar la escala**, el
encargo prohibe tocar umbrales, y **el pendiente de doctrina del `MIN_BLOQUE = 2` sigue entero y
sigue siendo del fundador.**

### 2.5 EL CASO POSITIVO: LA PUERTA SE EMPUJO POR LOS DOS LADOS

`scripts/loop/vuelta40_guarda_puerta.py`, salida en `docs/loop/SALIDA_V40_GUARDA_PUERTA.txt`,
**exit 0 con todas las comprobaciones en verde**. **Una puerta que solo se ha visto ABRIR no esta
probada:**

| | |
|---|---|
| con los fixtures de hoy | **ABRE**, los tres disparan, y los criterios 2 y 3 se comprueban como asertos |
| con un fixture que no dispara | **CIERRA** con `CalibracionRota`, y **el empujon se da con el RETIRADO `plan_mejora_procesos`: la averia de verdad, REPRODUCIDA a proposito y no recordada** |
| el diagnostico | **dice que hacer y que no**, comprobado como asertos sobre su texto |
| la puerta heredada por importacion (guarda de la vuelta 34) | **NO SE AFLOJO**: las dos senales publicas revientan con la puerta cerrada |
| `NO APLICA` (guarda de la vuelta 34) | **sigue reventando** al comparar, al convertir a `float` y como booleano |

---

## 3. PARTE B: `OP-D-05`, DE PUNTA A PUNTA

### 3.1 EL DESTEJIDO: **NO HAY COSTURA QUE DESTEJER**, y son TRES medidas que coinciden

**(a) EL INSTRUMENTO YA VIVO, leido de su cola entregada** (`vuelta40_costuras_opd05.py`,
`SALIDA_V40_OPD05_COSTURAS.txt`): de los tres nodos **cita UNO**,
`errores_comunes_asignacion_roles` (**bloque 45,5**, corte tras el paso 2), y **no cita** a los
otros dos (43,6 y 40,6).

**(b) LA LECTURA TEXTUAL CON LA CITA DELANTE, y `P.11` para separar advertencia de procedimiento.**
Los cinco pasos de ese nodo son **cinco errores distintos**, no una narracion contada dos veces.
Aplicada la pregunta literal de `P.11` (*quitale las frases que empiezan por NO, por EVITA o por DE
VERDAD*): *confrontar EN LUGAR DE evitarlo*, *evaluar OBJETIVAMENTE si es REALMENTE la mejor
opcion*, *SER CAUTELOSOS*, *EVITAR colocar por lealtad*. **Lo que queda es una lista de punteros:
por la vara, ese nodo es LINEA y no procedimiento.** Comparten **tema**, no **narracion**, que es
justo lo que un comparador de tokens no distingue y **su propio encabezado declara**.

**(c) EL HALLAZGO QUE NO ESTABA EN EL ENCARGO, y es el que cierra el punto.** Al leer las tres
razones **enteras** del archivo aparecio que **el destejido de `OP-D-05` SI tenia sujeto escrito**,
no en la seccion de la operacion sino **en las razones de sus propios pares**: el puesto **673**
dice que `seleccion_ceo_fundador` es **costura CONFIRMADA** en `docs/FICHA_SUBFUSION_GRADIENTE.md`,
**doce pasos**, corte **1 a 4 contra 5 a 12**; y el **492** describe el mismo corte. **Y la tabla de
orden del plan le cuenta a `OP-D-05` UN destejido con ese nodo de ancla**, citada literal por el
instrumento.

**MEDIDO CONTRA EL NODO DE HOY** (`vuelta40_destejido_opd05.py`, `SALIDA_V40_OPD05_DESTEJIDO.txt`):

| | |
|---|---|
| pasos cuando se escribio la razon | **12** |
| pasos HOY | **4** |
| fuente en la razon | dos libros |
| fuente HOY | **una** |
| huellas del bloque 5 a 12 (mentor, brecha, CEO profesional, control, autoevaluacion, clausula) | **CERO de SEIS sobreviven** |
| quien se lo llevo | **`OP-F-04-HOR`, commit `2bd8dd76`**, medido con `git log --follow` |

> **Es el mismo commit que dejo rancio al fixture del instrumento de costuras. La misma operacion
> legitima causo las dos cosas, y las dos se cerraron en esta vuelta.** Y es **el mismo precedente
> que `OP-D-03`**, cuya celda dice que **dos de sus tres costuras estaban CONSUMIDAS por la fase
> 01**.

### 3.2 `P.5` CON TEXTO YA ESTABLE: **UNA familia**

`vuelta39_acto.py --op OP-D-05`, `SALIDA_V40_OPD05_ACTO.txt`, corrido hoy: **3 de 3 pares con
clase, los tres `A` y los tres del ARCHIVO** (puestos **492**, **673**, **833**), **cero lecturas
dirigidas**, **cero nodos puente**, **UN subconjunto cerrado que es el acto entero**, **cero
aristas cojas en los tres** y **los tres de la misma fuente** (*The Founder's Dilemmas*): **NO es
acto de fuente mixta.** **Como no hubo destejido, ningun par quedo rancio y no se releyo ninguno**,
que es exactamente la condicion que la nota de la operacion pone.

### 3.3 `P.8` EN ORDEN: **DECIDE EL CONTENIDO**, y el cableado solo acompana

**SUPERVIVIENTE: `seleccion_ceo_fundador`.** Especie de `9.3.1`: **POR ELEGIR** (de tres pares `A`,
**uno solo** nombra ganador).

1. **PADRE DECLARADO POR EL ARCHIVO**, que `P.8` cuenta como contenido con el mismo peso que el
   texto: la razon del **673** dice literal *El corto cabe entero dentro del primer bloque del
   largo*, y **el primer bloque del largo es hoy el nodo entero**, sus cuatro pasos. Es ademas
   **el unico par que nombra ganador**.
2. **EL EJE COMUN ES EL TITULO DEL SUPERVIVIENTE**: el **492** dice que los dos *mandan decidir con
   intencion quien es el CEO*, y el titulo del nodo es, literal, *Decidir con intencion quien sera
   el CEO fundador*. Los otros dos son sus caras: el **833** los llama *el mismo reparto de titulos
   contado en positivo y en negativo*.
3. **`P.11` SOBRE UN DONANTE**: `errores_comunes_asignacion_roles` es **LINEA y no procedimiento**.
   Un checklist de advertencias no es la cabeza de un procedimiento. **Y eso NO autoriza a
   borrarlas: las cinco viajan, y el plan dice en que grupo cae cada una.**
4. **PIEZA PROPIA QUE NADIE MAS TIENE**: el catalogo de roles alternativos (*presidente de la junta
   (Chairman)*, *CTO*, *Chief Scientific Officer*).

**EL CABLEADO, citado y NO usado para decidir: 9 contra 4 y 4.** Va **a favor** del elegido, y por
eso hay que decir que **no hizo falta**: si el contenido no hubiera hablado habria decidido solo, y
si hubiera ido en contra habria perdido igual, como en el acto II del racimo del pivote. **Y el
coste de la eleccion esta medido: CERO aristas**, porque los tres tienen cero aristas propias sin
reciproco.

### 3.4 EL PLAN SELLADO ANTES DE EJECUTAR, Y GENERADO EN VEZ DE TECLEADO

`docs/loop/PLAN_V40_OPD05.json`, construido por `scripts/loop/vuelta40_plan_opd05.py`. **Lo unico
tecleado son las agrupaciones y sus MOTIVOS, que es lo que no puede salir de un instrumento: la
lectura.** Todo lo demas se genera: los **21 origenes VERBATIM** salen del fichero, las
redirecciones y las duplicadas se **miden** con la misma aritmetica del ejecutor, los pasos finales
se **derivan** de los grupos, y la tabla de perdidas se **deriva** de la particion.

| | sellado |
|---|---|
| pasos del resultado | **6**, **DENTRO del estandar de 3 a 6**: **esta operacion no necesita la excepcion de clase** que `OP-D-04` si necesito |
| condiciones | **3** |
| redirecciones sobre vivos | **8** |
| deprecados que nombran | **0** |
| duplicadas que la fusion fabrica | **2** |
| simetrizacion esperada | **5 aristas**, ni una mas ni una menos |
| tabla de perdidas de `P.13` | **21 de 21 piezas VIAJAN, CERO se pierden** |

**LOS REGISTROS QUE NO SON EL GRAFO, ENUMERADOS ANTES Y NO DESPUES** (la leccion de la vuelta 39
convertida en instrumento, `vuelta40_registros_no_grafo.py`): barrido de **todo el repo salvo el
grafo, los nodos y la prosa del bucle**, con las apariciones clasificadas en **REGENERADO** (lo
reescribe el ciclo), **ARCHIVO** (medicion con su corte, que reescribir seria falsificar) y **VIVO**
(el que una fusion tiene que redirigir). Resultado: **94 regenerado, 157 archivo, 0 VIVOS**, y la
comprobacion dirigida sobre **los nueve `bridges_aprobados.json`** da **cero apariciones en los
nueve**. **Aun asi se corrio `reanclar_por_resolutor.py`**: una guarda que solo se corre cuando se
sospecha no es una guarda.

**LA SIMULACION PREVIA SELLADA** (`SALIDA_V40_OPD05_SIM.txt`): **las trece guardas en verde**. **Y
el verificador de mapas de `regla 1`** (`SALIDA_V40_VERIFICADOR_MAPAS.txt`), con **los SEIS planes
sellados**: **6 tablas, 37 filas, 0 discrepancias**, varas 1 y 2 CORRIDAS.

### 3.5 LA FUSION EJECUTADA, con las trece guardas

**Se ejecuto tal como estaba sellada, sin recalcular ni una decision**, con el mismo
`scripts/loop/vuelta39_fundir.py` de la vuelta 39: **un superviviente con DOS absorbidos es
exactamente la forma para la que se escribio.**

| guarda | resultado |
|---|---|
| 1, fuente y vida de los tres | OK, **y ahora la etiqueta se MIDE**: `ACTO DE FUENTE UNICA (1 fuente distinta)` |
| 2, conteos contra el plan | OK, 3 de 3 |
| 3, **VERBATIM** contra `dataset/nodos` | **21 de 21**, 0 sobrantes |
| 4, cobertura exacta | **14 de 14 pasos** y **7 de 7 condiciones**, 0 repetidos, 0 faltan, 0 sobran |
| 5, finales derivados de los grupos | OK |
| 6, `preservar_literal` con su sede | **8 de 8** |
| 7, `rastros` con su sede | **5 de 5** |
| 8 y 8b, redirecciones y deprecados | **8 de 8** y **0 de 0** |
| 9, **`P.16`** | **2 duplicadas fabricadas, medidas ANTES de limpiarlas y limpiadas en la misma operacion** |
| 10 y 11, auto aristas y duplicadas | **0** y **0** |
| 12, **`a6`** | titulo y etiqueta **sin tocar** |
| 13, el censo | 3.853 = 3.853, **vivos menos 2** |

**`reanclar_por_resolutor.py` CORRIDO ENTRE LA FUSION Y `run_phase1`**, que es la practica que el
acta de la vuelta 39 adjudico para toda fusion futura: **`nada que re-anclar`**, tal como el plan lo
predijo tras enumerarlos antes.

**LA GUARDA DE SIMETRIZACION, EXACTA Y RELEIDA EN EL FICHERO:** **5 entradas en el log, las 5 para
el superviviente, 0 de otros nodos, 0 faltan y 0 sobran**, y **5 de 5 releidas en
`dataset/nodos/seleccion_ceo_fundador.json`**. *Un log dice lo que el paso 5 cree que hizo; el
fichero dice lo que paso.*

**EL CASO POSITIVO, con el MISMO instrumento las dos veces:** **18 pasan y 24 CAEN antes**, **44
pasan y 0 caen despues**, **conservacion de 1 a 5 vivos**.

### 3.6 `OP-D-05` CERRADA: la verificacion punto por punto

| punto de `OPERACIONES.jsonl` | como quedo |
|---|---|
| **1**, `Gate 0 verde` | **`GATE 0: OK`, exit 0**, mas 71 etiquetas y seis assets |
| **2**, `recomputo del cierre transitivo` | **CORRIDO**: actos **333 a 332**, `CERRADOS` **279 sobre 598** a **278 sobre 595**, `ABIERTOS` **quietos en 54 sobre 243** (el acto estaba CERRADO), nodos en actos **841 a 838**, `A` vigentes **569 a 566**. **Las cuatro comprobaciones: OK las cuatro** |
| **3**, `cada perdida en su bloque` | **CORRIDO**, 6 tablas y 37 filas sin discrepancias, y **21 de 21 piezas VIAJAN**: **la regla de reparto se cumple POR VACIO**, y se dice asi |
| **4**, `el acto leido ENTERO` | **3 de 3 con clase, los tres del ARCHIVO**, cero dirigidas |

**El campo `superviviente` SE ESCRIBE** con `seleccion_ceo_fundador`, **por el precedente medido de
`OP-D-02`**, que es la otra fusion de un solo superviviente y lo tiene escrito. **No es el `null` de
`OP-D-03` (por falta) ni el de `OP-D-04` (por sobra).** El estado sigue en `LISTA` como las cuatro
anteriores. **Cero enlaces de `P.10` que escribir**: el acto era **una familia entera de tres y los
tres se funden**, asi que no queda colgado. **Se dice en vez de callarlo, porque `OP-D-04` si lo
tuvo.**

### 3.7 EL PUNTO DEL ESTANDAR DE PASOS, CERRADO CON EL INSTRUMENTO YA VIVO, Y LO QUE APARECIO

**El resultado queda en SEIS pasos, dentro del estandar.** Pero el instrumento, **corrido otra vez
DESPUES de la fusion**, **CITA al resultante**: bloque **48,4**, corte tras el paso 3. **Y hay que
decir lo que la vuelta 39 SI pudo decir de su caso y esta NO puede: LA FUSION ENCENDIO LA SENAL.**
Antes de fundir daba **43,6** y estaba **fuera** de la cola.

**Eso se MIDIO en vez de sostenerse** (`vuelta40_senal_antes_despues.py`), sobre los **tres**
resultantes de fusion que la campana lleva, leyendo el *antes* de git:

| resultante | bloque ANTES | DESPUES | movimiento | la cola |
|---|---:|---:|---:|---|
| `reglas_brainstorming` (`OP-D-04`) | 47,7 | **50,6** | **mas 2,9** | DENTRO antes y despues |
| `pensamiento_convergente_divergente` (`OP-D-04`) | 0,0 | **43,8** | **mas 43,8** | fuera antes y despues |
| **`seleccion_ceo_fundador`** (`OP-D-05`) | **43,6** | **48,4** | **mas 4,8** | **fuera antes, DENTRO despues** |

> **SUBE EN 3 DE 3**, y el mecanismo es **mecanico y no semantico**: fundir mete el vocabulario de
> tres nodos en menos pasos y mas densos, y la senal mide **solape de tokens**. **Una cita sobre un
> nodo recien fundido es lo esperable.** **Y eso NO autoriza a descartar la cita.**

**LA LECTURA, con el texto delante.** El corte propuesto es **tras el paso 3**: los pasos 1 a 3 son
la **DELIBERACION** (con quien hablarlo, quien es la persona de la idea, con que vara se evalua) y
los 4 a 6 son la **EJECUCION** (que rol alternativo darle, como se negocia el titulo, como se
documenta). **El segundo bloque no vuelve a contar el primero: lo continua.** La pareja citada, los
pasos 1 y 5, comparte el **vocabulario del acto** y no su **narracion**. **VA COMO DISCUTIBLE 1.**

---

## 4. MODO DE EJECUCION CONTINUA: `OP-D-06` ABIERTA Y MEDIDA, **NO EJECUTADA**

**`vuelta39_acto.py --op OP-D-06` ABORTA**, y su salida se sella igual porque **el aborto es
informacion**: lee **18 nodos**, calcula **153 pares posibles** y declara **144 sin clase**.

> **Y no faltan 144 veredictos: es que `OP-D-06` NO ES UN ACTO.** Su propio titulo dice `LOS NUEVE
> ACTOS DE DOS` y su tabla sellada trae los nueve pares con sus nueve puestos. **Los pares cruzados
> entre actos distintos nunca fueron un par.**

Instrumento nuevo, `vuelta40_acto_opd06.py`, que **lee esa particion de la tabla sellada en vez de
teclearla** y comprueba como guarda que **la tabla y la nomina son el mismo conjunto de 18**:

| | medido hoy |
|---|---|
| actos | **9**, todos de dos |
| clases | **8 en `A`, 1 en `C`** (el **494**, que es el solape con `OP-D-01` que el propio plan avisa) |
| nodos vivos | **18 de 18** |
| actos de la misma fuente | **3 de 9** |
| aristas cojas | **CERO en los dieciocho** |
| `9.3.1` sobre los ocho `A` | **CERO nombran ganador**: **los nueve son POR ELEGIR y los nueve piden `P.8`** |

**LO QUE NO SE HIZO Y SE DICE: `OP-D-06` queda ABIERTA Y MEDIDA, NO EJECUTADA.** Cada uno de los
nueve pide su `P.5`, su `P.8` y su plan sellado, mas **los tres cruces con la fase 01** que el
propio plan avisa (`producto_unico_superior` y `propuesta_gasto_capital` en `OP-F-03`,
`future_scenarios_planning` en `OP-F-02`: en los tres manda fuente primero). **VA COMO DISCUTIBLE
5.**

---

## 5. EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE (regla 1)

**Corrido DESPUES de la ultima operacion de la vuelta**, salida en `docs/loop/SALIDA_V40_CIERRE.txt`.

| | apertura | **cierre** | movio |
|---|---:|---:|---|
| `n` | 3.388 | **3.388** | no, y no tenia que moverse: **esta vuelta no emitio ni un veredicto** |
| A / B / C / D | 575 / 83 / 8 / 2.722 | **575 / 83 / 8 / 2.722** | no |
| tasa | 17,0 | **17,0** | no |
| ficheros | 3.853 | **3.853** | no, **nadie borrado** |
| vivos | 3.534 | **3.532** | **si, menos 2**: los dos absorbidos |
| deprecados | 319 | **321** | **si, mas 2** |
| enlaces | 16.869 | **16.871** | **si, mas 2** |
| operaciones | 71 `LISTA`, 0 rotas | **71 `LISTA`, 0 rotas** | no |
| inventario | 672 | **672** | no |

**LA ARITMETICA DE LOS ENLACES, comprobada ENTRADA POR ENTRADA y no publicada a ojo:**
`criterios_equity_split.nodos_previos` **menos 1**;
`decision_fundador_solo_vs_equipo.nodos_siguientes` **menos 2** (nombraba a los DOS absorbidos y
ademas ya al superviviente, asi que tres entradas colapsan en una);
`seleccion_ceo_fundador` **mas 1** en `nodos_previos` y **mas 4** en `nodos_siguientes` por la
simetrizacion. **Menos 1, menos 2, mas 1, mas 4 igual mas 2; y 16.871 menos 16.869 es 2.**

**LA TASA POR DOMINIO AL CIERRE** (`SALIDA_V40_TASA_DOMINIO.txt`), **impresa y no tecleada**:

```
dominio                   n      A     tasa      B      C      D
core                   1445    336    23.3%     81      8   1020
quality                 844    126    14.9%      0      0    718
health_safety           192     45    23.4%      0      0    147
entrega                 171      2     1.2%      0      0    169
environmental           170     29    17.1%      0      0    141
compras                 155      1     0.6%      2      0    152
franquicias             148     18    12.2%      0      0    130
exportacion             130     15    11.5%      0      0    115
risk_management         106      0     0.0%      0      0    106
seguridad_digital        27      3    11.1%      0      0     24
```

**FIGURAS Y FAMILIAS AL DIA**, del inventario recontado al cierre: **672 entradas** (dominio 10,
acto 556, racimo 13, familia_de_ids 54, **figura 20**, defecto 19). **Familias de libro**: Weinberg
**72 / 70**, Horowitz **93 / 91**, Hugos **111 / 111**, Coleman **75 / 73**, Rackham **47 / 47**.
**Ninguna se movio, y ninguna tenia que moverse.**

**VARA POR TRAMO:** esta vuelta **no es de cribado y no emitio veredictos**, asi que **no hay vara
de tramo que publicar**. Se dice en vez de rellenar la casilla.

**LAS SUITES:** motor **25 de 25** exit 0; web **80 ficheros, 1.030 pasadas, 3 saltadas** exit 0;
`tsc --noEmit` **cero lineas** exit 0. **`GATE 0: OK`** con 3.853 compilados y alcanzabilidad
**100 por ciento**.

---

## 6. CORRECCIONES DECLARADAS (regla 8: nada se borra)

1. **MI PROPIO INSTRUMENTO `vuelta40_acto_opd06.py` MEDIA MAL `9.3.1` EN SU PRIMERA VERSION.**
   Probaba si la razon nombraba ganador **buscando el id del nodo**, y eso da **SI casi siempre**
   porque las razones empiezan por *REPITE con `<id>`*. **Corregido a la vara del hermano mayor**
   (que busca el VERBO de adjudicacion) **ANTES de publicar nada**, y la salida sellada trae ya la
   buena: **cero de ocho**, no ocho de ocho. **La vara se copio en vez de reinventarse** para que
   las dos medidas sean comparables, y va dicho dentro del codigo.
2. **LA ETIQUETA DE LA GUARDA 1 DE `vuelta39_fundir.py` AFIRMABA `ACTO DE FUENTE MIXTA` SIEMPRE.**
   Era cierto de los dos actos de `OP-D-04` y **falso de `OP-D-05`**. **Ahora se calcula**: cuenta
   las fuentes distintas y dice `UNICA` o `MIXTA`. **La medicion nunca estuvo mal, la etiqueta si**,
   y un instrumento que imprime una etiqueta falsa mientras mide bien es la degradacion silenciosa
   contra la que existen sus propias guardas. La simulacion se re-corrio tras el cambio.
3. **LA CIFRA DE VIVOS DE LA TABLA DE APERTURA DE ESTE REPORTE.** Se escribio primero `3.538`,
   copiando la forma de la tabla de la vuelta 39, **y la medicion de hoy dice `3.534`**. **El texto
   viejo se deja tachado en su sitio** en la seccion 0 en vez de sustituirse: es exactamente la
   especie de caida que la regla 1 nombra.
4. **LA PRIMERA SALIDA DE `vuelta40_costuras_opd05.py` SALIO ILEGIBLE**, con la codificacion de la
   consola comiendose los acentos de los pasos citados. **Re-corrida con `utf-8` y sellada de
   nuevo**: una cita que no se puede leer no sirve de cita.

---

## 7. LOS DISCUTIBLES MARCADOS, antes de saber si acierto

**DISCUTIBLE 1. DECLARO QUE NO HAY COSTURA EN UN NODO QUE MI PROPIA FUSION METIO EN LA COLA.**
`seleccion_ceo_fundador` pasa de **43,6 (fuera)** a **48,4 (dentro)**. Sostengo que no es costura
porque la lectura del texto dice que el segundo bloque **continua** al primero y no lo repite, y
porque la senal **sube en 3 de 3 fusiones medidas** por construccion. **Lo discutible es que el
mismo que hizo la fusion sea el que absuelve al resultante, y que mi argumento general (la senal
sube siempre al fundir) sirve para absolver cualquier resultante futuro.** La alternativa era
**abrir un destejido sobre un nodo recien fundido en la misma vuelta**. Elegi leer y declarar.
**Que se me discuta.**

**DISCUTIBLE 2. EL FIXTURE FRAGIL SE QUEDA, Y LA PUERTA SIGUE A DOS DECIMAS DE CAER.**
`economia_circular_como_modelo_de_negocio` entra por **mas 0,2**, y la semantica de la puerta
(**tienen que entrar TODOS**) **no la afloje**. O sea que **el instrumento puede volver a negarse
entero por un fixture al borde**, que es la misma especie de averia que acabo de reparar. **Lo
sostengo porque dispara hoy y es uno de los dos fundadores de la clase, y retirar un fixture que SI
cumple el criterio seria acomodar la puerta en vez de repararla**; y por eso anadi el aviso de borde
en vez de tocar la lista. **Lo discutible es no haberla dejado a prueba de eso.**

**DISCUTIBLE 3. USE UNA COLA QUE LA PROPIA CASA LLAMA ROTA.** El instrumento entrega **1.496 nodos,
el 42,3 por ciento del catalogo**, y su encabezado dice que *una baranda que caza lo correcto no es
estricta, esta rota*. **Con esa cola decidi el destejido de `OP-D-05`.** Lo sostengo porque lo que
use no fue el ranking global sino **lo que el instrumento dice de TRES nodos concretos**, y para eso
la tasa de la cola no cambia la medida de cada nodo. **Lo discutible es que el encargo mandaba
reparar la puerta y correr el instrumento, y el resultado es un instrumento que entrega una cola que
su propia doctrina rechaza.** No toque el umbral porque el encargo lo prohibe.

**DISCUTIBLE 4. EL ANCLA DE LA CALIBRACION ES UN NODO QUE NINGUNA PAGINA NOMBRA.**
`fases_traccion_producto` no aparece en el acta, ni en el encargo, ni en el plan: **lo elegi yo**,
por un criterio que **yo mismo escribi** dentro del instrumento (el mas alto del catalogo y sin
nomina de operacion). El encargo pedia *criterio escrito*, y el criterio **quedo escrito**, pero
**lo escribi en esta vuelta**. **Lo discutible es si eso cuenta como criterio escrito o como
criterio propio.** La alternativa era quedarme con los dos que el encargo y el acta nombran, y
entonces la puerta se apoyaria en un fixture al borde y en uno que la propia acta mando a la cola de
lectura.

**DISCUTIBLE 5. NO EJECUTE `OP-D-06`.** El encargo dice *retoma el MODO DE EJECUCION CONTINUA con la
siguiente operacion*. **La abri, la medi entera acto por acto y escribi el instrumento que hacia
falta, pero no fundi ninguno de los nueve.** Lo sostengo porque cada uno de los nueve es un acto con
su `P.5`, su `P.8` y su plan sellado, y **tres de ellos cruzan con la fase 01 con la regla de fuente
primero por delante**: hacerlos a media maquina habria sido peor que dejarlos medidos. **Lo
discutible es que eso es una decision de alcance que el encargo no me delego.**

---

## 8. PENDIENTES DE DOCTRINA

**NUEVO 1: LA SENAL DE BLOQUE NO ES NEUTRAL RESPECTO DE LA FUSION, Y NINGUNA PAGINA LO DICE.**
Medido: **sube en 3 de 3** resultantes de fusion, y en uno de los tres **mete al resultante en la
cola**. Ninguna pagina dice como se lee una cita sobre un nodo recien fundido. **Lo mejor sostenido
y aplicado hoy: la cita se lee siempre con el texto delante, y el hecho de que la fusion la haya
encendido se declara en el cierre.** No lo elevo a regla: **lo registro y sigo** (regla 5).

**NUEVO 2: `OPERACIONES.jsonl` GUARDA COMO UNA OPERACION LO QUE EL PLAN LLAMA NUEVE ACTOS.** El
instrumento del acto aborta contra `OP-D-06` porque su nomina de 18 no es un acto. **Lo mejor
sostenido y aplicado hoy: leer la particion de la tabla sellada del plan.** Es primo del pendiente
heredado *el acto que se parte en dos*.

**HEREDADO Y SIGUE ENTERO: QUE UMBRAL ACOMPANA A `MIN_BLOQUE = 2`.** La cola en **42,3 por ciento**
del catalogo. **Decision del fundador**, declarada desde la vuelta 34 y **no tocada hoy**.

**HEREDADOS, vivos y ninguno bloquea:** que una fusion mire los registros que no son el grafo (hoy
**enumerados en el plan** por primera vez, y el re-anclaje corrido igual); el recomputo que no ve
las dirigidas; el estado `HECHA` que no existe en el esquema; el esquema frente a dos
supervivientes (`a4`); el titulo del nodo del taller (`a6`); la linea general de prelacion; y los
pendientes 5 a 9 de la vuelta 36.

---

## 9. PREGUNTAS, lo que no esta escrito y no pude medir

1. **Puede un fixture de calibracion ser un nodo que la propia campana tenga en cola de lectura?**
   `reglas_brainstorming` es fixture desde hoy **y** esta encargado a la cola de lectura por el acta
   de la vuelta 39. Si esa lectura lo desteje, el fixture queda rancio **y la puerta vuelve a
   caer**. El criterio 4 que escribi (preferir el que no este en nomina de operacion) apunta a eso,
   pero **no lo prohibe**. **Debe prohibirlo?**
2. **Vale la cola al 42,3 por ciento como base de lectura, o el instrumento solo sirve nodo a
   nodo?** Hoy la use nodo a nodo y lo declare. **Si la respuesta es que solo sirve asi, deberia
   decirlo el propio instrumento en su salida.**
3. **`OP-D-06` se parte en nueve operaciones o se ejecuta como una con nueve actos?** De la
   respuesta depende si el registro se toca (nueve `id_op`) o si basta con que el instrumento lea la
   particion del plan, que es lo que hice hoy sin tocar el registro.

---

## 10. RUTAS TOCADAS, COMMITS E INSTRUMENTOS

`git diff --numstat e7623461..HEAD` corrido hoy: **71 ficheros, 8.830 insertadas, 278 borradas.**

| carpeta | ficheros |
|---|---:|
| `docs/loop` | 35 |
| `scripts/loop` | 16 |
| `dataset/nodos` | 10 |
| `docs/plan` | 3 |
| `web/lib/assets` | 2 |
| `docs` | 2 |
| `dataset/metadata` | 2 |
| `scripts` | 1 |

**Los commits de la vuelta, en orden:** `513267db` (tarea 1), `55811eb5` (la puerta reparada),
`002edf43` (la apertura, sola), `bdd7a82a` (el destejido leido), `764de090` (el plan sellado),
`7e8c1f36` (la fusion ejecutada), `70878328` (`OP-D-05` cerrada), `d9ec5481` (`OP-D-06` abierta),
`960de876` (el estado al cierre) y **`6a6544e0`** (este reporte). **El hash de este reporte se
anade DESPUES de commitear, medido con `git log` y no anticipado**, que es la unica forma de
citarlo sin inventarlo.

**INSTRUMENTOS NUEVOS, todos con su sucesion declarada dentro del codigo:**

| instrumento | sucede a | que anade |
|---|---|---|
| `vuelta40_calibrar_costuras.py` | `vuelta34_calibrar_costuras.py` | elige fixture con la vara delante en vez de mover un dial |
| `vuelta40_guarda_puerta.py` | nuevo | el caso positivo de la puerta, con la averia original reproducida a proposito |
| `vuelta40_costuras_opd05.py` | `vuelta34_costuras_opd03.py` | **lee la cola entregada** en vez de reimplementar las senales |
| `vuelta40_destejido_opd05.py` | nuevo | la costura declarada por el archivo, buscada por HUELLA en el nodo de hoy |
| `vuelta40_reciprocidad_post.py` | `vuelta38_reciprocidad_post.py` | la fusion entra por la linea de ordenes, no por el codigo |
| `vuelta40_registros_no_grafo.py` | nuevo | la leccion de la vuelta 39 hecha instrumento, con las tres clases de registro |
| `vuelta40_plan_opd05.py` | los planes tecleados de la vuelta 38 | **genera** el plan: origenes verbatim, redirecciones medidas, tabla derivada |
| `vuelta40_registro_opd05.py` | nuevo | el registro del plan escrito por instrumento, con su tabla validable |
| `vuelta40_cerrar_opd05.py` | `vuelta39_cerrar_opd04.py` | UN superviviente, y por eso el campo **se escribe** |
| `vuelta40_senal_antes_despues.py` | nuevo | que le hace una fusion a la senal, medido en los tres casos |
| `vuelta40_acto_opd06.py` | `vuelta39_acto.py` | lee la particion en NUEVE actos de la tabla sellada |
