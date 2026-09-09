### TAREA 2. LA VARA DE LAS TRES FASES, ESCRITA Y USADA

**LA DECISION QUE LO ORDENA, POR SU RUTA:**
`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, **DECISION 2**. El acta
211 ya habia reservado estas filas al fundador en su `6.4`, y el acta 213 midio
en su `7.2` que la ausencia era **total y no parcial**.

#### 2.a LAS TRES FILAS, DERIVADAS Y NO INVENTADAS

**LO QUE SE ESCRIBIO ES ADITIVO Y NO TOCA UNA LETRA DE LA TABLA VIEJA:**
`numstat` sobre `docs/plan/08_VERIFICACION.md` da **33 0 docs/plan/08_VERIFICACION.md**, o sea **altas y
CERO bajas**. La guarda comprueba ademas, sobre el texto y no de palabra, que
**las 8 filas viejas siguen enteras** y que **no desaparece ni una linea del
fichero**.

**LA REGLA DE DERIVACION ES MECANICA Y NO ES DE OJO:** cada celda se **compone
concatenando los textos VERBATIM** de las clausulas de `verificacion` que las
propias fichas traen, y **el juicio cae si una celda trae texto que no salga de
una clausula**. Las clausulas de `OP-V-01` que **abren con el numero de una fase
que ya tiene fila** se excluyen, porque no son la vara de su fase sino la ficha
repitiendo filas que ya existen: **de sus 9 clausulas se excluyen 8 y queda 1**,
la transversal, que es la de la fase 08.

**LAS TRES CELDAS, CON SU CUENTA DE CLAUSULAS LEIDA DEL FICHERO:** la fila
**08** trae **1** clausula, la **09** trae **8** y
la **10** trae **4**.

**Y LAS CORRECCIONES DECLARADAS NO ENTRAN, POR EL REGISTRO `R.72` DEL ACTA 208**,
que separo las clausulas de vara de las correcciones declaradas diciendo que
estas **nunca fueron puntos de la vara**. Contadas de la salida, ficha por ficha:

| ficha | fase | clausulas de vara | correcciones declaradas | excluidas por tener fila ya |
|---|---|---:|---:|---:|
| `OP-V-01` | 08_VERIFICACION | 9 | 0 | 8 |
| `OP-L-01` | 09_LECTURAS_DIRIGIDAS | 3 | 4 | 0 |
| `OP-L-02` | 09_LECTURAS_DIRIGIDAS | 3 | 1 | 0 |
| `OP-L-03` | 09_LECTURAS_DIRIGIDAS | 3 | 1 | 0 |
| `OP-I-01` | 10_INVENTARIO | 4 | 0 | 0 |

**Cada fila de la tabla de derivacion que se escribio en el plan lleva su cita:
ficha, indice de la clausula y linea de `docs/plan/OPERACIONES.jsonl`. FILAS DE
DERIVACION ARMADAS: 14.**

**EL CASO ROJO, PROBADO POR MUTACION** (`docs/loop/SALIDA_V214_T2_MUTANTES.txt`):
**5 mutantes y caen los 5**, con el texto bueno pasando el
mismo juicio en **0 fallos**.

**UNA CAIDA PROPIA MAS, `D.4`, CAZADA POR MI EN LA SIMULACION:** mi primera
version leia los numeros de fase **de todo el fichero**, y este fichero tiene
muchas tablas: se tragaba **707, 1096, 2464 y mas** como si fueran fases. **No
cambiaba el resultado** (el 8, el 9 y el 10 no estaban entre ellos), **pero una
vara que acierta por suerte no es una vara**, asi que la lectura se acoto a la
tabla del criterio, de su cabecera a su ultima fila. Hoy da exactamente
**[0, 1, 2, 3, 4, 5, 6, 7]**.

**`docs/plan/OPERACIONES.jsonl` NO SE TOCA EN LA `2.a`, y esta probado con su
`sha256`, no prometido:** el mismo al entrar y al salir de la escritura.

#### 2.b LAS CINCO FICHAS, RE-MEDIDAS CONTRA ESAS FILAS

**Salida: `docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt`. La vara se LEE de
`docs/plan/08_VERIFICACION.md`, no se teclea: si aquella fila cambiara, esta
medicion cambiaria con ella.**

**LA HONESTIDAD DEL ALCANCE VA DELANTE:** no toda clausula de una vara es
mecanizable. Cada una se marca **MECANICA** (con su sonda corrida hoy y su cifra)
o **DOCUMENTAL**, y **para las documentales SE DECLARA QUE NO HAY CASO ROJO
AUTOMATICO**, en vez de fabricar una sonda que se apruebe sola.

| ficha | fase | clausulas suyas | con sonda mecanica | documentales |
|---|---|---:|---:|---:|
| OP-V-01 | 08_VERIFICACION | 1 | 1 | 0 |
| OP-L-01 | 09_LECTURAS_DIRIGIDAS | 3 | 2 | 1 |
| OP-L-02 | 09_LECTURAS_DIRIGIDAS | 3 | 1 | 2 |
| OP-L-03 | 09_LECTURAS_DIRIGIDAS | 3 | 0 | 3 |
| OP-I-01 | 10_INVENTARIO | 4 | 4 | 0 |

**CIFRA fichas re-medidas: 5. CIFRA clausulas repartidas:
14, de ellas 8 con sonda y 6
documentales, y la suma se comprueba contra si misma en la salida.**

**LAS CUATRO SONDAS, CON SU CIFRA DE HOY:**

- **EL MARCADOR DEL ARCHIVO: 3388 filas**, contadas hoy de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.
- **LOS PARES DE LECTURA DIRIGIDA: 27 cabeceras**, y de esos **PARES**,
  **0 tienen veredicto en el archivo**, o sea que **la clausula
  CALZA**: viven solo en su pagina.
- **LOS CUATRO PUNTOS DE `OP-I-01`**, citados de la TAREA 1 de esta misma vuelta:
  **2 CUBRE y 2 A MEDIAS**.
- **LOS CINCO PUNTOS TRANSVERSALES DE `OP-V-01`**, buscados uno a uno por su
  marca propia dentro de la `nota` de la ficha (**5105 caracteres**):
  **los cinco estan escritos**, y el commit que movio su estado, leido de la
  propia nota, es **`e966d896`**.

**LA `OP-V-01` VA POR PRUEBA POR CITA Y NO SE VUELVE A PRODUCIR LA CORRIDA K**,
tal como el encargo dice: es la **cuarta via** que la DECISION 5 del fundador del
4 sep 2026 autorizo **para esta ficha**. **Y se repite aqui lo que la propia nota
de la ficha ya dice, para que nadie lo lea como un verde que no es: esa prueba NO
cambia el veredicto de la vara del expediente, que sigue midiendo la ficha como
HECHA sin ninguna de sus tres pruebas.**

**DOS DISCREPANCIAS DECLARADAS, NI RESUELTAS NI TAPADAS:**

1. **`D.5`, EL MARCADOR.** La clausula escribe *"sigue en 2.117"* y el archivo mide
   **3388** hoy. **Leida a la letra NO CALZA.** Las dos lecturas van
   escritas y **no elijo yo**: la literal dice que no calza; la de su corte dice
   que la clausula pide que **esa operacion** no mueva el marcador, y el marcador
   se movio porque **el cribado siguio hasta cerrar**, no por la ficha. **Cual de
   las dos manda es doctrina que no esta escrita: va como PENDIENTE DE
   DOCTRINA** (`EJECUTOR.md` 5).
2. **`D.6`, LA CIFRA ONCE.** La clausula dice *"las once"* y la pagina trae
   **27** cabeceras hoy, porque siguio creciendo. **La clausula es de su
   corte y se dice, en vez de reescribirla.**

**UNA CAIDA PROPIA MAS, `D.7`, Y ES DE LAS QUE IMPORTAN:** mi primera sonda de los
pares preguntaba si **los dos NOMBRES** aparecian en el archivo, y eso da que si
para casi cualquier par del catalogo: **salia 27 de 27 y habria publicado una
alarma falsa contra una clausula que en realidad se cumple**. Corregida a comparar
**el PAR** contra los campos `nodo_a` y `nodo_b`, da **0** y la
clausula calza. **Una sonda mas laxa que su clausula no mide esa clausula.**

**LO QUE ESTA TAREA NO HACE:** la `2.b` **no escribe en el arbol del plan**, no
mueve ningun campo `estado`, no toca la vara del expediente y **no asciende
ninguna ficha**. **`numstat` del arbol del plan al cerrar: 1 fila(s).**
