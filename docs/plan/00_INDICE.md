# EL CONSOLIDADO EJECUTABLE DE LA PASADA UNICA

**Este documento no decide: recoge lo decidido.** Su meta es que el dia de la
pasada **no haya que volver a pensar nada**, solo aplicar.

> **MODO DE CIERRE VIGENTE. Aqui no se repara ni un nodo.** Todo lo que sigue es
> documentacion.

**Primera entrega, 11 ago 2026: fases 00, 01, 02 y 05.** Las fases 03, 04, 06, 07
y 08 estan anunciadas en el mapa y **todavia sin escribir**.

> **SEGUNDA PASADA, 11 ago 2026: las QUINCE ADJUDICACIONES DEL AUDITOR estan
> aplicadas**, cada una escrita dentro de su operacion en el campo `adjudicacion`.
>
> **TERCERA PASADA, el mismo dia: DIECIOCHO DE DIECINUEVE OPERACIONES ESTAN
> LISTAS.** `OP-S-07` volvio al plan con sus 27 ids **confirmados por dos
> instrumentos**, y `OP-S-08` paso de pregunta a **clasificacion cerrada**: 42
> accesos, **22 internos y 20 externos**, cada externo con su blindaje.
>
> **Y el plan tiene banco propio**: [`BANCO_DEL_PLAN.md`](BANCO_DEL_PLAN.md), con
> la regla de medicion que este ciclo obligo a escribir y el hallazgo de la firma
> posicional del injerto.

---

## LA REGLA MADRE, y como leerla en cada pagina

> **Nada entra al plan sin su EVIDENCIA citada**, con puesto, seccion o ficha.
> **Lo que no tiene evidencia se escribe como DECISION PENDIENTE, no como
> operacion.**

**Cada operacion vive en `OPERACIONES.jsonl`, una por linea**, y las paginas de
fase son su lectura en prosa. **La fuente de verdad es el JSONL**; si una pagina y
el JSONL discrepan, manda el JSONL.

| estado | que significa | quien lo desbloquea |
|---|---|---|
| **LISTA** | se puede ejecutar sin volver a decidir: nodos, superviviente, perdidas, orden y verificacion estan escritos | nadie: se ejecuta |
| **DECISION PENDIENTE** | falta un dato o falta una adjudicacion. **Lleva la pregunta exacta escrita en el campo `pregunta_pendiente`** | el auditor o el fundador |

---

## EL MARCADOR DE ESTA ENTREGA

| | primera pasada | tras las adjudicaciones | **hoy** |
|---|---:|---:|---:|
| operaciones escritas | 19 | 19 | **19** |
| **LISTAS** | 4 | 16 | **18** |
| **DECISION PENDIENTE** | 15 | 3 | **1** |
| preguntas abiertas | 15 | 3 | **1** |

**LAS DIECIOCHO LISTAS**: las tres decisiones de fuente (`OP-F-01` a `OP-F-03`),
**los seis destejidos enteros** (`OP-D-01` a `OP-D-06`) y **nueve del saneo**
(`OP-S-01` a `OP-S-09`).

**LA UNICA PENDIENTE, y es condicional por adjudicacion:**

| id | por que |
|---|---|
| **`OP-S-10`** | **CONDICIONAL**: `franquicias` entra al barrido de marco **si** la medicion muestra ley con alcance real. **La condicion esta escrita para evaluarse sin volver a preguntar**, con las cuatro familias medidas al lado |

> **Ocho de los quince congelados se liberan con las tres primeras.** No estan
> repartidos por el catalogo: **estan amontonados**, y por eso el orden de la
> pasada se decidio por congelados liberados y no por tamano.

---

## EL MAPA DE FASES, con sus dependencias

```
01_FUENTES  ──(OP-F-02 bloquea)──►  02_DESTEJIDOS (OP-D-04)
    │
    └──(OP-F-01 fija el estandar)──►  verificacion de TODO 02

05_SANEO
    OP-F-03 ──bloquea──► OP-D-01 y OP-D-06 (tres nodos de Hugos estan ahi)
    OP-S-08 YA NO BLOQUEA: el resolutor EXISTE y funciona
    OP-S-01 ──precede──► OP-S-09

03_FUSIONES   (sin escribir)  ◄── depende de 02: no se funde lo que aun no se desteje
04_ENLACES    (sin escribir)  ◄── independiente, se puede adelantar
06_MESAS      (sin escribir)  ◄── depende de 02: tres mesas no se sientan hasta la cirugia
07_ADUANA     (sin escribir)  ◄── independiente, es puerta permanente
08_VERIFICACION (sin escribir) ◄── envuelve a todas
```

**LAS TRES DEPENDENCIAS QUE NO SON DE ORDEN SINO DE SENTIDO**, y por eso se
escriben aqui arriba:

| dependencia | por que no es negociable |
|---|---|
| **fuente antes que destejido** | el destejido decide que bloques sobreviven, y **esos bloques son los que cargan la atribucion**. Al reves se escribe la fuente equivocada en el superviviente, **y el superviviente es el que se queda** |
| **destejido antes que fusion** | fundir antes de destejer **obliga a decidir el destino de material que la cirugia iba a quitar de todos modos** |
| ~~resolutor de alias antes que el alias~~ **CORREGIDA** | **El codigo SI lee `ids_alias`.** `resolverId` existe en `graph.ts` (linea 131), camina cadenas y lo invocan `etiquetaArbol` y `tituloDeNodo`. **La dependencia no era esa**: lo que falta es MEDIR que caminos del runtime pasan por el. `OP-S-08` es ahora esa medicion y **no bloquea a nadie** |

---

## LAS CIFRAS, cada una con su corte

**Por el banco 9.21 y su tercera mitad: ninguna cifra viaja sin su fecha, y
ninguna glosa viaja sin la cifra que interpreta.**

| cifra | valor | corte | estado |
|---|---:|---|---|
| actos del cierre transitivo | **13** | **puesto 1256**, recomputado sin cambios al **1277** | **PENDIENTE DE RECOMPUTO** |
| nodos dentro de esos actos | **38** | igual | **PENDIENTE DE RECOMPUTO** |
| costuras con gemelo | **17** | igual | **PENDIENTE DE RECOMPUTO** |
| nodos de las tres decisiones de fuente | **18** | campana de costuras | firme |
| congelados | **15**, de ellos **8 sobre tres nodos** | seccion 5304 del informe | firme |
| herramientas verificadas | **14**, de ellas **6 muertas** | 11 ago 2026 | firme |
| alias huerfanos | **77** | medido el 11 ago 2026, **cuadra con lo publicado** | firme |
| campos sucios | **1 + 1 + 4** | medido el 11 ago 2026, **cuadra con lo publicado** | firme |

> **EL RECOMPUTO PENDIENTE, y por que no se hace aqui.** El cierre transitivo esta
> vigente **al puesto 1256** y el cribado va por el **2117**. El banco 9.21 manda
> que **el barrido de confirmadas se repita UNA SOLA VEZ, al cierre del cribado**,
> no en cada checkpoint. **Por eso la cifra se escribe con su corte y se marca
> pendiente, en vez de recomputarse ahora.**
>
> **Lo que el recomputo puede cambiar**: cada A nueva puede unir dos componentes y
> volver un acto de dos en un acto de cinco. **Puede cambiar los tamanos y el
> numero de actos; no cambia el orden**, porque el orden se decide por congelados
> liberados y los congelados no los mueve una A nueva.

---

## DOS CIFRAS PUBLICADAS QUE NO RECONCILIAN

**Las dos salieron de medir con el mismo instrumento con el que se midio antes.
Ninguna se ha tocado.** Las dos estan escritas como pregunta en su operacion.

| donde | publicado | medido el 11 ago 2026 | operacion |
|---|---:|---:|---|
| Incoterms sin version | **12 nodos** | **3** lo citan en su texto; los otros 9 solo lo apuntan. **ADJUDICADO: la reparacion pasa de doce a tres** | **`OP-S-02`** |
| auto-aristas | **27 nodos** | **27. LA CIFRA ESTABA BIEN**, confirmada por dos instrumentos. **SE CONFIRMA, NO SE CORRIGE** | **`OP-S-07`** |
| self-alias | **7 nodos** | **0**. Esa mitad si encogio | `CORRECCIONES_A_APLICAR.md` |
| familias de ids de la DECISION 4 | sin nomina | **53 familias, 125 nodos vivos**, recomputadas con el criterio de la propia decision | **`OP-S-09`** |

> **LA LECCION, y es cara: una de las dos discrepancias no existia.** La de
> Incoterms era real y esta adjudicada. **La de las auto-aristas era un fallo de
> mi instrumento**, y el fallo viajo hasta una decision: **el auditor adjudico
> sobre mi cero y mato una operacion real.**
>
> **De ahi sale la regla P.1 del [banco del plan](BANCO_DEL_PLAN.md): en este
> grafo, todo conteo que toque ids pasa por el resolutor ANTES de contar.** Aplica
> a los instrumentos y a los dictados del auditor por igual.

---

## LA UNICA PREGUNTA QUE SIGUE ABIERTA

**Las otras catorce quedaron cerradas**: doce por las adjudicaciones del 11 ago
2026, y dos mas al cerrarse `OP-S-07` y `OP-S-08` el mismo dia.

| operacion | la pregunta |
|---|---|
| **`OP-S-10`** | **la medicion muestra ley con alcance real en `franquicias`?** Se cumple si los nodos de marco cablean una norma que OBLIGA a quien opera bajo esa jurisdiccion, y no solo un formato de referencia. **Las cuatro familias medidas son FDD (23), regla federal (9), registro estatal (9) e items del FDD (6): las cuatro son norma obligatoria.** Si eso es ley con alcance real, `franquicias` entra |

**Y UN DELTA DECLARADO, que no es pregunta pero conviene que se vea**: el auditor
dio **123 nodos** para las familias de ids y **mi recomputo da 125**, con las **53
familias clavadas**. La diferencia es de dos nodos y no de familias. **Se declara
en vez de forzarse.**

## LAS PAGINAS

| pagina | que contiene | estado |
|---|---|---|
| [`01_FUENTES.md`](01_FUENTES.md) | las tres decisiones de fuente, 18 nodos, y el precedente fuente-primero | escrita |
| [`02_DESTEJIDOS.md`](02_DESTEJIDOS.md) | los 13 actos del cierre transitivo, en orden por congelados liberados | escrita |
| [`05_SANEO.md`](05_SANEO.md) | marco-pais, vigencia, herramientas, campos sucios, auto-aristas e ids | escrita |
| [`CORRECCIONES_A_APLICAR.md`](CORRECCIONES_A_APLICAR.md) | una confirmacion y cuatro correcciones que viven FUERA de `docs/plan/`. **Las aplica la SESION A** | escrita |
| [`BANCO_DEL_PLAN.md`](BANCO_DEL_PLAN.md) | **P.1** la regla de medicion por el resolutor, y **P.2** la firma posicional del injerto | escrita |
| `03_FUSIONES.md` | fusiones de par y de familia, con superviviente y direccion | **sin escribir** |
| `04_ENLACES.md` | la arista que falta: 624 candidatos, proyeccion de 376 a 586 | **sin escribir** |
| `06_MESAS.md` | las mesas con su nomina y sus dependencias | **sin escribir** |
| `07_ADUANA.md` | la puerta de insercion semantica permanente y Gate 0 | **sin escribir** |
| `08_VERIFICACION.md` | como se comprueba cada fase y el criterio de HECHO | **sin escribir** |
