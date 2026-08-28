## VUELTA 106, TAREA 1: LOS REGISTROS DEL ACTA 105

### 1.1 EL HASH DE HEAD EN LA CABECERA, CAIDA MIA (vuelta 105), DE REPORTE

El bloque "CABECERA, cada celda con su fichero" del `REPORTE.md` de la
vuelta 105 abrio con "(rama `pasada-unica`, apertura `1b76e800`, HEAD
`ba261321`)". `docs/loop/SALIDA_V105_HEAD_CIERRE.txt` -- el fichero de esa
misma cabecera, ya existente, escrito por mi pero que ningun tallador leia
-- dice `275cb46c`, el commit donde de verdad corri el ciclo de cierre;
`ba261321` es el HEAD de mi TAREA 4.4, dos commits antes. Caida de reporte
por `AUDITOR.md` 1.1 ("toda cifra o nombre propio se lee de la salida del
instrumento corrido EN ESTA VUELTA"), y acumula por la letra afinada del 27
ago porque vive en una CABECERA, no en una lista de rutas ni en prosa. La
racha de reporte paso de CERO a UNO tras tres vueltas limpias. No mueve
ningun dato: las nueve mediciones de apertura y cierre calzan todas,
remedidas por el auditor. El remedio es codigo, TAREA 2 de esta vuelta:
`leer_head_cierre()` en `tallar_cabecera_reporte.py`, que lee
`SALIDA_V<N>_HEAD_CIERRE.txt` y publica el HEAD real de cierre en la
columna de cierre, con fallo declarado si el fichero falta. Tallar la
vuelta 105 con el instrumento reparado publica ahora `275cb46c`
(`docs/loop/SALIDA_V106_TAREA2_4_CASO_POSITIVO_V105_HEAD_CIERRE.txt`).

### 1.2 LOS CINCO GUIONES LARGOS, CAIDA MIA (vuelta 105), DE INCUMPLIMIENTO DE ENCARGO

`git diff 9cf7a06a..HEAD | grep '^+'` filtrado a U+2013 y U+2014 dio cinco,
los cinco U+2014, todos en las cabeceras de
`docs/loop/SALIDA_V105_TAREA4_4_LECTURA_ENTERA.md`. El encargo cierra,
como todos, con "Cero guiones largos y cero guiones medios", sin excepcion
para los ficheros de salida. En la vuelta 104 esa misma medicion daba
cero. Esta vuelta se corrio el mismo chequeo sobre los ficheros propios
antes del commit (regla 10 de `EJECUTOR.md`, deja correr el hook) y no se
repite.

### 1.3 EL PERIMETRO DE LAS DOS ORACIONES, CAIDA DEL AUDITOR, DE ENCARGO (arreglada esta vuelta)

`tallar_veredictos_reporte.py` ensanchaba, desde la vuelta 105, de la
oracion de la palabra a UNA sola oracion siguiente, solo si esa oracion no
traia veredicto propio. La mutacion E del auditor (cita DOS oraciones
despues, con una oracion neutra de por medio: "...salio VERDE y no hubo
nada que declarar. La corrida fue de rutina y no llevo mas de un segundo.
La evidencia esta en `...`.") daba VERDE, EXIT 0: el ensanche de un solo
paso no alcanzaba. Arreglado en la TAREA 3 de esta vuelta (bloqueante): el
ensanche avanza ahora EN CADENA por las oraciones del parrafo mientras
ninguna traiga veredicto propio, parando en la primera que si lo traiga.
Mis mutaciones D (VERDE, sigue igual: su oracion siguiente trae veredicto
propio y el avance se detiene antes de la cita), E (ROJO, avanza 2
oraciones) y F (ROJO, ya alcanzada por el ensanche de un paso desde la
vuelta 105) quedan citadas en
`docs/loop/SALIDA_V106_TAREA3_2_MUT_E_ANTES_DESPUES.txt` y
`..._TAREA3_3_LAS_CINCO_QUE_NO_SE_MUEVEN.txt`. **EL PERIMETRO QUE QUEDA
DESPUES DEL ARREGLO, escrito explicito como el encargo pide:** una cita en
OTRO parrafo (no en la cadena de oraciones del mismo parrafo que la
palabra) y una cita detras de una oracion CON veredicto propio siguen
invisibles POR DISENO (el avance se detiene ahi a proposito, para no
repetir el emparejamiento por parrafo que produjo los seis falsos de la
vuelta 103); la defensa real de esos dos casos es la cobertura que se
publica cada vuelta (`docs/loop/SALIDA_V106_TAREA3_5_COBERTURA_REPUBLICADA.txt`),
no una regla que los cubra.

### 1.4 EL TALLADOR DE CABECERA, GUARDA ENVEJECIDA (adjudicada por el auditor, arreglada esta vuelta)

`lado_fase04()` leia el marcador del cribado con el formato viejo tipo
diccionario (`'A': (\d+)` ... `\}\s*(\d+)\s*$`), que ningun script vigente
imprime desde la vuelta 53: `lado()`, linea 447 de
`tallar_cabecera_reporte.py`, ya usaba `\n  A\s+(\d+)` (el formato de
`recomputar_marcador.py`); `lado_fase04()`, linea 617, se quedo con el
formato viejo. El auditor lo adjudico como GUARDA ENVEJECIDA cubierta por
extension de la letra del fundador del 29 ago (la que convirtio el desfase
de opcional a fallo declarado por el mismo motivo) y de la adjudicacion
5.4 del acta 85, no como doctrina nueva. Arreglado en la TAREA 2 de esta
vuelta: los cinco regex al formato vigente, con `n` leido de la primera
linea del mismo fichero de marcador ("n = 3388..."). Caso positivo (vuelta
105, VERDE, A 551/B 72/C 5/D 2.760, n 3.388 en los dos lados) y caso rojo
por mutacion (A 551 mutado a A 999, la celda tallada cambia) en
`docs/loop/SALIDA_V106_TAREA2_2_3_CASO_POSITIVO_Y_MUTACION.txt`.

### 1.5 LO QUE SE HIZO BIEN EN LA VUELTA 105, PARA QUE NO SE PIERDA

**Los siete discutibles de la vuelta 105 coinciden 7 de 7 con la relectura
ciega del auditor**, sin reserva: los cinco que se movieron (20, 21, 38,
66, 93) y los dos que se sostuvieron (87, 91). Los DOS contra-casos que el
auditor escribio el mismo, fuertes a proposito, examinados y perdidos los
dos, con razon escrita. **El re-barrido de la TAREA 4 encontro exactamente
los ocho puestos del auditor y ni uno mas**, y cuando el auditor barrio los
33 restantes con red mas ancha (nueve formulas en vez de una), CERO
satelites perdidos entre los 33. El censo del paso mal casado aguanto una
red mas ancha que la propia y dio el mismo resultado (46 y 147). La
aditividad por `difflib` con `04_ENLACES.md` 0 borradas/+6,
`PENDIENTES.md` 0 borradas/+110, `OPERACIONES.jsonl` 71 filas antes y
despues con una sola tocada. El sellado de apertura hecho a la primera,
sin que hiciera falta recordarselo.

### 1.6 LAS TRES FALSAS ALARMAS DEL AUDITOR (4, 47, 77), CORREGIDAS ANTES DE PUBLICAR

El auditor volco los 33 puestos que la vuelta 105 dejo en OBJETO y busco la
especie del satelite el mismo, con red mas ancha; levanto tres candidatos
(4, 47, 77) y se le cayeron los tres al leerlos enteros: el 4 porque el
titulo del hijo es literalmente el acto del paso; el 47 porque el paso 3
del hijo ES el acto de la madre; y **el 77 se cayo por la MISMA regla que
sostuvo al 87 y al 91**, la distincion de que un complemento que vive
DENTRO del objeto directo (complemento del nombre, "el impacto de la
capacitacion EN EL DESEMPENO de los proyectos") no es satelite, y solo lo
es el que gobierna al hijo desde FUERA del objeto: la misma distincion que
esta vuelta volvio a aplicar en los puestos 102, 114 y 132 del lote de los
tramos 3 y 4. La linea del ejecutor es internamente consistente.

### 1.7 EL PUESTO 147, LA DIRECCION YA ANULADA DESDE LA CORRECCION_V99

El auditor anoto, sobre el censo del paso mal casado de la TAREA 4.2 de la
vuelta 105, que el 147 ya tenia la direccion anulada desde `correccion_v99`
(`docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl`, puesto 147:
`correccion_v99` pone `direccion_leida` a `null`), asi que su paso mal
casado no toca ninguna cifra viva. Esta vuelta lo remidio de nuevo, en la
TAREA 4.1: el 147 ya NO PERTENECE al conjunto RESUELTA (medido hoy, no de
memoria), y por eso el encargo de la vuelta 106, al contarlo entre las 19
RESUELTA del tramo 3, se equivoco por ese puesto; la discrepancia se
declaro en la TAREA 4 (`docs/plan/04_ENLACES.md`, correccion del cierre de
la bolsa) en vez de resolverse copiando la lista del encargo.
