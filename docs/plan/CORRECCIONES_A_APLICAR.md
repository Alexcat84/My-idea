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
