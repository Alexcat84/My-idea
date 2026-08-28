## VUELTA 107, TAREA 1: LOS REGISTROS DEL ACTA 106

### 1.1 LA CABECERA "PEGADA ENTERA", CAIDA MIA (vuelta 106), DE REPORTE

El reporte de la vuelta 106 dijo que la tabla de cabecera venia "pegada
entera" del tallador. El auditor corrio `tallar_cabecera_reporte.py` y
cotejo celda por celda, normalizando espacios y marcas: 11 filas de 11 en
los dos lados y mismo orden, pero NUEVE de las once difieren en su texto,
no en su valor. Las tres parejas citadas por el auditor: "censo: nodos /
vivos / deprecados" contra "censo"; "OK (auto-aristas 0, duplicadas 0,
divergentes 0)" contra "OK (auto-aristas 0, dup 0, diverg 0)"; "80 passed
(80) / 1.030 passed, 3 skipped (1.033)" contra "80(80)/1.030+3 skipped".
CAIDA DE REPORTE por `AUDITOR.md` 1.1. ADJUDICACION DEL AUDITOR: NO
ACUMULA, porque la letra afinada del 27 ago hace acumular cuando LA CIFRA
vive en una tabla, cabecera o conclusion, y las once celdas, verificadas
contra el instrumento corrido ese dia, son TODAS fieles en su valor: no
hay ninguna cifra equivocada, solo texto condensado bajo el austero
publicado con la etiqueta erronea "pegada entera". La racha de reporte
sigue en UNO. El remedio es la TAREA 2 de esta vuelta: una guarda que
distingue PEGADA ENTERA de CONDENSADA y que corre sobre este mismo
reporte antes del commit.

### 1.2 LA CIFRA DEL CIERRE DE LA BOLSA, CAIDA MIA (vuelta 106), DE
INCUMPLIMIENTO DE ENCARGO

El encargo de la vuelta 105 pedia cuantas RESUELTA vivas habian pasado
POR LA PREGUNTA DE TRES VIAS. La respuesta publicada en la vuelta 106,
"Faltan 2, ambos en tramo1 (puestos 3 y 16)", media otra cosa:
`veces_releido == 0` y sin correccion, o sea nunca releido por NINGUN
barrido. LAS DOS DEFINICIONES Y SUS DOS CIFRAS: (a) nunca releidos por
NADA, **2** (puestos 3 y 16); (b) sin pasar por LA PREGUNTA DE TRES VIAS,
**11** (3, 5, 7, 10, 13, 16, 19, 27, 30, 33 del tramo1, mas el 148 del
tramo3), de los cuales NUEVE pasaron por relectura ciega entera en las
vueltas 101 a 104 (instrumento mas fuerte, pero no la pregunta de tres
vias) y el 148 se resolvio por `correccion_v99`. El "2" es verdadero para
lo que el instrumento de la vuelta 106 media, y el propio reporte de esa
vuelta daba la definicion correcta dos parrafos mas abajo ("nunca
releidos por ningun barrido"): es INCUMPLIMIENTO DE ENCARGO, se pidio una
cuenta y se entrego otra sin decir que eran distintas. A FAVOR: el
ejecutor SE NEGO A DECLARAR LA BOLSA CERRADA cuando el encargo de la
vuelta 105 daba por hecho que lo estaria. El remedio corrio en esta misma
vuelta, TAREA 5: bolsa cerrada de verdad, 74/74 por la pregunta de tres
vias, 0/74 sin ningun instrumento.

### 1.3 EL 109, DISCREPANCIA DEL AUDITOR FUERA DEL MARCADO

El auditor volco los 24 puestos que la vuelta 106 dejo en OBJETO y busco
la especie del satelite por su cuenta. Levanto tres: 109, 110 y 180. Dos
se le cayeron (110 por ser PREDICATIVO, especie distinta del complemento
instrumental; 180 porque registrar patentes en cada pais via PCT ES el
acto que el hijo despliega). EL 109 AGUANTO: en el paso 1 de
`business_model_canvas_scorecard` ("Llenar el canvas inicial con tus
hipotesis en las 9 areas: segmentos, propuesta de valor, canales,
relaciones, recursos, socios e ingresos"), el objeto directo es "el
canvas inicial"; "con tus hipotesis en las 9 areas" es complemento
preposicional INSTRUMENTAL; "socios" vive DENTRO de ese complemento, o
sea FUERA del objeto directo. El motivo escrito en la vuelta 106 citaba
como objeto "el canvas inicial CON TUS HIPOTESIS EN LAS 9 AREAS...",
incorporando el complemento al objeto: ahi esta el error, de analisis y
no de criterio. Por `AUDITOR.md` 1.2, una discrepancia fuera del marcado
baja el credito de toda la tanda y dispara la relectura al doble del
tramo donde vive: el tramo 3 se releyo al doble en esta vuelta, TAREA 4.
El 109, examinado con lectura entera esta misma vuelta
(`docs/loop/SALIDA_V107_TAREA4_1_2_LECTURA_ENTERA_109.md`), SOSTIENE: el
contra-caso (paso 6 del hijo PLANEA, no ejecuta, la validacion; los pasos
1 a 4 desarrollan el item "socios" en procedimiento completo, patron del
9.6.2; el paso 5 es la entrega de vuelta, patron del 2.215) gana.

### 1.4 EL 145, DISCREPANCIA DEL AUDITOR SOBRE UN DISCUTIBLE MARCADO

El discutible 145 (marcado en la vuelta 106 tras `correccion_v106`, que
movio el par de DIRECCION AFIRMADA a NO RESUELTA) fue discrepado por el
auditor: la tesis de `correccion_v106` es que el paso 4 del hijo
(`proposito_como_motor_energia`, "Evitar sustituir el pensamiento
profundo por 'mera accion fisica' como escape de la incertidumbre")
tensiona con la tesis central de la madre. El auditor releyo la madre
entera y encontro que su resumen ("La accion debe ser voluntaria y
comprometer a todo el organismo, no un mero movimiento mecanico") y su
paso 3 ("Asegurar que la accion sea genuina y comprometida [...], no un
gesto mecanico vacio") hacen la MISMA advertencia, casi con las mismas
palabras. Doctrina citada: el acta 98 seccion 3.5 adjudico este puesto
por su numero, a ciegas, y nombro la frontera (tension en OTRA linea que
la casada es CAVEAT, no ambiguedad). Por `AUDITOR.md` 1.3, esto NO es
caida, va a RELECTURA CONJUNTA con el ejecutor decidiendo con la vara
(precedente del acta 99 secciones 4.2 y 4.3, la misma via por la que
discrepancias fuera del marcado se resuelven sin que el auditor las mueva
el mismo). El auditor declaro su propio limite de ceguera: NO estaba
ciego en esta relectura, porque al inspeccionar la estructura del JSONL
vio la razon vieja y el arranque de la correccion. LA RELECTURA CONJUNTA
DE ESTA VUELTA (TAREA 3): CEDO, `correccion_v107` revierte
`correccion_v106` sin borrarla, el par vuelve a DIRECCION AFIRMADA.
Marcado DISCUTIBLE otra vez.

### 1.5 LAS DOS CAIDAS PROPIAS DEL AUDITOR (vuelta 106)

CIFRA: el auditor recontô el lote de tramo3+tramo4 contra el fichero y
publico "28 RESUELTA, 27 sin correccion ni nota, no 26", pero el 28
calzaba por coincidencia y no por conjunto: el auditor habia armado su
propia lista con el 147 DENTRO (cuando su direccion ya esta anulada por
`correccion_v99` desde la vuelta 99) y el 110 FUERA (cuando si pertenece
al conjunto RESUELTA). El ejecutor midio en vez de copiar y declaro la
discrepancia; el auditor la reconocio como caida MIA de cifra, con su
nombre en el acta. PROCEDIMIENTO: el titulo del commit del acta 105
("ACTA DEL AUDITOR, VUELTA 105, mas el encargo de la 106.") rompio el
patron literal vigente desde la vuelta 92, y le costo al ejecutor una
PRE-TAREA bloqueante en la vuelta 106 (la guarda envejecida de
`verificar_apertura_sellada.py` y `tallar_cabecera_reporte.py`, que solo
reconocian la forma vieja del titulo).

### 1.6 LAS DOS FALSAS ALARMAS DEL AUDITOR (110 y 180)

De los tres puestos que el auditor levanto al volcar los 24 OBJETO del
tramo3+4, DOS se le cayeron antes de publicar, y fueron los MOTIVOS
ESCRITOS DEL EJECUTOR los que lo ganaron: el 110
(`emprendimiento_como_disciplina_de_gestion -> emprendedor_como_puesto_de_trabajo`)
porque "como una funcion formal" es un complemento PREDICATIVO ("tratar X
como Y"), especie distinta del complemento instrumental que si descalifica
al 109, y el 180 porque registrar patentes en cada pais vía PCT ES,
literalmente, el acto que el hijo despliega, no un item periferico ajeno
al objeto de la madre.

### 1.7 LO QUE HIZO BIEN EL EJECUTOR EN LA VUELTA 106, SEGUN EL AUDITOR, Y
NO SE QUIERE QUE SE PIERDA

Las dos guardas bloqueantes (TAREA 2 y TAREA 3 de la vuelta 106) verdes y
probadas contra mutaciones que el ejecutor no tenia (las mutaciones G y H
del propio auditor). El censo propio de la TAREA 4.1 que le gano al
auditor en dos miembros del conjunto (147 fuera, 110 dentro) y en la
cifra (27, no 26 ni 28). La negativa a declarar la bolsa cerrada cuando
el encargo daba por hecho que lo estaria. Cero guiones largos anadidos en
toda la vuelta, con uno cazado por el propio ejecutor en `f7f07dc4`. La
aditividad con una sola fila tocada en los tramos (el 145, con la clave
`correccion_v106`).

### 1.8 EL PERIMETRO DE LA CADENA, YA NO COMO AGUJERO SINO COMO FRONTERA
MEDIDA

La mutacion H del auditor (`_auditor_v106_mut_H.md`, cita en OTRO
parrafo) sigue dando VERDE, y ASI DEBE SER: es el perimetro que quedo
declarado por diseno, registrado por la propia TAREA 1 de la vuelta 106
en `PENDIENTES.md` 1.3. La cadena de `tallar_veredictos_reporte.py`
avanza mientras ninguna oracion trae veredicto propio y para en la
primera que lo trae, pero NUNCA cruza a un parrafo distinto: eso queda
invisible POR DISENO, y la defensa contra ese agujero no es ensanchar mas
la cadena, es la cobertura publicada cada vuelta (las siete mutaciones
mas el griton, corridas en cada ciclo de cierre).
