Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la vuelta 201 de la campana My Idea, en la rama `pasada-unica`,
FASE III. Lee `docs/loop/EJECUTOR.md` entero antes de empezar y corre tu bloque de
apertura sellado ANTES de la primera operacion, como siempre.

**LA 201 NO ES VUELTA DE BATERIA.** La 200 lo fue y cerro entera: once tramos, 135 de
135 entradas, salida unica de 92570 bytes, 34.2 minutos. Por la cadencia de
`AUDITOR.md` 6.1 la bateria vuelve **cada cinco vueltas**, o sea que aqui **no corre**:
tu seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO** por su carril, con su medicion,
su atribucion y su corrida, como en las vueltas intermedias.

**RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): **no fabricas arneses, guardas
ni lectores nuevos**, y esta vuelta **no tiene ninguna excepcion**. La nomina sigue
**CONGELADA EN 135**: ni crece ni se poda. **El trabajo es EL PLAN**, que es para lo que
el bucle existe.

**EL TOPE DE SUB-TAREAS VUELVE A CINCO Y NO ES UN CAPRICHO MIO.** `AUDITOR.md` 6.2
apagaba el regimen temporal de dos sub-tareas cuando **dos vueltas seguidas cerraran su
propio reporte con `cerrar_reporte.py`**. Corri `vuelta192_racha_de_cierres.py` sobre el
inventario entero y **la racha vale 2: la 199 y la 200**. **Este encargo trae CUATRO.**

**LAS DOS PARADAS QUE LA 200 LEVANTO NO SON PARADAS, Y NO LAS ARREGLAS.** Mi acta 200
las adjudica en su `4.1` y su `4.2`: el rojo de los once tramos es **FALSO ROJO DE
CENSO** (la nomina congelada gana a la guarda, por el acta 185 punto 6.2 y la jerarquia
de `AUDITOR.md` 0) y el bloque `F` de `vuelta185_tarea1c_mutacion_bateria_continuada.py`
es **un arnes cuya PREMISA envejecio**, no una guarda muerta. **Las dos reparaciones son
de codigo y van a la auditoria integral: la moratoria las prohibe hoy.** No las toques
y no las vuelvas a levantar como paradas.

---

## TAREA 1: LOS REGISTROS. BLOQUEANTE.

**1.a** El **acta 200** entra en la serie con el numero que devuelve
`scripts/loop/serie_de_registros.py`, **computado y no tecleado** (hoy el siguiente libre
es `R.61`, pero **lo vuelves a correr y usas lo que diga**). Su cuerpo se acota con
`grep -n` EN ESTA VUELTA, no con las cifras de este encargo. **No escribas ningun lector
nuevo:** la moratoria lo prohibe y los que hay bastan.

**1.b** **LA ENTRADA DE LA VUELTA 198, POR LA ADJUDICACION `4.7` DE MI ACTA.** La 198
sigue **sin entrada propia en la serie y sin reporte archivado**, medido por mi hoy:
`docs/loop/reportes/REPORTE_V198.md` **no existe**. Escribe su entrada de serie
**DECLARANDO LA AUSENCIA**: que su reporte no se archivo, que **no se reconstruye**, y
con que instrumento lo mediste. **NO FABRIQUES EL REPORTE.** El ejecutor de la 200 hizo
bien en no inventarselo y esa decision se mantiene: lo que se registra es el hueco, con
su medicion, no un texto que nadie escribio.

**1.c** **UNA CORRECCION DE CITA, DE UNA LINEA, EN SU SEDE.** La seccion 8 de
`docs/loop/reportes/REPORTE_V200.md` (o sea el reporte de la 200 una vez que lo archives)
sostiene la PARADA `1` diciendo que *`AUDITOR.md` 0* dice que cuando una guarda
contradice una decision escrita del fundador, la que se corrige es la guarda. **Esas
palabras no estan en `AUDITOR.md`**: son del **acta 185, punto 6.2**, derivadas de la
jerarquia que `AUDITOR.md` 0 si establece. **Lo verifique con `grep` sobre los dos
ficheros.** **No es caida y no se cobra**: es la forma en que la casa lo cita desde el
acta 185. Anade el aviso de una linea con la cita entera, **con el texto viejo entero y
sin tachar**, por el carril del banco `9.10` mas `EJECUTOR.md` 8. Banco `9.5.0`, LA REGLA
SE CITA, NO SE PARAFRASEA.

## TAREA 2: LA CORRECCION DECLARADA DE LA EVIDENCIA DE `OP-I-01`.

**Adjudicada por el acta 199 en su `4.1`, y la cadencia de la bateria la aparto de la
200. NO ES PARADA y no hace falta decidir nada nuevo.**

La ficha de `OP-I-01` promete **323** entradas y `docs/plan/INVENTARIO.jsonl` tiene
**672**. La cifra vieja **no es una mentira**: viaja con su fecha de corte. Lo que
envejecio es la evidencia. Escribe la **CORRECCION DECLARADA en su sede**, con el texto
viejo entero y sin tachar, y **las dos cifras con su fecha de corte cada una** (banco
`9.21`, TODA CIFRA DE CRUCE LLEVA SU FECHA DE CORTE).

**NO SE TECLEA NINGUNA DE LAS DOS.** El 672 se recuenta del fichero EN ESTA VUELTA y se
pega su salida; el 323 se lee de la ficha y se cita por linea. **Y publicas el reparto
por tipo recontado hoy**, no el de mi acta ni el del acta 199.

**NINGUN CAMPO `estado` SE MUEVE.** La vara del trabajo pendiente es el instrumento,
nunca el campo `estado` (recuadro de `AUDITOR.md` 0, decision del fundador del 4 sep).

## TAREA 3: LA MEDICION DE `OP-L-02` CONTRA SU `verificacion`, NO CONTRA SU `evidencia`.

**Adjudicada por el acta 199 en su `4.2`.**

`OP-L-02` es la unica de las cuatro fichas reales **SIN DOCUMENTO QUE MEDIR**: corri
`vuelta150_3_relectura_expediente.py --corte d60facd0` hoy y su evidencia entera es
prosa, con **0 menciones de fichero**. Por eso **se mide contra su campo `verificacion`
y no contra su `evidencia`**, que es lo que la adjudicacion dice.

Lee la ficha entera, **cita su `verificacion` por linea**, y responde con medicion: **que
pide exactamente, que parte de eso se puede comprobar hoy contra el repo, y que parte
no**. Si la conclusion es que su `verificacion` tampoco alcanza para ejecutarla sin
decidir, **eso es un hallazgo medido y se escribe como tal**: no la improvises y no la
declares hecha. Una operacion cuyo texto no alcanza para ejecutarse sin decidir **es
PARADA, no una improvisacion** (`AUDITOR.md` 3), y si llegas ahi, paras y la traes.

## TAREA 4: LAS OTRAS DOS FICHAS REALES, `OP-L-01` Y `OP-L-03`, LEIDAS CONTRA SU VARA.

**Es el trabajo que la moratoria `6.3` manda: EL PLAN HASTA AGOTARLO, las cuatro fichas
reales.** Las cuatro salen de la vara corrida por mi hoy con exitcode 0: **71 fichas, 37
que no calzan, 6 en LISTA sin ninguna prueba, 4 de TRABAJO REAL y 2 CONSUMIDAS**. Las
cuatro reales son `OP-L-01`, `OP-L-02`, `OP-L-03` y `OP-I-01`, **las cuatro de tipo
MESA**. La 2 y la 3 se llevan `OP-I-01` y `OP-L-02`; aqui van las otras dos.

**LO PRIMERO, Y NO TE LO SALTES: vuelve a correr la vara TU MISMO** con el corte de tu
vuelta y **publica sus cifras de hoy**. Si discrepan de las mias, **la discrepancia se
declara, no se resuelve copiando** (`AUDITOR.md` 1.1, EL INSTRUMENTO MANDA).

Para `OP-L-01` y `OP-L-03`: la vara dice que **sus documentos SI existen en disco**
(`LECTURAS_DIRIGIDAS.md`, `INTRA_DOMINIO_INFORME.md`, `BANCO_DE_TEXTOS.md` y
`BANCO_DEL_PLAN.md`), y dice tambien, con todas sus letras, que **que el documento este
NO significa que su mesa se hiciera bien**: si cubre lo que la ficha describe **es
LECTURA, y esa vara no la hace**. **Hazla tu.** Por cada una: cita su `verificacion` por
linea, mide sus documentos (bytes exactos en disco y LF, `P.2`), y **di si el documento
cubre lo que la ficha describe, con la cita que lo sostenga o con el hueco nombrado**.

**NO MUEVAS NINGUN `estado`** y **no cierres ninguna ficha por tu cuenta**: lo que
produce esta tarea es **lectura medida**, y si de ella sale que una ficha esta cumplida,
**lo propones con su evidencia y lo adjudico yo**.

---

**LAS GUARDAS DE SIEMPRE, QUE NO SE AFLOJAN:** ciclo de Gate 0 **entero, sus cuatro
comandos** (correr `run_phase1.py` a secas recompila el grafo, revierte 71 etiquetas
curadas y da un rojo que no es del repo: me paso a mi en esta vuelta y al auditor de la
199 en la suya); suites en verde; `dataset/`, `web/`, `engine/` y `docs/plan/` medidos
con `numstat` al entrar y al salir y **las dos cifras publicadas**; el `sha256` de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` **abre y cierra en el mismo valor** (hoy
`0a77b5a35a962621`, y lo remides tu); **ninguna clase y ningun veredicto se mueven**,
porque mover una clase es del RECOMPUTO; y **los tamanos van en BYTES EXACTOS** leidos
del instrumento, nunca redondeados, con los KB solo entre parentesis y detras (`P.2`).

**CIERRA TU PROPIO REPORTE con `scripts/loop/cerrar_reporte.py`.** La racha vale 2 y de
ella depende que el tope de sub-tareas siga en cinco.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.
