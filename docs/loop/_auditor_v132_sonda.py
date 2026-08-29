# AUDITOR v132, SONDA AFINADA. La continuacion tiene que EXTENDER LA PALABRA
# cortada: el caracter inmediatamente siguiente al prefijo de 31 es una LETRA.
import json, glob, collections, re, os
viv=[json.load(open(p,encoding='utf-8')) for p in sorted(glob.glob('dataset/nodos/*.json'))]
viv=[d for d in viv if not (d.get('deprecated') or d.get('deprecado'))]
c=collections.Counter()
for d in viv:
    f=(d.get('fuente') or '').strip()
    if f: c[f.split('|')[0].strip()]+=1
def titulo(g): return g.split(' - ')[0].strip()
trunc=sorted([g for g in c if len(titulo(g))==31], key=lambda g:-c[g])
ficheros=[]
for r,d,fs in os.walk('docs'):
    if 'loop' in '/'.join(r.split(os.sep)).split('/'): continue
    for f in fs:
        if f.endswith('.md') or f.endswith('.jsonl'): ficheros.append(os.path.join(r,f))
print(f'ficheros sondeados fuera de docs/loop: {len(ficheros)}')
CORTE=re.compile(r'^[A-Za-z][A-Za-z0-9 ,:\'()-]*')
for g in trunc:
    t=titulo(g)
    print()
    print(f'  [{c[g]:4d}n] {g!r}')
    hits=collections.Counter()
    for fp in ficheros:
        ruta='/'.join(fp.split(os.sep))
        for i,ln in enumerate(open(fp,encoding='utf-8',errors='replace'),1):
            j=ln.find(t)
            while j>=0:
                cola=ln[j+len(t):]
                m=CORTE.match(cola)
                if m:
                    ext=(t+m.group(0)).strip().rstrip('.,;:')
                    hits[(ruta,i,ext)]+=1
                j=ln.find(t,j+1)
    if not hits:
        print('         CERO continuaciones -> FORASTERA PURA')
    for (ruta,i,ext),n in sorted(hits.items()):
        print(f'         {ruta}:{i}  (x{n})  ->  {ext!r}')
    print(f'         FICHEROS DISTINTOS: {len(set(h[0] for h in hits))} | PARES fichero:linea: {len(hits)}')
