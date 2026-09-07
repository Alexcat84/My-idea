# REPORTE DE LA VUELTA 196 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta196_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
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
> **VAN DOS SUB-TAREAS Y LAS DOS SON BLOQUEANTES, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> 1**, con las vueltas **195**. `AUDITOR.md` 6.2 pide **DOS vueltas
> seguidas** cerrando su propio reporte con `cerrar_reporte.py` para devolver el
> tope de cinco, **y con 1 el tope es de DOS**. **Lo que esta en mi mano y esta
> vuelta hace: sellar `docs/loop/SALIDA_V196_CERRAR_REPORTE.txt`**, con lo que la
> racha llega a 2 y el tope de cinco vuelve solo en la 197.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. Eso funciono en la 195 y **no se
> deshace**. **El desfase de calibrado se midio DENTRO del bloque de apertura y
> ANTES de la primera operacion.** Y el bloque `E` trae **el remedio de la caida
> `C.E1`** que el acta 196 me registra: **el nombre del instrumento de la racha ya
> no se teclea en la prosa**, sale de la constante que se ejecuta, y **se comprueba
> que existe y no mide cero bytes ANTES de correrlo**.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas en el orden del encargo para
> que la 197 no las redescubra:** que `cerrar_reporte.py` escriba su propia salida
> sellada; **el tope de 80 lineas del modo austero**, adjudicado en la `4.7` del
> acta 196 **en contra mia**, con el encargo de **medir este reporte por las dos
> varas y publicar las dos cifras**; la guarda de la `P.2` con su calibrado antes
> que sus dientes; **el desfase de `PATRONES_ACTA`, que lleva CUATRO encargos en
> primer lugar de la cola sin hacerse**; la fila de credito del acta con su rotulo
> impuesto por el instrumento; la guarda de codigo del hallazgo `5.3` del acta 194;
> `acumulan()` que lea la tabla; el cotejo de clon declarado; la excepcion que
> publica siempre su lista; el censo de arneses con carril de mutacion sin fichero
> propio; las ocho actas sin entrada propia en la serie (173 a 180); que el campo
> `evidencia` de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE
> MUEVE: sigue en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, y
> ahora tambien **LOS CUATRO PUESTOS QUE DOS LECTORES INDEPENDIENTES FALLARON**
> (`976`, `2428`, `2662`, `3173`), nombrados y medidos y **no resueltos, porque
> mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta196_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 195: `124a18a8`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 195: LA 194 REPRODUJO ENTERA Y SIN UNA SOLA CIFRA FALSA, Y EL REMEDIO DE CODIGO DE LA APERTURA FUNCIONO A LA PRIMERA.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y LLEVA SU FECHA DE CORTE.** La
  linea de arriba nombra el acta **195** porque `PATRONES_ACTA` pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la 196**. Es el `D.2` del
  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del
  acta 185, **y el encargo de esta vuelta lo deja EXPRESAMENTE FUERA y ademas lo
  nombra con su cuenta: CUATRO encargos en primer lugar de la cola sin hacerse**.
  Lo que si se puede contar: **7 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-06** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V196_HEAD_APERTURA.txt`: `85c3d52b`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `0bbe5f86`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **195**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 196`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 196 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y el cuerpo del acta se acota contando su primera linea con `grep -n` EN ESTA VUELTA, no por la linea que el encargo cita. La entrada registra, y cada cifra se cuenta del cuerpo acotado: LAS CATORCE ADJUDICACIONES `4.1` a `4.14`, Y LAS CATORCE A FAVOR (cuatro son las discrepancias de la ciega del propio auditor resueltas a favor del archivo, tres son mis preguntas `P.1`, `P.2` y `P.3` contestadas por extension citable, y siete son mis discutibles `D.1` a `D.7`), CERO EN CONTRA y es la SEXTA acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` el encargo que quema puestos de la ciega siguiente, `5.2` los mismos cuatro puestos fallados por dos lectores independientes, `5.3` la ciega que no puede alcanzar la clase de un puesto cuya correccion se apoya en una fusion planeada y no aplicada); UNA CAIDA MIA Y ES DE CIFRA PUBLICADA, NO DE REPORTE, la `C.E1`, con LA RACHA DE CIFRA PUBLICADA EN 1; MIS CUATRO CAIDAS DE METODO `C.1` a `C.4`, las cuatro cazadas dentro de la vuelta por guardas que yo mismo escribi y NINGUNA ACUMULA; UNA CAIDA PROPIA DEL AUDITOR, `C.A1`, DE METODO Y CON SU RACHA EN 2, con la escalada nombrada para la 197; y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos (60 aislados, 60 cotejados y DOS QUEMADOS, el `654` y el `719`) y la fila de caidas propias PARTIDA EN DOS. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. BLOQUEANTE, Y ES DEUDA SUYA QUE PAGA EL EJECUTOR CON EL INSTRUMENTO. `AUDITOR.md` 1.2: UNA discrepancia del auditor cayo FUERA de su marcado, el `2428`, asi que EL CREDITO DE SU TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE. El tramo y el doble estan CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v196_doble_para_la_197.txt`, para que no se elijan despues de mirar. SON CIENTO VEINTE PARES, y la serie medida va 30, 60 y ahora 120. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO se copia, con `evitar` cargado de TODO lo consumido y RECONTADO de sus ficheros en esta vuelta; el solape con el tramo y con el universo tiene que salir CERO POR CONSTRUCCION, no por suerte. (b) LEER LOS 120 A CIEGAS, tramo y doble, con `aislador_de_ciega.py`, y escribir las clases ANTES de abrir el destape. (c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no parafraseada, con sus precisiones `9.6.2` y `9.6.3`, Y CON LOS DOS ERRORES COMPARTIDOS PUESTOS DELANTE: la vara es EL SUELO Y NO EL TECHO (antes de aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA ya fijada), y LA SEMEJANZA DE LOS IDS NO DECIDE (`9.6.3` dice que el tamano del solape no decide y que se pesa el resto y en que lado). (d) NO SALTARSE LA `B` NI SOBRE EMITIRLA: el sesgo esta medido en las dos direcciones y las dos son perdida. (e) PUBLICAR EL COTEJO con sus cifras, cuantos coinciden, cuantos discrepan, y cuales caen dentro y fuera del marcado, con los discutibles marcados ANTES de saber si se acierta. (f) EL PUESTO INALCANZABLE A CIEGAS por el hallazgo `5.3` se DECLARA con su numero y su medicion y SALE DEL CREDITO, y NO se arregla | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
