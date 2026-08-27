# -*- coding: utf-8 -*-
"""RONDA 2 del discutible 1: limpio la vara negativa (quitando la clausula de
contabilidad 'misma relacion del puesto', que no es una confesion de solape
roto), pruebo combinaciones, y ademas miro QUE DICE cada vara sobre los TRES de
la mesa (886, 890, 947). Una vara que no decide los tres tampoco sirve para lo
que la mesa se sento."""
import json, io, re, unicodedata

EXPEDIENTE = {1083:"QUEDA",1191:"QUEDA",1886:"QUEDA",1844:"QUEDA",896:"QUEDA",
    909:"QUEDA",910:"QUEDA",940:"QUEDA",983:"QUEDA",993:"QUEDA",1020:"QUEDA",
    1057:"QUEDA",1086:"QUEDA",1196:"QUEDA",1220:"QUEDA",
    1098:"SALE",1009:"SALE",1281:"SALE",1992:"SALE"}
MESA = [886, 890, 947]

def sinac(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "")
                   if unicodedata.category(c) != "Mn").lower()

V = {}
for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8"):
    if l.strip():
        d = json.loads(l); V[d["puesto_intra"]] = d
R = {p: sinac(V[p]["razon"]) for p in list(EXPEDIENTE) + MESA}
NODOS = {p: (sinac(V[p]["nodo_a"]), sinac(V[p]["nodo_b"])) for p in list(EXPEDIENTE) + MESA}

ORD = r"(primer|segundo|tercer|cuarto|quinto|sexto|septimo|octavo|noveno|decimo|primera|segunda|tercera|cuarta|quinta)"
CONFIESA = r"queda\s+fuera|no crea jerarquia|ninguno la expande"

def ancla(t):
    return (bool(re.search(r"\bla madre\b", t))
            or bool(re.search(r"\b(es|son)\b[^.;]{0,40}?\blinea\b", t))
            or bool(re.search(r"\b(paso|fase)\s+" + ORD + r"|\b" + ORD + r"\s+(paso|fase)", t))
            or bool(re.search(r"\buna de (las|los)\s+\w+", t))
            or bool(re.search(r"\ben\s+\w*\s*\blinea\b", t))
            or bool(re.search(r":\s*[^.;]{0,30}\blinea\b", t)))

def nombra_dos(p, t):
    a, b = NODOS[p]; return a in t and b in t

VARAS = [
    ("w1  no confiesa solape roto",            lambda p,t: not re.search(CONFIESA, t)),
    ("w2  nombra los dos ids + no confiesa",   lambda p,t: nombra_dos(p,t) and not re.search(CONFIESA, t)),
    ("w3  ancla O (nombra dos y no confiesa)", lambda p,t: ancla(t) or (nombra_dos(p,t) and not re.search(CONFIESA, t))),
    ("w4  ancla Y no confiesa",                lambda p,t: ancla(t) and not re.search(CONFIESA, t)),
    ("w5  ancla",                              lambda p,t: ancla(t)),
]

print("=" * 100)
print("RONDA 2. CINCO VARAS MAS, CONTRA LAS 19 PUBLICADAS, Y QUE DICEN DE LOS TRES DE LA MESA")
print("=" * 100)
mejor = ("", 0)
for nombre, f in VARAS:
    choca = [(p, e, "QUEDA" if f(p, R[p]) else "SALE")
             for p, e in sorted(EXPEDIENTE.items())
             if ("QUEDA" if f(p, R[p]) else "SALE") != e]
    calzan = 19 - len(choca)
    mesa = {p: ("QUEDA" if f(p, R[p]) else "SALE") for p in MESA}
    print("%-42s CALZAN %2d/19 | CHOCAN %d %s" % (nombre, calzan, len(choca),
          [(p, "pub " + e + "/vara " + d) for p, e, d in choca]))
    print("%-42s   los tres de la mesa: %s" % ("", mesa))
    if calzan > mejor[1]: mejor = (nombre, calzan)
print()
print("MEJOR DE LAS TRECE VARAS PROBADAS (ocho + cinco): %s con %d de 19." % mejor)
print("ALGUNA REPRODUCE LAS DIECINUEVE:", "SI" if mejor[1] == 19 else "NO")
