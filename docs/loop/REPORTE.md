# REPORTE DE LA VUELTA 150

**Rama `pasada-unica`. Fase III, EJECUCION, modo continuo, REGIMEN COMPLETO.** Corte de
todas las cifras de esta pagina: **2 sep 2026**, salvo donde se diga otra cosa.

**LA VUELTA EN UNA LINEA: `OP-C-05` SE ENCIENDE POR SU MITAD EJECUTABLE Y SU OTRA MITAD SE
TRAE COMO PARADA MEDIDA; LOS REGISTROS DEL ACTA 149 QUEDAN ESCRITOS POR ADICION CON UNA
DISCREPANCIA DECLARADA CONTRA EL PROPIO ACTA; LA RELECTURA AL DOBLE ENCUENTRA TREINTA
FICHAS CONGELADAS EN SILENCIO; LAS OCHO FILAS DE LA TABLA POR FASE QUEDAN RECORRIDAS, Y
CINCO DE MIS PROPIAS VARAS ESTABAN MAL Y LO DIGO CON LAS DOS CORRIDAS DELANTE; Y LA TRAMPA
DEL CICLO DE GATE 0 YA MUERDE, PORQUE ME MORDIO A MI EN ESTA MISMA VUELTA.**

**LAS CIFRAS VIVEN DENTRO DE LOS BLOQUES PEGADOS**, cada uno con el fichero del que sale
escrito debajo, y la prosa las glosa sin repetirlas sueltas.

## 0. LA CABECERA, TALLADA Y PEGADA ENTERA

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 150 --fase04` deja su salida en
`SALIDA_V150_TALLADOR_CABECERA.txt` con **VERDE EXIT 0**, y su tabla se pega entera aqui
abajo, sin tocar una celda.

<!-- CABECERA TALLADA -->
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `fe98cf97` (asunto real leido de git log: 'ACTA DE LA VUELTA 149 DEL AUDITOR: LA 148 NO PUBLICA UNA SOLA CIFRA FALSA, LA FASE 07 QUEDA CERRADA, Y NO PARO PORQUE OP-C-05 ESTA DESBLOQUEADA Y NADIE LA NOMBRO.'), HEAD real de apertura `fe98cf97` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `0821eaa3` (leido de `SALIDA_V150_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
<!-- FIN CABECERA TALLADA -->

**HASH FINAL de la vuelta**, leido de `SALIDA_V150_HEAD_CIERRE.txt`, sellado TRAS la
ultima operacion:

```
0821eaa3327a08bb6d23a8d84f2a8b05690db91a
```

**LA APERTURA, SELLADA ANTES DE LA PRIMERA OPERACION.**
`python scripts/loop/verificar_apertura_sellada.py --vuelta 150` sale **VERDE**: los
**diez** ficheros `SALIDA_V150_*_APERTURA.txt` nacieron todos en `1f423cbc`, hijo directo
de `fe98cf97`, el acta de la 149. Esta vuelta no reanuda tras parada, asi que el corredor
que la 148 tuvo que abrir no aplica y la guarda pasa por su vara vieja.

<!-- COMMITS TALLADOS -->

**LOS COMMITS DE LA VUELTA, TALLADOS Y NO PEGADOS, y el motivo es una guarda de la casa.**
Se tallan con `git log fe98cf97..HEAD --pretty=format:"  %h %s" | cut -c1-152` y quedan
enteros en `SALIDA_V150_COMMITS_TALLADOS.txt`, **siete lineas, una por commit**, de la
apertura al cierre. **No se pegan aqui**, y no es pereza: la guarda de citas del
reporte lee cada frase como prosa del ejecutor, y el asunto de mi propio commit
`38e26678` trae una de las palabras de su vocabulario, que exige respaldo de un fichero
**en su misma frase o en la anterior**. Un asunto de commit ya escrito no admite ninguna de las
dos, asi que pegarlo obligaria a aflojar la guarda o a reescribir historia empujada.
**Prefiero citar el fichero.** Va marcado como discutible.

<!-- FIN COMMITS TALLADOS -->

**EL ORDEN NO ES EL DEL ENCARGO Y SE VE EN LA LISTA: la TAREA 2 va antes que la 1**, porque
el encargo lo manda con esas palabras (*"ES BLOQUEANTE. VA ANTES QUE TODO LO DEMAS DEL
TRABAJO"*). El commit de la 2 es `76a18a90` y el de la 1 es `fb3c0c75`.

---

## 1. TAREA 2, `OP-C-05`: MEDIA GUARDA ENCENDIDA Y MEDIA PARADA TRAIDA

**LO QUE ENTRA EN GATE 0.** *"Ninguna lista de aristas de un nodo VIVO tiene dos entradas
que RESUELVAN al mismo destino"*, cableada en `scripts/run_phase1.py` al lado de las dos de
`OP-C-04`, no en un script suelto, como la 2.a pide. Gate 0 pasa de 24 a **25
comprobaciones**.

**LAS SIETE VERIFICACIONES, LEIDAS DE LA FICHA EN LA CORRIDA Y CONTESTADAS EN SU ORDEN.**
Fichero de salida: `SALIDA_V150_2C_SIETE_VERIFICACIONES.txt`, y esta tabla esta contada de
ese fichero.

| # | que pide la ficha | veredicto |
|---:|---|---|
| 1 | CASO POSITIVO, `[destino, alias_de_destino]` a mano y la guarda falla nombrando nodo, campo y destino | **CONTESTADA, EN VERDE** |
| 2 | caso negativo, el grafo saneado por `OP-S-12` pasa en verde | **CONTESTADA, EN VERDE** |
| 3 | CASO DE BORDE, el mismo destino en previos y siguientes NO debe fallar | **CONTESTADA, EN VERDE** |
| 4 | la guarda RESUELVE, no compara literal | **CONTESTADA, EN VERDE** |
| 5 | CASO POSITIVO DE LA LISTA BLANCA | **PARADA** |
| 6 | CASO NEGATIVO DE LA LISTA BLANCA, las cuatro aristas de `OP-E-05` | **NO CONTESTABLE HOY** |
| 7 | cada entrada de la lista blanca cita su lectura | **CONTESTADA PARA LAS DOS ESCRITAS; ABIERTA para el resto** |

**LA 1 EN DOS SEDES.** En copia en memoria (`SALIDA_V150_2D_SIMULACION_OP_C_05.txt`) la
guarda saca **una** linea y los tres nombres estan dentro. Y en **GATE 0 REAL**, sobre
arbol de trabajo nunca commiteado y restaurado acto seguido
(`SALIDA_V150_2C_CASO_POSITIVO_GATE0.txt`): `[FALLO]` con la linea entera y **`GATE 0:
FALLIDO`, EXITCODE 1**. La sede es la adjudicada para `OP-C-04` el 14 ago 2026.

**LA 4 CON SU CIFRA, Y ES LA QUE PRUEBA QUE LA GUARDA GUARDA.** Se corre sobre
`a34328b2~1`, el grafo de justo ANTES de `OP-S-12`, que es el unico sitio donde queda algo
que cazar. La guarda **literales da 0 grupos**, leido de la linea `CIFRA` de
`SALIDA_V150_2C_SIETE_VERIFICACIONES.txt`. La que **resolviendo da 888 grupos**, leido de
la otra linea `CIFRA` de `SALIDA_V150_2C_SIETE_VERIFICACIONES.txt`. **Cero contra 888**, y
esa es la diferencia entre una guarda que guarda y una que no.

**LA PARADA, Y NO LA RESUELVO YO.** La adjudicacion de la ficha dice *"la guarda falla ante
cualquier arista bidireccional SALVO las de la lista blanca"*, y la lista blanca tiene
**DOS** entradas. Medido con instrumento propio (`scripts/loop/vuelta150_medir_opc05.py`):

Bidireccionales vivos en HEAD: **153 pares**, contado de la linea `CIFRA` que
`SALIDA_V150_2C_SIETE_VERIFICACIONES.txt` imprime con esa etiqueta.

Bidireccionales vivos en mergebase: **83 pares**, contado de la linea `CIFRA` que
`SALIDA_V150_2C_SIETE_VERIFICACIONES.txt` imprime con esa etiqueta.

Entradas escritas en la lista blanca: **dos**. De las cuatro aristas de `OP-E-05`, existe
**una**.

Encenderla pondria Gate 0 en rojo 153 veces sobre el grafo saneado, y eso choca de frente
con la **verificacion 2 de su propia ficha**. Meterlos todos en la lista blanca choca con
su otra letra, *"cada entrada CITA SU LECTURA"*, y en
`SALIDA_V150_2C_SIETE_VERIFICACIONES.txt` no hay ni una lectura detras de ellos.
**Y los 83 de antes de la campana dicen que no es un estado que la pasada creo: la guarda,
como esta adjudicada, no puede estar verde ni sobre el grafo original.** La verificacion 6
tampoco es contestable, y sale del mismo fichero: **`OP-E-05` sigue en `LISTA` y de sus
cuatro aristas existe UNA.**

**EL `estado` DE `OP-C-05` NO SE MUEVE**, y esa es la 2.e aplicada: sigue en `LISTA`.

**LAS GUARDAS DE LA 2.d, LAS CUATRO.** Simulacion previa sobre copia en memoria con
`dataset/` comprobado **identico antes y despues por el propio arnes** (sha256 del
`master_graph` y del directorio de nodos); **caso rojo por mutacion sobre variable
computada**, tres asserts mutados y **los tres CAEN**
(`SALIDA_V150_2D_SIMULACION_OP_C_05.txt`); ciclo entero de Gate 0 en su orden con el
`numstat` sin una fila; y motor, vitest y `tsc` en verde, con sus cuatro celdas en la
cabecera tallada de la seccion 0.

---

## 2. TAREA 1, LOS REGISTROS DEL ACTA 149

**1.a, `R.29`.** Escrito por adicion al final de `docs/plan/CORRECCIONES_A_APLICAR.md`, que
es el fichero que el encargo nombra: los nueve discutibles a favor con reserva en el 2, el
4 y el 5; las dos preguntas contestadas; la fase 07 dada por cerrada en la 3.12; las dos
adjudicaciones de orden; y las caidas 4.1 a 4.6.b con nombre. **`R.20` a `R.28` viven en
`docs/PENDIENTES.md`**, medido hoy, y ahi queda una **remision de una linea**, no una
copia.

**1.b, la CORRECCION 30, con el rastro reproducido y no copiado.** Instrumento propio:
`scripts/loop/vuelta150_1b_rastro_del_1056.py`; salida `SALIDA_V150_1B_RASTRO_1056.txt`, y
esta tabla esta contada de ese fichero.

| lo medido | cifra de hoy | lo que dice el acta 149 |
|---|---:|---:|
| versiones de `ARISTAS_DUPLICADAS.jsonl` en git | **30** | 30 |
| primera version `af467eb1`: grupos / nodos / sobran | **1.015 / 802 / 1.056** | 1.015 / 802 / 1.056 |
| version de HEAD `d6341ebe`: grupos / nodos / sobran | **898 / 711 / 935** | 898 / 711 / 935 |
| de esas 935, sobre nodos hoy DEPRECADOS | **10** | 10 |
| de esas 935, sobre nodos ausentes del grafo (`SALIDA_V150_1B_RASTRO_1056.txt`) | **0** | (no la separaba) |
| de esas 935, sobre nodos VIVOS | **925** | 925 |

**Las seis reproducen al digito.** La cifra vieja queda intacta con su corte (**11 ago
2026**) y su universo (**3.521 vivos**), y la verificacion 4 no esta contradicha: esta
vencida.

**Y UNA DISCREPANCIA CONTRA EL ACTA, DECLARADA EN VEZ DE RESUELTA COPIANDO (`EJECUTOR.md`
2).** El acta dice que la bajada de 1.056 a 935 es **monotona** a lo largo de las treinta
versiones. **Mi medicion dice que NO lo es**, por un escalon de una unidad: `706397c7` da
**995** y su descendiente `3ffc2091` da **996**, con `git merge-base --is-ancestor
706397c7 3ffc2091` en verde, o sea que el orden es el cronologico y no un artefacto del
listado. Las otras **28** transiciones bajan o se quedan igual. **La direccion general del
acta es correcta y la palabra no lo es**, y ninguna de las cifras que sostienen la
adjudicacion 3.8 depende de ella.

**1.c, el `estado` de `OP-S-12`, y DESPUES de la 1.b.** Pasa de `LISTA` a `HECHA`.
**`05_SANEO` queda 10 de 10 en `HECHA`.** El esquema no se toca: **71 fichas, un solo
esquema, 18 claves** antes y despues, comprobado por el propio registrador, y el diff del
jsonl toca **una sola linea**.

**1.d, el indice semantico**, a `docs/PENDIENTES.md` con **mi** medicion de hoy
(`SALIDA_V150_1D_INDICE_SEMANTICO.txt`): **3.521 ids**, **3.169 vivos**, **18 vivos SIN
VECTOR nombrados uno a uno**, **370 no vivos que son 370 DEPRECADOS y CERO FANTASMAS**, y
el cuadre por los dos lados (3.521 = 3.151 + 370; 3.169 = 3.151 + 18). Con la **linea 166**
de `build_semantic_index_voyage.py` citada: `main()` reconstruye la lista `ids` desde cero,
asi que una corrida arregla los 18 y los 370 en la misma pasada.

---

## 3. TAREA 3, LA RELECTURA AL DOBLE DEL EXPEDIENTE

**3.b, EL CRITERIO PRIMERO**, escrito entero en el docstring de
`scripts/loop/vuelta150_3_relectura_expediente.py`, con la fuente de cada pierna:

  - **P1, vara de GRAFO**: `tallar_estado_de_fase.py` dice DESTINO CUMPLIDO (acta 139,
    TAREA 2.a). **Se invoca, no se reimplementa.**
  - **P2, vara de CODIGO, MITAD DE PRESENCIA**: el `id_op` vive hoy en `scripts/`,
    `engine/` o `web/lib/`, con `scripts/loop/` FUERA (adjudicacion 3.9 del acta 144). **Y
    se dice que es media**: que muerda se prueba por mutacion una a una.
  - **P3, HUELLA EN GIT**: un commit que NOMBRA el `id_op` **y ademas toca** `dataset/`,
    `scripts/`, `engine/` o `web/`. Esa segunda condicion separa una ejecucion de un
    registro.

Las dos ultimas con **frontera de palabra**, porque `OP-M-01` es prefijo literal de
`OP-M-01-FUSION`. **Corri las dos versiones y los totales salen identicos**, asi que
ninguna fila de la tabla dependia del falso positivo.

**3.a, LA TABLA CORTA.** Contada de `SALIDA_V150_3_RELECTURA_EXPEDIENTE.txt`:

| lo contado | cifra |
|---|---:|
| fichas | **71** |
| **no calzan** | **58** |
| calzan (no se imprimen) | **13** |
| de las que no calzan, CONGELADAS **DECLARADAS** | **28** |
| de las que no calzan, CONGELADAS **EN SILENCIO** | **30** |
| `HECHA` sin ninguna prueba de ejecucion | **0** |
| cobertura: P1 con destino cumplido / P2 en codigo vivo / P3 con huella | **19 / 20 / 67** |

**Ninguna `HECHA` afirma mas que el repo**, y esa es la mitad buena. La otra mitad es que
**58 de 71 tienen `estado` `LISTA` con ejecucion medida**, y **30 de ellas no dicen ni una
palabra de su propio `estado`**. La caida 4.2 del acta 149 era una; **medida sobre el
catalogo entero, es una especie de treinta ejemplares.** La nomina de las 58, fila a fila y
con su motivo, esta en el fichero de salida.

**3.c.** Por el criterio estricto (`LISTA` con TODAS sus `depende_de` en `HECHA`) sale
**UNA y es `OP-C-05`**, que ya estaba nombrada: **ninguna operacion desbloqueada nueva**. Y
la otra cara, que traigo y **no toco**, contada del mismo
`SALIDA_V150_3_RELECTURA_EXPEDIENTE.txt`: las unicas **DOS** fichas en `LISTA` sin ninguna
de las tres pruebas son **`OP-V-01`** (`08_VERIFICACION`, `MESA`, con `depende_de` vacio,
que es el sujeto de la TAREA 4) y **`OP-L-01`** (`09_LECTURAS_DIRIGIDAS`, `MESA`, tambien
con `depende_de` vacio).

---

## 4. TAREA 4, LAS OCHO FILAS DE LA TABLA POR FASE

**Y EMPIEZO POR LO QUE ME DEJA PEOR, PORQUE ESCONDERLO SERIA LA CAIDA.** Mi **primera**
corrida publicaba **CINCO NO CUMPLE**. Al cotejar cada rojo contra la letra de su celda
encontre que **cinco varas mias estaban mal escritas**, las corregi, y la segunda corrida
da **CERO NO CUMPLE**. Un salto asi es exactamente la forma que tiene una vara ablandada
hasta que pasa, asi que las dos corridas van declaradas fila a fila, con el motivo y la
cita de cada cambio, en **`SALIDA_V150_4_LAS_DOS_VARAS.txt`**, incluido el aviso de que la
primera corrida **no llego a commitearse**. Lo unico auditable entero es la segunda, y por
eso cada correccion lleva su motivo escrito **dentro del codigo**, al lado de la linea que
cambio.

**LA TABLA DE LAS OCHO**, contada de `SALIDA_V150_4_TABLA_POR_FASE.txt`, con la celda de
cada fila **leida de `08_VERIFICACION.md` en la corrida**:

| fase | veredicto | cifra |
|---|---|---|
| 0 CODIGO | **VERDE** | 7 de 7 con caso positivo rojo commiteado (6 propias, 1 por portadora) |
| 01 FUENTES | **VERDE PARCIAL** | 0 desaparecidos de 73; 68 con pasos distintos del grafo previo, 20 de ellos en nomina de otra fase |
| 02 DESTEJIDOS | **VERDE PARCIAL** | mapas de destejido exitcode 0; los quince congelados sin vara escrita |
| 03 FUSIONES | **VERDE PARCIAL** | 14 fichas de 03_FUSIONES con superviviente, 0 incumplimientos, 2 divergentes de la CORRECCION 16 |
| 04 ENLACES | **VERDE PARCIAL** | auto-aristas en Gate 0 OK; la confirmacion por lectura la excluye la propia celda |
| 05 SANEO | **VERDE** | 6 de 6 sub-celdas en verde, acotadas a las nominas |
| 06 MESAS | **VERDE** | 5 de 5 mesas con decision, motivo y cobertura |
| 07 ADUANA | **VERDE** | 4 controles OP-A en Gate 0, 4 en OK |

**VERDE 4 de 8, VERDE PARCIAL 4 de 8, NO CUMPLE 0 de 8.**

**4.e, UNA PALABRA POR SENTIDO.** El arnes usa **tres** veredictos y no los mezcla nunca:
**VERDE** es celda medida entera y cumplida; **VERDE PARCIAL** es celda de dos mitades con
la mecanica verde y la otra nombrada **sin darla por buena**; **NO MECANIZABLE** es celda
sin vara escrita contra el repo. En este reporte *correr* nunca significa *quedo
satisfecho*, y donde dos conjuntos se solapan se dice.

**4.b, la fila 07** se lee con la fase ya cerrada por el acta 149 y se mide **contra Gate
0**, que es lo que la celda nombra, no contra la vara de codigo, que es otra unidad por la
frontera del acta 144. **Cuatro controles `OP-A` corriendo, cuatro en `OK`.**

**4.c, LO QUE NO CALZA, CON SU CIFRA Y SIN REDONDEAR.** Las cuatro VERDE PARCIAL **abren**
la fase, no la dan por cerrada: para los **quince congelados** de 02,
`SALIDA_V150_4_TABLA_POR_FASE.txt` deja escrito que no hay vara contra el repo que los mida;
la confirmacion **por lectura** de 04 la excluye su propia celda por construccion; la
alteracion de pasos de 01 **no es atribuible** (20 de los 68 estan tambien en nomina de
otra fase, y los destejidos alteran pasos a proposito); y los **dos supervivientes
divergentes** de 03 siguen contados y nombrados por la CORRECCION 16.

**4.d, LA VERIFICACION TRANSVERSAL NO SE TOCA.** No la corri, no la declaro cerrada.

---

## 5. TAREA 5, LA GUARDA DEL CICLO, Y ME MORDIO A MI ANTES DE EXISTIR

**LA CAIDA ES MIA Y ES DE ESTA VUELTA.** Antes del commit de la TAREA 1 corri
`run_phase1.py` suelto y el guardian me aborto con la assertion de los **71 divergentes
entre las dos copias**, entera en `SALIDA_V150_5A_FALSO_ROJO_EN_VIVO.txt`. **Es la misma trampa de la 4.6.a del acta 149 y la misma que el
acta 147 registro contra si misma.** Cerre el ciclo en su orden y el motor volvio a 25/25,
como deja escrito `SALIDA_V150_MOTOR_CIERRE.txt`. Va declarada aqui y en el mensaje del
commit `fb3c0c75`.

**LO QUE SE CABLEA.** `scripts/loop/diagnostico_ciclo_a_medias.py`, nombre estable, en los
**tres** sitios donde el falso rojo aparece de verdad: la assertion de
`engine/test_gate_alias.py`, el check de gemelos de `scripts/run_phase1.py`, y el guardian
`.githooks/pre-commit`, que es donde me mordio.

**COMO DECIDE, y es determinista, sin `mtime` ni fechas.** La curaduria no vive en los
nodos: vive en `dataset/metadata/etiquetas_de_cara_v1*.json`. Si toda la divergencia es de
`etiqueta_arbol` y el DATASET no trae la canonica mientras la WEB si, **falta el comando 2
y lo nombra**; si es al reves, **falta el comando 3 y lo nombra**; y si toca cualquier otro
campo, dice con esas palabras que **ESTO NO ES UN CICLO A MEDIAS** y lista los campos.

**5.b, NO SE AFLOJA NADA.** El assert sigue cayendo, el exit code sigue siendo **1** y el
guardian sigue abortando en los tres casos. Se anade diagnostico, no una excepcion, y el
propio texto lo dice: *si las dos copias divergen DESPUES del ciclo entero, eso sigue
siendo rojo y sigue parando*.

**5.c, LOS CUATRO CASOS, CONTADOS DE `SALIDA_V150_5C_MUTACION_CICLO.txt`:**

| caso | que prueba | lo medido | su mutacion |
|---|---|---|---|
| **(A) control** | el ciclo en orden NO dispara el aviso | 0 divergencias, diagnostico vacio | **CAE** |
| **(B) falta el comando 2** | lo nombra | `FALTA: python scripts/etiquetas_de_cara.py --aplicar` | **CAE** |
| **(C) falta el comando 3** | lo nombra | `FALTA: python scripts/sync_assets_web.py` | **CAE** |
| **(D) rojo de verdad** | NO lo tapa | `ESTO NO ES UN CICLO A MEDIAS` | **CAE** |

**Los cuatro veredictos COMPUTADOS y los cuatro mutados CAEN**, y las dos copias quedan
identicas por sha256 antes y despues.

**Y LA PRUEBA EN VIVO, NO SIMULADA:** `SALIDA_V150_5A_FALSO_ROJO_EN_VIVO.txt` es el falso
rojo REAL, reproducido corriendo `run_phase1` suelto con la guarda ya puesta.
`AssertionError` con los 71, **EXITCODE 1**, y debajo el diagnostico nombrando el comando 2
y el ciclo entero en su orden. **El fin de la 5.a queda cumplido: quien lee el rojo sabe en
un segundo cual de las dos cosas es.**

**DE PROPINA, UNA TRAMPA QUE ME MORDIO Y QUEDA ESCRITA EN LA GUARDA:** `git diff --numstat`
compara el arbol contra el **INDICE**, no contra HEAD, asi que despues de un `git add` a
mitad del ciclo sale sucio con el arbol **igual a HEAD**. **La vara buena es `git diff HEAD
--numstat`**, y asi va impreso en el orden del ciclo que la guarda escribe.

---

## 6. TAREA 6, EL CIERRE

**El ciclo entero en su orden**, con sus cuatro salidas de cierre commiteadas
(`SALIDA_V150_GATE0_CMD1_CIERRE.txt`, `_CICLO_ETIQUETAS_CIERRE`, `_CICLO_SYNC_CIERRE`,
`_CICLO_NUMSTAT_CIERRE`): `GATE 0: OK` exit 0, **71 etiquetas** reaplicadas sin
encogimiento, seis assets sincronizados y el `numstat` **contra HEAD** sin una fila. **Las
tres suites en verde** y todas las cifras del cierre **RECOMPUTADAS al cierre**, no
heredadas de la apertura: estan en la cabecera tallada de la seccion 0.

**LAS GUARDAS DEL CIERRE, RE CORRIDAS SOBRE EL FICHERO COMMITEADO.** Son cinco: la
apertura sellada, el `--comparar` de la cabecera contra este mismo reporte, la cabecera
pegada, el cierre sellado y las ausencias. Las cinco salidas viven juntas en
`SALIDA_V150_GUARDAS_DEL_CIERRE.txt`, que publica **CABECERA: IDENTICA AL TALLADOR** sin
una sola fila distinta.

**EL MERGE NO SE PIDE Y NO SE HACE.** Es del fundador y solo suyo, y la campana no esta
consumada.

---

## 7. LAS RUTAS TOCADAS

  - `scripts/run_phase1.py`: la guarda de `OP-C-05` y el diagnostico del ciclo.
  - `engine/test_gate_alias.py` y `.githooks/pre-commit`: el diagnostico del ciclo.
  - `docs/plan/OPERACIONES.jsonl`: **una** linea, el `estado` de `OP-S-12`.
  - `docs/plan/CORRECCIONES_A_APLICAR.md`: `R.29` y la CORRECCION 30, por adicion.
  - `docs/PENDIENTES.md`: la remision a `R.29` y la ficha del indice semantico, por adicion.
  - `scripts/loop/`: `diagnostico_ciclo_a_medias.py` (nombre estable) mas seis instrumentos
    de vuelta (`vuelta150_medir_opc05`, `_2d_simular_op_c_05`, `_2c_verificaciones_op_c_05`,
    `_1b_rastro_del_1056`, `_1_registrar`, `_3_relectura_expediente`, `_4_tabla_por_fase`,
    `_5c_mutacion_ciclo`).
  - `docs/loop/`: las salidas de apertura, las de cierre y las de las cinco tareas, mas este
    reporte.

## 8. CORRECCIONES DECLARADAS EN ESTA VUELTA

  - **CORRECCION 30** en `docs/plan/CORRECCIONES_A_APLICAR.md`: la verificacion 4 de
    `OP-S-12`, con la cifra vieja intacta.
  - **La discrepancia del "monotona"** contra el acta 149, escrita dentro de esa misma
    correccion y no en su lugar.
  - **Las cinco varas de la TAREA 4**, en `SALIDA_V150_4_LAS_DOS_VARAS.txt`, con las dos
    corridas delante.
  - **Mi caida del ciclo de Gate 0**, declarada en la seccion 5 y en el commit `fb3c0c75`.

## 9. PENDIENTES DE DOCTRINA

**Ninguno nuevo.** Lo que la vuelta encuentra sin regla escrita se nombra donde toca y no
se inventa: la nomina de los **quince congelados** de la fila 02 (no hay fichero de datos
que la liste) y la **atribucion** de una alteracion de pasos a una fase concreta en la fila
01.

## 10. PARADA

**UNA, y no la resuelvo yo (`EJECUTOR.md` 5, `AUDITOR.md` 3).** La mitad de la **lista
blanca de `OP-C-05`**: su adjudicacion, tal como esta escrita, **no puede estar verde sobre
ningun grafo de esta campana ni sobre el anterior a ella, con las cifras de la seccion 1
delante, y las
dos salidas que se me ocurren chocan cada una con una letra distinta de la misma ficha. **La
traigo con su cifra y sin decidirla.** El encargo preveia esta salida con esas palabras:
*"SI EL TEXTO DE LA FICHA NO ALCANZA PARA EJECUTARLA SIN DECIDIR, PARAS Y LA TRAES"*.

---

## 11. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**1. LAS CINCO VARAS QUE CORREGI EN LA TAREA 4, Y EL SALTO DE CINCO NO CUMPLE A CERO**,
declarado fila a fila en `SALIDA_V150_4_LAS_DOS_VARAS.txt`. Es el discutible mas serio de la
vuelta y lo pongo el primero a proposito. Cada correccion tiene
su cita (la ficha de `OP-C-04` para la portadora; el universo *03 FUSIONES* de la propia
celda; la letra *"en su id ni en su titulo"* de `OP-S-01`; la correccion declarada de la
vuelta 120 dentro de `OP-S-02`; y `06_MESAS.md` como sede de las decisiones de mesa), y
**dos de las cinco filas siguen sin llegar a VERDE**. Pero quien lo lea tiene derecho a
sospechar de un ejecutor que reescribe su vara hasta que pasa, y por eso las dos corridas
estan declaradas.

**2. LA VENTANA DE 4.000 CARACTERES DE LA FILA 06 MESAS.** Para buscar motivo y cobertura
leo, de `06_MESAS.md`, los 4.000 caracteres siguientes a la primera mencion de cada mesa.
**Ese numero lo elegi yo**, no lo delimita la pagina, y podria atrapar una cifra de la
seccion vecina. Es lo que mas facilmente convierte un 2 de 5 en un 5 de 5.

**3. EJECUTAR MEDIA `OP-C-05` EN VEZ DE PARAR ENTERA.** El encargo dice *"paras y la
traes"*. Yo pare la mitad de la lista blanca y **ejecute la otra mitad**, porque las cuatro
verificaciones de la guarda de duplicadas son contestables sin decidir nada y porque sin
ella las 925 entradas que `SALIDA_V150_1B_RASTRO_1056.txt` cuenta se quedan sin guarda
que las defienda. Se puede leer como haberme saltado una parada.

**4. `R.29` EN `CORRECCIONES_A_APLICAR.md` Y NO EN `PENDIENTES.md`.** El encargo nombra ese
fichero con esas palabras y obedeci la letra, pero `R.20` a `R.28` viven en la otra pagina,
medido hoy. Deje una **remision**, no una copia. Puede ser que el encargo se equivocara de
fichero y que lo correcto fuera traerlo como pregunta antes de escribir.

**5. LA MITAD DE PRESENCIA DE LA VARA P2 EN LA TAREA 3.** La adjudicacion 3.9 del acta 144
pide **dos** cosas a un control, que exista y que muerda. Yo mido la primera y lo digo, pero
una P2 sola sostiene filas de la tabla de las 58. Se puede argumentar que media vara no debe
contar como prueba de ejecucion.

**6. EL UMBRAL DE `CONGELADO DECLARADO`.** Doy por declarada una ficha si su `nota` o su
`adjudicacion` contienen `ESTADO`, `DIFERIDA`, `CONGELAD`, `SIGUE EN LISTA` o `NO SE
MUEVE`. Es una lista de marcas **elegida por mi**: con otra lista, el reparto 28 contra 30
se mueve.

**7. LEER LA GUARDA DE `OP-C-05` SOBRE VIVOS.** Cito el criterio ya adjudicado para
`OP-C-04` y el universo de `OP-S-12`, pero la ficha de `OP-C-05` **no lo dice ella misma**.
Los **330** sobrantes en deprecados quedan declarados en el comentario de la guarda y fuera
de su alcance.

**8. LLAMAR DISCREPANCIA AL "MONOTONA" DEL ACTA 149.** Es una palabra en una glosa, no una
cifra publicada en una tabla, y el escalon es de **una unidad sobre 121**. La declaro
porque `EJECUTOR.md` 2 manda declarar y no copiar, pero puede juzgarse ruido.

**9. NO PEGAR EL BLOQUE DE COMMITS TALLADOS.** Lo cito en vez de pegarlo porque el asunto
de `38e26678` trae una palabra del vocabulario de la guarda de citas, que la lee como una
afirmacion mia. Se puede argumentar que la costumbre de la casa es pegarlo y que lo
correcto era traer el choque como pregunta antes de decidirlo solo.

**10. LA PIERNA P3 CUENTA UN COMMIT QUE NOMBRA Y TOCA CODIGO COMO EJECUCION.** Un commit que
menciona un `id_op` y de paso toca `scripts/loop/` cuenta como huella. La condicion de rutas
recorta mucho, pero no separa del todo el registro de la ejecucion.

## 12. PREGUNTAS

**1. LA LISTA BLANCA DE `OP-C-05`: cual de las dos letras cede?** O la guarda de
bidireccionales no se enciende nunca tal como esta escrita, o la lista blanca deja de ser
por evidencia. **No la contesto yo.**

**2. LAS TREINTA FICHAS CONGELADAS EN SILENCIO: se descongelan o se declaran?** El acta 149
movio **una** (`OP-S-12`) por ser la unica de su fase sin mover. Medido sobre las 71, la
especie tiene **treinta** ejemplares, y no hay encargo que diga que hacer con ellos.

**3. `OP-L-01` sale sin huella de ejecucion en las tres pruebas y con `depende_de` vacio,
segun `SALIDA_V150_3_RELECTURA_EXPEDIENTE.txt`.** La nombro por la 3.c y no la toco.
**Entra en algun encargo, o esta cerrada por otra via que no supe medir?**
