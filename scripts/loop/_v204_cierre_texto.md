## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE AQUI CITA EL FICHERO DEL QUE SALE Y SE RECONSTRUYO CONTANDO ESE
FICHERO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). El cierre corrio
**el ciclo entero de Gate 0 otra vez**, nunca `run_phase1.py` a secas, con sus
**8 comandos en su orden y los 8 en `EXITCODE 0`**.

| cifra | valor | de que fichero se cuenta |
|---|---|---|
| marcador, en su forma canonica | **3388 filas; A 551, B 72, C 5, D 2760**, con **huecos 0**, **dups(puesto) 0** y **0** lineas que no son JSON | `docs/loop/SALIDA_V204_CIERRE_MEDICIONES.txt`, bloque C |
| veredictos, por las dos convenciones | `0a77b5a35a962621` **al entrar y al salir**, disco y LF | bloque `D` de la apertura y bloque `B` del cierre |
| serie `R.n` | **58, 0, 0, `R.67`** al abrir y **60, 0, 0, `R.69`** al cerrar | `SALIDA_V204_SERIE_APERTURA.txt` y `SALIDA_V204_SERIE_CIERRE.txt` |
| racha de cierres | **5**, con las vueltas **199, 200, 201, 202 y 203** | bloque `E` de la apertura, corrido del instrumento |
| nomina de la bateria | **135**, que calza con el congelado de `AUDITOR.md` 6.3 | bloques `F` de apertura y `E` de cierre |
| censo de arneses | **197**, con **2** fuera de la nomina con la vara **148** y **62** sin vara | los mismos bloques |
| ficheros que esta vuelta anade a `scripts/loop/` | **15**, y **0 de los 15** entra en el censo | bloque `E` del cierre, comprobado uno a uno |
| deuda del `4.9` del acta 201 | eran **4** y quedan **2**: las **179 y 180** | `SALIDA_V204_T1_REGISTROS.txt` |
| formas del campo `cobertura` | **23** formas y **77** valores literales, con **15** entradas fuera de toda vara candidata | `SALIDA_V204_T2_COBERTURA.txt` |
| componentes | **332** en el sellado y **47** hoy, con **285** que faltan y **0** nuevas | `SALIDA_V204_T3_COMPONENTES.txt` |
| censo del plan | **71** fichas, **42 LISTA** y **29 HECHA**, contra **37** que no calzan y **4** de trabajo real | `SALIDA_V204_T4_CENSO.txt` |
| inventario de salidas de la vuelta | **34** al cierre, **0** de cero bytes | bloque `H` del cierre |
| rutas que este reporte publica como prueba | **32** distintas, **30 vivas**, **2 ausentes** y **0** de cero bytes | bloque `J` del cierre |
| cabecera del reporte, cotejada contra su tallador | **9 filas cotejadas, 0 DISTINTAS y 0 ausentes**, con veredicto **CABECERA IDENTICA AL TALLADOR** | `SALIDA_V204_TALLADOR_CABECERA.txt` y `SALIDA_V204_TALLADOR_COMPARAR.txt` |
| cierre del reporte | `cerrar_reporte.py` sale en **EXITCODE 0** con sus **cuatro piezas**, **0 cifras sin pareja**, **0 parejas falsas** y **0 citas de arnes que no calzan** | `SALIDA_V204_CERRAR_REPORTE.txt` |
| `docs/PENDIENTES.md` al cierre | **1145356** bytes en disco y **1145356** normalizado a LF | bloque `G` del cierre |
| `docs/plan/OPERACIONES.jsonl` al cierre | **513043** bytes en disco y **513043** normalizado a LF | bloque `G` del cierre |
| `docs/plan/INVENTARIO.jsonl` al cierre | **584554** bytes en disco y **584554** normalizado a LF | bloque `G` del cierre |
| `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` al cierre | **96361** bytes en disco y **96029** normalizado a LF | bloque `G` del cierre |
| `docs/loop/RECOMPUTO_V169.jsonl` al cierre | **15369** bytes en disco y **15322** normalizado a LF | bloque `G` del cierre |

**LAS DOS RUTAS AUSENTES SON AUSENCIAS DECLARADAS Y NO CAIDAS DE CIFRA**, y se
distinguen la una de la otra: `docs/loop/SALIDA_V204_BATERIA.txt` es **el hueco
declarado y medido** de la seccion 9, y `docs/loop/PARA_ALEXIS.md` es **una sede
del auditor que solo nace cuando hay PARADA** (`AUDITOR.md` 4) y hoy no la hay.
**Ninguna de las dos se publica como prueba de nada: se publican como la ausencia
que son.**

**LA PRUEBA POR MUTACION DE ESTA VUELTA, CONTADA DE SU FICHERO.**
`docs/loop/SALIDA_V204_T1_REGISTROS.txt` dice **9 casos, los 9 pasan, 0 rojos**,
con **4 casos donde la plantilla ancha y la heredada discrepan** y **9 de 9 que
caen** con el esperado mutado. `docs/loop/SALIDA_V204_T1_REGISTROS_SEGUNDA.txt`
**vuelve a correrla en vez de heredar su verde** y dice lo mismo.

**LOS TRES CLONES DE ESTA VUELTA, MEDIDOS CON `difflib` Y NO AFIRMADOS:** el
esqueleto, **445 lineas sin tocar de 501 y 81 nuevas o cambiadas**; el
registrador, **459 sin tocar de 485 y 36 nuevas**; las mediciones de cierre,
**268 sin tocar de 275 y 36 nuevas**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**AL ENTRAR**, medido en el bloque `C` de `docs/loop/SALIDA_V204_APERTURA.txt`
**antes de la primera operacion**: `git status --porcelain` daba **1** linea, que
era el propio fichero del sello; y `git diff --numstat -- dataset/` daba **0**
filas.

**LA TAREA 0, QUE ES LA PIEZA QUE EL ENCARGO OBLIGA A PUBLICAR AQUI.** El
`numstat` de las **TRES SEDES DEL AUDITOR** contra mi HEAD de apertura
`59d32eee`, leido del sello y no tecleado (bloque `K` del cierre):

| sede del auditor | filas de `numstat` contra el HEAD de apertura | como se lee ese cero |
|---|---:|---|
| `docs/loop/PROMPT_SIGUIENTE.md` | **0** | el fichero existe y mide **15196** bytes en disco y **15196** normalizado a LF; el cero es de **no haberlo tocado** |
| `docs/loop/ACTA_AUDITOR.md` | **0** | el fichero existe y mide **4734621** bytes en disco y **4734621** normalizado a LF; el cero es de **no haberlo tocado** |
| `docs/loop/PARA_ALEXIS.md` | **0** | **el fichero NO EXISTE** en el arbol ni en `git ls-files`; el cero es **de ausencia de fichero**, no de fichero sin tocar |

**LAS TRES DAN 0, QUE ES LO QUE EL ENCARGO EXIGE, Y LA TERCERA SE DISTINGUE EN
VEZ DE SUMARSE A LAS OTRAS DOS.** Va como hallazgo en la seccion 5.

**LO QUE ESTA VUELTA ESCRIBIO, Y NADA MAS:**

- `docs/PENDIENTES.md`, en **dos** sitios y **solo por adicion**: las entradas
  nuevas `R.67` y `R.68`. Mide al cierre **1145356** bytes en disco y **1145356**
  normalizado a LF, con **209** lineas mas y **0** lineas borradas o cambiadas.
- `docs/loop/REPORTE.md`, este fichero.
- Ficheros nuevos en `docs/loop/` y en `scripts/loop/`, todos con prefijo
  `_v204_`, `_gen_v204_` o `SALIDA_V204_`, y **ninguno entra en el censo**.

**LO QUE NO SE TOCO, MEDIDO Y NO AFIRMADO:**

- **`dataset/`, `web/`, `engine/` y `docs/plan/` en 0 filas de `numstat`**, al
  entrar y al salir. Y el cero de `docs/plan/` **no es de arbol limpio despues de
  commitear**: es de **no haber escrito nada ahi**, porque las TAREAS 2, 3 y 4
  **LEEN** esas sedes y ninguna las abre en modo escritura.
- **Ninguna clase y ningun veredicto:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
  abre y cierra en `sha256` **`0a77b5a35a962621`** en disco y **`0a77b5a35a962621`** normalizado a LF.
- **Ningun campo `estado`:** `docs/plan/OPERACIONES.jsonl` sale con el mismo
  `sha256` **`829c583eb779cab6`** en disco y **`829c583eb779cab6`** normalizado a LF, y **0 de las 71 fichas**
  cambian de estado.
- **La nomina sellada de componentes y la sede sellada de la 169:** las dos con
  el mismo `sha256` LF antes y despues, y `git status` sobre las dos da **0**
  filas.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA AMBIGUEDAD DE `ADJUDICACIONES` PUEDE SER DE TITULO Y NO DE CONTENIDO.**
En las actas 177 y 178 hay DOS secciones que titulan el numeral, la **7** y la
**10**, y por eso `R.67` y `R.68` lo declaran NO COMPUTABLE. **Medido**: la
seccion 10 aporta **0 claves por la vara ancha y 0 por el heredado** en las dos
actas, mientras la 7 aporta **11** y **13**. Si la vara se leyera como *la
seccion titulada que APORTA claves*, el numeral seria 11 y 13 sin decidir nada a
ojo. **No lo aplique y no lo escribi en las entradas: seria doctrina nueva.**

**`D.2` EL AGUJERO DE `cobertura` ES MAS PEQUENO DE LO QUE SU NOMBRE SUGIERE.**
Con seis patrones sacados del propio campo, **657 de 672 entradas ya son
comprobables a maquina y quedan 15**. Quien escriba la vara no se enfrenta a 672
casos de texto libre. **No escribo la vara y no propongo cual de las seis es.**

**`D.3` LAS 22 COMPONENTES QUE EL COLAPSO NO EXPLICA.** De las 285 que faltan,
**263 son colapso puro** y **22 no lo son**: 21 pares y un trio que **no tocan
ninguna componente de hoy**. Apunta a que su arista dejo de ser `A` en la sede de
veredictos y no a que sus nodos se fundieran. **Lo mido, lo nombro y lo dejo.**

**`D.4` LAS TRECE DEL CENSO NO SON UN BLOQUE HOMOGENEO.** Cuatro de las seis de
`03_FUSIONES` son hermanas del tronco `OP-M-02-*` y **una sola lectura las
cubriria**; y `OP-V-01` es de genero distinto, porque las doce afirman de menos y
ella **de mas**. **Propongo sin decidirlo** empezar por `OP-V-01` sola y seguir
por el tronco en bloque.

**`D.5` LA COINCIDENCIA DE LAS 569 PUEDE SER MAS QUE UNA COINCIDENCIA.** Las 569
entradas que caen en la vara candidata `N de N` son **exactamente** las 569 de
tipo `acto` o `racimo`, que es la poblacion del disparador. **Comprobado por
igualdad de conjuntos, con 0 y 0 en las dos diferencias.** Puede leerse como que
**la vara ya existe de hecho para el ambito que el disparador cubre**, y que lo
que falta es escribirla. **No lo afirmo: lo mido y lo marco.**

**`D.6` MI LECTURA DE `CONGELADO EN SILENCIO` COMO *nadie la ha mirado nunca*.**
La vara dice literalmente que **la ficha no dice nada de su estado**, y de ahi a
*nadie la ha mirado* hay un paso que **doy y declaro que doy**. Podria haber sido
mirada y no escrita. **Lo marco por si el paso sobra.**

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` ¿ES `PARA_ALEXIS.md` UNA SEDE QUE HAY QUE MEDIR AUNQUE NO EXISTA?** El
encargo la nombra como una de las tres sedes del auditor y pide que las tres den
`numstat` **0**. Las tres dan 0, pero **el cero de esa no es de la misma especie**
que el de las otras dos: **no hay fichero**. `AUDITOR.md` 4 la describe como el
fichero que el auditor escribe **cuando hay PARADA**. **Pregunto si la forma
correcta de publicarla es la que uso aqui, distinguiendo el cero, o si la sede
deberia salir de la lista mientras no exista.** No lo decido yo.

**`P.2` ¿PUEDE UNA ENTRADA `R.n` PUBLICAR EL REPARTO DE UNA SECCION CUANDO EL
NUMERAL ES AMBIGUO?** Hoy `R.67` y `R.68` declaran NO COMPUTABLE y **el reparto
de las once y las trece adjudicaciones queda fuera de la entrada**, aunque este
medido y sellado en `docs/loop/SALIDA_V204_T1C_AMBIGUEDAD.txt`. **Pregunto si la
entrada deberia PEGAR ese reparto como medicion, sin usarlo como numeral.**

## 7. PENDIENTES DE DOCTRINA

**`PD.1` LA CONVENCION DE BYTES SIGUE SIN FIJAR**, y sigue siendo del fundador.
Mientras no este fijada, **toda cifra de bytes y todo `sha` van con las dos**,
disco y normalizado a LF, que es lo que este reporte hace en todas sus celdas.

**`PD.2` LOS DOS TAMANOS DE `docs/loop/RECOMPUTO_V169.jsonl` DISCREPAN POR EL
CRLF** que `git checkout` deja: **15369** bytes en disco y **15322** normalizado
a LF. **Se publica y no se resuelve**, que es lo que el encargo manda.

**`PD.3` LA VARA DEL NUMERAL CUANDO DOS SECCIONES LO TITULAN.** La del `4.1` del
acta 202 dice *la seccion cuyo PROPIO TITULO lo nombra* y **no dice que hacer
cuando son dos**. Hoy la lectura es declarar NO COMPUTABLE, que es la conservadora
y la que no decide. **Queda como pendiente de doctrina y no se resuelve aqui.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE

**SON CUATRO, Y SE CUENTAN UNA SOLA VEZ Y EN UN SOLO SITIO.** Dos se publicaron
antes de cazarse y dos se cazaron antes de publicarse, y esa diferencia se dice
en vez de esconderse.

**`C.1`. PUBLIQUE `NO ESCRIBE` SOBRE UN INSTRUMENTO QUE SI ESCRIBE.** El bloque
`H.3` de mi sello de apertura dice **VEREDICTO DE LA COMPROBACION PREVIA: NO
ESCRIBE** sobre `scripts/loop/vuelta169_tarea3_op_i_01.py`. **La cifra que la
sostiene era cierta** (0 lineas de escritura directa) **y la palabra que le puse
encima, no**: ese instrumento escribe **por subproceso**, en sus lineas 147 y
157. **PUBLICADA ANTES DE CAZARSE.** El texto viejo sigue entero en el sello y no
se borra. Remedio aplicado en la TAREA 3: la salida se redirigio con
`V169_RECOMPUTO_SALIDA` y **la sede sellada quedo intacta**.

**`C.2`. EL MISMO SELLO PUBLICO SEIS CEROS QUE SE LEEN COMO UNA AUSENCIA FALSA.**
El bloque `H.1` publica **CIFRA cabeceras `## R.n.` que nombran el acta N: 0**
para las seis actas 173 a 178, **y las 173 a 176 SI tienen entrada**: `R.63`,
`R.64`, `R.65` y `R.66` las nombran. La causa esta medida: mi expresion regular
admitia como mucho **12** caracteres entre la palabra `acta` y el numero, y las
entradas escriben `del acta de la vuelta 173`, que trae **14**. **PUBLICADA ANTES
DE CAZARSE**, y la desmiente mi propio instrumento en la misma vuelta:
`serie_de_registros.py` y `SALIDA_V204_T1_REGISTROS.txt` cuentan la deuda en
**4** y no en **6**. **La cifra que gobierna es la del instrumento, no la mia.**

**`C.3`. ESCRIBI UN VEREDICTO DE CAUSA QUE MI PROPIA MEDICION DESMENTIA.** Mi
primera redaccion del bloque `F` de la TAREA 3 decia, **tecleada y no medida**,
*el instrumento y el motor NO cambiaron desde el corte del sellado, asi que la
causa NO es el instrumento*, y mi bloque `D.3` cuenta **2 commits** sobre
`scripts/plan/recomputo_3388.py` desde ese corte. **CAZADA ANTES DE PUBLICARSE**,
y la frase vieja queda escrita entera en la salida.

**`C.4`. DI POR DISJUNTOS DOS CONJUNTOS SIN COMPROBARLO.** Mi primera redaccion
del bloque `G` de la TAREA 2 decia que el agujero estaba *en las 103 de fuera mas
las 15 que ninguna vara alcanza*, y ese **mas** las hacia sumar. **Medido: las 15
son SUBCONJUNTO de las 103**, con 15 de 15 fuera del disparador y 0 dentro.
**CAZADA ANTES DE PUBLICARSE.**

**LAS CUATRO SON DE LA MISMA FAMILIA Y LO DIGO:** en las cuatro la CIFRA era
cierta y lo falso era **la frase que le puse encima**. Es la especie que
`EJECUTOR.md` 2 llama publicar sin volver a mirar, aplicada a mis propias
mediciones.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**PROPONER ES MIO Y ENCARGAR ES DEL AUDITOR** (TAREA 0 del encargo de esta
vuelta). Esto es una propuesta, no un encargo, y no toca ninguna sede del
auditor.

1. **LA 205 ES VUELTA DE BATERIA** por la cadencia de `AUDITOR.md` 6.1, y **no
   lleva nada mas**. Lo que sigue es para la 206 o para donde el auditor lo
   ponga.
2. **LAS TRECE DEL CENSO SON EL TRABAJO NATURAL QUE QUEDA**, y en este orden:
   **`OP-V-01` sola primero**, porque es la unica del expediente cuyo estado
   afirma **de mas**; y despues **el tronco `OP-M-02-*` en bloque**, porque cuatro
   de sus fichas comparten la misma lectura.
3. **LA DEUDA DE REGISTROS QUEDA EN 2**, las actas **179 y 180**, y cabe entera
   en una vuelta con el mismo computo importado.
4. **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y SUSPENDIDA** (acta
   202 `4.6`, ratificada en el `4.9` del acta 203), y **la arrastro aqui para que
   la 205 no la redescubra**: una pieza de `cerrar_reporte.py` que, cuando el
   reporte declare una PARADA, exija la **medicion POSITIVA de cada premisa de
   hecho**, con su fichero sellado, y **caiga en ROJO si falta**, con su caso por
   mutacion delante. **Se ejecuta en la PRIMERA vuelta despues de que la
   moratoria se levante.**
5. **LA VARA ESCRITA PARA `cobertura`** sigue en la auditoria integral (acta 203
   `4.7`), y esta vuelta **le deja el terreno medido**: 23 formas, 15 entradas
   fuera de toda vara candidata, y la particion de 569 contra 103.
