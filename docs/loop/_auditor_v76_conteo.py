import json,sys
p = sys.argv[1] if len(sys.argv)>1 else 'dataset/metadata/master_graph.json'
G=json.load(open(p,encoding='utf-8'))
N=G['nodos']
sig=prev=0; ps=set(); pp=set(); vivos=0; depre=0
for nid,n in N.items():
    if n.get('deprecado'): depre+=1
    else: vivos+=1
    s=n.get('nodos_siguientes') or []; q=n.get('nodos_previos') or []
    sig+=len(s); prev+=len(q)
    for d in s: ps.add((nid,d))
    for d in q: pp.add((d,nid))
print("nodos:",len(N),"vivos:",vivos,"deprecados:",depre)
print("entradas nodos_siguientes:",sig)
print("entradas nodos_previos:",prev)
print("suma:",sig+prev)
print("union dirigida unica:",len(ps|pp))
print("solo siguientes:",len(ps-pp),"| solo previos:",len(pp-ps))
