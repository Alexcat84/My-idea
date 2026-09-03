# -*- coding: utf-8 -*-
"""Auditor vuelta 151: censo y aristas propios. Escrito hoy, sin leer cifra ajena.
union = |{(a,b) de nodos_siguientes} U {(a,b) de nodos_previos invertidas}|"""
import json, sys, subprocess

def cargar(ref):
    if ref == 'WORK':
        return json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))
    b = subprocess.run(['git','show','%s:dataset/metadata/master_graph.json'%ref], capture_output=True)
    if b.returncode: raise SystemExit('ROJO: no se pudo leer '+ref)
    return json.loads(b.stdout.decode('utf-8'))

for ref in sys.argv[1:]:
    N = cargar(ref)['nodos']
    vivos=depre=sig=prev=auto=0
    S=set(); P=set()
    for nid,n in N.items():
        if n.get('deprecado'): depre+=1
        else: vivos+=1
        s=n.get('nodos_siguientes') or []
        q=n.get('nodos_previos') or []
        sig+=len(s); prev+=len(q)
        for d in s:
            if d==nid: auto+=1
            S.add((nid,d))
        for d in q:
            if d==nid: auto+=1
            P.add((d,nid))
    print('%s | nodos %d vivos %d depre %d | sig %d prev %d suma %d union %d | solo_sig %d solo_prev %d auto %d'
          % (ref,len(N),vivos,depre,sig,prev,sig+prev,len(S|P),len(S-P),len(P-S),auto))
