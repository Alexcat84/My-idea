# REPORTE VUELTA 103 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `715130c2` (`docs/loop/SALIDA_V103_HEAD_APERTURA.txt`, ANTES
de la 1.a operacion, VERDE contra `scripts/loop/verificar_apertura_sellada.py
--vuelta 103`, `docs/loop/SALIDA_V103_APERTURA_SELLADA_VERDE.txt`). Cabecera
tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 103`
(`docs/loop/SALIDA_V103_CABECERA_TALLADA.txt`):

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `715130c2` (ACTA DE LA VUELTA 102 DEL AUDITOR, leido de git log), HEAD real de apertura `715130c2` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `715130c2` (ACTA DE LA VUELTA 102 DEL AUDITOR, leido de git log), HEAD real de apertura `715130c2` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE** |

Cero movimiento en dataset/web/engine en toda la vuelta (sha256 de
`master_graph.json` igual a HEAD en apertura y en cierre).

**TAREA 1 (bloqueante, arreglo de la escalada del cerco del tallador de
veredictos, acta 102).** `docs/loop/SALIDA_V103_TAREA1_2_MUTACION_VEREDICTOS_DOSVARIANTES.txt`
prueba, en una sola cita: `RE_CITA` ahora reconoce el nombre pelado y el
prefijado, la cobertura total de palabras de veredicto se publica, y el
emparejamiento con mas de una cita por parrafo se declara en la salida. Las
dos variantes de la mutacion (misma frase falsa, mismo fichero, nombre
pelado y con prefijo) dan ROJO tras el arreglo.

**TAREA 2.** Relectura conjunta con el auditor de los pares 28 y 40 (acta
102). Leidos los cuatro nodos enteros y 9.6.2/9.6.3 del banco enteros: en
los dos el primer brazo del test de reconocimiento falla y el 9.6.3 muestra
procedimiento propio a cada lado (SANO). `correccion_v103` en
`OP_E_03_LECTURA_TRAMO1_V96.jsonl`, puestos 28 y 40. Cifra de `OP-E-03`
recomputada (`docs/loop/SALIDA_V103_TAREA2_CIERRE_EFECTIVO.txt`): de 90/93
(50,8%) a 88/95 (51,9% NO RESUELTA).

**TAREA 3.** Registros del acta 102 en `PENDIENTES.md`, seccion propia con
5 subapartados (3.1 a 3.5: la caida de guarda y su arreglo, lo que se hizo
bien, las dos discrepancias ya cerradas, el punto ciego del muestreo ya
atendido, las tres falsas alarmas del auditor). Composicion tallada
(`docs/loop/SALIDA_V103_TAREA3_COMPOSICION.txt`): 1 nivel2 / 5 nivel3,
cotejo limpio contra 3.1-3.5.

**TAREA 4.** Relectura al doble del tramo 1 por el CENTRO del
`titulo_ratio` (8 puestos: 13, 19, 10, 31 y 15, 36, 35, 32; excluidos el 5,
los ocho de la TAREA 3 de la vuelta 102, y el 28/40 de la TAREA 2 de esta
vuelta), a ciegas con instrumento propio
(`docs/loop/SALIDA_V103_TAREA4_CIEGA_BLIND.txt`,
`docs/loop/SALIDA_V103_TAREA4_CIEGA_REVEAL.txt`). 7 de 8 coincidieron; el
31 discrepo por exceso de genero y se movio (`correccion_v103`). Cifra
final de `OP-E-03` (`docs/loop/SALIDA_V103_TAREA4_CIERRE_EFECTIVO.txt`):
**87/96 (52,5% NO RESUELTA)**.

**DISCUTIBLES MARCADOS:** ninguno nuevo esta vuelta (la unica discrepancia
de la TAREA 4, el puesto 31, se resolvio dentro de la propia vuelta con
`correccion_v103`, no queda abierta para la relectura ciega del auditor).

**PENDIENTE DE DOCTRINA:** ninguno nuevo.

Las tres guardas de la TAREA 1 corridas al cierre, tras la ultima edicion:
`tallar_veredictos_reporte.py` sobre este mismo reporte, `tallar_nombre_de_
operacion.py` y `verificar_apertura_sellada.py --vuelta 103`, con sus
salidas citadas en `docs/loop/SALIDA_V103_TAREA1_5_GUARDAS_CIERRE.txt`.

`wc -l docs/loop/REPORTE.md` medido AL CIERRE, tras esta misma edicion, y
vuelto a correr una vez mas antes del commit, en
`docs/loop/SALIDA_V103_WCL_CIERRE.txt`.
