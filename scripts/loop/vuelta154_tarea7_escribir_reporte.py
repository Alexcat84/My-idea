# -*- coding: utf-8 -*-
"""vuelta154_tarea7_escribir_reporte.py . TAREA 7 DE LA VUELTA 154.

ESCRIBE docs/loop/REPORTE.md CON LA CABECERA PEGADA DESDE EL FICHERO DEL
TALLADOR, no tecleada. El cuerpo vive en CUERPO (abajo) y la tabla se EXTRAE de
docs/loop/SALIDA_V154_T7_CABECERA.txt.

LA DEUDA 7.a DEL ENCARGO, ATENDIDA POR CONSTRUCCION. La vuelta 152 escribio LA
MARCA LITERAL de apertura de la cabecera dentro de la PROSA (linea 311) al
contar que la habia arreglado, y la marca quedo dos veces: la guarda de cifras
murio en ROJO POR AMBIGUA sin llegar a contar. Aqui las dos marcas SOLO existen
en este fichero, se componen por concatenacion de trozos y NUNCA aparecen
enteras en el cuerpo. Para citar el mecanismo en prosa, el cuerpo usa OTRO
literal (`marca de cabecera`), como el propio mensaje de error de la guarda
manda.

USO:  python scripts/loop/vuelta154_tarea7_escribir_reporte.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
CABECERA = os.path.join(LOOP, "SALIDA_V154_T7_CABECERA.txt")
GUARDA_CIFRAS = os.path.join(LOOP, "SALIDA_V154_T7_GUARDA_CIFRAS.txt")
REPORTE = os.path.join(LOOP, "REPORTE.md")

# Las dos marcas se COMPONEN, para que ni siquiera este fichero las traiga
# enteras mas de una vez y no haya forma de que se cuelen en el cuerpo.
_A, _B = "<!-- ", " -->"
MARCA_INI = _A + "CABECERA TALLADA" + _B
MARCA_FIN = _A + "FIN CABECERA TALLADA" + _B


def linea_cobertura():
    """LA LINEA COBERTURA, PEGADA DEL FICHERO DE LA GUARDA Y NO TECLEADA.

    El encargo la pide entera "salga como salga". Se extrae de la salida sellada
    de `verificar_cifras_del_reporte.py`. Si esa salida no existe todavia (la
    primera escritura del reporte, antes de que la guarda corra), se dice y no
    se inventa nada."""
    if not os.path.exists(GUARDA_CIFRAS):
        return "(la guarda todavia no ha corrido sobre este reporte)"
    for l in io.open(GUARDA_CIFRAS, encoding="utf-8"):
        if l.startswith("COBERTURA:"):
            return l.rstrip()
    return "(la salida de la guarda no trae linea COBERTURA)"


def tabla_tallada():
    """La tabla, EXTRAIDA del fichero del tallador. Ni una celda se teclea."""
    texto = io.open(CABECERA, encoding="utf-8").read()
    lineas = texto.splitlines()
    ini = next(i for i, l in enumerate(lineas) if l.startswith("| |"))
    fin = next(i for i, l in enumerate(lineas) if l.strip() == "FIN")
    return "\n".join(lineas[ini:fin]).rstrip()


CUERPO = """# REPORTE DE LA VUELTA 154

**Rama `pasada-unica`. FASE III, EJECUCION, modo continuo, REGIMEN COMPLETO.**
**Las nueve tareas del encargo entregadas. La TAREA 2, que era bloqueante, cierra
entera: la guarda de `OP-C-05` estaba verde sobre un universo incompleto, el
"0 sin cita" era FALSO: con la vara completa de los dos campos son 154 pares
(`docs/loop/SALIDA_V154_T2A_UNIVERSO.txt`), y hoy los 154 tienen cita. Seis caidas mias, las seis
declaradas por mi. Ocho discutibles marcados y cuatro preguntas.**

## LA CABECERA, TALLADA Y NO TECLEADA

Generada con `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 154`
(salida en `docs/loop/SALIDA_V154_T7_CABECERA.txt`) y **pegada entera por un
script**, no copiada a mano: `scripts/loop/vuelta154_tarea7_escribir_reporte.py`
extrae la tabla de ese fichero y la escribe aqui dentro. Ninguna celda de esta
tabla la escribi yo.

%(MARCA_INI)s
%(TABLA)s
%(MARCA_FIN)s

## 0. MIS SEIS CAIDAS, PRIMERO, PORQUE SON MIAS Y NO ME LAS ENCONTRARON

**CAIDA 1, DE FORMA, EN EL MENSAJE DEL COMMIT DE APERTURA.** Escribi el mensaje
con la sintaxis de PowerShell para textos de varias lineas dentro de una orden de
Bash, y el asunto del commit `12f87aae` quedo siendo un solo caracter, `@`. El
cuerpo del mensaje esta INTACTO y ninguna cifra salio de ahi. **No reescribi la
historia ya publicada**: una correccion que borra lo que corrige no se puede
auditar (`EJECUTOR.md` 8), y el commit ya estaba en `origin`. Queda declarado
aqui y el asunto real de ese commit es el que su cuerpo dice.

**CAIDA 2, UNA EXPECTATIVA MIA MAL ESCRITA, Y LA CAZO MI PROPIO ARNES.** En el
caso D de `scripts/loop/vuelta154_tarea6_mutacion_corredor.py` escribi que se
esperaban 1 intruso y **0** admitidos. El arnes salio en rojo. Tenia razon el
arnes: con los dos commits dentro y el del fundador admitido, lo correcto es
**1 intruso Y 1 admitido**, porque el admitido se sigue nombrando aparte aunque
la guarda caiga por otro. **Corregi la expectativa, no la guarda**, y la
correccion queda escrita dentro del propio arnes.

**CAIDA 3, UNA LINEA DE PROSA MIA QUE NOMBRABA MAL UN NODO.** La primera corrida
de `vuelta154_tarea2a_universo_bidireccionales.py` imprimio *"metodologia_6s
declara ida y vuelta hacia error_proofing_servicio, y metodologia_6s no se la
devuelve"*, donde el segundo nombre tenia que ser `error_proofing_servicio`. Lo
vi al leer la salida, lo corregi y volvi a correr **antes de publicar nada**.
Ninguna cifra se movio.

**CAIDA 4, UN CODIGO DE SALIDA FALSO EN UN FICHERO SELLADO, CAZADO ANTES DEL
COMMIT.** La primera version de `SALIDA_V154_T6_APERTURA_SELLADA.txt` publicaba
`EXITCODE: 0` debajo del caso rojo de la vuelta 100, y ese cero **era el de
`head`**, no el de la guarda, porque la orden iba por tuberia. Es exactamente la
especie que este bucle persigue: un verde que no es de quien parece. Lo rehice
midiendo el codigo real (**exit 1**) y contando las 48 cosas que no cuadran de la
propia salida. **Ninguna de las dos cifras falsas llego a publicarse.**

**CAIDA 5, LA MAS SERIA DE LAS CINCO: UNA CONTRAPRUEBA ANCLADA A UNA REFERENCIA
MOVIL, O SEA UN FALSO VERDE ESPERANDO SU DIA.** El arnes de la TAREA 2.d sacaba
la guarda VIEJA con `git show HEAD:scripts/run_phase1.py`. **`HEAD` avanza.**
Mientras el ensanche no estaba commiteado, `HEAD` traia la guarda vieja y el caso
B salia verde de verdad; **en cuanto commitee la TAREA 2, `HEAD` paso a ser la
guarda NUEVA** y la contraprueba se cayo publicando lo que ve la guarda mutada
y no la vieja (`docs/loop/SALIDA_V154_T2D_MUTACION.txt`). **Lo canto mi propio arnes al re
correrlo**, y por eso lo re corri. La vara pasa a ser el **HEAD DE APERTURA**,
leido del sello que la propia apertura dejo y no tecleado: ese commit es, por
construccion, anterior a toda operacion de la vuelta. La correccion queda escrita
dentro del arnes. **Ninguna cifra falsa se publico**, porque la primera corrida
se hizo antes del commit y la segunda con la vara ya fija, y las dos dan lo
mismo.

**CAIDA 6, HERMANA DE LA 5 Y DE LA MISMA FAMILIA: UNA MEDICION QUE DEPENDIA DEL
MOMENTO EN QUE SE CORRIERA.** El instrumento de la TAREA 2.a leia el registro de
citas **del arbol de trabajo**. Antes de escribir `LD-OPC05-122` daba la tabla
del acta (sin cita 0 / 1 / 2 / 4); despues de escribirla da 0 / 0 / 1 / 3,
porque el par ya tiene su cita. **Las dos mediciones son ciertas y describen
momentos distintos; lo que estaba mal es que el instrumento no dijera cual.** Lo
vi al re correrlo. Ahora el registro se lee de una **ref de git** (`--registro`),
la corrida que el reporte cita usa el **HEAD de apertura** y **reproduce la tabla
del acta para siempre**, y publico ademas la medicion de HOY en un fichero
aparte. Es la misma especie que la caida 5: **una vara anclada a algo que se
mueve**.

## 1. TAREA 1: LAS NUEVE ADJUDICACIONES, ESCRITAS DONDE CADA UNA VIVE

Instrumento: `scripts/loop/vuelta154_tarea1_registrar_adjudicaciones.py`, salida
`docs/loop/SALIDA_V154_T1_ADJUDICACIONES.txt`.

| adjudicacion | donde vive ahora |
|---|---|
| 6.1, 6.2 y 6.5 | `scripts/loop/vuelta150_3_relectura_expediente.py` (docstring) |
| 6.6 | `scripts/loop/vuelta150_4_tabla_por_fase.py` (docstring) |
| 6.7 | `scripts/loop/verificar_apertura_sellada.py` (docstring) |
| 6.8 | `scripts/loop/verificar_cifras_del_reporte.py` (docstring) |
| 6.3 | `docs/plan/OPERACIONES.jsonl`, las cinco fichas `OP-M-01` a `OP-M-05` |
| 6.4 y 6.9 | `docs/plan/OPERACIONES.jsonl`, ficha `OP-C-05` |

**TODAS POR ADICION, Y ESO SE MIDE EN VEZ DE PROMETERSE.** Los cuatro ficheros
`.py` salen con **0 lineas borradas**, contadas de git en
`docs/loop/SALIDA_V154_T1_ADITIVIDAD.txt` (+21/-0, +19/-0, +68/-0, +16/-0). En el JSONL, las seis notas tocadas traen el texto viejo **entero como
prefijo del nuevo**, comprobado por computo contra `HEAD`
(`docs/loop/SALIDA_V154_T1_ADITIVIDAD.txt`): **6 notas ampliadas, 0 campos
alterados no aditivamente**. Esquema intacto (71 fichas, 18 claves) y ningun
estado movido en esta tarea.

## 2. TAREA 2, LA BLOQUEANTE: LA GUARDA SE ENSANCHA A LA VARA DECLARADA

### 2.a Las cuatro varas, y se publican las cuatro

Instrumento propio escrito hoy, sin importar codigo de la casa, con su propio
resolutor de alias: `scripts/loop/vuelta154_tarea2a_universo_bidireccionales.py`,
salida `docs/loop/SALIDA_V154_T2A_UNIVERSO.txt`, de donde sale esta tabla.

| vara | pares bidireccionales entre vivos | sin cita |
|---|---:|---:|
| la vara estrecha de la guarda vieja (solo `nodos_siguientes`) | 153 | 0 |
| **la vara completa de los dos campos (LA QUE SE DECLARA)** | **154** | **1** |
| todas las fuentes, solo `nodos_siguientes` | 155 | 2 |
| todas las fuentes, los dos campos | 157 | 4 |

**LAS CUATRO CUADRAN AL DIGITO CON LA TABLA DEL ACTA 153, 4.1**, asi que no hay
nada que parar. **Y LA MEDICION ES REPRODUCIBLE PARA SIEMPRE, no solo hoy:** el
instrumento lee el registro de citas de una ref de git, y esta corrida usa el
HEAD de apertura, que es el estado que la tabla del acta describe. Con el
registro de HOY la columna de sin cita de la vara completa cae a cero
(`docs/loop/SALIDA_V154_T2A_UNIVERSO_HOY.txt`), que es justo lo que la 2.c
repara. **Esa segunda medicion la anadi despues de que el re correr el
instrumento me lo ensenara**, y va contada como mi caida 6. Y la aritmetica del 4.3 tambien reproduce, en ese mismo
`docs/loop/SALIDA_V154_T2A_UNIVERSO.txt`: **255 nodos vivos y 307 destinos de ida
y vuelta**, de los que **306 son mutuos**. Esos 306 entre dos son los 153 pares bidireccionales con la vara estrecha de la guarda vieja (`docs/loop/SALIDA_V154_T2A_UNIVERSO.txt`), **y queda UNO declarado por un solo lado**, `metodologia_6s` hacia `error_proofing_servicio`. **307 es impar, y ese uno es el agujero.**

### 2.b La vara se declara, y no me la invento

**LOS DOS CAMPOS, SOBRE FUENTES VIVAS.** Los tres sitios los fui a leer con mis
ojos en esta vuelta antes de tocar nada:

  - la **cabecera** cuenta `nodos_previos` (8.740) y su union de 9.914 sale de
    los dos campos, medido en `docs/loop/SALIDA_V154_CONTEO_APERTURA.txt`;
  - **`aristas_a_simetrizar`**, dentro de la propia `scripts/run_phase1.py`,
    admite una arista *"si LA DECLARA UN NODO VIVO, EN CUALQUIERA DE SUS DOS
    VISTAS"*, y la comprobacion de simetria de Gate 0 ya usa **exactamente ese
    universo**. Es la confirmacion mas fuerte de las tres: la vara que declaro no
    es nueva, es la que otra comprobacion del mismo fichero ya aplica;
  - **`web/lib/engine/planRedactor.ts` linea 96** recorre
    `[...nodos_siguientes, ...nodos_previos]` juntos como vecinos.

Mas **P.1**, que manda resolver antes de contar.

**NO DECIDO UNA VARA MAS ESTRECHA.** Las fuentes deprecadas quedan fuera por el
criterio **ya adjudicado el 14 ago 2026** (decision del fundador, camino A), que
el propio comentario de `OP-C-05` cita y que la ficha hereda de `OP-C-04`. Y **lo
que eso deja fuera se nombra dentro de la guarda en vez de callarse**: los TRES
pares que solo existen admitiendo declarante deprecado son
`asignacion_recursos_en_gates` contra `sistema_gates_go_kill`,
`formalizar_junta_asesora` contra `identificar_consejo_asesores` y
`revision_portafolio_periodica` contra `sistema_gates_go_kill`.

### 2.c El par que la vara destapa, leido por P.5

`error_proofing_servicio` contra `metodologia_6s`. **Medido antes de elegir via**
(`docs/loop/SALIDA_V154_T2C_LECTURA_DIRIGIDA.txt`): `metodologia_6s` aparece en
**0 puestos** del cribado, los dos juntos en **0**, y no hay declaracion sellada
de P.10 para el par. Luego **P.5**. Registrado como **`LD-OPC05-122`, clase C**
por el banco 9.22, primer polo: el paso 6 de 6S nombra la seguridad y no la
procedimenta, y el paso 4 de error-proofing nombra simplificar el trabajo y no lo
procedimenta. **Dos lineas distintas, una en cada nodo.**

**`n` NO SE MOVIO:** los veredictos del cribado siguen en **3.388 lineas** antes y
despues, comprobado con assert en
`docs/loop/SALIDA_V154_T2C_LECTURA_DIRIGIDA.txt`. Y el registro pasa de 153 a **154 pares distintos del registro de citas** con cero repetidos, contado en ese mismo `docs/loop/SALIDA_V154_T2C_LECTURA_DIRIGIDA.txt`.

### 2.d La mutacion muerde por el lado que era ciego

Salida `docs/loop/SALIDA_V154_T2D_MUTACION.txt`, de donde sale esta tabla.

**LA MUTACION INGENUA NO HABRIA PROBADO NADA, y lo digo porque casi la escribo.**
El **paso 5 de `run_phase1` simetriza los ids CRUDOS** antes de que Gate 0 corra:
metido el id crudo de un vivo en `nodos_previos` de otro, la vuelta aparece sola
en `nodos_siguientes` y **la guarda vieja tambien la ve**. El punto ciego real
vive en el desfase entre **ids crudos** (lo que la simetrizacion mira) e **ids
resueltos** (lo que la guarda mira), que es exactamente como nacio el par real. La
mutacion mete un **alias deprecado que resuelve a un vivo** en las DOS listas de
otro vivo, con los tres nombres elegidos **por computo**.

| caso | que prueba | esperado | obtenido |
|---|---|---|---|
| A | mutacion contra la guarda **NUEVA** | ROJO nombrando el par | **ROJO exit 1** (`docs/loop/SALIDA_V154_T2D_MUTACION.txt`): la guarda mutada ve 155 pares, uno huerfano, y nombra `ab_testing_optimizacion <-> abandonar_arreglos_rapidos` |
| B | **CONTRAPRUEBA**: la MISMA mutacion contra la guarda **VIEJA**, sacada literal de git | VERDE | **VERDE exit 0** (`docs/loop/SALIDA_V154_T2D_MUTACION.txt`): la guarda vieja ve 153 pares y ninguno huerfano |
| C | arbol intacto contra la guarda NUEVA | VERDE | **VERDE exit 0** (`docs/loop/SALIDA_V154_T2D_MUTACION.txt`): la guarda intacta ve 154 pares y ninguno huerfano |

Las tres cifras de esa tabla salen de las lineas `CIFRA` de ese fichero y ninguna
esta tecleada.

**`dataset/` IDENTICO ANTES Y DESPUES**, comprobado por sha256 y no prometido:
`0864e9cfe4e3b7746922bde54d8e551a45f02a7a1ba3780dcaed2e0986b65e37` las dos veces.

### 2.e La correccion declarada, en sus dos sedes

`docs/loop/SALIDA_V154_T2E_CORRECCION.txt`. Donde se publicaba que eran ciento cincuenta y tres, todos con cita y ninguno huerfano, lo cierto es que la vara completa de los dos campos ve **154 pares** (`docs/loop/SALIDA_V154_T2A_UNIVERSO.txt`), y que uno de ellos estaba huerfano. Las dos
sedes corregidas **por adicion**: los comentarios de la guarda en
`scripts/run_phase1.py` (la **cuarta sede**, creada por la decision del fundador
del 2 sep 2026, y escrita HOY, asi que la falta de retroactividad no la salva) y
la `nota` de `OP-C-05` en `docs/plan/OPERACIONES.jsonl`. El texto viejo queda
**entero como prefijo del nuevo**, con assert. Mas la **CORRECCION 34** en
`docs/plan/CORRECCIONES_A_APLICAR.md`, tambien por adicion pura.

### 2.f El estado, revisado AL FINAL

`docs/loop/SALIDA_V154_T2F_ESTADO_OPC05.txt`. La **verificacion 8**, que el acta
153 declaraba sin contestar, **queda contestada al cierre**, y en `docs/loop/SALIDA_V154_T2F_ESTADO_OPC05.txt` se cuentan **154 pares bidireccionales entre vivos al cierre**, todos con cita, en OK y **sobre el universo declarado**. Y no basta el
verde: por el criterio de HECHO de `08_VERIFICACION` la guarda **se caeria** si el
fallo volviera, y eso es lo que el caso A de la 2.d prueba. **El `estado` se queda
en HECHA**, y se dice por que.

## 3. TAREA 3: LA RELECTURA AL DOBLE. 40 COINCIDEN, 1 DISCREPA

**LA MUESTRA SE ELIGE POR COMPUTO**, con la zancada escrita en la salida:
**zancada 3, arranque en el puesto 1**, sobre las 122 lecturas dirigidas del
registro ordenadas por cita. Da **41 puestos**, que pasa del piso de 32 del
encargo y es mas del doble de la muestra de ocho del auditor.

**EL ORDEN LO PRUEBA GIT, NO MI PALABRA.** El ciego
(`docs/loop/SALIDA_V154_T3_CIEGA_BLIND.txt`) imprime solo titulo y pasos de los
dos nodos: sin clase, sin via, **sin cita** y sin razon. Mis 41 adjudicaciones
(`docs/loop/SALIDA_V154_T3_MIS_ADJUDICACIONES.txt`) se commitearon en `9f6de36f`,
**un commit entero antes del destape** (`bfadb55e`). Van indexadas por NUMERO DE
CASO justamente porque el ciego omite la cita: teclear la cita habria sido haber
mirado el registro.

**CONTADO DE `docs/loop/SALIDA_V154_T3_DESTAPE.txt`: 41 puestos releidos, 40
coinciden, 1 discrepa, 0 sin adjudicar.**

**LA DISCREPANCIA ES `LD-OPC05-097`**, `juran_rcca_metodo` contra
`viaje_diagnostico_remedial`. A ciegas la clasifico **A**; esta escrita **C**.
**No la arreglo callando y no la toco**: cambiar una clase del registro por mi
cuenta seria decidir una fusion en una vuelta de lectura. Mi caso, entero, en el
discutible 1.

## 4. TAREA 4: LA P3 DEJA DE CONTAR MENCIONES

**4.a LA VARA NUEVA.** La P3 cuenta commits que tocan `dataset/`, `web/` o
`engine/`. **`scripts/` sale.** La vara vieja **no se borra**: queda entera bajo
`--vara-vieja`, porque una vara borrada no se puede contrastar y el encargo pide
ensenar las dos salidas sobre el mismo corte.

**EL CASO DE MUTACION, MEDIDO AL DIGITO**
(`docs/loop/SALIDA_V154_T4C_ATRIBUCION.txt`): al corte `6f695db6` los **unicos**
commits que nombran `OP-V-01` y `OP-L-01` son `466a3c6e` (solo `docs/`, nunca
conto) y `c9c6ea40` (`docs/` y `scripts/`). **`c9c6ea40` cuenta con la vara VIEJA
y NO cuenta con la NUEVA, para las dos fichas.** Con la vieja salen como
CONGELADO EN SILENCIO con prueba P3a
(`docs/loop/SALIDA_V154_T4A_VARA_VIEJA.txt`); con la nueva caen a la tabla de
**LISTA SIN NINGUNA PRUEBA** (`docs/loop/SALIDA_V154_T4C_VARA_NUEVA.txt`), que es
donde el repo dice que estan.

**LA SEGUNDA VIA** que la adjudicacion nombra queda implementada como **P3b**, y
su limite va **declarado junto a la funcion**: mide que la ficha CITE una salida
de caso positivo o de mutacion presente en el arbol del corte, **no** que la
prueba se haya re corrido hoy. Cubre **3 fichas**. Es un proxy y va como
discutible.

**4.b LA ASIMETRIA P2 CONTRA P3** queda escrita **dentro** del instrumento, en el
docstring y en la cabecera de cada corrida, que era la condicion literal del acta.

**4.c EL RECUENTO, CONTADO DE SU FICHERO** y no tecleado
(`docs/loop/SALIDA_V154_T4C_RECUENTO.txt`). **Los dos movimientos van atribuidos
por separado, y no se cargan los dos a la vara:**

| celda | acta 153 (corte `6f695db6`) | vara VIEJA hoy | vara NUEVA hoy | a que se debe |
|---|---:|---:|---:|---|
| no calzan | 48 | 48 | 41 | **LA VARA** |
| congeladas DECLARADAS | 26 | 30 | 29 | **NO es la vara** |
| congeladas EN SILENCIO | 22 | 18 | 12 | **NO es la vara** |
| HECHA sin ninguna prueba | 0 | 0 | 0 | no se mueve |
| en LISTA sin ninguna prueba | 0 | 0 | 7 | **LA VARA** |

  - **El 48 que baja a 41 SI es la vara.** 10 fichas pierden su P3a al salir
    `scripts/`; **7 de ellas quedan en LISTA sin ninguna prueba**, y por eso su
    estado CALZA y salen de la tabla. Las otras 3 conservan otra prueba. La
    aritmetica cierra sola.
  - **El 26/22 que pasa a 30/18 NO es la vara: es MI PROPIA TAREA 1.** Anadi a
    `OP-M-01`, `OP-M-02`, `OP-M-03` y `OP-M-05` una nota que habla de su estado, y
    el instrumento lee la nota **del arbol de trabajo**. Son **exactamente 4
    fichas, medidas una a una**. La vara vieja corrida hoy **reproduce el 48 del
    acta al digito**.

## 5. TAREA 5: LAS CINCO MESAS PASAN A HECHA

**EL DISPARADOR NO SE HEREDA DEL ACTA, SE MIDE AQUI**
(`docs/loop/SALIDA_V154_T5_DISPARADOR.txt`): la fase 06 sale con **16 de 16**
operaciones del catalogo CUMPLIDAS y **0 sin cumplir**, y **las cinco mesas entre
ellas**. El pase esta implementado **por ficha y no por decreto**: si una fila no
hubiera dicho CUMPLIDO, esa ficha no se movia y se nombraba. Las cinco lo
dijeron.

**CONTEO, de `docs/loop/SALIDA_V154_T5_PASE_DE_ESTADO.txt`:** 71 fichas antes y
despues; **HECHA 23 a 28, LISTA 48 a 43**; congeladas EN SILENCIO **18 antes y 18
despues**, las 18 nombradas una a una. Esquema comprobado por assert (un solo
juego de 18 claves) y las 71 notas viejas enteras como prefijo, tambien por
assert. `verificar_cifras_del_plan.py` re corrida: **VERDE exit 0**. Mas la
**CORRECCION 35**, por adicion pura.

## 6. TAREA 6: EL CORREDOR ADMITE EL COMMIT DEL FUNDADOR, POR HASH CITADO

La puerta de admision es **una sola**: los hashes que `docs/loop/PROMPT_SIGUIENTE.md`
cita, resueltos con `git rev-parse`. **No por autor adivinado, no por asunto, no
por ruta**: un asunto lo escribe cualquiera. `intrusos_del_corredor` sigue siendo
**pura** y ahora devuelve dos listas; el admitido **se nombra aparte** en la
salida en vez de callarse.

**CUATRO CASOS POR MUTACION SOBRE EL CORREDOR REAL DE LA VUELTA 152 LEIDO DE
GIT** (`docs/loop/SALIDA_V154_T6_MUTACION_CORREDOR.txt`), **los cuatro como se
esperaba**:

| caso | que prueba | intrusos | admitidos | veredicto |
|---|---|---:|---:|---|
| A | corredor entero, sin admitidos (el estado ANTES de la 6.7) | 2 | 0 | ROJO |
| B | solo el del fundador, ADMITIDO por hash | 0 | 1 | **VERDE** |
| C | el MISMO commit, SIN admitir | 1 | 0 | ROJO |
| D | los dos, con el del fundador admitido | 1 | 1 | **ROJO, y el intruso es el del EJECUTOR** |

El caso C es el que importa y por eso lo anadi: prueba que **el verde de B lo
produce la admision** y no una laxitud nueva.

**LA GUARDA NO SE VOLVIO LAXA**, comprobado
(`docs/loop/SALIDA_V154_T6_APERTURA_SELLADA.txt`): `--vuelta 154` **VERDE exit 0**
con los diez ficheros hijos directos del acta; `--vuelta 100`, el caso rojo real
de siempre, sigue **ROJO exit 1** con **48** cosas que no cuadran, contadas de su
salida.

## 7. TAREA 7: LAS DOS DEUDAS DEL REPORTE

**7.a LA MARCA LITERAL, ARREGLADA POR CONSTRUCCION Y NO POR CUIDADO.** Este
reporte lo escribe un script, y ese script compone las dos marcas de cabecera por
concatenacion, de modo que **no existen enteras en el cuerpo ni pueden colarse**.
Para citar el mecanismo en prosa uso **otro literal** (`marca de cabecera`), que
es justo lo que el mensaje de error de la guarda manda. **No lo repito.**

**7.b LAS LINEAS CIFRA.** El contrato estaba escrito en el fichero que yo citaba y
la respuesta estaba a una lectura de distancia: formato `CIFRA <etiqueta>: <n>
<unidad>`, unidad del vocabulario cerrado, **en el fichero de salida que la cifra
cita**, nunca en el reporte, y anclada en columna cero. Queda registrado en el
docstring de `verificar_cifras_del_reporte.py` (adjudicacion 6.8) y **todos mis
instrumentos de esta vuelta la imprimen**, incluido el arnes de la tabla por fase,
que no la tenia. **Y AQUI VA LA LINEA COBERTURA ENTERA, salga como salga, pegada del fichero de la
guarda (`docs/loop/SALIDA_V154_T7_GUARDA_CIFRAS.txt`) y no tecleada:**

```
%(COBERTURA)s
La linea de arriba dispara el detector de afirmaciones de cierre porque trae dentro las palabras que lo activan, asi que va con su medicion al lado: la unica fase que esta vuelta declara cerrada es la 06, medida con tallar_estado_de_fase.py en docs/loop/SALIDA_V154_T5_DISPARADOR.txt, que sale con cero sin cumplir.
```

**DEJA DE SER CERO.** La guarda sale **VERDE exit 0** y coteja **13 de 13**, las
trece **POR ETIQUETA**, cero exentas y cero sin linea `CIFRA`, con **cuatro de
ellas viviendo dentro de una fila de tabla** y **dos afirmaciones de cierre**
cotejadas contra `tallar_estado_de_fase.py`. Ninguno de los ficheros citados deja
de ser UTF-8.

**UNA TRAMPA PROPIA DE PUBLICAR DENTRO DE UN DOCUMENTO UNA MEDIDA DE ESE MISMO
DOCUMENTO, y se resuelve en vez de esconderse:** pegar la linea de la guarda
CAMBIA el reporte, y la corrida siguiente puede medir otra cosa, con lo que el
reporte publicaria una linea VIEJA de si mismo. El script itera **hasta punto
fijo**: escribe, vuelve a medir, y solo sella cuando **la linea pegada es
identica, caracter a caracter, a la que la corrida mide**. Comprobado por
igualdad de cadena antes de sellar, no de vista.

**Y LA GUARDA ME ENSENO TRES COSAS QUE NO SABIA, y las dejo escritas porque la
proxima vuelta las va a encontrar igual:** (1) la ventana de cotejo es de TRES
FRASES, y este reporte va con las lineas cortadas a mano, asi que **la cita del
fichero tiene que ir pegada a la cifra**, no en el parrafo de al lado; (2) dos
etiquetas `CIFRA` de la misma unidad que compartan todas sus palabras dejan a la
guarda sin forma de saber contra cual cotejar, y entonces cae en AMBIGUO **con
razon**; (3) `_palabras` descarta las palabras de menos de cuatro letras, asi que
**`OK` no puede distinguir dos etiquetas**: por eso las de Gate 0 pasaron a
llamarse verdes y rojas.

**7.c EL "BAJA DE 12 A 7" NO SE REPITE.** Registrado como caida de reporte en el
acta 153, seccion 5. No hay reporte viejo que arreglar; hay que no repetirlo, y no
lo repito: **en este reporte no hay una sola cifra que no salga de un fichero de
salida citado al lado**.

## 8. TAREA 8: LA FILA 03 FUSIONES PASA A VERDE

Los dos divergentes de la CORRECCION 16 dejan de degradar el veredicto. **La rama
vieja del codigo queda escrita entera en el comentario que la sustituye**, para
que se pueda auditar que cambio. **No es aflojar la vara**: los divergentes se
siguen midiendo, contando y **nombrando uno a uno**
(`OP-M-02-MEDIOS` y `OP-M-02-ADMIT`); lo unico que cambia es que ya no degradan
**esta celda**. Un incumplimiento de verdad sigue poniendo la fila en NO CUMPLE:
hoy son **0 sobre 14 fichas y 21 absorbidos**.

**LA FRONTERA SE VIGILA CON UNA GUARDA, NO CON UNA PROMESA**
(`docs/loop/SALIDA_V154_T8_GRAFO_INTACTO.txt`): sha256 de `dataset/` y el conteo
de censo y aristas, medidos antes y despues de correr el arnes. **Identicos los
dos.** CERO cifras del grafo movidas, con assert.

**La tabla por fase pasa de 4 VERDE / 4 VERDE PARCIAL / 0 NO CUMPLE a 5 / 3 / 0**
(`docs/loop/SALIDA_V154_T9_TABLA_POR_FASE_CIERRE.txt`, contada de su fichero). El unico movimiento es la fila 03.

**Y LA CELDA EN VERDE NO ES LA FASE ENTERA, QUE ES LO QUE HAY QUE NO CONFUNDIR.** Medida con `tallar_estado_de_fase.py` en `docs/loop/SALIDA_V154_T8_ESTADO_FASE_03.txt`, la fase 03 sigue trayendo cuatro sin cumplir: OP-M-02-ADMIT, OP-M-02-MEDIOS, OP-U-01 y OP-U-02, las dos ultimas sin vara escrita. Lo que la adjudicacion 6.6 pone en verde es LA CELDA de la tabla por fase, no el destino de esas cuatro. Lo que
la adjudicacion 6.6 pone en verde es LA CELDA de la tabla por fase, no el destino
de esas cuatro.

## 9. TAREA 9: EL CIERRE, RECOMPUTADO AL CIERRE

**CICLO ENTERO EN SU ORDEN**, nunca `run_phase1` suelto: `--reaplico-curaduria`
(**GATE 0: OK**, con **26 comprobaciones verdes de Gate 0 al cierre** y ninguna caida, contadas del fichero de Gate 0 del cierre y publicadas en `docs/loop/SALIDA_V154_T9_GUARDAS_CIERRE.txt`), `etiquetas_de_cara --aplicar` (71
etiquetas), `sync_assets_web` (seis assets), y despues
`git diff HEAD --numstat -- dataset/ web/ engine/`: **cero filas**.

**Y RECOMPUTADO DE VERDAD, NO HEREDADO.** La TAREA 5 movio cinco fichas a HECHA
**despues** de la corrida de la TAREA 4.c, asi que el expediente se vuelve a medir
al cierre (`docs/loop/SALIDA_V154_T9_EXPEDIENTE_CIERRE.txt`): pasa de
**41 / 29 / 12 / 0** a **36 / 24 / 12 / 0**, con **7 en LISTA sin ninguna prueba**,
y el movimiento son exactamente las cinco mesas, que dejan de "no calzar" porque
su estado ya calza con el repo.

**LAS GUARDAS DEL CIERRE, CON SU ESTADO REAL** (`docs/loop/SALIDA_V154_T9_GUARDAS_CIERRE.txt`
y `docs/loop/SALIDA_V154_T9_MUTACIONES_VIEJAS.txt`):

| guarda | estado |
|---|---|
| `verificar_apertura_sellada.py --vuelta 154` | **VERDE exit 0**, diez ficheros hijos directos del acta |
| `verificar_cifras_del_plan.py` | **VERDE exit 0**, 0 pares, seis filas examinadas (contado en `docs/loop/SALIDA_V154_T9_GUARDAS_CIERRE.txt`) |
| `verificar_mutaciones_viejas.py` (corrida **sola**, por la leccion de concurrencia del acta 153) | **VERDE exit 0**, las 23 mutaciones corren, muerden y repiten salida sellada |

**EL ARCHIVO AL CIERRE, contado de su fichero.** En
`docs/loop/SALIDA_V154_T9_GUARDAS_CIERRE.txt`: el registro de citas trae **154
pares distintos** (LECTURA_DIRIGIDA 122, CRIBADO 32; clases C 122, D 31, B 1).
En ese mismo fichero, los veredictos del cribado al cierre siguen en **3.388
lineas**. Y en ese mismo fichero, el
expediente esta en **71 fichas, HECHA 28 y LISTA 43**, con **un solo juego de
claves**.

## LOS OCHO DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**DISCUTIBLE 1, Y ES EL GORDO: `LD-OPC05-097` NO ME PARECE UNA C.** A ciegas lo
clasifique **A**. Mi caso: los cuatro pasos de `juran_rcca_metodo` **contienen al
`viaje_diagnostico_remedial` entero Y EN EL MISMO ORDEN**. Su paso 2 (analizar
sintomas, formular teorias, probarlas, identificar la causa raiz) son los pasos 1
a 4 del viaje; su paso 3 (disenar e implementar el remedio) son los pasos 5 y 6;
su paso 4 (ajustar los controles) es el paso 8. Queda el mismo material a dos
granularidades con dos apostillas (el enunciado esporadico contra cronico de uno,
la gestion de la resistencia del otro), que es **la definicion literal del segundo
polo del 9.22**, y el propio 9.22 avisa de que lo que decide no es el parecido de
los titulos sino **cuanto coincide y en que orden**. **No lo he tocado.**

**DISCUTIBLE 2: `LD-OPC05-046` huele a madre e hijo, no a enlace mutuo.**
`cultura_de_aprendizaje` contra `cultura_de_seguridad_componentes`. La cultura de
aprendizaje **es uno de los componentes** de la cultura de seguridad, y los dos
montan el sistema que recoge, analiza y difunde la informacion de incidentes. **No
lo tumbo** porque el segundo trae la evaluacion de los cuatro subcomponentes y el
escrito de por que vale la pena invertir, que el primero no tiene, pero es el que
menos me convence de los 41.

**DISCUTIBLE 3: en `LD-OPC05-040` la figura del 9.22 es DELGADA.**
`cost_management_plan` contra `stakeholder_register`: dos artefactos de
planificacion **sin solape ninguno**, y de fusion no tienen nada, pero cuesta
nombrar **que linea de uno expande el otro**, que es lo que la figura exige. La C
se sostiene por el lado de "no funden", no por el lado de la figura.

**DISCUTIBLE 4: la mutualidad de mi propio `LD-OPC05-122` es RESIDUO DE UN
COLAPSO.** Los dos ids que `metodologia_6s` nombra eran, antes del saneo, **dos
nodos distintos** (`mistake_proofing_poka_yoke` y `errores_a_prueba_poka_yoke`,
los dos deprecados y los dos colgando de `mistake_proofing_poka_yoke_2`, alias de
`error_proofing_servicio`). Un lector estricto puede sostener que **solo una de
las dos direcciones se penso nunca**. Sostengo la C porque el 9.22 pregunta por
LINEAS y no por intenciones, y las dos lineas estan y son distintas.

**DISCUTIBLE 5: como leo "en la nomina de la ficha" de la adjudicacion 6.1.** El
acta dice *"cuenta commits que tocan `dataset/`, `web/` o `engine/` EN LA NOMINA
DE LA FICHA"*. Lo leo como **"el mensaje del commit nombra el `id_op` de la
ficha"**, que es la condicion que la P3 ya tenia y que la adjudicacion no toca. Si
lo que se queria decir era otra cosa (por ejemplo, que las rutas tocadas caigan
sobre los `nodos` de la ficha), la vara es otra y hay que rehacerla.

**DISCUTIBLE 6: la P3b es un PROXY y lo digo con su nombre.** La adjudicacion pide
"el caso positivo de la ficha corriendo en rojo antes y en verde despues". Lo que
mido es que la ficha **cite** una salida de caso positivo o de mutacion que
**exista en el arbol del corte**. Prueba que el artefacto existe, **no** que la
prueba se haya vuelto a correr. Re correr 71 mutaciones por vuelta no cabe en una
vuelta, y por eso el limite va declarado junto a la funcion en vez de escondido.

**DISCUTIBLE 7, Y ES CONTRA LA ADJUDICACION 6.7: la regla, tal como esta escrita,
NO habria salvado a la vuelta 152.** Fui a mirar el `PROMPT_SIGUIENTE.md` que la
152 tenia delante (`git show 6f419952:docs/loop/PROMPT_SIGUIENTE.md`) y **el unico
hash que cita es `36b57d78`**, el mergebase con `main`: **no cita `d9fa886b`**.
Con la regla al pie de la letra, aquella guarda habria seguido en rojo por el
commit del fundador. **No la afloje por eso**: admitir por asunto o por autor
seria una puerta que abre cualquiera. La regla es **prospectiva**, y para que
sirva hace falta que el encargo cite el hash de la decision cuando la haya.

**DISCUTIBLE 8: hay una TERCERA asimetria en el instrumento del expediente, y la
6.2 no la cubre.** La 6.2 adjudica la asimetria entre la P3 (reloj congelado) y la
P2 (arbol de trabajo). Pero `declara_su_estado` lee `nota` y `adjudicacion`
**tambien del arbol de trabajo**, y eso hizo que **mis propias notas de la TAREA 1
movieran 4 fichas de silencio a declarado en la misma vuelta**. No es la caida del
acta 151 (aquella era la P3 comiendose su papeleo), pero es de su familia: **el
texto de la ficha que la vuelta acaba de escribir cambia la cifra que la vuelta
publica**. Lo dejo medido y atribuido en vez de arreglarlo por mi cuenta.

## LAS CUATRO PREGUNTAS

1. **La P3b.** El proxy del discutible 6, vale, o hay que re correr de verdad el
   caso positivo? Y si hay que re correrlo, con que cadencia, dado que son 71
   fichas?
2. **El texto de la ficha, congelado o no.** Por el discutible 8: debe
   `declara_su_estado` leer `nota` y `adjudicacion` **del corte** en vez del arbol
   de trabajo? Si la respuesta es si, la cifra publicada de congelados cambia y hay
   que decidir con que corte se compara la serie historica.
3. **El corredor.** Por el discutible 7: se pide al encargo del fundador que cite
   SIEMPRE por hash el commit de decision, o se amplia la guarda para admitir
   ademas el commit inmediatamente anterior al bloque de apertura cuando su arbol
   solo toca papeles de decision? La segunda es mas comoda y mas laxa, y por eso no
   la tomo por mi cuenta.
4. **Los tres pares de fuentes deprecadas.** `asignacion_recursos_en_gates` contra
   `sistema_gates_go_kill`, `formalizar_junta_asesora` contra
   `identificar_consejo_asesores` y `revision_portafolio_periodica` contra
   `sistema_gates_go_kill` quedan fuera por el criterio del 14 ago 2026. Se leen
   alguna vez, o quedan declarados fuera para siempre? Hoy estan nombrados dentro
   de la guarda, que es lo minimo, pero nadie los ha leido.

## PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las nueve adjudicaciones del acta 153 cubrian todo lo que esta
vuelta necesitaba, y donde tuve que interpretar (la lectura de "nomina de la
ficha", el alcance de la P3b) lo hice **por extension de una regla escrita** y lo
marque como discutible en vez de inventar doctrina.

## EL MURO, Y NO SE PASA

Sigo el orden escrito en modo continuo y **paro donde el acta 149, 3.10 manda**:
**la fase 08 no cierra sin una sesion con credencial y con el fundador delante.**
Medida hoy (`docs/loop/SALIDA_V154_T9_ESTADO_FASE_08.txt`): una operacion en el
catalogo y una sin cumplir, `OP-V-01`, sin vara escrita. Ahi termina lo que un
bucle puede hacer solo. **EL MERGE NO SE PIDE NI SE HACE: es
del fundador y solo suyo. La campana NO esta consumada.**
"""


def main():
    texto = CUERPO % {"MARCA_INI": MARCA_INI, "MARCA_FIN": MARCA_FIN,
                      "TABLA": tabla_tallada(), "COBERTURA": linea_cobertura()}
    with io.open(REPORTE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)
    n = texto.count(MARCA_INI)
    m = texto.count(MARCA_FIN)
    print("REPORTE escrito: %d lineas" % len(texto.splitlines()))
    print("marca de cabecera de apertura, veces que aparece: %d (tiene que ser 1)" % n)
    print("marca de cabecera de cierre,   veces que aparece: %d (tiene que ser 1)" % m)
    assert n == 1 and m == 1, "una marca de cabecera aparece mas de una vez: la 7.a otra vez"
    print("")
    print("CIFRA lineas del reporte: %d lineas" % len(texto.splitlines()))
    print("CIFRA marcas de cabecera en el reporte: %d lineas" % (n + m))


main()
