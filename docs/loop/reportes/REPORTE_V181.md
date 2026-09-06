# REPORTE DE LA VUELTA 181 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta181_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA ES LA VUELTA DE BATERIA, Y NO LLEVA NADA MAS.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO, en VUELTA PROPIA. La cadencia se adjudico en el acta
> 176 punto 7.8, se reconfirmo en las actas 178 y 179, y el acta 180 la clava por
> cuarta vez en su punto 10 con estas palabras: *"LA BATERIA: LA PROXIMA ES LA
> 181, Y ES LA VUELTA QUE VIENE"*. **La 180 fue la ULTIMA que declaro el hueco.
> Aqui se corre.**
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y NO ES UN DESCUIDO: ES LA
> ADJUDICACION 6.8 DEL ACTA 180.** `AUDITOR.md` 6.2 devolvio el tope a cinco, pero
> la 6.1 y la 6.2 salen de la MISMA parada del 5 sep 2026 y la 6.2 se concedio
> *"combinada con la (a)"*, o sea subordinada a ella. **La vuelta de bateria no
> lleva trabajo de plan al lado.** El tope vuelve a cinco en la 182.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se lee ningun
> par, no se escribe ningun veredicto, no se toca el marcador, no se toca el estado
> de ninguna ficha, no se toca `docs/plan/`, no se arregla la `P.1` y no se toca
> `cerrar_reporte.py`. **Las dos ultimas van a la 182 y estan escritas en los
> puntos 6.6 y 6.8 del acta 180.**
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 y la 180 lo repitieron y aqui
> vuelve a correr en su sitio. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 180 escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta181_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 180: `b9f25049`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 180: LEVANTO UNA CAIDA DE REPORTE EN CABECERA, LA RACHA PASA A UNO, Y LAS TRECE DISCREPANCIAS DE LA CIEGA LAS PIERDO YO.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V181_HEAD_APERTURA.txt`: `b9f25049`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `8052c9ab`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **180**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 181`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y LO QUE SE HEREDA DEL ACTA 180, Y ES BLOQUEANTE. (a) El acta del auditor de la vuelta 180 vive en `docs/loop/ACTA_AUDITOR.md` con su cabecera en la linea `62449`, y levanta UNA caida de reporte contra la 180, la `E.1`, que vive en la cabecera de su seccion 9 y por tanto ACUMULA: la racha de reporte pasa de CERO a UNO. NO hay ninguna caida de cifra publicada (racha 0) y NO hay ninguna correccion declarada que arrastrar. Los CINCO discutibles de la 180 quedan adjudicados a favor del ejecutor los cinco (puntos 6.1 a 6.5), y el `D.1` corrige ademas el propio encargo del auditor, que lo registra como caida suya. La caida propia del auditor, la tercera seguida, esta en la seccion 2 del acta con el remedio que ata al auditor de la 181: no es trabajo del ejecutor y se cita para que quede en el carril de lectura. (b) Y se anota lo que NO se hace aqui y cuando se hace: la `P.1` (`vuelta172_tarea1c_guarda_que_mordio.py`, en rojo y fuera del censo) queda adjudicada en el `6.6` y el remedio del `E.1` en el `6.8`, LAS DOS EN LA 182 | **CERRADA** | `SALIDA_V181_T1_REGISTROS.txt`, `SALIDA_V181_APERTURA.txt` bloques H.6 y H.7, `ACTA_AUDITOR.md` lineas 62449 a 62896 |
| **TAREA 2** | LA BATERIA DE MUTACIONES, ENTERA, SOLA, Y CON SU RELOJ, Y ES LA UNICA TAREA DE TRABAJO DE ESTA VUELTA. (a) `scripts/loop/verificar_mutaciones_viejas.py` SIN `--tramo`, sobre la nomina entera, cada entrada corrida DOS VECES (el cotejo de reproducibilidad de la vuelta 141, que no se afloja), con la salida en `docs/loop/SALIDA_V181_BATERIA.txt` con ese nombre exacto y publicada COMPLETA Y SIN RECORTAR en la seccion 9; y con la guarda nueva de una linea que nace de la `E.1`: el valor de `vuelta que lleva dentro el nombre del fichero` que imprime `cerrar_reporte.py` TIENE QUE DECIR 181, y si dice `None` u otro numero SE PARA. (b) EL RELOJ, medido en esta corrida y no elegido a ojo: tiempo total, tiempo por entrada con su maximo, su minimo y su mediana, el nombre del arnes mas lento, y si el tope de 10 minutos se toco o no CON LA CIFRA AL LADO. Se mide, se publica y no se cambia nada. (c) EL VEREDICTO DE LAS SEIS PIEZAS de `hay_rojo_al_cierre()` una a una, cada una con su cifra, y no solo el color final. (d) LA DOBLE CORRIDA COTEJADA Y PUBLICADA COMO TAL, nombrando a quien no reproduzca. (e) NADA SE PODA DE LA NOMINA (`AUDITOR.md` 6.1), y si la bateria destapa un arnes roto NO se borra ni se saca: se deja en rojo, se nombra y se trae | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1 (BLOQUEANTE). LOS REGISTROS, Y LO QUE HEREDO DEL ACTA 180

**TODA LINEA QUE ESTA SECCION CITA SALE DE
`docs/loop/SALIDA_V181_T1_REGISTROS.txt`**, que la produce
`scripts/loop/vuelta181_tarea1_registros.py` buscando cada frase literal dentro
de `docs/loop/ACTA_AUDITOR.md` y contando su numero de linea del propio fichero.
**Ninguna linea se teclea y ninguna se recuerda:** si una frase del acta hubiera
cambiado una palabra, la aguja no se encontraria y el instrumento lo diria en vez
de seguir publicando la frase vieja. Su corrida de hoy sale **VERDE con 26 agujas
buscadas, 26 encontradas y 0 perdidas**.

**EL ACTA 180, LOCALIZADA Y NO TECLEADA:** su cabecera esta en la **linea
62449** de `docs/loop/ACTA_AUDITOR.md` (`# ACTA DEL AUDITOR, VUELTA 180 (5 sep
2026, auditor Opus 5)`), el fichero mide **62.906 lineas**, **4.177.731 bytes en
disco y 4.177.301 normalizados a LF**, y el acta 180 ocupa **458 lineas** desde su
cabecera hasta el final del fichero. **El encargo daba la linea 62449 y la
medicion de hoy la confirma**, pero la que se publica es la medida hoy.

#### 1.a LO QUE EL ACTA LEVANTA CONTRA LA 180, Y ES UNA SOLA COSA

**UNA CAIDA DE REPORTE, LA `E.1`, Y ACUMULA.** La tabla va pegada del fichero de
salida, fila a fila, con la linea del acta al lado:

| que sostiene | linea del acta | texto del acta, tal cual |
|---|---:|---|
| la caida `E.1`, y acumula | 62687 | `## 5. LA CAIDA DEL EJECUTOR, UNA, Y ACUMULA` |
| el titulo de la `E.1` | 62689 | `**`E.1`. LA CABECERA DE LA SECCION 9 AFIRMA QUE LA BATERIA CORRIO ENTERA Y SOLA` |
| la racha pasa de CERO a UNO | 62741 | `**ACUMULA. La racha de reporte pasa de CERO a UNO.**` |
| la causa medida: el fichero del hueco SI existe | 62709 | ``**`SALIDA_V180_HUECO_BATERIA.txt`, que SI existe (1.484 bytes, 21 lineas)**`` |
| la guarda que nunca corrio | 62717 | ``**LA GUARDA QUE `AUDITOR.md` 6.1 NOMBRA POR SU NOMBRE NUNCA CORRIO.**`` |
| la comprobacion de vuelta ajena tampoco mordio | 62722 | `**Y LA COMPROBACION DE VUELTA AJENA TAMPOCO MORDIO.**` |
| no es caida de cifra publicada | 62734 | `**NO ES CAIDA DE CIFRA PUBLICADA Y NO ES PARADA.**` |
| la fila de cifra publicada en la metrica | 62863 | `caidas del ejecutor que ACUMULAN por cifra publicada, 0` |
| la fila de reporte en la metrica | 62864 | ``caidas del ejecutor de reporte, 1 (`E.1`, en cabecera)`` |
| la escalada no se dispara | 62871 | `**LA ESCALADA NO SE DISPARA Y LO DIGO CON LA CUENTA DELANTE:**` |

**LO ACEPTO ENTERO Y SIN REGATEAR, Y LO DIGO CON LA MECANICA DELANTE PORQUE ES LA
QUE ME TIENE QUE ENSENAR ALGO.** La 180 le paso a `--bateria` el fichero
`docs/loop/SALIDA_V180_HUECO_BATERIA.txt`, que existe y trae lineas, asi que
`cerrar_reporte.py` entro por la rama del `if lineas_bat:` y escribio la cabecera
de la bateria corrida sobre una seccion cuyo cuerpo decia que nadie la habia
corrido. **La medi yo hoy en el codigo, no en la prosa del acta**, y sale en
`docs/loop/SALIDA_V181_APERTURA.txt` bloque H.6:

| pieza de la mecanica | donde vive, medido hoy |
|---|---|
| `CAB_9`, la cabecera de la bateria corrida | `scripts/loop/cerrar_reporte.py` **linea 155** |
| `CAB_9_HUECO`, la cabecera del hueco | `scripts/loop/cerrar_reporte.py` **linea 156** |
| `PATRON_FICHERO_BATERIA = re.compile(r"SALIDA_V(\d+)_BATERIA")` | **linea 163** |
| `def vuelta_de_fichero` | **linea 238** |
| `def hueco_declarado_que_falta` | **linea 247** |
| la unica llamada a `hueco_declarado_que_falta(seccion9, vuelta)` | **linea 558** |
| `if lineas_bat:`, la rama que la 180 tomo | **linea 679** |
| `vuelta que lleva dentro el nombre del fichero` | **linea 631** |

**Y EL PATRON, APLICADO A LOS CINCO NOMBRES CON LA FUNCION DE VERDAD** (no con una
lectura mia), en el mismo bloque H.6:

| nombre pasado a `--bateria` | `vuelta_de_fichero` devuelve | existe hoy |
|---|---|---|
| `docs/loop/SALIDA_V177_BATERIA.txt` | **177** | NO |
| `docs/loop/SALIDA_V178_BATERIA.txt` | **178** | NO |
| `docs/loop/SALIDA_V179_BATERIA.txt` | **179** | NO |
| `docs/loop/SALIDA_V180_HUECO_BATERIA.txt` | **`None`** | SI, **1.484 bytes en disco** |
| `docs/loop/SALIDA_V181_BATERIA.txt` | **181** | NO, todavia, y lo produce esta vuelta |

**AHI ESTA EL AGUJERO ENTERO EN UNA FILA:** con `None` no hay nada que comparar y
la comprobacion de vuelta ajena se salta sola. **Y LO QUE EL ACTA AGREGA COMO
AGRAVANTE TAMBIEN LO MEDI:** busque el nombre `SALIDA_V180_HUECO_BATERIA` en todo
`scripts/` y hoy lo nombra **1** fichero, que es
`scripts/loop/vuelta181_apertura.py`, **el mio de esta vuelta, y solo para
medirlo: no lo escribe**. **Ningun instrumento del repo escribia ese fichero**, y
por eso sus cifras entraron tecleadas.

**NO HAY NINGUNA CAIDA DE CIFRA PUBLICADA. RACHA DE CIFRA PUBLICADA 0**, leido de
la linea **62863** del acta.

**NO HAY NINGUNA CORRECCION DECLARADA QUE ARRASTRE, Y ESTA LA MIRE EN VEZ DE
DARLA POR BUENA** (`EJECUTOR.md` 9, una busqueda negativa no se puede citar). El
instrumento cuenta el literal `CORRECCION DECLARADA` dentro del acta 180 y da
**1 aparicion**, no cero. **Fui a verla:** esta en la **linea 62620**, dentro de
la tabla de la escalada de la seccion 3.9, y dice
``| `reportes/REPORTE_V179.md` | 1 cita, y es SIN COTEJO por CORRECCION DECLARADA; rojas **0** |``.
**Es la etiqueta de exencion de la guarda de citas aplicada a un reporte YA
ARCHIVADO, no una correccion declarada contra la 180.** La afirmacion del encargo
se sostiene, y la publico con la medicion al lado en vez de con un cero que el
fichero desmiente.

**LOS CINCO DISCUTIBLES DE LA 180 QUEDAN ADJUDICADOS A FAVOR DEL EJECUTOR LOS
CINCO**, y las ocho adjudicaciones `6.x` estan localizadas en el fichero de
salida, no contadas de memoria:

| adjudicacion | linea del acta | que decide |
|---|---:|---|
| `6.1` | 62758 | `D.1` a favor, y **el error era del encargo del auditor** |
| `6.2` | 62770 | `D.2` a favor, se quedan las dos columnas |
| `6.3` | 62779 | `D.3` a favor, declarar el limite fue lo correcto |
| `6.4` | 62787 | `D.4` a favor, lo cubre `P.16` |
| `6.5` | 62796 | `D.5` a favor, nombre estable y compartido |
| `6.6` | 62806 | `P.1`: se arregla el esperado y despues el nombre, **y NO en la 181** |
| `6.7` | 62823 | `P.2`, la convencion de bytes: octava acta, sigue siendo del fundador |
| `6.8` | 62827 | **el alcance de la 181: dos sub-tareas y nada de plan al lado** |

**CIFRA adjudicaciones `6.x` localizadas: 8**, contadas de
`docs/loop/SALIDA_V181_T1_REGISTROS.txt` seccion C.

**EL `D.1` CORRIGE ADEMAS EL ENCARGO DEL PROPIO AUDITOR, Y LO CITO CON SU LINEA
PORQUE ES UNA CAIDA QUE EL SE REGISTRA A SI MISMO:** la **linea 62764** dice
*"es **una caida de mi encargo, no suya**"*. **No la celebro y no la uso de
escudo:** lo que me toca aprender de ahi es que declarar en vez de congelar fue
lo correcto, y eso ya estaba escrito en `EJECUTOR.md` 8.

**LA CAIDA PROPIA DEL AUDITOR, LA TERCERA SEGUIDA, LA CITO Y NO LA TRABAJO.** Vive
en la **linea 62474** (`## 2. MI CAIDA PROPIA, DELANTE, Y ES LA TERCERA SEGUIDA DE
LA MISMA ESPECIE`) y su remedio, que ata al auditor de esta vuelta a correr
`aislador_de_ciega.py` como su PRIMER comando, esta en la **linea 62490**. **No es
trabajo mio y no lo toco:** queda aqui para que este en el carril de lectura, que
es exactamente lo que el encargo pide.

#### 1.b LO QUE NO SE HACE AQUI, Y CUANDO SE HACE, CON SU PUNTO DE ACTA

| lo que no se hace aqui | punto de acta | linea | cuando |
|---|---|---:|---|
| arreglar la `P.1`, `scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py` | `6.6` | 62806 | **la 182** |
| el remedio del `E.1` sobre `cerrar_reporte.py` | `6.8` | 62827 | **la 182** |

**Y LA LETRA QUE LO ORDENA, CITADA CON SU LINEA:** la **62820** dice **`NO se
encarga en la 181`** sobre la `P.1`; la **62833** dice que el encargo de la 181
lleva **`DOS sub-tareas: los registros y la bateria`**; la **62834** dice que el
`E.1` y la `P.1` **`van a la 182`**; la **62888** dice **`LA BATERIA: LA PROXIMA
ES LA 181, Y ES LA VUELTA QUE VIENE.`**; la **62893** dice **`EL TOPE: DOS
SUB-TAREAS EN LA 181, POR MI ADJUDICACION 6.8`**; y la **62896** cierra con
`## 11. PARADA: NO`.

**LA P.1, MEDIDA HOY Y NO SUPUESTA** (`docs/loop/SALIDA_V181_APERTURA.txt`, bloque
H.7): `scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py` **existe**, mide
**9.127 bytes en disco**, **NO esta en el censo** de `arneses_del_directorio()` y
**NO esta en la nomina `VIEJAS`**. **Esa medicion es la que sostiene la razon de
fondo del `6.8`:** la bateria de esta vuelta no la va a tocar, asi que esperar a
la 182 no le hace correr ningun riesgo. **No la arreglo y no la renombro.**

**LO QUE ESTA VUELTA NO TOCA, DICHO ANTES DE TOCAR NADA:** ni un par leido, ni un
veredicto escrito, ni el marcador, ni el estado de ninguna ficha, ni `docs/plan/`,
ni `dataset/`, ni `cerrar_reporte.py`. **La guarda del commit lo comprueba antes
de cada commit y su salida va en la seccion 4.**

<!-- FIN ANEXO DE TAREAS -->
