# REPORTE VUELTA 128 (MODO AUSTERO)

Identidad (git): rama `pasada-unica`, HEAD sellado de apertura `9ef3705d`
(acta 127), commit de nacimiento de las salidas de apertura `4e412a73`
(hijo directo del acta, 11 `*_APERTURA.txt` en un solo commit, correccion
abajo), HEAD sellado de cierre `e9413240` (`SALIDA_V128_HEAD_CIERRE.txt`).
`verificar_apertura_sellada.py --vuelta 128`: VERDE 11/11
(`SALIDA_V128_APERTURA_SELLADA.txt`).
## Cabecera tallada (`tallar_cabecera_reporte.py --fase04 --vuelta 128`)
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.184 / 669 | **3.853 / 3.184 / 669** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.195 / 9.177 / 18.372 / 9.830 | **9.198 / 9.180 / 18.378 / 9.833** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+3 / +3 / +6 / +3** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 3 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **3 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `9ef3705d` (asunto real leido de git log: 'ACTA DE LA VUELTA 127 DEL AUDITOR: la vuelta 127 NO ENTREGO, y el motor rojo que la detuvo era real, reproducible y culpa de mi propio encargo: el orden de captura que escribi garantizaba ese rojo.'), HEAD real de apertura `9ef3705d` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `e9413240` (leido de `SALIDA_V128_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
**Baterias cmp** (`SALIDA_V128_BATERIAS_CMP.txt`, 50 pares): GATE0/ETIQUETAS/TSC
6/6 IDENTICOS (no dependen de aristas ni `condiciones_activacion`;
investigado, numstat/conteo/huerfanas confirman que la escritura si llego).
DESFASE/MARCADOR 1/1 IDENTICOS. CONTEO 3/3 IDENTICOS tras 3.a (3.b no toca
aristas), 3/3 DISTINTOS vs APERTURA (+3). MOTOR/WEB 0/6: timing, no falla.
SYNC/NUMSTAT identicos solo OPS10 vs CIERRE (sin escritura entre medias).
## CORRECCION DE PROCEDIMIENTO DECLARADA: reescritura de la apertura
La guarda exige las 11 `*_APERTURA.txt` en UN commit hijo del acta; se
repartieron en tres por leer "commitea por tramo" demasiado literal dentro
de 1.a/1.b/1.c. Sin nada pusheado, corregido con `reset --soft` + `rebase
--onto` (no interactivo, cero conflictos, `git diff` vacio en `dataset/`,
`web/` y `engine/` entre HEAD viejo y nuevo, `SALIDA_V128_REBASE_ARBOL_IDENTICO.txt`).
Aviso: ese tramo nace en un solo commit, no se fragmenta.
## TAREA 1.h, guarda `verificar_huerfanas_por_fusion.py` (reemplaza vuelta126)
Contraste del encargo (par-resuelto, WORK antes de 3.a): TOTAL 32/HEREDADAS
29/REPARADAS 1/FABRICADAS 3, EXACTO. Par-crudo en `7150339f`: TOTAL 39,
EXACTO. Dos autopruebas por mutacion VERDES, clasifican FABRICADAS.
## TAREA 3.a, reposicion REGIMEN B (bloqueante)
Tres aristas, dos vistas c/u. Simulacion VERDE. Mutacion negativa: ROJO
esperado (`SALIDA_V128_OPS09REP3_MUTACION_NEGATIVA.txt`). 2.ª pasada: ROJO
con `git status --porcelain` pegado (`SALIDA_V128_OPS09REP3_ROJO_SEGUNDA_PASADA.txt`).
Bateria OPS09REP3 verde. Aristas vivas PERDIDAS 0 NUEVAS 3; huerfanas FABRICADAS 3->0.
## TAREA 3.b, OP-S-10 tramo 2 (16 nodos, REGIMEN B)
28 vivos, 2 contramodelos, 26 candidatos, 10 de la 126, 16 aqui (exacto).
`obtencion_marca_registrada`: vieja "federal" no reescrita, por mandato del
encargo. Tres guardas verdes; cero aristas nuevas.
## TAREA 3.c, verificacion 3 (Item 8/19/23)
7 nodos nombran algun item, 1 deprecado, 6 vivos CUBIERTOS tras 3.b. VERDE.
Correccion aditiva en `05_SANEO.md` (REGIMEN A, 0 borrados).
## TAREA 3.d, estado de OP-S-10 (DISCUTIBLE, no se cierra)
V3/V4/V5 VERDES. V1: 28/28 vivos VERDE, literal FALSO para los 31 (3
deprecados fuera de alcance). V2: antepone pais, vieja "federal" sin
reescribir por mandato del encargo. OP-S-11/OP-S-12 con `nodos` vacio
(`SALIDA_V128_TAREA3D_S11_S12_NOMINA.txt`).
## TAREA 2, REGIMEN A (0 borrados)
2.a: 32 vs 39 CERRADO (dos unidades), resta 33->32 y 39->38 misma arista;
retractada "todas anteriores". 2.b: R.9 (126). 2.c: R.10 (127, no cuenta en
racha). 2.d: ficha `ventana-truncada-de-condiciones-activacion`, tres sitios
(uno mas que el encargo: `prototipo_motor.py:2611`), 13 en `[:2]` y 6 en
`[:3]` tras 3.b (`SALIDA_V128_2D_VENTANA_TRUNCADA.txt`); ningun nodo tocado.
## Guardas 1.e/1.f/1.g/1.h finales
Citas (`SALIDA_V128_1E_VERIFICAR_CITAS.txt`), titulos+autoprueba+2
mutaciones, cifras del plan (0 pares)+2 casos positivos
(`SALIDA_V128_1F_VERIFICAR_CIFRAS.txt`), fusion OPS09 (4 REPITE+2
autopruebas, `SALIDA_V128_1G_FUSION_OPS09.txt`), aristas vivas+huerfanas
con sus autopruebas: todas VERDE (`EXITCODE: 0` en cada salida citada).
## DISCUTIBLES MARCADOS
1. V1/V2 de OP-S-10: letra vs alcance real.
2. Fase 05: quedan OP-S-11/OP-S-12 con `nodos` vacio
   (`SALIDA_V128_TAREA3D_S11_S12_NOMINA.txt`); adjudica el auditor.
3. Reescritura de historia de apertura: correcta por guarda y arbol
   identico verificado; primera vez en la campana, se trae marcada.
Racha de caidas de reporte: 0. Tope 80: `wc -l` da 74 (`SALIDA_V128_1J_WC_REPORTE.txt`).
