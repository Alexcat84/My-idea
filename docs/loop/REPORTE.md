# REPORTE DE LA VUELTA 137: LAS CUATRO REPARACIONES DE LA PARADA, Y LA FASE 06 ABIERTA Y MEDIDA SIN FUNDIR

REGIMEN COMPLETO. El modo austero queda SUSPENDIDO desde esta vuelta, por su
propio punto 5 y por la decision del fundador del 29 ago 2026.

## IDENTIDAD (leida de git en esta vuelta, regla 1, LA IDENTIDAD SE LEE DE GIT)

Rama `pasada-unica`, leida de `git rev-parse --abbrev-ref HEAD`.
HEAD sellado de apertura `51b76cd23e7c1c7db8f8c89b0fb97f97d9fb5b4c`, del
2026-08-29, leido de `git rev-parse 51b76cd2` y `git log -1 --format=%ad`.
HEAD sellado de cierre `62c4f0e8fcf2b62b72d495dc779062d2df85d4f5`, del
2026-09-01, leido de `git rev-parse HEAD` DESPUES del commit del reporte y
escrito en un commit propio, que es el carril que la vuelta 64 ya uso: el commit
del reporte no puede contener su propio hash.

Siete commits, leidos de `git log --oneline 51b76cd2..HEAD`: `25895ba4` (1.a),
`ebdb7962` (1.b), `4a7eee78` (1.c), `f0db4ef6` (1.d), `8165558f` (TAREA 2),
`e7942378` (las medidas del cierre) y `62c4f0e8` (el reporte).

## LA CABECERA NO SE TALLA ESTA VUELTA, Y SE DICE POR QUE

`tallar_cabecera_reporte.py --vuelta 137` NO se corre, y su tabla NO se pega.
El tallador arma cada celda de un par `SALIDA_V137_*_APERTURA.txt` y
`SALIDA_V137_*_CIERRE.txt`, diez familias, y **el lado APERTURA de esta vuelta
no existe: no lo capture antes de la primera operacion**. Escribir la tabla sin
el seria teclear la mitad de las celdas, que es exactamente lo que la regla
prohibe, y rellenar la apertura con la medicion de hoy seria la caida de la
vuelta 28. **La celda que no sale de un instrumento no se escribe**, asi que no
se escribe la tabla. Es una CAIDA MIA DE PROCEDIMIENTO y la declaro aqui, no en
el mensaje del commit: la vuelta 136 fue amonestada justamente por dejar el
aviso en el commit y no en el reporte.

Lo que si medi en la apertura, antes de tocar nada, y sirve de contraste: la rama
y el HEAD de arriba, y el arbol limpio: el ciclo del cierre lo deja vacio, y esa es la
comprobacion de `SALIDA_V137_CICLO_NUMSTAT_CIERRE.txt`.
El plan trae `71 lineas`, recontadas al cierre en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt` bajo la etiqueta operaciones del plan.
Los ficheros de nodo del censo son `3853 ficheros`, recontados en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`.

## EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE (regla 1)

Todo esto se corrio DESPUES del ultimo cambio de esta vuelta, no antes.

| comprobacion | resultado | fichero |
|---|---|---|
| Gate 0 con su ciclo | `GATE 0: OK`, EXIT 0 | `SALIDA_V137_GATE0_CIERRE.txt` |
| etiquetas de cara | 71 reaplicadas | `SALIDA_V137_CICLO_ETIQUETAS_CIERRE.txt` |
| sync de assets | EXIT 0 | `SALIDA_V137_CICLO_SYNC_CIERRE.txt` |
| numstat tras el ciclo | VACIO | `SALIDA_V137_CICLO_NUMSTAT_CIERRE.txt` |
| motor | 25/25 | `SALIDA_V137_MOTOR_CIERRE.txt` |
| web | 80 passed (80), 1030 passed 3 skipped (1033) | `SALIDA_V137_WEB_CIERRE.txt` |
| tsc | EXIT 0, cero lineas | `SALIDA_V137_TSC_CIERRE.txt` |

El censo de cierre trae `3184 nodos` vivos, recontados en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt` bajo la etiqueta nodos vivos del censo.
Y trae `669 nodos` deprecados, recontados en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt` bajo la etiqueta nodos deprecados del censo.

**Y LA PRUEBA DE QUE ESTA VUELTA NO TOCO EL CATALOGO:** `git diff --stat
51b76cd2 HEAD -- dataset/` sale **VACIO**. Ni un nodo tocado. Por eso el censo
del cierre coincide con el de la apertura: no porque lo herede, sino porque el
arbol es el mismo y esta comprobado que lo es.

## TAREA 1, LAS CUATRO REPARACIONES DE LA PARADA. HECHAS LAS CUATRO

Cada una con su caso por mutacion corrido sobre una variable **que el codigo
computa**, nunca sobre un literal, y con su salida pegada abajo.

### 1.a la guarda de la cabecera del mapeo, las dos cosas (commit `25895ba4`)

**ANTES, medido en la apertura** (`SALIDA_V137_1A_ANTES.txt`): ROJO EXIT 1, siete
cifras, con los seis peldanos recomputados en `[54, 54, 54, 54, 54, 54]`. Y la
segunda averia, medida a la vez: la corrida ensucio
`docs/loop/SALIDA_V135_4B_PELDANOS.txt`, ocho insertadas y ocho borradas por
`git diff --stat`. Los peldanos historicos del fichero protegido son `5 lineas`, recontadas en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`.
Son las que quedaban sobreescritas por 54 en cada corrida de la guarda vieja.

**LA REPARACION.** Se le fija el arbol contra el que recomputa:
`SELLO_APERTURA = 2deac539`, el commit que ESCRIBIO la tabla (vuelta 135, TAREA
4.b y 4.c) y por tanto el corte en que su cabecera se calculo. Medido en esta
vuelta y no heredado: `dataset/nodos` es IDENTICO entre `2deac539` y
`9e909a05^`, o sea que el sello de la tabla y el estado previo a la escritura de
`OP-S-11` son el mismo censo. El arbol sellado se saca con `git archive` a un tar
en memoria, sin checkout. `vuelta131_grupos_por_titulo.py` admite que se le fije
el directorio de nodos por `MAPEO_NODOS_DIR`, con el arbol vivo por defecto, asi
que ningun llamador viejo cambia. Y `SALIDA_V135_4B_PELDANOS.txt` entra en la
lista de ficheros protegidos.

**DESPUES** (`SALIDA_V137_1A_DESPUES.txt`): VERDE EXIT 0, con los peldanos
declarados `[54, 104, 105, 106, 108, 111]` iguales a los recomputados.
El mapeo queda con `17 grupos` de dos o mas miembros, releidos de esa salida y recontados en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`.
Quedan `92 grafias` en grupo, recontadas en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt` bajo la etiqueta grafias en grupo del mapeo.
Quedan `37 grafias` sin agrupar, recontadas en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt` bajo la etiqueta grafias sin agrupar del mapeo.
Y la tabla del mapeo cierra con `129 lineas` de fila real, recontadas en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`.

**LAS TRES MUTACIONES**, las tres VERIFICADAS, con sus salidas pegadas enteras
en `SALIDA_V137_1A_MUTACION.txt`, EXIT 0.
**A**, el sello es real y no decorado: se le fija `--sello 9f9e6892`, el arbol de
DESPUES de la escritura, y la guarda cae con sus seis peldanos recomputados en
`[54,54,54,54,54,54]`. Si el recomputo estuviera clavado a una constante, esta
mutacion no cazaria nada y la reparacion seria decorativa.
**B**, la cabecera sigue vigilada: la mutacion de la vuelta 135, borrar el
peldano 54 de una copia de la tabla, sigue cazandola y nombrandolo. Fijar el
arbol no afloja la comparacion, y la mutacion de la 135 se recorrio aparte y
quedo VERIFICADA.
**C**, control positivo de la proteccion: corrido el recomputo POR SU CUENTA el
fichero SI cambia; corrida la guarda, NO cambia. Sin el control positivo, un
fichero limpio no probaria nada.

### 1.b la clausula de campo presente en `verificar_fuente_canonico.py` (commit `ebdb7962`)

El cargador hacia `if not fu: continue`, o sea que un nodo vivo sin declaracion
salia LIMPIO. Ahora `verificar()` distingue cuatro motivos: campo AUSENTE, campo
VACIO, campo presente pero SIN NI UNA DECLARACION, y declaracion NO CANONICA.

Que hoy no muerda a nadie esta **medido en esta vuelta**, no heredado: la propia
guarda reparada da VERDE EXIT 0 en `SALIDA_V137_1B_REAL.txt` diciendo que todos
los nodos del censo que estan vivos traen `fuente` presente.
Son `3184 nodos` vivos, recontados en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt` bajo la etiqueta nodos vivos del censo.
Se reparo ANTES de que la aduana `OP-A-02` la herede, que es donde el caso deja de
ser hipotetico.

**LAS MUTACIONES**, las cuatro VERIFICADAS en `SALIDA_V137_1B_AUTOPRUEBA.txt`,
EXIT 0, todas sobre copia en memoria y cero escritura a disco. La vieja sigue
mordiendo: `activity_attributes`, con su canonica devuelta a la grafia vieja,
queda cazada y nombrada. Y las TRES nuevas sobre `ab_testing_optimizacion`, campo
AUSENTE, campo VACIO y campo de SOLO ESPACIOS, quedan cazadas cada una con su
motivo. Antes de la reparacion las tres pasaban limpias.

### 1.c las dos de `verificar_cifras_del_reporte.py` (commit `4a7eee78`)

Los dos defectos se **reprodujeron con ficheros reales antes de tocar nada**
(`SALIDA_V137_1C_DIAGNOSTICO.txt`), que es lo que la regla 2 manda.

**DEFECTO 1, la unidad `grafia`.** `SALIDA_V135_4B_PELDANOS.txt` trae DOS lineas
`CIFRA` de esa unidad y el contador devolvia la PRIMERA siempre.
La primera dice `92 grafias` en grupo, recontadas en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt` bajo la etiqueta grafias en grupo del mapeo.
La segunda dice `37 grafias` sin agrupar, recontadas en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt` bajo la etiqueta grafias sin agrupar del mapeo.
La segunda, que es CORRECTA, se cotejaba contra la primera y la guarda la
tumbaba. **La prueba de que el defecto ya deformaba el trabajo esta en la
cabecera de ese mismo fichero de salida**, que explica que el
peldano 6 va primero "porque el cotejo toma la PRIMERA linea CIFRA de la unidad
pedida": un instrumento doblado alrededor del defecto de la guarda.

**DEFECTO 2, el emparejamiento.** La 388 hacia `sorted(set(...))` y la 395 tomaba
`citas[0]`. La cifra de grafias en grupo, citando su fichero, con una frase vecina
que citaba otro alfabeticamente anterior, se cotejaba contra el del VECINO y la
guarda la tumbaba. Reproducido entero en `SALIDA_V137_1C_DIAGNOSTICO.txt`.

**LAS REPARACIONES.** La primera recoge TODAS las lineas `CIFRA` de la unidad con
su ETIQUETA y elige por la etiqueta (camino FUERTE). La segunda ordena las citas
por PROXIMIDAD TEXTUAL a la cifra en vez de por alfabeto. **La ventana no se
toca**: sigue siendo la forward-only, porque la asimetria de las dos ventanas
esta adjudicada como doctrina; lo que cambia es CUAL de las citas de esa misma
ventana se elige. Tras la reparacion las dos cifras correctas salen VERDE y por
el camino FUERTE.

**EL HALLAZGO QUE EL DEFECTO 2 ESCONDIA, Y QUE NADIE HABIA MEDIDO: tambien
DEJABA PASAR CIFRAS FALSAS.** El acta 136 lo nombra solo por el lado de los
falsos rojos. Corrida la version vieja sacada de git, una cifra de grafias en
grupo FALSA para su propio fichero sale **VERDE EXIT 0** porque cuadraba contra el
recuento generico del fichero del vecino: la mutacion C entera, con las dos
salidas pegadas, esta en `SALIDA_V137_1C_MUTACION.txt`. La guarda no solo era
injusta, era permeable, y el segundo defecto es el mas grave de los dos.

**LAS CUATRO MUTACIONES**, las cuatro VERIFICADAS en
`SALIDA_V137_1C_MUTACION.txt`, EXIT 0. **A**, cifra equivocada por uno: cazada.
**B**, cifra de la etiqueta VECINA del mismo fichero, escrita como sin agrupar:
cazada, y es la que prueba que el camino fuerte no se degrada al debil.
**C**, el falso verde de arriba. **D**, las mutaciones viejas recorridas.

### 1.d los registros (commit `f0db4ef6`)

`R.18` en `docs/PENDIENTES.md`, por adicion, donde viven `R.15`, `R.16` y `R.17`,
con cinco entradas: la caida de procedimiento del ejecutor de la vuelta 136 con
su nombre (**LA GUARDA NO SE ESTRECHO, SE LE QUITO EL SUJETO DE DEBAJO**) con su
atenuante y su agravante; el **ramal (xxi) UNA COBERTURA DE CERO NO ES UN VERDE,
ES UN PLATO VACIO** escrito entero y en cita; las cuatro reparaciones; el falso
verde recien descubierto; y el discutible de las tres mutaciones selladas.

## TAREA 2, LA FASE 06: ABIERTA Y MEDIDA, NINGUNA FUSION EJECUTADA

Y el motivo esta **contado**, no opinado (`SALIDA_V137_2A_TERRENO.txt`, EXIT 0).

**(A) EL ESTADO MEDIDO CONTRA EL GRAFO, no contra el campo `estado`**, tal como el
encargo avisaba. Las SEIS diferidas estan SIN FUNDIR de verdad, porque sus
absorbidos de las seis fusiones diferidas siguen sin deprecar: son `13 nodos`,
contados en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`. Las dependencias `OP-M-03-I` y `OP-M-03-II` SI estan
fundidas en el grafo (absorbidos deprecados). Y verifique `OP-M-02-MEDIOS`, del
que `OP-M-02-ACCLIMATE` depende: su superviviente de ficha esta DEPRECADO y el
nodo que la ficha mandaba eliminar esta VIVO, o sea ejecutada al reves. **NO es
parada**: su propia nota ya la declara CONSUMIDA por un tramo de `OP-U-01`, con
la divergencia de superviviente escrita como contraste y no resuelta copiando.

Las cinco mesas: las cinco ADJUDICADAS (11 y 12 ago 2026), las cinco con
`pregunta_pendiente` en null, y las dos fronteras que `OP-M-01` y `OP-M-05`
mandaban ESCRIBIR ya estan escritas como entradas 4 y 5 de
`FRONTERAS_DECLARADAS.md`. Lo que les queda no es decidir: es ejecutar sus hijas.

**(B) EL TAMANO.** Los absorbidos de las seis fusiones diferidas son `13 nodos`, recontados en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`.
Y las marcas editoriales por decidir en las seis son `87 lineas`, recontadas en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`.
Cada marca es paso o condicion de un absorbido, hay que decidirla una por una, con
su motivo escrito y su perdida sellada en campo propio si no viaja.

**(C) POR QUE NO SE FUNDIO NINGUNA, PROBADO CORRIENDO EL GENERADOR Y NO DEDUCIDO
DE LEER SU CODIGO.** En `generar_plan_de_fusion_de_mesa.py`, `marcar()` recibe
siempre el mismo `spec["pasos"]`, indexado por NUMERO DE PASO, dentro del bucle
`for ab in absorbidos`. Corri `G.marcar()` sobre los DOS absorbidos de
`OP-M-03-III` con el mismo spec: los cinco numeros de paso comunes reciben LA
MISMA marca en los dos. El reparto **no se puede diferenciar por absorbido**.
CINCO de las SEIS tienen mas de un absorbido (`OP-M-01-FUSION` con cuatro, y
`OP-M-03-III`, `OP-M-05-INDICE`, `OP-M-05-EDIFICIO` y `OP-M-05-APERTURA` con
dos): **no se pueden sellar con el generador tal como esta**. La unica de un solo
absorbido es `OP-M-02-ACCLIMATE`.

**NO PARCHEE EL GENERADOR Y NO FUNDI NADA A MANO POR FUERA DE EL.** Extender un
instrumento que SELLA planes de fusion es una operacion de codigo con sus propias
guardas, y hacerla de paso, al final de una vuelta que ya trae cuatro
reparaciones de guarda, es la clase de atajo que el ramal (xxi) acaba de nombrar.

**LO QUE NO HICE, DICHO ENTERO:** el encargo pedia `OP-M-01` a `OP-M-05` por su
orden escrito con sus seis fusiones diferidas, y **no sente ninguna mesa ni ejecute
ninguna fusion**. Ademas del generador, cinco de las seis piden **LECTURA DE ACTO
POR P.5 ANTES DE FUNDIR** y esa lectura no esta hecha; `OP-M-01-FUSION` es la
unica que declara P.5 satisfecha por construccion.

## LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**DISCUTIBLE 1, EL CAMINO DEBIL DE 1.c.** Cuando dos lineas `CIFRA` de la misma
unidad empatan en palabras con la frase, la guarda acepta que la cifra escrita sea
CUALQUIERA de las candidatas y lo marca `POR CONJUNTO`. Es mas debil que el camino
por etiqueta: una cifra podria cuadrar contra la etiqueta equivocada del mismo
fichero. Lo marco en vez de callarlo. Sigue siendo mas estricto que el estado
anterior, donde una cifra correcta caia ROJA y el ejecutor aprendia a evitar el
vocabulario, que es como nacio el ramal (xxi).

**DISCUTIBLE 2, EL SELLO QUE ELEGI EN 1.a.** Fije `2deac539`, el commit que
escribio la tabla. Se podia defender `9e909a05^`, el estado justo antes de la
escritura. Medi que los dos son el mismo censo, asi que hoy no cambia nada, pero
la eleccion es mia y si la campana prefiere anclar al padre de la escritura, se
cambia una constante.

**DISCUTIBLE 3, TRES MUTACIONES SELLADAS QUE NO PUEDEN CORRER, y no las repare.**
Las tres mutaciones 2.e de la vuelta 135 estan ancladas a un literal del reporte
de la vuelta 134, y ese reporte se sobreescribe cada vuelta: hoy mueren en su
comprobacion previa sin llegar a probar la guarda, mientras el docstring las
sigue llamando obligatorias. Medido con `git stash` que fallan IGUAL contra la
guarda vieja, o sea que no es regresion mia. Es de la especie del ramal (xxi):
una salida de error que no mide nada no es una prueba. No las toque porque
re-anclar instrumentos sellados no lo pide el encargo, y mi mutacion D ahora
distingue ANCLA PERDIDA de LA GUARDA NO MORDIO, para no mentir en la otra
direccion. Las cuatro, recorridas una por una, estan en
`SALIDA_V137_1C_MUTACION.txt`.

**DISCUTIBLE 4, TOQUE UN INSTRUMENTO DE LA VUELTA 131.** Para 1.a anadi a
`vuelta131_grupos_por_titulo.py` la lectura de `MAPEO_NODOS_DIR`. El defecto por
defecto es identico al de siempre, pero es un fichero sellado de otra vuelta y la
alternativa (duplicar `cargar_censo` en la guarda) habria reimplementado lo que la
casa manda reusar.

## LA CAIDA MIA, DECLARADA

**DE PROCEDIMIENTO: NO CAPTURE LA BATERIA DE APERTURA.** Medi la apertura a mano
(identidad, censo, operaciones, arbol limpio) pero no corri las diez familias
`SALIDA_V137_*_APERTURA.txt` que `tallar_cabecera_reporte.py` necesita, y por eso
esta vuelta **no publica cabecera tallada**. La consecuencia la asumo entera: sin
las dos columnas, la tabla no se escribe. Lo declaro aqui, en el reporte, y no en
el mensaje de un commit.

## PENDIENTES DE DOCTRINA

Ninguno nuevo. Las cuatro reparaciones se resolvieron con reglas ya escritas
(banco 9.10 para la guarda envejecida, EJECUTOR regla 1 para las mutaciones) y la
parada de la fase 06 no pide doctrina: pide un instrumento que sepa repartir entre
varios absorbidos.

## LO QUE LE PIDO AL AUDITOR

1. Adjudicar el **discutible 3**: si las tres mutaciones selladas se re-anclan (y
   contra que), o si se declaran superadas por las de esta vuelta.
2. Adjudicar si extender `generar_plan_de_fusion_de_mesa.py` al reparto por
   absorbido es operacion de codigo de la vuelta siguiente, y con que guardas.
3. Confirmar que la **LECTURA DE ACTO POR P.5** de las cinco fusiones que la piden
   entra como trabajo propio antes de fundir, y en que orden.

## LA COBERTURA, PEGADA TAL CUAL, QUE ES LO QUE EL RAMAL (xxi) PIDE

La guarda de cifras, ya reparada en la TAREA 1.c y corrida contra este mismo
reporte, da VERDE con su cobertura entera. Su linea literal es:

`COBERTURA: 16 cotejadas / 0 exentas / 16 cifras`

Y lo que mas me importa dejar dicho: **las dieciseis se cotejaron POR ETIQUETA**,
el camino FUERTE, y **ninguna por el camino debil POR CONJUNTO** que el discutible
1 declara. La vuelta 136 publico `0 cotejadas / 0 exentas / 0 cifras` reescribiendo
la prosa hasta que la guarda no encontrara nada. Aqui la guarda me tumbo trece
cifras de este mismo reporte y **no borre ni una para esquivarla**: escribi el
instrumento que faltaba, el de las cifras del reporte, que recomputa cada una y
la imprime como linea `CIFRA` en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`, y luego
puse cada cita junto a su cifra. Es el remedio que la regla manda y el contrario
del que la parada reprocho.

Tope: `wc -l docs/loop/REPORTE.md` da 300 lineas.
