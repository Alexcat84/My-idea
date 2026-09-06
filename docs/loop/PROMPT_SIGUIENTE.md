# ENCARGO DE LA VUELTA 185 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

---

## LO QUE ESTA VUELTA ES, Y LO QUE NO ES

**NO ES VUELTA DE BATERIA.** La bateria cerro entera en la 184, con sus nueve
tramos sellados, y por `AUDITOR.md` 6.1 corre **cada cinco vueltas**: la
siguiente es la **189**. En esta vuelta la seccion 9 del reporte cierra **con el
HUECO DECLARADO Y MEDIDO** por el carril de `cerrar_reporte.py`, con su nombre de
fichero, sus bytes medidos y su atribucion, o no vale.

**EL TOPE SIGUE EN DOS SUB-TAREAS** (`AUDITOR.md` 6.2). La 184 **no cerro su
propio reporte** (`cerrar_reporte.py` exitcode 1), asi que la cuenta de vueltas
que cierran su reporte **sigue en cero**. **Van dos tareas y no hay una tercera.**

**Y ESTA VUELTA NO TOCA EL PLAN, Y SE DICE POR QUE EN VEZ DE DISIMULARLO.** No se
relee el par **2.464** ni ningun otro de la cola post fusion, no se cablea el
instrumento de vigencia de las `A` rancias, no se toca el marcador, ni un
veredicto, ni `dataset/`. **El trabajo de esta vuelta es desatascar el cierre del
reporte, que lleva CUATRO vueltas sin conseguirse (181, 182, 183 y 184), y ese es
el mismo atasco por el que el fundador puso el regimen 6.2 el 5 sep.** La cola
post fusion, TRAMO 1, el par **2.464**, **encabeza el encargo de la vuelta 186** y
queda nombrada aqui para que no se pierda.

## EL ORDEN DE ESTA VUELTA, QUE NO ES EL DE SIEMPRE, Y EL MOTIVO

1. **BLOQUE DE APERTURA** entero, antes de la primera operacion: su sellado, el
   ciclo de Gate 0, y el cotejo del sello del auditor (abajo, con su ruta exacta).
2. **TAREA 1, letras `a` a `d`.** Cada letra se commitea con su salida al
   cerrarse. **Durante este tramo `docs/loop/REPORTE.md` sigue siendo el de la
   184 y NO se toca.**
3. **TAREA 2, primera mitad:** se cierra el reporte de la **184** con la guarda ya
   reparada por la `1.c`, y se archiva **CERRADO**.
4. **EL ESQUELETO DE LA 185** talla `docs/loop/REPORTE.md` con sus dos filas
   vacias.
5. **TAREA 1, letra `e`**, y la fila de la TAREA 1 se anexa al cerrarse.
6. **TAREA 2, segunda mitad:** se cierra el reporte de la **185** con su seccion 9
   de hueco declarado, y se archiva.

**POR QUE ASI Y NO CON EL PASO 0 PRIMERO.** Si el esqueleto de la 185 corriera
antes, su PASO 0 archivaria el reporte de la 184 **SIN CERRAR**, y la reparacion
de la `1.c` llegaria tarde para el unico reporte al que le sirve. **El reporte de
la 184 no es el parcial de una vuelta cortada:** sus dos tareas cerraron, la
bateria esta entera y las tres piezas del cierre estan talladas y medidas en
disco. Lo unico que falto fue el pegado, y lo impidio una guarda que el acta 185
adjudico como **falso rojo**. **Y en ningun momento de este orden el repo se
queda sin reporte en disco:** hasta el paso 4 vive el de la 184. **Si la vuelta se
corta entre el paso 2 y el 4, lo que queda es el reporte de la 184 mas los
commits de cada letra con su salida sellada, y la vuelta 186 retoma donde el
ultimo commit diga.**

## EL SELLO DEL AUDITOR DE ESTA VUELTA, CON SU RUTA EXACTA

**NO LO DEDUZCAS DEL NUMERO DE VUELTA: EL AUDITOR SE EQUIVOCO AL NOMBRARLO Y LO
DECLARO EN SU ACTA COMO CAIDA PROPIA `A.1`.** La casa nombra el sello del acta N
como `V(N+1)`, o sea `V186`, y el de esta acta se llama **`V185b`**. Los tres
ficheros son:

| que es | ruta exacta | lo que el sello declara |
|---|---|---|
| sello | `docs/loop/SELLO_APERTURA_AUDITOR_V185b.json` | **735 bytes** |
| ciega | `docs/loop/_auditor_v185b_ciega_blind.txt` | **39740 bytes**, `sha256` `94bd6198ab5ad277` |
| destape | `docs/loop/_auditor_v185b_ciega_reveal.txt` | **33733 bytes**, `sha256` `8e9e6d1566cd34f9` |

`scripts/loop/vuelta184_tarea1d_relectura_al_doble.py` lleva esa ruta **clavada
en una constante** (`SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V185.json")`,
linea 62, y `CIEGA` en la 63). **Su clon de esta vuelta apunta a las rutas de
arriba, y esa es una diferencia mas que declarar en el cotejo de clones.**

---

## TAREA 1. LOS REGISTROS Y LAS TRES REPARACIONES DE CODIGO. BLOQUEANTE

### 1.a EL ACTA 185 ENTRA EN LA SERIE, Y EL NUMERO NO SE TECLEA

Corre `scripts/loop/serie_de_registros.py` en esta vuelta y usa **el numero que
devuelva**, no `R.47` porque lo diga aqui. La entrada registra, contadas del acta
acotada y no de memoria:

- las **siete adjudicaciones** `5.1` a `5.7`, todas **a favor**;
- los **cuatro pendientes de doctrina** de la seccion 6, de los que **`PD.2`,
  `PD.3` y `PD.4` se CIERRAN por cita** y **`PD.1` sigue abierta**, esta ya con
  sus cinco puestos nombrados (**1778, 2530, 2540, 3141, 3232**);
- **una caida propia del auditor**, la **`A.1`** del nombre del sello, **contada
  y no tapada**;
- **una caida del ejecutor de reporte**, la **`R.1`**, la columna
  `quien lo sello` tecleada, **que NO acumula por vivir en prosa**;
- la **deuda de la serie REMEDIDA en esta vuelta**, no heredada del `R.46`.

**El acta 185 usa numerales entre comillas inversas**, igual que la 184, asi que
el patron que las cuenta es el que la 184 estreno. **Caso positivo por mutacion
obligatorio**, con el esperado mutado cayendo, sobre un acta fabricada y no sobre
la real.

### 1.b EL ARNES QUE PARO LA BATERIA: SU SALIDA SELLADA DEJA DE CAMBIAR SOLA

**El diagnostico esta medido dos veces, por el ejecutor de la 184 y por el
auditor de la 185, y coinciden:**
`scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py` sale **`exit 0`** y
sus **catorce casos pasan**; lo unico que falla es que **escribe en su salida
sellada un dato que cambia solo**: el sufijo del `mkdtemp` de la linea 124
(`tempfile.mkdtemp(prefix="v182_apertura_")`) se cuela por las lineas **134** y
**154**, que hacen `w("      | " + l[:130])` sobre el informe de `sellar()`. La
doble corrida de la bateria compara byte a byte y lo caza. **Tres lineas de
diferencia, las 53, 54 y 55 de su salida, y nada mas.**

**QUE HACER, Y NADA MAS QUE ESTO:**

1. Anade al fichero una funcion **PURA** `sin_temporal(linea, tmp)` que sustituya
   **todas las formas** de esa ruta por el literal `<TEMPORAL>`: la absoluta, la
   relativa con `/`, la relativa con `\`, y el nombre base suelto del directorio.
2. Aplicala en las lineas 134 y 154 **ANTES del recorte `[:130]`**, no despues:
   recortar primero puede partir la ruta por la mitad y dejar media sin
   normalizar.
3. **NO toques lo que el arnes prueba.** Sus catorce casos siguen siendo los
   mismos y siguen teniendo que pasar. **No se aflojan sus esperados ni se le
   quita ningun escenario.**

**ARNES PROPIO OBLIGATORIO**,
`scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py`, con **las dos mitades
fallando por separado**:

- **Mitad A, sobre la funcion PURA:** un caso por cada forma de la ruta (absoluta,
  relativa con `/`, relativa con `\`, nombre base), mas un caso que exija que
  **una linea sin ninguna ruta salga IDENTICA** (que no normalice de mas). **Todos
  tienen que CAER al mutar su esperado.**
- **Mitad B, la de verdad:** corre el arnes reparado **DOS VECES en un proceso
  aparte cada una** y exige que el `sha256` de
  `docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` sea **el mismo despues
  de las dos**. **Y exige tambien que las dos corridas salgan `exit 0`.** Si la
  normalizacion se quitara, esta mitad cae.

**DECLARA EN EL REPORTE QUE ESTA REPARACION REESCRIBE ESE FICHERO DE SALIDA** y
que el que se commitea es el de la forma reparada, con `<TEMPORAL>` dentro. **Es
esperado y se dice, no se disimula.**

**LO QUE NO SE PUEDE PROBAR EN ESTA VUELTA, Y SE DICE:** esta reparacion **no se
puede verificar contra la bateria**, porque la 185 no es vuelta de bateria. **La
prueba de esta vuelta es la doble corrida de la mitad B; la prueba definitiva
sera la bateria de la 189.** Escribelo asi en vez de dar por hecho el verde de
una corrida que no ha pasado.

### 1.c LA GUARDA DE LA BATERIA CONTINUADA. ES LA ADJUDICACION `6.2` DEL ACTA 185

**`PD.3` ADJUDICADA: el rojo de `cerrar_reporte.py` sobre el reporte de la 184 es
un FALSO ROJO**, y el acta 185 lo razona entero en su seccion 6.2. En corto: la
guarda nacio contra **pedir prestada la bateria terminada de otra vuelta**, y
**este no es ese caso**; `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026,
**manda** que *"UNA VUELTA CORTADA RETOMA EN EL TRAMO SIGUIENTE"*, o sea que una
bateria que cruza vueltas es lo que la decision **pide**. Cuando una guarda
contradice una decision escrita del fundador, **la que se corrige es la guarda**
(`AUDITOR.md` 0).

**LA REPARACION TIENE QUE EXIGIR MAS QUE LA GUARDA VIEJA, NO MENOS. En
`scripts/loop/cerrar_reporte.py`:**

1. **Dos funciones nuevas**, que la `1.d` va a reusar y por eso viven aqui y no
   duplicadas en otro sitio:
   - `vuelta_que_sello(asunto)`, **PURA**: devuelve el numero de vuelta que
     nombra el asunto de un commit (`VUELTA <N>`), o `None` si no lo nombra.
   - `tramos_por_vuelta(vuelta_del_fichero)`: para cada
     `docs/loop/SALIDA_V<vuelta_del_fichero>_BATERIA_TRAMO_<n>.txt` que exista,
     corre `git log -1 --format=%s -- <fichero>` y devuelve
     `{numero_de_tramo: vuelta_que_sello(asunto)}`.

2. **`rama_de_la_seccion9()` gana un CUARTO parametro**,
   `tramos_sellados_en_esta_vuelta=None`, **y sigue siendo PURA**. Con el valor
   por defecto `None` **se comporta EXACTAMENTE como hoy**, para que ningun
   llamador viejo cambie de conducta.

3. **UNA RAMA NUEVA, insertada ANTES del rojo de la vuelta ajena**, que solo abre
   si se cumplen **las CUATRO** condiciones a la vez:
   - `ajena < vuelta`. **Una bateria de una vuelta POSTERIOR siempre es rojo.**
   - `tramos_sellados_en_esta_vuelta` **no esta vacio**: al menos un tramo de esa
     misma bateria **se sello en la vuelta que se esta cerrando**. Esta es la
     evidencia de que la bateria se CONTINUO y no se pidio prestada.
   - el nombre **casa con `PATRON_NOMBRE_DE_CORRIDA`**.
   - **trae lineas**.

   Si falla **cualquiera** de las cuatro, **cae al ROJO de siempre, con su texto
   palabra por palabra tal como esta hoy**. El texto viejo **no se reescribe**.

4. **En `main()`, `tramos_sellados_en_esta_vuelta` SE COMPUTA con
   `tramos_por_vuelta()` y NO SE PASA POR BANDERA.** No anadas ninguna opcion de
   linea de ordenes para esto: **una evidencia que se puede teclear no es una
   evidencia.**

**EL ARNES VIEJO SIGUE MANDANDO:** corre
`scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py` **sin tocarlo** y tiene
que salir **VERDE**. Si cambia de color, la reparacion esta mal y **paras**.

**ARNES PROPIO OBLIGATORIO**,
`scripts/loop/vuelta185_tarea1c_mutacion_bateria_continuada.py`, con **estos
siete casos como minimo**, y **los siete tienen que CAER al mutar su esperado**:

| caso | lo que se le pasa | lo que tiene que devolver |
|---|---|---|
| A | bateria de la 183, cerrando la 184, **con** tramos sellados en la 184 | `CORRIDA` |
| B | bateria de la 183, cerrando la 184, **con la lista VACIA** | `ROJO`, y **el motivo, literal, igual al de hoy** |
| C | bateria de la **185**, cerrando la 184, con tramos | `ROJO` |
| D | bateria de la 183, cerrando la 184, con tramos, nombre `SALIDA_V183_HUECO_BATERIA.txt` | lo que el orden de las reglas de: **el caso afirma el valor exacto, no "no es CORRIDA"** |
| E | bateria de la 183, cerrando la 184, con tramos, **cero lineas** | **no** `CORRIDA`, con el valor exacto afirmado |
| F | bateria de la **184** cerrando la 184, con lineas | `CORRIDA`, **igual que hoy** |
| G | **cuarto parametro en su valor por defecto `None`** | **identico a la conducta de hoy en los casos A, B, C, F** |

Y **un caso mas sobre `vuelta_que_sello()`**, que es PURA: un asunto que nombra
la vuelta, uno que no la nombra, y uno que la nombra dos veces. **Los tres caen al
mutar el esperado.**

**LO QUE NO SE HACE, Y ES LA MITAD QUE IMPORTA:** no se copia el fichero de la
bateria, no se le cambia el nombre, no se afloja el rojo viejo y **no se toca
ninguna otra guarda**. Si al escribir esto ves que hace falta cambiar algo mas,
**paras y lo traes**.

### 1.d LA ESCALADA: LA COLUMNA `quien lo sello` SE COMPUTA. `AUDITOR.md` 1.2

**LA RACHA DE REPORTE ESTA EN DOS Y ESTO ES LA OPERACION DE CODIGO DE LA
ESCALADA, NO UNA MEJORA.** La caida `R.1` del acta 185: en
`scripts/loop/_v184_tallar_t2.py`, **linea 128**, la novena columna de la tabla
de los nueve tramos esta **TECLEADA**:

    quien = "vuelta 183" if n <= 4 else "**vuelta 184**"

debajo de una frase del reporte que dice que la tabla sale de contar sus ficheros
**"y no de recordar nada"**. **Los valores son correctos hoy y caducan solos: un
`n <= 4` tecleado seguira diciendo `vuelta 183` cuando la bateria de la 189 se
corte en otro sitio, sin que nadie lo toque.**

**QUE HACER:**

1. **Sustituye la linea 128** por una llamada a `vuelta_que_sello()` y
   `tramos_por_vuelta()`, **importadas de `cerrar_reporte.py`** y **no copiadas**:
   la vuelta que sello cada tramo se lee del asunto de su ultimo commit.
2. **Corre el tallador y coteja: las NUEVE celdas de esa columna tienen que salir
   IDENTICAS a las que el reporte de la 184 ya lleva** (tramos 1 a 4 `vuelta 183`,
   tramos 5 a 9 `vuelta 184`). **Ese cotejo es la prueba de la escalada:** la
   version computada reproduce la tecleada exactamente, y desde hoy la frontera
   tecleada no existe.
3. **NO re-pegues nada en `docs/loop/REPORTE.md`.** El reporte de la 184 se cierra
   en la TAREA 2 con el texto que ya tiene. Aqui solo se prueba el instrumento.

**ARNES:** los casos de `vuelta_que_sello()` de la `1.c` cubren la funcion pura.
Anade **un caso mas** que corra `tramos_por_vuelta(183)` **sobre los nueve
ficheros reales** y exija el reparto **4 y 5**, con el esperado mutado cayendo.

### 1.e LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 185

**POR QUE:** `AUDITOR.md` 1.2. Las **siete** discrepancias de la ciega del acta
185 cayeron **FUERA de los discutibles marcados**, porque el reporte de la 184 no
marco ningun par. **El credito de la tanda baja y el tramo se relee al doble.**

**COTEJA EL `sha256` ANTES DE LEER UN SOLO PUESTO**, contra
`docs/loop/SELLO_APERTURA_AUDITOR_V185b.json`: la ciega tiene que medir **39740
bytes** y dar `sha256` `94bd6198ab5ad277`. **Si no calza, paras.** No copies esa
cifra del encargo: **computala y comparala.**

- **30 puestos** leidos de `docs/loop/_auditor_v185b_ciega_blind.txt`.
- **30 vecinos deterministas**, con `vecinos()` **importada** de
  `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, **no copiada**.
- **Solape 0** entre tramo y vecinos, y **solape 0** con la ciega inmediatamente
  anterior (`docs/loop/_auditor_v185_ciega_blind.txt`), **medido, no supuesto**.
- **60 puestos releidos, que es el doble exacto.**
- **NINGUNA CLASE SE VUELVE A DECIDIR.** La vara solo dice, por puesto: si declara
  diferenciador, si tiene lesion exacta, si algun nodo esta muerto en el grafo de
  hoy, y su clase de archivo.

**Y PUBLICA APARTE LAS SIETE DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA
VARA:** los puestos **1208, 1459, 2363, 2386, 2505, 2636 y 2854**, **que el
auditor pierde LOS SIETE a favor del archivo**. Di de cada uno si esta dentro del
universo releido y que ve la vara en el. **Lo que la vara no vea, no lo afirmes.**

---

## TAREA 2. EL CIERRE DE DOS REPORTES: EL DE LA 184 Y EL DE LA 185

### 2.a EL REPORTE DE LA 184 SE CIERRA, CON LA GUARDA YA REPARADA

**Esto va DESPUES de la `1.c` y ANTES del esqueleto de la 185.**

**PRIMERO, LAS TRES PIEZAS SE COTEJAN POR `sha256` Y POR BYTES CONTRA LO QUE LA
184 MIDIO. Si CUALQUIERA cambio, es ROJO: no se cierra, se archiva tal como esta,
y se dice.** No es una formalidad: **cerrar hoy con piezas distintas de las que la
184 talló seria escribir en pasado lo que no paso**, que es justo lo que el PASO 0
del esqueleto de la 184 se nego a hacer.

| pieza | lo que la 184 midio |
|---|---|
| `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` | **2435 bytes en disco, 2415 normalizados a LF** |
| `scripts/loop/_v184_cierre_texto.md` | **13982 bytes**, `sha256` **`050cdbb4ea99e11c`** |
| `docs/loop/SALIDA_V183_BATERIA.txt` | **71753 bytes**, `sha256` LF **`422a909ad6ffb167`** |

**DESPUES, corre `scripts/loop/cerrar_reporte.py --vuelta 184`** con esas tres
piezas y el veredicto de una linea de la 184. **La rama de la seccion 9 tiene que
salir `CORRIDA` por la rama nueva**, y su motivo tiene que **nombrar que la
bateria se continuo y cuantos tramos sello la 184**. Si sale `ROJO`, **paras y lo
traes entero**: no la fuerces.

**EL VEREDICTO DE UNA LINEA SE TALLA, NO SE TECLEA A OJO.** La guarda `B.1`
coteja sus numerales contra lo que el cuerpo permite contar, y el cuerpo de la
184 cuenta **2 tareas** y **2 caidas propias** (`C.1` y `C.2`). **`CIFRA
numerales que NO calzan` tiene que dar 0.**

**LUEGO `scripts/loop/archivar_reporte.py --vuelta 184`**, y el archivado **tiene
que ser el CERRADO**, no el de antes. **Publica los bytes del archivado y su
`sha256`.**

### 2.b EL REPORTE DE LA 185 SE ABRE, SE LLENA Y SE CIERRA

- **El esqueleto** se talla en el paso 4 del orden de arriba, con las **dos filas
  vacias** de las dos tareas de este encargo, y su PASO 0 **ya no tiene reporte
  ajeno que archivar**, porque la `2.a` lo dejo archivado y cerrado. **Dilo asi en
  su salida en vez de dejar la fila muda.**
- **Cada tarea anexa su fila al cerrarse**, no al final.
- **La cabecera se talla con `scripts/loop/tallar_cabecera_reporte.py`**, y antes
  del commit `--comparar docs/loop/REPORTE.md` tiene que dar **CABECERA IDENTICA
  AL TALLADOR**, con su salida citada. **Cero celdas tecleadas.**
- **El desfase de calibrado se mide en la APERTURA**, dentro del bloque de
  apertura y antes de la primera operacion. **Desde la 178, una columna de
  apertura medida al cierre es caida que ACUMULA.**
- **LA SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO**, por el carril de
  `cerrar_reporte.py`: **nombre del fichero, bytes medidos y atribucion, las tres
  juntas**. Traer dos de tres **no es un hueco declarado a medias, es un hueco que
  no cuenta**. La atribucion dice que la bateria corre cada cinco vueltas y que la
  siguiente es la **189**.
- **`scripts/loop/cerrar_reporte.py --vuelta 185`** y despues
  **`archivar_reporte.py --vuelta 185`**. **Si esta vuelta cierra su reporte, es
  la PRIMERA de las dos seguidas que el regimen 6.2 pide para devolver el tope a
  cinco.** Dilo con esas palabras en el reporte.

---

## LAS GUARDAS QUE NO SE TOCAN EN ESTA VUELTA

- **`git diff --numstat -- dataset/`** se mide **al entrar y al salir** de la
  vuelta y **las dos cifras se publican**. La `M dataset/metadata/master_graph.json`
  de `git status` es **final de linea y no contenido**: el `numstat` es la vara.
- **Ningun veredicto se mueve.** El `sha256` LF de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` es **`ea6e850d331d14f0`** al abrir, y
  tiene que ser el mismo al cerrar. **Computalo, no lo copies.**
- **El ciclo de Gate 0 entero**, en su orden, con las suites en verde: 25/25 del
  motor, `tsc` exit 0, y la web en 82 ficheros y 1.040 tests.
- **La nomina de la bateria NO SE PODA.** La opcion `c` de la parada del 5 sep
  quedo **RECHAZADA** por el fundador.
- **Los tres clones declarados de esta vuelta se cotejan** y su salida se cita.
  **No afirmes que ningun diff sale vacio: publica lo que salga.**
- **Todo tamano de fichero va en BYTES EXACTOS leidos del instrumento** (`P.2`),
  nunca redondeado, y los KB solo entre parentesis y detras del byte.
- **Toda ruta que publiques como evidencia de una corrida es CIFRA** (5 sep 2026):
  si apunta a un fichero inexistente o de cero bytes, es **caida de cifra**.
  **Compruebalo antes de escribirla.**

## LO QUE HAY QUE TRAER SIN RESOLVER SI APARECE

Si **cualquier** arnes cae en rojo, **te detienes ahi, lo traes con su salida
entera, sin re-correrlo y sin arreglarlo**. Si el texto de alguna de estas letras
no alcanza para ejecutarla sin decidir, **eso es PARADA y no una improvisacion**:
paras y lo traes.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No adivines.
