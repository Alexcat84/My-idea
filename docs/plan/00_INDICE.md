# EL CONSOLIDADO EJECUTABLE DE LA PASADA UNICA

**Este documento no decide: recoge lo decidido.** Su meta es que el dia de la
pasada **no haya que volver a pensar nada**, solo aplicar.

> **MODO DE CIERRE VIGENTE. Aqui no se repara ni un nodo.** Todo lo que sigue es
> documentacion.

**EL PLAN ESTA COMPLETO: ONCE FASES, 45 OPERACIONES, 39 LISTAS. LAS SEIS PENDIENTES SON LAS CINCO MESAS Y UN RECOMPUTO CON FECHA.**

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
>
> **CUARTA PASADA, el mismo dia: LA FASE 04 DEJA DE SER UNA PROYECCION.** La
> calibracion del verbo corrio, la bolsa de trabajo baja de **624 a 477**, y la
> tasa esta **medida sobre 46 lecturas pineadas**: **32 aristas que faltan, 7
> gemelos, 7 basura**. **Muere la cifra de *cero podas en veinticuatro
> lecturas***. Las dos nominas que faltaban, **el pivote y la serie de Coleman**,
> estan medidas y escritas en sus mesas. Y **el puro de la competencia entre
> inversores DEGRADA a sub-puro** con correccion declarada.
>
> **QUINTA PASADA, el mismo dia: se cierran los tres cabos que dejo la cuarta.** La
> **degradacion queda RECONCILIADA** con las dos decisiones en el registro, la del
> puesto 878 y la de hoy, **y ninguna se tacha**. **`OP-E-03` se adjudica sin puerta
> nueva** y pasa a LISTA con su instrumento escrito. Y la mesa de Coleman abre con
> **el precedente de la fase 3 verificado**: cuatro ids en uno, **diez aristas por
> alias y las diez con su gemela literal**.

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

## EL MARCADOR

| | |
|---|---:|
| operaciones | **45** |
| **LISTAS** | **39** |
| **DECISION PENDIENTE** | **6** |

| fase | operaciones | LISTAS | pendientes |
|---|---:|---:|---:|
| **0 CODIGO** | 4 | **4** | 0 |
| **01 FUENTES** | 7 | **7** | 0 |
| **02 DESTEJIDOS** | 6 | **6** | 0 |
| **03 FUSIONES** | 2 | **1** | 1 |
| **04 ENLACES** | 3 | **3** | 0 |
| **05 SANEO** | 11 | **11** | 0 |
| **06 MESAS** | 5 | 0 | **5** |
| **07 ADUANA** | 2 | **2** | 0 |
| **08 VERIFICACION** | 1 | **1** | 0 |
| **09 LECTURAS DIRIGIDAS** | 3 | **3** | 0 |
| **10 INVENTARIO** | 1 | **1** | 0 |

> **LAS SEIS PENDIENTES SON LAS CINCO MESAS Y UN RECOMPUTO CON FECHA.** `OP-U-02`
> espera al dia en que el cribado llegue al puesto **3.388**, y su disparador esta
> escrito en `08_VERIFICACION`. **Ninguna es un dato que falte.**
>
> **`OP-E-03` dejo de estar pendiente el 11 ago 2026.** El auditor la adjudico **sin
> puerta nueva**: se escribe como **DIFERENCIA CONTRA LA COLA**, con su instrumento
> ya probado, y **cuelga del mismo disparador del recomputo**.

## EL MAPA DE FASES, con sus dependencias

```
FASE 0  CODIGO   ──bloquea──► TODO lo que mueve un id
   │              (OP-S-01 deprecar, OP-S-09 renombrar, OP-F-01 y la fase 03)
   ▼
01 FUENTES ──(OP-F-02)──► 02 DESTEJIDOS (OP-D-04)
   │        ──(OP-F-03)──► OP-D-01 y OP-D-06: tres nodos de Hugos estan ahi
   │        ──(OP-F-01)──► verificacion de TODO 02
   ▼
02 DESTEJIDOS ──► 03 FUSIONES   no se funde lo que aun no se desteje
   │           ──► 06 MESAS      tres mesas no se sientan hasta la cirugia
   ▼
05 SANEO      OP-S-01 ──precede──► OP-S-09
07 ADUANA     OP-A-01 hereda el control posicional de P.2
08 VERIFICACION envuelve a todas, y el reindexado va AL FINAL

04 ENLACES  independiente: no mueve ids. Pero se VERIFICA con OP-C-04
```

**LAS TRES DEPENDENCIAS QUE NO SON DE ORDEN SINO DE SENTIDO**, y por eso se
escriben aqui arriba:

| dependencia | por que no es negociable |
|---|---|
| **codigo antes que todo** | **la pasada ES lo que mueve ids.** Un camino que resuelva a pelo se rompe, o se calla, el dia que la pasada empiece, **y con el usuario dentro** |
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

## LO QUE SIGUE ABIERTO

**Ninguna pregunta de dato.** Lo que queda son **cinco mesas** y **un recomputo con
fecha**.

| que | por que sigue abierto |
|---|---|
| **`OP-M-01` a `OP-M-05`** | una mesa **es** una decision que se toma con la familia delante. **Las cinco siguen en pie**, y la de la junta asesora se sienta ya con **cobertura COMPLETA** |
| **`OP-U-02`** | los 48 actos abiertos esperan **una sola recomputacion al cierre del cribado** (banco 9.21) |


**Y DOS DELTAS DECLARADOS, que no son preguntas pero se ven:**

- las familias de ids dan **125 nodos** y el auditor dio 123, **con las 53 familias
  clavadas**
- la tanda de injertos son **43 nodos** y no 46: el 46 contaba **declaraciones**, y
  tres se solapan

**Y UN DELTA DECLARADO, que no es pregunta pero conviene que se vea**: el auditor
dio **123 nodos** para las familias de ids y **mi recomputo da 125**, con las **53
familias clavadas**. La diferencia es de dos nodos y no de familias. **Se declara
en vez de forzarse.**

## LAS PAGINAS

| pagina | que contiene | estado |
|---|---|---|
| [`FASE_0_CODIGO.md`](FASE_0_CODIGO.md) | los blindajes del runtime, **primeros de todos**, con caso positivo | escrita |
| [`01_FUENTES.md`](01_FUENTES.md) | las tres decisiones de fuente, 18 nodos, y el precedente fuente-primero | escrita |
| [`02_DESTEJIDOS.md`](02_DESTEJIDOS.md) | los 13 actos del cierre transitivo, en orden por congelados liberados | escrita |
| [`05_SANEO.md`](05_SANEO.md) | marco-pais, vigencia, herramientas, campos sucios, auto-aristas e ids | escrita |
| [`CORRECCIONES_A_APLICAR.md`](CORRECCIONES_A_APLICAR.md) | una confirmacion y cuatro correcciones que viven FUERA de `docs/plan/`. **Las aplica la SESION A** | escrita |
| [`BANCO_DEL_PLAN.md`](BANCO_DEL_PLAN.md) | **P.1** la regla de medicion por el resolutor, y **P.2** la firma posicional del injerto | escrita |
| [`RECORTE_POSICIONAL.md`](RECORTE_POSICIONAL.md) | el recorte de P.2 corrido sobre **los 55 libros**: 67 nodos candidatos, seis libros | escrita |
| [`LECTURAS_DIRIGIDAS.md`](LECTURAS_DIRIGIDAS.md) | los pares que la cola **no traera nunca**: 205 medidos, **27 leidos** en dos tandas | escrita |
| [`10_INVENTARIO.md`](10_INVENTARIO.md) | **el inventario navegable**: 324 entradas por sujeto, con sus huecos nombrados | escrita |
| [`03_FUSIONES.md`](03_FUSIONES.md) | 221 actos sobre 576 nodos, corte 2117, marcado para recomputo | escrita |
| [`04_ENLACES.md`](04_ENLACES.md) | 477 candidatos tras calibrar, tasa medida en 46 lecturas, mas los sueltos de racimos | escrita |
| [`06_MESAS.md`](06_MESAS.md) | cinco mesas con nomina, dependencia y opciones con evidencia | escrita |
| [`07_ADUANA.md`](07_ADUANA.md) | el control posicional permanente, y la puerta semantica sin especificar | escrita |
| [`08_VERIFICACION.md`](08_VERIFICACION.md) | verificacion por fase y **el criterio de HECHO** | escrita |
