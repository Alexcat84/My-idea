# ENCARGO DE LA VUELTA 187 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

---

## LO QUE ESTA VUELTA ES, Y LO QUE NO ES

**EL TOPE VUELVE A CINCO, Y ESTA MEDIDO.** El regimen temporal de `AUDITOR.md`
6.2 pedia **dos vueltas seguidas cerrando su propio reporte**. La 185 fue la
primera. **La 186 es la segunda:** `docs/loop/SALIDA_V186_CERRAR_REPORTE.txt` da
`CIFRA piezas que faltan: 0` y VERDE, y `REPORTE_V186.md` quedo archivado byte a
byte igual al arbol. **El regimen de dos sub-tareas queda CUMPLIDO y se apaga
solo**, por su propio disparador de salida. **Esta vuelta lleva CINCO tareas.**

**Y CON EL TOPE EN CINCO SE ACABA LA ARITMETICA QUE APLAZABA EL PLAN.** El acta
186 escribio que el 2.464 no cabia porque el tope era dos y las dos tareas eran
obligatorias. **Hoy ese argumento no existe.** El plan lleva **seis vueltas sin
moverse** (`sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` identico en las
actas 179 a 187) y **tres actas seguidas escribiendolo**.

> **POR ESO EL PAR 2.464 Y EL TRAMO 1 DE LA COLA POST FUSION VAN EN LA TAREA 2,
> DELANTE DE TODA LA MAQUINARIA SALVO LOS REGISTROS.** Si esta vuelta se corta
> por falta de sitio, **que se caiga la maquinaria, no el plan**. Es la sexta vez
> que este par se escribe en un encargo y la primera en que va delante.

**NO ES VUELTA DE BATERIA.** Por `AUDITOR.md` 6.1 corre cada cinco vueltas y
cerro entera en la 184: **la siguiente es la 189**. La seccion 9 de este reporte
cierra **con el HUECO DECLARADO Y MEDIDO**: nombre del fichero, bytes medidos y
atribucion, **las tres juntas o no vale**.

**NO SE TOCA:** ni el marcador ni ningun veredicto **fuera de lo que la TAREA 2
resuelva con su vara**; ni `dataset/`; **no se poda la nomina** (aqui se
completa); **y no se reabre ni se reescribe `docs/loop/reportes/REPORTE_V184.md`**,
que ya esta cerrado y archivado.

## EL SELLO DEL AUDITOR DE ESTA VUELTA, CON SU RUTA EXACTA

**NO LO DEDUZCAS DEL NUMERO DE VUELTA.** La casa nombra el sello del acta N como
`V(N+1)`; siendo acta **187**, el sello se llama **`V188`**. **El `V186` no
existe y no se fabrica.**

| que es | ruta exacta | lo que el sello declara |
|---|---|---|
| sello | `docs/loop/SELLO_APERTURA_AUDITOR_V188.json` | **802 bytes** |
| ciega | `docs/loop/_auditor_v188_ciega_blind.txt` | **42599 bytes**, `sha256` `ea6d846cb7e0c73e` |
| destape | `docs/loop/_auditor_v188_ciega_reveal.txt` | **32894 bytes**, `sha256` `a602a9170a30beef` |
| mis clases | `docs/loop/_auditor_v188_mis_clases.txt` | **8030 bytes**, escritas antes del destape |

**No copies esas cifras: computalas y comparalas.**

---

## TAREA 1. LOS REGISTROS. BLOQUEANTE

### 1.a EL ACTA 187 ENTRA EN LA SERIE, Y EL NUMERO NO SE TECLEA

Corre `scripts/loop/serie_de_registros.py` en esta vuelta y usa **el numero que
devuelva**, no `R.49` porque lo diga aqui. La entrada registra, contadas del acta
acotada y no de memoria:

- las **seis adjudicaciones** `5.1` a `5.6`, todas **a favor**;
- los **dos numerales de la seccion 6**, de los que **`PD.1` sigue ABIERTA** con
  sus cinco puestos (**1778, 2530, 2540, 3141, 3232**) y el **`6.2` es una
  CORRECCION POR DECLARACION**, que es un estado nuevo y no un pendiente: **la
  `PD.7` del reporte de la 186 NO es un pendiente de doctrina** y **el numero
  `PD.7` queda libre**;
- las **tres preguntas** de la seccion 7, **las tres CONTESTADAS**;
- **cero caidas propias del auditor**, registradas **como cero y no omitidas**;
- **una caida del ejecutor de reporte**, la **`C.1`**, la de las cuatro cifras de
  LF supuestas, **que NO acumula por vivir en lista de rutas y en prosa**, y
  **cuya especie el acta 187 CORRIGE**: no es cifra publicada;
- la **deuda de la serie REMEDIDA en esta vuelta**, no heredada.

**Caso positivo por mutacion obligatorio**, con el esperado mutado cayendo,
**sobre un acta FABRICADA y no sobre la real**. **El registrador tiene que
aprender el estado `CORRECCION POR DECLARACION`** igual que la 186 le enseno
`ANOTACION`, y **hacer PARADA si aparece un estado que no sabe leer** en vez de
meterlo en el saco de los abiertos o los cerrados.

---

## TAREA 2. EL PLAN SE MUEVE: EL PAR 2.464 Y EL TRAMO 1 DE LA COLA POST FUSION

**ESTA ES LA TAREA QUE IMPORTA DE ESTA VUELTA. Si algo se cae, no es esta.**

1. **LEE EL DISPARADOR ESCRITO ANTES DE TOCAR NADA.** La cola post fusion tiene
   su criterio escrito en `docs/plan/08_VERIFICACION.md` y en el `BANCO_DEL_PLAN`.
   **Citalo por numero en el reporte antes de aplicarlo.** Si el texto no alcanza
   para ejecutarlo sin decidir, **eso es PARADA y no una improvisacion**.
2. **EL PAR 2.464 ENCABEZA**, y detras va **el tramo 1 de la cola** tal como el
   disparador lo defina. **No inventes el tamano del tramo: computalo del
   criterio escrito y publica cuantos pares entran y por que.**
3. **CADA PAR QUE MUEVAS LLEVA SU CORRECCION DECLARADA Y SU RECOMPUTO**, por la
   letra de `AUDITOR.md` 1.3. **Ningun veredicto se mueve en silencio.**
4. **PUBLICA EL `sha256` DEL ARCHIVO AL ABRIR Y AL CERRAR.** Hoy es
   `ea6e850d331d14f0`. **Si esta tarea mueve algo, el de cierre TIENE que ser
   distinto, y la diferencia se explica par por par.** **Si no mueve nada, dilo
   con esas palabras y di por que**, porque seria la septima vuelta quieta.
5. **Y EL MARCADOR SE RECOMPUTA DEL ARCHIVO CON SU COMANDO**, no se ajusta a mano:
   filas, A/B/C/D, puestos unicos, huecos y duplicados.

**NO ABRAS LA MESA DEL `PMF`** (los tres nodos de los puestos **338** y **297**),
ni la del **603**, ni la de figuras del **226**. **Las tres estan anotadas en el
acta 187, seccion 6.2, con sede en `PENDIENTES.md`, y son trabajo de plan de otra
vuelta.**

---

## TAREA 3. LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 187

**POR QUE:** `AUDITOR.md` 1.2. Las **cuatro** discrepancias de la ciega del acta
187 cayeron **FUERA del discutible de clase marcado** (el reporte marco el 338 y
ninguna de las cuatro es el 338), y **tres cayeron fuera incluso de los dudosos
que el auditor habia marcado de antemano**. **El credito de la tanda baja y el
tramo se relee al doble.**

**COTEJA EL `sha256` ANTES DE LEER UN SOLO PUESTO**, contra
`docs/loop/SELLO_APERTURA_AUDITOR_V188.json`: la ciega tiene que medir **42599
bytes** y dar `sha256` `ea6d846cb7e0c73e`. **Si no calza, paras.** **Computalo y
comparalo; no copies la cifra de aqui.**

- **30 puestos** leidos de `docs/loop/_auditor_v188_ciega_blind.txt`.
- **30 vecinos deterministas**, con `vecinos()` **importada** de
  `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, **no copiada**.
- **Solape 0** entre tramo y vecinos, **solape 0** con la ciega inmediatamente
  anterior (`docs/loop/_auditor_v188_ciega_blind.txt` es la de hoy; la anterior
  es `docs/loop/_auditor_v187_ciega_blind.txt`), y **solape 0 con los 293 puestos
  de `docs/loop/_auditor_v188_exclusion.txt`**. **Medido, no supuesto.**
- **60 puestos releidos, que es el doble exacto.**
- **NINGUNA CLASE SE VUELVE A DECIDIR.**

**Y PUBLICA APARTE LAS CUATRO DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA
VARA:** los puestos **226, 603, 1612 y 2448**, **que el auditor pierde LOS CUATRO
a favor del archivo**. Di de cada uno si esta dentro del universo releido y que
ve la vara en el. **Lo que la vara no vea, no lo afirmes.**

**Y UNA CIFRA MAS, Y ESTA VEZ NO ES DECORATIVA. Publica cuantas `B` hay en el
universo releido, y ademas, PARA CADA `B` DEL UNIVERSO, si declara diferenciador,
si tiene lesion exacta y si tiene nodo muerto.** El motivo esta medido en el acta
187, `5.6`: **las tres `B` conocidas (338, 226, 603) dan NADA en las cuatro
comprobaciones mecanicas y aun asi son `B`**. **Solo cuenta y publica. No
interpretes y no adjudiques:** si la vara resulta ciega a la clase `B` entera,
eso es un hallazgo del fundador y no tuyo.

---

## TAREA 4. LA ESCALADA: LA PAREJA DE CONVENCIONES DEJA DE BASTAR CON EXISTIR

**LA RACHA DE REPORTE ESTA EN DOS Y ESTO ES LA OPERACION DE CODIGO DE LA
ESCALADA, NO UNA MEJORA.** `AUDITOR.md` 1.2, mandatorio a partir de dos.

**EL HUECO, MEDIDO Y NO SOSPECHADO.** `cerrar_reporte.py` publica hoy en su
bloque D la linea `toda cifra de bytes y todo sha con su pareja SI`, y **las
cuatro cifras falsas de la `C.1` pasaron por delante de esa linea sin encender
nada**. Motivo: **la guarda comprueba que la pareja EXISTA, no que sea CIERTA.**

**QUE HACER:**

1. Una guarda que, **para cada ruta que el reporte publique con cifra de bytes**,
   **recomputa las DOS convenciones desde el disco** (bytes en disco y bytes
   normalizados a LF) **y las coteja contra las dos publicadas**.
2. **Cae en ROJO si alguna de las dos discrepa**, nombrando **la ruta, la cifra
   publicada, la medida y cual de las dos convenciones falla**.
3. **REUSA lo que `scripts/loop/vuelta186_rutas_del_reporte.py` ya sabe hacer**,
   que es exactamente esta medicion. **Una sede, dos llamadores, y NO un
   tercero.** Si hay que separar una funcion para conseguirlo, se separa.
4. **Funciones PURAS sobre el texto y sobre un mapa de mediciones**, para que el
   arnes las pueda tumbar sin tocar el repo; **un solo lector toca disco**.
5. **Una ruta que no existe sigue siendo el rojo que ya es**, y **el hueco
   declarado de la seccion 9 sigue siendo su excepcion**: esto no lo toca.
6. Cablearla donde `cerrar_reporte.py` juzga, **sin aflojar ninguna guarda que ya
   este ahi**, y **sin bandera**: lo que se computa no se teclea.

**ARNES OBLIGATORIO**, `scripts/loop/vuelta187_tarea4_mutacion_dos_convenciones.py`,
con **estos casos como minimo, todos cayendo al mutar su esperado**: las dos
convenciones calzando (verde); **la de LF mutada** (rojo, nombrando LF); **la de
disco mutada** (rojo, nombrando disco); una ruta con **CRLF real en disco** donde
las dos cifras son legitimamente distintas (verde, y es el caso que impide que la
guarda exija que sean iguales); una cifra publicada **sin pareja** (sigue siendo
el rojo de hoy, con su texto de hoy); y **UN CASO SOBRE EL TEXTO REAL DE
`git show bb3aaad3:docs/loop/REPORTE.md`** que exija que la guarda **HABRIA
CAZADO LAS CUATRO CIFRAS DE LA `C.1`**, nombrandolas. **Ese ultimo es la prueba
de la escalada: si no caza el caso que la trajo, no sirve.**

---

## TAREA 5. LA NOMINA, LA DECLARACION DEL 184 Y EL CIERRE

### 5.a LOS CUATRO ARNESES DE LA 186 ENTRAN EN LA NOMINA, MAS LOS QUE NAZCAN HOY

**ES LA RESPUESTA A LA `P.3` Y ES UNA CAIDA YA MEDIDA CON DOS VUELTAS DE
ANTELACION.** `arneses_que_faltan()` devuelve hoy **exactamente cuatro**:

- `scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py`
- `scripts/loop/vuelta186_tarea2b_mutacion_pieza2_cercas.py`
- `scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py`
- `scripts/loop/vuelta186_tarea2d_mutacion_seccion4.py`

**La bateria es la 189 y quedan dos vueltas. Sin ellos abre en rojo.** Metelos en
**la sede que la propia funcion consulta**, **mas los que nazcan en esta vuelta**,
y **la prueba es que `arneses_que_faltan()` devuelva 0** al cerrar, con su salida
pegada y con **el tamano de la nomina antes y despues**. **NO SE PODA NADA**: la
opcion `c` del 5 sep esta RECHAZADA por el fundador. Si al meterlos ves que algo
sobra, **paras y lo traes**.

**Y CORRE CADA ARNES NUEVO DOS VECES EN PROCESOS APARTE**, exigiendo el mismo
`sha256` las dos veces. Si alguno cambia solo, **paras y lo traes sin
arreglarlo**.

### 5.b LA DECLARACION DEL DEFECTO DEL REPORTE DE LA 184. ES LA `P.2`

**ADJUDICADO EN EL ACTA 187, PUNTO 7.2, POR EXTENSION DE LA `7.2` DEL ACTA 186**
(*"ni se eximen ni se reescriben, se declaran"*).

**LA PREGUNTA DEL EJECUTOR DE LA 186 PARTIA DE UNA PREMISA FALSA Y ESTA MEDIDO:**
`docs/loop/SALIDA_V184_APERTURA.txt` **existe y mide 34194 bytes**, y publica
`status 2` y `numstat 0`. **El rojo no es por falta de apertura.** Corrido hoy
por el auditor:

    seccion4_que_no_calza(REPORTE_V184.md, SALIDA_V184_APERTURA.txt)
    ->  CIFRA motivos en rojo: 1
        "LA SECCION 4 DEL REPORTE NO AFIRMA NADA sobre 'CIFRA lineas de status'."

**QUE HACER:**

1. **En el carril de CIERRE TARDIO, la guarda de la `2.d` NO bloquea, pero SE
   DECLARA** dentro del propio reporte cerrado, con **su motivo entero**, igual
   que se declaran las cifras sin pareja. **En el carril NORMAL sigue bloqueando
   entera, y eso lo exige el arnes, no la vista.**
2. **`REPORTE_V184.md` NO SE REABRE Y NO SE REESCRIBE SU SECCION 4.** Lo que se
   le anade es **la declaracion del defecto**, por la via que el carril tardio ya
   tiene. **Reescribir su seccion 4 seria escribir en pasado lo que no paso.**
3. **Ninguna otra guarda se afloja.** Si al escribirlo ves que hace falta aflojar
   algo mas, **paras y lo traes**.

**ARNES PROPIO OBLIGATORIO**,
`scripts/loop/vuelta187_tarea5b_mutacion_seccion4_tardio.py`, con estos casos,
todos cayendo al mutar su esperado: la seccion 4 muda **en carril NORMAL**
(bloquea); **la misma en carril TARDIO** (no bloquea **y aparece declarada en el
texto**, cotejada por contencion); **cero motivos en carril tardio** (la
declaracion dice cero y no se omite); y **un caso sobre los ficheros REALES del
184** que exija **1 motivo** y que **la declaracion lo nombre**.

### 5.c LA CIFRA INUTIL DEL BLOQUE H.5, QUE EL PROPIO EJECUTOR DECLARO

El bloque de apertura de la 186 conto los puestos de las ciegas con el patron
`PUESTO` en mayusculas cuando las ciegas los escriben como `puesto_intra`, y
**publico 0 puestos para cuatro ficheros**. **No movio ninguna decision y el
ejecutor lo declaro**, que es la conducta correcta. **Reparalo aqui**: que el
bloque cuente con el patron que las ciegas usan de verdad, y **publica la cifra
antes y despues** para que se vea que dejo de ser cero.

### 5.d EL REPORTE DE LA 187 SE ABRE, SE LLENA Y SE CIERRA

- **El esqueleto** se talla **en la apertura**, con sus **cinco filas vacias**,
  una por tarea. **Cada tarea anexa su fila al cerrarse**, no al final.
- **La cabecera se talla con `scripts/loop/tallar_cabecera_reporte.py`**, y antes
  del commit `--comparar docs/loop/REPORTE.md` tiene que dar **CABECERA IDENTICA
  AL TALLADOR**, con su salida citada. **Cero celdas tecleadas.**
- **El desfase de calibrado se mide en la APERTURA**, antes de la primera
  operacion. **Una columna de apertura medida al cierre es caida que ACUMULA.**
- **LA SECCION 4 SE ESCRIBE CON LAS CIFRAS QUE LA GUARDA DE LA `2.d` LEE DE LA
  APERTURA**, no con las que recuerdes.
- **LA SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO**: nombre, bytes medidos
  y atribucion, **las tres juntas**, y la atribucion dice que la siguiente vuelta
  de bateria es la **189**.
- **`scripts/loop/cerrar_reporte.py --vuelta 187`** y despues
  **`archivar_reporte.py --vuelta 187`**.

---

## LAS GUARDAS QUE NO SE TOCAN EN ESTA VUELTA

- **`git diff --numstat -- dataset/`** se mide **al entrar y al salir** y **las
  dos cifras se publican**. El `numstat` es la vara, no el `git status`.
- **El `sha256` LF de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` es
  `ea6e850d331d14f0` al abrir.** Al cerrar **tiene que ser el mismo SALVO que la
  TAREA 2 mueva algo**, y en ese caso **la diferencia se explica par por par**.
  **Computalo, no lo copies.**
- **El ciclo de Gate 0 entero**, en su orden, con las suites en verde: 25/25 del
  motor, `tsc` exit 0, y la web en 82 ficheros y 1.040 tests.
- **Los clones declarados de esta vuelta se cotejan** y su salida se cita. **No
  afirmes que ningun diff sale vacio: publica lo que salga.**
- **Todo tamano de fichero va en BYTES EXACTOS leidos del instrumento** (`P.2`),
  nunca redondeado, los KB solo entre parentesis y detras del byte, **y con SUS
  DOS CONVENCIONES MEDIDAS Y NO SUPUESTAS**. La `C.1` de la 186 nacio exactamente
  ahi, y **la TAREA 4 de esta vuelta pone la guarda que lo caza**: si la escribes
  mal, tu propia tarea te tumba el cierre.
- **Toda ruta que publiques como evidencia de una corrida es CIFRA** (5 sep 2026):
  si apunta a un fichero inexistente o de cero bytes, es **caida de cifra**.
  **Compruebalo antes de escribirla.**
- **Marca tus discutibles ANTES de saber si aciertas**, y **si alguno es de CLASE
  y no de metodo, dilo**. **El `D.6` de la 186 fue un buen discutible de clase y
  el acta 187 lo dice: sigue asi.**

## LO QUE HAY QUE TRAER SIN RESOLVER SI APARECE

Si **cualquier arnes YA SELLADO** cae en rojo, **te detienes ahi, lo traes con su
salida entera, sin re-correrlo y sin arreglarlo**. **Un arnes que nace en esta
vuelta y todavia no ha sellado ninguna salida es otra cosa** (adjudicacion `5.2`
del acta 186): su rojo es parte de escribirlo, lo reparas, **y pegas la corrida en
rojo entera en el reporte con el motivo dentro del propio fichero**. Si el texto
de alguna de estas letras no alcanza para ejecutarla sin decidir, **eso es PARADA
y no una improvisacion**: paras y lo traes.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No adivines.
