### TAREA 4, CERRADA. EL PLAN, RETOMADO POR LA VARA DEL EXPEDIENTE

**LA PRUEBA VIVE EN `docs/loop/SALIDA_V199_T4_LECTURA_DEL_PLAN.txt`**, y toda
cifra de abajo se cuenta de ahi. **FECHA DE CORTE 2026-09-07**, leida de git en
esta corrida.

**QUE ES ESTA VUELTA DEL PLAN, DICHO EN UNA LINEA.** La vara
(`scripts/loop/vuelta150_3_relectura_expediente.py`) termina con una frase que
lleva vueltas escrita y que nadie habia contestado: **"Si cubre lo que la ficha
describe es LECTURA, y esta vara no la hace."** La vara sabe decir si el documento
que una ficha nombra EXISTE; **no sabe decir si dice lo que la ficha promete**.
**Esta tarea lo mide, ficha por ficha, contra el disco de hoy**, y la vara de cada
una **sale de su propia `evidencia` y `verificacion`**, leidas de
`docs/plan/OPERACIONES.jsonl` en esta corrida. **Ninguna promesa se teclea.**

**NINGUN `estado` SE MUEVE, Y NO ES UN OLVIDO.** El campo `estado` es justamente
lo que el encargo manda NO usar como vara, y moverlo seria cerrar por decreto lo
que aqui solo se mide. **Que un documento cubra lo que su ficha promete NO
significa que su mesa se hiciera bien:** significa que lo que la ficha escribio que
estaria, esta, y se puede abrir y contar. **Adjudicar el `estado` es del auditor.**

| ficha | saldo medido hoy |
|---|---|
| **`OP-L-03`** | **CUBIERTA EN SU LECTURA** |
| **`OP-L-01`** | **CUBIERTA EN SU DOCUMENTO** |
| **`OP-L-02`** | **SIN DOCUMENTO QUE MEDIR, y se declara** |
| **`OP-I-01`** | **CUBIERTA A MEDIAS**, y lo que falta va nombrado abajo |

#### 4.a `OP-L-03`, LA QUE LLEVA MAS VUELTAS APLAZADA

**EL INSTRUMENTO SE VOLVIO A CORRER HOY Y LA CIFRA NO SE HEREDO DE LA 179**
(`EJECUTOR.md` 2: un reporte anterior nunca es fuente de una cifra nueva).
`scripts/loop/vuelta179_tarea2_cobertura_final.py`, **exitcode 0**, al corte
`455384a1`:

| que cuenta | hoy |
|---|---:|
| actos que el instrumento da | **40** |
| filas de `docs/plan/OP_L_03_LECTURAS.jsonl` | **14** (6 de la 177, 8 de la 179) |
| pares distintos con clase escrita | **18** (8 de la 177, 10 de la 179) |
| **pares reales en todo el backlog** | **18** |
| de esos, **CON** lectura escrita en su acto | **18** |
| de esos, **SIN** lectura | **0** |

**La resta cierra: 18 mas 0 son 18, y los reales son 18.** El instrumento imprime
**VERDE**. Su registro propio mide **51368 bytes**, `sha256` LF
`d93c59a86372cf50`. **Los 18 pares reales que el encargo nombra estan leidos, y
esta vuelta lo comprueba en vez de citarlo.**

#### 4.b `OP-L-01`, LAS ONCE LECTURAS DIRIGIDAS

**Las once se buscaron UNA A UNA** en `docs/plan/LECTURAS_DIRIGIDAS.md`: **11 de
11 estan**, de `LD-01` a `LD-11`. Su clausula de `verificacion` *"ninguna de las
once aparece en `INTRA_DOMINIO_VEREDICTOS.jsonl`"* **se midio y da 0**: ninguna se
colo en el archivo. Los otros dos documentos de su evidencia responden a su ancla:
`docs/INTRA_DOMINIO_INFORME.md` (943970 bytes, 4 aciertos de cabecera con el 52) y
`docs/BANCO_DE_TEXTOS.md` (182228 bytes, 1 acierto de `TABLA VIVA DE LOS PUROS`).

**Y UN CONTRASTE QUE SE PUBLICA PARA QUE EL 11 NO SE LEA COMO EL TOTAL:** ese
fichero trae **68 identificadores `LD` distintos, del `LD-01` al `LD-154`**. **Las
once de `OP-L-01` son la PRIMERA TANDA, no el fichero entero.** Un `11 de 11` sin
esta linea al lado se leeria como que el fichero tiene once.

#### 4.c `OP-L-02`, Y AQUI EL ENCARGO TENIA RAZON

**SE MIDIO Y SE DICE, QUE ES LO QUE EL ENCARGO PIDE CON ESAS PALABRAS: `OP-L-02`
NO TIENE DOCUMENTO QUE MEDIR.** Su `evidencia` **entera** es una sola frase de
prosa, *"MEDIDO el 11 ago 2026: 205 pares fuera de cola, 11 leidos, 194
pendientes"*, y **nombra CERO ficheros**, contados por expresion regular sobre la
ficha de hoy. **No hay nada que abrir, y NO SE FABRICA NINGUNO:** fabricarlo seria
inventar la prueba que falta.

**LO QUE SI SE PUEDE MEDIR SIN FABRICAR NADA, Y SE MIDE.** Su `nota` describe una
segunda tanda de **16 lecturas** en tres grupos, y los tres tienen rastro en
`LECTURAS_DIRIGIDAS.md`, que es donde vivirian si vivieran: *cuadrantes de
mercado* **21** aciertos, *ecuacion de valor* **12**, *supervision humana de la
IA* **5**. **Eso NO cierra la ficha** y no se publica como si lo hiciera: un
acierto de expresion regular no es una lectura con su veredicto. Es lo unico que se
puede decir sin recomputar.

**Las cifras que su nota publica (205 fuera de cola, 126 esperando destejido o
cirugia, 79 que no esperan, y de esos 24 de mesa y 55 de resto) NO se re miden
aqui**, y el motivo se escribe: **re medirlas seria recomputo**, y esta vuelta no
lo trae encargado. **Son suyas, del corte 2026-08-11, y asi se citan.**

#### 4.d `OP-I-01`, Y AQUI SALE UNA DISCREPANCIA QUE NO ESTABA BUSCADA

**LA FICHA PROMETE 323 ENTRADAS. CONTADAS HOY: 672.** No calza, **y se declara en
vez de ajustarse**. `docs/plan/INVENTARIO.jsonl` mide **584554 bytes**, `sha256`
LF `69666b73339f2afe`, **672 filas no vacias**.

| tipo | la `nota` de la ficha (corte 2026-08-11) | contado del fichero hoy (2026-09-07) |
|---|---:|---:|
| actos | 221 | **556** |
| familias de ids | 53 | **54** |
| defectos | 14 | **19** |
| racimos | 13 | **13** |
| figuras | 12 | **20** |
| dominios | 10 | **10** |
| **total** | **323** | **672** |

**NO ES UNA CAIDA DE NADIE Y SE DICE ASI:** la cifra de la ficha **viaja con su
corte**, el `2026-08-11`, y el fichero se movio despues (git lo toco por ultima vez
el 4 sep 2026). Lo que hay es **una evidencia que envejecio**: quien lea la ficha
sin abrir el fichero se lleva `323`.

**LA CLAUSULA QUE SI SE PUEDE MEDIR SALE ENTERA EN VERDE:** *"toda entrada lleva su
`fecha_corte`"*, **672 de 672, 0 sin corte**. Y su vista humana,
`docs/plan/10_INVENTARIO.md`, existe con **34258 bytes y 414 lineas**, con el
literal `PROVISIONAL` **2** veces y `HUECO` **4**, que son las otras dos clausulas
de su `verificacion` con rastro.

**`P.4` DISCUTIBLE MARCADO, Y VA MARCADO ANTES DE SABER SI ACIERTO.** Leo que la
`evidencia` de `OP-I-01` **necesita una CORRECCION DECLARADA por el carril del
banco `9.10`**, la misma via que `OP-L-01` uso en la vuelta 166 y `OP-L-03` en la
72: el texto viejo entero arriba, sin tacharlo y sin clave nueva de esquema.
**No la escribo yo**, por dos motivos que digo: **tocar el expediente no esta en
las cuatro sub-tareas de este encargo**, y una correccion de evidencia es
adjudicacion. **La discrepancia queda medida y publicada, que es lo que si me
toca.**
