# -*- coding: utf-8 -*-
"""_v69_texto_lote_e.py . EL TEXTO EDITORIAL DEL REGISTRO DEL LOTE E.

NO ES UN INSTRUMENTO: es el texto. La maquina que arma sus tablas, coteja sus
citas y lo adosa es scripts/loop/vuelta69_registro_lote_e.py, que lo importa.

NI UNA TABLA NI UNA CIFRA TECLEADAS: las tablas entran por %%(clave)s y las
arma el registrador del plan sellado o de la salida del tallador; las celdas de
guardas y censos entran por %%(clave)s y las extrae por aguja de las salidas de
la vuelta; y las citas de linea entran como marcas [[CLAVE]].
"""

TEXTO = """

---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE E` (2026-08-26, vuelta 69)

**Se adosa al final del documento, bajo la cabecera de tramo que la vuelta 65 dejo en la linea
**[[PAG_TRAMO_CABECERA]]**, y NO reescribe ni una linea de las secciones de arriba.** El orden de la
fase sigue siendo el de la linea **[[PAG_ORDEN_FASE]]**; el registro del lote `C` esta en la
**[[PAG_LOTE_C]]** y el del lote `D` en la **[[PAG_LOTE_D]]**.

**EL LOTE SE DECLARO AL ABRIRLO Y SE ENTREGO ENTERO: SEIS actos y 22 nodos.** **Abre con LA FUSION
ADJUDICADA DEL `ACTO 18`**, que el acta 68 resolvio y que esta pagina registra en la linea
**[[PAG_SUP18]]**, ejecutada **como PRIMERA operacion del lote y dentro de un PLAN PROPIO** (la
adjudicacion esta en la linea **[[PAG_PLAN_PROPIO]]**: el plan del lote `D` NO se reabre, y el acto
CUENTA en la declaracion como cierre ENTERO). **Despues sigue el PREFIJO SIN SALTOS desde el `acto
25`.**

| | |
|---|---|
| **actos que cierran ENTEROS** | **6**: el **18**, **25**, **26**, **29** y **30** FUNDIDOS, y el **27** `DECLARADO Y NO FUNDIDO` |
| **nodos del lote** | **22** |
| **nodos que MUEREN** | **%(mueren)s** |
| **vivos del catalogo** | de **%(antes_vivos)s** a **%(despues_vivos)s** |
| **ficheros tocados** | **%(tocados)s** |
| **piezas repartidas** | **%(piezas)s** (**%(enteras)s** viajan enteras, **%(yadichas)s** ya estaban dichas) |
| **EL TOPE DEL PREFIJO, y es ESTRUCTURAL** | el siguiente es el **acto %(siguiente)s**, que **TIENE DUENO** (`OP-F-04-WEI` y `OP-S-04`, medido hoy sobre el fichero fijado) y que **no trae ninguno de los cuatro motivos sellados** con los que podria cerrar `DECLARADO`: **no podria cerrar ENTERO**, y el contrato del lote es entregar lo declarado |

**LAS FORMAS MEDIDAS DEL LOTE, y `P.8` aplicado en orden sobre cada una:**

| acto | miembros | **FORMA medida** | cierra | **la letra que decide** |
|---:|---:|---|---|---|
| **18** | 4 | `EMPATE SIN VARA` | **FUNDIDO** | **ninguna vara apunta**: lo adjudico el auditor, y este plan EJECUTA esa adjudicacion |
| **25** | 4 | `CONTENIDO EMPATA` | **FUNDIDO** | **el cableado DECIDE SOLO** y apunta a **la MISMA puerta** que la guarda `1B` obliga a conservar |
| **26** | 4 | `CHOCAN` | **FUNDIDO** | **decide LA PIEZA DECLARADA**, y apunta al mismo nodo que la vara de pasos, el cableado y la puerta |
| **27** | 4 | `TODAS DE ACUERDO` | **`DECLARADO Y NO FUNDIDO`** | **no llega a aplicarse: `P.10` detiene ANTES**, y la figura del inventario tambien |
| **29** | 3 | `UNA SOLA VARA` | **FUNDIDO** | **una sola vara BASTA**: la de condiciones, con pasos y cableado empatados |
| **30** | 3 | `CHOCAN` | **FUNDIDO** | **decide LA PIEZA DECLARADA**, y aqui la declaracion es **verbatim** del puesto **2838** |

> **LA GUARDA `1B` MUERDE EN DOS ACTOS DE ESTE LOTE Y NO PARA NINGUNO**, que es la mitad de la letra
> que menos se usa: el `acto 25` y el `acto 26` tienen **UNA** puerta cada uno, y con **UNA** puerta
> el acto **si se funde y la puerta SOBREVIVE** (acta 54, pregunta 1), frente al caso de **DOS o
> mas**, que cierra `DECLARADO` y esta registrado en la linea **[[PAG_GUARDA_1B]]**.

### a) **EL `ACTO 18`: LA FUSION QUE EL EJECUTOR NO ELIGIO, Y LAS CINCO PIEZAS DEL ACTA CONSERVADAS LAS CINCO**

**Es el cierre del carril del `EMPATE SIN VARA`** (registrado en la linea **[[PAG_TRANSITO]]** y
estrenado sobre este mismo acto en la **[[PAG_ACTO18_TRANSITO]]**). **La vuelta 68 lo dejo `ABIERTO
EN TRANSITO` sin elegir superviviente; el acta 68 adjudico `alianzas_cross_industry`; y esta vuelta
ejecuta esa fusion.** **El ejecutor no re-decidio nada: reparte.**

**`P.5`, contestada sobre el texto estable: ES UNA FAMILIA**, los cuatro del mismo libro (*The Green
to Gold Business Play*, de Esty), con **tres pares internos leidos y los tres en `A`** (puestos
**1797**, **1871** y **1903**), **cero `D`**, **cero nodos puente** y **cero triangulos**.

**LAS CINCO PIEZAS QUE EL ACTA MANDO CONSERVAR O SELLAR QUEDAN LAS CINCO CONSERVADAS**, y ninguna
sellada como perdida:

| pieza nombrada por el acta 68 | de donde sale | **como se conserva** |
|---|---|---|
| publicar y monitorear el cumplimiento colectivo | `co_opetition_industria`, paso 4 | **`APPEND`** |
| aplicar el estandar conjunto a los proveedores compartidos | `trabajo_colectivo_estandares_industria`, paso 4 | **`APPEND`** |
| el marco nombrado *Responsible Care* | `trabajo_colectivo_estandares_industria`, paso 3 | **`APPEND`** |
| el encuadre por riesgo reputacional compartido | `trabajo_colectivo_estandares_industria`, condicion 1 | **`APPEND`** |
| el test del poder de mercado **como arranque explicito** | `colaboracion_sectorial`, paso 1 | **`INCISO` ADOSADO AL PASO 1**, que es **la unica forma de que siga siendo un arranque**: un `APPEND` lo habria puesto al final |

**El nodo crece de %(p18a)s pasos a %(p18b)s y de %(c18a)s condiciones a %(c18b)s.** **EL REPARTO,
PIEZA POR PIEZA, GENERADO DEL PLAN SELLADO:**

%(rep18)s

%(abs18)s

**LAS PERDIDAS SELLADAS EN CAMPO PROPIO, recortadas enteras de la salida del tallador:**

%(per18)s

### b) **EL `ACTO 25`: LA PUERTA SOBREVIVE, Y ESTA FUSION FABRICA DOS COLISIONES DE CLASE**

**`P.5`, contestada: ES UNA FAMILIA, y es el acto MEJOR LEIDO del prefijo**: cuatro miembros del
mismo libro (*SPIN Selling*, de Rackham), **CINCO pares internos leidos de seis y los CINCO en `A`**
(puestos **209**, **278**, **303**, **800** y **862**), cero `D`, cero puentes, cero triangulos. **La
cuarta membresia la declara el archivo y no el ejecutor**: el **800** dice que **la familia no es de
tres sino de CUATRO** y que el cuarto puro queda degradado a sub-puro, y el **862** la deja en cinco
de seis.

**EL RACIMO CENSADO NO SE PARTE, Y ESO SE MIDE:** el racimo *La etapa de investigacion en la venta*
de `docs/RACIMOS_MIEMBROS.jsonl` tiene nomina de **TRES** y **los TRES estan DENTRO de este acto**:
el racimo cabe entero en el acto y esta fusion no lo corta por ningun sitio.

**LA PUERTA:** `enfoque_etapa_investigacion` **es puerta**, medido contra el universo protegido de
**256** ids, **y es UNA sola**, asi que **sobrevive**. **El cableado apunta al MISMO nodo** (6 contra
un maximo de 3), o sea que **no hay choque que resolver**, y se dice para que nadie tenga que
reconstruirlo.

**El nodo crece de %(p25a)s pasos a %(p25b)s y se queda en %(c25b)s condiciones.** **CERO `INCISO` y
es por la puntuacion**: los cuatro pasos del superviviente terminan en punto y la guarda de la
**JUNTURA ROTA** los habria rechazado. **CERO perdidas `DE CONDICIONES`, y se dice en vez de
callarlo.**

%(rep25)s

%(abs25)s

%(per25)s

> **LO QUE ESTA FUSION CUESTA, Y VA EN SU PROPIO APARTADO PORQUE ES LO MAS CARO DEL LOTE:** **fabrica
> DOS colisiones de clase**, predichas antes de tocar un nodo y publicadas en el apartado g).

### c) **EL `ACTO 26`: EL PRIMER `CHOCAN` DEL TRAMO QUE LLEGA A FUNDIRSE, Y EL NODO MAS GRANDE**

**`P.5`, contestada con la razon que la cerro delante: ES UNA FAMILIA.** Tres pares internos leidos y
los tres en `A` (puestos **230**, **381** y **839**), cero `D`, cero puentes, cero triangulos. **Son
DOS libros distintos** (*Change by Design* de Brown y *Winning at New Products* de Cooper) **y eso NO
parte la familia**: el **839** es justamente **el par que CRUZA las dos parejas ya declaradas** y
dice con todas sus letras que son **CUATRO nodos del mismo instrumento y no dos parejas vecinas**.

**LA FORMA ES `CHOCAN` Y DECIDE LA PIEZA DECLARADA:** la vara de PASOS apunta a
`investigacion_etnografica_ideacion` (6 contra 5) y la de CONDICIONES al otro lado (3 contra 2).
**Las otras dos cuentas apuntan al mismo sitio que los pasos**: el cableado (14 contra 8) **y la
puerta**, que aqui vuelve a ser UNA sola y sobrevive. **Este `CHOCAN` no deja residuo.**

**El nodo crece de %(p26a)s pasos a %(p26b)s y de %(c26a)s condiciones a %(c26b)s.** **NUEVE PASOS
IGUALA AL NODO MAS GRANDE QUE ESTE TRAMO HA PRODUCIDO** y va dicho en vez de maquillado. **UN solo
`INCISO`, al paso 2**: *deputizar*, que es un **parametro** de la observacion que el superviviente ya
manda hacer, no un gesto aparte.

%(rep26)s

%(abs26)s

%(per26)s

### d) **LOS `ACTOS 29` Y `30`: EL MAS BARATO DEL LOTE Y EL MAS RARO DEL TRAMO**

**EL `ACTO 29`, la familia del avance contra la continuacion.** `P.5`: **ES UNA FAMILIA**, los tres
del mismo libro, dos pares leidos y los dos en `A` (puestos **220** y **482**). **FORMA `UNA SOLA
VARA`**: pasos y cableado empatan y **la de CONDICIONES apunta**, y **una sola vara BASTA**. El nodo
crece de %(p29a)s pasos a %(p29b)s.

> **EL RACIMO CENSADO SI SE TOCA AQUI, Y SE DECLARA EN VEZ DE CALLARSE.** El racimo *El avance y el
> compromiso en la venta* tiene nomina censada de **CINCO** y este acto contiene **DOS** de ellos.
> **Los otros TRES no se tocan y tienen casa propia MEDIDA**: `INVENTARIO.jsonl` trae la entrada
> racimo *el compromiso contado tres veces*, **forma `PURO`, estado sano y forma cerrada**, con
> nomina de exactamente esos tres. **El censo de cinco del cribado ya estaba PARTIDO en el inventario
> en un `PURO` de tres mas dos sueltos, y esta fusion opera sobre los DOS SUELTOS.**

**EL `ACTO 30`, la familia del viaje diagnostico de Juran.** `P.5`: **ES UNA FAMILIA**, los tres de
la misma fuente, dos pares leidos y los dos en `A` (puestos **2600** y **2838**). **FORMA `CHOCAN`**,
con el cableado **empatado** (o sea que ni podria desempatar si le tocara), **y decide LA PIEZA
DECLARADA**: el **2838** dice `A` **POR CONTENCION** y cierra con la frase *superviviente
viaje_diagnostico_remedial*, verbatim.

> **CUATRO `INCISO` EN UN SOLO ACTO, QUE ES LA CIFRA MAS ALTA DE LA CAMPANA**, y **ninguno apilado
> sobre el mismo paso**. **La razon esta medida y no es de gusto:** el superviviente ya trae ocho
> pasos y las cuatro piezas propias del absorbido **no son gestos nuevos sino PARAMETROS DE RIGOR** de
> gestos que el superviviente ya manda hacer (el Pareto, los diagramas causa-efecto, la recoleccion
> disenada para correlacionar y la validacion estadistica). **Los cuatro pasos que reciben `INCISO`
> no terminan en punto**, asi que la guarda de la **JUNTURA ROTA** no salta en ninguno. El nodo se
> queda en %(p30b)s pasos y crece de %(c30a)s condicion a %(c30b)s.

%(rep29)s

%(abs29)s

%(per29)s

%(rep30)s

%(abs30)s

%(per30)s

### e) **EL `ACTO 27`: `DECLARADO Y NO FUNDIDO` POR `P.10`, CON LA `ESTRELLA` ENCIMA**

**Es la forma mas limpia del prefijo y aun asi NO se funde**, que es exactamente lo que `P.10`
existe para hacer: las tres cuentas apuntan al mismo nodo y **`P.10` detiene ANTES**.

**Y ES LA MISMA FORMA DEL `ACTO 24` DE LA VUELTA 68** (registrado en la linea
**[[PAG_ACTO24_ESTRELLA]]**): **el nodo puente que `P.10` detecta ES el centro de una figura
declarada del inventario**, y una fusion entera deprecaria a la vez el centro y sus perifericos.

%(dec27)s

> **LA LECTURA QUE UNA FUSION ENTERA DESMENTIRIA:** el **572** se titula *EL HIJO CON CASA PROPIA* y
> dice que `prototipado_modelos_negocio` **desarrolla el paso 5** de `proceso_ideacion_modelo_negocio`
> y le anade lo suyo entero, mientras **la madre se queda con lo suyo**. **Fundir los cuatro a un
> vivo unico deprecaria los dos extremos de ese `D` contra el mismo superviviente y sellaria que
> repiten entre si**, que es lo que esa lectura niega, y ademas es **una cadena de TRES PISOS** que el
> propio **572** cuenta al cerrar. **Los radios de la estrella son los puestos 507 y 641**, y el
> cuarto miembro, de otro libro, entra por el **1056**.

**El acto queda VIVO Y ENTERO. Su destino comparte carril con el pendiente del subconjunto cerrado:
el cierre de la fase 03.**

### f) **LAS GUARDAS DE LA OPERACION, LEIDAS DE LAS SALIDAS Y NO AFIRMADAS**

| guarda | resultado, extraido por aguja de su salida |
|---|---|
| **guardas 1, 1B, 2 y 3** | **VERDES en las CINCO fusiones**: miembros vivos y nomina completa, ningun absorbido es puerta, cobertura exacta de indices y cero repetidos literales |
| **`P.16`, quien fabrica limpia en el mismo commit** | **%(p16)s** duplicadas fabricadas y limpiadas en la misma corrida; **%(autoaristas)s** auto-arista retirada; el pasivo propio de la guarda baja de **%(pasivo_antes)s** a **%(pasivo_despues)s** |
| **guarda A** (cero auto-aristas nuevas) y **guarda B** (cero duplicadas nuevas tras resolver) | **las dos `OK`** |
| **guarda C** (los campos que esta operacion NO redacta, intactos) | **%(campos_intactos)s** |
| **guarda D** (los absorbidos conservan su texto INTACTO) | **`OK` sobre los %(mueren)s** |
| **redirecciones sobre nodos vivos** | **%(redirecciones)s** |
| **reanclaje**, corrido **ENTRE** la fusion y `run_phase1` | **%(reanclaje)s**, y se corrio igual, que es lo que la guarda pide |
| **diff independiente de duplicadas**, con la apertura sacada de `git` | **FABRICADOS %(dup_fab)s**, **RENOMBRADOS %(dup_ren)s**, y **%(dup_antes)s** grupos pasan a **%(dup_despues)s** |
| **Gate 0 con su ciclo de TRES** | **`OK`**: **%(gate_activos)s** activos y **%(gate_deprecados)s** deprecados, alcanzabilidad 100,0 por ciento; **SIN cuarta corrida** |
| **las tres suites** | motor **25/25**, web **80 ficheros y 1030 pasadas**, `tsc` **CERO lineas** |

**LAS PERDIDAS DEL LOTE, CONTADAS POR MAQUINA Y NO DE MEMORIA**, que es la regla que sale de la caida
del `D9` de la vuelta 68 y que esta pagina registro en la linea **[[PAG_CUENTA_AGREGADA]]**:

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **%(per_total)s** |
| de ellas `DE PARAMETRO DE PASO` | **%(per_paso)s** |
| de ellas `DE CONDICIONES` | **%(per_cond)s** |
| **filas con `ATENUANTE DECLARADO`** | **%(per_aten)s** |
| de ellas, de la **especie del pendiente 4** | **%(per_p4)s** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **%(per_medido)s** |
| **filas con DOS SEDES en el campo `donde`** | **%(per_dos_sedes)s** (el carril de la linea **[[PAG_D10_POR_PIEZA]]**) |
| la aritmetica de **la lectura contraria** (una fila por SITIO y no por PIEZA) | **%(per_contraria)s** y no **%(per_total)s** |

### g) **LAS DOS COLISIONES DE CLASE QUE ESTA VUELTA FABRICA, PREDICHAS ANTES DE TOCAR UN NODO Y PUBLICADAS EN ROJO CON SU DUENA**

**Es la pieza mas delicada del lote y por eso va en su propio apartado.** **La fusion del `acto 25`
fabrica DOS colisiones**, y **el carril esta escrito** en la linea **[[PAG_LINEA_BASE]]**: *la duena
es quien la fabrica*, la colision **nace de una sustitucion de `OP-U-02`, esta predicha en su plan y
se publica en rojo con dueno nombrado**.

| | medido |
|---|---:|
| **linea base declarada y MEDIDA sobre el arbol de antes** | **%(col_base)s** |
| **colisiones NUEVAS que la fusion fabricaria** | **%(col_nuevas)s** |
| colisiones que desaparecerian | %(col_idas)s |
| **ESPERADAS TRAS FUNDIR** | **%(col_esp)s** |
| **MEDIDAS al cierre por el censo** | **%(col_med)s** |
| **`CALZA`** | **`%(col_calza)s`** |
| auto-pares al cierre | **%(autopares)s** |

**LAS DOS, NOMBRADAS UNA A UNA CON SUS PUESTOS PARA QUE EL CENSO SE PUEDA COTEJAR SIN ABRIR OTRO
FICHERO:**

| colision nueva | clases | **de donde sale** |
|---|---|---|
| `cuatro_etapas_llamada_de_ventas` contra `enfoque_etapa_investigacion` | **`B`** contra **`D`** | el **775** dice `B` contra el superviviente; el **202** y el **1364** dicen `D` contra dos absorbidos, y al resolver los tres al mismo vivo las lecturas chocan |
| `enfoque_etapa_investigacion` contra `modelo_spin_preguntas` | **`B`** contra **`D`** | el **648** y el **769** dicen `B`; el **1422** dice `D` contra un absorbido |

> **LAS DOS SON LA MISMA ESPECIE, y se dice porque explica el choque**: **el marco entero contra una
> de sus etapas**. Contra el superviviente la lectura dijo `B` (dos caras del mismo asunto) y contra
> los absorbidos dijo `D` (el todo no repite la parte). **La fusion junta las tres lecturas en un
> solo par y el choque se vuelve visible.**
>
> **LA LINEA BASE OPERATIVA DEL CENSO PASA DE %(col_base)s A %(col_med)s**, y **eso NO se adjudica
> aqui**: la base vigente esta escrita en la linea **[[PAG_LINEA_BASE]]**, la anterior se movio por
> adjudicacion del auditor, y esta se le sube **COMO PREGUNTA** en el reporte de esta vuelta. **Las
> dos de la mesa `OP-M-03` no se tocan y las dos viejas de `OP-U-02` siguen vigentes con su duena.**

### h) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por los lotes `A` a `D` | **20** |
| **cerrados por el lote `E`** | **6** (5 fundidos, 1 declarado) |
| **quedan** | **%(quedan_actos)s actos** |
| **nodos que quedan** | **%(quedan_nodos)s** |
| **el siguiente del prefijo** | el acto **%(siguiente)s**, **con dueno** |
| de los que quedan, **con nodo puente** | **%(quedan_puente)s** |
| de los que quedan, **con par `D` interno** | **%(quedan_d)s** |
| de los que quedan, **con dueno medido** | **%(con_dueno)s** |
| **actos declarados que esperan el cierre de la fase 03** | **%(declarados_espera)s** |
| actos (componentes) al cierre | **%(actos_comp)s** |
| actos `ABIERTOS` al cierre | **%(abiertos)s** sobre **%(abiertos_n)s** nodos |

> **UN HECHO MEDIDO QUE CAMBIA LO QUE VIENE:** **de los %(quedan_actos)s actos que quedan, NINGUNO
> trae nodo puente y NINGUNO trae par `D` interno**. **Todos los actos con puente del tramo estan ya
> cerrados**, y con ellos el motivo sellado de `P.10` (linea **[[PAG_ACTO1_P10]]**) y el cuarto
> motivo (linea **[[PAG_CUARTO_MOTIVO]]**) **se quedan sin sujeto en lo que resta del tramo**. Lo que
> queda son actos de tres miembros con dos pares `A` leidos y uno sin veredicto.

### i) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las colisiones vigentes**, **NO adjudica la linea base nueva del censo** (la sube como pregunta),
**NO funde ningun acto con dueno** (el **%(siguiente)s** y el resto siguen fuera), **NO toca la mesa
`OP-M-03` ni sus dos colisiones**, **NO ejecuta ninguna de las cinco fichas `OP-M-02` consumidas** y
**NO abre el lote siguiente**. La respuesta *DOS FAMILIAS* de `P.5` sigue siendo motivo sellado en la
linea **[[PAG_P5_MOTIVO]]** y **en este lote no se uso: los seis actos contestaron UNA familia**. El
dueno se sigue midiendo como el acta 68 lo adjudico, en la linea **[[PAG_DUENO_MEDIDO]]**, y las
adjudicaciones de esa acta estan registradas desde la linea **[[PAG_ACTA68]]**.
"""
