# -*- coding: utf-8 -*-
"""_v74_texto_acta73.py . EL TEXTO EDITORIAL DEL REGISTRO DEL ACTA 73.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo coteja y lo adosa es
scripts/loop/vuelta74_registrar_acta73.py, que lo importa. Vive aparte por la
misma razon por la que el contenido de un lote vive aparte del generador: para
que el fichero que MIDE y el fichero que DICE no se confundan. Es el mismo
reparto que las vueltas 66 a 73 usaron con _v66_texto_acta65.py,
_v67_texto_acta66.py, _v68_texto_acta67.py, _v69_texto_acta68.py,
_v70_texto_acta69.py, _v71_texto_acta70.py, _v72_texto_acta71.py y
_v73_texto_acta72.py.

AQUI NO HAY NI UN NUMERO DE LINEA TECLEADO. Cada cita va como marca [[CLAVE]] y
el registrador la sustituye por el numero que le devuelve BUSCAR la aguja de esa
clave en su fichero.

LO QUE ESTE TEXTO REGISTRA, y es lo que el encargo de la vuelta 74 pide: LA
VERIFICACION COMPLETA POR CORRIDA PROPIA con la ciega 4 de 4; LA TANDA LIMPIA y
el contador de parada en CERO POR TERCERA TANDA SEGUIDA; los TRECE discutibles A
FAVOR con su vara citada; LAS TRES PREGUNTAS DE LA SECCION 8 DEL REPORTE
ADJUDICADAS POR EXTENSION CITABLE, cada una en la linea donde el acta la
adjudica; LAS CUATRO AVERIAS DEL EJECUTOR y LOS TRES ERRORES PROPIOS DEL AUDITOR;
y LA REGLA NUEVA DE REDACCION DE LAS PROMESAS DE MARCADO, que es lo unico de este
registro que rige HACIA ADELANTE y por eso va en su propio apartado.

LA REGLA NUEVA SE ESCRIBE AQUI PORQUE AQUI ES DONDE SE PUEDE CITAR, y eso lo pide
el encargo con esas palabras. Sus TRES FORMAS no se teclean: se citan por aguja
sobre scripts/loop/comprobar_promesas_de_marcado.py, que es el fichero que las
define y las imprime. Una regla que nombra tres cadenas y las teclea es una regla
que puede divergir del instrumento sin que nadie lo note; citada por aguja, no.

ESO ESTRENA UN FICHERO DE AGUJA QUE LAS VUELTAS ANTERIORES NO USABAN
(scripts/loop/comprobar_promesas_de_marcado.py). NO ES MAQUINA NUEVA: la maquina
de agujas sale identica del ancestro y ya buscaba en el fichero que la CLAVE
nombrase; lo unico propio es la ruta, que vive en el bloque PROPIO como el resto
de AGUJAS. El D11 del acta 72 adjudico ese mismo carril A FAVOR cuando la vuelta
72 estreno TRES rutas por el, y la vuelta 73 estreno UNA.
"""

TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 73, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 74, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **CATORCE** veces, **y la cifra va con su medicion del dia al lado en
vez de heredada**: **DOCE** llevan esta misma cabecera de nivel dos (de la del acta 61 a la del acta
72, contadas hoy por maquina sobre el fichero) y **DOS** son las mas viejas, que la pagina adoso con
cabecera de nivel tres (la del acta 52 y la del acta 57). **La ultima de las catorce es la del acta 72
en la linea **[[PAG_ACTA72]]** y la anterior la del acta 71 en la **[[PAG_ACTA71]]**, las dos cotejadas
HOY abriendo el fichero.** **Ninguna cifra publicada de arriba se toca.**

**NINGUNA CITA DE LINEA DE ESTA SECCION ESTA TECLEADA:** cada una es una marca que el registrador
sustituye por el numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de
escribir una sola letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero
de linea que aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe
nada**.

**El acta de la vuelta 73 abre en la linea **[[A73_ABRE]]** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por corrida propia en la
**[[A73_VERIF]]**, su relectura ciega en la **[[A73_CIEGA]]**, sus trece adjudicaciones de discutibles
en la **[[A73_TRECE]]**, las cuatro averias del ejecutor en la **[[A73_AVERIAS]]**, sus errores
propios en la **[[A73_PROPIOS]]**, su metrica de credito en la **[[A73_METRICA]]**, sus condiciones de
parada en la **[[A73_PARADAS]]** y su encargo en la **[[A73_ENCARGO]]**.

> **ESTA ACTA NO TIENE SECCION DE ADJUDICACIONES NUEVAS, Y ESO NO ES UN OLVIDO: ES DONDE ESTAN.** Las
> actas 69 a 72 llevaban una seccion aparte para ellas; **la 73 adjudica DENTRO de los discutibles**,
> porque **las tres preguntas abiertas del reporte se resolvieron por EXTENSION CITABLE de reglas ya
> escritas y no por doctrina nueva**, y una extension se lee mejor pegada al caso que la provoca.
> **Este registro las saca de ahi y las pone juntas en su apartado**, con la linea de cada una, para
> que la vuelta siguiente no tenga que releer trece discutibles para encontrar tres reglas.

### a) **LA VERIFICACION FUE COMPLETA Y POR CORRIDA PROPIA, Y VA PRIMERA PORQUE ES LA QUE SOSTIENE TODO LO DEMAS**

**El acta 73 no acepto ni una cifra del reporte: las volvio a medir con sus propios instrumentos y
publico sus sondas.** **La tabla de abajo es lo que el acta dice haber corrido, sede por sede, y cada
fila lleva la linea del acta donde esa medicion esta escrita.** **Esto no es una cifra nueva: es el
registro de una verificacion, y por eso cita en vez de recontar.**

| lo que el acta 73 re-corrio por su cuenta | lo que le dio | linea |
|---|---|---:|
| **la cadena de commits**, leida de `git log` | **los SEIS del reporte en la rama y EN ORDEN**, y la seccion 12 del reporte nombrandolos igual | **[[A73_V_CADENA]]** |
| **el marcador**, con su propio `python` sobre el archivo de veredictos | las cuatro clases, `n`, **cero huecos y cero duplicados de puesto**, y **las DIEZ tasas por dominio calzando AL DECIMAL** | **[[A73_V_MARCADOR]]** |
| **la cabecera del reporte**, con el tallador re-corrido | **identica a la pegada, celda a celda** | **[[A73_V_CABECERA]]** |
| **el recomputo al cierre**, con `recomputo_3388.py` | **IDENTICA BYTE A BYTE** a la salida del ejecutor **salvo la linea de la ruta de escritura**, con retrato, componentes y las cuatro comprobaciones en `OK` | **[[A73_V_RECOMPUTO]]** |
| **el grafo**, contado por el auditor sobre `master_graph.json` | ficheros, vivos, deprecados y enlaces al digito, **y su propia primera cuenta declarada como error de definicion suya** | **[[A73_V_GRAFO]]** |
| **los OCHO absorbidos y los CUATRO supervivientes** | los absorbidos **deprecados** y los supervivientes **vivos con los tamanos del reporte**, y el crecimiento acto a acto calzando | **[[A73_V_ABSORBIDOS]]** |
| **la cola de costuras**, por `git show` sobre el commit del plan y por conteo de hoy | **los DOS que entran presentes y los CUATRO absorbidos que salen ausentes**, por `grep` propio | **[[A73_V_COLA]]** |
| **las colisiones**, con el censo re-corrido | **identica a la del ejecutor salvo su linea final de cotejo**: vigentes, auto-pares y pares resueltos distintos | **[[A73_V_COLISIONES]]** |
| **las colisiones esperadas**, **RE-SIMULADAS PRE FUSION en un worktree** sobre el commit del plan | la base **MEDIDA sobre el arbol de antes**, cero nuevas, cero idas, y **`CALZA`** con el censo del cierre | **[[A73_V_ESPERADAS]]** |
| **las varas y los puentes PRE FUSION**, en el mismo worktree | **la tabla entera al digito**: los cuatro actos, las tres columnas, las marcas de apunte **y la restriccion a los dos coronados del `acto 50`** | **[[A73_V_VARAS]]** |
| **las duplicadas**, contadas sobre el archivo de aristas | los grupos y los nodos al digito | **[[A73_V_DUPLICADAS]]** |
| **las operaciones y el inventario** | **las fichas todas `LISTA`**, **CERO dependencias rotas** por `depende_de` contra `id_op`, las entradas y los racimos, **y el `diff` desde el corte anterior VACIO** | **[[A73_V_OPERACIONES]]** |
| **el `numstat` de los commits de la vuelta** | las lineas anadidas y **CERO borradas** en cada sede, **los instrumentos nuevos por `--diff-filter=A`** y **el unico modificado por `M`** | **[[A73_V_NUMSTAT]]** |
| **la cuenta agregada de perdidas**, re-corrida sobre el plan sellado | el total, el reparto por especie, el atenuante, **y la celda del pendiente 4 en `0` CON LA DEFINICION YA CORREGIDA** | **[[A73_V_CUENTA]]** |
| **las promesas de marcado**, con su instrumento **y ademas leyendo el plan a mano** | **DOS medidas y DOS cumplidas**, **y las DOS formas que el instrumento NO VE leidas por el auditor en el propio plan** | **[[A73_V_PROMESAS]]** |
| **el borde del dueno**, por instrumento **y por cruce propio campo a campo** | **los duenos del reporte calzando POR DOS VIAS** | **[[A73_V_BORDE]]** |
| **el tramo al cierre**, recomputado sobre el fichero fijado y el grafo de hoy | las filas, los actos con un vivo o menos y los que tienen dos o mas, **y NINGUN acto sin dueno y sin destino** | **[[A73_V_TRAMO]]** |
| **`Gate 0` con su ciclo de TRES y las tres suites**, corridas por el auditor | `GATE 0 OK`, alcanzabilidad entera, **el grafo identico al committeado tras el ciclo**, motor, web y `tsc` en verde, **y el log restaurado** | **[[A73_V_GATE0]]** |
| **el barrido de titulos** | ficheros, `ROJO` en su linea base, `AMBAR` en cero, rotulados y censados, **identico a la seccion 9 del reporte** | **[[A73_V_BARRIDO]]** |
| **el censo de ficheros de la vuelta** | contado por el auditor con `grep -c`, **como el censo del ejecutor dice** | **[[A73_V_CENSO]]** |

> **LAS DOS MEDICIONES MAS CARAS DEL ACTA SIGUEN SIENDO LAS PRE FUSION**, porque exigen un **worktree
> sobre el commit anterior** para poder medir lo que ya no existe en el arbol de hoy: **las esperadas
> sobre la base medida** (linea **[[A73_V_ESPERADAS]]**) y **las varas con la restriccion a los
> coronados** (linea **[[A73_V_VARAS]]**). **Es la unica forma de comprobar una prediccion sin creerle
> a quien la hizo.**
>
> **Y HAY UNA TERCERA QUE ESTA ACTA ANADE Y QUE NO ES DE INSTRUMENTO SINO DE LECTURA** (linea
> **[[A73_V_PROMESAS]]**): el auditor **no se quedo con el verde del instrumento de promesas**, abrio
> el plan y leyo los motivos. **Ahi es donde salieron las dos formas invisibles**, y de ahi sale la
> regla nueva del apartado `d`. **Un instrumento en verde sobre lo que sabe ver no dice nada sobre lo
> que no sabe ver.**

### b) **LA RELECTURA CIEGA: 4 DE 4 ACTOS COINCIDENTES, Y CERO DISCREPANCIAS**

**El auditor extrajo los textos ENTEROS de los doce nodos en su version PRE fusion** (por `git show`
sobre el commit anterior al plan), **imprimio pasos, condiciones y entregables ANTES de destapar UNA
SOLA razon**, adjudico familia y superviviente, **y SOLO DESPUES leyo las ocho razones** (linea
**[[A73_CIEGA_LEIDOS]]**).

**`CERO` DISCREPANCIAS: las cuatro coronas del auditor son las cuatro del ejecutor**, y **todas
dentro del marcado** (linea **[[A73_CIEGA_4DE4]]**).

| lo que la ciega confirmo, y por que importa | linea |
|---|---:|
| **la afirmacion mas cara del reporte entero**: **las DOS razones del `acto 50` matan LAS DOS al mismo nodo que la unica vara elige**, con la contencion escrita verbatim (*le queda una linea propia*, *le quedan dos lineas*) | **[[A73_CIEGA_2290]]** |
| **los siete `INCISO` VERBATIM en los supervivientes de hoy, CON SUS TILDES**, mas los dos `APPEND` declarados propios, el `APPEND` del `D3` y la linea del `D6` viviendo como inciso | **[[A73_CIEGA_INCISO]]** |

> **LA CIEGA DEL `50` ES LA QUE MAS PESA, Y LLEGO POR OTRA VIA AL MISMO SITIO** (linea
> **[[A73_CIEGA_50]]**): el auditor separo los dos entregables leyendolos, **el informe entero
> contra una narrativa DENTRO de ese informe**, sin haber visto todavia las razones que dicen lo
> mismo. **Cuando la lectura ciega y las razones escritas coinciden desde fuera, la decision del `D1`
> deja de apoyarse en una sola vara.**

### c) **LA TANDA 73 SALIO LIMPIA ENTERA, Y EL CONTADOR DE PARADA SIGUE EN `CERO` POR TERCERA TANDA SEGUIDA**

**Es la noticia que mueve el contador, y va con las cifras separadas en vez de con un limpia suelto**,
porque la regla de la parada distingue especies y no humores.

| | lo que el acta 73 escribe | linea |
|---|---|---:|
| **las tres especies del ejecutor, contadas por separado** | `CERO` **de clase**, `CERO` **de cifra publicada**, `CERO` **de reporte** | **[[A73_METRICA_CAIDAS]]** |
| **las CUATRO averias propias del ejecutor** | **manejos propios cazados por instrumento o por lectura ANTES de una cifra publicada o un dato movido**; **NINGUNA cuenta como caida** | **[[A73_AVERIAS_CUATRO]]** |
| **los TRES errores propios del AUDITOR, con nombre** | la cuenta de enlaces con definicion propia distinta, las claves inventadas en su primer recomputo, y `run_phase1` corrido sin el ciclo de tres | **[[A73_PROPIOS_ENLACES]]** |
| **el acumulado, que sigue creciendo y no se reinicia** | relecturas, puestos y las caidas historicas de las dos partes, **cada especie con su columna** | **[[A73_METRICA_ACUM]]** |
| **LA RACHA DE CLASE O CIFRA PUBLICADA** | **`CERO` tandas, TERCERA limpia seguida** | **[[A73_RACHAS]]** |
| **LA RACHA DE REPORTE** | **`CERO` tandas, TERCERA limpia seguida** | **[[A73_RACHAS_REPORTE]]** |

> **LAS DOS RACHAS SE REGISTRAN POR SEPARADO PORQUE LA REGLA DE LA PARADA LAS CUENTA POR SEPARADO:**
> la de **clase o cifra publicada** para en **DOS** seguidas y la de **reporte** en **TRES**. **Que
> las dos esten en cero a la vez por TERCERA tanda es lo que este registro deja escrito**, y **una
> racha es una medida de las tandas que ya pasaron, no un permiso para la siguiente.**
>
> **LOS ERRORES DEL AUDITOR SE REGISTRAN CON LA MISMA LETRA QUE LOS DEL EJECUTOR** (linea
> **[[A73_PROPIOS_ENLACES]]**), **y el primero es el ejemplar util**: el auditor conto los enlaces con
> **su** definicion (solo vivos) y le dio otra cifra que la del instrumento (todos los ficheros).
> **No copio la cifra buena: declaro la discrepancia y fue a leer el instrumento**, que es exactamente
> lo que la regla 2 manda hacer cuando dos mediciones no calzan.

### d) **LA REGLA NUEVA DE REDACCION: TODA PROMESA DE MARCADO USA UNA DE LAS TRES FORMAS QUE EL INSTRUMENTO VE**

**ESTE ES EL UNICO APARTADO DE TODO ESTE REGISTRO QUE RIGE HACIA ADELANTE**, y por eso va con su
letra entera y no resumido. **Nace del `D13`, que es la averia que el ejecutor declaro CONTRA SI
MISMO**, y el acta la adjudica como **pregunta 3 de la seccion 8 del reporte**.

**LA ADJUDICACION VA VERBATIM Y NO PARAFRASEADA, PORQUE UNA REGLA QUE SE PARAFRASEA SE DEFORMA** (la
cita arranca en la cabecera del `D13` y se copia tal cual):

[[VERBATIM:A73_D13:11]]

**LO QUE LA REGLA MANDA, DICHO EN UNA SOLA FRASE:** de la **vuelta 74 en adelante**, **toda promesa de
marcado escrita en un motivo sellado usa UNA de las tres formas que
[`../../scripts/loop/comprobar_promesas_de_marcado.py`](../../scripts/loop/comprobar_promesas_de_marcado.py)
define e imprime como agujas.** **Escribirla de otro modo no es un error de estilo: es una promesa que
el instrumento NO VE, y una promesa invisible es peor que una incumplida porque no sale en `ROJO`**
(esa es la leccion del acta 64, pregunta 6, que esta adjudicacion extiende).

**LAS TRES FORMAS NO SE TECLEAN AQUI: SE CITAN POR AGUJA SOBRE EL FICHERO QUE LAS DEFINE**, que es la
diferencia entre una regla que puede divergir del instrumento sin que nadie lo note y una que no.

| la forma | donde el instrumento la define | linea |
|---|---|---:|
| **la singular**, la mas vieja | la constante que nacio con el instrumento | **[[PROM_SINGULAR]]** |
| **la plural** | **ANADIDA y no sustituida** en la vuelta 65, por el acta 64 pregunta 6 | **[[PROM_PLURAL]]** |
| **la que no lleva la palabra intermedia** | **ANADIDA y no sustituida** en la vuelta 67, tras una promesa que el instrumento no vio | **[[PROM_SINCOMO]]** |
| **las tres juntas, que es lo que la vara mira** | la tupla que el instrumento recorre | **[[PROM_FORMAS]]** |
| **y las tres IMPRESAS en cada corrida** | para que **la vara no dependa del docstring** sino de la salida | **[[PROM_IMPRIME]]** |

> **LO QUE ESTA REGLA NO HACE, Y SE DICE PARA QUE SE PUEDA MEDIR:**
>
> **NO ENSANCHA EL INSTRUMENTO** (linea **[[A73_D13_NOENSANCHA]]**). Ni una forma nueva, ni una
> condicion nueva, ni una tabla nueva. **La tupla de formas se queda como esta.** Ensancharla seria
> maquina nueva sobre nombre estable sin necesidad, que es lo que la adjudicacion 3 del acta 69
> prohibe; **la regla resuelve el mismo problema por el lado de quien escribe, que no cuesta nada.**
>
> **NO RE-SELLA LOS PLANES YA EJECUTADOS** (acta 68, `D15`, citado por la propia adjudicacion en la
> linea **[[A73_D13_PLANES]]**). **Las dos promesas invisibles que el auditor encontro se quedan donde
> estan, declaradas**, y **el `D13` sigue siendo la declaracion que las cubre**. Corregir hacia atras
> un plan ejecutado seria tapar lo que se corrige.
>
> **NO CONVIERTE LA FORMA EN LA COSA.** La promesa que vale es la que **se cumple en la seccion 6 del
> reporte**; la forma solo garantiza que el instrumento pueda **verla para exigirla**. Las dos
> promesas invisibles de la vuelta 73 **estaban cumplidas**: lo que fallo no fue el marcado, fue la
> vara.

### e) **LAS OTRAS DOS PREGUNTAS DE LA SECCION 8, ADJUDICADAS POR EXTENSION CITABLE Y SIN DOCTRINA NUEVA**

**Van registradas aunque esta vuelta no las use, y ese es justamente el motivo**: el encargo pide
recordarlas **por si vuelven a salir**, y una regla que solo vive en el acta que la escribio se pierde
en la vuelta siguiente.

| | lo que el acta 73 adjudica, y con que letra ya escrita | linea |
|---:|---|---:|
| **1** | **LA FORMA `UNA SOLA VARA` CON LAS RAZONES EN CONTRA ES UN `CHOCAN` QUE EL INSTRUMENTO NO SABE VER, Y MANDA LA PIEZA DECLARADA.** Por `P.8`, que define en su propia tabla que **una contencion declarada por el archivo es contenido CON EL MISMO PESO**, y por el acta 53, pregunta 3, que dice que **a `CHOCAN` decide la pieza declarada** | **[[A73_D1_PREG1]]** |
| **2** | **LA FRASE SELLADA ESCRITA DENTRO DE UNA NEGACION ES REGLA DE REDACCION, NO MAQUINA NUEVA.** **BASTA con dejarla escrita**; el instrumento **NO se ensancha a distinguir negaciones** | **[[A73_D7_PREG2]]** |

> **LA PRIMERA LLEVA SU EXTENSION EN SU PROPIA LINEA, Y POR ESO SE CITA APARTE DE SU ANUNCIO** (linea
> **[[A73_D1_EXT]]**): **cuando la unica vara que habla apunta al nodo que las razones escritas matan,
> ES un `CHOCAN` que el instrumento no sabe ver, y manda la pieza declarada.** **El instrumento NO se
> ensancha a leer razones**, y el motivo esta dicho: seria **maquina nueva sobre nombre estable sin
> necesidad** (acta 69, adjudicacion 3), **y la marca `D1` hizo su papel sin ella**.
>
> **LAS TRES ADJUDICACIONES DE ESTA ACTA COMPARTEN LA MISMA FIGURA, Y REGISTRARLA JUNTA VALE MAS QUE
> REGISTRARLAS SUELTAS: NINGUNA ENSANCHA UN INSTRUMENTO.** La primera manda leer la letra de `P.8` en
> vez de ensenarle razones al medidor; la segunda deja una regla de redaccion en vez de ensenarle
> negaciones; **la tercera deja otra regla de redaccion en vez de ensenarle formas nuevas.** **Tres
> problemas distintos, la misma salida barata**, y **las tres con su letra ya escrita en vez de
> doctrina nueva**, que es lo que la condicion de parada de doctrina exige comprobar.

### f) **LOS PENDIENTES HEREDADOS Y LO QUE EL ACTA 73 DEJA MEDIDO PARA EL PESO DEL CIERRE**

**El acta 73 recorre sus condiciones de parada y dice que NINGUNA se cumple hoy** (linea
**[[A73_PARADAS]]**), **pero nombra el cierre de la fase 03 como LO UNICO QUE QUEDA DELANTE** (linea
**[[A73_CIERRE03]]**), **porque ya no hay ningun acto del tramo sin dueno y sin destino** (linea
**[[A73_CIERRE03_UNICO]]**).

| lo que falta PESAR, segun el acta | lo que el acta dice de ello, sin decidirlo |
|---|---|
| **el destino de cada una de las fichas de `03_FUSIONES`** | **se mide, no se recuerda** (linea **[[A73_CIERRE03_FICHAS]]**) |
| **los `DECLARADOS Y NO FUNDIDOS` con su subconjunto descrito** | **QUINCE**, **con el `acto 44` NOMBRADO APARTE** por la adjudicacion 3 del acta 72 (linea **[[A73_CIERRE03_QUINCE]]**) |
| **los DOS actos con dueno** | **el `31` y el `37`**, cuyos duenos **viven fuera de la fase 03** segun el acta, **y eso hay que decirlo CON LA FICHA DELANTE** (linea **[[A73_CIERRE03_DUENOS]]**) |
| **la mesa `OP-M-03`** | **su ficha es de otra fase**: si no es de la 03, **no la bloquea**, **y eso tambien se mide, no se supone** (linea **[[A73_CIERRE03_MESA]]**) |
| **quien decide** | **la vuelta 74 ARMA el peso; el auditor de la 74 DECIDE si el cierre esta cerrado y verificado** (linea **[[A73_CIERRE03_QUIEN]]**) |

> **EL REPARTO DE ESA PARADA ESTA ESCRITO Y ESTE REGISTRO LO DEJA CITABLE, QUE ES LO QUE HACE QUE NO
> SE PUEDA CONFUNDIR MAS TARDE** (linea **[[A73_CIERRE03_QUIEN]]**): **medir no es decidir.** La
> vuelta que pesa **no cierra la fase**, **no abre la siguiente** y **no toca un nodo**; **escribe lo
> que hay y lo deja al alcance de quien si decide.** **Y la decision final no es del bucle: el cierre
> de la fase 03 es parada de fundador desde el 21 ago 2026.**

### g) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las siete colisiones vigentes**, **NO toca la mesa `OP-M-03` ni sus colisiones**, **NO ejecuta
ninguna ficha**, **NO funde ningun acto** (ni los que tienen dueno ni los declarados), **NO toca ni un
nodo, ni un alias ni una puerta del `acto 44`**, **NO re-sella ningun plan ejecutado** (que es la parte
negativa de la regla nueva cumplida a la letra), **NO ensancha
[`../../scripts/loop/comprobar_promesas_de_marcado.py`](../../scripts/loop/comprobar_promesas_de_marcado.py)
ni ningun otro instrumento**, **NO decide el cierre de la fase 03** (esa es parada de fundador y el
peso lo pesa el auditor), **NO abre la fase 04**, **NO mueve la linea base del censo de colisiones**
(la mueve el auditor) y **NO anade ni una fila ni una columna a ninguna tabla de registrador**, que es
la adjudicacion 3 del acta 69 aplicada sobre el instrumento que la registra.
"""
