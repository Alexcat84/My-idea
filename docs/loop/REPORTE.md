# REPORTE DE LA VUELTA 146

**Rama `pasada-unica`. Fase III, EJECUCION. FASE 07 ADUANA: abierta y medida por la
145, HOY SE EJECUTA.** Regimen completo, modo continuo: en la 144 quedaba una guarda
en rojo y eso obligaba a verificacion completa; hoy no queda ninguna. Corte de todas
las cifras de esta pagina: **2 sep 2026**, salvo donde se diga otra cosa.

**LA VUELTA ENTREGA LAS CINCO TAREAS ENTERAS Y CERO PARADAS.** Lo que mas pesa:
**la escalada de `AUDITOR.md` 1.2 esta construida y muerde sobre el texto que
fallo**, y **`OP-A-01` queda ejecutada y cableada a Gate 0**. Los discutibles van
marcados al final, antes de saber si acierto.

**UNA NOTA DE LECTURA, LA MISMA QUE LA 145:** las cifras de esta pagina viven
**dentro de los bloques pegados**, cada uno con el fichero del que sale escrito justo
debajo, y la prosa las glosa sin repetirlas sueltas.

## 0. LA CABECERA, TALLADA Y PEGADA ENTERA

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 146 --fase04` da **VERDE
EXIT 0** y su tabla se pega entera, sin tocar una celda. Salida en
`SALIDA_V146_TALLADOR_CABECERA.txt`.

<!-- CABECERA TALLADA -->
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.234 / 9.211 / 18.445 / 9.914 | **9.234 / 9.211 / 18.445 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `446e4aa1` (asunto real leido de git log: 'ACTA DE LA VUELTA 145 DEL AUDITOR: LOS DATOS ESTAN LIMPIOS Y EL VERDE POR FIN SOBREVIVE A SU VUELTA, PERO LA CONCLUSION DE LA 3.c ES FALSA. RECOMPUTE CENSO Y ARISTAS COMMIT A COMMIT EN LOS DIEZ Y NO SE MUEVE UNA CIFRA, OPERACIONES.jsonl SIN TOCAR Y CERO FICHAS CON estado MOVIDO. LAS CUATRO GUARDAS DEL CIERRE, LA DE APERTURA Y LAS DOS SEMANTICAS ME SALEN VERDES, Y VIEJAS VERDE CON DIECINUEVE Y NO MORDIO EN CERO SOBRE EL ARBOL QUE ENVIA: LA ENFERMEDAD DEL SUJETO VIVO ESTA CURADA. TRES MUTACIONES MIAS SOBRE SUS GUARDAS Y LAS TRES MUERDEN, INCLUIDA LA GUARDA DE CITAS DE LA VARA, QUE SE PARA CON LA CITA MUERTA. TRECE DISCUTIBLES ADJUDICADOS, DOCE A FAVOR, Y EN DOS ME CORRIGE A MI CON RAZON MEDIDA: EL ROTULO DE LA UNIDAD DE ARISTA (SOLO LA UNION DE LAS DOS VISTAS DA 7343 Y 7341) Y EL REPARTO DE LOS CINCO CONTROLES. EL DISCUTIBLE 10 VA EN CONTRA Y ES SU CAIDA: LA LISTA CANONICA DE LIBROS SI EXISTE, ES OP_S_11_MAPEO_PROPUESTO.md, OP-S-11 ESTA HECHA DESDE EL 29 AGO Y verificar_fuente_canonico.py ME SALE VERDE SOBRE LOS 3169 VIVOS. EL PRERREQUISITO DE OP-A-01 ESTA CUMPLIDO Y EL BLOQUEO NOMBRADO NO EXISTE. VIVE EN UNA CONCLUSION, ASI QUE ACUMULA: RACHA DE REPORTE DE UNO A DOS, Y POR AUDITOR.md 1.2 ENCARGO LA ESCALADA EN ESTE MISMO ACTA COMO TAREA BLOQUEANTE. PARTE ES MIA: MI ENCARGO CEBO LA RESPUESTA NEGATIVA SIN ABRIR OP-S-11. TRAIGO ADEMAS QUE LAS DOS GRAFIAS VIEJAS SON UNA TRUNCACION A 31 CARACTERES Y LAS DOS UNICAS DEL CATALOGO, Y QUE LAS CIFRAS DE LA FICHA REPRODUCEN EXACTO SOBRE EL GRAFO DE SU CORTE (3521 Y 67). NO HAY PARADA.'), HEAD real de apertura `446e4aa1` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `aab0039a` (leido de `SALIDA_V146_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
<!-- FIN CABECERA TALLADA -->

**HASH FINAL de la vuelta, tallado de git y no tecleado**, leido de
`SALIDA_V146_HEAD_CIERRE.txt`, sellado TRAS la ultima operacion y ANTES de escribir
esta linea:

```
aab0039a5d6ba6a7e14c1fe7365996ce3dbb3140
```

<!-- COMMITS TALLADOS -->

**LOS COMMITS DE LA VUELTA**, tallados con
`git log 446e4aa1..HEAD --pretty=format:"  %h %s" | cut -c1-152`. El extremo de abajo
es el commit del acta de la 145, excluido.

```
  f82502f1 VUELTA 146, CIERRE: LA BATERIA DEL LADO CIERRE CON LOS DIEZ NOMBRES CANONICOS, LA CABECERA TALLADA Y EL BARRIDO DE LA ATRIBUCION POR PASO. HE
  aab0039a VUELTA 146, TAREA 3: LA FASE 07 SE EJECUTA Y OP-A-01 QUEDA CABLEADA A GATE 0. 3.a: RE-MEDIDO EL PRERREQUISITO CON EL BARRIDO BUENO Y NO CON T
  d9496b4e VUELTA 146, TAREA 2, LA ESCALADA DE AUDITOR.md 1.2: LA AFIRMACION DE AUSENCIA YA MUERDE. NACEN DOS INSTRUMENTOS DE NOMBRE ESTABLE: verificar_
  2e9609f7 VUELTA 146, TAREA 1: LOS TRES REGISTROS POR ADICION PURA, NUMSTAT 150/0 EN PENDIENTES Y 148/0 EN CORRECCIONES. R.27 CON LAS QUINCE ADJUDICACI
  1b7cf602 VUELTA 146, TAREA 0.d Y ESQUELETO DEL REPORTE: LA APERTURA SELLADA SALE VERDE EXIT 0 CON LOS DIEZ DENTRO, TODOS NACIDOS EN 105fef3d CUYO PADR
  105fef3d VUELTA 146, APERTURA: EL BLOQUE SELLADO CON LOS DIEZ NOMBRES CANONICOS ANTES DE LA PRIMERA OPERACION. HEAD DE APERTURA 446e4aa1 (EL ACTA DE L
```

<!-- FIN COMMITS TALLADOS -->

## 0.d. LA APERTURA SELLADA, VERDE CON LOS DIEZ DENTRO

`python scripts/loop/verificar_apertura_sellada.py --vuelta 146`, **sin ninguna
desviacion declarada**, da **VERDE EXIT 0**. La nomina, pegada de
`SALIDA_V146_0D_APERTURA_SELLADA.txt`:

```
   SALIDA_V146_CICLO_ETIQUETAS_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_CICLO_NUMSTAT_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_CICLO_SYNC_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_CONTEO_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_DESFASE_CALIBRADO_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_GATE0_CMD1_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_HEAD_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_MOTOR_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_TSC_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
   SALIDA_V146_WEB_APERTURA.txt -- nacido en 105fef3d, padre 446e4aa1
```

Todas nacen en `105fef3d`, **cuyo padre es `446e4aa1`, el commit del acta 145**. **La
leccion del discutible 13 se aplico de antemano**: ninguna otra salida de la vuelta se
llama `SALIDA_V146_*_APERTURA.txt`, y el bloque de apertura fue **un solo commit**.

## 1. LOS REGISTROS, LOS TRES POR ADICION PURA

**1.a. R.27 en `docs/PENDIENTES.md`.** Las **quince** adjudicaciones del acta 145
(3.1 a 3.15, con la 3.14 y la 3.15 como respuestas a mis dos preguntas), **mi caida
4.1** con el motivo escrito (**de reporte, y ACUMULA porque vive en una conclusion**),
**la 4.2 de la casa** (la regla 9 de `EJECUTOR.md` sin guarda que la haga morder) y
**las dos del auditor** (4.3 y 4.4, las dos de encargo). Y **las dos rachas con su
estado nuevo y su motivo**: cifra publicada **sigue en cero**, reporte **sube de uno a
dos**, y por `AUDITOR.md` 1.2 eso obliga a la escalada, que es la TAREA 2.

**1.b y 1.c. CORRECCION 23 y CORRECCION 24 en `docs/plan/CORRECCIONES_A_APLICAR.md`,
por adicion.** El numstat de los dos ficheros, pegado de
`SALIDA_V146_1_NUMSTAT_REGISTROS.txt`:

```
150	0	docs/PENDIENTES.md
148	0	docs/plan/CORRECCIONES_A_APLICAR.md
```

**Anadidas a la izquierda, borradas a la derecha: adicion pura en los dos, cero
borrados.** `docs/plan/OPERACIONES.jsonl` **no se toco en esta tarea**.

**LO QUE MIDO YO, Y NO COPIO.** La CORRECCION 23 lleva **mi medicion de hoy** de las
cuatro cosas que el acta 145 afirma, y **cuadro con ella en las cuatro**: los tres
nombres candidatos no estan en el indice de git, `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`
si esta y trae la tabla de grafias, la ficha de `OP-S-11` dice `estado: HECHA` con
`fecha_corte 2026-08-29`, y `verificar_fuente_canonico.py` me sale **VERDE**. La
CORRECCION 24 lleva las seis cifras de la ficha de `OP-A-01` recomputadas sobre el
grafo de su corte, y **tambien cuadro con el acta en las seis**. Estan en la seccion 3
con sus bloques pegados.

## 2. LA ESCALADA: LA AFIRMACION DE AUSENCIA YA MUERDE

**LO QUE SE CONSTRUYE Y POR QUE SON DOS PIEZAS Y NO UNA.**
`scripts/loop/verificar_ausencias_del_reporte.py` es la guarda; **una guarda que exige
algo que nadie sabe producir es un muro, no una guarda**, asi que nace con ella
`scripts/loop/barrer_ausencia.py`, el instrumento que produce el barrido con su sello.
Las dos con **nombre estable, sin numero de vuelta**, como `tallar_cabecera_reporte.py`
y `verificar_cifras_del_reporte.py`.

**2.a. EL CONTRATO, ESCRITO EN EL DOCSTRING Y NO ADIVINADO.** El vocabulario de
disparo va **cerrado y declarado**, y se pega aqui **citado del propio codigo**, no
retecleado, para que la guarda pueda comprobarlo contra el blob de su fichero:

<!-- CITA CONGELADA HEAD:scripts/loop/verificar_ausencias_del_reporte.py -->
```
    no existe / no existen / no hay ningun / no hay ninguna
    hallados: NINGUNO / hallado: NINGUNO / no se hallo / no se halla
    no esta en el repositorio / NO INSTALADO / NO INSTALADOS
    PRERREQUISITO CUMPLIDO: NO
```
<!-- FIN CITA CONGELADA -->

Y **que cuenta como barrido exhaustivo**: el fichero citado tiene que traer las **cinco**
piezas del sello (la marca `BARRIDO EXHAUSTIVO`, `PREGUNTA:`, `UNIVERSO:`, `CARDINAL:`
mayor que cero y `POR CONTENIDO:`). **La quinta es la que mas importa: es exactamente
la pierna que faltaba el dia de la caida.** Una busqueda por NOMBRE contra candidatos
tecleados no puede hallar un fichero que se llama por su operacion duena.

**Y HAY UN ROJO CON NOMBRE PROPIO:** si el fichero citado trae `candidatos mirados:` y
no trae la marca del barrido, la guarda cae **nombrando ese patron**, porque es
literalmente el metodo de la caida de la 145.

**2.b, 2.c Y LOS DOS QUE ANADO. CUATRO CASOS Y LOS CUATRO MUERDEN**, todos leyendo la
salida real del proceso y **ninguno comparando un literal consigo mismo**. El caso que
manda corre sobre **sujeto congelado de verdad**, `a9b638ba:docs/loop/REPORTE.md`, el
reporte de la 145 tal como se commiteo. Pegado de
`SALIDA_V146_2B_MUTACION_AUSENCIAS.txt`:

```
  A caso rojo sobre el reporte congelado de la 145               OK
  B caso verde con barrido sellado detras                        OK
  C el sello del barrido muerde, no solo la falta de cita        OK
  D la cita congelada se comprueba contra su ref                 OK

CASOS QUE MUERDEN: 4 de 4
```
Contado de `SALIDA_V146_2B_MUTACION_AUSENCIAS.txt`.

**EL CASO (A), QUE ES EL QUE EL ENCARGO PIDE:** la guarda sobre el reporte congelado
sale **EXIT 1** y **nombra la afirmacion de la 3.c**. La linea que imprime, pegada de
esa misma salida:

```
AUSENCIA SIN BARRIDO: 'MOTIVO: no existe en el repositorio ninguna lista canonica de libros con sus' (dispara por no existe) no cita ningun SALIDA_V<N>_*.txt en su ventana
```
Contado de `SALIDA_V146_2B_MUTACION_AUSENCIAS.txt` y respaldada por `SALIDA_V146_3A_BARRIDO_LISTA_CANONICA.txt`.

**LOS DOS QUE ANADO Y EL ENCARGO NO PEDIA, con su motivo.** (C) prueba que **el SELLO
muerde y no solo la falta de cita**: la misma frase citando un fichero que existe y no
es barrido cae nombrandolo. Sin el, la guarda podria estar aprobando cualquier cita.
(D) prueba que **la cita congelada no es un interruptor**, que es la leccion de la
vuelta 135: un reporte que documenta la caida tiene que poder citarla, y por eso hay
un bloque de CITA CONGELADA que lleva su ref y su ruta en la propia marca; **la guarda
lee el blob de ese ref con `git show` y exige que cada linea citada este verbatim
dentro**. Texto inventado
dentro del bloque cae; la contraprueba con la linea real, **elegida por computo**,
pasa.

**2.d. LA FRONTERA, ESCRITA EN EL DOCSTRING.** Esta guarda **no decide si la cosa
existe: decide si la AFIRMACION esta respaldada**. Y **no entra en ninguna columna de
`tallar_estado_de_fase.py`**, por la misma razon de unidades de la adjudicacion 3.9 del
acta 144 y de la CORRECCION 18.

**2.e. ENTRA EN `VIEJAS`, CON SUJETO CONGELADO**, por la regla con la coletilla de la
CORRECCION 22. La bateria pasa de diecinueve a veinte y sale **VERDE**, pegado de
`SALIDA_V146_2_VIEJAS_TRAS_TAREA2.txt`:

```
  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)

VERDE: las 20 mutaciones viejas corren, muerden, y sus salidas selladas salen IDENTICAS en dos corridas seguidas.
```
Contado de `SALIDA_V146_2_VIEJAS_TRAS_TAREA2.txt`.

**EL CICLO DE GATE 0 CON LAS SUITES DETRAS, AL CERRAR LA TAREA 2:** Gate 0 **OK**
(`SALIDA_V146_2_GATE0_TRAS_TAREA2.txt`), numstat del ciclo **sin una fila**
(`SALIDA_V146_2_CICLO_NUMSTAT.txt`), motor **25/25**
(`SALIDA_V146_2_MOTOR_TRAS_TAREA2.txt`), vitest **verde**
(`SALIDA_V146_2_WEB_TRAS_TAREA2.txt`) y tsc **EXIT 0 sin contenido**
(`SALIDA_V146_2_TSC_TRAS_TAREA2.txt`).

## 3. LA FASE 07 SE EJECUTA

### 3.a. EL PRERREQUISITO, RELEIDO AL DOBLE Y CON EL BARRIDO BUENO

**Esto es lo que toda caida de reporte dispara**, y se hace **con el barrido de la
TAREA 2 y no con tres nombres de fichero**. Pegado de
`SALIDA_V146_3A_BARRIDO_LISTA_CANONICA.txt`:

```
  PREGUNTA: existe en el repositorio una lista canonica de libros con sus alias de escritura, que es el prerrequisito que OP-A-01 nombra
  UNIVERSO: git ls-files de la rama actual (todo lo versionado, sin acotar)
  VEREDICTO: HALLADO
      docs/plan/OP_S_11_MAPEO_PROPUESTO.md  [nombre y contenido]
```
Pegado de `SALIDA_V146_3A_BARRIDO_LISTA_CANONICA.txt`. El universo barrido:

```
CIFRA ficheros del universo: 15135 ficheros
```
Contado de `SALIDA_V146_3A_BARRIDO_LISTA_CANONICA.txt`. Y la pierna POR CONTENIDO, la
que faltaba el dia de la caida y la que halla la lista:

```
CIFRA ficheros que coinciden por contenido: 51 ficheros
```
Contado de `SALIDA_V146_3A_BARRIDO_LISTA_CANONICA.txt`.

**LA LISTA APARECE POR LAS DOS PIERNAS**, y las tres rutas que la 145 miro a mano
salen en el mismo fichero, bajo el rotulo que dice en voz alta que **no son el
barrido**. La ficha de su duena, leida hoy y pegada de
`SALIDA_V146_3A_FICHA_OP_S_11.txt`:

```
estado: HECHA
fecha_corte: 2026-08-29
bloquea_a: ['OP-A-01', 'OP-A-02']
```

Y la guarda del criterio de HECHO, corrida por mi en esta vuelta, pegada de
`SALIDA_V146_3A_FUENTE_CANONICO.txt`:

```
CIFRA nodos vivos comprobados: 3169 nodos
```
Contado de `SALIDA_V146_3A_FUENTE_CANONICO.txt`, cuya linea de veredicto dice **VERDE
EXIT 0**: todos traen `fuente` presente, con al menos una declaracion, y **todas sus
declaraciones son canonicas de la tabla**.

> **EL PRERREQUISITO DE `OP-A-01` ESTA CUMPLIDO Y LO DECLARO ASI. NO HAY PARADA.**

**LO QUE LA 145 PUBLICO, CITADO Y NO ESCONDIDO**, porque una correccion que tapa lo
que corrige no se puede auditar. Verbatim del blob de su commit:

<!-- CITA CONGELADA a9b638ba:docs/loop/REPORTE.md -->
```
     hallados: NINGUNO
  PRERREQUISITO CUMPLIDO: NO
  MOTIVO: no existe en el repositorio ninguna lista canonica de libros con sus
```
<!-- FIN CITA CONGELADA -->

**Y EL APOYO POSITIVO QUE ESTABA INVERTIDO.** La 3.c dijo que la grafia vieja vive del
lado deprecado *"o sea que nada la esta normalizando"*. **Es al reves**, y lo mide mi
instrumento: la guarda canonica **solo obliga a los vivos**, asi que una grafia vieja
que sobrevive unicamente entre deprecados es la firma de una normalizacion
**consumada**. Las cifras van en la 3.f.

### 3.b. `OP-A-01` EJECUTADA, Y SU ALCANCE SON SUS TRES ENTRADAS

**LA SIMULACION PREVIA, SOBRE COPIA EN MEMORIA Y ANTES DE TOCAR NADA**, pegada de
`SALIDA_V146_3B_SIMULACION_ANTES.txt`:

```
CIFRA nodos vivos con mas de una fuente: 8 nodos
```
Contado de `SALIDA_V146_3B_SIMULACION_ANTES.txt`. Ninguno se queda sin pasos:

```
CIFRA nodos con mas de un libro y sin pasos: 0 nodos
```
Contado de `SALIDA_V146_3B_SIMULACION_ANTES.txt`. Y el campo ya resolvia limpio antes
de cablear nada:

```
CIFRA incumplimientos canonicos: 0 nodos
```
Contado de `SALIDA_V146_3B_SIMULACION_ANTES.txt`.

**LA NOMINA ADJUDICADA SE GENERA, NO SE TECLEA.**
`dataset/metadata/aduana_fuente_multiple.json` sale de leer el catalogo en esta
corrida, con su `fecha_corte` leida de git. Pegado de
`SALIDA_V146_3B_NOMINA_SELLADA.txt`:

```
  fecha_corte leida de git: 2026-09-02
CIFRA nodos adjudicados con mas de una fuente: 8 nodos
```
Contado de `SALIDA_V146_3B_NOMINA_SELLADA.txt`.

**LO QUE LA NOMINA NO DICE, escrito dentro del propio fichero:** no dice que el
reparto de material de esos nodos este adjudicado por lectura. Dice que **son los que
habia al cablear el control**, con su corte. La aduana garantiza que la lista **no se
mueva en silencio**, no que la lista sea buena. Y **re-sellarla es re-adjudicar**: no
se regenera para hacer callar a Gate 0.

**LOS TRES CONTROLES, CABLEADOS A `step7_validate` DE `scripts/run_phase1.py`:**

1. **La comprobacion posicional** (`BANCO_DEL_PLAN.md` P.2): todo nodo vivo con mas de
   una declaracion se coteja contra la nomina **entera y en orden**, para que anadirle
   en silencio un segundo libro a un nodo ya adjudicado caiga igual que un nodo nuevo.
   Es literalmente *"impedir que entre el sesenta y ocho"*.
2. **El campo `fuente` contra la lista canonica.** **No se reimplementa nada**: se
   llama a `verificar_fuente_canonico.verificar`, que ya es el criterio de HECHO de la
   fase 08. Dos versiones de la misma comprobacion serian la averia de los dos
   `master_graph` que el chequeo de gemelos vino a curar.
3. **El segundo libro y los pasos, LA MITAD SANA.** Un nodo con mas de un libro y sin
   ni un `pasos_accionables` **no puede** tener un paso donde aparezca su segundo
   libro: es mecanico y no da falsos rojos.

**LA OTRA MITAD DE LA ENTRADA 3 NO SE INSTALA, Y SE DICE POR QUE.** Atribuir el
MATERIAL de un paso concreto a un libro pide una atribucion POR PASO que el esquema
**no tiene**, y el barrido exhaustivo lo sella con su pierna por contenido en cero:

```
CIFRA ficheros que coinciden por contenido: 0 ficheros
```
Contado de `SALIDA_V146_3B_BARRIDO_ATRIBUCION_PASO.txt`. **No se adivina**
(`EJECUTOR.md` 11) y no se fabrica una heuristica de parecido, que decidiria por
semejanza lo que solo decide una lectura. **PENDIENTE DE DOCTRINA.**

### 3.c. LA GUARDA CANONICA, CABLEADA A GATE 0: EL CONTROL A2.4

Estaba escrita, salia verde y **no corria dentro de Gate 0**, o sea que nada impedia
que entrara manana un nodo con una grafia fuera de la tabla. **Hoy corre.** Es la
adjudicacion 3.15 aplicada: *"`OP-A-02` no los posee: los exige CORRIENDO"*, y Gate 0
es la puerta.

**LAS CUATRO MUTACIONES, SOBRE VARIABLE COMPUTADA Y COPIA EN MEMORIA.** Los sujetos se
eligen **por computo**, no se teclean. Pegado de
`SALIDA_V146_3C_MUTACION_ADUANA.txt`:

```
CONTRAPRUEBA, SIN MUTAR NADA: los tres checks salen OK: True
A nodo nuevo con dos libros sin adjudicar                        VEREDICTO: OK
B tercer libro anadido en silencio a uno ya adjudicado           VEREDICTO: OK
C grafia fuera de la tabla canonica (control A2.4)               VEREDICTO: OK
D segundo libro sin ni un paso                                   VEREDICTO: OK
dataset/ IDENTICO antes y despues (cero escrituras): True
CASOS QUE MUERDEN: 4 de 4
VEREDICTO GLOBAL: VERDE
```
Contado de `SALIDA_V146_3C_MUTACION_ADUANA.txt`.

**`dataset/` sin tocar antes ni despues**, y **la igualdad la comprueba el propio
arnes** con `git status --porcelain -- dataset/` a los dos lados: forma parte de su
veredicto, no es una promesa de la prosa.

### 3.d. LA VARA DE LA FASE 07, RE-CORRIDA, Y UNA REPARACION QUE NO ESTABA PEDIDA

El recuento nuevo, pegado de `SALIDA_V146_3D_VARA_FASE07.txt`:

```
  OP-A-01: 3 control(es) declarado(s) | EXISTEN 3 | MUERDEN 3 | INSTALADOS Y MORDIENDO 3
  OP-A-02: 6 control(es) declarado(s) | EXISTEN 5 | MUERDEN 5 | INSTALADOS Y MORDIENDO 5
     A2.6  NO INSTALADO
```
Contado de `SALIDA_V146_3D_VARA_FASE07.txt` y respaldado por `SALIDA_V146_2C_BARRIDO_VERDE.txt`.
Es la adjudicacion 3.9 atendida: un veredicto de control ausente es una busqueda
negativa y pasa por la guarda de la TAREA 2 como cualquier otra.

```
CIFRA controles declarados: 9 controles
CIFRA controles instalados y mordiendo: 8 controles
LA FASE NO SE CIERRA CONTRA ESTA VARA, y lo que le falta va nombrado: A2.6.
```
Contado de `SALIDA_V146_3D_VARA_FASE07.txt` y de `SALIDA_V146_3D_ESTADO_FASE07.txt`, que es la OTRA unidad, la de grafo, y sigue diciendo `sin cumplir: 2`: son `OP-A-01` y `OP-A-02`, las dos por `SIN VARA ESCRITA`.
**Las dos unidades no se mezclan**, por la frontera de la adjudicacion 3.9 del acta 144:
una mide CODIGO INSTALADO y la otra DESTINO CONTRA EL GRAFO.

**LA CIFRA QUE PUBLICO NO ES LA QUE EL ENCARGO ANTICIPA, Y LO DIGO CON SU MOTIVO.** El
encargo dice *"tu vara tiene que pasar de TRES a CUATRO instalados y mordiendo, y ESA
es la cifra que publicas"*. **Publico ocho, que es lo que el instrumento mide**, por
`EJECUTOR.md` 2. La razon es aritmetica y no un desacuerdo: el encargo cuenta **solo
el efecto de la 3.c**, y la 3.b instala ademas la comprobacion posicional, que **cuenta
dos veces** porque A1.1 y A2.3 son el mismo control con dos nombres, e igual pasa con
A1.2 y A2.4. **Marcado como discutible.**

**LA REPARACION QUE NO ESTABA PEDIDA Y QUE NO PODIA CALLARSE.** Al re-correr la vara
descubri que **sus propias sondas de A1.2 y A2.4 eran cinco rutas tecleadas a mano que
no existen**: `dataset/metadata/libros_canonicos.json`,
`dataset/metadata/fuentes_canonicas.json` y `docs/plan/LIBROS_CANONICOS.md`, las mismas
tres del barrido sellado en `SALIDA_V146_3A_BARRIDO_LISTA_CANONICA.txt`. **Es el metodo
exacto que la CORRECCION 23 acaba de prohibir, dentro del instrumento que yo escribi la
vuelta pasada.** Y la sonda de A2.3 buscaba un literal que solo vivia en la frase de la
ficha: **medir la ficha en vez de la instalacion**. Las sondas nuevas miran **lo que el
control es**, el rotulo del check cableado. **El texto viejo no se borra**: queda
escrito al lado, en el codigo, con su motivo.

**Y UNA SEGUNDA, DE LA MISMA ESPECIE:** la cola de la vara imprimia una frase FIJA,
*"LA FASE NO SE CIERRA HOY Y NINGUNA DE LAS DOS OPERACIONES SE EJECUTA"*, cierta el dia que se escribio y falsa en cuanto esta vuelta ejecuto OP-A-01, y la vara de grafo `SALIDA_V146_3D_ESTADO_FASE07.txt` sigue con `sin cumplir: 2`: `OP-A-01` y `OP-A-02`. **Una linea de
veredicto que no depende de lo que el instrumento acaba de medir es una cifra
tecleada.** Ahora se computa de la tabla y nombra lo que falta.

**LA GUARDA DE CITAS DE LA VARA SIGUE VERDE** tras los cambios: las nueve frases
literales siguen apareciendo verbatim en su ficha, y eso se comprueba en cada corrida.

### 3.e. LA PUERTA SEMANTICA `A2.6`: NO SE EJECUTA, QUEDA ESCRITA Y ACOTADA

**No se ejecuta en esta vuelta**, como el encargo manda. Lo que dejo acotado:

- **EL PUNTO DE INSERCION, NOMBRADO:** `scripts/integrar_packs.py`, funcion
  `paso_a_integrar_nodos_y_puentes`, en el `shutil.copy2(archivo, destino)` que copia
  cada nodo de un pack a `dataset/nodos/`. **Ese es el momento en que un nodo ENTRA**,
  y es donde el bloqueo por veredicto ausente tiene que vivir. **No en
  `step7_validate`**: Gate 0 valida el grafo entero despues, y para entonces el nodo ya
  entro.
- **EL UMBRAL, CITADO DE SU FICHA Y NO INVENTADO:** la `evidencia` de `OP-A-02` dice
  *"el umbral de la cola es el mismo del cribado intra, o sea que la aduana usa la vara
  que el archivo ya uso 2.117 veces"*, y `07_ADUANA.md` lo repite: *"el umbral no es
  nuevo: es el de la cola"*. **LA FICHA NO DA UN NUMERO**, y **no lo adivino**: el
  barrido exhaustivo lo sella con su pierna por contenido en cero, y **va como
  pregunta**.

```
CIFRA ficheros que coinciden por contenido: 0 ficheros
```
Contado de `SALIDA_V146_3E_BARRIDO_UMBRAL.txt`.
- **EL MECANISMO, CITADO:** correr el indice semantico contra **su dominio y el
  nucleo**; si algun vecino supera el umbral, la insercion **se bloquea**; se desbloquea
  con el veredicto continua-o-repite **citando el id del vecino**. *"Nunca bloquea por
  parecido. Solo por VEREDICTO AUSENTE."* Y la salida que no vale, escrita para que no
  se use: **bajar el umbral**.

### 3.f. LA TRUNCACION A 31 CARACTERES: MEDIDA Y DECLARADA, NO RESUELTA

**La regla del barrido, escrita antes de correrlo:** se parte cada grafia por ` - ` en
(titulo, autor); una pareja entra si **los dos traen autor**, el autor es **identico**
y un titulo es **prefijo estricto** del otro. Pegado de
`SALIDA_V146_1C_CIFRAS_FICHA.txt`:

```
   'Essentials of Supply Chain Mana - Michael H. Hugos' [titulo 31 car] vivos=0 depre=1
   'Essentials of Supply Chain Management - Michael H. Hugos' [titulo 37 car] vivos=95 depre=20
   'The Hard Thing About Hard Thing - Ben Horowitz' [titulo 31 car] vivos=0 depre=5
   'The Hard Thing About Hard Things - Ben Horowitz' [titulo 32 car] vivos=87 depre=1
```
Pegado de `SALIDA_V146_1C_CIFRAS_FICHA.txt`. Las parejas de hoy:

```
CIFRA parejas titulo-prefijo con el mismo autor WORK: 2 pares
```
Contado de `SALIDA_V146_1C_CIFRAS_FICHA.txt`. Las del grafo del corte:

```
CIFRA parejas titulo-prefijo con el mismo autor 0e5e0c60: 3 pares
```
Contado de `SALIDA_V146_1C_CIFRAS_FICHA.txt`. Y la OTRA unidad, la que el acta no mide:

```
CIFRA grafias con titulo de 31 caracteres WORK: 10 grafias
```
Contado de `SALIDA_V146_1C_CIFRAS_FICHA.txt`.

**COINCIDO CON EL ACTA EN LAS DOS DE HOY**, con sus longitudes y con sus ceros de nodos
vivos. **Traigo una tercera que el acta no nombra**, la de Tim Brown (`Change by
Design` contra `Change by Design, Revised and U`), que existia en el corte y hoy ya no.

> **Y AQUI VA MI UNICA DISCREPANCIA DE FONDO CON EL ACTA 145, DECLARADA Y NO COPIADA.**
> El acta dice que las dos son *"LAS DOS UNICAS DEL CATALOGO"*. **Es cierto de las
> PAREJAS y falso de las TRUNCACIONES**, y son dos unidades distintas. Un barrido por
> parejas **solo ve una truncacion cuando la forma larga tambien vive en el catalogo**;
> una grafia recortada cuyo original nadie escribio nunca es invisible para el. Censado
> con la otra unidad, hay diez grafias de titulo exactamente 31, y **ocho estan VIVAS y
> son CANONICAS de la tabla de `OP-S-11`**. **La truncacion a 31 no esta resuelta:
> esta HORNEADA EN LA TABLA CANONICA.**

**NO LAS TOCO.** La verificacion 2 de `OP-S-11` dice *"ninguna grafia truncada
sobrevive"*, y **se cumple sobre los vivos, que es el alcance de su guarda, y no se
cumple contando deprecados**. Es pregunta para el auditor, no operacion para mi.

### 3.g. NI UNA ARISTA SE MOVIO, ASI QUE NO HAY NADA QUE PARAR

La condicion sigue viva y **no se disparo**: la fila de aristas movidas de la cabecera
tallada dice **+0 / +0 / +0 / +0**, el censo de apertura y el de cierre dan las mismas
cuatro cuentas, y el numstat del ciclo no trae una fila
(`SALIDA_V146_CICLO_NUMSTAT_CIERRE.txt`). **Esta vuelta instala CONTROLES; no escribe
ni retira una sola flecha.** Lo unico que entra en `dataset/` es un fichero de
metadata, la nomina de la aduana.

### 3.h. EL CAMPO `estado` NO SE MUEVE, Y ESTE ES EL MOTIVO

El encargo permite mover `OP-A-01` **"solo por haberla ejecutado con su criterio de
HECHO cumplido"**. **No lo esta del todo, y prefiero decirlo a publicar un verde
falso.** Sus entradas 1 y 2 estan instaladas y muerden; **la entrada 3 solo en su mitad
sana**, porque la otra mitad pide un dato que el esquema no tiene. El criterio de la
fase 08 es *"una fase esta HECHA cuando su verificacion se caeria si el fallo
volviera"*, y **el fallo semantico de la entrada 3 no haria caer nada hoy**. Asi que
`docs/plan/OPERACIONES.jsonl` **queda sin tocar en toda la vuelta** y `OP-A-01` sigue
`LISTA`. **Marcado como discutible**, con su alternativa dicha: moverla a HECHA seria
defendible si el auditor lee la entrada 3 como cumplida por su mitad mecanica.

El pase del par 1190 fuera de congelados **sigue sin aplicarse**. `OP-S-12` sigue al
final de la pasada entera.

## 4. EL CIERRE

**4.a.** La bateria del lado CIERRE, **los mismos diez nombres**, y
`SALIDA_V146_HEAD_CIERRE.txt` sellado **tras la ultima operacion** y **antes** de
escribir el hash en este reporte.

**4.b.** `tallar_cabecera_reporte.py --vuelta 146 --fase04` corrido, su tabla pegada
entera entre las dos marcas, y sus dos comparaciones **verdes**: ver
`SALIDA_V146_4B_COMPARAR_CABECERA.txt` y `SALIDA_V146_4B_COMPARAR_COMMITS.txt`.

**4.c.** `verificar_cifras_del_reporte.py` corrido **sobre este mismo reporte** antes
de commitearlo, y **una segunda vez despues de pegar su linea**, para comprobar que
reproduce. La pareja de marcas aparece **exactamente una vez**:

<!-- COBERTURA DE LA GUARDA -->
COBERTURA: 12 cotejadas / 0 exentas / 12 cifras | reparto: 12 POR ETIQUETA, 0 POR CONJUNTO, 0 sin linea CIFRA | de las cotejadas, 0 viven en una FILA DE TABLA | afirmaciones de CIERRE cotejadas contra tallar_estado_de_fase.py: 2 | ficheros citados que NO son UTF-8: 0 [ninguno] | unidades vistas FUERA del vocabulario: 28 palabra(s) [car x4, depre x4, caracteres x2, control x2, controles x2, docs x2, lleva x2, acaba x1, aduana x1, afirma x1, aplicada x1, atendida x1, buscaba x1, cifra x1, eso x1, estaba x1, fuera x1, iba x1, miro x1, mutaciones x1, nombra x1, prohibe x1, publico x1, quedaba x1, tal x1, valida x1, veces x1, veredicto x1]
<!-- FIN COBERTURA DE LA GUARDA -->

**Y LA GUARDA NUEVA SOBRE SI MISMA:** `verificar_ausencias_del_reporte.py` corrida
sobre este reporte, salida en `SALIDA_V146_4C_GUARDA_AUSENCIAS.txt`. **Una escalada que
no se aplica a la pagina que la anuncia no es una escalada.**

**4.d y 4.e.** `verificar_mutaciones_viejas.py` y
`verificar_apertura_sellada.py --vuelta 146` re-corridas **despues** de escribir y
commitear el reporte, porque **el estado al cierre se mide al cierre**. Salidas en
`SALIDA_V146_4D_VIEJAS_TRAS_REPORTE.txt` y
`SALIDA_V146_4E_APERTURA_SELLADA_RECIERRE.txt`.

## 5. CORRECCIONES DECLARADAS DENTRO DE LA PROPIA VUELTA

**5.1. CORRI `run_phase1.py` SUELTO A MITAD DE LA TAREA 3 Y EL CHEQUEO DE GEMELOS
CANTO.** Al cerrar el ciclo de la TAREA 3, Gate 0 salio **FALLIDO** con setenta y un
nodos divergentes entre los dos `master_graph`. **La guarda tenia razon y el defecto
era mio**: recompile sin reaplicar la curaduria despues, o sea que deje el ciclo de
tres a medias. **Es exactamente la trampa que el propio encargo avisa**, citada verbatim de su
fichero:

<!-- CITA CONGELADA HEAD:docs/loop/PROMPT_SIGUIENTE.md -->
```
  el numstat da 72/72 en master_graph.json y parece un rojo que no existe.
```
<!-- FIN CITA CONGELADA -->

**La guarda no se toca**: se corrio el ciclo entero en su orden y volvio a **OK**
(`SALIDA_V146_3_GATE0_TRAS_TAREA3.txt`). **Lo escribo en vez de esconderlo**, y va
marcado como discutible.

**5.2. LA VARA DE LA FASE 07 SE REPARA DENTRO DE LA VUELTA**, y el defecto viejo queda
escrito al lado en el codigo, sin borrar. Esta en la 3.d.

**5.3. LA 4.c ME OBLIGO A TRES CAMBIOS DE INSTRUMENTO, Y LOS DECLARO UNO A UNO.** Al
correr las dos guardas sobre esta misma pagina salieron rojas, y **el remedio fue citar
y publicar, nunca reescribir hasta que no encontraran nada**. (1) `barrer_ausencia.py`
no publicaba sus dos piernas en forma contable: ahora imprime una linea `CIFRA` por
pierna, porque una cifra que la guarda no puede contar es una cifra sin fichero. (2)
`verificar_fuente_canonico.py` no publicaba su cifra de nodos vivos: ahora si, y **su
veredicto no cambia**. (3) La cola de la vara de la fase 07 iba partida en dos frases y
la cita no cabia en la ventana de tres: ahora va en una. **NINGUNO DE LOS TRES CAMBIA
UN VEREDICTO**, y los tres estan escritos en el codigo con su motivo.

**5.4. Y UN HUECO REAL DE MI GUARDA NUEVA, HALLADO POR ELLA MISMA SOBRE ESTA PAGINA.**
`verificar_ausencias_del_reporte.py` recortaba el bloque de commits tallados pero **no
la cabecera tallada**, y la celda de identidad de la cabecera trae el ASUNTO DEL COMMIT
DEL ACTA leido de `git log`, que puede contener cualquier formula del vocabulario sin
ser una afirmacion de quien escribe. **Se anade la cabecera al recorte, con su motivo
escrito**, y no la debilita: `tallar_cabecera_reporte.py --comparar` ya exige que ese
bloque sea IDENTICO AL TALLADOR, o sea que ahi no cabe una frase propia.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

1. **PUBLICO OCHO Y EL ENCARGO ANTICIPABA CUATRO.** `EJECUTOR.md` 2 dice que manda el
   instrumento; el encargo dice *"ESA es la cifra que publicas"*. Elegi el instrumento
   y explique la aritmetica. Pudo ser al reves.
2. **NO MUEVO `OP-A-01` A HECHA.** La entrada 3 esta instalada en su mitad sana. Lo
   trato como criterio no cumplido; el auditor puede leerlo como cumplido.
3. **INSTALE LA MITAD SANA DE LA ENTRADA 3 EN VEZ DE DEJARLA ENTERA SIN INSTALAR.**
   Media guarda que muerde de verdad me parece mejor que ninguna, pero hace que la vara
   marque A1.3 como INSTALADO Y MUERDE, que puede leerse como mas de lo que hay.
4. **LA NOMINA ADJUDICADA ES UN FICHERO NUEVO EN `dataset/metadata/`.** Es dato, no
   nodo, y no lo sincroniza `sync_assets_web.py`. Pero es la primera vez que un control
   de la aduana necesita datos propios.
5. **LA NOMINA CONGELA EL ESTADO DE HOY SIN ADJUDICAR SU CONTENIDO.** Los ocho entran
   por estar, no por haberse leido. Lo escribi dentro del fichero, pero es una
   adjudicacion por omision.
6. **LA VENTANA DE LA GUARDA DE AUSENCIAS ES BIDIRECCIONAL** y la de la guarda de
   cifras es forward-only por doctrina adjudicada. Argumente por que (la pregunta es
   binaria y la cita precede al veredicto en esta prosa) y declare lo que se paga: una
   frase podria apoyarse en el barrido del vecino. Lo mitiga `PREGUNTA:` obligatoria.
7. **EL BLOQUE `CITA CONGELADA` ES UNA EXENCION NUEVA.** La hice comprobable contra el
   blob del ref para que no sea un interruptor, pero sigue siendo una puerta que antes
   no existia.
8. **`barrer_ausencia.py` ADMITE `--excluir` Y `--universo-prefijo`.** Los dos acotan
   el universo y los dos se imprimen en el sello, pero acotar un universo es debilitar
   un barrido, y el que decide el recorte soy yo.
9. **EL `VEREDICTO` DEL BARRIDO PUEDE DECIR HALLADO POR LA PIERNA EQUIVOCADA.** En la
   3.e y en la 3.b el veredicto sale HALLADO por coincidencias de NOMBRE ajenas a la
   pregunta, y lo que sostiene la ausencia es la pierna POR CONTENIDO en cero. Lo digo
   en la prosa, pero el instrumento deberia saber decirlo solo.
10. **REPARE LA VARA DE LA 145, QUE NO ESTABA EN EL ENCARGO.** Sus sondas eran el
    metodo que la CORRECCION 23 prohibe. Podia haberlo dejado escrito como hallazgo sin
    tocar el instrumento.
11. **CAMBIE LA COLA DE LA VARA, QUE ERA PROSA Y NO CIFRA.** Es una linea de veredicto,
    no una celda, y ampliar la doctrina de "la cifra se talla" a la prosa de veredicto
    es cosa mia.
12. **EL VOCABULARIO DE AUSENCIAS TIENE DOCE FORMULAS Y LO ELEGI YO.** El encargo me
    dejaba elegirlo; no probe cuantas afirmaciones de ausencia reales se le escapan.
13. **CORRI `run_phase1.py` SUELTO Y ME PUSE LA 0.d EN RIESGO.** Fue error mio, lo
    corregi dentro de la vuelta y lo escribo, pero es procedimiento.

## 7. PENDIENTES DE DOCTRINA

**7.1. LA MITAD SEMANTICA DE LA VERIFICACION 3 DE `OP-A-01`.** Decidir si el material
de un paso viene del segundo libro pide una atribucion por paso que el esquema no
tiene. Registrado en el codigo de Gate 0, en la vara y aqui.

## 8. PREGUNTAS PARA EL AUDITOR

**PREGUNTA 1. LA TRUNCACION A 31 ESTA HORNEADA EN LA TABLA CANONICA.** Ocho grafias
vivas y canonicas de `OP_S_11_MAPEO_PROPUESTO.md` tienen el titulo cortado a 31. La
verificacion 2 de `OP-S-11` se cumple sobre vivos y no contando deprecados. **La mido,
la digo y la dejo:** que hago con ella no es decision mia.

**PREGUNTA 2. EL UMBRAL DE LA COLA NO TIENE NUMERO EN NINGUNA PARTE.** `OP-A-02` lo
cita por referencia y el barrido no halla ninguna constante que lo fije. Sin ese numero
la puerta semantica no se puede cablear. **Cual es, y de donde se lee.**

**PREGUNTA 3. LA VARA CUENTA NUEVE CONTROLES Y HAY SIETE DISTINTOS.** A1.1 y A2.3 son
el mismo control, y A1.2 y A2.4 tambien. La vara los cuenta por separado porque cada
ficha los declara. **Es la unidad correcta o hay que publicar las dos.**
