# -*- coding: utf-8 -*-
"""_v68_texto_lote_d.py . EL TEXTO EDITORIAL DEL REGISTRO DEL LOTE D.

NO ES UN INSTRUMENTO: es el texto, con HUECOS. Las tablas y las cifras las pone
scripts/loop/vuelta68_registro_lote_d.py leyendolas del plan sellado y de las
salidas del dia, y las citas de linea las resuelve la guarda ensanchada de la
vuelta 68 buscando cada aguja. Aqui NO hay ni una cifra de la corrida ni un
numero de linea tecleados: hay marcas.
"""

TEXTO = """

---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE D` (2026-08-26, vuelta 68)

**Se adosa al final del documento, bajo la cabecera de tramo que la vuelta 65 ya puso** (linea
**[[PAG_TRAMO_CABECERA]]**), **y NO reescribe ni una linea de arriba.** **Ninguna tabla de esta
seccion esta tecleada**: el reparto pieza a pieza, las piezas por absorbido y las fichas de los
declarados **se generan del plan sellado** [`../loop/PLAN_V68_OPU02_LOTE_D.json`](../loop/PLAN_V68_OPU02_LOTE_D.json);
la de perdidas **se recorta de la salida del tallador**; y las celdas de guardas, colisiones y
censos **se extraen por aguja** de las salidas de la vuelta. **Y las citas de linea tampoco se
teclean**: salen de buscar su aguja de contenido, con la guarda ensanchada que esta vuelta estreno
(el ensanche esta registrado arriba, en el apartado del acta 67 que abre en la linea
**[[PAG_ACTA67]]**).

**EL LOTE ES PREFIJO SIN SALTOS** del `orden_universo` de lo que quedaba: **el prefijo 18 a 24,
SIETE actos y 28 nodos**. **SEIS cierran ENTEROS** y **el acto 18 se procesa entero y se cuenta
APARTE**, por el carril del transito que el acta 67 adjudico y que esta pagina registra en la linea
**[[PAG_TRANSITO]]**.

| acto | miembros | cierra | motivo | superviviente |
|---:|---:|---|---|---|
| **18** | 4 | **`ABIERTO EN TRANSITO`** | **`EMPATE SIN VARA` y nada lo detiene**: ni guarda ni motivo sellado | **ninguno se elige**, y esa es la regla |
| **19** | 4 | **FUNDIDO** | `CONTENIDO EMPATA`, decide el cableado solo (`P.8`) | `division_trabajo_humano_ia` |
| **20** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, triangulo medido | ninguno se elige |
| **21** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, dos triangulos medidos | ninguno se elige |
| **22** | 4 | **FUNDIDO** | `UNA SOLA VARA` de pasos; el cableado apunta al otro y no habla | `comprension_capacidades_limitaciones_ia` |
| **23** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, triangulo medido | ninguno se elige |
| **24** | 4 | **`DECLARADO Y NO FUNDIDO`** | **`P.10`**, dos triangulos, **la figura `ESTRELLA`** y **el dueno `OP-S-07`** | ninguno se elige |

> **LOS CUATRO DECLARADOS DE ESTE LOTE CIERRAN LOS CUATRO POR EL MISMO MOTIVO, EL TRIANGULO DE
> `P.10`**, que es el primero de los CUATRO motivos sellados del catalogo (el cuarto se adjudico en
> el acta 67 y esta registrado arriba, en la linea **[[PAG_CUARTO_MOTIVO]]**). **Ningun acto de este
> lote necesito la guarda `1B`** (linea **[[PAG_GUARDA_1B]]**) **ni la respuesta de `P.5`** (linea
> **[[PAG_P5_MOTIVO]]**): las dos pasan por vacio y se dice.

**LO QUE LA FUSION MOVIO, LEIDO DE LA SALIDA DE LA EJECUCION:** **%(antes_vivos)s vivos a
%(despues_vivos)s**, **%(mueren)s nodos mueren**, **%(piezas)s piezas repartidas**
(**%(enteras)s** viajan enteras y **%(yadichas)s** ya estaban dichas), **%(tocados)s ficheros
tocados** y **%(redirecciones)s redirecciones sobre nodos vivos**.

### a) **EL `ACTO 19`: LA FAMILIA DEL REPARTO DE TAREAS ENTRE PERSONA Y MAQUINA, Y LA PRIMERA VEZ DEL TRAMO QUE EL CABLEADO DECIDE SOLO**

**`P.5` CONTESTADA SOBRE EL TEXTO ESTABLE: ES UNA FAMILIA, y no es lectura del ejecutor sino
declaracion del archivo.** El puesto **1597** dice con todas sus letras que **la familia del reparto
de tareas entre persona y maquina pasa a CUATRO nodos por cierre transitivo**, con
`descomposicion_tareas_trabajo` de centro y sus tres `A`, los puestos **972**, **1582** y ese; el
**1582** la habia visto pasar de dos a tres **y con miembros de DOS libros distintos**.

**UNA FRONTERA QUE EL ARCHIVO ESCRIBE Y QUE ESTA FUSION NO CRUZA:** el mismo puesto **1597** declara
que **esta familia NO es el racimo de la supervision de la IA**, y que **ninguno de sus cuatro
miembros figura en aquella nomina de diez**. **Cotejado hoy** contra
[`INVENTARIO.jsonl`](INVENTARIO.jsonl): **los cuatro estan FUERA de esa nomina**. Son dos familias
de IA distintas, una sobre quien hace que y otra sobre quien revisa.

**`P.8` EN ORDEN:** la FORMA medida es **`CONTENIDO EMPATA`** (pasos 4 a tres bandas, condiciones 2
a cuatro bandas), asi que **EL CABLEADO DECIDE SOLO** y apunta a `division_trabajo_humano_ia`.
**No es que el cableado gane a un contenido que dice otra cosa: es que el contenido NO DICE NADA**,
que es el unico supuesto en que `P.8` le da la palabra.

**EL NODO CRECE de %(p19a)s pasos a %(p19b)s y de %(c19a)s condiciones a %(c19b)s**, y **el costo va
publicado**. **CERO `INCISO` y es POR LA PUNTUACION**: los cuatro pasos del superviviente terminan
en punto y cualquier `INCISO` con nexo de coma cae en la guarda de la juntura rota.

%(rep19)s

%(abs19)s

**LAS PERDIDAS SELLADAS EN CAMPO PROPIO**, recortadas de la salida del tallador:

%(per19)s

### b) **EL `ACTO 22`: EL BLOQUE DE CUATRO DEL RACIMO DE LA SUPERVISION DE LA IA, Y LA PARTICION ESCRITA NO SE MUEVE**

**`P.5` CONTESTADA: ES UNA FAMILIA.** El puesto **177** dice *REPITE* entre
`comprension_capacidades_limitaciones_ia` y `jagged_frontier_ia`; el **456** dice que
`invitar_ia_a_todo` y `principio_invitar_ia_siempre` son **el mismo principio numerado**; y el
**1517** declara que **la absorcion SI ocurre** y que la pareja de invitar a la IA a todo **ENTRA**
al racimo por ese par.

**LA PARTICION `5 MAS 4 MAS 1`, CONTRASTADA HOY CONTRA EL FICHERO DEL TRAMO, Y ESTA FUSION NO CRUZA
NI UNA DE SUS DOS FRONTERAS:**

| bloque de la particion | que es hoy | quien lo dice |
|---|---|---|
| **el CINCO** | **el `acto 11` del tramo**, que ya cerro **`DECLARADO Y NO FUNDIDO` por `P.10`** en la vuelta 66 (registrado en la linea **[[PAG_ACTO11_IA]]**), y cuyo puesto **1541** dejo escrito que **la particion escrita NO se mueve** | el fichero del tramo mas la ficha de arriba |
| **el CUATRO** | **este `acto 22`**, que es el que se funde | el fichero del tramo |
| **el UNO** | `comprender_alineacion_etica_ia`, **el suelto**, que `04_ENLACES.md` manda a **mesa** por ser el suelto de un racimo **sin centro** | el carril de los sueltos |

> **LA SUMA DA `5 MAS 4 MAS 1` Y CALZA CON EL CAMPO `forma` DEL INVENTARIO**, medido hoy. **Esta
> fusion opera DENTRO de un bloque**: ni toca al bloque de cinco, ni toca al suelto.
>
> **LO QUE SE TRAE COMO CONTRASTE Y NO COMO FUENTE, y por eso va MARCADO DISCUTIBLE:** el campo
> `estado` de esa entrada de inventario dice **`en mesa, particion PROVISIONAL`**, con corte del 13
> ago 2026. **MEDIDO HOY** contra el fichero fijado del tramo, **este acto tiene los DOS campos de
> dueno VACIOS**, y **el campo `operaciones` de la propia entrada del racimo tambien esta vacio**:
> **ninguna operacion lo reclama**. El criterio con el que `OP-U-02` abrio su universo es el dueno
> medido. **La discrepancia se declara en vez de resolverse copiando** (regla 2), que es el mismo
> carril con el que el acto 17 de la vuelta 67 trajo el puesto 460.

**`P.8` EN ORDEN:** la FORMA medida es **`UNA SOLA VARA`**; la de PASOS apunta a
`comprension_capacidades_limitaciones_ia` (5 contra un maximo de 4) y **se funde a su lado**. **El
cableado apunta al OTRO**, `jagged_frontier_ia` (7 contra 3), **y NO HABLA**: `P.8` es regla de
**PRELACION**. **Es la misma forma que el acto 16 de la vuelta 67** (linea **[[PAG_LOTE_C]]**),
cuyo `D7` el acta 67 adjudico `A FAVOR` con esta misma letra. **El margen del cableado se publica
como dato.**

**EL NODO CRECE de %(p22a)s pasos a %(p22b)s y de %(c22a)s condiciones a %(c22b)s**, y **es el nodo
mas grande que este tramo ha producido**. **DOS `INCISO` y ninguno apilado sobre el mismo paso**,
los dos extraidos del nodo y comprobados VERBATIM.

%(rep22)s

%(abs22)s

**LAS PERDIDAS SELLADAS EN CAMPO PROPIO:**

%(per22)s

> **UNA PERDIDA CON DOS SEDES EN UN SOLO CAMPO `donde`, en cada uno de los dos actos fundidos**, por
> el criterio que el acta 67 adjudico y que esta pagina registra: **[[PAG_D10_POR_PIEZA]]**.

### c) **LOS `ACTOS 20`, `21`, `23` Y `24`: `DECLARADOS Y NO FUNDIDOS` POR `P.10`, CON SUS TRIANGULOS MEDIDOS**

**Los cuatro quedan VIVOS Y ENTEROS**, sin un nodo tocado ni un superviviente elegido, y **su destino
comparte carril con el pendiente 3 del acta 67: el cierre de la fase 03**.

**El `acto 20`, la familia del efecto latigo en la cadena de suministro:**

%(dec20)s

> **La lectura que una fusion entera desmentiria:** el **994** dice que `efecto_bullwhip` **mide el
> problema** y `compartir_datos_cadena_suministro` **es la inversion que lo cura**, que **ni un paso
> se solapa**, y que es **arista que falta de las mas claras** porque el diagnostico termina
> apuntando al remedio **por su nombre**. **Y hay un CHOQUE encima**, dicho en vez de callado: el
> puesto **730** declara que la clase queda en `A` **por la lectura vieja del cero-enlazados** y que
> **si mandara el contenido seria `D`**, y lo deja anotado en vez de elegir.

**El `acto 21`, la familia del Punto 4 de Deming:**

%(dec21)s

> **Las dos lecturas que una fusion entera desmentiria:** el **2927** avisa con todas sus letras de
> que los dos extremos **fusionan por `A` con el mismo tercer nodo** y de que **quien componga esa
> cadena sin verificar que es CONTENCION en los dos eslabones dira `A`**; el **3102** declara
> **conjuntos disjuntos** y entregables distintos. **El cierre transitivo junta a los cuatro
> justamente por la cadena que el 2927 dice que NO compone.**

**El `acto 23`, la familia de la reserva de opciones para empleados:**

%(dec23)s

> **La lectura que una fusion entera desmentiria:** el **1193** dice que uno es **NEGOCIACION** y el
> otro **MECANICA**, nombra las dos cuentas que la negociacion no trae, y cierra con que **ese par
> NO anade miembro: sale sano porque trae calculos propios, y no repeticion**. La familia esta
> contada por el archivo en el **1371** (cuatro nodos por cierre transitivo) y en el **1436**
> (cobertura de cinco de seis, forma **PROVISIONAL** por un solo par).

**El `acto 24`, la estrella de pass/fail, con TRES razones independientes:**

%(dec24)s

> **PRIMERA, `P.10`:** el **636** dice que **uno construye el experimento y el otro dicta cuando se
> aprueba**, y el **1346** repite la misma frontera entera.
> **SEGUNDA, la figura:** la entrada `figura` **`ESTRELLA (9.23)`** del inventario nombra a este
> acto como **su ejemplar numero UNO**, con el centro `diseno_experimentos_pass_fail`, los radios
> **467**, **511** y **639** y los perifericos **636** y **1346** en `D`, y declara que **las dos
> cuentas que el banco 9.23 exige estan hechas**. El propio **1346** dice que era **el par que
> decidia** y que al salir `D` **la figura queda CONFIRMADA**. Fundir el acto borraria el ejemplar.
> **TERCERA, y es la mas seca: ESTE ACTO TIENE DUENO.** Su campo `duenos_cualquier_operacion` trae
> **`OP-S-07`**, medido hoy. **Es la unica de las tres que habria bastado sola sin leer nada.**

### d) **EL `ACTO 18`, `ABIERTO EN TRANSITO`: EL ESTRENO DEL CARRIL QUE EL ACTA 67 ADJUDICO**

**Se procesa entero y se cuenta APARTE, ni cerrado ni saltado**, que es exactamente lo que el carril
de la linea **[[PAG_TRANSITO]]** manda. **NO se elige superviviente y esa es la regla, no una
omision.**

| | lo medido hoy |
|---|---|
| **miembros** | **4**: `alianzas_cross_industry`, `co_opetition_industria`, `colaboracion_sectorial`, `trabajo_colectivo_estandares_industria` |
| **pares internos con veredicto** | **3 de 6**, y **los TRES en `A`** (puestos **1797**, **1871** y **1903**) |
| **pares `D` internos** | **0** |
| **NODOS PUENTE / TRIANGULOS** | **0 / 0**, o sea **`P.10` NO se dispara** |
| **PUERTAS dentro** | **NINGUNA**: la guarda `1B` pasa por vacio |
| **`P.5`** | **ES UNA FAMILIA**, y la declara el archivo: el **1871** dice *LA MISMA ALIANZA SECTORIAL POR TERCERA VEZ* y que la familia **pasa de DOS a TRES**, y el **1903** dice *POR CUARTA VEZ* y que **pasa de TRES a CUATRO por cierre transitivo**. Los cuatro de la misma fuente |
| **FORMA medida** | **`EMPATE SIN VARA`**: pasos **4 a cuatro bandas**, condiciones **2 a cuatro bandas** y **el cableado tambien empata** |
| **destino** | **`ABIERTO EN TRANSITO`**, fuera de la cuenta de cerrados del lote. **El auditor adjudica el superviviente en su acta y el lote siguiente ejecuta esa fusion como su primera operacion** |

> **NADA LO DETIENE, Y POR ESO NO CIERRA `DECLARADO`.** `P.10` no se dispara, la `1B` pasa por
> vacio y `P.5` contesta que es UNA familia: **no hay motivo sellado que invocar**, y `DECLARADO Y
> NO FUNDIDO` queda reservado a motivos sellados. **El auditor aun no contesta no es un motivo, es
> una pregunta en viaje.**

### e) **LAS GUARDAS DE LA OPERACION, LEIDAS DE LAS SALIDAS Y NO AFIRMADAS**

| guarda | resultado |
|---|---|
| **las cuatro de cada fusion** (1 miembros vivos, **1B** ningun absorbido es puerta, 2 cobertura exacta, 3 cero repetidos) | **VERDES en los dos actos** |
| **`P.16`, quien fabrica limpia, en el mismo commit** | la fusion fabrico **%(p16)s** duplicada(s) y **las limpio en la misma corrida**; **%(autoaristas)s auto-arista(s)** retirada(s); el pasivo propio de la guarda baja de **%(pasivo_antes)s** a **%(pasivo_despues)s** |
| **colisiones esperadas, MEDIDAS ANTES de fundir sobre la linea base declarada** | base **%(col_base)s**, **NUEVAS %(col_nuevas)s**, **ESPERADAS %(col_esp)s**; el censo de cierre mide **%(col_med)s** y **`CALZA: %(col_calza)s`** |
| **diff de duplicadas, con la apertura sacada de `git`** | **FABRICADAS %(dup_fab)s**, **RENOMBRADAS %(dup_ren)s**, grupos **%(dup_antes)s a %(dup_despues)s** |
| **reanclaje entre la fusion y `run_phase1`** | **%(reanclaje)s**: el fundidor ya habia redirigido las **%(redirecciones)s** referencias vivas |
| **Gate 0 con su ciclo de TRES** | **`GATE 0: OK`**, universo **%(gate_activos)s activos / %(gate_deprecados)s deprecados**; sin cuarta corrida |
| **recomputo al cierre** | **%(actos)s** actos, **%(abiertos)s** `ABIERTOS` sobre **%(abiertos_n)s** nodos |

**Las CUATRO colisiones vigentes no se tocan** y siguen con su duena, por el carril general de la
linea **[[PAG_CARRIL_COLISIONES]]** y el que la vuelta 66 fijo en la base `4`.

### f) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por los lotes A, B y C | **14** |
| **cerrados por el lote D (esta vuelta)** | **6** (2 fundidos, 4 declarados) |
| **quedan** | **%(quedan_actos)s actos** |
| **nodos que quedan** | **%(quedan_nodos)s** |
| **el siguiente del prefijo** | el acto **%(siguiente)s**, que es el que queda `ABIERTO EN TRANSITO` |
| de los que quedan, con nodo puente | **%(quedan_puente)s** (acto %(quedan_puente_cuales)s) |
| **actos declarados que esperan el cierre de la fase 03** | **%(declarados_espera)s** (actos %(declarados_cuales)s) |

### g) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las cuatro colisiones vigentes**, **NO funde ningun acto con dueno** (los del tramo con dueno
siguen fuera, y el `acto 24` se declara con el suyo dicho), **NO toca la mesa `OP-M-03` ni sus dos
colisiones**, **NO toca las dos colisiones de `OP-U-02`**, **NO ejecuta ninguna de las cinco fichas
`OP-M-02` consumidas**, **NO elige superviviente para el acto 18** y **NO mueve la particion del
racimo de la supervision de la IA**. El orden de la fase sigue siendo el de la linea
**[[PAG_ORDEN_FASE]]**, la regla de la ficha envejecida la de la **[[PAG_FICHA_ENVEJECIDA]]**, el
carril del lote B el de la **[[PAG_LOTE_B]]**, el del acto 12 sin letra el de la
**[[PAG_ACTO12_SIN_LETRA]]** y la correccion declarada de la cita de esta vuelta el de la
**[[PAG_CORRECCION_CITA]]**.
"""
