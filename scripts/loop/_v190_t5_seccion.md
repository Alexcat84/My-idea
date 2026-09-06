### TAREA 5. LA SEDE DE `OP-L-02`. CERRADA, Y LA RESPUESTA NO ES LA QUE EL ENCARGO TEMIA

**LA CABECERA DE UNA LINEA: LAS TRES NOMINAS SI TIENEN SEDE EN EL REPO, Y ESTAN
MEDIDAS CON COBERTURA COMPLETA DESDE LA VUELTA 169. LO QUE `OP-L-02` NO TIENE ES
UN PRODUCTO DOCUMENTAL PROPIO EN `docs/plan/` NI UNA SOLA MENCION DE FICHERO EN SU
CAMPO `evidencia`.** No se le inventa ninguna sede, no se la declara HECHA y no se
la mueve de estado: sigue en `LISTA`.

**LOS FICHEROS, MEDIDOS POR LAS DOS CONVENCIONES:**

| fichero | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `scripts/loop/vuelta190_tarea5_sede_de_op_l_02.py` | 14028 | 14028 | 321 | `28431e872f3e7af8` |
| `docs/loop/SALIDA_V190_T5_SEDE_OP_L_02.txt` | 17879 | 17879 | 265 | `d39e232063a41eec` |

#### LO QUE SE BUSCO, DONDE, Y CON QUE UNIVERSO DICHO ANTES DE BUSCAR

- **El universo:** `docs/` y `scripts/`, extensiones `.md`, `.jsonl`, `.txt`,
  `.json`, `.py` y `.mjs`, excluyendo `__pycache__`, `node_modules` y `.git`.
  **CIFRA ficheros del universo: 10901.**
- **Que se busco:** los nombres de **las tres nominas** y de **los cuatro grupos
  del backlog**, leidos **del campo `nota` de la propia ficha** y no de una lista
  tecleada, cada uno con su literal al lado.
- **La busqueda negativa se hizo con su comando y no se cita** (`EJECUTOR.md` 9):
  cada busqueda queda escrita con lo que se busco y donde, para que el cero se
  pueda repetir.

**Y UNA CORRECCION DECLARADA SOBRE MI PROPIA APERTURA:** el bloque **H.7** del
sello de apertura de esta vuelta publica **`CIFRA fichas con id OP-L-02: 0`** sobre
las 71 fichas. **Esa cifra es cierta y engana:** busque por las claves `id` y
`operacion`, y **la clave del id en `docs/plan/OPERACIONES.jsonl` es `id_op`**. La
ficha existe y vive en la **linea 42**. **El texto viejo no se borra:** queda en el
sello de apertura, ya commiteado, con esta correccion al lado.

#### LA BUSQUEDA, CON SUS CIFRAS

**LAS TRES NOMINAS AFECTADAS:**

| nomina (literal de la ficha) | ficheros que la nombran | candidatos a sede en `docs/plan/` |
|---|---:|---:|
| `cuadrantes de mercado (8)` | 518 | 3 |
| `ecuacion de valor (5)` | 356 | 2 |
| `el bloque humano de la supervision de la IA (3)` | 103 | 4 |

**LOS CUATRO GRUPOS DEL BACKLOG:**

| grupo | ficheros que lo nombran |
|---|---:|
| 126 esperan destejido | 435 |
| 55 resto sin mesa ni nomina | 17 |
| 5 de sales roadmap | 137 |
| 3 ya leidas en la primera tanda | 32 |

**LAS SIETE RUTAS QUE LA PROPIA FICHA NOMBRA EXISTEN LAS SIETE Y NINGUNA MIDE CERO
BYTES**, comprobadas una a una en disco (una ruta publicada como prueba es CIFRA,
`EJECUTOR.md` 1): `SALIDA_V169_T5_COBERTURA_OP_L_02.txt` (5559), 
`SALIDA_V169_T5_LOTE_SALES_ROADMAP.txt` (7945),
`SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` (5337), `SALIDA_V170_T4B_PUENTES.txt` (4564),
`docs/plan/LD_SALES_ROADMAP.md` (20563), `docs/plan/LECTURAS_DIRIGIDAS.md`
(214916) y `docs/plan/INVENTARIO.jsonl` (584554).

#### LA RESPUESTA, Y VA CON LA DISTINCION QUE LA VARA NO HACE

**LAS TRES NOMINAS TIENEN SEDE, Y ADEMAS ESTAN MEDIDAS.** Su cobertura se computo
en la vuelta 169 y vive en `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt`
(**5559 bytes en disco y 5449 normalizado a LF**, **110 lineas**), cuya tabla final,
contada de ese fichero, dice: **46 pares posibles en las seis nominas, 0 pares SIN
veredicto, y 6 de 6 nominas con cobertura COMPLETA**. Y su contenido vive en
`docs/plan/LECTURAS_DIRIGIDAS.md`, `docs/plan/INVENTARIO.jsonl`,
`docs/plan/RECOMPUTO_3388.md` y `docs/plan/LD_SALES_ROADMAP.md`.

**LO QUE NO TIENE, MEDIDO Y NO SUPUESTO, SON DOS COSAS DISTINTAS Y CONVIENE NO
CONFUNDIRLAS:**

1. **CERO MENCIONES DE FICHERO EN SU CAMPO `evidencia`.** Su evidencia entera son
   **73 caracteres de prosa**: *"MEDIDO el 11 ago 2026: 205 pares fuera de cola,
   11 leidos, 194 pendientes"*. **Eso es lo que la vara del acta 190 mide**, y por
   eso la saca como **la unica de las cuatro mesas de TRABAJO REAL sin documento
   que medir**. La linea de la vara, leida de `docs/loop/_auditor_v190_vara.txt`:
   *"`OP-L-02` | 09_LECTURAS_DIRIGIDAS | ninguna | (su evidencia entera es prosa:
   no nombra ningun fichero) | NO"*.
2. **NINGUN PRODUCTO DOCUMENTAL PROPIO EN `docs/plan/`.** De los **178** ficheros
   que nombran `OP-L-02`, **solo UNO vive en `docs/plan/`**, y es
   `docs/plan/RECOMPUTO_3388.md`, que no es suyo. Es justo lo que la separa de sus
   hermanas: `OP-L-03` nombra `docs/plan/BANCO_DEL_PLAN.md` y
   `docs/plan/LECTURAS_DIRIGIDAS.md`, y `OP-I-01` nombra
   `docs/plan/INVENTARIO.jsonl` y `docs/plan/10_INVENTARIO.md`.

**Y AQUI VA LO QUE TRAIGO YO, QUE LA VARA NO MIDE PORQUE NO MIRA ESE CAMPO:** su
campo **`nota`** tiene **5578 caracteres** y **nombra 13 ficheros**, y su campo
`verificacion` **1682 caracteres** y **2 ficheros**. **La ficha SI apunta a
documentos; lo que no lo hace es el campo que la vara lee.** Ademas, **DOS ficheros
llevan su nombre dentro del suyo propio y los dos existen con bytes**:
`docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt` (5559) y
`docs/loop/SALIDA_V170_T5B_VEREDICTO_OP_L_02.txt` (5074). **Pero los dos viven en
`docs/loop/`, que es donde van las salidas de una vuelta, y no en `docs/plan/`, que
es donde vive el producto de una mesa.**

#### EL LIMITE, QUE NO SE CRUZA

**NO SE LE INVENTA UNA SEDE A LA FICHA.** Podria sostenerse que
`SALIDA_V169_T5_COBERTURA_OP_L_02.txt` **es** su producto documental, porque lleva
su nombre, mide sus nominas y existe con bytes. **No lo declaro yo:** decidir que
una salida de vuelta cuenta como producto de mesa **cambia el alcance de la
campana**, y el encargo reserva eso al fundador con esas palabras. **Lo mido, lo
publico entero, y lo elevo.**

**NO SE DECLARA HECHA Y NO SE MUEVE DE ESTADO:** sigue en **`LISTA`**.
`docs/plan/OPERACIONES.jsonl` se abrio **solo en lectura** y mide **498085 bytes en
disco y 498085 normalizado a LF** al entrar y al salir, **identicos**.

**LA PREGUNTA QUE TRAIGO, PARA QUE EL AUDITOR LA ELEVE:** dado que las tres
nominas **si** tienen sede y **si** estan medidas con cobertura completa desde la
169, y que `docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt` lleva el nombre de la
ficha y mide justo lo que su `verificacion` pide, **falta decidir si a `OP-L-02` le
falta un documento o solo le falta que su campo `evidencia` NOMBRE los que ya
existen**. **Son dos deudas muy distintas y la segunda es barata.** Yo no elijo
entre las dos.
