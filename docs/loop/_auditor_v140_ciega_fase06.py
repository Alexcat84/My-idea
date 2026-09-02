# -*- coding: utf-8 -*-
import json, os, glob, re
ops={}
for l in open('docs/plan/OPERACIONES.jsonl',encoding='utf-8'):
    if l.strip():
        o=json.loads(l); ops[o['id_op']]=o
nodos={}
for f in glob.glob('dataset/nodos/*.json'):
    d=json.load(open(f,encoding='utf-8'))
    nodos[d.get('node_id') or os.path.basename(f)[:-5]]=d
alias={}
for n,d in nodos.items():
    for a in (d.get('ids_alias') or []): alias[a]=n
def res(x):
    seen=set()
    while x in alias and x not in seen: seen.add(x); x=alias[x]
    return x
sig=set(); prev=set()
for n,d in nodos.items():
    rn=res(n)
    for x in (d.get('nodos_siguientes') or []): sig.add((rn,res(x)))
    for x in (d.get('nodos_previos') or []): prev.add((res(x),rn))
def vivo(x): return x in nodos and not nodos[x].get('deprecado')

# catalogo: parseado de los dos registros
seis=re.search(r'\*\*las seis fusiones\*\*.*?\|(.*?)\|', open('docs/plan/00_INDICE.md',encoding='utf-8').read(), re.S)
FUS=re.findall(r'`(OP-[A-Z0-9\-]+)`', seis.group(1))
enl=open('docs/plan/04_ENLACES.md',encoding='utf-8').read()
sec=enl.split('SEGUNDA MITAD, LAS CINCO REMITIDAS A LAS MESAS DE LA FASE 06')[1][:2000]
REM=[]
for m in re.finditer(r'^\| `(OP-[A-Z0-9\-]+)` \| `(OP-M-\d+)` \|', sec, re.M): REM.append(m.group(1))
MESAS=[k for k,o in ops.items() if o.get('fase')=='06_MESAS']
cat=sorted(set(MESAS))+FUS+REM
print("CATALOGO (%d): mesas %d, fusiones %d, remitidas %d"%(len(cat),len(MESAS),len(FUS),len(REM)))
print("  fusiones:",FUS); print("  remitidas:",REM)
print()
def parse_ar(s):
    # devuelve lista de pares dirigidos
    out=[]
    head=s.split(',')[0].split('(')[0]
    for chunk in re.split(r'\s+Y\s+', head):
        m=re.match(r'\s*([a-z0-9_]+)\s*->\s*([a-z0-9_]+)', chunk)
        if m: out.append((m.group(1),m.group(2)))
    return out
def destino(k):
    o=ops[k]; t=(o.get('tipo') or '').upper()
    if 'FUSION' in t:
        sup=o.get('superviviente'); elim=o.get('eliminar') or []
        if not sup: return 'SIN VARA (fusion sin superviviente)',''
        ok = vivo(res(sup)) and all((not vivo(e)) and res(e)==res(sup) for e in elim)
        det='sup=%s vivo=%s | absorbidos=%d ok=%d'%(sup,vivo(res(sup)),len(elim),sum(1 for e in elim if not vivo(e) and res(e)==res(sup)))
        return ('CUMPLIDO' if ok else 'SIN CUMPLIR'),det
    if 'ENLACE' in t:
        pares=[]
        for a in (o.get('aristas_nuevas') or []): pares+=parse_ar(a)
        rp=[(res(x),res(y)) for x,y in pares]
        pres=[p for p in set(rp) if p in sig and p in prev]
        return ('CUMPLIDO' if len(pres)==len(set(rp)) else 'SIN CUMPLIR'), '%d de %d direcciones distintas presentes'%(len(pres),len(set(rp)))
    if 'MESA' in t:
        hijas=[h for h in (o.get('bloquea_a') or []) if h in cat]
        return 'MESA(hijas en catalogo: %s)'%(hijas or 'NINGUNA'), ''
    return 'SIN VARA ESCRITA (tipo=%s)'%t,''
cum=[];nocum=[];mesas={}
for k in cat:
    v,det=destino(k)
    print("%-20s %-12s %-45s %s"%(k, ops[k].get('estado'), v, det))
    if v=='CUMPLIDO': cum.append(k)
    elif v.startswith('MESA'): mesas[k]=[h for h in (ops[k].get('bloquea_a') or []) if h in cat]
    else: nocum.append(k)
print()
for k,h in mesas.items():
    ok = bool(h) and all(x in cum for x in h)
    print("MESA %-10s hijas_en_catalogo=%s -> %s"%(k,h,'CUMPLIDO' if ok else 'SIN CUMPLIR'))
    (cum if ok else nocum).append(k)
print()
print("CIFRA: catalogo %d | cumplido %d | sin cumplir %d"%(len(cat),len(cum),len(nocum)))
print("SIN CUMPLIR:",sorted(nocum))
