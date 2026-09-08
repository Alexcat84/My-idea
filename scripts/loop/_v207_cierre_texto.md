## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CELDA DE ESTA SECCION SE TECLEO.** Cada tabla dice de que fichero de
salida sale y se reconstruyo contando ese fichero antes de publicarla
(`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO).

### 3.0 LO QUE SUBE PRIMERO, PORQUE ES LO MAS CARO QUE ENCONTRE

**NO ES UNA PARADA.** No contradice ninguna regla vigente ni ninguna cifra
publicada con su corte: es un hallazgo de instrumento, y lo dejo medido para que
el auditor decida. Van dos, en orden de coste.

**`3.0.a` LA VARA DEL `4.1` DEL ACTA 202 NO ALCANZA SOBRE UN ACTA MODERNA, Y
CUATRO DE SUS CINCO NUMERALES SALEN VACIOS O APUNTANDO A OTRA SECCION.** La vara
se escribio para actas ANTERIORES a la 184. El acta 206 es POSTERIOR y escribe
sus claves con comillas inversas, que es justo lo que el lector heredado pide, y
aun asi:

| numeral | lo que la VARA da | lo que hay, medido | la causa, leida del codigo |
|---|---|---|---|
| adjudicaciones | **0**, sobre la seccion **5** | **8**, `6.1` a `6.8`, seccion **6** | `MARCAS["adjudicaciones"]` es `("ADJUDICACIONES", "LA ADJUDICACION")` y casa con la seccion 5, *"LA ADJUDICACION 5.3 DEL ACTA 205 ES FALSA"*, que es una correccion y no la seccion de adjudicaciones. La real se titula `LO QUE ADJUDICO` |
| caidas propias del auditor | (ninguna seccion) | **3**, `C.1` a `C.3`, seccion **9** | sus marcas son `MIS CAIDAS PROPIAS` y `MIS PROPIAS CAIDAS`; el acta titula `MIS CAIDAS, CON SU NOMBRE` |
| caidas del ejecutor | **0** por las TRES formas | **2**, `E.1` y `E.2`, seccion **4** | la seccion SI se encuentra, pero sus claves son `E.n` y las tres formas miran `4.M`, `CAIDA n` y el lead en negrita |
| preguntas | **0**, y ademas *"la seccion de PREGUNTAS aparece 0 veces"* | **3**, `P.1` a `P.3` | el patron de `preguntas_del_reporte()` exige la palabra pegada al numero y el articulo `LAS` se lo rompe (acta 204 `4.4`, linea **196**) |
| hallazgos | **4** | **4**, `7.1` a `7.4` | calza, y es el unico de los cinco que calza |

**LO QUE ESTO CUESTA, DICHO SIN ADORNARLO:** el numeral de adjudicaciones no sale
0 por casualidad, sale 0 **contando bien una seccion equivocada**, que es la
especie de cero mas cara que hay: no se parece a un fallo. **Si una vuelta
publicara ese 0 sin mirar, el registro diria que el acta 206 no adjudico nada, y
adjudico ocho cosas, tres de ellas cerrando pendientes.** No lo arreglo:
ensanchar `MARCAS` toca un lector, y eso es moratoria.

**`3.0.b` LA `TABLA VIVA DE LOS PUROS` NO LLEVA EL EFECTO DE LA MESA QUE LA
NOMBRA COMO SU EVIDENCIA.** Medido en la TAREA 2 y marcado como mi `D.1`:

| nomina | lo que la mesa declara que dejo | lo que la tabla lleva hoy | cierra |
|---|---|---|---|
| junta asesora | **6 de 6, cobertura COMPLETA** (`LECTURAS_DIRIGIDAS.md:290`) | **5** leidos de **6** posibles (`BANCO_DE_TEXTOS.md:961`) | **NO** |
| seleccion de canal | **10 de 10, cobertura COMPLETA** (`LECTURAS_DIRIGIDAS.md:291`) | **8** leidos de **15** posibles (`BANCO_DE_TEXTOS.md:965`) | **NO** |

**Y NO ES QUE LA TABLA SEA VIEJA:** su corte es **14 ago 2026**, al puesto
**1157**, **tres dias DESPUES** del `fecha_corte` de la ficha, que es
**2026-08-11**. Es posterior y aun asi no lo lleva.

### 3.1 LA TAREA 1, CONTADA DE SUS FICHEROS

**LAS CIFRAS DEL ACTA 206, REMEDIDAS POR MI**, con
`git show 3e523b74^:docs/loop/ACTA_AUDITOR.md | wc -c` y su pareja sin el acento
circunflejo. Las tres calzan al digito con el contraste del encargo: **4771842**
antes, **4793964** despues, **22122** anadidos. Y la adicion pura la mide `git`:
`git show --numstat 3e523b74` da **360** lineas anadidas y **0** borradas.

**LA SERIE DE REGISTROS, CORRIDA AL ENTRAR Y AL SALIR**, contada de
`docs/loop/SALIDA_V207_SERIE_APERTURA.txt` y
`docs/loop/SALIDA_V207_SERIE_CIERRE.txt`:

| punta | entradas | colisiones | huecos | mayor | siguiente libre |
|---|---:|---:|---:|---|---|
| AL ENTRAR | 62 | 0 | 0 | `R.70` | `R.71` |
| AL SALIR | 63 | 0 | 0 | `R.71` | `R.72` |

**LA GUARDA DE ADICION PURA DE `R.71`:** `git diff --numstat` da **146** lineas
anadidas y **0** borradas sobre `docs/PENDIENTES.md`; las lineas del texto de
entrada que no estan, en orden, en el de salida son **0**; y la SEGUNDA corrida
escribe **0** entradas y crece **0** bytes. La sede pasa de **1161546** bytes en
disco y **1161546** normalizado a LF, sha256 disco `f933b87fcbd7ba12` y sha256 LF
`f933b87fcbd7ba12`, a **1171455** bytes en disco y **1171455** normalizado a LF,
sha256 disco `c2129e11ec925f1f` y sha256 LF `c2129e11ec925f1f`.

**LAS DOS CAIDAS DE REPORTE, CORREGIDAS.** `docs/loop/reportes/REPORTE_V206.md`
pasa de **38335** bytes en disco y **38335** normalizado a LF a **41867** bytes en
disco y **41867** normalizado a LF, con **57** lineas anadidas y **0** borradas.

**`E.1`, MEDIDA POR MI Y NO COPIADA:** `docs/loop/SALIDA_V206_NO_MORDIO.txt` mide
**4151** bytes en disco y **4103** normalizado a LF, sha256 de disco
`f38bd7855d7760b5` y sha256 LF `cffa5cd0724d0427`. **Son distintos**, y la propia
linea corregida ya lo probaba sin saberlo.

**`E.2`, CON LA FUENTE CORRECTA:** `git show 78ca7176:` sobre
`docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt` da **3188** bytes en disco y **3188**
normalizado a LF, sha256 LF `b9df894ff422dc77`, y dice **39** celdas (**19** de
APERTURA, **19** de CIERRE, **1** SIN LADO). El mismo nombre HOY mide **1922** bytes en disco y **1922** normalizado a LF, con sha256 disco `254c2257ae55a0f2` y sha256 LF `254c2257ae55a0f2`, y dice **19** celdas con **18** de APERTURA. **El
`19 / 18` sale del segundo, que la vuelta 206 escribio en `a75ff760`.**

### 3.2 LA TAREA 2, CONTADA DE SUS FICHEROS

**LA VARA, SELLADA ANTES DE ABRIR NINGUN DOCUMENTO Y EN SU PROPIO COMMIT
`d7ab4545`:** **14** puntos, **14** citas comprobadas verbatim contra la ficha y
**0** que no aparezcan; **10** sellados como documentales y **4** como no
documentales, con su motivo escrito antes de mirar.

**LAS ONCE, CONTADAS CON `CABECERA_LD` IMPORTADA Y NO CON UN PATRON MIO:** **27**
cabeceras `LD` en el documento de hoy, **11** de la tanda, **16** de fuera, **0**
de las once que el patron no encuentre. Sus veredictos, **leidos de las cabeceras
y no tecleados**, dan **2** que empiezan por `A` y **9** que son `D`, y eso
**calza** con el `SALDO: 2 A y 9 D` que la ficha declara.

**LA COBERTURA, QUE ES LA CIFRA QUE ESTA MESA LLEVABA DOS VUELTAS SIN TENER**,
contada de `docs/loop/SALIDA_V207_T2_COTEJO.txt`:

| veredicto | cuantos | cuales |
|---|---:|---|
| **CUBRE** | **10** | `V.1`, `V.2`, `V.4`, `V.5`, `V.6`, `V.7`, `V.8`, `V.9`, `V.10`, `V.11` |
| **A MEDIAS** | **1** | `V.3` |
| **NO CUBRE** | **0** | (NINGUNO) |
| **NO DOCUMENTAL** | **3** | `V.12`, `V.13`, `V.14` |

**LA LISTA NOMINAL DE LOS QUE NO CUBREN: NINGUNO.** Sobre los **10** puntos
documentales sellados: **9** cubren, **1** a medias, **0** no cubren.

**NO CIERRO LA FICHA Y LO DEJO PROPUESTO** (`2.d` del encargo). **No toque el
campo `estado`**, y no lo digo: lo mide el `sha256` de la seccion 4.3.

### 3.3 EL CICLO ENTERO DE GATE 0, CORRIDO POR MI Y NUNCA `run_phase1.py` A SECAS

**LOS OCHO COMANDOS EN SU ORDEN, LOS DOS LADOS**, por el envoltorio
`scripts/loop/_v207_ciclo_gate0.py`, que **IMPORTA** `_v205_ciclo_gate0.py` y solo
le corrige el dato de la vuelta, que ademas computa de su propio nombre:

| corrida | salida | peor exitcode de los ocho |
|---|---|---:|
| lado APERTURA | `docs/loop/SALIDA_V207_CICLO_APERTURA.txt` | 0 |
| lado CIERRE | `docs/loop/SALIDA_V207_CICLO_CIERRE.txt` | 0 |

**`git diff HEAD --numstat` sobre `dataset/`, `web/`, `engine/` y `docs/plan/` da
0 filas DESPUES de correr yo el ciclo entero**, en las dos corridas.

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ESTADO DEL ARBOL AL ENTRAR, MEDIDO ANTES DE LA PRIMERA OPERACION** y sellado
en `docs/loop/SALIDA_V207_APERTURA.txt`:

CIFRA lineas de status, medidas con `git status --porcelain`: 1

CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: 0

**LA UNICA LINEA DE STATUS SE DICE EN VEZ DE ESCONDERSE DETRAS DEL NUMERO:** era
`?? scripts/loop/_v207_apertura.py`, mi propio computo de apertura sin trackear,
escrito por el comando que estaba midiendo. **El arbol entro limpio**, y
`git rev-list --left-right --count origin/pasada-unica...HEAD` daba **0** y **0**,
asi que no habia nada pendiente que committear ni que pushear (`EJECUTOR.md` 3).

**TODO LO DE ESTA SECCION SALE DE `git` CORRIDO EN ESTA VUELTA Y NO SE HEREDA DE
LA APERTURA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). El HEAD de
apertura contra el que se mide todo es `3e523b74`.

### 4.1 LAS CUATRO SEDES QUE EL ENCARGO EXIGE EN CERO, MEDIDAS AL CIERRE

Comando: `git diff 3e523b74 --numstat -- <sede>`

| sede | filas de numstat |
|---|---:|
| `dataset/` | 0 |
| `web/` | 0 |
| `engine/` | 0 |
| `docs/plan/` | 0 |

**CIFRA suma de filas de las cuatro sedes: 0.**

### 4.2 LAS TRES SEDES DEL AUDITOR, QUE EL EJECUTOR NO ESCRIBE

**EL CERO DE `PARA_ALEXIS.md` ES DE AUSENCIA DE FICHERO, Y ASI SE DICE**
(`4.5` del acta 204). Comando: `git diff 3e523b74 --numstat -- <sede>`.

| sede del auditor | existe en disco | filas de numstat | de que es el cero |
|---|---|---:|---|
| `docs/loop/PROMPT_SIGUIENTE.md` | SI | 0 | de no haberla tocado |
| `docs/loop/ACTA_AUDITOR.md` | SI | 0 | de no haberla tocado |
| `docs/loop/PARA_ALEXIS.md` | NO | 0 | **de ausencia de fichero**, no de no haberla tocado |

### 4.3 LAS SEDES SELLADAS, REMEDIDAS AL CIERRE Y NO HEREDADAS

| fichero | bytes (disco y LF, en el mismo renglon) | sha256 (disco y LF, en el mismo renglon) |
|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 4054129 bytes en disco y 4054129 bytes normalizado a LF | sha256 disco `0a77b5a35a962621` y sha256 LF `0a77b5a35a962621` |
| `docs/plan/OPERACIONES.jsonl` | 513043 bytes en disco y 513043 bytes normalizado a LF | sha256 disco `829c583eb779cab6` y sha256 LF `829c583eb779cab6` |
| `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 bytes en disco y 214916 bytes normalizado a LF | sha256 disco `dda1cdd67042c733` y sha256 LF `dda1cdd67042c733` |
| `docs/INTRA_DOMINIO_INFORME.md` | 943970 bytes en disco y 943970 bytes normalizado a LF | sha256 disco `c05b6bcd20188a9c` y sha256 LF `c05b6bcd20188a9c` |
| `docs/BANCO_DE_TEXTOS.md` | 182228 bytes en disco y 182228 bytes normalizado a LF | sha256 disco `68557cd00a3124f4` y sha256 LF `68557cd00a3124f4` |

**NINGUN campo `estado`, NINGUNA clase y NINGUN veredicto se movio, y no lo digo:
lo miden los `sha256` de arriba, identicos por las dos convenciones a los de mi
propio sello de apertura.** Los tres documentos de la TAREA 2 **se leyeron y no
se escribieron**, y sus `sha256` al cierre son los mismos con los que los abri.

### 4.4 LO QUE LA VUELTA SI TOCO, LEIDO DE `git` Y NO NARRADO

Comando: `git diff 3e523b74 --numstat` sobre el arbol entero.

| directorio tocado | ficheros |
|---|---:|
| `docs/loop` | 36 |
| `scripts/loop` | 10 |
| `docs/loop/reportes` | 1 |
| `docs` | 1 |

**CIFRA ficheros tocados contra el HEAD de apertura: 48.**

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. BAJE LA `V.3` A `A MEDIAS` POR UNA VARA QUE LA FICHA NO ESCRIBE.** La
`evidencia[2]` de `OP-L-01` dice, verbatim, *"BANCO_DE_TEXTOS.md, TABLA VIVA DE
LOS PUROS"*. **Con la letra estrecha, ese punto se cumple: la tabla existe, con
ese nombre exacto, en la linea 938.** Yo le exigi ademas **que llevara el efecto
de la mesa**, y como no cierra ninguna de las dos nominas que la mesa declara
completas, la baje a `A MEDIAS`.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** la ficha nombra el documento como sede
de evidencia, **no promete que ese documento quede actualizado**. Si el auditor
lee que la evidencia es *"existe la tabla y ahi se mira"*, mi `A MEDIAS` sobra y
la cobertura es **11 de 11**. **Yo creo que una evidencia que no lleva el efecto
de lo que evidencia no evidencia nada, pero la letra es del auditor y no mia**, y
por eso publico las dos lecturas con sus lineas para que se pueda revocar sin
volver a medir.

**`D.2`. LA `V.4` IBA SELLADA COMO NO DOCUMENTAL Y RESULTA QUE SI TIENE SEDE, Y
NO LA MOVI DE LADO.** Antes de abrir nada declare que la cifra *"205 pares
internos fuera de cola sobre 221 componentes"* no era documental, porque su sede
seria una salida de instrumento. **Abri el documento y esta ahi**, en
`LECTURAS_DIRIGIDAS.md:17` y `:21`. **Lo coteje y lo publique como CUBRE, pero
NO lo movi a la lista de documentales del sello**, porque mover un punto de lado
despues de mirar es exactamente lo que sellar el reparto viene a impedir.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** el resultado es que mis cifras de
cobertura tienen **10** puntos sellados como documentales pero **11** filas con
veredicto documental, y esa asimetria hay que leerla con la nota al lado. **Un
auditor podria decir con razon que lo limpio era declarar el sello equivocado y
rehacerlo**, en vez de arrastrar dos cuentas.

**`D.3`. LE PUSE LAS CUATRO MARCAS DEL ANEXO A MI PROPIO ESQUELETO YA ESCRITO, EN
VEZ DE PARARME.** Mi esqueleto nacio sin `<!-- TABLA DE TAREAS -->` y sus tres
hermanas, que son las que `anexar_tarea_al_reporte.py` busca. Sin ellas la fila
de cada tarea habria que teclearla, que es lo que `EJECUTOR.md` 1 prohibe. Lo
arregle con `scripts/loop/_v207_marcas_anexo.py`, **por adicion, con las dos filas
de tarea comprobadas byte a byte y publicando entera la tabla de sitio que
sustitui**. Va tambien como caida mia en la `C.1`.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** toque un reporte ya abierto y
committeado. **No re-lance el esqueleto a proposito**, porque a esas alturas el
PASO 0 habria intentado archivar la vuelta 207, que no ha cerrado.

## 6. LAS PREGUNTAS

**`P.1`. LA VARA DEL `4.1` DEL ACTA 202 SE ESCRIBIO PARA ACTAS ANTERIORES A LA
184. QUE VARA RIGE PARA LAS POSTERIORES?** Medido en la `3.0.a`: sobre el acta
206 da **0** adjudicaciones contando bien una seccion equivocada, y **0** caidas
del ejecutor sobre una seccion que se titula DOS. **Cada vuelta que registre un
acta moderna va a chocar con esto**, y ensanchar `MARCAS` toca un lector, que es
moratoria. **No lo decido yo.**

**`P.2`. UNA EVIDENCIA QUE NO LLEVA EL EFECTO DE LO QUE EVIDENCIA, CUBRE O NO
CUBRE?** Es la `D.1` en forma de pregunta, y no es solo de `OP-L-01`: las otras
tres fichas reales nombran documentos igual, y la respuesta decide como se
cotejan las tres.

**`P.3`. LAS DOS FILAS DE LA `TABLA VIVA DE LOS PUROS` SE ACTUALIZAN, Y QUIEN?**
Si la respuesta a la `P.2` es que no cubre, alguien tiene que escribir esas dos
filas por el carril del banco `9.10`, con correccion declarada y sin borrar el
texto viejo. **No lo hice yo**: no cabia con sus guardas al lado de las dos
sub-tareas, y una mesa a medias es peor que una mesa pendiente.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`. QUE SE HACE CON UN PUNTO DE UNA VARA SELLADA QUE, AL MIRAR, RESULTA
ESTAR DEL OTRO LADO.** Es la `D.2`. La casa manda sellar antes de mirar y manda
declarar en vez de resolver copiando, **pero no dice si el sello se corrige por
adicion declarada o se arrastra entero con su nota**. Hoy lo arrastre entero.
**Registro lo mejor sostenido y sigo** (`EJECUTOR.md` 5).

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. MI ESQUELETO NACIO SIN LAS CUATRO MARCAS DEL ANEXO.** `EJECUTOR.md` 1
dice que el reporte crece por anexion, y el instrumento que anexa busca cuatro
marcas literales que mi esqueleto no puso. **Lo cace al ir a anexar la TAREA 1**,
no despues, y lo arregle por adicion con las dos filas comprobadas byte a byte.
**Es la misma familia de las dos marcas que le faltaban al esqueleto de la 205**,
y me la encontre por no haber mirado que exigia el anexador antes de tallar. Sube
tambien como `D.3`.

**`C.2`. `docs/loop/SALIDA_V207_HEAD_APERTURA.txt` NACIO AL CIERRE, CON LAS DOS
TAREAS YA HECHAS.** El VALOR que lleva, `3e523b74948ee5ec0168c016fddc40ae02506229`,
**es de apertura de verdad y no lo teclee**: lo leyo un computo de
`docs/loop/SALIDA_V207_APERTURA.txt`, que escribi **antes de la primera
operacion** y que quedo committeado en `70044f73`. **Pero el fichero con ese
nombre nace ahora**, y el tallador lo exige para tallar la fila de identidad.
**Es la misma especie que la `C.3` del reporte de la 206 y la cuento una sola
vez, aqui.**

**`C.3`. MI PRIMERA BUSQUEDA DE LAS DOS FILAS DE LA `TABLA VIVA` NO ENCONTRO
NINGUNA, Y CASI PUBLICO UN `CUBRE` FALSO.** Exigi el literal `| nombre |` y la
tabla escribe `la junta asesora`, con articulo y con negritas. **Mi computo
concluyo `CIFRA nominas que la mesa declara CERRADAS y la tabla NO lleva
cerradas: 0` y de ahi salio un `CUBRE`**, que es exactamente el cero de un
instrumento publicado como un hecho del mundo que `EJECUTOR.md` 9 prohibe. **La
cace porque el resultado 11 de 11 me parecio demasiado limpio y fui a mirar la
tabla a mano.** La arregle, y ahora el computo **cae en `NO CUBRE` si no halla la
fila** en vez de concluir que no hay desajuste. **No llego a ningun documento**,
pero la casi caida tambien se cuenta, y el comentario que lo explica quedo dentro
del propio codigo para que no se pierda.

**`C.4`. CORRI `cerrar_reporte.py` TRES VECES, Y LA SEGUNDA DEJO EL REPORTE
ESCRITO Y EN ROJO.** El instrumento **escribe primero y valida despues**: su
segunda corrida pego cuerpo y cabecera, luego cayo en la guarda `D.1` y publico
`ROJO`, dejando en disco un `docs/loop/REPORTE.md` cerrado **con el cuerpo viejo
dentro**, el que todavia tenia las dos cifras sin pareja. **Lo cace en la tercera
corrida, porque el propio instrumento me dijo que el sujeto ya no estaba en
estado de reporte SIN CERRAR**, y lo devolvi a su sitio con
`git checkout HEAD -- docs/loop/REPORTE.md`, que lo restaura byte a byte del
commit de la TAREA 2. **NO llego a ningun commit** y ningun texto se perdio,
porque lo que se restaura estaba committeado.

**LOS TRES MOTIVOS POR LOS QUE LAS DOS PRIMERAS CAYERON, Y LOS TRES ERAN MIOS:**
mi veredicto decia *"las dos caidas de reporte"* hablando de las del acta 206, y
la guarda de numerales lo leyo como una cuenta de MIS caidas, que son tres, e
hizo bien: su propio docstring avisa de que una cuenta AJENA no se escribe como
`N caidas` a secas. Mi sello de apertura escribia `CIFRA lineas de status,
medidas con git status --porcelain: 1`, y el patron de la guarda `D.1` exige los
dos puntos pegados a la palabra `status`, asi que **no podia cotejar mi seccion 4
y se nego a cerrar a ciegas**, que es exactamente lo que tiene que hacer. Y dos
`sha256` mios iban sin su pareja en la misma linea. **Las tres las arregle yo y
ninguna es del instrumento.**

**LA DEL SELLO VA POR EL CARRIL DE LA CORRECCION DECLARADA:** anadi a
`docs/loop/SALIDA_V207_APERTURA.txt` la misma cifra en la forma que la guarda
sabe leer, **por adicion pura, con el texto viejo entero arriba** y con el valor
**leido del propio fichero y no tecleado**. `git diff --numstat` sobre ese sello
da **13** lineas anadidas y **0** borradas, y las lineas de la entrada que no
estan, en orden, en la salida son **0**. **La medicion es la de la apertura; lo
que llego tarde es la forma de escribirla.**

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**PROPONER ES MIO Y ENCARGAR ES DEL AUDITOR.** No escribo `PROMPT_SIGUIENTE.md`,
`ACTA_AUDITOR.md` ni `PARA_ALEXIS.md`, y el `numstat` de las tres contra mi HEAD
de apertura va en la seccion 4.2, en **0**, **0** y **0**, con el cero de
`PARA_ALEXIS.md` distinguido como **de ausencia de fichero**.

1. **`OP-L-01` ESTA MEDIDA Y PROPUESTA PARA CIERRE, CON 0 PUNTOS SIN CUBRIR Y 1 A
   MEDIAS.** Cerrarla es adjudicacion del auditor. Si la `D.1` se revoca, la
   cobertura es **11 de 11** y la ficha cierra limpia.
2. **LA SIGUIENTE DE LAS CUATRO FICHAS REALES.** Quedan `OP-L-02`, `OP-L-03` y
   `OP-I-01`. **`OP-L-02` sigue sin ningun documento que medir** y el encargo
   dice expresamente que no se toque todavia.
3. **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y CON SU EJECUCION
   SUSPENDIDA** (acta 202 `4.6`, ratificada por la 203 `4.9`, la 204 `4.10`, la
   205, la 206 y esta): se ejecuta en la primera vuelta despues de que la
   moratoria se levante. **La arrastro para que la 208 no la pierda.**
4. **LA COLA DE LA AUDITORIA INTEGRAL, QUE HOY CRECE A SIETE ENTRADAS
   NOMBRADAS:** las **5** entradas de la nomina que no muerden, partidas en 4 mas
   1 por la `6.2` del acta 206; el `--siguiente` del lanzador, que responde
   **183** en cualquier vuelta (acta 205 `5.2`); el patron de
   `preguntas_del_reporte()`, roto en la linea **196** de
   `scripts/loop/_v203_reparto_de_actas_viejas.py` (acta 204 `4.4`); la guarda de
   las dos convenciones, que solo mira BYTES y no `sha256` (acta 206 `7.2`); la
   falta de argumento de ruta en `cerrar_reporte.py` (acta 206 `6.3`); y **las
   DOS que anado yo hoy**: las `MARCAS` de la vara del `4.1`, que sobre un acta
   moderna eligen la seccion equivocada (`3.0.a`), y **`preguntas_del_reporte()`
   otra vez, que ya va por su tercera vuelta rodeada a mano**.
5. **LA DEUDA DE REGISTROS, ENSANCHADA HASTA LA 206 Y REMEDIDA AL CIERRE:** de la
   173 a la 206 quedan **5** actas sin entrada propia, y son la **201**, la
   **202**, la **203**, la **204** y la **205**. La del `4.9` del acta 201 sigue
   agotada en **0**. **La mido y la subo; encargarla es del auditor.**
6. **LA BATERIA NO CORRE HASTA LA 210** (`AUDITOR.md` 6.1), y cuando corra se va
   a encontrar las mismas cinco entradas que no muerden.
