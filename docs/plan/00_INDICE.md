# EL CONSOLIDADO EJECUTABLE DE LA PASADA UNICA

**Este documento no decide: recoge lo decidido.** Su meta es que el dia de la
pasada **no haya que volver a pensar nada**, solo aplicar.

> **MODO DE CIERRE VIGENTE. Aqui no se repara ni un nodo.** Todo lo que sigue es
> documentacion.

**Primera entrega, 11 ago 2026: fases 00, 01, 02 y 05.** Las fases 03, 04, 06, 07
y 08 estan anunciadas en el mapa y **todavia sin escribir**.

> **SEGUNDA PASADA, 11 ago 2026: las QUINCE ADJUDICACIONES DEL AUDITOR estan
> aplicadas**, cada una escrita dentro de su operacion en el campo `adjudicacion`.
> **Dieciseis de diecinueve operaciones pasaron a LISTA.**
>
> **Y con una correccion mia declarada**, que esta entera en
> [`CORRECCIONES_A_APLICAR.md`](CORRECCIONES_A_APLICAR.md): **las 27 auto-aristas
> estaban bien y mi medicion de cero estaba mal.** La adjudicacion que mataba esa
> operacion se apoyaba en mi numero, asi que **la operacion vuelve al plan** y
> espera confirmacion.

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

| | primera pasada | **tras las adjudicaciones** |
|---|---:|---:|
| operaciones escritas | 19 | **19** |
| **LISTAS** | 4 | **16** |
| **DECISION PENDIENTE** | 15 | **3** |
| preguntas abiertas | 15 | **3** |

**LAS DIECISEIS LISTAS**: las tres decisiones de fuente (`OP-F-01`, `OP-F-02`,
`OP-F-03`), **los seis destejidos enteros** (`OP-D-01` a `OP-D-06`) y seis del
saneo (`OP-S-01` a `OP-S-06`, mas `OP-S-09`).

**LAS TRES QUE SIGUEN PENDIENTES**, y las tres por motivos distintos:

| id | por que sigue pendiente |
|---|---|
| **`OP-S-07`** | **vuelve al plan contra la adjudicacion**, porque la adjudicacion se apoyaba en una medicion mia que estaba mal. Espera confirmacion |
| **`OP-S-08`** | la medicion esta hecha; falta el veredicto caso por caso sobre 42 accesos directos en 12 ficheros |
| **`OP-S-10`** | es CONDICIONAL por adjudicacion: entra si la medicion muestra ley con alcance real, y la condicion queda escrita para evaluarse sin volver a preguntar |

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
| auto-aristas | **27 nodos** | **27**, remedido con la semantica de `resolverId`. **LA CIFRA ESTABA BIEN Y MI MEDICION DE CERO ESTABA MAL** | **`OP-S-07`** |
| self-alias | **7 nodos** | **0**. Esa mitad si encogio | `CORRECCIONES_A_APLICAR.md` |
| familias de ids de la DECISION 4 | sin nomina | **53 familias, 125 nodos vivos**, recomputadas con el criterio de la propia decision | **`OP-S-09`** |

> **LA LECCION, y es cara: una de las dos discrepancias no existia.** La de
> Incoterms era real y esta adjudicada. **La de las auto-aristas era un fallo de
> mi instrumento**, que devolvia el id sin resolver cuando el alias apuntaba a un
> nodo deprecado, **que es exactamente el caso de las 27**. Las 33 auto-aristas
> son **todas via alias y ninguna directa**, asi que un chequeo ingenuo da cero.
> **Detalle entero en [`CORRECCIONES_A_APLICAR.md`](CORRECCIONES_A_APLICAR.md).**

---

## LAS TRES PREGUNTAS QUE SIGUEN ABIERTAS

**Las otras doce quedaron cerradas por las adjudicaciones del 11 ago 2026**, y
cada una esta escrita dentro de su operacion en el campo `adjudicacion`.

| operacion | la pregunta |
|---|---|
| **`OP-S-07`** | la adjudicacion mataba esta operacion sobre una medicion mia de CERO. **Remedido bien: son 27, exactamente lo publicado.** Se confirma que vuelve al plan? |
| **`OP-S-08`** | de los **42 accesos directos al grafo en produccion** (12 ficheros, 9 con ids de origen externo), **cuales reciben un id que viene de fuera del grafo**? Esos son los unicos que tienen que pasar por `resolverId` |
| **`OP-S-10`** | la condicion esta escrita para evaluarse sola: **la medicion muestra ley con alcance real en `franquicias`?** Las cuatro familias medidas son norma obligatoria y no formato de referencia |

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
| [`CORRECCIONES_A_APLICAR.md`](CORRECCIONES_A_APLICAR.md) | las cinco correcciones que viven FUERA de `docs/plan/`, listas para pegar | escrita |
| `03_FUSIONES.md` | fusiones de par y de familia, con superviviente y direccion | **sin escribir** |
| `04_ENLACES.md` | la arista que falta: 624 candidatos, proyeccion de 376 a 586 | **sin escribir** |
| `06_MESAS.md` | las mesas con su nomina y sus dependencias | **sin escribir** |
| `07_ADUANA.md` | la puerta de insercion semantica permanente y Gate 0 | **sin escribir** |
| `08_VERIFICACION.md` | como se comprueba cada fase y el criterio de HECHO | **sin escribir** |
