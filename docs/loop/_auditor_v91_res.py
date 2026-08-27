# -*- coding: utf-8 -*-
"""VARA PROPIA: resuelve las cadenas de alias de los dos YA_ESTABA de OP-E-07
caminando ids_alias sobre el grafo de APERTURA (675b9969), no sobre el de hoy."""
import json, io, sys
G = json.load(io.open(sys.argv[1], encoding='utf-8'))['nodos']
ALIAS = {a: k for k, v in G.items() for a in (v.get('ids_alias') or [])}
def res(x):
    cadena = [x]; visto = set()
    while x in ALIAS and x not in visto:
        visto.add(x); x = ALIAS[x]; cadena.append(x)
    return x, cadena
for nid in ['fases_de_retencion_de_clientes', 'ocho_fases_experiencia_cliente',
            'fase_acclimate_experiencia_cliente', 'control_exportaciones_bis',
            'regulaciones_exportacion_ear', 'export_administration_regulations']:
    r, cad = res(nid)
    print('%-48s -> %-42s  cadena: %s | vivo: %s' % (nid, r, ' -> '.join(cad),
          'SI' if (r in G and not G[r].get('deprecado')) else 'NO/deprecado'))
