# -*- coding: utf-8 -*-
"""Vara PROPIA del auditor v92, con red MAS ANCHA que la del guarda del ejecutor:
busca en las 87 razones que SE QUEDAN cualquier formula que NIEGUE la jerarquia,
no solo las tres que el guarda conoce."""
import io, json, os, re
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V = {int(v["puesto_intra"]): v for v in (json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","INTRA_DOMINIO_VEREDICTOS.jsonl"),encoding="utf-8") if l.strip())}
filas = [json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","plan","OP_E_07_DIRECCION_V92.jsonl"),encoding="utf-8") if l.strip()]

# RED ANCHA: las tres del guarda MAS once formulas mas que el guarda NO conoce.
PATRONES = [
    ("no crea jerarquia", r"no crea jerarqu[ií]a"),
    ("ninguno la expande", r"ninguno la expande"),
    ("sin jerarquia", r"sin jerarqu[ií]a"),
    ("linea compartida", r"l[ií]nea\s+compartid"),
    ("no la expande", r"no la expande"),
    ("ninguno de los dos", r"ninguno de los dos"),
    ("cada uno trae lo suyo", r"cada uno trae lo suyo"),
    ("los dos lo dicen", r"los dos lo dicen"),
    ("en un solo paso", r"en un solo paso"),
    ("ENLACE MUTUO / 9.22", r"enlace mutuo|9\.22"),
    ("no hay madre", r"no hay madre|no es madre|no son madre"),
    ("simetric", r"sim[eé]tric"),
    ("mutuo/mutua", r"\bmutu[oa]"),
    ("de ida y vuelta", r"de ida y vuelta"),
    ("no expande", r"no expande"),
]
COMP = [(n, re.compile(p, re.IGNORECASE)) for n, p in PATRONES]
tocados = []
for f in filas:
    p = f["puesto"]
    r = V[p]["razon"]
    hits = [n for n, c in COMP if c.search(r)]
    if hits:
        tocados.append((p, hits))
print("filas barridas: %d" % len(filas))
print("filas que TOCAN alguna formula de negacion (red ancha): %d" % len(tocados))
for p, h in tocados:
    print("  puesto %s: %s" % (p, h))
    print("     %s" % V[p]["razon"][-420:].replace("\n"," "))
    print()
