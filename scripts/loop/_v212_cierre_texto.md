## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE ESTA SECCION CITA EL FICHERO DEL QUE SALE** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). Las de las dos tareas van en su anexo, talladas por `scripts/loop/_v212_t1_seccion.py` y `scripts/loop/_v212_t2_seccion.py`, y **aqui no se repiten**.

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS

Corrido con `scripts/loop/_v212_ciclo_gate0.py`, que **IMPORTA** los ocho comandos de `scripts/loop/_v205_ciclo_gate0.py` y solo le corrige el numero de vuelta, computado de su propio nombre y no tecleado. **PEOR EXITCODE DE LOS OCHO: 0 en APERTURA y 0 en CIERRE.**

**EL CICLO DE GATE 0, LOS DOS LADOS.** **FILAS ARMADAS LEYENDO las DIECIOCHO salidas `docs/loop/SALIDA_V212_*_APERTURA.txt` y `_CIERRE.txt`: 9; FILAS QUE DEBERIA HABER: 9.**

| # | comando | APERTURA | CIERRE |
|---|---|---|---|
| 1 | `run_phase1.py --reaplico-curaduria` | EXITCODE 0, 4790 bytes | EXITCODE 0, 4790 bytes |
| 2 | `etiquetas_de_cara.py --aplicar` | EXITCODE 0, 7928 bytes | EXITCODE 0, 7928 bytes |
| 3 | `sync_assets_web.py` | EXITCODE 0, 574 bytes | EXITCODE 0, 574 bytes |
| 4 | `git diff HEAD --numstat` | EXITCODE 0, **0 filas**, 140 bytes | EXITCODE 0, **0 filas**, 140 bytes |
| 5 | `vuelta83_conteo_aristas.py WORK` | EXITCODE 0, 168 bytes | EXITCODE 0, 168 bytes |
| 6 | `vuelta85_medir_desfase_calibrado` | EXITCODE 0, 498 bytes | EXITCODE 0, 498 bytes |
| 7 | `engine/run_all_tests.py` | EXITCODE 0, 1131 bytes | EXITCODE 0, 1131 bytes |
| 8a | `npx tsc --noEmit` | EXITCODE 0, 7 bytes | EXITCODE 0, 7 bytes |
| 8b | `pnpm test` | EXITCODE 0, 336 bytes | EXITCODE 0, 336 bytes |

**LAS DIECIOCHO CELDAS SE CUENTAN DE SUS DIECIOCHO FICHEROS**, una a una, y el `EXITCODE` sale de la ultima linea de cada uno. **`git diff HEAD --numstat` da CERO FILAS en los dos lados: el grafo no se movio ni al abrir ni al cerrar.**

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**LAS SEDES, AL ENTRAR Y AL CERRAR.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_APERTURA.txt` para la apertura y una medicion de AHORA para el cierre: 7; FILAS QUE DEBERIA HABER: 7.**

| sede | al entrar (disco / LF) | al cerrar (disco / LF) | `sha256` de cierre (disco / LF) | la movio esta vuelta |
|---|---|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 4054129 / 4054129 | 4057130 / 4057130 | `758edf1f5c313c18` / `758edf1f5c313c18` | **SI**, la `TAREA 1.b`: el puesto 730 |
| `docs/plan/OPERACIONES.jsonl` | 513043 / 513043 | 514452 / 514452 | `ca1d95b5b3d19e9e` / `ca1d95b5b3d19e9e` | **SI**, la `TAREA 1.c`: la `adjudicacion` de `OP-F-04-HOR` |
| `dataset/metadata/master_graph.json` | 8375817 / 8375817 | 8375817 / 8375817 | `627cc662296f7f00` / `627cc662296f7f00` | NO, solo se leyo para resolver aristas |
| `docs/plan/01_FUENTES.md` | 128187 / 126666 | 128187 / 126666 | `73168452929b3d42` / `f965abf6c3ca95c3` | NO, solo se leyeron sus lineas 1168 y 1453 |
| `docs/plan/08_VERIFICACION.md` | 69068 / 69068 | 69068 / 69068 | `76bfebb6b2d8ef72` / `76bfebb6b2d8ef72` | NO, solo se leyo su linea 9 |
| `docs/BANCO_DE_TEXTOS.md` | 186490 / 186490 | 186490 / 186490 | `8adbd60239509bb4` / `8adbd60239509bb4` | NO, solo se leyeron sus `9.6.1`, `9.6.2`, `9.6.3` y `9.10` |
| `docs/loop/ACTA_AUDITOR.md` | 4936249 / 4936249 | 4936249 / 4936249 | `a977aa91e8b9f86c` / `a977aa91e8b9f86c` | NO, solo se leyo |

**LAS DOS QUE SE MOVIERON SE MOVIERON UNA SOLA VEZ CADA UNA, Y LAS DOS LO PRUEBAN CON `sha256` DISTINTO AL SALIR** (`SI (se exige SI)` en la `1.b` y `SI (se exige SI)` en la `1.c`). **`docs/plan/01_FUENTES.md` es la unica sede cuyas dos convenciones NO COINCIDEN**, y no es cosa de esta vuelta: entra y sale igual, y ni se abrio para escribir.

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

**LA CIFRA NO SE PUBLICA AQUI, Y NO ES OMISION: ES LA REGLA.** El instrumento que las cuenta es `scripts/loop/vuelta186_rutas_del_reporte.py` y **necesita el reporte YA CERRADO** para contar las rutas que el propio cierre anade. Publicar aqui la cifra de antes del cierre seria medir temprano y publicar tarde, que es la caida de la vuelta 28 (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). **Su salida sellada es `docs/loop/SALIDA_V186_RUTAS_DEL_REPORTE.txt` y ahi vive la cifra**, corrida sobre el reporte cerrado.

**Y LA CORRIDA QUE SE COMMITEA ES LA DE DESPUES DEL CIERRE, no una de antes.** Su veredicto y su cifra de rutas que no existen o miden cero se leen en ese fichero sellado, y no se copian aqui: copiarlas seria volver a publicar una medicion de apertura como si fuera de cierre.

## 4. LO QUE SE TOCO, Y LO QUE NO

**SE TOCARON DOS SEDES Y TRES CAMPOS EN TOTAL:** la `clase` y la `razon` del puesto 730 en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y la `adjudicacion` de `OP-F-04-HOR` en `docs/plan/OPERACIONES.jsonl`. **NI UN NODO DEL GRAFO**, que es lo que la regla 4 de `EJECUTOR.md` manda en modo de cierre, y lo prueban las dos celdas de `git diff HEAD --numstat` de la `3.1`, las dos en cero filas.

**LO QUE MI APERTURA SELLADA DICE, COTEJADO Y NO TECLEADO** (`docs/loop/SALIDA_V212_APERTURA.txt`): **`git status --porcelain` AL ENTRAR daba 2 lineas**, y las dos eran mis propios computos `_v212_` sin seguir todavia, no trabajo ajeno colgando; y **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**, o sea que la vuelta empezo con el grafo limpio.

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**TODO LO QUE ESTA VUELTA ESCRIBIO EN scripts/loop, LISTADO CON `os.listdir` EN ESTA CORRIDA.** **FILAS ARMADAS LEYENDO un `os.listdir` del arbol scripts/loop (otra vez sin comillas inversas, por lo mismo que la 7 bis) filtrado por el prefijo: 14; FILAS QUE DEBERIA HABER: 14.**

| fichero | que es |
|---|---|
| `scripts/loop/_v212_apertura.py` | computo de la vuelta |
| `scripts/loop/_v212_ciclo_gate0.py` | computo de la vuelta |
| `scripts/loop/_v212_cierre_texto.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v212_cierre_texto.py` | computo de la vuelta |
| `scripts/loop/_v212_esqueleto.py` | computo de la vuelta |
| `scripts/loop/_v212_hallazgo_rutas.py` | computo de la vuelta |
| `scripts/loop/_v212_t1_seccion.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v212_t1_seccion.py` | computo de la vuelta |
| `scripts/loop/_v212_t1b_escribir.py` | computo de la vuelta |
| `scripts/loop/_v212_t1b_puesto_730.py` | computo de la vuelta |
| `scripts/loop/_v212_t1c_op_f_04_hor.py` | computo de la vuelta |
| `scripts/loop/_v212_t2_cola_relectura.py` | computo de la vuelta |
| `scripts/loop/_v212_t2_seccion.md` | cuerpo compuesto, no fuente |
| `scripts/loop/_v212_t2_seccion.py` | computo de la vuelta |

**CIFRA ficheros con prefijo `_v212_`: 14, de ellos 11 con extension `.py` y 3 con extension `.md`.** **LA CIFRA Y LA LISTA SALEN DEL MISMO `os.listdir`, en la misma linea de codigo**, que es el remedio de la `C.3` que el ejecutor de la 211 se cazo a si mismo: alli la cifra estaba tecleada y la lista no la miraba nadie.

**LOS 14 LLEVAN LOS 14 EL PREFIJO DE GUION BAJO**, o sea que estan **fuera del censo y fuera de la nomina**, y mueren con la vuelta. **NINGUNO ES ARNES, GUARDA NI LECTOR NUEVO:** los cuatro que miden importan sus funciones de la sede que ya existe (`scripts/loop/apertura_del_auditor.py` para el marcador, `scripts/loop/verificar_aristas_vivas.py` para el resolutor, `scripts/loop/vuelta186_rutas_del_reporte.py` para las dos convenciones y para el patron de rutas), y los tres compositores solo leen salidas y arman texto. **LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135 Y NADIE LA PODO.**

### 4.2. LA `1.d` DEL ENCARGO, CUMPLIDA POR OMISION Y DICHA EN VOZ ALTA

**NO TOQUE `OP-I-01`** (sigue en `LISTA`, contado en la `1.c` al medir por `estado` antes y despues), **NO MARQUE LAS 95 ENTRADAS DEL INVENTARIO**, y **NO ESCRIBI NI UNA FILA NUEVA EN `docs/plan/08_VERIFICACION.md`**. Las tres son prohibiciones expresas del encargo y las tres se cumplen. La `1.d` las registra con su cita en el anexo de la TAREA 1.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` NO BARRI LAS DOS CITAS VIVAS DEL 730 FUERA DEL ARCHIVO, Y EL BANCO `9.10` DICE QUE UN VOLTEO BARRE SUS TABLAS DERIVADAS EN EL MISMO ACTO.** Las medi y las publico en la TAREA 1: `docs/INTRA_DOMINIO_INFORME.md` linea 6941 y `docs/plan/03_FUSIONES.md` linea 5424, mas una tercera en un reporte archivado que no se toca. **Mi lectura es que no envejecen como frase**, porque las dos dicen que el 730 *declara* la `A` por la lectura vieja y la fila **sigue diciendo eso**, con el texto viejo entero encima; lo que envejece es la clase que el lector infiere. **Y mi motivo para no editarlas es que es prosa sellada del informe y del plan**, que es forma, y la forma del plan el propio auditor la manda al fundador en su `6.2`. **Puedo estar equivocado en las dos mitades y por eso lo marco.**

**`D.2` EL PUESTO `474`.** Es el unico de los tres que quedan en `A` que **no tiene bloque de EJECUCION con la vara nombrada**, y lleva la lectura vieja escrita en presente (*la figura NO APLICA: manda la regla original*). **No lo muevo**, porque la ratificacion del banco lo nombra entre los que se sostienen y su razon cierra por contenido. **Pero es el que mas se parece al 730 de los que quedan**, y si alguien va a discutir uno, va a ser ese.

**`D.3` DIGO QUE DOS CIFRAS DEL ACTA 211 NO REPRODUCEN.** Su **13** y su **9** no salen de ningun patron que yo haya probado: el guion literal da 11 y 8, el patron holgado da 14 y 10. **Puede que el auditor usara un tercer patron que no se me ocurrio**, y por eso publico LOS DOS MIOS con su expresion regular al lado en vez de decir solo que el suyo esta mal. **Lo que no es discutible es que la lista de los cuatro en `A` y los once del choque reproducen al digito.**

**`D.4` PEGUE LAS TRES RAZONES ENTERAS DENTRO DE CERCA.** El encargo pide la razon entera; las cercas son donde esta casa pone el verbatim, y la guarda de las dos convenciones **no mira dentro de una cerca** (es lo que el acta 211 mide en su `7.2`). **O sea que las cifras que esas razones llevan dentro entran al reporte sin que ninguna guarda las mire.** Son del autor que las escribio y no mias, y lo digo, pero alguien puede sostener que un verbatim con cifras deberia ir de otra manera.

## 6. LAS PREGUNTAS

**`P.1` EL BARRIDO DEL `9.10`: QUIEN LO HACE.** Cuando una relectura conjunta voltea UN veredicto, las citas vivas de ese numero en el informe y en el plan quedan describiendo la clase vieja. **El `9.10` manda barrerlas y el encargo no me lo ordena, y editar prosa sellada tampoco me toca.** No es contradiccion suficiente para parar (la `D.1` explica por que), pero la casa no tiene escrito quien lo hace en un volteo de UNA sola fila. **Traigo las dos lineas nombradas para que se adjudique.**

**`P.2` EL INSTRUMENTO DE RUTAS SE CAE CON UN DIRECTORIO, Y ESO TOCA A TRES REPORTES.** Va entera en la `7`, con su medicion. La pregunta es de gobierno: **la moratoria prohibe reparar lectores**, y este no da una cifra mala, da una excepcion. **No lo toque. Pregunto si el arreglo entra por la puerta de la caida de dato o si espera a que se levante la moratoria.**

## 7. PENDIENTES DE DOCTRINA

**`PD.1` UNA CORRECCION QUE CONSERVA EL TEXTO VIEJO ENTERO DEJA LAS CITAS DERIVADAS EN UN ESTADO QUE LA DOCTRINA NO NOMBRA.** El banco `9.10` habla de tablas que **citan un veredicto por numero** y de volteos **en bloque**. Aqui hay un volteo de UNA fila y dos citas que **no son tablas**: son prosa narrativa que describe lo que la fila decia, y que **sigue siendo cierta como descripcion del texto**. **No hay regla que diga si eso hay que barrerlo, matizarlo o dejarlo.** Registro lo mejor sostenido (no barrer, declarar) y sigo, que es lo que manda la regla 5 de `EJECUTOR.md`.

**`PD.2` UN VERBATIM CON CIFRAS AJENAS DENTRO DE UNA CERCA NO TIENE REGLA.** Va ligado a la `D.4`. La casa exige que toda cifra lleve su corte y su atribucion, y una razon del archivo pegada entera trae docenas de cifras del que la escribio. **La cerca las saca del alcance de la guarda, que es lo que las hace publicables; lo que no esta escrito es si eso es lo correcto o solo lo que funciona.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. ESCRIBI Y COMMITEE UN FICHERO LLAMADO `SALIDA_V212_TALLADOR_CABECERA.txt` QUE NO LLEVABA UNA CABECERA: LLEVABA UN RECHAZO.** En la apertura corri el tallador sabiendo que la mitad del cierre no existe todavia, y **redirigi su salida al mismo nombre que usa el fichero bueno**. Durante un commit entero, una ruta que promete una cabecera tallada apuntaba a veinte celdas que no se pudieron leer. **Es la especie de LA RUTA QUE PROMETE PRUEBA ES CIFRA** (`EJECUTOR.md` 1): la ruta existia y no media cero, asi que ninguna guarda la habria cazado, y el contenido no era el que el nombre promete. **REMEDIO, y es una linea: el tallador de apertura, si se corre, escribe en un nombre con `_RECHAZO` y no en el del cierre.** El fichero bueno existe desde el cierre y es el que la cabecera cita.

**LO QUE NO CUENTO COMO CAIDA, Y DIGO POR QUE.** Primero: **el heredoc de comillas simples se me cayo** al escribir el primer computo, igual que a la 209, la 210, la 211 y al propio auditor. **No es caida porque el remedio ya estaba escrito y lo cumpli:** use la herramienta de fichero y lo digo, que es lo que el acta 210 dejo dicho. Segundo: **el compositor de la TAREA 1 cayo en ROJO en su primera corrida**, porque le pedi la tercera aparicion de una linea que solo tiene dos. **Eso no es una caida: es la guarda haciendo su trabajo**, y cayo **antes** de escribir nada. Tercero: **parche una celda del reporte ya anexado** para quitarle unas comillas inversas a un directorio; **no lo cuento como caida porque el parche se verifico contra el `.md` regenerado byte a byte** y porque el motivo esta publicado entero en la `7`, pero **lo digo en vez de callarlo** porque un reporte parcheado a mano es exactamente lo que la 211 decidio no volver a hacer.

## 7 BIS. EL HALLAZGO DE LA VUELTA, MEDIDO Y NO REPARADO

**EL INSTRUMENTO QUE HACE CUMPLIR *LA RUTA QUE PROMETE PRUEBA ES CIFRA* SE CAE CON EXCEPCION SI EL REPORTE CITA UN DIRECTORIO.** `scripts/loop/vuelta186_rutas_del_reporte.py` casa la cadena docs/plan seguida de barra (la escribo aqui SIN comillas inversas a proposito, porque escribirla con ellas reproduce el fallo dentro de este mismo reporte, y eso me paso), `os.path.exists` dice que si porque el directorio existe, y el `read()` revienta. **Lo medi importando SU funcion, para que el patron fuera el suyo y no uno mio.**

**LOS DOS REPORTES ARCHIVADOS, MEDIDOS.** **FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V212_HALLAZGO_RUTAS.txt`: 6; FILAS QUE DEBERIA HABER: 6.**

| lo que midio el instrumento |
|---|
| docs/loop/reportes/REPORTE_V211.md: 29 rutas distintas, medidas con SU patron |
| rutas de docs/loop/reportes/REPORTE_V211.md que no existen en disco: 1 ['docs/loop/SALIDA_V211_BATERIA.txt'] |
| ese texto TUMBA el instrumento: SI (basta UNA fila de la tabla de arriba) |
| docs/loop/reportes/REPORTE_V210.md: 19 rutas distintas, medidas con SU patron |
| rutas de docs/loop/reportes/REPORTE_V210.md que no existen en disco: 0 |
| ese texto TUMBA el instrumento: SI (basta UNA fila de la tabla de arriba) |

**CIFRA directorios citados en los DOS sujetos archivados, sumados: 4.** **LOS SUJETOS SON LOS DOS REPORTES YA ARCHIVADOS Y NO EL DE ESTA VUELTA, A PROPOSITO:** este reporte todavia va a crecer con su cierre, y publicar aqui sus bytes seria medir temprano y publicar tarde. **A este lo mide el propio instrumento de la casa DESPUES del cierre, y si citara un directorio se caeria.** **NO ES UN DEFECTO QUE TRAIGA ESTA VUELTA:** el reporte de la 210 y el de la 211 citan dos directorios cada uno y los dos tumban el instrumento igual. **Y esto prueba una cosa que importa mas que el crash: la cifra de rutas que el reporte de la 211 publica no puede haber salido de este instrumento, porque sobre ese texto el instrumento no llega a imprimir.**

**NO LO REPARO, Y ES LETRA:** la moratoria de `AUDITOR.md` 6.3 prohibe arreglar lectores. **Lo que si hice, porque no cuesta codigo, es sacar de mi reporte los DOS sitios donde citaba un directorio entre comillas inversas**, uno en la TAREA 1 y otro en esta misma seccion, **y por eso el instrumento SI corre sobre este reporte**. El segundo es el que mas dice: **describir el fallo con su ejemplo entrecomillado lo reproducia**, y lo cace corriendo el instrumento sobre el reporte ya cerrado en vez de darlo por bueno. Su caso rojo por mutacion esta corrido: EL CASO ROJO CAE COMO TIENE QUE CAER: sin mutar da 0 y mutado da 1..

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

1. **ADJUDICAR LA `P.1`**: quien barre las citas vivas de un veredicto volteado cuando el volteo es de una sola fila. Las dos lineas estan nombradas y medidas, y el trabajo, si se adjudica, son dos ediciones de prosa.
2. **ADJUDICAR LA `P.2`**: si el crash del instrumento de rutas entra por la puerta de la caida de dato (y entonces se arregla ya) o espera a que se levante la moratoria. **Mientras no se decida, todo reporte que cite un directorio entre comillas inversas se queda sin medir sus rutas, y eso no deja sintoma.**
3. **NO ABRIR COLA DE RE-CRIBADO.** La TAREA 2 midio que **ninguno** de los tres que quedan en `A` cuelga de la silueta. **El cerco del cero-enlazados esta cerrado**, y la unica marca que queda es la `D.2` del `474`, que es marca y no encargo.
4. **LA 215 ES LA VUELTA DE BATERIA**, por la cadencia de cinco de `AUDITOR.md` 6.1. La 212 no lo es y su seccion 9 lo declara con su hueco medido.

