### TAREA 1. LOS REGISTROS. **CERRADA. `R.57` ESCRITA, IDEMPOTENCIA PROBADA EN BYTES, Y EL LECTOR TUVO QUE CAMBIAR TRES VECES PORQUE EL ACTA CAMBIO DE FORMA.**

**EL NUMERO DE LA ENTRADA NO SE TECLEA.** `scripts/loop/serie_de_registros.py`,
corrido en el bloque `G` de la apertura y otra vez dentro del registrador, da
**`SIGUIENTE LIBRE: R.57`** sobre **48 entradas** y **0 colisiones**. El encargo
adelanta `R.57` y **el instrumento dice `R.57`: CALZA**. Tras escribir, la serie
recomputada da **49 entradas, siguiente libre `R.58`, 0 colisiones y 0 huecos**.

#### 1.a LO QUE SE CONTO DEL CUERPO ACOTADO DEL ACTA, Y NINGUNA DEL ENCARGO

Acta 195 acotada en `docs/loop/ACTA_AUDITOR.md`, **lineas 68709 a 69017**, o sea
**309 lineas**. Secciones leidas y no tecleadas: **0, 1, 2, 3, 4, 5, 6, 7 y 8**.
Todo lo de abajo sale de `docs/loop/SALIDA_V195_T1A_REGISTRO_R57.txt`.

| lo que se cuenta | cifra | como se leyo |
|---|---:|---|
| adjudicaciones `4.1` a `4.10` | **10** | patron entrecomillado (el del acta 184) |
| las mismas, con el patron suelto (el del acta 189) | **0** | se publica aunque sea cero |
| de ellas, discutibles del ejecutor | **7** | familia leida del titulo |
| de ellas, preguntas contestadas | **3** | `P.1`, `P.2`, `P.3` |
| discutibles **A FAVOR** | **7** | estado leido del titulo |
| discutibles **EN CONTRA** | **0** | **y es la QUINTA acta seguida** |
| hallazgos de la seccion 5 | **3** | `claves_entrecomilladas` |
| caidas propias del auditor, del CUERPO de la seccion 3 | **1** | `C.1`, linea 68832 |
| caidas del ejecutor, de reporte | **0** | fila de la tabla |
| caidas del ejecutor, de cifra publicada | **0** | fila de la tabla |
| caidas del ejecutor, de metodo | **0** | fila de la tabla |
| actas sin entrada propia en la serie (173 a 194) | **8** | 173 a 180, remedido aqui |

**EL CERO DE `EN CONTRA` NO SE VUELVE A PROBAR POR MUTACION: SE DICE CON SU
FICHERO.** `docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt` mide **6904
bytes** en disco y **6904** por LF, y su veredicto, leido del propio fichero, es
`'VEREDICTO: VERDE'`. La guarda vieja de la 190 corrida sobre esta acta
**PARARIA**, y esa es la medicion que dice que el cero es un resultado y no un
descuido.

**LA RACHA DE REPORTE VUELVE A CERO**, leida de la celda derecha de su propia fila
y no supuesta: **`racha de reporte: 0`**. El acta lo dice expresamente y el
registrador **PARA si esa celda no publica la racha**, para que un cero no se
pueda teclear. **No hay escalada que encargar.**

#### 1.b EL LECTOR TUVO QUE CAMBIAR TRES VECES, Y LAS TRES CON SU CIFRA DELANTE

**Esto no es cosmetica: sin los tres cambios el registrador PARA, y con ellos mal
hechos registra una cifra falsa.** Los tres son ANADIDOS y no ensanches, que es la
diferencia que el acta 184 adjudico a favor en su `5.3`: **ninguna marca vieja se
retira ni se recorta, el lector heredado corre PRIMERO y entero, y la cifra de lo
que el heredado daria se publica al lado.**

**1. LA FILA DE LAS CAIDAS PROPIAS DEL AUDITOR VIENE PARTIDA EN DOS, Y LA AGUJA
VIEJA CASA CON LAS DOS.** El acta escribe `caidas propias del auditor QUE
ACUMULAN` (**0**) y `caidas propias del auditor, TOTAL del cuerpo` (**1**). La
aguja corta que usaba el registrador de la 194 (`caidas propias del auditor`) casa
sobre esta acta con **2 filas**, y quien se quedara con `[0]` **registraria 0
donde el cuerpo declara 1**. `filas_de_las_propias()` lee las dos con su aguja
larga, publica las dos y **coteja contra la del TOTAL**, que es la que mide lo
mismo que el cuerpo: **1 contra 1, CALZA**.

**Y esto merece decirse entero, porque es lo contrario de una rareza: la fila
partida ES EL REMEDIO DEL HALLAZGO `5.1` DEL PROPIO ACTA APLICADO A SU MISMA TABLA
EN LA VUELTA EN QUE LO LEVANTA.** El `5.1` denuncia que la fila del acta 194 decia
*"caidas propias del auditor: 1"* cuando su cuerpo declaraba dos, porque contaba
solo las que acumulan. **Un registrador que no cambiara habria repetido esa misma
confusion desde el otro lado.**

**2. LA FILA DE METODO ESCRIBE `**0 nuevas**` Y EL LECTOR HEREDADO NO LA LEE.**
`R92.numeral_de_la_fila` busca `**<digitos>**` pegados y devuelve `None` sobre esa
celda, o sea que el registrador **PARARIA por una fila que SI trae su cifra y solo
la acompana de un adjetivo**. `numeral_de_la_fila_195()` la lee y da **0**, sin
cambiar lo que el heredado ya leia y **sin dejar de dar `None` ante una celda de
verdad muda**.

**3. DOS ESTADOS DE ADJUDICACION QUE EL VOCABULARIO NO TENIA.** La `4.8` cierra
con *"CONTESTADA, y la respuesta corrige a mi predecesor, no al ejecutor"* y la
`4.10` con *"CONTESTADA, con las dos mitades"*. **Con el vocabulario heredado
entero saldrian `SIN DECIR` 2 adjudicaciones y el registrador PARARIA**, cifra
publicada en la propia salida. Las dos marcas nuevas son **literales del acta**,
no parafrasis.

**Y EN SENTIDO CONTRARIO, UN LECTOR QUE ESTA VUELTA NO HACE FALTA Y NO SE
RETIRA:** `hallazgos_en_titular()`, que la 194 tuvo que anadir porque su acta
titulaba con `###`, **da CERO sobre el acta 195**, que vuelve a la negrita de
apertura de parrafo. Los tres lectores se corren y las tres cifras se publican:
`claves_entrecomilladas` **3**, `claves_de_adjudicacion` **0**,
`hallazgos_en_titular` **0**. **Retirarlo estrecharia el vocabulario a la forma del
acta de hoy, y la proxima que titule con `###` haria PARAR el instrumento.**

#### 1.c LA EXIGENCIA QUE SE HACE CONDICIONAL, Y LA RAMA QUE SIGUE ENTERA

La fila de puestos del acta 195 dice **`30 aislados, 30 cotejados, CERO
quemados`** y **no publica un segundo cotejo**. El registrador de la 194 exigia
SIEMPRE `cotejo limpio va sobre N` y **sobre esta acta PARARIA**. Con **CERO**
quemados **no hay dos cotejos que publicar**, asi que el acta escribe uno solo, y
eso es correcto.

**LA EXIGENCIA SE HACE CONDICIONAL A QUE HAYA QUEMADOS, Y EN ESA RAMA SIGUE
ENTERA:** si los hubiera y faltara el segundo cotejo, el registrador para igual.
**Lo que se estrecha es el caso, no la guarda**, y `quemados_son_cero(None)`
devuelve `False` a proposito: **si no se pudo leer, no se supone que sean cero**.

**Y LA CIFRA DE CERO QUEMADOS TIENE CAUSA MEDIDA, QUE ES LO QUE EL ENCARGO MANDA
REGISTRAR:** la 194 midio **once**, y la diferencia es que **los mensajes de commit
del ejecutor ya no publican clases por puesto ni el reparto de una ciega**. **Eso
funciono, y se registra como lo que es: un remedio a mano que midio.** Su guarda de
codigo sigue pendiente y va nombrada en lo que queda fuera.

#### 1.d LAS TRES PREGUNTAS, CONTESTADAS, Y LO QUE CADA UNA ADJUDICA

| clave | pregunta | estado leido del titulo |
|---|---|---|
| `4.8` | `P.1` | CONTESTADA, y la respuesta corrige al predecesor del auditor |
| `4.9` | `P.2` | CONTESTADA A FAVOR POR EXTENSION CITABLE |
| `4.10` | `P.3` | CONTESTADA con las dos mitades: corrida SI, verde NO |

**LA `4.9` ES LA QUE ABRE LA TAREA 3 DE ESTA VUELTA** y la `4.10` la TAREA 4.
**Registrar no es adjudicar**, y esta seccion solo deja escrito lo que el acta
dice.

#### 1.e EL CASO POSITIVO POR MUTACION, Y LA IDEMPOTENCIA PROBADA EN BYTES

`--mutacion` corre sobre texto FABRICADO, con el valor esperado sacado de como se
fabrico el texto y no de una constante igual a la obtenida:
`docs/loop/SALIDA_V195_T1A_MUTACION_REGISTRADOR.txt`, **`CIFRA casos: 27 | pasan:
27 | fallan: 0`**, **`VEREDICTO: VERDE`**, contado de su propio fichero.

**Y CADA UNO DE LOS TRES CAMBIOS DE LECTOR LLEVA SU MUTACION, que es lo que los
separa de un adorno:** la aguja corta de la 194 tiene que casar con **DOS** filas
sobre la tabla fabricada y su primera tiene que ser el **0**; el heredado tiene que
devolver **`None`** sobre `**0 nuevas**` y **`SIN DECIR`** sobre los dos titulos
nuevos; y la guarda de la entrada tiene que **CAER** si la entrada se queda con una
sola mitad de la fila. **Si alguna de esas no cayera, el cambio no haria falta.**

**LA IDEMPOTENCIA NO SE AFIRMA: SE PRUEBA RE CORRIENDOLO, CON LA SEDE MEDIDA EN
BYTES.**

| momento | bytes de `docs/PENDIENTES.md` |
|---|---:|
| antes de escribir | **1039583** |
| despues de escribir `R.57` | **1050189** |
| **despues del RE CORRIDO** | **1050189** |

El re corrido escribio `docs/loop/SALIDA_V195_T1A_RECORRIDO_SIN_ESCRIBIR.txt` y
**no toco la sede**: el acta 195 aparece ya en **2 linea(s)** por sus dos marcas
literales, y **no se consumio el numero `R.58`**.
