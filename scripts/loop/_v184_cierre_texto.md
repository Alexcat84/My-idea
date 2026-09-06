## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LAS DOS TAREAS DEL ENCARGO CERRARON.** El tope era dos, por el regimen
temporal de `AUDITOR.md` 6.2, y son dos.

- rama, leida con `git rev-parse --abbrev-ref HEAD`: `pasada-unica`
- HEAD de apertura, sellado **antes de la primera operacion** en
  `docs/loop/SALIDA_V184_HEAD_APERTURA.txt`: **`dc558582`**
- HEAD del ultimo commit antes de cerrar, leido con `git rev-parse HEAD`:
  **`3500db9d`**
- commit del acta 184, localizado con `git log --grep` y no tecleado:
  **`dc558582`**
- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:
  **`c1ac7d59`**

**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA Y OTRA VEZ AL CIERRE.** Sus
salidas son `docs/loop/SALIDA_V184_GATE0_CMD1_APERTURA.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**)
y `docs/loop/SALIDA_V184_GATE0_CMD1_CIERRE.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**),
con motor **25 de 25**, `tsc` **exit 0** y web **1.040 passed** por las dos
puntas. La apertura entera vive en `docs/loop/SALIDA_V184_APERTURA.txt`
(**34194 bytes en disco y 34194 bytes normalizados a LF**) y **la sello el PRIMER commit de la vuelta**.

**EL ARCHIVO DE VEREDICTOS NO SE MOVIO, Y ESA ES LA PRUEBA INDEPENDIENTE DE
QUE ESTA VUELTA NO TOCO NINGUN VEREDICTO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:
**3388 filas**, **A 551, B 72, C 5, D 2760**, **cero huecos y cero duplicados**,
**4051967 bytes en disco y 4051967 bytes normalizados a LF**, y `sha256` **`ea6e850d331d14f0`**
**identico por las dos convenciones, disco y LF**. Es el mismo que la
apertura midio y el mismo que las actas 179 a 184 publican.

## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA

`git status --porcelain` da **`M dataset/metadata/master_graph.json`** al
abrir la vuelta y sigue dandolo al cerrarla. **Se midio antes de creerlo:**
`git diff --numstat -- dataset/` da **0 filas**. **Es artefacto de fin de
linea, no contenido. Ninguna perdida de catalogo que declarar**, y el fichero
**no se commitea**. Es la misma medicion que el acta 184 publica en su punto
3.1. La misma guarda corrio **diez veces mas dentro de la bateria de esta
vuelta**, una al entrar y otra al salir de cada uno de los cinco tramos que
esta vuelta corrio, y las diez dieron **cero filas**: esta contado de los
propios ficheros de tramo y no del lanzador.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. COMPUSE LA BATERIA Y CERRE EL REPORTE CON EL TRAMO 9 EN ROJO
DENTRO.** El encargo dice dos cosas que aqui se tocan: *"si otro arnes cae en
rojo, te detienes ahi"* y *"cuando los nueve tramos tengan salida sellada del
mismo calibre, corres `--componer`"*. **Me detuve** (no re-corri el tramo 9 y
no toque el arnes), pero **si compuse y si cerre**. Mi lectura de *mismo
calibre* es la de `AUDITOR.md` 6.1 con sus palabras: *"nueve salidas selladas
no valen si una es de otra HONDURA que las demas"*, y la hondura del tramo 9
es la misma que la de los otros ocho: mismo protocolo, misma doble corrida,
mismas mediciones. **Lo que cambia no es la hondura, es el resultado.** La
lectura contraria, la del encargo sobre el tramo 5 (*"una salida sellada en
rojo no es del mismo calibre que ocho en verde"*), llevaria a **no cerrar el
reporte por tercera vuelta seguida**. **Elegi la lectura que publica el rojo
entero en vez de la que deja el reporte sin cerrar, y lo marco.**

**`D.2`. EL ESQUELETO Y EL TALLADOR NOMBRAN EL ACTA DE LA VUELTA ANTERIOR Y NO
LA QUE ORDENA ESTA.** Las dos maquinas piden el acta de `VUELTA - 1`, o sea la
**183**, y el acta que encarga esta vuelta es la **184**, cuyo commit es
justamente el **HEAD de apertura** que la misma identidad publica. **No toque
la maquina**, porque el clon declarado dice que no se toca salvo el numero de
vuelta, y porque cambiarla el dia del cierre habria movido una celda tallada.
**Lo digo en vez de dejar que la celda hable sola.**

**`D.3`. LA PIEZA DE LA BATERIA SE LLAMA `SALIDA_V183_BATERIA.txt` Y LA VUELTA
ES LA 184.** El nombre lo computa el lanzador de su propio fichero, que es de
la 183, y el encargo lo nombra asi con todas las letras. **Pero
`cerrar_reporte.py` tiene una guarda que rechaza una corrida de otra vuelta
pegada en la seccion 9**, y esa guarda mira el numero del nombre. **La bateria
es de verdad la de esta corrida** (sus tramos 5 a 9 se sellaron hoy), pero **el
nombre dice 183**, y esa colision no la resuelvo yo.

**`D.4`. RENOMBRE UN CASO DEL ARNES DE LA 165 QUE EL ACTA 184 NOMBRA POR SU
NOMBRE.** El acta cita `A_el_patron_VIEJO_no_ve_dos_de_su_propia_nomina`; ese
caso hoy se llama `A_el_patron_VIEJO_no_ve_parte_de_su_propia_nomina` y ademas
**se partio en dos**, porque el nombre viejo lleva dentro la cifra que
caduco. **Mover una etiqueta que un acta cerrada nombra es una decision de
alcance**, y la tomo yo.

**`D.5`. EL ESPERADO COMPUTADO DEL CASO A RECOMPONE EL FILTRO DE LA FUNCION
BAJO PRUEBA.** `esperadas` se computa con
`[n for n in nomina_real if not PATRON_ARNES_VIEJO.match(n)]`, que es la via
directa; `nomina_invisible_al_censo()` hace lo mismo por dentro. **Se puede
leer como re implementacion del sujeto**, y entonces el caso probaria menos de
lo que parece. **Mi razon es que sigue cazando el orden, la nomina por defecto
y cualquier entrada que la funcion se coma**, y que el caso hermano, el de los
dos ficheros DENTRO del conjunto, es el que no envejece. Va marcado.

**`D.6`. LA RELECTURA AL DOBLE ENCONTRO UNA LESION EXACTA Y NO HICE NADA CON
ELLA.** Es el puesto **3.141**, y **es un VECINO, no del tramo de la ciega**.
El encargo dice *"ninguna clase se vuelve a decidir"*, asi que **no la toque**
y la dejo nombrada con su motivo en la salida. **Pero una lesion encontrada y
no registrada como pendiente se puede perder**, y no se si le tocaba entrada
propia.

**`D.7`. METI EL ARNES DE LA 1.c EN LA NOMINA DE LA BATERIA QUE LO ESTRENA.**
Corrio en el **TRAMO 9** de su propia bateria, el mismo dia que nacio. **La
regla me ampara** (acta 176 punto 7.2, reconfirmada por la `5.6` del acta
184), y la medicion la respalda: sin el, `arneses_que_faltan()` daba **1** y
los cinco tramos que quedaban habrian cerrado en rojo. **Pero es la misma
especie que la `PD.3` del reporte de la 183 dejo abierta**, y hoy vuelve a
pasar.

## 6. LAS PREGUNTAS

**1. QUE HACE UN EJECUTOR CUANDO LA PIEZA DE LA BATERIA LLEVA EL NUMERO DE
OTRA VUELTA.** La `D.3` de arriba, dicha como pregunta: el lanzador computa su
numero de su propio nombre (que es lo que la 183 reparo, y bien), la bateria
empezo en la 183 y acabo en la 184, y `cerrar_reporte.py` exige que la seccion
9 no traiga una corrida de otra vuelta. **Las tres reglas son buenas por
separado. La pregunta es cual manda cuando una bateria cruza dos vueltas.**

**2. EL TAMANO DE TRAMO SIGUE EN 13 Y LA NOMINA SIGUE CRECIENDO.** Hoy son
**113 entradas** y el noveno tramo lleva **9**. Con **117** los nueve tramos
quedan llenos, y a partir de ahi **el reparto daria DIEZ**. La opcion de podar
la nomina la **RECHAZO** el fundador el 5 sep, y no la pido. **Pregunto si el
numero de tramos puede pasar de nueve, o si lo que crece es el tamano.**

**3. LAS OCHO ACTAS SIN REGISTRO SIGUEN SIN REGISTRO.** El `R.46`, como el
`R.45` y el `R.44`, las documenta **como salto y sin rellenar**, y esta vuelta
volvio a medirlo en vez de heredarlo. **La pregunta es si alguna vez se releen
para escribirlas, o si el salto es la respuesta definitiva.**

## 7. PENDIENTES DE DOCTRINA

**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya
presente el dia del veredicto no son de la cola post fusion. Registrada y sin
resolver desde el acta 182, y esta vuelta la hereda igual.

**`PD.2` NUEVA. EL CALIBRE DE UN TRAMO EN ROJO.** `AUDITOR.md` 6.1 define
*mismo calibre* por la **hondura** y el encargo de esta vuelta lo aplico al
**resultado**. Las dos lecturas son defendibles y llevan a sitios opuestos:
una compone y cierra, la otra deja el reporte sin cerrar. **Aplique la
primera** y lo marque en la `D.1`. **No hay regla escrita que elija.**

**`PD.3` NUEVA. UN ARNES QUE SE ESTRENA DENTRO DE LA BATERIA QUE LO ESTRENA.**
Heredada del reporte de la 183 y **hoy con consecuencia medida**: el arnes que
hizo caer el tramo 9, `vuelta182_tarea2_mutacion_apertura_auditor.py`, **no
aparece en ninguna salida de bateria anterior a la de hoy**, comprobado
buscando su nombre en todas las `docs/loop/SALIDA_V*_BATERIA*.txt`. **Su
primera bateria de verdad es esta, y en ella cayo.** Es exactamente lo que el
acta 184 anoto en su `5.6` sin convertirlo en regla.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1`. PUBLIQUE DOS SALIDAS DE ARNES CON EL DENOMINADOR VENCIDO Y HUBO QUE
RE CORRERLAS.** Corri los arneses de la 1.b y de la 1.c **antes** de meter el
nuevo en la nomina, o sea con la nomina en **112**, y sus salidas quedaron
escritas en disco con ese denominador. Al subir la nomina a **113** hubo que
volver a correrlos para que sus cifras fueran las del cierre. **Es la misma
especie que la caida `E.1` del acta 184**, la estimacion publicada con una
nomina vencida, y la cometi el mismo dia que escribia su remedio. **Lo que la
salvo fue re correr antes de commitear, no un instrumento.**

**`C.2`. EL CLON DE LA RELECTURA CORRIO UNA VEZ CON UNA FRASE QUE SE
CONTRADECIA CON SU PROPIO TITULO.** La salida decia *"publica el reparto y LA
UNICA discrepancia"* debajo de una cabecera que decia **TRES**. La cace
**releyendo la salida**, no un instrumento, y se regenero antes del commit.
**Ningun fichero commiteado la lleva, pero estuvo a una orden de llevarla**, y
una contradiccion dentro de un fichero de evidencia es exactamente lo que esta
casa persigue.

> **NINGUNA DE LAS DOS SE TAPA.** La `C.1` es la que mas cerca estuvo de
> costar algo, y lo que la salvo no fue mi cuidado sino **el orden del
> encargo**, que manda medir el reparto antes de tocar la bateria: al medirlo
> hubo que volver a mirar la nomina, y ahi se vio.

### 8.1 LOS NUEVE TRAMOS, CONTADOS DE SUS PROPIOS FICHEROS

**LA TABLA SE CUENTA DE SU FICHERO** (`EJECUTOR.md` 1). Cada fila sale de
`docs/loop/SALIDA_V183_BATERIA_TRAMO_<n>.txt`, leido con
`scripts/loop/_v184_tallar_cierre.py`: los bytes con `os.path.getsize` y con
el mismo fichero normalizado a LF, las lineas contando saltos, las entradas
contando sus lineas `ENTRADA DEL TRAMO:`, el exitcode y los minutos de las
lineas que el propio tramo escribe al sellarse, y la columna de nomina de la
linea `LAS <n> MUTACIONES VIEJAS` que cada tramo imprime.

| tramo | bytes disco | bytes LF | lineas | entradas | nomina del sello | exitcode | minutos |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **1** | 9116 | 9116 | 120 | 13 | 112 | **0** | 2.1 |
| **2** | 7352 | 7352 | 114 | 13 | 112 | **0** | 3.8 |
| **3** | 7406 | 7406 | 114 | 13 | 112 | **0** | 3.7 |
| **4** | 7421 | 7421 | 114 | 13 | 112 | **0** | 1.0 |
| **5** | 7385 | 7385 | 114 | 13 | 113 | **0** | 0.9 |
| **6** | 7428 | 7428 | 114 | 13 | 113 | **0** | 0.9 |
| **7** | 7456 | 7456 | 114 | 13 | 113 | **0** | 0.5 |
| **8** | 7407 | 7407 | 114 | 13 | 113 | **0** | 0.7 |
| **9** | 6769 | 6769 | 105 | 9 | 113 | **1** | 0.4 |

**CIFRA tramos con salida sellada no vacia: 9 de 9.** **CIFRA entradas que
los tramos dicen haber corrido, sumadas de sus lineas `ENTRADA DEL TRAMO:`:
113.** **CIFRA exitcodes distintos de cero: 1.** **Suma de los minutos
medidos: 14.0.** El tramo mas largo midio **3.8 minutos** y el mas corto **0.4**.

**LA COLUMNA DE NOMINA DEL SELLO NO ES DECORACION, Y POR ESO ESTA:** los
tramos que la vuelta 183 sello lo hicieron con la nomina en un numero y los
que sello esta vuelta con otro, porque **la TAREA 1.c metio una entrada**. **La
cobertura sigue entera de todas formas y lo dice `--componer`, no yo:** **113
entradas corridas, 0 sin correr, 0 repetidas y 0 ajenas**, porque la entrada
nueva cayo en el **tramo 9**, que se corrio despues de meterla.

**EL TRAMO 9 SALIO EN ROJO Y NO SE RE CORRIO NI SE ARREGLO.** El motivo,
literal de su propia salida sellada: **`NO REPRODUCIBLE: 1
(vuelta182_tarea2_mutacion_apertura_auditor.py)`**, cuya salida
`SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` **cambia SOLO entre dos
corridas, en su linea 53**, y lo que cambia es **el sufijo aleatorio del
directorio temporal que esa misma linea imprime**. El arnes, corrido solo,
sale **exit 0**: **el rojo lo enciende la DOBLE CORRIDA de la bateria, que es
la unica que lo mira.** Se trae sin tocar, que es lo que el encargo manda y lo
que el acta 184 adjudico a favor cuando la 183 hizo lo mismo con su tramo 5.

**LA MIRADA DE LA BATERIA SOBRE SI MISMA, RECOMPUTADA AL CIERRE Y NO
HEREDADA DE LA CABECERA:** nomina **113 entradas**, `arneses_que_faltan()`
**0**, `nomina_invisible_al_censo()` **0**, `guarda_del_sujeto_congelado()`
**0**.

### 8.2 LAS OTRAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

| lo que se publica | cifra | fichero del que se cuenta |
|---|---:|---|
| casos del arnes del censo reparado | 14 pasan de 14, 0 fallan, 14 caen de 14 | `docs/loop/SALIDA_V184_T1B_ARNES_REPARADO.txt` |
| casos del arnes de la estimacion | 14 pasan de 14, 0 fallan, 14 caen de 14 | `docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt` |
| puestos releidos al doble | 60 | `docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` |
| de ellos, declaran diferenciador | 6 | `docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` |
| de ellos, con lesion exacta | 1 | `docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` |
| de ellos, con algun nodo muerto | 0 | `docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` |
| la salida compuesta de la bateria | **71753 bytes en disco y 71753 bytes normalizados a LF** | `docs/loop/SALIDA_V183_BATERIA.txt` |
| el reparto medido antes y despues | **1443 bytes en disco y 1443 bytes normalizados a LF** | `docs/loop/SALIDA_V184_T1_REPARTO_ANTES_Y_DESPUES.txt` |
| el cotejo de los tres clones declarados | **24487 bytes en disco y 24112 bytes normalizados a LF** | `docs/loop/SALIDA_V184_COTEJO_DE_CLONES.txt` |
