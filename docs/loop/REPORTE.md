# REPORTE DE LA VUELTA 33 (ejecutor Opus 5). FASE III, rama `pasada-unica`

**LAS TRES CORRECCIONES DEL REGISTRO ESTAN HECHAS, LAS TRES CLASES RELEIDAS ESTAN VOLCADAS CON SU
BARRIDO, EL ACTO DE `OP-D-02` SE LEYO ENTERO Y SU FUSION SE EJECUTO: es la PRIMERA fusion del plan
de la pasada unica que se escribe contra `dataset/`. Los tres congelados que ese nodo bloqueaba
salieron de la lista. Y el modo continuo se detuvo en `OP-D-03` con una PARADA de tres motivos
medidos y CERO nodos tocados: el instrumento de costuras se declara a si mismo MAL CALIBRADO.**

- **Hash de partida:** `3f196b73` (el commit del fundador con la decision).
- **Hash final:** ver el ultimo commit de `origin/pasada-unica`. **Siete commits de trabajo**, el
  primero de ellos la APERTURA medida antes de tocar nada (`e1105299`).
- **Rutas tocadas** (`git diff --stat e1105299..HEAD`, corrido hoy): **67 ficheros, 6.539
  insertadas, 138 borradas**. Por carpeta: `docs/loop` **38**, `scripts/loop` **12**, `docs/plan`
  **5**, `dataset/nodos` **5**, `docs` **3**, `web/lib/assets` **2**, `dataset/metadata` **2**.
  **Cero merges.** El hook corrio verde en los siete commits.
- **`dataset/nodos` son CINCO ficheros y ninguno mas:** `voz_del_cliente_voc`,
  `enfoque_mercado_voc`, `homework_frontend_loading`, `procesamiento_paralelo_con_espirales` y
  `ventaja_competitiva_producto`. **Ningun nodo nacio, ninguno se borro, y uno murio**
  (deprecado), que es exactamente lo que una fusion hace.

---

## 1. EL ESTADO, APERTURA CONTRA CIERRE

**Las dos columnas son de dos corridas del MISMO instrumento** (`scripts/loop/vuelta31_estado.py`,
el mismo que cerro la vuelta 32): la de **APERTURA** corrida **antes de la primera operacion** y
commiteada antes de tocar nada (`e1105299`, salida `SALIDA_V33_APERTURA.txt`), y la de **CIERRE**
corrida **al cerrar** (`SALIDA_V33_CIERRE.txt`). **El instrumento no cambio entre columnas.**
Ninguna cifra viene de un acta ni de un reporte anterior.

| | **APERTURA** | **CIERRE** |
|---|---:|---:|
| marcador: n / A / B / C / D | 3.388 / 583 / 89 / 7 / 2.709 | **3.388 / 582 / 84 / 8 / 2.714** |
| huecos / duplicados / clases fuera de ABCD | 0 / 0 / 0 | **0 / 0 / 0** |
| grafo: ficheros / ids / vivos / deprecados | 3.853 / 3.853 / 3.539 / 314 | **3.853 / 3.853 / 3.538 / 315** |
| enlaces / claves distintas | 16.848 / 15 | **16.852 / 15** |
| familias Weinberg / Horowitz / Hugos / Coleman / Rackham (vivos) | 72 / 93 / 111 / 75 / 47 | **identicas** |
| operaciones / estados / dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| inventario | 672 | **672** |
| indice rojo declarado | 18 lineas, 0 ausentes | **18 lineas, 0 ausentes** |
| fronteras de `OP-F-04-COL` | 14 de 15 | **14 de 15** |
| **superviviente de `OP-D-02`** | **`null`** | **`voz_del_cliente_voc`** |

> **EL MARCADOR SE MOVIO POR PRIMERA VEZ EN SEIS VUELTAS, y esa es la firma de esta.** Se movio
> **dos veces y en dos actos separados**, y las dos con **la cifra esperada escrita ANTES de
> correr el instrumento**, con orden de PARAR si daba otra cosa. **Las dos veces dio exactamente
> lo escrito.** `n` **no se movio**: las tres lecturas dirigidas nuevas **no entran en la cola**.

> **EL GRAFO SE MOVIO EN UN NODO, Y ESO TAMBIEN ES LA FIRMA.** Vivos **3.539 a 3.538** y
> deprecados **314 a 315**: **la fusion, y nada mas que la fusion.** El censo de ficheros **no se
> mueve** porque **una fusion depreca, no borra**.

> **LOS CUATRO ENLACES DE MAS ESTAN MEDIDOS Y NO SE PASAN POR ALTO** (`SALIDA_V33_ENLACES.txt`).
> Yo esperaba **menos uno** (la duplicada que la fusion limpia) y el instrumento da **mas cuatro**.
> **Nacen del RECIPROCADO de `Gate 0`**: al redirigir dos entradas hacia el superviviente, la
> pasada de curaduria escribio la arista de vuelta dentro del propio superviviente. **Ninguna
> arista se escribio a mano en esta vuelta.** Y eso abre la caida de la seccion 6, que va
> declarada y sin arreglar.

> **La tasa por dominio SI se movio, y solo en `core`**, porque los seis veredictos volteados son
> los seis de `core`: de `A 344, B 87, C 7, D 1.007` a **`A 343, B 82, C 8, D 1.012`**. **Los
> otros nueve dominios, identicos al digito** (`SALIDA_V33_TASA_DOMINIO_B.txt`). **La vara por
> tramo es cifra del cribado y esta vuelta no leyo ningun par de la cola: no se mueve, y no se
> copia de ningun lado para rellenar la tabla.**

---

## 2. TAREA 1.1, LA CELDA DEL ORIGEN 16. **EL MOTIVO TENIA RAZON Y LA CELDA ESTABA MAL**

**La medicion del dia, impresa ANTES de tocar nada** (`vuelta33_corregir_16.py`): el paso 16
original dice *Desarrolla tu primera version de forma incremental, en ciclos cortos e iterativos*.
**Es la CADENCIA**, que es el paso 6 del resultado, **no el conjunto minimo** del paso 2. Los tres
que si son el conjunto minimo (**6**, **15** y **19**) empiezan los tres por *Define el conjunto
minimo de caracteristicas*, y el 16 no.

**EL TEXTO DEL NODO NO SE TOCO, y no es una opinion: es una INVARIANTE QUE EL INSTRUMENTO
COMPRUEBA Y QUE LE HACE ABORTAR SI NO SE CUMPLE.** `vuelta32_podar.py` toma el superviviente por
el **primer origen del grupo** y el texto por `pasos_finales`. **`min` del grupo del paso 2 sigue
en 2 y el del paso 6 sigue en 8** con el 16 dentro o fuera, y la cobertura sigue en **22 de 22**.

**TRES CAMPOS DEL PLAN SELLADO CARGABAN LA MISMA PARTICION Y LOS TRES SE CORRIGIERON**, con las
particiones viejas enteras dentro de un bloque `correcciones_declaradas` del propio JSON:
`grupos_pasos` (el que el encargo nombra), **`mapa_pasos` (el campo OPERATIVO, el que el ejecutor
consume)** y `pruebas_repeticion`. **Corregir solo el primero habria dejado el plan
contradiciendose consigo mismo y al verificador en verde encima de la contradiccion.**

> **UN LIMITE DICHO PARA QUE NADIE LE ATRIBUYA AL VERDE LO QUE NO MIDIO:** la huella de la prueba
> de repeticion de ese grupo es *conjunto minimo de caracteristicas*, **que el paso 16 nunca
> contuvo**. La prueba **jamas midio al 16**, porque cuenta la huella sobre el nodo resultante y
> solo IMPRIME los origenes. **La celda mala no falseo ningun verde: no habia instrumento que la
> leyera.** Ese es el hueco exacto que el verificador de mapas cierra.

**Y LA TABLA YA NO ESTA TECLEADA: ESTA IMPRESA**, con `vuelta33_tabla_mapa.py`, instrumento nuevo,
y el comando citado al lado en el documento. La tabla vieja **se queda entera y tachada, cabecera
incluida**, y eso ultimo no es cosmetica: **asi el verificador no lee como vigente una tabla
retirada**.

---

## 3. TAREA 1.2, EL MOTIVO 2 DE LA PARADA: **CERO DE TRES, NO DOS DE TRES**

**La causa esta medida y es de la misma especie que la del origen 16.** El detector de ganador de
`vuelta32_acto_opd02.py` preguntaba `"gana" not in razon.lower()`: **un SUBSTRING**. Y el substring
`gana` vive dentro de `ganar`. **La razon del puesto 526 dice *saltarse la validacion por GANAR
TIEMPO***, y el detector leyo ahi un ganador que no existe.

**LAS DOS CORRIDAS SE PUBLICAN Y LA DIFERENCIA SE DECLARA**, en vez de resolverse sustituyendo:

| detector | pares A que nombran ganador |
|---|---:|
| **VIEJO**, substring `gana` | **1 de 3** |
| **NUEVO**, vocabulario de adjudicacion con frontera de palabra | **0 de 3** |

**El instrumento nuevo imprime la palabra culpable por su nombre** (`FALSO POSITIVO, y aqui esta
la palabra: 'ganar'`) **y la razon ENTERA de cada par A**, porque su vara sigue siendo lexica y no
un lector de espanol, y eso va escrito dentro.

**DOS COSAS QUE NO SE TOCARON, con su motivo.** La `nota` de `OP-D-02` en `OPERACIONES.jsonl`
**leida hoy entera**: no afirma que el 526 nombre ganador, nombra al 386 y al 788 y concluye bien.
Y `SALIDA_V32_PARADA_OPD02.txt` tampoco se reescribe: **una salida vieja se contrasta, no se
maquilla.**

---

## 4. TAREA 1.3, EL VOLCADO Y EL BARRIDO DEL `9.10`

**Las tres clases releidas en la vuelta 32 y dejadas sin escribir se volcaron**, con la
adjudicacion del fundador y el `9.10` como mecanismo: **494 de `A` a `C`** (banco `9.22`, tercer
ejemplar del archivo, con **enlace mutuo** declarado y sin poner), **592 de `B` a `D`** y **830 de
`B` a `D`** (arista que falta).

**LA RAZON VIEJA NO SE TECLEO: SE COPIO POR MAQUINA**, y `vuelta33_volcado_910.py` **aborta si la
razon vieja no queda literalmente dentro de la nueva**. Conservados **865, 1.359 y 962**
caracteres.

**EL BARRIDO, EN EL MISMO ACTO** (`vuelta33_barrido_910.py`, **77 candidatos listados sin ocultar
ninguno**). Lo corregido:

| documento | que se corrigio |
|---|---|
| `INTRA_DOMINIO_INFORME.md` | el marcador de `100.1`, la tasa por dominio de `100.2` y el *total de A en el archivo* de `100.6` |
| `PENDIENTES.md` | congelados **13 a 10**, cola **19 a 16**, la tabla de pares que libera el emblema y la de *clase hoy* |
| `RECOMPUTO_3388.md` | **el instrumento se volvio a correr entero**: A **583 a 582**, nodos con A **854 a 852**, componentes **335 a 334**, cerradas **280 a 279**. **Las cuatro comprobaciones vuelven a dar OK** |
| `RECOMPUTO_3388_COMPONENTES.jsonl` | **reescrito por el propio instrumento**: muere la componente de tamano 2 del 494 |
| `02_DESTEJIDOS.md` | la tabla del orden, el bloque del 494 congelado, la tabla del movimiento 4 y el bloque de *lo que esta vuelta NO escribe* |

> **EL BARRIDO SE ARREGLO A SI MISMO A MITAD DE CAMINO, y se dice:** su primera version **no veia
> la tabla del marcador del informe**, porque la fila se escribe `| **A** | **583** (17,2 %) |`,
> sin ninguna de las palabras que buscaba. **Una tabla derivada que el barrido de tablas derivadas
> no ve es exactamente la averia que el `9.10` nombra.** Se le anadio la vara de las filas de
> tabla, y entonces aparecio.

> **LO QUE EL BARRIDO NO TOCO, con su motivo y no callado:** las **trece** filas de checkpoints
> anteriores del informe que citan `core` con **A 344**, y las salidas viejas de `docs/loop`.
> **Cada una es la foto de su propio corte**, y reescribirlas fabricaria corridas que nunca
> existieron. **Va como pendiente de doctrina.**

---

## 5. TAREA 2.1, LAS TRES LECTURAS DIRIGIDAS: **`LD-72`, `LD-73` y `LD-74`, las tres `D`**

**Los cuatro nodos se imprimieron ENTEROS antes de decidir nada** y **se verifico contra
`INTRA_DOMINIO_PARES.jsonl` que ninguno de los tres pares esta en la cola**, que es lo que los
hace lectura dirigida y no par saltado. **`n` no se movio.**

> **UN GUARD PROPIO ATRAPO UN ERROR MIO ANTES DE ESCRIBIRLO:** iba a numerarlas `LD-66` a `LD-68`
> **y esos numeros estaban tomados** (el lote del sales roadmap, en otro fichero que mi primer
> barrido no miro). Medido despues sobre `docs/` entero, el maximo es **71**, **y el 71 esta
> tomado por una decision escrita de NO acunarlo**. Se quema y se empieza en **72**.

**LA RESPUESTA A `P.5`, y no es la que la operacion esperaba: NI UNA FAMILIA NI DOS.** Las tres
`A` (386, 788, 526) forman **un CAMINO** y **las tres cuerdas largas son `D`**: **cero triangulos
cerrados** y **DOS nodos puente**, que es el **segundo puente doble del archivo** por `P.10`. La
salida que `P.10` nombra es **fundir solo el subconjunto cerrado y enlazar el resto**, y ese
subconjunto es **el par del puesto 386**.

> **Y lo que eso confirma:** el ORDEN INTERNO escrito de `OP-D-02` **ya decia esto sin saberlo**.
> Manda *fundir con `enfoque_mercado_voc`* y de los otros dos solo **tener delante**. **La lectura
> no cambio el alcance: le dio la medicion que le faltaba.**

---

## 6. TAREAS 2.2 y 2.3, EL SUPERVIVIENTE Y **LA PRIMERA FUSION DEL PLAN**

**No hay GANADOR POR DERECHO** (0 de 3 pares A con victoria citable). **GANADOR POR ELEGIR por
`P.8`, contenido primero, y el contenido habla en TRES sitios:** el campo `preservar` de la propia
operacion declara la direccion; el procedimiento del objeto que da nombre al acto vive entero en
`voz_del_cliente_voc`; y la verificacion escrita exige releer 724, 755 y 827 **contra el
superviviente**, y los tres son pares contra el. **El cableado solo confirma**: 13 aristas contra
4, y 12 nodos vivos que lo nombran contra 3.

**LA FUSION, con nueve guardas escritas para caer, todas verdes.** El superviviente pasa de
**cinco pasos a SEIS** con el `preservar` **INTEGRO** (las tres piezas verificadas **literales**),
tres condiciones, entregable y resumen absorbidos, alias y `merged_originals` puestos. **El
absorbido queda deprecado con su TEXTO INTACTO y su fichero en pie.**

| guarda | resultado |
|---|---|
| simulacion previa sobre copia en memoria (`P.7`) | **verde**, mas la del instrumento sellado de la casa |
| guarda de texto sobre los DOS nodos | **15 de 15** calzan con su prefijo sellado |
| cobertura exacta | **10 de 10** en pasos, **5 de 5** en condiciones |
| el `preservar`, literal | **3 de 3** |
| **caso positivo ANTES** | **10 PASAN, 13 CAEN** |
| **caso positivo DESPUES** | **23 PASAN, 0 CAEN** |
| conservacion (aparte) | **de 3 a 10 rastros vivos de 10** |
| cero auto arista y cero duplicada, en TODO el grafo | **OK** |
| el censo no se mueve | **3.853 antes y despues** |

**`Gate 0` exit 0 con `GATE 0: OK`**, 3.853 compilados, universo **3.538 activos y 315
deprecados**; etiquetas **71**; `plan_readiness` 3.853; sync verde; **motor 24 de 24**, **web 80
ficheros con 1.030 pasadas y 3 saltadas**, **`tsc` cero lineas**.

> **UNA GUARDA CAZO UNA DISCREPANCIA REAL Y POR ESO SE SABE QUE SIRVEN.** El plan esperaba **TRES**
> redirecciones (las que da el instrumento de la casa sobre el grafo compilado) y el ejecutor,
> contando sobre `dataset/nodos`, **encontro CUATRO y ABORTO SIN ESCRIBIR**. La cuarta es
> `front_end_homework`, **que esta DEPRECADO**. Se adopta el criterio del instrumento sellado
> (**solo se redirige lo vivo**) y **la cuarta va DECLARADA en el plan, no filtrada en silencio**.

### 6.1 **UNA CAIDA MIA, MEDIDA AL CIERRE Y DEJADA CAYENDO A PROPOSITO**

> **EL RECIPROCADO DE `Gate 0` DESHACE PARTE DE LA REDIRECCION DE UNA FUSION.** Medido al cerrar
> (`SALIDA_V33_ENLACES.txt`): `enfoque_mercado_voc` **volvio a aparecer**, al final de la lista, en
> los tres nodos vivos de los que lo habia quitado. **La causa es que el absorbido conserva sus
> propias aristas** (que es lo que hace auditable la fusion) **y `Gate 0` las reciproca.**
>
> **Corri el caso positivo OTRA VEZ, ya despues de `Gate 0`, y lo publico cayendo**
> (`SALIDA_V33_OPD02_CASO_TRAS_GATE0.txt`): **22 PASAN, 1 CAE**, y el que cae es
> *ningun nodo VIVO sigue nombrando a `enfoque_mercado_voc`* (**quedan 3**).
>
> **NO LO ARREGLO Y NO AFLOJO LA PRUEBA, y digo las dos razones.** Volver a redirigir **lo
> desharia el siguiente `Gate 0`**, asi que seria un verde que dura hasta la proxima corrida; y
> aflojar la prueba seria **la segunda guarda que toco en el mismo dia**, que es justo de lo que
> mas hay que desconfiar. **Dano medido: NINGUNO hoy**, porque el resolutor manda
> `enfoque_mercado_voc` a `voz_del_cliente_voc` por su alias, y `Gate 0` y las tres suites estan
> verdes. **Pero es una deuda que envejece y va como pendiente de doctrina 1.**
>
> **Y hay que decir el orden en que paso, porque es la leccion:** el caso positivo se corrio
> **antes** del ciclo de `Gate 0` y dio 23 de 23. **Si no lo llego a correr otra vez al cerrar, la
> vuelta publica un verde que ya no era verdad.** Es el mismo renglon de la regla 1 del
> `EJECUTOR.md`: **el estado al cierre se mide al cierre.**

---

## 7. TAREA 2.4, LOS TRES CONGELADOS, RELEIDOS Y VOLCADOS

**Los tres estaban en `B` por el TOQUE UNICO del banco `9.4` y esa causa cayo.** Releidos contra
los SEIS pasos de hoy del superviviente y volcados en el mismo acto: **724, 755 y 827, los tres a
`D`**. **`voz_del_cliente_voc` sale entero del orden de la cirugia: no le queda ningun par
congelado.**

**LA GUARDA DEL ENCARGO, COMPROBADA Y NO SUPUESTA:** si el **724** hubiera dado **`A`**,
`voice_of_customer_estrategico` entraba al acto por `P.6` y **habia que PARAR**. **NO da `A`**, y
el motivo esta medido: trae un protocolo de interrogacion y registro (*que los mantiene despiertos
por la noche*, el *porque* de cada peticion, las *necesidades futuras*, los *ahas*) que el
superviviente no tiene en ninguno de sus seis pasos.

> **UNA LECCION DE METODO QUE LA VUELTA NO BUSCABA:** **antes de la fusion, el 724 estaba mucho
> mas cerca de `A`**, porque el superviviente era solo la observacion de campo. **Fue la fusion la
> que lo separo.** Es exactamente por lo que el `9.4` congela: **el mismo par da dos clases
> distintas segun el dia en que se lea.**

**EL RECOMPUTO SE VOLVIO A CORRER, y la FUSION si lo mueve aunque el volteo no:** el par 386
**COLAPSA a auto arista** al resolver por alias, **el primer colapso de la campana**, y el
instrumento lo nombra. Retrato **582 a 581**, nodos con A **852 a 851**, abiertas **254 a 253**
nodos. **Las cuatro comprobaciones, OK.** Corregida la frase del cuerpo que decia que *ninguna
fusion del plan se ha ejecutado*, **que era cierta el 13 ago**.

---

## 8. TAREA 2.5, **PARADA EN `OP-D-03`**. Cero nodos tocados

**`scripts/costuras_internas.py` SE DECLARA A SI MISMO MAL CALIBRADO Y SALE SIN ENTREGAR.** Su
propio encabezado escribio la regla que ahora lo detiene. **La baranda funciono; lo que hay que
decir es que llevaba tiempo funcionando y nadie lo habia corrido entero.**

**LA CAUSA, ESTRUCTURAL Y MEDIDA:** la senal de bloque recorre `range(MIN_BLOQUE, n - MIN_BLOQUE +
1)` con `MIN_BLOQUE = 3`. **Con CINCO pasos ese rango es VACIO y la senal devuelve `(0,0)`
siempre**, diga lo que diga el texto. **Y los DOS nodos de calibracion tienen cinco pasos hoy.**
Su docstring declara parejas de **60,0** y **54,7**; medidas hoy dan **47,1** y **54,3**.

> **CAIDA DE CIFRA PUBLICADA QUE ESTO ARRASTRA, declarada y NO arreglada por mi.** El **MOVIMIENTO
> 2 de `OP-D-01`** (acta 32) concluye que `principio_calidad_mvp` *no tiene costura interna* y lo
> sostiene en **pareja 51,2 contra 80** y **bloque 0,0 contra 44**. **La primera sigue en pie. LA
> SEGUNDA NO MIDE LO QUE DICE MEDIR:** ese 0,0 **no es un nodo sin bloque, es una senal que hoy
> devuelve 0,0 para todo**, incluidos los dos nodos que el instrumento sabe que son costura.
>
> **Y hay que decir COMO paso:** `vuelta32_costura_opd01.py` **importa** las senales y los
> umbrales, que es mas honesto que copiarlos, **y ademas pasa POR ENCIMA de la puerta de
> calibracion**, que vive en el `main()`. **Una guarda que se saltea importando por debajo es un
> test verde y mal.**
>
> **LO QUE ESTA CAIDA NO DICE:** no dice que la conclusion sea falsa. Su otra pata es **textual** y
> no depende del instrumento. **Lo que cae es la mitad instrumental de su apoyo.**

**Los otros dos motivos:** no se puede saber **cuales son las TRES costuras** que el orden interno
manda destejer (**ninguno de los seis nodos dispara ninguna senal hoy**, y ese 0,0 no se puede
leer como *no hay bloque*); y el acto esta a **8 de 15** pares, que **esta vez no se puede
resolver leyendo**, porque `P.5` manda leer **despues** del destejido y el destejido es lo que
esta bloqueado.

---

## 9. INSTRUMENTOS NUEVOS Y CORREGIDOS, todos con su motivo dentro

| instrumento | que es | el motivo |
|---|---|---|
| `vuelta33_tabla_mapa.py` | **NUEVO**, imprime la tabla desde el plan sellado | la cura de adelante de la regla del 15 ago: el verificador valida lo escrito, este lo **escribe desde la fuente** |
| `vuelta33_corregir_16.py` | **NUEVO** | corrige los tres campos y **aborta si la invariante que protege al nodo no se cumple** |
| `vuelta33_acto_opd02.py` | **SUCESOR** de `vuelta32_acto_opd02.py` | detector de ganador por **vocabulario con frontera de palabra**; publica **las dos corridas** y la razon entera |
| `vuelta33_volcado_910.py` y `_b.py` | **NUEVOS** | copian la razon vieja **por maquina** y **abortan si no queda dentro**. **No escriben el archivo**: eso lo hace el instrumento de la casa |
| `vuelta33_barrido_910.py` | **NUEVO** | el barrido del `9.10`, **sin tope y sin ocultar nada**, con su limite lexico declarado |
| `vuelta33_ld_opd02.py` | **NUEVO**, solo lectura | imprime los cuatro nodos **enteros** y prueba que los tres pares **no estan en la cola** |
| `vuelta33_superviviente.py` | **NUEVO** | escribe la eleccion con el `null` viejo dentro; **aborta si el campo ya no esta en `null`** |
| `vuelta33_plan_opd02.py` | **NUEVO**, constructor | **lee del grafo** los textos, prefijos y fuentes; cuatro guardas, una de ellas que el `preservar` quede **literal** |
| `vuelta33_fundir.py` | **NUEVO** | la maquinaria de fusion que no existia: **nueve guardas**, y **aborto sin escribir** si las redirecciones no son las del plan |
| `vuelta33_caso_positivo.py` | **SUCESOR** de `vuelta32_caso_positivo.py` | anade **muerte del absorbido**, **alias y ficha** y **redirecciones**, que en un destejido no tenian sentido |
| `verificar_mapas_destejido.py` | **CORREGIDO** | vara 2 generalizada a **N tablas contra N planes** (*toda tabla calza con algun plan y todo plan tiene su tabla*), y el **limite de la forma de fusion declarado en el codigo** |

**Y el verificador se probo EN ROJO, dos veces, para que el verde signifique algo** (`P.14`): con
la caida del acta 32 reintroducida **cae**, y con un motivo que cita un origen ajeno **cae**.
**Verde vigente: 2 tablas, 12 filas, 0 discrepancias.**

---

## 10. CORRECCIONES DECLARADAS DE ESTA VUELTA

1. **La celda del origen 16**, en los tres campos del plan sellado, con las particiones viejas
   dentro y la tabla impresa.
2. **El motivo 2 de la parada**, de *dos de tres* a **cero de tres**, con la palabra culpable
   nombrada y las dos corridas publicadas.
3. **El marcador y sus tablas derivadas**, dos veces, con el recomputo re corrido entero las dos.
4. **La frase de `RECOMPUTO_3388.md`** que decia que ninguna fusion se habia ejecutado.
5. **Mi propio caso positivo**: su prueba de redirecciones contaba deprecados y contradecia la
   politica de la operacion. **Se ajusto y se volvio MAS estricta**, exigiendo que los deprecados
   que quedan sean exactamente los declarados.
6. **El motivo de la fila 6 de la tabla de fusion**, que citaba *un paso 6* ajeno en una tabla de
   **dos fuentes**. **Se reescribio la prosa, no se aflojo el chequeo.**
7. **La vara 2 del verificador**, que comparaba cada tabla contra cada plan.
8. **Mi numeracion de las lecturas dirigidas**, atrapada por mi propio guard antes de escribirse.
9. **TROPIEZOS DE HERRAMIENTA, sin efecto en ninguna cifra pero declarados:** un heredoc de bash
   que murio por comillas (se rehizo con el escritor de ficheros), un `%d` sin argumento en la
   coletilla del barrido (arreglado), y **dos invocaciones fallidas del medidor de costuras** por
   no leer su firma antes de llamarlo.

---

## 11. PENDIENTES DE DOCTRINA

1. **NUEVO Y ES EL MAS CARO: `Gate 0` deshace parte de la redireccion de una fusion.** El
   absorbido conserva sus aristas y el reciprocado se las devuelve a los vivos. **Ninguna pagina
   dice si un nodo deprecado debe conservar su cableado**, y de eso depende que la redireccion de
   toda fusion futura sea estable. **Hoy no hace dano** (el alias resuelve) **pero envejece.**
2. **NUEVO: `scripts/costuras_internas.py` esta MAL CALIBRADO y lo dice.** Su senal de bloque
   devuelve 0,0 para todo. **Bloquea `OP-D-03` entero** y **deja sin la mitad de su apoyo al
   movimiento 2 de `OP-D-01`**. No lo arreglo yo.
3. **NUEVO: una guarda que se saltea importando por debajo.** `vuelta32_costura_opd01.py` importa
   las senales y **no la puerta de calibracion**. **Ninguna pagina dice que quien importe un
   instrumento tiene que importar tambien su baranda.**
4. **NUEVO: hasta donde atras alcanza el barrido del `9.10`.** Trece filas de checkpoints cerrados
   citan una cifra que hoy es otra, y ninguna pagina dice si se tocan.
5. **NUEVO: un acto con puente doble y cero triangulos cerrados.** `P.10` da la salida (fundir el
   subconjunto cerrado) **pero no dice que se hace con los puentes despues**: aqui quedaron dos
   nodos en la nomina que no entran en la fusion y no tienen operacion propia.
6. **CERRADO por la adjudicacion del fundador, y se dice para no repetirlo:** el carril de
   recomputo de las clases releidas **era el `9.10`**, y funciono dos veces.
7. **SIGUE VIVO:** los nodos propios de esta pasada **escritos sin acentos**, con cura escrita en
   `05_SANEO.md` linea 660 y sin numero de operacion.

---

## 12. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| # | que | por que es discutible |
|---:|---|---|
| **d1** | **Corregir `mapa_pasos` y `pruebas_repeticion`, que el encargo NO nombraba** | el encargo decia `grupos_pasos`. Toque dos campos mas. **Lo sostengo con que dejarlos habria puesto al verificador en verde encima de una contradiccion**, pero es alcance que me tome yo |
| **d2** | **Tachar la CABECERA de la tabla vieja** | es lo que hace que el verificador deje de leerla. **Un auditor puede decir que eso es adaptar el texto al instrumento** en vez de al reves |
| **d3** | **El 494 leido `C` y no `D`** | heredado de la vuelta 32 y ahora **escrito en el archivo**. Solo hay DOS ejemplares del `9.22` en 3.388 pares y este es el tercero |
| **d4** | **`LD-72` leido `D` y no `A`** | **el mas fuerte de la tanda**. Tres de cinco pasos compartidos es mucho, y **el puesto 788 llamo `A` a un par de la misma familia** con lo propio parecido. Lo separo porque alli eran dos lineas y aqui es un procedimiento con otro entregable |
| **d5** | **Declarar DOS nodos puente y no uno** | se sigue de las tres `D`, pero **las tres `D` son mias**. Si `LD-72` fuera `A`, el acto seria una familia y la fusion tendria que ser de cuatro |
| **d6** | **`voz_del_cliente_voc` como superviviente** | el contenido tiene un argumento en contra que no escondo: **`enfoque_mercado_voc` tiene el ALCANCE mas ancho** (*todo el proceso*), y `P.8` cuenta el alcance del rol como contenido. Lo vencen los otros tres apoyos, pero es una lectura contraria seria |
| **d7** | **Juntar la evaluacion preliminar de mercado y el analisis competitivo en UN paso** | son dos actos y los meti en uno **para caber en el estandar de 3 a 6**. La lectura contraria los separa y acepta siete pasos con la excepcion de clase |
| **d8** | **Llamar `SALVAGUARDA` a *los mas exigentes*** | encaja en la firma (protege un paso de decision) **pero tambien se puede leer como `ALCANCE`**, y el propio banco dice que la clase nacio de dos ejemplares |
| **d9** | **Que el `preservar` no cuente como perdida en la tabla de seis motivos** | escribi *NO ES PERDIDA* en dos filas. **La tabla de seis motivos es de perdidas**, y un auditor puede decir que entonces esas filas no van en esa tabla |
| **d10** | **Dejar el caso positivo CAYENDO tras `Gate 0`** | es lo contrario de lo que suele pedirse. **Lo sostengo con que arreglarlo daria un verde que dura hasta la proxima corrida**, pero deja la vuelta cerrada con una prueba en rojo publicada |
| **d11** | **No declarar `ARISTA QUE FALTA` en el 827 y si en el 724 y el 755** | apliqué tres criterios distintos a tres pares de la misma tanda. Lo sostengo con que alli el solape es **una linea contra una linea**, pero es el arreglo mas debil de las tres |
| **d12** | **Redirigir solo lo vivo** | lo tome del instrumento sellado de la casa, **no de una pagina de doctrina**. Un auditor puede decir que un deprecado que apunta a un id que ya no es nadie es una arista rota |
| **d13** | **PARAR en `OP-D-03` en vez de arreglar el instrumento de costuras** | el arreglo puede ser de una linea (`MIN_BLOQUE` o el rango). **No lo toco porque toca una cifra publicada de la vuelta 32** y la regla 5 manda traerlo. La lectura contraria es que un instrumento roto se arregla y punto |
| **d14** | **Aplicar a `OP-D-03` la doctrina de lecturas dirigidas que el fundador adjudico para `OP-D-02`** | **no lo hice**, y por eso hay siete pares sin leer. Lo sostengo con `P.5` (se lee **despues** del destejido), pero **es una decision mia sobre el alcance de una adjudicacion** |
| **d15** | **Tocar DOS guardas en el mismo dia** (el caso positivo y la vara 2 del verificador) | las dos las hice **mas estrictas** y las dos van declaradas, **pero es el patron exacto del que la vuelta 32 se marco a si misma en su `d15`** |

---

## 13. PREGUNTAS

1. **Un nodo deprecado, conserva su cableado o no?** De esto depende que la redireccion de toda
   fusion futura sea estable, y **hay una fusion ya ejecutada esperando la respuesta**.
2. **Quien arregla `costuras_internas.py`, y con que autoridad?** Su senal de bloque esta muerta,
   **bloquea `OP-D-03`** y **deja a medias el apoyo del movimiento 2 de `OP-D-01`**. El arreglo
   parece pequeno; el efecto sobre cifras ya publicadas, no.
3. **Los siete pares internos de `OP-D-03` se leen como dirigidas, igual que los tres de
   `OP-D-02`?** Si la respuesta es si, hay que decir **si antes o despues del destejido**, porque
   `P.5` dice despues y el destejido esta bloqueado por la pregunta 2.

---

## 14. LA RACHA DE DICTADO, dicha por mi

**El acta 32 conto una PARADA DE CREDITO por segunda tanda seguida con caida de cifra publicada
fuera del marcado.** Esta vuelta **midio la apertura antes de la primera operacion y la commiteo
antes de tocar nada** (`e1105299`); **midio el cierre al cerrar con el mismo instrumento**;
**escribio la cifra esperada del marcador ANTES de correr el instrumento, las dos veces, con orden
de parar si daba otra cosa**; **publico las dos corridas cada vez que dos instrumentos
discreparon**; y **dejo una prueba propia cayendo en vez de maquillarla**. **Cuatro de mis
correcciones de la seccion 10 las cazaron guardas que yo mismo escribi, y una me obligo a abortar
sin escribir.** **No me corresponde decir si la racha sigue cortada: eso lo mide el auditor.**
