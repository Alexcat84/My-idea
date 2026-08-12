# CORRECCIONES A APLICAR FUERA DE `docs/plan/`

**Esta pagina existe por una frontera de sesion.** La instruccion dice **escribir
solo en `docs/plan/`**, y ademas manda corregir cifras que viven **en la ficha y
en el banco**. Las dos cosas no caben a la vez.

> **Lo que hago: dejo la correccion ESCRITA, exacta y lista para pegar, con su
> ubicacion. Lo que no hago: cruzar la frontera y tocar ficheros que la otra
> sesion puede estar escribiendo.** Un fichero pisado en paralelo es caro de
> deshacer; una correccion escrita y no aplicada, no.

> **ADJUDICADO el 11 ago 2026: LAS CUATRO CORRECCIONES LAS APLICA LA SESION A**,
> que es la duena de esos ficheros, **cuando reporte su tanda.** Esta pagina es su
> encargo, escrito y verificado. **Desde aqui no se cruza la frontera.**

---

## CONFIRMACION 0: LAS 27 AUTO-ARISTAS SE CONFIRMAN, NO SE CORRIGEN

**Va primero y NO es una correccion: es lo contrario.** La cifra publicada de **27
esta bien** y **no hay que tocarla**.

**Que paso.** Informe *auto-aristas medidas hoy, CERO*. **Mi medicion estaba mal**:
mi resolutor era *el id, si esta en el grafo; y si no, su duena*, y **las 27
apuntan a ids que SI estan en el grafo, como DEPRECADOS**, asi que los devolvia sin
resolver.

**Remedido con la semantica de `resolverId`, y el auditor lo remidio aparte con el
mismo instrumento: coinciden.**

| | publicado | **remedido y confirmado** |
|---|---:|---:|
| nodos vivos con **auto-arista** | **27** | **27** |
| enlaces implicados | | **33** |
| **directos** | | **0** |
| **via alias propio** | | **33** |

> **QUIEN APLIQUE ESTA PAGINA TIENE QUE SABER DOS COSAS:**
>
> **1. La fila de las 27 en `PENDIENTES.md` se queda como esta.** Ni se corrige ni
> se anota como dudosa.
>
> **2. El motivo del banco 9.14 QUEDA CONFIRMADO.** Esa regla, *todo conteo de
> grado excluye el propio nodo*, se adopto **usando las 27 como motivo**. El motivo
> se sostiene entero: **la regla no solo sigue en pie, ahora tiene su cifra
> verificada dos veces.**

**Lo unico que si encogio es el self-alias**, y va como correccion 1.

**CONSECUENCIA EN EL PLAN**: `OP-S-07` **vuelve como operacion LISTA**, con los 27
ids, el arreglo y **la guarda que Gate 0 necesita**, que no es la que parece. Ver
[`05_SANEO.md`](05_SANEO.md).

---

## CORRECCION 1: el self-alias, de SIETE a CERO

**UBICACION**: `docs/AUDITORIA_MOTOR.md`, seccion **B.3**.

**TEXTO PUBLICADO:**

> *Además, 7 nodos se listan a sí mismos como su propio alias (`trilogia_de_juran`,
> `recomendaciones_smart`, …): ruido inofensivo, pero ruido.*

**CORRECCION A PEGAR DEBAJO, sin borrar el original:**

> **CORREGIDO el 11 ago 2026, medido sobre las tres copias del dataset: hoy son
> CERO.** Ningun nodo vivo ni deprecado se lista a si mismo en `ids_alias`.
> `trilogia_de_juran`, el ejemplar citado, lleva hoy tres alias y **ninguno es el
> suyo**. La guarda del codigo sigue en pie y hace bien: `mapaDeAlias` en
> `web/lib/engine/graph.ts` filtra `if (a !== nid)` con el comentario *el
> auto-alias (7 nodos) no dice nada*. **La guarda se queda; la cifra que la
> motivaba ya no.**

---

## CORRECCION 2: Incoterms, de DOCE a TRES

**UBICACION**: `docs/PENDIENTES.md`, seccion *ADJUDICADO PARA EL PLAN (11 ago
2026)*, tabla **LA EVIDENCIA REAL**, fila de Incoterms.

**FILA PUBLICADA**: `| citan **Incoterms** sin ninguna version | **12** |`

**FILA CORREGIDA:**

```
| citan **Incoterms** sin ninguna version, EN SU TEXTO | **3** |
```

**Y LA NOTA QUE LA ACOMPANA, para que la correccion se entienda y no se repita:**

> **CORREGIDO el 11 ago 2026.** La cifra de 12 sumaba **los 3 que lo CITAN en su
> texto mas 9 que solo lo llevan en una arista o en el id**. Es **el mismo error
> que esta misma adjudicacion habia corregido tres parrafos mas arriba para
> NAFTA**: *apuntar al nodo no es citar el tratado, y mezclarlos infla la cifra.*
> **Se corrigio la fila de NAFTA y no la de al lado.**
>
> **Los TRES son de `exportacion` y los tres sin version**:
> `incoterms_reglas_comerciales_internacionales`, `terminos_de_venta_incoterms` y
> `seguro_de_carga_transporte`. **Los dos primeros lo llevan tambien en el id.**
>
> **LA DECISION DE FONDO NO SE MUEVE.** La **UNION** de las tres averias baja de
> **21** a **12 nodos**, con **solape cero** entre ellas, y **los 12 de 12 siguen
> siendo de `exportacion`**, que era el argumento. **El argumento sobrevive
> entero: solo cambia el tamano.**

**Y la fila de la UNION en la misma tabla:**

```
| **UNION de las tres** | **12** |
```

---

## CORRECCION 3: la promesa del resolutor SI se cumplio

**UBICACION**: `docs/AUDITORIA_MOTOR.md`, seccion **B.3**, titulo y primer
parrafo.

**TEXTO PUBLICADO**: *`ids_alias`: una promesa que nadie cumple* ... *ningún
código lo lee. Busqué `ids_alias` en todo `web/lib`, `web/app`, `scripts/` y
`engine/`: solo aparece en la declaración del tipo y en el consolidador que lo
escribe. **No existe resolutor.***

**CORRECCION A PEGAR DEBAJO:**

> **CUMPLIDA, y verificada contra el codigo el 11 ago 2026.** El resolutor
> **existe**: `web/lib/engine/graph.ts` construye el mapa en `mapaDeAlias` (linea
> 107) y exporta **`resolverId`** (linea 131), que **camina cadenas de alias**
> hasta un nodo activo y, si la cadena entera fue retirada, devuelve el eslabon
> mas reciente que exista. **Lo invocan `etiquetaArbol` (164) y `tituloDeNodo`
> (172)**, hay un espejo en Python en `scripts/reanclar_por_resolutor.py`, y lo
> ejercitan `resolutorHistoria.test.ts` y `compass.test.ts`.
>
> **Lo que queda no es construirlo: es medir por donde pasa.** Medido el mismo
> dia: en produccion (`web/lib` y `web/app`, sin tests) hay **42 accesos directos
> al grafo por id, en 12 ficheros, y 9 de esos ficheros manejan ids de origen
> externo.** Esa es la lista que hay que revisar, y es `OP-S-08` del plan.

**Y la tabla de alias, medida el mismo dia**, por si la auditoria quiere fijarla:

| | |
|---|---:|
| alias totales | **391** |
| a nodo **deprecado**, que es su funcion | **314** |
| **colisiones vivas** (alias que apunta a un nodo vivo) | **0** |
| **huerfanos** a ids inexistentes | **77** |

> **Los 77 se limpian en el saneo sin riesgo**: con **cero colisiones vivas**, su
> borrado no puede romper una resolucion buena.

---

## CORRECCION 4: la cuenta de los 18 nodos de fuente

**UBICACION**: `docs/COSTURAS_INTERNAS_RESUMEN.md`, seccion 6 y seccion 7, punto 1.

**TEXTO PUBLICADO**: *Tres decisiones de fuente que cubren dieciocho nodos.*

**CORRECCION A PEGAR AL LADO:**

> **RECOMPUTADA con su corte, 11 ago 2026, tras la adjudicacion de que MANDA LA
> CLASE y no la cuenta.** La cuenta de 18 tomaba **cuatro** miembros de la clase
> LARGO LEGITIMO, los del *Basic Guide*, y dejaba fuera **tres** que estan en la
> misma clase: dos de *Juran's Quality Handbook* y uno de `core`. **Con la clase
> entera, el alcance de las tres decisiones de fuente es de 7 mas 3 mas 21 = 31
> nodos**, no 18.
>
> **El salto grande no es ese**: la nomina de Hugos, publicada como **11 de las 46
> confirmadas**, se midio el mismo dia en **21 nodos vivos que declaran Hugos
> junto a otra fuente**. **Los dos numeros conviven** porque cuentan cosas
> distintas: 11 son costuras confirmadas con pegado de Hugos; 21 son todos los
> nodos con la firma del injerto. **La cifra que el plan usa es la de 21, por
> adjudicacion.**

---

## RESUMEN, para decidir de un vistazo

| # | que pasa | donde | quien lo aplica |
|---:|---|---|---|
| **0** | **NO se corrige nada: las 27 se CONFIRMAN**, y con ellas el motivo del banco 9.14 | ninguna | nadie: **solo hay que saberlo** |
| 1 | self-alias, de 7 a **0** | `AUDITORIA_MOTOR.md` B.3 | **SESION A** |
| 2 | Incoterms, de 12 a **3**; union de 21 a **12** | `PENDIENTES.md`, adjudicacion del barrido | **SESION A** |
| 3 | la promesa del resolutor **si** se cumplio | `AUDITORIA_MOTOR.md` B.3 | **SESION A** |
| 4 | la cuenta de 18, recomputada con su corte | `COSTURAS_INTERNAS_RESUMEN.md` 6 y 7 | **SESION A** |

> **Las cuatro son de la SESION A y se aplican cuando reporte su tanda.** Ninguna
> se toca desde aqui.

> **Y NINGUNA TOCA EL BANCO 9.14.** Esa regla usaba las 27 como motivo, y **el
> motivo queda confirmado en vez de corregido.**
