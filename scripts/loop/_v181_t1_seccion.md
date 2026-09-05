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
