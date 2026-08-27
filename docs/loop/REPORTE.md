# REPORTE DE LA VUELTA 91 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 90. Apertura sellada ANTES de la primera operacion en
`docs/loop/SALIDA_V91_HEAD_APERTURA.txt`: `675b9969a93d23c92f217d4ff66f9a0357998bbc`
(el commit del acta de la vuelta 90, medido con `git rev-parse 675b9969` en esta
vuelta, ver nota de identidad mas abajo). Cierre recomputado AL CIERRE.

**ESTA VUELTA EJECUTA EL ENCARGO DE LA VUELTA 90** (acta del auditor,
`ACTA_AUDITOR.md` linea 30395 y siguientes): la TAREA 1 corrige la recomendacion
de `PENDIENTES.md` sobre los tres pares del banco 9.22 (2082, 2084, 2112) tras
una relectura dirigida que NO sostiene la etiqueta "enlace mutuo"; la TAREA 2
escribe en `04_ENLACES.md` la cadena medida y citable de 192 a 113 de `OP-E-06`;
la TAREA 3 (BLOQUEANTE) extiende el tallador a cifras de COMPOSICION de una
salida de texto, la clase exacta que fallo en la vuelta 90; y la TAREA 4 ejecuta
`OP-E-07`, que ABRE con **86 aristas ESCRITAS** (mas 2 filas `YA_ESTABA`, 88
leidas de 101). La racha de reporte queda en la que trae el encargo (UNA de
tres): **ninguna caida nueva de esta especie en esta vuelta.**

## CABECERA TALLADA (--fase04 --vuelta 91), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 91`.
Salida completa en `docs/loop/SALIDA_V91_CABECERA_TALLADA.txt`, **EXIT 0**. Antes
del commit de cierre, `--comparar docs/loop/REPORTE.md` se corre otra vez sobre
este mismo fichero ya escrito (seccion "LA COMPARACION FINAL", mas abajo).

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.108 / 9.087 / 18.195 / 9.731 | **9.194 / 9.173 / 18.367 / 9.817** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+86 / +86 / +172 / +86** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `675b9969` (ACTA DE LA VUELTA 90 DEL AUDITOR, leido de git log), HEAD real de apertura `675b9969` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `675b9969` (ACTA DE LA VUELTA 90 DEL AUDITOR, leido de git log), HEAD real de apertura `675b9969` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**LA FILA DEL MARCADOR NO SE IMPRIME A PROPOSITO** (mismo motivo que la vuelta
90): corri `python scripts/recomputar_marcador.py 3388` en apertura y en cierre
(los dos dan **A 551 / B 72 / C 5 / D 2.760, n 3.388, sin cambio**, guardado en
`docs/loop/SALIDA_V91_MARCADOR_CRIBADO_APERTURA.txt` y `..._CIERRE.txt`), pero el
tallador `--fase04` exige el formato de diccionario (`'A': (\d+)`) para esa fila
y ningun instrumento de esta vuelta lo produce; por la regla "la celda que no
salga de un instrumento no se escribe", la fila opcional no se talla. **El
marcador NO se movio esta vuelta** (fase 04 no toca el cribado).

**LAS ARISTAS SON LA UNICA CELDA QUE CAMBIA (fuera de las derivadas), Y ES LA
ESCRITURA DE `OP-E-07`:** `+86 / +86 / +172 / +86`, exactamente las 86 aristas
ESCRITAS (ver TAREA 4). El sha256 de `master_graph.json` **cambia**: de
`9acfc02d9c80e3ba1793de7c28ea44b499dbc79711d13dea83db4a3706484b42` (apertura,
identico al cierre de la vuelta 90) a
`a2936350db530f80c39e07fe96c92770f26453af6c09378a74b5eb005ff12738` (cierre de
esta vuelta), medido con `git show <ref>:dataset/metadata/master_graph.json |
sha256sum` sobre las dos refs.

**LA VARA MAS DURA, EL DIFF DE LA UNION ENTERA DEL GRAFO** entre la apertura
(`675b9969`) y el cierre (`WORK`), `docs/loop/SALIDA_V91_DIFF_UNION.txt`: **solo
en apertura (borradas): 0 | solo en cierre (nuevas): 86**, y esas 86 CALZAN
EXACTO, conjunto contra conjunto, contra las 86 filas `ESCRITA` del log de
escritura (verificado con un cotejo propio, sin diferencia).

El ciclo de tres (`scripts/run_phase1.py --reaplico-curaduria`,
`scripts/etiquetas_de_cara.py --aplicar`, `scripts/sync_assets_web.py`) se corrio
completo en la apertura (sobre el arbol pristino, tras un `git stash` temporal de
los cambios de la TAREA 4 para poder medir la apertura sin perderlos, restaurados
despues con `git stash pop`) y en el cierre (sobre el arbol ya con las 86
aristas escritas), verificado con `git status --porcelain -- dataset/
web/lib/assets/` en CERO despues del ciclo completo las dos veces.
`etiquetas_de_cara.py` cambia las mismas 71 etiquetas las dos veces (no
persisten en `dataset/nodos/`, se recalculan cada vez que `run_phase1.py`
recompila `master_graph.json`; comportamiento esperado, verificado igual en la
apertura y en el cierre, y ya declarado en el reporte de la vuelta 90).

## TAREA 1: LA RELECTURA DIRIGIDA DEL BANCO 9.22 (2082, 2084, 2112)

El encargo (acta 90, adjudicacion 4.1) pedia una relectura dirigida contra el
test de las DOS LINEAS del banco 9.22 antes de tocar la recomendacion escrita en
`docs/PENDIENTES.md` en la vuelta 90. La relectura, hecha en esta vuelta sobre el
campo `razon` COMPLETO de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`: **cada una de
las tres razones nombra UNA SOLA linea explicita con su paso**, y justifica el
"segundo sentido" con la formula de reparto que el banco reserva para la clase D
(*"cada uno trae lo suyo"*), no con una segunda linea identificada en el otro
nodo. **VEREDICTO: NO SOSTIENE.** La direccion, leida con la misma vara de
`vuelta90_tarea4_direccion_ope06.py` (quien dice la linea es la madre, quien
trae el procedimiento de esa linea es el hijo):

| puesto | direccion (madre -> hijo) |
|---:|---|
| 2082 | `validacion_con_franquiciados` -> `preparar_candidato_validacion` |
| 2084 | `gestion_responsabilidad_vicaria` -> `control_responsabilidad_manual` |
| 2112 | `capitalizacion_adecuada_del_franquiciador` -> `estimacion_inversion_inicial_franquiciador` |

**LA EXCLUSION DE `OP-E-06` NO SE TOCA** (los tres siguen sin escribirse: era
correcta por la letra de la operacion, no por la etiqueta). **LO QUE SE
CORRIGE** es la recomendacion: correccion aditiva en `docs/PENDIENTES.md`, sin
borrar el texto viejo, citando `ACTA_AUDITOR.md` (lineas 30626 a 30638, 30788 a
30811) y `BANCO_DE_TEXTOS.md` (lineas 2523, 2539 a 2541, 2577 a 2580, 2594 a
2602). Los tres pasan de candidatos de ENLACE MUTUO a candidatos de escalera de
una sola direccion, en una pasada posterior fuera de `OP-E-06` (misma familia
que los puestos 581 y 650 ya anotados). Commit `56e0f84c`.

## TAREA 2: LA CIFRA DE `OP-E-06`, 192 A 113, ESCRITA ENTERA

Nueva seccion en `docs/plan/04_ENLACES.md` ("LA CIFRA DE `OP-E-06`, ENTERA, DE
192 A 113"): doce eslabones, cada uno con su fuente (acta, fichero o
instrumento), citando lineas exactas de las salidas de las vueltas 88, 89 y 90:

> 192 (evidencia con direccion explicita) -> (-16, frente 4 del dedupe; los
> otros tres frentes en 0) -> 176 -> (-47, sin palabra de direccion) -> **129**
> (bolsa V88) -> (-12, releidas enteras sin desarrollo real) -> **117** (bolsa
> V89) -> [bloqueo: la reversion de la fila 117 de `OP-E-01`, NO un conteo de
> la bolsa, liberado en la vuelta 89] -> **117** (bolsa V90, +1/-1 por las
> adjudicaciones 4.1/4.2 del acta 89: ENTRA 530, SALE 932) -> (-3, banco 9.22)
> -> **114** con direccion -> **113 ESCRITA + 1 YA_ESTABA + 0 ESCALERA_ROTA**.

Cada eslabon del 192 al 129 sale de `docs/loop/SALIDA_V88_TAREA5_REBASE_OPE06.txt`
(TAREA 5.a/5.b/5.c de la vuelta 88, lineas citadas en `04_ENLACES.md`); el
eslabon a 117 (V89) sale de `docs/loop/SALIDA_V89_TAREA3_REBASE_OPE06.txt`; el
paso de V89 a V90 (117 a 117, conjunto distinto) esta verificado por el auditor
en `ACTA_AUDITOR.md` lineas 30565 a 30572; y el cierre (113/1/0) sale de
`docs/loop/SALIDA_V90_TAREA4_ESCRITURA.txt`, cruzado contra el diff de la union
del grafo por el auditor en su acta 90, seccion 1.7. Commit `56e0f84c`.

## TAREA 3 (BLOQUEANTE): EL TALLADOR DE CIFRAS DE COMPOSICION

**Por que era bloqueante:** la caida de reporte de la vuelta 90 (acta 90, seccion
3.1) fue una cifra de COMPOSICION ("cuantas filas de esta salida se resolvieron
por alias") que `tallar_conteo_campo.py` (solo mide LONGITUD de un campo de un
JSONL) no podia tallar. El auditor lo encargo con la racha de reporte en UNA y no
en DOS, declarando por que en su seccion 6.1: el remedio construido no cubria la
caida que ocurrio.

`scripts/loop/tallar_composicion_salida.py`, hermano nuevo: dado un fichero de
salida y un patron de clasificacion (regex con grupos nombrados), cuenta filas
por clase, ENUMERA los puestos de cada clase, coteja esa enumeracion contra una
lista citada (marca SOBRAN y FALTAN), y opcionalmente cuenta pares de
sustitucion DISTINTOS comparando el par escrito contra el par crudo, posicion a
posicion (necesario porque "filas" y "pares distintos" son cifras DISTINTAS
cuando una misma sustitucion de nodo se repite en varias filas).

**VARA DURA, corrida y citada** (`docs/loop/SALIDA_V91_TAREA3_COMPOSICION.txt`,
EXIT 0): sobre `docs/loop/SALIDA_V90_TAREA4_ESCRITURA.txt`, clase "resuelto por
alias", da **CATORCE filas, ONCE pares de sustitucion distintos**, y al cotejar
contra la lista de once que el reporte de la vuelta 90 publico marca **1207 y
1535 como FALTAN** (ademas del 2015, que el reporte de la vuelta 90 ya trataba
en otra seccion): exactamente el agujero que `tallar_conteo_campo.py` no podia
ver.

**Caso rojo probado por mutacion**
(`docs/loop/SALIDA_V91_TAREA3_MUTACION.txt`, EXIT 0), sobre `clasifica_fila()`,
la unica pieza de juicio del tallador nuevo: mutando el campo real de una fila
fabricada (`"sin alias"` a un par real de alias), el veredicto cambia de `"sin
alias"` a `"resuelto por alias"`, como exige el arnes de
`verificar_caso_rojo_por_mutacion.probar_por_mutacion`.

**Mecanica de ROJO verificada con tres entradas malas** (fichero inexistente,
patron que no casa ninguna linea, campo-clase ausente de los grupos del patron):
en los tres casos, **EXIT 1 y CERO lineas impresas antes del mensaje ROJO**
("NO SE TALLA NADA" es literal, no hay tabla parcial delante).

**Pulido del mismo paquete** (acta 90, seccion 1.11): `tallar_conteo_campo.py`
ahora valida la existencia de `--verificar-puestos` ANTES de imprimir la tabla
de distribucion, para que un ROJO por puesto inexistente no imprima primero una
tabla y diga "NO SE TALLA NADA" despues (la observacion menor de la vuelta 90).
El caso obligatorio de la vuelta 90 se reproduce identico (397/270/23/104, 2023
y 2082 DISTINTOS de 200). Commit `5783d081`.

## TAREA 4: `OP-E-07` ABRE, 86 ARISTAS ESCRITAS

**Re-base de la bolsa (101 de la ficha, core 74 / environmental 12 /
exportacion 11 / entrega 4, confirmado)** contra el grafo de hoy con los mismos
cuatro frentes de dedupe que `OP-E-06` (`scripts/loop/
vuelta91_tarea4_rebase_ope07.py`, la misma logica de `vuelta88_tarea5_rebase_ope06.py`
copiada sin variar): frentes 1, 2 y 3 quitan **0**; frente 4 (arista ya en el
grafo de hoy, resolviendo por alias) quita **13**, nombrados uno a uno. Quedan
**88** (`docs/plan/OP_E_07_REBASE_V91.jsonl`,
`docs/loop/SALIDA_V91_TAREA4_REBASE_OPE07.txt`, EXIT 0).

**Direccion de los 88, leida de la razon COMPLETA** (`scripts/loop/
vuelta91_tarea4_direccion_ope07.py`, `docs/loop/SALIDA_V91_TAREA4_DIRECCION.txt`,
EXIT 0), NO de la frase truncada (la leccion de la TAREA 3.a de la vuelta 90,
que fue justo la que dio los tres del 9.22): un criterio automatico
(`extraer_direccion_automatica`, aislado y probado por mutacion) toma, para
cada nodo, el segmento de texto desde su primera mencion hasta la mencion del
otro id, y busca la marca de hijo ("trae", sin ser la formula autoreferencial
"trae lo suyo", ni "desarrolla", ni "RECORRE EL CAMINO"); si exactamente un
segmento la trae, ese id es el hijo. Resuelve **80 de 88**. **OCHO leidas a
mano**, citadas con su frase literal en `DIRECCION_MANUAL` del propio script,
porque su razon dice quien es la madre con una formula distinta a "trae" (ES EL
INDICE / ES EL PROCEDIMIENTO DE UNA, ENUMERA / DIBUJA UNA, MONTA EL MARCO / LLENA
LA PATA, o nombra "la madre" literalmente): puestos 1163, 1191, 1388, 1500,
1778, 1847, 1886, 1992. **CERO excluidos por banco 9.22** (verificado en tiempo
de ejecucion: ninguna de las 88 razones cita "9.22" ni "ENLACE MUTUO"). **CERO
sin direccion resoluble.** Verificado: 88 con direccion + 0 excluidos + 0 sin
direccion = 88 (`docs/plan/OP_E_07_DIRECCION_V91.jsonl`, 88 filas).

**Escritura, con la via de OP-C-05 cableada:**

```
python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --vuelta 91 --antes
python scripts/loop/vuelta91_tarea4_escribir_ope07.py
python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --vuelta 91 --despues
```

`--antes`: **935 entradas que sobran, 711 nodos** (`docs/loop/
SALIDA_V91_GUARDA_OPC05_ANTES.txt`), identico a la linea base de las vueltas 89
y 90. `--despues`: **935 entradas que sobran** (`docs/loop/
SALIDA_V91_GUARDA_OPC05_DESPUES.txt`): **VERDE, la cuenta no crecio (+0)**.

La escritura (`scripts/loop/vuelta91_tarea4_escribir_ope07.py`, misma semantica
canonica de `resolverId` que `OP-E-06`, copiada sin variar) da **86 ESCRITA + 2
YA_ESTABA + 0 ESCALERA_ROTA** de 88 (`docs/loop/SALIDA_V91_TAREA4_ESCRITURA.txt`,
EXIT 0). **Los dos `YA_ESTABA`, nombrados:**

1. **Puesto 1388** (`ocho_fases_experiencia_cliente -> fase_acclimate_experiencia_cliente`):
   la misma arista que el puesto **1020** de la misma bolsa (`fases_de_retencion_de_clientes
   -> fase_acclimate_experiencia_cliente`, resolviendo por alias) ya escribio antes en el
   mismo orden de puesto.
2. **Puesto 1946** (`control_exportaciones_bis -> export_administration_regulations`):
   la misma arista que el puesto **1945** de la misma bolsa (`control_exportaciones_bis ->
   regulaciones_exportacion_ear`, resolviendo por alias) ya escribio antes.

**Idempotencia probada** (`docs/loop/SALIDA_V91_TAREA4_IDEMPOTENCIA.txt`, EXIT
0): correr `vuelta91_tarea4_escribir_ope07.py` una segunda vez sobre el arbol ya
escrito da **0 ESCRITA de 88, 88 YA_ESTABA, 0 ESCALERA_ROTA**, y `git status
--porcelain -- dataset/` no gana ningun fichero nuevo por esa segunda corrida.

**139 ficheros de `dataset/nodos/` tocados** en toda la vuelta (`git diff
--name-only 675b9969..HEAD -- dataset/nodos/ | wc -l` da 139; las dos
correcciones aditivas de la TAREA 1 y 2 no tocan `dataset/nodos/`, asi que los
139 son integros de la TAREA 4), menos que `86 * 2 = 172` porque varios nodos
son extremo de mas de un par (por ejemplo `pivotar_o_proceder`, cuya alias vive
resuelto en varias filas). `OPERACIONES.jsonl` actualizada: `OP-E-07` gana un
ADDENDUM DE EJECUCION en `nota` con la cifra completa; `estado` se queda en
`LISTA`, mismo criterio que `OP-E-01`, `OP-E-04` y `OP-E-06`. Commits `efb427bc`
(TAREA 4) y `1626d81b` (addendum de `OPERACIONES.jsonl`).

## DISCUTIBLES MARCADOS, PARA LA RELECTURA CIEGA DEL AUDITOR

1. **Las OCHO direcciones de OP-E-07 leidas a mano** (puestos 1163, 1191, 1388,
   1500, 1778, 1847, 1886, 1992), porque el criterio automatico no las resolvio
   y dependen de mi lectura de la razon completa, citada en `DIRECCION_MANUAL`
   de `vuelta91_tarea4_direccion_ope07.py`. Las 80 restantes salen de una regla
   mecanica (segmento de cada id, marca de hijo) y no dependen de mi lectura.
2. **La relectura dirigida del banco 9.22 (TAREA 1): el veredicto NO SOSTIENE,
   y las tres direcciones de la escalera que le siguen.** Marcado porque es una
   lectura mia sobre una figura que el propio banco reconoce como rara (dos
   ejemplares en 1.100 pares); si el auditor lee las tres razones y encuentra
   que si sostienen (o que la direccion es la otra), la correccion aditiva de
   `PENDIENTES.md` se mueve.
3. **Los dos `YA_ESTABA` de OP-E-07 (1388 y 1946)**, porque dependen de que
   `res()` resuelva de verdad las cadenas de alias citadas (verificado en vivo,
   ver TAREA 4) y no de una lectura mia: si el auditor corre el mismo `res()` y
   da otro nodo, la cuenta de 86 ESCRITA se mueve.
4. **El frente 4 del dedupe de OP-E-07 (13 quitados)**: depende de la misma
   `existe_arista()` con resolucion por alias que OP-E-06 uso, aplicada ahora
   sobre un grafo que YA tiene las 113 aristas de OP-E-06 dentro; si esa
   deteccion tuviera un caso ciego, alguno de los 88 podria en realidad ya
   tener arista y duplicarse. La via de OP-C-05 (935 antes / 935 despues) es la
   contraprueba independiente de que no paso.

## PENDIENTES DE DOCTRINA

Ninguna. Las cuatro tareas de esta vuelta salen citando regla escrita: el banco
9.22 con su test de las dos lineas (TAREA 1), la propia `verificacion` de
`OP-E-06` contra el descarte silencioso (TAREA 2), `EJECUTOR.md` regla 1 sobre
la escalada del tallador (TAREA 3), y la `verificacion` de `OP-E-07` mas la
semantica canonica de `resolverId` y la via de `OP-C-05` (TAREA 4).

## LA COMPARACION FINAL

`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 91 --comparar
docs/loop/REPORTE.md`, corrida DESPUES de escribir este fichero y ANTES del
commit de cierre: se cita su salida completa a continuacion, sin editar.

```
--- COMPARACION CONTRA docs/loop/REPORTE.md ---

  filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 0
  CABECERA: IDENTICA AL TALLADOR
```

EXIT 0. Salida completa en `docs/loop/SALIDA_V91_COMPARAR_CIERRE.txt`.

## COMMITS DE LA VUELTA

`git log --format='%h %s' 675b9969..HEAD` (medido al escribir esta seccion,
antes del commit de cierre): `56e0f84c` (TAREA 1 y 2), `5783d081` (TAREA 3),
`efb427bc` (TAREA 4), `1626d81b` (addendum de `OPERACIONES.jsonl`). Este
reporte va en el commit de cierre, el siguiente despues de este.

## CON EL FRENO DELANTE

La racha de reporte queda en UNA de tres: ninguna caida nueva de esta especie
en esta vuelta (medido contra el propio encargo, punto por punto, y contra la
cabecera tallada, identica al digito). La racha de clase o cifra publicada
sigue en CERO.
