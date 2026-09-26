# -*- coding: utf-8 -*-
"""Mezcla a ciegas las trampas de las pasadas K y M (solo en el scratchpad).
Uso: python mezclar_KM.py <W> <salida_workflow_trampas.output>"""
import hashlib
import io
import json
import os
import random
import sys

W = sys.argv[1]
escritas = {t['clave']: t for t in json.load(io.open(sys.argv[2], encoding='utf-8'))['result']}


def limpio(s):
    return ' '.join(str(s).split())


for P in ('K', 'M'):
    D = os.path.join(W, P)
    for d in ('lotes', 'claves'):
        os.makedirs(os.path.join(D, d), exist_ok=True)
    bases = json.load(io.open(os.path.join(D, 'bases_trampa.json'), encoding='utf-8'))
    faltan = [b['clave'] for b in bases if b['clave'] not in escritas]
    assert not faltan, faltan
    por_lote = {}
    for b in bases:
        t = escritas[b['clave']]
        n = {k: (list(v) if isinstance(v, list) else v) for k, v in b.items()
             if k in ('id', 'mundo', 'fase', 'titulo', 'resumen', 'pasos', 'entregable', 'condiciones')}
        c = {'dominio': 'mundo'}.get(t['campo'], t['campo'])
        if c in ('pasos', 'condiciones'):
            i = min(max(t['indice'], 0), max(len(n[c]) - 1, 0))
            if n[c]:
                n[c][i] = t['texto_nuevo']
            else:
                n[c] = [t['texto_nuevo']]
        else:
            n[c] = t['texto_nuevo']
        por_lote.setdefault(b['lote'], []).append({'nodo': n, 'trampa': dict(t, tipo=b['tipo'], base=b['id'])})
    args = {}
    for lote in sorted(por_lote):
        reales = json.load(io.open(os.path.join(D, 'reales', lote + '.json'), encoding='utf-8'))
        items = [{'real': True, 'nodo': x} for x in reales] + [{'real': False, **x} for x in por_lote[lote]]
        random.Random(int(hashlib.sha256((P + 'mezcla' + lote).encode()).hexdigest()[:8], 16)).shuffle(items)
        mapa, bloques, ids_trampa = {}, [], {}
        for i, it in enumerate(items, 1):
            ident = '%s-%03d' % (lote, i)
            n = it['nodo']
            if it['real']:
                mapa[ident] = {'real': True, 'id': n['id'], 'mundo': n['mundo'], 'fase': n['fase']}
            else:
                mapa[ident] = {'real': False, 'trampa': it['trampa']}
                ids_trampa[ident] = it['trampa']['tipo']
            pasos = '\n'.join('  %d. %s' % (j + 1, limpio(p)) for j, p in enumerate(n['pasos'])) or '  (ninguno)'
            conds = '\n'.join('  - %s' % limpio(c) for c in n['condiciones']) or '  - (ninguna)'
            meta = ('- dominio: %s\n- fase: %s\n' % (n['mundo'], n['fase'])) if P == 'M' else ''
            bloques.append('### %s\n%s- titulo: %s\n- resumen: %s\n- pasos:\n%s\n- entregable: %s\n- condiciones de activacion:\n%s\n' % (
                ident, meta, limpio(n['titulo']), limpio(n['resumen']), pasos, limpio(n['entregable']), conds))
        json.dump(mapa, io.open(os.path.join(D, 'claves', 'mapa_%s.json' % lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        io.open(os.path.join(D, 'lotes', 'lote_%s.md' % lote), 'w', encoding='utf-8', newline='\n').write(
            '# Lote %s: %d nodos del catalogo de My-idea\n\n' % (lote, len(items)) + '\n'.join(bloques))
        args[lote] = {'n': len(items), 'trampas': ids_trampa}
    json.dump(args, io.open(os.path.join(D, 'args_compacto.json'), 'w', encoding='utf-8'), separators=(',', ':'))
    print(P, 'lotes', len(args), '| filas', sum(a['n'] for a in args.values()), '| trampas', sum(len(a['trampas']) for a in args.values()))
