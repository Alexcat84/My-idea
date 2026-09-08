### TAREA 1. LOS REGISTROS, Y LOS DOS CAMPOS `estado` QUE EL ACTA 209 DEJO ADJUDICADOS

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN con
`scripts/loop/_v211_t1_seccion.py` de `docs/loop/SALIDA_V211_T1B_CERRAR_DOS_ESTADOS.txt`,
`docs/loop/SALIDA_V211_T1B_CERRAR_DOS_ESTADOS_MUTADO.txt`,
`docs/loop/SALIDA_V211_T1E_GRUPO_HOROWITZ.txt`,
`docs/loop/SALIDA_V211_T1E_GRUPO_HOROWITZ_MUTADO.txt` y
`docs/loop/SALIDA_V211_APERTURA.txt`, **y ese compositor cae en rojo si no puede leer
una sola de ellas**. Las lineas de acta que se citan aqui las **busca el propio
compositor en `docs/loop/ACTA_AUDITOR.md`** y caen en rojo si el texto no vive en
exactamente una linea: **se leen, no se recuerdan** (`6.6` del acta 210, linea **74203**).

#### 1.a. EL ACTA 210, LEIDA Y NO REESCRITA

La seccion de la **210** abre en la linea **73924** de `docs/loop/ACTA_AUDITOR.md`,
que mi apertura mide en **4902898** bytes en disco y **4902898** normalizado
a LF, `sha256` **`7217a5d76c98d65f`** (4788.0 KB). **Calza al digito con el encargo**,
que publica **4902898** y **`7217a5d76c98d65f`**.

#### 1.b. LOS DOS CAMPOS `estado`, EN EL MISMO COMPUTO Y CON LAS TRES GUARDAS

Las dos adjudicaciones que lo mandan viven en el acta **209**: la **`6.4`** en la linea
**73760** (*"`OP-L-02` SE CIERRA. 18 DE 18"*) y la **`6.5`** en la **73765**
(*"`OP-L-03` LLEVA UNA VUELTA CERRADA POR ACTA Y SU `estado` SIGUE EN `LISTA`"*). Las
tres guardas son las que esa misma acta nombra en su linea **73763**: *"el pase se
ejecuta con las mismas tres guardas del `2.c` de esta vuelta, que salieron limpias"*.

**EL CASO ROJO SE PROBO POR MUTACION ANTES DE ESCRIBIR NADA** (`EJECUTOR.md` 1). Con el
nombre de la segunda ficha cambiado a `OP-L-99`, el computo iba a cerrar con codigo
**1** y la prueba dio **VERDE, LA GUARDA MUERDE**. Sellado en
`docs/loop/SALIDA_V211_T1B_CERRAR_DOS_ESTADOS_MUTADO.txt`.

**GUARDA (1). LA SEDE POR LAS DOS CONVENCIONES, AL ENTRAR Y AL SALIR:**

| `docs/plan/OPERACIONES.jsonl` | bytes en disco | bytes normalizado a LF | `sha256` disco | `sha256` LF |
|---|---:|---:|---|---|
| **AL ENTRAR** | **513043** | **513043** | **`e96dbe74485814e9`** | **`e96dbe74485814e9`** |
| **AL SALIR** | **513043** | **513043** | **`7a52387bb8a4aa4f`** | **`7a52387bb8a4aa4f`** |

Los bytes no se mueven porque `LISTA` y `HECHA` miden lo mismo, **y los `sha256` si
cambian**, que es lo que prueba que algo se escribio. **2 de 2**
fichas pasaron la guarda del valor viejo, las dos leyendo `LISTA` del fichero.

**GUARDA (2). SOLO CAMBIAN ESOS DOS CAMPOS.** `git diff --numstat` sobre `docs/plan/`
da **1** fila, con **2** lineas anadidas y **2** borradas.
Las dos cuentas por `estado`, las dos publicadas:

| `estado` | ANTES | DESPUES |
|---|---:|---:|
| `HECHA` | **30** | **32** |
| `LISTA` | **41** | **39** |
| **TOTAL** | **71** | **71** |

**CIFRA fichas que se movieron: 2.** **CIFRA otros `id_op` cuyo `estado`
cambio: 0.**

**GUARDA (3), EL CASO POSITIVO.** El `jsonl` se recarga linea a linea: **71**
fichas releidas del disco contra las **71** de antes, y **0** lineas que
no son JSON valido. **VEREDICTO DE LAS TRES GUARDAS: VERDE, LAS TRES.**

**LA VARA NO ES ESTE CAMPO, Y SE DICE AQUI PARA QUE NADIE LO LEA AL REVES:** el `estado`
es **HISTORICO** y no decide que queda por ejecutar (recuadro 0 de `AUDITOR.md`). Se
pone al dia porque **un campo que contradice al acta que cerro la ficha engana a quien
venga**, no porque mida nada.

#### 1.e. LA MEDICION QUE NO ARREGLA NADA, Y SE QUEDO EN MEDICION

El hallazgo `7.1` del acta 210 vive en la linea **74223**. **Lo reproduje al digito y
no toque ni un nodo:** en `dataset/metadata/master_graph.json` (**3853** nodos
contados hoy) `posicionamiento_de_empresa` tiene **CINCO** `pasos_accionables`, los de
Blank, y `la_historia_de_la_empresa` tiene los **CUATRO** de Horowitz. **Cinco mas
cuatro dan nueve.** El veredicto del **1357** NO SE TOCA: su clausula
*"El solape de este par cae en el primer bloque y el veredicto es INVARIANTE"* la cita
el acta en sus lineas **74232** y **74233**, donde la frase parte en dos.

**(a) LAS DOS PREGUNTAS DEL ENCARGO, CONTESTADAS CON MI CONTEO DE HOY.** Menciones de
`posicionamiento_de_empresa` en `docs/plan/02_DESTEJIDOS.md`: **0**, que calza
con el **0** del encargo. Operaciones de `docs/plan/OPERACIONES.jsonl` en cuyo campo
`nodos` vive: **1**, que calza con el **1** del encargo, y es
**`OP-F-04-HOR`**, `DECISION_DE_FUENTE` en **`LISTA`**, fase `01_FUENTES`,
linea **38**.

**PERO LA TERCERA CIFRA NO CALZA, Y NO LA RESUELVO COPIANDO** (`AUDITOR.md` 1.1). El
encargo dice *"con sus **13** nodos"* y la propia adjudicacion de la ficha dice *"LEIDOS
LOS 13"*. **Mi conteo de hoy del campo `nodos` da 14.** La explicacion no la
pongo yo: vive en `docs/plan/01_FUENTES.md`, que en su linea **1453** declara *"El que
sobra es `principio_calidad_mvp`"* y en su linea **1168** que una decision del fundador
*"devolvio `principio_calidad_mvp` a la operacion y la nomina volvio a CATORCE"*.
**La discrepancia queda declarada: la adjudicacion de la ficha lleva el corte viejo, y
el campo lleva el nuevo. No toco ninguno de los dos.**

**(b) LA PARTICION DE LOS 14, CONTADA Y CON SUS NOMBRES.** La vara no es mia:
es la tabla de `docs/plan/01_FUENTES.md`, **lineas 1462 a 1477**, que publica por nodo
los libros declarados y **la frontera leida** el 11 y el 14 ago 2026. De esa frontera
salen dos cifras por nodo sin teclear ninguna (el fin del bloque 1 y el total), y contra
ellas se pone la CIFRA de `pasos_accionables` de HOY. **14** filas leidas,
**0** nodos de la tabla que faltan en el campo y **0** del campo que faltan
en la tabla. **La tabla que sigue esta PEGADA ENTERA de
`docs/loop/SALIDA_V211_T1E_GRUPO_HOROWITZ.txt`, no recompuesta:**

| # | nodo | frontera leida | fin bloque 1 | total de la frontera | pasos HOY | veredicto |
|---:|---|---|---:|---:|---:|---|
| 1 | `actualizacion_posiciones_existentes` | 1 a 4 / 5 a 19 | 4 | 19 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 2 | `background_startup_vs_corporativo` | 1 a 4 / 5 a 9 | 4 | 9 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 3 | `contratacion_experiencia_vs_potencial` | 1 a 4 / 5 a 10 | 4 | 10 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 4 | `decision_de_salir_a_bolsa` | 1 a 5 / 6 a 10 | 5 | 10 | 5 | **EL BLOQUE YA VIVE APARTE** |
| 5 | `decision_de_vender_startup` | 1 a 10 / 11 a 34 | 10 | 34 | 15 | **NI UNA COSA NI LA OTRA** |
| 6 | `estrategia_de_innovacion_producto` | 1 a 3 / 4 a 7 | 3 | 7 | 3 | **EL BLOQUE YA VIVE APARTE** |
| 7 | `manejo_empleados_en_adquisicion` | 1 a 4 / 5 a 9 | 4 | 9 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 8 | `metas_vs_proposito` | 1 a 4 / 5 a 9 / 10 a 14 | 4 | 14 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 9 | `organizacion_adaptativa` | 1 a 4 / 5 a 8 | 4 | 8 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 10 | `plan_mejora_procesos` | 1 a 5 / 6 a 10 / 11 a 15 | 5 | 15 | 5 | **EL BLOQUE YA VIVE APARTE** |
| 11 | `posicionamiento_de_empresa` | 1 a 5 / 6 a 9 | 5 | 9 | 5 | **EL BLOQUE YA VIVE APARTE** |
| 12 | `principio_calidad_mvp` | 1 a 5 / 6 a 10 / 11 a 14 | 5 | 14 | 7 | **NI UNA COSA NI LA OTRA** |
| 13 | `revisiones_regulares_desempeno_ceo` | 1 a 4 / 5 a 10 | 4 | 10 | 4 | **EL BLOQUE YA VIVE APARTE** |
| 14 | `seleccion_ceo_fundador` | 1 a 4 / 5 a 12 | 4 | 12 | 6 | **NI UNA COSA NI LA OTRA** |

**EL REPARTO: 11 con EL BLOQUE YA VIVE APARTE, 3 con NI UNA COSA NI
LA OTRA, y 0 con EL BLOQUE SIGUE DENTRO**, sobre **14** repartidos y
**0** sin medir.

**LA MUTACION, CORRIDA:** desplazando en uno el fin del bloque 1 de cada fila, el cubo
`NI UNA COSA NI LA OTRA` pasa de **3** a **14**. La comparacion
compara. Sellada en `docs/loop/SALIDA_V211_T1E_GRUPO_HOROWITZ_MUTADO.txt`.

**(c) LA PARTICION NO ES UNIFORME (NO), Y AQUI PARO, QUE ES LO QUE EL ENCARGO
MANDA.** Los tres que no calzan con ninguna de las dos son
`decision_de_vender_startup`, `principio_calidad_mvp` y `seleccion_ceo_fundador`.
**Decidir que hacer con una operacion de fuente sin destino no es de esta vuelta**, y no
lo decido.

**LO QUE NO AFIRMO, Y ES LA MITAD HONESTA DE ESTA MEDICION:** *EL BLOQUE YA VIVE APARTE*
es el nombre de **una coincidencia de cifras** (los pasos de hoy son exactamente los del
bloque 1 de la frontera de agosto), **no la prueba de que el bloque 2 exista hoy como
nodo propio**. Eso lo comprobe **para un solo nodo**, el del `7.1`, donde
`la_historia_de_la_empresa` esta y lleva los cuatro pasos. **Para los otros diez no lo
comprobe**, y por eso no lo escribo.
