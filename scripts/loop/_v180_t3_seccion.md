### TAREA 3. EL CORTE, CABLEADO DONDE TODAVIA FALTABA

**EL HALLAZGO ES DEL FUNDADOR Y ESTA MEDIDO EN LA SECCION 6 DEL ACTA 179**
(`docs/loop/ACTA_AUDITOR.md:62247`), y su propia acta dice con esas palabras
**"NO ES UNA CAIDA Y NO LA REGISTRO COMO TAL"**: las cifras de la 2.a de la 179
estaban contadas de su fichero y eran verdad. **Lo que faltaba es el corte.**

**EL SELLO GANA UN TERCER PARAMETRO, Y NO ES UN CAPRICHO.**
`sello_de_corte(denominador, head)` tenia la palabra `nomina` **clavada en su
texto**: cablearlo tal cual en la tabla de tramos habria escrito `nomina` encima
de una cifra que no es la nomina, o sea una etiqueta falsa. Ahora es
`sello_de_corte(cifra, head, que="nomina contada en esta corrida")`, y **el valor
por defecto conserva a sus llamadores viejos byte a byte**: lo prueba
`scripts/loop/vuelta179_tarea1d_mutacion_corte.py`, sin tocarle una linea, que
sigue dando **10 casos, los 10 pasan y los 10 CAEN** al mutarles el esperado.

**CABLEADO DONDE SE GENERA LA TABLA, NO EN UNA FRASE.** En
`scripts/loop/backlog_l03_resuelto.py` el corte se compone en el bloque `A)` con
`VMV.corte_de_git()` y baja a los bloques `B)`, `D)`, `E)` y `F)`. La tabla de
tramos, que es **la que se movio dentro de la 179**, sale hoy asi
(`docs/loop/SALIDA_V180_T3_BACKLOG.txt`, bloque `F)`, exit **0**):

| tramo | actos | pares del instrumento | pares reales | pares disueltos | sobran | corte |
|---|---|---|---|---|---|---|
| YA LEIDOS (la 177) | **14** | **39** | **18** | **41** | **21** | HEAD `cbe0feb94087` |
| SIN LEER | **26** | **34** | **0** | **93** | **34** | HEAD `cbe0feb94087` |
| **todos** | **40** | **73** | **18** | **134** | **55** | HEAD `cbe0feb94087` |

**LAS TRES MEDICIONES DE LA MISMA TABLA, LAS TRES VERDADERAS, CADA UNA CON SU
CORTE**, y la vieja no se borra (`banco 9.10`):

| quien la midio | corte | actos ya leidos | pares sin leer | reales sin leer |
|---|---|---|---|---|
| la 2.a de la 179 (`SALIDA_V179_T2_LOS_DIEZ.txt`) | **sin corte, y eso es lo que se arregla** | 6 actos, 29 pares, 8 reales | 34 actos, 44 pares | 10 |
| el fundador, seccion 6 del acta 179 | el de su corrida, que su acta no fija | 14 / 39 / 18 | 26 / 34 | 0 |
| esta vuelta, bloque `H.8` de la apertura | HEAD `d3240915e994` | 14 / 39 / 18 | 26 / 34 | 0 |
| esta vuelta, tras el cableado | HEAD `cbe0feb94087` | 14 / 39 / 18 | 26 / 34 | 0 |

**EL BARRIDO DEL RESTO, Y ENCONTRO TRECE.** Instrumento nuevo:
`scripts/loop/vuelta180_tarea3_barrido_de_cortes.py`. Corre los dos instrumentos
que el encargo nombra, recoge **toda** linea que publique una cifra y la cruza
con una tabla declarada. **Su primera corrida salio en ROJO con 13 cifras que se
mueven y no llevaban su corte**, y esa corrida esta guardada sin retocar en
`docs/loop/SALIDA_V180_T3_BARRIDO_ANTES.txt` (exit **1**). Las trece se
cablearon, y la corrida de despues
(`docs/loop/SALIDA_V180_T3_BARRIDO.txt`, exit **0**) da:

| cifra del barrido | valor | corte |
|---|---:|---|
| filas declaradas | **32** | HEAD `cbe0feb94087` |
| de esas, las que SE MUEVEN dentro de una vuelta | **25** | HEAD `cbe0feb94087` |
| de esas, las que NO se mueven | **7** | HEAD `cbe0feb94087` |
| lineas de cifra en las dos salidas | **34** | HEAD `cbe0feb94087` |
| lineas de cifra **sin cubrir** por la tabla | **0** | HEAD `cbe0feb94087` |
| fallos | **0** | HEAD `cbe0feb94087` |

**LAS TRECE QUE NO LLEVABAN CORTE Y AHORA LO LLEVAN**, nombradas del fichero rojo:
en `backlog_l03_resuelto.py`, `ficheros de dataset/nodos/ leidos`, `alias del
mapa`, `nodos del grafo`, `nodos VIVOS`, `filas de
docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `pares distintos tras resolver`, `actos
donde los dos caminos CALZAN`, `actos donde NO calzan`, `actos que el registro
dice leidos` y `de esos que el instrumento sigue dando`, mas las tres que **no se
mueven y no lo decian**: `actos que su LISTA DECLARADA trae`, `pares que el
instrumento da` y `actos medidos`, que ahora dicen en su propia linea que salen
del corte sellado en la vuelta 15.

**Y EL SEGUNDO INSTRUMENTO, `vuelta179_tarea2_cobertura_final.py`, ENTERO:** sus
**once** lineas de cifra llevan corte hoy
(`docs/loop/SALIDA_V180_T3_COBERTURA.txt`, exit **0**), menos la de `actos que el
instrumento da`, que dice en su linea que no se mueve. De paso, su reparto por
vuelta **deja de estar tecleado en dos vueltas** (`177` y `179` a mano) y se
cuenta del propio registro, para que el dia que escriba una tercera no se quede
muda.

**LA DECLARACION QUE `EJECUTOR.md` 1 EXIGE, Y VA DELANTE:** la columna **"se
mueve dentro de una vuelta" es una clasificacion A MANO**, porque no hay forma de
medir en una sola corrida si una cifra se movera en la siguiente. **NO HAY CASO
ROJO AUTOMATICO PARA ESA COLUMNA**, y no se fabrica uno que se apruebe solo. Lo
que **si** es mecanico y **si** cae en rojo son las cuatro comprobaciones del
barrido: que cada cifra declarada se publique hoy, que cada movible lleve su
corte, que cada no movible lo diga, y que **ninguna linea de cifra se escape de la
tabla**. Esa cuarta es la que impide que la tabla se quede corta en silencio.

**EL CASO POSITIVO POR MUTACION**
(`scripts/loop/vuelta180_tarea3_mutacion_corte_de_tramos.py`, salida
`docs/loop/SALIDA_V180_T3_MUTACION_CORTE.txt`, exit **0**): **16 casos, los 16
pasan y los 16 CAEN** al mutarles el valor esperado.

| lo que prueba | resultado |
|---|---|
| B, **el caso del acta 179**: la misma tabla en dos cortes (`8` y `18`) no se confunde | pasa y CAE al mutar |
| C, **la misma cifra con dos cortes distintos** tampoco se confunde | pasa y CAE al mutar |
| D, **dos cosas distintas del mismo tamano y del mismo corte** tampoco | pasa y CAE al mutar |
| E, el valor por defecto conserva a los llamadores viejos | pasa y CAE al mutar |
| G, H, I, las tres funciones puras del barrido | pasan y CAEN al mutar |
| C del informe, **la guarda del barrido tumbada**: una linea sin corte pasaria | `True` tumbada, `False` de verdad |

**LA D MERECE UNA LINEA APARTE Y ES HALLAZGO DE ESTA TAREA:** en la corrida de hoy
hay un **18** que son pares reales y otro **18** que son pares con clase escrita.
Con la palabra `nomina` clavada, los dos sellos habrian salido **identicos**. Esa
confusion solo aparece al sacar el sello fuera de la nomina, y es exactamente por
lo que el tercer parametro no es cosmetico.

**LA NOMINA CRECE DE 105 A 106** con
`vuelta180_tarea3_mutacion_corte_de_tramos.py`. Recontada al cerrar esta tarea:
censo **166**, nomina **106**, `166 - 106 = 60` y fuera de la nomina **60**;
`arneses_que_faltan()` **0**, invisibles al censo **0**, sujetos sin congelar
**0**. **`vuelta180_tarea3_barrido_de_cortes.py` NO entra**, y la vara es la
misma que en la TAREA 2: su nombre no trae ninguna de las tres familias del
censo, y no se publica como caso positivo por mutacion.
