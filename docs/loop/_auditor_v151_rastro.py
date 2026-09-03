# -*- coding: utf-8 -*-
"""Auditor v151: rastro propio de docs/plan/ARISTAS_DUPLICADAS.jsonl.
Recorre TODAS las versiones en git (orden cronologico de git log --reverse),
y por cada una: grupos, nodos distintos, suma de 'sobran'. Ademas mide, sobre
la version de HEAD, cuantas caen sobre nodos deprecados / ausentes / vivos."""
import json, subprocess

R = 'docs/plan/ARISTAS_DUPLICADAS.jsonl'
revs = subprocess.run(['git','log','--reverse','--format=%h','--follow','--',R],
                      capture_output=True, text=True).stdout.split()
print('VERSIONES EN GIT:', len(revs))

def leer(rev):
    b = subprocess.run(['git','show','%s:%s'%(rev,R)], capture_output=True)
    if b.returncode: return None
    filas=[json.loads(l) for l in b.stdout.decode('utf-8').splitlines() if l.strip()]
    return filas

prev=None; subidas=[]; serie=[]
for r in revs:
    f = leer(r)
    if f is None: continue
    g=len(f); n=len({x['nodo'] for x in f}); s=sum(x['sobran'] for x in f)
    serie.append((r,g,n,s))
    if prev is not None and s > prev[3]:
        subidas.append((prev[0],prev[3],r,s))
    prev=serie[-1]

print('PRIMERA:', serie[0])
print('ULTIMA :', serie[-1])
print('TRANSICIONES QUE SUBEN:', len(subidas))
for a,va,b,vb in subidas:
    anc = subprocess.run(['git','merge-base','--is-ancestor',a,b]).returncode
    print('   %s (%d) -> %s (%d) | %s es ancestro de %s: %s' % (a,va,b,vb,a,b,'SI' if anc==0 else 'NO'))
print('TRANSICIONES TOTALES:', len(serie)-1, '| que NO suben:', len(serie)-1-len(subidas))

G = json.load(open('dataset/metadata/master_graph.json',encoding='utf-8'))['nodos']
f = leer(revs[-1])
dep=aus=viv=0
for x in f:
    nid=x['nodo']
    if nid not in G: aus+=x['sobran']
    elif G[nid].get('deprecado'): dep+=x['sobran']
    else: viv+=x['sobran']
print('HEAD: sobran sobre DEPRECADOS %d | AUSENTES %d | VIVOS %d | total %d' % (dep,aus,viv,dep+aus+viv))
