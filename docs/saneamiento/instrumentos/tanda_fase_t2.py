# -*- coding: utf-8 -*-
"""Tanda de FASE, DOMINIO y COHERENCIA del saneamiento (TANDA 2, puntos 8 y 9, decision del fundador del 26 sep 2026).
- FASE: los nodos que la pasada F (lector con trampas, verificador ciego y arbitro) marco con la fase mal.
- DOMINIO: los 2 que la pasada M marco con el mundo mal.
- COHERENCIA: las 2 condiciones de activacion de `regalos_estrategicos_personalizados` que la pasada M hallo contra el
  propio contenido; se reescriben desde los pasos del nodo.
Uso: python tanda_fase_t2.py <repo> <final de la pasada F>"""
import io
import json
import os
import sys

REPO, FINAL_F = sys.argv[1], sys.argv[2]
os.chdir(REPO)
FECHA = '2026-09-26'
DEC = 'Saneamiento del dataset, TANDA 2 (decision del fundador del 26 sep 2026)'
fin = json.load(io.open(FINAL_F, encoding='utf-8'))
tanda = []
for x in sorted((x for x in fin if not x['fase_ok']), key=lambda x: x['nodo']):
    n = json.load(io.open('dataset/nodos/%s.json' % x['nodo'], encoding='utf-8'))
    tanda.append({'id': 't2-fase-%03d' % (len(tanda) + 1), 'node_id': x['nodo'], 'campo': 'fase_proyecto', 'veredicto': 'FASE',
                  'texto_anterior': n['fase_proyecto'], 'texto_nuevo': x['fase_propuesta'],
                  'cita': {'instrumento': 'Pasada F del saneamiento (docs/saneamiento/resultados/F)',
                           'evidencia': '%s: %s (%s)' % (x['id'], x['nota'], x['decidido_por'])},
                  'decision': DEC + ', punto 8: pasada de fase sobre los 853 nodos de validacion e ideacion.', 'fecha': FECHA})
M = {x['id']: x for x in json.load(io.open('docs/saneamiento/resultados/M/final.json', encoding='utf-8')) if not x.get('trampa')}
# colaboracion_transporte_ctm (nucleo -> entrega) se RETIENE para el fundador: es ancla de un puente aprobado a quality
# y 4 nodos del nucleo entran por el; sacarlo del nucleo lo cierra tras el mundo de entrega. Es decision de producto.
for nid in ('manufactura_celular',):
    x = M[nid]
    tanda.append({'id': 't2-dominio-%d' % (len(tanda) + 1), 'node_id': nid, 'campo': 'dominio', 'veredicto': 'DOMINIO',
                  'texto_anterior': x['mundo'], 'texto_nuevo': x['dominio_propuesto'],
                  'cita': {'instrumento': 'Pasada M del saneamiento (docs/saneamiento/resultados/M)', 'evidencia': '%s (%s)' % (x['nota'], x['decidido_por'])},
                  'decision': DEC + ', punto 9: corregir los casos de dominio hallados.', 'fecha': FECHA})
n = json.load(io.open('dataset/nodos/regalos_estrategicos_personalizados.json', encoding='utf-8'))
nota = M['regalos_estrategicos_personalizados']['nota']
for i, nuevo in ((1, 'Si se busca reforzar la lealtad de clientes clave con un gesto exclusivo y privado, sin fines publicitarios'),
                 (2, 'Cuando se quiere empezar con 2 o 3 clientes clave antes de escalar la practica')):
    tanda.append({'id': 't2-coherencia-%d' % i, 'node_id': 'regalos_estrategicos_personalizados', 'campo': 'condiciones_activacion',
                  'indice': i, 'veredicto': 'COHERENCIA', 'texto_anterior': n['condiciones_activacion'][i], 'texto_nuevo': nuevo,
                  'cita': {'instrumento': 'Pasada M del saneamiento (docs/saneamiento/resultados/M)', 'evidencia': nota},
                  'decision': DEC + ', punto 9: corregir el caso de condicion hallado; la condicion nueva sale de los pasos del propio nodo.',
                  'fecha': FECHA})
json.dump(tanda, io.open('docs/saneamiento/tandas/saneamiento-t2-fase.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('correcciones', len(tanda))
