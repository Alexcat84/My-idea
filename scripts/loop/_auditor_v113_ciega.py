# -*- coding: utf-8 -*-
"""_auditor_v113_ciega.py . Vuelca los pares del auditor SIN la razon vieja
(relectura ciega, AUDITOR.md 1.2). Con --destapar imprime SOLO razon, vara y
correcciones."""
import json, io, re, sys, argparse, os
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ap = argparse.ArgumentParser()
ap.add_argument("puestos", nargs="+", type=int)
ap.add_argument("--destapar", action="store_true")
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")
FILAS = {}
for f in ["OP_E_03_LECTURA_TRAMO1_V96.jsonl","OP_E_03_LECTURA_TRAMO2_V97.jsonl",
          "OP_E_03_LECTURA_TRAMO3_V98.jsonl","OP_E_03_LECTURA_TRAMO4_V99.jsonl"]:
    for l in io.open(os.path.join(RAIZ,"docs","plan",f), encoding="utf-8"):
        if l.strip():
            d = json.loads(l); FILAS[d["puesto_tramo"]] = d
G = json.load(io.open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"), encoding="utf-8"))["nodos"]
def pinta(nid, rol):
    n = G.get(nid)
    if n is None:
        print("  %s %s :: NO ESTA EN EL GRAFO" % (rol, nid)); return
    print("  %s %s" % (rol, nid))
    print("     titulo: %s" % n.get("titulo_concepto"))
    print("     resumen: %s" % (n.get("resumen_teorico") or "")[:700])
    for i, p in enumerate(n.get("pasos_accionables") or [], 1):
        print("       paso %d: %s" % (i, p))
    print("     entregable: %s" % n.get("entregable_esperado"))
    print("     deprecado: %s | dominio: %s" % (n.get("deprecado"), n.get("dominio")))
for p in a.puestos:
    d = FILAS[p]
    print("="*100)
    print("PUESTO %d | dominio %s | paso casado de la madre: %s" % (p, d["dominio"], d.get("paso_casado")))
    if a.destapar:
        print("  clase: %s" % d.get("clase"))
        print("  direccion_leida (cruda): %s" % d.get("direccion_leida"))
        print("  RAZON VIEJA: %s" % d.get("razon"))
        print("  VARA: %s" % d.get("vara"))
        for k, v in d.items():
            if re.match(r"^correccion_v\d+$", k):
                print("  %s: %s" % (k, json.dumps(v, ensure_ascii=False)))
    else:
        pinta(d["madre_de_la_bolsa"], "MADRE")
        print("  " + "-"*90)
        pinta(d["hijo_de_la_bolsa"], "HIJO ")
