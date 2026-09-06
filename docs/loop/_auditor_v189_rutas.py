# -*- coding: utf-8 -*-
r"""BARRIDO PROPIO DEL AUDITOR SOBRE UN DOCUMENTO: rutas y cifras de bytes.
No importa nada del ejecutor: patrones propios y medicion propia.
La regla de la ambiguedad es la misma que el ejecutor se destapo en su TAREA 4:
si entre la ruta y la pareja hay OTRA cifra de bytes, el sujeto es ambiguo y no
se atribuye. Es la unica pieza de criterio que le copio, y la copio a proposito:
sin ella el 15655 de una ENTRADA se lee como el tamano de su FICHERO."""
import io, os, re, sys
RAIZ = os.path.abspath(".")
NL = chr(10)
RUTA = re.compile(r"`((?:docs|scripts|web|engine|dataset)/[A-Za-z0-9_\-./]+)`")
CUERPO = r"([^`]{0,220}?)"
P1 = re.compile(r"`([A-Za-z0-9_\-./]+)`" + CUERPO +
                r"(\d[\d.]*) bytes en disco y (\d[\d.]*)(?: bytes?)? normalizad[oa]s? a LF")
P2 = re.compile(r"`([A-Za-z0-9_\-./]+)`" + CUERPO +
                r"disco \*{0,2}(\d[\d.]*)\*{0,2} bytes?[ ,|]{1,3}LF \*{0,2}(\d[\d.]*)\*{0,2} bytes?")
OTRA = re.compile(r"\d[\d.]* bytes")


def num(s):
    return int(s.replace(".", ""))


def medir(r):
    p = os.path.join(RAIZ, r)
    if not os.path.exists(p) or os.path.isdir(p):
        return None
    b = open(p, "rb").read()
    return len(b), len(b.replace(b"\r\n", b"\n"))


def barre(doc):
    t = io.open(doc, encoding="utf-8").read()
    L = []
    w = L.append
    rutas = sorted(set(RUTA.findall(t)))
    w("DOCUMENTO: %s" % doc)
    w("CIFRA rutas distintas: %d" % len(rutas))
    faltan = [r for r in rutas if medir(r) is None]
    cero = [r for r in rutas if (medir(r) or (1, 1))[0] == 0]
    w("CIFRA rutas que NO existen: %d" % len(faltan))
    for r in faltan:
        w("   NO EXISTE: %s" % r)
    w("CIFRA rutas de CERO BYTES: %d" % len(cero))
    for r in cero:
        w("   CERO BYTES: %s" % r)
    vistos, malas, buenas, ambiguas = set(), [], [], 0
    for pat in (P1, P2):
        for r, medio, a, b in pat.findall(t):
            if OTRA.search(medio):
                ambiguas += 1
                continue
            clave = (r, a, b)
            if clave in vistos:
                continue
            vistos.add(clave)
            m = medir(r)
            if m is None:
                malas.append((r, "NO EXISTE", a, b, "-", "-"))
                continue
            pa, pb = num(a), num(b)
            if pa != m[0] or pb != m[1]:
                malas.append((r, "DISCO" if pa != m[0] else "LF", a, b, m[0], m[1]))
            else:
                buenas.append((r, pa, pb))
    w("CIFRA parejas ambiguas NO atribuidas: %d" % ambiguas)
    w("CIFRA parejas de bytes atadas a una ruta: %d" % (len(buenas) + len(malas)))
    w("CIFRA parejas que CALZAN por las dos convenciones: %d" % len(buenas))
    for r, a, b in buenas:
        w("   CALZA: %s -> disco %d | LF %d" % (r, a, b))
    w("CIFRA parejas que DISCREPAN: %d" % len(malas))
    for r, cual, a, b, da, db in malas:
        w("   DISCREPA (%s): %s publicada %s/%s medida %s/%s" % (cual, r, a, b, da, db))
    return L


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    out = []
    for d in sys.argv[1:]:
        out += barre(d) + [""]
    print(NL.join(out))
