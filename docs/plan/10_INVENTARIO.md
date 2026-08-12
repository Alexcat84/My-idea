# FASE 10: EL INVENTARIO NAVEGABLE

**La vista humana de `INVENTARIO.jsonl`.** Una entrada por **sujeto**: dominio,
racimo, acto, familia de ids, figura y defecto.

> **AQUI NO SE MIDE NADA NUEVO. Es consolidacion de lo ya escrito**, y **todo lo
> que se copia lleva su fecha de corte**. Lo que no existe todavia **se escribe
> como HUECO NOMBRADO, no se rellena.**

**FECHA DE CORTE DE TODO EL INVENTARIO: 11 ago 2026, cribado al puesto 2.117 de
3.388.** Se recomputa entero con el disparador de `08_VERIFICACION`.

---

## EL VOLUMEN

| tipo | entradas |
|---|---:|
| **dominio** | **10** |
| **racimo** | **13** |
| **acto** | **221** |
| **familia_de_ids** | **53** |
| **figura** | **12** |
| **defecto** | **16** |
| **TOTAL** | **325** |

---

## POR DOMINIO

**Diez dominios vivos. Seis han pasado por el cribado intra, CINCO estan cerrados,
y CUATRO no han entrado nunca.**

| dominio | nodos vivos | pares leidos | A | tasa | estado |
|---|---:|---:|---:|---:|---|
| **compras** | 46 | 155 | 1 | 0,6% | CERRADO |
| **core** | 1618 | 1.445 | 344 | 23,8% | CERRADO |
| **entrega** | 47 | 171 | 2 | 1,2% | CERRADO |
| **environmental** | 289 | 170 | 29 | 17,1% | CERRADO |
| **exportacion** | 141 | 130 | 15 | 11,5% | CERRADO |
| **franquicias** | 195 | 46 | 9 | 19,6% | **abierto y bajando** |
| `health_safety` | 283 | 0 | 0 | | **SIN CRIBAR** |
| `quality` | 792 | 0 | 0 | | **SIN CRIBAR** |
| `risk_management` | 55 | 0 | 0 | | **SIN CRIBAR** |
| `seguridad_digital` | 55 | 0 | 0 | | **SIN CRIBAR** |

> **HUECO NOMBRADO, y es el mayor del inventario: CUATRO DOMINIOS NO HAN ENTRADO
> AL CRIBADO INTRA.** `quality` (792 nodos), `health_safety` (283),
> `risk_management` (55) y `seguridad_digital` (55). **Son 1.185 nodos vivos, un
> tercio del catalogo, sobre los que este inventario no dice nada.**

> **Y la tasa de `franquicias` NO se puede leer como esta:** el dominio esta
> abierto, y por el banco 9.27 **la cola del dominio se agota por dentro**. El
> 19,6% de hoy **va a bajar**, como bajo `exportacion` de 36,0% a 11,5%.

---

## LOS ACTOS

**Un ACTO es una componente conexa de la relacion gemelo** (banco 9.24): si A
repite con B y B con C, los tres se deciden juntos.

| | |
|---|---:|
| **actos** | **221** |
| nodos implicados | **576** |
| **CERRADOS**, listos para fundir | **173** |
| **ABIERTOS**, esperan al recomputo | **48** |

**POR TAMANO:**

| miembros | actos |
|---:|---:|
| 2 | 154 |
| 3 | 39 |
| 4 | 12 |
| 5 | 7 |
| 6 | 4 |
| 7 | 2 |
| 8 | 1 |
| 9 | 1 |
| 13 | 1 |

**LOS SEIS MAYORES, y CUATRO no se funden aqui:**

| miembros | el acto | donde se resuelve |
|---:|---|---|
| **13** | puertas y portafolio | **`OP-M-01`**, mesa |
| **9** | customer discovery | **`OP-M-05`**, mesa |
| **8** | build, measure, learn | fusion |
| **7** | customer validation | **`OP-M-05`**, mesa |
| **7** | el brainstorming | **`OP-D-04`**, destejido con decision de fuente |
| **6** | cuatro empatados | pruebas A/B en `OP-D-03`; los otros tres, fusion |

> **Cuando un acto es grande, casi nunca es una fusion limpia.** Los de 13, 9 y 7
> llegaron a serlo **porque el catalogo trato el mismo programa de varias
> maneras**, y eso es una decision de forma.

---

## LOS RACIMOS, con su forma medida

**Trece racimos con nombre.** La forma **no** es una etiqueta permanente: **es lo
que se sabe con la cobertura que tiene.**

| racimo | forma | cobertura | estado |
|---|---|---|---|
| **el efectivo contra la ganancia** | PURO | 3 de 3 | sano, forma cerrada |
| **la ecuacion de valor** | MEZCLADO | 10 de 10 | repite, forma cerrada |
| **el sales roadmap** | MEZCLADO | 10 de 15 | repite, cobertura INCOMPLETA |
| **la competencia entre inversores** | SUB-PURO | 7 de 10 | repite, DEGRADADO y RECONCILIADO el 11 ago 2026, cobertura INCOMPLETA |
| **la junta asesora** | MEZCLADO | 6 de 6 | en mesa, forma cerrada |
| **los cuadrantes de mercado** | MEZCLADO | 15 de 15 | repite, forma cerrada |
| **build, measure, learn** | SUB-PURO | 9 de 28 | repite, cobertura INCOMPLETA |
| **el compromiso contado tres veces** | PURO | 3 de 3 | sano, forma cerrada |
| **la seleccion de canal** | MEZCLADO | 10 de 10 | repite, forma cerrada |
| **la supervision de la IA** | PARTIDO 5 mas 4 mas 1 | 14 de 45 al puesto 1517 | en mesa, particion PROVISIONAL |
| **la mesa unida de puertas y portafolio** | una familia o dos, SIN DECIDIR | 18 de 120 | en mesa, cobertura 15% |
| **el racimo del pivote** | MEZCLADO | 13 de 21 | mesa, EXPEDIENTE ESCRITO el 12 ago 2026, pendiente de adjudicacion |
| **la serie de Coleman** | MEZCLADO | 41 de 378 | MESA ADJUDICADA el 12 ago 2026, siete operaciones hijas |

> **TRES SUB-PUROS CAYERON EL 11 ago 2026 al cerrarse su cobertura**: los
> cuadrantes, la ecuacion de valor y el bloque humano de la IA. **Los tres pasaron
> a MEZCLADO en cuanto se termino de leerlos**, y por la razon que el banco ya
> tenia escrita: **el sub-puro es una promesa, no un resultado.**

**LOS DOS HUECOS SE CERRARON EL 11 ago 2026.** El **racimo del pivote** y la
**serie de Coleman** ya tienen nomina por id, medida con el contador mas el barrido
de las A y escrita en su bloque de apertura de `06_MESAS`.

| nomina | miembros | cobertura | lo que trae a su mesa |
|---|---:|---|---|
| **el racimo del pivote** | **7** | **13 de 21**, MEZCLADO | **las cuatro A no hacen un acto, hacen TRES**, cosidos entre si por **seis dudosos** |
| **la serie de Coleman** | **27** *(19 programa, 8 medios)* | **38 de 351**, MEZCLADO | **la fase 3 YA recibio el tratamiento que la mesa debate**: `fase_affirm_buyers_remorse` lleva tres alias dentro |

**Y LA CIFRA QUE PEDIA RE MEDIRSE SE RE MIDIO, Y BAJO**: *la competencia entre
inversores* se declaro **PURA con 4 miembros y 6 pares al puesto 1030**; la
componente medida al puesto 2.117 tiene **5 miembros y 10 pares**, con **7 leidos y
los 7 en A**. **DEGRADA a SUB-PURO, cobertura 7 de 10.** El quinto miembro,
`tecnica_anclaje_negociacion`, entro por una A **posterior a la declaracion** (el
puesto 878), y **los tres pares que faltan son suyos y estan fuera de cola.**

> **La degradacion no desmiente ninguna lectura: los siete pares leidos siguen
> siendo siete A.** Dice otra cosa, y es la que vale: **la forma se declaro sobre
> una componente que todavia iba a crecer.**

**Y LA DEGRADACION QUEDO RECONCILIADA EL MISMO DIA, que es lo que la cierra.** Ese
quinto miembro **ya se habia mirado y ya se habia dejado fuera con motivo escrito**
en el puesto **878**, el primer uso del barrido de las A: *su objeto es como
negociar terminos y no como generar competencia entre inversores*. **La exclusion no
se borra**, y ademas explica por que el racimo se declaro con cuatro.

**Manda la admision de hoy por tres razones que se suman**, y ninguna es *porque es
mas nueva*:

| | |
|---|---|
| **1** | el propio archivo, en el puesto **1295** y por tanto **despues** de la exclusion y de la declaracion de puro, escribe que ese nodo **tiene una A vigente y ES GEMELO** de `construccion_de_leverage` |
| **2** | **las dos decisiones no hablan del mismo objeto**: la del 878 decide el **TEMA** del racimo; la de hoy decide el **ACTO**, que por el banco 9.24 es el cierre transitivo de la relacion gemelo **y no admite gusto** |
| **3** | **la forma publicada se calculo sobre el ACTO**, no sobre el tema: *puro, cuatro miembros, seis pares* es una cuenta de componente conexa, y por el banco 9.17 **manda la medicion** |

> **LO QUE DE VERDAD PASO: se declaro una forma de ACTO sobre una nomina de TEMA.**
> Mientras el quinto no tuvo A, las dos coincidian. **Desde el puesto 878 dejaron de
> coincidir, y la etiqueta se quedo con la cuenta vieja.**

> **Y EL DESEMPATE VA EN LOS DOS SENTIDOS.** Si los tres pares fuera de cola salen
> **A**, vuelve a PURO con cinco. Si salen **D**, el quinto sale del acto y vuelve a
> PURO con cuatro, **o sea gana la exclusion del 878**. **Tres lecturas lo
> resuelven**, y por eso las dos decisiones se quedan con su fecha y ninguna se
> tacha.

La correccion para el banco de la sesion A esta en `CORRECCIONES_A_APLICAR.md`,
**correccion 6**, con la reconciliacion entera dentro.

---

## LAS FAMILIAS DE IDS

**53 familias sobre 125 nodos vivos**, medidas con el criterio de la DECISION 4:
sufijo numerico, particulas, orden de palabras y sinonimo.

| miembros | familias |
|---:|---:|
| 5 | 2 |
| 4 | 2 |
| 3 | 9 |
| 2 | 40 |

**LAS CUATRO MAYORES:**

| familia | ids |
|---|---|
| `accion_correctiva` | `accion_correctiva`, `accion_correctiva_2`, `accion_correctiva_4`, `accion_correctiva_5`, `accion_correctiva_6` |
| `consejo_calidad` | `consejo_calidad`, `consejo_calidad_2`, `consejo_de_calidad`, `consejo_de_calidad_2`, `consejo_de_calidad_3` |
| `definiciones_operacionales` | `definiciones_operacionales`, `definiciones_operacionales_2`, `definiciones_operacionales_3`, `definiciones_operacionales_4` |
| `make_certain_programa` | `make_certain_programa`, `programa_make_certain`, `programa_make_certain_2`, `programa_make_certain_3` |

> **Todas se resuelven por `OP-S-09`, con continua o repite y fusion con alias.**
> La excepcion escrita se mantiene: **la transdominio y el `_2` de propiedad
> intelectual van por renombre, no por fusion**, porque en los dos el contenido
> esta sano.

---

## LAS FIGURAS

**Doce figuras de lectura con doctrina escrita.** No son defectos: **son formas que
el catalogo produce y que hay que saber distinguir.**

| figura | ejemplares | que es |
|---|---|---|
| **SUBCONJUNTO ESTRICTO** | 23 ejemplares | los pasos del corto viven dentro del largo y lo unico propio cabe en una linea |
| **LA VARA EN LOS DOS SENTIDOS (9.22)** | 2 polos, 3 ejemplares del primero y 2 del segundo | procedimiento en los dos: sanos, ENLACE MUTUO. Linea en los dos: repiten, fusion |
| **ESTRELLA (9.23)** | 9 ejemplares | un centro que repite con dos periferios que entre si son sanos. La septima es INVERTIDA: el centro es el corto |
| **TRIANGULO ABIERTO** | 2 ejemplares | tres nodos del mismo tema y los TRES pares en D: la fuente partio el tema en tres cortes reales |
| **EL ESQUELETO COMPARTIDO** | 3 ejemplares | misma forma de pasos, contenido distinto en cada uno. Es el contrario del subconjunto estricto |
| **LAS DOS ADUANAS** | 5 ejemplares | lo que el destino exige contra lo que el pais propio prohibe. Contra la regla ajena hay recurso, contra la propia no |
| **LA BIFURCACION** | 2 ejemplares | un nodo declara en su primer paso que NO es el otro |
| **LOS DOS PARES QUE NO SE CRUZAN** | 1 ejemplar | dos parejas gemelas cuyos cruces salen D: la duplicacion esta dentro de cada pareja |
| **LA FIRMA POSICIONAL DEL INJERTO (P.2)** | 67 nodos candidatos, 43 confirmados | el orden dentro del campo fuente lleva informacion: el segundo libro es lo pegado |
| **LA A DE BLOQUE (P.4)** | 1 ejemplar y 1 contraejemplo | la repeticion vive entre el bloque injertado y el otro nodo entero. Destejido mas fusion parcial, nunca fusion de enteros |
| **LA COLA DEL DOMINIO SE AGOTA POR DENTRO (9.27)** | 3 dominios medidos | la tasa de A cae dentro de cada dominio: un dominio a medio leer no describe al dominio |
| **EL PASO DE OFICIO** | medio dominio exportacion | una linea generica que abre media docena de nodos y por si sola no decide ninguna clase |

---

## LOS DEFECTOS, por clase y con su cuenta

| defecto | cuantos | estado | operaciones |
|---|---:|---|---|
| **aristas duplicadas tras resolucion** | 1056 | reparado en el plan | `OP-S-12`, `OP-C-05` |
| **aristas que faltan** | 477 | pendiente, BOLSA RECALIBRADA y tasa MEDIDA | `OP-E-01`, `OP-E-03` |
| **grafias no canonicas del campo fuente** | 129 | reparado en el plan | `OP-S-11` |
| **alias huerfanos** | 77 | reparado en el plan | `OP-S-08` |
| **marco de un solo pais** | 73 | reparado en el plan | `OP-S-10` |
| **gemelos que el cribado no ve** | 73 | pendiente, se recoge por DIFERENCIA CONTRA LA COLA | `OP-E-03` |
| **injertos de fuente** | 67 | reparado en el plan | `OP-F-01`, `OP-F-02`, `OP-F-03` y mas |
| **costuras internas confirmadas** | 46 | pendiente | `OP-D-01`, `OP-D-02`, `OP-D-03` y mas |
| **auto-aristas via alias** | 27 | reparado en el plan | `OP-S-07`, `OP-C-04` |
| **accesos al grafo sin resolver** | 20 | reparado en el plan | `OP-C-01`, `OP-C-02`, `OP-C-03` |
| **campos sucios** | 6 | reparado en el plan | `OP-S-06` |
| **herramientas muertas** | 6 | reparado en el plan | `OP-S-04`, `OP-S-05` |
| **Incoterms sin version** | 3 | reparado en el plan | `OP-S-02` |
| **portal caducado export.gov** | 3 | reparado en el plan | `OP-S-03` |
| **racimos con miembro de otro dominio** | 3 | pendiente | `OP-E-02` |
| **tratado extinto en id y titulo** | 1 | reparado en el plan | `OP-S-01` |

> **12 de los 16 ya tienen operacion LISTA en el plan.** Los 4 pendientes son: **costuras internas confirmadas** (46), **aristas que faltan** (477), **racimos con miembro de otro dominio** (3), **gemelos que el cribado no ve** (73).

> **Y el mas nuevo de todos es el ultimo de esa lista: los GEMELOS QUE EL CRIBADO NO
> VE.** Aparecio el 11 ago 2026 leyendo la bolsa calibrada, **no se busco**, y son
> unos 73 pares con banda de 36 a 135. **Seis de los siete ejemplares medidos estan
> en `quality`, que no ha entrado nunca al cribado.**

> **LA BOLSA DE LAS ARISTAS QUE FALTAN BAJO DE 624 A 477** con la senal del verbo, y
> su tasa dejo de ser proyeccion: **32 sanas, 7 gemelos y 7 basura en 46 lecturas
> pineadas**. **Con su limite escrito al lado, que es la cifra que nadie debe
> soltar: la senal del verbo SOLO OPINA CUANDO CONOCE LAS DOS FAMILIAS DE ACCION, y
> sobre los 477 las conoce en 104, el 21,8%.** Los 477 no son una bolsa filtrada del
> todo: **son una bolsa filtrada en el quinto de sitios donde el instrumento tenia
> con que comparar.**

---

## LAS FUENTES, ya normalizadas

**55 libros canonicos** detras de **129 grafias distintas**. La normalizacion es
`OP-S-11` y **es prerrequisito de la aduana**.

| | |
|---|---:|
| nodos vivos | **3.521** |
| grafias distintas en primera posicion | **129** |
| **libros canonicos** | **55** |
| nodos con **mas de un libro** | **67** |
| **libros que aparecen en segunda posicion** | **6** |

**LOS SEIS QUE APORTAN INJERTOS, y los otros 49 no aportan ninguno:**

| libro | 1a o unica | **2a o posterior** |
|---|---:|---:|
| Essentials of Supply Chain Management, Hugos | 107 | **21** |
| Never Lose a Customer Again, Coleman | 68 | **15** |
| The Hard Thing About Hard Things, Horowitz | 88 | **14** |
| Traction, Weinberg | 67 | **13** |
| SPIN Selling, Rackham | 47 | **4** |
| Co-Intelligence, Mollick | 47 | **3** |

> **Los 43 de Coleman, Horowitz, Weinberg y Rackham se leyeron el 11 ago 2026 y
> salieron 43 de 43 CONFIRMADOS**, con cero arrastre. **Los 21 de Hugos ya estaban
> adjudicados y los 3 de Mollick tambien.**

---

## COMO SE LEE ESTE INVENTARIO

| si busca | mire |
|---|---|
| **que hay en un dominio** | la tabla por dominio, y **compruebe si esta cribado**: cuatro no lo estan |
| **si un nodo repite** | `INVENTARIO.jsonl`, entradas de tipo `acto`, campo `miembros` |
| **si una forma es firme** | el campo `cobertura`. **Toda forma con cobertura incompleta es PROVISIONAL** (banco 9.26) |
| **quien toca un sujeto** | el campo `operaciones` de su entrada |
| **cuando caduca lo que lee** | el campo `fecha_corte`: **todo el inventario es del 11 ago 2026** |

> **LA ADVERTENCIA QUE GOBIERNA TODO EL DOCUMENTO: este inventario describe UN
> CATALOGO A DOS TERCIOS DE LEER.** 2.117 pares de 3.388, y cuatro dominios sin
> entrar. **Lo que dice es cierto; lo que no dice es la mayoria.**

