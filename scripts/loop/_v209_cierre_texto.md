## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Las compone
`scripts/loop/_v209_cierre.py` leyendolas de los ficheros de salida de la
vuelta, y **cae en rojo si no puede leer una** o si encuentra mas de una
coincidencia. Es la letra de `EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU
FICHERO.

### 3.1. LAS TRES TAREAS, CADA CIFRA CON EL FICHERO DEL QUE SALE

| que se midio | cifra | fichero de salida |
|---|---:|---|
| crecimiento del acta 208, en bytes en disco y en bytes normalizado a LF | **28592** y **28592** | `SALIDA_V209_T1_REGISTROS.txt` |
| lineas anadidas al acta, y borradas | **443** y **0** | `SALIDA_V209_T1_REGISTROS.txt` |
| discrepancias con el contraste en el `1.a` | **0** | `SALIDA_V209_T1_REGISTROS.txt` |
| entradas de la serie `R.N`, a la entrada y a la salida | **64** y **65** | `SALIDA_V209_T1_REGISTROS.txt` |
| adjudicaciones medidas del acta 208, y de ellas las que cierran pendiente | **10** y **6** | `SALIDA_V209_T1_REGISTROS.txt` |
| crecimiento de `docs/PENDIENTES.md`, en bytes en disco y en bytes normalizado a LF | **10054** y **10054** | `SALIDA_V209_T1_REGISTROS.txt` |
| lineas de la entrada que faltan, en orden, en la salida | **0** | `SALIDA_V209_T1_REGISTROS.txt` |
| miembros y pares de la seleccion de canal, en LITERAL | **6** y **15** | `SALIDA_V209_T2A_DENOMINADOR.txt` |
| cobertura recomputada de esa nomina | **10 de 15** | `SALIDA_V209_T2A_DENOMINADOR.txt` |
| discrepancias con el contraste en el `2.a` | **0** | `SALIDA_V209_T2A_DENOMINADOR.txt` |
| guardas del `2.b` que fallan | **0** | `SALIDA_V209_T2B_CORRECCIONES.txt` |
| crecimiento de `docs/plan/LECTURAS_DIRIGIDAS.md`, en bytes en disco y en bytes normalizado a LF | **4262** y **4262** | `SALIDA_V209_T2B_CORRECCIONES.txt` |
| lineas de la entrada que faltan, en orden, en la salida | **0** | `SALIDA_V209_T2B_CORRECCIONES.txt` |
| lineas anadidas y borradas en `docs/plan/OPERACIONES.jsonl` | **1** y **1** | `SALIDA_V209_T2C_CERRAR_OPL01.txt` |
| fichas que se movieron, y otros `id_op` cuyo estado cambio | **1** y **0** | `SALIDA_V209_T2C_CERRAR_OPL01.txt` |
| puntos de la vara, DOCUMENTALES y NO DOCUMENTALES | **18**, **13** y **5** | `SALIDA_V209_T3A_VARA.txt` |
| citas de la vara que NO aparecen VERBATIM en su campo | **0** | `SALIDA_V209_T3A_VARA.txt` |
| discrepancias con el contraste en el `3.a` | **0** | `SALIDA_V209_T3A_VARA.txt` |
| veredictos del cotejo: CUBRE, A MEDIAS y NO CUBRE | **16**, **2** y **0** | `SALIDA_V209_T3_COTEJO.txt` |
| filas del cotejo SIN cita de fichero y linea | **0** | `SALIDA_V209_T3_COTEJO.txt` |
| rutas del corpus comprobadas, y de ellas las que fallan | **11** y **0** | `SALIDA_V209_T3_COTEJO.txt` |
| apariciones del barrido negativo, y fichas del control positivo | **0** y **47** | `SALIDA_V209_T3_COTEJO.txt` |

**EL MARCADOR DEL CRIBADO, RECOMPUTADO POR MI DEL ARCHIVO LINEA A LINEA:
3388 filas, A 551, B 72, C 5, D 2760.** Calza al digito con el sello del auditor
`docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json`. **Esta vuelta no lo movio:**
no adjudico ninguna clase y no toca `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.

### 3.2. EL CICLO ENTERO DE GATE 0, CORRIDO POR MI Y NUNCA `run_phase1.py` A SECAS

Los ocho comandos en su orden, con `scripts/loop/_v209_ciclo_gate0.py`, que
**IMPORTA** `_v205_ciclo_gate0.py` y solo le cambia el numero de vuelta, que
computa de su propio nombre. **IMPORTAR NO ES CLONAR** (acta 206 `6.5`).

| que | cifra | fichero de salida |
|---|---:|---|
| peor `EXITCODE` de los ocho | **0** | las ocho salidas `SALIDA_V209_*_CIERRE.txt` |
| censo del grafo: nodos, activos y deprecados | **3853**, **3169** y **684** | `SALIDA_V209_GATE0_CMD1_CIERRE.txt` |
| Gate 0: auto-aristas, duplicadas de titulo y divergentes | **0**, **0** y **0** | `SALIDA_V209_GATE0_CMD1_CIERRE.txt` |
| cobertura del componente principal | **100.0** | `SALIDA_V209_GATE0_CMD1_CIERRE.txt` |
| aristas: siguientes, previas, suma y union | **8780**, **8740**, **17520** y **9914** | `SALIDA_V209_CONTEO_CIERRE.txt` |
| desfase del calibrado | **4** filas | `SALIDA_V209_DESFASE_CALIBRADO_CIERRE.txt` |
| tests del motor | **25** de **25** | `SALIDA_V209_MOTOR_CIERRE.txt` |
| web: ficheros de test y tests | **82 (82)** y **1040 (1040)** | `SALIDA_V209_WEB_CIERRE.txt` |
| `npx tsc --noEmit` | **EXITCODE 0** | `SALIDA_V209_TSC_CIERRE.txt` |
| filas de `git diff HEAD --numstat` tras correr el ciclo | **0** | `SALIDA_V209_CICLO_NUMSTAT_CIERRE.txt` |

**LAS CUATRO FILAS DEL DESFASE SON LAS MISMAS CUATRO DE SIEMPRE**, y esa
glosa lleva su corte: son las que el ciclo de la vuelta 208 ya listaba en su
propia salida, medidas hoy **7 sep 2026** y no heredadas.

## 4. LO QUE SE TOCO, Y LO QUE NO

**ESTA TABLA SE RECOMPUTA AL CIERRE Y NO SE HEREDA DE LA APERTURA**
(`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE).

**Mi apertura sellada, `docs/loop/SALIDA_V209_APERTURA.txt`, publica con
`git status --porcelain` 1 linea al entrar, y con
`git diff --numstat -- dataset/` 0 filas al entrar.** Las dos se LEEN de la
apertura sellada y no se teclean.

**Y RECOMPUTADAS AL CIERRE POR MI, CON LOS MISMOS DOS COMANDOS: 1 y 0.**
La del estado del arbol baja de 1 a 1 **y la diferencia esta medida y no
es un misterio**: al abrir, la unica linea sin rastrear era el propio fichero
de mi sello de apertura, y al cerrar ya esta committeado con todo lo demas.
**La de `dataset/` no se mueve: sigue en 0 por los dos lados.**

| sede | filas de `git diff --numstat` al cierre | por que |
|---|---:|---|
| `dataset/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `web/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `engine/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `docs/plan/` | **0** | la mueve la TAREA 2, y su guarda la mide |

**LAS TRES SEDES DEL AUDITOR, CON EL CERO DISTINGUIDO:**

| sede | filas | que clase de cero es |
|---|---:|---|
| `docs/loop/ACTA_AUDITOR.md` | **0** | fichero PRESENTE y sin tocar por mi |
| `docs/loop/PROMPT_SIGUIENTE.md` | **0** | fichero PRESENTE y sin tocar por mi |
| `PARA_ALEXIS.md` | **0** | **CERO DE AUSENCIA DE FICHERO**, no de fichero vacio: no existe en disco |

**LO QUE SI SE MOVIO, Y CADA UNO CON SU GUARDA:** `docs/PENDIENTES.md`
(**167** anadidas y **0** borradas), `docs/plan/LECTURAS_DIRIGIDAS.md`
(**78** anadidas y **0** borradas) y `docs/plan/OPERACIONES.jsonl` (**1**
anadida y **1** borrada, una sola linea). **Los tres por adicion o por
cirugia de una linea, y los tres con su guarda corrida encima.**

### 4.1. LA MORATORIA, MEDIDA CON SU CORTE ESCRITO DENTRO DE LA GLOSA

**Y AQUI VA LA CAIDA DEL ACTA 208 CONTRA MI PREDECESOR, APLICADA COMO
REMEDIO Y NO SOLO CITADA.** Su `4.1` midio que la glosa de la moratoria de la
208 publicaba `16` ficheros **sin su corte** cuando el corte de cierre daba
`19`, y su `7.2` explica la causa: **el instrumento del cierre no puede
contarse a si mismo**, porque va en el mismo commit que cuenta. **No se
arregla el instrumento, que es moratoria**: se escribe la glosa con su corte.

**CIFRA ficheros anadidos a `scripts/loop/` entre `32fc0348` y `HEAD`, medido en
ESTE CORTE, que es el commit de la TAREA 3 y NO el commit de cierre: 19, de
los que 19 llevan el prefijo `_v209_` y 0 no lo llevan.**

**ESTA CIFRA NACE CORTA POR CONSTRUCCION Y LO DIGO AQUI, DENTRO DE LA MISMA
FRASE.** `scripts/loop/_v209_cierre.py` es el fichero que cuenta, va en el
commit del cierre, y **ese commit todavia no existe cuando el conteo corre**:
faltan por tanto **este mismo fichero** y cualquiera que nazca despues de
este corte. **El corte real de la cifra es el que la frase nombra**, no el
estado final de la vuelta, y quien quiera la cifra final tiene que recontar
desde `32fc0348` hasta el commit de cierre. **La nomina de la bateria sigue
CONGELADA en 135**, recomputada importando su fuente y no tecleada.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. ESCRIBI LA CELDA `antes` DE LA FILA CORREGIDA DE LA LINEA 291, Y EL
ACTA 208 SOLO ADJUDICO LA CELDA `despues`.** La `5.2` del acta 208 y el
encargo nombran *10 de 10, cobertura COMPLETA*, que vive en la celda
`despues`; pero la celda `antes` de esa misma fila decia *8 de 10* y llevaba
**el mismo denominador que el recomputo desmiente**. La escribi como **8 de
15**, con los mismos leidos de siempre sobre el denominador recomputado, y lo
declare dentro de la propia correccion.
**Por donde me puedo estar equivocando:** republicar en una fila corregida
una cifra que el encargo no me mando tocar es ensanchar el encargo por mi
cuenta, y la casa castiga eso. La objecion contraria es que dejar *8 de 10*
dentro de una fila que se publica HOY seria publicar a sabiendas una cifra
que mi propia medicion desmiente, en la misma fila y a dos celdas de la
buena. **Elegi corregirla y decirlo; si el auditor prefiere que la celda
`antes` se quede como estaba, se revierte por el mismo carril del `9.10`.**

**`D.2`. DI POR CUMPLIDO EL CRITERIO DE HECHO DE `OP-L-01` Y CERRE LA FICHA
CON UNA COBERTURA QUE SIGUE SIENDO INCOMPLETA.** La cobertura escrita es **10
de 15**, o sea que faltan pares por leer, y aun asi la ficha pasa a `HECHA`.
**Por donde me puedo estar equivocando:** cerrar una mesa cuya nomina no esta
cubierta entera puede leerse como cerrar en falso. Lo que me sostiene es que
el criterio de HECHO de la fila **06 MESAS** no pide cobertura completa, pide
*cada decision escrita con su motivo y su cobertura al lado*, y que la
adjudicacion `6.2` del acta 208 ya resolvio exactamente esto: el banco `9.26`
**contempla lo PROVISIONAL en vez de prohibirlo**. **Si el auditor lee que la
mesa no cierra hasta que la cobertura sea completa, el pase de `estado` se
revierte con el mismo computo que lo escribio, que publica el valor viejo.**

**`D.3`. PUSE `V.15` EN A MEDIAS Y NO EN CUBRE, TENIENDO LAS DOS CONVENCIONES
PUBLICADAS.** La `nota` de `OP-L-02` afirma que las seis nominas tienen
cobertura COMPLETA; en LITERAL se sostiene y en RESUELTA la NOMINA 2 da `0 de
0`. Como la adjudicacion `6.6` dice que **manda la LITERAL**, se podria
defender un CUBRE limpio.
**Por donde me puedo estar equivocando:** puede que este castigando una
afirmacion que la doctrina ya salva, y que un A MEDIAS con las dos cifras
escritas sea mas timido de lo que la casa pide. Lo que me hizo bajarla es que
*cobertura COMPLETA* es una afirmacion sobre el mundo de HOY, y hoy cinco de
los seis miembros de esa nomina estan fundidos: el CUBRE me parecia esconder
eso detras de una convencion. **Marco el punto y no lo defiendo mas.**

## 6. LAS PREGUNTAS

**`P.1`. LA CELDA `antes` DE UNA FILA CORREGIDA, LA ESCRIBO O LA DEJO?** Es el
`D.1` puesto como pregunta general, porque va a volver a pasar: cuando una
correccion por adicion republica una fila entera, **las celdas que el encargo
no nombra pero que llevan la misma cifra mala, se corrigen o se copian tal
cual?** Lo he resuelto corrigiendo y declarando; una letra general me ahorra
decidirlo cada vez.

**`P.2`. `OP-L-02` CIERRA CON 16 DE 18 Y DOS `A MEDIAS`, O NO?** Yo mido y
propongo, y la adjudicacion es del auditor (`3.d`). Los dos `A MEDIAS` estan
nombrados con su motivo y **no hay ningun `NO CUBRE`**.

**`P.3`. EL GRUPO DE LOS 126 DEL BACKLOG LLEVA MOTIVO O NO?** Mi `V.8` sale
**A MEDIAS** porque ese grupo trae su cuenta y su condicion (*esperan
destejido o cirugia*) pero **no un motivo propio escrito** como los otros
tres. Puede que la condicion CUENTE como motivo y entonces la `V.8` sea
CUBRE. No lo decido yo.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`. UNA GUARDA DE UNICIDAD SOBRE UN FICHERO CON DOS SUJETOS NO ES UNA
GUARDA DE IDENTIDAD, Y ESO NO ESTA ESCRITO EN NINGUN SITIO.** Me paso **dos
veces en esta misma vuelta** (mi `C.1`) y la especie es exacta: un patron que
exige *exactamente una coincidencia* sobre un fichero que habla de **dos
nominas** puede casar con la nomina equivocada y **pasar la guarda**. El
remedio que use no cuesta codigo nuevo: **acotar el trozo al sujeto antes de
preguntar**, y comprobar que el otro sujeto queda fuera. Lo dejo como
PENDIENTE DE DOCTRINA y **no lo convierto en regla yo**.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. LEI UNA CIFRA DE NOMINA DEL FICHERO ENTERO Y ME SALIO LA DE LA OTRA
NOMINA. DOS VECES.** En el `2.b` el patron de `fundidos` exigia una linea de
detalle detras; la seleccion de canal tiene **0** fundidos y por tanto
ninguna, asi que la unica coincidencia del fichero era **la de la junta
asesora, que tiene 2**. Iba a publicar que la seleccion de canal tiene dos
miembros fundidos cuando no tiene ninguno. En la seccion de la TAREA 2 volvi
a caer en lo mismo por otra puerta, publicando los **pares resueltos** de la
junta donde iba su **cuenta de fundidos**. **Las dos las cace yo y antes de
publicar**, y las dos las arregle acotando el trozo a su nomina en vez de
afinar el patron. Va como PENDIENTE DE DOCTRINA en el `PD.1`.

**`C.2`. PUBLIQUE `CIFRA puestos distintos: 1` SOBRE UN ARCHIVO DE 3388
PUESTOS.** El cotejo pedia el campo `puesto` y ese campo **no existe** en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que lo llama `puesto_intra`. La
lectura devolvia vacio en las **3388** filas, el conjunto se quedaba con un solo
valor y la salida publicaba un **1**. **Ese 1 no era una medicion: era el uno
de un patron roto**, que es justo lo que `EJECUTOR.md` 9 prohibe publicar como
hecho del mundo. **La cace antes de que llegara al reporte**, arregle el campo
y **deje una guarda** que comprueba que el campo se lee en todas las filas
**antes** de publicar la cifra, y que la declara NO COMPUTABLE si no.

**`C.3`. ELEGI UN LITERAL DE CONTROL QUE NO ESTABA EN SU FICHERO Y TIRE LA
VARA EN ROJO EN SU PRIMERA CORRIDA.** El control positivo de
`SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` era la palabra `marcador` y aparecia
**0** veces: ese fichero habla del marcador por su sede y su cifra y **nunca
escribe la palabra**. **El fichero no estaba mal: mi eleccion si.** Lo cambie
por `OP-L-02` y **lo declare dentro del propio sello, con el texto viejo sin
borrar**. No es una caida de dato, pero es una caida y no la escondo.

**`C.4`. EL PRIMER INTENTO DE ESCRIBIR UN COMPUTO CON UN HEREDOC SE ME CAYO
EN EL SHELL Y TUVE QUE VOLVER A ESCRIBIRLO ENTERO.** No movio ningun dato ni
dejo nada a medias en disco, pero costo una corrida y lo cuento porque la
casa cuenta las caidas propias, no solo las que ensucian una cifra.

**`C.5`. EL LADO APERTURA DEL CICLO DE GATE 0 Y LOS DOS SELLOS DE `HEAD`
NACIERON AL CIERRE, NO AL ABRIR.** El tallador de la cabecera los exige y
**ninguno de los tres existia** cuando la vuelta llego a cerrarse: los corri y
los escribi ahi mismo. **Es tardio y lo digo con su nombre**, que es la misma
especie que la `C.3` del reporte de la 208. **Y el tallador lo repite por su
cuenta en su celda de identidad**, sin que yo se lo pida: dice `sello
RECONSTRUIDO DESPUES` con el commit en que nacio.

**LO QUE SI SE SOSTIENE, MEDIDO Y NO ALEGADO.** El `HEAD` de apertura **no se
invento**: `docs/loop/SALIDA_V209_HEAD_APERTURA.txt` se escribio copiando el
literal `CIFRA HEAD de apertura` de mi propio sello
`docs/loop/SALIDA_V209_APERTURA.txt`, que si se escribio **antes de la primera
operacion**, y los dos dicen `32fc0348`. **El fichero es tardio; la cifra que
lleva, no.** Y lo que sostiene que las cifras de APERTURA del ciclo valgan es
que **el arbol contra el que corre no se movio entre los dos lados**: mi sello
publica `dataset/`, `web/` y `engine/` en **0** filas de `git diff --numstat`
al entrar, y el numstat del cierre las da en cero otra vez, con censo **3853**
y `nodos_siguientes` **8780** iguales por los dos lados.

**LO QUE NO SOSTIENE, Y NO ME LO CALLO:** una medicion tomada al cierre **no
es una medicion de apertura** por mucho que el arbol no se haya movido, y
`EJECUTOR.md` 1 lo dice sin matices. **La columna de apertura de mi cabecera
es, en rigor, una segunda corrida del cierre**, y quien la lea tiene que
saberlo. Por eso esta caida se cuenta entera y no como media.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

La **210** es **VUELTA DE BATERIA** por la cadencia de cinco (`AUDITOR.md`
6.1) y **no lleva nada al lado**. Con `OP-L-01` cerrada en esta vuelta y
`OP-L-03` en la 208, de las cuatro fichas reales de la moratoria quedan
**`OP-L-02`**, medida y a la espera de adjudicacion, y **`OP-I-01`**, sin
empezar.

