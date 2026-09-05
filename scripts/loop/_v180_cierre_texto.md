## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**NINGUN HASH SE TECLEA** (`EJECUTOR.md` 1, LA IDENTIDAD SE LEE DE GIT). Todo lo
de esta seccion sale de `docs/loop/SALIDA_V180_IDENTIDAD_CIERRE.txt`, que lo
compone con `git rev-list`, `git log` y `git diff` en esta misma vuelta.

| pieza | valor | de donde sale |
|---|---|---|
| sello de APERTURA | `d3240915e9943016d026302cad437c4567e45653` | `docs/loop/SALIDA_V180_HEAD_APERTURA.txt`, sellado antes de la primera operacion |
| sello de CIERRE | `e4f5248e2681630e2f88a8239d15f72384e9afe1` | `docs/loop/SALIDA_V180_HEAD_CIERRE.txt`, sellado tras la ultima operacion |
| commits entre los dos sellos | **7** | `git rev-list --count` |
| rutas tocadas entre los dos sellos | **81** | `git diff --name-only` |
| de esas, en `scripts/loop/` | **41** | contado de la misma salida |
| de esas, en `docs/loop/` | **39** | contado de la misma salida |
| de esas, en `docs/plan/` | **1** | contado de la misma salida |
| `git diff --numstat` sobre `dataset/`, `web/`, `engine/` entre sellos | **0 filas** | `git diff --numstat` |

**LOS SIETE COMMITS, UNO A UNO, leidos de `git log`:** `122ca81f` la apertura,
`27b39975` el esqueleto, `7aacaa47` la TAREA 1, `cbe0feb9` la TAREA 2, `7b0a1ef1`
la TAREA 3, `0d307320` la TAREA 4 y `e4f5248e` la TAREA 5. **El commit que lleva
este cierre no se puede nombrar aqui**, porque se crea despues de escribirlo.

**LA UNICA RUTA DE `docs/plan/` QUE SE TOCO ES `OP_L_03_TRIANGULOS.jsonl`**, con
`3` lineas mas y `3` menos, que son las tres filas cuyos lados cambian de etiqueta
en la TAREA 1. **Ninguna clase se movio**, comprobado por `sha256` dentro del
propio instrumento.

### 3.1 EL MARCADOR, RECOMPUTADO DEL ARCHIVO AL CIERRE

Contado de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en esta corrida
(`docs/loop/SALIDA_V180_RECOMPUTO_ARCHIVO_CIERRE.txt`; **el fichero NO se llama
`SALIDA_V180_MARCADOR_CIERRE.txt` a proposito**, porque ese nombre lo reserva
`tallar_cabecera_reporte.py` para las salidas del cribado y ocuparlo con otro
formato le rompe cinco celdas, medido en
`docs/loop/SALIDA_V180_TALLADOR_RECHAZO.txt`):

| total | A | B | C | D | huecos | duplicados |
|---:|---:|---:|---:|---:|---:|---:|
| **3.388** | **551** | **72** | **5** | **2.760** | **0** | **0** |

Puestos de **1 a 3.388**. El `sha256`, medido por las DOS convenciones y
identico en las dos: en disco `ea6e850d331d14f01db1186a54f4913fa72eb2560a354430c5e6d047ff0d02be` y normalizado a LF `ea6e850d331d14f01db1186a54f4913fa72eb2560a354430c5e6d047ff0d02be`.
Y sus bytes, tambien por las dos: `4.051.967` bytes en disco y `4.051.967` bytes
normalizados a LF. **Es el mismo `sha256` que el acta 179 publica en su 3.2**, y
esa identidad es la prueba independiente de que **esta vuelta no movio ni un
veredicto**: no era su trabajo y no lo hizo.

### 3.2 EL ESTADO DE LA NOMINA AL CIERRE, RECOMPUTADO AL CIERRE

**Se recomputa aqui y no se hereda de ninguna cifra de arriba**, que es lo que
`EJECUTOR.md` 1 manda desde la caida de la vuelta 28:

| cifra | apertura (HEAD `d3240915e994`) | **cierre (HEAD `e4f5248e2681`)** |
|---|---:|---:|
| arneses que el censo ve | 163 | **168** |
| entradas de la nomina | 103 | **108** |
| censo menos nomina | 60 | **60** |
| los que estan FUERA de la nomina | 60 | **60** |
| `arneses_que_faltan()` | 0 | **0** |
| entradas invisibles al censo | 0 | **0** |
| entradas con el sujeto SIN CONGELAR | **17** | **0** |

**El sello entero, tallado y no tecleado: `108 (corte: HEAD e4f5248e2681, nomina
contada en esta corrida)`.** La nomina crece en **cinco**: los cinco arneses que
esta vuelta escribe. **La resta calza en las dos puntas.**

### 3.3 LO QUE ESTA VUELTA DEJA CORRIENDO, Y ES LO QUE LA 181 VA A ENCONTRAR

| guarda | antes | despues |
|---|---|---|
| sujeto congelado, contra la nomina | **17 de 103**, ROJO | **0 de 108**, VERDE |
| sujeto congelado, en el rojo global de la bateria | **no estaba cableada** | **cableada, y probada por mutacion** |
| etiqueta de fuente falsa | **5 de 15** | **0 de 10** |
| cifras del backlog sin corte | **13** | **0** |
| barrido de cortes | **no existia** | **32 filas, 0 fallos** |

## 4. LA GUARDA DEL COMMIT, CORRIDA EN CADA COMMIT DE ESTA VUELTA

`scripts/loop/guarda_commit_dataset.py` se corrio **antes de cada uno de los
siete commits** y salio **VERDE las siete veces**, con **0 filas de
`git diff --numstat -- dataset/`, 0 ficheros nombrados por
`git status --porcelain -- dataset/` y 0 blobs de arbol divergentes del de HEAD**.

**`dataset/` no se toca en ninguna de las cinco tareas**, y el ciclo de Gate 0 lo
confirma en las dos puntas: `git diff HEAD --numstat -- dataset/ web/ engine/`
da **0 filas** en la apertura y **0 filas** en el cierre.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los marco ANTES de saber si acierto, que es la condicion entera de que sirvan
para la relectura ciega.** Ninguno de los cinco es una clase de par: esta vuelta
**no leyo ni un par y no escribio ni un veredicto**, asi que la adjudicacion 7.1
del acta 179 (un discutible cuya clase va en una tabla queda quemado como sujeto
ciego) **no se activa en ninguno**.

**`D.1`. QUE `vuelta174_tarea1b_mutacion_esqueleto.py` NO ABRE NINGUN FICHERO
VIVO, contra lo que el encargo supone.** Mi lectura dice que su `REPORTE.md` es
un fichero que **el mismo fabrica** en un `tempfile.mkdtemp`, y que por eso le
faltaba **declararlo** y no **congelarlo**. La base de evidencia es el campo
`evidencia.codigo` del propio registro de la 179, linea 182. **Es discutible
porque contradice la letra del encargo**, que lo pone entre los cuatro que si
abren.

**`D.2`. QUE LA SEGUNDA COLUMNA DE REALES DE `OP-L-02` HACIA FALTA.** El encargo
pide **una** definicion de par real, la del archivo, que da **15**. Yo publico
**dos**, y la segunda da **0**. Sostengo que sin las dos la cifra engana en un
sentido o en el otro, porque los quince **estan leidos** como lectura dirigida.
**Es discutible porque anade una columna que el encargo no pidio.**

**`D.3`. QUE LA COLUMNA "SE MUEVE DENTRO DE UNA VUELTA" DEL BARRIDO NO PUEDE
TENER CASO ROJO AUTOMATICO.** Lo declaro en el propio instrumento y aqui. Alguien
podria sostener que si se puede, corriendo el instrumento en dos cortes distintos
de la misma vuelta y viendo cual cifra se movio. **No lo hice**, y la razon es que
eso mediria **lo que se movio hoy**, no **lo que puede moverse**, y una cifra que
hoy no se movio por casualidad quedaria clasificada como fija. **Es discutible.**

**`D.4`. QUE RETIRAR `docs/loop/reportes/REPORTE_V180.md` ERA LO CORRECTO.**
Decidi borrarlo por mi cuenta. Sostengo que un archivo de un reporte a medias
habria puesto en rojo al archivador del cierre. **Es discutible porque es una
destruccion de fichero que nadie me pidio**, aunque el fichero llevaba dos minutos
existiendo, no estaba seguido por git y su contenido esta entero en el commit
`7b0a1ef1`.

**`D.5`. QUE `sujeto_congelado_de_git.py` DEBIA NACER CON NOMBRE ESTABLE Y NO
COMO TRES BLOQUES DENTRO DE LOS TRES ARNESES.** Lo hice compartido porque tres
copias de la misma lectura envejecerian por separado. **Es discutible porque crea
una dependencia nueva** que tres arneses de mutacion ahora comparten, y si ese
fichero se rompe caen los tres a la vez.

## 6. LAS PREGUNTAS

**`P.1`. `scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py` ESTA EN ROJO Y
NACIO CADUCADO EN SU PROPIO COMMIT. NO LO ARREGLO PORQUE NADIE ME LO ENCARGO, Y
LO TRAIGO.** Lo destape corriendolo para comprobar que mi cambio del parametro de
`paso0` no rompia a sus llamadores. **Falla por una causa que no tiene nada que
ver con mi cambio**: su comprobacion `("el reporte de entonces NO estaba en el
archivo", "REPORTE_V171.md" not in archivados)` exige que ese archivo **no
exista**, y **existe**. Medido con git: el arnes **nace** en el commit `45fb75f5`
y `docs/loop/reportes/REPORTE_V171.md` **se anade en ese mismo commit `45fb75f5`**.
Es exactamente la especie que el arnes de la 157 declara de si mismo, *"NACIO
CADUCADO DENTRO DE SU PROPIO COMMIT"*. **Y no lo ve nadie**: su nombre no trae
ninguna de las tres familias del censo (`mutacion`, `caso_positivo`, `simular`),
asi que **no esta en el censo ni en la nomina y la bateria nunca lo corre**. Es la
frontera que el propio verde de la bateria declara con esas palabras: *"Un arnes
con un nombre de OTRA familia seguiria sin verse"*. **La pregunta: se le arregla
el esperado, se le cambia el nombre para que el censo lo vea, o se declara fuera?**

**`P.2`. LA CONVENCION DE BYTES SIGUE SIN FIJAR, Y ES DEL FUNDADOR.** Van siete
actas subiendo. **Sube como PENDIENTE y no como problema**, porque el remedio
provisional (publicar siempre las dos, disco y normalizado a LF) ya es
instrumento y esta cableado en `cerrar_reporte.py`.

## 7. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las cinco tareas se resolvieron con regla escrita: la
adjudicacion `7.7` del acta 179 para la TAREA 1, la `7.8` para la TAREA 2, el
`banco 9.21` mas el punto `7.2` del acta 178 para la TAREA 3, `EJECUTOR.md` 8 y
el `banco 9` para la TAREA 4, y `P.1` mas `banco 9.10` para la TAREA 5.

**LO QUE SIGUE SUBIENDO Y NO ES DOCTRINA NUEVA:** el grano del tope de 10 minutos
de la bateria, que **se mide EN LA 181 con el reloj de esa corrida** y no se
re-elige a ojo antes.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1`. CORRI EL ESQUELETO ENTERO A MITAD DE VUELTA Y ME BORRE EL REPORTE DEL
ARBOL.** Esta contada entera en la seccion de la TAREA 4, con su medicion. En una
linea: prediciendo que el paso 0 lo pararia, corri
`scripts/loop/vuelta180_esqueleto_reporte.py` completo; **no lo paro, y con
razon**; archivo el reporte de la 180 a medias y lo reescribio con cinco filas
vacias. **DANO MEDIDO: CERO.** Restaurado con `git checkout HEAD`, `sha256`
`4836dc51e19092efd56d164d945eaeac4605a96ce95ca6195971c6949a9c9563` a los dos
lados, tres filas `CERRADA` dentro. **Lo que me salvo fue commitear por tarea**, y
eso no es merito de esta vuelta sino de la regla 6 de `EJECUTOR.md`.

**`C.2`. `backlog_l02_resuelto.py` NACIO CON LA RESTA MAL Y SALIO EN ROJO EN SU
PRIMERA CORRIDA.** Contaba pares **escritos** donde debia contar **distintos tras
resolver**, que es la trampa que `backlog_l03_resuelto.py` **ya tiene declarada en
su propio codigo** y que yo no lei antes de escribir. **La cazo su propia guarda
de restas**, la corrida roja esta guardada sin retocar en
`docs/loop/SALIDA_V180_T5_BACKLOG_L02_ANTES.txt`, y el arreglo trae su arnes.
**No se publico ninguna cifra falsa**: el instrumento se nego a dar el verde.

**`C.3`. EN LA PRIMERA VERSION DEL BARRIDO DECLARE 32 CIFRAS Y TRECE NO LLEVABAN
CORTE.** No es una caida de publicacion, porque no publique nada antes de mirar,
pero **si es una prediccion mia que salio mal**: escribi la tabla del barrido
esperando que faltaran pocas. **Faltaban trece de veinticinco movibles.** La
corrida roja esta guardada en `docs/loop/SALIDA_V180_T3_BARRIDO_ANTES.txt`.

**NINGUNA DE LAS TRES SE TAPA, Y LAS TRES TIENEN SU FICHERO.** Y las tres son de
la misma especie, que es la que esta vuelta vino a perseguir: **predije en vez de
medir**, tres veces, y las tres veces el instrumento me corrigio.
