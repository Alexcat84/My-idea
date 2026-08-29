# REPORTE VUELTA 123 (MODO AUSTERO, tope 80 lineas)

Apertura sellada en vivo: `SALIDA_V123_HEAD_APERTURA.txt` = `128d0e5b`, primer
commit `db8805a2`. `verificar_apertura_sellada.py --vuelta 123` VERDE (8
ficheros nacidos en `db8805a2`).

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `128d0e5b` (asunto real leido de git log: 'ACTA DE LA VUELTA 122 DEL AUDITOR: el trabajo material aguanta al digito, y la guarda contra el dictado se estrecho para pasar sobre su propio reporte.'), HEAD real de apertura `128d0e5b` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `887f69bc` (leido de `SALIDA_V123_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

Tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 123`. Ciclo de tres
completo antes y despues de cada bateria (`SALIDA_V123_CICLO_CIERRE_NUMSTAT.txt`
vacio). **CAIDA PROPIA CORREGIDA EN VIVO, dos veces**: capturar `GATE0_CMD1` con una
corrida extra de `run_phase1.py` tras converger reabre la curaduria; lo
delato `engine/run_all_tests.py` (71 divergentes). Corregido reaplicando
`etiquetas_de_cara.py` + `sync_assets_web.py` las dos veces.

## TAREA 1, guardas

(1.e) `verificar_citas_del_reporte.py`: quitado el `continue` que sacaba toda
fila de tabla del cotejo (acta 122, 4.6); fila con cita propia si coteja.
Caso positivo (`vuelta123_tarea1e_mutacion_fila_tabla.py`) y mutacion vieja
de la 122 siguen cayendo en rojo. (1.f) `verificar_cifras_del_plan.py`
nuevo: coteja (numero, ruta `.test.ts`) del texto anadido de
`OPERACIONES.jsonl` contra vitest. Dos bugs propios corregidos al probarla
(`git show` sin `encoding=utf-8`; `difflib` sin separador entre tramos).
Caso positivo `--base ed916471`: rojo 32 contra 27
(`SALIDA_V123_TAREA1F_CASO_POSITIVO_ROJO.txt`); corregido, limpio
(`..._VERDE.txt`). (1.d) tsc cierra con `EXIT=0`, cabecera limpia.

## TAREA 2, correcciones aditivas

(2.a) `OP-S-08.verificacion[0]`: 27 casos, no 32
(`SALIDA_V123_TAREA2A_VITEST_ACCESOSRESUELTOS.txt`).
(2.b) `OP-S-09.nota`: 28 familias no 29 (excluida `estructura_de_gates`/
`estructura_gates`, va a `OP-M-01-FUSION`), 67 nodos, 39 pares
(`SALIDA_V123_TAREA2B_NOMINA_29.txt`).
(2.c) `PENDIENTES.md` R.5: dos caidas del dictado de la 122 (81 vs 80
insertadas; guarda de citas estrechada solo en el commit).
(2.d) `PENDIENTES.md` SEPTIMA entrada: censo propio de alias confirma al
acta 122, 742/0/719/23/0, tras corregir bug propio de clasificacion
(`SALIDA_V123_TAREA2D_CENSO_ALIAS.txt`); `alias_map_*.json` no se tocan.
(2.e) `PENDIENTES.md`: 4 llamadas vivas a `cargarEntrySeeds`, solo
`follow/route.ts:232` sin grafo; no se toca codigo.
Todas aditivas: `git diff --numstat` sobre `PENDIENTES.md` da 107/0.

## TAREA 3, OP-S-09 lectura dirigida

(3.a) 28 familias, 67 nodos, 39 pares leidos par a par contra
`MESA_RACIMOS.md:214`, en `SALIDA_V123_OPS09_LECTURA.jsonl` (decisiones ahi,
no en prosa, MODO AUSTERO 2): 37 continua, 2 repite
(`eliminacion_causas_error`->`eliminacion_causas_error_4`;
`dia_cero_defectos_3`->`dia_cero_defectos_2`). Ninguna cae en la excepcion
de transdominio/`_2` de propiedad intelectual.
(3.b) NO SE EJECUTA, entrega completa por el texto del encargo: las tres
guardas de escritura no cupieron con TAREA 1 y la lectura completa. Guardas
de escritura consumidas: cero. Pasa entera a la 124. (3.c) no aplica: 3.b no cerro.

## Discutibles marcados (para la relectura ciega)

(A) Los dos veredictos repite de 3.a: discutible de lectura, no de doctrina.
(B) El superviviente elegido en cada repite es criterio del ejecutor;
discutible si el auditor prefiere el otro miembro.

## Comprobaciones finales

`tallar_cabecera_reporte.py --comparar docs/loop/REPORTE.md`:
`SALIDA_V123_TALLADOR_COMPARAR.txt`.
`verificar_citas_del_reporte.py`: `SALIDA_V123_CITAS_FINAL.txt`.
`verificar_cifras_del_plan.py`: `SALIDA_V123_CIFRAS_FINAL.txt`, 0 pares.
`wc -l docs/loop/REPORTE.md`: `SALIDA_V123_WCL_REPORTE.txt`.
