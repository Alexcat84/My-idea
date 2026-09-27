# -*- coding: utf-8 -*-
"""Pasada MV del saneamiento (decision del fundador: los nodos que la pasada D decidio mover salen del nucleo a su mundo,
como colaboracion_transporte_ctm). Tres lecturas en un lote, sobre el grafo como queda DESPUES de mover:
  A. cada arista del nucleo a un mundo sin aprobar (las que llegan a un nodo movido, y las que dejaron los nodos que la
     pasada Q devolvio al nucleo): PUENTE o RETIRAR, con su fuerza (1 a 3) para la ley del ancla;
  B. cada puente aprobado cuya ancla se mueve a OTRO mundo: un ancla nueva del nucleo, entre 8 candidatos;
  C. cada nodo del nucleo que se queda sin camino por el nucleo: un predecesor del nucleo, entre 8 candidatos.
Solo lectura del repo. Uso: python preparar_MV.py <repo> <W> <final de la pasada D>"""
import collections
import glob
import io
import json
import math
import os
import sys

REPO, W, FINAL = sys.argv[1], sys.argv[2], sys.argv[3]
os.chdir(REPO)
sys.path.insert(0, 'scripts')
from run_phase1 import aristas_a_simetrizar, load_entry_seeds  # noqa: E402

nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    nod[n['node_id']] = n
viv = {k for k, n in nod.items() if not n.get('deprecado')}
mover = {x['nodo']: x['mundo'] for x in json.load(io.open(FINAL, encoding='utf-8')) if x['decision'] == 'NO'}
dom = {k: nod[k]['dominio'] for k in nod}
dom.update(mover)
E = [(a, b) for a, b in aristas_a_simetrizar(nod) if a in viv and b in viv]
aprob = {}
for p in glob.glob('packs/*/metadata/bridges_aprobados.json'):
    aprob[os.path.basename(os.path.dirname(os.path.dirname(p)))] = json.load(io.open(p, encoding='utf-8'))['aprobados']
aprobados = {(p['core'], p['dominio']) for ps in aprob.values() for p in ps}
core = {k for k in viv if dom[k] == 'core'}
suc = collections.defaultdict(set)
for a, b in E:
    suc[a].add(b)


def andar(nucleo):
    seen = {s for s in load_entry_seeds() if s in nucleo}
    st = list(seen)
    while st:
        c = st.pop()
        for y in suc[c]:
            if y in nucleo and y not in seen:
                seen.add(y)
                st.append(y)
    return seen


alc = andar(core)
idx = json.load(io.open('web/lib/assets/semantic_index.json', encoding='utf-8'))
vec = dict(zip(idx['ids'], idx['embeddings']))


def cos(a, b):
    x, y = vec[a], vec[b]
    return sum(p * q for p, q in zip(x, y)) / (math.sqrt(sum(p * p for p in x)) * math.sqrt(sum(q * q for q in y)))


def ficha(i):
    n = nod[i]
    return 'titulo: %s | mundo: %s\n    resumen: %s' % (n['titulo_concepto'], dom[i], ' '.join(n['resumen_teorico'].split()))


MUNDO = {'entrega': 'logistica y entrega', 'compras': 'compras y proveedores', 'quality': 'gestion de la calidad',
         'risk_management': 'gestion de riesgos', 'seguridad_digital': 'seguridad digital', 'health_safety': 'seguridad y salud',
         'environmental': 'gestion ambiental', 'exportacion': 'exportacion', 'franquicias': 'franquicias'}
txt, claves = ['# Pasada MV: nodos que salen del nucleo a su mundo\n'], {}
A = sorted({(a, b) for a, b in E if dom[a] == 'core' and dom[b] != 'core' and (a, b) not in aprobados})
txt.append('## A: aristas del nucleo a un mundo. PUENTE o RETIRAR, con fuerza 1 a 3 (0 si RETIRAR)\n')
for i, (a, b) in enumerate(A, 1):
    cid = 'MV-A%02d' % i
    claves[cid] = {'core': a, 'mundo': b, 'dominio': dom[b]}
    txt.append('### %s\n- NODO DEL NUCLEO [%s]\n    %s\n- NODO DEL MUNDO "%s" [%s]\n    %s\n' % (cid, a, ficha(a), MUNDO[dom[b]], b, ficha(b)))
B = [(m, p['core'], p['dominio']) for m, ps in aprob.items() for p in ps if p['core'] in mover and mover[p['core']] != m]
txt.append('## B: puentes aprobados cuya ancla sale del nucleo. Elige un ANCLA DEL NUCLEO nueva\n')
cuenta = collections.Counter((m, p['core']) for m, ps in aprob.items() for p in ps)
for i, (m, ancla, w) in enumerate(B, 1):
    cand = sorted(((cos(w, c), c) for c in alc if c in vec and cuenta[(m, c)] < 2 and w not in suc[c]), reverse=True)[:8]
    cid = 'MV-B%02d' % i
    claves[cid] = {'mundo': m, 'ancla_vieja': ancla, 'punta': w, 'candidatos': [c for s, c in cand]}
    txt.append('### %s\n- NODO DEL MUNDO "%s" QUE NECESITA UNA PUERTA DESDE EL NUCLEO [%s]\n    %s\n- CANDIDATOS A ANCLA (nucleo)' % (cid, MUNDO[m], w, ficha(w)))
    txt += ['  %d. [%s]\n    %s' % (j, c, ficha(c)) for j, (s, c) in enumerate(cand, 1)]
    txt.append('')
C = sorted(core - alc)
txt.append('## C: nodos del nucleo que se quedan sin camino por el nucleo. Elige un PREDECESOR DEL NUCLEO\n')
for i, t in enumerate(C, 1):
    cand = sorted(((cos(t, c), c) for c in alc if c in vec and t not in suc[c] and c not in suc[t]), reverse=True)[:8]
    cid = 'MV-C%02d' % i
    claves[cid] = {'punta': t, 'candidatos': [c for s, c in cand]}
    txt.append('### %s\n- NODO DEL NUCLEO SIN CAMINO [%s]\n    %s\n- CANDIDATOS A PREDECESOR (nucleo)' % (cid, t, ficha(t)))
    txt += ['  %d. [%s]\n    %s' % (j, c, ficha(c)) for j, (s, c) in enumerate(cand, 1)]
    txt.append('')
os.makedirs(os.path.join(W, 'MV'), exist_ok=True)
io.open(os.path.join(W, 'MV', 'lote_MV.md'), 'w', encoding='utf-8').write('\n'.join(txt))
json.dump(claves, io.open(os.path.join(W, 'MV', 'claves.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('A', len(A), '| B', len(B), '| C', len(C))
