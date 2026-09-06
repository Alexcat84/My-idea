# REPORTE DE LA VUELTA 195 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta195_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
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
> **VAN CUATRO SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de CINCO esta ganado y
> **la cifra se conto del instrumento en esta vuelta**, no se heredo: el bloque `E`
> del sello de apertura corrio `scripts/loop/vuelta193_racha_de_cierres.py`
> sobre el inventario ENTERO. `AUDITOR.md` 6.2 pedia DOS vueltas seguidas cerrando
> su propio reporte con `cerrar_reporte.py`.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. Esas eran las dos caidas `C.1` y
> `C.2` que el reporte de la 194 se declaro en su seccion 8.1, heredadas dos
> vueltas seguidas por clonar el bloque sin leer esa seccion, que es lo que su
> propia `C.3` nombraba como causa. **Aqui se leyo la seccion 8.1 ANTES de clonar.**
> **El desfase de calibrado se midio DENTRO del bloque de apertura y ANTES de la
> primera operacion.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas para que la 196 no las
> redescubra:** el desfase de `PATRONES_ACTA`, **que el encargo de la 195 pasa
> EXPRESAMENTE a la 196 y EN PRIMER LUGAR DE LA COLA**, con su motivo dicho (las
> cuatro de hoy atacan causas y esa es cosmetica de cabecera); la fila de credito
> del acta con su rotulo arreglado **en el instrumento que la talla**; la guarda de
> codigo del hallazgo `5.3` del acta 194 (mensajes de commit sin clases por puesto
> ni reparto de ciega), **que a mano YA FUNCIONA Y ESTA MEDIDO** y cuya guarda
> durable sigue pendiente; `acumulan()` que lea la tabla o que declare en su salida
> que no es la sede; el cotejo de clon declarado que separa sentencia de codigo de
> cambio de texto; la excepcion que publica siempre su lista; la medicion del censo
> de arneses con carril de mutacion sin fichero propio; las ocho actas sin entrada
> propia en la serie (173 a 180), medidas y no arregladas; que el campo `evidencia`
> de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue
> en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, nombrado y medido
> y **no resuelto, porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta195_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 194: `edff6568`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 194: LA 193 REPRODUJO ENTERA, PERO SU BATERIA LLEGA CON UNA GUARDA QUE SE DA VERDE A SI MISMA, Y MI PROPIA CIEGA VENIA QUEMADA DESDE EL CONTEXTO DE LA SESION.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y LLEVA SU FECHA DE CORTE.** La
  linea de arriba nombra el acta **194** porque `PATRONES_ACTA` pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la 195**. Es el `D.2` del
  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del
  acta 185, **y el encargo de esta vuelta lo pasa EXPRESAMENTE a la 196 y EN
  PRIMER LUGAR DE LA COLA**, con su motivo dicho. Lo que si se puede
  contar: **6 reportes archivados traen el literal `DESFASE DECLARADO`**
  (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`), contados por `reportes_con_el_literal()` de este mismo fichero,
  **con FECHA DE CORTE 2026-09-06** (banco `9.21`, TODA CIFRA DE CRUCE LLEVA SU
  FECHA DE CORTE). **Un inventario que crece cada vuelta sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V195_HEAD_APERTURA.txt`: `124a18a8`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `8bb20f7c`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **194**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 195`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 195 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta: LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, y LAS DIEZ A FAVOR (siete son los discutibles `D.1` a `D.7` del reporte de la 194 y las tres restantes son las preguntas `P.1`, `P.2` y `P.3`, dos contestadas por extension citable con la cita comprobada contra su fichero), CERO EN CONTRA y es la QUINTA acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` la fila de credito del acta 194 que rotula mal su cifra, `5.2` el rojo de la bateria que SI es reparable, `5.3` `--componer` que publica VERDE sobre diez tramos rojos); CERO CAIDAS DEL EJECUTOR EN LA VUELTA 194, de cifra publicada y de reporte, con LA RACHA DE REPORTE VUELTA A CERO desde el 1 que dejo el acta 194, y SIN ESCALADA QUE ENCARGAR, dicho expresamente para que no se lea como olvido; UNA CAIDA PROPIA DEL AUDITOR, `C.1`, DE METODO (leer `clase` y `razon` del archivo con `json` a mano en vez de por `AP.marcador()` y `AP.leer_veredictos()`, que es la cuarta puerta y ya ofrecia las dos cosas sin coste), con el sujeto NO quemado y probado DESPUES por la propia puerta: 30 de 30 sellados vuelven TAPADOS y 0 destapes apuntados; LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos (30 aislados, 30 cotejados, CERO QUEMADOS, que es la diferencia con la 194 y se debe a que los mensajes de commit del ejecutor ya no publican clases por puesto: ESO FUNCIONO); y LA FILA DE CAIDAS PROPIAS PARTIDA EN DOS, las que ACUMULAN y el total del cuerpo, que es el remedio del hallazgo `5.1` aplicado por el auditor a su propia tabla. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. BLOQUEANTE, Y ES DEUDA SUYA QUE PAGA EL EJECUTOR CON EL INSTRUMENTO. `AUDITOR.md` 1.2: dos discrepancias del auditor cayeron FUERA de su marcado, `654` y `719`, asi que EL CREDITO DE SU TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE. El tramo y el doble estan CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v195_doble_para_la_196.txt`, para que no se elijan despues de mirar. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO se copia, con `evitar` cargado de TODO lo consumido y contado de sus ficheros; el solape con el tramo y con el universo tiene que salir CERO POR CONSTRUCCION, no por suerte. (b) LEER LOS 60 A CIEGAS, tramo y doble, con `aislador_de_ciega.py`, y escribir las clases ANTES de abrir el destape. (c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no parafraseada, Y CON EL ERROR DEL AUDITOR PUESTO: la vara de contenido-manda es EL SUELO, NO EL TECHO, y antes de aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA ya fijada, porque entonces manda la especifica (el `719` se perdio por no preguntarlo: hay regla fijada en el puesto `595` con el `580` de precedente vivo). (d) NO SALTARSE LA `B`: el auditor emitio CERO `B` en 30 pares y el archivo tenia una, el `654`. (e) PUBLICAR EL COTEJO con sus cifras (cuantos coinciden, cuantos discrepan, y cuales caen dentro y fuera del marcado), con los discutibles marcados ANTES de saber si se acierta | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | EL ROJO DE LA BATERIA, ATACADO EN SU CAUSA. Es el hallazgo `5.2` del acta 195 y la adjudicacion de la pregunta `P.2` del reporte de la 194. LO RESERVADO AL FUNDADOR ES PODAR LA NOMINA, NO HACERLA CRECER: la opcion `c` que rechazo el 5 sep 2026 era JUBILAR ARNESES VIEJOS, que es lo contrario de anadir, y el NO TOQUES LA NOMINA de los encargos anteriores se escribio para VUELTAS DE BATERIA y contra LA PODA. (a) LOS SEIS QUE EL CENSO VE Y LA NOMINA NO TIENE ENTRAN EN LA NOMINA, cada uno CON SU SUJETO CONGELADO y cotejado contra su blob de git, RECONTADOS del instrumento al empezar. (b) EL QUE NO PUEDA TENER SUJETO CONGELADO ENTRA COMO CASO DECLARADO, con su marca. (c) LAS TRES ENTRADAS SIN SUJETO CONGELADO que ya estan dentro (`vuelta186_tarea2c_mutacion_cierre_tardio.py`, `vuelta187_tarea4_mutacion_dos_convenciones.py`, `vuelta188_tarea4_mutacion_cobertura_parejas.py`, las tres ancladas a `REPORTE.md` VIVO) se resuelven POR LA MISMA REGLA: o se les congela el sujeto, o pasan a CASO DECLARADO con su marca. (d) `vuelta172_tarea5_mutacion_cierre.py` NO MUERDE desde la 189: se arregla para que caiga cuando tiene que caer, o se declara rota con su motivo medido. (e) NO SE PODA NADA: la nomina solo crece. (f) AL CERRAR, LA BATERIA SOLO SOBRE LO QUE SE TOCO, para comprobar que el rojo atacado se apago, PUBLICANDO LA CIFRA de arneses fuera de la nomina y de entradas sin sujeto congelado, y NO la bateria entera, que no es su vuelta. (g) CON SU CASO POSITIVO POR MUTACION, que pruebe lo que falla hoy: que la mirada de la nomina sobre si misma CAIGA cuando un arnes que el censo ve se queda fuera de la nomina sin ser caso declarado | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | `--componer` DEJA DE PUBLICAR VERDE SOBRE DIEZ ROJOS. Es el hallazgo `5.3` del acta 195 y la otra mitad de la pregunta `P.3` del reporte de la 194: `SALIDA_V194_BATERIA_COMPUESTA.txt` termina en VERDE, los 10 tramos cubren la nomina entera, con exitcode 0, mientras los diez tramos traen `CLASE DEL VEREDICTO: ROJO POR FALLO` y exitcode 1. Es cierto EN LO QUE MIDE, la cobertura, y enganoso EN LO QUE PARECE DECIR, el estado de la bateria; banco `9.1`, el instrumento debe caerse en vez de mentir. (a) `--componer` PROPAGA EL PEOR VEREDICTO DE LOS TRAMOS a su propio exitcode y a su linea final: cobertura entera y algun tramo en rojo NO es VERDE. (b) LAS DOS COSAS SE SIGUEN DICIENDO POR SEPARADO, la cobertura con su cifra y el veredicto con la suya, porque que propague el rojo no puede borrar que la cobertura estaba completa. (c) CON SU CASO POSITIVO POR MUTACION, con la salida de la 194 de sujeto congelado, que es el caso real: diez tramos rojos con cobertura 127 de 127 tienen que dar ROJO | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
