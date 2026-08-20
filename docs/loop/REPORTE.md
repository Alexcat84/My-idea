# REPORTE DE LA VUELTA 61 (20 ago 2026, ejecutor Opus 5)

**LO PRIMERO, PORQUE EL ENCARGO MANDA DECIRLO PRIMERO: EL LOTE A DEL TRAMO 6 NO SE EJECUTA EN ESTA
VUELTA.** Se entrega **LA APERTURA ENTERA** del tramo 6 con sus cuatro piezas por instrumento y sus
guardas en verde, mas el contrato de la perdida sellada con su tallador y su caso positivo. Es la via
que el **acta 58, pregunta 6** deja escrita. **NINGUN NODO SE TOCO EN ESTA VUELTA:** el grafo cierra
igual que abrio, celda por celda.

**LA FECHA DE ARRIBA ESTA MEDIDA POR DOS RELOJES Y NO SUPUESTA:** `date` del sistema da `2026-08-20` y
`git log -1 --date=format:'%Y-%m-%d'` da `2026-08-20`. Es la misma medicion que
`scripts/loop/triage_ambar_titulos.py` escribe en el `corte=` de cada uno de los 25 rotulos que sello
hoy, y ese instrumento **cae en ROJO sin escribir si los dos relojes no coinciden**.

**LA RACHA DE REPORTE ESTABA EN DOS Y EL FRENO VA DELANTE.** La regla de dictado que el encargo pone
para este reporte se aplica en cada seccion: **todo instrumento que cayo en ROJO y luego quedo
arreglado se dicta con las DOS mitades en la misma frase**, cayo Y como quedo. Los cuatro sitios donde
esta vuelta tuvo un ROJO propio estan dictados asi y van nombrados en la seccion 8.

**EL HALLAZGO DE LA VUELTA, Y NO ES DE INSTRUMENTO SINO DE FONDO: OP-U-01 SE ESTA ACABANDO.** El
abridor del tramo 6 midio que **fuera de los tramos 1 a 5 quedan VEINTIUNO actos `CERRADOS`, no
cincuenta**. La vara pide cincuenta. El abridor **no recorto, no relleno y no callo**: se llevo el
resto entero, comprobo que no deja ni un acto fuera y lo declaro como **TRAMO CORTO POR AGOTAMIENTO,
PENDIENTE DE DOCTRINA**. Va como pregunta 1 al auditor.

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `eda42bc2` (el commit del acta 60), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** (`git status --porcelain` VACIO, comprobado) |
| **hash final** | **`ccf2832b`** mas el commit de este reporte, **pusheados a `origin/pasada-unica`** |
| **commits de la vuelta** | **4** antes de este, leidos de `git log --format=%h eda42bc2..HEAD`: `027606a6` (apertura medida), `789564f8` (TAREA 1, los 35 AMBAR), `32d6fcf3` (TAREA 2.1, el abridor estable y el tramo 6), `ccf2832b` (TAREA 2.2, varas, dossier, colisiones y el contrato de perdidas), **mas este** |
| **arbol al cierre** | limpio tras este commit |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1)

**NINGUNA CELDA ESTA TECLEADA:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 61`
([`SALIDA_V61_TALLAR_CABECERA.txt`](SALIDA_V61_TALLAR_CABECERA.txt)). **Las dos columnas se leen de
ficheros DISTINTOS.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.295 / 558 / 17.449 | **3.853 / 3.295 / 558 / 17.449** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 254 / 297 | **551 / 254 / 297** |
| actos (componentes) | 103 | **103** |
| actos `CERRADOS` / `ABIERTOS` | 50 / 53 | **50 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 109 / 240 | **109 / 240** |
| cola de costuras | 1.460 | **1.460** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 232 | **232** |
| duplicadas historicas: grupos / nodos | 935 / 741 | **935 / 741** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (349 igual a 349; 297 igual a 297) | **TODAS OK (349 igual a 349; 297 igual a 297)** |

**LAS DOS COLUMNAS SON IGUALES EN LAS CATORCE FILAS, Y ESO NO SE PUBLICA COMO SI FUERA SOLO,** porque
es exactamente la forma que tenia la caida de la vuelta 56 (heredar el lado de enfrente). **El propio
tallador lo avisa** al pie de su salida. Lo que lo sostiene aqui: **esta vuelta no toco ni un nodo**
(la fase de ejecucion no abrio ningun lote), y las dos columnas se leen de **ficheros distintos**,
`SALIDA_V61_*_APERTURA.txt` y `SALIDA_V61_*_CIERRE.txt`, medidos con **horas** distintas.

**LA APERTURA CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 60 MIDIO POR CORRIDA PROPIA**, y eso es
contraste, no fuente. Instrumentos de apertura corridos **ANTES de la primera operacion**:
[`SALIDA_V61_APERTURA.txt`](SALIDA_V61_APERTURA.txt),
[`SALIDA_V61_MARCADOR_APERTURA.txt`](SALIDA_V61_MARCADOR_APERTURA.txt),
[`SALIDA_V61_RECOMPUTO_APERTURA.txt`](SALIDA_V61_RECOMPUTO_APERTURA.txt),
[`SALIDA_V61_COLA_APERTURA.txt`](SALIDA_V61_COLA_APERTURA.txt),
[`SALIDA_V61_COLISIONES_APERTURA.txt`](SALIDA_V61_COLISIONES_APERTURA.txt) y
[`SALIDA_V61_DUPLICADAS_APERTURA.txt`](SALIDA_V61_DUPLICADAS_APERTURA.txt).

**LA MEDICION DE CIERRE SE RE-CORRIO DESPUES DEL `Gate 0` Y DEL CICLO DE TRES**, por si aquello movia
algo, y **las seis salidas dan `diff` VACIO** contra las publicadas (la del recomputo difiere en **una
sola linea**, la que imprime la ruta de su propio `--salida`, y se dice en vez de llamarla vacia).

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V61_MARCADOR_CIERRE.txt`](SALIDA_V61_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) | franquicias
10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0 (n 106) |
seguridad_digital 11,1 (n 27). **IDENTICA a la de la apertura al digito, y el motivo es el mismo: no
se fundio nada.**

---

## 1. TAREA 1: **LOS 35 `AMBAR`, TRIADOS, Y EL VEREDICTO ESCRITO DONDE LA MAQUINA LO VUELVE A MIRAR**

El barrido dice de cada `AMBAR`, con todas sus letras, que **NO LO DECIDE**. El triage es donde el ojo
escribe lo que leyo. **Lo que esta vuelta anade es que no lo escribe en un papel aparte: lo escribe
DENTRO del fichero, en una forma que el barrido COTEJA EN CADA CORRIDA.**

### 1.1 El instrumento y sus guardas

Nace **`scripts/loop/triage_ambar_titulos.py`**, de **nombre estable**
([`SALIDA_V61_TRIAGE_AMBAR.txt`](SALIDA_V61_TRIAGE_AMBAR.txt)). **Sus guardas corren ANTES de escribir
un solo byte**, y las dos primeras son la vara entera:

| guarda | que hace | medido hoy |
|---|---|---|
| **la tabla contra el barrido de HOY** | si una fila dice triar algo que hoy no es un `AMBAR` vivo alli, **ROJO y CERO escrituras** | **35 de 35 cubiertas** |
| **la cuenta cuadra o no se escribe** | si el barrido trae un `AMBAR` que la tabla no tria, **ROJO** | **ni uno de sobra ni uno de menos** |
| **la vuelta de la cita envejecida, por DOS relojes** | `git log --diff-filter=A` y el nombre del fichero | **56 y 56: COINCIDEN** |
| **idempotencia** | segunda corrida | **`YA ESTA`, 0 escrituras, exit 0** |

### 1.2 El reparto: **35 menciones, y solo UNA era una cita envejecida**

| veredicto | claves | menciones | que es |
|---|---:|---:|---|
| **`SELLO_FIJO`** | **10** | **17** | el numero nombra el **sujeto FIJO del propio instrumento** (el registro del tramo 2, el deshacer del acto 32 del tramo 4). Salio `AMBAR` porque el **nombre** del fichero no lleva el tramo y la maquina no tenia con que cotejarlo |
| **`PROCEDENCIA`** | **15** | **17** | el numero **nombra un ancestro a proposito**: el acta de otra vuelta, la propuesta de la 35, el instrumento del que se copio la aritmetica |
| **`ENVEJECIDA`** | **1** | **1** | `vuelta56_varas_tramo3.py` |

### 1.3 **EL ROTULO NO ES UN SILENCIADOR: ES UNA DECLARACION CON GUARDA**

Es la via del `vigente=` de la vuelta 58 traida a esta especie. **Cada rotulo se COTEJA en cada
corrida del barrido y el barrido prefiere `ROJO` a callar:**

- **`SELLO_FIJO`** se coteja contra el numero tallado **y contra que el fichero NO reciba esa especie
  por argumento**. **Un instrumento repuntable NO se puede sellar con este rotulo**, y eso es lo que
  impide que el rotulo sea una excusa.
- **`PROCEDENCIA`** se coteja contra la **fuente citada**, que tiene que **existir** y **contener el
  literal de prueba**. Si el ancestro desaparece o se renombra, `ROJO`.
- **Un rotulo que no casa con ningun `AMBAR` vivo es `ROJO` por huerfano**, para que no quede de
  adorno cuando el titulo que cubria ya se corrigio.

**Y ESTO NO SE AFIRMA, SE PROBO SEMBRANDO TRES AVERIAS**
([`SALIDA_V61_CASO_POSITIVO_ROTULO.txt`](SALIDA_V61_CASO_POSITIVO_ROTULO.txt)):

| averia sembrada | lo que hizo el barrido | restaurada |
|---|---|---|
| el literal de prueba deja de existir en la fuente | **`ROJO` nombrando el literal y el fichero**, y `ROJO` sube de 32 a **33** | `git checkout` |
| se le anade `--tramo` a un fichero con `SELLO_FIJO` | el titulo pasa a **`ROJO`** por la via normal **y el rotulo se va a huerfano**: las dos a la vez | `git checkout` |
| el rotulo declara `tramo:9` y el titulo dice `TRAMO 1` | **rotulo huerfano `ROJO`** y el `AMBAR` **vuelve a salir** | `git checkout` |

**El arbol quedo limpio tras las tres restauraciones, comprobado por `git status`.**

### 1.4 **LA UNICA CITA ENVEJECIDA, CORREGIDA CON EL TEXTO VIEJO CITADO**

`scripts/loop/vuelta56_varas_tramo3.py` imprimia
`EL CUADRO DE VARAS DE LOS %d ACTOS DEL TRAMO 3 (vuelta 54)`. El `(vuelta 54)` **venia del ancestro
`vuelta54_varas_tramo2.py`, donde SI es verdad** (ahi el fichero es de la vuelta 54). **Este fichero
nacio en la vuelta 56**, y eso **no se tecleo**: se mide con `git log --diff-filter=A`, commit
`2743bd88`, asunto *VUELTA 56, LOTE A DEL TRAMO 3*. La correccion queda con **nota fechada y el texto
viejo citado entero**, y la nota dice ademas lo que **no** se toco:

> **EL `TRAMO 3` DE ESTA MISMA LINEA NO SE TOCA: es un `ROJO` del barrido y esta vuelta no paga
> `ROJO`.**

### 1.5 **EL BARRIDO RE-CORRIDO, CON SU RESUMEN ENTERO**

```
RESUMEN: 380 ficheros barridos, 184 con hallazgo, 196 limpios | ROJO 32, AMBAR 0, ROTULADO 34, CENSO 214, ILEGIBLE 1
```

([`SALIDA_V61_BARRIDO_TRAS_TRIAGE.txt`](SALIDA_V61_BARRIDO_TRAS_TRIAGE.txt) es el de la TAREA 1, con
377 ficheros; el de arriba es el del cierre, con los tres instrumentos nuevos de la TAREA 2 ya
dentro.) **Contra la apertura** ([`SALIDA_V61_BARRIDO_APERTURA.txt`](SALIDA_V61_BARRIDO_APERTURA.txt),
`376 ficheros, 184 con hallazgo, 192 limpios | ROJO 32, AMBAR 35, CENSO 213, ILEGIBLE 1`):

| celda | apertura | cierre | por que se movio, medido |
|---|---:|---:|---|
| **`AMBAR`** | **35** | **0** | 34 rotulados y 1 corregido |
| **`ROTULADO`** | (no existia) | **34** | los 34 que quedaron con rotulo cotejado |
| **`ROJO`** | **32** | **32** | **SON LOS MISMOS, comprobado por `diff` linea a linea**: solo cambian numeros de linea porque los rotulos insertados empujaron el codigo hacia abajo. **Ni uno pagado, ni uno nuevo** |
| **`CENSO`** | **213** | **214** | la cita corregida, que ahora **calza** con el fichero |
| **ficheros** | **376** | **380** | los cuatro instrumentos nuevos de esta vuelta, **y ninguno sale con hallazgo** |

**Y NADA DE ESTO SE PUBLICA SIN CONTRASTE.** Antes de escribir **ni un rotulo**, el barrido
**extendido** se corrio sobre el arbol **sin un solo rotulo**
([`SALIDA_V61_BARRIDO_CONTRASTE_SIN_ROTULOS.txt`](SALIDA_V61_BARRIDO_CONTRASTE_SIN_ROTULOS.txt)) y dio
`376 / 184 / 192, ROJO 32, AMBAR 35, CENSO 213, ILEGIBLE 1`, **identico linea a linea al barrido
viejo** salvo la fila nueva del resumen. Es la cuarta condicion del `D7` de la vuelta 60 aplicada a mi
mismo: **quien cambia el instrumento que va a contar sus cifras contrasta contra la cifra ya
publicada.**

---

## 2. TAREA 2: **LA APERTURA DEL TRAMO 6**

### 2.1 **EL ABRIDOR NACE ESTABLE, Y AHI MUERE LA CADENA DE CLONES**

Nace **`scripts/loop/abrir_tramo_de_opu01.py`**: **sin numero de tramo ni de vuelta en el nombre, en
el titulo ni en el codigo**. Es la deuda del **acta 58 pregunta 4** y la que el reporte 60 volvio a
nombrar (`vuelta58_tramo5_nomina.py` sigue en el `ROJO` **con cuatro menciones**, y **ahi se queda**:
esta vuelta no paga `ROJO`).

**ES COPIA BYTE A BYTE DEL ANCESTRO** (`sha1 7d70bcfbc56a`, medido) y solo despues se le cambio lo que
su docstring enumera. **El ancestro queda intacto y re-corrible**, que es la via del acta 54 pregunta
3. **EL BARRIDO DA EL FICHERO NUEVO LIMPIO: no sale en `ROJO`, ni en `AMBAR`, ni en `CENSO`.**

| lo que cambia | de que a que | es aritmetica? |
|---|---|---|
| el tramo | constante `TRAMO = 5` **a** medido del censo de `TRAMO<N>_V<vuelta>.jsonl`, o `--tramo-numero` | **no** |
| los tramos previos | tres constantes tecleadas **a** descubiertos del mismo censo | **no** |
| tramo con varios ficheros | (no existia) **a** **manda el de la vuelta MAS BAJA**, la del dia en que se abrio, y **los descartados se imprimen con su nombre** | **no** |
| la clave del ordinal | `orden_tramo5` tallado **a** armado del numero medido | **no** |
| los titulos | **a** `%d` alimentado de lo medido, que es la via VERDE del barrido | **no** |
| **la guarda de solape** | `(1, 2, 3)` tallado **a** **TODOS los previos** | **SI, Y VA COMO DISCUTIBLE `D2`** |

**LA GUARDA QUE CRECE SE DICE ENTERA:** el ancestro miraba `(1, 2, 3)` escrito a mano, asi que **al
abrir el tramo 5 se dejo fuera el tramo 4**. Una guarda que crece **no es copia**, y por eso va
marcada.

**LA REGLA DEL FICHERO DE APERTURA NACIO DE UN `ROJO` PROPIO Y SE DICTA CON LAS DOS MITADES:** la
primera version **cayo en `ROJO` sin abrir el tramo** porque `TRAMO2_V54.jsonl` y `TRAMO2_V55.jsonl`
reclaman los dos el tramo 2; **y quedo arreglada** midiendo la regla que el ancestro llevaba escrita a
mano (aquel apuntaba al `V54`), o sea **manda la vuelta mas baja**, con el descartado impreso por su
nombre.

### 2.2 **EL HALLAZGO: `OP-U-01` SE ESTA ACABANDO, Y EL TRAMO 6 ES CORTO**

**Medido** ([`SALIDA_V61_TRAMO6_ABIERTO.txt`](SALIDA_V61_TRAMO6_ABIERTO.txt)):

| | |
|---|---:|
| actos `CERRADOS` hoy | **50** |
| de esos, **VIVOS de los tramos 1 a 5** (los declarados que no se fundieron) | **29** |
| **libres para el tramo 6** | **21** |
| lo que la vara pide | **50** |

**VERIFICADO POR CORRIDA APARTE E INDEPENDIENTE**, no por creerle al abridor: los `CERRADOS` de hoy
fuera de los tramos 1 a 5 son **21**, y los `CERRADOS` de la nomina de la 48 fuera de ellos son
**21** tambien.

**EL ABRIDOR NO RECORTO, NO RELLENO Y NO CALLO.** Se llevo el resto entero, **comprobo que no deja ni
un acto fuera** (21 tomados de 21) y lo imprimio en un bloque propio:

> **ESO ES AGOTARSE, NO TRUNCAR, y son cosas distintas: truncar deja actos detras del corte y
> agotarse no deja ninguno. ESTE ABRIDOR NO ADJUDICA si un tramo corto es tramo: MIDE Y DECLARA.**

Va como **`PENDIENTE DE DOCTRINA`** y como **pregunta 1** al auditor.

### 2.3 **EL INSUMO DEL TRAMO 6, FIJADO, CON SUS CUATRO PIEZAS Y SUS GUARDAS**

| pieza | instrumento | salida | lo medido |
|---|---|---|---|
| **nomina fijada** | `abrir_tramo_de_opu01.py` | [`TRAMO6_V61.jsonl`](TRAMO6_V61.jsonl) mas [`SALIDA_V61_TRAMO6_ABIERTO.txt`](SALIDA_V61_TRAMO6_ABIERTO.txt) | **21 actos**, puestos de hoy **30 a 50** y de la 48 **250 a 270** |
| **cuadro de varas de los 50** (aqui, de los 21) | `vuelta58_varas_tramo.py`, ya de nombre estable | [`SALIDA_V61_VARAS_TRAMO6.txt`](SALIDA_V61_VARAS_TRAMO6.txt) | pasos, condiciones, cableado, forma y puertas, una fila por acto |
| **dossier de razones enteras** (P.5) | **`dossier_del_tramo.py`**, nuevo | [`SALIDA_V61_DOSSIER_TRAMO6.txt`](SALIDA_V61_DOSSIER_TRAMO6.txt) | **848 lineas**, los **21** actos leidos enteros, 256 ids del universo protegido |
| **colisiones esperadas del tramo entero** | `vuelta56_colisiones_esperadas.py` | [`SALIDA_V61_COLISIONES_ESPERADAS_TRAMO6.txt`](SALIDA_V61_COLISIONES_ESPERADAS_TRAMO6.txt) | **42 combinaciones simuladas por par resuelto, CERO que fabriquen colision** |

**LAS GUARDAS DE LA APERTURA, TODAS MEDIDAS Y NINGUNA AFIRMADA:**

| guarda | resultado |
|---|---|
| **las dos lecturas** (orden de hoy contra orden de la 48) | **CALZAN, mismo conjunto y mismo orden. CERO divergencias** |
| **prefijo** | **29 vivos en los puestos 1 a 29, SIN HUECOS** |
| **cuatro ajenos, CAMINO 1 (literal)** | **VERDE, ninguno entra** |
| **cuatro ajenos, CAMINO 2 (por el resolutor, P.1)** | **VERDE**, y muerde donde hay que mirar: `brainstorming_divergente` esta deprecado y resuelve a `reglas_brainstorming`, **que tampoco entra** |
| **solape con los tramos 1 a 5** | **CERO** |
| **el tramo 2 contra su bloque 51 a 100 de la 48** | **sigue calzando** |
| **el tramo 3 contra su bloque** | **sigue sin calzar**, con el mismo acto de mas y el mismo de menos que la vuelta 56 midio |
| **figura y tamano** | **los 21 son de FUSION PURA: tamano 2 y `PURO A`. Ni uno mixto** |
| **modo de continuacion `--fijado`** | re-mide el tramo 6: **21 vivos, 0 fundidos** |
| **contraste del propio abridor** | la corrida con `--tramo-numero 6` da una nomina **IDENTICA por `diff`** a la del tramo medido |

**EL CUADRO DE VARAS, POR FORMA** (leido de la salida, no contado a ojo):

| forma | cuantos |
|---|---:|
| **UNA SOLA VARA** de contenido no empatada | **12** |
| **TODAS LAS VARAS de contenido de acuerdo** | **5** |
| **EL CONTENIDO EMPATA** y decide el cableado | **4** |
| **suma** | **21** |

**NI UN `CHOCAN` Y NI UN `EMPATE SIN VARA`.** Es, por forma, **el tramo mas limpio de la campana**, y
es justo lo contrario de lo que la mesa acumula: **los quince actos de la mesa no crecen con este
tramo**, al menos por lo que el cuadro imprime hoy.

### 2.4 **LA PERDIDA SELLADA EN CAMPO PROPIO: EL CONTRATO Y SU TALLADOR**

Es el **pendiente de instrumento del acta 60**: el tallador viejo **solo ve las perdidas con el token
en la prosa**, y en los lotes B y C del tramo 5 hubo **cuatro sin el**. Nace
**`scripts/loop/tallar_perdidas_del_plan.py`**, de nombre estable. **El ancestro no se toca**: sigue
entero y sus cifras siguen citadas por los registros de los tramos 3, 4 y 5.

**EL CONTRATO, decidido por el instrumento y escrito en su docstring** (que es lo que el encargo pide
declarar):

```
raiz del plan:  "contrato_de_perdidas": "CAMPO PROPIO v1"
cada acto:      "perdidas": [ {especie, que, donde, enrutada_a}, ... ]   SIEMPRE, aunque vacia
especies:       DE PARAMETRO DE PASO | DE CONDICIONES | DE NOMBRE   (y solo esas)
```

**LA MITAD UTIL DEL CONTRATO ES LA DISTINCION QUE LA PROSA NO SABIA HACER:**

> **LISTA VACIA es una DECLARACION de cero perdidas. CAMPO AUSENTE es que el plan NO LO DICE, y eso es
> `ROJO`.**

**Y LA GUARDA QUE HACE FIABLE AL CAMPO ES EL CRUCE CONTRA LA PROSA:** token suelto en una frase que no
dice que se repone, con el campo vacio, es **`ROJO`**; **al reves NO**, porque una perdida en el campo
**sin** token en la prosa es **el caso bueno**, el que el ancestro no veia. Es el motivo entero del
contrato.

**PROBADO CON SEIS PLANES DE PRUEBA, UNO POR GUARDA**
([`SALIDA_V61_CASO_POSITIVO_PERDIDAS.txt`](SALIDA_V61_CASO_POSITIVO_PERDIDAS.txt)):

| plan de prueba | esperado | medido |
|---|---|---|
| bueno (una perdida y una lista vacia) | talla | **tabla emitida, 1 perdida, exit 0** |
| campo ausente con contrato declarado | `ROJO` | **`ROJO`, sin tabla, exit 1** |
| especie desconocida (`DE COLOR`) | `ROJO` | **`ROJO`, sin tabla, exit 1** |
| prosa con token y campo vacio | `ROJO` | **`ROJO`, sin tabla, exit 1** |
| token en frase que dice `SE REPONE`, campo vacio | **NO** es rojo | **0 perdidas, exit 0** |
| plan sin contrato leido por campo | `ROJO` | **`ROJO`, exit 1** |
| `--por-token` sobre un plan que **SI** declara el contrato | `ROJO` | **`ROJO`: el modo no se elige en silencio** |

**CONTRASTE CONTRA LA CIFRA YA PUBLICADA:** el modo heredado sobre los lotes B y C del tramo 5 da **1
perdida sobre 31 actos**, que es **la cifra que el registro del tramo 5 publico**.

---

## 3. `Gate 0`, EL CICLO DE TRES Y LAS SUITES

| | |
|---|---|
| `Gate 0` (`python scripts/run_phase1.py --reaplico-curaduria`) | **`GATE 0: OK`**, simetrizacion **0 nodos** |
| `etiquetas_de_cara.py --aplicar` | **71 etiquetas re-aplicadas** |
| `sync_assets_web.py` | **6 assets sincronizados**, manifest escrito |
| **arbol tras el ciclo de tres** | **LIMPIO**, `git status` sin un rastreado modificado |
| suite del motor | **25 de 25** |
| suite web | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| `tsc --noEmit` | **CERO lineas** |

**EL `Gate 0` DEJO EL ARBOL SUCIO A MEDIO CAMINO Y SE DICTA CON LAS DOS MITADES:** corrido solo,
`run_phase1.py` recompila `master_graph.json` **desde los nodos** y **revierte 71 `etiqueta_arbol` a
su forma cruda** (`Canvas` donde el grafo publicado dice `Mapa`); **y quedo arreglado** al correr el
**ciclo de tres entero**, que es lo que la vuelta 60 ya dejo escrito: `etiquetas_de_cara --aplicar`
las repone las 71 y el arbol cierra limpio. **No es una averia nueva: es que el ciclo va entero o no
va.**

---

## 4. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| | que hice | por que se puede discutir |
|---|---|---|
| **D1** | **ABRI EL TRAMO 6 CON 21 ACTOS** cuando la vara pide 50, en vez de parar | El abridor mide, declara y sigue; yo elegi que un tramo corto **por agotamiento** es tramo. **Ninguna regla escrita lo dice.** Lo sostengo con la regla 5 del `EJECUTOR` (lo que ninguna regla cubre no para: se registra lo mejor sostenido y se marca `PENDIENTE DE DOCTRINA`) y con que **no queda ni un acto fuera**; pero un lector estricto dira que **la vara dice CINCUENTA** y que abrir un tramo con menos es estrenar clase |
| **D2** | **AMPLIE LA GUARDA DE SOLAPE** del abridor de `(1, 2, 3)` a **todos los tramos previos** | Es el **unico** cambio del abridor que **no es copia**: una guarda que crece cambia lo comprobado. Lo sostengo porque el ancestro se dejaba fuera el tramo 4 **por tenerlo tallado a mano**, que es la misma especie que toda esta vuelta persigue; pero **cambia el resultado posible** de una corrida del ancestro y por eso no se cuela como copia. **Que no cambiara aquella corrida es consecuencia, no excusa**, y no lo uso de argumento |
| **D3** | **EL ROTULO `SELLO_FIJO` ES UNA AUTODECLARACION** del fichero sobre cual es su sujeto | Un rotulo que el propio fichero se pone puede leerse como **permiso para silenciar un `AMBAR`**. Lo sostengo porque la maquina **no acepta la palabra sola**: comprueba que el fichero **no reciba esa especie por argumento**, que es exactamente lo que separa `ROJO` de `CENSO` en el barrido vigente, y lo probe sembrando el argumento (seccion 1.3). Aun asi, **es la primera vez que un fichero declara su propio sujeto y el barrido le cree** |
| **D4** | **EXTENDI EL BARRIDO** (el instrumento que cuenta la cifra que publico) **en la misma vuelta en que publico su cifra** | Es literalmente el `D7` de la vuelta 60. Lo hice con **las cuatro condiciones que aquel dejo adjudicadas**: cambio medido, **contraste contra la cifra publicada re-corrido antes de escribir nada** (seccion 1.5), guarda que prefiere `ROJO` a callar, y el estado final dictado exacto. Pero **sigue siendo cambiar la balanza el dia que me peso** |
| **D5** | **ESCRIBI DOS SUCESORES** (`dossier_del_tramo.py` y `tallar_perdidas_del_plan.py`) que el encargo **no pidio** | El encargo pide el **abridor** estable, no estos dos. Lo sostengo porque correr los ancestros habria publicado salidas con el **titulo mintiendo** (`vuelta56_dossier_tramo3.py` es `ROJO` con `--tramo`), que es la especie que la racha de la cabecera ya pago tres veces; y porque **un sucesor no paga el `ROJO` del ancestro**, que sigue en la lista de 32. Pero **son dos ficheros de mas** en una vuelta que ya trae tres |
| **D6** | **EXCLUI DEL COTEJO DE ROTULOS a los dos ficheros que hablan su gramatica** (el barrido y el triador) | Es una excepcion escrita a mano en el instrumento, y una excepcion es una puerta. Lo sostengo con **las dos mediciones que la levantaron**: el barrido leia **sus propios dos ejemplos** del docstring como rotulos y publico **dos huerfanos que no existen**, y al vaciar las lineas de rotulo del triador (que las **arma**) lo dejo **`ILEGIBLE`**. La excepcion es **de rotulos y de nada mas**: los dos ficheros se siguen barriendo enteros por sus titulos. Pero **un instrumento que se excluye a si mismo de su propia vara pide que lo miren** |
| **D7** | **DEJE EL LOTE A SIN EJECUTAR** | El encargo lo permite (`acta 58 pregunta 6`) y mando decirlo primero, y lo digo primero. Pero **la vuelta cierra sin haber fundido ni un acto**, y quien mida la campana por actos fundidos vera una vuelta en cero. Lo sostengo con lo que la apertura destapo: **el tramo es corto y eso es doctrina pendiente**, y fundir 21 actos bajo una vara que no los cubre habria sido decidir en silencio lo que el `D1` trae a la mesa |

---

## 5. PENDIENTES DE DOCTRINA

- **NUEVO, Y ES EL DE ESTA VUELTA: EL TRAMO CORTO POR AGOTAMIENTO.** La vara del registro del tramo 1
  dice **los CINCUENTA primeros actos `CERRADOS`**. Quedan **21**. **No propongo regla**: propongo que
  la mesa decida si un tramo corto por agotamiento es un tramo, si el ultimo tramo se declara **cierre
  de `OP-U-01`** en vez de tramo, o si los 29 vivos de los tramos 1 a 5 (los declarados) entran de
  algun modo en el reparto final. **La cifra 21 esta medida por dos caminos y no cambia con la
  decision.**
- **1, PARA LA MESA, con QUINCE actos:** heredado sin cambio. **El tramo 6 no le anade ni uno** por lo
  que el cuadro imprime hoy: **ni un `CHOCAN` y ni un `EMPATE SIN VARA`** en los 21.
- **2 (`INCISO`), 3, 4, 5 y 7: HEREDADOS SIN CAMBIO.** No se pagan hoy.
- **EL DE LA SERIE DEL TITULO** (la perdida de nombre que vive solo en el `titulo_concepto`, tres
  ejemplares): **HEREDADO Y EN LA MESA**, sin ejemplar nuevo esta vuelta.
- **PAGADO Y CERRADO, y se dice porque estaba en esta lista:** el **pendiente de instrumento** del
  tallador de perdidas. Ya no es pendiente: es contrato con guarda y caso positivo (seccion 2.4).
- **PAGADO Y CERRADO:** los **35 `AMBAR`** dejan de estar en cola. **`AMBAR 0`.**

---

## 6. PREGUNTAS PARA EL AUDITOR

1. **UN TRAMO CORTO POR AGOTAMIENTO ES UN TRAMO?** (`D1`.) Quedan 21 donde la vara pide 50, y no queda
   ni uno fuera. Si la respuesta es no, **que es**: cierre de `OP-U-01`, o tramo con otra vara.
2. **UNA GUARDA PUEDE CRECER DENTRO DE UN SUCESOR DECLARADO?** (`D2`.) El contrato del sucesor es
   *copia byte a byte y solo despues lo declarado*, y lo declarado aqui **amplia lo comprobado** en vez
   de solo reformularlo.
3. **UN FICHERO PUEDE DECLARAR SU PROPIO SUJETO Y QUE EL BARRIDO LE CREA?** (`D3`.) La guarda es que no
   reciba esa especie por argumento. **Basta esa guarda, o un `SELLO_FIJO` deberia exigir tambien una
   fuente externa como la `PROCEDENCIA`?**
4. **LOS 29 ACTOS VIVOS DE LOS TRAMOS 1 A 5 (los declarados) QUE SON AHORA?** Ocupan los puestos 1 a 29
   del orden de hoy y **no son de ningun tramo por abrir**. La mesa tiene quince de ellos; **los otros
   catorce no se han vuelto a nombrar** y esta vuelta no los toco.
5. **UN SUCESOR ESCRITO SOLO PARA NO PUBLICAR UN TITULO QUE MIENTE ESTA JUSTIFICADO?** (`D5`.) La
   alternativa era correr el ancestro `ROJO` y declarar la mentira en el reporte.

---

## 7. MIS PROPIOS MANEJOS Y TROPIEZOS, declarados

**Los cuatro `ROJO` propios de esta vuelta, cada uno dictado con las DOS mitades, cayo Y como quedo:**

- **EL BARRIDO SE LEYO A SI MISMO EL MANUAL Y PUBLICO DOS HUERFANOS QUE NO EXISTEN;** y **quedo
  arreglado** excluyendo del cotejo de rotulos a los dos ficheros que hablan la gramatica, con las dos
  mediciones escritas dentro del codigo. Es la piedra que `_v50_contraste_contar_ld_v49` ya dejo
  escrita: **un instrumento que se lee a si mismo se da la razon solo.**
- **AL VACIAR LAS LINEAS DE ROTULO DEJE `ILEGIBLE` AL TRIADOR** (`unmatched ')'`, linea 198), porque
  ese fichero **arma** las lineas de rotulo; y **quedo arreglado** con la misma exclusion. **Lo cazo
  la corrida siguiente del barrido, no una lectura.**
- **LAS LINEAS DE ROTULO SE VACIAN Y NO SE QUITAN,** y esto lo vi **antes** de que mordiera: quitarlas
  habria corrido hacia arriba **el numero de linea que el propio barrido publica**. Queda escrito
  dentro de `sin_rotulos` con su motivo.
- **EL ABRIDOR CAYO EN `ROJO` SIN ABRIR EL TRAMO** porque dos ficheros reclaman el tramo 2; **y quedo
  arreglado** midiendo la regla que el ancestro llevaba tallada (manda la vuelta mas baja), con el
  descartado impreso por su nombre. **La guarda funciono sobre mi diseno, no sobre los datos.**
- **LA IDEMPOTENCIA DEL TRIADOR CAYO EN `ROJO` LA PRIMERA VEZ** por una pregunta mal hecha: pregunte
  si el texto viejo habia desaparecido, cuando **la doctrina manda citarlo y no borrarlo**, asi que
  siempre sigue ahi; **y quedo arreglada** preguntando por la **nota** de la correccion. El
  razonamiento equivocado queda escrito dentro del propio instrumento.
- **BUSQUE `run_phase1.py` EN LA RAIZ Y ESTA EN `scripts/`.** Costo una corrida, cero cifras.
- **CORRI `recomputo_3388.py` APUNTANDO A `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`** y le quito
  **229 lineas** a un fichero publicado. **Lo restaure con `git checkout` y lo re-corri contra una
  salida propia**, y lo digo porque **restaurar un fichero rastreado es un acto y no un accidente**.
- **DEJE `phase1_run_log.json` CON EL LOG DE MI CORRIDA** tras el `Gate 0` y lo restaure a su estado
  committeado, por lo mismo.

---

## 8. LO QUE QUEDA, DICHO SIN ADORNO

**EL TRAMO 6 ESTA ABIERTO, FIJADO Y CON SU INSUMO ENTERO:** nomina de 21, cuadro de varas, dossier de
848 lineas y colisiones esperadas en cero. **Todas las guardas de la apertura en verde.** **EL LOTE A
NO SE EJECUTO** y esta dicho en la primera linea. **Los 35 `AMBAR` estan pagados y el barrido dice
`AMBAR 0`.** **Los 32 `ROJO` siguen siendo los mismos 32**, comprobado linea a linea. **La cadena de
clones del abridor murio**, y con ella el motivo por el que `vuelta58_tramo5_nomina.py` seguia siendo
la unica via de abrir un tramo. **El pendiente del tallador de perdidas esta pagado con contrato,
guarda y caso positivo.** **NINGUN NODO SE TOCO.** **Y la campana tiene por delante una pregunta que
esta vuelta destapo y no contesta: `OP-U-01` tiene 21 actos de vida, no 50.**
