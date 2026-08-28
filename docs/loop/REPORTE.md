# REPORTE VUELTA 113 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `e9ce3c86` (`docs/loop/SALIDA_V113_HEAD_APERTURA.txt`, ANTES de la 1.a operacion), `verificar_apertura_sellada.py --vuelta 113` VERDE EXIT 0 (`docs/loop/SALIDA_V113_APERTURA_SELLADA.txt`) y re-corrida al cierre sin cambio (`docs/loop/SALIDA_V113_GUARDAS_CIERRE_MUTACIONES.txt`).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 113` (`docs/loop/SALIDA_V113_CABECERA_TALLADA.txt`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `e9ce3c86` (asunto real leido de git log: 'ACTA DE LA VUELTA 112 DEL AUDITOR, mas el encargo de la 113.'), HEAD real de apertura `e9ce3c86` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `db5375ce` (leido de `SALIDA_V113_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

sha256 identico en apertura, cierre y HEAD (`f0e399396745...`, 8.391.653 bytes, `docs/loop/SALIDA_V113_SYNC_CIERRE.txt`). Nueve mediciones iguales en apertura y cierre: cero movimiento en `dataset/`, `web/`, `engine/` esta vuelta.

**TAREA 2, BLOQUEANTE, LOS TRES REMEDIOS.** (2.1-2.3) `interpretar_tsc()` (extraida de `tallar_cabecera_reporte.py`) descuenta, sin contarla, la linea final `EXIT=<n>`: la celda vuelve a distinguir tsc LIMPIO de SUCIO. Mutacion V (solo `EXIT=0`) da "EXITCODE 0, cero lineas"; mutacion W (una linea de error real mas `EXIT=1`) da celda DISTINTA nombrando la linea (`docs/loop/SALIDA_V113_TAREA2_2_3_MUTACION_V_W.txt`). Repetido sobre la vuelta 112 real: su tsc ya talla LIMPIO en las dos columnas, arriba. (2.4-2.5) `tallar_cifras_de_antes.py`: MARCAS deja de ser enumeracion y se documenta como REGLA (toda construccion que afirme un estado anterior o su permanencia), con la obligacion escrita de que el ejecutor sume el verbo que su propio reporte use. Se amplia con siete locuciones nuevas de permanencia (detalle en el docstring del tallador). Mutacion X sobre el reporte 112 real (`git show 87397be1`): antes no marca ninguna de las dos oraciones de esa especie, despues marca las dos, una con vara (2/1 citas) y otra ROJO por falta de cita, declarado tal cual sale (`docs/loop/SALIDA_V113_TAREA2_5_MUTACION_X_ANTES.txt` y `docs/loop/SALIDA_V113_TAREA2_5_MUTACION_X_DESPUES.txt`). HALLAZGO COLATERAL DECLARADO: la misma extension encuentra un TERCER caso, mas viejo, nunca visto: el reporte 111 (`git show 9aea9f43`) trae en su linea 30 una afirmacion de permanencia sin ninguna cita; el caso heredado T de las guardas del cierre pasa de EXIT 0 a EXIT 1 por este motivo, declarado con el detalle completo en `docs/loop/SALIDA_V113_GUARDAS_CIERRE_MUTACIONES.txt`. (2.6) Barrido 2.7 rehecho entero, las tres busquedas corridas de verdad (RE_CITA 14, patron txt|md 3, LOOP=os.path.join( 57), union 71), TODOS clasificados sin excepcion en 4 grupos; los tres previamente omitidos ya nombrados en GRUPO B (`docs/loop/SALIDA_V113_TAREA2_6_BARRIDO_TALLADORES.txt`).

**TAREA 1.** Registros del acta 112 en `PENDIENTES.md`, 4 subapartados (3 CAIDA: 1.1-1.2 del ejecutor, 1.3 del auditor; 1 SIN_CAIDA), composicion tallada sobre el bloque extraido DESPUES de la ultima edicion (`docs/loop/SALIDA_V113_TAREA1_COMPOSICION.txt`), fidelidad verificada con diff CERO diferencias (`docs/loop/SALIDA_V113_TAREA1_DIFF_FIDELIDAD.txt`).

**TAREA 3, TECHO 29 DECLARADO ANTES DE LEER (`docs/loop/SALIDA_V113_TAREA3_1_CENSO_29.txt`, sellado en su propio commit): mi recuento calza al digito con el del encargo** (8 territorio viejo: 168,170,171,173,176,178,181,183; 21 territorio nuevo con `correccion_vNN` que anula a None: 6,8,20,21,24,25,28,29,31,38,40,52,62,66,80,93,147,161,172,174,175; 3 fuera de este territorio: 46,145,148). Los 29 leidos contra `dataset/nodos/` (spot-check directo en 168, 183, 31, 147, 6 mas revision del resto) con banco 9.6.1/9.6.2/9.6.3: **cosecha CERO**, ninguno se mueve. Las 21 correcciones previas se confirman bien fundadas (test de reconocimiento, exceso de genero, senal de entregables, 9.6.3 SANO); los 8 del territorio viejo son falsos amigos por token compartido, confirmados leyendo el nodo. Registro completo en `docs/plan/OP_E_03_LECTURA_V113_REGISTRO.jsonl` (29 filas, `NO_SE_MUEVE` cada una con su nota). `contar_cierre_efectivo.py` sigue **74/109 (59,6%)** (vieja `docs/loop/SALIDA_V112_TAREA3_5_CIERRE_EFECTIVO_VIEJA.txt`, nueva `docs/loop/SALIDA_V113_TAREA3_7_CIERRE_EFECTIVO_NUEVA.txt`); cobertura sigue **74/74/0** (vieja `docs/loop/SALIDA_V112_TAREA3_5_COBERTURA_VIEJA.txt`, nueva `docs/loop/SALIDA_V113_TAREA3_7_COBERTURA_NUEVA.txt`).

**GUARDAS DEL CIERRE**, detalle en `docs/loop/SALIDA_V113_GUARDAS_CIERRE_MUTACIONES.txt`: NUEVE instrumentos y VEINTISEIS casos de mutacion (los veintitres heredados A-U mas V, W y X nuevos), TODOS calzan.

**DISCUTIBLES MARCADOS para la relectura ciega: UNO.** Puesto 66 (`cultura_justa_3` -> `cultura_de_aprendizaje`, regla 3.6: la razon vieja trae la palabra literalmente, "ES UNA LECTURA DE FRONTERA y va marcada como discutible"). Confirmado NO RESUELTA igual, con la misma cita del banco 9.6.2 y 9.6.3 que ya traia la correccion previa.

`tallar_veredictos_reporte.py` sobre este mismo reporte, `docs/loop/SALIDA_V113_GUARDAS_CIERRE.txt`.

`wc -l docs/loop/REPORTE.md` AL CIERRE en `docs/loop/SALIDA_V113_WCL_CIERRE.txt`.
