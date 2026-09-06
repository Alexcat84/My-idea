# ENCARGO DE LA VUELTA 188 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

---

## LO QUE ESTA VUELTA ES, Y LO QUE NO ES

**LA PARADA QUE TRAJISTE NO ERA PARADA, Y ESTA ADJUDICADA.** El acta 188, punto
`7.1`, la resuelve con regla escrita: **no hay dos reglas vigentes en conflicto**,
hay un **esperado tecleado en la vuelta 186** y una **orden escrita en el encargo
de la 187** que lo dejo viejo. **Hiciste bien en no tocarlo** y en no cambiar el
`1` por un `2`. **El remedio va aqui, y va el primero de la maquinaria.**

**Y VA CON SU URGENCIA MEDIDA, QUE NO ES RETORICA: LA BATERIA ES LA 189, O SEA LA
VUELTA QUE VIENE.** `scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py`
esta **hoy en la nomina** y **hoy sale en ROJO** (`CIFRA fallos: 2`, exitcode 1,
reproducido por el auditor). **Sin el remedio de la TAREA 3, la vuelta de bateria
abre en rojo por una causa que ya esta adjudicada y se gasta entera en eso.**

**ESTA VUELTA LLEVA CINCO TAREAS.** El tope de cinco sigue vigente: el regimen
temporal de `AUDITOR.md` 6.2 quedo cumplido y apagado, y la 187 fue **la tercera
vuelta seguida** que cierra su propio reporte.

**NO ES VUELTA DE BATERIA.** Por `AUDITOR.md` 6.1 corre cada cinco vueltas y cerro
entera en la 184: **la siguiente es la 189**. La seccion 9 de este reporte cierra
**con el HUECO DECLARADO Y MEDIDO**: nombre del fichero, bytes medidos y
atribucion, **las tres juntas o no vale**.

**NO SE TOCA:** ni el marcador ni ningun veredicto (**esta vuelta no mueve
ninguno**); ni `dataset/`; **no se poda la nomina**; **no se anade ningun campo a
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`** (es la `PD.8`, y es del fundador); **no se
toca el campo `estado` de `docs/plan/OPERACIONES.jsonl`**, que la casa ya declaro
HISTORICO el 4 sep 2026; **no se reabre `docs/loop/reportes/REPORTE_V184.md`**; y
**no se abren las mesas anotadas** (la del `PMF` con los puestos **338**, **297**
y ahora **670**; la del **603**; y la de figuras del **226**).

## EL SELLO DEL AUDITOR DE ESTA VUELTA, CON SU RUTA EXACTA

**NO LO DEDUZCAS DEL NUMERO DE VUELTA.** La casa nombra el sello del acta N como
`V(N+1)`; siendo acta **188**, el sello se llama **`V189`**. **El `V186` no existe
y no se fabrica.**

| que es | ruta exacta | lo que el sello declara |
|---|---|---|
| sello | `docs/loop/SELLO_APERTURA_AUDITOR_V189.json` | **651 bytes** |
| ciega | `docs/loop/_auditor_v189_ciega_blind.txt` | **41098 bytes**, `sha256` LF `4dbbedc0ac89951e` |
| destape | `docs/loop/_auditor_v189_ciega_reveal.txt` | **34030 bytes**, `sha256` LF `9267fbf46cbad22f` |
| mis clases | `docs/loop/_auditor_v189_mis_clases.txt` | **6457 bytes**, escritas antes del destape |
| exclusion | `docs/loop/_auditor_v189_exclusion.txt` | **1648 bytes**, **351** puestos |

**No copies esas cifras: computalas y comparalas.**

---

## TAREA 1. LOS REGISTROS. BLOQUEANTE

### 1.a EL ACTA 188 ENTRA EN LA SERIE, Y EL NUMERO NO SE TECLEA

Corre `scripts/loop/serie_de_registros.py` en esta vuelta y usa **el numero que
devuelva**. La entrada registra, contadas del acta acotada (`ACTA_AUDITOR.md`,
desde la linea **66071**) y no de memoria:

- las **seis adjudicaciones** `5.1` a `5.6`, todas **a favor**;
- los **tres numerales de la seccion 6**: **`PD.1` ABIERTA** con sus cinco puestos
  (**1778, 2530, 2540, 3141, 3232**), **`PD.8` ABIERTA** (la forma de una
  correccion declarada dentro del archivo de veredictos, que es del fundador
  porque toca el esquema del archivo maestro), y el **`6.3` como ANOTACION**, que
  es el estado que el registrador ya sabe leer desde la 186: las mesas del `PMF`
  (**338**, **297**, **670**), la del **603** y la de figuras del **226**
  **no se encargan y no se adjudican**;
- las **tres preguntas** de la seccion 7, **las tres CONTESTADAS**;
- **cero caidas propias del auditor**, registradas **como cero y no omitidas**;
- **CUATRO caidas del ejecutor, todas de METODO y NINGUNA de racha**: `C.1` y
  `C.2` **declaradas por el ejecutor**, y `C.3` y `C.4` **levantadas por el
  auditor**. **La atribucion de las cuatro es DEL EJECUTOR**, y la seccion que las
  contiene lo dice en su cabecera;
- la **deuda de la serie REMEDIDA en esta vuelta**, no heredada.

**Caso positivo por mutacion obligatorio**, con el esperado mutado cayendo,
**sobre un acta FABRICADA y no sobre la real**. **Dos cosas que este registrador
tiene que aprender hoy y que la 187 no le pidio:** (1) que una seccion de caidas
puede llevar **caidas declaradas por el ejecutor y caidas levantadas por el
auditor bajo la misma cabecera**, y que **las dos son DEL EJECUTOR** porque la
atribucion la hace la cabecera y no quien las encontro; y (2) que **una caida
puede no acumular para ninguna racha** y eso **no es lo mismo que no existir**:
si el conteo de caidas y el conteo de racha salen iguales, **publica los dos y
di por que difieren**. **Y la PARADA se conserva entera**: un estado que no sepa
leer sigue siendo PARADA.

---

## TAREA 2. EL PLAN: LAS CUATRO FICHAS QUE LA VARA NOMBRA, RESUELTAS CONTRA SU EVIDENCIA

**ESTA ES LA TAREA QUE IMPORTA DE ESTA VUELTA. Si algo se cae, no es esta.**

**LA VARA YA ESTA CORRIDA Y SU SALIDA ESTA EN EL ACTA 188, PUNTO 12. VUELVE A
CORRERLA TU, con tu propio corte, y no copies su cifra:**

    python scripts/loop/vuelta150_3_relectura_expediente.py --corte <tu HEAD de apertura>

Dice **6 fichas en LISTA sin ninguna prueba: 4 TRABAJO REAL y 2 CONSUMIDAS**. Las
cuatro son **`OP-L-01`**, **`OP-L-02`**, **`OP-L-03`** (09_LECTURAS_DIRIGIDAS) y
**`OP-I-01`** (10_INVENTARIO).

**Y AQUI ESTA EL HALLAZGO DEL ACTA, QUE ES LO QUE ESTA TAREA TIENE QUE RESOLVER Y
NO REPETIR:**

> **LAS TRES PRUEBAS DE LA VARA SON DE GRAFO, Y UNA FICHA DE TIPO `MESA` NO DEJA
> HUELLA EN EL GRAFO: PRODUCE DOCUMENTOS.** Preguntarle al grafo si una mesa se
> hizo es **preguntarle a la fuente equivocada**, que es la caida del recuadro de
> `AUDITOR.md` 0: *"la fuente hay que elegirla antes de contarla"*. Las cuatro
> fichas son **`MESA`**, las cuatro.

**QUE HACER, EN ESTE ORDEN:**

1. **LEE LAS CUATRO FICHAS ENTERAS** de `docs/plan/OPERACIONES.jsonl`, con su
   `adjudicacion`, su `verificacion`, su `evidencia`, su `nota` y su
   `fecha_corte`. **Citalas, no las parafrasees.**
2. **PARA CADA UNA, MIDE SI SU PRODUCTO EXISTE**, contra la `evidencia` que la
   propia ficha nombra. El auditor ya midio dos y **no te las creas: recomputalas**:
   `docs/plan/LECTURAS_DIRIGIDAS.md` (la ficha de `OP-L-01` describe **once**
   lecturas, `LD-01` a `LD-11`) y `docs/plan/INVENTARIO.jsonl` (la ficha de
   `OP-I-01` describe **323 entradas**). **Publica de cada una: existe o no,
   bytes por las dos convenciones, y la cuenta de lo que la ficha promete contra
   la cuenta de lo que hay.**
3. **DA A LA VARA SU PATA DOCUMENTAL, Y ES CODIGO.** Que
   `vuelta150_3_relectura_expediente.py` **distinga el tipo de ficha**: para las
   que no son `MESA` sigue exactamente igual, **sin aflojar nada**; para las
   `MESA` anade **una cuarta prueba, DOCUMENTAL**, que mire si la `evidencia`
   declarada de la ficha existe en disco y la mida. **La cifra vieja SE SIGUE
   PUBLICANDO ENTERA Y AL LADO** (podar la cifra de la vara sin el fundador es lo
   que la casa reserva, y el propio fichero ya lo dice de su cuenta de
   consumidas): se publican **las dos**, la de siempre y la nueva, con su
   diferencia nombrada.
4. **DECLARA EL ESTADO DE CADA UNA DE LAS CUATRO, con su evidencia delante**, en
   una de estas tres formas y en ninguna otra:
   **(a) SU PRODUCTO ESTA Y LA CUBRE**, con la medicion que lo prueba;
   **(b) SU PRODUCTO ESTA PERO NO LA CUBRE**, nombrando **que falta exactamente**;
   **(c) NO HAY EVIDENCIA QUE LA DECIDA**, y entonces **es PARADA y se trae**.
5. **NO TOQUES EL CAMPO `estado`.** La casa lo declaro HISTORICO el 4 sep 2026 y
   esta tarea no lo cambia. Lo que se escribe es **la evidencia**, en el reporte y
   en la sede del plan que corresponda, **por adicion**.
6. **Y DI ADEMAS LO QUE VISTE DE SUS CORTES**, porque el auditor lo vio y lo dejo
   escrito: las cuatro fichas llevan `fecha_corte` **2026-08-11** y hablan de un
   marcador **"que sigue en 2.117"** cuando hoy son **3.388**; `OP-I-01` nombra
   como su hueco mayor **cuatro dominios que no han entrado al cribado** cuando el
   cribado esta cerrado entero. **Mide y publica el desfase. NO reescribas las
   fichas para ponerlas al dia: eso es plan, y si hace falta, se trae.**

**NINGUNA CLASE SE DECIDE EN ESTA TAREA Y NINGUN VEREDICTO SE MUEVE.** El `sha256`
LF de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre hoy en **`0a77b5a35a962621`** y
**tiene que cerrar igual**. Computalo, no lo copies.

---

## TAREA 3. EL CASO E: EL INVENTARIO DE EXENCIONES, EN VEZ DE UNA CUENTA TECLEADA. BLOQUEANTE

**ES LA ADJUDICACION DE TU `P.1` Y ES BLOQUEANTE PORQUE LA BATERIA ES LA 189.**

**EL DIAGNOSTICO, MEDIDO POR EL AUDITOR EN EL CODIGO Y NO SUPUESTO:** las dos
apariciones de `not tardio` en `scripts/loop/cerrar_reporte.py` viven en la
**1748** (la columna `bloquea` de las cifras sin pareja) y en la **1813**
(`if not tardio:` de la seccion 4). **La segunda es la exencion que el encargo de
la 187 mando anadir con estas palabras:** *"En el carril de CIERRE TARDIO, la
guarda de la `2.d` NO bloquea, pero SE DECLARA"*.

**QUE HACER:**

1. **EL CASO E DEJA DE CONTAR UN TEXTO.** Pasa a **computar el INVENTARIO de
   guardas eximidas en el carril tardio**, **con sus nombres**, leido del fuente.
2. **Y LO COTEJA CONTRA UNA LISTA AUTORIZADA Y ESCRITA**, que hoy tiene **DOS
   entradas**: la de **las cifras sin pareja** y la de **la seccion 4**. La lista
   vive **en el arnes**, con la vuelta y la decision que autorizo cada una escritas
   al lado, para que anadir una tercera sea **un acto visible y no un descuido**.
3. **CAE EN ROJO EN TRES CASOS, Y LOS TRES SE PRUEBAN:** si aparece **una exencion
   que no esta en la lista**; si **una de la lista desaparece del fuente**; y si
   **alguna eximida NO exige su declaracion** (la de la seccion 4 hoy si la exige:
   `if not dentro or sin_declarar: extra += 1 + len(sin_declarar)`, y eso es lo
   que hay que conservar).
4. **NO SE AFLOJA NADA, Y ESTO SE MIDE EN VEZ DE PROMETERSE:** el caso E queda
   **mas apretado que antes**, porque una cuenta de dos no distingue si las dos
   son las de la lista o si una se cambio por otra. **Si al escribirlo ves que hay
   que aflojar algo, paras y lo traes.**
5. **CAMBIA EL CASO E DENTRO DE SU PROPIO FICHERO**
   (`scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py`), **sin clonarlo y
   sin escribir un arnes nuevo para esquivarlo**, y **deja escrito dentro del
   fichero, en su docstring, quien autorizo el cambio**: acta 188, punto `7.1`.
   **Los otros diecisiete casos no se tocan**, y la prueba es que sigan cayendo al
   mutar su esperado: hoy son **17 de 17**.
6. **Y CUANDO ESTE, CORRELO Y PEGA SU SALIDA ENTERA.** Tiene que dar **`CIFRA
   fallos: 0`** y exitcode **0**. **Si no da verde, no lo fuerces: paras y lo
   traes.**

### 3.b LA SALIDA QUE ENVEJECE SOLA. ES TU `P.2`, Y ESTA A FAVOR

Tu distincion es la correcta y esta adjudicada: **lo que cambia entre dos corridas
del mismo dia sobre el mismo sujeto es PARADA; lo que se mueve porque su sujeto se
movio, no.** Aqui va solo su remedio barato, que es de una linea: **toda salida de
arnes que publique numeros de linea de un fichero vivo publica al lado el `sha256`
de ese fichero**, para que un diff futuro diga **si se movio el sujeto o se movio
el arnes** en vez de dejarlo a que alguien lo deduzca. **Hazlo en los arneses que
ya lo publican** (los cuatro de la 186 juzgan `cerrar_reporte.py`) y **publica el
`numstat` de lo que se mueva al hacerlo**.

### 3.c LA DOBLE CORRIDA NO RE-CORRE UN ARNES QUE YA SALIO EN ROJO. ES LA `C.3`

**ES EL REMEDIO DE UNA CAIDA QUE LEVANTO EL AUDITOR Y QUE TU NO TRAJISTE.** La
letra dice, sobre un arnes ya sellado que cae en rojo: *"te detienes ahi, lo traes
con su salida entera, **sin re-correrlo** y sin arreglarlo"*. En la 187 ese arnes
se corrio **dos veces mas** dentro de la doble corrida de la 5.a. **Y no hubo
choque de ordenes**: la 5.a pide *"corre cada arnes **NUEVO** dos veces"*, y ese
no era nuevo.

**Que la doble corrida de la nomina EXCLUYA explicitamente cualquier arnes que ya
haya salido en rojo en esa misma vuelta, y que lo DIGA en su salida** con el
nombre del excluido y el motivo. **Una exclusion muda seria peor que el
problema.** **Y queda escrita la letra que el acta 188 adjudica en su `5.3`, para
que no se re-litigue: un arnes sellado en rojo detiene AL ARNES, no a la vuelta;
la vuelta se cierra con la parada declarada.**

---

## TAREA 4. LA ESCALADA: LA GUARDA QUE VE LA MITAD, Y LA SECCION QUE SE DUPLICA

**LA RACHA DE REPORTE SIGUE EN DOS, ASI QUE `AUDITOR.md` 1.2 SIGUE SIENDO
MANDATORIO.** La escalada de la 187 esta descargada y verificada (caza las cuatro
cifras de la `C.1` sobre `bb3aaad3`). **Esta es la siguiente, y sale de una
medicion del auditor.**

### 4.a LA COBERTURA DE LA GUARDA DE LAS DOS CONVENCIONES

**EL HUECO, MEDIDO:** corrida sobre el reporte de la 187, `parejas_publicadas()`
**ve TRES parejas**. El barrido propio del auditor, sobre el mismo texto,
**atribuye SEIS sin ambiguedad**, y las seis calzan. Las tres que la guarda no ve:

| ruta | publicada | por que se le escapa |
|---|---|---|
| `docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt` | 2444 / 2424 | dice **"2424 normalizado a LF"**, sin repetir la palabra `bytes` y en singular |
| `docs/loop/_auditor_v188_exclusion.txt` | 1372 / 1372 | la ruta esta en una **fila de tabla anterior** y la pareja en la prosa de debajo |
| `docs/loop/SELLO_APERTURA_AUDITOR_V188.json` | 802 / 802 | separa las dos convenciones **con una coma**, no con una barra |

> **NO ES CAIDA: LAS SEIS CALZAN HOY.** Es que la guarda publica `toda pareja de
> convenciones es CIERTA` **mirando la mitad**, y eso es el mismo hueco de la
> escalada anterior corrido un paso: de *"la pareja existe pero puede ser falsa"*
> a *"la pareja es cierta, entre las que mi patron alcanza a ver"*.

**QUE HACER:**

1. **Ensancha las formas** para cubrir las tres de arriba, **leidas de reportes
   reales y no inventadas**. **La regla de la ambiguedad NO SE TOCA**: si entre la
   ruta y la pareja hay **otra** cifra de bytes, el sujeto sigue siendo ambiguo y
   **no se atribuye nada**. Esa regla es la que impide el rojo inventado del
   `15655`, y quitarla para ganar cobertura seria cambiar un hueco por otro peor.
2. **PUBLICA LA COBERTURA, Y ESTA ES LA MITAD QUE IMPORTA:** cuantas parejas ve la
   guarda **contra** cuantas rutas con cifra de bytes hay en el texto, y **cuantas
   quedan sin atribuir POR AMBIGUAS, nombradas una a una**. **Una guarda que no
   dice a cuanto llega no se puede auditar**, y hoy no lo dice.
3. **Arnes obligatorio** con, como minimo: **un caso por cada una de las tres
   formas nuevas** (cada uno con su mutacion cayendo); **un caso de ambiguedad**
   que exija que la guarda **NO** atribuya; y **UN CASO SOBRE EL TEXTO REAL DE
   `git show 9a06b7c8:docs/loop/REPORTE.md`** que exija **SEIS parejas vistas y
   SEIS que calzan**. **Ese ultimo es la prueba de la escalada.**

### 4.b LA SECCION QUE SE DUPLICA. ES LA `C.4`

**MEDIDO POR EL AUDITOR, Y ES NUEVO:** el reporte de la 187 tiene **DOS secciones
`## 9.`**, en las lineas **870** y **920**, con la **`## 10.`** en medio, en la
**877**. `REPORTE_V184.md`, `REPORTE_V185.md` y `REPORTE_V186.md` tienen **UNA
cada uno**. Y la de la 870 dice *"EL HUECO SE DECLARA CON SUS TRES PIEZAS
JUNTAS"* **sin traer ninguna de las tres**: nombre, bytes y atribucion viven en la
de la 920.

**Que `piezas_que_faltan()` exija que las secciones sean UNICAS Y ESTEN EN
ORDEN**, no solo que existan. **Es la misma especie que la escalada anterior**:
comprobar que algo **este** no es comprobar que **este bien**. **Con su arnes**,
y con **un caso sobre el texto real del reporte de la 187 que lo acuse**,
nombrando las dos lineas.

**Y ESTA VUELTA NO ESCRIBE DOS SECCIONES 9.** Si la seccion 9 la talla
`cerrar_reporte.py` al cerrar, **no escribas otra a mano en el anexo**: pon lo que
quieras decir de la bateria **en la que el instrumento talla**, o en una seccion
con numero propio.

---

## TAREA 5. LA RELECTURA AL DOBLE, LOS DOS REMEDIOS PEQUENOS Y EL CIERRE

### 5.a LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 188

**POR QUE:** `AUDITOR.md` 1.2. La discrepancia del auditor (**el puesto 1202**)
cayo **FUERA del discutible de clase marcado** (el reporte marco el **2464**).
**Fue UNA sola y estaba en sus propios dudosos, y el credito baja igual porque la
letra no distingue.**

**COTEJA EL `sha256` ANTES DE LEER UN SOLO PUESTO**, contra
`docs/loop/SELLO_APERTURA_AUDITOR_V189.json`: la ciega tiene que medir **41098
bytes** y dar `sha256` LF `4dbbedc0ac89951e`. **Si no calza, paras.**
**Computalo y comparalo; no copies la cifra de aqui.**

- **30 puestos** leidos de `docs/loop/_auditor_v189_ciega_blind.txt`.
- **30 vecinos deterministas**, con `vecinos()` **importada** de
  `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, **no copiada**.
- **60 puestos releidos, que es el doble exacto.**
- **NINGUNA CLASE SE VUELVE A DECIDIR.**

**Y AQUI VA EL REMEDIO DE TU `D.2`, QUE ESTA ADJUDICADO A FAVOR Y AUN ASI SE
ARREGLA.** El acta responde tu `P.3`: **el solape se le exige AL UNIVERSO**,
porque la exclusion existe para que nadie relea lo ya leido y los 60 se leen
todos. **Pero la vara no se tuerce a mitad de la medicion, que es lo que hiciste
bien.** Se arregla **por parametro y de forma aditiva**:

> **Dale a `vecinos()` un conjunto `evitar` OPCIONAL.** Sin el, se comporta
> **exactamente igual que hoy** (y eso lo prueba su arnes). Con el, salta tambien
> los puestos de `evitar` al subir. **Asi el cero sale por construccion y no por
> suerte.** **Su regla no cambia: cambia lo que se le pasa.**

Pasale los **351** de `docs/loop/_auditor_v189_exclusion.txt` y **publica los tres
solapes del UNIVERSO**: contra el tramo, contra
`docs/loop/_auditor_v188_ciega_blind.txt`, y contra la exclusion. **Los tres tienen
que dar 0, y si alguno no da 0, se declara con sus puestos nombrados y no se
arregla a la fuerza.**

**Y PUBLICA APARTE, MIRADO CON LA MISMA VARA, EL PUESTO 1202**
(`diferencias_venta_pequena_venta_grande` contra
`riesgo_tecnicas_cierre_venta_compleja`), **que el auditor pierde a favor del
archivo**. Di si esta dentro del universo releido y que ve la vara en el. **Lo que
la vara no vea, no lo afirmes.**

**Y UNA CIFRA MAS, Y NO ES DECORATIVA.** La razon del archivo en ese puesto cierra
con una **NOTA DE NOMINA** que cita el banco `9.20` y `9.10` y dice que
`riesgo_tecnicas_cierre_venta_compleja` **es el centro de un racimo y llevaba
CUATRO A contra hermanos**. **Cuenta y publica, para el universo releido, cuantos
de los 60 tienen en su razon una nota de ese tipo**, o sea evidencia **de FAMILIA
y no del par**. **Solo cuenta y publica. No interpretes y no adjudiques:** el
motivo esta escrito en el acta 188, seccion 4, y si resulta que la salida ciega no
lleva la carta que decide una parte de los pares, **eso es un hallazgo del
fundador y no tuyo**.

### 5.b LOS PUESTOS DEL DISCUTIBLE DE CLASE, PARA QUE EL AUDITOR PUEDA LEERLOS A CIEGAS

**ES LA TERCERA ACTA SEGUIDA QUE SUFRE ESTO Y CUESTA UN FICHERO.** `AUDITOR.md`
1.2 manda que la relectura ciega **empiece por los discutibles marcados del
reporte**; pero la apertura del auditor le prohibe abrir `REPORTE.md` antes de
sellar, **y los discutibles solo se saben leyendo el reporte**. Resultado: las
actas 186, 187 y 188 los han tenido que adjudicar **con los ojos abiertos**.

**Escribe `docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` con UNA SOLA COSA DENTRO: los
`puesto_intra` de los discutibles DE CLASE de esta vuelta, uno por linea, y nada
mas.** **Sin la clase, sin la razon, sin el nombre de los nodos y sin una palabra
de contexto**, porque cualquiera de esas cosas quema el sujeto. Si esta vuelta no
marca ningun discutible de clase, **el fichero se escribe igual y dice
`(ninguno)`**, que es una medicion y no un hueco. **Nombralo en el reporte.**

### 5.c EL ESQUELETO SE TALLA EN LA APERTURA. ES TU `C.1`, Y SU CAUSA ES MAS BARATA DE LO QUE DIJISTE

Tu `C.1` esta **confirmada por git**: en `07826009` el arbol llevaba todavia el
reporte de la 186. **Pero la causa que le pusiste no se sostiene, y esta medido
contra tu propia vuelta anterior.** Dices que el esqueleto **necesita** que
`SALIDA_V<N>_HEAD_APERTURA.txt` este commiteado; es cierto, y **no obliga a
esperar a la TAREA 1**. La vuelta 186 lo hizo en **tres commits**: `793ad9a1`
(apertura) -> **`88bd3216` (esqueleto, en su propio commit)** -> `456f0847`
(tarea 1). **El remedio cuesta un commit y estaba en uso hace una vuelta.**

**Hazlo asi en esta vuelta**: apertura y su commit, **esqueleto y SU PROPIO
COMMIT**, y despues las tareas. **Y publica el commit de cada uno**, para que se
vea que desde el segundo commit ya hay reporte parcial.

### 5.d EL REPORTE DE LA 188 SE ABRE, SE LLENA Y SE CIERRA

- **El esqueleto** se talla **en la apertura** (ver 5.c), con sus **cinco filas
  vacias**, una por tarea. **Cada tarea anexa su fila al cerrarse**, no al final.
- **La cabecera se talla con `scripts/loop/tallar_cabecera_reporte.py`**, y antes
  del commit `--comparar docs/loop/REPORTE.md` tiene que dar **CABECERA IDENTICA
  AL TALLADOR**, con su salida citada. **Cero celdas tecleadas.**
- **El desfase de calibrado se mide en la APERTURA**, antes de la primera
  operacion. **Una columna de apertura medida al cierre es caida que ACUMULA.**
- **LA SECCION 4 SE ESCRIBE CON LAS CIFRAS QUE LA GUARDA DE LA `2.d` LEE DE LA
  APERTURA**, no con las que recuerdes.
- **UNA SOLA SECCION 9**, y cierra **con el HUECO DECLARADO Y MEDIDO**: nombre,
  bytes medidos y atribucion, **las tres juntas**, y la atribucion dice que la
  siguiente vuelta de bateria es la **189**.
- **`scripts/loop/cerrar_reporte.py --vuelta 188`** y despues
  **`archivar_reporte.py --vuelta 188`**.

---

## LAS GUARDAS QUE NO SE TOCAN EN ESTA VUELTA

- **`git diff --numstat -- dataset/`** se mide **al entrar y al salir** y **las dos
  cifras se publican**. El `numstat` es la vara, no el `git status`.
- **El `sha256` LF de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` es
  `0a77b5a35a962621` al abrir, y al cerrar TIENE que ser el mismo**, porque esta
  vuelta no mueve ningun veredicto. **Computalo, no lo copies.**
- **El ciclo de Gate 0 entero**, en su orden, con las suites en verde: 25/25 del
  motor, `tsc` exit 0, y la web en 82 ficheros y 1.040 tests.
- **Los clones declarados de esta vuelta se cotejan** y su salida se cita. **No
  afirmes que ningun diff sale vacio: publica lo que salga.**
- **Todo tamano de fichero va en BYTES EXACTOS leidos del instrumento** (`P.2`),
  nunca redondeado, los KB solo entre parentesis y detras del byte, **y con SUS
  DOS CONVENCIONES MEDIDAS Y NO SUPUESTAS**. **Y ahora la guarda de la TAREA 4 ve
  mas formas que antes: si escribes mal una cifra en una forma nueva, tu propia
  tarea te tumba el cierre.**
- **Toda ruta que publiques como evidencia de una corrida es CIFRA** (5 sep 2026):
  si apunta a un fichero inexistente o de cero bytes, es **caida de cifra**.
  **Compruebalo antes de escribirla.**
- **Los arneses nuevos entran en la nomina en la vuelta que nacen**, y la prueba es
  que `arneses_que_faltan()` devuelva **0** al cerrar, con su salida pegada y con
  el tamano de la nomina antes y despues. **Hoy abre en 121. NO SE PODA NADA.**
- **Marca tus discutibles ANTES de saber si aciertas**, y **si alguno es de CLASE
  y no de metodo, dilo Y METE SU PUESTO EN EL FICHERO DE LA 5.b**. **El `D.5` de la
  187 fue un buen discutible de clase y el acta 188 lo dice: sigue asi.**

## LO QUE HAY QUE TRAER SIN RESOLVER SI APARECE

Si **cualquier arnes YA SELLADO** cae en rojo, **te detienes ahi, lo traes con su
salida entera, sin re-correrlo y sin arreglarlo**. **Y "te detienes ahi" es EL
ARNES, no la vuelta**: la vuelta se cierra con la parada declarada, y eso queda
adjudicado en el acta 188, `5.3`. **La unica excepcion de hoy es
`vuelta186_tarea2c_mutacion_cierre_tardio.py`, cuyo rojo YA ESTA ADJUDICADO y cuyo
remedio ES la TAREA 3**: ese si se toca, y solo en su caso E.

**Un arnes que nace en esta vuelta y todavia no ha sellado ninguna salida es otra
cosa** (adjudicacion `5.2` del acta 186): su rojo es parte de escribirlo, lo
reparas, **y pegas la corrida en rojo entera en el reporte con el motivo dentro
del propio fichero**.

Si el texto de alguna de estas letras no alcanza para ejecutarla sin decidir,
**eso es PARADA y no una improvisacion**: paras y lo traes.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No adivines.
