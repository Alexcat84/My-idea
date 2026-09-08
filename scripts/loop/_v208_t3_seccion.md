### TAREA 3. LA MESA `OP-L-03`, MEDIDA CONTRA LOS SEIS DOCUMENTOS QUE SU FICHA NOMBRA

**LO QUE DEJO SELLADO, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON:**

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V208_T3_VARA.txt` (sellada en `4da48516`) | 11793 bytes en disco y 11793 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T3_COTEJO.txt` | 9279 bytes en disco y 9279 normalizado a LF | 0 |

#### 3.a. LA VARA, SELLADA EN SU PROPIO COMMIT ANTES DEL COTEJO

**18 PUNTOS, `V.1` a `V.18`**, cada uno con la CITA LITERAL del campo y del
elemento de la ficha del que sale, y **las 16 citas comprobadas VERBATIM contra la
ficha por el propio computo**: `CIFRA citas que NO aparecen verbatim: 0`. Los otros
dos no llevan literal porque son sobre la **estructura** de un campo y no sobre su
texto, y eso se dice en vez de inventarles una cita.

**LA SEDE FINA ES `campo[indice]`**, no un numero de linea: la ficha entera vive en
**UNA** sola linea de `docs/plan/OPERACIONES.jsonl`, la **43**.

**LA FICHA, SELLADA:** linea **43**, **18** campos, **4** elementos de `evidencia`
(**1** de ellos CORRECCION DECLARADA), **4** de `verificacion` (**1** CORRECCION
DECLARADA), `depende_de` con **6** (`OP-D-01` a `OP-D-06`), `bloquea_a` con **2**
(`OP-U-01`, `OP-U-02`), `fecha_corte` **2026-08-11**, `orden` **3**, `tipo` MESA.
**El campo `estado` se lee como dato y no se toca** (`AUDITOR.md` 0): dice `LISTA`.

**EL ESCARMIENTO DE LA 207 NO LO CITE: LO APLIQUE, Y ME CAZO UN PUNTO.** Antes de
sellar un punto como NO DOCUMENTAL, el computo **busca su literal en los seis
documentos** y cae en ROJO si aparece. Mi primer borrador sellaba la `V.17` (las
dependencias) como NO DOCUMENTAL por ser estructura de la ficha, y la busqueda
encontro `OP-U-01` en `docs/plan/BANCO_DEL_PLAN.md` y en
`docs/plan/LECTURAS_DIRIGIDAS.md`, **una vez en cada uno**. **La vara no se sello y
la `V.17` paso a DOCUMENTAL.** Eso es mover un punto **antes** de mirar el cotejo,
que es lo que el escarmiento pide, y **no despues**, que es lo que el sello
prohibe.

**Y LA BUSQUEDA VA TAMBIEN POSITIVA**, porque una negativa no se puede citar sola
(`EJECUTOR.md` 9): **6** literales de control, **los 6 aparecen**, **0** que
fallen.

**EL REPARTO, SELLADO ANTES DE COTEJAR:** **16** documentales y **2** NO
documentales con su motivo escrito. La `V.16` es una cifra de recomputo cuya sede
declarada es `docs/plan/RECOMPUTO_3388.md`, y la `V.18` una clausula sobre el campo
`en_cola_sin_leer` de `scripts/plan/recomputo_3388.py`; **ninguna de las dos es de
los seis**, con **0** apariciones medidas en cada uno.

| documento | puntos que se cotejan contra el |
|---|---|
| `docs/plan/BANCO_DEL_PLAN.md` | **4**: `V.1`, `V.9`, `V.15`, `V.17` |
| `docs/plan/OP_L_03_LECTURAS.jsonl` | **5**: `V.2`, `V.4`, `V.6`, `V.7`, `V.11` |
| `docs/plan/LECTURAS_DIRIGIDAS.md` | **3**: `V.3`, `V.8`, `V.10` |
| `docs/plan/OP_L_03_TRIANGULOS.jsonl` | **2**: `V.5`, `V.12` |
| `docs/loop/EJECUTOR.md` | **1**: `V.14` |
| `docs/loop/AUDITOR.md` | **1**: `V.13` |

**LO QUE DECLARO Y NO DISIMULO:** de los seis documentos, **TRES los abri antes de
esta tarea y en esta misma vuelta**: `EJECUTOR.md` porque lo manda el encargo como
primer acto, `AUDITOR.md` porque el encargo lo cita, y `LECTURAS_DIRIGIDAS.md`
porque lo midio mi TAREA 2. **Los otros tres los abro por primera vez en el
cotejo.** El sello garantiza que la vara y su reparto se escriben ANTES de cotejar,
y eso se cumple; **decir "antes de abrir ningun documento" sin esta nota seria
falso.** Va como `D.3`.

#### 3.b. LOS SEIS DOCUMENTOS, REMEDIDOS, Y EL COTEJO PUNTO POR PUNTO

**LOS SEIS CALZAN AL DIGITO CON EL CONTRASTE DEL ENCARGO, POR LAS DOS
CONVENCIONES**, y `CIFRA documentos cuya medicion NO calza: 0`:

| documento | mi medicion | el contraste | calza |
|---|---|---:|---|
| `docs/plan/BANCO_DEL_PLAN.md` | 61554 bytes en disco y 61554 normalizado a LF | 61554 | SI |
| `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 bytes en disco y 214916 normalizado a LF | 214916 | SI |
| `docs/loop/EJECUTOR.md` | 13194 bytes en disco y 13194 normalizado a LF | 13194 | SI |
| `docs/plan/OP_L_03_LECTURAS.jsonl` | 51368 bytes en disco y 51368 normalizado a LF | 51368 | SI |
| `docs/plan/OP_L_03_TRIANGULOS.jsonl` | 55705 bytes en disco y 55705 normalizado a LF | 55705 | SI |
| `docs/loop/AUDITOR.md` | 30581 bytes en disco y 30581 normalizado a LF | 30581 | SI |

**Y LO DIGO PORQUE EL ENCARGO LO PIDE EXPRESAMENTE: mi TAREA 2 NO toco
`docs/plan/LECTURAS_DIRIGIDAS.md`, solo lo leyo, y por eso sale igual.**

**LAS DIECIOCHO FILAS, CADA UNA CON SU FICHERO Y SU LINEA:**

| punto | doc | veredicto | cita |
|---|---|---|---|
| `V.1` | BDP | **CUBRE** | `docs/plan/BANCO_DEL_PLAN.md:239` `## P.5 REGLA DE ORDEN: CADA ACTO QUE VAYA A FUNDIRSE SE LEE ENTERO` |
| `V.2` | LEC | **CUBRE** | `docs/plan/OP_L_03_LECTURAS.jsonl:1`, `"id_op": "OP-L-03"` en 14 lineas |
| `V.3` | LD | **NO CUBRE** | `docs/plan/LECTURAS_DIRIGIDAS.md`, **el patron no encontro `reparto por acto`** |
| `V.4` | LEC | **CUBRE** | `docs/plan/OP_L_03_LECTURAS.jsonl:1`, `"acto":` en 14 lineas |
| `V.5` | TRI | **CUBRE** | `docs/plan/OP_L_03_TRIANGULOS.jsonl:1`, `"terna":` en 19 lineas |
| `V.6` | LEC | **CUBRE** | `docs/plan/OP_L_03_LECTURAS.jsonl:3`, con `"leido": true` en 11, `"leido": false` en 3 y `"cifra_pares_leidos"` en 11 |
| `V.7` | LEC | **CUBRE** | `docs/plan/OP_L_03_LECTURAS.jsonl:1`, `"leido": false` en 3 lineas |
| `V.8` | LD | **CUBRE** | `docs/plan/LECTURAS_DIRIGIDAS.md:76`, las DOS sondas de ausencia dan **0** y el control positivo aparece |
| `V.9` | BDP | **CUBRE** | `docs/plan/BANCO_DEL_PLAN.md:239` para `P.5` y `:759` para `P.10` |
| `V.10` | LD | **CUBRE** | `docs/plan/LECTURAS_DIRIGIDAS.md:11` `marcadas LECTURA DIRIGIDA: no entran en la cola ni mueven su marcador.` |
| `V.11` | LEC | **CUBRE** | `docs/plan/OP_L_03_LECTURAS.jsonl:1`, `"cobertura"` en las 14 filas |
| `V.12` | TRI | **CUBRE** | `docs/plan/OP_L_03_TRIANGULOS.jsonl:1`, `"el_lado_de_fuera_es_el_D"` en 19 lineas |
| `V.13` | AUD | **CUBRE** | `docs/loop/AUDITOR.md:17` `> **LA VARA DEL TRABAJO PENDIENTE ES EL INSTRUMENTO, NUNCA EL CAMPO estado**` |
| `V.14` | EJE | **CUBRE** | `docs/loop/EJECUTOR.md:164` `una busqueda negativa no se puede citar` |
| `V.15` | BDP | **CUBRE** | `docs/plan/BANCO_DEL_PLAN.md:239` |
| `V.16` | --- | **NO DOCUMENTAL** | sellado antes de mirar; se busco igual en los seis y da **0** |
| `V.17` | BDP | **CUBRE** | `docs/plan/BANCO_DEL_PLAN.md:282` `173 actos ya estan enteros (OP-U-01)` |
| `V.18` | --- | **NO DOCUMENTAL** | sellado antes de mirar; se busco igual en los seis y da **0** |

**LA `6.1` SE APLICA A TRES PUNTOS, Y NO LOS ELEGI A OJO:** cada uno lleva escrito
el trozo de su propia cita por el que entra. La `V.11` porque su cita dice
literalmente *"se re-mide con su cobertura al lado"*; la `V.6` y la `V.7` porque
publican cifras de cobertura. **Las tres pasan la `6.1` ENTERA**: las **14** filas
de `docs/plan/OP_L_03_LECTURAS.jsonl` llevan el campo `cobertura` no vacio y **0**
lo tienen vacio. Si alguna no lo llevara, el computo bajaba el punto a `A MEDIAS`,
y si no lo llevara ninguna, a `NO CUBRE`.

**DOS CAIDAS MIAS, LAS DOS CAZADAS CORRIENDO EL COMPUTO Y ANTES DE PUBLICARLAS.**
Mi primera corrida daba **3 NO CUBRE** y **dos de los tres eran de mi patron, no
del mundo**. Es la misma especie que la `C.3` de mi reporte de la 207 y la `9.3`
del auditor.

- **`V.8` AFIRMA UNA AUSENCIA Y YO LA BUSCABA COMO PRESENCIA.** Su cita dice que el
  documento *"trae 0 apariciones del literal `reparto por acto` y 0 menciones de
  `OP-L-03`"*. **Encontrar 0 es lo que la CONFIRMA**, y yo publicaba `NO CUBRE` por
  no encontrarla. Invertida, y con **control positivo** al lado (`LD-01` en 2
  lineas y `LECTURA DIRIGIDA` en 6), porque una busqueda negativa no se puede citar
  sola.
- **`V.13` SI ESTA Y MI SONDA NO LA VEIA POR LAS MAYUSCULAS.** `AUDITOR.md` lo
  escribe en versales en su linea **17** y yo buscaba minusculas. **Mi patron era
  mas estrecho que la afirmacion que verificaba.**

**LA VARA SELLADA NO SE TOCO PARA ARREGLAR NINGUNA DE LAS DOS**: lo que cambio es
**como busca el cotejo**, no **que** se coteja ni **contra que documento**. El
sello sigue en sus 18 puntos y su reparto de 16 mas 2.

#### 3.c. LA COBERTURA, MEDIDA Y NO NARRADA

| veredicto | cuantos | cuales |
|---|---:|---|
| **CUBRE** | **15** | `V.1`, `V.2`, `V.4`, `V.5`, `V.6`, `V.7`, `V.8`, `V.9`, `V.10`, `V.11`, `V.12`, `V.13`, `V.14`, `V.15`, `V.17` |
| **A MEDIAS** | **0** | (ninguno) |
| **NO CUBRE** | **1** | `V.3` |
| **NO DOCUMENTAL** | **2** | `V.16`, `V.18` |

**LA LISTA NOMINAL DE LOS QUE NO CUBREN: `V.3`.**

**LAS DOS CUENTAS SEPARADAS, Y ESTA VEZ CALZAN:** la del **SELLO** da **16** puntos
documentales y la de los **VEREDICTOS** da **16**. **Calzan.** Es la diferencia con
la 207, donde el sello decia 10 y los veredictos 11, y la causa es que aqui el
escarmiento movio la `V.17` **antes** de sellar en vez de despues de mirar.

**EL UNICO `NO CUBRE` ES CIERTO Y LA PROPIA FICHA YA LO SABIA.** La `V.3` sale de
`evidencia[2]`, que dice *"LECTURAS_DIRIGIDAS.md, el reparto por acto"*, y el
reparto por acto **no esta ahi**. No es un hallazgo nuevo: la CORRECCION DECLARADA
de la vuelta 202, que vive en `evidencia[3]` de esta misma ficha, ya lo midio y lo
escribio con estas palabras: *"EL DOCUMENTO NO ES EL QUE TRAE EL REPARTO: LA
EVIDENCIA APUNTABA AL DOCUMENTO EQUIVOCADO"*. **Mi cotejo lo reproduce por su
cuenta**, y las dos sedes reales (`OP_L_03_LECTURAS.jsonl` y
`OP_L_03_TRIANGULOS.jsonl`) **si cubren**, en la `V.4` y la `V.5`. **La evidencia
vieja no se retira y el `NO CUBRE` se publica igual**: la correccion anadio la sede
buena sin borrar la mala, y mientras la mala siga escrita, el punto que la cita no
cubre.

#### 3.d. NO CIERRO LA FICHA, LA PROPONGO Y PARO

**NO TOQUE EL CAMPO `estado`, QUE SIGUE DICIENDO `LISTA`**, y no lo digo: lo mide
el `sha256`. `docs/plan/OPERACIONES.jsonl` sale de esta tarea en **513043** bytes
en disco y **513043** normalizado a LF, con sha256 `829c583eb779cab6` por disco y
`829c583eb779cab6` por LF, **identico al de mi apertura**.

**MI PROPUESTA, Y PARO AHI:** `OP-L-03` queda **medida en 15 CUBRE, 1 NO CUBRE y 2
NO DOCUMENTALES sobre 18 puntos**, con su unico `NO CUBRE` nombrado, citado y ya
reconocido por la propia ficha en su correccion de la vuelta 202. **Propongo que no
se cierre mientras `evidencia[2]` siga apuntando al documento equivocado**, y **la
adjudicacion es del auditor**.

#### 3.e. LA TAREA CABE ENTERA, CON SUS GUARDAS, Y POR ESO NO QUEDA ABIERTA

El `3.e` dice que si la tarea no cabe con sus guardas completas se deja abierta y
se dice. **Cabe:** la vara va sellada en su propio commit (`4da48516`) con sus 16
citas verbatim y su control positivo, el cotejo trae las 18 filas **con fichero y
linea**, la `6.1` se aplica a los tres puntos que la piden, las dos cuentas se
publican separadas y la ficha no se cierra. **Ninguna guarda se recorto**, y las
dos caidas de sonda van declaradas arriba en vez de escondidas.
