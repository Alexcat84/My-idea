# REPORTE DE LA VUELTA 187 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta187_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189**. En las vueltas intermedias la seccion 9
> se cierra igual, con el **nombre del fichero, sus bytes medidos y su
> atribucion**, las tres juntas o no vale.
>
> **EL TOPE VUELVE A CINCO, Y ESTA MEDIDO EN VEZ DE DARSE POR BUENO.** El
> regimen temporal `AUDITOR.md` 6.2 devolvia el tope a cinco cuando **dos vueltas
> seguidas cerraran su propio reporte** con `scripts/loop/cerrar_reporte.py`. El
> **bloque H.0** del sello de apertura de esta vuelta midio las dos salidas de
> cierre, `docs/loop/SALIDA_V185_CERRAR_REPORTE.txt` y
> `docs/loop/SALIDA_V186_CERRAR_REPORTE.txt`, y **las dos dicen `CIFRA piezas que
> faltan: 0`**. **El regimen se apaga por su propio disparador de salida**, y esta
> vuelta lleva **CINCO tareas**.
>
> **Y CON EL TOPE EN CINCO SE ACABA LA ARITMETICA QUE APLAZABA EL PLAN.** El plan
> lleva **seis vueltas sin moverse**, y **por eso el par 2.464 y el tramo 1 de la
> cola post fusion van en la TAREA 2, delante de toda la maquinaria salvo los
> registros**. **Si esta vuelta se corta por falta de sitio, que se caiga la
> maquinaria, no el plan.**
>
> **DONDE SE TALLO ESTE ESQUELETO, DICHO SIN REDONDEAR.** No en la apertura, sino
> **despues de la TAREA 1**. La apertura si corrio primero y entera
> (`docs/loop/SALIDA_V187_APERTURA.txt`, con el ciclo de Gate 0 dentro), pero este
> esqueleto necesita que `docs/loop/SALIDA_V187_HEAD_APERTURA.txt` este
> **commiteado** para poder leer su commit de nacimiento con
> `git log --diff-filter=A`, y ese commit es el de la TAREA 1. **Se declara en vez
> de disimularse**, que es lo que el banco 9 manda: lo que `EJECUTOR.md` 1 protege
> es que una vuelta cortada deje reporte parcial y no vacio, y desde este punto
> eso se cumple.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** **no se abre la
> mesa de los tres nodos de la puerta del `PMF`** (puestos 338 y 297), ni la del
> **603**, ni la de **figuras del 226**; las tres estan anotadas en el acta 187,
> seccion 6.2, con sede en `docs/PENDIENTES.md`, y son trabajo de plan de otra
> vuelta. **No se poda la nomina de la bateria**, que es la opcion `c` que el
> fundador RECHAZO el 5 sep, y aqui se hace lo contrario, que es completarla. **No
> se reabre ni se reescribe `docs/loop/reportes/REPORTE_V184.md`**, que ya esta
> cerrado y archivado: lo que se le anade es la DECLARACION de su defecto. Y **no
> se toca `dataset/`**: el `numstat` se mide al entrar y al salir y las dos cifras
> se publican.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta187_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 186: `620dc837`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 186: LA 185 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA, ADJUDICO LOS SIETE DISCUTIBLES A FAVOR, CIERRO PD.5 Y PD.6 POR CITA Y CONTESTO LAS TRES PREGUNTAS QUE ERAN MIAS.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V187_HEAD_APERTURA.txt`: `2a8cb229`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `07826009`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **186**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 187`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 187 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SEIS adjudicaciones `5.1` a `5.6` todas a favor, los DOS numerales de la seccion 6 (`PD.1` ABIERTA con sus cinco puestos leidos del acta, y el `6.2` como CORRECCION POR DECLARACION, que es un ESTADO NUEVO: la `PD.7` del reporte de la 186 NO es un pendiente de doctrina y el numero `PD.7` queda libre), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, UNA caida del ejecutor de reporte (`C.1`, la de las cuatro cifras de LF supuestas) que NO acumula y cuya ESPECIE el acta 187 corrige, y la deuda de la serie REMEDIDA en esta vuelta. Con caso positivo por mutacion sobre un acta FABRICADA, el esperado mutado cayendo, y el registrador aprendiendo el estado nuevo y haciendo PARADA ante uno que no sepa leer | **CERRADA** | `docs/loop/SALIDA_V187_T1A_REGISTRO_R49.txt`, `docs/loop/SALIDA_V187_T1A_MUTACION_REGISTRO_187.txt` |
| **TAREA 2** | EL PLAN SE MUEVE: EL PAR 2.464 Y EL TRAMO 1 DE LA COLA POST FUSION. Se LEE el disparador escrito antes de tocar nada y se cita por numero; el par 2.464 encabeza y detras va el tramo 1 tal como el disparador lo defina, con el tamano del tramo COMPUTADO del criterio escrito y no inventado; cada par que se mueva lleva su CORRECCION DECLARADA y su RECOMPUTO por la letra de `AUDITOR.md` 1.3; el `sha256` del archivo se publica AL ABRIR y AL CERRAR, y si esta tarea mueve algo el de cierre tiene que ser distinto y la diferencia se explica par por par; y el marcador se RECOMPUTA del archivo con su comando. NO se abre la mesa del `PMF`, ni la del 603, ni la de figuras del 226 | **CERRADA. **EL PLAN SE MOVIO:** el `sha256` LF del archivo pasa de `ea6e850d331d14f0` a `0a77b5a35a962621`** | `docs/loop/SALIDA_V187_T2_COLA_POST_FUSION.txt`, `docs/loop/SALIDA_V187_T2B_TRAMO1_CERRADO.txt` |
| **TAREA 3** | LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 187, encargada por `AUDITOR.md` 1.2 porque las CUATRO discrepancias del auditor cayeron FUERA del discutible de clase marcado. Cotejo de `sha256` contra el sello `V188` ANTES de leer un solo puesto; 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA; solape 0 contra el tramo, contra la ciega anterior y contra los 293 puestos de la exclusion, MEDIDO y no supuesto; 60 puestos releidos que es el doble exacto; NINGUNA CLASE SE VUELVE A DECIDIR. Mas los cuatro puestos 226, 603, 1612 y 2448 mirados con la misma vara, y el censo de las `B` del universo releido con sus tres comprobaciones mecanicas una a una | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA ESCALADA: LA PAREJA DE CONVENCIONES DEJA DE BASTAR CON EXISTIR. `AUDITOR.md` 1.2, mandatorio a partir de dos. Una guarda que, para cada ruta que el reporte publique con cifra de bytes, RECOMPUTA LAS DOS CONVENCIONES DESDE EL DISCO y las coteja contra las dos publicadas, cayendo en ROJO si alguna discrepa y nombrando la ruta, la cifra publicada, la medida y cual de las dos convenciones falla. REUSA lo que `scripts/loop/vuelta186_rutas_del_reporte.py` ya sabe hacer: una sede, dos llamadores y NO un tercero. Funciones PURAS y un solo lector de disco, cableada donde `cerrar_reporte.py` juzga y SIN bandera. Con arnes obligatorio que incluye UN CASO SOBRE EL TEXTO REAL DE `git show bb3aaad3` exigiendo que HABRIA CAZADO LAS CUATRO CIFRAS DE LA `C.1` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LA NOMINA, LA DECLARACION DEL 184 Y EL CIERRE. (a) Los CUATRO arneses de la 186 entran en la nomina MAS los que nazcan hoy, con `arneses_que_faltan()` devolviendo 0 al cerrar, el tamano de la nomina antes y despues, y cada arnes nuevo corrido DOS VECES en procesos aparte exigiendo el mismo `sha256`. NO SE PODA NADA. (b) La declaracion del defecto del reporte de la 184, que es la `P.2`: en el carril de CIERRE TARDIO la guarda de la `2.d` NO bloquea pero SE DECLARA con su motivo entero, en el carril NORMAL sigue bloqueando entera, `REPORTE_V184.md` NO se reabre, y con arnes propio. (c) La cifra inutil del bloque H.5, reparada con la cifra antes y despues. (d) El reporte de la 187 se abre, se llena por anexion y se cierra con `cerrar_reporte.py --vuelta 187` y `archivar_reporte.py --vuelta 187`, con la cabecera tallada y `--comparar` dando CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS. **CERRADA.**

**EL NUMERO NO SE TECLEO.** `scripts/loop/serie_de_registros.py`, corrido en esta
vuelta, recomputo la serie de sus **dos sedes** (`docs/PENDIENTES.md` y
`docs/plan/CORRECCIONES_A_APLICAR.md`), hallo **40 entradas**, **0 colisiones**,
**0 huecos**, y devolvio **`R.49`**. El encargo tambien decia `R.49`, y las dos
cifras se publican al lado: **la que manda es la del instrumento**.

**LA ENTRADA ESCRITA:** `## R.49. Registro de las seis adjudicaciones numeradas,
los dos numerales de la seccion 6, las tres preguntas contestadas, las cero
caidas propias del auditor y la caida de reporte del ejecutor del acta de la
vuelta 187`. **Los cinco numerales del titulo estan CONTADOS del acta acotada**
(`docs/loop/ACTA_AUDITOR.md`, lineas **65441 a 66070**, 630 lineas) **y no
tecleados**, incluida la concordancia en palabra.

| que se conto | cifra | de donde sale |
|---|---:|---|
| adjudicaciones `5.1` a `5.6` | **6** | patron entrecomillado sobre el acta acotada |
| el mismo patron SIN comillas, el del acta 183 | **0** | se conserva intacto y su cero se publica |
| numerales de la seccion 6 | **2** | `6.1` y `6.2` |
| preguntas de la seccion 7 | **3** | `7.1`, `7.2` y `7.3`, las tres CONTESTADAS |
| caidas propias del auditor, patron `A.n` | **0** | y **declaradas**: la frase `CERO CAIDAS PROPIAS` esta en la linea **65460** |
| caidas del ejecutor | **1** | la `C.1`, en la linea **65857** |

**LAS SEIS ADJUDICACIONES SON A FAVOR, LAS SEIS.** El acta no regatea ninguna.

**EL ESTADO NUEVO, QUE ES LA PRIMERA DE LAS DOS COSAS QUE ESTE REGISTRADOR
ESTRENA.** El `6.2` del acta 187 no cierra un pendiente, no lo deja abierto y no
es la anotacion de un trabajo ajeno: es una **CORRECCION POR DECLARACION**. El
registrador de la 186 sabia leer `ABIERTA`, `CERRADA` y `ANOTACION`, y con este
titulo habria sacado `SIN DECIR` y habria hecho **PARADA**. El cuarto estado se
lee del titulo con la marca literal `NO ES UN PENDIENTE DE DOCTRINA`, y **la
PARADA se conserva entera**: un estado que el registrador no sabe leer sigue
siendo PARADA y **no se mete en el saco de los abiertos ni en el de los
cerrados**. El reparto medido: **CERRADAS 0, ABIERTAS 1, ANOTACIONES 0,
CORRECCIONES POR DECLARACION 1**.

> **Y LA CONSECUENCIA SE REGISTRA CON TODAS LAS LETRAS: LA `PD.7` DEL REPORTE DE
> LA 186 NO ES UN PENDIENTE DE DOCTRINA, Y EL NUMERO `PD.7` QUEDA LIBRE.**

**LA ATRIBUCION DE LA CAIDA, QUE ES LA SEGUNDA, Y ES LA QUE HABRIA PUBLICADO UNA
CIFRA FALSA.** El patron `C.n` nombraba **las caidas propias del AUDITOR** en las
actas 178 a 184, y el acta 187 usa `C.1` para **la caida del EJECUTOR**. Corrido
a secas sobre esta acta, ese patron da **1**, que es exactamente **una caida
propia del auditor donde el acta declara CERO**. Aqui la atribucion **no la hace
el patron: la hace LA SECCION en que la caida vive**, leyendo su cabecera:

```
   EL PATRON `C.n` A SECAS, SIN MIRAR LA SECCION: 1
   Y REPARTIDO POR LA CABECERA DE SU SECCION, QUE ES LA ATRIBUCION BUENA:
      DEL EJECUTOR: 1
         LINEA 65857: C.1 bajo '## 8. LA CAIDA PROPIA DEL EJECUTOR, Y LE CORRIJO LA ESPECIE'
      DEL AUDITOR: 0
      HUERFANAS (sin dueno declarado en su cabecera): 0
```

**Una `C.n` bajo una cabecera que no dice de quien es sale HUERFANA y hace
PARADA.** Una caida sin dueno no se reparte a ojo.

**LOS CINCO PUESTOS DE LA `PD.1`, LEIDOS DEL ACTA Y NO COPIADOS DEL ENCARGO:**
**1778, 2530, 2540, 3141, 3232**. Sexta vuelta abierta.

**LA DEUDA DE LA SERIE, REMEDIDA HOY Y NO HEREDADA DEL `R.48`:** tramo mirado
actas **173 a 186**, **8 actas sin entrada propia** (**173 a 180**), extremo bajo
**`R.42` cubre el acta 172** y extremo alto **`R.43` cubre el acta 181**. **No se
rellenan aqui.**

**EL CASO POSITIVO POR MUTACION, SOBRE UN ACTA FABRICADA Y NUNCA SOBRE LA REAL**,
que es lo que el encargo manda con esas palabras. **Doce mutaciones, `CIFRA
fallos: 0`, `VEREDICTO: VERDE`.** Las dos que importan hoy:

| mutacion | que prueba | con el esperado mutado |
|---|---|---|
| la **cuarta** | el cuarto estado sale `CORRECCION POR DECLARACION` sobre un acta fabricada, y **no aparece donde no lo hay** | **CAE** |
| la **quinta** | un `6.n` cuyo titulo no dice ninguna de las cuatro marcas sale **`SIN DECIR`**, que es la PARADA | **CAE** |
| la **sexta** | la misma `C.1` bajo cabecera del EJECUTOR es del ejecutor; bajo una sin dueno sale **HUERFANA** | **CAE** |
| la **octava** | los patrones `R.n` y `E.n` dan **0** sobre una caida escrita como `C.n`, y ese cero es la medicion que prueba que hacia falta la atribucion por seccion | |

**IDEMPOTENCIA COMPROBADA ANTES DE ESCRIBIR:** la marca `## R.49.` no estaba en
la sede. Escrita, `docs/PENDIENTES.md` pasa de **909780 a 924954 bytes**, la
entrada se releyo del disco byte a byte, **0 guiones largos o medios**, y la
serie recomputada DESPUES da **41 entradas**, siguiente libre `R.50`, **0
colisiones y 0 huecos**.

### TAREA 2. EL PLAN SE MUEVE: EL PAR 2.464 Y EL TRAMO 1 DE LA COLA POST FUSION. **CERRADA.**

> **EL PLAN SE MOVIO.** El `sha256` por la convencion de LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre en `ea6e850d331d14f0` y cierra en
> `0a77b5a35a962621`. **Son distintos**, y la diferencia se explica par por par
> mas abajo: **una fila tocada de 3388**.

**1. EL DISPARADOR, LEIDO ANTES DE TOCAR NADA Y CITADO CON SU LINEA.** No se cita
de memoria: `scripts/loop/vuelta187_tarea2_cola_post_fusion.py` lo localiza en el
fichero vivo y lo pega. **Si la seccion no estuviera, el instrumento cae en ROJO
y no relee nada.**

| pieza del criterio | donde vive, leido hoy | que dice |
|---|---|---|
| la sede | `docs/plan/08_VERIFICACION.md`, seccion `## LA COLA DE RELECTURA POST FUSION`, lineas **485 a 848** (364 lineas) | |
| **el disparador** | linea **491** | *"UN PAR VUELVE A LA COLA CUANDO UNO DE SUS DOS NODOS MUERE EN UNA FUSION O CAMBIA DE TEXTO"* |
| **la declaracion del tramo** | linea **585** | *"TRAMO 1 y unico con lo medido hoy: el unico par de arriba"*, y *"se relee entero o no cuenta"* |
| **la tabla de destinos** | linea **616** | si sale `A` entra en la fusion; **si sale `D` se queda**; si sale `B` otra vez va al inventario final |
| la tabla del tramo | linea **583** | el puesto **2464** |

**LA DISCREPANCIA CON EL ENCARGO, DECLARADA Y NO RESUELTA COPIANDO**
(`EJECUTOR.md` 2). El encargo dice que el criterio esta escrito *"en
`docs/plan/08_VERIFICACION.md` y en el `BANCO_DEL_PLAN`"*. **Medido hoy sobre
`docs/plan/BANCO_DEL_PLAN.md`: `post fusion` 0, `POST FUSION` 0, `cola post
fusion` 0, `2464` 0, `2.464` 0.** El criterio vive **entero y solo** en
`08_VERIFICACION.md`. **NO ES PARADA**, y se dice por que: el texto de
`08_VERIFICACION.md` **alcanza para ejecutar el tramo sin decidir nada**, que es
la condicion exacta que el encargo pone.

**Y UNA PRECISION SOBRE "CITALO POR NUMERO":** `08_VERIFICACION.md` **no numera
sus clausulas** como el `BANCO_DEL_PLAN` numera sus `P.n`. Se cita **por seccion
y por linea del fichero vivo**, que es la unica numeracion que ese fichero tiene.

**2. EL TAMANO DEL TRAMO, COMPUTADO DEL CRITERIO Y NO INVENTADO.** La criba
escrita en la propia seccion es **2760 `D` -> 99 que declaran diferenciador -> 6
que hoy lo tienen en el otro nodo -> 1 cuyo paso entro DESPUES del veredicto**, y
el parrafo del tramo dice *"el unico par de arriba"*. **ASI QUE EL TRAMO 1 SON 1
PAR: el 2464.** La lista no se tecleo: se leyo de la tabla de la linea 583.

**LA CRIBA, RE CORRIDA HOY SOBRE EL ARCHIVO ENTERO**, con la maquina IMPORTADA de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py` (varas `VARA_ABSOLUTA 3`
y `VARA_COBERTURA 0.45`, tambien importadas) **y sin correr su `main()`**, que
reescribiria evidencia sellada de la vuelta 182:

| que se conto | cifra |
|---|---:|
| `D` en el archivo | **2760** |
| `D` que declaran diferenciador | **99** |
| `D` con lesion exacta hoy, condiciones 1 y 2 | **6** |
| las que la criba nombra | **1778, 2464, 2530, 2540, 3141, 3232** |
| de ellas, fuera del tramo 1 | **1778, 2530, 2540, 3141, 3232** |

**Y ESAS CINCO DE MAS NO SON UN TRAMO NUEVO: SON LA `PD.1`, Y SE COTEJARON.** Esta
criba corre solo las condiciones 1 y 2; la tercera, que el paso entrara DESPUES
del veredicto, la fecho en git la vuelta 182. Los cinco que no la pasan son
**exactamente** los cinco que el registro `R.49` leyo del acta 187 (`6.1`):
**`SON LOS MISMOS CINCO: SI`**. **No pasan el disparador escrito y no se
encolan**: darles cola seria doctrina nueva, que es del fundador.

**3. LA RELECTURA DEL 2464, CON LOS PASOS DE HOY DE LOS DOS NODOS.**

| | `cero_defectos` | `zero_defects_concepto` |
|---|---:|---:|
| pasos hoy | **7** | **4** |

**LO QUE LA VARA MIDE:** *"hoy el paso 7 de `cero_defectos` cubre 3 palabras del
diferenciador declarado (cobertura 0.50)"*. El item declarado que se movio es
*"ELIMINAR EXPLICITAMENTE EL USO DE NIVELES DE CALIDAD ACEPTABLES como estandar"*
y el paso de hoy que lo cubre es *"Eliminar el lenguaje que normaliza niveles
aceptables de error (AQL)"*.

**LO QUE LA RELECTURA SOSTIENE, Y ES CLASE `D`:**

- la razon declaraba **DOS** cosas que `zero_defects_concepto` traia y el otro
  no. **De las dos, UNA ya no es diferenciador**: el AQL esta hoy en el paso 7 de
  `cero_defectos`, que una fusion nuestra le metio despues del veredicto.
- **LA OTRA SOBREVIVE ENTERA:** el arranque a escala minima. El paso 3 de
  `cero_defectos` habla de *"una fecha de lanzamiento (Dia de Cero Defectos) tras
  un periodo breve de preparacion para darle visibilidad"*, y **no** de *"aunque
  sea contigo mismo"* ni de *"poner por escrito un compromiso entre tu y la
  persona que te ayuda"*, que son los pasos 3 y 4 del otro nodo.
- **los diferenciadores del otro lado siguen intactos:** el despliegue caso por
  caso (paso 2), el reconocimiento genuino evitando el efectivo (paso 4) y la
  extension del estandar a todas las areas (paso 5) **no estan** en los cuatro
  pasos de `zero_defects_concepto`.

> **LOS DOS NODOS SIGUEN SANOS, ASI QUE LA CLASE NO SE MUEVE, QUE ES LO QUE LA
> TABLA DE DESTINOS MANDA PARA UNA `D`.** Lo que SI se movio es **la evidencia**:
> la razon vieja sostenia la `D` en dos diferenciadores y hoy **solo uno de los
> dos es cierto**.

**4. LA CORRECCION DECLARADA, SIN BORRAR EL TEXTO VIEJO.** La razon pasa de
**944 a 3106 caracteres**; **el texto viejo sigue entero dentro del nuevo: `SI`**;
la marca de correccion esta: `SI`; **0 guiones largos o medios**. **Ningun
veredicto se movio en silencio.**

**PENDIENTE DE DOCTRINA (`EJECUTOR.md` 5), Y SE DECLARA EN VEZ DE RESOLVERSE
SOLO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` tiene **ocho campos** y **ninguno es
de correccion**: contadas hoy sus 3388 filas, las claves son `puesto_intra`,
`dominio`, `nodo_a`, `nodo_b`, `clave`, `banda_078_080`, `clase` y `razon`, y
**ninguna fila ha llevado nunca un campo de correccion**. **La FORMA de una
correccion declarada dentro de este archivo no esta escrita en ninguna
doctrina.** Se registro lo mejor sostenido (anexar a la `razon` sin borrar nada,
con marca literal y vuelta) y **queda marcado PENDIENTE DE DOCTRINA dentro de la
propia razon**, para que el fundador decida la sede definitiva. **No se para**,
porque la regla 5 dice expresamente que no se para.

**5. EL MARCADOR, RECOMPUTADO DEL ARCHIVO CON SU COMANDO Y NO AJUSTADO A MANO**
(`python scripts/loop/vuelta187_tarea2_cola_post_fusion.py`, bloques F y H):

| | al abrir | al cerrar |
|---|---:|---:|
| filas | **3388** | **3388** |
| puestos unicos | **3388** | **3388** |
| min / max | **1 / 3388** | **1 / 3388** |
| huecos | **0** | **0** |
| duplicados | **0** | **0** |
| `A` | **551** | **551** |
| `B` | **72** | **72** |
| `C` | **5** | **5** |
| `D` | **2760** | **2760** |

**EL MARCADOR NO SE MOVIO, Y ES LO QUE TIENE QUE PASAR:** la relectura sostiene
la clase, asi que lo que cambia es la **evidencia** de la razon y no el reparto
por clase. **El `sha256` SI cambio**, y por eso hay que decir las dos cosas
juntas.

**6. EL TRAMO SE CIERRA EN SU PROPIA SEDE, Y SUS CIFRAS TAMPOCO SE TECLEAN.**
`scripts/loop/vuelta187_tarea2b_cerrar_tramo1_en_el_plan.py` anexa el registro
`#### REGISTRO: EL TRAMO 1 SE RELEYO Y SE CIERRA` **por adicion y dentro de la
seccion de la cola**, leyendo cada cifra del archivo de veredictos y de la salida
de la TAREA 2. `docs/plan/08_VERIFICACION.md` pasa de **67121 a 69068 bytes**; el
registro se releyo del disco byte a byte; la seccion **sigue siendo una** y ahora
va de la **485 a la 879**; el disparador, la declaracion del tramo y la marca del
registro **siguen los tres dentro**; **0 guiones largos o medios en la sede
entera**.

**LA COMPROBACION QUE LA PROPIA SECCION EXIGE, CORRIDA:** *"al cerrar, ningun par
de la lista sigue con su clase vieja apuntando a un nodo que ya no existe"*.
Medido sobre `dataset/metadata/master_graph.json` (**3853 nodos**): **`nodo_a`
vivo SI, `nodo_b` vivo SI**. **Pasa.**

**7. LO QUE ESTA TAREA NO ABRIO, Y EL ENCARGO SE LO PROHIBE CON ESAS PALABRAS:**
la mesa del `PMF` (puestos **338** y **297**), la del **603** y la de figuras del
**226**. Las tres estan anotadas en el acta 187, seccion `6.2`, con sede en
`docs/PENDIENTES.md`.

<!-- FIN ANEXO DE TAREAS -->
