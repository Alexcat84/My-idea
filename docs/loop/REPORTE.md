# REPORTE VUELTA 130 (MODO AUSTERO)

Identidad (git): rama `pasada-unica`, HEAD sellado de apertura `e2a68845`
(acta 129), commit de nacimiento de las salidas de apertura `3df04270`
(hijo directo del acta, 11 `*_APERTURA.txt` en un solo commit), HEAD
sellado de cierre `c6020899` (`SALIDA_V130_HEAD_CIERRE.txt`).
`verificar_apertura_sellada.py --vuelta 130`: VERDE 11/11
(`SALIDA_V130_APERTURA_SELLADA.txt`). `verificar_cierre_sellado.py --vuelta
130`: VERDE (`SALIDA_V130_1H_CIERRE_SELLADO.txt`, ultimo bloque).
## Cabecera tallada (`tallar_cabecera_reporte.py --fase04 --vuelta 130`)
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `e2a68845` (asunto real leido de git log: 'ACTA DE LA VUELTA 129 DEL AUDITOR: la 129 no entrego y es la cuarta de la campana, pero no fue como la 127: no hubo ni un rojo. Abrio bien y sellada, corrio las nueve guardas de la TAREA 1 verdes, escribio las dos piezas de codigo encargadas, y se apago sin commitear seis minutos y medio de trabajo bueno. Lo verifique pieza por pieza y lo rescate yo en commit propio, porque si lo commiteaba la 130 la guarda de apertura se le ponia roja. Sin doctrina nueva y sin parada.'), HEAD real de apertura `e2a68845` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `c6020899` (leido de `SALIDA_V130_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
**Baterias cmp** (`SALIDA_V130_BATERIAS_CMP.txt`, 3 lados: APERTURA,
OPS10REP1, CIERRE): GATE0/CONTEO/TSC/ETIQUETAS 3/3 IDENTICOS cada familia.
MOTOR/WEB 0/3 (timing, no falla). SYNC 1/3 IDENTICOS, el par exacto es
`OPS10REP1 vs CIERRE` (nada escribio entre medias). NUMSTAT 1/3 IDENTICOS,
el par exacto es `APERTURA vs CIERRE` (los dos sobre arbol ya committeado).
CONTEO confirmado tambien por `verificar_aristas_vivas.py`: PERDIDAS 0
NUEVAS 0. Huerfanas TOTAL 29 FABRICADAS 0, sin cambio (`SALIDA_V130_1G_
FUSION_ARISTAS.txt`, `SALIDA_V130_OPS10REP1_HUERFANAS.txt`).
## TAREA 3.a, OPS10REP1, REGIMEN B (bloqueante)
`prevenir_franquicias_inadvertidas` (superviviente de
`estructuras_combinadas_franquicia`) recibe la condicion de pais como
primera condicion; las cuatro viejas intactas y en orden. Tres guardas:
simulacion VERDE, mutacion negativa ROJO esperado
(`SALIDA_V130_OPS10REP1_MUTACION_NEGATIVA.txt`), rojo real en 2.ª pasada con
`git status --porcelain` pegado (`SALIDA_V130_OPS10REP1_ROJO_SEGUNDA_
PASADA.txt`). Verificacion 1 resuelta por P.1: 31 ids -> 29 vivos (el
resolutor mueve 3), 28/29 cubiertos ANTES, **29/29 DESPUES**
(`SALIDA_V130_3A_VERIFICACION1_ANTES.txt`,
`..._REMEDIDA.txt`). **DISCUTIBLE: no cierro OP-S-10 en OPERACIONES.jsonl.**
## TAREA 2, REGIMEN A (0 borrados, numstat con cero lineas `^-[^-]` en los tres)
R.11 en `PENDIENTES.md` (correcciones de la 128, 6 puntos: caida de reporte
de baterias, caida de expediente del rebase con `9c222986` escrito, regla
compuesta de push, las dos guardas ya verdes, caida de encargo del auditor,
ramal xi). Nota aditiva en `05_SANEO.md` (verificacion 1 pasa a VERDE tras
3.a). Tercera entrada de `aristas-huerfanas-por-fusion` (29/29/1/0 remedido
dos veces mas, cuadra). Docstring de `verificar_cierre_sellado.py`
corregido por adicion: el caso real uso `ce51aa27` sintetico, no `74d55f9e`
(verificado hoy: real de `main`, ajeno a la rama, y no se uso).
## TAREA 3.b, primera mitad de OP-S-11, REGIMEN A estricto (dataset intacto)
Verificado antes de medir: ninguna tabla de mapeo vive en `docs/` (21
ficheros mencionan "grafia", ninguno trae la correspondencia). Censo
(`SALIDA_V130_3B_CENSO_FUENTE.txt`): separador argumentado con los datos,
SOLO `|` (el `;`, 264 nodos, junta coautores o capitulos del MISMO libro,
nunca declaraciones; partirlo fabrica apellidos sueltos como grafia).
Candidatos: solo `;` -> 135; `;` y `|` -> 128; **solo `|` (propuesto) -> 129**
(coincide con el 129 del 11 ago 2026 por razones propias, no por copia).
Grupos mecanicos: 13 por prefijo (31 grafias), 0 por normalizacion. Sin
agrupar: 98, piden decision del auditor. Tabla propuesta:
`docs/plan/OP_S_11_MAPEO_PROPUESTO.md`, 129 filas, fichero nuevo, NO
aplicada, NO cambia el estado de OP-S-11. Hugos/Horowitz en dos unidades:
Hugos 2 grafias/95 en las dos; Horowitz **3/71 nodos** (fuente entero)
contra **2/72 declaraciones** (`|`, un nodo combina 3 libros). Ninguna es la
del recorte posicional (23/21, 16/14, otro universo, 67 nodos).
## Guardas 1.e/1.f/1.g/1.h/1.i finales
Citas (`SALIDA_V130_1E_VERIFICAR_CITAS.txt`, y VERDE sobre este mismo
REPORTE.md via 1.i), titulos+autoprueba+2 mutaciones VERDE, cifras del plan
(0 pares)+2 casos positivos VERDE (`SALIDA_V130_1F_VERIFICAR_CIFRAS.txt`),
fusion OPS09 (4 REPITE+2 autopruebas)+aristas vivas+huerfanas, todas VERDE
(`SALIDA_V130_1G_FUSION_ARISTAS.txt`). Caso rojo de la 1.h
(`SALIDA_V130_1H_CIERRE_SELLADO.txt`) probado por mutacion en las dos
direcciones: VERDE con HEAD real, ROJO con los dos sinteticos.
## DISCUTIBLES MARCADOS
1. Verificacion 1 de OP-S-10 en VERDE (29/29): no cierro la operacion, la
   adjudica el auditor.
2. Censo de fuente con separador `|`: coincide en 129 con la cifra del 11
   ago 2026; se trae la coincidencia como dato, no como prueba de acierto.
3. TAREA 2 bundle unico (2.a-2.d en un commit por tocar los mismos ficheros).
Racha de caidas de reporte: 0. Tope 80: `wc -l` da 80 (`SALIDA_V130_1K_WC_REPORTE.txt`).
