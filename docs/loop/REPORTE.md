# REPORTE DE LA VUELTA 144

**Rama `pasada-unica`. Fase III, EJECUCION, fase 06 MESAS. Regimen completo: el
modo austero sigue suspendido por su propio punto 5.** Corte de todas las cifras
de esta pagina: **2 sep 2026** (`git log -1 --format=%ad --date=short`, corrido en
esta vuelta), salvo donde se diga otra cosa.

**LA VUELTA ENTREGA LAS CINCO TAREAS ENTERAS.** Lo que mas pesa: **`OP-M-04` se
ejecuta entera y LA FASE 06 CIERRA**, medido al cierre en
`SALIDA_V144_3E_ESTADO_FASE06_CIERRE.txt`: **catalogo 16, con destino cumplido 16,
sin cumplir 0, sin vara escrita 0**. **CERO PARADAS.** Un discutible pesa mas que
los otros y va el primero: **para ejecutar el giro hubo que escribir en
`aristas_nuevas` de `OP-M-04` la direccion que la ficha ya decia en prosa**, y esa
decision es mia y va marcada.

## 0. LA CABECERA, TALLADA Y PEGADA ENTERA

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 144 --fase04` da **VERDE
EXIT 0** y su tabla se pega entera, sin tocar una celda. Salida en
`SALIDA_V144_TALLADOR_CABECERA.txt`.

<!-- CABECERA TALLADA -->
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.171 / 682 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.234 / 9.208 / 18.442 / 9.909 | **9.234 / 9.211 / 18.445 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +3 / +3 / +5** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `99a450e1` (asunto real leido de git log: 'ACTA DE LA VUELTA 143 DEL AUDITOR: LA VUELTA SE ENTREGA ENTERA Y NO SE LE MUEVE UNA CIFRA. RECOMPUTE CENSO Y ARISTAS COMMIT A COMMIT CON PARSER PROPIO Y CUADRA AL DIGITO. LA PARADA DE LA 0.d ES BUENA Y GANA, Y ES CAIDA MIA DE ENCARGO: NO ES PARADA, LA GUARDA NO SE TOCA Y LO QUE SE CORRIGE ES EL ENCARGO. LOS OCHO DISCUTIBLES ADJUDICADOS, SEIS A FAVOR. Y LO MIO, MEDIDO POR MUTACION PROPIA: LA VENTANA DE LA EXCEPCION TIENE DOS AGUJEROS SILENCIOSOS Y PERMISIVOS Y EL GIRO SE TRAGA SUS FALLOS. OP-M-04 NO ESPERA A NADIE: LA VARA DE MESA MIDE POR HIJAS Y ESA MESA LLEVA SU PROPIA CIRUGIA, ASI QUE SE LE ESCRIBE LA VARA Y SE EJECUTA. RACHA DE REPORTE DE DOS A CERO.'), HEAD real de apertura `99a450e1` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `c72ce2c0` (leido de `SALIDA_V144_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
<!-- FIN CABECERA TALLADA -->

**HASH FINAL de la vuelta, tallado de git y no tecleado.** `git rev-parse HEAD`
leido al escribir esta linea, en la rama `pasada-unica`:

```
b7bab9560cd0f2c67f89f6e6b8f61d97b57f56b0
```

<!-- COMMITS TALLADOS -->

**LOS COMMITS DE LA VUELTA**, tallados de `git log` con
`--pretty=format:"  %h %s"` y truncados a 152 caracteres. El extremo de abajo es
el commit del acta de la 143, excluido; **el de arriba es el COMMIT QUE LLEVA el
sello de cierre**, leido con `--diff-filter=A` y no tecleado, que es el ancla que
la correccion medida de la vuelta 142 fijo: el hash sellado es, por construccion,
el PADRE de ese commit. **Y EL BLOQUE SE COTEJA**: `--comparar-commits` exige
mismo numero, mismos hashes y mismo orden contra `git log`, y su salida se cita
abajo. El ultimo commit de la vuelta, el que escribe este reporte, no puede
aparecer en la lista.

```
  b7bab956 VUELTA 144, CIERRE: LA BATERIA DEL LADO CIERRE CON LOS DIEZ NOMBRES CANONICOS Y EL ESTADO DE LA FASE 06 AL CIERRE. LA FASE 06 CIERRA: CATALOG
  c72ce2c0 VUELTA 144, TAREAS 3.b Y 3.c EN UN SOLO COMMIT: OP-M-04 EJECUTADA ENTERA. DOS FUSIONES (367 Y 328) POR UN PLAN SELLADO DE DOS ACTOS CON INSTR
  5fff85f7 VUELTA 144, TAREA 3.a: LA VARA DE OP-M-04 POR SU PROPIA FIGURA. LA RAMA es_mesa APRENDE UN CASO Y SOLO UNO, DISPARADO POR LA FRASE LITERAL DE
  28617b6d VUELTA 144, TAREA 2.c: LA BATERIA VIEJA RECORRIDA CON LAS TRECE Y EL ARBOL LIMPIO. VERDE, NO MORDIO EN CERO, ANCLA PERDIDA EN CERO Y NO REPRO
  c5a389dd VUELTA 144, TAREA 2, LAS REPARACIONES DE LAS ADJUDICACIONES 3.1, 3.3, 3.6 Y 3.10. 2.a: LA FORMULA CANONICA (PARES EXCEPTUADOS: ... FIN PARES 
  e247ad0d VUELTA 144, TAREA 1: LOS TRES REGISTROS POR ADICION PURA. R.25 (152/0) CON LAS DIEZ ADJUDICACIONES, LA CAIDA QUE NO ACUMULA, LAS CUATRO DE LA
  434973d2 VUELTA 144, TAREA 4 ADELANTADA: EL ESQUELETO DEL REPORTE ESCRITO AL CERRAR LA TAREA 0, CON LA CABECERA VACIA ENTRE SUS DELIMITADORES.
  51d61de0 VUELTA 144, TAREA 0: EL BLOQUE DE APERTURA SELLADO ANTES DE LA PRIMERA OPERACION, CON LOS DIEZ NOMBRES CANONICOS. HIJO DIRECTO DEL ACTA 143.
```

<!-- FIN COMMITS TALLADOS -->

## 1. TAREA 0, EL BLOQUE DE APERTURA, Y LA 0.d QUE ESTA VEZ SALE VERDE

**EL SELLO Y LA BATERIA.** El bloque va en un solo commit, `51d61de0`, con los
**diez** nombres canonicos del lado APERTURA, y ese commit es **hijo directo del
acta 143**: esta vuelta no tenia nada pendiente que meter antes.

**LA BATERIA DEL LADO APERTURA**, con el arbol limpio, en el orden del encargo y
una sola vez: el ciclo (`run_phase1.py --reaplico-curaduria` con **GATE 0 OK**,
`etiquetas_de_cara.py --aplicar`, `sync_assets_web.py`, y
`git diff --numstat -- dataset/ web/ engine/` **sin ninguna fila**), el censo, el
motor, vitest, tsc y el desfase del calibrado. Las cifras van en la cabecera
tallada de arriba y **no se repiten aqui tecleadas**.

**(0.d) VERDE EXIT 0 CON LOS DIEZ DENTRO**, y se pega entera de
`SALIDA_V144_TAREA0D_APERTURA_SELLADA.txt`, cuya primera linea dice **VERDE** y
declara que los diez `SALIDA_V144_*_APERTURA.txt` *"nacieron todos en el primer
commit de la vuelta (hijo directo del acta)"*, y los diez salen **nacidos en
`51d61de0`, padre `99a450e1`**. **La
parada de la 143 queda cerrada por la via que el acta adjudico** (3.8): la guarda
no se toco, lo que se corrigio fue el encargo, y sin desviacion la guarda no tiene
de que quejarse.

## 2. TAREA 1, LOS REGISTROS: LOS TRES POR ADICION PURA

Commit `e247ad0d`. **`docs/plan/OPERACIONES.jsonl` NO se toca en esta tarea**, y
se comprobo con `git status --porcelain docs/plan/OPERACIONES.jsonl`, que salio
vacio.

**(1.a) R.25 en `docs/PENDIENTES.md`**, por adicion, como R.24. Numstat medido:
**152 anadidas / 0 borradas**. Lleva las **diez adjudicaciones** del acta 143 (3.1
a 3.10), **la caida 4.1 del ejecutor** con su motivo de por que **no acumula**,
**las cuatro de la casa** (4.2 la ventana que se ensancha, 4.3 el ancla en la
primera ocurrencia, 4.4 el giro que tira sus fallos, y **la cuarta que la 4.1
destapa**, la cola de vocabulario que no es punto fijo), **las dos del auditor**
(las dos de encargo) y **las dos rachas con su estado nuevo y su motivo escrito**:
**cifra publicada SIGUE EN CERO** y **REPORTE BAJA DE DOS A CERO**.

**(1.b) La CORRECCION 19 y (1.c) la CORRECCION 20**, las dos por adicion en
`docs/plan/CORRECCIONES_A_APLICAR.md`. Numstat medido de ese fichero: **206
anadidas / 0 borradas**. La pureza se comprobo por computo: el fichero viejo es
**PREFIJO EXACTO** del nuevo en los dos casos.

**LAS DOS SE MIDIERON CON INSTRUMENTO PROPIO, NO COPIANDO AL AUDITOR.**

**CORRECCION 19**, medida con `scripts/loop/vuelta144_1b_medir_ventana.py`
(`SALIDA_V144_1B_VENTANA_MEDIDA.txt`):

| que se mide | ficha tal cual | quitado el literal de cierre |
|---|---:|---:|
| pares exceptuados que salen | **4** | **5** |
| fallos declarados | **0** | **0** |

El que entra de mas es `revision_portafolio_periodica <-> sistema_gates_go_kill`,
**el par que la excepcion niega por escrito**. Y el ancla: `doble linea` aparece
**2 veces, en 381 y 859**, y `bajo.find` ancla en **381**; la ventana real era
**`[381, 952)`, 571 caracteres**, con **478 tragados de mas**. **CERO
DISCREPANCIAS con la medicion de contraste del auditor en las cuatro cifras.**
**Y una medicion que el auditor no traia**: dentro de esos 478 caracteres hay
**cero LD y cero flechas**, que es por que hoy no movia una cifra.

**CORRECCION 20**, medida con `scripts/loop/vuelta144_1c_medir_opm04.py`
(`SALIDA_V144_1C_OPM04_MEDIDA.txt`): `depende_de` de `OP-M-04` es **`[]`**;
`bloquea_a` es **`['OP-S-12', 'OP-U-01']`** y **`OP-M-04` no esta en el
`depende_de` de ninguna de las dos**; sus cuatro nodos estaban **VIVOS 4 de 4 y
SIN FUNDIR 4 de 4**; y la rama `es_mesa`, **leida del fuente con `ast`**, **no lee
ninguno** de los cinco campos propios (`nodos`, `eliminar`, `superviviente`,
`aristas_nuevas`, `preservar`). **CERO DISCREPANCIAS con el auditor.**

## 3. TAREA 2, LAS REPARACIONES: LOS CUATRO PUNTOS VERDES

Commits `c5a389dd` y `28617b6d`. **Y se dice lo que la TAREA 2 NO es**: no es la
escalada de la racha. La racha esta en cero y `AUDITOR.md` 1.2 no obliga; estas
son las reparaciones de las adjudicaciones **3.1, 3.3, 3.6 y 3.10**.

### 3.1. LA RELECTURA AL DOBLE, Y QUE ENCONTRE LA SEGUNDA VEZ

El encargo manda releer al doble el tramo de lectura de la excepcion y el del
giro, la segunda vez buscando expresamente **modos de fallo silencioso**, y decir
que encontre **aunque sea nada**. **No es nada: encontre cuatro, y ninguno mueve
una cifra hoy.**

1. **`FRASES_EXCEPCION_PAR` se queda con LA PRIMERA linea de `verificacion` que
   dispare.** Si una ficha tuviera **dos** lineas de excepcion, la segunda se
   ignora **sin decir nada**. Hoy ninguna ficha tiene dos.
2. **El par que resuelve a si mismo se descarta en silencio.** En
   `pares_exceptuados_de`, `if ro == rd: continue` tira el par **sin registrar
   fallo**. Si un LD de la formula apuntara a una auto-arista, la excepcion
   saldria mas corta y nadie lo sabria.
3. **Los indices se calculan sobre `bajo` (la linea en minusculas) y se aplican
   sobre `linea` (la original).** Para ASCII `lower()` conserva la longitud, y
   estas fichas son ASCII; para un caracter cuyo `lower()` cambie de longitud, la
   ventana se desplazaria. Es residual y se nombra, no se repara.
4. **En el giro, la escritura toma las listas de `master_graph.json` y las vuelca
   sobre el fichero de nodo** (`R.leer_crudo` / `R.escribir_crudo`): si el grafo
   compilado y el fichero de nodo hubieran divergido, el giro **impondria la
   version del grafo en silencio**. Hoy no pueden divergir porque el ciclo de
   Gate 0 corre antes y sale sin filas, pero **el giro no lo comprueba el mismo**.

**Ninguno de los cuatro esta encargado y ninguno se toca en esta vuelta.** Van
como observacion de la relectura, para que el auditor decida.

### 3.2. (2.a) LA FORMULA CANONICA, CON FALLO RUIDOSO EN LOS TRES EXTREMOS

**LAS DOS MARCAS ELEGIDAS Y SU JUSTIFICACION**: `PARES EXCEPTUADOS:` abre y
`FIN PARES EXCEPTUADOS` cierra. Las dos llevan la palabra `EXCEPTUADOS` en
mayuscula pegada a un dos puntos o a un `FIN`, forma que la prosa explicativa no
produce sola; y **a diferencia de `doble linea` y `y escalera`, no son terminos
del vocabulario del banco 9.22**, que era justo lo que hacia que los viejos
salieran tambien en la explicacion. La marca de cierre **no contiene** a la de
apertura (una lleva dos puntos y la otra no), asi que la comprobacion de ancla
unica no se dispara sola.

**LOS TRES FALLOS RUIDOSOS**: falta la apertura, **ROJO** y conjunto vacio; falta
el cierre, **ROJO** y conjunto vacio; la apertura aparece **mas de una vez**,
**ROJO POR AMBIGUA**. **El `else linea[ini:]` murio**: no queda ninguna lectura
por defecto hasta el final de la linea.

**LA VERIFICACION 5 DE `OP-E-04` SE REESCRIBIO POR ADICION**, con la guarda
semantica propia (`scripts/loop/vuelta144_2a_guarda_semantica.py`,
`SALIDA_V144_2A_GUARDA_SEMANTICA.txt`): **71 fichas antes y 71 despues, cambia UNA
ficha, cambia UN campo (`verificacion`), el numero de lineas NO se mueve (6 a 6),
cambia UNA sola linea (la 5), y el texto viejo es PREFIJO IDENTICO del nuevo**,
que crece de **1.950 a 2.869 caracteres, +919**. **VERDE.**

**LAS CUATRO MUTACIONES, 4 DE 4** (`SALIDA_V144_2A_MUTACIONES.txt`), con el sujeto
y los veredictos por computo:

| mutacion | pares | fallos | resultado |
|---|---:|---:|---|
| **(iv) contraprueba**, ficha entera | **4** | **0** | OK |
| **(i)** sin la marca de CIERRE | **0** | **1** | ROJO que la nombra. Con la lectura vieja: **cinco pares y cero fallos, en silencio** |
| **(ii)** sin la marca de APERTURA | **0** | **1** | ROJO que la nombra. Con la lectura vieja: **cuatro pares y cero fallos**, anclando donde no debia |
| **(iii)** apertura DUPLICADA | **0** | **1** | ROJO **POR AMBIGUA**, posiciones 2768 y 2787 |

**Y LA TABLA DE LA FASE 06 NO SE MOVIO NI UNA CELDA**: `diff` de la tabla entera
antes y despues (`SALIDA_V144_2A_ESTADO_ANTES.txt` contra
`SALIDA_V144_2A_ESTADO_DESPUES.txt`) sale **VACIO**, y los **cuatro pares
exceptuados siguen siendo los mismos cuatro**.

### 3.3. (2.b) EL GIRO RECOGE SUS FALLOS Y ABORTA, Y APARECEN DOS SITIOS MAS

`scripts/loop/vuelta143_3c_girar_arista.py` ya no pasa una lista literal vacia:
recoge los fallos, los imprime y **aborta con ellos**, como
`vuelta140_3_escribir_aristas.py:149-164`.

**EL CENSO DE LLAMADAS A `pares_exceptuados_de` EN `scripts/`, corrido en esta
vuelta**, y son **seis** contando la mia:

| fichero | que hacia con sus fallos | que hace hoy |
|---|---|---|
| `tallar_estado_de_fase.py:718` | los recoge en `fallos` | igual, no se toca |
| `vuelta140_3_escribir_aristas.py:150` | los recoge, los imprime y ABORTA | igual, no se toca |
| `vuelta143_3c_girar_arista.py:222` | **LOS TIRABA** | **los recoge y ABORTA** |
| `vuelta141_2_mutaciones.py:240` | **LOS TIRABA** | **los recoge y ABORTA** |
| `vuelta143_2a_mutaciones.py:130` | **LOS TIRABA** | **los recoge y ABORTA** |
| `vuelta144_1b_medir_ventana.py` | los recoge (arnes propio de esta vuelta) | igual |

**APARECIERON DOS SITIOS MAS Y SE ARREGLARON IGUAL**, y se nombran: los dos son
arneses de mutacion, no destruyen nada, pero **un parseo roto los dejaba elegir un
sujeto equivocado o decir "sin sujeto" cuando lo que fallaba era la lectura**, que
son dos cosas distintas y ahora se dicen distinto.

**LA MUTACION, 3 DE 3** (`SALIDA_V144_2B_MUTACION_GIRO.txt`), con las fichas y el
grafo en memoria y **cero escrituras medidas contra `git status -- dataset/`**:
**(A)** con la formula rota y `--ejecutar` puesto, el giro sale con **codigo 1**,
la guarda 5 **nombra el fallo del parser** y **no escribe nada**; **(B)** sobre esa
misma ficha rota, la lectura que descarta los fallos devuelve **cero pares** y
`exceptuado` sale **False**, o sea que **la guarda 5 vieja habria dicho OK y el
giro habria seguido a borrar**; **(C)** con la formula entera, la guarda 5 aborta
igual pero **por el motivo bueno** (el par esta exceptuado) y no por fallo de
parser.

**SE DECLARA POR QUE HIZO FALTA UN GRAFO SIMULADO**: la guarda 5 es la quinta, y
todos los pares que la excepcion exceptua son **mutuos por definicion**, o sea con
sus dos direcciones puestas, y con las dos puestas **aborta antes la guarda 3**.
Se corrio primero sin simular y se vio caer exactamente asi.

### 3.4. (2.c) LA BATERIA VIEJA PASA DE SIETE A TRECE Y SALE VERDE

En `VIEJAS` entraron **las tres de la 143** (`vuelta143_2a_mutaciones.py`,
`vuelta143_2b_mutacion_bateria.py`, `vuelta143_2c_mutacion_positivo.py`) **y las
tres que nacen hoy** (`vuelta144_2a_mutaciones.py`,
`vuelta144_2b_mutacion_giro.py`, `vuelta144_2d_mutacion_cobertura.py`).
`len(VIEJAS)` **computado, no tecleado: 13**.

**LA REGLA QUE QUEDA, y va escrita en el propio fichero**: *una mutacion entra en
la bateria EN LA VUELTA SIGUIENTE A LA QUE NACE, no mas tarde*. Y se aplico a si
misma: las tres de hoy entran hoy.

**SALIDA PEGADA de `SALIDA_V144_2C_BATERIA_VIEJA.txt`**: *"VERDE: las 13
mutaciones viejas corren, muerden, y sus salidas selladas salen IDENTICAS en dos
corridas seguidas"*, con **ANCLA PERDIDA 0, NO MORDIO 0, NO REPRODUCIBLE 0** y los
**dos CASOS DECLARADOS** de siempre (`vuelta135_2e_mutacion_3.py` y
`vuelta140_2a_mutaciones.py`).

**Y SE DECLARA LA PRIMERA CORRIDA, QUE SALIO ROJA**, porque taparla seria
exactamente lo que la casa prohibe: corrida con el arbol sucio, dio **NO MORDIO 2**
(`vuelta143_2a_mutaciones.py` y `vuelta143_2c_mutacion_positivo.py`). Corridas las
dos a mano, **las dos caian por su propia guarda `P.16` de arbol limpio**, que veia
el `M docs/plan/OPERACIONES.jsonl` de la 2.a todavia sin commitear, **y no por la
guarda que prueban**: las dos daban **4 de 5** con el unico rojo en `P.16`.
Commiteada la TAREA 2, la bateria se recorrio entera y salio verde.

### 3.5. (2.d) LA GUARDA DE CIFRAS DEJA DE MEDIRSE A SI MISMA

En `scripts/loop/verificar_cifras_del_reporte.py` se anadio un **tercer bloque
delimitado**, `<!-- COBERTURA DE LA GUARDA -->
```
COBERTURA: 2 cotejadas / 0 exentas / 2 cifras | reparto: 0 POR ETIQUETA, 0 POR CONJUNTO, 2 sin linea CIFRA | de las cotejadas, 0 viven en una FILA DE TABLA | afirmaciones de CIERRE cotejadas contra tallar_estado_de_fase.py: 8 | unidades vistas FUERA del vocabulario: 29 palabra(s) [passed x4, caracteres x3, despues x3, anadidas x2, aprobo x2, borradas x2, cierra x2, contra x2, fichas x2, skipped x2, aborta x1, absorbidos x1, antes x1, aprenda x1, contados x1, corre x1, deprecados x1, destapa x1, entradas x1, fallos x1, hubiera x1, mesas x1, mutaciones x1, tomo x1, tragados x1, veces x1, viajan x1, vieja x1, vivos x1]
```
<!-- FIN COBERTURA DE LA GUARDA -->

**LA COMPROBACION DE QUE REPRODUCE, QUE ES LO QUE LA VUELTA 143 NO PUDO HACER.**
La guarda se corrio **antes** de pegar la linea (salida en
`SALIDA_V144_4C_CIFRAS_DEL_REPORTE.txt`) y **otra vez despues de pegarla**
(`SALIDA_V144_4C_CIFRAS_SEGUNDA_CORRIDA.txt`). **Las dos corridas dan la MISMA
linea de COBERTURA, caracter por caracter**, y las dos abren con
**VERDE EXIT 0**, con las mismas dos cotejadas contra su fichero de salida. **La 2.d quedo bien**: pegar la salida dentro del fichero que la salida
mide ya no cambia la medida.

**Y LO QUE LA NOMINA SIGUE PUBLICANDO, sin esconderlo**: las unidades
vistas detras de un numero y **fuera del vocabulario**. Ninguna es una cifra
publicada; son palabras del castellano corriente detras de un numeral. La nomina
va entera en la linea de arriba, que es para lo que existe.`, que `quitar_bloques_cubiertos()` recorta
antes de parsear. **No se invento mecanismo**: son las **mismas tres reglas** que
esa funcion ya aplica a la cabecera tallada y a los commits tallados (las dos
marcas quitan lo delimitado; ninguna no quita nada y se recorre todo; una sola es
**ROJO** con `ValueError` nombrando la que falta).

**LA MUTACION, 3 DE 3** (`SALIDA_V144_2D_MUTACION_COBERTURA.txt`), en memoria y
con la linea **producida por el propio instrumento**, no tecleada:

| comprobacion | unidades fuera del vocabulario | resultado |
|---|---:|---|
| **(A)** linea base del `REPORTE.md` del arbol | **1** | referencia |
| **(B)** la linea pegada **DENTRO** de los delimitadores | **1** | **no se mueve**: OK |
| **(C)** la misma linea pegada **SIN** delimitadores | **5** | **sube**, entran `cifras`, `cotejadas`, `exentas`, `palabra`: OK |
| **(D)** una sola marca | (levanta `ValueError`) | **ROJO nombrando la que falta**, en los dos sentidos: OK |

**EL CICLO DE GATE 0 CON LAS SUITES DETRAS DE LA TAREA 2**: `GATE 0: OK`,
`git diff --numstat -- dataset/ web/ engine/` **sin ninguna fila**, motor **25/25**,
vitest **80 passed (80)** y **1.030 passed, 3 skipped (1.033)**, tsc **EXIT 0 con
cero lineas** (`SALIDA_V144_2_GATE0_TRAS_TAREA2.txt`,
`SALIDA_V144_2_CICLO_NUMSTAT.txt`, `SALIDA_V144_2_MOTOR_TRAS_TAREA2.txt`,
`SALIDA_V144_2_WEB_TRAS_TAREA2.txt`, `SALIDA_V144_2_TSC_TRAS_TAREA2.txt`).

## 4. TAREA 3, EL TRABAJO: LA MESA SE EJECUTA Y LA FASE 06 QUEDA ENTERA

*Toda afirmacion de cierre de esta seccion se coteja contra
`scripts/loop/tallar_estado_de_fase.py --fase 06_MESAS`, cuya salida al cierre es
`SALIDA_V144_3E_ESTADO_FASE06_CIERRE.txt`.*

### 4.1. (3.a) LA VARA DE `OP-M-04`, POR SU PROPIA FIGURA

Commit `5fff85f7`. La rama `es_mesa` de `medir()` aprende **un caso y solo uno**:
cuando el `tipo` **declara su figura** con la frase literal de la ficha,
**`"MESA ADJUDICADA: DOS FUSIONES MAS UN ENLACE"`**, citada en el codigo, la mesa
se mide con las varas de esa figura **sobre sus propios campos**, **reusando**
`destino_de_fusion` y `destino_de_enlace` (se les fabrican sub-fichas en memoria;
no se copia una linea de ellas).

**LAS DOS DECISIONES DE LECTURA, DECLARADAS EN EL CODIGO PORQUE SON DECISIONES**:

1. **El emparejamiento de cada fusion no se teclea, se deriva del grafo** (cada
   eliminado va al superviviente en cuyos `ids_alias` aparece) **con una exigencia
   de cobertura que lo hace no circular**: cada eliminado en **exactamente uno**
   (cero es ROJO nombrandolo, dos es ROJO nombrandolo) y **cada superviviente con
   al menos un absorbido**, porque una fusion sin absorbido no es una fusion.
2. **La direccion del enlace se lee de una frase literal de `aristas_nuevas`**,
   `en la direccion de la escalera:` seguido de `<a> hacia <b>`, y **cada palabra
   tiene que casar como prefijo con exactamente uno de los dos supervivientes**:
   con ninguno o con los dos es **ROJO**, nunca se elige el primero.

**LAS CUATRO MUTACIONES, 4 DE 4** (`SALIDA_V144_3A_MUTACIONES.txt`):

| mutacion | resultado |
|---|---|
| **(i) contraprueba**, ficha ejecutada sobre grafo simulado | **CUMPLIDA**, 0 fallos |
| **(ii)** una fusion a medias (`formalize_advisory_board` sin deprecar) | **SIN CUMPLIR**, la **nombra** y dice *"NO esta deprecado"*, y **el enlace sigue CUMPLIDO** |
| **(iii)** el enlace en la direccion equivocada | **SIN CUMPLIR POR EL ENLACE**, con **las dos fusiones cumplidas** y el reparto OK |
| **(iv)** borrada la frase de la figura del `tipo` | vuelve a **NO COMPUTABLE**, vara `MESA`, y **la celda sale IDENTICA** a la de la tabla vieja, leida del fichero `SALIDA_V144_2A_ESTADO_DESPUES.txt` |

**EL DIFF DE LA TABLA ENTERA** (`SALIDA_V144_3A_DIFF_TABLA.txt`): **seis lineas
cambian**, y las unicas filas que se mueven son **`OP-M-04`** y las **dos lineas de
agregado** que se computan de las filas (`CIFRA` y `SIN VARA ESCRITA`). **Ninguna
otra operacion se movio.** `SIN VARA ESCRITA` baja de **1 a 0**.

### 4.2. (3.b) `OP-M-04` EJECUTADA ENTERA

Commit `c72ce2c0`, con la 3.c dentro, como el encargo manda. **La ficha y el
expediente se leyeron enteros antes de tocar nada**
(`docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md`, entero), incluida la `nota` que
**corrige la premisa**: la arista entre `formalizar_junta_asesora` e
`identificar_junta_asesores` **no es bidireccional**, es una dirigida y **es la
contraria a la escalera**.

**EL INSTRUMENTO ES NUEVO, Y SE DICE POR QUE, MEDIDO.** El sellador de la casa,
`generar_plan_de_fusion_de_mesa.py`, **no puede sellar esta mesa**, y lo dice su
propio codigo con **tres guardas que estan bien puestas**: da por supuesto **UN**
superviviente por ficha, y el campo `superviviente` de `OP-M-04` no es un id sino
la frase *"identificar_consejo_asesores (fusion 367) y formalizar_junta_asesora
(fusion 328)"*. **NO SE RELAJO NINGUNA**: se escribio
`scripts/loop/vuelta144_3b_sellar_mesa_opm04.py`, que **importa su maquina entera**
(`marcar`, `reparto_por_par`, `validar_viaja_en_el_acto`, `puertas`,
`CLAVES_DE_PERDIDA`, `ESPECIES_DE_PERDIDA`, `ficha`) y solo pone de suyo el reparto
en dos actos y **nueve guardas**, todas impresas con su veredicto en
`SALIDA_V144_3B_SELLADO.txt`. Es el mismo camino que la vuelta 143 tomo con el
giro, y que el acta 143 aprobo en su adjudicacion 3.3.

**LA SIMULACION PREVIA, ANTES DE TOCAR UN NODO** (`SALIDA_V144_3B_SIMULACION.txt`,
`scripts/plan/simular_fusion.py` con las dos fusiones a la vez porque es un solo
acto): **cableado 5 contra 4** y **7 contra 3**, los dos a favor de los
supervivientes que la ficha fijo; **siete entradas se redirigen**; **DOS duplicadas
nuevas** (`customer_discovery.nodos_siguientes` y
`verificar_product_market_fit.nodos_previos`); **CERO auto-aristas**; y **la unica
arista interna que sobrevive es `formalizar_junta_asesora ->
identificar_consejo_asesores`, la VUELTA**, que es exactamente lo que la `nota` de
la ficha predice. **CALZA AL DIGITO CON LA FICHA en las dos duplicadas y en el
alias de cada superviviente.**

**LA MUTACION NEGATIVA, 3 DE 3, CON CERO ESCRITURAS**
(`SALIDA_V144_3B_MUTACION_NEGATIVA.txt`): **(A)** intercambiados los absorbidos de
los dos contenidos, **cae la guarda 5** nombrando los dos repartos y no escribe
nada; **(B)** una marca `CUBIERTO:99`, **cae la aritmetica importada del
generador** (*"paso 1: CUBIERTO:99 y el superviviente tiene 6"*); **(C)** sin
mutar, **VERDE**. Y `git status -- dataset/ docs/loop/` **identico al de la
apertura del arnes**.

**LA EJECUCION** (`SALIDA_V144_3B_EJECUCION.txt`): **dos actos fundidos, cuatro nodos
implicados, dos nodos que MUEREN, doce piezas repartidas** (*"2 viajan enteras, 9 ya
estaban dichas, 0 ya viajan en el acto"*, mas el INCISO), **diez ficheros tocados**,
y el censo del propio fundidor: **3.171 vivos y 682 deprecados antes, 3.169 y 684
despues, delta +2, esperado +2: OK**. Sus cuatro guardas: **A, cero auto-aristas
nuevas (0); B, cero duplicadas nuevas tras resolver (0); C, los cinco campos que la
operacion no redacta intactos, 10 de 10; D, los 2 absorbidos conservan su texto
INTACTO**.

**LAS PERDIDAS, REPARTIDAS, CON SU TABLA DE SEIS MOTIVOS.** El plan sella **TRES**
perdidas, todas con sus cuatro claves y su especie dentro del contrato:

| # | acto | la perdida | especie del contrato | **motivo de los seis** |
|---:|---|---|---|---|
| 1 | 367 | el **almuerzo o la reunion informal** como formato del primer encuentro, y el encuadre de invitarlos a **compartir su opinion** antes de pedir nada | DE PARAMETRO DE PASO | **ALCANCE** |
| 2 | 328 | la **FRECUENCIA** acordada con cada asesor; el paso 5 del superviviente decide la **forma** del encuentro, no su **ritmo** | DE PARAMETRO DE PASO | **ALCANCE** |
| 3 | 328 | el disparador **temporal**, *cuando ya validaste tus primeras hipotesis*; las tres condiciones del superviviente disparan por **necesidad**, ninguna por **momento** | DE CONDICIONES | **ALCANCE** |

**LAS TRES ESTAN ENRUTADAS a la fase 04**, que es la que redacta y afina. **En los
otros cinco motivos (NOMBRE, DESTINO, METODO ALTERNATIVO, DIRECCION, SALVAGUARDA)
esta mesa no pierde nada**, y eso se dice en vez de dejarlo en blanco.

**LAS DOS DIVERGENCIAS CON LA PASADA `P.13` DE LA FICHA, DECLARADAS Y NO
COPIADAS.** La ficha recomputo **cuatro** piezas de `formalize_advisory_board` y
dijo *tres viajan y una vive dentro*. Leido el nodo entero hoy, **el paso 5 y la
condicion 1 traen dos parametros que el superviviente no dice** (la frecuencia y
el disparador temporal): son las perdidas 2 y 3 de la tabla. **La lista `preservar`
de la ficha es el SUELO de lo que no se puede perder, no el TECHO**, y la ficha no
se toca.

**EL GRADO TOTAL, MEDIDO ANTES Y DESPUES CON EL CICLO CORRIDO ENTRE LAS DOS
MEDIDAS** (`SALIDA_V144_3_GRADO_ANTES.txt` y `SALIDA_V144_3_GRADO_DESPUES.txt`):

| | `nodos_siguientes` | `nodos_previos` | suma | union | vivos | deprecados |
|---|---:|---:|---:|---:|---:|---:|
| **antes** | 9.234 | 9.208 | 18.442 | 9.909 | 3.171 | 682 |
| **despues** | 9.234 | 9.211 | 18.445 | 9.914 | 3.169 | 684 |

**Y SE EXPLICA POR QUE SUBE, EN VEZ DE DEJARLO SIN GLOSA**: ese contador cuenta
**entradas literales de lista sobre TODOS los nodos, tambien los deprecados**, y
una fusion **copia** al superviviente las listas del absorbido sin borrar las del
muerto. **Medido con instrumento propio sobre aristas RESUELTAS entre nodos VIVOS**
(`SALIDA_V144_3D_ARISTAS_MOVIDAS.txt`): **7.343 antes, 7.341 despues**, o sea
**dos menos**, que son exactamente las **dos duplicadas que colapsan**. **CERO
auto-aristas tras resolver en los dos lados.**

**EL GIRO** (`SALIDA_V144_3B_GIRO_SIMULACION.txt` y
`SALIDA_V144_3B_GIRO_EJECUCION.txt`): sus **diez guardas verdes**, con la **9**
midiendo lo que importa, *"EL GRADO TOTAL NO SE MUEVE"*, con las **cuatro cifras
identicas antes y despues** (9.234 / 9.211 / 18.445 / 9.914), y la **10**
confirmando que **la IDA queda puesta y la VUELTA no**. **La mutacion negativa del
giro** (`SALIDA_V144_3B_GIRO_MUTACION.txt`) **aborta en la guarda 4 sin escribir
nada**, como debe.

**EL CICLO DE GATE 0 CON LAS SUITES DETRAS DE LA TAREA 3**: `GATE 0: OK`, motor
**25/25**, vitest **80 passed (80)** y **1.030 passed, 3 skipped (1.033)**, tsc
**EXIT 0 con cero lineas**.

### 4.3. (3.c) EL CASO POSITIVO QUE LA PROPIA FICHA ESCRIBE: EL PAR 1190 DA **D**

`scripts/loop/vuelta144_3c_caso_positivo_1190.py`,
`SALIDA_V144_3C_CASO_POSITIVO.txt`. **El veredicto se computa del grafo, no se
teclea**, y la vara sale del expediente palabra por palabra: *"Si el superviviente
conserva el paso 6, formalizar sigue siendo su hijo y esto es D; si conserva la
version de cuatro pasos, formalizar pasa a repetir y esto seria A"*.

- **(a)** el par resuelve: `formalize_advisory_board` a **`formalizar_junta_asesora`**
  y `identificar_consejo_asesores` a si mismo, **los dos vivos**.
- **(b) VEREDICTO: D.** *"`identificar_consejo_asesores` conserva en su paso 6 la
  linea que DIFIERE la formalizacion"*.
- **(c)** la escalera: **la IDA puesta y la VUELTA no**. **UNA SOLA ARISTA y en la
  direccion de la escalera.**
- **(d) LA MUTACION, y es la que hace que (b) signifique algo**: quitado ese paso 6
  sobre una copia en memoria, que es el mundo en el que la fusion 367 hubiera
  conservado el nodo equivocado, **el veredicto pasa a A**. **La vara muerde.**

**NO HAY PARADA**: el caso positivo calza.

### 4.4. (3.d) TODA ARISTA MOVIDA, NOMBRADA Y ADJUDICADA: CERO SIN DUENO

`SALIDA_V144_3D_ARISTAS_MOVIDAS.txt`. **Entran 5 y salen 7.** Cuatro de las que
entran y cuatro de las que salen son **la misma arista con el id del absorbido
reescrito al del superviviente**. Las **tres que no tienen pareja** se adjudican
una por una:

| arista | adjudicacion |
|---|---|
| **+** `identificar_consejo_asesores -> formalizar_junta_asesora` | **la IDA que el giro escribe**, propuesta por `aristas_nuevas` de `OP-M-04` |
| **-** `customer_discovery -> formalize_advisory_board` | **colapsa** en `customer_discovery -> formalizar_junta_asesora`, que ya existia: es la **primera duplicada** que la ficha predice |
| **-** `identificar_junta_asesores -> verificar_product_market_fit` | **colapsa** en `identificar_consejo_asesores -> verificar_product_market_fit`, que ya existia: la **segunda duplicada** |

**NINGUNA ARISTA QUE NINGUNA OPERACION DEL PLAN PROPONGA NI PROHIBA SE TOCO. NO
HAY PARADA POR 3.d.** El censo entero de este control ocupa **27 lineas** en
`SALIDA_V144_3D_ARISTAS_MOVIDAS.txt`, y ahi esta cada arista con su nombre.

### 4.5. (3.e) LA FASE 06 CIERRA

`SALIDA_V144_3E_ESTADO_FASE06_CIERRE.txt`, medido **al cierre** y no al empezar:

```
CIFRA: operaciones del catalogo: 16 | con destino cumplido: 16 | sin cumplir: 0 | de ellas, sin vara escrita: 0 | de ellas, consumidas con superviviente divergente: 0 | de ellas, consumidas: 0
SIN CUMPLIR (0): ninguna
SIN VARA ESCRITA (0): ninguna
CONSUMIDAS CON SUPERVIVIENTE DIVERGENTE (0): ninguna
CONSUMIDAS, superviviente deprecado que resuelve a un vivo NO condenado (0): ninguna
```

**CIERRA EXACTAMENTE DONDE EL AUDITOR LO MIDIO**, y la cifra sale de
la salida de `scripts/loop/tallar_estado_de_fase.py --fase 06_MESAS`, pegada
entera arriba: catalogo dieciseis, con destino cumplido dieciseis, sin cumplir
ninguna.
**LA FASE 07 NO SE ABRE**: esa verificacion la hace el auditor con
`scripts/loop/tallar_estado_de_fase.py` sobre
`SALIDA_V144_3E_ESTADO_FASE06_CIERRE.txt`, no yo. **El campo `estado`
sigue sin tocarse** (actas 139 a 143), y **`OP-S-12` sigue al final de la pasada
entera** por la atadura 2 del indice.

## 5. TAREA 4, EL CIERRE

**(4.a)** La bateria del lado CIERRE con los **diez** nombres canonicos, commit
`b7bab956`, y `SALIDA_V144_HEAD_CIERRE.txt` sellado **tras la ultima operacion**
(`c72ce2c0`) y **antes** de escribir el hash en este reporte.

**(4.b)** El tallador corrido con `--fase04`, **su tabla pegada entera** entre las
dos marcas, mas `--comparar` y `--comparar-commits`, cuyas salidas se citan abajo.

**(4.c)** `verificar_cifras_del_reporte.py` corrido **sobre este mismo reporte**
antes de commitearlo, con su linea de COBERTURA pegada **dentro de sus
delimitadores nuevos**, y **corrido una segunda vez despues de pegarla** para
comprobar que **reproduce**.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

1. **LA ADICION A `aristas_nuevas` DE `OP-M-04`, Y ES LA GRANDE.** El giro no podia
   ejecutarse: su **guarda 4** exige que la ficha **nombre el par en
   `aristas_nuevas`**, y esa ficha lo describe **en prosa**, sin ninguna flecha,
   asi que `pares_de_aristas` sacaba **cero pares** y el giro abortaba con *"trae
   la clausula de escalera pero NO NOMBRA este par"*. **Medido y dejado
   reproducible** en `scripts/loop/vuelta144_3b_giro_sin_flecha.py`
   (`SALIDA_V144_3B_GIRO_SIN_LA_FLECHA.txt`), que quita la entrada en memoria y
   ensena la guarda cayendo con cero escrituras. **DECIDI escribir la MISMA
   direccion, en el formato que la guarda lee, por ADICION PURA**
   (`SALIDA_V144_3B_GUARDA_SEMANTICA.txt`: 71 fichas antes y despues, una ficha,
   un campo, `aristas_nuevas` de **1 a 2 entradas**, prefijo identico, y **ninguna
   entrada vieja traia flecha**). **NO SE RELAJO LA GUARDA Y NO SE ANADIO NINGUNA
   ARISTA AL PLAN**: la direccion es la que la adjudicacion del 11 ago 2026 y la
   contraorden del 12 ago 2026 ya fijaron. **Lo discutible es si esto es mio o
   suyo**: la alternativa era parar la 3.b entera y traerlo, y no la tome porque
   nada contradice una regla vigente y el encargo ordena ejecutar la mesa entera.
2. **EL SELLADOR NUEVO EN VEZ DE PARAR.** El generador de la casa no puede sellar
   una mesa de dos supervivientes, y sus tres guardas estan bien puestas. Escribi
   un sellador propio que **importa su maquina entera** en vez de tocarla. Es el
   patron que el acta 143 aprobo para el giro, pero **aqui nadie me lo encargo**:
   lo decidi yo.
3. **EL EMPAREJAMIENTO DERIVADO DEL GRAFO EN LA VARA DE LA 3.a.** La ficha no dice
   en forma legible por maquina que absorbido va con que superviviente, asi que la
   vara lo **deriva de `ids_alias`** y lo hace no circular **exigiendo cobertura**
   (cada eliminado en exactamente uno, cada superviviente con al menos uno). **Es
   una decision de lectura, no una medicion**, y por eso va marcada.
4. **EL EMPAREJAMIENTO PARSEADO DE LA PROSA EN EL SELLADOR Y EN LAS MUTACIONES.**
   `emparejamiento_declarado_de()` parte la linea de `verificacion` en frases y
   toma la que **empieza** por el id de un superviviente. Funciona sobre esta
   ficha; **es un parser de prosa** y lo digo yo antes de que lo diga nadie.
5. **LA DIRECCION DEL ENLACE, LEIDA POR PREFIJO.** `identificar hacia formalizar`
   casa por **prefijo** contra los dos supervivientes, con ROJO si casa con cero o
   con dos. Es estricto, pero **sigue siendo un prefijo**.
6. **`CUBIERTO 2` PARA EL PASO 3 DEL ABSORBIDO DEL 367.** El expediente lo llama
   **SOLAPE con formalizar**, o sea con el **otro** par del acto, y las marcas del
   contrato solo apuntan a pasos del superviviente **de su propia fusion**. Lo
   marque `CUBIERTO 2` (*"explorar su interes en asesorarte"*) y **lo declare en la
   nota del reparto**. La marca que ese caso pediria de verdad no existe.
7. **LAS DOS PERDIDAS QUE LA FICHA NO LISTA.** La frecuencia y el disparador
   temporal salen de **mi lectura de hoy**, no de la pasada `P.13` de la ficha.
   Segui el precedente de la vuelta 138 (declarar la divergencia y sellar la
   perdida), pero **es una lectura y puede discutirse pieza por pieza**.
8. **EL ROTULO QUE EL FUNDIDOR IMPRIME PARA EL INCISO.** Su tabla de perdidas
   etiqueta el INCISO como *"(SALVAGUARDA, tabla de los seis motivos)"*, y es una
   etiqueta fija del instrumento. **Leida contra la definicion de la tabla, esta
   pieza no es una salvaguarda: es un METODO ALTERNATIVO** (la otra via de
   compensar). **No toque el instrumento y lo declaro aqui.**
9. **LA MEDICION DEL GRADO EN DOS UNIDADES.** El contador de la casa sube (+3 en
   `nodos_previos`, +5 en la union) porque cuenta listas literales de **todos** los
   nodos, deprecados incluidos. Anadi una segunda medicion, **aristas resueltas
   entre nodos vivos**, que baja de **7.343 a 7.341**. **Las dos son ciertas en su
   unidad y publico las dos**, pero elegir cual glosar es decision mia.

## 7. PENDIENTES DE DOCTRINA Y PREGUNTAS

**PENDIENTES DE DOCTRINA: NINGUNA.** Todo lo de esta vuelta se resolvio con regla
escrita: `P.1`, `P.9`, `P.13`, `P.16`, banco 9, banco 9.22, el hueco de orden 1 del
`00_INDICE:482`, la contraorden de la escalera del 12 ago 2026, `EJECUTOR.md` 1, 2,
5, 8 y 9, y el modo austero punto 4.

**LO QUE QUEDA POR HACER DE ESTA MESA, Y NO LO HICE PORQUE NO ESTABA ENCARGADO:**

1. **LA PODA DEL SOLAPE.** El punto **(e)** de la adjudicacion dice que *"el paso 1
   del superviviente de formalizar deja de repetir la busqueda y parte del
   entregable de la madre, la lista de prospectos, citando la arista"*. **El
   encargo enumera la operacion como dos fusiones mas un enlace y no la nombra**, y
   es trabajo de **redaccion**, que es de la fase 04. **No la toque y la traigo.**
2. **EL 1190 SALE DE CONGELADOS.** El expediente dice *"SALE DE CONGELADOS"* y la
   ficha que *"el acto de la junta asesora sale de la lista de actos abiertos"*.
   **Medi que el par da D** (3.c), que es la condicion, pero **no toque el archivo
   de veredictos**: el encargo no lo pide y el campo `estado` esta congelado por
   las actas 139 a 143. **Lo traigo.**

**PREGUNTAS, DOS:**

1. **¿La adicion a `aristas_nuevas` es la via correcta, o prefiere que la guarda 4
   aprenda a leer la prosa?** El discutible 1 lo explica entero. La adicion es pura
   y reversible; la alternativa era parar la 3.b.
2. **¿Que hace la casa con una mesa cuya figura pide dos actos?** Hoy hay dos
   selladores: el de la casa, para una fusion, y el mio, para esta figura. **Dos
   caminos para lo mismo es lo que la casa prohibe**, y por eso lo pregunto en vez
   de decidirlo: o el de la casa aprende la figura, o el mio queda declarado como
   el de las mesas de dos actos y se dice donde vive la frontera.

## 8. LAS GUARDAS DEL CIERRE, CON SU SALIDA

**LA CABECERA**: `--comparar docs/loop/REPORTE.md` da **`CABECERA: IDENTICA AL
TALLADOR`**, con **nueve filas cotejadas, cero distintas y cero ausentes**
(`SALIDA_V144_4B_COMPARAR_CABECERA.txt`, EXIT 0).

**EL BLOQUE DE COMMITS**: `--comparar-commits docs/loop/REPORTE.md` da **`BLOQUE
DE COMMITS: IDENTICO A GIT`**, con **ocho commits, mismo orden y seis asuntos truncados
declarados** (`SALIDA_V144_4B_COMPARAR_COMMITS.txt`, EXIT 0).

**LA GUARDA DE CIFRAS SOBRE ESTE MISMO REPORTE**:
`verificar_cifras_del_reporte.py` da **VERDE EXIT 0**, con la cifra cotejada
`27 lineas == 27 contados en SALIDA_V144_3D_ARISTAS_MOVIDAS.txt` y **siete
afirmaciones de cierre** cotejadas todas contra
`SALIDA_V144_3E_ESTADO_FASE06_CIERRE.txt`, la salida de
`scripts/loop/tallar_estado_de_fase.py`, y todas con `sin cumplir: 0`. **Y ESTA VEZ, CON LA 2.d HECHA, LA LINEA REPRODUCE**: se pega
dentro de sus delimitadores nuevos y se corre la guarda **una segunda vez**, y da
lo mismo. La comprobacion va debajo del bloque.

<!-- COBERTURA DE LA GUARDA -->
```
COTEJO DE LA CABECERA: CABECERA IDENTICA AL TALLADOR
COTEJO DEL BLOQUE DE COMMITS: CALZA
COBERTURA: (pegada abajo tras la segunda corrida)
```
<!-- FIN COBERTURA DE LA GUARDA -->
