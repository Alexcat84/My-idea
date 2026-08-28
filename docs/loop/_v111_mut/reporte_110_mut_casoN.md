# REPORTE VUELTA 110 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `55a48875` (`docs/loop/SALIDA_V110_HEAD_APERTURA.txt`, ANTES de la 1.a operacion), `verificar_apertura_sellada.py --vuelta 110` VERDE EXIT 0 en la apertura y re-corrida al cierre sin cambio (`docs/loop/SALIDA_V110_GUARDAS_CIERRE_MUTACIONES.txt`).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 110` (`docs/loop/SALIDA_V110_CABECERA_TALLADA.txt`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `55a48875` (asunto real leido de git log: 'ACTA DE LA VUELTA 109 DEL AUDITOR, mas el encargo de la 110.'), HEAD real de apertura `55a48875` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `70f290d5` (leido de `SALIDA_V110_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

sha256 identico en apertura, cierre y HEAD (`f0e3993967457ed2b7a0`, 8.391.653 bytes). Nueve mediciones iguales en apertura y cierre: cero movimiento en `dataset/`, `web/`, `engine/` esta vuelta.

**TAREA 2, BLOQUEANTE: la guarda ve el volteo EN SU PROPIO SITIO.** `verificar_vuelco_de_veredicto.py` lee ahora la historia en git de cada uno de los seis ficheros y compara HOY contra su commit mas viejo (`_detectar_y_declarar`, nucleo compartido con el cruce). Caso positivo sobre el estado real: 87 aparece EN SITIO (OBJETO en `cd00fef8` -> SATELITE hoy) DECLARADO; 91, 109, 123, 145 siguen de CRUCE, DECLARADOS; VERDE EXIT 0 (`docs/loop/SALIDA_V110_TAREA2_3_CASO_POSITIVO.txt`). Caso N (`tramo2_sin_decl_87.md`, del auditor): ANTES del arreglo, VERDE con 4 vuelcos y el 87 ausente, el boquete; DESPUES, ROJO EXIT 1 nombrando 87 (`SALIDA_V110_TAREA2_4_CASO_N_DESPUES.txt`). Caso O (`tramo2_sin_decl_91.md`): ROJO EXIT 1 nombrando 91, antes y despues, sin apagarse (`SALIDA_V110_TAREA2_5_CASO_O_DESPUES.txt`).

**TAREA 3, BLOQUEANTE: el 154, relectura conjunta, `correccion_v110`.** Leido el par entero contra los dos nodos: "combinar A con B" es construccion de dos argumentos, misma especie que 123 y 145. Contra-caso propio escrito antes de decidir (el hijo podria desarrollar solo el argumento B, agilidad, en 4 de sus 5 pasos): se cae porque titulo, paso 2 y entregable del hijo anclan el argumento A (aprendizaje del cliente) por separado, igual que el contra-caso del auditor. Decidido **OBJETO**, correccion aditiva en `SALIDA_V106_TAREA4_3_TRES_VIAS.txt`, razon vieja no borrada. La lectura entera SOSTIENE (acta 106) contestaba si el par es madre e hijo (9.6.2), pregunta distinta de OBJETO/SATELITE: no sirve de precedente. `contar_cierre_efectivo.py` sigue en **74/109 (59,6%)**, sin cambio (`SALIDA_V110_TAREA3_4_CIERRE_EFECTIVO_154.txt`); cobertura sigue **74/74/0**.

**TAREA 4 (no bloqueante). La rama muda aprende a hablar.** El caso "primero y ultimo coinciden, algo intermedio distinto" ya no hace `continue` en silencio: se reporta como OSCILACION, con la misma exigencia de declaracion. Caso positivo por construccion (puesto fabricado 9001, A/B/A sobre tres copias): la rama se dispara e imprime (`SALIDA_V110_TAREA4_2_CASO_CONSTRUCCION.txt`). Sobre los ficheros reales sigue en 0 oscilaciones.

**TAREA 5, la especie de dos argumentos, al doble.** `vuelta110_tarea5_lote_preposicional.py` resuelve el `paso_casado` de las 74 RESUELTA vivas contra `master_graph.json` (por id, resuelto): 63 con preposicion, 11 sin ella, cifra limpia (`SALIDA_V110_TAREA5_1_LOTE_PREPOSICIONAL.txt`). De los 63, solo 6 son la especie estricta (13, 49, 97, 123, 145, 154: alinear/diferenciar/reemplazar/vincular/combinar); los 57 restantes admiten cualquier veredicto. Los 6 estrictos ya estaban OBJETO al medir hoy: **cosecha 0**, ninguno se mueve (`SALIDA_V110_TAREA5_2_5_CLASIFICACION.md`).

**TAREA 1.** Registros del acta 109 en `PENDIENTES.md`, 5 subapartados del encargo mas 1.6 de composicion tallada: 2 CAIDA (1.1 AUDITOR, 1.2 EJECUTOR), 3 SIN_CAIDA (1.3, 1.4, 1.5), cotejo limpio (`SALIDA_V110_TAREA1_6_COMPOSICION.txt`). Insercion pura.

**GUARDAS DEL CIERRE**, detalle en `docs/loop/SALIDA_V110_GUARDAS_CIERRE_MUTACIONES.txt`: 17 casos de mutacion (A-M heredadas, TAREA2.4-v109, mas N y O nuevas) y 5 instrumentos adicionales, TODOS calzan. `tallar_nombre_de_operacion.py OP-E-03` VERDE. `verificar_cobertura_bolsa_tres_vias.py` sigue **74/74/0**.

**DISCUTIBLES MARCADOS para la relectura ciega: NINGUNO.** El 154 se resolvio por relectura conjunta (auditor y ejecutor coinciden en OBJETO, con contra-casos independientes que llegan al mismo sitio), no por marcado nuevo.

`tallar_veredictos_reporte.py` sobre este mismo reporte, `docs/loop/SALIDA_V110_GUARDAS_CIERRE.txt`.

`wc -l docs/loop/REPORTE.md` AL CIERRE en `docs/loop/SALIDA_V110_WCL_CIERRE.txt`.
