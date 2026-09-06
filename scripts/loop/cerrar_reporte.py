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
import subprocess
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
# EL CARRIL DE CIERRE TARDIO (vuelta 186, TAREA 2.c; respuesta del acta 186 a la
# `P.2`). La cabecera y la marca van aqui arriba, con las demas, para que un
# arnes pueda nombrarlas sin teclearlas.
CAB_10_TARDIO = ("## 10. LAS CIFRAS SIN PAREJA, DECLARADAS UNA A UNA POR EL "
                 "CARRIL DE CIERRE TARDIO")
MARCA_TARDIO = "CIFRAS SIN PAREJA DECLARADAS Y MEDIDAS:"
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

# LA SEPTIMA COMPROBACION, Y ES LA OPERACION DE CODIGO DE LA SEGUNDA ESCALADA
# (vuelta 183, TAREA 1.c). `AUDITOR.md` 1.2 vuelve a obligar: la racha de caidas
# de reporte llego a DOS con el `E.1` del acta 182, y la extension queda
# AUTOMATICAMENTE ENCARGADA sin esperar decision nueva.
#
# EL EJEMPLAR, MEDIDO Y NO SUPUESTO: `docs/loop/reportes/REPORTE_V182.md:46`
# publica como veredicto de una linea *"[...] Y LAS SEIS CAIDAS QUE COMETI VAN
# CON SU NOMBRE [...]"*, y su seccion 8 lista SIETE cabeceras `C.1` a `C.7`. El
# propio cierre de esa seccion dice *"NINGUNA DE LAS SIETE SE TAPA"*. O sea: el
# reporte se contradice consigo mismo en la unica linea que un lector apurado va
# a leer, y ninguna guarda lo vio porque el veredicto es LO ULTIMO que se teclea
# y no salia de ningun tallador.
#
# LA FIGURA ES LA DEL TALLADOR DEL 26 AGO 2026
# (`paradas/2026-08-26-racha-hash-apertura-DECISION.md`): LO QUE SE TECLEA SE
# COTEJA CONTRA LO QUE SE PUEDE CONTAR. El veredicto sigue siendo prosa del
# ejecutor (no se talla, porque es un juicio y no una celda), pero sus NUMERALES
# se cuentan contra el cuerpo, y si no calzan EL CIERRE NO ESCRIBE NADA.
#
# LOS NUMERALES SE LEEN TAMBIEN ESCRITOS CON LETRA, que es como el veredicto los
# escribe siempre: sin esto la guarda no morderia en el unico caso que la trae.
PALABRA_A_NUMERO = {
    "cero": 0, "un": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
}
# LAS DOS ESPECIES QUE EL CUERPO PERMITE CONTAR HOY, y se dice "hoy" a proposito:
# el encargo pide "como minimo" estas dos, y anadir una tercera es anadir una
# entrada aqui mas su contador, no reescribir la guarda.
SUSTANTIVO_A_ESPECIE = {
    "caida": "caidas", "caidas": "caidas",
    "tarea": "tareas", "tareas": "tareas",
}
PATRON_NUMERAL = re.compile(
    r"(?<![\w.,])(\d+|%s)\s+(caidas?|tareas?)\b"
    % "|".join(sorted(PALABRA_A_NUMERO, key=len, reverse=True)),
    re.IGNORECASE)
# LA CABECERA DE UNA CAIDA PROPIA. El acta 182 y el reporte 182 la escriben como
# ``**`C.1`. TITULO``; se admite sin backticks por si algun reporte los deja.
PATRON_CAIDA_PROPIA = re.compile(r"^\s*\*{0,2}`?C\.(\d+)`?\s*[.,]")
CAB_8 = "## 8."
MARCA_TABLA_ABRE = "<!-- TABLA DE TAREAS -->"
MARCA_TABLA_CIERRA = "<!-- FIN TABLA DE TAREAS -->"


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


def vuelta_que_sello(asunto):
    """EL NUMERO DE VUELTA QUE NOMBRA EL ASUNTO DE UN COMMIT (`VUELTA <N>`), o
    None si no lo nombra. PURA.

    NACE EN LA VUELTA 185, TAREA 1.c, y la 1.d la reusa IMPORTANDOLA en vez de
    copiarla: la columna `quien lo sello` de la tabla de los nueve tramos estaba
    TECLEADA con un `n <= 4` (caida de reporte `R.1` del acta 185), y una
    frontera tecleada caduca sola. Desde aqui, la vuelta que sello un fichero se
    LEE del asunto de su ultimo commit.

    SI EL ASUNTO NOMBRA LA VUELTA DOS VECES SE DEVUELVE LA PRIMERA, y se dice en
    vez de dejarlo al azar: el asunto de esta casa empieza por `VUELTA <N>,` y
    esa primera es la que identifica la vuelta que escribio el commit; las que
    vengan detras son citas de otras vueltas dentro del mismo texto."""
    if not asunto:
        return None
    m = re.search(r"\bVUELTA\s+(\d+)", asunto)
    return int(m.group(1)) if m else None


def tramos_por_vuelta(vuelta_del_fichero):
    """QUE VUELTA SELLO CADA TRAMO DE UNA BATERIA. Devuelve
    `{numero_de_tramo: vuelta_que_sello(asunto)}` para cada
    `docs/loop/SALIDA_V<vuelta_del_fichero>_BATERIA_TRAMO_<n>.txt` que EXISTA.

    NO ES PURA a proposito, como su hermana `lector_de_docs_loop()`: es la unica
    pieza de esta guarda que toca el disco y `git log`, y por eso va separada de
    la funcion que juzga, que si lo es y por eso se puede tumbar en un arnes.

    LA EVIDENCIA SE LEE DE GIT Y NO SE PUEDE TECLEAR. `main()` la computa con
    esta funcion y NO la recibe por bandera: una evidencia que se puede teclear
    no es una evidencia."""
    reparto = {}
    if vuelta_del_fichero is None:
        return reparto
    for n in range(1, 100):
        nombre = "SALIDA_V%d_BATERIA_TRAMO_%d.txt" % (vuelta_del_fichero, n)
        ruta = os.path.join(RAIZ, "docs", "loop", nombre)
        if not os.path.exists(ruta):
            continue
        r = subprocess.run(
            ["git", "log", "-1", "--format=%s", "--",
             "docs/loop/" + nombre],
            cwd=RAIZ, capture_output=True)
        asunto = r.stdout.decode("utf-8", errors="replace").strip()
        reparto[n] = vuelta_que_sello(asunto)
    return reparto


def vuelta_en_curso():
    """LA VUELTA QUE ESTA CORRIENDO AHORA MISMO, LEIDA DEL ASUNTO DEL ULTIMO
    COMMIT. Devuelve un entero o None si el asunto no nombra ninguna vuelta.

    NO ES PURA a proposito, como sus hermanas `tramos_por_vuelta()` y
    `lector_de_docs_loop()`: es la unica pieza de este carril que toca `git log`,
    y por eso va separada de la funcion que decide, que si es pura y por eso se
    puede tumbar en un arnes.

    LA EVIDENCIA SE LEE DE GIT Y NO SE PUEDE TECLEAR (vuelta 186, TAREA 2.c;
    respuesta del acta 186 a la `P.2`). `main()` la computa con esta funcion y NO
    la recibe por bandera: no hay ninguna opcion de linea de ordenes para esto, y
    no la hay a proposito, porque una evidencia que se puede teclear no es una
    evidencia. El asunto de esta casa empieza por `VUELTA <N>,`, y
    `vuelta_que_sello()` ya sabe leerlo: se REUSA en vez de escribir otro."""
    r = subprocess.run(["git", "log", "-1", "--format=%s"],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return vuelta_que_sello(r.stdout.decode("utf-8", errors="replace").strip())


def es_cierre_tardio(vuelta_del_reporte, curso):
    """SI ESTE CIERRE ES UN CIERRE TARDIO. PURA.

    QUE ES UN CIERRE TARDIO, Y ES LITERALMENTE LO QUE EL CASO ES: un reporte que
    se cierra en una vuelta POSTERIOR A LA SUYA. El acta 186, punto `7.2`,
    contestando la `P.2`: las cifras sin pareja del reporte de la 184 *"ni se
    eximen ni se reescriben. SE DECLARAN"*, y el carril donde eso pasa es este.

    LA CONDICION SE COMPUTA Y NO SE PASA POR BANDERA: `curso` sale de
    `vuelta_en_curso()`, que lo lee del asunto del ultimo commit con `git log`.
    Si no se puede leer la vuelta en curso, ESTO NO ES UN CIERRE TARDIO: la falta
    de evidencia no abre el carril, lo cierra.

    LA LETRA ES LA DEL ENCARGO, PALABRA POR PALABRA: *"se activa solo cuando la
    vuelta que se cierra NO es la vuelta en curso"*. No se estrecha ni se ensancha
    aqui; si algun dia hiciera falta distinguir un cierre tardio de un cierre
    adelantado, esa seria doctrina nueva y no se inventa en una guarda."""
    if vuelta_del_reporte is None or curso is None:
        return False
    return curso != vuelta_del_reporte


def declaracion_de_cifras_sin_pareja(huerfanas, vuelta, curso):
    """EL BLOQUE QUE DECLARA LAS CIFRAS SIN PAREJA DENTRO DEL PROPIO REPORTE
    CERRADO, UNA A UNA Y CON SU CUENTA TOTAL. PURA: devuelve texto.

    UN DEFECTO DECLARADO Y MEDIDO NO ES UN DEFECTO EXENTO, y esa es toda la
    diferencia entre este carril y una exencion muda, que banco 9 prohibe.

    EL CERO SE DICE Y NO SE OMITE: si no hay ninguna cifra sin pareja, este bloque
    se escribe igual y dice cero. Un campo ausente y un cero contado no son lo
    mismo, que es la misma letra que la casa aplica a las caidas propias.

    LA LISTA VA DENTRO DE UN BLOQUE CERCADO a proposito: es la salida cruda de una
    guarda, y `cifras_sin_pareja()` no mira dentro de las cercas. Si fuera prosa,
    esta declaracion se acusaria a si misma en la siguiente pasada, que es
    exactamente el falso positivo que la `PD.5` acaba de cerrar."""
    p = [CAB_10_TARDIO, "",
         "**CARRIL DE CIERRE TARDIO.** Este reporte es el de la vuelta %d y se"
         % vuelta,
         "cierra en la vuelta %s, leida del asunto del ultimo commit con `git log`"
         % curso,
         "y no tecleada. En este carril **las cifras sin pareja NO bloquean el",
         "cierre, pero SE DECLARAN una a una con su linea y su cuenta total**, que",
         "es la respuesta del acta 186 a la `P.2`: *ni se eximen ni se reescriben,",
         "se declaran*. **Un defecto declarado y medido no es un defecto exento**, y",
         "reescribir el texto de una vuelta pasada seria escribir en pasado lo que",
         "no paso.",
         "",
         "**NINGUNA OTRA GUARDA SE AFLOJA EN ESTE CARRIL.** Las cuatro piezas, el",
         "cuerpo byte a byte, los guiones y las citas de arnes siguen mandando",
         "igual, y en el carril normal las cifras sin pareja siguen siendo ROJO.",
         "",
         "%s **%d** cifra(s) publicada(s) sin su pareja." % (MARCA_TARDIO,
                                                             len(huerfanas)),
         "", CERCA,
         "CIFRA cifras publicadas sin su pareja: %d" % len(huerfanas)]
    if not huerfanas:
        p.append("(ninguna: la cuenta es CERO, y se escribe en vez de omitirse)")
    for n, especie, muestra, linea in huerfanas:
        p.append("linea %-6d %-5s %-24s | %s" % (n, especie, muestra, linea))
    p += [CERCA, ""]
    return NL.join(p) + NL


def rama_de_la_seccion9(lineas_bateria, nombre_bateria, vuelta,
                        tramos_sellados_en_esta_vuelta=None):
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

    LA BATERIA CONTINUADA (vuelta 185, TAREA 1.c; adjudicacion `6.2` del acta
    185, que cierra la `PD.3`). LA GUARDA DE ARRIBA NACIO BUENA Y NO SE AFLOJA:
    nacio en la vuelta 182 contra PEDIR PRESTADA la bateria terminada de otra
    vuelta, y ese caso sigue siendo ROJO. Pero `AUDITOR.md` 6.1, decision del
    fundador del 5 sep 2026, MANDA que *"UNA VUELTA CORTADA RETOMA EN EL TRAMO
    SIGUIENTE"*, o sea que una bateria que cruza vueltas es lo que la decision
    PIDE. Cuando una guarda contradice una decision escrita del fundador, la que
    se corrige es la guarda (`AUDITOR.md` 0).

    LA RAMA NUEVA EXIGE MAS QUE LA VIEJA, NO MENOS: solo abre si se cumplen LAS
    CUATRO condiciones a la vez, y si falla CUALQUIERA cae al ROJO de siempre,
    con su texto palabra por palabra:

      1. `ajena < vuelta`. UNA BATERIA DE UNA VUELTA POSTERIOR SIEMPRE ES ROJO.
      2. `tramos_sellados_en_esta_vuelta` NO ESTA VACIO: al menos un tramo de esa
         misma bateria se sello EN LA VUELTA QUE SE ESTA CERRANDO. Esta es la
         evidencia de que la bateria se CONTINUO y no se pidio prestada, y se lee
         de `git log`, no se teclea.
      3. EL NOMBRE CASA CON `PATRON_NOMBRE_DE_CORRIDA`.
      4. TRAE LINEAS.

    EL CUARTO PARAMETRO ES OPCIONAL Y SU VALOR POR DEFECTO `None` SE COMPORTA
    EXACTAMENTE COMO ANTES, para que ningun llamador viejo cambie de conducta: el
    arnes de la vuelta 182 se corre SIN TOCARLO y tiene que seguir VERDE.

    PURA: no lee ni escribe nada, para que su arnes la pueda tumbar caso por caso
    sin tocar el repo. Quien la llama le pasa la evidencia ya leida."""
    if vuelta is None:
        return "ROJO", ("no se dijo de que vuelta es este reporte, y sin eso no se "
                        "puede juzgar ninguna bateria")
    ajena = vuelta_de_fichero(nombre_bateria)
    if ajena is None:
        return "ROJO", ("el fichero de bateria %r no dice de que vuelta es. Un "
                        "fichero anonimo NO cierra un reporte: se llama "
                        "SALIDA_V<N>_BATERIA o no vale" % (nombre_bateria,))
    # LA BATERIA CONTINUADA, INSERTADA ANTES DEL ROJO DE LA VUELTA AJENA Y CON
    # LAS CUATRO CONDICIONES A LA VEZ. Si falla cualquiera, cae al ROJO de abajo,
    # que NO se reescribe.
    sellados = tramos_sellados_en_esta_vuelta or []
    if (ajena < vuelta and sellados
            and PATRON_NOMBRE_DE_CORRIDA.match(os.path.basename(nombre_bateria))
            and lineas_bateria):
        return "CORRIDA", (
            "la bateria del fichero es de la vuelta %d y se esta cerrando la %d, "
            "pero NO ES UNA CORRIDA AJENA: ES LA MISMA BATERIA CONTINUADA. La "
            "vuelta %d sello %d de sus tramos (los tramos %s), leido del asunto "
            "de su ultimo commit con git log y no tecleado, que es lo que "
            "AUDITOR.md 6.1 manda cuando dice que una vuelta cortada RETOMA EN "
            "EL TRAMO SIGUIENTE. Trae %d linea(s) no vacias."
            % (ajena, vuelta, vuelta, len(sellados),
               ", ".join(str(x) for x in sorted(sellados)), len(lineas_bateria)))
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


def caidas_propias_del_cuerpo(cuerpo):
    """LAS CAIDAS PROPIAS QUE EL CUERPO PERMITE CONTAR: los numerales distintos
    de las cabeceras `C.n` DENTRO DE LA SECCION 8. Devuelve el conjunto de
    numeros, o None si el cuerpo no trae seccion 8 y por tanto no hay nada que
    contar.

    SOLO LA SECCION 8, y no el documento entero, porque un reporte cita `C.n`
    ajenas en su prosa (las del acta del auditor, por ejemplo) y contarlas seria
    fabricar un rojo. PURA: recibe el texto y no lee nada."""
    lineas = cuerpo.split(NL)
    inicio = None
    for i, l in enumerate(lineas):
        if l.startswith(CAB_8):
            inicio = i
            break
    if inicio is None:
        return None
    fin = len(lineas)
    for i in range(inicio + 1, len(lineas)):
        if lineas[i].startswith("## "):
            fin = i
            break
    return set(int(m.group(1)) for m in
               (PATRON_CAIDA_PROPIA.match(l) for l in lineas[inicio:fin]) if m)


def tareas_de_la_tabla(cuerpo):
    """LAS FILAS DE LA TABLA DE TAREAS, contadas entre sus dos marcas y sin la
    cabecera ni el separador. Devuelve un entero, o None si no hay tabla que
    contar.

    UNA FILA ES UNA FILA CON UN NUMERO DE TAREA DENTRO, y no cualquier linea que
    empiece por barra: asi la cabecera (`| tarea | que encarga |`) y el separador
    (`|---|---|`) quedan fuera por lo que son y no por su posicion. PURA."""
    if MARCA_TABLA_ABRE not in cuerpo or MARCA_TABLA_CIERRA not in cuerpo:
        return None
    dentro = cuerpo.split(MARCA_TABLA_ABRE, 1)[1].split(MARCA_TABLA_CIERRA, 1)[0]
    return len([l for l in dentro.split(NL)
                if re.match(r"^\|\s*\*{0,2}TAREA\s+\d+", l.strip(), re.IGNORECASE)])


def numerales_del_veredicto(veredicto):
    """LOS NUMERALES QUE EL VEREDICTO PUBLICA, con su especie. Devuelve
    [(texto_del_numeral, valor, especie)], con la especie en `caidas` o `tareas`.

    LOS NUMERALES SE LEEN EN CIFRA Y EN LETRA, y la letra importa mas: el
    veredicto de una linea los escribe casi siempre con palabras (*"LAS SEIS
    CAIDAS"*), y una guarda que solo viera digitos no habria mordido en el unico
    caso que la trae. PURA."""
    hallados = []
    for m in PATRON_NUMERAL.finditer(veredicto):
        crudo, sust = m.group(1), m.group(2).lower()
        valor = (int(crudo) if crudo.isdigit()
                 else PALABRA_A_NUMERO[crudo.lower()])
        hallados.append((crudo, valor, SUSTANTIVO_A_ESPECIE[sust]))
    return hallados


def numerales_del_veredicto_que_no_calzan(veredicto, cuerpo):
    """LA GUARDA DE LA ESCALADA (vuelta 183, TAREA 1.c). Devuelve
    (motivos, cuentas, hallados): `motivos` VACIA si todo calza.

    QUE COTEJA: cada numeral que el veredicto publique de una especie que el
    cuerpo permite contar, contra esa cuenta. Hoy son dos, las que el encargo
    nombra como minimo: las CAIDAS PROPIAS (cabeceras `C.n` de la seccion 8) y
    las TAREAS CERRADAS (filas de la tabla de tareas).

    Y CAE EN ROJO TAMBIEN CUANDO EL VEREDICTO PUBLICA UNA CIFRA QUE EL CUERPO NO
    PERMITE CONTAR. Un veredicto que dice "las siete caidas" sobre un cuerpo sin
    seccion 8 no es un veredicto verde: es una cifra sin fichero que la sostenga,
    que es exactamente lo que `EJECUTOR.md` 1 prohibe.

    LO QUE NO HACE, Y SE DICE PARA QUE NADIE LO ESPERE: no talla el veredicto. El
    veredicto es un juicio del ejecutor y se sigue escribiendo a mano; lo que
    deja de ser libre son sus NUMEROS. Un veredicto que necesite nombrar una
    cuenta AJENA (las caidas de otra vuelta, por ejemplo) no puede escribirla
    como "N caidas" a secas, y eso es a proposito: en la unica linea que se llama
    a si misma veredicto, "seis caidas" significa las de este reporte.

    PURA: recibe los dos textos y no lee ni escribe nada. Por eso su caso
    positivo por mutacion la puede tumbar sin tocar el repo."""
    caidas = caidas_propias_del_cuerpo(cuerpo)
    tareas = tareas_de_la_tabla(cuerpo)
    cuentas = {"caidas": (len(caidas) if caidas is not None else None),
               "tareas": tareas}
    hallados = numerales_del_veredicto(veredicto)
    motivos = []
    for crudo, valor, especie in hallados:
        cuenta = cuentas.get(especie)
        if cuenta is None:
            motivos.append(
                "el veredicto publica %r (%d %s) y EL CUERPO NO TRAE NADA QUE "
                "CONTAR de esa especie: una cifra sin fichero que la sostenga no "
                "cierra un reporte" % (crudo, valor, especie))
        elif valor != cuenta:
            motivos.append(
                "el veredicto publica %r (%d %s) y el cuerpo, CONTADO, dice %d"
                % (crudo, valor, especie, cuenta))
    return motivos, cuentas, hallados


def frase_del_caso_del_hueco(existe, tam, tam_lf):
    """CUAL DE LOS DOS CASOS ES EL HUECO, DICHO Y NO CONFUNDIDO (vuelta 183,
    TAREA 1.d; adjudicacion 7.1 del acta 182, por extension citada del punto 3 de
    `paradas/2026-09-05-la-bateria-sin-techo-DECISION.md`, que NOMBRA LOS DOS
    CASOS Y NO LOS CONFUNDE).

    LO QUE PASABA ANTES NO SE BORRA, SE CUENTA: `main()` hacia
    `tam = os.path.getsize(ruta_bat) if existe else -1` y la seccion publicaba
    `max(tam, 0)`, asi que UN FICHERO AUSENTE SALIA COMO "0 bytes medidos con
    os.path.getsize". No lo era: ese cero salia de un `max`. El propio
    instrumento ya imprimia `NO EXISTE` en su consola, o sea que la informacion
    existia y se perdia al escribirla.

    DEVUELVE EL PARRAFO, Y SIEMPRE CON UNA CIFRA DE BYTES DENTRO, porque la
    pieza (2) del hueco declarado sigue exigiendo bytes medidos y esta funcion NO
    afloja ninguna de las tres piezas: solo dice de donde sale el cero.

    PURA: recibe tres valores y no toca el disco."""
    if not existe:
        return (
            "**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`" + NL +
            "devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no" + NL +
            "hay ninguna medicion suya que publicar. Lo que esta seccion recibio de" + NL +
            "bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes" + NL +
            "normalizados a LF**, **y ese cero sale de que no hay fichero, no de una" + NL +
            "medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026" + NL +
            "en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos" + NL +
            "casos y no los confunde.")
    if tam == 0:
        return (
            "**CUAL DE LOS DOS CASOS ES: EL FICHERO EXISTE Y MIDE CERO.**" + NL +
            "`os.path.exists` devuelve SI y `os.path.getsize` **si corrio sobre el**:" + NL +
            "**0 bytes en disco y 0 bytes normalizados a LF**. **El cero es una" + NL +
            "medicion, no el resultado de un `max`**, y por eso se puede citar. Es el" + NL +
            "caso que la bateria del ejecutor dio en las vueltas 171, 172 y 173, y que" + NL +
            "por la letra del 5 sep NO CUENTA COMO HECHA.")
    return (
        "**CUAL DE LOS DOS CASOS ES: NINGUNO DE LOS DOS.** El fichero **existe y" + NL +
        "tiene cuerpo**: `os.path.getsize` mide **%d bytes en disco y %d bytes" % (tam, tam_lf) + NL +
        "normalizados a LF**. La rama del hueco se tomo por otro motivo, que" + NL +
        "`rama_de_la_seccion9()` deja escrito arriba, y no por falta de bytes.")


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


def renglones_fuera_de_cerca(texto):
    """LOS RENGLONES DEL TEXTO QUE NO VIVEN DENTRO DE UN BLOQUE CERCADO.

    Devuelve [(numero_de_linea, renglon)] en numeracion de 1. PURA.

    NACE EN LA VUELTA 186, TAREA 2.b (adjudicacion `6.2` del acta 186, que cierra
    la `PD.5`), Y NO ES CODIGO NUEVO: ES EL DESBLOQUEADOR QUE `cifras_sin_pareja()`
    YA TENIA DENTRO, SEPARADO A UNA SEDE PARA QUE LA PIEZA (2) LO LLAME. El encargo
    lo dice con esas palabras: *"reusando el desbloqueador que `cifras_sin_pareja()`
    ya tiene en este mismo fichero. No escribas un tercero."*

    UNA SEDE, DOS LLAMADORES: `cifras_sin_pareja()` y la pieza (2) de
    `piezas_que_faltan()`. La linea de la cerca NO se devuelve, igual que antes: no
    es contenido, es frontera.

    LA CERCA SIN CERRAR, DICHA EN VEZ DE DEJARLA AL AZAR: si el texto abre una cerca
    y no la cierra, todo lo que va detras queda DENTRO y por tanto fuera de esta
    lista. Es la conducta que `cifras_sin_pareja()` ya tenia desde que nacio, y se
    conserva letra por letra: cambiarla aqui habria cambiado de paso la guarda de
    las cifras sin pareja, que no es lo que esta vuelta viene a hacer.

    Y QUEDA DECLARADO LO QUE NO SE TOCA: `parrafos_fuera_de_cerca()` lleva su propio
    recorrido de cercas porque hace OTRO trabajo (agrupa renglones en parrafos y
    corta el parrafo en la frontera). No se funde con esta, y esa decision se
    escribe aqui para que no haya que volver a deducirla."""
    fuera = []
    dentro = False
    for n, linea in enumerate(texto.split(NL), 1):
        if linea.lstrip().startswith(CERCA):
            dentro = not dentro
            continue
        if dentro:
            continue
        fuera.append((n, linea))
    return fuera


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
    for n, linea in renglones_fuera_de_cerca(texto):
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
                      vuelta=None, nombre_bateria=None,
                      tramos_sellados_en_esta_vuelta=None):
    """LAS CUATRO PIEZAS, COMPROBADAS SOBRE EL TEXTO YA ESCRITO. Devuelve la
    lista de las que FALTAN, vacia si estan las cuatro.

    PURA A PROPOSITO: recibe el texto del reporte, las filas de la cabecera
    tallada y las lineas no vacias de la salida de la bateria, para que su caso
    positivo por mutacion pueda tumbarla una a una **sin tocar el repo y sin
    escribir nada**. Si esto viviera dentro del cuerpo de una funcion que
    escribe, no habria nada que un arnes pudiera llamar, y una guarda que no se
    puede llamar no se puede probar.

    EL SEXTO PARAMETRO NACE EN LA VUELTA 186, TAREA 2.a (adjudicacion `6.1` del
    acta 186, que cierra la `PD.6`), y SU VALOR POR DEFECTO `None` CONSERVA
    EXACTAMENTE LA CONDUCTA DE HOY, igual que hizo `rama_de_la_seccion9()` con
    el suyo en la 185: sin tramos sellados, la rama de la bateria continuada no
    abre y la pieza (4) cae en los mismos casos en que caia antes. `main()` lo
    COMPUTA con `tramos_por_vuelta()` y NO lo recibe por bandera: no hay opcion
    de linea de ordenes para esto a proposito, porque UNA EVIDENCIA QUE SE PUEDE
    TECLEAR NO ES UNA EVIDENCIA."""
    faltan = []

    # (1) EL VEREDICTO ESCRITO
    if (VEREDICTO_VIEJO in texto
            or "**EL VEREDICTO DE UNA LINEA:" not in texto):
        faltan.append("(1) el veredicto de una linea no esta escrito")

    # (2) LA CABECERA PEGADA
    # LA MARCA SE BUSCA FUERA DE LOS BLOQUES CERCADOS (vuelta 186, TAREA 2.b;
    # adjudicacion `6.2` del acta 186, que cierra la `PD.5`). Hasta aqui esta
    # pieza buscaba en TODO el texto y se encendia sobre una CITA: el reporte de
    # la 185 pego la salida roja del cierre de la 184 dentro de una cerca, esa
    # salida nombraba la marca, y la pieza (2) la conto como hueco sin rellenar.
    # Un falso positivo no es fallar ruidoso, es ruido, y ademas hacia IMPOSIBLE
    # que un reporte citara entera la salida roja de otro, que es lo que el
    # encargo permanente manda hacer.
    # SE REUSA EL DESBLOQUEADOR QUE `cifras_sin_pareja()` YA TENIA, separado a
    # `renglones_fuera_de_cerca()`: una sede, dos llamadores, y NO un tercero.
    # LO DEMAS DE LA PIEZA (2) NO SE TOCA: si el hueco esta fuera de una cerca
    # sigue siendo rojo, si el tallador no trae filas sigue siendo rojo, y si
    # alguna fila no esta pegada sigue siendo rojo, con sus textos de hoy.
    if any(HUECO_CABECERA in l for _n, l in renglones_fuera_de_cerca(texto)):
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
                # LA REGLA VIVE EN UNA SOLA SEDE Y LA PIEZA (4) LA LLAMA (vuelta
                # 186, TAREA 2.a; adjudicacion `6.1` del acta 186, que cierra la
                # `PD.6`). Hasta aqui esta pieza llevaba SU PROPIA COPIA de la
                # comparacion `ajena != vuelta`, asi que la reparacion que la
                # vuelta 185 le hizo a `rama_de_la_seccion9()` no le llegaba: el
                # instrumento decia dos cosas distintas del mismo caso.
                #
                # NO SE LE PONE UNA COPIA SINCRONIZADA DE LA RAMA NUEVA. Dos
                # copias que hoy dicen lo mismo son dos copias que manana diran
                # cosas distintas, y eso es lo que ha costado cinco vueltas.
                #
                # EL ROJO VIEJO NO SE REESCRIBE: si la rama sale `ROJO`, esta
                # pieza sigue cayendo CON SU TEXTO DE HOY, palabra por palabra.
                # Lo unico que cambia es QUIEN decide.
                ajena = vuelta_de_fichero(nombre_bateria)
                rama_p4, _motivo_p4 = rama_de_la_seccion9(
                    lineas_bateria, nombre_bateria, vuelta,
                    tramos_sellados_en_esta_vuelta)
                if vuelta is not None and ajena is not None and rama_p4 == "ROJO":
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
    # LA EVIDENCIA DE LA BATERIA CONTINUADA SE COMPUTA AQUI Y NO SE PASA POR
    # BANDERA (vuelta 185, TAREA 1.c). NO HAY OPCION DE LINEA DE ORDENES PARA
    # ESTO A PROPOSITO: una evidencia que se puede teclear no es una evidencia.
    reparto_tramos = tramos_por_vuelta(ajena)
    tramos_sellados = sorted(n for n, v in reparto_tramos.items() if v == V)
    print("   TRAMOS DE ESA BATERIA Y LA VUELTA QUE SELLO CADA UNO, leidos del")
    print("   asunto de su ultimo commit con git log y NO tecleados:")
    for n in sorted(reparto_tramos):
        print("      tramo %-3d -> vuelta %s" % (n, reparto_tramos[n]))
    print("   CIFRA tramos de esa bateria con fichero en disco: %d"
          % len(reparto_tramos))
    print("   CIFRA tramos sellados EN LA VUELTA %d: %d %s"
          % (V, len(tramos_sellados), tramos_sellados))
    # LA DECISION DE RAMA YA NO SE TOMA AQUI: la toma rama_de_la_seccion9(), que
    # es pura y tiene arnes propio. REMEDIO DEL `E.1` DEL ACTA 180, vuelta 182.
    rama, motivo_rama = rama_de_la_seccion9(lineas_bat, a.bateria, V,
                                            tramos_sellados)
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

    print("B.0) EL CARRIL: NORMAL O CIERRE TARDIO, COMPUTADO Y NO PASADO POR")
    print("     BANDERA (vuelta 186, TAREA 2.c; respuesta del acta 186 a la P.2)")
    curso = vuelta_en_curso()
    tardio = es_cierre_tardio(V, curso)
    print("   vuelta que se cierra: %d" % V)
    print("   vuelta EN CURSO, leida del asunto del ultimo commit con git log y")
    print("   NO tecleada: %s" % curso)
    print("   CARRIL: %s" % ("CIERRE TARDIO" if tardio else "NORMAL"))
    if tardio:
        print("   en este carril las cifras sin pareja NO bloquean, pero SE DECLARAN")
        print("   una a una dentro del propio reporte cerrado. NINGUNA OTRA GUARDA SE")
        print("   AFLOJA: las cuatro piezas, el cuerpo byte a byte, los guiones y las")
        print("   citas de arnes siguen mandando igual.")
    else:
        print("   en el carril normal NO CAMBIA NADA: las cifras sin pareja siguen")
        print("   siendo ROJO.")
    print("")

    print("B.1) LOS NUMERALES DEL VEREDICTO, COTEJADOS CONTRA LO QUE EL CUERPO")
    print("     PERMITE CONTAR (vuelta 183, TAREA 1.c; escalada de AUDITOR.md 1.2)")
    # EL CUERPO QUE EL VEREDICTO DESCRIBE SON LAS DOS MITADES JUNTAS: la tabla de
    # tareas vive en el esqueleto que ya esta en el arbol, y la seccion 8 con sus
    # `C.n` vive en el borrador del cierre. Cotejar contra una sola mitad seria
    # no poder contar la otra.
    cuerpo_juzgado = texto + NL + cuerpo
    motivos_ver, cuentas_ver, hallados_ver = numerales_del_veredicto_que_no_calzan(
        a.veredicto, cuerpo_juzgado)
    print("   el veredicto, tal como se paso: %r" % a.veredicto.strip()[:120])
    print("   CIFRA numerales hallados en el veredicto: %d" % len(hallados_ver))
    for crudo, valor, especie in hallados_ver:
        print("      %-10r -> %d %s" % (crudo, valor, especie))
    print("   LAS CUENTAS DEL CUERPO, CONTADAS Y NO TECLEADAS:")
    for especie in sorted(cuentas_ver):
        v = cuentas_ver[especie]
        print("      %-8s -> %s"
              % (especie, v if v is not None else "(el cuerpo no permite contarlo)"))
    print("   CIFRA numerales que NO calzan: %d" % len(motivos_ver))
    for m in motivos_ver:
        print("      " + m)
    rojos.extend(motivos_ver)
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
            "**EL NOMBRE DEL FICHERO:** `%s`." % a.bateria + NL + NL +
            # LA MEDICION, Y AHORA DICE CUAL DE LOS DOS CASOS ES (vuelta 183,
            # TAREA 1.d; adjudicacion 7.1 del acta 182). La frase la arma
            # `frase_del_caso_del_hueco()`, que es PURA y tiene arnes propio, y
            # sigue publicando las DOS convenciones de bytes mientras la del
            # fundador no este fijada.
            frase_del_caso_del_hueco(existe, tam, tam_lf) + NL + NL +
            "%s %s" % (MARCA_ATRIBUCION, atribucion) + NL + NL +
            "**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este" + NL +
            "instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b" + NL +
            "(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es" + NL +
            "estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**." + NL +
            "Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y" + NL +
            "**una corrida de otra vuelta pegada aqui tampoco vale**." + NL)

    texto = texto.rstrip(NL) + NL + NL + cuerpo.rstrip(NL) + NL + NL + seccion9
    if tardio:
        # LA DECLARACION SE ANEXA AL FINAL Y VA DENTRO DE UNA CERCA, asi que no
        # se acusa a si misma en la relectura del bloque D ni mueve el numero de
        # linea de nada de lo que va antes. Se computa sobre el texto YA armado,
        # que es el que se va a escribir.
        huerfanas_previo = cifras_sin_pareja(texto)
        declaracion = declaracion_de_cifras_sin_pareja(huerfanas_previo, V, curso)
        texto = texto.rstrip(NL) + NL + NL + declaracion
        print("   CARRIL TARDIO: se anexa la declaracion de las cifras sin pareja")
        print("      CIFRA cifras sin pareja declaradas: %d" % len(huerfanas_previo))
        print("      la declaracion mide %d bytes"
              % len(declaracion.encode("utf-8")))
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
    print("   ESCRITO: %s (%d bytes, %d saltos de linea)"
          % (rel(REPORTE), len(texto.encode("utf-8")), texto.count(NL)))
    print("")

    print("D) SE RELEE DEL DISCO Y SE MIRAN LAS CUATRO PIEZAS")
    de_nuevo = leer(REPORTE)
    # LA EVIDENCIA DE LOS TRAMOS SE LE PASA TAMBIEN A LA PIEZA (4) (vuelta 186,
    # TAREA 2.a). Es la MISMA lista que ya se computo arriba con
    # `tramos_por_vuelta()` y que se le pasa a `rama_de_la_seccion9()`: una sede,
    # dos llamadores, y ninguna bandera de linea de ordenes.
    faltan = piezas_que_faltan(de_nuevo, filas, lineas_bat,
                               vuelta=V, nombre_bateria=a.bateria,
                               tramos_sellados_en_esta_vuelta=tramos_sellados)
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
    # EN EL CARRIL TARDIO LAS CIFRAS SIN PAREJA NO BLOQUEAN, PERO SE SIGUEN
    # MIDIENDO Y SE SIGUEN IMPRIMIENDO, y ademas quedan DECLARADAS dentro del
    # propio reporte por el bloque C. Las otras TRES comprobaciones de esta lista
    # NO SE AFLOJAN en ningun carril.
    for etiqueta, cond, bloquea in (
            ("el cuerpo del cierre esta byte a byte",
             cuerpo.rstrip(NL) in de_nuevo, True),
            ("cero guiones largos y cero guiones medios",
             chr(8212) not in de_nuevo and chr(8211) not in de_nuevo, True),
            ("toda cifra de bytes y todo sha con su pareja",
             not huerfanas, not tardio),
            ("toda cita de arnes calza con su fichero", not citas_rojas, True)):
        print("   %-34s %s%s"
              % (etiqueta, "SI" if cond else "NO",
                 "" if bloquea else "   (no bloquea: CARRIL DE CIERRE TARDIO,"
                                    " y va DECLARADA en la seccion 10)"))
        if not cond and bloquea:
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
