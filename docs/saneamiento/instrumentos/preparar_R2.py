# -*- coding: utf-8 -*-
"""Tras mover los nodos del nucleo a su mundo (pasadas D y MV): los nodos que se quedaron sin ninguna entrada desde las
semillas reciben un predecesor DE SU MISMO MUNDO por lectura (asi no se abre un puente nuevo). Se leen las raices; 8
candidatos alcanzables del mismo mundo, sin los que harian un par de ida y vuelta. Uso: python preparar_R2.py <repo> <W>"""
import glob
import io
import json
import math
import os
import sys

REPO, W = sys.argv[1], sys.argv[2]
os.chdir(REPO)
sys.path.insert(0, 'scripts')
from run_phase1 import load_entry_seeds  # noqa: E402

nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    if not n.get('deprecado'):
        nod[n['node_id']] = n
seen = {s for s in load_entry_seeds() if s in nod}
st = list(seen)
while st:
    c = st.pop()
    for x in nod[c].get('nodos_siguientes') or []:
        if x in nod and x not in seen:
            seen.add(x)
            st.append(x)
fuera = set(nod) - seen
raices = sorted(k for k in fuera if not any(p in fuera for p in nod[k].get('nodos_previos') or []))
idx = json.load(io.open('web/lib/assets/semantic_index.json', encoding='utf-8'))
vec = dict(zip(idx['ids'], idx['embeddings']))


def cos(a, b):
    x, y = vec[a], vec[b]
    return sum(p * q for p, q in zip(x, y)) / (math.sqrt(sum(p * p for p in x)) * math.sqrt(sum(q * q for q in y)))


def ficha(i):
    n = nod[i]
    return 'titulo: %s | mundo: %s\n    resumen: %s' % (n['titulo_concepto'], n['dominio'], ' '.join(n['resumen_teorico'].split()))


txt, claves = ['# Pasada R2: nodos sin entrada tras mover nodos del nucleo a su mundo\n'], {}
for i, t in enumerate(raices, 1):
    m = nod[t]['dominio']
    sig = set(nod[t].get('nodos_siguientes') or [])
    cand = sorted(((cos(t, c), c) for c in seen if c in vec and nod[c]['dominio'] == m and c not in sig), reverse=True)[:8]
    cid = 'R2-%02d' % i
    claves[cid] = {'punta': t, 'candidatos': [c for s, c in cand]}
    txt.append('### %s\n- NODO SIN ENTRADA [%s]\n    %s\n- CANDIDATOS A PREDECESOR (su mismo mundo)' % (cid, t, ficha(t)))
    txt += ['  %d. [%s]\n    %s' % (j, c, ficha(c)) for j, (s, c) in enumerate(cand, 1)]
    txt.append('')
os.makedirs(os.path.join(W, 'R2'), exist_ok=True)
io.open(os.path.join(W, 'R2', 'lote.md'), 'w', encoding='utf-8').write('\n'.join(txt))
json.dump(claves, io.open(os.path.join(W, 'R2', 'claves.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('sin entrada', len(fuera), '| raices', len(raices), raices)
