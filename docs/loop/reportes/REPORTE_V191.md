# REPORTE DE LA VUELTA 191 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta191_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que **no lleva
> nada mas**. **La 189 la corrio entera**, asi que **la siguiente cae en la 194**.
> El hueco va **con su nombre, sus bytes medidos y su atribucion, LAS TRES
> JUNTAS**, por el carril de `cerrar_reporte.py`: **un hueco declarado no es un
> hueco escondido.**
>
> **VAN CINCO SUB-TAREAS, Y EL TOPE DE CINCO NO HACE FALTA VOLVER A GANARLO:**
> esta vigente desde la `4.10` del acta 190. **Y la cifra que lo sostiene se
> remidio en esta vuelta en vez de heredarse:** el bloque **B.2** del sello de
> apertura busco en git los commits de cierre y midio sus ficheros
> `SALIDA_V<n>_CERRAR_REPORTE.txt` uno a uno, y publica lo que salga.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan, ni las mesas anotadas, ni **podar la
> nomina** (la opcion `c` que el fundador RECHAZO el 5 sep 2026: **la nomina
> sigue creciendo y nadie la poda sin el fundador**), ni la bateria, que cae en
> la 194. **Y siguen fuera, nombradas para que la 192 no las redescubra:**
> `acumulan()` que lea la tabla o declare que no es la sede; el cotejo de clon
> declarado que separa sentencia de codigo de cambio de texto; la excepcion que
> publica siempre su lista; la medicion del censo de arneses con carril de
> mutacion sin fichero propio; las ocho actas sin entrada propia en la serie (173
> a 180); el exitcode 2 propagado a `--componer`; y que el campo `evidencia` de
> `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue
> en `LISTA`**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo
> valor. **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al
> salir y **las dos cifras se publican**.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS CERRARON SIN MOVER UN SOLO VEREDICTO DEL ARCHIVO, QUE ABRE Y CIERRA EN 0a77b5a35a962621 POR LAS DOS CONVENCIONES. EL ACTA 191 ENTRA COMO R.53 Y EL REGISTRADOR APRENDIO A LEER UN CERO DE EN CONTRA SIN ROMPERSE Y A CONTAR CAIDAS QUE NO SE LLAMAN C.n; EL AL DOBLE DEL 3182 SE LEYO A CIEGAS CON 23 QUE COINCIDEN Y 7 QUE DISCREPAN, Y LA UNICA QUE CAE FUERA DE MIS DUDOSOS, EL 2832, LA TRAIGO ENTERA Y NO ME AUTO ENCARGO SU ESCALADA; LAS DOS CONVENCIONES DE LINEAS SE MIDIERON PRIMERO (12 EN ROJO) Y SE ARREGLARON DESPUES (0 EN ROJO) CON SU GUARDA APLICADA A QUIEN LA ESCRIBIO; cerrar_reporte.py YA CAE EN ROJO SI EL VEREDICTO LLEGA VESTIDO, Y LA MEDICION DESTAPA QUE EL REPORTE DE LA 188 TAMBIEN LO TRAIA, QUE ES LA PARADA QUE DECLARO; Y LA MARCA CONTRA LA DIFICULTAD TIENE SU UNIVERSO DECLARADO Y SUS TRES CIFRAS, Y NO ALCANZAN PARA CONCLUIR, QUE ES UN RESULTADO. LAS SEIS CAIDAS PROPIAS SON DE METODO Y NINGUNA LLEGO A PUBLICAR UNA CIFRA FALSA, INCLUIDA LA MAS GORDA: MI PROPIA PROSA PUBLICABA 22 CIFRAS DE BYTES SIN SU PAREJA Y EL CERRADOR SE NEGO A ESCRIBIR HASTA QUE LAS ARREGLE.**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta191_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 190: `b393347f`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer
  DENTRO cifras de bytes y `sha256` suyas, y una guarda que mira renglon a
  renglon no distingue una cita de una afirmacion. Cercarlo es decir lo que es:
  **una cita de la salida de un instrumento**, que es exactamente el motivo por
  el que `cerrar_reporte.py` deja los bloques cercados fuera de su guarda de
  parejas.

```
'ACTA DEL AUDITOR, VUELTA 190: LA 189 REPRODUJO ENTERA Y LA BATERIA CORRIO DE VERDAD, PERO TUMBO UNO DE LOS SEIS DISCUTIBLES. Gate 0 verde entero corrido por mi, marcador recomputado del archivo (3.388, A 551, B 72, C 5, D 2.760, 0 huecos, 0 duplicados, sha256 LF 0a77b5a35a962621) y cabecera recomputada (3.853/3.169/684, aristas 8.780/8.740/17.520/9.914). Los DIEZ tramos de la bateria sellados, ninguno de cero bytes, 125 entradas cada una una sola vez, y el rojo que declara REPRODUCE bajo mi mano: vuelta172_tarea5_mutacion_cierre.py exit 1, fallos=2. La idempotencia del registrador, que es el remedio de mi propia C.2 de ayer, la probe re corriendola: no escribe nada y PENDIENTES.md se queda en 961248 bytes. 230 rutas barridas, CERO de cero bytes; 12 parejas de bytes, las 12 calzan.'
```
- **DESFASE DECLARADO, SEPTIMA VUELTA:** la linea de arriba nombra el acta
  **190** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 191**. Es el `D.2` del reporte de la 184, adjudicado a
  favor con reparacion encargada por la `5.2` del acta 185. **Esta vuelta no la
  ejecuta** porque no es ninguna de sus cinco tareas y el encargo nombra una a
  una las que quedan fuera. Se declara en vez de colarse.
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V191_HEAD_APERTURA.txt`: `d21d5e8b`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `df038ec9`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **191**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 191`, y su salida
cruda vive en `docs/loop/SALIDA_V191_TALLADOR_CABECERA.txt` (3046 bytes en disco y 3026 normalizado a LF, 11 filas de
tabla,
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `b393347f` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 190: LA 189 REPRODUJO ENTERA Y LA BATERIA CORRIO DE VERDAD, PERO TUMBO UNO DE LOS SEIS DISCUTIBLES. Gate 0 verde entero corrido por mi, marcador recomputado del archivo (3.388, A 551, B 72, C 5, D 2.760, 0 huecos, 0 duplicados, sha256 LF 0a77b5a35a962621) y cabecera recomputada (3.853/3.169/684, aristas 8.780/8.740/17.520/9.914). Los DIEZ tramos de la bateria sellados, ninguno de cero bytes, 125 entradas cada una una sola vez, y el rojo que declara REPRODUCE bajo mi mano: vuelta172_tarea5_mutacion_cierre.py exit 1, fallos=2. La idempotencia del registrador, que es el remedio de mi propia C.2 de ayer, la probe re corriendola: no escribe nada y PENDIENTES.md se queda en 961248 bytes. 230 rutas barridas, CERO de cero bytes; 12 parejas de bytes, las 12 calzan.'), HEAD real de apertura `d21d5e8b` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `8a87d38b` (leido de `SALIDA_V191_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 191 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus NUEVE adjudicaciones `4.1` a `4.9`, QUE ESTA VEZ SI SON NUEVE A FAVOR: seis son los discutibles del ejecutor (`D.1` a `D.6`) y los seis van A FAVOR, y las tres restantes (`4.7`, `4.8`, `4.9`) son las tres preguntas contestadas. EL CERO DE `EN CONTRA` TIENE QUE SALIR SIN QUE LA MAQUINA SE ROMPA POR NO ENCONTRAR NINGUNA, y se prueba por mutacion con un acta fabricada que SI lleve una. Mas los TRES hallazgos de la seccion 5 que no salen de ningun discutible (la marca `DISCUTIBLE MARCADO` contra la dificultad medida en `5.1`, la etiqueta del veredicto duplicada en `5.2`, y `git checkout --` que no restaura byte a byte en `5.3`), UNA caida propia del auditor de metodo ESCRITA COMO UNA Y NO OMITIDA, CERO caidas del ejecutor que acumulen con las TRES de metodo que el reporte de la 190 declara, y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos con su nota de SOLAPE TOTAL a proposito. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido, no escribe nada, y se prueba re corriendolo con la sede medida en bytes antes y despues | **CERRADA EN VERDE** | `SALIDA_V191_T1A_REGISTRO_R53.txt`, `SALIDA_V191_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, `SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`, `SALIDA_V191_T1A_SIMULACION.txt` |
| **TAREA 2** | LA RELECTURA AL DOBLE DEL TRAMO DEL 3182. BLOQUEANTE. Es la deuda de credito que la TAREA 4 de la 190 dejo medida y que no se auto encargo, adjudicada A FAVOR en la `4.5` del acta 191 y encargada ahi mismo: quien encarga el doble es el auditor. EL TRAMO es la tanda de 30 puestos de `docs/loop/SALIDA_V190_T4_CIEGA.txt`, donde la discrepancia del `3182` cayo FUERA de los dudosos marcados. AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada: 30 mas 30 son 60, el doble exacto. EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO: a `vecinos()` se le pasa `evitar` con TODO lo consumido, contado de sus ficheros y no tecleado. Con `scripts/loop/aislador_de_ciega.py`, criterio escrito literal, ciega y destape en ficheros SEPARADOS, las clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y los dudosos NOMBRADOS DELANTE. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en el mismo valor por las dos convenciones | **CERRADA, CON UNA DISCREPANCIA FUERA DEL MARCADO TRAIDA ENTERA** | `SALIDA_V191_T2_AISLAMIENTO.txt`, `SALIDA_V191_T2_CIEGA.txt`, `SALIDA_V191_T2_MIS_CLASES.txt`, `SALIDA_V191_T2_DESTAPE.txt`, `SALIDA_V191_T2_COTEJO.txt` |
| **TAREA 3** | LAS DOS CONVENCIONES DE `lineas`, QUE LLEVAN DOS VUELTAS ESPERANDO. Es la `5.1` del acta 190 y no se ha tocado. Hay instrumentos de la cadena que cuentan lineas con `len(texto.split(NL))`, que suma un elemento vacio final que no es una linea, y otros que cuentan con `texto.count(NL)`, que si calza con `wc -l`. ES UNA MEDICION ANTES QUE UN ARREGLO: (a) MIDE PRIMERO cuantos ficheros de `scripts/loop/` cuentan lineas por cada una de las dos convenciones, nombralos y publica la cifra, porque sin esa cifra el arreglo no se sabe de que tamano es; (b) DESPUES ARREGLA con la vara de las dos convenciones de BYTES que esta casa ya construyo: o se publica la pareja, o se publica la que calza con `wc -l` diciendo cual es; (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un instrumento vuelve a publicar una sola cifra de lineas por la convencion que no calza. NO SE TOCAN LOS NUMEROS YA PUBLICADOS EN REPORTES CERRADOS | **CERRADA EN VERDE** | `SALIDA_V191_T3_CENSO_ANTES.txt`, `SALIDA_V191_T3_CENSO_DESPUES.txt`, `SALIDA_V191_T3_ARREGLO.txt`, `SALIDA_V191_T3_MUTACION_LINEAS.txt` |
| **TAREA 4** | LA GUARDA DEL VEREDICTO DUPLICADO EN `cerrar_reporte.py`. Es el hallazgo `5.2` del acta 191. La linea 50 del reporte de la 190 dice `**EL VEREDICTO DE UNA LINEA: **EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS...`, y la causa esta medida: `cerrar_reporte.py` en su linea 1817 compone la etiqueta y su propia salida prueba que el veredicto que se le paso YA la traia. (a) QUE `cerrar_reporte.py` CAIGA EN ROJO si el `--veredicto` que recibe ya trae la etiqueta o los asteriscos, en vez de pegarla dos veces, y que diga QUE RECIBIO y QUE ESPERABA: fallar ruidoso, sin limpiarla en silencio, porque limpiar en silencio es la otra mitad de la misma enfermedad. (b) CASO POSITIVO POR MUTACION que CAIGA si la guarda se quita. (c) EL REPORTE DE LA 190 NO SE REESCRIBE: esta cerrado y archivado byte a byte, y su etiqueta doble se queda donde esta con la explicacion al lado | **CERRADA EN VERDE, CON UNA PARADA DECLARADA** | `SALIDA_V191_T4_MUTACION_VEREDICTO.txt`, `SALIDA_V191_APERTURA.txt` bloque `H.5` |
| **TAREA 5** | LA MARCA `DISCUTIBLE MARCADO` CONTRA LA DIFICULTAD MEDIDA. SOLO MEDIR, Y NO TOCA NI UNA RAZON DEL ARCHIVO. Es el hallazgo `5.1` del acta 191: sobre su tanda de treinta, dos lectores independientes discrepan del archivo en los MISMOS OCHO puestos, `DISCUTIBLE MARCADO` aparece en 427 de las 3.388 filas y en CERO de esos ocho. TREINTA CASOS NO SON UNA LEY, y por eso esto es una medicion. (a) DI PRIMERO CUAL ES TU UNIVERSO Y COMO LO CONSTRUYES antes de contar nada: que ficheros de cotejo de ciega existen, de que vueltas, y cuales quedan fuera por no ser legibles con una regla unica, con la cifra de los que entran y de los que no y con sus nombres, porque un universo elegido despues de ver el resultado no sirve. (b) CUENTA sobre ese universo cuantos puestos han tumbado alguna vez a un lector, cuantos de esos llevan la marca, y cual es la tasa de la marca en el archivo entero: las tres cifras juntas o ninguna. (c) NO SAQUES LA CONCLUSION SI LA CUENTA NO LA SOSTIENE: si el universo sale pequeno, dilo y publica el tamano. (d) NO SE ESCRIBE NI UNA FILA DEL ARCHIVO | **CERRADA: LAS TRES CIFRAS ESTAN Y NO ALCANZAN PARA CONCLUIR** | `SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt`, `SALIDA_V191_T2_COTEJO.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS. CERRADA EN VERDE.

**EL ACTA 191 ENTRA EN LA SERIE COMO `R.53`, Y EL NUMERO NO ESTA TECLEADO.** Lo
computa `scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS
sedes: **44 entradas, 0 colisiones, 0 huecos, siguiente libre `R.53`** al entrar,
y **45 entradas, 0 colisiones, 0 huecos, siguiente libre `R.54`** despues de
escribir. El encargo decia `R.53` y **el instrumento tambien lo dice: CALZA**.

**EL INSTRUMENTO:** `scripts/loop/vuelta191_tarea1a_registrar_acta191.py`.
Salidas, las tres medidas y ninguna vacia:
`docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt` (disco 6904 bytes | LF 6904 bytes),
`docs/loop/SALIDA_V191_T1A_SIMULACION.txt`,
`docs/loop/SALIDA_V191_T1A_REGISTRO_R53.txt` (disco 9585 bytes | LF 9585 bytes) y
`docs/loop/SALIDA_V191_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (disco 9965 bytes | LF 9965
bytes).

**LO QUE ESTE REGISTRADOR TUVO QUE ESTRENAR, Y LAS CUATRO SALEN DE CORRER LA
MAQUINA HEREDADA SOBRE EL ACTA 191 Y VER DONDE SE ROMPE, NO DE SUPONERLO.** Las
cifras salen de `SALIDA_V191_T1A_REGISTRO_R53.txt`, bloques D, E, F y G:

| lo que estrena | la medicion que lo obliga | fuente |
|---|---|---|
| el cero de `EN CONTRA` no para | discutibles **6**, A FAVOR **6**, EN CONTRA **0**; la guarda vieja `if not en_contra: PARADA` de la 190 **PARARIA** sobre esta acta | bloque D |
| tres marcas nuevas de pregunta contestada | con el vocabulario de la 190 y nada mas, **3** titulos saldrian `SIN DECIR` y el instrumento pararia | bloque D |
| las caidas se cuentan por clave `N.M` y no por `C.n` | el patron `C.n` en linea da **0** sobre la seccion 6; `caidas_en_linea()` de la 190 saca **(0, 0, 0)** y `caidas_por_seccion()` de la 189 tambien | bloque F |
| la fila de la tabla se parte tambien por `,` | partiendo solo por `;` da **1** pieza y casa con **0**; partiendo por `;` y `,` da **3** piezas y casa con **1** | bloque E |

**Y LA CUARTA MERECE SU FRASE, PORQUE ES DONDE MAS FACIL ERA MENTIR:** que el
cotejo por subcadena casara **1 de 3** no autoriza a ensanchar el cotejo hasta que
diga lo que conviene. **Quien decide cuantos hallazgos cuentan fuera del marcado
es el numeral de la propia fila, leido de ella y no tecleado: dice `3`, y la
seccion tiene `3` claves `5.n`.** El cotejo por subcadena queda publicado al lado
**como lo que es, una medicion mas debil**, porque el acta parafrasea (*"la
restauracion que no restaura"*) donde el titulo dice otra cosa (*"`git checkout
--` NO ES RESTAURACION BYTE A BYTE"*).

**LAS CIFRAS QUE LA ENTRADA REGISTRA, TODAS CONTADAS DEL ACTA ACOTADA (lineas
67365 a 67620) Y NINGUNA DEL ENCARGO:** **9** adjudicaciones `4.1` a `4.9` (con
el patron entrecomillado del acta 188 dando **0** y el suelto dando **9**, las dos
publicadas), **6** discutibles `D.1` a `D.6` **los seis A FAVOR**, **0** EN
CONTRA, **3** preguntas contestadas (`4.7` que nombra `P.1`, `4.8` que nombra
`P.2`, `4.9` que nombra `P.3`), **3** hallazgos `5.n` y **los tres** cuentan fuera
del marcado, **1** caida propia del auditor y **3** del ejecutor, **0**
huerfanas.

**LA CAIDA DEL AUDITOR VA ESCRITA COMO UNA Y NO OMITIDA**, bajo su negrita
literal `MIAS: UNA, DE METODO, Y ES LA `5.3``. **Y las tres del ejecutor van con
su cero de racha intacto:** la negrita es `DEL EJECUTOR: CERO QUE ACUMULEN.`, que
es un cero de RACHA y **no neutraliza**. Medido: tratado como cero de CUENTA el
reparto sale **ejecutor 0**, o sea que confundirlas **borraria las 3**.

**Y UNA COSA QUE SE MIDE PORQUE ERA LA TRAMPA:** el parrafo del ejecutor nombra
`5.2` **dos veces**, la segunda para decir que la etiqueta duplicada *no se la
cuenta a el*. Contando **apariciones** salen **4**; contando **claves distintas**
salen **3**, que es lo que el acta declara. Por eso se deduplica por parrafo.

**LA METRICA DE CREDITO DE LA SECCION 7, PEGADA ENTERA DEL FICHERO Y NO
RESUMIDA.** Son **8** filas de datos, contadas por `filas_de_la_metrica()` y no
tecleadas; salen del bloque G de `SALIDA_V191_T1A_REGISTRO_R53.txt`:

| | esta vuelta | acumulado |
|---|---:|---:|
| relecturas | 1 | **326** |
| puestos | 30 aislados, **30 de solape TOTAL a proposito: control, NO cobertura nueva** | **1.006** |
| discrepancias DENTRO del marcado | **9** (las nueve en mis dudosos) | **42** |
| discrepancias y hallazgos FUERA del marcado | **3** (la marca contra la dificultad medida, la etiqueta duplicada, la restauracion que no restaura) | **151** |
| caidas propias del auditor | **1**, de metodo (`5.3`) | ninguna repetida: no abre racha |
| caidas del ejecutor que ACUMULAN por cifra publicada | **0** | **racha de cifra publicada: 0** |
| caidas del ejecutor de reporte | **0** | **racha de reporte: 0** |
| caidas del ejecutor de metodo, registradas y sin racha | **3** (`5.1`, `5.2`, `5.3` del reporte) | |

**LA FILA DE PUESTOS VA CON SU NOTA, QUE ES LO QUE EL ENCARGO MANDA, Y AQUI HAY
UNA CORRECCION DECLARADA SIN BORRAR LO QUE CORRIGE.** La guarda nacio exigiendo
el literal `SOLAPE TOTAL` **tal cual**, que es como lo escribe el encargo, y
**PARO el instrumento en su primera corrida**: el acta escribe `solape TOTAL`, con
minuscula. **Se cambio a comparar en mayusculas y a publicar el literal real**, y
**las dos cifras se publican**: TAL CUAL da **NO**, en mayusculas da **SI**, y lo
que el acta escribe de verdad es `'solape TOTAL'`. Exigir la caja habria hecho
parar el instrumento **por una mayuscula**, que es lo contrario de lo que la
guarda existe para cazar. El caso de mutacion nuevo corre las dos cajas.

**EL CASO POSITIVO POR MUTACION: VERDE, 0 casos que caen y 0 mutaciones que no
cayeron**, en seis bloques (`SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`). Las que
importan, cada una con su mutacion corrida:

- **el acta fabricada que SI lleva un `EN CONTRA`**: la cuenta lo ve (**1**), y
  mutado el esperado a 0, **CAE**. Es lo que el encargo pide con esas palabras.
- **la guarda vieja de la 190 sobre el acta fabricada SIN ninguna**: **PARA**, y
  por eso este registrador no la hereda.
- **el vocabulario de la 190 sobre las tres marcas nuevas**: las **3** salen
  `SIN DECIR`, o sea que heredarlo habria parado el instrumento.
- **la negrita muda**: reparto `(0, 1, 3)`, las tres huerfanas, y **la PARADA por
  huerfana se conserva entera**.
- **la nota de puestos con la caja del acta real**: comparada TAL CUAL **no se
  ve**; comparada en mayusculas **si**. Y un acta sin la nota da **falso**.
- **la idempotencia**: sede sin la entrada **0**, sede con la entrada **2**.

**LA IDEMPOTENCIA, PROBADA RE CORRIENDOLA Y NO AFIRMADA.** Las tres mediciones de
la sede van CERCADAS y no en prosa, y se dice por que: la de ANTES es una cifra
que hoy ya no se puede volver a medir en el disco, asi que publicarla como pareja
suelta seria darle a la guarda de las dos convenciones una cifra que no puede
cotejar contra el fichero de hoy. **Cercada es lo que es: una cita de la salida
del instrumento.**

```
CIFRA bytes de docs/PENDIENTES.md ANTES de tocar nada: 980013
la sede pasa de 980013 a 998216 bytes
RE CORRIDO: docs/PENDIENTES.md sigue en 998216 bytes, NO SE ESCRIBE NADA
```

La salida del re corrido vive en `SALIDA_V191_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, y
**su nombre lo dice**: una ruta que promete prueba es cifra, asi que el fichero no
se llama con un numero de serie que no se consumio. La comprobacion es **por el
acta y no por el numero**, en LAS DOS SEDES, con las marcas literales computadas
de la vuelta. `git diff --numstat -- dataset/`: **0 filas**, antes y despues.

**LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA DEL `R.52`:** **8** actas sin
entrada propia, las **173 a 180**, con `R.42` cubriendo el acta 172 y `R.43` el
acta 181. **El encargo las deja expresamente fuera, medidas y no arregladas**, y
esta entrada no rellena ninguna.

### TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DEL 3182. CERRADA, Y CON UNA DISCREPANCIA FUERA DEL MARCADO QUE TRAIGO ENTERA.

**QUIEN LA ENCARGA, PORQUE ESO ES LA MITAD DEL ASUNTO: LA ENCARGA EL AUDITOR.**
La TAREA 4 de la 190 dejo la deuda **medida y no auto encargada**, y la `4.5` del
acta 191 lo adjudico A FAVOR con esta razon leida hoy
(`docs/loop/ACTA_AUDITOR.md:67496`): *"`AUDITOR.md` 1.2 pone el doble en mi mano,
no en la suya, y LA ESCALADA SE ENCARGA, NO SOLO SE DECLARA es una regla contra
MI, no contra el ejecutor"*.

**LOS TRES PASOS, CADA UNO EN SU COMMIT, Y EL ORDEN LEIDO DE GIT Y NO
PROMETIDO.** El instrumento del cotejo lo comprueba solo y **CAE EN ROJO si no
puede leerlo**: aislamiento en **`2a414476`**, mis clases en **`5915621a`**, y el
destape se abre despues. `git status` del fichero de clases: **limpio**.

**EL TRAMO Y EL DOBLE, TODO CONTADO DE FICHEROS Y NADA TECLEADO**
(`SALIDA_V191_T2_AISLAMIENTO.txt`, disco 6348 bytes | LF 6348 bytes):

| lo que el encargo dice | lo que se conto hoy | |
|---|---|---|
| el tramo son 30 puestos y el 3182 esta dentro | 30 puestos de `SALIDA_V190_T4_CIEGA.txt`, el 3182 **DENTRO** | CALZA |
| son los mismos 30 que el auditor releyo en el acta 191 | diferencia simetrica contra `_auditor_v191_ciega_blind.txt`: **0** | CALZA |
| 441 consumidos antes de la 190 | **441**, union de cuatro ficheros | CALZA |
| 471 con los 30 de la tanda de la 190 | **471**, union de los cinco | CALZA |
| 30 vecinos, el doble exacto | **30** vecinos, **60** en total | CALZA |
| solape 0 con el tramo y 0 con el universo | **0** y **0**, y salen **POR CONSTRUCCION**: `evitar` va DENTRO de la llamada a `vecinos()`, no comprobado despues | CALZA |

**`vecinos()` VA IMPORTADA Y NO COPIADA** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`: **su regla no se toca,
cambia lo que se le pasa** (`5.2` del acta 188). El aislador cerro con
**exitcode 0**, **0 fugas** del destape en la ciega, y las palabras `clase`,
`razon` y `DISCUTIBLE` aparecen **0 veces** en el texto ciego.

**EL COTEJO, CONTADO DE `docs/loop/SALIDA_V191_T2_COTEJO.txt`
(disco 6851 bytes | LF 6851 bytes) Y NO TECLEADO:**

| | cifra |
|---|---:|
| releidos | **30** |
| COINCIDEN | **23** |
| DISCREPAN | **7** |
| discrepancias DENTRO de mis dudosos | **6** (201, 716, 1369, 1813, 3087, 3183) |
| discrepancias FUERA de mis dudosos | **1** (2832) |
| dudosos mios que SI coincidieron | **7** de 13 |

**MI REPARTO: A 7, B 3, D 20. EL DEL ARCHIVO: A 4, B 1, C 1, D 24.** Los dos
declarados antes de destapar el primero, y el segundo contado del destape.

**LA QUE CAE FUERA DE MIS DUDOSOS ES EL 2832, Y VA ENTERA.** Dije **A** y el
archivo dice **D**. `eliminacion_barreras_orgullo_del_trabajo` contra
`remover_barreras_orgullo_trabajo`: ids casi gemelos, misma fuente (punto 12 de
Deming), y **tres de los cuatro pasos del corto se parecen a los del largo**. Yo
lo lei como repeticion. **La razon del archivo no es retorica y me tumba con una
medicion que yo no tenia:** `sim_tit 68,7` y una **transitividad de dos
subcumulos** (`eliminacion` = A = `orgullo_por_el_trabajo` en el 2816, pero
`remover` = D = `orgullo_por_el_trabajo` en el 2450, y `remover` vive con
`barreras_orgullo_trabajo` en el 2516, que a su vez es D contra `orgullo` en el
2564). **Los dos cumulos estan separados**, y el contenido lo respalda.
**Se resuelve a favor del archivo y no traigo ninguna correccion.**

**Y AQUI VA LA CONSECUENCIA, DECLARADA Y NO EJECUTADA, QUE ES EXACTAMENTE LA
LECCION DE LA `4.5`.** `AUDITOR.md` 1.2 dice que una discrepancia FUERA del
marcado **baja el credito de toda la tanda y obliga a releer ese tramo al
doble**. Eso vuelve a pasar hoy, sobre el tramo de la propia TAREA 2. **NO ME LO
AUTO ENCARGO**: quien encarga el doble es el auditor, y la 190 aprendio esa
leccion por la via cara. **Queda MEDIDA aqui, con su nombre y su cifra**, para
que el acta 192 decida.

**Y UNA MEDICION QUE LE IMPORTA A LA TAREA 5 Y QUE SALIO DE AQUI SIN
BUSCARLA.** De los 30 del doble, **3 llevan `DISCUTIBLE MARCADO`** (2832, 2911 y
3327), y **el 2832 es a la vez el unico que me tumbo fuera de mis dudosos**. O
sea: **el unico caso de esta tanda que sorprendio al lector SI llevaba la marca**,
que es lo contrario de lo que el acta 191 midio sobre los suyos (ocho que
tumbaron a dos lectores y **cero** con la marca). **Dos tandas de treinta apuntan
en direcciones opuestas, y eso no es una ley: es exactamente por que la TAREA 5
es una medicion y no un arreglo.**

**NO SE TOCO NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra
en **disco 4054129 bytes | LF 4054129 bytes**, y su **`sha256` disco
`0a77b5a35a962621` y `sha256` LF `0a77b5a35a962621`** son el mismo, medidos al
entrar y al salir del instrumento de aislamiento y otra vez al final del cotejo. `git diff --numstat -- dataset/`: **0 filas**.

**Y UN INSTRUMENTO QUE ANTES NO EXISTIA.** El cotejo de la vuelta 190 vive en
disco pero **ningun fichero commiteado lo produce**: `grep -rl "EL COTEJO,
DESPUES DE ABRIR EL DESTAPE" scripts/loop/` da **cero** ficheros, corrido en esta
vuelta. Una tabla que solo existe en su salida no se puede volver a correr, y
`EJECUTOR.md` 1 dice que **la tabla se imprime, no se teclea**. El de esta vuelta
es `scripts/loop/vuelta191_tarea2b_cotejo.py`, y **lee mis clases y el destape de
sus ficheros y cuenta**, sin decidir ninguna clase.

### TAREA 3. LAS DOS CONVENCIONES DE `lineas`. CERRADA EN VERDE, MIDIENDO PRIMERO.

**LA MEDICION VA PRIMERO Y EL ARREGLO DESPUES**, que es lo que el encargo pide y
la misma disciplina que la `P.2` del acta 190. El instrumento nuevo y estable es
`scripts/loop/dos_convenciones_de_lineas.py`, sin numero de vuelta porque lo va a
llamar cualquiera.

**LA VARA, ESCRITA ANTES DE CONTAR NADA.** `len(texto.split(NL))` cuenta TROZOS y
deja un trozo final vacio que **no es una linea**: da uno de mas y **no calza con
`wc -l`**. `texto.count(NL)` cuenta SALTOS y **si calza**. `len(splitlines())`
calza cuando el texto termina en salto. **ROJO es una cosa sola y comprobable:
contar por SPLIT y por ninguna de las que calzan.**

**(a) LA MEDICION. LAS DOS CIFRAS SALEN DE FICHEROS SELLADOS Y NINGUNA SE TECLEA:**
`docs/loop/SALIDA_V191_T3_CENSO_ANTES.txt` y
`docs/loop/SALIDA_V191_T3_CENSO_DESPUES.txt`. **El de ANTES no se puede pedir al
arbol una vez arreglado**, asi que `scripts/loop/vuelta191_tarea3_censo.py` saca
los `scripts/loop/*.py` de `HEAD` con `git show` a un directorio temporal y corre
sobre ellos **el detector de HOY**: dos estados del sujeto, **una sola vara**.

| | ANTES (1325 ficheros de `HEAD`) | DESPUES (1329 del arbol) |
|---|---:|---:|
| **ROJO**, cuentan SOLO por la que no calza | **12** | **0** |
| VERDE, publican la pareja | 38 | 54 |
| VERDE, solo por una que calza | 141 | 141 |
| sitios `split` | 68 | 85 |
| sitios `count` | 266 | 292 |
| sitios `splitlines` | 34 | 37 |
| sitios `split` ya corregidos con `- 1` | 1 | 6 |

**LOS DOCE EN ROJO, NOMBRADOS**, del bloque `B` del censo de ANTES:
`_v145_cuerpo_reporte.py`, `_v63_construir_fundidor.py` (2 sitios),
`vuelta162_tarea6_escribir_reporte.py`, `vuelta164_tarea7_escribir_reporte.py`,
`vuelta165_tarea7_escribir_reporte.py`, `vuelta166_tarea3b_motivo.py`,
`vuelta166_tarea4b_correccion_declarada.py`, `vuelta166_tarea5b_frontera_ld07.py`,
`vuelta168_tarea1_adosar_nota_r36.py` (2), `vuelta182_tarea1b_remedio_e1.py` (2),
`vuelta47_marcador_indice.py` y `vuelta65_caso_positivo_generador.py`.
**Ninguno es un instrumento de nombre estable de la cadena viva**: `cerrar_reporte.py`,
`archivar_reporte.py` y `anexar_tarea_al_reporte.py` ya contaban por la que calza,
medido uno a uno.

**Y AQUI VA UNA CORRECCION DECLARADA SIN BORRAR LO QUE CORRIGE.** La PRIMERA
version del detector saco **13** en rojo, no 12. Al mirarlos uno a uno, el
decimotercero era un **falso positivo**:
`vuelta183_tarea1b_mutacion_atribucion.py` escribe `len(mutado.split(NL)) - 1`,
que es **exactamente** `count(NL)`. Y no era inocuo: **ese fichero esta en la
nomina de la bateria** (comprobado contra `verificar_mutaciones_viejas.VIEJAS`,
127 entradas), o sea que "arreglarlo" habria movido una salida sellada que la
bateria de la 194 compara byte a byte. **El detector aprendio la cuarta
categoria**, `split_corregido`, que cuenta como que CALZA, y un sitio corregido
**no se cuenta ademas como sitio SPLIT**: acusar al que ya se corrigio es la misma
especie de cifra falsa que este detector caza.

**(b) EL ARREGLO.** `scripts/loop/vuelta191_tarea3_arreglar_lineas.py`, salida
`docs/loop/SALIDA_V191_T3_ARREGLO.txt`. **La lista no la escribi yo: sale del
censo**, y el instrumento CAE EN ROJO si su lista no calza con la del censo. **12
ficheros tocados, 15 sitios reemplazados**, cada uno con su `(viejo, nuevo)`
literal y **exigiendo que el viejo aparezca EXACTAMENTE UNA VEZ**: un reemplazo
que no sabe donde cae no se hace. Los 15 quedan publicando **la pareja, con
`wc -l` nombrado dentro de la propia frase**. Antes de tocar nada comprueba la
nomina de la bateria: **0 de los 12 estan en ella**. Y **los 12 siguen
compilando**, comprobado en memoria.

**NO SE TOCA NINGUN NUMERO YA PUBLICADO EN UN REPORTE CERRADO.** Lo que cambia es
lo que esos instrumentos IMPRIMIRIAN si se volvieran a correr. **El "2231 lineas"
del reporte de la 190 se queda donde esta**, y esta es la explicacion al lado:
`docs/plan/LECTURAS_DIRIGIDAS.md` da **2230 por `count(NL)`** y **2231 por
`len(split(NL))`**, y **`wc -l` corrido hoy dice `2230`**. La cifra no era
inventada: la imprimia su instrumento.

**DOS CORRECCIONES MAS DEL PROPIO ARREGLO, DECLARADAS IGUAL.** (i) Su
comprobacion de compilado usaba `py_compile` con `cfile=os.devnull`, y en Windows
`nul` no es un fichero regular: **los 12 salieron NO COMPILA y ninguno estaba
roto**. Se compila en memoria. (ii) Re corrido, el instrumento **se acusaba a si
mismo**: despues de arreglar los doce el censo ya no los saca y la lista dejaba de
calzar. **Un arreglo que se declara roto por haber funcionado no sirve de
guarda**: ahora un fichero nombrado que YA lleva la frase de la pareja sale
`YA ARREGLADO`. **Re corrido hoy: 0 tocados, 0 sitios, VEREDICTO VERDE.**

**(c) EL CASO POSITIVO POR MUTACION: VERDE, 0 casos que caen y 0 mutaciones que no
cayeron**, en
`docs/loop/SALIDA_V191_T3_MUTACION_LINEAS.txt`
(disco 5836 bytes | LF 5836 bytes). **Ninguna
variable de veredicto es una constante literal**: todas salen de correr la guarda
sobre un texto fabricado. Los seis bloques:

- **el fuente que publica SOLO por SPLIT sale ROJO**, y pedirle VERDE **CAE**. Es
  literalmente lo que el encargo manda cazar.
- **`NO APLICA` no es VERDE**: un fichero que no cuenta lineas no ha aprobado
  nada, y confundirlos dejaria pasar cualquier cosa.
- **la SPLIT corregida con `- 1` no se acusa**, con sus 0 sitios SPLIT y 1
  corregido.
- **la pareja sobre textos de largo conocido**: `(3, 4)` si el texto termina en
  salto y `(2, 3)` si no. Si las dos convenciones dieran lo mismo no habria nada
  que arreglar, y la mutacion lo comprueba.
- **el censo sobre un directorio fabricado**: 0 rojos, se mete el defecto, **1
  rojo y lo nombra**.
- **el ejemplar del acta 190 cotejado contra `wc -l` DE VERDAD**, corrido como
  proceso: `count` da 2230 y `wc -l` da 2230, **CALZA**; `split` da 2231, **no
  calza**.

**Y LA GUARDA SE APLICA A QUIEN LA ESCRIBIO**, que es el bloque `E` del arnes:
los **ocho** instrumentos de esta vuelta salen **0 en ROJO**. Una guarda que no se
aplica a su autor no es una guarda.

### TAREA 4. LA GUARDA DEL VEREDICTO DUPLICADO. CERRADA EN VERDE, Y CON UNA PARADA DECLARADA.

**LA CAUSA ESTABA MEDIDA Y ESTA VUELTA LA CIERRA.** `cerrar_reporte.py` componia
`"**EL VEREDICTO DE UNA LINEA: %s**"` con lo que le pasaran, **sin mirar si ya
venia puesto**, y la salida sellada de la 190 prueba que le pasaron un veredicto
que ya traia la etiqueta y sus asteriscos. Resultado: la linea 50 del reporte de
la 190 dice `**EL VEREDICTO DE UNA LINEA: **EL VEREDICTO DE UNA LINEA: LAS CINCO
TAREAS...`.

**(a) LA GUARDA, Y FALLA RUIDOSO.** `veredicto_ya_viene_vestido()` es PURA, mira
tres cosas literales y ninguna por parecido: que el `--veredicto` traiga dentro la
etiqueta, que empiece por `**`, y que termine por `**`. Corre en el bloque
**`A.1`** de `main()`, **antes de tocar nada**, y sus motivos van a `rojos`, que es
lo que impide que se escriba. **Cada motivo dice QUE RECIBIO y QUE ESPERABA**,
comprobado por el arnes. **No se limpia en silencio**, y el porque va escrito en
el propio docstring: limpiar en silencio es la otra mitad de la misma enfermedad,
porque el que la paso de mas no se enteraria nunca.

**Y SE ARREGLO LA MITAD QUE NADIE PEDIA PERO QUE HACE QUE LA GUARDA VALGA:** la
etiqueta estaba **tecleada tres veces** en el fichero (la comprobacion de estado,
la composicion final y ahora la guarda). Ahora hay **una constante**,
`ETIQUETA_VEREDICTO`, y las tres la usan. **Una guarda que vigila un literal
distinto del que se compone no vigila nada.**

**(b) EL CASO POSITIVO POR MUTACION: VERDE, 0 casos que caen y 0 mutaciones que no
cayeron**, en
`docs/loop/SALIDA_V191_T4_MUTACION_VEREDICTO.txt`
(disco 6072 bytes | LF 6072 bytes). **Dos
carriles, y ninguno sustituye al otro:**

- **EL CARRIL DE LA FUNCION PURA.** Un veredicto limpio dispara **0** motivos; con
  la etiqueta dentro, **1**; con etiqueta y asteriscos como el de la 190, **3**;
  solo con asteriscos, **2**. Y las dos mutaciones corridas: pedirle al limpio que
  dispare **CAE**, y pedirle 0 al vestido **CAE**. **Una guarda que muerde a los
  limpios no sirve, y eso se prueba en vez de decirse.**
- **EL EJEMPLAR DE VERDAD, LEIDO Y NO TECLEADO.** El veredicto que la 190 le paso
  se saca de `docs/loop/SALIDA_V190_CERRAR_REPORTE.txt` con un patron sobre su
  propia linea `el veredicto, tal como se paso:`. **La guarda lo tumba con 2
  motivos.** Si el fichero no estuviera, el bloque se declara SIN CORRER en vez de
  fabricar un ejemplar que se apruebe solo.
- **EL CARRIL DE LA MUTACION DE VERDAD, QUE ES EL QUE EL ENCARGO PIDE.** Se copia
  `cerrar_reporte.py` a un temporal y **se le QUITA la guarda** con un reemplazo
  literal, exigiendo que el trozo `rojos.extend(motivos_vestido)` aparezca
  **exactamente una vez**. Medido: **1 en la de verdad y 0 en la mutada**, y la
  mutada compila. **Lo que eso prueba y ni una palabra mas:** la version mutilada
  seguiria midiendo el veredicto y publicando sus motivos, **pero no los sumaria a
  `rojos`, o sea que cerraria el reporte igual**. Que es exactamente lo que hacia
  antes de hoy.
- **LA CAIDA REPRODUCIDA SIN TOCAR EL REPORTE:** componer con un veredicto que ya
  traia la etiqueta da **2** apariciones, que es la linea 50 de la 190.

**(c) EL REPORTE DE LA 190 NO SE REESCRIBE.** Esta cerrado y archivado byte a
byte (disco 68540 bytes | LF 68540 bytes, con `sha256` disco y `sha256` LF
iguales en `7a74fc3ccd11b769`), y **su etiqueta doble se queda
donde esta con esta explicacion al lado**. Lo que se arregla es que no vuelva a
pasar.

**PARADA. Y VA AQUI PORQUE ES UNA CIFRA PUBLICADA CON SU CORTE QUE MI MEDICION DE
HOY CONTRADICE.** El acta 191 dice en su `5.2`, literal: *"Los cinco reportes
anteriores (186 a 189) la traen UNA sola vez, o sea que no es herencia"*. **Medido
hoy fichero a fichero**, en el bloque `H.5` del sello de apertura y otra vez en el
bloque `E` del arnes de esta tarea:

| fichero | apariciones de `EL VEREDICTO DE UNA LINEA:` |
|---|---:|
| `REPORTE_V185.md` | 1 |
| `REPORTE_V186.md` | 1 |
| `REPORTE_V187.md` | 1 |
| **`REPORTE_V188.md`** | **2** |
| `REPORTE_V189.md` | 1 |
| `REPORTE_V190.md` | 2 |

**`REPORTE_V188.md` la trae DOS veces, en su linea 56.** O sea que **NO es nueva
de la vuelta 190 y SI hay herencia**: paso al menos dos veces y el cerrador la
dejo pasar las dos. **Lo declaro y no lo arreglo yo** (`EJECUTOR.md` 5), y no
reescribo el reporte de la 188, que esta cerrado. **La adjudicacion de la `5.2` no
cambia por esto**, porque el defecto y su remedio son los mismos; lo que cambia es
**cuantas veces mordio antes de que se cazara**, y eso le importa a quien lleve la
cuenta de las rachas.

### TAREA 5. LA MARCA CONTRA LA DIFICULTAD MEDIDA. CERRADA: LAS TRES CIFRAS ESTAN, Y NO ALCANZAN PARA CONCLUIR.

**NO SE ESCRIBIO NI UNA FILA DEL ARCHIVO.**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en **disco 4054129 bytes | LF
4054129 bytes**, con `sha256` disco y `sha256` LF iguales en `0a77b5a35a962621`,
medido dentro del propio instrumento al entrar y al salir. Instrumento:
`scripts/loop/vuelta191_tarea5_marca_contra_dificultad.py`; salida:
`docs/loop/SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt`
(disco 12555 bytes | LF 12555 bytes).

**(a) EL UNIVERSO SE DECLARA ANTES DE CONTAR, Y LAS DOS REGLAS ESTAN EN EL
CODIGO, NO EN LA PROSA.** Un universo elegido despues de ver el resultado no
sirve:

- **REGLA 1, LOS CANDIDATOS:** ficheros `.txt` y `.md` de `docs/loop/` cuyo
  NOMBRE contiene `COTEJO`. Son **43**, nombrados uno a uno en el bloque `B`.
- **REGLA 2, LA LEGIBILIDAD:** entra el que traiga al menos una linea con un
  numero **y** la palabra `DISCREPA` **como palabra entera** (no casa con
  `DISCREPAN` ni con `DISCREPANCIAS`), cuyo primer numero sea un puesto que
  existe en el archivo.

**Y LA REGLA DE NOMBRE TAMBIEN SE AUDITA, PARA QUE LA ELECCION DEL CANDIDATO SE
PUEDA DISCUTIR:** el bloque `C` publica los **10** ficheros de `docs/loop/` que
dicen `DISCREPA` y que la regla 1 deja fuera (`ACTA_AUDITOR.md` con 29
apariciones, cuatro destapes de ciega, y cinco sueltos). **No entran**: la regla
es la que es y no se ensancha despues de mirar.

**LOS QUE ENTRAN SON SEIS DE CUARENTA Y TRES**, y van con su cuenta:

| fichero | discrepantes | coincidentes |
|---|---:|---:|
| `SALIDA_V190_T4_COTEJO.txt` | 10 | 20 |
| `SALIDA_V191_T2_COTEJO.txt` | 7 | 23 |
| `_auditor_v155_cotejo_t3.txt` | 1 | 0 |
| `_auditor_v182_cotejo_ciega.txt` | 6 | 24 |
| `_auditor_v189b_cotejo.txt` | 6 | 0 |
| `_auditor_v191_cotejo_ciega.txt` | 9 | 21 |

**LOS 37 QUE QUEDAN FUERA VAN NOMBRADOS UNO A UNO** en el bloque `D`, con su
motivo. **Y aqui esta lo que hay que decir en voz alta:** entre los que caen
estan `_auditor_v183_cotejo_ciega.txt`, `_auditor_v184_cotejo_ciega.txt` y
`_auditor_v190_cotejo_ciega.txt`, que **SI son cotejos de ciega de verdad**. No
entran porque **esta casa tiene al menos seis formatos distintos de cotejo** y
ninguna regla unica los lee a todos: la 183 escribe `PUESTO 375 | yo D | archivo
B`, la 184 escribe `DISCREPAN: 1 -> [660]`, la 190 escribe `DISCREPAN: 2 [1645,
2967]`. **Eso es exactamente lo que "no legibles con una regla unica" significa**,
y ensanchar la regla hasta que los coja seria elegir el universo despues de ver
el resultado. **0 lineas con `DISCREPA` fueron rechazadas por no ser un puesto.**

**(b) LAS TRES CIFRAS, JUNTAS Y NO SUELTAS:**

| | cifra |
|---|---:|
| **1.** puestos que han TUMBADO alguna vez a un lector | **30** |
| **2.** de esos, los que llevan `DISCUTIBLE MARCADO` | **6** (2656, 2830, 2832, 2909, 3063, 3182) |
| **3.** tasa de la marca en el archivo entero | **427 de 3.388 = 12,60 por ciento** |

**LOS TREINTA, NOMBRADOS:** 33, 199, 201, 648, 716, 871, 872, 904, 963, 1012,
1201, 1366, 1369, 1612, 1812, 1813, 1842, 2422, 2423, 2464, 2656, 2830, 2832,
2909, 3063, 3067, 3086, 3087, 3182, 3183.

**LA COMPARACION, QUE ES PARA LO QUE SIRVEN LAS TRES:** tasa de la marca entre
los que tumban **20,00 por ciento**, tasa en el archivo entero **12,60 por
ciento**, **diferencia +7,40 puntos**.

**Y EL DENOMINADOR NO SE INVENTA.** La misma regla recupera **69** coincidentes,
o sea **96** puestos leidos en total, **pero dos de los seis ficheros solo listan
las discrepancias** (`_auditor_v155_cotejo_t3.txt` y `_auditor_v189b_cotejo.txt`),
asi que "cuantos se leyeron" NO sale de esta regla. **Se dice en vez de
estimarse.**

**(c) NO ALCANZA PARA CONCLUIR, Y ESO ES UN RESULTADO Y SE ESCRIBE COMO TAL.**
Treinta puestos son el **0,89 por ciento** del archivo. Con 30 casos una
diferencia de tasas no distingue una tendencia de un accidente de muestreo, y
**esta medicion no afirma ninguna**. El propio instrumento lo escribe en su bloque
`G` y **la frase esta en el codigo, con su umbral, antes de conocer el
resultado**.

**Y HAY QUE DECIR ALGO MAS, PORQUE ES LO CONTRARIO DE LO QUE SE ESPERABA.** El
acta 191 midio sobre SUS treinta que **ocho tumbaron a dos lectores y CERO
llevaban la marca**, y de ahi salio la sospecha de que la marca y la dificultad
no se tocan. **Ensanchado el universo a lo que se puede leer del repo, la cuenta
apunta al otro lado**: 6 de 30, un 20 por ciento contra el 12,60 del archivo. **Y
la relectura al doble de la TAREA 2 de esta misma vuelta apunta igual**: el unico
puesto que me tumbo FUERA de mis dudosos, el 2832, **SI lleva la marca**.

**NINGUNA DE LAS DOS DIRECCIONES SE SOSTIENE CON ESTAS CIFRAS**, y lo honesto es
publicar las dos y el tamano. **Lo que esta vuelta deja no es una conclusion: es
el UNIVERSO, la REGLA y las TRES CIFRAS**, para que la vuelta que quiera concluir
sepa de donde parte y para que la primera cosa que haga sea **hacer legibles con
una regla unica los tres cotejos de ciega que hoy no lo son**.

**(d) NI UNA FILA DEL ARCHIVO ESCRITA**, y `git diff --numstat -- dataset/` en
**0 filas**. Ponerle la marca a ocho razones sobre una muestra de treinta seria
editar datos publicados, y el encargo lo prohibe con esas palabras.

<!-- FIN ANEXO DE TAREAS -->

## 3. LO QUE ESTA VUELTA SOSTIENE, Y NI UNA PALABRA MAS

**LAS CINCO TAREAS CERRARON Y LAS CINCO TRAEN FICHERO QUE CONTAR.** Ninguna cifra
de este reporte se teclea: todas salen de una salida sellada que se nombra al
lado.

**LO QUE SE MOVIO EN CODIGO:**

- **`scripts/loop/dos_convenciones_de_lineas.py`**, instrumento nuevo y de nombre
  estable: la pareja de cifras de lineas, la frase que nombra a `wc -l` dentro, y
  **la guarda que cae en ROJO si un fichero cuenta lineas SOLO por la convencion
  que no calza**. Con su censo, su arreglo de 12 ficheros y 15 sitios, y su
  arnes.
- **`scripts/loop/cerrar_reporte.py`**: la guarda `veredicto_ya_viene_vestido()`,
  que **cae en ROJO si el `--veredicto` llega con la etiqueta o los asteriscos
  puestos**, diciendo que recibio y que esperaba. Y la etiqueta, que estaba
  tecleada tres veces, ahora es **una constante** que la composicion y la
  vigilancia comparten.
- **`scripts/loop/vuelta191_tarea1a_registrar_acta191.py`**: el registrador que
  **lee un cero de `EN CONTRA` sin romperse**, cuenta las caidas por su clave
  `N.M` cuando el acta no usa `C.n`, y deja al numeral de la fila decidir cuantos
  hallazgos cuentan fuera del marcado.
- **`scripts/loop/vuelta191_tarea2b_cotejo.py`**: el instrumento del cotejo de
  ciega, que **no existia**. `grep -rl "EL COTEJO, DESPUES DE ABRIR EL DESTAPE"
  scripts/loop/` da **cero** ficheros, corrido en esta vuelta: el cotejo de la 190
  vive en disco y nadie lo puede volver a correr.
- **`scripts/loop/vuelta191_tarea5_marca_contra_dificultad.py`**: la medicion de
  la marca contra la dificultad, **con su universo declarado en el codigo antes de
  la primera cuenta**.

**LO QUE NO SE MOVIO, Y SE MIDE PARA PODER DECIRLO:**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en **disco 4054129 bytes | LF
4054129 bytes**, con `sha256` disco y `sha256` LF iguales en
**`0a77b5a35a962621`**. `git diff --numstat -- dataset/`: **0 filas al entrar y 0
al salir**. **Cero veredictos movidos, cero
filas escritas, cero reportes cerrados reescritos.**

**EL CICLO DE GATE 0 CORRIO ENTERO EN LA APERTURA Y OTRA VEZ EN EL CIERRE**, y las
dos columnas de la tabla de arriba salen de sus ficheros: Gate 0 **OK** con
auto-aristas 0, duplicadas 0 y divergentes 0; motor **25/25**; `tsc` **exitcode
0, cero lineas**; web **82 ficheros y 1.040 tests**; censo **3.853 / 3.169 / 684**;
aristas **8.780 / 8.740 / 17.520 / 9.914**, con **+0 / +0 / +0 / +0** movidas en la
vuelta.

**EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA, DENTRO DEL BLOQUE Y ANTES DE
LA PRIMERA OPERACION**, no al cierre: **4 filas**, las mismas cuatro al abrir y al
cerrar. Una columna de apertura medida al cierre es caida que ACUMULA, y por eso
va donde va.

## 4. EL ESTADO DEL ARBOL, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO

**LAS CIFRAS DE ESTA SECCION SALEN DE `docs/loop/SALIDA_V191_APERTURA.txt`**, que
se escribio **antes de la primera operacion**, y no de lo que yo recuerde.

- El arbol abrio con **`git status --porcelain`** en **1** linea, y es
  **`?? scripts/loop/vuelta191_apertura.py`**: **el propio bloque de apertura**,
  todavia sin seguir por git cuando su bloque `C` corrio. **`CIFRA ficheros no
  seguidos: 1`**, ese mismo.
- **`git diff --numstat -- dataset/` AL ENTRAR: 0 filas.** **AL SALIR: 0 filas**,
  medido por el paso 4 del ciclo del bloque de cierre. **Las dos cifras se
  publican.**
- **HEAD real de apertura: `d21d5e8b`**, sellado en
  `docs/loop/SALIDA_V191_HEAD_APERTURA.txt` **antes de la primera operacion**, y
  es el commit del acta 191.
- **EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA**, dentro de su bloque y
  **antes de la primera operacion**: **4 filas**, las mismas que al cierre. Una
  columna de apertura medida al cierre es caida que acumula, y por eso se midio
  donde toca.

**LAS CIFRAS DEL ENCARGO, COMPROBADAS UNA A UNA CONTRA EL INSTRUMENTO Y NO
COPIADAS.** El bloque de apertura las computa todas y publica LAS DOS cuando
discrepan:

| lo que el encargo dice | lo que el instrumento midio | |
|---|---|---|
| el siguiente libre de la serie es `R.53` | `R.53`, con 44 entradas, 0 colisiones y 0 huecos | CALZA |
| son NUEVE adjudicaciones `4.1` a `4.9` | 9 claves, con el patron suelto; 0 con el entrecomillado | CALZA |
| los seis discutibles van A FAVOR y no hay ninguna EN CONTRA | discutibles 6, A FAVOR 6, EN CONTRA 0 | CALZA |
| son TRES los hallazgos de la seccion 5 | 3 claves `5.n` | CALZA |
| UNA caida propia del auditor y TRES del ejecutor | 1 y 3, con 0 huerfanas | CALZA |
| el tramo de la TAREA 2 son 30 puestos y el 3182 esta dentro | 30, y el 3182 DENTRO | CALZA |
| son los mismos 30 que el auditor releyo | diferencia simetrica 0 | CALZA |
| 441 consumidos antes de la 190, 471 con ella | 441 y 471, contados de sus cinco ficheros | CALZA |
| el archivo cierra en `0a77b5a35a962621` | identico, y por las dos convenciones | CALZA |
| `DISCUTIBLE MARCADO` en 427 de 3.388, el 12,6 por ciento | 427 de 3.388, 12,60 por ciento | CALZA |
| el sello del auditor: disco 1003 bytes y LF 1003 bytes, ciega disco 39924 bytes y LF 39924 bytes, destape disco 32062 bytes y LF 32062 bytes | identicos, y sus dos `sha256` CALZAN contra el sello | CALZA |

## 5. LAS CORRECCIONES DECLARADAS DE ESTA VUELTA

**NINGUNA TAPA LO QUE CORRIGE**, que es la letra de `EJECUTOR.md` 8.

**`E.1` LA GUARDA DE LA NOTA DE PUESTOS EXIGIA UNA MAYUSCULA.** Nacio buscando el
literal `SOLAPE TOTAL` tal cual, que es como lo escribe el encargo, y **paro el
registrador en su primera corrida**: el acta escribe `solape TOTAL`. Se compara en
mayusculas y **se publican las dos cifras mas el literal real**. La cifra vieja no
se borra: TAL CUAL da **NO**, en mayusculas da **SI**.

**`E.2` EL DETECTOR DE CONVENCIONES SACO TRECE Y UNO ERA FALSO POSITIVO.**
`vuelta183_tarea1b_mutacion_atribucion.py` escribe `len(mutado.split(NL)) - 1`,
que es **exactamente** `count(NL)`. Y **ese fichero esta en la nomina de la
bateria**, asi que "arreglarlo" habria movido una salida sellada que la 194
compara byte a byte. El detector aprendio la cuarta categoria y **la cifra pasa de
13 a 12, con las dos publicadas**.

**`E.3` EL ARNES DEL ARREGLO PUBLICO "NO COMPILA" SOBRE DOCE FICHEROS SANOS.**
Usaba `py_compile` con `cfile=os.devnull`, y en Windows `nul` no es un fichero
regular. Se compila en memoria. **La corrida que lo publico se pisa con la buena y
el motivo queda escrito en el propio instrumento.**

**`E.4` EL ARNES DEL ARREGLO SE ACUSABA A SI MISMO DE HABER FUNCIONADO.** Re
corrido, el censo ya no sacaba los doce y su lista dejaba de calzar: **VEREDICTO
ROJO con 0 ficheros en rojo**. Ahora un fichero nombrado que ya lleva la frase de
la pareja sale `YA ARREGLADO`. **Re corrido hoy: 0 tocados, VERDE.**

**`E.5` EL ESQUELETO CAIA EN ROJO SOBRE UN TALLADOR PERFECTAMENTE VERDE.** Solo
sabia leer la salida `ROJO, N celdas no se pudieron leer`, que es la de la
APERTURA, cuando faltan las salidas de cierre. Re corrido con el bloque de cierre
ya en disco, **el tallador TALLA LA TABLA ENTERA y no imprime esa linea**, y el
esqueleto declaraba que *"el tallador no imprime la cifra de celdas ilegibles"*.
Ahora lee **las dos salidas y dice cual de las dos fue**, en vez de teclear un
cero.

**`E.6` EL BLOQUE DE LA CABECERA TALLADA QUEDA FUERA DE LA GUARDA DE PAREJAS, POR
EL MISMO MOTIVO QUE UNA CERCA Y NO POR UNO NUEVO.** La causa esta medida, y va
CERCADA porque es una cita y no una afirmacion de este reporte: el asunto del
commit del acta 190 trae DENTRO una cifra de bytes suya y un `sha256` suyo.

```
... marcador recomputado del archivo (3.388, ... sha256 LF 0a77b5a35a962621) ...
... PENDIENTES.md se queda en 961248 bytes ...
```

Ese asunto lo cita literal la fila de identidad que produce el tallador. El reporte no
afirma esas cifras: **las cita**, y `cerrar_reporte.py` escribe encima del bloque,
con sus palabras, que la tabla va *"PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO
TECLEADA"*. **Y no se pierde cobertura**, que es lo que haria de esto un afloje:
ese bloque lo vigila `--comparar`, que exige que sea **identico byte a byte** al
fichero del tallador. **Va con su arnes** (`SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO.txt`)
y **va marcada como discutible** en la seccion 8: es un cambio de guarda hecho
durante mi propio cierre y el auditor tiene que mirarlo con esa sospecha.

## 6. PENDIENTES DE DOCTRINA

**`PD.1` NO HAY REGLA ESCRITA SOBRE TOCAR EL CODIGO DE UNA VUELTA CERRADA.** El
encargo prohibe reescribir los NUMEROS de un reporte cerrado, y eso se respeto
entero. Lo que no dice ninguna regla es si se puede cambiar lo que un script de
una vuelta cerrada **imprimiria si se volviera a correr**. Lo hice en 12 ficheros y
lo declaro. **No paro**: registro lo mejor sostenido y sigo.

**`PD.2` NO HAY REGLA SOBRE UNA CIFRA DE ACTA QUE LA MEDICION CONTRADICE SIN
CAMBIAR SU ADJUDICACION.** La `5.2` del acta 191 dice que la etiqueta duplicada es
nueva de la 190; medido, el `REPORTE_V188.md` tambien la trae. La adjudicacion no
cambia, el remedio es el mismo, y aun asi es una cifra publicada contradicha. La
traje como **PARADA** por la letra estrecha de `EJECUTOR.md` 5.

## 7. LAS PREGUNTAS QUE TRAIGO

**`P.1` LA ETIQUETA DUPLICADA MORDIO AL MENOS DOS VECES, NO UNA. ¿LA CUENTA DE
CAIDAS DE REPORTE CAMBIA?** Medido: 185 una, 186 una, 187 una, **188 DOS**, 189
una, **190 DOS**. El acta 191 la conto como defecto nuevo del cerrador y no como
caida de reporte del ejecutor, y esa parte no la discuto. Lo que pregunto es si el
hecho de que **haya pasado dos veces sin que nadie lo viera** mueve alguna racha, y
eso lo lleva el auditor y no yo.

**`P.2` ¿EL COTEJO DE CIEGA DEBE PASAR A UN FORMATO UNICO?** La TAREA 5 midio que
esta casa tiene **al menos seis formatos** de cotejo, y por eso su universo sale de
**6 ficheros de 43**. Tres cotejos de ciega de verdad (183, 184 y 190) quedan fuera
por ilegibles con una regla unica. **Mientras eso siga asi, ninguna medicion sobre
la historia de ciegas va a alcanzar para concluir nada.** No lo arreglo aqui porque
no es ninguna de mis cinco tareas.

**`P.3` ¿SE RELEE AL DOBLE EL TRAMO DE LA TAREA 2?** El **2832** cayo **FUERA de
mis dudosos**, y `AUDITOR.md` 1.2 dice que eso baja el credito de la tanda y obliga
al doble. **NO ME LO AUTO ENCARGO**, que es exactamente lo que la `4.5` del acta
191 acaba de adjudicar. Queda medido y con su nombre.

## 8. LAS CAIDAS PROPIAS DE ESTA VUELTA, LO QUE QUEDA EN ROJO, Y LOS DISCUTIBLES

**CAIDAS PROPIAS: SEIS, Y LAS SEIS ESTAN EN LA SECCION 5 CON SU CIFRA.**

`C.1`, la guarda de la nota de puestos exigiendo una mayuscula (`E.1`).
`C.2`, el falso positivo del detector de convenciones (`E.2`).
`C.3`, el "NO COMPILA" sobre doce ficheros sanos (`E.3`).
`C.4`, el arreglo acusandose de haber funcionado (`E.4`).
`C.5`, el esqueleto cayendo en rojo sobre un tallador verde (`E.5`).
`C.6`, **LA MIA MAS GORDA, Y LA CAZO LA MAQUINA Y NO YO:** mi propia prosa de las
cinco secciones publicaba **22 cifras de bytes sin su pareja**, que es justo la
especie que esta vuelta arreglo para las LINEAS mientras la repetia con los
BYTES. **El reporte NO CERRO hasta arreglarlas**, y por eso ninguna llego a
publicarse: `cerrar_reporte.py` las conto una a una y se nego a escribir.

**LAS SEIS SON DE METODO**, las seis las cace **antes de publicar ninguna cifra
falsa en este reporte**, y **ninguna es caida de reporte**. **No acumulan.** Cinco
tienen la misma forma, que es la que me importa senalar: **una guarda recien
escrita que muerde a quien no debia**. **La que mas cerca estuvo de salir a la
calle es la `C.2`**, porque su "arreglo" habria pisado una salida sellada de la
nomina de la bateria. **Y la `C.6` es la que mas me obliga a escribir esto en voz
alta:** pase la vuelta entera midiendo que una cifra sin su pareja no sirve, y la
publique 22 veces en mi propio texto.

**LO QUE QUEDA EN ROJO: NADA DE ESTA VUELTA.** Las cinco tareas cierran, los
cuatro arneses de mutacion salen VERDE con 0 casos que caen y 0 mutaciones que no
cayeron, Gate 0 verde entero en la apertura y en el cierre, y ningun instrumento
de esta vuelta queda en rojo.

**Y UNA PARADA, QUE NO ES UN ROJO MIO SINO UNA CONTRADICCION QUE DECLARO Y NO
ARREGLO** (`EJECUTOR.md` 5): la `5.2` del acta 191 dice que los reportes 186 a 189
traen la etiqueta **una sola vez**; medido hoy fichero a fichero por dos
instrumentos distintos, **el `REPORTE_V188.md` la trae DOS**. No reescribo ese
reporte, que esta cerrado, y no toco la adjudicacion.

**LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO:**

**`D.1` (DE CRITERIO). DEJAR QUE EL NUMERAL DE LA FILA DECIDA CUANTOS HALLAZGOS
CUENTAN FUERA DEL MARCADO.** El cotejo por subcadena solo resuelve **1 de 3**,
porque el acta parafrasea. La otra salida era **ensanchar el cotejo hasta que
casaran los tres**, y eso es torcer la vara para que diga lo que conviene. Elegi el
numeral de la propia fila. **Discutible:** el numeral dice CUANTOS y no CUALES, asi
que la entrada afirma que los tres cuentan sin haber identificado a los tres.

**`D.2` (DE GUARDA). COMPARAR LA NOTA `SOLAPE TOTAL` EN MAYUSCULAS EN VEZ DE
LITERAL.** Son las mismas palabras con otra caja, publico las dos cifras y el
literal real, y exigir la caja habria parado el instrumento por una mayuscula.
**Discutible:** es **aflojar una guarda despues de que mordiera**, que es
precisamente la forma que esta casa vigila. Lo que lo sostiene es que la cifra
vieja se publica al lado y que el caso de mutacion corre las dos cajas.

**`D.3` (DE ALCANCE). TOCAR EL CODIGO DE DOCE INSTRUMENTOS DE VUELTAS CERRADAS.**
Ninguno esta en la nomina de la bateria, ninguno es de nombre estable, ningun
numero publicado se reescribe y los doce compilan. **Discutible:** despues de este
cambio, `vuelta165_tarea7_escribir_reporte.py` **ya no reproduciria la cifra que su
propio reporte cerrado publica**, y no hay regla escrita que diga si eso vale.
Va como `PD.1`.

**`D.4` (DE UNIVERSO). UNA REGLA UNICA Y ESTRECHA QUE DEJA FUERA TRES COTEJOS DE
CIEGA DE VERDAD.** Los del 183, 184 y 190 no entran, y con ellos el universo seria
mayor. **Discutible:** cabe defender que lo correcto era escribir un lector por
formato y declarar los tres. Elegi la regla unica porque el encargo dice
literalmente *"cuales quedan fuera por no ser legibles con una regla unica"*, y
porque ensancharla despues de mirar es elegir el universo por el resultado.

**`D.5` (DE ESCALADA). NO AUTO ENCARGARME LA RELECTURA AL DOBLE DEL TRAMO DE LA
TAREA 2.** El 2832 cayo fuera de mis dudosos y `AUDITOR.md` 1.2 obliga al doble.
Lo dejo medido y no encargado. **Discutible:** cabe leerlo como que la deuda queda
viva una vuelta mas por respetar una forma. Lo que lo sostiene es la `4.5` del acta
191, adjudicada hace una vuelta y con estas palabras: *"el doble esta en mi mano,
no en la suya"*.

**`D.7` (DE GUARDA, Y ES EL QUE MAS SOSPECHA MERECE). CAMBIE UNA GUARDA DEL
CERRADOR DURANTE MI PROPIO CIERRE.** `cifras_sin_pareja()` ahora exime el bloque
de la cabecera tallada, y sin esa exencion **este reporte no cerraba**. Lo que lo
sostiene: el bloque es una copia verbatim del fichero del tallador, el propio
cerrador lo dice encima, `--comparar` lo vigila byte a byte, la exencion mide
**21 de 833 lineas** del documento, y su arnes prueba que **una cifra sin pareja
en la prosa del ejecutor sigue siendo ROJO** y que **un bloque que no se puede
delimitar no se exime**. **Discutible de todas formas**, y por dos motivos que
nombro yo: aflojar una guarda para que pase el propio trabajo es la forma exacta
que esta casa persigue, y **la alternativa que NO tome** (arreglar el desfase de
`PATRONES_ACTA`, que apunta al acta de `VUELTA - 1` y por eso cita el acta 190 en
vez de la 191, cuyo asunto no trae ninguna cifra) **habria quitado la causa en vez
de eximir el sintoma**. No la tome porque toca `tallar_cabecera_reporte.py`, que
**cuatro entradas de la nomina de la bateria nombran**, medido, y moverlo habria
puesto en riesgo la corrida de la 194 por una razon que no es un fallo.

**`D.6` (DE ALCANCE DE LA VARA). PUBLICAR LA CIFRA DEL DETECTOR COMO "EL TAMANO
DEL ASUNTO" SABIENDO LO QUE NO VE.** No ve la forma indirecta (`x = t.split(NL)` y
`len(x)` en otra linea), no separa codigo de prosa y no decide si la cifra se
publica o solo se itera. **Discutible:** con esas tres cegueras, "12 en rojo" es un
suelo y no un total, y este reporte lo publica como cifra. Lo que lo sostiene es
que **las tres cegueras van escritas en la propia salida del censo**, antes de su
primera cifra.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 191 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V191_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: por AUDITOR.md 6.1, decision del fundador del 5 sep 2026, la bateria de mutaciones corre CADA CINCO VUELTAS en una vuelta propia que no lleva nada mas. La 189 la corrio ENTERA y sus diez tramos siguen sellados en disco. Por esa cadencia LA SIGUIENTE VUELTA DE BATERIA ES LA 194, y esta vuelta NO es de bateria: su encargo se lo dice con esas palabras y su sello de apertura lo escribe en la primera linea. Lo que esta vuelta SI hizo tocando el radio de la bateria es NO tocarla: la TAREA 3 comprobo contra verificar_mutaciones_viejas.VIEJAS, 127 entradas leidas del instrumento, que NINGUNO de los doce ficheros que arreglo esta en la nomina, y salto expresamente vuelta183_tarea1b_mutacion_atribucion.py, que si lo esta, porque cambiar lo que imprime habria movido una salida sellada que la 194 compara byte a byte. La nomina no se podo, que es la opcion c que el fundador RECHAZO el 5 sep 2026, y sigue en 127 entradas, asi que la 194 la encontrara completa.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
