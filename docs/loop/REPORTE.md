# REPORTE DE LA VUELTA 201 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta201_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA.** La
> 200 lo fue y cerro entera; `AUDITOR.md` 6.1 dice que la bateria corre **cada
> cinco vueltas**, en vuelta propia. Aqui la **seccion 9 cierra igual**, con el
> **HUECO DECLARADO Y MEDIDO** por el carril de `cerrar_reporte.py`, que lleva
> **su medicion, su atribucion y su corrida, o no vale**. El bloque `I` del sello
> de apertura ya lo midio: **0 ficheros `SALIDA_V201_BATERIA_TRAMO_N.txt`** y
> **`docs/loop/SALIDA_V201_BATERIA.txt` NO EXISTE**.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos**, y **esta
> vuelta NO TIENE NINGUNA EXCEPCION**. **La nomina queda CONGELADA EN 135**, y el
> bloque `F` del sello de apertura la midio contra ese congelado sin tocarla.
> **EL TRABAJO ES EL PLAN**, que es para lo que el bucle existe.
>
> **EL TOPE DE SUB-TAREAS VUELVE A CINCO, Y LA CIFRA QUE LO MANDA NO SE TECLEA.**
> El bloque `E` del sello de apertura de esta vuelta corrio el instrumento de la
> racha sobre el inventario ENTERO y **la racha de cierres vale 2**, con las
> vueltas **199, 200**. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
> sub-tareas cuando **DOS vueltas seguidas** cierran su propio reporte con
> `cerrar_reporte.py`, y con **2** **SE APAGA**. **Este encargo trae CUATRO,
> y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> publica la cifra de arneses del censo fuera de la nomina **con su vara al lado y
> las dos medidas**: con vara **148** salen **2** y sin vara salen
> **62**. **Esas son las cifras de HOY.**
>
> **LAS DOS PARADAS QUE LA 200 LEVANTO NO SE VUELVEN A LEVANTAR AQUI.** El acta
> 200 las adjudica en su `4.1` y su `4.2`: el rojo de los once tramos es **FALSO
> ROJO DE CENSO** y el bloque `F` de
> `vuelta185_tarea1c_mutacion_bateria_continuada.py` es **un arnes cuya premisa
> envejecio**. **Las dos reparaciones son de codigo y van a la auditoria integral:
> la moratoria las prohibe hoy.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina** (la poda se
> decide en la auditoria integral), ni **mover un solo campo `estado`** (la vara del
> trabajo pendiente es el instrumento, nunca el campo, por el recuadro de
> `AUDITOR.md` 0), ni **cerrar ninguna ficha por cuenta del ejecutor**: lo que estas
> tareas producen es **lectura medida**, y si de ella sale que una ficha esta
> cumplida, **se propone con su evidencia y lo adjudica el auditor**. **Y siguen
> fuera, nombradas para que la 202 no las redescubra:** la guarda de codigo del
> hallazgo `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de clon
> declarado; **QUE HACER CON LAS FILAS `B` DEL ARCHIVO**; y **los puestos que dos o
> tres lectores independientes fallaron**, nombrados y medidos y **no resueltos,
> porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` de `dataset/`, `web/`, `engine/`
> y `docs/plan/` se mide al entrar y al salir y **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta201_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 200: `405123f1`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 200, SIN PARADA: EL EJECUTOR CIERRA CON CERO CAIDAS Y LAS DOS PARADAS QUE LEVANTA SE ADJUDICAN CON REGLA ESCRITA; LAS CUATRO CAIDAS DE ESTA ACTA SON MIAS.'
```
- **EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y SE MIDE EN VEZ DE
  SUPONERSE.** `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la **200**,
  y **el acta que ORDENA esta vuelta ES la 200**: el bloque `H` del sello de
  apertura conto **1 acierto para la cabecera de la 200 y 0 para la 201**. El
  `D.2` del reporte de la 184 sigue vivo como especie, y aqui **no muerde**. Lo
  que si se sigue contando, porque es cifra de inventario y envejece sola: **11 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`, `REPORTE_V196.md`, `REPORTE_V197.md`, `REPORTE_V199.md`, `REPORTE_V200.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-07** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V201_HEAD_APERTURA.txt`: `405123f1`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `bc761e0e`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **200**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 201`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. (1.a) El **acta 200** entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, **computado y no tecleado**, y su cuerpo se acota EN ESTA VUELTA y no con las cifras del encargo. (1.b) **LA ENTRADA DE LA VUELTA 198**, por la adjudicacion `4.7` del acta 200: sigue sin entrada propia y sin reporte archivado, y su entrada **DECLARA LA AUSENCIA** con el instrumento que la midio. **NO SE FABRICA EL REPORTE.** (1.c) **UNA CORRECCION DE CITA, DE UNA LINEA, EN SU SEDE**: la seccion 8 de `docs/loop/reportes/REPORTE_V200.md` atribuye a `AUDITOR.md` 0 unas palabras que son del **acta 185**, y el aviso se anade **con el texto viejo entero y sin tachar**, por el carril del banco `9.10` mas `EJECUTOR.md` 8. **NO ES CAIDA Y NO SE COBRA.** Y **no se escribe ningun lector nuevo**: la moratoria lo prohibe | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA CORRECCION DECLARADA DE LA EVIDENCIA DE `OP-I-01`, adjudicada por el acta 199 en su `4.1`. La ficha promete **323** entradas y `docs/plan/INVENTARIO.jsonl` tiene otra cifra. La vieja **no es una mentira**: viaja con su fecha de corte, y lo que envejecio es la evidencia. La correccion va **EN SU SEDE**, con el texto viejo entero y sin tachar, y **las dos cifras con su fecha de corte cada una** (banco `9.21`). **NINGUNA DE LAS DOS SE TECLEA**: la del fichero se recuenta en esta vuelta y se pega su salida, la de la ficha se lee de la ficha y se cita por linea. Y se publica **el reparto por tipo recontado hoy**. **NINGUN CAMPO `estado` SE MUEVE** | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LA MEDICION DE `OP-L-02` CONTRA SU `verificacion`, NO CONTRA SU `evidencia`, adjudicada por el acta 199 en su `4.2`. Es la unica de las cuatro fichas reales **SIN DOCUMENTO QUE MEDIR**: su evidencia entera es prosa. Se lee la ficha entera, se **cita su `verificacion` por linea**, y se responde con medicion: **que pide exactamente, que parte se puede comprobar hoy contra el repo y que parte no**. Si su `verificacion` tampoco alcanza para ejecutarla sin decidir, **eso es un hallazgo medido y va como PARADA** (`AUDITOR.md` 3), no como improvisacion | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LAS OTRAS DOS FICHAS REALES, `OP-L-01` Y `OP-L-03`, LEIDAS CONTRA SU VARA. Es el trabajo que la moratoria `6.3` manda: **EL PLAN HASTA AGOTARLO**. **LO PRIMERO: la vara se vuelve a correr AQUI** con el corte de esta vuelta y **se publican sus cifras de hoy**; si discrepan de las del encargo, **la discrepancia se declara y no se resuelve copiando** (`AUDITOR.md` 1.1). Por cada ficha: **se cita su `verificacion` por linea**, se **miden sus documentos en bytes exactos de disco y LF** (`P.2`), y se dice **si el documento cubre lo que la ficha describe**, con la cita que lo sostenga o con el hueco nombrado. **NO SE MUEVE NINGUN `estado`** y **no se cierra ninguna ficha**: lo que produce esta tarea es **lectura medida** | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
