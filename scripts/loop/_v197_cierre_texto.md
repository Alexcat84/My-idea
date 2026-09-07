## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CIFRA DE ABAJO ESTA TECLEADA DE MEMORIA: cada una nombra el fichero de
salida del que se cuenta** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO).

| que | cifra | de que fichero se cuenta |
|---|---|---|
| racha de cierres al entrar | **2**, vueltas **195 y 196** | `SALIDA_V197_APERTURA.txt`, bloque `E` |
| serie de registros | siguiente libre **R.59**, 50 entradas, 0 colisiones, 0 huecos | `SALIDA_V197_APERTURA.txt` bloque `G` y `SALIDA_V197_T1A_REGISTRO_R59.txt` |
| acta 197 acotada | lineas **69341 a 69635**, **295** lineas, sobre **4595886** bytes | `SALIDA_V197_T1A_REGISTRO_R59.txt`, bloque `A` |
| lectores nuevos del registrador | **7**, con **35** casos de mutacion y **35** verdes | `SALIDA_V197_T1A_MUTACION_REGISTRADOR.txt` |
| idempotencia del registrador | `docs/PENDIENTES.md` 1063803 a **1072852** bytes, y **sigue en 1072852** al re correrlo | `SALIDA_V197_T1A_RECORRIDO_SIN_ESCRIBIR.txt` |
| guardas del turno del auditor | **49** casos, **49** verdes, **0** rojos | `SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt` |
| guarda del marcador sobre el acta REAL | **3388 filas; A 551, B 72, C 5, D 2760** calzan, y **5 de 5** mutaciones CAEN | `SALIDA_V197_T2C_GUARDA_MARCADOR_ACTA_197.txt` |
| arneses de la nomina que BORRAN la sede del turno | **1 de 5** corridos | `SALIDA_V197_T2_QUIEN_BORRA_LA_SEDE.txt` |
| universo consumido | **681** de **16** ficheros con su lector, **300** con un solo patron, **561** sin el tramo | `SALIDA_V197_T3_SUJETO.txt`, bloque `C` |
| el doble | **120**, solape **0** con el tramo y **0** con el universo | `SALIDA_V197_T3_SUJETO.txt`, bloque `D` |
| quemados | **14** sellados antes de leer y **2** declarados tarde: **16** | `SALIDA_V197_T3_SUJETO.txt` `D.2` y `SALIDA_V197_T3_COTEJO.txt` `C` |
| inalcanzables a ciegas | **14** citan RACIMO, **6** CORRECCION DECLARADA, **20** en union | `SALIDA_V197_T3_SUJETO.txt`, bloque `D.3` |
| marcado sobre los 240 | **31** llevan `DISCUTIBLE MARCADO`, **31 arriba del 2662** y **0 en los 177 de abajo** | `SALIDA_V197_T3_COTEJO.txt`, bloque `F` |
| cotejo de los 240 | **215 de 240**; **207 de 224 LIMPIOS**; **8 de 16** quemados | `SALIDA_V197_T3_COTEJO.txt`, bloque `D` |
| discrepancias limpias | **17**: **6 DENTRO** y **11 FUERA** del marcado | `SALIDA_V197_T3_COTEJO.txt`, bloque `E` |
| censo y nomina, CON SU VARA | censo **195**, nomina **135**, fuera **CON la vara 148: 0** y **SIN vara: 60** | `SALIDA_V197_APERTURA.txt`, bloque `F` |
| tope del austero, tres varas | V1 **459** y **460**, V2 **444**, V3 **408** | `SALIDA_V197_T4_TRES_VARAS.txt` |

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V197_APERTURA.txt`, bloque `C`, publica las dos cifras del estado
del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten LEIDAS de
ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**Y ESAS DOS CIFRAS LAS ESCRIBIO EL PROPIO BLOQUE DE APERTURA**, con la redaccion
exacta que la guarda `D.1` busca. **La apertura sellada no se toco al cierre ni una
vez.**

**LO QUE SE TOCO:**

- `scripts/loop/`: el bloque de apertura y el de cierre, el esqueleto del reporte,
  el registrador del acta 197, los tres arneses de las guardas nuevas, el sujeto de
  la relectura al doble, el fichero de mis clases, el cotejo, el medidor de las tres
  varas y los cuatro cuerpos de tarea.
- `scripts/loop/apertura_del_auditor.py`: **la unica pieza compartida que esta
  vuelta modifica**, y **no se clono**, que es lo que el encargo manda.
- `docs/loop/`: las salidas de esta vuelta, el reporte, `REPORTE_V196.md`
  archivado byte a byte antes de pisar nada, y `_TURNO_DEL_AUDITOR.json`,
  **reconstruido por su carril tras una caida mia declarada**.
- `docs/PENDIENTES.md`: la entrada `R.59`, y **solo por adicion**.

**LO QUE NO SE TOCO, MEDIDO Y NO PROMETIDO:**

- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO SE MOVIO.** Abre y cierra igual por
  LAS DOS CONVENCIONES, y las dos van en la misma linea:
  disco 4054129 bytes y LF 4054129 bytes; y los `sha256` de disco y LF son `0a77b5a35a962621` y `0a77b5a35a962621`.
  Medido en la apertura, en el bloque `A` y el `F` del sujeto de la ciega, en el
  bloque `H` del cotejo y otra vez al cerrar.
- **NINGUNA CLASE SE TOCO.** El cribado y el recomputo quedan fuera por encargo, y
  las **17 discrepancias limpias se DECLARAN y no se mueven**.
- **`dataset/` NO SE TOCO A MANO Y NO SE MOVIO.** `git diff --numstat -- dataset/`
  da **0 filas al entrar y 0 al salir**, y el ciclo de Gate 0 entero
  (`run_phase1.py --reaplico-curaduria` y despues `etiquetas_de_cara.py --aplicar`)
  deja **0 lineas** en `dataset/`, `web/` y `engine/` por los dos lados, sellado en
  `SALIDA_V197_CICLO_NUMSTAT_APERTURA.txt` y `..._CIERRE.txt`.
- **LA NOMINA NI SE PODO NI CRECIO:** **135 entradas** y `CASOS_DECLARADOS` en
  **2** al entrar, y ninguna tarea de esta vuelta la toca.
- **NINGUNA SALIDA SELLADA AJENA QUEDO PISADA.**
  `SALIDA_V192_RACHA_DE_CIERRES.txt` se re corrio en la apertura, se restauro con
  `git checkout --` y se REMIDIO, **identica antes y despues**, y va por LAS DOS
  CONVENCIONES porque en este fichero NO coinciden:
  disco 2443 bytes y LF 2399 bytes; y los `sha256` de disco y LF son `ceb100c9fb83df88` y `4469a54a3417f36b`.
- **EL SELLO DE APERTURA DEL AUDITOR, `SELLO_APERTURA_AUDITOR_V197.json`, NO SE
  TOCO**, y va por LAS DOS CONVENCIONES:
  disco 1657 bytes y LF 1657 bytes; y los `sha256` de disco y LF son `f43b81c3d2d6b378` y `f43b81c3d2d6b378`.
  La guarda `b` de `sellar()` lo sigue mirando en disco.
- **NI CRIBADO, NI RECOMPUTO, NI OPERACIONES DEL PLAN, NI MESAS ANOTADAS, NI LA
  BATERIA ENTERA**, que no es su vuelta y cae en la 199.

**LO QUE SI SE MOVIO Y NO DEBIA, DICHO EN LA MISMA SECCION Y NO ESCONDIDO:**
`docs/loop/_TURNO_DEL_AUDITOR.json` entro midiendo disco 329 bytes y LF 329 bytes, con `sha256` de disco y LF `7203f39fd7f5a54f` y `7203f39fd7f5a54f`,
y **lo borro un arnes mio**. Sale midiendo
disco 801 bytes y LF 801 bytes; y los `sha256` de disco y LF son `69dfc4b6c6854d39` y `69dfc4b6c6854d39`.
**Reconstruido por el carril de la TAREA 2.b** del
contenido que el bloque `D.1` del sello de apertura publico antes de la primera
operacion, y **escrito CERRADO**. Es la caida `C.1` de la seccion 8.1.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**ONCE, y cada uno vive completo en la seccion de su tarea.** Nueve se marcaron
**antes** de saber el resultado y dos son **posteriores al destape y se dicen como
tales**, que es la diferencia que hace que la marca valga.

| clave | de que va | cuando se marco |
|---|---|---|
| `D.1` | la marca `NO MUEVE LA RACHA` no cambia ninguna cifra publicada, y aun asi la escribi | antes |
| `D.2` | publico la resta heredada sabiendo que en esta acta no significa lo que dice | antes |
| `D.3` | `DE REPORTE` es la marca de especie mas corta del vocabulario | antes |
| `D.4` | `leer_reporte()` apunta su toque aunque luego caiga: la bitacora pasa a ser de intentos | antes |
| `D.5` | la constancia del cierre vale como prueba de que las clases se escribieron | antes |
| `D.6` | reconstrui la sede del turno que mi propio arnes borro | antes |
| `D.7` | emiti **cero `B`** en 240 pares, y lo escribi con su riesgo delante | antes, y sali perdiendo |
| `D.8` | amplie los quemados de nueve a dieciseis, contra mi propio credito | antes |
| `D.9` | aplique la contencion mas de lo que el archivo la aplica | **despues del destape** |
| `D.10` | los quemados me salieron peor que los limpios, 8 de 16 contra 207 de 224 | **despues del destape** |
| `D.11` | la tercera vara la defini yo, y ampliarla me favorece | antes |

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` EL TOPE DE 80 LINEAS, CON SUS TRES CIFRAS DELANTE Y SIN QUEJA.** V1 **459**
y **460**, V2 **444**, V3 **408**: **la tercera vara esta 5.1 veces por encima del
tope**. La `4.6` pidio las tres medidas para decidir sobre numeros, y aqui estan.
**No la contesto yo**, y las tres salidas posibles son del fundador: subir el tope,
medirlo por la vara estrecha, o recortar de verdad lo que hoy es obligatorio.

**`P.2` UN ARNES DE LA NOMINA BORRA LA SEDE DEL TURNO DEL AUDITOR EN CADA CORRIDA,
Y NO LO REPARO PORQUE NO ESTA ENCARGADO.** Medido con una corrida y no leyendo
codigo: de **5** arneses que tocan el modulo, **1** la borra
(`vuelta182_tarea2_mutacion_apertura_auditor.py`). **Mientras eso siga asi, cada
vuelta de bateria deja al auditor sin sede y el remedio de la TAREA 2.b no se ve en
produccion aunque este entero en el codigo.** La pregunta es si reparar un arnes de
la nomina sin encargo entra en el MODO DE CIERRE o si hace falta que se encargue.

**`P.3` LA DOCTRINA QUE SE MANDA CITAR QUEMA PUESTOS DEL PROPIO SUJETO.** El
encargo manda citar el banco `9.22`, y el `9.22` nombra su ejemplar **con puesto,
clase y los dos nodos**: el **1077**, que estaba dentro de mis 240. Es la misma
especie del hallazgo `5.1` del acta 197 pero por una puerta nueva: **no es el acta
ni el reporte, es el BANCO**. La pregunta es si los ejemplares del banco tienen que
salir del universo de las ciegas por construccion, como ya se hace con lo ya
consumido.

## 7. PENDIENTES DE DOCTRINA

**NINGUNO.** Las cuatro tareas se hicieron con letra escrita: `AUDITOR.md` 1.2, 6.1
y 6.2, las adjudicaciones `4.4`, `4.5`, `4.6` y `4.7` del acta 197, sus hallazgos
`5.2` y `5.4`, y el banco `9.6.1`, `9.6.2`, `9.6.3` y `9.22`. **Las tres preguntas
de la seccion 6 no piden doctrina nueva: piden una decision sobre cifras ya
publicadas.**

## 8. LO QUE LA 198 RECIBE

**LA DEUDA QUE ESTA VUELTA DEJA, MEDIDA Y NO ANUNCIADA:**

- **EL TRAMO SE RELEE AL DOBLE OTRA VEZ.** Once de mis diecisiete discrepancias
  limpias cayeron **FUERA del marcado**, asi que por `AUDITOR.md` 1.2 el credito de
  mi tanda BAJA. **La serie medida va 30, 60, 120, 240 y ahora 480.** Y con ella el
  hallazgo `5.2` del acta 197 en su forma mas dura: **nueve de esas once estan por
  debajo del 2662, donde el archivo no marca nada**, asi que caen fuera **por
  construccion**.
- **LAS DOS CAIDAS DE MI SECCION 8.1**, que abajo van con su nombre.
- **LAS TRES PREGUNTAS DE LA SECCION 6.**
- **LO QUE SIGUE FUERA Y NO SE REDESCUBRE:** el desfase de `PATRONES_ACTA`; la
  guarda de codigo del hallazgo `5.3` del acta 194; `acumulan()` que lea la tabla;
  el cotejo de clon declarado; las ocho actas sin entrada propia en la serie (173 a
  180, remedido en esta vuelta); el estado de `OP-L-02`, **que no se movio y sigue
  en `LISTA`**; **que hacer con las filas `B` del archivo**; y **los puestos que dos
  o tres lectores independientes fallaron**, a los que esta vuelta anade los suyos y
  **no resuelve, porque mover una clase es del RECOMPUTO**.

### 8.1 MIS CAIDAS DE ESTA VUELTA, DECLARADAS POR MI

**`C.1` DE METODO. MI ARNES BORRO LA SEDE DEL TURNO DEL AUDITOR.** La primera
version de `scripts/loop/vuelta197_tarea2_mutacion_orden_del_turno.py` restauraba
`AP.RUTA_DEL_TURNO` a su sede **antes** de llamar a `AP.olvidar_todo()`, y
`olvidar_todo()` borra el fichero del turno. **La cazo el ultimo caso de ese mismo
arnes**, el que mide la sede antes y despues. El orden esta corregido con su motivo
al lado, la sede se reconstruyo por el carril y **el arnes ahora tiene un caso mas
que comprueba que el temporal SI queda borrado**. **NO es caida de cifra publicada:
ninguna cifra falsa salio de aqui, y la medicion de entrada esta sellada en la
apertura.**

**`C.2` DE METODO. NO COMPROBE SI LOS QUEMADOS DE LA 196 CAIAN EN MI UNIVERSO.**
Clone `vuelta196_tarea2_relectura_al_doble.py` para escribir mi sujeto y lei su
lista `QUEMADOS` entera, que nombra el `654` con su clase de archivo, **y el `654`
estaba dentro de mis 240**. Lo declare en el fichero de clases, **antes del destape
pero despues de sellar el sujeto**, que es peor que declararlo antes. **El remedio
para la 198 es mecanico: al clonar un sujeto, cotejar su lista de quemados contra
el universo nuevo.**

**LAS DOS SON DE METODO Y NINGUNA ACUMULA.** Y las dos las cazo una guarda mia o mi
propia lectura, no el auditor.
