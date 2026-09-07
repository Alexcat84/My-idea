# REPORTE DE LA VUELTA 200 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta200_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA ES LA VUELTA DE BATERIA, Y NO LLEVA NADA MAS.** `AUDITOR.md` 6.1 lo dice
> con estas palabras: la bateria corre **cada cinco vueltas**, en una **vuelta
> propia** con **su doble corrida, su reloj y su salida sellada**, y **nada de
> trabajo de plan al lado**. Por eso este encargo trae **DOS** tareas y la segunda
> es la bateria; y por eso **la correccion declarada de `OP-I-01` y la medicion de
> `OP-L-02`, que el acta 199 ya adjudico en su `4.1` y su `4.2`, VAN A LA 201** y
> no se pierden.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos**, y **esta
> vuelta NO TIENE NINGUNA EXCEPCION**, porque las dos de la 199 se consumieron.
> **La nomina queda CONGELADA EN 135**, y el bloque `F` del sello de apertura la
> midio contra ese congelado.
>
> **EL TOPE SIGUE SIENDO DE DOS SUB-TAREAS, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> 1**, con las vueltas **199**. `AUDITOR.md` 6.2 apaga el regimen
> temporal de dos sub-tareas cuando **DOS vueltas seguidas** cierran su propio
> reporte con `cerrar_reporte.py`, y con **1** no se apaga. **Este encargo
> trae DOS, y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> **es la medicion de la caida `C.1` del acta 199, tomada antes de mirar nada**: la
> cifra de arneses del censo fuera de la nomina **viaja con su vara y se miden las
> dos**, con vara **148** salen **2** y sin vara salen **62**.
> **Esas son las cifras de HOY, y la TAREA 1.a las publica con sus nombres.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina** (la poda se
> decide en la auditoria integral, no aqui), ni **el trabajo de plan**, que la
> cadencia de 6.1 manda dejar fuera de una vuelta de bateria. **Y siguen fuera,
> nombradas para que la 201 no las redescubra:** la guarda de codigo del hallazgo
> `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de clon declarado;
> las actas sin entrada propia en la serie; **QUE HACER CON LAS FILAS `B` DEL
> ARCHIVO**, que el hallazgo `5.1` del acta 199 vuelve a poner encima de la mesa; y
> **los puestos que dos o tres lectores independientes fallaron**, nombrados y
> medidos y **no resueltos, porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**. **La bateria lo mide ella sola once veces mas**,
> al entrar y al salir de cada tramo, con `guarda_y_restauracion()`.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta200_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 199: `69a16e29`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 199, SIN PARADA: LA VUELTA REPRODUCE ENTERA SALVO UN NUMERO QUE SU PROPIA VUELTA VOLVIO FALSO, Y MIS ONCE DISCREPANCIAS SALEN DE UNA DEFINICION QUE HEREDE SIN COMPROBAR.'
```
- **EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y SE MIDE EN VEZ DE
  SUPONERSE.** `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la **199**,
  y **el acta que ORDENA esta vuelta ES la 199**: el bloque `H` del sello de
  apertura conto **1 acierto para la cabecera de la 199 y 0 para la 200**. El
  `D.2` del reporte de la 184 sigue vivo como especie, y aqui **no muerde**. Lo
  que si se sigue contando, porque es cifra de inventario y envejece sola: **10 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`, `REPORTE_V196.md`, `REPORTE_V197.md`, `REPORTE_V199.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-07** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V200_HEAD_APERTURA.txt`: `69a16e29`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `5b9604ac`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **199**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 200`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 199 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y su cuerpo se acota con `grep -n` EN ESTA VUELTA. Y con la entrada van LAS TRES CORRECCIONES DE CIFRA que la seccion 3 del acta 199 levanta, cada una EN SU SEDE, por el carril del banco `9.10` mas `EJECUTOR.md` 8, CON EL TEXTO VIEJO ENTERO Y SIN TACHAR: (1.a) la `C.1`, LA QUE ACUMULA, el reporte de la 199 dice UN arnes del censo fuera de la nomina con la vara 148 y al commit de cierre son DOS, y NO SE CORRIGE TECLEANDO EL DOS sino volviendo a correr `V.arneses_que_faltan(vara=148)` y pegando su salida con su corte, mas la cifra SIN VARA que el reporte dio en 61; (1.b) la `C.2`, el literal `HUECO` en `docs/plan/10_INVENTARIO.md` sale 3 y no 4, y hay que decir si se corrige la cifra o la etiqueta; (1.c) la `C.3`, ese fichero tiene 413 lineas y no 414 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA BATERIA ENTERA, POR TRAMOS, Y CON LA TRAMPA MEDIDA DELANTE. Es la TAREA de la cadencia de `AUDITOR.md` 6.1 y la vuelta NO LLEVA NADA MAS. El lanzador es `scripts/loop/vuelta183_bateria_por_tramos.py` y NO SE CLONA. Sus dos mitades, las dos medidas por el auditor corriendolas: `--siguiente` dice que faltan el 10 y el 11 sobre NUEVE SALIDAS AJENAS de la corrida de la 183, y correr el tramo 1 PISA la sellada del 183. Por eso: LAS NUEVE SE PRESERVAN POR COPIA con sus bytes y su `sha256` medidos antes y despues; SE CORREN LOS ONCE TRAMOS, no los dos que `--siguiente` dice, porque `--plan` da ONCE hoy y el NUEVE de 6.1 se escribio con una nomina menor; CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR; una salida sellada de CERO BYTES no cuenta como hecha; y la bateria se declara corrida cuando los once tienen salida sellada del mismo calibre, y el calibre lo coteja `--componer` y no el criterio del ejecutor | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
