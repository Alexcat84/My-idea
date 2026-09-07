### TAREA 4. LOS REGISTROS `R.63` Y `R.64`, LAS DOS MAS VIEJAS DE LA DEUDA

**ADJUDICADA POR EL ACTA 201 EN SU `4.9`:** la deuda son **8 actas seguidas, las
173 a las 180**, y se pagan **DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA**.
**Esta tarea fue DETRAS del trabajo de plan y nunca delante**, que es lo que la
moratoria `6.3` manda al decir que **el trabajo es el plan hasta agotarlo**: las
tareas 1, 2 y 3 cerraron y se commitearon antes de que esta empezara.

**NINGUN LECTOR NUEVO.** Los cinco que el computo usa se **importan**, como hizo
la 201: `serie_de_registros.siguiente_libre()`, `R84.claves_entrecomilladas()`,
`R94.caidas_propias_entrecomilladas()`, `R92.caidas_por_lead_heredado()` y
`R92.titulo_de_la_entrada()`, mas `R95.cifras_de_la_fila_de_puestos()`. El
computo vive en `scripts/loop/_v202_t4_registrar_actas.py`, con **prefijo de
guion bajo**, fuera del censo y fuera de la nomina, y es **CLON DECLARADO** de
`scripts/loop/_v201_t1_registrar_actas.py` generado con
`scripts/loop/_gen_v202_t4.py`: de sus **636 lineas**, **515 vienen sin tocar de
la fuente** y **121 son nuevas**, contadas con `difflib` y no a ojo.

#### LA PRUEBA POR MUTACION, ANTES DE ESCRIBIR NADA

**No hay lector nuevo que mutar, y eso se declara en vez de fabricar un caso que
se apruebe solo** (`EJECUTOR.md` 1). Lo que si se vuelve a probar es **la guarda
de idempotencia**, porque esta vuelta escribe **dos entradas seguidas**, que es
el escenario exacto en que la guarda vieja cayo. **8 casos, los 8 pasan**, y la
guarda vieja corre **al lado y entera** sobre los mismos textos: **discrepa de la
nueva en 2 de los 8**, que son justo los dos que miran el **sujeto** y no el
numero. **La segunda pasada muta el valor esperado y los 8 CAEN.** El repo no se
toca: los casos se fabrican en un temporal y se limpia (`P.16`).

#### LAS DOS ACTAS, ACOTADAS EN ESTA VUELTA

| acta | lineas de inicio y fin, contadas hoy | lineas | reporte archivado |
|---|---|---:|---|
| **173** | 58941 a 59447 | 507 | `docs/loop/reportes/REPORTE_V173.md` **NO EXISTE** |
| **174** | 59448 a 59994 | 547 | `docs/loop/reportes/REPORTE_V174.md` **existe, 32568 bytes en disco y 32568 bytes normalizados a LF** |

`docs/loop/ACTA_AUDITOR.md` mide **4680981 bytes en disco y 4680981 bytes
normalizados a LF**. **La ausencia del reporte de la 173 se midio con
`os.path.isfile` y `os.path.getsize`** y **NO SE FABRICO**: el bloque `H.2` del
sello de apertura ya lo habia contado sobre el rango entero, y en la **168 a la
199 faltan DOS**, la **173** y la **198**. **El encargo mandaba comprobarlo y no
suponerlo: comprobado.**

#### LA PARADA, Y ES DE MEDICION: EL REPARTO NO SE PUEDE COMPUTAR HOY

**LOS CINCO LECTORES HEREDADOS DEVUELVEN CERO SOBRE LAS DOS ACTAS**, y **ese cero
es DE CONVENCION Y NO DE AUSENCIA**. Medido, no supuesto:

| lector | acta 173 | acta 174 |
|---|---:|---:|
| `R84.claves_entrecomilladas()` con prefijo `4.` | 0 | 0 |
| `R84.claves_entrecomilladas()` con prefijo `5.` | 0 | 0 |
| `R84.claves_entrecomilladas()` con prefijo `C.A` | 0 | 0 |
| `R94.caidas_propias_entrecomilladas()` | 0 | 0 |
| `R92.caidas_por_lead_heredado()`, ejecutor y auditor y huerfanas | 0, 0, 0 | 0, 0, 0 |

**POR QUE DAN CERO, LEIDO DEL ACTA Y NO DEDUCIDO.** Las actas **173 y 174 son
ANTERIORES a la 184** y escriben sus claves como **cabeceras markdown** `### 4.1`,
no como ``**`4.1` ...``, que es la forma que esos lectores buscan. Y ademas **su
estructura es otra**: en las dos, **la seccion 4 es LOS HALLAZGOS** (con `4.1` a
`4.5`), **LAS ADJUDICACIONES viven en la seccion 6** y **sin clave numerada**, y
**las caidas propias del auditor viven en la seccion 3**. En la convencion nueva
la seccion 4 es la de adjudicaciones y la 5 la de hallazgos: **estan cruzadas**.

**POR ESO EL TITULO HEREDADO NO SE USA, Y SE PUBLICA COMO CONTRASTE.**
`R92.titulo_de_la_entrada()` produce, sobre estas cifras, *"Registro de las cero
adjudicaciones numeradas, los cero hallazgos de la seccion 5, las cero preguntas
contestadas, las cero caidas propias del auditor y las cero caidas del ejecutor
del acta de la vuelta 173"*. **Ese titulo se leeria como que el acta no adjudico
nada, y es falso.** La vuelta 201 ya rechazo un cero de esta misma especie en su
entrada de la 198, con estas palabras: *lo dice en vez de publicar un cero que se
leeria como que el acta 198 no contesto ninguna pregunta*. **Aqui se sigue ese
precedente**: el titulo heredado va escrito en la salida **como contraste**, y el
titulo que se escribe dice que **los cinco numerales NO SON COMPUTABLES POR LOS
LECTORES HEREDADOS**.

**Y AQUI PARO, PORQUE SEGUIR SERIA DECIDIR Y NO MEDIR.** Computar el reparto de
estas dos actas pide **una de dos cosas y las dos me estan cerradas**: **un lector
para la convencion anterior a la 184**, que la moratoria `AUDITOR.md` 6.3
**prohibe fabricar**; **o decidir que seccion del acta vieja cuenta como cada
numeral**, que es **DECIDIR y no medir**, y `AUDITOR.md` 3 llama a eso **PARADA y
no improvisacion**. **No lo arreglo yo.**

**LO QUE SI SE PUDO MEDIR SI ENTRO EN LAS DOS ENTRADAS**, y no es poco: la cota
por linea, los bytes de la sede y del acta por las dos convenciones, la existencia
o ausencia del reporte con su medicion, y **la metrica de credito PEGADA ENTERA
con su numero de linea**, que es cita y no celda tecleada. De ahi salen, sin
teclear nada: el acta 173 declara en su linea 59360 **3 caidas propias del
auditor** y en su linea 59357 **8 puestos**, y el acta 174 declara en su linea
59909 **2 caidas propias del auditor** y en su linea 59906 **8 puestos**.

#### LAS DOS ENTRADAS, ESCRITAS Y RE-CORRIDAS

**Ningun numero esta tecleado:** `siguiente_libre()` se recomputa **antes de cada
entrada**, que es la unica forma de que el segundo numero no se teclee. Salieron
**`R.63` para el acta 173** y **`R.64` para el acta 174**, y viven en
`docs/PENDIENTES.md` en las **lineas 15766 y 15865**.

`docs/PENDIENTES.md` mide AL SALIR **1101602 bytes en disco y 1101602 bytes normalizados a LF**, y ANTES de estas dos entradas media **1091080 bytes en disco y 1091080 bytes normalizados a LF**, con un **crecimiento de 10522 bytes en disco y de 10522 bytes normalizados a LF**. **La segunda corrida sella IDEMPOTENTE**: **0 entradas escritas** y **crecimiento de 0 bytes en disco y de 0 bytes normalizados a LF**, con la guarda
diciendo *NO SE ESCRIBE: la entrada ya estaba* las **2** veces. Selladas en
`docs/loop/SALIDA_V202_T4_REGISTROS.txt` y
`docs/loop/SALIDA_V202_T4_REGISTROS_IDEM.txt`.

#### LA SERIE MEDIDA AL CIERRE, RECOMPUTADA Y NO HEREDADA

| lo que se mide | al abrir esta vuelta | al cerrar esta tarea |
|---|---:|---:|
| entradas de la serie | **54** | **56** |
| colisiones | **0** | **0** |
| huecos | **0** | **0** |
| siguiente libre | **R.63** | **R.65** |

Y **la deuda se remide al cierre en vez de heredarse**: de la **173** a la **200**
quedan **6 actas sin entrada propia**, y son las **175, 176, 177, 178, 179 y 180**.
**Eran 8 y quedan 6**, que es lo que dos por vuelta significa. `dataset/`,
`web/` y `engine/` siguen en **0 filas de `numstat`**: la unica sede que esta
tarea toca es `docs/PENDIENTES.md`.

**DISCUTIBLE, MARCADO ANTES DE SABER SI ACIERTO:** decidi **escribir las dos
entradas igualmente**, con el reparto declarado como no computable, en vez de
**no escribirlas y traer solo la parada**. Sostengo que una entrada que paga la
deuda con todo lo medible y **nombra en voz alta lo que no pudo medir** vale mas
que un hueco; **pero quien prefiera que una entrada sin reparto no se escriba
tendra un argumento, y no lo cierro yo.**
