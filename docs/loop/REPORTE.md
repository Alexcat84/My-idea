# REPORTE DE LA VUELTA 174 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta174_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
> **EL TOPE DE ESTA VUELTA NO ES CINCO SINO DOS** (`AUDITOR.md` 6.2, regimen
> temporal del 5 sep 2026, vigente hasta que DOS vueltas seguidas cierren su
> propio reporte), y el encargo trae exactamente dos.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** La vuelta 173 **no escribio ningun reporte**, asi que lo
> que hay en el arbol es el de la **172**. El numero se LEE de la cabecera del
> fichero que se va a destruir, no se teclea, y la guarda corre igualmente sobre
> la 173 en modo solo comprobacion para publicar lo que salga. **Ninguna de
> sus cuatro clausulas se afloja: se le da el sujeto correcto.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta174_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 173: `ee3be26a`, asunto real leido de git log:
  '@ ACTA DEL AUDITOR, VUELTA 173, Y PARADA: DOS TAREAS SIN UNA SOLA CIFRA FALSA, PERO LA VUELTA NO ESCRIBIO REPORTE NI SIQUIERA EL ESQUELETO Y LA DEUDA YA ES DE DOS. EL REMEDIO DE ORDEN SE APLICO ENTERO Y LA VUELTA MURIO ANTES QUE LAS TRES ANTERIORES: LOS TRES REMEDIOS DEL AUDITOR ESTAN AGOTADOS Y LO QUE QUEDA ES ALCANCE, QUE ES DEL FUNDADOR. PROMPT_SIGUIENTE.md VACIO EN CERO BYTES @'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V174_HEAD_APERTURA.txt`: `9445cd21`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `f7284a6b`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **172**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 174`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Son todas del lado CIERRE, que al abrir todavia no existe.
Este hueco se rellena con la tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | EL REPORTE, Y ES LA QUE ROMPE LA RACHA DE CUATRO. Dos mitades y ninguna es opcional: 1.a CERRAR Y ARCHIVAR EL REPORTE DE LA VUELTA 172 con `scripts/loop/cerrar_reporte.py`, que es la deuda mas vieja porque el de la 172 no lo archivo nadie; 1.b ABRIR EL REPORTE DE LA 174 Y CERRARLO en la misma vuelta, que es exactamente lo que lleva cuatro vueltas sin pasar. Y con ellas, el unico arreglo de texto pendiente: la clausula de la `4.4` por el carril del `9.10` | **CERRADA EN SU 1.a; LA 1.b CON EL ESQUELETO TALLADO Y EL CIERRE PENDIENTE, QUE ES EL ULTIMO ACTO** | `SALIDA_V174_T1A_CORREGIR_44.txt`, `_T1A_MUTACION_44` (26/26), `_T1A_CERRAR_REPORTE_172` (4 piezas, 0 faltan), `_T1A_COMPARAR_CABECERA_172` (9 filas, 0 distintas), `_T1A_ARCHIVAR_172`, `_T1B_ESQUELETO`, `_T1B_MUTACION_ESQUELETO` (19/19) |
| **TAREA 2** | LAS DOS SUB-TAREAS QUE QUEDARON SIN EJECUTAR DE LA 172: 2.a EL ACTA 172 AL `R.42`, que es el siguiente libre RECOMPUTADO hoy y no tecleado; 2.b QUE NAZCA `scripts/loop/vuelta172_tarea1b_confirmar_r41.py`, que el recuadro del `R.41` PROMETE y que lleva dos vueltas sin existir, con lo que el `R.41` esta publicando una ruta que promete prueba sobre un vacio | **CERRADA** | `SALIDA_V174_T2A_REGISTRO_ACTA_172.txt` (R.42, 11 adjudicaciones y 2 caidas, serie 34 sin colisiones ni huecos), `_T2B_CONFIRMAR_R41` (adicion pura de 2686 bytes, 9 comprobaciones y 0 fallan), `_T2B_MUTACION_CONFIRMAR` (34/34) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. EL REPORTE. LA DEUDA DE LA 172 PAGADA Y EL DE LA 174 ABIERTO

**1.a EL REPORTE DE LA VUELTA 172 QUEDA CERRADO Y ARCHIVADO.** Y antes de
cerrarlo, la clausula de la `4.4`, porque archivar primero seria sellar la
afirmacion falsa en `docs/loop/reportes/REPORTE_V172.md` y corregir despues una
copia. **La eleccion del orden es mia y va escrita para que se pueda discutir**
(discutible `D.1`).

**LA CORRECCION DEL `4.4`, POR EL CARRIL DEL `9.10`.** Instrumento
`scripts/loop/vuelta174_tarea1a_corregir_44.py`, salida
`docs/loop/SALIDA_V174_T1A_CORREGIR_44.txt`. **Las dos rutas que la fila de la
TAREA 5 nombraba, MEDIDAS HOY en el disco con `os.path.getsize` y no creidas al
acta:**

| ruta que la fila publicaba como prueba | medido hoy |
|---|---|
| `docs/loop/SALIDA_V172_T5_MUTACION_CIERRE.txt` | 4921 bytes |
| `docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt` | **NO EXISTE** |

**CIFRA rutas de esa fila que apuntan a un vacio: 1.** El instrumento CAE EN
ROJO y no escribe nada si esa cifra no es exactamente 1: no corrige por lo que
dijo un acta, corrige por lo que mide el disco. El `CERRADA` viejo y la prueba
falsa quedan **enteros y tachados**, con el estado corregido al lado y la
correccion fechada debajo de la tabla. **13 comprobaciones de relectura, 0
fallan.** Su caso positivo por mutacion,
`scripts/loop/vuelta174_tarea1a_mutacion_44.py`, sobre **SUJETO CONGELADO**
(cero lecturas de disco y cero escrituras): **26 de 26**, once casos rojos que
caen cada uno por SU motivo nombrado y devolviendo el texto INTACTO, mas el caso
verde de catorce comprobaciones, mas la mutacion del propio arnes (se le pide un
motivo inventado y se comprueba que NO aparece).

**EL CIERRE.** `scripts/loop/cerrar_reporte.py --vuelta 172`, salida
`docs/loop/SALIDA_V174_T1A_CERRAR_REPORTE_172.txt`. **Las cuatro piezas, y
ninguna falta: `CIFRA piezas que faltan: 0`.** El reporte pasa de 33.434 a
**48.851 bytes** y de 536 a **761 saltos de linea**.

**LA SECCION 9 VA CON HUECO DECLARADO Y MEDIDO**, que es el carril que la TAREA
1.b de la vuelta 173 construyo. **Las dos cifras del hueco las midio el bloque
de apertura de esta vuelta, `H.3`, con `os.path.getsize`:**

| fichero de la bateria de la 172 | bytes medidos hoy |
|---|---:|
| `docs/loop/SALIDA_V172_BATERIA.txt` (ejecutor) | **0** |
| `docs/loop/SALIDA_V172_AUDITOR_BATERIA.txt` (auditor) | **0** |

**ATRIBUCION: NADIE la corrio**, y el auditor lo declara el mismo en su clausula
`4.3` (`docs/loop/ACTA_AUDITOR.md:58638`, leida hoy).

**LA CABECERA NO SE TECLEA Y ADEMAS SE COTEJA.**
`tallar_cabecera_reporte.py --vuelta 172 --fase04 --comparar docs/loop/REPORTE.md`
(`docs/loop/SALIDA_V174_T1A_COMPARAR_CABECERA_172.txt`) dice **`filas cotejadas:
9 | DISTINTAS: 0 | ausentes: 0`** y **`CABECERA: IDENTICA AL TALLADOR`**.
**ATRIBUCION DE LA CABECERA, y no es mia:** el fichero
`docs/loop/SALIDA_V172_TALLADOR_CABECERA.txt` nacio en el commit `0c287793`, que
es **el acta del auditor de la vuelta 172**, y es byte a byte identico a
`docs/loop/SALIDA_V172_AUD2_TALLADOR.txt`. La celda que se pego en el reporte de
la 172 la tallo **el auditor**, no el ejecutor (discutible `D.2`).

**EL ARCHIVADO.** `scripts/loop/archivar_reporte.py --vuelta 172`
(`docs/loop/SALIDA_V174_T1A_ARCHIVAR_172.txt`), leido de git y no del arbol:
`docs/loop/reportes/REPORTE_V172.md`, **48.851 bytes, 761 lineas, sha256
`d29e45527ea302a0`**, commit de origen `23d5743c`. **La cadena de archivados ya
no tiene hueco: 168, 169, 170, 171 y 172.**

**1.b EL REPORTE DE LA 174 SE ABRE Y SE CIERRA EN LA MISMA VUELTA.** Esqueleto
por `scripts/loop/vuelta174_esqueleto_reporte.py`
(`docs/loop/SALIDA_V174_T1B_ESQUELETO.txt`): **4.547 bytes, 65 lineas, 2 filas
de tarea abiertas.**

**Y TRAE EL UNICO CAMBIO DE MAQUINA DE LA VUELTA, QUE ES UN ENDURECIMIENTO.** El
paso 0 de todos los clones anteriores preguntaba por `VUELTA - 1`. **La vuelta
173 no escribio ningun reporte**, asi que ese sujeto ya no sirve. Corrido tal
cual, y publicado salga lo que salga, el paso 0 sobre la **173** da **ROJO por su
clausula (b)**: *"no existe el archivo `docs/loop/reportes/REPORTE_V173.md`"*.
**Eso es cierto y no es la pregunta.** La pregunta del paso 0 es *"lo que voy a
destruir, esta guardado?"*, y aqui el numero **se lee de la cabecera del fichero
que se va a pisar** con la funcion pura `vuelta_del_reporte_del_arbol()`, no se
teclea. Sobre la **172**, que es el reporte que de verdad estaba en el arbol, el
paso 0 da **VERDE con los dos sha256 calzando** (`d29e45527ea302a0`). **Ninguna
de sus cuatro clausulas se afloja: se le da el sujeto correcto.**

**Y NO SE PUBLICA SIN SU MUTACION.**
`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`
(`docs/loop/SALIDA_V174_T1B_MUTACION_ESQUELETO.txt`): **19 de 19**, con los
ficheros de mentira en un temporal que se borra al terminar y **el repo sin
tocar**. Ocho casos sobre la funcion pura (devuelve el numero cuando lo hay y
`None` cuando no, sin adivinar ninguno), ocho sobre las clausulas `(b)`, `(c)` y
`(d)` de la guarda (incluida la caida por **un solo byte** de diferencia y la
vuelta al verde al restaurar, que es lo que prueba que no es un rojo
permanente), y **el caso que prueba el cambio de esta vuelta: el sujeto TECLEADO
da ROJO y el LEIDO da VERDE**.

**LA IDENTIDAD, LEIDA DE GIT Y NO TECLEADA:** el commit del acta 173 se localizo
por **busqueda NO ANCLADA** (su asunto lleva arrobas sueltas delante, como paso
con el de la 170), con **exactamente 1 acierto**: `ee3be26a`. El HEAD de
apertura, `9445cd21`, salio del sello
`docs/loop/SALIDA_V174_HEAD_APERTURA.txt`, y el nacimiento de ese sello,
`f7284a6b`, de `git log --diff-filter=A`.

**EL CIERRE DE ESTA MISMA 1.b ES EL ULTIMO ACTO DE LA VUELTA Y TODAVIA NO HA
CORRIDO AL ESCRIBIR ESTA LINEA.** Se dice asi a proposito: la caida `4.4` que
esta misma tarea acaba de corregir fue exactamente una fila que dijo `CERRADA`
nombrando una prueba que aun no existia. **Aqui no se nombra ninguna ruta del
cierre**, porque por la regla del 5 sep 2026 una ruta a un fichero inexistente
ya es caida de cifra. Cuando el cierre corra, **la celda de estado de esta fila
la sella `scripts/loop/vuelta174_sellar_fila_cerrada.py`, que MIDE el fichero
antes de nombrarlo y se niega a sellar si no existe o mide cero bytes.**

### TAREA 2. LAS DOS SUB-TAREAS QUE LA VUELTA 173 NO EJECUTO

**2.a EL ACTA 172 ENTERA QUEDA EN EL `R.42`.** Instrumento
`scripts/loop/vuelta174_tarea2a_registrar_acta172.py`, salida
`docs/loop/SALIDA_V174_T2A_REGISTRO_ACTA_172.txt`. **Ninguna cifra tecleada:**

| que se computa | de donde sale | valor |
|---|---|---|
| numero de la entrada | `serie_de_registros.py`, siguiente libre de las DOS sedes | **R.42** |
| adjudicaciones | barrido `6.n` del cuerpo acotado, parando en el primer hueco | **11** |
| caidas propias del auditor | negritas `CAIDA n` del cuerpo acotado | **2** |
| cuerpo del acta 172 | acotado por su cabecera y la siguiente | `ACTA_AUDITOR.md` **58375 a 58940** |
| serie despues de escribir | recomputada | **34 entradas, 0 colisiones, 0 huecos** |
| sede | frase de la `6.3` del acta 162, hallada **1** vez en el fichero entero | `docs/PENDIENTES.md` |

**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** EJECUTADA **2** (`6.2`, `6.4`);
NO SE CORRIO **2** (`6.3`, `6.11`); SIN TOCAR NADA **7** (`6.1`, `6.5`, `6.6`,
`6.7`, `6.8`, `6.9`, `6.10`).

**LA MAQUINA NO SE CLONA, SE IMPORTA, Y ES LO UNICO NUEVO DEL INSTRUMENTO.** Los
dos registradores anteriores copiaban el mecanismo entero cada vuelta, o sea tres
sitios donde arreglar el mismo fallo. Aqui `PAT_CAIDA`, `PALABRA`,
`titulo_de_la_negrita`, `claves_de_adjudicacion` y `_cuenta_caidas` **se importan
de `vuelta172_tarea1_registrar_acta171.py`**, que es su ultima sede y la que la
bateria ya vigila con `vuelta172_tarea1b_mutacion_registro.py`. Lo unico propio
del fichero nuevo es **el acote de su acta y sus tablas de glosas**. Es la `6.6`
de la propia acta 172 aplicada a si misma (discutible `D.3`).

**Y LA DIFERENCIA DE FONDO CON EL `R.41`, QUE CIERRA EL CIRCULO DE LA `6.4`.** El
`R.41` se escribio **la primera** de su vuelta y por eso su campo era **VIA
PREVISTA** y sus glosas hablaban en futuro. **El `R.42` se escribe la penultima**,
con la TAREA 1 entera ya cerrada y medida, asi que su campo es **VIA** a secas,
sus glosas **si afirman en pasado** y **cada una lleva al lado la linea o la
salida que la mide**. Por eso el `R.42` **no necesita ningun fichero de
confirmacion posterior**: no hay nada que confirmar despues porque nada se afirmo
antes de tiempo.

**UNA ETIQUETA QUE NO ALCANZA, DECLARADA EN VEZ DE INVENTADA.** La `6.3` del acta
172 (mover la bateria al principio de la vuelta) **quedo sin objeto por una
decision posterior del fundador**, la del 5 sep 2026 que la saca del ciclo por
vuelta. Las tres etiquetas de VIA escritas son `EJECUTADA`, `SIN TOCAR NADA` y
`NO SE CORRIO`, y **ninguna dice "superada por decision del fundador"**. Se usa
la mas cercana y **el hueco sube como PENDIENTE DE DOCTRINA** (`EJECUTOR.md` 5),
en vez de estrenar una etiqueta por mano del ejecutor.

**2.b NACE `scripts/loop/vuelta172_tarea1b_confirmar_r41.py`, QUE LLEVABA DOS
VUELTAS PROMETIDO Y SIN EXISTIR.** Salida
`docs/loop/SALIDA_V174_T2B_CONFIRMAR_R41.txt`.

**EL NOMBRE LLEVA `vuelta172` Y NO `vuelta174`, Y ES DELIBERADO:** es el nombre
exacto que el recuadro del `R.41` publica (`docs/PENDIENTES.md:12455`, leido hoy).
**Renombrarlo dejaria la promesa apuntando igual a un vacio**, que es justo la
caida `4.5` que esta sub-tarea paga.

**QUE MIDE, Y LAS DOS COLUMNAS SE MIDEN SIN TECLEARSE:** la tarea que cada glosa
nombra se extrae del texto del propio `R.41` con expresion regular; el estado de
esa tarea se lee de la tabla de `docs/loop/reportes/REPORTE_V172.md`, **48.851
bytes medidos con `os.path.getsize` en la corrida**. **12 glosas leidas, 7 con
tarea nombrada y estado hallado, 5 que se acatan sin tarea.** La anexion es
**adicion pura de 2.686 bytes**, con **9 comprobaciones de relectura y 0 fallan**,
incluidas *"el texto de ARRIBA del `R.41` no se toco"* y *"el `R.42` de al lado
no se toco"*.

**Y EL INSTRUMENTO NO PODIA CORRER ANTES DE HOY, DICHO COMO CAUSA Y NO COMO
EXCUSA:** su fuente de estados es el reporte de la 172 **cerrado y archivado**, y
ese fichero no existio hasta la TAREA 1.a de esta misma vuelta. **Eso explica las
dos vueltas de promesa vacia, no las excusa.** Y el instrumento aplica la regla a
si mismo: **cae en rojo y no escribe nada si su fuente no existe o mide cero
bytes.**

**UN CONTRASTE DECLARADO Y NO RESUELTO COPIANDO** (`EJECUTOR.md` 2): las filas de
la `6.4` y la `6.5` leen **`ABIERTA, SIN CERRAR`**, que es lo que la fila entera
de la TAREA 4 publica. La clausula `4.6` del acta del auditor de la 172 midio
aparte que **la 4.a y la 4.b si estan hechas y verificadas** y que solo falta la
`4.c`. **Las dos cosas son ciertas y la discrepancia queda escrita en el bloque
anexado**, sin elegir una.

**LA GUARDA QUE MORDIO, Y NO SE AFLOJO SINO QUE SE REAPUNTO.** La primera corrida
salio **ROJA** por *"se colaron guiones largos o medios"*: `docs/PENDIENTES.md` es
un fichero historico que **ya traia** guiones largos de 2026, cosa que la TAREA
2.b de la vuelta 172 ya habia medido y dejado escrita. La guarda pasa a mirar **el
DELTA y no el total**, que es el remedio que la casa ya uso, y **el caso positivo
prueba las dos mitades**: que PASA sobre una sede que ya traia uno de antes y que
**CAE igualmente si el bloque anade uno nuevo sobre esa misma sede**.

**EL CASO POSITIVO POR MUTACION:**
`scripts/loop/vuelta174_tarea2b_mutacion_confirmar.py`
(`docs/loop/SALIDA_V174_T2B_MUTACION_CONFIRMAR.txt`), **34 de 34**, sobre SUJETO
CONGELADO y con cero lecturas de disco y cero escrituras. Tumba las cinco
funciones puras una a una: el acote cae si la cabecera falta o esta duplicada y
**para en la cabecera del `R.42` sin comersela**; las glosas devuelven **otra**
tarea si el texto dice otra (no hay constante escondida); los estados se leen sin
suavizar el `ABIERTA, SIN CERRAR`; y los cinco rojos de la anexion devuelven el
texto **INTACTO**.

<!-- FIN ANEXO DE TAREAS -->
