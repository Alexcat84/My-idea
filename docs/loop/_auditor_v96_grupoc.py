# -*- coding: utf-8 -*-
"""VARA PROPIA del auditor 96 sobre las 18 razones del grupo C: mide, con mis
propios patrones y sin importar el codigo de nadie, cuantas mencionan "linea",
cuantas casan la formula literal "es/son UNA LINEA" que el acta 95 cita entre
comillas, y cuantas anclan con "en ... linea"."""
import json, io, re, unicodedata

GRUPO_C = [886,890,896,909,910,940,947,983,993,1020,1057,1083,1086,1191,1196,1220,1844,1886]

def sinac(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "")
                   if unicodedata.category(c) != "Mn").lower()

V = {}
for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8"):
    if l.strip():
        d = json.loads(l)
        V[d["puesto_intra"]] = d

MENCIONA = re.compile(r"\blinea")
# la formula que el acta 95 pone ENTRE COMILLAS: "es/son UNA LINEA"
ESTRICTA = re.compile(r"\b(es|son)\s+(una|un|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|sola|solo|solamente|unicamente)?\s*\b(una\s+)?linea\b")
ESTRICTA_LITERAL = re.compile(r"\b(es|son)\s+una\s+(sola\s+)?linea\b")
ANCHA = re.compile(r"\b(es|son)\b[^.;]{0,40}?\blinea")
EN_LINEA = re.compile(r"\ben\s+(una|la|esa|su|dos|tres)?\s*[^.;]{0,20}?\blinea")

men, est_lit, ancha, en_l, sin = [], [], [], [], []
print("=" * 90)
print("LAS 18 RAZONES DEL GRUPO C, LEIDAS POR VARA PROPIA DEL AUDITOR 96")
print("=" * 90)
for p in GRUPO_C:
    r = V.get(p)
    t = sinac(r.get("razon") if r else "")
    m = bool(MENCIONA.search(t))
    e = bool(ESTRICTA_LITERAL.search(t))
    a = bool(ANCHA.search(t))
    n = bool(EN_LINEA.search(t)) and not a
    (men if m else sin).append(p)
    if e: est_lit.append(p)
    if a: ancha.append(p)
    if n: en_l.append(p)
    frag = ""
    for pat in (ESTRICTA_LITERAL, ANCHA, EN_LINEA, MENCIONA):
        g = pat.search(t)
        if g:
            frag = t[max(0, g.start()-45):g.end()+25]
            break
    print("%5d | menciona=%-5s literal_es_una_linea=%-5s ancha=%-5s en_linea=%-5s | ...%s..."
          % (p, m, e, a, n, frag))

print()
print("| pregunta | cuantas de las 18 |")
print("|---|---:|")
print("| mencionan la palabra linea en cualquier forma | %d |" % len(men))
print("| formula LITERAL 'es/son UNA (sola) LINEA' | %d |" % len(est_lit))
print("| formula ANCHA 'es/son ... linea' | %d |" % len(ancha))
print("| anclan con 'en ... linea' y NO con 'es/son' | %d |" % len(en_l))
print("| NO mencionan la palabra linea | %d |" % len(sin))
print()
print("ENUMERACION menciona (%d): %s" % (len(men), men))
print("ENUMERACION literal  (%d): %s" % (len(est_lit), est_lit))
print("ENUMERACION ancha    (%d): %s" % (len(ancha), ancha))
print("ENUMERACION en_linea (%d): %s" % (len(en_l), en_l))
print("ENUMERACION sin      (%d): %s" % (len(sin), sin))
print()
ACTA95_OCHO = [896, 909, 910, 940, 993, 1057, 1086, 1196]
print("EL OCHO DEL ACTA 95:", ACTA95_OCHO)
print("  de esos ocho, NO casan mi formula literal:",
      [p for p in ACTA95_OCHO if p not in est_lit])
print("  en mi literal y NO en el ocho del acta:",
      [p for p in est_lit if p not in ACTA95_OCHO])
