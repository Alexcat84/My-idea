# REPORTE DE LA VUELTA 97 (EJECUTOR)

Rama `pasada-unica`. Fase III, fase 04 ENLACES, modo de ejecucion continua.
Sobrescribe el reporte de la vuelta 96. Toda la identidad de esta cabecera (rama,
commit del acta, HEAD real de apertura) se lee de git y se talla, nunca se teclea
(`EJECUTOR.md` regla 1, "LA IDENTIDAD SE LEE DE GIT"): va en la ultima fila de la
tabla de abajo, salida entera del tallador.

**LA VUELTA ENTRA CON LAS DOS RACHAS EN CERO** y con el acta de la vuelta 96
declarando *"la primera tanda de la campana sin una sola caida"*
(`ACTA_AUDITOR.md` seccion 5, linea **34434**, leida hoy). Eso no relaja nada: la
especie que cayo tres veces seguidas (la cuenta de piezas de artefacto contada a
ojo) se talla en esta vuelta **tambien en las faciles**, y las cuentas de este
reporte llevan al lado el fichero del que salen.

Ejecuta el encargo entero de `docs/loop/PROMPT_SIGUIENTE.md`: **TAREA 1**, los
registros del acta 96; **TAREA 2**, el segundo tramo de `OP-E-03`, 60 pares.

**LOS DOS RESULTADOS DE FONDO, al frente.** `OP-E-03` pasa de 40 a **100 leidos de
183**, con los cinco puntos de su verificacion remedidos y no heredados. Y la
proporcion de direcciones no resueltas **SUBE del 27,5% al 45,0%**, que es lo que
el encargo pidio no maquillar: en vez de invocar la frase de cortesia que el
propio encargo ofrecia (*"es la bolsa, no tu vara"*, que estaba escrita **para el
caso de una proporcion parecida**, y esta no lo es), **se construyo un instrumento
que pone esa frase a prueba**. Lo medido: la bolsa **viene ordenada de mas fuerte
a mas debil**, cosa que no estaba escrita en ningun sitio. Lo que **NO** queda
probado, y se dice igual de fuerte: **eso no demuestra que mi umbral sea el
correcto.**

## CABECERA TALLADA (`--fase04 --vuelta 97`), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 97`.
Salida completa en `docs/loop/SALIDA_V97_CABECERA_TALLADA.txt`, **EXIT 0**. Antes
del commit de cierre se corre otra vez con `--comparar docs/loop/REPORTE.md` sobre
este mismo fichero ya escrito (seccion "LA COMPARACION FINAL", mas abajo).
**Ninguna celda de esta tabla esta tecleada.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `eb91fbd4` (ACTA DE LA VUELTA 96 DEL AUDITOR, leido de git log), HEAD real de apertura `eb91fbd4` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `eb91fbd4` (ACTA DE LA VUELTA 96 DEL AUDITOR, leido de git log), HEAD real de apertura `eb91fbd4` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE** |

**ESTA VUELTA EL COMMIT DEL ACTA Y EL HEAD REAL DE APERTURA COINCIDEN**, los dos
`eb91fbd4`, y se dice porque **la vuelta 96 fue el caso contrario** (acta
`ea93d674` y HEAD `f9c7bb77`, separados por el commit de la decision del
fundador). El caso facil se declara con su comando al lado igual que se declaro el
dificil. **El sello se escribio en el PRIMER commit de la vuelta** (`eee77af3`,
cuyo padre es `eb91fbd4`), antes de tocar nada.

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION Y EL CIERRE SE RECOMPUTO AL
CIERRE**, las dos con corrida propia completa y ninguna heredada: ciclo de tres
(`run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py --aplicar`,
`sync_assets_web.py`), conteo de aristas, desfase, motor, web y tsc, en los dos
lados. **CERO ARISTAS SE MOVIERON**: `git diff --stat -- dataset/
web/lib/assets/`, corrido **DESPUES** de todas las mediciones de cierre, da
**CERO lineas**.

## EL MARCADOR Y LA TASA POR DOMINIO, REMEDIDOS ESTA VUELTA

Comando: `python scripts/recomputar_marcador.py 3388`, salida en
`docs/loop/SALIDA_V97_MARCADOR_CRIBADO_CIERRE.txt`, EXIT 0. Cifras leidas de ese
fichero:

- `n = 3388 corte = 3388 huecos: [] dups(puesto): 0`, pares duplicados 0.
- **MARCADOR GLOBAL: A 551 (16,3) / B 72 (2,1) / C 5 (0,1) / D 2.760 (81,5).**
- **TASA POR DOMINIO:** compras 155/1 (0,6), core 1.445/325 (22,5), entrega 171/2
  (1,2), environmental 170/28 (16,5), exportacion 130/15 (11,5), franquicias
  148/15 (10,1), health_safety 192/43 (22,4), quality 844/119 (14,1),
  risk_management 106/0 (0,0), seguridad_digital 27/3 (11,1).

**NI EL MARCADOR NI LA TASA SE MUEVEN POR NADA DE ESTA VUELTA, y esta verificado y
no supuesto:** `git diff --stat` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y
`docs/INTRA_DOMINIO_PARES.jsonl` da **VACIO**
(`docs/loop/SALIDA_V97_TAREA2_CINCO_PUNTOS.txt`). Los 60 veredictos de la TAREA 2
son **LECTURA DIRIGIDA** y viven en fichero propio
(`docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl`), **fuera de la cola y fuera de la
tasa por dominio del banco 9.27**, como manda el punto 5 de
`OP-E-03.verificacion`.

**El fichero se llama `..._MARCADOR_CRIBADO_CIERRE.txt` y no
`..._MARCADOR_CIERRE.txt` a proposito**, misma convencion que las vueltas 94 y 96:
la fila opcional del tallador espera el formato viejo del cribado y este es el del
recomputo, asi que se le deja fuera en vez de darle un fichero que no sabe leer.

## TAREA 1: LOS REGISTROS DEL ACTA 96

Escritos en `docs/PENDIENTES.md`, seccion "VUELTA 97, TAREA 1". Composicion del
anadido **tallada, no contada a ojo**
(`docs/loop/SALIDA_V97_TAREA1_COMPOSICION.txt`, EXIT 0): **1 seccion de nivel 2 y
3 subsecciones de nivel 3**, 4 filas casadas. Aditividad tallada de
`docs/loop/SALIDA_V97_TAREA1_NUMSTAT.txt`: **182 anadidas, 0 borradas.**

**EL TALLADOR SE CORRIO PRIMERO CONTRA UN CASO POSITIVO, y por eso su cifra es
citable.** El mismo patron corrido sobre
`docs/loop/SALIDA_V96_TAREA1_DIFF_PENDIENTES.txt` reproduce **1 y 4**, que es
exactamente lo que la vuelta 96 publico. Un tallador que no reproduce una cifra
vieja conocida no puede avalar una nueva.

**(1.1) Las SEIS adjudicaciones del acta 96 (4.1 a 4.6)**, cada una con **su linea
leida hoy** con `grep -n '^### 4\.[1-6]'` y con su efecto sobre el trabajo:
**4.1** linea 34274, **4.2** linea 34317, **4.3** linea 34356, **4.4** linea
34367, **4.5** linea 34381, **4.6** linea 34415.

- **La 4.1 CIERRA LA MESA.** El auditor acepto la invitacion del reporte 96 y
  construyo **TRECE varas**, corridas contra las 19 adjudicaciones publicadas.
  Veredicto literal (linea 34297): *"NINGUNA DE LAS TRECE REPRODUCE LAS
  DIECINUEVE."* La mejor llega a **17 de 19** (contra los 14 de la mia) y sigue
  contradiciendo el **1281** y el **1992**, con lo cual **cae por la misma vara con
  la que yo descarte la mia**. Y el resultado que de verdad cierra: **las tres
  varas que llegan a 17 dicen QUEDA a los tres de la mesa**, o sea que el destino
  de 886, 890 y 947 **no depende de la vara elegida**. Queda registrado, sin que el
  auditor lo llame caida, que **la vara que elegi no era la mas fuerte disponible**.
- **La 4.3** confirma los pares **26, 16 y 23**: nada que rehacer en el fichero de
  lectura del tramo 1.
- **La 4.4 manda sobre el trabajo de HOY:** *"el umbral esta bien puesto y no se
  toca"* (linea 34374). El auditor leyo a ciegas las cinco que yo marque (**11, 22,
  35, 36, 37**) y llego a NO RESUELTA en las cinco. **El tramo 2 se leyo con ese
  mismo umbral, sin moverlo.**
- **La 4.6** deja la deriva de contenido **anotada para Alexis y sin encargar**. **No
  se toco.**

**(1.2) La correccion declarada del "OCHO", nombrada por lo que es: una CAIDA DE
ACTA DEL AUDITOR**, que el propio auditor lleva a sus errores con nombre (seccion
6 punto 1, linea **34457**). El texto viejo **no se borra**. **NO SE REMIDE**, por
mandato expreso del encargo: ya viene medida dos veces y de forma independiente
(mi instrumento de la vuelta 96 y las regex propias del auditor), y salieron
identicas con enumeraciones incluidas. **Correr una tercera no anade vara: anade
ruido**, y se dice en vez de dejarlo implicito.

**(1.3) El pendiente de doctrina de la vuelta 96 apartado (f) queda RESUELTO**, y
la marca de resuelto se escribio **DEBAJO de su texto, sin borrar nada**.
Adjudicado **POR EXTENSION CITABLE y no como doctrina nueva**, citando `AUDITOR.md`
1.2 (la relectura ciega se define por lo que produce, un contador de coincidencia)
y 1.3 (*"el ejecutor verifica contra el grafo y decide con la vara"*). Letra
literal (linea 34402): **manda el criterio escrito de la operacion; la lectura
ciega es control de la clase y detector de discrepancia, nunca fuente de
direccion.** Queda escrito que **NO reabre** el 1886, el 1844, el 1009 ni el 1098.

## TAREA 2: `OP-E-03` LLEGA A LA FILA 100 DE 183

Registrada entera en `docs/PENDIENTES.md`, seccion "VUELTA 97, TAREA 2".
Composicion tallada (`docs/loop/SALIDA_V97_TAREA2_COMPOSICION.txt`, EXIT 0): **1
seccion de nivel 2 y 7 de nivel 3**, 8 filas casadas. Aditividad tallada
(`docs/loop/SALIDA_V97_TAREA2_NUMSTAT.txt`): **232 anadidas, 0 borradas.**

Material entero en `docs/loop/SALIDA_V97_TAREA2_TRAMO2_MATERIAL.txt`, **2.070
lineas** contadas con `wc -l`, y **60 filas** casadas por el tallador de
composicion (`docs/loop/SALIDA_V97_TAREA2_MATERIAL_COMPOSICION.txt`, EXIT 0), de
ellas **29 de quality y 31 de otros dominios**. Corrido con
`vuelta96_tarea3_tramo1_opE03.py --desde 40 --cuantos 60`, o sea el instrumento de
la vuelta 96 **sin tocarle una linea**, como el encargo manda.

**LA LECTURA NO SE DEGRADO Y POR ESO NO SE PARO.** El encargo autorizaba parar a
mitad diciendolo con la cifra; se leyeron los **60** con el mismo detenimiento. Se
dice para que el silencio no tenga que interpretarse.

**Los cinco puntos de `OP-E-03.verificacion` se cumplen y se REMIDIERON en la
vuelta** (`docs/loop/SALIDA_V97_TAREA2_CINCO_PUNTOS.txt`): cribado recontado en
**3.388** filas cada fichero; **ids por el RESOLUTOR antes de cruzar nada** (`P.1`,
y en estas 60 **el resolutor no movio ninguno**, lo cual se declara igual **porque
`P.1` obliga a declararlo siempre**); cuenta sin fugas (**cero** de las 60 esta ya
en la cola tras resolver contra los **2.796** pares distintos, **cero** repetidas,
60 puestos distintos del 41 al 100); marca **LECTURA DIRIGIDA** contada **60 de
60** en el material y **60 de 60** en el JSONL; y veredictos **APARTE de la tasa
por dominio**, en fichero propio y rotulado.

### El resultado, tallado de `SALIDA_V97_TAREA2_VEREDICTOS.txt`

| clase | que significa | cuantas de 60 |
|---|---|---:|
| A | REPITE (lo que anade cabe en una linea) | 3 |
| B | DUDOSO (la vara no lo resuelve sola) | 1 |
| C | figura aparte | 0 |
| D | CONTINUA (trae procedimiento que el otro no tiene) | 56 |

| direccion (banco `9.6.2`) | cuantas |
|---|---:|
| LEIDA y afirmada | 33 |
| NO RESUELTA, declarada como tal | 27 |

| dominio | pares del tramo | A | B | C | D |
|---|---:|---:|---:|---:|---:|
| core | 22 | 1 | 1 | 0 | 20 |
| environmental | 3 | 0 | 0 | 0 | 3 |
| exportacion | 3 | 0 | 0 | 0 | 3 |
| health_safety | 2 | 1 | 0 | 0 | 1 |
| quality | 29 | 1 | 0 | 0 | 28 |
| risk_management | 1 | 0 | 0 | 0 | 1 |

**ESTA TABLA POR DOMINIO NO ENTRA EN LA TASA DEL BANCO `9.27`** y va rotulada asi
en su fichero.

**LOS TRES A:** el **42** (`cultura_justa_2` contra `preguntar_que_no_quien`), el
**88** (`genchi_gembutsu_salir_del_edificio` de Ries contra
`get_out_of_the_building` de Blank, dos casas del mismo consejo en dos libros) y
el **100** (`desarrollar_metas_anuales` contra `metas_negocio_calidad`, donde la
madre ya barre las areas, ya exige meta medible con plazo y ya la mete en el plan
de negocio). **EL UNICO B es el 47**, declarado DUDOSO en vez de forzado: **la
direccion si se lee** y lo que la vara no resuelve sola es la clase.

### La proporcion de no resueltas SUBE, y se mide en vez de explicarse

**LA CIFRA PRIMERO, sin suavizarla: 11 de 40 (27,5%) en el tramo 1 y 27 de 60
(45,0%) en este.** El encargo escribio *"Si el segundo tramo da otra proporcion
parecida, es la bolsa, no tu vara"*. **La premisa no se cumple**, asi que **no
invoco la conclusion**: construi
`scripts/loop/vuelta97_tarea2_senal_de_la_bolsa.py`
(`docs/loop/SALIDA_V97_TAREA2_SENIAL.txt`, EXIT 0) para ponerla a prueba.

| tramo | filas | mediana de `titulo_ratio` | madre e hijo de la MISMA fuente |
|---|---:|---:|---:|
| tramo 1 (filas 1 a 40) | 40 | 84.3 | 33 de 40 (82.5%) |
| tramo 2 (filas 41 a 100) | 60 | 78.2 | 44 de 60 (73.3%) |
| sin leer (filas 101 a 183) | 83 | 76.2 | 62 de 83 (74.7%) |

**LA BOLSA VIENE ORDENADA DE MAS FUERTE A MAS DEBIL, y eso no estaba escrito en
ningun sitio:** 84,3 a 78,2 a 76,2. **El tramo 2 no es una muestra equivalente al
tramo 1: es un tramo mas debil de la misma bolsa.**

| grupo del tramo 2 | filas | mediana de `titulo_ratio` | madre e hijo de la MISMA fuente |
|---|---:|---:|---:|
| direccion LEIDA | 33 | 81.5 | 26 de 33 (78.8%) |
| direccion NO RESUELTA | 27 | 77.3 | 18 de 27 (66.7%) |

Las mitades salen del JSONL de veredictos, **no de una lista tecleada**. Las filas
que la lectura no resolvio son, **medidas por fuera de la lectura**, las mas
debiles. Las dos afirmaciones salen **VERIFICADAS** y **las dos podian salir en
rojo**.

**LO QUE ESTO NO PRUEBA, y lo digo con todas las letras porque es lo primero que se
me podria conceder de mas: NO prueba que mi umbral sea el correcto.** Una vara
demasiado estricta aplicada a una bolsa que se debilita produciria **exactamente
estas dos mismas seniales**. Va marcado como **discutible numero 1**.

### Las NUEVE figuras, registradas y SIN ADJUDICAR

Mismo trato que las seis del tramo 1, por mandato del encargo. Impresas enteras en
el fichero de veredictos. Las cuatro que mas pesan:

1. **LOS GEMELOS DE LA ESTRATEGIA DE INNOVACION, y el tramo trae LOS DOS.**
   `estrategia_de_innovacion_de_producto` (madre del 45) contra
   `estrategia_innovacion_producto` (hijo del 84): dos preposiciones de diferencia
   en el id, mismo libro, contenido casi calcado. **Corrobora desde un segundo
   camino la figura que el tramo 1 registro.**
2. **LOS GEMELOS DEL TIEMPO DE CICLO:** `reduccion_de_tiempo_de_ciclo` (63) contra
   `reduccion_tiempo_ciclo` (70), misma especie que la familia de la capacidad de
   proceso del tramo 1.
3. **LA FAMILIA CROSBY DE LOS 14 PASOS, REPARTIDA Y MAL EMPAREJADA.**
   `costo_de_calidad_3` sale en **tres filas seguidas** (81, 82, 83) con tres madres
   distintas y la misma senial 84,4, y **solo la del 83 es la suya**, que ademas
   **esta dentro de la propia bolsa**.
4. **EL BARRIDO VUELVE A CASAR UN PASO CON SU REFUTACION**, y ahora es **Juran
   contra Deming** en dos filas (51 y 60), con `pre_control_estadistico` en medio.
   **No es un defecto del barrido: es material real de dos escuelas en tension**, y
   quien cablee esa zona tiene que saberlo antes de poner una arista.

### Las guardas, probadas por mutacion

`docs/loop/SALIDA_V97_TAREA2_MUTACION.txt`, EXIT 0. Cifras del pie **contadas por
el propio instrumento**: **12 de 12, con 6 mutaciones que tenian que caer y 6
controles verdes.** Las seis caen: clase fuera del alfabeto, puesto repetido,
direccion que nombra nodos de otra fila, tabla incompleta, `normaliza_fuente`
mutada a constante (la afirmacion 2 deja de sostenerse) y `titulo_ratio` del tramo
2 subido a 99,0 (la afirmacion 1 deja de sostenerse).

**Y SE DECLARA LO QUE NO SE PRUEBA:** la **clase** y la **direccion** de cada uno
de los 60 pares son **tabla a mano** y **NO tienen caso rojo automatico**, porque
no hay dentro del repo una segunda fuente independiente contra la que
contrastarlas. Su control es la relectura ciega del auditor, no un `assert`.

### El addendum, por script, con la guarda probada en vivo

La vuelta 96 dejo sellado en el plan que *"QUEDAN 143 SIN LEER"*. **Hoy quedan
83**, y una cifra sellada que la propia campana ya movio no se deja quieta. El
segundo addendum se escribio con
`scripts/loop/vuelta97_tarea2_addendum_opE03.py`, `--simular` antes de
`--aplicar`, **con las cifras leidas del JSONL y no tecleadas**, las dos salidas
commiteadas. Medido: `04_ENLACES.md` **puramente aditivo (36 anadidas, 0
borradas)** y `OPERACIONES.jsonl` **una sola linea**. **Guarda de idempotencia
probada EN VIVO:** la segunda corrida de `--aplicar` da **ROJO** y no escribe
(`docs/loop/SALIDA_V97_TAREA2_ADDENDUM_IDEMPOTENCIA.txt`, EXIT 1).

## DOS DESVIACIONES MIAS, DECLARADAS. NINGUNA MUEVE UNA CIFRA

**(1) UNA SALIDA DE APERTURA SALIO EN LA CODIFICACION EQUIVOCADA, Y ES MIA.**
`docs/loop/SALIDA_V97_GATE0_CMD1_APERTURA.txt` se escribio en **cp1252** y no en
UTF-8, por una redireccion mia; la salida equivalente de la vuelta 96 **si es
UTF-8**, o sea que es una desviacion respecto a la vuelta anterior y no una
propiedad del instrumento. **Se transcodifico sin perdida** y se dejaron los
`sha256` de antes y despues en
`docs/loop/SALIDA_V97_TRANSCODIFICACION_DECLARADA.txt`. **NO se volvio a correr el
ciclo de tres**, porque la apertura ya estaba sellada y remedirla la convertiria en
estado intermedio. **Ninguna celda de la cabecera cambia**: las cifras del Gate 0
son ASCII. **Lo detecte porque el tallador de composicion cayo en ROJO al no poder
leer el fichero**, o sea que lo encontro un instrumento y no mi memoria.

**(2) EL UNICO GUION LARGO DEL MATERIAL NO ES MIO, Y HAY DOCE MAS EN EL GRAFO.**
El guion de la linea 1120 del material sale del **titulo del nodo**
`smed_setup_reduction`, impreso literal. Medido a proposito de eso: **12 nodos del
grafo llevan guion largo o medio en su `titulo_concepto`** (entre ellos
`6s_workplace_organization`, `kanban_pull_system`, `muestreo_dodge_romig` y los
tres `costo_de_mala_calidad_copq`). **NO SE TOCA NINGUNO** (`EJECUTOR.md` regla 4,
modo de cierre, cero reparaciones de nodos: el encargo no dice que la campana entro
en fase de ejecucion de nodos). Va como **pregunta al final de este reporte**, no
como trabajo hecho.

## RUTAS TOCADAS (commits `eee77af3` a `c46cd795`)

**Talladas, no tecleadas** (`EJECUTOR.md` regla 1, "LA TABLA SE CUENTA DE SU
FICHERO"): `git diff --name-status eb91fbd4 HEAD` a
`docs/loop/SALIDA_V97_RUTAS_TOCADAS.txt`, contado con
`scripts/loop/tallar_composicion_salida.py` a
`docs/loop/SALIDA_V97_RUTAS_COMPOSICION.txt`, EXIT 0:

| clase | filas |
|---|---:|
| fichero NUEVO (A) | 28 |
| fichero MODIFICADO (M) | 3 |

**Los TRES modificados, enumerados por el instrumento:** `docs/PENDIENTES.md`,
`docs/plan/04_ENLACES.md`, `docs/plan/OPERACIONES.jsonl`. **Los 28 nuevos,
desglosados contando el mismo fichero:** **4** instrumentos en `scripts/loop/`,
**1** fichero de lectura en `docs/plan/` y **23** salidas `docs/loop/SALIDA_V97_*`.
**CERO ficheros de `dataset/`, `web/` o `engine/` tocados**, verificado por el
`git diff --stat` vacio citado arriba.

Aditividad de los tres modificados en la vuelta entera
(`docs/loop/SALIDA_V97_NUMSTAT_VUELTA.txt`): `PENDIENTES.md` **414 anadidas, 0
borradas**; `04_ENLACES.md` **36 y 0**; `OPERACIONES.jsonl` **1 y 1** (una linea
JSONL reescrita, que es la forma que tiene ese fichero de ser aditivo).

**El conteo cubre hasta `c46cd795`**, o sea las dos tareas; los ficheros de CIERRE
(`SALIDA_V97_*_CIERRE.txt`, la cabecera tallada, las rutas tocadas y este reporte)
entran en el commit de cierre y **por eso no estan en esa cuenta**. Se dice en vez
de dejar que la cifra parezca cubrirlo todo.

## LAS RACHAS

- **CLASE O CIFRA PUBLICADA: CERO.** Ninguna cifra de `docs/plan/` ni del banco
  quedo sin su corte, y ningun veredicto del cribado se movio.
- **REPORTE: CERO al entrar.** Lo que esta vuelta anade a la defensa: el tallador
  de composicion se corrio **con caso positivo delante** contra la cifra que la
  vuelta 96 publico, y las dos desviaciones que encontre **las declaro yo aqui** en
  vez de esperar a que las encuentre el acta.

## PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** El unico que estaba abierto (el de la vuelta 96 apartado (f))
**queda RESUELTO** por la adjudicacion 4.5 del acta 96, y esta marcado como
resuelto sin borrar su texto.

## LA COMPARACION FINAL

`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 97 --comparar
docs/loop/REPORTE.md`, corrido DESPUES de escribir este fichero y ANTES del commit
de cierre; su salida se pega en el mensaje del commit de cierre y se guarda en
`docs/loop/SALIDA_V97_COMPARAR_CIERRE.txt`.

## UNA PREGUNTA, porque no la puedo decidir yo

**Los 12 nodos con guion largo o medio en el titulo.** La regla de cero guiones es
canon del proyecto y estos son titulos que la web muestra, pero **arreglarlos es
tocar nodos**, y `EJECUTOR.md` regla 4 me lo prohibe mientras el encargo no diga
que la campana entro en fase de ejecucion de nodos. **No los toco y no adivino si
importan.** La traigo medida (12, con sus ids en el commit `c46cd795`) para que se
decida si es trabajo de esta campana, backlog de otra, o nada.

## LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

Marcados **antes** de saber si acierto.

1. **LA SUBIDA AL 45% DE DIRECCIONES NO RESUELTAS PODRIA SER MI VARA Y NO LA
   BOLSA, Y MI PROPIO INSTRUMENTO NO PUEDE DISTINGUIRLO.** Es el discutible mas
   grande de la vuelta y lo pongo primero. Medi que la bolsa se debilita y que las
   filas sin direccion son las mas debiles, pero **una vara demasiado estricta sobre
   una bolsa que se debilita daria las mismas dos seniales**, y lo escribi dentro
   del propio instrumento para no poder olvidarlo. **La forma de tumbarme es leer a
   ciegas una muestra de mis 27 no resueltas**, como el auditor hizo con cinco del
   tramo 1. Si de esa muestra salen direcciones afirmables, mi umbral se movio sin
   que yo lo notara entre un tramo y otro.
2. **LOS PARES 66 Y 77 SON LOS DOS QUE MAS CERCA ESTAN DE CAER DEL OTRO LADO, Y LOS
   PUSE LOS DOS EN LEIDA.** En el **66** el paso de la madre pide **BALANCEAR**
   accountability con proteccion del aprendizaje, y el hijo entrega **solo una de
   las dos mitades**. En el **77** el paso pide medir el impacto **DE LA
   CAPACITACION** sobre el desempenio de los proyectos, y el hijo mide el desempenio
   **sin cerrar ese vinculo causal**. Los sostuve por consistencia entre ellos y con
   el 97, pero **si el auditor los lee NO RESUELTOS, tiene un argumento mejor que el
   mio**, y entonces mi 45% deberia ser todavia mas alto, no mas bajo.
3. **EL PAR 42 LO LLAME A Y PODRIA SER D.** Lo que `preguntar_que_no_quien` anade
   sobre el paso 2 de `cultura_justa_2` lo lei como dos lineas sueltas, pero **el
   hijo tiene cuatro pasos y el 9.6.2 avisa de que una linea que tarda varios pasos
   en ejecutarse es un procedimiento nombrado en una linea**. Lo sostuve en A **por
   consistencia con el par 12 del tramo 1**, que tiene el mismo hijo contra otra
   madre de Dekker y salio A. **Si el 42 es D, el 12 tambien lo era**, y eso toca una
   clase ya publicada.
4. **EL PAR 47 EN B PODRIA SER A.** La frontera entre "mas que una linea" y "menos
   que un procedimiento" es donde vive la B y **es mi juicio**. Un lector estricto
   diria que "extender la comparacion a cronograma y calidad y calcular la magnitud"
   **cabe en una linea** y el par es A.
5. **MIS SOSPECHAS DE INVERSION (82, 89 y 65) LAS DEJE EN "NO RESUELTA" EN VEZ DE
   AFIRMAR LA DIRECCION CONTRARIA.** En el tramo 1 si afirme una inversion (el par
   16). Aqui vi tres casos donde **lo etiquetado como hijo parece la madre** y **no
   me atrevi a darles la vuelta**, solo a anotarlo. **Puede ser prudencia o puede ser
   incoherencia con lo que hice en el tramo 1**, y no se cual de las dos es.
6. **LAS NUEVE FIGURAS PUEDEN SER DEMASIADAS.** El tramo 1 registro seis en 40
   pares; yo registro nueve en 60. Es proporcion parecida, pero **algunas de las
   mias son propiedades del barrido y no hallazgos sobre nodos** (la 4, los nodos
   iman, y la 7, el falso amigo por nombre propio). **Si el auditor considera que
   eso es una sola figura repetida, mi cuenta baja.**
7. **DECIDI ESCRIBIR EL ADDENDUM SIN QUE EL ENCARGO LO PIDIERA.** El encargo de la
   vuelta 97 **no menciona el addendum**; lo hice porque la vuelta 96 dejo "QUEDAN
   143 SIN LEER" sellado en dos ficheros del plan y hoy es falso. **Es una
   iniciativa mia sobre ficheros del plan**, y si el criterio es que el plan solo se
   toca cuando el encargo lo dice, me pase.
