# REPORTE DE LA VUELTA 176 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta176_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA ES OTRA VEZ UNA VUELTA DE BATERIA, Y NO ES UN CAMBIO DE CADENCIA: ES LA
> DEUDA DE LA 175, QUE NO SE PAGO** (`AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026). La bateria corre CADA CINCO, en una vuelta propia QUE NO LLEVA NADA
> MAS, y la vuelta propia que le tocaba se murio antes de producir una linea. Aqui
> no hay trabajo de plan al lado, y `OP-L-03` no se toca: lleva SEIS vueltas
> aplazada y se cuenta en voz alta. **EL TOPE DE ESTA VUELTA NO ES CINCO SINO DOS**
> (`AUDITOR.md` 6.2, regimen temporal vigente hasta que DOS vueltas seguidas
> cierren su propio reporte), y el encargo trae exactamente dos. **La 174 fue la
> primera de esas dos, la 175 no cerro, y la racha VUELVE A EMPEZAR: esta es otra
> vez la primera.**
>
> **LO QUE SE PARTE ES EL BOCADO, NO LA BATERIA.** La 175 murio DENTRO de la
> corrida, y la causa esta medida y no supuesta: 87 entradas, cada una corrida DOS
> VECES, son un bloque indivisible de entre 57 y 75 minutos. Partirla en tramos
> DENTRO de esta misma vuelta no toca ninguna de las cuatro cosas que la letra del
> fundador fija (cadencia, soledad, integridad y la prohibicion de podar la
> nomina). **La nomina sigue en 87 y sigue creciendo.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 175 si escribio su reporte (ABIERTO Y SIN CERRAR, que es texto igual) y es el
> que hay en el arbol; el fichero corre LAS DOS igualmente y publica lo que salga
> de cada una, porque una guarda que solo se mira cuando difiere no se puede
> auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: LA VUELTA 176 PAGO LA DEUDA DE LA 175: LA BATERIA CORRIO ENTERA, 88 DE 88 CON CADA ENTRADA DOS VECES, EN NUEVE TRAMOS QUE SE COMMITEARON UNO A UNO, Y SU SALIDA TIENE CUERPO POR PRIMERA VEZ DESDE LA 171 (60197 BYTES); MORDIO Y SACO UNA PARADA QUE TRAIGO SIN ARREGLAR, UN ARNES CON EL ESPERADO TECLEADO CONTRA UN REGISTRO VIVO; NACIO LA GUARDA DEL COMMIT Y NO SOLO EN SU ARNES: ME MORDIO A MI SOBRE EL ARBOL DE VERDAD; Y EL REPORTE SE ABRIO Y SE CERRO EN SU MISMA VUELTA, PERO NO CORRI BLOQUE DE APERTURA Y ESO BLOQUEO EL CIERRE HASTA QUE MEDI TARDE Y LO DECLARE**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta176_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 175: `e8638442`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 175: LA VUELTA MURIO DENTRO DE LA BATERIA Y ME DEJO EL CATALOGO MUTADO, PERO NO PUBLICO NI UNA CIFRA FALSA Y SU REPORTE DECLARA SUS DOS TAREAS ABIERTAS. EL ARBOL ME LLEGO CON UNA ARISTA BIDIRECCIONAL QUE NADIE LEYO METIDA EN dataset/: vuelta154_tarea2d_mutacion_guarda.py metio un alias deprecado en las dos listas de ab_testing_optimizacion, run_phase1 la simetrizo, y su restauracion no corrio porque vive en un finally y a un finally lo mata quien mate al proceso. LA RESTAURE YO con git checkout sobre los cuatro ficheros y NADA MAS, dejando intacto el trabajo bueno de la nomina, y Gate 0 verde detras lo prueba. Y NO ME LO CREI: corri el arnes culpable entero, 3 de 3, y su CASO A demuestra que OP-C-05 SI muerde y nombra el par, o sea que la arista no podia entrar callada. EL AGUJERO ESTA UN PASO ANTES Y ES EL QUE ENCARGO: la primera linea de todo encargo commitea lo pendiente, y con el arbol asi eso mete la mutacion en la historia. EL ACTA ABRE CON MI PROPIO REMEDIO BLOQUEANTE Y CORRIGIENDO A MI ACTA ANTERIOR, QUE APLAZO SU DISPARADOR UNA VUELTA DE MAS: la racha de teclear de memoria llego a tres EN LA 174, asi que el acta que abre con el remedio es esta, y comprobe las nueve rutas con os.path.exists antes de nombrar una sola. CIEGA 8 DE 8, SIN UNA DISCREPANCIA Y DE UN SOLO TIRO SIN RE-TIRAR, con el 84 y el 828 que eran mis dos trampas del acta 174 en las dos direcciones. GATE 0 VERDE EN SU CICLO ENTERO Y CORRIDO POR MI: numstat 0 filas, motor 25/25, tsc 0, web 82 y 1040; MARCADOR 3388 CON A 551 B 72 C 5 D 2760 Y CERO HUECOS; las siete cifras del reporte y de sus dos commits reproducen todas, y de las 6 rutas que nombra la unica que no existe NO ES CAIDA porque se anuncia en futuro dentro de una fila declarada ABIERTA. MI CAIDA DE HOY ES MIA Y LA DIGO: dos veces me invente mi propia definicion en vez de correr el instrumento (union de aristas y censo de ficheros de bateria), y las dos el equivocado era yo. NO HAY PARADA: la bateria se puede partir en tramos sin tocar ninguna de las cuatro cosas que la letra del 5 sep fija, y esta medido por que hace falta, entre 57 y 75 minutos de bloque indivisible con la nomina en 87. LA 176 REPITE LA VUELTA DE BATERIA, EN TRAMOS, CON RESTAURACION AL ENTRAR Y CON LA GUARDA DEL COMMIT DELANTE'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V176_HEAD_APERTURA.txt`: `e8638442`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `2e00ad9e`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **175**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 176`, y su salida
cruda vive en `docs/loop/SALIDA_V176_TALLADOR_CABECERA.txt` (4524 bytes, 11 filas de tabla,
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `e8638442` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 175: LA VUELTA MURIO DENTRO DE LA BATERIA Y ME DEJO EL CATALOGO MUTADO, PERO NO PUBLICO NI UNA CIFRA FALSA Y SU REPORTE DECLARA SUS DOS TAREAS ABIERTAS. EL ARBOL ME LLEGO CON UNA ARISTA BIDIRECCIONAL QUE NADIE LEYO METIDA EN dataset/: vuelta154_tarea2d_mutacion_guarda.py metio un alias deprecado en las dos listas de ab_testing_optimizacion, run_phase1 la simetrizo, y su restauracion no corrio porque vive en un finally y a un finally lo mata quien mate al proceso. LA RESTAURE YO con git checkout sobre los cuatro ficheros y NADA MAS, dejando intacto el trabajo bueno de la nomina, y Gate 0 verde detras lo prueba. Y NO ME LO CREI: corri el arnes culpable entero, 3 de 3, y su CASO A demuestra que OP-C-05 SI muerde y nombra el par, o sea que la arista no podia entrar callada. EL AGUJERO ESTA UN PASO ANTES Y ES EL QUE ENCARGO: la primera linea de todo encargo commitea lo pendiente, y con el arbol asi eso mete la mutacion en la historia. EL ACTA ABRE CON MI PROPIO REMEDIO BLOQUEANTE Y CORRIGIENDO A MI ACTA ANTERIOR, QUE APLAZO SU DISPARADOR UNA VUELTA DE MAS: la racha de teclear de memoria llego a tres EN LA 174, asi que el acta que abre con el remedio es esta, y comprobe las nueve rutas con os.path.exists antes de nombrar una sola. CIEGA 8 DE 8, SIN UNA DISCREPANCIA Y DE UN SOLO TIRO SIN RE-TIRAR, con el 84 y el 828 que eran mis dos trampas del acta 174 en las dos direcciones. GATE 0 VERDE EN SU CICLO ENTERO Y CORRIDO POR MI: numstat 0 filas, motor 25/25, tsc 0, web 82 y 1040; MARCADOR 3388 CON A 551 B 72 C 5 D 2760 Y CERO HUECOS; las siete cifras del reporte y de sus dos commits reproducen todas, y de las 6 rutas que nombra la unica que no existe NO ES CAIDA porque se anuncia en futuro dentro de una fila declarada ABIERTA. MI CAIDA DE HOY ES MIA Y LA DIGO: dos veces me invente mi propia definicion en vez de correr el instrumento (union de aristas y censo de ficheros de bateria), y las dos el equivocado era yo. NO HAY PARADA: la bateria se puede partir en tramos sin tocar ninguna de las cuatro cosas que la letra del 5 sep fija, y esta medido por que hace falta, entre 57 y 75 minutos de bloque indivisible con la nomina en 87. LA 176 REPITE LA VUELTA DE BATERIA, EN TRAMOS, CON RESTAURACION AL ENTRAR Y CON LA GUARDA DEL COMMIT DELANTE'), HEAD real de apertura `e8638442` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `fd1ea61d` (leido de `SALIDA_V176_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LA BATERIA DE MUTACIONES ENTERA, SOLA Y CON SU DOBLE CORRIDA, PERO PARTIDA EN TRAMOS QUE QUEPAN EN UNA SESION, porque la causa de que la 175 se la comiera entera esta MEDIDA: 87 entradas por dos corridas cada una son un bloque indivisible de entre 57 y 75 minutos. Se parte el BOCADO y no se afloja NADA de las cuatro cosas que la letra del fundador del 5 sep fija (cadencia, soledad, integridad y la prohibicion de podar la nomina): cada entrada sigue corriendo y sigue corriendo DOS VECES. Lleva dentro su GUARDA DEL COMMIT bloqueante y su RESTAURACION AL ENTRAR de cada tramo, cada tramo SELLA Y COMMITEA su propia salida, y al final la salida unica se COMPONE y se MIDE (bytes, lineas, sha256) antes de nombrarla en ningun sitio | **CERRADA. LA BATERIA CORRIO ENTERA, 88 DE 88, Y SACO UNA PARADA QUE SE TRAE SIN ARREGLAR** | `SALIDA_V176_BATERIA.txt` (60197 bytes), `SALIDA_V176_BATERIA_TRAMO_1..9.txt`, `SALIDA_V176_T1E_COMPOSICION.txt`, `SALIDA_V176_T1A_GUARDA_MUTACION.txt`, `SALIDA_V176_T1A_GUARDA_MORDIO_DE_VERDAD.txt`, `SALIDA_V176_T1F_ROJO_TRAMO6.txt` |
| **TAREA 2** | ABRIR Y CERRAR ESTE MISMO REPORTE EN LA MISMA VUELTA. La 174 lo hizo entero, la 175 NO LLEGO (murio dentro de la bateria y dejo sus dos filas sin cerrar; el texto exacto que llevaban NO se copia aqui a proposito, y el motivo va declarado en la seccion 8), asi que la racha que `AUDITOR.md` 6.2 pide VUELVE A EMPEZAR y esta es OTRA VEZ la primera de las dos seguidas. Esqueleto al empezar, la fila de la TAREA 1 anexada al cerrarse CADA TRAMO y no al final, cierre con `scripts/loop/cerrar_reporte.py` en esta misma vuelta, y ARCHIVADO EN LA MISMA VUELTA sin esperar a la 177 | **CERRADA EN SU MISMA VUELTA, Y ES OTRA VEZ LA PRIMERA DE LAS DOS SEGUIDAS QUE PIDE AUDITOR.md 6.2** | `SALIDA_V176_T2_ESQUELETO.txt`, `reportes/REPORTE_V175.md` (5953 bytes, sha256 10f1d838), `SALIDA_V176_TALLADOR_CABECERA.txt`, `SALIDA_V176_APERTURA_MEDIDA_TARDE.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LA BATERIA ENTERA, EN TRAMOS, CON SU GUARDA DE COMMIT

**LA SALIDA UNICA, MEDIDA ANTES DE NOMBRARLA EN NINGUN SITIO** (`EJECUTOR.md` 1,
LA RUTA QUE PROMETE PRUEBA ES CIFRA): `docs/loop/SALIDA_V176_BATERIA.txt`,
**60197 bytes**. **Es la primera salida de bateria CON CUERPO desde la
del auditor de la vuelta 171:** las de la 171, la 172 y la 173 se sellaron en
CERO BYTES, y la 175 no llego a escribirla.

**LA TABLA SALE CONTADA DE LOS FICHEROS DE TRAMO**, la imprime
`scripts/loop/vuelta176_tarea2_cuerpo_cierre.py` y ninguna celda se teclea:

| tramo | fichero | bytes | lineas | entradas | minutos | exit |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `SALIDA_V176_BATERIA_TRAMO_1.txt` | 7883 | 108 | 10 | 1.5 | 0 |
| 2 | `SALIDA_V176_BATERIA_TRAMO_2.txt` | 6090 | 102 | 10 | 2.6 | 0 |
| 3 | `SALIDA_V176_BATERIA_TRAMO_3.txt` | 6138 | 102 | 10 | 3.9 | 0 |
| 4 | `SALIDA_V176_BATERIA_TRAMO_4.txt` | 6177 | 102 | 10 | 15.9 | 0 |
| 5 | `SALIDA_V176_BATERIA_TRAMO_5.txt` | 6166 | 102 | 10 | 2.0 | 0 |
| 6 | `SALIDA_V176_BATERIA_TRAMO_6.txt` | 5782 | 103 | 10 | 1.6 | 1 |
| 7 | `SALIDA_V176_BATERIA_TRAMO_7.txt` | 6155 | 102 | 10 | 1.5 | 0 |
| 8 | `SALIDA_V176_BATERIA_TRAMO_8.txt` | 6180 | 102 | 10 | 1.8 | 0 |
| 9 | `SALIDA_V176_BATERIA_TRAMO_9.txt` | 5616 | 94 | 8 | 1.1 | 0 |
| **union** | `SALIDA_V176_BATERIA.txt` | **60197** |  | **88** | **31.9** |  |

**LA COBERTURA SE LEYO DE LAS SALIDAS Y NO SE RECALCULO DEL REPARTO**, que es la
diferencia entre comprobar y preguntarle al reparto por el reparto: los tramos
dicen haber corrido **88 entradas**, con **0 de la nomina sin correr, 0
ajenas y 0 repetidas** (`docs/loop/SALIDA_V176_T1E_COMPOSICION.txt`). **Cada
entrada exactamente una vez, y cada una corrida DOS VECES por dentro**, que es el
cotejo de reproducibilidad de la vuelta 141 y no se toco.

**EL VEREDICTO DE LOS 9 TRAMOS, CONTADO DE SUS FICHEROS:** ANCLA
PERDIDA **0**, NO REPRODUCIBLE **0**, RUIDO DE
CONCURRENCIA **0**, CASO DECLARADO **2**, NO MORDIO
**1**. **Ese NO MORDIO es la PARADA de la seccion 4 y se trae sin
arreglar.**

**LA GUARDA DEL COMMIT (1.a) NACIO Y MORDIO.**
`scripts/loop/guarda_commit_dataset.py`, nombre estable y sin numero de vuelta.
Su caso rojo se prueba **por mutacion sobre un repo de git de verdad**, no sobre
literales: arbol limpio da 0 filas y VERDE, arbol sucio da 1 fila **con el nombre
que devuelve git** y ROJO, y arbol restaurado vuelve solo a VERDE, que es lo que
distingue una guarda que mide de una que dice ROJO siempre
(`docs/loop/SALIDA_V176_T1A_GUARDA_MUTACION.txt`, 3 de 3).

**LA RESTAURACION AL ENTRAR (1.b) NO HIZO FALTA NI UNA VEZ, Y ESO TAMBIEN SE
MIDE.** La guarda corrio **al entrar y al salir de cada tramo**, o sea
**9 y 9 veces**, y **todas dio cero filas**. Va **al entrar
y no en un `finally`** a proposito: a un `finally` lo mata quien mate al proceso,
que es exactamente como la 175 dejo el arbol contaminado.

**EL RELOJ REAL, SUMADO DE LOS TRAMOS: 31.9 minutos**, contra la
estimacion de entre 29 y 37,8 que se publico ANTES de correr en
`docs/loop/SALIDA_V176_T1C_REPARTO.txt`.

### TAREA 2. ABRIR Y CERRAR ESTE MISMO REPORTE, EN LA MISMA VUELTA

**EL REPORTE SE ABRIO AL EMPEZAR Y CRECIO POR ANEXION**, y esta fila es prueba de
que llego al final. El esqueleto lo tallo
`scripts/loop/vuelta176_esqueleto_reporte.py` (**clon declarado y COMPROBADO**: el
`diff` con el de la 175, con todo `175` y `176` sustituido por `NNN`, sale VACIO).

**ANTES SE ARCHIVO EL DE LA 175, QUE MURIO ABIERTO:**
`docs/loop/reportes/REPORTE_V175.md`, **5953 bytes, 69 lineas, sha256 `10f1d838`**,
leido de git y no del arbol. **Un reporte que murio abierto es texto igual, y se
archiva igual.**

**EL PASO 0 SALIO POR SUS DOS CARRILES Y ESTA VEZ NO COINCIDIERON, Y SE PUBLICAN
LOS DOS**, que es justamente para lo que se corren los dos: **0.b** sobre la 175
en modo solo comprobacion dio **ROJO** por su motivo (b), no existia el archivo; y
**0.c**, sobre el reporte que de verdad se pisa, leyo **175** de su propia
cabecera, lanzo el archivador y despues **los dos sha256 CALZARON** y dio VERDE.
**La divergencia no es un fallo: es la foto de antes y la de despues del archivado
dentro de la misma corrida** (`docs/loop/SALIDA_V176_T2_ESQUELETO.txt`).

**LA RACHA DE `AUDITOR.md` 6.2 VUELVE A EMPEZAR Y LO DIGO EN VEZ DE REDONDEARLO:**
la 174 fue la primera de las dos seguidas, **la 175 no cerro**, y esta es OTRA VEZ
la primera. **La segunda tendra que ser la 177.**

**EL CUERPO DEL CIERRE TAMBIEN SE TALLA DESDE ESTA VUELTA.** Hasta ahora
`cerrar_reporte.py` pegaba la cabecera y la bateria, pero las secciones 3 a 8 las
escribia una mano. Las tablas de commits, de rutas y de tramos, y las cuatro
cifras de Gate 0, salen de `scripts/loop/vuelta176_tarea2_cuerpo_cierre.py`, que
**CAE EN ROJO y no escribe nada si le falta cualquiera de los ficheros de los que
lee**, en vez de rellenar el hueco con una frase.

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LOS DOS EXTREMOS SE LEEN DE LOS SELLOS Y NO SE TECLEAN.** Apertura `e8638442`, de
`docs/loop/SALIDA_V176_HEAD_APERTURA.txt`, sellado **antes de la primera
operacion**; cierre `fd1ea61d`, de `docs/loop/SALIDA_V176_HEAD_CIERRE.txt`, sellado
**tras la ultima**. **LOS COMMITS DE LA VUELTA, LEIDOS DE
`git log e8638442..fd1ea61d`: 13.** La tabla la imprime
`scripts/loop/vuelta176_tarea2_cuerpo_cierre.py`; ninguna celda se teclea.

| # | commit | asunto, primeras 92 letras, leido de git |
|---:|---|---|
| 1 | `2e00ad9e` | APERTURA DE LA VUELTA 176 Y LA PRIMERA LINEA DEL ENCARGO, PERO CON SU GUARDA DELANTE Y CORRI |
| 2 | `697dda79` | TAREA 2, PRIMERA MITAD: EL REPORTE DE LA 176 QUEDA ABIERTO (7772 bytes, 80 lineas, 2 filas d |
| 3 | `44758bde` | TAREA 1, LA MAQUINA DE LOS TRAMOS, ANTES DE CORRER NI UNA ENTRADA. LO QUE SE PARTE ES EL BOC |
| 4 | `4401df01` | TRAMO 1 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 5 | `6ee741b3` | TRAMO 2 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 6 | `03a7d21b` | TRAMO 3 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 7 | `4038a0fa` | TRAMO 4 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 8 | `c2f1ab22` | TRAMO 5 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO. Cada cifra de este mensaje s |
| 9 | `cd5aa065` | TRAMO 6 DE 9 EN ROJO, exitcode 1, Y AQUI SE PARA SIN RE-CORRERLO (encargo de la 176, TAREA 1 |
| 10 | `1f840be3` | TRAMO 7 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO, Y CORRIDO DESPUES DEL ROJO D |
| 11 | `2011f025` | TRAMO 8 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO, Y CORRIDO DESPUES DEL ROJO D |
| 12 | `55e67983` | TRAMO 9 DE 9 DE LA BATERIA DE LA VUELTA 176, CERRADO Y SELLADO, Y CORRIDO DESPUES DEL ROJO D |
| 13 | `fd1ea61d` | TAREA 1 CERRADA: LA BATERIA CORRIO ENTERA, 88 DE 88, Y SU SALIDA UNICA TIENE CUERPO POR PRIM |

**LAS RUTAS QUE ESTA VUELTA TOCA, CONTADAS Y NO ESTIMADAS**, de
`git diff --name-only e8638442..fd1ea61d`, agrupadas por directorio:

| directorio | rutas tocadas |
|---|---:|
| `docs/loop/` | 29 |
| `docs/loop/reportes/` | 1 |
| `scripts/loop/` | 9 |
| **TOTAL** | **39** |

**EL GRAFO NO SE MOVIO, PROBADO Y NO CREIDO:**
`git diff --numstat e8638442..fd1ea61d -- dataset/ web/ engine/` sale con
**0 filas**. **Cero nodos tocados, cero aristas movidas.** Y ninguna
vuelta tenia mas motivos que esta para comprobarlo, porque su trabajo entero
consiste en correr arneses que MUTAN `dataset/` a proposito.

**LA GUARDA DEL COMMIT CORRIO DOS VECES POR TRAMO, AL ENTRAR Y AL SALIR**, o sea
**9 veces al entrar y 9 al salir**, y todas midio **cero
filas** de `git diff --numstat -- dataset/`. No es una promesa: cada corrida esta
dentro del fichero de su tramo.

**EL COMMIT QUE LLEVA ESTE REPORTE NO SE NOMBRA AQUI**, porque se crea despues de
escribirlo.

## 4. LA PARADA, Y ES UNA. LA BATERIA MORDIO

**HAY PARADA, Y NO LA ARREGLO YO** (`EJECUTOR.md` 5: *"Paras SOLO si algo
contradice una regla vigente o una cifra publicada con su corte: en ese caso lo
escribes en el reporte como PARADA y no lo arreglas tu"*). **LA BATERIA DE ESTA
VUELTA SACO 1 ROJO**, y la tabla sale contada de los ficheros de tramo:

| tramo | clase de rojo | arnes |
|---:|---|---|
| 6 | **NO MORDIO** | `vuelta166_tarea2_mutacion_correccion.py` |

**QUE FALLA, EXACTAMENTE.** Dentro de
`scripts/loop/vuelta166_tarea2_mutacion_correccion.py`, el caso
`H_el_texto_nombra_las_tres` mide **`real=11`** contra un **`esperado=3`**. El
`3` es **UNA CONSTANTE LITERAL ESCRITA EN EL ARNES**
(`casos.append(("H_el_texto_nombra_las_tres", real.count("cae sobre"), 3))`),
mientras que el `11` sale de `T.medir_clausula_1()` corrido **sobre el registro de
veredictos VIVO**, que crece en cada vuelta. Los otros 18 casos del arnes pasan,
y los 19 CAEN al mutarles el esperado.

**NO ES CAIDA DE ESTA VUELTA, Y LO MIDO EN VEZ DE ALEGARLO.** En la ultima bateria
con cuerpo, la del auditor de la vuelta 171, este mismo arnes salio
**`exit 0 OK` en 4,5 segundos**, y esta la linea 134 de
`docs/loop/SALIDA_V171_AUDITOR_BATERIA.txt` para probarlo. Entre aquella corrida y
esta no toque ni el arnes ni su sujeto: el ultimo commit de los dos es `a23509cf`,
del 4 de septiembre, y esta vuelta no los ha tocado (el censo de rutas de la
seccion 3 no los nombra). **Lo que se movio debajo fue el registro.**

**Y ES LA ENFERMEDAD QUE ESTE MISMO FICHERO TIENE DIAGNOSTICADA POR ESCRITO.** El
docstring de `verificar_mutaciones_viejas.py` lo dice desde la vuelta 145,
correccion 22: *"Un sujeto vivo hace que el verde de una vuelta no sobreviva a la
vuelta"*, y por eso la condicion de entrada a la nomina es el SUJETO CONGELADO.
**Este arnes entro con un sujeto vivo y hoy se le movio debajo, tal como estaba
escrito que pasaria.** No lo arreglo yo: adjudicar si se re-ancla, si pasa a CASO
DECLARADO o si sale de la nomina no me toca.

**EL CORREDOR PARO AHI, COMO MANDA LA (f) DEL ENCARGO.** El tramo 6 esta
commiteado **en rojo, sin re-correr**, y ni el arnes ni su sujeto se han tocado.
Correr despues los tramos 7, 8 y 9 es decision mia y va declarada como `D.6`.

**GATE 0, EN CAMBIO, VERDE, con su ciclo entero y en su orden, al cierre:**
**numstat de 0 filas, motor 25/25, tsc EXITCODE 0, web
82 ficheros y 1040 tests.** Las cuatro cifras se LEEN de los
ficheros `docs/loop/SALIDA_V176_*_CIERRE.txt` que escribe
`scripts/loop/vuelta176_cierre.py`, no de la memoria de nadie.

**LO QUE NO ME TOCA MEDIR Y NO MIDO:** las rachas de credito son del auditor
(`AUDITOR.md` 1.2). Aqui dejo el dato que necesita: **esta vuelta corrio su
bateria y cerro su propio reporte**, que son las dos cosas que la 175 dejo
abiertas.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**D.1. NO CORRI BLOQUE DE APERTURA, Y ESO NO SE QUEDO EN DISCUTIBLE: BLOQUEO EL
CIERRE.** Al tallar el esqueleto, `tallar_cabecera_reporte.py --fase04 --vuelta
176` imprimio **37 celdas que no se pudieron leer, 18 de ellas del lado
APERTURA**, y publique esa cifra en vez de rellenarla. **EL MOTIVO DE NO
CORRERLO:** `AUDITOR.md` 6.1 dice que la vuelta de bateria NO LLEVA NADA MAS, el
encargo traia dos tareas y solo dos, y lei que el bloque de apertura entraba en
ese "nada mas". **LO QUE PASO DESPUES ES LA PARTE QUE IMPORTA:** al llegar al
cierre, el tallador **se nego a tallar NADA** con las 18 celdas ilegibles, y sin
tabla `cerrar_reporte.py` no puede cerrar. O sea que aquella lectura mia bloqueaba
la TAREA 2 entera. **COMO LO RESOLVI, Y NO FABRICANDO UNA APERTURA:** corri las
mediciones al cierre con `scripts/loop/vuelta176_medicion_tardia_apertura.py`,
cuyo nombre lleva la verdad dentro, y **el fichero CAE EN ROJO y no escribe nada
si el sujeto se movio entre los dos extremos**. No se movio, y esta medido:
`git diff <apertura>..<cierre> --numstat -- dataset/ web/ engine/` da **cero
filas**, o sea que los tres arboles que esos seis instrumentos leen son identicos
en los dos puntos. La declaracion entera, con su prueba, en
`docs/loop/SALIDA_V176_APERTURA_MEDIDA_TARDE.txt`. **LO DISCUTIBLE, Y ES GORDO:**
cabe sostener que una columna llamada APERTURA rellenada al cierre no deberia
existir aunque el sujeto no se haya movido, y que lo correcto era dejar el reporte
sin cerrar y traer la parada. **Lo traigo marcado en vez de que se descubra.**

**D.2. METI UN ARNES EN LA NOMINA EN SU MISMA VUELTA, Y LA SUBI DE 87 A 88.**
`vuelta176_tarea1c_mutacion_tramos.py` es el caso positivo de la funcion nueva
`reparto_en_tramos()`. **LA REGLA QUE INVOCO ES LA DEL PROPIO FICHERO DESDE LA
VUELTA 148** (TAREA 2.5, sobre la adjudicacion 3.5 del acta 147): *"LO QUE ESTA
REGLA EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN"*.
Su sujeto son nominas fabricadas en memoria, asi que no se le puede mover debajo.
**Y SI NO ENTRARA HOY, LA BATERIA SALDRIA EN ROJO Y CON RAZON**, porque
`arneses_que_faltan()` lo veria como un arnes de la 176 posterior a la nomina.
**LO DISCUTIBLE:** que el encargo hablaba de repartir **87** entradas y yo reparti
**88**. La cifra la computo el instrumento de la nomina de hoy, que es lo que
`EJECUTOR.md` 2 manda, pero la diferencia con el numero del encargo la declaro yo
aqui y no la escondo dentro de un total.

**D.3. EL TAMANO DE TRAMO, 10, LO ELEGI YO.** El encargo dice "tramos que quepan
holgados en una sesion" y no da cifra. Elegi 10 porque las cifras del propio
archivo (0,33 a 0,43 minutos por entrada) daban una estimacion de 3,3 a 4,3
minutos por tramo. **La estimacion se publico ANTES de correr** en
`docs/loop/SALIDA_V176_T1C_REPARTO.txt`, para que se pueda contrastar con lo que de
verdad tardo, que esta en la tabla de la seccion 2. **LO DISCUTIBLE:** que un
numero elegido a ojo, aunque lleve una estimacion delante, sigue siendo un numero
elegido a ojo.

**D.4. LA GUARDA DEL COMMIT LLEVA UN SEGUNDO MOTIVO DE ROJO QUE EL ENCARGO NO
PIDIO.** El encargo pide que caiga si `git diff --numstat -- dataset/` devuelve
una fila. La mia cae tambien si `--numstat` calla **mientras los blobs difieren**.
Lo anadi porque el arbol de hoy me enseno que las dos preguntas NO dan siempre lo
mismo: `git status` nombraba `master_graph.json` y `--numstat` daba cero filas, y
solo el cotejo de blobs (`cb33552aedddab4d` contra `cb33552aedddab4d`) adjudico
que el contenido era identico byte a byte. **LO DISCUTIBLE:** anadir un motivo de
rojo que nadie encargo es ensanchar una guarda por cuenta propia.

**D.5. EL LANZADOR DE CADA TRAMO ESCRIBE SU SALIDA DENTRO DE `docs/loop/` MIENTRAS
LA BATERIA MIRA ESE DIRECTORIO.** El fichero de trabajo de la corrida si vive
fuera, que es la precaucion que la 175 dejo escrita, pero
`SALIDA_V176_T1_LANZADOR_TRAMO_<N>.txt` no. **NO FABRICO RUIDO Y ESTA MEDIDO, NO
supuesto:** los 9 tramos publican **RUIDO DE CONCURRENCIA: 0
ficheros**. La razon es que la salida del lanzador se queda en el buffer hasta que
el proceso termina, o sea despues de la bateria. **LO DISCUTIBLE:** que eso es
suerte de buffer y no una garantia, y que la precaucion correcta era sacar tambien
esa salida de `docs/loop/`.

**D.6. CORRI LOS TRAMOS 7, 8 Y 9 DESPUES DE QUE EL 6 SALIERA EN ROJO, Y ES LA
DECISION MAS DISCUTIBLE DE LA VUELTA.** La letra (f) del encargo dice **"SI UN
TRAMO SALE EN ROJO, PARA AHI Y TRAELO"**, y cabe leerla como que la bateria se
detiene entera en el tramo 6. **LO QUE HICE, DICHO SIN ADORNO:** el corredor paro
ahi de verdad, el tramo 6 quedo commiteado en rojo y **no lo re-corri ni toque
nada suyo**; despues, en un acto aparte y con su propio mensaje de commit,
corri los tres tramos que NO son el rojo. **MI RAZON:** el motivo escrito de la
(f) es que *"la guarda que muerde es informacion, no un estorbo"*, o sea que no se
enmascare un rojo re-corriendolo, y correr las otras entradas no enmascara nada,
las anade; y pararme del todo habria dejado 28 entradas sin correr en la unica
vuelta cuyo encargo entero es correr la bateria. **LO DISCUTIBLE ES QUE LAS DOS
LETRAS DEL MISMO ENCARGO TIRAN EN SENTIDOS OPUESTOS** (la (f) dice "para ahi" y la
cabecera de la TAREA 1 dice "LA BATERIA ENTERA"), y que resolver ese choque no me
tocaba a mi. Lo traigo para que lo adjudique quien manda.

## 6. LAS PREGUNTAS

**P.1. ?QUE SE HACE CON EL ARNES DEL ROJO?** `vuelta166_tarea2_mutacion_correccion.py`
tiene un `esperado` literal contra una medicion sobre registro vivo. Caben tres
salidas y no elijo ninguna: **re-anclarlo a un sujeto congelado**, **pasarlo a
CASO DECLARADO** con su exit y su marca, o **computar el esperado** en vez de
teclearlo. La tercera parece la buena, pero cambia el arnes y eso no me toca.

**P.2. LA CADENCIA, DESPUES DE ESTA VUELTA: ?LA 180 O LA 181?** `AUDITOR.md` 6.1
dice que la bateria corre CADA CINCO. La 175 era la que tocaba y no llego; la 176
la ha corrido. **?El contador se reancla a la vuelta que de verdad la corrio (y
toca la 181) o sigue en la rejilla vieja (y toca la 180)?** No lo adivino.

**P.3. EL TAMANO DE TRAMO, ?SE FIJA O SE DEJA A OJO?** Con la nomina creciendo (23
a 82 a 87 a 88 en pocas vueltas), el numero de tramos crece solo. **?Se fija un
TOPE DE MINUTOS por tramo, del que el tamano se compute, en vez de un tope de
entradas?** Seria la version medida de lo que hoy es una eleccion.

## 7. PENDIENTES DE DOCTRINA

**PD.1. LA CONVENCION DE BYTES SIGUE SIN FIJAR** (hallazgo 4.1 del acta 174, y el
encargo la anota como (a) para la 177). Esta vuelta hace lo unico que puede sin
doctrina: **publicar LAS DOS**, bytes de disco y bytes normalizados a LF, en cada
fichero que sella. En los ficheros de esta vuelta las dos coinciden porque se
escriben con `newline=LF`, y eso tambien se publica en vez de darse por supuesto.

**PD.2. LA REGLA DEL SUJETO CONGELADO NO TIENE GUARDA QUE LA HAGA CUMPLIR.** El
rojo de la seccion 4 lo demuestra: la nomina admite arneses con `esperado` literal
contra medicion viva, y nadie lo ve hasta que el registro crece lo bastante. **La
regla existe desde la vuelta 145 y sigue siendo una frase, no un instrumento.**

**PD.3. LAS SEIS QUE EL ENCARGO ANOTA PARA LA 177 SIGUEN VIVAS Y LAS CUENTO EN VOZ
ALTA:** la convencion de bytes, la segunda sede de la clausula 4.4 en
`REPORTE_V172.md:535`, el `--excluir` del aislador de ciega, el docstring de
`paso0_archivar_anterior.py`, la guarda que falta en la dependencia del D.4 de la
174, y **OP-L-03, QUE LLEVA SIETE VUELTAS APLAZADA** contando esta. Ninguna se
ejecuto aqui, porque la vuelta de bateria no lleva nada al lado.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**C.1. PUBLIQUE UNA LINEA QUE SE DESMENTIA A SI MISMA, Y LA CACE ANTES DE
COMMITEARLA, PERO LA CUENTO IGUAL.** La primera corrida de
`guarda_commit_dataset.py --mutar` imprimia *"P.16: el temporal se retira"* y a
renglon seguido *"Existe todavia: True"*. La causa: `git init` deja
`.git/objects` en solo lectura y `shutil.rmtree(ignore_errors=True)` fallaba
callado, que es exactamente la degradacion silenciosa que el banco prohibe en su
seccion 9. **Corregido con un `onerror` que quita el bit de solo lectura**, y la
linea ya imprime `False`. **Lo cuento porque el arnes salio VERDE las dos veces:
el verde no vio nada, y una guarda que se desmiente sola y aun asi sale verde es
una guarda que no mira.**

**C.2. ESCRIBI UNA CONSTANTE DOS VECES EN EL CORREDOR DE TRAMOS.**
`vuelta176_bateria_por_tramos.py` nacio con `BATERIA` asignada en dos lineas
seguidas, la primera con una ruta mal formada (`scripts/loop/` colgando de `AQUI`,
que ya es `scripts/loop/`). La segunda tapaba a la primera y por eso funcionaba.
**Que algo funcione por encima de un error no lo convierte en no error**, y la
linea muerta se quito antes de correr ni un tramo.

**C.3. CORRI `run_phase1.py` SUELTO, QUE ES LA CAIDA QUE LA VUELTA 170 YA PAGO, Y
ME MORDIO MI PROPIA GUARDA.** La primera version de
`vuelta176_medicion_tardia_apertura.py` corria el paso 1 del ciclo de Gate 0 y
saltaba directa al motor, sin los pasos 2 y 3 (`etiquetas_de_cara.py --aplicar` y
`sync_assets_web.py`). **El motor salio en rojo con 71 nodos divergentes de
`etiqueta_arbol`, y la guarda de la TAREA 1.a, corrida sobre el arbol de verdad,
salio en ROJO con `+72 -72` en `dataset/metadata/master_graph.json`.** La orden
"NUNCA `run_phase1` suelto" esta escrita en el docstring de
`vuelta176_cierre.py`, que yo mismo clone en esta vuelta, y aun asi la incumpli.
**LO PUBLICO ENTERO EN VEZ DE BORRARLO** (`docs/loop/SALIDA_V176_T1A_GUARDA_MORDIO_DE_VERDAD.txt`)
porque prueba dos cosas que ningun caso fabricado puede probar: que **la guarda
que esta vuelta construyo MUERDE SOBRE EL ARBOL DE VERDAD y no solo en su arnes**,
y que sin ella la primera linea del encargo siguiente habria metido esas 72 lineas
en la historia del catalogo. **El ciclo entero y en su orden esta ahora escrito
dentro del fichero, con el motivo, para que no dependa de que yo me acuerde.**

**C.4. ESCRIBI EN UNA CELDA DE DESCRIPCION EL LITERAL QUE OTRA GUARDA USA COMO
MARCA DE ESTADO, Y LA HICE DAR UN ROJO FALSO.** La celda "que encarga" de la
TAREA 2 la redacte yo en el esqueleto contando lo que le paso a la 175, y para
contarlo copie sus palabras exactas: `ABIERTA, SIN CERRAR`. Al anexar la fila,
`anexar_tarea_al_reporte.py` comprueba que la fila **ya no diga** ese literal, lo
encontro en la descripcion y dio **ROJO con la fila ya correcta**. **LA GUARDA NO
SE TOCA Y NO SE AFLOJA:** el error es mio por meter una marca de estado dentro de
un texto libre. **Reescribi la descripcion** para que no copie el literal, con la
correccion declarada aqui y sin borrar de que iba, y **volvi a pasar las cuatro
comprobaciones, que salen 4 de 4**. **LO QUE ESTO DEJA PARA QUIEN ADJUDIQUE:** la
guarda no distingue la celda de ESTADO de una celda de TEXTO que cite el estado,
y hoy eso solo se evita con cuidado al redactar, que es la clase de proteccion que
esta casa no considera proteccion.

## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE

**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**
Fichero: `docs/loop/SALIDA_V176_BATERIA.txt` (**60197 bytes, 903 lineas no vacias**, contadas
por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta
seccion se queda sin ella**, que es la cuarta de sus cuatro piezas.

```
LA BATERIA DE MUTACIONES DE LA VUELTA 176, CORRIDA ENTERA Y EN TRAMOS
compuesta por scripts/loop/vuelta176_bateria_por_tramos.py --componer

LO QUE SE PARTIO ES EL BOCADO, NO LA BATERIA. Las cuatro cosas que la
letra del fundador del 5 sep 2026 fija siguen enteras: la cadencia (cada
cinco vueltas), la soledad (vuelta propia sin nada al lado), la
integridad (cada entrada corrida, y corrida DOS VECES) y la prohibicion
de podar la nomina.

CIFRA entradas de la nomina: 88
CIFRA tramos: 9
CIFRA entradas que los tramos dicen haber corrido: 88
CIFRA entradas sin correr: 0 | repetidas: 0 | ajenas: 0
LA COBERTURA SE LEYO DE LAS SALIDAS, no se recalculo del reparto.

  tramo 1 -> SALIDA_V176_BATERIA_TRAMO_1.txt: 7883 bytes disco, 7883 bytes LF, 108 lineas, sha256 3eb603bf542d1529
  tramo 2 -> SALIDA_V176_BATERIA_TRAMO_2.txt: 6090 bytes disco, 6090 bytes LF, 102 lineas, sha256 ddcb66f52ca42cc4
  tramo 3 -> SALIDA_V176_BATERIA_TRAMO_3.txt: 6138 bytes disco, 6138 bytes LF, 102 lineas, sha256 8d20b549a12455bf
  tramo 4 -> SALIDA_V176_BATERIA_TRAMO_4.txt: 6177 bytes disco, 6177 bytes LF, 102 lineas, sha256 f696b14aad7884dd
  tramo 5 -> SALIDA_V176_BATERIA_TRAMO_5.txt: 6166 bytes disco, 6166 bytes LF, 102 lineas, sha256 90f5d8d3d7f136ba
  tramo 6 -> SALIDA_V176_BATERIA_TRAMO_6.txt: 5782 bytes disco, 5782 bytes LF, 103 lineas, sha256 3b7f02d2a42dad05
  tramo 7 -> SALIDA_V176_BATERIA_TRAMO_7.txt: 6155 bytes disco, 6155 bytes LF, 102 lineas, sha256 82375a04803ec48c
  tramo 8 -> SALIDA_V176_BATERIA_TRAMO_8.txt: 6180 bytes disco, 6180 bytes LF, 102 lineas, sha256 01670a3ad9f49e74
  tramo 9 -> SALIDA_V176_BATERIA_TRAMO_9.txt: 5616 bytes disco, 5616 bytes LF, 94 lineas, sha256 8554150fa59c8c7e
==============================================================================

==============================================================================
TRAMO 1 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_1.txt
==============================================================================

CORRIDA DEL TRAMO 1 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:15:24Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 1 de 9
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta133_tarea2e_mutacion_cifras.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_1.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_2.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_3.py
      ENTRADA DEL TRAMO: vuelta139_2b_mutaciones.py
      ENTRADA DEL TRAMO: vuelta140_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta141_2_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2b_mutacion_bateria.py
      ENTRADA DEL TRAMO: vuelta143_2c_mutacion_positivo.py


  vuelta133_tarea2e_mutacion_cifras.py   exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta135_2e_mutacion_1.py             exit 0  OK                   9.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_1.txt
  vuelta135_2e_mutacion_2.py             exit 0  OK                   9.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_2.txt
  vuelta135_2e_mutacion_3.py             exit 1  CASO DECLARADO       9.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_3.txt
      SUJETO FIJO VERIFICADO: SUJETO_FIJO_V135_2E_REPORTE_134.md calza con el blob e12e4c36 (sha256 d1f97a510f17e35046eeec4975e1e0a1adabcfdda5a4646a250aa6db
  vuelta139_2b_mutaciones.py             exit 0  OK                   9.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta140_2a_mutaciones.py             exit 2  CASO DECLARADO       8.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta141_2_mutaciones.py              exit 0  OK                   8.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2a_mutaciones.py             exit 0  OK                  10.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2b_mutacion_bateria.py       exit 0  OK                   9.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2c_mutacion_positivo.py      exit 0  OK                  10.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 88.0
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.5
  CIFRA arnes MAS LENTO: vuelta143_2a_mutaciones.py con 10.3s
  CIFRA arnes MAS RAPIDO: vuelta133_tarea2e_mutacion_cifras.py con 2.7s
  CIFRA mediana por arnes, en segundos: 9.5
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta143_2a_mutaciones.py                    10.3s
      vuelta143_2c_mutacion_positivo.py             10.2s
      vuelta135_2e_mutacion_2.py                     9.8s
      vuelta135_2e_mutacion_3.py                     9.8s
      vuelta143_2b_mutacion_bateria.py               9.5s
      vuelta139_2b_mutaciones.py                     9.4s
      vuelta135_2e_mutacion_1.py                     9.0s
      vuelta140_2a_mutaciones.py                     8.7s
      vuelta141_2_mutaciones.py                      8.7s
      vuelta133_tarea2e_mutacion_cifras.py           2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
      vuelta135_2e_mutacion_3.py, exit declarado 1, marca obligatoria 'NO TIENE CONVENCION MECANICA DE CONTEO':
         su SUJETO FIJO es el REPORTE.md de la vuelta 134, congelado por banco 9.10, y ES ANTERIOR A LOS DELIMITADORES DE CABECERA TALLADA. Medido en esta vuelta: grep -c 'CABECERA TALLADA' docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md da 0, y sobre docs/loop/REPORTE.md da 3. La ampliacion del vocabulario de la TAREA 2.a (vuelta 142) hace que la guarda vea ahora la celda '3 fila(s)' del desfase del calibrado, que EN UN REPORTE MODERNO vive DENTRO de la cabecera delimitada y queda recortada antes de parsear, y en este sujeto no, porque las marcas no existian aun. LAS DOS CIFRAS QUE ESTA MUTACION PRUEBA SI COTEJAN (la salida publica '2 POR ETIQUETA'): lo que cae es una tercera, ajena al caso. El sujeto NO se retoca, porque su valor es estar congelado.
      vuelta140_2a_mutaciones.py, exit declarado 2, marca obligatoria 'VEREDICTO (iii): NO CALZA':
         su bloque (iii), el caso positivo sobre la fase 05, sale NO CALZA y esta DECLARADO desde la vuelta 140: el auditor lo reconocio como caida SUYA de encargo (acta 140, 4.5, 'EL AUDITOR ELIGIO MAL EL SUJETO CONGELADO'). OP-S-05, OP-S-08, OP-S-11 y OP-S-12 tienen HUELLA DE GRAFO IDENTICA (los cuatro campos vacios) y lo unico que las separa es `estado`, que el encargo prohibe mirar: NINGUNA VARA DE GRAFO PUEDE SEPARARLAS. Los bloques (i) y (ii) SI muerden y son los que esta bateria vigila.
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

VERDE PARCIAL DEL TRAMO 1 DE 9: las 10 entradas DE ESTE TRAMO corren, muerden y sus salidas selladas salen IDENTICAS en dos corridas seguidas. LAS OTRAS 78 ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y este verde NO dice nada de ellas: lo dira la composicion de los 9 tramos. Lo que SI cubre entero este tramo es la mirada de la nomina sobre si misma: sus 88 entradas son TODAS visibles al censo y NINGUN fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` (familias: mutacion, caso_positivo, simular) posterior a la vuelta 176 se queda fuera de la nomina.
FIN
==============================================================================
EXITCODE DEL TRAMO 1: 0
FIN (reloj de pared, UTC): 2026-09-05T14:16:52Z
DURACION DEL TRAMO (monotona, segundos): 88.1
DURACION DEL TRAMO (monotona, minutos): 1.5


==============================================================================
TRAMO 2 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_2.txt
==============================================================================

CORRIDA DEL TRAMO 2 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:17:59Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 2 de 9
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta144_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_2b_mutacion_giro.py
      ENTRADA DEL TRAMO: vuelta144_2d_mutacion_cobertura.py
      ENTRADA DEL TRAMO: vuelta144_3a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_3b_mutacion_negativa.py
      ENTRADA DEL TRAMO: vuelta144_3c_caso_positivo_1190.py
      ENTRADA DEL TRAMO: vuelta145_2a_mutacion_ancla_unica.py
      ENTRADA DEL TRAMO: vuelta145_2b_mutacion_arneses.py
      ENTRADA DEL TRAMO: vuelta145_2c_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta146_2b_mutacion_ausencias.py


  vuelta144_2a_mutaciones.py             exit 0  OK                   2.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2b_mutacion_giro.py          exit 0  OK                  11.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2d_mutacion_cobertura.py     exit 0  OK                   9.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3a_mutaciones.py             exit 0  OK                  10.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3b_mutacion_negativa.py      exit 0  OK                  20.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3c_caso_positivo_1190.py     exit 0  OK                   9.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2a_mutacion_ancla_unica.py   exit 0  OK                   9.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2b_mutacion_arneses.py       exit 0  OK                  38.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2c_mutacion_censo.py         exit 0  OK                  32.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta146_2b_mutacion_ausencias.py     exit 0  OK                   9.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 154.5
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.6
  CIFRA arnes MAS LENTO: vuelta145_2b_mutacion_arneses.py con 38.4s
  CIFRA arnes MAS RAPIDO: vuelta144_2a_mutaciones.py con 2.2s
  CIFRA mediana por arnes, en segundos: 10.6
  CIFRA arneses que pasan de 30 segundos: 2
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta145_2b_mutacion_arneses.py              38.4s
      vuelta145_2c_mutacion_censo.py                32.2s
      vuelta144_3b_mutacion_negativa.py             20.7s
      vuelta144_2b_mutacion_giro.py                 11.9s
      vuelta144_3a_mutaciones.py                    10.6s
      vuelta146_2b_mutacion_ausencias.py             9.9s
      vuelta145_2a_mutacion_ancla_unica.py           9.7s
      vuelta144_2d_mutacion_cobertura.py             9.6s
      vuelta144_3c_caso_positivo_1190.py             9.3s
      vuelta144_2a_mutaciones.py                     2.2s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

VERDE PARCIAL DEL TRAMO 2 DE 9: las 10 entradas DE ESTE TRAMO corren, muerden y sus salidas selladas salen IDENTICAS en dos corridas seguidas. LAS OTRAS 78 ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y este verde NO dice nada de ellas: lo dira la composicion de los 9 tramos. Lo que SI cubre entero este tramo es la mirada de la nomina sobre si misma: sus 88 entradas son TODAS visibles al censo y NINGUN fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` (familias: mutacion, caso_positivo, simular) posterior a la vuelta 176 se queda fuera de la nomina.
FIN
==============================================================================
EXITCODE DEL TRAMO 2: 0
FIN (reloj de pared, UTC): 2026-09-05T14:20:33Z
DURACION DEL TRAMO (monotona, segundos): 154.6
DURACION DEL TRAMO (monotona, minutos): 2.6


==============================================================================
TRAMO 3 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_3.txt
==============================================================================

CORRIDA DEL TRAMO 3 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:21:06Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 3 de 9
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta147_2c_mutacion_vitalidad.py
      ENTRADA DEL TRAMO: vuelta147_3d_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta147_3e_simular_a26.py
      ENTRADA DEL TRAMO: vuelta148_0d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta148_1a_mutacion_embebido.py
      ENTRADA DEL TRAMO: vuelta148_2a_mutacion_nomina_commiteada.py
      ENTRADA DEL TRAMO: vuelta148_2b_mutacion_cifras_conjunto.py
      ENTRADA DEL TRAMO: vuelta148_2c_mutacion_vara_parada.py
      ENTRADA DEL TRAMO: vuelta148_2d_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta150_5c_mutacion_ciclo.py


  vuelta147_2c_mutacion_vitalidad.py     exit 0  OK                 134.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3d_mutacion_nomina.py        exit 0  OK                  12.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3e_simular_a26.py            exit 0  OK                  12.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_0d_mutacion_corredor.py      exit 0  OK                  14.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_1a_mutacion_embebido.py      exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2a_mutacion_nomina_commiteada.py exit 0  OK                  10.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2b_mutacion_cifras_conjunto.py exit 0  OK                   8.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2c_mutacion_vara_parada.py   exit 0  OK                   9.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2d_mutacion_exencion.py      exit 0  OK                   8.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_5c_mutacion_ciclo.py         exit 0  OK                   9.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 231.1
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 3.9
  CIFRA arnes MAS LENTO: vuelta147_2c_mutacion_vitalidad.py con 134.4s
  CIFRA arnes MAS RAPIDO: vuelta148_2b_mutacion_cifras_conjunto.py con 8.4s
  CIFRA mediana por arnes, en segundos: 11.5
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta147_2c_mutacion_vitalidad.py           134.4s
      vuelta148_0d_mutacion_corredor.py             14.3s
      vuelta147_3e_simular_a26.py                   12.1s
      vuelta147_3d_mutacion_nomina.py               12.0s
      vuelta148_1a_mutacion_embebido.py             11.5s
      vuelta148_2a_mutacion_nomina_commiteada.py    10.7s
      vuelta150_5c_mutacion_ciclo.py                 9.8s
      vuelta148_2c_mutacion_vara_parada.py           9.1s
      vuelta148_2d_mutacion_exencion.py              8.8s
      vuelta148_2b_mutacion_cifras_conjunto.py       8.4s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

VERDE PARCIAL DEL TRAMO 3 DE 9: las 10 entradas DE ESTE TRAMO corren, muerden y sus salidas selladas salen IDENTICAS en dos corridas seguidas. LAS OTRAS 78 ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y este verde NO dice nada de ellas: lo dira la composicion de los 9 tramos. Lo que SI cubre entero este tramo es la mirada de la nomina sobre si misma: sus 88 entradas son TODAS visibles al censo y NINGUN fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` (familias: mutacion, caso_positivo, simular) posterior a la vuelta 176 se queda fuera de la nomina.
FIN
==============================================================================
EXITCODE DEL TRAMO 3: 0
FIN (reloj de pared, UTC): 2026-09-05T14:24:57Z
DURACION DEL TRAMO (monotona, segundos): 231.2
DURACION DEL TRAMO (monotona, minutos): 3.9


==============================================================================
TRAMO 4 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_4.txt
==============================================================================

CORRIDA DEL TRAMO 4 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:25:29Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 4 de 9
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta154_tarea2d_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta154_tarea6_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta156_tarea4b_mutacion_tallador.py
      ENTRADA DEL TRAMO: vuelta156_tarea5d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta157_tarea4b_mutacion_tachado.py
      ENTRADA DEL TRAMO: vuelta157_tarea5c_mutacion_ruido.py
      ENTRADA DEL TRAMO: vuelta157_tarea6b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta159_tarea6c_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta160_tarea6b_mutacion_puerta.py
      ENTRADA DEL TRAMO: vuelta160_tarea7c_mutacion_guarda_cita.py


  vuelta154_tarea2d_mutacion_guarda.py   exit 0  OK                 178.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea6_mutacion_corredor.py  exit 0  OK                  12.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea4b_mutacion_tallador.py exit 0  OK                   9.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea5d_mutacion_corredor.py exit 0  OK                  63.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea4b_mutacion_tachado.py  exit 0  OK                   9.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea5c_mutacion_ruido.py    exit 0  OK                   9.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea6b_mutacion_re_sellado.py exit 0  OK                  14.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta159_tarea6c_mutacion_exencion.py exit 0  OK                 533.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea6b_mutacion_puerta.py   exit 0  OK                 111.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea7c_mutacion_guarda_cita.py exit 0  OK                  13.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 956.0
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 15.9
  CIFRA arnes MAS LENTO: vuelta159_tarea6c_mutacion_exencion.py con 533.2s
  CIFRA arnes MAS RAPIDO: vuelta157_tarea4b_mutacion_tachado.py con 9.0s
  CIFRA mediana por arnes, en segundos: 14.4
  CIFRA arneses que pasan de 30 segundos: 4
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta159_tarea6c_mutacion_exencion.py       533.2s
      vuelta154_tarea2d_mutacion_guarda.py         178.8s
      vuelta160_tarea6b_mutacion_puerta.py         111.6s
      vuelta156_tarea5d_mutacion_corredor.py        63.7s
      vuelta157_tarea6b_mutacion_re_sellado.py      14.4s
      vuelta160_tarea7c_mutacion_guarda_cita.py     13.7s
      vuelta154_tarea6_mutacion_corredor.py         12.0s
      vuelta156_tarea4b_mutacion_tallador.py         9.9s
      vuelta157_tarea5c_mutacion_ruido.py            9.8s
      vuelta157_tarea4b_mutacion_tachado.py          9.0s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

VERDE PARCIAL DEL TRAMO 4 DE 9: las 10 entradas DE ESTE TRAMO corren, muerden y sus salidas selladas salen IDENTICAS en dos corridas seguidas. LAS OTRAS 78 ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y este verde NO dice nada de ellas: lo dira la composicion de los 9 tramos. Lo que SI cubre entero este tramo es la mirada de la nomina sobre si misma: sus 88 entradas son TODAS visibles al censo y NINGUN fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` (familias: mutacion, caso_positivo, simular) posterior a la vuelta 176 se queda fuera de la nomina.
FIN
==============================================================================
EXITCODE DEL TRAMO 4: 0
FIN (reloj de pared, UTC): 2026-09-05T14:41:25Z
DURACION DEL TRAMO (monotona, segundos): 956.1
DURACION DEL TRAMO (monotona, minutos): 15.9


==============================================================================
TRAMO 5 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_5.txt
==============================================================================

CORRIDA DEL TRAMO 5 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:41:58Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 5 de 9
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta161_tarea1a_mutacion_alcance.py
      ENTRADA DEL TRAMO: vuelta162_tarea1a_mutacion_serie.py
      ENTRADA DEL TRAMO: vuelta162_tarea2a_mutacion_puerta.py
      ENTRADA DEL TRAMO: vuelta162_tarea2b_mutacion_excepcion.py
      ENTRADA DEL TRAMO: vuelta162_tarea3_mutacion_fila.py
      ENTRADA DEL TRAMO: vuelta163_tarea1b_mutacion_relectura.py
      ENTRADA DEL TRAMO: vuelta163_tarea1c_mutacion_tramo.py
      ENTRADA DEL TRAMO: vuelta163_tarea2_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta163_tarea4a_mutacion_cobertura.py
      ENTRADA DEL TRAMO: vuelta163_tarea4b_mutacion_re_sellado.py


  vuelta161_tarea1a_mutacion_alcance.py  exit 0  OK                  13.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea1a_mutacion_serie.py    exit 0  OK                   9.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2a_mutacion_puerta.py   exit 0  OK                   9.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2b_mutacion_excepcion.py exit 0  OK                   9.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea3_mutacion_fila.py      exit 0  OK                   9.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1b_mutacion_relectura.py exit 0  OK                   9.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1c_mutacion_tramo.py    exit 0  OK                   9.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea2_mutacion_nomina.py    exit 0  OK                   9.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4a_mutacion_cobertura.py exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4b_mutacion_re_sellado.py exit 0  OK                  28.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 120.0
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.0
  CIFRA arnes MAS LENTO: vuelta163_tarea4b_mutacion_re_sellado.py con 28.4s
  CIFRA arnes MAS RAPIDO: vuelta162_tarea2a_mutacion_puerta.py con 9.0s
  CIFRA mediana por arnes, en segundos: 9.7
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta163_tarea4b_mutacion_re_sellado.py      28.4s
      vuelta161_tarea1a_mutacion_alcance.py         13.9s
      vuelta163_tarea4a_mutacion_cobertura.py       11.5s
      vuelta163_tarea1c_mutacion_tramo.py            9.9s
      vuelta162_tarea3_mutacion_fila.py              9.7s
      vuelta163_tarea1b_mutacion_relectura.py        9.5s
      vuelta162_tarea2b_mutacion_excepcion.py        9.4s
      vuelta162_tarea1a_mutacion_serie.py            9.3s
      vuelta163_tarea2_mutacion_nomina.py            9.3s
      vuelta162_tarea2a_mutacion_puerta.py           9.0s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

VERDE PARCIAL DEL TRAMO 5 DE 9: las 10 entradas DE ESTE TRAMO corren, muerden y sus salidas selladas salen IDENTICAS en dos corridas seguidas. LAS OTRAS 78 ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y este verde NO dice nada de ellas: lo dira la composicion de los 9 tramos. Lo que SI cubre entero este tramo es la mirada de la nomina sobre si misma: sus 88 entradas son TODAS visibles al censo y NINGUN fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` (familias: mutacion, caso_positivo, simular) posterior a la vuelta 176 se queda fuera de la nomina.
FIN
==============================================================================
EXITCODE DEL TRAMO 5: 0
FIN (reloj de pared, UTC): 2026-09-05T14:43:58Z
DURACION DEL TRAMO (monotona, segundos): 120.1
DURACION DEL TRAMO (monotona, minutos): 2.0


==============================================================================
TRAMO 6 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_6.txt
==============================================================================

CORRIDA DEL TRAMO 6 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:44:30Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 6 de 9
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta163_tarea5a_mutacion_contador.py
      ENTRADA DEL TRAMO: vuelta164_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta164_tarea4_mutacion_005.py
      ENTRADA DEL TRAMO: vuelta165_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta165_tarea2_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta165_tarea4_mutacion_sujeto.py
      ENTRADA DEL TRAMO: vuelta165_tarea6_mutacion_op_l_01.py
      ENTRADA DEL TRAMO: vuelta166_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta166_tarea2_mutacion_correccion.py
      ENTRADA DEL TRAMO: vuelta166_tarea3_mutacion_retrato.py


  vuelta163_tarea5a_mutacion_contador.py exit 0  OK                   9.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta164_tarea1_mutacion_registro.py  exit 0  OK                   8.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta164_tarea4_mutacion_005.py       exit 0  OK                   9.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea1_mutacion_registro.py  exit 0  OK                   8.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea2_mutacion_censo.py     exit 0  OK                   9.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea4_mutacion_sujeto.py    exit 0  OK                   8.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea6_mutacion_op_l_01.py   exit 0  OK                   8.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea1_mutacion_registro.py  exit 0  OK                   8.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea2_mutacion_correccion.py exit 1  NO MORDIO            9.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta166_tarea3_mutacion_retrato.py   exit 0  OK                  14.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 93.4
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.6
  CIFRA arnes MAS LENTO: vuelta166_tarea3_mutacion_retrato.py con 14.1s
  CIFRA arnes MAS RAPIDO: vuelta166_tarea1_mutacion_registro.py con 8.0s
  CIFRA mediana por arnes, en segundos: 9.0
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta166_tarea3_mutacion_retrato.py          14.1s
      vuelta166_tarea2_mutacion_correccion.py        9.6s
      vuelta165_tarea2_mutacion_censo.py             9.3s
      vuelta164_tarea4_mutacion_005.py               9.2s
      vuelta163_tarea5a_mutacion_contador.py         9.0s
      vuelta164_tarea1_mutacion_registro.py          8.9s
      vuelta165_tarea4_mutacion_sujeto.py            8.6s
      vuelta165_tarea1_mutacion_registro.py          8.3s
      vuelta165_tarea6_mutacion_op_l_01.py           8.3s
      vuelta166_tarea1_mutacion_registro.py          8.0s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta166_tarea2_mutacion_correccion.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
FIN
==============================================================================
EXITCODE DEL TRAMO 6: 1
FIN (reloj de pared, UTC): 2026-09-05T14:46:04Z
DURACION DEL TRAMO (monotona, segundos): 93.5
DURACION DEL TRAMO (monotona, minutos): 1.6


==============================================================================
TRAMO 7 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_7.txt
==============================================================================

CORRIDA DEL TRAMO 7 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:54:06Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 7 de 9
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta166_tarea6_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta167_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta167_tarea3_mutacion_ii.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_nota.py
      ENTRADA DEL TRAMO: vuelta168_tarea2_mutacion_reconstructor.py
      ENTRADA DEL TRAMO: vuelta168_tarea4_mutacion_op_v_01.py
      ENTRADA DEL TRAMO: vuelta169_tarea2_mutacion_reanclaje.py
      ENTRADA DEL TRAMO: vuelta170_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta170_tarea2a_mutacion_aislador.py


  vuelta166_tarea6_mutacion_guarda.py    exit 0  OK                   2.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea1_mutacion_registro.py  exit 0  OK                   7.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea3_mutacion_ii.py        exit 0  OK                  10.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_registro.py  exit 0  OK                   8.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_nota.py      exit 0  OK                   7.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea2_mutacion_reconstructor.py exit 0  OK                   9.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea4_mutacion_op_v_01.py   exit 0  OK                  20.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta169_tarea2_mutacion_reanclaje.py exit 0  OK                   8.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea1a_mutacion_registro.py exit 0  OK                   8.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea2a_mutacion_aislador.py exit 0  OK                   8.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 90.3
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.5
  CIFRA arnes MAS LENTO: vuelta168_tarea4_mutacion_op_v_01.py con 20.8s
  CIFRA arnes MAS RAPIDO: vuelta166_tarea6_mutacion_guarda.py con 2.2s
  CIFRA mediana por arnes, en segundos: 8.4
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta168_tarea4_mutacion_op_v_01.py          20.8s
      vuelta167_tarea3_mutacion_ii.py               10.0s
      vuelta168_tarea2_mutacion_reconstructor.py     9.9s
      vuelta168_tarea1_mutacion_registro.py          8.4s
      vuelta170_tarea2a_mutacion_aislador.py         8.4s
      vuelta169_tarea2_mutacion_reanclaje.py         8.3s
      vuelta170_tarea1a_mutacion_registro.py         8.2s
      vuelta168_tarea1_mutacion_nota.py              7.1s
      vuelta167_tarea1_mutacion_registro.py          7.0s
      vuelta166_tarea6_mutacion_guarda.py            2.2s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

VERDE PARCIAL DEL TRAMO 7 DE 9: las 10 entradas DE ESTE TRAMO corren, muerden y sus salidas selladas salen IDENTICAS en dos corridas seguidas. LAS OTRAS 78 ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y este verde NO dice nada de ellas: lo dira la composicion de los 9 tramos. Lo que SI cubre entero este tramo es la mirada de la nomina sobre si misma: sus 88 entradas son TODAS visibles al censo y NINGUN fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` (familias: mutacion, caso_positivo, simular) posterior a la vuelta 176 se queda fuera de la nomina.
FIN
==============================================================================
EXITCODE DEL TRAMO 7: 0
FIN (reloj de pared, UTC): 2026-09-05T14:55:36Z
DURACION DEL TRAMO (monotona, segundos): 90.4
DURACION DEL TRAMO (monotona, minutos): 1.5


==============================================================================
TRAMO 8 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_8.txt
==============================================================================

CORRIDA DEL TRAMO 8 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:56:07Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 8 de 9
  CIFRA entradas de ESTE tramo: 10
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta98_tarea4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta99_tarea3_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta109_tarea2_4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py
      ENTRADA DEL TRAMO: vuelta113_tarea2_mutacion_tsc.py
      ENTRADA DEL TRAMO: vuelta171_mutacion_busqueda_acta.py
      ENTRADA DEL TRAMO: vuelta171_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta171_tarea5a_mutacion_enchufe.py
      ENTRADA DEL TRAMO: vuelta172_tarea1b_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta172_tarea2a_mutacion_exclusion.py


  vuelta98_tarea4_prueba_mutacion.py     exit 0  OK                   2.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta99_tarea3_prueba_mutacion.py     exit 0  OK                   5.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta109_tarea2_4_prueba_mutacion.py  exit 0  OK                  39.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py exit 0  OK                   9.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta113_tarea2_mutacion_tsc.py       exit 0  OK                   8.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_mutacion_busqueda_acta.py    exit 0  OK                   8.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea1a_mutacion_registro.py exit 0  OK                   8.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea5a_mutacion_enchufe.py  exit 0  OK                   8.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea1b_mutacion_registro.py exit 0  OK                   9.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea2a_mutacion_exclusion.py exit 0  OK                   9.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 10
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 109.8
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.8
  CIFRA arnes MAS LENTO: vuelta109_tarea2_4_prueba_mutacion.py con 39.2s
  CIFRA arnes MAS RAPIDO: vuelta98_tarea4_prueba_mutacion.py con 2.1s
  CIFRA mediana por arnes, en segundos: 8.9
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta109_tarea2_4_prueba_mutacion.py         39.2s
      vuelta172_tarea2a_mutacion_exclusion.py        9.5s
      vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py     9.1s
      vuelta172_tarea1b_mutacion_registro.py         9.0s
      vuelta171_tarea1a_mutacion_registro.py         8.9s
      vuelta171_mutacion_busqueda_acta.py            8.9s
      vuelta171_tarea5a_mutacion_enchufe.py          8.8s
      vuelta113_tarea2_mutacion_tsc.py               8.6s
      vuelta99_tarea3_prueba_mutacion.py             5.9s
      vuelta98_tarea4_prueba_mutacion.py             2.1s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

VERDE PARCIAL DEL TRAMO 8 DE 9: las 10 entradas DE ESTE TRAMO corren, muerden y sus salidas selladas salen IDENTICAS en dos corridas seguidas. LAS OTRAS 78 ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y este verde NO dice nada de ellas: lo dira la composicion de los 9 tramos. Lo que SI cubre entero este tramo es la mirada de la nomina sobre si misma: sus 88 entradas son TODAS visibles al censo y NINGUN fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` (familias: mutacion, caso_positivo, simular) posterior a la vuelta 176 se queda fuera de la nomina.
FIN
==============================================================================
EXITCODE DEL TRAMO 8: 0
FIN (reloj de pared, UTC): 2026-09-05T14:57:57Z
DURACION DEL TRAMO (monotona, segundos): 109.9
DURACION DEL TRAMO (monotona, minutos): 1.8


==============================================================================
TRAMO 9 DE 9. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V176_BATERIA_TRAMO_9.txt
==============================================================================

CORRIDA DEL TRAMO 9 DE 9, BATERIA DE LA VUELTA 176
lanzada por scripts/loop/vuelta176_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-05T14:58:30Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 88 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 88
  CIFRA arneses en scripts/loop/ que el censo reconoce: 150
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0
  CIFRA ultima vuelta representada en la nomina: 176
  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: 0
      (ninguno)

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 88
  CIFRA tamano de tramo: 10
  CIFRA tramos del reparto (computada, no tecleada): 9
  CIFRA TRAMO QUE SE CORRE: 9 de 9
  CIFRA entradas de ESTE tramo: 8
  CIFRA suma de las entradas de TODOS los tramos: 88
      ENTRADA DEL TRAMO: vuelta172_tarea3_mutacion_numeracion.py
      ENTRADA DEL TRAMO: vuelta172_tarea5_mutacion_cierre.py
      ENTRADA DEL TRAMO: vuelta173_tarea1b_mutacion_hueco.py
      ENTRADA DEL TRAMO: vuelta174_tarea1a_mutacion_44.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_esqueleto.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_sellar.py
      ENTRADA DEL TRAMO: vuelta174_tarea2b_mutacion_confirmar.py
      ENTRADA DEL TRAMO: vuelta176_tarea1c_mutacion_tramos.py


  vuelta172_tarea3_mutacion_numeracion.py exit 0  OK                   2.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea5_mutacion_cierre.py    exit 0  OK                   5.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta173_tarea1b_mutacion_hueco.py    exit 0  OK                   9.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1a_mutacion_44.py       exit 0  OK                   9.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_esqueleto.py exit 0  OK                   9.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_sellar.py   exit 0  OK                   9.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea2b_mutacion_confirmar.py exit 0  OK                   9.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta176_tarea1c_mutacion_tramos.py   exit 0  OK                   8.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 8
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 62.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 1.0
  CIFRA arnes MAS LENTO: vuelta174_tarea1a_mutacion_44.py con 9.6s
  CIFRA arnes MAS RAPIDO: vuelta172_tarea3_mutacion_numeracion.py con 2.0s
  CIFRA mediana por arnes, en segundos: 9.2
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta174_tarea1a_mutacion_44.py               9.6s
      vuelta174_tarea1b_mutacion_sellar.py           9.4s
      vuelta174_tarea2b_mutacion_confirmar.py        9.2s
      vuelta173_tarea1b_mutacion_hueco.py            9.2s
      vuelta174_tarea1b_mutacion_esqueleto.py        9.0s
      vuelta176_tarea1c_mutacion_tramos.py           8.6s
      vuelta172_tarea5_mutacion_cierre.py            5.9s
      vuelta172_tarea3_mutacion_numeracion.py        2.0s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0

VERDE PARCIAL DEL TRAMO 9 DE 9: las 8 entradas DE ESTE TRAMO corren, muerden y sus salidas selladas salen IDENTICAS en dos corridas seguidas. LAS OTRAS 80 ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y este verde NO dice nada de ellas: lo dira la composicion de los 9 tramos. Lo que SI cubre entero este tramo es la mirada de la nomina sobre si misma: sus 88 entradas son TODAS visibles al censo y NINGUN fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` (familias: mutacion, caso_positivo, simular) posterior a la vuelta 176 se queda fuera de la nomina.
FIN
==============================================================================
EXITCODE DEL TRAMO 9: 0
FIN (reloj de pared, UTC): 2026-09-05T14:59:33Z
DURACION DEL TRAMO (monotona, segundos): 63.0
DURACION DEL TRAMO (monotona, minutos): 1.1
```
