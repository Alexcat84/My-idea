# -*- coding: utf-8 -*-
"""Prepara los lotes de la campania completa (todo menos lo leido en el tramo 1), en orden de riesgo.

Salida en <W>/c2/: claves/reales_<lote>.json (privado), plan_lotes.json (lote -> libros, n, ficheros).
"""
import io
import json
import os
import sys

W, REPO = sys.argv[1], sys.argv[2]
OBJ = 110
L = json.load(io.open(REPO + '/docs/fidelidad/INVENTARIO_LIBROS.json', encoding='utf-8'))
rows = [json.loads(l) for l in io.open(REPO + '/docs/fidelidad/INVENTARIO_NODOS.jsonl', encoding='utf-8')]
HECHOS = {'The Field Guide to Understandin - Dekker, Sidney', 'SMALL_BUSINESS', 'OSHA3885', 'OSHA3886', 'Guia de empaque para envios (FedEx)'}
TXT = {x['libro']: x['texto'] for x in L}
TRAMO = {x['libro']: x['tramo'] for x in L}


def clave_libro(r):
    return ' | '.join(r['libros']) if r['compuesta'] else r['fuente']


por = {}
for r in sorted(rows, key=lambda r: r['nodo']):
    k = clave_libro(r)
    if k in HECHOS:
        continue
    d = json.load(io.open('%s/dataset/nodos/%s.json' % (REPO, r['nodo']), encoding='utf-8'))
    ficheros = TXT.get(k) or [f for lib in r['libros'] for f in TXT.get(lib, [])]
    for i, p in enumerate(d['pasos_accionables']):
        por.setdefault(k, []).append({'node_id': r['nodo'], 'paso': i + 1, 'titulo': d.get('titulo_concepto', ''),
                                      'resumen': d.get('resumen_teorico', ''), 'texto': p, 'libro': k,
                                      'ficheros': ficheros})

orden = sorted(por, key=lambda k: (TRAMO.get(k, TRAMO.get(k.split(' | ')[0], 3)), -len(por[k])))
lotes, pendiente = [], []


def cerrar(items):
    if items:
        lotes.append(items)


for k in orden:
    items = por[k]
    grupos = {}
    for it in items:
        grupos.setdefault(it['node_id'], []).append(it)
    if len(items) >= OBJ * 0.6:
        n = max(1, round(len(items) / OBJ))
        objetivo = len(items) / n
        cur = []
        for g in grupos.values():
            if len(cur) >= objetivo and len(lotes) >= 0:
                cerrar(cur)
                cur = []
            cur.extend(g)
        cerrar(cur)
    else:
        # libros pequenios: comparten lote dentro del mismo tramo
        if pendiente and (TRAMO.get(pendiente[0]['libro'].split(' | ')[0], 3) != TRAMO.get(k.split(' | ')[0], 3) or len(pendiente) + len(items) > OBJ * 1.2):
            cerrar(pendiente)
            pendiente = []
        pendiente.extend(items)
cerrar(pendiente)
lotes.sort(key=lambda items: min(TRAMO.get(x['libro'].split(' | ')[0], 3) for x in items))

os.makedirs(W + '/c2/claves', exist_ok=True)
plan = {}
for i, items in enumerate(lotes, 1):
    nombre = 'C%03d' % i
    json.dump(items, io.open('%s/c2/claves/reales_%s.json' % (W, nombre), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    libros = sorted({x['libro'] for x in items})
    plan[nombre] = {'n': len(items), 'libros': libros,
                    'ficheros': sorted({f for x in items for f in x['ficheros']}),
                    'tramo': min(TRAMO.get(l.split(' | ')[0], 3) for l in libros)}
json.dump(plan, io.open(W + '/c2/plan_lotes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(lotes), 'lotes;', sum(p['n'] for p in plan.values()), 'pasos')
for t in (1, 2, 3):
    ls = [k for k, p in plan.items() if p['tramo'] == t]
    print('tramo', t, len(ls), 'lotes', sum(plan[k]['n'] for k in ls), 'pasos', ls[0] if ls else '', '..', ls[-1] if ls else '')
print('tamanios', sorted(p['n'] for p in plan.values())[:5], '...', sorted(p['n'] for p in plan.values())[-5:])
