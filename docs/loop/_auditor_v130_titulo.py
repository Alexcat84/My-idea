# AUDITOR v130: la regla mecanica que YO escribi (prefijo estricto sobre la cadena
# entera) puede cazar el patron de truncamiento que 05_SANEO.md documenta?
import json, glob, collections
viv=[json.load(open(p,encoding='utf-8')) for p in sorted(glob.glob('dataset/nodos/*.json'))]
viv=[d for d in viv if not (d.get('deprecated') or d.get('deprecado'))]
c=collections.Counter()
for d in viv:
    f=(d.get('fuente') or '').strip()
    if f: c[f.split('|')[0].strip()]+=1
gr=sorted(c)
def titulo(g): return g.split(' - ')[0].strip()
# los cuatro casos que 05_SANEO.md nombra como truncados
print('--- LOS CASOS QUE 05_SANEO.md NOMBRA COMO TRUNCADOS A ~30 CARACTERES ---')
for sonda in ['Essentials of Supply Chain','Co-Intelligence','Juran','The Hard Thing About Hard']:
    fam=[g for g in gr if sonda in g]
    print(f'  sonda {sonda!r}:')
    for g in fam: print(f'      {c[g]:4d}  len(titulo)={len(titulo(g)):3d}  {g!r}')
    print(f'      prefijo estricto sobre la CADENA ENTERA los une? '
          f'{any(a!=b and b.startswith(a) for a in fam for b in fam)}')
    print(f'      prefijo estricto sobre el TITULO los une?        '
          f'{any(a!=b and titulo(b).startswith(titulo(a)) for a in fam for b in fam)}')
# cuantos grupos NUEVOS daria el prefijo sobre el titulo
padre={g:g for g in gr}
def find(x):
    while padre[x]!=x: x=padre[x]
    return x
def une(a,b):
    ra,rb=find(a),find(b)
    if ra!=rb: padre[rb]=ra
for a in gr:
    for b in gr:
        if a!=b and b.startswith(a): une(a,b)
base=len({find(g) for g in gr})
for a in gr:
    for b in gr:
        if a!=b and titulo(b).startswith(titulo(a)) and len(titulo(a))>=20: une(a,b)
tras=len({find(g) for g in gr})
print()
print(f'GRUPOS con MI regla (prefijo sobre cadena entera):      {base}  (129 grafias)')
print(f'GRUPOS anadiendo prefijo sobre el TITULO (>=20 chars):  {tras}')
print(f'COLAPSOS ADICIONALES QUE LA REGLA DEL TITULO GANA:      {base-tras}')
print(f'LA META de 05_SANEO.md (11 ago 2026): 55. Quedarian {tras-55} colapsos para decision humana.')
