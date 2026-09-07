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
| **TAREA 2** | EL ORDEN DEL TURNO DEL AUDITOR PASA A CODIGO. BLOQUEANTE. Sale de la adjudicacion `4.5` del acta 197, que contesta mi `P.3` por extension de `AUDITOR.md` 1.2, y esta MEDIDO: el reporte de la 196 publico la clase de archivo de 8 de los 120 puestos que el auditor de la 197 acababa de sellar. Sobre `scripts/loop/apertura_del_auditor.py`, QUE NO SE CLONA: (a) `leer_reporte()` APUNTA SU TOQUE Y CAE EN ROJO si el turno tiene sello y no ha declarado sus clases todavia, con lo que el orden obligatorio pasa a ser `sellar()` -> clasificar -> `--declarar-clases` -> `leer_reporte()`, y un turno SIN sello sigue pudiendo leer el reporte. (b) EL FICHERO DEL TURNO SE CIERRA, que es el hallazgo `5.4`: un carril que lo cierre al declarar las clases dejando constancia, de forma que un turno nuevo empiece limpio SIN TENER QUE BORRAR NADA, con el sello en disco intacto y la guarda `b` de `sellar()` mirando el disco igual que antes. (c) LA GUARDA DE CODIGO DE LA `C.A1`, que va por su TERCERA acta seguida: comprueba que la cifra del marcador que un acta publica calza con una salida de `AP.marcador()` de esa misma vuelta, y CAE EN ROJO si esa salida no existe o no calza. CADA UNA DE LAS TRES LLEVA SU CASO POSITIVO POR MUTACION DELANTE, con nombre estable y salida sellada, y el caso rojo tiene que MORDER: sin el remedio la guarda deja pasar y con el no | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. Es deuda suya que paga el ejecutor con el instrumento. `AUDITOR.md` 1.2: CINCO discrepancias del auditor cayeron FUERA del marcado del archivo (`655`, `719`, `976`, `1809`, `1810`), asi que el credito de su tanda baja y el tramo se relee al doble. EL TRAMO Y EL DOBLE ESTAN CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v197_doble_para_la_198.txt`: SON 240 PARES, 120 del tramo y 120 del doble, y la serie medida va 30, 60, 120 y ahora 240. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y `puestos_de()`, `numeros_de()` y `UNIVERSO_CONSUMIDO` de `scripts/loop/vuelta196_tarea2_relectura_al_doble.py`, y NADA se copia; se RECOMPUTA el doble y se comprueba que calza con el sellado, ESQUIVANDO LA TRAMPA DE LA `C.A5` (los `_exclusion.txt` guardan enteros sueltos y se leen con `numeros_de()`). (b) LEER LOS 240 A CIEGAS con `aislador_de_ciega.py` y escribir las clases ANTES de abrir el destape. (c) LA VARA es `9.6.1` con `9.6.2`, `9.6.3` y la tabla de LOS DOS POLOS del `9.22`, y CON LOS DOS ERRORES DEL AUDITOR DELANTE: la vara es el SUELO y no el TECHO (familia con regla propia manda), y la contencion se mide SOBRE EL CONTENIDO y no sobre el contenedor. (d) NO SALTARSE LA `B` NI SOBRE EMITIRLA. (e) PUBLICAR EL COTEJO con sus cifras y los discutibles marcados ANTES de saber si acierto, MAS el reparto por puesto del literal `DISCUTIBLE MARCADO` que el hallazgo `5.2` obliga. (f) LOS PUESTOS QUE LA CIEGA NO PUEDE ALCANZAR se declaran ANTES de leer y salen del credito. (g) LOS QUEMADOS por el acta y por el reporte se declaran ANTES de leer y no entran al credito | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LAS DOS CIFRAS QUE VIAJAN SIN SU VARA. (a) LA SECCION 9 PUBLICA "0 ARNESES DEL CENSO FUERA DE LA NOMINA" SIN NOMBRAR LA VARA. No es caida (la frase nombra su fuente y esa fuente si lleva la vara, adjudicacion `4.7`), pero un `0` al lado de un censo y una nomina de tres cifras se lee como que la nomina cubre el censo entero, y no lo cubre. Esa cifra pasa a viajar SIEMPRE CON SU VARA, en el sello de apertura y en el reporte, y se miden LAS DOS: con vara y sin vara. (b) EL TOPE DE 80 LINEAS DEL MODO AUSTERO SE MIDE POR TRES VARAS Y LAS TRES SE PUBLICAN, por la adjudicacion `4.6`: total, escrita a mano (la vara que el acta 196 fijo en su `4.7`), y escrita a mano menos lo que otra regla obliga a escribir. EL TOPE NO SE AFLOJA Y LA EXCEPCION NO SE INVENTA: se publican las tres cifras para que el fundador decida sobre numeros, y si la tercera vara sigue por encima de 80 SE DICE CON ESAS PALABRAS y la pregunta queda escrita | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
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

<!-- FIN ANEXO DE TAREAS -->
