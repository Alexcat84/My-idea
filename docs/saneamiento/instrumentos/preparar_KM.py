# -*- coding: utf-8 -*-
"""Pasadas K (COHERENCIA INTERNA, todos los vivos) y M (MUESTRA con semilla: titulo, condiciones, fase, dominio)
del diagnostico de saneamiento. Prepara reales y bases de trampa. Solo lectura del repo.
Uso: python preparar_KM.py <repo> <W>"""
import glob
import hashlib
import io
import json
import os
import random
import sys

REPO, W = sys.argv[1], sys.argv[2]
SEMILLA = 20260926
nodos = {}
for p in glob.glob(os.path.join(REPO, 'dataset/nodos/*.json')):
    n = json.load(io.open(p, encoding='utf-8'))
    if not n.get('deprecado'):
        nodos[n['node_id']] = {'id': n['node_id'], 'mundo': n['dominio'], 'fase': n['fase_proyecto'],
                               'titulo': n['titulo_concepto'], 'resumen': n['resumen_teorico'],
                               'pasos': n.get('pasos_accionables') or [], 'entregable': n.get('entregable_esperado') or '',
                               'condiciones': n.get('condiciones_activacion') or []}
ids = sorted(nodos)

# ---- K: todos los vivos, 46 lotes; 2 trampas por lote sobre un nodo de OTRO lote
os.makedirs(os.path.join(W, 'K/reales'), exist_ok=True)
azar = random.Random(SEMILLA)
orden = ids[:]
azar.shuffle(orden)
N = 46
lotesK = {'K%02d' % (i + 1): orden[i::N] for i in range(N)}
for l, v in lotesK.items():
    json.dump([nodos[k] for k in v], io.open(os.path.join(W, 'K/reales', l + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
basesK = []
nombres = sorted(lotesK)
for i, l in enumerate(nombres):
    fuente = lotesK[nombres[(i + 1) % N]]
    az = random.Random(int(hashlib.sha256(('K' + l).encode()).hexdigest()[:8], 16))
    for t in ('RESUMEN_CONTRA_PASOS', 'ENTREGABLE_AJENO'):
        k = az.choice(fuente)
        basesK.append(dict(nodos[k], clave='%s-%s' % (l, t), lote=l, tipo=t))
json.dump(basesK, io.open(os.path.join(W, 'K/bases_trampa.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---- M: muestra con semilla escrita, 300 vivos, 6 lotes de 50; 2 trampas por lote (fase y dominio cambiados,
# o titulo y condicion ajenos), sobre nodos FUERA de la muestra
os.makedirs(os.path.join(W, 'M/reales'), exist_ok=True)
muestra = sorted(random.Random(SEMILLA + 1).sample(ids, 300))
lotesM = {'M%02d' % (i + 1): muestra[i::6] for i in range(6)}
for l, v in lotesM.items():
    json.dump([nodos[k] for k in v], io.open(os.path.join(W, 'M/reales', l + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
fuera = [k for k in ids if k not in set(muestra)]
basesM = []
for l in sorted(lotesM):
    az = random.Random(int(hashlib.sha256(('M' + l).encode()).hexdigest()[:8], 16))
    for t in ('FASE_O_DOMINIO_MAL', 'TITULO_O_CONDICION_AJENA'):
        k = az.choice(fuera)
        fuera.remove(k)
        basesM.append(dict(nodos[k], clave='%s-%s' % (l, t), lote=l, tipo=t))
json.dump(basesM, io.open(os.path.join(W, 'M/bases_trampa.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'semilla': SEMILLA + 1, 'muestra': muestra}, io.open(os.path.join(W, 'M/muestra.json'), 'w', encoding='utf-8'), indent=1)
print('K: lotes', len(lotesK), 'nodos', sum(len(v) for v in lotesK.values()), 'bases', len(basesK))
print('M: semilla', SEMILLA + 1, 'muestra', len(muestra), 'lotes', len(lotesM), 'bases', len(basesM))
