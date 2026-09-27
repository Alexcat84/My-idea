# -*- coding: utf-8 -*-
"""Pasada D del saneamiento (decision del fundador del 26 sep 2026, escrita "28 sep"): los 35 nodos del nucleo que la
pasada Q vio de un mundo se deciden NODO POR NODO con la prueba "lo necesita cualquier emprendedor aunque nunca active
ese mundo?". SI: se queda en el nucleo (un tema general que el mundo profundiza). NO: se mueve a su mundo.
Trampas: NUCLEO (dos semillas de entrada del nucleo con un mundo propuesto inventado: tienen que salir SI) y MUNDO (dos
nodos reales del mundo de entrega presentados como del nucleo: tienen que salir NO). Solo lectura del repo.
Uso: python preparar_D.py <repo> <W>"""
import glob
import io
import json
import os
import random
import sys

REPO, W = sys.argv[1], sys.argv[2]
os.chdir(REPO)
nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    if not n.get('deprecado'):
        nod[n['node_id']] = n
MUNDO = {'entrega': 'logistica y entrega (empaque, envio, inventario, transporte, devoluciones)',
         'compras': 'compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra)',
         'quality': 'gestion de la calidad', 'risk_management': 'gestion de riesgos',
         'seguridad_digital': 'seguridad digital', 'health_safety': 'seguridad y salud en el trabajo'}
ret = json.load(io.open('docs/saneamiento/resultados/Q/retenidos_nucleo_a_mundo.json', encoding='utf-8'))
items = [(x['nodo'], x['a'], None) for x in ret]
az = random.Random(20261003)
semillas = json.load(io.open('dataset/metadata/entry_seeds.json', encoding='utf-8'))['seeds']
for s, m in zip(az.sample([s for s in semillas if nod[s]['dominio'] == 'core'], 2), ('risk_management', 'compras')):
    items.append((s, m, 'NUCLEO'))
for s in az.sample(sorted(k for k, n in nod.items() if n['dominio'] == 'entrega'), 2):
    items.append((s, 'entrega', 'MUNDO'))
az.shuffle(items)


def limpio(t):
    return ' '.join(str(t).split())


txt = ['# Pasada D: %d nodos, el nucleo o su mundo\n' % len(items)]
claves, trampas = {}, {}
for i, (k, m, t) in enumerate(items, 1):
    n = nod[k]
    cid = 'D-%02d' % i
    claves[cid] = {'nodo': k, 'mundo': m, 'trampa': t}
    if t:
        trampas[cid] = t
    pasos = '\n'.join('  %d. %s' % (j + 1, limpio(p)) for j, p in enumerate(n.get('pasos_accionables') or []))
    txt.append('### %s\n- mundo propuesto: %s (%s)\n- titulo: %s\n- resumen: %s\n- pasos:\n%s\n- entregable: %s\n' % (
        cid, m, MUNDO[m], limpio(n['titulo_concepto']), limpio(n['resumen_teorico']), pasos, limpio(n.get('entregable_esperado') or '')))
os.makedirs(os.path.join(W, 'D'), exist_ok=True)
io.open(os.path.join(W, 'D', 'lote_D.md'), 'w', encoding='utf-8').write('\n'.join(txt))
json.dump(claves, io.open(os.path.join(W, 'D', 'claves.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({'n': len(items), 'trampas': trampas}))
