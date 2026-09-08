### TAREA 2. LA `TABLA VIVA DE LOS PUROS`, PUESTA AL DIA POR EL CARRIL DEL `9.10`

**LO QUE DEJO SELLADO, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON:**

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V208_T2A_DENOMINADOR.txt` | 11634 bytes en disco y 11634 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2B_TABLA_VIVA_SECO.txt` | 4447 bytes en disco y 4447 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2B_TABLA_VIVA.txt` | 4592 bytes en disco y 4592 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2D_COTEJO_REPETIDO.txt` | 10767 bytes en disco y 10622 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2D_V3.txt` | 5403 bytes en disco y 5403 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2E_V14.txt` | 3492 bytes en disco y 3492 normalizado a LF | 0 |

#### 2.a. EL DENOMINADOR PRIMERO, RECOMPUTADO DE LA NOMINA DE MIEMBROS

**EL ORDEN NO ERA DE ADORNO Y LA MEDICION LO CONFIRMA.** Los pares posibles se
contaron de la **nomina de miembros** de cada familia, en
`docs/INTRA_DOMINIO_INFORME.md`, y **no de la tabla**, con el resolutor puesto
(`P.1`): **3853** ficheros de nodo leidos, **761** alias en el mapa y **3853**
`node_id` distintos en disco.

| nomina | miembros recomputados | posibles recomputados | posibles segun la tabla viva | posibles segun la mesa | veredicto |
|---|---:|---:|---:|---:|---|
| junta asesora | **4** | **6** | 6 | 6 | LAS TRES CALZAN |
| seleccion de canal | **6** | **15** | 15 | **10** | **LA TABLA CALZA, LA MESA NO** |

**Y EL HALLAZGO `7.2` DEL ACTA 207 QUEDA CONFIRMADO CON SU CAUSA MEDIDA, QUE ES
LO QUE FALTABA.** El **10** de la mesa sale de su tabla por nomina,
`docs/plan/LECTURAS_DIRIGIDAS.md:31`, que cuenta **5 miembros**. La nomina de esa
familia, verificada contra el grafo en `docs/INTRA_DOMINIO_INFORME.md:5313` y
enumerada de la **5314** a la **5319**, tiene **SEIS**, y lleva una **CORRECCION
DECLARADA del 11 ago 2026** en la linea **5321** que dice literalmente *"son SEIS
y no cinco"*. **La mesa cuenta sobre el universo anterior a esa correccion.**

**LOS LEIDOS TAMPOCO SE HEREDAN.** De las **27** cabeceras `LD` que hay hoy en el
documento de la mesa, las que tienen **los dos extremos dentro de la nomina tras
resolver** son **1** en la junta asesora (`LD-01`, **D**) y **2** en la seleccion
de canal (`LD-02` **D** y `LD-03` **A**).

| nomina | leidos que la tabla lleva hoy | mas las LD de la mesa | sobre el denominador recomputado | cobertura |
|---|---:|---:|---|---|
| junta asesora | 5 | **6** | **6 de 6** | **COMPLETA** |
| seleccion de canal | 8 | **10** | **10 de 15** | **INCOMPLETA, o sea PROVISIONAL** (banco `9.26`) |

**Y AQUI ESTA LO QUE CAMBIA LA RESPUESTA DE LA MESA, Y NO LO RESUELVO COPIANDO**
(`EJECUTOR.md` 2). La mesa declara en `docs/plan/LECTURAS_DIRIGIDAS.md:291` que
la seleccion de canal queda en *"10 de 10, cobertura COMPLETA"*. **Sobre el
denominador recomputado es 10 de 15 y NO es completa.** Las dos cifras quedan
escritas y ninguna se elige en silencio. **De las DOS nominas que la mesa declara
con cobertura COMPLETA, sobre el denominador recomputado solo UNA lo esta.**

**UNA SEGUNDA CUENTA QUE NADIE PEDIA Y QUE APARECIO AL PONER EL RESOLUTOR, Y LA
DECLARO PORQUE ES MIA Y NO DEL ENCARGO.** Los **4** miembros de la junta asesora
son **2** nodos distintos **tras resolver**: `identificar_junta_asesores` resuelve
hoy a `identificar_consejo_asesores`, y `formalize_advisory_board` a
`formalizar_junta_asesora`. En esa convencion los pares posibles son **1** y no
**6**. **Es HUELLA DE FUSION**, que es como la propia ficha `OP-L-01` llama a este
mismo fenomeno: la campana fundio dos de los cuatro **despues** del `fecha_corte`
de la ficha. **Las columnas de la tabla cuentan en LITERAL**, con los ids tal como
la nomina los escribe, y por eso el cotejo va contra la convencion literal; **la
resuelta se publica al lado y no sustituye a ninguna**. En la seleccion de canal
las dos convenciones dan lo mismo, **15**, y **0** miembros fundidos.

#### 2.b. LAS DOS FILAS, ESCRITAS POR ADICION Y CON CORRECCION DECLARADA

**NINGUNA DE LAS ONCE CIFRAS DE LAS DOS FILAS SE TECLEO:** el computo que las
escribe las **lee de la salida del 2.a** y cae en rojo si no puede leer una.

Las dos filas corregidas, pegadas enteras de la salida del instrumento:

| # | racimo | miembros | pares posibles | leidos | en A |
|---:|---|---:|---:|---:|---:|
| **7** | la junta asesora (fila corregida) | **4** | **6** | **6** | **4** |
| **11** | la seleccion de canal (fila corregida) | **6** | **15** | **10** | **9** |

La **7** queda **MEZCLADO con COBERTURA COMPLETA, 6 de 6**, cerrada por `LD-01`
(**D**, `docs/plan/LECTURAS_DIRIGIDAS.md:76`), que es el par que nunca entro a la
cola; **la clase no cambia, ya era MEZCLADO por el puesto 1190**. La **11** pasa
de **SUB-PURO** a **MEZCLADO**, porque `LD-02` (**D**, linea **95**) mete el
primer `D` dentro de la nomina y el sub-puro cae, y su cobertura queda en
**10 de 15, INCOMPLETA y por tanto PROVISIONAL**, con `LD-03` (**A**, linea
**112**) sumando el otro par.

**LA MARCA `(FILA CORREGIDA EN LA VUELTA 208)` EN LA CELDA DE RACIMO NO ES
ADORNO, Y LA CAZO LA PROPIA GUARDA.** Sin ella, la fila corregida de la junta
asesora empezaba con el mismo texto que la vieja, la guarda del cierre contaba
**dos** apariciones del ancla y no podia distinguir el texto viejo del nuevo. Se
vio corriendo el computo, no razonandolo.

#### 2.c. LAS DOS CONVENCIONES, ANTES Y DESPUES, Y CERO LINEAS BORRADAS

| momento | bytes en disco | bytes normalizado a LF | sha256 disco | sha256 LF |
|---|---:|---:|---|---|
| ANTES | 182228 | 182228 | `68557cd00a3124f4` | `68557cd00a3124f4` |
| DESPUES | 186490 | 186490 | `8adbd60239509bb4` | `8adbd60239509bb4` |

**LAS CUATRO CIFRAS DE ANTES CALZAN AL DIGITO CON EL CONTRASTE DEL ENCARGO.**
El fichero crece **4262** bytes por las dos convenciones y pasa de **3119** a
**3185** lineas.

**`git diff --numstat` da 66 lineas ANADIDAS y 0 BORRADAS.** El encargo dice que
borrar una sola linea de texto viejo es rojo: **son cero**. Y la guarda propia lo
mide por su lado: las lineas del texto de entrada que **no estan, en orden**, en
el de salida son **0**; las dos filas viejas siguen apareciendo **una vez cada
una**, ahora en las lineas **970** y **974**; y la cabecera con su corte de
**14 ago 2026** sigue entera.

**EL CORTE SE ACTUALIZA POR ADICION Y NO PISANDO LA CABECERA, Y ESO VA MARCADO
COMO DISCUTIBLE `D.2`.** El encargo dice que el corte de la tabla se actualiza
tambien; el 2.c dice que borrar una linea vieja es rojo. **Las dos cosas juntas
solo se pueden cumplir anadiendo:** debajo de la cabecera va un **puntero** que
declara que hay una correccion posterior con corte **7 sep 2026** y a que filas
toca, y la cabecera vieja no se toca ni se tacha.

**LO QUE ESTA CORRIDA ESCRIBIO NO TRAE NI UN GUION LARGO NI UNO MEDIO:** puntero
**0** y **0**, bloque **0** y **0**, medidos antes de escribir. El fichero entero
tenia **22** guiones largos y **1** medio al entrar, **todos del texto viejo**, y
no se toco ninguno.

#### 2.d. LA `V.3`, DEJADA MEDIDA PARA QUE EL AUDITOR LA CIERRE EN LA 209

**NO CIERRO `OP-L-01` Y NO TOQUE SU CAMPO `estado`.** `docs/plan/OPERACIONES.jsonl`
sale de esta tarea en **513043** bytes en disco y **513043** normalizado a LF, con
sha256 `829c583eb779cab6` por disco y `829c583eb779cab6` por LF, **identico al de
mi apertura**.

**TRES LECTURAS, Y NINGUNA SE ELIGE EN SILENCIO:**

| lectura | criterio | veredicto de la `V.3` | cita |
|---|---|---|---|
| **(1)** el instrumento sellado de la 207, corrido tal cual | toma la PRIMERA fila que case, y esa es la VIEJA | **A MEDIAS** | `docs/loop/SALIDA_V208_T2D_COTEJO_REPETIDO.txt` |
| **(2)** el mismo criterio, sobre las filas CORREGIDAS | `leidos` igual a `posibles` en las DOS nominas | **A MEDIAS** | `docs/BANCO_DE_TEXTOS.md:999` y `:1000` |
| **(3)** el criterio de la adjudicacion `6.1` del acta 207 | la cobertura ESCRITA al lado, con su motivo, y lo incompleto dicho PROVISIONAL | **CUBRE** | `docs/BANCO_DE_TEXTOS.md:999` y `:1000` |

**LA (1) HAY QUE LEERLA CON SU DEFECTO DELANTE, Y ES UN HALLAZGO MIO.** Corri el
instrumento sellado de la 207 sin tocarle una linea y sigue diciendo *"de las 2
nominas que la mesa declara con cobertura COMPLETA, 2 siguen sin cerrar"*. **Esa
frase ya no es cierta entera**: la junta asesora SI cierra en su fila corregida.
La causa esta medida: su busqueda toma `fila_ban[0]`, **la primera fila cuya celda
de nombre case**, y una correccion por adicion deja **dos** filas por nomina.
**El instrumento lee la vieja.** No lo ensancho, porque rige la moratoria: lo
declaro y va a la seccion 3.0.

**LO QUE LAS TRES LECTURAS TIENEN EN COMUN, Y ES LO UNICO QUE NO SE DISCUTE: la
tabla AHORA LLEVA EL EFECTO DE LA MESA**, que es exactamente lo que no llevaba y
lo que dejaba la `V.3` en `A MEDIAS`. **Lo que queda por adjudicar es si una
cobertura que la propia fila declara PROVISIONAL cubre el punto o no**, y esa
letra es del auditor.

**MI PROPUESTA, Y PARO AHI:** por la lectura (3), que es la del criterio que la
`6.1` escribio, la `V.3` pasa a **CUBRE** y `OP-L-01` queda en **11 de 11**.
**No la cierro yo.**

#### 2.e. LA `V.14`, CORREGIDA POR ADICION Y NO REHECHA

**EL SELLO NO SE REESCRIBE Y LO MIDE EL `sha256`.**
`scripts/loop/_v207_t2_vara.py` entra y sale de esta tarea en **10846** bytes en
disco y **10846** normalizado a LF, con sha256 `e5e1c0904ea135b2` por las dos
convenciones. Sigue diciendo, verbatim, que la `V.14` *"es una CLAUSULA DE
VERIFICACION contra las nominas del inventario, que NO viven en ninguno de los
tres"*.

**Y ESA SEDE SI EXISTE, MEDIDA HOY.** La cobertura de esas nominas vive en la
`TABLA VIVA DE LOS PUROS`, que abre en `docs/BANCO_DE_TEXTOS.md:938`, **que es
uno de los tres documentos de la evidencia**. Las **2** filas que esta vuelta
corrige estan en las lineas **999** y **1000**, y **las 2 llevan la palabra
COBERTURA escrita**. **La `V.14` es DOCUMENTAL y su sede es
`docs/BANCO_DE_TEXTOS.md`.**

**LAS CUENTAS, PUBLICADAS JUNTAS, QUE ES LO QUE LA `6.4` PIDE:**

| cuenta | cifra | cuales |
|---|---:|---|
| **la del SELLO**, que no se reescribe | **10** | `V.1`, `V.2`, `V.3`, `V.5`, `V.6`, `V.7`, `V.8`, `V.9`, `V.10`, `V.11` |
| **la de los VEREDICTOS de hoy**, leida del fichero de salida | **11** | las diez de arriba mas `V.4` |
| **la que esta declaracion anade**, y que el instrumento no puede ver porque lee el sello | **12** | las once de arriba mas `V.14` |

**LA ASIMETRIA SE DECLARA Y NO SE ARREGLA MOVIENDO EL SELLO.** Mover un punto de
lado despues de mirar es exactamente lo que sellar el reparto viene a impedir, y
la `6.4` lo adjudico asi con todas las letras. **Es la misma especie que la `D.2`
de la 207 con la `V.4`, y por eso se trata igual.**
