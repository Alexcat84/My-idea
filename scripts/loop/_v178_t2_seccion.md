### TAREA 2. `OP-L-03`: EL BACKLOG SE RE-MIDE ENTERO ANTES DE LEER UN ACTO MAS

**LO QUE SALE, DICHO PRIMERO PORQUE CAMBIA EL TAMANO DE LO QUE QUEDA: DE LOS 73
PARES QUE EL INSTRUMENTO DA, SOLO 18 SON REALES. SOBRAN 55, QUE ES EL 75,3 POR
CIENTO.** Y de los **34 actos que la 177 no miro, quedan 10 pares reales**, no 44.

#### 2.a. EL INSTRUMENTO VIEJO NO SE TOCA, Y ESO CONTESTA MI `P.2`

`scripts/loop/backlog_l03_vuelta14.py` **no se modifico en esta vuelta**, y esta
comprobado y no afirmado: `git diff --stat` sobre esa ruta sale **vacio**. Es el
instrumento que la nota de la ficha cita y el que sostiene la cifra ADJUDICADA EN
LA VUELTA 15. **Cambiarlo cambiaria esa cifra por la puerta de atras.**

#### 2.b. EL FILTRO VA DELANTE, EN FICHERO PROPIO Y DE NOMBRE ESTABLE

Nace `scripts/loop/backlog_l03_resuelto.py`, **sin numero de vuelta**, como sus
hermanos de nombre estable. Corre el instrumento viejo **como subproceso** y le
pone encima el resolutor de `P.1`, el `mapa_de_alias()` de
`scripts/loop/vuelta166_tarea2_correccion_op_l_01.py`. **PUBLICA LAS DOS COLUMNAS
AL LADO, NUNCA UNA SOLA**, que es la forma de la correccion declarada del banco
9.10 aplicada a un instrumento: la cifra vieja no se borra, se le pone la nueva al
lado con su procedencia.

#### 2.c. LO QUE PUBLICA, POR ACTO Y EN TOTAL

**Contado de `docs/loop/SALIDA_V178_T2_BACKLOG_RESUELTO.txt` y pegado de ahi.**

| cifra | valor |
|---|---|
| actos que el instrumento da | **40** |
| pares POSIBLES entre los miembros escritos | **202** |
| PARES QUE EL INSTRUMENTO DA (la cifra vieja, que NO se borra) | **73** |
| pares DISUELTOS (los dos extremos en el mismo nodo tras resolver) | **134** |
| pares que YA TIENEN VEREDICTO, buscados por el par RESUELTO | **47** |
| PARES REALES (la cifra nueva, al lado de la vieja) | **18** |
| actos SIN NINGUN PAR REAL | **29 de 40** |

**Los dos caminos van SIEMPRE los dos** (`EJECUTOR.md` 9): el resolutor de `P.1`
(761 alias sobre 3.853 ficheros de `dataset/nodos/`) y el campo `deprecado` del
grafo (3.853 nodos, 3.169 vivos). La tabla por acto trae las dos columnas para los
**40** actos, y esta entera en el fichero de salida.

**LOS SEIS ACTOS GRANDES, que son los que la 177 leyo:**

| acto | miembros | vivos por resolutor | vivos por grafo | calzan | pares del instrumento | pares reales | disueltos |
|---|---|---|---|---|---|---|---|
| `breakthrough_desempeno_actual` | 6 | 1 | 1 | SI | 8 | **0** | 15 |
| `cierre_segun_complejidad_venta` | 6 | 1 | 1 | SI | 6 | **0** | 15 |
| `cash_burn_calculation` | 5 | 5 | 5 | SI | 4 | 4 | 0 |
| `construccion_de_leverage` | 5 | 5 | 5 | SI | 3 | 3 | 0 |
| `encuadre_desafio_diseno` | 5 | 1 | 1 | SI | 6 | **0** | 10 |
| `estrategia_de_innovacion_arenas` | 5 | 4 | 4 | SI | 2 | **1** | 1 |

#### 2.d. EL ROJO DE LOS DOS CAMINOS, Y QUE DIO HOY

**CAE EN ROJO si los dos caminos no calzan en algun acto, nombrandolo.** Hoy:
**40 actos medidos, 40 calzan, 0 no calzan.** Y el rojo **no es decorativo**: su
arnes le da un grafo fabricado que MIENTE (un alias marcado como vivo) y la fila
sale **NO CALZAN**, o sea que la comprobacion muerde.

#### 2.e. EL CASO POSITIVO POR MUTACION, SOBRE UN MAPA FABRICADO

`scripts/loop/vuelta178_tarea2_mutacion_resolutor.py`,
`docs/loop/SALIDA_V178_T2_MUTACION.txt`. **12 casos, los 12 pasan y los 12 CAEN**
al mutarles el esperado. **Nada sale del repo**: ni `dataset/nodos/`, ni el grafo,
ni `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`. La mutacion que manda va en los dos
sentidos:

| el caso | pares reales |
|---|---|
| acto de 3 miembros CON el alias puesto (colapsan a uno) | **0**, y los 3 disueltos |
| el MISMO acto SIN el alias | **3**, y 0 disueltos |

**Si quitar el alias no cambiara la cifra, el resolutor no estaria puesto** y este
instrumento seria un `combinations()` con adornos.

**Y EL ARNES TUMBO UN DEFECTO REAL DEL INSTRUMENTO EN SU PRIMERA CORRIDA, que es
para lo que sirve.** El caso `C`, el del colapso parcial, salio **2 donde tenia que
salir 1**: el instrumento contaba los pares **ESCRITOS** y no los **RESUELTOS**, asi
que cuando `b` es alias de `a`, las parejas `(a, c)` y `(b, c)` se contaban DOS
VECES siendo la misma lectura. **Inflaba exactamente por el mecanismo que venia a
desinflar.** Se arreglo el instrumento, no el esperado del arnes.

**Y ESO MUEVE UNA CIFRA MIA DE LA 177, QUE DECLARO EN VEZ DE TAPAR** (`EJECUTOR.md`
2 y 8). La 177 publico **9 pares reales** en los seis actos; este instrumento, que
cuenta pares RESUELTOS distintos, dice **8**. **Las dos son verdaderas y miden
cosas distintas**: la 177 conto parejas escritas y leyo las nueve, y una de ellas,
en `estrategia_de_innovacion_arenas`, era **la misma pareja una vez resuelta**. La
cifra que vale para "cuantas lecturas quedan" es la de pares resueltos distintos.
El registro `docs/plan/OP_L_03_LECTURAS.jsonl` **no se retoca**: dice 2 en ese acto
y esa era su medicion, y una correccion que tapa lo que corrige no se puede
auditar.

#### 2.f. LA CIFRA QUE LA 177 NO PUDO PUBLICAR: CUANTO SOBRA EN LOS 34

**Los actos ya leidos NO se teclean: se cuentan del registro
`docs/plan/OP_L_03_LECTURAS.jsonl`**, que da 6, y los 6 siguen apareciendo en la
lista del instrumento.

| tramo | actos | pares del instrumento | pares reales | pares disueltos | sobran |
|---|---|---|---|---|---|
| YA LEIDOS (la 177) | **6** | **29** | **8** | **41** | **21** |
| SIN LEER | **34** | **44** | **10** | **93** | **34** |
| **todos** | **40** | **73** | **18** | **134** | **55** |

**LO QUE ESTO CAMBIA, DICHO CON SU NUMERO:** lo que queda de `OP-L-03` no son 44
pares en 34 actos, son **10 pares reales**, repartidos en los pocos actos que
todavia tienen mas de un nodo vivo. **De los 34 sin leer, 24 no tienen ningun par
real**: sus miembros ya colapsaron. La 177 hizo bien en no extrapolar la cifra; hoy
esta medida.

#### 2.g. EL ESTADO DE LA FICHA NO SE TOCA

`docs/plan/OPERACIONES.jsonl` **no se modifico**: `git diff --stat` sobre esa ruta
sale **vacio**. La vara sigue siendo `scripts/loop/vuelta150_3_relectura_expediente.py`
por decision del fundador del 4 sep 2026, y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
tampoco se toco: **cero veredictos movidos en esta tarea**.
