# CORRECCIONES A APLICAR FUERA DE `docs/plan/`

**Esta pagina existe por una frontera de sesion.** La instruccion dice **escribir
solo en `docs/plan/`**, y ademas manda corregir cifras que viven **en la ficha y
en el banco**. Las dos cosas no caben a la vez.

> **Lo que hago: dejo la correccion ESCRITA, exacta y lista para pegar, con su
> ubicacion. Lo que no hago: cruzar la frontera y tocar ficheros que la otra
> sesion puede estar escribiendo.** Un fichero pisado en paralelo es caro de
> deshacer; una correccion escrita y no aplicada, no.

> **ADJUDICADO el 11 ago 2026: LAS CUATRO CORRECCIONES LAS APLICA LA SESION A**,
> que es la duena de esos ficheros, **cuando reporte su tanda.** Esta pagina es su
> encargo, escrito y verificado. **Desde aqui no se cruza la frontera.**

---

## CONFIRMACION 0: LAS 27 AUTO-ARISTAS SE CONFIRMAN, NO SE CORRIGEN

**Va primero y NO es una correccion: es lo contrario.** La cifra publicada de **27
esta bien** y **no hay que tocarla**.

**Que paso.** Informe *auto-aristas medidas hoy, CERO*. **Mi medicion estaba mal**:
mi resolutor era *el id, si esta en el grafo; y si no, su duena*, y **las 27
apuntan a ids que SI estan en el grafo, como DEPRECADOS**, asi que los devolvia sin
resolver.

**Remedido con la semantica de `resolverId`, y el auditor lo remidio aparte con el
mismo instrumento: coinciden.**

| | publicado | **remedido y confirmado** |
|---|---:|---:|
| nodos vivos con **auto-arista** | **27** | **27** |
| enlaces implicados | | **33** |
| **directos** | | **0** |
| **via alias propio** | | **33** |

> **QUIEN APLIQUE ESTA PAGINA TIENE QUE SABER DOS COSAS:**
>
> **1. La fila de las 27 en `PENDIENTES.md` se queda como esta.** Ni se corrige ni
> se anota como dudosa.
>
> **2. El motivo del banco 9.14 QUEDA CONFIRMADO.** Esa regla, *todo conteo de
> grado excluye el propio nodo*, se adopto **usando las 27 como motivo**. El motivo
> se sostiene entero: **la regla no solo sigue en pie, ahora tiene su cifra
> verificada dos veces.**

**Lo unico que si encogio es el self-alias**, y va como correccion 1.

**CONSECUENCIA EN EL PLAN**: `OP-S-07` **vuelve como operacion LISTA**, con los 27
ids, el arreglo y **la guarda que Gate 0 necesita**, que no es la que parece. Ver
[`05_SANEO.md`](05_SANEO.md).

---

## CORRECCION 1: el self-alias, de SIETE a CERO

**UBICACION**: `docs/AUDITORIA_MOTOR.md`, seccion **B.3**.

**TEXTO PUBLICADO:**

> *Además, 7 nodos se listan a sí mismos como su propio alias (`trilogia_de_juran`,
> `recomendaciones_smart`, …): ruido inofensivo, pero ruido.*

**CORRECCION A PEGAR DEBAJO, sin borrar el original:**

> **CORREGIDO el 11 ago 2026, medido sobre las tres copias del dataset: hoy son
> CERO.** Ningun nodo vivo ni deprecado se lista a si mismo en `ids_alias`.
> `trilogia_de_juran`, el ejemplar citado, lleva hoy tres alias y **ninguno es el
> suyo**. La guarda del codigo sigue en pie y hace bien: `mapaDeAlias` en
> `web/lib/engine/graph.ts` filtra `if (a !== nid)` con el comentario *el
> auto-alias (7 nodos) no dice nada*. **La guarda se queda; la cifra que la
> motivaba ya no.**

---

## CORRECCION 2: Incoterms, de DOCE a TRES

**UBICACION**: `docs/PENDIENTES.md`, seccion *ADJUDICADO PARA EL PLAN (11 ago
2026)*, tabla **LA EVIDENCIA REAL**, fila de Incoterms.

**FILA PUBLICADA**: `| citan **Incoterms** sin ninguna version | **12** |`

**FILA CORREGIDA:**

```
| citan **Incoterms** sin ninguna version, EN SU TEXTO | **3** |
```

**Y LA NOTA QUE LA ACOMPANA, para que la correccion se entienda y no se repita:**

> **CORREGIDO el 11 ago 2026.** La cifra de 12 sumaba **los 3 que lo CITAN en su
> texto mas 9 que solo lo llevan en una arista o en el id**. Es **el mismo error
> que esta misma adjudicacion habia corregido tres parrafos mas arriba para
> NAFTA**: *apuntar al nodo no es citar el tratado, y mezclarlos infla la cifra.*
> **Se corrigio la fila de NAFTA y no la de al lado.**
>
> **Los TRES son de `exportacion` y los tres sin version**:
> `incoterms_reglas_comerciales_internacionales`, `terminos_de_venta_incoterms` y
> `seguro_de_carga_transporte`. **Los dos primeros lo llevan tambien en el id.**
>
> **LA DECISION DE FONDO NO SE MUEVE.** La **UNION** de las tres averias baja de
> **21** a **12 nodos**, con **solape cero** entre ellas, y **los 12 de 12 siguen
> siendo de `exportacion`**, que era el argumento. **El argumento sobrevive
> entero: solo cambia el tamano.**

**Y la fila de la UNION en la misma tabla:**

```
| **UNION de las tres** | **12** |
```

---

## CORRECCION 3: la promesa del resolutor SI se cumplio

**UBICACION**: `docs/AUDITORIA_MOTOR.md`, seccion **B.3**, titulo y primer
parrafo.

**TEXTO PUBLICADO**: *`ids_alias`: una promesa que nadie cumple* ... *ningún
código lo lee. Busqué `ids_alias` en todo `web/lib`, `web/app`, `scripts/` y
`engine/`: solo aparece en la declaración del tipo y en el consolidador que lo
escribe. **No existe resolutor.***

**CORRECCION A PEGAR DEBAJO:**

> **CUMPLIDA, y verificada contra el codigo el 11 ago 2026.** El resolutor
> **existe**: `web/lib/engine/graph.ts` construye el mapa en `mapaDeAlias` (linea
> 107) y exporta **`resolverId`** (linea 131), que **camina cadenas de alias**
> hasta un nodo activo y, si la cadena entera fue retirada, devuelve el eslabon
> mas reciente que exista. **Lo invocan `etiquetaArbol` (164) y `tituloDeNodo`
> (172)**, hay un espejo en Python en `scripts/reanclar_por_resolutor.py`, y lo
> ejercitan `resolutorHistoria.test.ts` y `compass.test.ts`.
>
> **Lo que queda no es construirlo: es medir por donde pasa.** Medido el mismo
> dia: en produccion (`web/lib` y `web/app`, sin tests) hay **42 accesos directos
> al grafo por id, en 12 ficheros, y 9 de esos ficheros manejan ids de origen
> externo.** Esa es la lista que hay que revisar, y es `OP-S-08` del plan.

**Y la tabla de alias, medida el mismo dia**, por si la auditoria quiere fijarla:

| | |
|---|---:|
| alias totales | **391** |
| a nodo **deprecado**, que es su funcion | **314** |
| **colisiones vivas** (alias que apunta a un nodo vivo) | **0** |
| **huerfanos** a ids inexistentes | **77** |

> **Los 77 se limpian en el saneo sin riesgo**: con **cero colisiones vivas**, su
> borrado no puede romper una resolucion buena.

---

## CORRECCION 4: la cuenta de los 18 nodos de fuente

**UBICACION**: `docs/COSTURAS_INTERNAS_RESUMEN.md`, seccion 6 y seccion 7, punto 1.

**TEXTO PUBLICADO**: *Tres decisiones de fuente que cubren dieciocho nodos.*

**CORRECCION A PEGAR AL LADO:**

> **RECOMPUTADA con su corte, 11 ago 2026, tras la adjudicacion de que MANDA LA
> CLASE y no la cuenta.** La cuenta de 18 tomaba **cuatro** miembros de la clase
> LARGO LEGITIMO, los del *Basic Guide*, y dejaba fuera **tres** que estan en la
> misma clase: dos de *Juran's Quality Handbook* y uno de `core`. **Con la clase
> entera, el alcance de las tres decisiones de fuente es de 7 mas 3 mas 21 = 31
> nodos**, no 18.
>
> **El salto grande no es ese**: la nomina de Hugos, publicada como **11 de las 46
> confirmadas**, se midio el mismo dia en **21 nodos vivos que declaran Hugos
> junto a otra fuente**. **Los dos numeros conviven** porque cuentan cosas
> distintas: 11 son costuras confirmadas con pegado de Hugos; 21 son todos los
> nodos con la firma del injerto. **La cifra que el plan usa es la de 21, por
> adjudicacion.**

---

## CORRECCION 5: EL CAVEAT DEL PREDICTOR

**UBICACION**: el **informe de cierre de costuras**,
`docs/COSTURAS_INTERNAS_RESUMEN.md`, seccion 2, *LA HERENCIA PRINCIPAL: EL
PREDICTOR DE FUENTES*.

**TEXTO PUBLICADO**: la tabla del predictor, **91% de aciertos en nodos de DOS o
mas libros contra 4% en los de UNO**.

**CAVEAT A PEGAR JUNTO A LA TABLA:**

> **CAVEAT, 11 ago 2026: CON EL CAMPO `fuente` SUCIO, ESTA CIFRA SOLO SIRVE PARA
> ORDENAR UNA COLA.**
>
> **El predictor separa por una propiedad del campo `fuente`: cuantos libros
> declara el nodo.** Y ese campo **no esta normalizado**: medido el mismo dia,
> **129 grafias distintas para 55 libros canonicos**. Hugos aparece con **dos**
> grafias y Horowitz con **tres**, varias truncadas a unos treinta caracteres.
>
> **LA CONSECUENCIA ES DIRECTA SOBRE EL PREDICTOR, no sobre el censo: un libro con
> dos grafias puede convertir un nodo de UN libro en uno de DOS**, que es
> exactamente la frontera por la que el predictor separa. **Un nodo que declare el
> mismo libro dos veces cae del lado del 91% sin serlo**, y hay al menos uno
> medido: `decision_de_vender_startup` lleva *The Hard Thing About Hard Thing* y
> *The Hard Thing About Hard Things* **en la misma linea**.
>
> **SU PRERREQUISITO TIENE NOMBRE: `OP-S-11`** del plan de la pasada unica, el
> campo `fuente` canonico. **Hasta que esa operacion corra, el 91 contra 4 ordena
> una cola y no prueba nada.**
>
> **Y esto NO contradice al informe: lo confirma.** El propio informe ya declaro la
> deuda en su ultima linea, *auditar el campo `fuente` antes de fiarse del
> predictor para nada que no sea ordenar una cola*. **Esta correccion solo pone la
> cifra de la averia al lado de la deuda, y le da dueno.**

---

## RESUMEN, para decidir de un vistazo

| # | que pasa | donde | quien lo aplica |
|---:|---|---|---|
| **0** | **NO se corrige nada: las 27 se CONFIRMAN**, y con ellas el motivo del banco 9.14 | ninguna | nadie: **solo hay que saberlo** |
| 1 | self-alias, de 7 a **0** | `AUDITORIA_MOTOR.md` B.3 | **SESION A** |
| 2 | Incoterms, de 12 a **3**; union de 21 a **12** | `PENDIENTES.md`, adjudicacion del barrido | **SESION A** |
| 3 | la promesa del resolutor **si** se cumplio | `AUDITORIA_MOTOR.md` B.3 | **SESION A** |
| 4 | la cuenta de 18, recomputada con su corte | `COSTURAS_INTERNAS_RESUMEN.md` 6 y 7 | **SESION A** |
| **5** | **el CAVEAT DEL PREDICTOR**: con el campo sucio, el 91 contra 4 solo ordena una cola | `COSTURAS_INTERNAS_RESUMEN.md` 2 | **SESION A** |

> **Las cuatro son de la SESION A y se aplican cuando reporte su tanda.** Ninguna
> se toca desde aqui.

> **Y NINGUNA TOCA EL BANCO 9.14.** Esa regla usaba las 27 como motivo, y **el
> motivo queda confirmado en vez de corregido.**

---

## CORRECCION 6. **EL PURO DE LA COMPETENCIA ENTRE INVERSORES DEGRADA A SUB-PURO**

**Va al banco de la SESION A, donde vive la tabla de racimos.** *(La tabla viva del
plan ya esta recomputada en `INVENTARIO.jsonl` y en `10_INVENTARIO.md`.)*

**LO PUBLICADO:** *la competencia entre inversores*, **PURO, cuatro miembros, seis
pares, todos en A**, declarado al puesto **1030**.

**LO MEDIDO al puesto 2.117** (`scripts/plan/puro_inversores.py`, contador por el
nombre mas barrido de las A):

| | publicado | **medido hoy** |
|---|---:|---:|
| miembros | 4 | **5** |
| pares posibles | 6 | **10** |
| pares leidos | 6 | **7** |
| de ellos en A | 6 | **7** |
| **forma** | **PURO** | **SUB-PURO** |
| cobertura | 6 de 6 | **7 de 10** |

**EL QUINTO MIEMBRO ES `tecnica_anclaje_negociacion`**, y entro por la **A del
puesto 878** contra `construccion_de_leverage`.

### LA RECONCILIACION, y sin ella la degradacion no cierra

**ESE NODO YA SE HABIA MIRADO Y YA SE HABIA DEJADO FUERA, CON MOTIVO ESCRITO.** No
es un descubrimiento: **es una decision que se toma dos veces con veinte meses de
archivo en medio.** Las dos quedan.

**DECISION 1, puesto 878** *(`INTRA_DOMINIO_VEREDICTOS.jsonl`, y glosada en
`INTRA_DOMINIO_INFORME.md` seccion 36.6 punto 2)*. Es el **PRIMER USO del barrido
de las A** del banco 9.15. El veredicto dice, literal:

> *este nodo aparece ahora con un A vigente contra un miembro del sub-puro de la
> competencia entre inversores, o sea que entra como candidato a miembro; **la
> lectura lo deja FUERA, porque su objeto es como negociar terminos y no como
> generar competencia entre inversores.** El candidato se levanta por el archivo y
> se resuelve leyendo, que es exactamente para lo que se escribio la regla.*

**LA EXCLUSION NO SE BORRA. Fue correcta para lo que decidia**, y ademas explica
por que el racimo se declaro con cuatro y no con cinco: **la declaracion de PURO
del puesto 1030 fue COHERENTE con ella**, no la ignoro.

**QUE APARECIO DESPUES DE AQUELLA EXCLUSION.** Solo dos lecturas tocan este asunto
despues del puesto 878, y hay que decirlas las dos:

| puesto | par | clase | que aporta |
|---:|---|---|---|
| **1030** | `gestion_multiples_term_sheets` contra `leverage_en_negociacion_con_vcs` | **A** | cierra los 6 pares de los CUATRO viejos. **Es el puesto donde se declara el PURO** |
| **1295** | `orden_negociacion_puntos` contra `tecnica_anclaje_negociacion` | **D** | y **lleva dentro la frase que decide**, ver abajo |

> **NINGUN PAR NUEVO DEL QUINTO MIEMBRO SALIO A DESPUES DE LA EXCLUSION. Hay que
> decirlo asi de claro:** su unica A sigue siendo la del 878. **Lo que cambio no es
> la cantidad de evidencia, es lo que el propio archivo dice de ella.**

**LA FRASE DEL PUESTO 1295, que es posterior a la exclusion Y posterior a la
declaracion de PURO:**

> *NOTA DEL BARRIDO: `tecnica_anclaje_negociacion` tiene **una A vigente**, el
> puesto 878 contra `construccion_de_leverage`. **Es gemelo de aquel** y no de este.*

### POR QUE MANDA LA ADMISION DE HOY

**No manda por ser mas nueva a secas. Manda por tres cosas que se suman:**

1. **La medicion mas reciente del propio archivo lo llama GEMELO**, en el puesto
   1295, con la A del 878 declarada **vigente** y no revocada.
2. **Las dos decisiones no hablan del mismo objeto, y por eso las dos pueden ser
   correctas.** La exclusion del 878 decide **el TEMA del racimo**: *generar
   competencia entre inversores* no es *como anclar terminos*. La admision de hoy
   decide **el ACTO**, que por el banco 9.24 **es el cierre transitivo de la relacion
   gemelo** y no admite gusto: **si hay A, el nodo esta dentro.**
3. **Y la forma publicada se calculo sobre el ACTO, no sobre el tema.** *PURO,
   cuatro miembros, seis pares* es una cuenta de componente conexa. **Por el banco
   9.17 manda la MEDICION**, y la medicion de la componente da cinco.

> **LO QUE DE VERDAD PASO, dicho sin adornos: se declaro una forma de ACTO sobre una
> nomina de TEMA.** Mientras el quinto no tuvo A, las dos coincidian. **Desde el
> puesto 878 dejaron de coincidir, y la etiqueta se quedo con la cuenta vieja.**

### LA CONSECUENCIA, Y ES QUE LA DEGRADACION SE PUEDE DESHACER EN LOS DOS SENTIDOS

**Los tres pares que faltan son los tres del quinto miembro, y los tres estan fuera
de cola.** Segun como salgan:

| si los tres salen | entonces | y quien gana |
|---|---|---|
| **A** | vuelve a **PURO con cinco miembros y diez pares** | la admision de hoy, del todo |
| **D** | el quinto **sale del acto**, la componente se parte y vuelve a **PURO con cuatro** | **la exclusion del 878, del todo** |
| mezclados | queda **MEZCLADO**, y el racimo deja de ser puro por cualquier via | ninguna: se lee y se escribe |

> **Por eso las dos decisiones se quedan en el registro con su fecha, y ninguna se
> tacha.** Hoy la degradacion cierra como **SUB-PURO 7 de 10**, y **el desempate
> esta nombrado, contado y fuera de cola.** **Tres lecturas lo resuelven.**

> **LA DEGRADACION NO DESMIENTE NINGUNA LECTURA.** Los siete pares leidos siguen
> siendo siete A. **Lo que dice es otra cosa: la forma se declaro sobre una nomina
> que todavia iba a crecer**, y crecio por una A posterior a la declaracion.

**LOS TRES FALTANTES, nombrados, y los tres FUERA DE COLA:**
`tecnica_anclaje_negociacion` contra `estrategia_competencia_vcs`, contra
`gestion_multiples_term_sheets` y contra `leverage_en_negociacion_con_vcs`.

> **Si los tres salen A, vuelve a PURO con cinco miembros y diez pares.** Hasta
> entonces es **SUB-PURO con cobertura 7 de 10**, y por el banco 9.26 **la forma va
> con la cobertura al lado o no va.**

**TEXTO PARA PEGAR EN LA FILA DE LA TABLA:**

> **la competencia entre inversores** | **SUB-PURO** | **7 de 10** al puesto 2.117 |
> degradado el 11 ago 2026: la componente crecio a **cinco miembros** por la A del
> puesto 878. Los tres faltantes son del quinto miembro y **estan fuera de cola**.

**Y LA LECCION, que es mas grande que este racimo:** *el efectivo contra la
ganancia* y *el compromiso contado tres veces* siguen declarados PUROS con
**cobertura completa**, asi que no corren este riesgo. **El riesgo lo corre toda
forma declarada sobre una componente que aun recibe A.** Es el mismo banco 9.26
dicho al reves: **una forma sin cobertura completa no es un resultado, es un
estado.**

---

## CORRECCION 7. **MUERE *CERO PODAS EN VEINTICUATRO LECTURAS***

**Va al banco de la SESION A y a la ficha del barrido paso contra nodo.**

**LO PUBLICADO:** sobre **624** candidatos sin arista, muestra pineada de 24, **19
jerarquias sanas, CERO podas, 5 falsos positivos**, proyeccion de **489** aristas
con banda de 376 a 586. **Y la glosa:** *la bolsa no es una mezcla de dos clases de
arreglo, es UNA y es la barata.*

**LO MEDIDO el 11 ago 2026**, sobre la bolsa calibrada y con **46 lecturas pineadas
en dos muestras disjuntas** (`docs/plan/PIN_SORTEO_CALIBRADO.txt`):

| | publicado | **medido** |
|---|---:|---:|
| candidatos sin arista | 624 | **477** |
| lecturas | 24 | **46** |
| jerarquia sana | 19 | **32, 69,6%** |
| **madre que repite** | **0** | **7, 15,2%** |
| falso positivo | 5 | 7, 15,2% |
| proyeccion de aristas | 489, banda 376 a 586 | **332, banda 263 a 386** |
| **pares gemelos proyectados** | **no se contemplaban** | **73, banda 36 a 135** |

**LA GLOSA SE RETIRA ENTERA. La bolsa SI es una mezcla de dos clases.**

**Y LA MEDIDA EXACTA DE LA DISCREPANCIA, porque no todo se explica con el tamano:**
el techo al 95% de un **0 de 24** es **11,7%**; lo medido es **15,2%**. **No son
compatibles del todo, pero por poco.** Quedan dos explicaciones abiertas y **desde
la sesion B no se puede elegir entre ellas**: o mala suerte de la muestra vieja, o
**la clase madre que repite no se aplico igual al leerla**. Se escribe como pregunta
abierta.

**LO QUE SI QUEDA CERRADO Y ES REGLA:**

> **UN CERO SOBRE 24 LECTURAS NO ES UN CERO, ES UN TECHO.** Se escribe *no vi
> ninguno en 24, techo 11,7%*, **nunca** *no hay*. Es el banco 9.21 aplicado a la
> clase vacia: **la cifra lleva su corte, y el cero lleva su banda.**
