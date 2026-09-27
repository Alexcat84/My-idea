# -*- coding: utf-8 -*-
"""Mezcla a ciegas las trampas con los pasos reales de cada lote del tramo 1.

Salidas:
  lotes/lote_<X>.md          lo que ve el lector: ids opacos, sin veredictos ni marcas
  claves/mapa_<X>.json       id opaco -> paso real (node_id, paso) o trampa (tipo, clave)
  claves/trampas_ids.json    ids de trampa por lote, para el workflow
"""
import io
import json
import random
import sys

W = sys.argv[1]
SEMILLA = 20260924
REPARTO = {  # lote -> [(libro de trampas, cuantas contrarias, cuantas anadidas)]
    'DK1': [('DK', 2, 2)], 'DK2': [('DK', 2, 2)], 'DK3': [('DK', 2, 2)], 'DK4': [('DK', 2, 2)],
    'SB1': [('SB', 2, 2)], 'SB2': [('SB', 2, 2)],
    'FX1': [('FX', 2, 2)],
    'O56': [('O5', 1, 1), ('O6', 1, 1)],
}
FICHERO = {v['clave']: v['fichero'] for v in json.load(io.open(W + '/libros.json', encoding='utf-8')).values()}

trampas = {}
for clave in {t for r in REPARTO.values() for t, _, _ in r}:
    trampas[clave] = json.load(io.open('%s/trampas/%s.json' % (W, clave), encoding='utf-8'))
usadas = {k: {'CONTRARIO': 0, 'ANADIDO': 0} for k in trampas}

azar = random.Random(SEMILLA)
ids_trampa = {}
for lote, reparto in REPARTO.items():
    items = [dict(x, _real=True) for x in json.load(io.open('%s/claves/reales_%s.json' % (W, lote), encoding='utf-8'))]
    for clave, nc, na in reparto:
        for tipo, n in (('CONTRARIO', nc), ('ANADIDO', na)):
            del_tipo = [t for t in trampas[clave] if t['tipo'] == tipo]
            for t in del_tipo[usadas[clave][tipo]:usadas[clave][tipo] + n]:
                items.append({'_real': False, 'tipo': tipo, 'clave': clave, 'titulo': t['titulo'],
                              'resumen': t['resumen'], 'texto': t['texto'], 'fichero': FICHERO[clave],
                              'paso': azar.randint(1, 5), 'trampa': t})
            usadas[clave][tipo] += n
    azar.shuffle(items)
    mapa, filas, ids_trampa[lote] = {}, [], []
    for i, it in enumerate(items, 1):
        ident = '%s-%03d' % (lote, i)
        if it['_real']:
            mapa[ident] = {'real': True, 'node_id': it['node_id'], 'paso': it['paso'], 'libro': it['libro']}
        else:
            mapa[ident] = {'real': False, 'tipo': it['tipo'], 'clave': it['clave'], 'trampa': it['trampa']}
            ids_trampa[lote].append(ident)
        resumen = ' '.join(str(it['resumen']).split())
        filas.append('| %s | %s | %s | %d | %s | %s |' % (
            ident, it['titulo'].replace('|', '/'), resumen.replace('|', '/'), it['paso'],
            ' '.join(it['texto'].split()).replace('|', '/'), it['fichero']))
    json.dump(mapa, io.open('%s/claves/mapa_%s.json' % (W, lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cab = ('# Lote %s: %d pasos a leer contra su libro\n\n'
           '| id | titulo del nodo | resumen del nodo | paso | texto del paso | fichero del libro |\n'
           '|---|---|---|---:|---|---|\n') % (lote, len(filas))
    io.open('%s/lotes/lote_%s.md' % (W, lote), 'w', encoding='utf-8', newline='\n').write(cab + '\n'.join(filas) + '\n')
    print(lote, len(filas), 'pasos,', len(ids_trampa[lote]), 'trampas')
json.dump(ids_trampa, io.open(W + '/claves/trampas_ids.json', 'w', encoding='utf-8'), indent=1)
for k, v in usadas.items():
    for tipo, n in v.items():
        disponibles = len([t for t in trampas[k] if t['tipo'] == tipo])
        assert n <= disponibles, (k, tipo, n, disponibles)
