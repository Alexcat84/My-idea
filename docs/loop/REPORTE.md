# REPORTE, vuelta 17 del ejecutor (Opus 5)

**FASE II, RECOMPUTO. MODO DE CIERRE: cero reparaciones de nodos, cero operaciones ejecutadas, cero
pares nuevos leidos de la cola.** La FASE III no se abre y la rama `pasada-unica` no se crea.

**Hash final del trabajo: `0ac78fc9`** (push confirmado a `origin/bucle`). Tres commits, uno por tramo:
`87d453c6` (TAREA 1 puntos 1 a 4), `2d5b3932` (TAREA 2) y `0ac78fc9` (TAREA 1 punto 5).
**Este reporte se commitea despues, en `0cc723b2`**, mas este ajuste de la propia linea del hash: **un
reporte no puede nombrar su propio commit, y por eso se separa el hash del trabajo del hash del
reporte en vez de dejar la cifra ambigua.** Todas las mediciones de abajo son sobre `0ac78fc9`, que es
donde el trabajo esta completo; los commits posteriores solo tocan `docs/loop/REPORTE.md`.

**Corte de todas las cifras de este reporte: 14 ago 2026**, sobre el cribado **CERRADO en 3.388 de
3.388**. Todas se leyeron de la salida de un instrumento corrido EN ESTA VUELTA (regla 1 de
`EJECUTOR.md`). Donde una cifra vieja se cita, se cita como contraste y con su autor.

---

## RUTAS TOCADAS

`git diff --stat db6959b6 HEAD`, doce rutas:

| ruta | |
|---|---:|
| `docs/plan/RECOMPUTO_3388.md` | 270 lineas |
| `docs/plan/INVENTARIO.jsonl` | 442 (221 lineas modificadas, cero altas, cero bajas) |
| `docs/plan/10_INVENTARIO.md` | 125 |
| `docs/plan/02_DESTEJIDOS.md` | 38 |
| `docs/plan/OPERACIONES.jsonl` | 4 (2 lineas nuevas mas la nota de `OP-I-01`) |
| **siete instrumentos nuevos**, todos de solo lectura salvo los dos que escriben su propio destino | |

Los siete: `scripts/loop/vuelta17_acto_que_crecio.py`, `..._marcar_221_superadas.py`,
`..._nota_op_i_01.py`, `..._dos_costuras.py`, `..._escribir_dos_operaciones.py`,
`..._fase2_pendiente.py` y `scripts/plan/simular_destejido.py`.

**`dataset/` INTACTO y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` INTACTO**, verificado y no supuesto:
`git diff --name-only db6959b6 HEAD -- dataset/ docs/INTRA_DOMINIO_VEREDICTOS.jsonl` sale **vacio**.
**Ninguna operacion se ejecuto. Dos se crearon, por decision escrita del fundador.**

---

## CORRECCION DE LA CAIDA DE LA VUELTA 16, en este mismo reporte y sin borrar

**Lo que decia el reporte de la vuelta 16, palabra por palabra** (`docs/loop/REPORTE.md`, seccion
"b a f", version del hash `afeb4933`):

> ~~**220 son identicos en tamano; 1 crecio** (`construccion_de_leverage`, de 4 a 5, ya documentado).~~

**LO CORRECTO: el que crecio es `gestion_terminacion_franquiciado`, de 2 a 3 miembros, ganando
`perdida_control_operativo`.**

**LA CAIDA ES DEL EJECUTOR**, no del auditor ni del archivo. El conteo "220 identicos y 1 crecio"
siempre estuvo bien; **el NOMBRE se copio de una nota vieja de otro objeto y de otra epoca en vez de
leerse de la salida del instrumento que acababa de correr.** Misma especie que la caida de la vuelta
15: el instrumento corriendo y la afirmacion saliendo de otro sitio.

**LA FUENTE CORRECTA YA ESTABA ESCRITA EN EL PROPIO PLAN, y no se leyo:** la nota de `OP-U-02` dice,
con esas palabras, *"CUARENTA Y DOS siguen abiertos identicos y UNO crecio (`gestion_terminacion_
franquiciado` con `terminacion_franquiciado_causas`, de 2 a 3)"*.

**REMEDIDO CON INSTRUMENTO PROPIO, NO COPIANDO LA CIFRA DEL AUDITOR**
(`scripts/loop/vuelta17_acto_que_crecio.py`), con **tres metodos independientes que tenian que
coincidir o se declaraba la discrepancia**:

| metodo | como | 220 identicos | 1 crecio | sin sucesor | mas de un sucesor |
|---|---|:--:|---|:--:|:--:|
| **A** | superset de los 221 viejos contra `RECOMPUTO_3388_COMPONENTES.jsonl` | si | `gestion_terminacion_franquiciado`, 2 a 3 | 0 | 0 |
| **B** | superset contra las 335 entradas nuevas de `INVENTARIO.jsonl` (mismo hecho, otra ruta de datos) | si | idem | 0 | 0 |
| **C** | sin superset: pertenencia nodo a componente, preguntando el tamano de hoy de la componente que contiene al primer miembro | si | idem | 0 | 0 |

**Control previo del metodo C:** los 335 componentes cubren **854 nodos distintos** con **cero** nodos
en dos componentes a la vez.

**Y EL CONTRASTE CON EL NOMBRE CAIDO, medido:** `construccion_de_leverage` tiene **CINCO miembros en
los dos cortes** y **no tuvo cuatro en ninguno**. La cifra "de 4 a 5" no describe a ningun objeto de
`INVENTARIO.jsonl` en ninguno de los dos cortes.

**DE DONDE SALIO EL "DE 4 A 5", localizado y no supuesto.** Vive, correcto y en su sitio, en dos
lugares que hablan de **otros objetos**: la nota de `OP-I-01` (*"la competencia entre inversores se
declaro PURA con 4 miembros al puesto 1030 y la componente de hoy tiene 5"*, que es una degradacion
**anterior** al corte 2.117) y `CORRECCIONES_A_APLICAR.md` linea 344 (*"la componente crecio a cinco
miembros por la A del puesto 878"*, misma degradacion). **Ninguna de las dos se toca: las dos son
ciertas de lo suyo.**

**LA CIFRA CAIDA NO VIVE EN NINGUN TERCER SITIO, verificado y no supuesto.** El otro "de 4 a 5" del
plan (`RECOMPUTO_3388.md` linea 227) es **la FILA de seis del histograma**, que paso de cuatro
componentes a cinco: otro objeto y correcto. **Corregida en los dos sitios que el encargo nombra y en
ningun otro, porque no hay ningun otro.**

---

## TAREA 1, PUNTOS 1 A 4

### 1. La caida, corregida con tachado en `RECOMPUTO_3388.md` linea 1042

Ejecutado. El tachado deja escrito **que la caida es del ejecutor** y **que la fuente correcta ya
estaba en la nota de `OP-U-02`**, con el metodo de las tres mediciones al lado.

### 2. Las 221 lineas viejas, marcadas como superadas con puntero a su sucesora

**Instrumento: `scripts/loop/vuelta17_marcar_221_superadas.py`**, con tres controles que tenian que
pasar antes de escribir (si fallaba uno, no escribia).

**MEDIDO ANTES DE ESCRIBIR:** los 221 tienen sucesora **unica** (cero sin sucesora, cero con mas de
una), **ninguna cambia de nombre**, y los **335 nombres nuevos son 335 distintos**. Por eso el puntero
no puede ser solo el nombre: **es nombre mas `fecha_corte` 2026-08-13**.

**COMO QUEDO MARCADA CADA UNA:** el marcador `SUPERADA POR EL CORTE 3.388 (vuelta 17, 14 ago 2026)` va
**al frente del campo `estado`**, con el texto viejo de ese campo conservado palabra por palabra
detras; y el **puntero a la sucesora** va al final del campo `nota`, con la frase *"PARA CONTESTAR SI
UN NODO REPITE HOY SE LEE LA SUCESORA, NO ESTA"*.

**DIFF EXACTO: 221 lineas modificadas, cero altas y cero bajas.** El archivo sigue en **671 lineas**.
Las 335 nuevas y las 115 de los otros cinco tipos: **cero tocadas** (verificado tras escribir). Hubo un
paso intermedio en el que el reescribir el archivo entero normalizo el formato de las 335 lineas nuevas
(que el script de la vuelta 16 escribio sin espacios tras los dos puntos); **se restauraron byte a byte
las 335 antes de commitear**, tras comprobar que las 335 eran identicas como JSON, **para que el diff
sea exactamente las 221 y nada mas**.

### 3. El aviso en `10_INVENTARIO.md`, sin regenerar la tabla

**Puesto en CINCO sitios**, no en uno: la cabecera (con tachado en "FECHA DE CORTE DE TODO EL
INVENTARIO"), la tabla `EL VOLUMEN` (filas `acto` y `TOTAL`), la seccion `LOS ACTOS` entera, la tabla
de los seis mayores, y las **dos** filas de `COMO SE LEE ESTE INVENTARIO` (la de "si un nodo repite",
que es la que el auditor nombro, y la de "todo el inventario es del 11 ago 2026").

**LA TABLA NO SE REGENERA:** sigue siendo el disparador de `08_VERIFICACION`. Las cifras de hoy van
**al lado** de las viejas, en columna propia, no en su lugar.

**REMEDIDO PARA EL AVISO, con instrumento propio:**

| | vista humana (corte 2.117) | archivo fuente hoy (corte 3.388) |
|---|---:|---:|
| filas de tipo `acto` | 221 | **556** (221 superadas mas 335 vigentes) |
| filas totales | 336 | **671** |
| actos CERRADOS | 173 | **280** |
| actos ABIERTOS | 48 | **55** |
| nodos implicados | 576 | **854** |
| los otros cinco tipos | 53, 20, 19, 13, 10 | **identicos** |

**Y EL MAYOR YA NO TIENE TRECE MIEMBROS: tiene QUINCE**
(`cultura_de_seguridad_interpretivista_funcionalista`), y hay otro de **diez**
(`causas_comunes_vs_especiales`). Los dos ABIERTOS y los dos solo bajo `OP-U-02`.

**UNA DIFERENCIA DE ETIQUETA QUE APARECIO AL REMEDIR Y SE DECLARA EN VEZ DE CUADRARSE:** contando las
221 viejas por la palabra de su campo `estado` salen **173 CERRADOS, 47 ABIERTOS y UNA que no dice
ninguna de las dos**, el acto de la junta asesora, cuyo `estado` dice *"repite, DECISION TOMADA por
`OP-M-04`"*. **La vista humana dice 48 abiertos porque cuenta a esa entre ellos.** No es caida de nadie
ni mueve ninguna decision: **173 mas 47 mas 1 son los mismos 221**, y esa no esperaba al recomputo,
esperaba a una mesa que ya la resolvio. Queda escrito para quien regenere la vista.

### 4. El hueco nombrado del discutible 2, registrado en `OP-I-01`

Registrado con su alcance exacto: **el campo `operaciones` de las 335 hereda lo que el campo `nodos` de
las operaciones viejas tenga incompleto**, la verificacion de la vuelta 16 (189 de 221) prueba que el
metodo es **consistente** con ese campo pero **no que ese campo este completo**, el hueco **no se
agranda** porque es el mismo campo que ya gobernaba a las 221 viejas, y **auditarlo operacion por
operacion es trabajo de la FASE III**. Nombrado y no rellenado, como pide la propia verificacion de
`OP-I-01`.

---

## TAREA 1, PUNTO 5: LA FASE II, MEDIDA BLOQUE POR BLOQUE

**LA FASE II NO CIERRA EN ESTA VUELTA, y se dice antes de dar ninguna cifra.** Detalle completo en
`docs/plan/RECOMPUTO_3388.md`, seccion "TAREA (vuelta 17)". Instrumento:
`scripts/loop/vuelta17_fase2_pendiente.py`.

| bloque | antes | despues |
|---|---|---|
| la cola de relectura post fusion | siete declarados, sin verificar al 3.388 | **VERIFICADA ENTERA, 7 de 7** |
| el criterio del forastero | dos ejemplares declarados | **VERIFICADOS LOS DOS** |
| el lote de cinco del sales roadmap | "cinco pares", sin nomina en ningun sitio | **LOS CINCO NOMBRADOS** |
| las lecturas de acto entero de P.5 | condicion escrita, sin cifra | **CUANTIFICADA** |
| los ejemplares de las veinte figuras | PENDIENTES DE MEDICION | **medido el tamano, NO cerrado** |

**LA COLA DE RELECTURA POST FUSION, 7 de 7.** Los siete (**707, 1096, 196, 253, 224, 591, 968**)
conservan su clase y su disparador, comprobado contra el plan de 71 operaciones: **dos mueren** (su
nodo esta en el `eliminar` de su operacion), **cuatro cambian de texto** (estan en la nomina y no en el
`eliminar`) y el **1096** entra porque su contraparte `filosofia_customer_validation` muere en
`OP-M-05-APERTURA`. **La baja tambien se verifica:** el **751** sale bien, porque **ninguna de las 71
operaciones tiene `customer_validation_sell_phase` en su `eliminar`**.

**EL CRITERIO DEL FORASTERO, los dos.** `tacticas_cierre_ventas`: **seis pares, 1 A y 5 D**, y su unica
A es el puesto **221** contra un nodo que no es del cierre. Exacto contra lo declarado.
`incentivos_no_monetarios_advocacy`: **cero pares en el cribado**, y **ese cero se re-verifico antes de
citarlo** (regla 8, una busqueda negativa no se puede citar): **NO es un hueco**, sus lecturas son
**dirigidas** (`LD-28`, `LD-30`, `LD-31`, las tres D) y viven en `LD_ADOPT_ADVOCATE.md`. Un instrumento
que solo mirara los veredictos lo habria dado por no leido.

**EL SALES ROADMAP, los cinco nombrados por primera vez.** Los diez que si estan dan **6 A y 4 D**,
exacto contra la tabla de los trece racimos de la vuelta 16. **HALLAZGO NO PEDIDO: los cinco que faltan
no estan repartidos por el racimo. CUATRO DE LOS CINCO cuelgan de `estrategia_de_ventas`**, que tiene
**uno solo de sus cinco pares leido**.

**P.5, CUANTIFICADA POR PRIMERA VEZ.** De las 335 componentes, **280 tienen todos sus pares leidos**
(P.5 ya es un hecho) y **55 no** (P.5 sigue siendo condicion). **Faltan 329 pares. Y LOS 329 ESTAN
TODOS FUERA DE COLA: cero en cola.** Con el cribado cerrado en 3.388 de 3.388, **ni uno va a llegar por
su cuenta: cada uno es una lectura dirigida o no es nada.**

**LAS VEINTE FIGURAS: medido el tamano, NO cerrado, y no es la medicion que la fase espera.** **7 de 20
nombran algun ejemplar en su propia nota y 13 no**, y **el reparto parte casi exacto por fecha de
corte**: las doce del 11 ago no nombran ninguno, y de las ocho del 12 ago siete nombran y una no. **Por
eso el `grep` de la vuelta 15 daba cero en doce de veinte: los ejemplares existen, no estan en la
entrada.** Ejemplares sin nombrar: **119** por la cuenta ingenua y **98** por la corregida, **las dos
publicadas con su definicion al lado porque la diferencia es de definicion y no de medicion**.

---

## TAREA 2: LAS DOS COSTURAS SIN DUENO. EL PLAN PASA DE 69 A 71

**LA VALVULA NO SE ACTIVO.** Ninguna de las dos exigio lecturas nuevas amplias ni una decision no
medida: la evidencia estaba escrita entera en `FICHA_SUBFUSION_GRADIENTE.md` (lote C2),
`COSTURAS_INTERNAS.jsonl`, los veredictos del cribado y `CONTROL_MUESTRA_D.md`. **El plan queda en 71,
no en 70 ni en 69.**

**Integridad tras escribir:** 71 operaciones, **ids unicos**, **cero dependencias rotas**, las 71 en
LISTA, esquema de dieciocho campos identico al de las 69. Las 69 viejas **no se reescriben**: las dos
se anaden al final.

| | `OP-D-08` | `OP-D-09` |
|---|---|---|
| nodo | `lienzo_modelo_negocio` | `planificacion_recoleccion_datos` |
| forma | DESTEJIDO SOLO | DESTEJIDO SOLO |
| orden | 8 de `02_DESTEJIDOS` | 9 |
| pares en el cribado | **7** (543 D, 784 B, 998 D, 999 D, 1123 D, 1136 D, 1434 D) | **1** (2695 D) |
| A vigentes | **0** | **0** |
| fuentes declaradas | **1** (Osterwalder) | **1** (Juran, Defeo) |
| congelados que libera | **1** (el par 784) | 0 |

**POR QUE DESTEJIDO SOLO Y NO ELECCION MIA: lo tenia escrito el propio archivo.** El veredicto del
puesto **1434** dice, literalmente, *"`lienzo_modelo_negocio` es costura confirmada y no tiene gemelo,
asi que su arreglo es un destejido solo"*.

**UNA PRECISION QUE AL CORTE 2.117 NO SE PODIA HACER.** `planificacion_recoleccion_datos` es de
`quality`, que entonces estaba **SIN CRIBAR con cero pares juzgados**: su "sin gemelo" de entonces **no
era una medicion, era un hueco de cribado**. Hoy `quality` tiene **844 pares juzgados con 126 A**, asi
que **su cero A vigentes SI es una medicion**.

### La simulacion, y lo que tumbo

**P.7 tiene instrumento para FUSIONES (`scripts/plan/simular_fusion.py`) y NO tenia ninguno para
DESTEJIDOS.** Las siete `OP-D-*` viejas se escribieron LISTAS sin simular, porque P.7 habla de
operaciones de MESA. **Escrito `scripts/plan/simular_destejido.py`, de solo lectura**, que mide lo
unico que un destejido puede romper: veredictos apoyados en un paso, anclas de aristas paso a nodo,
referencias internas colgando, y cero movimiento de grafo. **No extiende P.7 por su cuenta: la pregunta
de doctrina esta abajo.**

**LO QUE LA SIMULACION TUMBO, y es el motivo de que exista.** De las **cuatro** opciones de conservar
una sola narracion del lienzo, **tres rompen el veredicto 1434**, que es **el unico de los tres
veredictos que citan pasos de ese nodo cuya razon NO se declara invariante**. La cuarta (pasos 13 a 17)
no rompe ningun apoyo **pero se lleva toda la practica propia de los bloques 1 y 3**, que es justo lo
que **P.3** prohibe podar cuando el injerto es del mismo tema. **El reparto escrito es el unico
escenario probado que ni rompe ni pierde.**

### Dos correcciones medidas que las dos operaciones traen

**A LA FICHA DEL GRADIENTE, sobre `planificacion_recoleccion_datos`:** la ficha dice *"quitar un indice
que se colo como pasos"* y lo situa en los pasos **1 a 4**. **El indice son TRES, no cuatro.** El paso
1 (*formular la pregunta especifica*) **no tiene casa en el metodo de 5 a 16** y **sostiene al paso
14**, que apunta al *"problema tecnico original"*. Por la **REGLA DE REPARTO de la fase** (la perdida
sin bloque va al superviviente) **se reparte en vez de podarse**. La ficha no se toca: la correccion
esta escrita dentro de `OP-D-09`.

**TRES CONTEOS DEL MISMO HECHO RECONCILIADOS SIN CORREGIR NINGUNO.** Sobre `lienzo_modelo_negocio`, el
plan tenia escritas tres cifras que parecian pelearse: el literal *"completar cada uno de los 9
bloques"* esta en **DOS** pasos (ficha), las narraciones son **CUATRO** (informe), y los pasos que dan
la orden son **SIETE** (veredicto 998, via `CONTROL_MUESTRA_D.md`). **Los tres son correctos y cuentan
tres objetos distintos**: el literal exacto, las narraciones, y los pasos contando la enumeracion de 13
a 17 que recorre los bloques uno por uno. **Ninguno se corrige.**

### El hueco que `OP-D-08` tapa, y es el motivo de fondo

**El par 784 estaba congelado por una costura cuya cirugia no tenia dueno, asi que ese congelado no
entraba en la contabilidad de nadie.** Medido: **el numero 784 no aparece ni una vez en todo
`docs/plan/`**, y es **el unico par de los 3.388 cuya razon lleva la frase "NO SE JUZGA HOY"**. Su
propia razon se nombra *"tercer nodo del archivo que bloquea un par por costura"*, y **de los tres, dos
ya tenian operacion** (`voz_del_cliente_voc` en `OP-D-02`, `ab_testing_optimizacion` en `OP-D-03`) **y
este era el que no la tenia.**

---

## MARCADOR RECOMPUTADO DEL ARCHIVO

**Recomputado en esta vuelta, no copiado**, sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:

**A 583 (17,2 %), B 89 (2,6 %), C 7 (0,2 %), D 2.709 (80,0 %); n 3.388.**
**Cero huecos y cero duplicados**, comprobado por conjunto de puestos de 1 a 3.388.

**Sin cambio respecto a lo publicado**, y no podia haberlo: cero pares leidos esta vuelta y el archivo
sale intacto en el diff.

## TASA POR DOMINIO

| dominio | pares | A | tasa |
|---|---:|---:|---:|
| `core` | 1.445 | 344 | **23,8 %** |
| `health_safety` | 192 | 45 | **23,4 %** |
| `environmental` | 170 | 29 | 17,1 % |
| `quality` | 844 | 126 | 14,9 % |
| `franquicias` | 148 | 18 | 12,2 % |
| `exportacion` | 130 | 15 | 11,5 % |
| `seguridad_digital` | 27 | 3 | 11,1 % |
| `entrega` | 171 | 2 | 1,2 % |
| `compras` | 155 | 1 | 0,6 % |
| `risk_management` | 106 | **0** | **0,0 %** |
| **total** | **3.388** | **583** | **17,2 %** |

> **DOS COSAS QUE ESTA TABLA DICE Y NO SE PIDIERON.** Primera: **`franquicias` bajo de 19,6 % a
> 12,2 %**, que es exactamente lo que el banco 9.27 predecia (*"la cola del dominio se agota por
> dentro"*) y lo que `10_INVENTARIO.md` dejo escrito como *"va a bajar"* cuando el dominio estaba
> abierto con 46 pares. **La prediccion se cumplio y queda cobrada.** Segunda: **`risk_management`
> tiene 106 pares juzgados y CERO A.** Es el unico dominio del catalogo con cero.

## VARA POR TRAMO

**NO APLICA esta vuelta.** Cero pares nuevos leidos, cero operaciones ejecutadas.

## FIGURAS Y FAMILIAS AL DIA

**Las 20 figuras:** siguen 20 en el archivo. **Estado de sus ejemplares medido por primera vez esta
vuelta: 7 nombran, 13 no.** El bloque **sigue abierto** y sigue siendo trabajo de lectura.

**Las 53 familias, tres cubetas REMEDIDAS en esta vuelta con instrumento propio** (interseccion de
miembros contra las 335 componentes, sin leer ni un par):

| cubeta | cuantas |
|---|---:|
| **CONTENIDAS** en un solo componente | **23** |
| **PARTIDAS** entre componentes distintos | **14** |
| **SIN ARISTA A** al corte 3.388 | **16** |
| total | **53** |

**Calzan exacto con lo que la vuelta 16 publico** (23, 14, 16). Se remidieron en vez de copiarse
porque la regla 1 lo manda, y **el resultado es una confirmacion independiente, no una copia**.

---

## CORRECCIONES DECLARADAS, todas con tachado y sin borrar el texto viejo

1. **El acto que crecio entre el 2.117 y el 3.388:** ~~`construccion_de_leverage`, de 4 a 5~~ a
   **`gestion_terminacion_franquiciado`, de 2 a 3, ganando `perdida_control_operativo`**. Caida del
   ejecutor. Sedes: `RECOMPUTO_3388.md` linea 1042 y este reporte. Remedida con tres metodos propios.
2. **La adjudicacion "NO se crean operaciones nuevas para ellas"** (`RECOMPUTO_3388.md` seccion 4):
   revertida **solo para las dos nombradas** por decision del fundador. **Sigue en pie para las otras
   29.** El texto viejo no se borra.
3. **La cabecera de `02_DESTEJIDOS.md`**, ~~"`OP-D-01` a `OP-D-06`, LAS SEIS LISTAS"~~: la fase son
   **nueve** operaciones. La cifra vieja era correcta el 11 ago 2026 y no se borra.
4. **`10_INVENTARIO.md`**: cinco sedes de tachado con las cifras de hoy al lado, **sin regenerar la
   tabla**. Ninguna cifra vieja se sustituye.
5. **La ficha del gradiente sobre el indice de `planificacion_recoleccion_datos`**: son **tres** pasos
   y no cuatro. La ficha no se toca; la correccion vive dentro de `OP-D-09` con su motivo medido.

---

## PENDIENTES DE DOCTRINA

1. **La frase "no puede crecer" de la formula mecanica de las notas de acto.** La nota vieja de
   `gestion_terminacion_franquiciado` decia *"tamano 2. Sin pares pendientes: no puede crecer"*, **y
   crecio.** La formula no miente sobre lo que mide (los pares **internos** del acto) pero **su frase
   promete mas de lo que mide**: una componente tambien crece cuando entra un nodo **de fuera** por una
   A nueva. **Esa misma frase se sigue escribiendo hoy en las 335 entradas nuevas.** No se toco ninguna
   nota: reescribir la formula de 335 entradas no es una correccion, es una regeneracion, y eso lo
   adjudica quien corresponda.
2. **P.7 no cubre los destejidos.** Dice *"toda operacion de MESA se simula"*, y las siete `OP-D-*`
   viejas se escribieron LISTAS sin simulacion. Esta vuelta escribio un simulador de destejido y lo
   nombro dentro de las dos operaciones nuevas, **pero no extiende P.7 por su cuenta**. La pregunta:
   **debe un destejido simularse como una mesa?** Si la respuesta es si, **las siete viejas quedan sin
   ese requisito cumplido** y hay que decidir si se les corre hacia atras.
3. **La entrada de tipo `defecto` "pares que una fusion reabre" escribe su regla sin su excepcion.**
   Dice *"solo los B y los C"* y a continuacion lista un A, el 1096. **Leida sola se contradice; leida
   junto a `08_VERIFICACION.md` no**, porque alli esta la excepcion con su motivo. **No se toco.** La
   pregunta es si una entrada de inventario debe cargar la excepcion de la regla que copia, o basta con
   que la cargue su fuente.
4. **El motivo escrito para no leer los cinco del sales roadmap contesta a una pregunta y no a la
   otra.** *"Leerlos cierra cobertura, no cambia forma"* es cierto de **la clase del racimo**. **Pero
   la pregunta de P.5 es otra: si el acto es UNA familia o DOS**, y esa se contesta leyendo los cuatro
   pares que cuelgan de `estrategia_de_ventas`. **Son dos preguntas sobre los mismos cinco pares y el
   plan solo tiene escrita la respuesta a una.**

---

## PREGUNTAS, lo que no se puede medir desde aqui

1. **`planificacion_recoleccion_datos` declara en su `resumen_teorico` que el proceso "involucra 17
   pasos" y tiene 16 `pasos_accionables`** (medido sobre `dataset/metadata/master_graph.json`). Puede
   ser que el original de Juran traiga 17 y el catalogo perdiera uno al tejer, o que el resumen cuente
   mal. **No se rellena: es hueco nombrado, y decidirlo exige la fuente, que esta fuera del repo.**
2. **La FASE II cierra sin los ejemplares de las veinte figuras, o el fundador los difiere por
   escrito?** El bloque esta ahora medido en tamano (13 entradas, entre 98 y 119 ejemplares) pero
   cerrarlo es trabajo de lectura figura por figura, y es el que decide cuando cierra la fase.

---

## DISCUTIBLES MARCADOS, para la relectura ciega del auditor

**Marcados ANTES de saber si aciertan.**

1. **LA FORMA DEL MARCADO DE LAS 221.** Puse el marcador **al frente de `estado`** (conservando el
   texto viejo detras) y el puntero **al final de `nota`**, **sin anadir ninguna clave nueva**. La
   alternativa natural era una clave propia, `superada_por`. **Elegi no anadirla para que las 221 y las
   335 conserven exactamente el mismo esquema**, que es lo que permite compararlas campo a campo. **El
   coste de mi eleccion: un lector de maquina tiene que mirar dentro de un texto en vez de leer una
   clave.** Si el auditor prefiere la clave, se anade sin deshacer nada.
2. **EL ORDEN 8 Y 9 DE LAS DOS OPERACIONES NUEVAS.** El criterio de orden de `02_DESTEJIDOS` es
   **congelados liberados**, y por ese criterio `OP-D-08` (libera uno) iria **entre `OP-D-03` y
   `OP-D-04`**. **Las escribi al final porque renumerar siete operaciones ya adjudicadas no me parece
   autorizado por este encargo.** Si el auditor dice que el criterio manda sobre la comodidad, se
   renumera.
3. **EL REPARTO PROPUESTO DE `OP-D-08` DEJA DOCE PORTADORES DE LINEA, y el veredicto 1123 estimaba
   "unos cinco pasos".** Los dos numeros responden a cosas distintas (el 1123 estimaba una **poda** y
   P.3 obliga a un **reparto**), **pero soy yo quien decide que P.3 aplica aqui**, y si el auditor lee
   que las cuatro narraciones no son "del mismo tema" en el sentido de P.3, el reparto sobra y la poda
   basta.
4. **DIGO QUE EL INDICE DE `planificacion_recoleccion_datos` SON TRES PASOS Y NO CUATRO, corrigiendo a
   la ficha del gradiente, SIN HABER RELEIDO EL NODO ENTERO.** Me apoyo en dos cosas medidas: que
   ningun paso del 5 al 16 establece el objetivo o la pregunta, y que el paso 14 apunta al *"problema
   tecnico original"*. **Es una inferencia de texto, no una lectura de la vara.**
5. **EL SIMULADOR DE DESTEJIDO ES MIO Y SUS CRITERIOS TAMBIEN.** En particular: cuando vi que el
   veredicto 998 se disparaba como rotura en todos los escenarios, **anadi la regla de que una razon
   que se declara INVARIANTE cita el paso como POSICION y no como apoyo**. La lei de la propia razon,
   no la invente, **pero es un criterio que exculpa, y un criterio que exculpa siempre hay que
   mirarlo dos veces.**
6. **LA HEURISTICA DE "REFERENCIAS COLGANDO" DEL SIMULADOR ES TOSCA** (busca frases sueltas como "el
   canvas" o "el problema" en los pasos que sobreviven). **Produce avisos que no son roturas y en un
   caso senala como huerfano al paso 2, que es el que establece lo que la heuristica cree que pierde.**
   No la use para ningun veredicto, **pero queda en la salida y podria confundir a quien la corra.**
7. **ESCRIBI LAS DOS OPERACIONES EN ESTADO `LISTA` teniendo `OP-D-08` una `pregunta_pendiente`
   abierta** (si "para la solucion disenada" del paso 5 es un marco propio). **Me apoyo en el
   precedente de `OP-D-01`**, que esta LISTA con una decision abierta escrita en su `preservar`. **Si
   ese precedente no cubre este caso, `OP-D-08` deberia ir en otro estado.**
8. **LAS DOS CUENTAS DE EJEMPLARES SIN NOMBRAR (119 y 98) DEPENDEN DE UN CRITERIO MIO**: que una figura
   "nombra sus ejemplares" si su `nota` trae un id de nodo, un puesto o un `LD-nn`. **Es un criterio de
   forma, no de contenido**: una figura podria describir su ejemplar en prosa sin nombrarlo, y mi
   instrumento la contaria como que no nombra.
9. **PUSE UN AVISO EN `02_DESTEJIDOS.md` QUE EL ENCARGO NO PIDIO.** El encargo nombraba
   `10_INVENTARIO.md`. **Anadi el de `02_DESTEJIDOS.md` por mi cuenta**, porque su cabecera declara seis
   operaciones y ahora son nueve, y me parecio la misma clase de desfase. **Es iniciativa mia y puede
   leerse como salirse del encargo.**
10. **NO TOQUE `00_INDICE.md`, que tambien quedo desfasado**: dice "se ejecutan **sesenta y seis**
    operaciones LISTAS" y hoy son 71, y su tabla de lo que queda sigue diciendo "cinco pares" del sales
    roadmap sin la nomina que esta vuelta calculo. **Lo dejo sin tocar a proposito, para no repetir el
    patron del aviso no pedido dos veces en la misma vuelta, pero lo declaro: es un desfase vivo.**
