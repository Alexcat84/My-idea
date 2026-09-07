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
