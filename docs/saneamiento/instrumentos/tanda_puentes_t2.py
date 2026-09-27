# -*- coding: utf-8 -*-
"""Construye la tanda de PUENTES del saneamiento (TANDA 2, punto 9, decision del fundador del 26 sep 2026).

1. Ley del ancla en 2: ninguna ancla del nucleo lleva mas de 2 puentes aprobados por mundo. Donde hay 3, sale el de
   menor score (pasa a `rechazados` con su motivo).
2. Los puentes aprobados que el grafo no teje se TEJEN (nucleo -> mundo), y salen las aristas viejas que el reanclaje
   reemplazo (docs/_reanclaje_puentes.json: ancla_vieja -> nodo_del_mundo), si siguen vivas.
3. Las aristas del nucleo a un mundo que ningun fichero declara, leidas en la pasada P: PUENTE se declara en el
   fichero del mundo (con su score semantico y `declarado_de_arista_existente`), dentro de la ley del ancla (si una
   ancla se pasaria de 2, entran las de mas fuerza y, a igual fuerza, mas score; las demas se RETIRAN); RETIRAR sale
   del grafo.
Escribe los ficheros bridges_aprobados.json de cada mundo y la tanda de aristas; no toca dataset/nodos (eso lo hace
scripts/saneamiento/aplicar_aristas.py). Uso: python tanda_puentes_t2.py <repo> <final de la pasada P>"""
import collections
import glob
import io
import json
import math
import os
import sys

REPO, FINAL_P = sys.argv[1], sys.argv[2]
os.chdir(REPO)
sys.path.insert(0, 'scripts')
from run_phase1 import aristas_a_simetrizar  # noqa: E402

nodos = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    nodos[n['node_id']] = n
vivos = {k for k, n in nodos.items() if not n.get('deprecado')}
dom = {k: n['dominio'] for k, n in nodos.items()}
E = aristas_a_simetrizar(nodos)
idx = json.load(io.open('web/lib/assets/semantic_index.json', encoding='utf-8'))
vec = dict(zip(idx['ids'], idx['embeddings']))


def score(a, b):
    x, y = vec[a], vec[b]
    return round(sum(p * q for p, q in zip(x, y)) / (math.sqrt(sum(p * p for p in x)) * math.sqrt(sum(q * q for q in y))), 4)


FECHA = '2026-09-26'
DEC = 'Saneamiento del dataset, TANDA 2, punto 9 (decision del fundador del 26 sep 2026)'
ficheros = {os.path.basename(os.path.dirname(os.path.dirname(p))): p for p in glob.glob('packs/*/metadata/bridges_aprobados.json')}
datos = {d: json.load(io.open(p, encoding='utf-8')) for d, p in ficheros.items()}
ops = []


def op(o, a, b, motivo, evidencia, decision):
    ops.append({'id': 't2-puente-%03d' % (len(ops) + 1), 'operacion': o, 'desde': a, 'hacia': b, 'motivo': motivo,
                'evidencia': evidencia, 'decision': DEC + ': ' + decision, 'fecha': FECHA})


# 1. ley del ancla en 2
for d, x in sorted(datos.items()):
    por_ancla = collections.defaultdict(list)
    for b in x['aprobados']:
        por_ancla[b['core']].append(b)
    for ancla, bs in sorted(por_ancla.items()):
        if len(bs) > 2:
            for b in sorted(bs, key=lambda b: b.get('score', 0))[:len(bs) - 2]:
                x['aprobados'].remove(b)
                x.setdefault('rechazados', []).append(dict(b, motivo='Ley del ancla en 2 (saneamiento, tanda 2, 26 sep 2026): el ancla %s llevaba %d puentes; sale el de menor score.' % (ancla, len(bs))))
                print('ley del ancla: sale', d, ancla, '->', b['dominio'])

# 2. tejer los aprobados que faltan y retirar lo que el reanclaje reemplazo. Un aprobado cuya arista juzgo RANCIA la
# pasada R (lectura ciega con verificador y arbitro, posterior a la curaduria por score) y quito saneamiento-t2-aristas
# no se vuelve a tejer: pasa a `rechazados` con el motivo de R.
rancias_R = {(o['desde'], o['hacia']): o for o in json.load(io.open('docs/saneamiento/tandas/saneamiento-t2-aristas.json', encoding='utf-8')) if o['operacion'] == 'QUITAR'}
for d, x in sorted(datos.items()):
    for b in list(x['aprobados']):
        o = rancias_R.get((b['core'], b['dominio']))
        if o:
            x['aprobados'].remove(b)
            x.setdefault('rechazados', []).append(dict(b, motivo='Arista juzgada rancia en la pasada R del saneamiento (%s): %s' % (o['id'], o['motivo'])))
            print('aprobado rancio por R, a rechazados:', d, b['core'], '->', b['dominio'])
reancl = json.load(io.open('docs/_reanclaje_puentes.json', encoding='utf-8'))['cambios']
for d, x in sorted(datos.items()):
    for b in x['aprobados']:
        a, w = b['core'], b['dominio']
        if (a, w) not in E:
            op('TEJER', a, w, 'Puente aprobado en packs/%s/metadata/bridges_aprobados.json que el grafo no tejia.' % d,
               'AUD-09 M51 y M53; ficha puentes-reanclados-sin-tejer (docs/PENDIENTES.md)', 'tejer los puentes aprobados.')
for c in reancl:
    a, w = c['ancla_vieja'], c['nodo_del_mundo']
    if (a, w) in E and a in vivos and dom.get(a) != 'core':
        op('QUITAR', a, w, 'Arista vieja de mundo a mundo que el reanclaje del %s reemplazo por %s.' % (c['pack'], c['ancla_nueva']),
           'docs/_reanclaje_puentes.json (cambios); AUD-09 M51', 'retirar las aristas que los puentes reanclados reemplazan.')

# 3. las 61 aristas sin declarar (medidas antes de saneamiento-t2-aristas: la que esa tanda ya quito no se repite, y
# un PUENTE cuya arista quito la pasada R se lista aparte para decidirlo, no se declara a ciegas)
fin = json.load(io.open(FINAL_P, encoding='utf-8'))
ya_quitadas = [x for x in fin if (x['core'], x['mundo']) not in E]
for x in ya_quitadas:
    print('ya quitada por saneamiento-t2-aristas:', x['id'], x['veredicto'], x['core'], '->', x['mundo'])
fin = [x for x in fin if (x['core'], x['mundo']) in E]
cuenta = collections.Counter((d, b['core']) for d, x in datos.items() for b in x['aprobados'])
puentes = sorted((x for x in fin if x['veredicto'] == 'PUENTE'), key=lambda x: (-x['fuerza'], -score(x['core'], x['mundo'])))
for x in puentes:
    a, w, d = x['core'], x['mundo'], x['dominio']
    if cuenta[(d, a)] >= 2:
        op('QUITAR', a, w, 'Puente legitimo pero el ancla %s ya lleva 2 puentes a %s (ley del ancla); quedan los de mas fuerza.' % (a, d),
           'Pasada P (%s, fuerza %d): %s' % (x['id'], x['fuerza'], x['nota']), 'ley del ancla en 2.')
        continue
    cuenta[(d, a)] += 1
    datos[d]['aprobados'].append({'core': a, 'dominio': w, 'score': score(a, w), 'declarado_de_arista_existente': True,
                                  'fuerza_leida': x['fuerza'], 'lectura': 'Pasada P del saneamiento (%s): %s' % (x['id'], x['nota'])})
for x in fin:
    if x['veredicto'] == 'RETIRAR':
        op('QUITAR', x['core'], x['mundo'], x['nota'], 'Pasada P del saneamiento (%s, %s)' % (x['id'], x['decidido_por']),
           'retirar las aristas del nucleo a un mundo que no son puente.')
for d, x in datos.items():
    x['nota'] = x['nota'] + ' | 2026-09-26: saneamiento, tanda 2, punto 9: ley del ancla en 2, aprobados tejidos en el grafo y aristas del nucleo sin declarar leidas (docs/SANEAMIENTO_DATASET.md).'
    io.open(ficheros[d], 'w', encoding='utf-8', newline='\n').write(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
json.dump(ops, io.open('docs/saneamiento/tandas/saneamiento-t2-puentes.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('operaciones', len(ops), collections.Counter(o['operacion'] for o in ops))
print('aprobados por mundo', {d: len(x['aprobados']) for d, x in sorted(datos.items())})
