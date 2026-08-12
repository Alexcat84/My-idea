# FASE 04: LOS ENLACES

**La unica fase del plan que ANADE en vez de quitar.** No mueve ids, no funde, no
desteje: **pone la arista que falta.**

**Operaciones: `OP-E-01` y `OP-E-02`. LAS DOS LISTAS**, adjudicadas el 11 ago 2026.

---

## LA BOLSA DEL PASO CONTRA NODO

**Medida el 13 ago 2026 con una muestra pineada de 24** (pin en
`docs/PIN_SORTEO_PASO_NODO.txt`).

| | |
|---|---:|
| candidatos **sin arista** | **624** |
| leidos en la muestra | 24 |
| **JERARQUIA SANA** (arista que falta) | **19** |
| **MADRE QUE REPITE** (poda) | **0** |
| falso positivo | 5 |

> **CERO PODAS EN VEINTICUATRO LECTURAS.** La bolsa **no es una mezcla de dos
> clases de arreglo: es UNA, y es la barata.** No hay que triar entre enlazar y
> podar: hay que **enlazar**.

**PROYECCION, declarada como proyeccion**: **489** jerarquias sanas, con intervalo
de Wilson al 95% **entre 376 y 586**.

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

| | |
|---|---:|
| **JERARQUIA SANA**, la arista que falta | **32 de 46, 69,6%** |
| **MADRE QUE REPITE** | **7 de 46, 15,2%** |
| **FALSO POSITIVO** | **7 de 46, 15,2%** |

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

**Va a `OP-E-03`**, operacion nueva de esta fase.

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
