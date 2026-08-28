# REPORTE VUELTA 111 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `29aeb819` (`docs/loop/SALIDA_V111_HEAD_APERTURA.txt`, ANTES de la 1.a operacion), `verificar_apertura_sellada.py --vuelta 111` VERDE EXIT 0 en la apertura y re-corrida al cierre sin cambio (`docs/loop/SALIDA_V111_GUARDAS_CIERRE_MUTACIONES.txt`).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 111` (`docs/loop/SALIDA_V111_CABECERA_TALLADA.txt`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `29aeb819` (asunto real leido de git log: 'ACTA DE LA VUELTA 110 DEL AUDITOR, mas el encargo de la 111.'), HEAD real de apertura `29aeb819` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `4b199d6c` (leido de `SALIDA_V111_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

sha256 identico en apertura, cierre y HEAD (`f0e3993967457ed2b7a0`, 8.391.653 bytes). Nueve mediciones iguales en apertura y cierre: cero movimiento en `dataset/`, `web/`, `engine/` esta vuelta.

**TAREA 2, BLOQUEANTE: el instrumento que exige medir cifras de estado previo.** `scripts/loop/tallar_cifras_de_antes.py` (nombre estable): oracion a oracion, backticks protegidos, exige cita de fichero `SALIDA_*.txt`/`.md` que EXISTA (dos distintas si la oracion mezcla un estado previo con el de hoy). Caso positivo sobre el reporte 110 real (`git show 27ecfe43`): ROJO EXIT 1 nombrando la oracion del caso O (los dos estados en una sola cita), NO nombra la del caso N (dos citas distintas) (`docs/loop/SALIDA_V111_TAREA2_4_CASO_POSITIVO.txt`). Mutacion: quitar una cita a la oracion del caso N pasaba de OK a hallazgo, ROJO EXIT 1 (`docs/loop/SALIDA_V111_TAREA2_5_MUTACION_DESPUES.txt`). Paga la deuda 1.2 del acta 110: `verificar_vuelco_de_veredicto.py` version `55a48875` contra `tramo2_sin_decl_91.md` da CUATRO vuelcos, el 91 MUDO, ROJO EXIT 1, igual que declaro el auditor (`docs/loop/SALIDA_V111_CASO_O_ANTES.txt`).

**TAREA 3, BLOQUEANTE: los cinco SATELITE releidos.** Recuento propio antes de leer: 109 NO RESUELTA, 5 con pregunta de tres vias (20, 21, 38, 66, 93), los cinco SATELITE, VERDE contra la nomina del encargo (`docs/loop/SALIDA_V111_TAREA3_1_CENSO.txt`). Los cinco leidos enteros HOY contra el grafo, con contra-caso escrito antes de decidir por cada uno (`docs/loop/SALIDA_V111_TAREA3_2_4_RELECTURA.md`): en los cinco, la DIRECCION (NO RESUELTA) ya estaba decidida por `correccion_v105` sobre una razon de 9.6.2 independiente del veredicto SATELITE (3.3 del encargo); los cinco SIGUEN SATELITE. Ninguno se mueve: `contar_cierre_efectivo.py` sigue en **74/109 (59,6%)**, sin cambio (`docs/loop/SALIDA_V111_TAREA3_5_CIERRE_EFECTIVO.txt`); cobertura sigue **74/74/0** (`docs/loop/SALIDA_V111_TAREA3_5_COBERTURA.txt`).

**TAREA 4, no bloqueante: el techo de cada vara.** `scripts/loop/censar_alcance_de_la_vara.py` (nombre estable) cruza `contar_cierre_efectivo.py` con los seis `FICHEROS_VEREDICTO`, leyendo el veredicto de HOY (ultima aparicion cronologica, no la primera): 183 total; 74 RESUELTA con 72 OBJETO y 2 SATELITE (87, 109); 109 NO RESUELTA con 104 SIN VEREDICTO y 5 SATELITE (20, 21, 38, 66, 93). Calza al digito con la cifra de control del encargo (`docs/loop/SALIDA_V111_TAREA4_1_CENSO_ALCANCE.txt`). Desde esta vuelta, toda vara sobre este expediente declara su techo antes de correrse.

**TAREA 1.** Registros del acta 110 en `PENDIENTES.md`, 5 subapartados: 3 CAIDA (1.1 AUDITOR de encargo, 1.2 EJECUTOR de expediente sin acumular, 1.4 AUDITOR autodeclarada), 2 SIN_CAIDA (1.3, 1.5), composicion tallada sobre el anadido aislado (discutible de metodo por colision de patron con la tabla de la vuelta 110, resuelto extrayendo el bloque) (`docs/loop/SALIDA_V111_TAREA1_6_COMPOSICION.txt`). Insercion pura.

**GUARDAS DEL CIERRE**, detalle en `docs/loop/SALIDA_V111_GUARDAS_CIERRE_MUTACIONES.txt`: NUEVE instrumentos y VEINTE casos de mutacion (A-O heredados mas P, Q y R nuevos), TODOS calzan. `tallar_nombre_de_operacion.py OP-E-03` VERDE. `verificar_cobertura_bolsa_tres_vias.py` sigue **74/74/0**.

**DISCUTIBLES MARCADOS para la relectura ciega: UNO.** El metodo de la TAREA 1.6 (patron de la tabla de composicion colisiona entre vueltas, resuelto extrayendo el bloque de esta vuelta previo al tallado): ver TAREA 1 arriba.

`tallar_veredictos_reporte.py` sobre este mismo reporte, `docs/loop/SALIDA_V111_GUARDAS_CIERRE.txt`.

`wc -l docs/loop/REPORTE.md` AL CIERRE en `docs/loop/SALIDA_V111_WCL_CIERRE.txt`.
