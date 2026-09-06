
# ACTA DEL AUDITOR, VUELTA 191 (6 sep 2026, auditor Opus 5)
# Cubre LA VUELTA 190 ENTERA. Prefijo de mis ficheros: `_auditor_v191_*`, libre y
# sin tomar. Mi sello es `SELLO_APERTURA_AUDITOR_V191.json`.
# =========================================================================

**LA CABECERA DE UNA LINEA: LA VUELTA 190 REPRODUJO ENTERA BAJO MI MANO Y NO LE
ENCUENTRO NI UNA CIFRA FALSA NI UNA RUTA VACIA. GATE 0 VERDE ENTERO CORRIDO POR
MI, MARCADOR RECOMPUTADO DEL ARCHIVO (3.388, A 551, B 72, C 5, D 2.760, CERO
HUECOS Y CERO DUPLICADOS, `sha256` LF `0a77b5a35a962621`), CABECERA RECOMPUTADA
(3.853 / 3.169 / 684, ARISTAS 8.780 / 8.740 / 17.520 / 9.914) Y LAS 24 FILAS DE
PAREJAS DE BYTES DEL REPORTE CALZAN LAS 24 CONTRA EL DISCO, `sha256` Y LINEAS
INCLUIDOS. NO ELEGI MUESTRA FRESCA: RELEI A CIEGAS LOS MISMOS 30 PUESTOS QUE EL
EJECUTOR, Y ESA ES LA NOVEDAD DE ESTA ACTA. ME SALEN 21 COINCIDENCIAS Y 9
DISCREPANCIAS, LAS NUEVE DENTRO DE MIS DUDOSOS, Y LAS TREINTA SE RESUELVEN A
FAVOR DEL ARCHIVO. Y LA MEDICION QUE TRAIGO: OCHO DE LOS TREINTA TUMBAN A LOS DOS
LECTORES INDEPENDIENTES, Y NINGUNO DE LOS OCHO LLEVA LA MARCA `DISCUTIBLE
MARCADO` QUE 427 FILAS DEL ARCHIVO SI LLEVAN. ADJUDICO LOS SEIS DISCUTIBLES, LOS
SEIS A FAVOR, Y CONTESTO LAS TRES PREGUNTAS. UNA CAIDA PROPIA MIA, DE METODO, Y
CERO DEL EJECUTOR QUE ACUMULEN.**

## 0. HUECO DE ACTA: NO LO HAY, Y LO MIDO

La ultima acta escrita es la **190** y su cabecera dice que cubre **la vuelta
189**. La vuelta que audito es la **190**, inmediatamente anterior a esta.
**Cero vueltas sin acta.** Medido con `grep -n "^# ACTA DEL AUDITOR"
docs/loop/ACTA_AUDITOR.md`, que da la 190 en la linea 67092 como ultima.

## 1. LA APERTURA, SELLADA ANTES DE MI PRIMER COMANDO DE VERIFICACION

`scripts/loop/apertura_del_auditor.py` corrio **PRIMERO Y SOLO ESO**, con
`--vuelta 191` y `--puestos` de treinta numeros. **`PUEDE SELLAR: SI`, `bitacora
del turno hasta ahora: (vacia)`, `prohibidos tocados antes del sello: 0`,
`VEREDICTO: VERDE`.** El sello vive en
`docs/loop/SELLO_APERTURA_AUDITOR_V191.json` (**1003 bytes**) y nombra la ciega
(**39924 bytes**, `sha256` `03f7984f105d189b`) y el destape (**32062 bytes**,
`sha256` `42e02b2c068f3c26`). **Solo despues** toque `git log`, `git status` y
`REPORTE.md`, los tres por sus funciones del propio fichero, que apuntan su
toque: `docs/loop/_auditor_v191_apertura_toques.txt`.

**Y ESCRIBI MIS CLASES ANTES DE LEER EL REPORTE, NO SOLO ANTES DEL DESTAPE.**
`docs/loop/_auditor_v191_mis_clases.txt` quedo commiteado en **`a446a3b7`**, y mi
primer toque de `REPORTE.md` es posterior a ese commit. **El orden es la prueba y
esta en git**, no en mi palabra.

## 2. LO QUE VERIFIQUE, CON MI COMANDO Y NO CON SU PALABRA

| lo que el reporte dice | lo que mi instrumento mide | |
|---|---|---|
| marcador 3.388, A 551, B 72, C 5, D 2.760, 0 huecos, 0 duplicados | identico, recomputado del archivo | CALZA |
| `sha256` LF del archivo `0a77b5a35a962621` | `0a77b5a35a962621339d58a1eeda9afc046cbff9f42dc6dbbaf16aa627aae372` | CALZA |
| censo 3.853 / 3.169 / 684 | identico, contado del grafo | CALZA |
| aristas 8.780 / 8.740 / 17.520 / 9.914 | identico | CALZA |
| Gate 0 OK, motor 25/25, `tsc` 0, web 82 / 1.040, `numstat` 0 | identico, ciclo entero corrido por mi: `docs/loop/_auditor_v191_gate0.txt` | CALZA |
| las 24 filas de tabla con pareja de bytes | las 24 calzan en disco, LF, lineas y `sha256`: `docs/loop/_auditor_v191_parejas.txt` | CALZA |
| `R.52` de 18764 bytes, 198 lineas por `count(NL)` y 199 por `split`, 0 guiones | identico, medido de su cabecera a fin de fichero. **Mi primer corte dio 18761 y era MI delimitacion, no su cifra: lo digo porque el criterio manda declarar la discrepancia y no taparla** | CALZA |
| la serie cierra en 44 entradas, 0 colisiones, 0 huecos, mayor `R.52` | identico, `serie_de_registros.py` corrido por mi | CALZA |
| nomina 127, `arneses_que_faltan()` 0, `nomina_invisible_al_censo()` 0 | identico, corrido por mi | CALZA |
| la tarea 2 cierra en `ROJO POR DEUDA DECLARADA`, exitcode 2, 3 con motivo y 0 sin | identico, re corrido por mi: exitcode 2 | CALZA |
| los tres arneses de mutacion salen VERDE con 0 mutaciones sin caer | RE CORRIDOS POR MI: los tres exit 0 y sus salidas byte a byte iguales (6763, 7489, 6373) | CALZA |
| el registrador es idempotente | RE CORRIDO POR MI sin `--mutacion`: `NO SE ESCRIBE NADA`, `PENDIENTES.md` sigue en 980013 bytes | CALZA |
| el lanzador da 10 tramos, 127 entradas, y `--siguiente` dice el tramo 1 | identico, corrido por mi | CALZA |
| `evitar` de 441 puestos de sus cuatro ficheros, solape 0 con el tramo y con el universo | identico: union 441, solape 0 y 0, y el **2422 SI esta dentro** de la ciega del acta 189b | CALZA |
| el cotejo del ejecutor: 30 releidos, 20 coinciden, 10 discrepan, 9 dentro y 1 fuera, reparto A 7 B 3 D 20 | identico, contado de `SALIDA_V190_T4_COTEJO.txt`, y **el del archivo A 7, B 1, D 22 lo recompute yo del archivo** | CALZA |
| `OP-L-02` vive en la linea 42 y su clave es `id_op` | identico | CALZA |
| la vara: 71 fichas, 37 que no calzan, 6 en LISTA sin prueba, 2 consumidas, 4 de trabajo real, 3 mesas con documento, `OP-L-02` la unica sin documento | identico, corrida por mi con `--corte 25f2c047` | CALZA |
| el reporte archivado es identico byte a byte al vivo | los dos 68540 bytes, 983 lineas, `sha256` LF `7a74fc3ccd11b769` | CALZA |
| una sola `## 9.` | `grep` da 1, y `## 10.` da 0 | CALZA |
| el sello del auditor 765 bytes, ciega 41948, destape 37856 | identico | CALZA |

**LAS RUTAS QUE EL REPORTE PUBLICA:** barri los **94** nombres de fichero
citados. **CERO miden cero bytes** y **91 existen tal cual**. De las tres que no
resuelven solas: **dos son abreviaturas** y existen con bytes
(`scripts/run_phase1.py`, 75698, y
`docs/loop/paradas/2026-09-05-la-bateria-sin-techo-DECISION.md`, 1905); **y la
tercera es `docs/loop/SALIDA_V190_BATERIA.txt`, que el propio reporte declara
inexistente en su seccion 9**, con el nombre, el cero medido y su atribucion, que
es lo que la letra del hueco declarado exige. **Ninguna promete prueba sobre un
vacio.**

## 3. LA RELECTURA CIEGA, Y ESTA VEZ NO ES UNA MUESTRA FRESCA

**ELEGI SOLAPE TOTAL A PROPOSITO.** `AUDITOR.md` 1.2 manda empezar por los
discutibles marcados del reporte, y el tramo donde el ejecutor declara **diez
discrepancias y una fuera de sus dudosos** es el tramo con menos credito de la
campana. Relei **los mismos 30 puestos**, a ciegas y sin ver ni su destape ni sus
clases ni el reporte. **Lo compre con cobertura:** esos 30 no son cobertura nueva,
y la cuenta de puestos de la seccion 7 lo dice con esas palabras.

**21 COINCIDEN, 9 DISCREPAN, Y LAS NUEVE CAEN DENTRO DE MIS DOCE DUDOSOS
MARCADOS.** Mi reparto fue A 9, B 6, D 15; el del archivo, recomputado por mi, es
A 7, B 1, D 22. **Las nueve se resuelven a favor del archivo**, y las razones que
me tumban son medidas y no retoricas: el **1366** con cuatro de cinco pasos
correspondidos y sus perdidas repartidas por lado; el **1201** cerrando un racimo
en estrella con su cuenta periferica completa; el **2423** separando la linea de
su procedimiento con la arista que falta y su direccion.

**EL CREDITO DE MI TANDA NO BAJA:** cero discrepancias fuera del marcado.

## 4. LAS ADJUDICACIONES

**4.1 `D.1`, ampliar la guarda por una funcion hermana en vez de cambiarle la
firma. A FAVOR, Y LO COMPROBE EN EL CODIGO ANTES DE DECIRLO.** El encargo pide que
la guarda *"SEPARE EN SU SALIDA"*, y eso es lo que entrega. Lo que decide el caso
no es la lectura del encargo sino que **la hermana LLAMA a la original en vez de
copiar su logica** (`verificar_mutaciones_viejas.py`, linea 1397: su primer bucle
es sobre `guarda_del_sujeto_congelado(...)`), y su docstring **garantiza que la
suma de las tres listas es exactamente lo que devuelve la original**. **No hay dos
fuentes de verdad, hay una y un refinamiento encima.** Cambiarle la firma a una
funcion que tres arneses viejos llaman habria roto tres guardas para conseguir lo
mismo.

**4.2 `D.2`, la vara del `MOTIVO ESCRITO` escrita por el ejecutor porque el
encargo no la da. A FAVOR.** Lo que la salva no es que sea razonable, es **cuando
se escribio**: antes de medir y publicada en la simulacion previa. Una vara
escrita despues de ver las tres entradas se ajusta sola a lo que convenga, y esa
es la especie que la casa persigue. **Su fragilidad la declara el propio ejecutor
y la confirmo:** una vara mas estrecha sacaria las tres como `SIN MOTIVO`. Queda
escrita en el instrumento con su fecha, que es donde se puede discutir.

**4.3 `D.3`, el exitcode de la deuda es `2`. A FAVOR.** La `4.4` del acta 190 pide
dos cosas y las dos se cumplen: que el codigo **separe** y que **los dos rojos
sigan siendo distintos de cero**. Que numero exacto sea no lo fija ninguna regla y
no hace falta que lo fije.

**4.4 `D.4`, `SUJETO VIVO` cuenta como FALLO y no como DEUDA. A FAVOR.** Un arnes
que abre el fichero de hoy sin nada que lo module **mide el dia y no su maquina**:
eso es guarda rota, y llamarla deuda declarada seria la degradacion silenciosa del
banco 9 hecha por el lado amable. **Hoy esa lista esta en 0**, asi que no mueve
ninguna cifra de esta vuelta y decide como se leeran las proximas, que es
exactamente cuando conviene decidirlo.

**4.5 `D.5`, la tarea 4 no se auto encarga su relectura al doble. A FAVOR, Y LA
ENCARGO YO EN ESTA MISMA ACTA.** `AUDITOR.md` 1.2 pone el doble en mi mano, no en
la suya, y **LA ESCALADA SE ENCARGA, NO SOLO SE DECLARA** es una regla contra MI,
no contra el ejecutor. **Traerla medida, con su nombre y su cifra, fue lo
correcto; declararla y no encargarla habria sido caida mia.** Va como TAREA 2
bloqueante.

**4.6 `D.6`, no darle sede a `OP-L-02` pudiendo argumentarlo. A FAVOR, Y ADEMAS
ERA LO UNICO QUE PODIA HACER.** Declarar que una salida de vuelta en `docs/loop/`
cuenta como producto documental de una mesa **cambia el criterio de HECHO de la
fase 08**, y `AUDITOR.md` 4 reserva al fundador cambiar el alcance de la campana.
**No es que fuera prudente: es que no era suyo.**

**4.7 `P.1`, a `OP-L-02` le falta un documento o solo le falta que su `evidencia`
nombre los que existen. LA MITAD BARATA SE ADJUDICA, LA CARA NO SE TOCA.** Que el
campo `evidencia` **nombre los ficheros que ya existen** no cambia ningun estado
ni ningun alcance: es registrar lo medido, y la disciplina del dictado lo pide.
**Adjudicado: se puede y se debe.** Que eso **la haga HECHA** no lo adjudico yo por
lo dicho en la 4.6. **Y no es PARADA**, y digo por que: la ficha es de la fase 09,
no bloquea nada hoy, y la campana sigue con la mitad adjudicada puesta. **Su
estado no se mueve: sigue en `LISTA`.**

**4.8 `P.2`, la discrepancia del 3182 baja el credito de la tanda. ENCARGADA COMO
BLOQUEANTE.** Ver 4.5. **Y una precision que hace falta:** mi propia relectura de
esos mismos 30 **no es el doble y no lo sustituye**. Al doble es **mas extension**,
treinta vecinos nuevos; lo mio es **otro lector sobre la misma extension**. Son dos
controles distintos y hoy corren los dos.

**4.9 `P.3`, si el exitcode 2 debe propagarse a `--componer`. SI, POR EXTENSION
CITABLE Y SIN DOCTRINA NUEVA.** La `4.4` del acta 190 y el banco 9 dicen que un
unico codigo para dos especies de rojo es degradacion silenciosa. **Una
composicion que aplana los dos rojos que el tramo distinguio comete la misma falta
un piso mas arriba.** Adjudicado a favor. **No entra en esta vuelta y lo digo en
el encargo para que la 192 no lo redescubra.**

## 5. LO QUE TRAIGO YO, FUERA DE LO QUE EL REPORTE MARCA

**5.1 OCHO DE TREINTA TUMBAN A LOS DOS LECTORES, Y NINGUNO LLEVA LA MARCA QUE EL
ARCHIVO SI USA EN OTRAS 427 FILAS.** Es el hallazgo del solape total y no se podia
ver de otra manera. Dos lectores independientes, sin verse (mis clases estan
commiteadas antes de mi primer toque del reporte), discrepan del archivo **en los
mismos ocho puestos**: **872, 904, 963, 1201, 1366, 2423, 3067 y 3086**. Solo el
ejecutor discrepa en 648 y 3182; solo yo en 1812. **Y la medicion que importa:
`DISCUTIBLE MARCADO` aparece en 427 de las 3.388 filas del archivo, el 12,6 por
ciento, y en CERO de esos ocho.** El unico de los treinta que la lleva es el
**3182**, que tumbo a un lector y no al otro. **No digo que la marca este mal
puesta ni saco de ocho casos una ley:** digo que **la marca y la dificultad medida
no se estan tocando**, que la muestra es de treinta y que **eso se puede medir
sobre toda la historia de ciegas de la campana en vez de sobre mi tanda.**
Encargado como medicion, **sin tocar ni una razon del archivo**.

**5.2 EL VEREDICTO DE UNA LINEA DEL REPORTE SALE CON LA ETIQUETA DUPLICADA, Y ES
NUEVO DE ESTA VUELTA.** La linea 50 dice literalmente `**EL VEREDICTO DE UNA
LINEA: **EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS...`. La causa esta medida y
no supuesta: `cerrar_reporte.py` linea 1817 compone `"**EL VEREDICTO DE UNA
LINEA: %s**"`, y su propia salida (`SALIDA_V190_CERRAR_REPORTE.txt` linea 45)
prueba que **el veredicto que se le paso ya traia la etiqueta y los asteriscos**.
**Los cinco reportes anteriores (186 a 189) la traen UNA sola vez**, o sea que no
es herencia. **NO LA CUENTO COMO CAIDA DE REPORTE**, y lo razono en vez de
decidirlo a ojo: la caida de reporte es *una afirmacion equivocada*, y aqui no hay
afirmacion equivocada sino una etiqueta pegada dos veces. **Es un defecto del
cerrador**, de la misma especie que las dos convenciones de `lineas` del acta 190:
**el cerrador existe para cazar justo esto y no lo caza.** Encargado con su guarda.

**5.3 `git checkout --` NO ES RESTAURACION BYTE A BYTE EN ESTE REPO, Y ME MORDIO A
MI.** Re corriendo el instrumento de la nomina pise
`docs/loop/SALIDA_V190_T2_NOMINA.txt`, que es salida sellada de la 190. Lo restaure
con `git checkout --` y **el fichero volvio con 4587 bytes en disco en vez de los
4510 que el reporte publica**: `autocrlf` lo devuelve en CRLF. **Una restauracion
que cambia la cifra publicada no restaura nada.** Lo rehice leyendo el blob con
`git show` y escribiendolo en LF, y remedi: **4510 bytes, `sha256` LF
`82cc350f1dfbd694`, identico a lo publicado**, con `git diff --numstat` en cero
filas. **Esto le importa a la `4.9` del acta 190 que ya esta en codigo:** el
reporte dice que la restauracion de la bateria **va en LF**, y esta bien que lo
diga, porque la orden obvia habria dejado la cifra falsa. **Mi corte nuevo quedo al
lado con su nombre**, `docs/loop/_auditor_v191_nomina_corte_nuevo.txt`, que es lo
que la 4.9 manda.

## 6. LAS CAIDAS

**DEL EJECUTOR: CERO QUE ACUMULEN.** Declara tres (`5.1`, la cifra de su bloque
`H.7` cierta y enganosa por buscar la clave equivocada; `5.2`, su arnes con salida
que cambiaba sola por el sufijo de `mkdtemp`; `5.3`, dos cifras tecleadas dentro
del arnes que escribio para cazar cifras tecleadas). **Las tres son DE METODO**,
las tres las declara con su cifra y **ninguna llego a publicarse como cifra
falsa**. **Cero caidas de clase, cero de cifra publicada, cero rutas vacias.** La
etiqueta duplicada de mi `5.2` no se la cuento a el: **la dejo pasar el cerrador.**

**MIAS: UNA, DE METODO, Y ES LA `5.3`.** Restaure una salida sellada con la orden
que parece la correcta y **no comprobe la cifra antes de darla por restaurada**;
la cace remidiendo, no por suerte, pero el orden correcto era medir primero.
**No repite ninguna caida propia de las actas 189 ni 190**, asi que **no abre
racha de las tres seguidas**. Selle antes de tocar nada, escribi mis clases antes
de leer el reporte, y el arbol queda sin ninguna fila de `numstat`.

## 7. LA METRICA DE CREDITO

| | esta vuelta | acumulado |
|---|---:|---:|
| relecturas | 1 | **326** |
| puestos | 30 aislados, **30 de solape TOTAL a proposito: control, NO cobertura nueva** | **1.006** |
| discrepancias DENTRO del marcado | **9** (las nueve en mis dudosos) | **42** |
| discrepancias y hallazgos FUERA del marcado | **3** (la marca contra la dificultad medida, la etiqueta duplicada, la restauracion que no restaura) | **151** |
| caidas propias del auditor | **1**, de metodo (`5.3`) | ninguna repetida: no abre racha |
| caidas del ejecutor que ACUMULAN por cifra publicada | **0** | **racha de cifra publicada: 0** |
| caidas del ejecutor de reporte | **0** | **racha de reporte: 0** |
| caidas del ejecutor de metodo, registradas y sin racha | **3** (`5.1`, `5.2`, `5.3` del reporte) | |

**CREDITO ROTO: NO. PARADA: NO**, y repase las condiciones una a una: ninguna
adjudicacion pidio doctrina nueva (la `4.7` parte la pregunta y adjudica solo la
mitad que una regla escrita cubre, y la `4.9` sale por extension citable del banco
9); no hay contradiccion con regla vigente ni con cifra publicada; nada de lo que
la casa reserva se toco y **la nomina no se podo** (127 y creciendo); Gate 0 no ha
estado en rojo ninguna vuelta; el credito de tanda no se rompio; la campana no
esta consumida y las credenciales no hicieron falta.

## 8. LO QUE ENCARGO A LA VUELTA 191

**NO ES VUELTA DE BATERIA**: la 189 la corrio entera y la siguiente cae en la
**194**. La seccion 9 del reporte cierra con el **hueco declarado y medido** por su
carril. **Van CINCO sub-tareas**, que es el tope vigente desde la `4.10` del acta
190, y **lo confirmo medido: CUATRO vueltas seguidas cerraron su propio reporte**
(187, 188, 189 y 190), una mas que las tres que el acta 190 conto. Quedan escritas
enteras en `docs/loop/PROMPT_SIGUIENTE.md`.
