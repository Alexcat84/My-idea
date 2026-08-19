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
| **3** | `OP-D-03` | `ab_testing_optimizacion` | ~~**2** (738, 1061)~~ **2 LIBERADOS EL 15 ago 2026 (vuelta 34): los dos a `D`** | ~~**3**~~ **3, de las cuales DOS estaban CONSUMIDAS por la fase 01 y una se ejecuto** | **6** |
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

### PASO 2 DEL ORDEN INTERNO: **PARADA AL 15 ago 2026 (vuelta 35). CERO NODOS TOCADOS Y CERO VEREDICTOS VOLCADOS**

**El paso 2 dice *solo entonces decidir sobre los SEIS nodos*, o sea la fusion. No se
ejecuta, y el motivo no es una duda: es `P.5` medida.** `P.5` (`BANCO_DEL_PLAN.md` linea 239)
manda que **cada acto se lea ENTERO DESPUES de su destejido y ANTES de su fusion**, y escribe su
motivo en la misma pagina: *leer un par cuyo nodo va a perder la mitad de sus pasos es leer algo
que va a dejar de existir*.

**MEDIDO HOY CON DOS VARAS INDEPENDIENTES, y la segunda es la que manda.** La de FECHA
(`scripts/loop/vuelta35_pares_opd03.py`) compara la fecha de la lectura del par contra la del
ultimo cambio de sus dos ficheros. La de TEXTO (`scripts/loop/vuelta35_rancios.py`) compara los
**pasos accionables del nodo en el commit de la lectura contra los de hoy**, y hace falta porque
**un fichero de nodo cambia por cosas que no son su texto** (una redireccion, un reciprocado del
Gate, un campo de fuente): contar como rancio un par cuyo texto no se movio seria inflar el
hallazgo. **Las dos varas dan la misma lista.**

**LA TABLA NO ESTA TECLEADA: es la salida del instrumento, pegada entera.** Comando, corrido en
esta vuelta:

```
python scripts/loop/vuelta35_rancios.py
```

salida completa en `docs/loop/SALIDA_V35_RANCIOS.txt`, cierre pegado sin editar una coma:

```
RANCIOS POR TEXTO: 5
   277   A    optimizacion_embudo_get_customers de 10 a 5 pasos
   374   A    split_testing_experimentos_ab de 9 a 5 pasos
   452   A    ab_testing_optimizacion de 15 a 5 pasos
   1571  A    split_testing_experimentos_ab de 9 a 5 pasos
   1575  A    ab_testing_optimizacion de 15 a 5 pasos
AL DIA: 3 -> [(643, 'A'), (738, 'D'), (1061, 'D')]
```

> **CORRECCION DECLARADA (15 ago 2026, vuelta 35), y es de una cifra publicada por la vuelta 34.
> El texto viejo se queda entero arriba y abajo.** El **pendiente de doctrina 3** de la vuelta 34
> escribio que los pares emitidos contra texto muerto eran **DOS**, el `452` y el `1575`. **Medidos
> hoy son CINCO, y los cinco son `A`.** Los tres que aquel recuento no vio (`277`, `374`, `1571`)
> **no envejecieron por el destejido de esta operacion sino por los de la fase 01**, que se
> llevaron el bloque `6 a 10` de `optimizacion_embudo_get_customers` (`OP-F-04-WEI`) y el `6 a 9`
> de `split_testing_experimentos_ab` (`OP-F-04-RAC`). **La vuelta 34 miro solo hacia su propio
> destejido.**

**LO QUE ESTO LE HACE A LA CONCLUSION PUBLICADA.** La vuelta 34 publico que el acto **no es una
familia de seis sino DOS FAMILIAS CERRADAS**, una de cuatro y una de dos. **Esa forma se dibuja
con los SEIS pares `A` del acto, y CINCO de los seis estan rancios.** El unico `A` al dia es el
**643** (`split_testing` contra `test_ab_precio`), **y sus dos nodos no cambiaron de texto**.

**LAS CINCO RELECTURAS ESTAN HECHAS Y NO VOLCADAS**, y las dos mitades de esa frase son a
proposito. **Hechas**: los seis nodos impresos ENTEROS antes de decidir
(`SALIDA_V35_NODOS_ENTEROS.txt`), las razones viejas leidas enteras
(`SALIDA_V35_RAZONES.txt`), las aristas buscadas en los DOS sentidos, y las cinco con su razon
escrita, sostenida y con su discutible marcado. **No volcadas**: por la **regla 5 de
`EJECUTOR.md`**, lo que contradice una cifra publicada con su corte **se declara como PARADA y no
lo arregla el ejecutor**. La propuesta queda **sellada** en
`docs/loop/PROPUESTA_V35_RELECTURAS.json`, construida por `scripts/loop/vuelta35_relecturas.py`
con **seis guardas escritas para caer**, las seis verdes (`SALIDA_V35_RELECTURAS.txt`).

**Y LA CONSECUENCIA SE COMPUTA, NO SE DIBUJA** (`P.6`: la nomina de acto se computa y no admite
gusto). Si las cinco se volcaran, el instrumento mide que quedaria **UN solo par `A` dentro del
acto**, el `643`, y que el acto de **SEIS** pasaria a ser un acto de **DOS**
(`split_testing`, `test_ab_precio`), **saliendo del cierre transitivo `ab_testing_optimizacion`,
`funnel_get_customers_optimizacion`, `optimizacion_embudo_get_customers` y
`split_testing_experimentos_ab`**. **El paso 2 se quedaria sin los seis sobre los que decidir.**

> **LA PREGUNTA QUE ESTA VUELTA NO SE CONTESTA SOLA, y va al fundador:** el **643** cae bajo el
> mismo criterio de objeto que voltea a los otros cinco (`test_ab_precio` aplica la prueba al
> precio; `split_testing` compara alternativas de propuesta de valor), **pero `P.5` no lo
> alcanza**, porque ninguno de sus dos nodos cambio de texto. **Releerlo seria re cribar, que es
> otro frente y nadie lo abrio.** Queda declarado en vez de forzado.

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

> **CORRECCION DECLARADA (15 ago 2026, vuelta 34): las dos cifras de este recuadro envejecieron
> el mismo dia en que se escribieron.** Tras el destejido, el **1061** paso de `A` a `D` y el
> **738** de `B` a `D`: el acto tiene hoy **SEIS pares `A`** (277, 452, 643, 1571, 1575 y 374) y
> **CERO congelados**. El texto viejo se queda entero.
>
> **LO QUE SI QUEDA MEDIDO Y APROVECHABLE para quien retome:** el acto tiene **SIETE pares `A`**
> (277, 452, 643, 1061, 1571, 1575 y el 374) y **un congelado**, el **738**. El campo
> `superviviente` esta en **`null`**, leido hoy.

> **SEGUNDA CORRECCION DECLARADA (18 ago 2026, vuelta 36): LAS DOS CIFRAS DE ARRIBA VOLVIERON A
> ENVEJECER, y esta vez de golpe.** `P.5` mando releer el acto entero antes de fundirlo, la vuelta
> 35 midio que **CINCO de esos seis pares `A` se habian emitido contra texto que las cirugias ya se
> habian llevado**, y el fundador adjudico el volcado
> (`docs/loop/paradas/2026-08-15-p5-rancios-opd03-DECISION.md`). **Volcados hoy: 277, 374, 452,
> 1571 y 1575, los cinco de `A` a `D`** (`docs/loop/_lote_v36.jsonl`, marcador recomputado
> `n 3.388, A 576, B 83, C 8, D 2.721`). ~~**El acto tiene hoy UN solo par `A`, el 643**~~, y sigue
> con **cero congelados**. **El texto viejo se queda entero.**
>
> **TERCERA CORRECCION DECLARADA (18 ago 2026, MISMA vuelta 36 unas horas despues), y corrige a la
> de arriba, escrita por mi mismo hace un rato:** el **643** se leyo como lectura dirigida
> **`LD-82`** y dio **`D`**, asi que **el acto tiene CERO pares `A`**. **La cifra de una sola
> correccion vivio menos de una tarde, y va escrita asi a proposito**: la de arriba no se borra
> porque fue cierta mientras el `643` seguia sin leerse. **Los seis nodos estan vivos y son de TRES libros
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


---

## `OP-D-03` CERRADA: **DESTEJIDO HECHO Y SIN FUSION** (18 ago 2026, vuelta 36)

**El paso 2 de su orden interno decia *solo entonces decidir sobre los SEIS nodos*. La decision
esta tomada y es esta: NO SE FUNDE NINGUNO. Y no es una renuncia: es lo que la medicion dejo.**

### COMO SE LLEGO, con la medicion de cada tramo al lado

| tramo | quien | que dejo |
|---|---|---|
| **paso 1**, destejer las TRES costuras | vuelta 34 | **de las tres, solo UNA necesitaba operacion**: las otras dos ya estaban CONSUMIDAS por la fase 01 (`OP-F-04-WEI` se llevo el bloque 6 a 10 de `optimizacion_embudo_get_customers` y `OP-F-04-RAC` el 6 a 9 de `split_testing_experimentos_ab`); `ab_testing_optimizacion` se destejio de **diez pasos a cinco** |
| **paso 3**, releer 738 y 1061 | vuelta 34 | los dos a `D`, y el **1061** al caer **partio el acto en dos componentes** |
| **la medicion de `P.5`** | vuelta 35 | **CINCO de los seis pares `A` del acto se habian emitido contra texto que ya no existe** (dos varas independientes, `docs/loop/SALIDA_V35_RANCIOS.txt`). Las cinco relecturas hechas, selladas y **NO volcadas**: `PARADA` por la regla 5 de `EJECUTOR.md` |
| **la adjudicacion** | el fundador, 15 ago 2026 | se vuelcan las cinco; **el `643` SI se lee** como dirigida dentro del acto; y **la operacion se resuelve por el `643`** |
| **el volcado de las cinco** | **vuelta 36** | 277, 374, 452, 1571 y 1575, **las cinco de `A` a `D`**, marcador a **`n 3.388, A 576, B 83, C 8, D 2.721`** |
| **`LD-82`, el `643`** | **vuelta 36** | **`D`, los dos sanos, sin arista declarada**, marcador a **`n 3.388, A 575, B 83, C 8, D 2.722`** |

### LA RESPUESTA DE `P.5`, Y ES LA TERCERA VERSION DE LA MISMA PREGUNTA

> **NI UNA FAMILIA DE SEIS, NI DOS FAMILIAS, NI UN PAR. NINGUNA.** El acto tiene **cero pares `A`**
> y **desaparece del censo de actos**. Los **seis nodos quedan vivos, sanos y separados.**

**Y EL INSTRUMENTO LO CONFIRMA AL DIGITO, no el dibujo** (`scripts/plan/recomputo_3388.py`, salida
`docs/loop/SALIDA_V36_RECOMPUTO_3388_B.txt`): actos de **335 a 333**, cerradas de **281 sobre 604
nodos** a **279 sobre 598**, nodos con al menos una `A` de **851 a 845**, y **las cuatro
comprobaciones del `08_VERIFICACION.md` dan OK las cuatro**.

### LO QUE ESTE CIERRE NO HACE, y va dicho porque callarlo seria peor

- **No toca un solo nodo.** Ninguno se funde, ninguno se depreca, ninguno pierde un paso en esta
  vuelta. El censo del grafo no se mueve: **3.853 ficheros, 3.538 vivos, 315 deprecados.**
- **No fija superviviente ni eliminados.** Los campos `superviviente` y `eliminar` de la operacion
  se quedan como estaban, **y no por olvido: sin fusion no hay superviviente que fijar.**
- **No cambia el estado de la operacion.** Sigue en `LISTA`, **igual que `OP-D-01` y `OP-D-02`, que
  tambien estan ejecutadas**: el esquema de `OPERACIONES.jsonl` no tiene otro estado y la casa
  registra el hecho consumado en la NOTA. **Queda como PENDIENTE DE DOCTRINA: hoy no hay con que
  distinguir una operacion HECHA de una pendiente sin leerle la nota.**

> **LA FIGURA QUE ESTA OPERACION DEJA PARA EL INVENTARIO, y se propone sin darla por adoptada: UN
> ACTO PUEDE MORIR DE SU PROPIO DESTEJIDO.** El acto se convoca por transitividad de pares `A`; si
> lo que hacia repetir a esos pares eran **bloques ajenos que una cirugia anterior se llevo**,
> entonces destejer **no prepara la fusion: la cancela**. `OP-D-03` es el primer ejemplar medido de
> la campana.


---

### `OP-D-04`, ESTADO AL 19 ago 2026 (vuelta 37): **PASOS 1 Y 2 HECHOS, ACTO LEIDO ENTERO, FUSION EN PARADA**

**EL PASO 1 DEL ORDEN INTERNO ESTA HECHO Y NO LO HIZO ESTA OPERACION: lo hizo `OP-F-02`.** Medido
hoy contra el grafo y no leido de su nota (`scripts/loop/vuelta37_fuente_primero.py`, salida
`docs/loop/SALIDA_V37_OPD04_FUENTE.txt`): sus **tres nodo propio** estan vivos con 6, 5 y 4 pasos y
los tres declarados en `INDICE_ROJO_DECLARADO.jsonl`; **Mollick no aparece ya en ninguno de los
tres origenes**; y `brainstorming_divergente` entra con **una sola fuente**, Tim Brown, que es la
fijada. `OP-F-03` tambien verificada: sus **cuatro nodo propio** vivos con 4, 9, 4 y 8 pasos. **Del
cruce medido: de los siete nodos de `OP-D-04`, UNO esta en la nomina de `OP-F-02` y CERO en la de
`OP-F-03`**, asi que esa segunda dependencia es **de orden de fase y no de nodo compartido.**

**EL PASO 2, EL DESTEJIDO, ESTA CONSUMADO, Y NO POR RENUNCIA: porque su unica costura y el injerto
de fuente eran EL MISMO BLOQUE, y un solo corte sirvio a los dos frentes**
(`scripts/loop/vuelta37_destejido_opd04.py`, salida `docs/loop/SALIDA_V37_OPD04_DESTEJIDO.txt`).

| medicion de hoy | resultado |
|---|---|
| costurados del acto sobre los 128 registros de `docs/COSTURAS_INTERNAS.jsonl` | **1 de 7**, `brainstorming_divergente`; los otros seis sanos. La seccion 54.3 del informe declara 1 y 6 |
| corte registrado de esa costura | **el 5**, bloque **5 a 8** |
| frontera que `OP-F-02` publico en `01_FUENTES.md` | **1 a 4 / 5 a 8**: **el mismo sitio** |
| pasos de `brainstorming_divergente` hoy | **4**, exactamente el lado izquierdo del corte |
| los ocho pasos viejos, leidos por `git` del padre del commit de `OP-F-02` | **8**, tal como el registro de costuras dice |
| los 1 a 4 viejos contra el nodo de hoy | **4 de 4 IDENTICOS** |
| los 5 a 8 viejos contra `ideacion_con_ia_en_la_sesion` | **4 de 4 IDENTICOS**, y el destino cuelga del cableado |
| material perdido | **CERO**: 4 mas 4 igual a 8 |

> **LO QUE NO SE HIZO Y SE DICE EN VOZ ALTA: no se volvio a correr `scripts/costuras_internas.py`.**
> Ese instrumento **se declara MAL CALIBRADO en su propia salida** desde la vuelta 34
> (`docs/loop/SALIDA_V34_COSTURAS_RECALIBRADO.txt`: *INSTRUMENTO MAL CALIBRADO. No entrega nada*).
> **`OP-D-04` no necesita su cifra**: su frontera esta **publicada** en `01_FUENTES.md` y su corte
> **registrado con fecha** en `COSTURAS_INTERNAS.jsonl`. Preguntar si hoy nacio una costura que
> nadie registro seria abrir alcance que ninguna operacion escribio. **Va como discutible marcado
> del reporte, no como cifra.**

**EL PASO 3 SE PARTE EN DOS, Y SOLO LA PRIMERA MITAD SE PUDO HACER.** `P.5` manda leer el acto
entero **antes** de la fusion, y eso esta hecho: **21 de 21 pares leidos**, cuatro de ellos
releidos hoy por rancios (585, 823, 834 y 844, **ninguno cambia de clase**) y trece leidos como
lecturas dirigidas **`LD-83` a `LD-95`**. **La respuesta a la pregunta de `P.5` esta escrita entera
en `docs/plan/LECTURAS_DIRIGIDAS.md`**: no es una familia de siete, son **dos triangulos cerrados,
un nodo colgado y TRES puentes.**

**LA FUSION NO SE EJECUTA, y son TRES motivos medidos hoy, ninguno adivinado. Cero nodos tocados.**

**MOTIVO 1: NO HAY SUPERVIVIENTE, ni escrito ni deducible, y esta vez el hueco es mayor que en
`OP-D-02`.** El campo `superviviente` de `OP-D-04` esta en **`null`**, leido hoy en el fichero. Y
la especie de `9.3.1`, **con su correccion del 18 ago 2026 que manda hacer la prueba SOLO sobre los
pares `A`**, sale **POR ELEGIR** por el peor de los caminos: **de los OCHO pares `A` del acto,
CERO nombran ganador en su razon.** No es que un nodo gane unos y pierda otros: **es que no hay ni
una victoria citable de la que tirar.** Y dos de esas ocho, el **823** y el **834**, dicen
literalmente que **no se pelea la clase porque la decision ya esta tomada en otro sitio**, que es
la mesa del racimo. **`P.8` desempata a contenido empatado; aqui el contenido no ha hablado
todavia.**

**MOTIVO 2: TRES NODOS PUENTE, Y `P.10` PROHIBE FUNDIR LA COMPONENTE ENTERA.** El campo `preservar`
de la operacion habla de **el superviviente del acto**, en singular, y la medicion dice que el acto
**no puede volverse un solo nodo sin desmentir trece lecturas `D`**. La salida que `P.10` deja
(fundir solo el subconjunto cerrado y enlazar el resto) **da DOS triangulos, no uno**, y por lo
tanto **dos supervivientes y no uno**: eso **cambia la forma final de la operacion**, y la forma
final no la escribe ninguna pagina. La seccion **54.6** del informe lo dejo dicho el 11 ago 2026 y
sigue siendo cierto: *no dice si los siete nodos del brainstorming deben quedar en uno, en dos o en
cuatro; dice cuantos hay que tener delante para poder decidirlo*. **Hoy ya estan todos delante. La
decision sigue sin tomarse.**

**MOTIVO 3: EL PRIMER TRIANGULO ES UN RACIMO MIXTO AL QUE LE FALTA UN MIEMBRO, Y ESE MIEMBRO ESTA
FUERA DEL ACTO Y FUERA DEL DOMINIO.** Medido hoy en `docs/RACIMOS_MIEMBROS.jsonl`: el racimo **Las
reglas del brainstorming** tiene **CUATRO** miembros, `reglas_brainstorming`,
`brainstorming_divergente`, `brainstorming_efectivo` **y `brainstorming`, que es de `quality`**.
**Los tres primeros son exactamente el triangulo cerrado; el cuarto no esta en el acto.** Y
`docs/MESA_RACIMOS.md` escribe que este racimo es uno de los **tres mixtos** de los trece del
nucleo, con esta advertencia: *podar el lado del nucleo de un racimo mixto cambia el gradiente del
mundo que lo acompana*. **Fundir los tres aqui decidiria la forma del racimo sin su cuarto miembro
y sin su mesa.** Y `P.5` no da puerta para leerlo: su alcance adjudicado es **el acto en operacion,
nunca fuera**. **Medido tambien hoy: ninguna operacion de la fase 06 nombra a estos nodos**, asi
que esa mesa **no esta escrita como operacion**.

> **LO QUE SI QUEDA HECHO Y NO HAY QUE REPETIR:** la fuente verificada, el destejido consumado, el
> acto **leido entero por primera vez** con sus trece lecturas dirigidas nuevas, las cuatro
> relecturas de `P.5` volcadas con su correccion declarada, y **el mapa del acto medido**: dos
> triangulos, tres puentes y un nodo colgado. **Lo unico que falta para ejecutar es una decision
> sobre la forma final y sobre quien sobrevive en cada triangulo.**

**EL MARCADOR NO SE MOVIO, y esa es la prueba de que no se toco nada:** las cuatro relecturas no
cambian de clase y las trece lecturas dirigidas estan fuera de cola. **`n 3.388, A 575, B 83, C 8,
D 2.722`**, identico a la apertura de la vuelta.

---

### `OP-D-04`, ESTADO AL 19 ago 2026 (vuelta 38): **LOS DOS SUPERVIVIENTES ELEGIDOS POR `P.8` Y LOS DOS PLANES SELLADOS. CERO NODOS TOCADOS**

**CORRECCION DECLARADA sobre el estado de la vuelta 37, y nada de lo de arriba se borra.** Aquel
estado publicaba la fusion **EN PARADA** con tres motivos medidos. **Los tres estan resueltos, y
por dos vias distintas que conviene no confundir:**

| motivo de la parada del 19 ago (vuelta 37) | como quedo |
|---|---|
| **1**, no hay superviviente ni escrito ni deducible, y de las ocho `A` **cero** nombran ganador | **RESUELTO EN ESTA VUELTA POR LECTURA**: los dos supervivientes se eligen por `P.8`, por lectura de contenido escrita entera, y se publican aqui abajo |
| **2**, tres nodos puente y la forma final no la escribe ninguna pagina | **RESUELTO POR DECISION DEL FUNDADOR** el 19 ago 2026: la forma es **siete a tres**, dos fusiones de tres mas el colgado vivo, que es la tercera salida de `P.10` |
| **3**, el primer triangulo es un racimo mixto sin su cuarto miembro y sin mesa escrita | **RESUELTO EN ESTA VUELTA POR LECTURA**, con la excepcion de una vez autorizada: `LD-96` a `LD-98`, **las tres `D`**, con **una PARADA DE DOCTRINA declarada** al pie de la tanda |

**LA FUSION SIGUE SIN EJECUTARSE, y no por falta de nada: por mandato.** La `DECISION 2` del
fundador dice que la eleccion **se publica SELLADA y la fusion espera el acta del auditor**: no se
ejecuta en la misma vuelta que la decide. **Esta vuelta toco CERO nodos y `dataset/` esta
intacto.**

---

#### LA ELECCION DE `P.8` EN EL TRIANGULO DEL TALLER: **sobrevive `reglas_brainstorming`**

**`P.8` dice que el cableado desempata y NO decide.** Aqui decide el contenido, y el cableado
**apunta al otro lado**: se escribe en vez de esconderse.

| candidato | pasos | lo nombran | momentos de la sesion que cubre | piezas unicas |
|---|---:|---:|---:|---:|
| **`reglas_brainstorming`** | **5** | 11 | **5** | **2** |
| `brainstorming_efectivo` | 4 | **13** | 1 y medio, **y ninguno de captura** | 2 |
| `brainstorming_divergente` | 4 | 4 | 3 | **0** |

**Las dos columnas de la izquierda estan medidas** (`scripts/loop/vuelta38_triangulos.py`, salida
`docs/loop/SALIDA_V38_TRIANGULOS.txt`, bloques 1 y 4); **las dos de la derecha son la lectura de
contenido**, y va entera en el plan sellado, campo `eleccion_p8.lectura_de_contenido`.

**LA LECTURA, en una linea cada una:** `reglas_brainstorming` es el unico que cubre el arco de la
sesion de punta a punta (enunciado del problema, inmersion, reglas, captura visual y
calentamiento); es el unico que tiene **dos piezas que ningun otro miembro del triangulo tiene**
(la inmersion de campo y el ejercicio de calentamiento nombrado); y **es el que entrega mas
lejos**, con las ideas *agrupadas por tema* contra la coleccion suelta de uno y la sesion
documentada sin soporte del otro. **`brainstorming_efectivo` promete en su entregable una sesion
documentada y no tiene ni un paso que diga como se documenta.**

> **TRECE CONTRA ONCE, Y PIERDE EL TRECE.** Es la forma dura de `P.8`, la misma del acto II del
> racimo del pivote, donde `pivote_o_proceder` sobrevivio con **5 contra 10** por llevar material
> propio. **Y aqui ir contra el cableado cuesta CERO aristas, medido:** las trece de
> `brainstorming_efectivo` son **reciprocas las trece**, asi que las trece se redirigen solas al
> superviviente.

#### LA ELECCION DE `P.8` EN EL TRIANGULO DE LA ALTERNANCIA: **sobrevive `pensamiento_convergente_divergente`**

| candidato | pasos | lo nombran | abre? | cierra? | entregable |
|---|---:|---:|:---:|:---:|---|
| **`pensamiento_convergente_divergente`** | 4 | **5** | **si** | **si** | **mapa de iteraciones a lo largo del proyecto** |
| `generar_multiples_opciones` | 3 | 3 | si | **no** | set de 3 a 5 alternativas |
| `design_attitude_vs_decision_attitude` | 4 | 2 | si | **no** | mentalidad, que **no es documento** |

**LA LECTURA:** el triangulo se llama **LA ALTERNANCIA** y **solo uno de los tres tiene los dos
movimientos**. El embudo que estrecha (paso 2) y el descarte de ideas prometedoras (paso 4) **no
estan en ninguno de los otros dos**. Ademas es el unico cuya disciplina **se repite en el tiempo**,
que por el informe `67.6` es lo que convierte un paso en procedimiento, y el unico cuyo entregable
es un documento que dura. **Un nodo al que habria que injertarle la mitad de su propio nombre no
era la cabeza.**

> **AQUI EL CABLEADO COINCIDE con el contenido, cinco contra tres y contra dos, y se dice
> igualmente que NO fue lo que decidio.** Una coincidencia que no se declara se lee despues como si
> hubiera sido la razon.

---

#### LOS DOS PLANES SELLADOS

**`docs/loop/PLAN_V38_OPD04_TALLER.json`** y **`docs/loop/PLAN_V38_OPD04_ALTERNANCIA.json`**, los
dos con `estado` **SELLADO Y SIN EJECUTAR**. **No estan tecleados: los escribe
`scripts/loop/vuelta38_sellar_planes.py`** leyendo los textos de origen de `dataset/nodos/` (viajan
verbatim), derivando los pasos finales de los grupos (no se escriben dos veces) y **abortando si
un origen queda sin colocar o colocado dos veces**. Salida entera en
`docs/loop/SALIDA_V38_SELLAR.txt`.

**LA SIMULACION PREVIA DE `P.7` CORRIO SOBRE COPIA EN MEMORIA, y devolvio las seis cosas que la
regla le exige** (`scripts/plan/simular_fusion.py`, salidas `docs/loop/SALIDA_V38_SIM_TALLER.txt`
y `docs/loop/SALIDA_V38_SIM_ALTERNANCIA.txt`):

| | el taller | la alternancia |
|---|---:|---:|
| redirecciones de entradas vivas | **17** | **5** |
| deprecados que nombran y **no se tocan** | 0 | **1**, `fase_entender_modelo_negocio` |
| duplicadas **nuevas** que la fusion fabrica | **1** | **1** |
| auto aristas | 0 | 0 |
| aristas que quedarian declaradas en **un solo extremo** | **16** | **4** |

**Y LA SIMULACION SE GANO SU SUELDO DOS VECES, que es el caso positivo que `P.7` pide.**

**HALLAZGO 1, y es el que cierra la `DECISION 3` del fundador sin escribir nada.** La `DECISION 3`
manda que, si las tres lecturas dan `D`, el cuarto miembro **se ENLACE** al superviviente del
taller. **Ese enlace no hay que escribirlo: la fusion lo pone sola.** `brainstorming` nombra hoy a
`brainstorming_efectivo` en sus `nodos_previos`; al morir ese nodo, la entrada se redirige, y el
bloque 6 de la simulacion lo imprime resuelto: **`reglas_brainstorming -> brainstorming`**. **Eso
no se ve leyendo. Se ve simulando.**

**HALLAZGO 2, y corrige una premisa que parecia obvia.** El ejecutor de fusiones de la casa
(`scripts/loop/vuelta33_fundir.py`) redirige a los vecinos **y no le escribe al superviviente las
aristas del absorbido**: su lista propia no se toca. Leido asi, las dos fusiones dejarian **20**
aristas declaradas en un solo extremo, en un grafo cuya tasa de reciprocidad medida hoy es **99,59
por ciento** (15.448 de 15.511, `scripts/loop/vuelta38_reciprocidad_post.py`). **Pero no las deja,
y esto NO se dedujo: se fue a mirar.** Quien las escribe es `scripts/run_phase1.py` en su **paso 5,
Simetrizacion de enlaces**, y el precedente esta medido en el log de la fusion de `OP-D-02`
(**commit `72c718ea`**, `phase1_run_log.json`, `symmetrize_added` con las **dos** aristas que gano
`voz_del_cliente_voc`). **Los dos planes llevan por eso un bloque `simetrizacion_esperada` con la
lista ENTERA y su guarda escrita**: el dia de la ejecucion, `symmetrize_added` tiene que traer
exactamente esas entradas para el superviviente, **ni una mas ni una menos**.

---

#### EL MAPA DE MOVIMIENTO DEL TALLER: **de 5 mas 4 mas 4 a SIETE pasos**

**NO ESTA TECLEADA: esta IMPRESA desde el plan sellado** (`EJECUTOR.md` regla 1, cuarto renglon).
**Comando, corrido en esta vuelta:**

```
python scripts/loop/vuelta33_tabla_mapa.py docs/loop/PLAN_V38_OPD04_TALLER.json
```

salida entera en `docs/loop/SALIDA_V38_TABLAS.txt`, pegada aqui sin editar una coma. **Los
origenes llevan PREFIJO porque aqui hay TRES fuentes**: `R` el superviviente `reglas_brainstorming`,
`D` `brainstorming_divergente`, `E` `brainstorming_efectivo`.

| paso del resultado | de que origenes sale | el motivo de perdida de linea que lo modifica |
|---:|---|---|
| **1** | D1, E3 | LAS DOS PIEZAS SON DEL MISMO OBJETO, quien esta en la sala y donde. El superviviente no dice ni una cosa ni la otra en ninguno de sus cinco pasos, asi que las dos VIAJAN. Va primero porque en los dos donantes precede a todo y porque colocarla a la cabeza no mueve ninguno de los cinco pasos del superviviente entre si. |
| **2** | R1 | VERBATIM del superviviente. |
| **3** | R2, D2, E1, E2 | EL BLOQUE DE REGLAS DE LOS TRES EN UNO. El superviviente ya traia diferir el juicio, una conversacion a la vez, ir por cantidad, ser visual y las ideas locas. VIAJAN tres piezas que no tenia: hacerlas VISIBLES, mantenerse enfocado en el tema, y la regla de construir sobre las ideas de otros, que es la unica regla del acto que el superviviente no dice en ninguna parte. El procedimiento de esa ultima no se injerta porque vive en construir_sobre_ideas_ajenas, que queda VIVO y enlazado por P.10. |
| **4** | R3 | VERBATIM del superviviente. Es la pieza que ningun otro miembro del acto tiene, y la razon del puesto 834 ya la llamo lo mas caro de perder. |
| **5** | R4, D4 | MISMO GESTO EN LOS DOS. El superviviente ya capturaba y movia en post-its; del donante VIAJA solo el otro soporte nombrado, la pizarra. |
| **6** | R5 | VERBATIM del superviviente. |
| **7** | D3, E4 | EL ACTO DE GENERAR Y SU ENCUADRE. El superviviente manda ir por cantidad dentro de sus reglas pero no tiene paso de generacion, y no dice en ninguna parte que la sesion de generar vaya separada de la de elegir. Las dos VIAJAN y van al final porque son lo que se hace despues del calentamiento. |

**Y LAS CONDICIONES pasan de 2 mas 2 mas 2 a CUATRO.** Misma fuente, **con cabecera propia** para
que el verificador de mapas no la lea como tabla de particion de pasos:

| condicion del resultado | de que origenes sale | el motivo que la modifica |
|---:|---|---|
| **1** | RC1, EC1 | LA MISMA CONDICION DICHA DOS VECES. Del donante VIAJA el para que, antes de tomar decisiones. |
| **2** | RC2 | VERBATIM del superviviente. |
| **3** | DC1, DC2 | LAS DOS DEL DONANTE, que dicen el mismo momento del proyecto y ninguna de las dos esta en el superviviente. VIAJAN juntas. |
| **4** | EC2 | VIAJA entera: es la condicion que hace falta para el primer paso del resultado, y el superviviente no la tenia. |

#### LA TABLA DE PERDIDAS DEL TALLER (`P.13`)

**Tampoco esta tecleada.** Comando corrido en esta vuelta,
`python scripts/loop/vuelta38_tabla_perdidas.py docs/loop/PLAN_V38_OPD04_TALLER.json`, salida
entera en `docs/loop/SALIDA_V38_PERDIDAS.txt`.

| pieza | de que nodo | clase P.13 | a donde va | por que |
|---|---|:---:|---|---|
| el espacio dedicado sin distracciones | `brainstorming_divergente` | **VIAJA** | paso 1 del resultado | el superviviente no nombra el espacio en ninguno de sus cinco pasos |
| generar el mayor numero de ideas sin filtrar prematuramente | `brainstorming_divergente` | **VIAJA** | paso 7 del resultado | el superviviente lo tiene como REGLA y no como PASO: no hay en el ningun momento en que efectivamente se genere |
| que la cosecha se filtra despues, en la fase de convergencia | `brainstorming_divergente` | **VIAJA** | entregable y resumen del resultado | el entregable del superviviente se queda en las ideas agrupadas y no dice a donde van |
| la regla de construir sobre las ideas de otros, y su prioridad sobre generar ideas propias aisladas | `brainstorming_divergente y brainstorming_efectivo` | **VIAJA** | paso 3 del resultado | ES LA UNICA REGLA DEL TRIANGULO QUE EL SUPERVIVIENTE NO DICE, medido sobre sus cinco pasos. Viaja LA LINEA. El PROCEDIMIENTO de esa linea NO se injerta porque vive en construir_sobre_ideas_ajenas, que queda VIVO fuera de la fusion y enlazado por P.10: injertarlo seria fabricar la repeticion nueva contra la que P.13 avisa |
| hacer las reglas VISIBLES | `brainstorming_efectivo` | **VIAJA** | paso 3 del resultado | el superviviente manda establecerlas y hacerlas cumplir, no visibilizarlas |
| mantenerse enfocado en el tema | `brainstorming_efectivo` | **VIAJA** | paso 3 del resultado | el superviviente centra el ENUNCIADO al principio pero no manda sostener el foco durante la sesion |
| formar grupos donde los participantes se conozcan y tengan confianza mutua | `brainstorming_efectivo` | **VIAJA** | paso 1 y condicion 4 del resultado | ningun otro miembro del triangulo habla de quien compone el grupo |
| separar las sesiones de generar de las de seleccionar | `brainstorming_efectivo` | **VIAJA** | paso 7 del resultado | el superviviente no menciona la convergencia en ninguna parte |
| que sin reglas la sesion degenera en reunion ordenada o en caos improductivo | `brainstorming_efectivo` | **VIAJA** | resumen del resultado | es el por que de las reglas, y el superviviente solo las enumera |
| ir por cantidad | `brainstorming_divergente` | **VIVE DENTRO** | paso 3 del resultado, ya estaba | el superviviente ya manda ir por cantidad; viaja solo el matiz sobre calidad |
| el registro visual y la pizarra como soporte | `brainstorming_divergente` | **VIVE DENTRO** | paso 5 del resultado, ya estaba | el superviviente ya captura y mueve en Post-its; viaja solo el soporte alterno |
| diferir el juicio | `brainstorming_divergente y brainstorming_efectivo` | **VIVE DENTRO** | paso 3 del resultado, ya estaba | es la primera regla del paso 2 del superviviente |
| las ideas descabelladas | `brainstorming_efectivo` | **VIVE DENTRO** | paso 3 del resultado, ya estaba | el superviviente ya manda fomentar ideas locas |
| que el brainstorming no es la unica tecnica de ideacion | `brainstorming_divergente` | **YA NO APLICA** | se retira | es un encuadre del libro sobre el lugar de la tecnica, no material del procedimiento, y no hay linea del superviviente donde colgarlo sin inventarsela |

**14 piezas: 9 `VIAJA`, 4 `VIVE DENTRO`, 1 `YA NO APLICA`.**

> **LA FILA QUE MAS ENSENA es la de construir sobre las ideas de otros, y es `P.13` en estado
> puro.** Es la unica regla del triangulo que el superviviente no dice, asi que **la LINEA viaja**;
> pero **el PROCEDIMIENTO de esa linea vive en `construir_sobre_ideas_ajenas`, que queda VIVO fuera
> de la fusion** por ser el nodo colgado del par 586 y que `P.10` manda enlazar. **Injertarlo
> tambien seria fabricar la repeticion nueva contra la que `P.13` avisa**: *una perdida falsa
> obliga a injertar en el superviviente algo que ya esta, y eso es como se fabrica una repeticion
> nueva el dia de la pasada*.

---

#### EL MAPA DE MOVIMIENTO DE LA ALTERNANCIA: **de 4 mas 3 mas 4 a SIETE pasos**

**IMPRESA desde el plan sellado**, comando corrido en esta vuelta:

```
python scripts/loop/vuelta33_tabla_mapa.py docs/loop/PLAN_V38_OPD04_ALTERNANCIA.json
```

**Prefijos**: `P` el superviviente `pensamiento_convergente_divergente`, `G`
`generar_multiples_opciones`, `T` `design_attitude_vs_decision_attitude`.

| paso del resultado | de que origenes sale | el motivo de perdida de linea que lo modifica |
|---:|---|---|
| **1** | P1, G1, T2 | LOS TRES DICEN LA MISMA ORDEN y el superviviente la dice entera. De los donantes VIAJA solo el matiz: deliberadamente, y la energia ademas del tiempo. |
| **2** | G2 | VIAJA ENTERO. El superviviente no pone limite a la divergencia en ninguno de sus cuatro pasos, y sin limite la orden de divergir no tiene freno escrito. |
| **3** | P2 | VERBATIM del superviviente. |
| **4** | G3 | VIAJA ENTERO. Es lo unico del donante que no es la orden de divergir, y el superviviente no lo dice. |
| **5** | P3, T3 | LA ALTERNANCIA ES DEL SUPERVIVIENTE y viaja el matiz del donante, que nombra las TRES actividades entre las que se alterna. Ninguna de las tres esta nombrada en el superviviente. |
| **6** | P4, T4 | LAS DOS CARAS DE LA MISMA DISCIPLINA, soltar lo bueno y no agarrar lo primero. La segunda VIAJA del donante. |
| **7** | T1 | VIAJA ENTERO y va al final porque es la actitud que sostiene a los seis anteriores, no un paso que se ejecute antes que ellos. El superviviente no la nombra. |

**Y LAS CONDICIONES pasan de 2 mas 2 mas 1 a TRES:**

| condicion del resultado | de que origenes sale | el motivo que la modifica |
|---:|---|---|
| **1** | PC1, GC1, TC1 | LA MISMA CONDICION EN LOS TRES NODOS, escrita tres veces. |
| **2** | PC2 | VERBATIM del superviviente. |
| **3** | GC2 | VIAJA entera: es la unica que situa el momento y el superviviente no lo situa. |

#### LA TABLA DE PERDIDAS DE LA ALTERNANCIA (`P.13`)

| pieza | de que nodo | clase P.13 | a donde va | por que |
|---|---|:---:|---|---|
| alternar entre investigacion de mercado, prototipado y generacion de forma no lineal | `design_attitude_vs_decision_attitude` | **VIAJA** | paso 5 del resultado | el superviviente alterna entre GENERAR y SELECCIONAR y no nombra ninguna de esas tres actividades |
| evitar adoptar la primera solucion razonable | `design_attitude_vs_decision_attitude` | **VIAJA** | paso 6 del resultado | el superviviente lo dice en su resumen, que la cultura occidental favorece la convergencia rapida, y no lo tiene como paso |
| aceptar la ambiguedad y la incertidumbre como parte del proceso | `design_attitude_vs_decision_attitude` | **VIAJA** | paso 7 del resultado | no esta en el superviviente |
| el contraste ACTITUD DE DISENO contra ACTITUD DE DECISION de Collopy y Boland, con el Design Squiggle de Damien Newman | `design_attitude_vs_decision_attitude` | **VIAJA** | resumen del resultado | ES LA PIEZA MAS CARA DE ESTA FUSION: un concepto con autores nombrados y con su figura. Perderla seria borrar material atribuido |
| el deadline claro para la fase de divergencia, y la paralisis por analisis | `generar_multiples_opciones` | **VIAJA** | paso 2 del resultado | el superviviente manda divergir y no le pone freno en ninguno de sus pasos |
| la polinizacion cruzada entre ideas distintas | `generar_multiples_opciones` | **VIAJA** | paso 4 del resultado | no esta ni en el superviviente ni en el otro donante |
| el set documentado de al menos 3 a 5 alternativas evaluadas | `generar_multiples_opciones` | **VIAJA** | entregable del resultado | el entregable del superviviente cuenta ciclos y no cuenta alternativas |
| que los plazos ponen un limite productivo a la exploracion, y que no conformarse con la primera buena idea separa lo incremental de lo verdaderamente creativo | `generar_multiples_opciones` | **VIAJA** | resumen del resultado | es el por que del paso 2 que viaja; sin el, la orden del deadline queda sin motivo escrito |
| dedicar tiempo Y ENERGIA a explorar antes de converger | `design_attitude_vs_decision_attitude` | **VIVE DENTRO** | paso 1 del resultado, ya estaba | el superviviente ya manda dedicar tiempo explicito; viaja la energia |
| generar deliberadamente multiples alternativas antes de elegir una | `generar_multiples_opciones` | **VIVE DENTRO** | paso 1 del resultado, ya estaba | es el paso 1 del superviviente dicho con otras palabras; viaja el adverbio |
| mentalidad y proceso de trabajo del equipo, como ENTREGABLE | `design_attitude_vs_decision_attitude` | **YA NO APLICA** | se retira del entregable; su contenido vive en el resumen | una mentalidad no es un documento y el superviviente entrega uno. Retirarla del entregable no pierde material: viaja entero al resumen |

**11 piezas: 8 `VIAJA`, 2 `VIVE DENTRO`, 1 `YA NO APLICA`.**

---

#### LO QUE QUEDA PARA LA VUELTA QUE EJECUTE, escrito para que no haga falta volver a pensarlo

1. **`P.16`, QUIEN FABRICA LIMPIA.** Cada fusion fabrica **UNA duplicada nueva**, las dos ya
   nombradas en su plan: `prototipado_rapido.nodos_previos` en el taller y
   `analisis_y_sintesis.nodos_siguientes` en la alternancia. **Las limpia la misma operacion que
   las hace.**
2. **La guarda de simetrizacion**, con la lista entera en cada plan: `symmetrize_added` tiene que
   traer **16** entradas para `reglas_brainstorming` y **4** para
   `pensamiento_convergente_divergente`, **exactamente esas**.
3. **El enlace del cuarto miembro NO se escribe a mano**: la fusion del taller lo deja puesto. Lo
   que si hay que hacer es **comprobarlo despues**, porque una arista que se espera gratis y no
   llega es la peor de todas.
4. **Los tres que quedan vivos** (`reglas_brainstorming`, `pensamiento_convergente_divergente` y
   `construir_sobre_ideas_ajenas`) **se enlazan por `P.10`**, que es la tercera salida, y toda
   arista nueva se escribe **resuelta al dia de su escritura** (`P.9`).
5. **El campo `superviviente` de `OP-D-04` sigue en `null`** y **no se toca en esta vuelta**: el
   fichero de operaciones tiene UN campo `superviviente` y esta operacion produce **DOS**. Escribir
   uno de los dos seria mentir por omision y escribir los dos seria estrenar un formato. **Se trae
   como pregunta, no se resuelve.**
6. **Y sobre todo: la PARADA DE DOCTRINA del pie de la undecima tanda.** Si la regla
   `FAMILIA DECLARADA` gobierna sobre los tres pares del cuarto miembro, las tres lecturas se
   registran con la clase de su familia, que en los tres pares ya escritos es **`A`**, y entonces
   **estas dos fusiones no se ejecutan.**

---

#### `OP-D-04`, EL ACTA DEL AUDITOR DE LA VUELTA 38, LEIDA EL 19 ago 2026 (vuelta 39): **LAS DOS FUSIONES QUEDAN AUTORIZADAS**

**Linea de registro, con las lineas del acta citadas porque la regla 1 del `EJECUTOR.md` no admite
afirmar el estado del registro sin la medicion del dia al lado.** El acta vive en
`docs/loop/ACTA_AUDITOR.md` y se leyo hoy entera en su ultimo bloque (lineas 7.995 a 8.126, la
seccion 4 de adjudicaciones, la 5 de pendientes y la 7 de condiciones de parada).

| lo que el acta resuelve | donde lo dice, leido hoy |
|---|---|
| **LAS TRES LECTURAS DEL CUARTO MIEMBRO SE CONFIRMAN EN `D`.** `LD-96` sostenida en `D` por letra (el segundo polo del `9.22` no aplica porque la direccion de Juran hacia divergente devuelve procedimiento; el `9.6.3` prohibe pesar el solape) y `LD-98` sostenida en `D` por letra (el `67.6` mas la prueba del `9.6.2`). **La condicion de parada de la `DECISION 3` del fundador no se dispara.** | `ACTA_AUDITOR.md` seccion 4, puntos **a1** y **a2** (lineas 7.997 a 8.015) |
| **LAS DOS ELECCIONES DE `P.8` SE CONFIRMAN**, y ademas coinciden **5 de 5** con la relectura ciega del auditor junto a las tres `LD`. | `ACTA_AUDITOR.md` seccion 6, *Esta tanda (vuelta 38): mas 8 puestos de fondo (LD-96, LD-97, LD-98 y las dos elecciones de P.8 a ciegas...)* (lineas 8.094 y 8.095) |
| **`FAMILIA DECLARADA` NO GOBIERNA LAS TRES LECTURAS AUTORIZADAS**, adjudicado como choque entre reglas por el **orden de fuentes de `AUDITOR.md` seccion 0**: la excepcion del fundador vive en `docs/plan/BANCO_DEL_PLAN.md`, fuente de **rango 1**, y `FAMILIA DECLARADA` vive en `docs/INTRA_DOMINIO_INFORME.md`, fuente de **rango 3**. **Los tres pares `A` ya escritos del racimo (234, 823 y 834) NO SE TOCAN**: la regla sigue entera para los pares de cola de racimos declarados. | `ACTA_AUDITOR.md` seccion 4, punto **a3** (lineas 8.016 a 8.048) |
| **CONSECUENCIA ESCRITA POR EL AUDITOR: *LAS DOS FUSIONES QUEDAN AUTORIZADAS*.** | `ACTA_AUDITOR.md` linea 8.046, dentro de la `CONSECUENCIA` de **a3** (lineas 8.043 a 8.048) |
| **El campo `superviviente` de `OP-D-04` QUEDA EN `null`** y la verdad va en la nota de cierre nombrando los dos supervivientes y los dos planes sellados. Resuelve el punto 5 de *LO QUE QUEDA PARA LA VUELTA QUE EJECUTE*, que lo dejaba como pregunta. | `ACTA_AUDITOR.md` seccion 4, punto **a4** (lineas 8.049 a 8.056) |
| **Titulo y etiqueta del nodo del taller NO SE TOCAN** en esta fusion; el aviso de `P.8` va como pendiente de catalogo al fundador y no bloquea. | `ACTA_AUDITOR.md` seccion 4, punto **a6** (lineas 8.062 a 8.066) |

**LA PARADA DE DOCTRINA DEL PIE DE LA UNDECIMA TANDA, la del punto 6 de *LO QUE QUEDA PARA LA
VUELTA QUE EJECUTE*, QUEDA CERRADA:** el acta la recorre en su seccion 7 y la declara *adjudicado
por letras ya escritas (a3)*, con **ninguna condicion de parada cumplida** (linea 8.115).

> **Y va dicho lo que el acta NO hace, porque un registro que solo cuenta lo favorable no se puede
> auditar:** el acta deja **dos recomendaciones al fundador que no bloquean** (una linea general de
> prelacion para este choque, y el esquema de `OPERACIONES.jsonl` frente a operaciones con dos
> supervivientes, mas el titulo del nodo del taller), y **cuatro pendientes heredados vivos**
> (`ACTA_AUDITOR.md` seccion 5, cabecera en la 8.073 y cuerpo en las 8.074 a 8.086).

---

## `OP-D-04` CERRADA: **LAS DOS FUSIONES EJECUTADAS Y EL RESTO ENLAZADO** (19 ago 2026, vuelta 39)

**CORRECCION DECLARADA sobre TODO lo de arriba, y no se borra ni una linea.** Los dos estados
anteriores de `OP-D-04` (el de la vuelta 37, *FUSION EN PARADA*, y el de la vuelta 38, *LOS DOS
SUPERVIVIENTES ELEGIDOS Y LOS DOS PLANES SELLADOS*) se escribieron con la fusion **EN ESPERA**, y
la fusion **YA ESTA HECHA**. Los dos se quedan enteros donde estan, porque una correccion que tapa
lo que corrige no se puede auditar; esta seccion dice que cambio y que lo movio.

**QUE LO DESBLOQUEO, y son dos cosas distintas que no se confunden.** La `DECISION 2` del fundador
mandaba que la fusion **esperara el acta del auditor**. El acta de la vuelta 38 llego, y en su
seccion 4 **confirma las tres lecturas dirigidas en `D`** (`a1` y `a2`), **confirma las dos
elecciones de `P.8`**, y **adjudica en `a3` que `FAMILIA DECLARADA` no gobierna esas tres
lecturas**, por el orden de fuentes de `AUDITOR.md` seccion 0. Su `CONSECUENCIA`, textual: *LAS DOS
FUSIONES QUEDAN AUTORIZADAS* (linea 8.046, leida hoy). **Esta vuelta no volvio a decidir nada: solo
ejecuto lo sellado.**

**Y ANTES DE ESCRIBIR NADA, LAS DOS SIMULACIONES SELLADAS SE RE-CORRIERON: `BYTE IGUAL` las dos**
contra `SALIDA_V38_SIM_TALLER.txt` y `SALIDA_V38_SIM_ALTERNANCIA.txt` (`md5` `e3a3c927` y
`ff115810`). **Nada del grafo se habia movido desde el sellado, y eso se comprobo en vez de
suponerse.**

### TABLA 1: LOS SIETE NODOS DEL ACTO, ANTES Y DESPUES

| nodo | papel | fuente | pasos antes | pasos despues | condiciones | vivo hoy |
|---|---|---|---:|---:|---:|:---:|
| `reglas_brainstorming` | **superviviente de EL TALLER** | Business Model Generation (Osterwalder) | 5 | 7 | 4 | **si** |
| `brainstorming_divergente` | absorbido por `reglas_brainstorming` | Change by Design, Revised and U - Tim Brown | 4 | 4 | 2 | no, **deprecado** |
| `brainstorming_efectivo` | absorbido por `reglas_brainstorming` | Change by Design | 4 | 4 | 2 | no, **deprecado** |
| `pensamiento_convergente_divergente` | **superviviente de LA ALTERNANCIA** | Change by Design | 4 | 7 | 3 | **si** |
| `generar_multiples_opciones` | absorbido por `pensamiento_convergente_divergente` | Change by Design | 3 | 3 | 2 | no, **deprecado** |
| `design_attitude_vs_decision_attitude` | absorbido por `pensamiento_convergente_divergente` | Business Model Generation (Osterwalder) | 4 | 4 | 1 | no, **deprecado** |
| `construir_sobre_ideas_ajenas` | **el colgado, NO se funde** | Change by Design | 3 | 3 | 1 | **si** |

### TABLA 2: EL CUARTO MIEMBRO DEL RACIMO MIXTO, QUE NO ES DEL ACTO

| nodo | dominio | fuente | vivo | como quedo enlazado |
|---|---|---|:---:|---|
| `brainstorming` | quality | Juran's Quality Handbook_ The C - Joseph A. Defeo | **si** | `reglas_brainstorming` lo nombra en `nodos_siguientes` y el nombra a `reglas_brainstorming` en `nodos_previos` |

### TABLA 3: LOS TRES VIVOS Y SUS TRES PARES (`P.10`, tercera salida)

| par | como llego | extremo A lo declara en | extremo B lo declara en |
|---|---|---|---|
| `reglas_brainstorming` con `pensamiento_convergente_divergente` | **solo**, redirigido por la fusion del taller y simetrizado por el paso 5 | `nodos_previos` | `nodos_siguientes` |
| `reglas_brainstorming` con `construir_sobre_ideas_ajenas` | **escrito por `P.10` en esta vuelta**, con los dos extremos de una vez | `nodos_siguientes` | `nodos_previos` |
| `pensamiento_convergente_divergente` con `construir_sobre_ideas_ajenas` | **solo**, redirigido por la fusion de la alternancia y simetrizado por el paso 5 | `nodos_previos` | `nodos_siguientes` |

### TABLA 4: EL CENSO, TRAMO A TRAMO

| momento | ficheros | vivos | deprecados |
|---|---:|---:|---:|
| apertura de la vuelta 39 | 3.853 | 3.538 | 315 |
| tras EL TALLER | 3.853 | 3.536 | 317 |
| tras LA ALTERNANCIA | 3.853 | 3.534 | 319 |
| **recontado al cierre, ahora mismo** | **3.853** | **3.534** | **319** |

(las tres primeras filas son las que imprimio cada corrida de
`scripts/loop/vuelta39_fundir.py`; la cuarta la recuenta este script AL CIERRE)

**LAS CUATRO TABLAS NO ESTAN TECLEADAS:** las imprime `scripts/loop/vuelta39_tabla_cierre.py`
leyendo `dataset/nodos`, los dos planes sellados y `git show 03e8e0e8` para el *antes*. Salida
entera en `docs/loop/SALIDA_V39_TABLA_CIERRE.txt`.

### LO QUE SE VERIFICO, punto por punto de la propia `verificacion` de la operacion

| punto, tal como lo escribe `OPERACIONES.jsonl` | como quedo |
|---|---|
| **1**, `Gate 0 verde` | **`GATE 0: OK`, exit 0**, en las tres corridas del ciclo (tras el taller, tras la alternancia, tras el enlace). 3.853 compilados, 3.534 activos, 319 deprecados, alcanzabilidad **100 por ciento** |
| **2**, `sin congelados que liberar` | no aplica, y ya lo decia la propia operacion |
| **3**, `cada nodo resultante dentro del estandar, o dentro de la excepcion de clase de OP-F-01` | **LOS DOS QUEDAN EN SIETE PASOS**, uno por encima del estandar de 3 a 6, y entran por la puerta que la propia verificacion nombra. **PERO el instrumento de la casa NO ENTREGA HOY** y hay **UNA SENAL QUE DISPARA**: ver el bloque de abajo, que es un DISCUTIBLE |
| **4**, `recomputo del cierre transitivo tras el acto (banco 9.21)` | **CORRIDO** (`scripts/plan/recomputo_3388.py`, `SALIDA_V39_RECOMPUTO_3388.txt`): actos **333** sin cambio, ABIERTOS de **54 sobre 247** nodos a **54 sobre 243** (los cuatro absorbidos), el acto de **siete pasa a ser uno de tres** (`ABIERTOS por tamano` de `7: 2` a `7: 1` y de `3: 25` a `3: 26`), nodos en actos de **845 a 841**, `A` vigentes resueltas de **574 a 569**. **Las cuatro comprobaciones del `08_VERIFICACION.md`: OK las cuatro** |
| **5**, `cada perdida quedo en el bloque del que proviene, o en el superviviente` | **CORRIDO** (`scripts/loop/verificar_mapas_destejido.py` con los cinco planes sellados, `SALIDA_V39_VERIFICADOR_MAPAS.txt`): **5 tablas, 31 filas, 0 discrepancias**, varas 1 y 2 CORRIDAS |
| **6**, `el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto` | **hecho en la vuelta 37**, 21 de 21 por `P.5`, y el acta de la vuelta 38 lo re-verifico |

### EL DISCUTIBLE DEL PUNTO 3, y va escrito porque callarlo seria la peor version de este cierre

**El instrumento de la casa se niega a entregar.** `scripts/costuras_internas.py` cae en **su
propia puerta de calibracion**: `INSTRUMENTO MAL CALIBRADO. No entrega nada`, porque
`plan_mejora_procesos`, que es su fixture, ya no aparece en la cola (mejor bloque **43,1** contra
un umbral de **44**). **La averia es ANTERIOR a esta vuelta y ajena a ella**, y **el umbral no se
afloja para que entregue**: eso seria arreglar la vara en vez de la pieza.

**Con la puerta caida, las dos senales se calcularon a mano sobre estos dos nodos, con las mismas
funciones y los mismos umbrales, y UNA DISPARA:**

| nodo | pasos | peor pareja (umbral 80) | mejor bloque (umbral 44) | dispara |
|---|---:|---:|---:|---|
| `reglas_brainstorming` **antes** | 5 | 54,3 | **47,7** | **BLOQUE** |
| `reglas_brainstorming` **despues** | 7 | 54,3 | **50,6** | **BLOQUE** |
| `pensamiento_convergente_divergente` **antes** | 4 | 46,2 | 0,0 | ninguna |
| `pensamiento_convergente_divergente` **despues** | 7 | 48,1 | 43,8 | ninguna |

> **LO QUE ESA TABLA DICE, Y LO QUE NO.** La senal de bloque de `reglas_brainstorming` **dispara**,
> **pero NO la enciende la fusion: ya disparaba antes**, con **47,7** sobre sus cinco pasos viejos,
> medido contra `git 03e8e0e8`. **La fusion la sube de 47,7 a 50,6 y no la crea**, y el corte que
> senala es el mismo de antes, tras el paso 2. Y el propio instrumento declara que **CITA, NO
> JUZGA**: un nodo en la cola es *una cita para leer, no una costura probada*. **Asi que esto no
> decide la clase por si solo y NO SE RESUELVE AQUI: va como DISCUTIBLE MARCADO al auditor.**
> **Y el margen del otro se dice igual:** `pensamiento_convergente_divergente` se queda en **43,8
> contra 44**, o sea **por dos decimas**.

### LO QUE ESTE CIERRE HACE Y NO ESTABA EN EL PLAN SELLADO, declarado y no silenciado

**`Gate 0` cayo en rojo a la primera**, con **un puente aprobado de `quality` apuntando al recien
deprecado `brainstorming_efectivo`**. El plan enumeraba las **17 referencias de NODO** y **no las
del registro de puentes**. Se resolvio con el instrumento de la casa,
`scripts/reanclar_por_resolutor.py`, **que mueve REFERENCIAS y jamas nodos** y va **por el
resolutor** (`P.1`): el ancla pasa a `reglas_brainstorming` con **`ancla_original`** guardando de
donde venia. **No es una decision recalculada, es la misma redireccion**, y el precedente esta
**medido tres veces en git**: `a2902995`, `06dd2922` y `33265c05`, que es el que creo el
instrumento precisamente para no cazar el mismo pez cuatro veces. **Va como DISCUTIBLE al
auditor.**

### LO QUE ESTE CIERRE NO HACE

- **No fija `superviviente`.** El campo **se queda en `null`**, y aqui **no por falta sino por
  sobra**: la operacion produce **DOS** y el esquema tiene **UN** campo. Lo adjudica el acta de la
  vuelta 38, punto **`a4`**. **Es el mismo `null` que `OP-D-03` pero por el motivo contrario, y por
  eso se dice.** La verdad vive en la nota, con los dos supervivientes y los dos planes nombrados.
- **No toca titulo ni etiqueta** de ninguno de los dos supervivientes (adjudicacion **`a6`**). El
  aviso de `P.8` sobre el nombre del nodo del taller **sigue vivo como pendiente de catalogo**.
- **No cambia el estado de la operacion.** Sigue en `LISTA`, **igual que `OP-D-01`, `OP-D-02` y
  `OP-D-03`, que tambien estan ejecutadas**. **PENDIENTE DE DOCTRINA heredado: el esquema no
  distingue una operacion HECHA de una pendiente.**
- **No borra un solo fichero.** Los cuatro absorbidos **conservan su texto entero**, que es lo que
  hace auditable la fusion.

### `OP-D-04`, EL ACTA DEL AUDITOR DE LA VUELTA 39, LEIDA EL 19 ago 2026 (vuelta 40): **EL CIERRE VERIFICADO ENTERO Y LOS CUATRO DISCUTIBLES ADJUDICADOS**

**19 ago 2026 (vuelta 40).** El acta del auditor de la vuelta 39
(`docs/loop/ACTA_AUDITOR.md`, cabecera en la linea 8.128, leida hoy) **verifica este cierre entero
por corrida propia y cierra con `CERO DISCREPANCIAS: todo lo cotejado calza al digito`** (linea
8.217): marcador recomputado por via propia, estado y tasa por dominio `BYTE IGUAL`, ciclo de
`Gate 0` re-corrido con el arbol limpio, motor, web y `tsc`, los dos `md5` de las simulaciones, el
recomputo del cierre transitivo, las fusiones releidas en el fichero, el puente re-anclado leido en
su `json` y la arista de `P.10` leida en sus dos ficheros. **Y adjudica los cuatro discutibles que
este cierre marco** (seccion 3, linea 8.250):

| discutible | adjudicacion del acta, con su linea leida hoy |
|---|---|
| **`d1`**, el re-anclaje del puente de `quality` | **PROCEDE** (linea 8.252). No fue recalcular una decision: el destino del ancla lo fijaba el plan sellado al fijar el superviviente. Lo cubren por extension `P.1`, **la regla escrita del propio `Gate 0`** (ningun puente aprobado apunta a un deprecado) y el **precedente triple medido en git**: `a2902995`, `06dd2922` y `33265c05`, el tercero el commit que creo el instrumento |
| **`d2`**, los dos resultantes de **siete pasos** | **PROCEDEN LOS DOS** (linea 8.267), por la **excepcion de clase de `OP-F-01` aplicada por su criterio escrito** (`01_FUENTES.md` linea 90, superar el estandar sin narracion repetida dentro; precedente en la linea 294 de este mismo fichero), con **lectura textual propia del auditor** de los siete pasos de cada uno. **La senal de bloque de `reglas_brainstorming` (50,6 contra 44) queda REGISTRADA COMO CITA, no como veredicto**, y **se encarga** (linea 8.275): cuando el instrumento de costuras vuelva a entregar, **ese nodo entra en su cola de lectura como cualquier citado, sin trato especial ni excepcion** |
| **`d3`**, la arista `reglas_brainstorming` hacia `construir_sobre_ideas_ajenas` y el ciclo dirigido que cierra | **PROCEDE Y SE QUEDA** (linea 8.278). Ninguna pagina fija direccion ni prohibe ciclos, y el auditor **lo midio**: el grafo vivo ya contiene **134 ciclos dirigidos de tres entre nodos vivos** (linea 8.283), o sea **especie corriente del catalogo y no un estreno** |
| **`d4`**, restaurar y rehacer el taller para no citar un log pisado | **PROCEDE** (linea 8.290). Ningun contenido commiteado se descarto, y rehacer en el orden correcto es lo que permite que la guarda cite **el log de verdad** en vez de una reconstruccion, que es lo que la regla 2 del `EJECUTOR` exige |

**NINGUNA CAIDA QUE CORREGIR: el reporte de la vuelta 39 salio limpio** (acta, seccion 6: *Caidas:
CERO del ejecutor, CERO del auditor*), y la caida de la vuelta 38 quedo corregida en su sitio.
**Nada de este registro se borra ni se reescribe: el discutible del punto 3 y el bloque de lo que
el cierre hizo fuera del plan se quedan tal como se escribieron, y esta seccion dice como se
adjudicaron.**

## `OP-D-05` SELLADA: **LA FUSION UNICA DE LA SELECCION DEL CEO** (19 ago 2026, vuelta 40)

**ESTA SECCION SE ESCRIBE ANTES DE EJECUTAR Y NO SE REESCRIBE DESPUES.** Lo que pase al ejecutar va en su propia seccion de cierre, debajo, para que el plan y su resultado se puedan comparar sin que uno tape al otro.

### EL DESTEJIDO: **NO HAY COSTURA QUE DESTEJER**, y va medido

La tabla de orden de este mismo fichero le cuenta a `OP-D-05` **UN destejido** y le pone de ancla `seleccion_ceo_fundador`. **Ese destejido tenia sujeto escrito**, aunque no en la seccion de la operacion sino en las razones de sus propios pares: la del puesto **673** dice que `seleccion_ceo_fundador` es **costura CONFIRMADA** en `docs/FICHA_SUBFUSION_GRADIENTE.md`, **doce pasos** y corte **1 a 4 contra 5 a 12**, y la del **492** describe el mismo corte.

**MEDIDO CONTRA EL NODO DE HOY** (`scripts/loop/vuelta40_destejido_opd05.py`, salida en `docs/loop/SALIDA_V40_OPD05_DESTEJIDO.txt`): el nodo tiene **cuatro pasos** y **una sola fuente**, y de las **seis huellas** del bloque 5 a 12 (mentor, brecha, CEO profesional, control, autoevaluacion, clausula) **sobreviven CERO**. **Ya se lo llevo `OP-F-04-HOR`**, commit **`2bd8dd76`**, medido con `git log --follow` y no supuesto. **Es el mismo caso que `OP-D-03`**, cuya celda de esa tabla dice que **dos de sus tres costuras estaban CONSUMIDAS por la fase 01**.

**Y EL INSTRUMENTO DE LA CASA, YA VIVO, DICE LO SUYO.** `scripts/costuras_internas.py` se reparo en esta misma vuelta y entrega con `exit 0`. De los tres nodos **cita UNO**, `errores_comunes_asignacion_roles` (bloque **45,5**, corte tras el paso 2), y **no cita** a los otros dos. **La cita se leyo con el texto delante**: los cinco pasos de ese nodo son **cinco errores distintos**, y por **`P.11`** son **advertencias y no procedimientos** (quitadas las frases que empiezan por NO, por EVITA o por DE VERDAD, lo que queda es una lista de punteros). **Comparten tema, no narracion**, que es lo que la senal de bloque no puede distinguir y su propio encabezado declara. **El instrumento CITA y NO JUZGA: aqui cito, se leyo, y la lectura dice que no hay costura.**

### `P.5` CON EL TEXTO YA ESTABLE: **UNA familia, no dos**

`scripts/loop/vuelta39_acto.py --op OP-D-05`, salida en `docs/loop/SALIDA_V40_OPD05_ACTO.txt`, corrida hoy:

| | medido el 19 ago 2026 |
|---|---|
| pares | **3 de 3 con clase, los tres `A` y los tres del ARCHIVO** (puestos **492**, **673** y **833**), cero lecturas dirigidas |
| nodos puente (`P.10`) | **CERO** |
| subconjuntos cerrados | **1, y es el acto entero**: la respuesta a `P.5` es **UNA familia** |
| aristas cojas | **CERO en los tres**: elegir superviviente **no cuesta ni una arista** |
| fuente | **los tres de *The Founder's Dilemmas***: **NO es acto de fuente mixta**, al contrario que los dos de `OP-D-04` |
| `9.3.1` sobre los pares `A` | de 3, **UNO** nombra ganador (el 673). **No hay GANADOR POR DERECHO**: la especie es **POR ELEGIR** |

**Los tres pares ya tenian clase del archivo y el destejido no los dejo rancios** (no hubo destejido), asi que **`P.5` se contesta sobre texto ya estable sin releer ni un par**, que es exactamente la condicion que la nota de la operacion pone.

### `P.8`: **DECIDE EL CONTENIDO**, y el cableado solo acompaña

**SUPERVIVIENTE: `seleccion_ceo_fundador`.**

- 1. PADRE DECLARADO POR EL ARCHIVO, que P.8 cuenta como CONTENIDO con el mismo peso que el texto. La razon del par 673 dice, literal: 'El corto cabe entero dentro del primer bloque del largo'. El corto es errores_comunes_asignacion_roles y el primer bloque del largo es lo que HOY es seleccion_ceo_fundador entero, sus cuatro pasos, porque el segundo bloque ya se lo llevo OP-F-04-HOR. O sea que el archivo declara CONTENIDO de uno contenido en el otro, y nombra al continente. Es ademas el UNICO de los tres pares que nombra ganador.
- 2. EL EJE COMUN ES EL TITULO DEL SUPERVIVIENTE. La razon del par 492 dice que los dos 'mandan decidir con intencion quien es el CEO en vez de darlo por hecho', y el titulo de seleccion_ceo_fundador es, literal, 'Decidir con intencion quien sera el CEO fundador'. La cabeza de la serie es el nodo cuyo titulo ES el eje, y los otros dos son sus caras: la razon del 833 los describe como 'el mismo reparto de titulos contado en positivo y en negativo'.
- 3. P.11 SOBRE LOS DOS DONANTES, y desempata sin hacer falta el cableado. errores_comunes_asignacion_roles es, por la vara, LINEA y no procedimiento: quitadas las frases que empiezan por NO, por EVITA o por DE VERDAD (confrontar EN LUGAR DE evitarlo, evaluar OBJETIVAMENTE si es REALMENTE la mejor opcion, SER CAUTELOSOS, EVITAR colocar por lealtad) lo que queda es una lista de punteros. Un checklist de advertencias no es la cabeza de un procedimiento. Y P.11 lo cierra por el otro lado: eso NO autoriza a borrarlas, asi que las cinco viajan y este plan dice en que grupo cae cada una.
- 4. PIEZA PROPIA QUE NADIE MAS TIENE: el catalogo concreto de roles alternativos (presidente de la junta, CTO, Chief Scientific Officer) es del superviviente y no aparece en ninguno de los otros dos. Es la unica pieza del acto que dice QUE HACER con la persona de la idea cuando no es el mejor CEO.

**EL CABLEADO, citado y NO usado para decidir:** `seleccion_ceo_fundador` **9**, `asignacion_de_titulos_ejecutivos` **4**, `errores_comunes_asignacion_roles` **4**. NUEVE contra CUATRO y CUATRO, y gana el nueve, que es el mismo que gana por contenido. Cuando las dos varas coinciden la regla no se luce, y por eso se dice que la que mandaba era la primera.

> **Y EL COSTE DE LA ELECCION ESTA MEDIDO: CERO aristas.** Los tres nodos tienen CERO aristas propias sin reciproco (bloque 6 de la salida del acto), asi que elegir a cualquiera de los tres no perdia ni una arista. La eleccion se juega entera en el contenido.

### EL MAPA DE MOVIMIENTO, celda a celda

**Prefijos:** `S` = `seleccion_ceo_fundador` (superviviente), `T` = `asignacion_de_titulos_ejecutivos`, `E` = `errores_comunes_asignacion_roles`.

| paso del resultado | de que origenes sale | motivo |
|---:|---|---|
| 1 | S1, E1, E5 | LAS TRES PIEZAS SON EL MISMO MOMENTO: la conversacion que se tiene ANTES, antes de fundar y antes de titular. Y las dos del donante son ADVERTENCIAS, no procedimientos: por P.11 califican el paso que el superviviente ya tenia en vez de anadir pasos, y por esa misma regla VIAJAN ENTERAS, porque una advertencia es lo mas facil de perder en una fusion y lo mas caro de recuperar. |
| 2 | T1, E2 | LA MISMA PIEZA VISTA POR LOS DOS LADOS: el donante T la IDENTIFICA y el donante E obliga a PONERLA A PRUEBA. Sueltas son media pieza cada una, y el superviviente solo la nombraba de refilon dentro de su paso 1. |
| 3 | S2, T2, T3 | LA VARA DE LA EVALUACION. El superviviente decia CONTRA QUE evaluar (la capacidad de ejecucion) y no decia QUE MIRAR para medirla. Del donante viajan las dos varas concretas que le faltaban, que son ademas las que su propio resumen usa para explicar el 47 por ciento. |
| 4 | S3, E3 | EL MISMO OBJETO: los titulos que NO son el de CEO. El superviviente trae el catalogo concreto de roles alternativos, que no tiene ninguno de los otros dos, y el donante trae la advertencia de no inflarlos. Juntas son la pieza entera; separadas, el catalogo se lee como un premio de consolacion. |
| 5 | T4, E4 | EL REPARTO DE PODER FORMAL, y el superviviente NO LO NOMBRABA en ninguno de sus cuatro pasos: ni la negociacion explicita del titulo ni la junta. Las dos piezas son de los donantes y las dos viajan, la segunda como advertencia por P.11. |
| 6 | S4, T5 | LA MISMA ACCION DICHA DOS VECES, y del donante viaja el POR QUE: no basta con documentar el acuerdo, hay que documentar el MOTIVO de cada titulo. Es la pieza que hace auditable la decision, que es de lo que trata el nodo. |

| condicion del resultado | de que origenes sale | motivo |
|---:|---|---|
| 1 | SC1, TC1, EC1 | LA MISMA CONDICION DICHA TRES VECES, y de los donantes viaja EL MOMENTO: las primeras etapas, antes de asignar titulos formales. |
| 2 | SC2, TC2, EC2 | LA MISMA CONDICION DICHA TRES VECES, y del donante viaja la senal mas util de las tres: que el equipo ESTA EVITANDO la conversacion, que es el sintoma que se ve desde fuera. |
| 3 | TC3 | PIEZA PROPIA DEL DONANTE, sin equivalente en el superviviente ni en el otro: el disparador EXTERNO, el unico de los tres que no viene del propio equipo. Viaja entera y sola, y por eso tiene grupo propio. |

**LA TABLA DE PERDIDAS DE `P.13`, derivada de los grupos: 21 de 21 piezas VIAJAN y CERO se pierden.** La regla de reparto adjudicada el 11 ago 2026 manda cada perdida al bloque del que proviene y la que no tenga bloque al superviviente; **con cero perdidas no hay nada que repartir, y eso se comprueba al cierre en vez de suponerse.**

### LO QUE LA SIMULACION DICE QUE VA A PASAR, sellado antes de ejecutar

| | esperado |
|---|---|
| redirecciones sobre nodos vivos | **8** |
| deprecados que nombran y NO se tocan | **0** |
| duplicadas que la fusion fabrica (`P.16`) | **2**, y las limpia la misma operacion |
| aristas de simetrizacion que el paso 5 tiene que anadir | **5**, ni una mas ni una menos |
| pasos del resultado | **6**, **DENTRO del estandar de 3 a 6**: esta operacion **no necesita la excepcion de clase** que `OP-D-04` si necesito |

**LOS REGISTROS QUE NO SON EL GRAFO, ENUMERADOS ANTES Y NO DESPUES.** La leccion de la vuelta 39: su plan enumero 17 referencias de NODO, no miro el registro de puentes, y Gate 0 cayo en rojo DESPUES de escribir. Aqui se enumera ANTES. El barrido (`scripts/loop/vuelta40_registros_no_grafo.py`) da **CERO registros vivos** que nombren a alguno de los tres, y la comprobacion dirigida sobre **los nueve `bridges_aprobados.json`** da **cero apariciones en los nueve**. **Aun asi se corre `reanclar_por_resolutor.py` entre la fusion y `run_phase1`**: es la practica que el acta de la vuelta 39 adjudico para toda fusion futura, y **una guarda que solo se corre cuando se sospecha no es una guarda.**


### `OP-D-05` CERRADA: **LA FUSION EJECUTADA** (19 ago 2026, vuelta 40)

**Esta seccion NO reescribe la de arriba.** El plan sellado se queda entero donde esta, y aqui va lo que paso al ejecutarlo, para que los dos se puedan comparar sin que uno tape al otro.

#### EL RESULTADO, releido en `dataset/nodos` y no copiado del plan

| | |
|---|---|
| superviviente | `seleccion_ceo_fundador`, **vivo**, **6 pasos** y **3 condiciones** |
| titulo y etiqueta | **sin tocar** (`a6`): *Decidir con intención quién será el CEO fundador* / *Elige con Cuidado a Tu CEO* |
| alias | `asignacion_de_titulos_ejecutivos`, `errores_comunes_asignacion_roles` |
| absorbidos | `asignacion_de_titulos_ejecutivos`, `errores_comunes_asignacion_roles`, **deprecados y con su texto entero** |
| estandar de pasos | **6, DENTRO del estandar de 3 a 6.** Esta operacion **no usa la excepcion de clase** de `OP-F-01` |
| campo `superviviente` | **ESCRITO** con `seleccion_ceo_fundador`, por el precedente **medido** de `OP-D-02`, que es la otra fusion de un solo superviviente y lo tiene escrito. **No es el `null` de `OP-D-03` ni el de `OP-D-04`** |

#### EL CENSO, RECONTADO AL CIERRE

| momento | ficheros | vivos | deprecados | enlaces |
|---|---:|---:|---:|---:|
| antes de la fusion (commit `002edf43`) | 3.853 | 3.534 | 319 | 16.869 |
| **recontado al cierre, ahora mismo** | **3.853** | **3.532** | **321** | **16.871** |

**LA ARITMETICA DE LOS ENLACES, comprobada entrada por entrada y no publicada a ojo:** `criterios_equity_split.nodos_previos` **menos 1**, `decision_fundador_solo_vs_equipo.nodos_siguientes` **menos 2** (nombraba a los DOS absorbidos y ademas ya al superviviente, asi que tres entradas colapsan en una), y `seleccion_ceo_fundador` **mas 1** en `nodos_previos` y **mas 4** en `nodos_siguientes` por la simetrizacion del paso 5. **Menos 1, menos 2, mas 1, mas 4, igual mas 2; y 16.871 menos 16.869 es 2.**

#### LA VERIFICACION DE LA PROPIA OPERACION, punto por punto

| punto, tal como lo escribe `OPERACIONES.jsonl` | como quedo |
|---|---|
| **1**, `Gate 0 verde` | **`GATE 0: OK`, exit 0** (`docs/loop/SALIDA_V40_GATE0.txt`), mas **71 etiquetas** y **seis assets** |
| **2**, `recomputo del cierre transitivo` | **CORRIDO** (`docs/loop/SALIDA_V40_RECOMPUTO_3388.txt`): actos de **333 a 332**, `CERRADOS` de **279 sobre 598** nodos a **278 sobre 595**, `ABIERTOS` **quietos en 54 sobre 243** porque el acto estaba CERRADO, nodos en actos de **841 a 838** y `A` vigentes de **569 a 566**. **Las cuatro comprobaciones del `08_VERIFICACION.md`: OK las cuatro.** El acto de tres **deja de existir**, porque sus tres nodos son ahora uno |
| **3**, `cada perdida quedo en el bloque del que proviene, o en el superviviente` | **CORRIDO** (`scripts/loop/verificar_mapas_destejido.py` con los SEIS planes sellados, `docs/loop/SALIDA_V40_VERIFICADOR_MAPAS.txt`): **6 tablas, 37 filas, 0 discrepancias**, varas 1 y 2 CORRIDAS. Y la tabla de `P.13`: **21 de 21 piezas VIAJAN y CERO se pierden**, o sea que **la regla de reparto se cumple POR VACIO**, y se dice asi en vez de darla por cumplida |
| **4**, `el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto` | **3 de 3 con clase, los tres del ARCHIVO** y **cero lecturas dirigidas** (`docs/loop/SALIDA_V40_OPD05_ACTO.txt`). **No hizo falta releer ninguno: no hubo destejido que los dejara rancios** |

#### EL PUNTO DEL ESTANDAR DE PASOS, CERRADO CON EL INSTRUMENTO YA VIVO

**El resultado queda en SEIS pasos**, dentro del estandar de 3 a 6, asi que **no hace falta la excepcion de clase**. Pero el instrumento de costuras, reparado en esta misma vuelta y **corrido otra vez DESPUES de la fusion**, **CITA al resultado**: bloque **48,4**, corte tras el paso 3. **Y hay que decir lo que la vuelta 39 si pudo decir de su caso y esta NO puede: LA FUSION ENCENDIO LA SENAL.** Antes de fundir, `seleccion_ceo_fundador` daba **43,6** y estaba **fuera** de la cola.

**ESO SE MIDIO EN VEZ DE SOSTENERSE** (`scripts/loop/vuelta40_senal_antes_despues.py`, salida en `docs/loop/SALIDA_V40_SENAL_ANTES_DESPUES.txt`), sobre los **tres** resultantes de fusion que esta campaña lleva:

| resultante | bloque ANTES | bloque DESPUES | movimiento | la cola |
|---|---:|---:|---:|---|
| `reglas_brainstorming` (`OP-D-04`, el taller) | 47,7 | **50,6** | **mas 2,9** | DENTRO antes y despues |
| `pensamiento_convergente_divergente` (`OP-D-04`) | 0,0 | **43,8** | **mas 43,8** | fuera antes y despues |
| **`seleccion_ceo_fundador`** (`OP-D-05`) | **43,6** | **48,4** | **mas 4,8** | **fuera antes, DENTRO despues** |

> **SUBE EN 3 DE 3, y el mecanismo es mecanico y no semantico:** fundir mete el vocabulario de tres nodos en menos pasos y mas densos, y la senal de bloque mide **solape de tokens** entre los dos bloques de la lista. **Una cita sobre un nodo recien fundido es lo esperable.** **Y LO QUE ESO NO AUTORIZA: descartar la cita.** El instrumento **cita y no juzga**, y una cita es **una lectura obligada**.

**LA LECTURA, hecha con el texto delante.** El corte que la senal propone es **tras el paso 3**: los pasos 1 a 3 contra los 4 a 6. **Los pasos 1 a 3 son la DELIBERACION** (con quien hablarlo, quien es la persona de la idea, con que vara se evalua) **y los 4 a 6 son la EJECUCION** (que rol alternativo darle, como se negocia el titulo, como se documenta). **El segundo bloque no vuelve a contar el primero: lo continua.** Y la pareja que el instrumento cita, los pasos 1 y 5, comparte **el vocabulario del acto** (CEO, titulos, conflicto) **y no su narracion**: el 1 es la conversacion que hay que tener y el 5 es la negociacion del titulo y la junta. **Es el limite que el propio instrumento declara en su encabezado, visto por el otro lado: un comparador de tokens no distingue tema de narracion.**

**VA COMO DISCUTIBLE MARCADO AL AUDITOR**, porque quien declara que no hay costura es el mismo que hizo la fusion que encendio la senal.

#### LO QUE ESTE CIERRE NO HACE

- **No enlaza nada por `P.10`.** El acto era **UNA familia entera de tres** y **los tres se funden**: no queda colgado ni tercera salida que escribir. **Se dice en vez de callarlo**, porque `OP-D-04` si la tuvo.
- **No cambia el estado de la operacion.** Sigue en `LISTA`, **igual que `OP-D-01` a `OP-D-04`, que tambien estan ejecutadas**. **PENDIENTE DE DOCTRINA heredado: el esquema no distingue una operacion HECHA.**
- **No borra un solo fichero.** Los dos absorbidos **conservan su texto entero**, que es lo que hace auditable la fusion.


### EL ACTA DE LA VUELTA 40 VERIFICA ESTE CIERRE Y ADJUDICA SUS CINCO DISCUTIBLES (19 ago 2026, vuelta 41)

**Esta seccion no reescribe ninguna de las dos de arriba.** El plan sellado y el cierre ejecutado se quedan enteros donde estan, y aqui va **lo que el auditor hizo con ellos**, leido hoy de `docs/loop/ACTA_AUDITOR.md` con su linea al lado, como manda la regla 1 del `EJECUTOR.md`.

#### LO QUE EL AUDITOR RE-CORRIO POR SU CUENTA (acta de la vuelta 40, seccion 1, linea 8389)

**No dio por bueno un solo numero de este cierre: lo volvio a medir entero.** La lista, tal como la escribe el acta:

| lo re-corrido | como salio, segun el acta |
|---|---|
| **estado y marcador** (`vuelta31_estado.py` por su via) | n **3.388**, A **575**, B **83**, C **8**, D **2.722**, tasa **17,0**; grafo **3.853** ficheros, **3.532** vivos, **321** deprecados, **16.871** enlaces. *CALZA AL DIGITO* con la tabla de cierre |
| **los huecos, por su propio comando** | numeracion contigua por bloques de dominio: **CERO huecos, CERO duplicados** |
| **la apertura que se midio tarde** | md5 propio: `SALIDA_V40_APERTURA.txt` y `SALIDA_V39_CIERRE.txt` **BYTE IGUAL** (`9331c557163d522c98ebd8ba03dbdccf` las dos) |
| **la puerta de costuras** | `scripts/costuras_internas.py` **exit 0** con los tres fixtures al digito, el aviso de borde y el retirado declarado; **umbrales 80 y 44 intactos** |
| **la fusion, contra el grafo** | superviviente vivo con 6 pasos, absorbidos deprecados con su texto, **cero vivos nombran a un absorbido**, y **la aritmetica de enlaces nodo a nodo leida de git**: menos 1, menos 2, mas 5, igual mas 2, de **16.869 a 16.871** |
| **el ciclo Gate 0 entero** | `run_phase1` mas etiquetas mas sync, **sha256 de los seis assets IDENTICOS** a los sellados (`master_graph 56ebc5a616f1`) |
| **las suites** | motor **25 de 25**, web **1.030 pasadas** y 3 saltadas, `tsc` cero lineas, **los tres exit 0** |
| **el recomputo del cierre transitivo** | **332 actos**, `CERRADOS` **278 sobre 595**, nodos en actos **838**, A vigentes **566**, **las cuatro comprobaciones OK** y el jsonl escrito **identico al commiteado** |
| **el verificador de mapas con la vara 2** | los **seis** planes sellados via `--json`: **6 tablas, 37 filas, 0 discrepancias**. Identico al sellado |
| **`OP-D-06` re-medida** | **9 actos**, tabla y nomina el **mismo conjunto**, **8 A y 1 C**, **9 de 9 con los dos nodos vivos**, y de las ocho razones A **ninguna nombra ganador** |

**Y LA CIEGA COINCIDIO 2 DE 2 EN EL FONDO** (acta, seccion 2, linea 8466): leyo el nodo fundido paso a paso **antes** de destapar razon alguna.

#### LOS CINCO DISCUTIBLES, ADJUDICADOS: **LOS CINCO PROCEDEN** (acta, seccion 4, linea 8522)

| | el discutible | la adjudicacion, con su linea |
|---|---|---|
| **d1** | la declaracion de **no costura** sobre el resultante, hecha por quien lo fundio | **PROCEDE** (linea **8524**). Y no por confianza: *la relei yo*. La relectura ciega del auditor **coincide**, los pasos 4 a 6 **continuan** a los 1 a 3, comparten **vocabulario** y **no narracion**. La guarda contra el juez y parte **ya existe y se cumplio**: la cita queda **registrada en la cola** como cualquier citado y el auditor la relee a la vuelta siguiente. **Precedente citable: el d2 del acta 39** (la cita de `reglas_brainstorming` registrada, no despachada) |
| **d2** | el **fixture fragil** de la puerta de costuras | **SE QUEDA con su aviso de borde** (linea **8535**). Retirar un fixture que **hoy** cumple el criterio **seria acomodar la puerta**, que es la especie que el banco 9 prohibe. Si `economia_circular` cae, **cae ruidosa**, y la reparacion **ya esta escrita en el criterio 5** |
| **d3** | usar **la cola que la casa llama rota** | **PROCEDE EN SU USO NODO A NODO** (linea **8542**). La medida de un nodo concreto **no depende de la tasa de la cola**; lo roto es el **ranking global** como criterio de lectura, y eso **espera el `MIN_BLOQUE` del fundador** |
| **d4** | el ancla `fases_traccion_producto`, que **ninguna pagina nombraba** | **PROCEDE** (linea **8549**). El encargo pedia criterio **escrito**, no criterio **preexistente**: quedo escrito, **medido antes de escribirse** y comprobable por cualquiera que corra el instrumento |
| **d5** | **no ejecutar** `OP-D-06` y convocar al auditor | **PROCEDE, y no es decision de alcance** (linea **8557**). Es **la letra del modo continuo**: una operacion cuyo texto no alcanza para ejecutarse sin decidir **detiene al ejecutor y convoca al auditor** |

#### LAS TRES PREGUNTAS, CONTESTADAS (acta, seccion 5, linea 8565)

1. **Un fixture que vive en la cola de lectura: NO SE PROHIBE** (linea **8567**). Los **criterios 4 y 5** del propio instrumento **ya cubren la caida entera**: si la lectura desteje al nodo, el fixture **queda rancio y se retira declarado**, con la puerta cayendo ruidosa un ciclo, **que es su comportamiento de diseno**. Elevarlo a prohibicion **seria doctrina nueva que ninguna caida real pide todavia**.
2. **La cola global NO es base de lectura** (linea **8574**), y **debe decirlo el propio instrumento**. Adjudicado por extension de su regla escrita (*cita y no juzga*). **Queda encargado y hecho en esta vuelta 41**: la linea va al final de la salida, sellada en `docs/loop/SALIDA_V41_COSTURAS_LIMITE.txt` con **exit 0**, y **la cifra la mide la propia corrida en vez de teclearse**.
   > **DISCREPANCIA DECLARADA, no resuelta copiando** (regla 2 del `EJECUTOR.md`): el encargo y el acta hablan del **42,3 por ciento**; **la corrida de hoy da 42,4** (**1.496** nodos en la cola sobre **3.532** activos). **La cola no se movio: se movio el catalogo.** El 42,3 se midio contra **3.534** activos, antes de que `OP-D-05` deprecara sus **dos** absorbidos en la vuelta 40. **Misma cola, dos activos menos, una decima arriba.** Se publica la de hoy y se deja la vieja a la vista.
3. **`OP-D-06` se ejecuta como UNA OPERACION CON NUEVE ACTOS, y el registro NO se toca** (linea **8578**). Citable: **su propio titulo** (*LOS NUEVE ACTOS DE DOS*), **su tabla sellada** con los nueve puestos, y **`P.5`**, que define el acto por el **subconjunto cerrado** y no por la fila del registro. Partirla en nueve `id_op` **moveria una cifra publicada (71 operaciones) sin que ninguna regla lo ordene**.

#### UNA CAIDA DE REPORTE QUE CORREGIR, DECLARADA SIN BORRAR LO VIEJO (acta, seccion 3, linea 8491)

**El texto viejo no se toca, para que la correccion se pueda auditar.** Lo que el reporte de la vuelta 40 escribio fue:

> ~~*los nueve son POR ELEGIR y los nueve piden `P.8`*~~

**Y esa frase SOBREPASA LA MEDICION.** El acta lo halla con nombre en su linea **8497**:

- El puesto **494** (`principio_calidad_mvp` con `producto_minimo_viable`) es **clase C**, no A.
- **La prueba de `9.3.1` no corre sobre el**, y **el propio instrumento lo imprime**: *la prueba de 9.3.1 solo corre sobre A* (`docs/loop/SALIDA_V40_OPD06_NUEVE_ACTOS.txt`).
- **Su via es el precedente de `OP-D-01`**: cura acoplada mayor, exactamente como el **aviso de solape** de esta misma pagina lo advierte, y **no una eleccion de superviviente**.

**LO CORRECTO, y es lo que rige desde aqui: OCHO piden `P.8`. El noveno pide su DECLARACION.** La caida **no mueve ningun dato**: ninguna cifra publicada cambia, solo la via de un acto.

### EL ACTA DE LA VUELTA 41 VERIFICA LO COMMITEADO Y ADJUDICA LA REANUDACION DEL ACTO 285 (19 ago 2026, vuelta 42)

**Esta seccion no reescribe ninguna de las de arriba.** Va **lo que el auditor hizo con la vuelta 41**, leido hoy de `docs/loop/ACTA_AUDITOR.md` con su linea al lado, como manda la regla 1 del `EJECUTOR.md`. El acta empieza en la linea **8651**.

#### LA VUELTA 41 QUEDO INTERRUMPIDA POR LIMITE DE SESION DE LA API, MEDIDO Y NO SUPUESTO (acta, seccion 1, linea 8662)

| lo medido | como lo dice el acta, con su linea |
|---|---|
| **la causa** | `docs/loop/ultimo_ejecutor.json` leido por el auditor: `terminal_reason` **api_error**, status **429**, *"You've hit your session limit"*, **869 segundos**, **56 turnos**. **Murio por LIMITE DE SESION, no por decision ni por guarda en rojo** (linea **8664**) |
| **lo commiteado y pusheado** | **9f9fc182** (la apertura, sola) y **aaa15cbd** (la TAREA 1 entera), con `origin/pasada-unica` en `aaa15cbd` comprobado por `git fetch` del propio auditor (linea **8677**) |
| **lo sellado en disco SIN commit** | **seis rutas**: `SALIDA_V41_ACTO285_LECTURA.txt`, `SALIDA_V41_ACTO285_PLAN.txt`, `PLAN_V41_ACTO285.json`, `vuelta41_lectura_acto.py`, `vuelta41_plan_acto.py` y `scripts/loop/v41_actos/`. **La fusion del 285 NO se ejecuto** (linea **8680**) |
| **el grafo** | **INTACTO**: `git status` sobre `dataset/`, `web/`, `engine/` y `docs/plan/` limpio. **El acto a medias es de REGISTRO, no de datos: ni un nodo tocado** (linea **8685**) |

#### LO COMMITEADO, VERIFICADO POR CORRIDA PROPIA DEL AUDITOR (acta, seccion 2, linea 8691)

| lo re-corrido | como salio, segun el acta |
|---|---|
| **la apertura** (`vuelta31_estado.py` por su via) | **BYTE IGUAL** a `SALIDA_V41_APERTURA.txt` **salvo la etiqueta del encabezado**, que es el parametro del instrumento. n **3.388**, A **575**, B **83**, C **8**, D **2.722**, tasa **17,0**; **cero huecos y cero duplicados**; grafo **3.853** ficheros, **3.532** vivos, **321** deprecados, **16.871** enlaces; **71** operaciones LISTA y **0** rotas (linea **8693**) |
| **la seccion de registros de la TAREA 1** | **54 lineas anadidas, cero borradas**, leida entera contra su propia acta de la vuelta 40: **las OCHO lineas citadas** (**8524**, **8535**, **8542**, **8549**, **8557**, **8567**, **8574**, **8578**) impresas hoy con `sed` **dicen exactamente lo que la seccion les atribuye** (linea **8705**) |
| **el parche de `scripts/costuras_internas.py`** | numstat **24 anadidas y 0 borradas**, diff entero leido: **solo lineas de impresion** al final de `main()`, **`UMBRAL_PAREJA` 80 y `UMBRAL_BLOQUE` 44 intactos**, ningun fixture tocado, y el porcentaje **calculado en la corrida** y no tecleado (linea **8712**) |
| **el instrumento de costuras entero** | re-corrido por el auditor: **exit 0**, y su cola calza **LINEA A LINEA** con `SALIDA_V41_COSTURAS_LIMITE.txt`. **1.496 sobre 3.532 es 42,36, publicado 42,4**: la **discrepancia declarada** del commit (42,4 contra el 42,3 del acta) esta **bien declarada y bien explicada**, misma cola con dos activos menos por `OP-D-05` (linea **8717**) |
| **el ciclo Gate 0 y las suites** | los **tres comandos** (`run_phase1 --reaplico-curaduria`, `etiquetas_de_cara --aplicar`, `sync_assets_web`) **exit 0 los tres**, **GATE 0: OK**, **71 etiquetas**, **seis assets** sincronizados, **las dos copias del grafo byte iguales a HEAD**; motor **25 de 25**, web **1.030 pasadas** y 3 saltadas, `tsc` **cero lineas**. El `phase1_run_log.json` **restaurado con `git restore`** para no pisar la evidencia commiteada de la vuelta 40, y **el arbol quedo byte igual** (linea **8724**) |

**Y LA CIEGA SOBRE EL ACTO 285 COINCIDIO 2 DE 2 EN EL FONDO** (acta, seccion 3, linea 8758): el auditor imprimio **primero** los dos nodos enteros de `dataset/nodos`, adjudico por escrito, y **solo despues** abrio la lectura y el plan del ejecutor. Su adjudicacion ciega: **ninguno de los dos tiene costura interna** y el superviviente es **`producto_unico_superior` por contenido**; anoto ademas que **el cableado crudo favorecia al ABSORBIDO** (10 contra 6), asi que si el ejecutor elegia por contenido **tenia que decirlo**. Al destapar: el plan sella eso mismo, con el cableado **impreso DESPUES del contenido** y medido por `P.1` en **6 contra 7**. **La prelacion se cumplio: el cableado favorecia al perdedor y NO decidio.**

**Y LA ARITMETICA DEL PLAN, RE-CONTADA POR EL AUDITOR CONTRA LOS FICHEROS** (linea **8767**): **7 redirecciones** (3 en `nodos_previos` vivos, 4 en `nodos_siguientes` vivos), **3 deprecados** que nombran y no se tocan, **0 duplicadas** fabricadas, **16 origenes verbatim**, **7 aristas** de simetrizacion esperadas, **6 pasos finales** dentro del estandar de 3 a 6, y la tabla de `P.13` con **16 de 16 que VIAJAN**.

#### **CERO CAIDAS, Y NINGUNA CASILLA QUE RELLENAR** (acta, seccion 5, linea 8837)

**No hay caida de reporte que corregir en esta vuelta, y se dice asi en vez de rellenar la casilla.** La razon esta medida, no supuesta: **la vuelta 41 no dejo reporte** (`REPORTE.md` seguia siendo el de la 40, ya auditada, acta linea **8687**), asi que **no habia material del ejecutor con discutibles que adjudicar**; y **lo que si commiteo salio limpio**: el acta cierra con **"Caidas: CERO del ejecutor en lo commiteado, CERO de clase o cifra, CERO del auditor"** (linea **8837**). La racha de caidas de reporte **se queda en UNA y no se rompe**, porque **una racha no se rompe con material ausente**: la rompe un reporte limpio, y ese sera el de esta vuelta 42 si sale limpio.

#### LAS ADJUDICACIONES DE LA VUELTA 41, QUE RIGEN DESDE AQUI (acta, seccion 4, linea 8783)

| | la adjudicacion, con su linea |
|---|---|
| **1** | **EL ACTO 285 SE RETOMA DESDE SU PLAN SELLADO, no se rehace de cero** (linea **8785**). Letra citable: todo encargo abre con *"Commitea y pushea lo pendiente en la rama activa antes de tocar nada"*, y **lo pendiente se incorpora, no se tira**; el precedente de `OP-D-05` es que una fusion **se ejecuta tal como esta sellada tras verificarse**. **CON UNA CONDICION, que es la regla 1 y no una regla nueva**: la vuelta 42 **re-corre los dos instrumentos** (`vuelta41_lectura_acto.py` y `vuelta41_plan_acto.py`) y comprueba que **REPRODUCEN** las dos salidas y el plan sellados. **Cualquier diferencia se declara y detiene la ejecucion del sellado hasta adjudicarse** |
| **2** | **EL CORTE POR LIMITE DE SESION NO ES CAIDA DE DICTADO NI CONDICION DE PARADA** (linea **8796**). La letra de *fallo tecnico repetido* pide **hook o Gate 0 en rojo dos vueltas seguidas por la misma causa**: aqui el Gate 0 esta **verde por corrida propia** y el corte vino de la **cuota de la API**, que el propio bucle ya maneja esperando y reintentando. **Se registra con nombre y no acumula credito contra nadie** |
| **3** | **DOS COMMITS POR ACTO DESDE LA VUELTA 42** (linea **8802**), adjudicado **por extension y no como doctrina nueva**: **el plan sellado con su lectura en un commit pusheado ANTES de fundir; la fusion ejecutada en otro**. Extiende el *commit y push por acto* del encargo 41 por su propia logica y por la leccion de hoy: **un corte de sesion no debe poder dejar un sellado sin commit**. Es la misma especie que la regla del hueco de acta: **lo no registrado no existe** |

**LOS SEIS FICHEROS SIN COMMIT SE COMMITEARON EN ESTA VUELTA 42, TAL COMO QUEDARON**, que es lo que el propio auditor dejo escrito como discutible **(iii)** de su acta (linea **8815**): los dejo sin commitear **a proposito**, porque **son obra del ejecutor y los commitea el ejecutor de la 42 con su mensaje declarado**. Hecho en el commit **2414e7d9**, sin retocar una linea, y con la declaracion de que **la fusion del 285 no se ejecuto**.

## `OP-D-06`, ACTO 1 DE NUEVE (puesto 285): **`producto_unico_superior` ABSORBE A `superioridad_producto_beneficios`** (19 ago 2026, vuelta 42)

**EL PLAN SE SELLO EN LA VUELTA 41 Y SE REPRODUJO POR INSTRUMENTO EN LA 42 ANTES DE EJECUTARSE**, que es la condicion exacta que la adjudicacion 1 del acta de la vuelta 41 puso (`docs/loop/ACTA_AUDITOR.md` linea **8785**, leida hoy). Las tres reproducciones salieron **BYTE IGUALES**, medidas con `md5sum` y `diff` en esta vuelta:

| lo reproducido | instrumento corrido hoy | md5 del sellado y del reproducido |
|---|---|---|
| `docs/loop/PLAN_V41_ACTO285.json` | `python scripts/loop/vuelta41_plan_acto.py --puesto 285` | `33ec35d6d8709527303c3a40cfe097ce`, **diff vacio** |
| `docs/loop/SALIDA_V41_ACTO285_LECTURA.txt` | `python scripts/loop/vuelta41_lectura_acto.py --puesto 285` | `ee1fd3a4682fb63e78a3e9c22f0d39ca`, **diff vacio** |
| `docs/loop/SALIDA_V41_ACTO285_PLAN.txt` | salida por pantalla de `vuelta41_plan_acto.py` | `1fb2c4c86748df05ae77a7727a81e17a`, **diff vacio** |

**CERO DIFERENCIAS QUE DECLARAR, y por eso el sellado se ejecuta.** La reproduccion entera va sellada en `docs/loop/SALIDA_V42_ACTO285_REPRODUCCION.txt`.

### EL DESTEJIDO DEL ACTO: **SIN COSTURA QUE DESTEJER EN NINGUNO DE LOS DOS**

`scripts/loop/vuelta41_lectura_acto.py --puesto 285`, bloque (b), sobre la cola que el instrumento ya entrego (`docs/COSTURAS_INTERNAS.jsonl`, **1.496** nodos):

| nodo | lo que CITA el instrumento | disparo |
|---|---|---|
| `producto_unico_superior` | 6 pasos, pareja **52,7** (pasos 2 y 3), bloque **45,4**, corte tras **3** | pareja **NO**, bloque **SI**, franja 44 a 45 **NO** |
| `superioridad_producto_beneficios` | 6 pasos, pareja **48,4** (pasos 3 y 5), bloque **44,7**, corte tras **4** | pareja **NO**, bloque **SI**, franja 44 a 45 **SI** |

**EL INSTRUMENTO CITA Y NO JUZGA, y la lectura textual con el texto delante dice que NO hay costura en ninguno de los dos:** en los dos nodos el segundo bloque **CONTINUA** al primero en vez de volver a contarlo. **La cita queda REGISTRADA en la cola y no despachada**, que es la practica que el acta de la vuelta 40 adjudico en su **d1** (linea **8524**) y el precedente del **d2** del acta 39. **Y la relectura ciega del auditor de la vuelta 41 coincidio en esto mismo antes de destapar el plan** (acta, linea **8758**).

### `P.5`: **UNA FAMILIA DE DOS**, con el subconjunto cerrado por transitividad sobre las A

El par **285** es **clase A** y su razon **NO nombra ganador**: la vara del verbo de `9.3.1` da **NO, es POR ELEGIR**. Los **cuatro** pares del archivo que meten un tercero son **163 (D)**, **461 (D)**, **835 (B)** y **1390 (D)**: **CERO terceros de clase A**, asi que **el acto ES de dos**, como la tabla sellada dice. **Y el par 835** (`brief_competitivo` con `producto_unico_superior`, **clase B**) **vuelve a la cola de relectura post fusion** porque el superviviente **cambia de texto**, como manda `08_VERIFICACION`.

**Los dos nodos son de la MISMA fuente**, *Winning at New Products* de Robert G. Cooper: **NO es acto de fuente mixta**. La regla de fuente primero de los tres cruces quedo satisfecha **por precedencia** (`OP-F-03` **HECHA** en su nota **3376**, apertura de hoy).

### `P.8` EN ORDEN: **manda el CONTENIDO, y el cableado PIERDE y se dice que perdio**

**EL CONTENIDO, leido primero:** el titulo de uno **es el sujeto** (*Tener un Producto Unico y Superior: El Factor Numero Uno de Rentabilidad*) y el del otro **es un predicado sobre ese sujeto** (*La superioridad de tu producto esta en los beneficios, no en las caracteristicas*); el **padre declarado por el grafo** de `producto_unico_superior` es `ocho_factores_exito_criticos`, la lista de factores criticos de Cooper de la que su titulo dice cual es; **la cifra del 5 veces mas probabilidad de exito, 4 veces mas participacion y 4 veces mas rentabilidad vive SOLO en su resumen**; y **la propia razon del archivo** describe al otro como un **desarrollo** del posicionamiento (*"El segundo desarrolla mas el discurso de venta segun ese posicionamiento, pero la instruccion es la misma"*). **Superviviente: `producto_unico_superior`.**

**EL CABLEADO, citado DESPUES y NO usado para decidir, y VA EN CONTRA DEL ELEGIDO:** grado por `P.1` de **6** para `producto_unico_superior` contra **7** para `superioridad_producto_beneficios`. **`P.8` dice que el cableado DESEMPATA y NO DECIDE, asi que aqui PIERDE contra el contenido, y se escribe que perdio en vez de esconderlo.** Es **el primer acto de esta campana en que las dos varas se separan**, y por eso queda dicho con todas sus letras.

> **Y EL COSTE DE LA ELECCION ESTA MEDIDO: CERO aristas.** Los dos nodos tienen **CERO aristas propias sin reciproco** (bloque (e) de la lectura), asi que elegir a cualquiera de los dos **no pierde ni una arista**: las reciprocas las reescribe la simetrizacion de `run_phase1`, paso 5. **La diferencia de UNO en el grado no cuesta nada.**

### EL MAPA DE MOVIMIENTO, celda a celda

**Prefijos:** `P` = `producto_unico_superior` (superviviente), `B` = `superioridad_producto_beneficios` (absorbido).

**Las dos tablas se IMPRIMEN y no se teclean** (regla 1 del `EJECUTOR.md`, cuarto renglon), generadas del plan sellado con `python scripts/loop/vuelta33_tabla_mapa.py docs/loop/PLAN_V41_ACTO285.json` y `... --campo grupos_condiciones`:

| paso del resultado | de que origenes sale | el motivo de perdida de linea que lo modifica |
|---:|---|---|
| **1** | P1, B2 | LA MISMA ACCION EN EL MISMO MOMENTO, y del donante viaja lo que le faltaba al superviviente: EL NOMBRE DEL INSTRUMENTO (voz del cliente, VoC) y la distincion entre necesidades y deseos, que es la que hace util el estudio. El superviviente decia QUE hacer y CUANDO; el donante dice COMO se llama y QUE se busca. |
| **2** | P2, P3 | LAS DOS CARAS DE LA MISMA INDAGACION: lo que el cliente no sabe pedir y lo que de verdad pesa cuando compra. Y ES EXACTAMENTE LA PAREJA QUE EL INSTRUMENTO DE COSTURAS CITA en este nodo (pasos 2 y 3, similitud 52,7). Esa cita NO disparo por pareja, porque el umbral es 80: no es una costura probada, es una cita. La fusion es el momento en que se resuelve, y resolverla juntando dos pasos del superviviente NO es destejer nada: destejer es partir un nodo en dos, y esto es lo contrario. |
| **3** | P4, B1 | EL SUPERVIVIENTE DABA LA ORDEN Y EL DONANTE DA EL PORQUE. Definir por beneficios sin la distincion features contra benefits es una consigna; con ella es un criterio que se puede aplicar. Las dos palabras inglesas viajan literales porque son el vocabulario con el que el lector va a reconocer la idea en cualquier otra pagina. |
| **4** | P5, B3, B4 | EL MISMO PASO CON SU METODO Y SU HORIZONTE. El superviviente decia CONTRA QUE comparar (los tres ejes) y no decia COMO; el donante trae el como (desarmar el producto) y ademas el aviso que ninguno de los dos tenia dos veces: que la comparacion contra la foto de hoy caduca. |
| **5** | P6, B5 | EL CIERRE DEL PROCEDIMIENTO, dicho por los dos: el donante manda TRADUCIR lo aprendido a una definicion, y el superviviente manda REVISAR esa definicion contra la trampa del precio bajo. Escribir y revisar lo escrito son el mismo paso partido en dos, y juntos dicen que la propuesta de valor no es un documento que se firma sino uno que se somete a prueba. |
| **6** | B6 | PIEZA PROPIA DEL DONANTE, sin equivalente en el superviviente: es el UNICO paso del acto que dice que hacer ANTES de construir. Viaja entera y sola, y por eso tiene grupo propio en vez de disolverse dentro de otro. |

| condicion del resultado | de que origenes sale | el motivo que la modifica |
|---:|---|---|
| **1** | PC1, BC2 | LA MISMA CONDICION DICHA DOS VECES, una por cada nodo. Se junta en una sola porque son la misma senal vista con las mismas palabras. |
| **2** | PC2, BC1 | LA MISMA CONDICION POR SUS DOS SINTOMAS: no tener propuesta de valor es el resultado, y definir por caracteristicas tecnicas es la causa. El donante aporta la causa, que es la que se ve antes. |

**LA TABLA DE PERDIDAS DE `P.13`, derivada de los grupos y no tecleada: 16 de 16 piezas VIAJAN y CERO se pierden** (salida de `vuelta41_plan_acto.py`, sellada en `docs/loop/SALIDA_V41_ACTO285_PLAN.txt`). La regla de reparto adjudicada el 11 ago 2026 manda **cada perdida al bloque del que proviene y la que no tenga bloque al superviviente**; **este acto no tiene reparto escrito en la tabla de `OP-D-06`** (solo lo tienen el **392** y el **341**), y **con cero perdidas no hay nada que repartir, y eso se comprueba al cierre en vez de suponerse**.

> **POR QUE ESTA TABLA VA EN PROSA Y NO CON `vuelta38_tabla_perdidas.py`, declarado en vez de callado:** ese instrumento pide un campo `motivo` por fila que **el esquema de `tabla_perdidas_p13` no trae** (sus claves son `pieza`, `texto`, `de`, `clase`, `destino`), y **`OP-D-05` publico la suya en prosa por lo mismo**. La cifra **no se teclea igual**: sale impresa de la corrida del plan.

### LO QUE LA SIMULACION DICE QUE VA A PASAR, sellado antes de ejecutar

| | esperado |
|---|---|
| redirecciones sobre nodos vivos | **7** (3 en `nodos_previos`, 4 en `nodos_siguientes`) |
| deprecados que nombran y NO se tocan | **3** (`enfoque_resolucion_problemas_lanzamiento_producto`, `prevencion_de_objeciones`, `spiral_development`) |
| duplicadas que la fusion fabrica (`P.16`) | **0**, y aun asi se mide antes de darlo por bueno |
| aristas de simetrizacion que el paso 5 tiene que anadir | **7**, ni una mas ni una menos |
| pasos del resultado | **6**, **DENTRO del estandar de 3 a 6** |
| censo esperado | ficheros **3.853** sin moverse, vivos **3.532 menos 1**, deprecados **321 mas 1** |

**LOS REGISTROS QUE NO SON EL GRAFO, ENUMERADOS ANTES Y NO DESPUES**, con la leccion de la vuelta 39 delante. **Y aun asi se corre `scripts/reanclar_por_resolutor.py` ENTRE la fusion y `run_phase1`**: es la practica que el acta de la vuelta 39 adjudico para toda fusion futura, y **una guarda que solo se corre cuando se sospecha no es una guarda.**

### `OP-D-06` ACTO 285 CERRADO: **LA FUSION EJECUTADA** (19 ago 2026, vuelta 42)

`python scripts/loop/vuelta39_fundir.py --plan docs/loop/PLAN_V41_ACTO285.json --ejecutar`, salida sellada en `docs/loop/SALIDA_V42_ACTO285_EJEC.txt` con **exit 0** y **LAS TRECE GUARDAS EN VERDE**. Las doce primeras ya salieron verdes en la simulacion previa; **la trece solo puede correr en `--ejecutar`**, porque es el censo, y va dicho asi en vez de decir trece en verde cuando la simulacion solo alcanza doce.

| lo medido al ejecutar | como salio |
|---|---|
| **censo (guarda 13)** | ANTES **3.853** ficheros, **3.532** vivos, **321** deprecados; DESPUES **3.853**, **3.531**, **322**. *El censo no se movio y los vivos bajaron en 1*: **OK** |
| **enlaces** | **16.871** antes, **16.878** despues, **mas 7 exactos**. Y la aritmetica cierra sin resto: las **7 redirecciones** son CAMBIOS de id en la lista del vecino (neto **cero**), el absorbido conserva su lista intacta (**cero**), y los **mas 7** son las **7 vistas reciprocas** que la simetrizacion le escribe al superviviente |
| **`P.16`, las duplicadas** | **CERO fabricadas**, tal como el plan predijo. Guarda 9 OK, y guardas 10 y 11 con **cero auto-arista y cero duplicada** tras resolver |
| **`reanclar_por_resolutor.py` ENTRE la fusion y `run_phase1`** | corrido, *nada que re-anclar: ninguna referencia apunta a un absorbido*. **Salio en blanco, como el barrido previo predijo, y se corrio igual**: una guarda que solo se corre cuando se sospecha no es una guarda |
| **la simetrizacion, EXACTA** | `vuelta39_guarda_simetrizacion.py`: **7 entradas en el log del ciclo, las 7 del superviviente, 0 de otros nodos, faltan 0 y sobran 0**, y las **7 releidas en el fichero**. Las dos guardas verdes |
| **ciclo Gate 0 de TRES comandos** | `run_phase1 --reaplico-curaduria` **GATE 0: OK**, `etiquetas_de_cara --aplicar` **71 etiquetas**, `sync_assets_web` **seis assets**. **Las dos copias del grafo BYTE IGUALES al cerrar**: `master_graph.json` de `dataset/metadata` y de `web/lib/assets`, md5 `0cbf023fb6993d06c3e8f8530f72fffb` las dos, **8.133.183 bytes**, sha256 `0a83990caef2` |
| **las suites** | motor **25 de 25**, web **80 ficheros con 1.030 pasadas** y 3 saltadas, `tsc` **cero lineas**. Los tres **exit 0** |
| **caso positivo antes y despues, mismo instrumento** | ANTES **15 PASAN y 21 CAEN** (exit 1, y **tiene que caer**); DESPUES **37 PASAN y 0 CAEN** (exit 0). **La cuenta sube de 36 a 37 comprobaciones y va explicado**: la comprobacion *la ficha del absorbido guarda su fuente* solo existe cuando la entrada de `merged_originals` existe, y antes no existia |

### LOS REGISTROS QUE NO SON EL GRAFO: **TRES VIVOS, Y LOS TRES SON DE ESCRITURA Y NO DE LECTURA**

`scripts/loop/vuelta40_registros_no_grafo.py` sobre los dos nodos, **173.874 ficheros de texto barridos**, salida en `docs/loop/SALIDA_V42_ACTO285_REGISTROS.txt`. **Y AQUI HAY UNA DIFERENCIA CONTRA `OP-D-05` QUE HAY QUE DECIR EN VEZ DE CALLAR**: aquella dio **CERO** registros vivos y esta da **TRES**.

| el registro vivo | quien lo escribe, medido hoy | quien lo lee |
|---|---|---|
| `docs/GRADIENTE_PARES.jsonl` | `scripts/gradiente_pares.py` linea 40 | **NADIE**: cero lectores en `scripts/`, `web/lib`, `web/app` y `engine/` |
| `docs/PASO_NODO_CANDIDATOS.jsonl` | `scripts/paso_contra_nodo.py` linea 63 | **NADIE**, por la misma busqueda |
| `scripts/rumbos/_ultima_corrida.json` | `scripts/rumbos/prueba_rumbos.py` linea 290 | **NADIE**, y ademas **`.gitignore` lo declara artefacto transitorio** cuya vara es `linea_base_rumbos.json` |

**LA CLASE `VIVO` DEL INSTRUMENTO ES UN CAJON RESIDUAL, NO UNA CLASIFICACION POSITIVA**: `clase_de()` devuelve `VIVO` cuando la ruta no calza ningun prefijo de `REGENERADO` ni de `ARCHIVO`. Los tres son **salidas de su propio instrumento con su corte**, la misma especie que `docs/FRANJA_PARES.jsonl` y `docs/INTRA_DOMINIO_PARES.jsonl`, que **si estan en la lista de `ARCHIVO` solo porque su prefijo si figura**. **Y la comprobacion dirigida sobre la especie que si tumbo el Gate 0 en la vuelta 39 da CERO: los NUEVE `bridges_aprobados.json` nombran a los dos nodos 0 veces.** El Gate 0 de hoy lo confirma por su lado: *Ningun puente aprobado apunta a un nodo deprecado (valor: 0 rotos)*.

> **DOS DETALLES DE ETIQUETA DEL INSTRUMENTO, declarados porque no se arreglan aqui:** su encabezado imprime *LOS TRES NODOS BUSCADOS* y *(vuelta 40)* aunque hoy se le pasaron **dos** ids y corre en la **42**. Es texto fijo del hermano de `OP-D-05`, **no toca ni una cifra**, y cambiarlo dentro de un acto seria tocar un instrumento sellado sin motivo escrito.

### EL INSTRUMENTO DE COSTURAS SOBRE EL RESULTANTE: **CITA, Y LA FUSION NO ENCENDIO LA SENAL**

`scripts/costuras_internas.py` corrido DESPUES de fundir (`docs/loop/SALIDA_V42_COSTURAS_TRAS_FUSION.txt`, **exit 0**): la cola pasa de **1.496** a **1.495** nodos (el absorbido sale al deprecarse) sobre **3.531** activos, el **42,3 por ciento**.

**EL RESULTANTE ESTA CITADO**, y se lee con el texto delante como la practica adjudicada en el acta 40 manda: **pareja 56,6** (pasos **4 y 5**, bajo el umbral de **80**: no dispara), **bloque 50,6** con corte tras **3** (sobre el umbral de **44**: dispara).

`scripts/loop/vuelta42_senal_antes_despues.py --nodo producto_unico_superior --commit b563e7a5`, sellado en `docs/loop/SALIDA_V42_ACTO285_SENAL.txt`:

| | bloque | contra el umbral 44 |
|---|---|---|
| **antes**, leido de git `b563e7a5` | **45,4** (corte tras 3) | **SOBRE** por **mas 1,4**, o sea **YA ESTABA DENTRO de la cola** |
| **despues**, del fichero de hoy | **50,6** (corte tras 3) | **SOBRE** por **mas 6,6** |

**LA FUSION NO ENCENDIO LA SENAL: el nodo ya estaba dentro antes de fundirse y sigue dentro. La cita no es nueva.** El movimiento de **mas 5,2 puntos** es el mismo patron mecanico que la vuelta 40 midio en tres casos: fundir mete mas vocabulario en menos pasos y la senal mide solape de tokens.

**Y LA LECTURA TEXTUAL, que es la que decide: NO HAY COSTURA.** La pareja citada son los pasos **4** (*compara contra la competencia, desarma sus productos, imagina como evolucionara el suyo*) y **5** (*traduce todo lo que encuentres en una definicion de tu producto*). **El paso 5 empieza literalmente con "Traduce todo lo que encuentres": CONTINUA al 4 en vez de volver a contarlo.** Lo mismo con el bloque: los pasos 1 a 3 investigan y definen, los 4 a 6 comparan, traducen y prueban. **Comparten vocabulario, no narracion.** La cita **queda registrada en la cola** y el auditor la relee, que es la guarda contra el juez y parte.

### LA RELECTURA DEL PAR 835, HECHA Y VOLCADA: **DE `B` A `D`**

`scripts/loop/vuelta32_relectura_opd01.py 835`, con la razon vieja impresa ENTERA y las aristas buscadas en los dos sentidos (`docs/loop/SALIDA_V42_ACTO285_RELECTURA_835.txt`). Volcada con `scripts/corregir_veredicto.py` (`docs/loop/SALIDA_V42_ACTO285_VEREDICTO_835.txt`): **puesto 835, B a D, 3.388 veredictos sin altas ni bajas.**

**LA `B` ERA CONDICIONAL Y LA PROPIA RAZON VIEJA LO DECIA:** *decidir este par sin saber que queda del nodo tras la cirugia es decidir sobre un texto que va a cambiar, aunque el solape no toque la juntura*. **Hoy ya se sabe.** Los **dos** cruces que aquella razon nombro siguen siendo **exactamente dos y ninguno mas**, y lo que la fusion anadio (VoC, el desarmado, la evolucion futura, los protocepts) **no toca a `brief_competitivo`**. **La fusion los SEPARA en vez de acercarlos**: el resultante es hoy la doctrina entera del producto superior y `brief_competitivo` sigue siendo UN documento de analisis. Libros distintos, entregables distintos, **cero arista medida hoy en los dos sentidos**.

> **LO QUE NO SE HACE, y va dicho:** `08_VERIFICACION` anade *si hay jerarquia se enlaza*. **La jerarquia candidata se nombra** (`brief_competitivo` es plausiblemente el documento donde se escribe la comparacion que el paso 4 del resultante manda hacer), **pero ninguno de los dos textos nombra al otro**, asi que declararla seria leerla y no medirla. **La arista NO se escribe en esta vuelta**: queda **declarada como candidata de `9.6`** y **marcada como discutible**, porque escribir una arista fuera del plan sellado del acto moveria la cifra publicada de enlaces sin plan detras.

**EL MARCADOR SE MUEVE, Y SE PUBLICAN LAS DOS CIFRAS** (regla 1: el estado al cierre se mide al cierre, y la apertura no se retoca):

| | n | A | B | C | D | tasa de A |
|---|---:|---:|---:|---:|---:|---:|
| **apertura de la vuelta 42** (`SALIDA_V42_APERTURA.txt`) | 3.388 | 575 | **83** | 8 | **2.722** | 17,0 |
| **tras la relectura del 835**, recomputado por el instrumento | 3.388 | 575 | **82** | 8 | **2.723** | 17,0 |
