### TAREA 2. LA CORRECCION DECLARADA DE LA `verificacion` DE `OP-L-01`, EN SU SEDE

**ADJUDICADA POR EL ACTA 202 EN SU `4.4`.** El ejecutor de la 202 midio la
discrepancia y **pregunto** en su `P.2` en vez de escribirla por su cuenta.
Ahora esta adjudicada, y se escribe.

**2.a EL INSTRUMENTO SE IMPORTA, NO SE CLONA, Y ANTES SE COMPRUEBA DE VERDAD QUE
NO ESCRIBE.** `scripts/loop/vuelta166_tarea2_correccion_op_l_01.py` mide **25900**
bytes en disco y **25900** normalizado a LF, con `sha256` identico por las dos
convenciones, disco y normalizado a LF: `2886775eb6c29db5`. Leido antes de
llamarlo, trae **2 lineas con marca de escritura en disco**, las **431** y
**432**, y **las dos viven dentro de su `main()`**. De el se llaman
**`las_once()`, `mapa_de_alias()`, `veredictos()`, `medir_clausula_1()` y su
`CABECERA_LD`**, y **su `main()` no se llama**. **Esa comprobacion es la caida
`C.2` del auditor de la 202**, que corrio un instrumento sin mirar antes si
escribia y le reescribio a la vuelta 192 su salida sellada. **Aqui se miro
primero.**

**2.b LAS TRES COSAS QUE LA CORRECCION TENIA QUE DECIR, LAS TRES MEDIDAS HOY.**

**LA PRIMERA, `las_once()` NO DEVUELVE ONCE.** Devuelve **toda cabecera `LD` que
haya HOY** en `docs/plan/LECTURAS_DIRIGIDAS.md`. Medido con el resolutor delante
(`P.1`): **3853** ficheros de nodo, **761** alias en el mapa, y **27** cabeceras
`LD` al corte **2026-09-07**. **Y LA CIFRA VIEJA TAMPOCO SE TECLEA:**
`git rev-list -1 --before='2026-09-04 23:59:59'` sobre ese mismo fichero devuelve
el commit `9363c1ba`, de fecha **2026-09-04**; su contenido en ese commit mide
**205820** bytes, y contado **con la MISMA `CABECERA_LD`** trae **11** cabeceras
`LD`. **Once, medidas, no supuestas.** Hoy `docs/plan/LECTURAS_DIRIGIDAS.md` mide
**214916** bytes en disco y **214916** normalizado a LF.

**Y LA PALABRA `once` NO SALE DEL NOMBRE DE LA FUNCION**, que seria circular:
sale del campo `adjudicacion` de la propia ficha, que dice
`TANDA DE ONCE LECTURAS DIRIGIDAS`, leido de ella en esta vuelta.

**LA SEGUNDA, LA COMPARACION RESUELTA Y SUS PUESTOS, CADA CIFRA CON SU CORTE.**

| cifra | corte 2026-09-04, leido de la propia ficha | corte 2026-09-07, medido hoy | |
|---|---:|---:|---|
| cabeceras `LD` que `las_once()` devuelve | 11 | **27** | DISCREPA |
| filas de `INTRA_DOMINIO_VEREDICTOS.jsonl` | 3388 | 3388 | CALZA |
| alias del resolutor | 761 | 761 | CALZA |
| pares distintos, LITERAL | 3388 | 3388 | CALZA |
| pares distintos, RESUELTOS | 3009 | 3009 | CALZA |
| de las `LD` que aparecen, LITERAL | 0 | 0 | CALZA |
| de las `LD` que aparecen, RESUELTA | 3 | **11** | DISCREPA |
| puestos implicados | 5 | **61** | DISCREPA |

**8 cifras cotejadas y 3 que DISCREPAN**, contadas de
`docs/loop/SALIDA_V203_T2_CORRECCION_OP_L_01.txt`. Las tres viejas se leyeron
**del elemento 4 de la propia `verificacion`**, con expresiones regulares sobre
su texto, no de un acta ni del encargo. Las once que hoy caen en resuelto son
`LD-01`, `LD-05` y `LD-11`, que son las de siempre, mas **ocho `LD-139` a
`LD-146` que no son de aquella tanda**, con **7 puestos cada una**.

**LA TERCERA, Y ES LA QUE NO PODIA FALTAR: EN COMPARACION LITERAL SIGUEN
APARECIENDO 0.** La clausula 1 pregunta si alguna de las lecturas dirigidas vive
en `INTRA_DOMINIO_VEREDICTOS.jsonl`, y medido hoy la respuesta sigue siendo
**ninguna**. **LA CLAUSULA 1 NO SE CAE:** lo que envejecio es **la cifra de la
excepcion**, no la clausula. El instrumento **cae en ROJO y no escribe nada** si
esa comparacion literal no diera 0, y esa guarda es una expresion computada, no
un literal.

**2.c LA PROMESA VIEJA NO SE RETIRA Y NO ES UNA MENTIRA.** Viajaba con su corte
**2026-09-04** y con ese corte era cierta. Lo que cambio no es la medicion sino
**el universo medido**, y por eso la adicion **no borra ni tacha el elemento 4**,
que sigue entero arriba con su corte al lado.

**2.d LO QUE SE ESCRIBIO, Y SOLO POR ADICION.** Un elemento mas en la lista
`verificacion` de `OP-L-01`, **linea 41**, **sin clave nueva de esquema**. El
elemento mide **11156** caracteres y **11156** bytes utf-8.
`docs/plan/OPERACIONES.jsonl` mide hoy, al salir de esta tarea, **513043** bytes
en disco y **513043** normalizado a LF. Antes de esta tarea median **501883** y
**501883** por esas mismas dos convenciones, o sea un **crecimiento de 11160
bytes** por las dos. Su `sha256`, identico en disco y normalizado a LF, pasa de
`6006fd16dc08dc58` a `829c583eb779cab6`.

**2.e LA GUARDA, MEDIDA CONTRA `HEAD` Y NO CONTRA UNA COPIA EN MEMORIA.**

| lo que la guarda exige | lo que mide |
|---|---|
| **1 sola linea** distinta contra `HEAD` | **1**, la **41** |
| **1 sola clave** de esa ficha cambia | **1**, `verificacion` |
| los **6** elementos viejos, identicos y en su orden | **6 de 6**, y la lista pasa de **6** a **7** |
| el `estado` entra y sale igual | `LISTA` en `HEAD` y `LISTA` en disco |
| **0 de las 71** fichas mueven `estado` | **0 de 71**, y **0** fichas aparecen o desaparecen |
| `git diff --numstat` de esa sede | **1 fila**, `1 1 docs/plan/OPERACIONES.jsonl` |

**LA SEGUNDA CORRIDA SELLA CRECIMIENTO 0**, y su salida
`docs/loop/SALIDA_V203_T2_CORRECCION_OP_L_01_IDEM.txt` mide **8644** bytes en disco
y **8644** normalizado a LF. **El crecimiento de la sede en esa corrida es 0 por
las dos convenciones**, la ficha se reconoce como **ya corregida**, y el `sha256`
de la sede queda identico al de la salida de la primera.

**2.f UNA CAIDA MIA, CAZADA ANTES DE PUBLICARSE Y DECLARADA.** En la primera
prueba de idempotencia el elemento compuesto media **11161** caracteres en la
segunda corrida y **11156** en la primera, cinco mas. **No era inestabilidad del
computo:** el texto citaba dentro **el nombre del fichero de salida de cada
corrida**, y la segunda corrida usa `--salida ..._IDEM`. Arreglado fijando la
cita a la **ruta canonica** en vez de al argumento, con su motivo escrito dentro
del codigo; re-corrido, las dos corridas componen **11156** caracteres. **La
escritura ya habia citado la ruta canonica, asi que lo escrito no cambia.**

**2.g LO QUE NO SE HACE, Y ESTA DICHO DENTRO DEL PROPIO ELEMENTO:** `OP-L-01`
**NO SE CIERRA** (acta 202, `4.4`), su `estado` no se toca, no se mueve ni un
veredicto, no se adjudica clase a ningun puesto, no se toca ni un nodo y no se
autoriza ninguna lectura nueva.
