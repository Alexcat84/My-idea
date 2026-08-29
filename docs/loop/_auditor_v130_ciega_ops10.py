# AUDITOR VUELTA 130: verificacion 1 de OP-S-10 remedida hoy, con resolutor de alias propio.
import json, glob
alias={}; vivos={}; depre=set()
for p in sorted(glob.glob('dataset/nodos/*.json')):
    d=json.load(open(p,encoding='utf-8'))
    nid=d.get('node_id') or d.get('id')
    dep=bool(d.get('deprecated') or d.get('deprecado'))
    if dep: depre.add(nid)
    else: vivos[nid]=d
    for a in (d.get('ids_alias') or []): alias[a]=nid
    alias.setdefault(nid,nid)
print('resolutor de alias, entradas:', len(alias), '| vivos:', len(vivos), '| deprecados:', len(depre))
op=[json.loads(l) for l in open('docs/plan/OPERACIONES.jsonl',encoding='utf-8') if l.strip()]
op=[o for o in op if o.get('id_op')=='OP-S-10'][0]
ids=op['nodos']; print('ids en el campo `nodos`:', len(ids))
res, movidos, ausentes = [], [], []
for i in ids:
    r=alias.get(i)
    if r is None: ausentes.append(i); continue
    if r!=i: movidos.append((i,r))
    res.append(r)
uni=sorted(set(res))
print('resuelven a VIVOS DISTINTOS:', len(uni), '| deprecados tras resolver:', sum(1 for x in uni if x in depre), '| ausentes:', len(ausentes))
print('el resolutor mueve', len(movidos))
for a,b in movidos: print('   ', a, '->', b)
PAIS=('estados unidos','ee.uu','eeuu','e.e.u.u','estadounidense','united states')
sin=[]
for n in uni:
    d=vivos.get(n)
    if d is None: sin.append((n,'NO VIVO')); continue
    cond=' '.join(d.get('condiciones_activacion') or []).lower()
    if not any(k in cond for k in PAIS): sin.append((n,'sin pais'))
print('CUBIERTOS:', len(uni)-len(sin), 'de', len(uni))
for n,m in sin: print('   SIN CUBRIR:', n, m)
