# AUDITOR v133, CIEGA. Escrita ANTES de abrir los scripts vuelta133_* y las
# SALIDA_V133_4A/4B/4D. Extiende mi propia ciega de la 132 (misma base) con:
# la cola de localizador CON Apendice (4.a), el prefijo sobre la recortada CON
# guarda de RESTO (4.b), el censo de canonicas SINTETICAS (4.c) y el conteo de
# nodos por familia. Los cinco peldanos se imprimen POR SEPARADO.
import json, glob, collections, re

viv=[json.load(open(p,encoding='utf-8')) for p in sorted(glob.glob('dataset/nodos/*.json'))]
viv=[d for d in viv if not (d.get('deprecated') or d.get('deprecado'))]
c=collections.Counter()
for d in viv:
    f=(d.get('fuente') or '').strip()
    if f: c[f.split('|')[0].strip()]+=1
gr=sorted(c)
print(f'CENSO: {len(viv)} vivos, {sum(c.values())} con fuente, {len(gr)} grafias')

def titulo(g): return g.split(' - ')[0].strip()
def resto(g):
    p=g.split(' - ',1); return p[1].strip() if len(p)>1 else ''

LOC_VIEJA=re.compile(r',\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|Anexo\s+.*)$', re.IGNORECASE)
LOC_NUEVA=re.compile(r',\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|Anexos?\s+.*|Ap[eé]ndices?\s+.*)$', re.IGNORECASE)
def hacer_recortar(rx):
    def recortar(g):
        x=g
        while True:
            y=rx.sub('',x).strip().rstrip(' ;,.:')
            if y==x: return x
            x=y
    return recortar
rec_vieja=hacer_recortar(LOC_VIEJA)
rec_nueva=hacer_recortar(LOC_NUEVA)

def nuevo_uf():
    p={g:g for g in gr}
    def find(x):
        while p[x]!=x: x=p[x]
        return x
    def une(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: p[rb]=ra
    return find,une

def r1(une):
    for a in gr:
        for b in gr:
            if a!=b and b.startswith(a): une(a,b)
def r2(une):
    for a in gr:
        for b in gr:
            if a==b: continue
            ta,tb=titulo(a),titulo(b)
            if not (tb.startswith(ta) and len(ta)>=20 and ta!=tb): continue
            ra,rb=resto(a),resto(b)
            if ra and rb and ra!=rb and not (rb.startswith(ra) or ra.startswith(rb)): continue
            une(a,b)
def r3(une,rec):
    b=collections.defaultdict(list)
    for g in gr: b[rec(g)].append(g)
    for k,v in b.items():
        for x in v[1:]: une(v[0],x)
def r4(une,rec,con_resto=True):
    pares=[]
    for a in gr:
        for b in gr:
            if a==b: continue
            ra,rb=rec(a),rec(b)
            if ra==rb or len(ra)<20 or not rb.startswith(ra): continue
            if con_resto:
                xa,xb=resto(ra),resto(rb)
                if xa and xb and xa!=xb and not (xb.startswith(xa) or xa.startswith(xb)): continue
            pares.append((a,b)); une(a,b)
    return pares

def corre(reglas):
    find,une=nuevo_uf()
    extra=None
    for f in reglas: extra=f(une) or extra
    g=collections.defaultdict(list)
    for x in gr: g[find(x)].append(x)
    return g,extra

n=[]
for etiqueta,reglas in [
    ('(1) cadena entera sola            ', [r1]),
    ('(2) + titulo (>=20, guarda RESTO) ', [r1,r2]),
    ('(3) + localizador, cola VIEJA     ', [r1,r2,lambda u:r3(u,rec_vieja)]),
    ('(4) + Apendice en la cola (4.a)   ', [r1,r2,lambda u:r3(u,rec_nueva)]),
    ('(5) + prefijo sobre recortada(4.b)', [r1,r2,lambda u:r3(u,rec_nueva),lambda u:r4(u,rec_nueva)]),
]:
    g,extra=corre(reglas)
    multi=[v for v in g.values() if len(v)>1]
    n.append(len(g))
    print(f'{etiqueta} -> {len(g):3d} grupos | de 2+ {len(multi):2d} ({sum(len(v) for v in multi):3d} grafias) | solos {len(g)-len(multi):3d} | faltan para 55: {len(g)-55}')

# guarda de RESTO: cuesta cero hoy?
g_sin,_=corre([r1,r2,lambda u:r3(u,rec_nueva),lambda u:r4(u,rec_nueva,con_resto=False)])
print(f'MISMO peldano (5) SIN la guarda de RESTO -> {len(g_sin)} grupos (con ella {n[4]})')

# canonicas y SINTETICAS sobre el peldano (5)
g5,pares=corre([r1,r2,lambda u:r3(u,rec_nueva),lambda u:r4(u,rec_nueva)])
sint=0
for raiz,v in sorted(g5.items()):
    libros=[x for x in v if rec_nueva(x)==x]
    if libros: can=max(libros,key=len); marca=''
    else: can=rec_nueva(max(v,key=len)); marca='SINTETICA'; sint+=1
    if len(v)>1 and 'Lindstrom' in can:
        print(f'FAMILIA Lindstrom: {len(v)} grafias, {sum(c[x] for x in v)} nodos, canonica {can!r} {marca}')
print(f'CANONICAS SINTETICAS en el peldano (5): {sint}')
print(f'PARES que une el prefijo sobre recortada: {len(pares)}')
