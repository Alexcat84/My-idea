# REPORTE VUELTA 132 (MODO AUSTERO)

Identidad (git): rama `pasada-unica`, HEAD sellado de apertura `5eb04ca5`
(acta 131), commit de nacimiento de las salidas de apertura `5eb04ca5`,
HEAD sellado de cierre `3a5fd829` (`SALIDA_V132_HEAD_CIERRE.txt`, sellado
tras 1.a/1.b/1.c, ANTES de TAREA 3 por instruccion explicita del encargo
"NO ESPERES A LA TAREA 3": REGIMEN A puro, nada posterior toca dataset/).
`verificar_apertura_sellada.py --vuelta 132`: VERDE EXIT 0.
`verificar_cierre_sellado.py --vuelta 132`: VERDE
(`SALIDA_V132_1H_CIERRE_SELLADO.txt`).
## Cabecera tallada (`tallar_cabecera_reporte.py --fase04 --vuelta 132`)
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `5eb04ca5` (asunto real leido de git log: 'ACTA DE LA VUELTA 131 DEL AUDITOR: la vuelta entrego, el dataset no se movio un byte y las ocho cifras de la cabecera cuadran al digito con mi remedicion, pero DOS frases de contencion del reporte no reproducen y las dos acumulan.'), HEAD real de apertura `5eb04ca5` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `3a5fd829` (leido de `SALIDA_V132_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
**Bateria cmp** (`SALIDA_V132_BATERIAS_CMP.txt`, 2 lados, sin operacion
REGIMEN B esta vuelta): 8/10 familias IDENTICAS; MOTOR/WEB DISTINTOS solo
por timestamps de duracion (diff verificado antes de publicar). Aristas
vivas 7.296=7.296, PERDIDAS 0 NUEVAS 0. Huerfanas TOTAL 29 HEREDADAS 29
REPARADAS 1 FABRICADAS 0.
## TAREA 2, REGIMEN A puro (106 anadidas, 0 borradas)
`R.13` en `PENDIENTES.md`: las DOS caidas de reporte de la 131 que
acumulan (SEIS pares fichero:linea que desmienten "ningun fichero lo
usa"; traza de tres commits que desmiente "se movio a los dos ficheros de
CIERRE", EXITCODE 0/0/0/0 hoy), la caida de columna de titulo propuesto,
y mi propia caida de encargo (aritmetica 111/108/106). Ramales (xiv)/(xv)
enteros. DECIMA entrada en la ficha `fuente`: BOLSA 2a/2b con ficheros y
lineas, detector de truncamiento con su falso positivo nombrado.
## TAREA 3, segunda mitad de OP-S-11, REGIMEN A (dataset intacto)
**3.a** (AGRUPA, ramal xiv): igualdad exacta de la forma recortada de
localizador. Positivo (Lindstrom, 3 grafias -> 1 grupo) y negativo VERDE.
108 grupos -> **106**, gana 2 colapsos, igual al contraste del auditor.
**3.b** (SOLO CORONA, ramal xiv): canonica sintetica cuando ningun
miembro sigue siendo libro. Positivo (Lindstrom, SINTETICA) y negativo
(14 grupos de contraste) VERDE.
**3.c**: BOLSA 2 partida. 2a reconstruible (titulo copiado del fichero):
Green to Gold (`docs/CENSO_DUPLICACION.md:126`, `03_FUSIONES.md:8018`),
Managing the Risks (`CENSO_DUPLICACION.md:123`,
`FICHA_SUBFUSION_GRADIENTE.md:2612`, `PENDIENTES.md:3059`,
`03_FUSIONES.md:6522`). 2b forastera (propuesto por la fuente, marcado
FORASTERO): Juran's Quality Handbook, Co-Intelligence. DISCREPANCIA: mi
sonda anade un QUINTO fichero para Managing the Risks,
`03_FUSIONES.md:7159` (misma frase repetida); no la resuelvo.
**3.d, DISCUTIBLE, MEDIDO Y NO APLICADO**: prefijo sobre la forma
recortada (guarda >=20 caracteres). 106 grupos -> **104**, una fusion
nueva (3 grupos base, 7 grafias, familia Lindstrom completa, el ejemplo
que el encargo nombra). Lo adjudica el fundador.
**3.e**: `docs/plan/OP_S_11_MAPEO_PROPUESTO.md` REHECHA (word-diff
136/136 en su commit), CUATRO columnas, motivo con las DOS cosas
separadas (regla que agrupa + origen de la canonica). Cifras del plan
VERDE tras el cambio. **3.f**: `OP-S-11` sigue LISTA, `OP-S-12` no se
abre, fase 05 y 00_CODIGO sin tocar, no lo juzga el ejecutor.
## Guardas 1.e/1.f/1.g/1.h finales
Citas, titulos+autoprueba+2 mutaciones (siguen cayendo en el veredicto
negativo esperado), cifras del plan+2 casos positivos, fusion OPS09,
aristas vivas, huerfanas: todas VERDE con sus autopruebas. Sello de
cierre `SALIDA_V132_1H_CIERRE_SELLADO.txt` VERDE; casos fijos de la 129
(`SALIDA_V132_1H_CASOS_POSITIVOS.txt`), VERDE GENERAL.
## DISCUTIBLES MARCADOS
1. 3.d: prefijo sobre recortada, medido y no aplicado; la guarda de
   longitud >=20 caracteres es eleccion de diseno propia, no del encargo.
2. 3.c: mi sonda da CINCO ficheros para Managing the Risks, el encargo
   cito CUATRO; el quinto es `03_FUSIONES.md:7159`, misma frase repetida.
Racha de caidas de reporte: 0.
