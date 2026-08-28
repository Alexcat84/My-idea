# REPORTE DE LA VUELTA 98 (EJECUTOR)

Rama `pasada-unica`. Fase III, fase 04 ENLACES. Sobrescribe el reporte de la vuelta 97.

**ESTE REPORTE VA EN MODO AUSTERO AUNQUE TODAVIA NO LE TOQUE, y lo digo yo para que
nadie tenga que adivinarlo.** La decision del fundador (commit `d2c565ca`, leido de
git en esta vuelta) dice *"vigente desde la proxima vuelta"*, y entro **a mitad de
esta**, con la apertura ya sellada: por la letra, aplica desde la **99**. Lo adopto
**una vuelta antes y de forma voluntaria** porque el austero *"recorta tinta, no
control"* y ninguna guarda, tallador, simulacion ni mutacion se toca. Si el auditor
prefiere el regimen completo para esta vuelta, la prosa que falta esta entera en los
mensajes de los seis commits.

## CABECERA TALLADA (`--fase04 --vuelta 98`), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 98`. Salida
en `docs/loop/SALIDA_V98_CABECERA_TALLADA.txt`, **EXIT 0**. Ninguna celda tecleada.

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `19a8f95e` (ACTA DE LA VUELTA 97 DEL AUDITOR, leido de git log), HEAD real de apertura `19a8f95e` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `19a8f95e` (ACTA DE LA VUELTA 97 DEL AUDITOR, leido de git log), HEAD real de apertura `19a8f95e` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE** |

**UN COMMIT DEL FUNDADOR ENTRO A MITAD DE LA VUELTA**, entre `395a1524` y `752f39a6`:
`d2c565ca`, el modo austero. **Toco dos ficheros y los dos son de `docs/loop/`**
(`git show --stat`), **cero de `dataset/`**, asi que no mueve ninguna celda de arriba.
Se dice porque es el hueco que la vuelta 80 dejo documentado.

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION Y SE MIDIO DOS VECES**, y la
sellada es la segunda: la primera corrida del ciclo de tres salio en **cp1252** (44
bytes no-ASCII, UTF-8 invalida en el byte 6412) y se repitio entera con
`PYTHONIOENCODING=utf-8` **antes de sellar nada**. El fichero commiteado es UTF-8
valida de nacimiento (88 bytes no-ASCII, 312 lineas). Las dos corridas dan el mismo
texto (`a.decode('cp1252') == b.decode('utf-8')` da `True`). **Es el remedio en la
fuente de la caida 4.2 del acta 97, no un parche despues.**

## EL MARCADOR Y LA TASA, REMEDIDOS AL CIERRE

`python scripts/recomputar_marcador.py 3388`, salida en
`docs/loop/SALIDA_V98_MARCADOR_CRIBADO_CIERRE.txt`, **EXIT 0**. Cifras contadas de ese
fichero: `n = 3388 corte = 3388 huecos: [] dups(puesto): 0`, pares duplicados 0.
**MARCADOR GLOBAL: A 551 (16,3) / B 72 (2,1) / C 5 (0,1) / D 2.760 (81,5).**
**TASA POR DOMINIO:** compras 155/1 (0,6), core 1.445/325 (22,5), entrega 171/2 (1,2),
environmental 170/28 (16,5), exportacion 130/15 (11,5), franquicias 148/15 (10,1),
health_safety 192/43 (22,4), quality 844/119 (14,1), risk_management 106/0 (0,0),
seguridad_digital 27/3 (11,1). **NI EL MARCADOR NI LA TASA SE MUEVEN**, verificado:
`git diff --stat` de `INTRA_DOMINIO_PARES.jsonl` y `INTRA_DOMINIO_VEREDICTOS.jsonl`
da **VACIO** (`docs/loop/SALIDA_V98_TAREA4_CINCO_PUNTOS.txt`).

## LO QUE PASO, POR TAREA. Cada cifra con su fichero

**TAREA 1, LA FECHA. LA SERIE NO ERAN DOS: SON SEIS, Y TRES MAS EN OTRO FICHERO.**
`vuelta98_tarea1_fechas_addenda.py --medir` recorre los **8** addenda de
`OPERACIONES.jsonl` y coteja cada fecha contra `git log`
(`SALIDA_V98_TAREA1_FECHAS_MEDIR.txt`): **6 IMPOSIBLE, 1 CALZA, 1 SIN FECHA**. Techo
del reloj del repo: **2026-08-27**. Las seis son las vueltas 88, 89, 90, 91, 94 y 97;
la unica buena es la 96. En `04_ENLACES.md`, con el instrumento hermano
(`..._ENLACES_MEDIR.txt`): **3 IMPOSIBLE y 9 CALZA** de 12 marcadores, y las nueve
buenas son de las vueltas 57 a 82, o sea que **la especie esta acotada a las vueltas
88 a 97** y eso se mide, no se supone. **Las nueve corregidas sin borrar una letra.**
Aditividad probada **caracter a caracter y no por `numstat`**
(`SALIDA_V98_TAREA1_ADITIVIDAD.txt`, EXIT 0): 4 notas tocadas, unico campo cambiado
`nota`, **cero** campos de decision movidos. **LA FUENTE, ARREGLADA**: la constante
`MARCA` ya no lleva fecha tecleada, la lee de `git`.

**TAREA 2, LOS REGISTROS DEL ACTA 97.** En `docs/PENDIENTES.md`. Composicion tallada
(`SALIDA_V98_TAREA2_COMPOSICION.txt`, EXIT 0): **1 seccion de nivel 2 y 5 de nivel 3**,
6 filas casadas; **181 anadidas, 0 borradas** (`..._TAREA2_NUMSTAT.txt`). **El caso
positivo se commitea con su fichero** (`..._TAREA2_CASO_POSITIVO.txt`, EXIT 0),
que es lo que a la vuelta 97 le falto: reproduce **1 y 4** sobre el diff de la 96.

**TAREA 3, EL PAR 42: ME SOSTUVE EN A Y ESTABA MAL. SE MUEVE A D.** Lo que no mire:
**la senial de los entregables del `9.6.2`**, que el banco dice que decide mas rapido
que los pasos. La madre entrega un **protocolo de respuesta a incidentes**; el hijo,
un **registro de incidente**, que es lo que el paso 2 de la madre produce al
ejecutarse. Y el residuo no son dos lineas sueltas: el paso 4 del hijo **consume la
salida del 3**. Recomputo en los **tres** sitios del plan con las cifras leidas del
JSONL: **A 3 a A 2, D 56 a D 57**. **La direccion no cambia** (33/27, recontadas) y
**el par 12 sigue en A**, leido de su fichero hoy.

**TAREA 4, `OP-E-03` LLEGA A LA FILA 150 DE 183. NO CIERRA: QUEDAN 33.** Cincuenta
pares leidos con el instrumento de la vuelta 96 **sin tocarle una linea**. Los cinco
puntos **remedidos** (`..._TAREA4_CINCO_PUNTOS.txt`): cribado 3.388/3.388 contadas;
resolutor antes de cruzar y **no movio ningun id en las 83** (83 filas dicen "no", 0
dicen "si", contadas con `grep -c`); 2.796 pares distintos en la cola; marca completa
en las **50** filas, las cuatro banderas contadas; veredictos en fichero propio.
**Contado del JSONL: A 0, B 0, C 1, D 49.**

## LOS DOS HALLAZGOS DE LA LECTURA

**EL PRIMER `C` DE TODA LA LECTURA DE `OP-E-03`** (tramo 1: C 0; tramo 2: C 0). El par
**111** es la figura del `9.22`, primer polo: el hijo despliega el paso 1 de la madre
(*que caracteristicas son criticas*) y la madre despliega el paso 3 del hijo (*con que
metrica y que limites*). **Las dos direcciones no apuntan a la misma linea**, que es la
comprobacion que el `9.22` exige. Arreglo prescrito: **enlace mutuo, no fusion**.
**CERO ARISTAS ESCRITAS.**

**LA PROPORCION DE NO RESUELTAS SUBE OTRA VEZ: 27,5% (tramo 1), 45,0% (tramo 2),
60,0% (esta mitad).** Es la direccion que el encargo preveia para el tramo mas debil
(mediana de `titulo_ratio` **76,2** contra **84,3**), asi que **se publica con la cifra
y con la mediana al lado, sin maquillarla y sin explicarla**. Una inversion afirmada
(par **114**), la segunda de toda la lectura tras el 16, y afirmada **porque aqui si
hay linea de un lado y procedimiento del otro**, que es lo que faltaba en los pares
82, 89 y 65.

## FIGURAS DEL TRAMO, REGISTRADAS Y SIN ADJUDICAR

Viven **en la razon de su fila** del JSONL, no en prosa aparte. Ocho mecanismos:
**(1)** casado por el objeto y no por la accion (103, 126, 133); **(2)** falso amigo
por token compartido (112, 118, 121, 137, 139, 143, 144); **(3)** linea compartida con
procedimiento propio a cada lado, el caso 2.195 (104, 115, 125); **(4)** paso casado
con su refutacion, ahora **cuatro** apariciones y una **dentro del mismo libro**
(113, 119, 122); **(5)** nodos iman (`customer_validation`, `pre_control_estadistico`,
`auditorias_calidad_proceso`, `capacidad_de_proceso`); **(6)** inversion de papeles
entre filas, **cuatro** casos, que con cuatro deja de parecer accidente (138, 144, 146
y el 135); **(7 NUEVA)** el barrido casa **el paso equivocado del nodo correcto**, y
el par afirmable existe en otra linea del mismo nodo (147, 148); **(8 NUEVA)**
duplicacion **interna** de un nodo, que dice lo mismo en dos de sus propios pasos
(127). **El contraste 148 contra 149 es lo mas util:** el **mismo** falso amigo
("capacidad") da un par afirmable y uno no resuelto, o sea que **el falso amigo por si
solo no decide nada**; decide si en el nodo hay una linea que el hijo despliegue.

## GUARDAS Y MUTACIONES, TODAS CORRIDAS

`SALIDA_V98_TAREA1_MUTACION.txt` (EXIT 0): **11 casos, 3 controles, 8 mutaciones, las
8 mueven el veredicto**. `SALIDA_V98_TAREA3_MUTACION.txt` (EXIT 0): **10 casos, 2
controles, 8 mutaciones, las 8 tumban el instrumento**, y la M7 comprueba ademas que
**no escribe nada**. `SALIDA_V98_TAREA4_MUTACION.txt` (EXIT 0): **8 casos, 1 control,
7 mutaciones, las 7 caen**; la M4 es la clave (una direccion con un id ajeno al par cae
en ROJO). **Idempotencia disparada EN VIVO en los cuatro instrumentos que escriben**
(`..._FECHAS_IDEMPOTENCIA`, `..._ENLACES_IDEMPOTENCIA`, `..._TAREA3_IDEMPOTENCIA`,
`..._TAREA4_ADDENDUM_IDEMPOTENCIA`), los cuatro **EXIT 1** sin escribir.

**Y SE DECLARA LO QUE NO SE PRUEBA, en vez de fabricarlo:** la **clase** y la
**direccion** de los 50 pares, y la del 42, son **lectura a mano contra el grafo** y
**NO TIENEN CASO ROJO AUTOMATICO**, porque no hay en el repo una segunda fuente
independiente. Su control es la relectura ciega del auditor, no un `assert`.

## DOS COSAS QUE ENCONTRE YO Y DIGO YO

**(1) MI PROPIA CORRECCION ROMPIO UNA GUARDA AJENA.** La insercion de la correccion de
fecha entra **justo detras del parentesis**, o sea **en medio** de la marca, y con eso
la guarda de idempotencia (iv) del script de la vuelta 97 dejo de disparar, porque
buscaba la marca entera como subcadena. **Salio a la luz porque volvi a correr
`--aplicar` y salto UNA guarda de las dos.** Arreglado con `ancla_de()`, que ancla en
el parentesis y es inmune a lo que se inserte detras; comprobado en vivo, EXIT 1 con
las dos guardas disparando.

**(2) LA GUARDA DE CITA DEL BANCO ME TUMBO A MI 16 VECES.** La primera corrida de
`--medir` de la TAREA 4 cayo con **16 fallos**: dieciseis razones mias no citaban
ninguna regla. **Arregle las razones, no la guarda.**

## RUTAS TOCADAS (`19a8f95e` a `HEAD`)

Talladas, no tecleadas: `git diff --name-status` a `SALIDA_V98_RUTAS_TOCADAS.txt`,
contado con `tallar_composicion_salida.py` a `SALIDA_V98_RUTAS_COMPOSICION.txt`,
EXIT 0: **54 nuevos (A), 7 modificados (M)**, 61 filas. Desglose de los nuevos contando
el mismo fichero: **43** en `docs/loop/`, **10** en `scripts/loop/`, **1** en
`docs/plan/`. **De los 7 modificados, DOS NO SON MIOS**: `docs/loop/AUDITOR.md` y
`docs/loop/EJECUTOR.md` los escribio el fundador en `d2c565ca`. Los cinco mios:
`docs/PENDIENTES.md`, `docs/plan/04_ENLACES.md`, `docs/plan/OPERACIONES.jsonl`,
`docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl` y
`scripts/loop/vuelta97_tarea2_addendum_opE03.py`. **CERO de `dataset/`, `web/` o
`engine/`.** Los ficheros de cierre entran en el commit de cierre y por eso no estan
en esa cuenta.

## LAS RACHAS Y LOS PENDIENTES DE DOCTRINA

**CLASE O CIFRA PUBLICADA: entra en UNO.** Lo que esta vuelta pone contra esa racha:
la fecha ya no puede teclearse (sale de `git` en los dos instrumentos que la escriben)
y la serie entera esta medida, no solo las dos que el auditor encontro.
**REPORTE: CERO al entrar.** **PENDIENTES DE DOCTRINA: NINGUNO NUEVO.**

## DOS PREGUNTAS, porque no las puedo decidir yo

**(a) LOS SIETE NODOS CON GUION** (no doce: remedido hoy, 12 con guion, **7 vivos y 5
deprecados**, `SALIDA_V98_TAREA2_NODOS_CON_GUION.txt`). **Lo que anado medido:** cero
de los 3.853 nodos llevan guion en `etiqueta_arbol`, los 7 vivos tienen la suya y
limpia, y las superficies de navegacion usan `etiquetaArbol()` (`graph.ts` 173, 13
llamadas), **asi que por ahi el guion no llega**. `titulo_concepto` llega por
`tituloDeNodo()` (`graph.ts` 180), cuyas dos llamadas reales alimentan **al modelo**
(`juezSesion.ts` 58, `recorrido.ts` 409), no chrome visible. **Lo que NO establecí, y
lo digo en vez de afirmarlo:** no barri las 64 apariciones de `titulo_concepto` en
`web/`, asi que **no afirmo que ninguno de los siete llegue nunca a pantalla**. **No
toco ninguno.**

**(b) HAY FECHAS IMPOSIBLES FUERA DE LOS FICHEROS DEL PLAN, Y UNA NO SE PUEDE
CORREGIR SIN MENTIR.** La linea 1001 de `04_ENLACES.md` dice *"la decision del fundador
del 29 ago 2026"* y cita **en la misma frase** el fichero
`docs/loop/paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md`, que **existe y se
llama asi** (`ls` lo confirma; hay **dos** ficheros de parada con `2026-08-29` en el
nombre). Corregir la prosa la pondria en contradiccion con la ruta que ella misma cita,
y renombrar ficheros nadie me lo ha pedido. **La traigo medida y sin tocar.**

## LOS DISCUTIBLES MARCADOS, antes de saber si acierto

1. **EL `C` DEL PAR 111 ES EL DISCUTIBLE GRANDE Y LO PONGO PRIMERO.** Es el primer `C`
   en 150 pares leidos de esta bolsa, y el banco avisa de que la figura es rara
   (*"primera aparicion en 1.100 pares"*). **La forma de tumbarme es leer el sentido
   B hacia A**: si `limites_especificacion_funcionales` no es el procedimiento del paso
   3 del hijo sino solo material vecino, entonces es **D** y mi `C` sobra.
2. **LAS DOS DIRECCIONES QUE AFIRME SOBRE UN PASO DISTINTO DEL QUE EL BARRIDO CASO
   (147 y 148).** Me apoyo en el `9.6.3` (*"la vara no cuenta cuantos pasos comparten
   ni cual"*), pero **estoy eligiendo yo la linea contra la que mido**, y eso es un
   grado de libertad que las otras 48 lecturas no usan. Si el auditor cree que la vara
   se aplica **solo** sobre el paso casado, las dos caen a NO RESUELTA y mi 60,0% sube
   a 64,0%.
3. **EL 60,0% PUEDE SER OTRA VEZ MI VARA Y NO LA BOLSA.** El acta 97 ya adjudico que el
   45% era la bolsa, con muestra elegida en mi contra, y el umbral no se toco. **Pero
   ese control no se hereda**: esta mitad es material nuevo. **La forma de tumbarme es
   la misma**, leer a ciegas una muestra de mis 30 no resueltas.
4. **EL PAR 114, LA INVERSION AFIRMADA.** Le di la vuelta a la etiqueta de la bolsa. Si
   el paso 4 del hijo (*"evaluar la ejecucion del detalle"*) se lee como una linea
   demasiado generica para que `ejecucion_de_touchpoints` sea su procedimiento, **no
   hay inversion y el par es NO RESUELTA**.
5. **EL 145 PODRIA SER LA ESPECIE DE LA REFUTACION Y LO LLAME DIRECCION AFIRMADA.** El
   paso 4 del hijo matiza el paso 1 de la madre. **Lo lei como caveat de cobertura** por
   la adjudicacion 3.3 del acta 97, pero en el 113, el 119 y el 122 una tension parecida
   me llevo a NO RESUELTA. **Puede que la frontera que use no sea la misma en los cuatro.**
6. **CORREGI CUATRO FECHAS QUE EL ENCARGO NO ME MANDO CORREGIR** (vueltas 88, 89, 90 y
   91) **y TRES MAS EN UN FICHERO QUE EL ENCARGO NO NOMBRA** (`04_ENLACES.md`). Las
   meti por el borde de la 3.7 con sus tres condiciones medidas. **Si el criterio es que
   el borde solo cubre la operacion que el encargo ya toca, me pase en siete.**
7. **ADOPTE EL MODO AUSTERO UNA VUELTA ANTES DE QUE LE TOQUE.** Su letra dice *"desde
   la proxima vuelta"* y entro a mitad de esta. **Si eso es leer una regla a mi
   conveniencia**, este reporte deberia haber ido en regimen completo.
