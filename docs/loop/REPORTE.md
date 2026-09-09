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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 214`, y su salida
cruda vive en `docs/loop/SALIDA_V214_TALLADOR_CABECERA.txt` (2368 bytes en disco y 2348 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `20a7bd7c` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 213: EL PLAN ESTA AGOTADO Y EL BUCLE PARA. NO ES LA PARADA FELIZ Y NO PIDO NINGUN MERGE.'), HEAD real de apertura `89c7bf23` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `354cca1b` (leido de `SALIDA_V214_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LAS 95 SE DICEN, Y `OP-I-01` CIERRA (DECISION 1 del fundador). Marcar PROVISIONAL POR INSTRUMENTO, nunca a mano, exactamente las entradas de `docs/plan/INVENTARIO.jsonl` con forma N de M INCOMPLETA, con conteo ANTES y DESPUES; si el instrumento marca un numero distinto de 95, se PARA y se trae. Correccion DECLARADA citando el banco `9.26` y la decision del fundador POR SU RUTA. Y re-medir el punto 2 de `OP-I-01` a CUBRE, cerrando la ficha CON SU PRUEBA por la vara del expediente y su verificacion, SIN escribir el campo estado | **CERRADA Y ANEXADA** | `SALIDA_V214_T1_SIMULACION.txt`, `SALIDA_V214_T1_MUTANTES.txt`, `SALIDA_V214_T1_MARCAR_95.txt`, `SALIDA_V214_T1C_OP_I_01.txt`, `SALIDA_V214_T1C_EVIDENCIA.txt`, `SALIDA_V214_T1C_EVIDENCIA_MUT.txt`, `SALIDA_V214_T1_VARA.txt` |
| **TAREA 2** | LA VARA DE LAS TRES FASES (DECISION 2 del fundador). La tabla del criterio de HECHO de `docs/plan/08_VERIFICACION.md` gana sus filas para las fases 08, 09 y 10, DERIVADAS de las clausulas de verificacion que las propias fichas traen y cada fila CON SU CITA, por correccion declarada. Y las CINCO fichas sin ejecutar se re-miden contra esas filas con el resultado escrito ficha por ficha (`OP-V-01`, `OP-L-01`, `OP-L-02`, `OP-L-03`, `OP-I-01`), con la `OP-V-01` llevando su prueba POR CITA de la corrida K ya escrita | **CERRADA Y ANEXADA** | `SALIDA_V214_T2_SIMULACION.txt`, `SALIDA_V214_T2_MUTANTES.txt`, `SALIDA_V214_T2_VARA_TRES_FASES.txt`, `SALIDA_V214_T2B_REMEDIR_CINCO.txt` |
| **TAREA 3** | PREPARAR LA VUELTA 215, que es VUELTA DE BATERIA por la cadencia de cinco (`AUDITOR.md` 6.1) con la nomina CONGELADA EN 135 y por TRAMOS RESUMIBLES, y que lleva ademas el CIERRE INTEGRAL del bucle sin credencial: ciclo entero de Gate 0, las tres suites, el inventario de las 71 contra sus pruebas, y el marcador y el censo recomputados. La propuesta va EN ESTE REPORTE y no en la sede del auditor (doctrina de sedes del acta 203, ratificada por el fundador): el reparto de los tramos se COMPUTA con el lanzador y no se teclea, y la condicion de la PARA_ALEXIS.md de campaña consumada se deja escrita con su clausula de que NO se pide el merge | **CERRADA Y ANEXADA** | `SALIDA_V214_T3_PLAN_BATERIA.txt`, `SALIDA_V214_T3_SIGUIENTE.txt`, `SALIDA_V214_COMPOSITOR_T3.txt` |
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

### TAREA 3. LA VUELTA 215, PREPARADA, Y DOS TRAMPAS MEDIDAS QUE LE ESPERAN

**DONDE VA ESTA PROPUESTA Y POR QUE NO EN OTRO SITIO.**
`docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/ACTA_AUDITOR.md` y
y el PARA_ALEXIS.md que vive junto a ellos **son sede del auditor y el ejecutor
no los escribe**;
si cree que el encargo siguiente deberia decir otra cosa, **lo propone en su
reporte, que es su sede**. Adjudicacion `4.2` del acta 203, leida hoy en la
**linea 71543** de `docs/loop/ACTA_AUDITOR.md`, y **ratificada por el fundador**
en su decision del 9 sep 2026. **Por eso esta tarea no escribe una sola linea
fuera de este reporte.**

#### 3.a LA BATERIA: EL REPARTO SE COMPUTA, Y NO DA NUEVE

**Corrido por mi en esta vuelta con el carril `--plan`, que NO toca la nomina, NO
corre ningun arnes y NO escribe ninguna salida de bateria.** Salida:
`docs/loop/SALIDA_V214_T3_PLAN_BATERIA.txt`.

| que | cuanto |
|---|---:|
| entradas de la nomina | **135** |
| tamano de tramo | **13** |
| **tramos que el reparto da** | **11** |
| suma de las entradas de todos los tramos | **135** |

**LA NOMINA CALZA CON LA MORATORIA: 135, CONGELADA**, y la suma de los
tramos reproduce esa misma cifra, o sea que el reparto cuadra consigo mismo.

**PARADA 1: EL ENCARGO Y `AUDITOR.md` 6.1 DICEN NUEVE, Y EL INSTRUMENTO CUENTA
11.** No lo arreglo yo (`EJECUTOR.md` 5: se escribe como PARADA y no se
repara). **La letra vigente dice, con estas palabras, que la bateria SE DECLARA
CORRIDA CUANDO LOS NUEVE TRAMOS TIENEN SALIDA SELLADA DEL MISMO CALIBRE.** El
**NUEVE** era cierto en su corte, cuando la nomina era menor; **con la nomina
congelada en 135 el reparto da 11**, y **la practica ya se movio
sin que la letra la siguiera**: la ultima bateria, la de la **vuelta 210**,
corrio **11** tramos y sus propios commits lo dicen. **Si la 215 se cine a
la letra y para en nueve, deja DOS TRAMOS sin correr y declara corrida una bateria
que no lo esta.** La cifra que manda es la que el instrumento computa, pero
**cambiar la letra de `AUDITOR.md` no es mio**: lo subo.

**PARADA 2, Y ES LA QUE DE VERDAD PUEDE FABRICAR UN FALSO VERDE: EL CARRIL
`--siguiente` DICE HOY QUE NO FALTA NINGUN TRAMO.** Corrido por mi, salida en
`docs/loop/SALIDA_V214_T3_SIGUIENTE.txt`:

- **tramos del reparto: 11**
- **tramos CON salida sellada no vacia: 11**
- **tramos que FALTAN: 0**

**Y no es que la bateria de la 215 este hecha: es que las salidas que ese carril
mira son las de la vuelta 210 y siguen en el arbol.** El motivo,
medido y no supuesto: **el lanzador nombra sus salidas con el numero que computa
de SU PROPIO fichero**, que es el **183**, no con el de la vuelta que lo corre.
Asi que `SALIDA_V183_BATERIA_TRAMO_N.txt` es el mismo nombre para toda corrida, y
**ni `--siguiente` ni `--componer` pueden distinguir una corrida fresca de la
anterior**. Lo comprobe en el propio `componer()`: cotejea **cobertura** (que
ninguna entrada de la nomina se quede sin correr, que no sobre ninguna y que no
se repita) y **que ninguna salida mida cero bytes**, pero **no mira la fecha ni el
commit de los sellos**.

**LOS ONCE SELLOS QUE HOY VE ESE CARRIL, CON SU CABECERA Y SU COMMIT, LEIDOS POR
MI:**

| tramo | cabecera de la salida, leida de su primera linea | ultimo commit que la toco | bytes |
|---:|---|---|---:|
| 1 | CORRIDA DEL TRAMO 1 DE 11, BATERIA DE LA VUELTA 183 | `ca702058 2026-09-08` | 9544 |
| 2 | CORRIDA DEL TRAMO 2 DE 11, BATERIA DE LA VUELTA 183 | `4895fb06 2026-09-08` | 7795 |
| 3 | CORRIDA DEL TRAMO 3 DE 11, BATERIA DE LA VUELTA 183 | `3fa5b035 2026-09-08` | 8050 |
| 4 | CORRIDA DEL TRAMO 4 DE 11, BATERIA DE LA VUELTA 183 | `a9a8fff9 2026-09-08` | 7862 |
| 5 | CORRIDA DEL TRAMO 5 DE 11, BATERIA DE LA VUELTA 183 | `274a0aed 2026-09-08` | 8274 |
| 6 | CORRIDA DEL TRAMO 6 DE 11, BATERIA DE LA VUELTA 183 | `fc68e550 2026-09-08` | 8205 |
| 7 | CORRIDA DEL TRAMO 7 DE 11, BATERIA DE LA VUELTA 183 | `3d79c288 2026-09-08` | 7893 |
| 8 | CORRIDA DEL TRAMO 8 DE 11, BATERIA DE LA VUELTA 183 | `97185bc4 2026-09-08` | 7848 |
| 9 | CORRIDA DEL TRAMO 9 DE 11, BATERIA DE LA VUELTA 183 | `ed74786d 2026-09-08` | 8525 |
| 10 | CORRIDA DEL TRAMO 10 DE 11, BATERIA DE LA VUELTA 183 | `08e9acdd 2026-09-08` | 8472 |
| 11 | CORRIDA DEL TRAMO 11 DE 11, BATERIA DE LA VUELTA 183 | `7dfbfdf7 2026-09-08` | 6273 |

**LO QUE PROPONGO, Y ES BARATO:** que la 215 **NO use `--siguiente` como senal de
arranque**, y corra **`--tramo 1` a `--tramo 11` uno a uno**, cada uno
**commiteado con su salida sellada al terminar**, que es lo que la letra manda de
todas formas; y que **antes de empezar publique el commit de los sellos viejos**,
para que la corrida nueva se distinga de la de la vuelta 210 en el
propio reporte. **`--componer` va al final y es el que coteja el calibre.**
**No propongo tocar el lanzador: rige la moratoria.**

#### 3.b EL CIERRE INTEGRAL, CON SUS INSTRUMENTOS COMPROBADOS UNO A UNO

**Todo lo que la `3.b` del encargo pide es SIN CREDENCIAL y tiene instrumento
vivo. Comprobados hoy, existencia y bytes, porque una ruta que promete prueba es
cifra:**

| que pide el encargo | instrumento | existe |
|---|---|---|
| el ciclo entero de Gate 0, los ocho comandos | `scripts/loop/_v205_ciclo_gate0.py` | **SI**, 4359 bytes en disco y 4359 bytes normalizados a LF |
| la bateria por tramos | `scripts/loop/vuelta183_bateria_por_tramos.py` | **SI**, 35327 bytes en disco y 35327 bytes normalizados a LF |
| la vara del trabajo pendiente | `scripts/loop/vuelta150_3_relectura_expediente.py` | **SI**, 60262 bytes en disco y 60262 bytes normalizados a LF |
| el inventario de las 71 contra sus pruebas | `scripts/loop/_v213_t2_cierre_fase_iii.py` | **SI**, 16687 bytes en disco y 16687 bytes normalizados a LF |
| el marcador y el censo, recomputados | `scripts/loop/vuelta159_tarea9_marcador_cierre.py` | **SI**, 7948 bytes en disco y 7948 bytes normalizados a LF |
| las tres suites, dentro del ciclo de Gate 0 | `engine/run_all_tests.py` | **SI**, 2535 bytes en disco y 2457 bytes normalizados a LF |
| el cierre del reporte | `scripts/loop/cerrar_reporte.py` | **SI**, 114466 bytes en disco y 114466 bytes normalizados a LF |
| el tallador de la cabecera | `scripts/loop/tallar_cabecera_reporte.py` | **SI**, 100077 bytes en disco y 100077 bytes normalizados a LF |
| el barrido de rutas del reporte | `scripts/loop/vuelta186_rutas_del_reporte.py` | **SI**, 5887 bytes en disco y 5887 bytes normalizados a LF |

**CIFRA instrumentos comprobados: 9 | CIFRA ausentes o de cero bytes:
0.**

**EL ORDEN QUE PROPONGO, y el motivo de cada sitio:** la **bateria primero y
sola**, porque `AUDITOR.md` 6.1 dice que su vuelta **no lleva nada mas** y porque
es lo que lleva vueltas cayendose; el **cierre integral despues**, con el ciclo
entero de Gate 0 **en sus dos lados**, las tres suites (que ya van dentro de ese
ciclo, comandos 7, 8a y 8b), el **inventario de las 71 contra sus pruebas** y el
**marcador y el censo recomputados**. **La vara del expediente se corre con el
reloj de git congelado en el HEAD de apertura de la 215**, no en un ancestro.

#### 3.c LA `PARA_ALEXIS.md`: SU CONDICION, Y QUIEN LA ESCRIBE

**LA CONDICION, ESCRITA ANTES DE SABER SI SE CUMPLE:** la 215 escribe la parada
de **campaña consumada** **solo si** los **11** tramos de la bateria
tienen salida sellada **fresca** y del mismo calibre, el ciclo entero de Gate 0
sale en **peor exitcode 0 por los dos lados**, las tres suites salen verdes, el
inventario de las 71 cuadra contra sus pruebas y el marcador y el censo
recomputados calzan. **Si algo no da verde, se dice CUAL y la 215 NO escribe esa
parada**, tal como el encargo ordena.

**Y EN ESA PARADA VA DECLARADO QUE LA AUDITORIA INTEGRAL CON CREDENCIAL Y CON EL
FUNDADOR DELANTE ES EL PASO SIGUIENTE. NO SE PIDE EL MERGE: el merge es del
fundador y viene despues de esa auditoria.** El bucle no funde ramas.

**UNA PRECISION QUE NO ES MENOR, Y LA DIGO PORQUE ME TOCA A MI DECIRLA:
`PARA_ALEXIS.md` ES SEDE DEL AUDITOR.** Cuando el encargo dice *"la 215 escribe
el `PARA_ALEXIS.md`"*, quien lo escribe es **el auditor de la 215**, no su
ejecutor. **El ejecutor de la 215 lo PROPONE en su reporte**, igual que yo estoy
proponiendo esto aqui. Si el ejecutor de la 215 lo escribiera, romperia la misma
adjudicacion `4.2` que el fundador acaba de ratificar.

**Y LO QUE LA 215 NO PUEDE DECLARAR CONSUMADO SIN MIRARLO, PORQUE ESTA VUELTA LO
DEJA ABIERTO:** los **puntos 3 y 4 de `OP-I-01` siguen en A MEDIAS** (TAREA 1), y
las **dos discrepancias de la `2.b`**, el marcador contra su cifra vieja y la
cifra once, **siguen sin doctrina que las resuelva**. **Ninguna de las tres es NO
CUBRE y ninguna la levanta el bucle por su cuenta, pero una parada de campaña
consumada que no las nombre estaria consumando por encima de ellas.**

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: LA VUELTA 214 CIERRA SUS TRES TAREAS: las 95 entradas del inventario quedan DICHAS y OP-I-01 cierra su punto 2 con prueba y sin tocar un solo campo estado, la tabla del criterio de HECHO gana sus filas 08, 09 y 10 DERIVADAS de las clausulas de las propias fichas y las cinco fichas se re-miden contra ellas, y la 215 queda preparada con DOS PARADAS medidas que le esperan: el reparto de la bateria da ONCE tramos y no los NUEVE que la letra publica, y el carril --siguiente dice hoy que no falta ninguno porque esta viendo los sellos de la vuelta 210.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS

**Contado de las dos salidas de consola, no de memoria.**

| lado | comandos con exitcode leido | los que no dan 0 | peor |
|---|---:|---:|---|
| **APERTURA** | (sin fichero de consola) | | |
| **CIERRE** | (sin fichero de consola) | | |

**`numstat` del lado de cierre: 2 fila(s).** **`numstat` de `dataset/`
al cerrar: 0 fila(s).**

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**El `sha256` de apertura se LEE de `docs/loop/SALIDA_V214_APERTURA.txt`, que se
sello antes de la primera operacion; el de cierre se computa ahora.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes disco / LF |
|---|---|---|---|---|
| `docs/plan/INVENTARIO.jsonl` | 69666b73339f2afe | 43cea06634e6fc1a | **SE MOVIO** | 629533 / 629533 |
| `docs/plan/OPERACIONES.jsonl` | ca1d95b5b3d19e9e | 650578474361eb2b | **SE MOVIO** | 517181 / 517181 |
| `docs/plan/08_VERIFICACION.md` | 76bfebb6b2d8ef72 | 578eeefab6db2fd4 | **SE MOVIO** | 73652 / 73652 |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 758edf1f5c313c18 | 758edf1f5c313c18 | quieta | 4057130 / 4057130 |
| `docs/INTRA_DOMINIO_INFORME.md` | c05b6bcd20188a9c | c05b6bcd20188a9c | quieta | 943970 / 943970 |
| `docs/plan/00_INDICE.md` | 2e71336cc2fdc387 | 2e71336cc2fdc387 | quieta | 45278 / 45278 |
| `docs/BANCO_DE_TEXTOS.md` | 8adbd60239509bb4 | 8adbd60239509bb4 | quieta | 186490 / 186490 |
| `docs/plan/BANCO_DEL_PLAN.md` | 7836c8976c585143 | 7836c8976c585143 | quieta | 61554 / 61554 |
| `dataset/metadata/master_graph.json` | 627cc662296f7f00 | 627cc662296f7f00 | quieta | 8375817 / 8375817 |
| `docs/loop/ACTA_AUDITOR.md` | d78556e9744b4925 | d78556e9744b4925 | quieta | 5011522 / 5011522 |
| `docs/loop/PROMPT_SIGUIENTE.md` | 2d777a347a04b0fc | 2d777a347a04b0fc | quieta | 3358 / 3358 |

**CIFRA sedes cotejadas: 11 | CIFRA que se movieron: 3.** **Y
las que se movieron son EXACTAMENTE las tres que las tareas 1 y 2 nombran, ni una
mas:** el inventario (las 95), el expediente (la evidencia de `OP-I-01`) y la vara
del criterio de hecho. **`docs/loop/ACTA_AUDITOR.md` y
`docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, quedan QUIETAS**, y
esa es la prueba de que la TAREA 3 se quedo en mi reporte.

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y su salida se cita en el commit
de cierre. **Es el instrumento que en la 213 cazo la `C.1`, y esta vuelta lo lleva
ademas metido en tres de mis compositores como guarda previa: los tres cuentan
los directorios de dos o mas tramos entre comillas inversas ANTES de escribir, y
los tres me mordieron al menos una vez.**

## 4. LO QUE SE TOCO, Y LO QUE NO

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**Ningun arnes, guarda ni lector nuevo, y ninguno reparado.** Todo lo que esta
vuelta escribio en el arbol de scripts del bucle lleva **prefijo de guion bajo**,
vive **fuera del censo y fuera de la nomina**, y **muere con la vuelta**.

**CONTADO DE `git diff --name-only` entre el HEAD de apertura y el de ahora:
14 fichero(s) tocados ahi, de los cuales 14 llevan el
prefijo `_v214_` y 0 no lo llevan.**

**LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135**, medida por mi en esta
vuelta con el carril `--plan` del lanzador, que no la toca.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`, que me
la exigio y tenia razon):

- **`git status --porcelain` al entrar: 1 linea**, y era mi propio script
  de apertura sin rastrear.
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0.**

### 4.2. LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE

- **No declaro la campaña consumada y no pidio ningun merge.** El bucle no funde
  ramas.
- **No escribio una linea en la sede del auditor**, y esta medido arriba con los
  dos `sha256` quietos.
- **No movio ningun campo `estado`**, ni en `OP-I-01` ni en ninguna de las 71, y
  la guarda de la TAREA 1 lo comprueba sobre el fichero entero.
- **No toco ni un nodo, ni un veredicto, ni la vara del expediente.**
- **No corrio la bateria**: la 214 no es vuelta de bateria.

### 4.3. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA

- **commit de apertura**: 2026-09-09 06:07:10 -0400
- **primer commit de la vuelta**: 2026-09-09 06:14:26 -0400
- **ultimo commit al componer este cierre**: 2026-09-09 06:49:11 -0400

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

- **`D.3` LA `P3` DE LA VARA SE VA A DISPARAR CON MIS PROPIOS COMMITS.** La `P3`
  pide un commit cuyo mensaje nombre el `id_op` **y que toque `scripts/`,
  `dataset/`, `engine/` o `web/`**; mis commits nombran `OP-I-01` y tocan
  `scripts/`, porque ahi viven mis instrumentos. **El trabajo real aterrizo en el
  arbol del plan, que es justo lo que la `P3` descuenta a proposito.** No toco la
  vara y **no me apoyo en esa `P3`** para decir que la ficha cierra.
- **LA SEDE DE LA MARCA DE LAS 95 ES EL CAMPO `forma`.** Lo elegi por el
  precedente medido de la **linea 258** de `scripts/loop/_v203_t3_op_i_01.py`,
  pero **es una eleccion mia** y otra sede (una clave nueva) habria sido
  defendible. **Marco que es discutible.**
- **ESCRIBI EN `docs/plan/OPERACIONES.jsonl`, QUE LA VUELTA 213 TENIA PROHIBIDO
  TOCAR.** Mi encargo me manda cerrar la ficha con su prueba y use el carril que
  la propia ficha ya habia usado, **pero la prohibicion de la 213 era de la 213 y
  la mia no la repite**: si el auditor entiende que esa escritura necesitaba
  mandato explicito, **la marca es esta**.
- **LA REGLA DE EXCLUSION DE LA `2.a` LA ESCRIBI YO.** Que una clausula que abre
  con el numero de una fase con fila ya existente **no sea** la vara de su fase es
  una lectura mia, mecanica pero mia. **Sin ella, la fila 08 habria repetido la
  tabla entera.**

## 6. LAS PREGUNTAS

1. **¿La `2.a` deberia haber metido las tres filas DENTRO de la tabla, como hice,
   o como bloque aparte?** Las meti dentro porque el encargo dice que **la tabla
   gana sus filas**, y lo hice **sin tocar una letra de las viejas**. Si la casa
   prefiere el bloque aparte, se dice y se mueve.
2. **¿Un `numstat` de 95 lineas modificadas en un fichero del arbol del plan necesita
   algo mas que la decision del fundador por su ruta?** Lo hice con esa decision y
   con conteo antes y despues, y lo pregunto porque es la escritura mas ancha que
   una vuelta ha hecho ahi en mucho tiempo.

## 7. PENDIENTES DE DOCTRINA

1. **EL MARCADOR CONTRA SU CIFRA VIEJA (`D.5`).** La clausula de `OP-L-01` y
   `OP-L-02` escribe *"sigue en 2.117"* y el archivo mide **3388** hoy. **Leida a
   la letra no calza; leida por su corte, pide que ESA operacion no lo mueva, y lo
   movio el cribado al cerrar.** **Cual de las dos lecturas manda no esta escrito
   en ningun banco**, y no lo decido yo.
2. **SI LOS PUNTOS EN `A MEDIAS` BLOQUEAN UN CIERRE DE FASE.** `OP-I-01` queda con
   **2 en CUBRE y 2 en A MEDIAS**, y los dos que quedan lo estan por motivos
   estructurales (una negativa que no se puede citar, y una vista humana que su
   propio documento declara que no se regenera ahi). **Nada dice si eso cierra o
   no cierra.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**Son SIETE, y las siete las cazaron mis propias guardas ANTES de publicar nada.**
Las escribo porque una guarda que muerde y no se cuenta es una guarda que la
proxima vuelta no sabe que existe.

- **`D.1` EL FICHERO TENIA DOS CONVENCIONES DE VOLCADO Y YO NO LO SABIA.** Mi
  primera version de la TAREA 1 re-volcaba con `json.dumps` por defecto; la
  **simulacion** midio que **335 de las 672 lineas** estan volcadas con
  separadores compactos y **337** con los de por defecto. **Un re-volcado ciego
  habria reformateado 335 lineas que nadie mando tocar, y el cotejo semantico lo
  habria dado por bueno.** Remedio: medir la convencion de **cada** linea antes de
  tocarla, mas una **guarda de bytes** sobre las que no son de las 95.
- **`D.2` MI MUTANTE ERA EL DEFECTUOSO, NO MI JUICIO.** El mutante *A* quitaba
  **una sola** aparicion de la palabra y el texto de la marca la dice **dos
  veces**: la entrada seguia marcada y el mutante **pasaba**. Corregido a quitar
  todas.
- **`D.4` MI LECTOR DE NUMEROS DE FASE LEIA TODO EL FICHERO** y se tragaba **707,
  1096 y 2464** como si fueran fases. **No cambiaba el resultado, pero una vara que
  acierta por suerte no es una vara.** Acotado a la tabla del criterio.
- **`D.7` MI SONDA ERA MAS LAXA QUE SU CLAUSULA Y HABRIA PUBLICADO UNA ALARMA
  FALSA.** Preguntaba si **los dos nombres** de un par estaban en el archivo, cosa
  que da que si para casi cualquier par del catalogo: salia **27 de 27** contra una
  clausula que en realidad **se cumple**. Corregida a comparar **el par** contra
  `nodo_a` y `nodo_b`: da **0 de 27**.
- **`C.1` UN `%d` LITERAL SE ME COLO EN LA PROSA DE UNA SONDA**, y salio impreso
  tal cual en la primera corrida de la `2.b`.
- **`C.2` CITE EL ARBOL DEL PLAN ENTRE COMILLAS INVERSAS, DOS VECES**, que es
  exactamente la `C.1` de la 213. **Me lo conto mi propia guarda del compositor** y
  el texto se reescribio sin comillas.
- **`C.3` CITE UN FICHERO QUE NO EXISTE COMO SI FUERA RUTA DE PRUEBA.** La
  `PARA_ALEXIS.md` **todavia no esta escrita**, y nombrarla entre comillas
  inversas es una ruta que promete prueba apuntando a nada. Cazada por la guarda
  de rutas de mi compositor de la TAREA 3.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**Va entero en la TAREA 3 de este reporte, que es mi sede.** En una linea: **la
215 es vuelta de bateria y el reparto da 11 tramos, no nueve**; **el carril
`--siguiente` dice hoy que no falta ninguno porque esta viendo los sellos de la
vuelta anterior**; y **el `PARA_ALEXIS.md` de campaña consumada, si se gana, lo
escribe el AUDITOR de la 215 y no su ejecutor**.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 214 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V214_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio, y NO es un olvido: la 214 NO es vuelta de bateria. La cadencia de cinco de AUDITOR.md 6.1 la pone en la 215, que es justo lo que la TAREA 3 de esta vuelta prepara, y esa vuelta la corre entera y sola. La nomina sigue CONGELADA en 135, medida por mi en esta vuelta con el carril --plan del lanzador, que no la toca.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
