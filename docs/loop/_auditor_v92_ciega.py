# -*- coding: utf-8 -*-
"""RELECTURA CIEGA del auditor v92. Imprime SOLO los pasos de los dos nodos.
La razon NO se imprime aqui: se destapa con --destapar DESPUES de adjudicar."""
import io, json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V = {int(v["puesto_intra"]): v for v in (json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","INTRA_DOMINIO_VEREDICTOS.jsonl"),encoding="utf-8") if l.strip())}
DIR = {f["puesto"]: f for f in (json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","plan","OP_E_07_DIRECCION_V91.jsonl"),encoding="utf-8") if l.strip())}

def nodo(nid):
    p = os.path.join(RAIZ,"dataset","nodos","%s.json" % nid)
    if not os.path.exists(p): return None
    return json.load(io.open(p, encoding="utf-8"))

def ficha(nid):
    n = nodo(nid)
    if n is None:
        print("  (no existe fichero de nodo para %s)" % nid); return
    print("  NODO: %s" % nid)
    print("  TITULO: %s" % n.get("titulo_concepto"))
    print("  ENTREGABLE: %s" % n.get("entregable_esperado"))
    print("  PASOS:")
    for i, s in enumerate(n.get("pasos_accionables") or [], 1):
        print("    %d. %s" % (i, s))

destapar = "--destapar" in sys.argv
puestos = [int(a) for a in sys.argv[1:] if a.isdigit()]
for p in puestos:
    v = V[p]
    print("=" * 88)
    print("PUESTO %s | dominio %s | clase %s | %s  CONTRA  %s" % (p, v.get("dominio"), v.get("clase"), v.get("nodo_a"), v.get("nodo_b")))
    print("=" * 88)
    ficha(v.get("nodo_a")); print()
    ficha(v.get("nodo_b")); print()
    if destapar:
        print("  --- RAZON ESCRITA ---")
        print("  " + v["razon"])
        d = DIR.get(p)
        print("  --- DIRECCION QUE EL EJECUTOR ESCRIBIO: %s -> %s" % (d["madre"], d["hijo"]) if d else "  (sin fila)")
        print()
