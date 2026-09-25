# -*- coding: utf-8 -*-
"""Escribe (solo la sesion escribe) las trampas devueltas por el workflow y mezcla a ciegas cada lote.

Uso: python mezclar2.py <W> <salida_workflow_trampas.output> [<otra.output> ...]
Salidas en <W>/c2/: trampas/<lote>.json, lotes/lote_<lote>.md, claves/mapa_<lote>.json,
args_lectura.json (lote -> {n, trampas: {id: tipo}}) acumulado.
"""
import hashlib
import io
import json
import os
import random
import sys

W = sys.argv[1]
C2 = W + '/c2'
for d in ('trampas', 'lotes', 'claves'):
    os.makedirs('%s/%s' % (C2, d), exist_ok=True)
args_path = C2 + '/args_lectura.json'
args = json.load(io.open(args_path, encoding='utf-8')) if os.path.exists(args_path) else {}
sin_trampas = []
for salida in sys.argv[2:]:
    o = json.load(io.open(salida, encoding='utf-8'))
    for r in o['result']:
        lote, tr = r['lote'], r['trampas']
        if not tr or len(tr) < 4:
            sin_trampas.append(lote)
            continue
        json.dump(tr, io.open('%s/trampas/%s.json' % (C2, lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        reales = json.load(io.open('%s/claves/reales_%s.json' % (C2, lote), encoding='utf-8'))
        items = [dict(x, _real=True) for x in reales]
        azar = random.Random(int(hashlib.sha256(lote.encode()).hexdigest()[:8], 16))
        for t in tr:
            items.append({'_real': False, 'tipo': t['tipo'], 'titulo': t['titulo'], 'resumen': t['resumen'],
                          'texto': t['texto'], 'ficheros': [t['fichero']], 'paso': azar.randint(1, 5), 'trampa': t})
        azar.shuffle(items)
        mapa, filas, ids_trampa = {}, [], {}
        for i, it in enumerate(items, 1):
            ident = '%s-%03d' % (lote, i)
            if it['_real']:
                mapa[ident] = {'real': True, 'node_id': it['node_id'], 'paso': it['paso'], 'libro': it['libro']}
            else:
                mapa[ident] = {'real': False, 'tipo': it['tipo'], 'trampa': it['trampa']}
                ids_trampa[ident] = it['tipo']
            resumen = ' '.join(str(it['resumen']).split())[:400]
            filas.append('| %s | %s | %s | %d | %s | %s |' % (
                ident, it['titulo'].replace('|', '/'), resumen.replace('|', '/'), it['paso'],
                ' '.join(str(it['texto']).split()).replace('|', '/'), ' ; '.join(it['ficheros'])))
        json.dump(mapa, io.open('%s/claves/mapa_%s.json' % (C2, lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        cab = ('# Lote %s: %d pasos a leer contra su libro\n\n'
               '| id | titulo del nodo | resumen del nodo | paso | texto del paso | fichero del libro |\n'
               '|---|---|---|---:|---|---|\n') % (lote, len(filas))
        io.open('%s/lotes/lote_%s.md' % (C2, lote), 'w', encoding='utf-8', newline='\n').write(cab + '\n'.join(filas) + '\n')
        args[lote] = {'n': len(filas), 'trampas': ids_trampa}
json.dump(args, io.open(args_path, 'w', encoding='utf-8'), indent=1)
print('lotes mezclados:', len(args), '| sin trampas completas:', sin_trampas)
