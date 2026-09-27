# -*- coding: utf-8 -*-
"""Pasada C del saneamiento (decision del fundador del 27 sep 2026, punto 1): colaboracion_transporte_ctm pasa del
nucleo a entrega. Tres lecturas en un lote:
  A. el puente a calidad que anclaba (-> equipo_conjunto_de_mejora_con_proveedores) necesita un ancla del nucleo:
     8 candidatos, los vecinos semanticos alcanzables del nucleo con menos de 2 puentes a quality (ley del ancla);
  B. collaboration_enablers, del nucleo, solo entraba por el: necesita un predecesor del nucleo (8 candidatos);
  C. las 4 aristas del nucleo que llegan a el pasan a ir del nucleo a entrega: cada una PUENTE o RETIRAR.
Solo lectura del repo. Uso: python preparar_C.py <repo> <W>"""
import collections
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
    nod[n['node_id']] = n
viv = {k: n for k, n in nod.items() if not n.get('deprecado')}
M = 'colaboracion_transporte_ctm'
seen = {s for s in load_entry_seeds() if s in viv}
st = list(seen)
while st:
    c = st.pop()
    for x in viv[c].get('nodos_siguientes') or []:
        if x in viv and x not in seen and x != M:
            seen.add(x)
            st.append(x)
idx = json.load(io.open('web/lib/assets/semantic_index.json', encoding='utf-8'))
vec = dict(zip(idx['ids'], idx['embeddings']))


def cos(a, b):
    x, y = vec[a], vec[b]
    return sum(p * q for p, q in zip(x, y)) / (math.sqrt(sum(p * p for p in x)) * math.sqrt(sum(q * q for q in y)))


def ficha(i):
    n = viv[i]
    return 'titulo: %s | fase: %s | mundo: %s\n    resumen: %s' % (n['titulo_concepto'], n['fase_proyecto'], n['dominio'], n['resumen_teorico'])


q = json.load(io.open('packs/quality/metadata/bridges_aprobados.json', encoding='utf-8'))['aprobados']
cuenta_q = collections.Counter(b['core'] for b in q)
nucleo = [k for k in seen if viv[k]['dominio'] == 'core' and k != M]
txt = ['# Pasada C: %s pasa del nucleo a entrega\n' % M]
claves = {}
for cid, punta, excluir, extra in (('C-A', 'equipo_conjunto_de_mejora_con_proveedores', set(), lambda k: cuenta_q[k] < 2),
                                   ('C-B', 'collaboration_enablers', {M}, lambda k: True)):
    cand = sorted(((cos(punta, k), k) for k in nucleo if k in vec and k not in excluir and extra(k) and k != punta
                   and punta not in (viv[k].get('nodos_siguientes') or [])), reverse=True)[:8]
    claves[cid] = {'punta': punta, 'candidatos': [k for s, k in cand]}
    que = ('ANCLA DEL NUCLEO para el puente hacia este nodo de calidad' if cid == 'C-A'
           else 'PREDECESOR DEL NUCLEO para este nodo del nucleo, que solo entraba por un nodo que pasa a entrega')
    txt.append('### %s: elige un %s\n- NODO\n    %s\n- CANDIDATOS' % (cid, que, ficha(punta)))
    for j, (s, k) in enumerate(cand, 1):
        txt.append('  %d. [%s]\n    %s' % (j, k, ficha(k)))
    txt.append('')
txt.append('## C-C: aristas del nucleo que ahora llegan al mundo de entrega (logistica y entrega)\n- NODO DEL MUNDO ENTREGA [%s]\n    %s\n' % (M, ficha(M)))
for i, a in enumerate(sorted(p for p in viv[M].get('nodos_previos') or [] if p in viv and viv[p]['dominio'] == 'core'), 1):
    cid = 'C-C%d' % i
    claves[cid] = {'core': a, 'mundo': M}
    txt.append('### %s: %s -> %s\n- NODO DEL NUCLEO\n    %s\n' % (cid, a, M, ficha(a)))
os.makedirs(os.path.join(W, 'C'), exist_ok=True)
io.open(os.path.join(W, 'C', 'lote_C.md'), 'w', encoding='utf-8').write('\n'.join(txt))
json.dump(claves, io.open(os.path.join(W, 'C', 'claves.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(claves, ensure_ascii=False))
