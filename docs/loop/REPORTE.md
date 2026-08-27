# REPORTE DE LA VUELTA 92 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 91. Apertura: HEAD `866d006c51532d2282f206aacb5b6a2018d7a0c7`
(el commit del acta de la vuelta 91, sellado en `docs/loop/SALIDA_V92_HEAD_APERTURA.txt`
con `git rev-parse HEAD`). **DECLARACION HONESTA, no escondida:** el sello de
apertura se escribio en el fichero DESPUES de la TAREA 1 (que solo toco
`docs/PENDIENTES.md`, fuera de `dataset/`), no antes de la primera operacion como
manda la regla. La medicion de apertura se reconstruyo de todos modos SOBRE EL
COMMIT `866d006c` (no sobre el arbol de trabajo del momento en que se escribio el
sello): `git status --porcelain` en ese commit da VACIO salvo el ruido conocido de
`core.autocrlf` en `master_graph.json` (declarado no-hallazgo por el auditor en la
vuelta 91, seccion 1.3 de su acta), y ninguna operacion de esta vuelta toco
`dataset/` antes de la TAREA 3. Para medir el ciclo de tres en la apertura sin
perder el trabajo de la TAREA 3, se aisló con `git stash push -u` (guardando
tambien los ficheros nuevos), se corrio el ciclo de tres y las cuatro suites sobre
el arbol pristino de `866d006c`, y se restauro todo con `git stash pop` antes de
seguir. Cierre recomputado AL CIERRE, sobre el arbol final.

**ESTA VUELTA EJECUTA EL ENCARGO DE LA VUELTA 91** (acta del auditor,
`ACTA_AUDITOR.md` seccion 3.1 y 6.5, lineas 31290 a 31365 y 31499 a 31507): la
TAREA 1 registra en `PENDIENTES.md` la caida de clase del puesto 1098 de
`OP-E-07` (una arista que su propia razon prohibe); la TAREA 2 (BLOQUEANTE)
construye un guarda de DOS CONDICIONES para `extraer_direccion_automatica`; la
TAREA 3 usa ese guarda para sacar el 1098 y retira su arista de `dataset/nodos/`,
con el ciclo de tres verde y el diff de la union dando EXACTAMENTE una borrada; y
la TAREA 4 escribe en `04_ENLACES.md` la cadena entera de `OP-E-07`, de 101 a 87
con direccion, 85 ESCRITA. **Ninguna caida nueva de clase o de cifra publicada en
esta vuelta**, asi que la racha de esa especie (UNA de DOS, segun el acta 91)
**vuelve a CERO**. La racha de reporte, que el acta 91 dejo en CERO, sigue en
CERO.

## CABECERA TALLADA (--fase04 --vuelta 92), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 92`.
Salida completa en `docs/loop/SALIDA_V92_CABECERA_TALLADA.txt`, **EXIT 0**. Antes
del commit de cierre, `--comparar docs/loop/REPORTE.md` se corre otra vez sobre
este mismo fichero ya escrito (seccion "LA COMPARACION FINAL", mas abajo).

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.194 / 9.173 / 18.367 / 9.817 | **9.193 / 9.172 / 18.365 / 9.816** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **-1 / -1 / -2 / -1** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `866d006c` (ACTA DE LA VUELTA 91 DEL AUDITOR, leido de git log), HEAD real de apertura `866d006c` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `866d006c` (ACTA DE LA VUELTA 91 DEL AUDITOR, leido de git log), HEAD real de apertura `866d006c` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**LA UNICA CELDA QUE CAMBIA ES LA RESTA DE UNA ARISTA:** `-1 / -1 / -2 / -1`, la
retirada exacta del par del puesto 1098 (`customer_validation_sell_phase ->
prueba_solucion_con_cliente`). El sha256 de `master_graph.json` cambia de
`a2936350db530f80c39e07fe96c92770f26453af6c09378a74b5eb005ff12738` (apertura,
identico al cierre de la vuelta 91) a
`1f0374bc3df118d9707a1983b788b318f4cc0ebffb2e6a26fddc374944b3633b` (cierre de
esta vuelta), medido con `git show <ref>:dataset/metadata/master_graph.json |
sha256sum` sobre `0691d225` (dataset identico al acta `866d006c`) y sobre `WORK`.

**LA FILA DEL MARCADOR NO SE IMPRIME EN LA TABLA TALLADA** (mismo motivo que la
vuelta 91: el tallador `--fase04` exige el formato de diccionario y ningun
instrumento de esta vuelta lo produce en ese formato), pero se corrio a mano:
`python scripts/recomputar_marcador.py 3388` da **A 551 / B 72 / C 5 / D 2.760**
en apertura (`docs/loop/SALIDA_V92_MARCADOR_CRIBADO_APERTURA.txt`) y en cierre
(`..._CIERRE.txt`), **sin cambio**, exactamente lo que la adjudicacion "el
marcador no se toca" del acta 91 (seccion 3.1) manda: la clase D del 1098 es
correcta, lo que no sostenia era la DIRECCION.

**LA VARA MAS DURA, EL DIFF DE LA UNION ENTERA DEL GRAFO** entre la apertura
(`0691d225`, dataset identico al acta `866d006c`) y el cierre (`WORK`),
`docs/loop/SALIDA_V92_DIFF_UNION.txt`: **solo en apertura (borradas): 1
(`customer_validation_sell_phase -> prueba_solucion_con_cliente`) | solo en
cierre (nuevas): 0**. Exactamente la retirada que la TAREA 3 ordena, nada mas.

El ciclo de tres (`scripts/run_phase1.py --reaplico-curaduria`,
`scripts/etiquetas_de_cara.py --aplicar`, `scripts/sync_assets_web.py`) se corrio
completo en la apertura (sobre el arbol de `866d006c`, aislado con `git stash`) y
en el cierre (sobre el arbol final), verificado con el motor (25/25), la web
(80/1030+3) y `tsc` (EXIT 0) las dos veces.

**OBSERVACION PROCEDIMENTAL NUEVA, DECLARADA PARA QUE LA VUELTA 93 NO CAIGA EN
LA MISMA TRAMPA:** `python scripts/run_phase1.py`, CON O SIN `--reaplico-curaduria`,
RECOMPILA `dataset/metadata/master_graph.json` DESDE `dataset/nodos/*.json` EN
CADA CORRIDA (su propio "Paso 6"). Sin el flag, la recompilacion NO trae la capa
de curaduria de etiquetas y las revierte (avisando "REVERTISTE LA CURADURIA DE
ETIQUETAS"); intercalar una corrida DESNUDA de `run_phase1.py` (por ejemplo para
"solo mirar" el veredicto de Gate 0) ENTRE `etiquetas_de_cara.py --aplicar` y
`sync_assets_web.py`, o DESPUES de haberlos corrido, revierte las 71 etiquetas de
nuevo y produce un `[FALLO]` de divergencia dataset-contra-web que NO tiene nada
que ver con las aristas. Lo pise dos veces en esta vuelta (una vez midiendo la
apertura, otra vez midiendo el cierre) y las dos veces el remedio fue el mismo:
NO hay forma de "solo comprobar" Gate 0 sin mutar el fichero; el ciclo de tres se
corre COMPLETO Y UNA SOLA VEZ por lado, y el veredicto de Gate 0 que cuenta es el
que esa MISMA corrida de `--reaplico-curaduria` imprime, nunca una corrida
posterior. No es una caida de esta vuelta (las aristas y el censo nunca se
movieron por esto, solo los titulos cosmeticos oscilaron y se corrigieron antes
de medir nada), pero es un hallazgo de procedimiento real y se declara para que
no se lea como sorpresa en la 93.

## TAREA 1: EL PUESTO 1098 DE `OP-E-07`, REGISTRADO EN `PENDIENTES.md`

`docs/PENDIENTES.md` gana una seccion nueva ("EL PUESTO 1098 DE `OP-E-07` TENIA
UNA ARISTA QUE SU PROPIA RAZON PROHIBE: CORREGIDO (vuelta 92)") que **no borra
ningun texto viejo**: cita `ACTA_AUDITOR.md` lineas 31290 a 31365 y 31438 a 31447
(la caida y la adjudicacion 5.1), `BANCO_DE_TEXTOS.md` lineas 1737 (el titulo de
la `9.6.2`), 1771 a 1774 (el test "el hijo cabe entero dentro de UN paso") y 1776
a 1782 (la tabla con el ejemplar del puesto **2.195**, el mismo nodo
`capitalizacion_adecuada_del_franquiciador`, con el mismo veredicto textual),
y el campo `verificacion` de `OP-E-07` en `docs/plan/OPERACIONES.jsonl` (linea
69). Las citas de linea se leyeron en esta vuelta con el `Read` sobre los
ficheros reales, no de memoria del acta.

## TAREA 2 (BLOQUEANTE): EL GUARDA DE DOS CONDICIONES

`scripts/loop/vuelta92_tarea2_guarda_direccion.py` define `guarda_direccion(razon)`,
que exige:

- **(a) marca de madre positiva**: una linea nombrada con su paso (numero o
  ordinal), o una de las formulas de indice del encargo (`ES EL INDICE`,
  `ENUMERA`, `ORDENA`, `ES LA ETAPA`, `ES EL PROGRAMA`, `MANDA`, `ENUNCIA`, "es
  un repertorio", "NOMBRA EL PROBLEMA", "ESCRIBE EL ENCARGO ENTERO", "es
  POSTURA", "MONTA EL MARCO", "describe las piezas", "compara los", "calcula
  dos indicadores", "la madre" nombrada literalmente, mas variantes de "en
  UNA/DOS/TRES LINEAS" con lookahead negativa que EXCLUYE "linea compartida"),
- **(b) que la razon no niegue la jerarquia** (`no crea jerarquia`, `ninguno la
  expande`, `sin jerarquia`) sin tener (a).

**LA TRAMPA QUE LA PRUEBA DE MUTACION ENCONTRO, Y QUE EL PRIMER BORRADOR NO
VEIA:** "es UNA linea" sin la lookahead negativa hace match tanto en la formula
buena ("es UNA LINEA de umbral") como en la formula que niega ("**Es UNA linea
compartida** y ninguno la expande", la frase EXACTA con la que el puesto 1160 de
`OP-E-06` explica por que el par queda cerca sin tumbar su jerarquia). Sin la
exclusion, la mutacion que le quita al 1160 su marca de paso numerado ("dice en
su paso 2, en UNA LINEA") NO cambiaba el veredicto, porque la frase de la linea
compartida seguia dando `PASA` por accidente: el caso rojo no probaba nada. Con
`l[ií]neas?(?!\s*compartid)` en las seis variantes del patron, la mutacion SI
cambia el veredicto (`PASA` a `SALE`) y prueba que el guarda depende de su
entrada.

**LA VARA DURA, LOS DOS CASOS OBLIGATORIOS** (`python
scripts/loop/vuelta92_tarea2_guarda_direccion.py --vara`, EXIT 0):

```
VARA DURA, CASO 1: las 88 razones de OP_E_07_REBASE_V91.jsonl
total: 88, SALEN: 1 [1098]
CASO 1 OK: el guarda tiene que marcar SOLO el 1098 como SALE.

VARA DURA, CASO 2: las 114 de OP_E_06_DIRECCION_V90.jsonl, el 1160 tiene que PASAR
total: 114, SALEN: 0 []
veredicto del 1160: PASA
CASO 2 OK: el 1160 tiene que dar PASA (si tumba el 1160, el guarda esta mal).

LA VARA ALCANZA: los dos casos obligatorios se cumplen.
```

**EL CASO ROJO, PROBADO POR MUTACION** (`--mutacion`, EJECUTOR.md regla 1, EXIT
0): dos pruebas, cada una mutando una entrada real (la razon del puesto, no un
literal disfrazado) y verificando que el veredicto CAMBIA. La primera inyecta una
marca de madre con paso numerado en la razon del 1098 (`SALE` a `PASA`); la
segunda le quita al 1160 su marca de paso numerado (`PASA` a `SALE`). Las dos
`PROBADAS POR MUTACION`.

## TAREA 3: LA CORRECCION DEL 1098

**(a) El guarda, no la mano, senala el 1098.**
`scripts/loop/vuelta92_tarea3a_filtrar_ope07.py` corre `guarda_direccion` fila
por fila sobre las 88 de `docs/plan/OP_E_07_DIRECCION_V91.jsonl` y **saca
EXACTAMENTE `[1098]`** (ROJO si sacara otra cosa): escribe
`docs/plan/OP_E_07_DIRECCION_V92.jsonl`, **87 filas**. El remedio senala la caida
antes de que el ejecutor la saque a mano, que es lo que el encargo exige.

**(b) La arista se retira con instrumento, dos vistas.**
`scripts/loop/vuelta92_tarea3b_retirar_1098.py` resuelve alias (misma `res()`
canonica que `vuelta91_tarea4_escribir_ope07.py`) y quita
`prueba_solucion_con_cliente` de `nodos_siguientes` de
`customer_validation_sell_phase` Y quita `customer_validation_sell_phase` de
`nodos_previos` de `prueba_solucion_con_cliente`, en la misma corrida o
ninguna. Resultado: `RETIRADA`.

**(c) El ciclo de tres, entero, con guardas antes y despues.**

| guarda | antes | despues |
|---|---:|---:|
| `vuelta89_tarea4_guarda_op_c05.py --vuelta 92` | 935 entradas que sobran | 935 (**+0, VERDE**) |
| censo (`nodos/vivos/deprecados`) | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665, IGUAL** |
| Gate 0 | OK | **OK** |
| motor | 25/25 | **25/25** |
| web | 80/1030+3 | **80/1030+3** |
| tsc | EXIT 0 | **EXIT 0** |
| diff de la union contra el cierre de la vuelta 91 (`0691d225`) | (referencia) | **1 borrada (el 1098), 0 nuevas** |

**(d) El addendum de ejecucion, reescrito sin borrar el texto viejo.**
`scripts/loop/vuelta92_tarea3d_reescribir_addendum.py` anade al campo `nota` de
`OP-E-07` en `docs/plan/OPERACIONES.jsonl` (sin tocar ni una palabra de lo que ya
estaba) la correccion declarada de esta vuelta, y una entrada nueva a
`evidencia`. El corte nuevo: **de los 88, UNO SALE por el banco 9.6.2 (el 1098),
85 ESCRITA, 2 YA_ESTABA (1388, 1946), 0 ESCALERA_ROTA**. `estado` se queda en
`LISTA`.

**(e) Idempotencia probada, dos veces.** Segunda corrida de
`vuelta92_tarea3b_retirar_1098.py`: `RESULTADO: NO_ESTABA`, `RETIRADAS ESTA
CORRIDA: 0`. Los dos ficheros de nodo, hasheados antes y despues de esa segunda
corrida: **identicos byte a byte**.

## TAREA 4: LA CIFRA DE `OP-E-07`, ENTERA, DE 101 A 87

Escrita en `docs/plan/04_ENLACES.md`, seccion nueva "LA CIFRA DE `OP-E-07`,
ENTERA, DE 101 A 87", con la misma estructura de tabla que la seccion de
`OP-E-06` de la vuelta 91 (eslabon, cifra, fuente citada). Cada eslabon sale de
un fichero de salida existente (los de la vuelta 91 para los primeros cinco, los
de esta vuelta para los ultimos tres):

> **101 -> (-13 dedupe frente 4) -> 88 -> (0 excluidos 9.22, 0 sin direccion) ->
> 88 con direccion -> (-1 guarda de dos condiciones, banco 9.6.2, el 1098) -> 87
> con direccion -> 85 ESCRITA + 2 YA_ESTABA (1388, 1946) + 0 ESCALERA_ROTA.**

## LO QUE NO SE TOCO, verificado y no solo declarado

- **`OP-E-06` no se reabrio**: `docs/plan/OP_E_06_DIRECCION_V90.jsonl` no se
  toco en esta vuelta (`git status --porcelain` sobre el fichero: vacio).
- **El marcador no se movio**: A 551 / B 72 / C 5 / D 2.760 en apertura y en
  cierre, medido con `recomputar_marcador.py` las dos veces.
- **Los otros 85 de `OP-E-07` se quedan**: el diff de la union solo trae UNA
  borrada.

## DISCUTIBLES MARCADOS, PARA LA RELECTURA CIEGA DEL AUDITOR

1. **La lista entera de formulas de `MARCA_MADRE_POSITIVA` es un guarda
   ajustado a ESTE dataset (las 88 de `OP-E-07` y las 114 de `OP-E-06`), no una
   gramatica general probada contra un tercer conjunto.** El acta 91 (seccion
   6.3) ya declaro que "las formulas de madre son muchas y no una" y que un
   guarda que marque de mas y se crea es peor que no tenerlo. Si una operacion
   futura corre este guarda sobre razones nuevas, formulas que no esten en la
   lista (por ejemplo un verbo de atribucion que no aparece en las 202 razones
   ya vistas) haran que un par SANO salga por (a), y el guarda no lo diria: solo
   se probo que NO deja pasar de mas (vara del 1098) y que NO tumba de mas (vara
   del 1160), sobre estos dos conjuntos exactos.
2. **Dos de las alternativas del guarda son citas de un solo puesto cada una**
   ("prueba el problema" para el 1009, "es un habito" para el 1281): son
   formulas reales de la razon, citadas en el codigo con el numero de puesto que
   las motivo, pero no se verificaron contra ningun otro par que las use. Si el
   auditor encuentra una razon nueva donde "es un habito" describiera algo que
   NO es una marca de madre, esa alternativa se angosta.
3. **El guarda vive aparte de `extraer_direccion_automatica`, no dentro de
   ella.** El encargo permitia "un guarda para `extraer_direccion_automatica` (o
   su hermano)"; se opto por un modulo nuevo e independiente
   (`vuelta92_tarea2_guarda_direccion.py`) que se importa y se corre como paso
   POSTERIOR sobre la salida ya escrita, en vez de modificar la funcion original
   de la vuelta 91. Si una operacion futura vuelve a llamar
   `extraer_direccion_automatica` sin encadenar este guarda a continuacion, la
   proteccion no se aplica sola: no quedo cableada por defecto.
4. **La reconstruccion de la apertura via `git stash`** (declarada arriba, en la
   cabecera): la medicion es correcta porque `dataset/` no se toco antes de la
   TAREA 3, pero el sello de `SALIDA_V92_HEAD_APERTURA.txt` se escribio despues
   de la TAREA 1, no antes de la primera operacion como manda la regla al pie de
   la letra.

## PENDIENTES DE DOCTRINA

Ninguna. Las cuatro tareas citan regla escrita: el banco `9.6.2` con su test y
su ejemplar ya registrado (TAREA 1 y 3), la propia `verificacion` de `OP-E-07`
contra el descarte silencioso y el enlace inventado (TAREA 2 y 3), y la misma
regla contra el descarte silencioso que la TAREA 2 de la vuelta 91 aplico a
`OP-E-06` (TAREA 4). El hallazgo de `run_phase1.py` (seccion de la cabecera) es
un hallazgo de PROCEDIMIENTO, no de doctrina: no pide una regla nueva, pide
disciplina de orden en los comandos.

## LA COMPARACION FINAL

`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 92 --comparar
docs/loop/REPORTE.md`, corrida DESPUES de escribir este fichero y ANTES del
commit de cierre: se cita su salida completa a continuacion, sin editar.

```
--- COMPARACION CONTRA docs/loop/REPORTE.md ---

  filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 0
  CABECERA: IDENTICA AL TALLADOR
```

EXIT 0. Salida completa en `docs/loop/SALIDA_V92_COMPARAR_CIERRE.txt`.

## COMMITS DE LA VUELTA

`git log --format='%h %s' 866d006c..HEAD` (medido al escribir esta seccion,
antes del commit de cierre): los commits de las TAREAS 1 a 4 de esta vuelta.
Este reporte va en el commit de cierre, el siguiente despues de este.

## CON EL FRENO DELANTE

La racha de CLASE O CIFRA PUBLICADA, que el acta 91 dejo en UNA de DOS, **vuelve
a CERO**: ninguna caida de esa especie en esta vuelta (medido contra el propio
encargo, punto por punto, y contra la cabecera tallada, identica al digito). La
racha de REPORTE sigue en CERO. Los cuatro discutibles de arriba se marcan ANTES
de saber si el auditor los confirma, como manda la regla.
