# -*- coding: utf-8 -*-
"""Pasada E del saneamiento (TANDA 2, punto 7): las aristas rancias que eran la UNICA entrada a un nodo. Quitarlas deja
nodos sin camino desde las semillas; antes de quitarlas, cada punta recibe una entrada correcta. Para cada punta se
proponen hasta 8 predecesores candidatos (los vecinos semanticos mas cercanos, por el indice de la web, que hoy SI se
alcanzan desde las semillas y son del mismo mundo o del nucleo). Lector y verificador ciego eligen; arbitro si no
coinciden. Solo lectura del repo.

Uso: python preparar_E.py <repo> <W> <tanda de aristas>"""
import glob
import io
import json
import math
import os
import sys

REPO, W, TANDA = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, os.path.join(REPO, 'scripts'))
from run_phase1 import load_entry_seeds  # noqa: E402

nodos = {}
for p in glob.glob(os.path.join(REPO, 'dataset/nodos/*.json')):
    n = json.load(io.open(p, encoding='utf-8'))
    nodos[n['node_id']] = n
vivos = {k: n for k, n in nodos.items() if not n.get('deprecado')}


def alcanzados():
    seen = {s for s in load_entry_seeds() if s in vivos}
    st = list(seen)
    while st:
        c = st.pop()
        for x in vivos[c].get('nodos_siguientes') or []:
            if x in vivos and x not in seen:
                seen.add(x)
                st.append(x)
    return seen


hoy = alcanzados()
tanda = json.load(io.open(TANDA, encoding='utf-8'))
puntas = sorted({o['hacia'] for o in tanda if o['operacion'] == 'QUITAR' and o['hacia'] not in hoy and o['desde'] in hoy})
idx = json.load(io.open(os.path.join(REPO, 'web/lib/assets/semantic_index.json'), encoding='utf-8'))
vec = {i: v for i, v in zip(idx['ids'], idx['embeddings'])}


def cos(a, b):
    return sum(x * y for x, y in zip(a, b)) / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def ficha(i):
    n = vivos[i]
    return 'titulo: %s | fase: %s | mundo: %s\n    resumen: %s' % (n['titulo_concepto'], n['fase_proyecto'], n['dominio'], n['resumen_teorico'])


txt = ['# Pasada E: %d nodos que necesitan una entrada\n' % len(puntas)]
claves = {}
for i, t in enumerate(puntas, 1):
    cand = sorted(((cos(vec[t], vec[c]), c) for c in hoy if c != t and c in vec and vivos[c]['dominio'] in (vivos[t]['dominio'], 'core')
                   and t not in (vivos[c].get('nodos_siguientes') or [])), reverse=True)[:8]
    cid = 'E-%02d' % i
    claves[cid] = {'punta': t, 'candidatos': [c for s, c in cand]}
    txt.append('### %s\n- NODO QUE NECESITA UNA ENTRADA\n    %s\n- CANDIDATOS A PREDECESOR' % (cid, ficha(t)))
    for j, (s, c) in enumerate(cand, 1):
        txt.append('  %d. [%s]\n    %s' % (j, c, ficha(c)))
    txt.append('')
os.makedirs(os.path.join(W, 'E'), exist_ok=True)
io.open(os.path.join(W, 'E', 'lote_E.md'), 'w', encoding='utf-8').write('\n'.join(txt))
json.dump(claves, io.open(os.path.join(W, 'E', 'claves.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('puntas', len(puntas))
