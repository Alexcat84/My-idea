# REPORTE DE LA VUELTA 20 . Ejecutor: Opus 5 . 14 ago 2026

**FASE II, RECOMPUTO, VUELTA DE CIERRE DE REGISTROS. MODO DE CIERRE.** Cero reparaciones
de nodos, cero operaciones ejecutadas, cero pares nuevos leidos, FASE III sin abrir,
`pasada-unica` sin crear, Gate 0 sin correr, cribado sin tocar.

> **REGLA 1 DEL EJECUTOR, aplicada sin excepcion: toda cifra de este reporte se lee de la
> salida de un instrumento corrido EN ESTA VUELTA.** Las cifras de vueltas anteriores solo
> aparecen como contraste y con su corte al lado. **Donde mi medicion discrepa de una cifra
> publicada, la discrepancia se declara y la cifra vieja no se toca.**

> **EL CREDITO ESTABA RESTAURADO Y NO LO USE PARA AFLOJAR.** La tanda 19 salio limpia y el
> contador de tandas con caida esta en cero. Esta vuelta remidio las tres cifras de la cota
> con instrumento en vez de copiarlas de la nota, busco cada cosa en TODAS las sedes antes
> de decir que no existia, y **cazo dos guardas propias mal calibradas y un descuido mio de
> redaccion antes de publicar nada** (secciones 5 y 6).

> **LA CONCLUSION QUE MAS IMPORTA, dicha aqui arriba: la lista de cifras publicadas con dos
> lecturas NO queda vacia. Queda con UNA.** El encargo decia que tras los registros debia
> quedar vacia; midiendo, no queda. **Por eso NO declaro la FASE II lista para verificacion
> de cierre**, y traigo la que queda con sus dos sedes, sin arreglarla. Seccion 4.

---

## 0. LO PRIMERO: EL HASH, LAS RUTAS Y LO QUE NO SE TOCO

**Hash del TRABAJO: `1bfab1c4`.** Este reporte se commitea despues, **asi que el hash del
reporte es otro y no es el del trabajo.**

**Arbol al empezar: LIMPIO y sincronizado con `origin/bucle`** en `33d37f3c`, comprobado
antes de la primera edicion. **No habia nada pendiente que commitear.**

**Tres commits de trabajo, empujados por tramo a `bucle` segun se cerraba cada uno:**
`268d6225` (los instrumentos), `0342e6d5` (TAREA 1) y `1bfab1c4` (TAREA 2).

**LAS OCHO RUTAS del `git diff --stat 33d37f3c 1bfab1c4`, la lista COMPLETA:**

| ruta | que cambio |
|---|---|
| `docs/plan/01_FUENTES.md` | +106. La correccion declarada de la tanda de los cuatro libros, la nomina de los 14 de Horowitz y su forma verificada, la tercera sede, y dos hallazgos declarados y no arreglados |
| `docs/plan/INVENTARIO.jsonl` | 3 lineas de 671. El `racimo` del sales roadmap (`cobertura`, `estado`, `nota`), `EL PASO DE OFICIO` (`nota`) y `LA FIRMA POSICIONAL DEL INJERTO (P.2)` (`nota`, dos pasadas) |
| `docs/plan/LECTURAS_DIRIGIDAS.md` | +2. La linea aditiva de `LD-04` que apunta a su relectura |
| `docs/plan/RECOMPUTO_3388.md` | +92. La linea de rotulo en la tabla de la vuelta 19, y la seccion TAREA (vuelta 20) entera |
| `scripts/loop/vuelta20_medir.py` | NUEVO, solo lectura. El instrumento principal de la vuelta |
| `scripts/loop/vuelta20_horowitz.py` | NUEVO, solo lectura. La nomina de Horowitz y la medida posicional |
| `scripts/loop/vuelta20_tarea1.py` | NUEVO. Escribe las tres entradas del inventario, con guardas |
| `scripts/loop/vuelta20_tarea1b.py` | NUEVO. Escribe la tercera sede en la nota de `LA FIRMA POSICIONAL` |

**LO RESERVADO, comprobado con `git diff --stat 33d37f3c 1bfab1c4` acotado a esas rutas y
sale VACIO:** `dataset/` **intacto**, `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` **intacto en sus
3.388 lineas**, `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` **intacto en sus 335
componentes**, `docs/plan/OPERACIONES.jsonl` **intacto en sus 71 operaciones y cero
ejecutadas**. **Cero merges. `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se leyo para adjudicar
ningun par nuevo, ni de cola ni dirigido.**

**Cero guiones largos y cero guiones medios en las ocho rutas, contado por mi con
instrumento sobre el archivo entero antes de cada commit. El hook corrio verde en los tres.**

---

## 1. EL MARCADOR RECOMPUTADO, con instrumento propio de esta vuelta

**Fuente: `scripts/loop/vuelta20_medir.py` sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`,
corrido hoy. Corte: 14 ago 2026, cribado CERRADO en 3.388 de 3.388.**

| clase | pares | % |
|---|---:|---:|
| **A** | **583** | 17,2 |
| **B** | **89** | 2,6 |
| **C** | **7** | 0,2 |
| **D** | **2.709** | 80,0 |
| **n** | **3.388** | |

**Puestos 1 a 3.388, cero huecos y cero duplicados.**

**TASA POR DOMINIO, remedida hoy celda por celda:**

| dominio | pares | A | % |
|---|---:|---:|---:|
| `core` | 1.445 | 344 | 23,8 |
| `quality` | 844 | 126 | 14,9 |
| `health_safety` | 192 | 45 | 23,4 |
| `entrega` | 171 | 2 | 1,2 |
| `environmental` | 170 | 29 | 17,1 |
| `compras` | 155 | 1 | 0,6 |
| `franquicias` | 148 | 18 | 12,2 |
| `exportacion` | 130 | 15 | 11,5 |
| `risk_management` | 106 | **0** | 0,0 |
| `seguridad_digital` | 27 | 3 | 11,1 |

**VARA POR TRAMO: no hay.** El cribado esta cerrado y **esta vuelta no leyo ni un par**, ni
de cola ni dirigido, asi que no hay tramo que varar. **Lo digo en vez de omitirlo.**

**FIGURAS Y FAMILIAS AL DIA, medidas hoy:** figuras **20** (**20 de 20** por la cuenta de
forma y **13 de 20** por la de tanda, **las dos publicadas juntas** como manda la
adjudicacion 9 de la vuelta 18); `familia_de_ids` **53**; `racimo` **13**; `defecto` **19**;
`dominio` **10**; `acto` **556**. **Inventario: 671 entradas, y ninguna nace ni muere.**

---

## 2. TAREA 1: los cinco registros, y de que instrumento sale cada cifra

**Los cinco hechos, los cinco aditivos, el texto viejo conservado entero en los cinco.**

| # | registro | sede | de donde sale la cifra |
|---:|---|---|---|
| 1 | el puntero de `LD-04` a su relectura, y que **no se acuna numero nuevo** | `LECTURAS_DIRIGIDAS.md` | no lleva cifra. **Verificado hoy que `LD-71` NO existe en ninguna de las sedes de dirigidas** salvo como el numero que se decidio no acunar |
| 2 | el `racimo` del sales roadmap pasa a **15 de 15** y a **cobertura COMPLETA** | `INVENTARIO.jsonl` | `vuelta20_medir.py`: los 15 pares posibles son **10 en el archivo mas 5 en dirigidas**, y las cinco (`LD-66` a `LD-70`) **localizadas hoy en `LD_SALES_ROADMAP.md`** |
| 3 | la cota de `EL PASO DE OFICIO`, **regenerada** | `INVENTARIO.jsonl` | `vuelta20_medir.py`, **remedida hoy con las dos cadenas**: vigente **26 de 141 vivos, 7 en paso 1, 40 de 130**; contraste **6, 2 y 10** |
| 4 | Horowitz: la tanda son **44 nodos**, con la nomina de los 14 impresa | `01_FUENTES.md` y `INVENTARIO.jsonl` | `vuelta20_horowitz.py` sobre el grafo: **46 declaraciones, 2 solapes, 44 nodos distintos** |
| 5 | el rotulo del RECOMPUTO: el **9** son **EDICIONES** sobre **8** entradas | `RECOMPUTO_3388.md` | rotulo, no cifra |

> **LA CIFRA 3 NO SE COPIO DE NINGUN LADO.** El encargo pedia expresamente remedirla. Corri
> las dos cadenas hoy sobre los **141 nodos vivos** del dominio (de **158** en el grafo, **17
> con la clave `deprecado`**) y sobre los **130 pares leidos**, y **las dos reprodujeron
> exactas**: 26/7/40 la corregida y 6/2/10 la de la vuelta 18. **Coinciden con lo que el acta
> de la vuelta 19 verifico, y aun asi salen de mi corrida de hoy, no de su acta.**

---

## 3. HOROWITZ: EL CABO QUEDA SALDADO, Y EN DOS MITADES QUE NO DICEN LO MISMO

**Es la parte mas larga del encargo y la unica que era lectura de grafo entera. La hice
entera: los 14 impresos con sus pasos, uno por uno.**

**LA ARITMETICA, medida hoy:** 46 declaraciones en segunda o posterior posicion (Coleman 15,
**Horowitz 14**, Weinberg 13, Rackham 4), **DOS** solapes de nodos (`metas_vs_proposito` con
Horowitz y Coleman, `viral_loop_marketing` con Coleman y Weinberg), **44 nodos distintos**.
**El tercer solape que `01_FUENTES.md` nombraba, `decision_de_vender_startup`, es de
DECLARACIONES: declara a Horowitz dos veces con dos grafias, y un nodo que declara el mismo
libro dos veces sigue siendo un nodo y un libro.**

**EL SALDO DE LA FORMA, y va en dos mitades a proposito:**

| la pregunta | la respuesta medida |
|---|---|
| **por PRESENCIA del material** (que es lo que `01_FUENTES.md` afirma cuando dice *43 de 43 confirmados*) | **44 DE 44 CONFIRMADOS.** En los catorce el bloque del libro declarado en segunda posicion **esta presente y con la frontera visible**. Como los 43 ya estaban confirmados y el catorceavo era el unico que podia faltar, **sea cual sea el que la nomina de 13 dejaba fuera, esta verificado** |
| **por la FORMA ESTRICTA** (*como bloque apendice AL FINAL de los pasos*, que es la frase literal del doc) | **12 DE 14.** En **`metas_vs_proposito`** y **`principio_calidad_mvp`** el bloque de Horowitz **esta pegado y se ve, pero queda EN MEDIO**, porque cada uno declara un **TERCER** libro despues (Coleman y Hugos) y es ese tercer bloque el que cierra los pasos |

> **LOS DOS INSTRUMENTOS DAN EL MISMO CORTE, y eso es lo que me deja publicarlo.** Sin leer
> un solo paso, **la POSICION del libro en el campo `fuente`** ya separa a los mismos dos: un
> libro que no ocupa la ultima posicion declarada **no puede** tener el bloque final. Medido
> sobre los 44, las declaraciones fuera de la ultima posicion son **TRES**: esas dos, mas
> `viral_loop_marketing` con Coleman, **que ya estaba apartado por el propio doc**. **La
> lectura de pasos y la medida posicional coinciden nodo por nodo, sin que yo las ajustara.**

> **LA TERCERA SEDE, que casi me cuesta una busqueda negativa citada.** Ver seccion 6.
> `docs/plan/RECORTE_POSICIONAL.md`, **del MISMO 11 ago 2026** que el saldo que se corrige,
> ya publicaba el grupo de Horowitz con **14 candidatos Y SU NOMINA ESCRITA**. Cotejada hoy
> nodo por nodo, **es IDENTICA a la que midio mi instrumento**, y lo mismo las de Coleman
> (15) y Hugos (21) que ese doc nombra; sus agregados tambien reproducen exactos (**3.521**
> vivos, **67** con mas de un libro, **70** declaraciones en segunda o posterior).
> **Conclusion: el 13 de `01_FUENTES.md` ya estaba contradicho EL MISMO DIA por otro
> documento del plan, y hoy el 14 tiene TRES sedes contra UNA.**

---

## 4. LA LISTA DE CIFRAS CON DOS LECTURAS: NO QUEDA VACIA, QUEDA CON UNA

**El encargo decia que tras los registros debia quedar vacia. Barrida hoy con instrumento,
seis quedan cerradas y UNA queda viva.** Las siete estan en la seccion B de la TAREA (vuelta
20) de `RECOMPUTO_3388.md`, con sus sedes. **La viva es esta:**

| | |
|---|---|
| **la cifra** | los **pasos** de `decision_de_vender_startup` |
| **sede A** | `docs/plan/01_FUENTES.md`, tabla de *LOS TRES CASOS QUE NO SON UN SIMPLE APENDICE*: **25 pasos** |
| **sede B** | el **grafo** (medido hoy), `docs/FICHA_SUBFUSION_GRADIENTE.md`, `docs/COSTURAS_INTERNAS_RESUMEN.md` (fila 9 de sus veinte primeros) y la nota de `LA FIRMA POSICIONAL` en `INVENTARIO.jsonl`: **34 pasos** |
| **como aparecio** | la levanto la medicion de TAREA 1.4. **El encargo no la scopeaba** |
| **como se busco** | censadas **TODAS** las sedes `.md` y `.jsonl` de `docs/` con instrumento, no a ojo |
| **el contraste que la aisla** | los otros dos apartados de la MISMA tabla calzan exactos: `viral_loop_marketing` **30** y `coeficiente_viral` **16**. **El que diverge es uno solo** |
| **QUE HICE** | **la declare al lado de la vieja, sin tocar la vieja, y NO la arregle** |

> **POR QUE NO LA ARREGLE, y no es por cautela vaga.** El **25 no es una cifra suelta**: va
> cosido a un tramo escrito en la misma celda (*los pasos 11 a 15, 16 a 20 y 21 a 25 vuelven
> sobre el precio minimo y la disposicion del equipo*). Cambiar el 25 obliga a rehacer ese
> tramo entero, y **eso es reescribir un hallazgo, no anotar una correccion aditiva**. No hay
> regla vigente que mande esa reescritura sin saber **si el nodo crecio despues del 11 ago o
> si el conteo viejo era parcial**, y yo no puedo medir cual de las dos cosas paso: el grafo
> me da el estado de hoy, no su historia. **Lo traigo en vez de resolverlo.**

> **Y POR ESO EL VEREDICTO NO DICE LO QUE EL ENCARGO ANTICIPABA.** El encargo escribio: *si
> ningun bloque queda abierto **y** la lista de B esta vacia, la FASE II queda LISTA PARA
> VERIFICACION DE CIERRE*. **Los cinco bloques no dejan ninguno abierto. La lista no esta
> vacia.** La condicion pedia las dos cosas y solo se cumple una, asi que **no declaro la
> FASE II lista para verificacion de cierre**. Lo que si digo, medido: **la FASE II queda con
> sus cinco bloques cerrados y con UN cabo suelto nombrado**, y ese cabo es **una cifra de
> `01_FUENTES.md` sobre los pasos de un nodo, no un pendiente del cribado ni del recomputo**.

---

## 5. LA FASE II, BLOQUE POR BLOQUE, REMEDIDA HOY

| bloque | medido hoy |
|---|---|
| la cola de relectura post fusion | **7 de 7, y la cuenta cuadra con su propio campo `cobertura`**. La nota cita ocho puestos; quitado el **751**, que CAE por `LD-59`, quedan **siete**: seis en **B** (196, 224, 253, 591, 707, 968) y el **1096 en A**, con su excepcion escrita en `08_VERIFICACION.md`. El 751 esta hoy en **B** y **fuera** de la cola |
| el criterio del forastero | **los dos, igual**. `tacticas_cierre_ventas` con **6 lecturas, 1 A y 5 D**; `incentivos_no_monetarios_advocacy` con **0 pares** en el archivo, que es lo que su nota declara. El candidato condicionado sigue **registrado y sin contar** |
| el lote de cinco del sales roadmap | **CERRADO EN LAS DOS SEDES VIVAS** tras el registro 2 de esta vuelta |
| las lecturas de acto entero de P.5 | **556 actos** (221 superadas, **335 vigentes**), vigentes **281 CERRADOS y 54 ABIERTOS**, deuda **324** (**0 en cola, 324 fuera**) |
| los ejemplares de las veinte figuras | **20 de 20** de forma y **13 de 20** de tanda, **las dos juntas**. Las siete sin marca son las que nacieron nombradas |

**NINGUNO QUEDA ABIERTO.** El unico que se movio en esta vuelta (el del sales roadmap) se
movio **para cerrar la divergencia entre sus dos sedes vivas**, no para abrir nada.

---

## 6. ERRORES PROPIOS DE ESTA VUELTA, DECLARADOS CON NOMBRE Y CAZADOS ANTES DE PUBLICAR

**Tres. Ninguno llego a una cifra publicada, y los tres son de la misma especie que la
leccion que el bucle lleva tres vueltas repitiendo.**

1. **MI INSTRUMENTO DIO POR AUSENTES `LD-67`, `LD-68` y `LD-69`.** Mi primera guarda buscaba
   las cinco dirigidas **solo en `LECTURAS_DIRIGIDAS.md`**, y viven en `LD_SALES_ROADMAP.md`.
   **Es exactamente la trampa de la sede unica.** Corregi el instrumento para barrer **todas**
   las sedes `LD_*.md` antes de escribir una sola linea, y las cinco aparecieron.
2. **MI INSTRUMENTO METIA EL 751 DENTRO DE LA COLA.** Contaba los ocho puestos citados en la
   nota del `defecto` sin separar **el que CAE**. La cola son **siete**, y con la separacion
   hecha **cuadra con el campo `cobertura` de la propia entrada**, que dice 7. Corregido
   antes de publicar.
3. **Y EL PEOR, PORQUE YA ESTABA ESCRITO EN UN ARCHIVO:** en mi primera redaccion de
   `01_FUENTES.md` escribi que de los 13 de Horowitz *"del grupo solo habia conteos"*. **Era
   una busqueda negativa citada sin haber mirado todas las sedes**, y era **falsa**:
   `RECORTE_POSICIONAL.md` tiene la nomina de los 14 desde el 11 ago. Lo cace al censar las
   sedes para otra cosa. **Lo corregi declarandolo, no borrandolo**, en el propio
   `01_FUENTES.md` y con una segunda pasada sobre la nota de `LA FIRMA POSICIONAL`. **Lo que
   sigue sin estar escrito en ninguna parte es la nomina de los TRECE**, y por eso sigue sin
   poderse decir cual sobra.

> **Los tres los cace yo y los tres estan aqui. El tercero mejoro el resultado en vez de
> empeorarlo: la tercera sede es la confirmacion mas fuerte que tiene la correccion del 44.**

---

## 7. CORRECCIONES Y DISCREPANCIAS DECLARADAS, ninguna arreglada por mi mas alla del encargo

| # | lo que declaro | la cifra vieja | que hice |
|---:|---|---|---|
| 1 | la tanda de los cuatro libros son **44** nodos y Horowitz **14** | 43 y 13, en `01_FUENTES.md` | **correccion declarada, la vieja entera arriba**. Era el encargo |
| 2 | la cota vigente de `EL PASO DE OFICIO` es **26 / 7 / 40** | 6 / 2 / 10 | **regenerada con la vieja de contraste**. Era el encargo |
| 3 | `plan_mejora_procesos` **tambien** declara Horowitz dos veces con dos grafias | `01_FUENTES.md` nombraba solo a `decision_de_vender_startup` | **declarado, y `OP-S-11` NO se toca.** El texto viejo no afirmaba ser exhaustivo, asi que no lo corrijo: le anado el segundo ejemplar |
| 4 | la forma de apendice es **12 de 14** por la lectura estricta | *"siempre... como bloque apendice al final"* | **declarado con las dos mitades juntas**, y el 44 de 44 por presencia se sostiene igual |
| 5 | `decision_de_vender_startup` tiene **34** pasos | **25**, en `01_FUENTES.md` | **DECLARADO Y NO ARREGLADO.** Seccion 4 |

---

## 8. PENDIENTES DE DOCTRINA

**UNO, y no pare por el: registre la mejor lectura sostenida y segui, como manda la regla 4.**

> **NO HAY REGLA ESCRITA QUE DIGA SI UN BLOQUE PEGADO PERO NO FINAL CUENTA COMO *LA FORMA*.**
> `01_FUENTES.md` describe la firma posicional como *bloque apendice **al final** de los
> pasos*, y no dice que pasa cuando el nodo declara un tercer libro y el bloque del segundo
> queda en medio. **Lo sostenido que registre: publicar las DOS cuentas juntas** (44 de 44
> por presencia, 12 de 14 por forma estricta) **y nombrar los dos casos**, que es el mismo
> trato que el bucle ya le da a las dos cuentas de `SUBCONJUNTO ESTRICTO` y a las dos de las
> figuras. **No invente una categoria nueva y no toque el destino de destejido de esos dos
> nodos.** **PENDIENTE DE DOCTRINA.**

---

## 9. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Ocho, y los marco sin saber como salen.**

1. **NO DECLARAR LA FASE II LISTA PARA VERIFICACION DE CIERRE.** El encargo puso una
   condicion con dos partes y solo se cumple una, asi que no la declare. **Si la casa
   entiende que la fila 7 es de otro carril y no cuenta para esa lista, entonces me quede
   corto por literal** y la FASE II estaba lista. **Lo escribi sabiendolo, porque redondear
   hacia el cierre es exactamente lo que la doctrina prohibe.**
2. **HABER ESCRITO LA FILA 7 DENTRO DE `01_FUENTES.md`.** El encargo scopeaba esa sede a la
   correccion del 43 al 44. Yo sostengo que **declarar no es arreglar** y que la regla de
   declarar al lado de la vieja es obligatoria, no opcional. **Pero es escritura en una sede
   por un motivo que el encargo no listaba**, y puede leerse como scope excedido.
3. **EL CORTE 12 DE 14 ES MI LECTURA DE PASOS.** La medida posicional coincide nodo por nodo
   y por eso me atrevo a publicarlo, **pero la posicion del libro en el campo `fuente` es un
   PROXY, no una prueba de donde esta el bloque**. Si la casa lee los pasos y ve la frontera
   en otro sitio, el 12 se mueve. **El 44 de 44 por presencia no depende de esto.**
4. **DECIR 44 DE 44 CUANDO SOLO LEI 14.** Los otros 30 los da por confirmados el doc viejo,
   no mi lectura. **Mi argumento es que el unico que podia faltar era el catorceavo de
   Horowitz**, y por eso verificar los 14 basta. **Si la casa quiere los 44 leidos, esto es
   una confirmacion apoyada en una cifra ajena y lo estoy diciendo yo primero.**
5. **HABER CORREGIDO MI PROPIO TEXTO DE ESTA MISMA VUELTA CON UNA SEGUNDA PASADA** sobre la
   nota de `LA FIRMA POSICIONAL`, en vez de dejarlo mal y solo anotarlo en el reporte.
   Sostengo que dejar una frase falsa en `docs/plan/` porque ya la habia commiteado es peor.
   **Pero son dos ediciones sobre la misma entrada en una vuelta**, y la vuelta 19 se llevo
   un rotulo impreciso por menos que eso: **por eso el rotulo de esta va dicho entero, con
   los tres numeros** (3 entradas distintas, 4 pasadas, 6 campos).
6. **NO TOCAR `OP-S-11` al encontrarle un segundo ejemplar.** Puede que la casa esperara que
   la operacion recogiera el caso nuevo. **Lo deje declarado en la sede del hallazgo y no en
   la operacion, por scope.**
7. **HABER DADO POR ADJUDICADA LA FILA 2** (324 contra 329) apoyandome en el acta de la
   vuelta 19 en vez de re-discutirla. **Es la unica fila de la lista B cuyo estado no sale de
   una medicion mia de hoy sino de una adjudicacion previa**, aunque las dos cifras si las
   remedi. **Lo separo del resto a proposito.**
8. **LA COTA VIGENTE DE `EL PASO DE OFICIO`.** La remedi y reproduce, pero **no volvi a
   discutir si la cadena corregida es la correcta**: la di por adjudicada por el acta de la
   vuelta 19. Si esa adjudicacion se reabre, mi registro 3 se cae con ella.

---

## 10. LAS PREGUNTAS QUE TRAIGO, porque no las puedo medir

1. **La fila 7 (`decision_de_vender_startup`, 25 contra 34): quien la adjudica y quien
   reescribe el tramo.** Si manda el 34, hay que rehacer la celda entera de `01_FUENTES.md`
   (*los pasos 11 a 15, 16 a 20 y 21 a 25*), y eso ya no es aditivo. **No puedo medir si el
   nodo crecio despues del 11 ago o si el conteo viejo era parcial.**
2. **Los dos que no tienen la forma AL FINAL** (`metas_vs_proposito` y
   `principio_calidad_mvp`): **cambia eso su destino de destejido**, o el *44 de 44 por
   presencia* basta y siguen tratandose como los demas injertos.
3. **`RECORTE_POSICIONAL.md` queda como sede canonica de las nominas por libro?** Es la unica
   que las tiene escritas y hoy reprodujo exacta, pero su propio encabezado dice **NO
   ADJUDICA**. **Si lo es, `01_FUENTES.md` deberia apuntar a ella en vez de recontar.**
4. **`plan_mejora_procesos` entra formalmente a la evidencia de `OP-S-11`?** Lo deje
   declarado en `01_FUENTES.md` y no toque la operacion.

---

## 11. CONDICIONES DE PARADA: NINGUNA SE CUMPLE, Y UNA COSA SE TRAE SIN PARAR

- **Doctrina nueva: no.** El unico pendiente esta en la seccion 8, registrado con la mejor
  lectura sostenida, sin inventar categoria y sin parar, como manda la regla 4.
- **Contradiccion sin resolver: NO, pero hay UNA DECLARADA Y NO ARREGLADA**, la fila 7. **No
  contradice una regla vigente ni una cifra publicada con su corte por culpa de esta vuelta:
  es una divergencia vieja que esta vuelta descubrio, y por eso se declara y se trae en vez
  de pararlo todo.**
- **Decision de fundador: nada reservado se toco.** `dataset/` intacto, veredictos intacto,
  componentes intacto, operaciones intacto, cero merges, cero operaciones ejecutadas.
- **Fallo tecnico: no.** Arbol limpio, hook verde en los tres commits, cero guiones largos y
  cero guiones medios en las ocho rutas.
- **Credito de tanda: intacto.** No conozco ninguna caida mia en esta tanda; los tres errores
  propios de la seccion 6 los cace yo antes de publicar y estan escritos.
- **Campana consumada: no.** **La FASE II queda con sus cinco bloques cerrados y un cabo
  nombrado. El cierre y la apertura de la FASE III son del auditor en la vuelta 21. Esta
  vuelta NO abrio la FASE III, NO creo `pasada-unica` y NO corrio el Gate 0.**
