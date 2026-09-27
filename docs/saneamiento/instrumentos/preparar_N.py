# -*- coding: utf-8 -*-
"""Nivel 1, criterio 6 (decision del fundador del 27 sep 2026): los nodos del nucleo que no se alcanzan andando solo por
el nucleo desde las semillas reciben un predecesor del nucleo por lectura. Se leen las RAICES: los inalcanzables que
no cuelgan de otro inalcanzable del nucleo (darle entrada a la raiz alcanza lo que cuelga de ella). Para cada raiz, 8
candidatos: los vecinos semanticos del nucleo que si se alcanzan por el nucleo. Solo lectura del repo.
Uso: python preparar_N.py <repo> <W>"""
import glob
import io
import json
import math
import os
import sys

REPO, W = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(REPO, 'scripts'))
from run_phase1 import load_entry_seeds  # noqa: E402

os.chdir(REPO)
nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    if not n.get('deprecado'):
        nod[n['node_id']] = n
core = {k: n for k, n in nod.items() if n['dominio'] == 'core'}


def alcance(extra=()):
    seen = {s for s in load_entry_seeds() if s in core}
    st = list(seen)
    ady = {k: set(n.get('nodos_siguientes') or []) for k, n in core.items()}
    for a, b in extra:
        ady[a].add(b)
    while st:
        c = st.pop()
        for x in ady[c]:
            if x in core and x not in seen:
                seen.add(x)
                st.append(x)
    return seen


hoy = alcance()
fuera = sorted(set(core) - hoy)
raices = [k for k in fuera if not any(p in core and p in fuera and p != k for p in core[k].get('nodos_previos') or [])]
# una raiz dentro de un ciclo de inalcanzables no tiene previo "fuera" sin ciclo: se toma el primero de cada ciclo
cubiertos = set()
for r in raices:
    cubiertos |= alcance([(next(iter(hoy)), r)]) - hoy
resto = [k for k in fuera if k not in cubiertos]
while resto:
    raices.append(resto[0])
    cubiertos |= alcance([(next(iter(hoy)), x) for x in raices]) - hoy
    resto = [k for k in fuera if k not in cubiertos]
idx = json.load(io.open('web/lib/assets/semantic_index.json', encoding='utf-8'))
vec = dict(zip(idx['ids'], idx['embeddings']))


def cos(a, b):
    x, y = vec[a], vec[b]
    return sum(p * q for p, q in zip(x, y)) / (math.sqrt(sum(p * p for p in x)) * math.sqrt(sum(q * q for q in y)))


def ficha(i):
    n = nod[i]
    return 'titulo: %s | fase: %s\n    resumen: %s' % (n['titulo_concepto'], n['fase_proyecto'], n['resumen_teorico'])


txt = ['# Pasada N: %d nodos del nucleo sin camino por el nucleo\n' % len(raices)]
claves = {}
for i, t in enumerate(sorted(raices), 1):
    cand = sorted(((cos(t, c), c) for c in hoy if c in vec and t not in (core[c].get('nodos_siguientes') or [])), reverse=True)[:8]
    cid = 'N-%02d' % i
    cuelgan = sorted(alcance([(next(iter(hoy)), t)]) - hoy - {t})
    claves[cid] = {'punta': t, 'candidatos': [c for s, c in cand], 'cuelgan': cuelgan}
    txt.append('### %s\n- NODO DEL NUCLEO QUE NECESITA UNA ENTRADA DESDE EL NUCLEO\n    %s\n- CANDIDATOS A PREDECESOR' % (cid, ficha(t)))
    for j, (s, c) in enumerate(cand, 1):
        txt.append('  %d. [%s]\n    %s' % (j, c, ficha(c)))
    txt.append('')
os.makedirs(os.path.join(W, 'N'), exist_ok=True)
io.open(os.path.join(W, 'N', 'lote_N.md'), 'w', encoding='utf-8').write('\n'.join(txt))
json.dump(claves, io.open(os.path.join(W, 'N', 'claves.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('inalcanzables', len(fuera), '| raices', len(raices), '| cubiertos por las raices', len(cubiertos))
