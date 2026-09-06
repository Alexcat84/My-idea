### TAREA 4. LA RELECTURA AL DOBLE DEL TRAMO DEL 2422. CERRADA, Y ME SALE UNA DISCREPANCIA FUERA DEL MARCADO

**LA CABECERA DE UNA LINEA DE ESTA TAREA: 30 PUESTOS RELEIDOS A CIEGAS, 20
COINCIDEN Y 10 DISCREPAN; NUEVE CAEN DENTRO DE MIS DUDOSOS MARCADOS Y UNA CAE
FUERA, EL PUESTO 3182.** Las diez se resuelven **a favor del archivo** y **ninguna
clase se toca**.

**LOS FICHEROS, MEDIDOS POR LAS DOS CONVENCIONES:**

| fichero | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `scripts/loop/vuelta190_tarea4_relectura_al_doble.py` | 11340 | 11340 | 256 | `037bad0ee9024324` |
| `docs/loop/SALIDA_V190_T4_AISLAMIENTO.txt` | 5301 | 5301 | 78 | `9df007a50a1add26` |
| `docs/loop/SALIDA_V190_T4_CIEGA.txt` | 39678 | 39678 | 494 | `0e2e4f4c6b9ed113` |
| `docs/loop/SALIDA_V190_T4_MIS_CLASES.txt` | 4934 | 4934 | 57 | `726833347bd0c798` |
| `docs/loop/SALIDA_V190_T4_DESTAPE.txt` | 31816 | 31816 | 132 | `3e38cb6863405a73` |
| `docs/loop/SALIDA_V190_T4_COTEJO.txt` | 20783 | 20497 | 286 | `f8e1a8f6b2f5b296` |

**EL ORDEN NO SE PROMETE, SE LEE DE GIT.** El aislamiento y los dos ficheros
quedaron commiteados en **`a0148267`**, mis clases en **`92b22813`**, y el cotejo
solo existe despues. **Unas clases escritas despues del destape no prueban nada**,
y por eso van en ficheros y en commits separados.

#### EL SUJETO, ELEGIDO Y AISLADO ANTES DE MIRAR NADA

**QUE ES "EL TRAMO DEL 2422", MEDIDO Y NO TECLEADO:** la ciega del acta 189,
`docs/loop/_auditor_v189b_ciega_blind.txt`, **30 puestos**, y el **2422 esta
DENTRO** (contado de su fichero; si no lo estuviera, este instrumento hace PARADA
y no relee nada).

**QUE ES "AL DOBLE":** sus **30 vecinos deterministas**, con `vecinos()`
**IMPORTADA** de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no
copiada. **30 del tramo mas 30 vecinos son 60 puestos: el doble exacto.**

**EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO** (acta 188, `5.2` y `7.3`): a
`vecinos()` se le pasa `evitar` con los **441** puestos ya consumidos, contados de
sus **cuatro** ficheros (las dos exclusiones, 411 y 381, y las dos ciegas, 30 y
30). **Solape de los vecinos con el propio tramo: 0. Solape con el universo
consumido: 0. Los dos POR CONSTRUCCION**, porque `evitar` va dentro de la llamada
y no comprobado despues. **Su regla no se toca: cambia lo que se le pasa.**

**EL AISLADOR EN VERDE**, exitcode **0**: **30 pares elegidos, los 30 existen en el
archivo, `CIFRA fugas del destape en la salida ciega: 0`**. Ciega y destape en
**ficheros separados**, con el **criterio escrito literal** dentro de los dos.

#### EL COTEJO, CON LAS CIFRAS QUE EL ENCARGO PIDE

| medicion | cifra |
|---|---:|
| puestos releidos | **30** |
| **coinciden** | **20** |
| **discrepan** | **10** |
| discrepancias DENTRO de mis dudosos marcados | **9** |
| **discrepancias FUERA de mis dudosos marcados** | **1** |
| dudosos que marque y que SI coincidieron | 4 |

**MI REPARTO: A 7, B 3, C 0, D 20. EL DEL ARCHIVO: A 7, B 1, C 0, D 22.**

**LAS NUEVE DE DENTRO:** 648, 872, 904, 963, 1201, 1366, 2423, 3067 y 3086. Las
nueve las marque como dudosas **antes de saber si acertaba**, y las nueve se
resuelven a favor del archivo. Los casos que mas ensenan: el **1366**, donde el
archivo mide que **cuatro de los cinco pasos de cada uno se corresponden** y yo
me quede en que uno hablaba de embudo y el otro de capacidad; y el **2423**, el
vecino del propio 2422, donde el archivo separa **la linea contra su
procedimiento** con ids gemelos y misma fuente, y yo lo di por dudoso.

#### LA QUE CAE FUERA, Y SE TRAE ENTERA PORQUE ESO ES LO QUE BAJA EL CREDITO

**EL PUESTO 3182. YO DIJE `D` Y EL ARCHIVO DICE `A`, Y NO LO MARQUE COMO DUDOSO.**

- **mi motivo, literal de mi propio fichero de clases:** *"el plan de control del
  proceso del proveedor contra la planificacion tecnologica conjunta, **aunque
  comparten seis pasos**"*.
- **la razon del archivo:** misma fuente (Juran), `sim_tit 53,3`, sin arista,
  **`DISCUTIBLE MARCADO fuerte`** escrito en su propia razon, **tres pasos casi
  verbatim compartidos**, y **`A POR FUSION MUTUA`**, que mueve el contador de
  fusiones mutuas de veintiseis a veintisiete.

**ME EQUIVOQUE YO, Y LA PRUEBA ESTA EN MI PROPIA LINEA:** escribi *"aunque
comparten seis pasos"* y aun asi clasifique `D` **sin marcarlo dudoso**. Si seis
de los seis pasos del nodo corto estan en el largo, mi propio criterio escrito
(*"A cuando la mayoria de los pasos del nodo mas corto estan en el mas largo"*)
manda `A`. **La discrepancia es a favor del archivo y no hay ninguna correccion
que hacerle.**

**LO QUE ESO DISPARA, DICHO Y NO ESCONDIDO.** `AUDITOR.md` 1.2: *"si una
discrepancia aparece FUERA de los discutibles marcados, baja el credito de toda la
tanda: ese tramo se relee al doble y lo dices en el acta"*. **Esta tanda de 30 la
lei yo, y su credito baja por mi cuenta.** El tramo que habria que releer al doble
es el de estos 30 vecinos. **Yo no me lo auto encargo:** el encargo de esta vuelta
trae CINCO tareas y ese es el tope, y quien encarga las relecturas al doble es el
auditor. **Lo traigo medido, con su nombre y su cifra, para que la 191 lo
encuentre escrito.**

#### LO QUE ESTA TAREA NO HIZO

**NO SE TOCO NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abrio
**solo en lectura**, y su `sha256` LF abre y cierra en
**`0a77b5a35a962621`** (medido al entrar por el bloque A del aislamiento, al salir
por su bloque G, y otra vez en el bloque E del cotejo). **Las diez discrepancias
se resuelven a favor del archivo y no se escribe ni una fila.**
