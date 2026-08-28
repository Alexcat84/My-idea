## VUELTA 116, TAREA 1: LOS REGISTROS DEL ACTA 115

### C.1 LA CAIDA DE REPORTE DEL PARENTESIS QUE ATRIBUYE A T UN EXIT QUE SU FICHERO NO LE ATRIBUYE, CAIDA DEL EJECUTOR

El reporte 115 escribio, de la mutacion Z: "ANTES (real,
`SALIDA_V115_TAREA2_4_MUTACION_Z_ANTES.txt`): `[CALZA]` sin alerta, EXIT 1
(por T y por los dos instrumentos que dependian del reporte, ver abajo)". En
ese fichero, T sale "EXIT 1 (esperado 1) [CALZA]", es decir CALZA, y la
ultima linea del propio fichero enumera las causas reales del EXIT 1:
"ROJO: 2 caso(s) NO CALZAN: 4. verificar_cabecera_pegada_o_condensada.py, 8.
tallar_cabecera_reporte.py". SON DOS y T no es una de ellas; el auditor lo
confirmo leyendo el codigo, el EXIT sale de la lista `fallos` y T no entra en
ella. NO ACUMULA PARA LA RACHA por la letra del 27 ago 2026
(`paradas/2026-08-27-racha-parentesis-DECISION.md`): cuenta para la racha
solo si la cifra vive en una tabla, una cabecera o una conclusion, y esta
vive en un parentesis de prosa. Pero SI dispara la relectura al doble del
tramo. Lo que NO se cobra: el "ver abajo" SI tiene su abajo en el parrafo de
GUARDAS DEL CIERRE del mismo reporte.

### C.2 LA CAIDA DE GUARDA QUE NO ALCANZA, CAIDA DEL EJECUTOR

`vuelta115_guardas_cierre.py` construyo bien su capa de MOTIVO
(`ESPERADO_BASE` anclado aparte de `CASOS`, `imprimir_caso` compara y, si
difieren, imprime `MOTIVO` o `ALERTA`), pero `ESPERADO_BASE` solo tiene
VEINTIDOS entradas y solo pasan por `imprimir_caso` los veintidos de `CASOS`.
LOS OTROS SEIS (X, Y, TAREA2.4-v109, N, O, P) llevaban su esperado cableado
en su propia funcion, sin `ESPERADO_BASE` y sin poder disparar la ALERTA: si
alguien voltea en silencio el esperado de X, la guarda no lo delataba. La
salida se abria con "NUEVE INSTRUMENTOS Y VEINTIOCHO CASOS" y se cerraba con
"VERDE: los VEINTIOCHO casos ... calzan", un veredicto uniforme sobre
veintiocho cuando la proteccion llegaba a veintidos. NO ACUMULA en ninguna
racha (no es clase, ni cifra publicada, ni reporte). Su remedio es la TAREA 2
de esta vuelta, BLOQUEANTE, y QUEDA CERRADA por ella: `vuelta116_guardas_cierre.py`
ancla los seis con `ESPERADO_BASE_EXTRA`, publica su cobertura por codigo
("28 de 28 casos anclados") y la MUTACION AA prueba, del lado rojo, que
aflojar la propiedad esperada de uno de los seis sin motivo cae a ROJO (ver
TAREA 2 y `docs/loop/SALIDA_V116_TAREA2_3_MUTACION_AA_ANTES.txt` /
`_DESPUES.txt`).

### C.3 LA OBSERVACION QUE NO ES CAIDA, SIN_CAIDA

La letra de la 114 pedia "publica los absolutos que te salgan y di contra
que cifra de las mias los comparas": el reporte 115 no los trae en su propio
texto y no dice la comparacion. Los trae la salida de guardas que el reporte
cita, y SON CORRECTOS: el auditor los reconto con codigo propio sobre los
626 ficheros `.py` de `scripts/loop` (620 de la 114 mas los seis nacidos en
la 115) y le dieron crudo 16 / 5 / 59 union 73 y neto 15 / 4 / 58 union 72,
ningun absoluto bajo, y el motivo de que tampoco subieran: ninguno de los
seis ficheros nuevos de la 115 casa ninguno de los tres patrones del
barrido.

### C.4 LA CAIDA DEL AUDITOR, DE PROCEDIMIENTO

El primer contador de censo del auditor pidio `n.get('id')` sobre un grafo
cuyo campo real es `node_id`, y le dio una union falsa de 6.954. La caso por
aritmetica (la union no puede ser menor que las 9.190 de `nodos_siguientes`)
antes de publicar nada y la corrigio, pero el acta 101 ya dejaba escrito
cual era el campo real: lo tenia escrito y no lo leyo.

### C.5 EL HALLAZGO DE ORDEN, DOCTRINA ADJUDICADA, SIN_CAIDA

Por dependencia DIRECTA, `OP-E-06` declara `OP-D-01` a `OP-D-07` y `OP-E-07`
declara `OP-E-06`: ninguna de las dos nombra una mesa ni una fusion. Por
CIERRE TRANSITIVO, si llegan a la fase 06, cinco de las siete lo hacen por
`OP-M-01` y tres por `OP-M-03` (la TAREA 3.1 de esta vuelta recalculo el
cierre entero y calza al digito con el contraste del auditor), y por eso el
registro vigente NO ES UNA CAIDA de nadie. Pero el camino de `OP-E-06` y
`OP-E-07` es UNO SOLO, `OP-E-06 -> OP-D-07 -> OP-M-03`, y `OP-D-07` es el
UNICO de los siete `OP-D` que declara dependencia de fase 06 Y TRAE REGISTRO
DE CIERRE ESCRITO ("REGISTRO DE CIERRE, 19 ago 2026 (vuelta 47) ... OP-D-07
QUEDA SELLADA POR LA VIA DE OP-D-05 SELLADA", con sus tres verificaciones
cerradas y cero nodos tocados). DOCTRINA ADJUDICADA (la del acta 100, seccion
4.2, no una nueva): una dependencia con registro de cierre escrito NO
bloquea aunque su campo `estado` diga LISTA; aplicada a `OP-D-07`, CORTA LA
CADENA. El limite, igual de claro: NO queda adjudicado que `OP-E-06` y
`OP-E-07` sean ejecutables, porque falta medir si `OP-D-01` a `OP-D-06` (y
`OP-F-02`/`OP-F-03`, de los que cuelgan) llevan tambien su registro de
cierre escrito. Esa medicion es la TAREA 3.2 de esta vuelta: TRAJO UN
HALLAZGO NUEVO, `OP-D-03` y `OP-D-04` TAMBIEN traen `REGISTRO DE CIERRE`
escrito (18 ago 2026 vuelta 36, y 19 ago 2026 vuelta 39), ademas de
`OP-D-07`. La adjudicacion sobre lo que eso implica para la cadena es del
auditor de la 117, no de esta vuelta.

### C.6 EL ORDEN DE LA FASE 05, ADJUDICADO Y ESPERANDO, SIN_CAIDA

(a) `OP-S-12` NO CORRE EN LA FASE 05, va AL FINAL de la campana, por
`AUDITOR.md` seccion 3 ("OP-S-12 al final") y por la atadura 2 de
`00_INDICE.md` ("va AL FINAL, despues de la ultima fusion"), y como la
ultima fusion vive en la fase 06, LA FASE 05 CERRARA CON REMISION DE
OP-S-12. (b) `OP-S-01` antes de `OP-S-09`, por el mapa de fases de
`00_INDICE.md`. (c) las otras siete en su orden declarado (`OP-S-02` 2,
`OP-S-03` 3, `OP-S-04` 4, `OP-S-05` 5, `OP-S-08` 7, `OP-S-10` 9, `OP-S-11`
11). (d) `OP-S-01` y `OP-S-09` MUEVEN IDS, asi que la fase 0 se re-verifica
con su criterio de HECHO escrito (las cinco guardas en verde y cada una
fallando primero en su caso positivo) ANTES de tocarlas, y no se hereda del
registro de la vuelta 102. LA FASE 05 NO SE ABRE en esta vuelta.

### C.7 LO QUE NO ES CAIDA EN LA 115, SIN_CAIDA

La cabecera pegada entera y tallada con su instrumento; el registro de las
siete bloqueadas, que se sostiene por cierre transitivo y por eso no se
cobra; y la capa de motivo en si misma, que esta bien construida y cierra la
caida A.2 (acta 113) para los veintidos casos que cubre.

### C.8 LA COMPOSICION DEL ANADIDO, TALLADA

Extraccion del bloque hecha DESPUES de la ultima edicion de
`docs/PENDIENTES.md`. Linea de arranque medida con
`grep -n "^## VUELTA 116, TAREA 1" docs/PENDIENTES.md`, extraccion con
`sed -n '<linea>,$p' docs/PENDIENTES.md > docs/loop/_v116_pendientes_tarea1_solo.md`,
y tallado con
`python scripts/loop/tallar_composicion_salida.py --fichero docs/loop/_v116_pendientes_tarea1_solo.md --patron "^\| (?P<sub>C\.\d) \| (?P<clase>[A-Z_]+) \| (?P<atrib>[A-Z]+) \|$" --clave sub --campo-clase clase --valor-base SIN_CAIDA --etiqueta-base "sin caida" --etiqueta-otra "caida" --clase-cotejo "caida" --lista-citada C.1,C.2,C.4`
(salida completa en `docs/loop/SALIDA_V116_TAREA1_COMPOSICION.txt`): de los
siete subapartados de arriba, TRES son CAIDA (C.1 y C.2 del EJECUTOR; C.4
del AUDITOR) y CUATRO son SIN_CAIDA (C.3, C.5, C.6, C.7). Cotejo contra la
lista citada: SOBRAN NINGUNO, FALTAN NINGUNO. Fidelidad de la extraccion:
`git diff` sobre el anadido real de `docs/PENDIENTES.md` contra este mismo
fichero tallado, en `docs/loop/SALIDA_V116_TAREA1_DIFF_FIDELIDAD.txt`.

| sub | clase | atribucion |
|---|---|---|
| C.1 | CAIDA | EJECUTOR |
| C.2 | CAIDA | EJECUTOR |
| C.3 | SIN_CAIDA | NINGUNO |
| C.4 | CAIDA | AUDITOR |
| C.5 | SIN_CAIDA | NINGUNO |
| C.6 | SIN_CAIDA | NINGUNO |
| C.7 | SIN_CAIDA | NINGUNO |
