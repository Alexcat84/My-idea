### TAREA 3. LOS TRIANGULOS SE PUBLICAN PARTIDOS POR SU FUENTE

#### 3.a. LA MEDICION DEL ENCARGO, REPRODUCIDA ANTES DE ESCRIBIR NADA

El encargo pide reproducirla primero, y sale identica. Contada de
`docs/loop/SALIDA_V179_T3_TRIANGULOS_ANTES_DE_T2.txt`, **al corte del commit de
apertura de esta vuelta y ANTES de que la TAREA 2 escribiera una sola linea**:

| que se cuenta | cuantos |
|---|---:|
| lados con clase leida de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **38** |
| lados con clase leida de `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` | **10** |
| triangulos con los TRES lados con veredicto en el archivo | **8** |
| triangulos con al menos un lado SIN veredicto en el archivo | **8** |
| de esos, aquellos en que el lado de fuera es el `D` | **6** |
| **total de triangulos** | **16** |

**Las cinco cifras del encargo, las cinco.**

#### 3.b. Y LA DEL CIERRE, QUE ES OTRA, PORQUE LA TAREA 2 LA MOVIO

`EJECUTOR.md` 1 dice que **el estado al cierre se mide al cierre si algo de la
propia vuelta pudo haberlo movido**, y lo movio: la TAREA 2 escribio diez
lecturas nuevas en el mismo registro del que este instrumento saca la clase de
los lados de fuera. Contada de `docs/loop/SALIDA_V179_T3_TRIANGULOS.txt`, **al
cierre de la TAREA 2**:

| que se cuenta | cuantos |
|---|---:|
| lados con clase leida de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **42** |
| lados con clase leida del registro de `OP-L-03` | **15** |
| triangulos con los TRES lados con veredicto en el archivo | **8** |
| triangulos con al menos un lado SIN veredicto en el archivo | **11** |
| de esos, aquellos en que el lado de fuera es el `D` | **9** |
| de esos, aquellos en que el lado de fuera NO es el `D` | **2** |
| **total de triangulos** | **19** |

**LA RESTA CIERRA DOS VECES:** enteros **8** mas apoyados **11** son **19**, y de
los apoyados, **9** con el `D` fuera mas **2** sin el `D` fuera son **11**.

**LAS DOS TABLAS SON VERDADERAS Y NINGUNA SUSTITUYE A LA OTRA.** La de arriba es
la apertura, la de abajo el cierre, y cada una lleva su corte. **Los que no se
mueven son los ocho enteros:** los que descansan en el archivo siguen siendo
ocho, porque nada de esta vuelta anadio un veredicto al archivo.

#### 3.c. LOS NUEVE CON EL `D` FUERA, NOMBRADOS

Van uno a uno en `docs/loop/SALIDA_V179_T3_TRIANGULOS.txt`, con su acto, su terna
y el lado `D` que viene de fuera. **El `D` es el lado que hace que el triangulo
sea un triangulo**: dos `A` sin un `D` entre ellos no son esta figura, y por eso
se cuentan aparte de los otros **2**, cuyo lado de fuera es un `A`.

#### 3.d. EL CAMPO NUEVO Y LOS VEREDICTOS QUIETOS

`docs/plan/OP_L_03_TRIANGULOS.jsonl` gana **`recomputable_entero_del_archivo`** en
**las 19 filas, sin excepcion**, mas `el_lado_de_fuera_es_el_D` y
`vuelta_que_anota_la_fuente`. **El campo `fuente_de_la_clase` por lado no se
toca**, que es lo que el encargo manda.

**CERO VEREDICTOS MOVIDOS**, comprobado por `sha256` de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` antes y despues dentro del propio
instrumento, y los dos salen **IDENTICOS**.

#### 3.e. EL CASO POSITIVO POR MUTACION

`scripts/loop/vuelta179_tarea3_mutacion_triangulos.py`
(`docs/loop/SALIDA_V179_T3_MUTACION.txt`). **20 casos, los 20 pasan y los 20
CAEN** al mutarles el valor esperado. **El caso que lo decide todo esta puesto:**
un triangulo con sus tres lados en el archivo y otro con el `D` fuera caen en
casillas distintas. **Y esta la mitad que se olvida:** los DOS apoyados, el del
`D` fuera y el de un `A` fuera, tambien caen en casillas distintas. **Nada sale
del repo**: los cuatro triangulos son fabricados.

**Y EL ARNES TUMBO DOS ESPERADOS MIOS EN SU PRIMERA CORRIDA**, y lo escribo en vez
de callarlo: yo esperaba 6 y 6 lados por fuente sobre el registro fabricado, y
son **7 y 5**. **El codigo estaba bien y mis dos numeros estaban mal.** La
mutacion los cazo porque el esperado equivocado coincidia con el valor mutado.

#### 3.f. PARADA: UNA ETIQUETA DE FUENTE QUE YA NO ES VERDAD

**LA DESTAPO ESTA MISMA VUELTA Y LA CAUSA ES MIA.** `clases_por_par()` etiqueta
con el literal `"docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)"` **toda** clase
que venga de ese registro, porque cuando se escribio la 177 era la unica que
habia escrito ahi. **La TAREA 2 de esta misma vuelta escribio diez lecturas mas,
de la vuelta 179, y salen etiquetadas como si fueran de la 177.**

Contado por `scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py`
(`docs/loop/SALIDA_V179_T3_ETIQUETA.txt`):

| que se cuenta | cuantos |
|---|---:|
| lados etiquetados como del registro de la vuelta 177 | **15** |
| de esos, los que SI son de la vuelta 177 | **10** |
| de esos, los que NO lo son | **5** |
| de esos, los que no se pudieron cotejar | **0** |

**LA RESTA CIERRA:** 10 mas 5 mas 0 son 15. **Los cinco mal etiquetados van
nombrados uno a uno** en ese fichero.

**NO LO ARREGLO, Y DIGO POR QUE.** El encargo de esta vuelta dice con estas
palabras: *"El campo `fuente_de_la_clase` por lado NO se toca"*. Y lo que la
etiqueta rota contradice es `EJECUTOR.md` 8, **toda cifra de un autor con su
atribucion**. Cuando algo contradice una regla vigente, `EJECUTOR.md` 5 manda
**escribirlo como PARADA en el reporte y no arreglarlo por cuenta propia**. Asi
queda: **medido, nombrado y sin tocar**.
