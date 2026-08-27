# REPORTE DE LA VUELTA 90 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 89. Apertura sellada ANTES de la primera operacion en
`docs/loop/SALIDA_V90_HEAD_APERTURA.txt`: `314ca33a5c431c74273059720a3e3988fac0e599`
(la decision del fundador del 29 ago 2026). Cierre recomputado AL CIERRE.

**ESTA VUELTA EJECUTA LA DECISION DEL FUNDADOR DEL 29 AGO 2026** (opciones a y b,
las dos), registrada en `docs/loop/paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md`:
la escalada del tallador a las fases mecanicas por fin se ejecuta como operacion
de codigo (TAREA 3, BLOQUEANTE), nace el caso rojo probado por mutacion, y
`OP-E-06` ABRE con la bolsa V90: **113 aristas ESCRITAS** (mas 1 fila `YA_ESTABA`
por colapso de alias, 114 leidas de 117). La racha de reporte vuelve a cero al
relanzar.

## CABECERA TALLADA (--fase04 --vuelta 90), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 90`.
Salida completa en `docs/loop/SALIDA_V90_CABECERA_TALLADA.txt`, **EXIT 0**. Antes
del commit de cierre, `--comparar docs/loop/REPORTE.md` se corre otra vez sobre
este mismo fichero ya escrito (seccion de cierre, mas abajo).

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.995 / 8.974 / 17.969 / 9.618 | **9.108 / 9.087 / 18.195 / 9.731** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+113 / +113 / +226 / +113** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `d6e6f2eb` (ACTA DE LA VUELTA 89 DEL AUDITOR, leido de git log), HEAD real de apertura `314ca33a` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `d6e6f2eb` (ACTA DE LA VUELTA 89 DEL AUDITOR, leido de git log), HEAD real de apertura `314ca33a` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**LA FILA DEL MARCADOR NO SE IMPRIME A PROPOSITO**, y se dice por que en vez de
callarlo: el corri `python scripts/recomputar_marcador.py 3388` en apertura y en
cierre (los dos dan **A 551 / B 72 / C 5 / D 2.760, n 3.388, sin cambio**, guardado
en `docs/loop/SALIDA_V90_MARCADOR_CRIBADO_APERTURA.txt` y `..._CIERRE.txt`), pero
esa salida esta en el formato plano del cribado (`  A 551`), no en el formato de
diccionario que el modo `--fase04` del tallador exige para esta fila
(`'A': (\d+)`); ningun instrumento de esta vuelta produce ese segundo formato, y
por la regla "la celda que no salga de un instrumento no se escribe" la fila
opcional simplemente no se talla, en vez de fabricarsela a mano. **El marcador NO
se movio esta vuelta** (la fase 04 no toca el cribado), y la cifra de arriba esta
citada de su propio recomputo, no tecleada.

**LAS ARISTAS SON LA UNICA CELDA QUE CAMBIA (fuera de las filas derivadas), Y ES
LA ESCRITURA DE `OP-E-06`, NO UNA DISCREPANCIA:** `+113 / +113 / +226 / +113` en
`nodos_siguientes` / `nodos_previos` / suma / union, que es exactamente el numero
de aristas ESCRITAS esta vuelta (ver TAREA 4). El sha256 del `master_graph.json`
**cambia**: de `1671895b2a6c...` (apertura, identico al cierre de la vuelta 89) a
`9acfc02d9c80e3ba1793de7c28ea44b499dbc79711d13dea83db4a3706484b42` (cierre de esta
vuelta).

El ciclo de tres (`scripts/run_phase1.py --reaplico-curaduria`,
`scripts/etiquetas_de_cara.py --aplicar`, `scripts/sync_assets_web.py`) se corrio
completo dos veces (apertura y cierre), verificado con `git status --porcelain --
dataset/ web/lib/assets/` en CERO despues del ciclo completo las dos veces (antes
de escribir las aristas de `OP-E-06` entre medio). `etiquetas_de_cara.py` cambia
las mismas 71 etiquetas las dos veces (no persisten en `dataset/nodos/`, son
recalculadas por `run_phase1.py --reaplico-curaduria` cada vez que ese comando
regenera `master_graph.json`; es comportamiento esperado, verificado igual en la
apertura y en el cierre).

## TAREA 1: LOS REGISTROS DEL ACTA 89

Registrado en `docs/plan/04_ENLACES.md` (seccion nueva "REGISTRO DE LA VUELTA 89
(ACTA DEL AUDITOR), TAREA 1 DE LA VUELTA 90"): las dos caidas de reporte de la
vuelta 89 con su medicion (el truncado a 200 que en dos ejemplos mide 305 y 263,
y el caso rojo que compara `"ENTRA"` consigo mismo), la caida del auditor (la
escalada automatica no encargada, acta 89 seccion 6 punto 1), y las siete
adjudicaciones de la seccion 4 (4.1 a 4.7), cada una con su linea de
`ACTA_AUDITOR.md` citada. Commit `fc7fa309`.

## TAREA 2: LA BOLSA `OP_E_06_REBASE_V90.jsonl`

`scripts/loop/vuelta90_tarea2_rebase_ope06.py` parte de V89 (117 filas, sin
tocar) y aplica: **ENTRA el 530** (`estrategia_de_innovacion_de_producto ->
estrategia_de_innovacion_y_tecnologia`, tomado de V88, adjudicacion 4.1), **SALE
el 932** (`cumplimiento_magnuson_moss -> mecanismo_resolucion_disputas`,
adjudicacion 4.2). El instrumento verifica en tiempo de ejecucion que la cifra
final sea **exactamente 117** y que el conjunto de puestos sea DISTINTO del de
V89 (no solo el numero): las dos condiciones dieron VERDE (`docs/loop/
SALIDA_V90_TAREA2_REBASE_V90.txt`). Los puestos **581 y 650** quedan anotados en
`docs/PENDIENTES.md` como candidatos de una pasada posterior (adjudicacion 4.3):
se caen por como quedo cosechada su frase, no por su contenido. Commit
`fc7fa309`.

## TAREA 3 (BLOQUEANTE): LA ESCALADA DEL TALLADOR Y EL CASO ROJO POR MUTACION

**3.a, la escalada que quedo sin ejecutar el 26 ago.** `scripts/loop/
tallar_conteo_campo.py`, tallador hermano de `tallar_cabecera_reporte.py`: dado
un JSONL y un campo, cuenta la distribucion de longitud DIRECTO del fichero (no
tecleada) y coteja una lista de puestos citables contra su `len` real. **CASO
OBLIGATORIO, contra el ejemplar de la vuelta 89**
(`docs/loop/SALIDA_V90_TAREA3A_CASO_OBLIGATORIO.txt`, EXIT 0): tallar
`docs/plan/COSECHA_RAZONES_D.jsonl` con `--campo frase --longitud-exacta 200` da
**397 filas, 270 con `len` exactamente 200, 23 por encima (maximo 335), 104 por
debajo**, y `--verificar-puestos 1134,1149,1995,2023,2082,2106,2038` marca **2023
(305) y 2082 (263) como DISTINTOS**, no como "verificado": es la vara que la
decision del fundador puso ("las DOS caidas de la vuelta 89 tienen que caer
dentro de su alcance"), y la primera cae dentro.

**3.b, el caso rojo probado por mutacion.** `scripts/loop/
verificar_caso_rojo_por_mutacion.py`: arnes generico `probar_por_mutacion()` que
muta la ENTRADA de un criterio real (no el literal del lado derecho de un
assert) y exige que el veredicto CAMBIE. Su autoprueba
(`docs/loop/SALIDA_V90_TAREA3B_AUTOPRUEBA.txt`, EXIT 0) reproduce a proposito el
defecto EXACTO de la caida 3.2 del acta 89 (`veredicto_2 = "ENTRA"` como
constante) y confirma que **cae en rojo**, y valida en paralelo un caso positivo
(un criterio que si depende de la entrada) que pasa. Es la vara de la segunda
caida ("una afirmacion sobre una salida"): sin este arnes, el "caso rojo" de la
89 se habria publicado igual; con el, cae.

Aplicado sobre si mismo antes de tocar `OP-E-06`: `scripts/loop/
vuelta90_tarea3_prueba_mutacion_tallador.py` prueba por mutacion la unica pieza
de juicio del tallador nuevo (`clasifica_longitud()`), mutando el CAMPO real de
una fila fabricada (200 caracteres a 305, el largo real del puesto 2023) y
confirmando que el veredicto pasa de `IGUAL` a `MAYOR`
(`docs/loop/SALIDA_V90_TAREA3B_MUTACION_TALLADOR.txt`, EXIT 0). Commit `919841c0`.

## TAREA 4: `OP-E-06` ABRE CON LA BOLSA V90

**Primera mitad, la direccion.** `scripts/loop/vuelta90_tarea4_direccion_ope06.py`
lee la direccion de las 117 filas sobre el campo `razon` COMPLETO de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (no sobre la `frase` truncada a 200
caracteres de la cosecha, que en varias filas corta justo el nombre del nodo que
hace falta leer): el nodo que la razon describe despachando/diciendo/nombrando
"en UNA LINEA" es la madre; el que "trae el procedimiento (de esa linea)" es el
hijo. 108 de 117 se clasifican por expresion regular; 6 se leyeron a mano sobre
la razon completa, cada una con su cita literal en el codigo (530, 552, 1261,
1787, 2015, 2023). **HALLAZGO QUE MUEVE LA CUENTA, marcado DISCUTIBLE:** al leer
la razon completa, TRES pares (**2082, 2084, 2112**) citan literalmente "banco
9.22" con "CONTINUA en los dos sentidos": son ENLACE MUTUO, no la escalera de una
sola direccion que `OP-E-06` exige por su propia `verificacion`. Quedan
EXCLUIDOS de esta vuelta y anotados en `docs/PENDIENTES.md` para una operacion de
dos aristas aparte. Verificado: **114 con direccion + 3 excluidos = 117**
(`docs/loop/SALIDA_V90_TAREA4_DIRECCION.txt`, EXIT 0). Commit `aeb66e78`.

**Segunda mitad, la escritura, con la via de OP-C-05 cableada.**

```
python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --vuelta 90 --antes
python scripts/loop/vuelta90_tarea4_escribir_ope06.py
python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --vuelta 90 --despues
```

`--antes`: **935 entradas que sobran, 711 nodos** (`docs/loop/
SALIDA_V90_GUARDA_OPC05_ANTES.txt`), identico a la linea base de la vuelta 89.
`--despues`: **935 entradas que sobran** (`docs/loop/
SALIDA_V90_GUARDA_OPC05_DESPUES.txt`): **VERDE, la cuenta no crecio (+0)**.

La escritura usa la semantica canonica de `resolverId` (`scripts/plan/
aristas_duplicadas_tras_resolver.py`, camina la cadena de `ids_alias` entera,
copiada sin variar): madre y hijo se resuelven al id vivo ANTES de escribir.
**Dos hallazgos reales de esta resolucion, con nombre**, para que no queden
escondidos en el diff:

1. **El puesto 2023 sale `YA_ESTABA`, no `ESCRITA`.** Su madre
   (`certificado_de_origen_tratados_libre_comercio`) y la madre del puesto 2015
   (`nafta_free_trade_agreements`, DEPRECADO) resuelven, por la cadena de alias,
   al MISMO nodo vivo. Escribir los dos habria sido una entrada duplicada tras
   resolver, la clase exacta que `scripts/plan/
   aristas_duplicadas_tras_resolver.py` existe para contar. Procesando en orden
   de puesto y releyendo el fichero en cada paso (como `scripts/loop/
   vuelta87_tramo12_escribir.py`), el 2023 detecto la arista ya escrita por el
   2015 y no la repitio.
2. **Cinco pares mas escribieron sobre el ALIAS de la razon, no sobre el id
   literal citado en el titulo**, porque su madre o su hijo resulto ser un id
   deprecado con alias vivo: `pivotar_o_proceder` (deprecado) resuelve a
   `pivote_o_proceder` (vivo, 4 aristas: puestos 956, 1160, 1345, 1472, 1546),
   `warrants_deuda_convertible` a `warrant_pricing_venture_debt` (puesto 1286),
   `seleccion_etapa_fondo_vc` a `embudo_secuencial_de_inversores` (puesto 1169),
   `diseno_organizacional_equipos_innovacion` a `equipo_multifuncional_real`
   (puesto 1013), `seis_medios_comunicacion_cliente` a
   `estrategia_multicanal_bienvenida` (puesto 1012), `generar_multiples_opciones`
   a `pensamiento_convergente_divergente` (puesto 1270), y `build_metrics_
   toolset`/`metricas_cohortes` a `metricas_de_adquisicion_activacion`/
   `analisis_de_cohortes` (puesto 1545, los dos lados por alias). **Verificado
   uno por uno contra el `git diff` de cada fichero**: el nombre que aparece
   modificado en `dataset/nodos/` es siempre el id VIVO, nunca el deprecado.

**Resultado:** `docs/loop/SALIDA_V90_TAREA4_ESCRITURA.txt` (EXIT 0): **113
ESCRITA, 1 YA_ESTABA, 0 ESCALERA_ROTA**, de 114 pares. Las cuatro cifras de
aristas se movieron exactamente `+113 / +113 / +226 / +113` (verificado contra la
cabecera tallada arriba: calzan al digito). **172 ficheros de
`dataset/nodos/` tocados** (`git status --porcelain -- dataset/nodos/ | wc -l`),
menos que `113 * 2` porque varios nodos son extremo de mas de un par (por
ejemplo `pivote_o_proceder`, extremo de cinco). `OPERACIONES.jsonl` actualizada:
`OP-E-06` gana tres lineas de `evidencia` y un ADDENDUM DE EJECUCION en `nota`
con la cifra completa (114/113/1/0, los 3 excluidos, y el resultado de
`OP-C-05`); `estado` se queda en `LISTA`, mismo criterio que `OP-E-01` y
`OP-E-04` (el estado de verdad es el repo y el commit, no un campo nuevo, backlog
del 14 ago 2026).

## LOS TRES PARES DE ENLACE MUTUO (2082, 2084, 2112), Y POR QUE SON EL HALLAZGO MAS IMPORTANTE DE ESTA VUELTA

Ninguno de los tres mueve un dato: quedaron sin escribir, y sin escribir siguen.
**Lo que importa es que la bolsa V90, si se hubiera escrito con una sola
direccion forzada sobre los tres, habria escrito una escalera sobre un enlace
mutuo**, exactamente lo que `OP-C-05` (lista blanca por evidencia) y el banco
9.22 existen para impedir. Se encontraron porque la TAREA 4 lee la `razon`
COMPLETA, no la `frase` truncada de la cosecha (la misma leccion de la TAREA
3.a, aplicada donde de verdad podia doler: no en una tabla de reporte, sino en
una escritura real). Van a `docs/PENDIENTES.md` para una operacion de dos
aristas aparte, con su cita literal cada uno.

## DISCUTIBLES MARCADOS, PARA LA RELECTURA CIEGA DEL AUDITOR

1. **Los tres pares de enlace mutuo (2082, 2084, 2112), excluidos de OP-E-06.**
   Marcado DISCUTIBLE no porque dude de la exclusion (la razon de los tres cita
   "banco 9.22" literal, no hay ambiguedad de lectura), sino porque es la unica
   decision de ESTA vuelta que cambia la FORMA de la bolsa (117 se convierten en
   114 a escribir, no en 117): si el auditor lee la razon de los tres y
   encuentra una lectura distinta, la cuenta de esta vuelta se mueve.
2. **Las seis direcciones leidas a mano** (530, 552, 1261, 1787, 2015, 2023),
   porque la clasificacion automatica no las resolvio y dependen de mi lectura
   de la razon completa, citada en el codigo de `scripts/loop/
   vuelta90_tarea4_direccion_ope06.py` (variable `DIRECCION_MANUAL`). Las 108
   restantes salen de una regla mecanica (buscar el verbo de "una linea" pegado
   al id) y no dependen de mi lectura.
3. **El puesto 2023 como `YA_ESTABA`**, porque depende de que `nafta_free_trade_
   agreements` resuelva de verdad a `certificado_de_origen_tratados_libre_
   comercio` (verificado con `res()` en vivo, ver TAREA 4) y no de una lectura
   mia: si el auditor corre el mismo `res()` y da otro nodo, la cuenta de 113
   ESCRITA se mueve a 114.

## PENDIENTES DE DOCTRINA

Ninguna. Las tres adjudicaciones de esta vuelta (530 entra, 932 sale, los tres
2082/2084/2112 excluidos por enlace mutuo) salen de la letra ya adjudicada de
`OP-E-06` y del banco 9.22, no de una regla nueva.

## COMMITS DE LA VUELTA

`git log --format='%h %s' 314ca33a..HEAD` (medido al escribir esta seccion,
antes del commit de cierre): `fc7fa309` (TAREA 1 y 2), `919841c0` (TAREA 3),
`aeb66e78` (TAREA 4, primera mitad, direccion). Este reporte y la escritura de
`OP-E-06` (TAREA 4, segunda mitad) van en el commit de cierre, el siguiente
despues de este.

## CON EL FRENO DELANTE

La racha de reporte vuelve a CERO al relanzar (regla del acta 89, aplicada por
el fundador). La regla de las tres seguidas sigue viva. La racha de clase o
cifra publicada esta en CERO, no en una.
