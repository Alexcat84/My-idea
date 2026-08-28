## VUELTA 111, TAREA 1: LOS REGISTROS DEL ACTA 110

### 1.1 LA VARA DE TECHO DOS, CAIDA DEL AUDITOR, DE ENCARGO

La TAREA 5 de la vuelta 110 encargo una vara sobre la especie estricta de
construccion de dos argumentos (verbos alinear/diferenciar/reemplazar/
vincular/combinar) sin decir sobre cuantos pares podia morder. Medido hoy
por el auditor y confirmado por `censar_alcance_de_la_vara.py`
(`docs/loop/SALIDA_V111_TAREA4_1_CENSO_ALCANCE.txt`): de las 74 RESUELTA
vivas, 72 son OBJETO y solo 2 son SATELITE (87 y 109); el techo de
hallazgos de esa vara era DOS, no setenta y cuatro. La cosecha 0 de la
vuelta 110 es CORRECTA (los dos unicos SATELITE del lote, 87 y 109, no son
de la especie estricta de esa vara), pero no prueba salud por si sola: la
vara apuntaba donde casi no habia nada que ver. **La caida es del auditor,
de encargo**, declarada por el mismo en su acta. Remedio: TAREA 4 de esta
vuelta (`censar_alcance_de_la_vara.py`, toda vara declara su techo antes
de correrse desde ahora).

### 1.2 LA CAIDA DE EXPEDIENTE DEL EJECUTOR, EL "ANTES" DEL CASO O SIN MEDIR

`docs/loop/REPORTE.md` de la vuelta 110 publico del caso O "ROJO EXIT 1
nombrando 91, antes y despues, sin apagarse" citando SOLO el fichero de
DESPUES: no existia ningun `SALIDA_V110_TAREA2_5_CASO_O_ANTES.txt`. Medido
hoy: `verificar_vuelco_de_veredicto.py` en su version de `55a48875` contra
`docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md` da CUATRO vuelcos, el
91 MUDO, ROJO EXIT 1 (`docs/loop/SALIDA_V111_CASO_O_ANTES.txt`): la
afirmacion del reporte de la vuelta 110 era CIERTA, lo que faltaba era la
medicion. Por la letra del 27 ago NO acumula (no es caida de cifra
publicada ni de reporte), pero es la SEGUNDA vuelta seguida de la misma
especie (la primera fue la caida 4.2 de la vuelta 109, "antes de la TAREA 3
era 73/74"): dispara el remedio de codigo, EJECUTOR.md 1, la extension del
tallador a la letra del "antes". Remedio: TAREA 2 de esta vuelta
(`scripts/loop/tallar_cifras_de_antes.py`, BLOQUEANTE, VERDE/ROJO
confirmados antes de escribir una sola cifra de "antes" en este mismo
reporte).

### 1.3 LA ADJUDICACION DEL 154, CERRADA, SIN CAIDA DE NADIE

Cerrada en OBJETO en la relectura conjunta de la vuelta 110
(`correccion_v110`, `docs/loop/SALIDA_V106_TAREA4_3_TRES_VIAS.txt`, bloque
del PUESTO 154), con el precedente citable del 123 y el 145 (misma especie,
misma siembra del barrido 106, corregidos en la vuelta 107 sin que ninguna
acta los contara como caida de clase). Ninguna cifra publicada se mueve:
`contar_cierre_efectivo.py` da 74/109 (59,6%) con cualquiera de los dos
veredictos (SATELITE u OBJETO).

### 1.4 LA MUTACION P, CAIDA PROPIA DEL AUDITOR, AUTODECLARADA

El auditor construyo su propia mutacion sobre el volteo en sitio del 154
(`docs/loop/_auditor_v110_mut/v106_sin_decl_154.txt`, la mutacion P,
sumada a la nomina fija de las guardas del cierre desde esta vuelta). Su
primera version solo borro la fila del 154 y dio DECLARADO; el instrumento
del ejecutor tenia razon y el auditor no, porque la declaracion tambien
vivia en la NOTA ADITIVA del pie del fichero (el mismo caso que el
docstring de `verificar_vuelco_de_veredicto.py` ya documenta como caso 109
de esa familia). **Caida propia del auditor, autodeclarada en su acta**,
corregida antes de publicar su version final (sin declaracion en ningun
sitio, fila y pie): esa version SI da MUDO, ROJO, y el instrumento del
ejecutor la nombra.

### 1.5 EL SEXTO VUELCO, SIN CAIDA DE NADIE

Corrido hoy sobre HEAD, `verificar_vuelco_de_veredicto.py` halla SEIS
vuelcos, no cinco: el sexto es el 154 EN SITIO (SATELITE en `fb067d4f` a
OBJETO hoy), DECLARADO. El caso positivo de la TAREA 2 de la vuelta 110
decia cinco porque se corrio ANTES de la TAREA 3 de esa misma vuelta (el
orden que el propio auditor fijo), no por un error del ejecutor: la guarda
que nacio esa vuelta ya vigila la correccion que esa misma vuelta escribio.

### 1.6 LA COMPOSICION DEL ANADIDO, TALLADA

DISCUTIBLE DE METODO, marcado antes de saber si acierto: `--patron` casa
"1.1".."1.5" en CUALQUIER tabla del fichero con esta forma, y desde la
vuelta 110 hay DOS (la de la vuelta 110 y esta), asi que tallar contra
`docs/PENDIENTES.md` entero mezcla las dos tablas (10 filas, no 5). Para
tallar SOLO el anadido de esta vuelta, `sed -n '6252,$p' docs/PENDIENTES.md
> docs/loop/_v111_pendientes_tarea1_solo.md` (linea de arranque de "##
VUELTA 111, TAREA 1", medida con `grep -n` sobre el fichero) y despues:
`python scripts/loop/tallar_composicion_salida.py --fichero docs/loop/_v111_pendientes_tarea1_solo.md --patron "^\| (?P<sub>1\.\d) \| (?P<clase>[A-Z_]+) \| (?P<atrib>[A-Z]+) \|$" --clave sub --campo-clase clase --valor-base SIN_CAIDA --etiqueta-base "sin caida" --etiqueta-otra "caida" --clase-cotejo "caida" --lista-citada 1.1,1.2,1.4`
(salida completa en `docs/loop/SALIDA_V111_TAREA1_6_COMPOSICION.txt`): de
los cinco subapartados de arriba, TRES son CAIDA (1.1 AUDITOR, de encargo;
1.2 EJECUTOR, de expediente; 1.4 AUDITOR, autodeclarada) y DOS son
SIN_CAIDA (1.3 cerrada sin caida de nadie; 1.5 explicacion del orden, sin
caida de nadie). Cotejo contra la lista citada arriba: SOBRAN NINGUNO,
FALTAN NINGUNO.

| sub | clase | atribucion |
|---|---|---|
| 1.1 | CAIDA | AUDITOR |
| 1.2 | CAIDA | EJECUTOR |
| 1.3 | SIN_CAIDA | NINGUNO |
| 1.4 | CAIDA | AUDITOR |
| 1.5 | SIN_CAIDA | NINGUNO |
