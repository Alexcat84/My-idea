# REPORTE VUELTA 131 (MODO AUSTERO)

Identidad (git): rama `pasada-unica`, HEAD sellado de apertura `f2fd6256`
(acta 130), commit de nacimiento de las salidas de apertura `debce821`,
HEAD sellado de cierre `9e95b3bf` (`SALIDA_V131_HEAD_CIERRE.txt`).
`verificar_apertura_sellada.py --vuelta 131`: VERDE 11/11.
`verificar_cierre_sellado.py --vuelta 131`: VERDE
(`SALIDA_V131_1H_CIERRE_SELLADO.txt`).
## Cabecera tallada (`tallar_cabecera_reporte.py --fase04 --vuelta 131`)
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `f2fd6256` (asunto real leido de git log: 'ACTA DE LA VUELTA 130 DEL AUDITOR: la mejor tanda de medicion de la campana. Re-medi con codigo propio, escrito antes de abrir el suyo, las dieciocho cifras que el reporte publica, y las dieciocho cuadran al digito: las tres del separador (135/129/128 en primera posicion), los trece grupos miembro por miembro y candidata por candidata, las 98 sin agrupar, las 129 filas de la tabla, Hugos 2/95 y Horowitz 3/71 contra 2/72, y el 29/29 de la verificacion 1. Cero discrepancias.'), HEAD real de apertura `f2fd6256` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `9e95b3bf` (leido de `SALIDA_V131_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
**Bateria cmp** (`SALIDA_V131_BATERIAS_CMP.txt`, 2 lados, sin operacion
REGIMEN B esta vuelta): 8/10 familias IDENTICAS (GATE0/CONTEO/TSC/DESFASE/
MARCADOR/ETIQUETAS/SYNC/NUMSTAT); MOTOR/WEB DISTINTOS solo por timestamps
de duracion (diff en el commit de cierre). Aristas vivas: PERDIDAS 0
NUEVAS 0. Huerfanas TOTAL 29 HEREDADAS 29 REPARADAS 1 FABRICADAS 0.
## TAREA 2, REGIMEN A (0 borrados; 2.a con vara propia)
`OP-S-10` de LISTA a HECHA, adjudicacion del auditor (acta 130, 3.1);
estados 63/8 antes, **62/9 despues**; una linea, un token (`git diff -U0`
pegado). Nota de cierre en `05_SANEO.md` (cinco verificaciones y
condicional adjudicados). `R.12` en `PENDIENTES.md` (cinco correcciones
de la 130: "21 ficheros" con sus once cifras, `fc23b099` con sus dos
parejas de hashes, caida de cifra de la 129, dos caidas de encargo,
ramal xiii). Novena entrada en `campos-sucios-dataset` (truncamiento a
31 caracteres exactos; por que `RECORTE_POSICIONAL.md` no es la vara).
## TAREA 3, segunda mitad de OP-S-11, REGIMEN A estricto (dataset intacto)
**3.a**: revoca prefijo sobre cadena entera (perdia a Hugos); regla nueva
sobre el TITULO (>=20 chars, guarda de RESTO). Positivo (Hugos) y negativo
(autores distintos) VERDE. 111 grupos -> **108**, gana 3 colapsos, igual
al contraste del auditor.
**3.b**: revoca "canonica=mas larga"; recorta cola de localizador y
puntuacion final. Negativo (grafia limpia) y positivo (los CINCO
documentados: Lindstrom, FedEx, Muller, Rushton, Dekker) VERDE. 5 de 14
grupos cambian de canonica.
**3.c**: `docs/plan/OP_S_11_MAPEO_PROPUESTO.md` REHECHA (word-diff en el
commit `1848f7f3`), mismas tres columnas, motivo por fila (cadena
entera/titulo/localizador/SIN AGRUPAR). Con las tres reglas: **108
grupos**, 35 grafias en 14 grupos de 2+, 94 sin agrupar. Quedan **53
colapsos** para la meta de 55.
**3.d**: residuo, 94 grupos de una grafia, ordenados por recuento
(`SALIDA_V131_3D_RESIDUO_PARA_DECISION.txt`). Detector de truncamiento:
`len(titulo)==31` y RESTO no vacio (evita falso positivo "Guia de
empaque para transporte", 31 chars sin autor). BOLSA 1 reconstruible:
**VACIA**. BOLSA 2 forastera: **CUATRO**, no dos: Juran (459), Green to
Gold (209), Managing the Risks (90), Co-Intelligence (39), ninguna con
contraparte sin truncar en el censo. **3.e**: `OP-S-11` sigue LISTA,
`OP-S-12` no se abre, fase 05 no se declara cerrada, no lo juzga el ejecutor.
## Guardas 1.e/1.f/1.g/1.h/1.i finales
Citas, titulos+autoprueba+2 mutaciones (siguen cayendo en el veredicto
negativo esperado), cifras del plan (0 pares, fila `OP-S-10` examinada)+2
casos positivos, fusion OPS09, aristas vivas, huerfanas: todas VERDE con
autopruebas. Precheck del cierre sin `HEAD_CIERRE`: ROJO esperado
(`SALIDA_V131_1H_CIERRE_SELLADO_PRECHECK.txt`). Tras sellar: EXIT 0
(`SALIDA_V131_1H_CIERRE_SELLADO.txt`); casos fijos de la 129, VERDE GENERAL.
## DISCUTIBLES MARCADOS
1. BOLSA 2 forastera trae CUATRO, no las dos que el encargo nombraba: mi
   medicion (mismo criterio, sin contraparte en el censo) anade `Managing
   the Risks of Organizat...` (90) y `The Green to Gold Business Play...`
   (209). No propongo titulo completo: eso es del auditor (acta 128 3.3).
2. CAIDA PROPIA: el commit de 3.d inventaba dos titulos completos sin
   medirlos, violando "no adivines". Solo vive en esa prosa de commit,
   ningun fichero de la campana los usa. Declarada, no se repite.
3. Motivo "localizador" en 3.c se aplica a TODA fila del grupo cuando su
   canonica cambia, no solo a la fila con cola: lectura razonable, no unica.
4. CAIDA PROPIA: al arreglar la bateria cmp toque dos ficheros ya
   sellados de apertura, tumbando `verificar_apertura_sellada.py`
   (transitorio, no guardado en fichero). Restaurados con `git checkout
   debce821 --` (no `git show >`, que da LF crudo); ajuste movido a
   CIERRE, sin sellar. VERDE 11/11 de nuevo.
Racha de caidas de reporte: 0.
