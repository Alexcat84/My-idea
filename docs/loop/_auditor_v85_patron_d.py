# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 85. Comprueba la afirmacion de la seccion 5 del reporte:
"en los tramos 8 y 9, los pares con veredicto D coincidieron SIEMPRE con la
decision NO SE ENLAZA". Los pares se LEEN del registro; ninguno se teclea.

  python docs/loop/_auditor_v85_patron_d.py > docs/loop/_auditor_v85_patron_d.txt
"""
import json

REG = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"


def filas(ruta):
    return [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]


ver = {}
for v in filas(VER):
    ver[frozenset((v["nodo_a"], v["nodo_b"]))] = v

reg = filas(REG)
for tramo in (8, 9, 10):
    print()
    print("--- TRAMO %d: pares del registro CON veredicto en el marcador ---" % tramo)
    n = 0
    for r in reg:
        if r["tramo"] != tramo:
            continue
        v = ver.get(frozenset((r["madre"], r["hijo"])))
        if not v:
            continue
        n += 1
        print("    %-100s clase %s puesto %-5d decision HOY: %s"
              % ("%s -> %s" % (r["madre"], r["hijo"]), v["clase"],
                 v["puesto_intra"], r["decision"]))
    if n == 0:
        print("    (ninguno)")
