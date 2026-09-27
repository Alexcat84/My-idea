# -*- coding: utf-8 -*-
"""Decisiones del fundador del 27 sep 2026, puntos 1 y 2 (saneamiento, cierre de la tanda 2).

1. colaboracion_transporte_ctm pasa del nucleo a entrega (correccion declarada DOMINIO, por la pasada M). Su puente a
   calidad se reancla en el nucleo (pasada C, bloque C-A): el ancla nueva teje la arista y ocupa el renglon del fichero;
   la arista vieja de entrega a calidad sale. collaboration_enablers, que solo entraba por el, recibe un predecesor del
   nucleo (C-B). Las 4 aristas del nucleo que le llegan (C-C1 a C-C4): PUENTE se declara en el fichero de entrega
   (ley del ancla en 2) y RETIRAR sale.
2. El puente gestion_de_conflictos_cofundadores -> enfoque_situacional_vs_personal se rechaza: pasa a `rechazados` y la
   arista sale (el nodo conserva sus otras entradas de su mundo).
Escribe las dos tandas (aristas y correcciones) y los ficheros de puentes; no toca dataset/nodos.
Uso: python tanda_colaboracion.py <repo> <resultado C> <claves C>"""
import collections
import io
import json
import math
import os
import sys

REPO, RES, CLAVES = sys.argv[1], sys.argv[2], sys.argv[3]
os.chdir(REPO)
res = {x['id']: x for x in json.load(io.open(RES, encoding='utf-8'))}
claves = json.load(io.open(CLAVES, encoding='utf-8'))
FECHA = '2026-09-27'
DEC = 'Decisiones del fundador del 27 sep 2026'
M = 'colaboracion_transporte_ctm'
Q = 'equipo_conjunto_de_mejora_con_proveedores'
idx = json.load(io.open('web/lib/assets/semantic_index.json', encoding='utf-8'))
vec = dict(zip(idx['ids'], idx['embeddings']))


def score(a, b):
    x, y = vec[a], vec[b]
    return round(sum(p * q for p, q in zip(x, y)) / (math.sqrt(sum(p * p for p in x)) * math.sqrt(sum(q * q for q in y))), 4)


def leer(p):
    return json.load(io.open(p, encoding='utf-8'))


def escribir(p, d):
    io.open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


ops = []


def op(o, a, b, motivo, evidencia, decision):
    ops.append({'id': 'd27-arista-%02d' % (len(ops) + 1), 'operacion': o, 'desde': a, 'hacia': b, 'motivo': motivo,
                'evidencia': evidencia, 'decision': DEC + ', ' + decision, 'fecha': FECHA})


# 1. el puente a calidad, reanclado en el nucleo
fq = 'packs/quality/metadata/bridges_aprobados.json'
dq = leer(fq)
ancla = res['C-A']['eleccion']
assert ancla in claves['C-A']['candidatos'], ancla
viejo = next(b for b in dq['aprobados'] if b['core'] == M and b['dominio'] == Q)
dq['aprobados'].remove(viejo)
dq.setdefault('rechazados', []).append(dict(viejo, motivo='%s pasa a entrega (decision del fundador del 27 sep 2026): el puente se reancla en %s.' % (M, ancla)))
assert sum(1 for b in dq['aprobados'] if b['core'] == ancla) < 2, 'ley del ancla'
dq['aprobados'].append({'core': ancla, 'dominio': Q, 'score': score(ancla, Q), 'reanclado_de': M,
                        'lectura': 'Pasada C del saneamiento (C-A, %s): %s' % (res['C-A']['decidido_por'], res['C-A']['nota'])})
op('TEJER', ancla, Q, res['C-A']['nota'], 'Pasada C del saneamiento (C-A, %s)' % res['C-A']['decidido_por'], 'punto 1: el puente a calidad se ancla en el nucleo.')
op('QUITAR', M, Q, 'El puente a calidad deja de salir de %s, que pasa a entrega; lo reemplaza %s -> %s.' % (M, ancla, Q),
   'Decision del fundador del 27 sep 2026, punto 1', 'punto 1: la arista de entrega a calidad que el reanclaje reemplaza sale.')
dq['nota'] += ' | 2026-09-27: el puente de %s se reancla en %s (%s pasa a entrega).' % (M, ancla, M)

# collaboration_enablers, un predecesor del nucleo
pre = res['C-B']['eleccion']
assert pre in claves['C-B']['candidatos'], pre
op('TEJER', pre, 'collaboration_enablers', res['C-B']['nota'], 'Pasada C del saneamiento (C-B, %s)' % res['C-B']['decidido_por'],
   'punto 1: el nodo del nucleo que solo entraba por %s recibe un predecesor del nucleo.' % M)

# las 4 aristas del nucleo que llegan a el
fe = 'packs/entrega/metadata/bridges_aprobados.json'
de = leer(fe)
cuenta = collections.Counter(b['core'] for b in de['aprobados'])
for cid in ('C-C1', 'C-C2', 'C-C3', 'C-C4'):
    a, r = claves[cid]['core'], res[cid]
    if r['eleccion'] == 'PUENTE' and cuenta[a] < 2:
        cuenta[a] += 1
        de['aprobados'].append({'core': a, 'dominio': M, 'score': score(a, M), 'declarado_de_arista_existente': True,
                                'lectura': 'Pasada C del saneamiento (%s, %s): %s' % (cid, r['decidido_por'], r['nota'])})
    else:
        motivo = r['nota'] if r['eleccion'] == 'RETIRAR' else 'Puente legitimo pero el ancla %s ya lleva 2 puentes a entrega (ley del ancla).' % a
        op('QUITAR', a, M, motivo, 'Pasada C del saneamiento (%s, %s)' % (cid, r['decidido_por']), 'punto 1: la arista del nucleo a entrega que no es puente sale.')
de['nota'] += ' | 2026-09-27: %s entra a entrega; sus aristas del nucleo, leidas (pasada C).' % M

# 2. el puente rechazado
fh = 'packs/health_safety/metadata/bridges_aprobados.json'
dh = leer(fh)
A, B = 'gestion_de_conflictos_cofundadores', 'enfoque_situacional_vs_personal'
b = next(b for b in dh['aprobados'] if b['core'] == A and b['dominio'] == B)
dh['aprobados'].remove(b)
dh.setdefault('rechazados', []).append(dict(b, motivo='Rechazado por el fundador el 27 sep 2026: los dos lectores de la pasada P lo juzgaron debil (trampa P2-08).'))
dh['nota'] += ' | 2026-09-27: rechazado %s -> %s (decision del fundador).' % (A, B)
op('QUITAR', A, B, 'Los dos lectores de la pasada P juzgaron debil este puente: los conflictos entre cofundadores no llevan al enfoque situacional de la seguridad.',
   'Pasada P del saneamiento (P2-08)', 'punto 2: se rechaza el puente.')

for p, d in ((fq, dq), (fe, de), (fh, dh)):
    escribir(p, d)
json.dump(ops, io.open('docs/saneamiento/tandas/saneamiento-d27-aristas.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
n = leer('dataset/nodos/%s.json' % M)
x = {m['id']: m for m in leer('docs/saneamiento/resultados/M/final.json')}[M]
corr = [{'id': 'd27-dominio-1', 'node_id': M, 'campo': 'dominio', 'veredicto': 'DOMINIO', 'texto_anterior': n['dominio'], 'texto_nuevo': 'entrega',
         'cita': {'instrumento': 'Pasada M del saneamiento (docs/saneamiento/resultados/M)', 'evidencia': '%s (%s)' % (x['nota'], x['decidido_por'])},
         'decision': DEC + ', punto 1: colaboracion_transporte_ctm pasa a entrega.', 'fecha': FECHA}]
json.dump(corr, io.open('docs/saneamiento/tandas/saneamiento-d27-dominio.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('aristas', len(ops), collections.Counter(o['operacion'] for o in ops), '| puentes entrega', len(de['aprobados']), '| quality', len(dq['aprobados']), '| h&s', len(dh['aprobados']))
