# -*- coding: utf-8 -*-
"""AUDITOR v146: mido yo las variantes de unidad de arista, sin leer el
instrumento del ejecutor mas que para tomar el RESOLUTOR DE LA CASA."""
import os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T

def sets(ref):
    nodos = T.cargar_grafo(ref)
    res = T.resolver_de(nodos)
    vivo = lambda k: not (nodos.get(k, {}).get("deprecado") or nodos.get(k, {}).get("deprecated"))
    vivos = set(k for k in nodos if vivo(k))
    def rec(desde_vivos, usar_sig, usar_prev):
        s = set()
        fuente = vivos if desde_vivos else set(nodos)
        for nid in fuente:
            pares = []
            if usar_sig:  pares += [(nid, x) for x in (nodos[nid].get("nodos_siguientes") or [])]
            if usar_prev: pares += [(x, nid) for x in (nodos[nid].get("nodos_previos") or [])]
            for o, d in pares:
                ro, rd = res(o), res(d)
                if ro != rd: s.add((ro, rd))
        return s
    out = {}
    out["1 solo SIGUIENTES, leidas de nodos VIVOS"]       = rec(True, True, False)
    out["2 solo PREVIOS, leidas de nodos VIVOS"]          = rec(True, False, True)
    out["3 UNION de las dos vistas, leidas de VIVOS"]     = rec(True, True, True)
    out["4 UNION de las dos vistas, TODOS los nodos"]     = rec(False, True, True)
    todas = rec(False, True, True)
    out["5 UNION, todos, con la FUENTE resuelta VIVA"]    = set(p for p in todas if p[0] in vivos)
    out["6 UNION de VIVOS, con LOS DOS extremos vivos"]   = set(p for p in out["3 UNION de las dos vistas, leidas de VIVOS"] if p[0] in vivos and p[1] in vivos)
    return out

A, B = sets("5fff85f7"), sets("c72ce2c0")
print("%-48s %8s %8s %7s" % ("UNIDAD", "5fff85f7", "c72ce2c0", "delta"))
for k in sorted(A):
    print("%-48s %8d %8d %+7d" % (k, len(A[k]), len(B[k]), len(B[k]) - len(A[k])))
print()
for k in ["3 UNION de las dos vistas, leidas de VIVOS", "6 UNION de VIVOS, con LOS DOS extremos vivos"]:
    ent, sal = B[k] - A[k], A[k] - B[k]
    print("%s -> ENTRAN %d | SALEN %d" % (k, len(ent), len(sal)))
k3 = "3 UNION de las dos vistas, leidas de VIVOS"; k6 = "6 UNION de VIVOS, con LOS DOS extremos vivos"
print("MISMOS CONJUNTOS entre (3) y (6):", (B[k3]-A[k3]) == (B[k6]-A[k6]) and (A[k3]-B[k3]) == (A[k6]-B[k6]))
print("DIFERENCIA (3) menos (6): antes %d | despues %d" % (len(A[k3])-len(A[k6]), len(B[k3])-len(B[k6])))
