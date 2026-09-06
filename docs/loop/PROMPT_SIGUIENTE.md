Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 193. Rama `pasada-unica`. FASE III, EJECUCION.

NO ES VUELTA DE BATERIA, PERO ES LA ULTIMA ANTES. La 189 la corrio entera y por
`AUDITOR.md` 6.1 la siguiente cae en la 194, o sea la vuelta inmediatamente
despues de esta. La seccion 9 de tu reporte cierra con el HUECO DECLARADO Y
MEDIDO por su carril, con su nombre, sus bytes medidos y su atribucion, LAS TRES
JUNTAS. Un hueco declarado no es un hueco escondido.

Y POR ESO LAS DOS BLOQUEANTES SON LAS QUE LE LLEGAN ROTAS A ESA CORRIDA. Medi yo
mismo TRES arneses cuya salida sellada NO reproduce, y los tres entran en la
bateria de la 194 tal como estan. No es una sospecha: esta corrido y esta en
`docs/loop/_auditor_v193_reproducibilidad.txt`.

VAN CINCO SUB-TAREAS y DOS SON BLOQUEANTES. El tope de CINCO sigue vigente y esta
ganado con holgura: la racha de cierres mide 8 hoy (185 a 192), contada por mi
del inventario entero con `scripts/loop/vuelta192_racha_de_cierres.py`. CUENTALA
TU DEL INSTRUMENTO y publica lo que salga.

ABRE EL REPORTE AL EMPEZAR, con su esqueleto tallado y en su propio commit, y
mide tu desfase de calibrado DENTRO del bloque de apertura y ANTES de la primera
operacion. Una columna de apertura medida al cierre es caida que ACUMULA.

Y UNA COSA QUE ME PASO A MI EN ESTA AUDITORIA Y TE AHORRO: el ciclo de Gate 0
corre `run_phase1.py` CON `--reaplico-curaduria` (`vuelta192_apertura.py` linea
638). Sin esa bandera sale EXITCODE 2 y te deja `dataset/` sucio con 72 lineas
cambiadas, porque la compilacion pisa las 71 etiquetas de cara curadas. Va como
mi caida propia `C.1` en el acta 193.

=============================================================================
TAREA 1. LOS REGISTROS. BLOQUEANTE.
=============================================================================

El acta 193 entra en la serie con el numero que devuelva
`scripts/loop/serie_de_registros.py`, computado y no tecleado (hoy el siguiente
libre es `R.55`, pero lo dice el instrumento, no este encargo).

La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta, no de
aqui:

  - LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, y las diez van A FAVOR: siete son
    tus discutibles (`D.1` a `D.7`) y las tres restantes son tus preguntas
    `P.1`, `P.2` y `P.3` contestadas. Otra vez CERO EN CONTRA.
  - LOS CUATRO HALLAZGOS DE LA SECCION 5, que no salen de ningun discutible: la
    cuarta puerta que no se puede usar desde el CLI (`5.1`), el cotejo que
    convierte `"no"` en `si` (`5.2`), el arnes que imprime su `mkdtemp` en la
    salida sellada (`5.3`), y el reporte que se contradice a si mismo en la
    cuenta del `DESFASE DECLARADO` (`5.4`).
  - UNA CAIDA DEL EJECUTOR, DE REPORTE, QUE **NO ACUMULA**: la seccion 5.5 de tu
    reporte publica 3 donde hoy hay 4 y donde tu propia seccion 0 dice 4. Se
    registra con su nombre, dispara la relectura al doble, y NO acumula por la
    letra del 27 ago 2026, porque vive en prosa de una correccion declarada que
    ademas remite a la seccion 0, que trae la cifra correcta. RACHA DE REPORTE: 0.
  - UNA CAIDA PROPIA DEL AUDITOR, DE METODO (`C.1`): corri `run_phase1.py` sin
    `--reaplico-curaduria` y ensucie `dataset/`. La cace en el mismo comando y la
    repare. Va escrita y no se omite.
  - LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de
    puestos con su nota: 30 aislados y 30 cotejados, CERO quemados, y los 30 son
    SOLAPE TOTAL a proposito, o sea control y no cobertura nueva.

EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada. Pruebalo re
corriendolo, con la sede medida en bytes antes y despues.

=============================================================================
TAREA 2. LOS TRES ARNESES QUE NO REPRODUCEN, ANTES DE LA BATERIA DE LA 194.
BLOQUEANTE, Y ES LA MAS URGENTE DE LA VUELTA.
=============================================================================

ES MI ADJUDICACION `4.10` Y MI HALLAZGO `5.3`, Y ESTA MEDIDO, NO SUPUESTO. Corri
cada uno DOS veces y compare contra su salida sellada:

  `vuelta191_tarea3_mutacion_lineas.py`
      sellada 5836 bytes `bc8d7273baf30644` -> hoy 6559 bytes `9834acf0418c527e`
  `vuelta191_tarea6_mutacion_bloque_tallado.py`
      sellada 4173 bytes `6de586c0e5c7a104` -> hoy 4998 bytes `cd48a8a7071d6b89`
  `guarda_de_entrada_a_la_nomina.py` (su salida
      `SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt`, 2433 bytes)
      cambia EXACTAMENTE UNA LINEA por corrida: la del `mkdtemp`

LOS TRES REPRODUCEN ENTRE DOS CORRIDAS DE HOY Y NINGUNO CONTRA SU SELLADA. Yo
restaure las tres y lo comprobe: `git status` no deja ni una sellada ajena
modificada. VERIFICALO TU AL ENTRAR antes de tocar nada.

QUE HACER:

  a) LOS DOS PRIMEROS: CONGELA SU SUJETO o DECLARA EL CASO por el carril que la
     casa ya tiene para los `CASO DECLARADO`. La `4.4` del acta 191 dice que
     `SUJETO VIVO` es FALLO y no deuda, y mi `4.10` cierra la unica salida que
     quedaba: una salida que no reproduce NO ES DEL MISMO CALIBRE, tenga o no
     tenga motivo escrito. El motivo es contabilidad; la reproduccion es la
     guarda.
  b) EL TERCERO: que su salida sellada NO lleve el nombre del directorio
     temporal. El directorio se sigue fabricando y se sigue retirando (`P.16`);
     lo que no puede es imprimirse, porque es aleatorio por construccion.
  c) ARREGLA LA GUARDA QUE NO LO VIO. `guarda_de_entrada_a_la_nomina.py` cuenta
     `tempfile` y `mkdtemp` como huellas de CONGELADO, y por eso da CONGELADO a
     un arnes cuya salida cambia en cada corrida. UNA HUELLA DE TEXTO NO PRUEBA
     REPRODUCCION: la unica vara que la prueba es correrlo dos veces y comparar.
     Si eso es caro, dilo y deja la huella como indicio declarado, pero NO como
     veredicto.
  d) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes cuya salida no
     reproduce vuelve a salir CONGELADO.
  e) NO TOQUES LA NOMINA. No se poda, no se adelanta y no se le meten entradas
     nuevas: la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada,
     y sigue en 127 entradas leidas del instrumento.
  f) AL CERRAR, VUELVE A CORRER LOS TRES DOS VECES Y PUBLICA SUS BYTES Y SUS
     `sha256`. Si alguno sigue sin reproducir, PARAS Y LO TRAES: la 194 no se
     abre con esto abierto.

=============================================================================
TAREA 3. LA VARA DE LAS CIEGAS PASA A SER LA DEL BANCO, Y EL DOBLE SE LEE CON
ELLA.
=============================================================================

ES MI ADJUDICACION `4.9`, QUE CONTESTA TU `P.3` A FAVOR. No es doctrina nueva:
la vara ya esta escrita en `docs/BANCO_DE_TEXTOS.md` `9.6.1`, LA VARA DE LA RAMA
CONTENIDO-MANDA: LA LINEA O EL PROCEDIMIENTO, propuesta y adoptada el 12 ago
2026, y dice literal: *"Si lo que el hijo anade a lo que la madre ya dice CABE EN
UNA LINEA, REPITE. Si trae un PROCEDIMIENTO que la madre no tiene, CONTINUA."*
Por `AUDITOR.md` 0 el banco es la primera fuente de verdad y el literal privado
de un lector no es fuente de nada.

LO QUE LO DECIDE, Y ES MEDICION MIA DE ESTA VUELTA: la vara del banco resuelve
bien los tres pares que nos tumbaron a los dos lectores, Y EN LAS DOS
DIRECCIONES. En `1804` y `2833` cada nodo trae procedimiento entero propio, luego
CONTINUA, luego `D`, y los dos leimos `A`. En `1068` lo que cada uno anade cabe
en una linea, luego REPITE, luego `A`, y los dos leimos `D`. Un criterio que se
equivoca en los dos sentidos no esta calibrado de menos: mide otra cosa.

QUE HACER:

  a) ESCRIBE EL CRITERIO DE LA CIEGA CITANDO `9.6.1` POR NUMERO, con la frase de
     la vara copiada literal, y que sea el criterio que se le pasa a
     `aislador_de_ciega.py` de aqui en adelante. No lo parafrasees: `9.5.0` dice
     que la regla se cita y no se parafrasea.
  b) LA RELECTURA AL DOBLE DEL TRAMO DE LA 192, QUE ES LA DEUDA DE CREDITO DE MI
     TANDA Y LA ENCARGO YO, que es donde `AUDITOR.md` 1.2 la pone. El motivo es
     TRIPLE esta vez: dos discrepancias cayeron fuera de MI marcado, las dos
     cayeron tambien fuera del TUYO, y son el mismo par para los dos lectores.
  c) QUE TRAMO. Los 30 puestos de `docs/loop/SALIDA_V192_T2_CIEGA.txt`, que son
     los mismos 30 de mi ciega `docs/loop/_auditor_v193_ciega_blind.txt`. Lo mido
     y lo digo para que no lo busques: son el mismo conjunto, y esta vez lo han
     leido DOS lectores.
  d) QUE ES AL DOBLE. Sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de
     `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada. A
     `vecinos()` se le pasa `evitar` con TODO lo consumido. CUENTALO TU DE SUS
     FICHEROS, NO DE ESTE ENCARGO, y publica el conteo con los nombres de los
     ficheros de los que sale. Solape con el tramo y con el universo: 0 y 0, POR
     CONSTRUCCION.
  e) COMO SIEMPRE: criterio escrito literal, ciega y destape en ficheros
     SEPARADOS, tus clases escritas y COMMITEADAS en su propio commit ANTES de
     abrir el destape, y tus dudosos NOMBRADOS DELANTE.
  f) Y PUBLICA LO QUE LA VARA NUEVA CAMBIA: cuantos de tus dudosos y de tus
     discrepancias habrian salido distinto con `9.6.1`. Si no cambia nada, DILO,
     que tambien es un dato y me dejaria a mi con una adjudicacion floja.

NO SE TOCA NINGUNA CLASE. `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en
lectura y su `sha256` LF abre y cierra en `0a77b5a35a962621` por las dos
convenciones. Si de la relectura sale una correccion, se declara y se trae; no se
escribe ni una fila.

=============================================================================
TAREA 4. LA CUARTA PUERTA QUE SOBREVIVA AL PROCESO. ES MI HALLAZGO `5.1`.
=============================================================================

LO LEVANTO CONTRA EL FICHERO QUE ME PROTEGE A MI, Y LA ESCRIBISTE TU PARA MI EN
LA 192. No la pude poner en verde. Medido en
`docs/loop/_auditor_v193_cuarta_puerta_prueba.txt`:

  - `_BITACORA` y `_SELLADO` son estado de MODULO y mueren con el proceso. El
    auditor sella con el CLI, y en el proceso siguiente `puede_declarar_clases()`
    responde `NO: este turno no ha sellado` aunque el sello este en disco. El CLI
    no expone ninguna bandera para declarar clases.
  - Y LA MITAD MAS SERIA, QUE ES SOBRE LAS TRES PUERTAS VIEJAS: el docstring
    afirma que *"el sello no se pueda escribir despues"*. LO PROBE Y SE PUEDE. Un
    turno que toca `REPORTE.md` y arranca otro proceso vuelve a sellar con
    bitacora vacia, y `sellar()` SOBRESCRIBE el sello publicando `prohibidos
    tocados antes del sello: 0`.

QUE HACER:

  a) QUE LA BITACORA Y EL SELLO SOBREVIVAN AL PROCESO, en un fichero del turno,
     para que los toques apuntados en una corrida los vea la siguiente.
  b) QUE `sellar()` CAIGA EN ROJO SI YA HAY SELLO EN DISCO PARA ESA VUELTA, en
     vez de sobrescribirlo. Un sello no se reescribe, y hoy eso solo se cumple
     dentro de un mismo proceso.
  c) QUE EL CLI PUEDA DECLARAR LAS CLASES, con su bandera, leyendo el sello de
     disco. Sin eso la cuarta puerta no la puede usar nadie que selle por CLI, o
     sea nadie.
  d) Y SI ALGO DE ESTO NO SE PUEDE, DILO EN EL DOCSTRING EN VEZ DE AFIRMAR LO
     CONTRARIO. Lo que hoy sobra no es la guarda: es la frase que promete lo que
     no hace. Esa frase vive en un docstring de `scripts/`, que es sede de cifra
     publicada desde el 2 sep 2026.
  e) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un sello se puede reescribir
     despues de tocar uno de los tres prohibidos en otro proceso.
  f) NO SE CLONA EL FICHERO. `apertura_del_auditor.py` tiene nombre estable: se
     le anade.
  g) Y RE CORRE SU ARNES DE LA NOMINA CON EL PARCHE PUESTO Y COMPRUEBA QUE
     REPRODUCE BYTE A BYTE, como hiciste en la 192. Hoy da 4282 bytes y `sha256`
     `4779fcd04bc5b2da`. Si no reproduce, PARAS Y LO TRAES: la bateria es la
     vuelta siguiente.

=============================================================================
TAREA 5. EL COTEJO QUE NO CONVIERTA `"no"` EN `si`. ES MI HALLAZGO `5.2`.
=============================================================================

`cuerpo_del_cotejo()` de `scripts/loop/cotejo_de_ciega.py` hace `bool(du)`, y
`bool("no")` es `True`. Tu docstring especifica esa columna como *"`en dudosos` .
`si` o `no`"*, que es justo la forma que revienta. YO LA LLAME ASI Y EL
INSTRUMENTO ME PUBLICO `discrepancias FUERA de los dudosos: 0 (ninguna)` TENIENDO
DOS. Lo cace comparando a mano contra mis dudosos escritos.

TU CIFRA PUBLICADA NO ESTA AFECTADA y lo comprobe leyendo tu fuente:
`vuelta192_tarea2b_cotejo.py` linea 145 pasa `p in dudosos`, un booleano de
verdad. Es una trampa latente, y salto en cuanto lo uso alguien que no fue quien
lo escribio.

POR QUE IMPORTA MAS QUE UNA ERRATA: la columna `en dudosos` es la unica del
fichero de la que cuelga una regla de parada, porque `AUDITOR.md` 1.2 baja el
credito y encarga el doble POR LO QUE CAE FUERA. Un instrumento que silencia esa
cifra publica un verde donde hay una escalada.

QUE HACER:

  a) QUE `en_dudosos` SE NORMALICE O CAIGA, y no se resuelva en silencio. Tu
     propio caso `G` de la mutacion dice que `veredicto_de` *"NO NORMALIZA MAS
     QUE LA CAJA, PARA QUE UNA CLASE RARA SALGA A LA VISTA EN VEZ DE RESOLVERSE
     EN SILENCIO"*. Aplicale a esta columna la misma vara que ya le aplicaste a
     aquella.
  b) QUE LA GUARDA DE `escribir_cotejo()` MIRE ALGO MAS QUE EL DENOMINADOR, o
     que diga en su salida que no es la sede de esta comprobacion. Hoy relee del
     disco y da VERDE sobre un fichero cuya cifra de FUERA es falsa.
  c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un `en_dudosos` no booleano
     se convierte en `si` sin avisar. La mutacion de hoy prueba siete cosas y
     ninguna pasa un `en_dudosos` que no sea booleano.
  d) RE ESCRIBE MI COTEJO CON EL INSTRUMENTO ARREGLADO y comprueba que da lo que
     yo publico a mano: 30 cotejados, 25 coinciden, 5 discrepan, 3 dentro (`965`,
     `1068`, `1814`) y 2 fuera (`1804`, `2833`). Mi fichero es
     `docs/loop/_auditor_v193_cotejo.txt` y ya va con los booleanos bien puestos.
  e) `cotejo_de_ciega.py` NACIO EN LA 192 Y ENTRA EN LA NOMINA POR LA REGLA DEL
     PROPIO FICHERO. Tocarlo ahora es antes de que entre, y eso es a favor, no en
     contra: dilo en el reporte para que no se lea como que le metiste mano a una
     entrada de la nomina.

=============================================================================
LO QUE NO ENTRA, DICHO PARA QUE NO SE COLE NI SE REDESCUBRA
=============================================================================

Ni cribado, ni recomputo, ni operaciones del plan, ni las mesas anotadas, ni
podar la nomina (la opcion `c` que el fundador RECHAZO el 5 sep 2026), ni la
bateria, que cae en la 194.

Y SIGUEN FUERA, NOMBRADAS PARA QUE LA 194 NO LAS REDESCUBRA:

  - EL DESFASE DE `PATRONES_ACTA`, que apunta al acta de `VUELTA - 1`. NO se
    arregla todavia: toca `tallar_cabecera_reporte.py`, que CUATRO entradas de la
    nomina nombran, y moverlo antes de la bateria de la 194 pone en riesgo una
    corrida por algo que no es un fallo. SE ENCARGA DESPUES DE LA 194, y lo digo
    aqui para que no se lea como olvido. Lo que SI se arregla es que la cifra del
    ordinal lleve su FECHA DE CORTE (`9.21`), que es lo que fallo en tu 5.5.
  - `acumulan()` que lea la tabla, o que declare en su salida que no es la sede.
  - El cotejo de clon declarado que separa sentencia de codigo de cambio de texto.
  - La excepcion que publica siempre su lista.
  - La medicion del censo de arneses con carril de mutacion sin fichero propio.
  - Las ocho actas sin entrada propia en la serie (173 a 180), medidas y no
    arregladas.
  - El exitcode 2 propagado a `--componer`.
  - Que el campo `evidencia` de `OP-L-02` nombre los ficheros que ya existen. Su
    ESTADO NO SE MUEVE: sigue en `LISTA`, y declararla HECHA es del fundador.

Y NO SE MUEVE NINGUN VEREDICTO: el `sha256` LF de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en el mismo valor, y
`dataset/` no se toca a mano: el `numstat` se mide al entrar y al salir y las dos
cifras se publican.

Y SI RE CORRES UN INSTRUMENTO QUE PISA UNA SALIDA SELLADA AJENA, RESTAURALA CON
`git checkout --` Y REMIDELA ANTES DE DARLA POR RESTAURADA, Y NO LE TOQUES LOS
FINALES DE LINEA A MANO: a mi me paso en esta auditoria con cinco salidas, y
convertirlas a LF despues del `checkout` las volvio a ensuciar. El corte nuevo, si
interesa, va al lado con su nombre y su vuelta, nunca encima.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
