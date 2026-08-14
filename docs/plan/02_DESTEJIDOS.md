# FASE 02: LOS DESTEJIDOS, los trece actos del cierre transitivo

**Un acto no es un par: es una COMPONENTE.** Si A repite con B y B con C, los tres
son el mismo acto y **los tres tienen que estar en la mesa el dia que eso se
arregle** (banco 9.24).

> **La cifra que este calculo aporta no es cuantos pares hay. Es CUANTOS NODOS HAY
> QUE TENER DELANTE para poder decidir**, que es exactamente lo que faltaba.

~~**Operaciones: `OP-D-01` a `OP-D-06`. LAS SEIS LISTAS**, tras la adjudicacion del
11 ago 2026.~~

> **AVISO, 14 ago 2026 (vuelta 17). LA FASE YA NO SON SEIS OPERACIONES: SON NUEVE.** La cifra vieja
> no se borra, era correcta el 11 ago 2026.
>
> | | | |
> |---|---|---|
> | `OP-D-07` | `decision_pivote_perseverar` | anadida el 12 ago 2026, destejido previo al acto I de `OP-M-03` |
> | **`OP-D-08`** | **`lienzo_modelo_negocio`** | **anadida el 14 ago 2026 por DECISION DEL FUNDADOR** |
> | **`OP-D-09`** | **`planificacion_recoleccion_datos`** | **anadida el 14 ago 2026 por DECISION DEL FUNDADOR** |
>
> **LAS NUEVE ESTAN LISTAS. Las dos ultimas son las DOS COSTURAS QUE NO TENIAN DUENO:** estaban
> declaradas en `docs/plan/RECOMPUTO_3388.md` (TAREA 2.B, punto 4) como las dos unicas de las 31
> costuras confirmadas sin gemelo vigente que no aparecian en la nomina de ninguna operacion del
> plan, ni de fuente ni de fusion. **La adjudicacion que decia "NO se crean operaciones nuevas para
> ellas" queda revertida por el fundador el 14 ago 2026, y no se borra: sigue escrita con su fecha.**
>
> **LAS DOS SON DESTEJIDO SOLO, sin fusion acoplada**, y no por comodidad: **ninguna de las dos tiene
> gemelo con A vigente**, remedido en la vuelta 17 contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (cero
> A en los siete pares de `lienzo_modelo_negocio` y cero en el unico par de
> `planificacion_recoleccion_datos`). El veredicto del puesto 1434 ya lo tenia escrito para la
> primera: *"es costura confirmada y no tiene gemelo, asi que su arreglo es un destejido solo"*.
>
> **AVISO DE ORDEN, declarado y no arreglado por cuenta propia.** El criterio de orden de esta fase
> es **CONGELADOS LIBERADOS** (ver la tabla de abajo). Por ese criterio `OP-D-08` libera **uno** (el
> par 784) y le tocaria ir **entre `OP-D-03` y `OP-D-04`**, y `OP-D-09` libera **cero**. Las dos se
> escribieron con orden **8 y 9**, al final, **porque renumerar siete operaciones ya adjudicadas no
> es algo que la vuelta 17 tuviera autorizado.** Queda como discutible marcado.
>
> **Y EL HUECO QUE `OP-D-08` TAPA, que es el motivo de fondo:** el par **784** estaba congelado por
> una costura cuya cirugia **no tenia dueno**, asi que **ese congelado no entraba en la contabilidad
> de nadie**. Medido en la vuelta 17: **el numero 784 no aparece ni una vez en todo `docs/plan/`**, y
> la tabla de congelados de abajo no lo cuenta. **Su propia razon se nombra "tercer nodo del archivo
> que bloquea un par por costura"**, y de los tres, dos ya tenian operacion (`voz_del_cliente_voc` en
> `OP-D-02`, `ab_testing_optimizacion` en `OP-D-03`) **y este era el que no la tenia.**

> **LA REGLA DE REPARTO, adjudicada, y es lo que desbloqueo las tres que
> faltaban:** cada perdida se asigna **AL BLOQUE DEL QUE PROVIENE**; la que no
> tenga bloque va **AL SUPERVIVIENTE**.
>
> **Con eso el reparto deja de necesitar una relectura previa.** Los actos 1 y 4 y
> los nueve de dos estaban pendientes solo porque nadie habia escrito su reparto;
> ahora se resuelve **en el acto, bloque por bloque**.

---

## LA CIFRA, con su corte y su caducidad

| medida | resultado |
|---|---:|
| costuras miradas | 49 |
| sin ninguna A (componente de una) | 32 |
| **con gemelo** | **17** |
| **ACTOS en que se reparten** | **13** |
| **nodos totales dentro de esos 13 actos** | **38** |

> **VIGENTE AL PUESTO 1256**, recomputada sin cambios al **1277**. El cribado va
> hoy por el **2117**. **PENDIENTE DE RECOMPUTO**, y no se recomputa aqui: el
> banco 9.21 manda que el barrido de confirmadas se repita **una sola vez, al
> cierre del cribado**.

> **Que puede cambiar el recomputo y que no.** Cada A nueva puede unir dos
> componentes y volver un acto de dos en un acto de cinco: **puede cambiar los
> tamanos y el numero de actos**. **No cambia el orden**, porque el orden se decide
> por congelados liberados, y una A nueva no mueve un congelado.

---

## EL ORDEN, y el criterio que lo fija

**El criterio es CONGELADOS LIBERADOS. No es tamano, no es coste.**

| orden | operacion | el nodo ancla | congelados que libera | destejidos | nodos en la decision |
|---:|---|---|---:|---:|---:|
| **1** | `OP-D-01` | `producto_minimo_viable` | **3** (494, 592, 830) | **2** | 2 |
| **2** | `OP-D-02` | `voz_del_cliente_voc` | **3** (724, 755, 827) | 1 | 4 |
| **3** | `OP-D-03` | `ab_testing_optimizacion` | **2** (738, 1061) | **3** | **6** |
| 4 | `OP-D-04` | `brainstorming_divergente` | 0 | 1 mas la decision de fuente | **7** |
| 5 | `OP-D-05` | `seleccion_ceo_fundador` | 0 | 1 | 3 |
| 6 | `OP-D-06` | los nueve actos de dos | 0 | 9 | 2 cada uno |

> **OCHO de los quince congelados cuelgan de TRES nodos.** No estan repartidos por
> el catalogo: **estan amontonados.** Tres cirugias desbloquean mas de la mitad, y
> **hacerlas tarde bloquea ocho pares a la vez.**

> **Y la consecuencia para las mesas**: las que tocan esos tres nodos **no se
> sientan hasta que la cirugia este hecha.** No es eficiencia: es que **antes de la
> cirugia esas mesas no tienen el veredicto que necesitan para decidir.**

**AVISO DE COSTE, escrito y sin reordenar nada.** El tercer puesto del orden **no
es una cirugia: son tres.** El acto de las pruebas A/B contiene **TRES costuras
confirmadas**, y el plan lo escribio como una sola. **Medido por componentes es la
mas cara en cirugias y la segunda en nodos.** El orden se mantiene porque el
criterio es congelados liberados y por esa cuenta es correcto.

---

## `OP-D-01`: EL MVP, la cura acoplada mayor · **LISTA**

**Acto 11. Nodos: `producto_minimo_viable`, `principio_calidad_mvp`.**
`producto_minimo_viable` es **el emblema de la averia**: 22 pasos, cinco
narraciones, bloque 80,2, **el mas alto del archivo**. Y es **el primer destejido
del plan**, elegido *no por ser el mayor sino por ser el mas barato*: su material
sobrante **ya esta localizado paso por paso**, asi que el destejido deja de ser un
juicio y pasa a ser **una lista de borrados**.

**ORDEN INTERNO, y no son dos movimientos sino TRES:**

1. destejer `producto_minimo_viable`
2. destejer `principio_calidad_mvp`
3. **solo entonces** decidir si lo que queda se funde (par **494**)
4. releer **592** y **830** contra el superviviente

**QUE SE PRESERVA:**

- del destejido del emblema: el material sobrante, ya localizado paso por paso
- del destejido del pariente: **decidir si conserva la narracion de LA CALIDAD
  (pasos 1 a 5) o la del CONJUNTO MINIMO (pasos 11 a 14)**

> **Por eso el par 494 esta CONGELADO por dependencia directa:** si conserva la
> narracion de la calidad, el par **deja de repetir**; si conserva la del conjunto
> minimo, **sigue repitiendo**. **No se puede saber antes de la cirugia.**

**PRECEDENTE EXACTO DE LA FORMA**: el puesto **341**, `blueprint_de_experiencia`
contra `customer_journey_mapping`, donde los dos estaban costurados y el solape era
mapa contra mapa. **Es la segunda vez que aparece, y esta cae sobre el nodo que
abre el plan.**

---

## `OP-D-02`: LA VOZ DEL CLIENTE · **LISTA**

**Acto 3. Cuatro nodos**: `voz_del_cliente_voc`, `enfoque_mercado_voc`,
`homework_frontend_loading`, `voice_of_customer_homework`.

**`voz_del_cliente_voc` es el nodo que MAS PARES CONGELA de todo el archivo.**
Diez pasos, **doble de la observacion**: Cooper en 1 a 5, Coleman en 6 a 10, con
**duplicado literal del paso 2 contra el paso 6**.

**ORDEN INTERNO:**

1. destejer separando **Cooper (1 a 5)** de **Coleman (6 a 10)**
2. fundir con `enfoque_mercado_voc`, **que cubre justo la mitad que la cirugia
   deja en pie**
3. releer **724**, **755** y **827**
4. tener delante a `homework_frontend_loading` y `voice_of_customer_homework`

**QUE SE PRESERVA, ya repartido por bloques (banco 9.11):**

| va con | que |
|---|---|
| **la fusion** | de `enfoque_mercado_voc`: la evaluacion preliminar de mercado, el analisis competitivo detallado, y probar los conceptos con clientes reales antes del desarrollo formal |
| **el destejido** | el bloque 6 a 10 entero: observar una vez al mes, ponerse en el lugar del cliente, las pepitas de oro, anotar y revisar a los dos dias, y buscar patrones |

> **Aqui la cura acoplada es literal: destejer y fundir son el MISMO acto.**

> **Y este acto es el aviso de metodo del ejercicio.** `voz_del_cliente_voc`
> parecia una costura con **un** gemelo sano y son **tres**. Dos de ellos,
> `homework_frontend_loading` y `voice_of_customer_homework`, **se leyeron en la
> relectura R31 sin que nadie notara que colgaban de la misma costura.** La
> relectura ve **pares**; el alcance se decide sobre la **componente**.

---

## `OP-D-03`: LAS PRUEBAS A/B · **LISTA**

**Acto 2. SEIS nodos y TRES destejidos.** Costuras: `ab_testing_optimizacion`,
`optimizacion_embudo_get_customers`, `split_testing_experimentos_ab`. Sanos:
`funnel_get_customers_optimizacion`, `split_testing`, `test_ab_precio`.

**ORDEN INTERNO:**

1. destejer **las tres costuras**
2. **solo entonces** decidir sobre los **seis** nodos
3. releer **738** y **1061**

**QUE SE PRESERVA:**

- del nodo chico de `split_testing`: **la significancia estadistica del 95%**
- **el cambio porcentual y el grupo de control similar VIVEN en el bloque de
  Rackham (pasos 6 a 9)** y se van **con el destejido**: no se pierden en la
  fusion, y por eso no hay que rescatarlas

> **El 1061 es una costurada contra costurada**, el tercer acto de tres del
> archivo. Y es el par que **corrigio la cifra de costuras con gemelo**: no anadio
> una costura, **cambio la CLASE del acto**, de dos actos sueltos a uno solo.

---

## `OP-D-04`: EL BRAINSTORMING · **LISTA**

**Acto 1, el mayor: SIETE nodos.** `brainstorming_divergente` mas
`brainstorming_efectivo`, `reglas_brainstorming`, `generar_multiples_opciones`,
`construir_sobre_ideas_ajenas`, `pensamiento_convergente_divergente`,
`design_attitude_vs_decision_attitude`.

**Es el nodo de mas frentes del catalogo: cuatro pendientes viejos que resultaron
ser el mismo nodo.**

| frente | que pide |
|---|---|
| **1. decision de fuente** | el injerto de Mollick: lleva atribucion de un libro que no es de donde salio su contenido |
| **2. destejido** | es costura CONFIRMADA, con repeticion interna verificada |
| **3. tres gemelos** | 823, 834 y 844: **su cura acoplada es de cuatro nodos en un solo acto** |
| **4. racimo de cuatro libros** | la fusion toca la atribucion de mas de un miembro |

**ORDEN INTERNO, y no es negociable:**

1. **`OP-F-02` PRIMERO**, la fuente
2. el destejido despues
3. **los tres gemelos al final y en un solo acto**

**ADJUDICADO: la regla de reparto lo resuelve sin relectura previa.** El bloque de
IA va al racimo de supervision (`OP-F-02`); lo que quede de taller va al
superviviente; y de cada gemelo, lo propio que no este en el destejido va al
superviviente. **Cada perdida al bloque del que proviene.**

---

## `OP-D-05`: LA SELECCION DEL CEO · **LISTA**

**Acto 4. Tres nodos**: `seleccion_ceo_fundador`,
`asignacion_de_titulos_ejecutivos`, `errores_comunes_asignacion_roles`. Pares que
lo sostienen: **492, 673, 833**.

**Sin congelados: su orden es libre respecto de los tres primeros.**

**ADJUDICADO: misma regla de reparto.** Cada perdida al bloque del que proviene;
la que no tenga bloque, al superviviente. **Ya no necesita relectura previa.**

> **Nota util para quien se siente**: su par **492** es uno de los **doce
> ejemplares de cura acoplada encontrados de uno en uno**, y **se podia declarar
> desde el 673 sin que nadie lo declarara.** Es el argumento de por que el barrido
> de confirmadas existe.

---

## `OP-D-06`: LOS NUEVE ACTOS DE DOS · **LISTA**

**Anclas**: `producto_unico_superior`, `propuesta_gasto_capital`,
`blueprint_de_experiencia` con `customer_journey_mapping`,
`plan_de_adquisicion_acquire`, `key_partners_hypothesis`,
`metricas_de_adquisicion_activacion`, `principio_calidad_mvp` con
`producto_minimo_viable`, `future_scenarios_planning`, `retention_metrics`.

**DOS de los nueve YA tienen reparto escrito:**

| acto | que se preserva |
|---|---|
| `metricas_de_adquisicion_activacion` (puesto 392) | **en la fusion**: que el sistema escale luego a retencion y cohortes, de `build_metrics_toolset`. **Con el destejido**: definir que es una conversion, comparar el CAC contra el LTV, y usar SEM para aprender que mensaje funciona |
| `blueprint_de_experiencia` con `customer_journey_mapping` (puesto 341) | precedente de la cura acoplada, mapa contra mapa |

> **AVISO DE SOLAPE, y hay que verlo antes de contar dos veces:**
> `producto_minimo_viable` y `principio_calidad_mvp` **aparecen aqui Y en
> `OP-D-01`**. La seccion 54.3 los cuenta como uno de los nueve actos de dos; el
> plan de cirugia los trata como **cura acoplada mayor**. **Es la MISMA pareja
> vista por dos instrumentos, no dos trabajos.**

**ADJUDICADO Y COMPLETADO. Los nueve pares, medidos contra el archivo el 11 ago
2026, corte del puesto 2117:**

| puesto | el par |
|---:|---|
| **285** | `producto_unico_superior` con `superioridad_producto_beneficios` |
| **331** | `propuesta_gasto_capital` con `analisis_de_gastos_de_capital` |
| **341** | `blueprint_de_experiencia` con `customer_journey_mapping` |
| **344** | `plan_de_adquisicion_acquire` con `plan_acquire_activate` |
| **361** | `key_partners_hypothesis` con `partners_hypothesis_physical` |
| **392** | `metricas_de_adquisicion_activacion` con `build_metrics_toolset` |
| **494** | `principio_calidad_mvp` con `producto_minimo_viable` |
| **711** | `future_scenarios_planning` con `escenarios_futuros` |
| **969** | `retention_metrics` con `customer_retention_metrics_webmobile` |

> **HALLAZGO DEL RECOMPUTO: los NUEVE siguen siendo de DOS al corte del 2117.**
> Ninguno crecio. Es la primera vez que se comprueba, y le quita al recomputo
> pendiente una de las cosas que podia mover.

**EL REPARTO**: dos ya lo tienen escrito, el 392 y el 341; **los otros siete se
resuelven con la regla adjudicada**, cada perdida al bloque del que proviene.

> **Y DOS CRUCES MAS CON LA FASE 01**: `producto_unico_superior` y
> `propuesta_gasto_capital` estan en `OP-F-03`, y `future_scenarios_planning` es
> uno de los tres injertos de `OP-F-02`. **En los tres manda fuente primero.**

---

## VERIFICACION DE LA FASE

**Cada operacion, al terminar:**

- **Gate 0 verde**
- cada nodo resultante **dentro del estandar de pasos**, o declarado excepcion por
  `OP-F-01`
- **los pares congelados de esa operacion se releen** contra el superviviente y
  salen de la lista
- **recomputo del cierre transitivo** tras el acto (banco 9.21)

**Y de la fase entera**: los **quince congelados** releidos, y la tabla de trece
actos **recomputada al corte del cierre del cribado**, no al 1256.
