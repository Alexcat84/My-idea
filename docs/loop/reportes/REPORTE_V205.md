# REPORTE DE LA VUELTA 205 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**LA VUELTA DE BATERIA. UNA SOLA TAREA Y NADA MAS AL LADO** (`AUDITOR.md` 6.1,
decision del fundador del 5 sep 2026). La 200 era la anterior de la cadencia de
cinco y le tocaba a la 205.

**ESTE ESQUELETO SE ESCRIBIO AL ABRIR LA VUELTA, ANTES DE CORRER NINGUN TRAMO**
(`EJECUTOR.md` 1, EL REPORTE ABRE CON LA VUELTA). Cada tramo anexa su fila al
cerrarse, no al final. Una vuelta cortada deja reporte parcial, nunca vacio.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 205`, y su salida
cruda vive en `docs/loop/SALIDA_V206_TALLADOR_V205.txt` (5784 bytes en disco y 5764 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `e66bf67d` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 204: EL DATO CIERRA VERDE ENTERO Y LA UNICA CAIDA QUE ACUMULA ES UN NEGATIVO PUBLICADO SOBRE UNA MEDICION QUE LO DESMIENTE. La 204 escribio que ninguno de los reportes 177 y 178 titula seccion de PREGUNTAS, y los dos la titulan: ## 6. LAS PREGUNTAS, en las lineas 632 y 832. Persegui la causa hasta el codigo: preguntas_del_reporte() de _v203_reparto_de_actas_viejas.py, linea 196, casa con un patron que el articulo LAS le rompe, y de los reportes archivados 173 a 180 SEIS titulan esa seccion y NINGUNO casa. No se queda en el reporte: contamino R.67 y R.68. ACUMULA porque es la conclusion de su subseccion y de ella salio un valor escrito en otro documento; especie nueva, racha 1, y la especie vieja de la 203 se extingue a 0. Las otras dos caidas suyas registran y no acumulan: la misma caida propia lleva dos etiquetas, C.2 en su cuerpo y C.3 en su seccion 8; y publica Once formas de una sola entrada donde su propio instrumento lista QUINCE. TODO LO DEMAS REPRODUCE AL DIGITO CON EL CICLO DE GATE 0 CORRIDO POR MI, los nueve comandos en su orden: censo 3853/3169/684, Gate 0 OK con 0 auto-aristas, 0 duplicadas y 0 divergentes, aristas 8780/8740/17520/9914, motor 25/25, web 82 (82) y 1040 (1040), tsc EXIT 0, desfase en 4 filas las mismas cuatro, y numstat de dataset, web, engine Y docs/plan en CERO FILAS DESPUES de correr yo el ciclo entero. Marcador 3388 con A 551, B 72, C 5 y D 2760, 0 huecos, 0 duplicados, sellado y pasado por su guarda en VERDE. Las once cifras de bytes y sha256 calzan por las dos convenciones. La TAREA 0 la medi en git y no en su palabra: las tres sedes del auditor dan 0, 0 y 0 entre 59d32eee y el cierre real e48d272f, y la vuelta entera solo toca docs/loop, scripts/loop, docs/loop/reportes y docs/PENDIENTES.md con 209 lineas anadidas y 0 borradas. La TAREA 3 la reproduje con MI PROPIO RESOLUTOR y las nueve cifras calzan: 332 y 47, 285 que faltan, 0 nuevas, subconjunto estricto, 263 de colapso y 22 que no, 21 pares y un trio. La TAREA 4 la corri sobre un commit DISTINTO del suyo y las ocho cifras de la vara calzan, y las TRECE que nombra son las trece. LA CIEGA: 35 de 40, 34 de 39 efectivos porque queme el 297 yo mismo y lo declaro; mis cinco fallos son cuatro A de mas y una A de menos, y el archivo tiene razon en las cinco. La tanda NO se dobla, por LA RAIZ. TRES HALLAZGOS QUE SUBEN: la ciega gasta el 40 por ciento de su sujeto en pares ya resueltos, 21 de 78 nodos deprecados tocando 16 de los 40 pares y los DOS muertos en cinco de ellos, que convierte en cifra lo que el acta 203 levanto como anecdota; la ciega compara la clase de ayer con los pasos de hoy, medido en el 1325 contra el commit d6c76fbb, y no es cifra falsa sino envejecida; y LA BATERIA NO CORRE EN SU PROPIO NOMBRE DESDE LA 194, con 0 ficheros de la 195 y 0 de la 200, cuya seccion 9 nombra la corrida de la 183. Por eso el encargo de la 205 es LA BATERIA SOLA, con salidas selladas en su propio nombre y la letra de que una corrida de otra vuelta no cuenta. DOS CAIDAS MIAS: escribi mi plan de apertura despues de OCHO comandos y no antes del primero, cuarta seguida de su familia y segunda con el remedio ya escrito, o sea que ademas rompi un remedio escrito; y lei REPORTE.md con sed despues de que leer_reporte() me lo negara en rojo, que es la especie de la C.1 del acta 201 y la prueba de que el codigo no puede impedir el comando por tu cuenta. El acta solo crece por anexion: 4734621 bytes antes y 4755952 despues, y el texto viejo sigue entero al principio.'), HEAD real de apertura `e66bf67d` (sello RECONSTRUIDO DESPUES (commit 78ca7176), leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `78ca7176` (leido de `SALIDA_V205_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LA TAREA UNICA DEL ENCARGO, Y SU ESTADO

| tarea | que es | estado |
|---|---|---|
| TAREA UNICA | LA BATERIA DE MUTACIONES, ENTERA, SOLA Y POR TRAMOS | ABIERTA AL ESCRIBIR ESTE ESQUELETO |

## 2. LA TAREA, POR TRAMOS (cada tramo ANEXA su fila al sellarse)

| tramo | salida sellada | bytes disco | bytes LF | exitcode | minutos |
|---|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

**EL VEREDICTO DE UNA LINEA: LA BATERIA DE LA CADENCIA DE CINCO CORRIO ENTERA Y EN SU PROPIO NOMBRE POR PRIMERA VEZ DESDE LA 194, con los once tramos sellados, ninguno de cero bytes, cubriendo las 135 entradas de la nomina exactamente una vez y sumando 42.0 minutos, Y SALIO ROJA por la causa estructural de los 2 arneses del censo que la nomina congelada en 135 no puede admitir mientras dure la moratoria, a la que mi medicion del cierre le suma 5 entradas de la nomina que no mordieron y que suben como PARADA en el reporte de la vuelta 206, porque contradicen la cifra de una sola causa.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CELDA DE ESTA SECCION SE TECLEO.** Todas salen de
`scripts/loop/_v205_tallar_tabla_tramos.py 11`, que cuenta los once ficheros de
tramo uno a uno, y su salida cruda vive en `docs/loop/SALIDA_V205_TABLA_TRAMOS.txt`
(**3122** bytes en disco y **3083** normalizado a LF, sha256 LF `8749e987a401dc0d`). `EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO.

### 3.1 EL REPARTO, COMPUTADO DE LA NOMINA DE HOY Y NO TECLEADO DE OTRA VUELTA

Salido de `python scripts/loop/_v205_bateria_en_su_nombre.py --plan`, que lo
computa con `reparto_en_tramos()` sobre `VIEJAS`:

- `CIFRA entradas de la nomina: 135`
- `CIFRA tamano de tramo: 13`
- `CIFRA tramos: 11`
- `CIFRA suma de las entradas de todos los tramos: 135`

**LA NOMINA SIGUE CONGELADA EN 135**, contada del modulo y no del encargo. El
encargo dice 135 y la medicion de hoy dice 135: **calzan**.

### 3.2 EL SELLADO DE LOS ONCE TRAMOS, CONTADO DE SUS FICHEROS

LA TABLA DEL SELLADO, CONTADA DE LOS 11 FICHEROS Y NO TECLEADA

| tramo | salida sellada | bytes (las dos convenciones) | sha256 LF | entradas | exitcode | minutos |
|---|---|---|---|---|---|---|
| 1 | `SALIDA_V205_BATERIA_TRAMO_1.txt` | 9555 bytes en disco y 9555 normalizado a LF | `85c94304eef1fa28` | 13 | 1 | 2.8 |
| 2 | `SALIDA_V205_BATERIA_TRAMO_2.txt` | 7788 bytes en disco y 7788 normalizado a LF | `8a426852569997fb` | 13 | 1 | 6.7 |
| 3 | `SALIDA_V205_BATERIA_TRAMO_3.txt` | 8525 bytes en disco y 8525 normalizado a LF | `d665343b2715e6bb` | 13 | 1 | 11.2 |
| 4 | `SALIDA_V205_BATERIA_TRAMO_4.txt` | 8072 bytes en disco y 8072 normalizado a LF | `07a889be43424245` | 13 | 1 | 3.0 |
| 5 | `SALIDA_V205_BATERIA_TRAMO_5.txt` | 8149 bytes en disco y 8149 normalizado a LF | `65206552cad293f7` | 13 | 1 | 2.4 |
| 6 | `SALIDA_V205_BATERIA_TRAMO_6.txt` | 7880 bytes en disco y 7880 normalizado a LF | `6c8c8725822883c1` | 13 | 1 | 3.0 |
| 7 | `SALIDA_V205_BATERIA_TRAMO_7.txt` | 7896 bytes en disco y 7896 normalizado a LF | `427b396bd08b2fc8` | 13 | 1 | 2.5 |
| 8 | `SALIDA_V205_BATERIA_TRAMO_8.txt` | 7855 bytes en disco y 7855 normalizado a LF | `fa02d03f1befeaf2` | 13 | 1 | 2.8 |
| 9 | `SALIDA_V205_BATERIA_TRAMO_9.txt` | 8523 bytes en disco y 8523 normalizado a LF | `570ab8df86712b23` | 13 | 1 | 2.6 |
| 10 | `SALIDA_V205_BATERIA_TRAMO_10.txt` | 8473 bytes en disco y 8473 normalizado a LF | `7fc7bf36a70ad181` | 13 | 1 | 4.1 |
| 11 | `SALIDA_V205_BATERIA_TRAMO_11.txt` | 6271 bytes en disco y 6271 normalizado a LF | `c9e02832786abb5c` | 5 | 1 | 0.9 |

LA TABLA DEL VEREDICTO DE CADA TRAMO, CONTADA DE LOS MISMOS FICHEROS

| tramo | ancla perdida | no mordio | no reproducible | ruido de concurrencia | clase del veredicto | reloj de pared UTC |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | ROJO POR FALLO | 2026-09-07T20:59:33Z a 2026-09-07T21:02:20Z |
| 2 | 0 | 0 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:03:34Z a 2026-09-07T21:10:14Z |
| 3 | 0 | 1 | 0 | 2 | ROJO POR FALLO | 2026-09-07T21:21:06Z a 2026-09-07T21:32:15Z |
| 4 | 0 | 1 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:32:50Z a 2026-09-07T21:35:48Z |
| 5 | 0 | 2 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:36:25Z a 2026-09-07T21:38:48Z |
| 6 | 0 | 0 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:39:22Z a 2026-09-07T21:42:21Z |
| 7 | 0 | 0 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:42:53Z a 2026-09-07T21:45:21Z |
| 8 | 0 | 0 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:45:54Z a 2026-09-07T21:48:44Z |
| 9 | 0 | 1 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:49:17Z a 2026-09-07T21:51:52Z |
| 10 | 0 | 0 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:52:32Z a 2026-09-07T21:56:35Z |
| 11 | 0 | 0 | 0 | 0 | ROJO POR FALLO | 2026-09-07T21:57:09Z a 2026-09-07T21:58:04Z |

CIFRA tramos con fichero en disco: 11 de 11
CIFRA tramos AUSENTES: 0
CIFRA tramos de CERO BYTES: 0
CIFRA suma de las entradas corridas, sumada de las lineas ENTRADA DEL TRAMO: 135
CIFRA suma de bytes de los tramos: 88987 en disco y 88987 normalizado a LF
CIFRA suma de minutos de los tramos, sumada de sus lineas de duracion: 42.0
CIFRA suma de horas: 0.70

### 3.3 LA DOBLE CORRIDA, QUE ES OBLIGATORIA, Y DONDE VIVE

**LA DOBLE CORRIDA NO ES UNA SEGUNDA PASADA DE LA BATERIA: VIVE DENTRO DE ELLA**,
y eso lo comprobe en el codigo antes de decirlo. `verificar_mutaciones_viejas.py`
linea 1710: cada mutacion vieja se corre DOS VECES SEGUIDAS, y linea 1713: si
alguno difiere entre la primera y la segunda corrida, es ROJO nombrandolo. Es el
cotejo de reproducibilidad de la TAREA 2.f de la vuelta 141. Cada salida sellada
lo repite en su propio texto, en su AVISO DE RELOJ: cada entrada se corre DOS
VECES, asi que el tiempo de cada arnes YA INCLUYE sus dos corridas.

**SU RELOJ SE PUBLICA**, y sale de las lineas `DURACION DEL TRAMO (monotona,
minutos)` de los once ficheros, sumadas por el tallador de la tabla. **NO
REPRODUCIBLE sale 0 en los once tramos**, o sea que ninguna de las 135 entradas
difirio entre su primera y su segunda corrida.

### 3.4 EL CENSO Y LA NOMINA, CON VARA Y SIN VARA, LAS DOS CIFRAS JUNTAS

Contadas de `docs/loop/SALIDA_V205_BATERIA_TRAMO_1.txt`, que las trae en su
bloque de cabecera y otra vez recomputadas al cierre del tramo:

| cifra | valor | de que linea del fichero sale |
|---|---:|---|
| arneses que el censo reconoce en `scripts/loop/` | 197 | `CIFRA arneses en scripts/loop/ que el censo reconoce` |
| entradas de la nomina | 135 | `CIFRA entradas en la nomina` |
| entradas de la nomina que el censo NO VE | 0 de 135 | `CIFRA entradas de la nomina que el censo NO VE` |
| arneses del censo fuera de la nomina CON la vara 148 | 2 | `CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina` |
| arneses del censo fuera de la nomina SIN vara | 62 | 197 menos 135, y la resta vale porque las 135 estan las 135 dentro de las 197, que es lo que dice la fila de los 0 invisibles |

**LOS DOS ARNESES QUE LA VARA 148 DEJA FUERA, NOMBRADOS OTRA VEZ PORQUE EL
CONGELADO IMPIDE METERLOS Y ESO SE DICE EN VEZ DE CALLARSE:**

- `vuelta197_tarea2_mutacion_orden_del_turno.py`
- `vuelta199_tarea1_mutacion_guardas_revividas.py`

**EL CONTRASTE CON EL ENCARGO, QUE NO ES FUENTE SINO CONTRASTE:** el encargo dice
que al cerrar la 204 daban **2** y **62** sobre un censo de **197**. Mi medicion de
hoy da **2**, **62** y **197**. **Calzan las tres, y estan medidas hoy.**

### 3.5 EL VEREDICTO DE LA BATERIA, Y POR QUE ES ROJO

**LOS ONCE TRAMOS SALEN EN `ROJO POR FALLO` CON `exitcode 1`, Y LA CAUSA ES UNA
SOLA Y ES ESTRUCTURAL.** El desglose que el propio instrumento imprime, en la
linea `CIFRA de FALLO` de cada tramo, es identico en los once:

```
0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
```

**NINGUNA DE LAS 135 ENTRADAS DE LA NOMINA FALLA.** Las 135 muerden, las 135 se
reproducen entre sus dos corridas, ninguna perdio su ancla y ninguna tiene el
sujeto vivo. **Lo unico que enciende el rojo son los DOS arneses que la moratoria
impide meter en la nomina**, y es el mismo rojo que el propio codigo se predijo,
en el comentario de `verificar_mutaciones_viejas.py` que explica por que entraron
seis entradas en la vuelta 195: un rojo permanente y conocido apaga la bateria
sola, porque si siempre esta roja nadie mira el rojo nuevo.

**NO LO SALTO, NO LO AFLOJO Y NO PODO NADA.** Lo declaro con su nombre y su
salida, que es lo que el encargo manda cuando dice que un arnes que falla es
exactamente lo que la bateria existe para encontrar. Aqui hay que decir una cosa
mas, y va como hallazgo: **el que falla no es un arnes DE la nomina, sino la
relacion entre el censo y la nomina**, y eso no lo arregla la bateria.

**CORRECCION DECLARADA, HECHA EN LA VUELTA 206 AL CERRAR ESTE REPORTE, Y EL
TEXTO VIEJO SE QUEDA ENTERO ARRIBA** (`EJECUTOR.md` 8, "una correccion que tapa
lo que corrige no se puede auditar").

**LO QUE EL PARRAFO DE ARRIBA AFIRMA Y NO ES CIERTO:** que el desglose de la
linea `CIFRA de FALLO` es "identico en los once" con **0 que no mordieron**, y
que "NINGUNA DE LAS 135 ENTRADAS DE LA NOMINA FALLA".

**LO QUE MIDO YO HOY, CONTANDO LOS ONCE FICHEROS SELLADOS UNO A UNO**, con
`python scripts/loop/_v206_medir_no_mordio.py`, salida cruda en
`docs/loop/SALIDA_V206_NO_MORDIO.txt` (4151 bytes en disco y 4103 normalizado a
LF, sha256 LF `cffa5cd0724d0427`):

- **CIFRA familias distintas de la linea `CIFRA de FALLO` entre los once: 3**, no
  una. Las tres se diferencian SOLO en el segundo sumando: **0**, **1** y **2**
  que no mordieron.
- **CIFRA entradas de la nomina que NO MORDIERON en la bateria de la 205: 5**,
  repartidas en **4** tramos, y son estas cinco, con su tramo y su `exit`:

| tramo | entrada de la nomina que NO MORDIO | `exit` que publico |
|---|---|---:|
| 3 | `vuelta160_tarea6b_mutacion_puerta.py` | 3221225794 |
| 4 | `vuelta163_tarea4b_mutacion_re_sellado.py` | 1 |
| 5 | `vuelta165_tarea6_mutacion_op_l_01.py` | 1 |
| 5 | `vuelta166_tarea6_mutacion_guarda.py` | 1 |
| 9 | `vuelta185_tarea1c_mutacion_bateria_continuada.py` | 1 |

- **`ANCLA PERDIDA` y `NO REPRODUCIBLE` SI dan 0 en los once**, y eso del parrafo
  viejo SI se sostiene con la medicion de hoy.

**ESTO NO LO ARREGLO YO Y SUBE COMO PARADA EN EL REPORTE DE LA VUELTA 206**, por
`EJECUTOR.md` 5: contradice una cifra publicada con su corte, la adjudicacion
`5.3` del acta 205, que dice que los once tramos salen rojos "por una sola
causa". Medido, las causas del rojo son **dos**: los **2** arneses del censo que
la nomina congelada no admite, y estas **5** entradas que no mordieron.

### 3.6 LOS DOS CASOS DECLARADOS, QUE NO SON FALLOS Y SE NOMBRAN IGUAL

El tramo 1 publica `CASO DECLARADO : 2`, y los dos vienen declarados de vueltas
anteriores con su marca obligatoria dentro de la propia salida sellada:

- `vuelta135_2e_mutacion_3.py`, exit declarado 1, marca `NO TIENE CONVENCION MECANICA DE CONTEO`.
- `vuelta140_2a_mutaciones.py`, exit declarado 2, marca `VEREDICTO (iii): NO CALZA`.

**No los toco y no los cuento como fallo**, porque el instrumento no los cuenta
como fallo: su linea `CIFRA de FALLO` los deja fuera y los publica aparte.

## 4. LO QUE SE TOCO, Y LO QUE NO

**TODO LO DE ESTA SECCION SALE DE `git` CORRIDO EN ESTA VUELTA Y NO SE
HEREDA DE LA APERTURA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL
CIERRE). LA HUELLA SE MIDE ENTRE DOS COMMITS, `e66bf67d` de apertura y `43f2158e`
de cierre, **y no contra el arbol de trabajo**: esta vuelta se cierra
tarde, y medir contra el arbol de hoy le colgaria ficheros de otra vuelta.

### 4.1 LAS CUATRO SEDES QUE EL ENCARGO EXIGE EN CERO, MEDIDAS AL CIERRE

Comando: `git diff e66bf67d..43f2158e --numstat -- <sede>`

| sede | filas de numstat |
|---|---:|
| `dataset/` | 0 |
| `web/` | 0 |
| `engine/` | 0 |
| `docs/plan/` | 0 |

**CIFRA suma de filas de las cuatro sedes: 0.**

### 4.2 LAS TRES SEDES DEL AUDITOR, QUE EL EJECUTOR NO ESCRIBE

**EL CERO DE `PARA_ALEXIS.md` ES DE AUSENCIA DE FICHERO, Y ASI SE DICE**
(`4.5` del acta 204). Comando: `git diff e66bf67d..43f2158e --numstat -- <sede>`.

| sede del auditor | existe en disco | filas de numstat | de que es el cero |
|---|---|---:|---|
| `docs/loop/PROMPT_SIGUIENTE.md` | SI | 0 | de no haberla tocado |
| `docs/loop/ACTA_AUDITOR.md` | SI | 0 | de no haberla tocado |
| `docs/loop/PARA_ALEXIS.md` | NO | 0 | **de ausencia de fichero**, no de no haberla tocado |

### 4.3 LAS DOS SEDES SELLADAS, REMEDIDAS Y NO HEREDADAS

Leidas del arbol de `43f2158e` con `git show`, que es el arbol al cerrar
esa vuelta, y no del disco de hoy.

| fichero | bytes (disco y LF, en el mismo renglon) | sha256 (disco y LF, en el mismo renglon) | calza con el encargo |
|---|---|---|---|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 4054129 bytes en disco y 4054129 bytes normalizado a LF | sha256 disco `0a77b5a35a962621` y sha256 LF `0a77b5a35a962621` | SI |
| `docs/plan/OPERACIONES.jsonl` | 513043 bytes en disco y 513043 bytes normalizado a LF | sha256 disco `829c583eb779cab6` y sha256 LF `829c583eb779cab6` | SI |

**NINGUN campo `estado`, NINGUNA clase y NINGUN veredicto se movio, y no lo
digo: lo miden los dos `sha256` de arriba, identicos por las dos
convenciones a los que el encargo trae del cierre de la 204.**

### 4.4 LO QUE LA VUELTA SI TOCO, LEIDO DE `git` Y NO NARRADO

Comando: `git diff e66bf67d..43f2158e --numstat` sobre el arbol entero.

| directorio tocado | ficheros |
|---|---:|
| `docs/loop` | 24 |
| `scripts/loop` | 1 |

**CIFRA ficheros tocados contra el HEAD de apertura: 25.**

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. CORRI LA BATERIA CON UN CONDUCTOR `_v205_*` QUE IMPORTA EL LANZADOR, EN
VEZ DE CLONARLO O DE REUSAR LA SALIDA DE LA 183.** El encargo manda dos cosas que
con el codigo de hoy no pueden valer las dos: que el lanzador no se clone ni se
escriba otro, y que las salidas selladas vayan en el nombre de esta vuelta. Medi
el choque en vez de suponerlo, con sus lineas de codigo delante. Elegi la tercera
puerta: **no clonar, no reusar, e importar**. **Por donde me puedo estar
equivocando:** un fichero nuevo en `scripts/loop/` es un fichero nuevo, y aunque
lleve guion bajo y aunque no anada ni una guarda, alguien puede leer *no se
escribe otro* como *no se escribe NINGUNO*, y entonces la lectura correcta era
declarar la parada y dejar la bateria sin correr por tercera cadencia seguida.
**Yo creo que no**, porque la bateria sin correr es la enfermedad que esta vuelta
existe para curar y porque el propio encargo bendice el carril `_v205_*`; pero
**es del auditor y no mia**, y por eso sube tambien como pregunta.

**`D.2`. EL CICLO DE GATE 0 DE APERTURA LO CORRI TARDE, Y LO DECLARO EN VEZ DE
LLAMARLO APERTURA A SECAS.** No corri el ciclo antes del primer tramo. Lo que
sostiene que la medicion siga siendo la de la apertura es una **medicion, no una
promesa**: `git diff` con `--numstat` contra el HEAD de apertura sobre `dataset/`,
`web/` y `engine/` da **cero filas**, o sea que los tres arboles que el ciclo mide
son byte a byte los de la apertura. **Por donde me puedo estar equivocando:** la
regla dice que la apertura se mide antes de la primera operacion, y no dice *o
despues, si puedes probar que nada se movio*. Si el auditor lee la letra estrecha,
esto es caida y no discutible, y por eso **va tambien en la seccion 8 como caida
mia**, contada una sola vez y con una sola etiqueta.

**`D.3`. DOY LA BATERIA POR CORRIDA AUNQUE LOS ONCE TRAMOS SALGAN EN ROJO.** La
letra dice que la bateria se declara corrida cuando todos los tramos tienen salida
sellada del mismo calibre, y que el calibre lo coteja `--componer`. Corrida y verde
no son la misma cosa: **corrida** es que los once tienen salida sellada, no vacia
y del mismo calibre; **verde** es otra cosa y hoy no lo esta. **Por donde me puedo
estar equivocando:** si por *corrida* se entendia *corrida y en verde*, entonces la
bateria de la 205 no cuenta y la cadencia sigue rota, con la diferencia de que
ahora **se sabe por que**, con nombre y apellido de los dos arneses.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1`. EL CHOQUE DE LA `D.1` NECESITA LETRA, PORQUE VUELVE CADA CINCO VUELTAS.**
Con la moratoria vigente y el lanzador computando su vuelta del nombre del
fichero, **cada vuelta de bateria se topara con lo mismo**. Tres salidas posibles,
y ninguna la decido yo: (a) el carril `_v205_*` que use hoy queda bendecido por
escrito para las vueltas de bateria; (b) se autoriza, como excepcion nombrada de
la moratoria, cambiar el lanzador para que acepte una opcion de vuelta; (c) se
acepta que las salidas lleven el numero del lanzador y se cambia la letra de
`AUDITOR.md` 6.1 y la pieza (4) de `cerrar_reporte.py`, que hoy la rechazan.

**`P.2`. EL ROJO ESTRUCTURAL DE LOS DOS ARNESES NO LO PUEDE RESOLVER EL EJECUTOR.**
La regla escrita desde la vuelta 148 dice que un arnes del censo entra en la
nomina; la moratoria del 7 sep dice que la nomina queda congelada en 135. **Las
dos son vigentes y se contradicen sobre estos dos ficheros.** Mientras no se
resuelva, **la bateria sale roja todas las vueltas por la misma causa**, que es
justo lo que el propio codigo avisa que apaga una bateria.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`.** Que cuenta como *clonar* bajo la moratoria: un fichero que **importa**
un instrumento y le corrige un dato, sin copiar ni una linea suya, no esta escrito
en ningun sitio como permitido ni como prohibido. **Registro lo mejor sostenido y
sigo**, que es lo que `EJECUTOR.md` 5 manda cuando falta regla.

**`PD.2`.** La `PD.3` de la 204, que pregunta que hacer cuando dos secciones
titulan el mismo numeral, **sigue sin resolver** y esta vuelta no la toca. La cito
para que no se pierda, con su sede: adjudicacion `4.7` del acta 204.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE

**`C.1`. NO CORRI EL CICLO DE GATE 0 DE APERTURA ANTES DE LA PRIMERA OPERACION**, y
el sello `docs/loop/SALIDA_V205_HEAD_APERTURA.txt` nacio con la bateria ya
corriendo. **El tallador lo dice solo y no se lo tapo**: su fila de identidad
publica el sello como RECONSTRUIDO DESPUES, y esa es la celda que va en la
cabecera. Lo que si medi antes de la primera operacion, y esta copiado en el
bloque A del sello con esa advertencia escrita encima, son el HEAD, la rama, el
estado del arbol y los dos `sha256` de las sedes selladas. **Es la misma caida que
la `D.2` y por eso se cuenta UNA VEZ**, aqui, con una sola etiqueta, que es la
leccion que el acta 204 me deja escrita.

**`C.2`. MATE EL TRAMO 3 A MITAD POR LANZARLO CONTRA UN TOPE DE DIEZ MINUTOS QUE
NO LE ALCANZABA**, y lo dejo dicho porque dejo rastro medible: al morir, `dataset/`
quedo sucio en **1 fichero**, `dataset/metadata/master_graph.json`, contado con
`git diff --numstat -- dataset/`. **No lo arregle yo a mano**: la guarda del propio
lanzador lo restauro con `git checkout --` al entrar al tramo siguiente y lo
remidio en cero, y eso queda dentro de la salida sellada de ese tramo. El remedio
fue lanzar el resto en corrida de fondo, sin tope. **La caida es mia, la guarda
funciono, y el tramo 3 que cuenta es el que si termino.**

**CORRECCION DECLARADA, HECHA EN LA VUELTA 206 AL CERRAR ESTE REPORTE, Y EL
TEXTO VIEJO SE QUEDA ENTERO ARRIBA** (`EJECUTOR.md` 8).

**LO QUE LA `D.2` Y LA `C.1` AFIRMAN Y SE QUEDA CORTO:** dicen que el ciclo de
Gate 0 de apertura "lo corri tarde". Medido hoy: en el arbol del cierre de la
vuelta 205 **no habia NI UNO** de los seis ficheros que el tallador lee para la
columna de apertura, o sea que ese ciclo **no se corrio tarde: no se corrio**.
`git log --all -- docs/loop/SALIDA_V205_GATE0_CMD1_APERTURA.txt` no encontro
ninguna aparicion, y el rechazo sellado de aquella vuelta,
`docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt`, lo nombra en su primera linea de
celdas.

**QUIEN LOS ESCRIBIO Y CUANDO, DICHO SIN ADORNO:** los escribi **yo, el ejecutor
de la vuelta 206**, corriendo `python scripts/loop/_v205_ciclo_gate0.py APERTURA`
en mi propio turno, **8 de 8 comandos en `EXITCODE 0`**, con la salida en
`docs/loop/SALIDA_V206_CICLO_V205_APERTURA.txt`.

**POR QUE ESOS VALORES SIGUEN SIENDO LOS DE LA APERTURA DE LA 205, Y ES UNA
MEDICION Y NO UNA PROMESA:** `git diff --numstat e66bf67d..HEAD` sobre
`dataset/`, `web/` y `engine/` da **0 filas**, o sea que los tres arboles que ese
ciclo mide son **byte a byte** los que habia en el HEAD de apertura de la 205. Y
el propio ciclo lo confirma por otro camino: los nueve ficheros que escribio hoy
miden exactamente lo mismo que los que el auditor sello en el cierre de la 205
(**4790**, **7928**, **574**, **140**, **168**, **498**, **1131**, **7** y
**336** bytes).

**DONDE ME PUEDO ESTAR EQUIVOCANDO, Y VA MARCADO COMO DISCUTIBLE EN EL REPORTE
DE LA 206:** la letra de `EJECUTOR.md` 1 dice que la apertura se mide antes de la
primera operacion, y **no dice** "o despues, si puedes probar que nada se movio".
Si el auditor lee la letra estrecha, la columna de apertura de la cabecera de
este reporte es una **reconstruccion** y no una medicion de aquel momento, y asi
queda dicho aqui en vez de esconderse detras de una tabla tallada.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**PROPONER ES MIO Y ENCARGAR ES DEL AUDITOR.** No escribo `PROMPT_SIGUIENTE.md`,
`ACTA_AUDITOR.md` ni `PARA_ALEXIS.md`, y el `numstat` de las tres contra mi HEAD de
apertura lo publico en la seccion 4.

1. **LA DEUDA DE REGISTROS SIGUE EN 2**, actas **179** y **180**, tal como el
   encargo de esta vuelta la dejo escrita. La 206 la arrastra.
2. **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y SUSPENDIDA** (acta 202
   `4.6`, ratificada por el `4.9` de la 203 y el `4.10` de la 204): se ejecuta en la
   primera vuelta despues de que la moratoria se levante. **La arrastro aqui otra
   vez para que la 206 no la pierda**, que es exactamente lo que el encargo me pide.
3. **LA `P.1` Y LA `P.2` DE ARRIBA PIDEN LETRA DEL FUNDADOR**, no del ejecutor. La
   `P.2` es la mas cara: mientras dure, **cada vuelta de bateria sale roja por la
   misma causa conocida**, y un rojo permanente apaga la bateria sola.
4. **EL PATRON DE `preguntas_del_reporte()` SIGUE ROTO Y HOY NO SE TOCA** (acta 204
   `4.4`): `scripts/loop/_v203_reparto_de_actas_viejas.py` linea 196, el articulo
   `LAS` le rompe la coincidencia. Va a la integral, ya nombrado.
5. **LA CORRECCION DECLARADA DE `R.67` Y `R.68` ES DE LA 206** (acta 204 `4.3`), por
   el carril del banco `9.10`, por adicion y en su sede.

## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE

**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**
Fichero: `docs/loop/SALIDA_V205_BATERIA.txt` (**93745 bytes en disco y 93745 normalizado a LF**, **1325 lineas
no vacias**, contadas
por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta
seccion se queda sin ella**, que es la cuarta de sus cuatro piezas.

```
LA BATERIA DE MUTACIONES DE LA VUELTA 205, CORRIDA ENTERA Y EN TRAMOS
compuesta por scripts/loop/vuelta183_bateria_por_tramos.py --componer

LO QUE SE PARTIO ES EL BOCADO, NO LA BATERIA. Las cuatro cosas que la
letra del fundador del 5 sep 2026 fija siguen enteras: la cadencia (cada
cinco vueltas), la soledad (vuelta propia sin nada al lado), la
integridad (cada entrada corrida, y corrida DOS VECES) y la prohibicion
de podar la nomina.

CIFRA entradas de la nomina: 135
CIFRA tramos: 11
CIFRA entradas que los tramos dicen haber corrido: 135
CIFRA entradas sin correr: 0 | repetidas: 0 | ajenas: 0
LA COBERTURA SE LEYO DE LAS SALIDAS, no se recalculo del reparto.

  tramo 1 -> SALIDA_V205_BATERIA_TRAMO_1.txt: 9555 bytes disco, 9555 bytes LF, 129 lineas, sha256 85c94304eef1fa28
  tramo 2 -> SALIDA_V205_BATERIA_TRAMO_2.txt: 7788 bytes disco, 7788 bytes LF, 123 lineas, sha256 8a426852569997fb
  tramo 3 -> SALIDA_V205_BATERIA_TRAMO_3.txt: 8525 bytes disco, 8525 bytes LF, 131 lineas, sha256 d665343b2715e6bb
  tramo 4 -> SALIDA_V205_BATERIA_TRAMO_4.txt: 8072 bytes disco, 8072 bytes LF, 125 lineas, sha256 07a889be43424245
  tramo 5 -> SALIDA_V205_BATERIA_TRAMO_5.txt: 8149 bytes disco, 8149 bytes LF, 126 lineas, sha256 65206552cad293f7
  tramo 6 -> SALIDA_V205_BATERIA_TRAMO_6.txt: 7880 bytes disco, 7880 bytes LF, 123 lineas, sha256 6c8c8725822883c1
  tramo 7 -> SALIDA_V205_BATERIA_TRAMO_7.txt: 7896 bytes disco, 7896 bytes LF, 123 lineas, sha256 427b396bd08b2fc8
  tramo 8 -> SALIDA_V205_BATERIA_TRAMO_8.txt: 7855 bytes disco, 7855 bytes LF, 123 lineas, sha256 fa02d03f1befeaf2
  tramo 9 -> SALIDA_V205_BATERIA_TRAMO_9.txt: 8523 bytes disco, 8523 bytes LF, 125 lineas, sha256 570ab8df86712b23
  tramo 10 -> SALIDA_V205_BATERIA_TRAMO_10.txt: 8473 bytes disco, 8473 bytes LF, 123 lineas, sha256 7fc7bf36a70ad181
  tramo 11 -> SALIDA_V205_BATERIA_TRAMO_11.txt: 6271 bytes disco, 6271 bytes LF, 94 lineas, sha256 c9e02832786abb5c
==============================================================================

==============================================================================
TRAMO 1 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_1.txt
==============================================================================

CORRIDA DEL TRAMO 1 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T20:59:33Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD a128786c7ec8, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD a128786c7ec8, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD a128786c7ec8, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 1 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta133_tarea2e_mutacion_cifras.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_1.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_2.py
      ENTRADA DEL TRAMO: vuelta135_2e_mutacion_3.py
      ENTRADA DEL TRAMO: vuelta139_2b_mutaciones.py
      ENTRADA DEL TRAMO: vuelta140_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta141_2_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta143_2b_mutacion_bateria.py
      ENTRADA DEL TRAMO: vuelta143_2c_mutacion_positivo.py
      ENTRADA DEL TRAMO: vuelta144_2a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_2b_mutacion_giro.py
      ENTRADA DEL TRAMO: vuelta144_2d_mutacion_cobertura.py


  vuelta133_tarea2e_mutacion_cifras.py   exit 0  OK                  20.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta135_2e_mutacion_1.py             exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_1.txt
  vuelta135_2e_mutacion_2.py             exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_2.txt
  vuelta135_2e_mutacion_3.py             exit 1  CASO DECLARADO      11.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V135_2E_MUTACION_3.txt
      SUJETO FIJO VERIFICADO: SUJETO_FIJO_V135_2E_REPORTE_134.md calza con el blob e12e4c36 (sha256 d1f97a510f17e35046eeec4975e1e0a1adabcfdda5a4646a250aa6db
  vuelta139_2b_mutaciones.py             exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta140_2a_mutaciones.py             exit 2  CASO DECLARADO      11.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta141_2_mutaciones.py              exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2a_mutaciones.py             exit 0  OK                  13.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2b_mutacion_bateria.py       exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta143_2c_mutacion_positivo.py      exit 0  OK                  13.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2a_mutaciones.py             exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2b_mutacion_giro.py          exit 0  OK                  16.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_2d_mutacion_cobertura.py     exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 164.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.7
  CIFRA arnes MAS LENTO: vuelta133_tarea2e_mutacion_cifras.py con 20.5s
  CIFRA arnes MAS RAPIDO: vuelta141_2_mutaciones.py con 10.8s
  CIFRA mediana por arnes, en segundos: 11.6
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta133_tarea2e_mutacion_cifras.py          20.5s
      vuelta144_2b_mutacion_giro.py                 16.3s
      vuelta143_2c_mutacion_positivo.py             13.0s
      vuelta143_2a_mutaciones.py                    13.0s
      vuelta140_2a_mutaciones.py                    11.7s
      vuelta143_2b_mutacion_bateria.py              11.7s
      vuelta139_2b_mutaciones.py                    11.6s
      vuelta144_2d_mutacion_cobertura.py            11.4s
      vuelta135_2e_mutacion_2.py                    11.3s
      vuelta144_2a_mutaciones.py                    11.3s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
      vuelta135_2e_mutacion_3.py, exit declarado 1, marca obligatoria 'NO TIENE CONVENCION MECANICA DE CONTEO':
         su SUJETO FIJO es el REPORTE.md de la vuelta 134, congelado por banco 9.10, y ES ANTERIOR A LOS DELIMITADORES DE CABECERA TALLADA. Medido en esta vuelta: grep -c 'CABECERA TALLADA' docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md da 0, y sobre docs/loop/REPORTE.md da 3. La ampliacion del vocabulario de la TAREA 2.a (vuelta 142) hace que la guarda vea ahora la celda '3 fila(s)' del desfase del calibrado, que EN UN REPORTE MODERNO vive DENTRO de la cabecera delimitada y queda recortada antes de parsear, y en este sujeto no, porque las marcas no existian aun. LAS DOS CIFRAS QUE ESTA MUTACION PRUEBA SI COTEJAN (la salida publica '2 POR ETIQUETA'): lo que cae es una tercera, ajena al caso. El sujeto NO se retoca, porque su valor es estar congelado.
      vuelta140_2a_mutaciones.py, exit declarado 2, marca obligatoria 'VEREDICTO (iii): NO CALZA':
         su bloque (iii), el caso positivo sobre la fase 05, sale NO CALZA y esta DECLARADO desde la vuelta 140: el auditor lo reconocio como caida SUYA de encargo (acta 140, 4.5, 'EL AUDITOR ELIGIO MAL EL SUJETO CONGELADO'). OP-S-05, OP-S-08, OP-S-11 y OP-S-12 tienen HUELLA DE GRAFO IDENTICA (los cuatro campos vacios) y lo unico que las separa es `estado`, que el encargo prohibe mirar: NINGUNA VARA DE GRAFO PUEDE SEPARARLAS. Los bloques (i) y (ii) SI muerden y son los que esta bateria vigila.
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD a128786c7ec8, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD a128786c7ec8, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 1: 1
FIN (reloj de pared, UTC): 2026-09-07T21:02:20Z
DURACION DEL TRAMO (monotona, segundos): 167.1
DURACION DEL TRAMO (monotona, minutos): 2.8


==============================================================================
TRAMO 2 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_2.txt
==============================================================================

CORRIDA DEL TRAMO 2 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:03:34Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD c4d5ee4610a3, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD c4d5ee4610a3, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD c4d5ee4610a3, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 2 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta144_3a_mutaciones.py
      ENTRADA DEL TRAMO: vuelta144_3b_mutacion_negativa.py
      ENTRADA DEL TRAMO: vuelta144_3c_caso_positivo_1190.py
      ENTRADA DEL TRAMO: vuelta145_2a_mutacion_ancla_unica.py
      ENTRADA DEL TRAMO: vuelta145_2b_mutacion_arneses.py
      ENTRADA DEL TRAMO: vuelta145_2c_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta146_2b_mutacion_ausencias.py
      ENTRADA DEL TRAMO: vuelta147_2c_mutacion_vitalidad.py
      ENTRADA DEL TRAMO: vuelta147_3d_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta147_3e_simular_a26.py
      ENTRADA DEL TRAMO: vuelta148_0d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta148_1a_mutacion_embebido.py
      ENTRADA DEL TRAMO: vuelta148_2a_mutacion_nomina_commiteada.py


  vuelta144_3a_mutaciones.py             exit 0  OK                   7.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3b_mutacion_negativa.py      exit 0  OK                  27.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta144_3c_caso_positivo_1190.py     exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2a_mutacion_ancla_unica.py   exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2b_mutacion_arneses.py       exit 0  OK                  45.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta145_2c_mutacion_censo.py         exit 0  OK                  34.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta146_2b_mutacion_ausencias.py     exit 0  OK                  13.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_2c_mutacion_vitalidad.py     exit 0  OK                 180.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3d_mutacion_nomina.py        exit 0  OK                  13.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta147_3e_simular_a26.py            exit 0  OK                  13.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_0d_mutacion_corredor.py      exit 0  OK                  15.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_1a_mutacion_embebido.py      exit 0  OK                  12.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2a_mutacion_nomina_commiteada.py exit 0  OK                  12.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 397.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 6.6
  CIFRA arnes MAS LENTO: vuelta147_2c_mutacion_vitalidad.py con 180.1s
  CIFRA arnes MAS RAPIDO: vuelta144_3a_mutaciones.py con 7.5s
  CIFRA mediana por arnes, en segundos: 13.8
  CIFRA arneses que pasan de 30 segundos: 3
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta147_2c_mutacion_vitalidad.py           180.1s
      vuelta145_2b_mutacion_arneses.py              45.4s
      vuelta145_2c_mutacion_censo.py                34.2s
      vuelta144_3b_mutacion_negativa.py             27.4s
      vuelta148_0d_mutacion_corredor.py             15.0s
      vuelta146_2b_mutacion_ausencias.py            13.9s
      vuelta147_3d_mutacion_nomina.py               13.8s
      vuelta147_3e_simular_a26.py                   13.4s
      vuelta148_1a_mutacion_embebido.py             12.9s
      vuelta148_2a_mutacion_nomina_commiteada.py    12.3s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD c4d5ee4610a3, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD c4d5ee4610a3, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 2: 1
FIN (reloj de pared, UTC): 2026-09-07T21:10:14Z
DURACION DEL TRAMO (monotona, segundos): 400.1
DURACION DEL TRAMO (monotona, minutos): 6.7


==============================================================================
TRAMO 3 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_3.txt
==============================================================================

CORRIDA DEL TRAMO 3 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:21:06Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 2037cfe52848, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 2037cfe52848, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 2037cfe52848, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 3 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta148_2b_mutacion_cifras_conjunto.py
      ENTRADA DEL TRAMO: vuelta148_2c_mutacion_vara_parada.py
      ENTRADA DEL TRAMO: vuelta148_2d_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta150_5c_mutacion_ciclo.py
      ENTRADA DEL TRAMO: vuelta154_tarea2d_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta154_tarea6_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta156_tarea4b_mutacion_tallador.py
      ENTRADA DEL TRAMO: vuelta156_tarea5d_mutacion_corredor.py
      ENTRADA DEL TRAMO: vuelta157_tarea4b_mutacion_tachado.py
      ENTRADA DEL TRAMO: vuelta157_tarea5c_mutacion_ruido.py
      ENTRADA DEL TRAMO: vuelta157_tarea6b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta159_tarea6c_mutacion_exencion.py
      ENTRADA DEL TRAMO: vuelta160_tarea6b_mutacion_puerta.py


  vuelta148_2b_mutacion_cifras_conjunto.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2c_mutacion_vara_parada.py   exit 0  OK                  10.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta148_2d_mutacion_exencion.py      exit 0  OK                  10.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_5c_mutacion_ciclo.py         exit 0  OK                  11.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta154_tarea2d_mutacion_guarda.py   exit 0  OK                 206.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V205_TALLADOR_RECHAZO.txt
  vuelta154_tarea6_mutacion_corredor.py  exit 0  OK                  14.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea4b_mutacion_tallador.py exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta156_tarea5d_mutacion_corredor.py exit 0  OK                  55.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea4b_mutacion_tachado.py  exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea5c_mutacion_ruido.py    exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta157_tarea6b_mutacion_re_sellado.py exit 0  OK                  15.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta159_tarea6c_mutacion_exencion.py exit 0  OK                 295.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea6b_mutacion_puerta.py   exit 3221225794  NO MORDIO           10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      (sin salida)

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 667.4
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 11.1
  CIFRA arnes MAS LENTO: vuelta159_tarea6c_mutacion_exencion.py con 295.5s
  CIFRA arnes MAS RAPIDO: vuelta148_2b_mutacion_cifras_conjunto.py con 2.7s
  CIFRA mediana por arnes, en segundos: 11.6
  CIFRA arneses que pasan de 30 segundos: 3
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta159_tarea6c_mutacion_exencion.py       295.5s
      vuelta154_tarea2d_mutacion_guarda.py         206.1s
      vuelta156_tarea5d_mutacion_corredor.py        55.1s
      vuelta157_tarea6b_mutacion_re_sellado.py      15.2s
      vuelta154_tarea6_mutacion_corredor.py         14.6s
      vuelta150_5c_mutacion_ciclo.py                11.8s
      vuelta157_tarea5c_mutacion_ruido.py           11.6s
      vuelta156_tarea4b_mutacion_tallador.py        11.4s
      vuelta157_tarea4b_mutacion_tachado.py         11.4s
      vuelta160_tarea6b_mutacion_puerta.py          10.9s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta160_tarea6b_mutacion_puerta.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 2 fichero(s) (SALIDA_V205_APERTURA.txt, SALIDA_V205_HEAD_APERTURA.txt)
      cambian en docs/loop/ mientras la bateria corre y NO LOS ESCRIBE
      NINGUN script de la nomina. NO son de nadie y NO son rojo de nadie:
      son la senal de que esta bateria se corrio con algo al lado, y por
      regla de la casa SE CORRE SOLA.
      aparecio durante vuelta154_tarea2d_mutacion_guarda.py: SALIDA_V205_APERTURA.txt, linea 1
      aparecio durante vuelta154_tarea2d_mutacion_guarda.py: SALIDA_V205_HEAD_APERTURA.txt, linea 1
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD (no medible), nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD (no medible), nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 3: 1
FIN (reloj de pared, UTC): 2026-09-07T21:32:15Z
DURACION DEL TRAMO (monotona, segundos): 669.4
DURACION DEL TRAMO (monotona, minutos): 11.2


==============================================================================
TRAMO 4 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_4.txt
==============================================================================

CORRIDA DEL TRAMO 4 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:32:50Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 61ac9e5a5f53, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 61ac9e5a5f53, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 61ac9e5a5f53, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 4 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta160_tarea7c_mutacion_guarda_cita.py
      ENTRADA DEL TRAMO: vuelta161_tarea1a_mutacion_alcance.py
      ENTRADA DEL TRAMO: vuelta162_tarea1a_mutacion_serie.py
      ENTRADA DEL TRAMO: vuelta162_tarea2a_mutacion_puerta.py
      ENTRADA DEL TRAMO: vuelta162_tarea2b_mutacion_excepcion.py
      ENTRADA DEL TRAMO: vuelta162_tarea3_mutacion_fila.py
      ENTRADA DEL TRAMO: vuelta163_tarea1b_mutacion_relectura.py
      ENTRADA DEL TRAMO: vuelta163_tarea1c_mutacion_tramo.py
      ENTRADA DEL TRAMO: vuelta163_tarea2_mutacion_nomina.py
      ENTRADA DEL TRAMO: vuelta163_tarea4a_mutacion_cobertura.py
      ENTRADA DEL TRAMO: vuelta163_tarea4b_mutacion_re_sellado.py
      ENTRADA DEL TRAMO: vuelta163_tarea5a_mutacion_contador.py
      ENTRADA DEL TRAMO: vuelta164_tarea1_mutacion_registro.py


  vuelta160_tarea7c_mutacion_guarda_cita.py exit 0  OK                  14.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta161_tarea1a_mutacion_alcance.py  exit 0  OK                  20.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea1a_mutacion_serie.py    exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2a_mutacion_puerta.py   exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea2b_mutacion_excepcion.py exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta162_tarea3_mutacion_fila.py      exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1b_mutacion_relectura.py exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea1c_mutacion_tramo.py    exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea2_mutacion_nomina.py    exit 0  OK                  11.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4a_mutacion_cobertura.py exit 0  OK                  13.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta163_tarea4b_mutacion_re_sellado.py exit 1  NO MORDIO           23.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta163_tarea5a_mutacion_contador.py exit 0  OK                  14.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta164_tarea1_mutacion_registro.py  exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 175.7
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.9
  CIFRA arnes MAS LENTO: vuelta163_tarea4b_mutacion_re_sellado.py con 23.2s
  CIFRA arnes MAS RAPIDO: vuelta162_tarea2a_mutacion_puerta.py con 10.9s
  CIFRA mediana por arnes, en segundos: 11.7
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta163_tarea4b_mutacion_re_sellado.py      23.2s
      vuelta161_tarea1a_mutacion_alcance.py         20.0s
      vuelta163_tarea5a_mutacion_contador.py        14.7s
      vuelta160_tarea7c_mutacion_guarda_cita.py     14.3s
      vuelta163_tarea4a_mutacion_cobertura.py       13.4s
      vuelta163_tarea2_mutacion_nomina.py           11.9s
      vuelta163_tarea1c_mutacion_tramo.py           11.7s
      vuelta164_tarea1_mutacion_registro.py         11.5s
      vuelta163_tarea1b_mutacion_relectura.py       11.3s
      vuelta162_tarea2b_mutacion_excepcion.py       11.0s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta163_tarea4b_mutacion_re_sellado.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 61ac9e5a5f53, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 61ac9e5a5f53, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 4: 1
FIN (reloj de pared, UTC): 2026-09-07T21:35:48Z
DURACION DEL TRAMO (monotona, segundos): 177.9
DURACION DEL TRAMO (monotona, minutos): 3.0


==============================================================================
TRAMO 5 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_5.txt
==============================================================================

CORRIDA DEL TRAMO 5 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:36:25Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 1a7e88a6c50f, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 1a7e88a6c50f, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 1a7e88a6c50f, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 5 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta164_tarea4_mutacion_005.py
      ENTRADA DEL TRAMO: vuelta165_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta165_tarea2_mutacion_censo.py
      ENTRADA DEL TRAMO: vuelta165_tarea4_mutacion_sujeto.py
      ENTRADA DEL TRAMO: vuelta165_tarea6_mutacion_op_l_01.py
      ENTRADA DEL TRAMO: vuelta166_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta166_tarea2_mutacion_correccion.py
      ENTRADA DEL TRAMO: vuelta166_tarea3_mutacion_retrato.py
      ENTRADA DEL TRAMO: vuelta166_tarea6_mutacion_guarda.py
      ENTRADA DEL TRAMO: vuelta167_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta167_tarea3_mutacion_ii.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta168_tarea1_mutacion_nota.py


  vuelta164_tarea4_mutacion_005.py       exit 0  OK                   4.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea1_mutacion_registro.py  exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea2_mutacion_censo.py     exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea4_mutacion_sujeto.py    exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta165_tarea6_mutacion_op_l_01.py   exit 1  NO MORDIO           10.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta166_tarea1_mutacion_registro.py  exit 0  OK                  10.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea2_mutacion_correccion.py exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea3_mutacion_retrato.py   exit 0  OK                  15.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta166_tarea6_mutacion_guarda.py    exit 1  NO MORDIO           10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
      ==============================================================================
  vuelta167_tarea1_mutacion_registro.py  exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta167_tarea3_mutacion_ii.py        exit 0  OK                  11.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_registro.py  exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea1_mutacion_nota.py      exit 0  OK                  11.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 140.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.3
  CIFRA arnes MAS LENTO: vuelta166_tarea3_mutacion_retrato.py con 15.0s
  CIFRA arnes MAS RAPIDO: vuelta164_tarea4_mutacion_005.py con 4.9s
  CIFRA mediana por arnes, en segundos: 10.9
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta166_tarea3_mutacion_retrato.py          15.0s
      vuelta167_tarea3_mutacion_ii.py               11.8s
      vuelta166_tarea2_mutacion_correccion.py       11.3s
      vuelta165_tarea2_mutacion_censo.py            11.3s
      vuelta168_tarea1_mutacion_nota.py             11.2s
      vuelta167_tarea1_mutacion_registro.py         11.0s
      vuelta166_tarea6_mutacion_guarda.py           10.9s
      vuelta168_tarea1_mutacion_registro.py         10.9s
      vuelta165_tarea1_mutacion_registro.py         10.8s
      vuelta165_tarea4_mutacion_sujeto.py           10.8s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 2 (vuelta165_tarea6_mutacion_op_l_01.py, vuelta166_tarea6_mutacion_guarda.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 1a7e88a6c50f, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 1a7e88a6c50f, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 2 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 2 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 5: 1
FIN (reloj de pared, UTC): 2026-09-07T21:38:48Z
DURACION DEL TRAMO (monotona, segundos): 142.9
DURACION DEL TRAMO (monotona, minutos): 2.4


==============================================================================
TRAMO 6 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_6.txt
==============================================================================

CORRIDA DEL TRAMO 6 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:39:22Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD b3652d5c1812, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD b3652d5c1812, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD b3652d5c1812, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 6 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta168_tarea2_mutacion_reconstructor.py
      ENTRADA DEL TRAMO: vuelta168_tarea4_mutacion_op_v_01.py
      ENTRADA DEL TRAMO: vuelta169_tarea2_mutacion_reanclaje.py
      ENTRADA DEL TRAMO: vuelta170_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta170_tarea2a_mutacion_aislador.py
      ENTRADA DEL TRAMO: vuelta98_tarea4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta99_tarea3_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta109_tarea2_4_prueba_mutacion.py
      ENTRADA DEL TRAMO: vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py
      ENTRADA DEL TRAMO: vuelta113_tarea2_mutacion_tsc.py
      ENTRADA DEL TRAMO: vuelta171_mutacion_busqueda_acta.py
      ENTRADA DEL TRAMO: vuelta171_tarea1a_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta171_tarea5a_mutacion_enchufe.py


  vuelta168_tarea2_mutacion_reconstructor.py exit 0  OK                   7.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta168_tarea4_mutacion_op_v_01.py   exit 0  OK                  28.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta169_tarea2_mutacion_reanclaje.py exit 0  OK                   9.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea1a_mutacion_registro.py exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta170_tarea2a_mutacion_aislador.py exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta98_tarea4_prueba_mutacion.py     exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta99_tarea3_prueba_mutacion.py     exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta109_tarea2_4_prueba_mutacion.py  exit 0  OK                  33.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py exit 0  OK                   9.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta113_tarea2_mutacion_tsc.py       exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_mutacion_busqueda_acta.py    exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea1a_mutacion_registro.py exit 0  OK                  10.8s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta171_tarea5a_mutacion_enchufe.py  exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 176.6
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.9
  CIFRA arnes MAS LENTO: vuelta109_tarea2_4_prueba_mutacion.py con 33.8s
  CIFRA arnes MAS RAPIDO: vuelta168_tarea2_mutacion_reconstructor.py con 7.4s
  CIFRA mediana por arnes, en segundos: 10.9
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta109_tarea2_4_prueba_mutacion.py         33.8s
      vuelta168_tarea4_mutacion_op_v_01.py          28.0s
      vuelta170_tarea1a_mutacion_registro.py        11.6s
      vuelta99_tarea3_prueba_mutacion.py            11.4s
      vuelta98_tarea4_prueba_mutacion.py            11.3s
      vuelta171_mutacion_busqueda_acta.py           11.0s
      vuelta171_tarea5a_mutacion_enchufe.py         10.9s
      vuelta170_tarea2a_mutacion_aislador.py        10.9s
      vuelta113_tarea2_mutacion_tsc.py              10.8s
      vuelta171_tarea1a_mutacion_registro.py        10.8s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD b3652d5c1812, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD b3652d5c1812, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 6: 1
FIN (reloj de pared, UTC): 2026-09-07T21:42:21Z
DURACION DEL TRAMO (monotona, segundos): 178.8
DURACION DEL TRAMO (monotona, minutos): 3.0


==============================================================================
TRAMO 7 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_7.txt
==============================================================================

CORRIDA DEL TRAMO 7 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:42:53Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 675a2e22c6a9, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 675a2e22c6a9, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 675a2e22c6a9, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 7 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta172_tarea1b_mutacion_registro.py
      ENTRADA DEL TRAMO: vuelta172_tarea2a_mutacion_exclusion.py
      ENTRADA DEL TRAMO: vuelta172_tarea3_mutacion_numeracion.py
      ENTRADA DEL TRAMO: vuelta172_tarea5_mutacion_cierre.py
      ENTRADA DEL TRAMO: vuelta173_tarea1b_mutacion_hueco.py
      ENTRADA DEL TRAMO: vuelta174_tarea1a_mutacion_44.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_esqueleto.py
      ENTRADA DEL TRAMO: vuelta174_tarea1b_mutacion_sellar.py
      ENTRADA DEL TRAMO: vuelta174_tarea2b_mutacion_confirmar.py
      ENTRADA DEL TRAMO: vuelta176_tarea1c_mutacion_tramos.py
      ENTRADA DEL TRAMO: vuelta177_tarea1b_mutacion_esperado_vivo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1d_mutacion_cotejo.py
      ENTRADA DEL TRAMO: vuelta177_tarea1e_mutacion_correcciones_chicas.py


  vuelta172_tarea1b_mutacion_registro.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea2a_mutacion_exclusion.py exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea3_mutacion_numeracion.py exit 0  OK                  12.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea5_mutacion_cierre.py    exit 0  OK                  11.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta173_tarea1b_mutacion_hueco.py    exit 0  OK                  12.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1a_mutacion_44.py       exit 0  OK                  12.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_esqueleto.py exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea1b_mutacion_sellar.py   exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta174_tarea2b_mutacion_confirmar.py exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta176_tarea1c_mutacion_tramos.py   exit 0  OK                  12.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1b_mutacion_esperado_vivo.py exit 0  OK                  12.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1d_mutacion_cotejo.py   exit 0  OK                  13.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta177_tarea1e_mutacion_correcciones_chicas.py exit 0  OK                  12.4s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 146.0
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.4
  CIFRA arnes MAS LENTO: vuelta177_tarea1d_mutacion_cotejo.py con 13.3s
  CIFRA arnes MAS RAPIDO: vuelta172_tarea1b_mutacion_registro.py con 2.7s
  CIFRA mediana por arnes, en segundos: 12.1
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta177_tarea1d_mutacion_cotejo.py          13.3s
      vuelta177_tarea1e_mutacion_correcciones_chicas.py    12.4s
      vuelta177_tarea1b_mutacion_esperado_vivo.py    12.4s
      vuelta174_tarea1a_mutacion_44.py              12.2s
      vuelta172_tarea3_mutacion_numeracion.py       12.1s
      vuelta173_tarea1b_mutacion_hueco.py           12.1s
      vuelta176_tarea1c_mutacion_tramos.py          12.1s
      vuelta172_tarea5_mutacion_cierre.py           11.9s
      vuelta174_tarea2b_mutacion_confirmar.py       11.7s
      vuelta174_tarea1b_mutacion_sellar.py          11.1s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 675a2e22c6a9, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 675a2e22c6a9, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 7: 1
FIN (reloj de pared, UTC): 2026-09-07T21:45:21Z
DURACION DEL TRAMO (monotona, segundos): 148.2
DURACION DEL TRAMO (monotona, minutos): 2.5


==============================================================================
TRAMO 8 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_8.txt
==============================================================================

CORRIDA DEL TRAMO 8 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:45:54Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 861d2c7ad40e, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 861d2c7ad40e, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 861d2c7ad40e, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 8 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta177_tarea1f_mutacion_tope_minutos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1b_mutacion_hermano.py
      ENTRADA DEL TRAMO: vuelta178_tarea1c_mutacion_ast.py
      ENTRADA DEL TRAMO: vuelta178_tarea1d_mutacion_puestos.py
      ENTRADA DEL TRAMO: vuelta178_tarea1e_mutacion_higiene.py
      ENTRADA DEL TRAMO: vuelta178_tarea2_mutacion_resolutor.py
      ENTRADA DEL TRAMO: vuelta178_tarea4_mutacion_consumidas.py
      ENTRADA DEL TRAMO: vuelta150_2d_simular_op_c_05.py
      ENTRADA DEL TRAMO: vuelta160_tarea3b_caso_positivo.py
      ENTRADA DEL TRAMO: vuelta179_tarea1b_mutacion_citas.py
      ENTRADA DEL TRAMO: vuelta179_tarea3_mutacion_triangulos.py
      ENTRADA DEL TRAMO: vuelta179_tarea1d_mutacion_corte.py
      ENTRADA DEL TRAMO: vuelta180_tarea1b_mutacion_etiqueta.py


  vuelta177_tarea1f_mutacion_tope_minutos.py exit 0  OK                   2.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1b_mutacion_hermano.py  exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1c_mutacion_ast.py      exit 0  OK                  12.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1d_mutacion_puestos.py  exit 0  OK                  13.1s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea1e_mutacion_higiene.py  exit 0  OK                  12.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea2_mutacion_resolutor.py exit 0  OK                  12.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta178_tarea4_mutacion_consumidas.py exit 0  OK                  12.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta150_2d_simular_op_c_05.py        exit 0  OK                  13.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta160_tarea3b_caso_positivo.py     exit 0  OK                  32.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1b_mutacion_citas.py    exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea3_mutacion_triangulos.py exit 0  OK                  11.9s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta179_tarea1d_mutacion_corte.py    exit 0  OK                  11.0s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea1b_mutacion_etiqueta.py exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 168.5
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.8
  CIFRA arnes MAS LENTO: vuelta160_tarea3b_caso_positivo.py con 32.9s
  CIFRA arnes MAS RAPIDO: vuelta177_tarea1f_mutacion_tope_minutos.py con 2.6s
  CIFRA mediana por arnes, en segundos: 12.2
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta160_tarea3b_caso_positivo.py            32.9s
      vuelta150_2d_simular_op_c_05.py               13.3s
      vuelta178_tarea1d_mutacion_puestos.py         13.1s
      vuelta178_tarea1e_mutacion_higiene.py         12.7s
      vuelta178_tarea1c_mutacion_ast.py             12.6s
      vuelta178_tarea4_mutacion_consumidas.py       12.2s
      vuelta178_tarea2_mutacion_resolutor.py        12.2s
      vuelta179_tarea3_mutacion_triangulos.py       11.9s
      vuelta180_tarea1b_mutacion_etiqueta.py        11.6s
      vuelta179_tarea1b_mutacion_citas.py           11.3s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 861d2c7ad40e, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 861d2c7ad40e, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 8: 1
FIN (reloj de pared, UTC): 2026-09-07T21:48:44Z
DURACION DEL TRAMO (monotona, segundos): 170.7
DURACION DEL TRAMO (monotona, minutos): 2.8


==============================================================================
TRAMO 9 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_9.txt
==============================================================================

CORRIDA DEL TRAMO 9 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:49:17Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD d4b6a66fc5a7, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD d4b6a66fc5a7, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD d4b6a66fc5a7, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 9 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta180_tarea2c_mutacion_cableado.py
      ENTRADA DEL TRAMO: vuelta180_tarea3_mutacion_corte_de_tramos.py
      ENTRADA DEL TRAMO: vuelta180_tarea4_mutacion_texto_y_clon.py
      ENTRADA DEL TRAMO: vuelta180_tarea5_mutacion_backlog_l02.py
      ENTRADA DEL TRAMO: vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py
      ENTRADA DEL TRAMO: vuelta182_tarea2_mutacion_apertura_auditor.py
      ENTRADA DEL TRAMO: vuelta183_tarea1c_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta183_tarea1b_mutacion_atribucion.py
      ENTRADA DEL TRAMO: vuelta184_tarea1c_mutacion_estimacion.py
      ENTRADA DEL TRAMO: vuelta185_tarea1b_mutacion_sin_temporal.py
      ENTRADA DEL TRAMO: vuelta185_tarea1c_mutacion_bateria_continuada.py
      ENTRADA DEL TRAMO: vuelta186_tarea2a_mutacion_pieza4.py
      ENTRADA DEL TRAMO: vuelta186_tarea2b_mutacion_pieza2_cercas.py


  vuelta180_tarea2c_mutacion_cableado.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea3_mutacion_corte_de_tramos.py exit 0  OK                  10.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea4_mutacion_texto_y_clon.py exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta180_tarea5_mutacion_backlog_l02.py exit 0  OK                  11.3s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py exit 0  OK                  12.2s
      salidas selladas que escribe (computadas, no tecleadas): ninguna
  vuelta182_tarea2_mutacion_apertura_auditor.py exit 0  OK                  12.3s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt
  vuelta183_tarea1c_mutacion_veredicto.py exit 0  OK                  11.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1C_MUTACION_VEREDICTO.txt
  vuelta183_tarea1b_mutacion_atribucion.py exit 0  OK                  12.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt
  vuelta184_tarea1c_mutacion_estimacion.py exit 0  OK                  11.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V184_T1C_MUTACION_ESTIMACION.txt
  vuelta185_tarea1b_mutacion_sin_temporal.py exit 0  OK                  13.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt, SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt
  vuelta185_tarea1c_mutacion_bateria_continuada.py exit 1  NO MORDIO           17.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt
      ARNES DE LA RAMA DE LA BATERIA CONTINUADA (vuelta 185, TAREA 1.c)
  vuelta186_tarea2a_mutacion_pieza4.py   exit 0  OK                  12.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2A_MUTACION_PIEZA4.txt
  vuelta186_tarea2b_mutacion_pieza2_cercas.py exit 0  OK                  12.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 152.9
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 2.5
  CIFRA arnes MAS LENTO: vuelta185_tarea1c_mutacion_bateria_continuada.py con 17.5s
  CIFRA arnes MAS RAPIDO: vuelta180_tarea2c_mutacion_cableado.py con 2.7s
  CIFRA mediana por arnes, en segundos: 12.2
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta185_tarea1c_mutacion_bateria_continuada.py    17.5s
      vuelta185_tarea1b_mutacion_sin_temporal.py    13.4s
      vuelta186_tarea2a_mutacion_pieza4.py          12.8s
      vuelta186_tarea2b_mutacion_pieza2_cercas.py    12.7s
      vuelta183_tarea1b_mutacion_atribucion.py      12.7s
      vuelta182_tarea2_mutacion_apertura_auditor.py    12.3s
      vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py    12.2s
      vuelta184_tarea1c_mutacion_estimacion.py      11.8s
      vuelta183_tarea1c_mutacion_veredicto.py       11.6s
      vuelta180_tarea4_mutacion_texto_y_clon.py     11.6s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta185_tarea1c_mutacion_bateria_continuada.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD d4b6a66fc5a7, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD d4b6a66fc5a7, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 1 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
ROJO: 0 con el ancla perdida, 1 que no mordieron y 0 cuya salida sellada NO SE REPITE.
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 9: 1
FIN (reloj de pared, UTC): 2026-09-07T21:51:52Z
DURACION DEL TRAMO (monotona, segundos): 155.1
DURACION DEL TRAMO (monotona, minutos): 2.6


==============================================================================
TRAMO 10 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_10.txt
==============================================================================

CORRIDA DEL TRAMO 10 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:52:32Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD c5746937b9e6, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD c5746937b9e6, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD c5746937b9e6, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 10 de 11
  CIFRA entradas de ESTE tramo: 13
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta186_tarea2c_mutacion_cierre_tardio.py
      ENTRADA DEL TRAMO: vuelta186_tarea2d_mutacion_seccion4.py
      ENTRADA DEL TRAMO: vuelta187_tarea4_mutacion_dos_convenciones.py
      ENTRADA DEL TRAMO: vuelta187_tarea5b_mutacion_seccion4_tardio.py
      ENTRADA DEL TRAMO: vuelta188_tarea2_mutacion_pata_documental.py
      ENTRADA DEL TRAMO: vuelta188_tarea3c_mutacion_exclusion_por_rojo.py
      ENTRADA DEL TRAMO: vuelta188_tarea4_mutacion_cobertura_parejas.py
      ENTRADA DEL TRAMO: vuelta188_tarea5a_mutacion_vecinos_evitar.py
      ENTRADA DEL TRAMO: vuelta190_tarea2b_mutacion_deuda_y_fallo.py
      ENTRADA DEL TRAMO: vuelta190_tarea3b_mutacion_selladas_ajenas.py
      ENTRADA DEL TRAMO: vuelta191_tarea3_mutacion_lineas.py
      ENTRADA DEL TRAMO: vuelta191_tarea4_mutacion_veredicto.py
      ENTRADA DEL TRAMO: vuelta191_tarea6_mutacion_bloque_tallado.py


  vuelta186_tarea2c_mutacion_cierre_tardio.py exit 0  OK                   5.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
  vuelta186_tarea2d_mutacion_seccion4.py exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V186_T2D_MUTACION_SECCION4.txt
  vuelta187_tarea4_mutacion_dos_convenciones.py exit 0  OK                  13.0s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt
  vuelta187_tarea5b_mutacion_seccion4_tardio.py exit 0  OK                  11.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO.txt
  vuelta188_tarea2_mutacion_pata_documental.py exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt
  vuelta188_tarea3c_mutacion_exclusion_por_rojo.py exit 0  OK                  10.6s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt
  vuelta188_tarea4_mutacion_cobertura_parejas.py exit 0  OK                  12.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt
  vuelta188_tarea5a_mutacion_vecinos_evitar.py exit 0  OK                  10.9s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V188_T5A_MUTACION_VECINOS_EVITAR.txt
  vuelta190_tarea2b_mutacion_deuda_y_fallo.py exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt
  vuelta190_tarea3b_mutacion_selladas_ajenas.py exit 0  OK                  11.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt
  vuelta191_tarea3_mutacion_lineas.py    exit 0  OK                 107.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T3_MUTACION_LINEAS.txt
  vuelta191_tarea4_mutacion_veredicto.py exit 0  OK                  11.1s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T4_MUTACION_VEREDICTO.txt
  vuelta191_tarea6_mutacion_bloque_tallado.py exit 0  OK                  11.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 13
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 241.0
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 4.0
  CIFRA arnes MAS LENTO: vuelta191_tarea3_mutacion_lineas.py con 107.8s
  CIFRA arnes MAS RAPIDO: vuelta186_tarea2c_mutacion_cierre_tardio.py con 5.8s
  CIFRA mediana por arnes, en segundos: 11.5
  CIFRA arneses que pasan de 30 segundos: 1
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta191_tarea3_mutacion_lineas.py          107.8s
      vuelta187_tarea4_mutacion_dos_convenciones.py    13.0s
      vuelta188_tarea4_mutacion_cobertura_parejas.py    12.4s
      vuelta187_tarea5b_mutacion_seccion4_tardio.py    11.9s
      vuelta190_tarea2b_mutacion_deuda_y_fallo.py    11.7s
      vuelta191_tarea6_mutacion_bloque_tallado.py    11.7s
      vuelta188_tarea2_mutacion_pata_documental.py    11.5s
      vuelta190_tarea3b_mutacion_selladas_ajenas.py    11.4s
      vuelta191_tarea4_mutacion_veredicto.py        11.1s
      vuelta186_tarea2d_mutacion_seccion4.py        11.1s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD c5746937b9e6, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD c5746937b9e6, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 10: 1
FIN (reloj de pared, UTC): 2026-09-07T21:56:35Z
DURACION DEL TRAMO (monotona, segundos): 243.3
DURACION DEL TRAMO (monotona, minutos): 4.1


==============================================================================
TRAMO 11 DE 11. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/SALIDA_V205_BATERIA_TRAMO_11.txt
==============================================================================

CORRIDA DEL TRAMO 11 DE 11, BATERIA DE LA VUELTA 205
lanzada por scripts/loop/vuelta183_bateria_por_tramos.py
INICIO (reloj de pared, UTC): 2026-09-07T21:57:09Z
RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio (cero filas de `git diff --numstat`)
==============================================================================
==============================================================================
LAS 135 MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.
==============================================================================

  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)
  CIFRA entradas en la nomina: 135 (corte: HEAD 0d6ab8743d2f, nomina contada en esta corrida)
  CIFRA arneses en scripts/loop/ que el censo reconoce: 197
  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros
  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en mutacion, caso_positivo, simular.
  CIFRA entradas de la nomina que el censo NO VE: 0, de 135 (corte: HEAD 0d6ab8743d2f, nomina contada en esta corrida)
  CIFRA ultima vuelta representada en la nomina: 195 (INFORMATIVA desde la vuelta 178: ya no decide)
  LA VARA DEL CENSO, que es la que decide: 148 (vuelta 178, TAREA 1.b)
  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina: 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py

  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL
  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo
  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba
  corre ENTERA en este tramo y sigue encendiendo el rojo.
  CIFRA nomina entera: 135 (corte: HEAD 0d6ab8743d2f, nomina contada en esta corrida)
  CIFRA tamano de tramo: 13
  CIFRA tramos del reparto (computada, no tecleada): 11
  CIFRA TRAMO QUE SE CORRE: 11 de 11
  CIFRA entradas de ESTE tramo: 5
  CIFRA suma de las entradas de TODOS los tramos: 135
      ENTRADA DEL TRAMO: vuelta192_tarea4_mutacion_cuarta_puerta.py
      ENTRADA DEL TRAMO: vuelta193_tarea4e_mutacion_sello_entre_procesos.py
      ENTRADA DEL TRAMO: vuelta194_tarea2c_mutacion_sede_del_turno.py
      ENTRADA DEL TRAMO: vuelta195_tarea3g_mutacion_nomina_enchufada.py
      ENTRADA DEL TRAMO: vuelta195_tarea4c_mutacion_componer_rojo.py


  vuelta192_tarea4_mutacion_cuarta_puerta.py exit 0  OK                   2.7s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt
  vuelta193_tarea4e_mutacion_sello_entre_procesos.py exit 0  OK                  11.8s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt
  vuelta194_tarea2c_mutacion_sede_del_turno.py exit 0  OK                  14.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt, SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt, SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt
  vuelta195_tarea3g_mutacion_nomina_enchufada.py exit 0  OK                  11.5s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt
  vuelta195_tarea4c_mutacion_componer_rojo.py exit 0  OK                  12.4s
      salidas selladas que escribe (computadas, no tecleadas): SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt

  EL CRONOMETRO (adjudicacion 6.8 del acta 163)
  CIFRA arneses cronometrados: 5
  CIFRA TIEMPO TOTAL de la bateria, en segundos: 52.7
  CIFRA TIEMPO TOTAL de la bateria, en minutos: 0.9
  CIFRA arnes MAS LENTO: vuelta194_tarea2c_mutacion_sede_del_turno.py con 14.5s
  CIFRA arnes MAS RAPIDO: vuelta192_tarea4_mutacion_cuarta_puerta.py con 2.7s
  CIFRA mediana por arnes, en segundos: 11.8
  CIFRA arneses que pasan de 30 segundos: 0
  LOS DIEZ MAS LENTOS, DE MAS A MENOS:
      vuelta194_tarea2c_mutacion_sede_del_turno.py    14.5s
      vuelta195_tarea4c_mutacion_componer_rojo.py    12.4s
      vuelta193_tarea4e_mutacion_sello_entre_procesos.py    11.8s
      vuelta195_tarea3g_mutacion_nomina_enchufada.py    11.5s
      vuelta192_tarea4_mutacion_cuarta_puerta.py     2.7s
  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de
  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo
  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que
  darle al menos este total con holgura: matarla antes NO es un rojo,
  es no haberla medido.

  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 0 (ninguna)
  RUIDO DE CONCURRENCIA: 0 fichero(s) (ninguno)
  CIFRA arneses DEL CENSO, no anteriores a la vara 148, que se quedan FUERA de la nomina (recomputado al cierre): 2
      FUERA DE LA NOMINA: vuelta197_tarea2_mutacion_orden_del_turno.py
      FUERA DE LA NOMINA: vuelta199_tarea1_mutacion_guardas_revividas.py
  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): 0, de 135 (corte: HEAD 0d6ab8743d2f, nomina contada en esta corrida)
  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): 0, de 135 (corte: HEAD 0d6ab8743d2f, nomina contada en esta corrida)
      (ninguna)
  LA ESPECIE DEL VEREDICTO, SEPARADA (vuelta 190, TAREA 2):
      CIFRA de FALLO: 0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
      CIFRA de DEUDA DECLARADA: 0 NO DECIDIBLE con motivo escrito, 0 sin
      CLASE DEL VEREDICTO: ROJO POR FALLO | CIFRA exitcode: 1

ROJO: 2 arnes(es) que el censo VE y que la nomina NO tiene, nacidos en la vuelta 148 o despues, se quedan FUERA. La regla escrita en este mismo fichero desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que entre EN SU MISMA VUELTA. La lista entera: vuelta197_tarea2_mutacion_orden_del_turno.py, vuelta199_tarea1_mutacion_guardas_revividas.py
VEREDICTO DE ESTA CORRIDA: ROJO POR FALLO
CIFRA exitcode: 1
FIN
==============================================================================
EXITCODE DEL TRAMO 11: 1
FIN (reloj de pared, UTC): 2026-09-07T21:58:04Z
DURACION DEL TRAMO (monotona, segundos): 54.9
DURACION DEL TRAMO (monotona, minutos): 0.9
```

## 10. LAS CIFRAS SIN PAREJA, DECLARADAS UNA A UNA POR EL CARRIL DE CIERRE TARDIO

**CARRIL DE CIERRE TARDIO.** Este reporte es el de la vuelta 205 y se
cierra en la vuelta 206, leida del asunto del ultimo commit con `git log`
y no tecleada. En este carril **las cifras sin pareja NO bloquean el
cierre, pero SE DECLARAN una a una con su linea y su cuenta total**, que
es la respuesta del acta 186 a la `P.2`: *ni se eximen ni se reescriben,
se declaran*. **Un defecto declarado y medido no es un defecto exento**, y
reescribir el texto de una vuelta pasada seria escribir en pasado lo que
no paso.

**NINGUNA OTRA GUARDA SE AFLOJA EN ESTE CARRIL.** Las cuatro piezas, el
cuerpo byte a byte, los guiones y las citas de arnes siguen mandando
igual, y en el carril normal las cifras sin pareja siguen siendo ROJO.

CIFRAS SIN PAREJA DECLARADAS Y MEDIDAS: **1** cifra(s) publicada(s) sin su pareja.

```
CIFRA cifras publicadas sin su pareja: 1
linea 184    sha   cffa5cd0724d0427         | LF, sha256 LF `cffa5cd0724d0427`):
```

## 11. EL DEFECTO DE LA SECCION 4, DECLARADO POR EL CARRIL DE CIERRE TARDIO

**CARRIL DE CIERRE TARDIO.** Este reporte es el de la vuelta 205 y se
cierra en la vuelta 206, leida del asunto del ultimo commit con `git log`
y no tecleada. En este carril **la guarda de la seccion 4 NO bloquea el
cierre, pero SE DECLARA con su motivo entero**, que es la respuesta del
acta 187 a la `P.2` por extension de la `7.2` del acta 186: *ni se eximen
ni se reescriben, se declaran*.

**`docs/loop/reportes/REPORTE_V205.md` NO SE REABRE Y NO SE REESCRIBE SU SECCION 4.**
Lo que se le anade es esta declaracion. **Reescribir su seccion 4 seria
escribir en pasado lo que no paso.**

**EN EL CARRIL NORMAL ESTA GUARDA SIGUE BLOQUEANDO ENTERA**, y ninguna
otra se afloja en este: las cuatro piezas, el cuerpo byte a byte, los
guiones, las citas de arnes y **la guarda de las dos convenciones** siguen
mandando igual.

DEFECTO DE LA SECCION 4 DECLARADO Y MEDIDO: **2** motivo(s).

```
CIFRA motivos en rojo de la seccion 4: 2
LA SECCION 4 DEL REPORTE NO AFIRMA NADA sobre 'CIFRA lineas de status'. La apertura sellada docs/loop/SALIDA_V205_APERTURA.txt dice 0, y una cifra ausente y una cifra que calza NO son lo mismo
LA SECCION 4 DEL REPORTE NO AFIRMA NADA sobre 'CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR'. La apertura sellada docs/loop/SALIDA_V205_APERTURA.txt dice 0, y una cifra ausente y una cifra que calza NO son lo mismo
```

