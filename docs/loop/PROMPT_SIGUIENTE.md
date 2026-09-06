# ENCARGO DE LA VUELTA 186 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

---

## LO QUE ESTA VUELTA ES, Y LO QUE NO ES

**NO ES VUELTA DE BATERIA.** La bateria cerro entera en la 184 y por `AUDITOR.md`
6.1 corre **cada cinco vueltas**: la siguiente es la **189**. La seccion 9 de este
reporte cierra **con el HUECO DECLARADO Y MEDIDO** por el carril de
`cerrar_reporte.py`, con su nombre de fichero, sus bytes medidos y su atribucion.
**Las tres juntas o no vale.**

**EL TOPE SIGUE EN DOS SUB-TAREAS, PERO LA CUENTA YA NO ESTA EN CERO.** La 185
**cerro su propio reporte** (`cerrar_reporte.py` exitcode 0, cuatro piezas,
`REPORTE_V185.md` archivado en 42888 bytes): **es la PRIMERA de las dos seguidas
que el regimen `AUDITOR.md` 6.2 pide.** **Si esta vuelta cierra el suyo, la 187
recupera el tope de CINCO.** Van dos tareas y no hay una tercera.

**Y ESTA VUELTA TAMPOCO TOCA EL PLAN, Y EL ACTA 186 DICE POR QUE EN SU SECCION 12
EN VEZ DE DISIMULARLO.** El plan lleva **cinco vueltas sin moverse** (`sha256` del
archivo de veredictos identico en las actas 179 a 186). Las dos tareas de aqui son
**obligatorias, no elegidas**: la relectura al doble la manda `AUDITOR.md` 1.2, la
nomina evita un rojo ya medido para la 189, y las dos reparaciones son
adjudicaciones del acta 186 que no pueden quedar sin aplicar. **Meter el par 2.464
encima seria una tercera sub-tarea y el regimen 6.2 la prohibe.**

> **EL PAR 2.464, TRAMO 1 DE LA COLA POST FUSION, ENCABEZA EL ENCARGO DE LA 187**,
> y esta vez con el tope en cinco si esta vuelta cierra su reporte. **Queda escrito
> aqui, en la cabecera, para que no se pierda por sexta vez.**

**NO SE TOCA:** ni el marcador, ni un veredicto, ni `dataset/`, ni la mesa de los
tres nodos de la puerta del `PMF` que el acta 186 anota en su `6.4`. **Y NO SE
PODA LA NOMINA:** aqui se **completa**, que es lo contrario.

## EL SELLO DEL AUDITOR DE ESTA VUELTA, CON SU RUTA EXACTA

**NO LO DEDUZCAS DEL NUMERO DE VUELTA.** La casa nombra el sello del acta N como
`V(N+1)`, medido contra git en el acta 185; siendo acta **186**, el sello se llama
**`V187`**. **El `V186` no existe y no se fabrica**: es el hueco que dejo la `A.1`
del acta 185, explicado en la seccion 2 del acta 186.

| que es | ruta exacta | lo que el sello declara |
|---|---|---|
| sello | `docs/loop/SELLO_APERTURA_AUDITOR_V187.json` | **799 bytes** |
| ciega | `docs/loop/_auditor_v187_ciega_blind.txt` | **39911 bytes**, `sha256` `fd1275d43498fc9f` |
| destape | `docs/loop/_auditor_v187_ciega_reveal.txt` | **37559 bytes**, `sha256` `d5e5ec55e29378fd` |
| mis clases | `docs/loop/_auditor_v187_mis_clases.txt` | **4804 bytes**, escritas antes del destape |

**El clon de la relectura apunta a esas rutas, y esa es una diferencia mas que
declarar en el cotejo de clones.** **No copies esas cifras: computalas y
comparalas.**

---

## TAREA 1. LOS REGISTROS Y LAS DOS CUENTAS QUE VENCEN. BLOQUEANTE

### 1.a EL ACTA 186 ENTRA EN LA SERIE, Y EL NUMERO NO SE TECLEA

Corre `scripts/loop/serie_de_registros.py` en esta vuelta y usa **el numero que
devuelva**, no `R.48` porque lo diga aqui. La entrada registra, contadas del acta
acotada y no de memoria:

- las **siete adjudicaciones** `5.1` a `5.7`, todas **a favor**;
- los **cuatro pendientes de doctrina** de la seccion 6, de los que **`PD.5` y
  `PD.6` se CIERRAN por cita**, **`PD.1` sigue ABIERTA** con sus cinco puestos
  (**1778, 2530, 2540, 3141, 3232**), y el `6.4` es **una anotacion, no un
  pendiente propio**;
- las **tres preguntas** de la seccion 7, **las tres CONTESTADAS**;
- **cero caidas propias del auditor**, y eso se registra como cero, **no se
  omite**: un cero contado y un campo ausente no son lo mismo;
- **una caida del ejecutor de reporte**, la **`R.1`**, la del `git status` en cero
  lineas, **que NO acumula por vivir en prosa**;
- la **deuda de la serie REMEDIDA en esta vuelta**, no heredada del `R.47`.

**El acta 186 usa numerales entre comillas inversas**, igual que la 184 y la 185.
**Caso positivo por mutacion obligatorio**, con el esperado mutado cayendo, **sobre
un acta FABRICADA y no sobre la real**.

### 1.b LOS DOS ARNESES DE LA 185 ENTRAN EN LA NOMINA. ES LA RESPUESTA A LA `P.3`

**ESTO NO ES UNA MEJORA: ES UNA CAIDA YA MEDIDA CON TRES VUELTAS DE ANTELACION.**
El reporte de la 185 lo declaro en su `D.4` y su `P.3`, y el acta 186 lo verifico:
`arneses_que_faltan()` devuelve **2**, y son exactamente

- `scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py`
- `scripts/loop/vuelta185_tarea1c_mutacion_bateria_continuada.py`

**Sin ellos, la bateria de la 189 abre en rojo.**

**QUE HACER, Y NADA MAS QUE ESTO:**

1. Mete los dos en la nomina, **en la sede que la propia funcion consulta**. No
   inventes una sede nueva y no toques ninguna entrada existente.
2. **La prueba es que `arneses_que_faltan()` devuelva 0**, corrida despues, con su
   salida pegada. **Publica tambien el tamano de la nomina antes y despues**, para
   que se vea que crecio en dos y no en otra cosa.
3. **NO SE PODA NADA.** La opcion `c` de la parada del 5 sep (jubilar arneses
   viejos) quedo **RECHAZADA por el fundador**. Si al meterlos ves que algo
   sobra, **paras y lo traes**.

**Y CORRE LOS DOS ARNESES NUEVOS DOS VECES CADA UNO, EN PROCESOS APARTE**, y exige
que su `sha256` sea el mismo las dos veces. **Es la unica forma de saber hoy si
van a sobrevivir a la doble corrida de la 189 en vez de enterarse alli.** Si
alguno cambia solo, **paras y lo traes sin arreglarlo**: ese es un arnes ya
sellado, no uno en construccion, y le aplica la letra entera.

### 1.c LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 186

**POR QUE:** `AUDITOR.md` 1.2. Las **cuatro** discrepancias de la ciega del acta
186 cayeron **FUERA de los discutibles marcados**, porque el reporte de la 185 no
marco ningun par. **El credito de la tanda baja y el tramo se relee al doble.**

**COTEJA EL `sha256` ANTES DE LEER UN SOLO PUESTO**, contra
`docs/loop/SELLO_APERTURA_AUDITOR_V187.json`: la ciega tiene que medir **39911
bytes** y dar `sha256` `fd1275d43498fc9f`. **Si no calza, paras.** **Computalo y
comparalo; no copies la cifra de aqui.**

- **30 puestos** leidos de `docs/loop/_auditor_v187_ciega_blind.txt`.
- **30 vecinos deterministas**, con `vecinos()` **importada** de
  `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, **no copiada**.
- **Solape 0** entre tramo y vecinos, y **solape 0** con la ciega inmediatamente
  anterior (`docs/loop/_auditor_v185b_ciega_blind.txt`), **medido, no supuesto**.
- **60 puestos releidos, que es el doble exacto.**
- **NINGUNA CLASE SE VUELVE A DECIDIR.** La vara solo dice, por puesto: si declara
  diferenciador, si tiene lesion exacta, si algun nodo esta muerto en el grafo de
  hoy, y su clase de archivo.

**Y PUBLICA APARTE LAS CUATRO DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA
VARA:** los puestos **338, 491, 1775 y 2599**, **que el auditor pierde LOS CUATRO
a favor del archivo**. Di de cada uno si esta dentro del universo releido y que ve
la vara en el. **Lo que la vara no vea, no lo afirmes.**

**Y UNA CIFRA MAS, PORQUE EL 338 ES CLASE `B` Y LAS `B` SON 72 EN TODO EL
ARCHIVO:** publica **cuantas `B` hay en el universo releido**. **No la interpretes
ni la adjudiques: solo cuentala.**

---

## TAREA 2. LAS TRES REPARACIONES DE `cerrar_reporte.py` Y EL CIERRE DE DOS REPORTES

**LAS TRES REPARACIONES VAN JUNTAS Y CADA UNA CON SU PROPIO ARNES**, que es la
respuesta del acta 186 a la `P.1`. **Ninguna se prueba con el arnes de otra.**

**EL ARNES VIEJO SIGUE MANDANDO SOBRE LAS TRES:** corre
`scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py` **sin tocarlo** al
terminar, y tiene que salir **VERDE con sus 9 casos**. Si cambia de color, **paras**.

### 2.a LA PIEZA (4) DEJA DE LLEVAR SU PROPIA COPIA DE LA REGLA. ES LA `PD.6`

**ADJUDICADO EN EL ACTA 186, PUNTO 6.1.** `ajena != vuelta` vive **2 veces** en
`scripts/loop/cerrar_reporte.py`: en `rama_de_la_seccion9()`, que la `1.c` de la
185 ya reparo, y en la **pieza (4)** de `piezas_que_faltan()` (linea 905), que
**tiene su propia copia y no recibe la evidencia de los tramos**. El acta 185 ya
declaro ese rojo **falso** cuando la bateria se CONTINUA, citando la decision del
fundador de `AUDITOR.md` 6.1. **Reparar una sede y no la otra deja el instrumento
diciendo dos cosas distintas del mismo caso.**

**QUE HACER, Y ES LA MITAD QUE IMPORTA:**

1. **NO le pongas a la pieza (4) una copia sincronizada de la rama nueva.** **La
   regla se queda en UNA sede y la pieza (4) la LLAMA.** Dos copias que hoy dicen
   lo mismo son dos copias que manana diran cosas distintas, y eso es lo que ha
   costado cinco vueltas.
2. `piezas_que_faltan()` **gana el parametro que le falta** para poder llamarla, con
   **valor por defecto que conserva EXACTAMENTE la conducta de hoy**, igual que
   hizo `rama_de_la_seccion9()` en la 185.
3. **En `main()` ese valor SE COMPUTA con `tramos_por_vuelta()` y NO SE PASA POR
   BANDERA.** No anadas ninguna opcion de linea de ordenes: **una evidencia que se
   puede teclear no es una evidencia.**
4. **El rojo viejo no se reescribe.** Si falla cualquiera de las cuatro
   condiciones, la pieza (4) sigue cayendo con **su texto de hoy, palabra por
   palabra**.

**ARNES PROPIO OBLIGATORIO**, `scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py`,
con **estos casos como minimo, y todos tienen que CAER al mutar su esperado**: la
bateria de la 183 cerrando la 184 **con** tramos sellados en la 184 (la pieza (4)
**no** falta); **con la lista vacia** (falta, y con el motivo **literal** de hoy);
la bateria de la **185** cerrando la 184 (falta); **el parametro en su valor por
defecto** (identico a la conducta de hoy en todos los anteriores); y **un caso que
CAE si alguien vuelve a meter una segunda copia de la comparacion en el fichero**,
contando sus apariciones y exigiendo **1**.

### 2.b LA PIEZA (2) DEJA DE CAER SOBRE UNA CITA. ES LA `PD.5`

**ADJUDICADO EN EL ACTA 186, PUNTO 6.2, Y CON TRES CITAS.** Hoy
`cerrar_reporte.py` linea **877** hace `if HUECO_CABECERA in texto`, **busca en
todo el texto y no excluye los bloques cercados**. Medido sobre el caso real: la
marca aparece **UNA vez, en la linea 353**, **dentro de un bloque cercado**, y la
linea es **la propia guarda citando su propia salida**; y las **11 filas de 11** de
la cabecera **si estan pegadas**. **Es un falso positivo, y tal como esta hace
imposible que un reporte cite entera la salida roja de otro**, que es lo que el
encargo permanente manda hacer.

**QUE HACER:**

1. La pieza (2) busca `HUECO_CABECERA` **fuera de los bloques cercados**,
   **REUSANDO el desbloqueador que `cifras_sin_pareja()` ya tiene en este mismo
   fichero**. **No escribas un tercero.** Si esa funcion no esta separada, **sepArala
   y que las dos la llamen**: una sede, dos llamadores.
2. **Lo demas de la pieza (2) no se toca**: si el hueco esta fuera de una cerca,
   sigue siendo rojo; si el tallador no trae filas, sigue siendo rojo; si alguna
   fila no esta pegada, sigue siendo rojo, **con sus textos de hoy**.

**ARNES PROPIO OBLIGATORIO**,
`scripts/loop/vuelta186_tarea2b_mutacion_pieza2_cercas.py`, con **estos casos como
minimo, todos cayendo al mutar su esperado**: la marca **fuera** de toda cerca
(falta); la marca **solo dentro** de una cerca (**no** falta); la marca **en las
dos** (falta); **cero marcas** (no falta); una cerca **sin cerrar** al final del
texto, **con el valor exacto afirmado y no un "lo que salga"**; y **un caso sobre
el texto real de `SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md`** que exija que
la pieza (2) **ya no falte**.

### 2.c EL CARRIL DE CIERRE TARDIO, Y EL REPORTE DE LA 184 SE CIERRA. ES LA `P.2`

**LA RESPUESTA DEL ACTA 186 A LA `P.2` ES: NI SE EXIMEN NI SE REESCRIBEN. SE
DECLARAN.** Reescribir el texto de la 184 esta descartado (*"cerrar con el texto
que ya tiene"*, y seria escribir en pasado lo que no paso); eximir en silencio
esta descartado por banco 9.

1. `cerrar_reporte.py` gana un carril de **CIERRE TARDIO**, que se activa **solo
   cuando la vuelta que se cierra NO es la vuelta en curso**, y esa condicion **se
   computa, no se pasa por bandera**.
2. En ese carril, **las cifras sin pareja NO bloquean el cierre**, pero **se
   DECLARAN dentro del propio reporte cerrado, una a una, con su linea y su cuenta
   total**. **Un defecto declarado y medido no es un defecto exento.**
3. **En el carril normal no cambia nada**: las cifras sin pareja siguen siendo
   rojo. **Compruebalo con el arnes, no con la vista.**
4. **Ninguna otra guarda se afloja en el carril tardio.** Las cuatro piezas, el
   cuerpo byte a byte, los guiones y las citas de arnes siguen mandando igual. **Si
   al escribirlo ves que hace falta aflojar algo mas, paras y lo traes.**

**ARNES PROPIO OBLIGATORIO**,
`scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py`, con **estos casos como
minimo, todos cayendo al mutar su esperado**: cifras sin pareja **en carril
normal** (bloquea); **las mismas en carril tardio** (no bloquea **y aparecen
declaradas en el texto**, cotejado por contencion); **cero cifras sin pareja en
carril tardio** (la declaracion dice cero y no se omite); y **un caso que exija que
el carril tardio NO afloje ninguna de las cuatro piezas**.

**DESPUES, Y NO ANTES, SE CIERRA EL REPORTE DE LA 184.**

**PRIMERO LAS TRES PIEZAS SE COTEJAN POR `sha256` Y POR BYTES. Si CUALQUIERA
cambio, es ROJO: no se cierra, se dice, y paras.** **Recomputalas; no copies estas
cifras.**

| pieza | lo que la 184 midio y la 185 confirmo |
|---|---|
| `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` | **2435 bytes en disco, 2415 normalizados a LF** |
| `scripts/loop/_v184_cierre_texto.md` | **13982 bytes**, `sha256` **`050cdbb4ea99e11c`** |
| `docs/loop/SALIDA_V183_BATERIA.txt` | **71753 bytes**, `sha256` LF **`422a909ad6ffb167`** |

Luego `scripts/loop/cerrar_reporte.py --vuelta 184` con el veredicto de una linea
**TALLADO y no tecleado** (la guarda `B.1` tiene que dar **`CIFRA numerales que NO
calzan: 0`**), y despues `scripts/loop/archivar_reporte.py --vuelta 184`.
**Publica los bytes del archivado y su `sha256`, y di si es el CERRADO o no.**

**SI SIGUE SALIENDO ROJO POR ALGO QUE NO SEAN LAS CIFRAS SIN PAREJA, PARAS Y LO
TRAES ENTERO. No lo fuerces y no anadas un cuarto remedio por tu cuenta.**

### 2.d LA ESCALADA: LA SECCION 4 SE COTEJA CONTRA LA APERTURA SELLADA. `AUDITOR.md` 1.2

**LA RACHA DE REPORTE ESTA EN DOS Y ESTO ES LA OPERACION DE CODIGO DE LA ESCALADA,
NO UNA MEJORA.** La `R.1` del acta 186: el reporte de la 185 escribio en su seccion
4 que *"el arbol abrio limpio, con `git status --porcelain` en cero lineas"*, y
`docs/loop/SALIDA_V185_APERTURA.txt` bloque C, linea 36, dice **`CIFRA lineas de
status: 2`**. Y en la misma seccion vive un **15** tecleado en
`scripts/loop/_v185_cierre_texto.md` linea 40 que **ya no se puede reproducir**.
**Es la misma enfermedad: cifras del estado del arbol tecleadas en la prosa del
cierre en vez de leidas de la apertura sellada.**

**QUE HACER:**

1. Una guarda que **extrae de `docs/loop/SALIDA_V<N>_APERTURA.txt` las dos cifras
   que ese fichero ya publica**: `CIFRA lineas de status` y `CIFRA filas de
   git diff --numstat -- dataset/ AL ENTRAR`. **Funciones PURAS sobre el texto**,
   para que el arnes las pueda tumbar sin tocar el repo.
2. **Coteja esas dos contra lo que la seccion 4 del reporte afirma**, y **cae en
   ROJO si discrepan**, nombrando las dos cifras y sus dos sedes.
3. **Si el reporte no afirma una de las dos, eso NO es verde: es su propio rojo**,
   con su texto. Una cifra ausente y una cifra que calza no son lo mismo.
4. Cablearla donde `cerrar_reporte.py` juzga, **sin aflojar ninguna de las guardas
   que ya hay ahi**.

**ARNES OBLIGATORIO**, `scripts/loop/vuelta186_tarea2d_mutacion_seccion4.py`, con
**estos casos, todos cayendo al mutar su esperado**: las dos cifras calzando
(verde); **la de status mutada** (rojo, nombrandola); **la de numstat mutada**
(rojo); **la seccion 4 sin afirmar ninguna** (rojo); y **un caso sobre los ficheros
REALES de la 185** que exija que la guarda **hubiera cazado la `R.1`**. **Ese
ultimo es la prueba de la escalada: si no caza el caso que la trajo, no sirve.**

### 2.e EL REPORTE DE LA 186 SE ABRE, SE LLENA Y SE CIERRA

- **El PASO 0** del esqueleto **ya no tiene reporte ajeno que archivar** si la
  `2.c` cerro y archivo el de la 184. **Corre igual y pega lo que salga**, diga lo
  que diga, en vez de dejar la fila muda.
- **El esqueleto** se talla con sus **dos filas vacias**, una por tarea.
- **Cada tarea anexa su fila al cerrarse**, no al final.
- **La cabecera se talla con `scripts/loop/tallar_cabecera_reporte.py`**, y antes
  del commit `--comparar docs/loop/REPORTE.md` tiene que dar **CABECERA IDENTICA
  AL TALLADOR**, con su salida citada. **Cero celdas tecleadas.**
- **El desfase de calibrado se mide en la APERTURA**, dentro del bloque de apertura
  y antes de la primera operacion. **Desde la 178, una columna de apertura medida
  al cierre es caida que ACUMULA.**
- **LA SECCION 4 DE ESTE REPORTE SE ESCRIBE CON LAS CIFRAS QUE LA GUARDA DE LA
  `2.d` LEE DE LA APERTURA**, no con las que recuerdes. **Es el primer reporte que
  su propia escalada vigila, y eso se dice en el.**
- **LA SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO**: nombre del fichero,
  bytes medidos y atribucion, **las tres juntas**. La atribucion dice que la
  bateria corre cada cinco vueltas y que la siguiente es la **189**.
- **`scripts/loop/cerrar_reporte.py --vuelta 186`** y despues
  **`archivar_reporte.py --vuelta 186`**. **Si esta vuelta cierra su reporte, es la
  SEGUNDA de las dos seguidas y el tope vuelve a CINCO en la 187.** Dilo con esas
  palabras.

---

## LAS GUARDAS QUE NO SE TOCAN EN ESTA VUELTA

- **`git diff --numstat -- dataset/`** se mide **al entrar y al salir** y **las dos
  cifras se publican**. El `numstat` es la vara, no el `git status`.
- **Ningun veredicto se mueve.** El `sha256` LF de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` es **`ea6e850d331d14f0`** al abrir, y tiene
  que ser el mismo al cerrar. **Computalo, no lo copies.**
- **El ciclo de Gate 0 entero**, en su orden, con las suites en verde: 25/25 del
  motor, `tsc` exit 0, y la web en 82 ficheros y 1.040 tests.
- **Los clones declarados de esta vuelta se cotejan** y su salida se cita. **No
  afirmes que ningun diff sale vacio: publica lo que salga.**
- **Todo tamano de fichero va en BYTES EXACTOS leidos del instrumento** (`P.2`),
  nunca redondeado, y los KB solo entre parentesis y detras del byte.
- **Toda ruta que publiques como evidencia de una corrida es CIFRA** (5 sep 2026):
  si apunta a un fichero inexistente o de cero bytes, es **caida de cifra**.
  **Compruebalo antes de escribirla.**
- **Marca tus discutibles ANTES de saber si aciertas**, y **si alguno es de CLASE y
  no de metodo, dilo**: llevas dos vueltas sin marcar ninguno de clase y eso deja
  al auditor sin sujeto por donde empezar su ciega.

## LO QUE HAY QUE TRAER SIN RESOLVER SI APARECE

Si **cualquier arnes YA SELLADO** cae en rojo, **te detienes ahi, lo traes con su
salida entera, sin re-correrlo y sin arreglarlo**. **Un arnes que nace en esta
vuelta y todavia no ha sellado ninguna salida es otra cosa** (adjudicacion `5.2`
del acta 186): su rojo es parte de escribirlo, lo reparas, **y pegas la corrida en
rojo entera en el reporte con el motivo dentro del propio fichero**. Si el texto de
alguna de estas letras no alcanza para ejecutarla sin decidir, **eso es PARADA y no
una improvisacion**: paras y lo traes.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No adivines.
