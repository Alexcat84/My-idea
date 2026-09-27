# -*- coding: utf-8 -*-
"""Pasada de fidelidad sobre las etiquetas de cara (decision del fundador, 25 sep 2026).
Uso: python preparar.py <repo_my_idea> <W>
Reparte los nodos VIVOS del grafo en lotes y elige, para cada lote, los 4 nodos de OTRO lote sobre los que
se escribiran las trampas (2 CONTRARIA, 2 DISTINTA). En tres lotes una trampa es una de las tres etiquetas
erroneas reales corregidas en 6871a11e.
Salidas en <W>: reales/<lote>.json, bases_trampa.json."""
import hashlib
import io
import json
import os
import random
import sys

REPO, W = sys.argv[1], sys.argv[2]
N_LOTES = 20
for d in ('reales', 'lotes', 'claves'):
    os.makedirs(os.path.join(W, d), exist_ok=True)
g = json.load(io.open(os.path.join(REPO, 'dataset/metadata/master_graph.json'), encoding='utf-8'))['nodos']
vivos = sorted(k for k, v in g.items() if not v.get('deprecado'))
print('vivos', len(vivos))
azar = random.Random(20260925)
azar.shuffle(vivos)
lotes = {'E%02d' % (i + 1): vivos[i::N_LOTES] for i in range(N_LOTES)}


def ficha(k):
    n = g[k]
    return {'node_id': k, 'titulo': n['titulo_concepto'], 'resumen': ' '.join(n['resumen_teorico'].split()), 'etiqueta': n['etiqueta_arbol']}


for lote, ids in lotes.items():
    json.dump([ficha(k) for k in ids], io.open(os.path.join(W, 'reales', lote + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

HISTORICAS = {
    'valor_presente_franquicia_pvf': ('Calcula el Valor Futuro', 'CONTRARIA'),
    'warrants_financiamiento': ('Usa Opciones para Bajar la Valoración', 'CONTRARIA'),
    'modelos_negocio_mas_alla_del_lucro': ('Diseña tu Modelo sin Lucro', 'DISTINTA'),
}
dueno = {k: lote for lote, ids in lotes.items() for k in ids}
nombres = sorted(lotes)
bases = {}
usados = set()
hist = list(HISTORICAS.items())
# las historicas van a los lotes 3, 9 y 15 (o al siguiente si ese es el dueno del nodo)
destino = {}
for j, (k, _) in enumerate(hist):
    i = (2, 8, 14)[j]
    while dueno[k] == nombres[i] or nombres[i] in destino.values():
        i += 1
    destino[k] = nombres[i]
for i, lote in enumerate(nombres):
    fuente = lotes[nombres[(i + 1) % N_LOTES]]
    az = random.Random(int(hashlib.sha256(('etiq' + lote).encode()).hexdigest()[:8], 16))
    tipos = ['CONTRARIA', 'CONTRARIA', 'DISTINTA', 'DISTINTA']
    elegidos = []
    for k, (etq, tipo) in hist:
        if destino[k] == lote:
            assert dueno[k] != lote
            elegidos.append(dict(ficha(k), tipo=tipo, etiqueta_trampa=etq, historica=True))
            usados.add(k)
            tipos.remove(tipo)
    cand = [k for k in fuente if k not in usados and k not in HISTORICAS]
    for tipo in tipos:
        k = az.choice(cand)
        cand.remove(k)
        usados.add(k)
        elegidos.append(dict(ficha(k), tipo=tipo, historica=False))
    bases[lote] = elegidos
json.dump(bases, io.open(os.path.join(W, 'bases_trampa.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({l: len(v) for l, v in lotes.items()})
print('bases de trampa:', sum(len(v) for v in bases.values()), '| a escribir por el generador:', sum(1 for v in bases.values() for x in v if not x['historica']))
