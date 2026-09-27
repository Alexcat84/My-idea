# -*- coding: utf-8 -*-
"""Integracion del mundo 11 (decision del fundador, 28 sep 2026): `notas_extraccion` es un campo INTERNO.

Las notas de extraccion de la forja (unidad de origen, rutas, lineas, razonamiento del extractor, marcas de
discutible) se mudan del resumen a `notas_extraccion`, y ese campo jamas llega a la web ni a la IA: la vista web
de scripts/sync_assets_web.py lo quita, igual que `fuente` o `correcciones`, y la guarda del navegador
(web/lib/assets/sinInternos.test.ts) lo cuenta como clave interna.

    python engine/test_notas_extraccion_internas.py
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'scripts'))
import sync_assets_web as s  # noqa: E402

fallos = []
nodo = {'node_id': 'x', 'resumen_teorico': 'Resumen.', 'notas_extraccion': 'UNIDAD DE ORIGEN: fuentes/x/cap_01.md, lineas 1 a 9.'}
vista = s._vista_web('master_graph.json', {'nodos': {'x': dict(nodo)}})
if 'notas_extraccion' in vista['nodos']['x']:
    fallos.append('la vista web deja pasar notas_extraccion')
if 'notas_extraccion' not in s.CLAVES_INTERNAS_NODO:
    fallos.append('notas_extraccion no esta entre las claves internas del nodo (el chequeo de gemelos de Gate 0 no la vigilaria)')
guarda = open(os.path.join(RAIZ, 'web', 'lib', 'assets', 'sinInternos.test.ts'), encoding='utf-8').read()
bloque = re.search(r'const CLAVES_INTERNAS = new Set\(\[(.*?)\]\)', guarda, re.S)
if not bloque or '"notas_extraccion"' not in bloque.group(1):
    fallos.append('la guarda del navegador (sinInternos.test.ts) no cuenta notas_extraccion como clave interna')
if fallos:
    print('ROJO:')
    for f in fallos:
        print('  ' + f)
    sys.exit(1)
print('VERDE: notas_extraccion es interna: la vista web la quita, Gate 0 la vigila y la guarda del navegador la cuenta')
