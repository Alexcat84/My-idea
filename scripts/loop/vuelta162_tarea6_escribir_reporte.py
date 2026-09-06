# -*- coding: utf-8 -*-
r"""vuelta162_tarea6_escribir_reporte.py . EL CIERRE DE LA VUELTA 162.

ESCRIBE `docs/loop/REPORTE.md` ENTERO, SOBRESCRIBIENDO EL ANTERIOR.

LA CABECERA NO SE TECLEA: se LEE de `docs/loop/SALIDA_V162_T6_CABECERA.txt`,
que es la salida de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta
162`, y se pega ENTERA entre sus dos marcas. Si el fichero no trae la tabla,
este instrumento PARA sin escribir.

USO:  python scripts/loop/vuelta162_tarea6_escribir_reporte.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
CABECERA = os.path.join(LOOP, "SALIDA_V162_T6_CABECERA.txt")
REPORTE = os.path.join(LOOP, "REPORTE.md")
ABRE = "--- LA TABLA, PARA PEGAR ENTERA EN LA CABECERA DEL REPORTE ---"
CIERRA = "FIN"


def tabla_tallada():
    texto = io.open(CABECERA, encoding="utf-8").read()
    i = texto.find(ABRE)
    if i < 0:
        raise SystemExit("ROJO: la salida del tallador no trae su marca de apertura.")
    resto = texto[i + len(ABRE):]
    j = resto.rfind("\n" + CIERRA)
    if j < 0:
        raise SystemExit("ROJO: la salida del tallador no trae su marca de cierre.")
    filas = [l for l in resto[:j].split("\n") if l.strip().startswith("|")]
    if len(filas) < 5:
        raise SystemExit("ROJO: la tabla tallada trae %d fila(s)." % len(filas))
    return "\n".join(filas), len(filas)


CUERPO = u"""# REPORTE DE LA VUELTA 162 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**EL VEREDICTO DE UNA LINEA: EL ENCARGO ENTREGADO ENTERO, LAS CINCO TAREAS, Y LAS
TRES GUARDAS QUE EL ACTA 161 MANDO ARREGLAR MUERDEN AHORA Y NINGUN VEREDICTO
VIEJO SE MOVIO.** La puerta del corredor tras una parada se ensancha y
`verificar_apertura_sellada.py --vuelta 161` pasa de ROJA a VERDE; la vara de los
destejidos deja de ser mas ancha que la ficha de `OP-D-02`; y la guarda de cifras
vuelve a ver las de fase, que se le habian escondido en una tabla. La `R.29` que
la vuelta 161 escribio mal pasa a `R.30` sin borrar una linea, y su causa queda
arreglada EN LA FUENTE. **TRAIGO DOS COSAS MARCADAS COMO DISCUTIBLES Y UNA
DISCREPANCIA MEDIDA QUE NO RESUELVO COPIANDO**, y las digo antes de saber si
acierto. **Cero clases movidas y cero nodos tocados.**

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

Todo lo de esta seccion sale de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 162`, salida
`docs/loop/SALIDA_V162_T6_CABECERA.txt`, pegada entera por
`scripts/loop/vuelta162_tarea6_escribir_reporte.py`, que la LEE del fichero.

<!-- CABECERA TALLADA -->
__TABLA__
<!-- FIN CABECERA TALLADA -->

**EL CORREDOR DE ESTA VUELTA NO TRAE NADA, Y ES LA PRIMERA VEZ EN TRES VUELTAS.**
El acta 161 (`f7f52f91`) escribe su encargo en el mismo commit, o sea que no hay
parada que reanudar, y el bloque de apertura nace como HIJO DIRECTO del acta. El
encargo dice `HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA: NINGUNO`, y no hizo
falta admitir nada.

**LA APERTURA Y EL CIERRE NO HEREDAN UNO DEL OTRO.** Las diez mediciones de
apertura nacieron todas en `78d10690`, primer commit de la vuelta, y las diez de
cierre se volvieron a correr al cerrar. El ciclo de Gate 0 se corrio ENTERO y en
su orden las dos veces, nunca `run_phase1` suelto: `--reaplico-curaduria`,
`etiquetas_de_cara --aplicar`, `sync_assets_web` y despues
`git diff HEAD --numstat -- dataset/ web/ engine/`, que da cero filas
(`docs/loop/SALIDA_V162_CICLO_NUMSTAT_CIERRE.txt`).

**LAS TRES CONSTANCIAS DEL CIERRE, CADA UNA CON SU FICHERO AL LADO, PARA QUE LA
GUARDA DE CITAS TENGA QUE COTEJAR ALGO Y NO SALGA VERDE SOBRE CERO.**
GATE 0 OK en `docs/loop/SALIDA_V162_GATE0_CMD1_CIERRE.txt`. El motor da 25/25 en
`docs/loop/SALIDA_V162_MOTOR_CIERRE.txt`. Y la cabecera de este reporte sale
IDENTICA AL TALLADOR en `docs/loop/SALIDA_V162_T6_CABECERA_COMPARADA.txt`.

**Y LA COMPARACION DE LAS DOS BATERIAS, BYTE A BYTE Y SIN AFLOJARLA**
(`scripts/loop/vuelta162_baterias_cmp.py`, salida
`docs/loop/SALIDA_V162_T6_BATERIAS.txt`): siete familias IDENTICAS y dos
DISTINTAS, `MOTOR` y `WEB`. **La diferencia se mide en vez de excusarse**
(`docs/loop/SALIDA_V162_T6_BATERIAS_DIFF.txt`): son decimas de segundo por prueba
y la hora de arranque, y ningun veredicto se mueve.

## 1. TAREA 1.a, LA CAIDA DE LA `R.29`, ARREGLADA EN LA ENTRADA Y EN LA FUENTE

**LA SERIE SE RECOMPUTA CON INSTRUMENTO DE LOS DOS FICHEROS ANTES DE ESCRIBIR
NADA**, que es exactamente lo que fallo. Instrumento nuevo y de nombre estable,
sin numero de vuelta: `scripts/loop/serie_de_registros.py`, salida
`docs/loop/SALIDA_V162_T1A_SERIE_ANTES.txt`. **Lo que midio, con la serie entera
impresa fichero por fichero:** veintidos entradas, veintiuna en
`docs/PENDIENTES.md` y una en `docs/plan/CORRECCIONES_A_APLICAR.md`, **UNA
COLISION** en `R.29` y siguiente libre `R.30`.

**LA CORRECCION, SIN BORRAR UNA LINEA** (`docs/loop/SALIDA_V162_T1A_RENUMERAR.txt`):
la entrada de la vuelta 161 pasa a `R.30`, el titulo viejo queda **TACHADO Y
LEGIBLE** justo debajo con su motivo delante, y el `git diff --numstat` da
veinticinco anadidas contra **dos** borradas, que son las dos del titulo viejo y
vuelven tachadas. **Y LA CIFRA DEL ACTA REPRODUCE AL DIGITO**: entre la remision
de la vuelta 150 (`docs/PENDIENTES.md:10389`) y la entrada mal numerada hay
**setenta y seis** de distancia, que es lo que el acta 161 midio en su seccion
5.1. La `R.29` legitima sigue donde estaba, `docs/plan/CORRECCIONES_A_APLICAR.md:2127`.

**LA CAUSA, ARREGLADA EN LA FUENTE** (`docs/loop/SALIDA_V162_T1A_ARREGLO_FUENTE.txt`).
En `scripts/loop/vuelta161_tarea1_0_registros.py`: la frase tecleada de la
cabecera queda tachada y legible con su correccion al lado; la constante que
llevaba el numero DENTRO pasa a ser el titulo SIN numero; y la idempotencia deja
de mirar un solo fichero y pasa por la serie recomputada. **Re corrido hoy, el
instrumento dice `YA ESTABA: la entrada vive como R.30`.**

**CASO POSITIVO POR MUTACION SOBRE VARIABLE COMPUTADA**
(`docs/loop/SALIDA_V162_T1A_MUTACION_SERIE.txt`): se copian las dos sedes a un
temporal, se mete una `R.31` **de mentira en el OTRO fichero** y el instrumento
**LA VE**, moviendo el siguiente libre de `R.30` a `R.32`. Mirando solo
`docs/PENDIENTES.md` habria seguido diciendo `R.30`, que es la ceguera exacta de
la vuelta 161. Cinco casos, los cinco pasan y **los cinco CAEN** al mutarles el
valor esperado, y el arbol de trabajo queda del mismo tamano.

## 2. TAREA 1.b, LAS OCHO ADJUDICACIONES DEL ACTA 161

`docs/loop/SALIDA_V162_T1B_ADJUDICACIONES.txt`. Quedan como `R.31` en
`docs/PENDIENTES.md`, **sede ELEGIDA contando la serie** (veintiuna entradas
contra una) y no supuesta. El numero **no se teclea**: lo computa
`serie_de_registros.py`. El titulo de cada adjudicacion se **lee hoy** de su
linea en `docs/loop/ACTA_AUDITOR.md`, acotando la seccion 6 **del acta 161**
(lineas 53247 a 53613) porque el fichero trae mas de un `6.1`; la glosa que sigue
va marcada como prosa del ejecutor y no del acta.

**EL REPARTO, CONTADO Y NO TECLEADO:** tres se ejecutan EN CODIGO (6.4, 6.5,
6.6), dos EN EL REGISTRO (6.7, 6.8) y tres SIN TOCAR NADA (6.1, 6.2, 6.3),
porque adjudican que lo hecho estaba bien. Ninguna sube al fundador y ninguna
mueve una clase.

## 3. TAREA 1.c, LAS DIECISEIS MARCAS DE LA CIEGA DEL AUDITOR

`docs/loop/SALIDA_V162_T1C_MARCAS_CIEGA.txt`. **El sello se comprueba HOY** con
`git hash-object`: `ffe1fa6f96217ed9ee38b4b38fa43f56aa1b3848`, que calza con el
`ffe1fa6f` que el acta cita. **La nomina se RECOMPUTA del registro**: catorce en
`C` mas los dos ejemplares de exclusion, dieciseis. La marca va **por adicion**
en el campo `razon`, con la forma que `P.5.2` exige
(`RELECTURA CIEGA DEL AUDITOR, VUELTA 161`), citando la seccion 3 del acta y el
sello. **CERO CLASES MOVIDAS.**

**LAS GUARDAS DEL MOTOR, TODAS VERDES Y MEDIDAS:** las 154 razones conservan su
prefijo entero, los pares del registro siguen siendo los mismos 154 sin mover
ninguno, cero clases movidas, ninguna a
`A`, `sha256` de `dataset/` IDENTICO antes y despues, censo y aristas identicos,
`n` en 3.388 y cero citas que declaren una clase distinta de la vigente.
Recontado del fichero ya escrito: dieciseis filas llevan la marca.

**Y LA PROCEDENCIA DE CADA VEREDICTO SE DECLARA APARTE, PORQUE NO ES LA MISMA
PRUEBA, Y LO DIGO YO ANTES DE QUE ME LO PREGUNTEN.** SEIS de las dieciseis
(`049`, `098`, `052`, `095`, `100`, `122`) tienen su letra **escrita y sellada**
en el fichero del auditor, y el instrumento **la parsea de ahi**. LAS OTRAS DIEZ
**no traen fichero con su letra**, y esa cuenta la publica
`docs/loop/SALIDA_V162_T1C_MARCAS_CIEGA.txt` en sus dos lineas de procedencia,
seis selladas contra diez derivadas: su veredicto se **deriva** de la tabla de la
seccion 3 del acta, leida hoy en `docs/loop/ACTA_AUDITOR.md:53375`, que publica
dieciseis leidos, dieciseis coinciden y cero discrepan. **Esa lectura derivada va escrita
dentro de la marca de esas diez**, en vez de presentarla como si fuera una letra
sellada, y su cuenta se publica en
`docs/loop/SALIDA_V162_T1C_MARCAS_CIEGA.txt`.

**LA CIFRA DE `P.5.2`, RECOMPUTADA Y ANADIDA SIN BORRAR NI LA DE APERTURA NI LA
DE CIERRE DE LA 161** (`docs/loop/SALIDA_V162_T1C_ESCRITURA_P52.txt`, adicion
pura con cero borrados sobre el banco):

| | apertura de la 161 | cierre de la 161 | **vuelta 162** |
|---|---:|---:|---:|
| con al menos una segunda lectura independiente | 85 | 92 | **92** |
| con dos o mas | 0 | 7 | **16** |
| con ninguna | 37 | 30 | **30** |
| actos de relectura contados sobre filas | 85 | 99 | **115** |
| actos distintos `(tipo, vuelta)` | 6 | 7 | **8** |

**LO QUE ESA TABLA DICE:** el *con al menos una* NO se mueve, porque las
dieciseis ya tenian marca de otra pluma. Lo que se mueve es el **con dos o mas**,
de siete a dieciseis, que es exactamente lo que `P.5.2` persigue: una segunda
lectura independiente que antes no era contable porque vivia solo en el acta.

## 4. TAREA 2.a, LA PUERTA DEL CORREDOR TRAS UNA PARADA

**LA VARA DE ACEPTACION, CUMPLIDA Y MEDIDA**
(`docs/loop/SALIDA_V162_T2A_NUEVA.txt`): `verificar_apertura_sellada.py --vuelta
161` pasa de ROJA con diez fallos a **VERDE**, y `--vuelta 162` sale **VERDE**.

**LO QUE SE ANADE.** Cuatro piezas, y las tres primeras son **puras a
proposito** para que el caso por mutacion pueda darles un encargo y un corredor
fabricados en memoria: `es_firma_de_parada` (el acta trae el encargo VACIO y
`PARA_ALEXIS.md` ESCRITO), `portadores_del_encargo` (los commits del corredor que
escriben `PROMPT_SIGUIENTE.md`, en orden cronologico), `sin_el_portador` y
`contenido_en_commit`. **EL MECANISMO DEL ROTULO NO CAMBIA EN NADA**: sin el
literal `HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA:` no entra nada, y un
hash citado de paso sigue sin entrar. **Mas de un portador tumba la guarda por
ambiguo, y esa mitad es nueva.**

**NINGUN VEREDICTO VIEJO SE MUEVE, Y NO SE ALEGA.** Copia byte a byte de la
guarda vieja tomada ANTES de tocar nada (`scripts/loop/_v162_apertura_vieja_copia.py`),
las dos corridas sobre las vueltas 156, 158, 159, 160, 161 y 162, y cotejo
MECANICO de veredicto, codigo de salida y lineas de fallo
(`docs/loop/SALIDA_V162_T2A_COTEJO.txt`): **cinco IDENTICAS y una MOVIDA, la
161**, que es la unica que la adjudicacion manda mover. **El cotejo cae en los
dos sentidos**: tambien si una vuelta que debia moverse no se mueve.

**CASO POSITIVO POR MUTACION** (`docs/loop/SALIDA_V162_T2A_MUTACION.txt`):
catorce casos, los catorce pasan y **los catorce CAEN** al mutarles el valor
esperado. Los dos que importan van por su nombre:
`puerta_solo_con_firma` (sin firma de parada la puerta NO se abre) y
`rojo_del_ejecutor_intacto` (un commit del ejecutor delante de la apertura sigue
siendo intruso aunque el portador este en el mismo corredor).
`verificar_mutaciones_viejas.py` sigue VERDE con sus veintitres, o sea que la
firma de `intrusos_del_corredor` no se toco y los arneses viejos siguen
corriendo.

## 5. TAREA 2.b, LA VARA DE LOS DESTEJIDOS Y `OP-D-02`

**LA TABLA DE EXCEPCIONES CITA SU ADJUDICACION Y SE VERIFICA SOLA.** La entrada
de `OP-D-02` nombra los dos ids que la ficha manda TENER DELANTE, cita su
adjudicacion y trae **las dos frases literales de la ficha** que la sostienen. El
patron es el de la lista blanca de `OP-C-05`, donde *cada entrada cita su
lectura*: una excepcion sin cita es un agujero. **Y la cita no es decorativa**:
si una sola de esas frases desaparece de la ficha, **la excepcion NO se aplica** y
la operacion vuelve a medirse con la vara ancha, diciendolo en voz alta.

**LAS DOS CIFRAS DE LA FASE 02, ANTES Y DESPUES, Y LA DE ANTES NO SE BORRA:**

| momento | catalogo / cumplidas / sin cumplir | de donde sale |
|---|---:|---|
| antes de la excepcion | 9 / 1 / 8 | `docs/loop/SALIDA_V162_T2B_FASE_02_ANTES.txt` |
| despues de la excepcion | 9 / 2 / 7 | `docs/loop/SALIDA_V162_T2B_FASE_02_DESPUES.txt` |

Las siete que quedan sin cumplir son **exactamente** las siete SIN VARA ESCRITA:
en la fase 02 ya no queda ninguna roja con vara que muerda.

**CASO POSITIVO POR MUTACION, TODO EN MEMORIA Y EL PLAN INTACTO**
(`docs/loop/SALIDA_V162_T2B_MUTACION.txt`): ocho casos, los ocho pasan y **los
ocho CAEN** al mutarles el valor esperado. **El que el encargo exige por su
nombre, `absorbido_de_verdad_pendiente_sigue_rojo`, SIGUE SIN CUMPLIR**: se le
anade a la ficha un nodo vivo elegido POR COMPUTO y no tecleado, y la operacion
no se pone verde. Los otros dos que cierran la puerta: sin la tabla vuelve a salir el
*1 de 3* de siempre, y con la frase de la ficha retirada la excepcion no aplica.

## 6. TAREA 3, LA GUARDA DE CIFRAS VUELVE A VER LAS FILAS DE TABLA

**LOS SUJETOS SON CONGELADOS Y COMMITEADOS**, no el `REPORTE.md` vivo (banco
9.10): `docs/loop/SUJETO_FIJO_V162_T3_REPORTE_161.md` y el de la 160 sacado de
`git show aa6bb622`. Un sujeto que se mueve no sirve de vara.

**MEDIDO CON LA GUARDA VIEJA, copiada antes de tocar nada**
(`docs/loop/SALIDA_V162_T3_VIEJA.txt`): sobre el reporte de la 161 cotejaba CERO
afirmaciones de cierre y salia VERDE. **CON LA NUEVA**
(`docs/loop/SALIDA_V162_T3_NUEVA.txt`) coteja sus **cuatro** filas de fase, una
por una, contra la linea `CIFRA:` del fichero que cada fila cita, y sigue VERDE.
Sobre el reporte de la 160 **SIGUE DANDO 5** y no gana ni una fila de tabla,
porque su cierre vive en prosa y el camino viejo no se toco.

**NADA SE AFLOJA Y LA TABLA NO SE PROHIBE.** Una fila entra al cotejo cuando trae
uno de los dos sujetos del vocabulario COMO PALABRA ENTERA y ademas cita una
salida existente de `tallar_estado_de_fase.py`, reconocida POR SU CONTENIDO. La
palabra `desfase` lo lleva dentro y por eso NO cuenta, que si no la fila del
calibrado entraria sola. El cotejo es numerico y exige que la fila traiga EN
ORDEN Y SEGUIDOS los tres numeros que ese fichero publica. **Lo que no se puede cotejar sale en un
AVISO VISIBLE con su cifra y su fila**, y el aviso NO tumba la guarda.

**CASO POSITIVO POR MUTACION** (`docs/loop/SALIDA_V162_T3_MUTACION.txt`): trece
casos, los trece pasan y **los trece CAEN** al mutarles el valor esperado. Los
tres que importan: una cifra movida en una fila de fase (el `16 / 16 / 0` pasado
a `16 / 15 / 0`) **pone la guarda ROJA** y solo cae esa fila; a esa misma fila se
le quita la cita y **CAE AL AVISO** en vez de desaparecer; y el reporte de la 160
no cambia de veredicto ni de cuenta.

## 7. TAREA 4, LA MEDICION QUE NO ARREGLA NADA

`docs/loop/SALIDA_V162_T4_COLISIONES_TITULO.txt`. **ES UNA MEDICION: no se funde
nada, no se propone fusion y no se toca ningun titulo.**

| vara | grupos | con mas de un id vivo |
|---|---:|---:|
| `titulo_concepto` EXACTO, la de Gate 0, leida hoy en `scripts/run_phase1.py:811` | 3.169 | 0 |
| titulo NORMALIZADO (NFKD, sin diacriticos, minusculas, espacios colapsados) | 3.168 | 1 |

**Gate 0 dice cero duplicadas y NO se equivoca: mide otra cosa.** La unica
colision normalizada, con su nomina entera: `sistema_responsabilidad_gerencial`
(*El Sistema es tu Responsabilidad*) contra
`sistema_responsabilidad_gerencial_2` (*El Sistema es Tu Responsabilidad*), los
dos de Deming, los dos vivos, los dos con cinco pasos, y **los dos con excepcion
declarada desde la vuelta 124**. Colisiones NUEVAS sin excepcion: cero.

**LA NORMALIZACION NO SE REIMPLEMENTA**: se importa de
`verificar_titulos_normalizados.py`, que corrida hoy por su cuenta da la misma
cifra. **Salud de la propia lista de excepciones**: cero ids exentos que ya no
viven y cero exentos que ya no colisionan con nadie.

## 8. TAREA 5, EL ORDEN ESCRITO Y EL MURO

El recorrido entero, con su tabla y su muro, vive en
`docs/loop/SALIDA_V162_T5_ORDEN_Y_MURO.txt`, que trae 71 lineas. **El orden se
LEE del fichero**
(campo `fase` de `docs/plan/OPERACIONES.jsonl`): once fases, ochenta y dos del
catalogo. Sin cumplir cuarenta y seis, de ellas **cuarenta y cuatro SIN VARA
ESCRITA** y solo **DOS con vara que muerde**, las dos de la fase 03
(`OP-M-02-ADMIT` y `OP-M-02-MEDIOS`, consumidas con superviviente divergente).

**LA VUELTA 161 PUBLICO 47, 44 Y TRES, Y ESA CIFRA NO SE BORRA: SE PONE AL
LADO.** La que sale es `OP-D-02`, y sale **por la TAREA 2.b de esta vuelta**, no
porque se haya tocado el grafo.

**EL MURO, MEDIDO HOY Y NO CITADO DE MEMORIA:** `docs/loop/ACTA_AUDITOR.md:50182`
leida hoy abre la seccion 3.10 del acta 149 con *"SI LA FASE 08 PUEDE DARSE POR
HECHA: NO"*; el `.env` no esta en el arbol de trabajo y **si** esta en
`.gitignore`; y `scripts/rumbos/prueba_rumbos.py`, corrida hoy, **falla visible**
con codigo 2 y `ERROR: falta VOYAGE_API_KEY en .env`. **Se para ahi y se dice: es
la frontera del bucle, no un fallo. EL MERGE NO SE PIDE NI SE HACE.**

## 9. MI CAIDA DE LA VUELTA, CAZADA ANTES DE PUBLICARLA

**UNA, Y ES DE INSTRUMENTO HEREDADO.** Mi primera corrida de la TAREA 5 reuso
`scripts/loop/vuelta161_tarea3_orden_y_muro.py` entero, y **su seccion D lleva
escrito a mano** que `OP-D-02` es la unica operacion fuera de la fase 03 sin
cumplir con vara que mide. **Eso quedo rancio el mismo dia**, porque la TAREA 2.b
de esta vuelta la puso CUMPLIDA. Escribo
`scripts/loop/vuelta162_tarea5_orden_y_muro.py`, que **importa** las secciones
buenas del instrumento de la 161 en vez de copiarlas y **computa** la seccion que
antes se tecleaba. **La salida rancia no se publico**, y la cazo leer mi propia
salida antes del commit, que es la unica vara que muerde estas.

## 10. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

  1. **EL PORTADOR DEL ENCARGO FUERA DEL CENSO DE INTRUSOS, Y ES EL MAS GORDO.**
     La letra de la adjudicacion 6.5 dice *leer el encargo del PRIMER commit
     posterior al acta que escriba `PROMPT_SIGUIENTE.md`*. **ESO SOLO NO BASTA
     PARA LA VARA DE ACEPTACION, y lo medi antes de escribir nada**:
     `git show d3482b11:docs/loop/PROMPT_SIGUIENTE.md` **no trae el rotulo**, asi
     que leer el encargo de ahi admite cero hashes y la 161 seguiria ROJA. Lo que
     la pone verde es la pieza que escribo con todas sus letras dentro de la
     guarda: **el portador del encargo no entra en el censo de intrusos, porque
     hace el papel del acta**, que es el commit que ABRE la vuelta y que el rango
     `acta..nacimiento` siempre excluyo. **Si el auditor no lo comparte, es suyo
     tumbarlo**, y entonces la vara de aceptacion del encargo es inalcanzable y
     eso es lo que habria que decir.
  2. **LA SEDE DE `R.31`.** El encargo dice *en la sede que la serie recomputada
     diga*, y la serie no dice una sede: dice un reparto. Elegi
     `docs/PENDIENTES.md` **contando**, veintiuna entradas contra una, y publico
     el conteo para que la eleccion se pueda auditar. La otra lectura posible es
     que la sede de un registro de ADJUDICACIONES sea
     `docs/plan/CORRECCIONES_A_APLICAR.md`, que es donde vive la unica entrada
     que no esta en `PENDIENTES`.
  3. **LAS DIEZ LETRAS DERIVADAS.** Diez de las dieciseis marcas de la ciega
     llevan un veredicto **derivado** de la tabla del acta, no leido de un
     fichero con la letra de cada caso. Lo escribo dentro de la propia marca,
     pero **sigue siendo una lectura derivada** y alguien podria pedir que esas
     diez no lleven marca hasta que el auditor selle sus letras una a una.
  4. **LA FIRMA DE PARADA EXIGE QUE EL FICHERO EXISTA Y ESTE VACIO.** Un acta que
     BORRARA `PROMPT_SIGUIENTE.md` en vez de vaciarlo no dispararia la puerta. Lo
     escribi asi por la letra de la adjudicacion (*"el commit del acta TRAE
     `PROMPT_SIGUIENTE.md` VACIO"*), y lo marco porque es una frontera fina.
  5. **EL AVISO NO TUMBA LA GUARDA.** Una fila de fase sin cita cae al AVISO y la
     guarda sigue en verde. Es lo que la adjudicacion 6.6 pide con sus palabras
     (*"lo que no pueda cotejar lo tiene que DECIR con su cifra en un AVISO
     visible"*), pero se puede leer que un aviso deberia acumular hasta romper.
  6. **LA FORMA NUEVA EN `FORMAS_QUE_CUENTAN`.** Anadi
     `RELECTURA CIEGA DEL AUDITOR, VUELTA N` al contador de `P.5.2` en la misma
     vuelta que la escribio, con el mismo argumento que la vuelta 161 uso para la
     suya. Se puede leer como que el contador se ajusta a la marca del dia.
  7. **LA TABLA DE EXCEPCIONES ES POR OPERACION Y NO POR TIPO.** `OP-D-02` es la
     unica entrada. Un dia habra otro DESTEJIDO con la misma figura y habra que
     escribir su entrada a mano; eso es a proposito (una excepcion sin cita es un
     agujero) pero no escala solo.
  8. **RE CORRI EL INSTRUMENTO DE LA VUELTA 161 SOBRE EL REGISTRO.** La TAREA 1.c
     usa `vuelta161_tarea1c_segunda_lectura.py` para recomputar `P.5.2` en vez de
     escribir uno nuevo. Es la ley de una sola fuente, pero deja un instrumento
     con nombre de otra vuelta produciendo la cifra de esta.

## 11. LA DISCREPANCIA MEDIDA QUE NO RESUELVO COPIANDO

**LA VARA DE ACEPTACION DE LA TAREA 3 DICE OCHO FILAS DE FASE Y YO CUENTO
CUATRO.** El encargo y la adjudicacion 6.6 dicen que sobre el reporte de la 161
la guarda tiene que cotejar **las OCHO filas de fase** del bloque final. Contadas
hoy sobre el sujeto congelado, ese reporte trae **CUATRO** filas que citan una
salida de fase (las de 03, 06, 08 y 09) y **doce** numeros dentro de ellas. Ni
ocho filas ni ocho cifras. **No fabrico un ocho**: publico cuatro, digo de donde
sale cada una y lo traigo como pregunta. Lo demas de la vara SI se cumple entero:
el reporte de la 160 sigue dando cinco y ningun veredicto viejo se mueve.

## 12. PENDIENTES DE DOCTRINA Y PREGUNTAS AL FUNDADOR

  - **PENDIENTE DE DOCTRINA 1: el `AVISO` de la guarda de cifras no acumula.**
    Hoy avisa y sigue verde. Nadie ha escrito cuantos avisos seguidos convierten
    una cobertura menguante en un rojo.
  - **PENDIENTE DE DOCTRINA 2: la caducidad de la tabla de excepciones de
    absorbidos esta sin escribir.** Su entrada se cae sola si la frase
    desaparece de la ficha, pero ninguna regla manda revisarla cada N vueltas.
  - **PREGUNTA 1.** La vara de aceptacion de la TAREA 3 dice ocho y yo mido
    cuatro (seccion 11). Quiero saber si el ocho nombra otra cosa que no supe
    leer, o si es una cifra de memoria.
  - **PREGUNTA 2.** El discutible 1: sacar al portador del encargo del censo de
    intrusos es MIA, no de la letra de la 6.5. Quiero que se adjudique
    expresamente, a favor o en contra.
  - **PREGUNTA 3.** Las diez letras derivadas de la TAREA 1.c: se quedan como
    estan, con su procedencia escrita, o se retiran hasta que el auditor selle
    caso por caso.
  - **PREGUNTA 4.** `node_modules/` esta SIN VERSIONAR y SIN IGNORAR en esta
    rama, y sale en cada `git status` de cada vuelta. No lo commiteo ni lo
    ignoro por mi cuenta, porque tocar `.gitignore` es alcance del fundador.
    Digo que esta ahi.

## 13. RUTAS TOCADAS Y ESTADO AL CIERRE

**Fuera de `docs/loop/` y `scripts/loop/`, esta vuelta toca tres**:
`docs/PENDIENTES.md` (la correccion de `R.30` y la entrada `R.31`),
`docs/plan/BANCO_DEL_PLAN.md` (la cifra nueva de `P.5.2`, adicion pura) y el par
del registro, `docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl` con
`docs/plan/LECTURAS_DIRIGIDAS.md` (las dieciseis marcas). **`docs/plan/OPERACIONES.jsonl`
NO se toca. `dataset/`, `web/` y `engine/` no se movieron**: el `numstat` del
ciclo da cero filas.

**EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE** y no heredado de la apertura:

| | cifra | de donde sale |
|---|---:|---|
| marcador del archivo: `n` / A / B / C / D | 3.388 / 551 / 72 / 5 / 2.760 | `docs/loop/SALIDA_V162_T6_MARCADOR_CIERRE.txt` |
| huecos / duplicados del marcador | 0 / 0 | el mismo |
| registro de citas: filas / `C` de lectura dirigida / `D` de lectura dirigida | 154 / 14 / 108 | el mismo |
| citas con rastro de correccion / en la forma vieja | 110 / 0 | el mismo |
| expediente: fichas / no calzan / congeladas declaradas / congeladas en silencio / HECHA sin prueba / LISTA sin prueba | 71 / 36 / 24 / 12 / 0 / 7 | `docs/loop/SALIDA_V162_T6_EXPEDIENTE.txt` |
| fase 02: catalogo / cumplidas / sin cumplir | 9 / 2 / 7 | `docs/loop/SALIDA_V162_T6_FASE_02.txt` |
| fase 03 | 16 / 12 / 4 | `docs/loop/SALIDA_V162_T6_FASE_03.txt` |
| fase 06 | 16 / 16 / 0 | `docs/loop/SALIDA_V162_T6_FASE_06.txt` |
| fase 08 | 1 / 0 / 1, `OP-V-01` | `docs/loop/SALIDA_V162_T6_FASE_08.txt` |
| fase 09 | 3 / 0 / 3 | `docs/loop/SALIDA_V162_T6_FASE_09.txt` |

**LA RACHA DEL CREDITO SIGUE EN CERO** por letra expresa de la decision del
fundador del 3 sep 2026, y esta vuelta **no mueve ninguna clase**, asi que no le
anade nada. La caida de la `R.29` **no acumula** por la adjudicacion 6.8 del acta
161, y queda registrada con su nombre en la seccion 1.

**Y EL MERGE NO SE PIDE Y NO SE HACE.** `pasada-unica` no se funde a nada por
mano del bucle. **La campana no esta consumada.**
"""


def main():
    tabla, filas = tabla_tallada()
    print("LA CABECERA SE LEE DEL FICHERO, NO SE TECLEA")
    print("   fuente: %s" % os.path.relpath(CABECERA, RAIZ).replace("\\", "/"))
    print("   CIFRA filas de la tabla tallada: %d" % filas)
    texto = CUERPO.replace("__TABLA__", tabla)
    io.open(REPORTE, "w", encoding="utf-8", newline="\n").write(texto)
    n = len(texto.split("\n"))
    print("   CIFRA lineas del reporte escrito: %d lineas por count(NL), que calza con wc -l, y %d por len(split(NL))"
          % (texto.count("\n"), n))
    largos = [c for c in texto if c in u"—–"]
    print("   CIFRA guiones largos o medios: %d" % len(largos))
    if largos:
        print("ROJO: el reporte trae guiones largos o medios.")
        return 1
    print("VERDE: docs/loop/REPORTE.md escrito.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
