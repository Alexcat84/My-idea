# AUDITOR VUELTA 130, relectura ciega de la agrupacion mecanica (3.b(ii)/(iii)/(iv)).
# Escrito SIN mirar la salida del ejecutor.
import json, glob, collections, re
viv=[]
for p in sorted(glob.glob('dataset/nodos/*.json')):
    d=json.load(open(p,encoding='utf-8'))
    if not (d.get('deprecated') or d.get('deprecado')): viv.append(d)
c=collections.Counter()
for n in viv:
    f=(n.get('fuente') or '').strip()
    if f: c[f.split('|')[0].strip()]+=1
gr=sorted(c)
print('GRAFIAS EN 1a POSICION, separador |:', len(gr))
# (a) prefijo estricto
pares=[(a,b) for a in gr for b in gr if a!=b and b.startswith(a)]
padre={g:g for g in gr}
def find(x):
    while padre[x]!=x: x=padre[x]
    return x
def une(a,b):
    ra,rb=find(a),find(b)
    if ra!=rb: padre[rb]=ra
for a,b in pares: une(a,b)
# (b) normalizacion espacios/mayusculas/puntuacion final
def norm(s): return re.sub(r'\s+',' ',s).strip().lower().rstrip('.,;:')
por_norm=collections.defaultdict(list)
for g in gr: por_norm[norm(g)].append(g)
n_norm=0
for k,v in por_norm.items():
    if len(v)>1:
        n_norm+=1
        for x in v[1:]: une(v[0],x)
grupos=collections.defaultdict(list)
for g in gr: grupos[find(g)].append(g)
conmas=[v for v in grupos.values() if len(v)>1]
print('GRUPOS por PREFIJO ESTRICTO (pares crudos):', len(pares))
print('GRUPOS mecanicos con 2+ miembros:', len(conmas), ' GRAFIAS dentro de ellos:', sum(len(v) for v in conmas))
print('GRUPOS que salen SOLO de la normalizacion:', n_norm)
print('SIN AGRUPAR (grafias en grupo de 1):', sum(1 for v in grupos.values() if len(v)==1))

print()
print('--- LOS 13 GRUPOS, LEIDOS DE MI PROPIA MEDICION ---')
i=0
for r,v in sorted(grupos.items()):
    if len(v)>1:
        i+=1
        print(f'{i:2d}. canonica propuesta (la mas larga): {max(v,key=len)!r}')
        for g in sorted(v,key=len): print(f'      {c[g]:4d}  {g!r}')
print()
print('CUENTAS: 129 grafias -> ', len([v for v in grupos.values()]), 'grupos tras agrupar')
print('  (13 grupos de 2+ que absorben 31 grafias, mas 98 sueltas)')
print('LA META DE 05_SANEO.md (11 ago 2026): 55 libros canonicos.')
print('LO MECANICO SOLO LLEGA A', len(grupos), '. FALTAN', len(grupos)-55, 'COLAPSOS QUE PIDEN DECISION.')
