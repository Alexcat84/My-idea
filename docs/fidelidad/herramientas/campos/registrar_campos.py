# -*- coding: utf-8 -*-
"""Registro de la pasada sobre los campos que llegan a la IA (rama fidelidad-total) y comprobacion contra main de que
cada hallazgo tiene su correccion declarada en el campo que toca.

Uso: python registrar_campos.py <W> <salida_lectura.output> <salida_extra_R013.output> <repo_fidelidad> <repo_correcciones>
"""
import collections
import io
import json
import os
import shutil
import sys

W, SAL, EXTRA, RF, RC = sys.argv[1:6]
DST = RF + '/docs/fidelidad/campania/campos'
os.makedirs(DST, exist_ok=True)
CAMPO = {'resumen': 'resumen_teorico', 'entregable': 'entregable_esperado', 'condiciones': 'condiciones_activacion',
         'etiqueta': 'etiqueta_arbol', 'titulo': 'titulo_concepto'}
R = json.load(io.open(SAL, encoding='utf-8'))['result']
res = {'lotes': [], 'nodos': 0, 'trampas_lector': [0, 0], 'trampas_verificador': [0, 0], 'desacuerdos': 0,
       'relecturas': [], 'hallazgos': collections.Counter(), 'nodos_con_hallazgo': 0}
filas = []
for r in R:
    lote = r['lote']
    mapa = json.load(io.open('%s/c2/claves/mapa_%s.json' % (W, lote), encoding='utf-8'))
    h = r['historial'][-1]['recall']
    res['trampas_lector'][0] += h['detectadas']
    res['trampas_lector'][1] += h['total']
    res['trampas_verificador'][0] += r['recallVerificador']['detectadas']
    res['trampas_verificador'][1] += r['recallVerificador']['total']
    res['desacuerdos'] += r['desacuerdos']
    if len(r['historial']) > 1:
        res['relecturas'].append(lote)
    res['lotes'].append({'lote': lote, 'desacuerdos': r['desacuerdos'], 'trampas_lector': h, 'trampas_verificador': r['recallVerificador']})
    for x in r['final']:
        m = mapa[x['id']]
        res['nodos'] += 1
        if x['hallazgos']:
            res['nodos_con_hallazgo'] += 1
        for hh in x['hallazgos']:
            res['hallazgos']['%s %s' % (hh['campo'], hh['veredicto'])] += 1
        filas.append({'id': x['id'], 'node_id': m['node_id'], 'libro': m['libro'], 'decidido_por': x['decidido_por'],
                      'hallazgos': x['hallazgos']})
ex = json.load(io.open(EXTRA, encoding='utf-8'))['result']
json.dump(ex, io.open(DST + '/VERIFICADOR_EXTRA_R013.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
res['verificador_extra_R013'] = {'motivo': 'el lector de R013 no cazo una trampa en dos lecturas; un verificador ciego nuevo releyo sus nodos limpios no muestreados con las 4 trampas dentro',
                                 'trampas': '3 de 4 (la de un plazo anadido en una condicion, R013-014, se escapo a las cuatro lecturas)',
                                 'hallazgos_en_nodos_reales': 0}
res['hallazgos'] = dict(res['hallazgos'])
with io.open(DST + '/VEREDICTOS_CAMPOS.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for x in sorted(filas, key=lambda x: x['id']):
        f.write(json.dumps(x, ensure_ascii=False) + '\n')
for d in ('lotes', 'trampas', 'claves'):
    shutil.copytree('%s/c2/%s' % (W, d), '%s/rastro/%s' % (DST, d), dirs_exist_ok=True)
shutil.copy('%s/c2/plan_lotes.json' % W, DST + '/rastro/plan_lotes.json')
# comprobacion contra main
sin = []
for x in filas:
    if not x['hallazgos']:
        continue
    d = json.load(io.open('%s/dataset/nodos/%s.json' % (RC, x['node_id']), encoding='utf-8'))
    for hh in x['hallazgos']:
        c = CAMPO[hh['campo']]
        ok = any(k.get('campo') == c and x['id'] in k.get('auditoria', '') and (c != 'condiciones_activacion' or k.get('indice') == hh['indice'])
                 for k in d.get('correcciones', []))
        if not ok:
            sin.append((x['node_id'], hh['campo'], hh['indice'], x['id']))
res['hallazgos_sin_correccion_en_main'] = sin
json.dump(res, io.open(DST + '/RESUMEN.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('nodos', res['nodos'], '| con hallazgo', res['nodos_con_hallazgo'], '|', res['hallazgos'], '| trampas', res['trampas_lector'], res['trampas_verificador'],
      '| desacuerdos', res['desacuerdos'], '| sin correccion en main', len(sin), sin[:5])
