### TAREA 3, `OP-I-01` CLAUSULA 4: EL ALCANCE ESTABA ESCRITO, Y HAY UNA TERCERA CIFRA

**Salidas:** `docs/loop/SALIDA_V169_T3_OP_I_01.txt` (la medicion),
`docs/loop/SALIDA_V169_T3_FICHA.txt` (la correccion escrita) y
`docs/loop/RECOMPUTO_V169.jsonl` (la corrida de hoy).
**Instrumentos:** `scripts/loop/vuelta169_tarea3_op_i_01.py`,
`scripts/loop/vuelta169_tarea3_corregir_ficha.py` y `scripts/plan/recomputo_3388.py`.

**EL DISPARADOR SE LEYO EN SU SEDE ANTES DE APLICARLO, Y EL INSTRUMENTO PARA SI
NO LO ENCUENTRA.** `docs/plan/08_VERIFICACION.md`, **linea 397**, aparece **una
sola vez**, y se comprueba palabra por palabra que sigue diciendo `racimo`,
`acto`, `cobertura`, `9.26` y `paso 3`: los cinco, **True**.

**EL ALCANCE, PARTIDO EN DOS Y CONTADO** (seccion B de la salida):

| tipo | entradas | dentro del disparador |
|---|---:|---|
| `acto` | **556** | SI |
| `familia_de_ids` | **54** | NO |
| `figura` | **20** | NO |
| `defecto` | **19** | NO |
| `racimo` | **13** | SI |
| `dominio` | **10** | NO |

**DENTRO: 569 de 672. FUERA: 103 de 672.** Coincide con la adjudicacion 6.4, y
se cita como contraste y no como fuente.

**(3.a) LAS VIGENTES, RE MEDIDAS.** Cifras de la seccion F de la salida:
**348** re medidas, **333** cuyas cifras de cobertura CALZAN, **8** que DIFIEREN
y **7** SIN COMPONENTE. **333 mas 8 mas 7 son 348**, comprobado por el propio
instrumento antes de publicar.

**Y AQUI VA UNA CAIDA MIA, CAZADA MIDIENDO Y DECLARADA AUNQUE NO LLEGO A
PUBLICARSE.** La primera version de este instrumento partia las vigentes por
`fecha_corte` y daba **337**. **La vara es la marca `SUPERADA`, no la fecha:** la
llevan los **221** actos viejos uno a uno y **ningun racimo**, asi que once
racimos del corte `2026-08-11` estaban vivos y se quedaban fuera. **Son 348.** La
ficha ya escrita se restauro de git y se reescribio con la cifra buena, y el
motivo quedo escrito en el comentario del instrumento. **Lo que ensena:
`fecha_corte` dice cuando se midio, no si sigue valiendo.**

**(3.b) LO QUE EL DISPARADOR NO ALCANZA, DECLARADO Y NO RECOMPUTADO.** El paso 4
nombra *"cada racimo y cada acto"* y nada mas. Quedan fuera, con su cifra de hoy
y sin tocar: `familia_de_ids` **54**, `figura` **20**, `defecto` **19** y
`dominio` **10**. **Y una de esas cifras ya no cuadra con la nota de la ficha,
que declara 53 familias: hoy son 54.** No se recomputa: se declara.

**(3.c) LA DISCREPANCIA, POR EL CARRIL DEL 9.10, Y RESULTA QUE SON TRES CIFRAS Y
NO DOS.** La nota decia *"docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl mide 335
actos (280 CERRADOS, 55 ABIERTOS)"*. Contado hoy ese mismo fichero: **332 lineas,
278 CERRADOS, 54 ABIERTOS**. **Y ADEMAS, LO QUE NADIE HABIA CORRIDO:**
`scripts/plan/recomputo_3388.py`, ejecutado hoy sobre el grafo vivo, da **47
componentes (26 CERRADO, 21 ABIERTO)**.

| que se cuenta | cifra | corte |
|---|---:|---|
| lo que la nota declara del fichero de componentes | **335** (280 y 55) | vuelta 14 |
| el fichero de componentes, contado hoy | **332** (278 y 54) | 4 sep 2026 |
| `recomputo_3388.py` corrido hoy sobre el grafo vivo | **47** (26 y 21) | 4 sep 2026 |
| entradas de tipo `acto` VIGENTES en el inventario | **335** | 4 sep 2026 |

**LAS CUATRO SON CIERTAS Y CADA UNA ES DE SU CORTE, Y POR ESO NINGUNA SE COPIA
ENCIMA DE OTRA.** El 47 no desmiente al 332: **la campana FUNDIO**, y cada acto
fundido convierte sus pares `A` internos en auto-aristas que dejan de formar
componente. **La aritmetica lo sostiene sola:** el paso 1 de hoy mide **551 A
crudas, 398 colapsos y 149 pares distintos**; al sellarse el fichero los colapsos
eran **207** y los distintos **344**. De 344 salen 332 componentes; de 149 salen
47.

**Y LA FRASE VIEJA MEZCLABA DOS COSAS, QUE ES LO QUE LA CORRECCION SEPARA:** los
**335 actos SI existen**, pero en `INVENTARIO.jsonl`, no en el fichero de
componentes. **La nota atribuia al fichero de componentes una cifra que es del
inventario.**

**LA CORRECCION ESCRITA:** OCTAVA correccion de esa nota, **con el ordinal
CONTADO** de las siete marcas de correccion que la nota ya traia, no tecleado. Y
**se declara que esta nota NO TIENE contador mecanico** como la fila de los
colapsos: sus correcciones previas se escribieron en prosa, e inventarle un
contador retroactivo seria reescribir historia. La nota pasa de **7.437 a 10.928
caracteres**: solo crece. **18 claves antes y 18 despues, cero campos movidos
ademas de `nota`, y el `estado` sigue en `LISTA`.**
