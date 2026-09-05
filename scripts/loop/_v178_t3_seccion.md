### TAREA 3. LOS TRIANGULOS SE ANOTAN CON SU REGLA, NO SE MUEVEN

**CERO VEREDICTOS MOVIDOS, Y ESTA COMPROBADO Y NO PROMETIDO.** El sha256 de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` normalizado a LF sale
`ea6e850d331d14f01db1186a54f4913fa72eb2560a354430c5e6d047ff0d02be` **antes y
despues** de esta tarea, y el instrumento **cae en rojo si difieren**. El unico
fichero que se escribe es un registro PROPIO,
`docs/plan/OP_L_03_TRIANGULOS.jsonl`.

#### 3.a. LAS DOS REGLAS SON COMPATIBLES, Y ESO ES COSA JUZGADA

La `P.3` del reporte 177 queda adjudicada en el acta 177 punto 7.9. No hace falta
regla nueva: **la `9.6.1` del banco** (un nodo que es un paso de otro y NO TRAE
PROCEDIMIENTO PROPIO, REPITE) y **la correccion declarada del 13 ago 2026** (la
madre y su pieza de arenas, y la vara las separa) **parecen contrarias y no lo
son**. La condicion que las concilia la escribe la propia `9.6.1`: **si la pieza
trae procedimiento propio SE SEPARA; si es el paso dicho otra vez, REPITE.**

**Y NO SE RESUELVE MOVIENDO VEREDICTOS.** Que `P.10` bloquee la fusion de esos
actos es **el resultado correcto, no el defecto**: un acto que contiene a la vez un
nodo entero y una pieza suya llamada `A` no debe fundirse a ciegas, y el triangulo
es el aviso.

#### 3.b. LA ANOTACION, EN EL JSONL Y CON SU PRUEBA

Instrumento: `scripts/loop/vuelta178_tarea3_anotar_triangulos.py`. Salida:
`docs/loop/SALIDA_V178_T3_TRIANGULOS.txt`. Registro:
`docs/plan/OP_L_03_TRIANGULOS.jsonl`, **16 filas, 45.168 bytes en disco y 45.168
normalizados a LF**, sha256 en disco y sha256 en LF los dos
`28d4dd9d709046675d1b404bdce4fdf62a2d98c9e38085e9604f2a8f1414aca9`.

**LOS TRIANGULOS NO SE TECLEAN: SE ENCUENTRAN.** El instrumento enumera las ternas
de nodos VIVOS de cada acto del backlog y se queda con las que tienen dos lados `A`
y uno `D`. **La clase de cada lado sale de una de dos fuentes declaradas**: el
archivo de veredictos indexado POR EL PAR RESUELTO (`P.1`), o el registro de
lecturas de la 177 para los lados que aquella leyo como LECTURA DIRIGIDA y que por
la clausula de `OP-L-03` no entran en la cola.

**QUE REGLA GOBIERNA CADA LADO SE LEE DE SU RAZON ESCRITA, y es mecanico:** se
buscan en la razon las marcas literales de cada regla (`no trae procedimiento
propio`, `contado como nodo`, `REPITE` para la `9.6.1`; `LA MADRE Y SU PIEZA`, `la
vara las separa`, `CORRECCION DECLARADA el 13 ago 2026` para la del 13 ago).
**Ninguna razon se interpreta a ojo:** si un lado no trae marcas de ninguna de las
dos, se anota **SIN MARCA** y se dice.

**Y LA PRUEBA VA AL LADO, MEDIDA DEL GRAFO Y NO DE LA RAZON:** los
`pasos_accionables` de cada extremo, contados. Es la corroboracion independiente
de "trae procedimiento propio", y **la unica cifra de esta tarea que no sale de un
texto**.

| regla que gobierna el lado | lados |
|---|---|
| `banco 9.6.1`, la pieza NO trae procedimiento propio: REPITE | **22** |
| correccion declarada del 13 ago 2026, la pieza TRAE procedimiento propio: SE SEPARA | **2** |
| SIN MARCA DE NINGUNA DE LAS DOS | **24** |
| **total de lados** | **48** |

**El caso ejemplar sigue siendo el puesto 878**, cuya razon dice literalmente *"El
paso cuatro contado como nodo, y no trae procedimiento propio"*, contra los
puestos 530 y 863, cuya razon dice *"LA MADRE Y SU PIEZA DE ARENAS, y la vara las
separa"*. **Las dos varas, la misma condicion, resultados distintos porque los
sujetos son distintos.**

#### 3.c. NINGUN VEREDICTO SE MOVIO, Y LA CIFRA DE TRIANGULOS NO CUADRA CON LA MIA

**DISCREPANCIA DECLARADA, Y NO LA RESUELVO COPIANDO** (`EJECUTOR.md` 2). La 177
publico **CINCO** triangulos; este instrumento, corrido hoy sobre los MISMOS TRES
ACTOS, encuentra **NUEVE**. **Los cinco que nombre estan entre los nueve**: los
tres de `construccion_de_leverage`, el de `cash_burn` con
`validacion_hipotesis_ingresos` y `verificar_modelo_ingresos`, y el de las arenas.
**Los cuatro de mas son reales y yo no los vi**: tres mas en
`cash_burn_calculation` (los que entran `validar_modelo_financiero` y
`metrics_that_matter_framework`) y uno mas en `estrategia_de_innovacion_arenas`
(el que entra `seleccion_arenas_estrategicas`). **La causa es de metodo:** yo mire
los triangulos que tocaban los pares que estaba leyendo, y el instrumento enumera
TODAS las ternas del acto. **La cifra que vale es la del instrumento corrido hoy.**

#### 3.d. Y EL PATRON APARECE EN LOS ACTOS QUE LA TAREA 2 RE-MIDE, DICHO EN VOZ ALTA

| tramo | actos con triangulo | triangulos |
|---|---|---|
| en los actos QUE LA 177 LEYO | **3** | **9** |
| en los actos QUE LA 177 NO MIRO | **5** | **7** |
| **todo el backlog** | **8** | **16** |

**NO ES UNA CASUALIDAD DE TRES ACTOS, Y AHORA ESTA MEDIDO Y NO OPINADO.** En los
actos que la 177 nunca miro hay **SIETE triangulos mas**, en **cinco actos
distintos**: `colaboracion_cadena_suministro`,
`compra_por_precio_mas_bajo_como_error`, `creacion_option_pool`,
`disenar_tests_pass_fail` y `fase_diseno_prototipado_modelos`. **Es el sitio exacto
donde la lectura de a pares y la lectura por acto TIENEN que dar distinto**, que es
la razon entera por la que `P.5` existe.

**NINGUNO SE TOCA AQUI.** No hay encargo para moverlos y esta tarea prohibe
expresamente mover veredictos. Quedan anotados, con su regla y su prueba, en el
registro propio.
