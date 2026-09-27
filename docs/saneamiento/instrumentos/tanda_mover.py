# -*- coding: utf-8 -*-
"""Decision del fundador: los nodos que la pasada D decidio sacar del nucleo pasan a su mundo, como
colaboracion_transporte_ctm (pasada MV). Escribe las tandas y los ficheros de puentes; no toca dataset/nodos.
  1. DOMINIO: cada nodo que sale del nucleo, con su prueba ("lo necesita cualquier emprendedor...": NO).
  2. Puentes aprobados anclados en un nodo que se mueve AL MISMO mundo del puente: la arista queda dentro del mundo y
     el puente sale del fichero (a `rechazados`, con su motivo).
  3. Puentes aprobados anclados en un nodo que se mueve a OTRO mundo: ancla nueva del nucleo (MV-B); la arista vieja,
     ahora de mundo a mundo, sale.
  4. Aristas del nucleo a un mundo (MV-A): PUENTE se declara dentro de la ley del ancla (mas fuerza y mas score
     primero); lo que no cabe y RETIRAR salen.
  5. Predecesores del nucleo (MV-C) para los que se quedan sin camino por el nucleo.
Uso: python tanda_mover.py <repo> <final D> <final MV> <claves MV>"""
import collections
import glob
import io
import json
import math
import os
import sys

REPO, FD, FMV, CMV = sys.argv[1:5]
os.chdir(REPO)
FECHA = '2026-09-27'
DEC = 'Decision del fundador (nodo por nodo, prueba del nucleo)'
D = json.load(io.open(FD, encoding='utf-8'))
mover = {x['nodo']: x for x in D if x['decision'] == 'NO'}
res = {x['id']: x for x in json.load(io.open(FMV, encoding='utf-8'))}
cl = json.load(io.open(CMV, encoding='utf-8'))
nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    nod[n['node_id']] = n
sys.path.insert(0, 'scripts')
from run_phase1 import aristas_a_simetrizar  # noqa: E402
EXISTE = aristas_a_simetrizar(nod)
dom = {k: n['dominio'] for k, n in nod.items()}
dom.update({k: x['mundo'] for k, x in mover.items()})
idx = json.load(io.open('web/lib/assets/semantic_index.json', encoding='utf-8'))
vec = dict(zip(idx['ids'], idx['embeddings']))


def score(a, b):
    x, y = vec[a], vec[b]
    return round(sum(p * q for p, q in zip(x, y)) / (math.sqrt(sum(p * p for p in x)) * math.sqrt(sum(q * q for q in y))), 4)


corr = []
for k, x in sorted(mover.items()):
    corr.append({'id': 'mv-dominio-%02d' % (len(corr) + 1), 'node_id': k, 'campo': 'dominio', 'veredicto': 'DOMINIO',
                 'texto_anterior': 'core', 'texto_nuevo': x['mundo'],
                 'cita': {'instrumento': 'Pasada D del saneamiento (docs/saneamiento/resultados/D): "lo necesita cualquier emprendedor aunque nunca active ese mundo?" NO',
                          'evidencia': '%s: %s (%s)' % (x['id'], x['motivo'], x['decidido_por'])},
                 'decision': DEC + ': sale del nucleo a su mundo, con sus puentes y predecesores por lectura (pasada MV).', 'fecha': FECHA})
ficheros = {os.path.basename(os.path.dirname(os.path.dirname(p))): p for p in glob.glob('packs/*/metadata/bridges_aprobados.json')}
datos = {m: json.load(io.open(p, encoding='utf-8')) for m, p in ficheros.items()}
ops = []


def op(o, a, b, motivo, evidencia, decision):
    ops.append({'id': 'mv-arista-%03d' % (len(ops) + 1), 'operacion': o, 'desde': a, 'hacia': b, 'motivo': motivo,
                'evidencia': evidencia, 'decision': DEC + ': ' + decision, 'fecha': FECHA})


# 2 y 3
reanclas = {(v['mundo'], v['ancla_vieja'], v['punta']): (cid, v) for cid, v in cl.items() if cid.startswith('MV-B')}
for m, x in sorted(datos.items()):
    for b in list(x['aprobados']):
        if b['core'] not in mover:
            continue
        x['aprobados'].remove(b)
        if mover[b['core']]['mundo'] == m:
            x.setdefault('rechazados', []).append(dict(b, motivo='Su ancla %s pasa a %s (pasada D): la arista queda dentro del mundo.' % (b['core'], m)))
            continue
        cid, v = reanclas[(m, b['core'], b['dominio'])]
        r = res[cid]
        if r['eleccion'] == 'NINGUNO':
            raise SystemExit('%s sin ancla nueva' % cid)
        assert r['eleccion'] in v['candidatos'], (cid, r['eleccion'])
        x.setdefault('rechazados', []).append(dict(b, motivo='Su ancla %s sale del nucleo a %s (pasada D): el puente se reancla en %s.' % (b['core'], mover[b['core']]['mundo'], r['eleccion'])))
        if not any(y['core'] == r['eleccion'] and y['dominio'] == b['dominio'] for y in x['aprobados']):
            x['aprobados'].append({'core': r['eleccion'], 'dominio': b['dominio'], 'score': score(r['eleccion'], b['dominio']), 'reanclado_de': b['core'],
                                   'lectura': 'Pasada MV del saneamiento (%s, %s): %s' % (cid, r['decidido_por'], r['nota'])})
        if (r['eleccion'], b['dominio']) not in EXISTE:
            EXISTE.add((r['eleccion'], b['dominio']))
            op('TEJER', r['eleccion'], b['dominio'], r['nota'], 'Pasada MV del saneamiento (%s, %s)' % (cid, r['decidido_por']), 'el puente se ancla en el nucleo.')
        op('QUITAR', b['core'], b['dominio'], 'Arista de mundo a mundo: su ancla sale del nucleo y el puente se reancla en %s.' % r['eleccion'],
           'Pasada D y MV del saneamiento (%s)' % cid, 'la arista vieja que el reanclaje reemplaza sale.')
# 4
cuenta = collections.Counter((m, b['core']) for m, x in datos.items() for b in x['aprobados'])
aristas = [(cid, v, res[cid]) for cid, v in cl.items() if cid.startswith('MV-A')]
for cid, v, r in sorted(aristas, key=lambda t: (-t[2]['fuerza'], -score(t[1]['core'], t[1]['mundo']))):
    a, w, m = v['core'], v['mundo'], v['dominio']
    if r['eleccion'] == 'PUENTE' and cuenta[(m, a)] < 2:
        cuenta[(m, a)] += 1
        datos[m]['aprobados'].append({'core': a, 'dominio': w, 'score': score(a, w), 'declarado_de_arista_existente': True, 'fuerza_leida': r['fuerza'],
                                      'lectura': 'Pasada MV del saneamiento (%s, %s): %s' % (cid, r['decidido_por'], r['nota'])})
    else:
        motivo = r['nota'] if r['eleccion'] == 'RETIRAR' else 'Puente legitimo, pero el ancla %s ya lleva 2 puentes a %s (ley del ancla).' % (a, m)
        op('QUITAR', a, w, motivo, 'Pasada MV del saneamiento (%s, %s)' % (cid, r['decidido_por']), 'la arista del nucleo al mundo que no es puente sale.')
# 5
pares = []
for cid, v in sorted(cl.items()):
    if not cid.startswith('MV-C'):
        continue
    r = res[cid]
    if r['eleccion'] == 'NINGUNO':
        raise SystemExit('%s sin predecesor' % cid)
    assert r['eleccion'] in v['candidatos'], (cid, r['eleccion'])
    if r['eleccion'] in (nod[v['punta']].get('nodos_siguientes') or []):
        pares.append(cid)
        continue
    op('TEJER', r['eleccion'], v['punta'], r['nota'], 'Pasada MV del saneamiento (%s, %s)' % (cid, r['decidido_por']),
       'el nodo del nucleo que se queda sin camino por el nucleo recibe un predecesor del nucleo.')
for m, x in datos.items():
    x['nota'] += ' | 2026-09-27: nodos que salen del nucleo a su mundo (pasadas D y MV del saneamiento).'
    io.open(ficheros[m], 'w', encoding='utf-8', newline='\n').write(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
json.dump(corr, io.open('docs/saneamiento/tandas/saneamiento-mv-dominio.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
json.dump(ops, io.open('docs/saneamiento/tandas/saneamiento-mv-aristas.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('dominio', len(corr), '| aristas', len(ops), collections.Counter(o['operacion'] for o in ops), '| pares de ida y vuelta', pares)
print('aprobados por mundo', {m: len(x['aprobados']) for m, x in sorted(datos.items())})
