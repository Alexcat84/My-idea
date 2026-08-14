# REPORTE DE LA VUELTA 19 . Ejecutor: Opus 5 . 14 ago 2026

**FASE II, RECOMPUTO. MODO DE CIERRE.** Cero reparaciones de nodos, cero operaciones
ejecutadas, FASE III sin abrir, `pasada-unica` sin crear, cribado sin tocar.

> **REGLA 1 DEL EJECUTOR, aplicada sin excepcion: toda cifra de este reporte se lee de la
> salida de un instrumento corrido EN ESTA VUELTA.** Las cifras de vueltas anteriores solo
> aparecen como contraste y con su corte al lado. **Donde mi medicion discrepa de una cifra
> publicada, la discrepancia se declara y la cifra vieja no se toca.**

> **AVISO DE CREDITO, contestado de frente.** El encargo dijo que si esta tanda deja una
> caida de clase o de cifra publicada, el bucle PARA. **No conozco ninguna caida mia en
> esta tanda, y por eso el trabajo va con las cifras remedidas dos veces y con las
> discrepancias marcadas.** Lo que si trae esta vuelta es **una discrepancia contra una
> premisa del propio encargo**, medida y declarada: la seccion 4.

---

## 0. LO PRIMERO: EL HASH, LAS RUTAS Y LO QUE NO SE TOCO

**Hash del TRABAJO: `7b21a8d0`.** Este reporte se commitea despues, **asi que el hash del
reporte es otro y no es el del trabajo.**

**Arbol al empezar: LIMPIO y sincronizado con `origin/bucle`**, comprobado antes de la
primera edicion. No habia nada pendiente que commitear.

**LAS NUEVE RUTAS del `git diff --stat 5a7b7d60 7b21a8d0`, la lista COMPLETA:**

| ruta | que cambio |
|---|---|
| `docs/plan/INVENTARIO.jsonl` | **ocho lineas**: cinco de TAREA 1, una mas de su segunda mitad, tres de TAREA 2.B (`EL PASO DE OFICIO` se toca en las dos, por eso son ocho lineas y nueve ediciones) |
| `docs/plan/LD_ESTRELLA_DISRUPTIVAS.md` | **NUEVO**: la relectura del par periferico de la novena estrella |
| `docs/plan/RECOMPUTO_3388.md` | **NUEVO al final**: seccion TAREA (vuelta 19), la FASE II medida bloque por bloque |
| `scripts/loop/vuelta19_medir.py` | **NUEVO**, instrumento de solo lectura |
| `scripts/loop/vuelta19_figuras.py` | **NUEVO**, instrumento de solo lectura |
| `scripts/loop/vuelta19_fase2.py` | **NUEVO**, instrumento de solo lectura |
| `scripts/loop/vuelta19_tarea1.py` | **NUEVO**, escribe cinco lineas de `INVENTARIO.jsonl` |
| `scripts/loop/vuelta19_tarea1b.py` | **NUEVO**, escribe una linea de `INVENTARIO.jsonl` |
| `scripts/loop/vuelta19_tarea2.py` | **NUEVO**, escribe tres lineas de `INVENTARIO.jsonl` |

**LO RESERVADO SIGUE INTACTO, medido y no supuesto:** `git diff --name-only 5a7b7d60
7b21a8d0 -- dataset/ docs/INTRA_DOMINIO_VEREDICTOS.jsonl` devuelve **CERO lineas**. El
archivo de veredictos conserva sus **3.388** lineas y el cribado sigue **CERRADO en 3.388
de 3.388**.

**EL DIFF DEL INVENTARIO, verificado linea a linea contra `5a7b7d60`:** **671 entradas
antes y 671 despues**, **663 identicas byte a byte y 8 tocadas**; en las ocho **la adicion
es ADITIVA** (el valor nuevo empieza o acaba con el viejo, comprobado clave por clave), y
**en ninguna aparece o desaparece una clave**. En siete solo cambia `nota`; en la del acto
cambian `cobertura`, `estado` y `nota`, que es lo que el encargo pedia.

**Cero guiones largos y cero guiones medios en las nueve rutas**, contado por mi con un
lector propio antes de cada commit. **El hook corrio en los tres commits de trabajo y dio
verde las tres veces.**

---

## 1. EL MARCADOR RECOMPUTADO, con instrumento propio de esta vuelta

**Instrumento: `scripts/loop/vuelta19_medir.py`**, de solo lectura, sobre
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `dataset/metadata/master_graph.json` y
`docs/plan/INVENTARIO.jsonl`. **Corte: 14 ago 2026.**

| clase | pares | % |
|---|---:|---:|
| **A** | **583** | 17,2 |
| **B** | **89** | 2,6 |
| **C** | **7** | 0,2 |
| **D** | **2.709** | 80,0 |
| **n** | **3.388** | |

**Puestos unicos 3.388, del 1 al 3.388, CERO huecos y CERO duplicados.**

### La tasa por dominio

| dominio | pares | A | tasa |
|---|---:|---:|---:|
| compras | 155 | 1 | 0,6% |
| core | 1.445 | 344 | 23,8% |
| entrega | 171 | 2 | 1,2% |
| environmental | 170 | 29 | 17,1% |
| exportacion | 130 | 15 | 11,5% |
| franquicias | 148 | 18 | 12,2% |
| health_safety | 192 | 45 | 23,4% |
| quality | 844 | 126 | 14,9% |
| **risk_management** | 106 | **0** | **0,0%** |
| seguridad_digital | 27 | 3 | 11,1% |

**Las diez filas calzan celda por celda con el acta de la vuelta 18**, incluido el unico
cero del catalogo.

### La vara por tramo

**No hay tramo nuevo que medir: el cribado esta CERRADO y esta vuelta no leyo ni un par de
cola.** La unica lectura de esta vuelta es una **relectura dirigida** de un par que ya
estaba adjudicado, y **no mueve el marcador ni entra en la cola**.

### Figuras y familias al dia

| | medido hoy | contraste con la vuelta 18 |
|---|---:|---|
| entradas de `INVENTARIO.jsonl` | **671** | igual |
| de tipo `acto` | **556** (221 superadas mas **335** vigentes) | igual |
| actos vigentes **CERRADOS** / **ABIERTOS** | **281** / **54** | eran 280 / 55 |
| deuda total de P.5, desde el inventario | **324 pares** | el acta 17 midio **329** |
| `familia_de_ids` **53**, `figura` **20**, `defecto` **19**, `racimo` **13**, `dominio` **10** | igual | igual |
| **figuras que NOMBRAN**, criterio de FORMA de la vuelta 17 | **20 de 20** | eran 18 de 20 |
| **figuras con marca explicita de tanda de nombramiento** | **13 de 20** | eran 11 de 20 |

**Las dos cuentas de figuras se publican JUNTAS y ninguna sola**, porque el acta de la
vuelta 18 ya adjudico que la de forma tiene falsos positivos (su adjudicacion 9). **Las
siete sin marca de tanda no estan sin nombrar: nacieron nombradas**, y esta vuelta lo
comprobo entrada por entrada.

---

## 2. TAREA 1: los cinco registros

**Los cinco son aditivos y ninguno borra texto viejo.** Cada cifra sale de
`scripts/loop/vuelta19_medir.py`, corrido hoy.

**1. `LA BIFURCACION`, el aviso del contador: CORREGIDO.** Remedido: la palabra
`bifurcacion` aparece en la razon de **SIETE puestos, 1054, 1106, 2030, 2050, 2147, 2198 y
2478**, y **DOS de los siete SON los ejemplares** (el 2030 arranca *La bifurcacion del
origen* y el 2050 *La bifurcacion del origen otra vez*). **Lo unico exclusivo del 2198 es
la forma en MAYUSCULAS**, que aparece en **una sola razon**. **La leccion enderezada, y es
distinta de la que el aviso daba:** un contador **si** encuentra estos dos ejemplares; **lo
que no da es la figura**, porque de los siete puestos con la palabra solo dos son
ejemplares y los otros cinco la usan en otro sentido. **Diff de una linea, la frase vieja
entera.**

**2. `EL PASO DE OFICIO`, los "158 NODOS VIVOS": CORREGIDO.** Remedido sobre el grafo:
**158 nodos en el dominio, 17 deprecado, 141 VIVOS**, que es la cifra que la entrada de
tipo `dominio` de este mismo inventario ya publicaba. **La cota corregida es 6 de 141**, y
**la cota se reconto sobre los 141 y da los mismos seis nodos, ninguno deprecado**; los
diez pares de 130 no cambian. **Diff de una linea, la cifra vieja entera.**

**3. `ESTRELLA (9.23)`, la novena: REGISTRADA, y VERIFICADA 9 DE 9.** La cita del auditor
verifica palabra por palabra contra `docs/INTRA_DOMINIO_INFORME.md`. **Pero el registro no
quedo como el encargo lo escribio, porque la medicion dijo otra cosa: la seccion 4 de este
reporte.**

**4. El acto `customer_validation_sales_roadmap`: CERRADO, con el patron de las 221.**
`cobertura` pasa a **15 de 15 pares leidos, 0 en cola, 0 fuera de cola**, `estado` de
ABIERTO a **CERRADO**, y los dos candidatos (particion y forastero condicionado) quedan
registrados **como candidatos y no como hechos**, con su condicion escrita y su puntero a
`LD_SALES_ROADMAP.md`. **En los dos campos lo nuevo va al frente y el texto viejo queda
entero detras.**

> **REMEDIDO DESPUES DEL CAMBIO, con instrumento y no restando de memoria**, que es lo que
> el encargo mandaba: **actos vigentes 281 CERRADOS y 54 ABIERTOS** (el acta esperaba 281 y
> 54: coincide, y la coincidencia es de medicion, no de copia), y **la deuda total de P.5
> en 324 pares**. **La medicion se hizo por DOS rutas independientes**, el campo `nota` y
> el campo `cobertura` de las 335 entradas vigentes, **y las dos dan 324**. Antes del
> cambio las dos daban **329**, que es la cifra del acta 17 con su corte.

**5. Los punteros cruzados `ESTRELLA (9.23)` y `nodo puente`: PUESTOS EN LOS DOS SENTIDOS.**
Cada nota dice que la forma mecanica coincide, que **lo que las separa es la CONSECUENCIA**
(arreglese por separado sin mesa, contra cuidado que pueden ser dos familias), y apunta a
la otra. **Y las dos citan el mismo caso que lo prueba:** `sales_roadmap_vs_sales_force`
es estrella por los puestos 319 y 918 con periferico 1023, **y es a la vez el puente del
acto**.

**LA MITAD QUE SE ME OLVIDO Y QUE MI PROPIO INSTRUMENTO DESTAPO.** El punto 4 del encargo
pedia ademas la adicion en la nota de la figura `el forastero por cableado`, **y mi primer
pase de TAREA 1 solo la escribio en la entrada del acto.** Lo levanto
`scripts/loop/vuelta19_fase2.py` al medir el cierre (`candidato condicionado registrado en
esta vuelta: False`), y se corrigio en `scripts/loop/vuelta19_tarea1b.py`, **en su propio
script y con el motivo escrito en su cabecera, para que el orden real se pueda auditar en
vez de quedar disimulado dentro del script anterior.**

---

## 3. TAREA 2.B: las tres figuras que faltaban

**Instrumento: `scripts/loop/vuelta19_figuras.py`.** Criterio de ejemplar: el de la vuelta
18, **CONFIRMADO por el acta de la vuelta 18** (seccion 3, adjudicacion 1).

### 1. `SUBCONJUNTO ESTRICTO`: los 23, nombrados y verificados

**Las 23 que el campo `cobertura` declara son EXACTAMENTE las 23 razones del archivo que
traen la etiqueta `SUBCONJUNTO ESTRICTO` en mayusculas**, y no es una coincidencia elegida
a posteriori: **la aritmetica del informe reproduce exacta sobre ese conjunto.** El informe
declara *de 12 ejemplares a 23, once nuevos en el tramo*; medido hoy, **los puestos con la
etiqueta anteriores a ese tramo son DOCE y los once nuevos son esos once. 12 mas 11, 23.**

**Los 23 verificados uno por uno contra el archivo (existe, clase A, entre esos dos nodos):
CERO FALLOS y LOS 23 EN A.** Core 1182, 1332, 1573; entrega 1601 y 1602; environmental
1776, 1783, 1794, 1811; **exportacion siete** (1943, 1947, 1952, 1966, 1967, 2022, 2043);
**franquicias siete** (2072, 2074, 2075, 2076, 2079, 2087, 2090).

> **DISCREPANCIA DECLARADA, con la cifra vieja intacta: el 23 cuenta ETIQUETAS, no
> INSTANCIAS.** El puesto **511** esta **declarado por escrito** como subconjunto estricto
> en el informe (tabla de la tanda R30: *"NADA. Es un subconjunto estricto"*) y ademas **las
> razones del 1783 y del 1943 lo citan por su numero** dentro de la nomina corriente de la
> figura. **Su propia razon no trae la etiqueta.** Contando instancias declaradas por
> escrito son **24**. **El campo `cobertura` no se toca.**

### 2. `LA FIRMA POSICIONAL DEL INJERTO (P.2)`: las dos sedes, con los punteros verificados

**DONDE VIVEN LOS 67:** `docs/plan/10_INVENTARIO.md`, seccion *LAS FUENTES, ya
normalizadas*, tabla *LOS SEIS QUE APORTAN INJERTOS*. **Reproducida celda por celda con mi
instrumento sobre el grafo, y calza entera:**

| libro | 1a o unica | 2a o posterior |
|---|---:|---:|
| Hugos | **107** | **21** |
| Coleman | **68** | **15** |
| Horowitz | **88** | **14** |
| Weinberg | **67** | **13** |
| Rackham | **47** | **4** |
| Mollick | **47** | **3** |

**La columna de segunda posicion suma 70 por libro y los NODOS DISTINTOS son 67**, porque
tres nodos declaran dos de los seis a la vez: `metas_vs_proposito`, `viral_loop_marketing` y
`principio_calidad_mvp`. **Y los 67 salen tambien por la via corta y dan el mismo conjunto
exacto:** los nodos vivos cuyo campo `fuente` trae mas de un libro son **67**.

**DONDE VIVE LA NOMINA DE LOS 43:** `docs/plan/01_FUENTES.md`, seccion *LA TANDA DE LOS
INJERTOS: leidos los 43*, con su saldo, su tabla por grupo y sus cuatro decisiones de
fuente. **Los 21 de Hugos estan nombrados uno a uno en `BANCO_DEL_PLAN.md`, ficha P.2.**
**Diez ejemplares citables por nodo verificados contra el grafo**, los cuatro con corte
exacto, los tres que no son un simple apendice y los tres de Mollick.

> **DOS DISCREPANCIAS DECLARADAS, con las cifras viejas intactas.** **PRIMERA:** la tanda de
> los cuatro libros mide **44 nodos distintos** con mi instrumento y el doc publica **43**.
> **La diferencia entera es Horowitz**, que figura con **14** en la tabla de sede de
> `10_INVENTARIO.md` y con **13** en la tabla de grupos de `01_FUENTES.md`. **Cual de los 14
> queda fuera NO se puede decir, porque la nomina de los 13 no esta escrita en ninguna
> parte:** del grupo solo hay conteos. **SEGUNDA:** `01_FUENTES.md` explica el paso de 46
> declaraciones a 43 nodos nombrando tres solapes, y uno de los tres es
> `decision_de_vender_startup` por declarar Horowitz dos veces; **medido hoy ese caso no
> reduce esa cuenta** (un nodo que declara el mismo libro dos veces sigue siendo un nodo y
> un libro), y **los nodos que si declaran dos libros distintos de los cuatro son solo DOS**.

### 3. `EL PASO DE OFICIO`: tres ejemplares declarados, y la cota que callaba de menos

**LOS EJEMPLARES DECLARADOS POR ESCRITO SON TRES, Y ESTABAN EN EL SITIO DONDE LA VUELTA 18
NO MIRO: en la razon de los propios veredictos, que nombran la figura POR SU NOMBRE.**

| puesto | clase | el par | lo que su razon declara |
|---:|:--:|---|---|
| **2045** | D | `barreras_comerciales_no_arancelarias` contra `import_regulations_foreign_governments` | *comparten el paso de oficio del dominio*, y define la figura entera, incluida la frase **media docena** |
| **2054** | D | `export_administration_regulations` contra `import_regulations_foreign_governments` | *lo compartido es el paso de oficio del dominio, preguntarle al servicio comercial. Ni un paso mas se solapa* |
| **2070** | D | `barreras_comerciales_no_arancelarias` contra `export_administration_regulations` | *lo compartido es el paso de oficio del dominio. Ni un paso mas se solapa* |

**El 2045 es la sede de la frase `media docena`: es el unico puesto del archivo que la
trae.** Los seis nodos de la cota y los diez pares quedan renombrados en la nota con la
cota ya corregida a 141 vivos, **los seis verificados vivos y los diez verificados contra
el archivo** (1963 A, 1984 A, 1989 D, 2007 D, 2011 D, 2013 D, 2026 D, 2045 D, 2047 D,
2070 D).

> **Y AQUI ESTA LA MEDICION QUE MAS PESA DE ESTA VUELTA. La heuristica de la vuelta 18 no
> callaba un poco: callaba veinte nodos, y por una cadena mal escrita.** Su lista de pistas
> trae **`us commercial service` sin puntos**, y el grafo escribe **`U.S. Commercial
> Service`**: **esa cadena no casa nunca.** Recontado sobre los **mismos 141 vivos**,
> cambiando solo esa cadena por `commercial service`:

| | criterio de la vuelta 18 | criterio con la cadena corregida |
|---|---:|---:|
| nodos con la linea generica | **6** | **26** |
| de esos, con la linea en su **PASO 1** | **2** | **7** |
| pares del dominio que tocan a alguno | **10** | **40** |

> **LA PRUEBA DE QUE ESTO ES UN FALLO DE CADENA Y NO UNA DEFINICION MAS ANCHA: de los tres
> nodos que sostienen los tres ejemplares DECLARADOS, dos no aparecian en la cota de seis**,
> y uno de esos dos, `import_regulations_foreign_governments`, **trae la linea en su PASO
> 1**: *Consultar con el U.S. Commercial Service antes de exportar a un nuevo pais*.
>
> **Y la cifra corregida se acerca a lo declarado donde la vieja no llegaba:** el 2045 dice
> **el PRIMER paso de media docena de nodos**, y los nodos con la linea en su paso 1 son
> **SIETE** con la cadena corregida y eran **DOS** con la vieja.

**Las dos cifras quedan escritas con su criterio al lado y ninguna se borra: 6 de 141 y 26
de 141.** El campo `cobertura`, que dice *medio dominio exportacion*, **sigue sin tocarse**:
medido son 26 nodos de 141 vivos y 40 pares de 130.

---

## 4. TAREA 2.A: LA PREMISA DEL ENCARGO NO SE SOSTIENE, Y LA NOVENA ESTRELLA YA ESTABA VERIFICADA

**El encargo mandaba leer como `LD-71` el par periferico *que el informe declaro que la cola
no puede cerrar*. Medido en esta vuelta: EL PAR YA ESTABA LEIDO.**

> **Es `LD-04`**, de la primera tanda de lecturas dirigidas del **11 ago 2026**, en
> `docs/plan/LECTURAS_DIRIGIDAS.md`: *`LD-04` . `evaluacion_tecnologias_disruptivas` contra
> `explotacion_tecnologias_disruptivas` . **D***. **Y ese mismo `LD-04` ya declaraba por
> escrito, hace tres dias, lo que esta vuelta iba a buscar:** *"es una **ESTRELLA** del
> banco 9.23, con centro y dos periferios"*.

**LAS DOS CUENTAS DE 9.23, medidas hoy:**

| la cuenta | estado |
|---|---|
| **1. pares con el centro `tecnologias_disruptivas_oportunidad`, todos en A** | **SI**: 505 y 513, y son los **dos unicos** pares del archivo que tocan al centro |
| **2. al menos un par entre perifericos, leido y sano** | **SI**: `LD-04`, **D**, desde el 11 ago 2026 |

> **La novena estrella es EJEMPLAR: las verificadas pasan de OCHO a NUEVE y el campo
> `cobertura`, que dice 9, queda CONFIRMADO en vez de discrepante.**

**LO QUE ESTO CORRIGE, sin tapar nada.** La vuelta 18 escribio que a esta estrella *"le
falta la segunda cuenta"* y el acta de la vuelta 18 lo dio por bueno razonando que el par
*"nunca entro a la cola"*. **Lo segundo es cierto, esta medido, y lo primero no se sigue de
ello:** el par no entro a la cola **y aun asi estaba leido**, porque para eso existen las
lecturas dirigidas. **La busqueda no fallo en encontrar el centro: fallo en buscar la
segunda cuenta en un solo sitio.** Y es exactamente el limite que el propio reporte 18 ya
habia escrito en su seccion 4 (*"dos de las trece figuras tienen ejemplares que viven en
LECTURAS DIRIGIDAS y no en el archivo de veredictos"*), **aplicado a una tercera figura y no
visto.** La regla 8 del ejecutor es la que lo destapa: *una busqueda negativa no se puede
citar*.

**LA RELECTURA, hecha igual y entera**, esta en `docs/plan/LD_ESTRELLA_DISRUPTIVAS.md`: los
dos nodos impresos, la vara del **9.6.3** aplicada (procedimiento a los dos lados, y los
entregables como senal de verificacion del 9.6.2), y **D**. **Coincide con `LD-04` en la
clase y en el corte de las mitades.**

> **EL LIMITE DE ESA CONCORDANCIA, declarado y no maquillado: no fue una relectura ciega.**
> Lei los nodos y adjudique D antes de abrir `LECTURAS_DIRIGIDAS.md`, pero **la busqueda de
> `LD-04` era parte del mismo trabajo y no monte la ceguera como tal.** Vale menos que una
> ciega de verdad y queda dicho.

**NO ACUNE `LD-71`, y va marcado como discutible.** Un segundo numero para un par ya
adjudicado seria **una segunda fuente de verdad para un solo veredicto**, y quien cuente
lecturas dirigidas contaria el mismo par dos veces. **Si el auditor prefiere que el numero
se acune igual, se acuna en la vuelta 20: no lo decido yo.**

---

## 5. CORRECCIONES Y DISCREPANCIAS DECLARADAS, ninguna arreglada por mi

**Seis, y las seis con la cifra vieja intacta al lado.**

| # | donde | la cifra vieja | lo medido hoy |
|---:|---|---|---|
| 1 | nota de `LA BIFURCACION` | la palabra en **un solo puesto**, el 2198, y no es ejemplar | **siete puestos**, y **dos son los ejemplares**. Solo la forma en mayusculas es del 2198 |
| 2 | nota de `EL PASO DE OFICIO` | **158 nodos vivos** | **158 en el grafo, 17 deprecado, 141 VIVOS**. Cota corregida **6 de 141** |
| 3 | nota de `ESTRELLA (9.23)` | *la novena no se encontro* y *le falta la segunda cuenta* | **localizada y VERIFICADA 9 de 9**: `LD-04`, D, del 11 ago 2026 |
| 4 | `cobertura` de `SUBCONJUNTO ESTRICTO` | **23 ejemplares** | 23 **etiquetas**; instancias declaradas por escrito, **24** (falta el 511) |
| 5 | `cobertura` y sedes de `LA FIRMA POSICIONAL` | **43 confirmados**, Horowitz 13 en una sede y 14 en otra | **44 nodos distintos** con mi instrumento; el nodo que sobra **no es identificable** porque la nomina de los 13 no esta escrita |
| 6 | nota de `EL PASO DE OFICIO`, la cota | **6 nodos y 10 pares** | con la cadena corregida, **26 nodos y 40 pares** sobre los mismos 141 vivos |

**Y UNA SEPTIMA QUE NO ES DE UNA CIFRA SINO DE TRES SEDES QUE CUENTAN LO MISMO.** Tras el
registro de TAREA 1.4, **el mismo acto se cuenta de tres maneras**:

| sede | el acto del sales roadmap | la deuda total de P.5 |
|---|---|---:|
| `INVENTARIO.jsonl`, entrada de tipo `acto` | **15 de 15, CERRADO** | **324** |
| `RECOMPUTO_3388_COMPONENTES.jsonl` | 10 de 15, ABIERTO, 5 fuera de cola | **329** |
| `INVENTARIO.jsonl`, entrada de tipo `racimo` *el sales roadmap* | 10 de 15, MEZCLADO | no la cuenta |

> **La diferencia entre 324 y 329 son EXACTAMENTE los cinco pares de `LD-66` a `LD-70`, y no
> hay ninguna otra: lo comprobe par por par.** **Las dos primeras son correctas para lo que
> cada una mide:** el archivo de componentes es una foto del cierre transitivo al corte
> 3.388 y **no recoge lecturas dirigidas por diseno**. **Quien cite 329 tiene que decir de
> que sede sale.** **La tercera es el caso distinto:** la entrada de `racimo` mide la misma
> nomina que la de `acto` y **no tiene motivo para diferir**. **No la toque porque el
> encargo scopeaba la entrada de tipo `acto`**, y va como pregunta en la seccion 8.

---

## 6. PENDIENTES DE DOCTRINA

**Uno, y no paro el trabajo.**

**1. QUE HACER CON UN PAR QUE UN ENCARGO MANDA LEER Y YA ESTA LEIDO.** No esta escrito en
ninguna parte. **Lo mejor sostenido que encontre y lo que hice: no acunar numero nuevo,
escribir la relectura entera como relectura, y dejar la decision del numero al auditor.**
El motivo es la unica regla escrita que toca el caso de lejos, la de no dejar dos cifras
diciendo lo mismo sin aviso (adjudicacion 9 de la vuelta 17). **Si la casa prefiere acunar
siempre, la regla se escribe y se acuna en la vuelta 20.**

**LOS TRES DE LA VUELTA 18 quedan cerrados por sus adjudicaciones y por este trabajo:** el
criterio de ejemplar quedo confirmado y esta escrito dentro de las notas; el puntero cruzado
estrella y puente esta puesto en los dos sentidos; y la novena estrella esta localizada,
leida y verificada.

---

## 7. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Nueve, y los marco sin saber como salen.**

1. **NO ACUNAR `LD-71`.** El encargo lo pedia por su nombre y no lo acune, porque el par ya
   era `LD-04`. **Si la casa entiende que el encargo manda acunar igual, esto es una orden
   no ejecutada**, y lo escribi sabiendolo.
2. **REORDENAR EL TRABAJO: escribi `LD_ESTRELLA_DISRUPTIVAS.md` y el registro de la novena
   en el MISMO tramo de TAREA 1**, cuando el encargo pone esa lectura en TAREA 2.A. Lo hice
   porque escribir en TAREA 1 la frase *sigue sin la segunda cuenta*, que el encargo dictaba,
   **habria sido publicar algo que yo ya sabia falso**. **Elegi la regla 1 sobre el orden del
   encargo.**
3. **LA COTA AMPLIADA DE `EL PASO DE OFICIO`: 26 nodos.** Cambie una cadena de la lista de
   pistas y la cota se cuadruplico. **Sostengo que es un fallo de cadena y no una definicion
   nueva, y la prueba que doy son los dos nodos de ejemplares declarados que la cota vieja no
   veia.** Pero **es mi criterio contra el de la vuelta 18, que el acta 18 verifico y dio por
   bueno**, y puede que la casa lea esto como que yo ensanche la definicion.
4. **CONTAR 24 INSTANCIAS EN `SUBCONJUNTO ESTRICTO` cuando la cobertura dice 23.** Todo
   depende de si la razon de un veredicto cuenta como *declaracion por escrito*. **Yo digo
   que si, y por eso el 511 suma**; si la casa dice que solo cuentan informe, banco,
   expediente y lectura dirigida, **entonces el 511 sigue sumando igual porque esta en el
   informe**, y el que sobra soy yo contando la etiqueta. **Es el discutible que peor
   entiendo de los nueve.**
5. **DECIR QUE LA TANDA DE LOS INJERTOS SON 44 Y NO 43.** Mi cuenta depende entera de contar
   Horowitz por 14, que es lo que dice una de las dos sedes. **Si la buena es la otra sede,
   mi 44 es un artefacto de haber elegido la tabla equivocada.** Declare las dos y no arregle
   ninguna, pero **publique el 44 como mi medicion**.
6. **NOMBRAR LOS TRES EJEMPLARES DE `EL PASO DE OFICIO` desde la razon del archivo y no desde
   el informe.** Es una sede que el criterio de la vuelta 18 no listaba entre las cuatro.
   **La anadi a la formula del criterio dentro de las notas nuevas**, y eso es tocar un
   criterio que el acta 18 confirmo tal como estaba.
7. **NO TOCAR LA ENTRADA DE TIPO `racimo` del sales roadmap**, sabiendo que queda diciendo
   *10 de 15* a ocho lineas de una entrada de `acto` que dice *15 de 15*. **Me acogi al
   scope del encargo.** Puede que la doctrina de no dejar dos cifras sin aviso pesara mas
   que el scope, y entonces deje una divergencia viva que podia haber avisado.
8. **PONER EL TEXTO NUEVO AL FRENTE DEL CAMPO `nota` del acto**, y no al final como en las
   figuras. Lo hice porque el encargo decia *lo nuevo al frente* y porque **cualquier lector
   mecanico que busque la primera cifra de cola en esa nota se habria llevado la vieja**.
   Pero **rompe el patron de adicion al final** que las once notas de la vuelta 18 usaron.
9. **DECLARAR QUE LAS SIETE FIGURAS SIN MARCA DE TANDA "NACIERON NOMBRADAS".** Lo comprobe
   entrada por entrada leyendo sus notas, **pero no verifique sus ejemplares contra el
   archivo uno por uno**, que es lo que si hice con las trece. **Si alguna de las siete cita
   un puesto que no calza, mi 20 de 20 se cae.**

---

## 8. LAS PREGUNTAS QUE TRAIGO, porque no las puedo medir

1. **¿Se acuna `LD-71` o no?** El par esta leido, releido y concordante. **Lo unico que
   falta decidir es si la casa quiere un numero nuevo para la relectura.**
2. **¿Quien arregla la entrada de tipo `racimo` "el sales roadmap"?** Hoy dice *10 de 15,
   MEZCLADO* y la entrada de `acto` de la misma nomina dice *15 de 15, CERRADO*. **No la
   toque por scope. Si la doctrina manda avisar, hace falta encargo.**
3. **¿Cual de los dos numeros de Horowitz manda, el 14 de `10_INVENTARIO.md` o el 13 de
   `01_FUENTES.md`?** De eso depende si la tanda de injertos son 43 nodos o 44, **y la
   nomina de los 13 no esta escrita en ningun sitio, asi que no lo puedo resolver
   midiendo.**
4. **¿La cota de `EL PASO DE OFICIO` se regenera con la cadena corregida, o se queda con las
   dos cifras al lado?** Hoy la deje con las dos y su criterio. **Regenerar la cota es
   cambiar una cifra publicada y eso no lo hago sin encargo.**

---

## 9. AL CERRAR: LA FASE II, BLOQUE POR BLOQUE

**Medido con `scripts/loop/vuelta19_fase2.py` y escrito entero en `RECOMPUTO_3388.md`,
seccion TAREA (vuelta 19).**

| bloque | tras la vuelta 17 | **tras esta vuelta** |
|---|---|---|
| la cola de relectura post fusion | VERIFICADA ENTERA, 7 de 7 | **sigue verificada**, remedida hoy |
| el criterio del forastero | VERIFICADOS LOS DOS | **los dos, mas un candidato CONDICIONADO** registrado y no contado |
| el lote de cinco del sales roadmap | LOS CINCO NOMBRADOS | **LEIDOS Y EL ACTO CERRADO** |
| las lecturas de acto entero de P.5 | 280 hechos, 55 pendientes, 329 pares | **281 hechos, 54 pendientes, 324 pares** |
| los ejemplares de las veinte figuras | medido el tamano, NO cerrado | **LAS VEINTE NOMBRADAS** |

> **MI LECTURA, y la digo como lectura y no como veredicto porque el cierre es del auditor:
> el bloque de las veinte figuras QUEDA NOMBRADO, que era lo que faltaba.** Las trece con
> tanda estan nombradas y verificadas contra el archivo; las siete restantes nacieron
> nombradas y sus notas citan nodos y puestos. **Lo que NO queda cerrado, y por eso no digo
> que la FASE II cierre, son las SEIS discrepancias de la seccion 5 y las CUATRO preguntas
> de la seccion 8: ninguna es una figura sin nombrar, pero todas son cifras publicadas que
> hoy tienen dos lecturas y una sola de ellas puede ser la buena.**

**NO ABRI LA FASE III y NO CREE `pasada-unica`.** La verificacion del cierre de la FASE II y
la apertura de la FASE III son del auditor en la vuelta siguiente, tal como el encargo dice.

---

## 10. CONDICIONES DE PARADA: NINGUNA SE CUMPLE

| condicion | estado |
|---|---|
| doctrina nueva | **no**: el unico pendiente va registrado con lo mejor sostenido, y no invente regla |
| contradiccion con regla vigente o cifra publicada con su corte | **no**: las seis discrepancias medidas se declararon **al lado** de la cifra vieja, sin tocarla. **La premisa del encargo que no se sostiene se declaro entera y no se resolvio copiando** |
| decision de fundador | **nada reservado se toco**: `dataset/` y el archivo de veredictos intactos (diff vacio, corrido por mi), cero merges, cero operaciones ejecutadas, FASE III sin abrir, `pasada-unica` sin crear |
| fallo tecnico | **no**: arbol limpio, hook verde en los tres commits, cero guiones largos y cero guiones medios |
| credito de tanda | **no conozco caida mia en esta tanda.** Si el auditor encuentra una, la cuenta manda y el bucle para |
| campana consumada | **no** |

**Commit y push por tramo, tres tramos: los instrumentos (`26c15781`), TAREA 1 mas la
relectura (`945a6a16`) y TAREA 2.B mas el cierre de FASE II (`7b21a8d0`), los tres empujados
a `origin/bucle` segun se cerraban.** Este reporte va en el cuarto.
