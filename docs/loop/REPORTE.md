# REPORTE DE LA VUELTA 54 (20 ago 2026, ejecutor Opus 5)

**LA TAREA 1 ENTERA, sus CUATRO puntos, con las cifras de dos de ellos RE-MEDIDAS en vez de
copiadas del acta. Y LA TAREA 2 ABRE EL TRAMO 2 Y FUNDE VEINTIUN ACTOS EN DOS LOTES. EL HALLAZGO
DE LA VUELTA SALE DE CORRER LA GUARDA QUE EL ENCARGO MANDA: `vuelta51_colisiones_esperadas.py`
sobre la nomina del dia NO IMPRIME NI UNO de los cincuenta actos del tramo 2, porque su linea 130
salta la fusion pura, y los cincuenta son de fusion pura. La guarda no se apago: se le escribio un
sucesor declarado con la misma aritmetica. Y EL SEGUNDO HALLAZGO ES LA FORMA DEL TRAMO: donde el
tramo 1 dejo veintisiete mixtos esperando cinco vueltas, EL TRAMO 2 NO PIDE NI UNA SOLA LECTURA
`P.12`.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `92618dde` (el acta de la vuelta 53), **arbol limpio y todo pusheado** |
| **hash final** | `PENDIENTE, se escribe en el commit siguiente al del cierre` |
| **commits de la vuelta** | **4**: `e30e2ccb` (TAREA 1), `0feef54e` (tramo 2 abierto y lote A), `ca191ee6` (lote B) y el del cierre |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1, y la regla de la apertura del `D1` de la vuelta 53)

**Corrida ANTES de tocar nada. TODAS las filas son corridas propias de esta vuelta y NINGUNA se
hereda del cierre anterior**, que es exactamente lo que el `D1` de la vuelta 53 dejo pendiente y
el encargo convirtio en regla. **El arbol estaba limpio y todo pusheado en `92618dde`, asi que la
regla 3 se cumplio por vacio, y se dice asi en vez de darla por cumplida.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 73 / 6 / 2.758 | **551 / 73 / 6 / 2.758**, sin mover |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.477 / 376 / 17.052 | **3.853 / 3.456 / 397 / 17.118** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 72 / 479 | **551 / 93 / 458** |
| actos (componentes) | 285 | **264** |
| actos `CERRADOS` / `ABIERTOS` | 232 / 53 | **211 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 473 / 240 | **431 / 240** |
| cola de costuras | 1.483 | **1.489** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 51 | **72** |
| duplicadas historicas: grupos / nodos | 997 / 787 | **988 / 779** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK | **TODAS OK** |
| actos del tramo 2 fundidos / pendientes | 0 / 50 | **21 / 29** |

**Instrumentos de la apertura, todos corridos antes de la primera operacion:**
[`SALIDA_V54_APERTURA.txt`](SALIDA_V54_APERTURA.txt),
[`SALIDA_V54_MARCADOR_APERTURA.txt`](SALIDA_V54_MARCADOR_APERTURA.txt),
[`SALIDA_V54_RECOMPUTO_APERTURA.txt`](SALIDA_V54_RECOMPUTO_APERTURA.txt),
[`SALIDA_V54_COLA_APERTURA.txt`](SALIDA_V54_COLA_APERTURA.txt),
[`SALIDA_V54_COLISIONES_APERTURA.txt`](SALIDA_V54_COLISIONES_APERTURA.txt) y
[`SALIDA_V54_DUPLICADAS_APERTURA.txt`](SALIDA_V54_DUPLICADAS_APERTURA.txt). **El cierre esta en
los ficheros `_CIERRE` hermanos, corridos DESPUES del ultimo movimiento.**

**EL MARCADOR NO SE MUEVE, Y NO ES UN OLVIDO DEL BARRIDO.** Esta vuelta **no volteo ni un
veredicto**: los veintiun actos fundidos son de FUSION PURA y **ninguno fabrico colision**, asi
que `P.16` no tuvo nada que limpiar. **Por eso las DOS tablas por dominio hermanas tampoco se
mueven: la `A` de cada uno de los diez dominios es la misma al digito**, comprobado en las dos
corridas del marcador. **La hermandad escrita en la TAREA 1.1 de la vuelta 53 se cumple POR VACIO
y se dice asi en vez de darla por cumplida.**

**LO QUE SI SE MOVIO ES EL RETRATO, y cuadra al digito con lo ejecutado:** **VEINTIUN colapsos
mas** (72 a 93) y **VEINTIUN pares distintos menos** (479 a 458), **uno por cada acto fundido**,
porque cada fusion convierte el par `A` interno del acto en un par cuyos dos ids resuelven al
mismo nodo vivo. **458 es la resta exacta**: 551 crudas menos 93 colapsos.

**EL GRAFO GANA 66 ENLACES** (17.052 a 17.118) y **21 nodos pasan a deprecados** (376 a 397), que
es exactamente el numero de actos fundidos.

---

## 1. TAREA 1: LOS CUATRO PUNTOS, Y DOS DE ELLOS CON LA CIFRA RE-MEDIDA

**Instrumento: `scripts/loop/vuelta54_correcciones_tarea1.py`, idempotente al re-correrlo
([`SALIDA_V54_CORRECCIONES_T1_IDEMPOTENCIA.txt`](SALIDA_V54_CORRECCIONES_T1_IDEMPOTENCIA.txt)).**

| | lo que se escribio | de donde salen sus cifras |
|---|---|---|
| **1.1** | **LA PRECISION DE LA ESTRELLA**, nota NUEVA y fechada al final del **9.3.1** de `docs/BANCO_DE_TEXTOS.md`, **sin tachar nada**: cuando el GANADOR POR DERECHO de sus pares `A` es el CENTRO de una estrella cuyas puntas son `D` entre si, **manda la receta de `P.12` y el centro muere absorbido por el viable que el contenido elija** | **NO del acta: de corrida propia.** `scripts/loop/vuelta54_ejemplares_estrella.py` (nuevo) lee la clase de cada par **HOY y al abrir la vuelta 53** (commit `d88c42bb`, por git) y comprueba nodo a nodo que **ninguno de los tres centros pierde un solo par `A`**: los tres son GANADOR POR DERECHO, los tres estan hoy `deprecado: true` y los tres supervivientes vivos con el alias izado ([`SALIDA_V54_EJEMPLARES_ESTRELLA.txt`](SALIDA_V54_EJEMPLARES_ESTRELLA.txt)) |
| **1.2** | **LAS DOS AMPLIACIONES DEL CARRIL GENERAL DE COLISIONES**, adosadas al registro **1.4.b** de la vuelta 53 en `03_FUSIONES.md` **sin reescribir la tabla vieja**: la condicion de CONTEO O COBERTURA es **carril de TEXTO en sentido amplio** y se descarga POR MEDICION antes de fundir (figura, el `811`); y cuando mover un solo veredicto deja la colision viva, **LA RELECTURA MUEVE LOS DOS** y lo dice en las dos correcciones (figura, el par `811` contra `1222`) | las dos figuras y sus varas, del acta de la vuelta 53, seccion 5, preguntas 5 y 6, **leidas hoy** |
| **1.3** | **EL ROTULO DEL CENSO DE DUPLICADAS** de `vuelta48_fundir_tramo.py`, los dos `print`, con el **texto viejo delante entero** y la frase adosada: *CENSO PROPIO DE LA GUARDA; LA CIFRA DE OP-S-12 LA PUBLICA `aristas_duplicadas_tras_resolver.py`*. **LA LOGICA NO SE TOCA**, y el comentario dice por que el censo de la guarda ignora los alias de deprecados | la referencia del encargo (*hoy lineas 418 a 421*) **verificada por git**: ese `print` vivia en la linea 418 del commit anterior |
| **1.4** | **LA NOTA DE LOS 41 ENLACES**, adosada al registro del tramo de la vuelta 53 | **NO copia la derivacion del acta: la vuelve a medir.** `scripts/loop/vuelta54_41_enlaces.py` (nuevo) sobre los SEIS commits ([`SALIDA_V54_41_ENLACES.txt`](SALIDA_V54_41_ENLACES.txt)) |

**LA DERIVACION DE LOS 41 SALE MAS FINA QUE LA DEL ACTA, y eso es lo que se gana re-midiendo en
vez de copiar:** el acta cerro la resta global (45 vistas menos 4 retiros son 41); **mi corrida
la cierra LOTE A LOTE**, que es una comprobacion que la resta global no hace:

| lote | vistas de la simetrizacion | instancias retiradas | esperado | delta de enlaces MEDIDO | |
|---|---:|---:|---:|---:|---|
| **A** (`cadc9977`) | 13 | 1 | +12 | **+12** | **CALZA** |
| **B** (`04bd56de`) | 9 | 2 | +7 | **+7** | **CALZA** |
| **C** (`90bb930c`) | 23 | 1 | +22 | **+22** | **CALZA** |
| **la vuelta 53 entera** | **45** | **4** | **+41** | **+41** | **CALZA** |

**Y LAS CUATRO INSTANCIAS SE VERIFICAN UNA A UNA** (el id absorbido estaba en el campo ANTES del
lote y ya no esta DESPUES), **con los dos colapsos comprobando ademas que el superviviente YA
ESTABA en el campo**, que es lo que hace que dos instancias colapsen en una.

**UNA CORRECCION DECLARADA SOBRE MI PROPIO INSTRUMENTO DE LOS 41:** su primera version contaba
las instancias por el TAMANO del campo antes y despues, y esa resta da CERO, porque la
simetrizacion anade aristas a esos mismos campos en el mismo commit. **La cifra salio `CALZA: NO`
y se reescribio para contar LA INSTANCIA NOMBRADA**, que es lo que el acta afirma. **La primera
version no se publico.**

**Y UN PUNTO DE ALCANCE MIO, DECLARADO Y MARCADO (`D1`): la TAREA 1.3.b.** El encargo nombra
`vuelta48_fundir_tramo.py`, y la referencia es exacta. **Pero el instrumento que EJECUTA los
tramos desde la vuelta 49 es su sucesor declarado, `vuelta49_fundir_tramo.py`, que lleva LOS
MISMOS DOS ROTULOS palabra por palabra en sus lineas 478 a 481**, y es el que la vuelta 53 corrio
(comprobado: solo el de la 49 imprime `INCISOS ADOSADOS`, y las tres salidas de sus lotes lo
imprimen). **Reparar solo el ancestro dejaria el sintoma vivo justo donde la cifra se publica en
cada tramo. Adose la misma frase con el mismo texto viejo delante, y va marcado.**

---

## 2. TAREA 2: EL TRAMO 2, ABIERTO Y CON VEINTIUN ACTOS FUNDIDOS

### 2.1 LA FRONTERA DEL TRAMO NO SE DECIDIO: SE MIDIO

*Los 50 siguientes* admitia **dos lecturas**, y `scripts/loop/vuelta54_tramo2_nomina.py` computa
**las dos** ([`SALIDA_V54_TRAMO2_NOMINA.txt`](SALIDA_V54_TRAMO2_NOMINA.txt)):

| lectura | resultado |
|---|---|
| **A, por el orden de HOY**, saltando los actos del tramo 1 que siguen vivos **identificados POR SUS MIEMBROS** | los once del tramo 1 estan en los puestos **1 a 11** y el tramo 2 es del **12 al 61** |
| **B, por el orden de la vuelta 48**: los que ocupaban los puestos **51 a 100** de `RECOMPUTO_V48_COMPONENTES.jsonl` | **los mismos 50, en el mismo orden** |

> **LAS DOS COINCIDEN AL ACTO Y AL ORDEN, y el instrumento cae en ROJO CON PARADA si algun dia no
> calzan.** Una operacion cuyo texto no alcanza para ejecutarse sin decidir detiene; **esta
> alcanza, y la prueba esta impresa en vez de argumentada.**

### 2.2 LA FORMA DEL TRAMO 2, Y ES LO CONTRARIO DEL TRAMO 1

| | |
|---|---:|
| actos del tramo | **50** |
| por tamano | **los 50 de tamano 2** |
| por figura | **`{'PURO A': 50, 'MIXTO': 0}`** |
| nodos implicados | **100** |
| **lecturas `P.12` que este tramo pide** | **CERO** |

**Un acto de dos miembros con UN par `A` directo no deja ningun mixto fuera**, asi que la receta
de la estrella no tiene nada que decidir. **Lo que este tramo pide es la otra mitad de `P.8`:
quien sobrevive por CONTENIDO.** Guarda de los cuatro ajenos **VERDE** (y ninguno de los cuatro
esta ya en el lote `CERRADO` entero) y guarda de solape con el tramo 1 **VERDE, cero**.

### 2.3 EL HALLAZGO: LA GUARDA DE COLISIONES NO CUBRIA ESTA FORMA

**Corrido `scripts/loop/vuelta51_colisiones_esperadas.py` sobre la nomina del dia, como el encargo
2.2 manda, NO IMPRIME NI UNO de los cincuenta actos**
([`SALIDA_V54_COLISIONES_ESPERADAS.txt`](SALIDA_V54_COLISIONES_ESPERADAS.txt)). **El motivo esta
en su propio codigo, linea 130:** `continue  # fusion pura, no pide P.12`. **Y es correcto para lo
que aquel instrumento mide**: nacio para la guarda de cuenta de la vuelta 51, que cuenta una
colision por cada mixto en `CONTINUA`.

**La guarda no se apago y el instrumento viejo no se falseo: se escribio un SUCESOR DECLARADO**
(`scripts/loop/vuelta54_colisiones_esperadas.py`), **con la misma aritmetica copiada** y la rama
que faltaba. **Lo que predice, sobre el archivo entero y antes de tocar un nodo**
([`SALIDA_V54_COLISIONES_ESPERADAS_TRAMO2.txt`](SALIDA_V54_COLISIONES_ESPERADAS_TRAMO2.txt)):
**100 combinaciones simuladas, 6 que fabrican colision, y SOLO TRES ACTOS del tramo**: el **6**
(dos), el **44** (una) y el **49** (dos). **Las cinco son `B` DIRECTO contra `D` y todas FUERA del
acto**, o sea del carril del filo. **Los otros 47 actos, cero.**

### 2.4 LOS VEINTIUN ACTOS FUNDIDOS, EN DOS LOTES

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | colisiones predichas | **medidas** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14 | **11** | **11** | **70** | 19 | 38 | **13** | **0** | **0, CALZA** |
| **B** | 16, 17, 19, 21, 22, 23, 24, 25, 26, 27 | **10** | **10** | **57** | 16 | 35 | **6** | **0** | **0, CALZA** |

**Guardas, por acto y en los veintiuno:** miembros vivos y nomina completa, cobertura exacta de
indices sin olvidos, cero repetidos literales, **cero auto-aristas y cero duplicadas NUEVAS**, y
los cinco campos que la operacion no redacta **intactos, 55 de 55 en el lote A y 50 de 50 en el
B**. **La guarda `1B` paso POR VACIO en los veintiuno: ningun absorbido es puerta.**

### 2.5 LAS FORMAS DEL VEREDICTO, CONTADAS POR MAQUINA Y NO TECLEADAS

`scripts/loop/vuelta54_varas_tramo2.py` imprime **una fila por acto** con pasos, condiciones y
cableado contados, y **la FORMA del veredicto**
([`SALIDA_V54_VARAS_TRAMO2.txt`](SALIDA_V54_VARAS_TRAMO2.txt)):

| la forma | de los 50 | que decide | fundidos asi en esta vuelta |
|---|---:|---|---|
| **TODAS DE ACUERDO** | 13 | las varas de contenido que no empatan apuntan al mismo lado | 7 |
| **UNA SOLA VARA** | 22 | una sola vara de contenido no empata **y BASTA** (acta 53, pregunta 4) | 10 |
| **CHOCAN** | 5 | decide **LA PIEZA DECLARADA**; si no hay ninguna, **PARADA** (acta 53, pregunta 3) | 1 (el 25) |
| **CONTENIDO EMPATA** | 9 | **EL CABLEADO DECIDE SOLO** | 3 (21, 23, 27) |
| **EMPATE SIN VARA** | 1 | **se DECLARA** | 0 |

**Y SE DECLARA UNA CORRECCION SOBRE MI PROPIO INSTRUMENTO ANTES DE QUE NADIE LA ENCUENTRE:** la
mesa (`vuelta54_mesa_tramo2.py`) imprime una columna **MATERIAL PROPIO** calculada por **solape
lexico**, y **esa columna NO es la vara**: la receta define el contenido como *pasos y
condiciones, material propio y padre declarado EN LAS RAZONES*, y el material propio de la receta
es **el que la razon declara**, no el que un contador de palabras estima. **La retire de las varas
que deciden y quedo rotulada como contraste de maquina.** **Va marcada (`D9`), porque la columna
si esta publicada en la salida.**

### 2.6 LOS ACTOS QUE ESTA VUELTA NO FUNDE, CADA UNO CON SU ESPECIE

| actos | especie | por que |
|---|---|---|
| **1** y **15** | **EL CONTENIDO APUNTA AL QUE NO ES PUERTA** | la guarda `1B` exige que la puerta sobreviva y el contenido elige al otro (pasos 6 contra 4 y condiciones 3 contra 2 en el 1; pasos 5 contra 4 en el 15). **Ese choque no lo resuelve ninguna regla escrita hoy**, y el instrumento de las puertas lo dice desde la vuelta 48: *va como pregunta al auditor, no como decision*. **SE DECLARAN** (`D3`) |
| **4**, **20** y **42** | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | pasos a un lado, condiciones al otro, y la razon **no declara padre, ni contencion, ni alcance del rol**: la del 326 llega a escribir que los dos anadidos son *la misma deteccion por dos caminos*. **El acta 53, pregunta 3, manda PARAR y traerlo como pregunta** (`D2`) |
| **18** | **EMPATE SIN VARA** | pasos 4 contra 4, condiciones 3 contra 3 **y cableado 2 contra 2**. Es el unico del tramo donde TODO empata |
| **6**, **44** y **49** | **COLISION PREVISTA, PENDIENTE DE RELECTURA** | los tres fabrican colision `B` directo contra `D` y el carril del filo pide relectura EN EL MISMO ACTO. **No hubo cuerda** |
| los **veinte** restantes | **SIN TOCAR POR FALTA DE CUERDA** | ninguna guarda los frena |

---

## 3. EL CASO POSITIVO: LAS CUATRO GUARDAS PUESTAS A FALLAR, Y POR QUE HUBO QUE REESCRIBIRLO

**Corrido ANTES de ejecutar nada** (`scripts/loop/vuelta54_caso_positivo.py`,
[`SALIDA_V54_CASO_POSITIVO.txt`](SALIDA_V54_CASO_POSITIVO.txt)).

**EL CASO POSITIVO DE LA VUELTA 53 SE RE-CORRIO PRIMERO Y SALIO VERDE, y aun asi hubo que
reescribirlo**, por el mismo motivo por el que aquella vuelta reescribio el de la 52: sus tres
mentiras se fabricaban con `customer_profile_value_map`, que **aquella misma vuelta depreco**.
Re-corrido hoy ([`SALIDA_V54_CASO_POSITIVO_V53.txt`](SALIDA_V54_CASO_POSITIVO_V53.txt)), **la
mentira de la cobertura falla por CUATRO motivos y solo uno es el suyo**. Las tres se rehicieron
sobre un acto **VIVO** del tramo 2.

| guarda | la mentira | resultado |
|---|---|---|
| **`1B`** | un plan cuyo absorbido es `domina_lo_que_compras`, que es puerta | **exit 1, `ROJO`, aborta sin escribir** |
| **cobertura** | un plan que se olvida del paso 3 del absorbido | **exit 1, `faltan ['3']`, aborta sin escribir** |
| **INCISO VERBATIM** | un inciso que es PARAFRASIS y no trozo literal | **exit 1, `NO es trozo verbatim`, aborta sin escribir** |
| **colisiones** | el censo contra una cuenta esperada FALSA de 9 | **`MEDIDA: 0 \| CALZA: NO`** |

**LAS CUATRO MUERDEN, Y CADA UNA POR SU MOTIVO.**

**Y LA GUARDA DEL INCISO MORDIO DE VERDAD, no solo en el caso positivo:** el generador de planes
(`scripts/loop/vuelta54_planes.py`) comprueba el verbatim **antes** de escribir el plan, y **cazo
OCHO incisos mios escritos sin acentos**; no escribio nada hasta que los corregi. **Es la guarda
funcionando, no un acierto mio.**

---

## 4. EL BARRIDO `9.10` DEL CIERRE, CORRIDO DESPUES DEL ULTIMO MOVIMIENTO

**Con las cifras viejas DE HOY** (`--viejo 551,73,6,2758 --retrato 72,479`,
[`SALIDA_V54_BARRIDO_910_CIERRE.txt`](SALIDA_V54_BARRIDO_910_CIERRE.txt), 87 candidatos).
**SEIS celdas corregidas** ([`SALIDA_V54_CORRECCIONES_910.txt`](SALIDA_V54_CORRECCIONES_910.txt),
idempotente al re-correrlo):

| la celda | decia | **medido al cierre** |
|---|---:|---:|
| `RECOMPUTO_3388.md` **247**, colapsos **y su contador** | 72, contador SIETE | **93, contador OCHO** |
| **248**, pares distintos **y su contador** | 479, contador DIEZ | **458, contador ONCE** |
| **528**, el checkpoint `ii` en sus dos parentesis **y su nota** | 479 igual a 479 | **458 igual a 458, sigue OK** |

**LA FILA 246 (`A` crudas) NO SE TOCA Y NO ES UN OLVIDO:** esta vuelta no volteo ningun veredicto,
asi que la `A` global es la misma al abrir y al cerrar. **Y LAS DOS TABLAS POR DOMINIO HERMANAS
TAMPOCO, por lo mismo**: la `A` de cada uno de los diez dominios es identica al digito. **La
hermandad se cumple POR VACIO y se dice, en vez de darla por cumplida.**

---

## 5. GATE 0 Y LAS SUITES

**Corridos tras cada uno de los dos lotes y otra vez al cierre. Todos exit 0.**

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`** las tres veces; `etiquetas_de_cara --aplicar` con **71** etiquetas; `sync_assets_web` con **6** assets |
| **suite del motor** | **25 de 25**, las tres veces |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas |
| `tsc --noEmit` | **CERO** lineas |
| duplicadas / auto-aristas **NUEVAS** | **CERO** y **CERO** en los dos lotes |
| las cuatro comprobaciones de `08_VERIFICACION` | **TODAS OK** al cierre (671 igual a 671; 458 igual a 458) |
| censo de colisiones **al cierre** | **CERO** |
| **hook guardian** | verde en todos los commits |

---

## 6. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

1. **MI PRIMER INSTRUMENTO DE LOS 41 ENLACES llamaba a `git show` una vez POR FICHERO** (3.853
   por commit, seis commits) **y no termino en dos minutos.** Reescrito con una sola pasada de
   `git cat-file --batch` por commit, **con la vara intacta y el cambio declarado en su
   docstring.**
2. **Y SU SECCION 3 CONTABA LA COSA EQUIVOCADA:** medía el TAMANO del campo antes y despues, y esa
   resta da CERO porque la simetrizacion anade aristas a esos mismos campos en el mismo commit.
   **Salio `CALZA: NO` y se reescribio para contar LA INSTANCIA NOMBRADA.** La version mala **no
   se publico**.
3. **OCHO DE MIS INCISOS ESTABAN SIN ACENTOS** y el generador los rechazo antes de escribir el
   plan. **Los corregi contra el texto verbatim del paso.** Y **tres de mis nexos** tambien iban
   sin acentos (*y tambien*, *ademas*, *tacticas*): corregidos antes de sellar.
4. **MI PRIMERA VERSION DE LOS PLANES NO LLEVABA EL CAMPO `declarados_y_no_fundidos`** y el
   ejecutor cayo con `KeyError` **despues de tener todas las guardas en verde**, exactamente la
   misma caida que la vuelta 53 declaro en su correccion 1. **Lo puse en el generador para que
   vaya SIEMPRE**, aunque el lote no declare ninguno. **No escribio nada porque corria en modo
   simular.**
5. **LA COLUMNA `MATERIAL PROPIO` DE MI MESA es un contraste lexico y no la vara**, y lo declare
   antes de usarla para decidir (`D9`).
6. **MI PRIMER BORRADOR DE LA TABLA DEL CIERRE PUBLICABA LOS AUTO-PARES DE DESPUES DEL LOTE
   A (62) EN LA COLUMNA DE CIERRE**, que es la especie exacta del `D1` de la vuelta 53 en
   pequeno: medir temprano y publicar tarde sin remedir. **Lo cace releyendo la salida del
   censo del cierre, que imprime la cifra al lado de las colisiones**, y la columna publica
   **72**, medido DESPUES del ultimo movimiento
   ([`SALIDA_V54_COLISIONES_CIERRE.txt`](SALIDA_V54_COLISIONES_CIERRE.txt)). **El borrador no
   se llego a publicar.**
7. **Ficheros tocados que el encargo no nombraba, declarados:** `docs/COSTURAS_INTERNAS.jsonl` y
   `docs/COSTURAS_INTERNAS_RESUMEN.md`, `docs/plan/ARISTAS_DUPLICADAS.jsonl`,
   `dataset/metadata/*` y `web/lib/assets/*` (los reescriben los instrumentos y el ciclo de Gate
   0). **Mismo alcance que las vueltas 48 a 53.** Y **`scripts/loop/vuelta49_fundir_tramo.py`**,
   que va aparte y marcado (`D1`).

---

## 7. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto. Son DOCE.**

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **Adose la frase de la TAREA 1.3 tambien a `vuelta49_fundir_tramo.py`**, que el encargo NO nombra. | El encargo nombra el de la 48 y su referencia de linea es exacta. **Pero el que se corre es el de la 49, y lleva el mismo rotulo.** Reparar solo el ancestro dejaba el sintoma vivo donde la cifra se publica. **Anadir un fichero que el encargo no nombra es alcance mio** |
| **D2** | **Declare TRES actos (4, 20 y 42) por conteos de contenido que chocan sin pieza declarada EN LA RAZON**, en vez de leer el ALCANCE DEL ROL en los `entregable_esperado` de los dos nodos. | La receta dice *padre declarado EN LAS RAZONES*, y ahi no hay nada. **Pero la vuelta 53 leyo alcance del rol de la razon de OTRO par del acto, y aqui no hay otro par.** Si el auditor lee que el entregable del nodo tambien es pieza declarada, **los tres se podian fundir** |
| **D3** | **Declare DOS actos (1 y 15) porque el contenido apunta al que NO es puerta**, en vez de fundir con la puerta de superviviente. | La guarda `1B` es obligatoria y **la vara de las puertas la cumpliria fundiendo hacia la puerta**; el instrumento de puertas dice que el choque *va como pregunta al auditor*. **Elegi parar. Un lector puede decir que la guarda YA decide y que declararlos es no ejecutar lo ejecutable** |
| **D4** | **En el acto 24 (SCOR) elegi `scor_model_operaciones` por UNA sola vara, las condiciones 3 contra 2**, con pasos y cableado empatados. | La razon del **342** le reconoce al OTRO *bajar a metricas de nivel 2 y de diagnostico de nivel 3* y a este *quedarse en los KPI de nivel 1*. **Si eso se lee como contencion declarada, mandaria y elegiria al otro.** Lo lei como material propio A LOS DOS LADOS (el otro anade el benchmark) y por eso decidio el conteo. **Lo que lo hace sostenible es el reparto: los niveles 2 y 3 viajan ENTEROS** |
| **D5** | **En el acto 23 (cascada) decidio EL CABLEADO SOLO** con el contenido empatado. | La razon del **340** llama al gesto propio del OTRO *su unico gesto propio*, y una pieza declarada pesa mas que el cableado. **Lo trate como que los dos anaden y por eso el contenido empata.** Tambien aqui **el gesto propio viaja ENTERO** |
| **D6** | **En el acto 2 meti de `APPEND` el paso 4 del absorbido aunque su segunda mitad (publicitar para narrativa) ya la dice el paso 4 del superviviente.** | Su primera mitad (**documentar** el proceso) no la dice nadie, **y esta operacion mueve piezas enteras y no parte pasos**. El solape que fabrica es de los que recoge la poda de la fase 04. **Pero es un solape que yo fabrico a proposito** |
| **D7** | **En el acto 7 marque `CUBIERTO` con PERDIDA NOMBRADA** la comparacion contra el periodo anterior, **en vez de `INCISO`**. | El inciso encadenado sobre el mismo paso 1 habria quedado *hacerlo cada mes o contra el periodo anterior*, **que dice otra cosa**. La tabla de los seis motivos manda exactamente eso. **Pero es una perdida que yo elijo aceptar** |
| **D8** | **Escribi un SUCESOR del instrumento de colisiones en vez de repararlo.** | La vuelta 51 reparo ESE MISMO instrumento el dia que nacio, con correccion declarada. **Elegi sucesor para no mover un instrumento que cuatro registros ya citan.** Un lector puede decir que ahora hay dos instrumentos donde antes habia uno |
| **D9** | **Publique en la mesa una columna `MATERIAL PROPIO` calculada por solape lexico**, y luego la declare NO-vara. | La cifra esta impresa en `SALIDA_V54_MESA_TRAMO2.txt` **y se puede leer como una vara aunque yo diga que no lo es.** Deberia haberla rotulado como contraste desde la primera corrida |
| **D10** | **Los lotes no van en el orden impreso del tramo:** elegi primero los actos limpios y deje fuera los que tenian puerta, choque o colision. | El tramo tiene un orden y el encargo pide `P.8` EN ORDEN. **Los ejecute en orden dentro de cada lote, pero el lote lo forme por especie.** Es una decision de trabajo que nadie adjudico |
| **D11** | **En el acto 21 mande el paso 5 del absorbido a `CUBIERTO:3` con perdida nombrada del matiz** *emocionales y funcionales*. | El paso 3 del superviviente documenta *reacciones y sugerencias*, que no es lo mismo. **Podia haber ido de `INCISO`** |
| **D12** | **El caso positivo se fabrico sobre el acto 10 del tramo 2, que ESTA MISMA VUELTA fundio despues.** | Corrio ANTES de la fusion y era un acto vivo, que es lo que se le pide. **Pero deja el caso positivo caducado para la vuelta que viene, que es justo la trampa que esta vuelta tuvo que arreglar** |

---

## 8. PENDIENTES DE DOCTRINA

1. **EL CHOQUE ENTRE LA VARA DE LA FASE Y LA VARA DE LAS PUERTAS.** Cuando el CONTENIDO elige al
   miembro que **no** es puerta, `P.8` y la guarda `1B` piden cosas distintas. **El propio
   instrumento de las puertas lo declara sin resolver desde la vuelta 48**, y hasta hoy nunca
   habia pasado porque el contenido siempre coincidio con la puerta. **Esta vuelta pasa DOS
   veces** (actos 1 y 15). **Declarados y traidos** (`D3`).
2. **DONDE VIVE LA PIEZA DECLARADA CUANDO EL ACTO TIENE UN SOLO PAR.** La receta dice *padre
   declarado EN LAS RAZONES*; en un acto de dos miembros **la unica razon es la del propio par**,
   y si esa razon no declara direccion no hay a donde mirar. **Los `entregable_esperado` de los
   dos nodos si dicen alcance, pero no son razones.** **Aparecio TRES veces** (`D2`).
3. **UN INSTRUMENTO DE GUARDA QUE NO CUBRE UNA FORMA: SE REPARA O SE SUCEDE.** Las dos vias tienen
   precedente en la casa. **Elegi sucesor y lo traigo** (`D8`).
4. **QUIEN CONTESTA UNA PREGUNTA DE POLITICA DE CATALOGO.** Heredado y sin cambio. **Sigue
   afectando a DOS actos declarados del tramo 1** (el del S&OP por el 703 y el del mapa de
   influencia por el 604).
5. **HEREDADOS Y SIN CAMBIO HOY**: el `INCISO` para condiciones **sigue sin existir** en el
   instrumento (esta vuelta lo habria usado en el acto 3, donde la condicion 2 pierde un *o
   creativo*); el esquema de `OPERACIONES.jsonl` **sigue sin distinguir ejecutada de pendiente**
   (71 en `LISTA`, medido hoy); y el campo `orden` de la fase 03 **sigue sin ser su criterio de
   orden**.

---

## 9. LO QUE ESTA VUELTA NO HIZO, DICHO EN VEZ DE CALLADO

1. **NO FUNDIO LOS VEINTINUEVE ACTOS RESTANTES DEL TRAMO 2.** De los 50, quedan **29**: veinte sin
   tocar por falta de cuerda, tres pendientes de relectura del filo (6, 44 y 49), tres declarados
   por conteos que chocan (4, 20 y 42), dos declarados por el choque de la puerta (1 y 15) y uno
   por empate sin vara (18). **Es el incumplimiento de la vuelta y va el primero.**
2. **NO HIZO LAS CINCO RELECTURAS DEL FILO** que los actos 6, 44 y 49 piden, **que estan
   predichas, nombradas y con sus puestos** (`668`/`1312`, `968`/`1305`, `218`/`1008`,
   `338`/`490`, `297`/`497`).
3. **NO TOCO NINGUNO DE LOS ONCE ACTOS VIVOS DEL TRAMO 1**, incluidos los cinco de fusion pura y
   los tres imposibles por puerta. **Sus ordinales al cerrar se leen de la salida del dia**: hoy
   son los puestos **1 a 11** de la nomina.
4. **NO EJECUTO NINGUNA ARISTA NI PODA DE SOLAPES**: son de la fase 04. **Y esta vuelta fabrico
   solapes a proposito** en el acto 2 (`D6`), que quedan para esa poda.
5. **NO RESOLVIO LAS DUPLICADAS HISTORICAS** (988 grupos al cierre, medidos con
   `aristas_duplicadas_tras_resolver.py`) ni el alias durmiente `modelo_spin_2`: son de `OP-S-12`.
6. **NO REPARO `vuelta51_colisiones_esperadas.py`**: le escribio un sucesor (`D8`).

---

## 10. LAS PREGUNTAS PARA EL AUDITOR

1. **Cuando el CONTENIDO elige al miembro que no es puerta, quien manda: `P.8` o la guarda `1B`?**
   (`D3`, pendiente 1.) **Declare los actos 1 y 15.** Si manda la guarda, los dos se funden hacia
   la puerta y estaban listos.
2. **En un acto de UN SOLO PAR cuyos conteos de contenido chocan, el `entregable_esperado` de los
   nodos vale como PIEZA DECLARADA (alcance del rol), o solo valen las razones?** (`D2`,
   pendiente 2.) **De la respuesta dependen tres actos declarados.**
3. **Cuando un instrumento de guarda no cubre una forma nueva, se repara o se le escribe un
   sucesor?** (`D8`, pendiente 3.) La vuelta 51 reparo este mismo instrumento; yo le escribi un
   sucesor.
4. **El MATERIAL PROPIO que `P.8` pesa es SOLO el que la razon declara, o tambien el que se puede
   medir sobre los pasos?** (`D9`.) Lo trate como solo-declarado y retire mi propia columna.
5. **Una pieza cuya PRIMERA mitad es propia y la SEGUNDA ya la dice el superviviente: `APPEND`
   entero (y solape fabricado) o `CUBIERTO` con perdida nombrada?** (`D6`.) Elegi `APPEND`.
6. **El lote se forma por ORDEN del tramo o por ESPECIE del acto?** (`D10`.) Lo forme por especie
   para no mezclar los que necesitan relectura con los que no.
7. **El caso positivo debe fabricarse sobre actos que la propia vuelta NO vaya a fundir**, para
   que no caduque en la vuelta siguiente? (`D12`.) Es la tercera vuelta seguida que tiene que
   reescribirlo por esta causa.
