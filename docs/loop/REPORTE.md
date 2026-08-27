# REPORTE DE LA VUELTA 96 (EJECUTOR)

Rama `pasada-unica`. Fase III, fase 04 ENLACES, modo de ejecucion continua.
Sobrescribe el reporte de la vuelta 95. Toda la identidad de esta cabecera
(rama, commit del acta, HEAD real de apertura) se lee de git y se talla, nunca se
teclea (`EJECUTOR.md` regla 1, "LA IDENTIDAD SE LEE DE GIT"): va en la ultima
fila de la tabla de abajo, salida entera del tallador.

**ESTA VUELTA REANUDA EL BUCLE tras la parada de la vuelta 95** (tercera caida de
reporte seguida), con la decision del fundador del 27 ago 2026 delante
(`docs/loop/paradas/2026-08-27-racha-parentesis-DECISION.md`, recogida en
`AUDITOR.md` seccion 4). Ejecuta el encargo entero de
`docs/loop/PROMPT_SIGUIENTE.md`: **TAREA 1** los cuatro registros del acta 95;
**TAREA 2** la mesa de formula de los pares 886, 890 y 947; **TAREA 3** el primer
tramo de lectura de `OP-E-03`, 40 pares de 183.

**LOS TRES RESULTADOS DE FONDO, al frente:** la etiqueta del grupo C queda
corregida con instrumento propio y con **una discrepancia declarada** contra el
acta; la mesa se sento entera y **NO HAY VARA CITABLE**, asi que los tres pares
quedan como estan y la duda va sellada, que es la rama que la propia decision del
fundador escribio; y `OP-E-03`, que llevaba desde la vuelta 94 con la bolsa
establecida y sin leer, **ya tiene su primer tramo leido**.

## CABECERA TALLADA (`--fase04 --vuelta 96`), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 96`.
Salida completa en `docs/loop/SALIDA_V96_CABECERA_TALLADA.txt`, **EXIT 0**.
Antes del commit de cierre se corre otra vez con
`--comparar docs/loop/REPORTE.md` sobre este mismo fichero ya escrito (seccion
"LA COMPARACION FINAL", mas abajo). **Ninguna celda de esta tabla esta tecleada.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `ea93d674` (ACTA DE LA VUELTA 95 DEL AUDITOR, leido de git log), HEAD real de apertura `f9c7bb77` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `ea93d674` (ACTA DE LA VUELTA 95 DEL AUDITOR, leido de git log), HEAD real de apertura `f9c7bb77` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE** |

**EL COMMIT DEL ACTA Y EL HEAD REAL DE APERTURA SON DISTINTOS ESTA VUELTA, y es
el caso para el que la fila se construyo.** El acta 95 es `ea93d674`; el HEAD real
cuando abri era `f9c7bb77`, el commit de la DECISION DEL FUNDADOR que entro entre
el acta y la primera tarea. El tallador compara los arboles de `dataset/` de los
dos commits y da **VERDE** porque coinciden, o sea que las cifras de apertura son
fiables para el commit que la fila nombra. **El sello se escribio en el PRIMER
commit de la vuelta** (`a9cc39ee`, cuyo padre es `f9c7bb77`), antes de tocar nada.

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION Y EL CIERRE SE RECOMPUTO AL
CIERRE**, las dos con corrida propia completa y ninguna heredada: ciclo de tres
(`run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py --aplicar`,
`sync_assets_web.py`), conteo de aristas, desfase, motor, web y tsc, en los dos
lados. **CERO ARISTAS SE MOVIERON**: `git diff --stat -- dataset/ web/lib/assets/`
corrido DESPUES de todas las mediciones de cierre da **CERO lineas**.

## EL MARCADOR Y LA TASA POR DOMINIO, REMEDIDOS ESTA VUELTA

**Y esta vez SI hay instrumento corrido en esta vuelta que los produzca**, que es
lo que faltaba en la 95. Comando: `python scripts/recomputar_marcador.py 3388`,
salida en `docs/loop/SALIDA_V96_MARCADOR_CRIBADO_CIERRE.txt`, EXIT 0. Cifras
leidas de ese fichero:

- `n = 3388 corte = 3388 huecos: [] dups(puesto): 0`, pares duplicados 0.
- **MARCADOR GLOBAL: A 551 (16,3) / B 72 (2,1) / C 5 (0,1) / D 2.760 (81,5).**
- **TASA POR DOMINIO:** compras 155/1 (0,6), core 1.445/325 (22,5), entrega
  171/2 (1,2), environmental 170/28 (16,5), exportacion 130/15 (11,5),
  franquicias 148/15 (10,1), health_safety 192/43 (22,4), quality 844/119 (14,1),
  risk_management 106/0 (0,0), seguridad_digital 27/3 (11,1).

**NI EL MARCADOR NI LA TASA SE MUEVEN POR NADA DE ESTA VUELTA, y esta verificado
y no supuesto:** `git diff --stat f9c7bb77 -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl
docs/INTRA_DOMINIO_PARES.jsonl` da **vacio**. Los 40 veredictos de la TAREA 3 son
**LECTURA DIRIGIDA** y viven en fichero propio
(`docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl`), **fuera de la cola y fuera de la
tasa por dominio del banco 9.27**, como manda el punto 5 de
`OP-E-03.verificacion`.

**El fichero se llama `..._MARCADOR_CRIBADO_CIERRE.txt` y no `..._MARCADOR_CIERRE.txt`
a proposito**, misma convencion que la vuelta 94: la fila opcional del tallador
espera el formato viejo del cribado y este es el del recomputo, asi que se le
deja fuera en vez de darle un fichero que no sabe leer.

## TAREA 1: LOS REGISTROS DEL ACTA 95

Escritos en `docs/PENDIENTES.md`, seccion "VUELTA 96, TAREA 1". Composicion del
anadido **tallada, no contada a ojo**
(`docs/loop/SALIDA_V96_TAREA1_COMPOSICION.txt`): **1 seccion de nivel 2 y 4
subsecciones de nivel 3**, 5 filas casadas, con las dos enumeraciones nominales.

**(1.1) La caida de reporte de la vuelta 95, con la letra nueva al lado.**
`REPORTE.md` de la vuelta 95 linea 210 publicaba "`docs/PENDIENTES.md` (cinco
secciones nuevas)" y eran **CUATRO**. **No se remide**, por mandato expreso del
encargo ("ya viene medida"): la medicion es la del auditor,
`docs/loop/_auditor_v95_pendientes_tallado.txt`. **Vive en una LISTA DE RUTAS**,
asi que por la letra afinada del fundador **se registra, se relee al doble, y NO
acumula para la racha.**

**(1.2) Las dos caidas propias del auditor, cada una con su nombre y verificadas
hoy.** (i) El SyntaxWarning que **nunca existio**: `git log` sobre
`scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py` da **un solo commit**
(`d1d88d1a`) y ese commit ya abre con la cadena cruda. El ejecutor de la vuelta
95 gasto tres vias en desmentirlo y **tenia razon**. (ii) La omision que mando el
1844 a la mesa: la linea **32693** del acta (dos filas encima de la 32695 que el
auditor si cito) ya lo resolvia. **El 1844 QUEDA** y la relectura conjunta baja de
cuatro a **TRES**.

**(1.3) La etiqueta del grupo C, corregida sin borrar la vieja, Y CON UNA
DISCREPANCIA DECLARADA.** Instrumento propio de esta vuelta,
`scripts/loop/vuelta96_tarea1c_etiqueta_grupo_c.py`, salida en
`docs/loop/SALIDA_V96_TAREA1C_ETIQUETA_GRUPO_C.txt`, EXIT 0. La bolsa de 18 **no
se teclea**: se calcula importando `clasifica_razon()` del instrumento de la
vuelta 95. Cifras leidas de ese fichero:

| pregunta | cuantas de las 18 |
|---|---:|
| mencionan la palabra "linea" en cualquier forma | 9 |
| formula ESTRICTA "es/son UNA LINEA" (con determinante) | 6 |
| formula ANCHA "es/son ... LINEA" (con o sin determinante) | 7 |
| anclan con "en ... linea" y NO con "es/son" | 1 |
| NO mencionan la palabra "linea" | 9 |
| casan el patron A del acta 94 (tiene que ser 0) | 0 |

**El NUEVE del acta 95 calza al digito y con la misma enumeracion.** Su **OCHO
con la formula literal** no calza: mi estricta da **SEIS** y mi ancha **SIETE**.
**La discrepancia se declara, no se resuelve copiando** (`EJECUTOR.md` regla 2), y
esta nombrada par por par: el **909** es plural sin determinante (*"son lineas"*),
el **1086** dice *"en una sola linea"*, que **no es la formula "es/son"**, y el
**983** va tras dos puntos, cosa que el propio acta ya contaba aparte. **7 mas 1
mas 1 dan los 9: todo queda contado y nada sobra.** La CONCLUSION del auditor
sigue en pie y esta medida; lo que se corrige es la ETIQUETA.

**Mecanica de rojo probada por mutacion** (`docs/loop/SALIDA_V96_TAREA1C_MUTACION.txt`,
EXIT 0): dos guardas **CAEN** al mutarlas, control verde antes y despues, **y la
tercera se DECLARA sin caso rojo automatico** por ser tautologia, en vez de
fabricarle uno que se apruebe solo.

**(1.4) Las seis adjudicaciones del acta 95** (4.1 a 4.6), cada una con su linea
leida hoy con `grep -n '^### '`, y con su efecto sobre el trabajo.

## TAREA 2: LA MESA DE FORMULA. NO HAY VARA CITABLE

Registrada entera en `docs/PENDIENTES.md`, seccion "VUELTA 96, TAREA 2".
Composicion tallada (`docs/loop/SALIDA_V96_TAREA2_COMPOSICION.txt`): **1 seccion
de nivel 2 y 6 de nivel 3**, 7 filas casadas.

**(a) Los cinco ejemplares, impresos enteros y juntos.**
`scripts/loop/vuelta96_tarea2_mesa_de_formula.py` a
`docs/loop/SALIDA_V96_TAREA2_MESA_DE_FORMULA.txt`, **152 lineas** contadas del
fichero con `wc -l`, EXIT 0: razon COMPLETA de cada uno y `pasos_accionables`
ENTEROS de los diez nodos, con los ids **resueltos por el resolutor antes de
cruzarse** (`P.1`; ninguno de los diez cambio al resolverse, y se dice porque
`P.1` obliga a declararlo siempre).

**(b) y (c) La vara candidata se escribio de doctrina ya escrita y se probo ANTES
de usarse.** Sale entera de dos textos citados literalmente: banco **9.6.2**
(*"el hijo CABE ENTERO DENTRO DE UN PASO DE LA MADRE"*) y
**`OP-E-07.verificacion`** (*"NO SE RELEE EL PAR: se lee su razon"*). Se corrio
contra las adjudicaciones que el expediente YA publico
(`docs/loop/SALIDA_V96_TAREA2_VARA.txt`, EXIT 0), cifras leidas de ese fichero:

**EXPEDIENTE: 19 filas. CALZAN 16. CHOCAN 3: los puestos 1886, 1844 y 1009.**

**Una vara que tumba lo ya adjudicado no separa nada: reordena. NO ES CITABLE.**

**Y las tres chocan por LA MISMA RAIZ, que es el hallazgo de la mesa.** El 1886 y
el 1844 fueron adjudicados QUEDA **leyendo los PASOS DE LOS NODOS** (acta 93,
*"encaje limpio dentro del paso 1"*; lectura ciega del acta 95, *"ancla en su paso
2"*), mientras el 1009 y el 1098 cayeron **leyendo la RAZON**, que es el carril
que la operacion manda. **Los dos carriles dan respuestas opuestas sobre razones
de la MISMA FORMA**, y el ejemplar esta impreso: la razon del 1844
(*"X NOMBRA EL PROBLEMA: ... Y TRAE EL PROCEDIMIENTO"*) tiene la misma forma que
la del 1009 (*"X prueba el problema: ... Y trae un procedimiento que esa fase no
tiene"*), y sus veredictos son opuestos. **Ningun patron sobre el texto puede
separar dos frases con la misma forma.** El 1009 ademas trae un ordinal de fase en
su razon (*"en la fase I"*) que pertenece **al hijo**, no a la madre, y una regex
no sabe de quien es la fase.

**(d) La segunda vara posible, la que SI los separaria, se dice entera en vez de
callarla.** Si se leyera el PAR en vez de la RAZON (el test de `9.6.2` sobre los
`pasos_accionables` de hoy), los cinco se separarian, y en `PENDIENTES.md` esta la
lectura par por par que lo muestra. **No se aplica por dos razones escritas y
ninguna mia:** `OP-E-07.verificacion` manda literalmente el carril contrario, y la
**DERIVA DE CONTENIDO ya medida** lo haria poco fiable (de los 140 nodos de la
operacion, **26** tienen hoy pasos distintos de los del encendido, y afecta a
**32** de 87 pares; el ejemplar es el nodo de esta misma mesa,
`fit_problema_solucion`, que tenia **6** pasos y hoy tiene **3**, con el bloque de
traccion que las razones del 886 y del 1009 citan como lo valioso del par **ya
fuera del nodo**). Ampliar el carril **ya estaba declarado RESERVA DE FUNDADOR**.

**(e) LO QUE SE DECIDE.** Por la decision 2 del fundador, literal (*"si no hay
vara citable, los tres quedan como estan y la duda va sellada a PENDIENTES"*):
**el 886, el 890 y el 947 QUEDAN COMO ESTAN.** Ninguna arista se toca, **ninguna
cifra del plan ni del marcador se mueve por esta mesa**, y la relectura conjunta
queda **CERRADA SIN RETIRADAS**.

**CORRECCION DECLARADA, sin borrar el texto viejo:** la frase del acta 95
(seccion 4.2) *"Ninguna vara escrita hoy discrimina entre ellos"* queda
**RATIFICADA y ahora MEDIDA**, no solo afirmada. Lo que se corrige es su alcance:
era impresion y hoy es una medicion con fichero.

**Mecanica probada por mutacion** (`docs/loop/SALIDA_V96_TAREA2_MUTACION.txt`,
EXIT 0): la comparacion **no es tautologia en ninguna de las dos direcciones**
(mutacion A1, un par que hoy CALZA pasa a CHOCAR; mutacion A2, uno que hoy CHOCA
pasa a CALZAR), mas dos mecanicas de ROJO que **CAEN**, y control verde antes y
despues.

## TAREA 3: `OP-E-03` EMPIEZA A LEERSE, 40 DE 183

Registrada entera en `docs/PENDIENTES.md`, seccion "VUELTA 96, TAREA 3", con el
addendum en `docs/plan/OPERACIONES.jsonl` y el apartado hermano en
`docs/plan/04_ENLACES.md`. Composicion tallada
(`docs/loop/SALIDA_V96_TAREA3_COMPOSICION.txt`): **1 seccion de nivel 2 y 6 de
nivel 3**, 7 filas casadas.

**Los cinco puntos de `OP-E-03.verificacion` se cumplen, y los tres medibles se
REMIDIERON en la vuelta en vez de heredarse:** cribado cerrado (`INTRA_DOMINIO_PARES.jsonl`
y `INTRA_DOMINIO_VEREDICTOS.jsonl`, **3.388 filas cada uno**, contadas por el
instrumento); **ids por el RESOLUTOR antes de cruzar nada** (`P.1`, y en estas 40
el resolutor no movio ninguno, lo cual se declara porque `P.1` lo obliga); cuenta
sin fugas (**cero** de las 40 esta en la cola tras resolver contra los **2.796**
pares distintos de la cola, cero repetidas dentro del tramo); marca **LECTURA
DIRIGIDA** escrita en cada fila y en cada fila del JSONL; y veredictos contados
**APARTE de la tasa por dominio**, en fichero propio.

Material impreso entero en `docs/loop/SALIDA_V96_TAREA3_TRAMO1_MATERIAL.txt`,
**1.368 lineas** contadas con `wc -l`, EXIT 0. Cifras del resultado leidas de
`docs/loop/SALIDA_V96_TAREA3_VEREDICTOS.txt`:

| clase | que significa | cuantas de 40 |
|---|---|---:|
| A | REPITE (lo que anade cabe en una linea) | 1 |
| B | DUDOSO (la vara no lo resuelve sola) | 1 |
| C | figura aparte | 0 |
| D | CONTINUA (trae procedimiento que el otro no tiene) | 38 |

| direccion (banco 9.6.2) | cuantas |
|---|---:|
| LEIDA y afirmada | 29 |
| NO RESUELTA, declarada como tal | 11 |

| dominio | pares | A | B | C | D |
|---|---:|---:|---:|---:|---:|
| core | 20 | 0 | 1 | 0 | 19 |
| environmental | 2 | 0 | 0 | 0 | 2 |
| franquicias | 2 | 0 | 0 | 0 | 2 |
| health_safety | 2 | 1 | 0 | 0 | 1 |
| quality | 14 | 0 | 0 | 0 | 14 |

**ESTA TABLA POR DOMINIO NO ENTRA EN LA TASA DEL BANCO 9.27** y va rotulada asi en
su propio fichero de salida.

El unico **A** es el par 12 (`human_error_como_sintoma` contra
`preguntar_que_no_quien`, misma fuente Dekker: lo unico que anade cabe en una
linea). El unico **B** es el par 23, **declarado DUDOSO en vez de forzado**. Las
once direcciones no resueltas llevan cada una su motivo escrito, y tres de ellas
son el caso 2.195 que el propio `9.6.2` nombra (no hay madre e hijo en absoluto).

**Y el par 16 sale con la DIRECCION INVERTIDA respecto a la etiqueta de la
bolsa**, que es exactamente el error que el banco `9.6.2` nace para evitar: el
flujo de ventas es la madre y el guion de nueve pasos de la primera llamada cabe
entero dentro de su paso 1.

**SEIS FIGURAS que la lectura destapa** (enteras en `PENDIENTES.md`), cuatro de
ellas sospechas de gemelos **entre nodos**, que es justo lo que la nota de la
operacion prometia (*"EL BARRIDO CALIBRADO ES TAMBIEN UN DETECTOR DE GEMELOS"*):
el trio Make Certain, los dos Customer Development, los dos de estrategia de
innovacion (uno haciendo de madre y otro de hijo, la forma que mas cuesta ver), y
la familia de la capacidad de proceso, que **corrobora desde otro camino** un
aviso informativo del Gate 0 de esta misma vuelta (`capacidad_de_proceso` contra
`capacidad_del_proceso`, 97,6 de similitud de titulo). Mas una propiedad del
barrido que conviene tener escrita **antes** de leer los 143 que quedan: **puede
casar un paso con su propia refutacion** (par 32, el AQL de Juran contra la
critica al AQL de Crosby).

**SEIS guardas probadas por mutacion y las seis CAEN**
(`docs/loop/SALIDA_V96_TAREA3_MUTACION.txt`, EXIT 0), incluida la que sostiene la
adjudicacion del 11 ago 2026 de esta operacion (un par que ya esta en la cola).
**Y se DECLARA lo que no se prueba:** la clase de cada par es tabla a mano y **NO
tiene caso rojo automatico**, en vez de fabricarle uno que se apruebe solo.

**CERO ARISTAS ESCRITAS O RETIRADAS.** `OP-E-03` es LECTURA DIRIGIDA y su producto
es el juicio, no el cableado. **Quedan 143 sin leer**, filas 41 a 183; el
instrumento ya acepta `--desde 40 --cuantos 40` sin tocar codigo.

El addendum se escribio **por script y no a mano**
(`scripts/loop/vuelta96_tarea3_addendum_opE03.py`, con `--simular` antes de
`--aplicar`, las dos salidas commiteadas): sus cifras se LEEN del fichero de
lectura. Resultado medido: **una sola linea** de `OPERACIONES.jsonl` cambia y
`04_ENLACES.md` es **puramente aditivo** (28 lineas anadidas, 0 borradas). La
guarda de idempotencia se probo **en vivo**: la segunda corrida da ROJO y no
escribe.

## LAS RACHAS, CON LA LETRA NUEVA DELANTE

- **CLASE O CIFRA PUBLICADA: CERO.** Ninguna cifra de `docs/plan/` ni del banco
  quedo sin su corte esta vuelta, y ningun veredicto se movio.
- **REPORTE QUE ACUMULA: CERO.** La caida de la vuelta 95 **se registra y NO
  acumula**, por letra expresa de la decision del fundador del 27 ago 2026, que la
  nombra por su caso (vivia en una lista de rutas). Se releyo al doble su tramo.

## PENDIENTES DE DOCTRINA

**UNO nuevo**, registrado en `docs/PENDIENTES.md` seccion "VUELTA 96, TAREA 2",
apartado (f), y **NO es parada** (`EJECUTOR.md` regla 5: se registra lo mejor
sostenido y se sigue):

> Cuando la lectura ciega del auditor (`AUDITOR.md` seccion 1.2, que **manda**
> imprimir primero los pasos de los nodos y adjudicar sobre ellos) y el criterio
> de verificacion de la operacion (`OP-E-07.verificacion`, que **manda** decidir
> por la razon y no releer el par) apuntan a lados distintos, **cual manda**. Las
> dos reglas estan vigentes y el expediente tiene adjudicaciones publicadas de las
> dos clases. **Lo mejor sostenido mientras tanto:** cada operacion decide por SU
> propio criterio escrito, y la lectura ciega sigue siendo control de calidad de
> la clase, no fuente de direccion. Es lo que ya se hace de hecho; lo que falta es
> que este escrito.

## RUTAS TOCADAS (commits `a9cc39ee` a `c1873af3`)

**Talladas, no tecleadas** (`EJECUTOR.md` regla 1, "LA TABLA SE CUENTA DE SU
FICHERO"): `git diff --name-status f9c7bb77 HEAD` a
`docs/loop/SALIDA_V96_RUTAS_TOCADAS.txt`, contado con
`scripts/loop/tallar_composicion_salida.py` a
`docs/loop/SALIDA_V96_RUTAS_COMPOSICION.txt`, EXIT 0:

| clase | filas |
|---|---:|
| fichero NUEVO (A) | 33 |
| fichero MODIFICADO (M) | 3 |

**Los TRES modificados, enumerados por el instrumento:** `docs/PENDIENTES.md`,
`docs/plan/04_ENLACES.md`, `docs/plan/OPERACIONES.jsonl`. Los 33 nuevos son nueve
instrumentos en `scripts/loop/`, el fichero de lectura
`docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl`, y 23 salidas `docs/loop/SALIDA_V96_*`.
**CERO ficheros de `dataset/`, `web/` o `engine/` tocados**, verificado por
`git diff --stat` vacio, citado arriba.

**El conteo cubre hasta `c1873af3`**, o sea las tres tareas; los ficheros de
CIERRE (`SALIDA_V96_*_CIERRE.txt`, la cabecera tallada, las rutas tocadas y este
reporte) entran en el commit de cierre y por eso no estan en esa cuenta. **Se dice
en vez de dejar que la cifra parezca cubrirlo todo.**

## LA COMPARACION FINAL

`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 96 --comparar
docs/loop/REPORTE.md`, corrido DESPUES de escribir este fichero y ANTES del commit
de cierre; su salida se pega en el mensaje del commit de cierre y se guarda en
`docs/loop/SALIDA_V96_COMPARAR_CIERRE.txt`.

## LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

Marcados **antes** de saber si acierto.

1. **EL VEREDICTO DE LA MESA DESCANSA EN MI ELECCION DE FAMILIAS DE ANCLA
   (TAREA 2).** Declaro que no hay vara citable porque una vara de trece familias
   contradice tres adjudicaciones. **Otro conjunto de familias podria reproducir
   las diecinueve.** No lo ensanche despues de ver cuales fallaban, a proposito,
   porque eso seria afinar a la respuesta; pero **la eleccion inicial es mia**, y
   si el auditor construye una vara que las reproduzca todas, mi conclusion cae.
   **Es el discutible mas grande de la vuelta.**
2. **EL PAR 26 DE LA TAREA 3 (`rol_gates_agile` contra
   `gates_go_kill_decision_points`) LO LLAME D Y ESTA CERCA DE A.** Mismo libro
   (Cooper) y **`titulo_ratio` 91,7** segun la senal del barrido, leida de la
   linea 850 de `docs/loop/SALIDA_V96_TAREA3_TRAMO1_MATERIAL.txt`. Lo sostuve
   en D porque lo que anade `rol_gates_agile` son **tres instrucciones operativas**
   (revisar recursos, no separar hardware y software, cronograma estable), no una
   linea. **Si el auditor lee esas tres como una sola idea, el par es A.**
3. **LAS ONCE DIRECCIONES NO RESUELTAS DE LA TAREA 3.** El umbral entre "el hijo
   hace algo ADYACENTE al paso" y "el hijo ejecuta el paso" **lo puse yo**. Con un
   umbral mas laxo, varias de las once (11, 22, 35, 36, 37) tendrian direccion
   afirmada. Preferi no afirmarla, pero **once de cuarenta es mucho** y merece que
   se mire si estoy siendo demasiado estricto.
4. **LA DIRECCION INVERTIDA DEL PAR 16.** La afirmo **contra la etiqueta de la
   bolsa**, que es una afirmacion fuerte hecha sobre un solo par. Si me equivoco,
   he invertido una direccion buena.
5. **MI DISCREPANCIA CON EL "OCHO" DEL ACTA 95 (TAREA 1.3).** Mi regex de formula
   estricta da seis y la ancha siete. **Es posible que el auditor usara "formula
   literal" en un sentido mas suelto** que el mio y que su ocho sea correcto bajo
   su propia definicion. Declaro la discrepancia sin decidir quien tiene razon
   sobre la palabra "literal"; lo que si sostengo es la enumeracion par por par.
6. **EL PAR 23 CLASIFICADO B.** La frontera entre "mas que una linea" y "menos que
   un procedimiento" es exactamente donde vive la clase B, y **es mi juicio**. Un
   lector estricto lo pondria en A (el paso 3 del hijo ES el paso 2 de la madre) y
   uno laxo en D. Traigo la duda en vez de resolverla.
