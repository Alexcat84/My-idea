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
| **1** | `OP-D-01` | `producto_minimo_viable` | ~~**3** (494, 592, 830)~~ **3 LIBERADOS EL 15 ago 2026: 494 a `C`, 592 a `D`, 830 a `D`** | **2** | 2 |
| **2** | `OP-D-02` | `voz_del_cliente_voc` | ~~**3** (724, 755, 827)~~ **3 LIBERADOS EL 15 ago 2026: los tres a `D`** | 1 | 4 |
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

> ~~**Por eso el par 494 esta CONGELADO por dependencia directa:** si conserva la
> narracion de la calidad, el par **deja de repetir**; si conserva la del conjunto
> minimo, **sigue repitiendo**. **No se puede saber antes de la cirugia.**~~
>
> **RESUELTO EL 15 ago 2026 (vuelta 33), y la prediccion acerto:** la cirugia
> **conservo la narracion de la CALIDAD** (`principio_calidad_mvp` quedo en siete
> pasos, con el bloque 11 a 14 ya llevado por `OP-F-03`), **el par dejo de
> repetir**, y el 494 paso de `A` a **`C`**, sano con figura por el banco `9.22`.
> El congelamiento queda levantado. Detalle en el movimiento 3, mas abajo.

**PRECEDENTE EXACTO DE LA FORMA**: el puesto **341**, `blueprint_de_experiencia`
contra `customer_journey_mapping`, donde los dos estaban costurados y el solape era
mapa contra mapa. **Es la segunda vez que aparece, y esta cae sobre el nodo que
abre el plan.**

### `OP-D-01` EJECUTADA (15 ago 2026, vuelta 32), y sus cuatro movimientos con su medicion

**Nada de esta seccion viene de un acta ni de un reporte: todas las cifras salen de instrumentos
corridos en esta misma vuelta, con su salida en `docs/loop/`.**

#### MOVIMIENTO 1: el destejido del emblema, **HECHO**

**`producto_minimo_viable` pasa de 22 pasos a SEIS y de 10 condiciones a CINCO**, sin que salga
un solo bloque del nodo: su costura es de **fuente unica** (Ries consigo mismo, cinco
narraciones en fila), asi que no hay material ajeno que destejer con destino, solo repetido que
colapsar. Plan sellado en `docs/loop/PLAN_V32_OPD01_EMBLEMA.json`, ejecutado con
`scripts/loop/vuelta32_podar.py`.

**EL CRITERIO DEL SUPERVIVIENTE, escrito antes de aplicarlo para que se pueda auditar: de cada
grupo de repeticion sobrevive EL DE INDICE MAS BAJO.** No es una preferencia estetica: es el
unico criterio que no obliga a elegir entre frases que la ficha ya declaro equivalentes, y deja
el orden propio del nodo en pie. **El resultado cae exactamente sobre la NARRACION 1 (pasos 1 a
5), que es la que el propio `entregable_esperado` del nodo ya narraba**, mas el paso 8.

**TABLA VIEJA (15 ago 2026, vuelta 32), CONSERVADA ENTERA Y TACHADA, NO BORRADA.** Su celda
del paso 2 traia el origen **16** y por eso la fila del paso 6 contradecia a su propio motivo.
**La cabecera va tachada tambien, y no es cosmetica: asi el verificador de mapas no la lee como
tabla vigente**, que es lo que una tabla retirada no debe ser.

| ~~paso del resultado~~ | ~~de que origenes salia~~ | ~~el motivo de perdida de linea que lo modifica~~ |
|---:|---|---|
| ~~**1**~~ | ~~1, 10~~ | ~~**SALVAGUARDA**: el paso 10 trae la prueba de que alguien PAGARIA por resolverlo, y el inciso se adosa al paso que protege~~ |
| ~~**2**~~ | ~~2, 6, 11, 15, **16**, 19~~ | ~~**SALVAGUARDA**: los pasos 6, 15 y 19 nombran el sesgo (la lista larga de pedidos) que el superviviente no nombraba~~ |
| ~~**3**~~ | ~~3, 9, 13, 18~~ | ~~**ALCANCE**: el paso 13 trae el segundo criterio de la excepcion (que sin ella no se pueda vender) y entra a la enumeracion~~ |
| ~~**4**~~ | ~~4, 7, 12, 20~~ | ~~**NOMBRE** (banco 9.28): el superviviente decia *early adopters* y no *earlyvangelists*, que es la palabra por la que se busca y la que da nombre a dos nodos vecinos~~ |
| ~~**5**~~ | ~~5, 21~~ | ~~**SALVAGUARDA**: el paso 21 dice contra que sesgo se lee la medicion (no para expandir funciones)~~ |
| ~~**6**~~ | ~~8, 14, 17, 22~~ | ~~**ALCANCE**: los pasos 14 y 16 traen la cadencia (ciclos cortos, incremental)~~ |

> **CORRECCION DECLARADA (15 ago 2026, vuelta 33), y es la caida de CIFRA PUBLICADA que el
> acta 32 marco.** **EL ORIGEN 16 PASA DEL GRUPO DEL PASO 2 AL GRUPO DEL PASO 6.**
>
> **QUIEN TENIA RAZON, MEDIDO HOY Y NO SUPUESTO** (`scripts/loop/vuelta33_corregir_16.py`,
> salida `docs/loop/SALIDA_V33_C16_SIM.txt`, que imprime los pasos en disputa ANTES de tocar
> nada): **el MOTIVO tenia razon y la CELDA estaba mal.** El paso 16 original dice *Desarrolla
> tu primera version de forma incremental, en ciclos cortos e iterativos*: **es la cadencia**,
> que es el paso 6 del resultado, **no el conjunto minimo** del paso 2. Los tres que si son el
> conjunto minimo (**6**, **15** y **19**) empiezan los tres por *Define el conjunto minimo de
> caracteristicas*, y el 16 no.
>
> **EL TEXTO DEL NODO NO SE TOCA, y tampoco es una opinion:** `vuelta32_podar.py` toma el
> superviviente por el **primer origen del grupo** y el texto por `pasos_finales`, escrito
> aparte. **`min` del grupo del paso 2 sigue siendo 2 y el del paso 6 sigue siendo 8** con el 16
> dentro o fuera, **y la cobertura sigue en 22 de 22 sin huecos ni repetidos**. El instrumento
> comprueba esa invariante y **se niega a escribir si no se cumple**. `dataset/nodos` intacto.
>
> **TRES CAMPOS DEL PLAN SELLADO CARGABAN LA MISMA PARTICION Y LOS TRES SE CORRIGEN**, con las
> particiones viejas escritas enteras en el bloque `correcciones_declaradas` del propio
> `PLAN_V32_OPD01_EMBLEMA.json`: `grupos_pasos` (el que el encargo nombra y el que el
> verificador compara), **`mapa_pasos` (el campo OPERATIVO, el que `vuelta32_podar.py`
> consume)** y `pruebas_repeticion` (el que `vuelta32_caso_positivo.py` imprime al lado de cada
> huella). **Corregir solo el primero habria dejado el plan contradiciendose consigo mismo y al
> verificador en verde encima de la contradiccion.**
>
> **Y UN LIMITE, dicho para que nadie le atribuya al verde lo que no midio:** la huella de la
> prueba de repeticion de ese grupo es *conjunto minimo de caracteristicas*, **que el paso 16
> nunca contuvo**. La prueba **jamas midio al 16**, porque cuenta la huella sobre el NODO
> RESULTANTE y solo IMPRIME los origenes. **La celda mala no falseo ningun verde: no habia
> instrumento que la leyera.** Ese es exactamente el hueco que el verificador de mapas cierra.

**TABLA VIGENTE. NO ESTA TECLEADA: esta IMPRESA desde el plan sellado**, que es la regla del 15
ago 2026 (`EJECUTOR.md` regla 1, cuarto renglon). **Comando, corrido en esta vuelta:**

```
python scripts/loop/vuelta33_tabla_mapa.py docs/loop/PLAN_V32_OPD01_EMBLEMA.json
```

salida entera en `docs/loop/SALIDA_V33_TABLA_OPD01.txt`, y pegada aqui sin editar una coma:

| paso del resultado | de que origenes sale | el motivo de perdida de linea que lo modifica |
|---:|---|---|
| **1** | 1, 10 | SALVAGUARDA: el superviviente manda identificar la hipotesis y no dice contra que sesgo se decide cual es la critica. El paso 10 trae la prueba (que alguien PAGARIA por resolverlo) y el inciso se adosa al paso que protege. |
| **2** | 2, 6, 11, 15, 19 | SALVAGUARDA: el superviviente manda disenar lo mas simple y no dice contra que sesgo (la lista larga de pedidos). Los pasos 6, 15 y 19 nombran el sesgo y el inciso se adosa al paso que protege. |
| **3** | 3, 9, 13, 18 | ALCANCE: el superviviente trae UN criterio para la excepcion (que sirva para aprender) y el paso 13 trae el segundo (que sin ella no se pueda vender). El segundo entra a la enumeracion que el superviviente ya tiene, que es el remedio escrito del motivo. |
| **4** | 4, 7, 12, 20 | NOMBRE: el superviviente dice early adopters y no dice earlyvangelists, que es la palabra por la que se busca y la que da nombre a dos nodos vecinos del grafo. El nombre viaja como DENOMINACION dentro del paso. |
| **5** | 5, 21 | SALVAGUARDA: el superviviente manda medir para validar y no dice contra que sesgo se lee la medicion. El paso 21 lo dice (no para expandir funciones) y el inciso se adosa al paso que protege. |
| **6** | 8, 14, 16, 17, 22 | ALCANCE: el superviviente manda iterar y no dice a que cadencia. Los pasos 14 y 16 traen la cadencia (ciclos cortos, incremental) y entra a la enumeracion del superviviente. |

> **La columna del motivo cambia de redaccion respecto de la tabla vieja, y se dice por que:**
> la vieja era un resumen tecleado a mano y **esta es la frase entera del plan sellado**. El
> banco `9.28` que la fila 4 citaba no se pierde: **vive en el campo `motivo` del plan** y en el
> parrafo del criterio, arriba.

**`DESTINO`, `METODO ALTERNATIVO` y `DIRECCION` no aplican, y por eso no se nombran.**

> **UNA DISCREPANCIA DECLARADA EN VEZ DE RESUELTA COPIANDO, y es contra una cifra ya publicada.**
> La ficha (`docs/FICHA_SUBFUSION_GRADIENTE.md`, seccion a) proyectaba **de veintidos pasos a
> CINCO**. **La medicion de hoy, grupo por grupo, da SEIS**, y el sexto tiene nombre: *iterar o
> cambiar de rumbo* (pasos 8, 14, 17 y 22) **es una cosa que la narracion 1 no contiene**. La
> proyeccion de la ficha se queda escrita donde esta; **seis sigue dentro del estandar de 3 a
> 6** que la propia ficha cita.

| guarda | resultado |
|---|---|
| simulacion previa sobre copia en memoria | **verde** (`SALIDA_V32_OPD01_SIM.txt`) |
| guarda de texto sobre TODOS los pasos y TODAS las condiciones | **22 de 22** y **10 de 10** calzan con su prefijo |
| cero perdida, cobertura exacta sin huecos ni repetidos | **22 de 22** origenes en pasos, **10 de 10** en condiciones |
| **caso positivo ANTES** | **0 PASAN, 8 CAEN** (`SALIDA_V32_OPD01_CASO_ANTES.txt`) |
| **caso positivo DESPUES** | **8 PASAN, 0 CAEN** (`SALIDA_V32_OPD01_CASO_DESPUES.txt`) |
| conservacion (pasa las dos veces a proposito, se cuenta aparte) | **14 rastros vivos, 0 muertos** |
| fuente | **sin cambio**, Ries, unica |

#### MOVIMIENTO 2: el destejido del pariente, **CONSUMIDO, y se dice con su medicion**

**`principio_calidad_mvp` no tiene costura interna que destejer hoy, y no porque yo lo diga:
porque el instrumento no dispara.** Medido con `scripts/loop/vuelta32_costura_opd01.py`, que
importa las dos senales y los dos umbrales de `scripts/costuras_internas.py` en vez de
copiarlos: **mejor pareja de pasos 51,2 contra un umbral de 80; mejor alineacion de bloques 0,0
contra un umbral de 44. NINGUNA SENAL DISPARA.** (El emblema, ya destejido, da 50,3 y 0,0: los
dos quedan por debajo de las dos varas.)

> **CORRECCION DECLARADA (15 ago 2026, vuelta 34). LA CIFRA DE BLOQUE DE ESTE PARRAFO NO MEDIA LO
> QUE DECIA MEDIR, Y SE RECOMPUTA. La conclusion NO cambia; cambia una de sus dos patas.** El
> parrafo de arriba se queda entero: la caida la declaro el ejecutor de la vuelta 33 y la
> confirmo el acta 33 del auditor (seccion 3.2), y el fundador la mando arreglar el 15 ago 2026.
>
> **RECOMPUTO CORRIDO HOY, con el nodo impreso ENTERO delante** (`scripts/loop/vuelta34_mov2.py`,
> salida en `docs/loop/SALIDA_V34_MOV2_RECOMPUTO.txt`):
>
> | pata del apoyo | vuelta 32 | medido hoy |
> |---|---|---|
> | **senal 1, pareja de pasos** | **51,2** contra 80, no dispara | **51,2**, pasos 2 y 3. **SE REPRODUCE AL DIGITO** y sigue sin disparar |
> | **senal 2, alineacion de bloques** | **0,0** contra 44, no dispara | con la regla NUEVA: **45,8 con corte tras el paso 5. DISPARA** |
> | **lectura del nodo entero** | (no se publico) | **NO hay costura**: los pasos 6 y 7 son la CONTINUACION (decidir con el feedback, iterar), no un reinicio del bloque 1 a 5 |
>
> **Y LA CAUSA DEL 0,0 NO ERA LA QUE SE DIJO, y esto tambien se corrige.** El reporte de la vuelta
> 33 la atribuyo al **rango vacio** (`range(MIN_BLOQUE, n - MIN_BLOQUE + 1)` con cinco pasos). Eso
> es cierto **para los dos nodos de calibracion, que tienen cinco pasos, pero NO para este**, que
> tiene **siete** y cuyo rango no estaba vacio. **Medida hoy corte por corte, la causa real es
> otra:** el emparejamiento monotono solo lograba **UN** emparejamiento donde el promedio exigia
> **TRES**. **Dos averias distintas con el mismo sintoma**, y la del acta 33 no cubria a esta.
>
> **LO QUE EL 45,8 NO AUTORIZA A CONCLUIR, y por eso la conclusion no se voltea:** con
> `MIN_BLOQUE` en 2 el umbral 44 quedo **por debajo de la mediana** de la senal (**p50 45,8**,
> medido sobre 2.245 nodos en `docs/loop/SALIDA_V34_CALIBRACION.txt`). **Este nodo puntua
> exactamente la mediana del catalogo.** Disparar ahi no distingue a un nodo costurado de la mitad
> del archivo. **La pata instrumental de esta conclusion queda EN SUSPENSO, no volteada, y la que
> la sostiene hoy es la lectura**, que es la vara que el propio instrumento declara superior.

**LAS TRES NARRACIONES QUE LA FICHA LE CONTABA YA NO ESTAN, y cada una tiene su fecha y su
operacion:** la **TERCERA** (el conjunto minimo, pasos 11 a 14) **se la llevo `OP-F-03`**, y la
**SEGUNDA** (lanzar rapido y aceptar el fallo, pasos 6 a 10) **se fundio con la PRIMERA en esta
misma vuelta por `P.19`**, dentro de `OP-F-04-HOR`. **Queda UNA narracion, la de la calidad, y
el destejido que esta operacion pedia ya esta consumido por esas dos operaciones.**

> **EL NODO QUEDA EN SIETE PASOS, uno por encima del estandar de 3 a 6, y eso entra por la
> puerta que la propia verificacion de esta operacion nombra:** *cada nodo resultante dentro del
> estandar, **o dentro de la excepcion de clase de `OP-F-01`***. La firma escrita de esa clase
> (`01_FUENTES.md`) es **superar el estandar SIN narracion repetida dentro**, y eso es
> exactamente lo que el instrumento midio. **La excepcion se aplica por su criterio escrito, no
> por pertenencia a la nomina de `OP-F-01`**, que es de otra operacion.

#### MOVIMIENTO 3: el par **494**, releido con la vara ordinaria. **NO SE FUNDE**

**La razon publicada del 494 apoyaba la clase A en una sola cosa**, y esta leida hoy en el
archivo (`SALIDA_V32_OPD01_RELECTURA.txt`): *los pasos 11 al 14 del primero son el nucleo del
segundo dicho otra vez*. **Esos pasos ya no existen.** Y el informe (§494) habia escrito la
condicion por adelantado: *si el destejido conserva la narracion de la CALIDAD, el par deja de
repetir*. **La conserva.**

**LA VARA, aplicada en los DOS SENTIDOS y sobre LINEAS DISTINTAS:**

| sentido | la linea | quien trae el procedimiento entero |
|---|---|---|
| **1** | `principio_calidad_mvp` paso 3, en UNA linea: *lanza al mercado real versiones simplificadas y mide la reaccion real* | **`producto_minimo_viable`**, con sus seis pasos: hipotesis, version minima, sin extras, early adopters, medir, iterar o pivotar |
| **2** | `producto_minimo_viable` pasos 2 y 3, en UNA linea: *la version mas simple, sin funciones extra* (cuan simple es bastante simple) | **`principio_calidad_mvp`**, con su procedimiento de calidad: si sirve al aprendizaje, no asumir el estandar de la industria, distinguir el defecto de la fealdad, y decidir con el feedback si invertir en alta calidad |

> **Es el banco 9.22, LA VARA EN LOS DOS SENTIDOS**, y por su letra el par es **`C`, sano CON
> FIGURA, no `D`**: *ninguno de los dos es la madre, y fundirlos seria el error caro porque
> borraria los dos procedimientos para dejar un nodo con dos lineas sueltas*. **El arreglo es
> ENLACE MUTUO, dos aristas**, y **medido hoy en los dos sentidos NO HAY NINGUNA**: ni
> `principio_calidad_mvp` nombra a `producto_minimo_viable` ni al reves.
> **Seria el TERCER ejemplar del 9.22**, tras el 1077 y el 1240, y el primero que nace con el
> enlace sin poner.

#### MOVIMIENTO 4: **592** y **830**, releidos contra el superviviente

**Los dos estaban en `B` por la MISMA causa y esa causa cayo hoy:** *un nodo averiado por dentro
contamina todos los pares en los que entra, porque el veredicto se emite contra un texto que va
a cambiar* (banco 9.4, el TOQUE UNICO). **El texto ya cambio y ya es estable.**

> **CORRECCION DECLARADA (15 ago 2026, vuelta 33): LA COLUMNA SE LLAMABA *clase que sostengo* Y
> HOY SE LLAMA *clase VOLCADA*.** Cuando esta tabla se escribio, las dos clases estaban leidas y
> sin escribir en el archivo; **el 15 ago 2026 se volcaron las dos por el banco `9.10`**, y el
> archivo dice hoy lo que esta tabla sostenia. La columna se deja con su nombre viejo tachado.

| puesto | contra quien | lo que el otro trae y el emblema sigue sin decir, medido contra sus SEIS pasos de hoy | ~~clase que sostengo~~ **clase VOLCADA el 15 ago 2026** |
|---:|---|---|---|
| **592** | `mvp_catalogo_tecnicas` | **la ESCALERA DE COSTO**: empezar por el MVP mas barato (hoja de datos, folleto, storyboard), subir en sofisticacion solo si lo primero promete, y usar herramientas a mano antes de pagar produccion profesional. **Ninguno de los seis pasos del emblema nombra el coste, el tipo de prototipo ni la herramienta.** Comparten el arranque (identificar la hipotesis critica) | **`D`, sano, con ARISTA QUE FALTA** hacia `mvp_catalogo_tecnicas` |
| **830** | `prueba_mvp_alta_fidelidad` | **el AISLAMIENTO DE LA PRUEBA**: numero limitado de clientes invitados, llamada a la accion clara, cuantas visitas antes del primer uso, cuantos lo recomiendan y que tan rapido, y evitar publicidad, prensa o demostraciones publicas. **Ninguno de los seis pasos lo dice.** El solape (mostrar solo a los earlyvangelists) **era una de las ordenes que el emblema repetia CUATRO veces y ahora vive en UNA** | **`D`, sano, con ARISTA QUE FALTA** hacia `prueba_mvp_alta_fidelidad` |

> **LA CLASE SE SOSTIENE CON LA PRACTICA MEDIDA DEL ARCHIVO, no con mi gusto:** barrido hoy
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` entero, **los 207 veredictos cuya razon nombra ARISTA QUE
> FALTA son `D`, los 207**. Y **medido hoy en los dos sentidos, ninguno de los dos pares tiene
> arista**, que es lo que la razon del 592 ya decia (*sin arista*) y lo que el 830 no habia
> mirado.

#### LO QUE ESTA VUELTA **NO** ESCRIBE, y por que

> ~~**LAS TRES CLASES NUEVAS NO SE ESCRIBEN EN `INTRA_DOMINIO_VEREDICTOS.jsonl` EN ESTA VUELTA, y
> no es timidez: es la letra de la propia operacion.** El campo `preservar` de `OP-D-01`, en su
> correccion declarada del 15 ago 2026, dice: *si la relectura diera par nuevo, **entra por el
> recomputo (banco 9.10)**, no se decide aqui de antemano*. **Volcarlas movería el marcador
> publicado** (`A 583, B 89, C 7, D 2709` medido hoy al abrir esta vuelta) **y obligaria a
> barrer en el mismo acto todas las tablas derivadas que citan esos tres numeros**, que es
> exactamente lo que el 9.10 exige y lo que ninguna operacion de la fase 02 tiene escrito.
> **Las tres lecturas quedan publicadas aqui con su evidencia, y la escritura va al recomputo.**~~

#### LO QUE LA VUELTA 33 **SI** ESCRIBIO: EL VOLCADO, POR EL CARRIL QUE FALTABA

> **CORRECCION DECLARADA (15 ago 2026, vuelta 33). EL PARRAFO DE ARRIBA SE QUEDA ENTERO Y
> TACHADO: describia bien la situacion del 15 ago por la manana, y lo que cambio no fue la
> lectura sino que APARECIO EL CARRIL.** El `preservar` mandaba las tres clases *al recomputo
> (banco 9.10)* y **ninguna operacion de la fase 02 lo tenia escrito**; eso quedo publicado como
> pendiente de doctrina, y **el fundador lo adjudico: el `9.10` ES el mecanismo**, sin operacion
> nueva. Con esa letra, esta vuelta **volco las tres y barrio en el mismo acto**.
>
> | puesto | par | antes | ahora | el arreglo que queda escrito |
> |---:|---|:---:|:---:|---|
> | **494** | `principio_calidad_mvp` contra `producto_minimo_viable` | **A** | **C** | **ENLACE MUTUO, dos aristas** (banco `9.22`, **tercer ejemplar** del archivo) |
> | **592** | `mvp_catalogo_tecnicas` contra `producto_minimo_viable` | **B** | **D** | **ARISTA QUE FALTA** hacia `mvp_catalogo_tecnicas` |
> | **830** | `producto_minimo_viable` contra `prueba_mvp_alta_fidelidad` | **B** | **D** | **ARISTA QUE FALTA** hacia `prueba_mvp_alta_fidelidad` |
>
> **EL MARCADOR, RECOMPUTADO CON EL INSTRUMENTO DE LA CASA Y NO TECLEADO** (`python
> scripts/corregir_veredicto.py docs/loop/_lote_v33.jsonl`, salida
> `docs/loop/SALIDA_V33_MARCADOR.txt`):
>
> | | apertura de la vuelta 33 | tras el volcado |
> |---|---:|---:|
> | n | 3.388 | **3.388** |
> | A | 583 | **582** |
> | B | 89 | **87** |
> | C | 7 | **8** |
> | D | 2.709 | **2.711** |
>
> **La cifra esperada se escribio ANTES de correr el instrumento** (`SALIDA_V33_LOTE.txt`, ultima
> linea: *n 3388, A 582, B 87, C 8, D 2711*) **para que la comprobacion valiera algo**, con la
> orden de PARAR si daba otra cosa. **Dio exactamente eso.**
>
> **LAS TRES RAZONES SE REESCRIBIERON CON LA VIEJA DENTRO, copiada por maquina y no transcrita**
> (`scripts/loop/vuelta33_volcado_910.py`, que **aborta si la razon vieja no queda literalmente
> dentro de la nueva**): 865, 1.359 y 962 caracteres de razon vieja conservados.
>
> **EL BARRIDO DEL `9.10`, EN EL MISMO ACTO** (`scripts/loop/vuelta33_barrido_910.py`, salida
> `docs/loop/SALIDA_V33_BARRIDO_910.txt`, **77 candidatos listados sin ocultar ninguno**). Lo
> corregido, por documento:
>
> | documento | que se corrigio |
> |---|---|
> | `docs/INTRA_DOMINIO_INFORME.md` | el marcador de `100.1`, la tasa por dominio de `100.2` (fila `core`, la unica que se mueve) y el *total de A en el archivo* de `100.6` |
> | `docs/PENDIENTES.md` | la tabla de congelados (13 a **10**), la de cola (19 a **16**), la de pares que libera `producto_minimo_viable` y la de *clase hoy* de los tres |
> | `docs/plan/RECOMPUTO_3388.md` | **el instrumento se volvio a correr entero** y se publico el delta: A 583 a **582**, nodos con A 854 a **852**, componentes 335 a **334**, cerradas 280 a **279**. **Las cuatro comprobaciones vuelven a dar OK** |
> | `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` | **reescrito por el propio instrumento**: muere la componente de tamano 2 de `principio_calidad_mvp` con `producto_minimo_viable` |
> | `docs/plan/02_DESTEJIDOS.md` | esta seccion, la tabla del orden, el bloque del 494 congelado y la tabla del movimiento 4 |
>
> **Y LO QUE EL BARRIDO **NO** TOCO, dicho con su motivo y no callado:** las **trece** filas de
> checkpoints anteriores del informe que citan `core` con **A 344**, y las salidas viejas de
> `docs/loop/`. **Cada una es la foto de su propio corte**, y reescribirlas fabricaria corridas
> que nunca existieron. **Queda como PENDIENTE DE DOCTRINA: ninguna pagina dice hasta donde atras
> alcanza el barrido del `9.10`.**
>
> **LAS TRES ARISTAS SIGUEN SIN PONERSE**, y eso no cambia: el campo `aristas_nuevas` de
> `OP-D-01` sigue **vacio** y los enlaces son la **fase 04**. Lo que esta vuelta cerro es la
> CLASE, no el CABLEADO.

> **LAS TRES ARISTAS TAMPOCO SE PONEN**, por el mismo motivo de letra: el campo `aristas_nuevas`
> de `OP-D-01` esta **VACIO**, y los enlaces son la **fase 04** del indice, que va despues de
> los destejidos y de las fusiones. **Quedan declaradas aqui, con su sentido y su motivo, para
> que la fase 04 las encuentre escritas y no las tenga que redescubrir.** **(SIGUE VIGENTE AL 15
> ago 2026, vuelta 33: el volcado de clases NO puso ninguna arista.)**

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

### `OP-D-02` EJECUTADA (15 ago 2026, vuelta 33). **LA PARADA DE LA VUELTA 32 QUEDA LEVANTADA**

**Nada de esta seccion viene de un acta ni de un reporte: todas las cifras salen de instrumentos
corridos en esta misma vuelta, con su salida en `docs/loop/`.** La seccion de la parada se queda
entera debajo, sin tocar, porque describe bien el estado del que se partio.

#### LO QUE DESTRABO LA PARADA: sus tres motivos, uno por uno

| motivo de la parada (vuelta 32) | como se resolvio |
|---|---|
| **1.** el acto tenia **3 de 6** pares internos leidos, y `P.5` no se puede contestar con eso | **LEIDOS LOS TRES QUE FALTABAN** como lecturas dirigidas `LD-72`, `LD-73` y `LD-74`, adjudicadas por el fundador. **6 de 6.** Ninguno estaba en la cola, asi que **`n` no se movio**: sigue en 3.388 |
| **2.** no habia superviviente ni escrito ni deducible | **FIJADO en `voz_del_cliente_voc`** por `P.8`, contenido primero. Y la cifra del motivo se corrigio antes: **cero de tres pares A nombran ganador**, no dos de tres |
| **3.** la nomina podia estar corta | **MEDIDO Y RESUELTO SIN AMPLIARLA**, y por lectura: los dos de fuera (`voice_of_customer_estrategico` y `voc_temprano_en_agile_stage_gate`) no entran, porque el primero se releyo hoy en el **724** y dio **`D`**, no `A`. **`P.6` no se dispara** |

#### LA RESPUESTA DE `P.5`, y cambia el ALCANCE de la fusion

**El acto NO es una familia.** Con los seis pares leidos, sus tres `A` forman **un CAMINO** (386,
788, 526) y **las tres cuerdas largas son `D`**: **cero triangulos cerrados**, y **DOS nodos
puente** (`enfoque_mercado_voc` y `voice_of_customer_homework`), que es el **segundo puente doble
del archivo** por `P.10`. La salida que `P.10` nombra para ese caso es **fundir solo el
subconjunto cerrado y enlazar el resto**, y el subconjunto cerrado es **el par del puesto 386**.

> **`homework_frontend_loading` y `voice_of_customer_homework` NO ENTRAN EN LA FUSION**, y eso no
> reduce la operacion: **es lo que su punto 4 siempre dijo**, *tener delante*. El campo `nodos`
> **no se toca**, porque la nomina es el universo del acto que hay que leer junto (`9.24` con
> `P.12`), no la lista de lo que se funde. **El cierre transitivo es la citacion, no la
> sentencia.** El desarrollo entero esta en `LECTURAS_DIRIGIDAS.md`, octava tanda.

#### LA FUSION, y es **LA PRIMERA DEL PLAN QUE SE ESCRIBE CONTRA `dataset/`**

**`voz_del_cliente_voc` pasa de CINCO pasos a SEIS y absorbe a `enfoque_mercado_voc`**, que queda
**deprecado con su texto INTACTO y su fichero en pie**. Plan sellado en
`docs/loop/PLAN_V33_OPD02_FUSION.json`, construido por `scripts/loop/vuelta33_plan_opd02.py` (los
textos originales, los prefijos y las fuentes **se leen del grafo, no se teclean**) y ejecutado
con `scripts/loop/vuelta33_fundir.py`.

**EL `preservar` ENTRO INTEGRO, y el instrumento aborta si alguna pieza falta**: la evaluacion
preliminar de mercado, el analisis competitivo detallado, y probar los conceptos con clientes
reales antes del desarrollo formal. **Las tres verificadas LITERALES en el resultado.**

**LA TABLA DE LOS SEIS MOTIVOS. Solo DOS de los cinco pasos del absorbido producen perdida**, y se
dice por que: **tres son el `preservar`**, y el `preservar` no es perdida repartida, es material
salvado por mandato de la operacion.

**NO ESTA TECLEADA: esta IMPRESA desde el plan sellado** (`EJECUTOR.md` regla 1, cuarto
renglon). **Comando, corrido en esta vuelta:**

```
python scripts/loop/vuelta33_tabla_mapa.py docs/loop/PLAN_V33_OPD02_FUSION.json
```

salida entera en `docs/loop/SALIDA_V33_TABLA_OPD02.txt`, pegada aqui sin editar una coma.
**Los origenes llevan PREFIJO porque aqui hay DOS fuentes**: `S` el superviviente, `A` el
absorbido. Un numero suelto no diria de cual viene.

| paso del resultado | de que origenes sale | el motivo de perdida de linea que lo modifica |
|---:|---|---|
| **1** | S1, A1 | SALVAGUARDA: el superviviente manda observar a tus clientes y no dice a CUALES, asi que el paso se resuelve solo por el sesgo por defecto, observar a los que estan mas a mano. El absorbido dice contra que sesgo se elige (los mas exigentes) y el inciso se adosa al paso que protege, que es un paso de DECISION y no de ejecucion, que es la firma escrita de la clase. |
| **2** | S2 | VERBATIM: el superviviente conserva su paso entero y el absorbido no le anade nada. |
| **3** | S3 | VERBATIM: el superviviente conserva su paso entero. Aqui vive el 'hazles entrevistas a fondo' del absorbido, que ya decia lo mismo. |
| **4** | A2, A3 | NO ES PERDIDA: es PRESERVAR. El campo preservar de OP-D-02 manda salvar de enfoque_mercado_voc la evaluacion preliminar de mercado y el analisis competitivo detallado, y el superviviente no dice ninguna de las dos en ninguno de sus cinco pasos. Entra como PASO NUEVO porque no hay paso del superviviente al que adosarlo sin cambiarle el objeto. |
| **5** | S4, A4 | NO ES PERDIDA: es PRESERVAR, la tercera pieza. El campo preservar manda salvar probar los conceptos con clientes reales antes del desarrollo formal, y se adosa al paso del superviviente que ya habla de usar lo observado para disenar, que es el mismo momento del proceso. |
| **6** | S5, A5 | ALCANCE: el superviviente manda mantener el contacto durante todo el desarrollo y no dice a que cadencia. El absorbido la trae (ciclos cortos) y entra a la enumeracion que el superviviente ya tiene. Es la misma lectura de cadencia que OP-D-01 aplico en el sexto paso de su propia tabla, y se cita para que el criterio sea el mismo. |

**`NOMBRE`, `DESTINO`, `METODO ALTERNATIVO` y `DIRECCION` no aplican, y por eso no se nombran.**

**Y las condiciones pasan de 3 mas 2 a TRES**, con **`ALCANCE`** en la tercera (el superviviente
nombraba un solo momento, *antes de la etapa formal*, y el absorbido trae el otro, *mientras
avanzas sin retroalimentacion externa*). **El entregable absorbe lo que el nodo ahora si produce**:
la evaluacion preliminar de mercado, el analisis competitivo y los resultados de las pruebas de
concepto. **La fuente NO cambia: los dos eran del mismo libro.**

| guarda | resultado |
|---|---|
| simulacion previa sobre copia en memoria (`P.7`) | **verde**, y ademas la del instrumento sellado de la casa `scripts/plan/simular_fusion.py` |
| guarda de texto sobre pasos **y** condiciones de los DOS nodos | **15 de 15** calzan con su prefijo sellado |
| cero perdida, cobertura exacta | **10 de 10** origenes en pasos, **5 de 5** en condiciones |
| el `preservar`, literal en el resultado | **3 de 3** |
| **caso positivo ANTES** | **10 PASAN, 13 CAEN** (`SALIDA_V33_OPD02_CASO_ANTES.txt`) |
| **caso positivo DESPUES** | **23 PASAN, 0 CAEN** (`SALIDA_V33_OPD02_CASO_DESPUES.txt`) |
| conservacion (pasa las dos veces a proposito, contada aparte) | **de 3 a 10 rastros vivos de 10** |
| cero auto arista y cero duplicada, en TODO el grafo | **OK** |
| **el censo no se mueve** | **3.853 ficheros antes y despues**: una fusion **depreca, no borra** |

> **UNA GUARDA CAZO UNA DISCREPANCIA REAL Y SE DECLARA, porque es lo unico que prueba que las
> guardas sirven.** El plan sellado esperaba **TRES** redirecciones, que son las que da el
> instrumento de la casa sobre el grafo compilado; **el ejecutor, contando sobre `dataset/nodos`,
> encontro CUATRO**, y **aborto sin escribir**. La cuarta es `front_end_homework`, que **esta
> DEPRECADO**. Se adopta el criterio del instrumento sellado (**solo se redirige lo vivo**, su
> linea 87) y **la cuarta va DECLARADA en el plan, no filtrada en silencio**: el cableado de un
> nodo deprecado es registro historico, y se conserva por la misma razon por la que se conserva el
> texto del absorbido.

**Ciclo de `Gate 0`, entero y en su orden:** `run_phase1.py --reaplico-curaduria` **exit 0,
`GATE 0: OK`**, **3.853 nodos compilados**, y el universo pasa a **3.538 activos y 315 deprecados**
(antes 3.539 y 314), **que es exactamente la fusion y nada mas**; `etiquetas_de_cara.py --aplicar`
**71 etiquetas**; `plan_readiness.py` **3.853 nodos**; `sync_assets_web.py` verde. **Suites: motor
24 de 24, web 80 ficheros con 1.030 pasadas y 3 saltadas, `tsc --noEmit` cero lineas.**

#### LA CAIDA `6.1` **CERRADA** (15 ago 2026, vuelta 34), y con ella la redireccion queda ESTABLE

**REGISTRO DE LAS DOS PIEZAS QUE LA CERRARON, cada una por su fecha.** El **acta de la vuelta 33
del auditor** (15 ago 2026, Fable 5, `docs/loop/ACTA_AUDITOR.md`, seccion 6) declaro la
**PREGUNTA 1** no adjudicable por extension: *un nodo deprecado, conserva su cableado o no.
Ninguna pagina lo dice*. Y la **decision del fundador** (15 ago 2026,
`docs/loop/paradas/2026-08-15-cableado-deprecado-y-costuras.md`, ultimo parrafo) la contesta por
la **opcion a**: *el deprecado conserva su cableado como archivo y `Gate 0` deja de reciprocar
aristas que nacen en deprecados*.

**QUE SE TOCO DEL INSTRUMENTO SELLADO, y es una sola regla en dos funciones.** En
`scripts/run_phase1.py` nace `aristas_a_simetrizar(nodes)`, funcion **pura**, que es la que
decide que arista se completa: **entra la que declara un nodo VIVO**, en cualquiera de sus dos
vistas. `step5_symmetrize` y `count_asymmetric_edges` **leen las dos la misma funcion**, y eso no
es comodidad: un Gate que exigiera simetria en aristas que el paso 5 ya no simetriza se pondria
rojo por su propia politica, **y la salida barata seria aflojar la comprobacion**.

> **LA LECTURA ES POR DECLARACION, NO POR ORIGEN TOPOLOGICO, y la diferencia se dice porque es lo
> unico que resuelve el sintoma:** si se leyera por el extremo *antes*, una arista declarada por
> un vivo **hacia** un deprecado seguiria escribiendo el id del muerto dentro del vivo. **Lo que
> se exime es lo que UNICAMENTE dice un muerto.**

**EL CASO POSITIVO, EN ROJO Y EN VERDE, con la regla vieja viviendo dentro de la prueba**
(`engine/test_gate_deprecado_reciproco.py`, corrido hoy, salida en
`docs/loop/SALIDA_V34_CASO_RECIPROCADO.txt`): sobre el fixture con la figura exacta de una fusion,
**la regla vieja devuelve 2 aristas del muerto a los vivos** y **la nueva ninguna**; y la prueba
**exige que la vieja falle**, porque una prueba que solo mira la version nueva no distingue *la
regla esta puesta* de *la averia nunca existio*.

| medicion de hoy | resultado |
|---|---|
| censo previo sobre `dataset/nodos` (`scripts/loop/vuelta34_reciprocado.py`) | **110** aristas con su unica declaracion en un deprecado, **las 110 de deprecado a deprecado** y **0 tocando a un vivo**: al correr el censo, el Gate ya habia devuelto las tres |
| redireccion rehecha (`scripts/loop/vuelta34_redirigir.py`, seis guardas) | **3 sitios vivos**, **0** que quedaran nombrando al absorbido; el cableado del archivo, **intacto**, y sus **5 pasos** sin tocar |
| **caso positivo ANTES de rehacerla** | **22 PASAN, 1 CAE** (`SALIDA_V34_OPD02_CASO_ANTES.txt`), el mismo rojo que la vuelta 33 publico |
| `Gate 0` tras el arreglo, **paso 5** | **0 nodos actualizados, 0 vistas completadas**: ya no hay nada que devolver |
| **caso positivo DESPUES del ciclo entero de `Gate 0`** | **23 PASAN, 0 CAEN** (`SALIDA_V34_OPD02_CASO_TRAS_GATE0.txt`). **Esta es la cifra que prueba estabilidad**, porque se mide donde la otra caia |

**Ciclo de `Gate 0` entero:** `GATE 0: OK`, **20 comprobaciones `[OK]`, 0 `[FALLO]`**, 3.853
compilados, **3.538 activos y 315 deprecados**, simetria **0**; `etiquetas_de_cara --aplicar` 71;
`sync_assets_web` verde. **Suites: motor 25 de 25** (el fixture nuevo es el 25), **web 80 ficheros
con 1.030 pasadas y 3 saltadas**, **`tsc --noEmit` cero lineas**. La correccion va tambien
**dentro del plan sellado**, en su bloque `correcciones_declaradas`, **con la cifra vieja de 22 de
23 escrita dentro** (`scripts/loop/vuelta34_declarar_plan.py`).

> **LO QUE ESTO NO DICE:** no dice que el caso positivo de la vuelta 33 estuviera mal medido.
> **Estaba bien medido, y por eso se publico en rojo.** Lo que cambio es el instrumento de debajo.

#### LOS TRES CONGELADOS, RELEIDOS Y VOLCADOS por el carril del `9.10`

**Los tres estaban en `B` por el TOQUE UNICO del banco `9.4` y esa causa cayo hoy**: el
superviviente quedo estable. **Releidos contra sus SEIS pasos de hoy y volcados en el mismo acto**
(`scripts/loop/vuelta33_volcado_910_b.py`, con la razon vieja copiada por maquina dentro de la
nueva y el script abortando si no queda):

| puesto | contra quien | lo que el otro trae y el superviviente sigue sin decir | clase volcada |
|---:|---|---|:---:|
| **724** | `voice_of_customer_estrategico` | el **PROTOCOLO DE INTERROGACION Y REGISTRO**: que problemas enfrentan y **que los mantiene despiertos por la noche**, el **porque** detras de cada peticion, las **necesidades FUTURAS**, y documentar los **ahas**. Madre e hijo, con **ARISTA QUE FALTA** | **`D`** |
| **755** | `dia_en_la_vida_del_cliente` | **PROYECTAR** como cambiaria el dia con el producto, repetir por **CADA figura de la decision**, y **presentar al equipo** el antes y el despues en narrativa o storyboard. Dos objetos distintos, con **ARISTA QUE FALTA** | **`D`** |
| **827** | `ganar_comprension_del_cliente` | el **flujo de trabajo**, que otras soluciones usa, **que haria cambiar su comportamiento de compra**, que publicaciones lee y **criterios claros de que cuenta como validado**. **SIN arista declarada**, y se dice por que | **`D`** |

##### EL CRITERIO DE LA `ARISTA QUE FALTA` DE ESTA TANDA, ESCRITO UNA SOLA VEZ (15 ago 2026, vuelta 34)

**Encargado por el acta de la vuelta 33 del auditor** (seccion 4, punto 8: *el criterio es el
`9.6.1` y el `9.6.2` aplicados, no doctrina nueva, pero debe quedar escrito UNA VEZ donde las
tres razones lo compartan*), **y por el punto 1.4 del encargo del 15 ago 2026.** Va aqui, bajo la
tabla que junta a los tres, **y no dentro de cada razon**: escribirlo tres veces seria escribirlo
tres veces distintas, que es de donde salen las divergencias.

> **LA VARA ES EL TAMANO DE LO COMPARTIDO, no la formula.** Se declara `ARISTA QUE FALTA` cuando
> lo compartido es un **BLOQUE**: un procedimiento entero que uno de los dos expande de una linea
> del otro. **No se declara cuando lo compartido es UNA LINEA contra UNA LINEA** y los dos nodos
> ya tienen cableado propio denso, porque un enlace por una sola linea infla el grafo sin
> ensenarle nada al lector.

**Y LOS TRES CASOS DE LA TANDA, con lo que cada uno midio, porque el criterio se lee mejor en sus
ejemplares que en su enunciado:**

| puesto | que es lo compartido, medido | arista |
|---:|---|:---:|
| **724** | **madre e hijo del `9.6.2`**: el paso 1 del superviviente enuncia en UNA LINEA el prepararse para observar, y el otro trae **el protocolo entero** de esa linea | **SE DECLARA** |
| **755** | **NO hay madre e hijo** (se midio y se dijo: el hijo no cabe entero dentro de un paso del otro), pero lo compartido **sigue siendo un bloque**: el arranque de campo cubre **tres pasos** del superviviente | **SE DECLARA** |
| **827** | **UNA linea contra UNA linea**: *pasar un dia haciendo lo que hace tu cliente* contra *observar acompanandolo durante su trabajo real*, y los dos con cableado propio denso | **NO se declara** |

> **UNA PRECISION QUE EL ENUNCIADO DEL ENCARGO NO CUBRE, y se dice en vez de forzar el calce.** El
> encargo escribio el criterio como *se declara donde hay madre e hijo del `9.6.2`; no se declara
> donde el solape es linea contra linea*. **Eso nombra los dos EXTREMOS, el 724 y el 827, y deja
> fuera al 755**, que no tiene madre e hijo y sin embargo lleva arista. **La vara que cubre a los
> tres es la de arriba: bloque contra linea.** Madre e hijo es **un caso** de bloque compartido,
> **el mas nitido**, no la condicion.

> **Y LA PRACTICA MEDIDA DEL ARCHIVO SIGUE SIENDO LA MISMA** (barrido de la vuelta 33 sobre
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`): **los 207 veredictos cuya razon nombra `ARISTA QUE
> FALTA` son `D`, los 207.** La arista que falta **no cambia la clase**: la acompana.

> **LA GUARDA DEL ENCARGO, COMPROBADA Y NO SUPUESTA:** si el **724** hubiera dado **`A`**,
> `voice_of_customer_estrategico` habria entrado al acto por `P.6` y **habia que PARAR**, porque
> una fusion nueva sin operacion escrita no se improvisa. **NO DA `A`**, y por eso la vuelta sigue.

> **Y AQUI HAY UNA LECCION DE METODO QUE LA VUELTA NO BUSCABA:** **antes de la fusion, el 724
> estaba mucho mas cerca de `A`**, porque el superviviente era solo la observacion de campo. **Fue
> la fusion la que lo separo**, al darle el tramo de mercado. **Es exactamente por lo que el banco
> `9.4` congela: el mismo par da dos clases distintas segun el dia en que se lea.**

**EL MARCADOR, recomputado con el instrumento y con la cifra esperada escrita ANTES de correrlo,
las dos veces** (`SALIDA_V33_MARCADOR.txt` y `SALIDA_V33_MARCADOR_B.txt`):

| | apertura de la vuelta 33 | tras la tarea 1.3 | **al cierre** |
|---|---:|---:|---:|
| n | 3.388 | 3.388 | **3.388** |
| A | 583 | 582 | **582** |
| B | 89 | 87 | **84** |
| C | 7 | 8 | **8** |
| D | 2.709 | 2.711 | **2.714** |

---

### `OP-D-02`, ESTADO AL 15 ago 2026 (vuelta 32): **PASO 1 CONSUMIDO, FUSION EN PARADA**

> **SECCION SUPERADA POR LA DE ARRIBA (15 ago 2026, vuelta 33), y NO SE BORRA: describe bien el
> estado del que esta vuelta partio, y sus tres motivos son los que la vuelta 33 tuvo que
> levantar uno por uno.** Su cifra del motivo 2 lleva su propia correccion declarada, mas abajo.

**El paso 1 del orden interno esta HECHO y no lo hizo esta operacion: lo hizo `OP-F-04-COL`
en la vuelta 31.** Medido hoy sobre el arbol: `voz_del_cliente_voc` tiene **5 pasos y fuente
UNICA** (*Winning at New Products - Robert G. Cooper*), y el bloque 6 a 10 que el campo
`preservar` manda hacer viajar entero vive en `observar_al_cliente_en_su_contexto`, nodo propio
nacido en esa vuelta con **5 pasos y fuente unica Coleman**. **El destejido NO se repite**, y la
readjudicacion esta escrita como correccion declarada en la `nota` de la operacion.

**LA FUSION NO SE EJECUTA, y son TRES motivos medidos hoy, ninguno adivinado**
(`scripts/loop/vuelta32_acto_opd02.py`, de solo lectura; salidas en
`SALIDA_V32_OPD02_ACTO.txt` y `SALIDA_V32_PARADA_OPD02.txt`). **Cero nodos tocados.**

**MOTIVO 1, y lo exige la verificacion de la propia operacion**, que pide con estas palabras
*el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto*. **Medido par por
par: PARES POSIBLES 6, CON VEREDICTO 3, SIN VEREDICTO 3.** Los tres que faltan, por su nombre,
porque una ausencia no se afirma en bloque:

| par interno sin veredicto |
|---|
| `enfoque_mercado_voc` contra `homework_frontend_loading` |
| `homework_frontend_loading` contra `voz_del_cliente_voc` |
| `voice_of_customer_homework` contra `voz_del_cliente_voc` |

> **Y `P.5`, que la nota de la operacion cita, dice que la pregunta que el acto leido entero
> contesta es SI EL ACTO ES UNA FAMILIA O DOS. Con 3 de 6 esa pregunta no tiene respuesta
> medida.** Los tres que si tienen veredicto son los **tres pares A** del acto: **386, 526 y
> 788**, y su cierre transitivo cubre a los **cuatro** nodos de la nomina, sin ninguno fuera.

**MOTIVO 2: NO HAY SUPERVIVIENTE, ni escrito ni deducible.** El campo `superviviente` de
`OP-D-02` esta en **`null`**, leido hoy en el fichero. Y no se puede fijar por el banco `9.3.1`
(GANADOR POR DERECHO contra GANADOR POR ELEGIR, con la correccion del 18 ago 2026 que define el
acto como el cierre transitivo de las A): la prueba es *gano todos los pares A que lo tocan*, y
~~**medido hoy, DOS de los tres pares A no nombran ganador en su razon** (386 y 788)~~ **FRASE
VIEJA, TACHADA Y NO BORRADA: ver la correccion declarada debajo**. **Ningun nodo del acto tiene
una victoria citable**, asi que no hay ganador por derecho; y la otra especie, **por elegir,
exige `P.8` sobre la nomina entera CON EL ACTO COMPLETO delante**, que es justamente lo que el
motivo 1 dice que no hay.

> **CORRECCION DECLARADA (15 ago 2026, vuelta 33). LA CIFRA BUENA ES CERO DE TRES, NO DOS DE
> TRES: NINGUNO de los tres pares A nombra ganador.** La conclusion que la frase sostenia
> (*ningun nodo del acto tiene una victoria citable*) **no cambia; cambia la cuenta que la
> sostiene, y una cuenta mal publicada se corrige aunque apunte al mismo sitio.**
>
> **LA CAUSA, MEDIDA Y NO SUPUESTA, y es de la misma especie que la del origen 16.** El detector
> de ganador de `scripts/loop/vuelta32_acto_opd02.py` preguntaba `"gana" not in razon.lower()`:
> **un SUBSTRING**. Y el substring `gana` vive dentro de `ganar`. **La razon del puesto 526 dice
> *saltarse la validacion por GANAR TIEMPO***, y el detector leyo ahi un ganador que no existe.
> El instrumento nuevo (`scripts/loop/vuelta33_acto_opd02.py`) **imprime la palabra culpable por
> su nombre**: `FALSO POSITIVO, y aqui esta la palabra: 'ganar'`.
>
> **LAS DOS CORRIDAS SE PUBLICAN Y LA DIFERENCIA SE DECLARA, en vez de resolverse sustituyendo**
> (salida entera en `docs/loop/SALIDA_V33_OPD02_ACTO.txt`, corrida en esta vuelta):
>
> | detector | pares A que nombran ganador |
> |---|---:|
> | **VIEJO**, substring `gana` | **1 de 3** |
> | **NUEVO**, vocabulario de adjudicacion con frontera de palabra | **0 de 3** |
>
> **Y LA PRUEBA DEL 9.3.1, NODO POR NODO, con la cifra corregida:** `enfoque_mercado_voc` 2
> pares A y 0 victorias citables; `voice_of_customer_homework` 2 y 0;
> `homework_frontend_loading` 1 y 0; `voz_del_cliente_voc` 1 y 0. **NO HAY GANADOR POR DERECHO,
> y ahora se puede decir con los tres pares contados y no con dos.**
>
> **DOS COSAS QUE NO SE TOCAN, y se dice por que.** La `nota` de `OP-D-02` en
> `OPERACIONES.jsonl` **queda como esta**: leida hoy entera, **no afirma que el 526 nombre
> ganador**, nombra al 386 y al 788 y concluye *ningun nodo del acto tiene una victoria
> citable*, que es la conclusion correcta. Y `docs/loop/SALIDA_V32_PARADA_OPD02.txt` **tampoco
> se reescribe**: es la salida de un instrumento corrido aquel dia, **y una salida vieja se
> contrasta, no se maquilla**. La corrigen las dos corridas de la tabla de arriba.
>
> **EL LIMITE DEL DETECTOR NUEVO, declarado donde se lee:** sigue siendo una busqueda **lexica**
> y no un lector de espanol. Una razon puede adjudicar sin usar ninguna de las palabras del
> vocabulario. **Por eso el instrumento imprime la razon ENTERA de cada par A**: la vara final
> es la lectura, y la lectura necesita el texto delante.

**MOTIVO 3: LA NOMINA PUEDE ESTAR CORTA, y el aviso ya estaba escrito.** La razon del puesto
**788**, leida hoy, cierra asi: *la voz del cliente ya lleva cuatro nodos vistos en el cribado
(...). Hay que contarla entera antes de tocarla*. **Censo por nombre corrido hoy (banco 9.5.1),
y se dice lo que es: una CITA, no una prueba de pertenencia.** De los 9 nodos vivos que
contienen alguna marca buscada, **cuatro son falsos positivos del substring `voc`**
(`advocacy_customer_journey`, `centro_asesoria_advocacy_center`,
`incentivos_no_monetarios_advocacy`, `voces_externas_credibles`). Quedan **cinco** con la marca
de verdad y **DOS estan FUERA de la nomina**: `voice_of_customer_estrategico` y
`voc_temprano_en_agile_stage_gate`, **los dos del mismo libro que los cuatro de la nomina**, y
el primero es ademas el contrario del congelado **724**.

**Y POR ESO LAS RELECTURAS DE 724, 755 Y 827 SE LEEN PERO NO SE CLASIFICAN.** Los tres estan
congelados por el **TOQUE UNICO del banco `9.4`**: *un veredicto emitido contra un texto que va
a cambiar no vale*. **La mitad de esa causa ya cayo** (`voz_del_cliente_voc` esta destejido y
estable), **pero la otra mitad sigue en pie**: si la fusion de este acto se ejecuta, el
superviviente **puede no ser `voz_del_cliente_voc`**, y las tres relecturas se habrian emitido
contra un texto que iba a cambiar otra vez. **Emitirlas hoy seria romper la misma regla por la
que estan congelados.** Quedan leidas, con lo que cada contrario aporta medido contra el texto
de hoy (`SALIDA_V32_OPD02_RELECTURA.txt`), **y sin clase**.

---

## `OP-D-03`: LAS PRUEBAS A/B · **LISTA**

### PASO 1 DEL ORDEN INTERNO **HECHO** (15 ago 2026, vuelta 34): **DOS costuras estaban CONSUMIDAS y la tercera se destejio**

**La parada de la vuelta 33 queda levantada, y no por donde se esperaba.** Se levanta por la
decision del fundador del 15 ago 2026 (`docs/loop/paradas/2026-08-15-cableado-deprecado-y-
costuras.md`), que mando recalibrar el instrumento; **pero el destejido no lo desbloqueo el
instrumento recalibrado, que sigue sin pasar su propia puerta. Lo desbloqueo una CAIDA DE
REPORTE de la vuelta 33 que se corrige aqui.**

> **CORRECCION DECLARADA (15 ago 2026, vuelta 34), y es una caida de REPORTE de la vuelta 33. El
> texto viejo se queda entero debajo.** El **MOTIVO 2** de la parada dice: *la nomina de esas
> tres no esta escrita en ninguna parte por su nombre: sale del instrumento*. **ESTA ESCRITA, y
> en este mismo documento, ochenta lineas mas abajo del propio motivo**, desde la primera entrega
> del plan (commit `23f9ac32`, medido hoy con `git log -L`):
>
> ```
> **Acto 2. SEIS nodos y TRES destejidos.** Costuras: `ab_testing_optimizacion`,
> `optimizacion_embudo_get_customers`, `split_testing_experimentos_ab`. Sanos:
> `funnel_get_customers_optimizacion`, `split_testing`, `test_ab_precio`.
> ```
>
> **La cita la comprueba un instrumento, no un recuerdo:** `scripts/loop/vuelta34_costuras_
> opd03.py` **aborta si esa linea no esta en el documento o si le falta uno de los tres nombres**
> (salida en `docs/loop/SALIDA_V34_OPD03_COSTURAS.txt`). **El instrumento de costuras nunca fue
> la fuente de la nomina: era el contraste.**

**Y MEDIDAS HOY LAS TRES, DOS YA ESTABAN CONSUMIDAS POR LA FASE 01**, exactamente como le paso al
paso 1 de `OP-D-02`. **Cada una con su frontera escrita, su huella medida en el nodo de hoy y la
operacion que se llevo el bloque:**

| costura declarada | frontera escrita (`01_FUENTES.md`) | pasos hoy | la huella del bloque | estado |
|---|---|---:|---|---|
| `optimizacion_embudo_get_customers` | **1 a 5 / 6 a 10** sobre 10 pasos | **5** | *middle ring testing*: **YA NO ESTA** | **CONSUMIDA** por `OP-F-04-WEI` |
| `split_testing_experimentos_ab` | **1 a 5 / 6 a 9** sobre 9 pasos | **5** | *cambio porcentual*: **YA NO ESTA** | **CONSUMIDA** por `OP-F-04-RAC` |
| `ab_testing_optimizacion` | **1 a 10 / 11 a 15** sobre 15 pasos | **10** | *punto de saturacion*: **YA NO ESTA** | **EN PIE**: le queda la costura de dentro del tramo 1 a 10 |

**EL CAMPO `preservar` DE LA OPERACION, COMPROBADO DONDE VIVE HOY y no dado por bueno:** la
significancia estadistica del 95 por ciento vive en `split_testing`; el **cambio porcentual** y el
**grupo de control con nivel de desempeno inicial similar** viven en
`metodologia_evaluacion_entrenamiento_ventas`, **que es a donde `OP-F-04-RAC` los mando**. **Los
tres, en UN solo nodo vivo cada uno.** El `preservar` decia *se van CON EL DESTEJIDO: no se
pierden*, y **medido hoy no se perdieron**.

#### EL DESTEJIDO QUE QUEDABA: `ab_testing_optimizacion`, **de DIEZ pasos a CINCO**

**Su frontera tampoco se adivina: la escribio la tabla de fronteras de `OP-F-04-WEI`** en
`01_FUENTES.md` linea 947, en la misma fila del nodo: *Nota de costura: **los pasos 1 a 5 y 6 a 10
dicen la misma prueba A/B dos veces**, y eso es material de la fase 02, no de esta*.

**EL CRITERIO DEL SUPERVIVIENTE ES EL DE `OP-D-01`, citado y no inventado: de cada grupo de
repeticion sobrevive EL DE INDICE MAS BAJO.** Aqui cae entero sobre el bloque **1 a 5**, que es
ademas **la narracion del unico libro que el nodo declara como fuente**. Plan sellado en
`docs/loop/PLAN_V34_OPD03_AB.json`, construido por `scripts/loop/vuelta34_plan_opd03.py` (**los
textos, los prefijos y la fuente se leen del grafo**) y ejecutado con el instrumento sellado de la
casa `scripts/loop/vuelta32_podar.py`.

**LA TABLA NO ESTA TECLEADA: esta IMPRESA desde el plan sellado** (`EJECUTOR.md` regla 1, cuarto
renglon). **Comando, corrido en esta vuelta:**

```
python scripts/loop/vuelta33_tabla_mapa.py docs/loop/PLAN_V34_OPD03_AB.json
```

salida entera en `docs/loop/SALIDA_V34_TABLA_OPD03.txt`, pegada aqui sin editar una coma:

| paso del resultado | de que origenes sale | el motivo de perdida de linea que lo modifica |
|---:|---|---|
| **1** | 1, 6, 9 | ALCANCE: el superviviente SI nombra los elementos que impulsan la metrica (botones, titulares, imagenes, ofertas) pero trae UN solo juego de ejemplos y la metrica ya fijada de antemano. El paso 6 trae la metrica como ELECCION (ej. tasa de registro) y el paso 9 trae cuatro elementos mas (ubicacion de CTA, copy, prueba social, numero de campos de formulario). Los dos entran a la enumeracion que el superviviente ya tiene, que es el remedio escrito del motivo. |
| **2** | 2, 7 | SALVAGUARDA: el superviviente manda disenar dos versiones cambiando un solo elemento a la vez y NO dice contra que sesgo se elige QUE cambiar; sin eso el paso se resuelve por el sesgo por defecto, probar el ajuste mas pequeno y mas facil. El paso 7 dice contra que (hipotesis de cambios grandes antes que pequenos ajustes) y el inciso se adosa al paso que protege, que es un paso de DECISION y no de ejecucion, que es la firma escrita de la clase. |
| **3** | 3, 8 | ALCANCE: el superviviente dice como se reparte el trafico y no dice CUANTO dura la prueba ni sobre cuantas metricas a la vez se lee. El paso 8 lo trae (durante semanas, una sola metrica a la vez) y entra al paso. Es la misma lectura de cadencia que OP-D-01 aplico en el sexto paso de su tabla, y se cita para que el criterio sea el mismo. |
| **4** | 4 | VERBATIM: el superviviente conserva su paso entero y el bloque repetido no le anade nada. |
| **5** | 5, 10 | DESTINO: el superviviente produce el resultado (implementar la ganadora y repetir) y NO dice que hacer con el. El paso 10 lo dice, y son las dos cosas que el entregable del nodo ya prometia sin que ningun paso las mandara: DOCUMENTAR los resultados, y el criterio de cuando se pasa a la siguiente metrica (cuando se agoten las ideas). La linea de destino entra en el paso FINAL, que es el remedio escrito del motivo. |

**`NOMBRE`, `METODO ALTERNATIVO` y `DIRECCION` no aplican, y por eso no se nombran. Las DOS
condiciones NO se tocan**, y se dice por que: **no hay repeticion medida entre ellas**.

| guarda | resultado |
|---|---|
| las siete guardas del constructor, escritas para caer | **7 de 7 verdes** (cobertura 1..10 exacta, motivos completos, convergencias que caen hoy, huellas repetidas vivas, rastros literales, cabeza del superviviente conservada, resultado dentro del estandar) |
| simulacion previa sobre copia en memoria (`P.7`) | **verde** (`SALIDA_V34_OPD03_SIM.txt`) |
| guarda de texto sobre TODOS los pasos | **10 de 10** calzan con su prefijo sellado |
| cero perdida, cobertura exacta sin huecos ni repetidos | **10 de 10** origenes |
| **caso positivo ANTES** | **0 PASAN, 7 CAEN** (`SALIDA_V34_OPD03_CASO_ANTES.txt`) |
| **caso positivo DESPUES** | **7 PASAN, 0 CAEN** (`SALIDA_V34_OPD03_CASO_DESPUES.txt`) |
| conservacion (pasa las dos veces a proposito, aparte) | **17 rastros vivos de 17** |
| fuente | **sin cambio**, Blank, unica |
| el censo no se mueve | **3.853 ficheros**: un destejido de fuente unica **no crea ni depreca nada** |

**Ciclo de `Gate 0` entero, en su orden:** `run_phase1.py --reaplico-curaduria` **exit 0, `GATE 0:
OK`**, **20 comprobaciones `[OK]` y 0 `[FALLO]`**, 3.853 compilados, **3.538 activos y 315
deprecados**; `etiquetas_de_cara.py --aplicar` **71**; `sync_assets_web.py` verde. **El comando 4
NO se corre y se dice por que: el censo no cambia**, y su vara (`web/lib/readiness.test.ts`) queda
verde en la suite. **Suites: motor 25 de 25, web 80 ficheros con 1.030 pasadas y 3 saltadas,
`tsc --noEmit` cero lineas.**

> **LO QUE LA SENAL RECALIBRADA DICE DE ESTE NODO, y va aqui porque es lo que mide el valor del
> instrumento, no el del destejido.** Con `MIN_BLOQUE = 2` la senal **si aplica** y da **49,5 con
> el corte tras el paso 8**. **La frontera escrita, y la lectura, ponen la costura tras el paso
> 5, y ahi la senal da 42,1: POR DEBAJO DE SU PROPIO UMBRAL.** El docstring del instrumento
> presume de *acertar el corte exacto*; **medido hoy sobre esta costura, no lo acierta**. Y de los
> seis nodos del acto **dispara en CUATRO**, incluidos **dos que el plan declara SANOS**. **La
> nomina siguio siendo la escrita, y la vara final fue la lectura.**

### ~~**PARADA AL 15 ago 2026 (vuelta 33). CERO NODOS TOCADOS.**~~ **SECCION SUPERADA POR LA DE ARRIBA (15 ago 2026, vuelta 34) y CONSERVADA ENTERA:** describe bien el estado del que esta vuelta partio, y su motivo 2 lleva su correccion declarada arriba. El instrumento de costuras se declara MAL CALIBRADO

**El modo continuo llego hasta aqui y se detuvo antes de escribir nada.** Tres motivos medidos
hoy, ninguno adivinado (`docs/loop/SALIDA_V33_PARADA_OPD03.txt` y
`SALIDA_V33_OPD03_COSTURAS.txt`, las dos de solo lectura).

**MOTIVO 1, Y ES EL QUE BLOQUEA: `scripts/costuras_internas.py` SE NIEGA A ENTREGAR.** Corrido
entero y sin tocarlo, sale con codigo distinto de cero y este texto suyo:

```
INSTRUMENTO MAL CALIBRADO. No entrega nada.
  La calibracion conocida no aparece en la cola: ['plan_mejora_procesos', 'economia_circular_como_modelo_de_negocio']
```

**Su propio encabezado escribio la regla que ahora lo detiene:** *los dos nodos de arriba TIENEN
que aparecer en la cola. Si falta alguno, el instrumento esta mal calibrado, lo dice y SALE CON
CODIGO 1 SIN ENTREGAR.* **La baranda funciono. Lo que hay que decir es que llevaba tiempo
funcionando y nadie la habia corrido entera.**

**LA CAUSA, MEDIDA Y ESTRUCTURAL, no una casualidad del texto.** La segunda senal, la del bloque
reiniciado, recorre `range(MIN_BLOQUE, n - MIN_BLOQUE + 1)` con `MIN_BLOQUE = 3`:

| pasos del nodo | rango de cortes que recorre | puede dar score |
|---:|---|---|
| **5** | **vacio** | **NO: devuelve (0,0) siempre** |
| 6 | [3] | si |
| 10 | [3, 4, 5, 6, 7] | si |

**Y LOS DOS NODOS DE CALIBRACION TIENEN CINCO PASOS HOY.** Su docstring declara que sus mejores
parejas eran **60,0** y **54,7**; **medidas hoy dan 47,1 y 54,3**, y su senal de bloque, que era
la que los cazaba (*los pone en los puestos 7 y 32 de 567 y acierta el corte exacto en las dos*),
**da 0,0 en los dos, por el rango vacio.**

> **CAIDA DE CIFRA PUBLICADA QUE ESTO ARRASTRA, y va declarada aqui aunque no sea de esta
> operacion.** El **MOVIMIENTO 2 de `OP-D-01`** (acta y reporte de la vuelta 32, publicado mas
> arriba en este mismo documento) concluye que `principio_calidad_mvp` *no tiene costura interna
> que destejer* y lo sostiene en dos cifras: **mejor pareja 51,2 contra un umbral de 80** y
> **mejor alineacion de bloques 0,0 contra un umbral de 44**. **La primera sigue en pie. LA
> SEGUNDA NO MIDE LO QUE DICE MEDIR:** ese 0,0 no es un nodo sin bloque, es **una senal que hoy
> devuelve 0,0 para todo**, incluidos los dos nodos que el propio instrumento sabe que son
> costura.
>
> **Y hay que decir COMO paso, porque es la leccion:** `vuelta32_costura_opd01.py` **importa las
> senales y los umbrales** de `costuras_internas.py`, que es mas honesto que copiarlos **y ademas
> pasa POR ENCIMA de la puerta de calibracion**, que vive en el `main()`. **Una guarda que se
> saltea importando por debajo es un test verde y mal**, que es el canon del banco 9 aplicado a
> los instrumentos.
>
> **LO QUE ESTA CAIDA NO DICE:** no dice que la conclusion del movimiento 2 sea falsa. Su otra
> pata es TEXTUAL y no depende del instrumento: las tres narraciones que la ficha le contaba **ya
> no estan**, la tercera se la llevo `OP-F-03` y la segunda se fundio con la primera por `P.19`.
> **Lo que cae es la mitad instrumental de su apoyo, no su conclusion.** No lo arreglo yo.

**MOTIVO 2: NO SE PUEDE SABER CUALES SON LAS TRES COSTURAS QUE HAY QUE DESTEJER.** El `ORDEN
INTERNO` escrito de `OP-D-03` empieza por *destejer las TRES costuras*, y **la nomina de esas tres
no esta escrita en ninguna parte por su nombre**: sale del instrumento. **Medidos hoy los seis
nodos con las senales y los umbrales importados, NINGUNO dispara ninguna de las dos:**

| nodo | pasos | mejor pareja (umbral 80) | mejor bloque (umbral 44) | dispara |
|---|---:|---:|---:|---|
| `ab_testing_optimizacion` | 10 | 55,1 | 0,0 | ninguna |
| `funnel_get_customers_optimizacion` | 7 | 50,4 | 0,0 | ninguna |
| `optimizacion_embudo_get_customers` | 5 | 48,6 | 0,0 | ninguna |
| `split_testing` | 4 | 48,8 | 0,0 | ninguna |
| `split_testing_experimentos_ab` | 5 | 45,6 | 0,0 | ninguna |
| `test_ab_precio` | 5 | 54,5 | 0,0 | ninguna |

**Y el 0,0 de esta tabla NO se puede leer como *no hay bloque*: es la senal muerta.** Medido paso
a paso sobre el ancla de diez pasos, `ab_testing_optimizacion`, **los cinco cortes posibles logran
2 emparejamientos monotonos y hacen falta 3**, asi que ninguno llega a puntuar.

**MOTIVO 3: EL ACTO ESTA A 8 DE 15, y esta vez NO se puede resolver leyendo.** Los siete que
faltan **se leerian igual que los tres de `OP-D-02`**, por `P.5` y como lecturas dirigidas, **pero
`P.5` manda leer el acto DESPUES de su destejido**, y el destejido es justo lo que el motivo 1
bloquea. **Leerlos hoy seria leer texto que va a cambiar**, que es lo que la regla existe para
impedir.

| par interno **sin veredicto** |
|---|
| `ab_testing_optimizacion` contra `funnel_get_customers_optimizacion` |
| `funnel_get_customers_optimizacion` contra `split_testing` |
| `funnel_get_customers_optimizacion` contra `split_testing_experimentos_ab` |
| `funnel_get_customers_optimizacion` contra `test_ab_precio` |
| `optimizacion_embudo_get_customers` contra `split_testing` |
| `optimizacion_embudo_get_customers` contra `split_testing_experimentos_ab` |
| `optimizacion_embudo_get_customers` contra `test_ab_precio` |

> **LO QUE SI QUEDA MEDIDO Y APROVECHABLE para quien retome:** el acto tiene **SIETE pares `A`**
> (277, 452, 643, 1061, 1571, 1575 y el 374) y **un congelado**, el **738**. El campo
> `superviviente` esta en **`null`**, leido hoy. **Los seis nodos estan vivos y son de TRES libros
> distintos** (Blank, Ries y Value Proposition Design), cosa que `OP-D-02` no tenia: alli los
> cuatro eran de Cooper. **Ese detalle va a decidir su fusion y conviene tenerlo escrito antes.**

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
