## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Las compone
`scripts/loop/_v210_cierre.py` leyendolas de los ficheros de salida de la
vuelta, y **cae en rojo si no puede leer una** o si encuentra mas de una
coincidencia. Es la letra de `EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO.

### 3.1. LA UNICA TAREA, CADA CIFRA CON EL FICHERO DEL QUE SALE

| que se midio | cifra | fichero de salida |
|---|---:|---|
| entradas de la nomina, congelada por `AUDITOR.md` 6.3 | **135** | `SALIDA_V210_T1A_PLAN.txt` |
| tamano de tramo, y tramos del reparto | **13** y **11** | `SALIDA_V210_T1A_PLAN.txt` |
| tramos que `--siguiente` decia que FALTABAN antes de correr nada | **0** | `SALIDA_V210_T1B_SIGUIENTE_ANTES.txt` |
| entradas corridas sumadas de los once tramos | **135** | `SALIDA_V210_T1E_TABLAS.txt` |
| reparto de veredictos: OK, CASO DECLARADO y NO MORDIO | **126**, **2** y **7** | `SALIDA_V210_T1E_TABLAS.txt` |
| suma de las tres clases | **135** | `SALIDA_V210_T1E_TABLAS.txt` |
| tramos con exitcode distinto de 1 | **0** | `SALIDA_V210_T1E_TABLAS.txt` |
| tramos con RUIDO DE CONCURRENCIA distinto de cero | **0** | `SALIDA_V210_T1E_TABLAS.txt` |
| tramos cuyo commit nombra la VUELTA 210, y los que nombran otra | **11 de 11** y **0** | `SALIDA_V210_T1E_TABLAS.txt` |
| minutos sumados de los once tramos | **23.4** | `SALIDA_V210_T1E_TABLAS.txt` |
| entradas sin correr, ajenas y repetidas segun `--componer` | **0**, **0** y **0** | `SALIDA_V210_T1D_COMPONER.txt` |

**LA SALIDA UNICA DE LA BATERIA**, remedida al cierre por
`scripts/loop/_v210_tabla_tramos.py` y no copiada de `--componer`. **Las dos
convenciones van en la misma linea, y los dos `sha256` tambien**, que es como
esta casa publica una pareja:

- `docs/loop/SALIDA_V183_BATERIA.txt`: **93499 bytes en disco y 93499 bytes normalizado a LF**, **1433 lineas**.
- `docs/loop/SALIDA_V183_BATERIA.txt`: **sha256 disco `68e7505d560634c3` y sha256 LF `68e7505d560634c3`**.

**EL MARCADOR DEL CRIBADO NO SE MOVIO Y ESA GLOSA LLEVA SU CORTE:** esta vuelta
**no adjudica ninguna clase** y **no toca `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**,
medido con `git diff --numstat` al cierre en la tabla de la seccion 4. La vuelta
de bateria no lleva trabajo de plan al lado, que es la letra de `AUDITOR.md` 6.1.

### 3.2. EL CICLO ENTERO DE GATE 0, CORRIDO POR MI Y NUNCA `run_phase1.py` A SECAS

Los ocho comandos en su orden, con `scripts/loop/_v210_ciclo_gate0.py`, que
**IMPORTA** `_v205_ciclo_gate0.py` y solo le cambia el numero de vuelta, que
computa de su propio nombre. **IMPORTAR NO ES CLONAR** (acta 206 `6.5`).
**El lado APERTURA se corrio ANTES del primer tramo y el lado CIERRE despues del
ultimo**, que es la `C.5` de la 209 remediada.

| que | cifra | fichero de salida |
|---|---:|---|
| peor `EXITCODE` de los ocho, en los dos lados | **0** | las ocho salidas `SALIDA_V210_*_CIERRE.txt` |
| censo del grafo: nodos, activos y deprecados | **3853**, **3169** y **684** | `SALIDA_V210_GATE0_CMD1_CIERRE.txt` |
| Gate 0: auto-aristas, duplicadas de titulo y divergentes | **0**, **0** y **0** | `SALIDA_V210_GATE0_CMD1_CIERRE.txt` |
| aristas: siguientes, previas, suma y union | **8780**, **8740**, **17520** y **9914** | `SALIDA_V210_CONTEO_CIERRE.txt` |
| desfase del calibrado | **4** filas | `SALIDA_V210_DESFASE_CALIBRADO_CIERRE.txt` |
| tests del motor | **25** de **25** | `SALIDA_V210_MOTOR_CIERRE.txt` |
| web: ficheros de test y tests | **82 (82)** y **1040 (1040)** | `SALIDA_V210_WEB_CIERRE.txt` |
| `npx tsc --noEmit` | **EXIT 0** | `SALIDA_V210_TSC_CIERRE.txt` |
| filas de `git diff HEAD --numstat` tras correr el ciclo | **0** | `SALIDA_V210_CICLO_NUMSTAT_CIERRE.txt` |

**LAS 4 FILAS DEL DESFASE SON LAS MISMAS DE SIEMPRE**, y esa glosa
lleva su corte: son las cuatro que el ciclo de la vuelta 209 ya listaba en su
propia salida, **remedidas hoy en el lado CIERRE de esta vuelta** y no heredadas.

## 4. LO QUE SE TOCO, Y LO QUE NO

**ESTA TABLA SE RECOMPUTA AL CIERRE Y NO SE HEREDA DE LA APERTURA**
(`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE).

**Mi apertura sellada, `docs/loop/SALIDA_V210_APERTURA.txt`, publica con
`git status --porcelain` 1 lineas al entrar, y con
`git diff --numstat -- dataset/` AL ENTRAR: 0 filas.** Las dos se
LEEN de la apertura sellada y no se teclean.

**Y RECOMPUTADAS AL CIERRE POR MI, CON LOS MISMOS DOS COMANDOS: 8
y 0.**

| sede | filas de `numstat` al cierre | por que |
|---|---:|---|
| `dataset/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `web/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `engine/` | **0** | esta vuelta no toca nodos ni codigo de producto |
| `docs/plan/` | **0** | la vuelta de bateria no lleva trabajo de plan al lado |

**LO QUE SI SE MOVIO SON LAS SALIDAS DE LA BATERIA Y LOS FICHEROS DE COMPUTO DE
LA VUELTA**, y todo va committeado tramo a tramo. **`docs/plan/` no se toca en
ninguna de sus filas**, que es lo que `AUDITOR.md` 6.1 pide de una vuelta de
bateria: los dos campos `estado` de `OP-L-02` y `OP-L-03` y la ficha `OP-I-01`
que el acta 209 adjudica **esperan a la 211**.

### 4.1. LA MORATORIA, MEDIDA CON SU CORTE LEIDO Y NO TECLEADO

**AQUI VA APLICADA LA UNICA CAIDA QUE EL ACTA 209 ME CUENTA, Y NO SOLO CITADA.**
Su `4.1` midio que mi glosa nombraba *el commit de la TAREA 3* mientras la cifra
salia de un commit de cierre. **La causa estaba en el codigo**: el computo iba
contra el `HEAD` vivo y la frase que lo nombraba estaba TECLEADA. En
`scripts/loop/_v210_cierre.py` la funcion `moratoria()` devuelve **la cifra y
el `HEAD` contra el que la midio en la misma tupla**, y la frase de abajo se
compone con ese `HEAD`: **no hay forma de nombrar un corte distinto del medido.**

**CIFRA ficheros anadidos a `scripts/loop/` entre `e3d33e42` y `2cc9eb38`,
que es el `HEAD` que este mismo computo leyo y no uno tecleado: 10, de
los que 10 llevan el prefijo `_v210_` y 0 no lo llevan.**

**ESTA CIFRA NACE CORTA POR CONSTRUCCION Y LO DIGO DENTRO DE LA MISMA FRASE:**
`scripts/loop/_v210_cierre.py` es el fichero que cuenta, va en el commit del
cierre, y **ese commit todavia no existe cuando el conteo corre**. Falta por
tanto **este mismo fichero** y cualquiera que nazca despues de `2cc9eb38`.
**No se arregla el instrumento, que es moratoria**: se escribe la glosa con su
corte, y el corte es el que la frase nombra.

**LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135**, recomputada
importando su fuente y no tecleada, y **el lanzador
`scripts/loop/vuelta183_bateria_por_tramos.py` no se clono ni se toco**: su
`sha256` de disco y de LF al entrar estan en mi apertura sellada.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. RE CORRI EL TRAMO 4 EN VEZ DE PUBLICARLO CON SU `RUIDO DE
CONCURRENCIA` EN 2 Y DEJARLO.** El propio instrumento dice de esa cifra que
*"NO son de nadie y NO son rojo de nadie"*, o sea que la letra escrita **no me
obligaba a re correr**: podia haber publicado el tramo 4 tal cual, con su ruido
declarado, y seguir. Elegi re correrlo solo, y su ruido bajo de 2 a
**0** en los once.
**Por donde me puedo estar equivocando:** re correr un tramo que la letra admite
es gastar reloj y, peor, **es una decision mia que ninguna regla me manda**, y
esta casa castiga al que se inventa severidad tanto como al que afloja. La
objecion contraria es que el ruido de ese tramo no venia de un fichero cualquiera
sino de **otra corrida de la misma bateria cerrandose encima**, que es la cosa
exacta que `AUDITOR.md` 6.1 quiere evitar cuando dice que la bateria **se corre
sola**. **Si el auditor lee que bastaba con declararlo, el tramo 4 viejo esta
entero en el commit `3fa5b035` y su cifra sigue siendo leible.**

**`D.2`. PUBLICO LOS SIETE `NO MORDIO` SIN DIAGNOSTICAR NINGUNO.** Son siete
guardas de la nomina que ya no tumban lo que decian tumbar, y las dejo nombradas
con su tramo y nada mas.
**Por donde me puedo estar equivocando:** puede que **una guarda que no muerde
sea una CAIDA DE DATO** y que la moratoria, que exceptua justamente *"lo que una
CAIDA DE DATO exija, con su cita"*, me estuviera pidiendo abrir al menos una y
medir por que. Lo que me sostiene es que el acta 205 ya nombro cinco de estas
mismas y **no las adjudico como caida de dato sino como hallazgo que sube**, y
que abrir siete arneses y sus siete sujetos es maquinaria de la que la moratoria
me saca. **Marco el punto y no lo defiendo mas.**

**`D.3`. USO EL CARRIL DE LA BATERIA CONTINUADA DE `cerrar_reporte.py` SABIENDO
QUE SU ARNES NO MUERDE.** Mi salida compuesta se llama `SALIDA_V183_BATERIA.txt`
porque el lanzador computa su vuelta de su propio nombre, asi que
`rama_de_la_seccion9()` la juzga por el carril de la **bateria continuada**, y
`vuelta185_tarea1c_mutacion_bateria_continuada.py`, que es el arnes de ese
carril, sale **NO MORDIO** en el tramo 9 de esta misma corrida.
**Por donde me puedo estar equivocando:** cerrar por un carril cuya guarda esta
apagada es cerrar sin red, y se podria defender que hay que parar hasta que esa
guarda vuelva a morder. Lo que me sostiene es que **el carril lo abre la
evidencia de `git log`, no el arnes**: `tramos_por_vuelta()` lee de los commits
que los once tramos los sello la VUELTA 210, y esa evidencia **no se puede
teclear**. Aun asi **lo declaro antes de pasar por el**, que es lo unico que
puedo hacer sin tocar maquinaria.

## 6. LAS PREGUNTAS

**`P.1`. SIETE GUARDAS QUE NO MUERDEN, SON UNA CAIDA DE DATO O NO?** Es el `D.2`
puesto como pregunta general y va a volver a pasar cada cinco vueltas. La
moratoria de `AUDITOR.md` 6.3 exceptua *"lo que una CAIDA DE DATO exija, con su
cita"*. **Una entrada de la nomina que sale `NO MORDIO` entra en esa excepcion, o
se acumula hasta la auditoria integral?** Yo no lo decido.

**`P.2`. UN TRAMO CON `RUIDO DE CONCURRENCIA` DISTINTO DE CERO, SE RE CORRE O SE
DECLARA?** Es el `D.1` puesto como pregunta general. El instrumento dice que el
ruido **no es rojo de nadie**, pero no dice que hacer cuando el ruido lo produce
**otra corrida de la misma bateria**. Una letra general me ahorra decidirlo cada
cinco vueltas.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`. UN PROCESO LANZADO EN SEGUNDO PLANO CUYO LOG QUEDA EN CERO BYTES NO
ESTA MUERTO, Y ESTA CASA NO TIENE ESCRITO COMO COMPROBARLO.** Me paso en esta
misma vuelta y es mi `C.1`: di por muerto un tramo porque su log medía cero
bytes, lo relance, y los dos corrieron a la vez. **La letra vigente dice que una
SALIDA SELLADA de cero bytes no cuenta como hecha, y esa letra es buena; lo que
no existe es la hermana: un LOG de cero bytes NO prueba que el proceso murio.**
El remedio que use no cuesta codigo nuevo: **preguntar por el proceso, no por su
log**, antes de relanzar nada. Lo dejo como PENDIENTE DE DOCTRINA y **no lo
convierto en regla yo**.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. DI POR MUERTO UN TRAMO VIVO Y CORRI DOS BATERIAS A LA VEZ.** Lance el
tramo 3 con un `nohup ... &` dentro de un shell que se cierra al devolver, vi su
log en cero bytes y lo di por muerto. **No lo estaba.** Relance, y hubo dos
corridas del tramo 3 solapadas: la primera de `04:10:51Z` a `04:21:39Z` y la
segunda empezada a `04:20:42Z`, **cincuenta y siete segundos antes de que la
primera terminara**. Committee la primera, y la segunda me la piso despues.
**Quien me cazo fue la guarda de concurrencia del propio instrumento**, que
publico `RUIDO DE CONCURRENCIA: 2 fichero(s)` en la salida del tramo 4. **El
remedio fue correr, no narrar:** comprobe con `ps` que no quedaba proceso vivo y
re corri los tramos 3 y 4 solos, los dos con ruido en cero. **El commit
`e72a22b9` y el `3fa5b035` quedan enteros en la historia y no se reescriben:
decian la verdad de lo que habian medido.** Cuenta como UNA caida, no como tres.

**`C.2`. EL PRIMER INTENTO DE ESCRIBIR EL ESQUELETO MURIO EN EL SHELL Y NO EN EL
JUICIO.** El fichero `_v210_esqueleto.py` se escribio a la segunda porque el
primer intento se fue por una comilla del propio `heredoc`, no por nada del
esqueleto. **No toco ninguna cifra ni ningun fichero del repo** y lo digo porque
la casa cuenta las caidas, no solo las que dejan rastro.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**La 211 no es de bateria** (la cadencia de cinco pone la siguiente en la 215) y
el trabajo de plan que el acta 209 deja adjudicado esta esperando: el campo
`estado` de **`OP-L-02`** a `HECHA` con las tres guardas del `2.c` de la 209, el
de **`OP-L-03`** puesto al dia por el mismo carril y en el mismo computo, y
**`OP-I-01`**, que es la ultima de las cuatro fichas reales de la moratoria y no
se ha empezado. **Y los siete `NO MORDIO` de esta bateria necesitan una
adjudicacion**, que es mi `P.1`.
