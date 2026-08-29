# AUDITOR v131, CIEGA. Escrita ANTES de abrir SALIDA_V131_3A/3B/3C/3D ni los
# scripts vuelta131_*. Reproduce el censo, las tres reglas y el residuo con
# codigo propio, y adjudica la BOLSA 2 (discutible 1 del reporte).
import json, glob, collections, re

viv=[json.load(open(p,encoding='utf-8')) for p in sorted(glob.glob('dataset/nodos/*.json'))]
viv=[d for d in viv if not (d.get('deprecated') or d.get('deprecado'))]
c=collections.Counter()
for d in viv:
    f=(d.get('fuente') or '').strip()
    if f: c[f.split('|')[0].strip()]+=1
gr=sorted(c)
print(f'CENSO: {len(viv)} nodos vivos, {sum(c.values())} con fuente, {len(gr)} grafias distintas')

def titulo(g): return g.split(' - ')[0].strip()
def resto(g):
    p=g.split(' - ',1)
    return p[1].strip() if len(p)>1 else ''

LOC=re.compile(r',\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|Anexo\s+.*)$', re.IGNORECASE)
def recortar(g):
    x=g
    while True:
        y=LOC.sub('',x).strip()
        y=y.rstrip(' ;,.:')
        if y==x: return x
        x=y

padre={g:g for g in gr}
motivo={}
def find(x):
    while padre[x]!=x: x=padre[x]
    return x
def une(a,b,m):
    ra,rb=find(a),find(b)
    if ra!=rb:
        padre[rb]=ra
        motivo.setdefault(a,m); motivo.setdefault(b,m)

# R1: prefijo estricto sobre la CADENA ENTERA
for a in gr:
    for b in gr:
        if a!=b and b.startswith(a): une(a,b,'cadena entera')
n1=len({find(g) for g in gr})
# R2: prefijo estricto sobre el TITULO, titulo corto >=20, guarda de RESTO
for a in gr:
    for b in gr:
        if a==b: continue
        ta,tb=titulo(a),titulo(b)
        if not (tb.startswith(ta) and len(ta)>=20 and ta!=tb): continue
        ra,rb=resto(a),resto(b)
        if ra and rb and ra!=rb and not (rb.startswith(ra) or ra.startswith(rb)): continue
        une(a,b,'titulo')
n2=len({find(g) for g in gr})
# R3: localizador recortado
buck=collections.defaultdict(list)
for g in gr: buck[recortar(g)].append(g)
for k,v in buck.items():
    for x in v[1:]: une(v[0],x,'localizador')
for a in gr:
    for b in gr:
        if a!=b and recortar(b).startswith(recortar(a)) and len(recortar(a))>=20 and recortar(a)!=recortar(b):
            pass  # no se extiende: R3 solo normaliza, no reprefija
n3=len({find(g) for g in gr})
print(f'GRUPOS: R1 sola {n1} | +R2 titulo {n2} (gana {n1-n2}) | +R3 localizador {n3} (gana {n2-n3})')

grupos=collections.defaultdict(list)
for g in gr: grupos[find(g)].append(g)
multi=[v for v in grupos.values() if len(v)>1]
solos=[v[0] for v in grupos.values() if len(v)==1]
print(f'TOTAL GRUPOS {len(grupos)} | de 2+ miembros {len(multi)} ({sum(len(v) for v in multi)} grafias) | SIN AGRUPAR {len(solos)}')
print(f'COLAPSOS: {len(gr)-len(grupos)} logrados; para la meta de 55 faltan {len(grupos)-55}')

# LA CANONICA por la regla del localizador: la forma mas larga que sigue siendo libro
print()
print('--- LOS GRUPOS DE 2+ MIEMBROS, CON MI CANONICA ---')
for v in sorted(multi, key=lambda v:-sum(c[x] for x in v)):
    libros=[x for x in v if recortar(x)==x]
    canon=max(libros or v, key=len)
    print(f'  [{sum(c[x] for x in v):4d}n] canonica={canon!r}')
    for x in sorted(v): print(f'         {c[x]:4d}  {x!r}')

# EL RESIDUO Y LAS DOS BOLSAS
print()
print('--- DETECTOR DE TRUNCAMIENTO SOBRE EL RESIDUO ---')
trunc=[g for g in solos if len(titulo(g))==31]
print(f'grafias sin agrupar con len(titulo)==31: {len(trunc)}')
for g in sorted(trunc, key=lambda g:-c[g]):
    contra=[h for h in gr if h!=g and titulo(h).startswith(titulo(g)) and len(titulo(h))>len(titulo(g))]
    print(f'  {c[g]:4d}  resto={resto(g)!r:35s} contraparte_en_censo={contra}  {g!r}')
print()
print('--- toda grafia del censo con len(titulo)==31 (agrupada o no) ---')
for g in sorted([x for x in gr if len(titulo(x))==31], key=lambda g:-c[g]):
    print(f'  {c[g]:4d}  solo={g in solos}  resto={resto(g)!r:35s}  {g!r}')
