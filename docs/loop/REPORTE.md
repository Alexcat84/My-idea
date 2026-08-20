# REPORTE DE LA VUELTA 58 (20 ago 2026, ejecutor Opus 5)

**LA TAREA 1 ENTERA, EN SUS CUATRO PARTES. LA TAREA 2 A MEDIAS Y SE DICE CUAL MITAD: el tramo 5
queda ABIERTO con todo su insumo medido y LOS LOTES NO SE EJECUTAN.** **LA RELECTURA CONJUNTA DEL
ACTO 32 SE RESUELVE A FAVOR DEL CASO DEL AUDITOR**: medido contra el grafo pre fusion, el acto es
`EMPATE SIN VARA` y queda **DECLARADO, septimo del tramo 4**. **EL ATRASO DE LAS ONCE CITAS
HEREDADAS QUEDA EN CERO**, ocho corregidas y tres rotuladas, con el volteo de cada puesto **medido
por `git`** y no supuesto. **Y EL HALLAZGO DE LA VUELTA SALE, otra vez, DE CORRER UNA GUARDA EN VEZ
DE LEERLA: el abridor del tramo 5 llevaba `(vuelta 57)` tallado a mano en su titulo**, que es
exactamente la especie que la TAREA 1.3 mandaba reparar en otro instrumento. **La cace corriendola,
no leyendola.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `06b89c74` (el commit del reporte de la vuelta 57), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** |
| **hash final** | `3ffc2091` (el cierre) mas este mismo commit, que solo escribe esta cabecera, **pusheados a `origin/pasada-unica`** |
| **commits de la vuelta** | **7 hasta el cierre**, leidos de `git log --oneline` al escribir esto: `b222e1c5` (apertura medida), `2ef9adda` (TAREA 1.1, el acto 32 deshecho), `38a0f341` (TAREA 1.2, las once heredadas), `e00475db` (TAREAS 1.3 y 1.4), `5efa8382` (tramo 5 abierto), `908bc4c9` (dossier del tramo 5), `3ffc2091` (el cierre), **mas este**, que solo escribe esta cabecera porque el commit del cierre no podia contener su propio hash |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1)

**NINGUNA CELDA ESTA TECLEADA:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 58`
([`SALIDA_V58_TALLAR_CABECERA.txt`](SALIDA_V58_TALLAR_CABECERA.txt)). **Las dos columnas se leen de
ficheros DISTINTOS.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.341 / 512 / 17.369 | **3.853 / 3.342 / 511 / 17.366** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 208 / 343 | **551 / 207 / 344** |
| actos (componentes) | 149 | **150** |
| actos `CERRADOS` / `ABIERTOS` | 96 / 53 | **97 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 201 / 240 | **203 / 240** |
| cola de costuras | 1.471 | **1.471** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 186 | **185** |
| duplicadas historicas: grupos / nodos | 955 / 753 | **956 / 754** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (441 igual a 441; 343 igual a 343) | **TODAS OK (443 igual a 443; 344 igual a 344)** |

**Y ANTES DEL COMMIT SE CORRIO EL COMPARADOR:**
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 58 --comparar docs/loop/REPORTE.md`
([`SALIDA_V58_TALLAR_CABECERA_COMPARAR.txt`](SALIDA_V58_TALLAR_CABECERA_COMPARAR.txt)).

**LA APERTURA CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 57 MIDIO POR CORRIDA PROPIA**, y eso es
contraste, no fuente. **Instrumentos de apertura, corridos ANTES de la primera operacion y con el
arbol limpio:** [`SALIDA_V58_APERTURA.txt`](SALIDA_V58_APERTURA.txt),
[`SALIDA_V58_MARCADOR_APERTURA.txt`](SALIDA_V58_MARCADOR_APERTURA.txt),
[`SALIDA_V58_RECOMPUTO_APERTURA.txt`](SALIDA_V58_RECOMPUTO_APERTURA.txt),
[`SALIDA_V58_COLA_APERTURA.txt`](SALIDA_V58_COLA_APERTURA.txt),
[`SALIDA_V58_COLISIONES_APERTURA.txt`](SALIDA_V58_COLISIONES_APERTURA.txt) y
[`SALIDA_V58_DUPLICADAS_APERTURA.txt`](SALIDA_V58_DUPLICADAS_APERTURA.txt). **Las tres que
reescriben sus ficheros salieron IDEMPOTENTES, verificado por `git status`.** **El cierre esta en
los ficheros `_CIERRE` hermanos, corridos DESPUES del ultimo movimiento.**

**CADA CELDA QUE SE MOVIO LO HIZO EN UNO, Y ERA LO QUE EL ENCARGO PREDECIA** para el deshacer del
acto 32: colapsos bajan uno, pares distintos suben uno, actos suben uno, `CERRADOS` suben uno,
nodos en `CERRADOS` suben dos, auto-pares bajan uno, vivos suben uno y deprecados bajan uno.

**LAS DOS CELDAS QUE NO SE MUEVEN EN UNO, MEDIDAS Y NO SUPUESTAS:**

1. **LOS ENLACES BAJAN TRES.** El conteo del instrumento incluye a los deprecados; la fusion habia
   sumado **tres** `nodos_previos` al superviviente (los tres vecinos redirigidos), y esos tres son
   los que se van al deshacer.
2. **LAS DUPLICADAS HISTORICAS SUBEN UNA (955 a 956 grupos, 753 a 754 nodos), Y EL GRUPO TIENE
   NOMBRE:** es `programa_de_referidos_de_franquiciados` sobre `nodos_previos` hacia
   `principio_apalancamiento_numero_magico`, **una duplicada que ya existia antes de la fusion y
   que vuelve con el nodo que revive**. Medido en el diff de `docs/plan/ARISTAS_DUPLICADAS.jsonl`.
   **La cola no se mueve en su cuenta (1.471) pero SU FICHERO SI CAMBIA UNA LINEA**, y es el mismo
   nodo: `referidos_franquiciados_existentes` pasa de **6 pasos a 5**, que es el paso que devuelve.

**EL MARCADOR NO SE MUEVE Y NO ES UN OLVIDO:** el diff de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
entre la apertura (`b222e1c5`) y `HEAD` es **VACIO**, corrido y no supuesto. **Deshacer una fusion
pura no voltea ningun veredicto.**

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V58_MARCADOR_CIERRE.txt`](SALIDA_V58_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) |
franquicias 10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0
(n 106) | seguridad_digital 11,1 (n 27). **Identica a la de la apertura al digito.**

---

## 1. TAREA 1.1: **LA RELECTURA CONJUNTA DEL ACTO 32, RESUELTA A FAVOR DEL AUDITOR**

**SE VERIFICO CONTRA EL GRAFO ANTES DE TOCAR NADA**, que es lo que el encargo pedia. Nace
`scripts/loop/vuelta58_relectura_acto32.py`, **de solo lectura**, con la aritmetica de varas
copiada entera del cuadro de varas y **medida sobre el arbol PRE FUSION** (worktree en `75863aee`)
([`SALIDA_V58_RELECTURA_ACTO32_PREFUSION.txt`](SALIDA_V58_RELECTURA_ACTO32_PREFUSION.txt)).

| | `programa_de_referidos_de_franquiciados` | `referidos_franquiciados_existentes` |
|---|---:|---:|
| pasos | 5 | 5 |
| condiciones | 2 | 2 |
| cableado (vecinos resueltos distintos) | 3 | 3 |
| **forma que la receta le da** | | **`EMPATE SIN VARA`** |

**LA LETRA VIGENTE, LEIDA HOY Y CON SU LINEA AL LADO (regla 1):**

| la vara | donde | lo que dice |
|---|---|---|
| acta 53, pregunta 4 | `ACTA_AUDITOR.md` linea **13015** | *reserva el empate sin vara para cuando TODO empata* |
| acta 54, pregunta 4 | linea **13389** | *el conteo de caracteres no desempata* |
| acta 54, pregunta 4 | linea **13391** | *el propio declarado de UN SOLO LADO es una vara no empatada* |

**AQUI EL PROPIO DECLARADO ESTA A LOS DOS LADOS.** La razon del puesto **2127**, leida hoy entera,
mide **UNA LINEA** propia de uno y **DOS LINEAS** propias del otro. **Contar esas lineas es un
conteo sobre la letra y ninguna acta lo adjudica como vara.** Y la razon **no declara superviviente,
ni contencion, ni padre**: pesa una pieza como *la que mas cuesta reponer*, que no es ninguna de las
tres formas que el acta 53 pregunta 3 enumera. **Ademas ese carril ni siquiera aplica**, porque
habla de conteos que CHOCAN y aqui los tres EMPATAN.

> **EL CONTRASTE INTERNO, MEDIDO EN LA MISMA SALIDA Y NO CITADO DE MEMORIA:** el **acto 11** da
> **4 contra 4, 2 contra 2 y 2 contra 2**, tambien `EMPATE SIN VARA`, y su razon (puesto **1884**)
> declara propio **UNA linea contra TRES**. **La vuelta 57 lo DECLARO.** Dos actos con la misma
> forma y el mismo tipo de desempate no pueden acabar uno fundido y otro declarado.

**NINGUNA EVIDENCIA NUEVA CONTRA EL CASO**, asi que no hubo que parar antes de tocar el grafo.

### EL DESHACER, Y LO QUE OBLIGO A HACERLO DISTINTO DEL ACTO 23 DE LA VUELTA 55

**`scripts/loop/vuelta58_deshacer_acto32.py`, sucesor declarado del de la vuelta 55** con su maquina
copiada (alcance re-medido y no copiado, guardas antes de escribir, modos simular y ejecutar)
([`SALIDA_V58_DESHACER_ACTO32.txt`](SALIDA_V58_DESHACER_ACTO32.txt)).

**EL DESHACER NO PUDO SER UN RESTAURAR EL BLOB, Y EL MOTIVO ESTA MEDIDO:** de los **CINCO** ficheros
que el acto 32 toco en el lote B (`a1d7269d`), **CUATRO** no se habian vuelto a tocar y se restauran
al blob del lote A (`0481113f`); **el quinto, `principio_apalancamiento_numero_magico.json`, SI se
toco despues**, en el lote C (`706397c7`) y **por OTRO acto, el 35**, que le cambio
`marketing_en_ferias_comerciales_de_franquicias` por `ferias_comerciales_franquicia`.
**Restaurarle el blob habria BORRADO EL ACTO 35.** Ese fichero recibe el **DIFF INVERSO** del acto
32 (`git apply -R`), probado con `--check` antes de aplicarse. **El acto 35 queda en pie, verificado
por conteo.**

| la guarda | como salio |
|---|---|
| alcance re-medido de `git` contra el declarado | **CALZA** |
| clasificacion restaurable contra parcheable, **medida** | **CALZA** (4 y 1) |
| los cinco limpios en el arbol antes de escribir | **SI** |
| parche inverso probado con `--check` | **APLICA LIMPIO** |
| los dos miembros VIVOS y sin alias cruzado | **SI** |
| **campo a campo contra el blob pre fusion** | **IDENTICOS LOS DOS** |
| el cableado de vuelta al absorbido en los tres vecinos | **SI** (1 y 0 en cada uno) |

**RECOMPUTO TRAS EL DESHACER:** `reanclar_por_resolutor.py` **EN BLANCO**, Gate 0 **OK**, motor
**25 de 25**, web **80 ficheros con 1.030 pasadas y 3 saltadas**, `tsc` **CERO lineas**, censo con
`--esperadas 0` y **`CALZA: SI`**.

---

## 2. TAREA 1.2: **LAS ONCE HEREDADAS, CON TRIAGE MEDIDO POR `git`**

**EL TRIAGE NO SE ADIVINO.** Nace `scripts/loop/vuelta58_triage_heredadas.py`, de solo lectura, que
recorre las **194** versiones de `INTRA_DOMINIO_VEREDICTOS.jsonl` y encuentra **el commit exacto en
el que cada puesto cambio de clase**, y busca un **CORTE DECLARADO** en las veinte lineas de arriba
de cada cita ([`SALIDA_V58_TRIAGE_HEREDADAS.txt`](SALIDA_V58_TRIAGE_HEREDADAS.txt)).

**LA VARA CON LA QUE SE REPARTEN LAS ONCE, dicha con todas sus letras para que se pueda discutir:**
**se CORRIGE** cuando la letra es una afirmacion sobre el par que hoy es falsa **y cuya correccion
no rompe la frase de alrededor**; **se ROTULA** cuando reescribir la letra **HARIA MENTIR A LA
PAGINA**.

| cita | puesto | volteo medido | via |
|---|---:|---|---|
| `INTRA_DOMINIO_INFORME.md`:264, 265, 266 | 393, 395, 396 | `A` a `D` el 10 y el 11 ago 2026, `3e2e2d32` y `3896c57c` | **CORREGIDA** |
| `INTRA_DOMINIO_INFORME.md`:6597 | 658, 678 | `A` a `D` el 10 ago 2026, `59414fc7` | **CORREGIDA** |
| `INTRA_DOMINIO_INFORME.md`:9989 | 1222 | `A` a `D` el 20 ago 2026, `90bb930c` | **CORREGIDA** |
| `INTRA_DOMINIO_INFORME.md`:11743 | 1865 | `A` a `D` el 20 ago 2026, `cadc9977` | **CORREGIDA** |
| `BANCO_DE_TEXTOS.md`:2914 | 2477 y 2488 | el 2.488 `A` a `D` el 20 ago 2026, `04bd56de` | **CORREGIDA, partiendo la fila** |
| `02_DESTEJIDOS.md`:2569 | 599 | `B` a `D` el 19 ago 2026, `76c9fadc` | **ROTULADA** |
| `02_DESTEJIDOS.md`:3248 | 233 | `B` a `D` el 19 ago 2026, `15d42eef` | **ROTULADA** |
| `02_DESTEJIDOS.md`:3606 | 784 | `B` a `D` el 19 ago 2026, `c8172126` | **ROTULADA** |

**LAS TRES ROTULADAS LO SON POR EL MISMO MOTIVO MEDIDO, y no por conveniencia:** la clase que citan
es **la de ANTES de una relectura que la propia pagina anuncia** (*se relee al cierre del acto*) **y
que el commit de esa misma operacion ejecuto**: los tres commits se titulan *LA RELECTURA DEL 599 de
B a D*, *del 233* y *del 784*. **Escribir `D` dejaria la frase diciendo que un par ya releido se
relee, que es al reves de lo que paso.** El **784** ademas vive **dentro de un bloque de codigo que
es una salida de instrumento pegada verbatim**, con su propio corte medido dentro, que es el caso
del `D6` de la vuelta 57.

**LA FILA DEL BANCO SE PARTE EN DOS Y NO SE CORRIGE EN SU SITIO**, con el motivo medido: **publicaba
UNA letra para DOS puestos que hoy ya no la comparten** (el 2.477 sigue en `A`, el 2.488 esta en
`D`). Dos letras en una celda es lo que el barrido llama **AMBIGUO** y lo que no se puede cotejar
por maquina. **La fila vieja queda entera y TACHADA.**

### EL ROTULO NO ES UNA EXCUSA: **SE VERIFICA SOLO**

**Sucesor declarado `scripts/loop/vuelta58_puestos_volteados.py`, copiado BYTE A BYTE del de la
vuelta 57** (comprobado antes de tocarlo). La via es la del acta 54 pregunta 3 (linea **13381**):
sus cifras ya las cita el acta 57 del auditor, asi que **la logica no se toca y se escribe sucesor**.
**Lo unico anadido es el DETECTOR DE ROTULOS**, y **un rotulo cae en ROJO, y el barrido entero con
el, si su `vigente=` no calza con el archivo de hoy, si no cubre ninguna cita, o si su `cita=` no
calza.** Las lineas de rotulo **se blanquean antes de los dos detectores** para que el rotulo no se
juzgue a si mismo, que es la trampa que el `D2` de la vuelta 57 nombra.

| | ANTES | DESPUES | el ANCESTRO sobre lo ya reparado |
|---|---:|---:|---:|
| citas VERDES | 191 | **199** | 199 |
| citas AMBIGUAS | 16 | **16, LAS MISMAS** | 16 |
| citas envejecidas | 11 | **3, todas ROTULADAS** | 3 |
| **deuda** | **11** | **CERO, VERDE** | 3 (no sabe de rotulos) |

**QUE EL ANCESTRO DE LAS MISMAS CIFRAS SALVO LA CLASIFICACION DEL ROTULO ES LA PRUEBA DE QUE LA
ARITMETICA SE COPIO ENTERA**, y por eso se corre y se cita
([`SALIDA_V58_PUESTOS_VOLTEADOS_ANCESTRO.txt`](SALIDA_V58_PUESTOS_VOLTEADOS_ANCESTRO.txt)).
El escritor `vuelta58_correcciones_heredadas.py` va con **ANCLA LITERAL UNICA** y **final de linea
POR FICHERO** (medido: `docs/` en LF, `02_DESTEJIDOS.md` en CRLF). **IDEMPOTENTE:** los 15 sitios en
`YA ESTABA`.

---

## 3. TAREA 1.3: **EL TITULO DEJA DE SER UNA CONSTANTE**

**Sucesor declarado `scripts/loop/vuelta58_varas_tramo.py`, NOMBRE ESTABLE Y SIN NUMERO DE TRAMO**,
copiado **byte a byte** de `vuelta56_varas_tramo3.py`. **LO UNICO QUE CAMBIA ES EL TITULO:** el
numero de tramo sale de **la clave del ordinal que el propio fichero trae** (`orden_tramo4` dice
tramo 4) y la vuelta sale del argumento; ademas el cuadro **imprime la ruta del fichero del tramo**,
para que la salida diga sola sobre que se corrio.

**LA PRUEBA DE QUE LA ARITMETICA NO SE TOCO ES UN DIFF, no una afirmacion:** corrido sobre el arbol
**PRE FUSION** con el fichero del tramo 4, la salida sale **IDENTICA A LA DE LA VUELTA 57 EN LAS 63
LINEAS SALVO UNA**, y esa una es el titulo
([`SALIDA_V58_VARAS_TRAMO4_RECORRIDO.txt`](SALIDA_V58_VARAS_TRAMO4_RECORRIDO.txt)):

| | |
|---|---|
| **decia** | `EL CUADRO DE VARAS DE LOS 50 ACTOS DEL TRAMO 3 (vuelta 54)` |
| **dice** | `EL CUADRO DE VARAS DE LOS 50 ACTOS DEL TRAMO 4 (vuelta 57)` |
| **las 50 filas de varas y el resumen POR FORMA** | **no se mueven ni un caracter** |

---

## 4. TAREA 1.4 Y LA SEGUNDA MITAD DE LA 1.1: **EL REGISTRO DEL TRAMO 4**

**Sucesor tallador `scripts/loop/vuelta58_tallar_planes.py`**, tambien copiado byte a byte, con un
solo anadido: **`--retirado`**, que saca del talle un acto **SELLADO que se retiro despues** y lo
pasa a la tabla de declarados con su especie y su carril. **EL PLAN SELLADO NO SE TOCA:** los
`PLAN_V57_*.json` se quedan con el acto 32 dentro y su motivo entero, **porque reescribir un plan
sellado taparia lo que se corrige**. **Corrido SIN `--retirado` imprime lo mismo que su ancestro en
las 91 lineas salvo el titulo y el contador de retirados**, comprobado por diff.

| | vuelta 57 | **con el 32 retirado** |
|---|---:|---:|
| actos fundidos | 44 | **43** |
| piezas repartidas | 245 | **238** |
| actos declarados | 6 | **7** |
| la forma `LOS TRES CONTEOS EMPATAN y decide la pieza declarada POR CANTIDAD` | 1 (el acto 32) | **desaparece del tramo** |

**Nace una TABLA 5 que deja escrito que el motivo sellado sigue ahi con su forma vieja**, para que
la correccion no borre lo que corrige.

**El escritor `vuelta58_registro_acto32.py` NO TECLEA NINGUNA CELDA:** las **16** cifras salen por
expresion regular de las salidas del dia y **las cuatro tablas se RECORTAN POR MAQUINA** de la
salida del tallador. Las cuatro celdas del estado que se movieron quedan **con TACHADO y su cifra
nueva al lado**; las cuatro tablas del dia del sellado se quedan **enteras con un aviso `TABLA
SUPERADA` delante**; y el bloque nuevo va al final con las tablas vigentes pegadas enteras.

**LA ADJUDICACION DEL ACTA 57 SOBRE EL ACTO 25, anotada con fecha:** **declararlo fue correcto y el
carril ya estaba escrito**, el **IMPOSIBLE POR PUERTA** del acta 51 pregunta 3, citado por el acta
54 pregunta 1 y listado por el acta 54 pregunta 2 en el carril de declarar y acumular. **No se
escribio doctrina nueva.** **La SALIDA DE FONDO queda reservada a la mesa en el pendiente 5**, y el
acto 25 no vuelve a la cola mientras tanto.

---

## 5. TAREA 2: **EL TRAMO 5 ABIERTO, Y EL PREFIJO MIDE 26**

**Sucesor declarado `scripts/loop/vuelta58_tramo5_nomina.py`**, copiado byte a byte del abridor del
tramo 4 ([`SALIDA_V58_TRAMO5_NOMINA.txt`](SALIDA_V58_TRAMO5_NOMINA.txt)). **LO UNICO QUE NO ES
COPIA, y es poco a proposito:** el tramo 4 entra en la lista de tramos previos con su fichero
fijado, el ordinal pasa a `orden_tramo5`, y los rotulos que nombraban tres tramos nombran cuatro.

| | |
|---|---|
| **guarda del prefijo** | **26**, MEDIDO: 11 del tramo 1, 5 del 2, 3 del 3 y **SIETE del 4**, que son los seis declarados **mas el acto 32 que esta vuelta deshizo**. Ocupan los puestos **1 a 26 sin huecos** |
| **las dos lecturas** | **CALZAN**, mismo conjunto y mismo orden, **cero divergencias que diagnosticar** |
| **el tramo** | los puestos **27 a 76** de hoy, que son los **200 a 249** de la nomina de la 48 |
| **el tramo 2 contra su bloque 51 a 100** | **CALZA** |
| **el tramo 3 contra su bloque** | sigue **sin calzar**, tal como la vuelta 56 lo dejo escrito |
| **figura** | **FUSION PURA, tamano 2 y PURO A, 50 de 50**, cero que no lo sean |
| **los cuatro ajenos** | **VERDE POR LOS DOS CAMINOS**, el literal y el del resolutor |
| **solape con tramos anteriores** | **CERO** |
| **colisiones esperadas del tramo entero** | **100 combinaciones simuladas y CERO que fabriquen colision**, medidas ANTES de tocar un nodo |

**EL PREFIJO NO SE HEREDO, SE MIDIO, y por eso salio 26 y no 25**, que era la otra cifra que el
encargo contemplaba. **El instrumento no lleva ese numero escrito en ninguna parte.**

**CUADRO DE VARAS DEL TRAMO 5**, con el sucesor de la TAREA 1.3 y el titulo saliendo correcto solo
([`SALIDA_V58_VARAS_TRAMO5.txt`](SALIDA_V58_VARAS_TRAMO5.txt)): **22** de `UNA SOLA VARA`, **11** de
`TODAS DE ACUERDO`, **7** de `CONTENIDO EMPATA`, **6** que `CHOCAN` y **4** de `EMPATE SIN VARA`.

**DOSSIER DEL TRAMO 5** ([`SALIDA_V58_DOSSIER_TRAMO5.txt`](SALIDA_V58_DOSSIER_TRAMO5.txt)):
**1.979 lineas**, los 50 actos con su razon **entera sin recortar**, los dos nodos con sus pasos,
condiciones, cableado y entregable, y la marca de **PUERTA** sobre el universo protegido de 256 ids.

**CASO POSITIVO de la vuelta 57 re-corrido al abrir**, como el acta 54 pregunta 7 manda: **LAS SEIS
GUARDAS MUERDEN** sobre el acto 37 del tramo 3, que sigue declarado y que esta vuelta no toca
([`SALIDA_V58_CASO_POSITIVO_V57.txt`](SALIDA_V58_CASO_POSITIVO_V57.txt)).

---

## 6. EL HALLAZGO DE LA VUELTA: **UN SEGUNDO TITULO TALLADO A MANO, CAZADO CORRIENDO**

**El abridor del tramo 5 llevaba `(vuelta 57)` TALLADO A MANO en el `print` del titulo**, heredado
de su ancestro. **Es exactamente la especie que la TAREA 1.3 mandaba reparar en el cuadro de varas**
y que la racha de la cabecera del reporte pago tres veces en las vueltas 54, 55 y 56. **La vuelta
pasa a salir de `--vuelta`, y sin el argumento el titulo NO la nombra en vez de heredar una vieja.**

**LO QUE CONVIENE DEJAR DICHO ES COMO SE CAZO:** no leyendo el fichero, sino **corriendolo y
mirando la salida**. La TAREA 1.3 se encargo sobre UN instrumento porque el auditor vio SU salida;
este segundo llevaba el mismo defecto y nadie lo habia visto porque nadie habia mirado su cabecera.
**Sugiere que la especie no esta agotada y que la busqueda deberia ser por barrido y no por
denuncia**, y va como pregunta al auditor (seccion 11, pregunta 3).

---

## 7. EL BARRIDO `9.10` DEL CIERRE

**Con las cifras viejas DE HOY** (`--viejo 551,72,5,2760 --retrato 208,343`,
[`SALIDA_V58_BARRIDO_910_CIERRE.txt`](SALIDA_V58_BARRIDO_910_CIERRE.txt)). **TRES celdas
corregidas** con `scripts/loop/vuelta58_correcciones_910.py`
([`SALIDA_V58_CORRECCIONES_910.txt`](SALIDA_V58_CORRECCIONES_910.txt), **idempotente**: las tres en
`YA ESTABA` al re-correrlo):

| la celda | decia | **medido al cierre** |
|---|---:|---:|
| `RECOMPUTO_3388.md` **247**, colapsos **y su contador** | 208, contador ONCE | **207, contador DOCE** |
| **248**, pares distintos **y su contador** | 343, contador CATORCE | **344, contador QUINCE** |
| **528**, el checkpoint `ii` en sus dos parentesis | 343 igual a 343 | **344 igual a 344, sigue OK** |

**EL MARCADOR NO SE MUEVE Y EL MOTIVO ESTA MEDIDO, NO SUPUESTO:** el diff del archivo de veredictos
contra la apertura es **VACIO**. **Las filas del marcador del informe y sus dos tablas por dominio
hermanas se cumplen POR VACIO y se dice.**

**Y LA CELDA QUE NO SE TOCA, otra vez con su motivo:** la seccion **PASO 3** publica su corte con
todas sus letras en su linea 379. **El acta 57 ya lo adjudico A FAVOR (`D6`)**, asi que esta vuelta
no lo vuelve a marcar como discutible: **esta cerrado por cita.**

**EL BARRIDO DE PUESTOS VOLTEADOS AL CIERRE: VERDE**, deuda **CERO**
([`SALIDA_V58_PUESTOS_VOLTEADOS_CIERRE.txt`](SALIDA_V58_PUESTOS_VOLTEADOS_CIERRE.txt)).

---

## 8. GATE 0, LAS SUITES Y LOS REGISTROS

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`** las **dos** veces (tras el deshacer y al cierre); `etiquetas_de_cara --aplicar`; `sync_assets_web` |
| **suite del motor** | **25 de 25**, las dos veces |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas, las dos veces |
| `tsc --noEmit` | **CERO** lineas |
| censo de colisiones | **CERO**, con `--esperadas 0` y **`CALZA: SI`** |
| `reanclar_por_resolutor.py` | corrido **ENTRE el deshacer y `run_phase1`**. **En blanco** |
| `verificar_mapas_destejido.py` | **OK**, 14 tablas y 83 filas, **cero discrepancias** (vara 1; la 2 **no se corrio**, no hay mapa de particion nuevo, y se dice) |
| **hook guardian** | verde en todos los commits |

**UNA TRAMPA DE ENTORNO, declarada porque costo una corrida:** la suite web con
`--reporter=basic` **muere con `ERR_LOAD_URL`** en esta version de vitest. Se corre **sin ese
argumento**. No es un fallo del catalogo y no se cuenta como tal.

---

## 9. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

1. **MI PROPIA GUARDA DE ANCLAS ME CAYO ENCIMA DOS VECES, Y LAS DOS SE DECLARAN.** La primera: las
   cabeceras de las cuatro tablas del registro **son identicas en los tramos 1, 2, 3 y 4**, el ancla
   aparecia **dos y tres veces**, y el instrumento **no escribio nada**. Se acoto la ventana al
   registro del tramo 4. La segunda: **el bloque nuevo PEGA LAS TABLAS ENTERAS**, cabecera incluida,
   asi que tras la primera escritura el ancla volvia a aparecer dos veces **dentro de la ventana** y
   la guarda **cayo sobre su propio trabajo**. Se cerro la ventana antes del bloque. **Las dos veces
   la guarda hizo lo que se le pide: no escribir a medias.**
2. **EL SEPARADOR DE `--retirado` NACIO MAL Y LO CACE ANTES DE USARLO:** era `N:especie:carril`, y
   las especies llevan dos puntos dentro (`EMPATE SIN VARA: NI EL CONTENIDO...`), asi que el corte
   partia la especie por la mitad. Se cambio a `N|especie|carril`. **Costo cero cifras.**
3. **CORRI `recomputo_3388.py` MAL LA PRIMERA VEZ:** le pase `--salida` apuntando al fichero de
   texto, y `--salida` es el **jsonl de componentes**, no el informe. La salida de texto quedo con
   el volcado de componentes. **Se re-corrio bien antes de leer ni una cifra.**
4. **Ficheros tocados que el encargo no nombraba, declarados:** `docs/COSTURAS_INTERNAS.jsonl` y
   `docs/COSTURAS_INTERNAS_RESUMEN.md`, `docs/plan/ARISTAS_DUPLICADAS.jsonl`,
   `dataset/metadata/*` y `web/lib/assets/*` (los reescriben los instrumentos y el ciclo de Gate 0).
   **Mismo alcance que las vueltas 48 a 57 MENOS el banco de rumbos**, que esta vuelta no toco
   porque el re-anclaje salio en blanco.
5. **UN WORKTREE EN `75863aee`** para toda la medicion pre fusion (la relectura del 32 y el cuadro
   de varas re-corrido). **Copie dentro el instrumento nuevo y el fichero del tramo 4 para poder
   correrlos alli**, y lo declaro en vez de dejarlo implicito.

---

## 10. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto. Son SEIS.**

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **NO EJECUTE NINGUN LOTE DEL TRAMO 5**, y el encargo los pedia. Abri el tramo entero con su dossier, su cuadro de varas y sus colisiones esperadas, y **pare ahi**. | Los 50 planes son trabajo editorial acto por acto (motivo con sus conteos y reparto pieza a pieza sobre los dos nodos leidos enteros), y **empezar un lote que no puedo terminar bien deja el arbol a medias**, que es peor que no empezarlo. **Pero es la mitad de la TAREA 2 sin hacer**, y un lector estricto puede decir que un lote corto y bien guardado valia mas que ninguno |
| **D2** | **ROTULE TRES CITAS EN VEZ DE CORREGIRLAS**, con una vara que escribi yo: *se rotula cuando reescribir la letra haria mentir a la pagina*. | El tachado conserva el texto viejo **en los dos casos**, asi que un lector estricto puede decir que **corregir nunca falsifica y por tanto el rotulo nunca hace falta**. Mi motivo es que `es ~~clase B~~ clase D, asi que se relee al cierre` deja la frase contradiciendose sola, y que el 784 vive dentro de una salida pegada verbatim. **Pero la vara que separa las dos vias la trace yo, no un acta** |
| **D3** | **CORREGI LAS CUATRO TABLAS DE DOCTRINA DEL INFORME** (393/395/396, 658/678, 1222, 1865), donde la columna de clase es **la conclusion de una regla** y no un dato suelto. En la de la linea 264 la cabecera dice literalmente *clase que dicta la regla*. | Segui el precedente ratificado del **203** (vuelta 57, `D1` y `D2` A FAVOR), cuya nota dice con todas sus letras que el argumento no cambia y que **solo se mueve el veredicto de esa fila**, y escribi esa misma frase en cada nota. **Pero la celda corregida ahora dice que la regla dicta `D`**, y la regla dictaba `A`: el matiz vive en la nota, no en la celda |
| **D4** | **PARTI EN DOS LA FILA DEL BANCO** (`2.477 / 2.488`) en vez de corregirla en su sitio, y eso **cambia la forma de una tabla del banco de textos**. | La fila publicaba una letra para dos puestos que hoy no la comparten, y dos letras en una celda es lo que el barrido llama AMBIGUO. La fila vieja queda entera y tachada. **Pero es una decision de forma sobre `BANCO_DE_TEXTOS.md`, que es doctrina, y la tome yo** |
| **D5** | **MI ROTULO ES UNA FORMA NUEVA DE REGISTRO** (`> **RETRATO CON CORTE DECLARADO (9.10)...** ROTULO puesto=N cita=X vigente=Y ...`) y le escribi al barrido un detector para que la reconozca. | El encargo pedia expresamente que **el rotulo bastara para que el barrido dejara de listarla como deuda**, y un rotulo que el instrumento no lee no cumple eso; ademas se verifica solo y cae en rojo si envejece. **Pero invente una sintaxis de registro y se la ensene a la guarda que me juzga**, y eso se puede leer como acomodar la vara al papel |
| **D6** | **AMPLIE TRES INSTRUMENTOS POR SUCESION EN UNA SOLA VUELTA** (el barrido de puestos, el tallador de planes y el abridor), mas dos nuevos, mas el del cuadro de varas. | Los cuatro son sucesores declarados con la aritmetica **copiada byte a byte** y **comprobada por diff contra el ancestro**, que es la via del acta 54 pregunta 3. **Pero son seis ficheros de instrumento en una vuelta**, y cada sucesor es una copia mas que mantener: la casa puede querer poner un techo |

---

## 11. PENDIENTES DE DOCTRINA

1. **DONDE VIVE LA PIEZA DECLARADA CUANDO EL ACTO TIENE UN SOLO PAR, Y QUE PRELACION HAY ENTRE
   CONTEOS.** **Heredado y ENGORDADO A DOCE ACTOS**: los once de la vuelta 57 **mas el 32**, que
   entra por la puerta del empate sin vara. **La rama de la CANTIDAD como vara queda NO ADOPTADA y
   no se aplica mas** (acta 57, pregunta 2), y esta vuelta la retiro del unico acto donde se habia
   usado. **La rama del `D3` sigue CERRADA POR CITA.**
2. **EL `INCISO` PARA CONDICIONES SIGUE SIN EXISTIR EN EL INSTRUMENTO.** **Heredado.** Esta vuelta
   **no lo paga**, porque no genero ningun plan.
3. **QUIEN CONTESTA UNA PREGUNTA DE POLITICA DE CATALOGO.** **Heredado y sin cambio hoy.**
4. **LA GUARDA DE LOS CUATRO AJENOS NO DICE SI HABLA DE IDS O DE NODOS.** **Heredado.** Esta vuelta
   **no lo paga**: los cuatro salen verdes por los dos caminos en el tramo 5.
5. **QUE SE HACE CON UN ACTO CERRADO CUYOS DOS MIEMBROS SON PUERTA.** **Heredado del acto 25.** **La
   declaracion ya esta cubierta por cita** (acta 57, pregunta 3, anotada hoy en el registro); **lo
   que sigue abierto es SOLO la salida de fondo**, reservada a la mesa.
6. **NUEVO: CUANTOS SUCESORES DECLARADOS PUEDE ACUMULAR UN INSTRUMENTO ANTES DE QUE LA CADENA SEA EL
   PROBLEMA.** El barrido de puestos volteados va por su **segundo** fichero en dos vueltas, el
   tallador de planes por el **tercero**, y el abridor de tramo por el **quinto**. La vara del acta
   54 pregunta 3 dice **cuando** suceder, pero **no dice nada de cuando la cadena misma pide una
   poda**. **No se elige aqui.**
7. **HEREDADOS Y SIN CAMBIO HOY**: el esquema de `OPERACIONES.jsonl` **sigue sin distinguir ejecutada
   de pendiente** (71 en `LISTA`, medido hoy) y el campo `orden` de la fase 03 **sigue sin ser su
   criterio de orden**.

---

## 12. LO QUE ESTA VUELTA NO HIZO, DICHO EN VEZ DE CALLADO

1. **NO EJECUTO NINGUN LOTE DEL TRAMO 5. ES EL INCUMPLIMIENTO DE LA VUELTA Y VA EL PRIMERO.** El
   encargo pedia abrir el tramo **y de ahi los lotes**. El tramo queda **ABIERTO Y CON TODO SU
   INSUMO MEDIDO** (nomina fijada en `TRAMO5_V58.jsonl`, cuadro de varas, colisiones esperadas en
   CERO y dossier de 1.979 lineas), asi que **la vuelta siguiente empieza por el plan del lote A y
   no por medir de nuevo**. **El motivo esta en el `D1` y no se disfraza de decision de metodo:
   fue una decision de alcance mia.**
2. **NO FUNDIO NI DESHIZO NINGUN ACTO MAS QUE EL 32.** Los **26** vivos de los tramos 1 a 4 siguen
   en los puestos **1 a 26**, medido.
3. **NO TOCO LOS SEIS DECLARADOS DEL TRAMO 4 NI EL 32**, que ahora son siete y siguen acumulando
   para la mesa.
4. **NO CORRIGIO LA SECCION PASO 3 de `RECOMPUTO_3388.md`**, y esta vez **no va marcado como
   discutible** porque el acta 57 ya lo adjudico A FAVOR (`D6`): esta cerrado por cita.
5. **NO CORRIO LA VARA 2 DE `verificar_mapas_destejido.py`**: no hay mapa de particion nuevo.
6. **NO EJECUTO NINGUNA ARISTA NI PODA DE SOLAPES** (fase 04), **ni resolvio las duplicadas
   historicas** (956 grupos sobre 754 nodos al cierre) **ni el alias durmiente `modelo_spin_2`**
   (`OP-S-12`).
7. **NO BARRIO EL RESTO DE INSTRUMENTOS EN BUSCA DE MAS TITULOS TALLADOS A MANO.** Cace dos (el
   cuadro de varas y el abridor) y **los dos por tropezarme con su salida**. **No se si quedan mas**,
   y va como pregunta 3.

---

## 13. LAS PREGUNTAS PARA EL AUDITOR

1. **La vara con la que reparti las once (corregir contra rotular) es la correcta?** (`D2`, `D3`.)
   La escribi yo: *se rotula cuando reescribir la letra haria mentir a la pagina*. **Si la vara es
   que el tachado nunca falsifica**, entonces las tres rotuladas deberian ir corregidas y el rotulo
   sobra como figura.
2. **Corregir la celda de una tabla de DOCTRINA es correcto, cuando la columna es la conclusion de
   una regla?** (`D3`.) Segui el precedente del **203** y puse el matiz en la nota. **La celda
   corregida dice hoy que la regla dicta `D`, y la regla dictaba `A`.**
3. **La especie del titulo tallado a mano se persigue por denuncia o por barrido?** (Seccion 6.)
   **Cace DOS en esta vuelta y los dos por tropezarme con su salida**, no por buscarlos. Si la
   respuesta es barrido, hace falta un instrumento que lea las cabeceras de todos los instrumentos y
   marque las constantes, y eso es trabajo de una vuelta.
4. **Cuantos sucesores declarados puede acumular un instrumento antes de que la cadena sea el
   problema?** (Pendiente 6, `D6`.) El abridor de tramo va por su quinto fichero.
5. **Partir una fila de `BANCO_DE_TEXTOS.md` en dos es alcance del carril `9.10`?** (`D4`.) La fila
   ya no podia decir la verdad con una sola letra, pero cambie la forma de una tabla de doctrina.
6. **Fue correcto parar antes de los lotes en vez de hacer un lote corto?** (`D1`.) **Es la pregunta
   que mas me importa**, porque de la respuesta depende como se reparte el trabajo de un tramo entre
   vueltas cuando la tarea 1 se come la mitad de la vuelta.
