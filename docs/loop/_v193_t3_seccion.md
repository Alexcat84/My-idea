### TAREA 3. LA VARA DEL BANCO Y LA RELECTURA AL DOBLE. **CERRADA, Y LA VARA NUEVA NO ALCANZA A LA MITAD DE MIS DISCREPANCIAS.**

**a) EL CRITERIO, CITANDO `9.6.1` POR NUMERO Y CON LA FRASE COPIADA LITERAL.** Va
DENTRO del `CRITERIO` que se le pasa a `aislador_de_ciega.py`, o sea escrito en la
propia ciega y no en la cabeza del lector, y sale copiado en
`docs/loop/SALIDA_V193_T3_CIEGA.txt` (41185 bytes, `sha256` LF `fb9a9ed247ee550f`):

> **"Si lo que el hijo añade a lo que la madre ya dice CABE EN UNA LÍNEA, REPITE.
> Si trae un PROCEDIMIENTO que la madre no tiene, CONTINÚA."**

REPITE va a `A` y CONTINUA va a `D`, que es la lectura que la `4.9` adjudica. **No
se parafrasea** (`9.5.0`). **Y la vara vieja se nombra en vez de borrarse**: era el
solape de pasos, un literal privado que cada lector escribia por su cuenta.

**c) y d) EL TRAMO Y EL DOBLE, CONTADOS DE SUS FICHEROS.** De
`docs/loop/SALIDA_V193_T3_AISLAMIENTO.txt` (7653 bytes):

- **TRAMO: los 30 puestos de `docs/loop/SALIDA_V192_T2_CIEGA.txt`** (39850 bytes,
  `sha256` LF `da9b03300a305fbd`). **Y la ciega del auditor
  `docs/loop/_auditor_v193_ciega_blind.txt` trae los MISMOS 30**: no se creyo, se
  conto de su fichero, y el instrumento dice **ES EL MISMO CONJUNTO QUE EL TRAMO:
  SI**. **`1804` y `2833` estan los dos DENTRO del tramo.**
- **AL DOBLE: 30 vecinos deterministas**, con `vecinos()` **IMPORTADA** de
  `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`. **30 mas 30 son 60, el
  doble exacto.**
- **`evitar` cargado de OCHO ficheros, contados uno a uno y con sus nombres**, no
  de una lista tecleada: los seis de la 192 mas `_auditor_v192_ciega_blind.txt` y
  `SALIDA_V192_T2_CIEGA.txt`. **Universo consumido: 501 sin la tanda de la 192 y
  531 con ella.**
- **SOLAPE con el tramo: 0. SOLAPE con el universo: 0.** Los dos **POR
  CONSTRUCCION**: `evitar` va DENTRO de la llamada, no comprobado despues.

**e) EL ORDEN, QUE ES LA PRUEBA.** Criterio escrito literal; ciega y destape en
ficheros SEPARADOS; **mis 30 clases escritas y COMMITEADAS en su propio commit
`b57aa7d6` ANTES de abrir el destape**; y **mis OCHO dudosos NOMBRADOS DELANTE**
con el motivo de cada duda escrito: `203`, `718`, `967`, `2426` (donde digo `A` y
el otro lado podria traer procedimiento) y `132`, `972`, `1069`, `3171` (donde
digo `D` y lo que se anade podria caber en una linea).

**EL COTEJO, CON EL FORMATO UNICO YA ARREGLADO POR LA TAREA 5** y con `en dudosos`
pasado **COMO TEXTO** a proposito, o sea por el camino que reventaba. De
`docs/loop/SALIDA_V193_T3_COTEJO.txt` y su salida
`docs/loop/SALIDA_V193_T3_COTEJO_SALIDA.txt`:

| | cifra |
|---|---:|
| cotejados | **30** |
| coinciden | **23** |
| discrepan | **7** |
| dudosos marcados delante | **8** |
| discrepancias DENTRO de mis dudosos | **4** (`203`, `718`, `972`, `2426`) |
| discrepancias FUERA de mis dudosos | **3** (`158`, `612`, `651`) |
| reparto del lector | A 8, D 22 |
| reparto del archivo | A 6, B 3, D 21 |

**LAS TRES QUE CAEN FUERA DE MI MARCADO SE DECLARAN, Y CON ELLAS SE DISPARA LA
ESCALADA DE `AUDITOR.md` 1.2**: `158` (yo `A`, archivo `B`), `612` (yo `D`,
archivo `B`) y `651` (yo `D`, archivo `A`). **No las escondo tras el hecho de que
la vara sea nueva.**

**f) LO QUE LA VARA CAMBIA, MEDIDO Y NO AFIRMADO**, de
`docs/loop/SALIDA_V193_T3F_QUE_CAMBIA_LA_VARA.txt` (4168 bytes), contado de los
dos cotejos y no tecleado:

**A FAVOR DE LA VARA.** De mis **10** discrepancias de la 192, **4 estan DENTRO de
su alcance** (`1068`, `1804`, `1814`, `2833`) y **la vara resuelve BIEN las 3 que
el acta adjudica**: `1068` (yo `D`, archivo `A`, vara `A`), `1804` y `2833` (yo
`A`, archivo `D`, vara `D`). **Las tres son las que el criterio viejo no resolvia,
y dos de ellas son las que cayeron fuera del marcado de LOS DOS lectores.**

**EN CONTRA DE LA VARA, Y ES MI DATO PROPIO DE ESTA VUELTA. `9.6.1` TIENE DOS
SALIDAS Y NO PUEDE EMITIR `B` NUNCA.** Leyendo la tanda de la 193 **entera** con
ella emiti **CERO `B`** sobre un tramo donde **el archivo tiene TRES** (`158`,
`612`, `718`). **Y 3 de mis 7 discrepancias son exactamente eso**: un par que el
archivo llama `B` y que la vara solo sabe empujar a `A` o a `D`. En la 192 el
mismo agujero ya estaba: **6 de mis 10 discrepancias eran pares que yo llame `B`**
(`874`, `906`, `965`, `971`, `2425`, `2659`), y **la vara no las toca**.

**LA CONCLUSION, DICHA CON SUS DOS MITADES JUNTAS: la vara arregla el eje `A`
contra `D`, que es donde nos tumbo a los dos lectores, y no dice nada sobre el eje
que mas discrepancias me produce a mi.** No es una adjudicacion floja: es una
adjudicacion **cuyo alcance acaba de quedar medido**.

**LO QUE SI MEJORO, Y TAMBIEN ES MEDICION:** mi tasa pasa de **20 de 30** en la
192 a **23 de 30** en la 193, y mis dudosos bajan de **15 de 30** a **8 de 30**,
con la misma cifra de discrepancias fuera del marcado (**3** en las dos). **Un
criterio escrito reduce a la mitad lo que el lector tiene que marcar como duda.**

**NO SE TOCO NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abrio
**solo en lectura** y su `sha256` LF **abre y cierra en `0a77b5a35a962621`** por
las dos convenciones, medido en el aislamiento y otra vez en el cotejo.
