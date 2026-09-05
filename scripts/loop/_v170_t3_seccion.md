### TAREA 3. LAS DEUDAS DE CORTE, POR `9.21` MAS `9.10`

Instrumento `scripts/loop/vuelta170_tarea3_deudas_de_corte.py`, salida
`docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt`, **exit 0**. Corrido antes con
`--comprobar`, que mide y no escribe.

**NINGUNA DE LAS TRES CIFRAS ES UNA MENTIRA, Y ESO VA PRIMERO:** las tres son
ciertas en su corte y lo unico que les falta es el corte escrito al lado. Por
eso **no se sustituye ni una letra**.

**3.a LAS APARICIONES DEL 53 EN LA NOTA DE `OP-I-01`, CONTADAS AQUI Y NO
COPIADAS DEL ACTA.** Contadas del propio campo `nota` (10.928 caracteres):

| que se cuenta | cifra |
|---|---:|
| apariciones del literal `53` en la nota | **7** |
| de ellas escritas `53 familias` | 6 |
| de ellas escritas `53 familia_de_ids` | 1 |

**El encargo dice SIETE y yo cuento SIETE: CALZA.** La cifra se publica aunque
coincida, porque la vara es el conteo y no el acta.

**LAS TRES ARITMETICAS QUE LLEVAN UN 53, SUMADAS Y NO CREIDAS.** El instrumento
extrae los sumandos escritos y los suma:

| total escrito | sumandos | suma real | veredicto |
|---:|---|---:|:-:|
| 450 | 335, 53, 19, 13, 20, 10 | 450 | CUADRA |
| 671 | 556, 53, 19, 13, 20, 10 | 671 | CUADRA |
| 323 | 221, 53, 14, 13, 12, 10 | 323 | CUADRA |

**LAS TRES CUADRAN CONSIGO MISMAS, Y ESO ES EL HALLAZGO:** el problema **no es
aritmetico, es de corte**. Cada una suma bien con el 53 que tenia delante; con
el 54 de hoy cada total subiria en uno, y la de 671 seria **672**, que es justo
lo que el fichero mide hoy.

**EL INVENTARIO DE HOY, CONTADO DE `docs/plan/INVENTARIO.jsonl` LINEA A LINEA:**
**672** entradas (556 `acto`, **54** `familia_de_ids`, 20 `figura`, 19
`defecto`, 13 `racimo`, 10 `dominio`), y **la suma de los tipos da 672**, o sea
que el conteo cuadra consigo mismo.

**LO ESCRITO:** una `CORRECCION DECLARADA (2026-09-04, vuelta 170, TAREA 3.a)`
**dentro del campo `nota` que ya existe**, sin clave nueva de esquema. La nota
pasa de **10.928 a 12.772 caracteres** y **solo crece**. **Las siete apariciones
viejas sobreviven enteras: 7 de 7**, comprobado trozo a trozo con 60 caracteres
de contexto cada uno.

**3.b EL MARCADOR, RECOMPUTADO DEL ARCHIVO EN ESTA VUELTA:** **3.388** filas en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, **A 551, B 72, C 5, D 2.760**, 3.388
puestos distintos, maximo 3.388, **cero huecos**.

**Y AQUI VA LO QUE MIDO Y EL ENCARGO NO ANTICIPA, DECLARADO EN VEZ DE
RESUELTO COPIANDO** (`EJECUTOR.md` 2: *"si discrepan de la medicion de hoy, la
discrepancia se declara en vez de resolverse copiando"*):

| ficha | elementos en `verificacion` | la clausula literal | correccion fechada que la cita |
|---|---:|---|---|
| `OP-L-01` | 6 | indice 1 | **SI, indice 4**, `CORRECCION DECLARADA (2026-09-04, vuelta 166, TAREA 2)` |
| `OP-L-02` | 3 | indice 1 | **NO** |

**A `OP-L-01` YA LE PUSIERON EL CORTE, EN LA VUELTA 166.** Su correccion dice
literalmente *"EL NUMERAL 2.117 ES EL VALOR DEL MARCADOR EN LA fecha_corte DE
ESTA FICHA, TESTIGO Y NO CONDICION. MEDIDO HOY: el marcador del cribado vale
3388"*. **Escribir una segunda que diga lo mismo seria dejar dos versiones de la
misma cosa**, que es exactamente lo que la casa no quiere. **Asi que `OP-L-01`
NO SE TOCA**, y se comprueba en disco que su `verificacion` quedo **identica**.

**A `OP-L-02` SI LE FALTABA, Y AHI SE ESCRIBE:** un elemento mas en su lista
`verificacion` que ya existe, **sin clave nueva de esquema**, que es la via que
`OP-L-01` uso en la vuelta 166 y `OP-L-03` en la vuelta 72, y que el acta 71,
seccion 6, adjudicacion 3, adjudico **con las palabras NO ES PARADA**. La lista
pasa de **3 a 4** elementos y **la clausula literal del 2.117 sigue en disco**.

**LO QUE ESTA TAREA NO MUEVE, COMPROBADO Y NO PROMETIDO:** las 71 fichas siguen
siendo 71; `OP-I-01` y `OP-L-02` siguen en sus lineas 44 y 42; las dos siguen
con **18 claves**, **cero campos movidos** ademas de `nota` y `verificacion`, y
**el `estado` de las dos sigue diciendo `LISTA`**, que no es la vara y no se
toca.
