# -*- coding: utf-8 -*-
"""Mezcla a ciegas cada lote de la pasada de etiquetas (solo la sesion escribe).
Uso: python mezclar.py <W> <salida_workflow_trampas.output>
Salidas en <W>: trampas.json, lotes/lote_<lote>.md, claves/mapa_<lote>.json, args_lectura.json."""
import hashlib
import io
import json
import random
import sys

W = sys.argv[1]
salida = json.load(io.open(sys.argv[2], encoding='utf-8'))
escritas = {t['clave']: t for t in salida['result']}
bases = json.load(io.open(W + '/bases_trampa.json', encoding='utf-8'))
faltan, largas = [], []
for lote, v in bases.items():
    for i, b in enumerate(v):
        if b['historica']:
            b['explicacion'] = 'etiqueta erronea REAL del catalogo, corregida en 6871a11e'
            continue
        t = escritas.get('%s-%d' % (lote, i))
        if not t:
            faltan.append('%s-%d' % (lote, i))
            continue
        b['etiqueta_trampa'] = t['etiqueta_trampa']
        b['explicacion'] = t['explicacion']
        if len(t['etiqueta_trampa'].split()) > 6:
            largas.append(t['etiqueta_trampa'])
assert not faltan, faltan
print('trampas de mas de 6 palabras (se quedan, solo se avisa):', largas)
json.dump(bases, io.open(W + '/trampas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def limpio(s):
    return ' '.join(str(s).split())


args = {}
for lote, v in sorted(bases.items()):
    reales = json.load(io.open('%s/reales/%s.json' % (W, lote), encoding='utf-8'))
    items = [dict(x, _real=True) for x in reales]
    for b in v:
        items.append({'_real': False, 'titulo': b['titulo'], 'resumen': b['resumen'], 'etiqueta': b['etiqueta_trampa'], 'trampa': b})
    azar = random.Random(int(hashlib.sha256(('etiquetas' + lote).encode()).hexdigest()[:8], 16))
    azar.shuffle(items)
    mapa, bloques, ids_trampa = {}, [], {}
    for i, it in enumerate(items, 1):
        ident = '%s-%03d' % (lote, i)
        if it['_real']:
            mapa[ident] = {'real': True, 'node_id': it['node_id'], 'etiqueta': it['etiqueta']}
        else:
            mapa[ident] = {'real': False, 'tipo': it['trampa']['tipo'], 'trampa': it['trampa']}
            ids_trampa[ident] = it['trampa']['tipo']
        bloques.append('### %s\n- titulo: %s\n- resumen: %s\n- ETIQUETA: %s\n' % (ident, limpio(it['titulo']), limpio(it['resumen']), limpio(it['etiqueta'])))
    json.dump(mapa, io.open('%s/claves/mapa_%s.json' % (W, lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cab = '# Lote %s: %d etiquetas de cara a leer contra el titulo y el resumen de su nodo\n\n' % (lote, len(items))
    io.open('%s/lotes/lote_%s.md' % (W, lote), 'w', encoding='utf-8', newline='\n').write(cab + '\n'.join(bloques))
    args[lote] = {'n': len(items), 'trampas': ids_trampa}
json.dump(args, io.open(W + '/args_lectura.json', 'w', encoding='utf-8'), indent=1)
print('lotes:', len(args), '| filas', sum(a['n'] for a in args.values()), '| trampas', sum(len(a['trampas']) for a in args.values()))
