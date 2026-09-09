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
