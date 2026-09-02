import json, os, glob
D='dataset/nodos'
nodos={}
for f in glob.glob(os.path.join(D,'*.json')):
    d=json.load(open(f,encoding='utf-8'))
    nid=d.get('id') or os.path.basename(f)[:-5]
    nodos[nid]=d
vivos=[n for n,d in nodos.items() if not d.get('deprecado')]
depre=[n for n,d in nodos.items() if d.get('deprecado')]
sig=set(); prev=set(); nsig=0; nprev=0; auto=0; dup=0
for n,d in nodos.items():
    s=d.get('nodos_siguientes') or []
    p=d.get('nodos_previos') or []
    nsig+=len(s); nprev+=len(p)
    if len(set(s))!=len(s) or len(set(p))!=len(p): dup+=1
    for x in s:
        if x==n: auto+=1
        sig.add((n,x))
    for x in p:
        if x==n: auto+=1
        prev.add((x,n))
union=sig|prev
print("nodos %d vivos %d depre %d | sig %d prev %d suma %d union %d | solo_sig %d solo_prev %d auto %d dup %d"%(
    len(nodos),len(vivos),len(depre),nsig,nprev,nsig+nprev,len(union),len(sig-prev),len(prev-sig),auto,dup))
