# REPORTE VUELTA 108 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `bef757e4` (`docs/loop/SALIDA_V108_HEAD_APERTURA.txt`, ANTES de la 1.a operacion), `verificar_apertura_sellada.py --vuelta 108` VERDE EXIT 0 en la apertura y re-corrida al cierre sin cambio, AHORA CON LA COMPROBACION DE CONTENIDO DE LA TAREA 4 (`docs/loop/SALIDA_V108_APERTURA_SELLADA_VERDE_CIERRE.txt`).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 108` (`docs/loop/SALIDA_V108_CABECERA_TALLADA.txt`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `bef757e4` (asunto real leido de git log: 'ACTA DE LA VUELTA 107 DEL AUDITOR, mas el encargo de la 108.'), HEAD real de apertura `bef757e4` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `b77a23a5` (leido de `SALIDA_V108_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

sha256 identico en apertura, cierre y HEAD (`f0e3993967457ed2b7a0`, 8.391.653 bytes). Nueve mediciones iguales en apertura y cierre: cero movimiento en `dataset/`, `web/`, `engine/` esta vuelta.

**TAREAS 2 y 3, LAS DOS BLOQUEANTES: la bolsa de OP-E-03 se cierra de verdad.** El 74/74 publicado en el cierre de la vuelta 107 era **73/74** (`scripts/loop/verificar_cobertura_bolsa_tres_vias.py`, instrumento nuevo de nombre estable, cruza RESUELTA vivas contra las salidas de barrido declaradas): faltaba el 46. Corregido con `correccion_v108` (campo `vara (cita)`, sin tocar `direccion_leida` ni clase; verificado contra el grafo de hoy: el barrido caso el paso 1 de `customer_discovery_get_out_of_building` pero el hijo despliega el paso 2 entero). Precedente real: **puesto 148** de TRAMO3, no el 147 que cita el encargo (DISCREPANCIA DECLARADA). Pregunta de tres vias al 46: OBJETO. Recontado: **74 vivas, 74 con pregunta, 0 sin ella.** `contar_cierre_efectivo.py`: cifra de cierre sin cambio, **74 / 109 (59,6%)**. Correccion declarada en los tres sitios aditivos (OPERACIONES.jsonl, 04_ENLACES.md, PENDIENTES.md).

**TAREA 5, el tramo 2 al doble.** Recuento propio: 28 RESUELTA vivas, calza con el auditor. Pregunta de tres vias, tres campos, a las 28 (incluido el 46, citado): **28 OBJETO, 0 SATELITE, 0 NO_OBJETO.** Nadie se mueve. DISCUTIBLES MARCADOS para la relectura ciega: **64** (`clasificar los defectos por gravedad, causa y responsabilidad`: el hijo solo desarrolla `gravedad`, distinguido de 109 porque el objeto `los defectos` si es lo que el hijo clasifica) y **91** (`establecer gates... con criterios de Go/Kill`: el hijo desarrolla el complemento de criterios, no un objeto rival). Los dos podrian leerse SATELITE con otra vara.

**TAREA 4 (no bloqueante).** `verificar_apertura_sellada.py` ahora compara sha256 normalizado (CRLF/LF) del blob de nacimiento contra el fichero de hoy (el fichero de la vuelta 107 nacio con `EXIT=0` y hoy esta vacio). Caso real, `--vuelta 107`: ROJO, salida completa en `docs/loop/SALIDA_V108_TAREA4_3_CASO_VUELTA107_ROJO.txt`. Control, `--vuelta 106`: sigue dando VERDE, sin fichero tocado.

**TAREA 1.** Registros del acta 107 en `PENDIENTES.md`, 8 subapartados (1.1 a 1.8). Composicion tallada 1 nivel2/8 nivel3, cotejo limpio. Insercion pura: 104 lineas anadidas, 0 borradas.

**Limpieza menor:** docstring de `verificar_cabecera_pegada_o_condensada.py` corregido a "8 de 10" (lo que su propia salida mide).

**GUARDAS DEL CIERRE**, detalle en `docs/loop/SALIDA_V108_GUARDAS_CIERRE_MUTACIONES.txt`: los 13 casos de mutacion en una pasada. A, B, C, E, F, G ROJO EXIT 1; D, H VERDE EXIT 0; griton VERDE EXIT 0; I ROJO (promesa falsa); J ROJO (marcador, fila 7 apertura); K ROJO (numero de filas). **DISCREPANCIA DECLARADA en L:** ROJO EXIT 1 SI calza, pero mide 0 DISTINTA / 3 AUSENTE (linea base por etiquetas condensadas), no "4 celdas DISTINTA" como narra el acta 107: `--comparar` empareja por ETIQUETA de texto, no por POSICION. `tallar_nombre_de_operacion.py OP-E-03` da VERDE en `docs/loop/SALIDA_V108_TALLAR_NOMBRE_OP.txt`. Aparte, `tallar_veredictos_reporte.py` corre sobre este mismo reporte al final, sin autocitarse: su salida (no una palabra de veredicto de este parrafo) vive en `docs/loop/SALIDA_V108_GUARDAS_CIERRE.txt`.

**PENDIENTE DE DOCTRINA, hallada por la propia guarda:** `tallar_veredictos_reporte.py` sobre este reporte senala la fila de identidad de la cabecera (pegada entera del tallador, no editable) como afirmacion no verificable. La palabra de veredicto que el tallador imprime ahi, sola dentro de una fila de tabla sin punto que la corte, queda emparejada con el hash de cierre que la fila cita despues, y ese hash no trae marca de veredicto propia. No se toca la tabla (romperia la igualdad con el tallador); se deja anotado para quien decida si el cerco debe tratar las filas de tabla distinto de la prosa.

`wc -l docs/loop/REPORTE.md` AL CIERRE en `docs/loop/SALIDA_V108_WCL_CIERRE.txt`.
