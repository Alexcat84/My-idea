import json, hashlib
p='dataset/metadata/master_graph.json'
b=open(p,'rb').read()
print('bytes', len(b), 'sha256', hashlib.sha256(b).hexdigest()[:20])
g=json.loads(b.decode('utf-8'))
nodes=g['nodos']
items=list(nodes.items()) if isinstance(nodes,dict) else [(n['id'],n) for n in nodes]
print('censo nodos', len(items))
def esta_depr(n):
    for k in ('deprecado','deprecated','esta_deprecado'):
        if k in n: return bool(n[k])
    est=n.get('estado') or n.get('status')
    if est: return str(est).lower().startswith('deprec')
    return False
vivos=[i for i,n in items if not esta_depr(n)]
print('vivos', len(vivos), 'deprecados', len(items)-len(vivos))
sig=prev=auto=dup=0; union=set()
for i,n in items:
    s=n.get('nodos_siguientes') or []; pv=n.get('nodos_previos') or []
    s=[x['id'] if isinstance(x,dict) else x for x in s]
    pv=[x['id'] if isinstance(x,dict) else x for x in pv]
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
