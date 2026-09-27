# -*- coding: utf-8 -*-
"""Pasada R (ARISTAS RANCIAS tras las correcciones) del diagnostico de saneamiento, solo lectura del repo.
Universo: las aristas vivas que tocan a un nodo corregido por la campania de fidelidad. Cada nodo corregido va con
sus correcciones (antes y despues) y cada vecino con su titulo y resumen. Trampas: 2 aristas FALSAS por lote hacia un
nodo vivo de otro dominio sin relacion (semilla escrita).
Uso: python preparar_R.py <repo> <W>"""
import glob
import hashlib
import io
import json
import os
import random
import sys

REPO, W = sys.argv[1], sys.argv[2]
R = os.path.join(W, 'R')
for d in ('lotes', 'claves'):
    os.makedirs(os.path.join(R, d), exist_ok=True)
N = {}
for p in glob.glob(os.path.join(REPO, 'dataset/nodos/*.json')):
    n = json.load(io.open(p, encoding='utf-8'))
    N[n['node_id']] = n
viv = {k for k, n in N.items() if not n.get('deprecado')}
corr = sorted(k for k in viv if N[k].get('correcciones'))
random.Random(20260926).shuffle(corr)
TAM = 25
lotes = {'R%02d' % (i + 1): corr[i::-(-len(corr) // TAM)] for i in range(-(-len(corr) // TAM))}


def limpio(s):
    return ' '.join(str(s).split())


def corto(s, n=320):
    s = limpio(s)
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '...'


args = {}
for lote, ks in sorted(lotes.items()):
    az = random.Random(int(hashlib.sha256(('R' + lote).encode()).hexdigest()[:8], 16))
    trampa_en = set(az.sample(range(len(ks)), 2))
    bloques, mapa, trampas, total = [], {}, {}, 0
    for i, k in enumerate(ks):
        n = N[k]
        aristas = [('siguiente', v) for v in (n.get('nodos_siguientes') or []) if v in viv] + \
                  [('previo', v) for v in (n.get('nodos_previos') or []) if v in viv]
        if i in trampa_en:
            ajeno = az.choice([x for x in viv if N[x]['dominio'] != n['dominio'] and x not in dict(aristas).values()])
            aristas.insert(az.randrange(len(aristas) + 1), (az.choice(['siguiente', 'previo']), ajeno))
        cambios = '\n'.join('  - %s: ANTES "%s" / AHORA "%s"' % (c['campo'], corto(c['texto_anterior'], 260), corto(c['texto_nuevo'], 260))
                            for c in n['correcciones'])
        lineas = []
        for j, (sentido, v) in enumerate(aristas, 1):
            aid = '%s-%02d-%02d' % (lote, i + 1, j)
            falsa = (i in trampa_en and v not in (n.get('nodos_siguientes') or []) + (n.get('nodos_previos') or []))
            mapa[aid] = {'nodo': k, 'vecino': v, 'sentido': sentido, 'trampa': falsa}
            if falsa:
                trampas[aid] = 'ARISTA_FALSA'
            rel = 'va DESPUES de este nodo' if sentido == 'siguiente' else 'va ANTES de este nodo'
            lineas.append('  - %s: el vecino %s. Titulo: %s. Resumen: %s' % (aid, rel, limpio(N[v]['titulo_concepto']), corto(N[v]['resumen_teorico'])))
            total += 1
        bloques.append('### NODO %s-%02d\n- titulo: %s\n- resumen de hoy: %s\n- pasos de hoy: %s\n- correcciones de la campania de fidelidad:\n%s\n- sus aristas:\n%s\n' % (
            lote, i + 1, limpio(n['titulo_concepto']), limpio(n['resumen_teorico']),
            ' | '.join(limpio(p) for p in n.get('pasos_accionables') or []), cambios, '\n'.join(lineas)))
    json.dump(mapa, io.open(os.path.join(R, 'claves', 'mapa_%s.json' % lote), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    io.open(os.path.join(R, 'lotes', 'lote_%s.md' % lote), 'w', encoding='utf-8', newline='\n').write(
        '# Lote %s: %d nodos corregidos y sus %d aristas\n\n' % (lote, len(ks), total) + '\n'.join(bloques))
    args[lote] = {'n': total, 'trampas': trampas}
json.dump(args, io.open(os.path.join(R, 'args_compacto.json'), 'w', encoding='utf-8'), separators=(',', ':'))
print('R: nodos corregidos', len(corr), '| lotes', len(lotes), '| aristas', sum(a['n'] for a in args.values()),
      '| trampas', sum(len(a['trampas']) for a in args.values()))
