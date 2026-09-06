## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LAS DOS TAREAS DEL ENCARGO CERRARON.** El tope era dos, por el regimen temporal
de `AUDITOR.md` 6.2, y son dos. **Y ESTA VUELTA CIERRA SU PROPIO REPORTE: es la
SEGUNDA de las dos seguidas que el regimen pide, y el tope vuelve a CINCO en la
187.**

- rama, leida con `git rev-parse --abbrev-ref HEAD`: `pasada-unica`
- HEAD de apertura, sellado **antes de la primera operacion** en
  `docs/loop/SALIDA_V186_HEAD_APERTURA.txt`: **`620dc837`**
- HEAD del ultimo commit antes de cerrar, leido con `git rev-parse HEAD`
  **despues de la ultima operacion**: **`8c952bb1`**
- commit del acta 186, localizado en el log y no tecleado: **`620dc837`**
- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:
  **`793ad9a1`**

**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA Y OTRA VEZ AL CIERRE.** Sus
salidas son `docs/loop/SALIDA_V186_GATE0_CMD1_APERTURA.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**)
y `docs/loop/SALIDA_V186_GATE0_CMD1_CIERRE.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**),
con motor **25/25** en la apertura y **25/25** al cierre, `tsc` **EXIT=0** y **EXIT=0**,
y web **82 ficheros y 1040 passed (1040)** en las dos. La apertura entera vive en
`docs/loop/SALIDA_V186_APERTURA.txt` (**27078 bytes en disco y 27078 bytes normalizados a LF**)
y **la sello el PRIMER commit de la vuelta**.

**EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA, ANTES DE LA PRIMERA
OPERACION**, que es donde `EJECUTOR.md` 1 lo manda desde la 178: **4 filas** en la
apertura y **4 filas** al cierre. Sus dos salidas miden **505 bytes en disco y 498 bytes normalizados a LF** cada una.

**EL ARCHIVO DE VEREDICTOS NO SE MOVIO, Y ESA ES LA PRUEBA INDEPENDIENTE DE QUE
ESTA VUELTA NO TOCO NINGUN VEREDICTO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:
**3388 filas**, **A 551, B 72, C 5, D 2760**, **0 huecos y 0 duplicados**,
**4051967 bytes en disco y 4051967 bytes normalizados a LF**, y `sha256`
**identico por las dos convenciones, disco `ea6e850d331d14f0` y LF `ea6e850d331d14f0`**.
Es el mismo que la apertura de esta vuelta midio y el mismo que las actas 179 a
186 publican. **El plan lleva seis vueltas sin moverse, y esta vuelta tampoco lo
mueve: el acta 186 explica en su seccion 12 por que, y el par 2.464 encabeza la
187.**

## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA

**ESTA ES LA PRIMERA SECCION 4 QUE SU PROPIA ESCALADA VIGILA.** La guarda de la
TAREA 2.d lee las dos cifras de `docs/loop/SALIDA_V186_APERTURA.txt` y las coteja
contra lo que esta seccion afirma, cayendo en ROJO si discrepan o si esta seccion
no las afirma. **Las dos que van aqui salen de ese fichero y no de la memoria.**

`git status --porcelain` da **1 linea** en la apertura, medida en el bloque de
apertura antes de la primera operacion, y
`git diff --numstat -- dataset/` da **0 filas** AL ENTRAR.
**Ninguna perdida de catalogo que declarar**, y `dataset/` no se commitea en esta
vuelta.

**LA UNICA LINEA DE ESA APERTURA ERA EL PROPIO FICHERO DEL BLOQUE DE APERTURA,
TODAVIA SIN SEGUIR POR GIT**, y su docstring lo predijo **con esa cifra y no con
cero**, que es justo la leccion de la `R.1` del acta 186: aquella vuelta le
atribuyo al bloque C una medicion que el bloque C contradecia. **Aqui la
prediccion se escribio con el fichero ya contado.**

**LAS MEDICIONES DEL CIERRE NO SE TECLEAN EN ESTA PROSA, Y SE DICE POR QUE.** El
estado del arbol al cerrar es un instante que los commits del cierre consumen, y
la `R.1` y la cifra no verificable de las 15 lineas del reporte de la 185 son la
misma enfermedad. **Lo que el cierre midio vive en sus ficheros sellados**
(`docs/loop/SALIDA_V186_CICLO_NUMSTAT_CIERRE.txt`, **140 bytes en disco y 140 bytes normalizados a LF**),
y el recuento de filas de `dataset/` **volvio a dar 0 al salir**, medido con el
comando entero y no de memoria.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**SON SEIS Y VAN MARCADOS ANTES DE SABER SI ACIERTO.** Los cinco primeros son de
METODO; **el sexto es de CLASE**, que es lo que el encargo pide expresamente
despues de dos vueltas sin ninguno.

- **`D.1`. EL ARNES DE LA `2.a` NO CUENTA LAS LINEAS DE COMENTARIO.** El encargo
  dice *"contando sus apariciones y exigiendo 1"*, y la reparacion deja un
  comentario que NOMBRA la comparacion, asi que el conteo crudo da **2**. Decidi
  que un comentario no es una copia de la regla, **publico las dos cifras** y el
  arnes prueba que sabe contar sobre un texto fabricado. **Se puede leer que la
  letra pedia el conteo crudo y que entonces la reparacion no cumple.**
- **`D.2`. LA GUARDA DE LA `2.d` CAE EN ROJO SI EL FICHERO DE APERTURA NO
  EXISTE**, y eso el encargo no lo dice. Lo escribi asi porque una guarda que se
  calla cuando le falta la vara no sirve, pero **es una regla que nadie escribio**
  y hace imposible cerrar tarde un reporte de una vuelta que no dejo apertura
  sellada.
- **`D.3`. `es_cierre_tardio()` USA LA LETRA EXACTA DEL ENCARGO Y NO LA
  ESTRECHA.** Devuelve verdadero cuando la vuelta en curso **no es** la del
  reporte, asi que una vuelta ANTERIOR tambien abriria el carril. Se puede leer
  que un cierre solo puede ser tardio, nunca adelantado, y que la condicion
  deberia exigir ademas que la vuelta en curso sea la mayor. **No lo estreche
  porque seria doctrina nueva dentro de una guarda.**
- **`D.4`. FORCE EL ARCHIVADO DEL REPORTE DE LA 184 CON LA BANDERA DE FORZAR**,
  pisando el archivo viejo. Comprobe ANTES que el texto viejo sigue entero y byte
  a byte en otra sede, y publique las DOS corridas, pero **el encargo no nombra
  esa bandera** y se puede leer que pisar un archivo pide permiso.
- **`D.5`. LA GUARDA DE LA `2.d` SE CABLEO DESPUES DE CERRAR EL REPORTE DE LA
  184**, que es el orden de las letras del encargo. **Si hubiera corrido antes, el
  reporte de la 184 NO habria cerrado**, porque su seccion 4 no cita las cifras de
  su apertura sellada. Lo digo yo antes de que lo mida nadie.
- **`D.6`. Y ESTE ES DE CLASE, NO DE METODO: EL PUESTO 338.** La relectura al
  doble lo mira con la vara mecanica y **no ve nada** (no declara diferenciador,
  no tiene lesion, no tiene nodo muerto), y su clase de archivo es **`B`**, la
  unica `B` del universo releido. **Yo no la vuelvo a decidir y el encargo me lo
  prohibe**, pero **marco que la vara con la que reviso no puede ver lo que el
  auditor vio ahi**: el archivo lo clasifico por la correspondencia uno a uno de
  los pasos, y ninguna de mis cuatro comprobaciones mecanicas mira eso. **Si
  alguien quiere discutir una clase de esta vuelta, es esta.**

## 6. LAS PREGUNTAS

- **`P.1`. LA `D.1` DE ARRIBA, CONVERTIDA EN PREGUNTA: EL CONTEO DE LA SEGUNDA
  COPIA, CRUDO O SOLO EN CODIGO.** Si la casa quiere el crudo, la reparacion tiene
  que quitar la comparacion del comentario y el arnes se aprieta en una linea.
  **No lo hago yo porque el comentario es lo que explica por que la pieza (4)
  llama en vez de comparar.**
- **`P.2`. LA `D.2` DE ARRIBA: QUE HACE LA GUARDA DE LA `2.d` CUANDO SE CIERRA
  TARDE UN REPORTE SIN APERTURA SELLADA.** Hoy cae en rojo. Las salidas son
  eximirla en el carril tardio, o declarar que ese reporte no se cierra. **Las dos
  son doctrina y ninguna es mia.**
- **`P.3`. ENTRAN EN LA NOMINA LOS CUATRO ARNESES QUE NACEN EN ESTA VUELTA.** Son
  `vuelta186_tarea2a_mutacion_pieza4.py`, `vuelta186_tarea2b_mutacion_pieza2_cercas.py`,
  `vuelta186_tarea2c_mutacion_cierre_tardio.py` y
  `vuelta186_tarea2d_mutacion_seccion4.py`. **Medido al cerrar esta vuelta,
  `arneses_que_faltan()` los devuelve a los cuatro.** El tope de dos sub-tareas no
  me daba sitio para meterlos, igual que le paso a la 185 con los suyos, **y lo
  digo aqui para que la 187 no se entere en la 189**.

## 7. PENDIENTES DE DOCTRINA

- **`PD.1` SIGUE ABIERTA, QUINTA VUELTA.** Las cinco `D` con el diferenciador ya
  presente el dia del veredicto (**1778, 2530, 2540, 3141, 3232**) siguen sin
  pasar el disparador escrito de la cola post fusion. **Esta vuelta no la toca**,
  y sus cinco puestos quedan en el `R.48` leidos del acta.
- **`PD.7` NUEVA: LA MESA DE LOS TRES NODOS DE LA PUERTA DEL `PMF`.** El acta 186
  la ANOTA en su `6.4` y dice expresamente que **no la encarga y no la adjudica**,
  porque es trabajo de plan. **Aqui se registra como pendiente de doctrina para
  que tenga sede**, y esta vuelta no la abre porque su encargo se lo prohibe con
  esas palabras. Los nodos son los de los puestos **338** y **297**.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**CERO CAIDAS PROPIAS EN ESTA VUELTA, Y EL CERO VA CONTADO Y NO OMITIDO.** No
levanto ninguna `C.n`: los cuatro arneses nuevos salieron VERDES en su primera
corrida, ningun arnes ya sellado cambio de color, ninguna cifra publicada se
tecleo sin instrumento, y el bloque de apertura corrio entero antes de la primera
operacion con su prediccion escrita antes de medir.

**LO QUE SI DECLARO, Y NO ES UNA CAIDA SINO UNA LIMITACION MEDIDA:** el bloque de
apertura de esta vuelta contaba los puestos de la ciega con el patron de la
palabra PUESTO en mayusculas, y las ciegas del auditor los escriben con la clave
`puesto_intra`, asi que su bloque H.5 publico **0 puestos** para los cuatro
ficheros que miro. **No movio ninguna decision**, porque la relectura al doble de
la TAREA 1.c usa el patron correcto y leyo sus **30** puestos, pero **la cifra del
H.5 es inutil y se dice en vez de dejarla pasar por buena**.
