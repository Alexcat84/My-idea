# FASE 04: LOS ENLACES

**La unica fase del plan que ANADE en vez de quitar.** No mueve ids, no funde, no
desteje: **pone la arista que falta.**

**Operaciones: `OP-E-01` y `OP-E-02`. LAS DOS LISTAS**, adjudicadas el 11 ago 2026.

---

## LA BOLSA DEL PASO CONTRA NODO

### CORRECCION DECLARADA. **LA CIFRA DE ESTE APARTADO MURIO EL 11 ago 2026**

**Lo que este apartado decia, y se deja escrito para que la correccion se pueda
auditar:** medida con una muestra pineada de 24 sobre 624 candidatos sin arista,
**19 jerarquias sanas, CERO PODAS y 5 falsos positivos**, con proyeccion de 489
aristas y banda de 376 a 586.

**Y la glosa que se colgo de esa cifra, que es la que mas dano hacia:** *la bolsa
no es una mezcla de dos clases de arreglo, es UNA y es la barata; no hay que triar
entre enlazar y podar, hay que enlazar.*

**LO MEDIDO HOY, sobre la bolsa calibrada y con 46 lecturas pineadas:**

| | lo publicado | **lo medido el 11 ago 2026** |
|---|---:|---:|
| candidatos sin arista | 624 | **477** |
| lecturas | 24 | **46** |
| **jerarquia sana** | 19, 79,2% | **32, 69,6%** |
| **madre que repite** | **0** | **7, 15,2%** |
| falso positivo | 5, 20,8% | 7, 15,2% |
| proyeccion de aristas | 489, banda 376 a 586 | **332, banda 263 a 386** |

> **MUERE *CERO PODAS EN VEINTICUATRO LECTURAS*, y muere entera: no encoge, se
> invierte.** La bolsa **SI es una mezcla de dos clases de arreglo**, y la segunda
> clase vale unos **73 pares gemelos**.

> **POR QUE SALIO ASI, y aqui hay que ser exacto porque no todo se explica con el
> tamano de la muestra.** El techo al 95% de un **0 de 24** es **11,7%**. Lo medido
> hoy es **15,2%**. **Las dos cifras no son compatibles del todo, pero por poco**: si
> la tasa verdadera fuera 15,2%, ver cero gemelos en 24 lecturas tiene una
> probabilidad de **cerca del 2%**.

> **O SEA QUE QUEDAN DOS EXPLICACIONES ABIERTAS Y NO SE PUEDE ELEGIR ENTRE ELLAS
> DESDE AQUI:** o la muestra vieja tuvo mala suerte, o **la clase madre que repite no
> se aplico igual** al leerla, y algun gemelo se anoto como sana o como falso
> positivo. **No se puede saber: los 24 viejos son de otro pin y no se releen desde
> esta sesion.** Se deja escrito como pregunta abierta y no como conclusion.

> **LO QUE SI QUEDA CERRADO, y vale para todo el plan: una cifra de CERO sobre 24
> lecturas NO ES UN CERO, ES UN TECHO.** El techo de aquel cero llegaba al **11,7%**,
> y **la glosa lo leyo como si fuera un cero de verdad**. Se escribe *no vi ninguno
> en 24, techo 11,7%*, y **nunca** *no hay*.

**La correccion para el banco de la SESION A esta en `CORRECCIONES_A_APLICAR.md`,
correccion 7.**

---

## LA CALIBRACION DEL VERBO, YA CORRIDA. **PASO 1 DE `OP-E-01`, HECHO**

**Corrida el 11 ago 2026.** Instrumento: `scripts/plan/paso_contra_nodo_calibrado.py`.
Salida: `docs/plan/PASO_NODO_CALIBRADO.jsonl`.

**LO QUE SE CAMBIO, y es UNA cosa sola:** el instrumento importa la normalizacion
del original en vez de reescribirla, **para que la bolsa bruta siga siendo la misma
y las dos corridas se puedan comparar**. Los umbrales no se tocan: titulo 72,
contencion 0,45, minimo 4 tokens. **Lo unico que se anade es la senal del verbo.**

**LA REGLA DE LA SENAL, declarada dentro del script:**

> Se extrae la **FAMILIA DE ACCION** del paso y la del titulo del hijo. **Si las dos
> se conocen y son DISTINTAS, el candidato se descarta.** Si alguna no se reconoce,
> **el candidato se mantiene: la senal solo resta, y en la duda no descarta.**

### EL RESULTADO

| | brutos | descartados por el verbo | **bolsa reducida** |
|---|---:|---:|---:|
| todos los candidatos | 742 | **167** (22,5%) | **575** |
| **los que no tienen arista** | **624** | **147** | **477** |

**POR DOMINIO, la bolsa que queda sin arista:**

| dominio | brutos | **reducidos** | descartados |
|---|---:|---:|---:|
| `quality` | 296 | **208** | 88 |
| `core` | 229 | **199** | 30 |
| `environmental` | 32 | **22** | 10 |
| `franquicias` | 27 | **15** | 12 |
| `exportacion` | 17 | **15** | 2 |
| `health_safety` | 16 | **12** | 4 |
| `entrega` | 4 | **4** | 0 |
| `seguridad_digital` | 2 | **1** | 1 |
| `risk_management` | 1 | **1** | 0 |

**Los pares de familias que mas descartan**: observar contra gestionar (25),
observar contra construir (16), definir contra gestionar (15), construir contra
observar (11), ejecutar contra gestionar (9).

---

## LOS DOS DEFECTOS QUE ENCONTRO LA PRIMERA MUESTRA, y su correccion

**La primera corrida descartaba solo 96 de 742 (12,9%), y la muestra leida sobre
ella salio igual de sucia que la vieja.** Leyendo las 24 aparecio por que, y son
dos defectos del reconocedor de verbos, ninguno de los umbrales.

| defecto | que pasaba | correccion |
|---|---|---|
| **1. la lista de vacias del original CONTIENE VEINTE VERBOS** (`crear`, `definir`, `determinar`, `establecer`, `evaluar`, `hacer`, `identificar`, `realizar`, `revisar`, `usar` y sus formas de tu) | estan ahi con razon **para lo suyo**: el original mide solape de vocabulario y esos verbos son ruido. Pero **para la senal del verbo son justamente la senal**, y se filtraban antes de mirarlas | `contenido()` sigue usando la lista **sin tocar**; **solo `familia()` usa una lista puramente gramatical**, que es la misma menos los verbos |
| **2. la tabla guarda INFINITIVOS y el corpus escribe en imperativo de tu** (`documenta`, `define`, `revisa`) | el reductor de sufijos va al reves: quita la terminacion y busca la raiz, **y la raiz nunca esta en la tabla** | por cada infinitivo se registra tambien su forma de tu, con la regla mecanica **ar a**, **er/ir e**. Nada se anade a mano |

**MEDIDO: la correccion sube el descarte de 96 a 167**, y sobre las 24 ya leidas
**mata 2 de los 5 falsos positivos y no toca NI UNA de las 18 jerarquias sanas.**

> **Esa es la prueba que importa, y es la unica que valida una senal que resta:
> corta falsos y no corta buenos.**

### LO QUE LA CORRECCION NO ARREGLA, dicho con su cifra

**La senal solo puede opinar cuando conoce las DOS familias.** Sobre los 477 que
quedan sin arista:

| | candidatos | |
|---|---:|---:|
| conoce las **dos** familias | 104 | **21,8%** |
| conoce solo la del paso | 230 | 48,2% |
| conoce solo la del hijo | 24 | 5,0% |
| **no conoce ninguna** | 119 | 24,9% |

> **En casi la mitad de la bolsa el hijo no da verbo, porque su titulo es un
> sustantivo:** *Caracteristicas Clave de Producto y Proceso*, *Plan de Accion a
> Corto, Mediano y Largo Plazo*, *Indice de Capacidad de Proceso Cpk*. **Contra un
> titulo sin verbo, la senal no tiene con que comparar**, y por diseno se calla.

---

## LA TASA MEDIDA. **PASO 2 DE `OP-E-01`, HECHO**

**DOS muestras pineadas de 24, con la semilla escrita ANTES de mirar**
(`docs/plan/PIN_SORTEO_CALIBRADO.txt`), **disjuntas entre si**, leidas con la vara
del banco 9.6.1 y clasificadas en las tres clases del encargo.

| | jerarquia sana | madre que repite | falso positivo | total |
|---|---:|---:|---:|---:|
| **la vieja**, sin calibrar | 19 | 0 | 5 | 24 |
| **muestra 1**, bolsa de la correccion parcial | 18 | 1 | 5 | 24 |
| **muestra 2**, bolsa corregida y disjunta | **14** | **6** | **4** | 24 |
| **LAS DOS SOBRE LA BOLSA BUENA** *(22 de la 1 sobreviven a la correccion)* | **32** | **7** | **7** | **46** |

**LA TASA, sobre 46 lecturas y sobre la bolsa que de verdad se va a trabajar:**

| | tasa | **banda de Wilson al 95%** |
|---|---:|---|
| **JERARQUIA SANA**, la arista que falta | **32 de 46, 69,6%** | **de 55,2% a 80,9%** |
| **MADRE QUE REPITE** | **7 de 46, 15,2%** | de 7,6% a 28,2% |
| **FALSO POSITIVO** | **7 de 46, 15,2%** | de 7,6% a 28,2% |

> **POR `P.15`: toda tasa del plan lleva su banda, su N y su fecha de corte. Las
> tres.** N igual a **46 lecturas pineadas**, corte **11 ago 2026**. **Si no cabe la
> banda, no cabe la tasa.**

> **LA CIFRA QUE MUERE HOY ES *CERO PODAS EN VEINTICUATRO LECTURAS*.** Se escribio
> con la muestra vieja y **la muestra nueva la desmiente: siete de cuarenta y seis.**
> La bolsa **si** es una mezcla de dos clases de arreglo.

**PROYECCION sobre los 477, declarada como proyeccion:**

| | esperados |
|---|---|
| aristas que faltan | **unas 332**, banda de Wilson al 95% de **263 a 386** |
| **pares gemelos escondidos en la bolsa** | **unos 73**, banda de **36 a 135** |

---

## EL HALLAZGO GRANDE DE LA MUESTRA: **EL BARRIDO ES TAMBIEN UN DETECTOR DE GEMELOS**

**SEIS de los siete *madre que repite* estan en `quality`, que NO HA ENTRADO NUNCA
AL CRIBADO INTRA.** Y cinco de los siete son **familias de ids o titulos casi
sinonimos**, la misma figura que el cribado caza a mano:

| la madre | el hijo | que son |
|---|---|---|
| `capacidad_de_proceso` | `capacidad_del_proceso` | **una particula de diferencia** |
| `analisis_capacidad_proceso` | `capacidad_de_proceso_2` | sufijo numerico |
| `cero_defectos` | `zero_defects_concepto` | **el mismo titulo traducido** |
| `filosofia_zero_defectos` | `zero_defects_concepto` | tercer nodo del mismo concepto |
| `consejo_calidad_2` | `consejo_de_calidad_y_rol_del_director` | sufijo numerico |
| `identificar_clientes_diseno` | `identificar_clientes_externos_e_internos` | titulos casi sinonimos |
| `programa_de_referidos_de_franquiciados` | `referidos_franquiciados_existentes` | el paso de la madre resume al hijo entero |

> **Esto no estaba previsto y cambia el valor del instrumento.** El barrido se
> construyo para encontrar **aristas que faltan** en dominios cribados. **Lo que la
> muestra ensena es que en los dominios SIN cribar levanta GEMELOS**, que es
> exactamente lo que alli no tiene quien lo busque.

**Los cuatro dominios sin cribar son 1.185 nodos, un tercio del catalogo.** La
bolsa calibrada tiene **221 candidatos suyos** (`quality` 208, `health_safety` 12,
`seguridad_digital` 1). **Es la unica senal medida que existe hoy sobre ellos.**

**Va a `OP-E-03`, y el auditor la adjudico el 11 ago 2026: SIN PUERTA NUEVA.**

### `OP-E-03`, ESCRITA COMO **DIFERENCIA CONTRA LA COLA**

> **El barrido NO se abre como fuente del cribado.** Se corre **el dia en que la
> cola de un dominio cierra**, y solo se pregunta una cosa: **cuales de sus
> candidatos NO estaban en la cola.** **Esa diferencia, y nada mas que esa, va a
> lecturas dirigidas.**

**POR QUE ASI.** Una lectura que entra por dos puertas **se cuenta dos veces**, y
entonces **la tasa por dominio del banco 9.27 deja de significar nada**. La
diferencia contra la cola es **la unica forma de sumar sin contar doble**.

**EL INSTRUMENTO YA ESTA ESCRITO Y PROBADO**:
`scripts/plan/diferencia_contra_cola.py`. Entrada: la cola, los veredictos y los
candidatos. Salida: `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl` con la cuenta por
dominio. **Pasa los ids por el resolutor antes de comparar**, por la regla P.1: la
cola se escribio antes de fusiones y renombres, y comparar literal daria
diferencias falsas.

**ENSAYO EN VACIO DEL 11 ago 2026**, con la cola **tal como esta hoy**, o sea
**incompleta para los cuatro dominios sin cribar**:

| dominio | filas | par repetido | ya en la cola | **diferencia hoy** |
|---|---:|---:|---:|---:|
| `quality` | 208 | 1 | 40 | **167** |
| `core` | 199 | 1 | 36 | **162** |
| `environmental` | 22 | 0 | 0 | **22** |
| `exportacion` | 15 | 0 | 2 | **13** |
| `franquicias` | 15 | 0 | 2 | **13** |
| `health_safety` | 12 | 0 | 5 | **7** |
| `entrega` | 4 | 0 | 2 | **2** |
| `risk_management` | 1 | 0 | 0 | **1** |
| `seguridad_digital` | 1 | 0 | 1 | **0** |
| **TOTAL** | **477** | **2** | **88** | **387** |

> **ESTE ENSAYO NO ES EL RESULTADO Y NO SE PUEDE CITAR COMO TAL.** La cola de
> `quality` **todavia no se ha planificado**, asi que su diferencia de hoy es un
> **techo**, no una cuenta. **La cifra que vale es la del dia del cierre**, y por eso
> la operacion cuelga del **disparador del recomputo** de `08_VERIFICACION`.

> **Lo que el ensayo si prueba es que el instrumento corre y cuadra**: 477 filas
> igual a 2 pares repetidos mas 88 ya en cola mas 387 de diferencia. **Sin fugas.**

**ADDENDUM DE EJECUCION (29 ago 2026, vuelta 94, docs/loop/PROMPT_SIGUIENTE.md TAREA
6) **[CORRECCION DECLARADA DE FECHA (vuelta 98, TAREA 1): la fecha "29 ago 2026" de este marcador estaba TECLEADA y es FALSA. El texto viejo se queda entero y sin borrar una letra (EJECUTOR.md 8). LA FECHA REAL, LEIDA DE GIT EN LA VUELTA 98 con `git log --all --format=%ad^%h^%s --date=short, quedandose con los commits cuyo asunto empieza por "VUELTA 94"`, es 2026-08-27 (commits a4c89ab6, 4c22a083, 4cccca94, 57ab0476, d1d88d1a, 163c51c3, ce8767c9), o sea 27 ago 2026. Techo del reloj del repo, medido con `git log --all --format=%ad --date=short`: 2026-08-27.]**: OP-E-03 ABRE. EL DISPARADOR YA SE ACTIVO.** El cribado intra-dominio cerro
COMPLETO en 3.388 de 3.388 el 13 ago 2026 (commit `9095686e`, "CIERRA EL DOMINIO
quality en el 3255"; reconfirmado en `docs/plan/RECOMPUTO_3388.md` y en
`docs/loop/ACTA_AUDITOR.md`, "LA FASE I DEL CRIBADO INTRA DOMINIO ESTA CERRADA Y
VERIFICADA: 3.388 de 3.388"). Verificado en esta vuelta por conteo directo:
`docs/INTRA_DOMINIO_PARES.jsonl` (la cola) y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
(lo ya leido) tienen los DOS **3.388 filas**: la cola esta cerrada, no es un techo.

**LA CUENTA REAL** (`scripts/plan/diferencia_contra_cola.py`, sin `--dominio`, todos;
`docs/loop/SALIDA_V94_TAREA6_DIFERENCIA_CONTRA_COLA.txt`), sobre la bolsa calibrada
vigente hoy (`docs/plan/PASO_NODO_CALIBRADO.jsonl`, **468 filas**, no las 477 del
ensayo de agosto: la diferencia es que muchos candidatos de entonces ya tienen
arista escrita por otras operaciones del bucle desde el 11 ago, y el instrumento los
excluye por diseno con `--solo-sin-arista`):

| dominio | filas | par repetido | ya en la cola | **DIFERENCIA** |
|---|---:|---:|---:|---:|
| `quality` | 93 | 0 | 13 | **80** |
| `core` | 90 | 0 | 12 | **78** |
| `environmental` | 10 | 0 | 0 | **10** |
| `franquicias` | 7 | 0 | 2 | **5** |
| `health_safety` | 7 | 0 | 3 | **4** |
| `exportacion` | 4 | 0 | 0 | **4** |
| `entrega` | 1 | 0 | 0 | **1** |
| `risk_management` | 1 | 0 | 0 | **1** |
| **TOTAL** | **213** | **0** | **30** | **183** |

**LA CUENTA CUADRA SIN FUGAS**: 213 filas = 0 pares repetidos + 30 ya en cola + 183
de diferencia. **183 pares distintos** (sin repetir por varios pasos de la misma
madre) es la bolsa REAL de `OP-E-03`, escrita en `docs/plan/DIFERENCIA_CONTRA_COLA.
jsonl` (sobrescribe el ensayo de agosto, que se queda arriba sin borrar como
contraste historico: el ensayo proyectaba 387, la cuenta real es 183, casi la
mitad, porque para entonces muchos de esos candidatos ya se habian escrito por otra
via). Los ids pasaron por el resolutor antes de comparar (P.1, funcion `res()`
dentro del propio instrumento). **ESTA CORRIDA ES ESTRICTAMENTE DE SOLO LECTURA**:
no toco `dataset/`, `web/` ni `engine/` (`git status --short` antes y despues,
unico cambio `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl`), asi que el ciclo de tres no
aplica a esta apertura: no hay nada que Gate 0 o las suites puedan invalidar.

**LO QUE NO SE HIZO ESTA VUELTA, Y QUEDA PENDIENTE**: los 183 pares de la
diferencia AUN NO SE LEYERON. `OP-E-03.verificacion` exige que la diferencia se
marque LECTURA DIRIGIDA, no entre en la cola y no mueva el marcador del cribado;
eso se cumple por construccion (el instrumento nunca toca `INTRA_DOMINIO_PARES.
jsonl` ni el marcador). La LECTURA de los 183 (clasificarlos A/B/C/D y escribir sus
veredictos, contados APARTE de la tasa por dominio del cribado) es trabajo de una
vuelta futura, del mismo tamano que las lecturas de `OP-E-06`/`OP-E-07`: no cabia
sin decidir apurado en esta, y `PROMPT_SIGUIENTE.md` pide parar antes que decidir
sin texto que lo sostenga.

**LO QUE SI SE HIZO EN LA VUELTA 96, TAREA 3: EL PRIMER TRAMO YA ESTA LEIDO.**
El apartado de arriba se queda entero, sin borrar una palabra: describia el estado
de la vuelta 94, cuando la bolsa estaba establecida y sin leer. **Hoy ya no lo esta.**
Se leyeron las filas **1 a 40** de las **183**, con la vara del banco `9.6.1` para la
clase, la del `9.6.2` para la direccion y la del `9.6.3` para no dejar que el tamano
del solape decida. **Los cinco puntos de `OP-E-03.verificacion` se cumplen, y los
tres que son medibles se REMIDIERON en la vuelta en vez de heredarse.**

| lo que salio | cifra |
|---|---:|
| pares leidos | **40** de 183 |
| clase A, REPITE | **1** |
| clase B, DUDOSO | **1** |
| clase C | **0** |
| clase D, CONTINUA | **38** |
| direccion leida y afirmada | **29** |
| direccion NO RESUELTA, declarada | **11** |
| aristas escritas o retiradas | **0** |
| pares que quedan sin leer | **143** (filas 41 a 183) |

**CERO ARISTAS**: `OP-E-03` es LECTURA DIRIGIDA y su producto es el juicio, no el
cableado. El detalle entero, con las seis figuras que la lectura destapa y las seis
guardas probadas por mutacion, esta en `docs/PENDIENTES.md`, seccion "VUELTA 96,
TAREA 3". Los veredictos viven en `docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl` y
**no** en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`: se cuentan aparte de la tasa por
dominio del banco `9.27`, como manda el punto 5 de la verificacion.

**LO QUE SE HIZO EN LA VUELTA 97, TAREA 2: EL SEGUNDO TRAMO TAMBIEN ESTA LEIDO.**
El apartado de arriba se queda entero, sin borrar una palabra. Lo que cambia es
su ultima fila: decia que quedaban **143** pares sin leer, y hoy quedan **83**.
Se leyeron las filas **41 a 100** de las **183**, con la misma vara y con **el mismo
umbral de direccion**, que el acta de la vuelta 96 (seccion 4.4) adjudico bien
puesto y sin tocar.

| lo que salio | cifra |
|---|---:|
| pares leidos en este tramo | **60** (filas 41 a 100) |
| pares leidos en total | **100** de 183 |
| clase A, REPITE | **3** |
| clase B, DUDOSO | **1** |
| clase C | **0** |
| clase D, CONTINUA | **56** |

**[CORRECCION DECLARADA (vuelta 98, TAREA 3, relectura conjunta del par 42).]** La tabla de arriba se queda entera y sin borrar una celda. **LAS CIFRAS BUENAS, RECOMPUTADAS DEL PROPIO JSONL** en la vuelta 98 y no tecleadas: **clase A, REPITE: 2** (antes 3) y **clase D, CONTINUA: 57** (antes 56). El **par 42** pasa de **A** a **D** tras la relectura conjunta que pidio el acta de la vuelta 97 (seccion 3.2, linea 34789): el residuo del hijo no son dos lineas sueltas sino una secuencia con dependencia (el paso 4 consume la salida del 3), y los **entregables lo confirman** (la madre entrega un protocolo de respuesta a incidentes, el hijo un registro de incidente, que es lo que el paso 2 de la madre produce al ejecutarse). **La direccion NO cambia** y las cifras de direccion siguen en **33** afirmadas y **27** no resueltas. **Ninguna clase del tramo 1 se mueve**: el par **12** sigue en **A**.

| direccion leida y afirmada | **33** |
| direccion NO RESUELTA, declarada | **27** |
| aristas escritas o retiradas | **0** |
| pares que quedan sin leer | **83** (filas 101 a 183) |

**LA PROPORCION DE DIRECCIONES NO RESUELTAS SUBE, y se mide en vez de explicarse.**
Del **27,5%** del tramo 1 al **45.0%** de este. El encargo preveia el caso de una
proporcion PARECIDA (*"es la bolsa, no tu vara"*); como no lo es, esa conclusion no
se invoca: se construyo un instrumento que la pone a prueba
(`scripts/loop/vuelta97_tarea2_senal_de_la_bolsa.py`). Lo medido es que **la bolsa
viene ordenada de mas fuerte a mas debil** (mediana de `titulo_ratio` 84,3 en el
tramo 1, 78,2 en el 2, 76,2 en lo que queda) y que **dentro del tramo 2 las filas sin
direccion son las mas debiles medidas por fuera de la lectura**. **SE DECLARA QUE ESO
NO PRUEBA QUE EL UMBRAL SEA EL CORRECTO**, y va marcado como discutible.

**CERO ARISTAS**: `OP-E-03` sigue siendo LECTURA DIRIGIDA y su producto es el juicio.
El detalle entero, con las **nueve** figuras que la lectura destapa y las guardas
probadas por mutacion, esta en `docs/PENDIENTES.md`, seccion "VUELTA 97, TAREA 2".
Los veredictos viven en `docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl` y **no** en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.

**LO QUE SE HIZO EN LA VUELTA 98, TAREA 4: EL TERCER TRAMO SE ABRE Y SE LEE HASTA LA MITAD.**
Los dos apartados de arriba se quedan enteros, sin borrar una palabra. **`OP-E-03`
NO CIERRA**: se leyeron las filas **101 a 150** de las **183** y **quedan 33 sin
leer**, filas 151 a 183. La fecha de este apartado **se leyo de git en esta vuelta**
(`git log --all --format=%ad --date=short` sobre los commits cuyo asunto empieza
por "VUELTA 98"): **2026-08-27**. No esta tecleada.

| lo que salio | cifra |
|---|---:|
| pares leidos en esta mitad del tramo 3 | **50** (filas 101 a 150) |
| pares leidos en total | **150** de 183 |
| clase A, REPITE | **0** |
| clase B, DUDOSO | **0** |
| clase C, SANO CON FIGURA | **1** |
| clase D, CONTINUA | **49** |
| direccion leida y afirmada | **20** |
| direccion NO RESUELTA, declarada | **30** |
| direcciones invertidas y afirmadas | **1** |
| aristas escritas o retiradas | **0** |
| pares que quedan sin leer | **33** (filas 151 a 183) |

**EL PRIMER `C` DE TODA LA LECTURA DE `OP-E-03`.** El tramo 1 dio **C 0** y el
tramo 2 tambien. El par **111** es la figura del banco **9.22**, primer polo:
procedimiento en los **dos** sentidos sobre **dos lineas distintas**, cuyo arreglo
prescrito es **enlace mutuo** y no fusion. **NO se escribio ninguna arista**:
`OP-E-03` es LECTURA DIRIGIDA y su producto es el juicio.

**LA PROPORCION DE DIRECCIONES NO RESUELTAS SUBE OTRA VEZ**, del **27,5%** del
tramo 1 y el **45,0%** del tramo 2 al **60,0%** de esta mitad. Es la direccion que
el encargo preveia para el tramo mas debil de la bolsa (mediana de `titulo_ratio`
**76,2** contra **84,3** del tramo 1), asi que **se publica con la cifra y sin
maquillarla**.

**EL CIERRE DE `OP-E-03`: LAS 183 DE 183, RECONTADAS DE LOS CUATRO FICHEROS DE TRAMO (2026-08-27).**
Los apartados de arriba se quedan enteros, sin borrar una palabra. **`OP-E-03` QUEDA LEIDA ENTERA: 183 de 183**, recontadas de los CUATRO ficheros de tramo que existen (el encargo de la vuelta 99 decia "tres"; la cuenta real de hoy es cuatro, declarado como discrepancia de redaccion del encargo, no del trabajo).

| ficheros de tramo | filas |
|---|---:|
| `OP_E_03_LECTURA_TRAMO1_V96.jsonl` | 40 (1 a 40) |
| `OP_E_03_LECTURA_TRAMO2_V97.jsonl` | 60 (41 a 100) |
| `OP_E_03_LECTURA_TRAMO3_V98.jsonl` | 50 (101 a 150) |
| `OP_E_03_LECTURA_TRAMO4_V99.jsonl` | 33 (151 a 183) |
| **total** | **183** |

| cierre de la operacion entera | cifra |
|---|---:|
| clase A, REPITE | **3** |
| clase B, DUDOSO | **2** |
| clase C, SANO CON FIGURA | **1** (par 111) |
| clase D, CONTINUA | **177** |
| direccion leida y afirmada | **95** |
| direccion NO RESUELTA, declarada | **88** (48,1%) |
| direcciones invertidas y afirmadas | **2** (pares 16, 114) |
| aristas escritas o retiradas en toda la operacion | **0** |

**CORRECCION DECLARADA (vuelta 100, TAREA 4, encargo de la vuelta 99 acta seccion 2 y 4.4.) LA TABLA DE ARRIBA NO SE BORRA: es el texto viejo, y era la cifra CRUDA (campo `direccion_leida` sin corregir).** Recontado con `scripts/loop/contar_cierre_efectivo.py` (aplica `correccion_v99` del par 147 y `correccion_v100` de los pares 174 y 175, TAREA 3 de esta vuelta): **clase A 3, B 2, C 1 (par 111), D 177; direccion leida y afirmada 92, NO RESUELTA 91 (49,7%); invertidas 2 (pares 16, 114).** LA CIFRA BUENA ES **92 / 91 (49,7%)**.

**EL CUARTO TRAMO (filas 151 a 183, 33 pares) por si solo:** clase D **33**, direccion leida **13**, NO RESUELTA **20** (**60,6%**), mediana de `titulo_ratio` **73,2** (maximo 81,6, la mas baja de la bolsa). **CONFIRMA LA PREDICCION DEL ACTA 98**: proporcion NO RESUELTA por encima del 60,0%.

**ESTADO DE `OP-E-03` SE QUEDA EN `LISTA`**: la lectura esta completa, pero mover `estado` a `HECHA` es una decision que este addendum no toma; la TAREA 4 del encargo de la vuelta 99 mide, sin resolver, que las dependencias declaradas (`OP-E-01`, `OP-U-02`) no estan en `HECHA`.

**CORRECCION DECLARADA (vuelta 99, TAREA 2, relectura conjunta del par 147, acta
98 seccion 3.2). EL PARRAFO DE ARRIBA NO SE BORRA: es el texto viejo.** El
auditor discrepo de la unica lectura ciega de las once (`consortium_benchmarking`
contra `clasificacion_benchmarking`), y `AUDITOR.md` 1.3 pone la decision en el
ejecutor. Aplicado el test de reconocimiento del banco **9.6.2** ("el hijo cabe
entero dentro de UN paso de la madre, y la madre conserva materia propia que el
hijo no toca en ningun paso") sobre el paso 2 de la madre ("decidir el tipo de
participantes: internos, externos, competidores o no competidores"): **el test
FALLA**. Los pasos 2 a 5 de `consortium_benchmarking` (acordar alcance, metricas
y cronograma; designar facilitador; fijar criterios de validacion de datos;
ejecutar el estudio) son diseno y ejecucion aguas abajo de esa decision, no la
decision misma; el entregable del hijo es un consorcio YA FORMALIZADO, no una
definicion de tipo de participantes. **SE SOSTIENE EL CASO DEL AUDITOR: el par
147 pasa de DIRECCION AFIRMADA a NO RESUELTA.** La clase D no cambia. Recomputado
con `scripts/loop/vuelta99_tarea2_relectura147.py`
(`docs/loop/SALIDA_V99_TAREA2_RELECTURA147.txt`): **direccion leida y afirmada
20 a 19, direccion NO RESUELTA 30 a 31, proporcion NO RESUELTA 60,0% a 62,0%**.
La fila 147 de `docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl` queda con su
`direccion_leida` y `razon` viejas intactas y un campo `correccion_v99` anadido
aparte.

**CORRECCION DECLARADA (vuelta 100, TAREA 3, dos relecturas conjuntas con el
auditor, encargo de la vuelta 99 secciones 3.1 y 3.2, acta 99). LOS PARRAFOS
DE ARRIBA NO SE BORRAN: son el texto viejo.** Sobre el **par 175**
(`validar_modelo_financiero` -> `valor_de_vida_del_cliente`, paso 2, "Calcular
costos de adquisicion de clientes, tasas de conversion y Customer Lifetime
Value (LTV)"): leidos hoy los dos nodos, el hijo tiene CUATRO pasos y SOLO EL
PRIMERO calcula; el tercero y el cuarto ("Implementar nuevos programas y
ofertas que incrementen el LTV", "Mejorar la eficiencia de los procesos de
retencion y crecimiento") son INTERVENCION OPERATIVA que el paso 2 de la
madre no contempla. El test del **9.6.2** falla POR EXCESO DE GENERO: el
nombre literal "Customer Lifetime Value" coincide, pero el propio 9.6.2 dice
que la prueba lexica no sirve (34 de 46 marcados por vocabulario, 3% de
precision). **SE SOSTIENE EL CASO DEL AUDITOR: NO RESUELTA.** Sobre el **par
174** (`desarrollo_value_proposition_usp` -> `posicionamiento_vs_competidores`,
paso 1, "Identificar que hace unico al negocio frente a competidores
directos"): los CUATRO pasos del hijo son movimientos de una conversacion de
venta con un candidato a franquiciado, y su propio entregable lo dice
("listo para usar en cualquier conversacion con un candidato"); el hijo no
IDENTIFICA lo unico del negocio, lo PRESUPONE identificado y lo despliega
contra un prospecto: es el patron CASADO POR OBJETO Y NO POR ACCION (par 163
del mismo tramo). **SE SOSTIENE EL CASO DEL AUDITOR: NO RESUELTA.** Los dos
pares pasan de DIRECCION AFIRMADA a NO RESUELTA; la clase D no cambia en
ninguno de los dos. Recomputado con
`scripts/loop/vuelta100_tarea3_relectura_174_175.py`
(`docs/loop/SALIDA_V100_TAREA3_RELECTURA.txt`): **el cuarto tramo pasa de
direccion afirmada 13 / NO RESUELTA 20 (60,6%) a afirmada 11 / NO RESUELTA 22
(66,7%)**. Las filas 174 y 175 de
`docs/plan/OP_E_03_LECTURA_TRAMO4_V99.jsonl` quedan con su `direccion_leida`
y `razon` viejas intactas y un campo `correccion_v100` anadido aparte en cada
una.

---

## `OP-E-01`, DONDE QUEDA EL ORDEN ADJUDICADO

| paso | que se hace | estado |
|---:|---|---|
| **1** | la calibracion del verbo | **HECHO el 11 ago 2026** |
| **2** | muestra pineada nueva sobre la bolsa reducida | **HECHO: dos muestras, 46 lecturas** |
| **3** | decidir leer entera o proyectar | **es lo que queda, y ahora se decide con cifra** |

**LO QUE EL PASO 3 YA PUEDE USAR:** de cada cien candidatos de la bolsa reducida,
**setenta son arista que falta, quince son gemelos y quince son basura**. **Leer los
477 cuesta, en el peor caso, 477 lecturas; no leerlos cuesta meter 71 aristas malas
y perder 73 gemelos.**

> **CORRECCION DECLARADA (26 ago 2026, vuelta 76, adjudicada por el auditor,
> acta de la vuelta 75 seccion 4.4).** La verificacion de `OP-E-01` transcribia
> `P.9` sin su punto 1, y esa omision dejo pasar en el tramo 1 la arista
> `segmentos_de_clientes_problema_necesidad -> get_out_of_the_building` contra
> un destino condenado (`OP-M-05-EDIFICIO`, fusion de la fase 03 enrutada a la
> fase 06, no ejecutada). Se anade el **FILTRO DE ELEGIBILIDAD `P.9.1`,
> OBLIGATORIO ANTES DE ESCRIBIR**: todo candidato de la bolsa se cruza contra
> los campos `eliminar` y `superviviente` de las operaciones NO EJECUTADAS. Si
> el destino o la madre muere en una operacion pendiente, el par NO se lee
> para escribir: se aparta con el id de esa operacion escrito al lado y espera
> su turno. Es `P.9` punto 1 y aplica a toda operacion que escriba aristas
> desde una bolsa calculada. El texto viejo de la tabla no se toca: esta linea
> se anade a lo que ya estaba.

> **CORRECCION DECLARADA (26 ago 2026, vuelta 77, decision del fundador en
> docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md).** El
> filtro de arriba solo cruzaba `eliminar` y `superviviente`, y por eso
> nunca podia ver a `OP-S-09` (tipo `RENOMBRE_CON_ALIAS`: sus nodos no se
> eliminan, se renombran conservando alias, asi que viven en el campo
> `nodos`, no en `eliminar`). Con la nomina de `OP-S-09` ya escrita en su
> campo `nodos` (69 ids, vuelta 77, `docs/loop/SALIDA_V77_OP_S09_NOMINA.txt`),
> el filtro se ENSANCHA para cruzar tambien `nodos` en toda operacion NO
> EJECUTADA de tipo `RENOMBRE_CON_ALIAS`, en las dos direcciones (madre o
> hijo del candidato). Implementado en
> `scripts/loop/vuelta77_filtro_p91_ensanchado.py`, con caso positivo
> verificado en las dos direcciones. El texto viejo de arriba no se toca.

> **CORRECCION DECLARADA (26 ago 2026, vuelta 78, adjudicada por el auditor
> por cita, acta de la vuelta 77 seccion 3 D4 y seccion 5 punto 5, sin
> doctrina nueva).** El filtro de arriba solo cruzaba el PLAN
> (`eliminar`, `superviviente`, `nodos`), y el plan no es el inventario: las
> fusiones pendientes de verdad son los **551 veredictos A** del cribado
> (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`), y solo una parte pequena tiene
> operacion escrita todavia. Un A sin operacion es una fusion que el plan
> aun no ha citado, y `P.9` punto 1 (los enlaces corren DESPUES de las
> fusiones que tocan sus destinos) no distingue si la fusion ya tiene ficha
> o no. Se ENSANCHA el filtro para cruzar tambien los veredictos **A**
> donde los DOS nodos del par esten vivos hoy (**187** nodos vivos que
> participan en al menos un A con otro nodo vivo, sobre 551 A totales,
> medido por el auditor y confirmado por corrida propia en
> `scripts/loop/vuelta78_filtro_p91_vara_a.py`,
> `docs/loop/SALIDA_V78_FILTRO_P91_VARA_A_CASO_POSITIVO.txt`). Un A con un
> extremo ya deprecado no aparta nada: ya fue resuelto por otra via. El
> texto viejo de arriba no se toca.

> **CORRECCION DECLARADA (26 ago 2026, vuelta 79, adjudicada por el auditor
> por cita, acta de la vuelta 78 seccion 3 D4 y seccion 5 punto 4, sin
> doctrina nueva).** El reporte de la vuelta 78 (seccion 3.2) publico, como
> criterio unico para las once aristas que la vara de arriba toca, este
> texto, citado sin reescribir: *"si el extremo ESCRITO en la arista (no su
> companero de A) esta condenado por una operacion sin ser su
> superviviente, la arista SE MUEVE; si el extremo escrito ES el
> superviviente declarado, o si ninguna operacion condena al extremo
> escrito, la arista SE QUEDA con la razon puesta."* **Ese criterio no
> produce la decision que la propia tabla de esa seccion publica**: la fila
> 11 tiene el hijo escrito sin ninguna operacion que lo condene, y por el
> criterio publicado debia quedarse; se movio. El criterio real, que si
> existia pero solo vivia en el docstring de
> `scripts/loop/vuelta78_tarea32_decision_once.py`, es este: **no es lo
> mismo que el companero de A caiga en el `eliminar` de una FUSION que en
> los `nodos` de un RENOMBRE_CON_ALIAS. Una fusion ya declara
> superviviente: si el extremo escrito no es el condenado, el extremo
> escrito esta a salvo y la arista SE QUEDA (filas 2, 3 y 4). Un renombre no
> mata a nadie y no declara ganador: cual de los dos gemelos vivira sigue
> abierto, asi que la arista escrita sobre cualquiera de los dos SE MUEVE y
> espera (fila 11). Y cuando el archivo remite la familia a mesa, manda la
> mesa (fila 6, puesto 460).** Verificado contra las fichas en esta vuelta
> (`docs/loop/SALIDA_V79_TAREA12_FICHAS.txt`): `OP-M-05-APERTURA` es
> `FUSION DE MESA` con `superviviente` `customer_validation` y `eliminar`
> de dos ids; `OP-S-09` es `RENOMBRE_CON_ALIAS` con `superviviente` `null`.
> Las once disposiciones de la vuelta 78 no cambian: solo se corrige el
> criterio publicado, que vivia fuera del reporte. El texto viejo de arriba
> no se toca.

> **CORRECCION DECLARADA (26 ago 2026, vuelta 79, relectura conjunta del
> discutible 3 del reporte de la vuelta 78, seccion 4.4, con el caso del
> auditor confirmado contra el grafo, acta de la vuelta 78 seccion 3 D3 y
> seccion 5 punto 3).** El tramo 4 de `OP-E-01` (vuelta 78) escribio la
> arista `extraer_priorizar_hipotesis -> value_proposition_startup`. **SE
> REVIERTE.** El paso 1 de la madre (*"Lista todo lo que tiene que ser cierto
> sobre tu modelo de negocio, tu propuesta de valor y tu cliente"*) manda
> LISTAR; la propuesta de valor es uno de los tres objetos que se listan, no
> la accion que el paso ejecuta, y el resumen de la propia madre lo dice sin
> ambiguedad: *"A partir de tu mapa de propuesta de valor [...] identifica
> todas las suposiciones"*, o sea que la propuesta de valor es insumo previo,
> no resultado de este paso. El hijo (identificar problemas del segmento,
> definir que caracteristicas los resuelven, verificar el encaje) no ejecuta
> "listar hipotesis": la precede. Contraste con la hermana que si pasa la
> vara en el mismo hub, `etapa_build_business_case` (paso 1 *"Definir el
> mercado objetivo, posicionamiento y propuesta de valor del producto"*),
> donde la accion del paso ES definir la propuesta de valor y el hijo es como
> se define: esa se queda. Verificado contra `dataset/nodos/*.json` en esta
> vuelta y escrito en
> `scripts/loop/vuelta79_tarea31_relectura_conjunta.py`
> (`docs/loop/SALIDA_V79_TAREA31_REVERSION.txt`), quitada de las DOS vistas a
> la vez y confirmado tras el ciclo de Gate 0 que no reaparece
> (`docs/loop/SALIDA_V79_GATE0_CMD1_TRAS31.txt`). Las otras tres del mismo
> hub (`actualizar_business_model_canvas_tuneup`,
> `etapa_build_business_case`, `ventaja_competitiva_producto`) no se tocan:
> ya fueron confirmadas en el acta de la vuelta 78.

> **GUARDA NUEVA (26 ago 2026, vuelta 79, adjudicada por cita, SIN doctrina
> nueva, acta de la vuelta 78 seccion 4 y seccion 5 punto 6).** La bolsa
> filtrada trajo el mismo par DOS VECES en la vuelta 78, una en cada
> direccion (`necesidades_reales_vs_declaradas -> descubrir_necesidades_del_cliente`,
> fila 1; la reciproca en la fila 46), y el campo `arista` del calibrador NO
> TIENE DIRECCION: al escribir la fila 1, la fila 46 quedo resuelta sin que
> nadie la mirara. Es el mismo fallo que banco 9.6.2 nombra para la vara al
> reves. **LA GUARDA, adjudicada por cita de 9.6.2 y de `AUDITOR.md` seccion
> 3 (el criterio del forastero: la fuente propone, la lectura confirma):**
> antes de leer, la bolsa filtrada se agrupa por **par NO DIRIGIDO**; cuando
> el mismo par aparece en las dos direcciones, las dos filas se leen JUNTAS y
> la direccion se decide con 9.6.2 explicitamente, con las dos opciones
> escritas en la razon y la descartada nombrada; la fila hermana no se cuenta
> como candidato aparte en la cifra de bolsa restante. Implementada en
> `scripts/loop/vuelta79_guarda_par_no_dirigido.py`, con caso positivo
> SINTETICO verificado (`docs/loop/SALIDA_V79_TAREA4_GUARDA_CASO_POSITIVO.txt`):
> agrupa un par en dos direcciones, no rompe el candidato normal de una sola
> direccion, y no agrupa por falso positivo dos filas que solo comparten UN
> extremo con companeros distintos. **La direccion de la fila 1 ya fue
> adjudicada por el auditor y NO se toca**: la madre conserva materia propia
> que el hijo no toca (la miopia de marketing de Levitt, el rediseno de la
> propuesta de valor) y el hijo despliega el paso 2 de la madre con
> procedimiento propio de 6 pasos; la arista se queda como esta escrita.

> **CORRECCION DECLARADA (26 ago 2026, vuelta 80, relectura conjunta de los
> discutibles 2 y 3 del reporte de la vuelta 79 seccion 5.4, con el caso del
> auditor confirmado contra el grafo, acta de la vuelta 79 seccion 2 D2/D3 y
> seccion 5 puntos 2 y 3).** El tramo 5 de `OP-E-01` (vuelta 79) escribio dos
> aristas que **SE REVIERTEN**:
>
> 1. `producto_mercado_fit_motores -> afinar_motor_crecimiento`. **Es un
>    radio sobre una CADENA COMPLETA ya establecida en el grafo de la
>    apertura**: el paso 4 de la madre (*"Usa la contabilidad de la
>    innovacion..."*) nombra literalmente `contabilidad_innovacion`, YA
>    enlazado; `contabilidad_innovacion.nodos_siguientes` incluye
>    `establecer_linea_base_mvp` (*"Este es el primer paso..."*, por su
>    propio resumen); `establecer_linea_base_mvp.nodos_siguientes` es
>    exactamente `['afinar_motor_crecimiento']` (*"Es el segundo paso..."*).
>    Verificado campo a campo contra `dataset/nodos/*.json` en esta vuelta.
>    Es el CAVEAT MEDIDO de la 9.6.1 (*"la familia ENCADENADA no se cuenta
>    por radios [...] antes de contar, se mira la FORMA"*): el hijo no es
>    contenido huerfano de camino (banco 9.6), esta a tres saltos por el
>    camino que el propio paso 4 nombra. Mismo error, mismo remedio, que la
>    correccion declarada del primer ejemplar de la 9.6
>    (`proceso_diseno_modelo_negocio_5_fases`).
> 2. `terminologia_clave_breakthrough -> analisis_sintomas`. El paso 2 de la
>    madre es literal: *"Diferenciar sintomas de causas en cada problema
>    detectado"*. Los cuatro pasos del hijo (recolectar datos de ocurrencia,
>    ubicar la falla con diagramas de flujo, aplicar Pareto y
>    estratificacion, documentar frecuencia/severidad/tipo) **caracterizan
>    el sintoma; ninguno lo DIFERENCIA de la causa**. Los entregables no
>    coinciden (madre: *"glosario de terminos [...] y lista de teorias a
>    probar"*; hijo: *"analisis documentado de sintomas"*), que 9.6.2
>    declara la senal mas fiable que los pasos. Por 9.6.2 (*"la vara tiene
>    direccion"*), el hijo PRECEDE la accion del paso, no la ejecuta.
>
> Verificado contra `dataset/nodos/*.json` en esta vuelta y escrito en
> `scripts/loop/vuelta80_tarea3_relectura_conjunta.py`
> (`docs/loop/SALIDA_V80_TAREA3_REVERSION.txt`), las dos quitadas de las DOS
> vistas a la vez y confirmado tras el ciclo de Gate 0
> (`docs/loop/SALIDA_V80_GATE0_CMD1_TRAS_TAREA3.txt`, OK, sin reaparicion).
> Aristas tras la doble reversion: 8.958 `nodos_siguientes` / 8.937
> `nodos_previos` / 17.895 suma / 9.581 union
> (`docs/loop/SALIDA_V80_CONTEO_TRAS_TAREA3.txt`), dos menos que las 8.960 /
> 8.939 / 17.899 / 9.583 de la apertura de esta vuelta, en las cuatro
> cifras, como corresponde a dos aristas quitadas de las dos vistas.

> **LA VARA NUEVA DE LA CADENA, EN OPERACION (26 ago 2026, vuelta 80,
> adjudicada por el auditor en el acta de la vuelta 79 seccion 5 punto 6,
> SIN doctrina nueva).** Desde el tramo 6 de `OP-E-01`, antes de escribir
> una arista se mide si el hijo YA CUELGA de la cadena PROPIA de la madre
> (sus pasos enumerados, en el orden que la madre declara), reusando la
> maquina de `docs/loop/_auditor_v79_atajo.py`
> (`scripts/loop/vuelta80_vara_cadena.py`). **No aparta candidatos por si
> sola** (el acta 79 lo dejo escrito: *"alcanzable no es lo mismo que
> encadenado"*): marca cada candidato ALCANZABLE para que la lectura
> verifique EXPLICITAMENTE si el camino es la cadena propia antes de
> decidir, que es exactamente el error que produjo D2 (revertida arriba en
> esta misma vuelta). Integrada en
> `scripts/loop/vuelta80_tramo6_filtrar.py`, que anota la alcanzabilidad de
> las 30 unidades de cabeza sin descartar ninguna por eso
> (`docs/loop/SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt`).

> **CORRECCION DECLARADA (26 ago 2026, vuelta 82, relectura conjunta del
> discutible 1 del reporte de la vuelta 80 seccion 5.5, con el caso escrito
> del auditor verificado contra el grafo, acta de la vuelta 81 y encargo de
> la vuelta 82).** El texto viejo, sin borrar, tal como el reporte de la
> vuelta 80 lo publico en su seccion 5.3 (fila 27 de la lectura fresca del
> tramo 6) y lo repitio en su seccion 5.5: ***"`descubrir_necesidades_del_
> cliente -> traduccion_necesidades_cliente`, NO ESCRITA POR CAUTELA [...]
> Se decidio NO escribir por ser la misma especie de redirect de paso que
> D2 [...] y porque la familia ya tiene un camino establecido mas
> especifico (`identificar_clientes_externos_e_internos ->
> customer_needs_spreadsheet -> traduccion_necesidades_cliente`) para la
> misma transicion."***
>
> **Esa razon se cae al medirla campo a campo contra `dataset/nodos/*.json`
> en esta vuelta.** `dataset/nodos/identificar_clientes_externos_e_internos.
> json` trae `nodos_siguientes = [descubrir_necesidades_del_cliente,
> customer_needs_spreadsheet]`: los DOS son hijos DIRECTOS del mismo abuelo,
> no una cadena madre-hijo. El "camino establecido de la familia" que el
> reporte 80 cito arranca en ese abuelo y **no pasa por la madre
> (`descubrir_necesidades_del_cliente`) en ningun salto**, y
> `customer_needs_spreadsheet` **no esta entre los 9 `nodos_siguientes`** de
> la madre (`qfd_matriz`, `diseno_de_procesos_por_caracteristicas`,
> `diseno_servicio_calidad`, `gestion_de_quejas_y_fidelizacion`,
> `herramientas_de_diseno_de_calidad`, `sistema_manejo_quejas`,
> `desarrollar_caracteristicas_producto`, `design_for_six_sigma_dfss`,
> `six_sigma_dmaic`). No es la misma especie de error que D2 (ahi si habia
> una cadena propia de la madre, en su propio orden, que el hijo ya
> colgaba): aqui la vara nueva de la cadena **no muerde**, porque el unico
> camino previo que encuentra (`SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.
> txt`, fila 27) sube por `design_for_six_sigma_dfss -> innovacion_tipo_ii
> -> juran_quality_by_design -> identificar_clientes_externos_e_internos ->
> customer_needs_spreadsheet`, que tampoco es la cadena propia de la madre
> en su propio orden (`customer_needs_spreadsheet` no es paso de la madre).
>
> **Y las dos senales que 9.6.2 pide sobran a favor.** El hijo cabe entero
> en el paso 6 de la madre (*"Traducir las necesidades priorizadas al
> lenguaje tecnico de la organizacion"*), casi palabra por palabra el
> proposito entero del hijo (*"Traduccion de Necesidades del Cliente al
> Lenguaje del Proveedor"*); la madre conserva materia propia de sobra en
> los otros cinco pasos (recoleccion, listar, distinguir tipos de
> necesidad, investigar usos no previstos, analizar y priorizar), ninguno
> sobre traduccion. Los entregables (la senal que 9.6.2 declara mas
> fiable) confirman: la madre entrega *"lista de necesidades del cliente
> priorizadas Y traducidas al lenguaje de la organizacion"* (dos
> productos), y el hijo entrega exactamente el segundo (*"Documento de
> necesidades del cliente traducidas a especificaciones tecnicas claras y
> medibles"*).
>
> **SE ESCRIBE**: `descubrir_necesidades_del_cliente ->
> traduccion_necesidades_cliente`, en las DOS vistas a la vez
> (`scripts/loop/vuelta82_tarea3_escribir.py`,
> `docs/loop/SALIDA_V82_TAREA3_ESCRIBIR.txt`), con chequeo de escalera
> exacto (`docs/loop/SALIDA_V82_TAREA3_ESCALERA.txt`: en `nodos_siguientes`
> de la madre True, en `nodos_previos` del hijo True, cero inversas) y
> recomputo tras la escritura
> (`docs/loop/SALIDA_V82_GATE0_CMD1_TRAS_TAREA3.txt`, OK). Aristas tras la
> escritura: 8.961 `nodos_siguientes` / 8.940 `nodos_previos` / 17.901 suma
> / 9.584 union (`docs/loop/SALIDA_V82_CONTEO_TRAS_TAREA3.txt`), una mas
> que las 8.960 / 8.939 / 17.899 / 9.583 de la apertura de esta vuelta, en
> las cuatro cifras, como corresponde a una arista anadida en las dos
> vistas.

---

## `OP-E-01`, CIERRE MEDIDO (27 ago 2026, vuelta 87)

**No se anuncia: se talla, con instrumento propio y con los pares leidos de
los ficheros.** El campo `estado` de `OPERACIONES.jsonl` NO SE TOCA (00_
INDICE.md linea 111): sigue en `LISTA`, y la ejecucion queda declarada en el
campo `nota` de `OP-E-01`, con esta misma cifra dentro.

**La cola final, cuatro unidades (indices 117 a 120 de la bolsa filtrada
V87), leida POR LO NO DECIDIDO:**

| # | par (paso) | decision | discutible | alcanzable (vara de la cadena) |
|---:|---|---|:---:|---|
| 117 | `juran_rcca_metodo -> diseno_implementacion_remedio` (paso 3, quality) | **SE ESCRIBE** | SI | ALCANZABLE (6 saltos), ES la cadena propia de la madre |
| 118 | `valor_intangible_sostenibilidad -> alineacion_engagement_estrategia_general` (paso 1, environmental) | NO SE ENLAZA | SI | SIN CAMINO PREVIO |
| 119 | `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` (paso 4, core) | **SE ESCRIBE** | | ALCANZABLE (5 saltos), NO es la cadena propia de la madre |
| 120 | `no_shop_agreement -> dividends_terms` (paso 2, core) | NO SE ENLAZA | | ALCANZABLE (4 saltos), NO es la cadena propia de la madre |

Las razones completas, el volcado de las 8 fichas y la vara de la tanda
(TAREA 4, alcance de la adjudicacion 6.5 del acta 84) estan en
`docs/loop/REPORTE.md` de la vuelta 87 y en
`docs/loop/SALIDA_V87_TAREA4_VARA_TRAMO12.txt`. Aristas escritas y
verificadas en las DOS vistas
(`scripts/loop/vuelta87_tramo12_escribir.py`,
`scripts/loop/vuelta87_medir_tramo12.py` >
`docs/loop/SALIDA_V87_TRAMO12_ESCRIBIR.txt`): 2 ARISTAS ESCRITAS, 0
ESCALERA ROTA, 0 INCONSISTENTES. Aristas tras la escritura: 8.996
`nodos_siguientes` / 8.975 `nodos_previos` / 17.971 suma / 9.619 union
(`docs/loop/_v87_conteo_tras_tramo12.txt`), dos mas que las 8.994 / 8.973 /
17.967 / 9.617 de la apertura de esta vuelta, en las cuatro cifras, como
corresponde a dos aristas anadidas en las dos vistas.

**LA CIFRA FINAL DE LA OPERACION**, leida de `docs/plan/OP_E_01_DECIDIDAS.
jsonl` (nunca de la suma de reportes viejos): **220 unidades leidas en
total, 99 ESCRITA, 121 NO SE ENLAZA**, reparto por tramo `{3: 30, 4: 30, 5:
23, 6: 10, 7: 3, 8: 30, 9: 30, 10: 30, 11: 30, 12: 4}`.

**LA GUARDA, corrida DESPUES del horneado de cierre**
(`scripts/loop/vuelta83_guarda_decididas.py --bolsa docs/plan/PASO_NODO_
CALIBRADO_FILTRADO_V87.jsonl`, `docs/loop/SALIDA_V87_GUARDA_CIERRE.txt`):
**VERDE**, con el mensaje **TODA LA BOLSA ESTA DECIDIDA** sobre las 121
unidades de la bolsa filtrada V87. Ninguna unidad queda sin decision:
`OP-E-01` cierra sin bolsa a medias, y la recalibracion de esta vuelta no
abrio unidades nuevas respecto de la vuelta anterior (0 de 121, medido en
`docs/loop/SALIDA_V87_TRAMO12_FILTRO_P91_GUARDA_CADENA.txt`).

**CORRECCION DECLARADA (28 ago 2026, vuelta 88) **[CORRECCION DECLARADA DE FECHA (vuelta 98, TAREA 1): la fecha "28 ago 2026" de este marcador estaba TECLEADA y es FALSA. El texto viejo se queda entero y sin borrar una letra (EJECUTOR.md 8). LA FECHA REAL, LEIDA DE GIT EN LA VUELTA 98 con `git log --all --format=%ad^%h^%s --date=short, quedandose con los commits cuyo asunto empieza por "VUELTA 88"`, es 2026-08-27 (commits e7b0d21f, dfe9650a, e6402ea2, 970713d6), o sea 27 ago 2026. Techo del reloj del repo, medido con `git log --all --format=%ad --date=short`: 2026-08-27.]**: la celda de la fila 117 no se
borra, se corrige.** El auditor (acta de la vuelta 87, seccion 2.1 y
adjudicacion 6.1) discrepo con la fila 117 de la tabla de arriba, que dice **"ES
la cadena propia de la madre"** y a la vez **SE ESCRIBE**, sin una linea que
explique por que la condicion de muerte de la adjudicacion 6.1 del acta 83 no
aplica ahi. Es la caida que la adjudicacion 6.8 del acta 87 nombra: "contestar
SI y escribir SE ESCRIBE sin una linea mas no es una lectura, es un
formulario."

**LA RELECTURA CONJUNTA, con instrumento propio**
(`scripts/loop/vuelta88_tarea2_relectura_117.py`,
`docs/loop/SALIDA_V88_TAREA2_RELECTURA_117.txt`): las seis aristas del camino
`juran_rcca_metodo -> definicion_problema_moms_2 -> analisis_sintomas ->
formulacion_teorias_causa -> prueba_teorias_causa_raiz ->
evaluacion_alternativas_solucion -> diseno_implementacion_remedio` **estan
las seis, verificadas hoy en las dos vistas** (`nodos_siguientes` de cada
origen y `nodos_previos` de cada destino), los siete nodos **vivos**. Sobre
esto no hay hallazgo: el camino que el auditor trajo existe tal como lo
describio.

**LA LECTURA QUE CAMBIA es si ese camino ES la cadena propia de la madre.** La
fila de arriba dice que si. **NO LO ES, y la razon es la que faltaba**: la
regla de banco 9.6.1 (CAVEAT MEDIDO), citada por su letra y no parafraseada,
dice que la cadena cuenta como cableado establecido **"si los hijos estan
encadenados en el orden que la madre enumera"**, y que **"si estan sueltos
alrededor de la madre, se cuentan los radios"** (o sea, es alcanzabilidad, no
cadena). De los cinco nodos del camino que preceden al hijo, CUATRO son pasos
literales de la madre en su propio orden (`definicion_problema_moms_2` su paso
1; `analisis_sintomas`, `formulacion_teorias_causa` y
`prueba_teorias_causa_raiz` los tres, su paso 2) pero **UNO no lo es**:
`evaluacion_alternativas_solucion` no aparece en ninguno de los cuatro pasos de
`juran_rcca_metodo` (medido leyendo su ficha completa, `pasos_accionables`).
Ese nodo esta **suelto alrededor de la madre** en el sentido literal de 9.6.1,
y por el propio texto de la regla un camino con un tramo suelto no es la
cadena que la madre enumera: es alcanzabilidad, y **"contra la alcanzabilidad
la arista sigue faltando"**, que es la otra mitad de la adjudicacion 6.1 del
acta 83 que la fila de arriba no cito.

**El precedente sostiene esta lectura y no la contradice.** El par 55 (acta
del auditor, discusion de la vuelta 84, `institucionalizar_breakthrough ->
metas_negocio_calidad`) sobrevivio como NO cadena propia por dos motivos
escritos juntos: la direccion iba al reves **Y** el camino pasaba "por dos
nodos de gobernanza que la madre no enumera". El segundo motivo, por si solo,
es exactamente el que aplica aqui: no hace falta que la direccion falle para
que un nodo suelto rompa la cadena. Los pares 66, 91 y 100 (los tres citados
por el auditor como cadena propia que si mata) tienen los dos rasgos
opuestos: **cero nodos sueltos** en su camino (66: dos nodos, los dos pasos de
la madre; 91: dos nodos, los dos pasos; 100: dos nodos, los dos pasos) y
avance forzoso hacia adelante. El 117 comparte con esos tres el avance hacia
adelante, pero comparte con el 55 el rasgo que de verdad decide segun 9.6.1: un
nodo que la madre no enumera en el medio del camino.

**LA DECISION: LA CLASE SE SOSTIENE. `SE ESCRIBE` queda**, ahora con la razon
completa: el camino no es la cadena propia de la madre (por el nodo suelto
`evaluacion_alternativas_solucion`), asi que es mera alcanzabilidad y **9.6**
dice que contra la alcanzabilidad la arista sigue faltando; y **9.6.2** ya
daba la senal de contenido a favor (el paso 3 de la madre nombra el titulo
entero del hijo, el hijo trae seis pasos propios que la madre no tiene, y la
madre conserva materia propia en sus pasos 1, 2 y 4). **La fila de la tabla de
arriba (117, columna "alcanzable") queda superada por esta correccion: donde
dice "ES la cadena propia de la madre" la lectura correcta es "NO es la cadena
propia de la madre (nodo suelto: `evaluacion_alternativas_solucion`)", igual
que las filas 119 y 120.** La cifra final de la operacion (220 / 99 / 121,
arriba) NO CAMBIA: la arista ya estaba escrita con la clase correcta, lo que
cambia es la razon que la sostiene.

**CORRECCION DECLARADA (29 ago 2026, vuelta 89) **[CORRECCION DECLARADA DE FECHA (vuelta 98, TAREA 1): la fecha "29 ago 2026" de este marcador estaba TECLEADA y es FALSA. El texto viejo se queda entero y sin borrar una letra (EJECUTOR.md 8). LA FECHA REAL, LEIDA DE GIT EN LA VUELTA 98 con `git log --all --format=%ad^%h^%s --date=short, quedandose con los commits cuyo asunto empieza por "VUELTA 89"`, es 2026-08-27 (commits 71b5e17d, 5ae40940, 43bafe47, 7f546873), o sea 27 ago 2026. Techo del reloj del repo, medido con `git log --all --format=%ad --date=short`: 2026-08-27.]**: la correccion del 28 ago de
arriba queda SUPERADA, y no se borra.** El auditor corrio la relectura
conjunta del par 117 (acta de la vuelta 88, secciones 2.2 a 2.4 y
adjudicacion 5.1) y la resolvio CONTRA el ejecutor: la clase pasa de `SE
ESCRIBE` a **`NO SE ENLAZA`**, y la arista `juran_rcca_metodo ->
diseno_implementacion_remedio` se revierte de las dos vistas.

**(i) EL MOTIVO, citado entero y no resumido (acta de la vuelta 88, seccion
2.2):**

> El ejecutor contesta que el camino NO es la cadena propia de la madre, y
> por lo tanto la arista sobrevive. La adjudicacion del auditor es la
> contraria: SI es la cadena propia, y la clase es `NO SE ENLAZA`. El motivo
> no es que el auditor lea distinto: es que la regla adjudicada tiene DOS
> condiciones y el ejecutor le anade una TERCERA que no esta escrita.
>
> La regla, citada por su numero y no parafraseada (adjudicacion 6.1 del
> acta 83, la que esta campaña lleva cinco pares citando): "un camino
> ALCANZABLE solo cuenta como cableado establecido (o sea, solo mata la
> arista) cuando es LA CADENA PROPIA DE LA MADRE: arranca de lo que el paso
> nombra o de un hijo de un paso suyo, y avanza en el orden que la madre o
> los propios nodos declaran. Un camino que no sale del paso no es cadena:
> es alcanzabilidad."
>
> Las dos condiciones, medidas contra el camino del 117: (1) arranca de lo
> que el paso nombra o de un hijo de un paso suyo: SI, arranca en
> `definicion_problema_moms_2`, hijo directo de la madre y nodo de su paso
> 1. (2) avanza en el orden que la madre o los propios nodos declaran: SI,
> paso 1, luego los TRES nodos del paso 2 en el orden literal en que el paso
> 2 los enumera, y desemboca en el nodo del paso 3. El unico tramo que la
> madre no enumera (`prueba_teorias_causa_raiz -> evaluacion_alternativas_solucion
> -> diseno_implementacion_remedio`) lo declaran los propios nodos, que es
> la otra mitad literal de la condicion. Las dos se cumplen. No hay una
> tercera condicion en la regla.
>
> De donde sale la tercera condicion del ejecutor, y por que no se sostiene.
> El ejecutor la toma del banco 9.6.1, CAVEAT MEDIDO: "Si los hijos estan
> encadenados en el orden que la madre enumera, la cadena cuenta como
> cableado establecido. Si estan sueltos alrededor de la madre, se cuentan
> los radios." El sujeto de esa frase son LOS HIJOS DE LA MADRE, y lo que
> contrapone es una familia cableada en cadena contra una familia cableada
> en radios: es una regla de como medir la silueta de una familia, no una
> regla sobre los nodos por los que un camino pasa. `evaluacion_alternativas_solucion`
> no es un hijo de esta madre, ni encadenado ni suelto: es un nodo ajeno a
> la familia. Llamarlo "suelto alrededor de la madre" aplica la frase a un
> sujeto que la frase no nombra. El ejemplar que el propio CAVEAT trae
> (`proceso_diseno_modelo_negocio_5_fases`, cinco fases encadenadas) no
> tiene ni un nodo intermedio ajeno: no decide este caso en ninguna
> direccion.
>
> Y la prueba de proposito, que es la que el banco 9.6 pregunta de verdad:
> el contenido queda "huerfano de camino", o sea "un nodo entero que el no
> va a encontrar nunca, porque nada lo lleva alli"? No queda huerfano. El
> lector que llega al paso 1 y camina hacia adelante por la escalera de la
> propia madre desemboca en el hijo. Y el nodo que la madre no enumera no
> es un desvio: es el tejido de un hueco que la madre se salta ella misma,
> porque su paso 2 termina en "identificar la causa raiz" y su paso 3
> empieza en "disenar e implementar el remedio", y elegir entre alternativas
> es lo que va en medio. Contrastelo con el par 47 (adjudicacion 6.2 del
> acta 83), donde el camino de seis saltos atravesaba `plan_a_b_c_soft_landing`,
> `relaciones_con_clientes`, `flujos_de_ingresos`, `estructura_de_costos` y
> `lectura_balance_general`: ahi si el camino se iba del tema, y por eso no
> era la cadena de la madre.

El auditor tambien reconocio, sin matiz, que la conducta del ejecutor fue la
correcta: trajo una regla escrita, midio bien los hechos y decidio, que es
lo que la relectura conjunta pide; lo que falla es la regla que le anadio,
no el metodo.

**(ii) EL PRECEDENTE DEL PAR 91 CITADO ARRIBA ("91: dos nodos, los dos
pasos") ES INCORRECTO, medido con BFS (acta de la vuelta 88, seccion 2.3):
el camino de `diseno_controles_proceso_mejorado` a
`auditorias_calidad_proceso` tiene TRES intermedios, no dos**
(`validacion_sistema_medicion`, el paso 5 de la madre;
`autocontrol_y_controlabilidad`, el paso 6 de la madre; y
`autocontrol_planificacion_servicio`, que el acta 85 no nombra y que es
plausiblemente una segunda casa del paso 6 en el dominio de servicio, par
395). El par 91 **no corrobora ninguna de las dos lecturas**: ni sostenia al
ejecutor como el texto de arriba pretendia, ni sostiene al auditor. La
adjudicacion del 117 no se apoya en el 91: se apoya en las dos condiciones
de la 6.1 del acta 83 y en la prueba de proposito del banco 9.6, citadas
enteras en (i).

**LA CIFRA FINAL DE LA OPERACION QUEDA REESCRITA: donde arriba dice "220
unidades leidas en total, 99 ESCRITA, 121 NO SE ENLAZA" la cifra vigente hoy
es 220 unidades leidas en total, 98 ESCRITA, 122 NO SE ENLAZA**, rehorneada
con `scripts/loop/vuelta85_hornear_decididas.py`
(`docs/loop/SALIDA_V89_TAREA2_HORNEAR_OPE01.txt`) y verificada con
`scripts/loop/vuelta83_guarda_decididas.py --bolsa docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V87.jsonl`
(`docs/loop/SALIDA_V89_TAREA2_GUARDA_DECIDIDAS.txt`): VERDE, TODA LA BOLSA
ESTA DECIDIDA, con el indice 117 hoy `NO SE ENLAZA` (tramo 12). La fila 117
de la tabla de arriba (columna "decision") queda tambien superada: donde
dice `SE ESCRIBE` la decision vigente es `NO SE ENLAZA`.

---

## LOS SUELTOS DE RACIMOS, y los racimos con miembro ajeno

**`OP-E-02` junta dos cosas que se parecen y no son iguales.**

### 1. LOS SUELTOS

**Un SUELTO es un miembro que un racimo censo pero que ninguna A conecta con el
resto.** El ejemplar medido es **`comprender_alineacion_etica_ia`**, el suelto del
racimo de la supervision de la IA, cuya particion provisional es **5 mas 4 mas 1**.

**LA REGLA, adjudicada el 11 ago 2026, y son tres casos:**

| situacion | que se hace |
|---|---|
| el racimo **tiene centro** y el par del suelto con el centro **ya salio SANO** | **se ENLAZA** |
| el suelto **tiene par A** | **no es enlace: es FUSION**, y va a la fase 03 |
| el racimo **NO tiene centro** | **no se inventa: va a su MESA** |

> **EL EJEMPLAR MEDIDO CAE EN EL TERCER SUPUESTO.**
> `comprender_alineacion_etica_ia` es el suelto de un racimo **partido en dos
> bloques**, o sea **sin centro**: va a mesa y no se enlaza.

> **Por que la regla tiene que nombrar el caso sin centro: es justo donde la
> tentacion es inventar uno.** Un racimo partido en dos no tiene centro por
> definicion, y **colgar el suelto de cualquiera de los dos bloques seria adjudicar
> la particion de contrabando.**

### 2. LOS RACIMOS CON MIEMBRO DE OTRO DOMINIO

**Tres ya hallados, y son la muestra, no el censo:**

| racimo | el miembro | su dominio real |
|---|---|---|
| el lienzo de propuesta de valor (`core`) | `desarrollo_value_proposition_usp` | **franquicias** |
| mapeo del flujo de valor (`quality`) | `value_stream_mapping_ambiental` | **environmental** |
| mapeo del flujo de valor (`quality`) | `analisis_flujo_de_valor` | **core** |

> **La regla para estos SI esta escrita**: o **la nomina se depura**, o **el racimo
> se declara TRANSVERSAL de forma explicita**. **Lo que no puede quedar es un
> racimo que PARECE de un dominio y no lo es.**

**Y el control mecanico que los encuentra a todos de una vez ya esta adoptado**:
revisar **toda** nomina por el DOMINIO de sus miembros, cruzando
`RACIMOS_MIEMBROS.jsonl` contra el grafo.

> **CORRECCION DECLARADA (26 ago 2026, vuelta 76, adjudicada por el auditor,
> acta de la vuelta 75 seccion 4.1).** *"El control los encuentra todos de una
> vez"* es FALSA y esta medida como falsa: el control cubre los racimos
> **censados en `RACIMOS_MIEMBROS.jsonl`** (32 racimos, reconstruidos por el
> commit `d4d2652f` de las razones de `FRANJA_VEREDICTOS.jsonl`), o sea los
> racimos que el CRIBADO declaro. Un racimo del INFORME que nunca paso por
> franja, como *el lienzo de propuesta de valor* (seccion 14 del informe,
> remedido a SIETE miembros por cierre transitivo), **no esta en ese universo
> por construccion, no porque el control lo perdiera.** Las dos fuentes son
> distintas por construccion. Los tres ejemplares de la tabla de arriba ya
> estan resueltos: `value_stream_mapping_ambiental` y `analisis_flujo_de_valor`
> por la segunda salida (su racimo *Mapeo del flujo de valor* tiene
> `dominio_censado` literal `quality + environmental + nucleo`, que ES la
> declaracion transversal explicita); `desarrollo_value_proposition_usp` por
> la primera salida, la nomina se depura (informe seccion 33.2: *"CAE, y ni
> siquiera es del dominio... CERO SOLAPE"*, y 33.3 lo llama *"defecto de
> NOMINA, no de lectura"*). El texto viejo de arriba no se toca.

---

## ~~LAS SIETE C~~ LAS CINCO C TAMBIEN SON DE ESTA FASE

**Los pares de clase C, sanos con figura, se arreglan con DOS ARISTAS**, no con
una fusion. Puestos **201, ~~203~~, 215, ~~246~~, ~~360~~, 494, 1077 y 1240**.

> **Es el ENLACE MUTUO del banco 9.22**: cada nodo expande una linea distinta del
> otro, ninguno es la madre, **y fundirlos borraria los dos procedimientos.**

> **CORRECCION DECLARADA (20 ago 2026, vuelta 57, TAREA 1.2, por el carril del banco `9.10`). ESTA LISTA ES HERMANA DE LA DE `03_FUSIONES.md` Y ESTABA ENVEJECIDA IGUAL.** Salen el **`203`** (volteado por la vuelta 56, relectura del filo del acto 15 del tramo 3 de `OP-U-01`), el **`246`** y el **`360`** (sus actos se fundieron en las vueltas 52 y 53 y sus dos lados pasaron a resolver al mismo nodo vivo). Entra el **`494`**, que lo es desde el 15 ago 2026 por el commit `7cec9ecc` y que esta lista no recogio nunca. **La cuenta vigente, recomputada hoy del archivo: 201, 215, 494, 1077 y 1240, CINCO**, y por eso el titulo de la seccion tambien se tacha. **El texto de la regla no cambia**: siguen siendo enlace mutuo del banco `9.22` y siguen sin fundirse. Medido HOY sobre `../INTRA_DOMINIO_VEREDICTOS.jsonl` con `python scripts/loop/vuelta57_puestos_volteados.py --base c0e8041a --tambien 203,246,360` y con `python scripts/recomputar_marcador.py 3388`: [`../loop/SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt`](../loop/SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt) da estas celdas ROJAS, [`../loop/SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt`](../loop/SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt) las da VERDES, y [`../loop/SALIDA_V57_MARCADOR_APERTURA.txt`](../loop/SALIDA_V57_MARCADOR_APERTURA.txt) es la corrida del marcador de la que salen el 5 y el 72.

---

## POR QUE ESTA FASE SE PUEDE ADELANTAR, y su unica atadura

**No mueve ids**, asi que no depende de la FASE 0 para ejecutarse.

> **Pero SI depende de `OP-C-04` para verificarse.** Una arista nueva mal puesta
> **puede crear una auto-arista via alias**, que es justo lo que la guarda literal
> no ve. **Sin la guarda que resuelve, esta fase puede meter en silencio lo que
> `OP-S-07` acaba de sacar.**

---

# LA COSECHA DE RAZONES DE LAS D . **12 ago 2026**

**Salio de tirar del hilo del control de la muestra pineada.** Aquel encontro, **sin
buscarlo**, que **nueve de las veintitres D que sostienen su clase nombran una
jerarquia o una arista que falta**. Si eso pasa en el 39% de veinticuatro, **lo mismo
esta escrito en cientos de razones que nadie ha vuelto a leer.**

**Instrumento: `scripts/plan/barrido_razones_d.py`.** No interpreta los nodos:
**lee lo que el veredicto ya dijo.**

## LA COSECHA

| | |
|---|---:|
| D en el archivo al corte 2.117 | 1.621 |
| **D cuya razon nombra jerarquia o arista que falta** | **397** |
| sobre el total de D | **24,5%** |
| ya cubiertos | 104 |
| **NUEVOS** | **293** |
| de ellos, **con la direccion escrita en su propia razon** | **192** |
| levantados solo por *continua por la vara*, sin direccion | 101 |

**POR QUE ESTABAN CUBIERTOS LOS 104**: **92 ya tienen arista en el grafo** y **12
estaban en la bolsa de la fase 04**.

## EL DATO QUE MAS SORPRENDE

> **DE LOS 397 LEVANTADOS, SOLO DOCE ESTABAN EN LA BOLSA DE 477.** **Los dos
> instrumentos se solapan en un 3%.**

**El barrido paso contra nodo mide VOCABULARIO. La razon de un veredicto es una
LECTURA.** Y encuentran **cosas casi disjuntas**.

> **LO QUE ESO SIGNIFICA PARA LA FASE 04: tenia medida solo UNA de sus dos mitades.**
> La bolsa de 477 con su 69,6% de acierto **no era el universo de las aristas que
> faltan: era el universo de las que un instrumento de parecido puede ver.**

**Y LOS 92 QUE YA TENIAN ARISTA SON EL CONTROL DEL INSTRUMENTO**: son razones que
nombran la jerarquia sobre pares que **el grafo ya cablea**. **La figura no se la esta
inventando el barrido.**

## POR QUE ESTOS CANDIDATOS SON DE MEJOR CLASE

| | la bolsa de 477 | **la cosecha de razones** |
|---|---|---|
| **que es la evidencia** | dos senales de parecido, titulo y contencion | **un veredicto: el par se leyo entero** |
| **acierto** | **69,6%**, banda de 55,2 a 80,9 | **por definicion, el lector ya dijo que la arista falta** |
| **la direccion** | hay que deducirla | **192 la traen escrita en la razon** |
| **el coste** | 477 lecturas para confirmarlos | **cero: ya estan leidos** |

> **NO HAY QUE LEER NADA PARA COBRAR ESTOS CIENTO NOVENTA Y DOS. HAY QUE ESCRIBIRLOS.**

## REPARTO POR DOMINIO DE LOS 192

| dominio | con direccion | levantados |
|---|---:|---:|
| `core` | **146** | 300 |
| `entrega` | 15 | 22 |
| `environmental` | 15 | 35 |
| `exportacion` | 12 | 36 |
| `franquicias` | 4 | 4 |
| `compras` | **0** | **0** |

> **En `compras` no levanto ninguno, y no es que no haya jerarquias: es que sus razones
> son mas cortas y no usan la formula de la vara.** **El instrumento mide como se
> escribio el veredicto, no como es el par**, y eso hay que decirlo antes de que
> alguien lea el cero como una propiedad del dominio.

## LAS DOS OPERACIONES

| | |
|---|---|
| **`OP-E-06`** | **los 192 con direccion**. Se escriben, no se leen |
| **`OP-E-07`** | **los 101 sin direccion**. **No es una lectura de par: es una lectura de FRASE**, porque la clase ya esta decidida y solo falta saber quien es la madre |

> **Se separan a proposito: mezclarlas haria que ciento noventa y dos aristas seguras
> esperaran a ciento un lecturas de frase.**

---

## REGISTRO DE LA VUELTA 89 (ACTA DEL AUDITOR), TAREA 1 DE LA VUELTA 90

**Por que se registra aqui y no se deja solo en `ACTA_AUDITOR.md`:** la decision
del fundador del 29 ago 2026 (`docs/loop/paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md`)
manda TAREA 1, los registros, antes de tocar la bolsa de `OP-E-06`. Todo lo que
sigue es CITA del acta, no medicion nueva: cada linea trae su numero de linea en
`docs/loop/ACTA_AUDITOR.md`.

### Las dos caidas de reporte de la vuelta 89 (acta 89, seccion 3, lineas 30165 a 30244)

1. **El truncado a 200 caracteres, publicado como "verificado" con dos ejemplos
   que lo desmienten** (seccion 3.1, lineas 30167 a 30208). El reporte de la
   vuelta 89 publico que `len(frase) == 200` estaba "verificado" en siete
   puestos de ejemplo de `docs/plan/COSECHA_RAZONES_D.jsonl`, y dos de los
   siete (**2023** y **2082**) median **305** y **263** caracteres, no 200.
   Medicion del auditor de la cifra buena: **397 filas, 270 con `len(frase)`
   exactamente 200, 23 por encima de 200, maximo 335.**
2. **El caso rojo de la TAREA 3.d que no puede fallar** (seccion 3.2, lineas
   30210 a 30244). En `scripts/loop/vuelta89_tarea3_rebase_ope06.py`, lineas
   504 a 531, `veredicto_2` es una constante literal (`"ENTRA"`) y el `assert`
   la compara consigo misma: no puede salir en rojo nunca. El reporte lo
   publico como prueba de que el criterio se comporta.

### La caida del auditor: la escalada automatica no encargada (acta 89, seccion 6 punto 1, lineas 30320 a 30332)

El acta de la vuelta 88 declaro la racha de reporte en DOS y no encargo la
extension del tallador que `EJECUTOR.md` regla 1 deja AUTOMATICAMENTE
ENCARGADA en ese caso (decision del fundador del 26 ago 2026). El encargo de
la vuelta 89 puso la regla en prosa pero no la operacion de codigo, y la
tercera caida (la de esta misma seccion, punto 2) llego donde el remedio no
estaba puesto. Es el motivo por el que la TAREA 3 de esta vuelta (90) es
BLOQUEANTE y va antes de tocar `OP-E-06`.

### Las siete adjudicaciones de la seccion 4 del acta 89 (lineas 30245 a 30284), cada una por su numero

- **4.1** (linea 30247): el puesto **530 ENTRA** en la bolsa de `OP-E-06`. Su
  frase cita la linea entera del paso 3 de la madre, y el criterio que deja
  dentro a los puestos 1169 y 1002 no puede dejarlo fuera.
- **4.2** (linea 30252): el puesto **932 SALE** de la bolsa de `OP-E-06`. Su
  propia frase nombra a cuatro hermanos de la madre y `mecanismo_resolucion_
  disputas` no es ninguno de los cuatro.
- **4.3** (linea 30258): el puesto **581 se queda fuera**, y la exclusion se
  declara con su motivo real: la letra de `OP-E-06` ("si una razon no lo dice,
  el par NO entra") manda, aunque las fichas del par muestren el patron
  canonico por contenido. Va a `PENDIENTES` como candidato de una pasada
  posterior (ver TAREA 2 de esta vuelta), junto con el **650**, que es la
  misma familia por la misma razon.
- **4.4** (linea 30263): el fichero `OP_E_06_REBASE_V89.jsonl` no se corrige
  ni se borra en la vuelta 89: la correccion es a fichero propio nuevo (V90),
  que es la TAREA 2 de esta vuelta.
- **4.5** (linea 30269): la TAREA 4 de la vuelta 89 (la via de `OP-C-05`,
  `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`) queda ratificada entera:
  el instrumento, sus tres modos y la linea base de **935 entradas que sobran
  en 711 nodos**.
- **4.6** (linea 30273): la reversion del par 117 y sus correcciones
  declaradas quedan ratificadas enteras. La cifra vigente de `OP-E-01` es
  **220 / 98 ESCRITA / 122 NO SE ENLAZA**.
- **4.7** (linea 30278): un caso rojo que no puede fallar no es un caso rojo,
  y cuando el criterio es una lectura humana escrita a mano se declara como
  tal en vez de fabricarle una prueba automatica. Es el precedente directo de
  la regla nueva de `EJECUTOR.md` ("EL CASO ROJO SE PRUEBA POR MUTACION").

---

## LA CIFRA DE `OP-E-06`, ENTERA, DE 192 A 113 (TAREA 2 de la vuelta 91, adjudicacion 4.5 del acta de la vuelta 90, `ACTA_AUDITOR.md` lineas 30830 a 30835)

**Por que se escribe aqui:** hoy el descenso vive repartido entre el addendum
de `OPERACIONES.jsonl`, el acta 88 y el acta 89 del auditor. La regla contra
el descarte silencioso que la propia `verificacion` de `OP-E-07` lleva escrita
("un descarte silencioso aqui seria un enlace perdido") pide una sola cadena
medida y citable. Cada eslabon trae su fuente; si alguno no se pudiera medir
hoy se declararia "a verificar" y se diria cual, pero los ocho de abajo estan
todos medidos en un fichero de salida existente.

| # | eslabon | cifra | fuente / comando |
|---:|---|---:|---|
| 1 | Los candidatos con direccion explicita en su propia razon, tallados de `docs/plan/COSECHA_RAZONES_D.jsonl` (397 filas, `nuevo=true` con senal distinta de `["continua por la vara"]`) | **192** | `scripts/loop/vuelta88_tarea5_rebase_ope06.py`, TAREA 5.a, `docs/loop/SALIDA_V88_TAREA5_REBASE_OPE06.txt` linea 8 |
| 2 | Frente 1 del dedupe: contra `PASO_NODO_CALIBRADO.jsonl` (468 filas hoy) | quita **0** | mismo instrumento, TAREA 5.b, salida citada linea 20 |
| 3 | Frente 2 del dedupe: contra 18 pares ya declarados en `aristas_nuevas` de otras operaciones de `OPERACIONES.jsonl` | quita **0** | mismo instrumento, TAREA 5.b, salida citada linea 22 |
| 4 | Frente 3 del dedupe: contra los 7 puestos de la cola de relectura post fusion (`00_INDICE.md` linea 409) | quita **0** | mismo instrumento, TAREA 5.b, salida citada linea 24 |
| 5 | Frente 4 del dedupe: contra pares con arista YA en el grafo de hoy, resolviendo por alias | quita **16** | mismo instrumento, TAREA 5.b, salida citada linea 26. Remanente tras los cuatro frentes: 192 menos 16 igual a **176** |
| 6 | Filtro de direccion sobre el remanente (frase con alguna palabra de direccion, lista CRUDA de la vuelta 87) | **129** con direccion (**47** sin, descartados y nombrados uno a uno) | mismo instrumento, TAREA 5.c, salida citada lineas 39 a 41. Escrito a `docs/plan/OP_E_06_REBASE_V88.jsonl`, **129 filas** (`wc -l` confirmado en esta vuelta) |
| 7 | Re-base V89: las 129 frases de V88 releidas ENTERAS con el criterio nuevo ("la frase dice quien desarrolla a quien", no la lista de palabras derogada), 12 `NO_ENTRA` nombradas una a una | **117** | `scripts/loop/vuelta89_tarea3_rebase_ope06.py`, TAREA 3.a/3.b, `docs/loop/SALIDA_V89_TAREA3_REBASE_OPE06.txt` lineas 22 a 60 (cifras en lineas 60 y 61). Escrito a `docs/plan/OP_E_06_REBASE_V89.jsonl`, **117 filas** (`wc -l` confirmado en esta vuelta) |
| 8 | LA REVERSION DEL 117 (fila de `OP-E-01`, NO un conteo de la bolsa: `juran_rcca_metodo -> diseno_implementacion_remedio`, la tercera condicion que el ejecutor le habia anadido al banco 9.6.1 no esta escrita en ninguna regla). Era el bloqueo pendiente que impedia abrir `OP-E-06` en la vuelta 89 (`ACTA_AUDITOR.md` linea 29741, adjudicacion 5.8 del acta 88) | eslabon de **bloqueo, no de resta**: se ejecuta en la vuelta 89 y libera la apertura de `OP-E-06` para la vuelta 90 | `ACTA_AUDITOR.md` lineas 29670 a 29679 (adjudicacion 5.1 del acta 88) y linea 30273 (adjudicacion 4.6 del acta 89, ratificada) |
| 9 | Adjudicaciones 4.1 y 4.2 del acta 89 (`ACTA_AUDITOR.md` lineas 30247 y 30252) sobre la bolsa de 117 de V89: puesto **530 ENTRA**, puesto **932 SALE** | **117** (conjunto distinto, misma cuenta: +1 -1) | `scripts/loop/vuelta90_tarea2_rebase_ope06.py`, verificado por el auditor en la vuelta 90 (`ACTA_AUDITOR.md` lineas 30565 a 30572: "ENTRA solo el 530... SALE solo el 932... conjuntos distintos: SI"). Escrito a `docs/plan/OP_E_06_REBASE_V90.jsonl`, **117 filas** (`wc -l` confirmado en esta vuelta) |
| 10 | Los 3 excluidos por el banco 9.22 (2082, 2084, 2112: su razon cita literalmente "banco 9.22" con la formula "CONTINUA en los dos sentidos") | quita **3** | `scripts/loop/vuelta90_tarea4_direccion_ope06.py`, `EXCLUIDOS_MUTUO_922`, verificado contra la razon real en tiempo de ejecucion. Ver correccion aditiva sobre la etiqueta en `docs/PENDIENTES.md`, TAREA 1 de esta vuelta |
| 11 | Los 114 con direccion madre/hijo leida de la razon completa | **114** | `scripts/loop/vuelta90_tarea4_direccion_ope06.py`, escrito a `docs/plan/OP_E_06_DIRECCION_V90.jsonl`, **114 filas**. 117 menos 3 igual a 114 |
| 12 | La escritura de las aristas: `ESCRITA` + `YA_ESTABA` (puesto 2023, resuelve a la misma arista del 2015) + `ESCALERA_ROTA` | **113 ESCRITA + 1 YA_ESTABA + 0 ESCALERA_ROTA = 114** | `scripts/loop/vuelta90_tarea4_escribir_ope06.py`, `docs/loop/SALIDA_V90_TAREA4_ESCRITURA.txt`, cruzado arista por arista contra el diff de la union del grafo por el auditor (`ACTA_AUDITOR.md` lineas 30516 a 30531, seccion 1.7): "CALZAN EXACTO, conjunto contra conjunto" |

**LA ARITMETICA COMPLETA, eslabon por eslabon:** 192 menos 16 (frente 4 del
dedupe, los otros tres frentes en 0) igual a 176; 176 filtradas por direccion
dan 129 (bolsa V88) y descartan 47, nombradas todas; las 129 releidas ENTERAS
con el criterio nuevo dan 117 (bolsa V89) y descartan 12, nombradas todas; la
reversion del 117 de `OP-E-01` (un bloqueo de calendario, no una resta de la
bolsa) libera la apertura; las adjudicaciones 4.1 y 4.2 del acta 89 mueven un
puesto adentro y uno afuera sobre esos mismos 117, dando la bolsa V90 (117,
conjunto distinto); los 3 del banco 9.22 salen por invocar el arreglo de dos
aristas y no el de la escalera, dejando 114 con direccion; y la escritura
sobre esos 114 da **113 ESCRITA, 1 YA_ESTABA y 0 ESCALERA_ROTA**, la cifra
vigente de `OP-E-06`.

> **192 -> (-16 dedupe) -> 176 -> (-47 sin direccion) -> 129 -> (-12 releidas
> sin desarrollo) -> 117 -> (bloqueo de la reversion del 117 de `OP-E-01`,
> liberado) -> 117 (+1/-1, adjudicaciones 4.1/4.2) -> (-3 banco 9.22) -> 114
> -> 113 ESCRITA + 1 YA_ESTABA + 0 ESCALERA_ROTA.**

---

## LA CIFRA DE `OP-E-07`, ENTERA, DE 101 A 87 (TAREA 4 de la vuelta 92, por la misma regla contra el descarte silencioso que la TAREA 2 de la vuelta 91 aplico a `OP-E-06`)

**ACTUALIZADA EN LA VUELTA 93, DE 87 A 86 (ver filas 10 y 11 y el segundo
bloque citado al final): la relectura conjunta del puesto 1009 (bloqueante,
`docs/loop/PROMPT_SIGUIENTE.md` TAREA 2 de la vuelta 93, y `docs/loop/
ACTA_AUDITOR.md` acta de la vuelta 92, seccion 4) concluyo que la razon del
1009 tampoco nombra cual nodo es la madre y el par SALE por la misma
`verificacion` de `OP-E-07`. NADA de lo que sigue en esta seccion se borra:
la cifra de 87 fue correcta hasta la vuelta 93.**

**Por que se escribe aqui:** la misma razon que la seccion de arriba. La
cifra de `OP-E-07` vive repartida entre el addendum de `OPERACIONES.jsonl`
(reescrito en la TAREA 3.d de esta vuelta, y de nuevo en la vuelta 93) y las
actas 91, 92 y 93; la `verificacion` de `OP-E-07` pide la misma cadena unica
y citable. Cada eslabon trae su fuente; el unico nuevo de esta vuelta (el
descenso de 88 a 87) se mide con el guarda de la TAREA 2, no a mano.

| # | eslabon | cifra | fuente / comando |
|---:|---|---:|---|
| 1 | Los candidatos SIN direccion en su propia frase cosechada, tallados de `docs/plan/COSECHA_RAZONES_D.jsonl` (397 filas, `nuevo=true` con `senales == ["continua por la vara"]`) | **101** | `docs/loop/SALIDA_V91_TAREA4_REBASE_OPE07.txt` lineas 5 a 6, reparto por dominio **core 74, environmental 12, exportacion 11, entrega 4** |
| 2 | Frentes 1, 2 y 3 del dedupe (contra el calibrado, contra `aristas_nuevas` de otras operaciones, contra la cola de relectura post fusion) | quita **0** los tres | mismo fichero, lineas 11, 13 y 15 |
| 3 | Frente 4 del dedupe: contra pares con arista YA en el grafo de hoy, resolviendo por alias | quita **13**, nombrados uno a uno (875, 884, 990, 1000, 1001, 1022, 1139, 1194, 1231, 1276, 1339, 1474, 1855) | mismo fichero, lineas 17 a 30. Remanente: 101 menos 13 igual a **88** |
| 4 | La bolsa re-basada, escrita | **88** | `docs/loop/SALIDA_V91_TAREA4_REBASE_OPE07.txt` linea 36, escrito a `docs/plan/OP_E_07_REBASE_V91.jsonl`, **88 filas** (`wc -l` confirmado en esta vuelta) |
| 5 | La direccion de cada par leida de la razon COMPLETA de `INTRA_DOMINIO_VEREDICTOS.jsonl` (80 por criterio automatico, 8 a mano con cita textual donde la formula no usa "trae") | **88 con direccion**, 0 excluidos por banco 9.22, 0 sin direccion resoluble | `docs/loop/SALIDA_V91_TAREA4_DIRECCION.txt` lineas 4 a 7 y 12, escrito a `docs/plan/OP_E_07_DIRECCION_V91.jsonl`, **88 filas** |
| 6 | LA CAIDA DE CLASE (vuelta 91, acta seccion 3.1): el puesto **1098** tiene una arista escrita que su propia razon PROHIBE (banco `9.6.2`, `docs/BANCO_DE_TEXTOS.md` linea 1737 y siguientes: no hay madre e hijo, linea compartida que ninguno expande, mismo perfil que el puesto **2.195** de la tabla de linea 1776 a 1782) | quita **1** | `docs/loop/ACTA_AUDITOR.md` lineas 31290 a 31352; `docs/PENDIENTES.md`, seccion "EL PUESTO 1098 DE `OP-E-07` TENIA UNA ARISTA QUE SU PROPIA RAZON PROHIBE" |
| 7 | El guarda de dos condiciones (TAREA 2 de esta vuelta) filtra la bolsa de direccion | **87 con direccion**, EXACTAMENTE el 1098 sale | `scripts/loop/vuelta92_tarea2_guarda_direccion.py --vara` (los dos casos obligatorios en verde) y `scripts/loop/vuelta92_tarea3a_filtrar_ope07.py`, escrito a `docs/plan/OP_E_07_DIRECCION_V92.jsonl`, **87 filas** (`wc -l` confirmado en esta vuelta) |
| 8 | La escritura de las aristas sobre los 88 de V91 (vuelta 91): `ESCRITA` + `YA_ESTABA` (puestos 1388 y 1946, resuelven por alias a una arista que otro puesto de la misma bolsa ya escribio) + `ESCALERA_ROTA` | **86 ESCRITA + 2 YA_ESTABA + 0 ESCALERA_ROTA = 88** | `docs/loop/SALIDA_V91_TAREA4_ESCRITURA.txt` lineas 94 a 96 |
| 9 | La retirada de la arista del 1098 (`scripts/loop/vuelta92_tarea3b_retirar_1098.py`), sobre los 86 `ESCRITA`: los 2 `YA_ESTABA` no se tocan porque el 1098 no era ninguno de los dos | **85 ESCRITA + 2 YA_ESTABA + 0 ESCALERA_ROTA = 87**, cifra vigente de `OP-E-07` hasta la vuelta 92 | diff de la union del grafo contra el cierre de la vuelta 91 (`0691d2257ddbbf8b26357dbd25f5b304bc984611`): EXACTAMENTE una borrada (`customer_validation_sell_phase -> prueba_solucion_con_cliente`) y cero nuevas, corrido en esta vuelta |
| 10 | VUELTA 93: la relectura conjunta del puesto **1009** (TAREA 2, bloqueante) concluye que su razon tampoco nombra la madre (formula de la clase D "trae un procedimiento que ESA FASE no tiene", igual en forma a la del 1098; ninguna linea nombrada con su paso; y la propia razon declara que "el bloque de traccion queda fuera" del solape, lo que hace fallar el test del banco `9.6.2`, `BANCO_DE_TEXTOS.md` lineas 1771 a 1774). El guarda reparado en las dos direcciones (`scripts/loop/vuelta93_tarea3_guarda_direccion.py --vara`, los tres casos obligatorios en verde) lo confirma sobre la bolsa vigente de 87 | quita **1** | `docs/loop/SALIDA_V93_TAREA2_RELECTURA_1009.txt`; `docs/loop/SALIDA_V93_TAREA3_VARA.txt`; `docs/loop/ACTA_AUDITOR.md` seccion 4, lineas 31977 a 32106 |
| 11 | El guarda filtra `OP_E_07_DIRECCION_V92.jsonl` (87 filas) y saca EXACTAMENTE el 1009 (`scripts/loop/vuelta93_tarea3a_filtrar_1009.py`); la arista se retira de `dataset/nodos/` (`scripts/loop/vuelta93_tarea3b_retirar_1009.py`, las dos vistas). El 1009 SI estaba `ESCRITA` (no es 1388 ni 1946), asi que la resta cae sobre el conteo de `ESCRITA` | **84 ESCRITA + 2 YA_ESTABA + 0 ESCALERA_ROTA = 86**, cifra vigente de `OP-E-07` desde la vuelta 93 hasta la vuelta 94 (CORRECCION DECLARADA, vuelta 95: la cifra vigente desde la vuelta 94 es 82 ESCRITA + 2 YA_ESTABA, ver fila 12) | `docs/loop/SALIDA_V93_TAREA3A_FILTRAR.txt`, escrito a `docs/plan/OP_E_07_DIRECCION_V93.jsonl` (86 filas, `wc -l` confirmado en esta vuelta); diff de la union del grafo contra el cierre de la vuelta 92 (`85a250bee2495f4a23d89a4cf51338a5bcd8397e`): EXACTAMENTE una borrada (`customer_discovery_phase2_problem_test -> fit_problema_solucion`) y cero nuevas, `docs/loop/SALIDA_V93_DIFF_UNION.txt` |

**LA ARITMETICA COMPLETA, eslabon por eslabon:** 101 menos 13 (frente 4 del
dedupe, los otros tres frentes en 0) igual a 88; las 88 leidas por su razon
completa dan 88 con direccion (0 excluidos por 9.22, 0 sin direccion); el
guarda de dos condiciones de la TAREA 2 saca el 1098 por el banco 9.6.2 y deja
87 con direccion; y la escritura, que ya habia dado 86 ESCRITA mas 2
YA_ESTABA sobre los 88, pierde exactamente la arista del 1098 (que SI estaba
`ESCRITA`, no `YA_ESTABA`) y queda en **85 ESCRITA, 2 YA_ESTABA y 0
ESCALERA_ROTA**, la cifra vigente de `OP-E-07` hasta la vuelta 92 (CORRECCION
DECLARADA, vuelta 94: la cifra vigente desde la vuelta 93 es **84 ESCRITA, 2
YA_ESTABA y 0 ESCALERA_ROTA**, ver la fila 11 de la tabla de arriba y "LA
CADENA ACTUALIZADA, VUELTA 93" mas abajo; este parrafo se quedo sin la
salvedad que si se anadio a la fila 9 y al primer bloque citado, y por eso lo
seguia diciendo en presente, `docs/loop/ACTA_AUDITOR.md` seccion 2.4, lineas
32489 a 32516, acta de la vuelta 93).

> **101 -> (-13 dedupe frente 4) -> 88 -> (0 excluidos 9.22, 0 sin direccion)
> -> 88 con direccion -> (-1 guarda de dos condiciones, banco 9.6.2, el 1098)
> -> 87 con direccion -> 85 ESCRITA + 2 YA_ESTABA (1388, 1946) + 0
> ESCALERA_ROTA.** Cifra vigente hasta la vuelta 92.

**LA CADENA ACTUALIZADA, VUELTA 93 (el 1009 sale, relectura conjunta,
`OP-E-07.verificacion`):**

> **101 -> (-13 dedupe frente 4) -> 88 -> (0 excluidos 9.22, 0 sin direccion)
> -> 88 con direccion -> (-1 guarda de dos condiciones, banco 9.6.2, el 1098)
> -> 87 con direccion -> (-1 guarda reparado, banco 9.6.2, el 1009, relectura
> conjunta de la vuelta 93) -> 86 con direccion -> 84 ESCRITA + 2 YA_ESTABA
> (1388, 1946) + 0 ESCALERA_ROTA.** Cifra vigente hasta la vuelta 94
> (CORRECCION DECLARADA, vuelta 94: dos relecturas conjuntas mas la mueven,
> ver fila 12 y la cadena de abajo).

| # | eslabon | cifra | fuente / comando |
|---:|---|---:|---|
| 12 | VUELTA 94: dos relecturas conjuntas (acta de la vuelta 93, secciones 5.1 y 5.2, discrepancias del ejecutor sobre direcciones fijadas en la vuelta 91) sobre los puestos **1281** (`get_visual -> pensamiento_visual_modelos_negocio`) y **1992** (`seleccion_de_metodo_de_pago -> metodos_pago_electronico_internacional`): ninguna de las dos razones nombra cual nodo es la madre (el 1281 solo trae "es un habito", INVERIFICABLE, y su unico "trae" esta negado dentro de "ningun habito general trae"; el 1992 no cita paso ni linea, a diferencia de sus hermanos 1991 y 1993, y su direccion salio de un comentario de `DIRECCION_MANUAL`, no de la razon). Por `OP-E-07.verificacion`, LOS DOS SALEN | quita **2** | `scripts/loop/vuelta94_tarea3_relectura_1281_1992.py`, `docs/loop/SALIDA_V94_TAREA3_RELECTURA.txt`; arista retirada con `scripts/loop/vuelta94_tarea3b_retirar_1281_1992.py` (las dos vistas, idempotencia probada); diff de la union del grafo contra el cierre de la vuelta 93 (`352b8529`): EXACTAMENTE dos borradas y cero nuevas, `docs/loop/SALIDA_V94_DIFF_UNION.txt` |

**LA CADENA ACTUALIZADA, VUELTA 94 (el 1281 y el 1992 salen, dos relecturas
conjuntas, `OP-E-07.verificacion`):**

> **101 -> (-13 dedupe frente 4) -> 88 -> (0 excluidos 9.22, 0 sin direccion)
> -> 88 con direccion -> (-1 guarda de dos condiciones, banco 9.6.2, el 1098)
> -> 87 con direccion -> (-1 guarda reparado, banco 9.6.2, el 1009, relectura
> conjunta de la vuelta 93) -> 86 con direccion -> (-2 relectura conjunta de
> la vuelta 94, el 1281 y el 1992) -> 84 con direccion -> 82 ESCRITA + 2
> YA_ESTABA (1388, 1946) + 0 ESCALERA_ROTA.** Cifra vigente desde la vuelta
> 94.
