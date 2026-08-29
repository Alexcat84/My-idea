# REPORTE VUELTA 136 (MODO AUSTERO)

HEAD sellado de apertura: `96153acc`
commit de nacimiento de las salidas de apertura: `adcf0fd2`
HEAD sellado de cierre: `9f9e6892`
Los tres rotulos salen con hash distinto entre si (`tallar_identidad_reporte.py --vuelta 136`).

Cabecera (`tallar_cabecera_reporte.py --fase04 --vuelta 136`), pegada entera:

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.184 / 669 | **3.853 / 3.184 / 669** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.198 / 9.180 / 18.378 / 9.833 | **9.198 / 9.180 / 18.378 / 9.833** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 3 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **3 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `96153acc` (asunto real leido de git log: 'ACTA DE LA VUELTA 135 DEL AUDITOR: la tapia aguanta nueve mutaciones mias y el trabajo entrego entero, pero el reporte atribuye a SALIDA_V135_2A_DIAGNOSTICO.txt un resultado que ese fichero no dice. Tener razon no arregla la cita.'), HEAD real de apertura `96153acc` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `9f9e6892` (leido de `SALIDA_V136_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

REGIMEN B esta vuelta: `OP-S-11` escribe el campo `fuente` en 726 registros (`SALIDA_V136_3C_ESCRITURA.txt`).
Bateria 1.d (`SALIDA_V136_BATERIAS_CMP.txt`): 7 identicos; motor/web distintos solo por duracion (`SALIDA_V136_1D_DIFF_MOTOR.txt`, `SALIDA_V136_1D_DIFF_WEB.txt`); sync distinto por el sha256 movido (discutible 1).
1.g: vivas 7296 contra 7296, perdidas cero, nuevas cero (`SALIDA_V136_1G_ARISTAS_VIVAS.txt`, autoprueba en `SALIDA_V136_1G_ARISTAS_VIVAS_AUTOPRUEBA.txt`); huerfanas TOTAL 29 HEREDADAS 29 REPARADAS 1 FABRICADAS 0 (`SALIDA_V136_1G_HUERFANAS_LIVE.txt`, `SALIDA_V136_1G_FUSION_OPS09.txt`, autoprueba en `SALIDA_V136_1G_HUERFANAS_AUTOPRUEBA.txt`).
1.h/1.i/1.e/1.f verde (`SALIDA_V136_1H_CIERRE_SELLADO.txt`, `SALIDA_V136_1E_TITULOS.txt`, `SALIDA_V136_1F_CIFRAS_PLAN.txt`): cierre valido, titulos cotejan (1 dup. cubierto), plan en cero pares.

TAREA 2, R.17 en `docs/PENDIENTES.md`. 2.a: corrijo mi cita del ramal xx
(mi 2.a era forward-only; las tres exentas eran una si dos no, medido en
`SALIDA_V135_1J_CIFRAS_REPORTE.txt`). 2.b: pego la cobertura real de la
135 que la 2.d ordenaba y no pegue. 2.c: asimetria de ventanas en el
docstring de `verificar_cifras_del_reporte.py`, REGIMEN A
(`SALIDA_V136_2C_WORDDIFF.txt`, cero palabra borrada). 2.d: cierre con
remision de la fase 05 registrado, no declarado.

TAREA 3, `OP-S-11` EJECUTADA.
3.b: 3184 registros con `fuente`, de los cuales 726 cambian y el resto no; 129 formas en primera posicion, cero sin cubrir en la tabla, 54 al final; un nodo con perdida de declaracion repetida (`SALIDA_V136_3B_SIMULACION.txt`).
3.c: 726 registros escritos (`SALIDA_V136_3C_ESCRITURA.txt`), solo el campo `fuente`. Gate 0 verde tras escribir (`SALIDA_V136_GATE0_CMD1_CIERRE.txt`).
3.d, criterio de HECHO de la fase 08: contra el estado previo cae en rojo con 727 incumplimientos (`SALIDA_V136_3D_ANTES.txt`); la mutacion en memoria sobre `activity_attributes` tambien cae en rojo nombrandolo (`SALIDA_V136_3D_MUTACION.txt`); tras escribir, verde (`SALIDA_V136_1J_FUENTE_CANONICO.txt`).
3.e: `OP-S-11` LISTA a HECHA; el conteo de estados queda en 61 LISTA y 10 HECHA (`SALIDA_V136_3E_ESTADOS.txt`).
3.f: el catalogo queda con 54 canonicas, la meta de 55 de `05_SANEO.md` rebasada por uno; `05_SANEO.md` y `OP-S-12` sin tocar, fase 05 sin cerrar por mi.

1.j: cabecera y identidad IDENTICA AL TALLADOR
(`SALIDA_V136_1J_TALLADOR_CABECERA.txt`,
`SALIDA_V136_1J_TALLADOR_IDENTIDAD.txt`). Las otras seis dan VERDE EXIT 0
(`SALIDA_V136_1J_CITAS.txt`, `SALIDA_V136_1J_CIFRAS_PLAN.txt`,
`SALIDA_V136_1J_TITULOS.txt`, `SALIDA_V136_1J_CIERRE_SELLADO.txt`,
`SALIDA_V136_1J_CIFRAS_REPORTE.txt`, `SALIDA_V136_1J_FUENTE_CANONICO.txt`).

PARADA (novena comprobacion): verificar_cabecera_mapeo.py da ROJO (`SALIDA_V136_1J_CABECERA_MAPEO.txt`).
Recomputa el censo VIVO, que la propia escritura de `OP-S-11` ya canonizo: cada valor queda suelto, su propio grupo de uno solo; la cabecera describe el censo previo. No toco tabla ni guarda, ninguna esta en la lista de 1.l: la traigo escrita. Efecto lateral hallado y revertido: cada corrida escribe tambien `SALIDA_V135_4B_PELDANOS.txt` (protegido solo la tabla, no ese fichero); lo restaure con `git checkout` antes de commitear, sin tocarlo yo.

DISCUTIBLE (1): sync distinto no esta en la lista exigida identica de
1.c; lo juzgo esperado bajo REGIMEN B, no adjudicado.
DISCUTIBLE (2): "canonicas de la tabla" en `verificar_fuente_canonico.py`
son los 54 valores distintos de la columna; lectura mia, no letra del
encargo.

Correcciones de la 135: R.17 en `docs/PENDIENTES.md`. Credito CERO.
COBERTURA: 0 cotejadas / 0 exentas / 0 cifras (`SALIDA_V136_1J_CIFRAS_REPORTE.txt`).
Tope 1.k: `wc -l docs/loop/REPORTE.md`.
