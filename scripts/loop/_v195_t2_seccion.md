### TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. **CERRADA, CON 54 DE 60, Y CON DOS DISCREPANCIAS FUERA DE MI MARCADO QUE PUBLICO EN VEZ DE ESCONDER.**

**ESTA TAREA SE HIZO ANTES QUE LA 1, Y EL MOTIVO SE DECLARA EN VEZ DE
DEJARLO.** La seccion 2 del acta 195 se titula *"LA RELECTURA CIEGA: 27 DE 30, Y
LAS TRES QUE FALLE SON MIAS"* y publica las clases del auditor sobre **estos
mismos 30 puestos**. Registrar el acta antes de emitir mis clases me habria
quemado la ciega, y el registro no depende del orden. **Las dos tareas
bloqueantes estan cerradas; lo unico que cambia es cual va primero.**

#### 2.a EL SUJETO, RECOMPUTADO Y NO COPIADO

`vecinos()` **se importa** de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`
en `scripts/loop/vuelta195_tarea2_relectura_al_doble.py`, con
`from ... import vecinos`. **No se copia y su regla no se toca: cambia lo que se
le pasa**, que es la `5.2` del acta 188.

**EL UNIVERSO CONSUMIDO, CONTADO DE SUS DOCE FICHEROS Y NO COPIADO DEL ENCARGO.**
Cifras de `docs/loop/SALIDA_V195_T2_SUJETO.txt`:

| lo que se cuenta | cifra | de donde sale |
|---|---:|---|
| ficheros del universo que EXISTEN | **12 de 12** | los doce nombrados en `UNIVERSO_CONSUMIDO` |
| universo consumido SIN el tramo de la 195 | **561** | contado de sus ficheros |
| universo consumido CON el tramo de la 195 | **591** | contado de sus ficheros |
| la cifra que el encargo publica | **591** | `PROMPT_SIGUIENTE.md` |
| calzan | **SI** | cotejo en el propio instrumento |

**EL SOLAPE SALE CERO POR CONSTRUCCION Y NO POR SUERTE**, porque `evitar` va
DENTRO de la llamada y no comprobado despues: **solape de los vecinos con el
tramo 0** y **con el universo consumido 0**. Los 30 vecinos recomputados son **el
MISMO CONJUNTO** que la sellada del auditor
`docs/loop/_auditor_v195_doble_para_la_196.txt`, cotejado leyendo solo su linea
`EL DOBLE` para que el cotejo no calce por arrastrar tambien el tramo.

**Y EL 654 Y EL 719, QUE DISPARAN `AUDITOR.md` 1.2, ESTAN LOS DOS DENTRO** del
tramo que se dice releer. El instrumento **PARA** si alguno estuviera fuera.

#### 2.b LOS SESENTA, LEIDOS A CIEGAS, Y LAS CLASES SELLADAS ANTES DEL DESTAPE

`aislador_de_ciega.py` con criterio escrito: **60 pares elegidos, CERO fugas del
destape en la salida ciega**. Ciega `docs/loop/SALIDA_V195_T2_CIEGA.txt` (81838
bytes) y destape `docs/loop/SALIDA_V195_T2_DESTAPE.txt` (64898 bytes), **los dos
existen y ninguno mide cero bytes**.

**EL ORDEN NO SE AFIRMA: SE LEE DE GIT**, y el bloque `A` del cotejo lo publica
con `git log --diff-filter=A`. Mis clases viven en
`docs/loop/SALIDA_V195_T2_MIS_CLASES.txt` y **se commitearon con el destape sin
abrir**.

#### 2.c LA VARA, CITADA POR NUMERO Y NO PARAFRASEADA

`docs/BANCO_DE_TEXTOS.md` **`9.6.1`**, LA VARA DE LA RAMA CONTENIDO-MANDA: LA
LINEA O EL PROCEDIMIENTO, con sus dos precisiones **`9.6.2`** (la vara TIENE
DIRECCION: que anade el HIJO a la MADRE, nunca al reves) y **`9.6.3`** (el TAMANO
del solape NO decide: se pesa el resto y en que lado), y **`9.22`** disponible
para la figura que da `C`.

**Y LA VARA COMO SUELO Y NO COMO TECHO, que es el error que el auditor midio en
su propia tanda y lo mas util que salio de ella.** Va escrito DENTRO del criterio
que la ciega lleva, no en mi cabeza. **Donde se aplico y se ve:** el `719`, que la
regla fijada en el puesto `595` resuelve sin llegar a la vara general (dos nodos
de fases distintas del recorrido son sanos). **Mi clase ahi es `D` y el archivo
dice `D`.**

#### 2.d LA `B` NO SE SALTA, Y ESTA VEZ SE EMITIERON CUATRO

| quien | `B` emitidas | sobre cuantos | la `B` del archivo la vio |
|---|---:|---:|---|
| el auditor, acta 195 | **0** | 30 | no |
| yo, esta tanda | **4** | 60 | **SI, el `654`** |

Contado por el bloque `G` del cotejo: **`B` que el archivo tiene en estos 60: 1
(el `654`)**; **`B` que el archivo tiene y yo NO vi: ninguna**; **`B` que yo emito
y el archivo no tiene: 3 (`1807`, `1808`, `3173`)**. **Paso de perder la clase a
sobre emitirla**, y las tres de mas caen DENTRO de mi marcado.

#### 2.e EL COTEJO, CON SUS CIFRAS, CONTADO DE `SALIDA_V195_T2E_COTEJO.txt`

| lo que se mide | sobre los 60 | sobre los 58 limpios |
|---|---:|---:|
| coinciden | **54** | **52** |
| discrepan | **6** | **6** |
| discrepancias DENTRO de mi marcado | **4** | **4** |
| discrepancias FUERA de mi marcado | **2** | **2** |

**MI REPARTO CONTRA EL DEL ARCHIVO, los dos contados:** mio `A 9 | B 4 | C 0 | D
47`; del archivo `A 8 | B 1 | C 0 | D 51`.

**LAS SEIS DISCREPANCIAS, UNA A UNA:**

| puesto | yo | archivo | mitad | marcado |
|---:|---|---|---|---|
| **976** | `D` | `A` | vecino | **DENTRO** |
| **1807** | `B` | `D` | TRAMO | **DENTRO** |
| **1808** | `B` | `D` | vecino | **DENTRO** |
| **2428** | `A` | `D` | vecino | **FUERA** |
| **2662** | `A` | `D` | vecino | **FUERA** |
| **3173** | `B` | `D` | vecino | **DENTRO** |

**DE MIS SIETE DISCUTIBLES ACERTE 3** (`655`, `1206`, `2427`) **Y FALLE 4**
(`976`, `1807`, `1808`, `3173`). **El marcado hizo su trabajo en cuatro de las
seis**, y no en las otras dos.

**LAS DOS QUE CAEN FUERA DE MI MARCADO SON `2428` Y `2662`, Y LAS DOS TIENEN EL
MISMO PERFIL:** ids que solo se diferencian en una palabra o un numero
(`desarrollar` contra `desarrollo`; `consejo_calidad_2` contra
`consejo_de_calidad_3`), yo lei `A` por eso, y **el archivo dice `D` en las dos**.
**Mi error es el simetrico del que el auditor midio en su tanda:** el suyo fue
aplicar la vara general donde habia regla propia; el mio es **dejar que la
semejanza de los ids pese**, cuando `9.6.3` dice expresamente que **lo que se pesa
es el resto y en que lado**, y en los dos casos el lado largo conserva
procedimiento propio. **Lo digo con esas palabras porque es la leccion que la 196
puede usar, no una disculpa.**

**POR `AUDITOR.md` 1.2 ESO BAJA EL CREDITO DE MI TANDA Y MI TRAMO SE RELEE AL
DOBLE.** Lo declaro yo, con su cifra, sin esperar a que lo encuentre el auditor.

#### 2.f LO QUE ESTA TAREA NO HACE, Y ES LA MITAD QUE IMPORTA

**NO SE MUEVE NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y
cierra en **`sha256` LF `0a77b5a35a962621`** sobre **4054129 bytes**, medido por
las dos convenciones en el bloque `A` del sujeto y en el `H` del cotejo. Las seis
discrepancias **se declaran y se traen**; quien las aplica, si procede, es el
RECOMPUTO.

#### 2.g DOS CORRECCIONES DECLARADAS DENTRO DE ESTA TAREA, Y NINGUNA SE TAPA

**LA PRIMERA, EN MI FICHERO DE CLASES.** La columna que dice a que mitad
pertenece cada puesto salio mal en **tres filas** (`11`, `974`, `975`) y sumaba
**31 y 29** donde solo puede sumar **30 y 30**. **Ninguna clase se toco**: lo que
estaba mal era el rotulo de reparto. La correccion va **anexada al final del
fichero con lo que decia y lo que dice**, sin borrar el texto viejo
(`EJECUTOR.md` 8). Hoy el cotejo mide **0 filas con la columna mal rotulada**.

**LA SEGUNDA, EN EL PROPIO INSTRUMENTO DEL COTEJO, Y LA CAZO SU PROPIA GUARDA.**
`mis_discutibles()` partia el fichero ENTERO por sus filas, asi que **el bloque de
la ultima fila llegaba hasta el fin del fichero** y se tragaba la seccion titulada
`MIS DISCUTIBLES`. Resultado medido: el puesto `3331` salia marcado sin estarlo y
la cuenta daba **OCHO** donde la lista del final dice **SIETE**. **La guarda que
publica las dos cifras y dice si calzan es la que lo enseno**, y por eso la caida
se vio en vez de pasar. Corregido acotando la tabla por su cabecera de cierre; hoy
las dos listas salen **SIETE y SIETE, y LAS DOS SON LA MISMA**. **El codigo viejo
se nombra entero en el docstring de la funcion en vez de borrarse.**
