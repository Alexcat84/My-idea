import json, hashlib
p='dataset/metadata/master_graph.json'
b=open(p,'rb').read()
print('bytes', len(b), 'sha256', hashlib.sha256(b).hexdigest()[:20])
g=json.loads(b.decode('utf-8'))
nodos=g['nodos']
items=list(nodos.items())
print('censo nodos', len(items), '| total_nodos declarado', g.get('total_nodos'))
dep=[i for i,n in items if bool(n.get('deprecado'))]
print('vivos', len(items)-len(dep), 'deprecados', len(dep))
sig=prev=auto=dup=0; union=set()
for i,n in items:
    s=[x['id'] if isinstance(x,dict) else x for x in (n.get('nodos_siguientes') or [])]
    pv=[x['id'] if isinstance(x,dict) else x for x in (n.get('nodos_previos') or [])]
    sig+=len(s); prev+=len(pv)
    if len(set(s))!=len(s) or len(set(pv))!=len(pv): dup+=1
    for t in s:
        if t==i: auto+=1
        union.add((i,t))
    for t in pv:
        if t==i: auto+=1
        union.add((t,i))
print('nodos_siguientes', sig, 'nodos_previos', prev, 'suma', sig+prev, 'union dirigida', len(union))
print('auto-aristas', auto, 'nodos con duplicada en lista', dup)
