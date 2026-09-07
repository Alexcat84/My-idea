### TAREA 3. `OP-L-01` CONTRA EL CRITERIO DE HECHO, Y EL HUECO DE LA VIGENCIA MEDIDO

**ADJUDICADA POR EL ACTA 201 EN SU `4.8`.** Sus **cuatro pruebas de cobertura
estan cubiertas** y el auditor las reprodujo las cuatro. **Eso es PRESENCIA, no
CALIDAD**, y por eso no se cierra. **Esta tarea mide la CALIDAD**, y lo que
encuentra no estaba medido.

**LOS DOS INSTRUMENTOS SE IMPORTARON Y SE CORRIERON EN MODO MEDICION, SIN
`--aplicar`**, y **ninguno se toco**: `scripts/loop/vuelta166_tarea2_correccion_op_l_01.py`
para las clausulas 1 y 2, y `scripts/loop/vuelta169_tarea4_op_l_01_clausula3.py`
para la 3. **El `sha256` de `docs/plan/OPERACIONES.jsonl` entra y sale igual en
las dos corridas**, medido antes y despues: `6006fd16dc08dc58` las dos veces.
Selladas en `docs/loop/SALIDA_V202_T3_CLAUSULAS_12_166.txt` (**32943 bytes en disco y 32684 bytes normalizados a LF**) y `docs/loop/SALIDA_V202_T3_CLAUSULA_3_169.txt` (**4028 bytes en disco y 3963 bytes normalizados a LF**). La lectura entera esta en
`docs/loop/SALIDA_V202_T3_OP_L_01.txt`.

#### EL CRITERIO DE HECHO Y LA `verificacion`, CITADOS POR LINEA

El criterio vive en `docs/plan/08_VERIFICACION.md`, cabecera en la **linea 7**
con **1 solo acierto**, literal en las **lineas 9 y 11**, y su comprobacion barata
en las **13 a 15**. **Y en ese documento `OP-L-01` no se nombra ni una sola vez:
0 lineas.** Eso se dice en vez de callarse: **el criterio que se le aplica es el
general, no una fila suya.**

La ficha vive en la **linea 41** de `docs/plan/OPERACIONES.jsonl`, con **1 solo
acierto**. Su `verificacion` tiene **6 elementos**: **3 clausulas** y **3
CORRECCIONES DECLARADAS**, que no son clausulas que cumplir. Su `evidencia` tiene
**4 elementos**.

| coordenada | caracteres | que es |
|---|---:|---|
| linea 41 + indice 0 (elemento 1) | 78 | clausula: `ninguna de las once aparece en INTRA_DOMINIO_VEREDICTOS.jsonl: viven solo aqui` |
| linea 41 + indice 1 (elemento 2) | 51 | clausula: `el marcador del cribado no se mueve: sigue en 2.117` |
| linea 41 + indice 2 (elemento 3) | 69 | clausula: `cada nomina afectada se re-mide con su cobertura al lado (banco 9.26)` |
| linea 41 + indice 3 (elemento 4) | 3326 | CORRECCION DECLARADA de la vuelta 166 |
| linea 41 + indice 4 (elemento 5) | 1993 | CORRECCION DECLARADA de la vuelta 166 |
| linea 41 + indice 5 (elemento 6) | 2376 | CORRECCION DECLARADA de la vuelta 169 |

#### EL CRITERIO APLICADO: LA CIFRA CONGELADA NO AGUANTA, Y ESO SE MIDE

El criterio pregunta si la verificacion **se caeria si el fallo volviera**. Aqui
se le hace la pregunta mas dura y mas barata que el propio criterio nombra:
**volver a correr el instrumento hoy y cotejar sus cifras contra las que la ficha
tiene congeladas**. **7 cifras cotejadas, 3 DISCREPAN:**

| cifra | corrida sellada del 2026-09-04 | corrida de hoy, 2026-09-07 | |
|---|---:|---:|---|
| cabeceras `LD` leidas de `LECTURAS_DIRIGIDAS.md` | **11** | **27** | **DISCREPA** |
| de esas, las que aparecen en comparacion LITERAL | 0 | 0 | CALZA |
| de esas, las que aparecen en comparacion RESUELTA | **3** | **11** | **DISCREPA** |
| puestos implicados en total | **5** | **61** | **DISCREPA** |
| alias en el mapa del resolutor | 761 | 761 | CALZA |
| filas de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 3388 | 3388 | CALZA |
| marcador del cribado | 3388 | 3388 | CALZA |

**QUE SIGNIFICA, DICHO CON LA MEDICION DELANTE Y SIN ARREGLARLO.** La funcion que
el instrumento llama `las_once()` **no devuelve once**: devuelve **toda cabecera
`LD` que haya hoy en `docs/plan/LECTURAS_DIRIGIDAS.md`**, y ese documento **paso
de 11 a 27 cabeceras** entre el 4 y el 7 de septiembre de 2026. La ficha tiene
congelado, en su elemento 4, **EN COMPARACION RESUELTA APARECEN 3**, y hoy el
mismo instrumento sobre el mismo archivo dice **11**: los **3** de siempre
(`LD-01`, `LD-05` y `LD-11`) mas **8 nuevos** (`LD-139` a `LD-146`), que **no son
de la tanda de las once**.

**LA CIFRA VIEJA NO ES UNA MENTIRA:** viaja con su corte, el **2026-09-04**, y con
ese corte era cierta. **Lo que envejecio es el universo que la produce.** Es la
misma especie que la 201 corrigio en `OP-I-01` y que esta vuelta corrigio en
`OP-L-03`. **PERO AQUI NO SE ESCRIBE, SE PROPONE:** el encargo de esta tarea dice
**PROPON, NO CIERRES**, y esta correccion **no esta adjudicada**.

**Y LA CLAUSULA 1 NO SE CAE POR ESTO, Y SE DICE PARA NO EXAGERAR:** en comparacion
**LITERAL** siguen apareciendo **0**, que es lo que la clausula pregunta. Lo que
no aguanta es **la cifra de la excepcion nombrada**, no el veredicto.

**UN INVARIANTE ROJO QUE NO ES UN FALLO, DECLARADO PARA QUE NADIE LO LEA MAL:** la
corrida de hoy imprime **5 invariantes, 4 pasan y 1 falla**, y el que falla es
`3_verificacion_crece_en_exactamente_dos`, *de 6 a 6, delta 0*. **Falla porque la
correccion YA ESTA en la ficha y el modo medicion no escribe nada**, no porque
algo este mal.

#### EL HUECO DE LA VIGENCIA, MEDIDO POR PRIMERA VEZ

**LA VARA VA DECLARADA ANTES DE CORRERSE**, en la constante `VARA_DE_LA_VIGENCIA`
del propio fichero, **porque una aguja que se elige despues de mirar no mide
nada**. Dice: una fila **sigue en pie** si **todos los puestos que ella misma cita
existen hoy** en el archivo; una fila que **no cita ningun puesto** es **NO
MEDIBLE POR ESTA VARA** y se cuenta aparte, **ni en pie ni caida**; y la vara mide
**PRESENCIA DEL PUESTO, no calidad de la fila**.

**LAS DOS CIFRAS SE RECUENTAN AQUI.** La cabecera esta en la **linea 938** de
`docs/BANCO_DE_TEXTOS.md`, que mide **182228 bytes en disco y 182228 bytes
normalizados a LF**, y dice literalmente *TABLA VIVA DE LOS PUROS, al 14 ago 2026
(vigente al puesto 1157)*: **vigencia 1157, leida de la cabecera**. Y
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que mide **4054129 bytes en disco y 4054129 bytes normalizados a LF**, trae **3388 filas**, **0 lineas que no sean
JSON valido**, **3388 puestos distintos** y **maximo 3388**. **La diferencia es de
2231 puestos.**

**LA TABLA SE ACOTA AL BLOQUE CONTIGUO** de lineas que empiezan por barra tras la
cabecera, **lineas 953 a 965**, y dentro de esa cota hay **11 filas numeradas**.

| lo que se cuenta | cifra |
|---|---:|
| filas de la TABLA VIVA dentro de la cota | **11** |
| filas EN PIE al corte 3388 (todos sus puestos existen hoy) | **6** |
| filas CAIDAS (citan un puesto que hoy no existe) | **0** |
| filas NO MEDIBLES POR ESTA VARA (no citan puesto) | **5** |
| filas que citan un puesto MAS ALLA de la vigencia declarada 1157 | **4** |
| filas que citan un puesto igual o mayor que el marcador de hoy 3388 | **0** |

**EL HUECO, NOMBRADO Y NO ARREGLADO.** La cabecera declara **vigencia al puesto
1157** y **4 de las 11 filas citan un puesto por encima de esa vigencia** (la 5 al
2117, la 7 al 1190, la 9 al 1600 y la 11 al 1517): **la cabecera ya esta desmentida
por sus propias celdas**, y eso se ve sin salir del documento. Ademas, **ninguna
fila lleva recuento al corte de hoy**, que vale **3388**. **NINGUNA CLASE SE MUEVE
AQUI: mover una clase es del RECOMPUTO**, y aqui se nombra y se para.

**LO QUE LA VARA NO CAZA VA PUBLICADO Y NO CONTADO**, que es lo que la propia vara
manda: cinco filas mencionan numerales de tres o cuatro cifras que la expresion no
recoge, entre ellos el **862** de la fila 4 y los **197, 222 y 463** de la fila 10.
**Y ahi mismo se ve por que la vara es de `puesto N` y no de numerales sueltos:**
el numeral **2026** aparece en cinco filas y **es el ano de una fecha**, mientras el
archivo tiene ademas un puesto 2026 que no tiene nada que ver.

#### LA CORRECCION DE MI PROPIO COMPUTO, DECLARADA Y NO TAPADA

**Mi primer extractor de filas cogia toda linea `| **N** |` posterior a la
cabecera y sacaba 32 filas**, que no son las de la TABLA VIVA sino las de esa
tabla **mas las de otras tablas de mas abajo del banco** (lineas 1056, 1674, 2024
y 2591 entre otras). **La TABLA VIVA tiene 11.** Con el extractor malo el reparto
salia **9 en pie, 0 caidas y 23 no medibles**, y con el bueno sale **6, 0 y 5**.
Arreglado acotando al bloque contiguo, **y el texto viejo queda escrito dentro del
fichero**.

#### LA PROPUESTA, QUE NO CIERRA NADA

**DOS COSAS SE PROPONEN Y NINGUNA SE ESCRIBE:**

1. **UNA CORRECCION DECLARADA MAS EN LA `verificacion` DE `OP-L-01`**, por el
   mismo carril del banco `9.10` y por adicion, que diga que el universo del
   instrumento paso de **11** a **27** cabeceras `LD` y que la comparacion
   resuelta pasa de **3** a **11**, con sus dos fechas de corte. **Es la misma
   especie que `OP-I-01` en la 201 y `OP-L-03` en esta vuelta.**
2. **LA VIGENCIA DE LA CABECERA DE LA TABLA VIVA**, que hoy dice **1157** y esta
   desmentida por **4** de sus propias **11** filas. **Actualizarla es tocar el
   banco, y eso no lo decide el ejecutor.**

**NINGUN campo `estado` se movio**, y este computo cambia **0 lineas** de
`docs/plan/OPERACIONES.jsonl`. **Lo adjudica el auditor.**

**DISCUTIBLE, MARCADO ANTES DE SABER SI ACIERTO:** sostengo que la discrepancia
de `las_once()` **no tumba la clausula 1**, porque en comparacion literal el
resultado sigue siendo **0** y eso es lo que la clausula pregunta. **Quien decida
que una excepcion mal contada si tumba la clausula tendra un argumento, y no soy
yo quien lo cierra.**
