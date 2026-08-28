## VUELTA 117, TAREA 1: LOS REGISTROS DEL ACTA 116

### D.1 LA CAIDA DE GUARDA QUE NO ALCANZA, CAIDA DEL EJECUTOR

`vuelta116_guardas_cierre.py` declaraba, TECLEADO, "NUEVE INSTRUMENTOS" en su
apertura y en su cierre, pero su lista `INSTRUMENTOS` tenia OCHO entradas
(numeradas de la 2 a la 9, contadas con `ast` sobre el fichero, no a ojo): el
INSTRUMENTO 1, `tallar_veredictos_reporte.py --reporte` sobre el PROPIO
REPORTE.md, nunca entro a la lista. Un `grep` de `tallar_veredictos` sobre
`docs/loop/SALIDA_V116_GUARDAS_CIERRE.txt` no da una linea. La vuelta 115 SI
lo corrio aparte y pego sus diez lineas al final de su fichero
(`SALIDA_V115_GUARDAS_CIERRE.txt` linea 47), sin sumarlo al conteo del
script. La salida de la 116 se abre con "NUEVE INSTRUMENTOS Y VEINTINUEVE
CASOS" y se cierra con "VERDE: los VEINTINUEVE casos de mutacion y los NUEVE
instrumentos calzan": un veredicto uniforme sobre nueve cuando corrieron
ocho. El propio docstring se contradice solo: "mas los NUEVE instrumentos
(los mismos ocho de la vuelta 115...)". La cifra de casos SI se cuenta del
codigo (correcta); la de instrumentos estaba TECLEADA, NUEVE como literal
seis veces. Ningun dato se dano: el auditor lo corrio y dio EXIT 0 VERDE. NO
ACUMULA en ninguna racha (no es clase, ni cifra publicada en tabla, ni
reporte). Remedio: TAREA 2 de la vuelta 117, BLOQUEANTE, y QUEDA CERRADA por
ella: `vuelta117_guardas_cierre.py` mete el instrumento 1 A LA LISTA (entra
como la entrada 1, ya no corre aparte) y las lineas de apertura y de cierre
imprimen `len(INSTRUMENTOS)` y `total_casos` con `%d`, nunca un literal.
MUTACION BB (`scripts/loop/vuelta117_tarea2_3_mutacion_bb.py`) prueba, del
lado rojo, que el numero SI se mueve si la lista se mueve: una copia con una
entrada de `INSTRUMENTOS` quitada dice 8 en vez de 9, en las dos lineas
(`docs/loop/SALIDA_V117_TAREA2_3_MUTACION_BB_ANTES.txt` dice 9,
`_DESPUES.txt` dice 8, PASA EXIT 0).

### D.2 LA CAIDA DE INCUMPLIMIENTO DE ENCARGO, CAIDA DEL EJECUTOR

La letra literal del encargo de la 116 decia, en mayusculas y como
correccion expresa de la observacion de la 115: "ESTA VEZ LOS ABSOLUTOS VAN
AL REPORTE, en una linea, DICIENDO CONTRA QUE CIFRA MIA LOS COMPARAS". Un
`grep` de `16 / 5 / 59`, `15 / 4 / 58`, `crudo` y `neto` sobre el
`REPORTE.md` de la 116 no devuelve una sola linea. Los absolutos estan y son
correctos en la salida de guardas de esa vuelta, pero ninguno bajo al
reporte: es la SEGUNDA vez que se incumple esta letra (la primera fue
observacion en la 115, precisamente para apretarla). Las dos ternas medidas
por el auditor sobre 633 ficheros `.py` de `scripts/loop` (626 de la 115 mas
los siete de la 116): crudo `16 / 5 / 59` union `73`, neto `15 / 4 / 58`
union `72`, ninguno de los siete ficheros nuevos casa ninguno de los tres
patrones. Remedio, TAREA 2.5 de la vuelta 117: los absolutos SI van en este
reporte, re-medidos hoy sobre 636 ficheros `.py` de `scripts/loop` (633 de
la 116 mas los tres nuevos de la TAREA 2 de esta vuelta): crudo `16 / 5 / 59`
union `73`, neto `15 / 4 / 58` union `72`, IDENTICO al contraste del
auditor: ningun absoluto bajo, ninguno de los tres ficheros nuevos casa
ningun patron (commit de la TAREA 2 de esta vuelta cita la corrida
completa).

### D.3 LA CAIDA DE EXPEDIENTE, CAIDA DEL EJECUTOR

El registro C.5 de `docs/PENDIENTES.md` (vuelta 116) escribio: "cinco de las
siete lo hacen por `OP-M-01` y tres por `OP-M-03` (la TAREA 3.1 de esta
vuelta recalculo el cierre entero y calza al digito con el contraste del
auditor)". La aritmetica desmiente el parentesis: cinco mas tres son OCHO, y
solo hay SIETE operaciones que remiten; no pueden caber. La cifra "cinco y
tres" es del auditor (de su propia acta 115, mandada transcribir); EL
PARENTESIS QUE LA CERTIFICA NO ESTABA MANDADO Y ES DEL EJECUTOR de la 116, y
es FALSO: su propia salida 3.4
(`docs/loop/SALIDA_V116_TAREA3_4_CRITERIOS_REMISION.txt`) dice **CUATRO** a
`OP-M-01` y **TRES** a `OP-M-03`, no cinco y tres. Es exactamente lo que la
letra de la propia vuelta 116 prohibe: toda causa que se publique se cuenta
contra el fichero que la cita, y esta no se conto contra nada. NO ACUMULA
para la parada (`docs/PENDIENTES.md` no es `docs/plan/`, ni el banco, ni
`REPORTE.md`), pero SI se corrige con correccion declarada: ver la
correccion pegada debajo del C.5 original, mas arriba en este mismo fichero,
que deja el texto viejo entero y agrega la cifra correcta con su fichero.

### D.4 LA CAIDA DE REPORTE DE LA CITA, CAIDA DEL EJECUTOR

El reporte de la 116, su salida 3.3 y el asunto del commit `ac0e90be`
escriben: "los dos enlaces mutuos del banco 9.22, `LD-41` y `LD-43`, viven
en `OP-E-05` segun `LD_MESA_UNIDA.md`, no en `OP-E-01`". Un `grep` de
`OP-E-05` sobre `docs/plan/LD_MESA_UNIDA.md` no devuelve NADA: esa pagina
describe `LD-41` y `LD-43` como enlaces mutuos en sus lineas 140, 160 y 301,
y no nombra ninguna operacion. La asignacion real vive en
`docs/plan/OPERACIONES.jsonl`, en el campo `aristas_nuevas` de `OP-E-05`
(re-medido hoy en la TAREA 3.1 de esta vuelta,
`docs/loop/SALIDA_V117_TAREA3_1_CRITERIO_HECHO_TRES_FUENTES.txt`: las dos
direcciones de `LD-41` y de `LD-43` estan en `OP-E-05.aristas_nuevas`, que
cita `LD_MESA_UNIDA.md` en su propio campo `evidencia`, no la pagina
directamente). El FONDO es cierto y esta verificado: los dos enlaces mutuos
son de `OP-E-05`, no de `OP-E-01`. NO ACUMULA por la letra del 27 ago 2026
(vive en un parentesis de prosa del reporte), pero SI dispara la relectura
al doble del tramo (cumplida en esta vuelta: la TAREA 3.1 corrio sobre las
TRES fuentes, el doble del tramo habitual de una).

### D.5 LAS TRES CAIDAS DEL AUDITOR, CAIDA DEL AUDITOR

(a) El auditor mando medir el DESBLOQUEO de `OP-E-06` y `OP-E-07`, dos
operaciones que YA ESTABAN EJECUTADAS: las dos traen, en su propio campo
`nota`, un `ADDENDUM DE EJECUCION` (`OP-E-06` abre en la vuelta 90, fecha
real 27 ago 2026, con 113 aristas ESCRITAS y 1 YA_ESTABA; `OP-E-07` abre en
la vuelta 91, fecha real 27 ago 2026, con 86 ESCRITAS y 2 YA_ESTABA). El acta
115 las presento como trabajo futuro y mando medir el cierre transitivo de
sus DEPENDENCIAS sin mandar leer SU PROPIA nota, que es donde estaba la
respuesta entera. (b) El auditor apunto la TAREA 3.2 de la 116 al campo
`nota` como si fuera la UNICA superficie de registro de cierre, cuando la
doctrina que el mismo cita (acta 100, seccion 4.2) no nombra una superficie
unica. La medicion del ejecutor de la 116 fue exacta sobre el campo que se
le nombro, y el hallazgo de que `OP-D-03` y `OP-D-04` tambien traen registro
de cierre es real y suyo. (c) El auditor publico una cifra FALSA en su
propia acta 115: "cinco por `OP-M-01` y tres por `OP-M-03`" sobre SIETE
operaciones (cinco mas tres son ocho, no caben en siete). La cifra correcta,
medida hoy por partida doble (TAREA 3.4 de la 117, corrida tal cual sobre
las siete y acotada a las cinco): **CUATRO a `OP-M-01`, TRES a `OP-M-03`**
sobre las siete originales.

### D.6 LA CORRECCION DECLARADA DEL REGISTRO C.5 DE LA VUELTA 116, SIN_CAIDA

La correccion esta pegada DEBAJO del C.5 original, mas arriba en este mismo
fichero (no se reescribio ni se borro una letra del texto viejo), con la
cifra correcta (CUATRO a `OP-M-01`, TRES a `OP-M-03` sobre las siete;
CUATRO a `OP-M-01`, UNA a `OP-M-03` sobre las cinco que quedan tras sacar a
`OP-E-06`/`OP-E-07` ejecutadas) y el fichero que la mide
(`docs/loop/SALIDA_V117_TAREA3_4_CRITERIOS_REMISION_SIETE_TAL_CUAL.txt` y
`docs/loop/SALIDA_V117_TAREA3_4_CRITERIOS_REMISION_CINCO.txt`).

### D.7 LAS DOS DOCTRINAS ADJUDICADAS, SIN_CAIDA

**(1) EL REGISTRO DE CIERRE CUENTA VIVA DONDE VIVA DENTRO DE `docs/plan/`**,
con su cita localizada; la superficie no lo hace mas ni menos escrito. La
casa usa TRES formas, TODAS re-medidas HOY por la TAREA 3.2 de esta vuelta
(`docs/loop/SALIDA_V117_TAREA3_2_REGISTRO_CIERRE_TRES_SUPERFICIES.txt`): el
campo `nota` (`OP-D-03`, `OP-D-04`, `OP-D-07`); el encabezado de seccion en
la pagina de su fase (`OP-D-03` en `02_DESTEJIDOS.md:1197`, `OP-D-04` en
`:1614`, `OP-D-05` en `:1765` y `:1839`, `OP-D-06` en `:3407`, `OP-D-07` en
`:4597`, y `OP-F-02`/`OP-F-03` en `01_FUENTES.md:617`); y la frase `REGISTRO
DE OPERACION HECHA` (compartida por `OP-D-01` y `OP-D-02` en
`02_DESTEJIDOS.md:3585`, y tambien presente para `OP-D-07` en `:4461`). Las
NUEVE de NUEVE dependencias de aguas arriba traen registro de cierre en AL
MENOS UNA de las tres superficies. **(2) UNA OPERACION CON ADDENDUM DE
EJECUCION ESCRITO Y SUS ARISTAS EN EL GRAFO ESTA EJECUTADA AUNQUE SU CAMPO
`estado` DIGA `LISTA`** (acta 100, seccion 4.2, mas el preambulo de
`AUDITOR.md`, "el estado de verdad es EL REPO"). Aplicado hoy: `OP-E-06` y
`OP-E-07` estan ejecutadas (TAREA 3.1 y 3.3 de esta vuelta: 114/114 y 84/84
aristas presentes en el grafo), y el registro de la vuelta 102
(`04_ENLACES.md:1343`, "1 HECHA, 2 EJECUTABLES y 7 BLOQUEADAS") estaba
desmentido por el repo antes de escribirse en lo tocante a esas dos.
Correccion declarada aditiva en `docs/plan/04_ENLACES.md`, TAREA 4 de esta
vuelta.

### D.8 LO QUE NO ES CAIDA EN LA 116, SIN_CAIDA

La extension de la capa de motivo a los veintiocho casos que hasta la 115
quedaban fuera (`ESPERADO_BASE_EXTRA`, ancla fija separada del valor
`ACTUAL`), bien construida y cierra su propia caida (C.2 de la 116); la
MUTACION AA, que muerde de verdad (control en CALZA sin alerta, mutado cae a
ROJO con la ALERTA nombrando el caso); las cuatro mediciones de la TAREA 3 de
la 116 (3.0 techo, 3.1 cierre transitivo, 3.3 criterio de HECHO, 3.4 tres
criterios de remision), que calzan al digito con las del auditor; y la TAREA
1 de la 116, cuya extraccion se re-hizo y da cero lineas de diff.

### D.9 LA COMPOSICION DEL ANADIDO, TALLADA

Extraccion del bloque hecha DESPUES de la ultima edicion de
`docs/PENDIENTES.md`. Linea de arranque medida con
`grep -n "^## VUELTA 117, TAREA 1" docs/PENDIENTES.md`, extraccion con
`sed -n '<linea>,$p' docs/PENDIENTES.md > docs/loop/_v117_pendientes_tarea1_solo.md`,
y tallado con `tallar_composicion_salida.py` (patron `sub`/`clase`/`atrib`,
valor base `SIN_CAIDA`, clase de cotejo `caida`, lista citada
D.1,D.2,D.3,D.4,D.5), salida completa en
`docs/loop/SALIDA_V117_TAREA1_COMPOSICION.txt`.

| sub | clase | atribucion |
|---|---|---|
| D.1 | CAIDA | EJECUTOR |
| D.2 | CAIDA | EJECUTOR |
| D.3 | CAIDA | EJECUTOR |
| D.4 | CAIDA | EJECUTOR |
| D.5 | CAIDA | AUDITOR |
| D.6 | SIN_CAIDA | NINGUNO |
| D.7 | SIN_CAIDA | NINGUNO |
| D.8 | SIN_CAIDA | NINGUNO |
