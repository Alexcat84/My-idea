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

**EL VEREDICTO DE UNA LINEA: LAS CUATRO TAREAS CERRADAS: las dos guardas apagadas desde la 197 vuelven a morder con 26 de 26 en procesos distintos sobre un turno cerrado, el arnes de la nomina ya no se lleva la sede del turno y su caso rojo se prueba en dos pasos, 109 ejemplares del banco salen del universo de las ciegas computados y no tecleados con el carril corrido de verdad (61 pares contra 51), y el plan vuelve por la vara del expediente con los 18 pares reales de OP-L-03 re contados hoy, OP-L-02 declarada SIN DOCUMENTO QUE MEDIR y una discrepancia que no iba buscada en OP-I-01, que promete 323 entradas sobre un fichero de 672.**
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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 199`, y su salida
cruda vive en `docs/loop/SALIDA_V199_TALLADOR_CABECERA.txt` (2430 bytes en disco y 2410 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `04480e27` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 198, Y PARADA: LA 197 REPRODUCE ENTERA Y SIN UNA SOLA CIFRA FALSA, PERO DOS REMEDIOS ESCRITOS LLEVAN APAGADOS DESDE ELLA Y ME QUEMARON EL SUJETO A MI.'), HEAD real de apertura `17796e77` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `376037ac` (leido de `SALIDA_V199_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LAS DOS GUARDAS APAGADAS DE `apertura_del_auditor.py`. BLOQUEANTE, y es UNA DE LAS DOS UNICAS EXCEPCIONES a la moratoria de maquinaria (`AUDITOR.md` 6.3), porque el acta 198 ya la adjudico. Llevan apagadas desde la vuelta 197 y le quemaron el sujeto de la ciega al propio auditor. Son dos mitades y ninguna vale sin la otra: (1.a) REABRIR EL TURNO AL SELLAR, o no dejarlo cerrado para siempre; (1.b) `leer_reporte()` MIRANDO EL SELLO EN DISCO tambien cuando no hay `vuelta`, que es como `AUDITOR.md` manda llamarla. CADA MITAD CON SU CASO ROJO QUE MUERDA DE VERDAD, y con dos exigencias que no se negocian porque son justo por donde se escaparon: PROBADO EN PROCESOS DISTINTOS (no en la misma corrida, que es lo que las dejaba pasar) y SOBRE UN TURNO CERRADO. Se parte del ARNES QUE EL AUDITOR DEJO ESCRITO, `scripts/loop/_auditor_v198_guarda_muerta.py`; no se escribe uno nuevo desde cero | **CERRADA** | `SALIDA_V199_T1_GUARDAS_REVIVIDAS.txt` (26/26), y los cinco heredados corridos despues del cambio: `SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt` (52/52, tres casos anadidos) |
| **TAREA 2** | EL ARNES QUE BORRA LA SEDE DEL TURNO. BLOQUEANTE, y es LA OTRA EXCEPCION a la moratoria. `scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py` llama a `AP.olvidar_todo()` SEIS veces contra el modulo real SIN redirigir `AP.RUTA_DEL_TURNO`, asi que borra `docs/loop/_TURNO_DEL_AUDITOR.json` cada vez que corre. Se redirige `AP.RUTA_DEL_TURNO` en LAS SEIS llamadas, no en cinco: un arnes que borra la sede de verdad es peor que no tenerlo. TIENE FECHA porque la bateria corre esa nomina entera y su vuelta es la 200 | **CERRADA** | `SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` (0 fallos, sede intacta), `SALIDA_V199_T2_MUTACION_SEDE.txt` (9/9) |
| **TAREA 3** | LOS EJEMPLARES DEL BANCO FUERA DEL UNIVERSO DE LAS CIEGAS, COMPUTADOS DEL BANCO por el carril `--excluir` que `aislador_de_ciega.py` ya tiene. COMPUTADOS, NO TECLEADOS. Sale de la `P.3` del reporte de la 197, adjudicada por el auditor de la 198 por extension de la `4.4` del acta 197: el banco nombra sus ejemplares CON PUESTO Y CLASE, y la doctrina que se manda citar ENTREGA LA RESPUESTA. Le paso al ejecutor con el `1077` y al auditor con el `165`, y los dos se buscan como caso de control del computo | **CERRADA** | `SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` (5/5, 109 puestos con su linea del banco), `_v199_ejemplares_del_banco_exclusion.txt` (109 lineas), `SALIDA_V199_T3_CARRIL_CIEGA.txt` y `_CARRIL_DESTAPE.txt` (61 pares contra 51) |
| **TAREA 4** | RETOMAR EL PLAN, POR LA VARA DEL EXPEDIENTE Y NO POR EL CAMPO `estado`. Es la tarea que la moratoria viene a proteger: el plan es el trabajo, y las tres de arriba son la deuda que hay que pagar antes. En este orden: (4.a) `OP-L-03` CON SUS 18 PARES REALES, que es la que lleva mas vueltas aplazada; (4.b) `OP-L-01`; (4.c) `OP-L-02`, y aqui una advertencia del encargo: MEDIR SI SU DOCUMENTO EXISTE Y DECLARARLO, y si no existe SE DICE, no se da por hecho ni se fabrica; (4.d) `OP-I-01` | **CERRADA** | `SALIDA_V199_T4_LECTURA_DEL_PLAN.txt`, con `vuelta179_tarea2_cobertura_final.py` re corrido hoy (exitcode 0, 18 con lectura y 0 sin) |
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

**LA SEDE DE VERDAD NO SE MOVIO**, y va con su ruta delante y con las dos convenciones, porque la de bytes no esta fijada:
`docs/loop/_TURNO_DEL_AUDITOR.json` mide 789 bytes en disco y 789 normalizado a LF, con `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir del arnes.

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
`docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`, que cierra con
**`CIFRA fallos: 0`, VEREDICTO VERDE**.

**LA SEDE, CON SU RUTA EN LA MISMA LINEA QUE SU CIFRA:** `docs/loop/_TURNO_DEL_AUDITOR.json` mide 789 bytes en disco y 789 normalizado a LF, con `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir.

Los catorce casos que ese arnes ya probaba
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
| **M1** | solo la REDIRECCION | **la GUARDA muerde**: exitcode 1 y la sede queda intacta, `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280` |
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
| `docs/BANCO_DE_TEXTOS.md` medido hoy | 182228 bytes en disco y 182228 normalizado a LF, `sha256 disco 68557cd00a3124f4 y sha256 LF 68557cd00a3124f4`, 3119 lineas | la sellada de esta tarea |
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
**VERDE**. Su registro propio `docs/plan/OP_L_03_LECTURAS.jsonl` mide **51368 bytes en disco y 51368 normalizado a LF**, con `sha256 disco d93c59a86372cf50 y sha256 LF d93c59a86372cf50`. **Los 18 pares reales que el encargo nombra estan leidos, y
esta vuelta lo comprueba en vez de citarlo.**

#### 4.b `OP-L-01`, LAS ONCE LECTURAS DIRIGIDAS

**Las once se buscaron UNA A UNA** en `docs/plan/LECTURAS_DIRIGIDAS.md`: **11 de
11 estan**, de `LD-01` a `LD-11`. Su clausula de `verificacion` *"ninguna de las
once aparece en `INTRA_DOMINIO_VEREDICTOS.jsonl`"* **se midio y da 0**: ninguna se
colo en el archivo. Los otros dos documentos de su evidencia responden a su ancla:
`docs/INTRA_DOMINIO_INFORME.md` (943970 bytes en disco y 943970 normalizado a LF, 4 aciertos de cabecera con el 52) y
`docs/BANCO_DE_TEXTOS.md` (182228 bytes en disco y 182228 normalizado a LF, 1 acierto de `TABLA VIVA DE LOS PUROS`).

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
vez de ajustarse**. `docs/plan/INVENTARIO.jsonl` mide **584554 bytes en disco y 584554 normalizado a LF**, con `sha256 disco 69666b73339f2afe y sha256 LF 69666b73339f2afe`, y **672 filas no vacias**.

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
`docs/plan/10_INVENTARIO.md`, existe con **34258 bytes en disco y 33845 normalizado a LF**, que aqui NO coinciden y por eso se publican las dos, y **414 lineas**, con el
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

<!-- FIN ANEXO DE TAREAS -->

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA FILA DE ABAJO CITA EL FICHERO DEL QUE SALE Y SE RECONSTRUYO CONTANDO ESE
FICHERO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO, 26 ago 2026).

| que se cuenta | cuantos | de que fichero se cuenta |
|---|---:|---|
| casos del arnes de la TAREA 1 | **26 verdes, 0 rojos** | `SALIDA_V199_T1_GUARDAS_REVIVIDAS.txt` |
| casos de la mutacion del caso rojo de la TAREA 2 | **9 verdes, 0 rojos** | `SALIDA_V199_T2_MUTACION_SEDE.txt` |
| fallos del arnes reparado de la TAREA 2 | **0** | `SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` |
| casos del arnes del orden del turno, tras el cambio | **52 verdes, 0 rojos** | `SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt` |
| casos del computo de los ejemplares del banco | **5 verdes, 0 rojos** | `SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` |
| puestos que salen del universo de las ciegas | **109** | `_v199_ejemplares_del_banco_exclusion.txt` |
| pares elegidos por el aislador sin la lista y con ella | **61** y **51** | `SALIDA_V199_T3_CARRIL_CIEGA.txt` |
| pares reales de `OP-L-03`, con lectura y sin lectura | **18** y **0** | `SALIDA_V199_T4_LECTURA_DEL_PLAN.txt` |
| filas de `docs/plan/INVENTARIO.jsonl` contadas hoy | **672** | `SALIDA_V199_T4_LECTURA_DEL_PLAN.txt` |
| llamadas a `AP.olvidar_todo()` en el arnes de la TAREA 2 | **6** | `SALIDA_V199_APERTURA.txt`, bloque `H.1` |
| racha de cierres, contada del instrumento | **3**, vueltas 195, 196 y 197 | `SALIDA_V199_APERTURA.txt`, bloque `E` |
| entradas de la nomina de la bateria | **135**, y CALZA con el congelado | `SALIDA_V199_APERTURA.txt`, bloque `F` |
| arneses del censo fuera de la nomina, con vara 148 y sin vara | **1** y **61** | `SALIDA_V199_APERTURA.txt`, bloque `F` |

**LA CIFRA DE FUERA DE LA NOMINA VIAJA CON SU VARA Y SE PUBLICAN LAS DOS**
(adjudicacion `4.7` del acta 197). Y **el 1 con vara es NUEVO**: la 197 media 0.
**El que sobra es `vuelta197_tarea2_mutacion_orden_del_turno.py`**, escrito por la
197 y **nunca metido en la nomina porque `AUDITOR.md` 6.3 la congelo en 135**.
**Queda fuera por regla escrita, no por olvido**, y con el mismo motivo quedan
fuera los tres ficheros nuevos de esta vuelta.

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V199_APERTURA.txt`, bloque `C`, publica las dos cifras del estado
del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten LEIDAS de
ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**La apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `scripts/loop/apertura_del_auditor.py`, **que no se clona**: las dos guardas
  reencendidas y `_apuntar_sello()` extraida de `sellar()`.
- `scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py`: la redireccion de
  la sede que cubre sus seis llamadas.
- `scripts/loop/vuelta197_tarea2_mutacion_orden_del_turno.py`: sandbox completo y
  **tres casos anadidos**, de 49 a 52.
- `scripts/loop/`: el bloque de apertura y el esqueleto de esta vuelta, el arnes de
  la TAREA 1, la mutacion de la TAREA 2, el computo del banco, la lectura del plan,
  los dos parches de un solo uso y los cuatro cuerpos de tarea.
- `docs/loop/`: las salidas selladas de esta vuelta y el reporte.

**LO QUE NO SE TOCO, Y SE MIDE EN VEZ DE PROMETERSE:**

- **`dataset/` no se toco a mano.** El `numstat` contra `HEAD` sale con **0 filas**
  al entrar y **0 al salir**, y las dos cifras se publican:
  `SALIDA_V199_CICLO_NUMSTAT_APERTURA.txt` y `SALIDA_V199_CICLO_NUMSTAT_CIERRE.txt`
  traen solo el aviso de fin de linea de git, sin una sola fila.
- **Ningun veredicto se movio.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre en
  **4054129 bytes en disco y 4054129 normalizado a LF**, con `sha256 disco 0a77b5a35a962621 y sha256 LF 0a77b5a35a962621` (bloque `D` de la apertura), y **cierra en los mismos valores**.
- **Ningun `estado` del expediente se movio**, que es lo que la TAREA 4 dice con
  todas sus letras: `OP-L-01`, `OP-L-02`, `OP-L-03` y `OP-I-01` siguen en `LISTA`.
- **La nomina no se podo ni crecio:** 135 al entrar y 135 al salir.
- **La sede del turno del auditor no se movio:** `docs/loop/_TURNO_DEL_AUDITOR.json` mide 789 bytes en disco y 789 normalizado a LF, con `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir, medido tres veces por tres instrumentos distintos.
- **La bateria no corrio, y no tocaba**: su vuelta es la 200. Seccion 9.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`P.2` EL COMPUTO DE LA TAREA 3 CONTRA LA MORATORIA.** `AUDITOR.md` 6.3 prohibe
fabricar lectores nuevos y **la TAREA 3 no esta entre sus dos excepciones**. Lo que
la salva, y es mi lectura y puedo estar equivocado, es que el propio encargo manda
que la lista se COMPUTE y no se teclee, y computar necesita codigo. Se hizo con el
minimo posible: prefijo `_`, fuera del censo, fuera de la nomina, no vigila a nadie.
**Si el fundador lo lee como maquinaria, se retira.** Lo mismo vale para
`_v199_t4_lectura_del_plan.py` y para `_v199_t2_mutacion_sede.py`.

**`P.5` EL BLOQUE DE APERTURA Y EL ESQUELETO SE CLONARON, Y ESO TAMBIEN ES
CODIGO NUEVO.** Los lei como instancias por vuelta de un procedimiento que otras
reglas obligan a correr (la apertura antes de la primera operacion, el esqueleto al
abrir), y no como maquinaria nueva. **Va marcado porque la frontera es fina.**

**`P.6` LA MITAD `1.a` SE PUSO EN DOS SITIOS Y SOLO UNO SE VE SOLO.** El encargo
decia *"REABRIR EL TURNO AL SELLAR, o no dejarlo cerrado para siempre"*, con una
`o`. **Puse las dos**, y la mutacion demuestra que **la del sello no se ve mientras
la de la carga este puesta**. Elegi ponerla igual porque el encargo la nombra
primero y porque protege el caso en que nadie escriba antes del sello. **Si el
auditor lee que sobra, sobra, y se quita sin perder ninguna cifra.**

**`P.7` LA VARA DE `sello_mas_reciente_en_disco()` ES LA VUELTA MAS ALTA.** Es la
unica que se puede sostener sin adivinar, pero **es una eleccion mia**: un sello de
una vuelta baja escrito despues no se veria. Los sellos que hay en disco hoy van del
190 al 198 sin hueco salvo el 194, medido en esta vuelta.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` EL ARNES DEL AUDITOR DE LA 198 QUEDA CITADO Y NO CORRIDO.** Sus diez casos
estan escritos para salir verdes **sobre el agujero**, asi que ahora saldrian rojos,
y correrlo **pisaria `docs/loop/SALIDA_V198_GUARDA_MUERTA.txt`, que es su prueba
sellada**. Mi bloque `MUTACION TOTAL` reproduce sus cuatro medidas una a una. **No
esta en la nomina**, asi que la 200 no lo va a correr. **Si quiere que su arnes
quede invertido en vez de citado, lo decide el.**

**`P.3` LA LISTA DE EXCLUSION DEL BANCO ENVEJECE.** Son 109 al corte **2026-09-07**,
y el banco crece cada vuelta. El computo se puede volver a correr, pero **nadie ha
escrito que haya que correrlo**, y una lista vieja deja entrar al universo puestos
cuya clase ya esta publicada. **Si esto tiene que ser un paso fijo del sello de
apertura, es una linea de doctrina.**

**`P.4` LA EVIDENCIA DE `OP-I-01` PROMETE 323 ENTRADAS Y EL FICHERO TIENE 672.** No
es caida de nadie: la cifra de la ficha viaja con su corte, el `2026-08-11`, y el
fichero se movio despues. **Leo que necesita una CORRECCION DECLARADA por el carril
del banco `9.10`**, la misma via que `OP-L-01` uso en la vuelta 166 y `OP-L-03` en
la 72. **No la escribo yo**: tocar el expediente no esta en las cuatro sub-tareas de
este encargo, y una correccion de evidencia es adjudicacion.

**`P.8` `OP-L-02` SIGUE SIN DOCUMENTO Y ESO YA NO ES NUEVO.** Esta vuelta lo midio y
lo dice, que es lo que el encargo pedia. **Lo que nadie ha escrito es que se hace
con una ficha cuya evidencia entera es prosa**: ni se puede cerrar por lectura ni se
puede declarar incompleta sin recomputar. **Sigue en `LISTA` y sigue sin vara.**

## 7. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las cuatro sub-tareas se ejecutaron con reglas escritas, y lo que
no cabia en una regla vigente salio como pregunta en la seccion 6 en vez de
resolverse por mi cuenta. **La `P.2` es el caso mas cerca del borde**, y va marcada
como discutible y no como doctrina nueva porque **el propio encargo ordena la
tarea**: no invento una excepcion, leo una orden.

## 8. LO QUE LA 200 RECIBE

**LA 200 ES VUELTA DE BATERIA Y NO LLEVA NADA MAS**, por el encargo de esta vuelta:
*"LA VUELTA DE BATERIA SE CORRE EN LA 200, con la nomina CONGELADA en 135, para que
los remedios de las TAREAS 1 y 2 esten DENTRO cuando corra"*. **Los dos remedios
estan dentro:** `vuelta182_tarea2_mutacion_apertura_auditor.py` esta en la nomina
(linea 847 de `verificar_mutaciones_viejas.py`) y **ya no se lleva la sede por
delante**, y `apertura_del_auditor.py` es el modulo que media la nomina entera.

**LO QUE LA 200 SE VA A ENCONTRAR, Y SE DICE PARA QUE NO LO REDESCUBRA:**

- **la nomina mide 135 y CALZA con el congelado**, con `CASOS_DECLARADOS` en 2;
- **1 arnes del censo queda fuera de la nomina con la vara 148**, y es
  `vuelta197_tarea2_mutacion_orden_del_turno.py`. **La bateria no lo va a correr**,
  y eso es consecuencia del congelado y no un descuido de nadie;
- **los tres ficheros `_v199_*` de esta vuelta tampoco entran**, por el prefijo y
  por el congelado;
- **el siguiente libre de la serie es `R.60`**, con 0 colisiones, y **el acta 198
  todavia no esta registrada**: la registra quien la tome;
- **las cuatro fichas del plan siguen en `LISTA`**, con su saldo medido en la
  seccion 2 y las dos preguntas abiertas, `P.4` y `P.8`.

**Y SIGUEN FUERA, NOMBRADAS:** la guarda de codigo del hallazgo `5.3` del acta 194;
`acumulan()` que lea la tabla; el cotejo de clon declarado; las ocho actas sin
entrada propia en la serie (173 a 180); y **que hacer con las filas `B` del
archivo**.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 199 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V199_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio, y NO tocaba, y esta vez el motivo NO es la cadencia sino el encargo. Por AUDITOR.md 6.1 la cadencia de cinco desde la 194 ponia la bateria en esta vuelta, y el encargo de la 199 LA MUEVE A LA 200 con su motivo escrito en su propia linea: que los remedios de las TAREAS 1 y 2 esten DENTRO de la nomina cuando la bateria corra, porque correrla antes mediria una maquinaria que sabemos rota. Esta vuelta lo dice en su encargo, su sello de apertura lo escribe en el bloque I, y ese mismo bloque mide CERO ficheros SALIDA_V199_BATERIA_TRAMO_N.txt en disco al entrar, sobre 38 selladas de bateria que si hay en docs/loop/ repartidas entre las vueltas 176, 183, 189 y 194. El fichero docs/loop/SALIDA_V199_BATERIA.txt NO EXISTE y por eso mide cero, y esa medicion va aqui CON SU NOMBRE en vez de callarse: un hueco declarado no es un hueco escondido. Y LO QUE ESTA VUELTA SI MIDIO DEL RADIO DE LA BATERIA, sin correrla, y con su vara al lado: la nomina de verificar_mutaciones_viejas.py entra y sale en 135 entradas y CALZA con el congelado que manda AUDITOR.md 6.3, con CASOS_DECLARADOS en 2; el censo reconoce 196 arneses; LA VARA DEL CENSO VALE 148 y decide, y CON ESA VARA hay 1 arnes del censo fuera de la nomina, pero SIN VARA hay 61, y las dos cifras se publican juntas porque un numero solo al lado de un censo de 196 y una nomina de 135 se lee como cobertura total del censo y es cobertura desde la vara para arriba; hay ademas 0 entradas invisibles al censo y 0 entradas sin sujeto congelado. EL 1 CON VARA ES NUEVO Y SE NOMBRA: es vuelta197_tarea2_mutacion_orden_del_turno.py, escrito por la 197 y nunca metido en la nomina porque el congelado lo impide, asi que la 200 NO lo va a correr, y eso es consecuencia de una regla escrita y no un descuido. NO SE PODO NI UNA ENTRADA Y NO SE ANADIO NINGUNA: los tres ficheros nuevos de esta vuelta llevan prefijo de guion bajo y quedan fuera del censo y fuera de la nomina, por el mismo congelado. Y LO QUE ESTA VUELTA SI REPARO DEL RADIO DE LA BATERIA: el arnes de la nomina que borraba la sede del turno del auditor cada vez que corria, que era la P.2 del reporte de la 197 y la TAREA 2 de este encargo, ya redirige su sede en las SEIS llamadas y su caso rojo se probo por mutacion en dos pasos.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
