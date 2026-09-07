### TAREA 1, LOS REGISTROS. CERRADA. `R.59` ESCRITA, Y EL ACTA 197 OBLIGO SIETE LECTORES NUEVOS.

**Instrumento:** `scripts/loop/vuelta197_tarea1a_registrar_acta197.py`, que IMPORTA
la maquina de `R92`, `R94`, `R95` y `R96` y no copia nada.
**Ficheros de salida, y toda cifra de abajo se cuenta de ellos:**
`docs/loop/SALIDA_V197_T1A_REGISTRO_R59.txt` (14908 bytes),
`docs/loop/SALIDA_V197_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (15019 bytes),
`docs/loop/SALIDA_V197_T1A_MUTACION_REGISTRADOR.txt` (4085 bytes),
`docs/loop/SALIDA_V197_T1A_SIMULACION.txt`.

**EL CUERPO SE ACOTO EN ESTA VUELTA Y NO POR LA LINEA DEL ENCARGO:**
`R92.cuerpo_del_acta` da lineas **69341 a 69635**, **295 lineas**, sobre un
`ACTA_AUDITOR.md` de **4595886 bytes**. Las dos calzan con las que el encargo cita,
**y se dice que calzan porque se remidieron, no porque se heredaran**.

**EL NUMERO NO SE TECLEO:** serie recomputada de sus dos sedes, **50 entradas, 0
colisiones, 0 huecos, siguiente libre `R.59`**. Tras escribir: **51 entradas,
siguiente libre `R.60`, 0 colisiones y 0 huecos**.

**LO QUE LA ENTRADA REGISTRA, CADA CIFRA CONTADA DEL CUERPO ACOTADO:** **7**
adjudicaciones `4.1` a `4.7`, con las tres preguntas `P.1`, `P.2` y `P.3`
contestadas en la `4.3`, la `4.4` y la `4.5`; **4** hallazgos `5.1` a `5.4`;
**8** caidas en el cuerpo, **5 del auditor** (`C.A1` a `C.A5`) y **3 del ejecutor**
(`C.E1`, `C.E2`, `C.E3`); **0** del ejecutor de cifra publicada, con la fila del
acta en **0** y las dos rachas leidas de su celda derecha, **cifra publicada 1** y
**reporte 1**. Metrica: relecturas **332**, puestos **1.306**, dentro **60**, fuera
**179**, las cuatro leidas de las filas de la seccion 7 y no tecleadas.

**LOS SIETE LECTORES NUEVOS, CADA UNO CON LA CIFRA QUE LO OBLIGA.** Los seis
primeros salvan una PARADA sobre un acta correcta; el septimo no salva ninguna y
se escribe igual, y se dice.

| lector | sin el | con el |
|---|---|---|
| `caidas_en_titular_con_varias_claves()` | 6 claves, pierde `C.E3` y `C.A4`; el cuerpo daria 4 del auditor contra la fila que dice 5 | 8 claves, 5 del auditor, CALZA |
| `parte_de_la_caida_197()` | 2 `SIN DECIR` (`C.A3`, `C.A4`): el titular dice `MIAS` y el patron es `\bMIA\b` | 0 `SIN DECIR` |
| `cifras_de_la_fila_de_puestos_197()` | `('120', None, None, None)` | `('120', '120', '8', None)` |
| `cotejo_limpio_197()` | 0 aciertos, y con 8 quemados eso es PARADA | 112 en la linea 69416; `120 - 8 = 112` CALZA |
| `estado_de_la_adjudicacion_197()` | 5 de 7 en `SIN DECIR` | 0 |
| `claves_con_letra_de_la_fila()` | 0 claves: rama condicional SIN dientes | `C.E2`, `C.E3`, 2 contra fila 2, exigencia dura |
| `puestos_que_nombra_la_fila()` | la resta heredada da 1 | la fila nombra 5: `655`, `719`, `976`, `1809`, `1810` |

**NINGUNO ENSANCHA A OTRO: los seis corren DETRAS del heredado, entero y sin
tocar**, y la salida publica las dos lecturas una al lado de otra. Un texto mudo
sigue saliendo `SIN DECIR` y sigue haciendo PARAR, y eso esta probado.

**CASO POSITIVO POR MUTACION, CORRIDO ANTES DE ESCRIBIR NADA: 35 casos, 35 verdes,
0 rojos.** Cada lector se prueba sobre texto FABRICADO y **con el heredado corrido
sobre el mismo texto**, que es lo unico que convierte "hacia falta un lector nuevo"
en una medicion. Cuatro casos son de no ensanche: `MIAMI` no atribuye parte, la
fila de puestos VIEJA no cambia de valor, `EN CONTRA` y `A FAVOR` siguen ganando a
las seis marcas nuevas, y la fila `limpios` en minusculas NO casa con el patron del
cotejo limpio.

**IDEMPOTENCIA, MEDIDA EN BYTES Y NO AFIRMADA:** `docs/PENDIENTES.md` pasa de
**1063803** a **1072852** bytes al escribir; re corrido el instrumento, dice
*"el acta 197 YA TIENE ENTRADA, 2 lineas la nombran"*, no consume `R.60`, y la sede
**sigue en 1072852 bytes**. La entrada mide **9048 bytes, 152 lineas y 0 guiones
largos o medios**.

**DEUDA DE LA SERIE, REMEDIDA:** actas 173 a 196 sin entrada propia: **8** (173 a
180). No se repara aqui y no esta encargada.

**DISCUTIBLES MARCADOS, ESCRITOS ANTES DE SABER SI ACIERTO.**

**`D.1` DISCUTIBLE MARCADO. LA MARCA `NO MUEVE LA RACHA` LA ESCRIBI CONTRA UNA
LECTURA QUE YA SALIA BIEN.** Sin ella, el estado de la `4.3` salia igualmente
`A FAVOR`, pero del PARRAFO y **por la frase *"No adjudico a favor del bucle:
adjudico por la sede"***, o sea por un `A FAVOR` que en su sitio dice lo contrario
de lo que el lector entiende. Sostengo que un acierto por esa via no es un acierto,
y que anadir la marca del titulo lo endurece. **Lo discutible es que el resultado
publicado no cambia**, y una marca que no cambia ninguna cifra puede parecer
adorno. Las dos lecturas van publicadas en la tabla de la entrada.

**`D.2` DISCUTIBLE MARCADO. PUBLICO LA RESTA HEREDADA SABIENDO QUE SOBRE ESTA ACTA
NO SIGNIFICA LO QUE DICE.** `numeral - hallazgos` da **1**, y la fila nombra **5**
puestos que son los cinco discrepancias. La resta supone que la fila cuenta juntas
discrepancias y hallazgos, cosa que otras actas hacen y esta no. **No la retiro y
declaro la discrepancia**, por la regla de que una correccion que tapa lo que
corrige no se puede auditar. Lo discutible es si publicar una cifra que en esta
acta no significa nada es honestidad o ruido.

**`D.3` DISCUTIBLE MARCADO. `DE REPORTE` ES UNA MARCA DE ESPECIE MUY CORTA.**
La `C.E1` dice *"ES DE REPORTE, NO DE CIFRA"* y con las marcas de la 196 saldria
SIN ESPECIE. La marca solo se aplica a **la linea del titular**, nunca al parrafo,
que es lo que impide que una cita cualquiera de la palabra reporte atribuya especie.
Aun asi es la marca mas corta del vocabulario y podria casar de mas en un titular
futuro.
