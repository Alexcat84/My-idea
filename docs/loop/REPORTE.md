# REPORTE DE LA VUELTA 199 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta199_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA, Y NO POR LA CADENCIA SINO POR EL ENCARGO.** La
> cadencia de cinco de `AUDITOR.md` 6.1 la ponia aqui, y **el encargo de esta
> vuelta la MUEVE A LA 200 con su motivo escrito**: que los remedios de las
> TAREAS 1 y 2 esten **DENTRO** cuando la bateria corra, porque **correrla antes
> mediria una maquinaria que sabemos rota**. **La seccion 9 de este reporte cierra
> con el HUECO DECLARADO Y MEDIDO** por el carril de la TAREA 1.b de la vuelta
> 173, con su medicion, su atribucion y su corrida. **Un hueco declarado no es un
> hueco escondido.**
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos** salvo
> las TAREAS 1 y 2, que el acta 198 ya adjudico, y lo que una caida de dato exija
> con su cita. **La nomina queda CONGELADA EN 135**, y el bloque `F` del sello de
> apertura la midio contra ese congelado.
>
> **EL TOPE DE CINCO SUB-TAREAS VOLVIO SOLO, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> 3**, con las vueltas **195, 196, 197**. `AUDITOR.md` 6.2 apaga el regimen
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
> vara **148** salen **1** y sin vara salen **61**.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina**, ni **la
> bateria entera**, que cae en la 200. **Y siguen fuera, nombradas para que la 200
> no las redescubra:** la guarda de codigo del hallazgo `5.3` del acta 194;
> `acumulan()` que lea la tabla; el cotejo de clon declarado; las ocho actas sin
> entrada propia en la serie (173 a 180); **QUE HACER CON LAS FILAS `B` DEL
> ARCHIVO**; y **los puestos que dos o tres lectores independientes fallaron**,
> nombrados y medidos y **no resueltos, porque mover una clase es del RECOMPUTO**.
> **EL PLAN SI ENTRA**, y es la TAREA 4: esta vuelta es la que lo retoma.
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta199_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 198: `04480e27`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 198, Y PARADA: LA 197 REPRODUCE ENTERA Y SIN UNA SOLA CIFRA FALSA, PERO DOS REMEDIOS ESCRITOS LLEVAN APAGADOS DESDE ELLA Y ME QUEMARON EL SUJETO A MI.'
```
- **EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y SE MIDE EN VEZ DE
  SUPONERSE.** `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la **198**,
  y **el acta que ORDENA esta vuelta ES la 198**: el bloque `J` del sello de
  apertura conto **1 acierto para la cabecera de la 198 y 0 para la 199**. El
  `D.2` del reporte de la 184 sigue vivo como especie, y aqui **no muerde**. Lo
  que si se sigue contando, porque es cifra de inventario y envejece sola: **9 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`, `REPORTE_V196.md`, `REPORTE_V197.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-07** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V199_HEAD_APERTURA.txt`: `17796e77`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `9dc9caa0`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **197**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 199`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LAS DOS GUARDAS APAGADAS DE `apertura_del_auditor.py`. BLOQUEANTE, y es UNA DE LAS DOS UNICAS EXCEPCIONES a la moratoria de maquinaria (`AUDITOR.md` 6.3), porque el acta 198 ya la adjudico. Llevan apagadas desde la vuelta 197 y le quemaron el sujeto de la ciega al propio auditor. Son dos mitades y ninguna vale sin la otra: (1.a) REABRIR EL TURNO AL SELLAR, o no dejarlo cerrado para siempre; (1.b) `leer_reporte()` MIRANDO EL SELLO EN DISCO tambien cuando no hay `vuelta`, que es como `AUDITOR.md` manda llamarla. CADA MITAD CON SU CASO ROJO QUE MUERDA DE VERDAD, y con dos exigencias que no se negocian porque son justo por donde se escaparon: PROBADO EN PROCESOS DISTINTOS (no en la misma corrida, que es lo que las dejaba pasar) y SOBRE UN TURNO CERRADO. Se parte del ARNES QUE EL AUDITOR DEJO ESCRITO, `scripts/loop/_auditor_v198_guarda_muerta.py`; no se escribe uno nuevo desde cero | **CERRADA** | `SALIDA_V199_T1_GUARDAS_REVIVIDAS.txt` (26/26), y los cinco heredados corridos despues del cambio: `SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt` (52/52, tres casos anadidos) |
| **TAREA 2** | EL ARNES QUE BORRA LA SEDE DEL TURNO. BLOQUEANTE, y es LA OTRA EXCEPCION a la moratoria. `scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py` llama a `AP.olvidar_todo()` SEIS veces contra el modulo real SIN redirigir `AP.RUTA_DEL_TURNO`, asi que borra `docs/loop/_TURNO_DEL_AUDITOR.json` cada vez que corre. Se redirige `AP.RUTA_DEL_TURNO` en LAS SEIS llamadas, no en cinco: un arnes que borra la sede de verdad es peor que no tenerlo. TIENE FECHA porque la bateria corre esa nomina entera y su vuelta es la 200 | **CERRADA** | `SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` (0 fallos, sede intacta), `SALIDA_V199_T2_MUTACION_SEDE.txt` (9/9) |
| **TAREA 3** | LOS EJEMPLARES DEL BANCO FUERA DEL UNIVERSO DE LAS CIEGAS, COMPUTADOS DEL BANCO por el carril `--excluir` que `aislador_de_ciega.py` ya tiene. COMPUTADOS, NO TECLEADOS. Sale de la `P.3` del reporte de la 197, adjudicada por el auditor de la 198 por extension de la `4.4` del acta 197: el banco nombra sus ejemplares CON PUESTO Y CLASE, y la doctrina que se manda citar ENTREGA LA RESPUESTA. Le paso al ejecutor con el `1077` y al auditor con el `165`, y los dos se buscan como caso de control del computo | **CERRADA** | `SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` (5/5, 109 puestos con su linea del banco), `_v199_ejemplares_del_banco_exclusion.txt` (109 lineas), `SALIDA_V199_T3_CARRIL_CIEGA.txt` y `_CARRIL_DESTAPE.txt` (61 pares contra 51) |
| **TAREA 4** | RETOMAR EL PLAN, POR LA VARA DEL EXPEDIENTE Y NO POR EL CAMPO `estado`. Es la tarea que la moratoria viene a proteger: el plan es el trabajo, y las tres de arriba son la deuda que hay que pagar antes. En este orden: (4.a) `OP-L-03` CON SUS 18 PARES REALES, que es la que lleva mas vueltas aplazada; (4.b) `OP-L-01`; (4.c) `OP-L-02`, y aqui una advertencia del encargo: MEDIR SI SU DOCUMENTO EXISTE Y DECLARARLO, y si no existe SE DICE, no se da por hecho ni se fabrica; (4.d) `OP-I-01` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1, CERRADA. LAS DOS GUARDAS APAGADAS, VUELTAS A ENCENDER Y PROBADAS DONDE SE ESCAPARON

**LA PRUEBA VIVE EN `docs/loop/SALIDA_V199_T1_GUARDAS_REVIVIDAS.txt`, 26 casos,
26 VERDES, 0 ROJOS**, contados de ese fichero con `grep -E "CASOS:"` en esta
vuelta. El arnes es
`scripts/loop/vuelta199_tarea1_mutacion_guardas_revividas.py`, y **parte del que
el auditor dejo escrito**, `scripts/loop/_auditor_v198_guarda_muerta.py`, del que
copia el proceso hijo, el constructor de escenarios y la medicion de la sede.
**Lo que cambia son los esperados:** aquel salia verde probando que las guardas NO
mordian; este sale verde probando que SI muerden.

**LAS DOS EXIGENCIAS DEL ENCARGO SE CUMPLEN Y SE MIDEN:** cada paso corre en un
`subprocess` propio (**cuatro procesos distintos por escenario**), y todos los
escenarios se montan sobre un turno **CERRADO** (`vivo.abierto: false`), que es el
estado exacto en que la 197 dejo la sede.

**`1.a` REABRIR EL TURNO. La marca de cerrado SE CONSUME AL CARGARLA.** El
remedio va en `_cargar_turno()` (linea que reabre tras `_reiniciar_memoria()`) y
en `_apuntar_sello()`. **La memoria SIGUE reiniciandose**, o sea el turno nuevo
sigue empezando limpio, que era el remedio entero de la 197; lo unico que cambia
es que **el turno nuevo queda VIVO en vez de nacer muerto**.

**`1.b` `puede_leer_reporte()` MIRA EL DISCO TAMBIEN SIN `vuelta`**, por
`sello_mas_reciente_en_disco()`, que devuelve el sello de vuelta mas alta que hay
en el directorio. Con `vuelta` manda `vuelta`; sin ella manda el sello del disco;
y la clave del cierre (`_CERRADOS`) **se computa** en vez de exigirse por
parametro, para que la rama nueva no bloquee para siempre el reporte de una vuelta
cuyas clases si se declararon.

**LA MUTACION, QUE ES LO QUE HACE QUE ESTO SEA PRUEBA Y NO AFIRMACION.** Se copia
el modulo a un temporal, se le quitan los remedios por sustitucion de texto, y se
corren LOS MISMOS escenarios contra la copia mutilada. **Cada `viejo` se cuenta
antes: si no aparece exactamente una vez, el arnes cae sin medir nada.**

| mutacion | que quita | que pasa, medido |
|---|---|---|
| **A** | `_cargar_turno()` deja de reabrir | la bitacora ya NO acumula (`['git status', 'REPORTE.md']` en vez de los tres) y un toque anterior al sello ya NO cierra `puede_sellar()` |
| **B** | `_apuntar_sello()` deja de reabrir | con la `A` fuera y la `B` puesta el sello SOBREVIVE; con las dos fuera el sello SE TIRA |
| **C** | `sello_mas_reciente_en_disco()` devuelve vacio | `leer_reporte()` sin `vuelta` vuelve a DEJAR PASAR |
| **TOTAL** | las tres | reproduce las CUATRO medidas del auditor de la 198: sello no sobrevive, bitacora no acumula, cero prohibidos vistos, y la lectura pasa |

**DOS COSAS QUE ESTE ARNES APRENDIO EN ROJO CONTRA SI MISMO, Y VAN ESCRITAS
PORQUE SON LA MITAD QUE LO HACE VALER.** Su primera corrida salio **18 de 23**, y
los cinco rojos eran suyos y no del remedio:

1. **LA `B` NO SE VE SOLA.** Con la `A` puesta, `_cargar_turno()` ya reabre el
   turno antes de que la cola del sello llegue, asi que quitarle su linea no
   cambia nada medible. **Se mide contra la `A` ya quitada** (`mut_A` contra
   `mut_AB`). Un remedio que solo se ve cuando el otro falta sigue siendo un
   remedio, pero **decir que se prueba solo seria falso**.
2. **LA `C` NO SE VE EN EL ESCENARIO LARGO**, por el motivo simetrico: con la `A`
   puesta el sello sobrevive EN MEMORIA y la guarda cae por la memoria antes de
   mirar el disco. **Se mide en su escenario propio**, que es ademas el estado
   exacto del auditor de la 198: turno cerrado, memoria en blanco, y el sello en
   el disco al lado.

**Y UNA CAIDA MIA, `C.1`, DECLARADA SIN TAPAR LO QUE CORRIGE.** Mi primera version
del proceso hijo **COPIABA** dentro de si las cuatro lineas de la cola de
`sellar()`, igual que hacia el arnes del auditor. **Una copia no se entera de las
mutaciones que se le hacen al original**, asi que la MUTACION `B` salia ROJA
midiendo mi hijo y no el modulo. La salida honesta no era aflojar el caso: fue
sacar esas cuatro lineas a `_apuntar_sello()` en el modulo y **llamarla**. El
comportamiento de `sellar()` no cambia; lo que cambia es que ahora se puede probar.

**LO QUE NO SE AFLOJA, Y ES LA MITAD QUE IMPIDE QUE LA GUARDA SEA UNA PARED:** dos
casos propios miden que un turno cerrado **CON su constancia** (`cerrados[199]` con
su `ruta_clases`) **SI puede leer**, y que un turno **sin sello en ningun sitio**
tambien.

**LA SEDE DE VERDAD NO SE MOVIO:** `789 bytes, sha256 52a780c072700280` al entrar y
al salir del arnes.

**LOS CUATRO ARNESES HEREDADOS QUE MIRAN ESTE MODULO SE CORRIERON DESPUES DEL
CAMBIO**, y sus veredictos se leen de sus ficheros: `vuelta192_tarea4` VERDE,
`vuelta193_tarea4e` VERDE, `vuelta194_tarea2c` VERDE (14 de 14) y
`vuelta197_tarea2c` VERDE. El quinto, `vuelta197_tarea2_mutacion_orden_del_turno.py`,
**salio ROJO 48 de 49 y se resolvio sin aflojar nada**: va en su propio apartado
de abajo.

**`D.1` EL ROJO DEL ARNES DE LA 197, Y POR QUE NO ES UNA REGRESION.** Su caso
*"SIN sello: SI puede leer el reporte"* llamaba a `puede_leer_reporte()` a secas.
Ese arnes prometia en su docstring **"TODO SOBRE UN TEMPORAL"** y era **verdad a
medias**: redirigia `AP.RUTA_DEL_TURNO` pero **no `AP.LOOP`**. Mientras la guarda
solo mirara el disco CON `vuelta`, eso no se notaba; desde la `1.b` una llamada a
secas dentro de ese arnes leia **los sellos REALES de `docs/loop/`**. **La premisa
del caso, no su esperado, era lo que habia dejado de ser cierto.** Se arreglo
completando el sandbox y **anadiendo un caso en vez de sustituir ninguno**: el
original se mide ahora contra un directorio SIN sellos y sigue esperando `True`, y
al lado entra el que la `1.b` hace nacer, *"sin sello en memoria pero CON sello en
disco: ya NO puede"*, que espera `False`. **Ese arnes pasa de 49 a 52 casos, 52 en
verde, y ningun esperado se aflojo.**

**`P.1` UNA PREGUNTA QUE NO CONTESTO YO, Y VA MARCADA.** No corri
`_auditor_v198_guarda_muerta.py` despues del remedio, **a proposito**: sus diez
casos estan escritos para salir verdes sobre el agujero, asi que ahora saldrian
rojos, y correrlo **pisaria `docs/loop/SALIDA_V198_GUARDA_MUERTA.txt`, que es la
prueba sellada del auditor**. Su bloque `MUTACION TOTAL` de mi arnes reproduce sus
cuatro medidas una a una. **No esta en la nomina de la bateria** (medido: la nomina
no lo nombra), asi que la 200 no lo va a correr. **Si el auditor quiere que su
arnes quede invertido en vez de citado, eso lo decide el, no yo.**

### TAREA 2, CERRADA. EL ARNES QUE BORRABA LA SEDE DEL TURNO, Y LAS SEIS LLAMADAS

**LA CIFRA DE LAS SEIS NO SE HEREDO: SE CONTO HOY.** El bloque `H.1` del sello de
apertura de esta vuelta corrio el conteo ANTES de la primera operacion, y dice
**6 llamadas a `AP.olvidar_todo()`**, en las lineas **153, 175, 190, 213, 232 y
262**, y **CERO menciones de `RUTA_DEL_TURNO`** en todo el fichero. Calza con las
seis que el acta 198 nombra. Fuente: `docs/loop/SALIDA_V199_APERTURA.txt`.

**LA REPARACION CUBRE LAS SEIS, Y NO CINCO, PORQUE ES DE MODULO Y VA ANTES DE LA
PRIMERA.** `AP.RUTA_DEL_TURNO` se redirige a un `mkdtemp` justo despues del
`importlib.reload(AP)` y se restaura en el bloque final. Una redireccion por
llamada habria dejado seis sitios donde olvidarse de uno; una de modulo delante de
todas no los tiene. **Y se redirige tambien `AP.LOOP`**, por una razon que el
propio fichero declaraba mal y que va abajo.

**EL CASO ROJO ESTA DENTRO DEL ARNES Y ES SUYO:** mide la sede en bytes y `sha256`
al entrar y al salir, y **suma un fallo si se movio**. Ninguna de las dos cifras es
una constante literal: las dos salen de `sede_medida()`. Corrida de hoy, leida de
`docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`:
**`789 bytes, sha256 52a780c072700280`** al entrar y **lo mismo** al salir,
**`CIFRA fallos: 0`, VEREDICTO VERDE**. Los catorce casos que ese arnes ya probaba
siguen enteros: ningun esperado se aflojo y ningun escenario se quito.

**LA PRUEBA DE MUTACION DEL CASO ROJO, QUE `EJECUTOR.md` 1 EXIGE**, vive en
`docs/loop/SALIDA_V199_T2_MUTACION_SEDE.txt`, **9 casos, 9 VERDES**, y la corre
`scripts/loop/_v199_t2_mutacion_sede.py`. Va en fichero aparte y con prefijo `_`
por un motivo que se dice: **la mutacion es destructiva por naturaleza**, y la sede
esta en `.gitignore`, o sea que **git no la puede devolver**. Meterla dentro del
arnes de la nomina dejaria un arnes que destruye la sede cada vez que la bateria
pasa, que es exactamente lo que esta tarea repara. **No entra en la nomina**
(congelada en 135) y el censo no lo cuenta por el prefijo.

| paso | que se le quita al arnes | que se mide |
|---|---|---|
| **M1** | solo la REDIRECCION | **la GUARDA muerde**: exitcode 1 y la sede queda intacta, `sha256 52a780c072700280` |
| **M2** | la redireccion **Y** la guarda (el arnes tal como estaba antes de esta vuelta) | **la sede QUEDA PISADA**: `52a780c072700280` al entrar contra `31ddfaad65791b63` despues |
| **restauracion** | (nada) | la sede vuelve **byte a byte** y se **REMIDE**: `52a780c072700280` |

**`C.2` UNA CAIDA MIA EN ESTA MISMA PRUEBA, DECLARADA SIN TAPAR LO QUE CORRIGE.**
Mi primera version media **la EXISTENCIA** del fichero y esperaba que
desapareciera. Salio **ROJO**, y tenia razon: `olvidar_todo()` BORRA el fichero,
pero **el `apuntar()` siguiente LO VUELVE A CREAR** con la bitacora del arnes
dentro. **Medir la existencia daba VERDE sobre una sede PISADA**, que es el fallar
callado que el banco `9` prohibe. **La vara pasa a ser el contenido**, y con ella
el caso muerde. Lo que el acta 198 llama "borra la sede" es, medido de cerca,
**la borra y la reescribe con otro contenido**: el fichero sigue ahi y ya no es el
del auditor. **La diferencia importa** porque una guarda que solo mire si el
fichero existe habria dado verde.

**`D.2` Y UNA SEGUNDA CAPA QUE NO SABIA QUE ESTABA MIDIENDO, PUBLICADA COMO CASO.**
La `M1` se escribio esperando que borrara la sede, y **no la borra**: salta la
guarda que la propia reparacion dejo puesta (*"si la redireccion no se aplico, NO
se sigue: borraria la sede"*). **Eso no es un fallo de la mutacion, es una capa de
mas**, y por eso la mutacion se parte en dos en vez de darse por buena.

**`D.3` LA PROMESA DEL DOCSTRING QUE ERA FALSA, Y AHORA ES CIERTA.** Ese arnes
declara desde la vuelta 183 que **"este fichero NO ABRE `docs/loop/REPORTE.md` en
ninguna linea"**, y su bloque `B` llama a `AP.leer_reporte()`, que **lo abria**.
Con `AP.LOOP` redirigido al temporal, la afirmacion pasa a ser cierta y el bloque
`B` deja de depender de los sellos de la sede real. **Se declara aqui en vez de
corregirse callando**, porque una promesa de docstring que nadie mide es una cifra
sin vara.

**LA FECHA SE CUMPLE:** la bateria corre en la **200** con la nomina congelada en
**135**, y este arnes esta **dentro** de esa nomina (medido: `VMV.VIEJAS` lo nombra
en la linea 847 de `scripts/loop/verificar_mutaciones_viejas.py`). **Cuando la 200
lo corra, ya no se llevara la sede por delante.**

### TAREA 3, CERRADA. LOS EJEMPLARES DEL BANCO SALEN DEL UNIVERSO DE LAS CIEGAS

**LA LISTA SE COMPUTA Y NO SE TECLEA.** La escribe
`scripts/loop/_v199_t3_ejemplares_del_banco.py`, la procedencia entera vive en
`docs/loop/SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` (**5 casos, 5 VERDES**) y la
lista de enteros sueltos en
`docs/loop/_v199_ejemplares_del_banco_exclusion.txt`, **109 lineas**, contadas de
ese fichero.

**LA REGLA DE EXTRACCION VA DELANTE Y NO DETRAS, porque es lo unico auditable
aqui:** se busca un marcador (`puesto`, `puestos`, `par`, `pares`), detras se
consume una lista de numeros unidos por coma, `y`, `e` o `a`, la `a` entre dos
numeros se lee como rango cerrado, y los millares con punto se normalizan
(`2.117` es `2117`, que es como el banco los escribe). **Lo que la regla NO
hace:** no coge numeros sin marcador (un `9.21` de doctrina no es un puesto) ni el
numero que va DELANTE (*"los 240 pares"* es un conteo).

| cifra | valor | de donde sale |
|---|---:|---|
| banco medido hoy | 182228 bytes, `sha256` LF `68557cd00a3124f4`, 3119 lineas | `SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` |
| fecha de corte (banco `9.21`) | 2026-09-07 | leida de `git log -1 --date=short` |
| puestos cosechados del banco | **109** | mismo fichero |
| de esos, que NO existen en el archivo | **0** | mismo fichero |
| universo que queda | **3279 de 3388**, un 3.2 por ciento fuera | mismo fichero |
| rangos que el banco escribe | **1**, linea 2327, `2389 a 2400`, 12 puestos, EXPANDIDO | mismo fichero |

**EL CONTROL DEL ACTA 198 ES LO QUE IMPIDE QUE ESTO SE APRUEBE SOLO**, y no es un
`assert` contra si mismo: los dos numeros salen del acta y la lista sale del
banco. **El `1077` aparece en la linea 2543 del banco y el `165` en la 867**, las
dos leidas por el computo. Si cualquiera de los dos faltara, el fichero sale ROJO
y **no escribe la lista**.

**EL CARRIL SE PRUEBA CORRIENDOLO, no citandolo.** Misma banda del archivo, con y
sin la lista, en esta vuelta:

| corrida | pares elegidos | fugas del destape |
|---|---:|---:|
| `--desde 150 --hasta 210` | **61** | 0 |
| la misma **`--excluir`** con las 109 | **51** | 0 |

Los **diez** que se caen son `156`, `165`, `176`, `185`, `192`, `197`, `200`,
`201`, `206` y `209`, y **los diez estan nombrados en el banco con su linea**.
`aislador_de_ciega.py` sale **VERDE** en las dos corridas, y su guarda de puestos
inexistentes no salto ni una vez, que es la comprobacion de que las 109 son
puestos de verdad.

**`C.3` LA ERRATA QUE EL CONTROL CAZO, DECLARADA SIN TAPAR LO QUE CORRIGE, Y ES LA
QUE MAS PESA DE ESTA TAREA.** Mi primera version del marcador escribia `pares?`,
que en una expresion regular **no es "par o pares"**: es `par` + `e` + `s`
opcional, o sea **exige la `e`**. Con eso `puesto` y `puestos` entraban y **`par`
a secas no**, y el `165` del auditor, que el banco escribe como *"La nota del par
165"*, se quedaba fuera. **El caso de control salio ROJO y por eso se vio.** Sin
ese control la lista se habria publicado con **82** en vez de 109 y con cara de
completa.

**`C.4` Y DOS RECORTES MAS DE LA MISMA ESPECIE, LOS DOS MEDIDOS Y NO
SOSPECHADOS.** La cosecha empezo mirando **linea a linea**, y el banco parte sus
enumeraciones: en su linea 2327 escribe *"Los puestos 2.389 a"* y **el `2.400`
esta en la linea de abajo**, ademas **detras de la marca de cita `>`**. Cada uno
de los dos descuidos se llevaba puestos por delante en silencio, y la serie de la
cifra lo dice sola: **82, luego 96, luego 109**. Se arreglaron mirando la linea y
la siguiente, y quitandole a la siguiente su `>`. **Lo que decide sigue siendo el
mismo `numeros_tras()`:** entre dos numeros solo puede haber separadores de lista,
asi que un numero de abajo entra unicamente si el de arriba quedo colgando, y un
punto o cualquier palabra corta la union.

**`P.2` DISCUTIBLE MARCADO, Y VA MARCADO ANTES DE SABER SI ACIERTO.** La moratoria
de `AUDITOR.md` 6.3 prohibe fabricar lectores nuevos y **la TAREA 3 no esta entre
sus dos excepciones**; lo que la salva es que el propio encargo manda que la lista
se COMPUTE y no se teclee, y computar necesita codigo. **Lo lei asi y puedo estar
equivocado.** Se hizo con el minimo posible: prefijo `_` para que el censo de
arneses no lo cuente, **fuera de la nomina** (congelada en 135), no vigila a nadie
y no se cita como guarda. **Si el fundador lo lee como maquinaria, se retira y la
lista queda como fichero muerto con su fecha de corte.**

**`P.3` UNA SEGUNDA PREGUNTA QUE TAMPOCO CONTESTO YO.** La lista **envejece**: el
banco crece cada vuelta y estas 109 son las del corte **2026-09-07**. El computo se
puede volver a correr, pero **nadie ha escrito que haya que correrlo**, y una lista
de exclusion vieja deja entrar al universo puestos cuya clase ya esta publicada.
**Si esto tiene que ser un paso fijo del sello de apertura, es una linea de
doctrina y no la escribo yo.**

<!-- FIN ANEXO DE TAREAS -->
