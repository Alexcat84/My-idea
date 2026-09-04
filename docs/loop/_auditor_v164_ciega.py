# -*- coding: utf-8 -*-
"""CIEGA DEL AUDITOR, VUELTA 165. Imprime los nodos SIN clase, SIN via y SIN
razon. La razon del registro NO se toca aqui: se destapa despues, con
_auditor_v165_ciega_reveal.py, y solo cuando el sello ya existe."""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

G = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))
NODOS = G['nodes'] if 'nodes' in G else G['nodos']

PARES = [
    ('LD-OPC05-101', 'lienzo_modelo_negocio', 'search_for_business_model'),
    ('LD-OPC05-005', 'aim_of_leadership', 'causas_comunes_vs_especiales'),
]

CAMPOS = ['titulo_concepto', 'fuente', 'fase_proyecto', 'entregable_esperado', 'resumen_teorico',
          'condiciones_activacion', 'pasos_accionables', 'deprecado']

def pinta(nid):
    n = NODOS[nid]
    print('  NODO: %s' % nid)
    for c in CAMPOS:
        if c not in n:
            continue
        v = n[c]
        if isinstance(v, list):
            print('    %s:' % c)
            for i, x in enumerate(v, 1):
                print('      %2d. %s' % (i, x))
        else:
            print('    %s: %s' % (c, v))
    print()

for cid, a, b in PARES:
    print('=' * 78)
    print('PAR %s  (los dos nodos, enteros, sin clase y sin razon)' % cid)
    print('=' * 78)
    pinta(a)
    pinta(b)
