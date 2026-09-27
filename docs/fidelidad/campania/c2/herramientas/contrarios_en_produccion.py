# -*- coding: utf-8 -*-
"""Comprueba que cada CONTRARIO conocido tiene su correccion declarada en el nodo en main.

Uso: python contrarios_en_produccion.py <repo_fidelidad> <repo_correcciones> <muestreo_contrarios.json>
Fuentes de CONTRARIOS: VEREDICTOS_TRAMO1.jsonl, c2/VEREDICTOS_CAMPANIA.jsonl y los del muestreo (lista aparte).
Un CONTRARIO cuenta como corregido si el nodo lleva en `correcciones` una entrada del campo pasos_accionables
con ese indice. Imprime los que no.
"""
import io
import json
import sys

RF, RC, MUESTREO = sys.argv[1:4]
contrarios = set()
for f in (RF + '/docs/fidelidad/campania/VEREDICTOS_TRAMO1.jsonl', RF + '/docs/fidelidad/campania/c2/VEREDICTOS_CAMPANIA.jsonl'):
    for l in io.open(f, encoding='utf-8'):
        x = json.loads(l)
        if x['veredicto'] == 'CONTRARIO':
            contrarios.add((x['node_id'], int(x['paso'])))
for x in json.load(io.open(MUESTREO, encoding='utf-8')):
    contrarios.add((x['node_id'], int(x['paso'])))
sin = []
for nid, paso in sorted(contrarios):
    d = json.load(io.open('%s/dataset/nodos/%s.json' % (RC, nid), encoding='utf-8'))
    ok = any(c.get('campo') == 'pasos_accionables' and c.get('indice') == paso - 1 for c in d.get('correcciones', []))
    if not ok:
        sin.append((nid, paso, d['pasos_accionables'][paso - 1][:120]))
print('CONTRARIOS conocidos: %d | con correccion declarada en main: %d | SIN corregir: %d' % (len(contrarios), len(contrarios) - len(sin), len(sin)))
for s in sin:
    print('  SIN CORREGIR', s)
sys.exit(1 if sin else 0)
