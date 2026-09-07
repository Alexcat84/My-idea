### TAREA 2, LA BATERIA ENTERA. CERRADA. LOS ONCE TRAMOS CORRIDOS, SELLADOS Y COMMITEADOS, Y DOS ROJOS QUE NO SON LO MISMO

**Instrumento:** `scripts/loop/vuelta183_bateria_por_tramos.py`, **NO CLONADO**,
que es lo que el encargo manda por defecto. **Salida unica:**
`docs/loop/SALIDA_V183_BATERIA.txt`, **disco 92570 bytes y LF 92570 bytes**,
`sha256` `aac5f56abac9e758` por disco y `aac5f56abac9e758` por LF, **1424 lineas**. Preservacion previa en
`docs/loop/SALIDA_V200_T2_PRESERVAR_LAS_NUEVE.txt`.

**LAS DOS MITADES DE LA TRAMPA, MEDIDAS ANTES DE TOCAR NADA Y NO CREIDAS.** El
bloque `H.1` del sello de apertura corrio `--plan` y `--siguiente`: **`--plan` da
ONCE tramos sobre 135 entradas**, y **`--siguiente` dijo que habia NUEVE hechos y
que el siguiente era el TRAMO 10**, sobre **nueve salidas selladas de la corrida
de la vuelta 183**. **No se le hizo caso**: se corrieron **los once**.

**LAS NUEVE SE PRESERVARON POR COPIA ANTES DE QUE EL TRAMO 1 LAS PISARA**, en
`docs/loop/preservadas/v183/` y **con el nombre exacto del original**, que es lo
que las hace citables como la misma prueba. **9 copias identicas, 0 distintas, 0
ausentes**, y **las 9 originales INTACTAS tras copiar**, remedidas una a una:
copiar no es borrar y se comprueba en vez de prometerse.

#### LOS ONCE TRAMOS, CONTADOS DE `--componer` Y NO TECLEADOS

| tramo | bytes disco | bytes LF | lineas | `sha256` LF | entradas | exitcode | minutos |
|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 9558 | 9558 | 129 | `413cf381cac3` | 13 | 1 | 2.5 |
| 2 | 7804 | 7804 | 123 | `553e56b775af` | 13 | 1 | 6.4 |
| 3 | 7857 | 7857 | 123 | `5156e936d005` | 13 | 1 | 12.9 |
| 4 | 7867 | 7867 | 123 | `75acd39e3b70` | 13 | 1 | 3.0 |
| 5 | 7827 | 7827 | 123 | `2f4ba7df5015` | 13 | 1 | 0.7 |
| 6 | 7887 | 7887 | 123 | `98498ba8f979` | 13 | 1 | 2.2 |
| 7 | 7893 | 7893 | 123 | `c09960750d7c` | 13 | 1 | 0.6 |
| 8 | 7848 | 7848 | 123 | `b07f055c9e20` | 13 | 1 | 0.8 |
| 9 | 8523 | 8523 | 125 | `c323573fb6b3` | 13 | 1 | 2.3 |
| 10 | 8475 | 8475 | 123 | `a91d4a64007f` | 13 | 1 | 2.5 |
| 11 | 6273 | 6273 | 94 | `f50d0fbbd554` | 5 | 1 | 0.3 |

**Las once primeras columnas salen de la salida de `--componer`; el `exitcode` y
los minutos, de la linea `EXITCODE DEL TRAMO` y `DURACION DEL TRAMO (monotona,
minutos)` de cada sellada.** **NINGUNA MIDE CERO BYTES.** **El reloj de la
corrida entera, sumado de las once celdas: 34.2 minutos**, contra la estimacion
que `--plan` publico con su corte, **entre 44.6 y 58.0**.

**EL CALIBRE LO COTEJA `--componer` Y NO MI CRITERIO, Y SALE VERDE:** **135**
entradas de la nomina, **135** que los tramos dicen haber corrido, **0** sin
correr, **0** ajenas, **0** repetidas, y **la cobertura se leyo de las salidas,
no se recalculo del reparto**. **Cada entrada se corre DOS VECES**, que es la
integridad que la letra del fundador del 5 sep 2026 fija y que el propio
encabezado de cada tramo escribe.

**CADA TRAMO SE COMMITEO CON SU SALIDA SELLADA AL TERMINAR, ANTES DE SEGUIR**, en
once commits distintos, mas el de la preservacion y el de la composicion.

#### EL PRIMER ROJO: LOS DOS ARNESES DEL CENSO, Y ES EL CONGELADO

**LOS ONCE TRAMOS SALEN CON EXITCODE 1, Y LOS ONCE POR EL MISMO MOTIVO, QUE NO ES
NINGUNA MUTACION:**

```
ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta
148 o despues, se quedan FUERA. La lista entera:
vuelta197_tarea2_mutacion_orden_del_turno.py,
vuelta199_tarea1_mutacion_guardas_revividas.py
```

**ES EXACTAMENTE LA CONSECUENCIA DEL CONGELADO EN 135 DE `AUDITOR.md` 6.3**, y el
encargo manda nombrarla en la seccion 9 en vez de callarla. **No se arregla, y se
dice por que:** meter esos dos en la nomina seria saltarse una decision escrita
del fundador, y la moratoria lo prohibe.

**EL PRECEDENTE ESTA MEDIDO Y NO RECORDADO:** la bateria de la vuelta 194 corrio
sus **DIEZ** tramos con **exitcode 1 en los diez**, por **6** arneses fuera de la
nomina **mas 3** entradas sin sujeto congelado. **La de hoy tiene 2 fuera, 0
invisibles al censo y 0 sin sujeto congelado**, o sea que es **estrictamente
mejor** en las tres varas. Y las nueve selladas de la 183, contadas de las copias
preservadas, **traen exitcode 0 en ocho y 1 en la novena**.

#### EL SEGUNDO ROJO, QUE NO ES EL MISMO Y VA MARCADO COMO PARADA

**UNA SOLA ENTRADA DE LAS 135 SALE `NO MORDIO`, Y ES DEL TRAMO 9:**
`vuelta185_tarea1c_mutacion_bateria_continuada.py`, **exit 1, 13.0 segundos**.
Las otras **134** corren limpias: **0 ancla perdida, 0 sin reproducir, 0
invisibles al censo, 0 sin sujeto congelado, 0 ruido de concurrencia en los once
tramos**, y **2 casos declarados con su marca obligatoria**, los dos del tramo 1
(`vuelta135_2e_mutacion_3.py` y `vuelta140_2a_mutaciones.py`).

**Y NO ES UNA GUARDA MUERTA. Lo mido en su propia salida sellada,**
`docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt`: sus bloques `A` a
`E` y `G` **calzan enteros**. Los **6** casos de `rama_de_la_seccion9()` calzan y
**los 6 CAEN al mutar su esperado**; los cuatro del cuarto parametro por defecto
calzan y caen; `vuelta_que_sello()` calza en sus tres casos y cae en los tres.
**`CIFRA fallos: 1`, y el fallo es SOLO su bloque `F`.**

**LO QUE FALLA ES UN BLOQUE CUYO SUJETO ESTA VIVO.** El bloque `F` afirma que
`tramos_por_vuelta(183)` reparte **4 y 5**: *"los tramos 1 a 4 los sello la vuelta
183 y los tramos 5 a 9 la vuelta 184"*, leyendo **el asunto del ultimo commit de
cada una de las nueve selladas**. **Esta vuelta 200 RE SELLA esas nueve con sus
propios commits**, asi que el mismo lector, corrido hoy, dice:

```
   CIFRA sellados por la vuelta 183: 0 []
   CIFRA sellados por la vuelta 184: 1 [9]
   CIFRA sellados por otra vuelta o sin asunto: 8 [1, 2, 3, 4, 5, 6, 7, 8]
   EL REPARTO ES 4 Y 5 SOBRE NUEVE: NO
```

**ES CONSECUENCIA MEDIDA DE NO CLONAR EL LANZADOR**, que es lo que el encargo
manda por defecto y lo que se hizo. **No lo arreglo**: la moratoria `6.3` lo
prohibe, el sujeto no es mio, y **su esperado no ha dejado de ser correcto: lo
que ha dejado de ser cierto es su premisa**, que es la misma especie que el acta
199 nombro en la TAREA 1 de esa vuelta. **VA COMO PARADA AL REPORTE.**

#### LO QUE LA CORRIDA DEJO EN EL ARBOL, DICHO Y NO ESCONDIDO

**LOS FICHEROS QUE LA BATERIA RE ESCRIBE SON SUYOS Y ESTABAN YA RASTREADOS.** Al
correr, cada arnes vuelve a sellar su propia salida (`SALIDA_V182_T2_*`,
`SALIDA_V184_T1C_*`, `SALIDA_V185_*`, `SALIDA_V186_*`, `SALIDA_V187_*`,
`SALIDA_V188_*`, `SALIDA_V190_*`, `SALIDA_V191_*`, `SALIDA_V192_*`,
`SALIDA_V193_*`, `SALIDA_V194_*`, `SALIDA_V195_*`) y algunos regeneran su
fixture (`docs/loop/_v167_t3_mut_componentes_*.jsonl` y
`scripts/loop/_v167_recomputo_ultimo_gana_copia.py`, **los tres ya rastreados
desde `12053ade`, medido con `git log --diff-filter=A`**). **Van dentro de los
commits de su tramo**, y **`RUIDO DE CONCURRENCIA` sale 0 en los once**, porque
no son ficheros ajenos apareciendo: son las selladas de los propios arneses que
la bateria acaba de correr.

**UNA NOTA DE METODO QUE VA CON SU NOMBRE:** el tramo 3 tardo **12.9 minutos** y
su primer lanzamiento **se corto a los 10 por el tope de la sesion**, dejando
`dataset/metadata/master_graph.json` tocado y **sin escribir su sellada**. Se
restauro con `git checkout --`, el `numstat` volvio a **cero filas**, y **el
tramo se re corrio ENTERO desde el principio**, no desde donde se corto. **Esa
corrida cortada no dejo ninguna sellada, asi que no hay ninguna prueba a medias
publicada.** Los tramos siguientes se lanzaron en segundo plano por eso.

**Y LO QUE EL ENCARGO PIDE MEDIR AL ABRIR Y AL CERRAR, CON LAS DOS MEDIDAS:**

| que | al abrir | al cerrar |
|---|---:|---:|
| entradas de la nomina | **135** | **135** |
| casos declarados | **2** | **2** |
| arneses que el censo reconoce | **197** | **197** |
| fuera de la nomina CON la vara 148 | **2** | **2** |
| fuera de la nomina SIN vara | **62** | **62** |
| entradas invisibles al censo | **0** | **0** |
| entradas sin sujeto congelado | **0** | **0** |
| `sha256` LF de `INTRA_DOMINIO_VEREDICTOS.jsonl` | `0a77b5a35a962621` | `0a77b5a35a962621` |
