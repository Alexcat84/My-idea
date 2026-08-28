# REPORTE VUELTA 109 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `d696fde8` (`docs/loop/SALIDA_V109_HEAD_APERTURA.txt`, ANTES de la 1.a operacion), `verificar_apertura_sellada.py --vuelta 109` VERDE EXIT 0 en la apertura y re-corrida al cierre sin cambio (`docs/loop/SALIDA_V109_GUARDAS_CIERRE_MUTACIONES.txt`).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 109` (`docs/loop/SALIDA_V109_CABECERA_TALLADA.txt`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `d696fde8` (asunto real leido de git log: 'ACTA DE LA VUELTA 108 DEL AUDITOR, mas el encargo de la 109.'), HEAD real de apertura `d696fde8` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `21e1bc20` (leido de `SALIDA_V109_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

sha256 identico en apertura, cierre y HEAD (`f0e3993967457ed2b7a0`, 8.391.653 bytes). Nueve mediciones iguales en apertura y cierre: cero movimiento en `dataset/`, `web/`, `engine/` esta vuelta.

**TAREAS 2 y 3, LAS DOS BLOQUEANTES: el vuelco de veredicto se caza con un instrumento, y el 87 se resuelve.** Nace `scripts/loop/verificar_vuelco_de_veredicto.py` (nombre estable, reusa `FICHEROS_VEREDICTO`). Caso positivo: 5 vuelcos (87, 91, 109, 123, 145), 109/123/145 DECLARADOS, ROJO nombrando 87 y 91 (`docs/loop/SALIDA_V109_TAREA2_3_CASO_POSITIVO.txt`). Caso rojo por mutacion: el 123 cae de DECLARADO a MUDO al borrarle su declaracion (`docs/loop/SALIDA_V109_TAREA2_4_CASO_ROJO_MUTACION.txt`). El 87 leido entero contra el grafo (TAREA 3): el precedente citado en su fila vieja (116) resulto ser la forma CONTRARIA (alli el verbo es intransitivo, aqui `Evalua` tiene objeto propio distinto del complemento); decidido SATELITE, forma identica a 123 y 154. Correccion aditiva en `docs/loop/SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md`, razon vieja NO borrada. El 91 queda OBJETO, cerrado por el auditor. Instrumento tras la correccion: VERDE, 4 vuelcos, los 4 DECLARADOS (`docs/loop/SALIDA_V109_TAREA2_5_VERDE_TRAS_CORRECCION.txt`). `contar_cierre_efectivo.py` sigue en **74/109 (59,6%)**, sin cambio.

**TAREA 4 (no bloqueante).** `tallar_veredictos_reporte.py` corre `tallar_cabecera_reporte.py` de verdad y excluye del cerco toda linea IDENTICA a la que ese comando imprime (nunca por forma). Bug propio hallado y corregido en el desarrollo: la funcion se comia la tabla por la linea en blanco que el tallador imprime tras el marcador. Caso positivo: el REPORTE.md de la vuelta 108 (`7f697c00`), que fallaba por la fila 18, pasa a VERDE excluyendo esa 1 linea (`docs/loop/SALIDA_V109_TAREA4_3_CASO_VUELTA108_VERDE.txt`). Caso rojo por mutacion: una afirmacion VERDE falsa anadida EN PROSA, fuera de la cabecera, sigue ROJO EXIT 1 (`docs/loop/SALIDA_V109_TAREA4_4_CASO_ROJO_MUTACION.txt`).

**TAREA 5, el lote de los seis SATELITE historicos.** Recuento propio: 87, 91, 109, 123, 145, 154, calza con el auditor (`docs/loop/SALIDA_V109_TAREA5_1_RECUENTO_LOTE.txt`). Tres campos + historia completa de cada uno en `docs/loop/SALIDA_V109_TAREA5_LOTE_SATELITE_HISTORICO.md`. Ninguno se mueve: los seis ya pasaron por su propia lectura entera o relectura conjunta.

**TAREA 1.** Registros del acta 108 en `PENDIENTES.md`, 6 subapartados (1.1 a 1.6). Composicion tallada 1 nivel2/6 nivel3, cotejo limpio. Insercion pura: 117 lineas anadidas, 0 borradas. El 64 y el 91 dejan de estar marcados DISCUTIBLE.

**GUARDAS DEL CIERRE**, detalle en `docs/loop/SALIDA_V109_GUARDAS_CIERRE_MUTACIONES.txt`: los 15 casos de mutacion en una pasada. A, B, C, E, F, G ROJO EXIT 1; D, H VERDE EXIT 0; griton VERDE EXIT 0; I ROJO (promesa falsa); J ROJO (marcador, fila apertura); K ROJO (numero de filas); L ROJO EXIT 1 con 0 DISTINTA / 3 AUSENTE (calza con el entendimiento corregido de la vuelta 108); M ROJO EXIT 1 con CUATRO celdas exactas. La mutacion de la TAREA 2.4 muerde. `tallar_nombre_de_operacion.py OP-E-03` VERDE. `verificar_cobertura_bolsa_tres_vias.py` ahora **74/74/0**, cerrada.

**DISCUTIBLES MARCADOS para la relectura ciega: NINGUNO.** Los dos heredados (64 y 91) quedaron cerrados en la TAREA 1; el 87 se resolvio por juicio, no por marcado.

`tallar_veredictos_reporte.py` sobre este mismo reporte, `docs/loop/SALIDA_V109_GUARDAS_CIERRE.txt`.

`wc -l docs/loop/REPORTE.md` AL CIERRE en `docs/loop/SALIDA_V109_WCL_CIERRE.txt`.
