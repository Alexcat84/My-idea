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

---

## CORRECCION 8. **UN VOLTEO PROPUESTO: EL PUESTO 2.078**

**Sale del control de la muestra pineada de las D**, 12 ago 2026. **Es el UNICO de
veinticuatro que cae**, y **se propone, no se aplica: la sesion A decide.**

**EL PAR:** `elaboracion_fdd` contra `preparar_fdd`, franquicias, **clase actual D**.

**LO QUE DICE LA RAZON VIEJA:** *cada uno trae DOS pasos que el otro no tiene. Por eso
CONTINUA en los dos sentidos, banco 9.22.*

**LO QUE DICE LA LECTURA A CIEGAS DE HOY, con la vara y no con el conteo:**

| nodo | lo propio | que es |
|---|---|---|
| `elaboracion_fdd` | asegurar que **todas las cuotas esten divulgadas**; **documentar la entrega** con la pagina de recibo | **DOS LINEAS**: un criterio y una accion unica |
| `preparar_fdd` | incluir el contrato y los documentos accesorios; **preparar o crear una entidad corporativa nueva con estados financieros auditados** | una linea **y un PROCEDIMIENTO** |

> **Por la vara del banco 9.6.1, lo que `elaboracion_fdd` anade CABE EN LINEAS.** Y por
> **`P.11` del banco del plan**, *una advertencia es linea, no procedimiento*, con su
> pregunta de aplicacion: **quitale al nodo lo que es puntero, criterio suelto o accion
> unica, y mira si lo que queda es un procedimiento.** **No queda ninguno.**

**LA PROPUESTA, y va con su superviviente ya medido:**

| | |
|---|---|
| **clase propuesta** | **A**, y si la sesion A prefiere ser conservadora, **B** |
| **superviviente** | **`preparar_fdd`**, porque es el unico que trae un procedimiento propio |
| **perdidas que viajan** | las dos lineas de `elaboracion_fdd`: **la divulgacion completa de cuotas y fuentes de ingreso**, y **documentar la entrega con la pagina de recibo**, que es **lo unico del par que sirve para probar el cumplimiento despues** |
| **los ids** | `elaboracion_fdd` y `preparar_fdd` son **la misma cosa en dos verbos**: van a la **DECISION 4** |

> **Y LA HONESTIDAD DEL CASO, que hay que decir para que la sesion A pese bien: ESTO NO
> ES UN ERROR DEL CRIBADO. Es deriva de doctrina.** La razon vieja **cuenta pasos** y la
> vara **los pesa**, y la precision que lo hace explicito, `P.11`, **se escribio
> veinticuatro dias despues del veredicto.**

**LO QUE NO SE HIZO:** no se toco el veredicto. **El archivo sigue diciendo D.**

## CORRECCION 9. **LA FICHA DE `OP-M-02-ACCLIMATE` CONTRA SU PROPIA EJECUCION: DOS CIFRAS SELLADAS EL 12 AGO 2026 QUE LA PASADA DEL 2 SEP 2026 DESMIENTE**

**POR ADICION, Y NO SE TOCA LA FICHA.** Escrita en la vuelta 139, TAREA 1.b, por
encargo del acta de la vuelta 138 (adjudicacion **3.4**, discutibles 3 y 4). Lo
que la regla manda aqui es `P.9` y `P.13` con su frase comun, *"lo escrito el dia
de la decision hay que releerlo el dia de la ejecucion"*, y `EJECUTOR.md` regla 2:
**la discrepancia se declara, no se resuelve copiando**. El veredicto viejo se
queda donde esta, con su fecha de corte, y esta pagina dice al lado lo que se
midio el dia de fundir.

**QUIEN ES.** `OP-M-02-ACCLIMATE`, fusion de mesa de la serie Coleman, fase 5
Acclimate. Superviviente `fase_acclimate_experiencia_cliente`, absorbido
`fase_acclimate_mapa_de_proceso`. **FUNDIDA EN LA VUELTA 138**, la primera mesa de
la fase 06.

### 9.a. LAS DUPLICADAS: la ficha dice CERO, la pasada fabrico DOS

**LO QUE DICE LA FICHA SELLADA (`docs/plan/OPERACIONES.jsonl`, entrada
`OP-M-02-ACCLIMATE`, `fecha_corte` **2026-08-12**), y va copiado VERBATIM:**

> `verificacion`, **SEXTA** linea (indice contado con codigo sobre el JSON, no a
> ojo): *"la simulacion fabrica 0 duplicadas: se dejan para OP-S-12"*
>
> `nota`, ultima frase: *"Es ademas la unica de las cinco que NO fabrica ninguna
> duplicada."*

**LO QUE MIDIO LA SIMULACION DEL DIA DE LA EJECUCION.** `scripts/plan/simular_fusion.py`
corrida el **2 sep 2026**, salida sellada en
`docs/loop/SALIDA_V138_3_SIM_OPM02ACCLIMATE.txt`, bloque **4**, copiado VERBATIM:

> ```
> ### 4. DUPLICADAS QUE LA FUSION FABRICA (clase OP-S-12)
>     Solo las NUEVAS: se cuentan las duplicadas antes y despues, y se resta.
>      gamificacion_onboarding_visual               nodos_previos     -> fase_acclimate_experiencia_cliente
>      ocho_fases_experiencia_cliente               nodos_siguientes  -> fase_acclimate_experiencia_cliente
>      TOTAL NUEVAS: 2
> ```

| | cifra | corte | fuente |
|---|---|---|---|
| duplicadas nuevas, segun la ficha | **0** | 12 ago 2026 | `OPERACIONES.jsonl`, `verificacion` linea 6 y `nota` |
| duplicadas nuevas, segun la simulacion del dia de fundir | **2** | 2 sep 2026 | `SALIDA_V138_3_SIM_OPM02ACCLIMATE.txt`, bloque 4 |

**LAS DOS, CON NOMBRE:** `gamificacion_onboarding_visual` en `nodos_previos` y
`ocho_fases_experiencia_cliente` en `nodos_siguientes`, las dos apuntando a
`fase_acclimate_experiencia_cliente`.

### 9.b. EL CABLEADO: la ficha dice 10 contra 3, la pasada midio 11 contra 4

**LO QUE DICE LA FICHA SELLADA**, en dos sitios y con las mismas cifras, VERBATIM:

> `evidencia`, tercera linea: *"MEDIDO: 10 contra 3 en cableado"*
>
> `adjudicacion`: *"Sobrevive fase_acclimate_experiencia_cliente por DESEMPATE POR
> CABLEADO, 10 contra 3."*

**LO QUE MIDIO LA SIMULACION DEL DIA DE LA EJECUCION**, mismo fichero sellado,
bloque **1**, copiado VERBATIM:

> ```
>   1. DESEMPATE POR CABLEADO
>      fase_acclimate_experiencia_cliente           pasos  5 | nombra 11 | LO NOMBRAN 11
>      fase_acclimate_mapa_de_proceso               pasos  8 | nombra  4 | LO NOMBRAN  4
>      >>> gana fase_acclimate_experiencia_cliente por 11 contra 4
> ```

| | cifra | corte | fuente |
|---|---|---|---|
| cableado, segun la ficha | **10 contra 3** | 12 ago 2026 | `OPERACIONES.jsonl`, `evidencia` linea 3 y `adjudicacion` |
| cableado, segun la simulacion del dia de fundir | **11 contra 4** | 2 sep 2026 | `SALIDA_V138_3_SIM_OPM02ACCLIMATE.txt`, bloque 1 |

### 9.c. QUE SE HACE, Y QUE NO

**LO QUE NO SE HACE, y se dice con todas sus letras:**

- **NO se toca el veredicto ni la ficha.** `OPERACIONES.jsonl` sigue diciendo
  `0 duplicadas` y `10 contra 3` con su `fecha_corte` de 2026-08-12. Una correccion
  que tapa lo que corrige no se puede auditar (`EJECUTOR.md` regla 8).
- **NO se promedia ni se elige una de las dos cifras.** Las dos son ciertas con su
  corte: la ficha midio un grafo de hace veintiun dias, la simulacion midio el de
  hoy, y entre medias esta campaña movio aristas.
- **NO es parada.** Adjudicado por el auditor en el acta 138, 3.4: *"no es
  contradiccion irresoluble: es el caso que `P.9` y `P.13` cubren"*.

**LO QUE SI CAMBIA, y ya estaba escrito en la propia ficha:** las dos duplicadas
nuevas **quedan enrutadas a `OP-S-12`**, que es lo que la ficha manda en su cuarta
linea de `verificacion`, VERBATIM: *"las duplicadas que la fusion fabrica quedan
para OP-S-12, que corre despues"*. **La ficha se equivoco en la CANTIDAD, no en el
DESTINO**, y el destino es el que gobierna.

**LO QUE ESTA CORRECCION DEJA ESCRITO PARA LAS QUE FALTAN:** el desempate por
cableado y el conteo de duplicadas de una ficha sellada **se vuelven a medir el dia
de fundir, y si mueven, se declaran aqui**. En `OP-M-02-ACCLIMATE` el movimiento no
volteo nada (el superviviente gana por los dos conteos, y las duplicadas ya tenian
carril), pero **`OP-M-05-EDIFICIO` tiene el margen corto**: su `evidencia` linea 3
dice, VERBATIM, *"MEDIDO: cableado 6 contra 5 contra 3"*, o sea **una sola unidad
entre el superviviente y el primer perseguidor**, y ahi un movimiento de uno si
puede voltear un superviviente. Leido hoy de `OPERACIONES.jsonl` con codigo, no de
memoria.

## CORRECCION 10. **LAS CINCO FICHAS DE LA FASE 06 CONTRA SU PROPIA EJECUCION: EL CABLEADO Y LAS DUPLICADAS, MEDIDOS EL DIA DE FUNDIR**

**POR ADICION, Y NO SE TOCA NINGUNA FICHA.** Escrita en la vuelta 139, TAREA 3.
Es la hermana de la CORRECCION 9, que hizo lo mismo con `OP-M-02-ACCLIMATE`, y
sale de la misma regla: `P.9` y `P.13` con su frase comun, *"lo escrito el dia de
la decision hay que releerlo el dia de la ejecucion"*, y `EJECUTOR.md` regla 2,
**la discrepancia se declara, no se resuelve copiando**.

**COMO SE MIDIO:** `scripts/plan/simular_fusion.py` corrida el **2 sep 2026**
ANTES de cada fusion, con su salida sellada. Las cifras de la columna de la
ficha llevan corte **12 ago 2026** y salen de `docs/plan/OPERACIONES.jsonl`.

### 10.a. EL CABLEADO

| operacion | ficha (12 ago 2026) | medido el dia de fundir (2 sep 2026) | voltea |
|---|---|---|---|
| `OP-M-01-FUSION` | 9 contra 7, 5, 5 y 4 | **10** contra 7, 5, 4 y 5 | **NO** |
| `OP-M-03-III` | 13 contra 11 y 13 contra 4 | 13 contra **12** y 13 contra **3** | **NO** |
| `OP-M-05-INDICE` | 28 contra 6 contra 5 | **30** contra **11** y 30 contra **10** | **NO** |
| `OP-M-05-EDIFICIO` | 6 contra 5 contra 3 | **8** contra **6** y 8 contra 3 | **NO** |
| `OP-M-05-APERTURA` | 14 contra 8 contra 6 contra 5 | **18** contra **10** y 18 contra **8** | **NO** |

**NINGUNA VOLTEA UN SUPERVIVIENTE, y la que mas riesgo corria queda dicha:**
`OP-M-05-EDIFICIO` traia el margen mas corto del plan, **6 contra 5**, y su
propia ficha avisaba de que *"la lectura de acto de P.5 no es formalidad"* por
eso. Medido hoy, **el margen se ENSANCHA de 1 a 2** (8 contra 6). La vigilancia
que la ficha pedia se hizo y salio a favor de lo sellado.

**Y UNA NOTA DE FORMA, para que la tabla no se lea mal:** las celdas de la ficha
de `OP-M-05-INDICE`, `OP-M-05-EDIFICIO` y `OP-M-05-APERTURA` cuentan **la nomina
entera del acto** (tres o cuatro nodos en una sola cadena), mientras que el
instrumento de hoy imprime **un desempate por absorbido**. No es la misma forma
de contar, y por eso se publican las dos tal como cada fuente las escribe, sin
reescribir ninguna.

### 10.b. LAS DUPLICADAS QUE LA FUSION FABRICA

| operacion | ficha | hoy | los nombres |
|---|---|---|---|
| `OP-M-01-FUSION` | 4 | **5** | las cuatro de la ficha **mas** `tipos_criterios_gate.nodos_previos` |
| `OP-M-03-III` | 2 | 2 | **CUADRAN AL DIGITO Y CON SUS NOMBRES** |
| `OP-M-05-INDICE` | 4 | 4 | **CUADRAN AL DIGITO Y CON SUS NOMBRES** |
| `OP-M-05-EDIFICIO` | 1 | 1 | **CUADRA AL DIGITO Y CON SU NOMBRE** |
| `OP-M-05-APERTURA` | 3 | **6** | **SOLO DOS COINCIDEN** |

**LA DE `OP-M-05-APERTURA` ES LA DIVERGENCIA MAS GRANDE DE LA FASE 06 Y VA
ENTERA.** La ficha nombra tres: `business_model_canvas_scorecard.nodos_siguientes`,
`customer_creation.nodos_previos` y `customer_discovery.nodos_siguientes`. Hoy
son seis: siguen `business_model_canvas_scorecard` y `customer_discovery`, **ya
no esta `customer_creation`**, y aparecen `checkpoints_validacion.nodos_previos`,
`decision_pivotar_o_proceder.nodos_previos`,
`preservar_efectivo_buscar_modelo.nodos_siguientes` y
`realizar_pruebas_pasa_no_pasa.nodos_previos`.

**LO QUE NO CAMBIA EN NINGUNA DE LAS CINCO: EL DESTINO.** Todas las duplicadas,
las que la ficha previo y las que no, **quedan enrutadas a `OP-S-12`** por la
propia verificacion de cada ficha. **Las fichas se equivocaron en la CANTIDAD y,
en dos casos, en algun NOMBRE; ninguna se equivoco en el DESTINO**, y el destino
es el que gobierna. `OP-S-12` sigue al final de la pasada entera, por la atadura
2 del indice, y esta vuelta no lo toca.

**Y LO QUE NINGUNA MOVIO, medido en las cinco:** **CERO auto aristas nuevas** y
**CERO aristas internas del acto que sobrevivan**, en las cinco simulaciones y en
las cinco ejecuciones. La guarda B del fundidor (**cero duplicadas nuevas TRAS
RESOLVER**) sale **OK (0)** en las cinco, que es la cifra que de verdad importa
para el catalogo.

### 10.c. UNA LINEA DE `preservar` QUE NINGUNA MARCA DEL CONTRATO PUEDE CUMPLIR

**ES DE `OP-M-05-EDIFICIO`, linea 4, y no es una opinion sino una medicion campo
por campo.** Pide preservar *"la formulacion que le da nombre, NO HAY HECHOS
DENTRO DEL EDIFICIO"*, y su verificacion 2 manda comprobarla *"como FRASE"* en el
texto final.

**MEDIDO SOBRE `manifiesto_regla1_hechos_fuera_del_edificio` el 2 sep 2026:** esa
formulacion vive **SOLO en `node_id` y en `titulo_concepto`**. **NO esta en
ninguno de sus cuatro `pasos_accionables` ni en `resumen_teorico`.** Las cinco
marcas del contrato mueven pasos y condiciones VERBATIM, y **ninguna mueve un
titulo**; un `INCISO` cae en ROJO porque el trozo no es literal de ningun paso, y
escribirla a mano seria **inventar texto**, que es justo lo que el `INCISO`
existe para impedir.

**LO QUE SE HIZO, con regla escrita y no inventada:** se sello como **PERDIDA DE
ESPECIE `DE NOMBRE`**, una de las tres de `ESPECIES_DE_PERDIDA`, con sus cuatro
claves, **enrutada a la fase 04**, y declarando donde vive de verdad tras la
fusion: en **`merged_originals` del superviviente**, comprobado sobre el nodo
escrito (`titulo` = *"No Hay Hechos Dentro del Edificio: Sal a Buscarlos"*).
**NO SE PIERDE DEL CATALOGO.** Lo que no se puede es ponerla en el texto de los
pasos sin inventarla.

**QUEDA DECLARADO PARA EL AUDITOR: la verificacion 2 de esa ficha, TAL COMO ESTA
ESCRITA, NO SE PUEDE CUMPLIR con las cinco marcas de hoy.** No se toca la ficha y
no se finge que se cumplio.

### 10.d. DOS PIEZAS PROPIAS QUE `preservar` NO LISTABA

**Tambien de `OP-M-05-EDIFICIO`, y las registro porque su propia nota lo manda**
(*"si al leer los textos enteros aparece una pieza propia que no este en la lista
de perdidas, se registra antes de fundir"*). Aparecen **DOS**, y las dos en
`manifiesto_regla1_hechos_fuera_del_edificio`, no en `get_out_of_the_building`:

- **su paso 3**, conseguir experiencia de primera mano sobre **CADA PARTE** del
  modelo de negocio, que es mas ancho que el paso 1 del superviviente (que solo
  identifica hipotesis sobre problema, cliente y solucion);
- **su paso 4**, prepararse para recibir feedback **impredecible y a veces
  doloroso**, que es una disposicion y no la tiene ningun otro nodo del acto.

**Las dos viajan de `APPEND`**, porque `preservar` es **SUELO y no techo** (acta
138, adjudicacion 3.3) y marcarlas `CUBIERTO` habria afirmado del superviviente
algo que su texto no dice.

## CORRECCION 11. **UNA CIFRA DEL AUDITOR CONTRA LA MEDICION DEL DIA: "EL HUECO MUERDE EN TRES GRUPOS" ERAN CUATRO, Y NINGUNO ES EL QUE EL ACTA 138 NOMBRO**

**POR ADICION, Y NO SE BORRA NI SE REESCRIBE LA CIFRA VIEJA.** Escrita en la
vuelta 140, TAREA 1.b, por encargo expreso del acta 139 (caida **4.3**, del
auditor sobre si mismo). Sale de la misma regla que las CORRECCIONES 9 y 10:
`EJECUTOR.md` regla 2 y regla 8, **la discrepancia se declara, no se resuelve
copiando**, y *"una correccion que tapa lo que corrige no se puede auditar"*.

**ES LA PRIMERA CORRECCION DE ESTE FICHERO CUYA CIFRA VIEJA NO ES DE UNA FICHA
DEL PLAN SINO DE UN ACTA DEL AUDITOR.** Se registra igual que las otras, que es
lo que el encargo pide con esas palabras.

### 11.a. LAS DOS CIFRAS, CADA UNA CON SU CORTE Y SU AUTOR

| | cifra | quien la publica | corte | fuente |
|---|---:|---|---|---|
| **la vieja, que NO se borra** | **TRES grupos** | acta 138 del auditor, caida 4.2 (*"EL HUECO MUERDE EN TRES GRUPOS MEDIDOS, NO EN DOS"*) | **1 sep 2026** | lectura a mano sobre la linea 62 de `SALIDA_V138_3_PIEZA_DE_VARIOS_DUENOS.txt` |
| **la de hoy** | **CUATRO grupos** | ejecutor en la vuelta 139 (DISCUTIBLE 1), **adjudicado a favor** por el acta 139, 3.1, que lo re-midio a ciegas | **2 sep 2026** | lectura pieza por pieza de los cinco planes de la fase 06 |

**LOS CUATRO GRUPOS DE HOY, NOMBRADOS:** `OP-M-01-FUSION`, `OP-M-03-III`,
`OP-M-05-INDICE` y `OP-M-05-EDIFICIO`.

**EL QUE EL ACTA 138 NOMBRO Y HOY QUEDA FUERA:** `OP-M-05-APERTURA`.

**Y LA FORMA DE LA DISCREPANCIA NO ES "TRES CONTRA CUATRO", ES PEOR Y SE DICE
ENTERA:** de los grupos que el acta 138 conto, **`OP-M-05-APERTURA` es falso** y
**los tres que si muerden y no nombran ningun id no los vio**. La cifra no se
quedo corta por una unidad: **estaba mal poblada**.

### 11.b. POR QUE FALLO, Y ES EL PROXY Y NO LA ARITMETICA

**EL PROXY DEL QUE EL ACTA 138 SE FIO: "lineas de `preservar` que nombran DOS
absorbidos".** Se declara aqui, con las dos palabras que lo describen y que el
acta 139 escribio en su 4.3:

- **NO ES SUFICIENTE.** Que una linea de `preservar` nombre dos absorbidos **no
  implica que la pieza este partida entre los dos**. En `OP-M-05-APERTURA` la
  linea 3 nombra a los dos, y medido sobre el texto **sus tres partes (la
  repetibilidad, los pedidos a precio completo, los canales) estan LAS TRES en
  `introduccion_validacion_clientes`**, una por paso (1, 2 y 3). El paso 5 de
  `filosofia_customer_validation` toca **una** de las tres, **y como pregunta de
  puerta**. Un nombre en una linea no es una pieza compartida.
- **NO ES NECESARIO.** Los otros **tres** grupos donde el hueco si muerde
  (`OP-M-03-III`, `OP-M-05-INDICE` y `OP-M-05-EDIFICIO`) **no nombran ningun id
  en la linea de `preservar` correspondiente**, y el proxy no los podia ver por
  construccion.

**LA VARA QUE DECIDE SOLA Y QUE EL ACTA 138 NO USO, Y VIVE EN LA PROPIA FICHA:**
la linea **1** de `preservar` de `OP-M-05-APERTURA` **ya reclama ese paso 5
entero**, literal, *"de filosofia_customer_validation: LAS TRES PREGUNTAS DE
ESCALA"*. Leer la linea 3 como si viviera tambien ahi **asigna el mismo paso a
dos lineas de `preservar`**, y marcarlo `VIAJA_EN_EL_ACTO` habria **perdido las
preguntas del crecimiento y de la prediccion**. **No era discutible: estaba
prohibido por la ficha.**

### 11.c. QUE SE CAE Y QUE SIGUE EN PIE

- **SIGUE EN PIE lo que la caida 4.2 del acta 138 era en su nucleo:** el reporte
  de la vuelta 138 nombro **dos grupos distintos** de los que su propia salida
  sellada nombraba. Eso se midio contra el fichero y no se toca.
- **SE CAE la conclusion montada encima**, o sea la cifra de **TRES** y el
  nombre de `OP-M-05-APERTURA` como tercero.
- **NO SE TOCA NINGUNA FICHA de `docs/plan/OPERACIONES.jsonl`** ni ningun
  veredicto: esta correccion registra **una cifra de acta**, no un dato del
  plan.
- **CONSECUENCIA PARA QUIEN LEA DESPUES:** cuando haga falta contar donde el
  hueco muerde, **la vara no es el proxy sintactico sino la lectura pieza por
  pieza de los planes**, que es la que produjo la cifra de CUATRO. El proxy
  puede seguir usandose como **buscador de candidatos**, nunca como censo, que
  es exactamente lo que el banco **9.28** ya dice de su propio barrido
  (*"El instrumento no puede ser un censo: puede ser un buscador de
  candidatos"*).

## CORRECCION 12. **ENTRADA DE FASE 04: LA PERDIDA DE NOMBRE DE `OP-M-05-EDIFICIO`, CON EL REMEDIO LITERAL DEL BANCO 9.28 DENTRO**

**POR ADICION.** Escrita en la vuelta 140, TAREA 1.c, por encargo del acta 139,
adjudicacion **3.5**. Es la continuacion de la **10.c** de la CORRECCION 10, que
sello la perdida; esta escribe **el remedio**, para que la fase 04 no tenga que
redescubrirlo. **No se toca la ficha ni el nodo: la fase 04 es quien ejecuta.**

### 12.a. LA PERDIDA, TAL COMO QUEDO SELLADA

**Operacion:** `OP-M-05-EDIFICIO`, fase 06, ejecutada el **2 sep 2026**
(vuelta 139).
**Especie:** `DE NOMBRE`, una de las tres de `ESPECIES_DE_PERDIDA`.
**Muere:** `manifiesto_regla1_hechos_fuera_del_edificio`.
**Sobrevive:** `get_out_of_the_building`.
**La denominacion que se pierde del TEXTO:** *"NO HAY HECHOS DENTRO DEL
EDIFICIO"*, la formulacion que la linea 4 de `preservar` manda preservar y que la
verificacion 2 de la ficha manda comprobar **como frase** en el texto final.

**MEDIDO CAMPO POR CAMPO EL 2 SEP 2026:** esa formulacion vive **SOLO en
`node_id` y en `titulo_concepto`** del absorbido. **NO esta en ninguno de sus
cuatro `pasos_accionables` ni en `resumen_teorico`.** Tras la fusion vive en
`merged_originals` del superviviente, comprobado sobre el nodo escrito.

**POR QUE NINGUNA MARCA DE FUSION PUEDE MOVERLA:** las cinco marcas del contrato
mueven **pasos y condiciones VERBATIM**, y **ninguna mueve un titulo**; un
`INCISO` cae en ROJO porque el trozo no es literal de ningun paso, y escribirla a
mano seria **inventar texto**, que es justo lo que el `INCISO` existe para
impedir.

### 12.b. EL REMEDIO, LITERAL DEL BANCO 9.28, PARA QUE NO SE PIERDA EN EL CAMINO

**El banco de textos, seccion `9.28 CLASE DE PERDIDA: LA PERDIDA DE NOMBRE`,
nombra esta especie exacta:**

> **HAY FUSIONES DONDE LO QUE MUERE NO ES UN PASO NI UNA LINEA: ES LA PALABRA POR
> LA QUE EL LECTOR LLEGA.**

**Y ESCRIBE SU REMEDIO, y esta es la linea que la fase 04 tiene que ejecutar,
citada literal de esa misma seccion:**

> **EL REMEDIO, y es barato:** el nombre **viaja como DENOMINACION**, **una linea
> en el texto del superviviente**, no un paso ni un nodo. Basta con que el titulo
> o la primera linea digan *tambien llamada funcion de perdida de Taguchi*.

**QUE SIGNIFICA AQUI, sin inventar nada:** en `get_out_of_the_building` la
denominacion *"no hay hechos dentro del edificio"* tiene que aparecer **en el
texto que el lector ve**, como **una linea de denominacion** (titulo o primera
linea del `resumen_teorico`), **no como un paso nuevo ni como un nodo nuevo**.

**POR QUE EL ALIAS NO BASTA, y el 9.28 lo dice con su tabla:** el id muerto queda
en `ids_alias` y **eso cubre el GRAFO, no cubre AL LECTOR**. *"Un alias es una
redireccion interna. El lector que escribe [la denominacion] no esta resolviendo
un id: esta buscando una palabra que tiene que estar EN EL TEXTO."*

**COMO SE COMPROBARA QUE QUEDO HECHO, y es comprobable por script** (el criterio
de reconocimiento del propio 9.28): la denominacion **aparece en algun sitio del
texto del superviviente**, no solo en `merged_originals` ni en `ids_alias`.

### 12.c. LO QUE ESTA ENTRADA NO HACE, DICHO PARA QUE NADIE LO LEA DE MAS

- **NO se ejecuta aqui.** La denominacion **la escribe la pasada editorial**
  (adjudicacion 3.5 del acta 139: *"Una denominacion no la mueve ninguna marca de
  fusion: la escribe la pasada editorial"*). Esta entrada solo la enruta con su
  remedio dentro.
- **NO hace falta una sexta marca de fusion.** El acta 139, 3.5, lo adjudica con
  esas palabras, y el carril (`PERDIDA DE NOMBRE` enrutada a la fase 04) queda
  confirmado como el correcto.
- **NO se toca la ficha de `OP-M-05-EDIFICIO`, y queda dicho lo que la 10.c ya
  declaraba:** su **verificacion 2, tal como esta escrita, no se puede cumplir**
  con las cinco marcas de hoy. No se finge que se cumplio.

## CORRECCION 13. **LA CUENTA DE FILAS DE `OP-E-04` EN VIOLACION DE SU PROPIA VERIFICACION 0: TRES CONTRA CINCO, Y LA CIFRA VIEJA NO SE BORRA**

**POR ADICION, Y NO SE BORRA NI SE REESCRIBE LA CIFRA VIEJA.** Escrita en la
vuelta 141, TAREA 1.b, por encargo expreso del acta 140 (caida **4.1**, del
auditor sobre el ejecutor). Sale de la misma regla que las CORRECCIONES 9, 10 y
11: `EJECUTOR.md` regla 2 y regla 8, **la discrepancia se declara, no se resuelve
copiando**, y *"una correccion que tapa lo que corrige no se puede auditar"*.

**LA AFIRMACION SOBRE LA QUE LAS DOS CIFRAS SE MIDEN**, literal de la
`verificacion` 0 de la ficha de `OP-E-04` en `docs/plan/OPERACIONES.jsonl`, leida
en la vuelta 141:

> *"UNA SOLA DIRECCION POR ENLACE, de la madre al hijo. La vuelta no debe existir
> ni literal ni resuelta, por la regla de la escalera"*

### 13.a. LAS DOS CIFRAS, CADA UNA CON SU AUTOR, SU CORTE Y SU FUENTE

| | cifra | quien la publica | corte | fuente | como se midio |
|---|---:|---|---|---|---|
| **la vieja, que NO se borra** | **TRES filas**: `LD-42`, `LD-48`, `LD-53` | ejecutor, reporte de la vuelta 140 | **2 sep 2026** | `docs/loop/REPORTE.md` de la vuelta 140, seccion de la TAREA 3, remitida 5 de 5 | la vara de enlace de `tallar_estado_de_fase.py` **mide si la IDA esta presente** y nunca mira la vuelta; solo se inspeccionaron **las filas que aun no estaban puestas** |
| **la de hoy** | **CINCO filas**: `LD-35`, `LD-42`, `LD-48`, `LD-49`, `LD-51` | auditor, acta 140, caida 4.1; **re-medida por el ejecutor en la vuelta 141** | **corte de la vuelta 141** | `docs/loop/SALIDA_V141_1B_IDA_Y_VUELTA_OPE04.txt`, de `python scripts/loop/vuelta141_1b_medir_ida_y_vuelta.py --op OP-E-04` | **ida y vuelta a la vez**, con el resolutor de la casa (`P.1`) puesto y las dos vistas miradas (`nodos_siguientes` del origen y `nodos_previos` del destino) |

**LA TABLA DE LA MEDICION DE HOY, PEGADA DE SU FICHERO DE SALIDA Y NO TECLEADA**
(`docs/loop/SALIDA_V141_1B_IDA_Y_VUELTA_OPE04.txt`):

| lectura | fila cruda (origen -> destino) | origen resuelto | destino resuelto | IDA presente | VUELTA presente |
|---|---|---|---|---|---|
| LD-35 | gestion_portafolio_dos_niveles -> estructura_gates | gestion_portafolio_dos_niveles | sistema_gates_go_kill | SI | SI |
| LD-40 | requisitos_gates_con_dientes -> portfolio_management | sistema_gates_go_kill | portfolio_management | SI | no |
| LD-42 | requisitos_gates_con_dientes -> revision_portafolio_periodica | sistema_gates_go_kill | revision_portafolio_periodica | no | SI |
| LD-45 | requisitos_gates_con_dientes -> gestion_portafolio_foco | sistema_gates_go_kill | gestion_portafolio_foco | no | no |
| LD-48 | portfolio_management -> gates_go_kill_decision_points | portfolio_management | sistema_gates_go_kill | no | SI |
| LD-49 | gestion_portafolio_formal -> gates_go_kill_decision_points | gestion_portafolio_formal | sistema_gates_go_kill | SI | SI |
| LD-51 | gestion_portafolio_dos_niveles -> gates_go_kill_decision_points | gestion_portafolio_dos_niveles | sistema_gates_go_kill | SI | SI |
| LD-53 | gestion_portafolio_foco -> gates_go_kill_decision_points | gestion_portafolio_foco | sistema_gates_go_kill | no | no |
| LD-55 | decision_factory_mentality -> gates_go_kill_decision_points | decision_factory_mentality | sistema_gates_go_kill | no | no |

**Y LAS CIFRAS DE CIERRE DE ESA MISMA SALIDA, tambien pegadas:** *"FILAS DE
FICHA: 9 | DIRECCIONES DISTINTAS TRAS RESOLVER: 8"*, *"FILAS CON LA IDA
PRESENTE: 4 | FILAS CON LA VUELTA PRESENTE: 5"*, *"EN VIOLACION DE LA
VERIFICACION 0 (la vuelta existe hoy), 5 fila(s): LD-35, LD-42, LD-48, LD-49,
LD-51"*.

### 13.b. POR QUE DISCREPAN, Y NO ES ARITMETICA: ES QUE LA VARA MIRABA MEDIA COSA

**LA CAUSA, NOMBRADA:** la vara de enlace de `scripts/loop/tallar_estado_de_fase.py`
contaba **cuantas `aristas_nuevas` estan presentes**, y de ahi derivaba las que
faltaban. Una fila cuya **ida ya estaba puesta** salia como *"YA PRESENTE"* y **la
vara no seguia mirando**: la vuelta, que es lo que la verificacion 0 prohibe,
nunca se media. Por eso la cifra vieja solo pudo poblarse con filas **sin la ida
puesta**, y de esas solo tres tenian la vuelta.

**LAS TRES QUE LA CIFRA VIEJA NO PUDO VER, Y POR QUE:** `LD-35`, `LD-49` y
`LD-51` tienen **la ida presente**, asi que la vara las dio por buenas y paro.
Las tres tienen **tambien la vuelta presente**, o sea que las tres violan la
verificacion 0 y ninguna aparecia en la cuenta.

**Y `LD-53` ESTA EN LA CIFRA VIEJA Y NO EN LA DE HOY:** medida hoy con las dos
direcciones, `LD-53` tiene **ida no presente y vuelta no presente**. Es una fila
**sin escribir**, no una fila en violacion. La cifra vieja la contaba porque
mezclaba las dos cosas en un solo saco: *lo que falta por poner* y *lo que esta
puesto al reves*. **Son dos poblaciones distintas y hoy se publican separadas:**
en violacion de la verificacion 0 van **CINCO** (`LD-35`, `LD-42`, `LD-48`,
`LD-49`, `LD-51`); sin la ida puesta van **CINCO** tambien, y no son las mismas
(`LD-42`, `LD-45`, `LD-48`, `LD-53`, `LD-55`).

**LA FORMA DE LA DISCREPANCIA, DICHA ENTERA:** no es *"tres contra cinco"* por
una unidad y media. De las tres que la cifra vieja nombro, **dos siguen en pie**
(`LD-42` y `LD-48`) y **una no era de esta especie** (`LD-53`); y **tres que si
lo son no se vieron** (`LD-35`, `LD-49`, `LD-51`). La cifra vieja **estaba mal
poblada**, igual que la de la CORRECCION 11.

### 13.c. LO QUE ESTO ARRASTRA, Y QUE NO SE TOCA

- **DOS DE ESAS VUELTAS LAS ESCRIBIO LA VUELTA 140 ELLA MISMA.** `OP-E-05`
  escribio `sistema_gates_go_kill -> gestion_portafolio_dos_niveles` y su
  reciproca; resueltas, **son la vuelta de `LD-35` y de `LD-51`**. Es decir que
  una operacion de la mesa escribio la arista que otra operacion de la misma
  mesa prohibe, **y la tabla del reporte de la 140 publica las dos como
  CUMPLIDAS**. El choque es real y **no se resuelve aqui**: lo resuelve la
  lectura de la TAREA 3 de la vuelta 141 con la vara del banco 9.22, bajo el
  criterio de la CORRECCION 14.
- **NO SE TOCA NINGUNA FICHA de `docs/plan/OPERACIONES.jsonl`** ni ningun
  veredicto: esta correccion registra **una cifra de reporte**, no un dato del
  plan. El campo `estado` de `OP-E-04` sigue sin tocarse.
- **NO SE BORRA LA CIFRA VIEJA.** Queda arriba, con su autor y su corte, junto a
  la de hoy.
- **CONSECUENCIA PARA QUIEN LEA DESPUES, Y ES LA UTIL:** *"YA PRESENTE" NO ES UN
  VEREDICTO, ES MEDIA MEDICION.* Antes de publicar que una operacion de enlace
  cumple, se miden **sus dos direcciones** con el resolutor puesto en las dos
  vistas y se publica **cuantas tienen la vuelta presente**, aunque la ida ya
  estuviera. El remedio en codigo esta en la vuelta 141, TAREA 2.a.

## CORRECCION 14. **EL CRITERIO DEL PAR COLAPSADO: CUANDO UNA FUSION JUNTA LAS DOS DIRECCIONES DE UN MISMO PAR, EL PAR SE RELEE CON LA VARA DEL 9.22**

**POR ADICION.** Escrita en la vuelta 141, TAREA 1.c, por encargo del acta 140,
adjudicacion **3.7**. **Es un CRITERIO, no una medicion**, y el auditor lo dice
con esas palabras (`AUDITOR.md` 2). Se escribe aqui, y no en una ficha, para que
**la fase 04 y la fase 06 lo encuentren las dos**: la fase 04 porque es donde
viven `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES` y `OP-M-01-SEXTO`, y la fase 06
porque es la mesa que las remitio.

**NO ES DOCTRINA NUEVA, Y POR ESO NO HAY PARADA.** Las dos reglas que lo
sostienen estaban escritas antes de esta vuelta, y van citadas literales abajo.

### 14.a. LA ESPECIE, DESCRITA SIN NOMBRES PROPIOS

Una lectura dirigida escribe `A -> B`. Otra lectura dirigida, de **otro par**,
escribe `C -> D`. Llega una fusion y **`B` y `C` colapsan en el mismo
superviviente**, o **`A` y `D` colapsan**. Tras resolver, las dos aristas dejan
de ser de pares distintos: **son la ida y la vuelta del mismo par**.

**QUE PASA ENTONCES.** Si una de las dos fichas lleva la regla de la escalera en
su verificacion (*"la vuelta no debe existir ni literal ni resuelta"*), esa
verificacion **queda en violacion sin que nadie haya escrito mal nada**: la
fusion la puso en violacion. Y la otra ficha, que puede ser un `ENLACE MUTUO`
legitimo, **manda expresamente que la vuelta exista**.

### 14.b. LAS DOS CITAS LITERALES QUE LO GOBIERNAN

**(1) LA CONTRAORDEN DEL AUDITOR DEL 12 ago 2026**, en
`docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md`, seccion *"CONTRAORDEN DEL AUDITOR,
12 ago 2026: SE GIRA LA EXISTENTE"*:

> **EN UN GRAFO DE SECUENCIA LA VUELTA ES UNA INSTRUCCION FALSA, y el ciclo de
> dos FABRICA LA AVERIA QUE ESTA CAMPANA ESTA QUITANDO.**

y dos parrafos despues, en la misma seccion:

> **Y ESO DEJA UNA REGLA QUE VALE PARA TODAS LAS MESAS QUE VIENEN: en una
> escalera, la arista de vuelta no es redundante, es FALSA.** Decir *despues de
> formalizar viene identificar* **manda al lector a repetir el paso que acaba de
> dar.**

**Y SU REMEDIO OPERATIVO, tambien literal de esa seccion**, que es la parte que
convierte la regla en algo ejecutable: alli **la vuelta se retira del campo**
(*"`formalizar_junta_asesora`.`nodos_siguientes` | contiene
`identificar_junta_asesores` | se retira"*), **la ida se escribe**, todo **en el
mismo commit de la operacion que lo descubre**, y **el grado total NO SUBE**
(*"el grado total del acto NO SUBE: se gira una arista, no se anade. Si el conteo
sube en uno, se anadio en vez de girar"*).

**(2) EL BANCO 9.22 Y EL HUECO DE ORDEN 1 DEL `00_INDICE`**, que escriben la
excepcion y dan el test objetivo. Del banco, seccion *"9.22 FIGURA: LA VARA EN
LOS DOS SENTIDOS"*:

> **LA COMPROBACION QUE LA SEPARA DE LA DUPLICACION.** Si las dos direcciones
> apuntan a **la misma linea**, no es esta figura: es un solape y se juzga por
> las reglas de siempre. **La figura exige dos lineas distintas**, una en cada
> nodo.

Y del `00_INDICE`, *"LOS CUATRO HUECOS DE ORDEN QUE ESTE RESUMEN DESTAPA"*,
hueco **1**:

> **LA GUARDA TIENE QUE LLEVAR LA EXCEPCION ESCRITA, o el dia de la pasada borra
> cuatro aristas que costaron dos lecturas.** **La regla de la escalera vale para
> las ESCALERAS, no para los enlaces mutuos.**

### 14.c. EL CRITERIO, EN SUS TRES PIEZAS

**(i) EL PAR SE RELEE CON LA VARA DEL 9.22.** Cuando una fusion colapsa dos
aristas que eran de pares distintos **en las dos direcciones de un mismo par**,
el par **no se resuelve por antiguedad ni por cual ficha se ejecuto antes**: se
**relee**, leyendo **las dos lineas** que las dos lecturas dirigidas citan, **en
el nodo de HOY** y no en la ficha del 12 ago 2026. `P.12` cubre el reparto: **el
colapso convoca, la lectura decide.**

**(ii) EL TEST ES DE LINEAS, Y TIENE DOS SALIDAS Y NADA MAS.**

| lo que devuelve la relectura | la figura | que pasa con las dos direcciones |
|---|---|---|
| **DOS LINEAS DISTINTAS**, una en cada nodo, cada una expandida por el otro | **ENLACE MUTUO** (banco 9.22, primer polo) | **las dos viven**, y la figura **se registra**. La regla de la escalera **no aplica** |
| **LA MISMA LINEA** en las dos direcciones | **ESCALERA** | **la vuelta se retira** por la contraorden del 12 ago 2026, y la ida queda |

**El test es de LINEAS, no de tamano de nodo** (acta 140, 3.7): que un extremo
sea un superviviente muy crecido no cambia la vara. **Lo que queda abierto y va
nombrado:** si un superviviente crecido deja de *expandir* una linea y pasa a
*dominarla*, el 9.22 no lo mide. **Hoy no muerde; si asoma, es del fundador.**

**(iii) QUIEN CORTA, Y COMO SE MIDE QUE NO SE PASO.** Corta **la operacion cuya
verificacion lo exige**, **en su propio commit**, y **lo declara como GIRO o como
PODA**. Y se mide, por la contraorden:

- **el grado total se mide ANTES y DESPUES de cada retiro**;
- **girar NO sube el grado** (se retira una direccion y se escribe la otra: neto
  cero);
- **podar lo BAJA en uno** (se retira una direccion y no se escribe ninguna);
- **si el grado SUBE, se anadio en vez de girar, y esta mal.**

### 14.d. LO QUE ESTE CRITERIO NO AUTORIZA, DICHO PARA QUE NADIE LO LEA DE MAS

- **NO autoriza podar el grafo por gusto.** La contraorden cubre **la vuelta de
  una escalera que una ficha prohibe**. Si una retirada tocase una arista que
  **ninguna operacion del plan propuso ni prohibe**, esa retirada **se para y se
  trae**, no se ejecuta (`AUDITOR.md` 4: no se borra contenido que ninguna regla
  ordena).
- **NO decide cual sale en cada par.** El acta 140, 3.7, lo dice con esas
  palabras: *"NO ADJUDICO CUAL SALE EN CADA PAR: eso es lectura"*. Este criterio
  fija **la vara**; la adjudicacion par por par es trabajo de lectura y se marca
  **DISCUTIBLE** antes de conocer el resultado.
- **NO toca el campo `estado` de ninguna ficha.** El pase de estado de las once
  operaciones de la fase 06 sigue reservado a **una sola adjudicacion del
  auditor**, con el conteo antes y despues (acta 139, 3.6, y acta 140).
- **NO reescribe ninguna ficha de `docs/plan/OPERACIONES.jsonl`.** Las
  verificaciones de `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES` y `OP-M-01-SEXTO`
  quedan tal como estan; lo que este criterio dice es **como se leen cuando
  chocan**.

## CORRECCION 15. **EL TOTAL DE DIRECCIONES DE LA FASE 06: TRES CIFRAS, DOS UNIVERSOS Y DOS UNIDADES, Y LA VIEJA NO SE BORRA**

**POR ADICION.** Escrita en la vuelta 142, TAREA 1.b, por encargo del acta 141.
Cubre a la vez la **caida 4.4 del auditor** (cifra publicada en el acta 140) y la
**caida 4.1 del ejecutor** (declarar concordancia donde habia discrepancia de
composicion). **NADA DE LO VIEJO SE BORRA:** las tres cifras quedan escritas, cada
una con su autor, su corte y su fichero, que es lo que `EJECUTOR.md` 8 manda.

### 15.a. LAS TRES CIFRAS, UNA POR FILA

**LA TABLA SALE DE UN INSTRUMENTO Y SE PEGA ENTERA.** Comando corrido en esta
vuelta: `python scripts/loop/vuelta142_1b_desglose_direcciones.py --fase 06_MESAS`.
Salida en `docs/loop/SALIDA_V142_1B_DESGLOSE_DIRECCIONES.txt`.

| cifra | unidad | universo | desglose | autor | corte | fichero |
|---:|---|---|---|---|---|---|
| **18** | **direcciones** (asi la rotulo el acta) | **CINCO** operaciones | 2+9+4+2+1 | auditor | acta 140, adjudicacion 3.4 | `docs/loop/ACTA_AUDITOR.md`, acta de la vuelta 140 |
| **17** | **direcciones** | **CINCO** operaciones remitidas por `docs/plan/04_ENLACES.md` | 2+8+4+2+1 | ejecutor, vuelta 142 | 2 sep 2026 | `docs/loop/SALIDA_V142_1B_DESGLOSE_DIRECCIONES.txt`, universo 1 |
| **18** | **direcciones** | **SEIS** operaciones del catalogo con direcciones, `OP-M-05-APERTURA` dentro | 8+4+2+1+2+1 | ejecutor, vuelta 141 y re-medido en la 142 | 2 sep 2026 | `docs/loop/SALIDA_V142_1B_DESGLOSE_DIRECCIONES.txt`, universo 2 |

### 15.b. POR QUE DISCREPAN, MEDIDO Y NO OPINADO

**SON DOS DEFECTOS DISTINTOS SUMADOS, Y CADA UNO TIENE SU NOMBRE.**

**(1) EL 18 DEL ACTA 140 MEZCLA DOS UNIDADES DENTRO DE UNA SOLA SUMA.** Su
desglose mete **9 FILAS DE FICHA** de `OP-E-04` en una suma que la propia
adjudicacion 3.4 rotula en **DIRECCIONES**, y la propia adjudicacion lo dice tres
lineas antes (*"4 mas 5 da 9 filas, pero solo hay 8 direcciones"*). El instrumento
de hoy lo separa sin ambiguedad: sobre las cinco remitidas hay **18 FILAS DE
FICHA** y **17 DIRECCIONES DISTINTAS**. **El 18 del acta es correcto como filas de
ficha y falso como direcciones**, y la unidad que el acta escribio es la segunda.

**(2) EL 18 DE LA VUELTA 141 CUENTA UN UNIVERSO MAS ANCHO.** Su instrumento
recorre **todas** las operaciones del catalogo de la fase 06 con `aristas_nuevas`,
y eso mete a `OP-M-05-APERTURA` (**2 filas de ficha que colapsan en 1 direccion**,
remitida por `docs/plan/00_INDICE.md:261` y no por la tabla de las cinco), que el
acta 140 nunca conto. Medido hoy: **universo 1, cinco operaciones, 17
direcciones; universo 2, seis operaciones, 18 direcciones; diferencia exacta 1, y
esa 1 es `OP-M-05-APERTURA`.**

**LOS DOS TOTALES DAN 18 POR CASUALIDAD:** uno suma una fila de ficha de mas, el
otro suma una operacion de mas, y los dos errores valen exactamente 1. **Por eso
declarar concordancia entre los dos era la caida: coincidian los totales y no las
composiciones.**

### 15.c. LA REGLA QUE QUEDA, Y NO ES NUEVA

**LA UNIDAD SIGUE SIENDO LA DIRECCION** (acta 140, adjudicacion 3.4: *"es lo que
el grafo guarda y lo que la vara mide, y la cadena esconde el enlace mutuo"*), y
`tallar_estado_de_fase.py` ya la publica asi desde la vuelta 141, TAREA 2.c. **LO
QUE ESTA CORRECCION ANADE ES QUE UN TOTAL LLEVA SU UNIVERSO AL LADO**, no solo su
unidad: dos cifras de la misma unidad sobre universos distintos **no se cotejan**,
y si se cotejan hay que decir cual universo se toma. Es `EJECUTOR.md` 2 aplicado a
un total (*"si discrepan de la medicion de hoy, la discrepancia se declara en vez
de resolverse copiando"*) y `AUDITOR.md` 1.1.

**CIFRA VIEJA QUE NO SE BORRA, Y SE DICE DONDE VIVE:** el **18 (2+9+4+2+1)** del
acta 140 sigue escrito en `docs/loop/ACTA_AUDITOR.md` tal cual, y el **18** de la
vuelta 141 sigue escrito en `docs/loop/REPORTE.md` de esa vuelta y en
`docs/loop/SALIDA_V141_4_RELECTURA_AL_DOBLE.txt` tal cual. Esta correccion no
reescribe ninguno de los dos: los **coloca al lado de la medicion de hoy con su
universo nombrado**.

## CORRECCION 16. **EL SUPERVIVIENTE DIVERGENTE: UNA FUSION CONSUMIDA AL REVES NO ES CUMPLIDA NI SIN CUMPLIR**

**POR ADICION.** Escrita en la vuelta 142, TAREA 1.c, por encargo del acta 141,
adjudicacion **3.5**. **Es un CRITERIO con dos casos medidos detras.** Se escribe
aqui, y no en una ficha, porque gobierna **la vara `FUSION` de cualquier fase**, no
solo a las dos fichas que hoy la disparan.

**NO ES DOCTRINA NUEVA, Y POR ESO NO HAY PARADA.** Las tres cosas que la sostienen
estaban escritas antes de esta vuelta y van citadas abajo con su fichero.

### 16.a. LA ESPECIE, DESCRITA SIN NOMBRES PROPIOS

Una ficha de `FUSION` escribe un `superviviente` y un `eliminar`. Mas tarde, otra
operacion ejecuta la fusion **al reves**: deja vivo al que la ficha mandaba
eliminar y deprecar al que la ficha nombraba superviviente, con alias del muerto
al vivo. **El par queda consumido** (resuelve a un solo vivo, que es lo que la
fusion buscaba) **y a la vez ejecutado contra la letra de su ficha.**

**QUE PASA SI LA VARA SOLO RESUELVE.** Si la vara `FUSION` pasa el `superviviente`
escrito por el resolutor y se queda con lo que salga, el caso sale **CUMPLIDO**:
el id resuelto esta vivo, el absorbido esta deprecado y en `ids_alias`. **Y eso es
publicar CUMPLIDO sobre una operacion ejecutada al reves**, que es la degradacion
silenciosa del banco 9 entrando por la puerta de un arreglo que parece obvio.

### 16.b. LOS DOS CASOS, MEDIDOS CONTRA EL GRAFO DE HOY

Corte **2 sep 2026**. Los cuatro campos de cada fila salen de
`docs/plan/OPERACIONES.jsonl` y de `dataset/metadata/master_graph.json`, resueltos
con el resolutor de la casa (`EJECUTOR.md` regla 9, `P.1`).

| ficha | `superviviente` escrito | ¿vivo hoy? | resuelve a | ¿vivo? | campo `eliminar` de la ficha | ¿el que sobrevive esta en `eliminar`? |
|---|---|---|---|---|---|:---:|
| `OP-M-02-ADMIT` | `fase_admit` | **NO, deprecado** | `fase_admit_celebracion` | **si** | `["fase_admit_celebracion"]` | **SI** |
| `OP-M-02-MEDIOS` | `seis_medios_comunicacion_cliente` | **NO, deprecado** | `estrategia_multicanal_bienvenida` | **si** | `["estrategia_multicanal_bienvenida"]` | **SI** |

**EN LAS DOS, EL QUE SOBREVIVE ES EXACTAMENTE EL QUE LA FICHA MANDA ELIMINAR.**

### 16.c. LAS TRES COSAS ESCRITAS QUE LO GOBIERNAN, CITADAS

**(1) LA CORRECCION DECLARADA DE LA VUELTA 64, EN EL `nota` DE LAS DOS FICHAS**
(`docs/plan/OPERACIONES.jsonl`), literal:

> **CORRECCION DECLARADA (2026-08-20, vuelta 64, TAREA 1.c del encargo), POR EL
> CARRIL DEL BANCO 9.10 Y CON EL TEXTO VIEJO ENTERO ARRIBA: ESTA FICHA ESTA
> CONSUMIDA. NO SE EJECUTA Y NO SE REHACE.**

**(2) `docs/loop/SALIDA_V64_CONSUMIDAS.txt`**, que computa **CINCO fusiones de
mesa consumidas** y separa **DOS que DIVERGEN** de **TRES que COINCIDEN**, con el
criterio ya escrito alli (*"el par resuelve a UN solo vivo"* mas *"DIVERGEN: la
ficha decia X y el tramo dejo vivo a Y"*):

> `OP-M-02-MEDIOS` **DIVERGEN**, `OP-M-02-ADMIT` **DIVERGEN**, `OP-M-02-ASSESS`
> **COINCIDEN**, `OP-M-02-ACTIVATE` **COINCIDEN**, `OP-M-02-ACCOMPLISH`
> **COINCIDEN**.

**(3) `EJECUTOR.md` regla 9 con `P.1`**: *"Todo conteo que toque ids pasa por el
resolutor antes de contar"*. La vara **si** tiene que resolver; lo que no puede es
**quedarse solo con eso**.

### 16.d. EL CRITERIO ADJUDICADO, Y EL TERCER VEREDICTO

**UNA OPERACION `FUSION` CUYO `superviviente` ESCRITO ESTA DEPRECADO Y RESUELVE A
UN NODO VIVO QUE SU PROPIA FICHA LISTA EN `eliminar` NO ES CUMPLIDA NI SIN
CUMPLIR: ES `CONSUMIDA CON SUPERVIVIENTE DIVERGENTE`.** La celda publica las tres
cosas (el id escrito, el id al que resuelve y el campo `eliminar` que lo condena)
y **NUNCA la llama cumplida**.

Y el caso vecino, que tambien se nombra en vez de callarse: **un `superviviente`
deprecado que resuelve a un vivo que la ficha NO lista en `eliminar` se publica
como `CONSUMIDA` y se nombra, sin llamarla cumplida** tampoco.

### 16.e. POR QUE EL RESOLUTOR A SECAS SILENCIARIA SOLO A LAS QUE MERECEN RUIDO

**MEDIDO HOY, NO SUPUESTO.** `python scripts/loop/tallar_estado_de_fase.py --fase
03_FUSIONES`, corrido en esta vuelta ANTES del cambio de vara
(`docs/loop/SALIDA_V142_1C_ESTADO_FASE03_ANTES.txt`):

- **`OP-M-02-ASSESS`, `OP-M-02-ACTIVATE` y `OP-M-02-ACCOMPLISH` ya salen
  `CUMPLIDO`**, cada una con su superviviente escrito vivo y su absorbido
  deprecado y en `ids_alias`. **Las tres que COINCIDEN no necesitan el
  resolutor.**
- **`OP-M-02-ADMIT` y `OP-M-02-MEDIOS` salen `SIN CUMPLIR`**, las dos con la misma
  razon computada (*"superviviente X NO esta vivo hoy"*).

**O SEA QUE PONER EL RESOLUTOR AL `superviviente` Y NADA MAS NO ANADIRIA NINGUNA
CUMPLIDA LEGITIMA: SOLO CONVERTIRIA EN CUMPLIDAS A LAS DOS DIVERGENTES.** El rojo
de esas dos **no es ruido: es el sintoma bien puesto y mal rotulado**, y el remedio
es rotularlo, no apagarlo.

## CORRECCION 17. **EL `00_INDICE` DICE "LAS UNICAS" Y HOY SON EL DOBLE: CUATRO PARES Y OCHO ARISTAS, Y LA FRASE VIEJA NO SE BORRA**

**POR ADICION.** Escrita en la vuelta 143, TAREA 1.b, por encargo del acta 142,
adjudicacion 3.4. Corte de todas las cifras de esta correccion: **2 sep 2026**
(`git log -1 --format=%ad --date=short`, corrido en esta vuelta).

### 17.a. LA FRASE VIEJA, CITADA LITERAL Y SIN TOCAR

`docs/plan/00_INDICE.md:478`, dentro del **hueco de orden 1**, dice literal:

> **Los dos enlaces mutuos del banco 9.22 son las UNICAS aristas del plan que van en las
> dos direcciones a proposito.**

**ESA LINEA NO SE BORRA NI SE REESCRIBE.** Sigue en su fichero, en su linea y con
sus palabras, y esta correccion **la coloca al lado de la medicion de hoy**, que
es lo que `EJECUTOR.md` 8 manda (*"una correccion que tapa lo que corrige no se
puede auditar"*).

### 17.b. LA MEDICION DE HOY, TALLADA DE UN INSTRUMENTO Y NO TECLEADA

**Comando corrido en esta vuelta:**
`python scripts/loop/vuelta143_1b_pares_de_doble_direccion.py`.
Salida entera en `docs/loop/SALIDA_V143_1B_PARES_DOBLE_DIRECCION.txt`. El
instrumento recorre **las 71 fichas** de `docs/plan/OPERACIONES.jsonl`, saca los
pares con el parser de `tallar_estado_de_fase.py`, los **resuelve por alias**
(`P.1`, `EJECUTOR.md` regla 9) y busca los pares no ordenados `{A, B}` para los
que **la misma ficha** escribe `A -> B` y `B -> A`. El `LD` sale de la propia
cadena de `aristas_nuevas`, nunca se teclea.

| # | operacion | par (resuelto) | LD de la ida | LD de la vuelta | filas de ficha |
|---:|---|---|---|---|---|
| 1 | OP-E-04 | sistema_gates_go_kill <-> portfolio_management | LD-40 | LD-48 | DOS filas (indices 1 y 4) |
| 2 | OP-E-04 | sistema_gates_go_kill <-> gestion_portafolio_foco | LD-45 | LD-53 | DOS filas (indices 3 y 7) |
| 3 | OP-E-05 | sistema_gates_go_kill <-> gestion_portafolio_formal | LD-41 | LD-41 | UNA fila (indices 0 y 0) |
| 4 | OP-E-05 | sistema_gates_go_kill <-> gestion_portafolio_dos_niveles | LD-43 | LD-43 | UNA fila (indices 1 y 1) |

**PARES CON LAS DOS DIRECCIONES: 4. ARISTAS QUE ESO SUPONE: 8.** Desglose por
operacion, tallado de la misma salida: **`OP-E-04`: 2 pares. `OP-E-05`: 2 pares.**
Contexto de la misma corrida, para que las cifras no queden sueltas: **6 fichas
de 71 tienen `aristas_nuevas` no vacio; 20 filas de ficha en todo el plan; 18
direcciones distintas tras resolver.**

### 17.c. LAS DOS CIFRAS, UNA POR FILA, CADA UNA CON SU AUTOR Y SU FICHERO

| cifra | unidad | que cuenta | autor | corte | fichero |
|---:|---|---|---|---|---|
| **2** | **pares** (y **4** aristas) | los enlaces mutuos escritos en UNA sola fila, que es lo que la frase vio | plan, `00_INDICE` | sin fecha escrita en la linea | `docs/plan/00_INDICE.md:478` |
| **4** | **pares** (y **8** aristas) | todos los pares con las dos direcciones en su propio `aristas_nuevas`, tras resolver por alias | ejecutor, vuelta 143 | 2 sep 2026 | `docs/loop/SALIDA_V143_1B_PARES_DOBLE_DIRECCION.txt` |
| **4** | **pares** (y **8** aristas) | la misma cuenta, medida con parser propio del auditor | auditor, acta 142, adjudicacion 3.4 | acta de la vuelta 142 | `docs/loop/ACTA_AUDITOR.md`, acta 142 |

**COTEJO CONTRA LA MEDICION DE CONTRASTE DEL AUDITOR, QUE ES LO QUE `EJECUTOR.md`
2 pide: CERO DISCREPANCIAS.** El acta 142 da **cuatro pares y ocho aristas**, dos
de `OP-E-05` (`sgk` con `gestion_portafolio_formal` por LD-41 y `sgk` con
`gestion_portafolio_dos_niveles` por LD-43) y dos de `OP-E-04` (`sgk` con
`portfolio_management` por LD-40 y LD-48, `sgk` con `gestion_portafolio_foco` por
LD-45 y LD-53). **Mi instrumento da exactamente esos cuatro, con esos ocho LD y
esas dos operaciones. No hay discrepancia que declarar.**

### 17.d. POR QUE LA FRASE VIEJA NO ERA MENTIRA CUANDO SE ESCRIBIO

**LA DIFERENCIA ESTA EN LA FORMA, NO EN LA INTENCION, Y EL INSTRUMENTO LA MIDE.**
Los dos pares de `OP-E-05` llevan sus dos direcciones **en UNA sola fila** de
`aristas_nuevas` (*"A -> B Y B -> A, por LD-41"*): se ven leyendo la ficha. Los dos
pares de `OP-E-04` llevan sus dos direcciones **en DOS filas distintas**
(indices 1 y 4; indices 3 y 7) **y con nodos escritos que hoy son alias**
(`requisitos_gates_con_dientes` y `gates_go_kill_decision_points` resuelven los dos
a `sistema_gates_go_kill`): **no se ven leyendo la ficha, solo se ven tras
resolver.** La frase del `00_INDICE` miraba la forma que se ve.

### 17.e. LA REGLA QUE QUEDA

**UNA CUENTA DE "ARISTAS QUE VAN EN LAS DOS DIRECCIONES" SE HACE SOBRE LAS
DIRECCIONES RESUELTAS, NUNCA SOBRE LAS CADENAS ESCRITAS**, porque una fusion puede
juntar las dos direcciones de un par sin que ninguna fila lo diga (que es
exactamente el criterio de la **CORRECCION 14**, el par colapsado). Y la
consecuencia practica, que es la que el hueco de orden 1 ya pedia con sus palabras
(*"LA GUARDA TIENE QUE LLEVAR LA EXCEPCION ESCRITA"*): **la excepcion del 9.22 no
cubre dos pares, cubre cuatro**, y la ficha de `OP-E-04` los nombra desde la
vuelta 142 (TAREA 3.a, commiteada en la vuelta 143).

## CORRECCION 18. **LA TERCERA UNIDAD QUE NADIE NOMBRA: ENTRADA, FILA DE FICHA Y DIRECCION SON TRES COSAS DISTINTAS**

**POR ADICION.** Escrita en la vuelta 143, TAREA 1.c, por encargo del acta 142,
seccion 2 (la relectura ciega). Corte de todas las cifras: **2 sep 2026**.

### 18.a. POR QUE NACE, Y NO ES UN ERROR DE NADIE

El auditor de la vuelta 142 releyo a ciegas el desglose de direcciones con
instrumento propio y **coincidio al digito en la unidad adjudicada**: 17
direcciones sobre las cinco remitidas y 18 sobre las seis. **Donde no coincidio
fue en "filas": conto 16 donde el ejecutor conto 18.** Mordido hasta el fondo, no
habia cifra mal en ningun lado: **contaban unidades distintas**. El auditor contaba
**entradas del array JSON**; el ejecutor y `tallar_estado_de_fase.py` cuentan
**filas de ficha**. La tercera unidad existia y **ningun documento la nombraba**.

### 18.b. LAS TRES UNIDADES, DEFINIDAS DE UNA VEZ

| unidad | que es | quien la usa |
|---|---|---|
| **ENTRADA de `aristas_nuevas`** | un elemento del array JSON de la ficha | el parser ciego del auditor de la vuelta 142; **ningun documento del plan la nombraba antes de esta correccion** |
| **FILA DE FICHA** | un par `A -> B` tal como esta **ESCRITO**, ANTES de resolver alias | `pares_de_aristas()`; es lo que `tallar_estado_de_fase.py` llama **fila** y publica en su celda desde la vuelta 141, TAREA 2.c |
| **DIRECCION** | el par `(A, B)` **DESPUES** de resolver por alias (`P.1`) | la unidad **adjudicada** por el acta 140, adjudicacion 3.4; es la que el grafo guarda y la que la vara mide |

### 18.c. LOS TRES TOTALES, MEDIDOS HOY Y TALLADOS DE UN INSTRUMENTO

**Comando corrido en esta vuelta:**
`python scripts/loop/vuelta143_1c_tres_unidades.py --fase 06_MESAS`.
Salida entera en `docs/loop/SALIDA_V143_1C_TRES_UNIDADES.txt`.

| operacion | remitida por | entradas | filas | direcciones |
|---|---|---:|---:|---:|
| OP-E-04 | docs/plan/04_ENLACES.md:1452 | 9 | 9 | 8 |
| OP-E-05 | docs/plan/04_ENLACES.md:1453 | 2 | 4 | 4 |
| OP-M-01-ESLABONES | docs/plan/04_ENLACES.md:1454 | 2 | 2 | 2 |
| OP-M-01-SEXTO | docs/plan/04_ENLACES.md:1455 | 1 | 1 | 1 |
| OP-M-03-ENLACES | docs/plan/04_ENLACES.md:1451 | 2 | 2 | 2 |
| OP-M-05-APERTURA | docs/plan/00_INDICE.md:261 | 1 | 2 | 1 |

**UNIVERSO 1, LAS CINCO REMITIDAS por `docs/plan/04_ENLACES.md` (el que el acta
140 conto y el que el encargo pide): ENTRADAS 16, FILAS 18, DIRECCIONES 17.**

**UNIVERSO 2, LAS SEIS del catalogo con direcciones (anade `OP-M-05-APERTURA`):
ENTRADAS 17, FILAS 20, DIRECCIONES 18.**

**EL 16 DEL AUDITOR ERA CORRECTO EN SU UNIDAD:** es exactamente el total de
ENTRADAS sobre las cinco. **El 18 del ejecutor tambien:** es el total de FILAS
sobre las cinco. **No hay cifra que corregir en ninguno de los dos; hay una unidad
que faltaba nombrar.**

### 18.d. EL EJEMPLAR DE CADA SALTO

**`OP-E-05`: 2 entradas, 4 filas, 4 direcciones.** El salto es de entrada a fila:
cada una de sus dos entradas escribe **las dos direcciones dentro de la misma
cadena** (*"requisitos_gates_con_dientes -> gestion_portafolio_formal Y
gestion_portafolio_formal -> requisitos_gates_con_dientes, por LD-41"*). De fila a
direccion **no hay salto**: las cuatro filas resuelven a cuatro direcciones
distintas.

**`OP-M-05-APERTURA`: 1 entrada, 2 filas, 1 direccion.** Aqui saltan las dos: su
unica entrada escribe la arista **y su forma resuelta en la misma cadena**
(*"introduccion_validacion_clientes -> customer_validation_sell_phase, que tras la
fusion resuelve a customer_validation -> customer_validation_sell_phase"*), asi que
el parser saca **2 filas**; y las dos filas resuelven a **la misma direccion**,
`customer_validation -> customer_validation_sell_phase`, asi que colapsan en **1**.

### 18.e. LA REGLA QUE QUEDA

**UNA CIFRA DE ESTA FAMILIA SE PUBLICA SIEMPRE CON SU UNIDAD NOMBRADA.** No hay
cifra por defecto: entrada, fila y direccion son tres respuestas legitimas a tres
preguntas distintas, y la que el acta 140 adjudico como unidad **publicada** es la
**direccion**.

**Y "FILAS DE FICHA" NUNCA SIGNIFICA FILAS DEL ARRAY JSON.** Esa es la convencion
de la casa desde la vuelta 141, la sostiene `tallar_estado_de_fase.py` en su codigo
y en su celda, y quien quiera contar elementos del array **dice ENTRADAS**. Es la
misma doctrina que la **CORRECCION 15** fijo para el universo (*"un total lleva su
universo al lado"*), aplicada ahora a la unidad.

---

## CORRECCION 19. **LA EXCEPCION DEL 9.22 SE ESCRIBE CON FORMULA CANONICA, Y LA VENTANA TENIA DOS AGUJEROS**

**Adjudicacion 3.1 del acta de la vuelta 143. Escrita en la vuelta 144, TAREA 1.b,
POR ADICION: no se borra una letra de la CORRECCION 14, que sigue entera y
vigente.** Corte de todas las cifras de esta correccion: **2 sep 2026**, medidas en
la vuelta 144 con instrumento propio del ejecutor
(`scripts/loop/vuelta144_1b_medir_ventana.py`, salida en
`docs/loop/SALIDA_V144_1B_VENTANA_MEDIDA.txt`), **no copiadas de la medicion del
auditor**. La medicion de contraste del auditor va citada al lado en cada punto.

### 19.a. LO QUE HABIA, Y NO SE BORRA

La vuelta 143 (TAREA 2.a) enseno a `scripts/loop/tallar_estado_de_fase.py` a leer
la excepcion del banco **9.22** que la propia ficha de `OP-E-04` escribe en su
`verificacion 5`. La decision de lectura, escrita entonces y **que sigue en el
codigo sin tocarse**, fue: *"LOS PARES SE PARSEAN DE LA VENTANA QUE LA PROPIA FICHA
DELIMITA CON SUS PALABRAS"*, con la ventana yendo del literal `DOBLE LINEA` al
literal `y ESCALERA`. **El criterio es correcto y queda adjudicado** (acta 143,
3.1): restringir la ventana era necesario, porque la misma frase nombra **LD-42
como ESCALERA**, o sea como el par que la excepcion **expresamente NO cubre**, y
leer la linea entera lo colaria dentro.

**LO QUE SE CORRIGE NO ES EL CRITERIO, ES LA IMPLEMENTACION.**

### 19.b. AGUJERO 1: LA VENTANA SE ENSANCHA EN SILENCIO SI FALTA EL CIERRE

El codigo de la 143 dice, en `pares_exceptuados_de`:

```
fin = bajo.find(MARCA_CIERRA_EXCEPCION, ini)
ventana = linea[ini:fin] if fin > ini else linea[ini:]
```

Si el literal de cierre no esta, `find` devuelve **-1** y la ventana **se lee hasta
el final de la linea sin decir nada**. Habia fallo ruidoso para la apertura ausente
y para el caso de cero pares; **para el cierre ausente no lo habia**.

**MEDIDO POR EL EJECUTOR EN LA VUELTA 144, EN MEMORIA Y CON CERO ESCRITURAS:**

| que se mide | ficha tal cual | quitado el literal de cierre |
|---|---:|---:|
| pares exceptuados que salen | **4** | **5** |
| fallos declarados | **0** | **0** |

**EL PAR QUE ENTRA DE MAS ES
`revision_portafolio_periodica <-> sistema_gates_go_kill`**, que es **exactamente
el par que la excepcion niega por escrito**: el LD-42 que la propia formula de la
ficha adjudica como **ESCALERA**. Y entra **con cero fallos declarados**, o sea
**hacia el lado permisivo y en silencio**, que es lo contrario de banco 9.

**CONTRASTE:** el auditor midio lo mismo por mutacion propia (acta 143, seccion 2 y
caida 4.2) y nombro el mismo par. **CERO DISCREPANCIAS.**

### 19.c. AGUJERO 2: EL ANCLA ES LA PRIMERA OCURRENCIA, Y NO ES LA FORMULA

`bajo.find(MARCA_ABRE_EXCEPCION)` toma **la primera** ocurrencia del literal.

**MEDIDO POR EL EJECUTOR CON `re.finditer` SOBRE ESA MISMA LINEA** (verificacion 5,
**1.950 caracteres**):

- el literal `doble linea` aparece **2 veces**, en las posiciones **381** y **859**;
- **el codigo de hoy ancla en 381**, que cae dentro de la prosa del punto **(1)**
  (*"...NO para los enlaces de doble linea, por el banco 9.22..."*), **no en 859**,
  que es donde vive la formula de adjudicacion (*"adjudico DOBLE LINEA los pares
  de..."*);
- la ventana real de hoy es **`[381, 952)`, 571 caracteres**; el tramo **tragado de
  mas** va de **381 a 859**, o sea **478 caracteres**, y se come el punto (1)
  entero, la cita a la **CORRECCION 14** y una ruta de fichero.

**EL COMENTARIO DEL CODIGO DE LA 143 Y EL DISCUTIBLE 1 DE SU REPORTE DESCRIBEN UNA
VENTANA QUE EL CODIGO NO LEE.**

**POR QUE HOY NO MUEVE UNA CIFRA, MEDIDO Y NO SUPUESTO:** dentro de esos **478
caracteres** hay **cero LD** y **cero flechas** (`PATRON_LD` y `PATRON_ARISTA`
corridos sobre el tramo), asi que el conjunto de LDs de la ventana real
(`35, 40, 45, 48, 49, 51, 53`) y el de la ventana que el comentario describe son
**el mismo**. **Hoy sale bien por suerte, no por construccion**: el dia que una
excepcion cite un `LD-nn` en su encabezado, se cuela sola.

**CONTRASTE:** el auditor midio las mismas dos posiciones, 381 y 859 (acta 143,
caida 4.3). **CERO DISCREPANCIAS.**

### 19.d. LA FORMULA CANONICA QUE QUEDA, Y QUE LA TAREA 2.a IMPLEMENTA

**LA VARA DEJA DE DEPENDER DE LA REDACCION DE UNA FICHA.** No es doctrina nueva:
es el hueco de orden 1 del `00_INDICE:482` (*"LA GUARDA TIENE QUE LLEVAR LA
EXCEPCION ESCRITA"*) llevado a su consecuencia, mas **banco 9** (fallar ruidoso).

**LA FORMULA, en cuatro renglones:**

1. **LA EXCEPCION DECLARA SUS PARES ENTRE DOS MARCAS INEQUIVOCAS**, elegidas para
   que **no puedan aparecer en prosa**: `PARES EXCEPTUADOS:` abre y
   `FIN PARES EXCEPTUADOS` cierra. **Se justifica la eleccion:** las dos llevan la
   palabra `EXCEPTUADOS` en mayuscula pegada a un dos puntos o a un `FIN`, forma
   que ninguna explicacion en castellano corriente produce; y a diferencia de
   `doble linea` o `y escalera`, **no son terminos del vocabulario del 9.22**, que
   es justo lo que hacia que los viejos aparecieran tambien en la explicacion.
2. **SI LA FICHA DISPARA LA EXCEPCION Y NO TRAE LA FORMULA ENTERA, ES ROJO
   NOMBRANDOLA, y el conjunto sale VACIO.** Los dos extremos con su fallo: falta la
   apertura, **ROJO**; falta el cierre, **ROJO**. **NUNCA se lee hasta el final de
   la linea por defecto**: el `else linea[ini:]` muere.
3. **EL ANCLA ES UNICA O ES ROJO.** Si la marca de apertura aparece **mas de una
   vez** en la linea, es **ROJO por ambigua**, no se toma la primera.
4. **LO VIEJO NO SE BORRA:** la verificacion 5 de `OP-E-04` se reescribe **por
   adicion**, sin tocar una letra de lo que ya dice, con la guarda semantica de
   siempre (fichas antes y despues, ficha que cambia, campo que cambia, **prefijo
   identico**), y **los cuatro pares exceptuados tienen que seguir siendo los
   mismos cuatro**.

### 19.e. LA REGLA QUE QUEDA

**UNA VENTANA DE LECTURA SE DELIMITA CON MARCAS QUE NO PUEDAN SALIR EN LA PROSA QUE
LA RODEA, Y SUS DOS EXTREMOS FALLAN RUIDOSO.** Un extremo que, al faltar, ensancha
la lectura en vez de pararla, es un modo de fallo **silencioso y permisivo**: la
guarda sigue en verde mientras deja entrar justo lo que niega. Es la misma especie
que la **CORRECCION 16** registra para el superviviente divergente (una operacion
hecha al reves que pasaba por cumplida) y la misma que el banco 9 llama por su
nombre: **fallar ruidoso, no mentir calladito.**

---

## CORRECCION 20. **`OP-M-04` NO ESPERA A NADIE, Y LA VARA DE MESA MIDE SOLO POR HIJAS**

**Adjudicacion 3.9 del acta de la vuelta 143. Escrita en la vuelta 144, TAREA 1.c,
POR ADICION.** Corte de todas las cifras: **2 sep 2026**, medidas en la vuelta 144
con instrumento propio del ejecutor (`scripts/loop/vuelta144_1c_medir_opm04.py`,
salida en `docs/loop/SALIDA_V144_1C_OPM04_MEDIDA.txt`).

### 20.a. LA PREMISA VIEJA, QUE NO SE BORRA, Y POR QUE ERA FALSA

El reporte de la vuelta 143 escribio, en su PREGUNTA 2, que `OP-M-04` *"queda en NO
COMPUTABLE esperando a `OP-U-01`"*. **La conclusion (que la fase 06 no cierra sin
ella) era correcta; la premisa (que espera a alguien) no lo era**, y el texto viejo
se deja escrito porque una correccion que tapa lo que corrige no se puede auditar
(`EJECUTOR.md` 8).

### 20.b. LO MEDIDO, CON INSTRUMENTO PROPIO Y CERO ESCRITURAS

- **`depende_de` de `OP-M-04` es `[]`.** Vacio. **No espera a nadie.**
- **`bloquea_a` de `OP-M-04` es `['OP-S-12', 'OP-U-01']`**, o sea que **las bloquea,
  no depende de ellas**. Comprobado ademas por el otro lado: **`OP-M-04` no aparece
  en el `depende_de` de ninguna de las dos** (lista de coincidencias: vacia). Y
  **ninguna de las dos es de la fase 06**: `OP-S-12` es de `05_SANEO` y `OP-U-01` de
  `03_FUSIONES`.
- **Sus cuatro nodos siguen VIVOS y SIN FUNDIR en el grafo de hoy: 4 de 4 y 4 de
  4.** `formalize_advisory_board`, `formalizar_junta_asesora`,
  `identificar_junta_asesores` e `identificar_consejo_asesores` existen los cuatro,
  ninguno esta deprecado, y **los cuatro resuelven a si mismos** con el resolutor
  de alias puesto (`P.1`). **La operacion esta entera por hacer y nada la bloquea.**

### 20.c. LA CAUSA REAL: LA VARA DE MESA NUNCA MIRA LOS CAMPOS PROPIOS DE LA FICHA

**Medido leyendo el CODIGO FUENTE, no de memoria**: el arnes recorta con `ast` el
bucle de las mesas dentro de `medir()` (`tallar_estado_de_fase.py`) y busca en el
las cadenas de los campos propios. Resultado:

| campo propio de la ficha | lo lee la rama `es_mesa`? |
|---|---|
| `nodos` | **NO** |
| `eliminar` | **NO** |
| `superviviente` | **NO** |
| `aristas_nuevas` | **NO** |
| `preservar` | **NO** |

**Los campos de ficha que si lee son `bloquea_a`, `fase`, `estado`, `tipo` y `a`**
(el de la tabla de remision). O sea: **la vara de MESA mide una mesa SOLO por sus
hijas** (`bloquea_a` union remision).

**Y `OP-M-04` ES LA UNICA MESA QUE LLEVA SU PROPIA CIRUGIA DENTRO:** `nodos` con
cuatro, `eliminar` con dos, un `superviviente` doble y un giro en `aristas_nuevas`.
**Sus hijas no ejecutan su cirugia; la ejecuta ella.** Como sus dos hijas estan
fuera del catalogo de la fase 06, la celda de hoy sale, literal:

```
vara      : MESA
cumplido  : None
razon     : NINGUNA de sus hijas esta en el catalogo de esta fase; nomina de 2
            (bloquea_a 2, remision 0, union 2); nomina: OP-S-12 (05_SANEO),
            OP-U-01 (03_FUSIONES)
```

y cae en **SIN VARA ESCRITA**, que es **el propio instrumento diciendo en voz alta
que le falta una regla**, exactamente como su docstring promete. No es una averia
del instrumento: es su fallo ruidoso funcionando.

### 20.d. LA REGLA QUE QUEDA

**LA MESA QUE DECLARA SU FIGURA EN SU PROPIO `tipo` SE MIDE CON LAS VARAS DE SU
FIGURA, SOBRE SUS PROPIOS CAMPOS.**

**NO ES DOCTRINA NUEVA, Y SE DICE POR QUE.** El `tipo` de `OP-M-04` dice literal
**"MESA ADJUDICADA: DOS FUSIONES MAS UN ENLACE"**: **la propia ficha nombra su
figura**, igual que las seis frases literales que la vuelta 141 hizo citar en el
codigo y la excepcion que la 143 hizo leer de la ficha. **Y las dos varas que esa
figura pide ya estan escritas y en uso en este mismo fichero**: la de **FUSION**
(superviviente vivo, absorbidos deprecados y en `ids_alias`) y la de **ENLACE**
(direcciones con la IDA presente y el regimen de vuelta). No se copian: **se
reusan**.

**LA MESA QUE NO DECLARA SU FIGURA SE COMPORTA EXACTAMENTE COMO HOY.** La extension
es un caso mas y **solo uno**, disparado por una frase literal de la ficha citada en
el codigo; ninguna otra fila de la tabla de la fase 06 puede moverse, y si se mueve,
se trae en vez de ajustarse.


---

## CORRECCION 21. **LA ANCLA UNICA NO ERA SOLO DE LA FORMULA DE LA EXCEPCION**

**Adjudicacion 4.3 del acta de la vuelta 144** (caida de la casa). Registrada por
adicion en la vuelta 145, TAREA 1.b; implementada en la TAREA 2.a. Corte de todas
las cifras de esta entrada: **2 sep 2026**. **TODO LO QUE SIGUE ESTA MEDIDO POR EL
EJECUTOR CON INSTRUMENTO PROPIO**, `scripts/loop/vuelta145_1b_censo_de_marcas.py`,
salida en [`loop/SALIDA_V145_1B_CENSO_DE_MARCAS.txt`](../loop/SALIDA_V145_1B_CENSO_DE_MARCAS.txt);
no se copia ninguna cifra del acta.

### 21.a. EL DEFECTO

`quitar_bloques_cubiertos()` de `scripts/loop/verificar_cifras_del_reporte.py`
resolvia cada uno de sus **TRES** pares de marcas con `texto.find(MARCA)`, y `find`
**devuelve la PRIMERA ocurrencia**. Con la marca repetida, el recorte iba **de la
primera apertura al primer cierre** y el segundo bloque **se parseaba entero, en
silencio y con VERDE EXIT 0**.

### 21.b. CUANTAS VECES APARECE CADA MARCA, MEDIDO

**Sujeto: el `docs/loop/REPORTE.md` de la vuelta 144 YA COMMITEADO**, leido por ref
de git (`b7f07648:docs/loop/REPORTE.md`), nunca del arbol vivo. **40.541 caracteres,
639 lineas.**

| marca | veces | posiciones (linea, offset) |
|---|---:|---|
| apertura de CABECERA TALLADA | 1 | 22 (1038) |
| cierre de CABECERA TALLADA | 1 | 34 (3630) |
| apertura de COMMITS TALLADOS | 1 | 43 (3849) |
| cierre de COMMITS TALLADOS | 1 | 66 (5739) |
| apertura de COBERTURA DE LA GUARDA | **2** | **274 (17651), 632 (40326)** |
| cierre de COBERTURA DE LA GUARDA | **2** | **278 (18315), 638 (40505)** |

### 21.c. QUE RECORTA HOY Y QUE SE QUEDA FUERA

| par | recorta | queda fuera |
|---|---|---|
| COBERTURA | lineas **274 a 278**, 699 caracteres | **lineas 632 a 638, 214 caracteres, QUE SI SE PARSEAN** |
| COMMITS | lineas 43 a 66, 1.919 caracteres | nada |
| CABECERA | lineas 22 a 34, 2.621 caracteres | nada |

**El bloque que la guarda protege es el que el ORDEN DEL FICHERO elige; el que el
reporte designa** (*"pegada abajo tras la segunda corrida"*, dicho en su seccion 8)
**es el segundo, y ese no se protegia.**

### 21.d. QUE PASA CON LA CIFRA CUANDO LA LINEA REAL SE PEGA EN EL SEGUNDO BLOQUE

Pegada la linea real de cobertura que la propia guarda produce sobre ese sujeto,
**dentro del SEGUNDO bloque**: la guarda pasa de **VERDE EXIT 0** a **ROJO EXIT 1**,
y las unidades vistas fuera del vocabulario suben de **29 a 34**. Las cinco que
entran son las del propio bloque pegado: `cifras`, `cotejadas`, `exentas`,
`palabra`, `viven`.

### 21.e. CERO DISCREPANCIAS CON EL AUDITOR

Mi medicion coincide con la del acta 144 en los seis numeros que el acta publica:
lineas **274 y 278**, lineas **632 y 638**, y **29 a 34**. **No hay nada que
declarar como discrepante en esta correccion.**

### 21.f. LA REGLA QUE QUEDA

**SI CUALQUIERA DE LAS SEIS MARCAS DE BLOQUE APARECE MAS DE UNA VEZ, ES ROJO POR
AMBIGUA**, nombrando la marca y **todas** sus posiciones. **No se toma la primera.**
Es la misma regla `(iii)` que la TAREA 2.a de la vuelta 144 escribio para la formula
canonica de la excepcion, **el ancla unica**, que la 2.d de esa misma vuelta no
heredo. Vale para **las tres parejas** porque el defecto es de `find` y no de un
bloque. Las otras tres reglas de delimitador **no cambian**.

**Y LA REGLA DE ESCRITURA QUE LA ACOMPANA:** la pareja de marcas aparece
**exactamente una vez** en el reporte; quien necesite citar el mecanismo en la
prosa lo cita **con otro literal**, no con la marca de verdad.

**MUTACION:** `scripts/loop/vuelta145_2a_mutacion_ancla_unica.py`,
[`loop/SALIDA_V145_2A_MUTACION_ANCLA_UNICA.txt`](../loop/SALIDA_V145_2A_MUTACION_ANCLA_UNICA.txt),
**4 de 4**.

---

## CORRECCION 22. **UNA MUTACION DE LA BATERIA LLEVA SUJETO CONGELADO O NO ENTRA**

**Adjudicaciones 4.4 a 4.6 del acta de la vuelta 144** (las tres de la casa, **UNA
SOLA ENFERMEDAD: EL SUJETO VIVO**). Registrada por adicion en la vuelta 145, TAREA
1.c; implementada en la TAREA 2.b. Corte: **2 sep 2026**. Medido por el ejecutor
corriendo cada arnes **sobre el HEAD de apertura y con el arbol limpio**.

### 22.a. CUALES ARNESES VIVOS TOMAN SUJETO VIVO, Y SU VEREDICTO DE HOY

| arnes | de que toma su sujeto | veredicto HOY, arbol limpio | por que |
|---|---|---|---|
| `vuelta144_2d_mutacion_cobertura.py` | `docs/loop/REPORTE.md` **VIVO**, y le agrega SUS PROPIOS delimitadores | **ROJO, 1 de 3** | en cuanto el reporte trae ya un par de marcas, el par que el arnes agrega deja de ser el unico: **(B)** mide sobre el bloque equivocado y **(D)** no puede levantar `ValueError` |
| `vuelta144_3b_mutacion_negativa.py` | el **grafo de hoy**, o sea el mundo DESPUES de su propia fusion | **ROJO, 1 de 3** | su contraprueba **(C)** pide que el sellador salga VERDE y el sellador contesta *"el nodo `formalize_advisory_board` YA esta deprecado"*: **la fusion que sella ya corrio y ese mundo no existe** |
| `vuelta144_2a_guarda_semantica.py` | **WORK contra UN solo ref** (`REF = sys.argv[1] ... else "HEAD"`) | **ROJO** | *"cambian 0 fichas, se esperaba 1"* |
| `vuelta144_3b_guarda_semantica.py` | **WORK contra UN solo ref**, igual | **ROJO** | *"cambian 0 fichas, se esperaba 1"* |

**Y AQUI VA MI UNICA DISCREPANCIA CON EL ACTA 144, DECLARADA EN VEZ DE COPIADA.**
El acta dice que `vuelta144_3b_guarda_semantica.py` *"sigue verde SOLO POR HABER
SIDO LA ULTIMA"*. **Medido hoy sobre el arbol limpio de la apertura, las DOS salen
ROJO, y con el mismo fallo.** La causa es la misma que el acta diagnostica y el
diagnostico **no cambia**: con el arbol limpio `WORK` **es** `HEAD`, asi que no
cambia ninguna ficha y las dos caen. La de la 3.b solo puede salir verde con el
cambio **sin commitear**, que es exactamente lo que esta correccion viene a quitar.

### 22.b. LA BATERIA ENTERA, ANTES

`python scripts/loop/verificar_mutaciones_viejas.py` sobre el HEAD de apertura,
[`loop/SALIDA_V145_1C_VIEJAS_ANTES.txt`](../loop/SALIDA_V145_1C_VIEJAS_ANTES.txt):
**13 mutaciones, ANCLA PERDIDA 0, NO REPRODUCIBLE 0, NO MORDIO 1**
(`vuelta144_2d_mutacion_cobertura.py`), **CASO DECLARADO 2**. **ROJO EXIT 1.**

### 22.c. EL PATRON DE LA CASA QUE YA RESUELVE ESTO

`docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md` (**banco 9.10**), nacido en la vuelta
138 por la misma enfermedad: tres mutaciones ancladas a un literal de
`docs/loop/REPORTE.md`, que se sobreescribe cada vuelta. El sujeto se **congela**, se
**commitea** y las mutaciones lo **cotejan contra el blob de su acta en cada
corrida**. Medido hoy: ese fichero trae **0** ocurrencias de las seis marcas de
bloque, que es justo lo que un sujeto de este caso necesita.

**LA VARIANTE QUE LA VUELTA 145 ANADE, Y SE DECLARA:** cuando el sujeto es un nodo
del catalogo o `docs/plan/OPERACIONES.jsonl`, **no se copia al repositorio: se lee
de un ref de git**. Una copia commiteada de un nodo seria un **segundo nodo con el
mismo id**, que es la clase de duplicado que esta campana persigue. **Git ya es el
congelador y el commit citado es el ancla**
(`scripts/loop/vuelta145_2b_prestado_congelado.py`).

### 22.d. LA REGLA QUE QUEDA, Y CORRIGE LA QUE EL ACTA 144 ESCRIBIO CORTA

El texto viejo, **que no se borra**, decia: *"UNA MUTACION ENTRA EN ESTA BATERIA EN
LA VUELTA SIGUIENTE A LA QUE NACE, NO MAS TARDE."* Le faltaba la mitad:

**UNA MUTACION ENTRA EN `VIEJAS` EN LA VUELTA SIGUIENTE A LA QUE NACE, Y SOLO SI SU
SUJETO ESTA CONGELADO.** La que no pueda tenerlo entra como **CASO DECLARADO**, con
su **exit esperado** y su **motivo escrito en el propio fichero**, como ya hacen
`vuelta135_2e_mutacion_3.py` y `vuelta140_2a_mutaciones.py`.

**POR QUE LA MITAD QUE FALTABA IMPORTA:** sin ella la regla mete en una bateria
permanente arneses que **no pueden ser permanentes**, y el verde de una vuelta **no
sobrevive a la vuelta**. Es lo contrario de fallar ruidoso: es envejecer callado.

### 22.e. QUE SE HIZO CON CADA UNO, Y LA ELECCION JUSTIFICADA MEDIDA

| arnes | salida elegida | medido |
|---|---|---|
| `vuelta144_2d_mutacion_cobertura.py` | **sujeto congelado commiteado**, elegido por computo entre candidatos con la condicion *cero marcas de COBERTURA y como mucho una de cada otra* | vuelve a **3 de 3** |
| `vuelta144_3b_mutacion_negativa.py` | **pre-estado congelado por ref**, con el ref COMPUTADO (`5fff85f7`, padre del `c72ce2c0` que deprecio a los dos absorbidos) | vuelve a **3 de 3** |
| `vuelta144_2a_guarda_semantica.py` | **dos refs**, invocacion canonica `c5a389dd^ c5a389dd` escrita en el docstring | **VERDE** |
| `vuelta144_3b_guarda_semantica.py` | **dos refs**, invocacion canonica `c72ce2c0^ c72ce2c0` escrita en el docstring | **VERDE** |

**SE ELIGIO CONGELAR Y NO DECLARAR EN LOS DOS PRIMEROS, Y EL MOTIVO ES MEDIDO:** un
CASO DECLARADO deja el arnes **excusado y sin morder**; congelado vuelve a **3 de 3**
en los dos. Un arnes congelado que ya no muerde seria peor que uno rojo, asi que
**se comprobo que siguen mordiendo** relajando la guarda que cada uno prueba:
`scripts/loop/vuelta145_2b_mutacion_arneses.py`,
[`loop/SALIDA_V145_2B_MUTACION_ARNESES.txt`](../loop/SALIDA_V145_2B_MUTACION_ARNESES.txt),
**2 de 2**: cada uno **cae** con la guarda relajada y **vuelve a verde** con la
guarda entera.

**LA BATERIA, DESPUES:** de **13 a 19** entradas, **ANCLA PERDIDA 0, NO MORDIO 0, NO
REPRODUCIBLE 0**, **VERDE EXIT 0**
([`loop/SALIDA_V145_2_VIEJAS_TRAS_TAREA2.txt`](../loop/SALIDA_V145_2_VIEJAS_TRAS_TAREA2.txt)).

## CORRECCION 23. **UNA AFIRMACION DE AUSENCIA SE PRUEBA POR BARRIDO EXHAUSTIVO COMPUTADO O NO SE PUBLICA**

**Adjudicacion 3.10 del acta de la vuelta 145** (el discutible 10, EN CONTRA) **y su
caida de la casa 4.2** (*"la regla 9 de `EJECUTOR.md` no tiene guarda que la haga
morder"*). Registrada por adicion en la vuelta 146, TAREA 1.b; la guarda que la hace
morder se construye en la TAREA 2 de esta misma vuelta. Corte: **2 sep 2026**.
**TODAS LAS CIFRAS DE ESTA ENTRADA SON MEDICION MIA DE HOY, no copia del acta**, y
donde discrepe de ella lo digo.

### 23.a. LA AFIRMACION QUE CAYO, CITADA DE SU FICHERO CONGELADO

El reporte de la vuelta 145, congelado en `a9b638ba:docs/loop/REPORTE.md`, publica en
su 3.c, **verbatim**: *"no existe en el repositorio ninguna lista canonica de libros
con sus alias de escritura"*, y de ahi saca **`PRERREQUISITO CUMPLIDO: NO`** y el
bloqueo nombrado de la fase 07. El metodo, escrito en la propia salida: *"candidatos
mirados: `dataset/metadata/libros_canonicos.json`,
`dataset/metadata/fuentes_canonicas.json`, `docs/plan/LIBROS_CANONICOS.md`"*,
*"hallados: NINGUNO"*. **Tres rutas tecleadas a mano, cero busqueda por contenido.**

### 23.b. LO QUE MIDO YO HOY, Y CUADRA CON EL ACTA EN LAS CUATRO

| lo que se afirma | mi medicion de hoy | veredicto |
|---|---|---|
| los tres nombres candidatos no existen | `git ls-files --error-unmatch` sobre los tres: **los tres NO EXISTEN** en el indice | **CIERTO, y es lo unico cierto de la 3.c** |
| existe una lista canonica de libros con sus alias | `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`, **24.915 bytes, 143 lineas**, tabla `grafia / canonica propuesta / motivo / bolsa` que reduce **129 grafias** a **54 canonicas** | **LA LISTA EXISTE** |
| `OP-S-11` sigue sin hacerse | leida hoy su ficha de `docs/plan/OPERACIONES.jsonl`: **`estado: HECHA`**, **`fecha_corte: 2026-08-29`**, y `bloquea_a` nombra a `OP-A-01` y `OP-A-02` | **ESTA HECHA** |
| no hay contra que validar el campo | `python scripts/loop/verificar_fuente_canonico.py` corrido por mi: **VERDE EXIT 0**, *"los 3169 nodos vivos traen `fuente` PRESENTE y con al menos una declaracion, y todas sus declaraciones son canonicas de la tabla"* | **HAY, Y VALIDA VERDE** |

**CERO DISCREPANCIAS CON EL ACTA 145 EN ESTAS CUATRO.** El universo del barrido de
hoy: **15.088 ficheros** en `git ls-files`.

### 23.c. POR QUE EL METODO ES EL DEFECTO, Y NO LA MALA SUERTE

La lista **no aparecio con ninguno de los tres nombres porque no se llama asi**. Una
busqueda por NOMBRE contra tres candidatos tecleados **no puede** hallar un fichero
que se llama por su operacion duena; una busqueda POR CONTENIDO sobre el universo de
`git ls-files` **si**. Es exactamente lo que `EJECUTOR.md` 9 prohibe desde hace
vueltas (*"una busqueda negativa no se puede citar"*) y lo que el propio discutible 10
citaba mientras lo incumplia en la misma pagina.

**Y HAY UNA SEGUNDA MITAD DEL DEFECTO, QUE ES DE UNIDADES.** La 3.c apoyo su
conclusion en que `tallar_estado_de_fase.py` pone a `OP-S-11` **SIN VARA ESCRITA**.
Eso es CIERTO y **no significa lo que la 3.c le hizo decir**: esa columna mide
**destino contra el grafo**, y una operacion que no deja huella de fusion no puede
tener destino que medir. **Usar una columna de vara de grafo como veredicto de
ejecucion es la confusion que la adjudicacion 3.9 del acta 144 ya mandaba evitar** y
que la CORRECCION 18 llama por su nombre: dos unidades no comparten columna.

### 23.d. LA REGLA QUE QUEDA

**UNA AFIRMACION DE AUSENCIA (que algo NO EXISTE, que NO ESTA INSTALADO, que NO SE
HALLO) SE PUBLICA SOLO SI VIENE RESPALDADA POR UN BARRIDO EXHAUSTIVO COMPUTADO,
SELLADO EN UNA SALIDA, CON SU UNIVERSO Y SU CARDINAL PUBLICADOS.** Un barrido
exhaustivo es un recorrido del universo entero donde la cosa podria estar: para
ficheros, `git ls-files` **mas** una busqueda POR CONTENIDO, no solo por nombre. **Una
lista de rutas candidatas escritas a mano NO ES UN BARRIDO** y no respalda nada.

**LO QUE ESTA REGLA NO DICE, para que no se lea de mas:** no dice que la cosa exista
ni que no exista. Dice que **la afirmacion** tiene que estar respaldada. La guarda de
la TAREA 2 comprueba el respaldo, jamas el hecho.

### 23.e. EL APOYO POSITIVO QUE ESTABA INVERTIDO, MEDIDO POR MI

La 3.c dijo que la grafia vieja vive del lado deprecado *"o sea que nada la esta
normalizando"*. **Es al reves, y lo mido:** `verificar_fuente_canonico.py` **solo
obliga a los VIVOS**, asi que una grafia vieja que sobrevive **unicamente** entre
deprecados es la firma de una normalizacion **CONSUMADA**, no de una ausente. Medido
por mi con `scripts/loop/vuelta146_1c_cifras_ficha_op_a_01.py` sobre los dos refs
([`loop/SALIDA_V146_1C_CIFRAS_FICHA.txt`](../loop/SALIDA_V146_1C_CIFRAS_FICHA.txt)):
en el grafo del corte (`0e5e0c60`) Hugos y Horowitz tenian **2 grafias vivas cada
uno**; hoy tienen **1 y 1**, y las viejas quedan con **cero nodos vivos**.

## CORRECCION 24. **LAS SEIS CIFRAS DE LA FICHA DE `OP-A-01` CONTRA SU CORTE: TRES REPRODUCEN Y TRES NO, Y EL TEXTO DE LA FICHA NO SE TOCA**

**Adjudicacion 3.14 del acta de la vuelta 145**, que responde la PREGUNTA 1 del
reporte de la 145: *"ni se re-mide la ficha ni se deja muda"*. Registrada **POR
ADICION** en la vuelta 146, TAREA 1.c. **EL TEXTO DE `OP-A-01` NO SE TOCA**, por
`EJECUTOR.md` 8: una correccion que tapa lo que corrige no se puede auditar.

**EL SUJETO, ELEGIDO POR COMPUTO Y NO TECLEADO:** `0e5e0c60`, el ultimo commit que
toca `dataset/metadata/master_graph.json` **antes del 12 ago 2026**. Comprobado con
`git log --format='%H %ad' --date=short -- dataset/metadata/master_graph.json`: su
fecha es **2026-08-09** y el siguiente commit del fichero es del **2026-08-14**.
**Instrumento:** `scripts/loop/vuelta146_1c_cifras_ficha_op_a_01.py`, salida sellada
en [`loop/SALIDA_V146_1C_CIFRAS_FICHA.txt`](../loop/SALIDA_V146_1C_CIFRAS_FICHA.txt).

### 24.a. LAS SEIS, UNA A UNA, CON SU UNIDAD Y SU CORTE

| # | lo que la ficha dice (corte 11 ago 2026) | lo que mido sobre `0e5e0c60` | veredicto |
|---|---|---|---|
| 1 | *"3.521 nodos vivos"* | **3.521** nodos vivos | **REPRODUCE EXACTO** |
| 2 | *"67 con mas de un libro"* | **67** nodos vivos con mas de una declaracion en `fuente` | **REPRODUCE EXACTO** |
| 3 | *"70 declaraciones en segunda posicion o posterior"* | **74** declaraciones de indice mayor que cero, sobre nodos vivos | **NO REPRODUCE** |
| 4 | *"Hugos aparece con DOS grafias"* | **2** grafias distintas | **REPRODUCE EXACTO** |
| 5 | *"y Horowitz con TRES"* | **2** grafias distintas | **NO REPRODUCE: son DOS** |
| 6 | *"sin normalizar el recorte da 23 y 16 donde el canonico da 21 y 14"* | sobre el recorte (los 67): Hugos **21** sin normalizar y **20** solo canonica; Horowitz **11** y **6** | **NO REPRODUCE NINGUNO DE LOS CUATRO** |

**LA UNIDAD DE LA CIFRA 6 NO ESTA ESCRITA EN LA FICHA Y NO SE ADIVINA.** El
instrumento publica las CUATRO lecturas construibles (sobre todos los vivos y sobre
el recorte, sin normalizar y solo canonica) y **ninguna de las cuatro da 23, 16, 21 y
14 a la vez**. Es la caida 4.7 del acta 144 otra vez: una cifra sin unidad nombrada no
se puede cotejar. **Y NO PUEDO RE-CORRER SU INSTRUMENTO: no esta en `scripts/`.**

**UNA COINCIDENCIA QUE SI TRAIGO, PORQUE ES MEDIDA Y NO INTERPRETACION:** la
`evidencia` de la ficha dice *"los 21 de Hugos, verificados 21 de 21"*, y **21 es
exactamente lo que mi recorte da para Hugos SIN NORMALIZAR**. La ficha atribuye ese 21
al conteo CANONICO. **Lo dejo dicho y no lo resuelvo**: cual de las dos etiquetas
llevaba la nomina del auditor del 11 ago no se puede decidir sin su instrumento.

### 24.b. LO QUE NO ES UN ERROR DE NADIE, Y HAY QUE DECIRLO PARA QUE NO SE LEA MAL

Medido hoy sobre `WORK`: **3.169 vivos, 8 nodos con mas de un libro, 9 declaraciones
en segunda posicion o posterior**, contra **3.521 / 67 / 74** en el corte. **LA CAIDA
DE 67 A 8 ES OBRA DE LA CAMPANA, NO UN ERROR DE MEDICION.** Las cifras de la ficha
llevan su corte del 11 ago y describen un catalogo que la propia campana lleva
semanas reparando; **la ficha no envejece por estar equivocada, envejece por haber
funcionado**. Coincido con el acta 145 en las tres que reproducen y en las tres que
no, **sin una sola discrepancia**.

### 24.c. LA TRUNCACION A 31 CARACTERES, MEDIDA CON MI PROPIO BARRIDO

**LA REGLA DEL BARRIDO, ESCRITA ANTES DE CORRERLO:** se parte cada grafia distinta del
campo `fuente` por el separador ` - ` en (titulo, autor); una pareja entra si **los dos
traen autor**, el autor es **identico** y un titulo es **prefijo estricto** del otro.

| ref | parejas titulo-prefijo con el mismo autor | cuales |
|---|---|---|
| `0e5e0c60` (corte, 129 grafias) | **3 pares** | Hugos (31 contra 37), Horowitz (31 contra 32) y **Tim Brown** (`Change by Design` de 16 contra `Change by Design, Revised and U` de 31) |
| `WORK` (hoy, 67 grafias) | **2 pares** | Hugos, con **0 vivos** y 1 deprecado en la corta contra 95 vivos y 20 deprecados en la larga; Horowitz, con **0 vivos** y 5 deprecados contra 87 vivos y 1 deprecado |

**COINCIDO CON EL ACTA 145 EN LAS DOS DE HOY**, con sus longitudes y con sus ceros de
nodos vivos. **Y TRAIGO UNA TERCERA QUE EL ACTA NO NOMBRA**, la de Tim Brown, que
existia en el corte y **hoy ya no**: su forma corta se fusiono.

**Y AQUI VA MI UNICA DISCREPANCIA DE FONDO CON EL ACTA 145, DECLARADA Y NO COPIADA.**
El acta dice que las dos son *"LAS DOS UNICAS DEL CATALOGO"*. **Eso es cierto de las
PAREJAS y falso de las TRUNCACIONES**, y son dos unidades distintas. Un barrido por
parejas **solo ve una truncacion cuando la forma larga tambien vive en el catalogo**;
una grafia recortada cuyo original nadie escribio nunca **es invisible para el**.
Censado aparte, con la otra unidad: **hoy hay 10 grafias distintas cuyo titulo mide
exactamente 31 caracteres**, y **ocho de ellas estan VIVAS y son CANONICAS de la tabla
de `OP-S-11`** (`Change by Design, Revised and U`, `Co-Intelligence_ Living and Wor`,
`Juran's Quality Handbook_ The C`, `Managing the Risks of Organizat`, `The Field Guide
to Understandin`, `The Green to Gold Business Play`, mas `Guia de empaque para
transporte`, que mide 31 por coincidencia y no por recorte). **La truncacion a 31 no
esta resuelta: esta HORNEADA EN LA TABLA CANONICA.** Es medicion, no operacion: **no
se toca nada**, y va como pregunta al auditor en el reporte de esta vuelta.

---

## CORRECCION 25. **LA CIFRA DE LAS GRAFIAS DE 31 CARACTERES, CORREGIDA, CON SUS DOS UNIDADES Y SUS DOS NOMINAS ENTERAS**

**Vuelta 147, TAREA 1.b, sobre la caida 4.1 del acta del auditor de la vuelta
146 (de CIFRA PUBLICADA, y ACUMULA).** Corte de todas las cifras de esta
correccion: **2 sep 2026**. **NO SE BORRA NI UNA LETRA DE LA 24.c**: se anade
aqui debajo, por `EJECUTOR.md` 8, porque *una correccion que tapa lo que corrige
no se puede auditar*.

**LO QUE LA 24.c PUBLICA, Y ES FALSO EN SU CIFRA:** *"hoy hay 10 grafias
distintas cuyo titulo mide exactamente 31 caracteres, y **ocho** de ellas estan
VIVAS y son CANONICAS de la tabla de `OP-S-11`"*. **Y LA PROPIA FRASE ENUMERA
SIETE NOMBRES DEBAJO DE LA PALABRA OCHO**, entre parentesis y en el mismo
renglon: `Change by Design, Revised and U`, `Co-Intelligence_ Living and Wor`,
`Juran's Quality Handbook_ The C`, `Managing the Risks of Organizat`, `The Field
Guide to Understandin`, `The Green to Gold Business Play` y `Guia de empaque
para transporte`. **La cifra se contradice con su lista sin salir del renglon.**

**LO MEDIDO POR MI HOY, Y NO COPIADO DEL ACTA** (`EJECUTOR.md` 2):
`scripts/loop/vuelta147_3a_truncacion_dos_unidades.py`, salida en
`docs/loop/SALIDA_V147_3A_TRUNCACION_DOS_UNIDADES.txt`. El instrumento **no
reimplementa nada**: importa `partir` de
`vuelta146_1c_cifras_ficha_op_a_01.py`, que es el mismo particionador con el que
la 146 hizo su censo, y `cargar_tabla` de `vuelta136_simular_ops11.py`, que
parsea `OP_S_11_MAPEO_PROPUESTO.md` tal como esta escrita.

**LAS DOS UNIDADES, ESCRITAS ANTES DE CORRER NADA.** **(A) LA SOLA LONGITUD:**
`len(titulo) == 31`, con titulo el segmento anterior al primer ` - `. Es la que
uso la 3.f de la vuelta 146. **(B) EL DETECTOR VIGENTE DE LA CAMPANA:**
`len(titulo) == 31` **CON RESTO NO VACIO**.

**LA CIFRA CORREGIDA, sobre `dataset/metadata/master_graph.json` (WORK, 3.853
nodos, 67 grafias distintas del campo `fuente` en cualquier posicion), contada
de `docs/loop/SALIDA_V147_3A_TRUNCACION_DOS_UNIDADES.txt`:**

```
CIFRA grafias de 31 por la sola longitud WORK: 10 grafias
CIFRA grafias de 31 por la sola longitud vivas y canonicas WORK: 7 grafias
CIFRA grafias de 31 por el detector vigente WORK: 9 grafias
CIFRA grafias de 31 por el detector vigente vivas y canonicas WORK: 6 grafias
```

**LAS DOS NOMINAS ENTERAS.** Por **LA SOLA LONGITUD**, las **diez**, con sus
vivos y sus deprecados, y **siete** de ellas vivas y canonicas:

```
      Change by Design, Revised and U - Tim Brown          vivos=73   depre=5    [VIVA y CANONICA]
      Co-Intelligence_ Living and Wor - Ethan Mollick      vivos=39   depre=12   [VIVA y CANONICA]
      Essentials of Supply Chain Mana - Michael H. Hugos   vivos=0    depre=1    [ni viva ni canonica]
      Guia de empaque para transporte                      vivos=1    depre=0    [VIVA y CANONICA]
      Juran's Quality Handbook_ The C - Joseph A. Defeo    vivos=459  depre=111  [VIVA y CANONICA]
      Managing the Risks of Organizat - Reason, J. T_      vivos=90   depre=22   [VIVA y CANONICA]
      The Field Guide to Understandin - Dekker, Sidney     vivos=102  depre=1    [VIVA y CANONICA]
      The Field Guide to Understandin - Dekker, Sidney;    vivos=0    depre=15   [ni viva ni canonica]
      The Green to Gold Business Play - Daniel C. Esty     vivos=209  depre=33   [VIVA y CANONICA]
      The Hard Thing About Hard Thing - Ben Horowitz       vivos=0    depre=5    [ni viva ni canonica]
```

Por **EL DETECTOR VIGENTE**, las **nueve**, y **seis** de ellas vivas y
canonicas. **La diferencia entre las dos unidades es UNA SOLA GRAFIA, nombrada
por el instrumento**:

```
  LA DIFERENCIA ENTRE LAS DOS UNIDADES, NOMBRADA UNA A UNA: 1 grafia(s)
      Guia de empaque para transporte  titulo de 31 car, RESTO VACIO
```

Los tres bloques de arriba salen de
`docs/loop/SALIDA_V147_3A_TRUNCACION_DOS_UNIDADES.txt`.

**EL SEGUNDO CAMINO, INDEPENDIENTE Y QUE NO PASA POR EL GRAFO:** la tabla
canonica leida directamente. De sus **129 filas** salen **54 canonicas
distintas**, y de esas, **siete** tienen titulo de 31 por la sola longitud y
**seis** por el detector vigente. **Los dos caminos dan lo mismo**, contado de
la misma salida:

```
CIFRA canonicas distintas de la tabla OP-S-11: 54 grafias
CIFRA canonicas de 31 por la sola longitud: 7 grafias
CIFRA canonicas de 31 por el detector vigente: 6 grafias
```

**CUAL ES LA UNIDAD QUE GOBIERNA Y POR QUE, CON LA CITA DEL DETECTOR DELANTE.**
**Gobierna (B), el detector vigente**, y no lo decide esta correccion: lo decide
el registro. Esta escrito en `docs/PENDIENTES.md`, **DECIMA entrada** (vuelta
132, corregido en la vuelta 131 sobre el discutible del acta 130 y re-medido en
la vuelta 134), y **nombra a su falso positivo por su nombre**:

> *"El detector mecanico de truncamiento vigente, corregido en la vuelta 131
> (acta 130, discutible del 130) y medido de nuevo hoy: `len(titulo) == 31` CON
> RESTO NO VACIO. La sola longitud fichaba un falso positivo, `Guia de empaque
> para transporte`, titulo completo sin autor, RESTO vacio, que no esta
> truncado: simplemente su titulo real mide 31 caracteres."*

Y esta escrito ademas **en el codigo desde la vuelta 131**:
`scripts/loop/vuelta131_residuo_para_decision.py`, funcion `es_truncada`, que
dice `len(titulo_de(g)) == 31 and bool(resto_de(g))`. **La 3.f de la vuelta 146
uso la sola longitud y metio a `Guia de empaque para transporte` en la cuenta,
diciendolo entre parentesis en la misma frase.**

**LA CIFRA QUE QUEDA, ENTONCES: por la unidad que gobierna, NUEVE grafias de
titulo de 31 y SEIS vivas y canonicas.** Por la unidad que la 146 uso, **DIEZ y
SIETE**. **La palabra OCHO no sale de ninguna de las dos.**

**MI MEDICION NO DISCREPA DE LA DEL ACTA 146 EN NINGUNA DE LAS CUATRO CIFRAS**
(siete y seis por sus dos unidades, nueve y diez por las suyas). Lo declaro
porque `EJECUTOR.md` 2 obliga a declarar el contraste, coincida o no.

**LO QUE ESTA CORRECCION NO HACE, Y ES LA MITAD IMPORTANTE.** **No toca el
dataset, no toca la tabla, no toca una grafia y no toca
`docs/plan/OPERACIONES.jsonl`.** No mueve un nodo, no mueve una arista y no
mueve una ficha. **Y EL HALLAZGO DE FONDO DE LA 146 SIGUE EN PIE Y NO SE
RETIRA: la truncacion a 31 esta HORNEADA EN LA TABLA CANONICA**, y eso lo
demuestra el segundo camino de arriba, que ve **seis canonicas truncadas sin
mirar el grafo**. **Lo que fallaba era la cuenta y la unidad, no la idea.** Que
hacer con una tabla canonica que hornea titulos recortados **queda registrado
para quien cierre la fase 08**, y no es decision de esta vuelta.

---

## CORRECCION 26. **EL UMBRAL DE LA COLA EXISTE, TIENE NOMBRE, TIENE DOS NUMEROS Y TIENE MOTIVO ESCRITO**

**Vuelta 147, TAREA 1.c, sobre la caida 4.2 del acta del auditor de la vuelta
146 (de REPORTE, y ACUMULA).** Corte: **2 sep 2026**. **NO SE BORRA NI SE
ESCONDE LA FRASE QUE SE CORRIGE.**

**LA FRASE CORREGIDA, CITADA VERBATIM DE SU COMMIT Y NO REESCRITA.** Es la
cabecera de la PREGUNTA 2 del reporte de la vuelta 146 y su conclusion, tal como
se commitearon. El bloque va con su ref y su ruta en la propia marca, que es el
patron de la CITA CONGELADA, y el ref es **un hash y no `HEAD`**, porque un ref
movil no congela nada:

<!-- CITA CONGELADA 723b4639:docs/loop/REPORTE.md -->
```
**PREGUNTA 2. EL UMBRAL DE LA COLA NO TIENE NUMERO EN NINGUNA PARTE.** `OP-A-02` lo
cita por referencia y el barrido no halla ninguna constante que lo fije. Sin ese numero
la puerta semantica no se puede cablear. **Cual es, y de donde se lee.**
```
<!-- FIN CITA CONGELADA -->

**LO QUE HAY DE VERDAD, LEIDO POR MI DEL CODIGO Y NO DEL ACTA.**
`scripts/intra_dominio.py`:

  - **linea 60: `UMBRAL_TITULO = 80`**. Es el umbral de parecido de titulo
    (`token_sort_ratio` de rapidfuzz).
  - **linea 68: `UMBRAL_SEMANTICO = 0.78`**.

**Y TIENE MOTIVO ESCRITO EN EL PROPIO CODIGO**, en el comentario que va entre
las dos constantes: dice que el semantico se **BAJO DE 0.80 A 0.78 para el
cribado completo**, y da la medicion que lo justifica: las **DOS parejas ya
adjudicadas** que la corrida a 0,80 perdia viven en **0,7890**
(`accion_correctiva_4` con `accion_correctiva_sistematica`) y **0,7887**
(`cadencia` con `gestion_seguimiento_prospectos`); y los pares que entran por esa
rebaja van marcados con `banda_078_080` para poder contarlos aparte.

**UNA DISCREPANCIA MENOR CON EL ACTA, DECLARADA Y NO RESUELTA COPIANDO**
(`EJECUTOR.md` 2): el acta 146 dice *"con doce lineas de calibracion encima"*.
**Contadas por mi hoy sobre el fichero, el comentario de calibracion que va
encima de `UMBRAL_SEMANTICO` son SIETE lineas, de la 61 a la 67.** Las tres
lineas de comentario anteriores (56 a 58) son las de `MARCA_MANUAL` y no hablan
del umbral. **La discrepancia no cambia ningun veredicto: las dos constantes,
sus dos lineas y su motivo son exactamente los que el acta nombra.**

**POR QUE ES EL UMBRAL DE LA COLA.** La ficha de `OP-A-02` dice que *"el umbral
de la cola es el mismo del cribado intra"*, y `scripts/intra_dominio.py` **ES**
el cribado intra. **La consecuencia que importa: la puerta semantica `A2.6` SI se
puede cablear, y el bloqueo que la PREGUNTA 2 declaraba no existe.**

**POR QUE MI BARRIDO NO LO HALLO, ESCRITO SIN ADORNO, PORQUE ES EL CORAZON DE LA
ESCALADA DE LA VUELTA 147.** El barrido de la 3.e de la 146
(`docs/loop/SALIDA_V146_3E_BARRIDO_UMBRAL.txt`) tenia **las cinco piezas del
sello completas** y **`scripts/intra_dominio.py` estaba DENTRO de su universo**
(1.482 ficheros de `scripts/`, `engine/` y `web/`). Fallo por sus dos piernas:

  - **LA PIERNA POR NOMBRE era `umbral|cola`**, y el fichero **se llama
    `intra_dominio.py`**, o sea por su operacion y no por su constante. Es la
    misma forma en que la caida de la 145 no hallo
    `OP_S_11_MAPEO_PROPUESTO.md`.
  - **LA PIERNA POR CONTENIDO eran TRES NOMBRES DE CONSTANTE ADIVINADOS**,
    `UMBRAL_DE_LA_COLA`, `UMBRAL_COLA` y `umbral_de_la_cola`, **ninguno de los
    cuales existe en ninguna parte del repositorio**. **La constante real se
    llama `UMBRAL_SEMANTICO`.**

**ESO ES LO QUE LA TAREA 2 DE LA VUELTA 147 VIENE A IMPEDIR**, y no con prosa:
`barrer_ausencia.py` publica desde hoy **la SEXTA PIEZA del sello, la VITALIDAD
DE LOS PATRONES DE CONTENIDO** (cuantas de las alternativas del patron aparecen
en el universo), y `verificar_ausencias_del_reporte.py` **rechaza un barrido
cuyas alternativas de contenido esten TODAS muertas**. **Corrida sobre el sello
del umbral de la 146 congelado en su commit, la guarda sale ROJO nombrando las
tres cadenas muertas**, y sobre el mismo barrido **rehecho por el CONCEPTO**
(`umbral|similitud`) sale VERDE y **halla `scripts/intra_dominio.py`**. Las dos
salidas estan en `docs/loop/SALIDA_V147_2C_MUTACION_VITALIDAD.txt` y
`docs/loop/SALIDA_V147_2D_BARRIDO_UMBRAL_REHECHO.txt`.

**LO QUE ESTA CORRECCION NO HACE:** no toca `docs/plan/OPERACIONES.jsonl`, no
toca la ficha de `OP-A-02` y no toca una sola grafia del campo `fuente`.

---

## CORRECCION 27. **EL SEIS DE LAS COLADAS DEL ACTA 146 NO ES SEIS, Y MI MEDICION DE HOY TAMPOCO DICE CINCO EN LOS DOS SUJETOS**

**Vuelta 148, TAREA 2.6, sobre la caida 4.3.a del acta del auditor de la vuelta
147 (de CIFRA, DEL AUDITOR, declarada por el mismo).** Corte: **2 sep 2026**.
**POR ADICION: NO SE BORRA NI SE ESCONDE NINGUNA DE LAS DOS CIFRAS ANTERIORES.**

**LA CIFRA VIEJA, CITADA Y NO REESCRITA.** El acta 146 publica, en su propia
pagina, *"son SEIS escapes en esta misma pagina, CINCO de ellos sin barrido en
ventana"*, y su cabecera de commit lo repite: *"MEDI EL ESCAPE DE SU
VOCABULARIO: SEIS EN SU PROPIA PAGINA, CINCO SIN BARRIDO EN VENTANA"*.

**LA CORRECCION DEL PROPIO AUDITOR, CITADA COMO CONTRASTE Y NO COMO FUENTE**
(`EJECUTOR.md` 2). El acta 147, seccion 4.3.a, se corrige sola: *"mi acta 146
publico SEIS afirmaciones coladas y son CINCO"*.

**MI MEDICION DE HOY, CON INSTRUMENTO PROPIO**
(`scripts/loop/vuelta148_2f_medir_correcciones_27_28.py`, salida en
`docs/loop/SALIDA_V148_2F_CORRECCIONES_27_28.txt`). Se mide el **ESCAPE PURO**:
las frases que disparan **SOLO** formulas del vocabulario NUEVO, o sea las que
las DOCE formulas de la vuelta 146 no veian en absoluto. Vocabulario medido hoy:
**12 viejas mas 8 anadidas, 20 activas.**

  - **SUJETO (a), LA PAGINA DEL ACTA 146**, congelada en su commit de nacimiento
    `dc77ef71:docs/loop/_v146_acta_seccion.md`: **CUATRO frases**, y las cuatro
    van nombradas en la salida con la formula que las dispara.
  - **SUJETO (b), EL REPORTE DE LA VUELTA 146**, congelado por ref computado
    `723b4639:docs/loop/REPORTE.md`: **CINCO frases**, tambien nombradas una a
    una.

**LO QUE ESTO DEJA, DICHO SIN REDONDEAR HACIA LO COMODO.** **El SEIS no
reproduce en ninguno de los dos sujetos.** **El CINCO del acta 147 reproduce al
digito, pero sobre el REPORTE de la 146, no sobre la pagina del acta**, que es
el sujeto que la frase del acta 146 nombra (*"esta misma pagina"*). **Sobre la
pagina del acta mi instrumento cuenta CUATRO, y esa es una discrepancia NUEVA
con el acta 147 que declaro y NO resuelvo copiando**, por `EJECUTOR.md` 2.
**Ninguna de las dos lecturas cambia el veredicto de fondo**, que es lo que la
correccion existe para dejar escrito: la cifra publicada en la 146 era mas alta
que la real por cualquiera de los dos caminos, y la ampliacion del vocabulario
de la vuelta 147 estaba justificada.

---

## CORRECCION 28. **LAS DOCE LINEAS DE CALIBRACION SON SIETE, Y ESTA REPRODUCE AL DIGITO**

**Vuelta 148, TAREA 2.6, sobre la caida 4.3.b del acta del auditor de la vuelta
147 (de CIFRA, DEL AUDITOR, declarada por el mismo).** Corte: **2 sep 2026**.
**POR ADICION: NO SE BORRA LA CIFRA VIEJA.**

**LA CIFRA VIEJA, CITADA:** el acta 146 dice *"con doce lineas de calibracion
encima"* del umbral. **LA CORRECCION DEL AUDITOR, COMO CONTRASTE:** el acta 147,
seccion 4.3.b, dice *"son SIETE, de la 61 a la 67; conte desde la 56 y me lleve
por delante un comentario ajeno"*.

**MI CONTEO DE HOY, SOBRE EL FICHERO Y NO SOBRE EL ACTA** (mismo instrumento y
misma salida que la CORRECCION 27). En `scripts/intra_dominio.py`,
`UMBRAL_SEMANTICO = 0.78` esta en la **linea 68**, y las lineas de comentario
CONTIGUAS inmediatamente encima van de la **61 a la 67**, las siete impresas una
a una con su numero. **La linea 60, la de encima del bloque, es
`UMBRAL_TITULO = 80` y no es comentario**, o sea que el bloque no sigue hacia
arriba.

**CIFRA lineas de calibracion encima del umbral: 7 lineas.** **REPRODUCE AL
DIGITO la correccion del acta 147, y el DOCE del acta 146 no reproduce.** Las
tres lineas de comentario que van de la 56 a la 58 son las de `MARCA_MANUAL` y
no hablan del umbral, tal como el auditor declaro.

---

## CORRECCION 29. **LA VERIFICACION 3 DE `OP-A-01`: SU MITAD MECANICA SE QUEDA Y SU MITAD SEMANTICA SE REMITE A `A2.6`**

**Vuelta 148, TAREA 1.b, por DECISION DEL FUNDADOR del 2 sep 2026 (PREGUNTA 2,
opcion 2), escrita en
`docs/loop/paradas/2026-09-02-aduana-vector-y-a13-DECISION.md`.** Corte: **2 sep
2026**. **EL TEXTO VIEJO NO SE BORRA: ENCABEZA LA PROPIA ENTRADA DE LA FICHA.**

**EL TEXTO VIEJO, CITADO VERBATIM DE `docs/plan/OPERACIONES.jsonl`:** *"Gate 0
rechaza un nodo cuyo segundo libro no aparece en ningun paso"*. Es la tercera de
las tres verificaciones de `OP-A-01`.

**LO QUE LA DECISION DISPONE, Y ES LO QUE SE ESCRIBE DETRAS DEL TEXTO VIEJO, NO
EN SU LUGAR:**

  - **SU MITAD MECANICA QUEDA COMO ESTA**: el segundo libro se comprueba contra
    la nomina adjudicada, instalada en Gate 0 y mordiendo.
  - **SU MITAD SEMANTICA SE REMITE A LA PUERTA `A2.6`** de `OP-A-02`: la
    vecindad por contenido sobre el indice semantico es su lectura ejecutable.

**EL MOTIVO, MEDIDO Y NO DE PALABRA, CITADO DEL ACTA 146:** la lectura literal
de esta entrada (buscar el titulo del segundo libro como texto dentro de
`pasos_accionables`) **DISPARA EN 9 DE 9 sobre nodos adjudicados enteros**, o sea
que rechazaria los ocho ya adjudicados porque ningun paso del catalogo nombra su
libro: **INEJECUTABLE tal como esta escrita**.

**LO QUE ESTA CORRECCION NO HACE.** No toca el campo `estado` de ninguna ficha,
congelado desde la vuelta 139 y hoy medido en `LISTA` para `OP-A-01`. No toca el
esquema: las **71 fichas siguen teniendo UN solo esquema de 18 claves**, medido
hoy. Y no cierra la fase 07 de palabra: **la vara de codigo se re corre y publica
su propio veredicto**, y la remision de `A1.3` a `A2.6` solo cuenta como control
entero **mientras `A2.6` este instalado, muerda y no tenga parada abierta
encima**, comprobado en cada corrida y probado por mutacion en
`scripts/loop/vuelta148_2c_mutacion_vara_parada.py`.

---

## R.29. Registro de correcciones y adjudicaciones declaradas de la vuelta 149 (acta del auditor, vuelta 149; escrito en la vuelta 150, TAREA 1.a)

**POR ADICION, y en `docs/plan/CORRECCIONES_A_APLICAR.md` porque el encargo de la
vuelta 150 nombra este fichero con esas palabras.** R.20 a R.28 viven en
`docs/PENDIENTES.md`; ahi queda una **remision de una linea** a esta entrada, no
una copia. Corte de todas las cifras de esta entrada: **2 sep 2026**, salvo donde
se diga otra cosa. Las adjudicaciones y las caidas del auditor se escriben IGUAL
que las del ejecutor.

**(1) LOS NUEVE DISCUTIBLES DEL REPORTE 148, LOS NUEVE ADJUDICADOS A FAVOR, CON
RESERVA EN EL 2, EL 4 Y EL 5.**

  - **3.1, DISCUTIBLE 1, REPARAR LA GUARDA DE LA APERTURA EN VEZ DE PARAR: A
    FAVOR, SIN RESERVA.** La guarda exigia *el padre es el commit del acta*, que
    es un **proxy** del fin verdadero (*la apertura se midio antes de la primera
    operacion*), y el proxy se rompe **estructuralmente** en toda vuelta que
    reanuda tras una parada. Lo que lo salva de ser el auditado tocandose su
    propia guarda son tres cosas que el auditor verifico: el rojo corrido ANTES
    de tocarla y commiteado aparte
    (`SALIDA_V148_0D_APERTURA_SELLADA_GUARDA_VIEJA.txt`), el criterio nuevo
    cayendo con **dos** mutaciones, y el corredor aceptado **impreso entero**.
  - **3.2, DISCUTIBLE 2, LAS TRES RUTAS DEL CORREDOR LAS ELIGIO EL EJECUTOR: A
    FAVOR, CON RESERVA ANOTADA.** `PROMPT_SIGUIENTE.md`, `PARA_ALEXIS.md` y
    `docs/loop/paradas/` son los tres sitios donde la casa escribe una parada.
    **LA RESERVA:** el dia que una decision toque un cuarto sitio la guarda dara
    ROJO y habra que ensancharla; **que ensancharla sea un acto declarado y no un
    parche silencioso queda anotado**.
  - **3.3, DISCUTIBLE 3, `A1.3` CUENTA COMO ENTERO POR REMISION Y LA VARA PUBLICA
    9 DE 9: A FAVOR, Y EL AUDITOR LO PROBO POR MUTACION PROPIA.** Mando fuera el
    fichero de la decision y **la vara se cayo sola de 9 a 7 arrastrando a
    `A1.3`**, con el motivo escrito. Eso separa una remision de un interruptor:
    la remision se comprueba en la misma corrida y **cae en cascada**.
  - **3.4, DISCUTIBLE 4, `estado_de_parada` MIRA SI EL `-DECISION.md` ESTA AL
    LADO: A FAVOR, CON RESERVA SERIA Y NOMBRADA.** El fichero en disco es el
    unico sujeto que no se puede fingir con una palabra, y la vara no descansa
    solo en eso: `A2.6` ademas tiene que EXISTIR y MORDER por mutacion, 6 de 6.
    **LA RESERVA, escrita para quien venga: el fichero prueba que se decidio, no
    que se aplico.**
  - **3.5, DISCUTIBLE 5, LA EXENCION DECLARADA LA ESCRIBE EL AUDITADO: A FAVOR,
    CON RESERVA.** No es un interruptor porque **la guarda comprueba ella misma
    que lo eximido no habla del repositorio** y rechaza nombrando la ruta, el
    `SALIDA_V<N>_` o la extension. Verificado con su bateria de **seis casos**.
    **LA RESERVA: es una puerta que antes no existia**, y queda abierta con una
    condicion encargada: **cada exencion usada se imprime con su motivo en la
    salida del cierre**.
  - **3.6, DISCUTIBLE 6, LA CORRECCION DENTRO DEL MISMO STRING EN VEZ DE UNA
    CLAVE NUEVA: A FAVOR, SIN RESERVA.** Medido por el auditor: **71 fichas, un
    solo esquema, 18 claves**. Una clave 19 en una sola ficha habria roto la
    uniformidad que hace medible al catalogo entero.
  - **3.7, DISCUTIBLE 7, `OP-S-12` ELIGE QUE ENTRADA SOBREVIVE: A FAVOR, Y ES EL
    DISCUTIBLE MEJOR PLANTEADO DE LA VUELTA.** Medido y no creido: los `node_id`
    identicos, los `ids_alias` identicos, **CERO literales aparecen de la nada y
    121 desaparecen del todo**, y los **7.706** vecindarios resueltos identicos
    uno a uno. **Lo que la operacion elige no es un id: es cual de dos escrituras
    del mismo id sobrevive.**
  - **3.8, DISCUTIBLE 8, EL 1.056 QUE NO SE CUMPLE: A FAVOR, CON EL RASTRO
    COMPLETO.** Su desarrollo entero, re medido hoy con instrumento propio del
    ejecutor, va en la **CORRECCION 30** de esta misma pagina, con una
    discrepancia declarada.
  - **3.9, DISCUTIBLE 9, EL DESFASE DEL INDICE SE TRAE Y NO SE ARREGLA: A FAVOR,
    SIN RESERVA.** Arreglarlo pide `VOYAGE_API_KEY`, o sea gasto fuera del repo
    con una credencial que la casa reserva. El auditor anade que los **370** no
    vivos son **370 DEPRECADOS y CERO FANTASMAS**, y que **el blob del indice no
    se movio en toda la vuelta**.

**(2) LAS DOS PREGUNTAS DEL REPORTE 148, CONTESTADAS SIN DOCTRINA NUEVA.**

  - **3.10, PREGUNTA 1, SI LA FASE 08 PUEDE DARSE POR HECHA: NO.** El criterio
    esta en la primera linea de `docs/plan/08_VERIFICACION.md`: *"UNA FASE ESTA
    HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA. No cuando pasa
    verde: cuando se CAERIA."* **Una verificacion que no se puede correr no se
    puede caer.** Cubierto ademas por extension citable de la seccion 4 de
    `AUDITOR.md` (*"Credenciales ausentes... que falle visible"*). **LA FASE 08
    QUEDA ABIERTA HASTA LA SESION CON CREDENCIAL.**
  - **3.11, PREGUNTA 2, SI EL REINDEXADO ENTRA EN ESA SESION: SI, Y NO ES OPINION
    DEL AUDITOR.** El reindexado **ES el punto 5 de la verificacion transversal
    de la propia fase 08**. Verificado en el codigo: `main()` de
    `scripts/build_semantic_index_voyage.py` reconstruye la lista `ids` desde
    cero con los no deprecados, asi que **una corrida completa deja el indice con
    exactamente los vivos de hoy**.

**(3) EL CIERRE DE LA FASE 07 ADUANA, ADJUDICACION 3.12 DEL ACTA 149.**
**LA FASE 07 QUEDA CERRADA.** El auditor la cierra y la firma, sobre la letra de
la decision del fundador del 2 sep 2026 (*"Con las dos, la fase 07 CIERRA"*), con
las dos aplicaciones verificadas por el en el codigo y no en la prosa (el paso
`a-previo` existe en `integrar_packs.py:317`, se llama antes de la copia en la
linea 556, la puerta sigue en el `copy2` de la linea 420 con `A2.6` en la 417),
con **la vara de codigo en 9 de 9 enteros, 0 no enteros, 0 no instalados**,
sostenida por **su propia mutacion**, y con el motivo de la remision medido: la
lectura literal **dispara en los 9** sobre los 8 nodos adjudicados. Que
`tallar_estado_de_fase.py` diga `NO COMPUTABLE` no lo impide: es la frontera de la
adjudicacion 3.9 del acta 144, que separa la vara de GRAFO de la vara de CODIGO.
**Dos unidades no comparten columna.**

**(4) LAS DOS ADJUDICACIONES DE ORDEN, 3.13 Y 3.14.**

  - **3.13, `OP-C-05` SE EJECUTA EN LA VUELTA SIGUIENTE Y ES BLOQUEANTE.** No es
    un descubrimiento discutible: es el orden escrito de `AUDITOR.md` 3, FASE III
    (*"fase 0 de codigo primero y bloqueante"*). **Sin ella, las 925 entradas que
    la vuelta 148 retiro no tienen quien las defienda.**
  - **3.14, EL `estado` DE `OP-S-12` SE MUEVE A `HECHA`, PERO DESPUES DE LA
    CORRECCION, NO ANTES.** Por el precedente de la 3.12 del acta 147: `estado`
    en `HECHA` con una cuenta abierta encima es publicar un verde sobre una
    pregunta abierta. **La cuenta abierta es la verificacion 4.**

**(5) LAS CAIDAS, CON NOMBRE.**

  - **4.1, DEL EJECUTOR, DE CLASE Y DE CIFRA PUBLICADA: NINGUNA**, dicho con la
    lista de lo que el auditor re midio delante (catorce refs, las 7.706
    comparaciones, el marcador entero, las nueve filas de cabecera caracter por
    caracter, las seis baterias, las cinco guardas del cierre, los diez ficheros
    de apertura, motor, web y tsc).
  - **4.2, DEL EJECUTOR, DE EXPEDIENTE: `OP-S-12` EJECUTADA Y SU `estado` SIN
    MOVER NI DECLARAR.** La unica de las diez de `05_SANEO` que sigue en `LISTA`
    despues de correr. **Lo que la hace caida no es no moverlo: es no decir
    nada.** Un `estado` congelado a proposito es una decision; congelado en
    silencio es un expediente que no cuenta lo que paso.
  - **4.3, DEL EJECUTOR, DE INCUMPLIMIENTO DE ENCARGO, ATENUADA POR SU PROPIA
    DECLARACION: LA FASE 08 NO SE RECORRIO ENTERA POR LA MITAD QUE SI SE PODIA.**
    De las **OCHO** filas de la tabla POR FASE, que no piden credencial, se midio
    **UNA**. La declaracion lo separa de una mentira, no de un encargo sin
    entregar.
  - **4.4, DEL EJECUTOR, DE REPORTE: NINGUNA**, y el auditor explica la que
    estuvo a punto de registrar: *"Tres corren y tres piden credencial"* sobre
    cinco puntos son **dos afirmaciones verdaderas cuyos conjuntos se solapan en
    el punto 4** sin decirlo. **Registrada como imprecision de dictado, no como
    caida.** Lo que queda encargado es la palabra: *correr* no puede significar
    *se invoco* y *quedo satisfecho* en la misma frase.
  - **4.5, DE LA CASA: EL ENCARGO DE LA VUELTA 148 SALTA DE `OP-S-12` A LA FASE
    08 SIN PASAR POR `OP-C-05`.** Lo escribio el fundador al relanzar el bucle
    (commit `68db6230`), asi que no va a la cuenta de encargo del auditor ni a la
    del ejecutor, que lo siguio al pie de la letra. **Instruccion que deja
    escrita: el modo continuo mira el `depende_de` del catalogo y no solo la
    linea del encargo.**
  - **4.6.a, DEL AUDITOR, DE PROCEDIMIENTO: corrio `run_phase1.py` suelto, fuera
    del orden del ciclo, y se saco un falso rojo** (`AssertionError: 71 nodos
    divergentes entre las dos copias`). No era un rojo: era saltarse el comando
    2. **Es la cuarta acta seguida en que un auditor cae en la misma trampa**, y
    por eso encarga la guarda en vez de limitarse a confesarla.
  - **4.6.b, DEL AUDITOR, DE CIFRA DE SU LINAJE: el CINCO del acta 147 tampoco
    reproduce sobre el sujeto que la frase nombra.** Su medicion de hoy da
    **CUATRO sobre la pagina del acta y CINCO sobre el reporte de la 146**. **La
    correccion de la 147 corrigio la cifra y erro el sujeto.** El acierto es del
    ejecutor, que la declaro en vez de copiarla, y ya esta registrada por adicion
    en la CORRECCION 27.

**(6) LA METRICA DE CREDITO: LA TANDA BAJA.** Las dos discrepancias del acta
aparecieron **FUERA de los discutibles marcados** y las dos son de expediente
(el `estado` de `OP-S-12` sin mover ni declarar, y `OP-C-05` desbloqueada y sin
nombrar). Ninguna toca una cifra ni una clase. Por `AUDITOR.md` 1.2 **se debe una
relectura al doble del tramo del expediente**, entregada en la TAREA 3 de la
vuelta 150.

---

## CORRECCION 30. **LA VERIFICACION 4 DE `OP-S-12`: EL 1.056 ERA FIEL A SU CORTE Y HOY SON 925, CON EL RASTRO DE LAS TREINTA VERSIONES DELANTE**

**Vuelta 150, TAREA 1.b, sobre la adjudicacion 3.8 del acta del auditor de la
vuelta 149 (discutible 8 del reporte 148, a favor).** Corte de la medicion de
hoy: **2 sep 2026**. **POR ADICION: NO SE BORRA LA CIFRA VIEJA NI SE TOCA EL
TEXTO DE LA FICHA.**

**LA CIFRA VIEJA, CITADA VERBATIM DE `docs/plan/OPERACIONES.jsonl`, ficha
`OP-S-12`, campo `verificacion`, cuarta entrada:** *"el numero total de entradas
baja en exactamente 1.056; si baja mas, se borro algo que no era duplicado"*.

**SU CORTE Y SU UNIVERSO, LOS DOS ESCRITOS EN LA PROPIA FICHA:** `fecha_corte`
**2026-08-11**, y su `evidencia` dice *"scripts/plan/aristas_duplicadas_tras_resolver.py,
corrida del 11 ago 2026 sobre 3.521 nodos vivos"* y *"docs/plan/ARISTAS_DUPLICADAS.jsonl,
1.015 grupos"*.

**LO QUE LA OPERACION RETIRO EL 2 SEP 2026 (vuelta 148, commit `a34328b2`): 925
entradas.** No son 1.056, y **NO ES UNA CONTRADICCION**: es una cifra fiel a un
corte que se movio por debajo durante veintiuna vueltas.

**EL RASTRO, MEDIDO HOY CON INSTRUMENTO PROPIO DEL EJECUTOR** y no copiado del
acta (`EJECUTOR.md` 2). Instrumento:
`scripts/loop/vuelta150_1b_rastro_del_1056.py`; salida commiteada:
`docs/loop/SALIDA_V150_1B_RASTRO_1056.txt`.

| lo medido | cifra de hoy |
|---|---:|
| versiones de `docs/plan/ARISTAS_DUPLICADAS.jsonl` en git (`git log --follow`) | **30** |
| PRIMERA version, `af467eb1` (*"Plan: P.6, las 1.056 aristas duplicadas"*): grupos / nodos / entradas que sobran | **1.015 / 802 / 1.056** |
| version de HEAD, `d6341ebe` (vuelta 73): grupos / nodos / entradas que sobran | **898 / 711 / 935** |
| de esas 935, entradas sobre nodos **HOY DEPRECADOS** | **10** (en 10 grupos) |
| de esas 935, entradas sobre nodos **QUE YA NO EXISTEN** | **0** |
| de esas 935, entradas sobre nodos **VIVOS** | **925** |

**LAS SEIS CIFRAS REPRODUCEN AL DIGITO LAS DEL ACTA 149.** El fichero no es un
fichero quieto: **se regenera con cada fusion**, y cada fusion de `OP-U-01` y
`OP-U-02` consumio duplicadas por el camino. **La evidencia de la ficha era fiel
a su corte**, y el 925 de la pasada es el mismo numero por tres caminos
independientes: el parser del auditor, la operacion de la vuelta 148 y este
fichero escrito hace setenta y cinco vueltas.

**LA VERIFICACION 4 NO ESTA CONTRADICHA: ESTA VENCIDA.** Su guarda real (*"si
baja MAS, se borro algo que no era duplicado"*) **se respeta**: bajo exactamente
lo que habia sobre vivos, ni una entrada mas.

**UNA DISCREPANCIA CONTRA EL ACTA, DECLARADA Y NO COPIADA (`EJECUTOR.md` 2).**
El acta 149, adjudicacion 3.8, dice: *"La bajada de 1.056 a 935 es **monotona** a
lo largo de las treinta versiones"*. **MI MEDICION DE HOY DICE QUE NO ES
MONOTONA, por un solo escalon y de una sola unidad:** la version `706397c7`
(vuelta 57, 20 ago 2026 11:49) da **995** entradas que sobran y la siguiente,
`3ffc2091` (vuelta 58, 20 ago 2026 13:16), da **996**. Comprobado que la segunda
es descendiente de la primera (`git merge-base --is-ancestor 706397c7 3ffc2091`
sale en verde), o sea que el orden es el cronologico y no un artefacto del
listado. **Las otras veintiocho transiciones bajan o se quedan igual.** Sube en
una porque una fusion puede crear una duplicada nueva antes de consumir otras;
**la direccion general del acta es correcta y la palabra "monotona" no lo es**.
**La cifra que sostiene la adjudicacion 3.8 (1.056 al inicio, 935 en HEAD, 925
sobre vivos) NO depende de esa palabra y queda intacta.**

**LO QUE ESTA CORRECCION NO HACE.** No borra ni reescribe la cuarta
`verificacion` de `OP-S-12`, que se queda literal. No toca el esquema: las **71
fichas siguen teniendo UN solo esquema de 18 claves**, comprobado despues de
escribir. Y no mueve por si sola el `estado`: el `estado` se mueve **detras** de
esta correccion, que es el orden que manda la adjudicacion 3.14 del acta 149.


---

## CORRECCION 31. **EL PASE DE `estado` DE LAS ONCE, EN UN SOLO ACTO, CON EL DISPARADOR MEDIDO Y LA CONVENCION DECLARADA ANTES DE CONTAR**

**Fecha: 2026-09-02. Vuelta 152, TAREA 3. Reservada desde el acta 139, 3.6.**

**LA RESERVA, CITADA LITERAL Y NO PARAFRASEADA** (acta 139, adjudicacion 3.6):
*"Cuando las cinco remitidas queden con destino, el pase de estado de las once
(las seis fusiones y las cinco remitidas) va en UNA sola adjudicacion, con el
conteo antes y despues y la guarda de cifras del plan re-corrida, como en las
vueltas 131 y 136."*

**LAS ONCE, NOMBRADAS.**

  - **seis fusiones:** `OP-M-01-FUSION`, `OP-M-02-ACCLIMATE`, `OP-M-03-III`, `OP-M-05-APERTURA`, `OP-M-05-EDIFICIO`, `OP-M-05-INDICE`
  - **cinco remitidas:** `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES`, `OP-M-01-SEXTO`, `OP-M-03-ENLACES`

**EL DISPARADOR HA DISPARADO, Y SE MIDE EN VEZ DE AFIRMARSE.** Las once salen
**CUMPLIDO** en la tabla de `scripts/loop/tallar_estado_de_fase.py`, que es la
misma vara P1 con la que el expediente se relee. La salida entera, con las once
filas una a una, esta en `docs/loop/SALIDA_V152_T3_PASE_DE_ESTADO.txt`.

**LA CONVENCION SE DECLARA ANTES DE CONTAR, Y NO DESPUES.** El *"30 congeladas
en silencio"* **no es un cardinal duro**: es una convencion que depende de con
que lista de marcas se pregunta si una ficha habla de su propio `estado`. Medido
hoy con **cuatro listas distintas sobre las mismas 71 fichas y el mismo arbol**,
la respuesta va **de 26 a 52**. Por eso esta correccion declara la vara ANTES:
se usa **la lista A**, la que ya vive en
`scripts/loop/vuelta150_3_relectura_expediente.py:declara_su_estado`
(`ESTADO`, `DIFERIDA`, `CONGELAD`, `SIGUE EN LISTA`, `NO SE MUEVE`), porque es la
que produjo la cifra publicada y cambiarla en la misma vuelta en que se cuenta
seria mover la vara y el sujeto a la vez. Con esa vara, ANTES del pase habia
**32** fichas en `LISTA` que no hablan de su estado.

**LO QUE ESTA CORRECCION NO HACE.** No borra ni reescribe una sola linea de las
once fichas: el `estado` se mueve y el motivo se **anade** al campo `nota`. No
toca el esquema, y se comprueba con un `assert` despues de escribir: las **71
fichas siguen teniendo UN solo esquema de 18 claves**. Y **no mueve el `estado`
de las cinco mesas** (`OP-M-01` a `OP-M-05`), que hoy tambien miden CUMPLIDO:
la reserva del acta 139 nombra **once** y solo once, y ampliarla por mi cuenta
seria doctrina nueva disfrazada de cita. Queda dicho aqui, medido, para que el
auditor decida.


---

## CORRECCION 32. **LOS "307 NODOS VIVOS" DEL CASO DE BORDE DE `OP-C-05` SON 307 DESTINOS SOBRE 255 NODOS VIVOS**

**Fecha: 2026-09-02. Vuelta 152, TAREA 4. Hallazgo del acta 151, caida 4.4.**

**LA CIFRA VIEJA, INTACTA Y CITADA.** El comentario del CASO DE BORDE de la
guarda de `OP-C-05` en `scripts/run_phase1.py` dice *"hoy hay 307 nodos vivos
con un destino en las dos listas y ninguno es un fallo"*, y la linea 27 de
`docs/loop/SALIDA_V150_2C_SIETE_VERIFICACIONES.txt` dice *"307 nodo(s) vivo(s)
traen un mismo destino, tras resolver, en `nodos_previos` Y en
`nodos_siguientes` a la vez"*. **Las dos frases se quedan donde estan.**

**LA UNIDAD BUENA, AL LADO Y RE MEDIDA EN ESTA VUELTA.** El **307 es correcto**,
pero **no cuenta nodos: cuenta destinos**. Medido con instrumento propio escrito
en esta vuelta (`scripts/loop/_v152_tarea4_correccion_307.py`, salida en
`docs/loop/SALIDA_V152_T4_CORRECCION_307.txt`):

| cifra | valor |
|---|---|
| **NODOS VIVOS** con al menos un destino en `nodos_previos` Y en `nodos_siguientes` tras resolver | **255** |
| **DESTINOS** (pares nodo-destino) en esa situacion | **307** |

Un mismo nodo puede traer **varios** destinos en las dos listas a la vez, y por
eso los dos cardinales no coinciden.

**LO QUE ESTA CORRECCION NO TOCA.** El **veredicto** de la verificacion 3 de
`OP-C-05` sigue siendo **CONTESTADA, EN VERDE**: la guarda saca **0** sobre este
caso de borde, que es exactamente lo que su letra pide. Lo que estaba mal era
**como se nombraba el tamano del caso**, no el comportamiento de la guarda. Y no
se reescribe la linea 27 del fichero de la vuelta 150: se **anade** un bloque al
final, con un `assert` que comprueba que el fichero viejo es **prefijo exacto**
del nuevo.

**LA REGLA CON LA QUE ENTRA, ESCRITA POR EL FUNDADOR.** Por la **decision del 2
sep 2026, PREGUNTA 2**
(`docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md`), una cifra
falsa en el **codigo o el docstring de una guarda de `scripts/`** cuenta como
**CIFRA PUBLICADA desde esa fecha, sin retroactividad**. **Esta es anterior: se
corrige por declaracion y NO ACUMULA.**


---

## CORRECCION 33. **`OP-C-05` CIERRA ENTERA: LA MITAD DE BIDIRECCIONALES SE ENCIENDE COMO REGISTRO DE CITAS Y LAS TRES LETRAS DEJAN DE CHOCAR**

**Fecha: 2026-09-02. Vuelta 152, TAREA 6. Por la decision del fundador del 2 sep 2026, PREGUNTA 1.**

**LO QUE CHOCABA, CITADO Y NO BORRADO.** El acta 151 midio que las tres letras
vigentes de esta ficha no podian ser ciertas a la vez: **L1** (*"la guarda falla
ante cualquier arista bidireccional SALVO las de la lista blanca"*), **L2** (*"el
grafo saneado por `OP-S-12` pasa en verde"*) y **L3** (*"cada entrada CITA SU
LECTURA"*). Encender L1 como estaba escrita ponia Gate 0 **en rojo 153 veces**, y
meter los 153 en la lista obligaba a **151 entradas sin lectura**.

**LO QUE LA DECISION CAMBIA.** La lista blanca **deja de ser una lista y pasa a
ser un REGISTRO DE CITAS**. La guarda ya no pregunta *"esta en la lista?"* sino
**"tiene este par un veredicto de lectura registrado con cita?"**. **Un par sin
cita es rojo.** Asi **L2 y L3 quedan intactas y se cumplen las dos a la vez**.

**LAS CIFRAS, CONTADAS DE SUS FICHEROS Y NO TECLEADAS.**

| cifra | valor | fichero |
|---|---|---|
| pares bidireccionales entre vivos, **resolviendo alias (P.1)** | **153** | `SALIDA_V152_T6A_CRUCE.txt` |
| los mismos **sin resolver**, y la diferencia es la razon por la que P.1 no es opcional | **147** | `SALIDA_V152_T6A_CRUCE.txt` |
| contraste sobre el **mergebase con `main`** (`36b57d78`) | **83** | `SALIDA_V152_T6A_CONTRASTE_MERGEBASE.txt` |
| con cita por **CRIBADO** | **32** | `REGISTRO_DE_CITAS_OPC05.jsonl` |
| con cita por **P.10** | **0** | idem |
| con cita por **LECTURA DIRIGIDA** (`LD-OPC05-001` a `LD-OPC05-121`) | **121** | idem |
| **CON CITA, TOTAL** | **153 de 153** | idem |
| **SIN CITA** | **0** | idem |

**LAS OCHO `verificacion` DE LA FICHA QUEDAN CONTESTADAS**, y las dos que faltaban
se midieron en esta vuelta: la **6** (*"las cuatro aristas de `OP-E-05` pasan en
verde"*) da **2 de 2 pares mutuos con cita** tras resolver
(`SALIDA_V152_T6C_VERIFICACION6.txt`), y la **8**, anadida por la propia decision
del fundador, da **0 pares sin cita con el grafo saneado en verde**.

**EL CASO POSITIVO MUERDE POR LOS DOS LADOS, y esa es la parte que no se afloja.**
`SALIDA_V152_T6C_MUTACION.txt`: la contraprueba pasa en **VERDE exit 0**; quitar
**una** cita del registro tumba Gate 0 con **exit 1 nombrando el par**; y anadir
una arista bidireccional que nadie leyo **tambien** lo tumba con **exit 1
nombrandola**. Los dos pares se eligen **por computo** y no a dedo. **`dataset/`
queda identico antes y despues, comprobado con sha256 y no prometido.**

**DOS TRAMPAS QUE ME MORDIERON Y QUEDAN ESCRITAS DENTRO DEL ARNES**, porque la
proxima vuelta las va a encontrar igual: **(1)** `run_phase1` **suelto** deja la
copia web desincronizada y la corrida siguiente sale en rojo **por ciclo sin
cerrar**, no por la guarda; **(2)** `master_graph.json` **se regenera** desde
`dataset/nodos/*.json`, asi que **mutarlo no muta nada** y la guarda leia un grafo
que ya habia borrado la mutacion. La primera version del arnes cayo en las dos y
daba un **falso verde** en el caso B.

**Y EL `estado` SE MUEVE DETRAS DE ESTA CORRECCION, NO DELANTE**, que es el orden
que la adjudicacion 3.14 del acta 149 ya fijo para `OP-S-12`.


---

## CORRECCION 34. **LA GUARDA DE `OP-C-05` ESTABA VERDE SOBRE UN UNIVERSO INCOMPLETO: SON 154 PARES, NO 153, Y UNO ESTABA SIN CITA**

**Fecha: 2026-09-02. Vuelta 154, TAREA 2. Hallazgo del acta 153, seccion 4, FUERA de lo marcado.**

**LA CIFRA QUE SE CORRIGE.** Donde la `nota` de `OP-C-05` y los comentarios de
`scripts/run_phase1.py` publican *"153 pares bidireccionales entre vivos tras
resolver, 153 con cita, 0 sin cita"*, lo cierto es **154 PARES, Y UNO ESTABA SIN
CITA**. El **"0 sin cita" era FALSO**. Nada del texto viejo se borra en ninguna
de las dos sedes: la correccion se anade debajo, con la frase vieja tachada.

**POR QUE, Y ESTA MEDIDO.** La guarda recorria los nodos ACTIVOS y de cada uno
leia **SOLO** su lista `nodos_siguientes`. La FUENTE no hacia falta resolverla
(el nodo de partida ya es vivo por construccion), pero **`nodos_previos` NO SE
LEIA NUNCA**, asi que una arista declarada solo por ese lado era invisible.

**LA VARA DECLARADA SON LOS DOS CAMPOS, Y NO SE INVENTA HOY.** Esta escrita en
tres sitios, los tres re leidos con instrumento propio antes de tocar nada:
la **cabecera** cuenta `nodos_previos` (8.740) y su union de 9.914 sale de los
dos; **`aristas_a_simetrizar`**, dentro de la propia `scripts/run_phase1.py`,
admite una arista *"si LA DECLARA UN NODO VIVO, EN CUALQUIERA DE SUS DOS
VISTAS"*, que es exactamente esta vara y la comprobacion de simetria de Gate 0
ya la usa; y **`web/lib/engine/planRedactor.ts` linea 96** recorre los dos campos
juntos como vecinos. Mas **P.1**, que manda resolver antes de contar.

**LAS CUATRO VARAS, PUBLICADAS ENTERAS Y NO SOLO LA QUE CONVIENE**
(`scripts/loop/vuelta154_tarea2a_universo_bidireccionales.py`, salida
[`loop/SALIDA_V154_T2A_UNIVERSO.txt`](../loop/SALIDA_V154_T2A_UNIVERSO.txt)):

| vara | pares | sin cita |
|---|---:|---:|
| fuentes vivas, solo `nodos_siguientes` (la de la guarda vieja) | 153 | 0 |
| **fuentes vivas, LOS DOS campos (LA VIGENTE)** | **154** | **1** |
| todas las fuentes, solo `nodos_siguientes` | 155 | 2 |
| todas las fuentes, los dos campos | 157 | 4 |

Las cuatro **reproducen al digito** la tabla del acta 153, 4.1.

**EL PAR QUE FALTABA:** `error_proofing_servicio` contra `metodologia_6s`, los
dos VIVOS, con las dos direcciones declaradas por el **propio `metodologia_6s`**
dentro de sus dos listas (`nodos_siguientes` trae `mistake_proofing_poka_yoke` y
`nodos_previos` trae `errores_a_prueba_poka_yoke`, y los dos resuelven al mismo
nodo vivo). Leido por **P.5** en esta vuelta y registrado como **`LD-OPC05-122`,
clase C** por el banco 9.22, primer polo. **`n` no se movio: 3.388 antes y
despues.**

**LO QUE LA VARA DEJA FUERA SE NOMBRA EN VEZ DE CALLARSE** (banco 9, fallar
ruidoso). Con fuentes deprecadas admitidas saldrian 157 pares y 4 sin cita, o sea
**TRES pares mas**: `asignacion_recursos_en_gates <-> sistema_gates_go_kill`,
`formalizar_junta_asesora <-> identificar_consejo_asesores` y
`revision_portafolio_periodica <-> sistema_gates_go_kill`. Quedan fuera por el
criterio **ya adjudicado el 14 ago 2026** (un nodo deprecado es registro
historico, no superficie del producto), no por una vara estrechada hoy.

**LA MUTACION MUERDE POR EL LADO QUE ERA CIEGO, Y LA INGENUA NO HABRIA PROBADO
NADA.** El paso 5 de `run_phase1` **simetriza los ids CRUDOS** antes de que Gate
0 corra, asi que meter el id crudo de un vivo en `nodos_previos` de otro lo
vuelve visible tambien para la guarda vieja. El punto ciego real vive en el
desfase entre **ids crudos** (que es lo que la simetrizacion mira) e **ids
resueltos** (que es lo que la guarda mira). La mutacion mete un **alias
deprecado que resuelve a un vivo** en las DOS listas de otro vivo, con los tres
nombres elegidos **por computo**:
[`loop/SALIDA_V154_T2D_MUTACION.txt`](../loop/SALIDA_V154_T2D_MUTACION.txt).
**CASO A**, guarda nueva sobre la mutacion: **ROJO exit 1 nombrando el par**.
**CASO B, LA CONTRAPRUEBA OBLIGATORIA**, la guarda **VIEJA** sacada literal de
git sobre **LA MISMA** mutacion: **VERDE exit 0**. **CASO C**, guarda nueva sobre
arbol intacto: **VERDE**. `dataset/` **identico antes y despues por sha256**.

**LA CIFRA DE HOY, con Gate 0 en verde: 154 pares bidireccionales entre vivos
tras resolver, 154 con cita, 0 SIN CITA.** Con esto queda contestada la
**verificacion 8** de la ficha, que el acta 153 declaraba sin contestar.


---

## CORRECCION 35. **EL PASE DE `estado` DE LAS CINCO MESAS, CON SU DISPARADOR MEDIDO EN LA VUELTA QUE LO USA**

**Fecha: 2026-09-02. Vuelta 154, TAREA 5. Autorizada por el acta 153, adjudicacion 6.3.**

**POR QUE NO SE MOVIERON ANTES, Y NO ES UN OLVIDO.** La reserva del acta 139,
3.6 nombra literalmente *"el pase de estado de las once (las seis fusiones y las
cinco remitidas)"*, y **las cinco mesas no estan en esas once**. El ejecutor de
la vuelta 152 no las movio, y el acta 153 se lo cuenta a favor: ampliar la
reserva por cuenta propia habria sido improvisar.

**LO QUE SI HABIA, Y ES LO QUE DISPARA HOY.** Esa misma 3.6 les puso a las mesas
un disparador propio: **"cuando la fase 06 cierre"**. El acta 153, 6.3 lo mide
disparado y lo adjudica; **esta vuelta lo vuelve a medir con su propio
instrumento antes de mover una sola ficha**, que es lo que la regla del
instrumento manda.

**EL DISPARADOR, MEDIDO EN ESTA VUELTA** (`scripts/loop/tallar_estado_de_fase.py
--fase 06_MESAS`, salida
[`loop/SALIDA_V154_T5_DISPARADOR.txt`](../loop/SALIDA_V154_T5_DISPARADOR.txt)):
**16 de 16 operaciones del catalogo de la fase 06 con destino CUMPLIDO, 0 sin
cumplir**, y **las cinco mesas entre ellas**.

**LAS CINCO, NOMBRADAS:** `OP-M-01`, `OP-M-02`, `OP-M-03`, `OP-M-04`, `OP-M-05`.

**EL PASE ES POR FICHA Y NO POR DECRETO.** El encargo lo fija: la adjudicacion
cubre a las que el disparador alcance. Se mueve la ficha cuya fila diga
`CUMPLIDO` y se deja quieta la que no, y las que no se mueven se nombran. En
esta corrida se movieron **5 de 5**; sin mover: **ninguna**.

**EL ACTO Y SUS GUARDAS:** uno solo, las cinco a la vez, con el **conteo antes y
despues**, el **esquema comprobado por assert** (71 fichas, un solo juego de 18
claves) y la **guarda de cifras del plan re corrida**, exactamente el molde de
las vueltas 131, 136 y 152.

**LA CONVENCION DEL SILENCIO NO SE MUEVE EN LA MISMA VUELTA EN QUE SE CUENTA:**
se cuenta con la **lista A**, la que vive en
`vuelta150_3_relectura_expediente.py:declara_su_estado`. Cambiar la vara y el
sujeto a la vez es la trampa que la vuelta 152 ya evito.
