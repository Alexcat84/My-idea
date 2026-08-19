# -*- coding: utf-8 -*-
"""Pega la seccion del registro de OP-D-01 y OP-D-02 en 02_DESTEJIDOS.md,
con el bloque de la salida sellada IMPRESO y no retecleado (EJECUTOR.md regla 1)."""
import io

salida = io.open('docs/loop/SALIDA_V45_VERIF_OPD01_OPD02.txt', encoding='utf-8').read().rstrip('\n')

CAB = u"""

## `OP-D-01` Y `OP-D-02`: **LA VERIFICACION PUNTO POR PUNTO Y EL REGISTRO DE OPERACION HECHA** (19 ago 2026, vuelta 45)

**Encargado por el acta de la vuelta 44, seccion 4 punto 3, leida hoy en la linea 9688**, con sus
palabras: *EL REGISTRO DE `OP-D-01` Y `OP-D-02` NO BLOQUEA Y NO SE ADIVINA: SE VERIFICA*. La vara
es la que el cierre de `OP-D-06` acaba de modelar: **cada punto del campo `verificacion` con lo
medido al lado**, y el registro se escribe **si y solo si todo lo material cumple**.

### EL BLOQUE MEDIDO, PEGADO ENTERO Y SIN RETECLEAR

**Salida verbatim de `python scripts/loop/vuelta45_verificar_opd01_opd02.py`** (instrumento nuevo,
**estrictamente de solo lectura**, exit 0), sellada en `docs/loop/SALIDA_V45_VERIF_OPD01_OPD02.txt`.
Va **como bloque literal**, que es la unica forma de que la regla 1 del `EJECUTOR.md` (*la tabla se
imprime, no se teclea*) no dependa de que quien la copie no se equivoque:

```
"""

PIE = u"""```

### LO QUE ESE BLOQUE CONTESTA, y las TRES cosas que el bloque NO alcanza a ver

**Los cinco puntos son los MISMOS en las dos operaciones**, leidos del fichero y no tecleados.
**Cuatro se contestan con el bloque de arriba y uno se corre aparte:**

| # | el punto, copiado de `OPERACIONES.jsonl` | `OP-D-01`, MEDIDO | `OP-D-02`, MEDIDO |
|---:|---|---|---|
| **1** | *Gate 0 verde* | **CORRIDA EXTERNA, hecha hoy**: ciclo de **TRES** comandos (el 4 no aplica: al correrlo el censo no se habia movido), los tres **exit 0**. `run_phase1.py --reaplico-curaduria` con **`GATE 0: OK`** y sus **VEINTE** renglones en `[OK]`, **cero en rojo**; `etiquetas_de_cara.py --aplicar` **71**; `sync_assets_web.py` **seis assets**. **LAS DOS COPIAS DEL GRAFO BYTE IGUALES A HEAD**, md5 `f59b0a0eb6c4cf0aa16f797c6ff62ace` las dos | **LA MISMA CORRIDA**, y se dice asi en vez de fingir dos: un Gate 0 mide el arbol entero, no una operacion |
| **2** | *los congelados ... se releen contra el superviviente y salen de la lista* | **3 de 3 FUERA**: **494 `C`**, **592 `D`**, **830 `D`**, ninguno abre ya con marca de congelado y los tres con su razon **REESCRITA** y la vieja conservada | **3 de 3 FUERA**: **724**, **755** y **827**, los tres `D`, releidos contra el superviviente **escrito** (`voz_del_cliente_voc`) cuando la causa (el **TOQUE UNICO** del banco `9.4`) cayo al quedar el nodo estable |
| **3** | *cada nodo resultante dentro del estandar, o dentro de la excepcion de clase de `OP-F-01`* | **CUMPLIDO POR LAS DOS RAMAS**: `producto_minimo_viable` en **6**, DENTRO; `principio_calidad_mvp` en **7**, que entra por la **excepcion de clase aplicada por su criterio escrito**. **Y HAY UN DATO EN CONTRA, publicado abajo** | **CUMPLIDO POR LA PRIMERA RAMA y sin necesitar la excepcion**: los **tres** vivos dentro (**6**, **6** y **5**); el cuarto esta **deprecado con su texto intacto**, asi que no es nodo resultante |
| **4** | *recomputo del cierre transitivo tras el acto (banco `9.21`)* | **CORRIDO HOY** sobre las **575 `A` vigentes**: componente de **UNO** cada nodo, **cero** por encima de dos. El **494** no aporta arista porque hoy es `C` | **CORRIDO HOY**: una sola componente de **TRES**. **NO es deuda de la cirugia**: es lo que la vuelta 33 midio al contestar `P.5` y lo que `P.10` mando hacer con ello. **Y destapa una tension, publicada abajo** |
| **5** | *el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto* | **1 de 1**: la nomina son dos nodos, un solo par interno, el **494**, con fila en el archivo | **6 de 6**, contra los **DOS** registros. **El bloque de arriba reporta 2 sin veredicto y eso es un LIMITE DEL INSTRUMENTO, publicado abajo** |

> **PRIMERA, EL DATO QUE VA EN CONTRA DEL PUNTO 3 DE `OP-D-01`, dicho en vez de omitido.** El
> instrumento de costuras **DISPARA HOY** sobre `principio_calidad_mvp` por bloque (**`sim_bloque`
> 45,8**, **corte tras el paso 5**; la senal de pareja **NO** dispara, 51,2), asi que el nodo esta
> **en la cola**. Esa senal **queda REGISTRADA COMO CITA Y NO COMO VEREDICTO**, por el **limite
> declarado del propio instrumento** (*la cola global no es base de lectura*, acta de la vuelta 40
> seccion 5 pregunta 2) y por el **precedente escrito de `OP-D-04`** (linea **1755** de este mismo
> fichero, donde la senal de bloque de `reglas_brainstorming` quedo como cita y los dos resultantes
> de siete pasos procedieron). **LA LECTURA TEXTUAL PROPIA DE HOY, con los siete pasos delante:**
> son **UN SOLO ARCO** y no dos narraciones apiladas (preguntar si pulir contribuye al aprendizaje,
> no asumir el estandar de la industria, lanzar simplificado, distinguir el defecto que impide
> aprender de la baja fidelidad estetica, capturar y priorizar el aprendizaje, usar ese feedback
> para decidir si invertir, iterar rapido). **El corte tras el 5 cae en el PIVOTE DE CONSTRUIR A
> USAR**, que es exactamente la figura que el acta de la vuelta 44 adjudico **a favor** en la
> costura del **711**. **VA MARCADO COMO DISCUTIBLE.**

> **SEGUNDA, LA TENSION QUE EL RECOMPUTO DEL PUNTO 4 DE `OP-D-02` DESTAPA.** Como la fusion absorbio
> el nodo del **MEDIO** del camino (`enfoque_mercado_voc`) dentro de uno de sus **EXTREMOS**
> (`voz_del_cliente_voc`), el **resolutor de `P.1`** hace que la `A` del puesto **788**
> (`enfoque_mercado_voc` con `voice_of_customer_homework`) **resuelva hoy sobre el par
> `voz_del_cliente_voc` con `voice_of_customer_homework`, que es justo el que `LD-74` leyo como
> `D`.** **Dos registros dicen hoy cosas distintas del mismo par resuelto.** **Por la regla escrita
> no hay nada que corregir aqui:** la **cola de relectura post fusion** de `08_VERIFICACION.md`
> admite **solo `B` y `C`** y dice con sus palabras que *un `A` ya esta resuelto por definicion*, asi
> que el 788 **no vuelve a la cola**. Queda **ANOTADO PARA LA FASE 04**, que es donde vive el
> *enlazar el resto* que `P.10` ya mando. **VA MARCADO COMO DISCUTIBLE.**

> **TERCERA, UN LIMITE DE MI PROPIO INSTRUMENTO, declarado antes que su cifra.** El bloque de arriba
> reporta **2 pares internos sin veredicto** en `OP-D-02` porque **lee un solo registro**,
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`. **NO es un hueco de lectura:** los tres pares que faltaban
> se leyeron como **`LD-72`, `LD-73` y `LD-74`** en la vuelta 33, adjudicadas por el fundador por
> `P.5`, y viven en `docs/plan/LECTURAS_DIRIGIDAS.md` (**OCTAVA TANDA, linea 648**, leida hoy) **y no
> en el archivo de veredictos, porque ninguno de los tres estaba en la cola y por eso NO mueven `n`**,
> que sigue en **3.388**. Contra los **dos** registros el acto esta **6 de 6**: **386 `A`**, **788
> `A`** y **526 `A`** del cribado, mas **`LD-72` `D`**, **`LD-73` `D`** y **`LD-74` `D`**. **La salida
> del instrumento se deja TAL CUAL, con su 2, y la cifra correcta se dice aqui**: tapar la salida
> para que calce seria justamente lo que la casa prohibe.

### LO DEFERIDO, CITADO COMO DEFERIDO CON SU REGLA, y no impide ninguno de los dos registros

| que queda | su regla, citada | donde va |
|---|---|---|
| **el par nuevo que una relectura diera** | **ENTRA POR EL RECOMPUTO (banco `9.10`)**, que es la letra del propio campo `preservar` de `OP-D-01` en su correccion declarada del 15 ago 2026 | **ya ejecutado por la vuelta 33** |
| **el enlace mutuo del 494** | el campo `aristas_nuevas` de `OP-D-01` esta **VACIO**, leido hoy | **fase 04**. **RE-VERIFICADO HOY EN LOS DOS SENTIDOS** contra el grafo, porque una busqueda negativa no se puede citar (regla 9): **ninguno de los dos nombra al otro** en `nodos_previos` ni en `nodos_siguientes` |
| **los dos extremos del camino de `OP-D-02` sin enlazar** | `P.10`: *fundir solo el subconjunto cerrado y **enlazar el resto*** | **fase 04** |

**LAS DEPENDENCIAS, MEDIDAS HOY Y NO SUPUESTAS:** `OP-D-01` depende de `OP-F-03`, que trae **HECHA**
en su nota, y las tres que la bloquean por dependencia inversa (`OP-F-04-COL`, `OP-F-04-HOR`,
`OP-F-04-WEI`) traen **HECHA las tres**. `OP-D-02` tiene `depende_de` **vacio** y **ninguna** de las
**71** operaciones la nombra en su `bloquea_a`, comprobado por barrido. **Ninguna dependencia
abierta en las dos.**

### EL REGISTRO ESCRITO, con el patron de la vuelta 30 y sin estrenar nada

**TODO LO MATERIAL CUMPLE EN LAS DOS, asi que el registro se escribe.** Va **en la nota**, con
`python scripts/loop/vuelta30_nota.py docs/loop/NOTAS_V45_OPD01_OPD02.json --ejecutar`
(`docs/loop/SALIDA_V45_NOTA_OPD01_OPD02.txt`), **simulado antes con `--simular`**:

| | nota antes | nota despues | campo `estado` |
|---|---:|---:|---|
| `OP-D-01` | 5.258 | **11.739** | **`LISTA`**, sin tocar |
| `OP-D-02` | 8.190 | **14.355** | **`LISTA`**, sin tocar |

**El fichero sigue teniendo 71 lineas.** El campo `estado` **se queda en `LISTA`** porque el esquema
de `OPERACIONES.jsonl` **no tiene el valor `HECHA`** y estrenarlo seria doctrina de esquema,
**adjudicado NO en el punto 7 del acta de la vuelta 30**.

> **Y UNA DIFERENCIA CON EL REGISTRO DE `OP-D-06`, que aquel declaro que le faltaba: ESTOS DOS SI
> TIENEN ACTA DETRAS ANTES DE ESCRIBIRSE.** Los encarga el acta de la vuelta 44, que verifico la
> vuelta entera con **CERO caidas del ejecutor** y **ciega 7 de 7** (lineas **9762** y **9609**).
"""

with io.open('docs/plan/02_DESTEJIDOS.md', 'a', encoding='utf-8', newline='') as fh:
    fh.write(CAB + salida + u"\n" + PIE)
print("OK, seccion pegada")
