# AUDITOR v133, SONDA PROPIA sobre los 49 colapsos que quedan: que formas de
# localizador NO reconoce la cola de hoy. Solo mide; no adjudica ninguna regla.
import json, glob, collections, re
viv=[json.load(open(p,encoding='utf-8')) for p in sorted(glob.glob('dataset/nodos/*.json'))]
viv=[d for d in viv if not (d.get('deprecated') or d.get('deprecado'))]
c=collections.Counter()
for d in viv:
    f=(d.get('fuente') or '').strip()
    if f: c[f.split('|')[0].strip()]+=1
gr=sorted(c)
LOC=re.compile(r',\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|Anexos?\s+.*|Ap[eé]ndices?\s+.*)$', re.IGNORECASE)
def rec(g):
    x=g
    while True:
        y=LOC.sub('',x).strip().rstrip(' ;,.:')
        if y==x: return x
        x=y
sin=[g for g in gr if rec(g)==g]
print(f'grafias que la cola de HOY no recorta: {len(sin)} de {len(gr)}')
pat=collections.Counter()
for g in sin:
    m=re.search(r',\s*([A-Za-zÁÉÍÓÚáéíóúñÑ.]+)\s', g[g.rfind(','):] if ',' in g else '')
    if m: pat[m.group(1)]+=1
print('primera palabra tras la ULTIMA coma, en las no recortadas:')
for k,v in pat.most_common(14): print(f'   {k!r:18s} {v}')
print()
CAP=re.compile(r',\s*Caps?\.\s', re.IGNORECASE)
con_cap=[g for g in sin if CAP.search(g)]
print(f'NO RECORTADAS que llevan ", Cap." o ", Caps.": {len(con_cap)} grafias, {sum(c[g] for g in con_cap)} nodos')
fam=collections.Counter(CAP.split(g)[0] for g in con_cap)
print('sus familias (cadena antes del ", Cap."):')
for k,v in fam.most_common(): print(f'   {v:3d} grafias  {k!r}')
