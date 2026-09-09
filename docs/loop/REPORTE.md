# REPORTE DE LA VUELTA 214 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v214_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 213.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **TRES TAREAS, Y LA 214 NO ES VUELTA DE BATERIA.** La cadencia de cinco de
> `AUDITOR.md` 6.1 pone la bateria en la **215**, y la TAREA 3 de esta vuelta es
> justamente prepararla. **El tope de sub-tareas es CINCO** (acta 212,
> adjudicacion `6.8`, **linea 75168** de `docs/loop/ACTA_AUDITOR.md`, leida en
> esta vuelta), asi que las tres del encargo caben.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las tres tareas son trabajo de PLAN**, que
> es lo que la moratoria protege. Todo lo que esta vuelta escribe en el arbol
> scripts/loop (**sin comillas inversas, por la obligacion del `6.2` del acta
> 212**) son ficheros `_v214_*` **con prefijo de guion bajo, fuera del censo y
> fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
>
> **RIGE LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion `6.2`, **y es la `C.1` que esta vuelta no repite**); una seccion
> suplementaria va detras de la que amplia y nunca detras de una mayor (hallazgo
> `7.1`); y el tallador de cabecera corrido en la apertura escribe en un nombre
> con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V214_APERTURA.txt`,
> `docs/loop/SALIDA_V214_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 214`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LAS 95 SE DICEN, Y `OP-I-01` CIERRA (DECISION 1 del fundador). Marcar PROVISIONAL POR INSTRUMENTO, nunca a mano, exactamente las entradas de `docs/plan/INVENTARIO.jsonl` con forma N de M INCOMPLETA, con conteo ANTES y DESPUES; si el instrumento marca un numero distinto de 95, se PARA y se trae. Correccion DECLARADA citando el banco `9.26` y la decision del fundador POR SU RUTA. Y re-medir el punto 2 de `OP-I-01` a CUBRE, cerrando la ficha CON SU PRUEBA por la vara del expediente y su verificacion, SIN escribir el campo estado | **CERRADA Y ANEXADA** | `SALIDA_V214_T1_SIMULACION.txt`, `SALIDA_V214_T1_MUTANTES.txt`, `SALIDA_V214_T1_MARCAR_95.txt`, `SALIDA_V214_T1C_OP_I_01.txt`, `SALIDA_V214_T1C_EVIDENCIA.txt`, `SALIDA_V214_T1C_EVIDENCIA_MUT.txt`, `SALIDA_V214_T1_VARA.txt` |
| **TAREA 2** | LA VARA DE LAS TRES FASES (DECISION 2 del fundador). La tabla del criterio de HECHO de `docs/plan/08_VERIFICACION.md` gana sus filas para las fases 08, 09 y 10, DERIVADAS de las clausulas de verificacion que las propias fichas traen y cada fila CON SU CITA, por correccion declarada. Y las CINCO fichas sin ejecutar se re-miden contra esas filas con el resultado escrito ficha por ficha (`OP-V-01`, `OP-L-01`, `OP-L-02`, `OP-L-03`, `OP-I-01`), con la `OP-V-01` llevando su prueba POR CITA de la corrida K ya escrita | **CERRADA Y ANEXADA** | `SALIDA_V214_T2_SIMULACION.txt`, `SALIDA_V214_T2_MUTANTES.txt`, `SALIDA_V214_T2_VARA_TRES_FASES.txt`, `SALIDA_V214_T2B_REMEDIR_CINCO.txt` |
| **TAREA 3** | PREPARAR LA VUELTA 215, que es VUELTA DE BATERIA por la cadencia de cinco (`AUDITOR.md` 6.1) con la nomina CONGELADA EN 135 y por TRAMOS RESUMIBLES, y que lleva ademas el CIERRE INTEGRAL del bucle sin credencial: ciclo entero de Gate 0, las tres suites, el inventario de las 71 contra sus pruebas, y el marcador y el censo recomputados. La propuesta va EN ESTE REPORTE y no en la sede del auditor (doctrina de sedes del acta 203, ratificada por el fundador): el reparto de los tramos se COMPUTA con el lanzador y no se teclea, y la condicion de la PARA_ALEXIS.md de campaña consumada se deja escrita con su clausula de que NO se pide el merge | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LAS 95 SE DICEN, Y `OP-I-01` SE CIERRA POR SU PRUEBA

**LA DECISION QUE LO ORDENA, POR SU RUTA Y NO DE MEMORIA:**
`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, **DECISION 1**. **LA
DOCTRINA:** banco `9.26`, *"mientras falte un par, la forma es PROVISIONAL y se
dice asi"*, leido hoy en la **linea 2847** de `docs/BANCO_DE_TEXTOS.md`.

#### 1.a LAS 95, MARCADAS POR INSTRUMENTO Y NUNCA A MANO

**LA SEDE ES EL CAMPO `forma`, Y NO SE ELIGIO POR GUSTO:** el instrumento con que
la vuelta 203 midio ESTA MISMA CLAUSULA, `scripts/loop/_v203_t3_op_i_01.py`, mide
en su **linea 258** con `"PROVISIONAL" in (r.get("forma") or "")`. Escribir la
marca en otro campo habria dejado la clausula midiendo en rojo con el trabajo
hecho.

**EL CONTEO ANTES Y DESPUES, LEIDO DE `docs/loop/SALIDA_V214_T1_MARCAR_95.txt`:**

| que | ANTES | DESPUES |
|---|---:|---:|
| entradas del inventario | **672** | **672** |
| con cobertura de la forma N de M | **555** | **555** |
| de esas, INCOMPLETAS | **95** | **95** |
| **de esas incompletas, marcadas PROVISIONAL en `forma`** | **0** | **95** |
| entradas del fichero entero con PROVISIONAL en `forma` | 1 | 96 |
| entradas del fichero entero con PROVISIONAL en cualquier campo | 3 | 98 |
| bytes | 584554 | 629533 |
| sha256 | `69666b73339f2afe` | `43cea06634e6fc1a` |

**LA GUARDA DEL ENCARGO SE CUMPLIO SIN AJUSTAR NADA:** el encargo dice que si el
instrumento marca un numero distinto de **95** se para y se trae. **Midio
95 y calzo**, y la comprobacion esta escrita en la salida, no prometida
aqui.

**UNA CAIDA PROPIA, CAZADA POR MI SIMULACION ANTES DE ESCRIBIR NADA, Y LA
DECLARO: `D.1`.** Mi primera version re-volcaba cada linea con `json.dumps` por
defecto, y la simulacion la tumbo: **335 de las 672
lineas de este fichero estan volcadas con separadores COMPACTOS y las otras
337 con los de por defecto.** Un re-volcado ciego habria reformateado
**335 lineas que nadie mando tocar**, y el cotejo semantico lo
habria dado por bueno. **El remedio no fue elegir una convencion: fue medir la de
CADA linea probando cual reproduce su texto BYTE A BYTE antes de tocarla**, y
anadir al juicio una guarda de bytes sobre las lineas que no son de las 95.

**EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION**
(`docs/loop/SALIDA_V214_T1_MUTANTES.txt`): **6 mutantes y caen los
6**, con el texto bueno pasando el MISMO juicio en **0 fallos**.
**Y EL PRIMER MUTANTE SE CAYO DE VERDAD Y ERA MIO, `D.2`:** el mutante *A* quitaba
**una sola** aparicion de la palabra, y el texto de la marca la dice **dos veces**,
asi que la entrada seguia marcada y el mutante **PASABA**. **El defectuoso era el
mutante, no el juicio**, y es exactamente lo que la prueba de mutacion existe para
cazar. Corregido a quitar TODAS las apariciones, cae.

**EL ALCANCE, MEDIDO EN `git diff --numstat`:** `docs/plan/INVENTARIO.jsonl` sale
con **95 lineas modificadas, 0 altas y 0 bajas**. **Ninguna entrada COMPLETA gana
la marca**, el campo `cobertura` **no se toca** (la marca DICE la cobertura
incompleta, no la COMPLETA), y **el texto viejo de `forma` queda entero y delante
en las 95**.

#### 1.c LOS CUATRO PUNTOS DE `OP-I-01`, RE-MEDIDOS HOY Y NO COPIADOS

**Se re-miden LOS CUATRO y no solo el 2, por `EJECUTOR.md` 2:** los veredictos de
la vuelta 211 son de su corte y **entran como CONTRASTE**, nunca como fuente.
Salida: `docs/loop/SALIDA_V214_T1C_OP_I_01.txt`. **Filas armadas leyendo ese
fichero: 4, y los puntos de la ficha son 4.**

| punto | clausula, pegada de la ficha | 211 (contraste) | HOY (medido) | |
|---:|---|---|---|---|
| **1** | toda entrada lleva su fecha_corte | **CUBRE** | **CUBRE** | no se mueve |
| **2** | toda forma con cobertura incompleta va marcada PROVISIONAL | **NO CUBRE** | **CUBRE** | **SE MUEVE** |
| **3** | todo hueco va NOMBRADO, nunca rellenado | **A MEDIAS** | **A MEDIAS** | no se mueve |
| **4** | el inventario se recomputa entero con el disparador de 08_VERIFICACION | **A MEDIAS** | **A MEDIAS** | no se mueve |

**EL REPARTO DE HOY, CONTADO DE ESA TABLA: 2 en CUBRE, 2 en A
MEDIAS y 0 en NO CUBRE.** **CIFRA puntos que se mueven: 1**,
y es el **2**, de `NO CUBRE` a `CUBRE`.

**LA DISCREPANCIA CON EL ENCARGO SE DECLARA Y NO SE RESUELVE COPIANDO** (`EJECUTOR.md`
2 y 8). **El encargo y la DECISION 1 nombran el punto 2 como lo que bloquea, y el
punto 2 ya esta en CUBRE. PERO LOS PUNTOS 3 Y 4 SIGUEN EN A MEDIAS**, y no los
mueve esta vuelta ni los podria mover el marcado de las 95:

- **PUNTO 3:** su mitad pendiente es **una NEGATIVA** (*"nunca rellenado"*), y una
  busqueda negativa no se puede citar (`EJECUTOR.md` 9). La mitad que SI se mide
  da **119 entradas que nombran HUECO**. **No es trabajo que quede: es un
  limite de como esta escrita la clausula.**
- **PUNTO 4:** su mitad pendiente es **regenerar la vista humana**, y
  `docs/plan/10_INVENTARIO.md` declara en su **linea 19**, leida hoy, que **LA
  TABLA NO SE REGENERA AQUI, A PROPOSITO**. Es trabajo de la escala del
  disparador.

**NINGUNO DE LOS DOS ES `NO CUBRE` y ninguno lo levanta el bucle por su cuenta:
suben NOMBRADOS a la auditoria integral.**

#### 1.c LA PRUEBA DEL CIERRE, ESCRITA EN LA SEDE DE LA FICHA Y SIN TOCAR `estado`

**El encargo dice que la ficha NO escribe el estado y que se cierra por la vara y
por su verificacion. Asi se hizo:** la prueba entra como **UN ELEMENTO MAS de la
lista `evidencia`**, que es el carril que **esta misma ficha uso en la vuelta 201**
y la gemela `OP-L-01` en la **166**. Banco `9.10`, texto viejo entero y sin
tachar. La lista pasa de **4 a 5 elementos**.

**LO QUE LA GUARDA COMPROBO, y esta escrito en `docs/loop/SALIDA_V214_T1C_EVIDENCIA.txt`:**
cambia **exactamente una linea** del expediente y es la de `OP-I-01`; **de esa
ficha solo se mueve `evidencia`**; **el campo `estado` no se mueve en NINGUNA de
las 71 fichas**; los elementos viejos quedan **enteros y en su orden**; y **todas
las cifras del texto nuevo se leen de una salida sellada**, con las rutas que
promete comprobadas **existentes y de mas de cero bytes** antes de escribir
(`EJECUTOR.md` 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA). **Mutacion:
6 mutantes, caen los 6.**

**`numstat` sobre `docs/plan/OPERACIONES.jsonl`: 1 linea modificada, 0 altas y 0
bajas.**

#### LA VARA DEL EXPEDIENTE, CORRIDA POR MI EN ESTA VUELTA

`scripts/loop/vuelta150_3_relectura_expediente.py --corte 89c7bf23`, con el reloj
de git **congelado en el HEAD de apertura**. Salida:
`docs/loop/SALIDA_V214_T1_VARA.txt`. **Al abrir la vuelta seguia diciendo lo
mismo que en la 213: 1 ficha de trabajo real, y es `OP-I-01`.**

**Y AQUI VA UN DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO, `D.3`:** la vara
da por EJECUTADA una ficha por su prueba **P3**, que pide un commit cuyo mensaje
nombre el `id_op` **y que toque `scripts/`, `dataset/`, `engine/` o `web/`**. **El
commit de esta tarea nombra `OP-I-01` y toca `scripts/`**, porque ahi viven los
instrumentos de la vuelta. **Asi que la P3 va a dispararse.** Lo digo yo antes de
que lo mida nadie: **el trabajo real de esta ficha aterrizo en el arbol del plan, que
es justo lo que la P3 descuenta a proposito** (*"un commit que solo mueve `docs/`
esta anotando el plan, no corriendolo"*). **No toco la vara** (rige la moratoria)
y **no me apoyo en esa P3 para decir que la ficha cierra**: la ficha cierra por
sus cuatro puntos re-medidos y por su evidencia escrita. **Si el auditor entiende
que la P3 asi disparada es un falso verde, la cifra que hay que mirar es la de la
tabla de arriba y no la de la vara.**

**LO QUE ESTA TAREA NO HIZO, y lo digo para que no se busque:** no toco ni un
nodo, no movio ni un veredicto, no escribio en `docs/plan/08_VERIFICACION.md` (eso
es la TAREA 2), no regenero el inventario, no cambio ningun campo `estado` y no
declaro la campaña consumada.

**`numstat` del arbol entero al cerrar esta tarea: 2 fila(s), y las
2 del arbol del plan son las dos sedes de esta tarea.**

### TAREA 2. LA VARA DE LAS TRES FASES, ESCRITA Y USADA

**LA DECISION QUE LO ORDENA, POR SU RUTA:**
`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, **DECISION 2**. El acta
211 ya habia reservado estas filas al fundador en su `6.4`, y el acta 213 midio
en su `7.2` que la ausencia era **total y no parcial**.

#### 2.a LAS TRES FILAS, DERIVADAS Y NO INVENTADAS

**LO QUE SE ESCRIBIO ES ADITIVO Y NO TOCA UNA LETRA DE LA TABLA VIEJA:**
`numstat` sobre `docs/plan/08_VERIFICACION.md` da **33 0 docs/plan/08_VERIFICACION.md**, o sea **altas y
CERO bajas**. La guarda comprueba ademas, sobre el texto y no de palabra, que
**las 8 filas viejas siguen enteras** y que **no desaparece ni una linea del
fichero**.

**LA REGLA DE DERIVACION ES MECANICA Y NO ES DE OJO:** cada celda se **compone
concatenando los textos VERBATIM** de las clausulas de `verificacion` que las
propias fichas traen, y **el juicio cae si una celda trae texto que no salga de
una clausula**. Las clausulas de `OP-V-01` que **abren con el numero de una fase
que ya tiene fila** se excluyen, porque no son la vara de su fase sino la ficha
repitiendo filas que ya existen: **de sus 9 clausulas se excluyen 8 y queda 1**,
la transversal, que es la de la fase 08.

**LAS TRES CELDAS, CON SU CUENTA DE CLAUSULAS LEIDA DEL FICHERO:** la fila
**08** trae **1** clausula, la **09** trae **8** y
la **10** trae **4**.

**Y LAS CORRECCIONES DECLARADAS NO ENTRAN, POR EL REGISTRO `R.72` DEL ACTA 208**,
que separo las clausulas de vara de las correcciones declaradas diciendo que
estas **nunca fueron puntos de la vara**. Contadas de la salida, ficha por ficha:

| ficha | fase | clausulas de vara | correcciones declaradas | excluidas por tener fila ya |
|---|---|---:|---:|---:|
| `OP-V-01` | 08_VERIFICACION | 9 | 0 | 8 |
| `OP-L-01` | 09_LECTURAS_DIRIGIDAS | 3 | 4 | 0 |
| `OP-L-02` | 09_LECTURAS_DIRIGIDAS | 3 | 1 | 0 |
| `OP-L-03` | 09_LECTURAS_DIRIGIDAS | 3 | 1 | 0 |
| `OP-I-01` | 10_INVENTARIO | 4 | 0 | 0 |

**Cada fila de la tabla de derivacion que se escribio en el plan lleva su cita:
ficha, indice de la clausula y linea de `docs/plan/OPERACIONES.jsonl`. FILAS DE
DERIVACION ARMADAS: 14.**

**EL CASO ROJO, PROBADO POR MUTACION** (`docs/loop/SALIDA_V214_T2_MUTANTES.txt`):
**5 mutantes y caen los 5**, con el texto bueno pasando el
mismo juicio en **0 fallos**.

**UNA CAIDA PROPIA MAS, `D.4`, CAZADA POR MI EN LA SIMULACION:** mi primera
version leia los numeros de fase **de todo el fichero**, y este fichero tiene
muchas tablas: se tragaba **707, 1096, 2464 y mas** como si fueran fases. **No
cambiaba el resultado** (el 8, el 9 y el 10 no estaban entre ellos), **pero una
vara que acierta por suerte no es una vara**, asi que la lectura se acoto a la
tabla del criterio, de su cabecera a su ultima fila. Hoy da exactamente
**[0, 1, 2, 3, 4, 5, 6, 7]**.

**`docs/plan/OPERACIONES.jsonl` NO SE TOCA EN LA `2.a`, y esta probado con su
`sha256`, no prometido:** el mismo al entrar y al salir de la escritura.

#### 2.b LAS CINCO FICHAS, RE-MEDIDAS CONTRA ESAS FILAS

**Salida: `docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt`. La vara se LEE de
`docs/plan/08_VERIFICACION.md`, no se teclea: si aquella fila cambiara, esta
medicion cambiaria con ella.**

**LA HONESTIDAD DEL ALCANCE VA DELANTE:** no toda clausula de una vara es
mecanizable. Cada una se marca **MECANICA** (con su sonda corrida hoy y su cifra)
o **DOCUMENTAL**, y **para las documentales SE DECLARA QUE NO HAY CASO ROJO
AUTOMATICO**, en vez de fabricar una sonda que se apruebe sola.

| ficha | fase | clausulas suyas | con sonda mecanica | documentales |
|---|---|---:|---:|---:|
| OP-V-01 | 08_VERIFICACION | 1 | 1 | 0 |
| OP-L-01 | 09_LECTURAS_DIRIGIDAS | 3 | 2 | 1 |
| OP-L-02 | 09_LECTURAS_DIRIGIDAS | 3 | 1 | 2 |
| OP-L-03 | 09_LECTURAS_DIRIGIDAS | 3 | 0 | 3 |
| OP-I-01 | 10_INVENTARIO | 4 | 4 | 0 |

**CIFRA fichas re-medidas: 5. CIFRA clausulas repartidas:
14, de ellas 8 con sonda y 6
documentales, y la suma se comprueba contra si misma en la salida.**

**LAS CUATRO SONDAS, CON SU CIFRA DE HOY:**

- **EL MARCADOR DEL ARCHIVO: 3388 filas**, contadas hoy de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.
- **LOS PARES DE LECTURA DIRIGIDA: 27 cabeceras**, y de esos **PARES**,
  **0 tienen veredicto en el archivo**, o sea que **la clausula
  CALZA**: viven solo en su pagina.
- **LOS CUATRO PUNTOS DE `OP-I-01`**, citados de la TAREA 1 de esta misma vuelta:
  **2 CUBRE y 2 A MEDIAS**.
- **LOS CINCO PUNTOS TRANSVERSALES DE `OP-V-01`**, buscados uno a uno por su
  marca propia dentro de la `nota` de la ficha (**5105 caracteres**):
  **los cinco estan escritos**, y el commit que movio su estado, leido de la
  propia nota, es **`e966d896`**.

**LA `OP-V-01` VA POR PRUEBA POR CITA Y NO SE VUELVE A PRODUCIR LA CORRIDA K**,
tal como el encargo dice: es la **cuarta via** que la DECISION 5 del fundador del
4 sep 2026 autorizo **para esta ficha**. **Y se repite aqui lo que la propia nota
de la ficha ya dice, para que nadie lo lea como un verde que no es: esa prueba NO
cambia el veredicto de la vara del expediente, que sigue midiendo la ficha como
HECHA sin ninguna de sus tres pruebas.**

**DOS DISCREPANCIAS DECLARADAS, NI RESUELTAS NI TAPADAS:**

1. **`D.5`, EL MARCADOR.** La clausula escribe *"sigue en 2.117"* y el archivo mide
   **3388** hoy. **Leida a la letra NO CALZA.** Las dos lecturas van
   escritas y **no elijo yo**: la literal dice que no calza; la de su corte dice
   que la clausula pide que **esa operacion** no mueva el marcador, y el marcador
   se movio porque **el cribado siguio hasta cerrar**, no por la ficha. **Cual de
   las dos manda es doctrina que no esta escrita: va como PENDIENTE DE
   DOCTRINA** (`EJECUTOR.md` 5).
2. **`D.6`, LA CIFRA ONCE.** La clausula dice *"las once"* y la pagina trae
   **27** cabeceras hoy, porque siguio creciendo. **La clausula es de su
   corte y se dice, en vez de reescribirla.**

**UNA CAIDA PROPIA MAS, `D.7`, Y ES DE LAS QUE IMPORTAN:** mi primera sonda de los
pares preguntaba si **los dos NOMBRES** aparecian en el archivo, y eso da que si
para casi cualquier par del catalogo: **salia 27 de 27 y habria publicado una
alarma falsa contra una clausula que en realidad se cumple**. Corregida a comparar
**el PAR** contra los campos `nodo_a` y `nodo_b`, da **0** y la
clausula calza. **Una sonda mas laxa que su clausula no mide esa clausula.**

**LO QUE ESTA TAREA NO HACE:** la `2.b` **no escribe en el arbol del plan**, no
mueve ningun campo `estado`, no toca la vara del expediente y **no asciende
ninguna ficha**. **`numstat` del arbol del plan al cerrar: 1 fila(s).**

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

