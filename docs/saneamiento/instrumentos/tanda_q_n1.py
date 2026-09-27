# -*- coding: utf-8 -*-
"""Nivel 1, criterios 14 y 15 (decision del fundador del 27 sep 2026): la tanda de la pasada Q.
  - condiciones de activacion: cada condicion mal leida se reescribe desde el propio contenido del nodo (veredicto
    COHERENCIA); el texto es el del arbitro si lo hubo, si no el del verificador ciego, si no el del lector;
  - fase (planificacion y ejecucion): veredicto FASE;
  - dominio: veredicto DOMINIO, SOLO los cambios que no sacan un nodo del nucleo. Sacar un nodo del nucleo lo cierra
    tras un mundo (decision de producto, como colaboracion_transporte_ctm el 27 sep): esos se listan para el fundador.
Uso: python tanda_q_n1.py <repo> <final de la pasada Q>"""
import io
import json
import os
import sys

REPO, FINAL = sys.argv[1], sys.argv[2]
os.chdir(REPO)
fin = json.load(io.open(FINAL, encoding='utf-8'))
FECHA = '2026-09-27'
DEC = 'Saneamiento del dataset, nivel 1 (decision del fundador del 27 sep 2026), criterios 14 y 15'
INST = 'Pasada Q del saneamiento (docs/saneamiento/resultados/Q)'
tanda, retenidos = [], []


def nodo(nid):
    return json.load(io.open('dataset/nodos/%s.json' % nid, encoding='utf-8'))


for x in sorted(fin, key=lambda x: x['nodo']):
    n = nodo(x['nodo'])
    ev = '%s: %s (%s)' % (x['id'], x['nota'], x['decidido_por'])
    if not x['condiciones_ok']:
        conds = n['condiciones_activacion']
        vistos = set()
        for c in x['condiciones_malas']:
            i = c['indice']
            if i in vistos or not 0 <= i < len(conds):
                continue
            vistos.add(i)
            nuevo = ' '.join(c['texto_nuevo'].replace(chr(0x2014), ',').replace(chr(0x2013), '-').split())
            if nuevo == conds[i]:
                continue
            tanda.append({'id': 'n1-condicion-%03d' % (len(tanda) + 1), 'node_id': x['nodo'], 'campo': 'condiciones_activacion',
                          'indice': i, 'veredicto': 'COHERENCIA', 'texto_anterior': conds[i], 'texto_nuevo': nuevo,
                          'cita': {'instrumento': INST, 'evidencia': '%s Motivo: %s' % (ev, c['motivo'])},
                          'decision': DEC + ': las condiciones de activacion dicen cuando aplica de verdad el nodo.', 'fecha': FECHA})
    if not x['fase_ok'] and x['fase_propuesta'] != n['fase_proyecto'] and n['fase_proyecto'] in ('planificacion', 'ejecucion'):
        tanda.append({'id': 'n1-fase-%03d' % (len(tanda) + 1), 'node_id': x['nodo'], 'campo': 'fase_proyecto', 'veredicto': 'FASE',
                      'texto_anterior': n['fase_proyecto'], 'texto_nuevo': x['fase_propuesta'], 'cita': {'instrumento': INST, 'evidencia': ev},
                      'decision': DEC + ': fase de los nodos de planificacion y ejecucion.', 'fecha': FECHA})
    if not x['dominio_ok'] and x['dominio_propuesto'] != n['dominio']:
        if n['dominio'] == 'core':
            retenidos.append({'nodo': x['nodo'], 'de': 'core', 'a': x['dominio_propuesto'], 'nota': x['nota'], 'decidido_por': x['decidido_por']})
            continue
        tanda.append({'id': 'n1-dominio-%03d' % (len(tanda) + 1), 'node_id': x['nodo'], 'campo': 'dominio', 'veredicto': 'DOMINIO',
                      'texto_anterior': n['dominio'], 'texto_nuevo': x['dominio_propuesto'], 'cita': {'instrumento': INST, 'evidencia': ev},
                      'decision': DEC + ': dominio en todo el catalogo (los que no sacan un nodo del nucleo).', 'fecha': FECHA})
json.dump(tanda, io.open('docs/saneamiento/tandas/saneamiento-n1-q.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
json.dump(retenidos, io.open('docs/saneamiento/resultados/Q/retenidos_nucleo_a_mundo.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
import collections
print('correcciones', len(tanda), collections.Counter(c['veredicto'] for c in tanda), '| retenidos del nucleo a un mundo', len(retenidos))
