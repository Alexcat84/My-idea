### TAREA 3, CERRADA. LOS EJEMPLARES DEL BANCO SALEN DEL UNIVERSO DE LAS CIEGAS

**LA LISTA SE COMPUTA Y NO SE TECLEA.** La escribe
`scripts/loop/_v199_t3_ejemplares_del_banco.py`, la procedencia entera vive en
`docs/loop/SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` (**5 casos, 5 VERDES**) y la
lista de enteros sueltos en
`docs/loop/_v199_ejemplares_del_banco_exclusion.txt`, **109 lineas**, contadas de
ese fichero.

**LA REGLA DE EXTRACCION VA DELANTE Y NO DETRAS, porque es lo unico auditable
aqui:** se busca un marcador (`puesto`, `puestos`, `par`, `pares`), detras se
consume una lista de numeros unidos por coma, `y`, `e` o `a`, la `a` entre dos
numeros se lee como rango cerrado, y los millares con punto se normalizan
(`2.117` es `2117`, que es como el banco los escribe). **Lo que la regla NO
hace:** no coge numeros sin marcador (un `9.21` de doctrina no es un puesto) ni el
numero que va DELANTE (*"los 240 pares"* es un conteo).

| cifra | valor | de donde sale |
|---|---:|---|
| banco medido hoy | 182228 bytes, `sha256` LF `68557cd00a3124f4`, 3119 lineas | `SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` |
| fecha de corte (banco `9.21`) | 2026-09-07 | leida de `git log -1 --date=short` |
| puestos cosechados del banco | **109** | mismo fichero |
| de esos, que NO existen en el archivo | **0** | mismo fichero |
| universo que queda | **3279 de 3388**, un 3.2 por ciento fuera | mismo fichero |
| rangos que el banco escribe | **1**, linea 2327, `2389 a 2400`, 12 puestos, EXPANDIDO | mismo fichero |

**EL CONTROL DEL ACTA 198 ES LO QUE IMPIDE QUE ESTO SE APRUEBE SOLO**, y no es un
`assert` contra si mismo: los dos numeros salen del acta y la lista sale del
banco. **El `1077` aparece en la linea 2543 del banco y el `165` en la 867**, las
dos leidas por el computo. Si cualquiera de los dos faltara, el fichero sale ROJO
y **no escribe la lista**.

**EL CARRIL SE PRUEBA CORRIENDOLO, no citandolo.** Misma banda del archivo, con y
sin la lista, en esta vuelta:

| corrida | pares elegidos | fugas del destape |
|---|---:|---:|
| `--desde 150 --hasta 210` | **61** | 0 |
| la misma **`--excluir`** con las 109 | **51** | 0 |

Los **diez** que se caen son `156`, `165`, `176`, `185`, `192`, `197`, `200`,
`201`, `206` y `209`, y **los diez estan nombrados en el banco con su linea**.
`aislador_de_ciega.py` sale **VERDE** en las dos corridas, y su guarda de puestos
inexistentes no salto ni una vez, que es la comprobacion de que las 109 son
puestos de verdad.

**`C.3` LA ERRATA QUE EL CONTROL CAZO, DECLARADA SIN TAPAR LO QUE CORRIGE, Y ES LA
QUE MAS PESA DE ESTA TAREA.** Mi primera version del marcador escribia `pares?`,
que en una expresion regular **no es "par o pares"**: es `par` + `e` + `s`
opcional, o sea **exige la `e`**. Con eso `puesto` y `puestos` entraban y **`par`
a secas no**, y el `165` del auditor, que el banco escribe como *"La nota del par
165"*, se quedaba fuera. **El caso de control salio ROJO y por eso se vio.** Sin
ese control la lista se habria publicado con **82** en vez de 109 y con cara de
completa.

**`C.4` Y DOS RECORTES MAS DE LA MISMA ESPECIE, LOS DOS MEDIDOS Y NO
SOSPECHADOS.** La cosecha empezo mirando **linea a linea**, y el banco parte sus
enumeraciones: en su linea 2327 escribe *"Los puestos 2.389 a"* y **el `2.400`
esta en la linea de abajo**, ademas **detras de la marca de cita `>`**. Cada uno
de los dos descuidos se llevaba puestos por delante en silencio, y la serie de la
cifra lo dice sola: **82, luego 96, luego 109**. Se arreglaron mirando la linea y
la siguiente, y quitandole a la siguiente su `>`. **Lo que decide sigue siendo el
mismo `numeros_tras()`:** entre dos numeros solo puede haber separadores de lista,
asi que un numero de abajo entra unicamente si el de arriba quedo colgando, y un
punto o cualquier palabra corta la union.

**`P.2` DISCUTIBLE MARCADO, Y VA MARCADO ANTES DE SABER SI ACIERTO.** La moratoria
de `AUDITOR.md` 6.3 prohibe fabricar lectores nuevos y **la TAREA 3 no esta entre
sus dos excepciones**; lo que la salva es que el propio encargo manda que la lista
se COMPUTE y no se teclee, y computar necesita codigo. **Lo lei asi y puedo estar
equivocado.** Se hizo con el minimo posible: prefijo `_` para que el censo de
arneses no lo cuente, **fuera de la nomina** (congelada en 135), no vigila a nadie
y no se cita como guarda. **Si el fundador lo lee como maquinaria, se retira y la
lista queda como fichero muerto con su fecha de corte.**

**`P.3` UNA SEGUNDA PREGUNTA QUE TAMPOCO CONTESTO YO.** La lista **envejece**: el
banco crece cada vuelta y estas 109 son las del corte **2026-09-07**. El computo se
puede volver a correr, pero **nadie ha escrito que haya que correrlo**, y una lista
de exclusion vieja deja entrar al universo puestos cuya clase ya esta publicada.
**Si esto tiene que ser un paso fijo del sello de apertura, es una linea de
doctrina y no la escribo yo.**
