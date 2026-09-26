# -*- coding: utf-8 -*-
"""Mezcla a ciegas las trampas de la pasada J en sus lotes (solo la sesion escribe, y solo en su scratchpad).
Uso: python mezclar_J.py <W> <salida_workflow_trampas.output>"""
import hashlib
import io
import json
import os
import random
import sys

W = sys.argv[1]
J = os.path.join(W, 'J')
salida = json.load(io.open(sys.argv[2], encoding='utf-8'))
escritas = {t['clave']: t for t in salida['result']}
bases = json.load(io.open(os.path.join(J, 'bases_trampa.json'), encoding='utf-8'))
faltan = [b['clave'] for b in bases if b['clave'] not in escritas]
assert not faltan, faltan
CAMPO = {'resumen': 'resumen', 'entregable': 'entregable', 'pasos': 'pasos', 'condiciones': 'condiciones'}


def limpio(s):
    return ' '.join(str(s).split())


trampas_por_lote = {}
for b in bases:
    t = escritas[b['clave']]
    n = {k: (list(v) if isinstance(v, list) else v) for k, v in b.items() if k in ('id', 'mundo', 'titulo', 'resumen', 'pasos', 'entregable', 'condiciones')}
    c = CAMPO[t['campo']]
    if c in ('pasos', 'condiciones'):
        i = min(max(t['indice'], 0), max(len(n[c]) - 1, 0))
        if n[c]:
            n[c][i] = t['texto_nuevo']
        else:
            n[c] = [t['texto_nuevo']]
    else:
        n[c] = t['texto_nuevo']
    trampas_por_lote.setdefault(b['lote'], []).append({'nodo': n, 'trampa': dict(t, tipo=b['tipo'], base=b['id'])})

args = {}
for lote in sorted(trampas_por_lote):
    reales = json.load(io.open(os.path.join(J, 'reales', lote + '.json'), encoding='utf-8'))
    items = [{'real': True, 'nodo': x} for x in reales] + [{'real': False, **x} for x in trampas_por_lote[lote]]
    random.Random(int(hashlib.sha256(('Jmezcla' + lote).encode()).hexdigest()[:8], 16)).shuffle(items)
    mapa, bloques, ids_trampa = {}, [], {}
    for i, it in enumerate(items, 1):
        ident = '%s-%03d' % (lote, i)
        n = it['nodo']
        if it['real']:
            mapa[ident] = {'real': True, 'id': n['id'], 'mundo': n['mundo']}
        else:
            mapa[ident] = {'real': False, 'trampa': it['trampa']}
            ids_trampa[ident] = it['trampa']['tipo']
        pasos = '\n'.join('  %d. %s' % (j + 1, limpio(p)) for j, p in enumerate(n['pasos'])) or '  (ninguno)'
        conds = '\n'.join('  - %s' % limpio(c) for c in n['condiciones']) or '  - (ninguna)'
        bloques.append('### %s\n- titulo: %s\n- resumen: %s\n- pasos:\n%s\n- entregable: %s\n- condiciones de activacion:\n%s\n' % (
            ident, limpio(n['titulo']), limpio(n['resumen']), pasos, limpio(n['entregable']), conds))
    json.dump(mapa, io.open(os.path.join(J, 'claves', 'mapa_%s.json' % lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cab = '# Lote %s: %d nodos del catalogo de My-idea\n\n' % (lote, len(items))
    io.open(os.path.join(J, 'lotes', 'lote_%s.md' % lote), 'w', encoding='utf-8', newline='\n').write(cab + '\n'.join(bloques))
    args[lote] = {'n': len(items), 'trampas': ids_trampa}
json.dump(args, io.open(os.path.join(J, 'args_lectura.json'), 'w', encoding='utf-8'), indent=1)
print('lotes', len(args), '| filas', sum(a['n'] for a in args.values()), '| trampas', sum(len(a['trampas']) for a in args.values()))
