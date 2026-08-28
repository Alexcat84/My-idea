import json, hashlib
P='dataset/metadata/master_graph.json'
raw=open(P,'rb').read()
print('bytes', len(raw), 'sha256', hashlib.sha256(raw).hexdigest()[:20])
g=json.loads(raw.decode('utf-8'))
nod=g['nodos']
items=list(nod.values()) if isinstance(nod,dict) else nod
print('total_nodos declarado', g.get('total_nodos'), 'contados', len(items))
def dep(n): return bool(n.get('deprecated') or n.get('deprecado') or n.get('estado')=='deprecado')
vivos=[n for n in items if not dep(n)]
print('censo nodos/vivos/deprecados', len(items), len(vivos), len(items)-len(vivos))
sig=prev=auto=dupn=0; union=set()
ids=set()
for n in items:
    nid=n.get('id') or n.get('id_nodo') or n.get('node_id')
    ids.add(nid)
    s=n.get('nodos_siguientes') or []
    p=n.get('nodos_previos') or []
    sig+=len(s); prev+=len(p)
    if nid in s or nid in p: auto+=1
    if len(set(s))!=len(s) or len(set(p))!=len(p): dupn+=1
    for d in s: union.add((nid,d))
    for o in p: union.add((o,nid))
print('siguientes',sig,'previos',prev,'suma',sig+prev,'union',len(union))
print('auto-aristas',auto,'nodos con arista duplicada',dupn)
