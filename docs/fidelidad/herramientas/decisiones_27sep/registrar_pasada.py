# -*- coding: utf-8 -*-
"""Escribe (solo la sesion escribe) el registro de una pasada ciega (P = tramos 1 y 2, Q = tramo 3) en la rama
fidelidad-total: VEREDICTOS_<nombre>.jsonl con un veredicto por paso real (sin trampas) y RESUMEN_<nombre>.json con
trampas, desacuerdos y cuentas. Copia tambien el rastro (lotes mezclados, trampas, mapas, plan).

Uso: python registrar_pasada.py <W_pasada> <salida_workflow.output> <repo_fidelidad> <nombre: p2|p3>
"""
import collections
import io
import json
import os
import shutil
import sys

W, SAL, RF, NOM = sys.argv[1:5]
DST = RF + '/docs/fidelidad/campania/' + NOM
os.makedirs(DST, exist_ok=True)
o = json.load(io.open(SAL, encoding='utf-8'))
filas, res = [], {'lotes': [], 'cuenta': collections.Counter(), 'trampas_lector': [0, 0], 'trampas_verificador': [0, 0],
                  'desacuerdos': 0, 'relecturas': []}
for r in o['result']:
    lote = r['lote']
    mapa = json.load(io.open('%s/c2/claves/mapa_%s.json' % (W, lote), encoding='utf-8'))
    reales = {(x['node_id'], x['paso']): x for x in json.load(io.open('%s/c2/claves/reales_%s.json' % (W, lote), encoding='utf-8'))}
    h = r['historial'][-1]['recall']
    res['trampas_lector'][0] += h['detectadas']
    res['trampas_lector'][1] += h['total']
    res['trampas_verificador'][0] += r['recallVerificador']['detectadas']
    res['trampas_verificador'][1] += r['recallVerificador']['total']
    res['desacuerdos'] += r['desacuerdos']
    if len(r['historial']) > 1:
        res['relecturas'].append(lote)
    res['lotes'].append({'lote': lote, 'cuenta': r['cuenta'], 'desacuerdos': r['desacuerdos'],
                         'trampas_lector': h, 'trampas_verificador': r['recallVerificador']})
    for x in r['final']:
        m = mapa[x['id']]
        re_ = reales[(m['node_id'], m['paso'])]
        res['cuenta'][x['veredicto']] += 1
        filas.append({'id': x['id'], 'node_id': m['node_id'], 'paso': m['paso'], 'libro': m['libro'], 'veredicto': x['veredicto'],
                      'lineas': x.get('lineas', ''), 'frase_clave': x.get('frase_clave', ''), 'razon': x.get('razon', ''),
                      'dato': x.get('dato', ''), 'texto_fiel': x.get('texto_fiel', ''), 'texto_sugerencia': x.get('texto_sugerencia', ''),
                      'decidido_por': x.get('decidido_por', ''), 'lector': x.get('lector', ''), 'verificador': x.get('verificador', ''),
                      'primera_lectura': re_['id_primera_lectura'], 'origen': re_['origen']})
with io.open(DST + '/VEREDICTOS_SEGUNDA_PASADA.jsonl' if NOM == 'p2' else DST + '/VEREDICTOS_AMPLIACION.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for x in sorted(filas, key=lambda x: x['id']):
        f.write(json.dumps(x, ensure_ascii=False) + '\n')
res['cuenta'] = dict(res['cuenta'])
res['pasos'] = len(filas)
json.dump(res, io.open(DST + '/RESUMEN.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
for d in ('lotes', 'trampas', 'claves'):
    if os.path.isdir('%s/c2/%s' % (W, d)):
        shutil.copytree('%s/c2/%s' % (W, d), '%s/rastro/%s' % (DST, d), dirs_exist_ok=True)
shutil.copy('%s/c2/plan_lotes.json' % W, DST + '/rastro/plan_lotes.json')
print(NOM, len(filas), 'pasos', res['cuenta'], 'trampas', res['trampas_lector'], res['trampas_verificador'], 'desacuerdos', res['desacuerdos'])
