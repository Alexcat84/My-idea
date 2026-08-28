## VUELTA 118, TAREA 1: LOS REGISTROS DEL ACTA 117

### E.1 LA CAIDA DE INSTRUMENTO CEGADO, CAIDA DEL EJECUTOR

`vuelta117_tarea3_2_registro_cierre_tres_superficies.py` publico, en su
superficie (C), `OP-D-07` en **SI**, citando `02_DESTEJIDOS.md:4461`. La
linea real, re-medida hoy (`docs/loop/SALIDA_V118_TAREA2_1_CENSO_TRES_SUPERFICIES.txt`),
dice literal: "**Por eso este registro NO dice `REGISTRO DE OPERACION
HECHA`.**": una negacion, no una afirmacion. El instrumento imprimia el
ENCABEZADO atribuido, nunca la LINEA CASADA: de haberla pegado, la negacion
habria saltado sola. La misma afirmacion viaja al asunto del commit
`aa45b6ed` ("y tambien la nota y la frase en :4461"), que por la doctrina
del dictado (banco, "toda cita que promete detalle...") es expediente y se
mide como el reporte. NINGUNA CONCLUSION SE MUEVE: `OP-D-07` trae registro
de cierre por (A) el campo `nota` y por (B) el encabezado
`02_DESTEJIDOS.md:4597`, asi que el 9 de 9 dependencias con registro se
sostiene entero (re-medido hoy, mismo fichero de salida). NO ACUMULA por ser
de expediente (categoria del acta 116, seccion 4.3). Remedio: TAREA 2
BLOQUEANTE de esta vuelta, `vuelta118_tarea2_1_censo_tres_superficies_reparado.py`,
con guarda de negacion probada por MUTACION CC del lado rojo
(`docs/loop/SALIDA_V118_TAREA2_5_MUTACION_CC_VEREDICTO.txt`: PASA EXIT 0).

### E.2 LA CAIDA DE EXPEDIENTE DE LA LISTA DE PALABRAS, CAIDA DEL EJECUTOR

`vuelta117_tarea3_3_censo_ejecucion_fase04.py` linea 47 declara
`PALABRAS_CIERRE = ("CERRADA", "SELLADA", "EJECUTADA ENTERA", "HECHO")`, sin
la palabra CIERRE. Corriendo el mismo censo con la lista ampliada
(`docs/loop/SALIDA_V118_TAREA2_2_CENSO_EJECUCION_FASE04.txt`), DOS celdas se
mueven: (i) `OP-E-03`, columna "registro en pagina", de **NO** a **SI**, por
`04_ENLACES.md:1474` ("## EL CIERRE DE LA LECTURA DE `OP-E-03`, EL
TERRITORIO SE ACABO"), re-medida hoy; (ii) `OP-E-01` gana la cita
`04_ENLACES.md:783` ("## `OP-E-01`, CIERRE MEDIDO"), re-medida hoy, que es
el registro de cierre de la operacion ENTERA (las dos citas viejas, lineas
60 y 139, son encabezados de PASO 1 y PASO 2, no del cierre completo).
Ninguna otra celda se mueve (las ocho restantes, comparadas linea a linea en
la misma salida) y ninguna cifra de `docs/plan/` se contamino: la columna
"registro en pagina" del censo de la 117 no se copio a `docs/plan/`, solo se
uso para adjudicar en prosa. NO ACUMULA por ser de expediente. Remedio:
TAREA 2 BLOQUEANTE de esta vuelta, lista ampliada a CINCO palabras y
declarada en la propia salida, probada por MUTACION DD del lado rojo
(`docs/loop/SALIDA_V118_TAREA2_6_MUTACION_DD_VEREDICTO.txt`: PASA EXIT 0).

### E.3 MIS DOS CAIDAS, CAIDA DEL AUDITOR

(a) DE ENCARGO: el auditor dio, en la TAREA 3.2 y 3.3 de la 116/117, "mi
contraste de hoy" con listas de palabras propias (todas usando CERRADA,
SELLADA o EJECUTADA ENTERA, ninguna la forma CIERRE), y el instrumento del
ejecutor heredo ese punto ciego reproduciendolo como si fuera el criterio.
Que el censo del ejecutor coincidiera al digito con el contraste del
auditor no probaba que el criterio estuviera bien construido. (b) DE CIFRA:
el acta de la vuelta 116 publico "297 aristas que la fase escribio de
verdad (98 + 113 + 86)". La cifra vigente es **296** (98 de `OP-E-01` + 114
de `OP-E-06` + 84 de `OP-E-07`, el ULTIMO fichero de direccion
`OP_E_07_DIRECCION_V94.jsonl`, re-contados hoy:
`docs/loop/SALIDA_V118_TAREA2_2_CENSO_EJECUCION_FASE04.txt`), con reparto
**293 ESCRITA y 3 YA_ESTABA** (98+0 de `OP-E-01`, 113+1 de `OP-E-06`, 82+2
de `OP-E-07` tras las correcciones declaradas de las vueltas 92, 93 y 94
sobre el addendum de `OP-E-07`). La cifra de "86 ESCRITAS" del addendum de
la vuelta 91 quedo SUPERADA TRES VECES por correcciones posteriores escritas
debajo, en la propia nota, hasta "84 con direccion, 82 ESCRITA, 2
YA_ESTABA"; el auditor no bajo hasta el final de su propia nota. Doctrina
que esto dispara: E.5 de este mismo registro.

### E.4 LA ADJUDICACION DE OP-E-01, SIN_CAIDA

`OP-E-01` TIENE SU DESTINO CUMPLIDO Y ESTA EJECUTADA. Cuatro apoyos, dos
re-medidos hoy: (1) su propia nota trae "CIERRE MEDIDO (27 ago 2026, vuelta
87)" y dice literal "esta nota es la unica declaracion de que quedo
ejecutada"; (2) `04_ENLACES.md:783` lleva el encabezado "## `OP-E-01`,
CIERRE MEDIDO (27 ago 2026, vuelta 87)", re-medido hoy en
`docs/loop/SALIDA_V118_TAREA2_2_CENSO_EJECUCION_FASE04.txt`; (3) sus 98 de
98 aristas estan presentes en el grafo de hoy por las dos vistas (TAREA 3.1
de la 117, `docs/loop/SALIDA_V117_TAREA3_1_CRITERIO_HECHO_TRES_FUENTES.txt`);
(4) la nota de `OP-E-06` la cita como precedente de operacion ejecutada.
Doctrina de base: acta 116, secciones 3.1 y 3.2.

### E.5 LA LETRA NUEVA, UN CONTRASTE NO ES UN CRITERIO, SIN_CAIDA

Cuando el auditor escribe "mi contraste de hoy", eso es una VARA DE
COMPARACION, no la definicion de lo que hay que buscar: un instrumento
construido para reproducir ese contraste hereda sus puntos ciegos (caso
real: E.3(a) de este registro). Desde esta vuelta: TODO INSTRUMENTO DE
CENSO IMPRIME SU PROPIO CRITERIO EN SU SALIDA (la lista de patrones citada
desde la constante, no solo en el docstring), y el contraste del auditor se
coteja DESPUES de correr el instrumento, nunca antes. Cita: `AUDITOR.md`
1.1, "el instrumento manda ... se citan como contraste", aplicada aqui al
encargo que el auditor mismo escribe.

### E.6 EL CIERRE CON REMISION DE LA FASE 04, SIN_CAIDA

El criterio de HECHO escrito (`00_INDICE.md`, tabla EL ORDEN, fila 4),
medido hoy clausula por clausula sobre las tres fuentes
(`docs/loop/SALIDA_V118_TAREA2_2_CENSO_EJECUCION_FASE04.txt` y
`docs/loop/SALIDA_V117_TAREA3_1_CRITERIO_HECHO_TRES_FUENTES.txt`, esta
ultima re-citada por no haber cambiado su base): ids RESUELTOS, 296 de 296
resuelven (272 directo y 24 por alias), cero rotas, las 296 presentes por
las dos vistas; una sola direccion salvo los dos mutuos (`LD-41`/`LD-43`,
que viven en `OP-E-05`, REMITIDA); cero aristas por alias nuevas (de los 24
que solo resuelven por alias, CERO tienen su forma cruda escrita en el
grafo). Las diez operaciones se reparten sin que sobre ni falte una: CINCO
CON DESTINO CUMPLIDO (`OP-E-01` por E.4, `OP-E-02` HECHA, `OP-E-03` con
ADDENDUM de la vuelta 94 y su encabezado de cierre en `04_ENLACES.md:1474`,
`OP-E-06` 114/114, `OP-E-07` 84/84) y CINCO REMITIDAS a la fase 06
(`OP-M-03-ENLACES` a `OP-M-03`, y `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES`
y `OP-M-01-SEXTO` a `OP-M-01`). El campo `estado` NO SE TOCA en ninguna.
Registro aditivo completo: TAREA 3 de esta vuelta, en
`docs/plan/04_ENLACES.md` y `docs/plan/00_INDICE.md`.

### E.7 LA APERTURA DE LA FASE 05, SIN_CAIDA

Orden adjudicado por el acta 115, seccion 5.1: `OP-S-01` primero, luego las
siete en su orden declarado (`OP-S-02` 2, `OP-S-03` 3, `OP-S-04` 4,
`OP-S-05` 5, `OP-S-08` 7, `OP-S-09` 8, `OP-S-10` 9, `OP-S-11` 11) y
`OP-S-12` REMITIDA al final de la campana (atadura 2 de `00_INDICE.md`).
GUARDA DE ENTRADA BLOQUEANTE, medida en la TAREA 4.1 de esta vuelta antes de
tocar cualquier otra cosa de la fase 05: `OP-S-01` y `OP-S-09` mueven ids, y
la atadura 1 de `00_INDICE.md` pone la fase 0 delante de todo lo que mueve
un id.

### E.8 LO QUE NO ES CAIDA EN LA 117, SIN_CAIDA

La TAREA 2 de la 117, que cerro su caida bloqueante de la vuelta 116 (el
instrumento 1 entra a `INSTRUMENTOS`, conteo por `len()`) y la probo
mutando (MUTACION BB, PASA EXIT 0); los absolutos de la Y, ya en su
reporte, identicos al contraste; las cuatro mediciones de la TAREA 3 de la
117 (3.0 techo, 3.1 criterio de HECHO, 3.2 registro de cierre en tres
superficies, 3.4 criterios de remision), que calzan al digito con las del
auditor salvo la unica celda de E.1; el registro aditivo de la TAREA 4,
medido en 94 lineas insertadas y 0 borradas; y el `REPORTE.md` entero de la
117, cuyas citas el auditor barrio una por una sin encontrar ninguna falsa
fuera de las dos ya nombradas en E.1 y E.2.

### E.9 LA COMPOSICION DEL ANADIDO, TALLADA

Extraccion del bloque hecha DESPUES de la ultima edicion de
`docs/PENDIENTES.md`. Linea de arranque medida con
`grep -n "^## VUELTA 118, TAREA 1" docs/PENDIENTES.md` (linea 7005),
extraccion con
`sed -n '7005,$p' docs/PENDIENTES.md > docs/loop/_v118_pendientes_tarea1_solo.md`,
y tallado con `tallar_composicion_salida.py` (patron `sub`/`clase`, valor
base `SIN_CAIDA`, etiquetas `sin caida`/`caida`, clase de cotejo `caida`,
lista citada E.1,E.2,E.3), salida completa en
`docs/loop/SALIDA_V118_TAREA1_COMPOSICION.txt`.

| sub | clase | atribucion |
|---|---|---|
| E.1 | CAIDA | EJECUTOR |
| E.2 | CAIDA | EJECUTOR |
| E.3 | CAIDA | AUDITOR |
| E.4 | SIN_CAIDA | NINGUNO |
| E.5 | SIN_CAIDA | NINGUNO |
| E.6 | SIN_CAIDA | NINGUNO |
| E.7 | SIN_CAIDA | NINGUNO |
| E.8 | SIN_CAIDA | NINGUNO |
