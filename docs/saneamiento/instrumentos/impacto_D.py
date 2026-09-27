# -*- coding: utf-8 -*-
"""Mide, sin escribir, que pasa en el grafo si los nodos que la pasada D decidio mover salen del nucleo a su mundo.
Uso: python impacto_D.py <repo> <final de la pasada D>"""
import collections
import glob
import io
import json
import os
import sys

REPO, FINAL = sys.argv[1], sys.argv[2]
os.chdir(REPO)
sys.path.insert(0, 'scripts')
from run_phase1 import aristas_a_simetrizar, load_entry_seeds  # noqa: E402

nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    nod[n['node_id']] = n
viv = {k for k, n in nod.items() if not n.get('deprecado')}
mover = {x['nodo']: x['mundo'] for x in json.load(io.open(FINAL, encoding='utf-8')) if x['decision'] == 'NO'}
dom = {k: n['dominio'] for k, n in nod.items()}
nuevo = dict(dom)
nuevo.update(mover)
E = [(a, b) for a, b in aristas_a_simetrizar(nod) if a in viv and b in viv]
aprob = {}
for p in glob.glob('packs/*/metadata/bridges_aprobados.json'):
    m = os.path.basename(os.path.dirname(os.path.dirname(p)))
    aprob[m] = json.load(io.open(p, encoding='utf-8'))['aprobados']
# (a) aristas del nucleo que quedan hacia un nodo movido: se vuelven nucleo -> mundo
a = [(x, y) for x, y in E if y in mover and nuevo[x] == 'core']
# (b) puentes aprobados cuya ancla se mueve
b = [(m, p['core'], p['dominio']) for m, ps in aprob.items() for p in ps if p['core'] in mover]
# (c) nodos del nucleo que se quedan sin camino por el nucleo
core = {k for k in viv if nuevo[k] == 'core'}
suc = collections.defaultdict(set)
for x, y in E:
    suc[x].add(y)


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


antes = {k for k in viv if dom[k] == 'core'}
fuera_antes = antes - andar(antes)
fuera_despues = core - andar(core)
print('se mueven', len(mover), collections.Counter(mover.values()))
print('(a) aristas nucleo -> nodo movido:', len(a), 'desde', len({x for x, y in a}), 'nodos del nucleo')
print('(b) puentes aprobados anclados en un nodo movido:', len(b))
for t in b:
    print('    ', t, '(el mismo mundo al que se mueve)' if mover[t[1]] == t[0] else '')
print('(c) nodos del nucleo sin camino por el nucleo: antes', len(fuera_antes), 'despues', len(fuera_despues))
print('    nuevos:', sorted(fuera_despues - fuera_antes))
semillas = [s for s in load_entry_seeds() if s in mover]
print('semillas que se mueven:', semillas)
json.dump({'mover': mover, 'aristas_a_mundo': a, 'puentes_anclados': b, 'sin_camino_nucleo': sorted(fuera_despues - fuera_antes)},
          io.open('docs/saneamiento/resultados/D/impacto.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
