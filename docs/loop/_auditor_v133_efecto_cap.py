# AUDITOR v133: EFECTO MEDIDO de anadir la abreviatura "Cap./Caps." a la cola.
# Por el ramal (xvi) se miden LAS DOS cifras: grupos Y canonicas resultantes.
import json, glob, collections, re
viv=[json.load(open(p,encoding='utf-8')) for p in sorted(glob.glob('dataset/nodos/*.json'))]
viv=[d for d in viv if not (d.get('deprecated') or d.get('deprecado'))]
c=collections.Counter()
for d in viv:
    f=(d.get('fuente') or '').strip()
    if f: c[f.split('|')[0].strip()]+=1
gr=sorted(c)
def titulo(g): return g.split(' - ')[0].strip()
def resto(g):
    p=g.split(' - ',1); return p[1].strip() if len(p)>1 else ''
V133=r',\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|Anexos?\s+.*|Ap[eé]ndices?\s+.*)$'
CONCAP=r',\s*(cap[ií]tulos?\s+.*|Caps?\.\s*.*|secci[oó]n\s+.*|Anexos?\s+.*|Ap[eé]ndices?\s+.*)$'
def mk(p):
    rx=re.compile(p, re.IGNORECASE)
    def rec(g):
        x=g
        while True:
            y=rx.sub('',x).strip().rstrip(' ;,.:')
            if y==x: return x
            x=y
    return rec
def corre(rec):
    par={g:g for g in gr}
    def find(x):
        while par[x]!=x: x=par[x]
        return x
    def une(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: par[rb]=ra
    for a in gr:
        for b in gr:
            if a!=b and b.startswith(a): une(a,b)
    for a in gr:
        for b in gr:
            if a==b: continue
            ta,tb=titulo(a),titulo(b)
            if not (tb.startswith(ta) and len(ta)>=20 and ta!=tb): continue
            ra,rb=resto(a),resto(b)
            if ra and rb and ra!=rb and not (rb.startswith(ra) or ra.startswith(rb)): continue
            une(a,b)
    b=collections.defaultdict(list)
    for g in gr: b[rec(g)].append(g)
    for k,v in b.items():
        for x in v[1:]: une(v[0],x)
    for a in gr:
        for b2 in gr:
            if a==b2: continue
            ra,rb=rec(a),rec(b2)
            if ra==rb or len(ra)<20 or not rb.startswith(ra): continue
            xa,xb=resto(ra),resto(rb)
            if xa and xb and xa!=xb and not (xb.startswith(xa) or xa.startswith(xb)): continue
            une(a,b2)
    g=collections.defaultdict(list)
    for x in gr: g[find(x)].append(x)
    sint=[]
    for raiz,v in g.items():
        libros=[x for x in v if rec(x)==x]
        if libros: can=max(libros,key=len)
        else: can=rec(max(v,key=len)); sint.append((can,len(v),sum(c[x] for x in v)))
    return g,sint
for nom,p in [('cola de la 133 (vigente)   ',V133),('cola + abreviatura Cap./Caps.',CONCAP)]:
    g,sint=corre(mk(p))
    multi=[v for v in g.values() if len(v)>1]
    print(f'{nom} -> {len(g):3d} grupos | de 2+ {len(multi):2d} ({sum(len(v) for v in multi):3d} grafias) | solos {len(g)-len(multi):3d} | faltan para 55: {len(g)-55} | SINTETICAS {len(sint)}')
    for can,ng,nn in sorted(sint, key=lambda t:-t[2]):
        print(f'      SINTETICA: {can!r} ({ng} grafias, {nn} nodos)')
print()
print('convivencia medida: familias que traen LAS DOS formas (capitulo escrito y Cap. abreviado)')
fam=collections.defaultdict(set)
for g in gr:
    m=re.search(r'^(.*?),\s*(cap[ií]tulos?|Caps?\.)', g, re.IGNORECASE)
    if m: fam[m.group(1)].add('escrito' if m.group(2).lower().startswith('cap') and '.' not in m.group(2) else 'abreviado')
for k,v in sorted(fam.items()):
    print(f'   {sorted(v)}  {k!r}')
