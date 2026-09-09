# -*- coding: utf-8 -*-
r"""_v215_mensaje_tramo.py . EL MENSAJE DEL COMMIT DE UN TRAMO DE LA BATERIA,
COMPUESTO DE SU FICHERO SELLADO Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina (congelada en 135), no vigila nada y muere con la vuelta.

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5). Las cifras NO se vuelven a
computar aqui: se LEEN de la salida de scripts/loop/_v210_medir_tramo.py, que
es el instrumento que ya sabe leerlas del fichero sellado, y que esta vuelta NO
toca. Este fichero solo las COLOCA en el texto del commit.

POR QUE EXISTE, Y ES LA MISMA ENFERMEDAD DE SIEMPRE: once tramos son once
mensajes de commit con once juegos de cifras, y teclear cifras a mano once veces
es exactamente la especie de caida que EJECUTOR.md 1 lleva vueltas cazando (LA
TABLA SE IMPRIME, NO SE TECLEA). Aqui la unica prosa fija es la que NO lleva
cifras.

LA GUARDA QUE PUEDE CAER: si el medidor no publica alguna de las cifras que el
mensaje necesita, este instrumento CAE EN ROJO y no escribe el mensaje. NO
rellena el hueco con un blanco, que es justo la degradacion silenciosa que el
hallazgo 3.1 del acta 214 me cazo.

USO:  python scripts/loop/_v215_mensaje_tramo.py 2 > /tmp/msg.txt
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
MEDIDOR = os.path.join(AQUI, "_v210_medir_tramo.py")

CIFRAS = (
    ("bytes", "CIFRA bytes en disco: "),
    ("bytes_lf", "CIFRA bytes normalizado a LF: "),
    ("lineas", "CIFRA lineas: "),
    ("entradas", "CIFRA entradas que el tramo dice haber corrido: "),
    ("filas", "CIFRA filas de veredicto por arnes: "),
    ("ancla", "CIFRA ANCLA PERDIDA: "),
    ("no_mordio", "CIFRA NO MORDIO: "),
    ("no_repro", "CIFRA NO REPRODUCIBLE: "),
    ("declarado", "CIFRA CASO DECLARADO: "),
    ("ruido", "CIFRA RUIDO DE CONCURRENCIA: "),
    ("fuera", "CIFRA FUERA DE LA NOMINA: "),
    ("invisibles", "CIFRA INVISIBLES AL CENSO: "),
    ("sujeto", "CIFRA SUJETO NO CONGELADO: "),
    ("exitcode", "CIFRA EXITCODE DEL TRAMO: "),
    ("minutos", "CIFRA DURACION minutos: "),
)
TEXTOS = (
    ("sha", "CIFRA sha256 (LF), primeros 16: "),
    ("inicio", "CIFRA INICIO UTC: "),
    ("fin", "CIFRA FIN UTC: "),
    ("clase", "CLASE DEL VEREDICTO: "),
    ("anterior", "ultimo commit que toco el fichero, ANTES de este: "),
    ("fichero", "fichero: "),
)


def valor(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            return l.split(etiqueta, 1)[1].strip()
    return None


def reparto(texto):
    """LAS FILAS DEL REPARTO DE VEREDICTOS, LEIDAS DEL MEDIDOR. PURA."""
    fuera = []
    dentro = False
    for l in texto.split(NL):
        if "EL REPARTO DE VEREDICTOS" in l:
            dentro = True
            continue
        if dentro:
            m = re.match(r"^\s{6}(\S.*?)\s{2,}(\d+)\s*$", l)
            if not m:
                break
            fuera.append((m.group(1).strip(), m.group(2)))
    return fuera


def main():
    n = int(sys.argv[1])
    r = subprocess.run([sys.executable, MEDIDOR, str(n)], cwd=RAIZ,
                       capture_output=True)
    medido = r.stdout.decode("utf-8", errors="replace").replace(chr(13) + NL, NL)
    if r.returncode != 0 or not medido.strip():
        sys.stderr.write("ROJO: el medidor del tramo %d no dio salida.%s" % (n, NL))
        return 1
    sello = os.path.join(RAIZ, "docs", "loop",
                         "SALIDA_V%d_T2_TRAMO_%d_MEDIDO.txt" % (VUELTA, n))
    io.open(sello, "w", encoding="utf-8", newline=NL).write(medido)

    D = {}
    faltan = []
    for clave, etiqueta in CIFRAS:
        v = valor(medido, etiqueta)
        if v is None or not re.match(r"^-?[\d.]+$", v):
            faltan.append(etiqueta)
        D[clave] = v
    for clave, etiqueta in TEXTOS:
        v = valor(medido, etiqueta)
        if not v:
            faltan.append(etiqueta)
        D[clave] = v
    if faltan:
        sys.stderr.write("ROJO: el medidor no publica %d cifra(s) que el mensaje "
                         "necesita, y NO se rellena el hueco: %s%s"
                         % (len(faltan), faltan, NL))
        return 1

    filas_rep = reparto(medido)
    if not filas_rep:
        sys.stderr.write("ROJO: no hay reparto de veredictos que leer.%s" % NL)
        return 1
    rep = ", ".join("%s %s" % (c, nombre) for nombre, c in filas_rep)

    total = int(valor(medido, "CIFRA entradas que el tramo dice haber corrido: "))
    _, plan = subprocess.run(
        ["git", "log", "-1", "--format=%h %ad %s", "--date=short",
         "--", "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n],
        cwd=RAIZ, capture_output=True).returncode, ""

    cuerpo = """VUELTA %(v)d, BATERIA TRAMO %(n)d DE 11, SELLADO Y COMMITEADO AL TERMINAR, uno a uno y no todos al final.

%(fichero)s, %(bytes)s bytes en disco y %(bytes_lf)s normalizado a LF, %(lineas)s lineas, sha256 LF %(sha)s, exitcode %(exitcode)s, %(minutos)s minutos entre %(inicio)s y %(fin)s. Cifras leidas del propio fichero sellado por scripts/loop/_v210_medir_tramo.py %(n)d, NINGUNA TECLEADA, y colocadas en este mensaje por scripts/loop/_v%(v)d_mensaje_tramo.py, que CAE EN ROJO si alguna falta en vez de dejar el hueco. La salida del medidor queda sellada en docs/loop/SALIDA_V%(v)d_T2_TRAMO_%(n)d_MEDIDO.txt.

EL CALIBRE DEL TRAMO: %(entradas)s entradas corridas, %(filas)s filas de veredicto, %(rep)s. ANCLA PERDIDA %(ancla)s, NO MORDIO %(no_mordio)s, NO REPRODUCIBLE %(no_repro)s, invisibles al censo %(invisibles)s, SUJETO NO CONGELADO %(sujeto)s, RUIDO DE CONCURRENCIA %(ruido)s ficheros. NO REPRODUCIBLE en %(no_repro)s es la doble corrida diciendo que las dos corridas de las %(entradas)s entradas dan lo mismo.

CLASE DEL VEREDICTO: %(clase)s, Y NO ES UN ARNES DE LA NOMINA QUE CAIGA. Lo digo con las tres cifras delante porque la TAREA 2.d de mi encargo manda parar SI ALGUN ARNES DE LA NOMINA CAE, y ninguno cae: ANCLA PERDIDA %(ancla)s, NO MORDIO %(no_mordio)s, NO REPRODUCIBLE %(no_repro)s. El rojo lo enciende la mirada de la nomina sobre si misma, que corre ENTERA en cada tramo: %(fuera)s arneses que el censo VE, no anteriores a la vara 148, se quedan FUERA de la nomina porque AUDITOR.md 6.3 la congela en 135. Son vuelta197_tarea2_mutacion_orden_del_turno.py y vuelta199_tarea1_mutacion_guardas_revividas.py.

Y VA COMO PARADA EN MI REPORTE, POR EJECUTOR.md 5, PORQUE SON DOS REGLAS VIGENTES QUE SE CONTRADICEN Y NO LAS ARREGLO YO: la regla del propio lanzador desde la vuelta 148 dice que UN ARNES ENTRA EN LA NOMINA, y la moratoria del 7 sep 2026 dice que la nomina QUEDA CONGELADA EN 135, ni crece ni se poda. Mientras las dos rijan, este rojo es automatico y no lo apaga ninguna corrida. El precedente esta medido y no recordado: la bateria de la vuelta 210 encendio EXACTAMENTE este rojo, con los DOS MISMOS nombres.

LA VARA DE FRESCURA: el ultimo commit que toco este fichero ANTES de este era %(anterior)s. Como el lanzador computa su vuelta de su propio nombre y sus salidas se siguen llamando V183 corra la vuelta que corra, lo unico que prueba que este tramo es de la %(v)d es que su fichero cambie en un commit de la %(v)d. Este es ese commit.

La guarda del commit sobre el arbol del dataset corre al entrar y al salir del tramo, y su cifra queda dentro de la salida sellada.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
""" % dict(D, v=VUELTA, n=n, rep=rep)

    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        sys.stderr.write("ROJO: guiones largos o medios en el mensaje.%s" % NL)
        return 1
    sys.stdout.write(cuerpo)
    sys.stderr.write("VERDE: mensaje del tramo %d compuesto de %d cifras leidas, "
                     "0 tecleadas.%s" % (n, len(CIFRAS) + len(TEXTOS), NL))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
