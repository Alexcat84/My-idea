### TAREA 3 (TAREA 1 DEL ENCARGO DE LA CONTINUACION). LOS REGISTROS Y LA CORRECCION DE LA ATRIBUCION

> **LA FILA ENTRA COMO TAREA 3 Y SE DICE POR QUE.** El encargo de la
> continuacion la llama TAREA 1, pero la tabla de este reporte YA tiene una
> TAREA 1 cerrada (la de la primera sesion) y una TAREA 2 abierta que es la
> misma bateria que la TAREA 2 de hoy. Renumerar la tabla o reusar la fila de la
> TAREA 1 seria pisar trabajo ya cerrado y ya auditado. La fila se abrio VACIA
> con `scripts/loop/_v183b_abrir_fila_tarea3.py` **antes** de anexar nada, que
> es lo que `EJECUTOR.md` 1 pide, y su salida cuenta **3 filas de tarea en la
> tabla**.

**3.a. EL ACTA 183 ENTERA, REGISTRADA COMO `R.45`.** Instrumento
`scripts/loop/vuelta183b_tarea1a_registrar_acta183.py`, salida
`docs/loop/SALIDA_V183_T1A_REGISTRO_R45.txt` (**3.487 bytes en disco y 3.487
bytes normalizados a LF, 68 lineas**). El numero lo devolvio
`serie_de_registros.siguiente_libre()` y **no se tecleo**: la serie recomputada
de sus dos sedes daba **36 entradas, 0 colisiones y 0 huecos**, y el siguiente
libre **R.45**. Tras escribir: **37 entradas, 0 colisiones y 0 huecos**, y el
siguiente libre pasa a **R.46**. `docs/PENDIENTES.md` pasa de **862.331 bytes** a
**871.284 bytes**. La entrada mide **8.952 bytes y 98 lineas**, se releyo del
disco byte a byte y trae **0 guiones largos o medios**.

**LOS TRES NUMERALES DEL TITULO SE CONTARON DEL ACTA ACOTADA** (lineas 63.682 a
64.048, 367 lineas): **7 adjudicaciones** (`5.1` a `5.7`, lineas 63883, 63924,
63933, 63944, 63956, 63964 y 63971), **0 caidas propias del auditor** y **1 caida
del ejecutor** (`E.1`, linea 63883).

**HIZO FALTA CODIGO PROPIO OTRA VEZ, Y ESTA MEDIDO EN VEZ DE SUPUESTO**, por tres
cosas distintas y las tres con su cifra de contraste al lado. **UNA:** el acta 182
numeraba `7.n` y **el acta 183 numera `5.n`**; corrido el prefijo `7.` de la
vuelta pasada sobre esta acta, da **0**, porque su seccion 7 es la metrica de
credito. **DOS:** el acta 182 escribia la caida del ejecutor como ``**`E.1`.`` al
principio de linea y **el acta 183 la escribe DENTRO DEL TITULO de su primera
adjudicacion**; el patron viejo, corrido sobre esta acta, cuenta **0**. **TRES, y
es la que importa:** las caidas propias del auditor son **CERO**, y un cero que
sale de un patron que no muerde no es evidencia de nada. El instrumento **exige
ademas que el acta lo declare con todas las letras** y publica la linea:
**63726**, *"NINGUNA CAIDA PROPIA ESTA VUELTA, Y DECLARO EL METODO QUE LA EVITO
PORQUE ESTUVE A UN PASO DE UNA"*. **Si el patron diera cero y el acta no lo
declarara, el instrumento haria PARADA en vez de escribir la entrada**, y ese
caso esta probado en el arnes.

**LA DEUDA DE LA SERIE SE REMIDE EN ESTA VUELTA Y NO SE HEREDA DEL `R.44`:** **8
actas sin entrada propia, las 173 a 180**, con sus dos extremos **`R.42`, que
cubre el acta 172**, y **`R.43`, que cubre el acta 181**. **Sigue documentada como
salto y sin rellenar.**

**CASO POSITIVO POR MUTACION VERDE**, salida
`docs/loop/SALIDA_V183_T1A_MUTACION_REGISTRO_183.txt` (**3.181 bytes en disco y
3.181 bytes normalizados a LF, 55 lineas**), **0 fallos**: 4 actas fabricadas con
cifras distintas y los contadores calzan con las cuatro; el esperado mutado
**CAE**; el patron de caida del ejecutor del acta 182 sobre un acta en forma 183
da **CERO**; el prefijo `7.` sobre un acta que numera `5.n` da **CERO**; el
instrumento **distingue el cero declarado del cero sin declarar** (1 linea de
declaracion contra 0); y el numeral **cero** entra en el titulo con su
concordancia y no esta clavado.

**3.b. LA CORRECCION DEL `E.1`, QUE ES LA OPERACION DE CODIGO DE ESTA VUELTA.**
Adjudicacion 5.1 del acta 183. **LO QUE PASABA ANTES NO SE BORRA, SE CUENTA, Y SE
CONTO ANTES DE TOCAR NADA:** el bloque **H.2** de
`docs/loop/SALIDA_V183B_APERTURA.txt` (**30.531 bytes, 474 lineas**) conto **3
lineas con `176` en cada una de las cuatro salidas selladas, 12 en total**, con
sus numeros de linea y su texto.

**LAS TRES ESPECIES DE MENCION, SEPARADAS, PORQUE NO TODAS SON FALSAS.** De las
tres de cada fichero: en las dos salidas de bateria, **dos son atribucion falsa**
(las lineas 1 y 2, *"BATERIA DE LA VUELTA 176"* y *"lanzada por
scripts/loop/vuelta176_bateria_por_tramos.py"*) y **una es CITA HISTORICA
legitima** (la linea 21, *"EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c)"*, que
nombra de donde salio la regla y **vive en `verificar_mutaciones_viejas.py:1872`,
que no es el lanzador**). En las dos salidas de lanzador, **las tres son falsas**:
la linea 4 y los dos prefijos de `mkdtemp` que salen impresos en la ruta del
fichero temporal. **La cuenta de despues no baja a cero y se dice por que.**

**LA REPARACION NO ES TECLEAR UN 183 ENCIMA DEL 176.** Un 183 tecleado se hereda
igual que se heredo el 176. En `scripts/loop/vuelta183_bateria_por_tramos.py`
(**23.847 bytes en git al abrir, 539 lineas**), `LANZADOR` sale de
`os.path.basename(os.path.abspath(__file__))` y `VUELTA` de un `re.match` sobre
ese nombre, **y el modulo se niega a cargarse si el nombre no dice su vuelta**. De
ahi salen ahora, por **cuatro funciones PURAS** (`titulo_de_corrida`,
`linea_de_lanzador`, `titulo_de_composicion`, `linea_de_composicion`) y tres de
nombre (`nombre_tramo`, `nombre_transcripcion`, `nombre_de_la_compuesta`): las dos
primeras lineas de cada salida sellada (lineas 217 y 218 del encargo), la cabecera
de la composicion (359 y 360), la linea del titulo del tramo (181), **los dos
prefijos de `mkdtemp` que el encargo no nombraba** (198 y 516) y las dos rutas que
`--siguiente` y `--componer` imprimen. **El numero de tramos tampoco se teclea:
sale de `len(tramos)`.**

**Y EL GUARDA, QUE ES LA MITAD QUE IMPIDE QUE VUELVA A PASAR:**
`literales_de_vuelta_clavados()`, **pura**, corre en `main()` **sobre el fuente de
su propio modulo** y **el lanzador NO ARRANCA** si encuentra uno. Las citas
historicas se eximen **NOMBRANDOLAS** con la marca `CITA HISTORICA`, no
ensanchando el patron. Corrido hoy sobre el fuente real: **0 literales clavados**,
y esa linea sale impresa en la transcripcion sellada de cada tramo.

**EL CASO POSITIVO ES POR MUTACION SOBRE VARIABLE COMPUTADA, QUE ES LO QUE EL
ENCARGO PIDE.** Arnes `scripts/loop/vuelta183_tarea1b_mutacion_atribucion.py`,
salida `docs/loop/SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt` (**6.782 bytes en disco
y 6.782 bytes normalizados a LF, 116 lineas**), **0 fallos**, y **las dos corridas
seguidas salen identicas byte a byte**, que es lo que la doble corrida de la
bateria va a exigirle. El clon: el fuente REAL copiado a un
`vuelta777_bateria_por_tramos.py`, importado, y **todo lo que ese clon sellaria
dice 777**. La mutacion: el mismo clon con `VUELTA` clavado a mano, y **el arnes
CAE en los tres casos** (no computa su numero, sella con el numero de otra vuelta
y su primera linea miente). Y el remate: **el clon con un literal clavado en un
`print` corrido como PROCESO devuelve exitcode 1** y dice en rojo cual linea lo
clava, contra **exitcode 0** del clon sano.

**EL ARNES TUMBO AL GUARDA DOS VECES ANTES DE QUE NADIE LO DIERA POR BUENO, Y ESO
NO SE ESCONDE.** La primera version del patron pedia `V` mayuscula sin separador,
y el arnes la caza con **dos casos que el defecto REAL de esta vuelta traia**: el
prefijo `v176_tramo` de los `mkdtemp`, que va en minuscula, y la frase *"de la
vuelta 176"*, que lleva espacio. **Las dos salieron impresas en las salidas
selladas y el patron no las veia.** Se ensancho **una vez**, con la medicion
delante y escrita en el comentario del propio patron.

**LA NOMINA CRECE DE 111 A 112 Y NO SE PODA NADA.** El arnes entra por la regla
del acta 176 punto 7.2, que la `D.4` del acta 182 reconfirmo y la `5.4` del acta
183 volvio a conceder. **Medido antes de anadirlo:** `arneses_que_faltan()` daba
**ultima vuelta 183, faltan 1**, y ese uno era este arnes; **con el fuera,
`hay_rojo_al_cierre()` habria cerrado en ROJO los siete tramos que quedan**.
Remedido despues: `arneses_que_faltan()` **0**, `nomina_invisible_al_censo()`
**0**, `guarda_del_sujeto_congelado()` **0**, y el reparto sigue dando **NUEVE
tramos** con **suma 112** y tamanos **13, 13, 13, 13, 13, 13, 13, 13, 8**. **Los
ocho primeros tramos no se mueven: el que crece es el noveno**, de 7 a 8 entradas.

**3.c. LOS TRAMOS 1 Y 2 SE VUELVEN A CORRER, Y VA EN LA TAREA 2.** El regimen
`6.1` pide que los nueve tengan salida sellada **DEL MISMO CALIBRE**, y dos
salidas que se atribuyen otra vuelta no son del mismo calibre que siete que se
atribuyen bien. **El coste esta medido y no estimado:** los dos tramos costaron
**2,1 y 5,6 minutos** en su primera corrida (commits `ede210b2` y `34f7ef7f`),
o sea **7,7 minutos**, sobre una bateria que el `--plan` de hoy estima entre
**36,6 y 47,7 minutos** para la nomina entera. **No contradice "lo corrido queda
corrido":** esa regla protege el trabajo cuando la vuelta se corta, no una salida
sellada que dice de que vuelta es y se equivoca.

**3.d. LAS RUTAS DE LA CELDA DE PRUEBA DE LA TAREA 1, ESCRITAS ENTERAS.**
Adjudicacion 5.2 del acta 183, que las adjudica **a favor del ejecutor** y aun asi
encarga escribirlas enteras, por el motivo que ella misma da: una ruta que hay que
reconstruir mentalmente no se puede cotejar pegandola en un comando. **El encargo
nombra tres y se corrigen CUATRO:** la primera, `SALIDA_V183_T1A_REGISTRO_R44.txt`,
tampoco llevaba su carpeta. Las cuatro se comprobaron una a una antes de
escribirlas, que es lo que la regla del 5 sep manda: **4.498, 2.310, 7.681 y
12.375 bytes**, ninguna ausente y ninguna en cero.

**3.e. EL TALLADOR DEL CIERRE ENTRA A GIT Y NO SE BORRA.** Adjudicacion 5.6.
`scripts/loop/_v183_tallar_cierre.py`, **18.855 bytes**, medido en el bloque F del
bloque de apertura cuando todavia estaba sin seguir, commiteado con el bloque de
apertura en `da1ad513`.

**3.f. LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 183.** Instrumento
`scripts/loop/vuelta183b_tarea1f_relectura_al_doble.py`, clon declarado del de la
TAREA 1.e, salida `docs/loop/SALIDA_V183_T1F_RELECTURA_AL_DOBLE.txt` (**12.050
bytes en disco y 12.050 bytes normalizados a LF, 144 lineas**). **EL COTEJO VA
ANTES DE LEER UN SOLO PUESTO Y CALZA:** `SELLO_APERTURA_AUDITOR_V184.json` (658
bytes) declara **43.593 bytes** y `sha256`
`217077af6ea96a1862a692f81abae6393bd87b7587e14d8bd6e21003408ba9f9`, y el fichero
de hoy mide **43.593 bytes** con **ese mismo `sha256`**. **Si no calzaran, no se
releeria nada y la salida lo diria.**

**30 puestos del tramo + 30 vecinos deterministas = 60**, solape entre tramo y
vecinos **0**, solape con la ciega inmediatamente anterior
(`_auditor_v183_ciega_blind.txt`, 30 puestos) **0**. **60 releidos: 4 declaran
diferenciador, 0 tienen LESION EXACTA y 0 tienen un nodo muerto.** Reparto por
clase de los 60: **A 7, B 1, D 52**. El puesto **660**, que es la unica
discrepancia del auditor, esta **dentro** del universo releido: clase **B**,
declara diferenciador **SI**, lesion **no**. **Ninguna clase se vuelve a decidir:**
`vecinos()` se importa del instrumento de la 182 y la vara de
`vuelta182_tarea3_diferenciador_movido.py`; lo que la vara no ve, la salida no lo
afirma.

> **UNA COSA QUE EL ENCARGO NO DICE Y SE DECLARA EN VEZ DE CALLARLA.** El encargo
> manda leer los 30 de `_auditor_v184_ciega_blind.txt`, y ahi estan; pero la
> **seccion 4 del acta 183**, que es la de la ciega, **no lista ninguno de los
> 30** (parseada, devuelve **0**): publica el reparto por clase y la unica
> discrepancia. Se dice para que nadie busque los 30 en el acta y crea que
> faltan.

**LOS DOS COTEJOS DE CLON DECLARADO, PEGADOS CON LO QUE SALGA Y SIN PROMETER QUE
SALDRIAN VACIOS.** El bloque de apertura de esta continuacion contra el de la
primera sesion (`docs/loop/SALIDA_V183_T1B_COTEJO_CLON_APERTURA.txt`, **37.617
bytes en disco y 37.004 normalizados a LF**): **DIFIERE en los cuatro veredictos**,
con **5.535 nodos de arbol contra 4.852** y **42 tipos de nodo que no empatan**. El
instrumento de la relectura contra el de la TAREA 1.e
(`docs/loop/SALIDA_V183_T1F_COTEJO_CLON.txt`, **7.878 bytes en disco y 7.755
normalizados a LF**): **DIFIERE en los cuatro**, con **2.089 nodos contra 2.104** y
**17 tipos que no empatan**. Los dos docstrings anunciaron que no saldrian
identicos y ninguno de los dos lo prometio.
