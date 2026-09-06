# REPORTE DE LA VUELTA 193 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta193_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **NO ES VUELTA DE BATERIA, PERO ES LA ULTIMA ANTES.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO VUELTAS, **la 189 la corrio entera**, y **la siguiente
> cae en la 194**. La seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO** por el
> carril de `cerrar_reporte.py`, **con su nombre, sus bytes medidos y su
> atribucion, LAS TRES JUNTAS**. Y por eso **las dos bloqueantes son las que le
> llegan rotas a esa corrida**.
>
> **VAN CINCO SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de cinco esta ganado con
> holgura y **la cifra se conto del instrumento en esta vuelta**, no se heredo: el
> bloque `E` del sello de apertura corrio
> `scripts/loop/vuelta192_racha_de_cierres.py` sobre el inventario ENTERO.
>
> **EL DESFASE DE CALIBRADO SE MIDIO EN LA APERTURA**, dentro del bloque de
> apertura y **antes de la primera operacion**. Una columna de apertura medida al
> cierre es caida que ACUMULA.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina** (la opcion `c` que el fundador RECHAZO el
> 5 sep 2026: **la nomina sigue creciendo y nadie la poda sin el fundador**), ni la
> bateria, que cae en la 194. **Y siguen fuera, nombradas para que la 194 no las
> redescubra:** el desfase de `PATRONES_ACTA`, **que se encarga DESPUES de la 194**
> porque toca `tallar_cabecera_reporte.py` y cuatro entradas de la nomina lo
> nombran; `acumulan()` que lea la tabla o declare que no es la sede; el cotejo de
> clon declarado que separa sentencia de codigo de cambio de texto; la excepcion
> que publica siempre su lista; la medicion del censo de arneses con carril de
> mutacion sin fichero propio; las ocho actas sin entrada propia en la serie (173 a
> 180); el exitcode 2 propagado a `--componer`; y que el campo `evidencia` de
> `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue en
> `LISTA`**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta193_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 192: `485c2f3e`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 192: LA 191 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA NI UNA RUTA VACIA, Y LA PARADA QUE DECLARA ES CIERTA: LA CAIDA ERA MIA.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y DESDE ESTA VUELTA LLEVA SU
  FECHA DE CORTE.** La linea de arriba nombra el acta **192** porque
  `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la
  193**. Es el `D.2` del reporte de la 184, adjudicado a favor con reparacion
  encargada por la `5.2` del acta 185, **y el acta 193 lo deja expresamente DESPUES
  de la bateria de la 194**. Lo que si se puede contar: **4 reportes
  archivados traen el literal `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`), contados por
  `reportes_con_el_literal()` de este mismo fichero, **con FECHA DE CORTE
  2026-09-06** (banco `9.21`, TODA CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Esa
  fecha es la reparacion que el acta 193 encarga sobre la caida `5.5` del reporte
  de la 192**, que publico una cifra de este mismo inventario contradiciendo a su
  propia seccion 0: **un inventario que crece cada vuelta sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V193_HEAD_APERTURA.txt`: `5b921750`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `306c6fbb`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **192**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 193`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 23 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **4 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 193 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. Registra LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, las diez A FAVOR (siete son los discutibles `D.1` a `D.7` del reporte de la 192 y las tres restantes son las preguntas `P.1`, `P.2` y `P.3` contestadas), OTRA VEZ CERO EN CONTRA; LOS CUATRO HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` la cuarta puerta que no se puede usar desde el CLI, `5.2` el cotejo que convierte `"no"` en `si`, `5.3` el arnes que imprime su `mkdtemp` en la salida sellada, `5.4` el reporte que se contradice en la cuenta del `DESFASE DECLARADO`); UNA CAIDA DEL EJECUTOR, DE REPORTE, QUE NO ACUMULA (la seccion 5.5 publica 3 donde hay 4 y donde su propia seccion 0 dice 4: se registra con su nombre, dispara la relectura al doble y NO acumula por la letra del 27 ago 2026, RACHA DE REPORTE 0); UNA CAIDA PROPIA DEL AUDITOR, DE METODO (`C.1`, correr `run_phase1.py` sin `--reaplico-curaduria` y ensuciar `dataset/`); y LA METRICA DE CREDITO de la seccion 7 con la fila de puestos y su nota: 30 aislados y 30 cotejados, CERO quemados, SOLAPE TOTAL a proposito, o sea control y no cobertura nueva. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LOS TRES ARNESES QUE NO REPRODUCEN, ANTES DE LA BATERIA DE LA 194. BLOQUEANTE Y LA MAS URGENTE DE LA VUELTA. Es la adjudicacion `4.10` y el hallazgo `5.3` del acta 193, medido en `docs/loop/_auditor_v193_reproducibilidad.txt`: los tres REPRODUCEN entre dos corridas de hoy y NINGUNO contra su sellada. (a) LOS DOS PRIMEROS (`vuelta191_tarea3_mutacion_lineas.py` y `vuelta191_tarea6_mutacion_bloque_tallado.py`): CONGELAR SU SUJETO o DECLARAR EL CASO por el carril de los `CASO DECLARADO`, porque la `4.4` del acta 191 dice que `SUJETO VIVO` es FALLO y no deuda y la `4.10` cierra la salida que quedaba: una salida que no reproduce NO ES DEL MISMO CALIBRE, tenga o no tenga motivo escrito. (b) EL TERCERO (`guarda_de_entrada_a_la_nomina.py`): que su salida sellada NO lleve el nombre del directorio temporal; el directorio se sigue fabricando y se sigue retirando (`P.16`). (c) ARREGLAR LA GUARDA QUE NO LO VIO: `tempfile` y `mkdtemp` cuentan como huellas de CONGELADO y por eso da CONGELADO a un arnes cuya salida cambia en cada corrida; UNA HUELLA DE TEXTO NO PRUEBA REPRODUCCION. (d) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes cuya salida no reproduce vuelve a salir CONGELADO. (e) NO SE TOCA LA NOMINA: la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada. (f) AL CERRAR, CORRER LOS TRES DOS VECES Y PUBLICAR SUS BYTES Y SUS `sha256`; si alguno sigue sin reproducir, SE PARA Y SE TRAE | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LA VARA DE LAS CIEGAS PASA A SER LA DEL BANCO, Y EL DOBLE SE LEE CON ELLA. Es la adjudicacion `4.9` del acta 193, que contesta la `P.3` a favor. No es doctrina nueva: la vara ya esta escrita en `docs/BANCO_DE_TEXTOS.md` `9.6.1`, LA VARA DE LA RAMA CONTENIDO-MANDA: LA LINEA O EL PROCEDIMIENTO, propuesta y adoptada el 12 ago 2026. (a) ESCRIBIR EL CRITERIO DE LA CIEGA CITANDO `9.6.1` POR NUMERO, con la frase de la vara copiada LITERAL y no parafraseada (`9.5.0`), y que sea el criterio que se le pasa a `aislador_de_ciega.py` de aqui en adelante. (b) LA RELECTURA AL DOBLE DEL TRAMO DE LA 192, que es la deuda de credito de la tanda del auditor y la encarga el auditor, que es donde `AUDITOR.md` 1.2 la pone, CON MOTIVO TRIPLE: dos discrepancias cayeron fuera del marcado del auditor, las dos cayeron tambien fuera del marcado del ejecutor, y son el mismo par para los dos lectores. (c) EL TRAMO son los 30 puestos de `docs/loop/SALIDA_V192_T2_CIEGA.txt`, que son los mismos 30 de la ciega del auditor `docs/loop/_auditor_v193_ciega_blind.txt`. (d) AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada, con `evitar` cargado con TODO lo consumido, CONTADO DE SUS FICHEROS Y NO DEL ENCARGO, y con el solape contra el tramo y contra el universo en 0 y 0 POR CONSTRUCCION. (e) criterio escrito literal, ciega y destape en ficheros SEPARADOS, clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y dudosos NOMBRADOS DELANTE. (f) PUBLICAR LO QUE LA VARA NUEVA CAMBIA: cuantos dudosos y cuantas discrepancias habrian salido distinto con `9.6.1`, y si no cambia nada, DECIRLO. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en `0a77b5a35a962621` por las dos convenciones | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA CUARTA PUERTA QUE SOBREVIVA AL PROCESO. Es el hallazgo `5.1` del acta 193, levantado por el auditor CONTRA EL FICHERO QUE LE PROTEGE Y QUE EL EJECUTOR ESCRIBIO PARA EL EN LA 192, y medido en `docs/loop/_auditor_v193_cuarta_puerta_prueba.txt`: `_BITACORA` y `_SELLADO` son estado de MODULO y mueren con el proceso, el auditor sella con el CLI, y en el proceso siguiente `puede_declarar_clases()` responde `NO: este turno no ha sellado` aunque el sello este en disco. Y LA MITAD MAS SERIA ES SOBRE LAS TRES PUERTAS VIEJAS: el docstring afirma que el sello no se pueda escribir despues, y un turno que toca `REPORTE.md` y arranca otro proceso vuelve a sellar con bitacora vacia porque `sellar()` SOBRESCRIBE. (a) QUE LA BITACORA Y EL SELLO SOBREVIVAN AL PROCESO, en un fichero del turno. (b) QUE `sellar()` CAIGA EN ROJO SI YA HAY SELLO EN DISCO PARA ESA VUELTA, en vez de sobrescribirlo. (c) QUE EL CLI PUEDA DECLARAR LAS CLASES, con su bandera, leyendo el sello de disco. (d) Y SI ALGO NO SE PUEDE, DECIRLO EN EL DOCSTRING en vez de afirmar lo contrario, que esa frase vive en sede de cifra publicada desde el 2 sep 2026. (e) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un sello se puede reescribir despues de tocar uno de los tres prohibidos en otro proceso. (f) NO SE CLONA EL FICHERO: `apertura_del_auditor.py` tiene nombre estable y se le anade. (g) RE CORRER SU ARNES DE LA NOMINA CON EL PARCHE PUESTO Y COMPROBAR QUE REPRODUCE BYTE A BYTE; hoy da 4282 bytes y `sha256` `4779fcd04bc5b2da` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | EL COTEJO QUE NO CONVIERTA `"no"` EN `si`. Es el hallazgo `5.2` del acta 193. `cuerpo_del_cotejo()` de `scripts/loop/cotejo_de_ciega.py` hace `bool(du)`, y `bool("no")` es `True`; el docstring especifica esa columna como `en dudosos` . `si` o `no`, que es justo la forma que revienta, y el instrumento publico al auditor `discrepancias FUERA de los dudosos: 0 (ninguna)` TENIENDO DOS. LA CIFRA PUBLICADA DEL EJECUTOR NO ESTA AFECTADA: `vuelta192_tarea2b_cotejo.py` linea 145 pasa `p in dudosos`, un booleano de verdad. IMPORTA MAS QUE UNA ERRATA porque la columna `en dudosos` es la unica del fichero de la que cuelga una regla de parada: `AUDITOR.md` 1.2 baja el credito y encarga el doble POR LO QUE CAE FUERA. (a) QUE `en_dudosos` SE NORMALICE O CAIGA, y no se resuelva en silencio, con la misma vara que el caso `G` de la mutacion ya le aplica a `veredicto_de`. (b) QUE LA GUARDA DE `escribir_cotejo()` MIRE ALGO MAS QUE EL DENOMINADOR, o que diga en su salida que no es la sede de esta comprobacion. (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un `en_dudosos` no booleano se convierte en `si` sin avisar. (d) RE ESCRIBIR EL COTEJO DEL AUDITOR CON EL INSTRUMENTO ARREGLADO y comprobar que da lo que el publica a mano: 30 cotejados, 25 coinciden, 5 discrepan, 3 dentro y 2 fuera. (e) `cotejo_de_ciega.py` NACIO EN LA 192 Y ENTRA EN LA NOMINA POR LA REGLA DEL PROPIO FICHERO: tocarlo ahora es ANTES de que entre, y eso es a favor y no en contra | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
