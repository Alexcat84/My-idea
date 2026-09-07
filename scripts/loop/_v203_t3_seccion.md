### TAREA 3. `OP-I-01` CONTRA EL CRITERIO DE HECHO, LA CUARTA FICHA REAL

**ES LA UNICA DE LAS CUATRO QUE LA VARA DEL PLAN DA COMO TRABAJO REAL Y QUE NADIE
HABIA MEDIDO CONTRA EL CRITERIO DE HECHO.** La 201 le corrigio la `evidencia`;
**a la `verificacion` no la habia mirado nadie.**

**3.a EL CRITERIO, CITADO POR LINEA Y NO DE MEMORIA.** En
`docs/plan/08_VERIFICACION.md`, que mide **69068** bytes en disco y **69068**
normalizado a LF: la **cabecera** en la **linea 7**
(`## EL CRITERIO DE HECHO, y es uno solo`), **1 sola aparicion**; el **literal**
en la **linea 9**, *UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL
FALLO VOLVIERA*, **1 sola aparicion**; y su **comprobacion barata** en las
**lineas 14 y 15**, *correr la prueba ANTES del arreglo. Si pasa, no prueba
nada*. **Y SE DECLARA LO QUE NO ESTA:** ese documento **no nombra `OP-I-01` ni
una vez** (**0 lineas**), asi que el criterio que se le aplica es **el general**.

**3.b LA FICHA, POR LINEA MAS INDICE, Y LA LINEA SE COMPRUEBA EN VEZ DE
SUPONERSE.** El encargo dice **linea 44**; medido aqui, `OP-I-01` vive en **1
sola linea** de `docs/plan/OPERACIONES.jsonl` y es la **44**. **CALZA.**
`estado='LISTA'`, `tipo='MESA'`, `fase='10_INVENTARIO'`,
`fecha_corte='2026-08-11'`. Su `verificacion` trae **4 elementos** y **los 4 son
clausulas que hay que cumplir**: **0** de ellos es una `CORRECCION DECLARADA`.
**Esa distincion importa y por eso se mide**, porque en la ficha hermana
`OP-L-01` cuatro de sus siete elementos no son clausulas. En la `evidencia`, en
cambio, **1 de sus 4** si lo es, el **indice 3**.

**3.c LO QUE REPRODUCE LA CORRECCION DE LA 201, MEDIDO HOY CON OTRO
INSTRUMENTO.** La `evidencia` nombra `INVENTARIO.jsonl, 323 entradas` en **2**
de sus elementos, el **0** y el **3**, y hoy hay **672**. **No es un hallazgo
nuevo:** el acta 201 ya lo corrigio en su TAREA 2 y su correccion publica **672
entradas, 0 lineas no JSON, 584554 bytes en disco y 584554 normalizados a LF**.
**Medido hoy por mi: 672, 0, 584554 y 584554. CALZA AL DIGITO.** Y el reparto por
tipo tambien: **556 acto, 54 familia_de_ids, 20 figura, 19 defecto, 13 racimo,
10 dominio**, que suma **672**.

**3.d LAS CUATRO CLAUSULAS, MEDIDAS, Y DESPUES PASADAS POR LA PREGUNTA QUE EL
CRITERIO HACE.** Cada veredicto sale de una **expresion computada sobre el
fichero**, nunca de un literal.

| clausula | medida hoy | se caeria si el fallo volviera |
|---|---|---|
| **1.** `toda entrada lleva su fecha_corte` | **672 de 672** con `fecha_corte`, **0** sin ella, en **4** cortes distintos | **SI** |
| **2.** `toda forma con cobertura incompleta va marcada PROVISIONAL` | **1** entrada marcada `PROVISIONAL`, **0** con `cobertura` vacia, y **0 apariciones** de las **7** variantes buscadas | **NO** |
| **3.** `todo hueco va NOMBRADO, nunca rellenado` | **0** filas con `nota` y `cobertura` las dos vacias | **NO** |
| **4.** `el inventario se recomputa entero con el disparador de 08_VERIFICACION` | el instrumento corre en **exitcode 0** | **EN PARTE** |

**3.e Y LA COLUMNA DE LA DERECHA ES LA TAREA, NO LA DE EN MEDIO.** Las cuatro
salen **sin contraejemplo** hoy. Lo que esta tarea trae es que **dos de ellas no
se caerian** y **una se caeria solo en parte**:

- **LA 2 Y LA 3 COMPARTEN EL MISMO AGUJERO, Y ES DE VARA.** Las dos exigen saber
  **donde hay cobertura incompleta** o **donde hay hueco**, y la clave
  `cobertura` de `docs/plan/INVENTARIO.jsonl` es **texto libre**, no un campo con
  valores cerrados. **La busqueda positiva va publicada**, porque una busqueda
  negativa no se puede citar (`EJECUTOR.md` 9): de las **7** variantes
  (`incompleta`, `INCOMPLETA`, `parcial`, `PARCIAL`, `sin cerrar`, `pendiente`,
  `falta`), **las 7 dan 0 apariciones**. **El dia que alguien deje de marcar
  `PROVISIONAL` una forma incompleta, esta comprobacion daria exactamente lo
  mismo**, porque no hay campo que lo delate. Lo que hoy las sostiene es que
  **alguien las mira**, no una expresion que caiga: es la degradacion silenciosa
  del banco `9`.
- **LA 4 SE CAE SOLO EN LA PARTE QUE SI RECOMPUTA.** La clausula dice
  **`el inventario se recomputa ENTERO`**, y el alcance del disparador, acotado
  por la adjudicacion `6.4` del acta 168, son los tipos `acto` y `racimo`:
  **569 de 672 dentro y 103 fuera**, medido por el propio instrumento en esta
  vuelta. Los **103** de fuera **no tienen quien los tumbe**.

**3.f LO QUE EL INSTRUMENTO MIDE HOY, PEGADO DE SU PROPIA SALIDA.** **672**
entradas del inventario, **569 dentro** del disparador y **103 fuera**, **348
vigentes** y **221 marcadas SUPERADA**; de las **348** re medidas, **333
calzan**, **8 difieren** y **7** no tienen componente. **Y EL PROPIO INSTRUMENTO
DECLARA UNA DISCREPANCIA QUE NO RESUELVE COPIANDO**, y aqui se reproduce en vez
de silenciarse: el fichero sellado de componentes trae **332 lineas** (**54
ABIERTO**, **278 CERRADO**) y la corrida de hoy da **47** (**21 ABIERTO**, **26
CERRADO**), o sea que **`la corrida de hoy REPRODUCE el fichero sellado` sale
`False`**.

**3.g LA COMPROBACION DE SI ESCRIBE SALIO POSITIVA, Y NO SE IGNORO.**
`scripts/loop/vuelta169_tarea3_op_i_01.py` mide **13148** bytes en disco y
**13148** normalizado a LF, y leido **antes** de correrlo trae **2 lineas con
marca de escritura**, las **26** y la **147**: **escribe sobre
`docs/loop/RECOMPUTO_V169.jsonl`, que esta sellado y commiteado en la vuelta 169**
(commit `a77b206f`). **Por eso se corrio con el protocolo del sello**, el mismo
que el bloque `E` de la apertura uso con el instrumento de la racha: medir antes,
correr, leer, **restaurar con `git checkout --`** y remedir. Su `sha256` LF vale
`e8a10f174df3c5fa` **antes, despues de correr y despues de restaurar**, y
`git status` cierra con **0 lineas nuevas** respecto de antes. **Esto es
exactamente la caida `C.2` del auditor de la 202, y aqui no se repitio.**

**UN DETALLE QUE SE DECLARA EN VEZ DE DEJARSE PASAR:** el fichero mide hoy
**15369** bytes en disco y **15322** normalizado a LF, y esas dos cifras **no
coinciden entre si** porque `git checkout` lo devuelve con CRLF y la corrida lo
habia escrito con LF. **Su contenido no cambio**: el `sha256` normalizado a LF es
el mismo por las dos convenciones de lectura, y `git hash-object` sobre el disco
devuelve el mismo blob que `HEAD`.

**3.h LA PROPUESTA, Y LA ADJUDICA EL AUDITOR: `OP-I-01` NO SE CIERRA.** No porque
una clausula salga en rojo hoy, **que ninguna sale**, sino porque **2 de sus 4 no
se caerian si el fallo volviera y 1 se caeria solo en parte**, que es lo que el
criterio de la **linea 9** pregunta. **El `estado` no se toca: entra `LISTA` y
sale `LISTA`.** Y esta tarea **no escribe en el plan**: `git diff --numstat` da
**0 filas** en `docs/plan/OPERACIONES.jsonl`, `docs/plan/INVENTARIO.jsonl`,
`docs/plan/08_VERIFICACION.md` y `docs/loop/RECOMPUTO_V169.jsonl`.

**3.i UNA CAIDA MIA, CAZADA ANTES DE PUBLICARSE.** Mi primera tanda de patrones
para leer las cifras del instrumento sacaba **`(no legible)` en 3 de 4**, porque
yo habia **tecleado las etiquetas de memoria** en vez de leerlas de su salida.
Arreglado leyendo el fichero y ampliando a **12 etiquetas mas la del veredicto de
reproduccion**; re-corrido, **las 13 salen legibles**. Ninguna de esas cifras
llego a publicarse mal.
