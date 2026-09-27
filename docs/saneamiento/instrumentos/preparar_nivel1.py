# -*- coding: utf-8 -*-
"""NIVEL 1 del saneamiento (decision del fundador del 27 sep 2026): prepara las dos pasadas grandes de lectura.

Pasada Q (criterios 14 y 15): los 3.169 nodos vivos, con la vara calibrada de la pasada M: condiciones de activacion,
dominio y fase (la fase cuenta solo en planificacion y ejecucion: validacion e ideacion ya las leyo la pasada F). Van
primero los nodos-frontera de la politica marco contra pais (dataset/metadata/jurisdiccion.json), con su clase a la
vista: en clase C las condiciones deben decir que aplica si operas o vendes en ese pais; en clase B no deben exigirlo.
Trampas por lote: CONDICION_AJENA (las condiciones de un nodo de otro tema) y DOMINIO_MAL (un nodo con otro mundo).

Pasada K2 (criterio 12): segundo lector ciego, con la vara de la pasada K, sobre los 2.592 nodos que en K leyo un solo
lector (limpios no muestreados). Trampas por lote: RESUMEN_AJENO y ENTREGABLE_AJENO (de un nodo de otro tema).

Las trampas se arman por script (no las escribe un agente): el campo cambiado viene de otro nodo vivo, de otro mundo y
lejano por vector. Solo lectura del repo. Uso: python preparar_nivel1.py <repo> <W>"""
import glob
import hashlib
import io
import json
import math
import os
import random
import sys

REPO, W = sys.argv[1], sys.argv[2]
os.chdir(REPO)
nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    if not n.get('deprecado'):
        nod[n['node_id']] = n
ids = sorted(nod)
jur = json.load(io.open('dataset/metadata/jurisdiccion.json', encoding='utf-8'))['nodos']
PAIS = {'US': 'Estados Unidos', 'EU': 'la Union Europea', 'GB': 'Reino Unido', 'FR': 'Francia', 'CA': 'Canada', 'MX': 'Mexico',
        'ES': 'Espana', 'CO': 'Colombia', 'AR': 'Argentina', 'INT': 'internacional'}
MUNDOS = ['core', 'quality', 'health_safety', 'environmental', 'seguridad_digital', 'exportacion', 'franquicias', 'risk_management', 'compras', 'entrega']
idx = json.load(io.open('web/lib/assets/semantic_index.json', encoding='utf-8'))
vec = dict(zip(idx['ids'], idx['embeddings']))


def cos(a, b):
    x, y = vec[a], vec[b]
    return sum(p * q for p, q in zip(x, y)) / (math.sqrt(sum(p * p for p in x)) * math.sqrt(sum(q * q for q in y)))


def ajeno(k, az):
    """Un nodo vivo de otro mundo y lejano por vector: su texto no encaja con el de k."""
    cand = [c for c in (az.choice(ids) for _ in range(40)) if nod[c]['dominio'] != nod[k]['dominio']]
    return min(cand, key=lambda c: cos(k, c))


def limpio(s):
    return ' '.join(str(s).split())


def bloque(cid, n, q):
    pasos = '\n'.join('  %d. %s' % (j + 1, limpio(p)) for j, p in enumerate(n['pasos_accionables'] or [])) or '  (ninguno)'
    conds = '\n'.join('  - %s' % limpio(c) for c in n['condiciones_activacion'] or []) or '  - (ninguna)'
    meta = ''
    if q:
        meta = '- dominio: %s\n- fase: %s%s\n' % (n['dominio'], n['fase_proyecto'], ' (ya leida: no la midas, fase_ok true)' if n['fase_proyecto'] in ('validacion', 'ideacion') else '')
        j = jur.get(n['node_id'])
        if j and j['clase'] in ('B', 'C'):
            meta += '- marco contra pais: clase %s, %s (%s)\n' % (j['clase'], PAIS[j['pais']],
                     'norma de ese pais: sus condiciones deben decir que aplica si operas o vendes alli' if j['clase'] == 'C'
                     else 'ejemplo de ese pais: las condiciones no deben exigir operar alli')
    return ('### %s\n%s- titulo: %s\n- resumen: %s\n- pasos:\n%s\n- entregable: %s\n- condiciones de activacion:\n%s\n'
            % (cid, meta, limpio(n['titulo_concepto']), limpio(n['resumen_teorico']), pasos, limpio(n.get('entregable_esperado') or ''), conds))


def armar(P, universo, tam, tipos, q):
    D = os.path.join(W, P)
    for d in ('lotes', 'claves'):
        os.makedirs(os.path.join(D, d), exist_ok=True)
    N = (len(universo) + tam - 1) // tam
    lotes = {'%s%03d' % (P, i + 1): universo[i * tam:(i + 1) * tam] for i in range(N)}
    args = {}
    usados = set(universo)
    for l, reales in lotes.items():
        az = random.Random(int(hashlib.sha256((P + l).encode()).hexdigest()[:8], 16))
        items = [(k, None, None) for k in reales]
        for t in tipos:
            base = az.choice([k for k in ids if k not in usados] or ids)
            usados.add(base)
            items.append((base, t, ajeno(base, az)))
        az.shuffle(items)
        mapa, txt, trampas = {}, ['# Lote %s: %d nodos del catalogo de My-idea\n' % (l, len(items))], {}
        for i, (k, t, otro) in enumerate(items, 1):
            cid = '%s-%03d' % (l, i)
            n = dict(nod[k])
            if t == 'CONDICION_AJENA':
                n['condiciones_activacion'] = nod[otro]['condiciones_activacion']
            elif t == 'DOMINIO_MAL':
                n['dominio'] = az.choice([m for m in MUNDOS if m != n['dominio'] and m != 'core'])
            elif t == 'RESUMEN_AJENO':
                n['resumen_teorico'] = nod[otro]['resumen_teorico']
            elif t == 'ENTREGABLE_AJENO':
                n['entregable_esperado'] = nod[otro]['entregable_esperado']
            mapa[cid] = {'nodo': k, 'trampa': t, 'de': otro}
            if t:
                trampas[cid] = t
            txt.append(bloque(cid, n, q))
        io.open(os.path.join(D, 'lotes', 'lote_%s.md' % l), 'w', encoding='utf-8', newline='\n').write('\n'.join(txt))
        json.dump(mapa, io.open(os.path.join(D, 'claves', 'mapa_%s.json' % l), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        args[l] = {'n': len(items), 'trampas': trampas}
    json.dump(args, io.open(os.path.join(D, 'args.json'), 'w', encoding='utf-8'), separators=(',', ':'))
    print(P, 'nodos', len(universo), 'lotes', N)


frontera = [k for k in ids if k in jur]
resto = [k for k in ids if k not in jur]
random.Random(20260930).shuffle(resto)
armar('Q', frontera + resto, 30, ('CONDICION_AJENA', 'DOMINIO_MAL'), True)
K = json.load(io.open('docs/saneamiento/resultados/K/final.json', encoding='utf-8'))
k2 = sorted(x['nodo'] for x in K if x.get('decidido_por') == 'lector (limpio no muestreado)' and x['nodo'] in nod)
random.Random(20260931).shuffle(k2)
armar('K2', k2, 32, ('RESUMEN_AJENO', 'ENTREGABLE_AJENO'), False)
