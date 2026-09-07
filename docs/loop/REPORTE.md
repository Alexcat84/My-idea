# REPORTE DE LA VUELTA 197 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta197_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA.** `AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026: la bateria corre **CADA CINCO VUELTAS** en una vuelta propia **que no
> lleva nada mas**, **la 194 la corrio entera por sus diez tramos** y **la proxima
> cae en la 199**. **La seccion 9 de este reporte cierra con el HUECO DECLARADO Y
> MEDIDO** por el carril de la TAREA 1.b de la vuelta 173, con su medicion, su
> atribucion y su corrida. **Un hueco declarado no es un hueco escondido.**
>
> **EL TOPE DE CINCO SUB-TAREAS VOLVIO SOLO, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> 2**, con las vueltas **195, 196**. `AUDITOR.md` 6.2 apaga el regimen
> temporal de dos sub-tareas cuando **DOS vueltas seguidas** cierran su propio
> reporte con `cerrar_reporte.py`, **y entonces vuelve el tope de CINCO**. **Este
> encargo trae CUATRO, y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y trae **el
> remedio de la TAREA 4.a en su bloque `F`**: la cifra de arneses del censo fuera
> de la nomina **ya no puede viajar sin su vara**, porque se miden **las dos**, con
> vara **148** salen **0** y sin vara salen **60**.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas para que la 198 no las
> redescubra:** el desfase de `PATRONES_ACTA`, que apunta al acta de `VUELTA - 1`
> cuando el acta que ORDENA esta vuelta es la 197; la guarda de codigo del
> hallazgo `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de clon
> declarado; las ocho actas sin entrada propia en la serie (173 a 180); el estado
> de `OP-L-02`, **que NO se mueve y sigue en `LISTA`**; **QUE HACER CON LAS FILAS
> `B` DEL ARCHIVO**; y **los puestos que dos o tres lectores independientes
> fallaron**, nombrados y medidos y **no resueltos, porque mover una clase es del
> RECOMPUTO**.
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta197_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 196: `85c3d52b`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 196: LA 195 REPRODUJO ENTERA EN CATORCE CIFRAS, PERO PUBLICA UNA RUTA QUE PROMETE PRUEBA SOBRE UN FICHERO QUE NUNCA EXISTIO.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y LLEVA SU FECHA DE CORTE.** La
  linea de arriba nombra el acta **196** porque `PATRONES_ACTA` pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la 197**. Es el `D.2` del
  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del
  acta 185, **y el encargo de esta vuelta no lo trae entre sus cuatro sub-tareas**.
  Lo que si se puede contar: **8 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`, `REPORTE_V196.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-06** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V197_HEAD_APERTURA.txt`: `548856b1`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `cc714417`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **196**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 197`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 197 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y el cuerpo del acta se acota contando su primera linea con `grep -n` EN ESTA VUELTA. La entrada registra, y cada cifra se cuenta del cuerpo acotado: LAS SIETE ADJUDICACIONES `4.1` a `4.7`, con las tres preguntas del reporte de la 196 contestadas POR LETRA ESCRITA y no por doctrina nueva (`4.3` la `P.1`, `4.4` la `P.2`, `4.5` la `P.3`); LOS CUATRO HALLAZGOS de la seccion 5 (`5.1` el reporte que quema la ciega del auditor por construccion, `5.2` el marcado de discutibles que no existe por debajo del puesto 2662, `5.3` los tres puestos con tres lectores independientes contra el archivo, `5.4` el fichero del turno que no se limpia al cerrar); CERO CAIDAS DEL EJECUTOR DE CIFRA PUBLICADA, con la `C.E1` de la 196 RE CLASIFICADA A MI FAVOR como caida de REPORTE en prosa de acompanamiento, que NO acumula; MIS DOS CAIDAS DE METODO; y CINCO CAIDAS PROPIAS DEL AUDITOR, `C.A1` a `C.A5`, todas de metodo y todas remediadas dentro de su vuelta, con la `C.A1` en su TERCERA acta seguida de la misma especie. Y LA METRICA DE CREDITO de la seccion 7 con sus cifras. EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues, y CADA LECTOR NUEVO LLEVA SU MUTACION DELANTE | **CERRADA** | `SALIDA_V197_T1A_REGISTRO_R59.txt`, `_MUTACION_REGISTRADOR.txt` (35/35), `_RECORRIDO_SIN_ESCRIBIR.txt` |
| **TAREA 2** | EL ORDEN DEL TURNO DEL AUDITOR PASA A CODIGO. BLOQUEANTE. Sale de la adjudicacion `4.5` del acta 197, que contesta mi `P.3` por extension de `AUDITOR.md` 1.2, y esta MEDIDO: el reporte de la 196 publico la clase de archivo de 8 de los 120 puestos que el auditor de la 197 acababa de sellar. Sobre `scripts/loop/apertura_del_auditor.py`, QUE NO SE CLONA: (a) `leer_reporte()` APUNTA SU TOQUE Y CAE EN ROJO si el turno tiene sello y no ha declarado sus clases todavia, con lo que el orden obligatorio pasa a ser `sellar()` -> clasificar -> `--declarar-clases` -> `leer_reporte()`, y un turno SIN sello sigue pudiendo leer el reporte. (b) EL FICHERO DEL TURNO SE CIERRA, que es el hallazgo `5.4`: un carril que lo cierre al declarar las clases dejando constancia, de forma que un turno nuevo empiece limpio SIN TENER QUE BORRAR NADA, con el sello en disco intacto y la guarda `b` de `sellar()` mirando el disco igual que antes. (c) LA GUARDA DE CODIGO DE LA `C.A1`, que va por su TERCERA acta seguida: comprueba que la cifra del marcador que un acta publica calza con una salida de `AP.marcador()` de esa misma vuelta, y CAE EN ROJO si esa salida no existe o no calza. CADA UNA DE LAS TRES LLEVA SU CASO POSITIVO POR MUTACION DELANTE, con nombre estable y salida sellada, y el caso rojo tiene que MORDER: sin el remedio la guarda deja pasar y con el no | **CERRADA** | `SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt` (49/49), `_T2B_CIERRE_DEL_TURNO_197.txt`, `_T2C_GUARDA_MARCADOR_ACTA_197.txt`, `_T2_QUIEN_BORRA_LA_SEDE.txt` |
| **TAREA 3** | LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. Es deuda suya que paga el ejecutor con el instrumento. `AUDITOR.md` 1.2: CINCO discrepancias del auditor cayeron FUERA del marcado del archivo (`655`, `719`, `976`, `1809`, `1810`), asi que el credito de su tanda baja y el tramo se relee al doble. EL TRAMO Y EL DOBLE ESTAN CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v197_doble_para_la_198.txt`: SON 240 PARES, 120 del tramo y 120 del doble, y la serie medida va 30, 60, 120 y ahora 240. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y `puestos_de()`, `numeros_de()` y `UNIVERSO_CONSUMIDO` de `scripts/loop/vuelta196_tarea2_relectura_al_doble.py`, y NADA se copia; se RECOMPUTA el doble y se comprueba que calza con el sellado, ESQUIVANDO LA TRAMPA DE LA `C.A5` (los `_exclusion.txt` guardan enteros sueltos y se leen con `numeros_de()`). (b) LEER LOS 240 A CIEGAS con `aislador_de_ciega.py` y escribir las clases ANTES de abrir el destape. (c) LA VARA es `9.6.1` con `9.6.2`, `9.6.3` y la tabla de LOS DOS POLOS del `9.22`, y CON LOS DOS ERRORES DEL AUDITOR DELANTE: la vara es el SUELO y no el TECHO (familia con regla propia manda), y la contencion se mide SOBRE EL CONTENIDO y no sobre el contenedor. (d) NO SALTARSE LA `B` NI SOBRE EMITIRLA. (e) PUBLICAR EL COTEJO con sus cifras y los discutibles marcados ANTES de saber si acierto, MAS el reparto por puesto del literal `DISCUTIBLE MARCADO` que el hallazgo `5.2` obliga. (f) LOS PUESTOS QUE LA CIEGA NO PUEDE ALCANZAR se declaran ANTES de leer y salen del credito. (g) LOS QUEMADOS por el acta y por el reporte se declaran ANTES de leer y no entran al credito | **CERRADA** | `SALIDA_V197_T3_SUJETO.txt`, `_T3_CIEGA.txt`, `_T3_MIS_CLASES.txt` (selladas antes), `_T3_COTEJO.txt` |
| **TAREA 4** | LAS DOS CIFRAS QUE VIAJAN SIN SU VARA. (a) LA SECCION 9 PUBLICA "0 ARNESES DEL CENSO FUERA DE LA NOMINA" SIN NOMBRAR LA VARA. No es caida (la frase nombra su fuente y esa fuente si lleva la vara, adjudicacion `4.7`), pero un `0` al lado de un censo y una nomina de tres cifras se lee como que la nomina cubre el censo entero, y no lo cubre. Esa cifra pasa a viajar SIEMPRE CON SU VARA, en el sello de apertura y en el reporte, y se miden LAS DOS: con vara y sin vara. (b) EL TOPE DE 80 LINEAS DEL MODO AUSTERO SE MIDE POR TRES VARAS Y LAS TRES SE PUBLICAN, por la adjudicacion `4.6`: total, escrita a mano (la vara que el acta 196 fijo en su `4.7`), y escrita a mano menos lo que otra regla obliga a escribir. EL TOPE NO SE AFLOJA Y LA EXCEPCION NO SE INVENTA: se publican las tres cifras para que el fundador decida sobre numeros, y si la tercera vara sigue por encima de 80 SE DICE CON ESAS PALABRAS y la pregunta queda escrita | **CERRADA** | `SALIDA_V197_APERTURA.txt` bloque F, `SALIDA_V197_T4_TRES_VARAS.txt`, `_T4_MUTACION_TRES_VARAS.txt` (8/8) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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

### TAREA 2, EL ORDEN DEL TURNO DEL AUDITOR PASA A CODIGO. CERRADA. 49 DE 49 EN VERDE, Y UNA CAIDA MIA QUE CAZO MI PROPIA GUARDA.

**Sobre `scripts/loop/apertura_del_auditor.py`, que NO SE CLONA.** Instrumentos y
ficheros de salida, **y toda cifra de abajo se cuenta de ellos**:
`docs/loop/SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt` (6491 bytes),
`docs/loop/SALIDA_V197_T2B_CIERRE_DEL_TURNO_197.txt` (3480 bytes),
`docs/loop/SALIDA_V197_T2C_GUARDA_MARCADOR_ACTA_197.txt` (2364 bytes),
`docs/loop/SALIDA_V197_T2_QUIEN_BORRA_LA_SEDE.txt`,
`docs/loop/SALIDA_MARCADOR_AUDITOR_V197.json` (102 bytes).

**(a) `leer_reporte()` APUNTA SU TOQUE Y CAE EN ROJO.** La decision vive en
`puede_leer_reporte()`, pura y probable sin escribir un fichero, y el orden
obligatorio pasa a ser `sellar()` -> clasificar -> `--declarar-clases` ->
`leer_reporte()`. **Un turno SIN sello sigue pudiendo leer el reporte**, y eso se
prueba en dos casos. Con sello y sin clases, `leer_reporte()` levanta
`ReporteFueraDeOrden`: es excepcion y no valor de vuelta **porque una cadena vacia
devuelta en silencio es la degradacion que el banco `9` prohibe**. La guarda vale
**entre procesos**, con el sello leido de DISCO, que es la unica forma de que no se
esquive arrancando otro.

**(b) EL FICHERO DEL TURNO SE CIERRA, Y CERRAR NO ES BORRAR.** `cerrar_turno()`
escribe en el fichero un registro `cerrados[vuelta]` con el motivo, la ruta de las
clases y **la bitacora tal como quedo**, y marca el bloque vivo como cerrado. Un
turno nuevo lo carga como CERRADO y **empieza limpio sin borrar nada**. Medido en
procesos de verdad: el turno 2 heredaba `git log, git status, REPORTE.md` y **no
podia sellar**; tras el cierre, el turno nuevo entra con la bitacora **vacia**, ya
**puede sellar**, el fichero **sigue en disco** y el **sello en disco no se toco**.
**LA GUARDA NO SE PIERDE AL LIMPIAR:** declarar dos veces la misma vuelta sigue
cayendo, ahora por `cerrados` y **tambien entre procesos**.

**(c) LA GUARDA DE LA `C.A1`, QUE VA POR SU TERCERA ACTA SEGUIDA.**
`sellar_marcador()` sella la salida de `AP.marcador()` de una vuelta, y
`guarda_del_marcador()` exige que la cifra que un acta publica calce con ella.
**Corrida sobre el acta 197 REAL**, no sobre un texto fabricado: cuerpo acotado en
esa corrida, lineas **69341 a 69635**, y `3388 filas; A 551, B 72, C 5, D 2760`
calzan con la salida sellada. **Y las CINCO mutaciones sobre el acta real cayeron
las cinco** (las filas y cada una de las cuatro clases), mas el caso de **no haber
salida sellada**, que es exactamente lo que la `C.A1` es.

**CASO POSITIVO POR MUTACION: 49 casos, 49 verdes, 0 rojos**, con las dos
direcciones corridas en cada pieza (**sin el remedio la guarda deja pasar, con el
no**) y con la sede de verdad del turno medida antes y despues.

**`C.1` CAIDA MIA, DE METODO, DECLARADA Y CAZADA POR MI PROPIA GUARDA.** La primera
version del arnes restauraba `AP.RUTA_DEL_TURNO` a su sede **antes** de llamar a
`AP.olvidar_todo()`, y `olvidar_todo()` **borra el fichero del turno**: el arnes se
llevo por delante `docs/loop/_TURNO_DEL_AUDITOR.json`, que media **329 bytes** con
`sha256` LF `7203f39fd7f5a54f`. **Lo cazo el ultimo caso del propio arnes**, el que
mide la sede antes y despues. El orden ya esta corregido con su motivo al lado, y
la sede se reconstruyo **por el carril** con `vuelta197_tarea2b_cerrar_turno_197.py`,
del contenido que el bloque `D.1` del sello de apertura publico **antes de la
primera operacion**. **El fichero nuevo no se hace pasar por el original: se
escribe CERRADO y lleva el motivo dentro**, y mide **801 bytes**, `sha256` LF
`69dfc4b6c6854d39`.

**HALLAZGO QUE NADIE ENCARGO, MEDIDO Y NO SUPUESTO.** Corridos **5** arneses de la
nomina que tocan este modulo, **1 BORRA la sede del turno**:
`scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py`, que llama a
`AP.olvidar_todo()` contra el modulo real **sin redirigir `AP.RUTA_DEL_TURNO` a un
temporal**. Los otros cuatro la dejan intacta byte a byte. **Es la misma leccion
que la 193 le aplico a `olvidar_todo()` y la 194 al arnes de la 192, y a este no se
le aplico nunca.** **NO LO REPARO**, porque reparar un arnes de la nomina no esta
encargado en esta vuelta. Consecuencia dicha sin adorno: **mientras eso siga asi,
cada corrida de la bateria vuelve a dejar sin sede el turno del auditor**, y el
remedio de la `2.b` no se puede ver en produccion aunque este entero en el codigo.
Los cuatro arneses heredados siguen en VERDE.

**DISCUTIBLES MARCADOS, ESCRITOS ANTES DE SABER SI ACIERTO.**

**`D.4` DISCUTIBLE MARCADO. `leer_reporte()` APUNTA SU TOQUE AUNQUE LUEGO CAIGA.**
Un intento bloqueado deja `REPORTE.md` en la bitacora sin que se haya leido nada.
Lo sostengo porque el modulo dice desde la 182 que `apuntar()` va **antes** de
hacer la cosa, y porque apuntar de mas **solo puede hacer las guardas mas
estrictas**. Lo discutible es que la bitacora deja de ser un registro de lo hecho y
pasa a serlo de lo intentado.

**`D.5` DISCUTIBLE MARCADO. LA CONSTANCIA DEL CIERRE VALE COMO PRUEBA DE QUE LAS
CLASES SE ESCRIBIERON.** Sin esa via, cerrar el turno bloqueaba **para siempre** la
lectura del reporte de esa vuelta, porque el sello sigue en disco y la memoria de
las clases se limpia. **Lo cazo el arnes y no yo**. Lo discutible es que un registro
del propio fichero del turno se acepte como prueba: quien pudiera escribir ese
fichero se auto concederia el permiso. **El sello en disco no tiene ese problema y
la ruta de clases si.**

**`D.6` DISCUTIBLE MARCADO. RECONSTRUI LA SEDE DEL TURNO QUE MI ARNES BORRO.** La
alternativa era dejarla sin existir y declarar la perdida. Reconstrui porque el
contenido estaba medido y sellado antes de la primera operacion, y porque un
auditor sin sede empieza distinto. Lo discutible es que **un fichero reconstruido
por el ejecutor esta en la sede que prueba el turno del auditor**, aunque se escriba
cerrado, con su motivo dentro y sin hacerse pasar por el original.

### TAREA 3, LA RELECTURA AL DOBLE DE 240. CERRADA. 207 DE 224 EN LA MITAD LIMPIA, Y ONCE DISCREPANCIAS FUERA DEL MARCADO QUE VUELVEN A DOBLAR EL TRAMO.

**Instrumentos y ficheros de salida, y toda cifra de abajo se cuenta de ellos:**
`docs/loop/SALIDA_V197_T3_SUJETO.txt`, `_T3_CIEGA.txt` (326299 bytes),
`_T3_DESTAPE.txt` (250425 bytes), `_T3_MIS_CLASES.txt` (43605 bytes) y
`_T3_COTEJO.txt`. **El orden fue: sujeto commiteado, clases commiteadas, y SOLO
DESPUES el destape.**

**(a) EL DOBLE RECOMPUTADO CALZA CON LA SELLADA.** `vecinos()` importada de la
182, y `puestos_de()`, `numeros_de()` y `UNIVERSO_CONSUMIDO` de la 196. Universo
**681** de **16** ficheros con el lector que le toca a cada uno, **300** con un
solo patron: la trampa de la `C.A5` medida y no creida, con **381** puestos de
diferencia. **561** por diferencia de conjuntos. Doble **120**, solape **0** con
el tramo y **0** con el universo **por construccion**. **Y HUBO QUE ESCRIBIR UN
LECTOR:** la sellada se TITULA `EL DOBLE DEL TRAMO...`, asi que su primera linea
tambien empieza por `EL DOBLE`; el lector de la 196 casa con el titulo y devuelve
**0** vecinos, o sea **un `NO CALZA` falso contra una sellada correcta**. Con el
lector que exige los dos puntos: **120**, y **calza**.

**(b) LOS 240 LEIDOS A CIEGAS**, uno por uno, con `aislador_de_ciega.py`.
**Mi reparto, sellado antes del destape: A 47, B 0, C 1, D 192.**

**(c) LA VARA** fue `9.6.1` con `9.6.2`, `9.6.3` y la tabla de LOS DOS POLOS del
`9.22`, citadas por numero. **Los dos errores del auditor fueron dentro del
criterio y sirvieron:** catorce de mis `A` las marque como CONTENCION MEDIDA SOBRE
EL CONTENIDO, y en cinco de ellas hay pasos repetidos **palabra por palabra** entre
los dos nodos.

**(e) EL COTEJO.**

| sobre que se mide | coinciden | discrepan |
|---|---:|---:|
| los **240** enteros | 215 de 240 | 25 |
| **los 224 LIMPIOS, y es la cifra que manda** | **207 de 224** | **17** |
| solo los 16 quemados, fuera del credito | 8 de 16 | 8 |

| | mio | del archivo |
|---|---|---|
| sobre los 240 | A 47, B 0, C 1, D 192 | A 35, B 3, C 1, D 201 |
| sobre los 224 limpios | A 38, B 0, C 0, D 186 | A 31, B 2, C 0, D 191 |

**DENTRO del marcado: 6** (`2668`, `2917`, `2922`, `3076`, `3094`, `3095`).
**FUERA del marcado: 11** (`165`, `207`, `210`, `662`, `724`, `880`, `886`,
`1218`, `1807`, `1808`, `2434`). **`AUDITOR.md` 1.2: el credito de mi tanda BAJA y
el tramo se relee AL DOBLE. La serie medida va 30, 60, 120, 240 y ahora 480.**

**Y LA `B` LA FALLE POR OMISION, EXACTAMENTE COMO ESCRIBI QUE PODIA PASAR ANTES DE
ABRIR NADA.** El fichero de clases dice, sellado: *"EMITO CERO B... si el archivo
trae alguna B en estos 240, la falle por omision"*. El archivo trae **3** en los
240 y **2** en la mitad limpia (`210` y `662`). **Sobre emiti `A` por 7 en la
mitad limpia**, 38 contra 31, que es la otra cara del mismo sesgo.

**(f) LOS INALCANZABLES A CIEGAS, contados ANTES de leer** por un barrido que no
devuelve ni la clase ni el texto de la razon: **14** citan un RACIMO, **6** una
CORRECCION DECLARADA, **20** en union. Sobre los 120 del auditor fueron 6 y 3.
**No se ensancho la lista blanca del aislador**, que es lo que la `4.4` prohibe.

**(g) LOS QUEMADOS: 16, y CATORCE se sellaron antes de leer**, nueve nombrados por
el encargo y **cinco anadidos por mi contra mi propio credito** (`616`, `2428`,
`2429`, `2430`, `2662`). **Los otros DOS se declararon TARDE, en el fichero de
clases, y eso es peor que declararlos antes**, asi que van con su nombre:

- **`654`.** Su clase de archivo me llego por la lista `QUEMADOS` de
  `scripts/loop/vuelta196_tarea2_relectura_al_doble.py`, **que lei ENTERO al
  clonarlo para escribir mi propio sujeto**, o sea antes de la ciega. **Es
  contaminacion mia por no comprobar si los quemados de la 196 caian dentro de MI
  universo.**
- **`1077`.** Es el **EJEMPLAR del banco `9.22`**, y el banco lo nombra con su
  clase `C` y con sus dos nodos. **El encargo me manda citar el `9.22`.**

**(e.bis) EL REPARTO DEL MARCADO, QUE EL HALLAZGO `5.2` OBLIGA A PUBLICAR.** De
los **240**, llevan `DISCUTIBLE MARCADO` **31**, y **los 31 son del 2662 para
arriba**: **0 marcados en los 177 puestos por debajo**, contra **31 de 63** por
encima. **El reparto sale igual que el del auditor.** Dicho sin deducir: **la
metrica de dentro-o-fuera del marcado NO ES COMPARABLE ENTRE TRAMOS**, porque una
discrepancia en el tramo bajo cae FUERA **por construccion**, no por ser peor.
**Nueve de mis once discrepancias de fuera del marcado estan por debajo del 2662.**

**DISCUTIBLES.** Los dos primeros van marcados **antes de saber si acierto**, en el
fichero de clases sellado; los otros dos son **posteriores al destape y se dicen
como tales**, que es la diferencia que hace que la marca valga.

**`D.7` DISCUTIBLE MARCADO ANTES DEL DESTAPE. EMITI CERO `B`.** Lo escribi con su
riesgo delante y sali perdiendo: el archivo tiene 2 en la mitad limpia. Sostengo
que la definicion que use (se pisan sin arista y sin que ninguno nombre al otro) es
la del banco, y que el problema es que **no la busque activamente en 240 pares**.

**`D.8` DISCUTIBLE MARCADO ANTES DEL DESTAPE. AMPLIE LOS QUEMADOS DE NUEVE A
DIECISEIS, y siete de los siete de mas los puse yo contra mi credito.** Lo
discutible es si un puesto que el acta nombra en una lista de "discrepancias
quemadas" sin publicar su clase esta de verdad quemado.

**`D.9` DISCUTIBLE, POSTERIOR AL DESTAPE Y SE DICE. LA CONTENCION LA APLIQUE MAS
DE LO QUE EL ARCHIVO LA APLICA.** De mis 38 `A` limpias el archivo confirma 31, y
las que fallo son casi todas contencion (`886`, `1218`, `1807`, `1808`, `2434`,
`2668`, `2922`, `3076`, `3094`, `3095`). **El remedio del `2838` funciono en el
`2838` y me hizo sobre emitir en otros diez.**

**`D.10` DISCUTIBLE, POSTERIOR AL DESTAPE Y SE DICE. LOS QUEMADOS ME SALIERON
PEOR QUE LOS LIMPIOS**: 8 de 16 contra 207 de 224. Un puesto quemado deberia ser
mas facil, no mas dificil. **La causa que sostengo: los quemados son en su mayoria
los puestos que el acta discute, o sea los dificiles, y saber que el archivo gano
NO es saber que clase puso.**

### TAREA 4, LAS DOS CIFRAS QUE VIAJAN SIN SU VARA. CERRADA.

**Ficheros de salida, y toda cifra de abajo se cuenta de ellos:**
`docs/loop/SALIDA_V197_APERTURA.txt` bloque `F`,
`docs/loop/SALIDA_V197_T4_TRES_VARAS.txt` y
`docs/loop/SALIDA_V197_T4_MUTACION_TRES_VARAS.txt`.

**(a) LA CIFRA DE FUERA DE LA NOMINA YA NO PUEDE VIAJAR SOLA.** El remedio va
**dentro del bloque `F` del sello de apertura**, que es donde nace la cifra, y de
ahi lo lee la cabecera del reporte por `varas_de_la_nomina()` del esqueleto, que
**CAE EN ROJO si el sello no trae las dos**. Medido en esta vuelta: censo **195**,
nomina **135**, invisibles al censo **0**, sin sujeto congelado **0**, y **fuera de
la nomina CON la vara 148: 0**, **SIN vara: 60**. Las dos van impresas **con el
numero de la vara al lado**, y el sello lista los diez primeros de los 60 para que
la cifra no viaje sola. **No era caida** y la `4.7` lo dice; lo que se arregla es
que un `0` junto a un 195 y un 135 **se lee como cobertura total del censo, y es
cobertura desde la vara para arriba**.

**(b) EL TOPE DE 80 LINEAS, MEDIDO POR LAS TRES VARAS.** Instrumento:
`scripts/loop/vuelta197_tarea4_tres_varas.py`, con **8 casos de mutacion, 8
verdes, 0 rojos**.

| vara | que cuenta | este reporte | el de la 196 |
|---|---|---:|---:|
| **V1 total** | `count(NL)` | **395** | **588** |
| **V1 total** | `len(split(NL))` | **396** | **589** |
| **V2 escrita a mano** | total menos las piezas TALLADAS | **380** | **562** |
| **V3 estrecha** | V2 menos lo que otra regla obliga | **344** | **267** |

*(Las dos columnas se midieron al anexarse esta tarea; el reporte sigue creciendo
hasta el cierre y sus cifras finales las remide el instrumento al cerrar.)*

**LA TERCERA VARA SIGUE MUY POR ENCIMA DE 80, Y LO DIGO CON ESAS PALABRAS**, que
es lo que el encargo manda: **344 lineas contra un tope de 80, 4.3 veces el tope**,
y en el reporte de la 196 **267, 3.3 veces**. **El tope no se afloja y no invento
ninguna excepcion.**

**CADA RESTA LLEVA AL LADO LA GUARDA QUE LA OBLIGA**, y **una seccion sin guarda NO
se resta**: eso es lo unico que impide que la vara estrecha sea una excusa, y va
probado con su mutacion (una seccion `## 99.` fabricada sin guarda NO baja la V3).
**Una marca de pieza tallada que aparezca dos veces tampoco se resta.**

**DISCREPANCIA DECLARADA Y NO RESUELTA COPIANDO.** La `4.6` del acta 197 dice que
el reporte de la 196 mide **318 por la vara estrecha del acta 196**. Mi V2 sobre
ese mismo fichero da **562**. La causa que sostengo, medida: **318 es el numero de
saltos de linea del reporte de la 196 ANTES de cerrarlo**, y sale literal de
`docs/loop/SALIDA_V196_CERRAR_REPORTE.txt` (*"CIFRA bytes: 22804 | saltos de linea:
318"*). **No es la vara estrecha: es el conteo total de un reporte a medio
escribir.** Publico las dos y no elijo.

**LA PREGUNTA QUE DEJO ESCRITA, Y NO LA CONTESTO YO.** El austero dice que
**recorta tinta, no control**. Las tres cifras muestran que lo que empuja el
reporte por encima del tope **no es prosa de acompanamiento sino piezas que una
guarda exige**: la seccion 9, la seccion 4, la tabla de tareas, la cabecera
tallada. **Las tres respuestas posibles son del fundador y ninguna mia:** subir el
tope, medirlo por la vara estrecha, o recortar de verdad lo que hoy es
obligatorio.

**`D.11` DISCUTIBLE MARCADO. LA V3 LA DEFINI YO.** El encargo dice *"escrita a mano
menos lo que otra regla obliga a escribir"* y nombra cuatro piezas entre
parentesis. Yo reste **ocho secciones**, cada una con la guarda que la busca por su
literal. **Lo discutible es que ampliar la lista de restas hace la V3 mas pequena y
me favorece**, aunque el criterio (tener guarda que la busque) sea comprobable.

<!-- FIN ANEXO DE TAREAS -->
