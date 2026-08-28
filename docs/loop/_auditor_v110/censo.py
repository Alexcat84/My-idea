import json, hashlib, collections
p='dataset/metadata/master_graph.json'
b=open(p,'rb').read()
print('bytes',len(b),'sha256',hashlib.sha256(b).hexdigest()[:20])
g=json.loads(b.decode('utf-8'))
nodos=g['nodos']
tot=len(nodos); dep=sum(1 for k,v in nodos.items() if v.get('deprecado')); viv=tot-dep
sig=prev=0; auto=0; dup=0; union=set()
for k,v in nodos.items():
    s=v.get('nodos_siguientes') or []; pr=v.get('nodos_previos') or []
    sig+=len(s); prev+=len(pr)
    if len(set(s))!=len(s) or len(set(pr))!=len(pr): dup+=1
    for d in s:
        if d==k: auto+=1
        union.add((k,d))
    for o in pr:
        if o==k: auto+=1
        union.add((o,k))
print('censo',tot,'/',viv,'vivos /',dep,'deprecados')
print('sig',sig,'prev',prev,'suma',sig+prev,'union',len(union))
print('auto-aristas',auto,'nodos con duplicada',dup)
