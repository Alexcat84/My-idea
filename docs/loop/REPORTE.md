# REPORTE DE LA VUELTA 93 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 92. Apertura: HEAD `85a250bee2495f4a23d89a4cf51338a5bcd8397e`
(el commit del acta de la vuelta 92), sellado ANTES de la primera operacion en
`docs/loop/SALIDA_V93_HEAD_APERTURA.txt` con `git rev-parse HEAD` (regla del
encargo cumplida al pie de la letra esta vez: en la vuelta 92 el sello se escribio
despues de la TAREA 1, discutible 4 de ese reporte, CONFIRMADO por el acta 92).
Cierre recomputado AL CIERRE, sobre el arbol final.

**ESTA VUELTA EJECUTA EL ENCARGO DE LA VUELTA 93** (`docs/loop/PROMPT_SIGUIENTE.md`,
que a su vez ejecuta la relectura conjunta abierta por el acta de la vuelta 92,
`ACTA_AUDITOR.md` seccion 4): la TAREA 2 (BLOQUEANTE) resuelve la relectura
conjunta del puesto 1009, con veredicto EL PAR SALE; la TAREA 3 repara el guarda
de dos condiciones en las DOS direcciones (contra el falso SALE del 3,7% y contra
el falso PASA de "prueba el problema") y lo deja CABLEADO POR DEFECTO dentro de
`extraer_direccion_automatica`; la TAREA 4 recomputa la cifra de `OP-E-07`, de 87
a 86; la TAREA 1 deja los registros en `docs/PENDIENTES.md`; y la TAREA 5 mide el
estado de la fase `04_ENLACES` sin abrir ninguna operacion nueva. **Ninguna caida
de clase o de cifra publicada en esta vuelta**, asi que la racha de esa especie,
que el acta 92 dejo en CERO, **sigue en CERO**. La racha de reporte, tambien en
CERO, sigue en CERO.

## CABECERA TALLADA (--fase04 --vuelta 93), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 93`.
Salida completa en `docs/loop/SALIDA_V93_CABECERA_TALLADA.txt`, **EXIT 0**. Antes
del commit de cierre, `--comparar docs/loop/REPORTE.md` se corre otra vez sobre
este mismo fichero ya escrito (seccion "LA COMPARACION FINAL", mas abajo).

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.193 / 9.172 / 18.365 / 9.816 | **9.192 / 9.171 / 18.363 / 9.815** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **-1 / -1 / -2 / -1** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `85a250be` (ACTA DE LA VUELTA 92 DEL AUDITOR, leido de git log), HEAD real de apertura `85a250be` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `85a250be` (ACTA DE LA VUELTA 92 DEL AUDITOR, leido de git log), HEAD real de apertura `85a250be` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**LA UNICA CELDA QUE CAMBIA ES LA RESTA DE UNA ARISTA:** `-1 / -1 / -2 / -1`, la
retirada exacta del par del puesto 1009 (`customer_discovery_phase2_problem_test ->
fit_problema_solucion`). El sha256 de `master_graph.json` cambia de
`1f0374bc3df118d9707a1983b788b318f4cc0ebffb2e6a26fddc374944b3633b` (apertura,
identico al cierre de la vuelta 92) a
`2deefc9e2e878f88876d31d9198e32d3c0397dec24f3b8a648bb62b4414ccb8e` (cierre de esta
vuelta), medido con `git show <ref>:dataset/metadata/master_graph.json | sha256sum`
sobre `85a250be` y sobre `WORK`.

**LA FILA DEL MARCADOR NO SE IMPRIME EN LA TABLA TALLADA** (mismo motivo que las
vueltas 91 y 92: el tallador `--fase04` exige el formato de diccionario y ningun
instrumento de esta vuelta lo produce en ese formato), pero se corrio a mano:
`python scripts/recomputar_marcador.py 3388` da **A 551 / B 72 / C 5 / D 2.760** en
apertura (`docs/loop/SALIDA_V93_MARCADOR_CRIBADO_APERTURA.txt`) y en cierre
(`..._CIERRE.txt`), **sin cambio** (`diff` de los dos ficheros, vacio): la clase D
del 1009 es correcta y no se discute, lo que se discutia era la DIRECCION.

**LA VARA MAS DURA, EL DIFF DE LA UNION ENTERA DEL GRAFO** entre la apertura
(`85a250be`) y el cierre (`WORK`), `docs/loop/SALIDA_V93_DIFF_UNION.txt`: **solo en
apertura (borradas): 1 (`customer_discovery_phase2_problem_test ->
fit_problema_solucion`) | solo en cierre (nuevas): 0**. Exactamente la retirada que
la relectura conjunta ordena, nada mas.

El ciclo de tres (`scripts/run_phase1.py --reaplico-curaduria`,
`scripts/etiquetas_de_cara.py --aplicar`, `scripts/sync_assets_web.py`) se corrio
completo en la apertura y en el cierre, verificado con el motor (25/25), la web
(80/1030+3) y `tsc` (EXIT 0) las dos veces. La via de OP-C-05
(`scripts/loop/vuelta89_tarea4_guarda_op_c05.py --antes/--despues --vuelta 93`) dio
**935 entradas que sobran ANTES y 935 DESPUES: VERDE**, la cuenta no crecio
(`docs/loop/SALIDA_V93_GUARDA_OPC05_DESPUES.txt`).

## TAREA 2 (BLOQUEANTE): LA RELECTURA CONJUNTA DEL PUESTO 1009, RESUELTA: EL PAR SALE

**Por que.** El acta de la vuelta 92 (`ACTA_AUDITOR.md`, seccion 4, lineas 31977 a
32106) discrepo de SU PROPIA adjudicacion de la vuelta 91 sobre el puesto 1009 y
la mando a RELECTURA CONJUNTA (`docs/loop/AUDITOR.md` seccion 1.3), con la
decision reservada a esta vuelta.

**LA UNICA PREGUNTA QUE `OP-E-07.verificacion` MANDA HACER** (`docs/plan/
OPERACIONES.jsonl`, linea 69): *"NO SE RELEE EL PAR: se lee su razon, que ya esta
escrita. Si la razon tampoco lo dice, el par sale de la cosecha y se anota por
que"*. No es si hay jerarquia posible entre los dos nodos: es si LA RAZON NOMBRA
cual de los dos es la madre.

`scripts/loop/vuelta93_tarea2_relectura_1009.py` (`docs/loop/
SALIDA_V93_TAREA2_RELECTURA_1009.txt`) lee la razon completa del 1009 y la
contrasta contra los dos ejemplares ya adjudicados y escritos:

| puesto | como nombra al otro nodo | nombra "la madre" literal | linea con paso numerado | contradice el 9.6.2 |
|---:|---|---|---|---|
| **1083** (CONFIRMADO, acta 91) | "trae un procedimiento que **LA MADRE** no tiene" | SI | no hace falta, ya nombra | no |
| **1098** (CAYO, vuelta 92) | "trae un procedimiento de entrevista que **el otro** no tiene en ninguna forma" | NO | NO | no (sale por negar la jerarquia) |
| **1009** (esta vuelta) | "trae un procedimiento que **esa fase** no tiene" | NO | NO | **SI**: "el bloque de traccion queda fuera" del solape |

**Las tres mediciones apuntan al mismo lado:** (1) la formula "que esa fase no
tiene" es la de la clase D, palabra por palabra en su forma, igual que la del
1098 y distinta de "que la madre no tiene" del 1083; (2) "prueba el problema:"
no introduce una linea, introduce los CINCO pasos enteros del nodo; (3) la propia
razon declara que el bloque de traccion del hijo escrito queda FUERA del solape,
lo que hace fallar el test del banco `9.6.2` (`BANCO_DE_TEXTOS.md` lineas 1771 a
1774: *"el hijo cabe entero dentro de UN paso de la madre"*).

**VEREDICTO: la razon del 1009 NO NOMBRA cual nodo es la madre.** Por
`OP-E-07.verificacion`, **EL PAR SALE**, con el mismo tratamiento que el 1098 en
la vuelta 92. **EL MARCADOR NO SE TOCA**: la clase D del 1009 es correcta, lo que
no sostenia era la DIRECCION (mismo criterio que el acta 91 aplico al 1098).

## TAREA 3: EL GUARDA REPARADO EN LAS DOS DIRECCIONES, Y CABLEADO POR DEFECTO

`scripts/loop/vuelta93_tarea3_guarda_direccion.py` hereda `guarda_direccion(razon)`
de la vuelta 92 sin cambiar su estructura booleana, y repara la lista de
`MARCA_MADRE_POSITIVA`:

**(a) CONTRA EL FALSO SALE, medido por el acta 92 sobre un TERCER CONJUNTO de 81
razones** (los pares de `docs/plan/COSECHA_RAZONES_D.jsonl` con senales "formula
de la vara" o "procedimiento de esa linea", menos los 202 puestos de las dos
bolsas oficiales): reconstruido por codigo propio en esta vuelta
(`--tercer-conjunto`, `docs/plan/OP_E_07_TERCER_CONJUNTO_V93.jsonl`), **tambien 81
filas, sin discrepancia con la cifra del acta**. Tumbaba 3 pares SANOS (995, 1007,
1024) porque sus razones nombran la linea con una preposicion que la lista de la
vuelta 92 no traia ("termina/cierra/empieza CON UNA LINEA"), y el 995 ademas
cierra con "el paso nombra, el hijo ejecuta". **Reparado** anadiendo esas cuatro
formulas, cada una citada con el puesto que la motivo, CON LA MISMA LOOKAHEAD
NEGATIVA que excluye "linea compartida" (se anadieron como alternativas NUEVAS,
sin tocar las alternativas viejas de "en UNA LINEA" / "es UNA LINEA": el primer
borrador de esta reparacion fundio todo en un solo patron "VERBO PREPOSICION
LINEA" y eso TUMBO el CASO 1 y el CASO 2 de la vara al perder la forma "en UNA
LINEA" sin verbo especifico delante; el fichero deja esa trampa documentada en su
propio comentario).

**(b) CONTRA EL FALSO PASA**: la alternativa "prueba el problema" (anadida en la
vuelta 92 citando SOLO el puesto 1009) hacia PASAR el 1009, el 1411 y el 1557 sin
merecerlo: es su UNICO sosten, y la formula es la de la clase D (ver TAREA 2).
**Retirada de la lista.** Verificado que el 1397 (la cuarta aparicion de "prueba
el problema" en las 3.388 razones) sigue PASANDO por otra marca ("paso 4") y no
se ve afectado. "Es un habito" (1281) se queda en la lista, declarado
INVERIFICABLE (una sola aparicion en 3.388 razones, sin un segundo puesto contra
el que probarlo).

**(c) LA VARA, LOS TRES CASOS OBLIGATORIOS** (`python
scripts/loop/vuelta93_tarea3_guarda_direccion.py --vara`, `docs/loop/
SALIDA_V93_TAREA3_VARA.txt`, EXIT 0):

```
CASO 1: las 88 de OP_E_07_REBASE_V91.jsonl -> SALEN: 2 [1009, 1098]. OK (esperado: {1009, 1098}).
CASO 2: las 114 de OP_E_06_DIRECCION_V90.jsonl -> SALEN: 0 []. el 1160 da PASA. OK.
CASO 3: el tercer conjunto (81 filas, reconstruido) -> SALEN: 0. los tres falsos SALE (995, 1007, 1024) PASAN. OK.
LA VARA ALCANZA: los tres casos obligatorios se cumplen.
```

**EL CASO ROJO, PROBADO POR MUTACION** (`--mutacion`, `docs/loop/
SALIDA_V93_TAREA3_MUTACION.txt`, EXIT 0): SEIS casos, cada uno mutando una entrada
real y verificando que el veredicto CAMBIA. Dos heredados de la vuelta 92 (1098
SALE a PASA inyectando marca; 1160 PASA a SALE quitando marca). Cuatro nuevos de
esta vuelta: el 1009 (SALE a PASA inyectando marca en vez de "prueba el
problema"); el 1007 (PASA a SALE quitando "cierra con UNA LINEA", su unica
marca, verificado aparte que no trae ninguna otra); y el 995 en DOS pasos, porque
trae DOS marcas nuevas a la vez ("termina con UNA LINEA" y "el paso nombra, el
hijo ejecuta") y quitar una sola no mueve el veredicto (la otra lo sostiene
sola): se neutraliza primero una, se comprueba que el veredicto SIGUE PASA por la
otra, y ESA es la entrada del caso que prueba la segunda.

**(d) LA VARA NUEVA, EL TERCER CONJUNTO, reconstruido con codigo propio, no
copiado del acta**: los pares de `COSECHA_RAZONES_D.jsonl` con senales "formula
de la vara" o "procedimiento de esa linea", menos los puestos de las dos bolsas
oficiales, dan **81 filas**, la MISMA cifra que el acta 92 midio (sin
discrepancia que declarar). Sobre ese conjunto, con el guarda reparado: **0
SALEN**. Los tres falsos SALE conocidos pasan y ningun otro sale: la vara del
tercer conjunto **ALCANZA**.

**(e) CABLEADO POR DEFECTO** (discutible 3 del reporte de la vuelta 92,
CONFIRMADO por el acta 92 seccion 2.3): `extraer_direccion_automatica`
(`scripts/loop/vuelta91_tarea4_direccion_ope07.py`) ahora llama al guarda ELLA
MISMA antes de devolver, en vez de depender de un filtro posterior que un
llamador futuro pudiera olvidar encadenar. Verificado
(`docs/loop/SALIDA_V93_TAREA3E_VERIFICACION_CABLEADO.txt`): una corrida fresca de
la deteccion automatica sobre la bolsa de 88 excluye 1098 y 1009
AUTOMATICAMENTE, sin ningun filtro aparte. La prueba de mutacion ORIGINAL de la
vuelta 91 (`vuelta91_tarea4_prueba_mutacion_direccion.py`) se corrio de nuevo sin
tocarla y sigue en EXIT 0 (`docs/loop/SALIDA_V93_TAREA3E_MUTACION_HEREDADA.txt`):
su razon fabricada trae "en su paso 2, en UNA LINEA", que el guarda reconoce
como marca de madre positiva y no interfiere. El fichero `OP_E_07_DIRECCION_V91.jsonl`
ya escrito en la vuelta 91 NO se toco ni se regenero: el cableado solo afecta
corridas nuevas de la funcion.

**(f) LA NOTA DE LECTURA DEL ACTA 92, sobre `guarda_direccion`**: la rama `if
niega and not tiene_marca` sigue siendo INALCANZABLE (la estructura booleana no
cambio, solo la lista de (a) crecio y perdio una entrada). No es un defecto
nuevo, se deja comentada igual, como el acta 92 sugirio.

## TAREA 3(retiral): LA RETIRADA DE LA ARISTA DEL 1009

`scripts/loop/vuelta93_tarea3a_filtrar_1009.py` corre el guarda reparado fila por
fila sobre las 87 de `docs/plan/OP_E_07_DIRECCION_V92.jsonl` y **saca
EXACTAMENTE `[1009]`** (ROJO si sacara otra cosa): escribe
`docs/plan/OP_E_07_DIRECCION_V93.jsonl`, **86 filas**.
`scripts/loop/vuelta93_tarea3b_retirar_1009.py` resuelve alias (misma `res()`
canonica de siempre) y quita `fit_problema_solucion` de `nodos_siguientes` de
`customer_discovery_phase2_problem_test` Y quita `customer_discovery_phase2_problem_test`
de `nodos_previos` de `fit_problema_solucion`, en la misma corrida o ninguna.
Resultado: `RETIRADA`. **Idempotencia probada**: segunda corrida,
`RESULTADO: NO_ESTABA`, `RETIRADAS ESTA CORRIDA: 0`, y los dos ficheros de nodo
hasheados antes y despues de esa segunda corrida: **identicos byte a byte**
(`docs/loop/_v93_sha_antes_idem.txt`).

| guarda | antes | despues |
|---|---:|---:|
| `vuelta89_tarea4_guarda_op_c05.py --vuelta 93` | 935 entradas que sobran | 935 (**+0, VERDE**) |
| censo (`nodos/vivos/deprecados`) | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665, IGUAL** |
| Gate 0 | OK | **OK** |
| motor | 25/25 | **25/25** |
| web | 80/1030+3 | **80/1030+3** |
| tsc | EXIT 0 | **EXIT 0** |
| diff de la union contra el cierre de la vuelta 92 (`85a250be`) | (referencia) | **1 borrada (el 1009), 0 nuevas** |

## TAREA 4: LA CIFRA DE `OP-E-07`, DE 87 A 86

Escrita en `docs/plan/04_ENLACES.md`, en la MISMA seccion que la vuelta 92 abrio
("LA CIFRA DE `OP-E-07`, ENTERA, DE 101 A 87"), sin borrar ninguna fila ni
blockquote viejo: se anade una nota de actualizacion al principio de la seccion,
DOS filas nuevas a la tabla (10 y 11, la relectura del 1009 y su retirada) y una
SEGUNDA cadena citada al final, dejando la primera intacta y marcada "cifra
vigente hasta la vuelta 92":

> **101 -> (-13 dedupe frente 4) -> 88 -> (0 excluidos 9.22, 0 sin direccion) ->
> 88 con direccion -> (-1 guarda de dos condiciones, banco 9.6.2, el 1098) -> 87
> con direccion -> (-1 guarda reparado, banco 9.6.2, el 1009, relectura conjunta
> de la vuelta 93) -> 86 con direccion -> 84 ESCRITA + 2 YA_ESTABA (1388, 1946) +
> 0 ESCALERA_ROTA.** Cifra vigente desde la vuelta 93.

El `ADDENDUM DE EJECUCION` de `OP-E-07` en `docs/plan/OPERACIONES.jsonl` se
reescribe (`scripts/loop/vuelta93_tarea4_reescribir_addendum.py`,
`docs/loop/SALIDA_V93_TAREA4_ADDENDUM.txt`) anadiendo al final del campo `nota`,
**sin tocar ni una palabra de lo que ya estaba** (verificado: las 71 lineas del
fichero siguen siendo JSON valido linea a linea, y el texto de las vueltas 91 y
92 sigue presente en la nota). `estado` se queda en `LISTA`.

## TAREA 5: EL ESTADO DE LA FASE `04_ENLACES`, MEDIDO

`docs/loop/SALIDA_V93_TAREA5_ESTADO_FASE04.txt`, recorriendo
`docs/plan/OPERACIONES.jsonl` filtrado por `fase == "04_ENLACES"`, ordenado por
`orden`:

| orden | operacion | estado | tiene addendum/cierre |
|---:|---|---|---|
| 1 | `OP-E-01` | LISTA | SI ("CIERRE MEDIDO", "CIFRA FINAL") |
| 2 | `OP-E-02` | **HECHA** | (estado ya lo dice) |
| 3 | `OP-E-03` | LISTA | NO (nota de 550 caracteres, solo descripcion) |
| 4 | `OP-M-03-ENLACES` | LISTA | NO (248 caracteres) |
| 5 | `OP-E-04` | LISTA | NO (760 caracteres) |
| 6 | `OP-E-05` | LISTA | NO (444 caracteres) |
| 7 | `OP-M-01-ESLABONES` | LISTA | NO (490 caracteres) |
| 8 | `OP-M-01-SEXTO` | LISTA | NO (424 caracteres) |
| 9 | `OP-E-06` | LISTA | SI ("ADDENDUM DE EJECUCION") |
| 10 | `OP-E-07` | LISTA | SI ("ADDENDUM DE EJECUCION") |

Las dependencias de las seis sin addendum (`OP-U-02`, `OP-M-03-I`, `OP-M-03-II`,
`OP-M-03-III`, `OP-M-01`, `OP-M-01-FUSION`) estan TODAS en `estado: LISTA`, que en
este plan **no distingue ejecutado de pendiente** (el propio addendum de
`OP-E-07` lo dice: "el estado de verdad es el repo y el commit, no un campo
nuevo"), asi que NO PUDE DETERMINAR CON CERTEZA si esas seis operaciones estan
listas para abrirse sin leer sus fichas completas, algo que esta vuelta no hizo.

**NO SE ABRE NINGUNA OPERACION NUEVA esta vuelta.** Las TAREAS 1 a 4 (la
relectura bloqueante, la reparacion del guarda en las dos direcciones con tres
varas obligatorias, la retirada con instrumento y el recomputo) ya llenaron el
alcance que esta vuelta podia sostener con cuidado; el encargo pide medir antes
de empezar una operacion nueva, no empezarla porque queda tiempo de vuelta.
Queda para la vuelta siguiente determinar, leyendo las fichas de `OP-E-03` y sus
dependencias, cual es la que de verdad sigue en el orden del `00_INDICE`.

## LO QUE NO SE TOCO, verificado y no solo declarado

- **`OP-E-06` no se reabrio**: el guarda reparado sigue dejando PASAR el 1160 y 0
  SALEN de los 114 (vara caso 2).
- **El marcador no se movio**: A 551 / B 72 / C 5 / D 2.760 en apertura y en
  cierre.
- **Los otros 85 de `OP-E-07` se quedan**: el diff de la union solo trae UNA
  borrada.
- **`OP_E_07_DIRECCION_V91.jsonl` (el fichero historico de la vuelta 91) no se
  toco ni se regenero**: el cableado de la TAREA 3(e) solo afecta corridas
  nuevas de `extraer_direccion_automatica`.

## DISCUTIBLES MARCADOS, PARA LA RELECTURA CIEGA DEL AUDITOR

1. **El cableado de la TAREA 3(e) se hizo editando el fichero historico
   `scripts/loop/vuelta91_tarea4_direccion_ope07.py`**, en vez de crear un
   modulo aparte que un llamador tendria que elegir usar. Es la primera vez en
   esta campana que un script de una vuelta cerrada se edita en una vuelta
   posterior (verificado: `git log --follow` sobre ese fichero mostraba un solo
   commit antes de esta vuelta). Se opto por editarlo porque es la UNICA forma
   de que "una operacion futura que llame a `extraer_direccion_automatica` no
   pueda saltarse el guarda sin querer" (la redaccion literal del encargo): un
   modulo aparte es exactamente lo que la vuelta 92 ya probo que no basta
   (discutible 3 de ese reporte). El precedente que se cito para permitirlo es
   `scripts/loop/tallar_cabecera_reporte.py` ("NOMBRE ESTABLE A PROPOSITO", que
   SI se extiende vuelta tras vuelta sin clonarse), pero ese fichero es un
   instrumento de MEDICION que nunca fue la salida decidida de una vuelta
   cerrada, mientras que `vuelta91_tarea4_direccion_ope07.py` SI lo es
   (`OP_E_07_DIRECCION_V91.jsonl` es su salida congelada). Si el auditor
   considera que esta distincion no alcanza para justificar la edicion, el
   remedio correcto seria revertir el cableado a un modulo aparte y aceptar
   que "no pueda saltarselo sin querer" no se logra del todo, dejandolo
   declarado como en la vuelta 92.
2. **La lista de `MARCA_MADRE_POSITIVA` sigue siendo un guarda ajustado a los
   conjuntos que la ha probado** (las 88 de `OP-E-07`, las 114 de `OP-E-06`, y
   ahora el tercer conjunto de 81): el acta 92 ya lo declaro sobre la version
   anterior y sigue siendo cierto sobre esta, con un conjunto mas de prueba
   pero sin ser una gramatica general. Una razon nueva con un verbo de
   atribucion que no este en ninguna de las tres bolsas puede seguir marcando
   un par SANO como SALE sin que el guarda lo sepa.
3. **La reconstruccion del tercer conjunto dio 81, IGUAL que el acta**: no hubo
   discrepancia que declarar, pero tampoco hay una SEGUNDA fuente independiente
   que confirme que 81 es la cifra correcta mas alla de que las dos
   reconstrucciones (la del auditor y la de esta vuelta) usaron la misma
   definicion escrita en el encargo. Si esa definicion misma tuviera un hueco,
   los dos calculos lo heredarian igual.
4. **TAREA 5 se quedo en la medicion, sin abrir operacion nueva**: es una
   eleccion de alcance del ejecutor (declarada arriba con su razon), no una
   imposibilidad tecnica. Si el auditor prefiere que la vuelta siguiente abra
   directamente `OP-E-03` sin releer sus dependencias, o que se lean las
   fichas de las seis operaciones sin addendum antes de decidir el orden real,
   son dos caminos distintos y el encargo de la 94 puede elegir cualquiera de
   los dos.

## PENDIENTES DE DOCTRINA

Ninguna. Las cinco tareas citan regla escrita: `OP-E-07.verificacion` (la
relectura del 1009 y su retirada), el banco `9.6.2` con su test y su ejemplar ya
registrado (TAREA 2), la misma regla contra el descarte silencioso que motivo el
guarda de la vuelta 92 (TAREA 3), y el criterio de `estado: LISTA` que el propio
addendum de `OP-E-07` ya declaro por escrito (TAREA 5).

## LA COMPARACION FINAL

`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 93 --comparar
docs/loop/REPORTE.md`, corrida DESPUES de escribir este fichero y ANTES del
commit de cierre: se cita su salida completa a continuacion, sin editar.

```
--- COMPARACION CONTRA docs/loop/REPORTE.md ---

  filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 0
  CABECERA: IDENTICA AL TALLADOR
```

EXIT 0. Salida completa en `docs/loop/SALIDA_V93_COMPARAR_CIERRE.txt`.

## COMMITS DE LA VUELTA

`git log --format='%h %s' 85a250be..HEAD` (medido al escribir esta seccion, antes
del commit de cierre):

```
9643e5bd VUELTA 93, TAREA 5: el estado de la fase 04_ENLACES, medido, ninguna operacion nueva abierta.
52a4baa6 VUELTA 93, TAREA 1: los registros de PENDIENTES.md.
229e3647 VUELTA 93, TAREA 4: la cifra de OP-E-07 recomputada, de 87 a 86 (el 1009 sale).
39053558 VUELTA 93, TAREA 3(a-c cont.): retirada del 1009 de OP-E-07 por el guarda reparado.
1e91831e VUELTA 93, TAREA 3: guarda reparado en las dos direcciones, cableado por defecto.
f73adb67 VUELTA 93, TAREA 2 (BLOQUEANTE): relectura conjunta del puesto 1009, EL PAR SALE.
```

Este reporte va en el commit de cierre, el siguiente despues de estos seis.

## CON EL FRENO DELANTE

La racha de CLASE O CIFRA PUBLICADA, que el acta 92 dejo en CERO, **sigue en
CERO**: ninguna caida de esa especie en esta vuelta (medido contra el propio
encargo, punto por punto, y contra la cabecera tallada, identica al digito). La
racha de REPORTE sigue en CERO. Los cuatro discutibles de arriba se marcan ANTES
de saber si el auditor los confirma, como manda la regla. La discrepancia que el
acta 92 trajo sobre el 1009 se resolvio CON LA VARA, no por deferencia ni por
contradiccion: la medicion de esta vuelta coincide con la lectura del auditor, y
se dice sin adornarla, porque coincidir tampoco es lo mismo que copiar sin medir.
