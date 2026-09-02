# -*- coding: utf-8 -*-
"""Auditor v141: diff de CONJUNTOS de aristas y de numero de pasos entre dos
arboles de nodos, para nombrar una por una las aristas que la vuelta movio.
USO: python docs/loop/_auditor_v141_diffaristas.py <raiz apertura> <raiz cierre>"""
import json, os, glob, sys
def leer(raiz):
    S=set(); P=set(); pasos={}
    for p in glob.glob(os.path.join(raiz,"*.json")):
        d=json.load(open(p,encoding="utf-8"))
        nid=d.get("id") or os.path.splitext(os.path.basename(p))[0]
        for t in d.get("nodos_siguientes") or []: S.add((nid,t))
        for t in d.get("nodos_previos") or []: P.add((t,nid))
        pasos[nid]=len(d.get("pasos_accionables") or [])
    return S,P,pasos
Sa,Pa,pa = leer(sys.argv[1])
Sb,Pb,pb = leer(sys.argv[2])
print("SIGUIENTES anadidas:", sorted(Sb-Sa))
print("SIGUIENTES retiradas:", sorted(Sa-Sb))
print("PREVIOS anadidas:", sorted(Pb-Pa))
print("PREVIOS retiradas:", sorted(Pa-Pb))
print("UNION anadidas:", sorted((Sb|Pb)-(Sa|Pa)))
print("UNION retiradas:", sorted((Sa|Pa)-(Sb|Pb)))
cambios=[(k,pa.get(k),pb.get(k)) for k in set(pa)|set(pb) if pa.get(k)!=pb.get(k)]
print("NODOS CON CAMBIO DE PASOS:", sorted(cambios))
