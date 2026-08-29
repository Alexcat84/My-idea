# -*- coding: utf-8 -*-
"""Auditor 127: de donde sale el 51 de la verificacion 1 de OP-S-09, y
cuantos de esos 51 pares se leyeron EXPLICITAMENTE."""
import json, itertools, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
L = os.path.join(RAIZ, "docs", "loop")
fam = {}
for fn in ("SALIDA_V123_OPS09_LECTURA.jsonl", "SALIDA_V124_OPS09_LECTURA_RESTO.jsonl"):
    for l in open(os.path.join(L, fn), encoding="utf-8"):
        if l.strip():
            r = json.loads(l); fam[r["familia"]] = r
rel = [json.loads(l) for l in open(os.path.join(L, "SALIDA_V125_OPS09_RELECTURA_CONJUNTA.jsonl"), encoding="utf-8") if l.strip()]
explicitos = {}
for r in fam.values():
    for p in r["pares"]:
        explicitos[frozenset((p["a"], p["b"]))] = p["veredicto"]
relset = {}
for r in rel:
    par = r["par"]
    if isinstance(par, str): par = json.loads(par.replace("'", '"'))
    relset[frozenset(par)] = r["veredicto_final"]
todos = set()
for r in fam.values():
    for a, b in itertools.combinations(sorted(r["miembros"]), 2):
        todos.add(frozenset((a, b)))
print("familias: %d | miembros unicos: %d | TODOS los pares C(n,2): %d" % (len(fam), len({m for r in fam.values() for m in r['miembros']}), len(todos)))
print("pares LEIDOS explicitamente en los dos registros: %d" % len(explicitos))
print("pares de la relectura conjunta 125: %d" % len(relset))
implicitos = todos - set(explicitos)
print("pares IMPLICITOS (nunca leidos par a par): %d" % len(implicitos))
print("  de ellos, leidos despues en la relectura conjunta: %d" % len(implicitos & set(relset)))
print("  y su veredicto: %r" % [relset[p] for p in implicitos & set(relset)])
print("  quedan implicitos SIN lectura explicita: %d" % len(implicitos - set(relset)))
rep = [p for p, v in explicitos.items() if v == "REPITE"] + [p for p, v in relset.items() if v == "REPITE"]
print("REPITE totales: %d | CONTINUA por diferencia: %d" % (len(set(rep)), len(todos) - len(set(rep))))
