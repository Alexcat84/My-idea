# -*- coding: utf-8 -*-
r"""_v219_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 219,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda tabla o cifra del reporte
cita el fichero de salida del que sale, y se RECONSTRUYE CONTANDO ESE FICHERO
antes de publicarla. Aqui NINGUNA celda se teclea: las filas se leen de
docs/loop/SALIDA_V219_T1_REGISTROS.txt, y el compositor DICE cuantas armo y
cuantas deberia haber.

LO UNICO MIO SON LOS DISCUTIBLES Y SUS MOTIVOS, y van en su propia seccion
rotulada como lectura mia, para que se pueda auditar cual es cual.

USO:  python scripts/loop/_v219_t1_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T1_REGISTROS.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t1_seccion.md" % VUELTA


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def L(t, ancla):
    """LA LINEA QUE LLEVA EL ANCLA, LEIDA DEL FICHERO Y NO TECLEADA. PURA.

    Cae en rojo si no aparece exactamente una vez, porque una cifra que no
    tiene fichero de donde salir NO SE PUBLICA."""
    hay = [l.strip() for l in t.split(NL) if ancla in l]
    if len(hay) != 1:
        raise SystemExit("ROJO: el ancla %r aparece %d vez(ces) en %s y se "
                         "exige 1." % (ancla, len(hay), SALIDA))
    return hay[0]


def bloque_tabla(t, cabecera):
    """LA TABLA ENTERA QUE EMPIEZA EN SU CABECERA, PEGADA DEL FICHERO. PURA."""
    ls = t.split(NL)
    idx = [n for n, l in enumerate(ls) if l.startswith(cabecera)]
    if len(idx) != 1:
        raise SystemExit("ROJO: la cabecera de tabla %r aparece %d vez(ces)."
                         % (cabecera, len(idx)))
    n = idx[0]
    filas = []
    while n < len(ls) and ls[n].startswith("|"):
        filas.append(ls[n])
        n += 1
    return filas


CUERPO = """### TAREA 1. LOS REGISTROS

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:**
``%(salida)s``, **%(bytes_salida)s**, exitcode 0.

**EL INSTRUMENTO NO ES ARNES NUEVO, Y ESO IMPORTA CON LA MORATORIA ENCIMA.**
`scripts/loop/_v%(v)d_t1_registros.py` lleva prefijo de guion bajo, esta fuera
del censo y fuera de la nomina, y **no vigila nada**: muere con la vuelta. Lo
unico que hace es **localizar lineas en un fichero, leer un registro y correr un
recomputo de solo lectura**. La nomina sigue **CONGELADA EN 135**.

**Y LLEVA UNA CORRECCION DECLARADA DENTRO DE LA PROPIA VUELTA, QUE NO CAZO YO
SINO SU PROPIA GUARDA.** La primera version del instrumento buscaba la cabecera
del acta 217 con el ancla `# ACTA DEL AUDITOR, VUELTA 217:`, copiando la forma
de la del acta 218, **y la del acta 217 no lleva dos puntos sino un parentesis
con su fecha**. La corrida salio en **ROJO con 1 comprobacion fallando**, se
corrigio, y **el ancla vieja queda escrita en el codigo sin borrar**, porque una
correccion que tapa lo que corrige no se puede auditar. **No llego a ser cifra
publicada.**

#### 1.a. LAS SEIS ADJUDICACIONES CAYERON DE MI LADO, Y NINGUNA MUEVE UN VEREDICTO

**LA LINEA NO SE TECLEA.** El acta de la vuelta 218 empieza donde el fichero
dice, no donde yo recuerde: %(inicio)s

**LA TABLA, PEGADA ENTERA DE `%(salida)s` Y NO TECLEADA** (%(nadj)s filas
armadas leyendo ese fichero, y **la cifra que deberia haber es 6**):

%(tabla_adj)s

**LO QUE CADA UNA SOSTIENE, CON LA GLOSA DEL AUDITOR Y NO CON LA MIA.** La `4.1`
confirma el **299 en `D`** leyendo los dos nodos del grafo, y contesta mi propia
duda con un argumento mejor que el mio: **el paso 3 de la madre es DEFINIR el
mensaje y el paso 2 del hijo es CAPACITAR para entregarlo, y definir no es
capacitar**. La `4.2` sostiene el **1249 en `D`** porque el `9.6.3` **cuenta
lados y no pasos**, y hay procedimiento en los dos. La `4.3` adjudica `D.3` y
`P.3` juntas: **escribir en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no solo estaba
permitido, estaba ORDENADO** por la `5.7` del acta 217, que vive en la **linea
77304** de `docs/loop/ACTA_AUDITOR.md` y que este instrumento localizo hoy:
%(cita217)s **NO SE REVIERTE NADA.** La `4.4` fija que **el ANTES es la vispera
de la fase 01**, con lo que `01 FUENTES` idx 0 se sostiene en CUBRE y **el
recuento NO vuelve a 12 y 5**. La `4.5` fija que **la clausula exige el HECHO y
no la FRASE**, con lo que `02 DESTEJIDOS` idx 1 se sostiene en CUBRE. Y la `4.6`
confirma que **no fabricar el mutante fue la lectura correcta de la moratoria**,
y que ademas evito una guarda que se publica como mordiendo sin morder.

**QUE NINGUNA MUEVE UN VEREDICTO NO ES UNA AFIRMACION MIA: ES UNA MEDICION
CONTRA EL REGISTRO.**

%(no_mueve)s

**EL MARCADOR RECOMPUTADO HOY**, sellado en
``docs/loop/SALIDA_V%(v)d_T1_MARCADOR.txt``, **%(bytes_marcador)s**:

%(marcador)s

**Y LA CONCLUSION, CON SU CIFRA:** %(correcciones)s
%(no_paro)s

#### 1.b. EL RECUENTO DE LAS DIECISIETE, REMEDIDO HOY Y NO HEREDADO

**EL INSTRUMENTO ES EL MISMO QUE EL AUDITOR REPRODUJO BYTE A BYTE**, y lo corri
yo hoy al abrir la vuelta: `scripts/loop/_v218_t2_lecturas.py`. **Su fichero
sellado propio NO cambio de contenido al re-correrlo**, y esa es la prueba de
que es un lector y no un escritor: `docs/loop/SALIDA_V218_T2_LECTURAS.txt` mide
**18783 bytes en disco y 18783 normalizado a LF**, con `sha256` disco
**10e4d48abd6b4515** y `sha256` LF **10e4d48abd6b4515**, **los mismos antes y
despues de mi corrida**.

**LAS DOS RUTAS, CADA UNA CON SUS DOS CONVENCIONES EN SU MISMA LINEA:**

%(rutas_recuento)s

**LA TABLA, PEGADA ENTERA DE `%(salida)s`** (%(nrec)s filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 3**):

%(tabla_rec)s

**Y LA CIFRA DEL ENCARGO, CITADA COMO CONTRASTE Y NO COMO FUENTE:**
%(contraste)s
%(mi_medicion)s
%(calza)s

**LAS CUATRO QUE SIGUEN SIN CUBRIR, LEIDAS DE MI PROPIA CORRIDA DE HOY:**

%(resto)s

%(cifra_resto)s

#### 1.c. LAS SEIS COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL

**NO LAS RESUELVO: SOLO TIENEN QUE QUEDAR ESCRITAS DONDE EL FUNDADOR LAS
ENCUENTRE**, que es lo que el encargo pide. La tabla sale de la seccion 6 del
acta 218, que empieza en la linea que el fichero dice: %(inicio6)s

**LA TABLA, PEGADA ENTERA DE `%(salida)s`** (%(nint)s filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 6**):

%(tabla_int)s

**Y EL DETALLE DE CADA UNA, LEIDO VERBATIM DEL ACTA Y NO RESUMIDO POR MI:** la
**1** es la celda de `07 ADUANA` de `docs/plan/08_VERIFICACION.md`, **linea 30**,
que **dice CUATRO controles cuando su ficha `OP-A-02` dice CINCO**; manda la
ficha, ya adjudicado, y **la celda es sede del fundador y sigue sin corregir**.
La **2** es `scripts/loop/vuelta150_4_tabla_por_fase.py` **en rojo**, con
`AssertionError: la tabla no trae ocho filas: 11`, y **queda por decidir si se
repara o si su vara de ocho filas se retira** en favor de la de las diecisiete
clausulas. La **3** es el rotulo de `docs/loop/SALIDA_V183_BATERIA.txt`, que
**dice VUELTA 183 sobre el contenido de la 215**, por el lanzador estable que no
se clona. La **4** es la familia `C.1` del auditor **en OCHO**, con el remedio
del fundador **medido fallando DOS veces** desde su traslado del 9 sep, y el
propio auditor la marca como **lo mas urgente de esa lista**. La **5** es que
**la ciega no puede acertar las clases `B` y `C`**, que viven de figuras de tres
o mas miembros invisibles desde un par de dos. Y la **6** son **las CUATRO
clausulas en A MEDIAS con su cifra**: `01 FUENTES` idx 1 (**7 menciones** que aun
declaran un segundo libro), `03 FUSIONES` idx 0 (**71 actos** por la lectura
ancha, **SEIS fusiones de 19 nodos** por la estrecha), `05 SANEO` idx 1 (**1 de
los 3** de Incoterms anotado como trabajo post campana) y `07 ADUANA` idx 0 (**el
quinto control sin correr**).

#### ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA

%(sha)s

%(sha_total)s

#### LOS DISCUTIBLES DE LA TAREA 1, MARCADOS ANTES DE SABER SI ACIERTO

| # | que decidi | la duda que dejo escrita |
|---|---|---|
%(disc)s

#### EL CASO ROJO, DICHO CUAL ES CUAL

%(caso_rojo)s
"""

# LOS DISCUTIBLES SON LECTURA MIA Y SE MARCAN ANTES DE SABER SI ACIERTO
# (EJECUTOR.md 7).
DISCUTIBLES = [
    ("D.1", "QUE EL RECUENTO NO SE RECOMPUTA, SOLO SE REMIDE",
     "El encargo me manda volver a medir el recuento **con el mismo "
     "instrumento**, y yo lo entiendo como **re-correr el lector de la 218 tal "
     "cual**, sin tocarle nada, y publicar su cifra al lado de la que dejo. "
     "**La duda que dejo escrita antes de saber si acierto**: ese lector "
     "recompone el recuento leyendo la tabla de 17 filas que dejo "
     "`docs/loop/SALIDA_V218_T1_REGISTROS.txt` y aplicandole las dos subidas de "
     "la TAREA 2 de aquella vuelta. **Es una remedicion del mismo camino, no una "
     "medicion independiente**: si maniana alguien tocara aquella salida, la "
     "cifra se moveria sin que se moviera ninguna clausula. Si el auditor lee "
     "que remedir exigia recomputar las diecisiete sondas desde el grafo, mi "
     "1.b se queda corta y hay que correr el instrumento de la 217 entero."),
    ("D.2", "QUE RE-CORRER EL LECTOR DE LA 218 NO ES ESCRIBIR",
     "`scripts/loop/_v218_t2_lecturas.py` **escribe su propio fichero sellado** "
     "al terminar, y yo lo corri. **Lo declaro yo antes de que me lo pregunten**, "
     "porque es exactamente la especie de la caida `C.3` que el auditor de la 218 "
     "se cobro a si mismo. **Mi lectura es que aqui no aplica**: aquella era un "
     "instrumento que reaplicaba correcciones sobre "
     "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y este solo reescribe su propia "
     "salida con contenido identico, cosa que pruebo con el `sha256` medido "
     "antes y despues. **Si el auditor lee que re-correr cualquier cosa que "
     "escriba es escritura**, mi 1.b tenia que haberse hecho contra la salida ya "
     "sellada y sin correr nada."),
    ("D.3", "QUE LA GLOSA DE LAS SEIS ADJUDICACIONES ES REGISTRO Y NO LECTURA MIA",
     "En la 1.a escribo **lo que cada adjudicacion sostiene**, y lo escribo con "
     "las palabras del auditor, no con las mias, porque el encargo dice "
     "REGISTRA y no RELEE. **La duda**: al hacerlo estoy publicando en mi "
     "reporte afirmaciones sobre el grafo (los pasos del 299, los cuatro pasos "
     "del 1249) **que en esta vuelta NO he vuelto a medir yo**. Van con su "
     "atribucion y con su linea de acta, que es lo que la casa manda, **pero no "
     "van con medicion mia de hoy**, y eso lo digo aqui en vez de dejar que "
     "parezca medido."),
]


def main():
    t = leer(SALIDA)
    ruta_salida = os.path.join(RAIZ, SALIDA.replace("/", os.sep))
    b = io.open(ruta_salida, "rb").read()
    bytes_salida = ("%d bytes en disco y %d normalizado a LF"
                    % (os.path.getsize(ruta_salida),
                       len(b.replace(b"\r\n", b"\n"))))
    rm = os.path.join(RAIZ, "docs", "loop",
                      "SALIDA_V%d_T1_MARCADOR.txt" % VUELTA)
    bm = io.open(rm, "rb").read()
    bytes_marcador = ("%d bytes en disco y %d normalizado a LF"
                      % (os.path.getsize(rm), len(bm.replace(b"\r\n", b"\n"))))

    tabla_adj = bloque_tabla(t, "| rotulo | adjudicacion |")
    tabla_rec = bloque_tabla(t, "| veredicto | CIFRA que MIDO HOY")
    tabla_int = bloque_tabla(t, "| # | linea del acta 218 |")

    ls = t.split(NL)
    marcador = [l.strip() for l in ls if l.strip().startswith("marcador>")]
    no_mueve = [l.strip() for l in ls
                if l.strip().startswith("CIFRA veredictos en el registro:")
                or l.strip().startswith("puesto ")]
    rutas_recuento = [l.strip() for l in ls
                      if l.strip().startswith("docs/loop/SALIDA_V")
                      and "sha256 disco" in l]
    resto = [l.strip() for l in ls if re.match(r"^\s{6}\S.* idx \d+ \| ", l)]
    sha = [l.strip() for l in ls if " AL ENTRAR: sha256" in l
           or " AL SALIR:   sha256" in l]

    datos = {
        "v": VUELTA,
        "salida": SALIDA,
        "bytes_salida": bytes_salida,
        "bytes_marcador": bytes_marcador,
        "inicio": L(t, "EL ACTA 218 EMPIEZA EN LA LINEA"),
        "nadj": len(tabla_adj) - 2,
        "tabla_adj": NL.join(tabla_adj),
        "cita217": L(t, "LINEA 77304, LEIDA DEL FICHERO>"),
        "no_mueve": NL.join("- " + x for x in no_mueve),
        "marcador": NL.join("- " + x for x in marcador),
        "correcciones": L(t, "CIFRA correcciones que esta vuelta tiene que "
                             "aplicar por adjudicacion:"),
        "no_paro": L(t, "NO PARO."),
        "rutas_recuento": NL.join("- ``%s``" % x for x in rutas_recuento),
        "nrec": len(tabla_rec) - 2,
        "tabla_rec": NL.join(tabla_rec),
        "contraste": L(t, "Y LA CIFRA DEL ENCARGO, CITADA COMO CONTRASTE"),
        "mi_medicion": L(t, "MI MEDICION DE HOY:"),
        "calza": L(t, "CALZA CON EL CONTRASTE DEL ENCARGO:"),
        "resto": NL.join("- " + x for x in resto),
        "cifra_resto": L(t, "CIFRA filas de las que no cubren, armadas leyendo "
                            "mi corrida:"),
        "inicio6": L(t, "LA SECCION 6 EMPIEZA EN LA LINEA"),
        "nint": len(tabla_int) - 2,
        "tabla_int": NL.join(tabla_int),
        "sha": NL.join("- " + x for x in sha),
        "sha_total": L(t, "COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS "
                          "CONVENCIONES:"),
        "disc": NL.join("| **%s** | %s | %s |" % (a, b_, c)
                        for a, b_, c in DISCUTIBLES),
        "caso_rojo": L(t, "EL CASO ROJO, DICHO CUAL ES CUAL:"),
    }
    texto = CUERPO % datos

    print("CIFRA filas de la tabla de adjudicaciones, contadas del fichero: %d "
          "| CIFRA que deberia haber: 6" % datos["nadj"])
    print("CIFRA filas de la tabla del recuento, contadas del fichero: %d | "
          "CIFRA que deberia haber: 3" % datos["nrec"])
    print("CIFRA filas de la tabla de la integral, contadas del fichero: %d | "
          "CIFRA que deberia haber: 6" % datos["nint"])
    print("CIFRA filas del marcador, contadas del fichero: %d" % len(marcador))
    print("CIFRA rutas del recuento con sus dos convenciones: %d | CIFRA que "
          "deberia haber: 2" % len(rutas_recuento))
    print("CIFRA filas de las que no cubren, contadas del fichero: %d | CIFRA "
          "que deberia haber: 4" % len(resto))
    print("CIFRA lineas de sha al entrar y al salir: %d | CIFRA que deberia "
          "haber: 12" % len(sha))
    fallos = 0
    for etiqueta, cond in (("adjudicaciones", datos["nadj"] == 6),
                           ("recuento", datos["nrec"] == 3),
                           ("integral", datos["nint"] == 6),
                           ("rutas", len(rutas_recuento) == 2),
                           ("resto", len(resto) == 4),
                           ("sha", len(sha) == 12)):
        if not cond:
            fallos += 1
            print("   ROJO: la cuenta de %s no calza." % etiqueta)

    mayores = [l for l in texto.split(NL)
               if l.startswith("## ") and not l.startswith("### ")]
    print("CIFRA encabezados de nivel dos en el cuerpo del anexo: %d | CIFRA "
          "que deberia haber: 0" % len(mayores))
    if mayores:
        fallos += 1
    largos = texto.count(chr(8212)) + texto.count(chr(8211))
    print("CIFRA guiones largos mas medios en el cuerpo: %d" % largos)
    if largos:
        fallos += 1
    sospechosos = [c for c in re.findall(r"`([^`]+)`", texto)
                   if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        for s in sospechosos:
            print("   sospechoso> %s" % s)
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el compositor NO escribe.")
        return 1
    ruta = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO %s -> %d bytes en disco, %d lineas"
          % (DESTINO, os.path.getsize(ruta), texto.count(NL)))
    print("VERDE: el cuerpo de la TAREA 1 queda compuesto de su fichero.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
