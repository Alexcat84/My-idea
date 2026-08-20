# REPORTE DE LA VUELTA 63 (20 ago 2026, ejecutor Opus 5)

**LO PRIMERO, PORQUE ES LO QUE LA VUELTA ENTREGA: EL PUESTO 1 DE LA FASE 03 QUEDA CERRADO.** Agotada
`OP-U-01` en la vuelta anterior, esta vuelta ejecuta **LAS DOS FUSIONES DE MESA QUE QUEDABAN EN ESE
PUESTO**, en el orden adjudicado el 19 ago 2026 y sin elegirlo: **`OP-M-03-I` y despues
`OP-M-02-PROG`**. **Son las DOS PRIMERAS FUSIONES DE MESA DE LA CAMPANA.** Y ademas queda **MEDIDA
la apertura de `OP-U-02` sin fundir ni un acto suyo**, con su nomina fijada en fichero propio.

**LA FECHA ESTA MEDIDA POR DOS RELOJES Y NO SUPUESTA:** `date` del sistema da `2026-08-20` y
`git log -1 --date=format:'%Y-%m-%d'` da `2026-08-20`. Es la misma medicion que el campo `fecha` de
los dos planes sellados, que la lee del reloj y no de una constante.

**LA RACHA DE REPORTE ESTABA EN UNO Y SU LECCION MANDABA EN ESTA VUELTA.** La regla que el acta 62
dejo escrita (*lo que un motivo sellado prometa del reporte, el reporte lo cumple; y si un discutible
del plan no llega a la seccion 6, el reporte lo DICE con su motivo*) **se cumple aqui POR MAQUINA y no
por atencion**: nace `scripts/loop/comprobar_promesas_de_marcado.py`, **de nombre estable**, que busca
la frase en los planes sellados y la coteja contra la seccion 6.
**MEDIDO EN ESTA VUELTA: 2 promesas, 2 CUMPLIDAS, 0 INCUMPLIDAS**
([`SALIDA_V63_PROMESAS_CUMPLIDAS.txt`](SALIDA_V63_PROMESAS_CUMPLIDAS.txt)). **Y la cuenta la puso el
instrumento, no yo: el primer borrador de este reporte decia TRES, y el instrumento midio DOS.**

**DOS `ROJO` PROPIOS, LOS DOS DE LA MISMA ESPECIE Y LOS DOS MIOS, van dictados con las dos mitades en
la seccion 7 y no escondidos aqui.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `630c6d19` (el commit del acta 62), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** (`git status --porcelain` VACIO, comprobado) |
| **hash final** | el commit de este reporte, **pusheado a `origin/pasada-unica`**, mas el que escribe esta celda, porque el commit del reporte no podia contener su propio hash |
| **commits de la vuelta** | **5** hasta aqui, leidos de `git log --format=%h 630c6d19..HEAD`: `8d3c34cc` (apertura medida), `0f7d2ef0` (TAREA 1 entera), `f5e9a72b` (`OP-M-03-I`), `e55252dc` (el primer `ROJO` propio del barrido), `0f692945` (`OP-M-02-PROG`), **mas el de este reporte y el que escribe esta celda** |
| **arbol al cierre** | limpio tras el commit del reporte |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1)

**NINGUNA CELDA ESTA TECLEADA:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 63`
([`SALIDA_V63_TALLAR_CABECERA.txt`](SALIDA_V63_TALLAR_CABECERA.txt)). **Las dos columnas se leen de
ficheros DISTINTOS.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.274 / 579 / 17.486 | **3.853 / 3.272 / 581 / 17.490** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 275 / 276 | **551 / 277 / 274** |
| actos (componentes) | 82 | **80** |
| actos `CERRADOS` / `ABIERTOS` | 29 / 53 | **27 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 67 / 240 | **63 / 240** |
| cola de costuras | 1.456 | **1.456** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 253 | **255** |
| duplicadas historicas: grupos / nodos | 928 / 735 | **927 / 734** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (307 igual a 307; 276 igual a 276) | **TODAS OK (303 igual a 303; 274 igual a 274)** |

**LA APERTURA CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 62 MIDIO POR CORRIDA PROPIA**, y eso es
contraste, no fuente: marcador, cola, duplicadas y estado dan **`diff` VACIO** y el recomputo difiere
en **UNA linea**, la de la ruta del `--salida`. **EL BARRIDO DIFIERE EN TRES FICHEROS BARRIDOS**
(390 contra 387) **y se dice por que: son los tres scripts propios que el auditor committeo con el
acta 62**; `ROJO`, `AMBAR`, `ROTULADO`, `CENSO` e `ILEGIBLE` salen identicos.

Instrumentos de apertura corridos **ANTES de la primera operacion y con el arbol limpio**:
[`SALIDA_V63_APERTURA.txt`](SALIDA_V63_APERTURA.txt),
[`SALIDA_V63_MARCADOR_APERTURA.txt`](SALIDA_V63_MARCADOR_APERTURA.txt),
[`SALIDA_V63_RECOMPUTO_APERTURA.txt`](SALIDA_V63_RECOMPUTO_APERTURA.txt),
[`SALIDA_V63_COLA_APERTURA.txt`](SALIDA_V63_COLA_APERTURA.txt),
[`SALIDA_V63_COLISIONES_APERTURA.txt`](SALIDA_V63_COLISIONES_APERTURA.txt),
[`SALIDA_V63_DUPLICADAS_APERTURA.txt`](SALIDA_V63_DUPLICADAS_APERTURA.txt) y
[`SALIDA_V63_BARRIDO_APERTURA.txt`](SALIDA_V63_BARRIDO_APERTURA.txt). **Las tres que reescriben sus
ficheros salieron IDEMPOTENTES**, verificado por `git status`, que no listo **ni un fichero rastreado
modificado**.

**LA MEDICION DE CIERRE SE RE-CORRIO DESPUES DE ESCRIBIR LOS REGISTROS**, por si aquellas escrituras
movian algo: el estado re-corrido da **`diff` VACIO** contra el publicado. **La cabecera de arriba es
la ULTIMA medicion, no una heredada.**

**LAS CELDAS QUE SE MUEVEN, TODAS EN 2 O EN 4, Y TODAS PREDICHAS POR LAS DOS FUSIONES:** vivos bajan
**2**, deprecados suben **2**, colapsos suben **2**, pares distintos bajan **2**, actos bajan **2**,
`CERRADOS` bajan **2**, nodos en `CERRADOS` bajan **4** y auto-pares suben **2**. **Los dos deltas de
deprecados se midieron por separado al ejecutar cada operacion** (`+1` sobre `+1` esperado, dos
veces).

**LAS TRES CELDAS QUE NO SE MUEVEN ASI, MEDIDAS Y NO SUPUESTAS:**

1. **LOS ENLACES SUBEN 4** (17.486 a 17.490). Cada superviviente hereda los vecinos del que muere por
   la simetrizacion del paso 5 de Gate 0, y la fusion dedupica por literal, asi que el saldo no es
   multiplo de nada. **Medido en las dos corridas:** `3` vistas completadas en `nodos_siguientes` y
   `2` en `nodos_previos` tras `OP-M-03-I`, y `1` en `nodos_siguientes` tras `OP-M-02-PROG`.
2. **LA COLA NO SE MUEVE** (1.456 a 1.456), aunque los dos supervivientes crecieron en pasos: **su
   cuenta nueva no los saca ni los mete en el corte**.
3. **LAS DUPLICADAS BAJAN 1 (928 a 927 grupos), Y EL DIFF ESTA CORRIDO POR INSTRUMENTO, NO A OJO.**
   **CERO grupos fabricados en los dos cortes** y **cero renombrados**. Detalle en la seccion 4.

**LOS `ABIERTOS` NO SE MUEVEN NI UN DIGITO: 53 sobre 240 en los dos lados.** Es lo que cabe esperar
de dos operaciones que solo tocan actos `CERRADOS`, **y es ademas la comprobacion que hace honesta la
apertura de `OP-U-02` de la seccion 3**.

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V63_MARCADOR_CIERRE.txt`](SALIDA_V63_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) | franquicias
10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0 (n 106) |
seguridad_digital 11,1 (n 27). **IDENTICA a la de la apertura al digito, y no es casualidad: fundir
no voltea veredictos.**

---

## 1. TAREA 1: **LOS REGISTROS, EL CENSO DE PLANTILLAS Y SU UNICO `TALLADO`**

### 1.1 Las adjudicaciones del acta 62, registradas donde el patron de la campana las pone

Van al final de [`docs/plan/03_FUSIONES.md`](../plan/03_FUSIONES.md), **adosadas y SIN reescribir una
sola linea de las secciones de arriba** (**+125 lineas, de 2.929 a 3.054**, contadas por el propio
instrumento). Es la via que esa pagina ya uso **tres** veces: acta 52 (linea **1250**), acta 57 sobre
el acto 25 (**2475**) y acta 61 (**2689**), **las tres cotejadas HOY abriendo el fichero**.

Van los **NUEVE discutibles `A FAVOR` con la vara citable de cada uno**, la respuesta de las
plantillas, la no comparabilidad de las perdidas, **la caida de reporte con sus SEIS sitios**, las dos
preguntas restantes y **el orden que manda sobre lo que viene**.

**LA GUARDA DE LAS CITAS NACE DE UN `ROJO` DE LA VUELTA PASADA, Y ESO ES LO QUE LA HACE UTIL.** Aquel
registro saco **cuatro** citas de linea malas a la primera y las arreglo despues.
`scripts/loop/_v63_registrar_acta62.py` **las coteja TODAS antes de escribir**, imprimiendo la linea
citada, y **cae en `ROJO` sin escribir si una sola no calza**: **21 citas al acta MAS 4 a la propia
pagina, TODAS `OK` a la primera**
([`SALIDA_V63_REGISTRO_ACTA62.txt`](SALIDA_V63_REGISTRO_ACTA62.txt)).

**UN DATO QUE EL ACTA NO PUBLICO Y LA MEDICION DE HOY ANADE, Y NO ME FAVORECE:** el instrumento
`_v63_sitios_promesa.py` mide **SIETE** promesas de marcado en los planes de la vuelta 62, no seis, y
**UNA SI SE CUMPLIO** (el acto 5, que llego al reporte como `D8`). **Las incumplidas siguen siendo
exactamente las seis que el acta nombra** (7, 9, 10, 12, 15 y 19). La cuenta del acta **no cambia**;
lo que cambia es que ahora se ve que **la promesa a veces si se honraba**, que es **peor y no mejor**
para el ejecutor de aquella vuelta: no era un giro de estilo que nadie cumplia, era **un compromiso
cumplido una vez de siete** ([`SALIDA_V63_SITIOS_PROMESA.txt`](SALIDA_V63_SITIOS_PROMESA.txt)).

### 1.2 **EL CENSO DE PLANTILLAS: UN SOLO `TALLADO` EN QUINCE, Y ERA EL GENERADOR DE PLANES**

Nace `scripts/loop/censo_de_plantillas_talladas.py`, **de nombre estable** (la vuelta entra solo para
rotular la salida). **Es MEDICION y no doctrina**, que es exactamente lo que el acta 62 pregunta 1
encargo.

**LA VARA ES DE INCLUSION Y NO DE EXCLUSION, Y EL MOTIVO ESTA MEDIDO, NO RAZONADO.** El primer
borrador buscaba digitos y descartaba citas: **dio ONCE `TALLADOS` de quince, casi todos citas**
(*tramo 3*, *acto 23*, *TABLA 2*, *guarda 1B*). **Una vara que marca a casi todo el mundo no separa a
nadie.** La vara final: un digito cuenta **solo si HACE DE CANTIDAD**, en cuatro formas medibles
(delante de un sustantivo de medida, detras de dos puntos, en pareja con otro, o con su unidad). **Lo
que no fija veredicto se publica igual**, en la lista DEBIL del paso 4.

| | |
|---|---:|
| `.py` en `scripts/loop` | **312** |
| excluidos por marca de corrida (`_`, `vuelta<N>`, `v<N>_`, `acta<N>`, `tramo<N>`, `lote<X>`) | **297** |
| **de nombre estable, censados** | **15** |
| **`TALLADO`** | **1** |
| `DECLARA FALTA` | 3 |
| `MEDIDO` | 11 |

**EL UNICO `TALLADO` ERA `generar_plan_del_lote.py`**, con **NUEVE cantidades talladas** en su
`CABECERA` constante: **21 actos**, **42 combinaciones**, **848 lineas** de dossier y **21 de 21**.
**Es de nombre estable y esta VIVO**: corrido sobre cualquier otro tramo habria **SELLADO un plan
cuya cabecera afirma cifras que no midio**. Es la misma especie que la vuelta 62 cazo en
`registrar_cierre_de_tramo.py`.

**LA CORRECCION, con el texto viejo citado ENTERO dentro del propio fichero:** la cabecera pasa de
`dict` constante a **funcion que se arma del insumo o DECLARA su falta**. `--operacion` pasa a
**REQUERIDO**; `--nomina`, `--dossier`, `--varas-impresas` y `--colisiones-esperadas` entran
opcionales **y su ausencia se declara dentro del plan sellado**; el cotejo del insumo contra los
nodos de hoy **se MIDE al sellar**, sobre el tramo entero. **LA ARITMETICA NO SE TOCA.**

**EL CASO POSITIVO ESTA CORRIDO, NO AFIRMADO, Y SU SEGUNDA PRUEBA ES LA QUE IMPORTA**
([`SALIDA_V63_CASO_POSITIVO_CABECERA.txt`](SALIDA_V63_CASO_POSITIVO_CABECERA.txt)):

| prueba | como se midio | que dio |
|---|---|---|
| **1, como estaba** | el modulo del commit `630c6d19`, extraido con `git show` | **21 actos, 42 combinaciones y 848 lineas, SIN correr sobre ningun tramo**: son valores de un `dict` de modulo |
| **2, como queda sobre el insumo VERDADERO** | la cabecera de hoy armada con `TRAMO6_V61.jsonl` | **21 actos y 42 combinaciones**, **LAS MISMAS QUE LOS PLANES SELLADOS DE LA VUELTA 62 LLEVAN**. *La correccion HONRA el conteo, no lo acomoda* |
| **3, como queda sobre un insumo DISTINTO** | la misma cabecera con un tramo de **tres** filas | **la de hoy dice TRES y la vieja sigue diciendo VEINTIUNO**. **Ahi es donde mentia** |
| **4, la falta** | sin los cuatro ficheros externos | **los cuatro bloques DECLARAN su ausencia** con todas las letras; y con el fichero puesto, **la cifra se mide** |

**EL CENSO RE-CORRIDO DESPUES DA CERO `TALLADOS`**
([`SALIDA_V63_CENSO_PLANTILLAS_TRAS_CORREGIR.txt`](SALIDA_V63_CENSO_PLANTILLAS_TRAS_CORREGIR.txt)).
**Y AL CIERRE SE RE-CORRIO OTRA VEZ, PORQUE ESTA VUELTA ANADIO CINCO INSTRUMENTOS DE NOMBRE ESTABLE Y
LA CIFRA DE ARRIBA YA NO ERA LA DEL ARBOL: `CERO TALLADOS` sobre VEINTE**
([`SALIDA_V63_CENSO_PLANTILLAS_CIERRE.txt`](SALIDA_V63_CENSO_PLANTILLAS_CIERRE.txt)). **Los cinco que
nacen hoy pasan su propio censo.**
**Y UNA DIFERENCIA DE UN DIGITO QUE VA DICHA EN VEZ DE CALLADA:** el bloque del dossier corregido
publica **849 lineas** y el texto viejo tallado decia **848**. **No es que uno mienta: son dos varas**
(`wc -l` cuenta lineas terminadas y da 848; el bloque parte por el salto de linea y da 849). **La
cifra publicada es la que el instrumento mide hoy, con su vara dicha.**

---

## 2. TAREA 2a: **LAS DOS FUSIONES DE MESA DEL PUESTO 1**

**EL ORDEN NO SE ELIGIO.** Sale de `03_FUSIONES.md` seccion **EL ORDEN DE ESTA FASE** (linea **62**,
cotejada hoy), cuya tabla de desbloqueos dejo medido el empate del puesto 1: `OP-U-01` con **2**,
`OP-M-03-I` con **1**, `OP-M-02-PROG` con **0**. **Lo aplica el acta 62, pregunta 5.**

### 2.1 **DOS INSTRUMENTOS NUEVOS, Y LOS DOS NACEN DE UNA AVERIA MEDIDA**

| instrumento | por que nace | como se construyo |
|---|---|---|
| **`generar_plan_de_fusion_de_mesa.py`** | el generador de lotes lee su insumo de un **fichero de tramo**, y una fusion de mesa no tiene tramo: su insumo es **LA FICHA** de `OPERACIONES.jsonl` | **IMPORTA** la maquina de guardas de `generar_plan_del_lote.py` en vez de copiarla, para que **el que sella un lote y el que sella una mesa no puedan discrepar en silencio** |
| **`fundir_por_plan.py`** | el ancestro `vuelta49_fundir_tramo.py` imprime **`OP-U-01, TRAMO %s`** con la operacion **TALLADA en el literal**: corrido sobre una fusion de mesa habria publicado `OP-U-01` en la cabecera de una operacion que no lo es | **sucesor declarado**, construido **POR EXTRACCION** con `_v63_construir_fundidor.py` (sha1 del ancestro **`8ea1020d074f`**, medido hoy), **un assert por cambio** e **IDEMPOTENTE** (re-corrido da `IDENTICO`). **Cinco rotulos de salida y nada mas: ni una linea de aritmetica** |

**EL ASSERT CAZO UN FALLO PROPIO EN LA PRIMERA CORRIDA Y SE DICE:** una de las agujas, sin anclar al
salto de linea, **mordia DOS veces**, y la segunda era **el texto viejo que el ancestro cita dentro
de un comentario**, que es justo lo que no se debe tocar. **El constructor cayo y no escribio nada**;
la aguja se anclo y quedo en una.

### 2.2 **`OP-M-03-I`: LA PUERTA DE METRICAS DE RIES**

`pivotar_o_perseverar` **absorbe** `decision_pivote_perseverar`. **7 piezas repartidas: 2 enteras, 2
de `INCISO` y 3 ya dichas. 3 perdidas selladas en campo.** El superviviente pasa de **5 a 6 pasos** y
de **2 a 3 condiciones**.

**LO QUE HACIA DELICADA ESTA FUSION, Y ESTA COMPROBADO Y NO AFIRMADO: EL BLOQUE DEL PUNTO
BRILLANTE.** La ficha lleva una **correccion declarada** del 19 ago 2026 (decision del fundador) que
dice que el bloque **NO esta en el que muere**, que **vive entero en su nodo propio
`puntos_brillantes_antes_del_pivote`**, que **NO se toca**, y que lo unico que esta fusion tiene que
hacer con el es **redirigir su arista al superviviente, con su espejo**.
[`SALIDA_V63_VERIFICAR_OPM03I.txt`](SALIDA_V63_VERIFICAR_OPM03I.txt) **mide las seis cosas, y las
seis salen en verde**:

| | lo medido |
|---|---|
| **las tres piezas propias del par** | *racionalizacion del fracaso* en el **paso 6**, *linea base nueva* en el **4**, *comprobacion posterior* en el **5** |
| **el bloque, byte a byte** | **5 pasos identicos** a los del arbol previo, **fuente `Traction` sola**, y **0 de 5** pasos del bloque en el que muere, tal como la correccion declarada predecia |
| **la arista, con su espejo** | ANTES el que muere lo nombraba en `nodos_siguientes` y el nodo propio a el en `nodos_previos`; **HOY el SUPERVIVIENTE lo nombra en `nodos_siguientes` y el nodo propio nombra al superviviente**, y **el id del muerto ya no aparece** |
| **el nodo propio** | **VIVO**, no deprecado |
| **el alias** | `ids_alias` y `merged_originals` cargan `decision_pivote_perseverar` |
| **el absorbido** | **deprecado** y con su texto y sus aristas **INTACTOS** |

### 2.3 **`OP-M-02-PROG`: EL PROGRAMA UNICO**

`ocho_fases_experiencia_cliente` **absorbe** `fases_de_retencion_de_clientes`. **5 piezas: 2 enteras
y 3 ya dichas. CERO `INCISOS`, y se dice por que en vez de callarlo: LOS CUATRO PASOS DEL
SUPERVIVIENTE CIERRAN EN PUNTO**, uno a uno, asi que ningun inciso se adosa limpio y **la guarda de
la juntura lo habria puesto en `ROJO`**. **1 perdida sellada.** El superviviente pasa de **4 a 5
pasos** y de **1 a 2 condiciones**.

[`SALIDA_V63_VERIFICAR_OPM02PROG.txt`](SALIDA_V63_VERIFICAR_OPM02PROG.txt), **las seis en verde**:
las **dos prioridades `Affirm` y `Activate`** en el paso 5; las dos piezas propias del que muere
viajadas; **las dos que la ficha reclasifica como QUE VIVEN DENTRO intactas y en el mismo sitio**
(pasos 3 y 4, antes y despues); alias y `merged_originals`; el absorbido deprecado con su texto
intacto; **y la duplicada medida EN EL TESTIGO**: `pensamiento_h2h` nombraba a los dos miembros y
**hoy nombra al superviviente UNA sola vez y al muerto CERO**, sin auto-arista.

### 2.4 **LA LISTA DE VERIFICACION DEL ENCARGO, ENTERA Y CON SU SALIDA**

| guarda | `OP-M-03-I` | `OP-M-02-PROG` |
|---|---|---|
| **`P.5`, el acto leido entero antes de fundir** | los **tres** nodos leidos enteros (los dos del par mas el nodo propio) | los **dos** nodos leidos enteros |
| **`P.16` por el resolutor, ANTES de fundir** | **NINGUNA** | **NINGUNA** (ver el aviso de abajo) |
| **simulacion previa sobre copia, cotejada contra la sellada** | **5** entradas (la sellada decia 4) | **3** entradas, **IDENTICO al digito** a la sellada, con los tres nombres calzando |
| **guarda `1B`, ningun absorbido es puerta** | `OK` | `OK` |
| **cobertura exacta de indices** | `OK` | `OK` |
| **guarda 3, cero repetidos literales** | `OK` | `OK` |
| **alias cargando el id que muere** | `OK` | `OK` |
| **`P.16` medida ANTES de limpiar** | **0** duplicadas, **0** auto-aristas | **1** duplicada, **1** auto-arista, **las dos impresas antes de retirarse** |
| **guardas A y B (cero nuevas tras resolver)** | `OK (0)` y `OK (0)` | `OK (0)` y `OK (0)` |
| **guarda C, los cinco campos que no se redactan** | **5 de 5** intactos | **5 de 5** intactos |
| **guarda D, el absorbido intacto** | `OK` | `OK` |
| **delta de deprecados** | **`+1` sobre `+1`** esperado | **`+1` sobre `+1`** esperado |
| **re-anclar entre la fusion y `run_phase1`** | *nada que re-anclar* | *nada que re-anclar* |
| **Gate 0** | `OK`, ciclo de tres entero | `OK`, ciclo de tres entero |
| **motor** | **25/25** | **25/25** |
| **web** | **80 ficheros, 1.030 pasadas, 3 saltadas** | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| **`tsc`** | **CERO lineas** | **CERO lineas** |
| **censo de colisiones** | esperadas **0**, medidas **0**, **`CALZA: SI`** | esperadas **0**, medidas **0**, **`CALZA: SI`** |
| **`diff` de duplicadas por instrumento** | 928 a 927 grupos, **CERO fabricados, CERO renombrados**, y **el grupo que desaparece nombrado** | 927 a 927, **CERO fabricados, CERO renombrados, CERO desaparecidos** |

**EL CICLO DE TRES VA DICHO ENTERO PORQUE `run_phase1` SOLO NO BASTA, Y ESTO SE MIDIO:** tras la
primera corrida de Gate 0, **Gate 0 dio `OK` con su chequeo de gemelos en 0 y la suite del motor cayo
con 73 nodos divergentes**. **No es una contradiccion y el propio codigo lo tiene escrito:** el
chequeo de Gate 0 compara **el snapshot de ANTES del paso 6**, porque recompilar borra la curaduria
de etiquetas, que vive en `dataset/metadata` y no en los nodos. **El remedio esta escrito ahi mismo y
EN ESE ORDEN**, y es el que se corrio las dos veces: `etiquetas_de_cara.py --aplicar` (**71
etiquetas**) y despues `sync_assets_web.py` (**6 assets mas el manifest**). **Motor 25/25 despues.**

### 2.5 **LOS DOS CASOS POSITIVOS, Y POR QUE HACIAN FALTA LOS DOS**

| | sujeto | resultado |
|---|---|---|
| **el heredado** (`vuelta57_caso_positivo.py`) | el **acto 37 del tramo 3**, que esta vuelta no toca | **LAS SEIS GUARDAS MUERDEN** ([`SALIDA_V63_CASO_POSITIVO_HEREDADO.txt`](SALIDA_V63_CASO_POSITIVO_HEREDADO.txt)) |
| **el nuevo** (`_v63_caso_positivo_mesa.py`) | **`OP-M-03-II`**, la fusion de mesa siguiente de la misma mesa, **que esta vuelta NO ejecuta** | **LAS NUEVE MUERDEN** ([`SALIDA_V63_CASO_POSITIVO_MESA.txt`](SALIDA_V63_CASO_POSITIVO_MESA.txt)) |

**EL HEREDADO NO BASTABA, Y ESO ES MEDIBLE: pone a fallar las guardas del ANCESTRO
(`vuelta49_fundir_tramo.py`), no las de los dos instrumentos que nacen hoy.** Las nueve mentiras del
nuevo aislan una guarda cada una: superviviente y absorbido que **la ficha no escribe**, cobertura
por **olvido** y por **sobrante**, `INCISO` no verbatim, **perdida de especie desconocida**, nodo
**ya deprecado**, **semilla de entrada**, y la novena que no es mentira sino **la mitad positiva de
la correccion del titulo**: un plan sin campo `operacion` imprime **`SIN OPERACION DECLARADA EN EL
PLAN`** en vez de suponer `OP-U-01`. **Re-corrido tras la segunda fusion: las nueve siguen mordiendo.**

### 2.6 **LOS REGISTROS, TALLADOS Y NO TECLEADOS**

Nace `scripts/loop/registrar_fusion_de_mesa.py`, **de nombre estable**, hermano de
`registrar_cierre_de_tramo.py`: **talla cada celda del plan sellado y de la salida de la ejecucion**.
**+104 lineas** para `OP-M-03-I` y **+98** para `OP-M-02-PROG`, **adosadas sin reescribir una linea de
arriba**.

**DOS BUGS PROPIOS DEL REGISTRADOR, CAZADOS EN `--simular` Y ARREGLADOS ANTES DE ESCRIBIR NADA:** una
**barra vertical dentro de una celda** partia la tabla en dos columnas de mas, y **las filas de
condiciones publicaban *paso n* donde el ejecutor lee *condicion n***. **El segundo es el que
importa: publicaba un destino FALSO**, y lo cazo mirar la salida de la simulacion en vez de darla por
buena.

---

## 3. TAREA 2b: **LA APERTURA MEDIDA DE `OP-U-02`, SIN FUNDIR NI UN ACTO**

**NI UN ACTO SUYO SE FUNDE EN ESTA VUELTA.** Nace `scripts/loop/abrir_universo_de_opu02.py`, **de
nombre estable**, **de solo lectura sobre el dataset**, que escribe **UN** fichero: la nomina.

**EL INSUMO ES EL RECOMPUTO CORRIDO EN ESTA MISMA VUELTA**
([`_v63_componentes_cierre.jsonl`](_v63_componentes_cierre.jsonl)), medido **DESPUES** de las dos
fusiones, **no un fichero sellado viejo**. **Y por `P.1` el instrumento RESUELVE POR ALIAS ANTES DE
CONTAR**, o contaria como libre un acto cuyo miembro ya fue absorbido.

| | |
|---|---:|
| **actos abiertos, medidos hoy** | **53** sobre **240** nodos |
| **`OP-U-02` ABRE** (criterio del propio plan: sin dueno en mesa ni destejido) | **47** actos sobre **201** nodos |
| **quedan FUERA, con dueno en otra fase** | **6** actos sobre **39** nodos |
| **criterio ANCHO** (el *aviso de trampa*: toca CUALQUIER nomina) | **9** tocan alguna, **44** no tocan ninguna |
| **la nomina, FIJADA** | [`NOMINA_OPU02_V63.jsonl`](NOMINA_OPU02_V63.jsonl), **53 filas, una por acto, con sus miembros** |

**LOS SEIS QUE QUEDAN FUERA, CADA UNO CON SU DUENO NOMBRADO:** el de **13** (`OP-M-01` y su hija), el
de **9** (`OP-M-05-INDICE` y `OP-M-05-EDIFICIO`), el de **7** (`OP-M-05-APERTURA`), el de **4** de la
junta asesora (`OP-M-04`), el de **3** de la voz del cliente (`OP-D-02`) y el de **3** del pivote
(`OP-M-03-III`). **Los seis con sus miembros impresos** en
[`SALIDA_V63_APERTURA_OPU02.txt`](SALIDA_V63_APERTURA_OPU02.txt).

### 3.1 **LA FRASE DE LA LINEA 226 ESTA ENVEJECIDA, Y LO MEDIDO RECONCILIA LAS DOS VERSIONES**

**`03_FUSIONES.md` lineas 226 a 228 (leidas hoy y cotejadas por el instrumento antes de escribir)
dicen CUATRO exclusiones. La ficha de `OP-U-02` en `OPERACIONES.jsonl` ya lo habia corregido en la
vuelta 13 y dice OCHO.** **Lo medido hoy no elige entre las dos: las reconcilia.**

- **SEIS de los ocho siguen ABIERTOS y quedan fuera por su dueno**, y son exactamente los seis de
  arriba.
- **LOS DOS DE DESTEJIDO (`OP-D-03` y `OP-D-04`) YA NO SON ACTOS: no aparecen en NINGUNA componente
  del recomputo de hoy, ni abierta ni cerrada.**

**Y LA DESAPARICION DE ESOS DOS NO SE SUPONE: SE MIDE, Y LAS DOS CAUSAS SON DISTINTAS**
([`SALIDA_V63_DESTEJIDOS_COMPROBADOS.txt`](SALIDA_V63_DESTEJIDOS_COMPROBADOS.txt)):

| | lo medido | la causa |
|---|---|---|
| **`OP-D-04`** | sus **7** nodos resuelven HOY a **2** supervivientes, los dos vivos | **la componente se consumio POR FUSION** |
| **`OP-D-03`** | sus **6** nodos siguen **VIVOS** y **ninguno resuelve a otro** | **lo que desaparecio no son los nodos: son LAS ARISTAS `A`**. Los **8** pares internos que el archivo tiene entre ellos son **8 de clase `D`**, y una componente de este recomputo se forma **solo con aristas `A`** |

**UNA CIFRA MAS QUE CAMBIO Y VA DICHA:** la ficha de la vuelta 13 llamaba **de tamano 4** al acto de
la voz del cliente; **hoy mide 3**. **Es un acto que encogio, no una cuenta mal hecha.**

**NO HAY PARADA: la nomina se fijo SIN DECIDIR NADA.** El criterio es el que **el propio plan
escribe** (dueno en mesa o destejido), no uno nuevo; **el instrumento no elige superviviente, no
reparte piezas y no declara ningun acto.** **La fusion de esos 47 actos es trabajo de la vuelta que
la ejecute.**

---

## 4. LAS DUPLICADAS Y LAS COLISIONES, POR INSTRUMENTO

**EL `diff` NO SE HACE A OJO:** `scripts/loop/diff_duplicadas_por_resolutor.py` resuelve **nodo y
destino por la cadena de alias de hoy** antes de comparar, que es lo que separa **las fabricadas de
verdad de las renombradas**.

| corte | grupos antes | grupos despues | **fabricados** | renombrados | desaparecen |
|---|---:|---:|---:|---:|---:|
| **`OP-M-03-I`** | 928 | 927 | **0** | 0 | **1**, nombrado: `pivotar_o_perseverar / nodos_siguientes / catalogo_pivotes` |
| **`OP-M-02-PROG`** | 927 | 927 | **0** | 0 | 0 |

**UNA COSA QUE PARECE UNA DISCREPANCIA ENTRE DOS INSTRUMENTOS Y NO LO ES, dicha porque leerla mal
cuesta una vuelta:** en `OP-M-02-PROG`, `simular_fusion.py` reporta **UNA duplicada nueva** y
`retirar_duplicada_por_resolutor.py` (el instrumento de `P.16` que corre ANTES de fundir) reporta
**NINGUNA**. **No se contradicen: el segundo declara en su propio docstring que SALTA A PROPOSITO el
caso que el ejecutor de fusiones deduplica solo**, y persigue solo las que llegan por una cadena de
alias y sobrevivirian. **Esta trae los dos ids literalmente**, asi que el ejecutor **la conto, la
imprimio y la limpio en el sitio**, que es lo que `P.16` exige.

---

## 5. LO QUE ESTA VUELTA NO HIZO, DICHO CON NOMBRE

- **NO se fundio ni un acto de `OP-U-02`.** Solo se midio su apertura.
- **NO se toco la mesa.** Sigue en **QUINCE actos** mas la serie del titulo con tres ejemplares, y
  este encargo no la tocaba.
- **NO se renumero ninguna operacion** ni se movio el campo `orden`.
- **NO se reescribio ni una linea de las secciones de arriba de `03_FUSIONES.md`.** Los tres
  registros de esta vuelta van **adosados** (+125, +104, +98 y +47 lineas, contadas por sus
  instrumentos), y **la frase envejecida de la linea 226 queda entera con su contraste al lado en vez
  de corregida en el sitio**.
- **NO se decidio nada del fundador.** El merge de `pasada-unica` sigue siendo suyo.

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**LOS DOS SITIOS DE LOS PLANES DE ESTA VUELTA QUE PROMETEN MARCADO ESTAN AQUI, y van senalados con
`(PROMETIDO EN EL PLAN)` para que la promesa se pueda cotejar por maquina:** el **motivo** de
`OP-M-03-I` (el `CHOCAN`, aqui el `D4`) y la **nota** de `OP-M-02-PROG` (la perdida de mas, aqui el
`D7`). **`comprobar_promesas_de_marcado.py` las mide y las da CUMPLIDAS las dos.**

**UNA CORRECCION DECLARADA SOBRE ESTE MISMO REPORTE, y el texto viejo va delante:** su primer
borrador decia *los TRES sitios* y contaba tambien el motivo de `OP-M-02-PROG`. **El instrumento midio
DOS**: aquel motivo declara la divergencia de cableado pero **no dice la frase que promete marcado**.
**La cifra publicada es la del instrumento, y la mia era de memoria.** El `D6` sigue en la tabla por
su propio peso; lo que se retira es la etiqueta de prometido.

| | que hice | por que se puede discutir |
|---|---|---|
| **`D1`** | **HICE CRECER OTRA VEZ UNA GUARDA en un instrumento estable**: `generar_plan_del_lote.py` pasa a exigir `--operacion` y a declarar la falta de cuatro insumos | Es la figura que el acta 61 (`D2`) adjudico **con dos condiciones**, y las dos se cumplen (enumerada en el docstring, marcada aqui). Pero **es la segunda vuelta seguida que uso esa adjudicacion**, y **`--operacion` REQUERIDO rompe la invocacion documentada del ancestro**: quien corra el comando viejo se lo encuentra en `ROJO` |
| **`D2`** | **CORREGI, OTRA VEZ EL MISMO DIA, un instrumento que sella los planes de la campana** | Es el `D2` de la vuelta 62 repetido. Lo sostengo porque **la prueba 2 del caso positivo mide que la cabecera corregida da las MISMAS cifras que los planes ya sellados**; pero **quien mida el riesgo dira que tocar el sellador dos vueltas seguidas es exactamente como se pierde un sello** |
| **`D3`** | **ESCRIBI DOS INSTRUMENTOS NUEVOS DE NOMBRE ESTABLE EN LA MISMA VUELTA EN QUE LOS USE** (`generar_plan_de_fusion_de_mesa.py` y `fundir_por_plan.py`) | El segundo es **sucesor declarado y extraido con assert**, y hay caso positivo propio; pero **un instrumento estrenado y usado el mismo dia no tiene mas historia que su propia corrida**, y la campana venia de seis tramos con un fundidor rodado |
| **`D4` (PROMETIDO EN EL PLAN)** | **EJECUTE `OP-M-03-I` con la ficha diciendo *CABLEADO A CONTENIDO EMPATADO* cuando el contenido de HOY no empata**: pasos 5 contra 4 al superviviente y condiciones 2 contra 3 al que muere, o sea **`CHOCAN`** | En un `CHOCAN` decide **la pieza declarada** (acta 53, pregunta 3), que aqui es **la propia adjudicacion sellada** y nombra al mismo nodo: **las dos vias convergen**. Pero **la ficha adjudico por una vara que hoy no se sostiene medida**, y un lector estricto dira que **una adjudicacion cuya premisa envejecio se re-adjudica, no se ejecuta** |
| **`D5`** | **SEGUI `P.16` CONTRA LA LETRA EXPLICITA DE LA FICHA Y DEL ENCARGO**, que dicen que la duplicada de `OP-M-02-PROG` *queda para `OP-S-12`* | `P.16` es **posterior** a la ficha (14 contra 12 de ago), es **decision del fundador**, su punto 3 convierte a `OP-S-12` en **verificacion de cero**, `AUDITOR.md` seccion 3 pide **cero duplicadas tras resolver** como guarda de la fase III, y **es el carril con el que se ejecutaron los seis tramos**. Pero **el encargo de esta vuelta lo dice con todas sus letras**, y **no obedecer una linea del encargo es discutible aunque la doctrina te de la razon** |
| **`D6`** | **EJECUTE LAS DOS FUSIONES CON SUS SIMULACIONES SELLADAS DESCUADRADAS**: `OP-M-03-I` daba 4 entradas y hoy da **5**, con cableado **6 contra 5** en vez de 6 contra 4; `OP-M-02-PROG` medía 13 contra 3 y hoy **12 contra 3** | Las tres diferencias estan **medidas y explicadas** (un nodo nacido dos dias despues de la simulacion; cinco nodos hoy deprecados) y **ninguna cambia el superviviente**. Pero **una simulacion sellada que ya no reproduce lo que sella es una simulacion vieja**, y quien sea estricto dira que **se re-sella la ficha antes de ejecutarla, no se ejecuta con una nota al pie** |
| **`D7` (PROMETIDO EN EL PLAN)** | **SELLE UNA PERDIDA QUE LA FICHA DE `OP-M-02-PROG` NIEGA**: la ficha dice *LA UNICA PERDIDA REAL DE ESTA FUSION ES PRIORIZAR AFFIRM Y ACTIVATE*, y esa **viaja**, asi que por su letra la fusion cerraria con **CERO** perdidas | Medido contra el texto de hoy, el parentesis *no solo para Assess y Admit* **no esta en ningun paso del superviviente**, y **la pasada `P.13` de aquella ficha es del 12 ago y ANTERIOR al contrato `CAMPO PROPIO v1`**. Pero **estoy contradiciendo una afirmacion sellada del plan con una lectura mia**, y quien lea estrecho dira que **eso es re-abrir una ficha cerrada** |
| **`D8`** | **MARQUE `CUBIERTO` con perdida sellada en el paso 1 de `decision_pivote_perseverar`** por el calificativo *accionables* | Es el carril del `D9` de la vuelta 62. Pero **la mitigacion que doy es de GRAFO, no de texto** (*`metricas_accionables` es nodo previo del superviviente*), y **un concepto a un salto no esta en el nodo**: quien sea estricto dira que **o es perdida sin atenuante o no es perdida** |
| **`D9`** | **ESCRIBI LA VARA DEL CENSO DE PLANTILLAS Y DESPUES LA CAMBIE**, al ver que la primera daba once `TALLADOS` de quince | Lo digo entero en el docstring y publico **la lista DEBIL** para que no se pierda nada. Pero **cambiar la vara despues de ver su resultado es exactamente como se fabrica una vara que da lo que uno queria**, y la unica defensa que tengo es que **la vara nueva es mas estrecha, no mas ancha** |
| **`D10`** | **DECIDI POR MI CUENTA QUE LA CONDICION 1 DE `fases_de_retencion_de_clientes` NO PIERDE NADA** y la marque `CUBIERTO` sin sellar perdida | El disparador operativo (*despues de la venta*) esta en el texto del superviviente con todas sus letras. Pero **el que muere nombra el sintoma concreto** (*solo hay procesos para atraer y cerrar ventas*) **y el superviviente nombra la necesidad**, y **no declarar es la mitad que no se puede auditar** |

---

## 7. MIS PROPIOS ROJOS Y TROPIEZOS, declarados con las dos mitades

**LOS DOS `ROJO` PROPIOS DEL BARRIDO SON DE LA MISMA ESPECIE, Y QUE SEAN DOS ES LO QUE HAY QUE
DECIR:** puse un `ROTULO` **por precaucion, antes de correr el barrido**, en dos ficheros cuyo titulo
**no disparaba ningun `AMBAR`**. El barrido los llama **`ROTULO HUERFANO`** y los pone en `ROJO` **a
proposito**, para que un rotulo no se quede de adorno cuando no cubre nada.

| | cayo asi | quedo asi |
|---|---|---|
| **1** | tras `OP-M-03-I` el barrido subio de `ROJO` **32** a **33**: `_v63_verificar_opm03i.py` con un `SELLO_FIJO` huerfano | retirado; **barrido re-corrido: `ROJO` 32**, y el verificador **re-corrido sigue dando las seis en verde**. Va en su propio commit (`e55252dc`) **sin reescribir el anterior** |
| **2** | al cerrar, el barrido volvio a subir a **33**: `_v63_registrar_opu02.py` con un `PROCEDENCIA` huerfano, **la misma especie otra vez** | retirado; **barrido de cierre: `ROJO` 32, `AMBAR` 0, `ROTULADO` 35, `CENSO` 218, `ILEGIBLE` 1** |

**LA LECCION QUE ME LLEVO, dicha para que se pueda cotejar la vuelta que viene: un rotulo se pone
DESPUES de que el barrido pida uno, nunca antes.**

**UN `AMBAR` PROPIO, ESE SI LEGITIMO Y ROTULADO:** el titulo de `_v63_registrar_acta62.py` nombra la
**vuelta 62** y el fichero es de la **63**. Es **`PROCEDENCIA` de verdad** (transcribe el acta de la
62), lleva su fuente y su literal de prueba, **y el barrido lo coteja por maquina en cada corrida**.

**DOS BUGS PROPIOS DEL REGISTRADOR DE MESA, cazados en `--simular`:** la barra vertical que partia la
tabla y **las filas de condiciones publicando *paso n* en vez de *condicion n***, que es **un destino
falso**. Los dos arreglados **antes de escribir en la pagina**.

**UN FALLO PROPIO DEL CONSTRUCTOR DEL FUNDIDOR, cazado por su propio assert:** una aguja sin anclar
al salto de linea mordia **dos** veces, y la segunda era el texto viejo citado en un comentario del
ancestro. **Cayo y no escribio nada.**

**UN TROPIEZO DE HERRAMIENTA, sin cifra de por medio:** mi primera corrida de la suite del motor uso
`npx vitest` desde `engine/`, que no es su corredor; el corredor es `python engine/run_all_tests.py`,
que es lo que el guardian de commit usa.

---

## 8. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Todo lo de esta vuelta se ejecuto con reglas ya escritas: `P.1`, `P.5`, `P.8`,
`P.16`, acta 53 pregunta 3 y 4, acta 54 preguntas 1 y 3, acta 55 pregunta 5, acta 58 pregunta 4, acta
61 `D2`, acta 62 preguntas 1, 3 y 5, y el orden adjudicado en la vuelta 47.

---

## 9. PREGUNTAS PARA EL AUDITOR

1. **`D4` y `D6` juntos: cuando una ficha sellada se EJECUTA con nota al pie y cuando se RE-SELLA
   antes de ejecutarla?** Las dos fusiones de hoy llegaron con su simulacion descuadrada y, en
   `OP-M-03-I`, con **la vara de la adjudicacion tambien descuadrada**. Ejecute las dos porque **el
   superviviente no cambia por ninguna via** y porque el encargo decia *tal como esta escrita*. **No
   hay regla escrita para el caso**, y quedan **doce fusiones de mesa mas** con fichas del 12 ago.
2. **`D5`: el encargo repite la letra de una ficha que una doctrina posterior contradice. Quien
   manda?** Segui `P.16` y `AUDITOR.md` seccion 3. **Si la respuesta es que manda el encargo, la
   operacion habria que rehacerla**, y prefiero preguntarlo que darlo por bueno.
3. **`D7`: puede un plan sellar una perdida que su propia ficha niega?** La ficha dice cero y yo
   selle una. **Mi vara fue el texto de hoy contra el contrato `CAMPO PROPIO v1`; la ficha es
   anterior al contrato.**
4. **El censo de plantillas dio `DECLARA FALTA` en cuatro ficheros y `MEDIDO` en once, y la
   diferencia entre esas dos etiquetas es floja**: hoy basta con que el fichero traiga un literal que
   nombre un insumo ausente, aunque sea un mensaje de error. **Las dos significan cero cifras
   talladas.** Merece la pena afinar la vara, o basta con decir esto?
5. **La apertura de `OP-U-02` deja 47 actos sobre 201 nodos, y el mayor es de 15.** El universo de
   `OP-U-01` se repartio en tramos con tope de cincuenta. **Vale el mismo instrumento de tramos aqui,
   o los abiertos piden otra forma?** No lo decido: lo traigo.

---

## 10. LOS DISCUTIBLES DE LA VUELTA ANTERIOR, PARA LA RELECTURA CIEGA

Los nueve del acta 62 quedaron **`A FAVOR`** y **registrados en `03_FUSIONES.md`** (seccion 1.1). **No
se re-abren aqui.**
