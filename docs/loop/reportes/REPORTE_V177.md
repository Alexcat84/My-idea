# REPORTE DE LA VUELTA 177 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta177_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA
> ADJUDICADA.** El acta 176, punto 7.8, reancla el contador a la vuelta que de
> verdad corrio la bateria y no a la que la tenia encargada: **la 175 no fue una
> vuelta de bateria porque murio sin producir una linea**, la corrio la 176, y
> desde ella se cuentan los cinco. **La proxima vuelta de bateria es la 181, no
> la 180.** Por eso la seccion 9 de este reporte cierra con el **HUECO DECLARADO
> Y MEDIDO** por el carril de la TAREA 1.b de la 173, con su medicion, su
> atribucion y su corrida. Un hueco declarado no es un hueco escondido.
>
> **EL TOPE DE ESTA VUELTA SIGUE EN DOS** (`AUDITOR.md` 6.2, regimen temporal
> vigente hasta que DOS vueltas seguidas cierren su propio reporte con
> `cerrar_reporte.py`), y el encargo trae exactamente dos. **LA 176 ES LA PRIMERA
> DE LAS DOS SEGUIDAS**, medido y no supuesto: cerro su reporte y lo archivo en su
> misma vuelta. **Si esta cierra el suyo, el tope vuelve a CINCO por la propia
> letra de la 6.2, sin que nadie tenga que decidirlo.**
>
> **Y ESTA VUELTA SI CORRIO SU BLOQUE DE APERTURA ANTES DE SU PRIMERA
> OPERACION**, que es lo que la 176 no hizo. Su lectura (que la 6.1 sacaba el
> aparato de abrir y cerrar la vuelta) **quedo corregida en el acta 176 punto
> 7.1**: la 6.1 saca el TRABAJO DE PLAN, no el aparato; si lo sacara, sacaria
> tambien el reporte y la 6.1 y la 6.2 se contradirian. Ademas esta vuelta no es
> de bateria, asi que la duda ni se plantea.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas coinciden, porque la
> 176 escribio su reporte, lo cerro y lo archivo; el fichero corre LAS DOS
> igualmente y publica lo que salga de cada una, porque una guarda que solo se
> mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: LA VUELTA 177 ENTREGA SUS DOS TAREAS ENTERAS Y CIERRA SU PROPIO REPORTE, QUE ES LA SEGUNDA DE LAS DOS SEGUIDAS QUE AUDITOR.md 6.2 PIDE PARA QUE EL TOPE VUELVA A CINCO. El rojo bloqueante esta remediado computando el esperado y PROBADO QUE SIGUE MORDIENDO por tres mutaciones del texto; nace cotejar_clon_declarado.py con tres veredictos y clasificacion por token, y su propio arnes me tumbo dos errores de diseno antes de que salieran de la vuelta; las tres correcciones chicas del acta van con arnes propio, y la del tallador SE ESTRENO CAZANDO A SU AUTOR. OP-L-03 se desaplaza y lo que encuentra vale mas que lo que se le pedia: TRES DE LOS SEIS ACTOS GRANDES NO ESTABAN PENDIENTES SINO DISUELTOS, de 29 pares solo 9 son reales, y los tres actos leidos dejan cinco triangulos A mas A mas D con un patron comun. CERO VEREDICTOS MOVIDOS, comprobado por sha256 antes y despues; marcador intacto en 3.388 con 0 huecos; Gate 0 verde entero y en su orden en las dos puntas. MI CAIDA PROPIA ES LA MEDICION DE DESFASE TOMADA AL CIERRE, que es la especie que el acta 176 acepto diciendo NO SE REPITE, y se repitio: la traigo con su causa medida, su remedio para la 178 y marcada como discutible.**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta177_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 176: `f3087229`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 176: LA VUELTA PAGO LA DEUDA DE LA 175 ENTERA Y TODO LO QUE PUBLICA REPRODUCE BAJO MI MANO SALVO UNA FRASE. Recomputo verificado: bateria 88 de 88 con su doble corrida, 0 repetidas, 0 ajenas, 0 de la nomina sin correr, y los seis nombres que mi conteo vio de mas NO EXISTEN COMO FICHERO, son literales de prueba del propio arnes. Salida unica 60197 bytes en disco y 60197 normalizado a LF, 995 lineas, sha256 2f86d9e075d4e5ce, y sus 903 lineas no vacias estan LAS 903 dentro de la seccion 9: no es un hueco declarado, es la corrida. Los 18 numeros de los nueve tramos calzan uno a uno, el reloj suma 31.9, y las cinco cuentas de veredicto dan ANCLA PERDIDA 0, NO REPRODUCIBLE 0, RUIDO 0, CASO DECLARADO 2, NO MORDIO 1. GATE 0 VERDE EN SU CICLO ENTERO Y EN SU ORDEN, CORRIDO POR MI: numstat 0 filas, motor 25/25, tsc exit 0, web 82 y 1040. MARCADOR 3388 CON A 551 B 72 C 5 D 2760, puestos de 1 a 3388, CERO HUECOS Y CERO DUPLICADOS. LA CABECERA NO LA LEI, LA COTEJE: corri el tallador y las 11 filas salen IDENTICAS, 0 distintas y 0 ausentes. 13 commits en su orden, 39 rutas, y el grafo con 0 filas entre los dos sellos. LAS 55 RUTAS DEL REPORTE EXISTEN Y NINGUNA MIDE CERO BYTES. MI UNICA CAIDA CONTRA EL EJECUTOR ES DE REPORTE Y NO ACUMULA: el "diff del clon declarado sale VACIO" NO sale vacio, y lo medi hasta el fondo antes de acusar, porque el fondo le da la razon: de las 33 lineas de maquina que difieren, SENTENCIAS DE CODIGO 0 y LITERALES DE TEXTO 33, y en vuelta176_cierre.py la maquina sale VACIA de verdad. Vive en prosa del cuerpo, luego por la letra del 27 ago se registra y no acumula, y NO la meto en la cuarta sede de cifra publicada porque estirar cifra y ruta hasta un resultado de diff seria legislar, que es parada y no adjudicacion. LAS DOS RACHAS EN CERO Y LA ESCALADA NO SE DISPARA. CIEGA 7 DE 8, AISLADA DE UN SOLO TIRO ANTES DE GATE 0, DE LA VARA, DE LOS ARNESES Y DEL RECOMPUTO, Y EL QUE FALLO LO FALLE YO: el 491 lo di por gemelo leyendo el titulo cuando la prueba estaba en los pasos que tenia delante, la excepcion de rondas en uno y el term sheet en el otro. El archivo no fallo ninguna de las ocho. SIETE ADJUDICACIONES, TODAS CITANDO REGLA ESCRITA, y la mas gorda es la P.1: el arnes del rojo SE RE-COMPUTA EL ESPERADO, no se pasa a caso declarado ni se poda de la nomina. Le doy la razon al ejecutor en el D.6 y la culpa de la ambiguedad es mia, y reescribo la letra (f) en el encargo. La cadencia queda adjudicada: la proxima bateria es la 181, no la 180, porque la 175 no fue una vuelta de bateria, murio sin producir una linea. NO HAY PARADA: no escribo PARA_ALEXIS.md y el encargo de la 177 va completo, con dos sub-tareas, el remedio del rojo bloqueante y OP-L-03 desaplazada despues de siete vueltas.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V177_HEAD_APERTURA.txt`: `f3087229`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `1d18aa04`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **176**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 177`, y su salida
cruda vive en `docs/loop/SALIDA_V177_TALLADOR_CABECERA.txt` (5001 bytes, 11 filas de tabla,
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `f3087229` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 176: LA VUELTA PAGO LA DEUDA DE LA 175 ENTERA Y TODO LO QUE PUBLICA REPRODUCE BAJO MI MANO SALVO UNA FRASE. Recomputo verificado: bateria 88 de 88 con su doble corrida, 0 repetidas, 0 ajenas, 0 de la nomina sin correr, y los seis nombres que mi conteo vio de mas NO EXISTEN COMO FICHERO, son literales de prueba del propio arnes. Salida unica 60197 bytes en disco y 60197 normalizado a LF, 995 lineas, sha256 2f86d9e075d4e5ce, y sus 903 lineas no vacias estan LAS 903 dentro de la seccion 9: no es un hueco declarado, es la corrida. Los 18 numeros de los nueve tramos calzan uno a uno, el reloj suma 31.9, y las cinco cuentas de veredicto dan ANCLA PERDIDA 0, NO REPRODUCIBLE 0, RUIDO 0, CASO DECLARADO 2, NO MORDIO 1. GATE 0 VERDE EN SU CICLO ENTERO Y EN SU ORDEN, CORRIDO POR MI: numstat 0 filas, motor 25/25, tsc exit 0, web 82 y 1040. MARCADOR 3388 CON A 551 B 72 C 5 D 2760, puestos de 1 a 3388, CERO HUECOS Y CERO DUPLICADOS. LA CABECERA NO LA LEI, LA COTEJE: corri el tallador y las 11 filas salen IDENTICAS, 0 distintas y 0 ausentes. 13 commits en su orden, 39 rutas, y el grafo con 0 filas entre los dos sellos. LAS 55 RUTAS DEL REPORTE EXISTEN Y NINGUNA MIDE CERO BYTES. MI UNICA CAIDA CONTRA EL EJECUTOR ES DE REPORTE Y NO ACUMULA: el "diff del clon declarado sale VACIO" NO sale vacio, y lo medi hasta el fondo antes de acusar, porque el fondo le da la razon: de las 33 lineas de maquina que difieren, SENTENCIAS DE CODIGO 0 y LITERALES DE TEXTO 33, y en vuelta176_cierre.py la maquina sale VACIA de verdad. Vive en prosa del cuerpo, luego por la letra del 27 ago se registra y no acumula, y NO la meto en la cuarta sede de cifra publicada porque estirar cifra y ruta hasta un resultado de diff seria legislar, que es parada y no adjudicacion. LAS DOS RACHAS EN CERO Y LA ESCALADA NO SE DISPARA. CIEGA 7 DE 8, AISLADA DE UN SOLO TIRO ANTES DE GATE 0, DE LA VARA, DE LOS ARNESES Y DEL RECOMPUTO, Y EL QUE FALLO LO FALLE YO: el 491 lo di por gemelo leyendo el titulo cuando la prueba estaba en los pasos que tenia delante, la excepcion de rondas en uno y el term sheet en el otro. El archivo no fallo ninguna de las ocho. SIETE ADJUDICACIONES, TODAS CITANDO REGLA ESCRITA, y la mas gorda es la P.1: el arnes del rojo SE RE-COMPUTA EL ESPERADO, no se pasa a caso declarado ni se poda de la nomina. Le doy la razon al ejecutor en el D.6 y la culpa de la ambiguedad es mia, y reescribo la letra (f) en el encargo. La cadencia queda adjudicada: la proxima bateria es la 181, no la 180, porque la 175 no fue una vuelta de bateria, murio sin producir una linea. NO HAY PARADA: no escribo PARA_ALEXIS.md y el encargo de la 177 va completo, con dos sub-tareas, el remedio del rojo bloqueante y OP-L-03 desaplazada despues de siete vueltas.'), HEAD real de apertura `f3087229` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `4cafaf56` (leido de `SALIDA_V177_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE. Siete letras: (a) dejar constancia de la lectura del acta 176 nombrando sus adjudicaciones; (b) EL ARNES DEL ROJO, que es lo primero que se arregla, computando el esperado de la misma fuente viva en vez del `3` tecleado de la linea 175, SIN pasarlo a caso declarado, SIN re-anclarlo a sujeto congelado y SIN podar la nomina, con su caso positivo por mutacion que pruebe que el arnes SIGUE MORDIENDO; (c) la correccion declarada de la caida de reporte 1 del acta 176, el `diff` del clon que se publico como vacio y no lo es, en los DOS docstrings y sin borrar de que iban; (d) `scripts/loop/cotejar_clon_declarado.py`, el instrumento de nombre estable que hace innecesaria esa correccion a mano, con TRES veredictos separados y la clasificacion de SENTENCIAS DE CODIGO contra LITERALES DE TEXTO; (e) las dos correcciones chicas del acta, la salida del lanzador fuera de `docs/loop/` (`D.5`) y el tallador sellando su propio rechazo; (f) `D.3` y `P.3`, el tope de tramo POR MINUTOS computado del reloj medido dentro de `reparto_en_tramos()`, para que la 181 no lo decida a ojo; (g) contar en voz alta lo que NO entra en esta vuelta | **CERRADA. Las siete letras entregadas, con arnes propio en las cuatro que tocan codigo** | `SALIDA_V177_T1B_ROJO_ANTES.txt`, `_T1B_ARNES_DESPUES.txt`, `_T1B_MUTACION.txt`, `_T1C_COTEJO_176.txt`, `_T1D_MUTACION.txt`, `_T1D_COTEJO_MIS_CLONES.txt`, `_T1E_MUTACION.txt`, `_T1E_RECHAZO_DEMO.txt`, `_T1F_MUTACION.txt`, `_T1F_ARNES_VIEJO.txt` |
| **TAREA 2** | `OP-L-03`, QUE LLEVA SIETE VUELTAS APLAZADA Y SE DESAPLAZA AQUI. La vara de hoy la sigue dando en LISTA sin ninguna prueba de ejecucion. Leer los ACTOS GRANDES primero, que es donde la lectura por acto cambia algo: el de SEIS miembros y los cuatro de CINCO. El criterio es `P.5` del banco del plan y se CITA, no se parafrasea: cada acto que vaya a fundirse se lee ENTERO despues de su destejido y antes de su fusion, y la decision es POR ACTO y no por pareja. Cada lectura se registra en JSONL y no se narra en prosa; ningun veredicto se mueve sin correccion declarada y recomputo; las 55 lecturas marcadas LECTURA DIRIGIDA no entran en la cola ni mueven su marcador; y el campo `estado` de la ficha NO SE TOCA aunque la operacion termine, porque la vara es `vuelta150_3_relectura_expediente.py` por decision del fundador del 4 sep 2026 | **CERRADA. El tramo entero: 6 de 6 actos grandes y 9 de 9 pares reales, con 0 veredictos movidos** | `docs/plan/OP_L_03_LECTURAS.jsonl` (6 filas), `SALIDA_V177_T2_UNIVERSO.txt`, `_T2_DOSSIER.txt`, `_T2_REGISTRO.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS Y LAS CORRECCIONES (bloqueante)

#### 1.a. CONSTANCIA DE QUE LEI EL ACTA 176, Y QUE HACE CADA ADJUDICACION CONMIGO

Leida en `docs/loop/ACTA_AUDITOR.md` desde la linea **60402** (`sed -n
'60402,60864p'`), que es donde empieza su cabecera, hasta el final del fichero
(**60864** lineas en total, contadas con `wc -l` en esta vuelta).

**UNA CORRECCION DE CONTEO ANTES DE ENUMERARLAS, PORQUE EL ENCARGO DICE SIETE Y
YO CUENTO DIEZ.** La seccion 7 del acta trae **diez puntos numerados, del 7.1 al
7.10**. El **siete** del encargo no sale de ahi: sale de la propia seccion 10 del
acta, que enumera las que **citan regla escrita** y nombra exactamente estas
siete: `D.1`, `D.2`, `D.4`, `D.5`, `P.1`, `D.6` y `P.2`. Las tres restantes no
son adjudicaciones plenas y el acta lo dice de cada una: la **7.3** acepta hoy y
encarga el instrumento para manana, la **7.9** es un encargo con vuelta de
destino (la 178) y la **7.10** dice expresamente *"NO LA FIJO YO"* y la sube al
fundador. **Nombro las diez, porque callar tres para que cuadre un numero seria
la especie que este bucle castiga.**

| punto | que adjudica | **que hace conmigo** |
|---|---|---|
| **7.1** `D.1` | la columna de apertura medida al cierre: **ACEPTADA**, y corrige la lectura que la causo | **me obliga a correr el bloque de apertura ANTES de la primera operacion**, que es lo que la 176 no hizo. Corrido: `docs/loop/SALIDA_V177_APERTURA.txt` |
| **7.2** `D.2` | la nomina de 87 a 88 con el arnes de su misma vuelta: **ACEPTADA por regla escrita** (la del propio fichero desde la 148) | **me deja meter en la nomina los tres arneses que escribo hoy**, sin esperar una vuelta |
| **7.3** `D.3` | el tamano de tramo elegido a ojo: **ACEPTADO HOY, INSTRUMENTADO MANANA** | **es mi TAREA 1.f**: el tope por minutos, computado del reloj medido |
| **7.4** `D.4` | el segundo motivo de rojo de la guarda del commit: **ACEPTADO SIN RESERVA** | **nada que hacer**, y me sirvio hoy: mi arbol llego con la `M` y solo el cotejo de blobs la adjudico |
| **7.5** `D.5` | la salida del lanzador dentro de `docs/loop/`: **ACEPTADA HOY, CORREGIDA EN LA 177** | **es la primera mitad de mi TAREA 1.e** |
| **7.6** `D.6` | correr los tramos 7, 8 y 9 tras el rojo del 6: **A FAVOR MIO**, y la ambiguedad es del auditor | **nada que corregir**, y la letra (f) queda reescrita en mi encargo |
| **7.7** `P.1` | el arnes del rojo: **SE COMPUTA EL ESPERADO**, las otras dos salidas descartadas con motivo | **es mi TAREA 1.b, la bloqueante** |
| **7.8** `P.2` | la cadencia: **la proxima bateria es la 181, no la 180** | **esta vuelta NO es de bateria** y mi seccion 9 cierra con el hueco declarado y medido |
| **7.9** `PD.2` | la guarda del sujeto congelado: **el ejecutor tiene razon**, entra en la **178** | **no entra en esta vuelta**, y va contada en la 1.g |
| **7.10** `PD.1` | la convencion de bytes: **NO LA FIJA EL AUDITOR**, sube al fundador | **sigo publicando LAS DOS** (disco y normalizado a LF) mientras nadie fije cual manda |

#### 1.b. EL ARNES DEL ROJO (bloqueante). REPRODUCIDO, CORREGIDO Y VUELTO A MORDER

**REPRODUJE EL ROJO ANTES DE TOCAR NADA**, que es lo que impide arreglar un
sintoma que no se ha visto. `docs/loop/SALIDA_V177_T1B_ROJO_ANTES.txt`:

| lo que medi | mi corrida | lo que el acta 176 dice |
|---|---|---|
| exit | **1** | 1 |
| casos / pasan / fallan | **19 / 18 / 1** | 19 / 18 / 1 |
| el caso que falla | **`H_el_texto_nombra_las_tres` real=11 esperado=3** | real=11 esperado=3 |
| la linea del literal | **175**, localizada en el fichero | 175 |

**LA CORRECCION ES LA TERCERA SALIDA Y ENTRA POR EL CARRIL DEL BANCO 9.10.** La
linea vieja **sigue entera dentro del fichero, verbatim y sin tachar**, y el
propio arnes lo comprueba con dos casos (`H_la_linea_vieja_sigue_declarada_y_sin_tachar`
y `H_la_linea_vieja_ya_no_es_sentencia_activa`). El esperado pasa a
`len(hall)`, computado de la misma fuente viva.

**LAS TRES COSAS QUE EL ENCARGO PROHIBE, Y NO HICE NINGUNA:** no se paso a CASO
DECLARADO, no se re-anclo a sujeto congelado, y **LA NOMINA NO SE PODO** (crece).

**19 CASOS PASAN A SER 20, Y LO DIGO EN VEZ DE PUBLICAR EL 19 QUE EL ENCARGO
ESPERA.** Anadi `H_la_medicion_viva_trae_hallazgos`, porque un esperado computado
deja pasar `0 == 0` el dia que la medicion viva se quede sin hallazgos, y el
propio encargo dice que *"un esperado computado que no puede fallar nunca no es
una guarda, es un adorno"*.

| el arnes entero, despues | cifra |
|---|---:|
| exit | **0** |
| casos / pasan / fallan | **20 / 20 / 0** |
| casos que caen al mutar el esperado | **20 de 20** |
| hallazgos de la medicion viva hoy | **11** |

Fichero: `docs/loop/SALIDA_V177_T1B_ARNES_DESPUES.txt`.

**Y SU CASO POSITIVO POR MUTACION PRUEBA LO QUE EL ENCARGO EXIGE, QUE NO ES QUE
PASE SINO QUE MUERDA.** `scripts/loop/vuelta177_tarea1b_mutacion_esperado_vivo.py`
**deja el esperado en paz y rompe el producto**, que es la mutacion dura:

| mutacion del TEXTO (el esperado no se toca, sigue en 11) | veces que dice "cae sobre" | el caso |
|---|---:|---|
| un hallazgo de menos | 10 | **CAE** |
| un hallazgo de mas | 12 | **CAE** |
| ningun hallazgo | 0 | **CAE** |
| ninguna (el texto entero) | 11 | PASA |

exit **0**, **8 casos, 8 pasan, 8 caen al mutar el esperado**, y el registro de
veredictos queda **identico byte a byte**. Fichero:
`docs/loop/SALIDA_V177_T1B_MUTACION.txt`.

#### 1.c. LA CORRECCION DECLARADA DE LA CAIDA DE REPORTE 1

**Las dos sedes corregidas, sin borrar de que iban**, con la misma forma con la
que el fundador corrigio el *"307 nodos vivos"* de `scripts/run_phase1.py`:
`scripts/loop/vuelta176_esqueleto_reporte.py` y `scripts/loop/vuelta176_cierre.py`.
Comprobado en los dos: **la frase vieja sigue presente** y **la correccion
tambien**. El reporte archivado de la 176 **no se reescribe**.

**REPRODUZCO AL AUDITOR EN LO QUE IMPORTA Y DISCREPO EN UN NUMERO**, medido con
mi instrumento y no copiado de su acta
(`docs/loop/SALIDA_V177_T1C_COTEJO_176.txt`, sujetos leidos de git en el corte
`f3087229` y no del arbol, porque el arbol ya lleva mi correccion):

| par, con `175` y `176` a `NNN` | entero | docstring | **la maquina** | sentencias | literales |
|---|:-:|:-:|:-:|---:|---:|
| `vuelta175_esqueleto_reporte.py` vs `vuelta176_...` | DIFIERE | DIFIERE | **DIFIERE, 33 lineas** | **1** | **32** |
| `vuelta175_cierre.py` vs `vuelta176_cierre.py` | DIFIERE | DIFIERE | **VACIO DE VERDAD** | 0 | 0 |

**Las 33 lineas calzan exactas con el acta. La clasificacion no.** Donde el acta
dice SENTENCIAS **0** y LITERALES **33**, mi instrumento dice **1 y 32**, y la
sentencia es **una coma final** de la lista `TAREAS` que el fichero de la 175
lleva y el de la 176 no (token 150, linea A:62, un `,`). **Una coma final no
cambia lo que el programa hace, asi que la conclusion del auditor se sostiene
entera; lo que no se sostiene es el CERO exacto.** Publico el numero del
instrumento y no el de la prosa (`EJECUTOR.md` 2).

#### 1.d. `cotejar_clon_declarado.py`, EL INSTRUMENTO QUE LA HACE INNECESARIA

Nombre estable y sin numero de vuelta. **Tres veredictos separados y no uno**,
clasificacion en **SENTENCIAS DE CODIGO** y **LITERALES DE TEXTO**, y **rojo si
le falta un fichero**.

**CLASIFICA POR TOKEN PORQUE POR LINEA ESTABA MAL, Y LO CUENTO PORQUE LO ESCRIBI
YO.** Mi primera version tapaba **caracter a caracter**, cosa que conserva la
longitud: dos cadenas distintas quedaban como dos hileras de puntos de distinto
largo, o sea **seguian difiriendo**. Corrida contra el par del auditor daba
**SENTENCIAS 33 y LITERALES 0, justo del reves que su medicion**, y ese
desacuerdo fue lo que me hizo mirar. Por token, una cadena de veinte lineas es
**un** token y vale `<TEXTO>` a los dos lados mida lo que mida.

**Y SU ARNES ME TUMBO UN SEGUNDO ERROR DE DISENO, QUE ES PARA LO QUE ESTAN.** Mi
unico carril bloqueante, `--exigir-maquina-identica`, enrojecia tambien con un
cambio de **solo texto**, que es exactamente lo que este instrumento existe para
excusar: **inutil para el unico uso que iba a tener**. El arnes lo cazo con un
`exit 1` donde esperaba `0`. Ahora hay **dos carriles** y cada uno dice para que
es: el estricto, y `--exigir-codigo-identico`, que es el util.

`scripts/loop/vuelta177_tarea1d_mutacion_cotejo.py`: exit **0**, **28 casos, 28
pasan, 28 caen**, sobre **siete clones de mentira** que incluyen el que tumbo la
primera version (una cadena de varias lineas que se alarga).
Fichero: `docs/loop/SALIDA_V177_T1D_MUTACION.txt`.

**Y ME LO APLICO A MI MISMO EN ESTA MISMA VUELTA**, aunque la obligacion empiece
en la 178 (`docs/loop/SALIDA_V177_T1D_COTEJO_MIS_CLONES.txt`):

| mi clon | lineas de maquina que difieren | sentencias | literales |
|---|---:|---:|---:|
| `vuelta177_apertura.py` (de `vuelta175_apertura.py`) | 208 | **151** | 57 |
| `vuelta177_esqueleto_reporte.py` (de `vuelta176_...`) | 50 | **1** | 49 |

**Y LAS 151 NO ME LAS QUITO DE ENCIMA.** Mi docstring ya declara que reescribe el
bloque H entero, asi que la cifra no contradice lo que dice; **lo que hace es
ponerle numero, y 151 sentencias es mucho para la palabra "clon"**. La del
esqueleto es otra **coma final**.

#### 1.e. LAS DOS CORRECCIONES CHICAS

**`D.5`.** El lanzador escribe su propia transcripcion **fuera de `docs/loop/`** y
la copia dentro **al terminar**: la misma precaucion que su fichero de trabajo ya
tenia, aplicada al **segundo** fichero, que era el que faltaba. Al abrir la
vuelta habia **9** ficheros de lanzador dentro de `docs/loop/` y el lanzador **no
escribia su transcripcion a ningun sitio** (medido en el bloque H.7).

**Y SE PRUEBA SIN CORRER LA BATERIA**, que esta prohibida fuera de una vuelta de
bateria y ademas muta `dataset/`: se sustituye `correr_tramo` por un doble y se
llama a `main()` con `--tramo 1`, asi que **el camino real se ejercita entero sin
correr una sola entrada de la nomina**. El doble comprueba **desde dentro, mientras
el tramo corre**, que el fichero de `docs/loop/` **todavia no existe**.

**EL TALLADOR SELLA SU PROPIO RECHAZO** en `SALIDA_V<N>_TALLADOR_RECHAZO.txt`. Al
abrir la vuelta habia **0** ficheros de esos y el tallador **no nombraba esa
cadena** en sus 1822 lineas (bloque H.8). **Y no reparte a ojo lo que no nombra
lado**: lo cuenta aparte como `SIN LADO`. Demostrado contra una vuelta **999** que
no existe: **40 celdas, 19 de APERTURA, 19 de CIERRE, 2 SIN LADO**
(`docs/loop/SALIDA_V177_T1E_RECHAZO_DEMO.txt`; el fichero con numero de vuelta
inventada se borro).

`scripts/loop/vuelta177_tarea1e_mutacion_correcciones_chicas.py`: exit **0**, **24
casos, 24 pasan, 24 caen**. **Su primera version fallo uno, y era mi assertion y
no el codigo**: la etiqueta va acolchada a ocho, o sea `[CIERRE  ]` y no
`[CIERRE]`. Fichero: `docs/loop/SALIDA_V177_T1E_MUTACION.txt`.

#### 1.f. `D.3` Y `P.3`: EL TAMANO DE TRAMO SE COMPUTA Y NO SE ELIGE

`TOPE_DE_MINUTOS_POR_TRAMO = 10.0` **escrito con su motivo**, mas
`reloj_de_la_corrida()`, `minutos_por_entrada()` y `tamano_por_minutos()`, y un
carril nuevo en `reparto_en_tramos()` que es **opcional** para que las llamadas
viejas no se muevan.

**EL RELOJ, LEIDO DE LA SALIDA DE LA 176 Y NO DE SU REPORTE:**

| | |
|---|---:|
| tramos que el reloj trae | **9** |
| suma de los minutos | **31,9** |
| suma de las entradas | **88** |
| coste por entrada, **MAXIMO** | **1,59 min** |
| coste por entrada, media (que **no** se usa) | 0,36 min |
| **tamano computado** | **6** |

**EL COSTE ES EL MAXIMO Y NO LA MEDIA, Y ESA ES LA MITAD ENTERA DE LA
CORRECCION.** Con la media, un tope de 10 minutos daria tramos de **27** entradas
y **el tramo de 15,9 volveria a pasar, mas gordo**. El arnes tiene un caso
dedicado (reloj desigual: un tramo carisimo entre baratos, que es la forma exacta
del reloj de la 176) y exige que el tamano salga **del caro**.

`scripts/loop/vuelta177_tarea1f_mutacion_tope_minutos.py`: exit **0**, **25 casos,
25 pasan, 25 caen** (`docs/loop/SALIDA_V177_T1F_MUTACION.txt`).

**NO ROMPI NADA DE LO VIEJO, COMPROBADO Y NO SUPUESTO:**
`vuelta176_tarea1c_mutacion_tramos.py` sigue verde (**35 casos buenos, 0 fallos**,
`docs/loop/SALIDA_V177_T1F_ARNES_VIEJO.txt`), y `--mutar-nomina` (6 casos) y
`--mutar-reproducibilidad` siguen verdes.

#### 1.g. LO QUE NO ENTRA EN ESTA VUELTA, CONTADO EN VOZ ALTA

La guarda del **sujeto congelado** (`PD.2`, acta 7.9, entra en la **178**); la
**ceguera de la vara**, que no distingue una ficha CONSUMIDA de una PENDIENTE y
por eso imprime SEIS donde el trabajo real son CUATRO (**178**); la **convencion
de bytes**, que sube al fundador; la **segunda sede de la clausula 4.4** en
`REPORTE_V172.md:535`; el **`--excluir`** del aislador de ciega; el **docstring de
`paso0_archivar_anterior.py`**; y la **guarda que falta en la dependencia del
`D.4` de la 174**. **Ninguna de las siete se toco.**

#### LO QUE ENCONTRE SIN QUE NADIE ME LO ENCARGARA, Y NO ME CALLO

**`arneses_que_faltan()` ME DIJO QUE NO FALTABA NINGUNO CUANDO FALTABAN DOS
MIOS.** Solo mira los arneses de vuelta **estrictamente posterior** a la ultima
representada en la nomina; en cuanto entro la entrada de la 1.b, la ultima vuelta
paso a ser **177** y los otros dos arneses de la 177 se volvieron **invisibles**
para ella. **El primer arnes de una vuelta ciega a los demas de su misma vuelta.**

Medido: el censo ve **153** arneses, la nomina tiene **92** entradas, y **62** de
los que el censo ve siguen fuera de la nomina (los 60 anteriores a la vara del
censo son de por si, los **2** de la 177 no lo eran). **Los anadi a mano y la
nomina va de 89 a 92.** **No toco la funcion**: la mido, la declaro y la subo,
que es lo que `EJECUTOR.md` 5 manda cuando algo no tiene regla escrita.

**Y UNA CAIDA DE MI PROPIO BLOQUE DE APERTURA, CAZADA POR MI.** Mi H.6 busca el
literal `SALE VACIO` y publica **un solo fichero viejo**; el acta dice **dos
docstrings** y **el acta tiene razon**: en `vuelta176_esqueleto_reporte.py` la
frase parte en dos por un salto de linea y mi busqueda literal no la ve.
Re-medido normalizando espacios: **los dos que el acta nombra**. **La cifra buena
es la del acta y la mala es la mia**, y esta escrita asi en el commit `1d18aa04`.

### TAREA 2. `OP-L-03`, DESAPLAZADA DESPUES DE SIETE VUELTAS

#### 2.a. LA FICHA, LEIDA ENTERA ANTES DE TOCAR NADA

`docs/plan/OPERACIONES.jsonl` **linea 43**, `OP-L-03`, fase
`09_LECTURAS_DIRIGIDAS`, tipo **MESA**, estado `LISTA`, `fecha_corte`
**2026-08-11**, con sus **4** clausulas de `verificacion`, su `adjudicacion` y su
`nota`. Mas `docs/plan/LECTURAS_DIRIGIDAS.md` (**2230** lineas).

**Y LA FICHA CONTRADICE AL ENCARGO EN SU PROPIO CUERPO, ASI QUE LO DIGO ANTES DE
EMPEZAR.** El encargo dice *"El universo esta MEDIDO desde el 11 ago 2026: 55
pares en 29 actos, corte puesto 2117"*, y eso es exacto **para la `evidencia` y
la `fecha_corte` de la ficha**. Pero **la `nota` de esa misma ficha declara un
RECOMPUTO POSTERIOR**, al corte **3.388**, **ADJUDICADO EN LA VUELTA 15**: *"EL
BACKLOG QUEDA EN CUARENTA ACTOS Y SETENTA Y TRES PARES, por LECTURA LITERAL de la
regla y no por preferencia"*. **Corrido hoy el instrumento que la propia nota
cita** (`scripts/loop/backlog_l03_vuelta14.py`,
`docs/loop/SALIDA_V177_T2_UNIVERSO.txt`): **40 actos, 73 pares**, con reparto
**24 de tres, 10 de cuatro, 4 de cinco y DOS de seis**.

**DE AHI SALE UNA SEGUNDA DIFERENCIA, Y CAMBIA POR DONDE SE EMPIEZA.** El encargo
manda empezar por `cierre_segun_complejidad_venta`, *"seis miembros, seis pares
por leer de quince, **el mayor del reparto**"*. **En el universo adjudicado NO es
el mayor**: hay **dos** actos de seis, y el otro
(`breakthrough_desempeno_actual...`) tiene **8** pares por leer, no 6. El "mayor"
del encargo es el del corte **2117**. **Sigo el universo adjudicado y no el de la
`evidencia`**, porque `EJECUTOR.md` 2 dice que la cifra la da el instrumento
corrido hoy, y **hago los SEIS actos grandes** (los dos de seis y los cuatro de
cinco) en vez de los cinco que el encargo nombra: es la misma instruccion
(*"LOS ACTOS GRANDES PRIMERO"*) aplicada a lo que hay. **MARCADO COMO
DISCUTIBLE.**

#### 2.b. EL CRITERIO, CITADO Y NO PARAFRASEADO (`P.5`, banco 9.5.0)

La clausula de la ficha, **verbatim**: *"cada acto que vaya a fundirse **SE LEE
ENTERO** despues de su destejido y antes de su fusion"*. **La lectura es del
ACTO, no de la pareja**, y el motivo es la regla de **FAMILIA DECLARADA** del
informe intra-dominio: **una familia juzgada de a pares da incoherencia, porque
la pregunta no es de pares**. Una decision por acto.

#### 2.c. EL HALLAZGO QUE CAMBIA LA TAREA: LA MITAD DEL TRAMO YA NO EXISTE

**TRES DE LOS SEIS ACTOS GRANDES NO TIENEN NADA QUE LEER, Y NO PORQUE SE HAYAN
LEIDO: PORQUE SE FUNDIERON.** Sus miembros escritos son **hoy un solo nodo**, asi
que sus pares no estan pendientes, **estan disueltos**.

**VERIFICADO POR DOS CAMINOS INDEPENDIENTES QUE DAN LO MISMO**, que es lo que
`EJECUTOR.md` 9 manda (*"toda perdida de catalogo declarada se re-verifica contra
el grafo"*): el **resolutor de `P.1`** sobre `ids_alias`, y el campo
**`deprecado` del `master_graph.json`**.

| acto | miembros | vivos (resolutor) | vivos (grafo) | pares que el instrumento da por leer | **pares reales** |
|---|---:|---:|---:|---:|---:|
| `breakthrough_desempeno_actual...` | 6 | **1** | **1** | 8 | **0** |
| `cierre_segun_complejidad_venta...` | 6 | **1** | **1** | 6 | **0** |
| `cash_burn_calculation...` | 5 | 5 | 5 | 4 | **4** |
| `construccion_de_leverage...` | 5 | 5 | 5 | 3 | **3** |
| `encuadre_desafio_diseno...` | 5 | **1** | **1** | 6 | **0** |
| `estrategia_de_innovacion_arenas...` | 5 | **4** | **4** | 2 | **2** |
| **TOTAL** | | | | **29** | **9** |

**LOS DOS CAMINOS CALZAN EN LOS SEIS ACTOS.** Y el acto por el que el encargo me
manda empezar, `cierre_segun_complejidad_venta`, **es uno de los tres disueltos**:
sus seis miembros son hoy un solo nodo vivo, que lleva su mismo nombre.

**QUE SIGNIFICA, DICHO SIN ADORNO:** el backlog de `OP-L-03` **esta medido sobre
el archivo de componentes del corte 3.388 y la campana ha fundido nodos desde
entonces**, asi que **cuenta como pendientes pares que ya no existen**. En el
tramo grande, **de 29 pares solo 9 son reales: sobran 20**. No extrapolo al resto
del backlog porque no lo he medido, y **decir cuanto sobra en los 34 actos que no
mire seria adivinar**.

#### 2.d. LAS LECTURAS, EN JSONL Y NO EN PROSA (letra (d))

`docs/plan/OP_L_03_LECTURAS.jsonl`, **6 filas, 24.158 bytes**, releido del disco y
**calza byte a byte con lo escrito**. Cada fila lleva el acto, los miembros con su
fuente, los nodos vivos por los dos caminos, los pares en sus **tres** cajones,
la **forma** del acto, **si esa forma cambia** respecto de lo que el par decia por
separado, y la **cobertura** al lado (banco 9.26, cuarta clausula de la ficha).

| cuenta de la tarea, sumada de las filas | |
|---|---:|
| actos del tramo | **6** |
| actos LEIDOS | **3** |
| actos sin nada que leer (ya fundidos) | **3** |
| pares que el instrumento daba por leer | **29** |
| **pares por leer reales** | **9** |
| **pares LEIDOS en esta vuelta** | **9** |
| pares del tramo sin lectura | **0** |
| reparto de clases de lo leido | **A 3, D 6** |
| actos donde la forma **CAMBIA** respecto del par | **3 de 3** |
| **veredictos movidos** | **0** |

**LAS TRES FORMAS, EN UNA LINEA CADA UNA** (enteras en el JSONL):

- **`cash_burn_calculation`**: **una familia y un vecino, no una familia de
  cinco.** La familia es el modelo financiero del fin de la validacion, y **la
  nombra la razon del puesto 404**, no yo. `cash_burn_calculation` no es un
  hermano: **es el paso de caja que los otros tres llevan dentro** (paso 4 de
  metrics, 5 de validar, 6 de verificar). `validacion_hipotesis_ingresos` es
  vecino: **sale por otra puerta**, el LTV.
- **`construccion_de_leverage`**: **una familia pura de cuatro y una tecnica que
  no es de la familia.** El puro de cuatro lo declara la razon del puesto 1030.
  `tecnica_anclaje_negociacion` es **el anclaje**, tecnica de mesa, no maniobra de
  calendario.
- **`estrategia_de_innovacion_arenas`**: **la madre y sus piezas**, y la vara **ya
  esta escrita en el propio acto**: es la de la **correccion declarada del 13 ago
  2026** (puestos 530 y 863), *"LA MADRE Y SU PIEZA DE ARENAS, y la vara las
  separa"*. Lo que hago es aplicarla al acto entero en vez de a un par.

#### 2.e. NINGUN VEREDICTO SE MOVIO, Y ESTA COMPROBADO Y NO PROMETIDO

**`veredictos_movidos: 0` en las seis filas.** Y el sha256 de los dos ficheros que
podrian haberse movido, tomado **antes y despues** de correr el registrador:

| fichero | antes | despues |
|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | `ea6e850d331d14f0` | **`ea6e850d331d14f0`** |
| `docs/plan/OPERACIONES.jsonl` | `bbdde43a00bdc35c` | **`bbdde43a00bdc35c`** |

`git diff --numstat -- dataset/ docs/plan/` da **0 filas**, y lo unico nuevo en
`docs/plan/` es mi registro. **El marcador no se toco: sigue en 3.388.**

**Y LA LECTURA NO ME OBLIGO A MOVER NINGUNO**, que es distinto de que me haya
callado. Relei entera la razon del puesto **1374** antes de decidir y **se
sostiene sola**. Los puestos **530 y 863** son ya una **correccion declarada
encargada por el auditor**, y mover encima de una correccion declarada sin que
nadie me lo encargue **seria legislar**.

#### 2.f. LO QUE LA LECTURA POR ACTO VE Y LA DE A PARES NO PUEDE VER

**LAS TRES FORMAS DEJAN TRIANGULOS `A` MAS `A` MAS `D` MEDIDOS**, que por **`P.10`
BLOQUEAN LA FUSION** del acto. **No los fabrico: salen de cruzar mi lectura con
los veredictos que ya estaban**, y son la razon entera por la que `P.5` manda leer
el acto y no la pareja.

| acto | el triangulo | de donde sale cada lado |
|---|---|---|
| `cash_burn_calculation` | **1** | `cash_burn`+`verificar` **A** (mi lectura), `verificar`+`validacion_hipotesis` **A** (puesto 451), `cash_burn`+`validacion_hipotesis` **D** (puesto 1374) |
| `construccion_de_leverage` | **3** | `anclaje` es **A** con `construccion_de_leverage` (puesto 878) y **D** con los otros tres (mi lectura), que son **A** con `construccion_de_leverage` (puestos 787, 394, 334) |
| `estrategia_de_innovacion_arenas` | **1** | la madre es **A** con `estrategia_de_innovacion_arenas` (puestos 460 y 1121) y **D** con `y_tecnologia` (puestos 530 y 863) y con `seleccion_arenas` (mi lectura) |

**Y HAY UN PATRON EN LOS TRES, QUE ES EL HALLAZGO DE FONDO DE ESTA TAREA:** en los
tres actos, **el par que rompe la coherencia es siempre el mismo tipo de par**, el
que junta **UN NODO ENTERO CON UNA PIEZA DE SI MISMO** y lo llama `A`. La
contencion (`cash_burn` dentro de los tres modelos, el anclaje dentro del paso 4
de `construccion_de_leverage`, la pieza de arenas dentro de la estrategia madre)
**se leyo como repeticion cuando se miro de a dos**. Leida el acto entero, no lo
es. **Lo traigo medido y no lo adjudico yo.**

#### 2.g. LO QUE NO TOQUE, PORQUE LA FICHA Y EL ENCARGO LO PROHIBEN

**Las 55 lecturas marcadas LECTURA DIRIGIDA no entraron en la cola ni movieron su
marcador** (segunda clausula de la `verificacion`): mi registro vive en un fichero
propio, `docs/plan/OP_L_03_LECTURAS.jsonl`, y **no escribe en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**. **`LD-04` y `LD-08` no se releyeron ni se
les acuno numero nuevo** (adjudicacion 4.1 del acta 19): ninguno de los seis actos
del tramo los contiene.

**Y EL `estado` DE LA FICHA NO SE TOCO** (letra (g), decision del fundador del 4
sep 2026): sigue en `LISTA`, y el sha256 de `OPERACIONES.jsonl` de la tabla de
arriba lo prueba. **La vara es `vuelta150_3_relectura_expediente.py` y la corri en
el bloque de apertura**: sigue dando `OP-L-03` en LISTA sin prueba de ejecucion, y
asi se queda. Quien lea despues, que corra la vara.

#### 2.h. LO QUE QUEDA, CON LA CUENTA EXACTA (letra (c))

**El tramo encargado esta ENTERO: 6 de 6 actos grandes, 9 de 9 pares reales.** No
hubo que parar a media tarea.

**Lo que queda de `OP-L-03`: 34 actos** (los 40 del backlog menos los 6 grandes),
con **44 pares** segun el instrumento (73 menos los 29 del tramo). **Ese 44 es la
cifra del instrumento y casi seguro esta inflada por la misma causa que inflaba el
29**, pero **no lo mido aqui y no lo estimo**: los 34 actos son de tres y cuatro
miembros y hay que resolverlos uno a uno. **Van a la 178.**

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**Todo hash de esta seccion sale de `git log` o `git rev-parse` corrido en esta
vuelta** (`EJECUTOR.md` 1, LA IDENTIDAD SE LEE DE GIT).

| | |
|---|---|
| rama | `pasada-unica` |
| sello de apertura, escrito ANTES de la 1.a operacion | `f3087229` (`SALIDA_V177_HEAD_APERTURA.txt`) |
| sello de cierre, escrito TRAS la ultima operacion | `4cafaf56` (`SALIDA_V177_HEAD_CIERRE.txt`) |
| commits entre los dos sellos | **7** |
| rutas tocadas | **42** (`docs/loop/` 24, `scripts/loop/` 17, `docs/plan/` 1) |
| **el grafo entre los dos sellos** | **`git diff --numstat` sobre `dataset/`, `web/` y `engine/`: 0 filas** |

**LOS SIETE COMMITS, EN SU ORDEN:**

| hash | que cierra |
|---|---|
| `1d18aa04` | el bloque de apertura, corrido antes de la primera operacion |
| `0adc280e` | el esqueleto del reporte, abierto al empezar |
| `2a33a295` | TAREA 1.b, el arnes del rojo (bloqueante) |
| `0c3320dd` | TAREAS 1.c y 1.d, la correccion declarada y el instrumento |
| `4bb4f459` | TAREAS 1.e y 1.f, las tres correcciones chicas con su arnes |
| `d9a8a44c` | la fila de la TAREA 1, anexada al cerrarse |
| `4cafaf56` | TAREA 2, `OP-L-03` |

Los commits posteriores a `4cafaf56` son **el cierre de este reporte y su
archivado**, y por eso no estan en la cuenta de arriba: el sello de cierre se
escribe antes que ellos y no puede nombrarlos.

**EL MARCADOR, RECOMPUTADO AL CIERRE Y NO HEREDADO DE LA APERTURA**
(`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE):

| | total | A | B | C | D |
|---|---:|---:|---:|---:|---:|
| **marcador al cierre** | **3.388** | **551** | **72** | **5** | **2.760** |

Puestos de **1 a 3.388**, **0 huecos** y **0 duplicados**. **Identico al de la
176, y esa es la cifra que la TAREA 2 promete no mover.**

**GATE 0, EL CICLO ENTERO Y EN SU ORDEN, EN LAS DOS PUNTAS**, nunca `run_phase1`
suelto:

| paso | apertura | cierre |
|---|---|---|
| `run_phase1.py --reaplico-curaduria` | **GATE 0: OK**, exit 0 | **GATE 0: OK**, exit 0 |
| `etiquetas_de_cara.py --aplicar` | corrido | corrido |
| `sync_assets_web.py` | corrido | corrido |
| `git diff HEAD --numstat -- dataset/ web/ engine/` | **0 filas** | **0 filas** |
| `engine/run_all_tests.py` | **25/25** | **25/25** |
| `npx tsc --noEmit` | **exit 0, cero lineas** | **exit 0, cero lineas** |
| `pnpm test` | **82 (82) / 1.040 (1.040)** | **82 (82) / 1.040 (1.040)** |

## 4. LA GUARDA DEL COMMIT, USADA EL DIA QUE SERVIA

El encargo manda correrla antes de la primera linea y **no dejarla sin usar el
dia que sirve**. Corrida: **VERDE**. Y adjudico la `M` que el arbol traia **por
el cotejo de blobs y no por el `--numstat`**, que es el segundo motivo de rojo
que la 176 le anadio:

| medicion | resultado |
|---|---|
| filas de `git diff --numstat -- dataset/` | **0** |
| ficheros que `git status --porcelain` nombra | **1** (` M dataset/metadata/master_graph.json`) |
| blob del arbol contra blob de HEAD | **`cb33552aedddab4d` = `cb33552aedddab4d`** |
| veredicto | **CONTENIDO IDENTICO: la `M` es de estado, no de contenido** |

**NO RESTAURE NADA PORQUE NO HABIA NADA QUE RESTAURAR**, y no lo di por bueno sin
medirlo: lo midio la guarda.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**D.1. HICE SEIS ACTOS DONDE EL ENCARGO NOMBRA CINCO, Y CAMBIE EL PUNTO DE
PARTIDA.** El encargo manda empezar por `cierre_segun_complejidad_venta`, *"el
mayor del reparto"*, y seguir por los cuatro de cinco. **En el universo
adjudicado en la vuelta 15 (corte 3.388) eso ya no describe el reparto**: hay
**dos** actos de seis y el mayor es el otro, con 8 pares. **Hice los seis
grandes.** **LO DISCUTIBLE:** que interprete *"LOS ACTOS GRANDES PRIMERO"* como la
instruccion de fondo y la lista de actos como su ilustracion al corte viejo. Si
la lista era la instruccion, hice un acto de mas.

**D.2. EL TOPE DE 10 MINUTOS DE LA TAREA 1.f ES UN NUMERO DE JUICIO.** Que el
tamano **se compute** no es discutible y esta adjudicado. **Que el tope sea 10 y
no 8 ni 12 lo elegi yo**, con los numeros de la 176 delante (el mas largo fue
15,9, los otros ocho entre 1,1 y 3,9). **LO DISCUTIBLE:** un tope de 10 con el
coste maximo medido da tramos de **6**, o sea **16 tramos** para una nomina de 92,
casi el doble de los 9 de la 176. Puede ser demasiado grano.

**D.3. ANADI UN CASO AL ARNES DEL ROJO Y PUBLICO 20 DONDE EL ENCARGO ESPERA 19.**
`H_la_medicion_viva_trae_hallazgos` no me lo pidio nadie. **Mi razon** es que el
propio encargo dice que un esperado computado que no puede fallar nunca es un
adorno, y sin ese caso `0 == 0` pasaria. **LO DISCUTIBLE:** que anadir un caso a
un arnes ajeno en la misma vuelta en que se le corrige otro es tocar dos cosas
donde el encargo pedia una.

**D.4. RENOMBRE EL CASO `H_el_texto_nombra_las_tres`.** Pasa a
`H_el_texto_nombra_TODOS_los_hallazgos`. **Mi razon** es que el nombre viejo
publica una cifra que ya no es cierta, y comprobe antes que **ningun codigo
depende del nombre** (solo lo citan actas y reportes). **LO DISCUTIBLE:** que el
acta 176 y el encargo lo nombran por su nombre viejo, y a partir de aqui esas
citas apuntan a un caso que se llama de otra manera.

**D.5. TOQUE UN FICHERO DE UNA VUELTA PASADA, `vuelta176_bateria_por_tramos.py`.**
La correccion del `D.5` del acta vive ahi porque **es el fichero que la 181 va a
clonar**, y arreglarlo en su sitio es lo unico que hace que el clon herede el
arreglo. **LO DISCUTIBLE:** que modifica el lanzador con el que la 176 ya corrio
su bateria, asi que ese fichero ya no es exactamente lo que corrio aquel dia.

**D.6. LA MEDICION DE DESFASE DE LA APERTURA SE TOMO AL CIERRE.** Es la misma
especie que el `D.1` del acta 176, que el auditor acepto **una vez** diciendo *"no
se repite"*. **Y aqui se repitio.** No la escondo y digo la causa exacta abajo, en
la seccion 8. **LO DISCUTIBLE:** si la prueba que la sostiene (el arbol identico
en las dos puntas, y la salida byte a byte igual) basta, o si esto es
sencillamente la misma caida otra vez.

**D.7. NO MOVI NINGUN VEREDICTO AUNQUE EL ENCARGO ME AUTORIZABA HASTA DOS.** La
letra (e) permite mover clases con correccion declarada y recomputo. **Mi razon**
es que ninguna de las tres lecturas me obligo: relei entera la razon del puesto
1374 y se sostiene sola, y los puestos 530 y 863 **ya son** una correccion
declarada encargada por el auditor. **LO DISCUTIBLE:** que dejo cinco triangulos
`A` mas `A` mas `D` medidos y sin resolver, y cabe leer que la letra (e) me pedia
resolver hasta dos de ellos en vez de traerlos.

## 6. LAS PREGUNTAS

**P.1. EL BACKLOG DE `OP-L-03` ESTA INFLADO Y NO SE CUANTO.** Medido en el tramo
grande: de **29** pares que el instrumento da por leer, **9** son reales; **20**
son pares cuyos dos extremos son hoy el mismo nodo. **La causa es estructural**:
el backlog se computa sobre el archivo de componentes del corte **3.388** y la
campana ha fundido nodos despues. **No extrapolo a los 34 actos que no mire.** La
pregunta es si la 178 debe **re-medir el backlog entero con el resolutor puesto**
antes de seguir leyendo, en vez de leer contra una lista que sabemos inflada.

**P.2. ¿SE ARREGLA `backlog_l03_vuelta14.py` O SE LE PONE UN FILTRO DELANTE?** No
lo toque porque es el instrumento que la ficha cita y cambiarlo cambia una cifra
adjudicada en la vuelta 15. Pero hoy **cuenta como pendiente trabajo que no
existe**.

**P.3. ¿QUE SE HACE CON LOS CINCO TRIANGULOS `A` MAS `A` MAS `D`?** Por `P.10`
bloquean la fusion de sus tres actos. Los traigo medidos y con el patron
identificado (siempre el mismo tipo de par: **un nodo entero llamado `A` con una
pieza de si mismo**). No se si eso es una correccion de tres pares, una regla
nueva de lectura, o cosa juzgada.

## 7. PENDIENTES DE DOCTRINA

**PD.1. `arneses_que_faltan()` CIEGA A LOS HERMANOS DE SU MISMA VUELTA.** Solo
mira arneses de vuelta **estrictamente posterior** a la ultima representada en la
nomina. Medido hoy: con la entrada de la 1.b dentro, **me dijo que no faltaba
ninguno cuando faltaban dos mios**. Los anadi a mano. **No toque la funcion**
porque no hay regla escrita que diga cual es su vara, y cambiarla es cambiar la
guarda que la casa usa para saber si la nomina esta al dia.

**PD.2. LA CONVENCION DE BYTES, POR CUARTA ACTA.** Sigue sin fijar y el auditor la
subio al fundador (acta 176, seccion 8, punto 1). **Publico las dos** mientras
tanto. En esta vuelta coinciden porque todo se escribe con LF.

**PD.3. ¿UNA COMA FINAL ES UNA SENTENCIA DE CODIGO?** Mi instrumento dice que si,
porque es un token que no es texto, y por eso discrepo del **0** del auditor con
un **1**. Es defendible al reves: una coma final no cambia lo que el programa
hace. **No lo decido yo y no le meti una excepcion al instrumento**, porque una
excepcion escrita a ojo es exactamente lo que este instrumento vino a sustituir.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**CAIDA 1. MI BLOQUE H.6 PUBLICO UNA CIFRA MALA Y EL ACTA TENIA RAZON.** Busque el
literal `SALE VACIO` y publique **un solo fichero viejo**; el acta 176 dice **dos
docstrings**. **El acta acierta y yo no**: en `vuelta176_esqueleto_reporte.py` la
frase **parte en dos por un salto de linea** y mi busqueda literal no la ve.
Re-medido normalizando espacios: **los dos**. **La cace yo, en la misma vuelta, y
esta escrita asi en el commit `1d18aa04`.**

**CAIDA 2. LA PRIMERA VERSION DE `cotejar_clon_declarado.py` CLASIFICABA AL
REVES.** Tapaba caracter a caracter, cosa que **conserva la longitud**, asi que dos
cadenas distintas seguian difiriendo. Contra el par del auditor daba **SENTENCIAS
33 y LITERALES 0**, **justo del reves que su medicion**. **Lo que me hizo mirar fue
el desacuerdo con el acta**, no una prueba mia. Reescrito por token.

**CAIDA 3. MI PROPIO ARNES ME TUMBO UN ERROR DE DISENO.**
`--exigir-maquina-identica` enrojecia con un cambio de **solo texto**, que es
justo lo que el instrumento existe para excusar: **inutil para su unico uso**. Lo
cazo el arnes con un `exit 1` donde esperaba `0`. Ahora hay dos carriles.

**CAIDA 4. UNA ASSERTION MIA ESTABA MAL Y EL CODIGO BIEN.** En el arnes de la 1.e
comprobaba `[CIERRE]` cuando la etiqueta va acolchada a ocho, `[CIERRE  ]`.
Corregida en el arnes, no en el sujeto.

**CAIDA 5, Y ES LA QUE MAS ME PESA: LA MEDICION DE DESFASE DE LA APERTURA SE TOMO
AL CIERRE, QUE ES LA ESPECIE QUE EL ACTA 176 ACEPTO DICIENDO "NO SE REPITE".**

**LA CAUSA, MEDIDA Y NO SUPUESTA, Y NO ME EXCULPA:** el bloque de apertura del que
clone (`vuelta175_apertura.py`) **no corre el paso del desfase y el de cierre
si**. La palabra "desfase" sale **0** veces en aquel y **2** en el de cierre. Como
`tallar_cabecera_reporte.py --fase04` exige **las dos columnas**, la apertura coja
hacia **imposible** que el tallador saliera verde por la izquierda. **Corri mi
bloque de apertura entero y aun asi faltaban esas 2 celdas.**

**COMO SE DESCUBRIO, Y TIENE GRACIA: LA GUARDA QUE PUSE EN LA TAREA 1.e SE
ESTRENO CAZANDO A SU AUTOR.** El tallador salio **ROJO por 2 celdas, las 2 del
lado APERTURA**, y **dejo el rastro que hasta esta vuelta no dejaba**, en
`docs/loop/SALIDA_V177_T1E_RECHAZO_REAL.txt`. **El 37 de la 176 no se pudo
re-verificar; este 2 si, y esta en disco.**

**LO QUE HICE, DICHO ENTERO:** tome la medicion al cierre y **la declaro como
tardia**, con la prueba que la sostiene: `git diff --numstat` entre los dos sellos
da **0 filas** sobre `dataset/`, `web/` y `engine/`, y la salida de apertura sale
**identica byte a byte a la de cierre** (sha256 **`7d683eea4700f18b`** las dos), o
sea que el arbol que ese instrumento lee **es el mismo en las dos puntas**. **Y
arregle el bloque de apertura** para que desde la 178 se tome en su sitio.

**LO QUE NO HAGO ES LLAMARLO OTRA COSA.** El auditor escribio *"no se repite"* y se
repitio. Va marcado como discutible `D.6` y lo adjudica quien manda.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 177 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V177_BATERIA.txt`.
**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por
`scripts/loop/cerrar_reporte.py`, no tecleados: **0 bytes**.

ATRIBUCION: NADIE LA CORRIO, NI EL EJECUTOR NI EL AUDITOR, Y NO ES UN OLVIDO SINO LA CADENCIA. La bateria corre CADA CINCO vueltas en una vuelta propia que no lleva nada mas (AUDITOR.md 6.1, decision del fundador del 5 sep 2026), y el acta 176 punto 7.8 adjudico que LA PROXIMA ES LA 181 Y NO LA 180, porque el contador se reancla a la vuelta que de verdad la corrio y la 175 murio sin producir una linea. La ultima corrida real es la de la vuelta 176, verificada por el auditor: 60197 bytes, 995 lineas, sha256 2f86d9e075d4e5ce, 88 de 88 entradas con su doble corrida. ESTA VUELTA NO LA CORRIO Y NO DEBIA CORRERLA, y su fichero propio mide CERO BYTES porque no existe. LO QUE ESTA VUELTA SI LE HIZO A LA BATERIA, y vive entero en la TAREA 1 de este mismo reporte: se remedio su UNICO ROJO (el arnes de la vuelta 166, que medía contra un 3 tecleado y hoy sale exit 0 con 20 casos), la nomina paso de 88 a 92 entradas sin podar ninguna, y el reparto en tramos gano un TOPE POR MINUTOS computado del reloj medido de esa misma corrida de la 176.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
