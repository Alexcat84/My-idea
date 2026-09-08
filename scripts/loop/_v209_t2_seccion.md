### TAREA 2. LAS DOS CIFRAS DE `OP-L-01` QUE SEGUIAN MAL EN SU PROPIO DOCUMENTO

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de
`docs/loop/SALIDA_V209_T2A_DENOMINADOR.txt`,
`docs/loop/SALIDA_V209_T2B_CORRECCIONES.txt` y
`docs/loop/SALIDA_V209_T2C_CERRAR_OPL01.txt` con
`scripts/loop/_v209_t2_seccion.py`, que **cae en rojo si no puede leer una**.

#### 2.a. EL DENOMINADOR, RECOMPUTADO ANTES DE ESCRIBIR NADA

**EL RESOLUTOR VA PUESTO** (`P.1`): **3853** `node_id` distintos en disco y
**761** alias en el mapa, con `mapa_de_alias()` y `resolver()` **importados**
de `vuelta166_tarea2_correccion_op_l_01.py`. **La nomina se leyo de
`docs/INTRA_DOMINIO_INFORME.md`, lineas `5314` a `5319`, y NO de la tabla**,
que es lo que el encargo manda y lo que el hallazgo `7.2` del acta 207
explica: escribir los leidos sobre un denominador sin comprobar seria
arreglar la mitad visible.

| nomina | LITERAL, que es la que MANDA | RESUELTA, publicada AL LADO | fundidos |
|---|---|---|---:|
| junta asesora | **4** miembros y **6** pares | **2** miembros y **1** pares | **2** |
| **seleccion de canal** | **6** miembros y **15** pares | **6** miembros y **15** pares | **0** |

**MANDA LA CONVENCION DEL CORTE DE LA FICHA, O SEA LA LITERAL, Y NO LA VUELVO
A DECIDIR:** es la adjudicacion `6.6` del acta 208, por el banco `9.21` mas
`P.1`. El `fecha_corte` de `OP-L-01` es **2026-08-11** y la resuelta es la
foto de hoy, **7 sep 2026**, que se publica **al lado y nunca en su lugar**.
En la seleccion de canal **las dos convenciones dan lo mismo**, con **0**
miembros fundidos; en la junta asesora **no**, y por eso las cuatro cifras van
las cuatro escritas en vez de elegir una en silencio.

**LA NOMINA ESTA VERIFICADA CONTRA EL GRAFO** en
`docs/INTRA_DOMINIO_INFORME.md:5314` a `:5319`, y su **CORRECCION DECLARADA
del 11 ago 2026** vive en la `:5321`, literal: *son SEIS y no cinco*. Los seis
existen hoy en el grafo, **0** fuera.

**LOS LEIDOS TAMPOCO SE HEREDAN:** hay **27** cabeceras `LD` en el documento y
**2** lecturas dirigidas cuyos dos extremos, **tras resolver**, caen dentro de
esta nomina: `LD-02` (**D**) y `LD-03` (**A**). Cobertura medida: **10 de 15**.

**CIFRA discrepancias con el contraste del encargo en el 2.a: 0.** Las nueve
celdas cotejadas calzan al digito.

#### 2.b. LAS DOS CORRECCIONES, POR EL CARRIL DEL BANCO `9.10` Y POR ADICION PURA

**NO SE PISO NI UNA LINEA.** Las dos filas viejas siguen enteras y sin tachar,
y las dos nuevas se anaden detras de su tabla con su CORRECCION DECLARADA.

| que | donde queda hoy, remedido sobre el fichero de salida |
|---|---|
| la fila VIEJA de la tabla por nomina | linea **31** (entraba en la 31) |
| la fila VIEJA de que nominas cambian | linea **339** (entraba en la 291) |
| la fila NUEVA de la tabla por nomina | linea **79** |
| la fila NUEVA de que nominas cambian | linea **377** |

**LA VIEJA DE LA 291 SE MUEVE A LA 339 Y LA DE LA 31 SE QUEDA DONDE ESTABA, Y
LO DIGO EN VEZ DE DEJAR QUE PAREZCA UN PISOTON:** la primera adicion va
**debajo** de la fila 31 y **encima** de la 291, asi que la de abajo cambia de
numero. **El numero cambia; el texto, no**, y la guarda lo prueba.

**LA MARCA EN LA CELDA DE NOMBRE NO ES UNA ELECCION MIA:** es la adjudicacion
`6.5` del acta 208, y las dos filas nuevas llevan
**`(FILA CORREGIDA EN LA VUELTA 209)`**. El motivo esta medido en esa misma
adjudicacion: un lector que toma la primera fila que casa no distingue la vieja
de la nueva sin ella.

**LAS CUATRO GUARDAS DEL 2.b, LAS CUATRO CORRIDAS ANTES DE ESCRIBIR:**

- **(a) y (b):** cada ancla y cada fila vieja aparece **exactamente una vez**,
  y las lineas 31 y 291 se cotejaron **VERBATIM** contra su numero antes de
  tocar nada. **CIFRA guardas que fallan: 0.**
- **(c) EL CONTROL POSITIVO DE LA COLUMNA `fuera de cola`**, que es lo que
  impide computar una columna que no significa lo que se cree: sobre la fila
  VIEJA, *posibles menos leidos* tiene que dar *fuera de cola*, y da **CALZA**.
  Solo entonces se computa el **5** de la fila nueva con esa misma regla.
- **(d)** al terminar, **CIFRA lineas del texto de entrada que NO estan, en
  orden, en el de salida: 0**.

**LA SEDE, POR LAS DOS CONVENCIONES Y EN SUS DOS PUNTAS.** Entra en **214916**
bytes en disco y **214916** bytes normalizado a LF, con `sha256` disco **`dda1cdd67042c733`** y
`sha256` LF **`dda1cdd67042c733`**, que calza al digito con el contraste del encargo.
Sale en **219178** bytes en disco y **219178** bytes normalizado a LF, con `sha256`
disco **`a8ba1749b9a3fa13`** y `sha256` LF **`a8ba1749b9a3fa13`**.
**CIFRA crecimiento: 4262 bytes en disco y 4262 bytes normalizado a LF.**
`git diff --numstat` sobre esa sede da **78** anadidas y **0** borradas:
**CERO BORRADAS**, que es lo que el encargo exige.

**UNA CAIDA MIA, CAZADA ANTES DE PUBLICAR, Y VA MARCADA COMO `C.1`.** La
primera version del 2.b leia las cifras del fichero de salida **entero** con
una guarda de *exactamente una coincidencia*. **La guarda paso y la cifra salio
mal igual:** el patron de `fundidos` exigia una linea de detalle detras, la
seleccion de canal tiene **0** fundidos y por tanto **ninguna**, y la unica
coincidencia del fichero era **la de la JUNTA ASESORA, que tiene 2**. Iba a
publicar que la seleccion de canal tiene miembros fundidos cuando no tiene
ninguno. **Una guarda de unicidad sobre un fichero con dos nominas no es una
guarda de identidad**, y el arreglo no fue afinar el patron sino **acotar el
trozo** a su nomina, con una comprobacion de que el bloque de la otra queda
fuera. Va entera en la seccion 8.

#### 2.c. `OP-L-01` QUEDA CERRADA, Y SE DICE CON SUS DOS CUENTAS

**SU CRITERIO DE HECHO QUEDA CUMPLIDO.** `docs/plan/08_VERIFICACION.md`, fila
**06 MESAS**, linea **29**, pide *cada decision escrita con su motivo y su
cobertura al lado (banco 9.26)*, y con el 2.b hecho la decision de la mesa lleva
**la cobertura buena al lado**: **10 de 15, INCOMPLETA y por tanto PROVISIONAL**.
**Y SU VARA QUEDA EN 11 DE 11** por la adjudicacion `6.2` del acta 208: el banco
`9.26` **contempla lo PROVISIONAL en vez de prohibirlo** (*mientras falte un par,
la forma es PROVISIONAL y se dice asi*), asi que una cobertura de **10 de 15**
escrita como PROVISIONAL **CUBRE**.

**LAS TRES GUARDAS DEL ENCARGO, LAS TRES EN VERDE. VEREDICTO DEL INSTRUMENTO:
VERDE.**

**(1) EL VALOR VIEJO SE LEYO Y SE PUBLICA AL LADO DEL NUEVO:** el campo `estado`
de `OP-L-01` pasa de **`LISTA`** a **`HECHA`**, leidos los dos del fichero. La ficha
esta en la linea **41**, trae **18** campos, y **17 de 17** campos distintos del
`estado` **no se movieron**.

**EL VALOR NUEVO NO SE INVENTO.** `HECHA` ya es vocabulario del propio fichero:
lo llevaban **29** de las **71** fichas antes de tocar nada. Estrenar un valor
que no existiera en la sede seria doctrina nueva, y eso no lo decide el ejecutor.

**(2) LA SEDE, POR LAS DOS CONVENCIONES, ANTES Y DESPUES, CON SUS DOS `sha256`:**

| `docs/plan/OPERACIONES.jsonl` | bytes en disco y bytes normalizado a LF | `sha256` disco | `sha256` LF |
|---|---:|---|---|
| **ANTES** | **513043** y **513043** | **`829c583eb779cab6`** | **`829c583eb779cab6`** |
| **DESPUES** | **513043** y **513043** | **`e96dbe74485814e9`** | **`e96dbe74485814e9`** |

Los bytes no se mueven porque `LISTA` y `HECHA` miden lo mismo, **y los
`sha256` si cambian**, que es lo que prueba que algo se escribio. Los de ANTES
calzan al digito con el contraste del encargo y con mi sello de apertura.

**(3) UNA LINEA CAMBIADA Y NI UNA MAS, Y NINGUN OTRO `id_op` MOVIDO:**
`git diff --numstat` da **1** fichero tocado, **1** anadida y **1** borrada.
El censo de `id_op` y `estado` se cotejo **entero**, las **71** fichas contra las
**71**: **CIFRA fichas que se movieron: 1**, y es `OP-L-01`. **CIFRA otros
`id_op` cuyo estado cambio: 0.** El reparto pasa de **29** `HECHA` y **42**
`LISTA` a **30** y **41**.

**LA CIRUGIA FUE DE TEXTO, NO DE JSON, Y ESO ES LO QUE HACE POSIBLE LA GUARDA
(3).** Se sustituyo el par `estado` **dentro de su linea y solo ahi**, comprobado
que aparece exactamente una vez en ella. Volver a serializar el JSON reordenaria
claves o cambiaria espaciados y ensuciaria el `numstat` de las demas lineas, que
es justo lo que la guarda mide.

