# -*- coding: utf-8 -*-
"""_auditor_v95_hueco_patron.py . EL HUECO DEL CRIBADO DE CITA DE LINEA:
el grupo A del acta 94 casa "EN una/dos/tres/media linea(s)" pero NO casa
"ES una linea", "SON lineas" ni "en una SOLA linea", que es como el redactor
escribe la mayoria de sus anclas. Este instrumento mide cuantas de las 18
razones del grupo C citan una linea de todos modos, y con que formula.

    python docs/loop/_auditor_v95_hueco_patron.py > docs/loop/_auditor_v95_hueco_patron.txt
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
C = [886, 890, 896, 909, 910, 940, 947, 983, 993, 1020, 1057, 1083, 1086, 1191, 1196, 1220, 1844, 1886]


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


ver = {int(v["puesto_intra"]): v for v in cargar(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"))}

# el patron del acta (grupo A), tal como el acta 94 lo describe
ACTA_A = re.compile(r"\bpaso\s+\d+\b|\ben\s+(?:una|dos|tres|media)\s+l[ií]neas?\b|"
                    r"\bdice\s+(?:\d+|un|una|dos|tres|cuatro|cinco|seis|siete|ocho)\s+l[ií]neas?\b|"
                    r"\b(?:primera|segunda|tercera)\s+l[ií]nea\b|\buna\s+de\s+sus\s+l[ií]neas\b|"
                    r"\bentre\s+sus\s+pasos\b", re.IGNORECASE)
# la formula que el acta NO casa y que el redactor si usa
HUECO = re.compile(r"\b(?:es|son|es\s+la|queda\s+en)\s+(?:una|dos|tres|la)?\s*l[ií]neas?\b|"
                   r"\ben\s+una\s+sola\s+l[ií]nea\b|\bson\s+l[ií]neas\b", re.IGNORECASE)
CUALQUIER_LINEA = re.compile(r"l[ií]neas?\b", re.IGNORECASE)
# ancla a UN paso ordinal escrito ("ese tercer paso", "su primer paso")
ORDINAL = re.compile(r"\b(?:primer|segundo|tercer|cuarto|quinto|sexto|septimo|octavo)o?\s+paso\b|"
                     r"\ben\s+la\s+(?:primera|segunda|tercera|cuarta)\b", re.IGNORECASE)

print("las 18 del grupo C del acta 94, remedidas hoy:\n")
print("| puesto | casa el patron A del acta | trae 'es/son linea' | trae ordinal de paso | menciona 'linea' |")
print("|---:|---|---|---|---|")
n_hueco = n_ord = n_cualq = 0
enum_hueco = []
for p in C:
    r = ver[p]["razon"]
    a = bool(ACTA_A.search(r))
    h = bool(HUECO.search(r))
    o = bool(ORDINAL.search(r))
    c = bool(CUALQUIER_LINEA.search(r))
    n_hueco += h
    n_ord += o
    n_cualq += c
    if h:
        enum_hueco.append(p)
    print("| %d | %s | %s | %s | %s |" % (p, a, h, o, c))

print("\nde las 18: %d traen 'es/son linea' (el hueco), %d traen ordinal de paso, %d mencionan 'linea'"
      % (n_hueco, n_ord, n_cualq))
print("ENUMERACION de las que traen 'es/son linea':", enum_hueco)
print("\nlas frases literales, para que no haya que creerme:")
for p in enum_hueco:
    r = ver[p]["razon"]
    m = HUECO.search(r)
    ini = max(0, m.start() - 70)
    print("  %5d ... %s ..." % (p, r[ini:m.end() + 40].replace("\n", " ")))

print("\n\n--- LA VARA MECANICA CONTRA EL VEREDICTO DEL EJECUTOR ---")
QUEDAN = [896, 909, 910, 940, 983, 993, 1020, 1057, 1086, 1196, 1220]
RELECTURA = [886, 890, 947, 1844]
PRERESUELTOS = [1083, 1191, 1886]
OTRO_ANCLA = re.compile(r"\bUNA\s+de\s+las\s+(?:ocho|cinco|tres|cuatro)\b|\bes\s+la\s+MADRE\b", re.IGNORECASE)
mia_quedan, mia_relectura = [], []
for p in QUEDAN + RELECTURA:
    r = ver[p]["razon"]
    if CUALQUIER_LINEA.search(r) or OTRO_ANCLA.search(r):
        mia_quedan.append(p)
    else:
        mia_relectura.append(p)
print("MI vara (menciona 'linea' O designador explicito) -> QUEDAN:", sorted(mia_quedan))
print("MI vara -> SIN ancla:", sorted(mia_relectura))
print("el ejecutor    -> QUEDAN:", sorted(QUEDAN))
print("el ejecutor    -> RELECTURA CONJUNTA:", sorted(RELECTURA))
print("COINCIDEN LAS DOS LISTAS:", sorted(mia_quedan) == sorted(QUEDAN) and sorted(mia_relectura) == sorted(RELECTURA))
