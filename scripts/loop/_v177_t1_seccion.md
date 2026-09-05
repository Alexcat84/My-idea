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
