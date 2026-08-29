# REPORTE VUELTA 125 (MODO AUSTERO)

Identidad (git): rama `pasada-unica`, HEAD apertura `486ac73a` (hijo del acta
`c9ac2fb8`), HEAD cierre `65910ae3` (`SALIDA_V125_HEAD_CIERRE.txt`).
`verificar_apertura_sellada.py --vuelta 125`: VERDE, 8/8 nacidos en el primer commit.
## Cabecera tallada (`tallar_cabecera_reporte.py --fase04 --vuelta 125`)

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.184 / 669** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.194 / 9.176 / 18.370 / 9.829** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+4 / +7 / +11 / +16** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **2 fila(s): `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `c9ac2fb8` (asunto real leido de git log: 'ACTA DE LA VUELTA 124 DEL AUDITOR: el suelo esta cumplido al digito, mi ciega abre dos discrepancias que van a relectura conjunta, y el discutible mayor queda adjudicado sin doctrina nueva.'), HEAD real de apertura `c9ac2fb8` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `65910ae3` (leido de `SALIDA_V125_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

**Baterias cmp** (`SALIDA_V125_BATERIAS_CMP.txt`): TSC/MARCADOR IDENTICOS
apertura/OPS09/cierre (no dependen de `dataset/nodos`). GATE0_CMD1/CONTEO/
DESFASE_CALIBRADO DISTINTOS apertura-cierre: escritura real de OP-S-09
llegando (avisado en 1.d, no es falla). MOTOR/WEB DISTINTOS por timings,
mismos resultados.
## TAREA 3.a, relectura conjunta (`docs/loop/SALIDA_V125_OPS09_RELECTURA_CONJUNTA.jsonl`)

1. `auditoria_de_producto`/`auditoria_producto`: CONTINUA->**REPITE** (cableado
   7 vs 1, vara `docs/BANCO_DE_TEXTOS.md` linea 1658).
2. `estrategia_innovacion_producto`/`estrategia_de_innovacion_de_producto`:
   REPITE, superviviente corregido a `estrategia_innovacion_producto`
   (cableado 14 vs 7, vara `docs/BANCO_DE_TEXTOS.md` linea 1834).
## TAREA 1.g + 3.b, ejecucion OP-S-09 (REGIMEN B, 4 pares REPITE)

Guarda `scripts/loop/verificar_fusion_ops09.py`: autoprueba y corrida real
VERDE EXIT 0 (`docs/loop/SALIDA_V125_FUSION_OPS09_AUTOPRUEBA.txt`), 4 pares.
Plan `docs/loop/PLAN_V125_OPS09.json` ejecutado con
`scripts/loop/fundir_por_plan.py`. Simulacion previa VERDE
(`docs/loop/SALIDA_V125_OPS09_SIMULACION.txt`). Mutacion negativa ROJO
esperado (`docs/loop/SALIDA_V125_OPS09_MUTACION_NEGATIVA.txt`). Ejecucion
real, ROJO en 2.ª pasada con `git status --porcelain` pegado
(`docs/loop/SALIDA_V125_OPS09_ROJO_SEGUNDA_PASADA.txt`). 27 ficheros, +4
deprecados. Ciclo de tres corrido, Gate 0 y 3 suites verdes (1.d).
## TAREA 2, REGIMEN A

2.a (`OPERACIONES.jsonl`): 2 correcciones aditivas en la fila OP-S-09
(prefijo-exacto verificado). Medido hoy: 26 ids vivos de la nomina con sufijo
numerico (48 en el grafo entero), 25 resueltos por CONTINUA, residuo
`eliminacion_causas_error_4`. 2.b: R.7 en PENDIENTES.md (61 explicado, caida
de las 2 varas es del auditor). 2.c: OCTAVA entrada de `campos-sucios-dataset`
(22 ids fuera de nomina, post campana).
## TAREA 3.c, remedicion OP-S-10 (NO EJECUTADA)

`SALIDA_V125_OPS10_REMEDIDA.txt`: nomina 31 (coincide con el campo `nodos`,
ramal v OK). 28 vivos, 3 deprecados: `cinco_categorias_costos_franquicia`->
`estimacion_inversion_inicial_franquiciador`, `elaboracion_fdd`->
`preparar_fdd`, `estructuras_combinadas_franquicia`->
`prevenir_franquicias_inadvertidas`.
## Guardas 1.e/1.f/1.h

Todas VERDE EXIT 0 (`docs/loop/SALIDA_V125_1E_CITAS.txt`,
`docs/loop/SALIDA_V125_1E_TITULOS.txt`, `docs/loop/SALIDA_V125_1E_MUTACION_CITAS.txt`,
`docs/loop/SALIDA_V125_1E_MUTACION_FILA_TABLA.txt`, `docs/loop/SALIDA_V125_1F_CIFRAS_PLAN.txt`,
`docs/loop/SALIDA_V125_1F_CASO_POSITIVO_123.txt`, `docs/loop/SALIDA_V125_1F_CASO_POSITIVO_VENTANA.txt`,
`docs/loop/SALIDA_V125_FUSION_OPS09_AUTOPRUEBA.txt`): citas, titulos
(+autoprueba), sus 2 mutaciones, cifras del plan (0 pares, base `c9ac2fb8`),
sus 2 casos positivos, `verificar_fusion_ops09.py --autoprueba`. Cabecera
IDENTICA AL TALLADOR (`docs/loop/SALIDA_V125_TALLADOR_COMPARAR.txt`).
## PENDIENTE DE DOCTRINA
Id nuevo para `eliminacion_causas_error_4` (sufijo ya no distingue gemelos):
sin regla escrita, anotado en `campos-sucios-dataset`.
## DISCUTIBLES MARCADOS PARA RELECTURA CIEGA
1. Las 4 fusiones REPITE usan mapeo CUBIERTO editorial (paso a paso,
   `docs/loop/PLAN_V125_OPS09.json`) sin precedente identico en la casa para
   racimos multi-par: 2 pasos APPEND genuinos (`dia_cero_defectos_3` paso 5,
   `estrategia_de_innovacion_de_producto` paso 6) por juicio propio.
2. `OP-S-09` no se declara `HECHA` (campo `estado` intacto): las 51 pares
   quedan resueltos (47 CONTINUA + 4 REPITE) pero el cierre de la operacion
   lo adjudica el auditor, no el ejecutor (regla 5/11).
Tope de 80 lineas: `wc -l docs/loop/REPORTE.md` da 80. CUMPLIDO AL DIGITO.
