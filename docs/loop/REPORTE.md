# REPORTE DE LA VUELTA 18 . Ejecutor: Opus 5 . 14 ago 2026

**FASE II, RECOMPUTO. MODO DE CIERRE.** Cero reparaciones de nodos, cero operaciones
ejecutadas, FASE III sin abrir, `pasada-unica` sin crear.

> **REGLA 1 DEL EJECUTOR, aplicada sin excepcion: toda cifra de este reporte se lee de la
> salida de un instrumento corrido EN ESTA VUELTA.** Las cifras de vueltas anteriores
> aparecen solo como contraste y con su corte al lado. Donde mi medicion discrepa de una
> cifra publicada, **la discrepancia se declara y la cifra vieja no se toca.**

---

## 0. LO PRIMERO: EL HASH, LAS RUTAS Y LO QUE NO SE TOCO

**Hash del TRABAJO: `d697bc06`.** Este reporte se commitea despues, asi que **el hash del
reporte es otro y no es el del trabajo**; se dice porque en la vuelta 17 esa distincion ya
hizo falta.

**Arbol al empezar: LIMPIO y sincronizado con `origin/bucle`.** No habia nada pendiente que
commitear antes de tocar nada, y se comprobo antes de la primera edicion.

**LAS ONCE RUTAS del `git diff --stat 93203f48 d697bc06`, la lista COMPLETA:**

| ruta | que cambio |
|---|---|
| `docs/plan/00_INDICE.md` | TAREA 1.1: el tachado de las sesenta y seis mas el puntero del sales roadmap |
| `docs/plan/10_INVENTARIO.md` | TAREA 1.3: la linea nueva del AVISO |
| `docs/plan/INVENTARIO.jsonl` | TAREA 1.2 (una linea) mas TAREA 2.B (once lineas) |
| `docs/plan/LD_SALES_ROADMAP.md` | **NUEVO**: las cinco lecturas dirigidas `LD-66` a `LD-70` |
| `docs/plan/LECTURAS_DIRIGIDAS.md` | dos lineas: el backlog del sales roadmap pasa a leido, con tachado |
| `scripts/plan/simular_destejido.py` | TAREA 1.4: la etiqueta de aviso orientativo |
| `scripts/loop/vuelta18_medir.py` | **NUEVO**, instrumento de solo lectura |
| `scripts/loop/vuelta18_puntero_defecto.py` | **NUEVO**, escribe una linea de `INVENTARIO.jsonl` |
| `scripts/loop/vuelta18_sales_roadmap.py` | **NUEVO**, instrumento de solo lectura |
| `scripts/loop/vuelta18_figuras.py` | **NUEVO**, instrumento de solo lectura |
| `scripts/loop/vuelta18_nombrar_figuras.py` | **NUEVO**, escribe once lineas de `INVENTARIO.jsonl` |

**LO RESERVADO SIGUE INTACTO, medido y no supuesto:** `git diff --name-only 93203f48
d697bc06 -- dataset/ docs/INTRA_DOMINIO_VEREDICTOS.jsonl` devuelve **CERO lineas**. El
archivo de veredictos conserva sus **3.388** lineas y el cribado sigue **CERRADO en 3.388
de 3.388**.

**Cero guiones largos y cero guiones medios en todo lo tocado**, comprobado archivo por
archivo con un contador propio antes de cada commit. El hook corrio en los tres commits y
dio verde las tres veces.

---

## 1. EL MARCADOR RECOMPUTADO, con instrumento propio de esta vuelta

**Instrumento: `scripts/loop/vuelta18_medir.py`**, de solo lectura, sobre
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/plan/OPERACIONES.jsonl` y
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

**Las diez filas calzan con el acta de la vuelta 17 celda por celda**, incluido el unico
cero del catalogo.

### La vara por tramo

**No hay tramo nuevo que medir: el cribado esta CERRADO y esta vuelta no leyo ni un par de
cola.** Las cinco lecturas de la TAREA 2.A son **dirigidas**, no entran en la cola y **no
mueven el marcador**, exactamente como las 65 anteriores. **Lo unico que se midio por
tramo es la curva de tres dominios**, y esta en la seccion 5 porque destapo una
discrepancia.

### Figuras y familias al dia

| | medido hoy |
|---|---:|
| entradas de `INVENTARIO.jsonl` | **671** |
| de tipo `acto` | **556** (221 superadas mas **335** vigentes) |
| actos vigentes **CERRADOS** / **ABIERTOS** | **280** / **55** |
| `familia_de_ids` | **53**: **23 contenidas, 14 partidas, 16 sin arista A** |
| `figura` | **20** |
| `defecto` | **19**, `racimo` **13**, `dominio` **10** |
| **figuras que NOMBRAN** por el criterio de forma de la vuelta 17 | **18 de 20**, contra **7 de 20** al empezar |
| **el plan** | **71 operaciones, 71 ids unicos, las 71 en LISTA** |

---

## 2. TAREA 1: los cuatro registros, los cuatro aditivos

**1. `00_INDICE.md`.** Tachado sobre *"se ejecutan sesenta y seis operaciones LISTAS"*, con
la cifra de hoy al lado y **remedida, no copiada**: `OPERACIONES.jsonl` tiene **71 lineas,
71 ids unicos y estado LISTA en las 71**, cero en DECISION PENDIENTE. **Y se declaran las
dos diferencias contra el marcador del 12 ago que sigue en esa misma pagina**: la fase 02
lleva **9 y no 7** (`OP-D-08` y `OP-D-09`, las dos con `fecha_corte` 2026-08-14) y
`OP-U-02` **ya no esta pendiente**. El marcador viejo **no se regenera**: se le pone el
aviso. Y la linea de los cinco pares del sales roadmap recibe **el puntero a la nomina** de
`RECOMPUTO_3388.md`, seccion TAREA vuelta 17, punto 4.

**2. `INVENTARIO.jsonl`, la entrada `defecto` "pares que una fusion reabre".** Adicion
declarada **al final** del campo `nota`, con el puntero a `08_VERIFICACION.md` donde el
1096 vive con su motivo. **La regla escrita en la entrada no se reescribe.** Diff de **UNA
linea**: el script comprobo **670 de 671 identicas** antes de escribir y aborta si no lo
son.

**3. `10_INVENTARIO.md`, una linea mas al AVISO.** La frase *"sin pares pendientes: no
puede crecer"* mide **los pares INTERNOS**. Medido en esta vuelta: **280 de las 335 notas
de acto vigentes la llevan**, y el ejemplar que la desmiente es
`gestion_terminacion_franquiciado`, cuya entrada del corte 2.117 decia *"tamano 2. Sin
pares pendientes: no puede crecer"* con **1 de 1 pares leidos, 0 en cola y 0 fuera de
cola**, y que hoy tiene **tres miembros** porque entro `perdida_control_operativo` **por la
A del puesto 2190**, un nodo de fuera. **Las 335 notas NO se reescriben.** Queda escrito
que quien regenere escribe **"sin pares internos pendientes: no puede crecer POR DENTRO"**.

**4. `simular_destejido.py`.** La salida de la heuristica de referencias colgando **dice
ahora con palabras que es AVISO ORIENTATIVO, no veredicto y no rotura**, en los dos casos:
cuando encuentra algo y cuando no encuentra nada (**ese cero tampoco es un certificado**).
**Ningun criterio del simulador cambio**: la corrida de humo contra `lienzo_modelo_negocio`
da el mismo VEREDICTO DEL ESCENARIO que antes.

---

## 3. TAREA 2.A: los cinco del sales roadmap, `LD-66` a `LD-70`

**Documento entero en `docs/plan/LD_SALES_ROADMAP.md`**, con el patron de
`LD_ADOPT_ADVOCATE.md`: numero propio, nodos impresos, clase y razon.

| LD | el par | clase |
|---|---|:--:|
| `LD-66` | `customer_validation_sales_roadmap` contra `estrategia_de_ventas` | **D** |
| `LD-67` | `customer_validation_sales_roadmap` contra `sales_roadmap` | **D** |
| `LD-68` | `estrategia_de_ventas` contra `hoja_de_ruta_de_ventas` | **A** |
| `LD-69` | `estrategia_de_ventas` contra `refinar_sales_roadmap` | **D** |
| `LD-70` | `estrategia_de_ventas` contra `sales_roadmap_vs_sales_force` | **D** |

**Saldo 1 A y 4 D. La cobertura del acto cierra en 15 de 15 y su deuda de P.5 baja a
CERO.**

### La pregunta de P.5, contestada por escrito

**Por la letra del criterio (9.24, componente conexa) el acto es UNO, y ya lo era antes de
estas lecturas:** medido con las seis A del archivo solas, los seis nodos formaban **una
sola componente**. Las cinco de hoy anaden una A y **no mueven el conteo**. Lo que mueven
es la FORMA.

**Por la forma son DOS familias pegadas**, y la prueba se corrio con instrumento
(`scripts/loop/vuelta18_sales_roadmap.py`), quitando primero cada nodo y despues cada
arista:

| se quita | componentes que quedan |
|---|---|
| `refinar_sales_roadmap` | **2**, de 3 y de 2 |
| `sales_roadmap_vs_sales_force` | **2**, de 4 y de 1, con `customer_validation_sales_roadmap` **SUELTO** |
| cualquiera de los otros cuatro nodos | 1 de 5 |
| **la A del puesto 918** | **2**, de **4** y de **2** |
| **la A del puesto 319** | **2**, de **5** y de **1** |
| las otras cinco A (966, `LD-68`, 200, 255, 192) | 1 de 6, **ninguna corta** |

> **UN NUCLEO DE CUATRO** (`sales_roadmap`, `hoja_de_ruta_de_ventas`,
> `refinar_sales_roadmap`, `estrategia_de_ventas`; **5 de sus 6 pares en A**) **Y UNA COLA
> DE DOS** (`customer_validation_sales_roadmap` y `sales_roadmap_vs_sales_force`, su unico
> par en A), **cosidos por la cadena 918 mas 319, las dos por el mismo nodo.**

**`estrategia_de_ventas` PERTENECE, no es forastero**, y falla las tres senales de la
figura: tiene **dos A dentro del nucleo** (966 y `LD-68`), tiene a `refinar_sales_roadmap`
**entre sus `nodos_previos`**, y **no entro por el nombre**. **La sospecha del encargo
apuntaba al nodo equivocado.**

**Y el que SI cumple el perfil del forastero es el nodo que le da NOMBRE al acto**,
`customer_validation_sales_roadmap`: **cuatro D contra el nucleo**, su unica A hacia la
cola, y **sus seis aristas apuntando todas fuera del acto**. Esto **no se pidio, sale de la
medicion, y se declara sin ejecutar.**

### Tres propuestas al plan, DECLARADAS y NO ejecutadas

**Medido: de las 71 operaciones LISTAS, NINGUNA funde este acto.** La unica que nombra a
alguno de los seis nodos es `OP-M-02-PROG`, y lo nombra **como arista entrante que su
simulacion redirige**. **Ninguna operacion LISTA queda contradicha.**

| # | la propuesta | su consecuencia si se adjudica |
|---:|---|---|
| **1** | la entrada de tipo `acto` pasa de **10 de 15** a **15 de 15** y de ABIERTO a CERRADO | los actos abiertos pasarian de **55 a 54**, los cerrados de **280 a 281**, y la deuda de P.5 de **329 pares a 324** |
| **2** | el acto es candidato a **partirse en dos**, cuatro mas dos, cosidos por el 918 | cambia la nomina de una fusion futura, no una operacion de hoy |
| **3** | `customer_validation_sales_roadmap` es candidato a **tercer ejemplar de la figura del forastero** | la figura pasaria de 2 a 3 ejemplares |

> **La 2 y la 3 no son independientes: si el acto se parte, el forastero deja de serlo,
> porque pasa a ser la mitad de su propia familia de dos.** Se dicen las dos y las adjudica
> quien pueda.

**Lo que estas cinco NO cambian:** la clase del racimo. Sigue **MEZCLADO** desde el 872.
**El motivo escrito para no leerlos acerto en lo suyo y erro en lo otro:** la clase no se
movio, **la forma si**.

---

## 4. TAREA 2.B: las diez figuras chicas, nombradas

**Once entradas de tipo `figura` reciben adicion ADITIVA al final de su `nota`.** Diff de
**once lineas**: **660 de 671 identicas byte a byte**, y **ninguna otra clave cambia en
ninguna de las once** (el script compara el resto del objeto antes y despues y aborta si
difiere). Instrumento de verificacion: `scripts/loop/vuelta18_figuras.py`.

> **EL CRITERIO DE EJEMPLAR QUE USE, escrito para que se pueda discutir y marcado como
> discutible mas abajo: un ejemplar es una instancia DECLARADA POR ESCRITO** (en el
> informe, en el banco, en un expediente o en una lectura dirigida), **no cualquier par que
> calce con la forma.** Cada puesto citado esta **verificado contra el archivo**: existe,
> con esa clase y entre esos dos nodos.

| figura | ejemplares nombrados | verifica |
|---|---|:--:|
| **LA VARA EN LOS DOS SENTIDOS (9.22)** | polo 1: **1077** C, **1240** C y **`LD-02`**; polo 2: **2080** A y **2105** A; mas el contraste **2091** D | 5 de 5 |
| **ESTRELLA (9.23)** | **ocho** centros con sus radios y su periferico: 467/511/639 mas 636 y 1346; 184/820 mas 1201; 251/799 mas 1348; 507/641 mas 572; 1601/1602 mas 1609; 1966/1967 mas 1972; 2076/2090 mas 2086; 2074/2075 mas 2092 | 8 de 8 |
| **TRIANGULO ABIERTO** | **1497, 1509, 1558** (los mercados de varios lados) y **377, 854, 855** (el proceso a tres alturas) | 6 de 6 |
| **EL ESQUELETO COMPARTIDO** | **2001**, **2011** y **`LD-02`** | 3 de 3 |
| **LAS DOS ADUANAS** | **2008, 2013, 2037, 2054, 2070**, repartidos entre cuatro nodos | 5 de 5 |
| **LA BIFURCACION** | **2030** y **2050**, los dos colgando de `certificados_genericos_de_origen` | 2 de 2 |
| **LOS DOS PARES QUE NO SE CRUZAN** | **1942** y **1969** en A, **2034** y **2059** en D, sobre cuatro nodos | 4 de 4 |
| **LA A DE BLOQUE (P.4)** | ejemplar **`LD-06`**, contraejemplo **`LD-07`**, con la fuente doble verificada contra el grafo | 2 de 2 |
| **LA COLA DEL DOMINIO SE AGOTA POR DENTRO (9.27)** | los tres dominios con sus rangos de puesto y sus tercios **remedidos hoy** | 3 de 3 |
| **cobrar una A sin fundir** | la A del **puesto 488**, mas la segunda del mismo nodo, el **801** | 2 de 2 |

**Veintidos ejemplares verificados uno por uno contra el archivo, CERO fallos**, y las ocho
estrellas verificadas **con las DOS cuentas que 9.23 exige**, no con una.

**`EL PASO DE OFICIO`: ACOTADA y NO nombrada, como pedia el encargo.** Medido sobre el
grafo y sobre las 3.388 lineas: el dominio `exportacion` tiene **158 nodos vivos** y **130
pares leidos**; **SEIS de los 158 nodos** traen la linea generica de la oficina
(`barreras_comerciales_no_arancelarias` paso 1, `desmitificacion_barreras_exportacion` paso
2, `ecosistema_global_emprendimiento_gee` paso 1, `investigacion_empresa_extranjera` pasos
4 y 5, `programas_ex_im_bank` paso 6, `resolucion_problemas_de_pago` paso 2); **DOS** la
traen en su paso 1; y **DIEZ de los 130 pares** tienen al menos un lado con ella. **El seis
confirma la media docena** que la nota ya declaraba, que era su unico numero escrito. **El
criterio es una heuristica de palabras, asi que la salida es una COTA y un aviso
orientativo, no un veredicto: puede callar de menos.** Nombrar sus ejemplares **sigue
pendiente**.

### Por que el grep nunca iba a servir, ahora con cifra en vez de con argumento

**La vuelta 15 descarto el grep y la vuelta 16 lo confirmo sobre las veinte. Esta vuelta
mide POR QUE, y la cifra es mas fuerte que el argumento:**

| figura | ejemplares **declarados** | pares que **calzan con la forma**, contados a maquina |
|---|---:|---:|
| **TRIANGULO ABIERTO** | **2** | **1.773** al corte 3.388, y **1.354** ya al corte 2.117 |
| **ESTRELLA (9.23)** | 9 declarados, **8 localizados** | **33** centros que pasan las dos cuentas |

> **La figura no es la forma: es la forma MAS la lectura**, y por eso ni un contador de
> palabras ni un contador de estructuras la mide. **Y hay una consecuencia practica que no
> estaba escrita: dos de las trece figuras tienen ejemplares que viven en LECTURAS
> DIRIGIDAS y no en el archivo de veredictos** (`EL ESQUELETO COMPARTIDO` con `LD-02`, `LA
> A DE BLOQUE` con `LD-06` y `LD-07`). **Ningun barrido sobre
> `INTRA_DOMINIO_VEREDICTOS.jsonl` los iba a encontrar nunca, porque no estan ahi.**

---

## 5. CORRECCIONES Y DISCREPANCIAS DECLARADAS, ninguna arreglada por mi

**Las tres salen de remedir cifras publicadas y las tres se dejan escritas al lado de la
cifra vieja, sin tocarla.**

**1. `ESTRELLA (9.23)` declara NUEVE ejemplares y solo localice OCHO declarados por
escrito.** La novena no se encontro. **El candidato mas probable es
`tecnologias_disruptivas_oportunidad`** (dos A, puestos **505** y **513**), y **NO lo cuento
como ejemplar a proposito**: su par entre perifericos **nunca entro a la cola**, o sea que
**le falta la segunda cuenta**, y el propio 9.23 dice que sin ella no se puede llamar
estrella. **El campo `cobertura` no se toca.**

**2. `LA COLA DEL DOMINIO SE AGOTA POR DENTRO (9.27)`: su tercer dominio se midio
ABIERTO.** Remedido hoy con mi corte de tercios declarado (n dividido entre 3 sobre el
orden de puesto):

| dominio | primer tercio | segundo | ultimo | cierre |
|---|---:|---:|---:|---:|
| `environmental`, puestos 1772 a 1941, 170 pares | 32,1% | 12,5% | **6,9%** | 17,1% |
| `exportacion`, puestos 1942 a 2071, 130 pares | 30,2% | 2,3% | **2,3%** | 11,5% |
| `franquicias`, puestos 2072 a 2219, 148 pares | 20,4% | 4,1% | **12,0%** | 12,2% |

> **Los dos primeros bajan. El tercero YA NO.** La figura se escribio el 11 ago 2026 con
> `franquicias` **abierto y 32 pares leidos**, dando 66,7% en su primer tercio y 0,0% en el
> ultimo. **Hoy el dominio esta cerrado con 148 pares y su ultimo tercio SUBE a 12,0%.** La
> cifra vieja era correcta para su corte y no se toca. **Lo que la remedicion dice es que
> el tercer ejemplar de esta figura se midio abierto, que es exactamente el error contra el
> que la propia figura avisa.** La figura sigue en pie en sus dos primeros dominios.

**3. `EL PASO DE OFICIO` dice "medio dominio exportacion" y medido son 6 nodos de 158 y 10
pares de 130.** Cifra vieja intacta.

**Y una diferencia de metodo que declaro para que nadie compare mal:** mis tercios de la
tabla de arriba **no son los del informe** (el informe daba `environmental` 34,5 / 24,0 /
7,3). **La direccion es la misma; los numeros no, porque el corte de tercios es distinto.**
No corrijo el informe: declaro que mi corte es otro y cual es.

---

## 6. PENDIENTES DE DOCTRINA

**Ninguno paro el trabajo. Los tres van registrados y con lo mejor sostenido escrito, como
manda la regla 4.**

**1. QUE ES UN EJEMPLAR DE UNA FIGURA. No esta escrito en ningun sitio.** Yo use
**instancia declarada por escrito**, y la alternativa **par que calza con la forma** da
1.773 contra 2 en una figura y 33 contra 8 en otra. **La eleccion no es cosmetica: decide
si las cifras de cobertura de las veinte figuras estan bien o estan mal por dos ordenes de
magnitud.** Lo dejo escrito dentro de cada nota tocada para que se pueda revertir de una
sola pasada si el auditor prefiere la otra definicion.

**2. `ESTRELLA (9.23)` DE DOS RADIOS Y `nodo puente` SON LA MISMA FORMA MECANICA, y son
dos entradas distintas del inventario.** Medido: la definicion de estrella (un centro con A
a dos perifericos que entre si no son A) y la de nodo puente (*"el que tiene A con dos
nodos que entre si son D"*) **coinciden**. Mi propio instrumento levanto
`sales_roadmap_vs_sales_force` **como estrella** por los puestos 319 y 918 con periferico
1023, y es **exactamente el nodo puente** que la TAREA 2.A encontro. **La diferencia no
esta en la forma: esta en la consecuencia** (la estrella dice *arreglese por separado, sin
mesa*; el puente dice *cuidado, puede que sean dos familias*). **No invento la regla que las
separe. Se registra y sigue.**

**3. LA NOVENA ESTRELLA no se localizo**, y la salida que sostengo es la del punto 1 de la
seccion 5: no inventarla y dejar el candidato nombrado con el motivo por el que no cuenta.

---

## 7. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Diez, y los marco sin saber como salen.**

1. **El criterio de ejemplar de la vuelta 18.** Elegi *instancia declarada por escrito*. Si
   la FASE II esperaba *todo par que calce con la forma*, **las diez notas que escribi
   nombran lo que no era**, y ademas nueve de las diez coberturas estarian mal por mucho.
2. **`LD-68` en A es la lectura de la que cuelga toda la estructura de la TAREA 2.A.** Es
   la unica A de mi tanda. Si cae a D, `estrategia_de_ventas` se queda con una sola A (el
   966), el nucleo pasa de cuatro a tres y **mi conclusion de que pertenece se debilita
   mucho**. La marque sabiendo que es la pata unica.
3. **`LD-69` en D contra los puestos 200 y 192, que dieron A con nodos parecidos.** Mi
   motivo es que a `estrategia_de_ventas` le falta el paso de DOCUMENTAR que hacia repetir
   a los otros dos con `refinar_sales_roadmap`. **Es una distincion fina y puede que sea
   demasiado fina.**
4. **Llamar candidato a forastero al nodo que le da NOMBRE al acto.** No se pidio, sale de
   la medicion, y **es la clase de hallazgo que resulta ser un artefacto de como se nombran
   las componentes**. Lo declare como propuesta y no lo ejecute, pero lo escribi con
   enfasis.
5. **Nombrar `LD-02` como ejemplar de DOS figuras a la vez** (el esqueleto compartido y el
   primer polo de la vara). Es la lectura literal de lo que ese `LD` dice de si mismo, pero
   **puede ser que una figura no admita compartir ejemplar con otra**.
6. **Contar el puesto 2091 dentro de la nota de LA VARA aunque no sea ejemplar.** Lo escribi
   aparte y con su motivo, pero **mete un puesto que no es ejemplar en el campo donde
   alguien va a contar ejemplares**.
7. **Tocar `LECTURAS_DIRIGIDAS.md`.** El encargo no lo nombraba. Lo hice porque su backlog
   decia *"sales roadmap, 5 pares, no se lee"* y eso **ya no es cierto desde esta misma
   vuelta**, y la doctrina adjudicada dice que una cifra vieja sin aviso miente. **Fue
   iniciativa mia y va declarada.**
8. **El aviso de `00_INDICE.md` declara dos diferencias de marcador y no regenera el
   marcador.** Elegi la contencion de la vuelta 17 (aviso, no regeneracion), pero **la
   pagina queda con un marcador que dice 69 y 68 y un aviso que dice 71 y 71 a diez lineas
   de distancia**.
9. **`EL PASO DE OFICIO` ahora PASA el criterio de forma de la vuelta 17 sin que yo haya
   nombrado ni un ejemplar suyo**, porque su nota trae ids de nodo que son la COTA, no los
   ejemplares. **Es un falso positivo del criterio de la vuelta 17, y lo produje yo.** Por
   eso el 18 de 20 de la seccion 1 hay que leerlo con esta linea al lado.
10. **Publicar mis tercios sabiendo que no son los del informe.** Podia haber reproducido
    el corte del informe antes de medir, como manda la leccion del auditor de la vuelta 17.
    **No lo hice: declare mi corte en vez de reproducir el suyo**, y por eso la fila de
    `environmental` no calza con la publicada.

---

## 8. LAS PREGUNTAS QUE TRAIGO, porque no las puedo medir

1. **¿La FASE II cierra con esto, o le falta el bloque grande?** De las trece figuras sin
   nombrar quedan **tres**: `SUBCONJUNTO ESTRICTO` (23 ejemplares), `LA FIRMA POSICIONAL
   DEL INJERTO` (67 candidatos, 43 confirmados) y `EL PASO DE OFICIO`, que esta acotada
   pero no nombrada. **Las tres eran las excluidas del encargo de esta vuelta.** No decido
   si el bloque que cierra la FASE II se considera hecho con diez de trece.
2. **¿Las tres propuestas de la TAREA 2.A entran en `OP-U-02` o abren operacion propia?**
   La primera cambia una entrada de inventario y dos cifras agregadas; la segunda cambia
   una nomina; la tercera cambia una figura. **Ninguna la ejecuto y ninguna tiene hoy
   operacion que la recoja.**
3. **¿La novena estrella existe?** Si el auditor la localiza, mi cifra de ocho es una caida
   de reporte mia y quiero que se cuente como tal.

---

## 9. CONDICIONES DE PARADA: NINGUNA SE CUMPLE

| condicion | estado |
|---|---|
| doctrina nueva | **no**: los tres pendientes van registrados, ninguno se resolvio inventando regla |
| contradiccion con regla vigente o cifra publicada con su corte | **no**: las tres discrepancias medidas se declararon **al lado** de la cifra vieja, sin tocarla |
| decision de fundador | **nada reservado se toco**: `dataset/` y el archivo de veredictos intactos, cero merges, cero operaciones ejecutadas, FASE III sin abrir, `pasada-unica` sin crear |
| fallo tecnico | **no**: arbol limpio, hook verde en los tres commits, cero guiones |
| credito de tanda | **no aplica a esta vuelta** |
| campana consumada | **no** |

**Commit y push por tramo, tres tramos: TAREA 1 (`6b8fd72b`), TAREA 2.A (`12c99b95`) y
TAREA 2.B (`d697bc06`), los tres empujados a `origin/bucle` segun se cerraban.** Este
reporte va en el cuarto.
