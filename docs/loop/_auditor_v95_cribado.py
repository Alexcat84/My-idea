# -*- coding: utf-8 -*-
"""_auditor_v95_cribado.py . EL CRIBADO DE CITA DE LINEA, TERCERA
IMPLEMENTACION, escrita por el auditor de la vuelta 95 sin mirar la del
ejecutor para afinarla. Ademas del cribado con los patrones del acta 94, mide
LA ESTABILIDAD del grupo C bajo tres varas mas anchas y mas estrechas, que es
lo que decide si la lista de 18 es un hecho o un artefacto de los patrones.

    python docs/loop/_auditor_v95_cribado.py > docs/loop/_auditor_v95_cribado.txt
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENTRADA = os.path.join(RAIZ, "docs", "plan", "OP_E_07_DIRECCION_V94.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


filas = cargar(ENTRADA)
ver = {int(v["puesto_intra"]): v for v in cargar(VEREDICTOS)}
pares = [(f["puesto"], ver[f["puesto"]]["razon"]) for f in filas]
print("bolsa vigente:", len(pares))

NUM = r"(?:\d+|un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|media)"

VARAS = {
    # 1. LA DEL ACTA, escrita por mi de su prosa
    "acta": (
        [r"\bpaso\s+\d+\b",
         r"\ben\s+(?:una|dos|tres|media)\s+l[ií]neas?\b",
         r"\bdice\s+" + NUM + r"\s+l[ií]neas?\b",
         r"\b(?:primera|segunda|tercera)\s+l[ií]nea\b",
         r"\buna\s+de\s+sus\s+l[ií]neas\b",
         r"\bentre\s+sus\s+pasos\b"],
        [r"\bes\s+el\s+[ií]ndice\b", r"\benumera\w*\b", r"\benuncia\w*\b"],
    ),
    # 2. LA MAS ANCHA QUE SE ME OCURRE: cualquier mencion de paso numerado o
    #    de la palabra linea, y cualquier forma de indice o enumeracion
    "ancha": (
        [r"\bpasos?\s+\d+\b", r"l[ií]neas?\b"],
        [r"[ií]ndice", r"\benumer\w*\b", r"\benunci\w*\b", r"\blist\w*\b"],
    ),
    # 3. LA MAS ESTRECHA: solo paso numerado explicito
    "estrecha": (
        [r"\bpaso\s+\d+\b"],
        [r"\bes\s+el\s+[ií]ndice\b"],
    ),
}

resultados = {}
for nombre, (pa, pb) in VARAS.items():
    ra = [re.compile(p, re.IGNORECASE) for p in pa]
    rb = [re.compile(p, re.IGNORECASE) for p in pb]
    g = {"A": [], "B": [], "C": []}
    for puesto, razon in pares:
        if any(p.search(razon) for p in ra):
            g["A"].append(puesto)
        elif any(p.search(razon) for p in rb):
            g["B"].append(puesto)
        else:
            g["C"].append(puesto)
    resultados[nombre] = g
    print("\nVARA '%s': A %d / B %d / C %d" % (nombre, len(g["A"]), len(g["B"]), len(g["C"])))
    print("  B:", g["B"])
    print("  C:", g["C"])

c_acta = set(resultados["acta"]["C"])
print("\n--- ESTABILIDAD DEL GRUPO C ---")
for nombre in ("ancha", "estrecha"):
    c = set(resultados[nombre]["C"])
    print("vara '%s': |C|=%d | comparte con la del acta %d | solo en el acta %s | solo en '%s' %s"
          % (nombre, len(c), len(c & c_acta), sorted(c_acta - c), nombre, sorted(c - c_acta)))

print("\n--- LAS VARAS DE SENTIDO ---")
for p in (1098, 1009, 1281, 1992, 1083):
    fila = dict(pares).get(p)
    donde = [n for n in VARAS if p in resultados[n]["C"]]
    print("  puesto %5d | %s | en C bajo las varas: %s"
          % (p, "en la bolsa" if fila is not None else "FUERA de la bolsa vigente", donde or "ninguna"))
