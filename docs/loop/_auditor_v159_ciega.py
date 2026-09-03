# -*- coding: utf-8 -*-
"""AUDITOR VUELTA 159, CIEGA. Imprime SOLO titulo, fuente, entregable y pasos
accionables de los dos nodos de cada lectura dirigida. NI clase, NI via, NI
cita, NI razon. El destape va aparte y despues de sellar mis adjudicaciones."""
import json, os, sys, ast, re, io
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

def registro():
    d = {}
    for l in io.open(REG, encoding="utf-8"):
        l = l.strip()
        if not l: continue
        r = json.loads(l)
        m = re.match(r"(LD-OPC05-\d\d\d)", r["cita"])
        if m: d[m.group(1)] = r
    return d

def nodo(nid):
    p = os.path.join(RAIZ, "dataset", "nodos", nid + ".json")
    return json.load(io.open(p, encoding="utf-8"))

def pasos(n):
    v = n.get("pasos_accionables")
    if isinstance(v, list): return v
    try:
        r = ast.literal_eval(str(v))
        return r if isinstance(r, list) else [str(v)]
    except Exception:
        return [str(v)]

def ficha(nid, rotulo):
    n = nodo(nid)
    print("  %s: %s" % (rotulo, nid))
    print("     titulo    : %s" % n.get("titulo_concepto"))
    print("     fuente    : %s" % n.get("fuente"))
    print("     entregable: %s" % n.get("entregable_esperado"))
    print("     pasos:")
    for i, p in enumerate(pasos(n), 1):
        print("       %2d. %s" % (i, p))

def main(claves):
    reg = registro()
    for k in claves:
        r = reg[k]
        print("=" * 78)
        print("CASO %s" % k)
        print("=" * 78)
        ficha(r["nodo_a_leido"], "NODO A")
        print()
        ficha(r["nodo_b_leido"], "NODO B")
        print()

if __name__ == "__main__":
    main(sys.argv[1:])
