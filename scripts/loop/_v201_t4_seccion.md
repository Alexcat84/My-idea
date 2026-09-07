### TAREA 4: `OP-L-01` Y `OP-L-03`, LEIDAS CONTRA SU VARA. LECTURA MEDIDA, SIN MOVER NADA

**LO PRIMERO Y SIN SALTARSELO: LA VARA CORRIDA POR MI, CON EL CORTE DE ESTA
VUELTA.** El corte es **el HEAD de apertura**, `405123f1`, leido del sello
`docs/loop/SALIDA_V201_HEAD_APERTURA.txt` y no tecleado. **La vara no se clona y
no se toca: se invoca.** Salidas selladas en `docs/loop/SALIDA_V201_T4_VARA.txt`
(**17849 bytes en disco y 17565 normalizados a LF**, y las dos van porque la
convencion sigue sin fijar) y `docs/loop/SALIDA_V201_T4_LECTURA.txt` (**13224
bytes en disco y 13224 normalizados a LF**).

```
python scripts/loop/_v201_t4_leer_op_l_01_y_03.py --corte 405123f1b49cde57f4ce4f05a1d1cd5ab4d7e065
```

**LAS CIFRAS DE HOY, LEIDAS DE SU SALIDA Y CONTRASTADAS UNA A UNA CON LAS DEL
ENCARGO.** Exitcode **0**. Contado de `docs/loop/SALIDA_V201_T4_VARA.txt`:

| cifra de la vara | encargo | hoy | veredicto |
|---|---:|---:|---|
| fichas del expediente | 71 | 71 | CALZA |
| fichas que no calzan | 37 | 37 | CALZA |
| fichas en LISTA sin ninguna prueba | 6 | 6 | CALZA |
| de esas, TRABAJO REAL | 4 | 4 | CALZA |
| de esas, CONSUMIDAS por otra ficha | 2 | 2 | CALZA |

**CIFRA cifras del encargo que discrepan de las de hoy: 0.** Y las que el encargo
no trae y la vara si publica, para que la tabla no se lea como si fueran todas:
**24 congeladas declaradas**, **12 congeladas en silencio**, **1 HECHA sin ninguna
prueba**, **6 fichas de tipo MESA** de las cuales **5 en LISTA**.

**LA PRUEBA DE COBERTURA VA DECLARADA ANTES DE CORRERSE**, en la constante
`PRUEBAS` del propio fichero, **para que la aguja no se elija despues de mirar**. Y
**es prueba de PRESENCIA de lo que la ficha dice que hay, no de calidad de la
mesa**, que es exactamente lo que la propia vara advierte y aqui no se mejora.

#### `OP-L-01`, LINEA 41. LOS TRES DOCUMENTOS CUBREN LO QUE LA FICHA DESCRIBE

`estado` **LISTA** (leido, no movido), `fecha_corte` **2026-08-11**, tipo **MESA**,
`depende_de` **vacio**, y `nodos`, `preservar`, `eliminar` y `superviviente` en
**0, 0, 0 y `None`**.

**SU `verificacion`, CITADA POR LINEA.** La ficha es **una linea de JSONL**, asi que
la coordenada es **la linea 41 mas el indice**, y las dos van juntas. **6
elementos**: `verificacion[1]` (78 caracteres), `[2]` (51), `[3]` (69), y
`[4]`, `[5]` y `[6]` son **CORRECCIONES DECLARADAS POR ADICION** de **3326, 1993 y
2376 caracteres**, escritas por las vueltas 166 y 169.

| evidencia | documento | disco | LF | que se busco | aciertos | veredicto |
|---|---|---:|---:|---|---:|---|
| `[1]` | `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 | las cabeceras `LD-01` a `LD-11` | 11 | CUBIERTA |
| `[1]` | `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 | la cabecera `LAS ONCE, una por una` | 1 | CUBIERTA |
| `[2]` | `docs/INTRA_DOMINIO_INFORME.md` | 943970 | 943970 | la seccion 52 con su titulo entero | 1 | CUBIERTA |
| `[3]` | `docs/BANCO_DE_TEXTOS.md` | 182228 | 182228 | `TABLA VIVA DE LOS PUROS` | 1 | CUBIERTA |

**LAS CITAS QUE LO SOSTIENEN, pegadas de su linea:** la **74** de
`LECTURAS_DIRIGIDAS.md` dice `## LAS ONCE, una por una` y detras van las once, de
la **76** a la **268**; la **10055** de `INTRA_DOMINIO_INFORME.md` dice `## 52. LAS
PAREJAS QUE EL EJERCICIO NO PUEDE CERRAR`, **palabra por palabra lo que la
`evidencia` promete**; y la **938** de `BANCO_DE_TEXTOS.md` dice `#### TABLA VIVA DE
LOS PUROS, al 14 ago 2026 (vigente al puesto 1157)`.

**Y LO QUE ESA TERCERA CITA TRAE DENTRO SE NOMBRA EN VEZ DE PASARSE POR ALTO:** su
propio titulo declara vigencia **al puesto 1157**, y el marcador del cribado
recontado en la TAREA 3 de esta misma vuelta vale **3388**. **La tabla existe y
cubre la presencia que la ficha promete; su corte es viejo, y eso es una medicion,
no una acusacion.** `[4]` es prosa y no nombra fichero: por esa via no hay
documento que medir.

**CIFRA pruebas de cobertura de `OP-L-01`: 4 CUBIERTAS y 0 NO CUBIERTAS.**

#### `OP-L-03`, LINEA 43. UNO CUBRE, Y EL HUECO NO ES QUE FALTE EL TRABAJO

`estado` **LISTA** (leido, no movido), `fecha_corte` **2026-08-11**, tipo **MESA**,
`depende_de` **`OP-D-01` a `OP-D-06`**, y `nodos`, `preservar`, `eliminar` y
`superviviente` en **0, 0, 0 y `None`**.

**SU `verificacion`, CITADA POR LINEA (linea 43 mas indice). 4 elementos:**
`[1]` (53 caracteres), `[2]` (85), `[3]` (83), y `[4]` es una **CORRECCION
DECLARADA POR ADICION de 3455 caracteres**, escrita por la vuelta 72.

| evidencia | documento | disco | LF | que se busco | aciertos | veredicto |
|---|---|---:|---:|---|---:|---|
| `[1]` | `docs/plan/BANCO_DEL_PLAN.md` | 61554 | 61554 | la cabecera `P.5` | 1 | CUBIERTA |
| `[3]` | `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 | el literal `reparto por acto` | 0 | NO CUBIERTA |
| `[3]` | `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 | el propio `OP-L-03` nombrado en el documento | 0 | NO CUBIERTA |

**LA CITA QUE SOSTIENE LA CUBIERTA:** la linea **239** de `BANCO_DEL_PLAN.md` dice
`## P.5 REGLA DE ORDEN: CADA ACTO QUE VAYA A FUNDIRSE SE LEE ENTERO`.

**EL HUECO VA NOMBRADO, Y MEDIDO HASTA EL FINAL EN VEZ DE DEJARLO EN NO CUBIERTA.**
Una busqueda negativa no se puede citar sin haberla corrido (`EJECUTOR.md` 9), asi
que **se corrio tambien la positiva**: hay **2 ficheros `docs/plan/OP_L_03_*` en
disco**, `OP_L_03_LECTURAS.jsonl` (**51368 bytes en disco y LF**, **14 filas no
vacias**, **0 lineas no JSON**, **14 valores distintos del campo `acto`**) y
`OP_L_03_TRIANGULOS.jsonl` (**55705 bytes en disco y LF**, **19 filas**, **0 lineas
no JSON**, **8 valores distintos del campo `acto`**). **La `evidencia` de la ficha
no nombra ninguno de los dos.**

> **LA FRASE ENTERA, Y LAS DOS MITADES SE MIDEN: el documento que la `evidencia` de
> `OP-L-03` NOMBRA no trae ni el literal `reparto por acto` ni una sola mencion de
> `OP-L-03`; y los ficheros que SI traen un reparto por acto de esta ficha EXISTEN
> en disco y su `evidencia` NO LOS NOMBRA. EL HUECO NO ES QUE FALTE EL TRABAJO: ES
> QUE LA EVIDENCIA APUNTA AL DOCUMENTO EQUIVOCADO.**

**CIFRA pruebas de cobertura de `OP-L-03`: 1 CUBIERTA y 2 NO CUBIERTAS.**

#### LO QUE SE PROPONE Y LO QUE NO SE DECIDE

**NO SE MOVIO NINGUN `estado`, NO SE CERRO NINGUNA FICHA, no se adjudico ninguna
clase, no se toco ni un nodo ni un veredicto y NO SE ESCRIBIO UNA SOLA LINEA EN
`docs/plan/` en esta tarea.** Lo que produce es **lectura medida**. Y de ella salen
**dos propuestas**, que **propongo con su evidencia y adjudica el auditor**:

1. **`OP-L-01`:** sus **tres documentos existen y cubren la presencia que su
   `evidencia` promete**, 4 pruebas de 4. **Eso NO dice que su mesa se hiciera
   bien**, y por eso no la cierro: **propongo que se mire si el criterio de HECHO
   de `docs/plan/08_VERIFICACION.md` se da**, y **el corte del puesto 1157 de la
   TABLA VIVA queda nombrado** como lo que habria que remirar.
2. **`OP-L-03`:** propongo **una correccion declarada de su `evidencia`**, del
   mismo carril que la que esta vuelta escribio para `OP-I-01`, **que nombre
   `docs/plan/OP_L_03_LECTURAS.jsonl` y `docs/plan/OP_L_03_TRIANGULOS.jsonl`**, que
   existen y traen el reparto por acto. **No la escribo yo en esta vuelta**: el
   encargo manda **lectura medida** para esta tarea, y una correccion en su sede es
   escritura en `docs/plan/` que nadie me adjudico aqui.
