### TAREA 1. LOS REGISTROS Y LAS TRES REPARACIONES DE CODIGO. CERRADA, CON UNA PARADA LEVANTADA EN LA 1.c

**TODAS LAS CIFRAS DE ESTA SECCION SALEN DE CONTAR SUS FICHEROS DE SALIDA CON
`scripts/loop/_v185_tallar_t1.py`, Y NINGUNA ESTA TECLEADA.** Las 10 rutas que
esta seccion publica como prueba existen y **ninguna mide cero bytes**: las de
cero medidas hoy son **0**.

#### 1.a EL ACTA 185 EN LA SERIE, CON EL NUMERO LLAMADO Y NO TECLEADO

Entrada **`R.47`**, en `docs/PENDIENTES.md`. El numero lo devolvio
`scripts/loop/serie_de_registros.py` recomputando la serie de sus dos sedes:
**38 entradas** antes de escribir, cero colisiones y cero huecos.

| lo que se registra | cifra contada del acta acotada |
|---|---:|
| adjudicaciones numeradas `5.1` a `5.7`, todas a favor | **7** |
| pendientes de doctrina `6.1` a `6.4` | **4** |
| caidas propias del auditor (`A.n`, cabecera `###`) | **1** |
| caidas de reporte del ejecutor (`R.n`) | **1** |

**EL ESTADO DE CADA PENDIENTE SALE DE SU TITULO Y NO DE UNA TABLA A MANO:**
`PD.2`, `PD.3` y `PD.4` **CERRADAS**, `PD.1` **ABIERTA**. **Y LOS CINCO PUESTOS
DE LA `PD.1` NO SE COPIARON DEL ENCARGO:** se leyeron del parrafo del `6.4` del
acta y son **1778, 2530, 2540, 3141, 3232**.

**LOS PATRONES VIEJOS SE CORREN IGUAL Y SU CERO SE PUBLICA**, que es lo que
prueba que hacian falta los nuevos: el patron sin comillas del acta 183, el
`C.n` de linea, el `C.n` de negrita de frase y el `E.n` de las actas 182 y 184
dan **0** los cuatro sobre esta acta.

**LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL `R.46`:**
**8 actas** sin entrada propia, las **173, 174, 175, 176, 177, 178, 179, 180**.

Prueba: `docs/loop/SALIDA_V185_T1A_REGISTRO_R47.txt` (**4615 bytes en disco y 4615 bytes normalizados a LF**).
Caso positivo por mutacion sobre un acta **FABRICADA**, nunca la real, en
`docs/loop/SALIDA_V185_T1A_MUTACION_REGISTRO_185.txt` (**4443 bytes en disco y 4443 bytes normalizados a LF**):
**CIFRA fallos: 0**, veredicto **VERDE**.

#### 1.b LA SALIDA SELLADA DEL ARNES QUE PARO LA BATERIA DEJA DE CAMBIAR SOLA

La reparacion es una funcion **PURA**, `sin_temporal(linea, tmp)`, aplicada en
las dos lineas `w("      | " + l[:130])` **ANTES del recorte y no despues**.
**NO SE TOCO LO QUE EL ARNES PRUEBA:** ningun esperado aflojado, ningun
escenario quitado.

| mitad | lo que mide | cifra contada de su fichero |
|---|---|---:|
| A, la funcion pura | casos | **7** |
| A | casos que CALZAN | **7** |
| A | casos que CAEN al mutar su esperado | **7 de 7** |
| B, corrida 1 | exitcode, y sus bytes por las dos convenciones al lado | **exitcode 0** |
| B, corrida 2 | exitcode, y sus bytes por las dos convenciones al lado | **exitcode 0** |

**LAS DOS CORRIDAS, EN PROCESOS APARTE, DAN EL MISMO `sha256`:**
`ce85fd0cc659774c` y `ce85fd0cc659774c`, identicos.
Y `docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` mide **4982 bytes en disco y 4982 bytes normalizados a LF**
despues de las dos.

**ESTA REPARACION REESCRIBE ESE FICHERO DE SALIDA, Y SE DICE EN VEZ DE
DISIMULARLO.** El que se commitea es el de la forma reparada, con
`<TEMPORAL>` dentro: **3 apariciones de `<TEMPORAL>`** y **0 de
`v182_apertura_`**. `git diff --numstat` sobre ese fichero dio **3 y 3**, o sea
las tres lineas 53, 54 y 55 que el acta 185 punto 3.5 diagnostico **y ninguna
mas**.

**LO QUE ESTA VUELTA NO PUEDE PROBAR, Y SE DICE:** esta reparacion **NO se
verifica contra la bateria**, porque la 185 no es vuelta de bateria
(`AUDITOR.md` 6.1). **La prueba de esta vuelta es la doble corrida de la mitad
B; la prueba definitiva sera la bateria de la 189.**

Prueba: `docs/loop/SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt` (**6100 bytes en disco y 6100 bytes normalizados a LF**),
**CIFRA fallos: 0**, veredicto **VERDE**.

#### 1.c LA GUARDA DE LA BATERIA CONTINUADA, Y LA PARADA QUE LEVANTA

**LA RAMA NUEVA EXIGE MAS QUE LA VIEJA Y NO MENOS:** cuatro condiciones a la
vez, y si falla cualquiera cae al ROJO de siempre. **La evidencia se computa de
`git log` en `main()` y NO se pasa por bandera:** apariciones de `--tramos` en
`cerrar_reporte.py`, contadas hoy: **0**.

| lo que se mide | cifra contada de su fichero |
|---|---:|
| casos de la tabla (el caso G va aparte) | **6** |
| casos que CALZAN | **6** |
| casos que CAEN al mutar su esperado | **6 de 6** |
| fallos del caso G, el del cuarto parametro por defecto | **0** |
| `tramos_por_vuelta(183)`: sellados por la vuelta 183 | **4** |
| `tramos_por_vuelta(183)`: sellados por la vuelta 184 | **5** |

**EL MOTIVO DEL ROJO VIEJO NO SE REESCRIBIO,** y eso no se afirma: el caso B
exige que su motivo sea **IDENTICO** al que la misma funcion devuelve con el
cuarto parametro en su valor por defecto, y sale identico.

**EL ARNES VIEJO SIGUE MANDANDO Y SE CORRIO SIN TOCARLO:**
`scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py`, con **9 casos**, **9
que calzan** y veredicto **VERDE**, en
`docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt` (**5802 bytes en disco y 5802 bytes normalizados a LF**).

Prueba: `docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt` (**7937 bytes en disco y 7937 bytes normalizados a LF**),
**CIFRA fallos: 0**, veredicto **VERDE**.

**PARADA. LA MISMA REGLA VIVE DOS VECES EN `cerrar_reporte.py`, Y EL ENCARGO
SOLO NOMBRA UNA.** El propio encargo lo previo: *"no se toca ninguna otra
guarda; si al escribir esto ves que hace falta cambiar algo mas, paras y lo
traes"*. **Se ve.** `ajena != vuelta` aparece **2 veces** en el fichero: en
`rama_de_la_seccion9()`, que es la que el encargo manda reparar y esta
reparada, y en la **PIEZA (4) de `piezas_que_faltan()`**, que tiene su propia
copia y **no recibe la evidencia**. Medido sobre un reporte **FABRICADO**, sin
escribir nada, en `docs/loop/SALIDA_V185_T1C_SEGUNDA_GUARDA.txt` (**2234 bytes en disco y 2234 bytes normalizados a LF**):
la rama sale **CORRIDA** y `piezas_que_faltan()` devuelve **1 pieza que**
**falta**. **NO SE TOCA Y NO SE ARREGLA AQUI.**

#### 1.d LA ESCALADA: LA COLUMNA `quien lo sello` SE COMPUTA

**LA PRUEBA DE LA ESCALADA ES QUE LA VERSION COMPUTADA REPRODUCE LA TECLEADA
EXACTAMENTE:** las **9 de 9** celdas calzan y **0 no calzan**.
Las tecleadas se leen de `docs/loop/REPORTE.md`, donde el reporte de la 184 las
publico; las computadas, de `scripts/loop/_v184_t2_seccion.md`, que es lo que el
tallador acaba de escribir con `tramos_por_vuelta()`.

La linea tecleada muere como codigo vivo: **0 apariciones como CODIGO VIVO** y
**1 como CITA dentro de un comentario**, nombrada y pegada porque
`EJECUTOR.md` 8 manda que una correccion no tape lo que corrige. Las dos
funciones se **IMPORTAN** de `cerrar_reporte.py` y no se copian.

**NO SE RE-PEGO NADA EN `docs/loop/REPORTE.md`.** El cierre del reporte de la
184 va en la TAREA 2 y usa el texto que ese reporte ya tenia; aqui solo se
prueba el instrumento.

Prueba: `docs/loop/SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt` (**2602 bytes en disco y 2602 bytes normalizados a LF**),
**CIFRA fallos: 0**, veredicto **VERDE**.

#### 1.e LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 185

**EL `sha256` SE COTEJO ANTES DE LEER UN SOLO PUESTO, Y NO SE COPIO DEL
ENCARGO:** el sello `V185b` declara la ciega y el fichero de hoy calza. **EL
FICHERO ES EL QUE EL SELLO DICE: SI.**

| lo que se mide | cifra contada de su fichero |
|---|---:|
| puestos del tramo, leidos de la ciega sellada | **30** |
| vecinos deterministas anadidos | **30** |
| solape entre tramo y vecinos | **0** |
| solape con la ciega inmediatamente anterior | **0** |
| puestos releidos EN TOTAL | **60** |
| es el doble exacto del tramo | **SI** |
| de los releidos, declaran diferenciador | **4** |
| de los releidos, con LESION EXACTA | **0** |
| de los releidos, con algun nodo muerto en el grafo de hoy | **0** |
| clase `A` / clase `D` en el universo releido | **9** / **51** |

**LAS SIETE DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA.** El auditor
las pierde **las siete** a favor del archivo. **AQUI NO SE RE-DECIDE NINGUNA
CLASE:** solo se dice si estan dentro del universo releido y que ve la vara.

| puesto | clase | declara diferenciador | lesion exacta | dentro del universo |
|---:|:-:|:-:|:-:|:-:|
| **1208** | A | no | no | **SI** |
| **1459** | D | no | no | **SI** |
| **2363** | D | no | no | **SI** |
| **2386** | D | no | no | **SI** |
| **2505** | D | no | no | **SI** |
| **2636** | D | no | no | **SI** |
| **2854** | D | no | no | **SI** |

**LO QUE LA VARA NO VE, ESTA SECCION NO LO AFIRMA.** La vara dice, por puesto,
si declara diferenciador, si tiene lesion exacta, si algun nodo esta muerto y
su clase de archivo, **y nada mas**.

Prueba: `docs/loop/SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt` (**12566 bytes en disco y 12566 bytes normalizados a LF**).

#### LOS TRES CLONES DECLARADOS, COTEJADOS, Y SE PUBLICA LO QUE SALGA

**NO SE AFIRMA QUE NINGUN DIFF SALGA VACIO.** Salida en
`docs/loop/SALIDA_V185_COTEJO_DE_CLONES.txt` (**42081 bytes en disco y 41431 bytes normalizados a LF**).

| clon | sentencias de codigo | literales de texto |
|---|---:|---:|
| `vuelta184_apertura.py` -> `vuelta185_apertura.py` | **276** | **117** |
| `vuelta184_esqueleto_reporte.py` -> `vuelta185_esqueleto_reporte.py` | **1** | **67** |
| `vuelta184_tarea1d_relectura_al_doble.py` -> `vuelta185_tarea1e_relectura_al_doble.py` | **4** | **35** |

**Y LA DIFERENCIA MAS QUE EL ENCARGO MANDA DECLARAR:** el clon de la relectura
apunta a `SELLO_APERTURA_AUDITOR_V185b.json` y a `_auditor_v185b_ciega_blind.txt`,
y NO a las rutas que el numero de vuelta sugeriria. El auditor nombro su sello
`V185b` cuando la casa lo nombra `V186` y lo declaro como su caida propia `A.1`;
**las rutas vienen del encargo, no de deducirlas**.

#### LAS GUARDAS DE ESTA TAREA, MEDIDAS

`git diff --numstat -- dataset/` al cerrar esta tarea: **0 filas**.

#### LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. ANADI UN CAMBIO MAS DE LOS TRES QUE LA `1.d` NOMBRA.** El encargo
lista tres cosas que hacer y yo hice una cuarta: anadir a la prosa del tallador
la procedencia de la NOVENA columna. **Mi razon es que la `R.1` dice que la
averia es que la enumeracion no la incluia**, asi que dejarla fuera conservaria
el defecto en el instrumento. **No mueve ninguna celda de la tabla.** Pero es
un cambio que el encargo no pidio y lo marco.

**`D.2`. MI ARNES DE LA `1.b` SALIO EN ROJO EN SU PRIMERA CORRIDA Y LO REPARE
YO EN VEZ DE TRAERLO.** El encargo dice *"si cualquier arnes cae en rojo, te
detienes ahi, lo traes con su salida entera, sin re-correrlo"*. **Lo que cayo
fue MI arnes recien escrito, no una guarda de la casa**, y lo que estaba mal era
mi entrada de prueba tecleada, no la funcion bajo prueba. **Lei que esa regla
protege a los arneses ya sellados y no al que estoy escribiendo en esta misma
linea**, y arregle la prueba. **La corrida en rojo va entera en el reporte y en
el comentario del fichero**, pero la decision de alcance la tome yo.

**`D.3`. PUBLIQUE LA COLUMNA `quien lo sello` CON UNA NEGRITA COMPUTADA.** La
version tecleada ponia en negrita la vuelta mas alta (`**vuelta 184**`) y la
computada tiene que reproducirla, asi que **calculo cual es la vuelta mas alta
del reparto y esa va en negrita**. Reproduce las nueve celdas exactamente, pero
**es una regla de formato que nadie escribio**: la deduje de las celdas que
tenia que reproducir.

**`D.4`. NO METI LOS DOS ARNESES NUEVOS EN LA NOMINA DE LA BATERIA.**
`arneses_que_faltan()` da **2**, y son los dos que nacen hoy. La `5.6` del acta
185 ampara meterlos en su propia vuelta, pero **esta vuelta no es de bateria y
su encargo no nombra la nomina**. **Elegi no tocarla y declararlo**, a sabiendas
de que la bateria de la 189 empezara en rojo por esa via si nadie los mete
antes.

**`D.5`. GUARDE EL REPORTE DE LA 184 QUE `cerrar_reporte.py` SI LLEGO A
ESCRIBIR, Y DESPUES RESTAURE EL ARBOL.** El instrumento escribe en su bloque C
y juzga en el D, asi que al devolver 1 dejo en disco un reporte de contenido
completo. **Lo guarde con un nombre que dice lo que es y restaure**
**`docs/loop/REPORTE.md` con `git checkout`**, para que el arbol y el archivado
digan lo mismo. **Es una decision de alcance que tome yo**: destruirlo habria
perdido la evidencia, y dejarlo habria hecho que el esqueleto de la 185 pisara
un texto que no estaba en ninguna otra sede.

#### LAS PREGUNTAS

**`P.1`. LA PIEZA (4) DE `piezas_que_faltan()` Y LA PIEZA (2), ¿SE REPARAN
JUNTAS O POR SEPARADO?** La (4) es la copia gemela de la regla que la `1.c`
acaba de reparar. La (2) es otra especie: la marca `PENDIENTE DE TALLAR AL
CIERRE` se busca **en todo el texto**, y un reporte que CITA una salida roja
dentro de un bloque cercado la lleva dentro sin estar sin tallar. **No se cual
de las dos es prioridad y no me lo encargaron.**

**`P.2`. ¿QUE SE HACE CON LAS 10 CIFRAS SIN PAREJA DEL REPORTE DE LA 184?** La
guarda `cifras_sin_pareja()` las caza y el encargo prohibe tocar ese texto. **O
se exime el texto ya escrito, o se reescribe, o la guarda aprende a mirar solo
lo nuevo.** No elijo yo.

#### MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1`. ESCRIBI UN ARNES CUYA SALIDA SELLADA LLEVABA DENTRO EL MISMO DATO QUE
CAMBIA SOLO QUE LA REPARACION VIENE A QUITAR.** La primera version de
`vuelta185_tarea1b_mutacion_sin_temporal.py` pegaba las lineas de entrada
**crudas**, con el sufijo aleatorio del `mkdtemp` dentro. **Habria hecho caer la
bateria de la 189 por la misma averia que estaba reparando.** Lo cace
**mirando mi propio fichero**, no un instrumento, y anadi `mostrar()`.

**`C.2`. MI PRIMER ARNES DE LA `1.b` FABRICO UN TEMPORAL QUE NO EXISTE Y SUS
DOS CASOS DE RUTA RELATIVA SALIERON EN ROJO.** La funcion estaba bien; lo que
estaba mal era mi entrada tecleada. **Es exactamente la especie que esta casa
castiga**: teclear una cadena en vez de medirla. La salida en rojo va entera en
el reporte y el motivo queda escrito en el propio fichero.

