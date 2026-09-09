### TAREA 2. LAS DOS CLAUSULAS QUE TODAVIA SE PUEDEN MOVER LEYENDO

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:**
``docs/loop/SALIDA_V219_T2_LECTURAS.txt``, **28878 bytes en disco y 28878 normalizado a LF**, exitcode 0.

**ES LECTURA, NO INSTRUMENTO NUEVO.** `scripts/loop/_v219_t2_lecturas.py`
lleva prefijo de guion bajo, esta fuera del censo y fuera de la nomina, y muere
con la vuelta. **La sonda de la clausula NO SE CLONO: se IMPORTA** de
`scripts/loop/_v217_t1_diecisiete.py`, que es la que publico el 7, y el
resolutor viene por la misma via. **Las dos clausulas bloqueadas no se
intentaron**, que es lo que el encargo manda: `07 ADUANA` idx 0 depende de un
control que no corre y de una celda que es sede del fundador, y `03 FUSIONES`
idx 0 depende de ejecutar las SEIS fusiones enrutadas, que es trabajo de plan y
no de lectura.

**EL ESTADO DEL ARBOL, MEDIDO AL EMPEZAR LA TAREA:**
- EL GRAFO DE HOY, MEDIDO Y NO HEREDADO: 3853 nodos en el censo, 3169 vivos.
- EL EXPEDIENTE DE HOY: 71 fichas leidas de docs/plan/OPERACIONES.jsonl.

#### 2.a. `01 FUENTES` idx 1: EL MATERIAL DEL SEGUNDO LIBRO, REUBICADO O BORRADO

**PRIMERO LA CIFRA, REPRODUCIDA Y NO HEREDADA, QUE ES LO QUE EL ENCARGO PIDE
ANTES DE NADA:**

- sonda> CIFRA menciones que TODAVIA declaran mas de una fuente: 7
- CIFRA menciones que TODAVIA declaran mas de una fuente, MEDIDA HOY POR MI: 7 | CIFRA que el acta 217 publica en su linea 77346: 7

**LAS DOS CIFRAS CALZAN, ASI QUE NO HAY PARADA POR AHI.** Y digo, porque
callarlo seria sesgo, que **la sonda por su propio detector estrecho sigue
diciendo `A MEDIAS`**: EL VEREDICTO QUE LA SONDA DA HOY POR SU PROPIO DETECTOR (el estrecho, el que mira si el nodo sigue declarando dos fuentes): A MEDIAS **Ese no es el detector que el encargo
manda usar**, y la vara que si es la de la `4.5` del acta 218 (**linea 77628**
de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero): **reubicado es un hecho
comprobable en el grafo, no una frase escrita en una ficha.**

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V219_T2_LECTURAS.txt` Y NO TECLEADA** (7 filas armadas
leyendo ese fichero, y **la cifra que deberia haber es 7**):

| # | ficha | nodo que la declara | libro de la tanda | vive hoy | donde vive hoy (resuelto) | como |
|---:|---|---|---|---|---|---|
| 1 | `OP-F-03` | `principio_calidad_mvp` | Hugos | **VIVE** | `ejecucion_incremental_transicion_tecnologica` | mudado al receptor, los 4 actos comprobados en sus pasos |
| 2 | `OP-F-04-COL` | `keep_customers_strategy` | Coleman | **VIVE** | `keep_customers_strategy` | fundido DENTRO del propio nodo, fuente intacta |
| 3 | `OP-F-04-COL` | `viral_loop_marketing` | Coleman | **VIVE** | `viral_loop_marketing` | fundido DENTRO del propio nodo, fuente intacta |
| 4 | `OP-F-04-HOR` | `decision_de_vender_startup` | Horowitz | **VIVE** | `decision_de_vender_startup` | fundido DENTRO del propio nodo, fuente intacta |
| 5 | `OP-F-04-HOR` | `principio_calidad_mvp` | Horowitz | **VIVE** | `principio_calidad_mvp` | fundido DENTRO del propio nodo, fuente intacta |
| 6 | `OP-F-04-WEI` | `coeficiente_viral` | Weinberg | **VIVE** | `coeficiente_viral` | fundido DENTRO del propio nodo, fuente intacta |
| 7 | `OP-F-04-WEI` | `viral_loop_marketing` | Weinberg | **VIVE** | `viral_loop_marketing` | fundido DENTRO del propio nodo, fuente intacta |

**SEIS DE LAS SIETE VIVEN DENTRO DE SU PROPIO NODO, Y NO POR DESCUIDO: POR
DOCTRINA.** `P.19` punto 2 **obliga** a dejar el campo `fuente` intacto cuando
el material se funde dentro del nodo en vez de salir, y `01_FUENTES.md` lo dice
con todas las letras: *ahi la fuente se reduce porque el material se fue; aqui
el material se queda y solo deja de estar dicho dos veces*. **Los cinco nodos
que las alojan estan VIVOS, resueltos con el resolutor delante, y sus pasos de
hoy calzan uno a uno con la cifra que su propio registro publico** (23, 15, 8,
7 y 6).

**Y LA SEPTIMA ES LA UNICA QUE SE MUDO, Y ES LA QUE HABIA QUE COMPROBAR DE
VERDAD.** El bloque de Hugos de `principio_calidad_mvp`, tramo **11 a 14**, ya
no vive en el nodo que lo declaraba: su enrutamiento esta escrito en la
**linea 500** de `docs/plan/01_FUENTES.md` y su destino es
`ejecucion_incremental_transicion_tecnologica`. **No me creo el registro: lo
comprobe acto por acto contra los pasos del receptor**, y los cuatro estan:

- acto 'funcionalidades criticas' -> PASO 9: Identificar las funcionalidades críticas que generan el mayor valor.
- acto 'excluir las secundarias' -> PASO 10: Excluir deliberadamente características secundarias en la primera versión.
- acto 'lanzar la minima viable' -> PASO 11: Lanzar la solución mínima viable y monitorear su desempeño.
- acto 'iterar con el uso real' -> PASO 12: Iterar y mejorar el sistema en función del uso real y feedback.

CIFRA actos del material hallados en el receptor: 4 | CIFRA que el registro promete: 4

**EL SALDO, Y LA VARA APLICADA SIN PROMEDIAR:**

CIFRA menciones cuyo material VIVE en un nodo vivo del grafo: 7 | CIFRA menciones BORRADAS SIN DESTINO: 0 | CIFRA total de menciones: 7

CIFRA borradas sin destino: 0 | CIFRA que la vara tolera: 0

**VEREDICTO DE 01 FUENTES idx 1: CUBRE**

#### 2.b. `05 SANEO` idx 1: LOS TRES DE INCOTERMS CON SU VERSION

**LA ANOTACION DEL ACTA 120, LOCALIZADA Y CON SU LINEA LEIDA DEL FICHERO, QUE
ES LO QUE EL ENCARGO PIDE Y NO DE MEMORIA:**

- EL ACTA 120 EMPIEZA EN LA LINEA 41598, LEIDA DEL FICHERO> # ACTA DE LA VUELTA 120 DEL AUDITOR (28 ago 2026, fecha LEIDA DE GIT, Opus 5)
- LA ADJUDICACION 3.1 DEL ACTA 120 VIVE EN LA LINEA 41699, Y ESTAS SON SUS LINEAS LEIDAS DEL FICHERO:

> 41699> **3.1 EL DISCUTIBLE (b) NO ES DOCTRINA NUEVA Y NO ES PARADA: SE ADJUDICA CITANDO DOS REGLAS
> 41700> ESCRITAS, Y RATIFICO LA LECTURA DE ALCANCE DEL EJECUTOR.** Fui a la fusion que produjo el
> 41701> superviviente y la lei: `docs/plan/03_FUSIONES.md`, **acto 16 del lote A** (`seguro_exportacion`
> 41702> absorbe `seguro_de_carga_transporte`), **6 piezas: 2 enteras, 3 ya dichas, 1 `INCISO`**, y su
> 41703> unica perdida nombrada es **DE CONDICIONES**, no de pasos. **O sea que el paso 1 se conto como
> 41704> "ya dicha"**, que es exactamente la clase **VIVE DENTRO** de **P.13**: la unidad del reparto es
> 41705> **el paso**, no la palabra, y el parentesis `(Incoterms)` cayo por debajo de esa granularidad.
> 41706> **Por eso no hay perdida sin declarar en la fusion 16, y por eso restituir la palabra NO cabe en
> 41707> `OP-S-02`**, cuyo acto literal es *anadir version a una cita que ya existe*. **Y el resto se
> 41708> resuelve por extension natural del punto 2 de la decision del fundador del 28 ago 2026** (el
> 41709> contenido que la operacion no alcanza **se anota en la ficha y no se ejecuta**, y el punto de
> 41710> `verificacion` se acota por correccion declarada), **que es literalmente lo que ya se hizo con
> 41711> `OP-S-01`**. **Adjudico: `seguro_exportacion` NO se toca; la mitad que falta es LA ANOTACION,
> 41712> que la 120 no escribio, y va como tarea de la 121.** El *"PENDIENTE DE DOCTRINA"* de la nota de
> 41713> `OP-S-02` **queda adjudicado por esta acta** y se corrige por remision, sin borrar el texto.

**Y SU SEDE, PORQUE UNA ADJUDICACION QUE MANDA ANOTAR NO ES LA ANOTACION.** El
acta 120 dice que *la mitad que falta es LA ANOTACION, que la 120 no escribio, y
va como tarea de la 121*, y esa anotacion **existe y la localice**:

- LA SEXTA ENTRADA VIVE EN LA LINEA 1574 DE docs/PENDIENTES.md, LEIDA DEL FICHERO> ### SEXTA entrada (vuelta 121, adjudicacion del auditor en el acta 120 seccion 3.1 sobre OP-S-02): `seguro_exportacion` perdio la palabra "Incoterms" de su paso 1 en la fusion del `ACTO 16`

> 1597> nodo no se toca en esta vuelta**: queda anotado como trabajo post campaña, igual
> 1598> que las entradas de arriba.

**LOS TRES DE LA NOMINA, LEIDOS DEL EXPEDIENTE Y NO TECLEADOS:**

- EL SUJETO SON LOS TRES DE LA NOMINA DE OP-S-02, leidos del expediente (linea 11) y no tecleados. CIFRA nodos de la nomina: 3 | CIFRA que la clausula escribe: 3
- EL ESTADO DE LA FICHA, LEIDO DEL EXPEDIENTE: HECHA

**LA TABLA, PEGADA ENTERA DE `docs/loop/SALIDA_V219_T2_LECTURAS.txt`** (3 filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 3**):

| # | nodo de la nomina | declara version hoy | cual | de donde sale | estado del nodo |
|---:|---|---|---|---|---|
| 1 | `incoterms_reglas_comerciales_internacionales` | **SI, en el propio nodo** | Incoterms 2020 | incoterms_reglas_comerciales_internacionales, campo resumen_teorico | vivo |
| 2 | `terminos_de_venta_incoterms` | **SI, por su superviviente** | Incoterms 2020 | incoterms_reglas_comerciales_internacionales, campo resumen_teorico | deprecado, resuelve a incoterms_reglas_comerciales_internacionales |
| 3 | `seguro_de_carga_transporte` | **NO** | (ninguna) | (ninguno: ni el nodo ni su superviviente la fijan) | deprecado, resuelve a seguro_exportacion |

CIFRA de los tres que llegan a una version de Incoterms, por si mismos o por su superviviente: 2 de 3

**LA PREGUNTA QUE DECIDE LA CLAUSULA ES DE FRONTERA Y NO DE CONTEO, Y NO LA
DECIDO YO.** Va entera al bloque de discutibles de abajo, con mi lectura y su
motivo, y **no se aplica al recuento**:

- LA PREGUNTA QUE DECIDE LA CLAUSULA ES DE FRONTERA Y NO DE CONTEO, Y NO LA DECIDO YO: un nodo que la campana DIFIRIO A PROPOSITO Y POR DECISION ESCRITA, cuenta como incumplimiento de la clausula o como fuera de su alcance?
- LO MEDIDO: 2 de 3 llegan a la version; el que no es el tercero, y su motivo esta escrito en las dos sedes localizadas arriba.
- MI LECTURA, CON SU MOTIVO Y MARCADA COMO DISCUTIBLE: la escribo en el reporte, en la seccion de discutibles, y NO la aplico al recuento. La clausula se queda donde estaba mientras la frontera no se adjudique.

**VEREDICTO DE 05 SANEO idx 1 QUE ESTA TAREA APLICA: A MEDIAS (SIN MOVER), y la razon es que la frontera es del auditor y no mia.**

#### 2.c. EL RECUENTO DE LAS DIECISIETE, REHECHO AL CIERRE DE ESTA TAREA

**NO SE HEREDA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). Las
17 filas salen de mi propia corrida de hoy, y la unica que esta tarea mueve es
la de `01 FUENTES` idx 1:

- LA FUENTE DE LAS 17 FILAS ES MI PROPIA CORRIDA DE HOY, sellada en ``docs/loop/SALIDA_V219_T1_RECORRIDA_DEL_LECTOR.txt``.
- CIFRA filas armadas leyendo ese fichero: 17 | CIFRA que deberia haber: 17
- EL REPARTO QUE LA TAREA 1 DEJO MEDIDO: CUBRE 13 | A MEDIAS 4 | NO CUBRE 0
- SUBE POR LECTURA: 01 FUENTES idx 1, de A MEDIAS a CUBRE
- CIFRA clausulas que esta tarea mueve: 1 | CIFRA que el encargo pone en juego: 2 (y la de 05 SANEO no se mueve porque su frontera es del auditor)

**LAS TRES CIFRAS DEL CIERRE, CADA UNA CON LA QUE LA TAREA 1 DEJO AL LADO:**

- CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: 14 de 17 | CIFRA que dejo la TAREA 1: 13
- CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2: 3 de 17 | CIFRA que dejo la TAREA 1: 4
- CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2: 0 de 17 | CIFRA que dejo la TAREA 1: 0

**LA TABLA ENTERA AL CIERRE DE ESTA TAREA, PEGADA DE `docs/loop/SALIDA_V219_T2_LECTURAS.txt`**
(17 filas armadas leyendo ese fichero, y **la cifra que deberia haber es
17**):

| # | fila | idx | veredicto | la clausula, VERBATIM |
|---:|---|---:|---|---|
| 1 | 0 CODIGO | 0 | CUBRE | cada caso positivo **se cae antes** del arreglo y pasa despues |
| 2 | 01 FUENTES | 0 | CUBRE | ningun nodo de la clase con pasos alterados |
| 3 | 01 FUENTES | 1 | CUBRE (SUBE POR LECTURA: la TAREA 1 la dejo en A MEDIAS) | **el material del segundo libro reubicado, no borrado** |
| 4 | 02 DESTEJIDOS | 0 | CUBRE | los **quince congelados** releidos |
| 5 | 02 DESTEJIDOS | 1 | CUBRE | **cada perdida en el bloque del que proviene** |
| 6 | 03 FUSIONES | 0 | A MEDIAS | un superviviente por acto, el resto **DEPRECADO CON ALIAS** |
| 7 | 03 FUSIONES | 1 | CUBRE | `resolverId` devuelve el superviviente |
| 8 | 04 ENLACES | 0 | CUBRE | cada arista nueva **confirmada por lectura**, no por el instrumento |
| 9 | 04 ENLACES | 1 | CUBRE | ninguna crea auto-arista tras resolver |
| 10 | 05 SANEO | 0 | CUBRE | ningun id vivo con tratado extinto |
| 11 | 05 SANEO | 1 | A MEDIAS | los tres de Incoterms con su version |
| 12 | 05 SANEO | 2 | CUBRE | ningun nodo cablea `export.gov` |
| 13 | 05 SANEO | 3 | CUBRE | ninguna de las seis herramientas muertas |
| 14 | 05 SANEO | 4 | CUBRE | ningun nodo con dos claves de fase |
| 15 | 05 SANEO | 5 | CUBRE | **ningun nodo se cita a si mismo tras resolver** |
| 16 | 06 MESAS | 0 | CUBRE | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| 17 | 07 ADUANA | 0 | A MEDIAS | los cuatro controles mecanicos **corriendo en Gate 0** |

**LAS QUE SIGUEN SIN CUBRIR, CON SU FILA, SU INDICE Y SU CIFRA:**

- 03 FUSIONES    idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
- 05 SANEO       idx 1 | A MEDIAS  | los tres de Incoterms con su version
- 07 ADUANA      idx 0 | A MEDIAS  | los cuatro controles mecanicos **corriendo en Gate 0**

CIFRA clausulas que siguen sin cubrir: 3

#### 2.d. LA PARADA FELIZ: NO SE PROPONE, Y LA CONDICION NO LA PONGO YO

- LA CONDICION PIDE QUE LAS DIECISIETE QUEDEN EN CUBRE.
- CIFRA en CUBRE: 14 | CIFRA que la condicion exige: 17
- LA CONDICION SE CUMPLE: NO
- POR TANTO, LA PARADA FELIZ: NO SE PROPONE, y las que faltan van arriba con su fila, su indice y su cifra

#### ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA

- docs/plan/OPERACIONES.jsonl AL ENTRAR: sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b
- docs/plan/OPERACIONES.jsonl AL SALIR:   sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b, 517181 bytes en disco y 517181 normalizado a LF
- docs/plan/08_VERIFICACION.md AL ENTRAR: sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4
- docs/plan/08_VERIFICACION.md AL SALIR:   sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4, 73652 bytes en disco y 73652 normalizado a LF
- docs/plan/07_ADUANA.md AL ENTRAR: sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0
- docs/plan/07_ADUANA.md AL SALIR:   sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0, 3815 bytes en disco y 3723 normalizado a LF
- docs/plan/01_FUENTES.md AL ENTRAR: sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3
- docs/plan/01_FUENTES.md AL SALIR:   sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3, 128187 bytes en disco y 126666 normalizado a LF
- docs/plan/05_SANEO.md AL ENTRAR: sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806
- docs/plan/05_SANEO.md AL SALIR:   sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806, 39450 bytes en disco y 38699 normalizado a LF
- docs/plan/INVENTARIO.jsonl AL ENTRAR: sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a
- docs/plan/INVENTARIO.jsonl AL SALIR:   sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a, 629533 bytes en disco y 629533 normalizado a LF

LOS 12 SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS CONVENCIONES: SI

#### LOS DISCUTIBLES DE LA TAREA 2, MARCADOS ANTES DE SABER SI ACIERTO

| # | que decidi | la duda que dejo escrita |
|---|---|---|
| **D.1** | QUE LA VARA DE REUBICADO ES LA DEL GRAFO Y NO LA DEL CAMPO `fuente` | Subo `01 FUENTES` idx 1 a **CUBRE** aplicando la vara que la `4.5` del acta 218 (**linea 77628** de `docs/loop/ACTA_AUDITOR.md`) fija: **reubicado es un hecho comprobable en el grafo, no una frase escrita en una ficha**, y el encargo la repite palabra por palabra. **Y digo antes de saber si acierto que la sonda del instrumento de la 217 sigue diciendo A MEDIAS por su propio detector**, que mira si el nodo dejo de declarar dos fuentes. **Las dos lecturas estan medidas y publicadas juntas arriba.** Si el auditor lee que *reubicado* exige que el material SALGA del nodo, entonces **cinco de las siete no lo estan** (las que `P.19` y `P.20` fundieron dentro dejando la fuente intacta a proposito) y **la clausula vuelve a A MEDIAS**. Mi motivo para leerlo al reves es que `P.19` punto 2 **obliga** a dejar la fuente intacta cuando el material se funde dentro, asi que **el campo `fuente` sin tocar es la senal de la operacion hecha, no la de la operacion pendiente**: castigarla seria medir contra una vara que la propia doctrina prohibe cumplir. |
| **D.2** | QUE LA FRONTERA DE LA 2.b NO LA DECIDO, PERO SI DIGO COMO LA LEO | El encargo me manda medir los tres, escribir mi lectura con su motivo y **marcarla**, y eso hago: **NO la aplico al recuento** y `05 SANEO` idx 1 se queda en **A MEDIAS sin mover**. **Como la leo yo:** el tercero queda **FUERA DEL ALCANCE** de la clausula, no como incumplimiento. **El motivo, y es una cita, no una opinion:** el acto literal de `OP-S-02` es *anadir version a una cita que ya existe*, y el superviviente del tercero **no tiene la cita**, porque la palabra se perdio en una fusion anterior por debajo de la granularidad del paso. Eso lo adjudico el acta 120 en su **linea 41699** y quedo anotado como trabajo post campana en la **linea 1574** de `docs/PENDIENTES.md`, las dos leidas hoy del fichero. **Y es la misma forma de razonar que el auditor uso en su `4.4`** (acta 218, **linea 77614**): una clausula de verificacion verifica **lo que su operacion hizo**. **Si el auditor lee lo contrario**, que un diferido escrito sigue contando como incumplimiento mientras el nodo no lleve la version, **la clausula se queda en A MEDIAS para siempre** hasta que alguien ejecute el trabajo post campana, y eso conviene saberlo antes de medir la parada feliz contra ella. |
| **D.3** | QUE EL REPARTO DE TANDA A LIBRO ES MIO | La pregunta *cual es el segundo libro de esta mencion* la contesto yo con una tabla escrita a mano de seis entradas (`OP-F-02` a Mollick, `OP-F-03` a Hugos, y las cuatro de `OP-F-04` a Coleman, Horowitz, Weinberg y Rackham). **No se puede deducir del campo `fuente`**, y el propio `01_FUENTES.md` explica por que: un nodo que no se toco y uno fundido por `P.19` **se ven igual ahi**. **La guarda que le puse**: la propia ficha del expediente tiene que nombrar ese apellido en su texto, y las seis lo hacen. **Lo que esa guarda NO prueba** es que el apellido nombrado sea el de la tanda y no otro citado de pasada, **y eso lo digo yo en vez de dejar que parezca comprobado**. |

#### EL CASO ROJO, DICHO CUAL ES CUAL

EL CASO ROJO, DICHO CUAL ES CUAL: la reproduccion del 7, el campo fuente, el resolutor, la cuenta de pasos contra la publicada, los cuatro actos del material mudado dentro de su receptor, las lineas de acta y de PENDIENTES y la version de Incoterms campo a campo CAEN EN ROJO por si solas y estan contadas arriba. LO MIO ES EL REPARTO DE TANDA A LIBRO, que va con guarda que exige que la propia ficha nombre el apellido, Y LA LECTURA DE FRONTERA DE LA 2.b, QUE VA MARCADA COMO DISCUTIBLE: para esa NO HAY CASO ROJO AUTOMATICO y se declara en vez de fabricarse uno que se apruebe solo.
