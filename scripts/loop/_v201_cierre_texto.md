## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA FILA DE ESTA TABLA CITA EL FICHERO DEL QUE SE CUENTA** (`EJECUTOR.md` 1,
LA TABLA SE CUENTA DE SU FICHERO). Ninguna celda esta tecleada de memoria.

| que | cifra | de que fichero se cuenta |
|---|---|---|
| racha de cierres, que decide el tope de sub-tareas | **2**, con las vueltas **199** y **200** | `SALIDA_V201_APERTURA.txt`, bloque `E` |
| entradas de la serie `R.N`, antes y despues | **52** y **54**, con **0** colisiones y **0** huecos en las dos | `SALIDA_V201_T1_REGISTROS.txt` |
| numerales del acta 200 | **8** adjudicaciones, **4** hallazgos, **2** preguntas, **4** caidas del auditor, **0** del ejecutor | `SALIDA_V201_T1_REGISTROS.txt` |
| numerales del acta 198 | **3** adjudicaciones, **5** hallazgos, **3** preguntas, **2** caidas del auditor, **0** del ejecutor | `SALIDA_V201_T1_REGISTROS.txt` |
| cuerpo del acta 200, acotado hoy | lineas **70230** a **70549**, **320** lineas | `SALIDA_V201_APERTURA.txt`, bloque `H` |
| cuerpo del acta 198, acotado hoy | lineas **69636** a **69877**, **242** lineas | `SALIDA_V201_T1_REGISTROS.txt` |
| prueba de la guarda de idempotencia | **8** casos, **8** verdes, **0** rojos, **8 de 8 CAEN** al mutar el esperado, **2** discrepan contra la guarda vieja | `SALIDA_V201_T1_REGISTROS.txt` |
| la segunda corrida del registrador | **0** entradas escritas, crecimiento **0** bytes | `SALIDA_V201_T1_REGISTROS_IDEM.txt` |
| deuda de la serie al cerrar | **8** actas de la 173 a la 200 sin entrada propia, las de la **173** a la **180** | `SALIDA_V201_T1_REGISTROS.txt` |
| el literal de la 1.c, en los dos ficheros | **0** lineas en `AUDITOR.md` y **4** en `ACTA_AUDITOR.md`, de las cuales **1** cae dentro del acta 185 | `SALIDA_V201_T1C_CORRECCION_DE_CITA.txt` |
| entradas de `docs/plan/INVENTARIO.jsonl`, recontadas hoy | **672** lineas no vacias y **0** que no son JSON valido | `SALIDA_V201_T2_CORRECCION_OP_I_01.txt` |
| reparto por tipo del inventario, recontado hoy | **556** acto, **54** familia_de_ids, **20** figura, **19** defecto, **13** racimo, **10** dominio, suma **672** | `SALIDA_V201_T2_CORRECCION_OP_I_01.txt` |
| la cifra vieja de `OP-I-01`, citada y no tecleada | **323**, en la linea **44** y en el elemento **1** de su `evidencia` | `SALIDA_V201_T2_CORRECCION_OP_I_01.txt` |
| la guarda de que ningun `estado` se movio | **1** linea difiere de **71**, **1** clave cambia y es `evidencia`, **0** de **71** fichas cambian su `estado` | `SALIDA_V201_T2_GUARDA_ESTADO.txt` |
| elementos de `evidencia` de `OP-L-02` que nombran un fichero | **0** de **1** | `SALIDA_V201_T3_OP_L_02.txt` |
| marcador del cribado, recontado hoy | **3388** filas, **3388** puestos distintos, maximo **3388**, **0** huecos, y **A 551, B 72, C 5, D 2760** que suma **3388** | `SALIDA_V201_T3_OP_L_02.txt` |
| backlog de `OP-L-02` | **189** pares en **4** grupos, **4 de 4** con motivo escrito, suma **189** contra **189** | `SALIDA_V201_T3_OP_L_02.txt` |
| rutas que `OP-L-02` promete como prueba | **8** distintas, **8** vivas, **0** inexistentes, **0** de cero bytes | `SALIDA_V201_T3_OP_L_02.txt` |
| la vara del plan, corrida por mi con el corte de esta vuelta | **71** fichas, **37** que no calzan, **6** en LISTA sin prueba, **4** de trabajo real, **2** consumidas, **24** congeladas declaradas, **12** en silencio, **1** HECHA sin prueba | `SALIDA_V201_T4_VARA.txt` |
| contraste de esa vara contra las cifras del encargo | **0** discrepan | `SALIDA_V201_T4_LECTURA.txt` |
| cobertura de `OP-L-01` | **4** pruebas CUBIERTAS y **0** NO CUBIERTAS | `SALIDA_V201_T4_LECTURA.txt` |
| cobertura de `OP-L-03` | **1** prueba CUBIERTA y **2** NO CUBIERTAS | `SALIDA_V201_T4_LECTURA.txt` |
| los ficheros `docs/plan/OP_L_03_*` que la `evidencia` no nombra | **2**, con **14** filas y **14** actos distintos uno, y **19** filas y **8** actos distintos el otro, **0** lineas no JSON en los dos | `SALIDA_V201_T4_LECTURA.txt` |
| la nomina y el censo, al entrar y al salir | **135** y **135** contra el congelado **135**, censo **197**, vara **148**, fuera **2** con vara y **62** sin vara, **0** invisibles, **0** sin sujeto congelado | `SALIDA_V201_APERTURA.txt` bloque `F` y `SALIDA_V201_CIERRE_MEDICIONES.txt` bloque `D` |
| ficheros sellados de esta vuelta, remedidos DESPUES del cierre | **36** ficheros `SALIDA_V201_*`, **36** vivos y **0** de CERO BYTES, mas ese mismo fichero con **6578** bytes en disco y **6578** normalizados a LF. **La cifra se remidio despues de cerrar a proposito**: el propio cierre escribe su sellada y la del cotejo del tallador, y una cuenta tomada antes se quedaria corta en dos | `SALIDA_V201_CIERRE_MEDICIONES.txt` bloques `G` y `H` |

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V201_APERTURA.txt`, bloque `C`, publica las dos cifras del
estado del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten
LEIDAS de ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**La apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `docs/PENDIENTES.md`: las entradas **`R.61`** (acta 200) y **`R.62`** (acta 198,
  declarando la ausencia de su reporte), anadidas al final. **171 lineas anadidas
  y 0 borradas**, contadas con `git diff --numstat`.
- `docs/loop/reportes/REPORTE_V200.md`: **un aviso de cita de una linea** detras
  del parrafo de su PARADA `1`. **2 lineas anadidas y 0 borradas**. El fichero sale
  en **138307 bytes en disco y 138307 normalizados a LF**, y entraba en
  **137433 en disco y 137433 en LF**, medido antes de escribir.
- `docs/plan/OPERACIONES.jsonl`: **un elemento mas** en la `evidencia` de
  `OP-I-01`, en su linea **44**. Es **la unica escritura de esta vuelta en
  `docs/plan/`**, y va con su guarda medida contra `HEAD`.
- `scripts/loop/`: el bloque de apertura, el esqueleto y el bloque de cierre (los
  tres **clones declarados**, y los dos ultimos generados programaticamente del de
  la 200 para que su codigo vaya byte a byte), **cinco computos de un solo uso con
  prefijo de guion bajo** y **cuatro cuerpos de tarea**.
- `docs/loop/`: las salidas selladas de esta vuelta y el reporte.

**LO QUE NO SE TOCO, Y SE MIDE EN VEZ DE PROMETERSE:**

- **`dataset/` no se toco a mano.** El `numstat` contra `HEAD` sale con **0
  filas** al entrar y **0 al salir**, medido en
  `SALIDA_V201_CICLO_NUMSTAT_APERTURA.txt` y en
  `SALIDA_V201_CICLO_NUMSTAT_CIERRE.txt`, y **contra el HEAD de apertura tambien
  sale en 0 filas**, medido en `SALIDA_V201_CIERRE_MEDICIONES.txt` bloque `C`.
- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se movio.**
  **4054129 bytes en disco y 4054129 normalizados a LF**, con
  `sha256` `0a77b5a35a962621` de disco y `0a77b5a35a962621` de LF,
  **al entrar y al salir**. **Ninguna clase y ningun veredicto se mueven,
  porque mover una clase es del RECOMPUTO.**
- **`web/` y `engine/` en cero filas de `numstat`** por las dos varas, la de
  `HEAD` y la del HEAD de apertura.
- **NINGUN CAMPO `estado` SE MOVIO**, y no se afirma: se mide contra `HEAD` en
  `SALIDA_V201_T2_GUARDA_ESTADO.txt`, que sale **VERDE** con **0 de 71 fichas**
  cambiando su `estado`. La vara del trabajo pendiente es el instrumento, nunca el
  campo (recuadro de `AUDITOR.md` 0).
- **La nomina no crecio ni se podo**: **135** al entrar y **135** al salir, con
  `CASOS_DECLARADOS` en **2** y el censo en **197** las dos veces. **Los dos
  arneses que quedan fuera con la vara 148 siguen fuera**, y son
  `vuelta197_tarea2_mutacion_orden_del_turno.py` y
  `vuelta199_tarea1_mutacion_guardas_revividas.py`.
- **`AUDITOR.md` no se toco**, ni siquiera para la correccion de cita de la
  TAREA 1.c: **el aviso va en el reporte que hizo la cita, no en la regla**.
- **Las dos paradas que la 200 levanto no se tocaron y no se volvieron a
  levantar.** El acta 200 las adjudica en su `4.1` y su `4.2` y **las dos
  reparaciones son de codigo**: la moratoria `6.3` las prohibe hoy y van a la
  auditoria integral.
- **`OP-L-01`, `OP-L-02` y `OP-L-03` se LEYERON y no se movieron:** las tres
  entran y salen en `LISTA` y **ninguna ficha se cerro por cuenta del ejecutor**.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA COTA DE LA `verificacion` DE UNA FICHA JSONL SE CITA COMO LINEA MAS
INDICE, Y ESO LO ELEGI YO.** El encargo manda *"cita su `verificacion` por
linea"*, y las cuatro fichas reales viven **cada una en UNA sola linea** de
`docs/plan/OPERACIONES.jsonl`. Citar solo la linea (**41**, **42** o **43**) no
distingue una clausula de otra, asi que **doy las dos coordenadas juntas, la
linea y el indice del elemento**. **Si la casa queria otra cosa, esta es la
lectura que use y va marcada antes de saberlo.**

**`D.2` LA PRUEBA DE COBERTURA DE LA TAREA 4 ES DE PRESENCIA, NO DE CALIDAD, Y LA
AGUJA LA ELEGI YO.** La declare **antes de correrla**, en la constante `PRUEBAS`
de `scripts/loop/_v201_t4_leer_op_l_01_y_03.py`, justamente para no elegirla
despues de mirar. Pero **quien decide que literal representa a cada elemento de
`evidencia` soy yo**: que `las once con su razon` se compruebe con las once
cabeceras `LD-01` a `LD-11` es una decision de lectura, no una medicion. **Va
marcada.**

**`D.3` DIGO QUE `OP-L-03` TIENE UN HUECO DE EVIDENCIA Y NO DE TRABAJO, Y ESA
FRASE ES UNA INTERPRETACION SOBRE DOS MEDICIONES.** Las dos mediciones son
firmes: el documento que su `evidencia` nombra **no trae ni el literal `reparto
por acto` ni una sola mencion de `OP-L-03`**, y **existen dos ficheros
`docs/plan/OP_L_03_*` que si traen un reparto por acto y que su `evidencia` no
nombra**. **Que eso signifique que el trabajo esta hecho y mal apuntado, y no que
falte, NO lo he medido:** no he leido si esos dos ficheros cubren lo que la ficha
describe. **Lo digo como interpretacion y va marcada.**

**`D.4` NO ESCRIBI LA CORRECCION DECLARADA DE LA `evidencia` DE `OP-L-03`,
AUNQUE SE PARECE MUCHO A LA QUE SI ESCRIBI PARA `OP-I-01`.** El motivo es que **el
encargo adjudica escritura en sede para `OP-I-01` y solo LECTURA MEDIDA para
`OP-L-01` y `OP-L-03`**, y escribir en `docs/plan/` sin adjudicacion es lo que la
casa reserva. **La propongo en la TAREA 4 con su evidencia. Si la lectura correcta
era escribirla, este es el error y va marcado.**

**`D.5` LA CIFRA DE PREGUNTAS DE `R.62` NO SALE DE LA MISMA VIA QUE LA DE
`R.61`.** Para el acta 200 el numeral se filtra contra la seccion de PREGUNTAS de
su reporte archivado; para el acta 198 **ese reporte no existe**, asi que use **las
claves `P.n` nombradas en los titulos `4.n` del acta**. **La entrada lo dice con
todas sus letras**, y prefiero eso a publicar un **0** que se leeria como que el
acta 198 no contesto ninguna pregunta. **Pero son dos varas distintas en la misma
serie, y eso va marcado.**

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LA `verificacion[1]` DE `OP-L-02` DA TRES Y SU `nota` DA SEIS PARA LAS
MISMAS NOMINAS, Y NINGUNA LAS NOMBRA POR ID.** Es la PARADA de esta vuelta.
**Cuales son las nominas afectadas, nombradas por id, y son tres o son seis.** No
lo decido yo.

**`P.2` LA `evidencia` DE `OP-L-03` APUNTA A UN DOCUMENTO QUE NO TRAE LO QUE
PROMETE, Y LOS QUE SI LO TRAEN EXISTEN Y NO ESTAN NOMBRADOS.** Propongo una
correccion declarada de su `evidencia`, del mismo carril que la de `OP-I-01`.
**No la escribo sin adjudicacion.**

**`P.3` `OP-L-01` TIENE SUS CUATRO PRUEBAS DE COBERTURA CUBIERTAS.** Eso **no
dice que su mesa se hiciera bien**, y por eso no la cierro. **Pregunto si toca
mirarla contra el criterio de HECHO de `docs/plan/08_VERIFICACION.md`**, y dejo
nombrado lo unico que la lectura levanta: **la TABLA VIVA DE LOS PUROS declara
vigencia al puesto 1157 y el marcador vale hoy 3388**.

**`P.4` LA DEUDA DE LA SERIE BAJA A 8 Y SON TODAS SEGUIDAS: LAS ACTAS 173 A 180.**
Esta vuelta pago la de la 198 porque el acta 200 la adjudico en su `4.7`. **Las
ocho restantes no las adjudica nadie todavia**, y pregunto si se pagan y en que
orden.

## 7. PENDIENTES DE DOCTRINA

**Ninguno nuevo.** Esta vuelta no encontro ningun par ni ninguna operacion que
pidiera una regla que no existe. Lo que encontro fue **una ficha cuyo texto no
alcanza para ejecutarse sin decidir**, y para eso **la regla si existe** y es
`AUDITOR.md` 3: **es PARADA, no una improvisacion**, y asi va escrita.

## 8. LO QUE LA 202 RECIBE, Y LA UNICA PARADA

**PARADA `1`: `OP-L-02` NO SE PUEDE EJECUTAR SIN DECIDIR, Y NO LA ARREGLO YO.**
Su `verificacion[1]`, en la linea **42** de `docs/plan/OPERACIONES.jsonl`, pide
que **las tres nominas afectadas** queden con cobertura completa y su forma
reescrita; el campo `nota` **de la misma ficha** escribe **`SEIS nominas`** una vez
y **`TRES nominas`** una vez, sobre las mismas nominas; y **ninguna de las dos las
nombra por id**, con `nodos`, `preservar`, `eliminar` y `superviviente` en **0, 0,
0 y `None`**. **Elegir cuales son las tres es decidir, no medir.** `AUDITOR.md` 3
lo llama PARADA con esas palabras. **Lo que hace falta para desbloquearla es una
sola decision escrita, y no es mia.**

**Y NO HAY UNA SEGUNDA PARADA, AUNQUE LA 200 DEJARA DOS.** El acta 200 las
adjudica en su `4.1` y su `4.2`: el rojo de los once tramos es **falso rojo de
censo** y el bloque `F` de `vuelta185_tarea1c_mutacion_bateria_continuada.py` es
**un arnes cuya premisa envejecio**. **Las dos reparaciones son de codigo y van a
la auditoria integral. Esta vuelta ni las toca ni las vuelve a levantar.**

**LO QUE LA 202 SE VA A ENCONTRAR, Y SE DICE PARA QUE NO LO REDESCUBRA:**

- **la racha de cierres vale 2** con las vueltas 199 y 200, asi que el **tope de
  sub-tareas esta en CINCO** y `AUDITOR.md` 6.2 ya no aplica. **Si esta vuelta
  cierra, la racha pasa a 3.**
- **la bateria vuelve en la 205** por la cadencia de cinco de `AUDITOR.md` 6.1,
  contando desde la 200. **Aqui la seccion 9 cierra con hueco declarado.**
- **la nomina sigue congelada en 135** y **los dos arneses que el censo ve y ella
  no tiene siguen fuera**, con la vara 148. **Sin vara son 62.**
- **quedan DOS de las cuatro fichas reales sin resolver**: `OP-L-02`, que es la
  PARADA de arriba, y `OP-L-03`, cuya `evidencia` propongo corregir.
- **`OP-L-01` queda con sus cuatro pruebas de cobertura cubiertas** y **propuesta,
  no cerrada**.
- **`OP-I-01` ya tiene su correccion declarada en su sede**, con las dos cifras y
  sus dos fechas de corte, y **su campo `estado` sin mover**.
- **la deuda de la serie son 8 actas seguidas**, de la **173** a la **180**.
- **el lanzador de la bateria sigue sellando con nombre de 183**, asi que la
  corrida de la 200 vive en `SALIDA_V183_BATERIA.txt`. **No es que la 200 no
  corriera la bateria: es que su salida no se llama como su vuelta**, y el acta
  200 ya lo adjudica.
