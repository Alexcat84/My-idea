### TAREA 1 (BLOQUEANTE). LOS REGISTROS Y LA ETIQUETA DE FUENTE, ARREGLADA

**1.a. LOS REGISTROS, LEIDOS HOY Y CITADOS CON SU LINEA.** El acta del auditor de
la vuelta 179 esta escrita en `docs/loop/ACTA_AUDITOR.md`, cabecera en la
**linea 62019**, y **no levanta ninguna caida contra la 179**:

| lo que dice el acta 179 | linea leida hoy | literal |
|---|---:|---|
| caidas del ejecutor | `62232` | "CAIDAS DEL EJECUTOR: NINGUNA, Y LO DIGO CON LA LISTA DE LO QUE BUSQUE" |
| racha de reporte | `62238` | "La racha de reporte, que mi acta 178 dejo en DOS, vuelve a CERO" |
| racha de cifra publicada | `62406` | "caidas del ejecutor que ACUMULAN **0** / racha de cifra publicada **0**" |
| racha de reporte en la metrica | `62407` | "caidas del ejecutor de reporte **0** / racha de reporte **0**" |
| parada | `62437` | "## 12. PARADA: NO" |

**NO HAY NINGUNA CORRECCION DECLARADA QUE ARRASTRAR DE LA 179.** El acta declara
UNA caida propia del auditor (`C.1`, seccion 2, linea `62031`), que es suya y no
mia, y **seis caidas que el propio ejecutor se levanto** y que el acta declara
expresamente **NO caidas de esa acta** (linea `62240`).

**1.b. LA ETIQUETA DE FUENTE, ARREGLADA, Y ESO LEVANTA MI PARADA DE LA 3.f DE LA
179.** La adjudicacion **7.7 del acta 179** estrecha la instruccion que me hacia
parar: lo que aquel encargo protegia era que ninguna clase ni su procedencia se
movieran, y un literal que atribuye a la 177 cinco lecturas de la 179 no protege
eso, lo rompe, contra `EJECUTOR.md` 8.

**LO QUE CAMBIA EN LA MAQUINA, Y NADA MAS QUE ESO.** En
`scripts/loop/vuelta178_tarea3_anotar_triangulos.py`:

- nace `etiqueta_del_registro(vuelta)`, **PURA**, que compone la etiqueta con la
  vuelta que se le pasa y dice `(vuelta desconocida)` si la fila no la trae, en
  vez de inventar un numero;
- `clases_por_par()` **lee `d.get("vuelta")` de la fila del registro** y llama a
  esa funcion, en vez del literal `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)`
  que estaba clavado en la **linea 160** del fichero de apertura;
- `clases_por_par()` gana los parametros `lecturas` y `filas`, para que su caso
  positivo por mutacion pueda apuntarla a un registro fabricado sin tocar nada
  vivo;
- el sello de `sha256` pasa de UN registro a **LOS DOS**, antes y despues, dentro
  del propio instrumento, y el ROJO cubre a los dos.

**LOS CUATRO `sha256`, IMPRESOS POR EL PROPIO INSTRUMENTO** (bloques `A)` y `H)`
de `docs/loop/SALIDA_V180_T1B_TRIANGULOS.txt`):

| registro | sha256 ANTES | sha256 DESPUES | identicos |
|---|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | `ea6e850d331d14f0...` | `ea6e850d331d14f0...` | **SI** |
| `docs/plan/OP_L_03_LECTURAS.jsonl` | `d93c59a86372cf50...` | `d93c59a86372cf50...` | **SI** |

Los cuatro completos: `ea6e850d331d14f01db1186a54f4913fa72eb2560a354430c5e6d047ff0d02be`
dos veces, y `d93c59a86372cf501f407a82cc79d649d02fd73c404429489ec6c07b4272719f`
dos veces. **NINGUNA CLASE SE MOVIO.** Bytes de los dos, por las dos
convenciones: `4.051.967` en disco y `4.051.967` normalizado a LF el primero;
`51.368` y `51.368` el segundo.

**LAS DOS MEDICIONES DE LA ETIQUETA, CADA UNA CON SU CORTE, Y LA VIEJA NO SE
BORRA** (`banco 9.10`). Las dos salen del mismo instrumento,
`scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py`, corrido dos veces:

| medicion | corte | fichero contado | etiquetados como de la 177 | verdaderos | **falsos** |
|---|---|---|---:|---:|---:|
| ANTES del arreglo | HEAD `d3240915e994`, apertura de la 180 | `docs/loop/SALIDA_V180_APERTURA.txt`, bloque `H.6` | 15 | 10 | **5** |
| DESPUES del arreglo | HEAD `122ca81fb96e`, tras la 1.b de la 180 | `docs/loop/SALIDA_V180_T1B_ETIQUETA_DESPUES.txt`, bloque `C)` | 10 | 10 | **0** |

**DA CERO FALSOS Y POR ESO NO PARO.** Los cinco que antes salian falsos, nombrados
uno a uno por el instrumento de apertura, eran dos lados de
`colaboracion_cadena_suministro`, uno de `creacion_option_pool` y dos de
`fase_diseno_prototipado_modelos`, **los cinco escritos por la vuelta 179**.

**EL REPARTO DE LADOS POR FUENTE CON LAS ETIQUETAS NUEVAS**, contado del bloque
`D.1)` de `docs/loop/SALIDA_V180_T1B_TRIANGULOS.txt`:

| que se cuenta | cuantos |
|---|---:|
| lados con clase leida de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **42** |
| lados con clase leida de `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` | **10** |
| lados con clase leida de `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 179)` | **5** |
| **total de lados** | **57** |
| **total de triangulos** | **19** |

**EL TOTAL NO SE MOVIO: 19 triangulos y 57 lados**, que es lo que el encargo
exige, y `42 + 10 + 5 = 57` calza. Antes del arreglo el mismo reparto daba **42 y
15** en dos filas; ahora son tres filas y la de la 179 sale a la luz. La particion
de triangulos tampoco se movio: **8 enteros del archivo, 11 apoyados en un lado de
fuera, 9 de ellos con el `D` fuera**.

**EL CASO POSITIVO POR MUTACION, CORRIDO Y NO PROMETIDO**
(`scripts/loop/vuelta180_tarea1b_mutacion_etiqueta.py`, salida en
`docs/loop/SALIDA_V180_T1B_MUTACION_ETIQUETA.txt`, exit **0**). Registro
**fabricado en un temporal**, dos filas de **dos vueltas distintas** (177 y 180),
mapa de alias vacio y veredictos vacios: **ni un fichero vivo**.

| caso | que hace | etiquetas distintas | veredicto |
|---|---|---:|---|
| 1, el codigo de hoy | cada lado con su vuelta | **2** | **VERDE** |
| 2, la mutacion: etiqueta clavada en el literal de la 177 | los dos lados iguales | **1** | **CAE, VERDE** |

**UN REGISTRO DE UNA SOLA VUELTA NO PODRIA CAZAR ESTO**, porque con una sola
vuelta el literal acierta por casualidad; por eso el registro fabricado tiene dos.
La mutacion se deshace en `finally` y el temporal se retira (`P.16`), las dos
cosas comprobadas y publicadas por el propio arnes.

**LO QUE ESTA TAREA MOVIO EN EL ARBOL, contado con `git diff --numstat`:**
`docs/plan/OP_L_03_TRIANGULOS.jsonl` **3 lineas mas 3 menos** (las tres filas cuyos
lados cambian de etiqueta) y
`scripts/loop/vuelta178_tarea3_anotar_triangulos.py` **83 mas 21**. La guarda de
`dataset/` sale **VERDE con 0 filas, 0 ficheros y 0 blobs divergentes**.
