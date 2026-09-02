# -*- coding: utf-8 -*-
"""Instrumento propio del auditor v141 para la RELECTURA CIEGA: imprime los dos
nodos de cada uno de los seis pares enteros (pasos numerados EN EL NODO DE HOY)
y el estado de las dos direcciones en las DOS vistas con resolutor propio.
Se corre ANTES de abrir SALIDA_V141_3B_VARA_922.txt. NO lee ninguna salida del
ejecutor ni ninguna ficha del plan."""
import json, os, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
RAIZ = "dataset/nodos"
N = {}
ALIAS = {}
for p in glob.glob(os.path.join(RAIZ, "*.json")):
    d = json.load(open(p, encoding="utf-8"))
    nid = d.get("node_id") or os.path.splitext(os.path.basename(p))[0]
    N[nid] = d
    for a in d.get("ids_alias") or []:
        ALIAS[a] = nid
def R(x):
    v = x
    for _ in range(10):
        if v in N and not N[v].get("deprecado"): return v
        if v in ALIAS and ALIAS[v] != v: v = ALIAS[v]; continue
        return v
    return v
SIG = {}; PREV = {}
for nid, d in N.items():
    SIG[nid] = [R(t) for t in (d.get("nodos_siguientes") or [])]
    PREV[nid] = [R(t) for t in (d.get("nodos_previos") or [])]
def existe(a, b):
    a, b = R(a), R(b)
    return (b in SIG.get(a, [])), (a in PREV.get(b, []))
PARES = [
 ("sistema_gates_go_kill", "gestion_portafolio_dos_niveles"),
 ("sistema_gates_go_kill", "gestion_portafolio_formal"),
 ("sistema_gates_go_kill", "portfolio_management"),
 ("sistema_gates_go_kill", "gestion_portafolio_foco"),
 ("sistema_gates_go_kill", "revision_portafolio_periodica"),
 ("sistema_gates_go_kill", "asignacion_recursos_en_gates"),
]
vistos = set()
for i,(a,b) in enumerate(PARES, 1):
    print("="*78)
    print("PAR %d: %s  CONTRA  %s" % (i, a, b))
    print("="*78)
    for nid in (a, b):
        if nid in vistos and nid == "sistema_gates_go_kill":
            print("\n--- %s (ya impreso arriba, pasos identicos) ---" % nid); continue
        vistos.add(nid)
        d = N[R(nid)]
        print("\n--- NODO %s  (vivo=%s, resuelto=%s) ---" % (nid, not d.get("deprecado"), R(nid)))
        print("TITULO: %s" % d.get("titulo_concepto"))
        print("RESUMEN: %s" % (d.get("resumen_teorico") or "")[:600])
        for j, s in enumerate(d.get("pasos_accionables") or [], 1):
            print("  paso %2d: %s" % (j, s))
    s1, p1 = existe(a, b); s2, p2 = existe(b, a)
    print("\nESTADO HOY: %s -> %s  sig=%s prev=%s   |   %s -> %s  sig=%s prev=%s"
          % (a, b, s1, p1, b, a, s2, p2))
