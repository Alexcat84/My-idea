# -*- coding: utf-8 -*-
"""Instrumento propio del AUDITOR, vuelta 103. Vuelca entregable_esperado y
pasos_accionables de madre e hijo SIN clase, SIN direccion, SIN razon y SIN
paso casado (--modo blind); destapa despues (--modo reveal)."""
import argparse, io, json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
DC = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
def cargar(r):
    return [json.loads(l) for l in io.open(r, encoding="utf-8") if l.strip()]
def dir_ef(f):
    v = f.get("direccion_leida")
    for k in sorted(x for x in f if x.startswith("correccion_v")):
        if f[k].get("campo_corregido") == "direccion_leida":
            v = f[k].get("valor_nuevo")
    return v
def nodo(nid):
    return json.load(io.open(os.path.join(NODOS, "%s.json" % nid), encoding="utf-8"))
ap = argparse.ArgumentParser()
ap.add_argument("--modo", choices=["blind", "reveal"], required=True)
ap.add_argument("--puestos", nargs="+", type=int, required=True)
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")
t1 = {f["puesto_tramo"]: f for f in cargar(T1)}
dc = cargar(DC)
for p in a.puestos:
    f = t1[p]
    d = dc[p - 1]
    assert d.get("madre") == f.get("madre_de_la_bolsa") and d.get("hijo") == f.get("hijo_de_la_bolsa"), p
    print("=" * 100)
    print("PUESTO %d  (titulo_ratio %s)" % (p, d.get("titulo_ratio")))
    if a.modo == "blind":
        for rol, nid in (("A", f["madre_de_la_bolsa"]), ("B", f["hijo_de_la_bolsa"])):
            n = nodo(nid)
            print("-- NODO %s: %s" % (rol, nid))
            print("   titulo: %s" % n.get("titulo_concepto"))
            print("   entregable: %s" % (n.get("entregable_esperado") or "")[:400])
            for i, pa in enumerate(n.get("pasos_accionables") or [], 1):
                print("   paso %d: %s" % (i, pa if isinstance(pa, str) else json.dumps(pa, ensure_ascii=False))[:500])
    else:
        print("  madre_de_la_bolsa: %s" % f.get("madre_de_la_bolsa"))
        print("  hijo_de_la_bolsa: %s" % f.get("hijo_de_la_bolsa"))
        print("  paso_casado: %s" % f.get("paso_casado"))
        print("  clase: %s" % f.get("clase"))
        print("  direccion EFECTIVA: %s" % (dir_ef(f) or "NO RESUELTA"))
        print("  razon: %s" % f.get("razon"))
