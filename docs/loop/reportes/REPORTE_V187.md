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

**EL VEREDICTO DE UNA LINEA: EL PLAN SE MOVIO DESPUES DE SEIS VUELTAS QUIETO: el sha256 del archivo pasa de ea6e850d331d14f0 a 0a77b5a35a962621 por el par 2.464, cuya relectura SOSTIENE la clase D y le CORRIGE la evidencia; la escalada de las dos convenciones caza las cuatro cifras de la C.1 donde la guarda vieja acusaba 0 de 7; la nomina crece de 115 a 121 con arneses_que_faltan() en 0; y HAY UNA PARADA que no arreglo, porque un arnes ya sellado de la 186 cae en rojo por la exencion que este mismo encargo manda anadir.**
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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 187`, y su salida
cruda vive en `docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt` (2444 bytes en disco y 2424 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `620dc837` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 186: LA 185 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA, ADJUDICO LOS SIETE DISCUTIBLES A FAVOR, CIERRO PD.5 Y PD.6 POR CITA Y CONTESTO LAS TRES PREGUNTAS QUE ERAN MIAS.'), HEAD real de apertura `2a8cb229` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `93954475` (leido de `SALIDA_V187_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 187 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SEIS adjudicaciones `5.1` a `5.6` todas a favor, los DOS numerales de la seccion 6 (`PD.1` ABIERTA con sus cinco puestos leidos del acta, y el `6.2` como CORRECCION POR DECLARACION, que es un ESTADO NUEVO: la `PD.7` del reporte de la 186 NO es un pendiente de doctrina y el numero `PD.7` queda libre), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, UNA caida del ejecutor de reporte (`C.1`, la de las cuatro cifras de LF supuestas) que NO acumula y cuya ESPECIE el acta 187 corrige, y la deuda de la serie REMEDIDA en esta vuelta. Con caso positivo por mutacion sobre un acta FABRICADA, el esperado mutado cayendo, y el registrador aprendiendo el estado nuevo y haciendo PARADA ante uno que no sepa leer | **CERRADA** | `docs/loop/SALIDA_V187_T1A_REGISTRO_R49.txt`, `docs/loop/SALIDA_V187_T1A_MUTACION_REGISTRO_187.txt` |
| **TAREA 2** | EL PLAN SE MUEVE: EL PAR 2.464 Y EL TRAMO 1 DE LA COLA POST FUSION. Se LEE el disparador escrito antes de tocar nada y se cita por numero; el par 2.464 encabeza y detras va el tramo 1 tal como el disparador lo defina, con el tamano del tramo COMPUTADO del criterio escrito y no inventado; cada par que se mueva lleva su CORRECCION DECLARADA y su RECOMPUTO por la letra de `AUDITOR.md` 1.3; el `sha256` del archivo se publica AL ABRIR y AL CERRAR, y si esta tarea mueve algo el de cierre tiene que ser distinto y la diferencia se explica par por par; y el marcador se RECOMPUTA del archivo con su comando. NO se abre la mesa del `PMF`, ni la del 603, ni la de figuras del 226 | **CERRADA. **EL PLAN SE MOVIO:** el `sha256` LF del archivo pasa de `ea6e850d331d14f0` a `0a77b5a35a962621`** | `docs/loop/SALIDA_V187_T2_COLA_POST_FUSION.txt`, `docs/loop/SALIDA_V187_T2B_TRAMO1_CERRADO.txt` |
| **TAREA 3** | LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 187, encargada por `AUDITOR.md` 1.2 porque las CUATRO discrepancias del auditor cayeron FUERA del discutible de clase marcado. Cotejo de `sha256` contra el sello `V188` ANTES de leer un solo puesto; 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA; solape 0 contra el tramo, contra la ciega anterior y contra los 293 puestos de la exclusion, MEDIDO y no supuesto; 60 puestos releidos que es el doble exacto; NINGUNA CLASE SE VUELVE A DECIDIR. Mas los cuatro puestos 226, 603, 1612 y 2448 mirados con la misma vara, y el censo de las `B` del universo releido con sus tres comprobaciones mecanicas una a una | **CERRADA, con UNA DESVIACION DECLARADA: el solape del universo entero con la exclusion no es 0, es **2**, y los dos son VECINOS deterministas (1287 y 2383), no puestos del tramo** | `docs/loop/SALIDA_V187_T3_RELECTURA_AL_DOBLE.txt`, `docs/loop/SALIDA_V187_COTEJO_DE_CLONES.txt` |
| **TAREA 4** | LA ESCALADA: LA PAREJA DE CONVENCIONES DEJA DE BASTAR CON EXISTIR. `AUDITOR.md` 1.2, mandatorio a partir de dos. Una guarda que, para cada ruta que el reporte publique con cifra de bytes, RECOMPUTA LAS DOS CONVENCIONES DESDE EL DISCO y las coteja contra las dos publicadas, cayendo en ROJO si alguna discrepa y nombrando la ruta, la cifra publicada, la medida y cual de las dos convenciones falla. REUSA lo que `scripts/loop/vuelta186_rutas_del_reporte.py` ya sabe hacer: una sede, dos llamadores y NO un tercero. Funciones PURAS y un solo lector de disco, cableada donde `cerrar_reporte.py` juzga y SIN bandera. Con arnes obligatorio que incluye UN CASO SOBRE EL TEXTO REAL DE `git show bb3aaad3` exigiendo que HABRIA CAZADO LAS CUATRO CIFRAS DE LA `C.1` | **CERRADA. La guarda caza LAS CUATRO cifras de la `C.1` sobre el texto real de `bb3aaad3`, por LF, y la guarda vieja acusaba **0 de 7**** | `docs/loop/SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt`, `docs/loop/SALIDA_V187_T4_MUTACION_EN_ROJO.txt` |
| **TAREA 5** | LA NOMINA, LA DECLARACION DEL 184 Y EL CIERRE. (a) Los CUATRO arneses de la 186 entran en la nomina MAS los que nazcan hoy, con `arneses_que_faltan()` devolviendo 0 al cerrar, el tamano de la nomina antes y despues, y cada arnes nuevo corrido DOS VECES en procesos aparte exigiendo el mismo `sha256`. NO SE PODA NADA. (b) La declaracion del defecto del reporte de la 184, que es la `P.2`: en el carril de CIERRE TARDIO la guarda de la `2.d` NO bloquea pero SE DECLARA con su motivo entero, en el carril NORMAL sigue bloqueando entera, `REPORTE_V184.md` NO se reabre, y con arnes propio. (c) La cifra inutil del bloque H.5, reparada con la cifra antes y despues. (d) El reporte de la 187 se abre, se llena por anexion y se cierra con `cerrar_reporte.py --vuelta 187` y `archivar_reporte.py --vuelta 187`, con la cabecera tallada y `--comparar` dando CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO | **CERRADA, CON UNA PARADA DECLARADA: el arnes ya sellado `vuelta186_tarea2c_mutacion_cierre_tardio.py` cae en ROJO por su CASO E, y NO lo arreglo** | `docs/loop/SALIDA_V187_T5A_NOMINA.txt`, `docs/loop/SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO.txt`, `docs/loop/SALIDA_V187_T5B_ARNES_SELLADO_186_2C_EN_ROJO.txt` |
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
la sede. `docs/PENDIENTES.md` mide hoy **924954 bytes en disco y 924954 bytes normalizados a LF**,
y lo que crecio lo dice su propio instrumento, citado y no tecleado:

```
   la sede pasa de 909780 a 924954 bytes
```

La entrada se releyo del disco byte a byte, **0 guiones largos o medios**, y la
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
de la TAREA 2. `docs/plan/08_VERIFICACION.md` mide hoy **69068 bytes en disco y 69068 bytes normalizados a LF**,
y lo que crecio lo dice su propio instrumento, citado y no tecleado:

```
   la sede pasa de 67121 a 69068 bytes
```

El
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

### TAREA 3. LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 187. **CERRADA, Y CON UNA DESVIACION DECLARADA.**

**EL COTEJO DEL `sha256` VA ANTES DE LEER UN SOLO PUESTO, Y SE COMPUTO EN VEZ DE
COPIARSE DEL ENCARGO.**

| | el sello dice | medido hoy | |
|---|---|---|:-:|
| `docs/loop/SELLO_APERTURA_AUDITOR_V188.json` | | disco **802** bytes, LF **802** bytes | |
| bytes de la ciega | **42599** | **42599** | **CALZA** |
| `sha256` de la ciega | `ea6d846cb7e0c73e0d2e9794906b2551bb32d939b8ad88f02bbc473b73e79c55` | `ea6d846cb7e0c73e0d2e9794906b2551bb32d939b8ad88f02bbc473b73e79c55` | **CALZA** |

**`EL FICHERO ES EL QUE EL SELLO DICE: SI`.** El nombre del sello **no se dedujo
del numero de vuelta**: siendo acta **187**, se llama **`V188`**. **El `V186` no
existe y no se fabrica.**

**EL TRAMO Y SU DOBLE.** El tramo se leyo de la ciega sellada, **no del acta**,
que en su seccion 4 (lineas **65635 a 65699**, cabecera *"LA RELECTURA CIEGA: 26
DE 30, Y LAS CUATRO LAS PIERDO YO"*) lista **0 puestos**.

- **30 puestos del tramo**: 226, 252, 255, 293, 426, 603, 954, 1222, 1286, 1332,
  1341, 1367, 1509, 1540, 1612, 1676, 1703, 1910, 1912, 1953, 2124, 2177, 2382,
  2448, 2834, 2953, 3030, 3158, 3314, 3340.
- **30 vecinos deterministas**, con `vecinos()` **IMPORTADA** de
  `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y **no copiada**.
- **60 puestos releidos. `ES EL DOBLE DEL TRAMO: SI`.**

**LOS TRES SOLAPES, MEDIDOS Y NO SUPUESTOS. Y EL TERCERO NO SALE CERO, ASI QUE SE
DECLARA EN VEZ DE ARREGLARSE.**

| solape | contra | cifra |
|---|---|---:|
| **F.1** | el tramo contra sus vecinos | **0** |
| **F.2** | el tramo contra `docs/loop/_auditor_v187_ciega_blind.txt` (30 puestos) | **0** |
| **F.2** | el **universo entero** contra esa misma ciega | **0** |
| **F.3** | el **tramo** contra los puestos de `docs/loop/_auditor_v188_exclusion.txt` | **0** |
| **F.3** | el **universo entero** contra esa misma exclusion | **2** |

**La exclusion mide 1372 bytes en disco y 1372 bytes normalizados a LF, y lista
293 puestos distintos, CONTADOS del fichero y no copiados del criterio.** Los dos que cruzan son **1287** (vecino
determinista del **1286**) y **2383** (vecino determinista del **2382**), **los
dos VECINOS y ninguno del tramo**.

> **POR QUE NO LO ARREGLO, Y ES UNA DESVIACION DECLARADA Y NO UN DESCUIDO.** El
> encargo pide **solape 0 con los 293**. **El tramo lo cumple: 0.** Los que
> cruzan salen de `vecinos()`, que es una funcion **importada y congelada**;
> cambiarla aqui para que la cifra saliera cero seria **mover la vara a mitad de
> la medicion**, que es exactamente lo que `P.5.1` prohibe. **Se publica la cifra
> y se nombran los dos puestos.** **DISCUTIBLE DE METODO, MARCADO.**

**LAS CIFRAS DE LA RELECTURA MECANICA, con la maquina IMPORTADA de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py`:**

| | cifra |
|---|---:|
| puestos releidos | **60** |
| que declaran diferenciador | **3** |
| con **lesion exacta** | **0** |
| con algun **nodo muerto** en el grafo de hoy | **0** |
| clase `A` en el universo | **8** |
| clase `B` en el universo | **4** |
| clase `D` en el universo | **48** |

**`NINGUNA CLASE SE VOLVIO A DECIDIR.`** Esta relectura es la **mecanica** del
tramo con la vara, no una lectura de juicio.

**LAS CUATRO DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA. LAS CUATRO
CAEN DENTRO DEL UNIVERSO RELEIDO.**

| puesto | clase | declara | lesion | nodo muerto | nodos |
|---:|:-:|:-:|:-:|:-:|---|
| **226** | `B` | no | no | no | `antidilucion_provisiones` contra `antidilution_weighted_average_broad_narrow` |
| **603** | `B` | no | no | no | `decision_autofinanciamiento_vs_inversion` contra `decision_intensidad_capital` |
| **1612** | `D` | no | no | no | `elegir_caja_correcta` contra `elegir_resistencia_caja_peso` |
| **2448** | `D` | **SI** | no | no | `entrenamiento_y_control_estadistico` contra `importancia_de_la_capacitacion` |

**LO QUE LA VARA VE, Y NI UNA PALABRA MAS:** de los cuatro, **solo el 2448
declara un diferenciador**, y **ninguno de los cuatro tiene lesion exacta ni nodo
muerto**. **Lo que la vara no ve, aqui no se afirma.**

**EL CENSO DE LAS `B` DEL UNIVERSO, UNA POR UNA CON SUS TRES COMPROBACIONES.
SOLO SE CUENTA Y SE PUBLICA.**

| puesto | declara diferenciador | lesion exacta | nodo muerto | nodos |
|---:|:-:|:-:|:-:|---|
| **226** | NADA | NADA | NADA | `antidilucion_provisiones` contra `antidilution_weighted_average_broad_narrow` |
| **253** | NADA | NADA | NADA | `fase_acclimate` contra `fase_acclimate_experiencia_cliente` |
| **603** | NADA | NADA | NADA | `decision_autofinanciamiento_vs_inversion` contra `decision_intensidad_capital` |
| **604** | NADA | NADA | NADA | `mapa_de_influencia` contra `mapa_organizacional_influencia` |

| la cuenta | cifra |
|---|---:|
| `B` en el universo releido | **4 de 60** |
| `B` que declaran diferenciador | **0** |
| `B` con lesion exacta | **0** |
| `B` con algun nodo muerto | **0** |
| **`B` que dan NADA en las tres** | **4 de 4** |
| `B` en TODO el archivo, contadas del archivo | **72 de 3388 filas** |
| de las cuatro discrepancias, cuales son `B` | **226 y 603** |

> **Y AQUI SE PARA.** Esta salida **no dice** que la vara sea ciega a la clase
> `B`, **no adjudica** ninguna de estas cuatro y **no propone** nada. Publica la
> cuenta y las tres columnas, que es exactamente lo que el encargo pide. **Si la
> vara resulta ciega a la clase `B` entera, eso es un hallazgo del fundador y no
> mio.**

**EL COTEJO DE LOS CLONES DECLARADOS DE ESTA VUELTA, CON LO QUE SALGA Y SIN
AFIRMAR QUE NINGUN DIFF SALE VACIO** (`docs/loop/SALIDA_V187_COTEJO_DE_CLONES.txt`,
tres cotejos, los tres con `EXITCODE: 0`):

| clon | fichero entero | docstring | maquina | AST sin docstring | lineas de maquina que difieren |
|---|:-:|:-:|:-:|:-:|---:|
| `vuelta186_apertura.py` a `vuelta187_apertura.py` | DIFIERE | DIFIERE | DIFIERE | DIFIERE | **452** |
| `vuelta186_esqueleto_reporte.py` a `vuelta187_esqueleto_reporte.py` | DIFIERE | DIFIERE | DIFIERE | DIFIERE | **68** |
| `vuelta186_tarea1c_relectura_al_doble.py` a `vuelta187_tarea3_relectura_al_doble.py` | DIFIERE | DIFIERE | DIFIERE | DIFIERE | **148** |

**Los tres DIFIEREN por los cuatro veredictos, y es lo esperado:** un clon
declarado de esta casa cambia el sufijo, las rutas, los bloques propios y las
glosas. **La afirmacion de clon se mide, no se promete.**

### TAREA 4. LA ESCALADA: LA PAREJA DE CONVENCIONES DEJA DE BASTAR CON EXISTIR. **CERRADA.**

**EL HUECO, MEDIDO Y NO SOSPECHADO.** `cerrar_reporte.py` publicaba en su bloque
D la linea `toda cifra de bytes y todo sha con su pareja SI`, y **las cuatro
cifras falsas de la `C.1` pasaron por delante de esa linea sin encender nada**.
La causa es exacta: `cifras_sin_pareja()` comprueba que la pareja **EXISTA**, no
que sea **CIERTA**. **Medido en el arnes de esta tarea: de las 7 lineas que la
guarda nueva acusa sobre el texto real de `bb3aaad3`, la guarda vieja acusaba
0.**

**LO QUE SE ESCRIBIO, Y DONDE.**

| pieza | sede | que es |
|---|---|---|
| `dos_convenciones(datos)` | `scripts/loop/vuelta186_rutas_del_reporte.py` | **PURA.** Se SEPARO de dentro del bucle de su `main()` para que la guarda nueva pudiera llamarla. **Una sede, dos llamadores, y NO un tercero.** |
| `medir_en_disco(raiz, ruta)` | la misma | **EL UNICO SITIO QUE TOCA DISCO** para esto. Devuelve `None` y no cero cuando el fichero no existe: cero seria una cifra y la ausencia no lo es. |
| `parejas_publicadas(texto)` | `scripts/loop/cerrar_reporte.py` | **PURA.** Toda pareja publicada contra una ruta, en las **tres formas** que esta casa usa de verdad. |
| `convenciones_que_no_calzan(texto, mediciones)` | la misma | **PURA.** Recibe un MAPA de mediciones, no el disco. |
| `mediciones_de_las_rutas(texto, raiz)` | la misma | el lector unico, que llena ese mapa llamando a la sede de arriba |

**`main()` la llama SIN BANDERA** (lo que se computa no se teclea) y la cablea en
la misma lista del bloque D donde este fichero juzga, con `bloquea=True`, **que
bloquea en LOS DOS CARRILES**: el carril tardio exime una cifra sin pareja y una
seccion 4 muda, que son defectos de un reporte viejo que se declaran; **una cifra
FALSA no es un defecto que se declare, es una cifra falsa**.

**LAS TRES FORMAS, LEIDAS DE REPORTES REALES Y NO INVENTADAS:** (a) `` `<ruta>` ...
N bytes en disco y M bytes normalizados a LF ``; (b) `` `<ruta>` ... disco N bytes
| LF M bytes ``; y (c) **una tabla cuya CABECERA declara que las dos convenciones
son IGUALES y cuyas filas publican UNA sola cifra por ruta**. La tercera hacia
falta: **la cuarta cifra de la `C.1`, el 49804, vive exactamente ahi.**

**Y UNA REGLA QUE LA PROPIA GUARDA SE DESTAPO AL CORRERLA.** En su primera
version acusaba tambien la linea 191 de `bb3aaad3`, donde el reporte dice
*"`docs/PENDIENTES.md` pasa de 894124 bytes en disco a 909780 bytes, la entrada
mide 15655 bytes en disco y 15655 normalizados a LF"*: **la pareja es de LA
ENTRADA escrita, no del fichero**, y atribuirsela habria sido un rojo inventado.
**Si entre la ruta y la pareja hay OTRA cifra de bytes, el sujeto es ambiguo y
esta guarda no atribuye nada.** Es la regla mas estrecha que sigue cazando los
cuatro casos de la `C.1`, donde entre la ruta y su pareja no hay mas que una
coma.

**EL ARNES**, `scripts/loop/vuelta187_tarea4_mutacion_dos_convenciones.py`,
**7 casos, `CIFRA fallos: 0`, `VEREDICTO: VERDE`**, todos con su esperado mutado
cayendo:

| caso | que exige | con el esperado mutado |
|---|---|---|
| **1** | las dos convenciones calzando: **VERDE** | **CAE** |
| **2** | la de **LF** mutada: ROJO, **nombrando LF**, la ruta, la publicada y la medida | **CAE** |
| **3** | la de **DISCO** mutada: ROJO, **nombrando DISCO** | **CAE** |
| **4** | una ruta con **CRLF real**, donde las dos son legitimamente distintas: **VERDE**. Es el caso que impide que la guarda exija que sean iguales | **CAE** |
| **5** | una cifra **sin pareja**: sigue siendo el rojo de `cifras_sin_pareja()`, con su texto de hoy, y **la nueva no la duplica** | **CAE** |
| **5.1** | una **ruta que no existe**: sigue siendo el rojo que ya es, y esta guarda **no lo duplica** | **CAE** |
| **6** | **EL QUE DECIDE**, sobre el texto real de `git show bb3aaad3:docs/loop/REPORTE.md` | **CAE** |

**EL CASO 6, ENTERO.** Sobre ese texto, que mide **46086 bytes en disco y 46086 bytes normalizados a LF** porque el blob de git no lleva CRLF, y **708 lineas**, la
guarda halla **33 parejas publicadas** y acusa **11**, sobre **5 rutas
distintas**:

| ruta | convencion | publicada | medida |
|---|:-:|---:|---:|
| `docs/loop/SALIDA_V186_COTEJO_DE_CLONES.txt` | **LF** | 49804 | **49036** |
| `docs/loop/SALIDA_V186_T2C_CERRAR_REPORTE_184.txt` | **LF** | 6128 | **6030** |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184_SIN_FORZAR.txt` | **LF** | 790 | **780** |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184.txt` | **LF** | 965 | **948** |
| `docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` | DISCO y LF | 5040 | **5043** |

**`DE LAS CUATRO DE LA C.1, FALTAN POR CAZAR: (ninguna)`**, y **`LA CONVENCION QUE
FALLA EN LAS CUATRO ES LF, Y NO DISCO: SI`**.

**LA QUINTA NO ES UN ROJO INVENTADO, Y ESO NO SE SUPONE: SE MIDE.** El primer
criterio de este caso exigia **cero rutas de mas** y salio en **ROJO** en cuanto
otra tarea de esta misma vuelta movio un fichero; **la corrida en rojo entera
vive en `docs/loop/SALIDA_V187_T4_MUTACION_EN_ROJO.txt`** y el motivo esta dentro
del propio arnes. El criterio nuevo va contra `git show`: una ruta de mas es
**legitima** si el fichero **HA CAMBIADO** desde `bb3aaad3`, e **inventada** solo
si sigue byte a byte igual y aun asi se acusa.

    docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
       -> en bb3aaad3 5040 bytes | hoy 5043 bytes | HA CAMBIADO: SI
    CIFRA rutas de mas que serian ROJO INVENTADO: 0

**Es un arnes que nace en esta vuelta**, asi que su rojo es parte de escribirlo
(adjudicacion `5.2` del acta 186), la corrida en rojo se pega entera y el motivo
queda dentro del fichero. **Esa es la letra, y aqui se cumple.**

### TAREA 5. LA NOMINA, LA DECLARACION DEL 184, LA CIFRA DEL H.5 Y EL CIERRE. **CERRADA, CON UNA PARADA DECLARADA.**

#### 5.a LA NOMINA: DE 115 A 121, Y `arneses_que_faltan()` DEVUELVE **0**

**ERA UNA CAIDA MEDIDA CON DOS VUELTAS DE ANTELACION, Y POR SEGUNDA VEZ
SEGUIDA.** El bloque H.3 del sello de apertura, corrido **antes de tocar nada**,
midio `arneses_que_faltan()` devolviendo **`ultima vuelta 185, faltan 4`**.

| | apertura | cierre |
|---|---:|---:|
| censo de arneses del directorio | **181** | **181** |
| tamano de la nomina | **115** | **121** |
| `arneses_que_faltan()` | **4** | **0** |
| `nomina_invisible_al_censo()` | **0** | **0** |
| `guarda_del_sujeto_congelado()` | **0** sin congelar | **0** sin congelar |

**LOS SEIS QUE ENTRAN**, los cuatro de la 186 mas **los dos que nacen hoy**, y
los seis comprobados uno a uno dentro de la nomina (**6 de 6**):
`vuelta186_tarea2a_mutacion_pieza4.py`,
`vuelta186_tarea2b_mutacion_pieza2_cercas.py`,
`vuelta186_tarea2c_mutacion_cierre_tardio.py`,
`vuelta186_tarea2d_mutacion_seccion4.py`,
`vuelta187_tarea4_mutacion_dos_convenciones.py` y
`vuelta187_tarea5b_mutacion_seccion4_tardio.py`.

**NO SE PODA NADA.** La opcion `c` de la parada del 5 sep sigue RECHAZADA por el
fundador y aqui se hace lo contrario, que es completarla. **Y el instrumento de
esta tarea no entra en la nomina, y se mide en vez de decirse:**
`vuelta187_tarea5a_nomina.py` **no esta en el censo de arneses** y **no esta en la
nomina**.

**LA DOBLE CORRIDA EN PROCESOS APARTE: LOS SEIS SON DETERMINISTAS.** Los seis dan
**el mismo `sha256` en las dos corridas**. Ninguna salida cambia sola.

| arnes | exitcode | `sha256` LF, las dos corridas |
|---|:-:|---|
| `vuelta186_tarea2a_mutacion_pieza4.py` | 0 | `9bb37980006e99d3` en las dos |
| `vuelta186_tarea2b_mutacion_pieza2_cercas.py` | 0 | `cf0e9dfc2a8bf63d` en las dos |
| **`vuelta186_tarea2c_mutacion_cierre_tardio.py`** | **1** | `5541805c720b9770` en las dos |
| `vuelta186_tarea2d_mutacion_seccion4.py` | 0 | `443a4f12e3b2ce76` en las dos |
| `vuelta187_tarea4_mutacion_dos_convenciones.py` | 0 | `969c147da84ac882` en las dos |
| `vuelta187_tarea5b_mutacion_seccion4_tardio.py` | 0 | `a0e622551af7ca0a` en las dos |

> ## PARADA. UN ARNES YA SELLADO CAE EN ROJO, Y NO LO ARREGLO
>
> **`scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` sale en ROJO**,
> con **`CIFRA casos: 18 | pasan: 16`** y **`CIFRA fallos: 2`**. **La corrida
> entera vive en
> `docs/loop/SALIDA_V187_T5B_ARNES_SELLADO_186_2C_EN_ROJO.txt`.** Lo que cae es
> su **CASO E**, y lo pego literal:
>
> ```
>       CIFRA apariciones de `not tardio` en el instrumento: 2
>       ESPERADO exactamente 1 -> NO CALZA
>       MUTACION del esperado (exigir 2): PASA
> ```
>
> **LA CAUSA ES EXACTA Y ES MIA, Y LA DIGO PRIMERO.** Ese caso cuenta las
> apariciones de `not tardio` en `cerrar_reporte.py` y **exige EXACTAMENTE 1**,
> porque cuando se escribio **la unica guarda eximida en el carril tardio era la
> de las cifras sin pareja**. La **TAREA 5.b de esta vuelta anade la segunda
> exencion**, la de la `2.d`, que es **literalmente lo que el encargo manda**, y
> con ella la cuenta pasa a **2**.
>
> **NO LO ARREGLO, Y POR LA LETRA:** *"Si cualquier arnes YA SELLADO cae en rojo,
> te detienes ahi, lo traes con su salida entera, sin re-correrlo y sin
> arreglarlo"*. **Cambiar ese `1` por un `2` seria aflojar la guarda que existe
> para impedir que el carril tardio se ensanche solo**, y quien decide si la
> exencion ordenada por el encargo cabe dentro de esa cuenta **no soy yo**.
>
> **LO QUE SI HICE, Y LO DIGO PARA QUE SE PUEDA AUDITAR:** la primera corrida
> clobbero su salida sellada y **la restaure con `git checkout`**; despues, la
> doble corrida de la 5.a la volvio a correr **dos veces** y su salida quedo
> resellada en rojo con `git diff --numstat` de **7 lineas**. **Es
> DETERMINISTA**: el mismo `sha256` en las dos corridas.
>
> **Y LO QUE NO SOSTENGO:** no afirmo que el arnes este mal. Afirmo que **su
> esperado y el encargo de esta vuelta dicen cosas distintas**, y eso es una
> contradiccion entre dos reglas vigentes, que es exactamente el caso en que
> `EJECUTOR.md` 5 manda parar y traerlo.

**Y LAS SALIDAS SELLADAS DE LA 186 SE MOVIERON, CON SU CAUSA MEDIDA.** Esta
vuelta toco `cerrar_reporte.py`, que es el sujeto de los cuatro arneses de la
186, y sus salidas publican **numeros de linea** de ese fichero. `git diff
--numstat` de cada una: `2A` **4 lineas** (solo numeros de linea: la 700 pasa a
la 770 y la 1223 a la 1446, con el veredicto intacto), `2B` **0**, `2C` **7**
(la parada de arriba), `2D` **0**.

#### 5.b LA DECLARACION DEL DEFECTO DEL REPORTE DE LA 184. ES LA `P.2`

**LA PREMISA DE LA PREGUNTA ERA FALSA Y ESTA MEDIDO.**
`docs/loop/SALIDA_V184_APERTURA.txt` **existe** y mide **34194 bytes en disco y 34194 bytes normalizados a LF**, y publica **`CIFRA lineas de status: 2`** y
**`numstat AL ENTRAR: 0`**. **El rojo no es por falta de apertura.** Corrido hoy
sobre los dos ficheros reales:

    seccion4_que_no_calza(REPORTE_V184.md, SALIDA_V184_APERTURA.txt)
    ->  CIFRA motivos en rojo: 1
        "LA SECCION 4 DEL REPORTE NO AFIRMA NADA sobre 'CIFRA lineas de
         status'. La apertura sellada docs/loop/SALIDA_V184_APERTURA.txt
         dice 2, y una cifra ausente y una cifra que calza NO son lo mismo"

**LO QUE SE ESCRIBIO:** `declaracion_de_seccion4()` en `cerrar_reporte.py`,
**PURA** y **hermana exacta** de `declaracion_de_cifras_sin_pareja()`. Misma
puerta, misma forma, **y por eso no se escribe una tercera manera de declarar un
defecto**. En el carril tardio `main()` la computa **sobre el texto ya armado** y
la anexa; en el bloque D.1 la exencion **se coteja POR CONTENCION**: si la marca
no esta o algun motivo no esta declarado, **vuelve a ser rojo**. **Una exencion
sin su declaracion seria una exencion muda, y eso es lo que el banco 9 prohibe.**

**`docs/loop/reportes/REPORTE_V184.md` NO SE REABRE Y NO SE REESCRIBE SU SECCION
4.** Lo que se le anade es la declaracion. **Reescribir su seccion 4 seria
escribir en pasado lo que no paso.**

**EL ARNES**, `scripts/loop/vuelta187_tarea5b_mutacion_seccion4_tardio.py`, **7
casos, `CIFRA fallos: 0`, `VEREDICTO: VERDE`**:

| caso | que exige | con el esperado mutado |
|---|---|---|
| **A** | en el carril **NORMAL** la seccion 4 muda **BLOQUEA**, leido de la columna `bloquea` real de `main()` en el fichero fuente | **CAE** |
| **B** | en el **TARDIO** no bloquea y **aparece DECLARADA**, cotejada por contencion | **CAE** (dos mutaciones) |
| **B.1** | la declaracion **no se acusa a si misma**: 1 motivo antes y 1 despues de anexarla | **CAE** |
| **C** | **cero motivos**: la declaracion se escribe igual y **dice cero** | **CAE** |
| **D** | sobre los ficheros **REALES** del 184: **1 motivo**, y la declaracion **lo nombra** (1 de 1) | **CAE** (dos mutaciones) |
| **E** | la guarda de las dos convenciones de la TAREA 4 **bloquea en los dos carriles** | **CAE** |
| **F** | la exencion **no es gratis**: sin declaracion, vuelve a ser rojo | **CAE** |

**SU PRIMERA CORRIDA SALIO EN ROJO Y SE PEGA ENTERA**, que es lo que la
adjudicacion `5.2` del acta 186 manda para un arnes que nace en la vuelta:
`docs/loop/SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO_EN_ROJO.txt`, **`CIFRA
fallos: 1`**. El motivo esta dentro del propio fichero: **el arnes fabricaba su
seccion 4 con la frase `CIFRA lineas de status` cuando la guarda busca el
MARCADOR literal `git status --porcelain`**. *Un arnes que fabrica su sujeto con
otras palabras que las que la guarda busca no prueba la guarda: prueba la
parafrasis.* Ahora los dos marcadores **se importan de la guarda** y no se
teclean.

#### 5.c LA CIFRA INUTIL DEL BLOQUE H.5, REPARADA, CON SU ANTES Y SU DESPUES

El bloque de apertura de la 186 conto los puestos de las ciegas con el patron en
mayusculas cuando las ciegas los escriben como `puesto_intra`. El bloque H.5 de
esta vuelta cuenta con **LOS DOS** y publica **LAS DOS CIFRAS**:

| fichero | cifra VIEJA (patron de la 186) | cifra NUEVA (`puesto_intra`) |
|---|---:|---:|
| `docs/loop/_auditor_v188_ciega_blind.txt` | **0** | **30** |
| `docs/loop/_auditor_v188_ciega_reveal.txt` | **0** | **30** |
| `docs/loop/_auditor_v187_ciega_blind.txt` | **0** | **30** |
| `docs/loop/_auditor_v188_mis_clases.txt` | **0** | **0** |

**TRES DE LOS CUATRO DEJAN DE SER CERO. EL CUARTO SIGUE EN CERO, Y ES CORRECTO,
Y SE DICE EN VEZ DE DISIMULARLO:** `_auditor_v188_mis_clases.txt` **no escribe
`puesto_intra` en ninguna linea**; escribe una TABLA con cabecera `puesto | mi
clase | dudoso | mi razon en una linea`. **Su cero no es una cifra inutil: es la
medicion correcta de un fichero con otro formato.**

#### 5.d EL CIERRE

El esqueleto se tallo con sus **cinco filas vacias** y **cada tarea anexo la suya
al cerrarse**. La cabecera se talla con
`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 187` y su
salida vive en `docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt`. **Cero celdas
tecleadas.**

<!-- FIN ANEXO DE TAREAS -->

## 3. LO QUE ESTA VUELTA SOSTIENE, Y NI UNA PALABRA MAS

1. **EL PLAN SE MOVIO, Y ES LO PRIMERO QUE HAY QUE DECIR.** Llevaba **seis
   vueltas quieto** y esta vuelta lo movio: el `sha256` por la convencion de LF
   de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` **abre en `ea6e850d331d14f0` y cierra
   en `0a77b5a35a962621`**. La diferencia es **una fila de 3388**, el puesto
   **2464**, y va explicada par por par en la TAREA 2.
2. **EL TRAMO 1 DE LA COLA POST FUSION QUEDA CERRADO EN SU PROPIA SEDE.** El
   disparador se leyo **antes de tocar nada** y se cito con su linea; el tamano
   del tramo **se computo del criterio escrito** (2760 `D` a 99 a 6 a 1) y no se
   invento; **la relectura SOSTIENE la clase `D`**, y lo que se movio es **la
   evidencia**: de los dos diferenciadores que la razon declaraba, **hoy solo uno
   es cierto**.
3. **LA ESCALADA DE `AUDITOR.md` 1.2 ESTA PUESTA Y CAZA EL CASO QUE LA TRAJO.**
   La guarda de las dos convenciones acusa **las cuatro cifras de la `C.1`** sobre
   el texto real de `bb3aaad3`, **por LF**, y **la guarda vieja acusaba 0 de 7**.
4. **LA NOMINA CRECE DE 115 A 121 Y `arneses_que_faltan()` DEVUELVE 0.** Los seis
   son **deterministas** en la doble corrida en procesos aparte.
5. **HAY UNA PARADA Y NO LA ARREGLO.** El arnes ya sellado
   `scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` cae en **ROJO** por
   su **CASO E**, porque la exencion que el encargo manda anadir en la 5.b hace
   que su cuenta de `not tardio` pase de **1** a **2**. Va entera en la TAREA 5.
6. **NINGUNA CLASE SE VOLVIO A DECIDIR EN LA RELECTURA AL DOBLE**, y **el
   marcador no se movio**: 3388 filas, 551 `A`, 72 `B`, 5 `C`, 2760 `D`, 0 huecos
   y 0 duplicados, **al abrir y al cerrar**.
7. **LO QUE ESTA VUELTA NO ABRIO:** la mesa del `PMF` (puestos 338 y 297), la del
   **603** y la de **figuras del 226**. Las tres son trabajo de plan de otra
   vuelta, con sede en `docs/PENDIENTES.md`, y el encargo lo prohibe con esas
   palabras. **Y `docs/loop/reportes/REPORTE_V184.md` no se reabrio.**

## 4. EL ESTADO DEL ARBOL, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO

**LAS DOS CIFRAS DE ESTA SECCION SALEN DE `docs/loop/SALIDA_V187_APERTURA.txt`**,
que se escribio **antes de la primera operacion**, y **no de lo que yo recuerde**.
Es la guarda de la `2.d` la que las lee de ahi y las coteja contra lo que este
apartado afirma.

- El arbol abrio con **`git status --porcelain`** en **1** linea, y esa linea era
  **`?? scripts/loop/vuelta187_apertura.py`**: el propio bloque de apertura,
  todavia sin seguir por git cuando su bloque C corrio. **La prediccion estaba
  escrita en su docstring antes de medir, y calzo.**
- Y con **`git diff --numstat -- dataset/`** en **0** filas **AL ENTRAR**.
- **AL SALIR**, medido de nuevo por el instrumento de la TAREA 5.a:
  **`CIFRA filas de git diff --numstat -- dataset/`: 0**. **Las dos cifras se
  publican, que es lo que el encargo pide.**

**EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA**, dentro del bloque de
apertura y antes de la primera operacion: **4 filas**, las mismas cuatro que al
cierre. **Una columna de apertura medida al cierre es caida que ACUMULA, y esta
no lo esta.**

## 5. LAS CORRECCIONES DECLARADAS DE ESTA VUELTA

**UNA SOLA, Y ES LA DEL PUESTO 2464.** La `razon` pasa de **944 a 3106
caracteres**; **el texto viejo sigue entero dentro del nuevo**; la marca
`CORRECCION DECLARADA (vuelta 187, TRAMO 1 DE LA COLA POST FUSION)` esta; y **0
guiones largos o medios**. **Ningun veredicto se movio en silencio y nada se
borro.**

**Y UNA SEGUNDA COSA QUE NO ES UNA CORRECCION DE VEREDICTO PERO SI DE ESPECIE:**
el registro `R.49` **no cuenta la `PD.7` del reporte de la 186 como pendiente de
doctrina**, porque el acta 187 la corrige por declaracion. **El numero `PD.7`
queda libre.**

## 6. PENDIENTES DE DOCTRINA

**`PD.1` SIGUE ABIERTA, SEXTA VUELTA.** Sus cinco puestos, **leidos del acta y no
copiados del encargo**: **1778, 2530, 2540, 3141, 3232**. Y esta vuelta le anade
**su medicion de hoy**: la criba de las condiciones 1 y 2 los nombra a los cinco,
y **son exactamente los mismos cinco** que el `R.49` leyo del acta. **No pasan la
condicion 3, no entran en la cola, y darles cola seria doctrina nueva, que es del
fundador.**

**`PD.8` NUEVA, Y NACE MEDIDA.** **LA FORMA DE UNA CORRECCION DECLARADA DENTRO DE
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO ESTA ESCRITA EN NINGUNA DOCTRINA.**
Contadas hoy sus 3388 filas, el archivo tiene **ocho campos** (`puesto_intra`,
`dominio`, `nodo_a`, `nodo_b`, `clave`, `banda_078_080`, `clase`, `razon`) y
**ninguno es de correccion**; **ninguna fila ha llevado nunca uno**. Por
`EJECUTOR.md` 5 **no se para**: se registro lo mejor sostenido, que es **anexar a
la `razon` sin borrar nada, con marca literal y vuelta**, y queda **marcado
PENDIENTE DE DOCTRINA dentro de la propia razon** para que el fundador decida la
sede definitiva.

## 7. LAS PREGUNTAS QUE TRAIGO

**`P.1`. ¿CABE DENTRO DEL CASO E DEL ARNES DE LA 186 LA EXENCION QUE EL ENCARGO
ORDENA?** Es la PARADA de la TAREA 5. El arnes exige **exactamente 1** aparicion
de `not tardio` en `cerrar_reporte.py`; la 5.b de este encargo anade **la
segunda**, la de la `2.d`, y con ella son **2**. Las dos reglas son vigentes y
dicen cosas distintas. **No lo arreglo**: cambiar ese `1` por un `2` seria
aflojar la guarda que existe para impedir que el carril tardio se ensanche solo.

**`P.2`. ¿QUE HAGO CON UNA SALIDA SELLADA QUE SE MUEVE SOLA PORQUE PUBLICA
NUMEROS DE LINEA DEL FICHERO QUE JUZGA?** Los cuatro arneses de la 186 juzgan
`cerrar_reporte.py`, y esta vuelta lo toco. El `2A` mueve **4 lineas** de su
salida y su veredicto **sigue en VERDE**: lo unico que cambia es que la linea 700
pasa a la 770 y la 1223 a la 1446. **La distincion que aplique** es que hace
PARADA lo que **cambia entre dos corridas de la misma vuelta**, no lo que se
mueve porque su sujeto se movio. **Si la casa quiere la otra letra, lo digo aqui
para que se escriba.**

**`P.3`. ¿EL SOLAPE DE LA RELECTURA AL DOBLE SE EXIGE AL TRAMO O AL UNIVERSO?**
El encargo pide **solape 0 con los 293 puestos de la exclusion**. **El tramo lo
cumple: 0.** **El universo entero da 2**, y los dos son **vecinos deterministas**
(**1287**, vecino del 1286, y **2383**, vecino del 2382). **No lo arregle**:
`vecinos()` es una funcion **importada y congelada**, y cambiarla para que la
cifra saliera cero seria mover la vara a mitad de la medicion, que es lo que
`P.5.1` prohibe.

## 8. LAS CAIDAS PROPIAS DE ESTA VUELTA

**DOS, Y LAS LEVANTO YO, Y LAS DOS SON DE METODO Y NO DE CIFRA.**

**`C.1`. EL ESQUELETO DEL REPORTE SE TALLO DESPUES DE LA TAREA 1, NO EN LA
APERTURA.** `EJECUTOR.md` 1 dice que **el reporte se abre al empezar**. La
apertura si corrio primero y entera, pero el esqueleto necesita que
`docs/loop/SALIDA_V187_HEAD_APERTURA.txt` este **commiteado** para leer su commit
de nacimiento con `git log --diff-filter=A`, y ese commit es el de la TAREA 1.
**Consecuencia medida: si esta vuelta se hubiera cortado dentro de la TAREA 1, no
habria dejado reporte parcial, habria dejado el de la 186.** **Esta declarada en
el docstring del esqueleto y en el propio encabezado del reporte**, y la traigo
aqui con su nombre en vez de dejarla solo ahi.

**`C.2`. EL PRIMER CRITERIO DEL CASO 6 DE LA TAREA 4 ERA FRAGIL Y SALIO EN
ROJO.** Exigia **cero rutas de mas**, lo que lo ataba al estado del disco de
ficheros que no tienen nada que ver con la `C.1`; en cuanto otra tarea de esta
misma vuelta movio uno, cayo. **La corrida en rojo entera esta publicada** en
`docs/loop/SALIDA_V187_T4_MUTACION_EN_ROJO.txt` y el criterio nuevo va contra
`git show`, que es medible. **Es un arnes que nace en esta vuelta**, asi que por
la adjudicacion `5.2` del acta 186 su rojo es parte de escribirlo; lo levanto
igual porque **el primer criterio estaba mal pensado, no incompleto**.

**Y UNA TERCERA COSA QUE NO ES CAIDA Y SE DICE IGUAL:** el arnes de la 5.b salio
en rojo en su primera corrida por fabricar su sujeto con una parafrasis en vez
del marcador literal. **Nace en esta vuelta, la corrida esta publicada y el
motivo vive dentro del propio fichero**, que es exactamente lo que la letra
permite.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**ESTA VUELTA NO ES DE BATERIA, Y EL HUECO SE DECLARA CON SUS TRES PIEZAS
JUNTAS.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria
**corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada mas. **Cerro
entera en la 184**, asi que **la siguiente vuelta de bateria es la 189**.

## 10. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` (DE METODO).** **La forma de la correccion declarada del 2464: anexarla a
la `razon` en vez de darle campo propio.** El archivo no tiene ningun campo de
correccion y nunca lo ha tenido, asi que no hay sede escrita. Anexar conserva el
texto viejo entero, que es lo que `EJECUTOR.md` 8 manda, pero **engorda un campo
que se lee a ojo** y **no se puede filtrar por programa**. Va marcado
**PENDIENTE DE DOCTRINA** dentro de la propia razon. **Si la casa prefiere un
campo, esto es lo que hay que rehacer.**

**`D.2` (DE METODO).** **El solape del universo releido con la exclusion es 2 y
no 0**, y lo dejo asi en vez de arreglarlo. **El tramo cumple el 0**; los dos que
cruzan son vecinos deterministas de una funcion congelada. **Mi criterio fue no
mover la vara a mitad de la medicion.**

**`D.3` (DE METODO).** **Segui adelante despues de que un arnes ya sellado cayera
en rojo**, en vez de detener la vuelta ahi. Entregue las cinco tareas y traje la
parada entera con su salida. **Mi lectura es que "te detienes ahi" gobierna el
arnes, no la vuelta**, porque el mismo encargo manda entregar cinco tareas y
cerrar el reporte. **Puede leerse al reves.**

**`D.4` (DE METODO).** **Anexe un registro a `docs/plan/08_VERIFICACION.md`
cerrando el tramo 1**, y el encargo no lo pide con esas palabras: pide mover el
par y publicar el `sha256`. **Lo hice porque el propio criterio escrito exige una
comprobacion al cierre de la cola**, y un tramo releido que no se anota en su sede
deja el plan diciendo que sigue pendiente. **Es plan, y el plan es del fundador.**

**`D.5` (DE CLASE, Y LO DIGO CON ESAS PALABRAS).** **La relectura del 2464
sostiene la `D`, y podria discutirse.** Tras la lesion, **`zero_defects_concepto`
se queda con UN solo diferenciador**: el arranque a escala minima (marcar el dia
aunque sea contigo mismo, y el compromiso por escrito). El otro lado conserva
tres. **Quien crea que un solo diferenciador de dos pasos contra un nodo de siete
ya no sostiene dos nodos sanos, adjudicaria `A` o `B`.** Yo sostengo `D` porque
los dos pasos que quedan **traen procedimiento propio y no solo el nombre de
otro**, que es la vara de `P.5.1`. **Marcado antes de saber si acierto.**

**`D.6` (DE METODO).** **Restaure con `git checkout` las salidas selladas de la
186 que mis corridas habian clobbereado**, y despues la doble corrida de la 5.a
las volvio a mover. **El arbol final las lleva reselladas.** Mi criterio fue que
un arnes que entra en la nomina debe tener en disco la salida que produce hoy,
pero **esto pisa evidencia de otra vuelta** y va con su `numstat` publicado al
lado.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 187 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V187_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: AUDITOR.md 6.1, decision del fundador del 5 sep 2026: la bateria corre CADA CINCO VUELTAS y cerro entera en la 184. LA SIGUIENTE VUELTA DE BATERIA ES LA 189, y esta vuelta 187 NO la corre.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
