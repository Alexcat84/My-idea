# REPORTE DE LA VUELTA 32 (ejecutor Opus 5). FASE III, rama `pasada-unica`

**EL 14vo DE HOROWITZ QUEDA RESUELTO Y LA FASE 01 SE RE-CIERRA EN 14 DE 14. `OP-D-01`, la
primera de la fase 02 y la que paro la vuelta 31, QUEDA EJECUTADA en sus cuatro movimientos.
Y el modo continuo se detuvo en la SIGUIENTE, `OP-D-02`: su fusion no se puede ejecutar tal
como esta escrita, y va como PARADA con tres motivos medidos y CERO nodos tocados.**

- **Hash de partida:** `ec6eefa4` (la decision del fundador sobre el 14vo y el `preservar`).
- **Hash final:** `c0cc10b3`. **Cinco commits de trabajo**, todos en `origin/pasada-unica`.
- **Rutas tocadas** (`git diff --stat ec6eefa4..HEAD`, corrido hoy): **59 ficheros, 4.855
  insertadas, 128 borradas**. Por carpeta: `docs/loop` **36**, `scripts/loop` **13**,
  `docs/plan` **4**, `web/lib` **2**, `dataset/nodos` **2**, `dataset/metadata` **2**.
  **Cero merges.** El hook corrio en los cinco commits (`[guardian] verde` en los cinco).
- **`dataset/nodos` son DOS ficheros y ninguno mas:** `principio_calidad_mvp.json` y
  `producto_minimo_viable.json`. **Ningun nodo nacio, ninguno murio y ninguna arista cambio.**

---

## 1. EL ESTADO, APERTURA CONTRA CIERRE

**Las dos columnas son de dos corridas distintas del MISMO instrumento**
(`scripts/loop/vuelta31_estado.py`, el sucesor declarado que cerro la vuelta 31): la de
**APERTURA** corrida **antes de la primera operacion** y commiteada antes de tocar nada
(`38a0a321`, salida `SALIDA_V32_APERTURA.txt`), y la de **CIERRE** corrida **al cerrar**
(`SALIDA_V32_CIERRE.txt`). **El instrumento NO cambio entre columnas esta vez**, asi que todas
las filas son comparables. Ninguna cifra viene del acta 31 ni de un reporte anterior.

| | **APERTURA** | **CIERRE** |
|---|---:|---:|
| marcador: n / A / B / C / D | 3.388 / 583 / 89 / 7 / 2.709 | **identico** |
| huecos / duplicados / clases fuera de ABCD | 0 / 0 / 0 | **0 / 0 / 0** |
| grafo: ficheros / ids / vivos / deprecados | 3.853 / 3.853 / 3.539 / 314 | **identico** |
| enlaces / claves distintas | 16.848 / 15 | **identico** |
| familias Weinberg / Horowitz / Hugos / Coleman / Rackham (vivos) | 72 / 93 / 111 / 75 / 47 | **identicas** |
| operaciones / estados / dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| inventario | 672 | **672** |
| indice rojo declarado | 18 lineas, 0 ausentes | **18 lineas, 0 ausentes** |
| fronteras de `OP-F-04-COL` | 14 de 15 | **14 de 15** |
| **nomina de `OP-F-04-HOR`** | **14** | **14** |
| **nota de `OP-F-04-HOR` (caracteres)** | 5.139 | **8.536** |

> **QUE EL MARCADOR NO SE MUEVA ES UN RESULTADO, NO UNA OMISION, y por eso va arriba.** Esta
> vuelta **releyo TRES congelados** (494, 592, 830) y **sostiene una clase nueva para los tres**,
> pero **NO los volco al archivo**, por la letra del propio `preservar` de `OP-D-01`. La seccion
> 4 lo explica con la regla citada. **La tasa por dominio y la vara por tramo son cifras del
> cribado y esta vuelta no leyo ningun par de la cola: no se mueven, y no se copian de ningun
> lado para rellenar la tabla.**

> **QUE EL GRAFO TAMPOCO SE MUEVA ES LA FIRMA DE LO QUE SE HIZO.** Las dos operaciones de esta
> vuelta son **colapsos DENTRO del nodo**: `principio_calidad_mvp` de 10 pasos a 7 y
> `producto_minimo_viable` de 22 a 6 y de 10 condiciones a 5. **Nada sale del nodo, asi que el
> censo, los enlaces y las familias quedan quietos.** Es la contraria exacta de la firma de la
> vuelta 31, donde el material SI salia y la familia Coleman se movio entera.

---

## 2. TAREA 1, LOS REGISTROS

1. **LA CAIDA DE CIFRA DE LA VUELTA 31, CORREGIDA CON EL TEXTO VIEJO TACHADO Y NO BORRADO**
   (`08_VERIFICACION.md`, tabla de las diecisiete costuras). La fila que nombraba a
   `investigar` **se queda entera arriba, tachada**, y debajo va la corregida con **UN solo
   destino**, `conexion_personal_emocional`. **Medido hoy, fichero por fichero:**
   `dataset/nodos/investigar.json` **NO EXISTE**; `conexion_personal_emocional` existe con **5
   pasos** y fuente unica Coleman; `investigar_datos_cliente` existe con **11 pasos** y la misma
   fuente. **Y el plan sellado lo dice sin ambiguedad** (`PLAN_V31_OPF04_COL.json`, leido hoy):
   el bloque de `ganar_comprension_del_cliente` se partio en **DOS cortes con DOS destinos**,
   *los pasos [7, 8, 9, 10] de 11* a `investigar_datos_cliente` y *los pasos [11] de 11* a
   `conexion_personal_emocional`. **La cuenta de la tanda no se mueve** (21 destinos, 17 con
   costura, 4 sin ella): lo que estaba mal era el NOMBRE de un destino, no su numero.

   > **LA LECCION, escrita donde se va a leer:** un nombre de destino tecleado a mano en una
   > tabla de prosa **no pasa por el resolutor**, y `investigar` es justamente la palabra que el
   > motivo `P.18` del corte hermano usa para el PRIMER paso del metodo IOPS de Coleman. **El
   > nombre correcto estaba a dos lineas de distancia, en la fila de arriba.**

2. **`OP-D-02` READJUDICADA en su `nota`** (`scripts/loop/vuelta32_registros.py`, correccion
   declarada al final, **texto viejo entero delante**), **con la medicion del dia al lado y no
   copiada del acta**: `voz_del_cliente_voc` tiene **5 pasos y fuente UNICA** Cooper, y el
   bloque 6 a 10 que su `preservar` manda hacer viajar entero vive en
   `observar_al_cliente_en_su_contexto`, con **5 pasos y fuente unica Coleman**. **El destejido
   no se repitio.** Lo que le queda escrito: la fusion, las relecturas de 724, 755 y 827, y
   tener delante a los otros dos. **Los campos `tipo` y `preservar` NO se tocan**, y se dice por
   que: lo que esta vuelta adjudica es el ALCANCE que queda por ejecutar, no la etiqueta.

3. **LAS CUATRO CORRECCIONES DEL COMMIT DEL FUNDADOR, CITADAS CON SU LINEA LEIDA HOY** y sin
   reescribirlas, que es lo que el encargo pide:

   | correccion | verificada hoy, y donde |
   |---|---|
   | la nomina de `OP-F-04-HOR` vuelve a **14** con `principio_calidad_mvp` reincorporado | medido en el fichero: **14 ids en el campo `nodos`**, con `principio_calidad_mvp` el ultimo de la lista; y la apertura lo levanta solo |
   | el `preservar` de `OP-D-01` reescrito (preserva el objeto RESTANTE por lectura; el par 494 se re-lee con la vara ordinaria sobre el nodo estable) | leido hoy entero en el campo `preservar`, con el texto viejo **tachado y no borrado** |
   | la `nota` de `OP-D-01` corregida de **Hugos** a **Horowitz** | leida hoy en el campo `nota`: *~~declara Hugos como segunda fuente~~ ... declara HOROWITZ* |
   | la pasada de **FORMA UNICA** para los acentos | `05_SANEO.md`, **linea 660**, leida hoy: *LA CURA ES UNA PASADA DE FORMA UNICA, DENTRO DE ESTA FASE (05_SANEO), AL FINAL DE LA PASADA* |
   | **`HECHA` no se estrena** | `00_INDICE.md`, **linea 102**, leida hoy: *REGISTRO: EL VALOR `HECHA` NO SE ESTRENA* ... *La tercera vez que se pregunta, la respuesta sigue siendo la misma: NO* |

---

## 3. TAREA 2.1, EL 14vo DE HOROWITZ: **`P.19`, NO `P.18`**

**La lectura se publico ENTERA antes de decidir nada** (`vuelta32_lectura_hor14.py`, salida
`SALIDA_V32_HOR14_LECTURA.txt`): el nodo con sus dos bloques y **los 93 miembros vivos de la
familia Horowitz con su titulo y su entregable**, que es lo que `P.18` punto 1 obliga a leer.

**LA DECISION, con el texto delante y no de antemano: el bloque 6 a 10 REPITE EL OBJETO de los
pasos 1 a 5.** Par por par: el **6** (resistir la presion del equipo de completar todas las
funcionalidades ideales antes de lanzar) es el **1** (antes de invertir en pulir, preguntate si
contribuye al aprendizaje) **con el sesgo nombrado**; el **7** (distinguir requerimientos
heredados de un cliente anterior de las necesidades del mercado amplio) es el **3** (no asumas
que el estandar de la industria es lo que el cliente valora) **con otra fuente del estandar
falso**; el **8** (lanzar al mercado real lo antes posible aceptando que fallara) es el **2**
(lanza versiones simplificadas y mide la reaccion real) **a escala de producto**. **Los que no
repiten se quedan VERBATIM: el 9 y el 10 de Horowitz, y el 4 y el 5 de Ries.**

**POR QUE NO `P.18`, con los descartados por su nombre** (`P.18` punto 2 lo exige):
`framework_good_bad_product_manager` (su objeto es el ROL del product manager y su entregable un
documento de expectativas del puesto), `lead_bullets_no_silver_bullets` y
`estrategia_de_balas_de_plomo` (cerrar una desventaja competitiva **sin atajos**, que es el
consejo contrario), `respuesta_estrategica_a_amenaza_competitiva` (el pivote ante un competidor
dominante), `descubrir_valor_inesperado_cliente` (el dolor no contractual de UN cliente critico)
y `toma_decisiones_bajo_incertidumbre` (decidir con informacion incompleta, que es el genero y
no este objeto). **Y la salida de nodo propio de `P.18` punto 3 habria fabricado aqui el gemelo
exacto del propio donante**, que es literalmente el caso que el motivo de `P.19` nombra para
existir.

**LAS DIFERENCIAS, por la tabla de los SEIS MOTIVOS:** `SALVAGUARDA` en el paso 1 del resultado,
`ALCANCE` en el 2, `ALCANCE` mas `SALVAGUARDA` en el 3. **`NOMBRE`, `DESTINO`, `METODO
ALTERNATIVO` y `DIRECCION` no aplican y por eso no se nombran.**

| guarda | resultado |
|---|---|
| simulacion previa sobre copia en memoria | **verde** (`SALIDA_V32_HOR14_SIM.txt`) |
| guarda de texto sobre TODOS los pasos | **10 de 10** calzan con su prefijo |
| cero perdida, cobertura exacta de 1 a 10 | **sin huecos ni repetidos** |
| **caso positivo ANTES** | **0 PASAN, 5 CAEN** (`SALIDA_V32_HOR14_CASO_ANTES.txt`) |
| **caso positivo DESPUES** | **5 PASAN, 0 CAEN** (`SALIDA_V32_HOR14_CASO_DESPUES.txt`) |
| conservacion (pasa las dos veces a proposito, contada aparte) | **10 rastros vivos, 0 muertos** |
| fuente | **sin cambio**: MULTIFUENTE LEGITIMO con procedencia por bloque |

**Ciclo de `Gate 0`, entero y en su orden:** comando 1 `run_phase1.py --reaplico-curaduria`
**exit 0, `GATE 0: OK`**, 3.853 nodos compilados; comando 2 `etiquetas_de_cara.py --aplicar`
**71 etiquetas**; **comando 4 `plan_readiness.py` NO aplica** y se dice por que, con la cifra:
**el censo no se movio, 3.853 ficheros antes y despues**; comando 3 `sync_assets_web.py`.
**Suites:** motor **24 de 24**, web **80 ficheros, 1.030 pasadas y 3 saltadas**, `tsc --noEmit`
**cero lineas**.

### 3.1 LA FASE 01 SE RE-CIERRA, **14 DE 14**, con las DOS corridas publicadas

| corrida | instrumento | resultado |
|---|---|---|
| **con el instrumento de la vuelta 31, sin tocar** | `vuelta30_saldo_opf04.py` (`SALIDA_V32_SALDO_HOR_VIEJO.txt`) | **NOMINA 14, RESUELTOS 12, FUNDIDOS 1, PENDIENTES 1** ... *LA TANDA SIGUE PARCIAL* |
| **con el sucesor declarado** | `vuelta32_saldo_opf04.py` (`SALIDA_V32_SALDO_HOR.txt`) | **NOMINA 14, RESUELTOS 12, FUNDIDOS por `P.19` 2, PENDIENTES 0** ... *LA TANDA ESTA ENTERA* |

> **LAS DOS SE PUBLICAN Y LA DIFERENCIA SE DECLARA, en vez de resolverse copiando:** el sucesor
> anade **UNA entrada** al censo de fundidos por `P.19` y nada mas. **Ese censo se escribe a
> mano a proposito, y ahora esta escrito por que:** un nodo que sigue declarando el libro de la
> tanda **o no se toco, o se fundio**, y las dos cosas se ven **igual** en el campo `fuente`. Un
> instrumento que dedujera *fundido* de la sola presencia del libro **convertiria cada bloque
> sin tocar en un falso verde.**

**La fila del cierre de la vuelta 31 que decia `13 de 13` no se borra**, y la correccion dice
por que era correcta: **lo que cambio no fue el trabajo, fue la NOMINA**, que volvio a catorce
por decision del fundador. Publicado en `01_FUENTES.md`, seccion *LA FASE 01 SE RE-CIERRA CON 14
DE 14*.

---

## 4. TAREA 2.2, `OP-D-01` EJECUTADA: los cuatro movimientos

### 4.1 MOVIMIENTO 1, el destejido del emblema. **HECHO**

**`producto_minimo_viable` pasa de 22 pasos a SEIS y de 10 condiciones a CINCO**, y **no sale un
solo bloque del nodo**: su costura es de **fuente UNICA** (Ries consigo mismo, cinco narraciones
en fila), asi que no hay material ajeno que destejer con destino, **solo repetido que
colapsar**.

**EL CRITERIO DEL SUPERVIVIENTE, ESCRITO ANTES DE APLICARLO para que se pueda auditar: de cada
grupo de repeticion sobrevive EL DE INDICE MAS BAJO.** No es una preferencia estetica: es el
unico criterio que **no obliga a elegir entre frases que la ficha ya declaro equivalentes**, y
deja el orden propio del nodo en pie. **El resultado cae exactamente sobre la NARRACION 1 (pasos
1 a 5), que es la que el propio `entregable_esperado` del nodo ya narraba**, mas el paso 8.

| paso | origenes | motivo de perdida aplicado |
|---:|---|---|
| **1** | 1, 10 | `SALVAGUARDA` (la prueba de que alguien PAGARIA por resolverlo) |
| **2** | 2, 6, 11, 15, 16, 19 | `SALVAGUARDA` (el sesgo de la lista larga de pedidos) |
| **3** | 3, 9, 13, 18 | `ALCANCE` (el segundo criterio de la excepcion: que sin ella no se pueda vender) |
| **4** | 4, 7, 12, 20 | `NOMBRE` (banco 9.28): *earlyvangelists* es la palabra por la que se busca |
| **5** | 5, 21 | `SALVAGUARDA` (no para expandir funciones) |
| **6** | 8, 14, 17, 22 | `ALCANCE` (la cadencia: ciclos cortos, incremental) |

Y las cinco condiciones supervivientes (**1, 3, 4, 6, 8**) por el mismo criterio, **todas
VERBATIM**: la ficha no declara ninguna linea perdida en ese campo, solo repeticion.

> **DISCREPANCIA DECLARADA CONTRA UNA CIFRA PUBLICADA, y no la resuelvo copiando.** La ficha
> proyectaba *de veintidos pasos a **CINCO*** y **la medicion de hoy, grupo por grupo, da
> SEIS**. El sexto tiene nombre: **iterar o cambiar de rumbo** (pasos 8, 14, 17 y 22) **es una
> cosa que la narracion 1 no contiene**. La proyeccion se queda escrita donde esta, y **seis
> sigue dentro del estandar de 3 a 6** que la propia ficha cita.

| guarda | resultado |
|---|---|
| simulacion previa | **verde** (`SALIDA_V32_OPD01_SIM.txt`) |
| guarda de texto sobre pasos **y** condiciones | **22 de 22** y **10 de 10** |
| cero perdida, cobertura exacta en los dos campos | **sin huecos ni repetidos** |
| **caso positivo ANTES** | **0 PASAN, 8 CAEN** |
| **caso positivo DESPUES** | **8 PASAN, 0 CAEN** |
| conservacion | **14 rastros vivos, 0 muertos**, las dos veces |

**`Gate 0` exit 0 con `GATE 0: OK`, etiquetas y sync verdes, motor 24 de 24, web 1.030 pasadas,
`tsc` cero lineas. El comando 4 tampoco aplica: 3.853 antes y despues.**

### 4.2 MOVIMIENTO 2, el destejido del pariente. **CONSUMIDO, y lo dice el instrumento**

**`principio_calidad_mvp` no tiene costura interna que destejer hoy.** Medido con
`vuelta32_costura_opd01.py`, que **importa** las dos senales y los dos umbrales de
`scripts/costuras_internas.py` en vez de copiarlos: **mejor pareja de pasos 51,2 contra un
umbral de 80; mejor alineacion de bloques 0,0 contra un umbral de 44. NINGUNA SENAL DISPARA.**
(El emblema ya destejido da **50,3 y 0,0**: los dos por debajo de las dos varas.)

**Sus tres narraciones tienen cada una su fecha y su operacion:** la **TERCERA** se la llevo
`OP-F-03`; la **SEGUNDA** se fundio con la **PRIMERA** hoy mismo por `P.19`. **Queda una sola
narracion y el destejido que esta operacion pedia ya esta consumido por esas dos operaciones.**

> **El nodo queda en SIETE pasos, uno por encima del estandar, y entra por la puerta que la
> propia verificacion de `OP-D-01` nombra:** *cada nodo resultante dentro del estandar, **o
> dentro de la excepcion de clase de `OP-F-01`***. La firma escrita de esa clase es **superar el
> estandar SIN narracion repetida dentro**, que es exactamente lo que el instrumento midio.

### 4.3 MOVIMIENTO 3, el par **494**: **NO SE FUNDE**

**La razon publicada apoyaba la A en una sola cosa** (*los pasos 11 al 14 del primero son el
nucleo del segundo dicho otra vez*) **y esos pasos ya no existen**. El informe habia escrito la
condicion por adelantado: *si el destejido conserva la narracion de la CALIDAD, el par deja de
repetir*. **La conserva.**

**LA VARA, aplicada en los DOS SENTIDOS y sobre LINEAS DISTINTAS:**

| sentido | la linea | quien trae el procedimiento entero |
|---|---|---|
| **1** | `principio_calidad_mvp` paso 3, en UNA linea: *lanza al mercado real versiones simplificadas y mide la reaccion real* | **`producto_minimo_viable`**, con sus seis pasos |
| **2** | `producto_minimo_viable` pasos 2 y 3, en UNA linea: *la version mas simple, sin funciones extra* | **`principio_calidad_mvp`**, con su procedimiento de calidad |

**Es el banco `9.22`, LA VARA EN LOS DOS SENTIDOS**, y por su letra el par es **`C`, sano CON
FIGURA**, con **ENLACE MUTUO** como arreglo. **Medido hoy en los dos sentidos: NO HAY NINGUNA
ARISTA.** Seria el **tercer ejemplar** del 9.22, tras el 1077 y el 1240, **y el primero que nace
con el enlace sin poner.**

### 4.4 MOVIMIENTO 4, **592** y **830** releidos

Los dos estaban en `B` por la misma causa (**banco 9.4**, el veredicto emitido contra un texto
que iba a cambiar) **y esa causa cayo**. Medido contra los SEIS pasos de hoy del emblema:

| puesto | lo que el otro trae y el emblema sigue sin decir | clase que sostengo |
|---:|---|---|
| **592** | la **ESCALERA DE COSTO** de `mvp_catalogo_tecnicas`: empezar por el MVP mas barato, subir solo si promete, herramientas a mano antes de produccion profesional | **`D`, sano, con ARISTA QUE FALTA** |
| **830** | el **AISLAMIENTO DE LA PRUEBA** de `prueba_mvp_alta_fidelidad`: numero limitado de invitados, CTA clara, visitas antes del primer uso, cuantos recomiendan, y evitar publicidad y prensa | **`D`, sano, con ARISTA QUE FALTA** |

> **LA CLASE SE SOSTIENE CON LA PRACTICA MEDIDA DEL ARCHIVO, no con mi gusto:** barrido hoy el
> fichero entero de veredictos, **los 207 cuya razon nombra ARISTA QUE FALTA son `D`, los 207**.
> Y **medido hoy en los dos sentidos, ninguno de los dos pares tiene arista.**

### 4.5 LO QUE ESTA VUELTA **NO** ESCRIBIO, y con que regla

> **LAS TRES CLASES NUEVAS NO SE VOLCARON en `INTRA_DOMINIO_VEREDICTOS.jsonl`**, y no es
> timidez: es la letra del `preservar` de la propia operacion, corregido por el fundador el 15
> ago y leido hoy: *si la relectura diera par nuevo, **entra por el recomputo (banco 9.10)**, no
> se decide aqui de antemano*. **Volcarlas moveria el marcador publicado** y **obligaria a
> barrer en el mismo acto todas las tablas derivadas que citan esos tres numeros**, que es lo
> que el 9.10 exige y lo que **ninguna operacion de la fase 02 tiene escrito**.

> **LAS TRES ARISTAS TAMPOCO SE PUSIERON:** el campo `aristas_nuevas` de `OP-D-01` esta
> **VACIO** y los enlaces son la **fase 04**, que va despues. **Quedan declaradas con su sentido
> y su motivo en `02_DESTEJIDOS.md`** para que la fase 04 las encuentre escritas.

---

## 5. TAREA 2.3, **PARADA EN `OP-D-02`**. Cero nodos tocados

**Su paso 1 no se repitio** (lo hizo `OP-F-04-COL`), y esa parte esta hecha y registrada. **La
FUSION no se ejecuta**, y son tres motivos medidos hoy con `vuelta32_acto_opd02.py`, de solo
lectura (`SALIDA_V32_OPD02_ACTO.txt`, `SALIDA_V32_PARADA_OPD02.txt`).

**MOTIVO 1, y lo exige la verificacion escrita de la propia operacion** (*el acto se leyo ENTERO
antes de fundirse: cero pares internos sin veredicto*). **Medido par por par: PARES POSIBLES 6,
CON VEREDICTO 3, SIN VEREDICTO 3.** Los tres que faltan, **por su nombre**, porque una ausencia
no se afirma en bloque:

| par interno **sin veredicto** |
|---|
| `enfoque_mercado_voc` contra `homework_frontend_loading` |
| `homework_frontend_loading` contra `voz_del_cliente_voc` |
| `voice_of_customer_homework` contra `voz_del_cliente_voc` |

**Y `P.5`, que la nota de la operacion cita, dice que la pregunta que el acto leido entero
contesta es SI EL ACTO ES UNA FAMILIA O DOS. Con 3 de 6 esa pregunta no tiene respuesta
medida.** Los tres que si la tienen son los **tres pares A** (386, 526, 788) y su cierre
transitivo cubre a **los cuatro** nodos de la nomina, ninguno fuera.

**MOTIVO 2, NO HAY SUPERVIVIENTE ni escrito ni deducible.** El campo `superviviente` esta en
**`null`**, leido hoy. Y no se puede fijar por el banco **9.3.1**, cuya prueba corregida es
*gano todos los pares **A** que lo tocan*: **medido hoy, DOS de los tres pares A (386 y 788) NO
NOMBRAN GANADOR en su razon**. **Ningun nodo del acto tiene una victoria citable**, asi que no
hay GANADOR POR DERECHO; y GANADOR POR ELEGIR **exige `P.8` sobre la nomina entera con el acto
completo delante**, que es justo lo que el motivo 1 dice que no hay.

**MOTIVO 3, LA NOMINA PUEDE ESTAR CORTA, y el aviso ya estaba escrito.** La razon del puesto
**788** cierra asi: *la voz del cliente ya lleva cuatro nodos vistos en el cribado (...). Hay
que contarla entera antes de tocarla*. **Censo por nombre corrido hoy (banco 9.5.1), y se dice
lo que es: una CITA, no una prueba de pertenencia.** De los 9 nodos vivos con alguna marca,
**CUATRO son falsos positivos del substring `voc`** (`advocacy_customer_journey`,
`centro_asesoria_advocacy_center`, `incentivos_no_monetarios_advocacy`,
`voces_externas_credibles`). De los **cinco** reales, **DOS estan FUERA de la nomina**:
`voice_of_customer_estrategico` y `voc_temprano_en_agile_stage_gate`, **los dos del mismo libro**
que los cuatro de la nomina, **y el primero es ademas el contrario del congelado 724**.

**LAS RELECTURAS DE 724, 755 Y 827 SE LEEN PERO NO SE CLASIFICAN, y el motivo es la misma regla
que las congelo.** El **TOQUE UNICO del banco 9.4** prohibe emitir un veredicto contra un texto
que va a cambiar. **La mitad de esa causa ya cayo** (`voz_del_cliente_voc` esta destejido y
estable) **pero la otra mitad sigue en pie**: si la fusion se ejecuta, el superviviente **puede
no ser `voz_del_cliente_voc`**. **Emitirlas hoy seria romper la misma regla por la que estan
congelados.** Quedan leidas y publicadas (`SALIDA_V32_OPD02_RELECTURA.txt`), **sin clase**.

> **EL MODO CONTINUO SE DETIENE AQUI, y por la letra del encargo:** su punto 4 empieza con *Con
> `OP-D-01` y `OP-D-02` **hechas***, y `OP-D-02` no lo esta. **No salto a `OP-D-03`**: el propio
> encabezado del encargo dice que una operacion cuyo texto no alcance para ejecutarse sin
> decidir **detiene al ejecutor y convoca al auditor**.

---

## 6. LOS INSTRUMENTOS NUEVOS, TODOS DECLARADOS CON SU MOTIVO DENTRO

| instrumento | que es | el motivo, con la medicion que lo levanto |
|---|---|---|
| `vuelta32_lectura_hor14.py` | lectura pura | imprime el nodo y los 93 miembros vivos de la familia **antes** de decidir; no decide nada |
| `vuelta32_plan_hor14.py` | **constructor** del plan | los prefijos y los textos NO se teclean, se leen del grafo, y las huellas que si son mias pasan por **cuatro guardas escritas para caer**. Es la cura de la correccion 3 de la vuelta 31 (diez huellas sin acentos) |
| `vuelta32_caso_positivo.py` | sucesor de `vuelta30_caso_positivo.py`, **dos ampliaciones declaradas** | **1)** la **prueba de CONVERGENCIA**: la de huella repetida exige que las dos versiones compartan un trozo **literal**, y aqui la repeticion es **de OBJETO, no de letra** (el unico trozo literal compartido es `Lanza`). **2)** el campo `condiciones_activacion`: la ficha del emblema mide *veintidos pasos y **diez condiciones***, y un caso positivo que solo mirara pasos daria TODO PASA con media costura en pie |
| `vuelta32_saldo_opf04.py` | sucesor de `vuelta30_saldo_opf04.py` | **una** entrada mas en el censo de fundidos por `P.19`, con **las dos corridas publicadas** y la diferencia declarada |
| `vuelta32_podar.py` | sucesor de `vuelta30_fundir.py` | anade `condiciones_activacion` **con las mismas guardas** que los pasos: conteo, prefijo, cobertura exacta y mapa |
| `vuelta32_costura_opd01.py` | solo lectura | **importa** las dos senales y los dos umbrales de `costuras_internas.py` en vez de copiarlos, y **sin barrer el catalogo ni reescribir sus salidas en `docs/`**, que esta vuelta no tiene encargo de recomputar |
| `vuelta32_acto_opd02.py` | solo lectura | mide la cobertura del acto, el cierre transitivo de las A y el censo por nombre. **No funde, no escribe, no decide** |
| `vuelta32_relectura_opd01.py` | solo lectura | imprime los dos nodos de cada congelado y **busca la arista en los dos sentidos**, porque afirmar que falta una sin haberla buscado seria citar una busqueda negativa |

---

## 7. CORRECCIONES DECLARADAS DE ESTA VUELTA

1. **La fila `investigar` de la tabla de costuras**, ordenada por el encargo y ejecutada con el
   texto viejo **tachado y no borrado**, mas la leccion escrita al lado (seccion 2.1).
2. **`OP-D-02` readjucada en su nota**, con el texto viejo entero delante (seccion 2.2).
3. **`OP-F-04-HOR`: el 14vo resuelto**, correccion declarada al ejecutar como `P.18` punto 2 y
   `P.19` exigen, con la lectura que la sostiene y los descartados por su nombre.
4. **La fase 01 re-cerrada en 14 de 14**, sin borrar la fila de `13 de 13` de la vuelta 31 y
   diciendo por que aquella era correcta: **cambio la nomina, no el trabajo**.
5. **La discrepancia de la ficha del emblema, declarada y no resuelta copiando:** proyectaba
   **cinco** pasos y la medicion de hoy da **seis**, con el sexto nombrado.
6. **El contraste entre los dos instrumentos de saldo, publicado entero** en vez de resolverse
   sustituyendo el viejo por el nuevo.
7. **DOS TROPIEZOS MIOS DE HERRAMIENTA, sin efecto en ninguna cifra pero declarados igual:**
   invoque la suite del motor como `python -m pytest engine` (no hay `pytest` en el entorno; el
   corredor es `engine/run_all_tests.py`) y la suite web con `--reporter=basic` (esa bandera no
   existe en la version instalada de vitest). **Las dos corridas publicadas son las de los
   comandos correctos**, y ninguna cifra salio de la invocacion fallida.

---

## 8. PENDIENTES DE DOCTRINA

1. **NUEVO, y es el que bloquea el orden de la fase 02:** un acto de la fase 02 puede necesitar
   **pares internos que la cola cerrada del cribado no trae**. `OP-D-02` tiene **3 de 6**, y
   ninguna pagina dice quien lee los tres que faltan ni con que autoridad, **sabiendo que
   leerlos moveria `n` de 3.388**, que es cifra publicada y trabajo de la fase I, cerrada.
2. **NUEVO:** las tres clases releidas (494 `C`, 592 `D`, 830 `D`) **necesitan un carril de
   recomputo que ninguna operacion de la fase 02 tiene escrito**. El `preservar` las manda al
   recomputo por el banco 9.10, pero **el recomputo es la fase II y esta cerrada**.
3. **NUEVO:** las tres aristas que las relecturas levantan (**enlace mutuo** del 494, **arista
   que falta** del 592 y del 830) **no tienen operacion de la fase 04 que las reclame por
   nombre**. Quedan escritas en `02_DESTEJIDOS.md` para que no se redescubran.
4. **SIGUE VIVO:** los nodos propios de esta pasada **escritos sin acentos**. Ya tiene cura
   escrita (`05_SANEO.md` linea 660, leida hoy: pasada de FORMA UNICA al final de la fase III)
   **pero no tiene numero de operacion**, y su nomina depende de cuantos nodos propios existan
   al cierre.
5. **CERRADO, y se dice para no repetirlo como pendiente:** el valor `HECHA` del campo `estado`
   **no se estrena**, adjudicado por tercera vez y registrado en `00_INDICE.md` linea 102, leida
   hoy. **Las 71 operaciones siguen en `LISTA`, medido al cierre.**

---

## 9. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| # | que | por que es discutible |
|---:|---|---|
| **d1** | **Resolver el 14vo por `P.19` (fundir) y no por `P.18` (nodo propio)** | la repeticion aqui es **de OBJETO, no de letra**: los dos libros dicen lo mismo con vocabulario distinto y el unico trozo literal compartido es `Lanza`. **Una lectura que exija repeticion textual llamaria a esto "dos tratamientos del mismo tema" y mandaria nodo propio** |
| **d2** | **El paso 7 de Horowitz leido como repeticion del 3 de Ries** | es **el mas flojo de los tres pares**. El 3 habla del ESTANDAR DE CALIDAD de la industria; el 7 habla de REQUERIMIENTOS heredados de un cliente. Los uni porque los dos son *una fuente falsa de lo que hace falta*, pero se pueden leer como dos cosas |
| **d3** | **Dejar los pasos 9 y 10 de Horowitz VERBATIM en vez de fundirlos con el 5 de Ries** | los tres hablan del feedback de los primeros clientes. Los deje separados porque el 5 decide una inversion y el 9 captura y el 10 itera. **La lectura contraria los funde y el nodo baja de 7 a 5 o 6 pasos, y de paso deja de estar por encima del estandar** |
| **d4** | **El criterio del INDICE MAS BAJO para el superviviente del emblema** | es deterministico y auditable, **pero no esta escrito en ninguna pagina**: lo escribi yo antes de aplicarlo. La lectura contraria elige el mas COMPLETO de cada grupo, y en las condiciones daria la 7 en vez de la 3 |
| **d5** | **SEIS pasos y no cinco** | contradice una cifra publicada de la ficha. Lo sostengo con el grupo nombrado (iterar o cambiar de rumbo no esta en la narracion 1), **pero es una discrepancia contra un papel del plan y va marcada como tal** |
| **d6** | **Adosar remedios (`SALVAGUARDA`, `ALCANCE`, `NOMBRE`) a cuatro de los seis supervivientes** | la ficha dice que este destejido *no exige releer y decidir: exige borrar*, y *sin escribir una sola frase nueva*. **Yo escribi incisos.** Lo sostengo con que la seccion 3 de `AUDITOR.md` exige *perdidas repartidas, tabla de seis motivos incluida*, por operacion. **Son dos textos que tiran en direcciones contrarias y elegi uno** |
| **d7** | **Las condiciones supervivientes 1, 3, 4, 6 y 8** | mismo criterio que d4, y **la 3 es menos completa que la 7** (*antes de validar* contra *con todas las funciones, antes de lanzar*). Las deje verbatim porque la ficha declara ese grupo pura repeticion |
| **d8** | **`principio_calidad_mvp` en 7 pasos acogido a la excepcion de clase de `OP-F-01`** | la verificacion de `OP-D-01` la nombra, **pero el nodo no esta en la nomina de `OP-F-01`**. Aplico el CRITERIO escrito de la clase, no la pertenencia. La lectura contraria exige bajarlo a 6 |
| **d9** | **El par 494 leido `C` (banco 9.22) y no `D`** | el informe habia escrito *seria **D***. Lo leo `C` porque la figura de los dos sentidos aparece cuando los dos nodos ya estan estables, que es despues de esa prediccion. **Solo hay DOS ejemplares de esta figura en todo el archivo**, y estoy proponiendo el tercero |
| **d10** | **592 y 830 leidos `D` con arista que falta** | lo sostengo con **207 de 207**, pero esa cifra dice como se ha clasificado, **no que sea correcto aqui**. La lectura contraria es que el solape de 830 (mostrar solo a los earlyvangelists) sigue siendo el mismo paso en los dos nodos |
| **d11** | **NO volcar las tres clases nuevas al archivo de veredictos** | lo sostengo con la letra del `preservar`, **pero deja la verificacion de `OP-D-01` a medias**: sus congelados no *salen de la lista*. La lectura contraria es que releer ES volcarlas y que el recomputo es un tramite del mismo acto |
| **d12** | **NO poner las tres aristas** | mismo caso. `aristas_nuevas` vacio y la fase 04 despues, **pero un enlace mutuo declarado y no puesto es una deuda que puede envejecer** |
| **d13** | **Declarar PARADA en `OP-D-02` en vez de leer los tres pares que faltan** | leerlos moveria `n`, que es cifra publicada del cribado cerrado. **La lectura contraria es que esos tres pares nunca estuvieron en la cola (su similitud no llego) y que leerlos DENTRO de un acto no es cribar, es completar un acto**, y entonces la parada sobra |
| **d14** | **No saltar a `OP-D-03` tras la parada** | el precedente del acta 27 punto 5 permite seguir con lo independiente, y `OP-D-03` no depende de `OP-D-02`. **No lo hice** porque el encargo condiciona su punto 4 a que las dos esten hechas y porque su encabezado dice que la parada detiene al ejecutor |
| **d15** | **Escribir una CLASE DE PRUEBA nueva (la convergencia) en medio de una operacion** | es la misma especie de movimiento que el d10 de la vuelta 31 (cambiar una guarda). **Aqui no cambie una guarda que cayo: anadi una donde la vieja no alcanzaba**, y la vieja se sigue corriendo y se sigue publicando. **Pero inventar una prueba propia mientras se ejecuta es de lo que mas hay que mirar** |

---

## 10. PREGUNTAS

1. **Los tres pares internos que le faltan a `OP-D-02`: quien los lee y con que autoridad?** Si
   se leen, **`n` deja de ser 3.388** y hay que barrer todas las tablas que lo citan. Si no se
   leen, **la verificacion escrita de la operacion no se puede cumplir nunca**. De la respuesta
   depende toda la fase 02, porque **este no va a ser el unico acto incompleto**.
2. **Se amplia la nomina de `OP-D-02`?** El censo por nombre levanta dos nodos del mismo libro
   fuera de ella (`voice_of_customer_estrategico`, `voc_temprano_en_agile_stage_gate`) y la
   razon del 788 pedia contar la familia entera antes de tocarla.
3. **El volcado de las tres clases releidas y sus tres aristas abre un recomputo DENTRO de la
   fase III, o espera al cierre de la campana?** Las tres lecturas estan hechas y publicadas;
   lo que falta es el carril por donde entran.

---

## 11. LA RACHA DE DICTADO, dicha por mi

**El acta 31 conto UNA caida de cifra publicada fuera del marcado** (el nombre `investigar`) y
**la correccion esta hecha en esta vuelta, con el texto viejo tachado y la leccion escrita**.
Esta vuelta **midio la apertura antes de la primera operacion y la commiteo antes de tocar
nada** (`38a0a321`); **midio el cierre al cerrar con el mismo instrumento**; **cada cita del
registro lleva su linea leida hoy** (`05_SANEO.md` 660, `00_INDICE.md` 102); y **las siete
correcciones de la seccion 7 son mias y estan declaradas con nombre**, incluidos los dos
tropiezos de herramienta que no cambiaron ninguna cifra. **Las cifras de esta vuelta salen de
instrumentos corridos hoy, y donde dos instrumentos discreparon publique los dos.** **No me
corresponde decir si la racha sigue cortada: eso lo mide el auditor.**
