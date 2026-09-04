### TAREA 3, EL MANTENIMIENTO DE LA BATERIA, Y UN ROJO QUE SOBREVIVE Y SE TRAE

**Salidas:** `docs/loop/SALIDA_V168_BATERIA.txt` (la corrida entera) y
`docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt` (la re corrida sellada al cierre).
**Instrumento:** `scripts/loop/verificar_mutaciones_viejas.py`.

**(3.a) LOS SEIS ARNESES DE LAS VUELTAS 166 Y 167 ENTRAN A LA NOMINA**, mas los
que nacen hoy. La cifra que lo prueba no es una afirmacion mia: la recomputa la
propia bateria al cierre y la publica. **`CIFRA arneses POSTERIORES a la nomina
que se quedan FUERA (recomputado al cierre): 0`**, contra los **6** que el acta
167 midio en su hallazgo 4.5. Y **`CIFRA entradas de la nomina que el censo NO
VE: 0`**, o sea que la nomina sigue siendo visible a su propio censo.

**(3.b) EL ANCLA DE `vuelta165_tarea6_mutacion_op_l_01.py` PASA DE TRES A CINCO
CLAUSULAS, Y NO SE AFLOJA AL HACERLO.** La vuelta 166 anadio `V4` y `V5` a
`OP-L-01` **por adicion** y el acta 166 lo adjudico bien en su `6.8`; el arnes se
quedo atras porque la bateria no se corrio en dos vueltas. El caso sigue siendo
una **igualdad exacta** contra el conteo real de la ficha, asi que vuelve a caer
en rojo si alguien anade o quita una clausula sin declararlo: **cambia el numero,
no el filo**. Y se le anaden **dos invariantes que el numero solo no da**: que
**2 de las 5** sean `CORRECCION DECLARADA` y que **las 3 viejas sigan enteras**,
para que reescribir la ficha borrando el texto viejo caiga aunque el conteo
siguiera dando cinco. Corrido: **16 casos pasan y los 16 caen al mutar**, exit 0.

**(3.c) LA BATERIA, RE CORRIDA ENTERA, Y SU SALIDA PEGADA.** Cifras contadas de
`docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt`:

| lo que mide la bateria | cifra al cierre de la 168 | cifra del acta 167 |
|---|---:|---:|
| arneses cronometrados (la nomina) | **72** | 62 |
| ANCLA PERDIDA | **0** | 0 |
| NO MORDIO | **1** | **2** |
| NO REPRODUCIBLE | **0** | 0 |
| CASO DECLARADO (los dos de siempre, con su marca) | **2** | 2 |
| arneses posteriores FUERA de la nomina | **0** | **6** |
| entradas de la nomina invisibles al censo | **0** | (no publicada) |
| RUIDO DE CONCURRENCIA | **0** | 0 |

**LOS DOS ROJOS DEL ACTA 167 ESTAN ARREGLADOS Y SE MIDE QUE LO ESTAN:**
`vuelta163_tarea2_mutacion_nomina.py`, que mordia los seis fuera de la nomina,
sale hoy **exit 0 OK**; y `vuelta165_tarea6_mutacion_op_l_01.py`, re anclado,
tambien.

**PERO LA BATERIA NO SALE EN VERDE, Y ESO ES LO PRIMERO QUE ESTA FILA DICE.**
El encargo pedia verde y ordena que, si un rojo sobrevive, **se traiga sin
aflojar la guarda**. Sobrevive uno, y **no es de los dos que el encargo mandaba
arreglar: es un TERCERO que la primera corrida completa en tres vueltas destapo.**

**EL ROJO QUE SE TRAE: `vuelta166_tarea3_mutacion_retrato.py`, exit 1 NO MORDIO,
3 casos de 23 fallan.** Diagnosticado corriendolo solo, no supuesto:

| caso que cae | real | esperado |
|---|---|---|
| `B_con_13_tachadas_el_siguiente_es_TRECE` | `CATORCE VECES` | `TRECE VECES` |
| `B_mutar_la_palabra_no_mueve_el_computo` | `CATORCE VECES` | `TRECE VECES` |
| `B_la_guarda_CAE_con_el_contador_desincronizado` | `True` | `False` |

**LA CAUSA, MEDIDA: ES LA MISMA ESPECIE QUE EL 3.b, Y POR ESO NO SE TOCA SIN
ORDEN.** El arnes lee la fila de los colapsos del documento VIVO y cuenta sus
tachadas (`cuantas`), pero su valor esperado es la **CONSTANTE LITERAL**
`"TRECE VECES"`. La vuelta 167, en su TAREA 4, anadio una tachada mas por el
carril del banco 9.10, cosa que el acta 167 verifico y dio por buena; con eso el
computo pasa a `CATORCE` y la constante se queda en `TRECE`. **La guarda muerde
algo cierto: que la campana movio su sujeto. No esta rota.**

**POR QUE NO LO ARREGLO YO, con la letra delante.** El encargo autoriza re
anclar **uno** (`3.b`, nombrado por su fichero) y ordena que lo que sobreviva
**se traiga**. Re anclar un arnes que el encargo no nombra seria decidir por mi
cuenta que su sujeto se movio legitimamente, y esa es justo la lectura que el
auditor tiene que hacer. **El remedio esta escrito y no lo aplico**: la
constante `"TRECE VECES"` tiene que salir del conteo, igual que `cuantas`, y el
`t.replace("DOCE VECES,", ...)` de su segundo caso tambien esta clavado al texto
vivo. **Marcado como DISCUTIBLE.**
