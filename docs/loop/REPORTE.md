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
| **TAREA 1** | LAS DOS GUARDAS APAGADAS DE `apertura_del_auditor.py`. BLOQUEANTE, y es UNA DE LAS DOS UNICAS EXCEPCIONES a la moratoria de maquinaria (`AUDITOR.md` 6.3), porque el acta 198 ya la adjudico. Llevan apagadas desde la vuelta 197 y le quemaron el sujeto de la ciega al propio auditor. Son dos mitades y ninguna vale sin la otra: (1.a) REABRIR EL TURNO AL SELLAR, o no dejarlo cerrado para siempre; (1.b) `leer_reporte()` MIRANDO EL SELLO EN DISCO tambien cuando no hay `vuelta`, que es como `AUDITOR.md` manda llamarla. CADA MITAD CON SU CASO ROJO QUE MUERDA DE VERDAD, y con dos exigencias que no se negocian porque son justo por donde se escaparon: PROBADO EN PROCESOS DISTINTOS (no en la misma corrida, que es lo que las dejaba pasar) y SOBRE UN TURNO CERRADO. Se parte del ARNES QUE EL AUDITOR DEJO ESCRITO, `scripts/loop/_auditor_v198_guarda_muerta.py`; no se escribe uno nuevo desde cero | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | EL ARNES QUE BORRA LA SEDE DEL TURNO. BLOQUEANTE, y es LA OTRA EXCEPCION a la moratoria. `scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py` llama a `AP.olvidar_todo()` SEIS veces contra el modulo real SIN redirigir `AP.RUTA_DEL_TURNO`, asi que borra `docs/loop/_TURNO_DEL_AUDITOR.json` cada vez que corre. Se redirige `AP.RUTA_DEL_TURNO` en LAS SEIS llamadas, no en cinco: un arnes que borra la sede de verdad es peor que no tenerlo. TIENE FECHA porque la bateria corre esa nomina entera y su vuelta es la 200 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LOS EJEMPLARES DEL BANCO FUERA DEL UNIVERSO DE LAS CIEGAS, COMPUTADOS DEL BANCO por el carril `--excluir` que `aislador_de_ciega.py` ya tiene. COMPUTADOS, NO TECLEADOS. Sale de la `P.3` del reporte de la 197, adjudicada por el auditor de la 198 por extension de la `4.4` del acta 197: el banco nombra sus ejemplares CON PUESTO Y CLASE, y la doctrina que se manda citar ENTREGA LA RESPUESTA. Le paso al ejecutor con el `1077` y al auditor con el `165`, y los dos se buscan como caso de control del computo | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | RETOMAR EL PLAN, POR LA VARA DEL EXPEDIENTE Y NO POR EL CAMPO `estado`. Es la tarea que la moratoria viene a proteger: el plan es el trabajo, y las tres de arriba son la deuda que hay que pagar antes. En este orden: (4.a) `OP-L-03` CON SUS 18 PARES REALES, que es la que lleva mas vueltas aplazada; (4.b) `OP-L-01`; (4.c) `OP-L-02`, y aqui una advertencia del encargo: MEDIR SI SU DOCUMENTO EXISTE Y DECLARARLO, y si no existe SE DICE, no se da por hecho ni se fabrica; (4.d) `OP-I-01` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
