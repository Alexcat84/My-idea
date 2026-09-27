# -*- coding: utf-8 -*-
"""Pasada contra la fuente sobre los campos que no son pasos (decision del fundador del 27 sep, segunda tanda, punto 2):
titulo_concepto, etiqueta_arbol, resumen_teorico, entregable_esperado y condiciones_activacion de cada nodo vivo.
Solo se buscan CONTRARIOS y ANADIDOS de cifra, plazo o norma.

Una fila por nodo. Lotes de ~OBJ nodos del mismo tramo, en orden de riesgo. Salida en <W>/c2/:
claves/reales_<lote>.json (privado) y plan_lotes.json; <W>/args_trampas.json.
Uso: python preparar_campos.py <W> <repo_fidelidad> <repo_correcciones>
"""
import io
import json
import os
import sys

W, RF, RC = sys.argv[1:4]
OBJ = 45
INV = {x['libro']: x for x in json.load(io.open(RF + '/docs/fidelidad/INVENTARIO_LIBROS.json', encoding='utf-8'))}
rows = [json.loads(l) for l in io.open(RF + '/docs/fidelidad/INVENTARIO_NODOS.jsonl', encoding='utf-8')]


def clave(r):
    return ' | '.join(r['libros']) if r['compuesta'] else r['fuente']


items = []
for r in rows:
    d = json.load(io.open('%s/dataset/nodos/%s.json' % (RC, r['nodo']), encoding='utf-8'))
    if d.get('deprecado') is True:
        continue
    fich = [f for lib in r['libros'] for f in INV[lib]['texto']]
    tramo = min(INV[lib]['tramo'] for lib in r['libros'])
    items.append({'node_id': d['node_id'], 'libro': clave(r), 'ficheros': fich, 'tramo': tramo,
                  'titulo': d.get('titulo_concepto', ''), 'etiqueta': d.get('etiqueta_arbol', ''),
                  'resumen': d.get('resumen_teorico', ''), 'entregable': d.get('entregable_esperado', '') or '',
                  'condiciones': list(d.get('condiciones_activacion', []) or [])})
items.sort(key=lambda x: (x['tramo'], x['libro'], x['node_id']))
lotes, cur = [], []
for it in items:
    if cur and (len(cur) >= OBJ or cur[-1]['tramo'] != it['tramo']):
        lotes.append(cur)
        cur = []
    cur.append(it)
if cur:
    lotes.append(cur)
os.makedirs(W + '/c2/claves', exist_ok=True)
plan, args_tr = {}, {}
for i, lote in enumerate(lotes, 1):
    nombre = 'R%03d' % i
    json.dump(lote, io.open('%s/c2/claves/reales_%s.json' % (W, nombre), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    fs = sorted({f for it in lote for f in it['ficheros']})
    plan[nombre] = {'n': len(lote), 'libros': sorted({it['libro'] for it in lote}), 'ficheros': fs, 'tramo': lote[0]['tramo']}
    args_tr[nombre] = {'ficheros': fs}
json.dump(plan, io.open(W + '/c2/plan_lotes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), 'nodos;', len(lotes), 'lotes;', {t: sum(p['n'] for p in plan.values() if p['tramo'] == t) for t in (1, 2, 3)},
      '| max ficheros por lote', max(len(p['ficheros']) for p in plan.values()))
