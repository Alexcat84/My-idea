# -*- coding: utf-8 -*-
"""Cobertura final de la campania de fidelidad: cada paso vivo del catalogo en main, una vez.

Uso: python cobertura_final.py <repo_fidelidad> <repo_correcciones>
Lee VEREDICTOS_TRAMO1.jsonl (calibracion, commit 6f024db) y c2/VEREDICTOS_CAMPANIA.jsonl, y los cruza con
los nodos vivos de dataset/nodos (deprecado no verdadero). Imprime censo por clase y por libro.
"""
import collections
import glob
import io
import json
import os
import sys

RF, RC = sys.argv[1:3]
reg = {}
dup = []
for f in (RF + '/docs/fidelidad/campania/VEREDICTOS_TRAMO1.jsonl', RF + '/docs/fidelidad/campania/c2/VEREDICTOS_CAMPANIA.jsonl'):
    for l in io.open(f, encoding='utf-8'):
        x = json.loads(l)
        k = (x['node_id'], int(x['paso']))
        if k in reg:
            dup.append(k)
        reg[k] = x
vivos = set()
libro_de = {}
for f in glob.glob(RC + '/dataset/nodos/*.json'):
    d = json.load(io.open(f, encoding='utf-8'))
    if d.get('deprecado') is True:
        continue
    for i in range(len(d['pasos_accionables'])):
        vivos.add((d['node_id'], i + 1))
    libro_de[d['node_id']] = d.get('fuente', '')
faltan = sorted(vivos - set(reg))
sobran = sorted(set(reg) - vivos)
cuenta = collections.Counter(reg[k]['veredicto'] for k in vivos if k in reg)
por_libro = collections.defaultdict(collections.Counter)
for k in vivos:
    if k in reg:
        por_libro[reg[k].get('libro') or libro_de.get(k[0], '')][reg[k]['veredicto']] += 1
res = {'pasos_vivos': len(vivos), 'con_veredicto': len(vivos) - len(faltan), 'faltan': faltan[:50], 'n_faltan': len(faltan),
       'sobran': sobran[:50], 'n_sobran': len(sobran), 'duplicados': dup[:50], 'n_duplicados': len(dup),
       'censo': dict(cuenta), 'por_libro': {k: dict(v) for k, v in sorted(por_libro.items())}}
json.dump(res, io.open(RF + '/docs/fidelidad/campania/COBERTURA_FINAL.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('pasos vivos %d | con veredicto %d | faltan %d | sobran %d | duplicados %d' % (len(vivos), res['con_veredicto'], len(faltan), len(sobran), len(dup)))
print('censo', dict(cuenta))
