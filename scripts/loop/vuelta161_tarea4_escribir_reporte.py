# -*- coding: utf-8 -*-
"""vuelta161_tarea4_escribir_reporte.py . EL CIERRE DE LA VUELTA 161: ESCRIBE
docs/loop/REPORTE.md.

LA CABECERA NO SE TECLEA (EJECUTOR.md 1): se LEE ENTERA de
`docs/loop/SALIDA_V161_T4_CABECERA.txt`, que es la salida de
`tallar_cabecera_reporte.py --fase04 --vuelta 161`, y se pega entre las dos
marcas literales que `--comparar` y `verificar_cifras_del_reporte.py` reconocen.
Si el fichero no esta o no trae tabla, este script PARA sin escribir nada.

USO:  python scripts/loop/vuelta161_tarea4_escribir_reporte.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
CABECERA = os.path.join(LOOP, "SALIDA_V161_T4_CABECERA.txt")
REPORTE = os.path.join(LOOP, "REPORTE.md")


def tabla_de_la_cabecera():
    texto = io.open(CABECERA, encoding="utf-8").read()
    filas = [l for l in texto.split("\n") if l.startswith("|")]
    return "\n".join(filas)


CUERPO = u"""# REPORTE DE LA VUELTA 161 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**EL VEREDICTO DE UNA LINEA: EL ENCARGO ENTREGADO ENTERO, LAS CATORCE EN `C`
RELEIDAS CON LA VARA CONGELADA Y NINGUNA MOVIDA, LAS TRES DEUDAS CERRADAS, Y
TRAIGO TRES COSAS QUE NO ARREGLO YO.** Las tres: la guarda de la apertura sale
ROJA por una puerta que despues de una parada es inalcanzable por construccion;
dos de las catorce (`LD-OPC05-049` y `LD-OPC05-098`) piden mover la frontera de
la vara y por eso **no les toco la clase**; y el orden escrito, recorrido entero,
saca un rojo nuevo en `OP-D-02` que puede ser de la vara y no de la operacion. Y
declaro **DOS caidas propias**, las dos cazadas leyendo mi propia salida antes de
commitear.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

Todo lo de esta seccion sale de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 161`, salida
`docs/loop/SALIDA_V161_T4_CABECERA.txt`, pegada entera por
`scripts/loop/vuelta161_tarea4_escribir_reporte.py`, que la LEE del fichero.

<!-- CABECERA TALLADA -->
__CABECERA__
<!-- FIN CABECERA TALLADA -->

**Y LA IDENTIDAD DEL CORREDOR, LEIDA DE GIT EN ESTA VUELTA**, salida
`docs/loop/SALIDA_V161_T4_RUTAS.txt`:

| | valor | de donde sale |
|---|---|---|
| rama | `pasada-unica` | `git rev-parse --abbrev-ref HEAD` |
| commit del acta que abre la vuelta | `ed234154` | tallador `--fase04`, patron "ACTA DE LA VUELTA 160 DEL AUDITOR" |
| HEAD de apertura, sellado antes de la 1.a operacion | `d3482b11` | `docs/loop/SALIDA_V161_HEAD_APERTURA.txt` |
| HEAD de cierre, sellado tras la ultima operacion | `24f48fac` | `docs/loop/SALIDA_V161_HEAD_CIERRE.txt` |
| commits del corredor, medidos ANTES del commit de este reporte | 9; con el seran 10 | `git rev-list --count d3482b11..HEAD` |
| intrusos en el corredor | 0 | los 9 son mios, uno de apertura y ocho de tarea |
| `git diff --numstat d3482b11..HEAD` de `dataset/ web/ engine/` | cero filas | `docs/loop/SALIDA_V161_T4_RUTAS.txt` |

**LA APERTURA Y EL CIERRE NO HEREDAN UNO DEL OTRO.** Las diez mediciones de
apertura nacieron todas en `4208b8fa`, el primer commit de la vuelta, y las diez
de cierre se volvieron a correr al cierre.
`scripts/loop/vuelta161_baterias_cmp.py`, salida
`docs/loop/SALIDA_V161_T4_BATERIAS.txt`: siete familias IDENTICAS y dos
DISTINTAS, `MOTOR` y `WEB`. **Y la diferencia se mide en vez de excusarse**
(`docs/loop/SALIDA_V161_T4_BATERIAS_DIFF.txt`): son tiempos por prueba y la hora
de arranque, y ningun veredicto se mueve.

## 1. MIS CAIDAS, LAS DOS, Y VAN ANTES QUE LO DEMAS

**CAIDA 1, DE CLAVE ADIVINADA, EN LA TAREA 1.b, Y ES LA MISMA ESPECIE QUE EL
ACTA 158 YA TIENE REGISTRADA.** Mi primer auditor de assets leyo el grafo con
`grafo.get("nodes", grafo)` y publico *"CIFRA nodos del grafo: 6"*, que son las
claves de primer nivel del fichero: esta casa llama `nodos` a esa clave. **Es
literalmente el caso que `docs/loop/ACTA_AUDITOR.md:52977` describe**, leido hoy:
*"leyo el grafo por la clave `nodes` y las filas del archivo por `puesto`, y esta
casa las llama `nodos` y `puesto_intra`. Salio `CIFRA nodos: 6`"*. **La cazo
releer mi propia salida antes de commitearla.** Corregida en la fuente con la
linea vieja TACHADA Y LEGIBLE, y ademas **la clave ya no se adivina**: si no esta,
el instrumento revienta en vez de caer a un valor por defecto.

**CAIDA 2, DE LEER UNA COLUMNA POR OTRA, EN LA TAREA 3.** Mi primera version del
recorrido del orden leyo la columna `sin cumplir` del tallador de fases como si
fuera *operaciones pendientes*, y publico **"LA PRIMERA DEL ORDEN QUE NO CIERRA:
`00_CODIGO`"**, que contradice el estado publicado de la campana. El tallador
cuenta como `sin cumplir` **tambien las NO COMPUTABLES**, o sea las de un tipo
para el que no hay regla escrita que mida su destino contra el grafo, y las
publica aparte en su propia cifra. **Tambien la cazo releer mi propia salida.**
Corregida separando las dos columnas, con el motivo escrito en la fuente.

**LO QUE TIENEN EN COMUN LAS DOS, Y LO ESCRIBO PORQUE ES LA LECCION: NINGUNA LA
VI AL ESCRIBIR, Y LAS DOS SE CAZARON LEYENDO LA SALIDA.** Las dos habrian pasado
cualquier guarda de esta casa: la primera porque `dict.get` con valor por defecto
no falla nunca, y la segunda porque la cifra que copie era correcta en su propio
fichero. **La unica vara que las mordio fue mirar la salida antes de publicarla.**

## 2. LO QUE TRAIGO Y NO ARREGLO: TRES COSAS, CADA UNA CON SU CARA

### 2.1 LA GUARDA DE LA APERTURA SALE ROJA, Y LA PUERTA ES INALCANZABLE POR CONSTRUCCION

Salida entera en `docs/loop/SALIDA_V161_T0_APERTURA_SELLADA.txt` (al abrir) y
`docs/loop/SALIDA_V161_T4_APERTURA_SELLADA.txt` (al cerrar). **Las dos ROJAS, y
las publico enteras en vez de resumirlas.**

**QUE PASA.** El corredor de esta vuelta trae `d3482b11`, la **decision del
fundador**, que toca `docs/plan/BANCO_DEL_PLAN.md` (donde escribe la `P.5.1`
congelada) y `docs/plan/OPERACIONES.jsonl` (la nota de la ficha de `OP-C-05`)
porque la propia decision manda escribir la vara **donde vive**. La guarda admite
un commit de decision del fundador **solo si el encargo lo marca por su hash**
(adjudicacion 6.8 del acta 155), y **el encargo se lee DEL COMMIT DEL ACTA**.

**POR QUE ES INALCANZABLE, Y NO ES OPINION.** Tras una parada, el acta deja
`docs/loop/PROMPT_SIGUIENTE.md` **VACIO a proposito** (es lo que la seccion 4 del
`AUDITOR.md` le manda al auditor, y el acta 160 lo dice con esas palabras).
Medido hoy: `git show ed234154:docs/loop/PROMPT_SIGUIENTE.md` **no imprime nada**,
y la guarda lo declara ella misma, *"rotulo ... en ese encargo: NO"*. **El rotulo
no puede existir ahi.** Toda vuelta que reanude tras una parada de decision nace
con esta puerta cerrada.

**LO QUE SI SE PUEDE MEDIR, Y LO MIDO** (`docs/loop/SALIDA_V161_T0_CORREDOR_MEDIDO.txt`):
entre `ed234154` y `d3482b11` los arboles de `dataset/`, `web/` y `engine/` son
**el mismo objeto de git** (`bfbdaa56...`, `5d6b8b39...`, `caf82f2c...` en los dos
extremos), `git diff --numstat` entre los dos da **cero filas** sobre esas rutas y
sobre `docs/plan/PASO_NODO_CALIBRADO.jsonl`, y censo, aristas y desfase del
calibrado salen **identicos** en los dos extremos. **Ninguna cifra de la apertura
se pudo mover.** El propio tallador de la cabecera lo confirma por su cuenta:
*"arboles de `dataset/` IGUALES: VERDE"*.

**NO TOCO LA GUARDA.** Ensanchar la puerta o mover de donde se lee el encargo es
mover una vara sobre la marcha, que es la enfermedad que esta campana acaba de
congelar. **PENDIENTE DE DOCTRINA y va como pregunta.**

### 2.2 DOS DE LAS CATORCE PIDEN MOVER LA FRONTERA: `LD-OPC05-049` Y `LD-OPC05-098`

**Y NO LES MUEVO LA CLASE.** El encargo lo dice con todas sus letras: *"Si una
lectura pide mover la frontera, ESO ES PARADA Y SE TRAE, no se ajusta la vara
sobre la marcha"*. Las dos van con su caso entero escrito en su razon del
registro y con la clase **intacta en `C`**.

**LA COLISION, Y ES DENTRO DE LA MISMA `P.5.1`:**

  - **LA LETRA** dice que la segunda linea cuenta como expansion **si trae
    procedimiento propio**. En las dos, el lado que expande lo trae: en la `049`
    son los seis pasos de `decision_pivotar_o_proceder` (revision honesta,
    cuatro confirmaciones, consejo asesor, decision formal); en la `098` son los
    pasos 5 a 10 de `lean_launchpad_web_startup_process` (sitio de baja
    fidelidad, trafico, backend, analytics, alta fidelidad, cobro real). **Por la
    letra, la `C` se sostiene.**
  - **EL EJEMPLAR `100`**, que es uno de los cuatro que la propia `P.5.1` fija,
    es `lienzo_modelo_negocio` contra un nodo que **lo consume**, y la vara lo
    **EXCLUYE**. Las dos de hoy son `lienzo_modelo_negocio` contra un nodo que lo
    consume, con la misma figura. **Por el ejemplar, la clase seria `D`.**

**LA DIFERENCIA ENTRE LAS DOS SE DECLARA EN VEZ DE TAPARSE:** en la `049` el
entregable de la otra ficha dice *"Business Model Canvas actualizado"*, o sea que
la consume explicitamente; en la `098` el entregable **no** menciona el lienzo
(dice sitio web de alta fidelidad con metricas, feedback y cobro), asi que ahi el
argumento del entregable **es mas debil**. Lo digo aunque juegue contra la
simetria de mi propio veredicto.

### 2.3 EL ORDEN ESCRITO SACA UN VEREDICTO NUEVO: `OP-D-02`

Salida `docs/loop/SALIDA_V161_T3_ORDEN_Y_MURO.txt`, seccion D. Es la unica
operacion **fuera de la fase 03** que sale sin cumplir **con una vara que mide**.
La vara toma como absorbidos todo el campo `nodos` menos el superviviente y les
exige estar deprecados y en `ids_alias`. **La ficha no dice eso**: su orden
interno manda **fundir** con `enfoque_mercado_voc` (punto 2) y solo **tener
delante** a `homework_frontend_loading` y `voice_of_customer_homework` (punto 4),
y su campo `eliminar` no lista ni un nodo. Medido contra el grafo, **lo que la ficha
manda si esta hecho**: `enfoque_mercado_voc` esta deprecado y esta en los
`ids_alias` del superviviente. **NO TOCO NI LA VARA NI LA FICHA.**

## 3. TAREA 1.0, LOS REGISTROS DE LAS DOS TANDAS Y DE LA PARADA

Instrumento `scripts/loop/vuelta161_tarea1_0_registros.py`, salida
`docs/loop/SALIDA_V161_T1_0_REGISTROS.txt`. **Sede: `docs/PENDIENTES.md`, entrada
`R.29`, por adicion pura con cero borrados medidos.** La sede se elige y **se
declara**: es la forma que la casa usa desde `R.9` y la ultima escrita era `R.28`.
**VA MARCADA COMO DISCUTIBLE**, porque el encargo dice *"LOS REGISTROS"* sin
nombrar fichero.

**Y SOBRE "CON SUS PUESTOS" SE MIDE EN VEZ DE ADIVINARSE.** En esta casa un
**puesto** es la posicion en el archivo del cribado (`puesto_intra`, de 1 a
3.388), que es como el banco cita sus ejemplares (*"el puesto 2091"*). Las cinco
caidas son de lectura dirigida y **ninguna esta en ese archivo**: comprobado
contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, **CERO de CINCO** tienen
`puesto_intra`. Lo que si tienen y se publica es su lugar en la racha y su fila
del registro, contada del fichero: `005` en la 7, `094` en la 121, `100` en la
127, `101` en la 128 y `118` en la 149.

**LA PARADA, RESUELTA POR CITA Y NO POR MEMORIA.** La regla del credito se lee
HOY de `docs/loop/AUDITOR.md:135` (*"para la parada. Dos tandas seguidas:
PARADA."*) y la decision del fundador de su fichero
`docs/loop/paradas/2026-09-03-credito-vara-movil-DECISION.md`, comprobando
literalmente la frase *"La racha del credito vuelve a CERO con la vara
congelada"* antes de citarla. **Si cualquiera de las dos hubiera dejado de decir
lo que se cita, el instrumento paraba sin escribir.**

## 4. TAREA 1.a, EL ALCANCE DE P.16 DEJA DE EXCLUIR POR NOMBRE

**EL DEFECTO, REPRODUCIDO ANTES DE TOCAR NADA**
(`docs/loop/SALIDA_V161_T1A_ALCANCE_ANTES.txt`): el instrumento daba **15** y
exit 1, exactamente lo que el encargo anticipaba. Su exclusion era una nomina
cerrada de dos nombres, y la vuelta 160 escribio tres instrumentos mas que
contienen el patron sin anadir ni un check. **Envejecia solo.**

**LA VARA NUEVA SE LEE DEL CONTENIDO CON `tokenize`, NUNCA DEL NOMBRE.** El
remedio de la vuelta 160 estampo en cada miembro del alcance un bloque de
comentario con su marca literal, y de ahi salen tres clases, que son **el que lo
LLEVA contra el que lo ESCRIBE EN OTROS**:

| clase | criterio, leido del contenido | cuantos |
|---|---|---:|
| `ALCANCE` | la marca vive en un COMENTARIO REAL y en ninguna cadena | 12 |
| `ESCRIBE_EL_REMEDIO` | la marca vive dentro de una CONSTANTE DE CADENA | 2 |
| `SOLO_CITA` | contiene el patron y no trae la marca de ninguna forma | 3 |

Las tres cifras y la nomina entera salen de
`docs/loop/SALIDA_V161_T1A_ALCANCE_DESPUES.txt`, seccion E. **La cuenta reproduce
DOCE y sale exit 0**, con los siete de la bateria al digito. Y **este mismo
instrumento se excluye solo**, sin que su nombre aparezca en ninguna nomina.

**EL CASO NEGATIVO SE PRUEBA POR MUTACION Y SOBRE VARIABLE COMPUTADA**
(`docs/loop/SALIDA_V161_T1A_MUTACION.txt`): la decision vive en `clasificar`, que
es **pura** y recibe el TEXTO. Quitarle la marca del comentario a uno del alcance
lo tumba a `SOLO_CITA` y baja la cuenta a **11**; ponersela a uno que no la tiene
lo sube a `ALCANCE` y la cuenta a **13** **sin cambiarle el nombre**; moverla a
una cadena da `ESCRIBE_EL_REMEDIO`; y **mutar el valor esperado de 12 a 13 tumba
el cotejo**. Seis casos, seis verdes, y los tres ficheros reales **intactos por
sha256** antes y despues.

**LO QUE ESTA VARA NO VE VA DICHO Y CONTADO, no callado.** Un check nuevo con
`git status` como vara no llevaria la marca y quedaria fuera; por eso la seccion
E imprime un **AVISO** con los que EJECUTAN el patron sin llevarla. Hoy sale uno,
`vuelta160_tarea3b_caso_positivo.py`, **y esta bien que salga**.

**Y DOS CAIDAS DE ROTULO MIAS, CAZADAS LEYENDO LA SALIDA** (no las cuento como
caidas de reporte porque nunca llegaron a publicarse): la seccion C seguia
diciendo *"(lectura B)"* sobre una nomina que ya no sale de ahi, y su cifra decia
*"ficheros con el patron: 12"* chocando de frente con los **17** que publica la
seccion E. Las dos corregidas con la linea vieja tachada y legible
(`docs/loop/SALIDA_V161_T1A_ROTULO.txt`).

## 5. TAREA 1.b, LOS SEIS ASSETS LEIDOS UNA VEZ, Y NO SALEN TODOS VERDES

Instrumento `scripts/loop/vuelta161_tarea1b_auditar_assets.py`, salida
`docs/loop/SALIDA_V161_T1B_ASSETS.txt`. **La deuda llevaba desde el acta 157 y la
vara vieja era el exit code y el `numstat` del ciclo: las dos dicen que el script
corrio y que el arbol no se movio, y ninguna mira lo que hay dentro.**

**LAS VARAS NO SON LA MISMA PORQUE LAS FUENTES NO SON LA MISMA COSA**, y el
resultado va con nombre, que es lo que el encargo pide:

| asset | vara | veredicto |
|---|---|---|
| `master_graph.json` | bytes contra su fuente del repo, CRLF normalizado a LF | **VERDE**, sha256 identico |
| `preguntas_cache.json` | igual | **VERDE**, sha256 identico |
| `node_families.json` | igual | **VERDE**, sha256 identico |
| `entry_seeds.json` | igual | **VERDE**, sha256 identico |
| `prompts.json` | caracter a caracter contra las constantes `SYSTEM_*` importadas | **VERDE**: doce guardadas, cero faltan, cero sobran, cero distintas |
| el indice semantico | cobertura contra el grafo (su fuente no vive en el repo) | **ROJO DE COBERTURA** |
| `manifest.json` | sha256 y bytes contra los ficheros de verdad | **VERDE**, cero descuadradas |

**EL ROJO, CON SU CARA, Y SU FICHERO SALE CON EXITCODE 1**
(`docs/loop/SALIDA_V161_T1B_ASSETS.txt`). El indice semantico **no lo produce
este script** y su fuente no vive en el repo: la escribe
`scripts/build_semantic_index_voyage.py` llamando a una API que cuesta dinero
real. **Eso se dice en vez de fabricarle una
fuente.** Lo que si se puede medir sin salir del repo es la cobertura: el indice
trae 3.521 vectores, **los 3.521 son nodos reales** y **cero son claves
fantasma**; 332 entradas del grafo se quedan sin vector, y de esas **314 estan
deprecadas y DIECIOCHO ESTAN VIVAS**. **Un nodo vivo sin vector lo pierde la
busqueda semantica en silencio.** Los dieciocho van nombrados uno a uno en la
salida.

**Y NO ES UN HALLAZGO NUEVO, Y LO DIGO AUNQUE ME QUITE MERITO: REPRODUCE AL
DIGITO UNA CIFRA QUE EL AUDITOR YA PUBLICO.** `docs/loop/ACTA_AUDITOR.md:50196`,
seccion 3.11 del acta 149, leida hoy: una corrida completa del indexador *"deja el
indice con exactamente los 3.169 vivos de hoy: **los 18 entran y los 370 salen**
en la misma pasada"*. Mi medicion de hoy da los mismos 18 vivos sin vector y los
mismos 370 deprecados dentro del indice (3.521 menos 3.151). **Su remedio ya esta
adjudicado a la sesion con credencial**, o sea al muro de la seccion 8. **No se
arregla de paso.**

## 6. TAREA 1.c, LA DEFINICION DE SEGUNDA LECTURA INDEPENDIENTE

**Queda escrita en `docs/plan/BANCO_DEL_PLAN.md` como `P.5.2`**, junto a `P.5` y
`P.5.1`, por adicion pura con cero borrados medidos y **sin una sola celda
tecleada**: las cifras se extraen por expresion regular de
`docs/loop/SALIDA_V161_T1C_SEGUNDA_LECTURA.txt` y el escritor **para** si alguna
no se puede leer.

**LAS TRES COSAS QUE EL ENCARGO PIDE, Y ESTAN LAS TRES:**

  1. **QUE MARCA CUENTA.** La escrita en el campo `razon` del registro que dice
     **que es una RELECTURA** y **en que vuelta**. **No cuentan** la marca de la
     lectura que ABRE la fila (`LOTE 1 DE LA VUELTA 157`, `LOTE 2 DE LA VUELTA
     159`) ni las ediciones de mantenimiento (`UNIFICACION DEL CAMPO cita`,
     `ADJUDICACION 6.x DEL ACTA N`), **porque no vuelven a los nodos**.
  2. **QUIEN PUEDE FIRMARLA.** **La firma la da LA VUELTA, no la persona**:
     cuenta la relectura hecha en una vuelta posterior a la que publico la clase,
     y pueden firmarla las dos plumas. **Pero solo cuenta la que deja su marca en
     el registro**, porque una cifra que no se puede recomputar de un fichero no
     es una cifra.
  3. **UNA RELECTURA CONJUNTA CUENTA UNA SOLA VEZ**, y no por una regla aparte:
     los actos entran en un **conjunto** de pares `(tipo, vuelta)` y dos marcas
     del mismo acto sobre la misma fila **colapsan solas**.

**LA CIFRA, RECOMPUTADA POR ESA DEFINICION, Y LAS DOS VIEJAS TACHADAS AL LADO.**
De `docs/loop/SALIDA_V161_T1C_SEGUNDA_LECTURA.txt` (apertura) y
`docs/loop/SALIDA_V161_T2_SEGUNDA_LECTURA_CIERRE.txt` (cierre, porque la TAREA 2
de esta misma vuelta la movio):

| | apertura de la 161 | **cierre de la 161** |
|---|---:|---:|
| con AL MENOS UNA segunda lectura independiente | 85 | **92** |
| con DOS O MAS | 0 | **7** |
| con NINGUNA | 37 | **30** |

**LAS DOS VIEJAS NO SE COPIAN Y NO SE BORRAN**, cada una con su autor, su corte y
su linea leida hoy: **~~84~~** (auditor, acta 158, `docs/loop/ACTA_AUDITOR.md:52411`)
sumaba **dos libros**, las heredadas de las actas mas las ciegas del propio
auditor; **~~82~~** (auditor, acta 160, `docs/loop/ACTA_AUDITOR.md:53172`) contaba
**bloques anadidos**, incluidos los de mantenimiento. **Las dos eran fieles a lo
que cada una media. Lo que faltaba era decir que se mide.**

**Y LO QUE ESTA CIFRA NO VE VA MEDIDO Y NO ALEGADO:** doce razones nombran al
auditor **en prosa** y su relectura ciega **no deja marca contable** aqui, sino en
su acta y en sus `_auditor_v*_ciega*`. **Ahi es exactamente por donde bailaban
las cifras**, y la regla impone su remedio: **quien relee, escribe su marca**.

## 7. TAREA 2, LAS CATORCE EN `C` RELEIDAS CON LA VARA CONGELADA

**LA NOMINA NO SE COPIA DEL ENCARGO, SE RECOMPUTA**
(`docs/loop/SALIDA_V161_T2_NOMINA.txt`): sale CATORCE y **calza elemento a
elemento** con las catorce que el encargo nombra. Las cuatro que el encargo
excluye (`094`, `100`, `101`, `118`) se comprueban **en `D` y fuera de la
nomina**, y **los cuatro ejemplares de la vara se cotejan contra el registro
antes de leer nada**: `052` y `095` en `C`, `122` y `100` en `D`. **Los cuatro
calzan.**

**LOS NODOS SE IMPRIMEN ENTEROS ANTES DE ADJUDICAR.** El dossier de las
catorce trae 495 lineas y vive en `docs/loop/SALIDA_V161_T2_DOSSIER.txt`,
producido con
`vuelta159_dossier.py --nomina docs/loop/NOMINA_V161_TRAMO_C.json`.

**COMO SE LEE `P.5.1`, DECLARADO ANTES DE LEER PARA QUE SE PUEDA AUDITAR.** La
frase dice que la segunda linea *"cuenta COMO EXPANSION"*, o sea que **la segunda
linea es el lado que EXPANDE**, y lo que se le exige es que traiga procedimiento
propio. **Es la unica lectura que reproduce los cuatro ejemplares a la vez**:
`052` acepta por las seis preguntas de Chopra y Meindl con sus dimensiones
enumeradas; `095` acepta por los cinco pasos de process tracing, un metodo
secuenciado entero; `122` excluye porque el lado que expande solo **nombra**; y
`100` excluye porque es **la misma orden con complementos**.

**EL RESULTADO**, de `docs/loop/SALIDA_V161_T2_VEREDICTOS.txt`:

| | cifra |
|---|---:|
| lecturas del tramo | 14 |
| **que SOSTIENEN su clase** | **14** |
| que CAMBIAN de clase | 0 |
| traidas como PARADA de frontera, con la clase intacta | 2 |
| discutibles marcados | 5 |

**LA GUARDA DE COHERENCIA DEL ENCARGO PASA**: `052` y `095`, los ejemplares de
aceptacion, sostienen `C`, comprobado por assert. **Si alguno hubiera caido, eso
no era una reclasificacion mas y se paraba.**

**LAS GUARDAS DEL MOTOR, TODAS VERDES** (seccion C de la misma salida): prefijo
viejo intacto en las 154 razones, ningun par movido (su seccion C.2), cero
clases a `A`, sha256 de `dataset/` **identico** antes y despues, censo y aristas
identicos, `n` en 3.388, y **cero citas** que declaren una clase distinta de la
vigente. **EL RECORTE SE DECLARA**, como ya hizo la vuelta 160: la cifra de la
C.2 no se pega aqui porque su fichero no la escribe en la forma que
`verificar_cifras_del_reporte.py` sabe cotejar, y pegarla dejaria en el reporte
una cifra que ninguna guarda puede comprobar. Esta entera en el fichero. **La guarda
de `OP-C-05` re corrida** (`docs/loop/SALIDA_V161_T2_GUARDA_OPC05.txt`): 3.169
nodos vivos revisados, **0 entradas que sobran** antes y despues, **VERDE con
+0**. Y se declara sin que nadie lo pregunte: el sello `--antes` se tomo
**despues** de escribir el tramo, y vale porque el grafo es byte a byte el mismo,
medido por el propio motor.

**UNA CORRECCION DE CITA QUE NO ES MIA Y SE DECLARA.** Las razones de `087`, `088`
y `110` decian que `OP-E-04` las exceptua del 9.22 **en su verificacion 5**.
Leida la ficha hoy, **la verificacion 5 es la de `P.9` y los ids resueltos, y la
excepcion vive en la VERIFICACION 6**. Los tres pares **si** estan exceptuados
(las filas `LD-35` con `LD-51`, `LD-45` con `LD-53`, `LD-40` con `LD-48`); lo que
estaba mal era el numero. Corregido por adicion en las tres razones. **Y la `116`
NO esta exceptuada y se dice: su `C` se sostiene solo por la lectura de sus dos
lineas, sin declaracion sellada detras.**

## 8. TAREA 3, EL ORDEN ESCRITO Y EL MURO

**EL ORDEN SE LEE DEL FICHERO**, no de una lista tecleada: los nombres de fase
salen del campo `fase` de `docs/plan/OPERACIONES.jsonl`. **El recorrido entero
esta en `docs/loop/SALIDA_V161_T3_ORDEN_Y_MURO.txt`, seccion B**, con una columna
que separa lo que no se puede medir de lo que falla midiendose: de 47 sin
cumplir, **44 son NO COMPUTABLES** (nadie ha escrito con que medirlas) y **solo
TRES tienen vara que muerda**: las dos ya adjudicadas de la fase 03
(`OP-M-02-ADMIT` y `OP-M-02-MEDIOS`) y `OP-D-02`, que es la de la seccion 2.3.

**EL MURO, MEDIDO HOY Y NO CITADO DE MEMORIA:**

  - `docs/loop/ACTA_AUDITOR.md:50182`, leida hoy, abre la seccion 3.10 del acta
    149 con *"SI LA FASE 08 PUEDE DARSE POR HECHA: NO"*.
  - **`.gitignore` lista `.env`**, comprobado linea a linea en la seccion C de
    `docs/loop/SALIDA_V161_T3_ORDEN_Y_MURO.txt`.
  - **Y NO PUBLICO AQUI UNA AFIRMACION DE AUSENCIA SOBRE `.env`, Y DIGO POR
    QUE**: el instrumento de barrido de esta casa recorre `git ls-files`, y un
    fichero ignorado **no puede estar en ese universo por construccion**, asi que
    un barrido suyo daria un verde que no prueba nada. Lo que si prueba el punto
    es lo de abajo, que es positivo y se corre.
  - **La prueba de rumbos, corrida hoy, falla VISIBLE**: exit 2 y
    `ERROR: falta VOYAGE_API_KEY en .env`.

**LA FASE 08 TIENE UNA SOLA OPERACION, `OP-V-01`, y su punto 9 es la verificacion
TRANSVERSAL**: Gate 0, suite, **vuelo completo**, **prueba de rumbos** y
**reindexado semantico**. Las tres ultimas necesitan credencial. **SE PARA Y SE
DICE: es donde termina lo que un bucle puede hacer solo, y no es un fallo del
bucle.** **EL MERGE NO SE PIDE NI SE HACE.**

## 9. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

  1. **`LD-OPC05-049` y `LD-OPC05-098`**, las dos paradas de frontera. Un lector
     estricto puede decir que el ejemplar `100` decide solo y que debi bajarlas a
     `D`; otro puede decir que la letra manda y que sostener `C` es lo correcto.
     **No lo resuelvo yo.**
  2. **`LD-OPC05-005`.** El lado que expande su linea 2 es **fino**: su paso 3
     leido solo seria orden mas complemento, o sea de la especie que el ejemplar
     `122` excluye. Se sostiene porque los tres pasos leen como secuencia.
  3. **`LD-OPC05-068`.** Su linea 2 es una **prohibicion** con condicion
     temporal, no un acto, y `P.11` dice que una advertencia califica el acto y no
     lo constituye. Si `P.11` alcanza tambien al lado EXPANDIDO, esa figura se
     cae y la clase seria `D`.
  4. **`LD-OPC05-084`.** La linea manda **disenar experimentos** y el otro nodo
     procedimenta **observar**: el encaje es por proposito y no por acto.
  5. **LA SEDE DE LA TAREA 1.0.** Escribi los registros en `docs/PENDIENTES.md`
     como `R.29` porque es la forma que la casa ya usa; el encargo decia *"LOS
     REGISTROS"* sin nombrar fichero.
  6. **LA LECTURA DE `P.5.1` QUE APLIQUE A LAS CATORCE**, o sea que la segunda
     linea es el lado que EXPANDE. La justifico con los cuatro ejemplares, pero
     **es una lectura mia de una frase que admite otra**, y de ella cuelgan los
     catorce veredictos.
  7. **LA VARA DE CONTENIDO DE LA TAREA 1.a.** Excluye por la marca del remedio,
     que es un rastro historico; un lector puede decir que eso es una nomina
     cerrada disfrazada. Lo mitigo con el AVISO, pero **el reparo es legitimo**.
  8. **CONTAR EL AVISO DE LA TAREA 1.b COMO ROJO DEL ASSET**
     (`docs/loop/SALIDA_V161_T1B_ASSETS.txt`). El manifest y el sha256 del
     indice semantico estan los dos verdes; lo que esta roto es su **cobertura**.
     Elegi llamarlo ROJO, y su fichero sale con EXITCODE 1
     (`docs/loop/SALIDA_V161_T1B_ASSETS.txt`), porque una perdida silenciosa de
     busqueda es peor que un hash que cuadra.

## 10. PENDIENTES DE DOCTRINA Y PREGUNTAS AL FUNDADOR

  1. **LA PUERTA DEL CORREDOR DESPUES DE UNA PARADA** (seccion 2.1). El mecanismo
     de admision del commit de decision **no puede usarse** tras una parada,
     porque el acta vacia el encargo por mandato. **Pregunta:** donde debe leerse
     el rotulo en ese caso.
  2. **LA COLISION DE `P.5.1` CON SU PROPIO EJEMPLAR `100`** (seccion 2.2), sobre
     `lienzo_modelo_negocio`. **Pregunta:** manda la letra o manda el ejemplar.
  3. **LA VARA DE LOS DESTEJIDOS Y `OP-D-02`** (seccion 2.3). **Pregunta:** si
     *tener delante* cuenta como absorcion, la operacion esta sin cumplir; si no
     cuenta, la vara es mas ancha que la ficha y el rojo es falso.
  4. **LOS DIECIOCHO NODOS VIVOS SIN VECTOR** (seccion 5). Ya adjudicados a la
     sesion con credencial por el acta 149. **No es pregunta nueva: es el muro.**
  5. **`P.5.2` OBLIGA A ALGO QUE HOY NO SE HACE**: que el auditor deje su marca de
     ciega en el registro. Mientras no lo haga, la cifra que la regla define
     **pierde sus relecturas**. **Pregunta:** se adopta esa obligacion.

## 11. RUTAS TOCADAS Y ESTADO AL CIERRE

Todas leidas de git en esta vuelta, salida `docs/loop/SALIDA_V161_T4_RUTAS.txt`:
`docs/PENDIENTES.md`, `docs/plan/BANCO_DEL_PLAN.md`,
`docs/plan/LECTURAS_DIRIGIDAS.md`, `docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`,
`scripts/loop/vuelta159_tarea5_alcance_p16.py`, los instrumentos nuevos de la
vuelta bajo `scripts/loop/vuelta161_*` y las salidas bajo `docs/loop/SALIDA_V161_*`.
**`dataset/`, `web/` y `engine/` no se movieron**: `git diff --numstat` entre la
apertura y `HEAD` da cero filas sobre esas rutas.

**EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE** y no heredado de la apertura:

| | cifra | de donde sale |
|---|---:|---|
| marcador del archivo: `n` / A / B / C / D | 3.388 / 551 / 72 / 5 / 2.760 | `docs/loop/SALIDA_V161_T4_MARCADOR_CIERRE.txt` |
| huecos / duplicados del marcador | 0 / 0 | el mismo |
| registro de citas: filas / `C` de lectura dirigida / `D` de lectura dirigida | 154 / 14 / 108 | el mismo |
| citas con rastro de correccion / en la forma vieja | 110 / 0 | el mismo |
| expediente: fichas / no calzan / congeladas declaradas / congeladas en silencio / HECHA sin prueba / LISTA sin prueba | 71 / 36 / 24 / 12 / 0 / 7 | `docs/loop/SALIDA_V161_T4_EXPEDIENTE.txt` |
| fase 03: catalogo / cumplidas / sin cumplir | 16 / 12 / 4 | `docs/loop/SALIDA_V161_T4_FASE_03.txt` |
| fase 06 | 16 / 16 / 0 | `docs/loop/SALIDA_V161_T4_FASE_06.txt` |
| fase 08 | 1 / 0 / 1, `OP-V-01` | `docs/loop/SALIDA_V161_T4_FASE_08.txt` |
| fase 09 | 3 / 0 / 3 | `docs/loop/SALIDA_V161_T4_FASE_09.txt` |

**LA RACHA DEL CREDITO, POR LETRA EXPRESA DE LA DECISION DEL FUNDADOR, ESTA EN
CERO**, y esta vuelta **no mueve ninguna clase**, asi que no le anade nada. Lo
que si trae son **dos caidas propias declaradas** (seccion 1), ninguna de las
cuales llego a publicarse: las dos se cazaron leyendo la salida antes del commit.

**Y EL MERGE NO SE PIDE Y NO SE HACE.** `pasada-unica` no se funde a nada por
mano del bucle. **La campana no esta consumada.**
"""


def main():
    if not os.path.exists(CABECERA):
        print("PARADA: no existe %s. Sin cabecera tallada no se escribe reporte."
              % CABECERA)
        return 1
    tabla = tabla_de_la_cabecera()
    if tabla.count("\n") < 5:
        print("PARADA: la cabecera tallada no trae tabla suficiente.")
        return 1
    texto = CUERPO.replace("__CABECERA__", tabla)
    with io.open(REPORTE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)
    print("REPORTE ESCRITO en docs/loop/REPORTE.md")
    print("CIFRA lineas del reporte: %d" % (texto.count("\n") + 1))
    print("CIFRA filas de la cabecera pegadas del tallador: %d"
          % (tabla.count("\n") + 1))
    print("guiones largos: %d ; guiones medios: %d"
          % (texto.count(u"—"), texto.count(u"–")))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
