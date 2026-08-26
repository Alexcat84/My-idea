# -*- coding: utf-8 -*-
"""_v73_texto_acta72.py . EL TEXTO EDITORIAL DEL REGISTRO DEL ACTA 72.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo coteja y lo adosa es
scripts/loop/vuelta73_registrar_acta72.py, que lo importa. Vive aparte por la
misma razon por la que el contenido de un lote vive aparte del generador: para
que el fichero que MIDE y el fichero que DICE no se confundan. Es el mismo
reparto que las vueltas 66 a 72 usaron con _v66_texto_acta65.py,
_v67_texto_acta66.py, _v68_texto_acta67.py, _v69_texto_acta68.py,
_v70_texto_acta69.py, _v71_texto_acta70.py y _v72_texto_acta71.py.

AQUI NO HAY NI UN NUMERO DE LINEA TECLEADO. Cada cita va como marca [[CLAVE]] y
el registrador la sustituye por el numero que le devuelve BUSCAR la aguja de esa
clave en su fichero.

LO QUE ESTE TEXTO REGISTRA, y es lo que el encargo de la vuelta 73 pide: LA
VERIFICACION COMPLETA POR CORRIDA PROPIA con la ciega 5 de 5; LA TANDA LIMPIA y
el contador de parada en CERO POR SEGUNDA TANDA SEGUIDA; los TRECE discutibles A
FAVOR con su vara citada; LAS TRES ADJUDICACIONES de la seccion 5 con sus letras;
LAS TRES OBSERVACIONES SIN CARGO de la seccion 1; los pendientes heredados con su
destino; y LA UNICA CORRECCION DECLARADA que esta vuelta aplica (la glosa de
cuenta_agregada_de_perdidas.py), con su texto viejo entero y su cita.

LA SEDE DE LA CORRECCION SE CITA POR AGUJA Y NO POR NUMERO TECLEADO, y eso
estrena UN fichero de aguja que las vueltas anteriores no usaban
(scripts/loop/cuenta_agregada_de_perdidas.py). NO ES MAQUINA NUEVA: la maquina de
agujas sale identica del ancestro y ya buscaba en el fichero que la CLAVE
nombrase; lo unico propio es la ruta, que vive en el bloque PROPIO como el resto
de AGUJAS. El D11 del acta 72 adjudico ese mismo carril A FAVOR cuando la vuelta
72 estreno TRES rutas por el.
"""

TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 72, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 73, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **TRECE** veces, **y la cifra va con su medicion del dia al lado en vez
de heredada**: **ONCE** llevan esta misma cabecera de nivel dos (de la del acta 61 a la del acta 71,
contadas hoy por maquina sobre el fichero) y **DOS** son las mas viejas, que la pagina adoso con
cabecera de nivel tres (la del acta 52 y la del acta 57). **La ultima de las trece es la del acta 71
en la linea **[[PAG_ACTA71]]** y la anterior la del acta 70 en la **[[PAG_ACTA70]]**, las dos
cotejadas HOY abriendo el fichero.** **Ninguna cifra publicada de arriba se toca.**

**NINGUNA CITA DE LINEA DE ESTA SECCION ESTA TECLEADA:** cada una es una marca que el registrador
sustituye por el numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de
escribir una sola letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero
de linea que aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe
nada**.

**El acta de la vuelta 72 abre en la linea **[[A72_ABRE]]** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por corrida propia en la
**[[A72_VERIF]]**, su relectura ciega en la **[[A72_CIEGA]]**, su veredicto sobre la tanda del
ejecutor en la **[[A72_LIMPIA]]**, sus trece adjudicaciones de discutibles en la **[[A72_TRECE]]**,
sus tres adjudicaciones nuevas en la **[[A72_ADJUD]]**, sus averias con nombre en la
**[[A72_AVERIAS]]**, su metrica de credito en la **[[A72_METRICA]]** y sus condiciones de parada en la
**[[A72_PARADAS]]**.

### a) **LA VERIFICACION FUE COMPLETA Y POR CORRIDA PROPIA, Y VA PRIMERA PORQUE ES LA QUE SOSTIENE TODO LO DEMAS**

**El acta 72 no acepto ni una cifra del reporte: las volvio a medir con sus propios instrumentos y
publico sus sondas.** **La tabla de abajo es lo que el acta dice haber corrido, sede por sede, y cada
fila lleva la linea del acta donde esa medicion esta escrita.** **Esto no es una cifra nueva: es el
registro de una verificacion, y por eso cita en vez de recontar.**

| lo que el acta 72 re-corrio por su cuenta | lo que le dio | linea |
|---|---|---:|
| **la cabecera del reporte**, con el tallador y su `--comparar` | `IDENTICA AL TALLADOR`, catorce filas cotejadas, distintas `0` | **[[A72_V_CABECERA]]** |
| **el marcador**, por conteo propio sobre el archivo | `n` en su corte, cero huecos, cero duplicados, y **la tasa por dominio identica al digito en las diez lineas** | **[[A72_V_MARCADOR]]** |
| **el recomputo al cierre**, con `recomputo_3388.py` | grafo, retrato, componentes y **las cuatro comprobaciones en `OK`**, todo al digito | **[[A72_V_RECOMPUTO]]** |
| **la cola de costuras**, por su propio `diff` con la apertura sacada de `git` | el delta con **los dos absorbidos que salen NOMBRADOS**, y la cola del arbol anterior comprobada aparte | **[[A72_V_COLA]]** |
| **las colisiones esperadas**, **RE-SIMULADAS PRE FUSION en un worktree** sobre el commit del plan | la base **MEDIDA sobre el arbol de antes** y no pasada a mano, cero nuevas, cero idas, y **`CALZA`** con el censo del cierre | **[[A72_V_ESPERADAS]]** |
| **las varas y los puentes PRE FUSION**, en el mismo worktree | **las formas al byte** y **todas** las celdas de pasos, condiciones y cableado **leidas de la columna `cab`**, mas las puertas medidas contra el universo protegido | **[[A72_V_VARAS]]** |
| **la guarda `D` y los supervivientes**, leidos de `dataset/nodos` | los absorbidos deprecados con su texto entero, **cada id reclamado como `ids_alias` por su superviviente**, y **cero referencias de vivos a absorbidos** | **[[A72_V_GUARDAD]]** |
| **el `acto 44`**, comparado contra el commit del plan | **sus tres nodos vivos e IDENTICOS byte a byte**: el acto declarado no se toco | **[[A72_V_ACTO44]]** |
| **las duplicadas**, con instrumento propio y la apertura por `git show` | los grupos y los nodos al digito, **`CERO` fabricadas y `CERO` renombradas**, y las que desaparecen nombradas una a una | **[[A72_V_DUPLICADAS]]** |
| **la cuenta agregada de perdidas**, re-corrida sobre el plan sellado | el total, el reparto por especie, el atenuante, **la celda del pendiente 4 en `0` con su glosa** y la lectura contraria | **[[A72_V_CUENTA]]** |
| **la fila del atenuante**, leida ENTERA y no contada | **es exactamente el sujeto del `D8`**: la pieza llega por el `INCISO` de un paso desde otro absorbido del mismo acto | **[[A72_V_ATENUANTE]]** |
| **el tramo al cierre**, recontado sobre el grafo | las filas, los `FUNDIDOS`, **los QUINCE declarados por historia**, los que quedan con sus nodos, **y las FORMAS y PUERTAS de los que quedan medidas una a una** | **[[A72_V_TRAMO]]** |
| **`Gate 0` con su ciclo de TRES y las tres suites**, corridas por el auditor | `GATE 0 OK`, alcanzabilidad entera, motor, web y `tsc` en verde | **[[A72_V_GATE0]]** |
| **el barrido, el censo de plantillas, las promesas y los SEIS casos positivos** | **el `ROJO` en su linea base**, `AMBAR` en cero, cero tallados, promesas cumplidas y **los seis casos positivos muerden** | **[[A72_V_BARRIDO]]** |
| **la codificacion de las salidas de la vuelta** | **`CERO` fuera de `UTF-8`**, y los ficheros que la fusion toco contados aparte | **[[A72_V_CODIF]]** |

> **LO QUE ESTA TABLA REGISTRA NO ES QUE LAS CIFRAS SEAN CIERTAS, SINO QUE FUERON RE-MEDIDAS**, y la
> diferencia importa: **el acta no leyo el reporte y asintio, corrio los instrumentos**. **Las dos
> mediciones mas caras del acta son las PRE FUSION**, porque exigen un **worktree sobre el commit
> anterior** para poder medir lo que ya no existe en el arbol de hoy: **las esperadas sobre la base
> medida** (linea **[[A72_V_ESPERADAS]]**) y **las varas con la columna `cab`** (linea
> **[[A72_V_VARAS]]**). **Es la unica forma de comprobar una prediccion sin creerle a quien la hizo.**

### b) **LA RELECTURA CIEGA: 5 DE 5 ACTOS COINCIDENTES, Y CERO DISCREPANCIAS**

**El auditor extrajo los textos ENTEROS de los quince nodos en su version PRE fusion** (por `git show`
sobre el commit del plan del lote `H`), **adjudico familia y superviviente por acto SIN leer las
razones escritas, y SOLO DESPUES destapo los motivos y las notas.** **Los cinco actos van uno a uno.**

| acto | la familia y el superviviente que el auditor adjudico CIEGO | linea |
|---:|---|---:|
| **43** | **UNA** familia (el freno al gasto antes de validar el modelo, Blank); ciego `preservar_efectivo_buscar_modelo`, **el unico con el arco entero**. **Coincide con el superviviente y con la vara de condiciones** | **[[A72_CIEGA_43]]** |
| **44** | **UNA** familia (las tecnologias disruptivas, Cooper); la ciega de contenido habria coronado a `explotacion_tecnologias_disruptivas`, con `tecnologias_disruptivas_oportunidad` segundo | **[[A72_CIEGA_44]]** |
| **45** | **UNA** familia (la reconstruccion del contexto sin sesgo retrospectivo, Dekker); **el contenido EMPATA de verdad** leidos los tres enteros; ciego `reconstruccion_contexto_situacional`. **Coincide con el cableado, que es quien decide a contenido empatado** | **[[A72_CIEGA_45]]** |
| **46** | **UNA** familia (el riesgo ambiental de la cadena extendida, Esty); la ciega de contenido habria coronado a `gestion_eco_riesgos`, **que es EXACTAMENTE lo que la vara de condiciones dice** | **[[A72_CIEGA_46]]** |
| **47** | **UNA** familia (la terminacion del franquiciado, Siebert); ciego `gestion_terminacion_franquiciado`, el guion mas completo. **Coincide con la vara de pasos y con las dos razones** | **[[A72_CIEGA_47]]** |

> **LA CIEGA DEL `44` ES LA QUE MAS PESA, Y POR ESO VA APARTE:** las **DOS** coronas de contenido del
> auditor **SON EXACTAMENTE LAS DOS PUERTAS DEL ACTO** (linea **[[A72_CIEGA_44_PUERTAS]]**). **La
> trampa que el reporte de la vuelta 72 declaro queda confirmada desde fuera y a ciegas**, y con ella
> que **el `DECLARADO` de la guarda `1B` era la unica salida escrita**: no habia superviviente posible
> que no absorbiera a una puerta, ni por topologia ni por contenido.
>
> **`CERO` DISCREPANCIAS EN LA CIEGA** (linea **[[A72_CIEGA_CERO]]**), **y las coronas cruzadas del
> `45` quedaron leidas cada una sobre SU par**, que es el precedente que el acta 70 fijo.

### c) **LA TANDA 72 SALIO LIMPIA ENTERA, Y EL CONTADOR DE PARADA SIGUE EN `CERO` POR SEGUNDA TANDA SEGUIDA**

**Es la noticia que mueve el contador, y va con las tres cifras separadas en vez de con un limpia
suelto**, porque la regla de la parada distingue especies y no humores.

| | lo que el acta 72 escribe | linea |
|---|---|---:|
| **las tres especies, contadas por separado** | `CERO` caidas **de clase**, `CERO` **de cifra publicada**, `CERO` **de reporte**: toda cifra y todo nombre propio verificado **calza al digito** con las corridas del auditor | **[[A72_LIMPIA_CERO]]** |
| **las CINCO averias propias del ejecutor** | **ninguna llego a una cifra publicada**; cuatro las cazo un instrumento cayendo en `ROJO` **sin escribir** y una un censo corrido antes de tiempo a proposito | **[[A72_AVERIAS_EJEC]]** |
| **las DOS declaraciones de frente del reporte** | **son manejos correctos, NO caidas**: la celda que mentia se corrigio por carril con marca, y la fila del pendiente 4 se declaro **sin re-sellar un plan ejecutado** | **[[A72_LIMPIA_MANEJOS]]** |
| **las averias del propio auditor** | **cuatro, con nombre y sin cifra publicada de por medio**, escritas en su acta con la misma letra con la que se escriben las del ejecutor | **[[A72_AVERIAS_AUD]]** |
| **las caidas de la tanda, en la metrica** | `CERO` de clase, `CERO` de cifra publicada y `CERO` de reporte **del ejecutor**; `CERO` **de acta** del auditor | **[[A72_METRICA_CAIDAS]]** |
| **el acumulado, que sigue creciendo y no se reinicia** | relecturas, puestos y las caidas historicas de las dos partes, **cada especie con su columna** | **[[A72_METRICA_ACUM]]** |
| **LA RACHA DE CLASE O CIFRA PUBLICADA** | **`CERO` tandas** | **[[A72_RACHAS]]** |
| **LA RACHA DE REPORTE** | **`CERO` tandas, y es la SEGUNDA tanda limpia seguida** | **[[A72_RACHAS_REPORTE]]** |

> **LAS DOS RACHAS SE REGISTRAN POR SEPARADO PORQUE LA REGLA DE LA PARADA LAS CUENTA POR SEPARADO:**
> la de **clase o cifra publicada** para en **DOS** seguidas y la de **reporte** en **TRES**. **Que
> las dos esten en cero a la vez es lo que este registro deja escrito**, y la segunda tanda limpia
> seguida **es una medida de la tanda, no un permiso para la siguiente**.

### d) **LOS TRECE DISCUTIBLES, TODOS A FAVOR, CON LA VARA QUE CADA UNO CITA**

**La relectura ciega se hizo sobre los discutibles que el ejecutor habia marcado ANTES de saber si
acertaba**, que es la unica forma en que ese marcado vale algo.

| | el discutible | lo que el acta 72 adjudica, y por que letra | linea |
|---|---|---|---:|
| `D1` | la clausula de `OP-L-03` **no es identica al byte** y la correccion se aplico igual | **A FAVOR**: las cuatro varas del acta 65 son **de la REGLA y no de la letra exacta**, y **la discrepancia esta DECLARADA dentro de la correccion** en vez de resuelta copiando | **[[A72_D1]]** |
| `D2` | el `43` funde contra un cableado de **11 a 7** | **A FAVOR por la letra**: el cableado solo habla a contenido empatado y **la vara de condiciones hablo**; la ciega eligio el mismo nodo por el fondo | **[[A72_D2]]** |
| `D3` | el `43` crece de cinco pasos a ocho | **A FAVOR como medida**: los tres `APPEND` **estan nombrados por las razones como propios**, y la tendencia de los nodos grandes queda **ANOTADA para la fase 04, no convertida en tope** | **[[A72_D3]]** |
| `D4` | el `46` funde **con la puerta sobreviviendo** contra la unica vara que habla | **A FAVOR por la letra explicita** (acta 54, pregunta 1, con el `acto 20` de `OP-U-01` de precedente): **la puerta no se absorbe, gane o pierda en contenido**, y el choque va escrito en el motivo sellado | **[[A72_D4]]** |
| `D5` | `OP-S-09` queda con un alias **fuera de su familia** | **A FAVOR**: la cobertura es de **PARTE** de la nomina, que es el caso que el acta 70 resolvio; el sujeto queda **SERVIBLE** y **la consecuencia esta publicada en vez de callada** | **[[A72_D5]]** |
| `D6` | las dos razones del `45` coronan distinto **y los coronados tienen arista** | **A FAVOR**: cada corona es **sobre SU par**, las dos matan al mismo nodo, y **la arista es de secuencia y no una segunda familia**, con `P.10` confirmandolo por maquina | **[[A72_D6]]** |
| `D7` | el `47` funde a favor del **peor cableado** | **A FAVOR por la letra**: la vara de pasos habla y el cableado no habla a contenido no empatado; **el nodo hoja gana cableado con la propia fusion** y el afinado es de la fase 04 | **[[A72_D7]]** |
| `D8` | la fila del pendiente 4 **en sustancia**, con vehiculo `INCISO` | **A FAVOR el manejo**: declarar **sin re-sellar un plan ejecutado** es la letra del acta 68. **La pregunta de fondo va adjudicada aparte**, y es la que esta vuelta ejecuta | **[[A72_D8]]** |
| `D9` | la **celda corregida** de una tabla congelada | **A FAVOR**, adjudicado en la seccion de adjudicaciones y no aqui | **[[A72_D9]]** |
| `D10` | el `44` es **especie nueva** entre los declarados | **A FAVOR como registro**, adjudicado en la seccion de adjudicaciones | **[[A72_D10]]** |
| `D11` | **tres ficheros de aguja nuevos** en el registrador | **A FAVOR**: `AGUJAS` siempre fue un mapa de clave a fichero mas aguja **y el fichero es un DATO**; cero funciones y cero condiciones nuevas, verificado | **[[A72_D11]]** |
| `D12` | **cinco `INCISO`, dos al mismo acto** | **A FAVOR**: los cinco trozos **verbatim contra su fuente** y presentes en su resultante, los dos del `47` **a pasos distintos sin apilarse** | **[[A72_D12]]** |
| `D13` | el `45` cierra **sin una sola perdida de paso** | **A FAVOR**: `CERO` perdidas de paso contadas por el auditor, y **su lectura ciega confirma que el solape es casi total** | **[[A72_D13]]** |

### e) **LAS TRES ADJUDICACIONES NUEVAS, CON SUS LETRAS**

| | lo que el acta 72 adjudica | linea |
|---:|---|---:|
| **1** | **LA ESPECIE DEL PENDIENTE 4 LA DEFINE EL HECHO, NO EL VEHICULO**, y su **CORRECCION DECLARADA va encargada** sobre la glosa del instrumento | **[[A72_ADJ1]]** |
| **2** | **LA CELDA COPIADA QUE MIENTE SE CORRIGE POR EL CARRIL DEL ACTA 61, SIN PARAR**: la congelacion del acta 69 era contra el crecimiento y la edicion sin declarar, **no contra la correccion declarada de una falsedad MEDIDA** | **[[A72_ADJ2]]** |
| **3** | **EL `ACTO 44` ENTRA NOMBRADO APARTE EN EL PAQUETE DEL CIERRE DE LA FASE 03**, que es **parada de fundador**: hoy no se decide su salida | **[[A72_ADJ3]]** |

**LA PRIMERA VA VERBATIM Y NO RESUMIDA, PORQUE ES LA QUE ESTA VUELTA EJECUTA Y UNA REGLA QUE SE
PARAFRASEA SE DEFORMA** (la cita arranca en la cabecera de la adjudicacion y se copia tal cual):

[[VERBATIM:A72_ADJ1:10]]

> **EL HECHO Y EL VEHICULO, SEPARADOS EN LA LINEA DONDE EL ACTA LOS SEPARA** (linea
> **[[A72_ADJ1_HECHO]]**): la marca existe porque **una perdida cuya sustancia LLEGA ENTERA desde otro
> absorbido del mismo acto es mas barata que una perdida seca**, y **ese hecho no depende del
> vehiculo**. **El nombre historico nombra el `APPEND` porque el `APPEND` era el unico vehiculo que la
> producia cuando la marca nacio; el `INCISO` nacio despues.**
>
> **LO QUE SE ENCARGA Y LO QUE NO SE TOCA, QUE VA EN OTRA LINEA Y POR ESO SE CITA APARTE** (linea
> **[[A72_ADJ1_ENCARGO]]**): se encarga **la CORRECCION DECLARADA de la glosa** con el texto viejo
> verbatim en el docstring; **la busqueda y la aritmetica NO se tocan.**
>
> **Y LA TERCERA DECISION DE LA MISMA ADJUDICACION, QUE ES UNA NEGATIVA Y TAMBIEN VA EN SU PROPIA
> LINEA** (linea **[[A72_ADJ1_NORESELLA]]**): **el plan del lote `H` NO se re-sella**, por el `D15`
> del acta 68. **Su fila queda declarada donde ya esta**, y **la cuenta publicada era la cuenta del
> instrumento, correcta sobre lo sellado**. **Corregir la glosa NO reabre el plan.**

**LA SEGUNDA ADJUDICACION DEJA UN CARRIL ABIERTO PARA LA PROXIMA CELDA QUE MIENTA, Y SE REGISTRA CON
SU BORDE** (linea **[[A72_ADJ2_CONGELO]]**): **la adjudicacion 3 del acta 69 congelo las tablas de los
registradores contra el CRECIMIENTO y contra la edicion sin declarar, no contra la correccion
declarada de una falsedad MEDIDA.** **El carril tiene DOS condiciones y las dos son obligatorias:
enumerar el texto viejo VERBATIM y marcar el cambio como discutible.** **Cumplidas las dos, se corrige
sin encargo previo y sin parar.** **Publicar una afirmacion que la vuelta no midio seria una caida
fabricada a sabiendas.**

**LA TERCERA MANDA EL `ACTO 44` A UNA PARADA QUE YA EXISTE, Y NO INVENTA NINGUNA** (linea
**[[A72_ADJ3_SEDE]]**): **el `CIERRE DE LA FASE 03` es parada de fundador desde el 21 ago 2026.**
**Y el motivo de que sea especie propia esta en la linea siguiente y por eso se cita aparte** (linea
**[[A72_ADJ3_CATORCE]]**): **los CATORCE anteriores esperan por `P.10` o por su familia; el `44`
espera porque la guarda `1B` NO ORDENA LAS PUERTAS ENTRE SI**, y **ninguna regla escrita ordena hoy
esa eleccion**. **Decidirlo en el bucle seria doctrina nueva.** **Sus tres nodos y sus dos puertas no
se tocan.**

### f) **LAS TRES OBSERVACIONES DE LECTURA SIN CARGO, REGISTRADAS EN VEZ DE TRAGADAS**

**El acta 72 las llama asi ella misma** (linea **[[A72_OBS]]**): **son lecturas que NO son caidas y que
el auditor escribio igual, para que nadie las lea como tragadas.** **Se registran aqui las tres con su
linea, porque una observacion que solo vive en el acta se pierde en la vuelta siguiente.**

| | lo que el acta observa, sin cargo | linea |
|---:|---|---:|
| **a** | **la celda del censo de codificacion del reporte cuenta un fichero menos de los que hoy existen**, y **la lectura consistente es que el censo corrio antes de que existiera la ultima salida**; **la SUSTANCIA la verifico el auditor sobre todos: `CERO` fuera de `UTF-8`** | **[[A72_OBS_A]]** |
| **b** | **el `--diff-filter=M` sobre `scripts/` devuelve tambien el banco de rumbos, que es DATO y no instrumento**, y **cuyo diff el reporte declara aparte**: la frase de UN SOLO instrumento modificado **es correcta filtrada a instrumentos** | **[[A72_OBS_B]]** |
| **c** | **la arista del `D6` dicha con precision**: lo medido es **UNA arista dirigida vista de sus dos extremos**, y no dos aristas | **[[A72_OBS_C]]** |

> **LA TERCERA SE REGISTRA CON SU MEDICION Y NO SOLO CON SU NOMBRE, PORQUE ES LA UNICA QUE AFINA UNA
> FRASE PUBLICADA** (linea **[[A72_OBS_C_ARISTA]]**): el auditor midio que
> `evitar_shopping_bag` esta **en los siguientes** de `reconstruccion_contexto_situacional` **y** que
> `reconstruccion_contexto_situacional` esta **en los previos** de `evitar_shopping_bag`. **Eso es una
> sola arista mirada desde sus dos puntas.** **El hecho que el `D6` necesitaba (que los dos coronados
> SI tienen arista, a diferencia del precedente) es cierto tal cual**, asi que **la observacion afina
> la frase y no mueve la adjudicacion**, que quedo `A FAVOR`.

### g) **CORRECCION DECLARADA, UNICA DE ESTA VUELTA: LA GLOSA DE LA ESPECIE DEL PENDIENTE 4**

**El instrumento es de nombre estable** (`cuenta_agregada_de_perdidas.py`) **y por eso la correccion va
por el carril declarado**, el mismo que `generar_plan_del_lote.py` uso en las vueltas 63, 65 y 72: **el
texto viejo se queda entero, citado VERBATIM en el docstring, y no se tacha.**

**EL TEXTO VIEJO, ENTERO Y ARRIBA, LEIDO HOY DEL PROPIO INSTRUMENTO:**

> `la frase sellada ATENUANTE DECLARADO, las que ademas son de la ESPECIE DEL`
> `PENDIENTE 4, las que llevan ATENUANTE DECLARADO Y MEDIDO`

**ESO NO ERA FALSO Y NO SE CORRIGE: SIGUE SIENDO EXACTAMENTE LO QUE EL INSTRUMENTO CUENTA.** **Lo que
faltaba no era una cuenta sino UNA DEFINICION**, y su ausencia se pago en la vuelta 72: la fila del
`acto 43` de aquel lote **cumplia el hecho y llegaba por `INCISO`**, y la celda salio en `0` con
glosa. **Un lector que solo tuviera delante el nombre historico de la marca podia entender que el
vehiculo mandaba.**

**LO QUE LA CORRECCION ESCRIBE** (linea **[[CUENTA_HECHO]]**): que **una fila es de esta especie
cuando LA SUSTANCIA QUE SE PIERDE LLEGA ENTERA DESDE OTRO ABSORBIDO DEL MISMO ACTO, sea el vehiculo un
`APPEND` o un `INCISO`**, con el motivo de la adjudicacion escrito al lado.

**LO QUE LA CORRECCION NO TOCA, Y SE DICE PARA QUE SE PUEDA MEDIR** (linea **[[CUENTA_NOTOCA]]**): **la
BUSQUEDA y la ARITMETICA se quedan como estaban, byte a byte.** La constante de la frase sellada sigue
siendo la misma cadena, la nomina sigue buscandola dentro del mismo campo, y **la tupla de pistas
conserva la que nombra el vehiculo**: esa tupla **no define la especie**, solo delata prosa de
atenuante sin sello, y **estrecharla o ensancharla seria mover la busqueda**.

**LA SEDE DE LA CORRECCION, CITADA POR AGUJA Y NO TECLEADA:** el bloque declarado abre en la linea
**[[CUENTA_CORRECCION]]** de
[`../../scripts/loop/cuenta_agregada_de_perdidas.py`](../../scripts/loop/cuenta_agregada_de_perdidas.py).

> **LA PRUEBA DE QUE LA CORRECCION ES DE GLOSA Y NO DE MAQUINA SE MIDE Y NO SE PROMETE:** el
> instrumento de la correccion **compara byte a byte todo lo que va del final del docstring en
> adelante** antes y despues, **y solo escribe si es IDENTICO**. **Y el caso positivo del instrumento
> se re-corrio despues**, con **sus cinco mitades en verde**: la cuenta, la exclusion dicha, la fila
> de dos sedes y el total salen igual que antes de la correccion. **Una glosa que moviera una cifra no
> seria una glosa.**

### h) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**

| pendiente | su destino, dicho y no supuesto |
|---|---|
| **los `DECLARADOS Y NO FUNDIDOS` que esperan el cierre de la fase 03** | **QUINCE**, y **esperan la PARADA DEL FUNDADOR**: el acta 72 recorre las condiciones de parada y dice que **el cierre de la fase 03 NO SE CUMPLE TODAVIA** (linea **[[A72_CIERRE03]]**), porque **quedan actos sin destino, dos de ellos con dueno, la mesa `OP-M-03`, y los quince esperando con el `44` como especie propia** (linea **[[A72_CIERRE03_QUEDAN]]**) |
| **el `acto 44`, dentro de esos quince** | **NO es uno mas**: entra **NOMBRADO APARTE** en el paquete de ese cierre, con **sus DOS puertas y la figura `ESTRELLA`** dichas, porque **espera por una pregunta distinta de la de los catorce** |
| **el subconjunto cerrado de un acto con puente** | **PENDIENTE NOMBRADO sin urgencia medida**: en lo que resta del tramo unico **no hay ningun acto con nodo puente**, asi que **la lista ya no puede crecer por `P.10` en este tramo** |
| **la marca para *ya lo dice el `APPEND` de un hermano*** | **PENDIENTE NOMBRADO, y la definicion YA no es ambigua**: la adjudicacion 1 la ata **al HECHO** y la glosa del instrumento lo escribe. **Lo que sigue sin existir es la marca propia**, no su definicion |
| **el `INCISO` de condiciones** | **SIGUE SIN EXISTIR**: solo hay `INCISO` de pasos. Las perdidas `DE CONDICIONES` se **sellan con su motivo** y van **enrutadas a la fase 04** por el carril del acta 55, pregunta 5 |
| **el esquema de `OPERACIONES.jsonl`** | **PENDIENTE HEREDADO** (acta 55 en su cierre, acta 64 en su `D7`), **y esta vuelta NO lo toca**: la unica correccion declarada de la `TAREA 1` vive en un instrumento, no en una ficha |

### i) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las siete colisiones vigentes**, **NO toca la mesa `OP-M-03` ni sus dos colisiones**, **NO toca las
CINCO colisiones de `OP-U-02` ya publicadas**, **NO ejecuta ninguna de las cinco fichas `OP-M-02`
consumidas** (lo consumado no se ejecuta ni se rehace), **NO funde ningun acto con dueno** (el `31` y
el `37` quedan con los suyos), **NO toca ni un nodo, ni un alias ni una puerta del `acto 44`**, **NO
re-sella el plan del lote `H`** (que es la adjudicacion 1 del acta 72 cumplida a la letra en su parte
negativa), **NO decide la salida del `44`** (esa es parada de fundador), **NO abre la fase 04**, **NO
borra ni tacha el texto viejo que la correccion cita**, **NO mueve la busqueda ni la aritmetica del
instrumento corregido**, **NO mueve la linea base del censo de colisiones** (la mueve el auditor) y
**NO anade ni una fila ni una columna a ninguna tabla de registrador**, que es la adjudicacion 3 del
acta 69 aplicada sobre el instrumento que la registra.
"""
