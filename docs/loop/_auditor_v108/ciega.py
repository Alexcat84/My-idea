# -*- coding: utf-8 -*-
"""Volcado CIEGO: los dos nodos enteros con el paso_casado marcado.
NO imprime direccion_leida, ni razon, ni vara, ni correccion_vNN, ni veredicto."""
import json, sys
g=json.load(open('dataset/metadata/master_graph.json',encoding='utf-8'))['nodos']
tramo=sys.argv[1]; puestos=[int(x) for x in sys.argv[2:]]
filas={}
for ln in open(tramo,encoding='utf-8'):
    ln=ln.strip()
    if not ln: continue
    o=json.loads(ln)
    filas[o['puesto_tramo']]=o
def pinta(nid, etiqueta, marcado=None):
    n=g.get(nid)
    print('  %s: %s' % (etiqueta, nid))
    if not n: print('    (NO ESTA EN EL GRAFO)'); return
    print('    titulo: %s' % n.get('titulo_concepto'))
    r=n.get('resumen') or n.get('descripcion') or ''
    if r: print('    resumen: %s' % r)
    pasos=n.get('pasos_accionables') or []
    for i,p in enumerate(pasos,1):
        txt=p if isinstance(p,str) else json.dumps(p,ensure_ascii=False)
        marca='  <<< PASO CASADO' if marcado==i else ''
        print('    paso %d: %s%s' % (i,txt,marca))
    ent=n.get('entregable_esperado')
    if ent: print('    entregable: %s' % ent)
for p in puestos:
    o=filas[p]
    print('='*100)
    print('PUESTO %d  (dominio %s, paso_casado %s)' % (p, o.get('dominio'), o.get('paso_casado')))
    print('='*100)
    pinta(o['madre_de_la_bolsa'],'MADRE', o.get('paso_casado'))
    print()
    pinta(o['hijo_de_la_bolsa'],'HIJO')
    print()
