# REPORTE DE LA VUELTA 55 (20 ago 2026, ejecutor Opus 5)

**LA TAREA 1 ENTERA Y LA TAREA 2 ENTERA. EL TRAMO 2 QUEDA CERRADO: 45 ACTOS FUNDIDOS DE 50 Y CINCO
DECLARADOS. LA RELECTURA CONJUNTA CONFIRMA LA VARA EN LOS DOS ACTOS: el 18 se funde y el 23 se
DESHACE Y SE REHACE al reves con correccion declarada. EL HALLAZGO DE LA VUELTA SALE, otra vez, DE
CORRER LA GUARDA QUE EL ENCARGO MANDA: `vuelta54_tramo2_nomina.py` CAE EN ROJO CON PARADA sobre la
nomina del dia, y el rojo NO dice lo que dice. Y EL SEGUNDO HALLAZGO ES DE LAS CINCO RELECTURAS DEL
FILO: CUATRO de las cinco destapan PREGUNTA DE POLITICA DE CATALOGO, asi que los actos 6 y 49 NO se
funden, y el carril del filo lo manda con esas palabras.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `4e48e8e6` (el acta de la vuelta 54), **arbol limpio y todo pusheado** |
| **hash final** | el de este commit del cierre mas el commit que escribe esta cabecera, **pusheados a `origin/pasada-unica`** |
| **commits de la vuelta** | **5**: `795c2fdd` (apertura y sucesor del instrumento del tramo), el de la TAREA 1.1, el del lote A, el del lote B y el del cierre, mas el de esta cabecera |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1)

**Corrida ANTES de tocar nada. TODAS las filas son corridas propias de esta vuelta y NINGUNA se
hereda del cierre anterior.** El arbol estaba limpio y todo pusheado en `4e48e8e6`, **asi que la
regla 3 se cumplio por vacio, y se dice asi en vez de darla por cumplida.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 73 / 6 / 2.758 | **551 / 72 / 6 / 2.759** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.456 / 397 / 17.118 | **3.853 / 3.432 / 421 / 17.168** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 93 / 458 | **551 / 117 / 434** |
| actos (componentes) | 264 | **240** |
| actos `CERRADOS` / `ABIERTOS` | 211 / 53 | **187 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 431 / 240 | **383 / 240** |
| cola de costuras | 1.489 | **1.482** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 72 | **96** |
| duplicadas historicas: grupos / nodos | 988 / 779 | **983 / 774** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK | **TODAS OK** (623 igual a 623; 434 igual a 434) |
| actos del tramo 2 fundidos / pendientes | 21 / 29 | **45 / 5, los cinco DECLARADOS** |

**Instrumentos de la apertura, todos corridos antes de la primera operacion:**
[`SALIDA_V55_APERTURA.txt`](SALIDA_V55_APERTURA.txt),
[`SALIDA_V55_MARCADOR_APERTURA.txt`](SALIDA_V55_MARCADOR_APERTURA.txt),
[`SALIDA_V55_RECOMPUTO_APERTURA.txt`](SALIDA_V55_RECOMPUTO_APERTURA.txt),
[`SALIDA_V55_COLA_APERTURA.txt`](SALIDA_V55_COLA_APERTURA.txt),
[`SALIDA_V55_COLISIONES_APERTURA.txt`](SALIDA_V55_COLISIONES_APERTURA.txt) y
[`SALIDA_V55_DUPLICADAS_APERTURA.txt`](SALIDA_V55_DUPLICADAS_APERTURA.txt). **El cierre esta en los
ficheros `_CIERRE` hermanos, corridos DESPUES del ultimo movimiento.** **Ninguna celda de la tabla
del registro esta tecleada:** `scripts/loop/vuelta55_registro_tramo.py` las EXTRAE de esas mismas
salidas por expresion regular y cae en rojo si alguna no se puede leer.

**EL MARCADOR SI SE MUEVE ESTA VUELTA, y es la diferencia con la 54:** la relectura del filo del
acto 44 corrigio el puesto **218** de `B` a `D`. **`B` baja de 73 a 72 y `D` sube de 2.758 a
2.759.** **`A` y `C` NO se mueven**, y por eso **las DOS tablas por dominio hermanas tampoco**:
publican la `A` de cada dominio, y la `A` de los diez es identica al digito en las dos corridas del
marcador. **La hermandad se cumple POR VACIO y se dice, en vez de darse por cumplida.**

**EL RETRATO SE MUEVE VEINTICUATRO, NO VEINTICINCO, y la cuenta se deja escrita porque el numero
sorprende:** esta vuelta ejecuto **25** fusiones, pero **el acto 23 es una fusion REHECHA** sobre un
acto que ya estaba colapsado en la apertura, y su deshacer resto uno antes de sumar los veinticinco.
**93 menos 1 mas 25 son 117**, y **458 menos 24 son 434**, que es la resta exacta (551 crudas menos
117 colapsos).

---

## 1. TAREA 1.1: LA RELECTURA CONJUNTA, CONFIRMADA EN LOS DOS ACTOS

**Lei los dos actos enteros contra el grafo (`P.5`), con las razones enteras al lado**
([`SALIDA_V55_DOSSIER_TRAMO2.txt`](SALIDA_V55_DOSSIER_TRAMO2.txt), instrumento nuevo
`scripts/loop/vuelta55_dossier_tramo2.py`), **y el 23 en su estado PRE FUSION leido del blob de
git**. **LA VARA ES LA DEL ACTA 54, PREGUNTA 4** (el material propio que `P.8` pesa es SOLO el
declarado en las razones) **mas la del acta 53, pregunta 4** (una vara de contenido no empatada
BASTA).

| acto | lo que la razon DECLARA, verbatim | donde esta ese gesto | mi decision |
|---:|---|---|---|
| **18** (puesto 322) | *El primero anade revisar como se incentiva a quien vende, **QUE ES SU UNICO GESTO PROPIO*** | el **primero** es `desconexion_ventas_experiencia`, y el gesto es **su paso 2**, verificado en el fichero | **VARA CONFIRMADA.** Se funde con `desconexion_ventas_experiencia` de superviviente |
| **23** (puesto 340) | *El segundo anade no contratar estructuras completas, VP de ventas y equipos, antes de validar, **QUE ES EL UNICO GESTO PROPIO*** | el **segundo** es `modelo_tradicional_introduccion_producto`, y el gesto es **su paso 4** | **VARA CONFIRMADA.** Correccion declarada y fusion rehecha hacia `modelo_tradicional_introduccion_producto` |

**LO QUE LA LECTURA ANADE AL CASO DEL AUDITOR, y no estaba en su acta:** en el **18** la razon
**enumera los cuatro gestos que declara compartidos y los cuatro son los cuatro pasos de
`traspaso_ventas_cuentas`**, asi que del otro lado **no queda propio declarado**; las tres varas
contables empatan al digito (4/4, 3/3, 2/2) y por eso la 54 lo llamo empate sin vara. En el **23**
el motivo sellado decia *la razon le reconoce a cada uno lo suyo*, **y la razon no dice eso**:
reconoce **UN** gesto y lo llama **UNICO**.

### EL 23, DESHECHO CON EL ALCANCE MEDIDO POR GIT Y NO SUPUESTO

`scripts/loop/vuelta55_deshacer_acto23.py`
([`SALIDA_V55_DESHACER_ACTO23.txt`](SALIDA_V55_DESHACER_ACTO23.txt)). **De los 50 ficheros de nodo
que toco el lote B de la vuelta 54, los del acto 23 son CUATRO**, y el instrumento **los mide** en
vez de creerselos: el superviviente, el absorbido y los dos nodos vivos cuya arista la fusion
redirigio. **Comprobado antes de escribir: ninguno se toco despues del lote B y los cuatro estan
limpios en el arbol.** **Restaurados al blob de `0feef54e`, que es el commit del lote A**, y por eso
conserva el acto 8 entero (`stage_gate_system` es su superviviente): **el commit de referencia no se
elige, se mide.**

**SU PROPIA GUARDA MORDIO EN EL PRIMER INTENTO, y queda declarada en el codigo:** la primera version
atribuia un fichero al acto 23 si su diff **mencionaba** alguno de los dos ids, y **el fichero del
ABSORBIDO no se nombra a si mismo en su diff** (su unico cambio es `"deprecado": true`). Salio
**ROJO con 3 de 4** y no escribio nada. **La vara de atribucion se amplio a su segunda mitad** (un
fichero es del acto si su diff menciona los ids **o si el fichero ES el de uno de los dos
miembros**) y quedo escrita en el comentario.

### EL REPARTO DEL 23 ES EL ESPEJO EXACTO DEL SELLADO EN LA OTRA DIRECCION

**Y por eso las cuentas calzan:** alli el superviviente pasaba de **4 a 6** pasos y de **2 a 3**
condiciones, **y aqui tambien**. **Ademas salva DOS INCISOS que aquella direccion perdio sin
nombrarlos** (la herencia de la empresa grande, y el mercado y el cliente como hipotesis). **El
motivo viejo entero va pegado dentro del motivo nuevo, sin tapar nada.** **Va marcado (`D3`)**,
porque anadir incisos que la direccion original no tenia es asimetria mia.

---

## 2. TAREA 1.2 Y 1.3: LOS DOS REGISTROS DE LAS ADJUDICACIONES

**Instrumento: `scripts/loop/vuelta55_correcciones_tarea1.py`, idempotente al re-correrlo**
([`SALIDA_V55_CORRECCIONES_T1_IDEMPOTENCIA.txt`](SALIDA_V55_CORRECCIONES_T1_IDEMPOTENCIA.txt), los
dos sitios en `YA ESTABA`). **Cada sitio se localiza por un ANCLA literal y cae en rojo si el ancla
falta o aparece mas de una vez: un ancla ambigua no es un ancla.**

| | lo que se escribio | donde |
|---|---|---|
| **1.2.a** | **LA NOTA DE LA ADJUDICACION DE LAS PUERTAS**, *LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO*, con **sus cuatro piezas en tabla y cada una con su sede** (la receta ratificada, la vara del acta 51 pregunta 3, la precision de la estrella del `9.3.1` y el acta 50 adjudicacion 3) | `03_FUSIONES.md`, **detras de la cabecera del registro del tramo 2**, para que se lea al abrir la seccion |
| **1.2.b** | **LA RESPUESTA ADOSADA AL ROTULO DEL INSTRUMENTO DE LAS PUERTAS**, con el **texto viejo delante entero** | `scripts/loop/vuelta48_puertas_en_el_lote.py`. **LA LOGICA NO SE TOCA: el diff por git da 19 lineas anadidas y CERO borradas**, todas `print` y comentario |
| **1.3** | **LA NOTA DEL CHOQUE SIN PIEZA**: el `entregable_esperado` **no es razon**, y los actos **4**, **20** y **42** quedan **DECLARADOS Y ACUMULAN PARA LA MESA**, con el choque de cada uno medido y el pendiente de doctrina nombrado en sus dos ramas | `03_FUSIONES.md`, junto a la anterior |

**NINGUNO DE LOS TRES ACTOS SE TOCO**, y los tres siguen vivos al cerrar, comprobado en la nomina
del cierre.

---

## 3. EL HALLAZGO: EL INSTRUMENTO DEL TRAMO CAE EN ROJO AL CONTINUAR, Y EL ROJO NO DICE LO QUE DICE

**Corrido `scripts/loop/vuelta54_tramo2_nomina.py` sobre la nomina del dia, como el encargo 2.1
manda, CAE EN ROJO CON PARADA**
([`SALIDA_V55_TRAMO2_NOMINA.txt`](SALIDA_V55_TRAMO2_NOMINA.txt)): *solo en A: 21, solo en B: 0*.
**Fui a mirar antes de tocar nada.**

**EL MOTIVO ES ESTRUCTURAL Y NO DEL TRAMO:** aquel instrumento **nacio para ABRIR un tramo** y
compara los 50 `CERRADOS` siguientes de HOY (lectura A) contra los puestos 51 a 100 de la nomina de
la vuelta 48 (lectura B). **En cuanto se funde un acto del tramo, ese acto deja de ser componente
`CERRADA` y sale de la nomina, la lectura B encoge, y la lectura A rellena hasta 50 con actos del
tramo SIGUIENTE.** **El rojo dice *el tramo ya se toco*, no *el tramo no esta determinado*.**

**SUCESOR DECLARADO, POR LA VARA DEL ACTA 54, PREGUNTA 3** (un instrumento de guarda cuyas cifras ya
citan registros no cambia de logica: se le escribe sucesor declarado con la aritmetica copiada; y la
tabla de las dos lecturas de este instrumento **la publica el registro del tramo 2 en
`03_FUSIONES.md`**): **`scripts/loop/vuelta55_tramo2_nomina.py`**, con la aritmetica copiada, la
identidad del tramo **POR MIEMBROS** de los puestos 51 a 100 de la 48, **el ordinal derivado del
fichero y no tecleado**, y el calzar de la continuacion en **dos formas**
([`SALIDA_V55_TRAMO2_NOMINA_SUCESOR.txt`](SALIDA_V55_TRAMO2_NOMINA_SUCESOR.txt)):

| lo que el sucesor comprueba | al abrir la vuelta 55 | **al cerrarla** |
|---|---|---|
| los 50 del tramo, entre VIVOS y FUNDIDOS | **29 vivos y 21 fundidos**, suma 50 de 50 | **5 vivos y 45 fundidos**, suma 50 de 50 |
| los FUNDIDOS, uno a uno contra el grafo (resuelven a UNO y alias izado) | **21 de 21** | **45 de 45** |
| lectura A (orden de hoy) contra lectura B (orden de la 48), sobre los vivos | **CALZAN** | **CALZAN** |
| los supervivientes son **PREFIJO** de la lectura A de hoy | **SI** | **SI** |
| guarda de los cuatro ajenos / guarda de solape con el tramo 1 | **VERDE** / **VERDE** | **VERDE** / **VERDE** |

> **Y LOS ORDINALES QUE IMPRIME REPRODUCEN AL DIGITO LOS QUE LA VUELTA 54 PUBLICO**, porque el
> ordinal se deriva del puesto de la vuelta 48 menos 50 y no de un contador nuevo. **La primera
> version de mi propio resolutor tambien cayo en rojo y se declara**: invente un campo de reenvio en
> el nodo deprecado que no existe. **El resolutor correcto es el de `P.1`, con la aritmetica copiada
> de `vuelta51_censo_colisiones.py` lineas 42 a 53: es el nodo VIVO el que iza los ids del muerto en
> `ids_alias`.** Marcado (`D2`).

---

## 4. LAS CINCO RELECTURAS DEL FILO: **UNA SE RESUELVE Y CUATRO DESTAPAN POLITICA**

**Las cinco estaban predichas y nombradas con sus puestos ANTES de tocar un nodo**
([`SALIDA_V55_COLISIONES_ESPERADAS_TRAMO2.txt`](SALIDA_V55_COLISIONES_ESPERADAS_TRAMO2.txt)), y son
**exactamente las cinco que el encargo nombra**: `668`/`1312`, `968`/`1305`, `218`/`1008`,
`338`/`490`, `297`/`497`. Las cinco se releyeron por **el carril general de colisiones con sus dos
ampliaciones**.

| acto | los dos puestos | que decide la relectura | consecuencia |
|---:|---|---|---|
| **44** | **218** `B` contra **1008** `D` | **CONDICION DE TEXTO, y se resuelve.** La condicion de CONTEO Y COBERTURA se descargo **MIDIENDO ANTES**: la madre despacha el momento en **UNA LINEA** (paso 1) y el hijo trae un **PROCEDIMIENTO de cuatro decisiones**, **tres ausentes de la madre**. La vara del banco `9.6.1` devuelve **CONTINUA** | **el 218 pasa de `B` a `D`** con correccion declarada, y **el acto SE FUNDE** |
| **6** | **668** `B` contra **1312** `D` | **POLITICA.** La razon del 668 escribe que *esa diferencia de alcance la tiene que resolver la **mesa del racimo del pivote**, no yo*, y la del 1312 anade una **NOTA DE COHERENCIA** que manda la discrepancia a esa misma mesa | **el acto NO se funde** |
| **6** | **968** `B` contra **1305** `D` | **POLITICA.** La razon del 968 dice que *si el criterio adoptado fuera un nodo por PUERTA, este par sobrevive entero*, y que es **el unico de los cuatro cruzados donde los dos criterios de la mesa dan respuestas distintas** | **el acto NO se funde** |
| **49** | **338** `B` contra **490** `D` | **POLITICA.** La razon del 338 escribe que juzgarlos de dos en dos *da respuestas incoherentes* y que **esto pide mesa de los tres a la vez, como los racimos** | **el acto NO se funde** |
| **49** | **297** `B` contra **497** `D` | **POLITICA.** La razon del 297 dice ***no lo decido*** y deja las dos lecturas abiertas | **el acto NO se funde** |

**EL CARRIL SE CUMPLE EN SU LETRA:** el acta de la vuelta 51, pregunta 2, dice que si la relectura
encuentra que lo congelado es **una pregunta de POLITICA de catalogo, el acto NO se funde**.
**Cuatro de las cinco lo son.** **Y el propio par `A` del acto 49 (puesto 536) ya lo escribia**:
*este par vive entero dentro del racimo nuevo de la puerta del ajuste, y por la regla operativa
registrada en la seccion 9 NO SE PELEA LA CLASE AQUI*.

**LA AMPLIACION DE MOVER LOS DOS NO HIZO FALTA, Y SE COMPROBO EN VEZ DE SUPONERSE:** en el 44, mover
UN solo veredicto cierra la colision porque el 1008 ya era `D`. **El censo esperado se RE-CORRIO
DESPUES de la correccion y baja de UNA colision a CERO para ese acto**
([`SALIDA_V55_COLISIONES_ESPERADAS_TRAS_FILO.txt`](SALIDA_V55_COLISIONES_ESPERADAS_TRAS_FILO.txt)).

---

## 5. LOS TRES LOTES: **VEINTICINCO FUSIONES EN EL ORDEN IMPRESO DEL TRAMO**

**El lote se forma EN EL ORDEN del tramo y solo se aparta el acto con bloqueo declarado**, que es la
regla de trabajo nueva del acta 54, punto 6. **LAS TRES TABLAS DE ESTA SECCION NO ESTAN TECLEADAS:
salen enteras de `python scripts/loop/vuelta55_tallar_planes.py`**
([`SALIDA_V55_TALLAR_PLANES.txt`](SALIDA_V55_TALLAR_PLANES.txt)), **que las cuenta de los
`PLAN_V55_*.json` SELLADOS**. Es el remedio mecanico de la caida de reporte que el acta 54 nombra.

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **T1** | 18, 23 | **2** | **2** | **13** | 5 | 4 | **4** | **1** |
| **A** | 1, 15, 28, 29, 30, 31, 32, 33, 34, 35, 36 | **11** | **11** | **75** | 28 | 32 | **15** | **2** |
| **B** | 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 50 | **12** | **12** | **68** | 20 | 39 | **9** | **1** |
| **los tres** | | **25** | **25** | **156** | **53** | **75** | **28** | **4** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **11** | 18, 29, 30, 31, 34, 36, 37, 39, 46, 47, 48 |
| **TODAS LAS VARAS de contenido de acuerdo** | **7** | 32, 35, 38, 41, 43, 44, 50 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **3** | 28, 33, 40 |
| **LA PUERTA SOBREVIVE, con el choque de conteos registrado** | **2** | 1, 15 |
| **CORRECCION DECLARADA, la fusion rehecha al reves** | **1** | 23 |
| **LA PIEZA DECLARADA decide, y la puerta apunta al mismo lado** | **1** | 45 |
| **suma** | **25** | |

**Guardas, por acto y en los veinticinco:** miembros vivos y nomina completa, **guarda 1B por vacio
en los veinticinco** (ningun absorbido es puerta), cobertura exacta de indices sin olvidos, cero
repetidos literales, **cero auto-aristas y cero duplicadas NUEVAS en los tres lotes**, y los cinco
campos que la operacion no redacta **intactos: 10 de 10 en el T1, 55 de 55 en el A y 60 de 60 en el
B**. **Guarda D en verde:** los 25 absorbidos conservan su texto INTACTO.

### LOS DOS DEL CHOQUE DE LA PUERTA, EJECUTADOS Y CON EL CHOQUE REGISTRADO

| acto | sobrevive | los conteos, impresos en el motivo |
|---:|---|---|
| **1** | `trade_off_responsividad_eficiencia` (**la puerta**) | contenido al OTRO: **pasos 6 contra 4** y **condiciones 3 contra 2**; cableado a la puerta, 2 contra 6 |
| **15** | `apertura_llamada_venta_grande` (**la puerta**) | contenido al OTRO: **pasos 5 contra 4**; condiciones **2 contra 2** y cableado **4 contra 4**, empatados |

**LO QUE PROTEGE EL CONTENIDO QUE EL CONTEO PREFIRIO ES EL REPARTO**, y se mide: en el **1** viajan
enteros **cuatro pasos y dos condiciones**, y en el **15** **tres pasos y una condicion**.

**Y SE DICE LA FIGURA CONTRARIA, que tambien cayo en este tramo:** el **acto 33** tiene puerta
(`leap_of_faith_assumptions`) **y el cableado la elige por su cuenta** (9 contra 3), asi que **la
guarda `1B` se cumple SIN choque**. Tenerlo escrito es lo que hace comparable el caso de los actos 1
y 15.

### EL ACTO 45: LA PIEZA DECLARADA GANA AL CABLEADO, Y LA PUERTA APUNTA IGUAL

**Los conteos de contenido EMPATAN al digito** (pasos 5/5, condiciones 2/2) **y el cableado apunta a
`milk_run_deliveries`** (4 contra 2). **Pero el cableado solo habla cuando el contenido calla
ENTERO, y aqui no calla:** la razon del **474** declara **CONTENCION** con todas sus letras
(*`milk_run_deliveries` es el paso 3 de `programacion_entregas_delivery_scheduling` DESARROLLADO*, y
*REPITE ademas dos pasos mas de la madre*). **La pieza declarada pesa mas que el cableado y apunta a
la MADRE, que ademas es PUERTA. Las dos varas coinciden**, tal como el encargo avisaba.

---

## 6. EL CASO POSITIVO: FABRICADO SOBRE UN ACTO QUE ESTA VUELTA **NO** TOCA

**`scripts/loop/vuelta55_caso_positivo.py`, corrido ANTES de ejecutar nada y RE-CORRIDO al cierre**
([`SALIDA_V55_CASO_POSITIVO.txt`](SALIDA_V55_CASO_POSITIVO.txt) y
[`SALIDA_V55_CASO_POSITIVO_CIERRE.txt`](SALIDA_V55_CASO_POSITIVO_CIERRE.txt)). **Sus dos mentiras de
plan se fabrican sobre EL ACTO 4** (`hr_calidad_gestion` y `hr_como_control_de_calidad_gerencial`),
que es **uno de los tres DECLARADOS** y que el encargo manda **no tocar**: **es la regla de trabajo
del acta 54, pregunta 7, y con ella el caso positivo DEJA DE CADUCAR.** **El de la vuelta 54 se
re-corrio primero y tambien sale verde**, como contraste
([`SALIDA_V55_CASO_POSITIVO_V54.txt`](SALIDA_V55_CASO_POSITIVO_V54.txt)).

| guarda | la mentira | resultado |
|---|---|---|
| **`1B`** | un plan cuyo absorbido es `domina_lo_que_compras`, que es puerta | **exit 1, `ROJO`, aborta sin escribir** |
| **cobertura** | un plan que se olvida del paso 3 del absorbido | **exit 1, `faltan ['3']`, aborta sin escribir** |
| **INCISO VERBATIM** | un inciso que es PARAFRASIS y no trozo literal | **exit 1, `NO es trozo verbatim`, aborta sin escribir** |
| **colisiones** | el censo contra una cuenta esperada FALSA de 9 | **`MEDIDA: 0 \| CALZA: NO`** |

**LAS CUATRO MUERDEN**, las dos veces. **Y SE DECLARA UN MATIZ DE LA SEGUNDA (`D6`):** la mentira de
la cobertura imprime **dos** lineas rojas, la de la guarda 2 y una *marca desconocida*, porque
quitar la marca del paso 3 produce las dos a la vez. **Es una sola causa con dos sintomas, no dos
motivos**, pero se dice.

---

## 7. EL BARRIDO `9.10` DEL CIERRE, CORRIDO DESPUES DEL ULTIMO MOVIMIENTO

**Con las cifras viejas DE HOY** (`--viejo 551,73,6,2758 --retrato 93,458`,
[`SALIDA_V55_BARRIDO_910_CIERRE.txt`](SALIDA_V55_BARRIDO_910_CIERRE.txt)). **OCHO celdas
corregidas** ([`SALIDA_V55_CORRECCIONES_910.txt`](SALIDA_V55_CORRECCIONES_910.txt), **idempotente**:
al re-correrlo las ocho salen `YA ESTABA`):

| la celda | decia | **medido al cierre** |
|---|---:|---:|
| `RECOMPUTO_3388.md` **247**, colapsos **y su contador** | 93, contador OCHO | **117, contador NUEVE** |
| **248**, pares distintos **y su contador** | 458, contador ONCE | **434, contador DOCE** |
| **528**, el checkpoint `ii` en sus dos parentesis **y su nota** | 458 igual a 458 | **434 igual a 434, sigue OK** |
| `INTRA_DOMINIO_INFORME.md`, la fila **`B`** del marcador publicado | 73 | **72** |
| la fila **`D`** del marcador publicado **y su nota fechada** | 2.758 | **2.759** |

**LA FILA 246 (`A` crudas) NO SE TOCA Y NO ES UN OLVIDO:** el unico veredicto que esta vuelta movio
paso de `B` a `D`, y ese volteo **no toca la `A`**. **Y LAS DOS TABLAS POR DOMINIO HERMANAS TAMPOCO,
por lo mismo**: publican la `A` de cada dominio y la `A` de los diez es identica al digito. **La
hermandad se cumple POR VACIO y se dice.**

---

## 8. GATE 0 Y LAS SUITES

**Corridos tras cada uno de los tres lotes, tras el deshacer del acto 23 y otra vez al cierre. Todos
exit 0.**

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`** las cinco veces; `etiquetas_de_cara --aplicar` con **71** etiquetas; `sync_assets_web` |
| **suite del motor** | **25 de 25**, las cuatro veces |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas, las cuatro veces |
| `tsc --noEmit` | **CERO** lineas |
| duplicadas / auto-aristas **NUEVAS** | **CERO** y **CERO** en los tres lotes |
| censo de colisiones tras cada lote | **CERO**, con `--esperadas 0` y **`CALZA: SI`** las tres veces |
| las cuatro comprobaciones de `08_VERIFICACION` | **TODAS OK** al cierre (623 igual a 623; 434 igual a 434) |
| **hook guardian** | verde en todos los commits |

---

## 9. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

1. **MI PRIMER RESOLUTOR EN EL SUCESOR DEL INSTRUMENTO DEL TRAMO ERA INVENTADO.** Escribi una cadena
   de reenvio leyendo campos (`reemplazado_por`, `fusionado_en`, `alias_de`) **que el nodo deprecado
   no tiene**. **Salio ROJO en los 21 fundidos** y no se publico. **El resolutor correcto es el de
   `P.1`**, con la aritmetica copiada de `vuelta51_censo_colisiones.py`: es el nodo **VIVO** el que
   iza los ids del muerto en `ids_alias`. Marcado (`D2`).
2. **LA GUARDA DE ALCANCE DE MI INSTRUMENTO DE DESHACER MORDIO A SU PROPIO AUTOR.** Ver la seccion
   1: atribuia por mencion en el diff y dejaba fuera al absorbido. **Salio ROJO con 3 de 4 y no
   escribio nada.** La vara ampliada esta escrita en el codigo con su motivo.
3. **UNA CORRECCION DE ACENTOS EN DOS NEXOS MIOS** (*calificacion* y *cuanto*), cazada releyendo los
   incisos antes de sellar. **Los incisos mismos ya no pueden fallar por acentos** porque el
   generador los EXTRAE del nodo (seccion 10).
4. **Ficheros tocados que el encargo no nombraba, declarados:** `docs/COSTURAS_INTERNAS.jsonl` y
   `docs/COSTURAS_INTERNAS_RESUMEN.md`, `docs/plan/ARISTAS_DUPLICADAS.jsonl`, `dataset/metadata/*` y
   `web/lib/assets/*` (los reescriben los instrumentos y el ciclo de Gate 0). **Mismo alcance que
   las vueltas 48 a 54.** Y **`scripts/loop/vuelta48_puertas_en_el_lote.py`**, que el encargo SI
   nombra (TAREA 1.2) y cuyo diff es **19 lineas anadidas y cero borradas**.

---

## 10. LO QUE ESTA VUELTA MEJORA EN EL INSTRUMENTAL, con su motivo medido

| instrumento | que cambia | de que caida nace |
|---|---|---|
| **`vuelta55_planes.py`** | **el INCISO se declara EN ASCII y el generador lo casa contra el paso real sin tildes y EXTRAE la subcadena REAL del nodo**. La guarda no se afloja (se comprueba literal despues de extraer) y **una casacion ambigua es ROJO** | el reporte de la vuelta 54 declara **OCHO incisos suyos rechazados por acentos**. La guarda funcionaba; el trabajo de teclear tildes no aportaba nada |
| **`vuelta55_tramo2_nomina.py`** | **sucesor declarado** que identifica el tramo por miembros y sabe continuarlo, con el ordinal derivado del fichero | el ancestro cae en rojo estructural al continuar (seccion 3) |
| **`vuelta55_tallar_planes.py`** | **talla las tablas del reporte de los planes sellados**, y cae en rojo si un motivo no encaja en ninguna forma conocida | la **caida de reporte de la vuelta 54**: la tabla 2.5 no calzaba con sus propios planes |
| **`vuelta55_registro_tramo.py`** | **extrae por expresion regular cada cifra del registro de la salida que su celda cita**, y cae en rojo si alguna no se puede leer | las paradas de credito de las vueltas 31 y 32, las dos por celdas manuales |
| **`vuelta55_caso_positivo.py`** | **se fabrica sobre un acto DECLARADO que la vuelta no toca** | tres vueltas seguidas (52, 53 y 54) tuvieron que reescribirlo por caducidad |

---

## 11. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto. Son NUEVE.**

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **Declare los actos 6 y 49 por PREGUNTA DE POLITICA en vez de fundirlos**, apoyandome en que **cuatro de las cinco razones del filo mandan la decision a una mesa**. | El carril del filo dice literalmente que si lo congelado es politica **el acto NO se funde**, y las cuatro razones lo escriben con sus palabras. **Pero es MI lectura la que decide que esas frases son politica y no matiz**, y con ella dos actos que nadie habia declarado se quedan fuera. Un lector puede decir que el 6 tenia ademas conteos que chocan (forma `CHOCAN`) y que esa era la especie mas conservadora |
| **D2** | **Escribi un SUCESOR del instrumento del tramo en vez de repararlo**, y ademas **el sucesor lo escribi yo con un resolutor inventado que fallo**. | La vara del acta 54 pregunta 3 es exactamente esta (cifras ya citadas por registros implican sucesor), y la tabla de las dos lecturas vive en `03_FUSIONES.md`. **Pero ahora hay dos instrumentos del tramo donde habia uno**, y el mio nacio con un fallo que su propia guarda cazo. **La eleccion es mia y va marcada** |
| **D3** | **En el acto 23 rehice el reparto con DOS INCISOS que la direccion original no tenia**, en vez de espejar exactamente sus marcas. | El espejo exacto habria sido `CUBIERTO` liso en los dos, como hizo la 54 en la otra direccion. **Elegi salvar dos parametros que aquel reparto perdio sin nombrarlos.** Es asimetria mia y va en la direccion de perder menos, pero es asimetria |
| **D4** | **En el acto 28 mande SIETE pasos de APPEND**, y el superviviente pasa de 9 a 16 pasos. | La razon del **364** da por compartido *resolver en un solo contacto* y **el texto del superviviente no lo dice**, medido paso a paso. **Reparti contra el TEXTO y no contra la razon**, porque APPEND no pierde nada. **Pero fabrico un nodo de dieciseis pasos y un solape interno** (sus pasos 5 y 9 miden los dos el impacto) que queda para la poda de la fase 04 |
| **D5** | **En el acto 45 marque `CUBIERTO` con PERDIDA NOMBRADA** las *ventanas de tiempo*, **en vez de `INCISO`**. | El inciso habria quedado adosado a un paso que dice *cuando LA UNICA restriccion es capacidad del vehiculo*, **y lo contradiria**. La tabla de los seis motivos manda perdida nombrada antes que inciso que miente. **Pero es una perdida que yo elijo aceptar** |
| **D6** | **La mentira de cobertura del caso positivo falla por DOS lineas rojas**, la de la guarda 2 y una *marca desconocida*. | Es **una sola causa** (quitar la marca del paso 3) con dos sintomas, no dos motivos independientes. **Pero la leccion de las vueltas 53 y 54 es que una mentira que falla por el motivo que no es no prueba nada**, y aqui hay una linea de mas |
| **D7** | **Aplique una regla de reparto uniforme que yo formule** para elegir entre `INCISO`, `CUBIERTO` con perdida y `APPEND`: **misma cosa dicha implica CUBIERTO (mas INCISO si se pierde un parametro concreto); cosa distinta implica APPEND**. | Es la politica heredada leida al pie, y la aplique igual en los 25 actos para no decidir caso a caso. **Pero la frontera entre *parametro concreto* y *gesto distinto* la trazo yo**, y en las condiciones no hay `INCISO`, asi que ahi la frontera solo tiene dos lados |
| **D8** | **Las CUATRO perdidas nombradas de la vuelta son TODAS de condiciones**, y las cuatro por la misma causa heredada. | El `INCISO` para condiciones **sigue sin existir en el instrumento** (pendiente de doctrina 5, heredado). **Podria haberlas mandado de `APPEND` y no perder nada**, a costa de fabricar condiciones casi gemelas. **Elegi nombrar la perdida** |
| **D9** | **Corri el Gate 0 y el recomputo entre el deshacer del acto 23 y su re-fusion**, y publique esa medicion intermedia como tal. | Sin rehacer `master_graph.json` el recomputo seguia viendo el acto fundido, asi que el ciclo era necesario. **Pero eso mete una medicion mas en la vuelta que no es ni apertura ni cierre**, y la rotule *tras deshacer* para que no se confunda con ninguna de las dos |

---

## 12. PENDIENTES DE DOCTRINA

1. **DONDE VIVE LA PIEZA DECLARADA CUANDO EL ACTO TIENE UN SOLO PAR.** **RESUELTO EN SU RAMA
   NEGATIVA y ABIERTO PARA LA MESA en la positiva** (acta 54, pregunta 2, registrada esta vuelta en
   `03_FUSIONES.md`): el `entregable_esperado` **no es razon**, y los actos **4**, **20** y **42**
   se declaran y acumulan. **Lo que sigue abierto es lo que la mesa tiene que elegir**: una
   **prelacion entre conteos de contenido**, o una **ampliacion de donde vive la pieza declarada**.
2. **EL `INCISO` PARA CONDICIONES SIGUE SIN EXISTIR EN EL INSTRUMENTO.** **Heredado, y esta vuelta
   lo paga CUATRO veces** (`D8`): las cuatro perdidas nombradas de los actos 18, 31, 33 y 45 son
   todas de condiciones, y tres de ellas eran exactamente la figura del inciso.
3. **QUIEN CONTESTA UNA PREGUNTA DE POLITICA DE CATALOGO.** **Heredado, y esta vuelta lo AGRAVA:**
   antes afectaba a dos actos declarados del tramo 1 (el S&OP del `703` y el mapa de influencia del
   `604`); **ahora se le suman los actos 6 y 49 del tramo 2**, que son los primeros que se declaran
   **por politica destapada en una relectura del filo** y no en su propio par.
4. **HEREDADOS Y SIN CAMBIO HOY**: el esquema de `OPERACIONES.jsonl` **sigue sin distinguir
   ejecutada de pendiente** (71 en `LISTA`, medido hoy) y el campo `orden` de la fase 03 **sigue sin
   ser su criterio de orden**.

---

## 13. LO QUE ESTA VUELTA NO HIZO, DICHO EN VEZ DE CALLADO

1. **NO FUNDIO LOS CINCO ACTOS DECLARADOS DEL TRAMO 2** (4, 6, 20, 42 y 49), y **dos de ellos, el 6
   y el 49, los declaro esta misma vuelta**. **Es el incumplimiento de la vuelta y va el primero.**
   Los cinco estan vivos al cerrar, en los puestos **12, 13, 14, 15 y 16** de la nomina del cierre.
2. **NO ABRIO EL TRAMO 3.** El tramo 2 queda cerrado en codigo y el siguiente no se toco.
3. **NO TOCO NINGUNO DE LOS ONCE ACTOS VIVOS DEL TRAMO 1**, incluidos los cinco de fusion pura
   declarados y los tres imposibles por puerta. **Sus ordinales al cerrar se leen de la salida del
   dia**: hoy son los puestos **1 a 11** de la nomina.
4. **NO EJECUTO NINGUNA ARISTA NI PODA DE SOLAPES**: son de la fase 04. **Y esta vuelta dejo un
   solape interno declarado en el acto 28** (`D4`) para esa poda.
5. **NO RESOLVIO LAS DUPLICADAS HISTORICAS** (983 grupos sobre 774 nodos al cierre) ni el alias
   durmiente `modelo_spin_2`: son de `OP-S-12`.
6. **NO REPARO `vuelta54_tramo2_nomina.py`**: le escribio un sucesor (`D2`), y el ancestro **sigue
   cayendo en rojo** si alguien lo corre sobre un tramo ya consumido. **Su rojo queda registrado en
   `03_FUSIONES.md` como lo que es.**
7. **NO CONTESTO NINGUNA DE LAS PREGUNTAS DE POLITICA** que las cuatro relecturas del filo
   destaparon: **las mando a la mesa, que es el carril, y las dejo nombradas.**

---

## 14. LAS PREGUNTAS PARA EL AUDITOR

1. **Una razon del filo que dice *esto lo decide la mesa* o *no lo decido*, cuenta como PREGUNTA DE
   POLITICA que bloquea el acto, o como matiz que no lo bloquea?** (`D1`.) **De la respuesta
   dependen los actos 6 y 49**, que esta vuelta declaro. Si son matiz, los dos eran fusibles y el
   tramo 2 cerraba con 47.
2. **Cuando una fusion se rehace en la direccion contraria, el reparto nuevo debe ESPEJAR las marcas
   del viejo, o puede mejorarlas?** (`D3`.) **Elegi mejorarlas** con dos incisos que la direccion
   original no tenia.
3. **Cuando la RAZON declara compartido un gesto que el TEXTO del superviviente no dice, manda la
   razon o manda el texto?** (`D4`.) **Reparti contra el texto** (APPEND, que no pierde), y en el
   acto 28 eso deja un nodo de dieciseis pasos.
4. **La frontera entre *parametro concreto* (que va de `INCISO`) y *gesto distinto* (que va de
   `APPEND`) la puede fijar el ejecutor con una regla uniforme, o hay que decidirla acto a acto?**
   (`D7`.) **La fije uniforme y la escribi.**
5. **Las perdidas de CONDICIONES deberian ir de `APPEND` mientras el `INCISO` para condiciones no
   exista?** (`D8`.) **Elegi nombrarlas**, y son las cuatro perdidas de la vuelta.
6. **Una medicion intermedia entre dos operaciones de la misma vuelta (el deshacer y la re-fusion
   del acto 23) hay que publicarla, y con que rotulo?** (`D9`.) **La publique rotulada *tras
   deshacer*.**
