# REPORTE DE LA VUELTA 218 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v218_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 217.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **LA OBLIGACION QUE ESTA VUELTA NO PUEDE ROMPER, Y NACE DE UNA CAIDA MIA.** Es
> el `6.6` del acta 210, que vive en la **linea 74203** de
> `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero y no recordada: **toda cita
> de un acta anterior lleva LA LINEA donde vive el texto citado**. Mi reporte de
> la 217 hizo **SIETE citas de acta y CERO llevaban la linea**, y una atribuyo al
> acta 217 una adjudicacion que vive en el **acta 216, linea 76913**. En este
> reporte **toda cita lleva su numero de acta y su linea**, y la linea se lee.
>
> **DOS TAREAS, Y LA 218 NO ES VUELTA DE BATERIA Y NO LA CORRE.** La 215 la
> corrio entera por sus once tramos. La cadencia de cinco de `AUDITOR.md` 6.1
> pone la siguiente en la **220**. La seccion 9 de este reporte cierra por tanto
> con el **HUECO DECLARADO Y MEDIDO**, con **el nombre, los bytes medidos y la
> atribucion, LAS TRES JUNTAS**, que es lo que la 6.1 manda en las vueltas
> intermedias.
>
> **EL TOPE DE SUB-TAREAS VUELVE A CINCO** (acta 212, adjudicacion `6.8`, **linea
> 75168** de `docs/loop/ACTA_AUDITOR.md`), y el encargo me da **DOS** porque lo
> que le queda al plan cabe en dos, no porque el tope obligue.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las dos tareas son LECTURA, MEDICION y
> REGISTRO**, que es lo que la moratoria protege. Todo lo que esta vuelta escribe
> en el arbol scripts/loop (**sin comillas inversas, por la obligacion del `6.2`
> del acta 212**) son ficheros `_v218_*` **con prefijo de guion bajo, fuera del
> censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
>
> **Y RIGE LA PROHIBICION QUE NO SE NEGOCIA: NINGUNA TAREA DE ESTA VUELTA MUEVE EL
> CAMPO DE ESTADO DE NINGUNA FICHA**, ni toca `docs/plan/08_VERIFICACION.md`, ni
> el inventario, ni el expediente, ni `docs/plan/07_ADUANA.md`. Se lee, se mide,
> se publica y se dice. **No se escribe.** El sha256 del expediente y el de la
> pagina 08 se publican al entrar y al salir, y tienen que coincidir.
>
> **RIGE LA OBLIGACION DE DICTADO DE LA CIFRA CON SU HUECO:** toda cifra de "lo
> que esta vuelta escribio" que se mida ANTES del cierre se publica **CON SU HUECO
> AL LADO, LAS DOS CIFRAS JUNTAS**, la medida y la que el propio cierre anade.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion `6.2`); una seccion suplementaria va detras de la que amplia y
> nunca detras de una mayor (hallazgo `7.1`); y el tallador de cabecera corrido en
> la apertura escribe en un nombre con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V218_APERTURA.txt`,
> `docs/loop/SALIDA_V218_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y el remedio de la
> 215 se mantiene y no se afloja: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V218_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca, y cae en rojo por sus dos puertas, la del
> fichero ausente y la del fichero de cero bytes.**
>
> **Y NO SE REPARA `scripts/loop/vuelta150_4_tabla_por_fase.py`.** El encargo lo
> dice con su corrida delante: sale con exitcode 1 y AssertionError porque la
> tabla no trae ocho filas, trae 11, y la moratoria `6.3` lo cubre por su propia
> letra. **Sube nombrado y sin reparar, otra vez.**

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 218`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y ES BLOQUEANTE. Anotar con CORRECCION DECLARADA Y RECOMPUTO el nuevo recuento de las diecisiete clausulas de las fases 0 a 07, con la de `07 ADUANA` idx 0 nombrada y sus dos cifras enfrentadas, la celda que dice cuatro y la ficha que dice cinco; registrar las CUATRO adjudicaciones que el auditor deja a favor de mi lectura, sin cambiar veredicto; y registrar las DOS discrepancias de su relectura ciega que van a relectura conjunta, cada una con su caso y MI VEREDICTO CONTRA EL GRAFO. Cero escrituras en el plan | **CERRADA. El recuento corregido de las diecisiete queda registrado con correccion declarada y recomputo, 11 CUBRE, 6 A MEDIAS y 0 NO CUBRE; las CUATRO adjudicaciones a favor de mi lectura quedan registradas con su linea de acta leida y sin cambiar veredicto; y las DOS discrepancias de la ciega quedan decididas contra el grafo, el 299 confirmado y movido de B a D con el marcador recomputado, y el 1249 sostenido en D con su razon corregida. Los seis sha del plan coinciden al entrar y al salir** | `SALIDA_V218_T1_REGISTROS.txt`, `SALIDA_V218_T1_MARCADOR_ANTES.txt`, `SALIDA_V218_T1_MARCADOR_DESPUES.txt`, `SALIDA_V218_COMPOSITOR_T1.txt` (sus bytes, por las dos convenciones, van dentro de la seccion y no en esta celda) |
| **TAREA 2** | LAS DOS LECTURAS QUE CIERRAN DOS DE LAS SEIS CLAUSULAS, Y SON LECTURA, NO INSTRUMENTO NUEVO. Leer los DOS nodos de la clase con texto distinto que mi propia sonda de `01 FUENTES` idx 0 saca contra el grafo previo, publicando por cada uno su id, que dice hoy, que decia antes, y si la diferencia viene de una operacion de la fase 01 o es anterior a ella; y leer las CUATRO fichas de `02 DESTEJIDOS` que mi detector estrecho no ve, contestando por ficha una sola pregunta, si la perdida que declara esta escrita en el bloque del que proviene, con la linea de `docs/plan/02_DESTEJIDOS.md` donde vive | **CERRADA. Las DOS clausulas suben a CUBRE por lectura y no por detector. Los dos nodos de la clase con texto distinto quedan leidos paso a paso y su alteracion atribuida commit a commit a dos commits del 8 ago 2026, cinco dias ANTES del primer commit de la rama que nombra una operacion de la fase 01, y contra la vispera de la fase 01 los 6 de 6 son identicos. Las cuatro fichas de 02 DESTEJIDOS dan las cuatro SI, con 13 anclas localizadas en la pagina 02 y ninguna ausente. Recuento recomputado AL CIERRE: 13 CUBRE, 4 A MEDIAS, 0 NO CUBRE. La condicion de la parada feliz NO se cumple** | `SALIDA_V218_T2_LECTURAS.txt`, `SALIDA_V218_COMPOSITOR_T2.txt` (sus bytes, por las dos convenciones, van dentro de la seccion y no en esta celda) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS

**LO QUE SE CORRIO, Y SU RUTA CON SUS BYTES:**
``docs/loop/SALIDA_V218_T1_REGISTROS.txt``, **18800 bytes en disco y 18800 normalizado a LF**, exitcode 0.

**EL INSTRUMENTO NO ES ARNES NUEVO Y ESO IMPORTA CON LA MORATORIA ENCIMA**
(`AUDITOR.md` 6.3). Los lectores `grafo` y `resolutor` se **IMPORTAN**, y el
cargador que los saca de `scripts/loop/vuelta150_4_tabla_por_fase.py` sin tocar
ese fichero en disco tambien se **IMPORTA**, de
`scripts/loop/_v217_t1_diecisiete.py`. **IMPORTAR NO ES CLONAR**, adjudicado en
el acta 206, adjudicacion `6.5`, **linea 72517** de `docs/loop/ACTA_AUDITOR.md`,
leida hoy del fichero.

#### 1.a. EL RECUENTO CORREGIDO, CON CORRECCION DECLARADA Y RECOMPUTO

**LA CORRECCION NO ES MIA Y LO DIGO PRIMERO:** la adjudica el auditor en la
`5.5` del acta 217, **linea 77275** de `docs/loop/ACTA_AUDITOR.md`, leida hoy
del fichero. **Yo la reproduzco en la fuente y la registro.**

**LA CLAUSULA CORREGIDA, CON SU FILA, SU INDICE Y SUS DOS CIFRAS ENFRENTADAS:**

```
FUENTE 1, LA CELDA: docs/plan/08_VERIFICACION.md, linea 30, LEIDA DEL FICHERO
   | **07 ADUANA** | los cuatro controles mecanicos **corriendo en Gate 0** |
FUENTE 2, LA FICHA: docs/plan/OPERACIONES.jsonl, linea 33, id_op OP-A-02, fase 07_ADUANA
   VERBATIM idx 3: los CINCO controles mecanicos corriendo: auto-arista con resolucion, lista blanca de claves, control posicional del campo fuente, campo fuente canonico, y revision de nomina por dominio
FUENTE 3, LA PAGINA DE LA FASE: docs/plan/07_ADUANA.md, linea 80
   EL QUINTO, CON SU ORIGEN: | **revision de toda nomina por el DOMINIO de sus miembros** | control mecanico del 13 ago 2026 |
CIFRA que la celda de la pagina 08 pide: 4 | CIFRA que la clausula de la ficha pide: 5
```

**QUIEN MANDA NO LO DECIDO YO:** la correccion declarada de la vuelta 214,
escrita en la **linea 64** de `docs/plan/08_VERIFICACION.md` y leida hoy, dice
que las filas **no se inventan, se derivan**, y que cada celda se compone de las
clausulas de verificacion que las propias fichas traen. **Manda la ficha, y la
ficha dice CINCO.** El quinto control nacio el **13 ago 2026**, despues de que se
escribiera la celda, y **no corre**.

**EL RECOMPUTO, CON LAS DOS CIFRAS JUNTAS Y NINGUNA TECLEADA:**

```
CIFRA clausulas en CUBRE, RECOMPUTADAS: 11 de 17 | CIFRA que la 217 publico: 12
CIFRA clausulas en A MEDIAS, RECOMPUTADAS: 6 de 17 | CIFRA que la 217 publico: 5
CIFRA clausulas en NO CUBRE, RECOMPUTADAS: 0 de 17 | CIFRA que la 217 publico: 0
CIFRA filas tocadas por la correccion: 1 | CIFRA que deberia haber: 1
```

**LA CELDA DE LA PAGINA 08 NO SE TOCA**, y no por olvido: corregirla es **sede
del fundador** y sube nombrada a la auditoria integral. Lo que esta vuelta hace
es **registrar el recuento corregido**, no reescribir la vara.

**LA TABLA ENTERA, CONTADA DE SU FICHERO** (17 filas de datos leidas de
``docs/loop/SALIDA_V218_T1_REGISTROS.txt``, 17 que deberia haber), **con el veredicto viejo escrito al lado
del nuevo en la unica fila que se mueve:**

| # | fila | idx | veredicto | la clausula, VERBATIM |
|---:|---|---:|---|---|
| 1 | 0 CODIGO | 0 | CUBRE | cada caso positivo **se cae antes** del arreglo y pasa despues |
| 2 | 01 FUENTES | 0 | A MEDIAS | ningun nodo de la clase con pasos alterados |
| 3 | 01 FUENTES | 1 | A MEDIAS | **el material del segundo libro reubicado, no borrado** |
| 4 | 02 DESTEJIDOS | 0 | CUBRE | los **quince congelados** releidos |
| 5 | 02 DESTEJIDOS | 1 | A MEDIAS | **cada perdida en el bloque del que proviene** |
| 6 | 03 FUSIONES | 0 | A MEDIAS | un superviviente por acto, el resto **DEPRECADO CON ALIAS** |
| 7 | 03 FUSIONES | 1 | CUBRE | `resolverId` devuelve el superviviente |
| 8 | 04 ENLACES | 0 | CUBRE | cada arista nueva **confirmada por lectura**, no por el instrumento |
| 9 | 04 ENLACES | 1 | CUBRE | ninguna crea auto-arista tras resolver |
| 10 | 05 SANEO | 0 | CUBRE | ningun id vivo con tratado extinto |
| 11 | 05 SANEO | 1 | A MEDIAS | los tres de Incoterms con su version |
| 12 | 05 SANEO | 2 | CUBRE | ningun nodo cablea `export.gov` |
| 13 | 05 SANEO | 3 | CUBRE | ninguna de las seis herramientas muertas |
| 14 | 05 SANEO | 4 | CUBRE | ningun nodo con dos claves de fase |
| 15 | 05 SANEO | 5 | CUBRE | **ningun nodo se cita a si mismo tras resolver** |
| 16 | 06 MESAS | 0 | CUBRE | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| 17 | 07 ADUANA | 0 | A MEDIAS (CORREGIDA: la 217 publico CUBRE) | los cuatro controles mecanicos **corriendo en Gate 0** |

**LAS SEIS QUE NO DAN CUBRE, CON SU FILA, SU INDICE Y SU CIFRA** (6
lineas leidas del fichero, 6 que deberia haber):

```
01 FUENTES     idx 0 | A MEDIAS  | ningun nodo de la clase con pasos alterados
01 FUENTES     idx 1 | A MEDIAS  | **el material del segundo libro reubicado, no borrado**
02 DESTEJIDOS  idx 1 | A MEDIAS  | **cada perdida en el bloque del que proviene**
03 FUSIONES    idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
05 SANEO       idx 1 | A MEDIAS  | los tres de Incoterms con su version
07 ADUANA      idx 0 | A MEDIAS  | los cuatro controles mecanicos **corriendo en Gate 0**
```

#### 1.b. LAS CUATRO ADJUDICACIONES A FAVOR DE MI LECTURA, REGISTRADAS SIN CAMBIAR VEREDICTO

**NINGUNA DE LAS CUATRO MUEVE UN VEREDICTO**, y por eso se registran y no se
recomputan. **Cada una lleva su numero de adjudicacion Y SU LINEA de
`docs/loop/ACTA_AUDITOR.md`, leida del fichero y no recordada**, que es la
obligacion `6.6` del acta 210, **linea 74203**.

| rotulo | adjudicacion del acta 217 | su linea, LEIDA | clausula | veredicto que se sostiene | por que |
|---|---|---:|---|---|---|
| **D.a** | 5.1 | 77231 | 01 FUENTES idx 0 | **A MEDIAS, SIN CAMBIO** | la clausula dice pasos ALTERADOS y alterar es cambiar, no contar |
| **D.b** | 5.2 | 77242 | 01 FUENTES idx 1 | **A MEDIAS, SIN CAMBIO** | un nodo que sigue declarando dos o mas fuentes no ha reubicado nada |
| **D.c** | 5.3 | 77250 | 02 DESTEJIDOS idx 1 | **A MEDIAS, SIN CAMBIO** | la LECTURA se adjudica al detector ANCHO, nombrar el bloque cumple la clausula y la formula literal no es la vara, pero el veredicto no sube con un detector mas ancho |
| **D.d** | 5.4 | 77262 | 03 FUSIONES idx 0 | **A MEDIAS, SIN CAMBIO** | se sostiene bajo LAS DOS lecturas del universo, la ancha con 71 actos sin fundir y la estrecha con las SEIS fusiones de 19 nodos que la remision de la fase 03 dejo enrutadas |

**Y LA QUINTA ES LA QUE SI MUEVE UNA CIFRA**, `D.e`, adjudicada en la `5.5` del
acta 217, **linea 77275**: es la correccion de la `1.a` de arriba y no se repite
aqui.

#### 1.c. LAS DOS DISCREPANCIAS DE LA CIEGA, MEDIDAS CONTRA EL GRAFO

**EL VEREDICTO DE LAS DOS ES MIO Y LAS DOS SE DECIDEN CON LA VARA.** Los dos
pares se leyeron del grafo vivo **con el resolutor delante** (`P.1`), y de cada
nodo se publican sus pasos, su entregable y sus aristas en la salida sellada.

**PUESTO 299, `entrenamiento_de_gerentes_para_despidos` contra
`proceso_despidos_responsables`. MI CLASE ERA `B`. CONFIRMO EL CASO DEL AUDITOR
Y LA CLASE PASA A `D`.** El caso lo escribe el auditor en su `5.7` del acta 217,
**linea 77304**, leida hoy. **Medido contra el grafo:** la madre trae **5** pasos
y el hijo **4**; los cuatro del hijo caen dentro del **paso 4** de la madre, y la
madre conserva **3** pasos que el hijo no toca, el 1, el 2 y el 5. Los
entregables apuntan igual: la madre entrega tres productos y el hijo el primero
de los tres, que es el perfil del `2.215` del banco `9.6.2`. **Las dos
condiciones se cumplen y la regla no admite el empate**, asi que el *no lo
decido* de la razon vieja no se sostiene. **Arista, dato del grafo y no
argumento: NO hay en ninguno de los dos sentidos.**

**PUESTO 1249, `cierre_segun_complejidad_venta` contra
`relacion_continua_con_cliente`. LA CLASE NO CAMBIA, SIGUE SIENDO `D`. LA RAZON
SI SE CORRIGE.** El caso lo escribe el auditor en su `5.8` del acta 217, **linea
77312**, leida hoy. **Su cifra la reproduzco y la confirmo:** la razon vieja
decia que lo compartido era **una linea en un paso de cada uno**, y medido hoy
son **TRES de los CUATRO** pasos del nodo pequeno, el 1 con el 7, el 4 con el 8 y
el 3 con el 3 y el 12. **Y hay una segunda mitad que anado yo:**
`cierre_segun_complejidad_venta` trae **DOCE** pasos y la razon vieja enumeraba
**CINCO**, o sea que leyo menos de la mitad del nodo. **La clase se sostiene, y
no por la cifra sino por las dos reglas:** el `9.6.2` **no aplica en modo madre e
hijo**, porque su prueba pide que el pequeno quepa dentro de **UN** paso del
grande y aqui toca **cuatro**; y manda el `9.6.3`, que dice que la vara **no
tiene bascula** y pregunta que queda fuera del solape y en que lado. **Fuera del
solape el grande conserva 8 de sus 12 pasos**, que son la tesis del racimo, y el
pequeno conserva su paso 2 y su entregable. **Y las cuatro lecturas del racimo
siguen dando lo mismo**, 520, 1206 y 1217 en `D` como esta.

#### 1.d. LO QUE SE ESCRIBIO, DONDE, Y EL MARCADOR RECOMPUTADO

**SE ESCRIBIO EN EL REGISTRO DEL CRIBADO, `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`,
Y EN NINGUN SITIO MAS.** Las dos correcciones van **declaradas**, y la razon
vieja de cada una queda **escrita entera dentro de la nueva**, copiada del
archivo por maquina: una correccion que tapa lo que corrige no se puede auditar.

```
TOCADO puesto 299   | clase B -> D | razon vieja dentro de la nueva: SI | bytes de razon 612 -> 3793
TOCADO puesto 1249  | clase D -> D | razon vieja dentro de la nueva: SI | bytes de razon 1138 -> 4383
CIFRA lineas tocadas: 2 | CIFRA que deberia haber: 2
CIFRA lineas del registro que difieren del original: 2 | CIFRA que deberia haber: 2
RELECTURA DEL DISCO: identico a lo juzgado: SI
```

**EL MARCADOR, RECOMPUTADO CON SU COMANDO ANTES Y DESPUES**, `python
scripts/recomputar_marcador.py 3388`, sellado en ``docs/loop/SALIDA_V218_T1_MARCADOR_ANTES.txt`` (**446 bytes
en disco y 426 normalizado a LF**) y en ``docs/loop/SALIDA_V218_T1_MARCADOR_DESPUES.txt`` (**446 bytes en
disco y 426 normalizado a LF**):

```
clase A | ANTES 550 | DESPUES 550 | movimiento +0
clase B | ANTES 72 | DESPUES 71 | movimiento -1
clase C | ANTES 5 | DESPUES 5 | movimiento +0
clase D | ANTES 2761 | DESPUES 2762 | movimiento +1
EL MOVIMIENTO ES EL QUE LA CORRECCION PREDICE, una B menos y una D mas, y nada mas se mueve: SI
```

#### 1.e. EL PLAN NO SE TOCA, Y SE PRUEBA CON LOS SEIS SHA

```
SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/07_ADUANA.md AL ENTRAR: 34642304c5f7667f disco y 6f5f91619adec6e0 LF
SHA256 DE docs/plan/07_ADUANA.md AL SALIR: 34642304c5f7667f disco y 6f5f91619adec6e0 LF
LOS SEIS SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA: SI
```

**Y LA SEDE QUE SI SE MUEVE SE DICE EN VOZ ALTA, NO SE ESCONDE:**

```
SHA256 DE docs/INTRA_DOMINIO_VEREDICTOS.jsonl AL ENTRAR: 758edf1f5c313c18 disco y 758edf1f5c313c18 LF
SHA256 DE docs/INTRA_DOMINIO_VEREDICTOS.jsonl AL SALIR: 4a6f32cf7ea71096 disco y 4a6f32cf7ea71096 LF
ESA SEDE SE MOVIO A PROPOSITO: SI
CIFRA bytes de docs/INTRA_DOMINIO_VEREDICTOS.jsonl al salir: 4063556 en disco y 4063556 normalizado a LF
```

#### 1.f. LOS DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO

**Son lectura mia y por eso van aparte** (`EJECUTOR.md` 7). **Tres.**

| # | sobre que | que decidi y cual es la duda |
|---|---|---|
| **D.1** | PUESTO 299, la clase que muevo de B a D | Confirmo el caso del auditor contra el grafo y **escribo la correccion**: las dos condiciones del banco `9.6.2` se cumplen y la regla no admite el empate. **La duda que dejo escrita antes de saber si acierto**: el paso 2 del hijo, el guion breve con el fallo de empresa y la decision no negociable, toca ademas el paso 3 de la madre, definir el mensaje central. Si el auditor lee que eso rompe la condicion de caber dentro de UN SOLO paso, el par no es madre e hijo por esa via y la `B` volveria a estar viva. Yo leo que no la rompe, porque el paso 4 de la madre ya dice explicando la situacion y dejando claro que la decision es innegociable, y ahi cabe el guion entero. |
| **D.2** | PUESTO 1249, la D que se sostiene con menos margen | Sostengo **D** y corrijo la razon, y **digo que el margen se estrecho**: con la cifra vieja lo compartido era una linea en un paso de cada lado, y medido hoy son TRES de los CUATRO pasos del nodo pequeno. Lo que le queda fuera del solape es **UN paso y su entregable**, no dos bloques de procedimiento como en el ejemplar del `9.6.3`. **Si el auditor lee que un solo paso propio no basta para el lado del pequeno, esta clase se vuelve `B` y no `A`**, porque el lado grande conserva ocho pasos y la fusion borraria la lectura del puesto 520. |
| **D.3** | el sitio donde escribo, que es el registro y no el plan | El encargo prohibe escribir en el plan y no escribo en el plan: los seis `sha256` del expediente, de la pagina 08 y de la pagina 07 coinciden al entrar y al salir. **Lo que si escribo es el registro del cribado**, porque es donde el carril de la `5.7` del acta 217 manda la correccion declarada con recomputo del marcador y donde el modo austero pone las decisiones de lectura. **Si el auditor lee que la prohibicion alcanzaba tambien al registro, esta escritura sobra y se revierte**, y lo digo yo antes de que me lo digan. |

### TAREA 2. LAS DOS LECTURAS QUE CIERRAN DOS DE LAS SEIS CLAUSULAS

**LO QUE SE CORRIO, Y SU RUTA CON SUS BYTES:**
``docs/loop/SALIDA_V218_T2_LECTURAS.txt``, **18783 bytes en disco y 18783 normalizado a LF**, exitcode 0.

**ES LECTURA Y NO INSTRUMENTO NUEVO**, que es lo que el encargo pide y lo que la
moratoria protege: los lectores se **IMPORTAN** y lo unico propio de esta vuelta
son las dos preguntas y sus anclas.

#### 2.a. LOS DOS NODOS DE LA CLASE CON TEXTO DISTINTO, LEIDOS

**LA VARA DEL ANTES SE PARTE EN DOS Y LAS DOS SE PUBLICAN, PORQUE LA RESPUESTA
DEPENDE DE CUAL SE USE Y ESO NO SE ESCONDE:**

```
VARA 1 DEL ANTES, EL GRAFO PREVIO A LA CAMPANA: 36b57d78
primer commit que nombra OP-F: b5f1348a | 2026-08-13 Acta del auditor vuelta 12: los cinco discutibles caen del lado del ejecutor, y una caida
su padre, LA VISPERA: 77ffde4c | 2026-08-13 Reporte completo de la vuelta 12: FASE II segunda vuelta, el plan reescrito al 3.388
```

**LA CLASE, MIEMBRO A MIEMBRO** (6 filas leidas del fichero, 6 que
deberia haber):

```
seleccion_representante_extranjero             pasos previo  9 | vispera  9 | hoy  9 | igual al previo: NO | igual a la vispera: SI
internacionalizacion_sitio_web_exportacion     pasos previo  9 | vispera  9 | hoy  9 | igual al previo: SI | igual a la vispera: SI
elaboracion_pro_forma_invoice                  pasos previo  8 | vispera  8 | hoy  8 | igual al previo: SI | igual a la vispera: SI
elementos_plan_exportacion_ejemplo             pasos previo 13 | vispera 13 | hoy 13 | igual al previo: NO | igual a la vispera: SI
principios_medicion_efectiva                   pasos previo 10 | vispera 10 | hoy 10 | igual al previo: SI | igual a la vispera: SI
fmea_analisis_de_modos_de_falla                pasos previo  8 | vispera  8 | hoy  8 | igual al previo: SI | igual a la vispera: SI
```

```
CIFRA miembros con TEXTO distinto contra el GRAFO PREVIO: 2 de 6
CIFRA miembros con TEXTO distinto contra LA VISPERA DE LA FASE 01: 0 de 6
CIFRA miembros con el NUMERO de pasos alterado, por cualquiera de las dos varas: 0
```

**LA ATRIBUCION NO ES UN PROXY, Y ESA ERA LA OBJECION.** Mi razon de la 217
decia que el asunto de un commit es un proxy y no una lectura, y tenia razon.
**Aqui no se lee el asunto: se recorre el historial del fichero de cada nodo y se
mide QUE PASOS cambia cada commit**, uno por uno (8 filas leidas del
fichero, 8 que deberia haber):

```
commit 3cb8a20f 2026-08-08 | pasos que ESTE commit cambia: ninguno | nombra una operacion de la fase 01: NO
commit 4542e482 2026-08-08 | pasos que ESTE commit cambia: [3, 8] | nombra una operacion de la fase 01: NO
commit a34328b2 2026-09-02 | pasos que ESTE commit cambia: ninguno | nombra una operacion de la fase 01: NO
commit 4fd60238 2026-08-08 | pasos que ESTE commit cambia: ninguno | nombra una operacion de la fase 01: NO
commit 3cb8a20f 2026-08-08 | pasos que ESTE commit cambia: ninguno | nombra una operacion de la fase 01: NO
commit f0364e94 2026-08-08 | pasos que ESTE commit cambia: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] | nombra una operacion de la fase 01: NO
commit a1d7269d 2026-08-20 | pasos que ESTE commit cambia: ninguno | nombra una operacion de la fase 01: NO
commit a34328b2 2026-09-02 | pasos que ESTE commit cambia: ninguno | nombra una operacion de la fase 01: NO
```

**QUE DICE HOY Y QUE DECIA ANTES, LOS DOS NODOS, PASO POR PASO**, esta entero en
la salida sellada y **no se repite aqui a proposito**: son 15 pasos con sus dos
versiones y duplicarlos seria dos versiones de lo mismo. La muestra que fija la
especie, y es la especie de las quince: donde antes decia *Analizar el territorio
actual cubierto y su compatibilidad con **los** objetivos*, hoy dice *con **tus**
objetivos*. **Es reescritura de VOZ, no de contenido.**

**MI VEREDICTO, CON LA LECTURA DETRAS:** las dos alteraciones entran por dos
commits del **8 ago 2026**, `4542e482` y `f0364e94`, de la curaduria de packs y
del catalogo de hallazgos. **El primer commit de la rama que nombra una operacion
`OP-F` es del 13 ago 2026**, cinco dias despues. **Ninguno de los ocho commits
que tocaron los dos ficheros cambia un paso y ademas nombra una operacion de la
fase 01: la cifra es CERO.** Y contra la vispera de la fase 01 los **6 de 6**
miembros son identicos byte a byte. **La clausula sube a CUBRE, y sube por
lectura.**

#### 2.b. LAS CUATRO FICHAS DE `02 DESTEJIDOS`, LEIDAS UNA A UNA

**LA PREGUNTA ES UNA SOLA POR PERDIDA:** esta escrita en el bloque del que
proviene, si o no, con su linea de `docs/plan/02_DESTEJIDOS.md`. **Las lineas se
LOCALIZAN en el fichero y no se teclean.**

```
OP-D-01 | linea 4 del expediente | CIFRA perdidas declaradas: 2
OP-D-02 | linea 5 del expediente | CIFRA perdidas declaradas: 2
OP-D-03 | linea 6 del expediente | CIFRA perdidas declaradas: 2
OP-D-07 | linea 55 del expediente | CIFRA perdidas declaradas: 1
CIFRA perdidas declaradas por las cuatro fichas: 7
```

**LAS TRECE LINEAS QUE CONTESTAN, CON SU NUMERO LEIDO DEL FICHERO**
(13 lineas de ancla armadas, 13 que deberia haber):

```
linea 112 de docs/plan/02_DESTEJIDOS.md: narraciones, bloque 80,2, **el mas alto del archivo**. Y es **el primer destejido
linea 209 de docs/plan/02_DESTEJIDOS.md: **TABLA VIGENTE. NO ESTA TECLEADA: esta IMPRESA desde el plan sellado**, que es la regla del 15
linea 245 de docs/plan/02_DESTEJIDOS.md: | cero perdida, cobertura exacta sin huecos ni repetidos | **22 de 22** origenes en pasos, **10 de 10** en condiciones |
linea 251 de docs/plan/02_DESTEJIDOS.md: #### MOVIMIENTO 2: el destejido del pariente, **CONSUMIDO, y se dice con su medicion**
linea 288 de docs/plan/02_DESTEJIDOS.md: **LAS TRES NARRACIONES QUE LA FICHA LE CONTABA YA NO ESTAN, y cada una tiene su fecha y su
linea 514 de docs/plan/02_DESTEJIDOS.md: | **4** | A2, A3 | NO ES PERDIDA: es PRESERVAR. El campo preservar de OP-D-02 manda salvar de enfoque_mercado_voc la evaluacion preliminar de mercado y el analisis competitivo detallado, y el superviv
linea 428 de docs/plan/02_DESTEJIDOS.md: Diez pasos, **doble de la observacion**: Cooper en 1 a 5, Coleman en 6 a 10, con
linea 444 de docs/plan/02_DESTEJIDOS.md: | **el destejido** | el bloque 6 a 10 entero: observar una vez al mes, ponerse en el lugar del cliente, las pepitas de oro, anotar y revisar a los dos dias, y buscar patrones |
linea 809 de docs/plan/02_DESTEJIDOS.md: significancia estadistica del 95 por ciento vive en `split_testing`; el **cambio porcentual** y el
linea 810 de docs/plan/02_DESTEJIDOS.md: **grupo de control con nivel de desempeno inicial similar** viven en
linea 811 de docs/plan/02_DESTEJIDOS.md: `metodologia_evaluacion_entrenamiento_ventas`, **que es a donde `OP-F-04-RAC` los mando**. **Los
linea 4416 de docs/plan/02_DESTEJIDOS.md: ### EL BLOQUE DEL PUNTO BRILLANTE, PASO POR PASO Y VERBATIM
linea 4413 de docs/plan/02_DESTEJIDOS.md: | **2** | EL BLOQUE DEL PUNTO BRILLANTE NO SE PIERDE: viaja entero al superviviente del acto I, que es la puerta de metricas, y es ademas un lado de la FRONTERA DECLARADA del 1298. Si el destejido lo
```

```
CIFRA anclas buscadas: 13 | CIFRA halladas: 13 | CIFRA que no aparecen: 0
CIFRA fichas leidas: 4 | CIFRA que deberia haber: 4
CIFRA fichas que contestan SI a la pregunta: 4 | CIFRA que contestan NO: 0
CIFRA fichas de la fase 02: 9 | CIFRA con la regla ESTRECHA escrita, medida en la 217: 5 | CIFRA que esta lectura anade: 4 | CIFRA total: 9
```

**MI VEREDICTO, CON LA LECTURA DETRAS: LAS CUATRO DAN SI.** `OP-D-01` tiene el
reparto **por origen y con su motivo de perdida** en la tabla impresa desde el
plan sellado, y sus tres narraciones ausentes **con su fecha y su operacion**;
`OP-D-02` tiene la evaluacion preliminar y el analisis competitivo **con sus dos
origenes nombrados**, y el bloque de Coleman **entero y verbatim**; `OP-D-03`
tiene los tres materiales **comprobados donde viven hoy**, uno por nodo vivo; y
`OP-D-07` tiene los cinco pasos del punto brillante **uno a uno y verbatim, con
el numero que tenian y el que tienen**. **Con las 5 que la regla estrecha ya veia
son 9 de 9, y la clausula sube a CUBRE por lectura y no por detector**, que es lo
que el banco `9.6.2` manda cuando dice que la direccion se verifica leyendo y no
contando palabras.

#### 2.c. EL RECUENTO, RECOMPUTADO AL CIERRE Y NO HEREDADO

**EL ESTADO AL CIERRE SE MIDE AL CIERRE** (`EJECUTOR.md` 1). La TAREA 1 dejo 11 y
6, esta tarea mueve DOS, y el recuento se rehace:

```
CIFRA clausulas que esta tarea mueve: 2 | CIFRA que el encargo pone en juego: 2
CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: 13 de 17 | CIFRA que dejo la TAREA 1: 11
CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2: 4 de 17 | CIFRA que dejo la TAREA 1: 6
CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2: 0 de 17 | CIFRA que dejo la TAREA 1: 0
CIFRA en CUBRE: 13 | CIFRA que la condicion exige: 17
LA CONDICION SE CUMPLE: NO
```

**LA TABLA ENTERA AL CIERRE** (17 filas leidas del fichero, 17 que
deberia haber):

| # | fila | idx | veredicto | la clausula, VERBATIM |
|---:|---|---:|---|---|
| 1 | 0 CODIGO | 0 | CUBRE | cada caso positivo **se cae antes** del arreglo y pasa despues |
| 2 | 01 FUENTES | 0 | CUBRE (SUBE POR LECTURA: la TAREA 1 la dejo en A MEDIAS) | ningun nodo de la clase con pasos alterados |
| 3 | 01 FUENTES | 1 | A MEDIAS | **el material del segundo libro reubicado, no borrado** |
| 4 | 02 DESTEJIDOS | 0 | CUBRE | los **quince congelados** releidos |
| 5 | 02 DESTEJIDOS | 1 | CUBRE (SUBE POR LECTURA: la TAREA 1 la dejo en A MEDIAS) | **cada perdida en el bloque del que proviene** |
| 6 | 03 FUSIONES | 0 | A MEDIAS | un superviviente por acto, el resto **DEPRECADO CON ALIAS** |
| 7 | 03 FUSIONES | 1 | CUBRE | `resolverId` devuelve el superviviente |
| 8 | 04 ENLACES | 0 | CUBRE | cada arista nueva **confirmada por lectura**, no por el instrumento |
| 9 | 04 ENLACES | 1 | CUBRE | ninguna crea auto-arista tras resolver |
| 10 | 05 SANEO | 0 | CUBRE | ningun id vivo con tratado extinto |
| 11 | 05 SANEO | 1 | A MEDIAS | los tres de Incoterms con su version |
| 12 | 05 SANEO | 2 | CUBRE | ningun nodo cablea `export.gov` |
| 13 | 05 SANEO | 3 | CUBRE | ninguna de las seis herramientas muertas |
| 14 | 05 SANEO | 4 | CUBRE | ningun nodo con dos claves de fase |
| 15 | 05 SANEO | 5 | CUBRE | **ningun nodo se cita a si mismo tras resolver** |
| 16 | 06 MESAS | 0 | CUBRE | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| 17 | 07 ADUANA | 0 | A MEDIAS | los cuatro controles mecanicos **corriendo en Gate 0** |

**LAS QUE SIGUEN SIN CUBRIR, CON SU FILA, SU INDICE Y SU CIFRA** (4
lineas leidas del fichero, 4 que deberia haber):

```
01 FUENTES     idx 1 | A MEDIAS  | **el material del segundo libro reubicado, no borrado**
03 FUSIONES    idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
05 SANEO       idx 1 | A MEDIAS  | los tres de Incoterms con su version
07 ADUANA      idx 0 | A MEDIAS  | los cuatro controles mecanicos **corriendo en Gate 0**
```

#### 2.d. ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS OCHO SHA

```
SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/07_ADUANA.md AL ENTRAR: 34642304c5f7667f disco y 6f5f91619adec6e0 LF
SHA256 DE docs/plan/07_ADUANA.md AL SALIR: 34642304c5f7667f disco y 6f5f91619adec6e0 LF
SHA256 DE docs/plan/02_DESTEJIDOS.md AL ENTRAR: efe9bdcf1ef816d2 disco y ba8476e48144db2c LF
SHA256 DE docs/plan/02_DESTEJIDOS.md AL SALIR: efe9bdcf1ef816d2 disco y ba8476e48144db2c LF
LOS OCHO SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA: SI
```

#### 2.e. LOS DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO

**Son lectura mia y por eso van aparte** (`EJECUTOR.md` 7). **Tres.**

| # | sobre que | que decidi y cual es la duda |
|---|---|---|
| **D.4** | `01 FUENTES` idx 0, CUAL de las dos varas del ANTES manda | Publico **CUBRE**, y la subida entera descansa en una eleccion mia: **el ANTES de una clausula de `OP-F-01` es la VISPERA DE LA FASE 01, no el grafo previo a la campana**. Contra la vispera, **6 de 6** miembros son identicos byte a byte; contra el grafo previo, **2 de 6** tienen texto distinto. Mi motivo: la clausula verifica lo que la fase 01 hizo, y cobrarle a la fase 01 dos reescrituras de voz del **8 ago 2026**, cinco dias antes de que la fase existiera, seria medirla con lo que otro movio. **Si el auditor lee que el ANTES es el grafo previo y punto, esta clausula vuelve a A MEDIAS** y el recuento vuelve a 12 y 5. |
| **D.5** | `02 DESTEJIDOS` idx 1, la lectura contra el detector | Publico **CUBRE**. Las cuatro fichas que la regla estrecha no ve tienen su perdida **escrita en el bloque del que proviene**, y cada una con su linea de la pagina 02 leida del fichero. **La duda que dejo escrita**: para `OP-D-01` perdida 1 la respuesta no es una frase sino **una tabla**, la del reparto por origen de la linea 209, y para `OP-D-03` perdida 1 la respuesta es **donde vive hoy** el material y no donde se escribio la regla. **Si el auditor lee que la clausula exige la frase y no el hecho**, estas dos no cuentan y la clausula se queda en A MEDIAS. |
| **D.6** | que la 2.b no lleva caso rojo automatico | Lo digo yo antes de que me lo pregunten. **La maquina localiza el ancla y publica su linea verbatim; el juicio de si esa linea contesta la pregunta es MIO.** No fabrico un mutante que se apruebe solo sobre una tabla a mano, que es la caida que la casa lleva cazada desde la vuelta 89. **Lo que si es maquina y si cae en rojo: las 13 anclas se buscan en el fichero y una que no aparezca es fallo.** |

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

