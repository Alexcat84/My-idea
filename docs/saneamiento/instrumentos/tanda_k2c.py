# -*- coding: utf-8 -*-
"""Nivel 1, criterio 12: las correcciones de los 4 nodos incoherentes de la pasada K2, contra su libro (dos lectores
ciegos con el libro y un arbitro con cita literal). Veredicto COHERENCIA. El texto anterior que copiaron los lectores es
de antes de la ortografia: si hoy solo difiere en tildes o enie, vale el de hoy. Uso: python tanda_k2c.py <repo> <final>"""
import io
import json
import os
import sys
import unicodedata

os.chdir(sys.argv[1])
fin = json.load(io.open(sys.argv[2], encoding='utf-8'))['final']
LIBRO = {'Franchise Your Business - Mark Siebert': 'Franchise Your Business (Siebert)',
         "Juran's Quality Handbook_ The C - Joseph A. Defeo": "Juran's Quality Handbook"}


def plano(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', ' '.join(s.split())) if not unicodedata.combining(c)).lower()


tanda, fallos = [], []
for x in fin:
    n = json.load(io.open('dataset/nodos/%s.json' % x['node_id'], encoding='utf-8'))
    campo = x['campo']
    hoy = n[campo][x['indice']] if isinstance(n[campo], list) else n[campo]
    if plano(hoy) != plano(x['texto_anterior']):
        fallos.append('%s.%s[%s]' % (x['node_id'], campo, x['indice']))
        continue
    nuevo = ' '.join(x['texto_nuevo'].replace(chr(0x2014), ',').replace(chr(0x2013), '-').split())
    c = {'id': 'n1-coherencia-%02d' % (len(tanda) + 1), 'node_id': x['node_id'], 'campo': campo, 'veredicto': 'COHERENCIA',
         'texto_anterior': hoy, 'texto_nuevo': nuevo,
         'cita': {'instrumento': 'Pasada K2 del saneamiento y correccion contra el libro (docs/saneamiento/resultados/K2c)',
                  'evidencia': '%s, lineas %s: "%s". %s' % (LIBRO[n['fuente']], x['cita_lineas'], x['cita_frase'], x['nota'])},
         'decision': 'Saneamiento del dataset, nivel 1 (decision del fundador del 27 sep 2026), criterio 12: el residuo de coherencia interna, corregido contra su libro.',
         'fecha': '2026-09-27'}
    if isinstance(n[campo], list):
        c['indice'] = x['indice']
    tanda.append(c)
json.dump(tanda, io.open('docs/saneamiento/tandas/saneamiento-n1-coherencia.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('correcciones', len(tanda), 'en', len({c['node_id'] for c in tanda}), 'nodos | sin casar', fallos)
