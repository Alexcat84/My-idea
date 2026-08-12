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

---

## LAS SIETE C TAMBIEN SON DE ESTA FASE

**Los pares de clase C, sanos con figura, se arreglan con DOS ARISTAS**, no con
una fusion. Puestos **201, 203, 215, 246, 360, 1077 y 1240**.

> **Es el ENLACE MUTUO del banco 9.22**: cada nodo expande una linea distinta del
> otro, ninguno es la madre, **y fundirlos borraria los dos procedimientos.**

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
