# REPORTE DE LA VUELTA 168 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION.** Es la
> regla nueva de `EJECUTOR.md` 1 ("EL REPORTE ABRE CON LA VUELTA", decision del
> fundador del 4 sep 2026) estrenandose sobre si misma. El esqueleto lo tallo
> `scripts/loop/vuelta168_esqueleto_reporte.py` antes de la primera tarea;
> cada tarea ANEXA SU FILA AL CERRARSE, no al final; y el cierre talla la
> cabecera. **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se
> hizo, y las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.** Tope de cinco tareas por vuelta, y el encargo trae exactamente
> cinco.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar. Un veredicto escrito en la apertura seria justo la especie
que esta regla existe para matar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta168_esqueleto_reporte.py`, que la busca con
`git rev-parse --abbrev-ref HEAD` y con `git log` y CAE EN ROJO si no la
encuentra o si es ambigua:

- rama: `pasada-unica`
- commit del acta de la vuelta 167: `e3152a9c`, asunto real leido de git log:
  'ACTA DE LA VUELTA 167 DEL AUDITOR Y PARADA: OP-C-01 NO SE PUEDE EJECUTAR PORQUE ESTA EJECUTADA, Y NO ES UN CASO SUELTO. 37 DE 71 FICHAS NO CALZAN Y LA CAIDA ES MIA'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V168_HEAD_APERTURA.txt`: `edbc1a48`
- commit de nacimiento del bloque de apertura y commit de cierre: se tallan al
  cierre. **Un reporte no puede nombrar el commit que lo lleva**, porque ese
  commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla de
comprobaciones sale de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 168`, cuya columna
derecha se lee de las salidas `SALIDA_V168_*_CIERRE.txt`. En la apertura esas
salidas no existen, y el tallador, corrido hoy, lo dice sin adorno: **"ROJO, 19
celdas no se pudieron leer y NO se talla nada"**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS: el acta 167 en `R.37`, y la nota adosada al `R.36` | **CERRADA** | `SALIDA_V168_T1_REGISTRO_ACTA_167.txt`, `SALIDA_V168_T1_NOTA_R36.txt`, `SALIDA_V168_T1_MUTACION_NOTA_R36.txt` |
| **TAREA 2** | EL REPORTE QUE CUBRE LAS VUELTAS 166 Y 167 | **CERRADA** | `SALIDA_V168_T2_RECONSTRUCCION_166_167.txt`, `SALIDA_V168_T2_MUTACION_RECONSTRUCTOR.txt` |
| **TAREA 3** | EL MANTENIMIENTO DE LA BATERIA (3.a nomina, 3.b re anclaje, 3.c corrida entera) | **CERRADA CON UN ROJO QUE SE TRAE** | `SALIDA_V168_BATERIA.txt`, `SALIDA_V168_T3_BATERIA_CIERRE.txt` |
| **TAREA 4** | `OP-V-01` POR LA DECISION 5, VERIFICADA CONTRA GIT | **CERRADA** | `SALIDA_V168_T4_OP_V_01.txt`, `SALIDA_V168_T4_MUTACION_OP_V_01.txt` |
| **TAREA 5** | ABRIR LAS SEIS POR LA VARA DEL INSTRUMENTO (5.a, 5.b valvula, 5.c depende_de) | **CERRADA, CON DOS CLAUSULAS QUE SE TRAEN** | `SALIDA_V168_T5_LAS_SEIS.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
### TAREA 1, LOS REGISTROS: `R.37`, Y LA NOTA ADOSADA AL `R.36`

**Salidas:** `docs/loop/SALIDA_V168_T1_REGISTRO_ACTA_167.txt` (la escritura del
`R.37`), `docs/loop/SALIDA_V168_T1_NOTA_R36.txt` (la nota adosada) y
`docs/loop/SALIDA_V168_T1_MUTACION_NOTA_R36.txt` (su caso positivo).
**Instrumentos:** `scripts/loop/vuelta168_tarea1_registrar_acta167.py`,
`scripts/loop/vuelta168_tarea1_adosar_nota_r36.py` y el arnes
`scripts/loop/vuelta168_tarea1_mutacion_registro.py`.

**LAS CIFRAS, CONTADAS DE SU FICHERO DE SALIDA Y NO TECLEADAS.** Cada una sale
de `docs/loop/SALIDA_V168_T1_REGISTRO_ACTA_167.txt`, en la seccion que se
nombra al lado:

| lo que se midio | cifra | de que seccion de la salida sale |
|---|---:|---|
| adjudicaciones `6.n` del acta 167 | **6** (6.1 a 6.6) | B |
| caidas propias del auditor, seccion 3 del acta | **2** | C |
| cuerpo del acta 167 acotado, `ACTA_AUDITOR.md` | **lineas 55.644 a 56.057** | A |
| entradas de la serie ANTES de escribir | **28** | E |
| colisiones y huecos de la serie | **0 y 0** | E |
| numero libre, computado y no tecleado | **`R.37`** | E |
| entradas de la serie DESPUES de escribir | **29** | K |

**EL REPARTO POR VIA, DE LA SECCION I DE LA MISMA SALIDA:** `SIN TOCAR NADA` 3
(6.1, 6.2, 6.3); `EN MEDICION` 2 (6.4, 6.5); `AL FUNDADOR, YA CONTESTADA` 1
(6.6). **Y LA LINEA DEL FUNDADOR DEJA DE SER UNA FRASE FIJA:** el `R.36` decia
*"Ninguna de las nueve sube al fundador"* porque el acta 166 no subia ninguna;
el acta 167 SI sube su `6.6` con la palabra *"lo subo"*, asi que en este
instrumento esa frase **se computa del reparto**. Si estuviera tecleada, la
herencia la habria arrastrado mintiendo.

**LAS DOS CIFRAS DEL TITULO SE MOVIERON EN SENTIDOS OPUESTOS, Y ES LA MEJOR
PRUEBA DE QUE NO ESTAN TECLEADAS:** el `R.36` registro **nueve** adjudicaciones
y **una** caida; el `R.37` registra **seis** y **dos**. La concordancia del
titulo cambia sola de la rama del singular a la del plural.

**EL CASO POSITIVO POR MUTACION DEL REGISTRADOR:** `34 casos pasan tal cual y
los 34 caen al mutar el esperado`, exit 0, corrido por el arnes de nombre propio
que la bateria ve.

**LA NOTA ADOSADA AL `R.36`, Y LO QUE LA HACE DISTINTA DE UNA GLOSA MAS: LOS
CUATRO VEREDICTOS SE MIDIERON CONTRA GIT, NO SE COPIARON DEL ACTA.** Cifras de
`docs/loop/SALIDA_V168_T1_NOTA_R36.txt`, secciones B, C y E:

| glosa del `R.36` | la medicion de hoy | ocurrio |
|---|---|---|
| `6.1` y `6.3`: el reporte de la 167 cubre las dos vueltas | `git show e3152a9c:docs/loop/REPORTE.md` da primera linea **VUELTA 165** | **NO** |
| `6.4`: la bateria de verdad se corre en esa vuelta | `SALIDA_V167_BATERIA.txt` en ese arbol mide **0 bytes** | **NO** |
| `6.9`: EJECUTADA EN EJECUCION, TAREA 5 | ultimo commit del ejecutor antes del acta: `3d0277d3`, *"TAREA 5: PARADA..."* | **NO** |

**4 de 4 no ocurrieron**, y la cifra sale del conteo de los veredictos, no de la
adjudicacion. **NINGUNA PALABRA VIEJA SE BORRO Y EL INSTRUMENTO LO COMPRUEBA
SOLO:** la seccion E dice `el cuerpo viejo del R.36 sigue ENTERO dentro del
nuevo: SI`, **32 lineas anadidas y 0 borradas**, porque la escritura es una
insercion. **Su caso positivo por mutacion:** `14 casos pasan tal cual y los 14
caen al mutar el esperado`, exit 0, y **el veredicto de cada glosa es una
variable computada**: alimentado con un sujeto fabricado donde el reporte SI es
el de la 167 y la bateria trae 4.000 bytes, el mismo codigo dice que las cuatro
ocurrieron. **Si la medicion hubiera dicho que ocurrieron, el instrumento NO
habria escrito la nota y lo habria declarado**, que es lo contrario de dar por
buena una adjudicacion sin comprobarla.

**LO QUE ESTA TAREA NO HACE:** no reabre el `R.36`, no mueve ninguna clase del
cribado, no toca ningun `estado` y no borra una linea.

### TAREA 2, EL REPORTE QUE CUBRE LAS VUELTAS 166 Y 167

**Salidas:** `docs/loop/SALIDA_V168_T2_RECONSTRUCCION_166_167.txt` (la
reconstruccion) y `docs/loop/SALIDA_V168_T2_MUTACION_RECONSTRUCTOR.txt` (su caso
positivo). **Instrumento:**
`scripts/loop/vuelta168_tarea2_reconstruir_166_167.py`.

**LA DEUDA, MEDIDA Y NO RECORDADA.** Las dos vueltas terminaron sin escribir su
reporte, y esta tarea lo comprueba en vez de creerlo: la seccion F de la salida
dice, para el arbol del acta 166 Y para el del acta 167, que la primera linea de
`docs/loop/REPORTE.md` era *"# REPORTE DE LA VUELTA 165"*. **Dos vueltas
seguidas, y la misma cabecera heredada en las dos.**

**LAS DOS VUELTAS, CONTADAS DE SU FICHERO DE SALIDA.** Cada celda sale de
`docs/loop/SALIDA_V168_T2_RECONSTRUCCION_166_167.txt`, secciones A, C y D:

| | **vuelta 166** | **vuelta 167** |
|---|---:|---:|
| commit que la abre (acta anterior, leido de git) | `00cfe6e0` | `7028a76a` |
| commit que la cierra (su propia acta) | `7028a76a` | `e3152a9c` |
| commits del corredor, acta incluida | **9** | **6** |
| de ellos, commits del ejecutor | **8** | **5** |
| tareas con commit propio | **6** | **4** |
| lineas anadidas | **8.886** | **7.754** |
| lineas quitadas | **181** | **199** |
| rutas distintas tocadas | **83** | **71** |
| rutas bajo `dataset/` | **0** | **0** |
| rutas bajo `web/` | **0** | **0** |
| rutas bajo `docs/plan/` | **3** | **1** |
| escribio su `REPORTE.md` | **NO** | **NO** |

**LAS CERO RUTAS BAJO `dataset/` Y BAJO `web/` SON LA CIFRA QUE MAS DICE:** en
las dos vueltas **no se toco ni un nodo ni una arista ni una linea de la web**.
Todo lo que se movio fue documentacion, instrumentos y salidas.

**LAS TAREAS, UNA POR UNA, CON SU COMMIT (seccion C de la salida).** Vuelta 166:
`TAREA 1` `2ee2592a`, `TAREA 2` `a23509cf`, `TAREA 3` `33fe1380`, `TAREA 4`
`6c38fb39`, `TAREA 5` `9363c1ba`, `TAREA 6` `0a0e658f`, mas su bloque de
apertura `8472d645` y su bloque de cierre `0f7d5bb2`. Vuelta 167: `TAREA 1`
`a6b318ca`, `TAREA 3` `12053ade`, `TAREA 4` `c6ac70f6`, `TAREA 5` `3d0277d3`
(parada), mas su bloque de apertura `b08543eb`. **LA 167 NO TIENE `TAREA 2` NI
BLOQUE DE CIERRE, y el hueco se ve en la propia lista de commits**: su TAREA 2
era el reporte.

**EL VEREDICTO DEL AUDITOR SOBRE CADA UNA, LEIDO DE SU ACTA Y MARCADO COMO
SUYO** (seccion E; es de otra sede y por eso no se mezcla con lo de arriba):

- **166** (`docs/loop/ACTA_AUDITOR.md:55297`): *"LAS SEIS TAREAS DE LA 166 ESTAN
  ENTREGADAS Y REPRODUCEN TODAS BAJO MIS INSTRUMENTOS, PERO LA VUELTA SE CORTO
  ANTES DE ESCRIBIR SU REPORTE Y ANTES DE QUE LA BATERIA TERMINARA."*
- **167** (`docs/loop/ACTA_AUDITOR.md:55653`): *"LAS CUATRO TAREAS QUE LA 167
  ENTREGO REPRODUCEN TODAS AL DIGITO BAJO MIS INSTRUMENTOS, SU QUINTA ENTREGA
  UNA PARADA QUE ES CORRECTA, Y LA SEGUNDA NO SE ENTREGO."*

**LAS CIFRAS DE TAREAS DE ESTA TABLA Y LAS DE LOS DOS VEREDICTOS COINCIDEN, Y SE
DICE PORQUE PODRIAN NO HABERLO HECHO:** 6 y 4, medidas por mi de los asuntos de
los commits, contra "las seis tareas" y "las cuatro tareas" del auditor, medidas
por el en su vuelta. **Dos manos y dos metodos dan lo mismo.**

**LO QUE NO SE PUEDE RECONSTRUIR, DECLARADO Y NO RELLENADO (seccion G, 4 cosas).**
Ninguna de estas cuatro vive en un commit ni en un acta, asi que **no se
escriben**:

1. **LOS DISCUTIBLES MARCADOS de cada vuelta.** Un discutible se marca ANTES de
   saber si se acierta. Hoy las dos actas ya publicaron su veredicto, asi que
   cualquier lista escrita ahora seria una copia con la respuesta delante.
2. **LAS PREGUNTAS de cada vuelta.** Fabricarlas hoy seria inventar el estado
   mental de una sesion cerrada.
3. **LOS PENDIENTES DE DOCTRINA que las dos vueltas hubieran levantado.** Solo
   se conocen los que llegaron a una sede escrita.
4. **EL VEREDICTO DE UNA LINEA del ejecutor de cada vuelta.** Escribirlo hoy
   seria escribir el del auditor con otra letra.

**UNA CIFRA MIA QUE ESTUVO MAL Y LA CAZO MI PROPIO ARNES ANTES DE PUBLICARSE, y
se declara en vez de taparse:** al escribir los casos puse **8 y 5 commits** de
memoria, de un `git log --oneline -8` truncado. El arnes midio **9 y 6**, porque
el corredor que este instrumento define llega hasta el acta INCLUSIVE. **No
llego a ninguna salida sellada ni a ninguna tabla**; la correccion vive escrita
en el comentario del propio instrumento, junto al caso, sin borrar el motivo.
**Caso positivo por mutacion: 17 casos pasan tal cual y los 17 caen al mutar el
esperado, exit 0.** El contador de tareas se probo ademas sobre corredores
fabricados en memoria, incluido uno cuyo asunto NOMBRA una tarea sin abrirla
(*"ACTA: la TAREA 5 quedo en parada"*), que el instrumento no cuenta.

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

### TAREA 4, `OP-V-01` POR LA DECISION 5: HAY PRUEBA, Y LA FICHA NO VUELVE A PENDIENTE

**Salidas:** `docs/loop/SALIDA_V168_T4_OP_V_01.txt` y
`docs/loop/SALIDA_V168_T4_MUTACION_OP_V_01.txt`. **Instrumento:**
`scripts/loop/vuelta168_tarea4_op_v_01.py`.

**EL HASH NO SE RECIBIO DEL ENCARGO: SE BUSCO.** El encargo nombra `e966d896` y
ordena *"VERIFICALO TU TAMBIEN"*, asi que el instrumento recorre los commits que
tocan `docs/plan/OPERACIONES.jsonl` y compara la ficha contra la de su padre
hasta encontrar el que cambia el campo. Cifras de la seccion A de la salida:

| lo que se midio | cifra |
|---|---|
| commits que MUEVEN el estado de `OP-V-01` en toda la historia | **1**, `e966d896`, `LISTA -> HECHA` |
| commits que la HACEN NACER, contados aparte | **1**, `c891b3ff`, `(nace) -> LISTA` |
| hash del encargo contra hash medido | `e966d896` contra `e966d896`, **COINCIDEN** |
| los cinco puntos transversales en el cuerpo del commit medido | **5 de 5 PRESENTES** |

**LOS CINCO PUNTOS SE BUSCARON POR SU MARCA PROPIA Y NO POR SU ORDEN** (seccion
C): Gate 0 con su ciclo entero y `26 en OK`; las tres suites (`motor 25/25`,
`1.040 pasadas`, `tsc exitcode 0`); el vuelo `16 de 16` en la `corrida K`; la
`PRUEBA DE RUMBOS` `SIN DERIVA`; y el reindexado con `d70adc1d` y `42223fcc`.
**Si faltara uno, el instrumento paraba y la ficha volvia a pendiente**, que es
lo que la decision 5 manda. No falto ninguno.

**LO ESCRITO, Y ES CORTO A PROPOSITO** (seccion E). La ficha **YA TRAIA** la
corrida K y los dos sellos: los escribio el propio commit del fundador. Lo que
**no traia**, y es exactamente lo que el hallazgo 4.4 del acta 167 declaro no
haber verificado, es **que commit movio el estado**. Eso es lo que se adosa:
**1.711 caracteres anadidos, de 3.394 a 5.105; la nota vieja sigue ENTERA dentro
de la nueva (comprobado por el instrumento, no afirmado); 71 fichas antes y 71
despues; 18 claves, el esquema no crece; y el estado NO se movio.**

**Y LA NOTA DICE ALGO MAS, QUE ES LO QUE LE IMPIDE SER UN FALSO VERDE: LA FICHA
SIGUE SIN CALZAR CON EL INSTRUMENTO, Y SE DECLARA.** Escribir la prueba por cita
**no cambia** el veredicto de `vuelta150_3_relectura_expediente.py`, que en esta
misma vuelta sigue midiendo `OP-V-01` como **HECHA SIN NINGUNA PRUEBA** (medido
en la TAREA 5: `CIFRA fichas HECHA sin ninguna prueba: 1`). **Y EL INSTRUMENTO NO
SE TOCA PARA QUE CAMBIE.** Sus tres pruebas son grafo, codigo vivo y huella en
git con rutas `dataset/`, `web/` o `engine/`, y `e966d896` toca `docs/` y
`examples/`, medido con `git show --numstat`. **La prueba por cita es una CUARTA
via que la decision del fundador autoriza para esta ficha, no una de las tres.**
Aflojar el instrumento para que la fila se pusiera verde habria sido la
degradacion callada que el canon 9 del banco prohibe. **Marcado como
DISCUTIBLE.**

**EL CASO POSITIVO POR MUTACION: 16 casos pasan tal cual y los 16 caen al mutar
el esperado**, exit 0. El veredicto de los cinco puntos es variable computada:
alimentado con cuerpos fabricados, el mismo codigo da 5, 4, 3 y 0 segun lo que el
cuerpo traiga.

**UNA CIFRA MIA QUE ESTUVO MAL Y LA CAZO EL ARNES, declarada y no tapada:** puse
que habia **1** movimiento de estado y el arnes midio **2**. No era la ficha, era
mi vara: contaba el NACIMIENTO (`None -> LISTA`, en `c891b3ff`) como movimiento.
Se arreglo **en la fuente**, separando las dos poblaciones y publicando las dos,
que es mas exacto que antes y no mas laxo. El motivo queda escrito en el
comentario del instrumento.

### TAREA 5, LAS SEIS ABIERTAS POR LA VARA DEL INSTRUMENTO

**Salida:** `docs/loop/SALIDA_V168_T5_LAS_SEIS.txt`. **Instrumento:**
`scripts/loop/vuelta168_tarea5_abrir_las_seis.py`, que **no reimplementa la vara:
invoca** `scripts/loop/vuelta150_3_relectura_expediente.py` y lee su salida.
**Cero nodos tocados, cero estados movidos, cero fichas editadas por esta tarea.**

**LA VARA, CORRIDA EN ESTA VUELTA** (seccion 0), comando pegado al lado:
`python scripts/loop/vuelta150_3_relectura_expediente.py --corte edbc1a48
--apertura 36bafc1a`, exit 0.

| lo que mide el instrumento | cifra de hoy | cifra del acta 167 |
|---|---:|---:|
| fichas del expediente | **71** | 71 |
| fichas que NO CALZAN | **37** | 37 |
| congeladas DECLARADAS | **24** | 24 |
| congeladas EN SILENCIO | **12** | 12 |
| `HECHA` sin ninguna prueba | **1** | 1 |
| `LISTA` sin ninguna prueba de ejecucion | **6** | 6 |

**LAS SEIS SE LEYERON DE LA SALIDA DEL INSTRUMENTO, NO DE UNA LISTA MIA**, y el
instrumento nombra: `OP-L-01`, `OP-L-02`, `OP-L-03`, `OP-I-01`,
`OP-M-02-MEDIOS`, `OP-M-02-ADMIT`. **MISMO CONJUNTO que el encargo: SI.** Si
hubieran discrepado, el instrumento paraba.

**5.b LA VALVULA DE VIGENCIA, CORRIDA ANTES DE TOCAR NADA, Y LAS DOS SALEN
CUMPLIDAS POR CONSUNCION.** La medicion **no se copio de la nota de las fichas**
(que la traen desde la vuelta 64): se re corrio hoy con
`scripts/loop/vuelta64_consumidas.py`, porque una nota vieja es contraste y nunca
fuente.

| ficha | sus dos miembros resueltos contra el grafo de HOY | veredicto |
|---|---|---|
| `OP-M-02-MEDIOS` | `seis_medios_comunicacion_cliente` DEPRECADO va a `estrategia_multicanal_bienvenida`, que esta VIVO: **UN solo vivo** | **CUMPLIDA POR CONSUNCION, NO SE EJECUTA** |
| `OP-M-02-ADMIT` | `fase_admit` DEPRECADO va a `fase_admit_celebracion`, que esta VIVO: **UN solo vivo** | **CUMPLIDA POR CONSUNCION, NO SE EJECUTA** |

**QUIEN CONSUMIO EL ACTO, CON SU LINEA:** `OP-U-01` TRAMO 3, vuelta 56, acto 32,
lote B, `docs/plan/03_FUSIONES.md` **linea 2091** para MEDIOS; y `OP-U-01` TRAMO
2, vuelta 55, acto 38, lote B, **linea 1840** para ADMIT. **Las cinco
`OP-M-02-*` resuelven a un solo vivo (5 de 5).** Y la valvula publica ademas lo
que ninguna de las dos fichas puede tapar: **DIVERGEN**, porque cada ficha
adjudico el 12 ago 2026 el superviviente OPUESTO al que el tramo dejo vivo. **Eso
no se deshace y no se copia: se declara**, como ya hizo la vuelta 64.

**5.c LOS `depende_de`, LEIDOS POR EL INSTRUMENTO Y NO POR EL CAMPO.** El
encargo avisa: *"Si el instrumento dice otra cosa, paras y lo traes."* **No dice
otra cosa.**

| `OP-D-*` | estado (CAMPO, historico) | pruebas (INSTRUMENTO) | por la vara nueva |
|---|---|---|---|
| `OP-D-01` | LISTA | P2+P3a | **CUMPLIDA** |
| `OP-D-02` | LISTA | P1+P2+P3a | **CUMPLIDA** |
| `OP-D-03` | LISTA | P3a | **CUMPLIDA** |
| `OP-D-04` | LISTA | P2+P3a | **CUMPLIDA** |
| `OP-D-05` | LISTA | P1+P3a | **CUMPLIDA** |
| `OP-D-06` | LISTA | P3a | **CUMPLIDA** |

**6 de 6 con prueba, 0 sin prueba**, asi que **`OP-L-02` y `OP-L-03` dejan de
estar bloqueadas**. **Y LA DIFERENCIA ENTRE LAS DOS VARAS SE PUBLICA EN VEZ DE
DISIMULARSE:** por el campo `estado` las seis siguen en `LISTA`, y la seccion
3.c del propio instrumento, que **lee el campo**, no las lista como
desbloqueadas. Es exactamente el caso que la decision del fundador zanja.

**5.a `OP-I-01`, ABIERTA Y MEDIDA CLAUSULA A CLAUSULA.** No escribe nada en el
grafo (0 elementos entre `nodos`, `preservar`, `eliminar` y `aristas_nuevas`).
El inventario de hoy, contado de `docs/plan/INVENTARIO.jsonl`: **672 entradas**
(556 actos, 54 familias de ids, 20 figuras, 19 defectos, 13 racimos, 10
dominios), en **4 fechas de corte** (11 ago = 323, 12 ago = 11, 13 ago = 337, 14
ago = 1).

- **CLAUSULA 1**, *toda entrada lleva su `fecha_corte`*: **SE CUMPLE**, 0
  entradas sin corte.
- **CLAUSULA 2**, *toda forma con cobertura incompleta va marcada PROVISIONAL*:
  **NO ES MEDIBLE POR CONTEO Y SE DICE en vez de darla por buena.** Se pueden
  contar las **2** que SI estan marcadas; para saber si estan TODAS haria falta
  la lista de las incompletas, y el inventario no la trae como campo.
- **CLAUSULA 3**, *todo hueco va NOMBRADO, nunca rellenado*: **119** entradas
  nombran un hueco, y la nota de la ficha nombra los suyos.
- **CLAUSULA 4**, *el inventario se recomputa entero con el disparador de
  `08_VERIFICACION`*: **ESTA ES LA QUE NO SE PUEDE EJECUTAR SIN DECIDIR.** La
  nota de la ficha declara **335 actos (280 CERRADOS, 55 ABIERTOS)** al corte
  3.388, medidos en la vuelta 14. **Medido hoy sobre
  `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`: 332 lineas, 278 CERRADOS, 54
  ABIERTOS.** **La discrepancia se declara y NO se resuelve copiando.** Y se
  dice de donde viene, trazada commit a commit con `git show` sobre ese fichero:
  **335 en `7f4ec6d9`** (vuelta 11), **334 en `7cec9ecc`**, **333 en
  `97552714`**, **332 en `70878328`** (vuelta 40, `OP-D-05`), cada bajada
  declarada en el asunto de su propio commit. **La cifra de la nota no es falsa:
  es de su corte.** Lo que no existe es **un instrumento que regenere el
  inventario**: sus dos formas se escribieron a mano entre las vueltas 17 y 20, y
  la ficha no escribe el procedimiento. **Recomputarlo entero hoy exigiria
  decidir su alcance**, y `AUDITOR.md` 3 dice que una operacion cuyo texto no
  alcanza para ejecutarse sin decidir es **PARADA, no una improvisacion**.

**5.a `OP-L-01`, ABIERTA Y MEDIDA CLAUSULA A CLAUSULA.** 5 clausulas, 2 de ellas
`CORRECCION DECLARADA` de la vuelta 166; no escribe nada en el grafo.

- **CLAUSULA 1: CERRADA** por la correccion de la vuelta 166, verificada por el
  acta 166 y adjudicada en su `6.8`. No se reabre.
- **CLAUSULA 2: CERRADA** por la correccion de la vuelta 166: el `2.117` es
  **TESTIGO de su corte, no condicion**. Medido hoy, contado del fichero, el
  marcador vale **3.388**.
- **CLAUSULA 3**, *cada nomina afectada se re-mide con su cobertura al lado
  (banco 9.26)*: **SIGUE ABIERTA, y con la medicion delante.** Para re-medir
  *"cada nomina afectada"* hay que saber cuales son, y la ficha no las escribe:
  sus cuatro listas de escritura estan **vacias**. La sede que nombra miembros es
  el inventario, o sea `OP-I-01`, cuya clausula 4 acaba de quedar declarada no
  ejecutable sin decidir. **La cadena es real y no una excusa: sin inventario
  recomputado no hay nomina que re-medir.**

**EL SALDO DE LAS SEIS, CONTADO:** **2 cumplidas por consuncion y no
ejecutadas** (`OP-M-02-MEDIOS`, `OP-M-02-ADMIT`); **2 desbloqueadas por la vara
nueva y no ejecutadas en esta vuelta** (`OP-L-02`, `OP-L-03`); **2 abiertas,
medidas clausula a clausula y con su ultima clausula bloqueada por la misma
cadena** (`OP-I-01` clausula 4, `OP-L-01` clausula 3). **Ninguna se cierra
declarandola cerrada, y ninguna se improvisa.**

<!-- FIN ANEXO DE TAREAS -->
