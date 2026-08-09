# La deuda de `RE_CIFRA`: PARO con los casos grises

**Tarea 2 detenida a proposito.** El encargo lo dijo: *"si al construirlo
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

**No se escribio ni un patron.** El detector sigue como estaba.
