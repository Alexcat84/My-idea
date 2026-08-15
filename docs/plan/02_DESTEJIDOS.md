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

| puesto | contra quien | lo que el otro trae y el emblema sigue sin decir, medido contra sus SEIS pasos de hoy | clase que sostengo |
|---:|---|---|---|
| **592** | `mvp_catalogo_tecnicas` | **la ESCALERA DE COSTO**: empezar por el MVP mas barato (hoja de datos, folleto, storyboard), subir en sofisticacion solo si lo primero promete, y usar herramientas a mano antes de pagar produccion profesional. **Ninguno de los seis pasos del emblema nombra el coste, el tipo de prototipo ni la herramienta.** Comparten el arranque (identificar la hipotesis critica) | **`D`, sano, con ARISTA QUE FALTA** hacia `mvp_catalogo_tecnicas` |
| **830** | `prueba_mvp_alta_fidelidad` | **el AISLAMIENTO DE LA PRUEBA**: numero limitado de clientes invitados, llamada a la accion clara, cuantas visitas antes del primer uso, cuantos lo recomiendan y que tan rapido, y evitar publicidad, prensa o demostraciones publicas. **Ninguno de los seis pasos lo dice.** El solape (mostrar solo a los earlyvangelists) **era una de las ordenes que el emblema repetia CUATRO veces y ahora vive en UNA** | **`D`, sano, con ARISTA QUE FALTA** hacia `prueba_mvp_alta_fidelidad` |

> **LA CLASE SE SOSTIENE CON LA PRACTICA MEDIDA DEL ARCHIVO, no con mi gusto:** barrido hoy
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` entero, **los 207 veredictos cuya razon nombra ARISTA QUE
> FALTA son `D`, los 207**. Y **medido hoy en los dos sentidos, ninguno de los dos pares tiene
> arista**, que es lo que la razon del 592 ya decia (*sin arista*) y lo que el 830 no habia
> mirado.

#### LO QUE ESTA VUELTA **NO** ESCRIBE, y por que

> **LAS TRES CLASES NUEVAS NO SE ESCRIBEN EN `INTRA_DOMINIO_VEREDICTOS.jsonl` EN ESTA VUELTA, y
> no es timidez: es la letra de la propia operacion.** El campo `preservar` de `OP-D-01`, en su
> correccion declarada del 15 ago 2026, dice: *si la relectura diera par nuevo, **entra por el
> recomputo (banco 9.10)**, no se decide aqui de antemano*. **Volcarlas movería el marcador
> publicado** (`A 583, B 89, C 7, D 2709` medido hoy al abrir esta vuelta) **y obligaria a
> barrer en el mismo acto todas las tablas derivadas que citan esos tres numeros**, que es
> exactamente lo que el 9.10 exige y lo que ninguna operacion de la fase 02 tiene escrito.
> **Las tres lecturas quedan publicadas aqui con su evidencia, y la escritura va al recomputo.**

> **LAS TRES ARISTAS TAMPOCO SE PONEN**, por el mismo motivo de letra: el campo `aristas_nuevas`
> de `OP-D-01` esta **VACIO**, y los enlaces son la **fase 04** del indice, que va despues de
> los destejidos y de las fusiones. **Quedan declaradas aqui, con su sentido y su motivo, para
> que la fase 04 las encuentre escritas y no las tenga que redescubrir.**

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

### `OP-D-02`, ESTADO AL 15 ago 2026 (vuelta 32): **PASO 1 CONSUMIDO, FUSION EN PARADA**

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
**medido hoy, DOS de los tres pares A no nombran ganador en su razon** (386 y 788). **Ningun
nodo del acto tiene una victoria citable**, asi que no hay ganador por derecho; y la otra
especie, **por elegir, exige `P.8` sobre la nomina entera CON EL ACTO COMPLETO delante**, que es
justamente lo que el motivo 1 dice que no hay.

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
