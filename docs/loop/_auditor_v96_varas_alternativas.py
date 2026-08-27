# -*- coding: utf-8 -*-
"""DISCUTIBLE 1 DE LA VUELTA 96, PROBADO Y NO OPINADO.

El ejecutor declara NO HAY VARA CITABLE con UNA vara (trece familias de ancla)
que contradice tres adjudicaciones, e invita expresamente: "si el auditor
construye una vara que las reproduzca todas, mi conclusion cae".

Aqui construyo OCHO varas distintas sobre el texto de la razon, cada una con una
idea distinta de que es "nombrar a la madre", y las corro contra las DIECINUEVE
adjudicaciones publicadas. Si alguna da 19/19, la conclusion del ejecutor cae.
"""
import json, io, re, unicodedata

EXPEDIENTE = {
    1083: "QUEDA", 1191: "QUEDA", 1886: "QUEDA", 1844: "QUEDA", 896: "QUEDA",
    909: "QUEDA", 910: "QUEDA", 940: "QUEDA", 983: "QUEDA", 993: "QUEDA",
    1020: "QUEDA", 1057: "QUEDA", 1086: "QUEDA", 1196: "QUEDA", 1220: "QUEDA",
    1098: "SALE", 1009: "SALE", 1281: "SALE", 1992: "SALE",
}

def sinac(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "")
                   if unicodedata.category(c) != "Mn").lower()

V = {}
for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8"):
    if l.strip():
        d = json.loads(l); V[d["puesto_intra"]] = d

R = {p: sinac(V[p]["razon"]) for p in EXPEDIENTE}
NODOS = {p: (V[p]["nodo_a"], V[p]["nodo_b"]) for p in EXPEDIENTE}

ORD = r"(primer|segundo|tercer|cuarto|quinto|sexto|septimo|octavo|noveno|decimo|primera|segunda|tercera|cuarta|quinta)"
LINEA = r"\blinea\b"

def v1(p, t):  # la palabra madre, literal
    return bool(re.search(r"\bla madre\b|\bes la madre\b", t))

def v2(p, t):  # madre literal O es/son ... linea
    return v1(p, t) or bool(re.search(r"\b(es|son)\b[^.;]{0,40}?" + LINEA, t))

def v3(p, t):  # v2 O paso/fase ordinal O 'una de las N' O 'en N lineas' O dos puntos+linea
    return (v2(p, t)
            or bool(re.search(r"\b(paso|fase)\s+" + ORD, t))
            or bool(re.search(r"\b" + ORD + r"\s+(paso|fase)", t))
            or bool(re.search(r"\buna de (las|los)\s+\w+", t))
            or bool(re.search(r"\ben\s+\w*\s*" + LINEA, t))
            or bool(re.search(r":\s*[^.;]{0,30}" + LINEA, t)))

def v4(p, t):  # LA RAZON ASIGNA PAPEL A LOS DOS IDS NOMBRADOS
    a, b = (sinac(x) for x in NODOS[p])
    return a in t and b in t

def v5(p, t):  # v3 pero SIN el ancla que solo vive en el hijo (ordinal de fase)
    return (v2(p, t)
            or bool(re.search(r"\buna de (las|los)\s+\w+", t))
            or bool(re.search(r"\ben\s+\w*\s*" + LINEA, t))
            or bool(re.search(r":\s*[^.;]{0,30}" + LINEA, t)))

def v6(p, t):  # v3 Y ADEMAS la razon NO declara que algo del hijo queda fuera
    fuera = bool(re.search(r"queda\s+fuera|no crea jerarquia|ninguno la expande", t))
    return v3(p, t) and not fuera

def v7(p, t):  # solo: la razon NO declara solape roto
    return not bool(re.search(r"queda\s+fuera|no crea jerarquia|ninguno la expande"
                              r"|pareja nueva|misma relacion del puesto", t))

def v8(p, t):  # v4 Y no declara solape roto
    return v4(p, t) and v7(p, t)

VARAS = [
    ("v1  madre literal", v1),
    ("v2  v1 + es/son linea", v2),
    ("v3  la del ejecutor (trece familias)", v3),
    ("v4  la razon nombra los DOS ids", v4),
    ("v5  v3 sin el ordinal de fase", v5),
    ("v6  v3 + no declara solape roto", v6),
    ("v7  no declara solape roto (sola)", v7),
    ("v8  v4 + no declara solape roto", v8),
]

print("=" * 96)
print("OCHO VARAS SOBRE EL TEXTO DE LA RAZON, CONTRA LAS 19 ADJUDICACIONES PUBLICADAS")
print("=" * 96)
mejor = None
for nombre, f in VARAS:
    choca = []
    for p, esperado in sorted(EXPEDIENTE.items()):
        da = "QUEDA" if f(p, R[p]) else "SALE"
        if da != esperado:
            choca.append((p, esperado, da))
    calzan = len(EXPEDIENTE) - len(choca)
    print("%-40s CALZAN %2d/19 | CHOCAN %d %s"
          % (nombre, calzan, len(choca),
             [(p, "publicado " + e + " / vara " + d) for p, e, d in choca]))
    if mejor is None or calzan > mejor[1]:
        mejor = (nombre, calzan)
print()
print("MEJOR VARA DE LAS OCHO: %s, con %d de 19." % mejor)
print("HAY VARA QUE REPRODUZCA LAS DIECINUEVE:", "SI" if mejor[1] == 19 else "NO")
