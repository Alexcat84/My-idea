# REPORTE VUELTA 122 (MODO AUSTERO, tope 80 lineas)

Apertura sellada en vivo: `SALIDA_V122_HEAD_APERTURA.txt` = `ed916471`, primer
commit de la vuelta `2dc557c3` (hijo directo), `verificar_apertura_sellada.py
--vuelta 122` VERDE (8 ficheros, todos nacidos en `2dc557c3`,
`SALIDA_V122_VERIFICAR_APERTURA_SELLADA.txt`).

**CABECERA, TALLADA** (`tallar_cabecera_reporte.py --fase04 --vuelta 122`,
`SALIDA_V122_CABECERA_TALLADA.txt`):

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | 1 linea(s) de salida (revisar): EXITCODE: 0 | **1 linea(s) de salida (revisar): EXITCODE: 0** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `ed916471` (asunto real leido de git log: 'ACTA DE LA VUELTA 121 DEL AUDITOR: dato cierto al digito, tres operaciones cerradas, y tres afirmaciones que dicen mas que su registro.'), HEAD real de apertura `ed916471` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `ec881c1a` (leido de `SALIDA_V122_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

Cero cambios entre apertura y cierre en TODA la tabla: ninguna operacion de
esta vuelta toco `dataset/`. Fila `tsc`: ver discutible (a).

**TAREA 1.** Ciclo de tres x3 (apertura, checkpoint `OP-S-08`, cierre),
numstat en CERO las tres (`SALIDA_V122_CICLO_APERTURA_NUMSTAT.txt`,
`SALIDA_V122_CICLO_OPS08_NUMSTAT.txt`,
`SALIDA_V122_CICLO_CIERRE_NUMSTAT.txt`). CAIDA PROPIA CORREGIDA EN
VIVO: al medir `OP-S-08` corri `run_phase1.py --reaplico-curaduria` solo,
sin completar el ciclo. Corregido: ciclo completado y remedido. Bateria
`OP-S-08`: `SALIDA_V122_OPS08_GATE0_POST.txt` da Gate 0 verde.
`SALIDA_V122_OPS08_MOTOR_POST.txt` da 25/25.
`SALIDA_V122_OPS08_WEB_POST.txt` da 80/80 (1.030 tests).
`SALIDA_V122_OPS08_TSC_POST.txt` da EXITCODE: 0.

**TAREA 1.e.** `scripts/loop/verificar_citas_del_reporte.py`, nueva: coteja
cada afirmacion del vocabulario cerrado contra el fichero que cita. Prueba de
mutacion (`scripts/loop/vuelta122_tarea1e_mutacion_citas.py`): sobre una
copia del `REPORTE.md` de la 121 con la linea de git status enlazada sin
abreviar a `SALIDA_V121_OPS03_ROJO_SEGUNDA_PASADA.txt` (que trae tres lineas
de `M`), la guarda cae en rojo nombrando ese par exacto
(`SALIDA_V122_TAREA1E_MUTACION_ROJO.txt`).

**TAREA 2.** Cuatro correcciones aditivas del acta 121 (81 insertadas, 0
borradas en `PENDIENTES.md`+`08_VERIFICACION.md`; `OPERACIONES.jsonl` 1/1 por
linea JSONL unica, texto viejo preservado). (2.a) `OP-S-05`: Quantcast NO fue
generalizado (vive en
`inteligencia_de_anuncios_de_la_competencia.pasos_accionables[1]`), fila
sigue HECHA. (2.b) Entrada 7 de `PENDIENTES.md` ampliada: la misma linea
carga Alexa (`OP-S-04`) y Quantcast (`OP-S-05`). (2.c) Correccion bajo la
tabla de `08_VERIFICACION.md`: fila fase 05 acotada a las nominas de sus
operaciones; `vigencia-del-marco-internacional` 6 entradas,
`vigencia-de-herramientas-nombradas` 7, contadas hoy. (2.d) R.4 nueva: las
dos caidas de reporte de la 121 reverificadas, los dos instrumentos vuelven a
fallar en segunda pasada sin escribir nada
(`SALIDA_V122_TAREA2D_VERIFICO_OPS03_ROJO.txt`,
`SALIDA_V122_TAREA2D_VERIFICO_OPS04_ROJO.txt`).

**TAREA 3.a.** `OP-S-08` **HECHA CON REMISION**. Los veinte externos, uno a
uno, cubiertos por `OP-C-01/02/03` (ya ejecutadas,
`accesosResueltos.test.ts` verde dentro de los 1.030). Discutible: "77
huerfanos/314 a deprecado" citaba los `alias_map_*.json`, que NO son la
fuente del resolutor (esa es `ids_alias` en `master_graph.json`, confirmado
en `graph.ts:109` y `reanclar_por_resolutor.py:51`). Censo de hoy: fuente
canonica 742 entradas, 0 colisiones, 719 a vivo, 23 a deprecado, 0 huerfanas;
los cuatro ficheros dan 230 claves, 15 huerfanos, 37 a deprecado (confirma
con codigo propio la cifra del encargo). No se borra ningun alias.

**TAREA 3.b.** `OP-S-09` remedida, **NO se ejecuta**. Nomina recomputada
(`vuelta77_op_s09_nomina.py`): 29 familias, 69 nodos, IDENTICO a la 77; con
el toque unico de la 78 baja a 67, IGUAL a la fila. El criterio aprobado
(continua o repite, `MESA_RACIMOS.md` DECISION 4) es lectura de CONTENIDO
familia por familia, nunca hecha antes: forzar 29 veredictos sin leer es
adivinar. Sigue LISTA; guarda consumida citada
(`SALIDA_V122_TAREA3B_OPS09_FAMILIAS.txt`).

**DISCUTIBLES MARCADOS.** (a) Fila `tsc` sale "revisar": desajuste entre el
marcador `EXITCODE: N` de esta vuelta y el `EXIT=N` que el tallador reconoce
desde la 113; los dos lados son identicos, no es caida. (b) PENDIENTE DE
DOCTRINA: si la lectura de las 29 familias de `OP-S-09` se abre como frente
propio de lectura dirigida, como `OP-E-01/03/06/07`. (c) PENDIENTE DE
DOCTRINA heredado de `OP-S-08`: si limpiar algo de los tres `alias_map_*.json`
que si alimentan `run_phase1.py` (otra etapa), dado que la fuente canonica
del resolutor da 0 huerfanas.
Commits: `2dc557c3`, `d0179e94`, `d7521e8a`, `0f69effa`, `645d3cb5`,
`ec881c1a`, `bd62d88b`.

`tallar_cabecera_reporte.py --fase04 --vuelta 122 --comparar docs/loop/REPORTE.md`
da CABECERA IDENTICA AL TALLADOR (`SALIDA_V122_TALLADOR_COMPARAR.txt`).
`verificar_citas_del_reporte.py` sobre este mismo fichero da VERDE, 3 pares
cotejados (`SALIDA_V122_TAREA1E_CITAS_VERDE.txt`).
