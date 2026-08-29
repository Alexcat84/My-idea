# AUDITOR v132, CIEGA. Escrita ANTES de abrir SALIDA_V132_3A/3B/3C/3D y los
# scripts vuelta132_*. Censo propio, tres reglas propias, el prefijo sobre la
# recortada de 3.d propio, y la sonda de las cuatro truncadas propia.
import json, glob, collections, re, os

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
LOC=re.compile(r',\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|Anexo\s+.*)$', re.IGNORECASE)
def recortar(g):
    x=g
    while True:
        y=LOC.sub('',x).strip().rstrip(' ;,.:')
        if y==x: return x
        x=y

def uf(gr):
    p={g:g for g in gr}
    def find(x):
        while p[x]!=x: x=p[x]
        return x
    def une(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: p[rb]=ra
    return p,find,une

p,find,une=uf(gr)
for a in gr:
    for b in gr:
        if a!=b and b.startswith(a): une(a,b)
n1=len({find(g) for g in gr})
for a in gr:
    for b in gr:
        if a==b: continue
        ta,tb=titulo(a),titulo(b)
        if not (tb.startswith(ta) and len(ta)>=20 and ta!=tb): continue
        ra,rb=resto(a),resto(b)
        if ra and rb and ra!=rb and not (rb.startswith(ra) or ra.startswith(rb)): continue
        une(a,b)
n2=len({find(g) for g in gr})
buck=collections.defaultdict(list)
for g in gr: buck[recortar(g)].append(g)
for k,v in buck.items():
    for x in v[1:]: une(v[0],x)
n3=len({find(g) for g in gr})
print(f'MIS GRUPOS: R1 sola {n1} | +R2 titulo {n2} | +R3 localizador IGUALDAD EXACTA {n3}')
g3=collections.defaultdict(list)
for g in gr: g3[find(g)].append(g)
multi=[v for v in g3.values() if len(v)>1]
print(f'  de 2+ miembros {len(multi)} ({sum(len(v) for v in multi)} grafias), sin agrupar {len(g3)-len(multi)}, faltan para 55: {len(g3)-55}')

# --- 3.d, PREFIJO SOBRE LA RECORTADA, guarda >=20 ---
antes={k:sorted(v) for k,v in g3.items()}
for a in gr:
    for b in gr:
        if a==b: continue
        ra,rb=recortar(a),recortar(b)
        if ra!=rb and len(ra)>=20 and rb.startswith(ra): une(a,b)
n4=len({find(g) for g in gr})
print(f'MI 3.d: prefijo sobre recortada (guarda >=20) -> {n4} grupos (gana {n3-n4})')
g4=collections.defaultdict(list)
for g in gr: g4[find(g)].append(g)
for raiz,v in sorted(g4.items()):
    fus=[k for k,w in antes.items() if set(w)<=set(v)]
    if len(fus)>1:
        print(f'  COLAPSO NUEVO: {len(fus)} grupos base -> 1, {len(v)} grafias')
        for k in fus:
            print(f'     grupo base ({len(antes[k])}): '+' || '.join(repr(x) for x in antes[k]))

# --- LA SONDA DE LAS CUATRO TRUNCADAS ---
print()
print('--- SONDA: titulo truncado (len==31) contra TODO docs/ fuera de docs/loop ---')
trunc=sorted([g for g in gr if len(titulo(g))==31], key=lambda g:-c[g])
ficheros=[]
for r,d,fs in os.walk('docs'):
    if 'loop' in '/'.join(r.split(os.sep)).split('/'): continue
    for f in fs:
        if f.endswith('.md') or f.endswith('.jsonl'): ficheros.append(os.path.join(r,f))
for g in trunc:
    t=titulo(g)
    pref=t[:-1] if t.endswith(' ') else t
    print(f'\n  [{c[g]:4d}n] {g!r}\n         resto={resto(g)!r} prefijo sondeado={pref!r}')
    hits=[]
    for fp in ficheros:
        for i,ln in enumerate(open(fp,encoding='utf-8',errors='replace'),1):
            j=ln.find(pref)
            while j>=0:
                cola=ln[j+len(pref):]
                m=re.match(r'[^|*`\n\]\[]*', cola)
                ext=(pref+m.group(0)).strip().rstrip('.,;:')
                if len(ext)>len(pref.strip()):
                    hits.append(('/'.join(fp.split(os.sep)),i,ext))
                j=ln.find(pref,j+1)
    if not hits: print('         CERO ficheros -> FORASTERA PURA')
    for h in hits: print(f'         {h[0]}:{h[1]}  ->  {h[2]!r}')
