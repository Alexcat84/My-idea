## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, Y ESTA VEZ CON CIFRAS DENTRO

**ESTA ES LA SECCION QUE EN LA 214 SALIO PUBLICADA VACIA**, y el remedio son las
dos mitades de la TAREA 5, no una: **la consola se sella desde dentro del propio
instrumento**, y **el compositor CAE EN ROJO si no la encuentra**. La segunda es
la que importa: en la 214 el fichero no existia y mi compositor **escribio una
fila en blanco y siguio**.

**Contado de las dos consolas selladas, no de memoria. FILAS ARMADAS:
2. FILAS QUE DEBERIA HABER: 2.**

| lado | comandos con exitcode leido | los que no dan 0 | peor exitcode | consola sellada |
|---|---:|---:|---|---|
| **APERTURA** | 9 | 0 | **0** | `docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt` |
| **CIERRE** | 9 | 0 | **0** | `docs/loop/SALIDA_V215_CICLO_GATE0_CIERRE_CONSOLA.txt` |

**Y LAS DIECIOCHO SALIDAS EN DISCO, CADA UNA CON SU EXITCODE LEIDO DE DENTRO DEL
PROPIO FICHERO Y SUS BYTES MEDIDOS.** **FILAS ARMADAS: 9. FILAS QUE
DEBERIA HABER: 9, una por comando, con sus DOS lados en la misma fila, o sea
DIECIOCHO celdas.** **CIFRA salidas ausentes o sin exitcode dentro: 0**, y si
hubiera una sola este cuerpo no existiria.

| # | comando | APERTURA (exitcode / bytes) | CIERRE (exitcode / bytes) |
|---|---|---|---|
| **1** | `run_phase1.py --reaplico-curaduria` | 0 / 4790 bytes | 0 / 4790 bytes |
| **2** | `etiquetas_de_cara.py --aplicar` | 0 / 7928 bytes | 0 / 7928 bytes |
| **3** | `sync_assets_web.py` | 0 / 574 bytes | 0 / 574 bytes |
| **4** | `git diff HEAD --numstat` | 0 / 140 bytes | 0 / 140 bytes |
| **5** | `vuelta83_conteo_aristas.py WORK` | 0 / 168 bytes | 0 / 168 bytes |
| **6** | `vuelta85_medir_desfase_calibrado` | 0 / 498 bytes | 0 / 498 bytes |
| **7** | `engine/run_all_tests.py` | 0 / 1131 bytes | 0 / 1131 bytes |
| **8a** | `npx tsc --noEmit` | 0 / 7 bytes | 0 / 7 bytes |
| **8b** | `pnpm test` | 0 / 336 bytes | 0 / 336 bytes |

**`numstat` de los arboles del dataset al cerrar: 0 fila(s). Del
arbol del plan: 0 fila(s).**

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**El `sha256` de apertura se LEE de `docs/loop/SALIDA_V215_APERTURA.txt`, que se
sello antes de la primera operacion; el de cierre se computa ahora.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes disco / LF |
|---|---|---|---|---|
| `docs/plan/INVENTARIO.jsonl` | 43cea06634e6fc1a | 43cea06634e6fc1a | quieta | 629533 / 629533 |
| `docs/plan/OPERACIONES.jsonl` | 650578474361eb2b | 650578474361eb2b | quieta | 517181 / 517181 |
| `docs/plan/08_VERIFICACION.md` | 578eeefab6db2fd4 | 578eeefab6db2fd4 | quieta | 73652 / 73652 |
| `docs/plan/10_INVENTARIO.md` | 67f464d3d0b9e067 | 67f464d3d0b9e067 | quieta | 34258 / 33845 |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 758edf1f5c313c18 | 758edf1f5c313c18 | quieta | 4057130 / 4057130 |
| `docs/INTRA_DOMINIO_INFORME.md` | c05b6bcd20188a9c | c05b6bcd20188a9c | quieta | 943970 / 943970 |
| `docs/plan/00_INDICE.md` | 2e71336cc2fdc387 | 2e71336cc2fdc387 | quieta | 45278 / 45278 |
| `docs/BANCO_DE_TEXTOS.md` | 8adbd60239509bb4 | 8adbd60239509bb4 | quieta | 186490 / 186490 |
| `docs/plan/BANCO_DEL_PLAN.md` | 7836c8976c585143 | 7836c8976c585143 | quieta | 61554 / 61554 |
| `dataset/metadata/master_graph.json` | 627cc662296f7f00 | 627cc662296f7f00 | quieta | 8375817 / 8375817 |
| `docs/loop/ACTA_AUDITOR.md` | c072020f7b7c8b9c | c072020f7b7c8b9c | quieta | 5036598 / 5036598 |
| `docs/loop/PROMPT_SIGUIENTE.md` | e14899642d324038 | e14899642d324038 | quieta | 8281 / 8281 |

**CIFRA sedes cotejadas: 12 | CIFRA que se movieron: 0.**
**LAS DOCE ESTAN QUIETAS, Y ESA ES LA PRUEBA MEDIDA DE QUE ESTA VUELTA NO
ESCRIBIO NI UN NODO, NI UN VEREDICTO, NI UNA FICHA.** La 6.1 prohibe trabajo de
plan al lado de la bateria, y **el cierre integral no es trabajo de plan, es
verificacion**: aqui esta la cifra que lo sostiene. **`docs/loop/ACTA_AUDITOR.md`
y `docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, tambien quedan
quietas.**

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y su salida se cita en el commit
de cierre. **Y ademas va metido como guarda previa en los CUATRO compositores de
tarea de esta vuelta**: los cuatro cuentan las rutas inexistentes o de cero bytes
y los directorios de dos tramos entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**Ningun arnes, guarda ni lector nuevo que se quede vigilando, y ninguno
reparado.** **NO SE TOCO EL LANZADOR DE LA BATERIA**, que es lo que el encargo
nombra: `scripts/loop/vuelta183_bateria_por_tramos.py` no cambia ni un byte, y se
uso tal cual. **La nomina sigue CONGELADA EN 135.**

**CONTADO DE `git diff --name-only` entre el HEAD de apertura y el de ahora:
21 fichero(s) tocados en el arbol de scripts del bucle, de los cuales
21 llevan el prefijo `_v215_` y 0 no lo llevan.**

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: 1 linea**, y era mi propio
  script de apertura sin rastrear.
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0.**

### 4.2. LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE

- **No escribio el PARA_ALEXIS del bucle, y no lo escribe.** Es **sede del
  auditor** por la adjudicacion `4.2` del acta 203, **linea 71543**, ratificada
  por el fundador el 9 sep 2026. **Yo lo PROPONGO en mi reporte, que es mi
  sede**, y va al final.
- **No escribio una linea en la sede del auditor**, y esta medido arriba con los
  `sha256` quietos.
- **No movio ningun campo `estado`**, y la TAREA 4 lo prueba con los dos `sha256`
  del expediente y su `numstat` en cero.
- **No toco ni un nodo, ni un veredicto, ni la vara del expediente.**
- **No arreglo ningun arnes en rojo**: los trae como PARADA, que es lo que la
  TAREA 2.d manda.
- **No pidio ningun merge. El bucle no funde ramas.**

### 4.3. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA

- **commit de apertura**: 2026-09-09 07:31:07 -0400
- **ultimo commit al componer este cierre**: 2026-09-09 08:33:27 -0400

## 5. LAS DOS PARADAS QUE TRAIGO, Y NO LAS ARREGLO YO

**`EJECUTOR.md` 5: se para cuando algo contradice una regla vigente o una cifra
publicada con su corte, se escribe en el reporte como PARADA y no lo arregla el
ejecutor.** Aqui van las dos, cada una con su cifra.

### PARADA 1. CAEN 7 ARNESES DE LA NOMINA, Y LA TAREA 2.d MANDA TRAERLOS

**La cifra y los nombres estan en la TAREA 2, tabla de la `2.d`, contados de los
once ficheros sellados.** Lo que importa para la parada es el cotejo: **CAEN
7 y NUEVOS RESPECTO DE LA CORRIDA ANTERIOR: 0.** **Los
7 ya caian en la vuelta 210**, medido con `git show` sobre el commit que
sello cada fichero entonces.

**NO LOS TOCO, Y DOY LOS DOS MOTIVOS:** mi encargo dice con estas palabras que
*"un arnes en rojo en la vuelta del cierre integral no se arregla de paso"*, y
repararlos seria **fabricar maquinaria bajo la moratoria**. **Se suben con su
nombre.**

### PARADA 2. EL ROJO ESTRUCTURAL DE LOS ONCE TRAMOS ES UNA CONTRADICCION ENTRE DOS REGLAS VIGENTES

**Los once tramos salen en exitcode 1 tambien por otra cosa, y esa otra cosa no
la puede apagar ninguna corrida.** La regla que el propio lanzador lleva escrita
desde la vuelta 148 dice que **UN ARNES ENTRA EN LA NOMINA**; la moratoria del 7
sep 2026 (`AUDITOR.md` 6.3) dice que **la nomina queda CONGELADA EN 135,
ni crece ni se poda**. **Mientras las dos rijan, los dos arneses nacidos despues
de la vara 148 se quedan fuera y el rojo es automatico.**

**LO DIGO CON SU PRECEDENTE MEDIDO Y NO RECORDADO:** la bateria de la vuelta 210
encendio **exactamente este mismo rojo, con los dos mismos nombres**, y se
declaro corrida igual. **No propongo cual de las dos reglas cede: eso no es
mio.**

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

- **`D.a` EL VOCABULARIO DE RELLENO DE LA TAREA 4 ES MIO.** Las 23 palabras que
  definen que es un hueco RELLENADO **las elegi yo**, y van escritas enteras en
  el instrumento para que se puedan discutir. **Otra lista habria dado otro
  numero.** Lo que si esta medido es que la que hay **no es demasiado laxa**
  (compara el campo entero, nunca por subcadena) y **no es demasiado estrecha**
  (su caso positivo caza el relleno y el vacio de una entrada fabricada).
- **`D.b` LA REGLA DEL DESCARTE POR VOCABULARIO DEL CAMPO TAMBIEN ES MIA.** Que
  `pendiente` en `estado` sea vocabulario y no relleno **lo decido yo**, aunque
  la evidencia sea mecanica (el mismo campo trae su forma larga). **Sin esa
  regla, el punto 3 saldria NO CUBRE.** **Es el discutible mas caro de esta
  vuelta y por eso va con su tabla de seis filas delante.**
- **`D.c` CORRI LOS ONCE TRAMOS AUNQUE EL PRIMERO SALIERA EN ROJO.** El lanzador
  dice, al acabar un tramo en rojo, *"Y AQUI SE PARA"*. Lo lei como que **para
  ESE tramo**, no la bateria, y segui con `--tramo 2`. **Me apoyo en el
  precedente medido de la vuelta 210, que hizo lo mismo con el mismo rojo**, pero
  **es una lectura mia** y la marco.
- **`D.d` PUBLICO EL PUNTO 3 COMO CUBRE CON UNA BUSQUEDA QUE DA CERO.** Es lo que
  la adjudicacion `5.4` manda, pero **un cero solo vale lo que valga su
  busqueda**, y la mia es la de arriba. **Si el auditor lee que la clausula pide
  otra cosa, el CUBRE se cae y lo digo antes de que lo mida nadie.**

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**PREGUNTA 1. LOS ONCE TRAMOS SALEN EN EXITCODE 1 POR EL ROJO ESTRUCTURAL. ESO,
LA CASA, LO CUENTA COMO BATERIA CORRIDA O NO?** La `6.1` dice que se declara
corrida cuando los tramos de su reparto tienen **salida sellada del mismo
calibre**, y **los once la tienen**: mismo formato, misma doble corrida, las 135
entradas cubiertas una vez cada una. **Pero once exitcodes en 1 no son un verde**,
y prefiero preguntarlo a decidirlo.

**PREGUNTA 2. LAS CUATRO FICHAS EN HECHA SIN NINGUNA PRUEBA BLOQUEAN EL CIERRE DE
LA CAMPANA?** Mido **4**, el encargo nombra dos, y **ninguna vuelta
las puede cerrar sin escribir en el expediente**, cosa que esta vuelta tiene
prohibida.

**PENDIENTE DE DOCTRINA 1. UN PUNTO EN `A MEDIAS` CUYA SEDE NO EXISTE.** El punto
4 de `OP-I-01` queda en A MEDIAS porque **ningun instrumento del repo escribe la
vista humana** (`CIFRA ficheros .py que la ESCRIBEN: 0`). **Nada dice
si un pendiente sin sede bloquea un cierre de fase o si se declara y se pasa.**

**Y UN PENDIENTE QUE YA NO LO ES, Y LO DIGO PARA QUE NO SE BUSQUE:** el del
marcador contra su cifra vieja **quedo CERRADO por la adjudicacion `5.3`, linea
76166**, y **no lo vuelvo a traer**.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**Son TRES, y las tres las cazaron mis propias guardas ANTES de que el veredicto se
publicara. LA PRIMERA SALIO EN UN COMMIT Y LA CORREGI POR DECLARACION; LAS OTRAS
DOS NO LLEGARON A SALIR.**

- **`D.1` MI PROSA CONTRADECIA A LAS CIFRAS DE SU PROPIO PARRAFO, Y SALIO EN EL
  COMMIT DEL TRAMO 3.** Mi compositor de mensajes de tramo llevaba la frase *"y
  ninguno cae"* **clavada en el texto**, con sus tres ceros tecleados, al lado de
  cifras que si se leian del fichero sellado. En los tramos 1 y 2 coincidieron y
  la mentira no molesto a nadie; **en el 3 el medidor leyo NO MORDIO 1 y la prosa
  siguio diciendo que ninguno cae**. **El texto viejo no se borra: esta en git y
  la correccion va declarada en el commit del tramo 4.** Remedio: la frase se
  **COMPUTA** de las tres cifras, y el instrumento **cae en rojo** si la prosa y
  las cifras no dicen lo mismo. **Mutacion: 5 casos, 0 que no calzan.**
- **`D.2` MI SONDA DEL PUNTO 3 ERA MAS LAXA QUE SU CLAUSULA Y HABRIA PUBLICADO UN
  `NO CUBRE` FALSO.** Contaba **6** campos de relleno, los seis con `pendiente`
  en el campo `estado`, **que ahi no es relleno: es el estado**. **Es la misma
  especie que la `D.7` de la 214**, y esta vez me mordio a mi solo. Remedio: la
  regla del vocabulario del campo, con la forma larga medida en el MISMO campo, y
  **los seis descartes publicados con su nombre**.

- **`C.1` CITE UN FICHERO QUE NO EXISTE COMO SI FUERA RUTA DE PRUEBA, DOS
  VECES, Y ES EXACTAMENTE LA `C.3` DE LA 214 REPITIENDOSE.** El PARA_ALEXIS del
  bucle **todavia no esta escrito**, y nombrarlo entre comillas inversas es una
  ruta que promete prueba apuntando a nada (`EJECUTOR.md` 1, LA RUTA QUE PROMETE
  PRUEBA ES CIFRA). **Me lo conto la guarda de rutas de este mismo compositor,
  que conto 2 rutas malas de 22 y NO ESCRIBIO NADA**, y el texto se reescribio
  sin comillas. **Se registra porque una guarda que muerde y no se cuenta es una
  guarda que la vuelta siguiente no sabe que existe.**

**Y UNA TERCERA QUE NO CUENTO COMO CAIDA Y DIGO POR QUE, PARA QUE NADIE LA CUENTE
POR MI:** mi compositor de la TAREA 3 salio en **ROJO** en su primera corrida
porque su lector de las cuatro clases del marcador devolvia vacio. **NO ESCRIBIO
NADA.** Eso no es una caida de reporte: **es exactamente la guarda de la TAREA 5
haciendo su trabajo**, y si la contara como caida estaria penalizando lo unico
que el hallazgo `3.1` me pidio construir.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**LA CONDICION DE LA PARADA FELIZ, MEDIDA CONTRA LO QUE EL ENCARGO ESCRIBIO ANTES
DE SABER EL RESULTADO.** El encargo dice: *si la bateria da los ONCE tramos en
verde y del mismo calibre, si el cierre integral sale limpio, y si los dos puntos
de la TAREA 4 quedan medidos y dichos*, entonces la campana esta consumada en lo
que el bucle puede consumar.

**LAS TRES, UNA A UNA, CON MI CIFRA DELANTE:**

1. **LOS ONCE TRAMOS: DEL MISMO CALIBRE SI, EN VERDE NO.** Los once tienen salida
   sellada, las **135** entradas corrieron una vez cada una y dos veces
   cada una, **126 en OK**. **Pero los once exitcodes son 1**, y **caen
   7 arneses**. **NO DECLARO ESTO VERDE.**
2. **EL CIERRE INTEGRAL: LIMPIO.** Gate 0 con sus dos lados y sus dieciocho
   salidas, las tres suites en 0, marcador **3388** y censo calzando
   con las trece cifras del encargo, **0 que no calzan**. **Con una cifra que no
   es verde y no la escondo: 40 fichas de 71 no calzan.**
3. **LOS DOS PUNTOS: MEDIDOS Y DICHOS, SI.** El 3 pasa a **CUBRE** con su
   busqueda corrida; el 4 se queda en **A MEDIAS** con su sede buscada y **no
   encontrada**.

**MI PROPUESTA, Y ES LA UNICA HONESTA CON LAS CIFRAS DE ARRIBA: NO SE DECLARA LA
CAMPANA CONSUMADA EN ESTA VUELTA.** Falla la primera de las tres condiciones, y
falla por una cifra que **ni yo ni la vuelta siguiente podemos apagar sin una
decision del fundador**, porque es la contradiccion de la PARADA 2.

**LO QUE SI PROPONGO QUE HAGA LA 215 DEL AUDITOR, EN SU SEDE Y NO EN LA MIA:**

- **Llevar al fundador las DOS PARADAS**, que son las dos que bloquean el verde:
  la contradiccion entre la regla de la nomina y la moratoria, y los **7**
  arneses que llevan cayendo desde antes de la 210.
- **Decidir, o hacer decidir, la PREGUNTA 1**: once tramos del mismo calibre con
  exitcode 1 estructural, **se cuentan como bateria corrida o no**. De esa
  respuesta cuelga si la condicion 1 se puede dar por cumplida.
- **Y NO ESCRIBIR EL PARA_ALEXIS TODAVIA SI LA RESPUESTA NO LLEGA**,
  porque una parada feliz escrita sobre una condicion que no se cumple es
  exactamente la especie de verde que esta casa lleva doscientas vueltas
  cazando. **Si llega y es que si, quien lo escribe es EL AUDITOR de la 215, no
  su ejecutor**, por la `4.2` del acta 203.
- **Y EL MERGE NO SE PIDE EN NINGUN CASO.** Es decision del fundador y viene
  despues de la auditoria integral con credencial. **El bucle no funde ramas.**
