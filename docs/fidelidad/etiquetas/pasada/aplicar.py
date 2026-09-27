# -*- coding: utf-8 -*-
"""Escribe (solo la sesion escribe) las correcciones de la pasada de etiquetas en la lista de fidelidad del repo,
y el informe de la pasada en docs/fidelidad/etiquetas/.
Uso: python aplicar.py <W> <repo> [extra.json]
extra.json: hallazgos adicionales ya decididos (verificador extra + arbitro), con la misma forma que hallazgos.json."""
import io
import json
import os
import sys

W, REPO = sys.argv[1], sys.argv[2]
hallazgos = json.load(io.open(W + '/hallazgos.json', encoding='utf-8'))
if len(sys.argv) > 3:
    hallazgos += json.load(io.open(sys.argv[3], encoding='utf-8'))
ajustes = json.load(io.open(W + '/ajustes_sesion.json', encoding='utf-8'))
g = json.load(io.open(REPO + '/dataset/metadata/master_graph.json', encoding='utf-8'))['nodos']
ruta_lista = REPO + '/dataset/metadata/etiquetas_de_cara_v1_fidelidad.json'
lista = json.load(io.open(ruta_lista, encoding='utf-8'))

filas, fallos = [], []
for h in hallazgos:
    k, d = h['node_id'], h['hallazgo']
    n = g[k]
    vieja = h['etiqueta']
    if n['etiqueta_arbol'] != vieja:
        fallos.append('%s: el grafo dice %r y la pasada leyo %r' % (k, n['etiqueta_arbol'], vieja))
    fuente = n['titulo_concepto'] + ' ' + ' '.join(n['resumen_teorico'].split())
    cita_ok = d['cita'] in fuente
    if not cita_ok:
        fallos.append('%s: cita no literal: %r' % (k, d['cita']))
    nueva = ajustes.get(k, d['etiqueta_propuesta'])
    if len(nueva.split()) > 6:
        fallos.append('%s: la nueva pasa de 6 palabras: %r' % (k, nueva))
    motivo = "decia '%s'; %s: %s (cita del nodo: '%s'). Pasada de etiquetas del 25 sep 2026, %s." % (
        vieja, d['veredicto'], d['razon'].rstrip('.'), d['cita'], h['decidido_por'])
    lista['_motivos'][k] = motivo
    lista[k] = nueva
    filas.append({'id_pasada': h['id'], 'node_id': k, 'titulo': n['titulo_concepto'], 'antes': vieja, 'despues': nueva,
                  'veredicto': d['veredicto'], 'cita': d['cita'], 'razon': d['razon'], 'decidido_por': h['decidido_por'],
                  'propuesta_del_lector': d['etiqueta_propuesta'], 'ajustada_por_la_sesion': k in ajustes})
if fallos:
    print('NO APLICO:')
    for f in fallos:
        print('  ' + f)
    sys.exit(1)
io.open(ruta_lista, 'w', encoding='utf-8', newline='\n').write(json.dumps(lista, ensure_ascii=False, indent=2) + '\n')
os.makedirs(REPO + '/docs/fidelidad/etiquetas', exist_ok=True)
json.dump(filas, io.open(REPO + '/docs/fidelidad/etiquetas/CORRECCIONES_PASADA_ETIQUETAS.json', 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('corregidas:', len(filas), '| CONTRARIA', sum(f['veredicto'] == 'CONTRARIA' for f in filas), '| DISTINTA', sum(f['veredicto'] == 'DISTINTA' for f in filas))
