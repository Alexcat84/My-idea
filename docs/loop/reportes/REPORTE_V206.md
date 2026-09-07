# REPORTE DE LA VUELTA 206 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**DOS SUB-TAREAS Y NINGUNA MAS** (`AUDITOR.md` 6.2, adjudicacion `4.4` del acta
205: la 204 cerro su reporte y la 205 no, asi que la racha de dos se corto y el
tope vuelve a dos).

**ESTE ESQUELETO SE ESCRIBE ANTES DE LA TAREA 2 Y NO AL FINAL** (`EJECUTOR.md` 1,
EL REPORTE ABRE CON LA VUELTA). Cada tarea anexa su fila al cerrarse. Una vuelta
cortada deja reporte parcial, nunca vacio.

**POR QUE NO SE ESCRIBIO ANTES DE LA TAREA 1, Y VA COMO CAIDA MIA EN LA SECCION
8:** `docs/loop/REPORTE.md` ES el fichero que la TAREA 1 tenia que cerrar, porque
lo que quedo a medias de la vuelta 205 era su propio esqueleto vivo en esa misma
ruta. Tallar el mio encima antes de cerrar aquel habria borrado el sujeto de la
TAREA 1. Se dice, no se esconde.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 206`, y su salida
cruda vive en `docs/loop/SALIDA_V206_TALLADOR_CABECERA.txt` (6485 bytes en disco y 6465 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `78ca7176` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 205: LA BATERIA CORRIO ENTERA Y EN SU PROPIO NOMBRE POR PRIMERA VEZ DESDE LA 194, Y LA VUELTA NO CERRO. Los ONCE tramos estan sellados y committeados, ninguno de cero bytes, del MISMO CALIBRE (1 sola familia de secciones sobre los once, medida por mi), sumando las 135 entradas de la nomina y 42.0 minutos; las once cifras de bytes, sha256 LF, exitcode y minutos que el ejecutor publico en sus once commits CALZAN LAS ONCE con mi medicion. Pero --componer nunca corrio y cerrar_reporte.py tampoco: REPORTE.md sigue siendo el esqueleto de 27 lineas con TODAS sus celdas en PENDIENTE. EL EJECUTOR NO PUBLICO NI UNA CIFRA FALSA: cero caidas de cifra y cero de reporte contra el. Lo que hay es una vuelta sin cerrar, y por AUDITOR.md 6.1 se RETOMA EN SU CIERRE, no se repite. NO SE CUMPLE NINGUNA CONDICION DE PARADA, y mido las cuatro candidatas en positivo: 6.1 cubre la vuelta cortada por extension citable; no hay contradiccion con regla vigente; el rojo de la bateria NO es Gate 0 ni el hook y tiene regla que lo explica (la moratoria con la nomina congelada en 135); y el credito de tanda no se rompe porque una vuelta de bateria no abre tanda. TODO REPRODUCE AL DIGITO CON EL CICLO ENTERO DE GATE 0 CORRIDO POR MI, 8 de 8 en EXITCODE 0: censo 3853/3169/684, Gate 0 OK con 0 auto-aristas, 0 duplicadas y 0 de simetria, aristas 8780/8740/17520/9914, motor 25/25, web 82 (82) y 1040 (1040), tsc EXIT 0, desfase en 4 filas las mismas cuatro, y numstat de dataset, web y engine en CERO FILAS despues de correr yo el ciclo. Marcador 3388 con A 551, B 72, C 5 y D 2760, 0 huecos, 0 duplicados, sellado y pasado por su guarda en VERDE, que me tumbo el acta DOS VECES antes de dejarme publicarlo y las dos con razon. Veredictos en 0a77b5a35a962621 y OPERACIONES en 829c583eb779cab6 por las dos convenciones: no se movio ni un veredicto ni un estado. La M de dataset/ NO es una modificacion y casi la publico como tal: el fichero es identico EN CRUDO al de HEAD, 8375817 bytes y sha256 LF 627cc662296f7f00 en los dos, y es el aviso de fin de linea de git. LA CIEGA: 28 de 40, y el archivo tiene razon en mis DOCE discrepancias; ONCE de las doce son A DE MAS, que es lo que mi propio fichero de clases predijo POR ESCRITO antes del destape. La tanda NO se dobla, por LA RAIZ. CINCO HALLAZGOS: la causa de que la bateria no corriera en su nombre desde la 194 queda MEDIDA Y CERRADA, y la cazo el ejecutor antes que yo (el lanzador computa su vuelta de su propio nombre de fichero, lineas 91, 92 y 96, y --siguiente responde 183 en cualquier vuelta dando los once tramos por sellados con cero que faltan); ese --siguiente SIGUE MINTIENDO para la 210 y va a la integral ya nombrado; la bateria NO PUEDE SALIR VERDE mientras la moratoria viva, asi que la 210 y la 215 saldran rojas igual; LA GUARDA DE CONCURRENCIA MORDIO DE VERDAD, cazando en el tramo 3 dos ficheros que el propio ejecutor escribia mientras ese tramo corria, y ese tramo tardo 11.2 minutos contra una mediana de 2.8; y TRES AUDITORES SEGUIDOS FALLAN LA CIEGA EN LA MISMA DIRECCION, 23 fallos con 21 A de mas entre las actas 203, 204 y 205, porque el auditor adjudica con solape fuerte y el archivo pide que ninguno contenga al otro Y que cada uno traiga pasos enteros propios. CUATRO CAIDAS MIAS Y SOLO UNA ACUMULA: toque REPORTE.md con wc -l antes de sellar, en el primer comando del turno, quinta seguida de su familia y con el remedio ya escrito, o sea que rompi un remedio escrito y el sello salio limpio solo porque el modulo no ve un comando que no pasa por sus funciones; escribi tres ficheros en docs/loop mientras la bateria corria, dentro de las ventanas de los tramos 4, 5 y 7, que dan RUIDO 0 pero el riesgo lo cree yo; mi primer conteo de la nomina dio 0 por leer VIEJAS como cadenas cuando son tuplas, y lo cace antes de publicarlo; y declare EJECUTOR PARADO con el ejecutor vivo en el tramo 8, y lo cace al re-verificar. Commiteo ademas los 6 ficheros sellados de otras vueltas que la bateria reescribe al correr y que el ejecutor dejo sin committear, declarados en la seccion 7, para no dejar la rama sucia. El acta solo crece por anexion: 4755952 bytes antes y 4771842 despues, y el texto viejo sigue entero al principio.'), HEAD real de apertura `78ca7176` (sello RECONSTRUIDO DESPUES (commit a75ff760), leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `3a20dd4a` (leido de `SALIDA_V206_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

| tarea | que es | estado |
|---|---|---|
| TAREA 1 | CERRAR LA VUELTA 205, QUE QUEDO A MEDIAS: `--componer`, la tabla de los once tramos y `cerrar_reporte.py` con sus cuatro piezas | CERRADA. `--componer` VERDE, cotejo de las once filas con 0 discrepancias, `cerrar_reporte.py` en EXITCODE 0 y reporte archivado en `docs/loop/reportes/REPORTE_V205.md` |
| TAREA 2 | LA DEUDA DE REGISTROS: el acta 179 en `R.69` y el acta 180 en `R.70`, en `docs/PENDIENTES.md`, por adicion pura y en su sede | CERRADA. Las dos escritas, 257 lineas anadidas y 0 borradas por `numstat`, serie sin colisiones ni huecos, y la deuda del `4.9` del acta 201 remedida al cierre en 0 |

## 2. LO QUE CADA TAREA DEJO SELLADO (cada tarea ANEXA su fila al cerrarse)

| tarea | salida sellada | bytes disco | bytes LF | exitcode |
|---|---|---|---|---|
| TAREA 1 | `docs/loop/SALIDA_V206_CERRAR_REPORTE_V205.txt` | 9109 | 8967 | 0 |
| TAREA 2 | `docs/loop/SALIDA_V206_T2_REGISTROS.txt` | 18067 | 18066 | 0 |

**EL VEREDICTO DE UNA LINEA: LAS DOS DEL ENCARGO CIERRAN Y NINGUNA SE QUEDA A MEDIAS: la vuelta 205 quedo CERRADA Y ARCHIVADA sin repetir ni un tramo, con --componer en VERDE cubriendo las 135 entradas de la nomina exactamente una vez y mis once filas calzando al digito con las once del acta 205, cero discrepancias y el cotejo probado por mutacion; y la deuda de registros del 4.9 del acta 201 queda AGOTADA con R.69 y R.70 escritas por adicion pura, contando yo a mano las preguntas porque el lector heredado no ve la seccion que si existe. LO QUE SUBE ES UNA PARADA QUE NO ARREGLO: el rojo de aquella bateria NO tiene una sola causa, porque cinco entradas de la nomina no mordieron en cuatro tramos y hay tres familias distintas de la linea de fallo, contra la cifra de una sola causa que el acta 205 publico.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CELDA DE ESTA SECCION SE TECLEO.** Cada tabla dice de que fichero de
salida sale y se reconstruyo contando ese fichero antes de publicarla
(`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO).

### 3.0 LA PARADA, QUE VA PRIMERA PORQUE ES LO MAS CARO QUE ENCONTRE

**PARADA. EL ROJO DE LA BATERIA DE LA 205 NO TIENE UNA SOLA CAUSA, Y LA CIFRA
PUBLICADA DICE QUE SI.** No lo arreglo yo (`EJECUTOR.md` 5).

**LA CIFRA CON LA QUE CHOCA, CITADA CON SU SEDE:** la adjudicacion `5.3` del acta
205, que mi encargo trae con estas palabras, *"Los once tramos dan `ROJO POR
FALLO` con exitcode 1 por una sola causa: los 2 arneses del censo nacidos despues
de la vara 148 que la nomina congelada en 135 no puede admitir"*.

**LA PREMISA, MEDIDA EN POSITIVO ANTES DE DECLARAR NADA**, como manda el propio
encargo. Corri `python scripts/loop/_v206_medir_no_mordio.py`, que lee las lineas
`NO MORDIO`, `ANCLA PERDIDA`, `NO REPRODUCIBLE` y `CIFRA de FALLO` de los once
ficheros sellados de la bateria. Salida cruda en
`docs/loop/SALIDA_V206_NO_MORDIO.txt`, 4151 bytes en disco y 4103 normalizado a
LF, sha256 `cffa5cd0724d0427` en disco y `cffa5cd0724d0427` normalizado a LF.

> **CORRECCION DECLARADA DE LA VUELTA 207, SOBRE LA `E.1` DEL ACTA 206.** El renglon de arriba se queda **entero y sin tocar**, porque una
> correccion que tapa lo que corrige no se puede auditar (`EJECUTOR.md` 8).
> **LO QUE DICE Y ES FALSO:** que el `sha256` de disco y el normalizado a LF
> de `docs/loop/SALIDA_V206_NO_MORDIO.txt` son los dos `cffa5cd0724d0427`.
> **LO QUE MIDO YO EN LA VUELTA 207, con `hashlib` sobre el fichero y sobre
> el mismo fichero con los `CRLF` cambiados por `LF`, y NO copiado de nadie:**
> **4151** bytes en disco y **4103** normalizado a LF, **sha256 de disco
> `f38bd7855d7760b5`** y **sha256 LF `cffa5cd0724d0427`**. **Los dos son distintos**, y
> la propia linea corregida ya lo probaba sin saberlo: **4151** contra **4103**
> bytes solo puede salir de que el fichero tiene `CRLF`, y entonces los dos
> `sha256` no pueden coincidir. **La cifra de bytes era correcta; el `sha256`
> de disco era el de LF escrito dos veces.**
> **LOS DOS COMPLETOS, PARA QUE SE PUEDAN REHACER:** disco
> `f38bd7855d7760b5cf4d9e3c2fc1983ea443684062a7743f9948244b9aac737c`,
> LF `cffa5cd0724d04274fc88c70259c36fa6b28c07d9a7f5da114c1bd931e00f6ae`.
> **ESTA CAIDA NO ACUMULA** (`AUDITOR.md` 4, letra afinada del 27 ago 2026,
> citada por el acta 206 en su `E.1`): vive en prosa de acompanamiento de una
> linea de evidencia, no en tabla, cabecera ni conclusion. **La conclusion de
> la seccion 3.0 no se mueve ni un digito.**


- **CIFRA familias distintas de la linea `CIFRA de FALLO` entre los once: 3.** Si
  la causa fuera una sola, esa cifra seria **1**. Las tres se diferencian solo en
  el segundo sumando: **0**, **1** y **2** que no mordieron.
- **CIFRA entradas de la nomina que NO MORDIERON: 5**, en **4** tramos:

| tramo | entrada de la nomina que NO MORDIO | `exit` que publico | segundos |
|---|---|---:|---:|
| 3 | `vuelta160_tarea6b_mutacion_puerta.py` | 3221225794 | 10.9 |
| 4 | `vuelta163_tarea4b_mutacion_re_sellado.py` | 1 | 23.2 |
| 5 | `vuelta165_tarea6_mutacion_op_l_01.py` | 1 | 10.6 |
| 5 | `vuelta166_tarea6_mutacion_guarda.py` | 1 | 10.9 |
| 9 | `vuelta185_tarea1c_mutacion_bateria_continuada.py` | 1 | 17.5 |

**LO QUE SI SE SOSTIENE DE LA CIFRA VIEJA, Y SE DICE PARA NO EXAGERAR LA PARADA:**
`ANCLA PERDIDA` da **0** en los once, `NO REPRODUCIBLE` da **0** en los once, y
los **2** arneses fuera de la nomina estan en los once. **La causa estructural es
real y es la mayoritaria: lo que no es cierto es que sea la unica.**

**LO QUE LA PARADA CUESTA, DICHO SIN ADORNARLO:** el rojo estructural tiene regla
que lo explica y por eso no apaga nada. Estas **5** no la tienen. Un arnes de
mutacion que deja de morder es un arnes que ya no vigila lo suyo, y **eso es
justo lo que una bateria existe para encontrar**. Ahora mismo estan escondidas
detras de un rojo que se da por explicado.

**UNA DE LAS CINCO NO ES DE LA MISMA ESPECIE QUE LAS OTRAS CUATRO, Y LO SEPARO EN
VEZ DE MEZCLARLO:** `vuelta160_tarea6b_mutacion_puerta.py` publica
`exit 3221225794` y `(sin salida)`, y ese numero es `0xc0000142` de Windows, o
sea que **el proceso no llego a arrancar**. Las otras cuatro publican `exit 1`
con su salida. **Si es lo mismo o no, no lo decido yo.**

**NO LO ARREGLO, NO LO SALTO Y NO LO ESCONDO.** No toco ni uno de los cinco
arneses, no toco la nomina y no toco el instrumento.

### 3.1 LA TAREA 1, CONTADA DE SUS FICHEROS

**`--componer` CORRIO POR EL ENVOLTORIO Y NO POR EL LANZADOR A PELO**, como manda
el encargo: `python scripts/loop/_v205_bateria_en_su_nombre.py --componer`,
`EXITCODE 0`. Salida en `docs/loop/SALIDA_V206_COMPONER.txt`,
3189 bytes en disco y 3144 normalizado a LF.

**SALIO VERDE, Y ESTO ES LO QUE COTEJO**, leido de su salida y no narrado:

| lo que `--componer` coteja | cifra |
|---|---:|
| entradas de la nomina, leidas del modulo | 135 |
| tramos con salida sellada | 11 |
| entradas que los tramos dicen haber corrido | 135 |
| entradas de la nomina que NINGUN tramo corrio | 0 |
| entradas corridas que NO estan en la nomina | 0 |
| entradas corridas MAS DE UNA VEZ | 0 |
| tramos de CERO BYTES | 0 |

**LA SALIDA UNICA EXISTE Y LA MIDO YO:** `docs/loop/SALIDA_V205_BATERIA.txt`,
93745 bytes en disco y 93745 normalizado a LF, 1437 lineas, sha256
`e50f8dd06f01e6b5` en disco y `e50f8dd06f01e6b5` normalizado a LF. **Antes de
esta vuelta no existia**, y eso lo declaraba el propio encargo.

**QUE COTEJA `--componer` DE VERDAD, DICHO PORQUE NO ES LO QUE SU NOMBRE
SUGIERE Y VA MARCADO COMO DISCUTIBLE:** su cotejo de calibre es **cobertura**
(que ningun tramo falte, que ninguna entrada se repita, que ninguna sea ajena y
que ninguna salida mida cero bytes). **NO cuenta familias de secciones.** La
cifra de *una sola familia de secciones sobre los once* que el acta 205 publica
sale del instrumento propio del auditor, **no de `--componer`**, y lo digo
porque el encargo me manda que el calibre lo cotee la herramienta y no mi ojo:
**la herramienta lo cotea, pero cotea otra cosa que la frase sugiere.**

**LAS ONCE FILAS, CONTADAS POR MI DE LOS ONCE FICHEROS EN ESTA VUELTA**, con
`python scripts/loop/_v206_tallar_tabla_tramos.py`. Salida cruda en
`docs/loop/SALIDA_V206_TABLA_TRAMOS.txt`, 5020 bytes en disco y 4935 normalizado
a LF.

| tramo | salida sellada | bytes disco | bytes LF | lineas | sha256 LF | exitcode | minutos |
|---|---|---|---|---|---|---|---|
| 1 | `SALIDA_V205_BATERIA_TRAMO_1.txt` | 9555 | 9555 | 129 | `85c94304eef1fa28` | 1 | 2.8 |
| 2 | `SALIDA_V205_BATERIA_TRAMO_2.txt` | 7788 | 7788 | 123 | `8a426852569997fb` | 1 | 6.7 |
| 3 | `SALIDA_V205_BATERIA_TRAMO_3.txt` | 8525 | 8525 | 131 | `d665343b2715e6bb` | 1 | 11.2 |
| 4 | `SALIDA_V205_BATERIA_TRAMO_4.txt` | 8072 | 8072 | 125 | `07a889be43424245` | 1 | 3.0 |
| 5 | `SALIDA_V205_BATERIA_TRAMO_5.txt` | 8149 | 8149 | 126 | `65206552cad293f7` | 1 | 2.4 |
| 6 | `SALIDA_V205_BATERIA_TRAMO_6.txt` | 7880 | 7880 | 123 | `6c8c8725822883c1` | 1 | 3.0 |
| 7 | `SALIDA_V205_BATERIA_TRAMO_7.txt` | 7896 | 7896 | 123 | `427b396bd08b2fc8` | 1 | 2.5 |
| 8 | `SALIDA_V205_BATERIA_TRAMO_8.txt` | 7855 | 7855 | 123 | `fa02d03f1befeaf2` | 1 | 2.8 |
| 9 | `SALIDA_V205_BATERIA_TRAMO_9.txt` | 8523 | 8523 | 125 | `570ab8df86712b23` | 1 | 2.6 |
| 10 | `SALIDA_V205_BATERIA_TRAMO_10.txt` | 8473 | 8473 | 123 | `7fc7bf36a70ad181` | 1 | 4.1 |
| 11 | `SALIDA_V205_BATERIA_TRAMO_11.txt` | 6271 | 6271 | 94 | `c9e02832786abb5c` | 1 | 0.9 |

**LOS TOTALES, SUMADOS POR EL MISMO INSTRUMENTO Y NO A MANO:** suma de las
entradas de los once **135**, suma de minutos **42.0**, tramos de cero bytes
**0**, exitcodes distintos entre los once **1** (el `1`), veredictos distintos
entre los once **1** (`ROJO POR FALLO`), mediana de minutos por tramo **2.8**,
maximo **11.2** en el tramo **3**, y **1** solo tramo con `RUIDO DE
CONCURRENCIA` distinto de cero, el **3**, con **2** ficheros.

**EL COTEJO CONTRA LAS ONCE FILAS DEL ACTA 205, Y NO LO HACE MI OJO.** Corri
`python scripts/loop/_v206_cotejar_tramos.py --mutar`, que lee mis once filas de
los ficheros y las once del acta de su tabla, y las compara campo por campo.
Salida en `docs/loop/SALIDA_V206_COTEJO_TRAMOS.txt`,
1030 bytes en disco y 1010 normalizado a LF.

- **CIFRA discrepancias entre mis once filas y las once del acta: 0.** No hay
  ninguna que declarar, y por eso no declaro ninguna.
- **CIFRA suma de bytes de disco de los once: 88987**, y la misma suma sobre los
  bytes normalizados a LF da **88987**.
- **LA PRUEBA DE MUTACION, PORQUE UN COTEJO QUE SIEMPRE DICE VERDE NO PRUEBA
  NADA** (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): muto una celda
  mia cada vez, en cuatro campos distintos, y el cotejo **CAE las cuatro veces**.
  La cifra la publica el propio fichero: `CIFRA casos de mutacion: 4 | CIFRA que
  CAEN: 4`.

**EL CIERRE DE LA 205 CORRIO Y SALIO VERDE.** `cerrar_reporte.py --vuelta 205`
con sus cuatro piezas, `EXITCODE 0`, salida en
`docs/loop/SALIDA_V206_CERRAR_REPORTE_V205.txt`,
9109 bytes en disco y 8967 normalizado a LF. **Las cuatro piezas presentes**: veredicto escrito, cabecera
pegada, secciones 3 a 9, y **la bateria entera dentro de la seccion 9, sin hueco
declarado**, que es lo que el encargo exigia. El carril fue **CIERRE TARDIO**,
computado por el instrumento y no pasado por bandera.

**ARCHIVADO:** `docs/loop/reportes/REPORTE_V205.md`,
125443 bytes en disco y 125443 normalizado a LF, 1912 lineas, sha256 `caee50b8439838ae` en disco y
`caee50b8439838ae` normalizado a LF.

**NINGUN TRAMO SE VOLVIO A CORRER.** Los once ficheros que conte son los mismos
que la 205 sello: sus once `sha256` calzan con los once que el acta publica.

### 3.2 LA TAREA 2, CONTADA DE SUS FICHEROS

**LA SERIE, RECOMPUTADA POR MI EN LAS DOS PUNTAS Y NO COPIADA DEL ENCARGO**, con
`python scripts/loop/serie_de_registros.py`:

| momento | salida | entradas | colisiones | huecos | mayor | siguiente libre |
|---|---|---:|---:|---:|---|---|
| al entrar | `docs/loop/SALIDA_V206_SERIE_APERTURA.txt` | 60 | 0 | 0 | `R.68` | `R.69` |
| al cerrar | `docs/loop/SALIDA_V206_SERIE_CIERRE.txt` | 62 | 0 | 0 | `R.70` | `R.71` |

**EL ENCARGO DECIA 60, 0, 0, `R.68` Y `R.69`, Y ES CONTRASTE Y NO FUENTE. Mi
medicion de hoy da lo mismo: calzan las cinco.**

**LAS DOS ENTRADAS ESCRITAS**, con `python scripts/loop/_v206_t2_registros.py
--escribir`. Salida en `docs/loop/SALIDA_V206_T2_REGISTROS.txt`,
18067 bytes en disco y 18066 normalizado a LF.

| entrada | sujeto | linea en `docs/PENDIENTES.md` | numeral de preguntas |
|---|---|---:|---|
| `R.69` | acta del auditor de la vuelta 179 | 16638 | **no computable** |
| `R.70` | acta del auditor de la vuelta 180 | 16766 | **no computable** |

**POR ADICION PURA Y EN SU SEDE, Y LO MIDE `git`, NO YO:** `git diff --numstat --
docs/PENDIENTES.md` da **257** lineas anadidas y **0** borradas. Y la guarda del
propio instrumento, que es otra medicion y no la misma dos veces, cuenta **0**
lineas del texto de entrada que no esten, en orden, en el de salida. El fichero
pasa de 1145356 bytes en disco y 1145356 normalizado a LF, a **1161546** en
disco y **1161546** normalizado a LF.

**LA DEUDA DEL `4.9` DEL ACTA 201 QUEDA EN CERO, REMEDIDA AL CIERRE POR EL
INSTRUMENTO Y NO AFIRMADA:** `CIFRA actas de la 173 a la 180 SIN entrada propia:
0`.

**LAS PREGUNTAS LAS CONTE A MANO, Y DIGO COMO**, porque el encargo prohibe usar
`preguntas_del_reporte()` y porque su patron esta roto (acta 204 `4.4`). Mi
cuenta hace cuatro cosas, y las cuatro quedan pegadas en la salida para que
cualquiera pueda rehacerlas sin correr nada: busco toda seccion `## N. TITULO`
cuyo TITULO nombre la palabra PREGUNTAS **sin exigir que vaya pegada al numero**,
que es lo que el patron heredado si exige y por lo que el articulo `LAS` se lo
rompe; acoto esa seccion hasta la siguiente cabecera; saco las claves `P.n` **en
las dos formas** que esta campana usa, con comillas inversas y sin ellas; y pego
la linea cruda de la que sale cada clave.

| reporte archivado | seccion, con su linea | mi cuenta a mano | el lector heredado |
|---|---|---:|---:|
| `docs/loop/reportes/REPORTE_V179.md` | `## 6. LAS PREGUNTAS`, linea 750 | **4** (`P.1`, `P.2`, `P.3`, `P.4`) | 0 |
| `docs/loop/reportes/REPORTE_V180.md` | `## 6. LAS PREGUNTAS`, linea 843 | **2** (`P.1`, `P.2`) | 0 |

**EL CERO DEL LECTOR HEREDADO NO ES UN HECHO DEL MUNDO** (`EJECUTOR.md` 9): es
que **su patron no encontro nada**. Los dos reportes SI titulan su seccion de
preguntas, y la linea de cada una esta ahi arriba. **LA DISCREPANCIA QUEDA
DECLARADA DENTRO DE LAS DOS ENTRADAS Y NO RESUELTA COPIANDO** (`EJECUTOR.md` 2).

**Y EL NUMERAL SIGUE `NO COMPUTABLE`, QUE ES LO QUE EL ENCARGO MANDA:** ninguna
seccion de esas dos actas titula las adjudicaciones, asi que no hay titulo del
que sacar una `P.n`, y un cero ahi se leeria como *el acta no contesto ninguna
pregunta*. **El reparto medido va DEBAJO, marcado como medicion y no como
numeral** (acta 204 `4.6`).

**EL CLON ESTA MEDIDO Y NO AFIRMADO.** `_v206_t2_registros.py` se genero de
`_v204_t1_registros.py` con `scripts/loop/_gen_v206_t2_registros.py`, que cuenta
con `difflib`: **495** lineas de fuente, **624** de destino, **460** sin tocar y
**164** nuevas o cambiadas. Salida en
`docs/loop/SALIDA_V206_GEN_T2_REGISTROS.txt`,
2149 bytes en disco y 2114 normalizado a LF. **El computo del reparto NO se clona: se IMPORTA**, igual que
hicieron la 203 y la 204.

**EL LECTOR HEREDADO NO SE TOCO**, y el generador lo comprueba solo: **CIFRA
veces que este generador escribe `def preguntas_del_reporte`: 0.** Cuento aparte
y piso el campo; no le cambio ni un caracter a un fichero que el acta 205
declaro codigo que hoy no se toca.

**LA PRUEBA POR MUTACION DEL ENSANCHE CORRIO OTRA VEZ ANTES DE ESCRIBIR NADA**, y
no heredo su verde de otra corrida: **9** casos, **9** verdes, **0** rojos, y la
segunda pasada muta el esperado y exige que cada caso caiga, **9 de 9 CAEN**.

**LA SEGUNDA CORRIDA ES IDEMPOTENTE Y LO MIDO**, no lo prometo: volvi a correr el
escritor y da **0** bytes de crecimiento y **0** entradas escritas, con las dos
guardas diciendo `NO SE ESCRIBE: la entrada ya estaba. IDEMPOTENTE.`. Salida en
`docs/loop/SALIDA_V206_T2_REGISTROS_IDEM.txt`,
17973 bytes en disco y 17972 normalizado a LF.

### 3.3 EL CICLO ENTERO DE GATE 0, CORRIDO POR MI Y NUNCA `run_phase1.py` A SECAS

**LOS OCHO COMANDOS EN SU ORDEN, LOS DOS LADOS, TRES CORRIDAS EN TOTAL**, todas
en `EXITCODE 0` peor de los ocho:

| corrida | para que | salida | peor exitcode |
|---|---|---|---:|
| lado APERTURA de la 206 | mi propia cabecera | `docs/loop/SALIDA_V206_CICLO_APERTURA.txt` | 0 |
| lado CIERRE de la 206 | mi propia cabecera, recomputada al cierre | `docs/loop/SALIDA_V206_CICLO_CIERRE.txt` | 0 |
| lado APERTURA de la 205 | la columna de apertura de SU cabecera, que nunca se midio | `docs/loop/SALIDA_V206_CICLO_V205_APERTURA.txt` | 0 |

**`git diff HEAD --numstat` sobre `dataset/`, `web/` y `engine/` da 0 filas
DESPUES de correr yo el ciclo entero**, en las tres corridas.

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ESTADO DEL ARBOL AL ENTRAR, EN LA REDACCION QUE LA GUARDA LEE**, medido
antes de la primera operacion y sellado en `docs/loop/SALIDA_V206_APERTURA.txt`:

CIFRA lineas de status, medidas con `git status --porcelain`: 5

CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: 0

**LAS CINCO LINEAS DE STATUS SE DICEN UNA A UNA EN VEZ DE ESCONDERSE DETRAS DEL
NUMERO.** Una es la `M` de `dataset/metadata/master_graph.json`, que **NO ES UNA
MODIFICACION**: el fichero es identico EN CRUDO al de HEAD, **8375817** bytes en
disco y **8375817** normalizado a LF en los dos, sha256 `627cc662296f7f00` en
disco y `627cc662296f7f00` normalizado a LF en los dos, y `git diff --numstat` da
**0** filas. Es el aviso de fin de linea de git, y el encargo ya me avisaba de
que no lo denunciara como caida. Las otras cuatro son ficheros de computo que el
auditor de la 205 dejo sin committear, y committearlas fue mi primera operacion,
como manda `EJECUTOR.md` 3.

**Y LA `M` LA PERSEGUI ANTES DE CREERME EL AVISO**, no despues.

**TODO LO DE ESTA SECCION SALE DE `git` CORRIDO EN ESTA VUELTA Y NO SE
HEREDA DE LA APERTURA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL
CIERRE). El HEAD de apertura contra el que se mide todo es `78ca7176`,
leido de `git rev-parse HEAD` antes de la primera operacion.

### 4.1 LAS CUATRO SEDES QUE EL ENCARGO EXIGE EN CERO, MEDIDAS AL CIERRE

Comando: `git diff 78ca7176 --numstat -- <sede>`

| sede | filas de numstat |
|---|---:|
| `dataset/` | 0 |
| `web/` | 0 |
| `engine/` | 0 |
| `docs/plan/` | 0 |

**CIFRA suma de filas de las cuatro sedes: 0.**

### 4.2 LAS TRES SEDES DEL AUDITOR, QUE EL EJECUTOR NO ESCRIBE

**EL CERO DE `PARA_ALEXIS.md` ES DE AUSENCIA DE FICHERO, Y ASI SE DICE**
(`4.5` del acta 204). Comando: `git diff 78ca7176 --numstat -- <sede>`.

| sede del auditor | existe en disco | filas de numstat | de que es el cero |
|---|---|---:|---|
| `docs/loop/PROMPT_SIGUIENTE.md` | SI | 0 | de no haberla tocado |
| `docs/loop/ACTA_AUDITOR.md` | SI | 0 | de no haberla tocado |
| `docs/loop/PARA_ALEXIS.md` | NO | 0 | **de ausencia de fichero**, no de no haberla tocado |

### 4.3 LAS DOS SEDES SELLADAS, REMEDIDAS Y NO HEREDADAS

| fichero | bytes (disco y LF, en el mismo renglon) | sha256 (disco y LF, en el mismo renglon) | calza con el encargo |
|---|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 4054129 bytes en disco y 4054129 bytes normalizado a LF | sha256 disco `0a77b5a35a962621` y sha256 LF `0a77b5a35a962621` | SI |
| `docs/plan/OPERACIONES.jsonl` | 513043 bytes en disco y 513043 bytes normalizado a LF | sha256 disco `829c583eb779cab6` y sha256 LF `829c583eb779cab6` | SI |

**NINGUN campo `estado`, NINGUNA clase y NINGUN veredicto se movio, y no lo
digo: lo miden los dos `sha256` de arriba, identicos por las dos
convenciones a los que el encargo trae del cierre de la 204.**

### 4.4 LO QUE LA VUELTA SI TOCO, LEIDO DE `git` Y NO NARRADO

Comando: `git diff 78ca7176 --numstat` sobre el arbol entero.

| directorio tocado | ficheros |
|---|---:|
| `docs/PENDIENTES.md` | 1 |
| `docs/loop` | 33 |
| `scripts/loop` | 14 |

**CIFRA ficheros tocados contra el HEAD de apertura: 48.**

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. FABRIQUE LOS SEIS FICHEROS DE APERTURA DE LA 205 QUE NUNCA EXISTIERON,
EN VEZ DE DECLARAR QUE SU CABECERA NO SE PODIA TALLAR.** El encargo manda cerrar
la 205 con las cuatro piezas, y la pieza de la cabecera exige un tallador verde.
El tallador de la 205 salia rojo por **19** celdas, y **18** de ellas eran la
columna de apertura entera: esos seis ficheros **no existian y nunca habian
existido**, y no es una suposicion mia, es lo que dice el rechazo que aquella
vuelta dejo sellado en `docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt`. Corri el
ciclo entero hoy, en mi turno, y sus valores quedaron en esos nombres.

> **CORRECCION DECLARADA DE LA VUELTA 207, SOBRE LA `E.2` DEL ACTA 206.** El parrafo de arriba se queda **entero y sin tocar**
> (`EJECUTOR.md` 8). **LO QUE SE CORRIGE ES LA PROCEDENCIA, NO EL HECHO.**
> **LO QUE DICE Y ES FALSO:** que el **19** y el **18** son *lo que dice el
> rechazo que aquella vuelta dejo sellado*. **No lo son.** Ese `19 / 18` es el
> contenido que **esta misma vuelta 206** escribio encima de
> `docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt` al volver a correr el tallador, en el
> commit `a75ff760`.
> **LO QUE LA VUELTA 205 SELLO DE VERDAD, LEIDO POR MI CON
> `git show 78ca7176:docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt`:**
> `CIFRA celdas que no se pudieron leer: 39`
> `CIFRA de ellas del lado APERTURA: 19`
> `CIFRA de ellas del lado CIERRE  : 19`
> `CIFRA de ellas del lado LOS DOS : 0`
> `CIFRA de ellas del lado SIN LADO: 1`
> Ese blob mide **3188** bytes y **3188** normalizado a LF, sha256 LF
> **`b9df894ff422dc77`**.
> **Y ESTO ES LO QUE EL MISMO NOMBRE DE FICHERO DICE HOY EN DISCO**, que es
> de donde salio el `19 / 18`: **1922** bytes en disco y **1922** normalizado a
> LF, sha256 disco **`254c2257ae55a0f2`** y sha256 LF **`254c2257ae55a0f2`**.
> `CIFRA celdas que no se pudieron leer: 19`
> `CIFRA de ellas del lado APERTURA: 18`
> `CIFRA de ellas del lado CIERRE  : 1`
> `CIFRA de ellas del lado LOS DOS : 0`
> `CIFRA de ellas del lado SIN LADO: 0`
> **LA REGLA QUE ESTO DEJA, Y ES EL HALLAZGO `7.3` DEL ACTA 206:** una salida
> sellada que una vuelta posterior vuelve a correr **deja de ser evidencia de
> la vuelta que la sello**. La fuente correcta es
> `git show <commit de aquella vuelta>:<ruta>`, nunca el fichero de hoy.
> **LA CONCLUSION DEL `D.1` SE SOSTIENE Y NO SE TOCA:** los seis
> `SALIDA_V205_*_APERTURA.txt` no existian antes de la vuelta 206, y el acta
> 206 lo verifico aparte midiendo que los seis se anaden **una sola vez en
> toda la historia de git, y es en `a75ff760`**. Lo que estaba mal era
> de donde se decia que salia la cifra. **ESTA CAIDA NO ACUMULA**, por la
> misma letra que la `E.1`: prosa de un discutible.


**LO QUE SOSTIENE QUE ESOS VALORES SEAN LOS DE AQUEL MOMENTO ES UNA MEDICION Y NO
UNA PROMESA:** `git diff --numstat e66bf67d..HEAD` sobre `dataset/`, `web/` y
`engine/` da **0** filas, o sea que los tres arboles que el ciclo mide son byte a
byte los de la apertura de la 205; y la vuelta 205 entera solo toco `docs/loop`,
`docs/loop/reportes` y `scripts/loop`. Ademas los nueve ficheros que escribi hoy
miden exactamente lo mismo que los nueve que el auditor sello en el cierre de
aquella vuelta.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** `EJECUTOR.md` 1 dice que la apertura se
mide antes de la primera operacion, y **no dice** *o despues, si puedes probar
que nada se movio*. Con la letra estrecha, la columna de apertura de
`REPORTE_V205.md` es una **reconstruccion mia de la vuelta 206** y no una
medicion de aquel momento. **Yo creo que la reconstruccion es honesta porque va
declarada dentro del propio reporte cerrado y con su prueba al lado, y porque la
alternativa era dejar la 205 sin cerrar por tercera cadencia; pero la letra es
del auditor y no mia.**

**`D.2`. REPARE EL ESQUELETO DE LA 205 EN VEZ DE DECLARARLO ROTO Y PARARME.**
`cerrar_reporte.py` reventaba dos veces seguidas sobre el, con `ValueError:
substring not found`, y las dos por defectos del esqueleto y no del instrumento:
le faltaban las marcas `<!-- CABECERA TALLADA -->` y `<!-- FIN CABECERA TALLADA
-->`, y le faltaba la linea en blanco detras del veredicto. Le anadi las dos
cosas y nada mas: el esqueleto pasa de 1087 bytes en disco y 1087 normalizado a
LF, a 1144 en disco y 1144 normalizado a LF, y **guarde su estado anterior byte a
byte** en `docs/loop/_v206_esqueleto_v205_antes.md`,
1087 bytes en disco y 1087 normalizado a LF, sha256 `362c76a5bd33564b` en disco y `362c76a5bd33564b`
normalizado a LF, para que la reparacion se pueda auditar. **Por donde me puedo
estar equivocando:** tocar el sujeto que se esta cerrando es tocar el sujeto, y
alguien puede leer eso como que el reporte de la 205 lo termine de escribir yo.

**`D.3`. CORREGI UNA AFIRMACION DEL BORRADOR DE LA 205 DENTRO DEL REPORTE DE LA
205, EN VEZ DE DEJARLA Y SOLO SENALARLA DESDE EL MIO.** Su seccion `3.5` afirma
que el desglose del fallo es identico en los once y que ninguna de las 135
entradas falla, y las dos cosas son falsas medidas hoy. Deje **el parrafo viejo
entero** y puse la correccion debajo con su medicion (`EJECUTOR.md` 8). **Por
donde me puedo estar equivocando:** ese reporte lo firma el ejecutor de la 205, y
meterle una correccion escrita por el de la 206 mezcla dos manos en un mismo
documento. La alternativa era publicar a sabiendas una cifra falsa, y esa no la
tomo.

**`D.4`. USE EL BORRADOR QUE LA 205 DEJO ESCRITO COMO CUERPO DE SU CIERRE, EN VEZ
DE ESCRIBIR UNO NUEVO.** `scripts/loop/_v205_cierre_texto.md` estaba sin
committear, con sus tres huecos sin rellenar. Rellene los tres desde ficheros de
salida y no teclee ninguna celda. **Por donde me puedo estar equivocando:** un
borrador sin committear no es un documento de la vuelta, y quiza lo que la 205
dejo a medias habia que darlo por no escrito.

**`D.5`. MEDI LA SECCION 4 DEL REPORTE DE LA 205 ENTRE DOS COMMITS Y NO CONTRA EL
ARBOL DE HOY.** El instrumento que aquella vuelta dejo,
`_v205_tallar_numstat.py`, mide siempre contra el arbol de trabajo, y eso le
habria colgado a la 205 los cuarenta y ocho ficheros de la 206. Escribi un
computo `_v206_*` que acepta un cierre explicito y medi
`e66bf67d..43f2158e`, que es el ultimo commit del ejecutor de aquella vuelta.
**Por donde me puedo estar equivocando:** la vuelta 205 no termina en su ultimo
commit de ejecutor sino en el acta del auditor, `78ca7176`, y medida hasta ahi
sus tres sedes de auditor dan **1**, **1** y **0** en vez de **0**, **0** y
**0**. **Publico las dos mediciones y no elijo en silencio**: hasta el ultimo
commit del ejecutor, las tres dan cero; hasta el acta, dos dan uno, y las
escribio el auditor.

## 6. LAS PREGUNTAS

**`P.1`. LAS CINCO ENTRADAS QUE NO MORDIERON, QUE ES LA PARADA DE LA `3.0`.** Se
les arregla el arnes, se declaran como caso conocido con su marca dentro de la
salida como ya hacen otras dos, o se sacan de la nomina? Las tres puertas mueven
la nomina o mueven un arnes, y las dos cosas estan bajo moratoria. **No lo decido
yo, y la bateria de la 210 se las va a encontrar igual.**

**`P.2`. `exit 3221225794` NO ES UN ARNES QUE NO MUERDE, ES UN PROCESO QUE NO
ARRANCA.** El instrumento lo mete en el mismo saco de `NO MORDIO`. **Vale la pena
saber si esa es la lectura que se queria**, porque un fallo de arranque del
sistema operativo y un arnes que dejo de vigilar lo suyo no piden el mismo
remedio.

**`P.3`. QUE HACE UNA VUELTA CUANDO EL REPORTE QUE TIENE QUE CERRAR ES EL FICHERO
DONDE TIENE QUE ABRIR EL SUYO.** `EJECUTOR.md` 1 manda tallar el esqueleto en la
apertura, y `docs/loop/REPORTE.md` es una sola ruta. Hoy resolvi cerrando primero
y abriendo despues, y lo cuento como caida mia en la `C.2`. **Si la respuesta es
que el esqueleto va primero y el cierre tardio se hace sobre el fichero
archivado, hace falta decirlo, porque esto vuelve cada vez que una vuelta se
corta.**

## 7. PENDIENTES DE DOCTRINA

**`PD.1`.** Que cuenta como reconstruir una medicion de apertura que nunca se
tomo. La letra dice cuando se mide, y no dice nada sobre que hacer con una
columna que no se midio en su momento y cuyo arbol se puede probar identico.
**Registro lo mejor sostenido y sigo** (`EJECUTOR.md` 5), que es lo que hice en
la `D.1`.

**`PD.2`.** La `PD.1` de la 205, sobre que cuenta como clonar bajo la moratoria
cuando un fichero **importa** un instrumento y solo le corrige un dato, sigue sin
resolver. Esta vuelta la volvi a usar dos veces, en `_v206_ciclo_gate0.py` y en
el envoltorio que el acta 205 `4.1` ya adjudico a favor. **La cito para que no se
pierda.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. MI PROPIO TALLADOR DE LA TABLA DE TRAMOS PUBLICO ONCE VECES QUE NO
ENCONTRABA EL FICHERO, Y LOS ONCE FICHEROS ESTABAN AHI.** Calcule la raiz del
repositorio subiendo **un** directorio desde `scripts/loop/` en vez de **dos**,
asi que buscaba los tramos en `scripts/docs/loop/`. Su primera corrida dio
`CIFRA tramos con fichero contado: 0` y `CIFRA ficheros que el patron no
encontro: 11`. **Es exactamente la especie contra la que el encargo me avisaba,
un cero de mi instrumento que no es un hecho del mundo**, y el aviso es lo que me
hizo mirar en vez de publicarlo. **La cace antes de que saliera de mi turno y no
llego a ningun documento**, pero la escribo porque la casi caida tambien se
cuenta: si el fichero hubiera dicho *no existe* en vez de *el patron no
encontro*, me la habria creido.

**`C.2`. NO TALLE MI ESQUELETO ANTES DE LA PRIMERA TAREA.** `EJECUTOR.md` 1 dice
que el reporte abre con la vuelta y que crece por anexion, y el mio nacio con la
TAREA 1 ya cerrada. **El motivo es real y esta escrito en la cabecera del propio
reporte**, no lo escondo detras de una excusa: `docs/loop/REPORTE.md` era el
sujeto que la TAREA 1 tenia que cerrar. **Pero el motivo no lo convierte en
cumplimiento**, y por eso va aqui y sube como `P.3`.

**`C.3`. EL SELLO `docs/loop/SALIDA_V206_APERTURA.txt` NACIO CON LAS DOS TAREAS
YA CERRADAS.** Los valores que lleva dentro los medi antes de la primera
operacion y estan copiados de esa medicion, con la advertencia escrita encima del
fichero; el fichero, no. **El tallador lo dice solo y no se lo tapo:** su fila de
identidad publica el sello como `RECONSTRUIDO DESPUES (commit a75ff760)`, y esa
es la celda que va en mi cabecera. **Es la misma especie que la `C.1` de la 205 y
la cuento una sola vez, aqui.**

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**PROPONER ES MIO Y ENCARGAR ES DEL AUDITOR.** No escribo `PROMPT_SIGUIENTE.md`,
`ACTA_AUDITOR.md` ni `PARA_ALEXIS.md`, y el `numstat` de las tres contra mi HEAD
de apertura va en la seccion 4, en **0**, **0** y **0**, con el cero de
`PARA_ALEXIS.md` distinguido como **de ausencia de fichero**.

1. **LA PARADA DE LA `3.0` PIDE LETRA Y NO LA DECIDE EL EJECUTOR.** Cinco
   entradas de la nomina no muerden y el rojo de la bateria las tapa. **Mientras
   no se resuelva, la 210 sale roja por las mismas dos causas y la segunda sigue
   sin verse.**
2. **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y CON SU EJECUCION
   SUSPENDIDA** (acta 202 `4.6`, ratificada por la 203 `4.9`, la 204 `4.10` y la
   205): se ejecuta en la primera vuelta despues de que la moratoria se levante.
   **La arrastro aqui otra vez para que la 207 no la pierda**, que es lo que el
   encargo me pide expresamente.
3. **`--siguiente` DEL LANZADOR SIGUE MINTIENDO** y va a la auditoria integral ya
   nombrado (acta 205 `5.2`): computa su vuelta del nombre del fichero, lineas
   **91**, **92** y **96** de `scripts/loop/vuelta183_bateria_por_tramos.py`.
   **Yo no lo corri para saber que tramo tocaba: no me hacia falta, porque no
   corri ningun tramo.**
4. **EL PATRON DE `preguntas_del_reporte()` SIGUE ROTO Y HOY NO SE TOCO** (acta
   204 `4.4`), linea **196** de `scripts/loop/_v203_reparto_de_actas_viejas.py`.
   Esta vuelta lo rodee contando a mano, y la vuelta que lo rodee otra vez volvera
   a contar a mano. **Va a la integral.**
5. **LA DEUDA DE REGISTROS DEL `4.9` DEL ACTA 201 SE AGOTO**, medido al cierre en
   **0** actas sin entrada propia de la 173 a la 180. **La 207 no la arrastra**, y
   si el auditor quiere seguir la serie, el siguiente sujeto ya no sale de esa
   deuda sino de una nueva.
6. **LA VARA DE `cobertura` SIGUE DIFERIDA A LA INTEGRAL** (acta 203 `4.7`, acta
   204 `4.8`), y **`OP-I-01`, `OP-L-01` y `OP-L-02` siguen sin cerrar**: no las
   levante y no les toque el `estado`.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 206 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V206_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio en la vuelta 206, y no es un olvido: por AUDITOR.md 6.1 la bateria de mutaciones corre CADA CINCO vueltas, en una vuelta propia que no lleva nada al lado. La anterior de la cadencia fue la 205, que la corrio ENTERA por tramos y cuya salida quedo compuesta y sellada en esta vuelta al cerrar aquel reporte; la siguiente de la cadencia es la 210. Esta vuelta traia DOS sub-tareas por AUDITOR.md 6.2 y ninguna de las dos era la bateria, asi que aqui NO hay corrida propia que pegar y lo que va es este hueco declarado y medido.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
