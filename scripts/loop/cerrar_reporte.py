# -*- coding: utf-8 -*-
r"""cerrar_reporte.py . EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como sus hermanos
`paso0_archivar_anterior.py`, `tallar_cabecera_reporte.py`,
`archivar_reporte.py`, `serie_de_registros.py`, `aislador_de_ciega.py` y
`anexar_tarea_al_reporte.py`: se invoca al cierre de cada vuelta y NO se clona,
para que el proximo clon no lo pierda.

POR QUE NACE (adjudicacion 6.6 del acta del auditor de la vuelta 171, y la causa
esta MEDIDA, no supuesta). Las vueltas 170 y 171 murieron las dos en el mismo
tramo: su bloque de cierre corrio entero, su tallador salio VERDE, y
`docs/loop/REPORTE.md` se quedo diciendo "SIN ESCRIBIR TODAVIA" y "PENDIENTE DE
TALLAR AL CIERRE". La causa no fue prisa: `vuelta171_cierre.py` **SOLO MIDE**,
escribe once ficheros `SALIDA_*` y **no toca `REPORTE.md` en ninguna linea**.
Cerrar el reporte era un paso a mano que venia despues, y ahi cayeron las dos.

QUE HACE, EN UN SOLO ACTO (es lo que `vuelta171_tarea1b_cerrar_reporte_170.py`
ya sabia hacer, con nombre estable y parametrizado):

  1. PEGA LA CABECERA leyendola del fichero del tallador. NINGUNA CELDA SE
     TECLEA (`EJECUTOR.md` 1, "LA CABECERA DEL REPORTE SE TALLA, NO SE TECLEA").
  2. ANEXA EL CUERPO DEL CIERRE (las secciones 3 a 8) tal como esta en su
     borrador, comprobando por sha256 que lo que anexa es byte a byte lo que el
     borrador dice.
  3. ESCRIBE LA SECCION 9 con LA SALIDA DE LA BATERIA ENTERA DENTRO.
  4. ESCRIBE EL VEREDICTO DE UNA LINEA en el sitio del "SIN ESCRIBIR TODAVIA".
  5. RELEE DEL DISCO lo que acaba de escribir.

LA QUINTA COMPROBACION, QUE NO ES UNA PIEZA SINO UNA CONVENCION (vuelta 178,
TAREA 1.e; adjudicacion del acta 177 punto 7.11). LA CONVENCION DE BYTES SIGUE
SIN FIJAR y es del fundador, no la fija nadie mas; lo que el auditor SI adjudica,
porque no elige entre las dos, es que MIENTRAS NO ESTE FIJADA TODA CIFRA DE
BYTES O SHA SE PUBLIQUE CON LAS DOS, disco y normalizado a LF. La causa esta
medida en la 177: su propio reporte declaraba hacerlo y luego no lo hizo en dos
celdas, un tallador publicado en "5.001 bytes" cuando el disco decia 5.021, y un
sha `7d683eea4700f18b` que era el de LF y no el de disco. LAS DOS CIFRAS ERAN
VERDADERAS Y LAS DOS HUBO QUE IR A BUSCARLAS. Aqui deja de depender de que
alguien se acuerde.

COMO SE MIDE, Y ES MECANICO. Una cifra esta EMPAREJADA si EN SU MISMA LINEA hay
DOS O MAS apariciones de su especie (dos "N bytes", o dos sha), O si la linea
NOMBRA AL MENOS DOS de las marcas de convencion (`disco`, `LF`, `normalizado`,
`cat-file`, `getsize`), que es la forma de decir "las dos convenciones dan esta
misma cifra" sin escribirla dos veces.

QUE QUEDA FUERA, Y SE DICE POR QUE: los bloques de codigo cercados con tres
comillas invertidas. Ahi va PEGADA la salida cruda de un instrumento, que es una
CITA y no una celda publicada: exigirle la pareja seria exigirsela al
instrumento citado, y una cita que se retoca deja de ser una cita. Los sha solo
se buscan en lineas que digan `sha`, para no confundir un hash de commit (que es
identidad y no contenido) con el sha de un fichero.

LA SEXTA COMPROBACION, Y ES LA OPERACION DE CODIGO DE LA ESCALADA (vuelta 179,
TAREA 1.b). `AUDITOR.md` 1.2 obliga a encargar la extension del tallador a las
fases mecanicas cuando la racha de caidas de reporte llega a dos, y llego (acta
178, seccion 6). El alcance lo autorizo el fundador el 29 ago 2026
(`paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md`), literal: *"toda
tabla y toda cifra del reporte en fases mecanicas se genera contando su fichero
de salida"*. La cabecera se talla desde la vuelta 56 y las tablas desde la 76; LO
QUE FALTABA ERA LA PROSA QUE CITA UN FICHERO, que es por donde entraron las dos
ultimas caidas.

EL EJEMPLAR, MEDIDO Y NO SUPUESTO: la linea 349 de
`docs/loop/reportes/REPORTE_V178.md` publica *"16 casos, los 16 pasan y los 16
CAEN"* citando `docs/loop/SALIDA_V178_T1E_MUTACION.txt`, y ese fichero, contado,
dice `CIFRA casos: 18 | pasan: 18 | fallan: 0`. La frase empieza en la linea 348
y termina en la 352, y por eso la unidad que se juzga es EL PARRAFO y no la
linea.

LA CONDUCTA, en `citas_de_arnes_que_no_calzan()`, que es PURA y recibe un lector:
toda frase que publique una cifra de casos Y nombre un `SALIDA_V*.txt` se cuenta
contra ese fichero, y CAE EN ROJO nombrando la linea, la cifra publicada y la del
fichero si no calzan, si el fichero no existe o si mide cero bytes. Los bloques
cercados quedan fuera, por el mismo motivo que la guarda de la pareja.

Y CAE EN ROJO SI AL TERMINAR FALTA CUALQUIERA DE LAS CUATRO PIEZAS:

  (1) EL VEREDICTO ESCRITO      . el "SIN ESCRIBIR TODAVIA" ya no esta y hay un
                                  veredicto de una linea en su sitio.
  (2) LA CABECERA PEGADA        . todas las filas de tabla del fichero del
                                  tallador estan dentro del reporte, byte a
                                  byte, y el hueco "PENDIENTE DE TALLAR" ya no
                                  esta.
  (3) LAS SECCIONES 3 A 9       . las siete existen.
  (4) LA BATERIA DENTRO DE LA 9 . la salida de la bateria de ESTA vuelta esta
                                  dentro de la seccion 9 y no vacia, **O** un
                                  HUECO DECLARADO Y MEDIDO en su sitio.

LA PIEZA (4) ADMITE EL HUECO DECLARADO Y MEDIDO (vuelta 173, TAREA 1.b;
adjudicacion 6.2 del acta del auditor de la vuelta 172). POR QUE CAMBIA, Y NO ES
DOCTRINA NUEVA SINO UN CHOQUE ENTRE DOS REGLAS ESCRITAS: chocan la 6.6 del acta
171, que exige *"la salida de la bateria dentro de la 9"*, y la regla de la casa
que el reporte de la 171 aplico al pie de la letra, *"el hueco se declara y no se
rellena"*, que sale de `EJECUTOR.md` 1 y del carril `9.10`. Tal como estaba, este
instrumento **solo podia cerrar los reportes que no lo necesitaban** y no podia
cerrar ninguno de los tres que habian fallado, que es exactamente para lo que
nacio.

LA LETRA ES ESTRECHA A PROPOSITO, y es la del acta:

  . la (4) se satisface con LA SALIDA DE LA BATERIA DENTRO DE LA SECCION 9,
    COMO HASTA AHORA;
  . O con un HUECO DECLARADO que traiga LAS TRES COSAS JUNTAS: el NOMBRE DEL
    FICHERO, sus BYTES MEDIDOS EN LA CORRIDA, y la ATRIBUCION de quien si la
    corrio o la declaracion de que no la corrio nadie;
  . LA AUSENCIA MUDA NO LA SATISFACE: una seccion 9 que se calla no es un hueco
    declarado, es un hueco escondido;
  . UNA CORRIDA DE OTRA VUELTA PEGADA AHI TAMPOCO: ni como bateria (se mira el
    numero de vuelta del fichero que se pega) ni dentro del hueco (se mira el
    numero de vuelta de todo `SALIDA_V<N>_BATERIA` que la seccion 9 nombre).

LAS CUATRO SE COMPRUEBAN CON `piezas_que_faltan()`, que es PURA y recibe el
texto: asi su caso positivo por mutacion puede tumbarla una a una sin tocar el
repo ni escribir nada. Su arnes es
`scripts/loop/vuelta172_tarea5_mutacion_cierre.py`, cuyos 17 casos SIGUEN VERDES
y no se tocan (condicion expresa de la 6.2), y la conducta nueva se prueba en un
arnes NUEVO, `scripts/loop/vuelta173_tarea1b_mutacion_hueco.py`. Los dos
parametros nuevos de `piezas_que_faltan()` son OPCIONALES justamente para que los
17 casos viejos, que la llaman con tres argumentos, sigan llamandola igual.

LO QUE NO HACE: no talla la cabecera (eso es de `tallar_cabecera_reporte.py`), no
archiva (eso es de `archivar_reporte.py`), no corre la bateria y NO ANEXA TAREAS
(eso es de `anexar_tarea_al_reporte.py`). Recibe lo que otros produjeron y lo
monta, y si algo falta lo dice en rojo en vez de escribir un reporte a medias.

USO:
  python scripts/loop/cerrar_reporte.py --vuelta 172 \
      --cuerpo scripts/loop/_v172_cierre_texto.md \
      --tallador docs/loop/SALIDA_V172_TALLADOR_CABECERA.txt \
      --bateria docs/loop/SALIDA_V172_BATERIA.txt \
      --veredicto "LA VUELTA 172 ..."

  Y cuando la bateria de esa vuelta NO CORRIO, con la atribucion delante, que es
  lo unico que convierte una ausencia muda en un hueco declarado:

  python scripts/loop/cerrar_reporte.py --vuelta 172 ... \
      --hueco-atribucion "NADIE la corrio: ni el ejecutor ni el auditor."
"""
import argparse
import hashlib
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

MARCA_ABRE = "<!-- CABECERA TALLADA -->"
MARCA_CIERRA = "<!-- FIN CABECERA TALLADA -->"
VEREDICTO_VIEJO = "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**"
HUECO_CABECERA = "PENDIENTE DE TALLAR AL CIERRE"
CAB_9 = "## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE"
CAB_9_HUECO = "## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO"

# LAS TRES MARCAS DEL HUECO DECLARADO. Son literales y no expresiones sueltas
# justamente para que un hueco no se pueda declarar "por parecido": o trae la
# marca, o no hay hueco declarado y la ausencia sigue siendo muda.
MARCA_HUECO = "HUECO DECLARADO Y MEDIDO"
MARCA_ATRIBUCION = "ATRIBUCION:"
# EL PATRON, ENSANCHADO EN LA VUELTA 182 POR EL REMEDIO DEL `E.1` DEL ACTA 180.
# ANTES ERA r"SALIDA_V(\d+)_BATERIA" Y ESA ERA LA PRIMERA DE LAS TRES CAUSAS: el
# fichero que la vuelta 180 paso se llamaba `SALIDA_V180_HUECO_BATERIA.txt`, con
# la palabra HUECO metida entre la vuelta y la palabra BATERIA, asi que el patron
# NO casaba y `vuelta_de_fichero()` devolvia None. El trozo `[A-Z0-9_]*` admite
# cualquier cosa en medio SIN admitir minusculas ni otro fichero: sigue exigiendo
# `SALIDA_V<numero>_` delante y `BATERIA` detras.
PATRON_FICHERO_BATERIA = re.compile(r"SALIDA_V(\d+)_[A-Z0-9_]*BATERIA")

# EL NOMBRE DE UNA CORRIDA, QUE NO ES LO MISMO QUE UN NOMBRE QUE LLEVE UNA VUELTA
# DENTRO. Nace en la vuelta 182 con la pieza (d) del remedio del `E.1`:
# `SALIDA_V180_BATERIA.txt` y `SALIDA_V176_BATERIA_TRAMO_3.txt` SI son nombres de
# corrida; `SALIDA_V180_HUECO_BATERIA.txt` NO lo es, y ese fue justamente el
# fichero con el que la vuelta 180 publico una cabecera falsa sobre un cuerpo que
# decia lo contrario.
PATRON_NOMBRE_DE_CORRIDA = re.compile(r"^SALIDA_V\d+_BATERIA[A-Z0-9_]*\.txt$")
PATRON_BYTES = re.compile(r"(\d[\d.]*)\s+bytes")

# LA PAREJA DE CIFRAS (vuelta 178, TAREA 1.e). Un sha se busca SOLO en lineas
# que digan `sha`, y con 12 caracteres hexadecimales como minimo, para no
# confundirlo con un hash corto de commit: un commit es identidad, no contenido,
# y la convencion que falta es la del contenido.
PATRON_SHA = re.compile(r"\b[0-9a-f]{12,64}\b")
MARCAS_CONVENCION = ("disco", "LF", "normalizado", "cat-file", "getsize")
CERCA = "```"

# LA CITA DE ARNES (vuelta 179, TAREA 1.b; operacion de codigo de la escalada de
# AUDITOR.md 1.2, con el alcance que el fundador autorizo el 29 ago 2026). Se
# caza la prosa que publica una cifra de casos Y nombra el fichero de salida de
# donde deberia salir. La ventana esta en caracteres y no en lineas porque el
# markdown parte las frases donde le cabe el ancho: la frase de la caida de la
# 178 empieza en la linea 348 y termina en la 352.
PATRON_SALIDA_TXT = re.compile(r"SALIDA_V\d+_[A-Za-z0-9_]+\.txt")
# DOS FORMAS DE PUBLICAR LA MISMA CIFRA, y las dos se cazan (vuelta 179, y el
# motivo esta MEDIDO, no supuesto). La primera version de esta guarda solo veia
# `N casos`, y sobre `REPORTE_V178.md` invento un rojo en su linea 189: ahi la
# prosa dice *"pasa de 5 casos a 8, los 8 pasan y los 8 caen"*, la cifra que va
# con el fichero es la 8 y la palabra `casos` solo acompana a la 5. Una guarda
# que inventa un rojo no sirve para cazar los de verdad, que es justo lo que su
# propio docstring dice, asi que se caza tambien `los N pasan`.
PATRON_CASOS = re.compile(r"(?:(\d+)\s+casos\b|los\s+(\d+)\s+pasan\b)")
PATRON_PROPIA_CASOS = re.compile(r"CIFRA casos:\s*(\d+)\s*\|\s*pasan:\s*(\d+)")
PATRON_PROPIA_CAEN = re.compile(r"CIFRA casos que CAEN:\s*(\d+)\s+de\s+(\d+)")
# LA VENTANA, ELEGIDA CONTANDO Y NO A OJO. Las siete parejas reales de
# `REPORTE_V178.md` estan a 32, 34, 36, 45, 51, 51 y 54 caracteres; 120 deja
# holgura de mas del doble sobre la mayor y sigue siendo mucho menos que un
# parrafo, que es lo que evita emparejar un fichero con la cifra de otro.
VENTANA_CITA = 120

# LA UNICA EXENCION, Y ES ESTRECHA A PROPOSITO (vuelta 179, TAREA 1.b, y la
# destapo la propia guarda al cerrar el reporte que la estrena). LA CASA OBLIGA A
# CITAR LA CIFRA EQUIVOCADA: `EJECUTOR.md` 8 dice que toda correccion se declara
# SIN BORRAR EL TEXTO VIEJO, porque "una correccion que tapa lo que corrige no se
# puede auditar". Un reporte que corrige un 16 por un 18 TIENE que escribir el 16
# al lado de su fichero, y sin esta exencion la guarda lo acusaria por hacer
# exactamente lo que la doctrina manda.
#
# SE PAGA CON UNA PALABRA Y NO CON UN SILENCIO: el parrafo tiene que DECIR el
# literal, y entonces la cita se publica igual, con su motivo, pero no cuenta como
# rojo. Una exencion que se coge sin declararla seria un agujero; esta hay que
# pedirla por escrito y queda escrita en el reporte.
MARCA_CORRECCION = "CORRECCION DECLARADA"


def sha(t):
    return hashlib.sha256(t.replace(chr(13) + NL, NL).encode("utf-8")).hexdigest()


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def rel(ruta):
    return os.path.relpath(ruta, RAIZ).replace(os.sep, "/")


def lector_de_docs_loop(nombre):
    """EL LECTOR DE VERDAD que `citas_de_arnes_que_no_calzan()` usa cuando la
    llama `main()`. Devuelve el texto del fichero, la cadena vacia si mide cero
    bytes, o None si no existe. NO ES PURO a proposito: es la unica pieza de
    esta guarda que toca el disco, y por eso va separada de la funcion que
    juzga, que si lo es y por eso se puede tumbar en un arnes."""
    ruta = os.path.join(RAIZ, "docs", "loop", nombre)
    if not os.path.exists(ruta):
        return None
    if os.path.getsize(ruta) == 0:
        return ""
    return leer(ruta)


def vuelta_de_fichero(nombre):
    """El numero de vuelta que lleva dentro un `SALIDA_V<N>_BATERIA...`, o None
    si el nombre no dice de que vuelta es. PURA."""
    if not nombre:
        return None
    m = PATRON_FICHERO_BATERIA.search(nombre)
    return int(m.group(1)) if m else None


def rama_de_la_seccion9(lineas_bateria, nombre_bateria, vuelta):
    """QUE RAMA LE TOCA A LA SECCION 9, Y POR QUE. Devuelve (rama, motivo) con
    rama en `CORRIDA`, `HUECO` o `ROJO`.

    NACE EN LA VUELTA 182 COMO REMEDIO DEL `E.1` DEL ACTA 180, y nace FUERA de
    `main()` a proposito. Mientras esta decision vivio dentro de `main()` no se
    podia probar sin escribir un reporte entero, y por eso nadie la probo: el
    reporte de la 180 salio diciendo CORRIDA ENTERA Y SOLA sobre una seccion cuyo
    cuerpo decia que nadie la corrio.

    LAS TRES REGLAS, EN ORDEN, Y LA PRIMERA ES LA QUE FALTABA:

      1. SI EL NOMBRE NO DICE DE QUE VUELTA ES, ES ROJO. Antes esto era silencio:
         `vuelta_de_fichero()` devolvia None y la guarda de vuelta ajena se
         saltaba porque su condicion pedia `ajena is not None`. Un fichero de
         bateria anonimo NO cierra un reporte (`banco 9`, fallar ruidoso).
      2. SI EL NOMBRE DICE OTRA VUELTA, ES ROJO. Esta ya existia y se conserva
         palabra por palabra: una corrida de otra vuelta no cierra este reporte.
      3. SI EL NOMBRE NO ES EL DE UNA CORRIDA, ES `HUECO` AUNQUE TRAIGA LINEAS.
         `SALIDA_V<N>_BATERIA...` es el nombre de una corrida;
         `SALIDA_V<N>_HUECO_BATERIA` no lo es. ESTA ES LA REGLA QUE LE FALTABA A
         LA 180: su fichero era de la vuelta 180 y traia 21 lineas, asi que ni la
         identidad ni el conteo lo paraban, y la cabecera salio diciendo CORRIDA
         ENTERA Y SOLA sobre un cuerpo que decia lo contrario.
      4. SOLO ENTONCES SE MIRA SI TRAE LINEAS. Con lineas, `CORRIDA`; sin lineas,
         `HUECO`, que es la rama donde vive `hueco_declarado_que_falta()`.

    LA RAMA DE CORRIDA SE VUELVE MAS ESTRECHA, NO MAS ANCHA: antes bastaba con
    traer lineas, ahora hay que traer lineas Y ser de esta vuelta.

    PURA: no lee ni escribe nada, para que su arnes la pueda tumbar caso por caso
    sin tocar el repo."""
    if vuelta is None:
        return "ROJO", ("no se dijo de que vuelta es este reporte, y sin eso no se "
                        "puede juzgar ninguna bateria")
    ajena = vuelta_de_fichero(nombre_bateria)
    if ajena is None:
        return "ROJO", ("el fichero de bateria %r no dice de que vuelta es. Un "
                        "fichero anonimo NO cierra un reporte: se llama "
                        "SALIDA_V<N>_BATERIA o no vale" % (nombre_bateria,))
    if ajena != vuelta:
        return "ROJO", ("el fichero de bateria que se pasa es el de la vuelta %d y "
                        "se esta cerrando la %d. UNA CORRIDA DE OTRA VUELTA NO "
                        "CIERRA ESTE REPORTE." % (ajena, vuelta))
    if not PATRON_NOMBRE_DE_CORRIDA.match(os.path.basename(nombre_bateria)):
        return "HUECO", ("el fichero %r es de la vuelta %d pero NO se llama como "
                         "una corrida: una corrida se llama SALIDA_V<N>_BATERIA y "
                         "esto no lo es, asi que no puede declararse corrida por "
                         "mucho que traiga lineas"
                         % (os.path.basename(nombre_bateria), vuelta))
    if lineas_bateria:
        return "CORRIDA", ("la bateria de la vuelta %d trae %d linea(s) no vacias"
                           % (vuelta, len(lineas_bateria)))
    return "HUECO", ("la bateria de la vuelta %d no corrio: su fichero no existe o "
                     "esta vacio" % vuelta)


def hueco_declarado_que_falta(seccion9, vuelta):
    """LO QUE LE FALTA A UN HUECO PARA ESTAR DECLARADO Y MEDIDO. Devuelve la
    lista de motivos, VACIA si el hueco esta completo.

    LAS TRES COSAS TIENEN QUE VENIR JUNTAS (adjudicacion 6.2 del acta 172): el
    NOMBRE DEL FICHERO, sus BYTES MEDIDOS y la ATRIBUCION. Traer dos de tres no
    es un hueco declarado a medias: es un hueco que no cuenta.

    PURA a proposito, como su hermana `piezas_que_faltan()`: recibe el texto de
    la seccion 9 y el numero de vuelta, y no lee ni escribe nada. Asi su caso
    positivo por mutacion la puede tumbar motivo a motivo sin tocar el repo."""
    if vuelta is None:
        return ["no se dijo de que vuelta es este reporte, y sin eso un hueco no "
                "se puede juzgar"]
    if MARCA_HUECO not in seccion9:
        return ["LA AUSENCIA ES MUDA: la seccion 9 no declara ningun hueco (no "
                "trae la marca %r)" % MARCA_HUECO]
    motivos = []

    nombrados = sorted(set(int(n) for n in PATRON_FICHERO_BATERIA.findall(seccion9)))
    if not nombrados:
        motivos.append("el hueco no nombra el fichero de la bateria")
    elif vuelta not in nombrados:
        motivos.append("el hueco no nombra la bateria de la vuelta %d" % vuelta)
    ajenas = [n for n in nombrados if n != vuelta]
    if ajenas:
        motivos.append("la seccion 9 trae la bateria de la vuelta %s, que es UNA "
                       "CORRIDA DE OTRA VUELTA"
                       % ", ".join(str(n) for n in ajenas))

    if not PATRON_BYTES.search(seccion9):
        motivos.append("el hueco no trae sus bytes medidos")

    atribucion = ""
    if MARCA_ATRIBUCION in seccion9:
        atribucion = seccion9.split(MARCA_ATRIBUCION, 1)[1].split(NL, 1)[0].strip()
    if not atribucion:
        motivos.append("el hueco no trae atribucion de quien si la corrio ni "
                       "declaracion de que no la corrio nadie")
    return motivos


def parrafos_fuera_de_cerca(texto):
    """LOS PARRAFOS DEL REPORTE QUE NO SON CITA, con la linea en que empieza
    cada uno y el mapa de sus saltos.

    Devuelve [(linea_de_inicio, texto_del_parrafo, [(numero, renglon), ...])].
    Un parrafo es una racha de renglones no vacios; el texto va unido con un
    espacio, porque el markdown parte las frases donde le cabe el ancho y la
    frase es la unidad que este fichero juzga. PURA."""
    parrafos = []
    dentro = False
    actual = []

    def cerrar():
        if actual:
            parrafos.append((actual[0][0],
                             " ".join(r for _n, r in actual),
                             list(actual)))
            del actual[:]

    for n, linea in enumerate(texto.split(NL), 1):
        if linea.lstrip().startswith(CERCA):
            dentro = not dentro
            cerrar()
            continue
        if dentro:
            continue
        if not linea.strip():
            cerrar()
            continue
        actual.append((n, linea.strip()))
    cerrar()
    return parrafos


def cifra_propia_del_arnes(texto_del_fichero):
    """LA CIFRA DE CASOS QUE UN FICHERO DE SALIDA DE ARNES DICE DE SI MISMO.

    Devuelve (total, forma), o (None, "") si el fichero no publica ninguna de
    las dos formas que la casa escribe. PURA: recibe el texto.

    LAS DOS FORMAS, Y DE DONDE SALE EL TOTAL EN CADA UNA:
      . `CIFRA casos: X | pasan: Y`        -> el total es X.
      . `CIFRA casos que CAEN: X de Y`     -> el total es Y, porque X son los
                                              que caen y Y los que hay.
    Se mira primero la primera, que es la que nombra el total sin rodeos."""
    if not texto_del_fichero:
        return None, ""
    m = PATRON_PROPIA_CASOS.search(texto_del_fichero)
    if m:
        return int(m.group(1)), m.group(0).strip()
    m = PATRON_PROPIA_CAEN.search(texto_del_fichero)
    if m:
        return int(m.group(2)), m.group(0).strip()
    return None, ""


def emparejar_citas(parrafo):
    """QUE CIFRA DE CASOS VA CON QUE FICHERO DENTRO DE UN PARRAFO.

    Devuelve [(publicada, ruta, distancia_en_caracteres)]. PURA.

    LA REGLA, ESCRITA AQUI PARA QUE NO HAYA QUE DEDUCIRLA DE LA SALIDA, y es la
    que el encargo pide ("en la misma frase o en la misma linea") sin depender
    de partir frases, que en markdown no se puede hacer sin equivocarse: CADA
    FICHERO SE EMPAREJA CON LA CIFRA DE CASOS QUE TIENE MAS CERCA EN SU MISMO
    PARRAFO, y cada cifra se gasta una sola vez. Se recorren todas las parejas
    posibles de menor a mayor distancia y se van tomando las que no pisan a
    ninguna ya tomada.

    POR QUE ASI Y NO POR PARRAFO ENTERO, y el ejemplar esta medido en
    `docs/loop/reportes/REPORTE_V178.md`: sus lineas 239 y 241 viven en el MISMO
    parrafo, publican DOS cifras (20 y 28) y nombran UN SOLO fichero, que es el
    de la de 28. Emparejar por parrafo acusaria a la de 20 de no calzar con un
    fichero que no es el suyo, y una guarda que inventa un rojo no sirve para
    cazar los de verdad.

    Y LA VENTANA: si la mas cercana esta a mas de VENTANA_CITA caracteres, no se
    empareja. Un fichero y una cifra separados por medio parrafo no estan en la
    misma frase, y este fichero prefiere callarse a acusar."""
    cifras = [(m.start(), int(m.group(1) or m.group(2)))
              for m in PATRON_CASOS.finditer(parrafo)]
    ficheros = [(m.start(), m.group(0)) for m in PATRON_SALIDA_TXT.finditer(parrafo)]
    if not cifras or not ficheros:
        return []
    posibles = []
    for pf, ruta in ficheros:
        for pc, valor in cifras:
            posibles.append((abs(pf - pc), pf, pc, ruta, valor))
    posibles.sort()
    usados_f, usados_c, salida = set(), set(), []
    for dist, pf, pc, ruta, valor in posibles:
        if pf in usados_f or pc in usados_c or dist > VENTANA_CITA:
            continue
        usados_f.add(pf)
        usados_c.add(pc)
        salida.append((valor, ruta, dist))
    return salida


def citas_de_arnes_que_no_calzan(texto, leer_fichero):
    """LA PROSA QUE PUBLICA UNA CIFRA DE CASOS Y NOMBRA EL FICHERO DE DONDE
    DEBERIA SALIR, COTEJADA CONTRA ESE FICHERO.

    Devuelve [(linea, ruta, publicada, propia, motivo)], VACIA si todas las
    citas calzan. PURA A PROPOSITO, como sus hermanas de este fichero: recibe el
    texto del reporte y UN LECTOR, `leer_fichero(nombre) -> texto o None`, para
    que su caso positivo por mutacion pueda tumbarla sin tocar el repo ni leer
    nada de disco. El lector devuelve None si el fichero no existe y la cadena
    vacia si mide cero bytes.

    POR QUE NACE, Y NO ES UNA IDEA NUEVA SINO UNA ORDEN PENDIENTE. `AUDITOR.md`
    1.2 obliga a encargar la extension del tallador a las fases mecanicas cuando
    la racha de caidas de reporte llega a dos, y llego (acta 178, seccion 6). El
    alcance lo autorizo el fundador el 29 ago 2026
    (`paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md`): *"toda tabla y
    toda cifra del reporte en fases mecanicas se genera contando su fichero de
    salida"*. La cabecera y las tablas ya se tallan; LO QUE FALTABA ERA LA PROSA
    QUE CITA UN FICHERO, que es por donde entraron las dos ultimas caidas.

    EL EJEMPLAR QUE LA MOTIVA, MEDIDO Y NO SUPUESTO: la linea 349 de
    `docs/loop/reportes/REPORTE_V178.md` publica *"16 casos, los 16 pasan y los
    16 CAEN"* citando `docs/loop/SALIDA_V178_T1E_MUTACION.txt`, y ese fichero,
    contado, dice `CIFRA casos: 18 | pasan: 18 | fallan: 0`.

    LOS TRES MOTIVOS DE ROJO, y son los del encargo:
      (1) LA CIFRA NO CALZA con la que el fichero publica de si mismo;
      (2) EL FICHERO CITADO NO EXISTE;
      (3) EL FICHERO CITADO MIDE CERO BYTES.
    Los dos ultimos por la letra del 5 sep 2026 de `EJECUTOR.md` 1, LA RUTA QUE
    PROMETE PRUEBA ES CIFRA: una ruta publicada como evidencia cuenta como cifra
    publicada en su sede.

    LO QUE NO ES ROJO, Y SE DICE EN VEZ DE CALLARLO: un fichero que existe, no
    esta vacio y NO publica ninguna de las dos formas de cifra propia. Ahi no
    hay nada que no calce, y fabricar un rojo sobre lo que no se puede cotejar
    seria lo mismo que la casa condena en el otro sentido. Ese caso sale con
    motivo SIN COTEJO y el que llama decide; `main()` lo imprime y NO lo suma a
    los rojos.

    QUEDA FUERA lo cercado con tres comillas invertidas, por el mismo motivo que
    la guarda de la pareja: ahi va pegada la salida cruda del instrumento, que
    es una CITA, y una cita que se retoca deja de ser una cita."""
    fallos = []
    for linea0, parrafo, renglones in parrafos_fuera_de_cerca(texto):
        for publicada, ruta, _dist in emparejar_citas(parrafo):
            # LA LINEA QUE SE NOMBRA es aquella en que aparece la ruta citada,
            # buscada renglon a renglon; si no se encuentra, la del parrafo.
            n = linea0
            for num, renglon in renglones:
                if ruta in renglon:
                    n = num
                    break
            contenido = leer_fichero(ruta)
            if contenido is None:
                fallos.append((n, ruta, publicada, None,
                               "EL FICHERO CITADO NO EXISTE, y una ruta publicada "
                               "como prueba es una cifra publicada"))
                continue
            if not contenido.strip():
                fallos.append((n, ruta, publicada, None,
                               "EL FICHERO CITADO MIDE CERO BYTES, y una ruta que "
                               "promete prueba y no la trae es caida de cifra"))
                continue
            propia, forma = cifra_propia_del_arnes(contenido)
            if propia is None:
                fallos.append((n, ruta, publicada, None,
                               "SIN COTEJO: el fichero no publica ninguna de las dos "
                               "formas de cifra propia, y no se fabrica un rojo sobre "
                               "lo que no se puede cotejar"))
                continue
            if propia != publicada:
                if MARCA_CORRECCION in parrafo:
                    fallos.append((n, ruta, publicada, propia,
                                   "SIN COTEJO por %s: el parrafo declara que la "
                                   "cifra publicada (%d) es LA QUE SE CORRIGE y no "
                                   "la que se afirma; la del fichero es %d"
                                   % (MARCA_CORRECCION, publicada, propia)))
                    continue
                fallos.append((n, ruta, publicada, propia,
                               "LA CIFRA PUBLICADA NO ES LA DEL FICHERO: el reporte "
                               "dice %d y su propio fichero, contado, dice %d (%s)"
                               % (publicada, propia, forma)))
    return fallos


def cifras_sin_pareja(texto):
    """LAS CIFRAS DE BYTES Y LOS SHA QUE EL REPORTE PUBLICA SIN SU PAREJA.

    Devuelve [(numero_de_linea, especie, muestra, linea)], VACIA si todas van
    emparejadas. PURA a proposito, como sus hermanas de este fichero: recibe el
    texto y no lee ni escribe nada, para que su caso positivo por mutacion la
    pueda tumbar caso a caso sin tocar el repo.

    LA REGLA, ESCRITA AQUI PARA QUE NO HAYA QUE DEDUCIRLA DE LA SALIDA: una
    cifra esta emparejada si en su MISMA LINEA hay dos o mas apariciones de su
    especie, o si la linea nombra al menos DOS marcas de convencion. Los bloques
    cercados quedan fuera porque son citas de la salida de un instrumento."""
    fallos = []
    dentro_de_cerca = False
    for n, linea in enumerate(texto.split(NL), 1):
        if linea.lstrip().startswith(CERCA):
            dentro_de_cerca = not dentro_de_cerca
            continue
        if dentro_de_cerca:
            continue
        marcas = sum(1 for m in MARCAS_CONVENCION if m in linea)
        for especie, hits in (("bytes", PATRON_BYTES.findall(linea)),
                              ("sha", PATRON_SHA.findall(linea)
                               if "sha" in linea.lower() else [])):
            if not hits:
                continue
            if len(hits) >= 2 or marcas >= 2:
                continue
            fallos.append((n, especie, hits[0], linea.strip()[:120]))
    return fallos


def piezas_que_faltan(texto, filas_tallador, lineas_bateria,
                      vuelta=None, nombre_bateria=None):
    """LAS CUATRO PIEZAS, COMPROBADAS SOBRE EL TEXTO YA ESCRITO. Devuelve la
    lista de las que FALTAN, vacia si estan las cuatro.

    PURA A PROPOSITO: recibe el texto del reporte, las filas de la cabecera
    tallada y las lineas no vacias de la salida de la bateria, para que su caso
    positivo por mutacion pueda tumbarla una a una **sin tocar el repo y sin
    escribir nada**. Si esto viviera dentro del cuerpo de una funcion que
    escribe, no habria nada que un arnes pudiera llamar, y una guarda que no se
    puede llamar no se puede probar."""
    faltan = []

    # (1) EL VEREDICTO ESCRITO
    if (VEREDICTO_VIEJO in texto
            or "**EL VEREDICTO DE UNA LINEA:" not in texto):
        faltan.append("(1) el veredicto de una linea no esta escrito")

    # (2) LA CABECERA PEGADA
    if HUECO_CABECERA in texto:
        faltan.append("(2) el hueco de la cabecera sigue sin rellenar")
    elif not filas_tallador:
        faltan.append("(2) el fichero del tallador no trae ninguna fila de tabla")
    else:
        fuera = [f for f in filas_tallador if f.rstrip() not in texto]
        if fuera:
            faltan.append("(2) %d fila(s) de la cabecera tallada no estan pegadas"
                          % len(fuera))

    # (3) LAS SECCIONES 3 A 9
    ausentes = [k for k in range(3, 10) if (NL + "## %d." % k) not in texto]
    if ausentes:
        faltan.append("(3) faltan las secciones %s"
                      % ", ".join(str(k) for k in ausentes))

    # (4) LA BATERIA DENTRO DE LA SECCION 9, O EL HUECO DECLARADO Y MEDIDO
    if (NL + "## 9.") not in texto:
        faltan.append("(4) no hay seccion 9 donde meter la bateria")
    else:
        seccion9 = texto[texto.index(NL + "## 9."):]
        if lineas_bateria:
            fuera = [l for l in lineas_bateria if l.rstrip() not in seccion9]
            if fuera:
                faltan.append("(4) %d linea(s) de la bateria no estan dentro de la "
                              "seccion 9" % len(fuera))
            else:
                ajena = vuelta_de_fichero(nombre_bateria)
                if vuelta is not None and ajena is not None and ajena != vuelta:
                    faltan.append("(4) la salida pegada en la seccion 9 es la de la "
                                  "vuelta %d y no la de la %d: UNA CORRIDA DE OTRA "
                                  "VUELTA NO SATISFACE ESTA PIEZA" % (ajena, vuelta))
        else:
            motivos = hueco_declarado_que_falta(seccion9, vuelta)
            if motivos:
                faltan.append("(4) la bateria no esta y el hueco no vale: %s"
                              % "; ".join(motivos))
    return faltan


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--cuerpo", required=True)
    ap.add_argument("--tallador", required=True)
    ap.add_argument("--bateria", required=True)
    ap.add_argument("--veredicto", required=True)
    ap.add_argument("--hueco-atribucion", dest="hueco_atribucion", default="",
                    help="LA ATRIBUCION DEL HUECO. Solo se usa cuando la salida "
                         "de la bateria de ESTA vuelta esta vacia o no existe. "
                         "Sin ella, una bateria vacia sigue siendo ROJO: la "
                         "ausencia muda no cierra ningun reporte.")
    a = ap.parse_args()
    V = a.vuelta

    print("=" * 78)
    print("SE CIERRA EL REPORTE DE LA VUELTA %d, EN UN SOLO ACTO" % V)
    print("=" * 78)
    print("")
    rojos = []

    print("A) EL SUJETO, COMPROBADO ANTES DE TOCARLO")
    texto = leer(REPORTE)
    primera = texto.split(NL, 1)[0]
    print("   %s primera linea: %s" % (rel(REPORTE), primera[:88]))
    m = re.match(r"^#\s*REPORTE DE LA VUELTA\s+(\d+)\b", primera)
    if not m or int(m.group(1)) != V:
        rojos.append("el REPORTE.md del arbol no es el de la vuelta %d" % V)
    print("   CIFRA bytes: %d | saltos de linea: %d"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    for marca, esperado in ((VEREDICTO_VIEJO, True), (HUECO_CABECERA, True),
                            (NL + "## 3.", False), (NL + "## 9.", False)):
        hay = marca in texto
        print("   contiene %-36r -> %s (se esperaba %s)"
              % (marca[:34], "SI" if hay else "NO", "SI" if esperado else "NO"))
        if hay != esperado:
            rojos.append("el sujeto no esta en el estado de un reporte SIN CERRAR: %r"
                         % marca[:36])
    print("")

    print("B) LAS TRES PIEZAS QUE VIENEN DE FUERA, MEDIDAS ANTES DE PEGARLAS")
    tallador = leer(os.path.join(RAIZ, a.tallador.replace("/", os.sep)))
    filas = [l.rstrip() for l in tallador.split(NL) if l.strip().startswith("|")]
    print("   %-52s %7d bytes, %d filas de tabla"
          % (a.tallador, len(tallador.encode("utf-8")), len(filas)))
    if len(filas) < 8:
        rojos.append("el fichero del tallador trae %d filas de tabla, muy pocas" % len(filas))

    cuerpo = leer(os.path.join(RAIZ, a.cuerpo.replace("/", os.sep)))
    print("   %-52s %7d bytes, sha256 %s"
          % (a.cuerpo, len(cuerpo.encode("utf-8")), sha(cuerpo)[:16]))
    secciones = [l for l in cuerpo.split(NL) if l.startswith("## ")]
    for l in secciones:
        print("      %s" % l[:92])
    if not cuerpo.startswith("## 3."):
        rojos.append("el borrador del cierre no empieza por la seccion 3")

    ruta_bat = os.path.join(RAIZ, a.bateria.replace("/", os.sep))
    existe = os.path.exists(ruta_bat)
    tam = os.path.getsize(ruta_bat) if existe else -1
    print("   %-52s %s" % (a.bateria, ("%d bytes" % tam) if existe else "NO EXISTE"))
    bateria = leer(ruta_bat) if existe and tam > 0 else ""
    tam_lf = len(bateria.encode("utf-8"))
    lineas_bat = [l for l in bateria.split(NL) if l.strip()]
    print("   CIFRA lineas no vacias de la bateria: %d" % len(lineas_bat))
    ajena = vuelta_de_fichero(a.bateria)
    print("   vuelta que lleva dentro el nombre del fichero: %s" % ajena)
    # LA DECISION DE RAMA YA NO SE TOMA AQUI: la toma rama_de_la_seccion9(), que
    # es pura y tiene arnes propio. REMEDIO DEL `E.1` DEL ACTA 180, vuelta 182.
    rama, motivo_rama = rama_de_la_seccion9(lineas_bat, a.bateria, V)
    print("   RAMA DE LA SECCION 9, decidida por rama_de_la_seccion9(): %s" % rama)
    print("      motivo: %s" % motivo_rama)
    if rama == "ROJO":
        rojos.append(motivo_rama)
    atribucion = a.hueco_atribucion.strip()
    if rama == "HUECO":
        print("   LA BATERIA DE ESTA VUELTA NO CORRIO. Se mira la atribucion:")
        print("   --hueco-atribucion: %s"
              % (repr(atribucion) if atribucion else "(vacia)"))
        if not atribucion:
            rojos.append("la salida de la bateria de la vuelta %d esta vacia o no "
                         "existe y NO SE DECLARO NINGUNA ATRIBUCION. La ausencia "
                         "muda no cierra un reporte: o va la bateria, o va un "
                         "HUECO DECLARADO Y MEDIDO con --hueco-atribucion." % V)
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for r in rojos:
            print("   " + r)
        return 1

    print("C) SE ESCRIBE")
    bloque_cabecera = (
        MARCA_ABRE + NL +
        "**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio" + NL +
        "de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %d`, y su salida" % V + NL +
        "cruda vive en `%s` (%d bytes en disco y %d normalizado a LF, %d filas de"
        % (a.tallador, os.path.getsize(os.path.join(RAIZ, a.tallador.replace("/", os.sep))),
           len(tallador.encode("utf-8")), len(filas)) + NL +
        "tabla," + NL +
        "contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN" + NL +
        "INSTRUMENTO NO SE ESCRIBE.**" + NL + NL +
        NL.join(filas) + NL + NL +
        MARCA_CIERRA + NL)
    i0 = texto.index(MARCA_ABRE)
    i1 = texto.index(MARCA_CIERRA) + len(MARCA_CIERRA) + 1
    texto = texto[:i0] + bloque_cabecera + texto[i1:]
    print("   cabecera: %d bytes de hueco -> %d bytes de tabla pegada"
          % (i1 - i0, len(bloque_cabecera.encode("utf-8"))))

    veredicto = "**EL VEREDICTO DE UNA LINEA: %s**" % a.veredicto.strip()
    i = texto.index(VEREDICTO_VIEJO)
    j = texto.index(NL + NL, i)
    texto = texto[:i] + veredicto + texto[j + 1:]
    print("   veredicto escrito: %d bytes" % len(veredicto.encode("utf-8")))

    if rama == "CORRIDA":
        seccion9 = (
            CAB_9 + NL + NL +
            "**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**" + NL +
            "Fichero: `%s` (**%d bytes en disco y %d normalizado a LF**, **%d lineas"
            % (a.bateria, tam, len(bateria.encode("utf-8")), len(lineas_bat)) + NL +
            "no vacias**, contadas" + NL +
            "por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta" + NL +
            "seccion se queda sin ella**, que es la cuarta de sus cuatro piezas." + NL + NL +
            "```" + NL + bateria.rstrip(NL) + NL + "```" + NL)
    else:
        # EL HUECO SE DECLARA Y NO SE RELLENA. Las tres cosas van juntas, y las
        # dos primeras SE MIDEN AQUI con os.path.getsize: ninguna se teclea.
        seccion9 = (
            CAB_9_HUECO + NL + NL +
            "**%s. LA BATERIA DE LA VUELTA %d NO CORRIO, Y EL HUECO SE DECLARA EN VEZ"
            % (MARCA_HUECO, V) + NL +
            "DE RELLENARSE CON OTRA COSA.**" + NL + NL +
            "**EL NOMBRE DEL FICHERO:** `%s`." % a.bateria + NL +
            "**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por" + NL +
            "`scripts/loop/cerrar_reporte.py`, no tecleados, y POR LAS DOS" + NL +
            "CONVENCIONES mientras la del fundador no este fijada:" + NL +
            "**%d bytes en disco y %d bytes normalizados a LF**."
            % (max(tam, 0), max(tam_lf, 0)) + NL + NL +
            "%s %s" % (MARCA_ATRIBUCION, atribucion) + NL + NL +
            "**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este" + NL +
            "instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b" + NL +
            "(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es" + NL +
            "estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**." + NL +
            "Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y" + NL +
            "**una corrida de otra vuelta pegada aqui tampoco vale**." + NL)

    texto = texto.rstrip(NL) + NL + NL + cuerpo.rstrip(NL) + NL + NL + seccion9
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
    print("   ESCRITO: %s (%d bytes, %d saltos de linea)"
          % (rel(REPORTE), len(texto.encode("utf-8")), texto.count(NL)))
    print("")

    print("D) SE RELEE DEL DISCO Y SE MIRAN LAS CUATRO PIEZAS")
    de_nuevo = leer(REPORTE)
    faltan = piezas_que_faltan(de_nuevo, filas, lineas_bat,
                               vuelta=V, nombre_bateria=a.bateria)
    for etiqueta in ("(1) veredicto escrito", "(2) cabecera pegada",
                     "(3) secciones 3 a 9",
                     "(4) bateria dentro de la 9 o hueco declarado"):
        codigo = etiqueta[:3]
        mal = [f for f in faltan if f.startswith(codigo)]
        print("   %-34s %s" % (etiqueta, "SI" if not mal else "NO: " + mal[0]))
    print("   CIFRA piezas que faltan: %d" % len(faltan))
    extra = 0
    huerfanas = cifras_sin_pareja(de_nuevo)
    citas = citas_de_arnes_que_no_calzan(de_nuevo, lector_de_docs_loop)
    citas_rojas = [c for c in citas if not c[4].startswith("SIN COTEJO")]
    for etiqueta, cond in (
            ("el cuerpo del cierre esta byte a byte", cuerpo.rstrip(NL) in de_nuevo),
            ("cero guiones largos y cero guiones medios",
             chr(8212) not in de_nuevo and chr(8211) not in de_nuevo),
            ("toda cifra de bytes y todo sha con su pareja", not huerfanas),
            ("toda cita de arnes calza con su fichero", not citas_rojas)):
        print("   %-34s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            extra += 1
    if huerfanas:
        print("   LAS CIFRAS SIN PAREJA, UNA A UNA (vuelta 178, TAREA 1.e):")
        for n, especie, muestra, linea in huerfanas:
            print("      linea %-5d %-5s %-20s | %s" % (n, especie, muestra, linea))
    print("   CIFRA cifras publicadas sin su pareja: %d" % len(huerfanas))
    if citas:
        print("   LAS CITAS DE ARNES, UNA A UNA (vuelta 179, TAREA 1.b):")
        for n, ruta, publicada, propia, motivo in citas:
            print("      linea %-5d %-38s publicada %s | del fichero %s"
                  % (n, ruta, publicada, propia if propia is not None else "(no medible)"))
            print("         %s" % motivo)
    print("   CIFRA citas de arnes cotejadas que NO calzan: %d" % len(citas_rojas))
    print("   CIFRA citas de arnes SIN COTEJO posible: %d" % (len(citas) - len(citas_rojas)))
    print("")
    if faltan or extra:
        print("ROJO: al reporte de la vuelta %d le faltan %d de sus cuatro piezas."
              % (V, len(faltan)))
        for f in faltan:
            print("   " + f)
        return 1
    print("VERDE: el reporte de la vuelta %d queda cerrado, con sus cuatro piezas." % V)
    print("   LA SEGUNDA COMPROBACION (leer de git lo que se acaba de commitear)")
    print("   NO la hace este fichero: va DESPUES del commit, con git show.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
