# -*- coding: utf-8 -*-
"""Escribe (solo la sesion escribe) las trampas de la pasada de campos y mezcla a ciegas cada lote.
Uso: python mezclar_campos.py <W> <salida_workflow_trampas.output>
Salidas en <W>/c2/: trampas/<lote>.json, lotes/lote_<lote>.md, claves/mapa_<lote>.json, args_lectura.json."""
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
args, sin = {}, []


def limpio(s):
    return ' '.join(str(s).split()).replace('|', '/')


o = json.load(io.open(sys.argv[2], encoding='utf-8'))
for r in o['result']:
    lote, tr = r['lote'], r['trampas']
    if not tr or len(tr) < 4:
        sin.append(lote)
        continue
    json.dump(tr, io.open('%s/trampas/%s.json' % (C2, lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    reales = json.load(io.open('%s/claves/reales_%s.json' % (C2, lote), encoding='utf-8'))
    items = [dict(x, _real=True) for x in reales]
    for t in tr:
        items.append({'_real': False, 'titulo': t['titulo'], 'etiqueta': t['etiqueta'], 'resumen': t['resumen'],
                      'entregable': t['entregable'], 'condiciones': t['condiciones'], 'ficheros': [t['fichero']], 'trampa': t})
    azar = random.Random(int(hashlib.sha256(('campos' + lote).encode()).hexdigest()[:8], 16))
    azar.shuffle(items)
    mapa, bloques, ids_trampa = {}, [], {}
    for i, it in enumerate(items, 1):
        ident = '%s-%03d' % (lote, i)
        if it['_real']:
            mapa[ident] = {'real': True, 'node_id': it['node_id'], 'libro': it['libro']}
        else:
            mapa[ident] = {'real': False, 'tipo': it['trampa']['tipo'], 'trampa': it['trampa']}
            ids_trampa[ident] = it['trampa']['tipo']
        conds = '\n'.join('  - condiciones[%d]: %s' % (j, limpio(c)) for j, c in enumerate(it['condiciones']))
        bloques.append('### %s\n- fichero del libro: %s\n- titulo: %s\n- etiqueta: %s\n- resumen: %s\n- entregable: %s\n- condiciones:\n%s\n' % (
            ident, ' ; '.join(it['ficheros']), limpio(it['titulo']), limpio(it['etiqueta']), limpio(it['resumen']),
            limpio(it['entregable']), conds or '  - (ninguna)'))
    json.dump(mapa, io.open('%s/claves/mapa_%s.json' % (C2, lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cab = '# Lote %s: %d nodos a leer contra su libro (titulo, etiqueta, resumen, entregable, condiciones)\n\n' % (lote, len(items))
    io.open('%s/lotes/lote_%s.md' % (C2, lote), 'w', encoding='utf-8', newline='\n').write(cab + '\n'.join(bloques))
    args[lote] = {'n': len(items), 'trampas': ids_trampa}
json.dump(args, io.open(C2 + '/args_lectura.json', 'w', encoding='utf-8'), indent=1)
print('lotes mezclados:', len(args), '| filas', sum(a['n'] for a in args.values()), '| sin trampas completas:', sin)
