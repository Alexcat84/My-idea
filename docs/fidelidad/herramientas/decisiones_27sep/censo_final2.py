# -*- coding: utf-8 -*-
"""Censo final tras las decisiones del fundador del 27 sep: el registro de la campania (tramo 1 calibrado y c2),
con los veredictos posteriores encima, en este orden: segunda pasada (p2), ampliacion (p3) y arbitraje de las
EXCEPCIONES. Comprueba tambien, contra main, que cada CONTRARIO conocido tiene su correccion declarada.

Uso: python censo_final2.py <repo_fidelidad> <repo_correcciones> <muestreo_contrarios.json>
Escribe docs/fidelidad/campania/COBERTURA_FINAL.json (con el censo de antes y el de ahora).
"""
import collections
import glob
import io
import json
import sys

RF, RC, MUE = sys.argv[1:4]
C = RF + '/docs/fidelidad/campania'
reg, dup = {}, []
for f in (C + '/VEREDICTOS_TRAMO1.jsonl', C + '/c2/VEREDICTOS_CAMPANIA.jsonl'):
    for l in io.open(f, encoding='utf-8'):
        x = json.loads(l)
        k = (x['node_id'], int(x['paso']))
        if k in reg:
            dup.append(k)
        reg[k] = dict(x, fuente_veredicto=f.split('/')[-1])
antes = collections.Counter(x['veredicto'] for x in reg.values())
cambios = collections.Counter()
for f, nombre in ((C + '/p2/VEREDICTOS_SEGUNDA_PASADA.jsonl', 'segunda pasada'), (C + '/p3/VEREDICTOS_AMPLIACION.jsonl', 'ampliacion')):
    for l in io.open(f, encoding='utf-8'):
        x = json.loads(l)
        k = (x['node_id'], int(x['paso']))
        if reg[k]['veredicto'] != x['veredicto']:
            cambios[(nombre, reg[k]['veredicto'], x['veredicto'])] += 1
        reg[k] = dict(x, fuente_veredicto=nombre)
for x in json.load(io.open(C + '/ARBITRAJE_EXCEPCIONES.json', encoding='utf-8')):
    k = (x['node_id'], int(x['paso']))
    if reg[k]['veredicto'] != x['veredicto']:
        cambios[('arbitraje excepciones', reg[k]['veredicto'], x['veredicto'])] += 1
    reg[k] = dict(reg[k], veredicto=x['veredicto'], fuente_veredicto='arbitraje excepciones')

vivos, libro_de = set(), {}
for f in glob.glob(RC + '/dataset/nodos/*.json'):
    d = json.load(io.open(f, encoding='utf-8'))
    if d.get('deprecado') is True:
        continue
    for i in range(len(d['pasos_accionables'])):
        vivos.add((d['node_id'], i + 1))
    libro_de[d['node_id']] = d.get('fuente', '')
faltan, sobran = sorted(vivos - set(reg)), sorted(set(reg) - vivos)
ahora = collections.Counter(reg[k]['veredicto'] for k in vivos if k in reg)
por_libro = collections.defaultdict(collections.Counter)
for k in vivos:
    if k in reg:
        por_libro[reg[k].get('libro') or libro_de.get(k[0], '')][reg[k]['veredicto']] += 1

contrarios = {k for k in vivos if k in reg and reg[k]['veredicto'] == 'CONTRARIO'}
contrarios |= {(x['node_id'], int(x['paso'])) for x in json.load(io.open(MUE, encoding='utf-8'))}
sin = []
for nid, paso in sorted(contrarios):
    d = json.load(io.open('%s/dataset/nodos/%s.json' % (RC, nid), encoding='utf-8'))
    if not any(c.get('campo') == 'pasos_accionables' and c.get('indice') == paso - 1 for c in d.get('correcciones', [])):
        sin.append((nid, paso))
res = {'pasos_vivos': len(vivos), 'con_veredicto': len(vivos) - len(faltan), 'n_faltan': len(faltan), 'faltan': faltan[:50],
       'n_sobran': len(sobran), 'sobran': sobran[:50], 'n_duplicados': len(dup), 'duplicados': dup[:50],
       'censo_campania': dict(antes), 'censo': dict(ahora),
       'cambios_posteriores': [{'fuente': a, 'de': b, 'a': c, 'pasos': v} for (a, b, c), v in sorted(cambios.items())],
       'contrarios_conocidos': len(contrarios), 'contrarios_sin_corregir_en_main': sin,
       'por_libro': {k: dict(v) for k, v in sorted(por_libro.items())}}
json.dump(res, io.open(C + '/COBERTURA_FINAL.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('pasos vivos %d | con veredicto %d | faltan %d | sobran %d | duplicados %d' % (len(vivos), res['con_veredicto'], len(faltan), len(sobran), len(dup)))
print('censo de la campania', dict(antes))
print('censo ahora', dict(ahora))
for x in res['cambios_posteriores']:
    print('  ', x)
print('CONTRARIOS conocidos %d | sin corregir en main %d %s' % (len(contrarios), len(sin), sin))
