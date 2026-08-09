# La deuda de `RE_CIFRA`: ACTA de los casos grises y su adjudicacion

> **Este documento es un ACTA, no un archivo.** El paro se resolvio: cada
> pregunta lleva su adjudicacion al lado, y la construccion esta hecha.

**La tarea 2 se detuvo a proposito.** El encargo lo dijo: *"si al construirlo
descubres que la frontera entre numeral y palabra de orden es mas fina de lo que
estos ejemplos sugieren, PARAS y traes los casos grises en vez de decidir el
limite solo"*.

**Lo es.** Y no por poco.

---

## El origen

`RE_CIFRA` en `scripts/revoz_pack.py` y `scripts/consolidar_pack.py` es
`\d+(?:[.,]\d+)?`: **solo digitos**. En la cirugia 1, un peldano volvio con
*"no es lo mismo un veinte por ciento que un cuarenta y cinco"*, un ejemplo
**inventado** que la baranda no vio. Se quito a mano.

---

## Lo que encontre mirando el catalogo real

No parti de ejemplos de laboratorio: busque cada palabra candidata en los 3.521
nodos activos. **Casi todas viven en el catalogo con dos sentidos distintos, y
uno de ellos no es una cifra.**

### 1. Compuestos donde la palabra nombra una COSA, no una cantidad

- *"cajas de **doble** pared"* y *"usa caja de **doble** pared"*: `doble pared`
  es **un tipo de caja**, una especificacion de material. No es un multiplicador.
- *"**numero par de** miembros divididos equitativamente"*: `par` aqui es
  **paridad**, lo contrario de impar. No es *"un par de"*.
- *"el metodo **MIL**-STD-105D"*: `MIL` dentro del **nombre propio** de una
  norma.

### 2. Modismos que no cuentan nada

- *"resolver **de una vez** los problemas"*: significa *definitivamente*, no
  *una sola vez*.
- *"nunca permitir que el mismo error se cometa **dos veces**"*: enfasis, no un
  conteo.

Y sin embargo *"imprimir la etiqueta de envio **dos veces**"* **si** es un
conteo real, en el mismo catalogo.

### 3. La misma palabra, fraccion en un sitio y posicion en otro

- *"mostrando la version A a la **mitad** de los visitantes"*: **fraccion real**.
- *"hablar de tu producto en la primera **mitad** de la llamada"*: **posicion**.

Igual con `cuarto`: *"un **cuarto** paso critico"* (posicion) contra *"pasar de
**cuarto** a segundo cuartil"* (posicion tambien, pero de un ranking) contra un
hipotetico *"un cuarto de tus clientes"* (fraccion).

### 4. Los ordinales son sobre todo marcadores de discurso

*"**Segundo** punto de Deming"*, *"**Tercero**, en el anillo interior"*,
*"ataca **primero** los mas grandes"*. **No son cifras**: ordenan el texto.

Pero *"es el **segundo** paso de la contabilidad de la innovacion"* si designa
una posicion real en una secuencia.

### 5. Los numerales sueltos son articulos la mayor parte del tiempo

*"**una** solucion rapida"*, *"comparar **dos** versiones"*, *"existen **tres**
tipos"*. En espanol `un`, `una` son **articulos**, y `dos`, `tres` son
cuantificadores genericos.

---

## El radio de explosion, medido

| patron ingenuo | nodos que caza | del catalogo |
|---|---:|---:|
| numerales sueltos (uno, dos, tres...) | **2.488** | **70,7%** |
| ordinales (primero, segundo...) | 440 | 12,5% |
| frecuencia (una vez, dos veces) | 121 | 3,4% |
| multiplicadores (doble, triple, par de) | 56 | 1,6% |
| decenas y mas (veinte, cien, mil) | 48 | 1,4% |
| fracciones (mitad, tercio) | 33 | 0,9% |
| **porcentaje escrito (X por ciento)** | **8** | **0,2%** |

**Un detector de numerales sueltos marcaria siete de cada diez nodos.** Eso no es
una baranda: es ruido que se acaba desactivando, y esta casa ya tiene la doctrina
escrita de que **una baranda que caza lo correcto no es estricta, esta rota**.

---

## Lo unico que puedo afirmar sin adjudicacion

**El caso que origino la deuda es el mas estrecho de todos y el mas seguro**: el
patron `<numeral> por ciento` caza **8 nodos** en todo el catalogo, y los ocho
que mire son porcentajes de verdad. Ahi no hay frontera fina.

**Las preguntas que traigo**, y que no decido:

1. **Alcance**: ¿el detector se limita a `<numeral> por ciento` y a las decenas
   grandes (`veinte`, `cincuenta`, `cien`, `mil`), que son las que un modelo
   inventa cuando quiere ilustrar? ¿O se intenta cubrir fracciones y frecuencias
   asumiendo falsos positivos?
2. **La regla del contexto**: ¿se acepta que el detector mire **lo que sigue** a
   la palabra (`por ciento`, `de tus`, `veces al`) en vez de la palabra sola? Eso
   reduce el ruido, pero es mas fragil ante una redaccion nueva.
3. **Que hace al cazar**: en `RE_CIFRA` una cifra nueva **rechaza el nodo**. Con
   estas palabras, ¿rechaza tambien, o solo **avisa** para que un ojo mire? Un
   rechazo con 2 por ciento de falsos positivos sobre 3.500 nodos son 70 nodos
   buenos bloqueados.
4. **Los cinco compuestos** que documente arriba (`doble pared`, `numero par`,
   `de una vez`, `primera mitad`, `MIL-STD`): ¿entran como exenciones fijas al
   registro de falsos positivos adjudicados, o se resuelven con la regla de
   contexto?

---

# LA ADJUDICACION, pregunta por pregunta

## 1. Alcance: **ESTRECHO**

Dos clases unicamente: **el compuesto exacto `<numeral> por ciento`**, y **las
decenas, centenas y el mil como palabra** (veinte a noventa, cien, ciento,
doscientos a novecientos, mil), incluidos compuestos como *"cuarenta y cinco"*.

**Fracciones, frecuencias, ordinales y numerales chicos quedan FUERA a
proposito**: la medicion del radio de explosion demostro el doble sentido. Lo que
queda fuera **lo cubre la lectura del lote**, como cazo el primer caso.

### Enmienda: `ciento` suelto, RATIFICADO fuera

El ejecutor excluyo `ciento` de la clase de las que disparan solas, apartandose
de la letra de la lista de centenas, y lo reporto. **El auditor lo ratifica con
su mismo razonamiento**: su uso real vive dentro de *"por ciento"*, que ya esta
cubierto por la clase del compuesto, y suelto **solo duplicaba la unidad
detectada** sin cazar nada nuevo.

### Comportamiento verificado y CORRECTO, para que nadie lo reporte como bug

Un **nombre de norma con digitos**, como `MIL-STD-105D`, **SI dispara** cuando se
anade como texto **nuevo**: no por la extension de palabras, sino por **la mitad
de digitos** de la baranda, que ve el `105`.

**Es lo deseado.** Una norma citada que **no estaba en el original** es un hecho
nuevo, y un hecho nuevo es exactamente lo que la baranda existe para frenar.

Comprobado en los dos sentidos:

| caso | resultado |
|---|---|
| `MIL-STD-105D` **nuevo** respecto del original | **dispara** (`105`) |
| `MIL-STD-105D` **ya presente** en el original | **no dispara** |

Lo que la regla de tokenizacion resuelve es otra cosa: que la **palabra** `MIL`
dentro de ese token **jamas** case con el numeral `mil`.

## 2. Contexto: **SI**, el compuesto exacto para "por ciento"

**La fragilidad ante redacciones nuevas es aceptable porque falla hacia el falso
NEGATIVO**, que la lectura ve. Un falso positivo bloquea nodos buenos **en
silencio**.

## 3. Accion: **RECHAZA**, con la semantica de diff intacta

Igual que los digitos. **Solo la aparicion NUEVA respecto del original rechaza**;
lo que ya estaba en el nodo jamas dispara.

**VALVULA DE DEGRADACION, fijada por adelantado y no discutible en caliente**: si
en operacion se adjudican **DOS falsos positivos** de esta extension en el
registro de falsos positivos, **se degrada a aviso** y vuelve a adjudicacion.

## 4. Los cinco compuestos: **SIN LISTA DE EXENCIONES**

Cuatro quedan fuera **por alcance** (`doble pared`, `numero par`, `de una vez`,
`primera mitad`) y `MIL-STD` cae **por la regla de tokenizacion**: se matchean
**palabras completas en minuscula**, jamas subcadenas de tokens con mayusculas,
guiones o digitos pegados.

---

# LA CONSTRUCCION, hecha

**La baranda salio a un solo sitio: `scripts/cifras.py`.** Estaba **duplicada**
en `revoz_pack.py` y `consolidar_pack.py`, y ampliarla habria dejado la misma
regla escrita dos veces. Los dos scripts ahora la importan y **ninguno guarda
copia**, con un test que lo custodia.

**Un ajuste que tomo el ejecutor y reporta**: `ciento` no entra en la clase de
las que disparan solas, aunque este en las centenas. Suelto es arcaico y su uso
real es siempre dentro de *"por ciento"*, que ya cubre la clase del compuesto;
dejarlo solo duplicaba la unidad detectada sin cazar nada nuevo.

## Los fixtures, los dos lados

**DEBE CAZAR** (6): el compuesto `<numeral> por ciento`, `cuarenta y cinco`,
`cien` como cuantificador, `mil` como palabra, otro porcentaje escrito, y los
digitos de siempre.

**NO DEBE CAZAR** (13), **todos sacados del catalogo real** y no de laboratorio:
`doble pared`, `numero par`, `de una vez`, `una vez por semana`, `primera mitad`,
`la mitad de`, los marcadores de discurso, `MIL-STD-105D`, `tres tipos`, `una
solucion`, `ciencia` (contiene `cien`), `milagro` (contiene `mil`), y
`Mil Millones` en mayuscula.

## La pasada en seco

**Cada uno de los 3.521 nodos activos comparado consigo mismo: CERO disparos**,
que es lo que la semantica de diff exige. Un solo disparo habria sido un defecto
de construccion.

**23 nodos (0,7 por ciento) contienen hoy alguna cifra en palabras** y quedan
protegidos por el diff: ya estaban, y jamas dispararan.

`engine/test_cifras.py` custodia las seis cosas, incluida la pasada en seco.
