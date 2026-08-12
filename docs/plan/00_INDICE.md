# EL CONSOLIDADO EJECUTABLE DE LA PASADA UNICA

**Este documento no decide: recoge lo decidido.** Su meta es que el dia de la
pasada **no haya que volver a pensar nada**, solo aplicar.

> **MODO DE CIERRE VIGENTE. Aqui no se repara ni un nodo.** Todo lo que sigue es
> documentacion.

**Primera entrega, 11 ago 2026: fases 00, 01, 02 y 05.** Las fases 03, 04, 06, 07
y 08 estan anunciadas en el mapa y **todavia sin escribir**.

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

| | |
|---|---:|
| operaciones escritas | **19** |
| **LISTAS** | **4** |
| **DECISION PENDIENTE** | **15** |
| preguntas para el auditor | **15**, una por operacion pendiente |

**LAS CUATRO LISTAS**, y las tres primeras son el corazon de la pasada:

| id | que es |
|---|---|
| **`OP-D-01`** | el MVP, cura acoplada mayor. Libera **tres** congelados |
| **`OP-D-02`** | la voz del cliente. Libera **tres** congelados |
| **`OP-D-03`** | las pruebas A/B. Libera **dos** congelados, y son **tres destejidos** |
| **`OP-S-03`** | `export.gov` a `trade.gov`. Tres nodos, cuatro menciones |

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
    OP-S-08 (resolutor de alias) ──bloquea──► OP-S-01 (toque unico NAFTA)
                                              OP-S-09 (ids de la DECISION 4)
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
| **resolutor de alias antes que el alias** | `OP-S-01` crea un alias para proteger dos aristas. **Ningun codigo lee `ids_alias` hoy**: sin resolutor, ese alias no protege nada, solo lo documenta |

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
| Incoterms sin version | **12 nodos** | **3** lo citan en su texto; los otros 9 solo lo llevan en una arista o en el id | **`OP-S-02`** |
| auto-aristas | **27 nodos**; y 7 self-alias | **0** y **0**, en las tres copias del dataset | **`OP-S-07`** |

> **En los dos casos, lo que rodea a la cifra SI cuadra**: NAFTA da 6 y
> `export.gov` da 3 en la misma tabla que Incoterms; los 77 alias huerfanos y los
> seis campos sucios cuadran clavados en la misma auditoria que las auto-aristas.
> **O sea que el dataset es el mismo y la discrepancia esta en esas dos filas, no
> en el instrumento entero.**

---

## LAS QUINCE PREGUNTAS, en una lista

**Estan enteras y con su contexto en cada operacion. Aqui van en corto para que se
puedan repartir.**

| # | operacion | la pregunta, en una linea |
|---:|---|---|
| 1 | `OP-F-01` | el estandar de 3 a 6 pasos, admite excepcion nombrada para los formatos lista? y alcanza a los siete o solo a los cuatro del Basic Guide? |
| 2 | `OP-F-02` | los tres injertos de Mollick: se retira la atribucion, se desteje el bloque de IA, o se conserva como segunda fuente? |
| 3 | `OP-F-03` | **cuales son los once ids del pegado de Hugos?** La cifra esta publicada y la nomina no existe |
| 4 | `OP-D-04` | el acto del brainstorming (siete nodos) no tiene reparto de perdidas escrito: se abre relectura antes, o entra en blanco? |
| 5 | `OP-D-05` | el acto 4 tampoco tiene reparto: relectura previa o mesa el mismo dia? |
| 6 | `OP-D-06` | los nueve actos de dos no tienen nomina par a par: relectura de reparto o entran como bloque? |
| 7 | `OP-S-01` | **la direccion de la fusion de NAFTA**: una cierra los tres encargos y la otra deja dos abiertos |
| 8 | `OP-S-02` | la fila publicada de Incoterms contaba aristas como citas? y que ano se escribe? |
| 9 | `OP-S-04` | herramienta muerta: se borra, se sustituye, o se generaliza la linea perdiendo el nombre propio? |
| 10 | `OP-S-05` | se verifican los dieciocho nombres pendientes antes de la pasada, o se sanea solo lo verificado? |
| 11 | `OP-S-06` | `fuentes_adicionales` en cuatro nodos: se fusiona en `fuente` o se borra? |
| 12 | `OP-S-07` | las auto-aristas ya se repararon fuera de la campana, o el instrumento medía otra base? |
| 13 | `OP-S-08` | los 77 alias huerfanos: se borran o se registran como deprecados? y el resolutor entra en esta pasada? |
| 14 | `OP-S-09` | **cual es la nomina completa de ids de la DECISION 4?** La politica esta aprobada y la lista no existe |
| 15 | `OP-S-10` | entra `franquicias` al barrido de marco junto a `exportacion`? |

> **Tres de las quince son la misma clase de agujero y conviene verlas juntas: la
> 3, la 14 y, en parte, la 6.** En las tres hay **una cifra publicada y aprobada
> sin la nomina de ids que la sostiene**. No es que la decision falte: **falta la
> lista sobre la que se decidio.**

---

## LAS PAGINAS

| pagina | que contiene | estado |
|---|---|---|
| [`01_FUENTES.md`](01_FUENTES.md) | las tres decisiones de fuente, 18 nodos, y el precedente fuente-primero | escrita |
| [`02_DESTEJIDOS.md`](02_DESTEJIDOS.md) | los 13 actos del cierre transitivo, en orden por congelados liberados | escrita |
| [`05_SANEO.md`](05_SANEO.md) | marco-pais, vigencia, herramientas, campos sucios, auto-aristas e ids | escrita |
| `03_FUSIONES.md` | fusiones de par y de familia, con superviviente y direccion | **sin escribir** |
| `04_ENLACES.md` | la arista que falta: 624 candidatos, proyeccion de 376 a 586 | **sin escribir** |
| `06_MESAS.md` | las mesas con su nomina y sus dependencias | **sin escribir** |
| `07_ADUANA.md` | la puerta de insercion semantica permanente y Gate 0 | **sin escribir** |
| `08_VERIFICACION.md` | como se comprueba cada fase y el criterio de HECHO | **sin escribir** |
