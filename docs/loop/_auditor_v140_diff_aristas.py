import json, os, glob, sys
def load(D):
    nodos={}
    for f in glob.glob(os.path.join(D,'*.json')):
        d=json.load(open(f,encoding='utf-8'))
        nid=d.get('id') or os.path.basename(f)[:-5]
        nodos[nid]=d
    return nodos
def edges(nodos):
    sig=set(); prev=set()
    for n,d in nodos.items():
        for x in (d.get('nodos_siguientes') or []): sig.add((n,x))
        for x in (d.get('nodos_previos') or []): prev.add((x,n))
    return sig,prev
a=load('./_aud140_open/dataset/nodos')
b=load('dataset/nodos')
sa,pa=edges(a); sb,pb=edges(b)
print("SIG anadidas:", sorted(sb-sa))
print("SIG quitadas:", sorted(sa-sb))
print("PREV anadidas:", sorted(pb-pa))
print("PREV quitadas:", sorted(pa-pb))
# pasos cambiados
for n in b:
    if n in a and json.dumps(a[n].get('pasos'),ensure_ascii=False)!=json.dumps(b[n].get('pasos'),ensure_ascii=False):
        print("PASOS CAMBIAN:",n,len(a[n].get('pasos') or []),"->",len(b[n].get('pasos') or []))
